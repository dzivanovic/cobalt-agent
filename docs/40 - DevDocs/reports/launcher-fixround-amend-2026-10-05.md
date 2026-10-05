## §0 Headline
Row F1 of `prompts/2026-10-02/21-launcher-checks-card.md` now uses the brain's option b: an optional last `## SHIPS` column `fix report`.
The real lines match the prompt: `carry` is line 714 (field 7), the new cell is field 8, the check-tip test is 746-748, the committed test is 733-736.
The header is written by `ops/desk/deploy-card.sh` (lines 207-208), so F1's files now name it.
Three points for the desk are in DECISIONS (3 decisions). Nothing was run, committed or launched.

## CARD
- Row F1, text and red-first cell and files: replaced as above. The files are now `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_prechecks.py` and `ops/desk/deploy-card.sh`.
- The negative controls are: (a) the `fix report` cell is empty; (b) its last line lacks `tip: <code tip>`; (c) uncommitted; (d) the check tip is not an ancestor of the code tip. Each is green on BASE for `neither the code tip`, and also run against the fixed script. A card with no `fix report` column passes as today.
- `## NOT IN THIS JOB` line 1: `any new argument` became `any new command (the column is a header value, not a new argument or command)`.

## DECISIONS
1. Extra test (mine): row F1 also asserts the header that `deploy-card.sh` writes ends `| fix report |`. The prompt widened the files to that script but named no test for it. Drop that sentence if unwanted.
2. `deploy-card.sh` line 141 writes each SHIPS row with 6 cells. A header with a 7th column needs an empty 7th cell on each row for a well-formed table. F1 does not say so. The builder either adds the empty cell on line 141 or leaves the rows short, and the launcher reads an absent cell as empty either way. The desk should rule which.
3. `prompts/CARD.md` line 44 shows the same SHIPS header, and `CARD.md` is fenced by this card. It stays at 6 columns until the desk allows an edit there. `## NOT IN THIS JOB` line 1 still says `anything else in desk-launch.sh than lines 746-748's test`, though F1 now also adds line 714's `frep=`. I left that as written per "touch nothing else".

## RECORDS
- Read: the card; `ops/desk/desk-launch.sh` 690-764; `ops/desk/deploy-card.sh` 195-219; `prompts/CARD.md` SHIPS lines; grep of `SHIPS` in `ops/desk/`.
- Edited: the card only (row F1 and `## NOT IN THIS JOB`). Time 13:44.

LAUNCHER FIXROUND AMENDED · decisions: 3
