# Set 3b deploy card — preflight (2026-10-04)

Card: `prompts/2026-10-04/07-deploy-set3b-card.md`. Read-only. Where a command needed a pipe or a count, I ran the count in the row's own worktree (`/Users/cobalt/cobalt-wt/<job>`), after `git -C <wt> rev-parse --short=8 HEAD` returned the row's head (all five matched).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `rev-parse --short=8` on each branch | `ops/adoption-port-1003` → `15ba4b75` · `ops/dev-rebuild-port-1003` → `0452dc99` · `ops/desk-tools-port-1003` → `525b5ae1` · `ops/close-timer-1003` → `47a689a1` · `ops/cobalt-guard-1004` → `a2e19ceb`. All five equal the card's TIP and `## SHIPS`. | OK |
| 1a | `tail -n 1` of each check report | each ends `tip: <code tip>`, `held unfixed: 0`, `ready: YES`: 685b88d6 · 396edb5a · 5c1d629f · 47a689a1 · a2e19ceb. All equal the card's code tips. | OK |
| 1b | `merge-base --is-ancestor <code tip> <head>` ×3 (rows 1–3; rows 4–5 tip = head) | `685b88d6`→`15ba4b75`, `396edb5a`→`0452dc99`, `5c1d629f`→`525b5ae1`: all exit 0 | OK |
| 2 | `merge-base --is-ancestor 5ff16b1f <head>` for rows 1, 2, 3 | all exit 0 (row 1 `15ba4b75`, row 2 `0452dc99`, row 3 `525b5ae1`). Row 1 contains it, so it is an ancestor of row 1's head. | OK |
| 2a | `merge-base --is-ancestor a8d8a848 main` · `… a8d8a848 a2e19ceb` | both exit 0: `a8d8a848` IS an ancestor of main, and of row 5's head. (`5ff16b1f` is NOT an ancestor of main, exit 1: expected, row 1 brings it.) | OK |
| 3 | `diff --stat main...<head> -- src/cobalt/db_migrations` ×5 | row 1: `cli.py` (+114/−1) · row 2: `cli.py` (350), `dev_rebuild.py` (879, new) · row 3: `cli.py` (+114/−1; the `5ff16b1f` change) · row 4: nothing · row 5: nothing. No `.sql` file in any range. `MIGRATIONS: none` holds. | OK |
| 4a | `grep -c -F "window (v) does not hold" …/DEPLOY-HUB.md` on main | before `0` ✔. After, row 1 head `15ba4b75`: `2` ✔ | OK |
| 4b | `ls …/db_migrations/dev_rebuild.py` on main | before `No such file or directory` ✔. After, row 2 head `0452dc99`: file listed ✔ | OK |
| 4c | `grep -c -F "claude-fable-5-1" ops/desk/desk-launch.sh` on main | before `0` ✔. After, last carrying head row 3 `525b5ae1`: `2` ✔ (row 5 head shows `0`, since it is based on `a8d8a848`, which is on main; the trial merge in order was clean, so the final result is 2) | OK |
| 4d | `ls ops/desk/close-timer.sh` on main | before `No such file or directory` ✔. After, row 4 head `47a689a1`: listed ✔ (`git show 47a689a1:ops/desk/close-timer.sh` prints the script) | OK |
| 4e | `grep -c -F "route: production is the deploy hub" ops/desk/bare-guard.py` on main | before `0` ✔. After, row 5 head `a2e19ceb`: `1` ✔ | OK |
| 4f | `diff --stat main...<head> -- DEPLOY-HUB.md` rows 2–5 | rows 2, 3: `22 insertions, 26 deletions` each, the same as `5ff16b1f`'s change (and `diff --stat 5ff16b1f <head>` on the file is empty for both). Rows 4, 5: empty. Rows 2–5 change nothing in that file beyond `5ff16b1f`. | OK |
| 5 | smoke reads at each row's head (worktree) | `grep -c -F "def test_" tests/ops/test_hub_lines.py` @ `15ba4b75` → `8` · `… tests/cobalt/test_dev_rebuild_cli.py` @ `0452dc99` → `18` · `ls ops/desk/stop-guard.py ops/desk/idle-wake.py` @ `525b5ae1` → both listed · `ls ops/desk/com.cobalt.close-timer.plist` @ `47a689a1` → listed · `grep -c -F "route: a fixed file changes by a card row" ops/desk/bare-guard.py` @ `a2e19ceb` → `1`. All five commands use absolute paths and no `%`. | OK |
| 6 | `grep -c -x -F "<card stop line>" <report>` ×5 | each returns `1`: the card's quoted line equals a whole line of its report, and `tail -n 1` of each report is that same line | OK |
| 7 | `grep -n "^| R157 "` (cto-2026-10-02.md) · `R216` · `R230` (cto-2026-10-03.md) | R157 line 164 `HIS RULING (B) … HIS RULING · APPROVED` · R216 line 222 `HIS RULING … HIS RULING · APPROVED` · R230 line 236 `HIS RULING … HIS RULING · APPROVED`. All three carry both. | OK |
| 8 | set 3 failure and the `11b` fix | `deploy-set3-1004.md` `## DECISIONS` 1: red is the shared seam between dev-rebuild-port's `tests/cobalt/conftest.py` session-start connect and lock-relief's `test_db_only_selection.py`. At `0452dc99`: `conftest.py:157 if os.getenv("PYTEST_CURRENT_TEST"):` (docstring `:155`) and `test_dev_rebuild_cli.py:425 monkeypatch.delenv("PYTEST_CURRENT_TEST")`. `396edb5a` is `fix(dev-rebuild-port): the nested-session seam … (P4, P4b; L72)`. Card `11b` rows P4, P4b ask for exactly those two lines. Check report r2 O2 finds P4's lines in the diff, and line 106 reads `pass 1 without --db-only (P4) 4461 passed, 7 skipped, 67 deselected, 3 xfailed`. | OK |
| 9 | `diff --stat main...a2e19ceb` | `reports/cobalt-guard-build-2026-10-04.md` (313) · `ops/desk/bare-guard.py` (664) · `tests/ops/test_bare_guard.py` (847) · 3 files. No `src/` or `configs/` file. | OK |

## ISSUES

None: no FAIL.

Noted, not a FAIL: row 5's check stop line carries `open: 2 · decisions: 3 · for Dejan: 1`, and `house B: none available`. The card's gate for it is `held unfixed: 0` and `ready: YES`, which hold. The desk may want to read that `for Dejan: 1` before launch. R216's text says `10` follows in its own deploy; R230 (later) overrides that and puts it in this set.

PREFLIGHT DONE · card: set3b-1004 · checks: 9 · fails: 0 · ready: YES
