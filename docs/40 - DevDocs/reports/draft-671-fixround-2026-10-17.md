# draft-671-fixround — 2026-10-17

## §0 Headline
Card 671 gains one fix-round row, FR-1 (check O1): `bare-guard.py:1205` reads every `--add-dir` spelling (`[ =]`), RED is the check's O1 test, two controls, one mutation.
A `## CONTINUE FIX ROUND` section and a `FIX ROUND ORDER` paragraph are added; no existing row is changed.
O2 and X6 get no row.

## DECISIONS
1. ASK DESK: the fix is the regex `r" --add-dir[ =](\S+)"`, not a refusal of an agy template holding `--add-dir=`. Default taken: the regex (one rule; a second `--add-dir` in either spelling fails `targets != {target/**}`). [before the build launch]
2. ASK DESK: FR-1 adds two controls beyond the O1 test (`=` spelling on the worktree stays admitted; a second space-form `--add-dir` stays G7). Default taken: add them. [before the build launch]

## RECORDS
- Edited only `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/671-gemini-builder-row-card.md` (Edit tool); this report is the one other file written.
- `file:line` proved on `git show ops/gemini-builder-row-1017:ops/desk/bare-guard.py` (branch tip `7b22e411`, docs only after `7b986738`): `:1203` `if head == "agy":`, `:1204` the G2 comment, `:1205` `targets |= {d + "/**" for d in re.findall(r" --add-dir (\S+)", prefix + suffix)}`, `:1206` `if targets != {target + "/**"}:`, `:1213-1215` the agy `--mode`/`--sandbox` rule.
- O1 test quoted from `reports/gemini-builder-row-check-2026-10-17.md` `## OWN FINDINGS` O1 and its RUNS line (`AssertionError: (0, '')`).
- Fences kept: card 670's files and card 583's `g5` hunk untouched.
- Not run by this seat: the tests (drafting only).

DRAFTED · decisions: 2
