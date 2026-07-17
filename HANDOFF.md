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

Pan Yao's scientific review reopened the project at the pollutant-selection gate. The previous funnel mixed nutrients and inorganic pollutants with emerging organic contaminants, while its scoring strongly rewarded mature static-dynamic biomimetic evidence. That objective allowed phosphate to win despite being misaligned with the intended paper scope. The former ten-pollutant ranking, D1-A primary and D1-B backup remain preserved as historical artifacts but are no longer active selections and must not be presented as approved deliverables.

The active scope is organic pollutants, with priority given to emerging contaminants in municipal secondary effluent. `pollutant_kb.pollutant_index` is the candidate seed, not a risk authority. PFOA, PFBS, roxithromycin, bisphenol A and 2,6-dichlorophenol form the initial priority verification group. The exact ten candidates are not frozen. Secondary-effluent relevance and environmental or health concern are binary admission gates applied before scoring; neither receives weighted points, and failure cannot be rescued by a strong biomimetic concept. Only admitted candidates are scored for selective-adsorption difficulty, biomimetic capability, static-dynamic synergy, engineering generality and novelty/evidence opportunity.

The revised work has now produced an auditable pre-screen and ten mechanism-distinct schemes. The recommended five are S1 PFOA/hL-FABP two-stage portal, S5 BPA/ERRγ bidentate aromatic clamp, S3 HFPO-DA (GenX)/HSA branched ether-acid pocket, S4 PFBS/PFHxS/PFOS HSA chain-length gate, and S6 roxithromycin/23S rRNA local gate. These are portfolio recommendations, not approved finalists. S10 2,6-dichlorophenol remains conditional because direct municipal secondary-effluent evidence is insufficient.

Pan Yao approved the recommended top five for isolated deep-design: S1 PFOA, S5 BPA, S3 HFPO-DA/GenX, S4 PFBS/PFHxS/PFOS and S6 roxithromycin. The historical phosphate D1-A and D1-B packages remain committed and accessible in GitHub; they are superseded for the current paper scope, not deleted.

Round 1 is complete. No scheme passed. S1 scored 82/revise, S5 81/revise, S3 79/revise, S6 77/revise and S4 73/revise-or-static-only. The common blocking issue is that direct target-recognition evidence is mostly static while the proposed material motion is not supported as a target-specific biological dynamic. S3 also risks misreading the HSA–HFPO-DA–myristate ternary structure; S4 currently supports only a static chain-length engineering bed; S6 cannot transfer all A2062/A2503 dynamics from related macrolides to roxithromycin.

The isolated designer and attacker agents did not return artifacts within the bounded run. Main-agent fallbacks are explicitly labeled in the round-1 files, and no pass was issued. Round 2 must restore independent role review before any scheme can pass.

The unique next action is a limited Round 2: resolve or terminate dynamic-prototype gaps and ordinary-adsorption relabeling. BMDL remains excluded from design.

## Superseded completed cycle

The governing contract, ten-pollutant shortlist, evidence ledger, key-claim spot check, and isolated model-only baseline are complete. A PostgreSQL BMDL snapshot was exported with both default and transaction read-only settings confirmed as `on`. The structural audit found 48 prototypes, 44 pollutant profiles, 130 matches, and 3015 raw performance rows that collapse to 1076 unique rows after removing surrogate IDs.

The frozen model-only ranking is led by phosphate/PstS (91), nitrate/NrtA (87), ODV/SERT (84), clarithromycin/ribosome (82), and PFOA/FABP (80). Scores are design triage values, not predicted performance. Evidence spot checking narrowed five of ten high-impact claims; in particular, NrtA and SERT sources do not independently establish complete open-to-closed cycles, and hL-FABP evidence does not yet establish a transferable dynamic gate.

BMDL remains provisionally restricted to evidence checking. The first anonymous comparison appeared to favor the assisted variants by 5.8 points on average, but the comparison is invalid: the evidence ledger was updated between the two arms, and the reviewer explicitly rewarded those evidence corrections. The invalid attempt and its blind scores are preserved rather than erased.

The controlled second comparison is complete. The assisted arm won 8/10 but improved the mean score by only 2.3 points, below the required 5. BMDL inputs also contained at least four severe cross-pollutant or mislabeled associations. The final policy is `exclude_design_stage_allow_posthoc_negative_audit_only`: designers must not read BMDL; after a design is frozen, the supervisor may use the snapshot only to add conventional baselines or detect known bad associations.

Five concepts completed round-1 design, attack, and cross-review. None passed. D1 phosphate scored 78 and is the strongest revision candidate; D2 clarithromycin scored 70 and remains the likely backup route; D3 PFOA scored 63 with a dynamic critical; D4 nitrate scored 62 and the full static-dynamic concept was rejected; D5 ODV scored 51 and its SERT dynamic mapping was rejected. Exact issue tables are in the two reviewer files and summarized in `rounds/round_1/REVIEW.md`.

Round 2 is complete. D1 phosphate improved to 83 and is the only working primary; D2 clarithromycin was rejected as a finalist at 74 because bound-state A2062 heterogeneity is not a supported biological gate; D3-D5 remain terminated. No original concept passed the 85/no-open-high threshold.

The threshold was not lowered. A limited backup implementation was reopened: D1-B, a C-terminally immobilized PBP/PiBP protein–porous-carrier hybrid. Round 3 compared D1-A synthetic peptide clamp and D1-B biohybrid, required a full bench SOP for both, and defined complementary switch conditions. D1-B does not inherit adsorption capacity, regeneration, or stability from protein-sensor precedents.

Round 3 is complete. D1-A passed at 93/100 after the single-arm controls and accessible-capacity units were repaired. D1-B passed at 89/100 after the dynamic bed-volume gate was corrected and the biased random-immobilization orientation claim was removed. Both have zero unresolved critical/high design issues. These are design passes only; every material-performance claim remains subject to the frozen experimental gates.

D1-A is the primary because it has the stronger original materials contribution, a pure-organic receptor, and a tighter delete/lock causal chain. D1-B is a trace-polishing backup for `Cin≤0.10 mg P/L`; its exact PBP protein sequences and SHA-256 records are committed, while DNA, sortase lot and resin lot remain procurement hold points that prohibit experimental startup until recorded.

The Chinese main report and all final attachments are committed under `deliverables/`. Commit `53014c468f2e174f5ff69737f7a64e66ff7fee06` was pushed, restored into a fresh clone, and passed state-path, snapshot-checksum, credential and machine-path checks. A context-free Codex recovered the objective, decisions, rejected concepts and pending action using only that clone. Pan Yao's final scientific approval remains pending and must not be inferred from design-review pass scores.

Translation-evidence dossiers were prepared in parallel but are deliberately excluded from the rerun manifest. They strengthen the later deep-design gate: PBP has an experimental apo/bound pair and direct fluorescence/FRET precedents; NrtA still lacks an experimental apo structure; clarithromycin has a direct 3.3 Å ribosome structure with local A2062 heterogeneity; hL-FABP supports PFOA binding and local portal mobility but not a large global closure; ODV binds hSERT functionally but lacks a target-bound structure.

## Resume instructions

1. Read `AGENTS.md`, `SOUL.md`, `PROJECT_STATE.yaml`, and `research_contract.yaml`.
2. Verify `main`, read `DEEP_RESEARCH_BIOMIMETIC_SCHEME_PORTFOLIO.md`, and treat all former finalists as historical only.
3. Continue the limited top-five Round 2 action recorded in `PROJECT_STATE.yaml`; keep BMDL excluded from design, preserve phosphate history, and do not start experiments.
4. Update this file and `PROJECT_STATE.yaml` before every checkpoint commit and push.
