# flake-fix card preflight, round 2 (2026-10-06)

Card: `prompts/2026-10-06/02-flake-fix-card.md` at `356b4646` (main HEAD). BASE `d1adf256`.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | Read card lines 14 and 24 | L14: "...not a second writer (`reports/second-writer-survey-2026-10-05.md` lines 5, 35-38; the survey ran under R326, and the brain's judgment of it is R479, a desk record)". L24: "Disabling autovacuum or any server setting (the server may also host production; the brain's judgment (R479, a desk record) puts the fix test-side: a retry in the migration fixture)". Neither attributes the autovacuum finding or a rejection to R326. | OK |
| 1b | Read survey lines 5, 35-38 | L5: "every blocker is a Postgres **autovacuum worker** ... not a client". L35-38: K3-1, K3-2, D5-1, D5-2, each `blocker = autovacuum: VACUUM <table>`. Matches the card (four runs, autovacuum blocker, no second writer). | OK |
| 1c | `grep -n "^| R479 " reports/cto-2026-10-05.md` | `135:\| R479 \| 10-05 23:32 ET \| DESK RECORD (brain): second-writer survey DONE: no second writer; the 4 deadlocks are autovacuum vs migration DDL. Fix = test-side retry on DeadlockDetected (max 2) in the migration fixture, own card by a drafter after P2; hub removed. \| DESK RECORD \|` The card says R479 is the brain's judgment, a desk record, with the fix test-side as a retry in the migration fixture. It holds that and claims no more (the card does not call it a ruling and does not list it in RULINGS). | OK |
| 1d | Read `reports/cto-2026-10-03.md:330-333` | `332: \| R326 \| 10-05 06:19 ET \| HIS RULING: A on all three ... second-writer survey gets its 5 read strings, this seat only; ... \| HIS RULING · APPROVED \|`. The card cites R326 only as the ruling the survey ran under (L14), plus the unchanged LADDER/RULINGS header lines that round 1 passed (1d, 2a). R326 is not cited for autovacuum or a rejection. R326 does not say the flake card waits on it, and the card does not claim that. | OK |
| 1e | all of 1a-1d | The round-1 issue 3h is answered. | OK |
| 2a | `git log --oneline -3 -- <card>` then `git diff e849653f 356b4646 -- <card>` | The log shows `356b4646` and `e849653f`. The diff has exactly two hunks, line 14 and line 24, both reworded sentences. No other line changed. | OK |
| 2b | header, Read card lines 1-10 | `BASE: d1adf256`, which is an ancestor of main (`git rev-parse d1adf256` = `d1adf256102cbab1...`). `BRANCH: ops/flake-fix-1006`, `WORKTREE: flake-fix-1006`, `TIP:` empty, `CHECK REPORT:` empty, `HOUSE B:` empty. | OK |
| 2c | `grep -n "^| R412 " reports/cto-2026-10-05.md` | `109:\| R412 \| 10-05 13:16 ET \| HIS RULING: drop pre-merge (d2) from DEPLOY-HUB ... \| APPROVED (in cto-desk-contract.md ...) \|`. R326 (2a above) is `HIS RULING · APPROVED`. Both files are committed (`git log` names `59981ca7`, `4c58a879` for the 10-05 file; the 10-03 file was in `b1337431` in round 1; neither is in git status). RULINGS is `2026-10-03 R326, 2026-10-05 R412`. | OK |
| 2d | `grep -n -E "def migrated\|connect_migration\|autocommit = False\|_apply\(conn, FORWARD\)\|conn.close\(\)" tests/cobalt/test_drc_store.py` | `232:def migrated`, `233: db.connect_migration`, `234: autocommit = False`, `237: _apply(conn, FORWARD)`, `249: conn.close()`; the decorator is 231. The range 231-249 holds. | OK |
| 2e | Read `src/cobalt/db_migrations/cli.py` at BASE, lines 631-642 | `631: def _apply(conn, paths) -> None:` through `642: conn.execute(path.read_text())`. Cite holds. | OK |
| 2f | `git diff --stat d1adf256 HEAD -- tests/cobalt/test_drc_store.py src/cobalt/db_migrations/cli.py` | empty: neither file changed since BASE, so the working-tree reads equal BASE. | OK |
| 2g | files list | The only file in the row is `tests/cobalt/test_drc_store.py`. `conftest.py` and `src/` are in NOT IN THIS JOB. | OK |
| 2h | no new command (R411, R412) | Line 26: "A new command, script or `ops/desk/` change: the build seat uses only its allow line (R412)". The card adds no command. | OK |
| 2i | `grep -c -F "«FILL" <card>` | `0` | OK |
| 3a | `git diff --stat -- <card>` | empty (clean) | OK |
| 3b | `git log -1 --format=%h -- <card>` | `356b4646` (non-empty, committed on main) | OK |

## ISSUES
None.

Notes, not fails: row 332 of the 10-03 file carries 10-05 timestamps (the file name does not match the row date). The card says `2026-10-03 R326`, which matches the file. This is unchanged from round 1.

PREFLIGHT DONE · card: flake-fix-02-r2 · checks: 16 · fails: 0 · ready: YES
