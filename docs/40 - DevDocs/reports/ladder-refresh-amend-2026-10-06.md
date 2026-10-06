## §0 Headline
- Card `prompts/2026-10-06/54-radar-ladder-refresh-card.md` amended by the desk's decisions 1-4.
- An expanded card no longer pauses the tick. Rule (2), its test, its mutation and the BEHAVIOUR NOTE are rewritten; a new test (2b) turns RED if the tick pauses on an expanded item.
- RESTARTS already read `com.cobalt.aset com.cobalt.radar` everywhere; no line changed.
- Decisions 3 and 4 are kept as drafted.

## CHANGES
Card `54-radar-ladder-refresh-card.md`:
- Row A rule (2), states list (line 18): removed `a .ladder-item.open (openIds() :1513, over items() :1510)`.
- Row A rule (2), after the no-`<select>` sentence (line 18): added that an EXPANDED card is not work in progress and never pauses the tick (`:1451`, `:1519`, `:1526`), and that `tickLadder` does not name `.ladder-item.open` or `openIds`.
- Row A test (2) (line 18): removed `.ladder-item.open (or openIds().length)` from the guard list; added that the body does not name them.
- Row A test (2b) (line 18), new: an expanded card does not pause the tick, and a new card still appears. MUTATION: add a `.ladder-item.open` guard to `tickLadder`; the test goes RED.
- Row A (line 18): `one per rule` is now `one per rule, plus (2b)`.
- `## RECORDS` BEHAVIOUR NOTE (line 44): the top 2 stay open across a tick because `keep` restores them; a new card appears collapsed. The old sentence that the tick waits until he closes them is gone.
- `## CHECK ASKS` X1 (line 36): removed `a card is open,`. It contradicted rule (2). This is the only edit outside the four named places.
- Unchanged: `BASE`, `TIP`, `CHECK REPORT`, `HOUSE B`. The only `«FILL` is `BASE`.

## DECISIONS
1. ASK DESK: X1 edit above sits outside the named places. Default: kept, since the old X1 would send the checker to fail a correct build. [16:55 EDT]

## RECORDS
- `git -C /Users/cobalt/cobalt rev-parse HEAD` → `f4c4b33a43a1c30f08aac16fea4567b2018e1bb0`.
- `git -C /Users/cobalt/cobalt diff --stat 542a8348 HEAD -- src tests` → no output, so every `file:line` the card cites for `src/` and `tests/` holds at HEAD.
- Read whole: the prompt `55`, card `54`, `reports/ladder-refresh-draft-2026-10-06.md`, `Memory/topics/writing-rules.md`.
- `src/cobalt/aset/radar_panel.py:1446`–`:1580` read at HEAD: `:1451` (top 2 open), `:1510`, `:1513` (`openIds`), `:1518`–`:1527` (`refreshLadder`, `keep` at `:1519`, `:1526`), `:1546` (dot toggle), `:1560`–`:1576` (`refreshPool`, `setInterval`). All match the card.
- `grep` of the card for `com.cobalt`: five hits, all in `## RECORDS` RESTARTS, all the two-job form.
- Nothing was run but reads. No git write, no launch.

LADDER REFRESH CARD AMENDED · decisions: 1
