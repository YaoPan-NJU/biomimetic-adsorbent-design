# R2_S14 · beta-HCH R2 — honest near-exhaustion (aliphatic-Cl-weak + shape-occupied wall)

- Program: fresh_1000 R2 | Pollutant: beta-HCH | Tier 2 (Group C) | breadth-first slot 1
- Status: **terminated / honest near-exhaustion** (r1 structural; no viable orthogonal angle)
- Score: r1 **~44/100**, verdict terminate, 1 critical (structural)
- Mechanism map: MECH_betahch_001

## Summary
R1 A01 (gamma-CD inclusion) TERMINATED at 45 — the core assumption was experimentally REFUTED (beta-CD preferentially includes
gamma-HCH, not beta-HCH; FM3). R1 then reached a self-eval pass (85-88) via **shape-imprint MIP / molecular cage** on beta-HCH's
one distinctive handle: the all-equatorial (eeeeee) symmetric rigid chair (unique compact SHAPE vs alpha/gamma/delta, which differ
only in Cl orientation). R2 candidates all fail pre-screen (X): (a) **halogen-bond belt on the 6 equatorial C-Cl** — these are
ALIPHATIC (sp3) C-Cl whose sigma-holes are markedly weaker than the aromatic C-Cl of DDT/TCDD, so the PROTO_R2_006 pattern route
does NOT clear TFG in water; (b) **dipole-null recognition** — beta-HCH's centrosymmetric ~zero dipole is a NEGATIVE property
(you cannot positively bind for LACKING a dipole); (c) **reactive dehydrochlorination** — beta-HCH is the E2-RESISTANT isomer (no
antiperiplanar H-Cl), so LinA-type reactive capture intrinsically fails for beta specifically.

## Designer/Attacker/Reviewer r1 (condensed)
- Designer: proposed the equatorial-Cl halogen-bond belt (transferring the DDT PROTO_R2_006 pattern); self-flagged aliphatic-Cl weakness.
- Attacker C1 (critical, structural): the halogen-bond-pattern route requires AROMATIC C-Cl sigma-holes; beta-HCH's Cl are sp3
  (aliphatic), too weak in water for ng/L. The one distinctive handle (all-equatorial SHAPE) is R1-occupied (shape-imprint/cage);
  dipole-null is non-engineerable; reactive route fails for the E2-resistant isomer. No orthogonal-and-viable angle. Not rebuildable.
- Reviewer: C1 upheld structural. Score ~44. Terminate (no rebuild).

## Residual value (negative knowledge)
- **KEY: aromatic-only halogen-bond-pattern boundary** — the DDT PROTO_R2_006 halogen-bond-PATTERN route transfers ONLY to
  AROMATIC-C-Cl OCP (DDT/TCDD/PCB), NOT to aliphatic-C-Cl OCP (beta-HCH). This sharpens the PROTO_R2_006 applicability domain.
- beta-HCH is the hardest-to-remove HCH isomer; its selectivity budget (symmetric shape) was spent in R1. Honest near-exhaustion.
- Next: TCDD.
