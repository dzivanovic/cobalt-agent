# guard-g2 deploy card — preflight (read-only)

Card `prompts/2026-10-06/34-deploy-guard-g2-card.md`, job `guard-g2`, branch `ops/guard-g2-1006`, tip `19f75dc6`.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt rev-parse --verify 19f75dc6^{commit}` | `19f75dc6f0850d649c563b1dc8dae40e50e2d01f` | OK |
| 2 | `git -C /Users/cobalt/cobalt log --oneline -1 ops/guard-g2-1006` | `19f75dc6 fix(guard-g2): G2 reads the words bash runs; R1 stamps only an APPROVED production-read row ...` | OK |
| 3 | `git merge-base --is-ancestor 19f75dc6 ops/guard-g2-1006` | exit 0, no output | OK |
| 4 | `tail -n 3 reports/guard-g2-check-2026-10-06.md` | `CHECK DONE · job: guard-g2 · pass: 1 · tip: 19f75dc6 · ... held unfixed: 0 ... RESTARTS: none ... ready: YES ...` (pass 1, tip, held unfixed 0, ready YES all present) | OK |
| 5 | `git -C /Users/cobalt/cobalt log -1 --format=%h -- reports/guard-g2-check-2026-10-06.md` (also with `--all`) | empty both times; `ls` shows the file exists, so it is on disk but not committed | FAIL |
| 6 | `rev-parse --verify deploy/deploy-guard-g2-1006` (BRANCH) | `fatal: Needed a single revision` (absent) | OK |
| 7 | `rev-parse --verify deploy-2026-10-06-guard-g2` (TAG) | `fatal: Needed a single revision` (absent) | OK |
| 8 | `ls /Users/cobalt/cobalt-wt/deploy-guard-g2-1006` (WORKTREE) | `No such file or directory` | OK |
| 9 | `ls reports/deploy-deploy-guard-g2-1006.md` (REPORT) | `No such file or directory` | OK |
| 10 | `grep -n "^| R511 " reports/cto-2026-10-06.md` | line 40: `HIS RULING: add the G2 row ...` · `APPROVED — pending fold` | OK |
| 11 | `grep -n "^| R412 " reports/cto-2026-10-05.md` | line 109: `HIS RULING: drop pre-merge (d2) ...` · `APPROVED (in cto-desk-contract.md, ...)` | OK |
| 12 | `grep -n "^| R474 " reports/cto-2026-10-05.md` | line 140: `HIS RULING · APPROVED: ...` · `HIS RULING · APPROVED` | OK |
| 13 | `git log -1 --format=%h -- reports/cto-2026-10-06.md`, `... cto-2026-10-05.md`, and `git diff --stat` of both | `6392d540`, `1f4a8598`, diff empty (committed, clean) | OK |
| 14 | `git diff --stat main...ops/guard-g2-1006` | 5 files, 624 insertions, 3 deletions: guard-g2-build report, `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `tests/ops/test_bare_guard.py`, `tests/ops/test_desk_launch_prechecks.py`; the SHIPS row lists exactly these five, same totals | OK |
| 15 | BEFORE (main) `grep -c -F "def marked_read(command, s)" ops/desk/bare-guard.py` | `0` (card: 0) | OK |
| 16 | BEFORE `grep -c -F "MARKER = re.compile" ops/desk/bare-guard.py` | `0` (card: 0) | OK |
| 17 | BEFORE `grep -c -F "and not marked_read(command, s)" ops/desk/bare-guard.py` | `0` (card: 0) | OK |
| 18 | BEFORE `grep -c -F "PROD-READ:" ops/desk/desk-launch.sh` | `0` (card: 0) | OK |
| 19 | BEFORE `grep -c -F "production reads?([^[:alpha:]]|\$)" ops/desk/desk-launch.sh` | `0` (card: 0) | OK |
| 20 | BEFORE `grep -c -F "MARKED_KINDS" tests/ops/test_bare_guard.py` | `0` (card: 0) | OK |
| 21 | BEFORE `grep -c -F "def test_g2_a_marked_seat_is_denied_a_production_word_in_a_brace_word" tests/ops/test_bare_guard.py` | `0` (card: 0) | OK |
| 22 | BEFORE `grep -c -F "def test_r1_a_disapproved_row_stamps_nothing" tests/ops/test_desk_launch_prechecks.py` | `0` (card: 0) | OK |
| 23 | AFTER: `git -C /Users/cobalt/cobalt-wt/guard-g2-1006 rev-parse HEAD`, then the same 8 greps in that worktree (`git show` cannot be counted without a pipe) | HEAD `19f75dc6f085...`; counts `1`, `1`, `1`, `8`, `1`, `3`, `1`, `1` = card's 1, 1, 1, 8, 1, 3, 1, 1. Smoke reads are the same greps and are all 1 or more | OK |
| 24 | `grep -c -F "«FILL" 34-deploy-guard-g2-card.md` | `0` | OK |
| 25 | `git log -1 --format=%h -- 34-deploy-guard-g2-card.md`; `git diff --stat -- <card>` | `2913612a`; diff empty (committed, clean) | OK |
| 26 | `ls -l /Users/cobalt/.claude/ops/` | `desk-launch.sh -> /Users/cobalt/cobalt/ops/desk/desk-launch.sh`, `bare-guard.py -> /Users/cobalt/cobalt/ops/desk/bare-guard.py` (both symlinks into the repo) | OK |
| 27 | `grep -n OPS_DESK_PREFIX src/cobalt/jobs/restarts.py`; restarts.py lines 225, 245 | `ops/desk/` → operator-script class (line 230), `docs/` → DOCS (225), `tests/` → test class (245); all five shipped paths have a RESTARTS class home | OK |

## ISSUES
- Check 5 FAIL: `reports/guard-g2-check-2026-10-06.md` is not committed (empty `git log`, also with `--all`); the card cites it as the check report. Commit it on main before the deploy.

PREFLIGHT DONE · card: deploy-guard-g2-34 · checks: 27 · fails: 1 · ready: NO
