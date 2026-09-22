# `cobalt.radar.formation.triggers` — TRIGGERS

Added 2026-09-21 in STEP-2 of the setups one build (FINAL §2.2).

`TRIGGERS: dict[TriggerType, TriggerResolver]`. Each resolver has two methods:

- `serves(params)` says whether it understands the parameter shape.
- `resolve(frame, trigger_def, value)` returns a `TriggerOutcome`. The outcome carries `state` (`armed | fired | unavailable`), `price`, `ref_bar_ts`, `kind`, `inputs`, a `why` fragment, and the bar-break `level` when there is one.

A resolver works in the FRAME's coordinates, for the def's long-side text. On the mirrored frame, "long" is the short side. The stage calls `outcome.unmirrored(side)` before the price reaches `Formation`: prices are negated, and the level's `trade_direction` becomes `short`. `trigger_resolver(trigger_def)` returns the resolver, or None, which the registry names as `trigger:<type>`.

Registered so far: `bar_break {bars_cleared}`, which is `structure.bar_break_trigger` re-registered. Its output is byte-identical to before (Lego (ii) pins in `tests/cobalt/test_setups_registries.py`).

**2026-09-22 — `range_break` (setups one build STEP-4; FINAL §2.2).** `RangeBreak` serves `{ref: Range(micro).bound | Range(micro).top}`. Taxonomy §3.0: `bound` is the trade-side bound, long → `top`. Any other ref is not served, and the registry names it missing. The resolver reads the frame's `Range(micro)` object and fires intrabar at its `top`, in frame coordinates. On the mirrored frame that is the real base, so the short side's trigger comes out right after `unmirrored`.

`Formation.trigger` stays a `TriggerLevel`, so the card, audit and replay readers are unchanged. The level carries the top's touch bars with `bars_cleared = 0`: this trigger is a level, not a count of bars cleared. The kind and inputs ride on `trigger_outcome`. No instantiated Range raises `InsufficientBars`, which the stage reports as `not_formed`.
