# QWEN.md — Cobalt Trading Agent

Read `CLAUDE.md` for the repository operating contract.

Before work, read `/Users/cobalt/Vault/Think/6 - Permanent/Memory/INDEX.md`, then the `## NOW` section at the top of `/Users/cobalt/Vault/Think/6 - Permanent/Memory/areas/cobalt.md` (current state, rewritten at every close), then its mandatory `LAWS.md` entry at `/Users/cobalt/Vault/Think/6 - Permanent/Memory/LAWS.md`. LAWS.md is the ONLY canonical current law; read it in full. It is also named here directly so every house reaches it in one hop. Open other linked memory files when relevant. Historical memory summaries and this operating contract do not replace current law.

PROJECT-LEDGER.md remains the dated record. A ruling in its appendix is not law until the hub folds it into LAWS.md. Superseded wording lives in LAWS-HISTORY.md. Dejan rules; unresolved law disagreements are OPEN items, never a vote or "dissent recorded and proceed." If required law is missing, unreadable, or contradictory, report the exact path and unresolved issue; do not substitute a stale copy or invent a resolution. Never write directly to the vault; the hub performs the authorized fold through the applicable write path.

## Morning command (RULED 2026-09-14, A)

The day-open sweep is a Cobalt command, not a prompt: run `uv run cobalt day-open` (from `~/cobalt`) and it runs all six checks, writes
`docs/40 - DevDocs/reports/day-open-<date>.md` itself, and prints the VERDICT table. This seat's only job is to run that one command and read what it printed — never compose the checks by hand, never write the report yourself (the Qwen allowlist denies every write for this reason: L49, this seat reads and judges, never composes). Add a verdict on top of it with `uv run cobalt day-open verdict "<one line>"` — that is this seat's one write path, through Cobalt, never a direct file edit.
