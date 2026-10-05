## §0 Headline
- Card `prompts/2026-10-02/21-launcher-checks-card.md` amended with one fix round: row F1, L1–L6 marked SHIPPED, not rebuilt.
- F1: `desk-launch.sh` 746-748 also accepts a check tip that is an ancestor of the code tip, if the committed build REPORT ends `BUILT · … tip: <code tip>`.
- Header: BRANCH `ops/launcher-fixround-1005`, BASE left as the fill token. Not committed.
- decisions: 0.

## CARD
- Header lines 3-12: BRANCH, WORKTREE, REPORT (`launcher-fixround-1005` worktree), `BASE: «FILL: the 8-hex head of main when the build launches»`, TIP, CHECK REPORT and HOUSE B empty, RULINGS `2026-10-05 R376, 2026-10-05 R412`. HOUSE A and TREE STATE unchanged.
- New `THIS ROUND (2026-10-05)` paragraph before the table; old `WHY` kept as `WHY (original)`.
- Rows L1–L6 each prefixed `· SHIPPED, not rebuilt`.
- New row F1 (what quoted, red first with three negative controls, files) and a gate/touched-tests paragraph naming R390.
- `## NOT IN THIS JOB`: new first bullet (nothing else in `desk-launch.sh`, no hub file, no new command, no new argument).
- Test file for F1: `tests/ops/test_desk_launch_prechecks.py` (`neither the code tip` at `:432`).

## DECISIONS
None. The fix uses `git merge-base --is-ancestor`, already used at line 753; no new command or script.

## RECORDS
- Read: the card, `desk-launch.sh` 700-760, `CARD.md` header fields, `03d-adoption-port-card.md` (precedent), the test file's fixture index.
- Not run: `git log -L` (not needed; card and block already identified). No git write, no launch.
- Note: the prompt's header parenthesis says the desk fills RULINGS, while the same line sets its value; I set `2026-10-05 R376, 2026-10-05 R412` as instructed.

LAUNCHER FIXROUND DRAFTED · decisions: 0
