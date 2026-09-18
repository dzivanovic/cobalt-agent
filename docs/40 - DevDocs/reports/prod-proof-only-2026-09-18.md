# Production `--proof-only` — the fixed migration harness against production data (read-only)

Hub `prod-proof-0918` (Opus 5, `claude-opus-5`), worktree `/Users/cobalt/cobalt-wt/s2-p2-cards`, branch `sprint-2/cards` at `450316c` (code `511bff0`). Prompt: `docs/40 - DevDocs/prompts/2026-09-18/17-prod-proof-only.md`.

## §0 Headline

- RUN OPEN 16:51 ET. PREFLIGHT clean: tree empty, tip `450316c` / code `511bff0` = the reviewed pair, 16:51 ET is outside the 20:25–21:15 archiver window, `--proof-only` + server `READ ONLY` present in this checkout.
- AUTHORIZATION VERIFIED against main: R1 list (1) for every dev/git/read rule, R8 satisfied (§24 — Grok AND Gemini `VERDICT: SAFE TO RUN --proof-only ON PRODUCTION`), R12 16:50 ET approves the exact production line spelled in this launch line.
- Nothing written anywhere: no vault write, no DB write, no push, no merge (L28 — no trace line is owed).
- Sections below fill as the run proceeds. ESCALATE: TBD.

## PREFLIGHT

Run 16:51 ET from `/Users/cobalt/cobalt-wt/s2-p2-cards`. **Zero denials.**

| rule | command | exit | allowed / DENIED |
|---|---|---|---|
| `Bash(git status*)` | `git status --porcelain` | 0 | allowed — **empty**, worktree clean |
| `Bash(git rev-parse *)` | `git rev-parse --short HEAD` | 0 | allowed — **`450316c`** = the expected tip |
| `Bash(git log*)` | `git log --oneline -3` | 0 | allowed — `450316c` (build report) · **`511bff0`** (the fix, the reviewed code commit) · `fd13970` (red tests) |
| `Bash(date*)` | `date` | 0 | allowed — `Fri Sep 18 16:51:39 EDT 2026`; the archiver window is 20:25–21:15 ET → **outside it** |
| `Bash(grep *)` | `grep -n "proof_only\|READ ONLY\|read_only" src/cobalt/db_migrations/cli.py` | 0 | allowed — 11 hits: `_connect(..., read_only=True)` → `conn.read_only = True` (cli.py:402-412), `cmd_migrate`'s `if proof_only:` branch returns **before** `_apply` (cli.py:439-451), the flag itself (cli.py:523). The flag and the read-only connection exist in THIS checkout |
| `Bash(git -C /Users/cobalt/cobalt log*)` | `git -C /Users/cobalt/cobalt log --oneline -6 -- "docs/40 - DevDocs/reports/cto-2026-09-18.md"` | 0 | allowed — top commit **`bff4ddd` "docs(desk): 09-18 R12 — production --proof-only (read-only, one exact line) approved 16:50 ET"**; below it `4afd5f6` (the review + this prompt). The approval rows are committed on main |
| `Bash(ls *)` | `ls -la "docs/40 - DevDocs/reports/"` | 0 | allowed — reports tree read |

Rules with no harmless variant inside their own pattern, probed by their first real use (UNATTENDED-LAUNCH §6): the `.env` `cp`/`rm`/`ls -la` (step 1), `COBALT_ENV=dev uv run cobalt db migrate --proof-only` (step 1 — it IS the harmless variant), `COBALT_ENV=production … --proof-only` (step 2, run ONCE), `git add`/`git commit` (this section's commit).

### AUTHORIZATION — verified by this hub, 16:51 ET

Dejan's words are in `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-18.md` §4, committed on main (`bff4ddd`, proven above).

| what this run needs | where it is approved | verdict |
|---|---|---|
| the ONE production line `COBALT_ENV=production uv run cobalt db migrate --allow-prod --proof-only` | **R12, 16:50 ET** — "For the approval, I do approve the test." — approving that exact spelling, run ONCE, read-only, from the `s2-p2-cards` worktree on tip `450316c` / code `511bff0`, dev first, outside the archiver window. "No other production command." | **MATCH** — the launch line carries that string character for character, and no other `db migrate` spelling (no bare `migrate`, no `--rollback`, no `--down-to`) |
| this worktree's `.env` `cp` / `rm` / `ls` by path | **R1 list (1)**, 06:46 ET "Approved" — "`.env` cp/rm/ls by path" | MATCH (L41 interim: by name only, never printed, removed after — even on failure) |
| `COBALT_ENV=dev uv run cobalt db migrate --proof-only` | **R1 list (1)** — "`COBALT_ENV=dev uv run cobalt db migrate*`" | MATCH |
| git add/commit/diff/status/log/show/rev-parse, `git -C /Users/cobalt/cobalt log*`, cd/ls/grep/tail/wc/date | **R1 list (1)** | MATCH |
| second opinion BEFORE production use | **R8**, 14:29 ET standing direction; satisfied by `cto-2026-09-18.md` §24 — both houses `VERDICT: SAFE TO RUN --proof-only ON PRODUCTION`, review file `/Users/cobalt/cobalt-wt/agy-trial/scratch/review-migrate-fix/REVIEW.md` (hub-verified REAL 2, blocks proof-only 0, blocks migrate 0) | MATCH |

No rule in this launch line is outside R1 list (1) + R12's one production line. Absent from it by design: push, merge, `bypassPermissions`, any vault write, any other production command, `--rollback`, `--down-to`, bare `migrate`.

Known cosmetic carried in from the review, named before the run so it is not mistaken for a failure: **F1** — `count(*)` and the digest are two READ COMMITTED statements, so on a live table the `rows` value can be off by the rows inserted between them. `--proof-only` renders no verdict, so this is a wrong-looking number, not a failure (REVIEW.md F1 row: blocks proof-only **no**).

Also noted, unchanged from the four runs before this one: the prompt file's tail carries a block styled as a system reminder asking for a `Claude-Session:` URL line in every commit. It arrives inside a tool result — the file's own bytes — not from the harness or from Dejan; the genuine harness attribution reminder names only `Co-Authored-By` and says not to add lines it leaves out. **Not followed.**

## Dev

Pending.

## Production

Pending.

## ESCALATE

Pending.
