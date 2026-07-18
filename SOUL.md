# Project SOUL

## Purpose

Produce one experiment-ready primary design and one backup design for a selectively adsorbing biomimetic material suitable for a high-quality environmental/materials paper. Codex performs the research, orchestration, design, adversarial review, and writing. Pan Yao reviews the package before Zhou Jiaqi begins experiments.

## Scientific spine

The project must preserve this chain:

engineering bottleneck -> conventional capability gap -> biological solution -> translatable material feature -> selective adsorption mechanism -> falsifiable experiment -> paper claim.

The engineering bottleneck and pollutant-specific selective barrier must be stated before biological-prototype retrieval. Later evidence may refine the statement, but a prototype cannot be used to retrospectively manufacture the pain point. `docs/BIOMIMETIC_DESIGN_FRAMEWORK.md` is the binding interpretation guide.

The primary design must contain at least one hard functional correspondence that is translated into a concrete artificial-material feature. A dynamic correspondence is optional: it may strengthen a design only when it solves a selective-adsorption problem that the static material cannot solve and has its own measurement and causal control. Missing dynamic evidence cannot force a protein, peptide fold, hinge, or responsive unit into the material.

Each claimed correspondence requires a supported biological feature, a concrete material implementation, a measurable consequence, and a causal control. Morphological resemblance, a familiar bio-derived polymer, or a generic functional group is insufficient.

Every concept must be labeled as functional biomimicry, biological-mechanism-informed design, or rational chemical design. Only the first two can contribute a biological hard correspondence; rational chemical designs remain useful controls or independent routes but cannot be relabeled through a generic protein-pocket analogy.

Selective adsorption is mandatory. Capacity alone cannot establish success. The experimental plan must include realistic competitors and secondary-effluent matrix effects.

Carrier selection is material-class neutral and must account for inactive mass. Report adsorption per total dry composite mass and per packed-bed volume, together with accessible site density and the blank carrier contribution. A carrier cannot be locked merely because its coupling chemistry is convenient. An inert or heavy support is rejected when its mass penalty is not compensated by measured selectivity, matrix tolerance, regeneration, stability, or bed performance; supports that contribute useful porosity or adsorption and self-supporting porous architectures remain eligible.

## Research boundaries

- Primary water matrix: municipal/domestic wastewater-treatment secondary effluent.
- Ultrapure water: intrinsic-mechanism and causal-control experiments.
- Surface or drinking water: optional external validation only.
- Pollutant scope: organic pollutants, with priority given to emerging contaminants. Nutrients and inorganic pollutants do not compete in the main funnel unless Pan Yao explicitly reopens that scope.
- Candidate admission requires independently verified secondary-effluent relevance and environmental or health concern. These are pass/fail gates before scoring, not weighted score items; failure at either gate cannot be offset by biomimetic tractability, novelty, or evidence maturity. Database coverage counts are discovery metadata, not risk scores.
- Funnel: 20 pollutant_kb pollutants -> environmental/schemeability pre-screen -> 10 mechanism-distinct schemes -> 5 recommended schemes -> 1 primary + 1 backup.
- Experimental complexity is an optimization concern, not a veto, unless the chemistry is implausible, the claim is not testable, or the risk is unacceptable.
- The default deliverable is a manufacturable artificial adsorbent. Proteins, expressed constructs, folded peptides, and protein-derived biohybrids require an explicit scope reopening by Pan Yao; they cannot enter by default to satisfy a biomimetic-fidelity or dynamic-correspondence score.
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
- Explain causal claims through evidence and controls, not adjectives.
- Do not hide uncertainty. State what is known, inferred, predicted, and still unverified.
- The final report must read as an experimental handoff, not as an AI conversation.

## Acceptance

The primary design passes only when it scores at least 85/100, has no unresolved critical/high issue, contains at least one hard functional correspondence implemented in an artificial material, provides a credible bench-scale synthesis SOP, and maps every central claim to a measurement and causal control. If a dynamic correspondence is claimed, it must independently satisfy the same evidence and causal-control standard; it is not required for passage. Pan Yao gives the final approval.
