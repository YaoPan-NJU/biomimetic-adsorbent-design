# Cross-device handoff

## Objective

Develop one primary and one backup biomimetic material for selective adsorption in environmentally meaningful water treatment scenarios. Deliver a Chinese experimental handoff package, not a software product.

## Locked decisions

- ADRMATS is unrelated to this implementation.
- Water matrix is any environmental water treatment scenario with independently verified environmental significance and practical value (municipal secondary effluent, industrial wastewater, surface water, drinking water sources, groundwater); ultrapure or deionized water is the mechanism control.
- Before searching for biological prototypes, the specific scientific problem and engineering challenge must be identified from the pollutant. The scientific problem ensures academic depth; the engineering challenge ensures practical application and paper closure.
- Main design requires at least one hard functional correspondence translated into an artificial material. Dynamic correspondence is optional and cannot force protein, folded peptide or a generic responsive unit into the design.
- Tissue or organ enrichment is an optional, non-scoring prototype-discovery signal, not proof that a specific protein causes accumulation.
- The default deliverable is a manufacturable nonprotein artificial adsorbent; protein, folded-peptide or biohybrid routes require an explicit scope reopening by Pan Yao.
- Carrier class is not preselected. Capacity must be reported per total dry composite mass and packed-bed volume, and inactive carrier mass must earn its place through selectivity, matrix tolerance, regeneration, stability or bed performance.
- The active executor (Claude Code primary, Qwen cross-device secondary) supervises isolated designer, attacker, and reviewer roles; at most one executor is active at a time.
- BMDL is removed from this branch; biomimetic research uses web-based deep search.
- Every scheme must pass the innovation checklist (`INNOVATION_CHECKLIST.md`) before formal scoring.
- All tasks must be executed at maximum thinking depth; no shortcuts or reduced-depth approximations are permitted.
- Final approval belongs to Pan Yao; no laboratory work is performed in this repository.

## Current state

This branch has undergone a methodology correction (2026-07-19). The supervisor is now Qwen. BMDL has been removed from the project design. The water scenario has been expanded from municipal secondary effluent to any environmentally meaningful water treatment context. A new "scientific problem + engineering challenge" gate has been added before biological prototype search. An independent innovation checklist has been created. Maximum thinking intensity is now a project rule.

All historical artifacts (20-scheme portfolio, BPA/PFBS/ROX deep-design rounds, evidence ledger, former finalists D1-A/D1-B, S11, portfolio_100, and all scores) are preserved in the repository as audit evidence and counter-examples, but are no longer active selections. The new design flow starts fresh from pollutant selection under the corrected methodology.

No primary design or backup design exists. No material order, synthesis, or experiment is authorized.

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
2. Read `INNOVATION_CHECKLIST.md` to understand the innovation gate.
3. Begin fresh pollutant selection: identify candidate organic pollutants with environmental significance, then for each candidate define the specific scientific problem and engineering challenge before searching for biological prototypes.
4. Use web-based deep search for all biomimetic design research; no local database dependency exists.
5. All historical artifacts are preserved but not active; do not inherit scores or selections from former rounds.
6. Update this file and `PROJECT_STATE.yaml` before every checkpoint commit and push.
7. Work on the `Qwen` branch and push only to `origin/Qwen`; do not touch `kimi-k3` or `main`. Claude Code and Qwen share this branch sequentially: pull and re-read the state files before starting work.

## GLM branch takeover (2026-07-17)

Pan Yao split the repository into two executor workstreams so concurrent Codex and Claude Code sessions do not clash. Codex continues on `main` and syncs `origin/main`; Claude Code took over the executor role on a new `GLM` branch at `df8a7ef` and syncs `origin/GLM` only. The two branches evolve independently, neither cross-pushes, and any future merge is reconciled manually only if explicitly requested.

On `GLM`, `CLAUDE.md` is the Claude Code entrypoint and supersedes `AGENTS.md` for executor identity and branch sync only; `AGENTS.md` is retained as the Codex entrypoint and shared-rules reference. `research_contract.yaml` records `executor: Claude Code` and `executor_branch: GLM` here; `main` keeps `executor: Codex`. `PROJECT_STATE.yaml` records `active_branch: GLM` here; `main` keeps `active_branch: main`. Resume-instruction step 1 still reads `AGENTS.md` as a shared-rules reference, with `CLAUDE.md` as the branch-specific entrypoint.

The research state is unchanged by the takeover. The live phase remains `rox2_nonimprinted_slit_paper_attack`; `primary_design` and `backup_design` remain `null`; the next action remains the ROX-2 paper attack. All historical rounds, scores, and decisions are preserved. BMDL remains excluded from design. No material order, synthesis, or experiment is authorized.

## Biomimetic design framework correction (2026-07-18)

After completing the 100-scheme portfolio (5 pollutants × 20 schemes each, with cull and ranking at commit `f7f797c`), Pan Yao identified a fundamental deviation in the project's biomimetic design approach. This section documents the correction.

### The problem identified

Many schemes in the portfolio followed **approach 3** from the source brief (`docs/source/仿生吸附材料设计任务总纲.md`): "find proteins that can bind the target pollutant, then mimic them." The source brief explicitly deprioritizes this approach:

> "针对某种特定污染物，寻找能特定吸附它的生物原型进行仿生设计。逻辑牵强，'因为难去除，所以自然界有现成方案'这一步不成立。倾向放弃，或仅作个案补充。"

This approach-3 thinking led to schemes like:
- "FABP4 binds PFOA, so we mimic FABP4" (but FABP4 evolved for fatty acids, not PFOA)
- "ERRγ binds BPA, so we mimic ERRγ" (but ERRγ binding BPA is endocrine disruption, not a solution)
- Various schemes with no real biological prototype (pure supramolecular chemistry)

### The corrected framework

The project's main route must be **approach 2 (top-down, solve engineering problems) + approach 1 (bottom-up, mechanism matching)**:

**Approach 2 (Why - rationale layer)**: Identify common engineering challenges in adsorption that traditional synthesis cannot solve. Examples:
- Structural hierarchy (multi-scale ordered pores)
- Dynamic response (stimulus-responsive conformational changes)
- Multi-component cooperative self-assembly

**Approach 1 (How - method layer)**: 
1. Analyze pollutant properties
2. Identify adsorption mechanisms (e.g., amino-carboxyl matching, electrostatic attraction)
3. Find biological prototypes that use the **same mechanisms**
4. Study how biology implements these mechanisms
5. Translate the **design principles** (not the protein itself) into materials

**Approach 3 (Case - validation layer)**: Optional, only as case validation, not as the main route.

### Multi-dimensional correspondence requirement

True biomimetic design requires **at least 2 hard correspondences** across these dimensions:

| Dimension | Examples | Addresses pain point |
|-----------|----------|---------------------|
| **Static structure** | Hierarchical pores, hydrophilic/hydrophobic patterns | "Why is the pollutant hard to remove?" (intrinsic adsorption capacity) |
| **Dynamic behavior** | Stimulus response, regeneration | "Why is it hard to design adsorbents?" (engineering bottleneck) |

Single-dimension mimicry (e.g., only copying a binding site) is insufficient and reads as "packaging, not biomimicry."

### Pain point-biomimicry causal chain

The correct sequence is:
1. **First** determine what biological prototypes can offer (which dimensions can truly be mimicked)
2. **Then** derive the pain points from those capabilities
3. **Finally** write the introduction with a closed causal chain

NOT: start with a pain point, then force-fit a biological prototype.

The causal chain must be:
> Root cause why pollutant is hard to remove → This root cause is exactly what traditional synthesis cannot solve → A biological prototype evolved to solve this root cause → Therefore we mimic its corresponding dimensions

### Material complexity constraint

Do **not** require Ångström-level precise spatial control (e.g., replicating exact protein 3D structures). Instead:
- Extract **design principles** (e.g., "hydrophobic cavity + polar headgroup anchor + spatial preorganization")
- Implement these principles with **synthesizable materials** (COFs, hypercrosslinked polymers, etc.)
- Allow structural flexibility within the design principle

### Terminology standard

Use **"人工识别单元" (artificial recognition unit)** to refer to synthetic molecular recognition structures. Do **not** use "受体" (receptor), which confuses with biological protein receptors.

### Optional bioaccumulation reference

The document `research/evidence/ORGAN_ENRICHMENT_BIOMIMETIC_HEURISTIC.md` provides an **optional, non-scoring** prototype discovery heuristic: study how pollutants bioaccumulate in organisms (e.g., PFOA in liver via FABP binding), understand the mechanism, then intercept pollutants before they enter organisms.

This is **one valid reference line, not mandatory**. It does not change scoring, gates, or the main route.

### Next steps

1. Reassess portfolio_100 schemes against this corrected framework
2. For each scheme, ask:
   - What engineering problem does this solve that traditional synthesis cannot?
   - How many hard correspondence dimensions does it have?
   - Is the biological prototype real and relevant (not contrived)?
   - Is the material synthesizable without Ångström-level precision?
   - Is the pain point derived from the biomimetic capability (not forced)?
3. Prioritize schemes with strong multi-dimensional correspondence and clear engineering problem solving
4. Be honest about schemes that are rational design (not truly biomimetic)

See `docs/BIOMIMETIC_DESIGN_FRAMEWORK.md` for the complete framework reference.

## Qwen branch activation (2026-07-19)

The methodology correction is committed as `75c8144`, the first Qwen-only commit. The `Qwen` branch starts from `kimi-k3` HEAD `100b7df`, so all historical artifacts (portfolio_20, portfolio_100, framework correction, top-five rounds, S11, D1-A/D1-B, ROX-2) remain present on this branch as preserved audit evidence; `kimi-k3` is frozen at `100b7df` and receives no new commits.

Claude Code is the primary executor on this branch and reads `CLAUDE.md`; Qwen (千问) is the cross-device secondary executor and reads `AGENTS.md`. The two share the `Qwen` branch sequentially: commit and push before switching executor or device, and pull and re-read the state files on arrival. `main` remains the independent Codex workstream. `research_contract.yaml`, `SOUL.md` and `orchestration/PROTOCOL.md` now name both executors with the one-active-at-a-time rule; `PROJECT_STATE.yaml` records `active_branch: Qwen`. BMDL remains excluded; biomimetic research uses web-based deep search. No material order, synthesis, or experiment is authorized.

On the same date Pan Yao offered two optional biomimetic inspiration lines: (1) take the WWTP biological treatment unit itself as a prototype and decompose its mechanisms and design methods; (2) take pollutant-organ or tissue interactions as a prototype, already recorded in `research/evidence/ORGAN_ENRICHMENT_BIOMIMETIC_HEURISTIC.md`. The first line is now recorded in `research/evidence/BIOLOGICAL_TREATMENT_UNIT_BIOMIMETIC_HEURISTIC.md`. Both remain optional, non-scoring discovery heuristics, not gates or scoring items; they must not be force-fit, and their applicability to any candidate is judged by reasoning plus web-based deep research.
