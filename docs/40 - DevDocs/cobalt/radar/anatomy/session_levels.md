# `cobalt.radar.anatomy.session_levels` — DayRange, VWAP, PMH/PML, PDH/PDL

Added 2026-09-21 in STEP-3 of the setups one build (FINAL §3 D1).

Pure detectors: bars go in, a typed observation comes out. Prices stay in the coordinates of the bars they receive, so the Frame's mirrored bars give the short side's levels without separate code ([F-04]).

- **`day_range(run)`** (convention `dayrange.session`, `A-06`) returns the RTH run's high and low, from 09:30 to the last closed working bar, with the premarket excluded. `upper_third = low + 2/3 · (high − low)`. An empty run returns `None`; the frame serves that as `insufficient_bars`. On the mirrored frame the same formula gives the real bottom third's ceiling, which is the short side's "upper third".
- **`vwap(rth_i1)`** (convention `vwap.anchor`, `A-12`) is anchored at 09:30: Σ(typical · volume) / Σ volume over the closed RTH one-minute bars, where typical = (high + low + close) / 3, computed in Decimal at 28 digits. No bars or zero volume gives `insufficient_bars`; it never divides by zero.
- **`premarket_levels(premarket_i1)`** returns the premarket high and low. With no premarket print it returns `None`, which the frame serves as `null` (`not_instantiated`).
- **`prior_day_levels(daily, trade_date)`** returns the prior session's high and low through `daily.prior_session`, the one existing path. It raises `NoDailyBars` when no earlier bar exists. The frame also serves `no_daily_bars` when the daily series is stale.

`TUNABLE_KEYS = ()`. The two conventions are `label` rows in `tunables.yaml`, both null for now, and the atoms that implement them declare them (`formation/atoms.py`). A null convention row counts as assumed in a formation's closure.
