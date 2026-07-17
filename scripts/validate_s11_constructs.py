#!/usr/bin/env python3
"""Validate frozen S11 mature Sortase-substrate sequences."""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FASTA = ROOT / "rounds/prototype_reopen_1/S11_CONSTRUCTS.fasta"
FILE_SHA256 = "f1d2d789cf8cf9c2dd9fab5d793432d15cc4d3feb671ff59d8f3c6df9dd12e89"
P15090 = (
    "MCDAFVGTWKLVSSENFDDYMKEVGVGFATRKVAGMAKPNMIISVNGDVITIKSESTFKN"
    "TEISFILGQEFDEVTADDRKVKSTITLDGGVLVHVQKWDGKSTTIKRKREDDKLVVECVM"
    "KGVTSTRVYERA"
)
EXPECTED_MUTATIONS = {
    "S11_WT": {},
    "S11_T30A": {30: "A"},
    "S11_F58A": {58: "A"},
    "S11_F58W": {58: "W"},
    "S11_R107A": {107: "A"},
    "S11_R127A": {127: "A"},
    "S11_Y129F": {129: "F"},
    "S11_R127A_T30A": {30: "A", 127: "A"},
}


def parse_fasta(text: str) -> list[tuple[str, str]]:
    records: list[tuple[str, str]] = []
    header: str | None = None
    sequence: list[str] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line.startswith(">"):
            if header is not None:
                records.append((header, "".join(sequence)))
            header, sequence = line[1:], []
        elif line:
            if header is None:
                raise ValueError("sequence before first FASTA header")
            sequence.append(line)
    if header is not None:
        records.append((header, "".join(sequence)))
    return records


def main() -> None:
    raw = FASTA.read_bytes()
    actual_file_hash = hashlib.sha256(raw).hexdigest()
    if actual_file_hash != FILE_SHA256:
        raise SystemExit(f"file SHA-256 mismatch: {actual_file_hash}")

    records = parse_fasta(raw.decode("ascii"))
    if len(records) != len(EXPECTED_MUTATIONS):
        raise SystemExit(f"expected 8 records, found {len(records)}")

    for header, sequence in records:
        fields = header.split("|")
        name = fields[0]
        expected_hash = next(
            field.removeprefix("sha256=") for field in fields if field.startswith("sha256=")
        )
        actual_hash = hashlib.sha256(sequence.encode("ascii")).hexdigest()
        if actual_hash != expected_hash:
            raise SystemExit(f"{name}: sequence SHA-256 mismatch")
        if len(sequence) != 148 or not sequence.startswith("GH") or not sequence.endswith("GSGLPETGHHHHHH"):
            raise SystemExit(f"{name}: invalid mature substrate frame")

        expected_core = list(P15090)
        for position, residue in EXPECTED_MUTATIONS[name].items():
            expected_core[position - 1] = residue
        if sequence[2:134] != "".join(expected_core):
            raise SystemExit(f"{name}: P15090 core or declared mutation mismatch")
        print(f"{name}: OK")

    print(f"file SHA-256: {actual_file_hash}")


if __name__ == "__main__":
    main()
