#!/usr/bin/env python3
"""Fail when tracked files contain common credential forms."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "credentialed database URI": re.compile(
        r"\b(?:postgres(?:ql)?|mysql|mongodb(?:\+srv)?):\/\/[^\s:/]+:[^\s/@]+@",
        re.IGNORECASE,
    ),
}


def tracked_files() -> list[Path]:
    output = subprocess.run(
        ["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True
    ).stdout
    return [ROOT / item.decode() for item in output.split(b"\0") if item]


def main() -> None:
    findings: list[str] = []
    for path in tracked_files():
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for name, pattern in PATTERNS.items():
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                findings.append(f"{path.relative_to(ROOT)}:{line}: {name}")
    if findings:
        print("FAIL: possible credentials in tracked files", file=sys.stderr)
        print("\n".join(findings), file=sys.stderr)
        raise SystemExit(1)
    print(f"PASS: scanned {len(tracked_files())} tracked files; no credential patterns found")


if __name__ == "__main__":
    main()
