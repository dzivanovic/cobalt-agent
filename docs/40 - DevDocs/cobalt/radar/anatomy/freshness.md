# `src/cobalt/radar/anatomy/freshness.py`

## What it does
Two pieces of Astra R1-12. It makes vendor RVOL a replayable observation, and it defines staleness by dependency type instead of one wall-clock rule.

## Key functions/classes
- `rvol_observations(source_sets, observed_at=) -> dict[ticker, RvolObservation]` gives one timestamped observation per ticker from the scan's own `SourceSet`s. Precedence (`PRECEDENCE`, stated on every observation): screen before list, then lower note order, then lexically lower source id. `candidates` lists every carrier, winner first. Only healthy, active sources count. A carried ticker with no RVOL keeps `value=None`; it is never dropped and never zero.
- `intraday_staleness(observed_at=, as_of=, scan_interval=)` applies rule `intraday_2x_scan_interval`: stale when age > 2 × scan_interval (equal is fresh). An observation after `as_of` raises.
- `daily_staleness(series, trade_date=, is_trading_day=)` applies rule `daily_last_completed_session`: fresh only when the series holds the last trading day before the trade date (`previous_trading_day`, holiday-aware through the session calendar). Today's partial row does not count.
- `policy_staleness(version_sha256=)` applies rule `versioned_never_wall_clock`. Policy, tunable and settings inputs are replaced by a new version, never aged out.

## Gotchas
Persisting the observations into `"user".radar_score_receipt` and marking an evaluation `input_stale` are STEP-4 work (chunk B). This module only decides.
