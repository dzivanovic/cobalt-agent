# `src/cobalt/strike/measure.py`

`cobalt strike measure` — the F9 re-measure, measurement only (the `LIVE-FEED-SPIKE.md` pattern, committed). One `fetch_bars(ticker, Interval.I1, token)` per name per cycle, paced by its own `TokenBucket` at names × 60 / cadence rpm.

- **Lag** (the spike's definition): for each bar start T, the first wall-clock poll whose newest bar has ts = T, minus T; a ticker's first poll is its baseline, not a transition (`lag_rows`).
- **Summary** per window (PREMARKET, RTH): GETs, HTTP status counts, fetch ms and lag n/p50/p95/max (nearest rank). Its last line is the verdict: `CRITERION ≤<c> s HOLDS at <cadence> s` (every GET 200, lag p95 ≤ `strike.alert_criterion_s` in each window run); `THROTTLED at <cadence> s — Charter re-rule: 10 s cadence (~8 s)` on a 403, a 429 or a transport failure; else `NOT MET — <WINDOW> p95 <x> s` (or `… GET failed (…)`, `… p95 none (no bar transitions)`, `no PREMARKET or RTH poll`).
- **Refused before the first GET** (`MeasureRefused`, exit 2): more than `strike.max_armed` names; a cadence below `strike.poll_interval_min`; the radar's planned rpm unreadable (`configured_sources().planned_rpm`); a demand that with the radar's planned rpm puts the peak over `radar.finviz_max_rpm` through `check_scheduled_demand("strike-measure", …)` — the refusal names the minimum cadence, `max(floor, ⌈names × 60 / (ceiling − planned)⌉)`.
- **Stops** at the first non-200 or fetch error (summary written, exit 1), at the GET cap names × ⌈minutes × 60 / cadence⌉, or at `--minutes`. Outside PREMARKET and RTH it waits and makes no GET.
- Writes only `<out>/strike-measure-<ET date>.jsonl` (one row per GET) and `.md`. Opens no database connection, writes no vault file, touches no trading platform.

## 2026-10-09 — s4-p1-1009
New module (S4-P1 M1).
