# R2_S19 · Chloroform R2 — honest near-exhaustion (too-small-no-handle wall)

- Program: fresh_1000 R2 | Pollutant: Chloroform | Tier 3 (Group B) | breadth-first slot 1
- Status: **terminated / honest near-exhaustion** (r1 structural; no viable orthogonal angle)
- Score: r1 **~42/100**, verdict terminate, 1 critical (structural)
- Mechanism map: MECH_chloroform_001

## Summary
R1 A01 (alpha-CD size matching) TERMINATED at 45 (ug/L affinity gap + 0.5 Angstrom size difference + innovation checklist all
fail). Chloroform (CHCl3) is the **smallest / hardest target** in the program: a 5-atom molecule with only 3 ALIPHATIC C-Cl and a
weak C-H, no aromatic ring, no charge, no distinctive polar group. R2 candidates all fail (X): (a) **halogen-bond on 3 aliphatic
C-Cl** — sp3 sigma-holes are weak (aromatic-only boundary, cf beta-HCH) + only 3 Cl (sparse) + ug/L affinity gap; (b) **weak C-H
H-bond donor** — a single weak C-H...B contact cannot deliver ug/L aqueous affinity/selectivity; (c) **size/confinement** — that
is the R1 alpha-CD axis (occupied, terminated), and 0.5 A discrimination vs co-THMs is below reliable aqueous size resolution.

## Designer/Attacker/Reviewer r1 (condensed)
- Designer: proposed aliphatic-Cl halogen-bond + confinement; self-flagged the ug/L affinity gap.
- Attacker C1 (critical, structural): chloroform has no aromatic/charge/polar handle; only 3 sp3 C-Cl (weak halogen-bond) + a weak
  C-H + a size/shape axis already R1-tried-and-terminated on the ug/L affinity gap. No orthogonal-and-viable angle. Not rebuildable.
- Reviewer: C1 upheld structural. Score ~42. Terminate (no rebuild).

## Residual value (negative knowledge)
- **Chloroform too-small-no-handle wall**: the clearest small-molecule exhaustion case — a 5-atom neutral THM with only weak
  aliphatic-Cl + a size handle (R1-terminated on ug/L affinity). Real-world removal is volatility/air-stripping-driven, not
  selective adsorption. Honest near-exhaustion (transferable: selective aqueous adsorption is infeasible for tiny neutral THMs).
- Next: BDE-209 (final pollutant).
