# `src/cobalt/session/store.py`

## What it does
Persistence for `market_reset` refusals — the heartbeat-visible counter
SPRINT-LADDER §S1 F1 asks for.

## Why a table and not an in-process counter
The writers are separate processes with separate lifetimes: the ASET web
app is resident, `prefill-daily` and `prefill-drc` are launchd one-shots.
An in-process counter is invisible to the heartbeat by construction. A
row per refusal is durable, survives a restart, answers the heartbeat as
a `count(*)` over a window — and doubles as the audit trail of what was
refused, by whom, and against what target.

## Key functions/classes
- `HEARTBEAT_WINDOW_KEY = "session.blocks.heartbeat_window"` — F16: the
  lookback is a tunables row (1440 min), not a `timedelta(hours=24)` in
  a method body.
- `SessionBlockStore(db_name=None)` — `db_name` is the test/tooling seam
  only; production and dev both take the database from `COBALT_ENV` via
  `env.resolve_db_name()` (RULING 7/9).
- `.ensure_schema()`, `.record(...)`, `.count_since(ts)`,
  `.count_over_window(now=None)`, `.recent(limit)`.

## The degradation rule
`record()` returns `None` and logs at `ERROR` if the database is
unreachable. It never raises. By the time it is called the block has
already been decided — and a database outage turning a hard block into a
pass is the failure mode that would actually hurt. Loud, and
non-blocking, in that order.

## Schema
`migrations/0001_session_blocks.sql` — `id`, `ts`, `session`, `actor`,
`target`, `reason`, plus a `ts DESC` index. **Append-only**; nothing
updates a row.

## Tests
`tests/cobalt/test_session.py::test_the_block_is_recorded_for_the_heartbeat`
and `::test_a_dead_database_loses_the_counter_row_not_the_block`.

---

## 2026-09-08 — ADR-0008 (two-layer data model)

Declares `SIDE = Side.SYSTEM` (ADR-0008 D2 — the side is chosen PER STORE, never per process).
the market_reset block is a system rule and its audit trail is system data.

`_connect()` passes it to the factory; `ensure_schema()` asserts the two-layer schemas exist before running its own DDL, naming `cobalt db migrate` if they do not.
