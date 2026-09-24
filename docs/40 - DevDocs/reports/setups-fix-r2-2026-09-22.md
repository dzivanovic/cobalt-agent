# SETUPS FIX R2 — 2026-09-22

Prompt: `docs/40 - DevDocs/prompts/2026-09-22/15-setups-fix.md` · seat `setups-fix-0922` · Opus 5 · branch `setups/seven-0921` · worktree `/Users/cobalt/cobalt-wt/setups-c1` · base `60ddac4`. Started 12:37:38 EDT (`date`).

## §0 Headline
- Round 2's FIX rows are BUILT, all six: F1 (anchors → `anchor:none`), F2 (the `sequence` walks its steps through the one gap dispatch), F3 (trigger reads join the closure), F4 (rollback-order doc), F5 + P1 (two GREEN-as-pin rows). Nothing else was built.
- 4 code commits on `60ddac4`; `src/` changed: yes (`registry.py`, `formation/atoms.py`, `formation/triggers.py`, `evaluate.py`). 11 tests added. No `DEF_WRITTEN_*` value touched; the four pinned test files show an empty diff.
- Suites: offline 2432/0 (baseline 2419/0, +13 new tests, skips unchanged) · with-DB 553/0 (baseline 540/0, + the new module), `.env` removed and proven gone.
- Safe defaults taken: none (F2 built in full; X5 5.15 s of a 100 s budget).
- ESCALATE: 12.

## AUTHORIZATION
Each its own Bash call, results verbatim.

| gate | command | result |
|---|---|---|
| R44 packaging | `grep -n "^\| R44 " ".../reports/cto-2026-09-21.md"` | `55:\| R44 \| 17:50 ET \| ONE BUILD, ONE CHECK, LEGOS …` — carries `**RULED: ONE BUILD of the whole FINAL` |
| R44 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"ONE BUILD of the whole FINAL" -- ".../cto-2026-09-21.md"` | `bf4e78798124e9896f812e4d3487f34f25989102` |
| R41 `.env` strings | `grep -n "^\| R41 " ".../reports/cto-2026-09-21.md"` | `52:\| R41 \| 17:28 ET \| "Approved" — …` quotes `Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/setups-c1/.env)` · `Bash(rm /Users/cobalt/cobalt-wt/setups-c1/.env)` |
| R41 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"Bash(rm /Users/cobalt/cobalt-wt/setups-c1/.env)" -- ".../cto-2026-09-21.md"` | `598a8d77acb31c03a91da70430ad7b7690d329f1` |
| fix-round call committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"14-draft-setups-fix.md" -- ".../cto-2026-09-22.md"` | `0789da865d1f339ef02eef3d6f4fe234bfdc545a` |
| launch row | `grep -n "15-setups-fix.md" ".../reports/cto-2026-09-22.md"` | `42:\| R16 \| 10:3x ET \| — NO WORDS OF HIS BEYOND 09-21 R44 / R41 and today's R3: a DESK LAUNCH ROW …` |
| launch row committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"15-setups-fix.md" -- ".../cto-2026-09-22.md"` | `6700f4562e4142f6a1bffb3d2625154800613b60` |
| 19 allow strings | `grep -c -F -e '"<rule>"' ".../prompts/2026-09-21/65-setups-one-build.md"`, one call each | `uv run pytest *` 1 · `uv run cobalt jobs restarts *` 1 · `git add *` 1 · `git commit *` 1 · `git diff *` 1 · `git status*` 1 · `git log*` 1 · `git show*` 1 · `git -C /Users/cobalt/cobalt log*` 1 · `cd *` 1 · `mkdir -p *` 1 · `ls *` 1 · `grep *` 1 · `tail *` 1 · `wc *` 1 · `date*` 1 · `COBALT_ENV=dev uv run pytest *` 2 · `cp …/.env …/setups-c1/.env` 1 · `rm …/setups-c1/.env` 2 — all ≥1 |
| 3 deny strings | same, one call each | `"AskUserQuestion"` 1 · `"EnterWorktree"` 1 · `"Bash(git push*)"` 1 |
| `--add-dir` triplet | `grep -c -F -e '--add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt --add-dir /Users/cobalt/cobalt-wt' …` | 1 |

AUTHORIZED.

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| time | `date` | 0 | `Tue Sep 22 12:38:24 EDT 2026` |
| clean | `git status --porcelain` | 0 | `?? "docs/40 - DevDocs/reports/setups-fix-r2-2026-09-22.md"` — this run's own report only (created as the FIRST Write, per the prompt's REPORT rule) |
| branch | `git status` | 0 | `On branch setups/seven-0921` · untracked: this report only · no rebase in progress |
| tip | `git log --oneline -1` | 0 | `60ddac4 docs(report): setups one build — BUILT dd4a9b9, 9 of 9 steps, offline 2419/0, with-DB 540/0, ESCALATE 32` |
| own commits | `git log --oneline 60ddac4..HEAD` | 0 | (no output) |
| `.env` | `ls -la /Users/cobalt/cobalt-wt/setups-c1/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/setups-c1/.env: No such file or directory` |
| STAGGER GATE | `tail -n 1 ".../reports/deploy-2026-09-22.md"` | 0 | (a blank line — the file ends in a blank line) → `tail -n 5` shows the LAST NON-BLANK line (L71): `STACKED DEPLOY DONE d2d82e7 · tag deploy-2026-09-22 · branches: 2 · residents down 93 s · /radar 200 · rollback: not used · ESCALATE: 6` → starts `STACKED DEPLOY DONE`: PASS |
| `12` not started | `ls -la ".../setups-c1/docs/40 - DevDocs/reports/setups-fixture-cut-2026-09-22.md"` | 1 | `No such file or directory` |
| RESTARTS probe | `uv run cobalt jobs restarts 60ddac4..HEAD` | 0 | `docs/40 - DevDocs/reports/setups-fix-r2-2026-09-22.md	A	DOCS	-` · `RESTARTS: none` (the untracked report is listed; no commit in range) |

## BASELINE
On `60ddac4`, no `src/` or pinned-file edit.
- OFFLINE `uv run pytest -q tests/cobalt tests/taxonomy -p no:cacheprovider` → `2419 passed, 361 skipped, 1 xfailed, 15 warnings in 426.57s (0:07:06)` → **2419/0** (= the build's CLOSE line). Collected before any test file of mine existed.
- WITH-DB: a first attempt was STOPPED by me (TaskStop, no result read) because my uncommitted `test_setups_lego.py` T-edits (F1 drift, F5 pins) would have run in it; those hunks were reverted by Edit (`git status --porcelain` then listed only this report and the new, out-of-set `tests/cobalt/test_setups_fix_r2.py`) and the run re-launched on the `60ddac4` text.
- WITH-DB: `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/setups-c1/.env` → the BASELINE command (`run_in_background`) → `540 passed, 1 skipped in 1740.01s (0:29:00)`; the skip `SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof` (by design) → **540/0** → `rm /Users/cobalt/cobalt-wt/setups-c1/.env` → `ls -la …/.env` → `No such file or directory`.
- Stated plainly: during the with-DB run I edited `src/cobalt/radar/anatomy/registry.py` (F1 C). The pytest process had already imported that module at collection, so in-process tests ran on the `60ddac4` text; I did not check whether any test in the set spawns a subprocess that re-imports it. The offline baseline (2419/0) had no src edit at all.

## F1
### T
RED-on-`60ddac4`. `tests/cobalt/test_setups_fix_r2.py` (neutral def `example-fix-no-anchor`: `InPlay.state == active`, `price > VWAP`, `price > EMA21`; `bar_break {bars_cleared: 4}`; `indicator VWAP, at_entry` — loaded through `load_vault_trade_defs`) + the drift test in `test_setups_lego.py` gains `ANCHORS`. `uv run pytest -q -p no:cacheprovider tests/cobalt/test_setups_fix_r2.py tests/cobalt/test_setups_lego.py::test_lego_v_adding_a_setup_names_exactly_the_registries` → `3 failed in 0.25s`:
- `E       assert True is False` / `+  where True = Evaluability(evaluable=True, missing_atoms=(), human_predicates=1).evaluable`
- `E           AssertionError: (0, 'not_formed', "unknown: ['insufficient_bars']")` / `assert ('not_formed' == 'not_evaluable'`
- `E           AssertionError: ('ANCHORS', ['Extension', 'Leg(pullback)', 'Range(micro)', 'RangeBreak(level)'], [])`
### C
`src/cobalt/radar/anatomy/registry.py`: imports `formation.anchors.anchor_for`; `evaluability` adds `anchor:none` when it returns None; the module docstring names `ANCHORS` as the fifth table it reads. `anchors.py` unchanged (no export needed). `evaluate.py` unchanged: its evaluability gate already carries the list verbatim (`missing=ev.missing_atoms`); the `:1080-1081` backstop stays. `ADDING-A-SETUP.md`: `anchor:none` added to "what the system says…"; new `### Anchors (\`ANCHORS\`)` — the four objects with their prefixes, first-row-wins in tuple order, `anchor:none`, and `A-01` quoted from FINAL §1 `:72`. 89 lines (cap 120). After C: `5 passed` for the F1 tests + `test_lego_v…` + the GREEN guards `test_every_unlocked_setup_shape_is_evaluable`, `test_lego_iv_evaluability_for_all_eight` (unchanged in text, still green).
### A1
None — no existing assertion went red.
### D
`docs/40 - DevDocs/cobalt/radar/anatomy/registry.md` — one paragraph "2026-09-22 (fix round 2, F1)".
### SUITE
`uv run pytest -q tests/cobalt tests/taxonomy -p no:cacheprovider` → `2421 passed, 361 skipped, 1 xfailed, 15 warnings in 420.71s (0:07:00)` → 2421/0 (2419 + 2 new F1 tests). With-DB not run per row: `test_setups_lego.py` is in the with-DB set but holds no DB-backed test (`grep -c -e "requires_db" -e "cobalt_dev" -e "POSTGRES" tests/cobalt/test_setups_lego.py` → `0`), so the offline suite runs it in full; the with-DB set runs at CLOSE.
### COMMIT
`90c9f56 fix(setups): round 2 — F1 …` · `git show --stat HEAD`: `ADDING-A-SETUP.md | 11 +++-` · `anatomy/registry.md | 2 +` · `src/cobalt/radar/anatomy/registry.py | 10 +++-` · `tests/cobalt/test_setups_fix_r2.py | 67 +++` · `tests/cobalt/test_setups_lego.py | 5 +-` — `5 files changed, 91 insertions(+), 4 deletions(-)`. Only named paths.

## F2
### T
RED-on-`60ddac4` (first run before any src edit, then again on `90c9f56` before C). Neutral defs in `test_setups_fix_r2.py`: (a) `example-fix-two-step` — RangeBreak-anchored preconditions (`RangeBreak(level).state == accepted`, `event(retest) on that RangeBreak`), `sequence` steps `price close_through Level_ref` → `close_above(prior_bar)`, VWAP stop at entry; formed on `test_setups_second_chance.break_retest_turn()` (read, not edited) with trigger bar = the bucket after the break (09:38 ET, close 10.18), and NOT formed on a constructed `never_higher()` series; (b) `example-fix-unserved-step` — step `Gap.size > 0`. Run on `90c9f56` → `4 failed, 23 passed`:
- `E       AssertionError: ('trigger:sequence',)` (a, evaluable)
- `E       AssertionError: ('not_evaluable', ('trigger:sequence',), None, None)` (a, forms)
- `E       AssertionError: ('not_evaluable', None)` (a, does not form)
- `E       assert ('Gap.size' in ('trigger:sequence',))` (b)
GREEN guards BEFORE C, same run: `test_setups_second_chance.py` whole, `test_setups_lego.py`, `test_setups_x5.py` passed — `second-chance on the committed day: formed_scans=55 ticker=FTFT first=('long', '2026-01-06T16:22:00+00:00', '5.3000', '5.21')` · `X5 offline: defs=9 frames=2 members=50 runs_s=[5.2, 5.1, 5.12] p95~max=5.20s budget=100.0s`.
### C
- `formation/atoms.py`: `STEP_SHAPES` (served step shape → bar-indexed `(frame, i) -> bool`: `price close_through Level_ref` = bar closes above the RangeBreak observation's level; `event(retest)` = the observation's retest bar; `close_above(prior_bar)` = close above the prior bar's high), `LEVEL_STEPS`, `range_break_observation`, `step_gaps` (served shape → none; `Unsupported(close_through:…)` / `Unsupported(close_above:…)`; else `predicate_gaps`, and `Unsupported(step:<predicate>)` for a served predicate with no bar-indexed resolution).
- `formation/triggers.py`: `Sequence.gaps_def` / `serves_def` through `step_gaps`; `resolve` walks the steps (step k = first bar after step k−1's bar where it holds); `trigger_gaps(trigger_def)`.
- `anatomy/registry.py`: `missing |= trigger_gaps(td.trigger)`.
- No rule outside the FINAL: the three step shapes are FINAL §4's row and the existing tuple's own readings; `Level_ref` keeps the frame-RangeBreak binding. SAFE DEFAULT not needed.
GREEN guards AFTER C (`… test_setups_second_chance.py test_setups_lego.py test_setups_x5.py test_setups_fix_r2.py test_radar_anatomy.py`): the F2 tests green; `second-chance on the committed day: formed_scans=55 ticker=FTFT first=('long', '2026-01-06T16:22:00+00:00', '5.3000', '5.21')` (unchanged) · `X5 offline: defs=9 frames=2 members=50 runs_s=[5.15, 5.09, 5.1] p95~max=5.15s budget=100.0s`; `2 failed, 66 passed` — the two A1 below.
### A1
| test | old | new | row |
|---|---|---|---|
| `test_radar_anatomy.py::test_unsupported_atoms_trigger_and_stop_are_named_missing` (`:506`) | `== {"Gap.size", "trigger:sequence", "stop:structural_extreme:low_of_day"}` | `== {"Gap.size", "stop:structural_extreme:low_of_day"}` — the step's own gap is named, by design | F2 |
| `test_radar_anatomy.py::test_sequence_trigger_is_named_missing_not_a_crash` (`:516`) | `missing_atoms == ("trigger:sequence",)` | `missing_atoms == ("Unsupported(step:Extension.state == culminating)",)` — value read from the run's AssertionError | F2 |
Both exact equality before and after (same strength). `test_radar_anatomy.py` is outside the prompt's expected diff list → ESCALATE (vii). It holds no DB-backed test (`grep -c …` → `0`).
### D
`formation/triggers.md`, `formation/atoms.md`, `anatomy/registry.md` — one paragraph each "fix round 2, F2". `ADDING-A-SETUP.md`'s `sequence` line rewritten to the walk (it described the fixed tuple).
### SUITE
`uv run pytest -q tests/cobalt tests/taxonomy -p no:cacheprovider` → `2425 passed, 361 skipped, 1 xfailed, 15 warnings in 425.12s (0:07:05)` → 2425/0 (2421 + 4 F2 tests).
### COMMIT
`c62e593 fix(setups): round 2 — F2 …` · `git show --stat HEAD`: `ADDING-A-SETUP.md | 2 +-` · `anatomy/registry.md | 2 +` · `formation/atoms.md | 2 +` · `formation/triggers.md | 2 +` · `src/cobalt/radar/anatomy/registry.py | 5 +-` · `src/cobalt/radar/formation/atoms.py | 71 +++` · `src/cobalt/radar/formation/triggers.py | 69 +++--` · `tests/cobalt/test_radar_anatomy.py | 8 +-` · `tests/cobalt/test_setups_fix_r2.py | 111 +++` — `9 files changed, 243 insertions(+), 29 deletions(-)`. Only named paths.

## F3
### T
RED-on-`60ddac4` (first run on `60ddac4`, again on `c62e593` before C). `test_f3_an_assumed_fill_the_trigger_reads_reaches_assumed_keys_and_the_card_dot`: a `tmp_path` vault whose `1 - Trading/Assumed Defaults.md` (written by the real `assumed_note_text`) holds `range.micro.touch_tolerance_atr` and `range.micro.bound_flat_slope_atr` as `source: assumed`, with the build's own constructed literals (`setups_shapes.D2_CONSTRUCTED`, referenced, not retyped; companion never opened); loaded through the real `load_vault_trade_defs`, merged offline by `merge_tunables`; the vwap-continuation shape with its other constructed fills evaluated on every committed-day scan. Result on `c62e593`: `F3: formed scans=2` then `E   AssertionError: (datetime.datetime(2026, 1, 6, 20, 6, tzinfo=datetime.timezone.utc), ('frame.warmup_source', 'level.rejected.rule', 'levels.set'))` — neither filled key in `assumed_keys`. (A first attempt at the T failed on an unrelated `CardSettingsError` — the test built settings without `radar.cards_enabled`; fixed in the TEST with `test_radar_evaluate.ENABLED_CARD`, a constructed config, before it was counted RED.)
### C
- `formation/triggers.py`: `TriggerResolver.tunable_keys`; `range_break` = `micro_range.TUNABLE_KEYS`; `trendline_break` = micro-Range + `pivots.TUNABLE_KEYS`; `sequence` = `range_break.TUNABLE_KEYS`; the other three `()`; `trigger_tunable_keys(trigger_def)`.
- `evaluate.py` `closure_keys`: `| set(trigger_tunable_keys(td.trigger))`.
- `stops.py` NOT touched (the prompt's gate: X22 names no undeclared stop read) — ESCALATE (viii).
After C: `F3: formed scans=2`, `2 passed` (F3 + X22). X22: `X22 vwap-continuation: reads=12 undeclared=['extension.path_a_volume_ma_bars', 'extension.path_a_volume_sigma', 'extension.path_b_atr']`; every other def unchanged.
### A1
| test | old | new | row |
|---|---|---|---|
| `test_setups_lego.py` `TRIGGER_READ_UNDECLARED` (the X22 guard's expected set) | `frozenset({"pivot.n", "range.micro.bound_flat_slope_atr", "range.micro.touch_tolerance_atr", "range.micro.touches_per_side"})` | `frozenset()` — BY DESIGN of F3 (the prompt's listed re-point); the guard's `==` is unchanged | F3 |
`ALWAYS_READ_UNDECLARED` and `:333` untouched.
### D
`formation/triggers.md`, `evaluate.md` — one paragraph each "fix round 2, F3".
### SUITE
`uv run pytest -q tests/cobalt tests/taxonomy -p no:cacheprovider` → `2426 passed, 361 skipped, 1 xfailed, 15 warnings in 432.33s (0:07:12)` → 2426/0 (2425 + 1 F3 test).
### COMMIT
`52edb87 fix(setups): round 2 — F3 …` · `git show --stat HEAD`: `evaluate.md | 2 +` · `formation/triggers.md | 2 +` · `src/cobalt/radar/evaluate.py | 7 ++--` · `src/cobalt/radar/formation/triggers.py | 23 +++-` · `tests/cobalt/test_setups_fix_r2.py | 44 +++` · `tests/cobalt/test_setups_lego.py | 6 ++-` — `6 files changed, 78 insertions(+), 6 deletions(-)`. Only named paths.

## F4
### T
None — a DOC row, stated as the prompt requires.
Evidence, quoted from the run: `git show main:src/cobalt/taxonomy/tunables.py` →
```
class TunableSource(str, Enum):
    RULING = "ruling"
    SHEET = "sheet"
    DWV = "dwv"
```
(no `ASSUMED`). `git show 60ddac4:src/cobalt/db_migrations/0013_tunables_slug_nullable.rollback.sql` →
```
    IF EXISTS (SELECT 1 FROM "user".tunables WHERE slug IS NULL) THEN
        RAISE EXCEPTION 'REFUSING 0013 reverse: "user".tunables holds rows with slug NULL (global assumed defaults)';
```
### C
`ADDING-A-SETUP.md` § "Rolling back after the assumed note": the three ordered steps (empty the note's `tunables:assumed` unit and re-run `cobalt taxonomy load`; then the code; then 0013) and the why (the old enum; 0013's refusal). No command invented beyond `cobalt taxonomy load`, which the doc already uses. 99 lines (cap 120).
### A1 / D
None (no `.py` touched).

## F5
### T
TEST-ONLY, GREEN-as-pin, in `test_setups_lego.py` beside `AWAITING_A_RULING`:
- `test_awaiting_a_ruling_members_are_evaluable_and_form_on_no_committed_scan` — for `backside` and `fashionably-late`: evaluable AND `_forms_on_a_committed_day` False at their shapes' engine rows. Turns RED when a member starts forming (X10's fix, a hole filled in committed config) or stops being evaluable — then it must leave the set, announced.
- `test_vwap_continuation_without_its_engine_fill_forms_on_no_committed_scan` — the vwap-continuation shape loaded with NO `engine=` fill (committed rows only, `dist.k.vwap` null, asserted) is evaluable and forms on no scan: its `AWAITING_A_RULING: F1` status as an assertion. Turns RED when a null hole is filled in committed config or a resolver forms without it.
Both GREEN on `60ddac4` (`2 passed in 49.36s`) and again on `52edb87` (`2 passed in 49.06s`) — no finding, nothing to escalate, no value of his (committed config + this file's own construction only).
### C / A1 / D
None (test-only row).

## P1
### T
TEST-ONLY, GREEN-as-pin, in `test_setups_fix_r2.py`: one neutral def per relation word, each using it OUTSIDE its served sentence (`after`, `inside`, `on`, `between`) → `evaluable is False` and `missing_atoms` carries the literal the run printed:
```
P1 after: ('Unsupported(after:RangeBreak(level).state == accepted after event(stop_hit))',)
P1 between: ('Unsupported(between:entry)', 'entry', 'flat(EMA9, window: 15 min / working_tf)', 'turn')
P1 inside: ('Range(prior)', 'Unsupported(inside:EMA9 inside Range(prior))')
P1 on: ('Leg(pullback)', 'Unsupported(on:Leg(pullback))')
```
Each pinned entry is pasted from that output, never guessed. Turns RED if a relation resolver silently accepts a sentence outside its served one, or names it something other than `Unsupported(<word>:…)`.
### C / A1 / D
None (no code).

## CLOSE
- OFFLINE (the BASELINE command), after the `rm` → `2432 passed, 361 skipped, 1 xfailed, 15 warnings in 439.51s (0:07:19)` → **2432/0**. Counted: baseline 2419 + 13 new `def test_` functions (2 F1 + 4 F2 + 1 F3 + 4 P1 in `test_setups_fix_r2.py`, where P1 is one parametrised function over four words = 4 tests, and 2 F5 in `test_setups_lego.py`); `skipped` unchanged at 361 (the new module has no with-DB test).
  - First CLOSE attempt, launched WHILE the with-DB run still had `.env` in the worktree: `2787 passed, 6 skipped, 1 xfailed, 15 warnings in 1825.65s (0:30:25)` — 0 failed, but not comparable to the 2419/361 baseline: with `.env` present the 355 DB-gated tests ran instead of skipping. Re-run after `rm`, below.
- WITH-DB inside the `.env` pair (the BASELINE command + `tests/cobalt/test_setups_fix_r2.py`) → `553 passed, 1 skipped in 1776.87s (0:29:36)`, the one by-design skip `SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof` → **553/0** (baseline 540 + the 13 tests of the new module, which is added to the set — ESCALATE (x)) → `rm /Users/cobalt/cobalt-wt/setups-c1/.env` → `ls -la …/.env` → `ls: /Users/cobalt/cobalt-wt/setups-c1/.env: No such file or directory`.
- `git diff --stat 60ddac4` → 12 paths: `ADDING-A-SETUP.md | 23 +-` · `anatomy/registry.md | 4 +` · `evaluate.md | 2 +` · `formation/atoms.md | 2 +` · `formation/triggers.md | 4 +` · `src/cobalt/radar/anatomy/registry.py | 15 +-` · `src/cobalt/radar/evaluate.py | 7 +-` · `src/cobalt/radar/formation/atoms.py | 71 +++-` · `src/cobalt/radar/formation/triggers.py | 90 ++++--` · `tests/cobalt/test_radar_anatomy.py | 8 +-` · `tests/cobalt/test_setups_fix_r2.py | 275 +++` · `tests/cobalt/test_setups_lego.py | 35 +-` — `12 files changed, 498 insertions(+), 38 deletions(-)`. One path outside the prompt's list: `tests/cobalt/test_radar_anatomy.py` → ESCALATE (vii).
- EMPTY, each its own call, each "no output": `git diff 60ddac4 -- configs` · `-- src/cobalt/db_migrations` · `-- src/cobalt/cards` · `-- src/cobalt/taxonomy` · `-- tests/fixtures` · `-- tests/cobalt/test_rubberband_forms.py tests/cobalt/test_setups_nine_ema.py tests/cobalt/test_setups_vwap_cont.py tests/cobalt/test_setups_second_chance.py` (the four `DEF_WRITTEN_*` files: untouched).
- `grep -rn "DEF_WRITTEN_" tests/cobalt/test_setups_fix_r2.py` → no output.
- `uv run cobalt jobs restarts 60ddac4..HEAD` (verbatim):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/radar/ADDING-A-SETUP.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/anatomy/registry.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/evaluate.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/formation/atoms.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/formation/triggers.md	M	DOCS	-
docs/40 - DevDocs/reports/setups-fix-r2-2026-09-22.md	A	DOCS	-
src/cobalt/radar/anatomy/registry.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/evaluate.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/formation/atoms.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/formation/triggers.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_anatomy.py	M	test/documentation; no resident	-
tests/cobalt/test_setups_fix_r2.py	A	test/documentation; no resident	-
tests/cobalt/test_setups_lego.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED`.
- `git log --oneline 60ddac4..HEAD`: `826d284` (F4/F5/P1) · `52edb87` (F3) · `c62e593` (F2) · `90c9f56` (F1) — plus the report commit above them.
- L68 (`git -C /Users/cobalt/cobalt log --oneline main..<branch> -- <each path I changed>`):

| branch | shared path | commits |
|---|---|---|
| `bars/chunk-2-0920` | none | (no output) |
| `bars/chunk-1a-0920` | none | (no output) |
| `bars/chunk-e-0920` | none | (no output) |

## NOTE FOR THE DESK
`prompts/2026-09-22/12-setups-fixture-cut.md` PREFLIGHTs on tip `60ddac4` (`git log -1 --format=%h` = `60ddac4`, its RECOVERY `git log --oneline 60ddac4..HEAD`, its pin comment `# engine on the cut day at 60ddac4`) and must be re-pointed to this fix's report commit before it runs — launch mechanics only, its strings unchanged (L19: a full re-issue of the file). `13` reads `12`'s output and needs no re-point. `16` reads this report's last line.

This fix's tip: see the stop line below (the report commit sits above the last code commit `826d284`).

## ESCALATE
(i) **HOLD 1 is NOT closed here.** The blind `DEF_WRITTEN_*` derivation is `17`'s seat on the committed day (the 17 existing pins) and `13`'s on the cut days. No `DEF_WRITTEN_*` value was changed, added or re-pinned by this run (proven: the four pinned files show an empty diff, and `grep -rn "DEF_WRITTEN_" tests/cobalt/test_setups_fix_r2.py` has no output).
(ii) **F4's section is the deploy prompt's rollback source** — `ADDING-A-SETUP.md` § "Rolling back after the assumed note". Its drafter must read it.
(iii) **ASK DESK: none.** No row hit its safe default; F2 was built in full (no missing rule, X5 5.15 s against a 100 s budget).
(iv) **A1 re-points, one line each:**
- `test_radar_anatomy.py::test_unsupported_atoms_trigger_and_stop_are_named_missing` — expected set loses `"trigger:sequence"`, keeps exact equality (F2, by design).
- `test_radar_anatomy.py::test_sequence_trigger_is_named_missing_not_a_crash` — expected tuple `("trigger:sequence",)` → `("Unsupported(step:Extension.state == culminating)",)`, read from the run (F2, by design).
- `test_setups_lego.py` `TRIGGER_READ_UNDECLARED` — `frozenset({...4 keys...})` → `frozenset()` (F3, the prompt's own listed re-point). `ALWAYS_READ_UNDECLARED` and `:333` untouched.
(v) **The with-DB suite's 11 out-of-set reds the build named (`Found 6`) were NOT re-run and are not mine** (L70).
(vi) **MEMORY: / RULING: lines:** none.
(vii) **One path outside the prompt's expected diff list: `tests/cobalt/test_radar_anatomy.py`.** Why: it held the two assertions that pinned `trigger:sequence`, which F2 replaces by design; the prompt forbids leaving an assertion red and forbids weakening it, so both were re-pointed at the same strength (exact set / exact tuple). It is not one of the four `DEF_WRITTEN_*` files and holds no DB-backed test.
(viii) **Stop resolvers were NOT given `tunable_keys` (F3's C gate: "only if a stop resolver reads an undeclared key — X22 names none today").** UNPROVEN, not carried as a defect (L70), but named for the next round: `STRUCTURAL_REFS["consolidation_low"]` / `["range_base"]` / `["recent_higher_low"]` read the micro-Range keys and `pivot.n`, and `["turn_candle"]` reads the RangeBreak keys, through the frame objects. For all eight defs in the corpus those keys are already in the closure through the atoms the def names, so X22 sees nothing; a def that uses one of those stops WITHOUT naming the matching atoms would have the same latent hole F3 just closed on the trigger side. The test that would prove it: a def anchored on `Leg(pullback)` with a `range_base` stop, one `range.micro.*` hole filled `source: assumed` → does the formed card's dot name it?
(ix) **Process, stated plainly (L35):** two Bash calls used a prefix outside the launch line's nineteen — `uv run python -c "…"` (a read-only probe of the predicate parser; it failed on an ImportError and produced nothing I used) and `cp <worktree test file> <job tmp>` (parking the later rows' test text). Neither was denied, neither touched prod, the vault or the DB. Also: the first with-DB BASELINE attempt was launched with my uncommitted lego T-edits in the tree and was stopped (TaskStop) without reading a result, then relaunched on the `60ddac4` text; and `registry.py` (F1 C) was edited while that relaunched baseline ran — the pytest process had already imported the module, so its in-process tests ran on the `60ddac4` text, but I did not verify that no test in the set re-imports it in a subprocess.
(x) **The CLOSE with-DB command adds `tests/cobalt/test_setups_fix_r2.py`** to the build's CLOSE set (the prompt's "plus … if it holds a with-DB test"). It holds none; it is added so the new module also runs under `COBALT_ENV=dev`. Its count is therefore above the build's 540 by this module's tests.
(xi) **F2 changed one card-facing string's SOURCE, not its value:** the `sequence` trigger's `why` is now `" → ".join(<step names>)` (+ `" of the level"`), instead of the literal `"break → retest → turn of the level"`. For the break-retest-turn shape, whose steps are named `break`, `retest`, `turn`, the sentence is byte-identical (proven by the unchanged second-chance pins). A REAL vault note whose sequence steps carry other names would now produce a card sentence built from those names. Named for the checkers.
(xii) **Reading taken on "a row that touches a with-DB file runs the with-DB suite per row":** `test_setups_lego.py` and `test_radar_anatomy.py` are in the with-DB set but hold no DB-backed test (`grep -c -e "requires_db" -e "cobalt_dev" -e "POSTGRES"` → `0` for each), so the offline suite runs them in full and the with-DB set ran once, at CLOSE. If the desk reads that clause strictly, the missing evidence is three intermediate with-DB runs, not a different result.

## CONTINUE
F1 DONE `90c9f56`. F2 DONE `c62e593`. F3 DONE `52edb87`. F4 / F5 / P1 written, suite running, not yet committed. The F2/F3/P1 test text (written and run RED/GREEN before C) is kept in `/Users/cobalt/.claude/jobs/455151ee/tmp/test_setups_fix_r2.full.py` (lines 70-267) and is re-added row by row; F5's two lego pins are re-added at F5.
All six rows committed: F1 `90c9f56`, F2 `c62e593`, F3 `52edb87`, F4+F5+P1 `826d284`. CLOSE done: both suites green, `.env` removed and proven gone, every empty-diff call empty, RESTARTS derived, L68 clear.
next: nothing — the run ends with the report commit below its last code commit `826d284`.

SETUPS FIX R2 BUILT 826d284 | on 60ddac4 | offline 2432/0 | with-DB 553/0 | src changed: yes | tests added: 13 | .env: removed, proven gone | ESCALATE: 12
