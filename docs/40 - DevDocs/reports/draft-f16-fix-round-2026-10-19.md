# draft-f16-fix-round (2026-10-19)

## §0 Headline
- Card 790 gains row FIX1 (O1 + O2 from the check's `## FIXES`), CHECK ASKS X6 and X7, one `## RECORDS` line. Nothing else changed; BASE, TIP, CHECK REPORT, HOUSE B, BAND untouched.
- Files: `src/cobalt/taxonomy/loader.py` (`:88` only) and `tests/cobalt/test_f16_close_1018.py`, both already in the card's `files` (C1; V1/V2/C1).
- The two `FIXED:` lines are exactly as ordered, placed in the build report's text; the row's step text has no underscore-free problem (it says run the touched tests and gate, then `BUILT`).

## DECISIONS
1. ASK DESK: the fix text is referenced to the check report's `## FIXES` ("copied byte for byte") instead of pasted into the card cell. Default: the builder copies from the report. [08:27]
2. ASK DESK: the O1 test is placed after `test_c1_a_row_with_no_consumer_is_refused` (`:97`); the check did not fix a position. Default: as placed. [08:27]

## RECORDS
- `date` → Mon Oct 19 08:25:18 EDT 2026.
- Read: prompt 830; `areas/cobalt.md`; card 790; check report (whole); precedent 801 and card 448 row FIX1 (format).
- Proved: `git show s5/f16-close-1018:src/cobalt/taxonomy/loader.py` and `:tests/cobalt/test_f16_close_1018.py` (whole); worktree reads for line numbers: `loader.py:74-93`, test file `:1-102`, `cli.py:333-355`; Grep `tests/cobalt/test_playbook_offline.py:264`.
- `FIXED:` format checked against `ops/desk/deploy-card.sh:208`.
- Not run: no tests, no git write, no launch.

DRAFTED · decisions: 2
