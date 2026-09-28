---
name: cobalt
description: Start here — state, then rules for working on Cobalt.
updated: 2026-09-28
---
## Start here
[stated 2026-09-28 · Dejan]
- Read `## NOW` below. Then read `/Users/cobalt/Vault/Think/6 - Permanent/Memory/INDEX.md` once and obey its `## start`, skipping [[cobalt]] (this file). A `[[name]]` resolves to `name.md` under the memory root, `areas/`, `topics/` or `people/`; archived files are addressed by explicit path. A `[[name#heading]]` selects the heading whose complete text, after its leading `#` marks and space, equals `heading`. Read its body until the next heading of equal or higher level, or EOF. A missing or ambiguous target is reported, never guessed.
- The sections from `## Build rules` down are the rules for building Cobalt. Every house but the CTO desk reads them now; the desk opens them when its task plans, drafts, builds, reviews or documents Cobalt code, config or docs.

## NOW
«snapshot ≤1,500 chars, rewritten whole at every close and desk refresh»

## What Cobalt is
[stated ≤2026-09-05 · export]
- Trading wingman: scanner → in-play pool → graded cards → sizing → alert. He trades by hand; Cobalt never touches a platform or trades.

## Working rules
[stated ≤2026-09-10 · CLAUDE.md]
- Report: §0 ≤5 lines → tables → ESCALATE; facts only.
- State to vault/DB before `/clear`; avoid `/compact`. Prompts carry paths, not contents; never paste into an auto-mode pane without text.
- Never commit reviewer captures or Codex logs.
- If a law is missing, unreadable or contradictory: report the path and the issue; never substitute a stale copy.

## Build rules
[stated ≤2026-08-22 · CLAUDE.md]
- Python · Pydantic · Postgres + pgvector · rotating logs. Behavior in config, never code; schemas ready for swing and options.
- LLMs read cached, validated data only; code computes every number.
- Sprint close: tests and architecture review; ADR per decision, PDD per module or feature, agent-authored DevDocs per .py accepted by the symbol-check gate. Keep backlog and kanban current; never build ahead of testing and approval.
- Three model failures → next tier.
- Never commit vault content, secrets or gitignored files. Quote the source of every figure.
- [stated ≤2026-09-05 · export] Ruling-heavy sessions end with a ledger appendix. Engineering choices: you decide, and he may veto.

## Sources
[stated 2026-08-29 · export]
- Read `docs/00 - Project/COBALT-REQUIREMENTS.md` before planning or architecture, and `docs/20 - Assessment/TRIAGE.md` before build or design. Project record: `docs/00 - Project/PROJECT-LEDGER.md`; scope: `MVP-CHARTER.md`; sequence: `SPRINT-LADDER-v0_1.md`; queue: `BACKLOG.md`. Designs: `docs/30 - Design/`; ADRs: `docs/10 - Decisions/`. `_imports/`: chat history 08-21 → 09-05 — reasons behind a Ledger line, never a source of truth.

## Production and dev
[stated ≤2026-08-31 · CLAUDE.md]
- Prod = the running install, its Postgres, and the vault at /Users/cobalt/Vault/Think. A production process opens that vault only when its own environment sets COBALT_VAULT_PATH. Dev = worktree, `cobalt_dev`, `~/dev-vault-cobalt` (default), `configs/dev`, dev Mattermost token.
- Sprint done = green smoke test of everything delivered. Order by income; nothing takes the agent down.

## Strangler rebuild
[stated ≤2026-08-28 · CLAUDE.md]
- Old tree: untouched, runnable; KILL code dies there. New code: `src/cobalt/` only, never touching prod. KEEP-AS-IS ports via tests; KEEP-CONCEPT/REBUILD use old code as spec; REDESIGN needs an ADR.
- New config: `configs/dev/`, `configs/cobalt/`, `src/cobalt/` — never top-level `configs/*.yaml`. Check the loader’s glob and git-ignore placement before adding a new-core config file.

## Docs tree
[stated 2026-09-13 · CLAUDE.md]
- `docs/` = vault `0 - Projects/Cobalt`: 00 Project · 10 Decisions · 20 Assessment · 30 Design · 40 DevDocs (PLACEMENT.md) · 50 Roles · 90 References · `_archive`. Git: one carve-out per numbered folder, never widened; never `90 - References/assets/`, `60 - Agent Output/`, `0 - Projects/`. Nothing under docs/ is deleted. Root markdown: CLAUDE, AGENTS, QWEN, README, REQUIREMENTS stub.

## Repo facts
[stated ≤2026-08-31 · CLAUDE.md]
- Old tree: `validation_alias` fields read env only (their `config.yaml` keys are dead); `scribe.py` resolves separately. Memory code says `_hilt_`, schema `hitl_`: log, don't fix.
- `cobalt_master_context.txt` is stale (regenerate: `dev_utils/generate_context.py`). Never run `dev_utils/wipe_memory.py` or `reset_memory_table.py`.
