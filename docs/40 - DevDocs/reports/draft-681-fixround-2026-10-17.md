## §0 Headline
- Card 681 gains row FR-1 and a `CONTINUE FIX ROUND` section: finding O1 (`stage-set.sh:134`, the legacy `HOUSE A:` filter, pinned by no test).
- The fix is one appended test, the check's `test_o1_legacy_a_higher_numbered_build_copy_is_not_the_prior_card` verbatim; green on the tip, red with `:134` removed; no source change.
- No row for A1 or `_two_card_copies`. Only the card was edited.

## DECISIONS
1. ASK DESK: the proof of `:134` is a grep of the worktree `cobalt-wt/check-scratch-fr1` (HEAD `5f42c4f3`; code equals `b093f192`) plus a whole `git show` read; `git show … | sed -n` was refused by the pipe guard. Default taken: the card cites `:134` as the check did. [11:20]

## RECORDS
- Edited: `docs/40 - DevDocs/prompts/2026-10-16/681-check-scratch-fr1-card.md` (section `## CONTINUE FIX ROUND` before `## ROWS`; row FR-1 and `FIX ROUND ORDER` after R2). Shape from card 671 FR-1 and its section.
- `git -C /Users/cobalt/cobalt show ops/check-scratch-fr1:ops/desk/stage-set.sh` read whole: the `grep -q '^HOUSE A:' || continue` line sits in the legacy loop; `grep -n "HOUSE A:"` on the worktree file → `134`. Test helpers by `grep -n` on the worktree test file: `CHECK_A :189`, `prior_staging :193`, `fr_card :344`, `build_card_copy :442`, the last test `test_mk2_control_a_marker_that_is_a_link_is_refused :651`.
- Test text taken from the check report `## OWN FINDINGS`. Nothing was run; the green and the red are the builder's to quote (L70).
- Time: `date` 11:16 EDT. No git write, no launch.

DRAFTED · decisions: 1
