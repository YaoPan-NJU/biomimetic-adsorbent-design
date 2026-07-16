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

The repository skeleton and governing contract are established and pushed. A PostgreSQL BMDL snapshot was exported with both default and transaction read-only settings confirmed as `on`. The structural audit found 48 prototypes, 44 pollutant profiles, 130 matches, and 3015 raw performance rows that collapse to 1076 unique rows after removing surrogate IDs. BMDL is provisionally restricted to evidence checking until the paired evaluation is complete.

Primary-source retrieval for the ten-pollutant shortlist is in progress. No pollutant or material has been selected. The next action is to merge and verify the retrieval evidence, lock the ten pollutant problem briefs, and then run the paired model-only versus BMDL-assisted benchmark.

## Resume instructions

1. Read `AGENTS.md`, `SOUL.md`, `PROJECT_STATE.yaml`, and `research_contract.yaml`.
2. Verify the active branch and inspect only artifacts listed in `PROJECT_STATE.yaml`.
3. Continue the single `next_action` recorded there.
4. Update this file and `PROJECT_STATE.yaml` before every checkpoint commit and push.
