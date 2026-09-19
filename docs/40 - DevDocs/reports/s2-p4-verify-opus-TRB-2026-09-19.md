# S2-P4 TR-B — K9 compares against the rows the export really had (2026-09-19)

## §0 Headline
- **BUILT.** The replay result now records, per side, what the export really had (`exported`), the cap in force (`top_n`) and `expected = min(top_n, exported)`; K9 is six rows (three per side) whose `compare` asserts stored = expected. A short side PASSES, a side below what its export allowed FAILS; `top_n not_null` and `not_archived = 0` still asserted, tenancy unchanged.
- The STOP sentence did **not** trigger: nothing selects, ranks or scores. Proof below — HEAD's own `parse_movers`, executed out of git, returns byte-identical rows at 8 caps × 2 sides, and the diff touches no line of `benchmark_misses`, `archive_movers` or `MoversStore`.
- Offline suite `1796 passed, 324 skipped, 1 xfailed, 15 warnings in 55.16s` (0 failed; TR-A's 1788 + 8 new).
- ESCALATE: 0. NOT DONE HERE (no DB, no `.env`, L41 interim): the two new K9 statements have never been executed — `test_committed_queries_run_read_only_on_cobalt_dev` (`requires_db`) is their first real run; `cobalt validate` not run, I launch nothing (L36). No commit.

## Files changed
| file | change |
|---|---|
| `src/cobalt/replay/models.py` | `MoversExport.exported_rows` + its validator; new `MoversSideCount` (`exported`, `top_n`, `expected`, validated as `min`); `ReplayResult.movers_by_side: dict[Side, MoversSideCount]`; `__all__` |
| `src/cobalt/replay/movers.py` | `parse_movers` passes `exported_rows=len(rows)`; new `export_counts(exports, *, top_n)`; module docstring paragraph; `__all__` |
| `src/cobalt/replay/runner.py` | one statement in `movers_step`: `result.movers_by_side = export_counts(exports, top_n=settings.top_n)`, between the exports and the first write |
| `configs/cobalt/smoke/s2.yaml` | K9 → K9.1…K9.6 (+ the block comment explaining the split); file-header line listing all three `compare` rows |
| `tests/cobalt/test_replay_movers.py` | 3 tests + imports |
| `tests/cobalt/test_replay_runner.py` | 3 tests + import |
| `tests/cobalt/test_smoke.py` | 2 tests + helpers (`K9_SIDES`, `_k9_trio`, `_k9_deps`) |
| `docs/40 - DevDocs/cobalt/replay/{models,movers,runner}.md` | DevDocs for every changed `.py` |
| `docs/40 - DevDocs/cobalt/smoke/{config,models}.md` | the K9 paragraph (the old text described the hand count of the cached CSV) and the compare-shape sentence — docs edits with no `.py` change, flagged |

`git diff --stat`: 12 files changed, 483 insertions(+), 28 deletions(-). Nothing outside the bound: no migration, no `radar/**`, no scoring or ranking code, no other smoke check besides the header line naming K8.3, no dependency, no commit.

## The K9 rewrite, row by row
| row | kind / side | asserts | prints |
|---|---|---|---|
| K9.1 | `sql` user | `top_n not_null`, `not_archived = 0` for the day's active **gainers** | `stored` |
| K9.2 | `job_row` system | `movers_by_side` present, `trade_date = {last_trading_day}` | `movers_by_side.gainers.expected` |
| K9.3 | `compare` | K9.1 `eq` K9.2 | both numbers |
| K9.4–K9.6 | the same three for **losers** | | |

Why six rows and not one: the stored rows live in `system.movers_daily` (granted to `cobalt_user` by `0008`) and the night's export row count lives in `system.cobalt_jobs.last_result`, which the user role is never granted — the same wall that split K8, answered the same way (no new grant; `test_no_smoke_check_reads_across_the_tenancy_wall_it_declares` stays green and still derives the granted set from the migrations). Why per side and not one pair: `result_number` names ONE number per check, and the ruling is per side. `side` is CHECK-constrained to `gainers|losers` (`0008`), so the two `not_archived = 0` predicates together still cover every active row of the day.

Verdict change, exactly: old K9 failed `full_sides eq true` whenever either side held fewer than `top_n` rows and deferred the difference to a hand count of `data/radar-cache/<date>/movers-<side>-*.csv`. Now a side whose export really returned fewer rows than `top_n` PASSES (the plan's "or fewer with export evidence", line ≈230), and a side holding fewer rows than its export allowed FAILS.

Rendered hand commands (R6 A), from the shipped file:

```
--- K9.1 [sql] movers_daily — gainers stored (user side)
uv run cobalt db query --side user --prod --format json 'SELECT (SELECT (value ->> 'top_n')::int FROM trader_settings WHERE key = 'radar.benchmark') AS top_n, count(*) AS stored, count(*) FILTER (WHERE NOT bars_archived) AS not_archived FROM system.movers_daily WHERE trade_date = DATE '2026-09-22' AND side = 'gainers' AND active'
--- K9.3 [compare] movers — gainers stored = what the export allowed
# compare K9.1 eq K9.2 — run both rows above; their two printed numbers must be eq
```
(quoting simplified for this report; the real render doubles the shell quotes — see `scratch/render_k9.py`.)

Two deliberate consequences: K9.2 and K9.5 render the same `cobalt_jobs` read, as K7 and K8.1 already do — a job row is read per row that asks it something, and each prints its own number. And a pre-2026-09-19 replay result (no `movers_by_side`) gives K9.2/K9.5 a FAIL naming the key and K9.3/K9.6 an ERROR, never a quiet PASS; that case is asserted.

## Tests added (names)
| file | test |
|---|---|
| `test_replay_movers.py` | `test_the_export_records_how_many_rows_it_really_had_and_keeps_the_same_top_rows` |
| `test_replay_movers.py` | `test_export_counts_record_min_top_n_exported_per_side` |
| `test_replay_movers.py` | `test_export_counts_refuse_a_disagreement_and_a_repeated_side` |
| `test_replay_runner.py` | `test_the_result_records_what_each_export_had_and_how_many_rows_that_allows` |
| `test_replay_runner.py` | `test_a_dry_run_and_a_retained_export_run_record_the_counts_too` |
| `test_replay_runner.py` | `test_the_recorded_counts_round_trip_through_job_result` |
| `test_smoke.py` | `test_the_shipped_k9_compares_the_stored_count_against_what_the_export_allowed` |
| `test_smoke.py` | `test_k9_passes_a_short_side_and_fails_a_stored_count_below_what_the_export_allowed` |

Against the brief's list, row by row: a short side passes (`stored=18, exported=18, top_n=25` → PASS, both sides) · a full side passes (`stored=25, exported=151` → PASS) · a stored count below `min(top_n, exported)` fails (`stored=17, exported=18` → the compare FAILs, AMBER) · the result model round-trips (`ReplayResult.model_validate(result.job_result()) == result`) · the shipped `s2.yaml` still loads (every test above loads it through `load_suite`). Extra: `not_archived = 1` still FAILs the sql row; a result without `movers_by_side` → FAIL + ERROR (RED); a job row for another day → FAIL naming `trade_date`; the cap above and below the export (runner, both recorded); dry run and the retained `--date` run both record the counts.

## Red before, green after
Tests were written first and run against the unchanged code.

```
tests/cobalt/test_replay_movers.py:42: in <module>
    from cobalt.replay.models import (
E   ImportError: cannot import name 'MoversSideCount' from 'cobalt.replay.models' (/Users/cobalt/cobalt-wt/s2-p4/src/cobalt/replay/models.py)
ERROR tests/cobalt/test_replay_movers.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
55 deselected, 1 error in 0.32s
```

```
FAILED tests/cobalt/test_replay_runner.py::test_the_result_records_what_each_export_had_and_how_many_rows_that_allows - AttributeError: 'ReplayResult' object has no attribute 'movers_by_side'
FAILED tests/cobalt/test_replay_runner.py::test_a_dry_run_and_a_retained_export_run_record_the_counts_too - AttributeError: 'ReplayResult' object has no attribute 'movers_by_side'
FAILED tests/cobalt/test_replay_runner.py::test_the_recorded_counts_round_trip_through_job_result - KeyError: 'movers_by_side'
FAILED tests/cobalt/test_smoke.py::test_the_shipped_k9_compares_the_stored_count_against_what_the_export_allowed - AssertionError: assert 'K9' not in {'K1': LaunchctlCheck(id='K1', title='co...
FAILED tests/cobalt/test_smoke.py::test_k9_passes_a_short_side_and_fails_a_stored_count_below_what_the_export_allowed - KeyError: 'K9.1'
5 failed, 55 deselected in 0.53s
```

After the edit, the same eight:

```
tests/cobalt/test_smoke.py::test_the_shipped_k9_compares_the_stored_count_against_what_the_export_allowed PASSED
tests/cobalt/test_smoke.py::test_k9_passes_a_short_side_and_fails_a_stored_count_below_what_the_export_allowed PASSED
tests/cobalt/test_replay_movers.py::test_the_export_records_how_many_rows_it_really_had_and_keeps_the_same_top_rows PASSED
tests/cobalt/test_replay_movers.py::test_export_counts_record_min_top_n_exported_per_side PASSED
tests/cobalt/test_replay_movers.py::test_export_counts_refuse_a_disagreement_and_a_repeated_side PASSED
tests/cobalt/test_replay_runner.py::test_the_result_records_what_each_export_had_and_how_many_rows_that_allows PASSED
tests/cobalt/test_replay_runner.py::test_a_dry_run_and_a_retained_export_run_record_the_counts_too PASSED
tests/cobalt/test_replay_runner.py::test_the_recorded_counts_round_trip_through_job_result PASSED
======================= 8 passed, 79 deselected in 0.66s =======================
```

## The proof: the movers stored and scored are unchanged
**(1) From the diff.** `git diff -U0 src/cobalt/replay/` reports six hunks in `models.py`, five in `movers.py`, two in `runner.py`. None is inside `benchmark_misses`, `archive_movers`, `MoversStore.reconcile`/`active`/`mark_bars_archived`, `MoversCollector.exports`, `retained_exports`, or the row-building loop of `parse_movers` — those functions have **zero changed lines**. The single changed line inside `parse_movers` is the constructor call, where the selection expression survives verbatim:

```
-        header=tuple(header), rows=tuple(rows[:top_n]), source=source, cache_path=cache_path,
+        header=tuple(header), rows=tuple(rows[:top_n]), exported_rows=len(rows), source=source,
+        cache_path=cache_path,
```

`top_n` handling is untouched, nothing is reordered, `benchmark_misses` receives the same `stored` list, and `movers_daily` is written by the same `reconcile` call with the same `exports`.

**(2) By execution against HEAD.** `scratch/proof_rows.py` (gitignored scratch, re-runnable with `uv run python scratch/proof_rows.py`) reads HEAD's `parse_movers` **out of git**, executes it against the current module's globals with a plain record standing in for `MoversExport`, and compares every selected row field by field plus a sha256 over their canonical serialisation, on both real-shape fixtures at eight caps:

```
gainers  top_n=   1  rows=  1  exported_rows= 60  identical=True  d8adf278b0ae8b40
gainers  top_n=  25  rows= 25  exported_rows= 60  identical=True  8fcdf14e58a56fb8
gainers  top_n=  60  rows= 60  exported_rows= 60  identical=True  538d890414e94eea
gainers  top_n=1000  rows= 60  exported_rows= 60  identical=True  538d890414e94eea
losers   top_n=  25  rows= 25  exported_rows= 60  identical=True  940837e66b300c41
losers   top_n=1000  rows= 60  exported_rows= 60  identical=True  90bc329d508536fe
ALL IDENTICAL
```
(16 lines in full: sides × `top_n` ∈ 1, 5, 10, 25, 59, 60, 61, 1000 — all `identical=True`.)

**(3) By the pre-existing tests.** Every mover assertion that names real tickers, ranks and gates — `test_tesla_class_mover_absent_from_pool_appears_in_miss_line_with_excluded_by` (QNME rank 2, `mover_id=2`, `+92.25%`), `test_nightly_report_lists_misses_…`, the archive and reconcile tests — is unchanged and green.

**(4) Fail-loud, if it ever stops being true.** `export_counts` refuses when an export's kept rows disagree with `min(top_n, exported_rows)`; a future change to the selection would crash the movers step instead of writing a quiet wrong count.

## What I could not do
1. **Neither new K9 statement has been RUN.** No database and no credentials here (L41 interim). They load and validate offline (`guard_select`, `load_suite`); the hub's `COBALT_ENV=dev` run of `test_committed_queries_run_read_only_on_cobalt_dev` is their first execution against real DDL. The spot to watch is `trader_settings` resolving unqualified under the user role's `search_path` — carried over verbatim from the old K9, not introduced here.
2. **No production `job.result` carries `movers_by_side` yet.** Until the next `com.cobalt.replay` run after deploy, K9.2/K9.5 read FAIL and K9.3/K9.6 ERROR (RED) — the intended loud behaviour, but it means K9 is not GREEN on a report generated before that run. Worth naming in the deploy order.
3. **`cobalt validate` not run** — no `.env` here and I launch nothing (L36).
4. **Two docs edits outside the "changed `.py`" rule**: `smoke/config.md` and `smoke/models.md`, whose K9/compare paragraphs described the removed hand count. Flagged, same precedent as TR-A.
