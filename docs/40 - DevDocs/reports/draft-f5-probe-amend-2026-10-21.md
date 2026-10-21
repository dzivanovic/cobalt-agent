# draft-f5-probe-amend — 2026-10-21

## §0 Headline
- Card 973 amended in place for preflight FAILs #21-#24; nothing else changed. Uncommitted.
- #21: second `## RECORDS` line added verbatim (R2284).
- #22: X6 clause starts `figures: 1 real fetch + 3 derived by rule D`; `test_x6_four_prompts_one_per_slot_pair` asserts it.
- #23: G1 PATH must be under `/Users/cobalt/cobalt-wt/.f5-probe/`; new `test_the_run_path_writes_no_body`.
- #24: X4 FAIL (exit 1) names the known FINAL `:178` consequence and ends `plist load not blocked by X4`.

## DECISIONS
1. X4 digit hit: `validate_reply` already refuses a digit in any string (`checkpoints.py:372-374`), so an accepted line can only hit by number-word. The row says so. No new digit scan.
2. X4 clause wording: `→ narrative degraded-by-default (FINAL :178)` when valid is below 15; `→ <phrase_id> removed from the enum (FINAL :178)` for each phrase with a hit; every FAIL ends `; plist load not blocked by X4`. Both X4 tests assert these parts.
3. G1 off-root refusal: `FAIL refused: --keep-groups PATH must be under /Users/cobalt/cobalt-wt/.f5-probe/`. The test monkeypatches the root to a `tmp_path` subdir, so no test writes under the real root.
4. Run-path pin, three legs: (a) no file in cwd, `HOME` or the root after `fetch_groups` / `fetch_figures` are called without `keep`; (b) the same after `checkpoint run --slot 0745 --dry-run` through the real `run_checkpoint`; (c) a content pin that `keep=` appears only in `fetch_groups`, `fetch_figures` and the pass-on between them, never in `cmd_run` or `run_checkpoint`. A run without `--dry-run` writes the note through the fakes, so the body check uses the dry run.
5. NOTE 8: the X6 test's constructed sector Changes are eleven distinct values. Its added assertion, `ONE Groups GET recorded`, backs "1 real fetch".
6. Growth: `973-f5-probe-card.md` is now 22897 bytes (+4/−3 lines, `git diff --stat`). The growth is the four fixes, all required by the preflight.

## RECORDS
- Seat `draft-f5-probe-amend` (prompt 975). Ran 2026-10-21 12:15:36–12:16:26 EDT (`date`). Read-only apart from Edit on card 973 and Write of this report. No git write, no run.
- `git -C /Users/cobalt/cobalt rev-parse main` → `9e551491` at the end. Card BASE `d988d543` stays as written (preflight NOTE 5).
- `git show main:src/cobalt/prefill/checkpoints.py`: `:140` `UnsourcedFigure`; `:200` `parse_groups`; `:222-235` `fetch_groups` (async; `raise_for_status` `:232`, `return parse_groups(response.text)` `:235`); `:238-256` `fetch_figures`; `:353` `_strings`; `:363-391` `validate_reply` (digit refusal `:372-374`); `:813-834` `cmd_run` (passes no `keep`); `:837-844` `add_parser`.
- The card's existing `:224-235` cite for `fetch_groups` is two lines late: the def is at `:222`. The prompt said to change nothing else, so it is left as is.
- `git grep main -- "docs/30 - Design/F5-FINAL-2026-10-11.md"`: `:178` X4 (digit or number-word → phrase removed; under 15 of 20 → degraded-by-default), `:180` X6, `:187` X13.
- `git grep main -- reports/cto-2026-10-21.md`: `:12` R2284 DESK RECORD (brain, L79).
- `git grep main -- tests/cobalt/test_checkpoints_offline.py`: `:138` `cp`, `:307` `groups_http`, `:327` `TestNumbers`.
- Preflight read: `reports/f5-probe-preflight-2026-10-21.md` `## ISSUES` 1-8.

DRAFTED · decisions: 6
