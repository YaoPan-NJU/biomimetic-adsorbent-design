# Cross-device handoff

## Objective

Develop one primary and one backup biomimetic material for selective adsorption in municipal secondary effluent. Deliver a Chinese experimental handoff package, not a software product.

## Locked decisions

- ADRMATS is unrelated to this implementation.
- Primary matrix is municipal/domestic secondary effluent; ultrapure water is the mechanism control.
- Funnel is 10 pollutants, 5 deep concepts, 1 primary and 1 backup.
- Main design requires at least one static and one dynamic hard biomimetic correspondence.
- Codex supervises isolated designer, attacker, and reviewer roles.
- BMDL is evaluated against a frozen model-only baseline before any design use.
- Final approval belongs to Pan Yao; no laboratory work is performed in this repository.

## Current state

The governing contract, ten-pollutant shortlist, evidence ledger, key-claim spot check, and isolated model-only baseline are complete. A PostgreSQL BMDL snapshot was exported with both default and transaction read-only settings confirmed as `on`. The structural audit found 48 prototypes, 44 pollutant profiles, 130 matches, and 3015 raw performance rows that collapse to 1076 unique rows after removing surrogate IDs.

The frozen model-only ranking is led by phosphate/PstS (91), nitrate/NrtA (87), ODV/SERT (84), clarithromycin/ribosome (82), and PFOA/FABP (80). Scores are design triage values, not predicted performance. Evidence spot checking narrowed five of ten high-impact claims; in particular, NrtA and SERT sources do not independently establish complete open-to-closed cycles, and hL-FABP evidence does not yet establish a transferable dynamic gate.

BMDL remains provisionally restricted to evidence checking. The first anonymous comparison appeared to favor the assisted variants by 5.8 points on average, but the comparison is invalid: the evidence ledger was updated between the two arms, and the reviewer explicitly rewarded those evidence corrections. The invalid attempt and its blind scores are preserved rather than erased.

The exact next action is a controlled rerun. Fresh isolated contexts must use the hash-locked common inputs in `research/bmdl/rerun/FROZEN_INPUT_MANIFEST.yaml`; only the assisted arm may additionally read the per-candidate BMDL packages. New anonymous variants are then reviewed without access to the identity mapping. No BMDL policy may be upgraded from the invalid first attempt.

Translation-evidence dossiers were prepared in parallel but are deliberately excluded from the rerun manifest. They strengthen the later deep-design gate: PBP has an experimental apo/bound pair and direct fluorescence/FRET precedents; NrtA still lacks an experimental apo structure; clarithromycin has a direct 3.3 Å ribosome structure with local A2062 heterogeneity; hL-FABP supports PFOA binding and local portal mobility but not a large global closure; ODV binds hSERT functionally but lacks a target-bound structure.

## Resume instructions

1. Read `AGENTS.md`, `SOUL.md`, `PROJECT_STATE.yaml`, and `research_contract.yaml`.
2. Verify `main`, the frozen input hashes, and the invalid-attempt record.
3. Continue only the controlled BMDL rerun recorded in `PROJECT_STATE.yaml`.
4. Update this file and `PROJECT_STATE.yaml` before every checkpoint commit and push.
