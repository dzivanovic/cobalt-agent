# `src/cobalt/session/clock.py`

## What it does
The session resolver. Converts a tz-aware instant to ET, walks the day's
ordered windows, and returns the `Session` it falls in — plus
`next_boundary()`, which walks forward over weekends and holidays.

Also owns **`now_utc()`, the one system-clock read in the new core**.

## Key functions/classes
- `ET = ZoneInfo("America/New_York")` — sessions are defined here and
  nowhere else.
- `BOUNDARY_KEYS` — the eight `session.*` tunables rows this module reads.
- `MAX_CLOSED_RUN_DAYS = 400` — the forward-walk safety bound. Named,
  and deliberately **not** a tunables row: it asserts the exchange does
  not close for a year, and if it trips the answer is a broken calendar,
  not a number to tune.
- `now_utc() -> datetime` — the single system-clock read. Callers reach
  it as `clock.now_utc()` **through the module**, never by importing the
  name, so one `monkeypatch.setattr` freezes time for all of them.
- `Window(session, start, end)` — one `[start, end)` ET wall-clock span.
- `SessionClock`
  - `.from_config(calendar=None)` — reads the tunables rows, checks each
    is `unit: time`, parses `HH:MM`, then `_assert_ordered()`.
  - `.windows_for(day)` — the day's ordered windows; `[]` on a
    weekend/holiday.
  - `.session(ts)` — the answer. Raises on a naive `ts`.
  - `.next_boundary(ts)` — `(when_utc, next_session)`.
  - `.to_et(ts)` / `.describe(ts)`.
- `session_clock()` — `lru_cache(1)` process-wide instance.
- `current_session(now=None)`.

## Boundary semantics
Inclusive of its own minute, exclusive of the next. `09:29:59` is
`premarket`; `09:30:00` is `rth`. That pair is a test.

## `_assert_ordered()` — what a bad config edit hits
Two ordered chains are checked (full day and early-close day), plus one
equality: `session.market_reset_open` **must equal**
`session.aftermarket_close`. On a full day those are the same instant by
design; letting them drift would insert an unnamed `overnight` sliver
into the middle of the trading evening, and nothing downstream would
notice. An early close opens such a gap on purpose — which is why the
rule is stated on the *full-day* pair only.

## Config it reads
Eight rows in `configs/cobalt/taxonomy/tunables.yaml`
(`session.premarket_open`, `.rth_open`, `.rth_close`,
`.aftermarket_close`, `.market_reset_open`, `.market_reset_close`,
`.early_close.rth_close`, `.early_close.aftermarket_close`), each
`unit: time`, plus the calendar via `calendar.load_calendar()`.

## Safety properties
- **A naive datetime is refused, not guessed.** The message names
  ADR-0007 — the 4.75M-row correction that this precondition exists to
  prevent recurring.
- **No built-in boundary.** Delete `session.rth_open` from the registry
  and `from_config()` raises; there is no 09:30 anywhere in the module.
- **A wrong unit is refused.** A row that says `min` instead of `time`
  crashes rather than being coerced.

## Tests
`tests/cobalt/test_session.py` — the Charter acceptance trio (18:30 →
aftermarket, 21:30 → overnight, 20:30 → refused), a 12-case boundary
sweep, the 09:29:59/09:30:00 pair, Saturday/Sunday, Labor Day, the
2026-11-27 early close in eight positions, the same UTC hour resolving
differently in EST and EDT, naive/non-datetime refusals, and six
`next_boundary` walks including Friday-night-over-a-holiday-Monday.

## Gotchas
- `next_boundary` returns its instant in **the caller's tzinfo**, not
  forced to UTC. `cobalt session now` converts to ET for display.
- The `lru_cache` means a config edit needs a restart.
