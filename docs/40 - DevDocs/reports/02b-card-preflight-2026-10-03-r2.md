# Card 02b deploy-hub-text — preflight, round 2 (2026-10-03)

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 44b29c63 main` | no output, exit 0 | OK |
| 1b | `git -C /Users/cobalt/cobalt diff --stat 44b29c63 main -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | empty | OK |
| 2a | `git -C /Users/cobalt/cobalt rev-parse --verify ops/deploy-hub-text-1003` | `fatal: Needed a single revision` (exit 128: branch absent) | OK |
| 2b | `ls /Users/cobalt/cobalt-wt/deploy-hub-text-1003` | `No such file or directory` | OK |
| 3-P1 | `grep -n` on `DEPLOY-HUB.md` | `59:- **P1 DATE AND WINDOW**: \`date\`. Lawful when ONE of these holds; name it in the ro` — (i)–(iv) present, no (v) | OK |
| 3-P7 | same | `65:- **P7 THE MIGRATIONS**: for each head, \`git -C /Users/cobalt/cobalt diff --stat main` | OK |
| 3-G | same | `115:- A red anywhere → name each test and assertion, (f) and THE RELEASE if the lock is` | OK |
| 3-R | same | `91:## STEP-R — RESTARTS (L42): DERIVED BY THE TOOL, BEFORE ANY SUITE` | OK |
| 3-T | same | `82:## STEP-T — THE TREE (L54, L68): the heads of \`TIP\` merged into \`<BRANCH>\`, in orde`; FORWARD check at `85:- After the merges, each its own call, quoted: \`git -C /Users/cobalt/cobalt log --o…` (carries `grep -n -F "MIGRATIONS_DIR / \"00"` and `FORWARD`) | OK |
| 3-C | same | `88:## STEP-C — THE CONFIGS AND THE JOBS (read-only; rule C)` | OK |
| 3-O | same | `43:- A DEPLOY NEVER CONTINUES BY MESSAGE (his 2026-09-30 ruling, the deploy's version ` — contains `INSIDE THE OUTAGE (4.1 to the end of 4.6) the strict rule stays` | OK |
| 4 | `git -C /Users/cobalt/cobalt show 9694a679:"docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | exists. Exit-5/6 bullet at line 102: `5 → FAILED: gate — G (b) — cobalt_dev not at 0013 — <its read: lines> · rollback: not used; 6 → DECISION 0: cobalt_dev NOT back at 0013 — <its line> and the run ends FAILED`. Equal-tree clause at line 99: `…quote them from the check report with its path and skip (a)–(f); otherwise the gate runs whole. The clause applies only when the check's stop l…`. Launch line 11 flag text: `--append-system-prompt "ONE bare command per Bash call: … A call the hook blocks is NOT A REFUSAL: resend it as single calls."`. Note: the chain's text does not yet contain T2's "trap on every exit" ending (line 105 reads "the gate's trap runs (f) on every exit"); T2 writes it, as the card says | OK |
| 5a | `grep -n "^## DECISIONS"` in `reports/deploy-set2-1003.md` | `73:## DECISIONS` | OK |
| 5b | `ls` + `grep` findings in `reports/deploy-hub-other-house-read-2026-10-03.md` | file exists; findings 1 (line 9), 2 (12), 3 (15), 4 (18), 5 (21) | OK |
| 5c | `grep` items in `reports/adoption-hubs-decisions-2026-10-03.md` | file exists; items 5 (line 11), 6 (12), 7 (13) | OK |
| 6 | `git show main:src/cobalt/db_migrations/` | every `.sql` is `NNNN_*.sql` or `NNNN_*.rollback.sql` (0001–0022, 0012 absent); non-sql: `__init__.py`, `cli.py`, `placement.py`. No `dev_rebuild.py` on main (T1 names it as code; harmless) | OK |
| 7a | `grep -rn OPS_DESK_PREFIX /Users/cobalt/cobalt/src` | `src/cobalt/jobs/restarts.py:38:OPS_DESK_PREFIX = "ops/desk/"` and `:230` use (path is `jobs/restarts.py`) | OK |
| 7b | `ls /Users/cobalt/cobalt/configs/cobalt/jobs.yaml` | exists | OK |
| 8 | `grep -n "^| R47 \|^| R154 \|^| R157 "` in `cto-2026-10-02.md` | R47 (line 54), R154 (161), R157 (164): each `HIS RULING … HIS RULING · APPROVED` | OK |
| 9 | `grep -c -F "«FILL"` on the card | `0` | OK |

## ISSUES
None.

PREFLIGHT DONE · card: 02b · checks: 20 · fails: 0 · ready: YES
