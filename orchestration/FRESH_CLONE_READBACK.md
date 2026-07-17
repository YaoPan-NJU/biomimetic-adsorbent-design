# Fresh-clone continuity validation

Validation date: 2026-07-16
Validated commit: `53014c468f2e174f5ff69737f7a64e66ff7fee06`

## Mechanical checks

The private remote was cloned into a new empty directory. The clone had a clean worktree and the expected `main` HEAD. Commands run inside the clone:

```text
python3 scripts/validate_repository.py
python3 scripts/scan_credentials.py
machine-specific absolute-path scan
```

Results:

- 49 state-indexed artifacts resolved.
- Six BMDL snapshot files existed and matched committed SHA-256 values.
- 113 tracked files passed credential-pattern scanning.
- No machine-specific absolute path remained.

## Context-free Codex readback

An isolated Codex with no inherited conversation context was instructed to read only the fresh clone and follow `AGENTS.md`. It correctly recovered:

- the independent, non-ADRMATS objective and municipal-secondary-effluent scope;
- D1-A as the 93/100 primary and D1-B as the 89/100 backup;
- the meaning of design pass and the absence of experimental results;
- the rejection reasons for clarithromycin, PFOA, nitrate and ODV concepts;
- `exclude_design_stage_allow_posthoc_negative_audit_only` as the BMDL policy;
- Pan Yao's approval authority and Zhou Jiaqi's post-approval experimental role;
- the exact pending continuity action recorded at that commit.

The readback concluded that the repository alone was sufficient to continue without the original chat. The pending continuity action identified by the clone has since been completed by this validation and is replaced in `PROJECT_STATE.yaml` with Pan Yao's review action.

## S11 checkpoint validation

Validation date: 2026-07-17

Validated commit: `739c39d83d120aa4d70ae143f874029b335986eb`

The private remote was cloned into a new empty directory after the top-five Round 2/3, external-prototype reopening and S11 Gate 1a checkpoint had been pushed. The fresh clone was clean and matched `origin/main`.

Mechanical results:

- `scripts/validate_repository.py`: 80 state-indexed artifacts resolved and six BMDL snapshot checksums passed.
- `scripts/scan_credentials.py`: 145 tracked files passed; no credential pattern was found.
- `scripts/validate_s11_constructs.py`: all eight 148-aa mature Sortase substrates passed the whole-file hash, per-record hash, P15090 core and declared-mutation checks.
- No `/Users/panyao` or temporary-clone absolute path was present in tracked project content.

A context-free Codex with no inherited conversation read only the fresh clone and correctly recovered:

- the independent objective, municipal-secondary-effluent matrix and organic/emerging-pollutant scope;
- the Round 2 disposal of S3/S4/S5/S6 and the 56/100 termination of S1 in Round 3;
- why direct `9OB7/9MIW` evidence admitted S11 without inheriting the old S1 score;
- Gate 1a pass, Gate 1b procurement block, Gate 2 experimental critical/high issues and the absence of an active primary or backup;
- preservation of the historical phosphate D1-A/D1-B artifacts;
- the BMDL design-stage exclusion policy;
- Pan Yao review as the unique current action, followed by Gate 1b only if laboratory work is later authorized.

The repository is sufficient for another Codex instance to continue without the original chat. This validation does not convert S11 into a passed material and does not authorize ordering or experiments.

## Synthetic-material direction recovery checkpoint

Validation date: 2026-07-17

Validated commit: `266df42e09800974262f68361ae1ea7bdd257ebf`

The checkpoint that corrected the protein/peptide design drift was pushed to `origin/main` and cloned into a new directory. Repository-level `eol=lf` handling removed the prior Mac/Windows byte-hash mismatch.

Mechanical results:

- `scripts/validate_repository.py`: 81 state-indexed artifacts resolved and six BMDL snapshot checksums passed.
- `scripts/scan_credentials.py`: 147 tracked files passed.
- `scripts/validate_s11_constructs.py`: all eight historical constructs and the whole-file SHA-256 passed; the S11 record remains intact although its route is scope-superseded.
- No local Windows, prior Mac user, or temporary-clone absolute path was found in tracked project content.

The fresh clone identifies `synthetic_material_direction_recovery` as the active phase, `S1-SYN` as the only active deep concept, no primary or backup, and one next action: submit an exact nonpeptidic receptor plus OEG-passivated mesoporous-silica immobilization SOP. No context-free model readback was repeated for this checkpoint; the recorded validation is mechanical and document-consistency based.

## ROX-2 and BPA-5 termination checkpoint

Validation date: 2026-07-18

Validated commit: `7c573bb857281994a5bb1201edde84db621fb3ee`

The private remote was cloned into a new empty directory after both paper attacks and independent reviews had been pushed. The clone was clean and matched `origin/main`.

Mechanical results:

- `scripts/validate_repository.py`: 104 state-indexed artifacts resolved and six BMDL snapshot checksums passed.
- `scripts/scan_credentials.py`: 177 tracked files passed; no credential pattern was found.
- `PROJECT_STATE.yaml` and all gate YAML files parsed successfully.

A context-free Codex reading only the clone correctly recovered:

- the artificial-material objective, municipal-secondary-effluent matrix and absence of a primary or backup;
- the 40/100 termination of ROX-2 because no ROX-specific ribosomal geometry or exact artificial slit exists;
- the 40/100 termination of BPA-5 because the two-ended ERRgamma necessity claim is unsupported, no exact aqueous calix[4]arene receptor passed, and direct CalP4 prior art exists;
- BPA-2E, PFBS-1, downgraded ROX-2 and CalP4 as controls rather than candidates;
- DCP-1 environmental relevance and soluble-recognition paper attack as the unique next action;
- the prohibition on POP design, procurement, synthesis and experiment at this stage.

The repository is sufficient for another Codex instance to continue without the original chat at this checkpoint.
