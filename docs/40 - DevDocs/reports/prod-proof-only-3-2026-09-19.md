# Production `--proof-only`, THIRD run — the FINAL migration harness meets production (2026-09-19)

Seat: proof hub `prod-proof-0919`, Opus 5 (`claude-opus-5`), worktree `/Users/cobalt/cobalt-wt/s2-p2-cards`, branch `sprint-2/stack`, gated code `ad9b07c`.
Prompt: `docs/40 - DevDocs/prompts/2026-09-19/03-prod-proof-only-3.md`. Authorization: `cto-2026-09-19.md` §4 **R7** (07:49 ET, "Approved"), on `cto-2026-09-18.md` §4 R1 list (1), R12, R16, R18–R21.

## §0 Headline

- RUN IN PROGRESS — this section is rewritten at the close.

## PREFLIGHT

Every allowlisted shape this run needs, in the order the steps use it. Rules with no harmless variant inside their own pattern (`cp`/`rm` of the `.env`, the two `db migrate` lines) are probed by their first real use, per `UNATTENDED-LAUNCH.md` §6.

| # | rule | command | exit | verdict |
|---|---|---|---|---|
| 1 | `Bash(git status*)` | `git status --porcelain` | 0 | allowed — **no output: worktree clean** |
| 2 | `Bash(git rev-parse *)` | `git rev-parse --abbrev-ref HEAD` | 0 | allowed — `sprint-2/stack` |
| 3 | `Bash(git log*)` | `git log --oneline -4` | 0 | allowed — tip `c44c760`, then `ad9b07c`, `fb7911b`, `9f03ec1` |
| 4 | `Bash(git diff *)` | `git diff --stat ad9b07c HEAD -- src tests configs ops` | 0 | allowed — **no output: the only commit above the gated code is report-only** |
| 5 | `Bash(git log*)` | `git log --oneline -1 ad9b07c` | 0 | allowed — the tribunal fold is on this branch |
| 6 | `Bash(date*)` | `date` | 0 | allowed — `Sat Sep 19 07:50:29 EDT 2026`, **outside 20:25–21:15 ET** |
| 7 | `Bash(grep *)` | `grep -n "proof_only\|READ ONLY\|read_only\|REPEATABLE READ\|repeatable" src/cobalt/db_migrations/cli.py` | 0 | allowed — 17 hits; see below |
| 8 | `Bash(ls -la /Users/cobalt/cobalt-wt/s2-p2-cards/.env)` | as written | 1 | allowed (the rule matched; exit 1 is the file being absent, which is the expected starting state) |
| 9 | `Bash(git -C /Users/cobalt/cobalt log*)` | `git -C /Users/cobalt/cobalt log --oneline -6 -- "docs/40 - DevDocs/reports/cto-2026-09-19.md"` | 0 | allowed — `9917515 docs(desk): 09-19 R7 …` proves the approval row is committed on main |

**No denials. 0 rules failed.**

### The three gate conditions, verified by this hub

| gate | evidence | verdict |
|---|---|---|
| Tip is the gated code with report-only commits above it | `git diff --stat ad9b07c HEAD -- src tests configs ops` prints nothing | PASS |
| Snapshot fix present in THIS checkout | `cli.py:488` `conn.isolation_level = IsolationLevel.REPEATABLE_READ`; `cli.py:487` `conn.read_only = read_only`; `cli.py:543` `_connect(…, read_only=True)` on the `if proof_only:` branch (`cli.py:541`); `cli.py:404` prints `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.` | PASS |
| L67 review gate (R18–R21) | `/Users/cobalt/cobalt-wt/agy-trial/scratch/review-harness-0919/REVIEW.md` last line: `REVIEW DONE · grok: 0/0/1 SAFE TO DEPLOY · gemini: 1/0/0 FIX FIRST Q5 · astra: 1/0/1 FIX FIRST 1 · houses that read it: 3 of 3 · hub-verified REAL: 3 (blocks the deploy: 0) · NOT REAL: 0 · UNVERIFIABLE: 1` | PASS — **blocks the deploy: 0** |

Authorization row, quoted from `cto-2026-09-19.md` §4 R7: *"(1) a THIRD run of the exact read-only production line `COBALT_ENV=production uv run cobalt db migrate --allow-prod --proof-only` via `prompts/2026-09-19/03-prod-proof-only-3.md` … launch line = 09-18 R12/R16's with the session name `prod-proof-0919`; every other rule = 09-18 R1 list (1) for the `s2-p2-cards` worktree"*. Match: exact. (The row also pins the prompt file by sha256; `shasum` is not in this session's allowlist, so this hub verifies the row's text and the launch line, not the hash — noted, not routed around.)

Also carried into this run from round 2's ESCALATE 2: if production ever acquired one table name in two of `public`/`user`/`system`, `_schema_of` now raises at the FIRST probe. That outcome would be recorded verbatim as `FAILED: production proof-only — duplicate table name`, never retried.
