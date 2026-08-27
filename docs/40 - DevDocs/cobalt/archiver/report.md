# `src/cobalt/archiver/report.py`

## What it does
Writes the one visible artifact every Bar Archiver run produces: one
appended row in `docs/30 - Design/archiver-runs.md`. Fail-loud
*alerting* can come later (per the task that created this component) —
this is the current minimum: a human-readable, append-only record of
date, mode, tickers, requests, rows written, failure count, and duration.

**Deliberately kept strictly tabular** — every write is exactly one
markdown table row, never interleaved with other content (no per-
failure detail lines between rows). A markdown table's rows must stay
contiguous to render; since this file is appended to forever, anything
non-tabular inserted after one run's row would break the table for
every run that follows. Full per-ticker failure text goes to
stdout/loguru (the launchd job's own log file) instead — the Failures
column here is a count, not a list.

## Key functions/classes
- `REPORT_PATH` — `docs/30 - Design/archiver-runs.md`, resolved via
  `archiver.config.REPO_ROOT`.
- `HEADER` — the markdown title, a one-line description, and the table
  header + separator row. Written exactly once, on first creation.
- `RunSummary` — accumulates one run's stats: `mode` (`"full"` or
  `"backfill:<ticker>"`), `started_at`, the set of distinct tickers
  touched, total requests, total rows written, and a list of failure
  strings (kept in-memory for logging; only the *count* reaches the file).
  - `.record_success(ticker, rows)` / `.record_failure(ticker, interval,
    error)` — called once per `(ticker, interval)` attempt by `runner.py`.
  - `.duration_str()` — `"18m32s"`-style, computed from `started_at` to
    call time.
- `append_run_report(summary) -> Path` — writes the header if the file
  is new, then appends exactly one row. Returns the path (logged by
  the runner).

## Data flow in/out
**In:** a populated `RunSummary`.
**Out:** appends to (or creates) `docs/30 - Design/archiver-runs.md`.
No other side effects.

## Config it reads
None — `REPORT_PATH` is a fixed, computed constant, not configurable.
