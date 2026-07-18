# Codex execution entrypoint

This repository is the single source of truth for the independent biomimetic selective-adsorbent project. It is not an ADRMATS component.

Before any action, read in this exact order:

1. `SOUL.md`
2. `PROJECT_STATE.yaml`
3. `HANDOFF.md`
4. `research_contract.yaml`

Then inspect only the artifacts listed in `PROJECT_STATE.yaml`. Do not recover decisions from chat history when the repository contains a recorded decision.

## Non-negotiable rules

- The remote BMDL/PostgreSQL database is strictly read-only. Use `default_transaction_read_only=on` and a read-only transaction. Never run INSERT, UPDATE, DELETE, DDL, migration, ETL, or administrative statements.
- Design claims, literature facts, and quantitative values must be traceable to the evidence ledger. Unverified statements remain hypotheses and cannot support a hard biomimetic correspondence.
- Freeze model-only work before exposing a design role to BMDL output.
- Keep designer, attacker, and reviewer contexts isolated. Persist role deliverables and decisions, never hidden chain-of-thought.
- Do not commit credentials, tokens, connection strings, restricted full-text papers, or private model reasoning.
- At every material checkpoint, update `PROJECT_STATE.yaml` and `HANDOFF.md`, commit all non-sensitive state, and push `main`.
- Never leave the only copy of a decision or next action in an uncommitted local file.
- Read and obey `docs/TERMINOLOGY.md`. In user-facing Chinese, call synthetic recognition chemistry `人工识别单元`, never the unqualified `受体`; reserve `生物原型` or an exact biological category for proteins, enzymes, ribosomes, and other biological evidence sources.
- Do not reintroduce proteins, peptide chains, folded peptides, expression constructs, or labile biological components into the default material design. They are mechanism evidence only unless Pan Yao explicitly reopens scope.

## Completion protocol

Before declaring a checkpoint portable, verify that the worktree is clean, `main` is pushed, referenced paths exist, credentials are absent, and a fresh clone can identify the exact next action without prior chat context.
