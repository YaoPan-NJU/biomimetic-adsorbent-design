# R2_S18 · HCBD R2 — honest near-exhaustion (four-axes-R1-occupied, inert perchloro-diene)

- Program: fresh_1000 R2 | Pollutant: HCBD | Tier 3 (Group B) | breadth-first slot 1
- Status: **terminated / honest near-exhaustion** (r1 heavily occupied; no viable orthogonal angle)
- Score: r1 **~45/100**, verdict terminate, 1 critical (structural)
- Mechanism map: MECH_hcbd_001

## Summary
R1 covered HCBD (hexachlorobutadiene, C4Cl6) with FOUR axes: A02 (in_progress, S-grade) = **halogen-bond-donor-array x hydrophobic
cavity**; SL05 (revise) = **CD-cavity shape**; SL12 (revise) = **corrinoid reductive** reactive capture. HCBD is a neutral, inert,
perchloro-diene with **no polar / no aromatic / no charge handle** — its only recognition handles are halogen-bond + hydrophobic
shape + reactive, all R1-occupied. R2 candidates all fail (X): (a) **chaotropic** — needs an ion; HCBD is neutral (N/A); (b)
**halogen-bond pattern** on the 6 vinylic C-Cl — R1-DEDUP fail (A02 already halogen-bond-donor-array) + vinylic sp2 C-Cl weaker
than aromatic; (c) **diene π / conformer** — π is R1-occupied (shape/hydrophobic) and near-degenerate with the HCE competitor.

## Designer/Attacker/Reviewer r1 (condensed)
- Designer: proposed vinylic-Cl halogen-bond pattern + diene-π; self-flagged R1 A02 overlap.
- Attacker C1 (critical, structural): HCBD's three recognition handles (halogen-bond, hydrophobic shape, reactive) are all
  R1-occupied; being neutral it has no chaotropic/charge axis, and it has no polar/aromatic handle. No orthogonal angle. Not rebuildable.
- Reviewer: C1 upheld structural. Score ~45. Terminate (no rebuild).

## Residual value (negative knowledge)
- **HCBD inert-perchloro-diene wall**: a small neutral inert perchloro-diene offers only halogen-bond + hydrophobic + reactive
  handles (all R1-occupied) and NO charge/aromatic/polar axis for an orthogonal R2 angle. Honest near-exhaustion.
- Next: Chloroform.
