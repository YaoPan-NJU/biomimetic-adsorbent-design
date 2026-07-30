# fresh_1000 R3 — Tier-2 + Tier-3 Depth Audit (2026-07-30)

Depth adjudication of the remaining 15 pollutants (Tier 2: already-passed but heavily R1-terminated; Tier 3: unpassed, R2 revises).
Judged against the hard constraints using in-repo R1/R2 evidence; honest-N recorded, no padding. Completes the 20-pollutant depth map
(Tier 1 in TIER1_DEPTH_AUDIT.md).

## Tier 2 — already-passed, heavily R1-terminated (expect honest-N = 1)

### NP
- Formal pass: A01 ipso alpha-quaternary topology (92, strong). R1 A04/A06/A08/A10 ALL terminated; R1 explicitly declared
  "NP 2nd-pass honest-exhaustion" (equilibrium-binding space exhausted + reactive T8 locked). R2_S06 amphiphilic terminate.
- **Honest-N(NP) = 1 formal. Near-exhaustion (R1-declared). No 2nd in-repo pass.**

### Dieldrin
- Formal pass: A01 exo-epoxide dual-NH squaramide (89). R1 A02/A03 terminated (FM3 Koc ~5e6 impossibility). R2_S12 FM3 terminate.
- **Honest-N(Dieldrin) = 1 formal. Near-exhaustion (FM3 Koc caps all non-A01 angles).**

### Endosulfan
- Formal pass: A01 mineral Lewis-acid hydrolysis (85, Phase-0 GO). R2_S13 terminate (reactive handle spent; residual FM2/class-wide).
- **Honest-N(Endosulfan) = 1 formal. Near-exhaustion.**

### PFBS
- Formal pass: A17 pore-mouth dual-site headgroup-contrast (85). R1 A05/A01/A04 terminated. R2_S02 chaotropic x C4 ~72 revise (ITC gate; C4 affinity marginal + reverse size-window vs PFOS).
- **Honest-N(PFBS) = 1 formal + 1 gate-bound revise (chaotropic ~72, marginal). No 2nd in-repo pass.**

### BDE-209
- Formal pass: A07 (85, r5). R1 A03 sigma-hole halogen-bond-array TERMINATED (aqueous XB weak + DBDPE Br-pattern-degeneracy). R2_S20 terminate.
- **Honest-N(BDE-209) = 1 formal. Near-exhaustion.**

**Tier 2 conclusion: all 5 = 1 formal pass + near-exhaustion (PFBS has 1 marginal gate-revise). No 2nd in-repo formal pass. Confirms Tier-1 pattern.**

## Tier 3 — unpassed (R2 revises + R1 self-eval claims)

The in-repo path to formal passes here is NOT new design (angle space exhausted in R2) but **formal adjudication of R1 self-eval
>=85 claims**. Caveat (honest): self-eval claims can COLLAPSE under formal adversarial review — e.g. DDE self-eval 86 -> 75 revise
(structurally fragile). So self-eval-pending is an in-repo opportunity with genuine two-way risk, NOT a guaranteed pass.

| Pollutant | R1 formal | R1 self-eval claim | R2 carry-in | Honest classification |
|---|---|---|---|---|
| **PFHxS** | 0 | none (both R1 angles terminated) | R2_S03 chaotropic x OAT4 C6 **~84 pass_pending_gate (ITC)** | 0 formal + 1 pass_pending_gate (CLOSEST to a pass; ITC-GO -> ~86-88) |
| **PCP** | 0 | **85-87 (A04 beta-CD snug-fit; S31_A04 scheme exists)** | R2_S17 chaotropic ~78 revise | 0 formal + 1 self_eval_pending (A04, most solid self-eval; formal adjudication = priority in-repo pass candidate) |
| **betaHCH** | 0 | 85-88 (shape-imprint/cage; NOT backed by an executed main-STATUS slot) | R2_S14 terminate | 0 formal + 1 self_eval_pending (weaker: not slot-backed; adjudication risk high) |
| **TCDD** | 0 | none | R2_S15 AhR class-capture ~78 revise | 0 formal + 1 revise |
| **DDE** | 0 | 86 but FRAGILE -> 75 revise under review | R2_S11 terminate | 0 formal; self-eval already collapsed to revise (near-exhaustion) |
| **GenX** | 0 | "85?" dubious (R1 A01=36/A03=61 both terminated) | R2_S04 terminate | 0 formal; self-eval not credible; near-exhaustion |
| **DCP26** | 0 | none | R2_S07 terminate | 0 formal; near-exhaustion (regio-monotonic) |
| **PCB209** | 0 | none | R2_S16 terminate | 0 formal; near-exhaustion (4 axes R1-occupied) |
| **HCBD** | 0 | none | R2_S18 terminate + SL05/SL12 revise | 0 formal + gate-bound revises; near-exhaustion |
| **Chloroform** | 0 | none | R2_S19 terminate | 0 formal; near-exhaustion (too-small-no-handle) |

**Tier 3 conclusion:** the only in-repo formal-pass opportunities are **formal adjudication of PCP A04 (85-87 self-eval, solid)**
and possibly betaHCH (85-88 self-eval, weaker/unbacked). PFHxS is the closest overall but ITC-gated (pass_pending_gate). All other
Tier-3 pollutants are near-exhaustion or external-gate/intrinsic-cap revises.

## Consolidated honest picture (all 20 pollutants)
- **Formal passes (confirmed): 9** (R1: PFOA/BPA/PFBS/NP/Dieldrin/ROX/Octocrylene/Endosulfan/BDE-209, 1 each).
- **In-repo formal-pass candidates (adjudication-pending, two-way risk): PCP A04 (85-87), betaHCH (85-88, weaker).**
- **pass_pending_gate (design-complete, external-gate-blocked): 3** — PFHxS chaotropic~84 (ITC), Octocrylene A04 Michael~80 (DFT), BPA PXR~82 (ITC).
- **revise (intrinsic-cap or gate): BPA ERRgamma~79, PFOA anion-pi~74, ROX cation-pi~81, DDT halogen-bond~79 + corrinoid~78, TCDD AhR~78, PCP chaotropic~78, PFBS chaotropic~72.**
- **Realistic honest total toward the 200 target: ~9 formal + up to ~2 self-eval-adjudication conversions (PCP, maybe betaHCH) + up to ~3 external-gate-GO conversions.** Best case ~11-14 formal; the 200 (10x20) target is NOT honestly attainable — most pollutants are angle-space-exhausted at N=1.

## Next depth actions (highest-value, in-repo)
1. Formally adjudicate **PCP A04** (85-87 self-eval, S31_A04) -> if it holds >=85 under adversarial review, PCP gets its 1st formal pass (10th program pass).
2. (Lower priority / higher risk) betaHCH shape-imprint self-eval adjudication.
3. Then R3_CLOSEOUT.md with the full honest completion assessment + external-gate register + precise path to any further passes.
