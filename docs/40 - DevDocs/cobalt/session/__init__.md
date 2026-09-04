# `src/cobalt/session/`

## What it does
The **F1 session clock** (Charter §3 F1, SPRINT-LADDER §S1) — the one
place that knows what time it is for Cobalt. Answers two questions about
any tz-aware instant: *which session is this* (`premarket` / `rth` /
`aftermarket` / `market_reset` / `overnight`) and *when does that
change*. Also enforces the `market_reset` hard block on every write path.

Charter's rule, verbatim: "every card, alert and note carries the
session … no feature keys off wall-clock."

## Modules
| File | Purpose |
|---|---|
| `models.py` | `Session` enum (5 values, total and exclusive) + `BLOCKED_SESSION`. |
| `calendar.py` | `nyse-<year>.yaml` → `TradingCalendar`. Holidays, early closes, weekends. Fail-loud on an uncovered year. |
| `clock.py` | `SessionClock` — boundaries from tunables, days from the calendar, `session()` / `next_boundary()`. Owns `now_utc()`, the one system-clock read. |
| `guard.py` | `assert_writable()` — the `market_reset` refusal, its log line, its counter row. |
| `store.py` | `session_blocks` — the durable, heartbeat-visible refusal counter. |
| `cli.py` | `cobalt session now / backfill / blocks`. |
| `migrations/0001_session_blocks.sql` | The counter table. |

## The three laws, one per module
- **`clock.py`: sessions are ET, storage is UTC, naive is refused.** Not
  a convention — a precondition. ADR-0007 had to reinterpret 4.75M
  `bars` rows because a naive ET wall clock reached a `timestamptz`
  column and Postgres labelled it UTC. `SessionClock.to_et()` raises on
  a naive datetime and names that ADR in the message.
- **`calendar.py`: the calendar is config, and an uncovered year is a
  crash.** No "weekday ⇒ trading day" fallback: that fallback is wrong
  exactly on the days that matter (Labor Day is a Monday), and it would
  resolve a holiday to `rth` silently.
- **`guard.py`: `market_reset` is a refusal, not a warning.** With a log
  line and a `session_blocks` row behind it, because the heartbeat
  (F18, S1-P3) has to be able to see it from another process.

## The day is a walk, not a case analysis
`SessionClock.windows_for(day)` builds the day's ordered `[start, end)`
windows and `session()` walks them. Consequences that fall out for free
rather than being special-cased:
- a weekend or a holiday returns **no windows**, so the whole day is
  `overnight`;
- an **early close** simply ends its RTH window at 13:00 and its
  aftermarket at 17:00 — and the 17:00–20:00 gap before `market_reset`
  falls through to `overnight` the same way 02:00 does;
- `market_reset` is **not** moved on a half day, because the archiver
  still runs at 20:30.

## Config it reads
- `configs/cobalt/taxonomy/tunables.yaml` — eight `session.*` rows,
  `unit: time` (ET "HH:MM"), each with a named consumer. F16: this
  module is nothing but boundary predicates, so a literal clock time
  anywhere in it would be the whole violation.
- `configs/cobalt/calendar/nyse-2026.yaml` — holidays and early closes.
  Weekends are derived, never listed.

Both are checked by `cobalt validate`.

## Who calls it
- `cobalt/vaultwrite/writer.py` — `_session_gate()` on `create_if_absent`,
  `upsert_unit`, `upsert_region`; every write stamps `vault_writes.session`.
- `cobalt/aset/web.py` — `/size` and `/fill` refuse during `market_reset`.
- `cobalt/aset/store.py` — `save()` stamps `aset_sizings.session`.
- `cobalt/cli.py` — mounts the `session` command group and `validate`.

## Tests
`tests/cobalt/test_session.py` — 60 cases. Time is **frozen, never
slept**: every case builds an explicit tz-aware instant.

## Gotchas
- **`session_clock()` is `lru_cache`d.** A tunables or calendar edit
  needs a process restart — which is L28's restart-on-deploy rule
  anyway. Tests that mutate the registry patch
  `cobalt.session.clock.load_tunables` and build a clock directly.
- **The suite freezes `now_utc` autouse** (`conftest.FROZEN_NOW`,
  2026-09-03 10:00 ET). Without it the whole suite would go red for one
  hour every evening, which is not a test.
- **`session_blocks` is append-only.** Nothing updates a row.
