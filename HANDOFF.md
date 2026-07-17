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

Pan Yao reopened portfolio design because S1-SYN alone did not provide enough success insurance. The material-class-neutral portfolio contains 20 nonprotein artificial adsorbent schemes for BPA (6), PFBS (5), roxithromycin (5), and 2,6-dichlorophenol (4). The full schemes, pre-attack ranking, evidence audit, and top-five attack are under `rounds/portfolio_20_reopen/`; all earlier files and scores remain intact.

The pre-attack top five were BPA-1, PFBS-1, PFBS-2, BPA-2, and ROX-1. Attack reduced them to BPA-1 84/revise, BPA-2 74/revise, PFBS-1 74/revise, PFBS-2 73/revise, and ROX-1 67/control-only. No scheme passes the 85/no-open-high final gate. S1-SYN remains paused, not terminated.

At that checkpoint Pan Yao authorized continued work and BPA-1 alone advanced first. The first deep-design checkpoint is `rounds/bpa1_deep_design_1/GEOMETRY_AND_RECEPTOR_TRIAGE.md`. Official `2E2R` coordinates give a derived BPA phenolic O-O distance of 9.274 Å and an approximately 87.4-degree acute inter-ring angle. The translated feature was initially recorded as a preorganized static two-ended polar geometry with a hydrophobic environment; no ERRgamma sequence, fold, Helix 12, protein or dynamic gate entered the material. Later additive files below supersede the symmetric requirement without deleting this history.

The first exact low-mass probe was `R1-BPE`, 1,2-di(pyridin-4-yl)ethyne (`C12H8N2`, 180.20 g/mol). Its PubChem 3D terminal N-N distance is 9.651 Å, within 0.377 Å of the bound BPA O-O distance, and a literature synthesis reported 75% isolated yield. This first-pass freeze is preserved in `GEOMETRY_AND_RECEPTOR_TRIAGE.md`.

The subsequent chemistry attack rejected R1 as the complete receptor. Its two terminal 4-pyridine acceptors point outward as a divergent linker; equality of O-O and N-N distances omitted lone-pair direction, hydrogen-bond length/angle and aromatic-framework collision. The proposed short/long/hydrophobic controls also changed solubility, mass, aromatic area and basicity simultaneously. `R1_CHEMISTRY_ATTACK.md` therefore returns BPA-1 to `exact receptor not frozen`, scores the refined proposal 68/100 with two critical and four high issues, and retains R1 only as a possible negative control.

The next review corrected a deeper translation error. ERRgamma mutagenesis places the chief and corroborative interactions on the same BPA phenol hydroxyl, and single-hydroxyl 4-alpha-cumylphenol still binds strongly. A symmetric 9.27-angstrom two-ended clamp is therefore no longer mandatory. The active translation is one complementary polar primary anchor plus hydrophobic aromatic enclosure, with the second hydroxyl retained only as an optional discriminator. The prior symmetric geometry files remain preserved as history.

`rounds/bpa1_deep_design_1/ASYMMETRIC_ANCHOR_REDIRECTION.md` defines exact candidate probe `P1-MAPy`, 2-methacrylamidopyridine (`C9H10N2O`, 162.19 g/mol). Its adjacent pyridine/amide donor-acceptor environment and methacryloyl polymer handle are synthesis- and polymerization-backed. It is not a proven BPA receptor: aqueous BPA binding, water competition, self-association and analog selectivity remain open. Its pure-site 1:1 ceiling is 1407.6 mg BPA/g MAPy, so any final dry material has the upper bound `1407.6 × w_MAPy mg/g`; this explicitly charges all pore-wall, crosslinker and carrier mass to the denominator.

`P1_MAPY_CONTROL_AND_GATE.md` freezes `C1-NHoff` (N-methyl-N-(2-pyridyl)acrylamide), `C2-Noff` (N-phenylmethacrylamide), `C3-meta` (N-(pyridin-3-yl)methacrylamide), and styrene `C4-H`. The pre-registered aqueous gate requires P1-BPA `Ka >= 100 M-1`, at least a threefold advantage over the strongest C1/C2/C3 control, and no more than threefold disagreement between two orthogonal methods after self-association is modeled. These are design thresholds, not experimental results.

`P1_MAPY_ATTACK.md` found that the established two-point acylaminopyridine synthon recognizes two-oxygen carboxylic acids and does not prove an ERRgamma-like two-contact geometry to one phenol oxygen. A direct aqueous 2-acrylamidopyridine/HEMA hydrogel precedent adsorbed phenol, 2,6-dimethylphenol and bulkier 2,6-di-tert-butylphenol at about 35.1, 30.1 and 17.2 mg/g for the reported 50% AP composition, a size trend unfavorable to a BPA-selectivity claim. P1 therefore remains only a high-information experimental probe; BPA-1 is 70/revise/experiment-gated and cannot be materialized on paper. Under Pan Yao's dynamic-allocation authorization, the next paper-design effort moves to BPA-2 as the higher-success insurance route. No material order, synthesis, experiment, S11 Gate 1b or Gate 2 work is authorized.

The BPA-2 attack is now recorded in `rounds/bpa2_deep_design_1/BPA2_BASELINE_AND_COLOCALIZATION_ATTACK.md`. Direct aqueous NMR supports a 1:1 beta-CD:BPA complex with Ka about 3.62-4.10e3 M-1, but random copolymerization of beta-CD and a polar monomer cannot establish that one guest contacts both sites. The pure-beta-CD 1:1 ceiling is only 201.14 mg BPA/g beta-CD, and every final material is bounded by `201.14 × w_betaCD mg/g dry material`. BPA-2 is therefore split additively: BPA-2E is a 72/revise engineering baseline with no added dual-site biomimetic claim; BPA-2R is a 63/revise research variant that requires an exact covalent secondary-rim polar receptor before materialization. No earlier 79 or 74 score was deleted. The active paper task is a lightweight high-accessible-beta-CD architecture comparison for BPA-2E; there is still no primary or backup.

That architecture comparison is complete in `BPA2E_ARCHITECTURE_COMPARISON.md`. Low-crosslink high-beta-CD networks maximize mass efficiency; a diarylsulfone-crosslinked beta-CD polymer already reports 113 mg BPA/g rapid column removal and regeneration; aqueous flexible-rigid T-E-CDP already covers rapid broad-spectrum removal and humic-acid/ionic-strength tolerance; and a 2023 double-crosslinked variant already reports real industrial wastewater. A low-density pendant-beta-CD particle is column-ready but demonstrates the user's mass-penalty concern because its 0.239 mmol/g site loading caps capacity near 54.5 mg/g. BPA-2E is therefore control-only, not a novel candidate, while BPA-2R remains unfrozen. Dynamic paper allocation now moves to PFBS-1.

PFBS-1 has now been attacked in `rounds/pfbs1_deep_design_1/PFBS1_PRIOR_ART_AND_SALT_ATTACK.md`. The proposed sevenfold styrenyl-beta-CD plus cationic methacrylate permanently porous copolymer was already implemented in ACS Central Science in 2022. More importantly, its PFBS removal at 1 mg/L adsorbent and 1 ug/L PFAS fell from about 94% in nanopure water to about 38% in 1 mM sodium sulfate, while PFOS retained about 79%. This directly contradicts a salt-resistant PFBS-over-long-chain preference. PFBS-1 is therefore 58/control-only; historical 82 and 74 scores remain. The next paper attack moves to PFBS-2 at the exact soluble-receptor level, with no materialization before water and salt evidence.

Pan Yao reviewed the complete post-Round-2 trajectory and identified a direction error. The original S1 translated hL-FABP evidence into an artificial headgroup site, finite low-polar chain region and hydrophilic porous carrier. The mandatory static-plus-dynamic gate then rewarded increasingly literal portal, folded-peptide and protein implementations. That gate optimized biomimetic fidelity instead of the intended material translation and caused the Round-3 S1 and later S11 routes to leave the intended synthetic-adsorbent scope.

The governing rules are now corrected. One hard functional correspondence in a manufacturable artificial material is required; dynamics are optional and must add selective function if claimed. Proteins, expressed constructs and folded peptides are excluded by default. All earlier rounds remain committed as historical audit evidence and no score or decision has been erased.

`S1-SYN` was the first corrected artificial-material candidate and remains a preserved paused route. Pan Yao's carrier-efficiency correction removed the prior assumption that OEG-passivated mesoporous silica would be the final carrier: silica, porous carbon, activated carbon, porous polymers, other supports and self-supporting architectures are only candidates. Any later BPA-1 material must expose total-composite gravimetric capacity, packed-bed capacity, accessible sites and blank-architecture uptake; inactive support mass cannot be hidden.

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
2. Verify `main`, then read `rounds/bpa1_deep_design_1/GEOMETRY_AND_RECEPTOR_TRIAGE.md`; treat all former finalists and S11 as historical only, and S1-SYN as paused.
3. Read the complete BPA-1 and BPA-2 deep-design folders, then `rounds/pfbs1_deep_design_1/PFBS1_PRIOR_ART_AND_SALT_ATTACK.md`; retain BPA-2E and PFBS-1 as positive controls, keep BPA-2R unfrozen, and begin PFBS-2 only at the soluble-receptor paper gate.
4. Keep BMDL excluded, preserve every phosphate, top-five, S1, S11 and portfolio artifact, and do not order materials or start experiments.
5. Update this file and `PROJECT_STATE.yaml` before every checkpoint commit and push.
