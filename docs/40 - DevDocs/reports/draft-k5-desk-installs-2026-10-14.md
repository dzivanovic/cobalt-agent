# draft-k5-desk-installs — 2026-10-14

## §0 Headline
- Card `prompts/2026-10-14/549-desk-installs-card.md` drafted: K5, `desk-installs-1014`, 2 rows plus one run row (I1, I2, R3).
- One string added: `"SendMessage"` on the desk line `CTO-DESK-WAKEUP.md:13`; source of truth a new `STANDING-LIST.md` §4 row (after `:166`). Survey row 1 names no sibling.
- Row I1 turns `tests/ops/test_desk_refresh_wakeup.py::test_w1_the_launch_line_is_unchanged` red (whole-line pin to `f7d71571`); the card repairs it by deleting that test.
- Nothing run: reads only, on `main` HEAD `0ffb6949`.

## DECISIONS
- ASK DESK: Survey row 1 says "`SendMessage` and its siblings" but names no sibling string (row 1 and the row it names, §8 of the list, hold only `SendMessage`). Any other desk string is not added (R411, R412). Default: none added. [07:36]
- ASK DESK: `STANDING-LIST.md:14` and `:172` still say the desk line has "no allow" NEW strings; the new §4 row makes that stale. Default: the card leaves both lines unedited. [07:36]
- ASK DESK: cards 546, 547 and 548 were not in `prompts/2026-10-14/` at the read (`ls` ended at 545), so overlap with them is unproven. The three files this card touches are not in 521, 523 or 537. Default: the desk checks their ranges before the launch. [07:36]
- ASK DESK: the repair of the card-458 pin deletes `test_w1_the_launch_line_is_unchanged`, `BASE` and `import subprocess` in `tests/ops/test_desk_refresh_wakeup.py` (R1472 direction a). Default: delete, as the card says. [07:36]

## RECORDS
- Date 2026-10-14 07:36 (the machine's `date`); `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `0ffb6949`.
- Read on `git grep … HEAD`: `CTO-DESK-WAKEUP.md:13` (desk `- LAUNCH` line, allow list ends `"Bash(git -C * merge-base*)" --disallowedTools`), `:12` and `:16` (the only `SendMessage` hits); `STANDING-LIST.md:159`, `:168`, `:171`, `:225`, `:229`; `desk-launch.sh:544-563` (kind `desk`), `:866`, `:914`.
- `git diff --stat HEAD` on the wake-up, the list and `desk-launch.sh`: nothing (only `.claude/settings.json` is modified in the tree, survey row 2, kept out of the card).
- Law read: `LAWS.md` `### L81` (K1-K5; K5 = allow strings by card); survey `reports/survey-blockers-2026-10-12.md:13` (row 1); R1471 at `reports/cto-2026-10-14.md:8`.
- Pins found: `tests/ops/test_desk_refresh_wakeup.py:15`, `:76-83` (turns red). `tests/ops/test_hub_lines.py:151-155` holds the flag only; `test_desk_launch_brain.py:497-501` and `test_prodwrite_hub.py:153-157` read other sections of the list.
- Not read: `prompts/2026-10-13/516-sweep-pin-card.md` (the shape came from 523 and `CARD.md`).

DRAFTED · decisions: 4
