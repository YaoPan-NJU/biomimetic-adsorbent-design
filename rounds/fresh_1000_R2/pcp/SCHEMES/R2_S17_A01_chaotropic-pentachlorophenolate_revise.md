# R2_S17 · PCP R2 — chaotropic recognition of the pentachlorophenolate anion (PROTO_R2_002 reuse) — revise

- Program: fresh_1000 R2 | Pollutant: PCP | Tier 2 (Group B, chlorophenol) | breadth-first slot 1
- Status: **revise** (0 critical / 1 high) — chlorination-gradient favors PCP; intra-penta/tetra narrow + chaotropic-host prior art cap ceiling
- Score: r1 **~78/100** (0c/1h), verdict revise, ceiling ~78-80
- Prototype: **PROTO_R2_002** Hofmeister/chaotropic selective channel (REUSE from PFBS/PFHxS) | Mechanism map: MECH_pcp_001
- Orthogonality: R1 mapped 5 axes (A01 TTR halogen-bond, A02 H-bond, A03 five-point σ-hole, A04 β-CD shape [self-eval pass], A07 reductive); this slot uses a **hydration-thermodynamic (chaotropic)** axis — orthogonal to all five.

## Supervisor summary
PCP at neutral pH is the **pentachlorophenolate anion** — large, hydrophobic, low-charge-density (charge delocalized over the
phenolate O and the electron-poor perchloro ring). That makes it a **chaotropic** anion (Hofmeister). R1 mapped PCP's halogen-bond
(A01 TTR / A03 five-point σ-hole), H-bond (A02), shape/CD (A04, the self-eval pass), and reactive (A07) axes — but NOT a
hydration-thermodynamic axis. R2 therefore reuses **PROTO_R2_002** (the chaotropic/Hofmeister selective channel from PFBS/PFHxS):
a high-energy-water-release cavity that binds the weakly-hydrated PCP anion and rejects strongly-hydrated competitors. Lands
**revise** (not pass): the chlorination gradient correctly favors PCP (penta = most chaotropic chlorophenol), but intra-penta/tetra
selectivity is narrow and chaotropic anion-host prior art caps originality.

## Scientific question
Can a chaotropic-selective (high-energy-water-release) cavity capture the weakly-hydrated pentachlorophenolate anion from water,
selecting it over strongly-hydrated inorganic anions (Cl⁻, sulfate) and less-chlorinated (more-hydrated) chlorophenolates — an
orthogonal hydration-thermodynamic axis to R1's halogen-bond / H-bond / shape / reactive angles?

## Biological prototype evidence (H1)
| prototype | biological recognition | evidence tier | translation |
|---|---|---|---|
| Biological anion channels' Hofmeister/chaotropic selectivity (PROTO_R2_002) | anion channels rank permeant anions by the chaotropic (lyotropic) series via dehydration energetics | fact | high-energy-water-release synthetic cavity (cucurbituril/CD-based) tuned to the chaotropic pentachlorophenolate |

- H1 (hard functional correspondence): biological chaotropic/Hofmeister anion selectivity -> synthetic high-energy-water-release
  cavity (same hydration-thermodynamic physics). Satisfies >=1 hard correspondence.
- Selectivity dimension: hydration thermodynamics (chaotropicity), orthogonal to all R1-mapped axes.

## Material architecture
- Chaotropic-selective macrocyclic cavity (cucurbituril/cyclodextrin-derived or a rigid hydrophobic-lined pore) sized to the
  pentachlorophenolate, engineered to release high-energy confined water on binding the weakly-hydrated anion; hydrophobic lining
  rejects strongly-hydrated small anions and less-chlorinated phenolates.

## Selectivity verdict + external gate
- **1 high (intrinsic):** intra-chlorophenol selectivity is a chaotropic GRADIENT (monotonic in chlorination) — it correctly
  favors PCP (the most chlorinated/chaotropic), but discrimination against tetrachlorophenolate (4 Cl) is narrow. Honestly scoped.
- No critical issues (chaotropic anion binding is real, aqueous-viable supramolecular chemistry; correct selectivity direction).
- Absolute Kd at ng/L: calorimetry (ITC) go/no-go recommended (external gate; non-blocking).

## Innovation checklist
- Novel biomimetic mapping (chaotropic channel -> pentachlorophenolate capture): **pass** (first chaotropic application to an organic chlorophenolate here)
- Not a trivial logKow/hydrophobic design: **pass** (hydration-thermodynamic selectivity, not bulk partitioning)
- >=1 hard functional correspondence (H1): **pass**
- Prior-art delta: **borderline** — chaotropic anion hosts exist (inorganic/PFAS); organic-chlorophenolate application + chlorination-gradient is the delta.

## Scoring (six-dimension, /100)
- Causal closed loop 20 -> 16 (chaotropic->selectivity plausible, correct direction; absolute ng/L Kd calorimetry-pending)
- Selective adsorption mechanism 25 -> 20 (orthogonal hydration axis; intra-penta/tetra narrow)
- Artificial-material translatability 20 -> 16 (cucurbituril/CD chaotropic hosts feasible)
- Originality 15 -> 10 (chaotropic anion-host prior art caps; organic-chlorophenolate application is the delta)
- Falsifiable controls 10 -> 9 (chlorophenol chlorination series + Hofmeister-series anion panel clean)
- Evidence completeness 10 -> 8 (chaotropic physics fact-tier; PCP-specific Kd calorimetry-pending)
- **Total ~78/100** — revise (0c/1h)

## Residual value
- **Transferable positive knowledge:** the chaotropic recognition principle (PROTO_R2_002) extends beyond PFAS to any large,
  hydrophobic, weakly-hydrated ORGANIC anion (chlorophenolates, other hydrophobic acid anions) — a broad reuse of the PFAS-derived
  prototype. Chlorination/hydrophobicity gradient gives correct-direction selectivity for the most-substituted congener.
- PROTO_R2_002 applicable_pollutants extended to include pcp (no new prototype).
- Next: HCBD.
