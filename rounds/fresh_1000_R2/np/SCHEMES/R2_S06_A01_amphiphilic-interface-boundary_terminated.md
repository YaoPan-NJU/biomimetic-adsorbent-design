# R2_S06 · R2_A01 NP amphiphilic-interface partitioning (terminated, T1 monotonic trap)

- Program: fresh_1000 Round 2 | Pollutant: NP (nonylphenol) | Tier 2 (Group D) | breadth-first slot 1
- Status: **terminated** (r1 structural T1 monotonic; not rebuildable)
- Score: r1 **48/100**, verdict terminate, 1 critical (structural)
- Role: representative near-exhaustion slot + amphiphilic-axis boundary negative knowledge

## Supervisor summary

NP was DEEP-EXHAUSTED in R1 (A01=92 ipso alpha-quaternary topology PASSED; equilibrium-binding space exhausted; reactive axis
T8-blocked). Angle map: 3 R2 candidates, none A-grade (amphiphilic-interface B/T1-limited; chaotropic X since NP is neutral;
reactive-ipso X/T8-blocked). This slot runs the least-infeasible candidate (amphiphilic interface) to an honest r1 terminate,
documenting the boundary; NP R2 is recorded as honest near-exhaustion (honest N > padding), consistent with R1.

## 1. Scientific problem

NP (neutral para-C9-branched alkylphenol, logKow 4.5-5.2) selective capture in secondary effluent (ng/L-low ug/L). Closest
competitor OP (C8) is also a para-alkylphenol amphiphile. R1 A01 already took the topology axis (alpha-quaternary carbon).

## 2. Designer r1 (amphiphilic-interface attempt)

Proposed a lipid-bilayer/admicelle-mimetic interface (oriented amphiphilic layer) to partition NP + orient its phenol head,
prototype = biological interface partitioning (lipid membrane / lung surfactant). Designer self-flagged the fatal issue:
NP and OP are both amphiphilic para-alkylphenols; interfacial partitioning scales with logKow (NP ~ OP, near-degenerate),
so selectivity degrades to a single monotonic parameter (T1). Oriented-phenol readout adds no orthogonal dimension vs OP
(also para-phenol). Absolute ng/L interfacial partitioning is weak.

## 3. Attacker r1

**C1 (critical, structural, not fixable)** — amphiphilic-interface partitioning is logKow-monotonic (T1). NP vs OP differ by
one CH2 (C9 vs C8) with near-degenerate logKow; interfacial partitioning cannot resolve them without a topology/shape axis —
which is A01's occupied space. No orthogonal 2nd dimension exists for the amphiphilic axis vs OP. Changing interface chemistry/
geometry does not change the monotonic nature (structural, per D-dim). R1 already exhausted the equilibrium-binding space.

## 4. Reviewer r1

C1 upheld, structural (T1). Score: causal 11 / selectivity 6 / translatability 10 / originality 6 / falsifiability 8 / evidence 7
= **48/100**. **Verdict: terminate** (no rebuild — the amphiphilic axis is intrinsically monotonic vs OP; rebuild cannot add an
orthogonal dimension that isn't A01's topology).

## 5. Residual value (negative knowledge)

- **NP amphiphilic-axis boundary**: NP's surfactant/amphiphilic behavior CANNOT serve as a selective recognition axis vs OP
  (both amphiphilic para-alkylphenols, logKow-degenerate); interfacial partitioning is a T1 monotonic trap. Only NP's
  alpha-quaternary-carbon TOPOLOGY (A01, passed) resolves NP from OP — and it is already occupied.
- **NP R2 honest near-exhaustion**: 3 R2 candidates all non-A (amphiphilic B/T1, chaotropic X/neutral, reactive-ipso X/T8).
  Consistent with R1's explicit deep-exhaustion. NP is a case where R1 fully captured the tractable space.
- **Transferable**: for neutral alkylphenol/amphiphile pollutants, the amphiphilic-partitioning axis is monotonic (T1); only
  branch-topology/shape axes give orthogonal selectivity, and those are single-angle (one deep-cage design each).
- Next: DCP26 (Group D, R1 3x terminated on single-parameter-monotonic).
