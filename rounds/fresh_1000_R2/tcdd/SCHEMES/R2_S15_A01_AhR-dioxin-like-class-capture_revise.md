# R2_S15 · TCDD R2 — AhR-templated dioxin-like-class capture (pi-stack orthogonal to R1 halogen-bond) — revise

- Program: fresh_1000 R2 | Pollutant: TCDD | Tier 3 (Group C, dioxin) | breadth-first slot 1
- Status: **revise** (0 critical / 1 high) — promiscuity = class-capture; pg/L extreme-Kd + planar-host prior art cap ceiling
- Score: r1 **~78/100** (0c/1h), verdict revise, ceiling ~78-80
- Prototype: **PROTO_R2_007** aryl-hydrocarbon receptor (AhR) ligand-binding domain | Mechanism map: MECH_tcdd_001
- Orthogonality: R1 A01 (S50, revise ~70) occupied the **lateral-Cl halogen-bond / sigma-hole** axis; this slot uses **planar pi-stack + shape** (AhR recognition) — an orthogonal MECHANISM.

## Supervisor summary
TCDD's R1 best angle (A01, lateral-Cl halogen-bond) is capped by the sub-1-kJ/mol single-site aqueous halogen bond (ceiling
78-82, narrow path to 85). Rather than re-fight that occupied axis, R2 uses TCDD's OTHER evolved recognition: the aryl-hydrocarbon
receptor (AhR), a real high-affinity aqueous receptor for TCDD (direct tritiated-TCDD binding, cross-species). AhR physics =
planar pi-stacking + shape-complementary hydrophobic pocket. Because AhR is promiscuous across coplanar dioxin-like compounds
(other PCDD/F, dl-PCB), the translated host performs **dioxin-like-compound (DLC) CLASS capture**, not intra-dioxin selectivity.
Lands **revise** (not pass): class-capture (not single-congener) + planar-aromatic-host prior art + the pg/L target's extreme-Kd
demand.

## Scientific question
Can an electron-rich planar aromatic host (pi-stacking cleft shape-matched to the dioxin scaffold), templated on AhR's evolved
recognition, deliver high-affinity CLASS capture of dioxin-like compounds from water via pi-stacking + hydrophobic desolvation —
an orthogonal MECHANISM to the R1 lateral-Cl halogen-bond axis?

## Biological prototype evidence (H1)
| prototype | biological recognition | evidence tier | translation |
|---|---|---|---|
| Aryl-hydrocarbon receptor (AhR) LBD | direct high-affinity binding of tritiated-TCDD, cross-species (Gasiewicz & Rucci 1984) | fact (4th-level direct binding) | electron-rich planar pi-stacking cleft + shape-matched hydrophobic pocket (COF/cyclophane) |

- AhR is an evolved, aqueous-functional, high-affinity dioxin receptor — a strong biological anchor for a pi-stack/shape host.
- Honest caveat: AhR is PROMISCUOUS (dioxin-like class), so the translated recognition is class-level, not intra-congener.

## Biomimetic correspondence matrix
- **H1 (hard functional correspondence):** biological pi-stack/shape recognition of the planar dioxin (AhR) -> synthetic
  electron-rich planar pi-stacking cavity. Genuine mechanism-level correspondence (satisfies >=1 hard correspondence).
- Selectivity dimension: planar pi-stack + shape (DLC class) — orthogonal MECHANISM to R1 sigma-hole halogen bond.

## Material architecture
- Electron-rich extended-aromatic COF / cyclophane cleft, interlayer spacing shape-matched to the planar dioxin (pi-stack), in a
  hydrophobic pocket that desolvates the aromatic faces; captures the dioxin-like class. (pi-stack + desolvation give affinity;
  planar shape gives class selectivity vs non-planar co-contaminants.)

## Selectivity verdict + external gate
- **1 high (intrinsic):** AhR promiscuity -> the host captures the DLC class, not TCDD specifically; intra-PCDD/F selectivity is
  FM2-monotonic and NOT delivered. Honestly scoped as class-capture (mirrors ROX macrolide-class / BPA PXR-class capture).
- No critical issues (pi-stack + hydrophobic desolvation is a real, aqueous-viable high-affinity mode; AhR proves it).
- pg/L target: extreme-Kd demand is a materials challenge (noted, not disqualifying at design layer).

## Innovation checklist
- Novel biomimetic mapping (AhR pi-stack/shape -> DLC-class-capture host): **pass**
- Not a trivial logKow/hydrophobic design: **pass** (planar pi-stack + shape selectivity, orthogonal to occupied halogen bond)
- >=1 hard functional correspondence (H1): **pass**
- Prior-art delta: **borderline** — planar-aromatic dioxin hosts exist; AhR-templated DLC-class framing + orthogonality is the delta.

## Scoring (six-dimension, /100)
- Causal closed loop 20 -> 16 (pi-stack->class affinity plausible; intra-selectivity not delivered)
- Selective adsorption mechanism 25 -> 19 (class-level, not single-congener; capped by promiscuity)
- Artificial-material translatability 20 -> 16 (planar COF/cyclophane feasible; pg/L Kd hard)
- Originality 15 -> 10 (planar-host prior art; AhR-class framing is the delta)
- Falsifiable controls 10 -> 9 (planar vs non-planar + DLC panel + Cl->H series clean)
- Evidence completeness 10 -> 8 (AhR binding fact-tier; class-capture honestly scoped)
- **Total ~78/100** — revise (0c/1h)

## Residual value
- **Transferable positive knowledge:** when a pollutant's halogen-bond axis is R1-occupied, an evolved-receptor pi-stack/shape
  angle (AhR here) is the orthogonal-MECHANISM escape, delivering CLASS capture — carry the DLC-class-capture host to dl-PCB.
- New prototype PROTO_R2_007 (AhR LBD) added to library.
- Next: PCB-209.
