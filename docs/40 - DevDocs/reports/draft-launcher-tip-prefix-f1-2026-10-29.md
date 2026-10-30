# draft-launcher-tip-prefix-f1 — 2026-10-29

## §0 Headline
- Card 1085 now has row `F1` after `A2`: `ops/desk/card-fill.sh:71` and `:74` take 8 hex plus optional further hex and write the first 8 to `TIP:`.
- The flipped card-386 pin (`tests/ops/test_card_fill.py:187` on the branch, `:179` on `main`) becomes a refused `…4dz` row, and a new test pins "a 9-hex SHADOW line fills the 8-hex prefix".
- The check's red test is the proof: `FIXED: O1 — tests/ops/test_card_fill.py::test_1085_check_o1_a_nine_hex_built_line_fills_the_eight_hex_tip`.
- Only card 1085 was edited. Nothing was run but reads, so every RED in F1 is UNPROVEN until the builder quotes it.

## DECISIONS
- ASK DESK: should the card's `## DEPLOY PROOF` get a marker for `card-fill.sh` (`grep -c -F "card 1085" /Users/cobalt/cobalt/ops/desk/card-fill.sh` · before `0` · after at least `1`)? [22:00 EDT] Default: not added; the brief said to edit only the one row, and the four existing markers stand.
- ASK DESK: the card has no `ORDER:` line, so F1 sits last in `## ROWS` and its text says it runs after A2. [22:00 EDT] Default: no `ORDER:` line added.
- No fence change: `## NOT IN THIS JOB` does not name `card-fill.sh`, so nothing was narrowed.

## RECORDS
- Read 22:0x EDT (`date` 21:59:11 and 22:00:05): the prompt `1095-draft-launcher-tip-prefix-f1.md`; card `1085-launcher-tip-prefix-card.md` whole; `prompts/CARD.md` whole; `prompts/BUILD-HUB.md:10-18` (the BUILD line); check report `launcher-tip-prefix-check-2026-10-29.md` whole (`## OWN FINDINGS`, `## RUNS` O1, `## FIXES`, `## OPEN`, `## DECISIONS`).
- Proved on the branch with `git -C /Users/cobalt/cobalt show` and `grep -n … ops/launcher-tip-prefix` (tip `5babf712`): `ops/desk/card-fill.sh:71`, `:74` (the two regexes), `:5` (the `<8 hex>` comment); `tests/ops/test_card_fill.py:105-117` (BUILT refused list), `:127` (O1 test), `:164` (`test_386_e1_…`), `:177-187` (the SHADOW refused list, the `1a2b3c4d5` row at `:187`). `:179` is the same pin on `main`. `desk-launch.sh`, `preflight.sh` and `BUILD-HUB.md` hold no `card-fill` reference.
- The first edit joined the A2 row and F1 on one line (`||`); read back and fixed. One range corrected (`:105-117`).
- The ledger line in the prompt for the launch (`desk-launch.sh prompt`) was not run. No git write, no test run.

DRAFTED · decisions: 2
