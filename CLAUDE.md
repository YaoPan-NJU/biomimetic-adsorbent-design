# Claude Code execution entrypoint (GLM branch)

This repository is the single source of truth for the independent biomimetic selective-adsorbent project. It is not an ADRMATS component. The `GLM` branch is the Claude Code workstream; the `main` branch remains the Codex workstream.

## Branch convention

- Claude Code works on `GLM` and syncs only with `origin/GLM`. Never push to `main`.
- Codex works on `main` and syncs only with `origin/main`.
- The two branches evolve independently so concurrent Codex and Claude Code sessions do not clash. Do not assume state files are shared. Reconcile manually only if a merge is ever explicitly requested.
- `AGENTS.md` is retained as the Codex entrypoint and shared-rules reference. On this branch `CLAUDE.md` supersedes it for executor identity and branch sync only; the binding rules below are identical.

## Reading order

Before any action, read in this exact order:

1. `SOUL.md`
2. `PROJECT_STATE.yaml`
3. `HANDOFF.md`
4. `research_contract.yaml`

Then inspect only the artifacts listed in `PROJECT_STATE.yaml`. Do not recover decisions from chat history when the repository contains a recorded decision.

## Executor

Executor on this branch is Claude Code. `research_contract.yaml` records `executor: Claude Code` and `executor_branch: GLM` here; the `main` branch keeps `executor: Codex`. Pan Yao is the owner and final approver; Zhou Jiaqi is the post-approval experimental handoff. No laboratory work is performed in this repository.

## Non-negotiable rules

- The remote BMDL/PostgreSQL database is strictly read-only. Use `default_transaction_read_only=on` and a read-only transaction. Never run INSERT, UPDATE, DELETE, DDL, migration, ETL, or administrative statements.
- Design claims, literature facts, and quantitative values must be traceable to the evidence ledger. Unverified statements remain hypotheses and cannot support a hard biomimetic correspondence.
- Freeze model-only work before exposing a design role to BMDL output.
- Keep designer, attacker, and reviewer contexts isolated. Persist role deliverables and decisions, never hidden chain-of-thought.
- Do not commit credentials, tokens, connection strings, restricted full-text papers, or private model reasoning.
- At every material checkpoint, update `PROJECT_STATE.yaml` and `HANDOFF.md`, commit all non-sensitive state, and push `GLM`.
- Never leave the only copy of a decision or next action in an uncommitted local file.

## Role isolation

`orchestration/PROTOCOL.md` requires isolated designer, attacker, and reviewer contexts with bounded inputs and designated output files. Claude Code implements this with isolated subagents or workflow agents that read only their bounded inputs and write only their designated files. Hidden chain-of-thought is never persisted.

## Completion protocol

Before declaring a checkpoint portable, verify that the worktree is clean, `GLM` is pushed, referenced paths exist, credentials are absent, and a fresh clone of `origin/GLM` identifies the exact next action without prior chat context. Run `python3 scripts/validate_repository.py`, `python3 scripts/scan_credentials.py`, and (when S11 artifacts are touched) `python3 scripts/validate_s11_constructs.py`.

## De-AI canon

Follow `SOUL.md`: restrained academic Chinese in deliverables; no promotional claims, no em dashes, no `不是……而是……` template, no bare ambiguous pronouns at sentence start, consistent terminology, honest labeling of known, inferred, and unverified. The final report must read as an experimental handoff, not as an AI conversation.

## Takeover record

2026-07-17: Claude Code took over the executor role from Codex at `df8a7ef`, branched to `GLM`, and re-ran the mechanical validators. See `HANDOFF.md` and `orchestration/FRESH_CLONE_READBACK.md` for the checkpoint. The research phase and next action are unchanged by the takeover.
