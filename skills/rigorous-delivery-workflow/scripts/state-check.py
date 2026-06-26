#!/usr/bin/env python3
"""Check a delivery state file for required sections and non-empty key fields."""

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_LABELS = [
    "Objective:",
    "Latest User Instruction:",
    "Current Phase:",
    "In Scope:",
    "Out of Scope:",
    "Allowed Paths:",
    "Forbidden Paths:",
    "Review Findings Ledger:",
    "Execution Checklist:",
    "Verification Ledger:",
    "Drift Ledger:",
    "Current Blocker:",
    "Next Single Action:",
]


def has_nonempty_value(text: str, label: str) -> bool:
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        if line.strip() == label:
            for following in lines[idx + 1: idx + 5]:
                stripped = following.strip()
                if stripped and not stripped.endswith(":") and not stripped.startswith("| ---"):
                    return True
            return False
        if line.startswith(label):
            return bool(line[len(label):].strip())
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("state_file", type=Path)
    args = parser.parse_args()

    if not args.state_file.is_file():
        print(f"[FAIL] Missing state file: {args.state_file}")
        return 2

    text = args.state_file.read_text(encoding="utf-8", errors="replace")
    missing = [label for label in REQUIRED_LABELS if label not in text]
    empty = [label for label in REQUIRED_LABELS if label in text and not has_nonempty_value(text, label)]

    if missing or empty:
        print("[FAIL] State file incomplete.")
        if missing:
            print("Missing labels:")
            for label in missing:
                print(f"- {label}")
        if empty:
            print("Empty labels:")
            for label in empty:
                print(f"- {label}")
        return 1

    print("[OK] State file has required labels and non-empty key fields.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
