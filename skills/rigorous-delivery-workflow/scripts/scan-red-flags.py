#!/usr/bin/env python3
"""Scan delivery artifacts for vague markers and unfinished work."""

from __future__ import annotations

import argparse
import os
import re
import subprocess
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

DOC_SUFFIXES = {".md", ".txt", ".rst"}
CODE_SUFFIXES = {
    ".py", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".json", ".yaml", ".yml",
    ".toml", ".ini", ".cfg", ".css", ".scss", ".html", ".sql", ".sh", ".ps1",
}
SKIP_DIRS = {
    ".git", "node_modules", "dist", "build", "coverage", "test-results", "playwright-report",
    "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache",
}


def run_git(args: list[str]) -> list[Path]:
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
    return [Path(line.strip()) for line in result.stdout.splitlines() if line.strip()]


def changed_paths(include_untracked: bool) -> list[Path]:
    paths = run_git(["diff", "--name-only"])
    paths += run_git(["diff", "--name-only", "--cached"])
    if include_untracked:
        paths += run_git(["ls-files", "--others", "--exclude-standard"])
    seen: set[str] = set()
    unique: list[Path] = []
    for path in paths:
        key = str(path)
        if key not in seen:
            seen.add(key)
            unique.append(path)
    return unique


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def is_scannable(path: Path, include_code: bool) -> bool:
    suffixes = DOC_SUFFIXES | (CODE_SUFFIXES if include_code else set())
    return path.suffix.lower() in suffixes


def iter_files(paths: list[Path], include_code: bool) -> tuple[list[Path], list[Path], int]:
    files: list[Path] = []
    missing_paths: list[Path] = []
    skipped = 0
    for path in paths:
        if not path.exists():
            missing_paths.append(path)
            continue
        if should_skip(path):
            skipped += 1
            continue
        if path.is_dir():
            for candidate in path.rglob("*"):
                if should_skip(candidate):
                    continue
                if candidate.is_file() and is_scannable(candidate, include_code):
                    files.append(candidate)
                elif candidate.is_file():
                    skipped += 1
        elif path.is_file() and is_scannable(path, include_code):
            files.append(path)
        elif path.is_file():
            skipped += 1
    return files, missing_paths, skipped


def code_false_positive(path: Path, line: str, pattern_text: str) -> bool:
    if path.suffix.lower() not in CODE_SUFFIXES:
        return False
    lower = line.lower()
    if "red-flag-allow" in lower:
        return True
    if "placeholder" in pattern_text.lower():  # red-flag-allow
        # UI placeholder attributes/properties are legitimate product text, not unfinished work.  # red-flag-allow
        if "placeholder=" in lower or "placeholder:" in lower or "placeholder}" in lower:
            return True
    return False


def scan_file(path: Path, patterns: list[tuple[str, re.Pattern[str]]]) -> list[str]:
    hits: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = path.read_text(encoding="utf-8", errors="replace")
    for lineno, line in enumerate(text.splitlines(), start=1):
        if path.name == "scan-red-flags.py" and "red-flag-allow" in line:
            continue
        for pattern_text, pattern in patterns:
            if pattern.search(line) and not code_false_positive(path, line, pattern_text):
                hits.append(f"{path}:{lineno}: {line.strip()}")
                break
    return hits


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, help="Files or directories to scan")
    parser.add_argument("--changed", action="store_true", help="Scan git changed files")
    parser.add_argument("--include-untracked", action="store_true", help="Include untracked files with --changed")
    parser.add_argument("--include-code", action="store_true", help="Scan common code/config files, not only docs")
    parser.add_argument("--case-sensitive", action="store_true", help="Use case-sensitive matching")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Working directory for changed-file paths")
    args = parser.parse_args()

    root = args.root.resolve()
    os.chdir(root)

    input_paths = list(args.paths)
    if args.changed:
        input_paths.extend(changed_paths(args.include_untracked))

    if not input_paths and args.changed:
        print("[OK] No changed files to scan.")
        return 0

    if not input_paths:
        parser.error("provide paths or use --changed")

    flags = 0 if args.case_sensitive else re.IGNORECASE
    patterns = [(pattern, re.compile(pattern, flags)) for pattern in DEFAULT_PATTERNS]
    files, missing_paths, skipped = iter_files(input_paths, args.include_code)

    if missing_paths:
        print("[FAIL] Missing path(s):", file=sys.stderr)
        for path in missing_paths:
            print(f"- {path}", file=sys.stderr)
        return 2

    if not files:
        print(f"[FAIL] No scannable files found. skipped={skipped}", file=sys.stderr)
        return 2

    all_hits: list[str] = []
    for file in files:
        all_hits.extend(scan_file(file, patterns))

    print(f"[INFO] scanned={len(files)} skipped={skipped} include_code={args.include_code}")
    if all_hits:
        print("[FAIL] Red flags found:")
        for hit in all_hits:
            print(hit)
        return 1

    print("[OK] No red flags found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
