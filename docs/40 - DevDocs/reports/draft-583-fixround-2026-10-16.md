# draft-583-fixround — fix-round rows FR-1 to FR-5 on card 583 (2026-10-16)

## §0 Headline
- Card `prompts/2026-10-15/583-band-routing-card.md` amended: `## FIX ROUND`, rows FR-1 to FR-5 (RED, edit, control each), `## ORDER`, `## WHY`, `## NOT IN THIS JOB`, `## CHECK ASKS` X8-X12, `## RECORDS`.
- G1 (PASS-2) barred and named as a follow-up. `RULINGS`, `BASE`, `TIP`, `RESTARTS: none` stand.
- Two ASK DESK items: an existing test pins CHECK-HUB `:64`/`:117` whole; FR-4 supersedes two B-row sentences.
- Every `file:line` read on the tip; nothing run, so every RED is UNPROVEN until the builder quotes it.

## DECISIONS
1. ASK DESK: `tests/ops/test_check_hub_shadow.py` pins both CHECK-HUB lines byte for byte (`L6_LINE` `:27-30`; `test_l6_…` `:73-79` asserts exactly two lines equal to it). FR-2's edit turns it red by design. Default taken: FR-2 changes that one constant `L6_LINE` to the new line and nothing else of the file; the card's ORDER permits only that diff in the nine suites. The other way: the brain adds the file to the round by his own row. [10:03]
2. ASK DESK: FR-4 changes the B2 `BAND ROUTING` sentence ("the fix round goes to the same builder") and contradicts B3's row text ("a routed card's fix round goes to its own original builder model") and the `## NOT IN THIS JOB` line that barred a fix round on any other model. Default taken: the brain's direction wins; `## FIX ROUND` states that an FR row beats a B row, the barred line is reworded, the built B3 text is left as written. [10:03]
3. ASK DESK: the brain's FR-2 RED reads "0 today, 1 after"; two lines (`:64`, `:117`) change, so the count of lines holding the clause is 0 then 2. Default taken: the row says `0` then `2`, the clause read by content. [10:03]
4. ASK DESK: FR-1's refusal text and `//` test. The direction gives the `/./` and `//` refusal and "the error names the path"; the wording `the card path holds '/./' or '//': <path>` and the extra `//` test are mine. Default taken: as drafted. [10:03]

## RECORDS
- Read 2026-10-16 10:03 EDT: the card whole; the check report `band-routing-check-2026-10-16.md` whole; the brain's `band-routing-check-decisions-2026-10-16.md` whole; precedent `prompts/2026-10-16/622-jev-shadow-fr1-card.md` (`## FIX ROUND`; `CARD.md` has no `FIX ROUND` text).
- Tip proved: `git -C /Users/cobalt/cobalt rev-parse ops/band-routing-1015` → `ee21824d…`. `git show` of the tip: `CARD.md` whole (`BAND` row `:23`, check cell `optional`), `SHADOW-HUB.md` whole (`:28`, `:53`, `:70`). Worktree `git status --short` → nothing, so `Read`/`Grep` of its files equal the tip: `desk-launch.sh` `:984-1001`, `:1635-1668`, `:1786-1815`; `CHECK-HUB.md` `:64`, `:117`, headings `:61`, `:115`; `test_band_routing_1015.py` `:372-383` (marker `:377-379`); `test_check_hub_shadow.py` `:1-90`; `preflight.sh` `:158-167` by grep.
- The allow line has no `git show` for files other than by the one form used; the worktree reads stand in for the large files (recorded, not a change of command).
- Edits: the card only, with Edit. No git write, no launch.

DRAFTED · decisions: 4
