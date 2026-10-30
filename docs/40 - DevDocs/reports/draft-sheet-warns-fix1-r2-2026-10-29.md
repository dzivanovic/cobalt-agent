# DRAFT r2 — card 1082 fix row S1 — 2026-10-29

## §0 Headline
- Card 1082 edited in three places only: row S1 proof, `:80-98` → `:80-100`, `ORDER:` names S1 after D1.
- S1 drops `uv run python -c` red/green and `bash -n`; proof is two greps plus T1 (a) pin; snippet run is `UNPROVEN (L70)`.
- BASE/TIP/CHECK REPORT/HOUSE B/RULINGS and all other rows untouched.

## DECISIONS
1. ASK DESK: header `TIP: 01107570` is behind the branch tip `d57714468` (preflight NOTE 2); not touched. Default: the desk owns it and leaves it, since the script and `match.py` did not change between the two. [20:08]
2. ASK DESK: the desk may run the S1 snippet itself if it wants the proof. Default: stays `UNPROVEN (L70)`. [20:08]

## RECORDS
- `date` → `Thu Oct 29 20:07:53 EDT 2026` (reads done); `Thu Oct 29 20:08:02 EDT 2026` (edits).
- Read whole: prompt 1092, card 1082, preflight `sheet-warns-fix1-preflight-2026-10-29.md`, draft `draft-sheet-warns-fix1-2026-10-29.md`, `prompts/CARD.md`, `BUILD-HUB.md:10-18`, `writing-rules.md`.
- `git grep -n` on `ops/sheet-check-warns:scripts/smoke_s1.sh`: grade steps `:80`, `:87`, `:94`, last `except SheetMismatch` at `:100`; the F6 sheet step `:101-108`; `assert_sheet_matches` at `:103`, `:106`; selector step `:109`. So `:80-100` is right.
- `git grep -n` on `ops/sheet-check-warns:tests/cobalt/test_daymode.py`: `sheet_warning` import `:33`; `TestMatchCheck` full-on-reduced test `:395-404` asserts the text ending `reload half.htk or overrule` (`:401-404`).
- `git show ops/sheet-check-warns:src/cobalt/daymode/match.py`: `sheet_warning` returns `sheet FULL loaded, day mode REDUCED (= the HALF sheet) — reload half.htk or overrule` for `full.htk` on `reduced`.
- Edited: `docs/40 - DevDocs/prompts/2026-10-29/1082-sheet-check-warns-card.md`. Nothing run, nothing committed.

DRAFTED · decisions: 2
