# Flake-fix card amend 2026-10-06

## §0 Headline
- Preflight 3h fixed: two wrong attributions in `02-flake-fix-card.md` reworded (WHY line 14, out-of-scope line 24).
- The finding is now sourced to `reports/second-writer-survey-2026-10-05.md` lines 5, 35-38; the judgment to R479, named a desk record.
- R326 is kept only as the ruling under which the survey ran. `RULINGS` and LADDER unchanged; R479 not added.
- `git diff` of the card shows only those two lines; no `«FILL` token in the card.

## DECISIONS
- Line 24 says the brain's judgment (R479) "puts the fix test-side: a retry in the migration fixture", not "rejected disabling autovacuum". R479's row holds the retry fix and nothing about rejecting autovacuum-disable or editing migrations 0002/0007, so the card claims no more than the row.
- R479 not added to `RULINGS`: it is a DESK RECORD, not `HIS RULING · APPROVED`.
- Survey lines 5 and 35-38 read before citing; line 5 and the table rows K3-1, K3-2, D5-1, D5-2 name autovacuum workers as blockers.

## RECORDS
Old, line 14: "(`reports/second-writer-survey-2026-10-05.md` lines 5, 35-38, judged by the brain, R326)"
New, line 14: "(`reports/second-writer-survey-2026-10-05.md` lines 5, 35-38; the survey ran under R326, and the brain's judgment of it is R479, a desk record)"

Old, line 24: "(the server may also host production; his R326 rejected it)"
New, line 24: "(the server may also host production; the brain's judgment (R479, a desk record) puts the fix test-side: a retry in the migration fixture)"

R326 row (`reports/cto-2026-10-03.md:332`): "| R326 | 10-05 06:19 ET | HIS RULING: A on all three — D5 ships at `c96b5118` with O1 pinned (follow-up card: items' store + B2 wording); second-writer survey gets its 5 read strings, this seat only; F15 P2 X11 → follow-up card. Words: `cto-2026-10-05-words.md` R326–R327. | HIS RULING · APPROVED |"
- It holds: the second-writer survey is run (5 read strings, this seat only). It does not say the flake card waits on the survey findings, and holds nothing on autovacuum.

R479 row (`reports/cto-2026-10-05.md:135`): "| R479 | 10-05 23:32 ET | DESK RECORD (brain): second-writer survey DONE: no second writer; the 4 deadlocks are autovacuum vs migration DDL. Fix = test-side retry on DeadlockDetected (max 2) in the migration fixture, own card by a drafter after P2; hub removed. | DESK RECORD |"

Survey lines cited: 5 "The four deadlocks have no second writer: every blocker is a Postgres **autovacuum worker** (`autovacuum: VACUUM <table>`), a server-side process, not a client."; lines 35-38 are the K3-1, K3-2, D5-1, D5-2 rows, each `blocker = autovacuum: VACUUM <table> · other process (Postgres autovacuum)`.

FLAKE FIX AMENDED · decisions: 3
