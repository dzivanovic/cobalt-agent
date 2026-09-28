# `cobalt.radar.anatomy.range_break` — the RangeBreak lifecycle, retest and sequence

Added 2026-09-22 in STEP-8 of the setups one build (FINAL §3 D6; taxonomy §3.4 :104, §10.2).

The lifecycle is `forming → break_attempt → accepted | failed_trap`, promoted by `close_through`. The construction is pure and runs in frame coordinates: the long-side text breaks UP through a level L.

- **Eligible levels.** A level can break only inside the session: the run's first bar must open at or under it.
- **The states.**
  - `forming`: no bar traded above L.
  - `break_attempt`: a bar traded above L, but none closed above it.
  - `accepted`: a bar CLOSED above L.
  - `failed_trap`: a close back under L within `cfg(range_break.failed_trap_bars)` bars of the accepting close (`A-19`, a global hole).
- **The events.**
  - `event(retest)`: the first bar after the accepting close whose low comes back within `cfg(range_break.retest_tolerance_atr)` × ATR (`A-20`) and closes above L.
  - The turn: the first bar after the retest that closes above the prior bar's high. It is the `sequence` trigger bar, and its low is the `turn_candle` ref (`A-23`).
- **`prior_low`** is the floor of `Range(prior)` (`A-21`): the lowest low before the break.
- **`choose(run, levels)`** picks the level broken latest, or the nearest level above when none is broken. The frame hands it the level set `A-17` (PMH, PDH).

`range_break_params` returns `<key>_unset` for a null row.
