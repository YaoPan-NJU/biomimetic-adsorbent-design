# R2_S08 · ROX R2 — cation-pi aromatic cage macrolide-class capture (revise)

- Program: fresh_1000 R2 | Pollutant: Roxithromycin | Tier 3 (Group E) | breadth-first slot 1
- Status: **revise** (r1 66 -> r2 ~81; 0 critical / 1 high; ceiling ~82-83)
- Angle: R2_A01 cation-pi aromatic cage (protonated desosamine amine) + 14-membered size window; prototype AChE aromatic-gorge cation-pi (PROTO_R2_005)

## Summary
Orthogonal to R1's A01 (NPET nucleobase H-bond array), A02 (oxime-ether H-bond, negative alpha), A06 (esterase reactive).
Mechanism: an aromatic-rich electron-dense macrocyclic cage (calixarene/pillararene/aromatic HCP) recognizes the protonated
desosamine tertiary amine (pKa~8.8, cationic at env pH) via **cation-pi** (ion-quadrupole), gated by a **14-membered
macrocycle size window**. Selectivity = macrolide-CLASS capture (macrolides vs non-macrolide matrix; co-occurring macrolide
antibiotics erythromycin/clarithromycin/azithromycin all captured — real engineering value), NOT intra-macrolide (which R1
A01 partially addresses via C9 oxime probe).

## Designer/Attacker/Reviewer (condensed, r1->r2)
- Designer r1: cation-pi cage + size window; prototype AChE gorge cation-pi (Dougherty, textbook biological cation-pi of
  protonated/quaternary amines). Honest: class-wide (all macrolides cationic).
- Attacker r1: **C1** cation-pi to a *tertiary* protonated amine is weaker than to quaternary ammonium; water competition;
  class-capture not intra-selective; macrolide-CD inclusion precedent (gamma-CD, erythromycin-beta-CD). **H** originality (CD
  inclusion prior art).
- Designer r2: reframe as macrolide-class removal (engineering value) + cation-pi × size-window causal controls (cation-pi
  kill = electron-poor cage control; size series; N-methylated-amine vs des-amine control). Cation-pi to tertiary-ammonium is
  moderate but real (survives in water per AChE). ITC go/no-go on cation-pi magnitude.
- Reviewer r2: C1 -> resolved to borderline (cation-pi moderate, size-window adds orthogonality, class-capture value real);
  residual **1 high** = originality capped by CD-inclusion prior art + class-capture (not intra-macrolide) + cation-pi
  magnitude to tertiary amine needs ITC. Score ~81. **revise** (ceiling ~82-83). Not 85.

## Scoring (r2): causal 16 / selectivity 16 / translatability 15 / originality 10 / falsifiability 9 / evidence 8 = ~81/100
## Evidence: AChE cation-pi (Dougherty, textbook, fact); macrolide-CD inclusion (gamma-CD docking; erythromycin-beta-CD; directional prior art, title-level); ROX profile inherited R1 (verified).

## Residual value
- Transferable: cation-pi aromatic-cage recognition of protonated-amine pharmaceuticals (macrolides, aminoglycosides,
  alkaloids) = a reusable class-capture axis for cationic-amine micropollutants; orthogonal to H-bond/reactive routes.
- New prototype PROTO_R2_005 (AChE aromatic-gorge cation-pi). Mechanism MECH_rox_001.
- Next: Octocrylene.
