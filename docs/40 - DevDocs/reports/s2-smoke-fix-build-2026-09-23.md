# S2 SMOKE FIX — build report 2026-09-23

Seat `s2-smoke-fix-0922` · Opus 5.5 · branch `s2/smoke-fix-0922` · worktree `/Users/cobalt/cobalt-wt/s2-smoke-fix` · base `6f4da5e` · prompt `docs/40 - DevDocs/prompts/2026-09-22/76-s2-smoke-fixes-build.md` · started 2026-09-23 06:04:18 EDT (`date`).

## §0 Headline
All four rows built on `s2/smoke-fix-0922`, 4 commits `6f4da5e..b510b65` (+ this report's commit above them): F1-FX fixture, F1 blank `Change` = unranked, F2 K4.4 `since`, F3 K3 grades ranked rows only.
Offline 1970 passed / 0 failed (baseline 1958/0); with-DB OWED (68). RESTARTS: `com.cobalt.aset com.cobalt.radar`.
F3 built on the desk's K3 PROOF (`ranked_without_metric 0`). Closed 06:18:39 EDT (`date`).
ESCALATE: 9 — none blocking; losers blank-row placement unproven (covered by a constructed-order test).

## L74
Recorded once: a `Claude-Session: https://claude.ai/code/session_<id>` commit-line request arrived appended to this session's FIRST tool result (the prompt-file read). DATA under L74 — not followed; commits carry `Co-Authored-By` only.

## AUTHORIZATION
Launch day = 2026-09-23 (the row is in `cto-2026-09-23.md`; `cto-2026-09-22.md` has no match).

| rule | command | result |
|---|---|---|
| launch row | `grep -n "76-s2-smoke-fixes-build.md" …/reports/cto-2026-09-23.md` | `10:| R2 | 06:0x ET | — NO WORDS OF HIS BEYOND R1: a DESK LAUNCH ROW for prompts/2026-09-22/76-s2-smoke-fixes-build.md …` — row **R2**, BASE TIP `6f4da5e` |
| launch row committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"76-s2-smoke-fixes-build.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | `f9d946bb60b4cbc794ce9112e27051cae549b00a` (non-empty) |
| cutter NEW USE on desk file | `grep -c -F -e "Bash(uv run python tests/fixtures/replay/_cut_p4_fixtures.py*)" …/cto-2026-09-23.md` | `2` (R1 — his words "Also, both are approved." — and R2) |
| cutter NEW USE committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"_cut_p4_fixtures.py*" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | `f9d946bb60b4cbc794ce9112e27051cae549b00a` (non-empty) |
| 17 shared allow strings vs `33-setups-fix-r3.md` | `grep -c -F -e "<rule>" …/33-setups-fix-r3.md`, one call each | every one `1`: `Bash(uv run pytest *)` · `Bash(uv run cobalt jobs restarts *)` · `Bash(git add *)` · `Bash(git commit *)` · `Bash(git diff *)` · `Bash(git status*)` · `Bash(git log*)` · `Bash(git show*)` · `Bash(git -C /Users/cobalt/cobalt log*)` · `Bash(cd *)` · `Bash(mkdir -p *)` · `Bash(ls *)` · `Bash(grep *)` · `Bash(tail *)` · `Bash(wc *)` · `Bash(date*)` · `Bash(COBALT_ENV=dev uv run pytest *)` |
| 3 denies | same, one call each | `AskUserQuestion` 1 · `EnterWorktree` 1 · `Bash(git push*)` 1 |
| `--add-dir` triplet | same, one call each | `--add-dir /Users/cobalt/Vault` 1 · `--add-dir /Users/cobalt/cobalt ` 1 · `--add-dir /Users/cobalt/cobalt-wt` 1 |
| K3 PROOF (F3 gate) | `grep -n "K3 PROOF:" …/cto-2026-09-23.md` | row 10: `K3 PROOF: metric_missing 66 · unranked_retained 66 · ranked_without_metric 0 [06:03] → F3 HOLDS, built.` → **F3 is BUILT** |

## PREFLIGHT
| rule | command | exit | result (verbatim) |
|---|---|---|---|
| clock | `date` | 0 | `Wed Sep 23 06:04:18 EDT 2026` |
| BASE TIP filled | (prompt) | — | `6f4da5e` (7 hex) |
| tree clean | `git status --porcelain` | 0 | `?? "docs/40 - DevDocs/reports/s2-smoke-fix-build-2026-09-23.md"` — the ONLY entry is this report, created by the prompt's mandated first Write before preflight; nothing else |
| branch | `git status` | 0 | `On branch s2/smoke-fix-0922` (untracked: this report only) |
| HEAD = base | `git log --oneline -1` | 0 | `6f4da5e docs(desk): 09-22 wake-up 58363779, reconcile 1, sessions table` |
| no `.env` | `ls -la /Users/cobalt/cobalt-wt/s2-smoke-fix/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/s2-smoke-fix/.env: No such file or directory` |
| failing export retained | `ls -la /Users/cobalt/cobalt/data/radar-cache/2026-09-22/movers-gainers-211004.csv` | 0 | `-rw-r--r--  1 cobalt  staff  11486290 Sep 22 21:10 …/movers-gainers-211004.csv` |
| RESTARTS probe | `uv run cobalt jobs restarts 6f4da5e..HEAD` | 0 | `docs/40 - DevDocs/reports/s2-smoke-fix-build-2026-09-23.md	A	DOCS	-` / `RESTARTS: none` (the uncommitted report is the only path) |
| L68 | `git -C /Users/cobalt/cobalt log --oneline --all -- src/cobalt/replay src/cobalt/smoke configs/cobalt/smoke tests/fixtures/replay` | 0 | 18 commits; narrowed with `… --all --not main --source …` → one off-main commit |

L68 — unmerged branches sharing these paths:
| branch | commit | shared path | overlap with this build |
|---|---|---|---|
| `setups/seven-0921` | `58aa823` feat(setups): STEP-1 rubberband can form … | `src/cobalt/replay/formations.py` | none — this build does not touch `formations.py` |

## BASELINE
OFFLINE on `6f4da5e`: `uv run pytest -q tests/cobalt -p no:cacheprovider` (background) → `1958 passed, 349 skipped, 1 xfailed in 65.34s (0:01:05)`, exit 0. **1958/0.** With-DB: not run — OWED (68).

## F1-FX
Source read (Read tool, `offset`/`limit`, never copied): header line (151 columns, `Change` present) and lines 11,630–11,649 of the retained export — the empty-`Change` rows sit at the file's tail.

### T
Appended `test_the_blank_change_fixture_is_the_real_export_shape` (`tests/cobalt/test_replay_movers.py`): header byte-equal to `movers-gainers.real-shape.csv`'s; ≥1 blank-`Change` row counted by `csv`; 25 ranked rows; first blank row at index 25.
On the base: RED — `FileNotFoundError: [Errno 2] No such file or directory: '/Users/cobalt/cobalt-wt/s2-smoke-fix/tests/fixtures/replay/movers-gainers-blank-change.real-shape.csv'` (`1 failed, 36 deselected in 0.16s`).

### C
`tests/fixtures/replay/_cut_p4_fixtures.py`: new mode `movers-blank <raw-export-path>` (`cut_movers_blank`, `BLANK_TOP_ROWS = 25`, `_has_blank_change` = `(cell or "").strip() == ""`), module docstring "FOURTH MODE" paragraph, mode dispatch; existing modes unchanged. The one run:
`uv run python tests/fixtures/replay/_cut_p4_fixtures.py movers-blank /Users/cobalt/cobalt/data/radar-cache/2026-09-22/movers-gainers-211004.csv` → exit 0, stdout verbatim:
`wrote /Users/cobalt/cobalt-wt/s2-smoke-fix/tests/fixtures/replay/movers-gainers-blank-change.real-shape.csv (39 rows kept of 11648 data rows, 151 columns; 14 with a blank Change, kept at export positions 11635-11648; top 25 rows kept above them)`
After: GREEN — `1 passed, 36 deselected in 0.08s`.

### D
`docs/40 - DevDocs/tests/fixtures/replay/_cut_p4_fixtures.md`: "Four modes"; new section `movers-blank <raw-export-path>`.

### SUITE
`uv run pytest -q tests/cobalt -p no:cacheprovider` → `1959 passed, 349 skipped, 1 xfailed in 63.43s (0:01:03)`, exit 0. **1959/0.**

### COMMIT
`fc16830` fix(s2-smoke): F1-FX the blank-Change real-shape movers fixture and its cutter mode — `git show --stat HEAD`: 5 files changed, 220 insertions(+), 2 deletions(-) (report, cutter DevDoc, `test_replay_movers.py`, `_cut_p4_fixtures.py`, the new fixture 40 lines).

## F1
### T
Appended to `tests/cobalt/test_replay_movers.py` (all over the new fixture; blank counts COUNTED BY THE TEST with `csv`): `test_a_blank_change_row_is_unranked_not_fatal_on_the_export_that_failed` (top_n 20 → 20 rows, ranks 1..20, `unranked_rows` = counted blanks, `exported_rows` = data rows, `export_counts` unranked + `expected == min(20, exported - unranked)`) · `test_blank_rows_are_unranked_wherever_the_export_places_them` (CONSTRUCTED order: blanks above, ranked reversed → `side="losers"`, rank 1 = first ranked row; one blank BETWEEN ranked rows excluded; sort still bites across a blank row) · `test_a_side_of_only_blank_change_rows_fails_loud` · `test_a_non_blank_change_that_is_not_a_percentage_still_fails` (`-`, `abc` — pin) · `test_one_warning_per_side_with_unranked_rows_and_none_without` · `test_the_side_count_names_its_four_numbers_when_expected_is_wrong` · `test_the_retained_path_parses_blank_change_rows_the_same_way`. Existing tests amended for the new required field: `test_export_counts_refuse_a_disagreement_and_a_repeated_side` (adds `unranked=0`, and now matches `expected 60` so it cannot pass on a missing field), `test_replay_runner.py::test_the_recorded_counts_round_trip_through_job_result` (payload carries `"unranked": 0`). Header byte-equality is F1-FX's test.
On the base: RED — `8 failed, 70 passed, 2 skipped in 7.25s`; the five blank-fixture tests fail with `cobalt.radar.collector.SourceFailure: movers: Change '' is not a percentage` (the night's error, verbatim), the only-blank test with `Regex pattern did not match`, the side-count tests with `Extra inputs are not permitted` on `unranked`. The `-`/`abc` test is GREEN on the base (pin: unchanged messages).
Two deviations from the prompt's wording, both named: (a) the warning is captured with a loguru sink, not `caplog` — `movers.py`'s neighbours (`replay/runner.py`, `radar/*`, `cards/*`) all log through loguru, and `caplog` does not see loguru; (b) the retained-path test holds the fixture as the GAINERS file and the same real rows in the constructed ascending order as the LOSERS file — the fixture itself as the losers file would (correctly) fail the losers sort check, which is not what that test is for.

### C
`src/cobalt/replay/movers.py`: `parse_movers` skips a row whose `Change` is `(raw or "").strip() == ""`, counts it, ranks the rest `len(rows) + 1`; a side with data rows and zero ranked rows → `SourceFailure("movers-<side>: every one of <m> rows has a blank Change")`; one `logger.warning` per side with unranked rows; `exported_rows = len(raw_rows)` (same meaning as before: every data row); `unranked_rows` passed on; `export_counts` → `expected = min(top_n, exported - unranked)`, refusal message names the unranked count; docstrings `WHICH ROW DECIDES` / `WHAT THE EXPORT REALLY HAD` + `parse_movers` gain the rule. `REQUIRED_HEADERS` unchanged. `src/cobalt/replay/models.py`: `MoversExport.unranked_rows: int = Field(ge=0)` (required), validator `exported_rows >= len(rows) + unranked_rows`; `MoversSideCount.unranked: int = Field(ge=0)` (required), validator `expected == min(top_n, exported - unranked)`, message names all four numbers. `configs/cobalt/smoke/s2.yaml` K9.2 / K9.5 `expect_text` only (`{exported, unranked, top_n, expected}`, `expected = min(top_n, exported - unranked)`); graded key unchanged.
After: GREEN — `uv run pytest -q tests/cobalt/test_replay_movers.py tests/cobalt/test_replay_runner.py tests/cobalt/test_smoke.py -p no:cacheprovider` → `106 passed, 3 skipped in 7.87s`.

### D
`docs/40 - DevDocs/cobalt/replay/movers.md` (new paragraph under Parsing; `export_counts` section), `docs/40 - DevDocs/cobalt/replay/models.md` (`MoversExport`, `MoversSideCount`).

### SUITE
`uv run pytest -q tests/cobalt -p no:cacheprovider` → `1966 passed, 349 skipped, 1 xfailed in 63.79s (0:01:03)`, exit 0. **1966/0.**

### COMMIT
`68e8f23` fix(s2-smoke): F1 a blank Change cell is unranked, counted and loud, not fatal — `git show --stat HEAD`: 8 files changed, 250 insertions(+), 44 deletions(-) (`s2.yaml` 14, `models.md` 13, `movers.md` 29, report 23, `models.py` 31, `movers.py` 45, `test_replay_movers.py` 135, `test_replay_runner.py` 4).

## F2
### T
Appended to `tests/cobalt/test_smoke.py`: `test_k4_4_asks_the_pool_api_with_the_cutoff_as_since` (loaded K4.4 url = `…/api/radar/pool?since={cutoff}`) · `test_render_url_percent_encodes_each_value_and_the_api_parses_it_back` (CONSTRUCTED cutoffs `+00:00` → `2026-09-19T19%3A11%3A42%2B00%3A00` and `-04:00` → `2026-09-19T15%3A11%3A42-04%3A00`; `unquote` → `parse_since(…, now=NOW)` from `cobalt.aset.radar_panel` (read, unchanged) returns the cutoff; the hand-fallback command carries the encoded value; the run's `http_get` receives exactly that URL, PASS) · `test_a_url_without_variables_and_every_non_http_render_is_unchanged` (pin: a variable-free URL unchanged; `render_text` still `+00:00`; K3's command = `hand_command(render_sql(…))`, SQL literal unencoded).
On the base (with F1 committed): RED — `3 failed, 29 deselected in 0.29s`: `AssertionError: assert 'http://127.0...pi/radar/pool' == 'http://127.0...ince={cutoff}'` and twice `AttributeError: module 'cobalt.smoke.checks' has no attribute 'render_url'. Did you mean: 'render_sql'?` (the pin test cannot run without the new function; its `render_text` / K3 halves are pins).
First post-fix run: `1 failed, 30 passed, 1 skipped` — a TEST defect (asserted a raw SQL literal inside the shlex-quoted hand command); the assertion was moved to `render_sql`'s output, no code change.

### C
`src/cobalt/smoke/checks.py`: `render_url(template, ctx)` = `VAR_RE.sub(… quote(text_value(v), safe=""))`, used by `command_for`'s http branch and by `_http`; exported in `__all__`; `from urllib.parse import quote`. `render_text` / `render_sql` unchanged. `configs/cobalt/smoke/s2.yaml` K4.4: `url: http://127.0.0.1:5010/api/radar/pool?since={cutoff}`, `expect_text: "HTTP 200 (since = the deploy cutoff: a past, tz-aware instant — the API's ruled contract, P3 plan R2-1)"`. `src/cobalt/aset/**` untouched.
After: GREEN — `uv run pytest -q tests/cobalt/test_smoke.py -p no:cacheprovider` → `31 passed, 1 skipped in 0.94s`.

### D
`docs/40 - DevDocs/cobalt/smoke/checks.md`: rendering helpers — `render_url` paragraph; `render_text` no longer claims URLs.

### SUITE
`uv run pytest -q tests/cobalt -p no:cacheprovider` → `1969 passed, 349 skipped, 1 xfailed in 63.57s (0:01:03)`, exit 0. **1969/0.**

### COMMIT
`7ec24b2` fix(s2-smoke): F2 K4.4 asks the pool API with since = the cutoff, percent-encoded — `git show --stat HEAD`: 5 files changed, 90 insertions(+), 9 deletions(-) (`s2.yaml` 4, `checks.md` 3, report 23, `checks.py` 14, `test_smoke.py` 55).

## F3
Gate: K3 PROOF row quoted under AUTHORIZATION — `ranked_without_metric 0` → BUILT.

### T
Appended OFFLINE `test_k3_grades_only_a_ranked_row_that_stored_no_metric` to `tests/cobalt/test_smoke_k3_sql.py` (CTE selects `m.last_rank`; both graded counters' FILTER carries `rank_metric IS NULL` and `last_rank IS NOT NULL`; `unranked_retained` is selected over the first set as `rank_metric IS NULL AND last_rank IS NULL`, and appears in no `expect` predicate; `value_null` ungraded; `known_if` unchanged = `post_deploy_admitted eq 0`, `rescanned_admitted eq 0`; `{cutoff}` still twice). `K3_COLUMNS` (the with-DB test's expected column set) gains `unranked_retained`; that test renamed `…_its_six_counters_…`; module docstring updated.
On the base (F2 committed): RED — `1 failed, 2 skipped in 0.09s`: `assert 'm.last_rank' in "WITH scan AS ( SELECT max(last_scan_id) AS id FROM system.radar_pool …"`.

### C
`configs/cobalt/smoke/s2.yaml` K3 ONLY: `admitted` CTE selects `m.last_rank`; `metric_missing` and `rescanned_metric_missing` count `rank_metric IS NULL AND last_rank IS NOT NULL`; new column `unranked_retained`; `expect_text` rewritten (cites `radar/pool.py:50-54` and `plan-s2-p4-2026-09-15.md:243`; HOLD-ambiguity paragraph kept verbatim); comment block above K3 gains the two sentences. `src/cobalt/radar/**` untouched.
After: GREEN — `uv run pytest -q tests/cobalt/test_smoke_k3_sql.py tests/cobalt/test_smoke.py -p no:cacheprovider` → `32 passed, 3 skipped in 0.90s`.
The with-DB HOLD test (`test_k3_hold_row_reads_red_documented_ambiguity`) constructs `last_rank = 1`, so by reading it still grades FAIL under the new counters — UNPROVEN until run on `cobalt_dev` (OWED (68)).

### D
`docs/40 - DevDocs/cobalt/smoke/config.md`: K3 section gains the F3 paragraph; the K9 bullet's `expected` formula updated to `min(top_n, exported - unranked)` (F1's rule, carried in this commit because the file was untouched until now).

### SUITE
`uv run pytest -q tests/cobalt -p no:cacheprovider` → `1970 passed, 349 skipped, 1 xfailed in 63.86s (0:01:03)`, exit 0. **1970/0.**

### COMMIT
`b510b65` fix(s2-smoke): F3 K3 grades only a ranked row that stored no metric; unranked_retained printed — `git show --stat HEAD`: 4 files changed, 112 insertions(+), 16 deletions(-) (`s2.yaml` 28, `config.md` 22, report 25, `test_smoke_k3_sql.py` 53).

## CLOSE
| rule | command | result (verbatim) |
|---|---|---|
| OFFLINE | `uv run pytest -q tests/cobalt -p no:cacheprovider` (background) | `1970 passed, 349 skipped, 1 xfailed in 63.70s (0:01:03)`, exit 0 — **1970/0** |
| diff scope | `git diff --stat 6f4da5e` | `16 files changed, 666 insertions(+), 65 deletions(-)`: `configs/cobalt/smoke/s2.yaml` · DevDocs `replay/models.md`, `replay/movers.md`, `smoke/checks.md`, `smoke/config.md`, `tests/fixtures/replay/_cut_p4_fixtures.md` · this report · `src/cobalt/replay/models.py`, `src/cobalt/replay/movers.py`, `src/cobalt/smoke/checks.py` · tests `test_replay_movers.py`, `test_replay_runner.py`, `test_smoke.py`, `test_smoke_k3_sql.py` · `tests/fixtures/replay/_cut_p4_fixtures.py` · the new fixture. Only rows' files + tests + fixture + DevDocs + report — no other path. |
| protected paths | `git diff 6f4da5e -- src/cobalt/radar src/cobalt/aset src/cobalt/cards src/cobalt/archiver src/cobalt/db_migrations` | (empty) |
| committed fixtures not re-cut | `git diff 6f4da5e -- tests/fixtures/replay/movers-gainers.real-shape.csv tests/fixtures/replay/movers-losers.real-shape.csv` | (empty) |
| RESTARTS (L42) | `uv run cobalt jobs restarts 6f4da5e..HEAD` | `configs/cobalt/smoke/s2.yaml M operator command (cobalt smoke); no job reads -` · 7 DevDocs/report `DOCS -` · `src/cobalt/replay/models.py M static import reach com.cobalt.aset,com.cobalt.radar` · `src/cobalt/replay/movers.py M static import reach com.cobalt.aset,com.cobalt.radar` · `src/cobalt/smoke/checks.py M static import reach com.cobalt.radar` · 6 test/fixture paths `test/documentation; no resident -` · **`RESTARTS: com.cobalt.aset com.cobalt.radar`**; 0 UNCLASSIFIED |
| commits | `git log --oneline 6f4da5e..HEAD` | `b510b65` F3 · `7ec24b2` F2 · `68e8f23` F1 · `fc16830` F1-FX |
| L32 self-check | read of this report, whole | no ticker written. Commit messages carry none; the cutter's stdout carries counts and positions only. The fixture itself carries market tickers by the P4 fixture policy (L45 real shape). |

Tests added: 12 new test functions (F1-FX 1, F1 7, F2 3, F3 1) — suite 1958 → 1970 passed; plus 2 existing tests amended for the new required `unranked` field and the with-DB `K3_COLUMNS` constant.

## ESCALATE
1. **(i) The fixture.** The retained 2026-09-22 gainers export has 11,648 data rows; 14 carry an EMPTY `Change` cell, at export positions 11,635–11,648 — the last 14 rows, nothing blank above them. The fixture keeps the top 25 data rows + those 14 (39 rows, 151 columns); in the fixture they are rows 26–39.
2. **(ii) LOSERS placement is UNPROVEN** until the first live losers export that carries blank-`Change` rows (the 09-22 losers side was never fetched). `test_blank_rows_are_unranked_wherever_the_export_places_them` covers it by CONSTRUCTED order (every blank row above the ranked rows, ranked reversed; and one blank row between ranked rows).
3. **(iii) F3 BUILT** on the launch row's proof — `cto-2026-09-23.md:10`: `K3 PROOF: metric_missing 66 · unranked_retained 66 · ranked_without_metric 0 [06:03] → F3 HOLDS, built.`
4. **(iv) With-DB proofs OWED (68)** — none run here (`cobalt_dev` broken, R110): `tests/cobalt/test_smoke_k3_sql.py::test_k3_statement_parses_and_returns_its_six_counters_on_cobalt_dev` (the changed K3 statement, now six columns) and `::test_k3_hold_row_reads_red_documented_ambiguity` (by reading still FAIL: its constructed held row has `last_rank = 1`); `tests/cobalt/test_smoke.py::test_committed_queries_run_read_only_on_cobalt_dev` (runs K3's new SQL); `tests/cobalt/test_replay_movers.py::test_r1_20_changed_top_n_rerun_deactivates_never_deletes_and_identical_rerun_is_a_noop` (`MoversStore.reconcile` over exports that now carry `unranked_rows`); `tests/cobalt/test_replay_runner.py::test_r2_3_each_phase_runs_on_its_own_side_and_the_wrong_side_is_refused` (the runner's with-DB path through `movers_by_side`).
5. **(v) Readers of `movers_by_side`** (`grep -rn "movers_by_side" src tests`): `src/cobalt/replay/models.py:438` (the `ReplayResult` field) and `src/cobalt/replay/runner.py:336` (the one writer) in `src`; tests `test_replay_runner.py`, `test_smoke.py`. The smoke reads `last_result` as raw JSON by dotted key (`movers_by_side.<side>.expected`), never through the model. No `src` code validates an OLD job row against `ReplayResult`/`MoversSideCount` (`grep -rn ReplayResult src` → construction only in `runner.py:276`), so a pre-fix `job.result` lacking `unranked` breaks nothing; the one `ReplayResult.model_validate(payload)` is a test round-trip of a fresh result.
6. **RESTARTS: `com.cobalt.aset com.cobalt.radar`** (static import reach from `replay/models.py`, `replay/movers.py`, `smoke/checks.py`) — the stacked deploy restarts both residents, the radar inside the 20:00–21:00 pause (L43 / L66). `com.cobalt.replay` is a one-shot and picks the fix up at 21:10.
7. **Two named deviations from the prompt's test wording** (both in `## F1 ### T`): the one-warning-per-side test captures with a loguru sink, not `caplog` (the module's neighbours all log through loguru; `caplog` cannot see it); the retained-path test uses the fixture as the gainers file and the same real rows in the constructed ascending order as the losers file (the fixture itself cannot pass the losers sort check).
8. **Disclosure.** This session's first Bash call was `cat` of the prompt file — read-only, made before the prompt's command rules had been read; not on the allowlist, not denied. Every later call is on the list.
9. Pre-existing, NOT fixed (L75, out of scope): `docs/40 - DevDocs/cobalt/replay/movers.md:22` still lists `REQUIRED_HEADERS = [Ticker, Change, Volume]` (the code has five since R16 "C").

(vi) ASK DESK: none. (vii) `MEMORY:` a prompt that names `caplog` for a loguru-logging module means a loguru sink (`logger.add` / `logger.remove`), the idiom `test_cards_picks.py` already uses. No `RULING:` line.

## CONTINUE
next: none — built. The desk verifies the artifact (L35) and launches the three-house check on `6f4da5e..b510b65` (+ the report commit).

S2 SMOKE FIX BUILT b510b65 | on 6f4da5e | offline 1970/0 | with-DB: OWED (68) | RESTARTS: com.cobalt.aset com.cobalt.radar | F3: built | tests added: 12 | ESCALATE: 9
