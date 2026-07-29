# R2_S10 · DDT R2 — halogen-bond sigma-hole PATTERN (transthyretin/thyroxine prototype) — revise_with_phase0_prerequisite

- Program: fresh_1000 R2 | Pollutant: DDT | Tier 2 (Group C, organochlorine) | breadth-first slot 1
- Status: **revise_with_phase0_prerequisite** (0 critical / 1 high, Phase-0 DFT gate pending)
- Score: r1 **~79/100** (0c/1h), verdict revise, ceiling ~78-80
- Prototype: **PROTO_R2_006** transthyretin (TTR) halogen-bond channel | Mechanism map: MECH_ddt_001
- Orthogonality: R1 S51_A01 (86) occupied the REACTIVE beta-elimination axis + whole-propeller SHAPE axis; this slot reads the para-Cl **halogen-bond position pattern** (orthogonal axis).

## Supervisor summary
DDT's R1 pass (S51_A01=86) is a reactive-recognition design (dehydrochlorinase beta-elimination dual-motif) with a shape binary
switch. The one orthogonal angle R2 offers is a **halogen-bond sigma-hole pattern**: recognize the two aromatic para-Cl at the
fixed 2,2-bis(4-chlorophenyl) geometry via a Lewis-base array (backbone C=O / pyridyl-N), templated on transthyretin's documented
biological halogen bonds to thyroxine iodines. This is orthogonal to both reactivity and whole-shape. It lands **revise** (not
pass) because aqueous **aromatic C-Cl** halogen bonds are weak (weaker than the C-I of thyroxine; DCP26-A04 regime), so absolute
ng/L affinity needs a Phase-0 DFT gate, and halogen-bonding hosts have prior art that caps originality.

## Scientific question
Can a geometric **pattern** of Lewis-base acceptors, positioned to simultaneously engage BOTH para-Cl sigma-holes of DDT (fixed
diaryl geometry), deliver aqueous selectivity for DDT over co-occurring OCP (DDD/DDE/methoxychlor) via halogen-bond geometry
rather than reactivity or bulk hydrophobic shape?

## Biological prototype evidence (H1)
| prototype | biological halogen bond | evidence tier | translation |
|---|---|---|---|
| Transthyretin (TTR) T4-binding channel | thyroxine iodine ... backbone C=O halogen bonds documented in TTR crystal structures | fact (structural) | Lewis-base (C=O / pyridyl-N) array reading aromatic C-Cl sigma-holes at a fixed diaryl geometry |

- Halogen bond directionality (C-X...B ~180 deg) makes a two-point para-Cl pattern geometrically discriminating (not a single
  monotonic contact) — this is the non-monotonic escape from FM2.
- Honest caveat: C-Cl sigma-hole << C-I; the TTR prototype uses iodine. Translation distance is real (documented in card).

## Biomimetic correspondence matrix
- **H1 (hard functional correspondence):** biological halogen bond (TTR/thyroxine) -> synthetic halogen-bond-acceptor pattern.
  This is a genuine physics-level correspondence (same interaction type), satisfying the >=1 hard-correspondence requirement.
- Selectivity dimension: two-point para-Cl geometric pattern (orthogonal to reactivity + whole-shape).

## Material architecture
- Halogen-bond-acceptor pattern host: pyridyl-N / amide-C=O array pre-positioned (rigid COF or discrete cage) to match the
  ~across-the-molecule para-Cl...para-Cl separation of the bis(4-chlorophenyl) geometry, in a hydrophobic pocket that desolvates
  the aromatic rings (partitioning provides the bulk affinity floor; halogen-bond pattern provides the selectivity).

## Selectivity verdict + external gate
- **Phase-0 DFT gate (pending, external):** compute aqueous two-point C-Cl...(C=O/N) halogen-bond energy + geometric pattern gain
  vs single-Cl contacts; go/no-go on whether the pattern clears ng/L absolute affinity. This is the 1 remaining **high** issue.
- No critical issues (halogen bond is a real interaction; the design does not rely on a thermodynamically self-falsifying step).

## Innovation checklist
- Novel biomimetic mapping (TTR halogen bond -> DDT para-Cl pattern): **pass**
- Not a trivial logKow/hydrophobic design: **pass** (halogen-bond geometric pattern)
- >=1 hard functional correspondence (H1): **pass**
- Prior-art delta: **borderline** — halogen-bonding hosts exist; the two-point para-Cl PATTERN + TTR mapping is the novel delta.

## Scoring (six-dimension, /100)
- Causal closed loop 20 -> 16 (pattern->selectivity plausible; absolute affinity Phase-0-pending)
- Selective adsorption mechanism 25 -> 20 (orthogonal halogen-bond pattern; aqueous C-Cl weak caps it)
- Artificial-material translatability 20 -> 16 (halogen-bond COF feasible; geometric templating nontrivial)
- Originality 15 -> 10 (halogen-bonding-host prior art caps; TTR mapping is the delta)
- Falsifiable controls 10 -> 9 (DDD/DDE/methoxychlor + Cl->H control series clean)
- Evidence completeness 10 -> 8 (TTR halogen bond fact-tier; DDT-specific aqueous energy Phase-0-pending)
- **Total ~79/100** — revise_with_phase0_prerequisite (0c/1h)

## Residual value
- **Transferable positive knowledge:** aromatic C-Cl halogen-bond PATTERN recognition (two-point, geometry-directed) is the
  orthogonal escape from FM2 hydrophobic-monotonicity for polychloroaromatic OCP — carry to PCB-209 / BDE-209 (polyhalogen
  pattern targets) where more/heavier halogens make the halogen bond stronger and the pattern richer (likely higher ceiling there).
- New prototype PROTO_R2_006 (TTR halogen bond) added to library.
- Next: DDE.
