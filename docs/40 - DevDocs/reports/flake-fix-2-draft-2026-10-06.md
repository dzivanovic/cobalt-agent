# flake-fix-2 draft, 2026-10-06

## §0 Headline
- Card `flake-fix-2` drafted: one row, one shared helper `open_migrated(apply, paths)` in `tests/cobalt/migration_retry.py`, 10 callers named by file.
- BASE `71f69821`; red: `test_radar_score_migration.py:420` raises `DeadlockDetected` with a monkeypatched first deadlock.
- No new command needed; test-side only.

## CARD
`/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/14-flake-fix-2-card.md`

## DECISIONS
None. (decisions: 0)

## RECORDS
- BASE: `git -C /Users/cobalt/cobalt rev-parse HEAD` = `71f6982158ec3413b21faa16ccf4f025dfbe5bf6`.
- `git show 433e1c7e --stat`: a merge adding only the deploy report; the shipped fixture code is read from the tree at BASE, `tests/cobalt/test_drc_store.py:231-264` (loop at 237-252, already hardened: close even when rollback raises), retry tests at 349-481.
- Caller grep (Grep tool, `_apply\(conn, FORWARD\)|_migration_conn\(\)|connect_migration`, `tests/`): hits read in context at `test_radar_score_migration.py:296-310, 410-430`; `radar_migrated_support.py:60-96`; `test_p4_migrations.py:300-310, 440-490, 544-554`; `test_voice_store.py:163-210`; `test_archiver_migrations.py:444-456`; `test_stale_score_db.py:132-184`; `test_tenancy.py:330-358, 542-582`; `test_radar_handicap_store.py:140-180`; `test_xl76_membership_harness.py:106-160`; `test_drc_d2_fix_r1_db.py:100-128` (uses the `migrated` fixture, not its own connection); `test_db_only_selection.py:450-520` (`connect_migration` is text in a string, not a caller).
- Broader `_apply(` grep over `tests/`: every other hit takes the `migrated` or `migrated_radar` fixture's connection.
- `test_tenancy.py:311` `_python_files` reads `SRC` only (`:59`): the one-caller lint is not touched by a `tests/` helper.
- `tests/cobalt/__init__.py` absent: a bare-name import works as for `radar_migrated_support`.
- `git status --short -- tests` and the three CTO reports: empty (clean).
- Rulings: `grep -n "^| R326 "` → `cto-2026-10-03.md:332` (HIS RULING · APPROVED); `^| R412 ` → `cto-2026-10-05.md:109` (HIS RULING, APPROVED); `^| R474 ` → `cto-2026-10-05.md:140` (HIS RULING · APPROVED); `^| R501 ` → `cto-2026-10-06.md:19` (DESK RECORD). All files tracked.
- Only the card's header values the desk fills: `TIP`, `CHECK REPORT`, `HOUSE B` left empty per CARD.md; no `«FILL` token.
- Note for the desk: the `xl76` harness (tests/experiments) is included as a caller because the grep hits it; the card keeps its `apply_ms` timer.
- Nothing run (no tests, no git write).

FLAKE FIX 2 DRAFTED · decisions: 0
