# `src/cobalt/archiver/runner.py`

## What it does
Orchestrates a full Bar Archiver run: sequential, gentle-rate, one
`(ticker, interval)` at a time, fail-loud per target — a single
ticker's failure is logged and counted, never silently skipped and
never allowed to abort the rest of the run. Also the `archiver` CLI
entry point (`[project.scripts]` in `pyproject.toml`).

## Key functions/classes
- `GENTLE_SLEEP_SECONDS = 1.2` — the rate; matches the Data-Source
  Spike probes' own rate.
- `_run_targets(targets, mode) -> RunSummary` — the shared
  engine: resolves the Finviz token once (not per-request), ensures the
  `bars` schema exists once, then for each target: `fetch_bars` →
  `upsert_bars` → record success, or catch `CollectorError` (or any
  other exception — never lets an unexpected error type escape and
  abort the loop) → record failure and log it loudly. Sleeps between
  targets, not after the last one.
- `run_full() -> RunSummary` — the nightly job:
  `WatchlistsConfig.archive_targets()` (tier_a + tier_b, tier_c
  excluded), run, append the report.
- `run_backfill(ticker) -> RunSummary` — the
  on-demand path: `WatchlistsConfig.backfill_targets(ticker)` (always
  tier_a's 5 intervals, regardless of the ticker's actual tier), run,
  append the report.
- `main()` — sets `LOGURU_LEVEL=INFO` before any import that pulls in
  loguru (same rationale as `aset/__main__.py` — cheap standing
  insurance against the old tree's since-fixed DEBUG secret dump),
  parses `--backfill TICKER`, runs the appropriate
  coroutine, and exits non-zero if the run had any failures (so a
  launchd/cron wrapper can detect a bad night from the exit code alone,
  even before a human reads the report).

## Data flow in/out
**In:** `configs/cobalt/watchlists.yaml` (via `load_config()`), the
Finviz vault token (via `collector.resolve_token()`).
**Out:** rows written to `bars` in the database `COBALT_ENV` names, one appended line in
`docs/30 - Design/archiver-runs.md`, loguru output to stdout/whatever
redirects it (the launchd plist, in production).

## Config it reads
`configs/cobalt/watchlists.yaml`, indirectly via `archiver.config`. The
database is **not** configurable here and is not a parameter anywhere in
this module.

## Gotchas
- **The database is not an argument (RULING 9, 2026-09-04).** This
  module used to thread `db_name="cobalt_dev"` through every entry point
  and expose it as a `--db-name` CLI flag. Those are deleted, not
  re-pointed: a per-run override of the target database is the same hole
  RULING 7 closed for `AsetConfig.db_name`, and `test_env.py`'s
  `test_archiver_runner_exposes_no_database_override` fails if either
  the parameters or the flag come back.
- `com.cobalt.archiver` is a **`StartCalendarInterval` batch job**
  (Mon–Fri 20:30 local) with `RunAtLoad=false`, not a resident
  collector. Booting it out mid-session interrupts nothing unless a run
  is actually in flight — the day's bars are fetched from Finviz history
  in one pass at 20:30, so the job only has to be loaded *by* 20:30, not
  continuously.
