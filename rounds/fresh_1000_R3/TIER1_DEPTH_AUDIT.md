# fresh_1000 R3 — Tier-1 Depth Audit (2026-07-30)

Depth adjudication of the 5 easy-first Tier-1 pollutants (already-passed, richest R1 angle space) for ADDITIONAL formal passes
toward the contract's 10/pollutant. Each candidate is judged against the hard constraints (>=85, 0 unresolved critical/high,
distinct axis) using the R1/R2 evidence already in-repo. Honest-N recorded; no padding. See SPEC.md sect. 3 for external-gate policy.

## Method
For each pollutant: (1) list the R1 formal pass (axis taken), (2) inventory every other R1-mapped/executed angle + R2 revise,
(3) classify the best remaining candidate as formal-pass / pass_pending_gate / revise / near-exhaustion. A candidate already
adjudicated in R1/R2 is not re-run (respect prior verdicts); only genuinely new candidates get fresh design-attack-review.

## Per-pollutant findings

### BPA (done in R3_BPA_S01)
- Formal pass: A01 DmpR anchor+bridge-gate (86).
- 2nd-best: **ERRgamma pocket (R3, revise ~79, 0c/2h)** — material pocket-precision + affinity ITC gate. PXR avidity (R2 ~82) = pass_pending_gate (ITC).
- R1 terminated A02/A03/A04/A07 (aqueous phenol H-bond near-thermoneutral / logKow-T1 / no precedent).
- **Honest-N(BPA) = 1 formal + 2 near-pass (ERRgamma revise, PXR pass_pending_gate). 10 NOT attainable in-repo.**

### PFOA
- Formal pass: A02 urea oxyanion-hole POP (85).
- Inventory: A01/A03-A10 terminated; A11-A26 ENUMERATED but unexecuted (low grade — incl. A13/A14 fluorophilic/fluorous-core,
  which are the "perfluoro-tail recognition" angle: mapped, graded low, not novel for R3). R2_S01 anion-pi ~74 revise (Phase-0 DFT
  gate; anion-pi also favors sulfate = liability).
- Best remaining: anion-pi (R2 revise ~74, Phase-0 DFT gate) — NOT a formal pass; fluorophilic tail is R1-mapped-low (aqueous
  fluorous interaction too weak at ng/L vs sulfate background). No new in-repo 2nd pass.
- **Honest-N(PFOA) = 1 formal (A02) + 1 gate-bound revise (anion-pi). PFAS head-group recognition intrinsic hardness (R1-documented). 10 NOT attainable.**

### Octocrylene
- Formal pass: A01 CT donor-acceptor cavity (85).
- Inventory: A02 cyano-dipole terminated (55, dehydration self-falsifying + selectivity reversal). **A04 Michael covalent capture:
  R1 r2=80 revise_with_phase0_prerequisite, DESIGN-COMPLETE, only residual = external DFT gate (delG-dagger<=55 -> GO; pass prob
  ~25-35%).** R2_S09 near-exhaustion (electronic axis occupied).
- Best remaining: **A04 Michael = pass_pending_gate ~80-83** (design layer closed; the ONLY blocker is the external DFT barrier
  calculation). This is a genuine near-pass, promoted to pass_pending_gate.
- **Honest-N(OC) = 1 formal (A01) + 1 pass_pending_gate (A04 Michael, DFT). If DFT-GO -> 2 formal.**

### ROX
- Formal pass: A01 23S-rRNA NPET nucleobase-cleft cage (85).
- Inventory: A02 oxime-ether terminated (73, alpha~0.40 NEGATIVE-selectivity mode + mechanism-homologous to A01, ceiling 78-80).
  A06 macrolide-esterase terminated (49, catalytic gap 7-10 OOM + no intra-class selectivity). R2_S08 cation-pi aromatic-cage
  class-capture ~81 revise (cation-pi moderate to tertiary amine + CD-inclusion prior art).
- Best remaining: cation-pi (R2 revise ~81) — class-capture, ceiling 82-83, not a formal pass. No new in-repo 2nd pass.
- **Honest-N(ROX) = 1 formal (A01) + 1 revise (cation-pi class-capture). R1 portfolio_100 explored 20 angles, max 78 (none >=85 besides A01). 10 NOT attainable.**

### DDT
- Formal pass: A01 dehydrochlorinase beta-elimination dual-motif (86).
- Inventory: A02 corrinoid reductive capture revise_with_low_ceiling (~78; ng/L kinetics + DDE SET shadow + precedent density,
  ceiling 78-80). R2_S10 halogen-bond para-Cl pattern ~79 revise (Phase-0 DFT gate; aqueous aromatic C-Cl weak).
- Best remaining: halogen-bond pattern (R2 revise ~79, DFT gate) — not a formal pass; corrinoid is low-ceiling. No new in-repo 2nd pass.
- **Honest-N(DDT) = 1 formal (A01) + 2 revise (corrinoid low-ceiling, halogen-bond DFT-gate). 10 NOT attainable.**

## Cross-pollutant honest conclusion (Tier 1 — the richest, easy-first pollutants)
Across ALL 5 Tier-1 pollutants, **NO 2nd FORMAL pass is attainable in-repo.** Each has exactly 1 formal pass (R1) plus 1-2
near-passes that are either external-gate-bound (Octocrylene A04 DFT, BPA PXR ITC, PFOA anion-pi DFT, DDT halogen-bond DFT) or
intrinsic-cap revises (ROX cation-pi class-capture, BPA ERRgamma, DDT corrinoid low-ceiling). The remaining R1-mapped angles were
graded low and left unexecuted for cause.

**Implication for the contract target:** if the RICHEST pollutants yield honest-N ~= 1 formal + 1-2 gate-bound near-passes, the
10-passes-per-pollutant / 200-total target is NOT honestly attainable in-repo. The realistic honest total is ~9 formal (R1) + a
handful of external-gate-GO conversions (best candidates: PFHxS ITC ~84->pass, Octocrylene A04 DFT). Tier 2/3 (heavily R1-terminated
/ external-gate-bound) will only reinforce this. This is the honest-N reality the contract's clause anticipates ("recorded N<10 beats padding").

## R3 pass_pending_gate register (design-complete, external-gate-blocked near-passes)
1. PFHxS R2_S03 chaotropic x OAT4 C6 ~84 (ITC) — closest to a pass.
2. Octocrylene A04 Michael covalent ~80 (DFT barrier; pass prob 25-35%).
3. BPA R2_S05 PXR avidity ~82 (ITC).
(Plus revises: BPA ERRgamma ~79, PFOA anion-pi ~74, ROX cation-pi ~81, DDT halogen-bond ~79, PCP chaotropic ~78, TCDD AhR ~78, PFBS chaotropic ~72.)

Next: Tier 2 (NP/Dieldrin/Endosulfan/PFBS/BDE209) depth audit — expect honest near-exhaustion (R1 heavily terminated).
