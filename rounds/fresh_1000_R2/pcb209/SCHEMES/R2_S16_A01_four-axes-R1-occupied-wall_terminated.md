# R2_S16 · PCB-209 R2 — honest near-exhaustion (four-axes-R1-occupied + DDT-transfer-already-occupied wall)

- Program: fresh_1000 R2 | Pollutant: PCB-209 | Tier 3 (Group C) | breadth-first slot 1
- Status: **terminated / honest near-exhaustion** (r1 heavily occupied; no viable orthogonal angle)
- Score: r1 **~45/100**, verdict terminate, 1 critical (structural — orthogonal space R1-exhausted)
- Mechanism map: MECH_pcb209_001

## Summary
R1 covered PCB-209 (decachlorobiphenyl) with FOUR angles: A01A03 (in_progress, S-grade) = **torsional profile x C-Cl halogen-bond
ARRAY**; SL02 (revise 64) = torsional-complementary cavity; SL06 (revise) = **PXR large-soft-cavity**; SL08 (revise) =
**multi-epitope orthogonal receptor**. So the halogen-bond-array, torsional-shape, PXR-soft-cavity and multi-epitope axes are ALL
R1-occupied. **Honest correction:** the DDT PROTO_R2_006 halogen-bond-PATTERN transfer — which the DDT slot flagged as promising
for PCB-209 (more/heavier halogens) — is here found to be **R1-occupied** (A01A03 already IS torsional x halogen-bond array); the
polyhalogen-aromatic pattern route was independently reached in R1. R2 residual candidates all fail (X): (a) halogen-bond pattern
(R1-DEDUP fail, occupied); (b) pi-acid EDA/CT on electron-poor decachlorobiphenyl (weak in water, prior-art-crowded, PCB-class-
degenerate); (c) atropisomer chirality (deca-PCB is symmetric, low twist barrier, not a stable atropisomer; shape R1-occupied).
Compounding: **no PCB-209 monomer measured in any real water body post-2019** (Wolkersdorfer 2025) — low real-world priority.

## Designer/Attacker/Reviewer r1 (condensed)
- Designer: attempted the polyhalogen halogen-bond-pattern (DDT PROTO_R2_006 transfer) as the "highest-ceiling" OCP target; on
  R1-DEDUP check found R1 A01A03 already occupies torsional x halogen-bond array.
- Attacker C1 (critical, structural): R1 occupies four axes including the exact halogen-bond-array route R2 proposed; residual
  pi-acid/atropisomer angles are weak/degenerate/occupied. No orthogonal-and-viable angle remains. Not rebuildable.
- Reviewer: C1 upheld structural. Score ~45. Terminate (no rebuild).

## Residual value (negative knowledge)
- **DDT-transfer landed but R1-occupied**: the DDT PROTO_R2_006 halogen-bond-PATTERN route DOES apply to PCB-209 (10 aromatic Cl,
  rich pattern) — confirming the transfer hypothesis — but R1 already occupies it (A01A03). Honest: the hypothesis is validated as
  a real route yet yields no NEW R2 angle here. The transfer's remaining unclaimed target is BDE-209 (check next: R1 A03 was a
  sigma-hole halogen-bond array, terminated — so likely occupied there too).
- PCB-209 R2 = honest near-exhaustion. **Group C complete: 7/7 pollutants covered (DDT revise + 6 near-exhaustion/terminate).**
- Next: Group B (PCP).
