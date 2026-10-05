## §0 Headline
Card 20 row F3's `red first` cell now names the test and the assertion, and says BASE, not main.
Confirmed at BASE `b56622fa`: `test_the_trees_brain_hub_line_is_printed_with_its_handover_filled` holds `assert INSTALL in text` at line 285.
One cell edited; nothing else touched.

## CARD
`prompts/2026-10-05/20-preflight-fixes-card.md` line 21, F3 `red first` cell: test `test_the_trees_brain_hub_line_is_printed_with_its_handover_filled`, assertion `assert INSTALL in text` (line 285): it fails on BASE `b56622fa`, because the hub title reads `installed 2026-10-05`, not the unfilled token.

## DECISIONS
None.

## RECORDS
- Read: the prompt 37, the card, the test file at BASE by `git show b56622fa:tests/ops/test_desk_launch_brain.py`, line 285 by `git grep -n`.
- I did not re-read the hub title at BASE; the prompt states it as `installed 2026-10-05`.
- No git write, no launch.

PREFLIGHT FIXES AMENDED 2 · decisions: 0
