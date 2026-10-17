# check-scratch-fr1 FR-1 preflight — 2026-10-17

Read-only. Card `prompts/2026-10-16/681-check-scratch-fr1-card.md`, draft `reports/draft-681-fixround-2026-10-17.md`, check `reports/check-scratch-fr1-check-2026-10-17.md`, branch `ops/check-scratch-fr1` (code tip `b093f192`, head `5f42c4f3`).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt diff --stat -- <card 681>` | empty: the card is committed (`1364f214`), its diff against HEAD is empty | OK |
| 2 | `git diff 42cd6874 1364f214 -U0 -- <card>` (last commit before the amendment) | `7 insertions(+)`, no `-` line: the `## CONTINUE FIX ROUND` section (one paragraph, before `## ROWS`), ONE new row `FR-1`, the `FIX ROUND ORDER` paragraph. Rows R0, MK-1, CL-1, R2 unchanged | OK |
| 3 | FR-1 test vs the check's `## OWN FINDINGS` | card names `test_o1_legacy_a_higher_numbered_build_copy_is_not_the_prior_card` with the same steps as the check's test: `job`; `prior_staging(job, change=False)`; `unlink(missing_ok=True)` of `STAGED-CARD`; `build_card_copy(dest, card, name="05-x-job-build-card.md")`; `fr_card(job)`; `stage`; exit 0; `cleared: {dest} (prior check {repo / CHECK_A})` first; `not build.exists()`. Helpers exist on the branch (`build_card_copy` `:442` with `name`, `fr_card` `:344`, `prior_staging` `:193`, `CHECK_A` `:189`); no `test_o1` yet, so it is appendable | OK |
| 4 | green run and red run named | green: `-k test_o1_legacy` → `1 passed` on the tip. Red: `:134` removed by Edit → whole file `1 failed` (the O1 test, `assert 1 == 0`, stderr `the prior card copy is no version of a card on main …`), others green; undone, `git diff --stat <tip> -- ops/desk/stage-set.sh` prints nothing; then `0 failed`. Matches the check's O1 run | OK |
| 5 | no source change | row says `ops/desk/stage-set.sh` stands byte for byte; files column is `tests/ops/test_stage_set.py` (appended test only) | OK |
| 6 | no row for A1 or `_two_card_copies` | the section and the row both say "Not added: A1 … `_two_card_copies`"; the table has no such row. A1 settled as rejected (R1786) | OK |
| 7 | scope and fences | FR-1 touches `tests/ops/test_stage_set.py` only; `## NOT IN THIS JOB` kept (card 583's files, `desk-watch.sh`, other scripts, hubs, `.claude/settings.json*`) | OK |
| 8 | `git show ops/check-scratch-fr1:ops/desk/stage-set.sh` + `grep -n` on the worktree: `:134` | `            printf '%s\n' "$head" \| grep -q '^HOUSE A:' \|\| continue` — in the `while IFS= read -r f` loop of the no-marker `else`, after the `^CHECK REPORT:` line at `:133` | OK |
| 9 | same file, `:92`, `:173`, `:194`, `:201` | `clearable() {`; caller `clearable`; the two `rm -rf` lines (`grep -n "rm -r"` → exactly `194`, `201`) | OK |
| 10 | `git diff --stat b093f192 ops/check-scratch-fr1 -- ops tests src` | empty: head `5f42c4f3` adds only the report, as the card says | OK |
| 11 | tip test file `git show ops/check-scratch-fr1:tests/ops/test_stage_set.py` | last test `test_mk2_control_a_marker_that_is_a_link_is_refused` (`:651`); the legacy test `test_mk2_legacy_real_shape_…` (`:574`) ranks its build copy `01-…` below the check cards, as the row says | OK |
| 12 | the row's "every FR-1-era test runs the MARKER branch" | `prior_staging` (`:193`) calls `stage(...)`, which writes `STAGED-CARD` (`stage-set.sh:242`); the unlink in the O1 test forces the legacy `else` | OK |
| 13 | new commands | `uv run pytest -q -p no:cacheprovider …`, `uv run pytest -q tests/ops`, `uv run cobalt jobs restarts <tip>..HEAD`, `grep -c -F "rm -r"`, `git diff --stat`: the commands of the card's earlier rows; no new command outside the standing allow line (L62) | OK |
| 14 | `ls -d /Users/cobalt/cobalt-wt/*/.env` | no match (exit 1): no `.env` in any worktree | OK |
| 15 | what blocks `desk-launch.sh build` on this card (`:1637-1655`) | nothing found. Header has `JOB LADDER BRANCH WORKTREE BASE REPORT RULINGS`; REPORT is under `cobalt-wt/check-scratch-fr1/docs/40 - DevDocs/reports/`; worktree exists, on `ops/check-scratch-fr1`; the resume step `FIX ROUND row FR-1` runs `lock_free`, which passes (check 14). Empty `TIP:` and `CHECK REPORT:` bind the check kind only (precedent: the 671 fix-round preflight). Not verifiable here: `git status --porcelain` of the worktree (not on the allow line); `ls -a` of it shows no stray file, and the check report states it ended at `## ops/check-scratch-fr1` clean | OK |
| 16 | `CARD.md` shape | `CARD.md` holds neither section name; the shape is card 641's / 671's (`## CONTINUE FIX ROUND` before `## ROWS`, `FIX ROUND ORDER` after the last row) | OK |

## ISSUES
- NOTE: line `:134` is the tip's number (the draft's DECISION 1, default taken: cited as the check did); the row finds the line by content.
- NOTE: the worktree's `git status --porcelain` clean state is not provable from this seat (no `git -C cobalt-wt` on the allow line); `desk-launch.sh build` refuses at `:1650` if it is dirty.
- NOTE: the row's red-run claim is the check's run (`1 failed, 37 passed` with the A1 trial test deselected); with the O1 test added the file has 38 tests, so the builder's quote reads `1 failed, 37 passed`.

PREFLIGHT DONE · card: check-scratch-fr1-fixround · checks: 16 · fails: 0 · ready: YES
