# R2_S07 · DCP26 R2 — honest near-exhaustion (regio-isomer monotonic wall)

- Program: fresh_1000 R2 | Pollutant: 2,6-dichlorophenol | Tier 2 (Group D) | breadth-first slot 1
- Status: **terminated / honest near-exhaustion** (r1 structural; no viable orthogonal angle)
- Score: r1 **44/100**, verdict terminate, 1 critical (structural, FM2 regio-monotonic)

## Summary
R1 terminated A01(75)/A02(76)/A03(68) on one structural fact: **aqueous quantitative selectivity among chlorophenol
regio-isomers (2,6- vs 2,4-/2,5-) is single-parameter-monotonic** (pKa/logKow), selectivity-factor prior <2 (FM2). The one
non-monotonic geometric axis — halogen-bond sigma-hole pattern (A04, S-grade) — is R1's occupied in-progress best angle and is
itself aqueous-halogen-bond-weak (Phase-0 DFT-gated). All 3 R2 candidates fail pre-screen (X): chaotropic/anion-pi (regio-
degenerate hydration; anion-pi favors sulfate), reactive dehalogenation (class-wide not 2,6-selective; ng/L kinetics),
flanked-OH recognition (collapses into A01's occupied regio-steric axis).

## Designer/Attacker/Reviewer r1 (condensed)
- Designer attempted flanked-OH (2,6-diortho-Cl) recognition; self-flagged it collapses into regio-steric (A01, terminated).
- Attacker C1 (critical, structural): regio-isomer discrimination is FM2 monotonic; no orthogonal 2nd dim exists that isn't
  A01 (regio-steric) or A04 (halogen-bond, R1-occupied + weak). Not rebuildable.
- Reviewer: C1 upheld structural. Score 44. Terminate (no rebuild).

## Residual value (negative knowledge)
- **DCP26 regio-monotonic wall**: chlorophenol regio-isomer aqueous selectivity is intrinsically single-parameter (pKa/logKow);
  the only non-monotonic axis is halogen-bond sigma-hole pattern geometry (A04, R1-occupied, DFT-gated, aqueous-weak). R2 adds
  nothing orthogonal. DCP26 is a genuine honest-exhaustion pollutant in R2 (as it was near-exhausted in R1: 3/3 terminated).
- Transferable: for positional-isomer discrimination of small halophenols in water, geometric sigma-hole pattern is the ONLY
  escape from the pKa/logKow monotonic trap, and it is aqueous-halogen-bond-limited.
- Next: ROX.
