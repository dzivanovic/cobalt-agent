# `src/cobalt/archiver/report.py`

## What it does
Writes the one visible artifact every Bar Archiver run produces: one
appended row in `docs/30 - Design/archiver-runs.md`. Fail-loud
*alerting* can come later (per the task that created this component) —
this is the current minimum: a human-readable, append-only record of
date, mode, **database**, tickers, requests, rows written, failure
count, and duration.

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
- `COLUMNS` / `_RULE` — the 8-column header row and its separator.
  `COLUMNS` doubles as the schema marker: its absence from an existing
  file is what triggers the one-time break below.
- `HEADER` — the markdown title, a one-line description, and the table
  header + separator row. Written exactly once, on first creation.
- `SCHEMA_BREAK` — appended ONCE to a pre-RULING-9 file: a short note
  plus a fresh 8-column header, so the log gains a second table instead
  of 8-column rows misaligning under the old 7-column header. Existing
  rows are never rewritten.
- `RunSummary(mode, db_name=None)` — accumulates one run's stats:
  `mode` (`"full"` or `"backfill:<ticker>"`), `db_name` (resolved once
  at construction from `env.resolve_db_name()`, the same source
  `BarStore` uses, so the log cannot disagree with where rows actually
  went), `started_at`, the set of distinct tickers
  touched, total requests, total rows written, and a list of failure
  strings (kept in-memory for logging; only the *count* reaches the file).
  - `.record_success(ticker, rows)` / `.record_failure(ticker, interval,
    error)` — called once per `(ticker, interval)` attempt by `runner.py`.
  - `.duration_str()` — `"18m32s"`-style, computed from `started_at` to
    call time.
- `append_run_report(summary) -> Path` — writes the header if the file
  is new, else the schema break if the file predates the Database
  column, then appends exactly one row. Returns the path (logged by
  the runner).

## Data flow in/out
**In:** a populated `RunSummary`.
**Out:** appends to (or creates) `docs/30 - Design/archiver-runs.md`.
No other side effects.

## Config it reads
None — `REPORT_PATH` is a fixed, computed constant, not configurable.
`COBALT_ENV` is read indirectly, through `env.resolve_db_name()`.

## Gotchas
- **Why a Database column exists (RULING 9, 2026-09-04).** The archiver
  wrote production bars into `cobalt_dev` for three weeks and this log
  could not show it, because no column named a database. Every row now
  states its target. Rows above the schema break were all written to
  `cobalt_dev`.
- The `SCHEMA_BREAK` is the one deliberate exception to the
  "strictly tabular, never interleaved" rule above. It is written at
  most once per file, and it opens a *new* table rather than
  interrupting the old one — so both tables still render.
