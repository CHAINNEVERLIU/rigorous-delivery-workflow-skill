#!/usr/bin/env python3
"""Scan delivery artifacts for vague markers and unfinished work."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


DEFAULT_PATTERNS = [
    r"\bTBD\b",  # red-flag-allow
    r"\bTODO\b",  # red-flag-allow
    r"placeholder",  # red-flag-allow
    r"implement later",  # red-flag-allow
    r"fill in",  # red-flag-allow
    r"handle edge cases",  # red-flag-allow
    r"add validation",  # red-flag-allow
    r"similar to",  # red-flag-allow
    "\u9002\u5f53",  # red-flag-allow
    "\u540e\u7eed\u518d\u8bf4",  # red-flag-allow
    "\u7b49\u7b49",  # red-flag-allow
    "\u7c7b\u4f3c",  # red-flag-allow
    "\u6309\u9700",  # red-flag-allow
    "\u89c6\u60c5\u51b5",  # red-flag-allow
]


def iter_files(paths: list[Path]) -> tuple[list[Path], list[Path]]:
    files: list[Path] = []
    missing_paths: list[Path] = []
    for path in paths:
        if path.is_dir():
            files.extend(
                p
                for p in path.rglob("*")
                if p.is_file() and p.suffix.lower() in {".md", ".txt", ".rst"}
            )
        elif path.is_file():
            files.append(path)
        else:
            missing_paths.append(path)
    return files, missing_paths


def scan_file(path: Path, patterns: list[re.Pattern[str]]) -> list[str]:
    hits: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = path.read_text(encoding="utf-8", errors="replace")
    for lineno, line in enumerate(text.splitlines(), start=1):
        if path.name == "scan-red-flags.py" and "red-flag-allow" in line:
            continue
        for pattern in patterns:
            if pattern.search(line):
                hits.append(f"{path}:{lineno}: {line.strip()}")
                break
    return hits


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="Files or directories to scan")
    parser.add_argument(
        "--ignore-case",
        action="store_true",
        help="Deprecated; matching is case-insensitive by default",
    )
    parser.add_argument(
        "--case-sensitive",
        action="store_true",
        help="Use case-sensitive matching",
    )
    args = parser.parse_args()

    flags = 0 if args.case_sensitive else re.IGNORECASE
    patterns = [re.compile(pattern, flags) for pattern in DEFAULT_PATTERNS]
    files, missing_paths = iter_files(args.paths)

    if missing_paths:
        print("[FAIL] Missing path(s):", file=sys.stderr)
        for path in missing_paths:
            print(f"- {path}", file=sys.stderr)
        return 2

    if not files:
        print("[FAIL] No scannable files found.", file=sys.stderr)
        return 2

    all_hits: list[str] = []
    for file in files:
        all_hits.extend(scan_file(file, patterns))

    if all_hits:
        print("[FAIL] Red flags found:")
        for hit in all_hits:
            print(hit)
        return 1

    print(f"[OK] No red flags found in {len(files)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
