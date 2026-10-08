# desk-ops-amend2 — report 2026-10-08

## §0 Headline
- Card `106-desk-ops-fixes-card.md` amended in place: G4 gains a second notify, `desk missing — relaunch with desk-launch.sh desk`.
- It fires when `desk-list.sh` shows no live `cto-desk` row. The day-open desk check (card `109`) is dropped.
- G1, G2, G3, G5 untouched. `BASE` is still the only fill token. No new seat command.
- Card 13290 → 16817 bytes. Not committed.

## CHANGES
- Header: `RULINGS` gains `2026-10-08 R662`, `2026-10-08 R664`.
- G4 title and text: the SECOND NOTIFY, placed after the rows read (`close-timer.sh:76`) and before the hub loop. Live row = non-empty id and name exactly `cto-desk`. Id-less rows count for nothing. An unreadable list sends it, then `refuse` as before.
- G4 tests: three new (`no cto-desk row` sends one; `live cto-desk row` sends none; `id-less rows` no crash, only real rows counted). `test_an_unreadable_session_list_is_refused` now asserts two notify lines. Count 15 → 18 in `test_close_timer.py`.
- `NOT IN THIS JOB`: the day-open line replaced, and a no-new-seat-command line added. Self-check (1), (2) and `RECORDS` extended.

## DECISIONS
- C9: card `109` dropped; the timer sends the desk-missing notify (R662, R664).
- C10: an unreadable list sends the desk-missing notify, then the REFUSED notify (two lines, exit 1).
- C11: the check runs on every fire, so a missing desk repeats hourly until relaunched. Once-a-night would need state.
- C8 reworded: it no longer points at a separate day-open card.

## RECORDS
- Read: card 106 (whole), `reports/desk-ops-amend-2026-10-08.md` (whole), the prompt 111.
- Read at main HEAD `e5c62696`: `ops/desk/close-timer.sh` (whole): `:42-45` refuse, `:75-76` list read, `:77-91` hub loop, `:81` name field. `tests/ops/test_close_timer.py` (whole): `:79` default rows `CTO`, `:60` `LOOKALIKE`, `:162` and `:170` the two refused tests.
- `grep -c '^def test_'` on `test_close_timer.py` → 15. `grep -c '«FILL'` on the card → 1 (BASE).
- `wc -c` on the card: before 13290, after 16817.
- Not read: `writing-rules.md` (the report follows the shape of the previous amend report).
- Nothing run: no test, no send, no key read.

DESK OPS CARD AMENDED 2 · decisions: 3
