# fresh_1000 Round 3 (R3) — Depth Round Spec

Created 2026-07-30 | Branch: Ultimate | Predecessors: `rounds/fresh_1000` (R1), `rounds/fresh_1000_R2` (R2, see `R2_CLOSEOUT.md`)

## 1. What R3 is (and is NOT)
R3 is a **DEPTH round toward the `research_contract.yaml` target**, NOT another 1000 breadth-first orthogonal angles.
- **Contract target:** 10 PASSING schemes (final_scoring >=85, 0 unresolved critical/high) per pollutant, **200 total**.
- **Order:** EASY-FIRST — deepen the already-passed pollutants toward 10 passes first, then work the unpassed ones.
- **Honest-N clause (non-negotiable):** a recorded N < 10 for a pollutant BEATS padding. "1000" is a nominal ceiling, not a target.

### Why depth, not breadth (evidence from R2)
R2 covered 20/20 with **0 passes** (8 revise + 12 near-exhaustion) and documented that the angle space ORTHOGONAL to R1 is
largely exhausted, with the 8 revises blocked on out-of-repo external gates. Therefore R3 does not chase more orthogonal angles;
it converts the BEST existing candidates (R1 passes' sibling angles, R1-mapped-but-unexecuted angles, and R2 revises) into
additional formal passes where honestly reachable, and records honest exhaustion where not.

## 2. Pass definition (hard constraints, inherited)
A scheme counts toward the 10/pollutant target only if ALL hold:
- Six-dimension score >= 85/100; zero unresolved critical/high.
- Innovation checklist pass; >= 1 hard functional correspondence (biological -> material).
- Web-grounded evidence, no fabrication; distinct selectivity mechanism (not a duplicate of an already-counted angle).
- Orthogonal-enough to already-counted passes for the same pollutant (distinct recognition axis, not a trivial restyle).

## 3. External-gate handling (the decisive R2 lesson)
Many candidates' final ~1-3 point gap to 85 is bound by an EXTERNAL gate (Phase-0 DFT / ITC calorimetry / paid-literature full
text) that cannot be resolved in-repo or fabricated. Policy:
- If a candidate is design-complete with its ONLY residual high being an external gate -> record status `pass_pending_gate`
  (r-score ~83-84, design layer closed, gate + expected post-gate score named). It does NOT count as a formal pass until the gate
  returns GO, but it is the highest-value near-pass and is logged explicitly.
- Do NOT force such candidates to >=85 in-repo (padding). Move to the next candidate/pollutant; record and bypass.

## 4. Per-slot procedure (isolated design-attack-review)
For each depth candidate: (a) state the recognition axis + biological prototype (reuse R2 prototype cards where applicable);
(b) design-attack-review, up to 3 rebuilds; (c) verdict = pass (>=85, 0c/0h) / pass_pending_gate / revise / terminate;
(d) extract intermediate products (scheme file + mechanism map; new prototype card only if a genuinely new prototype); commit/push.

## 5. Easy-first triage (initial; refined per-pollutant in STATUS)
Tier 1 (deepen already-passed, richest remaining angle space): PFOA (26 angles mapped), BPA, Octocrylene (A04 Michael revise ~80),
ROX, DDT. Tier 2 (passed but R1-heavily-terminated -> expect low honest-N): NP, Dieldrin, Endosulfan, PFBS, BDE-209.
Tier 3 (unpassed, R2 revises -> mostly external-gate-bound): PFHxS (~84), PCP (~78), TCDD (~78), DDE, GenX, DCP26, betaHCH, PCB209,
HCBD, Chloroform.

## 6. Milestones (extend R2 M1-M6)
- R3-M-passes: cumulative formal passes toward 200 (10/pollutant). Honest reality tracked, not forced.
- R3-M-library: prototype library toward 120/150 (retrospective prototype mining from deepened passes).
- Completion of R3 = each pollutant reaches 10 formal passes OR honest angle-space exhaustion recorded, per contract.

## 7. State files
`rounds/fresh_1000_R3/STATUS.yaml` (per-pollutant depth tracker), this SPEC, per-pollutant `<slug>/SCHEMES/` + `mechanism_maps/`
+ `prototype_cards/` (reuse R2 cards). Update HANDOFF.md + PROJECT_STATE.yaml at each pollutant checkpoint; commit/push per slot.
