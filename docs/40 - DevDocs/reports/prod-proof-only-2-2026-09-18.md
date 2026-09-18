# Production `--proof-only`, SECOND run — the FINAL code against production data (read-only)

Hub `prod-proof-0918b` (Opus 5, `claude-opus-5`), worktree `/Users/cobalt/cobalt-wt/s2-p2-cards`, branch `sprint-2/stack` at `20add4f` (stack tip `d72ece4`). Prompt: `docs/40 - DevDocs/prompts/2026-09-18/20-prod-proof-only-2.md`. Authorization: `cto-2026-09-18.md` §4 **R16** (17:26 ET, "Approved.") for a SECOND run of the exact line `COBALT_ENV=production uv run cobalt db migrate --allow-prod --proof-only`; R12 approved the first; R1 list (1) for every other rule; R8 second opinion done (§24, both houses `SAFE TO RUN --proof-only ON PRODUCTION`).

## §0 Headline

- RUNNING — filled at the close.

## PREFLIGHT

Run 17:27 ET from `/Users/cobalt/cobalt-wt/s2-p2-cards`. **Zero denials.**

| rule | command | exit | allowed / DENIED |
|---|---|---|---|
| `Bash(git -C /Users/cobalt/cobalt log*)` | `git -C /Users/cobalt/cobalt log --oneline -6 -- "docs/40 - DevDocs/reports/cto-2026-09-18.md"` | 0 | allowed — top row `392a53f docs(desk): 09-18 R16 — proof rerun + second-attempt stacked deploy approved 17:26 ET …`: **R16 is committed on main** |
| `Bash(grep *)` | `grep -n "R16\|R12\|R8\|R1 " "…/reports/cto-2026-09-18.md"` | 0 | allowed — R16 names *"a SECOND run of the exact read-only production line `COBALT_ENV=production uv run cobalt db migrate --allow-prod --proof-only` (R12 approved the first), on the final code, per `prompts/2026-09-18/20-prod-proof-only-2.md`"* → **matches this prompt file and this launch line exactly.** No mismatch |
| `Bash(grep *)` | `grep -n "SAFE TO RUN" …/REVIEW.md` | 0 | allowed — Grok and Gemini both `VERDICT: SAFE TO RUN --proof-only ON PRODUCTION`; hub-verified REAL 2, blocks proof-only **0** |
| `Bash(git status*)` | `git status --porcelain` | 0 | allowed — **empty**, worktree clean |
| `Bash(git rev-parse *)` | `git rev-parse --abbrev-ref HEAD` | 0 | allowed — **`sprint-2/stack`** |
| `Bash(git rev-parse *)` | `git rev-parse --short HEAD` | 0 | allowed — **`20add4f`** = the expected tip |
| `Bash(git log*)` | `git log --oneline -4` | 0 | allowed — `20add4f` · `2f69714` (STACK READY) · `237ef25` (PART B) · `d72ece4` (PART A, the stack tip) — the two report-only commits sit above `d72ece4` as the prompt states |
| `Bash(git log*)` | `git log --oneline --grep="review F1" -1` | 0 | allowed — **`0e1f768 fix(db-migrate): count rows inside the streamed fold — one statement, one pass (review F1)`** is on this branch |
| `Bash(date*)` | `date` | 0 | allowed — **`Fri Sep 18 17:27:52 EDT 2026`** — outside the archiver window 20:25–21:15 ET |
| `Bash(grep *)` | `grep -n "proof_only\|READ ONLY\|read_only" src/cobalt/db_migrations/cli.py` | 0 | allowed — the flag and the read-only connection exist in THIS checkout: `cmd_migrate` `if proof_only:` (line 450) → `_connect(…, read_only=True)` (452) → `conn.read_only = True` (423); `--proof-only` refuses `--rollback`/`--down-to` (434); output line 377 `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.` |

Read for the index card: `UNATTENDED-LAUNCH.md` §2+§6 · Memory `INDEX.md` → `areas/cobalt.md` `## NOW` → `LAWS.md` in full · `migrate-harness-fix-2026-09-18.md` (§0, BASELINE, §3.1, ESCALATE 1–3) · `src/cobalt/db_migrations/cli.py` (`cmd_migrate`, `_connect`, `_probe`, `_stream_row_texts`, `_digest_rows`) · `…/agy-trial/scratch/review-migrate-fix/REVIEW.md`.

**F1 is no longer a caveat on this code.** The prompt's index card warns that the two-statement probe can print a `rows` value off by concurrent inserts. `_probe` at this tip takes both numbers from ONE statement — `rows, digest = _digest_rows(_stream_row_texts(conn, table, stream))`, the count being the rows the cursor yields (`0e1f768`). On a live `bars` the printed count and digest are therefore the same snapshot, and the 8.4M-row table is read once per probe, not twice.

**L28:** nothing is written by this run — no vault write, no DB write, no trace line is owed.
