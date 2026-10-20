# draft-f5-x3-measure-amend — card 945 after preflight round 1

## §0 Headline
Card 945 amended in place for the 2 fails and 3 notes; nothing else changed, nothing committed.
FAIL 10: fixture is 13 lines (proved). FAIL 13: desk-staged script dropped; the builder writes `tests/cobalt/test_x3_calls_scratch.py`, runs it once in the background, deletes it with `scratch-clean.sh` before the commit.
Notes 3–5 added (background run, `figures()` shape, desk launches after 20:35 ET).

## DECISIONS
None open. (ASK DESK 1 in the card now holds the option-(b) default; its [18:15] tag is unchanged.)

## RECORDS
- 2026-10-20 18:09 EDT (`date`).
- Read: card 945 whole; `reports/f5-x3-measure-preflight-2026-10-20.md` whole; prompt 947 whole.
- Proofs: `git show main:tests/cobalt/fixtures/checkpoints/groups_sector_v140.csv` → marker line, header line, 11 rows = 13 lines. `git grep -n main -- BUILD-HUB.md` → `:70` "Write each row's `red first` test and each RUN row's test", `:72` scratch-clean rule, `:26` "Long runs `run_in_background`", `:14` admitted strings. `ops/desk/scratch-clean.sh` header: removes one untracked path under `$WT/<name>/…` (so the test must not be `git add`ed before removal). `git grep -F x3_calls main` → only docs of this job; the placement-named tests (`tests/cobalt/test_placement.py`, `tests/ops/test_build_hub_no_clutter.py`) do not read it.
- Edits: READ fixture line; TIME GATE sentence; R1 text (scratch test, path, background run, `figures()`); R1 "files" cell; C1 clean-up; CHECK ASK X1; DECISION 1; READ gains `BUILD-HUB.md:70`.
- Not edited (stale, left per "change nothing else"): `## RECORDS` lines of the card that still describe the staged `/tmp` script (the "Admitted strings" and "How a probe reaches the route" lines). ASK DESK: strike them at the next amend? [before launch] Default: leave; DECISION 1 governs.

DRAFTED · decisions: 1
