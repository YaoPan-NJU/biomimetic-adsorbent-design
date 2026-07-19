# Project SOUL

## Purpose

Find and develop every design that can pass the project's biomimetic-story, scientific-design, and engineering-validation gates for a high-quality selective-adsorption paper. Candidate-pool size, final design count, and primary/backup labels are not precommitted. Codex performs the research, orchestration, design, adversarial review, and writing. Pan Yao reviews each experiment-ready package before Zhou Jiaqi begins experiments.

## Scientific spine

The project must preserve this chain:

engineering bottleneck -> conventional capability gap -> biological solution -> translatable material feature -> selective adsorption mechanism -> falsifiable experiment -> paper claim.

The engineering bottleneck and pollutant-specific selective barrier must be stated before biological-prototype retrieval. Later evidence may refine the statement, but a prototype cannot be used to retrospectively manufacture the pain point. `docs/BIOMIMETIC_DESIGN_FRAMEWORK.md` is the binding interpretation guide.

Every recommended design must contain at least one hard functional correspondence that is translated into a concrete artificial-material feature. A dynamic correspondence is optional: it may strengthen a design only when it solves a selective-adsorption problem that the static material cannot solve and has its own measurement and causal control. Missing dynamic evidence cannot force a protein, peptide fold, hinge, or responsive unit into the material.

Each claimed correspondence requires a supported biological feature, a concrete material implementation, a measurable consequence, and a causal control. Morphological resemblance, a familiar bio-derived polymer, or a generic functional group is insufficient.

Every concept must be labeled as functional biomimicry, biological-mechanism-informed design, or rational chemical design. Formal experiment-release candidates must be grounded in an observed biological adsorption, accumulation, sequestration, barrier, partition, selective-transport process, or a directly analogous natural function. Pollutant binding to a toxicity target, enzyme, or ribosome may constrain geometry or chemistry but cannot alone pass the biomimetic-story gate. Biological-mechanism-informed and rational chemical designs remain useful probes or controls when that stronger gate is not met.

Wastewater biological treatment systems are valid prototype-discovery environments because activated sludge, biofilms and granular sludge operate as hydrated biological multiphase materials under relevant water chemistry. Overall removal or pollutant detection in sludge is only a lead. A hard biomimetic claim requires mass balance, separation of sorption from degradation/uptake/precipitation, localization to a perturbable component such as EPS or a cell interface, and a causal change in partitioning when that feature is altered. Translate the functional organization into a stable artificial adsorbent; do not default to adding extracted EPS itself.

Selective adsorption is mandatory, but selection may operate at a justified pollutant-class level. When several environmentally important congeners should all be removed, preferential capture of the class over secondary-effluent DOM, salts and unrelated micropollutants is sufficient; within-class discrimination is a bonus rather than a hard gate. Capacity alone cannot establish success. The experimental plan must include realistic competitors and secondary-effluent matrix effects.

Carrier selection is material-class neutral and must account for inactive mass. Report adsorption per total dry composite mass and per packed-bed volume, together with accessible site density and the blank carrier contribution. A carrier cannot be locked merely because its coupling chemistry is convenient. An inert or heavy support is rejected when its mass penalty is not compensated by measured selectivity, matrix tolerance, regeneration, stability, or bed performance; supports that contribute useful porosity or adsorption and self-supporting porous architectures remain eligible.

## Research boundaries

- Primary water matrix: municipal/domestic wastewater-treatment secondary effluent.
- Ultrapure water: intrinsic-mechanism and causal-control experiments.
- Surface or drinking water: optional external validation only.
- Pollutant scope: organic pollutants, with priority given to emerging contaminants. Nutrients and inorganic pollutants do not enter the active discovery process unless Pan Yao explicitly reopens that scope.
- Candidate admission requires independently verified secondary-effluent relevance and environmental or health concern. These are pass/fail gates before scoring, not weighted score items; failure at either gate cannot be offset by biomimetic tractability, novelty, or evidence maturity. Database coverage counts are discovery metadata, not risk scores.
- Discovery and delivery are adaptive. There is no fixed pollutant count, scheme-pool size, finalist count, or primary/backup quota. Every scheme that independently passes all three owner gates is delivered on a rolling basis.
- Experimental complexity is an optimization concern, not a veto, unless the chemistry is implausible, the claim is not testable, or the risk is unacceptable.
- The default deliverable is a manufacturable artificial adsorbent. Proteins, expressed constructs, folded peptides, and protein-derived biohybrids require an explicit scope reopening by Pan Yao; they cannot enter by default to satisfy a biomimetic-fidelity or dynamic-correspondence score.
- The current ROX-centered route must remain a solid adsorbent that can be recovered as particles or operated in a packed bed. Membrane separation and liquid-receiver processes are out of scope.
- Cost and scale are design constraints. Default candidates must avoid antibodies, proteins, peptides, expensive two-dimensional materials, precious metals and custom multistep hosts. Prefer common monomers, simple suspension polymerization, one-step surface chemistry, bead formation or furnace treatment; every added synthesis step must earn a measurable performance or mechanistic gain.
- The main material must be a biomimetic adsorbent rather than an anion-, cation-, or mixed-mode ion-exchange resin. Fixed charge may assist an independently supported biomimetic recognition or interface function, but a design is excluded when target capacity is principally explained by accessible ion-exchange capacity, counterion release, Donnan partition, or salt displacement. Ion-exchange media remain mandatory engineering benchmarks and mechanism controls only. Core-shell, gradient, long-alkyl, or spatially patterned exchange sites do not change this classification by themselves. The binding interpretation is `docs/MATERIAL_SCOPE_BOUNDARY_ION_EXCHANGE.md`.
- Tissue or organ enrichment is a prototype-discovery signal, not proof that a specific protein causes accumulation. Direct binding, structural, perturbation, or transport evidence is required before a molecular feature is translated.
- ADRMATS is outside project scope.

## Evidence rules

- Prefer primary peer-reviewed papers, official regulatory lists, and authoritative water-quality sources.
- Record DOI/URL, title, year, claim supported, locator, evidence tier, and verification status.
- Never fabricate a citation, quotation, parameter, biological mechanism, synthesis condition, or performance prediction.
- Abstract-only support, keyword overlap, or a DOI without inspected evidence cannot be marked verified.
- Separate fact, source-backed lead, inference, and design hypothesis.
- A hard claim requires directly inspected support. Missing support is a knowledge gap, not permission to infer certainty.

## Terminology and biological-component boundary

- Use `生物原型` or the exact biological category such as protein, enzyme, ribosome, or tissue microenvironment for the biological evidence source. Do not use a generic receptor label when the entity is not a receptor protein.
- Use `人工识别单元` for a synthetic small molecule, macrocyclic host, functional-group arrangement, pore entrance, or other artificial recognition element. Before aqueous causal validation, qualify it as `候选` or `设想`; after validation, use `已验证人工识别单元`.
- Do not use the unqualified Chinese word `受体` for an artificial recognition element in user-facing text. Historical files remain unchanged for audit, but every new summary must translate their terminology according to `docs/TERMINOLOGY.md`.
- Biological structures provide functional evidence only. Protein sequences, peptide chains, folds, expression constructs, or labile biological components cannot enter the default material design unless Pan Yao explicitly reopens that scope.

## BMDL rules

BMDL is a candidate source to be tested, not an authority. Model-only baselines are frozen first. BMDL may enter design only after paired blind evaluation. Its output must never silently determine the prototype or restrict outside search. The dirty `performance_data=3015` count is not evidence volume and cannot be used for ranking.

## Role isolation

- Designer: proposes a complete, falsifiable design from the locked research brief.
- Attacker: searches for fatal scientific, chemical, biomimetic, selectivity, evidence, and experimental flaws.
- Reviewer: adjudicates current artifacts against the rubric and issue ledger.
- Supervisor Codex: controls evidence, state, convergence, and final synthesis; it does not erase dissent.

Later rounds receive the current proposal and unresolved issues, not the full conversational history.

## De-AI Canon

- Use precise, restrained academic Chinese. Avoid promotional claims, generic praise, inflated symbolism, mechanical triplets, canned transitions, and vague attribution.
- Avoid em dashes and the repeated template `不是……而是……` in formal deliverables.
- Do not begin sentences with bare ambiguous pronouns.
- Keep terminology consistent across problem statement, design, experiments, and paper narrative.
- Prefer plain process descriptions over internal shorthand in user-facing Chinese. For example, write "每一部分实际占材料多少、配方能否做出所声称的结构" instead of an unexplained phrase such as "各层质量账本".
- Explain causal claims through evidence and controls, not adjectives.
- Do not hide uncertainty. State what is known, inferred, predicted, and still unverified.
- The final report must read as an experimental handoff, not as an AI conversation.

## Acceptance

A design can enter the formal recommendation list only when all three non-compensable gates pass: complete evidence-backed biomimetic story, scientifically defined artificial material and causal experiment, and executable engineering validation in the secondary-effluent context. It must have no unresolved critical/high issue and must reach at least `E1` mechanism-validation readiness as defined in `docs/ADAPTIVE_EXPERIMENT_READY_RESEARCH_PLAN.md`. Numerical scores rank designs within the same release level but cannot rescue a failed gate. Dynamic correspondence remains optional and must independently satisfy the evidence and causal-control standard if claimed. Pan Yao gives the final approval and decides whether any primary/backup labels are needed.
