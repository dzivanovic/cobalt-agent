# `cobalt.radar.formation.triggers` — TRIGGERS

Added 2026-09-21 in STEP-2 of the setups one build (FINAL §2.2).

`TRIGGERS: dict[TriggerType, TriggerResolver]`. Each resolver has two methods:

- `serves(params)` says whether it understands the parameter shape.
- `resolve(frame, trigger_def, value)` returns a `TriggerOutcome`. The outcome carries `state` (`armed | fired | unavailable`), `price`, `ref_bar_ts`, `kind`, `inputs`, a `why` fragment, and the bar-break `level` when there is one.

A resolver works in the FRAME's coordinates, for the def's long-side text. On the mirrored frame, "long" is the short side. The stage calls `outcome.unmirrored(side)` before the price reaches `Formation`: prices are negated, and the level's `trade_direction` becomes `short`. `trigger_resolver(trigger_def)` returns the resolver, or None, which the registry names as `trigger:<type>`.

Registered so far: `bar_break {bars_cleared}`, which is `structure.bar_break_trigger` re-registered. Its output is byte-identical to before (Lego (ii) pins in `tests/cobalt/test_setups_registries.py`).

**2026-09-22 — `range_break` (setups one build STEP-4; FINAL §2.2).** `RangeBreak` serves `{ref: Range(micro).bound | Range(micro).top}`. Taxonomy §3.0: `bound` is the trade-side bound, long → `top`. Any other ref is not served, and the registry names it missing. The resolver reads the frame's `Range(micro)` object and fires intrabar at its `top`, in frame coordinates. On the mirrored frame that is the real base, so the short side's trigger comes out right after `unmirrored`.

`Formation.trigger` stays a `TriggerLevel`, so the card, audit and replay readers are unchanged. The level carries the top's touch bars with `bars_cleared = 0`: this trigger is a level, not a count of bars cleared. The kind and inputs ride on `trigger_outcome`. No instantiated Range raises `InsufficientBars`, which the stage reports as `not_formed`.

**2026-09-22 — `indicator_cross` (STEP-5; FINAL §2.2).** `IndicatorCross` serves `{a, b, direction}` with `a ≠ b` in `{EMA9, EMA21, VWAP}` and direction `a_crosses_above_b` / `a_crosses_below_b`. It finds the latest closed working bar where the cross happened, in frame coordinates, through the frame's `cross_index`. It stamps `cross_point` (that bar), and its close is the entry the card arms at. No cross yet raises `InsufficientBars`, which becomes `not_formed`.

**2026-09-22 — `indicator_rejection` (STEP-6; taxonomy §10.2 A.4).** `IndicatorRejection` serves `{indicator ∈ EMA9|EMA21|VWAP, contact ⊆ {touch, penetrate}}`. It is `close_through` by definition: the LAST closed working bar whose low reached the indicator (`touch`: ≤; `penetrate`: <) and whose close is above it is both the trigger and the entry, at its close. The last bar is not a rejection → `InsufficientBars`. Next-bar continuation is the human read (L11).

**2026-09-22 — `trendline_break` (STEP-7; FINAL §2.2, taxonomy §3.7).** `TrendlineBreak` serves `{ref: Level_ref(trendline), anchor_leg: Leg(pullback), pivots}`, intrabar, in frame coordinates. It tries two cases in order:

- **The flat case** (taxonomy `:114`): a micro-Range instantiated after the anchor leg began. The trigger is its top, the far bound.
- **Otherwise, the sloped line** through the pivot highs (`cfg(pivot.n)`) from the leg before the pullback to now. It needs at least `pivots` of them, descending. The line runs from the first to the last pivot and is extended to the last bar, rounded to 0.0001.

Neither case → `InsufficientBars`.
