# card 324 fix rows F1, F2 — preflight (read-only), 2026-10-11

Card: `prompts/2026-10-11/324-shadow-hub-card.md` at `b02889d8`. Checked tip `cd302109` (`git rev-parse cd302109 ops/shadow-hub-1011` → both `cd302109296c…`).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | read card rows F1, F2 against precedent `298…card.md` F1 | four columns `row · what · red first · files`, as the precedent | OK |
| 1b | each row's FIXED instruction | F1 `FIXED: A9 — tests/ops/test_shadow_hub_file.py::<name>`; F2 `FIXED: O2 B5 — …::<name>`; both "append from column 0 above the build report's stop line", proof by `grep -n -F "def <name>"` (F2: "as in F1") | OK |
| 1c | each row names its red test | F1: new test in `test_shadow_hub_file.py`, RED on `cd302109` (prompt last, `:20`); F2: new test, RED (`"Read"` at `:20`) | OK (NOTE 1) |
| 2a | `git show cd302109:docs/40 - DevDocs/prompts/SHADOW-HUB.md`, line count | `:20` is the `claude-sonnet-5-5` row; prompt last after `"mcp__*"`; `"Read"` bare | OK |
| 2b | same file, `:33` and `:46` | both name `/Users/cobalt/cobalt-wt/<worktree>/SHADOW-INSTRUCTIONS.md`; `:46` ends "The builder's sandbox reads only its workspace, so everything it needs is copied in" | OK |
| 2c | `git show cd302109:ops/desk/bare-guard.py`, `grep -n` | `:104 SHADOW_FILE = "SHADOW-INSTRUCTIONS.md"`; `:1139-1145 write_targets` (reads `Edit(//`, `Write(//`, `--allow "Write(`, ` -C `); `:1148 builder_call`; `:1164 prefix, suffix = filled.split(PASS_PROMPT)`; `:1169 write_targets(prefix)`; `:1171 head = verb(words(prefix))`; `:1172` both flag tests on `prefix` | OK |
| 2d | `git show cd302109:tests/ops/test_bare_guard.py`, `grep -n` | `SHADOW_ROWS` `:2097`, Sonnet row `:2102-2107`; `test_s3_the_gate_seat_runs_its_models_builder_command` `:2146` | OK |
| 2e | `grep -n` in `test_shadow_hub_file.py` (tree = `cd302109`) | `test_s1_the_claude_builder_runs_no_command` `:151-154` | OK |
| 3a | F1 prompt first and the signed allow string still matches | new cell `claude -p --model claude-sonnet-5-5 "<pass prompt>" --permission-mode …` begins with `claude -p --model claude-sonnet-5-5 `, so `Bash(claude -p --model claude-sonnet-5-5 *)` (test file `ALLOW`, row cell) still matches; no new command class | OK |
| 3b | F1 guard change proved | reordered template: `prefix` = `claude -p --model claude-sonnet-5-5 `, `suffix` = the flags; `write_targets(prefix)` is empty ≠ `{target/**}` (`:1169`) and both `:1172` tests miss, so G7 denies every Sonnet call. With `prefix + suffix`: one target (Edit and Write give the same set), `" --permission-mode dontAsk "` and `'--disallowedTools "Bash" '` found. `:1171` stays on `prefix` (head `claude`). Grok (suffix empty) and Terra (suffix ` < /dev/null`, `-C` in prefix) read the same | OK |
| 3c | F1 files | `bare-guard.py` (`:1169-1172` only) is named in the row's `files`; also in S3's files; RESTARTS class home: `## RECORDS` line "RESTARTS class per path: S6", S6 names `ops/desk/` → "operator script; no Cobalt reader", `tests/ops/` → no resident, `docs/` → `DOCS`; F1 and F2 add no path beyond S1/S3's | OK (NOTE 2) |
| 3d | F1 negative controls | with the reorder, `test_s1_the_claude_builder_runs_no_command` still holds (`" --permission-mode dontAsk "` and `--disallowedTools "Bash" ` are both in the cell), `test_s1_each_row_…` (`startswith` `claude -p --model claude-sonnet-5-5 `) and `test_s1_every_builder_writes_only_its_worktree` stay green; `NO BASH DENY` case still denied (command no longer ends with the template suffix) | OK |
| 4a | F2 scope string | `"Read"` → `"Read(//Users/cobalt/cobalt-wt/<worktree>/**)"`, the `//` spelling of the cell's `Edit`/`Write` | OK |
| 4b | `SHADOW-INSTRUCTIONS.md` inside the glob | `/Users/cobalt/cobalt-wt/<worktree>/SHADOW-INSTRUCTIONS.md` matches `/Users/cobalt/cobalt-wt/<worktree>/**`; `grep -n -F -e "SHADOW-INSTRUCTIONS.md"` on the hub → `:29, :33, :46, :57, :70`; guard `:104` | OK |
| 4c | no unscoped `Read` test | F2: "exactly one `Read` entry … no entry is the bare word `"Read"`"; guard pin: bare `"Read"` call denied G7 (command no longer ends with the template suffix) | OK |
| 4d | `write_targets` needs no change for `Read(//…)` | regex `"(?:Edit|Write)\((//[^)]*)\)"` does not match `Read(`; `:1139-1145` | OK |
| 5a | `grep -c -F -e "«FILL"` on the card | `0` | OK |
| 5b | `git diff 4ea2b0ec b02889d8 -U0` on the card | `2 insertions(+)` only, the two rows at `:28-29`; header lines 1-11 untouched; precedent's F1 (`0a517366`) also changed no header | OK |
| 6 | commands the F1/F2 steps need | `grep -n -F`, `uv run pytest`, edits of four listed files, the FIXED line; all inside the builder's allow line | OK |
| 7 | `grep -n -E "ops/desk\|tests/ops\|prompts" configs/cobalt/jobs.yaml` | no output; the `ops/` hits are `start_aset.sh` and plists, none `ops/desk` | OK, `RESTARTS: none` holds |

## ISSUES
- NOTE 1: both rows leave the test name as `<name>`, as the 298 F1 precedent does; the build names it and proves it with `grep -n -F "def <name>"`.
- NOTE 2: the RESTARTS class home for `bare-guard.py` is the card's existing S6 line in `## RECORDS`; F1 adds no line of its own and needs none, since the file was already in S3's `files`.
- NOTE 3: `tests/ops/test_desk_launch_shadow.py:47` carries its own Sonnet fixture line (`… --permission-mode dontAsk "<pass prompt>"`), independent of the hub cell, so F1 does not touch it.
- NOTE 4: F2's two `test_bare_guard.py` cases are pins (green once the fixture is scoped), as the row says; its red is the hub-file test.

PREFLIGHT DONE · card: shadow-hub-1011 · checks: 21 · fails: 0 · ready: YES
