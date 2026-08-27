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
- `_run_targets(targets, mode, db_name) -> RunSummary` — the shared
  engine: resolves the Finviz token once (not per-request), ensures the
  `bars` schema exists once, then for each target: `fetch_bars` →
  `upsert_bars` → record success, or catch `CollectorError` (or any
  other exception — never lets an unexpected error type escape and
  abort the loop) → record failure and log it loudly. Sleeps between
  targets, not after the last one.
- `run_full(db_name="cobalt_dev") -> RunSummary` — the nightly job:
  `WatchlistsConfig.archive_targets()` (tier_a + tier_b, tier_c
  excluded), run, append the report.
- `run_backfill(ticker, db_name="cobalt_dev") -> RunSummary` — the
  on-demand path: `WatchlistsConfig.backfill_targets(ticker)` (always
  tier_a's 5 intervals, regardless of the ticker's actual tier), run,
  append the report.
- `main()` — sets `LOGURU_LEVEL=INFO` before any import that pulls in
  loguru (same rationale as `aset/__main__.py` — cheap standing
  insurance against the old tree's since-fixed DEBUG secret dump),
  parses `--backfill TICKER` / `--db-name`, runs the appropriate
  coroutine, and exits non-zero if the run had any failures (so a
  launchd/cron wrapper can detect a bad night from the exit code alone,
  even before a human reads the report).

## Data flow in/out
**In:** `configs/cobalt/watchlists.yaml` (via `load_config()`), the
Finviz vault token (via `collector.resolve_token()`).
**Out:** rows written to `bars` in `cobalt_dev`, one appended line in
`docs/30 - Design/archiver-runs.md`, loguru output to stdout/whatever
redirects it (the launchd plist, in production).

## Config it reads
`configs/cobalt/watchlists.yaml`, indirectly via `archiver.config`.
