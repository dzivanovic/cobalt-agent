# F5 gate-run preflight — prompt 970 (read-only), 2026-10-21 07:32 ET

Checked at `main` = `effab441` (`date`: Wed Oct 21 07:31:51 EDT 2026).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git show main:src/cobalt/prefill/checkpoints.py` (CLI at `:837-844`); `desk-launch.sh:131-141` | `checkpoint run --slot HHMM --dry-run` matches the dry-run command byte for byte. Each of the 4 runnable commands (dry run; pytest x2 in one string; pytest x1) has its own `--allowedTools` string, and the step-2 command equals its allow string. `uv run` and `COBALT_ENV=` are write strings the launcher passes only on a HIS RULING + APPROVED RULINGS row (`:135-138`). The one `COBALT_ENV` string is `dev`, not `production` (`:138`), not a glob. No `launchctl`, no `-c` (only `git -C`), no script. | OK |
| 2 | `grep -rn "^| R1863 " reports/` | `cto-2026-10-18.md:90`: `R1863 · HIS RULING · APPROVED (brain, L79)`. Same RULINGS line as precedent 873. | OK |
| 3 | prompt line 1 | `--permission-mode auto` | OK |
| 4 | `data/deploy/bootstrap-owed.json:5-8` vs `## RESULTS` | All four `checkpoint-*` labels list `X2, X3, X4, X5, X6, X7, X10, X12, X13, values card`. The template has the same 10 items, once each, in that order, for 4 labels = 40 lines. Report path `reports/f5-gate-run-2026-10-21.md` is stated. | OK |
| 5 | prompt `RULES` (ONLY A RESULT OF EXACTLY `OK` COUNTS) and `## DECISIONS` | Stated. Every `FAIL` / `NOT RUN` gets an `ASK DESK … [<time>]` with default "plists stay unloaded"; every `OK (…)` gets one with default "the line does not count until the brain rules it". The four `[HIS HAND]` questions are verbatim. | OK |
| 6 | prompt `RULES`, `LIVE COST` | "Run each command once"; "Run once, never retried"; no loop. The only live-cost command is step 1. | OK |
| 7 | `file:line` cites on main | Verified: `checkpoints.py` `:20` `:104` `:167` `:200-235` `:224-235` `:238` `:423-425` `:576` `:607-610` `:697` `:747-751` `:779` `:820`; `client.py:129-133`; `modelaccess.yaml:70-74`; `test_checkpoints_offline.py` `:682` `:747` `:876` (the three `def` lines); `deploy-step-c.sh:185-186`; `F5-FINAL` `:176` `:178-181` `:184` `:186-187`; `bootstrap-owed.json:5-8`. | OK |
| 8 | prompt `WRITE`, `RULES` | "WRITE only …/f5-gate-run-2026-10-21.md"; "No production command"; "The four checkpoint plists stay unloaded … loading them is a separate card"; "no `launchctl` of any kind". | OK |
| 9 | prompt last line of `## REPORT` | `GATES DONE · ok: <n> · fail: <n> · not run: <n>` or `FAILED: <reason>` | OK |
| 10 | `git -C … diff HEAD --quiet -- …970-f5-gate-run.md` | exit 0, empty diff. Committed in `effab441` (= `main` = HEAD). | OK |

## ISSUES

- NOTE · Step 0 `ls -d /Users/cobalt/cobalt-wt/.cobalt_dev.lock` is absent now (exit 1), so step 1 runs as written; the seat should record that exit as expected, not as a failure.
- NOTE · `default_stores()` calls `vault_store.ensure_schema()` (`checkpoints.py:559-563`), so even a dry run opens the dev DB and may run an idempotent schema create. The prompt's "writes no row" holds for data rows; it does not state the schema call. Harmless on dev; not a blocker.
- NOTE · X6's best case is `OK (one real-shape prompt: 07:45 vs prior close)` and X13's is `OK (offline: …)`. Both are qualified, so neither counts at `deploy-step-c.sh:185-186`. Only X2 can reach a plain `OK`. This is by design and already has the "does not count until the brain rules it" default. Expect `ok` in the stop line to be 3 at most.
- NOTE · The `ASK DESK` rule says "one per FAIL or NOT RUN". Read literally it also covers X3 and `values card` ("not this hub's"). The drafter's intent (their lines are the desk's) is clear, but a seat may add two redundant ASK lines. Harmless.
- NOTE · The RULINGS line cites only R1863 (row text unrelated to this run; same line as precedent 873). R2279 and R2276 are DESK RECORD / RECORD rows in `cto-2026-10-21.md:14,17`, cited in prose only, not as rulings. This is fine for the launcher, which reads only the one RULINGS line.

Nothing blocks the launch.

PREFLIGHT DONE · prompt: 970 · checks: 10 · fails: 0 · ready: YES
