## §0 Headline
Card 21 amended with the brain's four answers; edits by Edit on the card only.
Row F1 now keeps the header test, adds the empty 7th cell at `deploy-card.sh:141` with a test on a written row, and adds `CARD.md` (line 44 only) to its files.
`## NOT IN THIS JOB` names exactly the changed lines; `## CHECK ASKS` gains X5.
Real line numbers re-read and matched: `desk-launch.sh` 714, 746-748; `deploy-card.sh` 141, 207; `CARD.md` 44.
One open point: the `CARD.md` separator line 45 (see DECISIONS).

## CARD
File: `prompts/2026-10-02/21-launcher-checks-card.md`
- F1 `what`: after the `deploy-card.sh` header sentence (lines 207-208), added "line 141 (the written row) gains the empty 7th cell … so written rows match the header", and "In `CARD.md` ONLY the `## SHIPS` header at line 44 gains `fix report` as its last column: one line, nothing else in `CARD.md`".
- F1 `red first`: the header assertion is kept (it stops the script and the launcher drifting apart); added a test that reads a written SHIPS row and asserts the empty 7th cell, so the row has as many cells as the header.
- F1 `files`: added `docs/40 - DevDocs/prompts/CARD.md` (line 44 only).
- `## NOT IN THIS JOB`: first two lines rewritten. They now name `desk-launch.sh` line 714 (new `frep=` after it) and 746-748, `deploy-card.sh` line 141 (and the header lines 207-208 of F1), `CARD.md` line 44, and each file's test. The hubs and `CARD.md` beyond line 44 stay out.
- `## CHECK ASKS`: added `X5 card 21 F1: optional fix report SHIPS column; header asserted; deploy-card.sh:141 writes the empty cell; CARD.md:44 header only.`

## DECISIONS
1. `CARD.md` line 45 is the separator row of the `## SHIPS` table. The fence allows line 44 only, so the header gets 7 cells and the separator keeps 6. GFM may then not render it as a table. I kept to the fence. Widen it to line 45 or accept the mismatch? Not applied.

## RECORDS
- The brain's four answers applied as given. Precedent: prompt 28 and `reports/launcher-fixround-amend-2026-10-05.md`.
- Nothing touched but the card; no git write, no launch, no command beyond Read, Grep and Edit.

LAUNCHER FIXROUND AMENDED 2 · decisions: 1
