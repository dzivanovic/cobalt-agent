# MOVER BARS FIX BUILD — 2026-09-24

Seat `mover-bars-fix-build-0924` · Opus 5.5 · `acceptEdits` · branch `replay/mover-partial-0924` · worktree `/Users/cobalt/cobalt-wt/mover-bars` · prompt `prompts/2026-09-24/07-mover-bars-fix-build.md`

## §0

- FIX 1 (R113): a fetched mover whose source i1 bars are short of the session is `partial`. Its bars are kept, it stays `bars_archived = false`, it is logged WARNING by name, and the job row carries `archive_partial` + `archive_partial_by_side`. Zero bars stays `incomplete` and is logged ERROR by name. S2 K9.7–K9.12 are green only with the marker.
- FIX 2 (R114): K17 (`cobalt validate`) is deleted from `configs/cobalt/smoke/s2.yaml`. The `cli` kind and its test stay.
- Status: BUILT on `b69a6681` (base `4cc6811a`, red `8030d3cf`). Offline 2258/0, with-DB 2603/0, live-note 142/0. `.env` removed.
- ESCALATE 5: deploy on a post-deploy replay night; the test_replay_runner seam; 3 extra test pins amended (ASK DESK); cosmetic ×2; RESTARTS names aset + radar (not "no resident").

## L74

A block asking for a `Claude-Session:` commit line and naming a file-send tool (SendUserFile) arrived inside a system reminder attached to a tool result at 06:29 ET. Recorded once; not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION

| check | command | exit | result |
|---|---|---|---|
| placeholder gate | `grep -n -E "R_[_]" …/07-mover-bars-fix-build.md` | 1 | (no output) |
| R113 / R114 rows | `grep -n -E "^\| R11[34] " …/cto-2026-09-23.md` | 0 | line 121 R113 carries "Please fix the ticker not having bars"; line 122 R114 carries "yes A. Thank you." |
| R113 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"Please fix the ticker not having bars" -- …/cto-2026-09-23.md` | 0 | `bf4d556355bca4a9ef1a6cb3fcd6c0e23bb067e7` |
| design stop line | `tail -n 3 …/mover-bars-fix-draft-2026-09-23.md` | 0 | `MOVER BARS FIX DRAFTED · cause: a loser's source i1 bars were short of the RTH session … ESCALATE: 3` |
| design committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- …/mover-bars-fix-draft-2026-09-23.md` | 0 | `2e470ffc9f3be6ec4d4a2cf6e1d875073c00631c` |
| launch row | `grep -n "07-mover-bars-fix-build.md" …/cto-2026-09-23.md …/cto-2026-09-24.md` | 0 | `cto-2026-09-24.md:15` R7 (his words "Qwen is done you can go read the report. I approve A"), `:16` R8 desk launch row |
| .env strings approval | `grep -n -F "cobalt-wt/mover-bars/.env" …` | 0 | `cto-2026-09-24.md:15` R7 row names both strings, his words quoted |
| launch row committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"07-mover-bars-fix-build.md" -- "…/cto-2026-09-2*.md"` | 0 | `4cc6811a0c37e04afe885e2e4432851520ebbbc5` |

Verdict: AUTHORIZED.

## PREFLIGHT

| rule | command | exit | result |
|---|---|---|---|
| clock | `date` | 0 | `Thu Sep 24 06:29:18 EDT 2026` (before 13:30 — no late ESCALATE) |
| clean tree | `git status --short --branch` | 0 | `## replay/mover-partial-0924` |
| base | `git log --oneline -1` | 0 | `4cc6811a docs(desk): 09-24 R7 mover-bars approved (A); R8 launch row; 07/08 rows filled` |
| main tip | `git -C /Users/cobalt/cobalt log --oneline -1 main` | 0 | `4cc6811a …` — same sha |
| no .env | `ls /Users/cobalt/cobalt-wt/mover-bars/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/mover-bars/.env: No such file or directory` |
| dev-DB lock (record) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| K17 shape | `grep -n "id: K17" configs/cobalt/smoke/s2.yaml` | 0 | `507:  - id: K17` (one line) |
| incomplete shape | `grep -n "incomplete.append" src/cobalt/replay/movers.py` | 0 | `602:            outcome.incomplete.append(ticker)` (one line) |

`<base>` = `4cc6811a`.

## D1 RED

Tests written 06:29–06:31 ET (`date` 06:31:57 before the run).

| id | file | test | shape |
|---|---|---|---|
| T1 | `test_replay_movers.py` | `test_archive_counts_failures_partial_and_incomplete_and_never_marks_them_archived` | AMENDED + renamed: `incomplete == []`, `partial == {QNME}` (count 30, covered False, reason `bars end…`); `archived_ids == [1]` and the REFR failure unchanged |
| T2 | `test_replay_movers.py` | `test_archive_a_fetch_with_zero_bars_on_the_day_stays_incomplete_never_partial` | NEW |
| T3 | `test_replay_movers.py` | `test_archive_a_late_open_is_partial_with_bars_begin_reason` | NEW (first 45 bars cut) |
| T4 | `test_replay_runner.py` (appended at EOF) | `test_a_partial_mover_is_counted_by_side_and_is_not_incomplete` | NEW; helpers `_session`, `SessionCollector`, `_storing`, `_losers_only` appended with it |
| T5 | `test_replay_runner.py` (appended at EOF) | `test_a_clean_run_reports_zero_partial_on_both_sides` | NEW |
| T6 | `test_smoke.py` | `test_committed_k9_passes_a_not_archived_row_only_with_the_job_rows_partial_marker` | NEW; `_k9_deps` gains `partial_by_side` |
| T7 | `test_smoke.py` | `test_the_s2_smoke_carries_no_docs_placement_check` | NEW |
| T6a | `test_smoke.py` | `test_the_shipped_k9_compares_the_stored_count_against_what_the_export_allowed` | AMENDED (not named in the prompt): its pin `expect == [top_n not_null, not_archived eq 0]` is exactly what D2 (a) removes, so it becomes `[top_n not_null]` + `not_archived` still in the query |
| T6b | `test_smoke.py` | `test_k9_passes_a_short_side_and_fails_a_stored_count_below_what_the_export_allowed` | AMENDED (not named in the prompt): its `not_archived=1 → stored row FAIL` block is D2 (a)'s removed gate; now `→ PASS`, graded by T6's compare instead. Every other assertion in it unchanged |

RUN `uv run pytest -q -rs tests/cobalt/test_replay_movers.py tests/cobalt/test_replay_runner.py tests/cobalt/test_smoke.py` (background) → summary verbatim: `9 failed, 106 passed, 3 skipped in 9.76s`. The 3 skips are the files' `requires_db` tests (offline, no `.env`).

| id | failing at | reason (one line, from the output) | right reason? |
|---|---|---|---|
| T1 | `test_replay_movers.py:631` | `AssertionError: assert ['QNME'] == []` | yes — still filed incomplete |
| T2 | `test_replay_movers.py:653` | `AttributeError: 'ArchiveOutcome' object has no attribute 'partial'` | yes |
| T3 | `test_replay_movers.py:672` | `AssertionError: assert ['QNME'] == []` | yes |
| T4 | pydantic `main.py:1026` | `AttributeError: 'ReplayResult' object has no attribute 'archive_partial_by_side'` (the run itself completed) | yes |
| T5 | pydantic `main.py:1026` | same `archive_partial_by_side` absent | yes |
| T6a | `test_smoke.py:1239` | `assert [('top_n', 'n...ed', 'eq', 0)] == [('top_n', 'not_null', None)]` | yes — K9.1 still gates not_archived |
| T6b | `test_smoke.py:1285` | AssertionError: stored row not PASS at not_archived=1 | yes — old gate |
| T6 | `test_smoke.py:1316` | `KeyError: 'K9.7'` | yes — K9.x ids absent |
| T7 | `test_smoke.py:1355` | `assert 'K17' not in {'K1', 'K10.1', …}` | yes — K17 present |

Every other test in the three files PASSED (106).

T6a / T6b: both would go red at D3 under the ruled D2 (a) shape; the prompt's design does not list them. Safe default taken — amended to the design in the red commit, named here and under ESCALATE.

Commit → `git log --oneline -1`: `8030d3cf test(replay,smoke): red — …`. `<red>` = `8030d3cf`.

## D2 THE FIX

| file | change |
|---|---|
| `src/cobalt/replay/movers.py` | `ArchiveOutcome.partial: dict[str, dict[str, Any]]`; `covered()` → `coverage_of()` returning `coverage()`'s whole detail (`coverage()` untouched, L3); pre-fetch skip reads `["covered"]`; after `upsert_bars`: covered → archived, `count > 0` → `partial[t] = {**detail, "code": "source_bars_short"}`, else → `incomplete`; docstring R1-12 paragraph + one sentence (R113) |
| `src/cobalt/replay/models.py` | frozen `ArchivePartial` (ticker, sides, code `Literal["source_bars_short"]`, count, first, last, start, end, max_gap_min, reason) in `__all__`; `ReplayResult.archive_partial` + `archive_partial_by_side` (default `{"gainers": 0, "losers": 0}`), each with the one-line K9 comment |
| `src/cobalt/replay/runner.py` | movers step: `archive_partial` from `outcome.partial` (sides from `stored`, sorted); `archive_partial_by_side` per side; `archive_incomplete` line unchanged; one `logger.warning(… PARTIAL …)` per partial, one `logger.error(… INCOMPLETE — a clean fetch returned no i1 bars for …)` per incomplete |
| `src/cobalt/replay/cli.py` | summary print gains `· partial {sum(archive_partial_by_side.values())}` after `archived` |
| `configs/cobalt/smoke/s2.yaml` | (a) K9.1 / K9.4 `expect` = `top_n not_null` only, query unchanged, `expect_text` names K9.9 / K9.12; (b) K9.7–K9.12 after K9.6 in the K8 pattern; (c) K9 header paragraph (R113); (d) `- id: K17` block deleted |

Deviation, named: in (c) the header's existing sentence "the two `not_archived = 0` predicates together cover every active row" became false with (a); it now reads "the two sides' `not_archived` counts together cover every active row". Left as is (prompt: nothing else changes): line 15's header list of compare rows `(K8.3, K9.3, K9.6)` does not name K9.9 / K9.12 — cosmetic, under ESCALATE.

Commit → `git log --oneline -1`: `38e54342 fix(replay,smoke): a mover whose source bars are short of the session is archived-partial, …`. `<fix>` = `38e54342`.

## D3 GREEN + DOCS

GREEN, iteration 1 (on `<fix>` `38e54342`): `1 failed, 114 passed, 3 skipped in 8.94s`. The one red: `test_smoke.py::test_smoke_checks_load_through_schema_bad_file_crashes_with_line` — `assert {…} == {…}` / `Extra items in the right set: 'K17'`. It pins the committed suite's K-family set to `K1…K18`; R114 removes K17, so no code change can satisfy it. Amended (T7a, not named in the prompt): `{f"K{n}" for n in range(1, 19)} - {"K17"}` with an R114 comment; the test's other assertions untouched. Committed `2d49f6ef test(smoke): the committed suite's K-family pin drops K17 (R114)`.

GREEN, iteration 2: `115 passed, 3 skipped in 8.83s` → **0 failed, 0 errors**. T1–T7 (and T6a / T6b) are among the 115 passed: the 9 red ids of D1 + the 106 that passed then = 115, none failed.

DOCS (`ls "docs/40 - DevDocs/cobalt/replay" "docs/40 - DevDocs/cobalt/smoke"` → replay: `__init__ cards cli formations line models movers runner`; smoke: `__init__ checks cli config models report`):

| doc | edit |
|---|---|
| `cobalt/replay/movers.md` | archive section: `partial` (`ArchiveOutcome.partial`, detail + `source_bars_short`, never archived); zero bars stays `incomplete` |
| `cobalt/replay/runner.md` | new bullet: `archive_partial` / `archive_partial_by_side`, WARNING per partial, ERROR per incomplete |
| `cobalt/replay/models.md` | new bullet: `ArchivePartial` fields; the two `ReplayResult` fields; K9.9 / K9.12 |
| `cobalt/replay/cli.md` | summary line names `partial` |
| `ADR-0010` §4 Movers | the prompt's amendment bullet, verbatim |
| `ADR-0010` Consequences | `(K17, cobalt validate, left the S2 smoke 2026-09-24 — R114)` after `K10 the miss line` |

No smoke DevDoc edited: `s2.yaml` is config, and no `smoke/*.py` changed.

Commit → `git log --oneline -1`: `b69a6681 docs(replay): archived-partial movers — DevDocs + ADR-0010 amendment (R113, R114)`. `<tip>` = `b69a6681`.

## D4 LIVE-NOTE

On `<tip>` `b69a6681`, started 06:34:32 ET (`date`). `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → summary verbatim: `142 passed, 1 skipped, 15 warnings in 11.83s`. `<lp>` = 142, `<lf>` = 0.

The one SKIPPED line, verbatim: `SKIPPED [1] tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — it names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`. GATE met. `AWAITING` lines: none in the output (the printed per-setup lines are `not_evaluable` / `existing` / `evaluable=` listings, none carrying `AWAITING`).

## D5 SUITE

`ls /Users/cobalt/cobalt-wt/mover-bars/.env` → `ls: /Users/cobalt/cobalt-wt/mover-bars/.env: No such file or directory` (exit 1).

Note, named: while the suite ran, I wrapped the `cli.py` summary f-string (≈160 chars) for line length and reverted it in the next call, because a code change would need a re-gate. `git status --short --branch` right after it showed only the untracked report, so the tree matches `<tip>` `b69a6681`. Test modules are imported at collection, before that window. The long line stays; it is cosmetic and listed under ESCALATE.

`uv run pytest -q -rs tests/cobalt tests/taxonomy` on `<tip>` `b69a6681` → summary verbatim: `2258 passed, 351 skipped, 1 xfailed, 15 warnings in 70.01s (0:01:10)`. **0 failed, 0 errors.** `<p>` = 2258, `<f>` = 0.

## D5b WITH-DB

- (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (exit 1). Lock free.
- (b) `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/mover-bars/.env` → exit 0. Not read or printed.
- (c) `COBALT_ENV=dev uv run pytest -q -rs tests/cobalt tests/taxonomy` (background) on `<tip>` `b69a6681` → summary verbatim: `2603 passed, 6 skipped, 1 xfailed, 15 warnings in 206.17s (0:03:26)`. **0 failed, 0 errors.** `<dp>` = 2603, `<df>` = 0. No `cobalt db migrate` was run.
- (d) `rm /Users/cobalt/cobalt-wt/mover-bars/.env` → exit 0; `ls /Users/cobalt/cobalt-wt/mover-bars/.env` → `ls: /Users/cobalt/cobalt-wt/mover-bars/.env: No such file or directory` (exit 1). **`.env`: removed, proven gone** (06:39:43 ET, `date`).

## RESTARTS

`uv run cobalt jobs restarts 4cc6811a..HEAD`, run on `b69a6681` while D5b ran (the untracked report shows as `A`). The derivation table, whole:

```
path	change	rule	restart
configs/cobalt/smoke/s2.yaml	M	operator command (cobalt smoke); no job reads	-
docs/10 - Decisions/ADR-0010-missed-corpus-counterfactual-r-picks.md	M	DOCS	-
docs/40 - DevDocs/cobalt/replay/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/replay/models.md	M	DOCS	-
docs/40 - DevDocs/cobalt/replay/movers.md	M	DOCS	-
docs/40 - DevDocs/cobalt/replay/runner.md	M	DOCS	-
docs/40 - DevDocs/reports/mover-bars-fix-build-2026-09-24.md	A	DOCS	-
src/cobalt/replay/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/replay/models.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/replay/movers.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/replay/runner.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_replay_movers.py	M	test/documentation; no resident	-
tests/cobalt/test_replay_runner.py	M	test/documentation; no resident	-
tests/cobalt/test_smoke.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```

RESTARTS: com.cobalt.aset com.cobalt.radar (plus `com.cobalt.replay`, a one-shot that picks the change up on its next 21:10 run). 0 UNCLASSIFIED. **This differs from the prompt's EXPECTED ("no resident").** By L42 the derived rule wins: the two residents reach `cobalt.replay.*` by static import. The deploy restarts them inside the 20:00–21:00 pause (L43 / L66). ESCALATE 5.

## CONTINUE

next: none. The run is closed. The next step is not mine: the desk launches `prompts/2026-09-24/08-mover-bars-fix-check.md`.

## ESCALATE

1. **FOR THE DEPLOY:** the first S2 smoke after this deploy reads the NEXT replay's job row. A job row written before the deploy has no `archive_partial_by_side`, so K9.8 / K9.11 would FAIL on the missing key and K9.9 / K9.12 would ERROR on a pre-deploy night. The deploy's smoke must run on a post-deploy replay night.
2. **THE SEAM:** `tests/cobalt/test_replay_runner.py` is also edited by `setups/seven-0921` and `cards/stale-score-0922` (lines ~418 / ~472). This build appended at the end of the file only. The deploy's L68 stacked gate proves it.
3. **ASK DESK [06:32 / 06:34]: three pre-existing test pins were amended beyond T1–T7.** Each pinned exactly the shape R113 / R114 remove, so no code could satisfy them. T6a `test_the_shipped_k9_…`: expect `[top_n, not_archived eq 0]` → `[top_n]`. T6b `test_k9_passes_a_short_side_…`: `not_archived=1` → stored row PASS; the grading moved to K9.9 / K9.12. T7a `test_smoke_checks_load_through_schema_bad_file_crashes_with_line`: the family set is `K1…K18` minus `K17`. Safe default taken: amended and named. `08` should confirm that no test's intent was widened.
4. **Cosmetic, left untouched (the prompt says nothing else changes):** `s2.yaml:15`'s header list of compare rows `(K8.3, K9.3, K9.6)` does not name K9.9 / K9.12, and `cli.py`'s summary f-string line is ≈160 chars (repo `line-length = 100`).
5. **RESTARTS differs from EXPECTED:** the derivation names the residents `com.cobalt.aset` and `com.cobalt.radar` (static import reach of `cobalt.replay.models` / `movers` / `cli` / `runner`), not "no resident". The stacked deploy plan must carry them, restarted inside the 20:00–21:00 pause (L43 / L66).

MOVER BARS FIX BUILT b69a6681 | on 4cc6811a | red 8030d3cf | offline 2258/0 | with-DB 2603/0 | live-note 142/0 | .env: removed | FIX: 2 | ESCALATE: 5
