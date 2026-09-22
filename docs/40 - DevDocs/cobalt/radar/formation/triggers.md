# `cobalt.radar.formation.triggers` — TRIGGERS

Added 2026-09-21 in STEP-2 of the setups one build (FINAL §2.2).

`TRIGGERS: dict[TriggerType, TriggerResolver]`. Each resolver has two methods:

- `serves(params)` says whether it understands the parameter shape.
- `resolve(frame, trigger_def, value)` returns a `TriggerOutcome`. The outcome carries `state` (`armed | fired | unavailable`), `price`, `ref_bar_ts`, `kind`, `inputs`, a `why` fragment, and the bar-break `level` when there is one.

A resolver works in the FRAME's coordinates, for the def's long-side text. On the mirrored frame, "long" is the short side. The stage calls `outcome.unmirrored(side)` before the price reaches `Formation`: prices are negated, and the level's `trade_direction` becomes `short`. `trigger_resolver(trigger_def)` returns the resolver, or None, which the registry names as `trigger:<type>`.

Registered so far: `bar_break {bars_cleared}`, which is `structure.bar_break_trigger` re-registered. Its output is byte-identical to before (Lego (ii) pins in `tests/cobalt/test_setups_registries.py`).
