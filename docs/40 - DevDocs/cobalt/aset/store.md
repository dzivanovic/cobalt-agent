# `src/cobalt/aset/store.py`

## What it does
Persistence for computed sizings. Every completed `/size` POST is saved
here before the sheet auto-appends to the daily note — this is the
future EV/Guardian training truth (TRIAGE pre-beta increment 1). DDL
lives under `migrations/` (one path — this module executes those files,
it does not carry a second copy of the schema).

**Iteration 4 (2026-08-28, ruled by Dejan):** a new migration,
`0002_aset_sizings_sheet_mode.sql`, adds `sheet_mode` and drops the
retired `daily_stop`/`risk_pct` columns. This forced `ensure_schema()`
to become a real multi-file, multi-statement runner instead of a single
`conn.execute(file.read_text())` call — psycopg's `execute()` only runs
one statement at a time, so 0002's three `ALTER TABLE` statements can't
be handed over as one call the way 0001's single `CREATE TABLE` could.
**Real bug caught during this change:** a naive `split(";")` on the raw
file text broke, because 0002's own header comment contains a semicolon
mid-sentence ("...(they simply have no sheet_mode); daily_stop and
risk_pct are dropped..."), which merged two statements into one invalid
string. Fixed by stripping full-line `--` comments *before* splitting
on `;` — verified against a live `cobalt_dev` run. The consequence:
**a migration file must never put a trailing comment after SQL on the
same line** — only full-line comments are stripped.

## Key functions/classes
- `MIGRATIONS_DIR` — the migrations directory; `ensure_schema()` globs
  `*.sql` inside it and sorts by filename, so `0001_...` always runs
  before `0002_...`.
- `AsetStore(db_name="cobalt_dev")` — thin wrapper around
  `cobalt.db.connect(self.db_name)`. Never called with `"cobalt_brain"`
  anywhere in the ASET codebase; `db.connect` would refuse it anyway.
  - `.ensure_schema()` — for each migration file (sorted, ascending):
    strips full-line `--` comments, splits the remainder on `;`,
    executes each non-empty statement individually. Idempotent
    (`CREATE TABLE IF NOT EXISTS`, `ADD/DROP COLUMN IF EXISTS`), called
    on every `/size` POST before insert.
  - `.save(result: SizingResult) -> int` — inserts one row into
    `aset_sizings` (now including `sheet_mode`, no longer `daily_stop`/
    `risk_pct`), returns the new row's `id`. Raises `RuntimeError` if
    the `INSERT ... RETURNING id` somehow returns no row — a persistence
    failure surfaces loudly, never silently.
  - `.recent(limit=10) -> list[dict]` — reads back the most recent rows
    (used by the integration test to verify a round trip; not currently
    exposed in the web UI). Selects `sheet_mode` in place of the old
    `daily_stop`.
  - `.for_date(day: date) -> list[dict]` — **(Slice 2)** every card
    whose `created_at` falls on `day` **in America/New_York**, not the
    DB session's UTC default (`(created_at AT TIME ZONE
    'America/New_York')::date = %s`) — Dejan's actual trading-day
    boundary. Ordered oldest-first: `prefill/drc.py`'s re-entry
    numbering (entry #1/#2/#3+) depends on chronological order within a
    ticker.

## Data flow in/out
**In:** a `SizingResult` (from `engine.compute_sizing`).
**Out:** the new row's integer `id`, or a raised exception (connection
failure, schema failure, or the `RuntimeError` above). Writes to the
`aset_sizings` table in whichever Postgres database `db_name` names
(`cobalt_dev` in every real call site).

## Config it reads
None directly — `db_name` is passed in by the caller (`web.py`, from
`AsetConfig.db_name`); actual connection parameters come from
`cobalt.db.connect`'s environment-variable read.
