# R3_BPA_S01 · BPA depth slot — ERRgamma-templated high-affinity phenol-anchor + pocket (bisphenol-class capture) — revise

- Program: fresh_1000 R3 (DEPTH) | Pollutant: BPA | Tier 1 | depth slot toward 2nd formal pass (beyond A01 DmpR=86)
- Status: **revise** (0 critical / 2 high) — NOT a formal pass; strong prototype but material-precision + affinity gate cap it
- Score: r1 **~79/100** (0c/2h), ceiling ~80-82
- Prototype: **PROTO_R3_001** ERRgamma (estrogen-related receptor gamma) ligand-binding domain | Mechanism map: MECH_R3_bpa_002
- Orthogonality vs A01 (DmpR bacterial-sensor anchor + bridge-region SPATIAL GATE): ERRgamma uses a nuclear-receptor **high-affinity single-phenol anchor + POCKET-VOLUME complementarity** (distinct mechanism + distinct prototype). Distinct from terminated A04 (ERbeta volume-THRESHOLD, no precedent) because ERRgamma has a solved ERRgamma-BPA crystal structure and optimal-fit (not threshold) binding.

## Supervisor summary
BPA's one formal pass (A01, DmpR anchor+bridge-gate, 86 after 5 rounds) took the bacterial-sensor spatial-gate axis. R1 terminated
A02/A03/A04/A07 (aqueous phenol H-bond near-thermoneutral; geometric-ruler signatures covered by logKow T1; ERbeta volume-threshold
thermodynamically invalid + no precedent). The best remaining orthogonal angle is **ERRgamma**: BPA is ERRgamma's highest-affinity
known environmental ligand (Kd ~nM), with a solved ERRgamma-LBD-BPA crystal structure (Matsushima 2007) — a real evolved, aqueous,
high-affinity BPA recognition. Translated: an ERRgamma-mimetic pocket = one H-bond donor for a phenol OH + a hydrophobic aromatic
pocket shaped to the C(CH3)2 bridge. Because ERRgamma also binds BPF/BPS/other bisphenols, this delivers **bisphenol-class capture**
(mirrors AhR dioxin-class / ROX macrolide-class). Lands **revise** (not pass): material pocket-volume precision (A04 lesson recurs,
though ERRgamma has the precedent A04 lacked) + absolute nM->ng/L affinity is calorimetry-gated.

## Scientific question
Can an ERRgamma-templated pocket (single-phenol H-bond anchor + hydrophobic pocket sized to the C(CH3)2 bridge) capture BPA from
water with high affinity and bisphenol-class selectivity over co-occurring phenols — an orthogonal recognition mechanism to A01's
DmpR bridge-spatial-gate?

## Biological prototype evidence (H1)
| prototype | biological recognition | evidence tier | translation |
|---|---|---|---|
| ERRgamma LBD (Matsushima 2007 crystal; Okada 2008 binding) | BPA bound with ~nM affinity via phenol-OH H-bond + hydrophobic pocket accommodating the dimethyl bridge; BPA-preferring among bisphenols | fact (structural + binding) | H-bond-donor + hydrophobic aromatic pocket (MIP/COF) sized to the C(CH3)2 bridge |

- H1 (hard correspondence): biological high-affinity phenol-anchor + pocket-fit (ERRgamma) -> synthetic anchor+pocket host. Genuine mechanism-level correspondence.
- ERRgamma is a stronger anchor than A04's ERbeta (higher affinity + a solved BPA co-crystal precedent); orthogonal to A01's spatial-gate mechanism.

## Material architecture
- ERRgamma-mimetic host: a rigid pocket presenting ONE pre-organized H-bond donor (for a phenol OH) + a hydrophobic aromatic
  sub-pocket dimensioned to the C(CH3)2 bridge (MIP imprinted with BPA, or a designed COF cavity). Bridge-volume complementarity
  provides intra-bisphenol bias (BPA C(CH3)2 > BPF CH2 > BPS SO2 by pocket fit); phenol anchor + hydrophobic desolvation give affinity.

## Selectivity verdict + external gate
- **2 high:** (1) material pocket-volume PRECISION for intra-bisphenol discrimination (A04 lesson — COF/MIP cavity tolerance vs the
  subtle bridge difference; downgraded from A04's critical because ERRgamma provides a real binding-mode precedent); (2) absolute
  nM->ng/L aqueous affinity is calorimetry(ITC)-gated (external).
- No critical (ERRgamma-BPA binding is real, aqueous, high-affinity, crystallographically defined).
- Honestly scoped as bisphenol-CLASS capture (intra-BPA vs BPF/BPS is a bias, not a hard claim).

## Innovation checklist
- Novel biomimetic mapping (ERRgamma high-affinity pocket -> BPA-class host): **pass** (first ERRgamma-templated adsorbent here)
- Not trivial logKow/hydrophobic: **pass** (specific pocket + phenol anchor, evolved high-affinity template)
- >=1 hard correspondence (H1): **pass**
- Prior-art delta: **borderline** (bisphenol MIPs exist; the ERRgamma-crystal-templated pocket + class-capture framing is the delta)

## Scoring (six-dimension, /100)
- Causal closed loop 20 -> 17 | Selective adsorption mechanism 25 -> 18 | Translatability 20 -> 15 | Originality 15 -> 11 |
  Falsifiable controls 10 -> 9 | Evidence completeness 10 -> 9 | **Total ~79/100** — revise (0c/2h)

## Residual value & honest-N note
- **BPA honest-N so far: 1 formal pass (A01) + this ERRgamma revise (~79, 2nd-best angle).** R1 terminated 4 other angles; the
  aqueous-phenol-recognition space is intrinsically hard (H-bond near-thermoneutral). Reaching the contract's 10 passes for BPA is
  NOT honestly attainable in-repo — the tractable angles are A01 (passed), ERRgamma (revise, this), PXR avidity (R2 ~82 pass_pending_gate).
  Honest-N for BPA is likely ~1 formal + 2 near-pass (gate-bound). Recorded, not padded.
- **New prototype PROTO_R3_001 (ERRgamma)** added (library 90 -> 91) — transferable to other xenoestrogen phenolics (NP, alkylphenols).
- Next: PFOA depth audit (26 R1 angles) or ROX/DDT; continue easy-first.
