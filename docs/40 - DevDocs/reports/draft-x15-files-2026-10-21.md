## §0 Headline
Card 977 amended in place: P1's `files` now include `tests/cobalt/test_s3_c3_panel_offline.py`, with the one-line `BASE_ROUTES` change (`:61`) named in P1's row.
Line proven against `main`. Nothing else changed, nothing committed.

## DECISIONS
1. The `files` list was the only place needing the file. The `## NOT IN THIS JOB` fence names no tests, and the RESTARTS note already says `tests/` → no resident, so neither changed.

## RECORDS
- 2026-10-21 13:04 EDT (`date`).
- `git grep` on `main:tests/cobalt/test_s3_c3_panel_offline.py:61` → `"/hitl", "/hitl/{row_id}", "/hitl/{row_id}/approve", "/hitl/{row_id}/deny",`. The `:542` assert is `pre_existing == BASE_ROUTES`.
- Edited: `prompts/2026-10-21/977-x15-hitl-probe-card.md`, the P1 row (what text + files cell). Builder ASK DESK W report lines 160/170 were not opened; the card's own prompt gave the route and test names.

DRAFTED · decisions: 1
