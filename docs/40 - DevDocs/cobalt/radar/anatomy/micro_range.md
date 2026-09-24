# `cobalt.radar.anatomy.micro_range` — Range(micro)

Added 2026-09-22 in STEP-4 of the setups one build (FINAL §3 D2; taxonomy §2.3, §3.0).

This is the intraday consolidation: "a Range instance at micro scale — instantiation 2 touches per side (`cfg(range.micro.touches_per_side)`). No bar count". Diverging bounds are no Range. The construction is fixed in the module docstring so a recompute cannot drift:

- **Windows.** A candidate window ends at the last closed working bar. It never spans an incomplete bucket; an incomplete LAST bar gives `incomplete_bucket`.
- **Bounds.** `top` / `base` are the window's highest high and lowest low.
- **Touches.** A bar touches a bound within `tol = range.micro.touch_tolerance_atr × ATR` (`A-03`). One touch is one maximal run of consecutive touching bars.
- **`bound_type`.** It comes from the per-bar slope between each bound's first and last touch, against `range.micro.bound_flat_slope_atr × ATR` (`A-04`): `flat`, `converging` or `channel`. A `diverging` window is discarded.
- **The Range** is the LONGEST such window with at least `touches_per_side` touches on each bound.
- **Fields.**
  - `instantiated_ts`: the bar at which both bounds first reached the count; it is the formation's bar.
  - `duration_min`: window start to the end of the last bar.
  - `height = top − base`.
  - `wick_ratio = Σ(range − body) / Σ range`; a zero sum gives `None`.
  - `base_bar_ts`: the latest bar holding the base; it is the stop's structure.

**Inputs.**

- The ATR is the frame's seeded `ATR(working_tf)`. `None` gives `insufficient_seed`.
- `range_params(rows)` returns the params, or the first null key as `<key>_unset`. An absent row raises `KeyError`, which is loud.

**Bounds are near-flat by construction.** A window's bounds are its own extremes and touches must lie within the tolerance of them, so the touch lines are close to flat. This detector can reach `channel` only within that tolerance. A steep channel is not detected as a Range, a limit stated here rather than hidden.

**The mirror.** The detector is pure and knows no side. The frame hands the short side mirrored bars, so the short side's `top` is the real base.

**X13, before wiring.** At 09:40 / 09:50 / 10:00, the median ratio of the seeded ATR to the RTH-weighted true-range mean was 0.53 / 0.69 / 0.79. By 10:00, 190 name-sessions had an `open_drive` micro-Range under the seeded ATR and 231 under the RTH-weighted one. That fires the FINAL's fail line; it is an ESCALATE in the build report, and no key changed.
