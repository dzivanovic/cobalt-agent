## §0 Headline
- Card `83-worktree-salvage-card.md` amended by the four stated edits; nothing else changed.
- Test count proven: 7 functions, 12 collected tests.
- `BASE` is still the one fill token; `TIP`, `CHECK REPORT`, `HOUSE B` stay empty.
- The draft report's RECORDS still says "8 tests"; this seat edits the card and this report only.

## CHANGES
- W1 (`:19`), count: "The eight existing … tests" → "The existing … tests (`:251-315`: 7 test functions, 12 collected tests, the parametrized `:290` running 6 cases)".
- X2 (`:45`), count: "the eight old tests" → "the 12 old collected tests (7 functions)".
- W1 (`:19`), lock match: "whether a `locked` line is present" → adds "the line matches `^locked( |$)` (git prints `locked <reason>` when a reason was given), not the bare line".
- W4 (`:22`), steps: adds "`add -A` and `commit` run only when `status --porcelain` is non-empty; a DETACHED, CLEAN, unmerged tree takes the wip branch at its HEAD with `switch -c` alone, no commit, and prints `SALVAGED: <wip> 0 files <m> commits ahead`".
- W4 (`:22`), DETACHED test: adds "(the clean path: `switch -c` only, no salvage commit; the wip tip is that commit)".
- W7 (`:25`): adds "it greps for `--force` and `-f ` forms only, so `clean -` is a loose substring: the builder keeps the card header and every script comment free of `clean -`".

## DECISIONS
- ASK DESK: amend the draft report `worktree-salvage-draft-2026-10-07.md` (`:5` "eight existing tests", `:25` "8 tests") to 7 functions / 12 collected tests? Default: leave it, the card is the build source. [11:00 ET]

## RECORDS
- Read `tests/ops/test_gate_clean.py` at main HEAD `4ab74c8b`: `def test_` at `:251 :269 :274 :282 :290 :298 :310` = 7 functions in `:251-315`; `:290` is `@pytest.mark.parametrize` over 6 values (`:290`) → 6 + 6 = 12 collected. The file has 22 `def test_` in all.
- Read `reports/worktree-salvage-preflight-2026-10-07.md` `## ISSUES` (FAIL #13, NOTE W4, W1, W7).
- Grep of the card and draft for "eight": card `:19`, `:45`; draft `:5`, `:25`.
- Read the card whole before and after the edits; `grep FILL` token count unchanged (the BASE token only).

WORKTREE SALVAGE CARD AMENDED · decisions: 1
