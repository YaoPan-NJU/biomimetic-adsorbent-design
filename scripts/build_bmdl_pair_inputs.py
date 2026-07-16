#!/usr/bin/env python3
"""Build compact BMDL-assisted inputs for the frozen ten-pollutant set."""

from __future__ import annotations

import json
from pathlib import Path


CANDIDATES = {
    "pfoa": "PFOA",
    "pfos": "PFOS",
    "genx": "HFPO-DA (GenX)",
    "clarithromycin": "Clarithromycin",
    "odv": "O-desmethylvenlafaxine",
    "smx": "SMX",
    "bpa": "BPA",
    "phosphate": "PO43-",
    "nitrate": "NO3-",
    "as_iii": "As(III)",
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def prototype_id(prototype: dict) -> str | None:
    return prototype.get("prototype_id") or prototype.get("id")


def compact_prototype(prototype: dict) -> dict:
    return {
        "prototype_id": prototype_id(prototype),
        "organism": prototype.get("organism"),
        "biomimetic_dimension": prototype.get("biomimetic_dimension"),
        "source_category": prototype.get("source_category"),
        "mechanisms": prototype.get("mechanisms") or [],
        "design_translation": prototype.get("design_translation") or [],
        "engineering_constraints": prototype.get("engineering_constraints") or [],
        "honesty_ledger": prototype.get("honesty_ledger") or {},
    }


def main() -> None:
    snapshot = Path("data/bmdl_snapshot")
    output = Path("research/bmdl/paired_inputs")
    output.mkdir(parents=True, exist_ok=True)
    profiles = load(snapshot / "pollutant_profiles.json")
    matches = load(snapshot / "match_weights.json")
    prototypes = load(snapshot / "biological_prototypes.json")

    by_profile = {}
    for profile in profiles:
        for key in (profile.get("pollutant_id"), profile.get("canonical_name")):
            if key:
                by_profile[str(key).casefold()] = profile
    by_prototype = {
        str(prototype_id(item)): item
        for item in prototypes
        if prototype_id(item)
    }

    index = []
    for slug, query in CANDIDATES.items():
        profile = by_profile.get(query.casefold())
        pollutant_id = profile.get("pollutant_id") if profile else None
        rows = [row for row in matches if pollutant_id and row.get("pollutant_id") == pollutant_id]
        rows.sort(key=lambda row: (-float(row.get("weight") or 0), str(row.get("prototype_id"))))
        rows = rows[:5]
        package = {
            "candidate": slug,
            "query": query,
            "exact_profile_hit": bool(profile),
            "profile": profile,
            "matches": rows,
            "prototypes": [
                compact_prototype(by_prototype[row["prototype_id"]])
                for row in rows
                if row.get("prototype_id") in by_prototype
            ],
            "use_constraints": {
                "BMDL_weight_is_not_performance": True,
                "exploratory_and_inference_are_leads_only": True,
                "outside_prototype_search_remains_allowed": True,
            },
        }
        path = output / f"{slug}.json"
        path.write_text(json.dumps(package, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        index.append(
            {
                "candidate": slug,
                "query": query,
                "profile_hit": bool(profile),
                "match_count": len(rows),
                "lanes": [row.get("lane") for row in rows],
                "prototype_ids": [row.get("prototype_id") for row in rows],
            }
        )
    (output / "index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()

