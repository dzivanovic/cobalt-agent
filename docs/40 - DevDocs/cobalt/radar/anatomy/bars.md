# `src/cobalt/radar/anatomy/bars.py`

## What it does
`working_bars(i1, minutes, as_of=…) -> WorkingSeries` builds working-timeframe buckets from one ticker's i1 bars and flags whether each bucket is whole (Astra R1-8). `archiver.aggregate` stays the one aggregation path. This module wraps it because it emits a first-minute-only bucket as a closed bar and accepts a missing minute silently.

## Rules
- Only i1 bars that closed by `as_of` (`ts + 1 min <= as_of`) are read, so a replay never reads the future.
- A bucket not closed by `as_of` is excluded and named in `unclosed_bucket`.
- A closed bucket missing a minute is emitted with `complete=False`, `minutes_present` and `missing_minutes`.
- `require_complete(bars)` raises `IncompleteBucket` on any partial bucket. Detectors call it rather than guess.
- `rth_only(series, clock)` keeps buckets that open and close inside RTH.

## Gotchas
In `system.bars`, a minute with no print and a minute never fetched look identical, so the flag covers both. Mixed tickers and non-i1 input are refused. `as_of` must be tz-aware. Bucket starts use a UTC minute floor, which matches the aggregate's ET floor because ET offsets are whole hours.
