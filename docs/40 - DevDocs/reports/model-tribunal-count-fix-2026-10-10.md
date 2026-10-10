# Model tribunal count fix, 2026-10-10

## §0 Headline
Item count 19 → 18 in `270`, `271`, `272` (S1–S9 + Q1–Q8 + S11, preflight F2).
Edited by the Edit tool only; no other text changed.
17 lines changed: 270 = 11, 271 = 4, 272 = 2. No `01-QUESTIONS.md` file is named for writing, so nothing to correct there.
No split was derived from the 19 (the `7` in "18 for 7" is 258's count).

## DECISIONS
1. "item count 19 for 7" → "18 for 7": the 7 is the item count of 258 (F4 tribunal), not computed from the 19, so only 19 changed.
2. `NINETEEN`/`nineteen` → `EIGHTEEN`/`eighteen`, `k of 19` → `k of 18` (all three spellings in 270), "S11 = 19 items", "(19 items)", "(19 items each)", "summing to 19" (271 stop line) → 18.

## RECORDS
Hits left of `grep -n -i -E "19|nineteen"` (none is the count):
- 270 line 15: `19,850 B`, a file size. Other 270 hits: R919 / R19 row ids and `19` inside dates and times.
- 271 line 1: `19:34 ET`, a time. Other 271 hits: R919 ids.
- 272 line 1: `19:34 ET`, a time. Other 272 hits: R919 ids.

`grep -c -i -E "18|eighteen"` (lines): 270 = 16, 271 = 5, 272 = 2.
Note: the grep for "18" also matches non-count text, so these are upper bounds on the count lines.

COUNT FIXED · places: 17 · decisions: 2
