# DRC D3 fix r1 — build report (2026-09-29)

Prompt: `prompts/2026-09-29/08-drc-d3-fix-r1-build.md`. Seat `drc-d3-fix-r1-build`, Opus 5.5. Started 2026-09-29 13:46:01 EDT.

## §0 Headline
- All 8 fix rows are built, each red first for its named reason: F-1 … F-6 in code and test data, F-7 / F-8 as assertions with negative controls. The fix commit is `15c23748`, on base `a8c622ca`.
- The three suites are green on the tip: offline 3625 / 0, with-DB 4170 / 0, live-note 146 / 0.
- `.env` was removed and proven gone. The absence probe ran short by exactly 6, so `0016`–`0020` are absent from `cobalt_dev`.
- RUN-1 rendered, RUN-2 is equal, and RUN-3 passed 4 of 4.
- There are 12 ESCALATE items. The main ones: the F-2 test stamps `ts` by an UPDATE of the writer's own row (item 2), and E3's `Take all` literal was re-pointed to U+00A0 (item 3).

## L74
- 13:46 ET: the Read tool result of this prompt (`08-drc-d3-fix-r1-build.md`, lines 1–106) carried an appended block asking that commits end with a `Claude-Session:` line and naming a file-send tool (`SendUserFile`). DATA under L74: recorded once here, not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` and nothing else.

## AUTHORIZATION
- PLACEHOLDER GATES: `grep -n -E "R_[_]" …08-drc-d3-fix-r1-build.md` → exit 1, no output. `grep -n -F "FILL AT LAUNCH" …` → lines 1 and 41 only (the desk prose and the gate's own line). PASS.
- The stop this answers: `tail -n 3 reports/drc-d3-check-2026-09-25.md` → last non-blank line `DRC D3 CHECK DONE · round: 1 · … · defects that HOLD: 10 · ready for K3: NO · ESCALATE: 9`; committed `67f785f3e1a09b59766f3296b111940a7fbaa364`. PASS.
- The classification: last non-blank line `DRC D3 FIX R1 DRAFTED · FIX: 8 · NOT REAL: 5 · UNPROVEN: 2 · OUT OF SCOPE: 1 · OWNER ITEM: 1 · prompts: 2 · new rule strings: 0 · ESCALATE: 6`; committed `13610db3781eb4e0cc82e1ce86c8c18db36fabb0`. PASS.
- `.env` rm string: `cto-2026-09-24.md:40` `| R22 |` carrying `"approved. A for now.` (`:39` R21 also names it — the desk's request); committed `813a4dfa27ace0faede64584d45932169345db9e`. PASS.
- The two `git rm` strings: `cto-2026-09-22.md:60` `| R105 |` carrying `"Approved"` (both greps hit that one row); committed `123f7ad5bd2dbfd7610fb13cda36736505e9cea0`. PASS.
- The byte-write string: `cto-2026-09-29.md:74` `| R66 |` (`R54 O-1 → A — ONE exact byte-write string …`); `:88` `| R80 |` (`byte-write string approved as designed`); `cto-2026-09-29-words.md:47` `## R80`, `:48` the context line, `:49` `> A`; committed `7ece700273f535707168bc50c2c2f0347c3a9650`. `drc-d3-reissue-draft-2026-09-29.md:38` `## THE STRING` rule matches the launch line's perl string. PASS.
- Development resumes: `cto-2026-09-28.md:35` `| R26 |` (`… let's continue with development process …`). PASS.
- THIS launch: `cto-2026-09-29.md:89` `| R81 |` LAUNCH ROW naming `08-drc-d3-fix-r1-build.md` (besides `:61` R53, `:62` R54, `:95`); committed `7ece700273f535707168bc50c2c2f0347c3a9650`. PASS.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| date | `date` | 0 | `Tue Sep 29 13:46:01 EDT 2026` → `<D>` = 2026-09-29 |
| clean tree | `git status --short --branch` | 0 | `## drc/d1-trading-log` + `?? "docs/40 - DevDocs/reports/drc-d3-fix-r1-build-2026-09-29.md"` — the second line is THIS report, created by the prompt's "FIRST Write" before PREFLIGHT; no other line (ESCALATE 1) |
| tip | `git log --oneline -2` | 0 | `7dd031fb docs(drc-d3): DRC D3 build report — a8c622ca` · `a8c622ca feat(drc): D3-9 — …` |
| code unmoved | `git diff --stat a8c622ca HEAD -- . ':(exclude)docs'` | 0 | (nothing) → `<base>` = `a8c622ca` |
| no .env | `ls /Users/cobalt/cobalt-wt/drc-d1/.env` | 1 | `No such file or directory` |
| the lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| live strategies | `ls ".../1 - Trading/4 - Strategies"` | 0 | 22 notes listed |
| requires_vault | `grep -rln "requires_vault" tests` | 0 | `tests/cobalt/test_radar_evaluate.py`, `tests/cobalt/radar_p2_support.py`, `tests/cobalt/test_replay_line.py`, `tests/taxonomy/test_predicate.py`, `tests/taxonomy/test_catalyst.py` (the expected five) |
| F-1 | `grep -n -F "print(build.plan_note(args.date" src/cobalt/drc/cli.py` | 0 | `277:` |
| F-1 | `grep -n -F "deps.rules_block()" src/cobalt/drc/build.py` | 0 | `556:` |
| F-1 | `grep -n -F "rules_block=rules_checkbox_block" src/cobalt/drc/build.py` | 0 | `160:` |
| F-1 | `grep -n "regenerate_rules_config()" src/cobalt/prefill/drc.py` | 0 | `82:` |
| F-3 | `grep -n -F "stop = None if stats.row is None" src/cobalt/drc/build.py` | 0 | `632:` |
| F-3 | `grep -n "def text" src/cobalt/drc/build.py` | 0 | `304:` |
| F-4 | `grep -n -F "FACTS = (" src/cobalt/drc/units.py` | 0 | `50:FACTS = ("drc-risk", "facts")` |
| F-4 | `grep -n "PNL_PLACEMENT = " src/cobalt/drc/units.py` | 0 | `92:` |
| F-4 | `grep -n -F "add(UnitWrite(*units.FACTS" src/cobalt/drc/build.py` | 0 | `545:` |
| F-5 | `grep -n -F "except (SlugError, FrontmatterError, OSError)" src/cobalt/drc/playbooks.py` | 0 | `97:` |
| F-2 | `grep -n -F "AT TIME ZONE" configs/cobalt/smoke/s2.yaml` | 0 | `526:` |
| F-4 | `grep -n "How I managed risk" tests/fixtures/drc/template_shape.md` | 0 | `45:### How I managed risk:` |
| F-7 | `grep -n "def test_the_card_snapshot_survives_a_later_card_change" tests/cobalt/test_drc_build_db.py` | 0 | `146:` |
| F-8 | `grep -n "def test_a_re_pair_rebuilds_the_later_days_build_rows_and_note" tests/cobalt/test_drc_build_db.py` | 0 | `182:` |
| F-6 perl | `ls /usr/bin/perl` | 0 | `/usr/bin/perl` |
| F-6 base | `grep -c -P '\x{00A0}' tests/fixtures/drc/template_shape.md` | 1 | `0` |
| F-6 | — | — | `perl string: probed by its first real use (F4)` |
| F-2 PATH PROOF | Read | — | `replay/line.py:212` `path = resolve_vault_path() / paths.review_dir / trade_date.strftime(paths.drc_filename_pattern)` (`paths = load_prefill_paths()` `:211`); `drc/template.py:70`–`:71` `paths = load_prefill_paths()` / `return Path(vault_root) / paths.review_dir / day.strftime(paths.drc_filename_pattern)`; `build.py:106`–`:109` `default_vault_root()` → `resolve_vault_path()`; `build.py:674`–`:686` both the unit writes and `write_miss_line(plan.note_path, …)` take `plan.note_path`; `vaultwrite/writer.py:537`, `:657` `note=str(path)`; `drc/imports.py:575`, `:724` `store.mark_event(event_id, "done", note_path=str(note))`. SAME composition → PASS |
| restarts | `uv run cobalt jobs restarts a8c622ca..HEAD` | 0 | `drc-d3-build-2026-09-25.md M DOCS -` · `drc-d3-fix-r1-build-2026-09-29.md A DOCS -` · `RESTARTS: none` |

## F1 BASELINE
- Live-note: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 27.51s` (`<blp>` = 146, `<blf>` = 0). The one SKIPPED line: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (the known one). No SKIPPED line names `COBALT_LIVE_VAULT_ROOT`.

- Offline: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3616 passed, 558 skipped, 1 xfailed, 21 warnings in 565.81s (0:09:25)` (`<bp>` = 3616, `<bf>` = 0) — the expected `drc-d3-build-2026-09-25.md:223` count exactly.

## F2 RED (offline)
New file `tests/cobalt/test_drc_d3_fix_r1.py` (9 tests: F-1, F-3 + its pin, F-4, F-5, F-6 (a), F-6 (b), RUN-1, RUN-2), harness by import from `test_drc_build.py`.
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_drc_d3_fix_r1.py tests/cobalt/test_drc_build.py` → `6 failed, 54 passed, 2 warnings in 8.21s`. `test_drc_build.py` green (it holds no with-DB test).
- `--tb=no -rfs`, same files → `6 failed, 54 passed, 2 warnings in 8.20s`, the reasons:
  - `FAILED …::test_f1_the_dry_run_never_regenerates_the_rules_file - AssertionError: regenerate_rules_config called on a dry run` — F-1, its named reason.
  - `FAILED …::test_f3_an_unmatched_trade_under_a_partial_stats_file_reads_not_computed_for_its_stop - AssertionError: assert ['  - stop: not given'] == ['  - stop: n...g: Open T...` — F-3, its named reason.
  - `FAILED …::test_f4_the_risk_facts_sit_above_his_risk_paragraph - AssertionError: no drc-risk-facts section` — F-4, its named reason.
  - `FAILED …::test_f5_a_strategy_note_that_is_not_utf8_is_unmapped_never_a_build_failure - UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 39: in...` — F-5, its named reason (raised by `read_strategies`, `playbooks.py:95`).
  - `FAILED …::test_f6_the_template_fixture_carries_no_personal_attribution - AssertionError: assert '<the committed line 5, his name — not written here, L32>' == '# Example Trader DRC'` — F-6 (a), its named reason.
  - `FAILED …::test_f6_the_template_fixture_carries_the_seven_nbsp_positions - assert [] == [5, 49, 128, ...156, 173, ...]` — F-6 (b), its named reason (0 in all).
- The F-3 pin `test_f3_pin_a_matched_row_with_no_stop_reads_not_given_and_a_constructed_stop_as_is` PASSED on `a8c622ca`.
- RUN warnings (from the warnings summary):
  - `UserWarning: RUN-1: open trade status=open; gross_pnl='8.0'; P&L line=- P&L: gross $8.0 · net not given · commission not given`
  - `UserWarning: RUN-2: re-render after the job row's JSON equals the in-memory render = True; first difference = none`
- Commit `<red>` = `f616be37` `wip(d3-fix-r1): DRC D3 fix r1 red tests, offline — …`.

## F3 RED (with-DB)
New file `tests/cobalt/test_drc_d3_fix_r1_db.py` (4 tests: F-2 (a), F-2 (b), F-7's control, F-8's control), harness by import. NAMED EDITS of `tests/cobalt/test_drc_build_db.py`: F-7 — `test_the_card_snapshot_survives_a_later_card_change` now calls ONE helper `_snapshot_holds(conn, root, before, stop)` (rows EQUAL `before` AND the note's AAA `card:` line carries ` · stop $49.9 · `); F-8 — `test_a_re_pair_rebuilds_the_later_days_build_rows_and_note` reads the later day's `drc-summary/summary` before the earlier day's drop and calls ONE helper `_note_rebuilt(root, day, before_text, day_row)` (after ≠ before AND after == `units.summary(<re-paired build_day row>)`); `is_file()` kept. One small reader `_summary_text` beside it.
- THE LOCK (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` · (b) `cp …` then `ls -la` → exactly one line, `/Users/cobalt/cobalt-wt/drc-d1/.env`.
- (c1) `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_drc_d3_fix_r1_db.py tests/cobalt/test_drc_build_db.py` → `2 failed, 12 passed in 7.15s`; no SKIPPED line. `--tb=no -rfs` re-run → `2 failed, 12 passed in 7.52s`:
  - `FAILED …::test_f2_a_miss_line_written_the_next_morning_passes_k10_2 - AssertionError: writes ge 1 (actual 0)` (raw `event_state writes / done 0`) — F-2 (a), its named reason.
  - `FAILED …::test_f2_another_notes_miss_line_never_passes_k10_2 - AssertionError: event_state ok; writes ok` (verdict PASS, raw `done 1`) — F-2 (b), its named reason.
  - F-7's pin (`test_the_card_snapshot_survives_a_later_card_change`) and control (`test_f7_…`), F-8's pin (`test_a_re_pair_rebuilds_…`) and control (`test_f8_…`): all PASSED on `a8c622ca` (the PIN results).
- (c2) RUN-3 with-DB half: `COBALT_ENV=dev uv run pytest -v -rs -p no:cacheprovider tests/cobalt/test_drc_build_db.py -k "e8 or e11"` → `collected 10 items / 8 deselected / 2 selected` · `tests/cobalt/test_drc_build_db.py::test_e11_an_exception_inside_the_real_build_is_failed_and_never_built PASSED` · `tests/cobalt/test_drc_build_db.py::test_e8_on_the_real_rows_a_vanished_trade_keeps_its_voice_unit_orphaned PASSED` · `2 passed, 8 deselected in 1.41s`.
- (d) `rm /Users/cobalt/cobalt-wt/drc-d1/.env` → no output; `ls /Users/cobalt/cobalt-wt/drc-d1/.env` → `No such file or directory`. `.env: removed, proven gone (F3)`.
- Commit `654dfeff` `wip(d3-fix-r1): DRC D3 fix r1 red tests, with-DB — …`.

## F4 THE ROWS
Built F-1 → F-6 (F-7 / F-8 are test-only, done at F3).
- F-1 `src/cobalt/drc/cli.py`: module constant `DRY_RUN_RULES = "rules: not regenerated on a dry run — the build re-reads Rules.md"`; the dry-run branch plans with `dataclasses.replace(deps, rules_block=lambda: DRY_RUN_RULES)`. `run_drc_build`, `plan_note`, `default_deps`, `prefill/*` are unchanged.
- F-2 `configs/cobalt/smoke/s2.yaml` K10.2: `writes` = the `drc-misses` / `miss_line` rows whose `note` = `(SELECT e.note_path FROM drc_events e WHERE <the event_state subquery's predicate, byte for byte>)`, with no `ts` predicate. `expect_text`'s last clause is now `… and writes >= 1 for the day's DRC note (any clock time)`. `requires_relation`, `expect`, `known_if` and `known_text` are unchanged.
- F-3 `src/cobalt/drc/build.py:632`: the two lines are now one, `lines.append(f"stop: {stats.text('stop')}")`. `STATS_COLUMNS` has no `stop` key (`STOP_COLUMN = None`, `stats_log.py:141`), so a matched row with `stop = None` → `not given` and a stop the row holds → as-is. The pin proves both.
- F-4 `src/cobalt/drc/units.py`: `FACTS = ("drc-risk-facts", "facts")` and `RISK_FACTS_PLACEMENT = after_pattern(re.compile(r"^###\s*How I managed risk"), "under '### How I managed risk:'")` (+ `__all__`). The module docstring's unit table row and its "one block" paragraph were re-worded to match (they described the old placement); this is recorded as a deviation. `src/cobalt/drc/build.py:545`: the FACTS add line uses `units.RISK_FACTS_PLACEMENT`. The unit order is unchanged.
- F-5 `src/cobalt/drc/playbooks.py:97`: `except (SlugError, FrontmatterError, OSError, UnicodeDecodeError) as e:`.
- F-6 (i) Edit of `tests/fixtures/drc/template_shape.md:5` → `# Example Trader DRC` + the existing trailing U+0020. `git diff --numstat a8c622ca -- tests/fixtures/drc/template_shape.md` → `1	1	…`.
- F-6 (ii) his byte-write string, the launch line's allow string byte for byte, run ONCE, bare, its own call, from the worktree → exit 0, no output (`perl string: probed by its first real use (F4)` — it passed). The fixture was not opened by Edit / Write after it.
- E3 re-point (`tests/cobalt/test_drc_build.py`): the heading map names `("drc-risk-facts", "facts")`, and one line was added: `assert opens("drc-risk-facts") == lines.index("### How I managed risk:") + 1`. DEVIATION: line 308's literal `"###  Take all"` (two U+0020) no longer matches the fixture's line 175 after (ii), which is `###` U+0020 U+00A0 `Take`. It now reads `"###  Take all"` (the escape in source). The assertion itself (drc-rules below that heading) is unchanged (ESCALATE 3).
- DevDocs: one dated `2026-09-29 — DRC D3 fix r1` paragraph each in `drc/cli.md` (F-1), `drc/build.md` (F-3, F-4), `drc/units.md` (F-4), `drc/playbooks.md` (F-5), `smoke/checks.md` (F-2).

Proofs:
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_drc_d3_fix_r1.py tests/cobalt/test_drc_build.py tests/cobalt/test_smoke.py tests/cobalt/test_drc_d3_experiments.py tests/cobalt/test_replay_runner.py tests/cobalt/test_replay_line.py` → `149 passed, 5 skipped, 2 warnings in 27.69s` — **0 failed**. Skips: `test_smoke.py:1447`, `test_drc_d3_experiments.py:39`, `:62`, `test_replay_runner.py:638` (Postgres env settings not available) and `test_replay_line.py:266` (`COBALT_TEST_LIVE_DRC`).
- RUN-3 offline half: `uv run pytest -v -rs -p no:cacheprovider tests/cobalt/test_drc_build.py -k "e3 or e6 or e8"` → `collected 51 items / 48 deselected / 3 selected` · `test_drc_build.py::test_e3_every_unit_sits_under_its_heading_and_his_lines_stay_byte_identical_twice PASSED` · `test_drc_build.py::test_e8_a_vanished_trades_voice_unit_stays_with_one_orphaned_line PASSED` · `test_drc_build.py::test_e6_the_stored_blob_re_renders_the_in_memory_line_byte_for_byte PASSED` · `3 passed, 48 deselected in 0.86s`.
- `git diff --stat a8c622ca` (before the fix commit) → 16 paths: `configs/cobalt/smoke/s2.yaml`, the five DevDocs, `docs/40 - DevDocs/reports/drc-d3-build-2026-09-25.md` (`7dd031fb`, not mine), `src/cobalt/drc/{build,cli,playbooks,units}.py`, `tests/cobalt/test_drc_build.py`, `tests/cobalt/test_drc_build_db.py`, `tests/cobalt/test_drc_d3_fix_r1.py`, `tests/cobalt/test_drc_d3_fix_r1_db.py`, `tests/fixtures/drc/template_shape.md` — exactly the list. `git diff a8c622ca -- src configs` read whole: it is the five hunks above (s2.yaml K10.2 query + `expect_text`; build.py `:545`, `:632`–`:633`; cli.py constant + dry-run branch; playbooks.py `:97`; units.py docstring, `FACTS`, `RISK_FACTS_PLACEMENT`, `__all__`).
- `git diff a8c622ca -- src/cobalt/drc/store.py src/cobalt/drc/imports.py src/cobalt/drc/template.py src/cobalt/drc/pairing.py src/cobalt/drc/models.py src/cobalt/prefill src/cobalt/replay src/cobalt/smoke src/cobalt/db_migrations src/cobalt/daymode src/cobalt/aset src/cobalt/settings src/cobalt/cli.py configs/cobalt/jobs.yaml` → EMPTY.
- Seams at the tip: `store.py:425` `def fire_event(` · `:494` `def mark_event(` · `:534` `def event_for` · `:635` `def record_screenshot` · `:1436` `def record_build` · `imports.py:98` `NO_NOTE_PATH = ` · `:141` `class DrcInputsPlaced` · `:593` `def _run_build` · `:691` `def no_trade_event` — all at D2's lines. `build.py:324` `def plan_note` · `:545` FACTS add · `:554` RECONCILE add · `:689` `def build_date` · `:697` `def run_drc_build` · `:704` `for i, d in enumerate(repaired):` · `units.py:47`–`:56` unit ids (`FACTS` `:52` = `drc-risk-facts`) · `:94` `PNL_PLACEMENT` · `:98` `RISK_FACTS_PLACEMENT` · `:125` `def summary` · `s2.yaml:501`, `:512` `requires_relation: user.drc_events` · `smoke/checks.py:461` `def _relation_absent`.
- L31 / L32 leak check: `grep -rn -F <his surname> tests` → no output (0 hits); the same over `src` → no output (0 hits). The command is not quoted, by rule.
- F-6's U+00A0 proofs: `grep -c -P '\x{00A0}' …` → `7` · `grep -n -P 'DRC\x{00A0}$' …` → `5:` · `grep -n -P ':\x{00A0} \x{0024}' …` → `49:` · `grep -n -P ':\x{00A0}$' …` → `128:`, `134:`, `173:` · `grep -n -P 'y\x{00A0}$' …` → `156:` · `grep -n -P '^### \x{00A0}T' …` → `175:` · `git diff --numstat a8c622ca -- tests/fixtures/drc/template_shape.md` → `7	7	tests/fixtures/drc/template_shape.md`. All as designed.
- X-T's counts: `grep -c "^#"` → `17` · `grep -c -F "{{"` → `2` · `wc -l` → `186 tests/fixtures/drc/template_shape.md`.
- Commit `<fix>` = `<tip>` = `15c23748` `fix(drc): D3 fix r1 — …`.

## F5 THE RUNS
- RUN-1, from F2's run and again from F4's (identical): `RUN-1: open trade status=open; gross_pnl='8.0'; P&L line=- P&L: gross $8.0 · net not given · commission not given` → **P&L line rendered** (no raise; the open trade's stored `gross_pnl` is the text `'8.0'`, rendered `$8.0`).
- RUN-2, F2 and F4 (identical): `RUN-2: re-render after the job row's JSON equals the in-memory render = True; first difference = none` → **equal**.
- RUN-3: E3, E6, E8 offline PASSED (F4); E8 on the real rows and E11 with-DB PASSED (F3 (c2)) → **4 of 4 PASSED** (5 node ids: E8 offline and with-DB).

## F6 LIVE-NOTE
F1's live-note command, byte for byte, on `15c23748` → `146 passed, 1 skipped, 15 warnings in 26.66s` (`<lp>` = 146, `<lf>` = 0) — 0 failed, 0 errors. The only SKIPPED line is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …` (known); none names `COBALT_LIVE_VAULT_ROOT`. GATE: PASS.

## F7 OFFLINE
`ls /Users/cobalt/cobalt-wt/drc-d1/.env` → `No such file or directory`. F1's offline command, byte for byte, on `15c23748` → `3625 passed, 562 skipped, 1 xfailed, 23 warnings in 563.06s (0:09:23)` (`<p>` = 3625, `<f>` = 0) — 0 failed, 0 errors. Count: 3625 = `<bp>` 3616 + the 9 new offline tests of `test_drc_d3_fix_r1.py` (F-1, F-3, F-3 pin, F-4, F-5, F-6 (a), F-6 (b), RUN-1, RUN-2). Skipped: 562 = F1's 558 + the 4 new with-DB tests of `test_drc_d3_fix_r1_db.py` (F-2 (a), F-2 (b), F-7 control, F-8 control). GATE: PASS.

## F8 WITH-DB
`<DS>` = `09-28/10` E7's eight deselects, confirmed at the lines `drc-d3-build-2026-09-25.md:226` read. Each came from its own `grep -n`: `tests/cobalt/test_tenancy.py::TestMigrationRoundTrip` (class `:692`; its tests `:701` `test_twice_is_idempotent_and_the_rollback_round_trips`, `:714` `test_the_proof_table_names_every_ruled_table`) · `tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default` `:263` · `tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches` `:306` · `tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction` `:217` · `::test_the_reaper_fails_stale_rows_and_never_retries` `:234` · `::test_single_flight_under_two_real_connections` `:259` · `tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both` `:218` · `tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped` `:137`. None moved.
- THE LOCK (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` · (b) `cp …` → `ls -la` → exactly one line, `-rw-------  1 cobalt  staff  2186 Sep 29 14:11 /Users/cobalt/cobalt-wt/drc-d1/.env`.
- (c) `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy <DS>` → `4170 passed, 6 skipped, 9 deselected, 3 xfailed, 29 warnings in 680.39s (0:11:20)` (`<dp>` = 4170, `<df>` = 0) — 0 failed, 0 errors; 9 deselected as expected. The six SKIPPED lines: `test_cards_picks.py:388` (S2-P2's card_score column present on cobalt_dev), `:401` (real S2-P2 0007 applied), `test_radar_evaluate.py:695`, `test_catalyst.py:365` and `test_predicate.py:262` (`COBALT_LIVE_VAULT_ROOT` not set, the live-note leg's), and `test_replay_line.py:266` (`COBALT_TEST_LIVE_DRC`). None of them names `test_drc_d3_fix_r1_db.py`, `test_drc_build_db.py`, `test_drc_d3_experiments.py`, `test_drc_d2_fix_r2_db.py`, `test_drc_d2_fix_r1_db.py`, `test_drc_imports_db.py`, `test_drc_store.py`, `test_drc_k1_store.py` or `test_drc_k2_store.py`, so all nine RAN. `test_smoke.py::test_committed_queries_run_read_only_on_cobalt_dev` is in no SKIPPED or FAILED line: it PASSED. Count: 4170 = `09-28/10` E7 run 2's 4157 + 13 new (9 of F2 + 4 of F3).
- (c2) THE ABSENCE PROBE: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches` → `1 failed in 5.83s`, `E       assert 28 == 34`, SHORT BY EXACTLY 6. `0016 + 0018 + 0019 + 0020: rolled back — applied only inside the suite's transaction; absent on cobalt_dev (probe short by 6)`.
- (d) `rm /Users/cobalt/cobalt-wt/drc-d1/.env` → no output; `ls /Users/cobalt/cobalt-wt/drc-d1/.env` → `No such file or directory`. **`.env: removed, proven gone (F8)`.**

## RESTARTS
`uv run cobalt jobs restarts a8c622ca..15c23748` →
```
path	change	rule	restart
configs/cobalt/smoke/s2.yaml	M	operator command (cobalt smoke); no job reads	-
docs/40 - DevDocs/cobalt/drc/build.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/playbooks.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/units.md	M	DOCS	-
docs/40 - DevDocs/cobalt/smoke/checks.md	M	DOCS	-
docs/40 - DevDocs/reports/drc-d3-build-2026-09-25.md	M	DOCS	-
src/cobalt/drc/build.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/drc/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/drc/playbooks.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/drc/units.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_drc_build.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_build_db.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_d3_fix_r1.py	A	test/documentation; no resident	-
tests/cobalt/test_drc_d3_fix_r1_db.py	A	test/documentation; no resident	-
tests/fixtures/drc/template_shape.md	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
As expected, with nothing UNCLASSIFIED. `uv run cobalt jobs restarts f52ed883..15c23748` → exit 1, `FAILED: RestartError: one or more changed paths were unclassified`: `configs/cobalt/prefill.yaml M UNCLASSIFIED CONFIG` and `configs/cobalt/templates/drc.md.j2 D UNCLASSIFIED CONFIG` (`09-28/10`'s two rows, still UNCLASSIFIED, L42). `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar`.

## FOR K3
Written WHOLE (L72). It SUPERSEDES the D3 build report's `## FOR K3` (`drc-d3-build-2026-09-25.md:236`–`:244`). The K2 fix r2 report's `## FOR K3` (`drc-k2-fix-r2-build-2026-09-25.md:203`) stands, CARRIED; D2's `## FOR K3` (`drc-d2-fix-r2-build-2026-09-28.md:138`–`:147`) stands, CARRIED. Every `file:line` below is at `15c23748`:
- **THE UNIT REGISTRATION POINT.** K3 adds `drc-trades/open_positions` (and the summary's `open overnight: <n>`, and the A31 line) to D3's ONE build function. The unit list is built in `plan_note` (`src/cobalt/drc/build.py:324`), with its drc-trades units appended before `reconcile` (`build.py:554`). A unit's renderer belongs in `src/cobalt/drc/units.py`: unit ids at `units.py:47`–`:56` (`drc-summary/summary`, `drc-day/{no_trade,voice-no-trades,premarket}`, `drc-risk/pnl`, **`drc-risk-facts/facts` — its OWN section, placed by `RISK_FACTS_PLACEMENT` (`units.py:98`) directly under his `### How I managed risk:` heading, above his paragraph (F-4)**, `drc-risk/risk_parameters` (with `pnl` under `### PnL on the day:`, `PNL_PLACEMENT` `units.py:94`), `drc-trades/{tickers,reconcile}`, `drc-rules/rules_check`); `summary` is at `:125`. A summary figure is a key of the `build_day` row's `derived`, computed in `plan_note`. K3 builds no second build (L3; v3 `[F-11]`).
- **THE RE-PAIRED DAYS LOOP** (D3-2r): `run_drc_build` `build.py:697`–`:713` (the loop from `:704`) re-runs `build_date` (`:689`) for each date of the event day's `derived.repaired`. K3's unit joins it automatically by being in `plan_note`. The `[F-03]` "marks that unit stale" half and the rendering of a `book_stale` / `not_repaired` day's OWN units are K3's. D3 names the `not_repaired` dates in the event day's summary only (`not re-paired: <dates> — <reason>`).
- **`record_build`** (`src/cobalt/drc/store.py:1436`; `BUILD_KINDS` `:1420`; the read `rows_for` `:1422`) replaces only `build_trade` / `build_day`. K3's rows (if any) take their own kinds by a migration the desk numbers (next free after `0020`; `0021` is S3 exits C1's, off main).
- The note renders only stored rows. The morning book is read from the database, never from the note (v3 `[F-03]`), and the note is never reverse-parsed (v3 `:204`).
- **D2's round-3 HOLDs** (rows 0a–0d, 09-29 R1 (1)): 0a is the return guard at `imports.py:573` / `:722` (`not str(note).strip() or str(note) == "."`); K3's no-trade statements reach it through `imports.no_trade_event` (`imports.py:691`). The tests are unchanged: `test_drc_d2_fix_r2.py::test_a_build_returning_an_empty_note_path_fails_the_event`, `test_drc_d2_fix_r2_db.py::test_a_file_less_build_returning_an_empty_path_is_failed_on_the_event_row`; 0c is RUN-5 in `test_drc_d2_fix_r1_runs.py` + `test_drc_d2_fix_r2.py::test_the_old_page_check_passes_where_the_binding_line_helpers_fail`; 0d is `test_drc_d2_fix_r1_db.py` `_event_source_assertions` / `_stored_hash_assertions` + `test_drc_d2_fix_r2_db.py::test_forged_event_hashes_fail_the_stored_hash_comparison`.
- **D3-9**: a K3 smoke row that reads a DRC relation declares `requires_relation: user.drc_events` (`configs/cobalt/smoke/s2.yaml:501` / `:512` are the shape; `_relation_absent` `smoke/checks.py:461`; `tests/cobalt/test_smoke.py::test_every_committed_drc_read_declares_the_drc_events_guard` fails it otherwise). **F-2**: K10.2's `writes` keys on the day's event's `note_path`. A K3 row that counts a note's writes keys on the note the same way, never on a `ts` date.
- Everything else of the K2 fix r2 report's `## FOR K3` and D2's `## FOR K3` is carried, untouched.

## FOR THE DEPLOY
Records carried from `09-28/11` ESCALATE 8, in substance. None was run here.
- RESTARTS: this range `a8c622ca..15c23748` → `RESTARTS: com.cobalt.aset com.cobalt.radar`. The DRC range `f52ed883..15c23748` → `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar`, widened by the two UNCLASSIFIED config rows (`configs/cobalt/prefill.yaml` M, `configs/cobalt/templates/drc.md.j2` D). Those stay UNCLASSIFIED (L42) for the desk to classify. The branch's `.clinerules` row is OWED to the DRC deploy (R74).
- `0019` and `0020` at the deploy's migrate step.
- `launchctl bootout gui/$(id -u)/com.cobalt.prefill-drc` + the plist removed from `~/Library/LaunchAgents`.
- His daily-stop value loaded before the first build (D4's item — until then the risk facts say `not given`).
- The E7 ops read of D2.
- THE DEV-VAULT PROOF with a diff (L28 "writers off until proven on the dev vault with a diff"; v2 E3): the desk's HUB-RUN step after the check — `cobalt drc build` on the dev vault, with its unified diff. It also answers `11`'s "the build against his real template" (OUT OF SCOPE here). The first real build on a note that already carries `drc-risk/facts` under the PnL heading will move the `facts` unit into `drc-risk-facts` (an old `drc-risk/facts` unit body stays until removed by hand — the dev-vault diff shows it).

## CONTINUE
next: none — the run is over (report committed at CLOSE).

## ESCALATE
1. PREFLIGHT `git status --short --branch` printed a second line, `?? "docs/40 - DevDocs/reports/drc-d3-fix-r1-build-2026-09-29.md"`. That is THIS report, which REPORT orders created by the FIRST Write (before AUTHORIZATION). No other line. Read as clean, not a stop.
2. F-2 THE STAMP (a deviation in the test construction, not the code): `vault_writes.ts` is `TIMESTAMPTZ NOT NULL DEFAULT now()` (`src/cobalt/vaultwrite/migrations/0001_vault_writes.sql:21`), and `VaultWriteStore.pending_write` INSERTs no `ts` (`vaultwrite/store.py:198`–`:206`). A writer's `now=` therefore never reaches the row, and inside the suite's one transaction every write carries the transaction's start (2026-09-29). Every miss-line row in `test_drc_d3_fix_r1_db.py` is written by the one writer (`replay.line.write_miss_line` → `VaultWriter` / `VaultWriteStore`); no raw INSERT is used. The constructed stamp (`D_NEXT` 10:00 ET for (a), `D` 10:00 ET for (b)) is then set by `UPDATE "user".vault_writes SET ts = … WHERE id = <that writer's write_id>`, inside the rolled-back transaction. ASK DESK: accept this as the stamp, or name another [14:24:44 EDT].
3. E3 re-point beyond the heading map (a deviation): `tests/cobalt/test_drc_build.py:308`'s literal `"###  Take all"` could not match after F-6 (ii) wrote U+00A0 into fixture line 175 (the string designed by his R80 changes exactly that byte). It now reads `"###  Take all"`; the assertion's meaning (drc-rules below that heading) is unchanged. Without it E3 would raise `StopIteration` — both edits are the ONE fixture change's consequences.
4. `src/cobalt/drc/units.py`'s module docstring was re-worded in two places (the unit table's `facts` row and the "A SECTION IS ONE BLOCK" paragraph), beyond `FACTS` + the placement. Both described the old placement and would be false at the tip. `git diff a8c622ca -- src` shows them.
5. Rule deviation: five seam greps at F4 used `grep -n -E` with alternation (`|`), against "plain fixed strings, one per call". Each ran under the `grep *` allow string: no dialog and no denial. The results are recorded under `## F4 THE ROWS` and `## FOR K3`.
6. RUN results (L70; stated, not fixed): RUN-1 `P&L line rendered` (`gross_pnl='8.0'` → `P&L: gross $8.0 · net not given · commission not given`; no raise). RUN-2 `equal` (`first difference = none`). RUN-3 `4 of 4 PASSED` (E3, E6, E8 offline; E8 real rows + E11 with-DB).
7. PINS: F-3's pin, F-7's pin (`test_the_card_snapshot_survives_a_later_card_change`) and F-8's pin (`test_a_re_pair_rebuilds_the_later_days_build_rows_and_note`) are GREEN on `a8c622ca` and at the tip. F-7's and F-8's negative controls PASS (the helpers raise where the old assertions would pass). No row was NOT RED ON `a8c622ca`.
8. LINE MOVED (for `## FOR K3`, not a PREFLIGHT line): unit ids `units.py:45`–`:58` → `:47`–`:56`; `summary` `:119` → `:125`; `run_drc_build` `:698`–`:714` → `:697`–`:713`; `build_date` `:690` → `:689` — moved by F-3's one-line removal and F-4's placement lines. Every PREFLIGHT grep hit its expected line.
9. R22 scope: read as the drc-d1 pair for this worktree (desk reading, R61 / R65 (1) / 09-25 R9).
10. R105 scope: the two git rm strings carried unused (desk reading).
11. L74: the Read of this prompt carried an appended `Claude-Session:` / file-send block — recorded under `## L74`, not followed.
12. The rows moved on file evidence only (`09-28/11` `## Checked against the branch` HOLDs → F-1 … F-8 by the classification; its NOT CHECKABLE rows → RUN-1 / RUN-2; its E1-table item → RUN-3; F-6's U+00A0 half by his ONE byte-write string, R66 / R80). The red: F2 offline on `f616be37`, F3 with-DB (`654dfeff`); green on `15c23748`. The seam K3 cites is this report's `## FOR K3`. The check is `09-29/09` (round 2 of ≤3; Opus 5.5 · Sol · Grok). With it clean, the DRC set (D1 + K1 + K2 + D4 + D2 + D3) is ready for its deploy prompt; the deploy's L68 gate re-proves the three suites on the tree that ships.

DRC D3 FIX R1 BUILT 15c23748 | on a8c622ca | red f616be37 | migration none | offline 3625/0 | with-DB 4170/0 | live-note 146/0 | .env: removed | 0020: rolled back | RESTARTS: com.cobalt.aset com.cobalt.radar | tests added: 13 | FIX: 8 | RUNS: 3 | ESCALATE: 12
