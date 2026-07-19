# PFBS-CD-OG1: 短链 PFAS 选择性吸附活性炭复合材料

**设计日期**: 2026-07-18  
**设计方法**: 多智能体对抗研讨（4 设计师 + 4 攻击者 + 综合 + 最终设计）  
**目标污染物**: PFBS（C4 全氟磺酸），GenX（次要筛选）

---

# Executive Summary

PFBS-CD-OG1 is a granular composite adsorbent for the removal of the short-chain perfluoroalkyl sulfonate PFBS from secondary effluent, where granular activated carbon (GAC) fails by early breakthrough and cationic sorbents fail by sulfate interference. The material carries a covalent, orientation-controlled monolayer of mono-6-amino-6-deoxy-beta-cyclodextrin on bituminous GAC: each cyclodextrin is tethered through its narrow primary face by a single amide bond, presenting the wide secondary face to solution as a preorganized, neutral 人工识别单元 (artificial recognition unit).

Two biological sources define the design. Beta-cyclodextrin supplies the verified structural module, an apolar 6.0 to 6.5 angstrom cavity that includes perfluoroalkyl tails with a measured PFBS affinity near 2.5 x 10^3 M^-1. The GPR43 short-chain receptor supplies the 设计原理 (design principle) of a depth-limited pocket whose polar rim flattens the chain-length affinity ladder. The composite translates this pair into a layer whose incremental affinity is short-chain enriched relative to the carbon carrier, with no cationic group, no fluorinated component, and no metal.

Success is defined by four 硬对应 (hard correspondence) gates, ending in a column-level survival test: apparent Kd at or above 10^4 L/kg at 1 ug/L in 1 mM sulfate, at least threefold GAC bed life, and solvent regeneration over five cycles. Estimated pilot cost is 15 to 45 USD/kg, far below the 5 yuan/g ceiling. The decisive unknown, a roughly 10^4-fold effective affinity enhancement at ng/L, is tested first and cheaply.

---

# Engineering Problem

## Primary target

PFBS (perfluorobutanesulfonate, C4 perfluorosulfonate), a contract-admitted pollutant of verified secondary-effluent relevance. GenX/HFPO-DA is retained only as a gated secondary screen with its own pass bar, consistent with its superseded-pollutant status in the project contract; it is reported separately and never used to support the primary claim.

## Why short-chain PFAS are the leading unsolved challenge

Three ledger-anchored facts define the gap.

1. **Hydrophobic partitioning fails.** The C4 perfluoro tail is too short to drive partitioning into carbon micropores. GAC breaks through for PFBS at roughly 5,000 to 20,000 bed volumes, versus 100,000 to 300,000 or more for PFOA and PFOS (literature consensus consistent with ledger E028). The incumbent technology is therefore weakest exactly where regulation is moving.

2. **Electrostatic capture is repelled or nonselective.** The sulfonate head is fully ionized at all relevant pH values. Oxidized carbon surfaces carry negative charge and repel it; cationic sorbents capture it but cannot distinguish it from the far more abundant sulfate, bicarbonate, and chloride in real effluent.

3. **The cationic route is disqualified by the repository's own frozen counterexample.** A cationic beta-cyclodextrin polymer lost PFBS removal from about 94% to about 38% in 1 mM Na2SO4, while PFOS retention held near 79% (E056, ACS Cent. Sci. 2022; exact percentages pending full-text recheck). Ledger E058 and E059 plus the PFBS-2 attack establish that guanidinium motifs drift toward sulfate rather than PFBS. Charge-based short-chain capture is a closed avenue inside this project.

## Current state of the art and the residual gap

The earlier framing that no short-chain sorbent exists is outdated and is corrected here. Four recent platforms now occupy parts of the space, and each must be ledgered with an explicit what-it-fails-to-deliver note:

- Guanidinium anion-exchange polymer (ES&T 2023): charge-based; inherits the sulfate fragility documented above.
- Short-chain-preferring cyclodextrin polymer (JACS 2024): selective, but a specialty polymer, not a drop-in granular medium in GAC format.
- Guanidinium-beta-CD polymer retaining PFBS in 100-fold sulfate (ES&T 2024): combines a cationic motif with CD; cost, regeneration chemistry, and long-term matrix behavior at ng/L remain open.
- Fluorinated porous aromatic framework with column-level PFBS-over-PFOS preference (Nature Water 2025): carries the fluorinated-material lifecycle burden and is not a granular drop-in.

The defensible residual gap: no low-cost, drop-in, GAC-format granular medium demonstrates a verified short-chain Kd increment in real secondary effluent, with solvent regeneration and without a fluorinated-material lifecycle burden.

## Quantitative objective, stated correctly

At environmental concentrations of 50 to 500 ng/L PFBS, the monomer affinity Ka of about 2.5 x 10^3 M^-1 is arithmetically insufficient: at 1 ug/L the fraction of monomer cavities occupied would be far below what a treatment bed requires. The treatment objective therefore demands an apparent composite Kd of at least 10^4 L/kg at 1 ug/L in 1 mM Na2SO4, corresponding to an effective affinity enhancement of roughly 10^4 over the soluble monomer. Every verification threshold in this design is set against that number. Any cost scenario that depends on this Kd is labeled a target to be tested, not an estimate.

## Why solving it matters

PFBS is mobile, persistent, and increasingly regulated as long-chain PFAS are phased out and replacement chemistries shift toward shorter chains. A medium that upgrades the world's installed GAC base with a short-chain recognition layer, regenerable in solvent rather than by thermal reactivation, addresses the capability gap at the exact format in which treatment infrastructure already exists.

---

# Biological Prototype

The design uses two prototypes with a deliberate division of labor: one supplies a structural module with hard, verified chemistry; the other supplies a functional selectivity principle verified at the pharmacology level. Neither is asked to carry the other's evidential load. All claims below require evidence-ledger entry before use in any external document.

## Prototype 1 (structural module): beta-cyclodextrin

**Identity and origin.** Beta-cyclodextrin (beta-CD) is the cyclic heptasaccharide produced in nature and industrially (more than 10,000 t/yr) by cyclodextrin glucanotransferase (CGTase, EC 2.4.1.19) acting on starch. It is a defined single molecule, not a statistical polymer, which is what makes it a preorganizable recognition unit.

**Structural evidence.** The truncated-cone geometry is established by X-ray crystallography of crystalline cyclodextrin hydrates and of numerous inclusion complexes, and is treated here as verified: internal cavity diameter 6.0 to 6.5 angstrom, cavity height 7.9 angstrom. The interior lining (H3, H5, and the glycosidic O4 atoms) is apolar and polarizable; the wide rim carries the secondary 2-OH/3-OH belt; the narrow rim carries the primary 6-OH belt. No protein structure is invoked for this module, and no PDB entry is needed to support geometry that small-molecule crystallography establishes directly. (The ledger records the crystallographic sources; this document does not cite PDB identifiers it has not inspected.)

**Binding evidence, with a mandatory correction.** The PFBS affinity benchmark is the isothermal titration calorimetry consensus of three studies: Xiao et al. 2019 (ES&T Lett), Wang et al. 2020 (ES:Nano), Gao et al. 2021 (JPCB), giving Ka approximately 2.2 to 2.8 x 10^3 M^-1 for PFBS and approximately 1.5 x 10^3 M^-1 for GenX (method-dependent range up to 6.5 x 10^3; the branched-ether steric fit of GenX is flagged as an open question). Weiss-Errico and O'Shea 2017 (JPCB 121:8359) is a gamma-CD study and must be relabeled in the ledger; its 19F/ROESY data support the cavity-matching control (the beta better than gamma ordering), not the beta-CD benchmark. Affinity rises with perfluoro chain length (PFOA roughly 10^4 to 10^5 M^-1), so beta-CD supplies geometry-selective, non-electrostatic recognition of fluorinated tails, not an intrinsic short-chain preference. The reported orientation is wide-face tail entry with the anionic headgroup hydrated at the rim; provenance of this orientation for beta-CD specifically must be re-verified, failing which the orientation correspondence (HC3) is downgraded to hypothesis.

## Prototype 2 (functional principle, not structure): the GPR43 (FFAR2) chain-length gate

**System.** GPR43 is a G-protein-coupled receptor for short-chain carboxylates. The mutagenesis-verified polar core (Arg180, Arg255, His242; Stoddart et al., J. Biol. Chem. 2008, 283(47):32913-32924, citation corrected from the design-1 misprint; Le Poul et al., JBC 2003; Brown et al., JBC 2003) defines a shallow polar pocket.

**Verified pharmacology.** C2 to C5 carboxylates are active; C6 and longer are inactive; C1 (formate) is inactive. Activity, not binding free energy, is the measured quantity, and this document states the evidence at exactly that level.

**Structural evidence status.** No experimental three-dimensional structure of GPR43 is used. The pocket-depth argument rests on mutagenesis and structure-activity data, labeled FACT at the pharmacology level and INFERENCE at the geometry level. This honesty matters: only the gate principle is transferred, and no residue, guanidinium group, or protein geometry is copied into the material.

## Why this pair is appropriate

The engineering problem is not the absence of PFAS binders but the absence of non-electrostatic, short-chain-tolerant recognition in a granular format. Beta-CD is the rare case of a binder whose chemistry is neutral, water-compatible, industrially cheap, and crystallographically defined. GPR43 is the clearest biological demonstration that a depth-limited pocket with a polar mouth can flatten a chain-length response curve, which is precisely the selectivity behavior the material layer must reproduce. Prototype 1 supplies the cavity; prototype 2 supplies the 设计原理 (design principle) that tells the cavity what selectivity profile to express.

---

# Design Principle

Five principles are extracted from the two prototypes. Each is stated with its biological source, its material translation, and its evidence label.

## P1. Neutral cavity inclusion instead of electrostatic capture (from prototype 1; FACT)

An apolar, polarizable cavity of matched cross-section binds perfluoroalkyl tails by dispersion and cavity-solvation effects, with no dependence on charge. Because the interaction is non-electrostatic, it carries none of the sulfate fragility that disqualified the cationic platforms (E056, E058, E059). The sulfonate head remains hydrated outside the cavity; it is tolerated, not targeted.

## P2. The depth-limit gate: a bounded apolar zone flattens the chain-length ladder (from prototype 2; principle verified at pharmacology level, material effect INFERENCE)

GPR43 achieves short-chain selectivity because its pocket is shallow: once a tail exceeds the pocket depth, additional carbons gain no further burial, so binding energy stops growing with chain length, while the polar anchor at the mouth does most of the work for the shortest ligands. The beta-CD cavity (7.9 angstrom deep) is a physical implementation of the same gate. A C4 tail is fully accommodated; longer tails gain progressively less incremental burial per CF2 beyond the cavity. Consequence: on a surface-tethered cavity layer, the chain-length affinity ladder should be flatter than the ladder of the carbon carrier, and the layer's incremental Kd should be short-chain enriched relative to blank GAC. This design claims the flattening on the layer only; it makes no claim of composite-level alpha(PFBS/PFOS) greater than 1, because that metric is confounded by carrier partitioning and is demoted to a stretch target.

## P3. A neutral polar rim as the headgroup contact zone (from both prototypes; FACT for CD chemistry, INFERENCE for its contribution to selectivity)

GPR43's pocket mouth is polar and does the anchoring work for short ligands. The wide rim of beta-CD presents a belt of secondary hydroxyls that contacts the hydrated sulfonate head without any cationic charge. The material therefore places a polar but neutral rim at the solution interface, and caps all residual surface carboxyls so the layer as a whole is neutral and does not repel anionic guests (lesson imported from the design-2 surface-charge attack).

## P4. Orientation control to maximize correctly presented recognition units (from prototype 1 geometry; magnitude UNVERIFIED)

Statistical grafting presents cavities in mixed orientations; a fraction face the wrong way or lie flat and are inaccessible. Tethering every CD through a single defined point (the primary face) presents the wide entry face to solution, maximizing accessible, correctly oriented cavities per grafted molecule. This is the design's residual novelty axis and is tested causally (HC3) rather than assumed.

## P5. Division of labor between layer and carrier (engineering principle; FACT for carrier behavior)

The GAC core retains its native function: micropores partition long-chain PFAS and a fraction of natural organic matter. The CD layer adds the short-chain increment the carrier lacks. The composite is read as carrier plus layer, with the blank-GAC contribution always subtracted and reported.

## Why conventional synthesis cannot reach this behavior

Electrostatic sorbents are disqualified by sulfate mass action at environmental concentrations. Conventional CD-functionalized carbons use epichlorohydrin or statistical coupling, which destroys orientation, collapses porosity (the Dichtel group's crosslinker comparison documents the collapsed non-porous gel), and leaves charged residues. Fluorinated sorbents achieve short-chain affinity but import the lifecycle burden this project excludes. The combination of preorganized single-molecule recognition, defined orientation, carrier-neutrality, and granular format is not accessible by any of these conventional routes; it requires the oriented-monolayer construction specified here.

---

# Material Design

**Working name:** PFBS-CD-OG1 (oriented-gate cyclodextrin on granular activated carbon).

## Architecture

A core-shell granular composite. The core is bituminous-coal GAC, 12 x 40 mesh, BET 900 to 1100 m2/g, with mixed micro- and mesoporosity, serving as mechanical scaffold and as the partition baseline for long-chain PFAS and natural organic matter. On the oxidized outer surface, a covalent monolayer of mono-6-amino-6-deoxy-beta-CD is tethered exclusively through the narrow primary face by a single amide bond to surface carboxyls, at 5 to 15 wt% CD (approximately 0.04 to 0.13 mmol cavity per gram of composite), presenting the wide secondary face to solution. Residual unconsumed surface carboxyls are capped with ethanolamine so the net layer is neutral and does not repel anionic guests. Micropore volume is preserved as the native long-chain sink: the BET retention gate is at least 80% of parent GAC, with NLDFT pore-size-distribution mapping before and after grafting to locate where CD actually lands, because pore-locus control by grafting cannot be enforced a priori.

## The recognition unit (人工识别单元)

Each tethered beta-CD molecule is a preorganized artificial recognition unit with three functional zones in fixed spatial arrangement:

- **Apolar cavity (6.0 to 6.5 angstrom diameter, 7.9 angstrom deep):** sole capture site; neutral, geometry-selective inclusion of the perfluoroalkyl tail.
- **Secondary-OH belt at the wide rim:** neutral polar contact zone for the hydrated sulfonate head; the functional analog of GPR43's polar pocket mouth, without charge.
- **Single primary-face amide tether:** orientation lock; guarantees wide-face presentation and prevents face-down or buried cavities.

## Recognition logic, element by element

1. Cavity inclusion is the only capture mechanism claimed: neutral, non-electrostatic, carrying no sulfate fragility of the kind that killed designs 1 and 4.
2. The secondary-OH rim contacts the hydrated headgroup; the surface as a whole is neutral after ethanolamine capping.
3. The 7.9 angstrom depth implements the chain-length gate of P2: the layer's per-cavity chain-length ladder is predicted to be flatter than the carrier's, so the layer increment is short-chain enriched. No composite-level selectivity inversion is claimed.
4. Orientation maximizes the number of usable cavities per grafted CD, which is the cheapest route to the local cavity density that the ng/L Kd target requires.

## Deliberate omissions, each tied to an attack

- No guanidinium or any cationic group (sulfate trap; E056, E058, E059).
- No pentafluorophenyl or any fluorinated component (PFBS-18 cull; self-neutralizing stacking on graphene; lifecycle burden; the motif had no basis in the biological prototype in any case).
- No zinc or any metal (bicarbonate/VFA mass action; N,O-chelation stoichiometry trap; leaching).
- No polydopamine, chitosan, or alginate (direct prior art for GenX on GAC; chitosan is only about 20 to 25% protonated at pH 7; Ca-alginate disintegrates in sulfate).
- No epichlorohydrin (IARC 2A carcinogen; collapsed non-porous gel per the Dichtel group's crosslinker comparison).

## Optional high-affinity arm (decision branch, not default)

If the oriented monolayer fails the Kd gate in G1 batch testing, a rigid, fluorine-free network skin is grown by interfacial crosslinking of the tethered CD layer with terephthaloyl chloride (rigid aromatic ester links). The arm imports one lesson from the TFN networks, namely that rigidity rather than crosslinking per se produces affinity enhancement, but it is a fluorine-free structural analog, is gated on a freedom-to-operate opinion, and is never cited using TFN performance data; its performance must be measured on its own coupons.

## Status labeling

- **Known:** beta-CD host-guest chemistry and its ITC benchmark; GAC short-chain deficiency; cationic-platform salt collapse.
- **Inferred:** orientation benefit magnitude; depth-gate flattening on a surface-tethered cavity; local-cavity-density avidity at ng/L.
- **Unverified:** apparent Kd at ng/L in real effluent; DOM competition magnitude; regeneration cycle life.

## Why this material will work, and the honest size of the bet

The mechanism requires only chemistry that is individually verified: inclusion, neutral rims, amide tethers, carbon partitioning. The single large uncertainty is quantitative: whether oriented, densely grafted neutral cavities on a rigid non-swelling carrier can deliver the roughly 10^4-fold effective enhancement over monomer Ka that the treatment objective needs. That enhancement is inferred from network-effect precedents, not demonstrated for this architecture, and it is exactly what gates G0 to G2 are built to falsify cheaply before serious money is spent.

---

# Synthesis Route

Ordering principle (imported from the design-4 attack): the cheapest decisive kill experiments run first; no full build before the survival question of the recognition chemistry is tested.

## GATE G0: soluble-phase verification (before any carbon work; weeks 1 to 6; milligram scale)

Measure Ka(PFBS) and Ka(GenX) for mono-6-amino-beta-CD and for its amide-capped form (acetamide capping of the 6-amino group, modeling the tethered state) by ITC and 19F NMR, in nanopure water, in 1 mM Na2SO4, and with equimolar PFOA competitor.

- Kill criteria: the tethering-model rim chemistry must not depress Ka below the 2.2 to 2.8 x 10^3 M^-1 benchmark, and PFBS occupancy must survive 1 mM sulfate (expected, because the rim is neutral, but measured, not assumed).
- Failure at G0 terminates the design for the cost of reagents and weeks, not for the cost of a materials program.

## Main route: oriented monolayer (all steps below 60 C, aqueous buffers)

**Step 1, GAC preparation.** Wash 12 x 40 bituminous GAC in 0.1 M HCl, then 0.01 M NaOH, rinse to neutral, dry at 105 C. Mild oxidation in 2 M HNO3 at 60 C for 3 h. Gates: BET loss below 20%; Boehm carboxyl content 0.5 to 1.0 mmol/g; zeta potential versus pH recorded as QC.

**Step 2, precursor.** Mono-6-amino-6-deoxy-beta-CD, commercial, or prepared in two steps from beta-CD (mono-6-tosylation, then azide formation and reduction, or ammonolysis; standard literature transformations). Identity confirmed by NMR and MS. Bulk beta-CD costs 8 to 15 USD/kg, which is why the precursor, not the sugar, is the reagent-cost item.

**Step 3, oriented coupling.** Activate GAC carboxyls with EDC/NHS in 0.1 M MES pH 5.5 for 30 min, then react with mono-6-NH2-CD in HEPES pH 7.4 for 24 h at room temperature with gentle mixing. The single 6-amino group per CD forces primary-face tethering; amide formation at any other position is chemically excluded. Cap residual activated esters and carboxyls with ethanolamine. Wash until no UV-detectable CD elutes.

**Step 4, grafting-specific QC** (per the design-3 attack: TGA and FTIR cannot distinguish grafted from occluded CD).

- Covalent fraction: post-hydrolysis mass balance or labeled-CD tracer.
- Accessible-cavity count: adamantane-1-carboxylate uptake (the cavity census used by every downstream normalization).
- XPS surface composition; TGA CD wt% (target window 5 to 15%); BET and NLDFT pore mapping; zeta potential at pH 7.
- Leaching: 7-day soak plus thermal and pH-stress leaching tests.

**Step 5, performance QA at the correct concentration.** Batch uptake at 100 to 500 ng/L PFBS by LC-MS/MS, with a Freundlich fit spanning 0.1 to 100 ug/L. Then the frozen four-matrix mixture protocol: PFBS/PFPeS/PFHxS/PFOS mixture in nanopure water, 1 mM Na2SO4, NaCl/NaHCO3 matrix, and real secondary effluent; DOM panel 0 to 10 mg/L TOC with size-fractionated NOM. Report Kd, saturation capacity in mg per g of total composite, and the blank-GAC-subtracted increment.

## Network arm (only if the monolayer fails the Kd gate)

Terephthaloyl chloride interfacial crosslinking of the tethered CD layer (Schotten-Baumann conditions on the suspended carbon), with the same QC battery. Never built before G1 data justify it; never cited with TFN performance numbers; built only after freedom-to-operate clearance.

## Frozen controls (architecture imported from design 1's praised control logic)

- **M0:** blank washed GAC.
- **M-ox:** oxidized-only GAC (isolates the oxidation contribution).
- **C-random:** native beta-CD coupled non-selectively at equal CD loading and equal accessible-cavity count (the orientation causal test).
- **C-silica:** identical oriented CD layer on nonporous silica beads (the non-adsorbing-carrier control; makes the layer's chain gate measurable without carbon partitioning).
- **C-alpha / C-gamma:** mono-6-amino-alpha-CD and gamma-CD analogs at equal molar loading (cavity-matching test; the relabeled Weiss-Errico gamma-CD data predict the ordering).
- **C-load:** 5/10/15 wt% loading series (tests local-density dependence without the moles-constant self-contradiction of design 3's original HC2).

## Regeneration

Methanol or 50% ethanol with 0.1 to 0.5% NaCl, 2 to 4 bed volumes at 40 to 50 C; the protocol class is validated on crosslinked CD polymers (Ling et al. 2020). Solvent recovered by distillation; PFAS concentrate routed to destruction, carried as an explicit OPEX line. Pre-registered gates: at least 5 cycles with less than 10% capacity loss per cycle, with full mass balance. No caustic, no thermal reactivation, no metal reload.

## EHS

No epichlorohydrin, no fluorinated reagents, no metals. Residual terephthalic acid (network arm only) is low-hazard. The drinking-water deployment path budgets NSF/ANSI 61 extraction testing from the outset.

---

# Hard Correspondence Dimensions (硬对应)

Four correspondences are registered. HC1 to HC3 establish mechanism; HC4 is the survival gate whose failure kills the design regardless of the other three.

## HC1. Cavity-geometry recognition (prototype 1, static structure; mechanistically load-bearing)

- **Biological/module feature (verified):** beta-CD binds perfluoroalkyl tails by cavity inclusion, with affinity rising with chain length and a size-matched cross-section.
- **Material implementation:** oriented beta-CD monolayer on GAC.
- **Measurements:** (a) adamantane-1-carboxylate displacement must suppress PFBS uptake by at least 50% at equimolar competitor relative to accessible cavities; (b) the cavity-size series at equal molar loading must give the order beta > gamma > alpha for PFBS (the relabeled Weiss-Errico gamma-CD data support this as a control, not as the benchmark); (c) the apparent composite affinity for PFBS must meet or exceed the corrected three-study ITC benchmark of 2.2 to 2.8 x 10^3 M^-1.
- **Controls:** C-alpha, C-gamma (size match); M0, M-ox (nonspecific sorption baseline).
- **Falsification:** failure of (a) or (b) reclassifies uptake as nonspecific sorption and voids the correspondence.

## HC2. Chain-length gate on the layer contribution (prototype 2 principle; metric rebuilt per the design-1 attack)

- **Biological feature (verified at pharmacology level):** GPR43 responds to C2-C5 carboxylates, not to C6+ and not to C1, because a shallow pocket caps incremental apolar burial while a polar anchor does most of the work.
- **Material implementation:** depth-limited (7.9 angstrom) neutral cavity on a non-cationic surface.
- **Metric, defined on the layer, never on the raw composite:** delta-Kd per accessible cavity, equal to Kd(composite) minus Kd(M0 blank), normalized to adamantane-counted cavities, must be significantly flatter across PFBS/PFHxS/PFOS than the strongly long-chain-skewed profile of M0. The C-silica non-adsorbing-carrier control must show the same flattening without any carbon partitioning. PFBS Kd retention under equimolar PFOA competition is a measured gate, not an assumed inversion. No composite-level alpha(PFBS/PFOS) greater than 1 is registered.
- **Controls:** M0 (carrier ladder), C-silica (partitioning-free readout).
- **Falsification:** if the layer's per-cavity profile is as long-chain-skewed as M0, or C-silica contradicts the composite-derived value, the gate correspondence is withdrawn and the design reverts to an honest broadened-envelope claim (carbon keeps long chains, CD adds short-chain Kd, no selectivity claim).

## HC3. Entry-face orientation (prototype 1 geometry; the residual novelty axis)

- **Feature:** fluorinated tails are reported to enter from the wide secondary face with the headgroup hydrated at the rim. The literature basis must be re-verified for beta-CD specifically; failing that, this feature is labeled hypothesis.
- **Implementation:** primary-face mono-tether presenting the wide face.
- **Measurement:** primary-face-tethered material versus C-random (mixed-face tether at equal CD loading, equal accessible-cavity count, equal residual-OH budget) must give Ka(oriented)/Ka(random) at or above 1.5 for PFBS. Accessibility matching is mandatory so orientation is not confounded with crosslink density. Supporting spectroscopy uses soluble mono-6-amino-CD model complexes or HR-MAS NMR on powders, not broad-line NMR on GAC at trace loading.
- **Control:** C-random.
- **Falsification:** a ratio below 1.5 downgrades orientation to a neutral manufacturing choice. The design is narrowed but not killed.

## HC4. Engineering survival gate (budgeted first per the design-4 attack; failure terminates the design)

- **Product claim:** a verified short-chain increment in real water at trace level in GAC format.
- **Measurement:** rapid small-scale column test (RSSCT) at 50 to 500 ng/L PFBS in real secondary effluent and in 1 mM Na2SO4, with virgin GAC and a DEXSORB-class CD-polymer benchmark in parallel.
- **Pre-registered pass bars:** apparent Kd(PFBS) at or above 10^4 L/kg at 1 ug/L in 1 mM sulfate (the threshold the cost case actually needs, replacing the earlier token 10x gate); at least 3x GAC bed volumes to the effluent target; mass-normalized parity or better versus the CD-polymer benchmark; regeneration of at least 5 cycles with less than 10% capacity loss per cycle.
- **Secondary metric:** GenX reported separately with its own bar, its Ka range and branched-ether steric caveat acknowledged, consistent with its superseded-pollutant contract status.
- **Falsification:** failure of the Kd or bed-volume bar terminates the design regardless of HC1-HC3 outcomes.

## How these correspondences prove the biomimetic mechanism

HC1 proves the recognition unit is doing inclusion chemistry rather than nonspecific sorption. HC2 proves the layer expresses the transferred 设计原理 (design principle) of the depth-limit gate, with the silica control excluding the carrier as an explanation. HC3 proves that the geometry of presentation, the design's novelty axis, is causally responsible for part of the affinity. HC4 proves the mechanism survives translation into the engineering format. A design that passes HC1 and HC4 but fails HC2 is still a usable broadened-envelope sorbent; a design that fails HC4 is terminated no matter how elegant HC1-HC3 are.

---

# Experimental Validation Plan

Phased, kill-gate-ordered program. No phase begins before the previous gate passes; the cheapest decisive experiments run first. GenX is tracked throughout as a separately gated secondary metric.

## Phase 0: Paperwork gates (week 0)

- Evidence-ledger entries with tier boundaries: Stoddart JBC 2008 (283:32913-32924, corrected), Le Poul JBC 2003, Brown JBC 2003; the three PFBS-beta-CD ITC studies with Weiss-Errico 2017 relabeled as gamma-CD; GenX Ka as a method-dependent range; the ACS Cent. Sci. 2022 percentages re-verified from full text; the 2023-2025 short-chain platforms (ES&T 2023, JACS 2024, ES&T 2024, Nature Water 2025) each with a what-it-fails-to-deliver note.
- Commission the SciFinder/WoS novelty audit and the freedom-to-operate search.
- **Success criterion:** every quantitative claim in this document maps to a ledger entry or is explicitly labeled inference.

## Phase 1: Material characterization (gates G0/G1 chemistry)

- ITC and 19F NMR on soluble mono-6-amino-CD and its amide-capped form (G0).
- On the composite: TGA (CD wt%), XPS, Boehm titration, BET and NLDFT pore-size distributions before and after grafting, zeta potential versus pH, accessible-cavity census by adamantane-1-carboxylate uptake, covalent-fraction mass balance (post-hydrolysis or labeled tracer), 7-day and stress leaching.
- **Success criteria:** Ka within the 2.2 to 2.8 x 10^3 M^-1 benchmark window and sulfate-tolerant at G0; 5 to 15 wt% CD; BET retention at least 80% of parent GAC; neutral zeta at pH 7; no detectable CD leaching.

## Phase 2: Adsorption performance (batch, correct concentration)

- LC-MS/MS quantification at 100 to 500 ng/L PFBS; Freundlich isotherm over 0.1 to 100 ug/L; kinetics to equilibration on the composite and on M0/M-ox.
- **Success criteria:** isotherm closure at ng/L; apparent Kd trajectory consistent with the 10^4 L/kg bar at 1 ug/L; blank-GAC subtraction reported for every point; saturation capacity reported per gram of total composite and per packed-bed volume.

## Phase 3: Selectivity and mechanism (HC1-HC3)

- Four-PFAS mixture (PFBS/PFPeS/PFHxS/PFOS); equimolar PFOA competition; adamantane displacement (HC1a); cavity-size series C-alpha/C-gamma at equal molar loading (HC1b); orientation pair versus C-random at equal accessibility (HC3); layer-normalized chain-gate metric including C-silica (HC2); loading series C-load for local-density dependence.
- **Success criteria:** displacement at least 50%; ordering beta > gamma > alpha; orientation ratio at least 1.5; per-cavity ladder significantly flatter than M0 and reproduced on silica; PFBS Kd retention under PFOA competition measured and reported.

## Phase 4: Matrix tolerance (frozen four-matrix protocol)

- Matrices: nanopure water; 1 mM Na2SO4; NaCl/NaHCO3; real secondary effluent. DOM panel 0 to 10 mg/L TOC with size-fractionated NOM. DOM is treated as a primary measured risk, not as a claimed scaffold benefit (the design-3 geometry rebuttal is accepted).
- **Success criteria:** Kd in sulfate and effluent reported against the 10^4 L/kg bar; DOM dose-response quantified; no reliance on pure-water performance in any claim.

## Phase 5: Regeneration, stability, and column survival (HC4; months 4 to 9)

- RSSCT at 50 to 500 ng/L PFBS in secondary effluent and in 1 mM sulfate, with virgin GAC and a DEXSORB-class benchmark in parallel; regeneration cycling (methanol or 50% ethanol with 0.1 to 0.5% NaCl, 40 to 50 C, solvent distilled, PFAS concentrate to destruction); accelerated aging in a biofilm-seeded 60 to 90 day column with TOC-bleed and capacity-drift monitoring.
- **Success criteria (pre-registered):** apparent Kd(PFBS) at or above 10^4 L/kg at 1 ug/L in 1 mM sulfate; at least 3x GAC bed volumes to target; mass-normalized parity or better versus the CD-polymer benchmark; at least 5 regeneration cycles with less than 10% capacity loss per cycle and full mass balance.

## Decision tree after Phase 5

- All gates pass: hand off as an experimental candidate with frozen controls, per-bed-volume reporting, blank-GAC disclosure, and the levelized cost model.
- HC2 fails but HC1/HC4 pass: reframe as a broadened-envelope GAC upgrade with no selectivity claim, labeled 仿生启发/rational hybrid, with the biomimetic correspondence count downgraded accordingly.
- HC4 fails: terminate; the failure cost is bounded by the gate ordering.

---

# Cost and Scalability Analysis

**Cost target:** below 5 yuan/g (approximately 690 USD/kg). Met with large margin at pilot scale; met even at bench scale except at the reagent-pricing extreme.

## Bench-scale cost, per kg composite (oriented monolayer, 10 wt% CD)

| Item | Amount | Unit cost | Cost (USD) |
|---|---|---|---|
| Bituminous GAC | 0.90 kg | 2-4 USD/kg | 2-4 |
| Mono-6-amino-beta-CD (in-house from beta-CD at 8-15 USD/kg via tosylation/amination; reagents about 20-40 USD per 0.1 kg batch) | 0.10 kg | 100-300 USD/kg-equivalent | 30-60 |
| EDC/NHS (about 2.5 mmol/g activated sites) | reagent grade | dominant lab cost driver | 300-700 |
| Buffers, ethanolamine, solvents | - | - | about 10 |
| **Bench total** | | | **about 350-780 USD/kg** |

The top of the range is a lab-scale artifact of carbodiimide reagent pricing, not a process cost; this honest accounting is imported from design 2.

## Pilot-scale cost, per kg composite (process chemicals)

- Replace EDC/NHS with CDI or cyanuric-chloride coupling (10 to 30 USD/kg reagent class), with byproduct removal from porous carbon included as a wash burden.
- Mono-6-NH2-CD at 50 to 150 USD/kg from bulk beta-CD.
- GAC at 2 to 4 USD/kg.
- **Estimated total: 15 to 45 USD/kg**, roughly 0.02 to 0.05 yuan/g, two orders of magnitude under the 5 yuan/g ceiling.
- Network arm (if invoked): terephthaloyl chloride at 10 to 20 USD/kg, under 5 wt% of composite, plus one unit operation: plus 3 to 8 USD/kg.

## Benchmarks

| Technology | Cost | Short-chain service weakness |
|---|---|---|
| Virgin GAC | 2-4 USD/kg | 5-20x more frequent changeout in PFBS service (5,000-20,000 BV) |
| DEXSORB-class CD polymer | 150-500 USD/kg | specialty polymer, not GAC-format drop-in |
| Strong-base anion exchange | 15-40 USD/kg plus brine handling | sulfate fragility in short-chain service |
| Fluorinated PAF (Nature Water 2025) | high, fluorinated | lifecycle burden; not granular drop-in |

The composite's fluorine lifecycle burden is zero: no fluorinated reagents anywhere in the route. This is a genuine cost and regulatory advantage over TFN networks and over the deleted fluorophenyl design.

## OPEX honesty

The treatment-cost scenario is built bottom-up from measured Kd and RSSCT bed life only after HC4 data exist. Regeneration (methanol at roughly 0.3 to 0.5 USD/kg solvent, largely distillable) plus PFAS-concentrate destruction is an explicit OPEX line, not omitted. A levelized USD/m3 comparison versus GAC and ion-exchange incumbents, with cycle-life sensitivity, is required before any scale claim. **Break-even rule (imported intact):** the composite must deliver at least 3x GAC bed life for PFBS; otherwise re-bed GAC or ion exchange wins and the design has no commercial case.

## Scalability and path to commercialization

Every unit operation is standard: acid/base washing, nitric oxidation, aqueous carbodiimide (or CDI/cyanuric-chloride) coupling, solvent washing, solvent-regenerable operation. All steps run below 60 C in aqueous buffers. Raw materials are commodity (bituminous GAC, starch-derived beta-CD at more than 10,000 t/yr global production). The manufacturing risks are QC discipline (covalent-fraction verification, accessible-cavity census) and the coupling-reagent supply chain, both routine at industrial scale. Deployment path: RSSCT, pilot column on real secondary effluent, NSF/ANSI 61 extraction testing budgeted from the outset for drinking-water adjacency, then licensing to a GAC producer or water-treatment media supplier. Freedom-to-operate clearance is a hard gate before any commercialization statement.

---

# Honest Assessment

## Biomimetic strength: moderate

The structural half of the biomimesis is strong: beta-cyclodextrin is a natural, enzymatically produced molecule whose inclusion chemistry is verified by calorimetry and crystallography, and the material uses the molecule itself rather than a vague analog. The functional half is a principle-level transfer: the GPR43 depth-limit gate is verified pharmacology, but its translation into a surface-tethered neutral cavity is an analogy tested by HC2, not a demonstrated equivalence. HC3 (orientation) rests on a literature basis that must be re-verified for beta-CD specifically. Overall: one hard structural correspondence with strong evidence, one principle correspondence of moderate strength, one geometry correspondence pending re-verification.

## Evidence quality map

- **FACT:** beta-CD geometry (6.0-6.5 angstrom cavity, 7.9 angstrom depth) from crystallography; PFBS Ka of 2.2 to 2.8 x 10^3 M^-1 (three-study ITC consensus); chain-length rise of Ka toward PFOA; GAC short-chain breakthrough deficiency; cationic-platform collapse in sulfate (E056, percentages pending full-text recheck); GPR43 pharmacology C2-C5 active, C6+ inactive, C1 inactive; epichlorohydrin hazards and gel collapse; chitosan protonation arithmetic.
- **LEAD:** wide-face entry orientation for fluorinated tails in beta-CD (provenance to be re-verified for beta-CD specifically); network-rigidity affinity enhancement as a transferable effect (TFN precedent, different composition); GenX Ka as a method-dependent range with an open branched-ether steric question.
- **INFERENCE:** orientation benefit magnitude (HC3 ratio); depth-gate flattening on a surface-tethered cavity (HC2); local-cavity-density avidity at ng/L; the roughly 10^4-fold effective enhancement from monomer to composite.
- **UNVERIFIED:** apparent Kd at ng/L in real effluent; DOM competition magnitude; regeneration cycle life; biofilm-aged stability.

## Principal risks

1. **The enhancement bet (largest).** The design requires about 10^4 effective affinity enhancement over the monomer at ng/L. If multivalency and local-density effects on a non-swelling carbon surface fall short by orders of magnitude, and the loading series shows no superlinear trend, the material is a marginally better GAC, not a short-chain sorbent. Gated at G0/G1; the network arm is the single fallback.
2. **DOM competition.** Humic molecules compete for cavities and can block pore mouths. The design accepts the design-3 rebuttal and treats DOM as a measured risk (Phase 4 panel), not a managed benefit.
3. **Pore-locus uncertainty.** Grafting cannot be directed a priori to outer surfaces; CD may land inside mesopores and lose accessibility, or block micropores and erode the carrier's long-chain sink. NLDFT mapping and the BET retention gate exist precisely to catch this.
4. **Grafting QC ambiguity.** TGA/FTIR cannot separate grafted from occluded CD; the mass-balance and tracer methods in Step 4 are mandatory, not optional.
5. **GenX sterics.** The branched ether may fit the cavity poorly; GenX stays a separately gated metric and cannot rescue or sink the primary claim.
6. **Prior-art and IP compression.** The 2023-2025 platforms narrow the white space; the novelty audit and FTO opinion are hard preconditions, and the CycloPure record must be cited as the documented 2021 DuPont partnership, not as an acquisition.

## What could go wrong, stated plainly

The soluble chemistry could survive G0 and the grafted layer could still underperform, because tethering changes hydration and rim dynamics in ways ITC on model compounds does not capture. The orientation effect could be real but small, collapsing HC3 into a manufacturing footnote. The chain-gate flattening could be an artifact of pore-size selection by the carbon rather than a cavity property, which is why the silica control exists. Regeneration could work chemically and fail economically if cycle life is short. Each failure mode has a pre-registered detection point and a bounded cost, which is the operative meaning of the kill-gate ordering.

---

# Novelty Statement

Defensible novelty is deliberately narrow and survives the prior-art audits of four attack rounds.

## What is novel

1. **Orientation-controlled primary-face tethering of beta-CD on granular activated carbon for short-chain PFAS.** To our knowledge this specific construction has not been published. Both design 3 and its attacker independently identified it as the residual white space after accounting for epichlorohydrin-CD-on-carbon (Long et al., Chemosphere 2020), CD-polymer-functionalized GAC for GenX/PFBS, and CD-biochar composites. Orientation is not cosmetic here: it is the variable that maximizes correctly presented cavities per grafted molecule, and it is tested causally against an accessibility-matched mixed-face control (HC3).

2. **The layer-isolated chain-gate metric.** Delta-Kd per accessible cavity, with blank-GAC subtraction and a non-adsorbing-carrier (silica) control, is a new measurement construct, not packaging. It makes the GPR43-derived depth-gate principle falsifiable on a carbon carrier for the first time, and it immunizes the selectivity claim against the carrier-partitioning confound that invalidates composite-level alpha metrics.

3. **The optional terephthaloyl rigid-network-on-GAC arm.** A fluorine-free structural analog of the TFN rigidity lesson, differentiated in composition from the Dichtel/CycloPure/DuPont thicket. Conditional on a formal freedom-to-operate search, which is a mandatory pre-materialization gate. The ledger must also correct the acquisition claim to the documented 2021 DuPont-CycloPure partnership.

## What is explicitly not claimed as novel

- Beta-CD host-guest chemistry itself (decades of literature, three-study ITC consensus cited here).
- CD-on-carbon composites in general (multiple prior arts).
- Short-chain-selective CD polymers as a class (JACS 2024 and relatives).

## Why this deserves publication

The contribution is a verified negative result avoided and a falsifiable positive claim: a neutral, oriented recognition layer that adds a short-chain increment to the world's standard adsorbent format, with a measurement construct that lets reviewers separate layer chemistry from carrier partitioning. Whether HC2 passes or fails, the layer-isolated gate metric and the accessibility-matched orientation control are publishable methodological contributions. A systematic SciFinder/WoS novelty audit plus an FTO opinion is a hard gate before any paper or commercialization statement.

---

# Visual Aids

## Figure 1. Material structure (cross-section, not to scale)

```
                 bulk secondary effluent (PFAS at ng/L, DOM, sulfate)
   ........................................................................
        PFBS (C4)            PFHxS/PFOS (C6-C8)            NOM (kDa)
          |                      |                            |
          v                      v                            v
   +-------------------------------------------------------------------+
   |   ORIENTED beta-CD MONOLAYER (5-15 wt%, net-neutral surface)       |
   |   wide rim: secondary 2-OH/3-OH belt faces solution                |
   |                                                                   |
   |        _________          _________          _________            |
   |       /         \        /         \        /         \           |
   |      |  cavity   |      |  cavity   |      |  cavity   |          |
   |      | 6.0-6.5 A |      | 6.0-6.5 A |      | 6.0-6.5 A |          |
   |      | depth 7.9A|      | depth 7.9A|      | depth 7.9A|          |
   |       \_________/        \_________/        \_________/           |
   |       narrow rim        narrow rim          narrow rim            |
   |           |                 |                   |                 |
   |     C(=O)-NH (single amide tether per CD, primary face)           |
   +-----------|-----------------|-------------------|-----------------+
   |        GAC CORE (12x40 mesh, BET 900-1100 m2/g)                   |
   |   surface -COOH: amide to CD  |  residual -COOH capped with       |
   |                               ethanolamine (neutral layer)        |
   |                                                                   |
   |    [micropore <2 nm]   [mesopore]   [micropore]                   |
   |    long-chain PFAS + NOM partition sink (native GAC function)     |
   +-------------------------------------------------------------------+
```

## Figure 2. Single recognition unit (人工识别单元) and guest orientation

```
   solution side
                    hydrated -SO3(-) head at the rim (neutral H-bond contact)
                                 |
   PFBS:  (-)O3S-CF2-CF2-CF2-CF3
                                 v
          wide rim  o o o o o o o o o      <- secondary OH belt (entry face)
                    \                 |
                     )   apolar,      |    beta-CD truncated cone
                     )   polarizable  |    (tail fully buried: C4 fits
          narrow rim /_________________|     within the 7.9 A depth)
                          |
                       -CH2-NH-C(=O)-        <- single primary-face amide tether
   =======================|================================================
                     GAC surface (oxidized; residual COOH capped)
```

## Figure 3. Biomimetic mechanism: GPR43 gate transferred to the CD layer (设计原理)

```
   GPR43 / FFAR2 (biological gate)              PFBS-CD-OG1 layer (artificial gate)
   -------------------------------              --------------------------------
   shallow polar pocket                          7.9 A neutral cavity
   Arg180/Arg255/His242 anchor at mouth   ~=>    secondary-OH rim contact (neutral,
                                                 no guanidinium, no charge)
   depth-limited apolar contact zone       ~=>   cavity depth caps incremental
                                                 burial per CF2
   C2-C5 active / C6+ no further gain       ~=>   flatter per-cavity Kd ladder
   (polar anchor does most of the work            across PFBS/PFHxS/PFOS;
    for the shortest ligands)                     short-chain increment enriched
                                                 vs blank GAC (HC2 metric:
                                                 delta-Kd per accessible cavity)

   Chain length:   C2   C4   C6   C8
   GPR43 response: ###  ###  .    .      (flat beyond pocket depth)
   CD-layer goal:  ###  ###  ##   ##     (flattened vs GAC's strongly
   blank GAC:      .    #    ###  #####   long-chain-skewed profile)
```

## Figure 4. Synthesis and decision flow

```
   [G0 soluble gate: ITC + 19F NMR on mono-6-NH2-CD and amide-capped model;
    nanopure / 1 mM Na2SO4 / +PFOA]
        | pass (Ka within 2.2-2.8e3 M^-1, sulfate-tolerant)
        v
   GAC wash (HCl/NaOH) --> mild HNO3 oxidation (60 C, 3 h; BET loss <20%)
        --> EDC/NHS activation (MES pH 5.5) --> mono-6-NH2-CD coupling
        (HEPES pH 7.4, 24 h, RT) --> ethanolamine cap --> wash to no CD bleed
        --> QC: covalent fraction, adamantane cavity census, XPS, TGA,
            BET/NLDFT, zeta, leaching
        v
   [G1 batch: HC1 displacement + cavity series; HC3 orientation ratio;
    HC2 layer-normalized gate with C-silica; DOM panel]
        |-- Kd within reach of 1e4 L/kg bar ------------------> [G2 RSSCT]
        |-- Kd short by orders of magnitude, no superlinear
        |   loading trend --> [FTO opinion] --> terephthaloyl
        |   network arm --> retest; fail --> STOP
        v
   [G2 survival gate: RSSCT at 50-500 ng/L in effluent + 1 mM sulfate;
    benchmarks: virgin GAC, DEXSORB-class polymer; regeneration >=5 cycles;
    biofilm aging 60-90 d]
        | pass all bars
        v
   Handoff: frozen controls, per-bed-volume reporting, blank-GAC disclosure,
   levelized cost model. (HC2 fail with HC1/HC4 pass: reframe as
   broadened-envelope GAC upgrade, no selectivity claim.)
```

---

## 对抗审查记录

本设计经过 4 个独立设计师和 4 个独立攻击者的对抗研讨：

- **设计 1（GPR43 多点识别）**: 46/100 - 失败（胍基硫酸根陷阱）
- **设计 2（锌酶配位）**: 39/100 - 失败（碳酸氢根竞争、金属溶出）
- **设计 3（环糊精主客体）**: 54/100 - 最高分（核心识别化学真实、已验证）
- **设计 4（生物膜 EPS）**: 36/100 - 失败（电荷捕获、硫酸根不稳定）

**综合策略**: 提取设计 3 的环糊精核心 + 设计 1 的链长门原理 + 设计 2 的成本现实 + 设计 4 的冷冻矩阵测试协议

---

## 工作流元数据

- **工作流 ID**: wydj333t5
- **Agent 数量**: 10
- **工具调用**: 124
- **Token 消耗**: 558,475
- **耗时**: 63.7 分钟
- **完成时间**: 2026-07-18 18:46

---

**文档状态**: 完整设计方案，待实验验证  
**下一步**: Phase 0（证据台账录入 + 新颖性审计 + FTO 搜索）
