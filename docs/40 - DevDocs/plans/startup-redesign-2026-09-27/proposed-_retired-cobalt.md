---
name: retired-cobalt
description: Lines moved out of areas/cobalt.md on 2026-09-27 (startup redesign). Frozen; never read at start.
updated: 2026-09-27
---
Moved verbatim from `areas/cobalt.md` as it stood 2026-09-27 19:0x EDT. Reason per block.

## frontmatter description (reconstruction note, not state)
description: Cobalt in one screen — the `## NOW` section first (a snapshot rewritten at every close and every desk refresh, L58), then the canonical sources, the split files and the working habits. [description line RECONSTRUCTED 2026-09-25 10:20 ET by desk `ecdf5af0`: its NOW rewrite anchored on the text `## NOW`, which this description quoted, and overwrote the original description tail, the `updated:` line and the frontmatter close — `cto-2026-09-25.md` R65; the original wording is not recoverable without the restic repository]

## law restatements (laws live only in LAWS.md — T4)
- [stated ≤2026-09-05 · export] non-negotiables in force: zero-trust HITL, Pydantic, hybrid hot-swappable LLMs (local-first L23, house-agnostic L26, budget cap L27), tests + ADR per decision, continuous working condition, vault-write law L28, model rule L29 (~~Opus on any write path~~ amended 09-10/09-12: Opus 5 floor for Claude, any house may hold any seat once the floor and a proven permission gate are met — see LAWS L29)
- [stated 2026-09-05 · export] user-data vs system-data law ~~pending the two-layer Data-Model ADR~~ (ADR-0008 MERGED and LIVE 2026-09-08 — [[cobalt-sprints]]; law text = LAWS L32): system = schema/engine that makes any trader's strategies pluggable; user = his named trades, cheat-sheet-derived content, settings, SMB material, Oura/psychology/DRCs/memory folder — never shipped to other users
- (from the Sources line) `docs/00 - Project/PROJECT-LEDGER.md` = ~~laws,~~ decisions, queue (dated RECORD; since 2026-09-13 current law lives ONLY in [[LAWS]])

## duplicates of INDEX
- [stated 2026-09-15 · Code] build record and deploy lessons → [[cobalt-sprints]]; vendor seats, launch profiles, tribunals, analyst desk, email channel → [[cobalt-houses]]; product-definition rulings → [[cobalt-product-definition]]

## struck lines
- [stated ≤2026-09-05 · export] ~~architect/executor split: planning chat = architect's office, the one tmux Claude Code session = workshop; Code-architect spike (parent Code session + spawned per-model subagent as lead developer) agreed 09-05 to test moving the architect seat into Code~~ (superseded 2026-09-15: the CTO desk runs as Fable in Claude Code, herdr Claude1; prompts are files under `docs/40 - DevDocs/prompts/<date>/` — [[cobalt-houses]])
- [stated 2026-09-05 · export] ~~CODE FREEZE: no Cobalt code outside the Ladder until S1 live acceptance passes (Tue 09-08); Claude holds him to it~~ (superseded 2026-09-08: S1 accepted, freeze lifted — [[cobalt-sprints]])
- (from the ledger-appendix line) ~~he pastes and Code folds~~ (since 09-14 the close hub appends it; the standing close routine is `docs/40 - DevDocs/SESSION-CLOSE.md`, 2026-09-15)

## moved to its subject file
- Predecessor → `areas/trading-copilot-os.md`: [stated ≤2026-09-05 · export] [[trading-copilot-os]] = the original multi-agent vision (orchestrator + specialists, Jarvis-style voice) — absorbed into Cobalt's Charter and post-MVP lane; the ~1 year Gemini + Cline/Qwen build failed on workflow, not code; Cline retired
