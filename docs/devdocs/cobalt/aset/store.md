# `src/cobalt/aset/store.py`

## What it does
Persistence for computed sizings. Every completed `/size` POST is saved
here before the sheet renders success — this is the future EV/Guardian
training truth (TRIAGE pre-beta increment 1). DDL lives in exactly one
place (`migrations/0001_aset_sizings.sql`); this module executes that
file rather than carrying a second copy of the schema (one-path rule).

## Key functions/classes
- `MIGRATION_SQL` — path to the one DDL file.
- `AsetStore(db_name="cobalt_dev")` — thin wrapper around
  `cobalt.db.connect(self.db_name)`. Never called with `"cobalt_brain"`
  anywhere in the ASET codebase; `db.connect` would refuse it anyway.
  - `.ensure_schema()` — runs the migration SQL (`CREATE TABLE IF NOT
    EXISTS`), idempotent, called on every `/size` POST before insert
    (cheap enough at this scale; avoids a separate migration-runner
    dependency for slice 1).
  - `.save(result: SizingResult) -> int` — inserts one row into
    `aset_sizings`, returns the new row's `id`. Raises `RuntimeError` if
    the `INSERT ... RETURNING id` somehow returns no row — a persistence
    failure surfaces loudly, never silently.
  - `.recent(limit=10) -> list[dict]` — reads back the most recent rows
    (used by the integration test to verify a round trip; not currently
    exposed in the web UI).

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
