# `cobalt.radar.anatomy.slope` — slope, slope_norm, flat

Added 2026-09-21 in STEP-3 of the setups one build (FINAL §3 D1: `EMA9.slope`, `slope_norm(x)` `A-11`, `flat(x, window)` `A-09` / `A-10`).

All functions are pure. The input is a series of indicator values, oldest first, one per closed working bar.

- `slope(series, n) = (x_t − x_{t−n}) / n`, in price per working bar. The frame serves it as `EMA9.slope`.
- `slope_norm(series, n, atr) = (x_t − x_{t−n}) / (n · atr)`. The ATR is the frame's `ATR(working_tf)`, i.e. the seeded one ([F-10]). If the ATR is zero or missing, the result is `insufficient_bars`: unknown, never infinite (FINAL §4).
- `n` is the global engine row `slope_norm.bars` (`A-11`), read through `slope_bars(rows)`:
  - a null row returns `None`, which the frame serves as `unavailable: slope_norm.bars_unset`;
  - an absent row is a `KeyError`, i.e. a loud config error.

  The row is a global hole, so the assumed note can fill it (R2-3 B).
- `flat(norm_slopes, threshold)` is True when every normalised slope in the window has `|s| <= threshold`. An empty window returns `None` (unknown). The threshold comes from the `per_indicator` row `flat_threshold.<indicator>` through `flat_threshold(rows, indicator)`. F1 is not widened, so the null holes stay null. The `flat(...)` atom and its window argument are interpreted at STEP-5, together with `between`. This module is the detector that interpretation will call.

`TUNABLE_KEYS = ("slope_norm.bars",)`, and the three slope atoms declare it. A slope flips sign under the mirror, so those atoms carry the `price` flag (negated back before publication, X12).
