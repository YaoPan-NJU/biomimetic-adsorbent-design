# R2_S20 · BDE-209 R2 — honest near-exhaustion (A07 passed + halogen-bond R1-terminated re DBDPE) — FINAL SLOT (20/20)

- Program: fresh_1000 R2 | Pollutant: BDE-209 | Tier 3 (Group B) | breadth-first slot 1 — **FINAL pollutant, 20/20 coverage**
- Status: **terminated / honest near-exhaustion** (r1 best angle occupied + halogen-bond R1-explored-terminated)
- Score: r1 **~46/100**, verdict terminate, 1 critical (structural)
- Mechanism map: MECH_bde209_001

## Summary
R1 A07 PASSED at 85 (r5, 9th program pass; occupied best angle). Critically, R1 A03 (**sigma-hole halogen-bond ARRAY**) was worked
to r5 and **TERMINATED**: aqueous halogen bond weak + **DBDPE (decabromodiphenyl ETHANE, the replacement) is Br-pattern-
indistinguishable** from BDE-209 (identical 10-Br pattern; differ ONLY in ether-O vs ethane bridge). R2 candidates all fail (X):
(a) **halogen-bond PATTERN on 10 aromatic Br (PROTO_R2_006 transfer)** — R1-DEDUP fail (A03 tried) AND structurally defeated by
DBDPE Br-pattern degeneracy (a halogen-pattern host cannot resolve ether-vs-ethane bridge); (b) **ether-O recognition** (the one
distinguishing feature) — the ether-O is a weak H-bond acceptor STERICALLY SHIELDED between two perbrominated rings (buried); (c)
**AhR planar π-stack (PROTO_R2_007)** — BDE-209 is NON-planar (deca-substitution + ether bridge force a large twist).

## Designer/Attacker/Reviewer r1 (condensed)
- Designer: proposed the PROTO_R2_006 halogen-bond pattern (aromatic C-Br stronger than C-Cl — the "highest-ceiling" transfer target);
  on R1-DEDUP found A03 already tried-and-terminated, defeated by DBDPE degeneracy.
- Attacker C1 (critical, structural): A07 passed (occupied); the halogen-pattern route is R1-terminated AND competitor-degenerate
  (DBDPE); the only distinguishing ether-O is sterically buried; AhR π-stack fails (non-planar). No orthogonal-and-viable angle. Not rebuildable.
- Reviewer: C1 upheld structural. Score ~46. Terminate (no rebuild).

## Residual value (negative knowledge)
- **CLOSES the DDT halogen-bond-pattern (PROTO_R2_006) transfer analysis** across all polyhalogen-aromatic OCP: the route needs
  (i) AROMATIC halogen (not aliphatic — cf beta-HCH), (ii) the halogen pattern to be competitor-DISTINGUISHING (fails BDE-209 vs
  DBDPE), and (iii) the halogen-bond axis to be R1-unoccupied (fails TCDD/PCB/BDE). DDT is the one target where all three held.
- **20/20 COVERAGE COMPLETE — breadth-first (M2) achieved.**
- Next: full milestone / completion audit.
