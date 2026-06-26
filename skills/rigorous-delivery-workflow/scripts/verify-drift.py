#!/usr/bin/env python3
"""Check git changed files against allowed and forbidden roots."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import PurePosixPath


def git(args: list[str]) -> list[str]:
    try:
        result = subprocess.run(
            ["git", *args],
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        )
    except (OSError, subprocess.CalledProcessError):
        return []
    return [line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip()]


def under(path: str, root: str) -> bool:
    root = root.strip("/").replace("\\", "/")
    path = path.strip("/").replace("\\", "/")
    return path == root or path.startswith(root + "/")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--allow", action="append", default=[], help="Allowed root; repeatable")
    parser.add_argument("--forbid", action="append", default=[], help="Forbidden root; repeatable")
    parser.add_argument("--include-untracked", action="store_true", help="Include untracked files")
    args = parser.parse_args()

    if not git(["rev-parse", "--show-toplevel"]):
        print("[FAIL] Not a git repository.")
        return 2

    files = git(["diff", "--name-only"]) + git(["diff", "--name-only", "--cached"])
    if args.include_untracked:
        files += git(["ls-files", "--others", "--exclude-standard"])

    unique = sorted(set(files), key=lambda p: PurePosixPath(p).as_posix())
    violations: list[str] = []

    for path in unique:
        if any(under(path, root) for root in args.forbid):
            violations.append(f"forbidden: {path}")
            continue
        if args.allow and not any(under(path, root) for root in args.allow):
            violations.append(f"outside-allowed: {path}")

    print(f"[INFO] changed_files={len(unique)}")
    for path in unique:
        print(path)

    if violations:
        print("[FAIL] Drift violations:")
        for item in violations:
            print(item)
        return 1

    print("[OK] Drift check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
