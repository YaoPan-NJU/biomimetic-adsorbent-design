#!/usr/bin/env python3
"""Validate portable project state and committed snapshot integrity."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    state = yaml.safe_load((ROOT / "PROJECT_STATE.yaml").read_text(encoding="utf-8"))
    contract = yaml.safe_load((ROOT / "research_contract.yaml").read_text(encoding="utf-8"))

    if not state.get("next_action"):
        fail("PROJECT_STATE.yaml has no unique next_action")
    if contract["project"]["independence"].lower().startswith("adrmats") is False:
        fail("research contract no longer records ADRMATS independence")

    missing = []
    for label, relative in state.get("artifacts", {}).items():
        if not (ROOT / relative).is_file():
            missing.append(f"{label}: {relative}")
    if missing:
        fail("state artifact paths are missing: " + "; ".join(missing))

    manifest_path = ROOT / "data/bmdl_snapshot/manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for label, metadata in manifest["files"].items():
        relative = Path(metadata["path"])
        if relative.is_absolute():
            fail(f"snapshot path is not portable: {relative}")
        path = ROOT / relative
        if not path.is_file():
            fail(f"snapshot file is missing: {relative}")
        expected = metadata.get("sha256")
        if expected and sha256(path) != expected:
            fail(f"snapshot checksum mismatch: {label}")

    branch = subprocess.run(
        ["git", "branch", "--show-current"], cwd=ROOT, check=True, text=True, capture_output=True
    ).stdout.strip()
    if branch != state.get("active_branch"):
        fail(f"active branch {branch!r} differs from recorded {state.get('active_branch')!r}")

    print(
        f"PASS: {len(state.get('artifacts', {}))} state artifacts, "
        f"{len(manifest['files'])} snapshot files, branch={branch}, next_action={state['next_action']}"
    )


if __name__ == "__main__":
    main()
