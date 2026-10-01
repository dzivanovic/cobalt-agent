# F15 P1 check — decisions answered (2026-09-30)

Seat `f15-p1-check-judge` (Opus 5.5, read-only). Source: `reports/f15-p1-check-2026-09-30.md` `## DECISIONS` (:301-316), checked at tip `1d70cf72` on `f15/p1-records`.

## §0 Headline
- Both ASK DESK items are answered with the default the check already took: X5-with-records stays unrun, and the docs-excluded `diff.md` stands.
- Nothing goes to Dejan. Neither item touches scope, a date or money, and the design rulings (09-29 R145, R151) are not re-asked.

## ANSWERS
DECISION 1 — Keep X5's with-records half unrun; the card has already settled this, and the evidence already on file (W1's lock test, X12 (iii), X5 at BASE, O1–O3) covers what that run would show. — The card's `61-f15-p1-card.md:69` records this half as not run. The `0022` FK `card_id … REFERENCES "user".aset_sizings(id)` (`f15/p1-records:src/cobalt/db_migrations/0022_prediction_records.sql:37`) plus the `prediction_records_immutable` trigger (`:61-66`) mean a card with records cannot be deleted. Disabling the trigger is fenced (`61-f15-p1-card.md:43`), so running it would leave the stray card W (c3r) reports. `seq` under the lock is pinned by `test_write_record_takes_seq_and_transition_id_under_the_callers_lock` (`f15/p1-records:tests/cobalt/test_f15_p1_records_db.py:145`).
DECISION 2 — Accept `diff.md` as the hub defines it, with `":(exclude)docs"`; no re-copy is needed. — Per `git show --stat`, the two missing commits touch only docs: `32a910d5` is the build report and `28d9364f` is a one-line change each to `BUILD-HUB.md` and `DEPLOY-HUB.md`. Card row T1 (`61-f15-p1-card.md:34`) says those hub edits are "proven by W: (c) and (c3) run the edited commands byte for byte", not by a code diff.

F15 P1 CHECK DECISIONS ANSWERED · answered: 2 of 2 · for Dejan: 0
