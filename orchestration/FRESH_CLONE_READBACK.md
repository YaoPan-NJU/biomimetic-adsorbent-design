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
