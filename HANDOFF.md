# Cross-device handoff

## Objective

Develop one primary and one backup biomimetic material for selective adsorption in municipal secondary effluent. Deliver a Chinese experimental handoff package, not a software product.

## Locked decisions

- ADRMATS is unrelated to this implementation.
- Primary matrix is municipal/domestic secondary effluent; ultrapure water is the mechanism control.
- Funnel is 10 pollutants, 5 deep concepts, 1 primary and 1 backup.
- Main design requires at least one hard functional correspondence translated into an artificial material. Dynamic correspondence is optional and cannot force protein, folded peptide or a generic responsive unit into the design.
- Tissue or organ enrichment is an optional, non-scoring prototype-discovery signal, not proof that a specific protein causes accumulation. The evidence ladder and pre-exposure interception idea are recorded in `research/evidence/ORGAN_ENRICHMENT_BIOMIMETIC_HEURISTIC.md`; they do not alter the active route or next action.
- The default deliverable is a manufacturable nonprotein artificial adsorbent; protein, folded-peptide or biohybrid routes require an explicit scope reopening by Pan Yao.
- Carrier class is not preselected. Silica, resin, carbon and self-supporting architectures are candidates only; capacity must be reported per total dry composite mass and packed-bed volume, and inactive carrier mass must earn its place through selectivity, matrix tolerance, regeneration, stability or bed performance.
- Codex supervises isolated designer, attacker, and reviewer roles.
- BMDL is evaluated against a frozen model-only baseline before any design use.
- Final approval belongs to Pan Yao; no laboratory work is performed in this repository.

## Current state

Pan Yao reviewed the complete post-Round-2 trajectory and identified a direction error. The original S1 translated hL-FABP evidence into an artificial headgroup site, finite low-polar chain region and hydrophilic porous carrier. The mandatory static-plus-dynamic gate then rewarded increasingly literal portal, folded-peptide and protein implementations. That gate optimized biomimetic fidelity instead of the intended material translation and caused the Round-3 S1 and later S11 routes to leave the intended synthetic-adsorbent scope.

The governing rules are now corrected. One hard functional correspondence in a manufacturable artificial material is required; dynamics are optional and must add selective function if claimed. Proteins, expressed constructs and folded peptides are excluded by default. All earlier rounds remain committed as historical audit evidence and no score or decision has been erased.

The active candidate is now `S1-SYN`, an hL-FABP-informed but nonprotein artificial material. Its recognition unit remains one exact nonpeptidic receptor with a guanidinium/amide carboxylate site and a finite low-polar chain-accommodation unit. Pan Yao's carrier-efficiency correction removed the prior assumption that OEG-passivated mesoporous silica would be the final carrier: silica remains eligible as a mechanism platform, while porous carbon, activated carbon, porous polymers, other supports and self-supporting architectures remain equally eligible. The exact receptor, carrier choice and bench SOP are not yet frozen, so `S1-SYN` is not a primary or backup.

The unique next action is an isolated design of one exact nonpeptidic receptor and matched controls, a material-class-neutral comparison of carrier or self-supporting routes, and a complete SOP for the selected route under `rounds/synthetic_recovery_1/S1_SYNTHETIC_RECOVERY_BRIEF.md`. The comparison must expose total-composite gravimetric capacity, packed-bed capacity, accessible sites and blank-carrier uptake. No ordering, synthesis or experiment is authorized. S11 Gate 1b and Gate 2 are scope-superseded unless Pan Yao explicitly reopens a protein/biohybrid project.

## Preserved trajectory

Pan Yao's scientific review reopened the project at the pollutant-selection gate. The previous funnel mixed nutrients and inorganic pollutants with emerging organic contaminants, while its scoring strongly rewarded mature static-dynamic biomimetic evidence. That objective allowed phosphate to win despite being misaligned with the intended paper scope. The former ten-pollutant ranking, D1-A primary and D1-B backup remain preserved as historical artifacts but are no longer active selections and must not be presented as approved deliverables.

The active scope is organic pollutants, with priority given to emerging contaminants in municipal secondary effluent. `pollutant_kb.pollutant_index` is the candidate seed, not a risk authority. PFOA, PFBS, roxithromycin, bisphenol A and 2,6-dichlorophenol form the initial priority verification group. The exact ten candidates are not frozen. Secondary-effluent relevance and environmental or health concern are binary admission gates applied before scoring; neither receives weighted points, and failure cannot be rescued by a strong biomimetic concept. Only admitted candidates are scored for selective-adsorption difficulty, biomimetic capability, static-dynamic synergy, engineering generality and novelty/evidence opportunity.

The revised work has now produced an auditable pre-screen and ten mechanism-distinct schemes. The recommended five are S1 PFOA/hL-FABP two-stage portal, S5 BPA/ERRγ bidentate aromatic clamp, S3 HFPO-DA (GenX)/HSA branched ether-acid pocket, S4 PFBS/PFHxS/PFOS HSA chain-length gate, and S6 roxithromycin/23S rRNA local gate. These are portfolio recommendations, not approved finalists. S10 2,6-dichlorophenol remains conditional because direct municipal secondary-effluent evidence is insufficient.

Pan Yao approved the recommended top five for isolated deep-design: S1 PFOA, S5 BPA, S3 HFPO-DA/GenX, S4 PFBS/PFHxS/PFOS and S6 roxithromycin. The historical phosphate D1-A and D1-B packages remain committed and accessible in GitHub; they are superseded for the current paper scope, not deleted.

Round 1 produced no pass. Round 2 restored independent designer, attacker and reviewer roles and disposed of all five schemes: S3 and S6 terminated, S4 and S5 became control-only, and S1 alone entered Round 3 at 82/revise. Round 3 converted S1 into an explicit hL-FABP plus iLBP-derived artificial portal proposal, but independent review terminated it at 56/100 with three critical and four high issues. The artificial portal was not a determined chemical state and the iLBP family evidence did not establish a target-specific dynamic hard correspondence.

The contract-required external prototype reopening is complete. A 2025 peer-reviewed JACS Au study and PDB structures `9OB7/9MIW` directly show apo versus PFOA-bound FABP4, two PFOA positions and a local Phe57 author-numbered state difference. PFOA-PPARgamma was rejected as a dynamic prototype because its reported partial agonism is Helix-12-independent; PFOS-FadL remains simulation-led; roxithromycin still lacks target-specific ribosome dynamic evidence.

The only reopened candidate is S11, an actual FABP4 biohybrid. Its initial design was attacked and scored 60/100, pause-for-preexperiment. The attack caught an `ST/TS` sequence transcription error and a numbering offset: PDB author Phe57/Thr29/Arg126 correspond to UniProt P15090 F58/T30/R127. It also rejected the original bifunctional-amine GGG surface route. Gate 1a now passes after freezing eight machine-validated constructs, a `GGGGC` thiol-maleimide surface route, native-MS plus equilibrium-dialysis occupancy tests, residue-level NMR, T30A as the unique dynamic causal control, PFOA/octanoate as the unique primary selectivity endpoint, batch statistics and stop rules. Gate 1a has zero design-layer critical/high issues.

S11 has **not** passed as a primary or backup. Gate 1b procurement/manufacturing records are pending and prohibit ordering or experiments. Gate 2 still has three experimental critical issues and four high issues: soluble second occupancy, Phe58 residue-level dynamic causality, independent activity normalization, immobilized accessibility and real secondary-effluent competitive selectivity. This repository intentionally stops before actual laboratory work, consistent with the first-delivery boundary.

Under the former contract, the unique next action was Pan Yao's review of the S11 Gate 1a package. That action is preserved here as historical state but is superseded by the artificial-material direction correction above. BMDL remains excluded from design.

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
2. Verify `main`, read `rounds/synthetic_recovery_1/S1_SYNTHETIC_RECOVERY_BRIEF.md`, and treat all former finalists and S11 as historical only.
3. Keep BMDL excluded, preserve every phosphate, top-five, S1 and S11 artifact, and do not order materials or start experiments.
4. Update this file and `PROJECT_STATE.yaml` before every checkpoint commit and push.
