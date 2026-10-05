# launcher-fixround deploy card 47 — amend after preflight, 2026-10-05

## §0 Headline
- Card 47 amended in place for the three preflight fails (5, 6a, 7b); no other change.
- `## SHIPS` now has main's six columns; the fix-round note is one line in `## RECORDS`.
- Base `DEPLOY-HUB.md` lines corrected to `26, 50, 57, 74, 93, 101, 134, 178, 181` (matches the diff).
- OWED bullet is on its own line. `grep -c -F "«FILL"` → 0.

## DECISIONS
None.

## RECORDS
- FAIL 5: seventh column `fix report` removed from header, separator and data row; main's header read with `git show main:"docs/40 - DevDocs/prompts/CARD.md"` (six columns). The card held no `fix report` EMPTY DECISION wording to remove (grep: only the header and the two deploy-card.sh marker lines matched; those name the script's string, not the card's column, and stay). Added to `## RECORDS`: the fix-round column is added by this deploy; the row needs none because the check's `tip:` equals the code tip `a545a4d8`.
- FAIL 6a: `git -C /Users/cobalt/cobalt diff -U0 5fb0ddf5 main -- DEPLOY-HUB.md` hunks: 26, 50, 57, 74, 93, 101, 134, 178, 181; the card's `100` and `176-177` corrected. No-conflict conclusion unchanged.
- FAIL 7b: `…without a conflict.- OWED, …` split onto separate lines.

LAUNCHER-FIXROUND DEPLOY CARD AMENDED · decisions: 0
