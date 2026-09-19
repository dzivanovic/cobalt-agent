# S2-P4 verify — AT-1: one column-set source (2.3) + the 151-column movers fixture (2.5)

MODEL: Opus 5 headless builder (L29 floor, L50), launched by the Sonnet hub · WORKTREE: `/Users/cobalt/cobalt-wt/s2-p4` (branch `sprint-2/p4`) · BRIEF: `scratch/at1-brief.md` · NOT COMMITTED (the hub commits).

## §0 Headline

BUILT both. `cobalt.radar.config.screener_columns()` is now the only producer of the Finviz `c=` index list; all four sites call it and `grep -rn "range(151)" src/cobalt` prints nothing.
Both movers fixtures re-cut by the new cutter mode: 151 columns, `Asset Type` present, header byte-identical to the radar export fixture, 29/19 real fund rows.
Gate suite `uv run pytest -q tests/cobalt tests/taxonomy`: **1783 passed, 322 skipped, 1 xfailed, 15 warnings in 55.20s**.
The not-equity RULE was not touched, as briefed. 6 tests added, 1 renamed in effect, 5 existing test modules corrected.
ESCALATE: 5 — the biggest is that the re-fetched exports are a DIFFERENT TRADING DAY from the membership fixture, which forced ticker repairs in three test modules the brief did not name.

## Files changed

| file | change |
|---|---|
| `src/cobalt/radar/config.py` | +`screener_columns()` / `screener_columns_param()` beside `ExportConfig`, both exported. Parses `a-b` (inclusive) and a comma list; anything else raises `RadarConfigError`. No config shape change, no `radar.yaml` edit. |
| `src/cobalt/radar/collector.py` | `_params()`'s `c` comes from `screener_columns_param(self.config.export.columns)`. |
| `src/cobalt/replay/movers.py` | `MoversCollector._params()` likewise. |
| `src/cobalt/radar/propose.py` | `_columns()` keeps owning the note's formatting (backticks, whitespace, `<same columns>`) and hands the declaration to `screener_columns`; a refusal chains into the same `ProposalRefused` message as before. |
| `src/cobalt/radar/throttle.py` | `run_probe(..., columns: str)` is now a REQUIRED keyword argument, rendered through `screener_columns_param`; `command()` reads `load_config().export.columns` once and passes it down. The module still holds no config of its own. |
| `tests/fixtures/replay/_cut_p4_fixtures.py` | New `movers` mode (third CLI mode; `evidence` untouched, `main()` untouched). `MOVERS_ROWS`, `_one_row`, `_first_fund_row`, rewritten `cut_movers`. Module docstring: re-fetched raw inputs + THIRD MODE paragraph. |
| `tests/fixtures/replay/movers-{gainers,losers}.real-shape.csv` | RE-CUT by the mode above (I ran it; the fixture is its output, never hand-edited). |
| `tests/cobalt/test_radar_config.py` | +2 tests (parsing, malformed). |
| `tests/cobalt/test_finviz_consumers.py` | +2 tests (all consumers agree, source scan) and the module docstring's second subject. |
| `tests/cobalt/test_replay_movers.py` | +3 tests; docstring's KNOWN SHAPE FACT replaced; 8 tests' facts corrected to the new export. |
| `tests/cobalt/test_p4_asset_type_evidence.py` | +3 tests, +`narrowed_export` fixture; docstring and 4 tests corrected (the movers fixture is no longer the "file without the columns"). |
| `tests/cobalt/test_radar_throttle.py` | 4 `run_probe` calls pass `columns=COLUMNS`. |
| `tests/cobalt/test_replay_runner.py` | 2 pinned tickers corrected to the new export. |
| `docs/40 - DevDocs/cobalt/radar/{config,collector,throttle,propose}.md`, `cobalt/replay/movers.md` | updated (agent-authored). |
| `docs/40 - DevDocs/tests/fixtures/replay/_cut_p4_fixtures.md` | NEW — the cutter had no DevDoc (AT-0 ESCALATE 2). |

Not touched: `configs/` (any file), migrations, `not_equity` / `NotEquityConfig` / `runner.py`'s exclusion line / `benchmark_misses`'s `unreported` branch / `REQUIRED_HEADERS`, scoring, ranking. No dependency added. No `.env`. Nothing outside this worktree. No commit.

## 2.3 — tests added

| test | file | proves |
|---|---|---|
| `test_screener_columns_parses_the_two_declarations_the_radar_uses` | `test_radar_config.py` | `"0-150"` → 0..150 inclusive, `"0-3"`, `"7"`, `"0,1,65"`; `screener_columns_param(load_config().export.columns)` equals the written-out 151-index string |
| `test_a_malformed_column_declaration_crashes` | `test_radar_config.py` | 10 malformed values raise `RadarConfigError` (L1), including `"150-0"` and `"0-150 "` — the function tidies nothing |
| `test_every_finviz_consumer_asks_for_the_same_column_set` | `test_finviz_consumers.py` | `FinvizScreenerCollector._params()["c"]` == `MoversCollector._params("gainers")["c"]` == `…("losers")["c"]` == the throttle probe's `c` == `",".join(map(str, range(151)))` |
| `test_only_one_function_in_the_new_core_builds_the_column_set` | `test_finviz_consumers.py` | the brief's `grep` as a test, plus: no `"c"` param is assembled inline, and any module sending a computed one imports the one function |

The throttle probe's `c` is captured by driving `throttle.command()` itself (transport, credential, refusal clock and result file faked), not by reading `run_probe`'s signature — the wiring under test is `command()` reading the config.

### Red, then green

`test_a_malformed_column_declaration_crashes` + its sibling, before the edit (collection error, verbatim):

```
tests/cobalt/test_radar_config.py:7: in <module>
    from cobalt.radar.config import (
E   ImportError: cannot import name 'screener_columns' from 'cobalt.radar.config' (/Users/cobalt/cobalt-wt/s2-p4/src/cobalt/radar/config.py)
```

`test_only_one_function_in_the_new_core_builds_the_column_set`, before the edit (verbatim):

```
>       assert literals == []
E       AssertionError: assert ['radar/colle...ay/movers.py'] == []
E         
E         Left contains 4 more items, first extra item: 'radar/collector.py'
1 failed, 2 passed, 1 xfailed in 0.30s
```

Two intermediate reds, recorded rather than smoothed over: the scan first flagged `radar/config.py` itself (my own docstring spelled the literal out in prose — reworded, not exempted), then `radar/propose.py` (the regex matched its deliberate one-column literal `"c": "0"` through backtracking — the pattern now requires a non-quote first character of the value).

`test_every_finviz_consumer_asks_for_the_same_column_set` **passed before and after**, and that is its point: it pins behaviour the refactor must not change. Stated plainly rather than presented as a red.

GREEN, the four together with the two collector/propose modules:

```
82 passed, 1 xfailed in 6.13s
```

### The grep

BEFORE (over `src` and `tests`, so the old tree shows too):

```
src/cobalt/replay/movers.py:210:        return {"v": self.config.export.v, "c": ",".join(str(v) for v in range(151)), "o": SIDES[side]}
src/cobalt/radar/collector.py:161:            "c": ",".join(str(value) for value in range(151)),
src/cobalt/radar/propose.py:180:        return list(range(151))
src/cobalt/radar/throttle.py:180:                "c": ",".join(str(v) for v in range(151)),
src/cobalt_agent/skills/research/finviz_api.py:66:    MASTER_COLUMNS = ",".join(map(str, range(151)))
```

AFTER — `grep -rn "range(151)" src/cobalt`:

```
(no output)
```

Zero hits, not one: `screener_columns` derives the list from the declaration (`range(start, end + 1)`) and never spells 151. The old-tree hit in `src/cobalt_agent/` is outside `src/cobalt` and outside the strangler boundary — untouched.

## 2.5 — the fixture

`uv run python tests/fixtures/replay/_cut_p4_fixtures.py movers`, verbatim:

```
wrote /Users/cobalt/cobalt-wt/s2-p4/tests/fixtures/replay/movers-gainers.real-shape.csv (60 rows, 151 columns, 29 with a non-blank Asset Type; no Asset Type row appended)
wrote /Users/cobalt/cobalt-wt/s2-p4/tests/fixtures/replay/movers-losers.real-shape.csv (60 rows, 151 columns, 19 with a non-blank Asset Type; no Asset Type row appended)
```

Both raw files already carry a non-blank `Asset Type` inside the first 60 data rows (gainers row 5, losers row 7), so nothing had to be appended — the append path exists, is documented in the cutter's docstring and on stdout, and was not needed. No row invented.

Cut rules, as built: header row from the raw file, never rebuilt; `assert _anonymize(header) == header` (asserted per side); the cutter also asserts the CSV record count equals the line count, so cutting by line cannot split a row; dates and hex suffixes stripped by the existing `_anonymize` (23 and 26 shifted dates in the two files; `2026-09-` count in each fixture: 0).

One judgement recorded: "header row byte for byte" is satisfied up to LINE ENDINGS. The raw exports are CRLF; `read_text`/`write_text` normalise to LF, which is what the cutter already did to `pool-metrics.real-shape.csv`. Keeping CRLF would have made the movers header *unequal* to the radar fixture's, which is the other thing the brief asks for. LF for all three, one shape, asserted byte for byte.

### Tests added

| test | file | proves |
|---|---|---|
| `test_the_collector_receives_one_export_shape` | `test_replay_movers.py` | all three fixtures' header rows are equal byte for byte; 151 columns; `Asset Type` among them |
| `test_both_movers_fixtures_hold_a_real_row_with_a_non_blank_asset_type` | `test_replay_movers.py` | 60 data rows per side, ≥1 with a non-blank `Asset Type` |
| `test_asset_type_is_read_from_the_movers_export_itself` | `test_replay_movers.py` | `parse_movers` reads the value from the movers export (gainers rank 5, losers rank 7 = `Equities (Stocks)`), rank 1 blank → `None` |
| `test_both_committed_exports_now_carry_the_two_columns` | `test_p4_asset_type_evidence.py` | no committed export lacks `Asset Type`/`Industry`; 80 rows with columns, 0 without |
| `test_the_movers_fixture_gives_tables_a_and_b_real_rows` | `test_p4_asset_type_evidence.py` | real input: table B = `[("CryptoCurrency", 5), ("Equities (Stocks)", 24)]`, table A the same pairs against `Exchange Traded Fund`, 29 fund tickers, table C total 0 |
| `test_a_real_export_renders_non_empty_a_and_b_tables` | `test_p4_asset_type_evidence.py` | the report's ROW rendering exercised from a real artifact, and the stdout summary still carries no ticker (L32) |

### Red, then green

The three new `test_replay_movers` tests and the three new evidence tests, run against the PREVIOUS committed fixtures (restored from `HEAD` into the worktree for the measurement, then regenerated by the cutter — the regenerated files are byte-identical to the cut taken before the restore, verified):

```
FAILED tests/cobalt/test_replay_movers.py::test_the_collector_receives_one_export_shape - AssertionError: gainers
FAILED tests/cobalt/test_replay_movers.py::test_both_movers_fixtures_hold_a_real_row_with_a_non_blank_asset_type - KeyError: 'Asset Type'
FAILED tests/cobalt/test_replay_movers.py::test_asset_type_is_read_from_the_movers_export_itself - AssertionError: assert 'Asset Type' in ('No.', 'Ticker', 'Industry', 'Count...
FAILED tests/cobalt/test_p4_asset_type_evidence.py::test_both_committed_exports_now_carry_the_two_columns - AssertionError: assert ['movers-gain...al-shape.csv'] == []
FAILED tests/cobalt/test_p4_asset_type_evidence.py::test_the_movers_fixture_gives_tables_a_and_b_real_rows - AssertionError: assert 0 == 60
FAILED tests/cobalt/test_p4_asset_type_evidence.py::test_a_real_export_renders_non_empty_a_and_b_tables - AssertionError: assert '| Equities (Stocks) | Exchange Traded Fund | 24 |' ...
6 failed in 0.14s
```

The other direction of the same red — the NEW fixture meeting the OLD assertions, which is the list of facts that had to be corrected:

```
FAILED tests/cobalt/test_replay_movers.py::test_tesla_class_mover_absent_from_pool_appears_in_miss_line_with_excluded_by - KeyError: 'CTNT'
FAILED tests/cobalt/test_replay_movers.py::test_admitted_mover_is_not_a_miss - AssertionError: assert 'AEHL' in {'CONL', 'IMCC', 'SNDG', 'SNXX'}
FAILED tests/cobalt/test_replay_movers.py::test_never_admitted_episode_supplies_its_excluded_by - KeyError: 'DAIC'
FAILED tests/cobalt/test_replay_movers.py::test_movers_archived_regardless_of_watchlist - AssertionError: assert ['IMCC', 'QNME', 'REFR'] == ['CTNT', 'DAIC', 'KXIN']
FAILED tests/cobalt/test_replay_movers.py::test_parse_real_movers_exports_rank_in_export_order_and_hash_the_raw_bytes - AssertionError: assert [(1, 'IMCC', ...mal('68.49'))] == [(1, 'CTNT', ...ma...
FAILED tests/cobalt/test_replay_movers.py::test_r1_20_a_ticker_on_both_sides_resolves_to_one_missed_row - assert 0 == 1
FAILED tests/cobalt/test_replay_movers.py::test_archive_counts_failures_and_incomplete_coverage_and_never_marks_them_archived - assert [] == [1]
FAILED tests/cobalt/test_replay_movers.py::test_archive_skips_tickers_already_covered_and_dry_run_fetches_nothing - assert [] == [1]
FAILED tests/cobalt/test_p4_asset_type_evidence.py::test_rows_read_counts_both_kinds_of_file - AssertionError: assert 80 == 20
FAILED tests/cobalt/test_p4_asset_type_evidence.py::test_file_without_the_columns_is_listed_never_skipped - AssertionError: assert [] == ['movers-gain...al-shape.csv']
FAILED tests/cobalt/test_p4_asset_type_evidence.py::test_render_reports_the_file_without_the_columns_by_name - AssertionError: assert 'movers-gainers.real-shape.csv' in '# Asset Type vs ...
FAILED tests/cobalt/test_p4_asset_type_evidence.py::test_stdout_summary_carries_counts_and_no_ticker - AssertionError: assert 'rows: 20' in 'files: 2 (without the columns: 0); ro...
12 failed, 19 passed, 1 skipped in 0.24s
```

Plus two in `test_replay_runner.py` (`MISS mover CTNT …`, `FakeCollector(fail={"CTNT"})`).

GREEN after the corrections — `tests/cobalt/test_replay_movers.py`: `23 passed, 1 skipped`; `tests/cobalt/test_p4_asset_type_evidence.py`: `14 passed`; `tests/cobalt/test_replay_runner.py`: `27 passed, 1 skipped`.

### The leak scans

`test_screen_filter_values_live_only_in_approved_radar_fixtures` passes (it is inside the gate suite).

`grep -rlE '2026-09-' tests/fixtures/replay tests/fixtures/radar` prints two files, and NEITHER is a fixture:

```
tests/fixtures/radar/_cut_p2_fixtures.py
tests/fixtures/radar/_cut_panel_fixtures.py
```

Both are pre-existing prose in the P2/P3 sibling CUTTERS, describing the scan pattern itself (e.g. `# for the literal "2026-09-1" pattern).`), present before this chunk and untouched by it. `grep -c` over both new movers fixtures: `0` and `0`. No fixture carries an anchor-month date, so there was nothing to fix in this cutter. See ESCALATE 4.

## Suite line (verbatim)

`uv run pytest -q tests/cobalt tests/taxonomy`:

```
1783 passed, 322 skipped, 1 xfailed, 15 warnings in 55.20s
```

(1764 → 1783: +6 new, +13 from the two 2.3 test modules and parametrisation.)

## ESCALATE

**1. The re-fetched exports are a DIFFERENT TRADING DAY from the membership fixture — the fixture set is no longer one coherent day.** The brief expected the re-cut to change two tests; it changed 14 across three modules, because every ticker, rank and percentage in the exports is new. `membership-day.real-shape.json` is still the original anchor day. The overlap is real but smaller (gainers: 4 admitted, 2 never-admitted; losers: 6 and 2), and I re-pointed each benchmark test at a row that genuinely carries its case — e.g. the F13 "Tesla-class mover" is now QNME (+92.25%, rank 2, no episode at all), because rank 1 IMCC WAS admitted that day and is correctly not a miss. Every assertion is a real row of a real export against a real episode set; what is no longer true is that the mover and the membership come from the SAME session. If that pairing matters, the membership fixture has to be re-cut from 2026-09-19 too — a production DB read, which this seat cannot do (L41). Dejan's / the hub's call.

**2. Table C still has no real-artifact coverage.** In both 60-row cuts the two fund signals agree on every row: every non-blank `Asset Type` row is also `Industry = Exchange Traded Fund`, and there is no fund-industry row with a blank type. Table C total = 0. The hub's full-cache evidence found 16 rows of class (ii), so the disagreement exists — just not in the top 60 of either side. AT-0's ESCALATE 1 is therefore **closed for tables A and B and for the report's row rendering** (now exercised from a real export) and **still open for table C**.

**3. `"v": 152` is the same L3 duplicate, one field over.** `radar/throttle.py` and `radar/propose.py` both write the literal `152` where `config.export.v` says the same thing. Identical shape to the column set, deliberately out of this brief's scope, not fixed. One line each when someone rules it.

**4. The leak grep is not clean, for a reason that predates this chunk.** The two sibling cutters mention the anchor-month pattern in comments. The brief says "fix the CUTTER" — but the offending cutters are P2's and P3's, not this one, and the strings are prose describing the test, not leaked data. I did not edit another chunk's cutter on my own authority. If the scan is meant to be zero-output, those two comments need rewording by whoever owns them.

**5. DevDocs.** I wrote the missing `_cut_p4_fixtures.md` (half of AT-0 ESCALATE 2). Still absent: `docs/40 - DevDocs/tests/cobalt/test_p4_asset_type_evidence.md` and `…/test_replay_movers.md`. P4's test modules have no pages at all; `docs/40 - DevDocs/tests/` holds 40 other test pages, so this is a gap, not a convention.

## What I could not do / did not do

- Did not touch the not-equity rule in any form (config, `NotEquityConfig`, `runner.py`'s exclusion, `benchmark_misses`, `REQUIRED_HEADERS`) — briefed as ESCALATED to Dejan's desk.
- Did not commit; did not launch anything; no DB, no credentials, no `.env`, nothing outside this worktree.
- `run_probe`'s `columns` is a REQUIRED keyword argument, not a defaulted one. A default would have been a second place the shipped value is written. Cost: four call-site edits in `test_radar_throttle.py`, which pass the smallest valid declaration because those tests are about stopping, not about shape.
- `ruff` is not a gate here (`pyproject.toml:84` scopes it to taxonomy, and even that scope has 83 pre-existing findings); pytest is. Line lengths in the touched files follow the surrounding style, which already exceeds 100 throughout.
