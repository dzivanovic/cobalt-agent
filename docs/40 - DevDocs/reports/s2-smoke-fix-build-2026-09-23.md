# S2 SMOKE FIX — build report 2026-09-23

Seat `s2-smoke-fix-0922` · Opus 5.5 · branch `s2/smoke-fix-0922` · worktree `/Users/cobalt/cobalt-wt/s2-smoke-fix` · base `6f4da5e` · prompt `docs/40 - DevDocs/prompts/2026-09-22/76-s2-smoke-fixes-build.md` · started 2026-09-23 06:04:18 EDT (`date`).

## §0 Headline
(filled at close)

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
(hash recorded under `## CLOSE`)

## CONTINUE
next: F3 COMMIT, then CLOSE

(run in progress — next step under ## CONTINUE)
