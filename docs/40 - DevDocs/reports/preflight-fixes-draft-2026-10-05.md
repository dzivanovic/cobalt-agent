# preflight-fixes draft — 2026-10-05

## §0 Headline
- Card written: two rows, F1 (self-check below 3 recorded) and F2 (PASS-2 head row), each derived from a quoted hub line.
- Files: `ops/desk/preflight.sh` and `tests/ops/test_preflight.py` only; DB: none; no new command or argument.
- Only `BASE` is a `«FILL»` (the desk's header value).

## CARD
`/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/20-preflight-fixes-card.md`

## DECISIONS
none

## RECORDS
- F1 derivation: `BUILD-HUB.md:97` ("`self-check: <k> of 3` in the stop line"), `CHECK-HUB.md:61` ("A lower self-check count is recorded and goes to the house as a fact"); script line `ops/desk/preflight.sh:204`.
- F2 derivation: `CHECK-HUB.md:120` (`<tip now>` = pass 1's `tip:`; the script's check `head` row at `preflight.sh:143-157` uses the card's `TIP`). The script learns the pass from the `CHECK REPORT` last line, since `CHECK-HUB.md:58` gives it no argument.
- The existing test `test_a_check_whose_report_is_short_of_three_self_checks_fails` (`tests/ops/test_preflight.py:213`) pins the old behaviour; the card rewrites it.
- The hub's added PASS-2 rows (the `tail -n 3` of `CHECK REPORT`, the house-B probe) are left out of the card as not mechanical rows of the script.
- No outside-house read; no git write; no launch.

PREFLIGHT FIXES DRAFTED · decisions: 0
