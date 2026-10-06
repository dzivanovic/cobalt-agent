# next-flow deploy card 09 — preflight (2026-10-06, read-only)

Card: `prompts/2026-10-06/09-deploy-next-flow-card.md`

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `git -C /Users/cobalt/cobalt rev-parse --verify 987ab80d^{commit}` | `987ab80de88d8efc13bc02e378bcac6cfb517201` | OK |
| 1b | `git -C /Users/cobalt/cobalt log --oneline -1 ops/next-flow-1006` | `987ab80d fix(next-flow): one-pass wording at L36 line, COUNTING, ...` | OK |
| 1c | `tail -n 3` of `reports/next-flow-check-2026-10-06.md` | last line: `CHECK DONE · job: next-flow · pass: 1 · tip: 987ab80d · ... held unfixed: 0 · ... RESTARTS: none · ... ready: YES ...` | OK |
| 1d | `git log -1 --format=%h -- <check report>` | `e782ae9f` | OK |
| 2a | `rev-parse --verify deploy/deploy-next-flow-1006` | `fatal: Needed a single revision` (absent) | OK |
| 2b | `rev-parse --verify refs/tags/deploy-2026-10-06-next-flow` | `fatal: Needed a single revision` (absent) | OK |
| 2c | `ls /Users/cobalt/cobalt-wt/deploy-next-flow-1006` | `No such file or directory` | OK |
| 2d | `ls` of the card's REPORT `reports/deploy-deploy-next-flow-1006.md` and of this report path before writing | both `No such file or directory` | OK |
| 3a | `grep -n "^| R438 " reports/cto-2026-10-05.md` | line 173, ends `HIS RULING · APPROVED` | OK |
| 3b | `grep -n "^| R412 " reports/cto-2026-10-05.md` | line 109, text begins `HIS RULING:`, status `APPROVED (in cto-desk-contract.md ...)`; not APPLIED-only | OK |
| 3c | `git log -1 --format=%h -- cto-2026-10-05.md` / `git diff --stat -- same` | `1f4a8598` / empty (committed, clean) | OK |
| 4a | 12 marker commands on main, `before` values | CHECK-HUB: no-second-pass 0, start-both 0, `## PASS 2` 1, after-a-check 0, `<WORKTREE> all --deploy` 0, L36-two 0, L36-one 1, house-wrote 1, both-houses 0; BUILD-HUB: one-fix-round 0, `<WORKTREE> all --deploy` 0, `pass 1: whole (deploy)` 0. All equal the card's `before` | OK |
| 4b | the same 12 on the worktree `/Users/cobalt/cobalt-wt/next-flow-1006` (HEAD `987ab80d`, `git diff --stat 987ab80d` empty) | no-second-pass 1, start-both 1, `## PASS 2` 0, after-a-check 1, one-fix-round 1, `--deploy` CHECK 1, `--deploy` BUILD 1, `pass 1: whole` 1, L36-two 1, L36-one 0, house-wrote 0, both-houses 1. All equal the card's `after` (smoke reads are the same 5 greps; each ≥1) | OK |
| 4c | `git diff --stat main...987ab80d` | `BUILD-HUB.md` 12, `CHECK-HUB.md` 76, `reports/next-flow-build-2026-10-06.md` 140 added; 3 files | OK |
| 4d | SHIPS row vs diff; RESTARTS | row lists the same 3 files; all `docs/**`; check line 92: `BUILD-HUB.md M DOCS -`, `CHECK-HUB.md M DOCS -`, build report `A DOCS -`, `RESTARTS: none`. No `ops/desk/`, `tests/`, `src/` path | OK |
| 5a | `grep -c -F "«FILL"` on the card | `0` | OK |
| 5b | shape vs `CARD.md` and `41-deploy-hub-text-card.md` | headers JOB, LADDER, BRANCH, WORKTREE, BASE, TIP, REPORT, RULINGS, TAG, MIGRATIONS, SET all present in the deploy order; body `## SHIPS`, `## MARKERS`, `## SMOKE READS`, `## RECORDS`; no `## READ-BACK` (MIGRATIONS none); bare headings; no launch line | OK |
| 6a | `git diff --stat -- <card>` | empty | OK |
| 6b | `git log -1 --format=%h -- <card>` | `38815999` | OK |

Checks: 20 rows.

Method notes (not fails):
- `git show 987ab80d:<path>` cannot be piped to grep under the one-bare-command rule. The `after` counts were read from the worktree at HEAD `987ab80d` with a clean diff against it, which is the same content. The deploy hub re-proves them with `git show`.
- `CARD.md` has no word "RESTARTS" (the K10 home is not in it). The class home used is the check report's RESTARTS table (line 92).
- R412's status cell does not repeat `HIS RULING`; that phrase opens the row's text. It passes the L7a literal read; the desk may re-read it.

## ISSUES
none

PREFLIGHT DONE · card: next-flow-deploy-09 · checks: 20 · fails: 0 · ready: YES
