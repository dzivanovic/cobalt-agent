# card 106 fix-round rows — 2026-10-08

## §0 Headline
Added `## FIX ROUND` (rows F1-F3, the brain's words) to card `106`, after the ROWS section and before `## DECISIONS`. Header values and rows G1-G5 are unchanged.
S3, S4, S5 are recorded as KEPT, no row. Each `file:line` was proven against `d522f6f7`.
One discrepancy: the brain's F1 grep `grep -rn "INSTALL in" tests/ops` matches nothing. The literal is `«INSTALL`.

## CHANGES
- Card `prompts/2026-10-08/106-desk-ops-fixes-card.md`, edited in place:
  - New `## FIX ROUND` section (table in the card's row format) with F1, F2, F3.
  - The card has no single `files` line, so the widening is in the F1 `files` cell: it now names `tests/ops/test_desk_launch_devfix.py`. F2 and F3 name their own paths.
  - `## RECORDS`: three new lines (FIX ROUND RESTARTS, the citation proofs, the F1 grep note), placed before the "Post-deploy" line.
- Nothing else touched, including `## NOT IN THIS JOB`.

## RECORDS
Reads at `d522f6f7` (`git grep` / `git show`):
- `src/cobalt/notify/mattermost.py:152` `return SendResult(False, "channel disabled …")`: confirmed.
- `ops/desk/close-timer.sh:63` `send_dm(sys.argv[1])`: the result is discarded, confirmed.
- `ops/desk/desk-launch.sh:374` refuses when the close report exists: confirmed.
- `tests/ops/test_desk_launch_devfix.py:180` `assert "«INSTALL" in text`: confirmed. Hits at `:181`, `:287` and `:289` are not asserts that the token is in a filled hub.
- `tests/ops/test_desk_launch_brain.py:25` defines `INSTALL`. `:285` already asserts `INSTALL not in text` (R358), so it is not a F1 file.
- `DEVFIX-HUB.md` and `BRAIN-HUB.md` hold no `«INSTALL` now (count 0), so the install rows have landed.
- S3, S4, S5: read in the check's `## OPEN` and KEPT, no row.
- Lines changed in the card: the new `## FIX ROUND` block and three RECORDS lines only.
- RESTARTS class: the F1 test file goes in `test/documentation; no resident`, with the card's other `tests/ops` paths.

FIX ROUND ROWS ADDED · decisions: 1
