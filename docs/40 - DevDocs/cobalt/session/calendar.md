# `src/cobalt/session/calendar.py`

## What it does
Loads `configs/cobalt/calendar/nyse-<year>.yaml` (globbed, one file per
year) into a `TradingCalendar` that answers three questions about a
date: is it a weekend, is it a holiday, is it an early close.

## Key functions/classes
- `CalendarError(RuntimeError)` — missing, invalid, or **asked about an
  uncovered year**.
- `CalendarDay` — `{date, name}`, `extra="forbid"`.
- `CalendarYear` — `{year, holidays[], early_closes[]}`. Validates that
  every date belongs to the file's own year, that no date is both a
  holiday and an early close, and that neither list repeats a date.
- `TradingCalendar` — `.covered_years`, `.holiday_count`,
  `.early_close_count`, `.is_weekend`, `.holiday_name`,
  `.early_close_name`, `.is_early_close`, `.is_trading_day`,
  `.describe(day)`.
- `load_calendar(directory=CALENDAR_DIR)`.

## Safety properties
- **Coverage is explicit and fail-loud.** Ask about 2031 with no
  `nyse-2031.yaml` and it raises, naming the year, the loaded years, and
  the file to create. It never falls back to "weekday ⇒ trading day":
  that guess is wrong precisely on holidays, and a holiday resolving to
  `rth` would silently corrupt every count keyed off the session.
- **No files = crash.** An empty calendar directory is not an empty
  calendar.
- **One file per year.** Two files claiming the same year is an error
  (one-path rule), not a merge.
- **Weekends are derived.** Listing them would be a second source of
  truth for something `date.weekday()` already knows.

## Config it reads
`configs/cobalt/calendar/nyse-2026.yaml` — 10 holidays, 2 early closes.
The file says **which** days; `tunables.yaml` says **what time** an early
close ends. That split is deliberate: the times are thresholds (F16), the
days are an exchange fact table.

## Data provenance — NEEDS CONFIRMATION
The 2026 dates were derived, not fetched from an exchange feed, and the
file says so in its own header. One cross-check held: the 09-04 ledger
line *"Defer the landing proof to Tuesday 09-08. Available (Monday is a
holiday)"* agrees with `2026-09-07 Labor Day`. It is config, so a
correction is a one-line edit and no code change.

## Tests
`tests/cobalt/test_session.py` — Labor Day resolving to `overnight` at
10:30 while 09-08 resolves to `rth`; the 2026-11-27 early close;
year-mismatch, holiday/early-close overlap, and empty-directory
refusals; and a test that the loaded counts equal the YAML's own list
lengths (no hidden second copy).

## Gotchas
- `bars` starts 2025-08-08 and there is no `nyse-2025.yaml`, so
  `session()` over the 2025 portion of the corpus raises. Deliberate —
  add the file when a 2025 join is actually needed, with its holidays
  confirmed rather than assumed.

---

## S1-P2 addition (2026-09-04) — `nyse-2025.yaml`

S1-P1 closed with an explicit carried item: *"No `nyse-2025.yaml`, so
`session()` over the 2025 third of the bars corpus raises
`CalendarError` by design. Add the file when a 2025 join is actually
needed."* F7's card backfill and F6's prior-trading-day lookback both
walk historical rows, and ADR-0007 left ~4.75M reinterpreted `bars`
rows a third of which are 2025 — so the year is now genuinely reachable
and the file ships.

Eleven holidays and three early closes. Two entries worth noting:

- **2025-01-09, National Day of Mourning (President Carter)** — not an
  annual holiday but a one-off full closure by exchange proclamation. It
  is exactly the day a "weekday ⇒ trading day" fallback gets silently
  wrong, which is why this module refuses to have such a fallback.
- **2025-07-03 IS an early close** (unlike 2026, where July 4 fell on a
  Saturday and July 3 was the observed holiday itself).

Unlike `nyse-2026.yaml`, whose dates are derived and still carry Dejan's
confirmation flag, every 2025 date is a settled, already-observed fact.

Proof (`cobalt session now --at`), 2025-11-28, the day after Thanksgiving:

| ET instant | Session |
|---|---|
| 12:00 | `rth` (early close is still RTH until 13:00) |
| 13:30 | `aftermarket` |
