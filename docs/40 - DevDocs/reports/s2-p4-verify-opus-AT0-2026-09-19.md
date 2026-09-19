# S2-P4 verify — AT-0: read-only `evidence` mode for the fixture cutter

MODEL: Opus 5 headless builder (L29 floor, L50), launched by the Sonnet hub `p4-verify-0919` · WORKTREE: `/Users/cobalt/cobalt-wt/s2-p4` (branch `sprint-2/p4`) · BRIEF: `scratch/at0-brief.md` · NOT COMMITTED (the hub commits).

## §0 Headline

BUILT. `tests/fixtures/replay/_cut_p4_fixtures.py` now takes a first CLI argument: none = today's cut, unchanged; `evidence` = read-only scan writing `scratch/asset-type-evidence.md` only.
11 tests added in `tests/cobalt/test_p4_asset_type_evidence.py`; 10 were red before the code (module attribute missing), all green after.
Gate suite: `1764 passed, 322 skipped, 1 xfailed, 15 warnings in 54.30s`.
The evidence mode was NOT run against the real cache — that is the hub's step 2.2.
ESCALATE: 2 (the disagreement path is unexercised by any committed fixture; `_cut_p4_fixtures.py` has no DevDoc).

## Files changed

| file | change |
|---|---|
| `tests/fixtures/replay/_cut_p4_fixtures.py` | +~260 lines, all additive and all below `main()`: module docstring gains a "SECOND MODE" paragraph; new imports (`sys`, `Counter`, `Iterable`/`Sequence`, `pydantic.BaseModel`); `EvidenceError`; models `DisagreementRow` / `PairCount` / `AssetTypeCount` / `EvidenceReport`; `_read_csv`, `collect_evidence`, `_table`, `render_evidence`, `summarize_evidence`, `discover_evidence_inputs`, `evidence_main`; the `__main__` block dispatches on `sys.argv[1]`. No existing function, constant or output path touched. |
| `tests/cobalt/test_p4_asset_type_evidence.py` | NEW, 11 tests. |

Nothing else: no fixture, no `src/`, no config, no `scratch/` file (the tests write only to `tmp_path`; `EVIDENCE_OUT` is written only by `evidence_main`, which I did not run).

## Behaviour built (against the brief)

| brief item | built as |
|---|---|
| mode by first CLI argument | no arg → `main()` verbatim; `evidence` → `evidence_main()`; anything else → `SystemExit("unknown mode 'bogus'; expected no argument or 'evidence'")`, exit 1 (probed) |
| inputs | `sorted(RADAR_CACHE_DIR.rglob("*.csv"))` under `/Users/cobalt/cobalt/data/radar-cache`, then `scratch/movers-gainers-raw.csv`, `scratch/movers-losers-raw.csv` via the existing `SCRATCH` constant |
| header row real | `csv.DictReader`; every lookup by column name, never by position |
| file lacking a column | counted, its rows counted separately, its **name** listed on the "files without the columns" line; never skipped, never an error |
| §1 Read | files read; rows read (files with both columns); rows read (files without the columns); the input dirs |
| §2 Distinct counts | distinct fund tickers (a row in table A or table B) and distinct non-blank `Asset Type` values |
| Table A / B / C | as specified; blank rendered `<blank>`; C carries a COUNTS block first — (i), (ii), total — then the two row tables (file basename, ticker, both values) |
| empty table | the whole line `(none)` |
| tickers | in `scratch/asset-type-evidence.md` only; `summarize_evidence()` (the one stdout line) carries five counts and no ticker — asserted against all 20 tickers of the real radar fixture |
| pure functions | `collect_evidence(paths, input_dirs=()) -> EvidenceReport`, `render_evidence(report) -> str`, plus `summarize_evidence(report) -> str` so the stdout contract is testable without writing a file |
| models | Pydantic `BaseModel` (no new dependency; the file's own idiom is plain functions, the repo's is Pydantic) |
| fail loud (L1) | `EvidenceError` naming the file for: unreadable/undecodable/malformed CSV, and a file with no header row at all. `discover_evidence_inputs()` also raises if the cache directory or either staged movers export is missing — an evidence run over an empty input set would be a plausible-empty artifact |

Decision recorded: a 0-byte or headerless cache file RAISES rather than joining the "without the columns" list. The brief's "counted, never an error" rule is about a header that *lacks the two columns*; a file with no header at all is not a screener export and is a loud failure.

## Tests added — `tests/cobalt/test_p4_asset_type_evidence.py`

Loaded by path with `importlib.util.spec_from_file_location` (the cutter is not an importable package). The loader registers the module in `sys.modules`: the cutter is `from __future__ import annotations`, so without that entry Pydantic cannot resolve the model annotations (`PydanticUserError: EvidenceReport is not fully defined` — caught by these tests, fixed in the loader, not by touching the cutter).

Fixtures are the committed real-shape exports (L45), no row invented:
`tests/fixtures/radar/pool-metrics.real-shape.csv` — real 151-column export, HAS both columns, 20 data rows, every `Asset Type` blank, no `Industry = Exchange Traded Fund` row.
`tests/fixtures/replay/movers-gainers.real-shape.csv` — real `v=152` export, 21 columns, 60 data rows, NO `Asset Type` column.

| test | proves |
|---|---|
| `test_no_argument_path_untouched` | `main`, `evidence_main` and all five `cut_*` functions still exposed and callable |
| `test_rows_read_counts_both_kinds_of_file` | `files_read == 2`, `rows_with_columns == 20`, `rows_without_columns == 60` |
| `test_file_without_the_columns_is_listed_never_skipped` | the list is exactly `["movers-gainers.real-shape.csv"]` |
| `test_input_dirs_are_recorded_as_given` | the input dirs reach the report |
| `test_radar_fixture_has_no_fund_rows` | A, B, C(i), C(ii) empty and both distinct counts 0 for the radar fixture as it is |
| `test_render_prints_none_for_every_empty_table` | header + one real row copied byte-for-byte into `tmp_path` → exactly four whole-line `(none)` (A, B, C(i), C(ii)) and `- total: 0` |
| `test_render_shapes_a_non_empty_table` | table markdown for a non-empty A/B/C (see ESCALATE 1) |
| `test_render_reports_the_file_without_the_columns_by_name` | the movers file's name and its row count appear in the rendered file |
| `test_stdout_summary_carries_counts_and_no_ticker` | the five counts are present; not one of the fixture's 20 tickers appears (L32) |
| `test_unreadable_file_raises_with_its_name` | invalid UTF-8 → `EvidenceError` carrying `not-utf8.csv` |
| `test_headerless_file_raises_with_its_name` | 0-byte file → `EvidenceError` carrying `empty-cache-write.csv` |

No test writes outside `tmp_path`.

## Red, then green

RED (tests written first, before any line of the mode) — `uv run pytest -q tests/cobalt/test_p4_asset_type_evidence.py`, verbatim tail:

```
FAILED tests/cobalt/test_p4_asset_type_evidence.py::test_no_argument_path_untouched - AttributeError: module '_cut_p4_fixtures' has no attribute 'evidence_main'
FAILED tests/cobalt/test_p4_asset_type_evidence.py::test_rows_read_counts_both_kinds_of_file - AttributeError: module '_cut_p4_fixtures' has no attribute 'collect_evidence'
FAILED tests/cobalt/test_p4_asset_type_evidence.py::test_file_without_the_columns_is_listed_never_skipped - AttributeError: module '_cut_p4_fixtures' has no attribute 'collect_evidence'
FAILED tests/cobalt/test_p4_asset_type_evidence.py::test_input_dirs_are_recorded_as_given - AttributeError: module '_cut_p4_fixtures' has no attribute 'collect_evidence'
FAILED tests/cobalt/test_p4_asset_type_evidence.py::test_radar_fixture_has_no_fund_rows - AttributeError: module '_cut_p4_fixtures' has no attribute 'collect_evidence'
FAILED tests/cobalt/test_p4_asset_type_evidence.py::test_render_prints_none_for_every_empty_table - AttributeError: module '_cut_p4_fixtures' has no attribute 'collect_evidence'
FAILED tests/cobalt/test_p4_asset_type_evidence.py::test_render_reports_the_file_without_the_columns_by_name - AttributeError: module '_cut_p4_fixtures' has no attribute 'collect_evidence'
FAILED tests/cobalt/test_p4_asset_type_evidence.py::test_stdout_summary_carries_counts_and_no_ticker - AttributeError: module '_cut_p4_fixtures' has no attribute 'collect_evidence'
FAILED tests/cobalt/test_p4_asset_type_evidence.py::test_unreadable_file_raises_with_its_name - AttributeError: module '_cut_p4_fixtures' has no attribute 'EvidenceError'
FAILED tests/cobalt/test_p4_asset_type_evidence.py::test_headerless_file_raises_with_its_name - AttributeError: module '_cut_p4_fixtures' has no attribute 'EvidenceError'
10 failed in 0.07s
```

Two intermediate reds after the first implementation pass, both recorded here rather than smoothed over:

```
E       pydantic.errors.PydanticUserError: `EvidenceReport` is not fully defined; you should define `PairCount`, then call `EvidenceReport.model_rebuild()`.
7 failed, 3 passed in 0.12s
```
→ fixed in the TEST loader (`sys.modules[spec.name] = module`), not in the cutter.

```
>       assert text.count("(none)") == 4  # A, B, C(i), C(ii)
E       AssertionError: assert 6 == 4
1 failed, 9 passed in 0.06s
```
→ a wrong assertion, not a defect: §1's prose markers (`files without the columns (0): (none)`, `input dirs: (none)`) also contain the string. The assertion now counts whole lines equal to `(none)`, which counts tables exactly.

GREEN — same command:

```
11 passed in 0.03s
```

CLI dispatch probed without running either real mode — `uv run python tests/fixtures/replay/_cut_p4_fixtures.py bogus`:

```
unknown mode 'bogus'; expected no argument or 'evidence'
```
(exit 1)

## Suite line (verbatim)

`uv run pytest -q tests/cobalt tests/taxonomy`:

```
1764 passed, 322 skipped, 1 xfailed, 15 warnings in 54.30s
```

Tree after the run: `M tests/fixtures/replay/_cut_p4_fixtures.py`, `?? tests/cobalt/test_p4_asset_type_evidence.py` (plus the hub's own `M docs/40 - DevDocs/reports/s2-p4-verify-2026-09-19.md`, untouched by me) — and this report. `scratch/` is gitignored; no evidence output exists yet.

## ESCALATE

**1. The disagreement path has no real-artifact coverage.** No committed fixture contains a row with a non-blank `Asset Type` or an `Industry = Exchange Traded Fund` — the radar export's 20 rows are all blank/non-fund. So the A/B/C ROW logic (the part the hub's real-cache run will actually print) is proved only by `test_render_shapes_a_non_empty_table`, which builds `EvidenceReport` objects directly and asserts the markdown shape. That is a renderer unit test, not a parser tested against an invented export, so it does not breach L45 — but it is the honest limit of what this chunk could prove, and it was written AFTER the implementation, so it has no red line of its own. The hub's own run against the real cache is the first real exercise of those rows. If step 2.5 re-cuts the movers fixtures from 151-column exports containing a non-blank `Asset Type` row, that fixture should be added to this test module and the coverage closes.

**2. `_cut_p4_fixtures.py` has no DevDoc.** `docs/40 - DevDocs/tests/fixtures/` holds `radar/_cut_panel_fixtures.md` only; there is no `replay/_cut_p4_fixtures.md`, and the new test module has no `docs/40 - DevDocs/tests/cobalt/test_p4_asset_type_evidence.md`. Pre-existing for the cutter, new for the test file. DevDocs are a sprint-close job and the brief did not ask for them, so I wrote neither — flagging both for the close.

## Not done, and why

- Did not run `evidence` mode against `/Users/cobalt/cobalt/data/radar-cache/` — the brief reserves that for the hub. I also never listed or read that directory (the attempt was refused by the sandbox, correctly), so `RADAR_CACHE_DIR`'s existence and contents are unverified from here; a missing directory fails loud with the path.
- Did not commit (brief).
- Did not touch any fixture, `src/`, config, or any `scratch/` file.
