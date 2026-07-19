# Claude Code execution entrypoint (Qwen branch)

This repository is the single source of truth for the independent biomimetic selective-adsorbent project. It is not an ADRMATS component. The `Qwen` branch is the active workstream branch shared by Claude Code and Qwen (千问); the `main` branch remains the Codex workstream; `kimi-k3` is frozen at `100b7df`.

## Branch convention

- Claude Code is the primary collaborator. It works on `Qwen` and syncs only with `origin/Qwen`. Never push to `main` or `kimi-k3`.
- Qwen (千问) is the cross-device secondary executor on the same `Qwen` branch and reads `AGENTS.md` as its entrypoint.
- Codex works on `main` and syncs only with `origin/main`.
- Claude Code and Qwen share one branch, so they work sequentially, never in parallel: commit and push `Qwen` before switching executor or device; the incoming executor pulls first and reads the updated state files before any action. If true parallel work is ever needed, reopen a separate branch per executor instead.
- `Qwen` and `main` evolve independently so concurrent Codex sessions do not clash. Do not assume state files are shared across branches. Reconcile manually only if a merge is ever explicitly requested.
- `AGENTS.md` is retained as the Qwen entrypoint and shared-rules reference. On this branch `CLAUDE.md` supersedes it for executor identity and branch sync only; the binding rules below are identical.

## Reading order

Before any action, read in this exact order:

1. `SOUL.md`
2. `PROJECT_STATE.yaml`
3. `HANDOFF.md`
4. `research_contract.yaml`

Then inspect only the artifacts listed in `PROJECT_STATE.yaml`. Do not recover decisions from chat history when the repository contains a recorded decision.

## Executor

The primary executor on this branch is Claude Code; Qwen (千问) is the cross-device secondary executor. Both follow the same contract and the same role-isolation rules, and at most one of them is active at any moment. `research_contract.yaml` records `executor: Claude Code`, `secondary_executor: Qwen`, and `executor_branch: Qwen` here; the `main` branch keeps `executor: Codex`. Pan Yao is the owner and final approver; Zhou Jiaqi is the post-approval experimental handoff. No laboratory work is performed in this repository.

## Non-negotiable rules

- Design claims, literature facts, and quantitative values must be traceable to the evidence ledger. Unverified statements remain hypotheses and cannot support a hard biomimetic correspondence.
- Biomimetic design research uses web-based deep search; no local database dependency exists in this branch.
- Keep designer, attacker, and reviewer contexts isolated. Persist role deliverables and decisions, never hidden chain-of-thought.
- Do not commit credentials, tokens, connection strings, restricted full-text papers, or private model reasoning.
- At every material checkpoint, update `PROJECT_STATE.yaml` and `HANDOFF.md`, commit all non-sensitive state, and push `Qwen`.
- Never leave the only copy of a decision or next action in an uncommitted local file.
- All tasks must be executed at maximum thinking depth; no shortcuts or reduced-depth approximations are permitted.
- Every scheme must pass the innovation checklist (`INNOVATION_CHECKLIST.md`) before formal scoring.

## Role isolation

`orchestration/PROTOCOL.md` requires isolated designer, attacker, and reviewer contexts with bounded inputs and designated output files. Claude Code implements this with isolated subagents or workflow agents that read only their bounded inputs and write only their designated files. Hidden chain-of-thought is never persisted.

## Completion protocol

Before declaring a checkpoint portable, verify that the worktree is clean, `Qwen` is pushed, referenced paths exist, credentials are absent, and a fresh clone of `origin/Qwen` identifies the exact next action without prior chat context. Run `python3 scripts/validate_repository.py`, `python3 scripts/scan_credentials.py`, and (when S11 artifacts are touched) `python3 scripts/validate_s11_constructs.py`.

## De-AI canon

Follow `SOUL.md`: restrained academic Chinese in deliverables; no promotional claims, no em dashes, no `不是……而是……` template, no bare ambiguous pronouns at sentence start, consistent terminology, honest labeling of known, inferred, and unverified. The final report must read as an experimental handoff, not as an AI conversation.

## Takeover record

2026-07-17: Claude Code took over the executor role from Codex at `df8a7ef`, branched to `GLM`, and re-ran the mechanical validators. See `HANDOFF.md` and `orchestration/FRESH_CLONE_READBACK.md` for the checkpoint. The research phase and next action are unchanged by the takeover.

2026-07-19: Methodology correction committed as `75c8144` (supervisor rule, BMDL removal, expanded water scenarios, scientific-problem/engineering-challenge gate, innovation checklist, maximum thinking intensity). The `Qwen` branch was activated from `kimi-k3` HEAD `100b7df`; `kimi-k3` is frozen. Claude Code is the primary executor on this branch and Qwen (千问) the cross-device secondary; the two share `Qwen` sequentially and never push in parallel. See `HANDOFF.md`.
