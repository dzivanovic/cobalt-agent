# gemini-builder-row FR-1 preflight — 2026-10-17

Read-only. Card `prompts/2026-10-16/671-gemini-builder-row-card.md`, draft `reports/draft-671-fixround-2026-10-17.md`, branch `ops/gemini-builder-row-1017`.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff HEAD --stat -- <card> <prompt 696>` | empty: the card is committed (`e831ef8f`), its diff against HEAD is empty | OK |
| 2 | `git diff 255451d1 e831ef8f -- <card>` (the card's last commit before the amendment) | `7 insertions(+)`, no `-` line: the `## CONTINUE FIX ROUND` section (1 paragraph), ONE new table row `FR-1`, the `FIX ROUND ORDER` paragraph. Rows L1, G2, H1, X2, R1 unchanged | OK |
| 3 | FR-1 shape | RED before the fix (O1 test on the tip, `1 failed`, `AssertionError: (0, '')`); the fix (`r" --add-dir[ =](\S+)"` plus comment); two controls; the mutation; the quoted-output order in `FIX ROUND ORDER`. `## CONTINUE FIX ROUND` is in the shape of card 641's (`:17`); card 583 names its section `## FIX ROUND` | OK |
| 4 | no row for O2 or X6 | the section says "Not added: O2 … and X6 (keep the four R1 lines)"; the table has no such row | OK |
| 5 | scope and fences | FR-1 files: `ops/desk/bare-guard.py` (`builder_call`, one line + comment) and `tests/ops/test_bare_guard.py` (appended only). Card 670's files stay in `## NOT IN THIS JOB`; the 583 `g5` hunk (`:1274`) is stated untouched. On the tip `g5` is at `:1264` (583 not deployed) | OK |
| 6 | `git show ops/gemini-builder-row-1017:ops/desk/bare-guard.py`, grep `-n`: `:1203` | `if head == "agy":` | OK |
| 7 | same, `:1204`, `:1205` | `# card 671 G2: agy --add-dir D (D/**), read for agy only`; `targets \|= {d + "/**" for d in re.findall(r" --add-dir (\S+)", prefix + suffix)}` (space spelling only, as the card says) | OK |
| 8 | same, `:1206`, `:1207` | `if targets != {target + "/**"}:` then `return False` | OK |
| 9 | same, `:1197`, `:1213-1215` | `:1197` the `startswith(prefix)`/`endswith(suffix)` test; `:1213-1214` the agy `--mode`/`--sandbox` rule, `:1215` `return False` | OK |
| 10 | tip test file `tests/ops/test_bare_guard.py` (`git show 7b986738:…`) | `GEMINI` `:2461`, `gemini_seat` `:2468`, `gemini` `:2481`, last test `test_k5_add_dir_widens_no_other_builder` `:2533`; `G7_ROUTE` `:157`; `assert_denied`/`assert_allowed`/`run` exist. No `check_o1` test yet, so the tests are appendable and the `-k check_o1` count is 3 | OK |
| 11 | `git diff --stat 7b986738 ops/gemini-builder-row-1017` | only `reports/gemini-builder-row-build-2026-10-17.md` and `.result`: the later head `7b22e411` is docs only, as the card says | OK |
| 12 | new commands | `uv run pytest -q -p no:cacheprovider …`, `uv run pytest -q tests/ops`, `uv run cobalt jobs restarts <tip>..HEAD`, `git diff`, `git diff --stat`: the row-R1 commands of the card (R411, R412); no new command outside the standing allow line (L62) | OK |
| 13 | blockers of `desk-launch.sh build` on this card (`:1020-1060`, `:1637-1655`) | header fields `JOB LADDER BRANCH WORKTREE BASE REPORT RULINGS` present; BASE `7f415a4f` is a commit; card committed and unstaged; REPORT under the worktree; worktree `gemini-builder-row-1017` exists and `git status --porcelain` is empty; `ls /Users/cobalt/cobalt-wt/*/.env` finds none, so the resume `FIX ROUND row FR-1` (`lock_free`) passes. Empty `TIP:`/`CHECK REPORT:`/`HOUSE B:` bind the check kind only (`:1694`). Nothing blocks | OK |
| 14 | RED claim, controls | the O1 test is the check's run; control 1 (`=` form on the worktree stays allowed) and control 2 (second space-form `--add-dir` stays G7 at `:1206`) are sound on the tip and after the regex | OK |

## ISSUES
- NOTE: control 1 says "the hub row's `--add-dir {wt}` rewritten `--add-dir={wt}`"; the hub row holds `--add-dir /Users/cobalt/cobalt-wt/<worktree>`, and `gemini()` fills `<worktree>`. The builder rewrites ` --add-dir ` to ` --add-dir=` in `GEMINI[2]` before filling; the meaning is clear.
- NOTE: this launch needs the worktree to stay clean and no `.env` in any `cobalt-wt/*`; both held at the time of this read.
- NOTE: line numbers are the tip's; card 583 is not deployed, and FR-1 finds its lines by content (`:1203-1206`).

PREFLIGHT DONE · card: gemini-builder-row-fixround · checks: 14 · fails: 0 · ready: YES
