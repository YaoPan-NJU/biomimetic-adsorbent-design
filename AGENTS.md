# Qwen execution entrypoint

This repository is the single source of truth for the independent biomimetic selective-adsorbent project. It is not an ADRMATS component.

Before any action, read in this exact order:

1. `SOUL.md`
2. `PROJECT_STATE.yaml`
3. `HANDOFF.md`
4. `research_contract.yaml`

Then inspect only the artifacts listed in `PROJECT_STATE.yaml`. Do not recover decisions from chat history when the repository contains a recorded decision.

## Non-negotiable rules

- Design claims, literature facts, and quantitative values must be traceable to the evidence ledger. Unverified statements remain hypotheses and cannot support a hard biomimetic correspondence.
- Biomimetic design research uses web-based deep search; no local database dependency exists in this branch.
- Keep designer, attacker, and reviewer contexts isolated. Persist role deliverables and decisions, never hidden chain-of-thought.
- Do not commit credentials, tokens, connection strings, restricted full-text papers, or private model reasoning.
- At every material checkpoint, update `PROJECT_STATE.yaml` and `HANDOFF.md`, commit all non-sensitive state, and push the active branch.
- Never leave the only copy of a decision or next action in an uncommitted local file.
- All tasks must be executed at maximum thinking depth; no shortcuts or reduced-depth approximations are permitted.
- Every scheme must pass the innovation checklist (`INNOVATION_CHECKLIST.md`) before formal scoring.

## Completion protocol

Before declaring a checkpoint portable, verify that the worktree is clean, the active branch is pushed, referenced paths exist, credentials are absent, and a fresh clone can identify the exact next action without prior chat context.

