#!/usr/bin/env python3
"""Print changed and untracked files for delivery review."""

from __future__ import annotations

import argparse
import subprocess
import sys


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
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-untracked", action="store_true", help="Do not include untracked files")
    args = parser.parse_args()

    if not git(["rev-parse", "--show-toplevel"]):
        print("[INFO] Not a git repository.")
        return 0

    changed = git(["diff", "--name-only"]) + git(["diff", "--name-only", "--cached"])
    untracked = [] if args.no_untracked else git(["ls-files", "--others", "--exclude-standard"])

    seen: set[str] = set()
    print("Changed files:")
    for path in changed:
        if path not in seen:
            seen.add(path)
            print(f"M {path}")
    print("Untracked files:")
    for path in untracked:
        if path not in seen:
            seen.add(path)
            print(f"? {path}")
    if not seen:
        print("none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
