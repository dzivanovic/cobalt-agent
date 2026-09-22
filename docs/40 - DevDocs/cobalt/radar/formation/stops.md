# `cobalt.radar.formation.stops` — STOPS and STRUCTURAL_REFS

Added 2026-09-21 in STEP-2 of the setups one build (FINAL §2.3).

The two tables:

- `STOPS: dict[placement type, StopResolver]`. Each resolver has `serves(placement)` and `resolve(frame, placement, value) -> StopOutcome`.
- `STRUCTURAL_REFS: dict[StructuralRef, resolver]`. Each maps a §3.6 reference to the extreme it names.

A `StopOutcome` carries `price`, `placement`, `ref`, `inputs`, a `why` fragment, the buffered and nudged `structural` stop (`structure.structural_stop`, unchanged), and the protected `extreme`. It is resolved in frame coordinates. `unmirrored(side)` negates every price field and flips the extreme's `high` / `low` for a short. X4 checked this over the cent grid and found no case where the nudge law breaks under negation.

The geometry guard (FINAL §9 point (5)) is not here. It is written once in the stage (`evaluate.stop_on_protective_side`), so every placement registered here inherits it.

Registered so far: `structural_extreme` on `snapback_candle` and `turn_low`, the run's tracked extreme. Both are re-registered with byte-identical output.

**2026-09-22 — `consolidation_low` / `range_base` (setups one build STEP-4; FINAL §2.3).** Both taxonomy aliases of `Range.base` now resolve through `STRUCTURAL_REFS` to the live micro-Range's base, as a `TrackedExtreme` (side `low`, at its latest holding bar). The buffer and the nudge law stay `structure.structural_stop`, and the geometry guard is still the stage's one check. With no instantiated Range the resolver raises `InsufficientBars`, which becomes `not_formed`.

**2026-09-22 — `recent_higher_low`, `measured_fraction` (STEP-5; FINAL §2.3).**

- `recent_higher_low` resolves to the latest pivot low (`cfg(pivot.n)`, `anatomy.pivots`) inside the live micro-Range: the micro-Range's counter-pivot on the trade-opposite side. It uses `structural_extreme`'s buffer and nudge.
- `MeasuredFraction` serves `{anchor_a, anchor_b, fraction}` when both anchors are `entry` or a `STRUCTURAL_REFS` ref. `entry` is the trigger's price: the stage now hands `trigger=` to every stop resolver. The stop is `measured_fraction_price(a, b, f) = a − f × (a − b)`, floored to the cent. No buffer and no ten-cent nudge: the nudge moves a stop toward a structure, and a measured stop has none. The outcome's `ref` is `anchor_b`, which the stage now takes as `Formation.stop_ref` (for a structural placement that is the same value as before).

**2026-09-22 — `indicator` (STEP-6; taxonomy A.2).** `IndicatorStop` serves `{indicator ∈ EMA9|EMA21|VWAP, snapshot: at_entry}`; the ruled default, `live`, is not served. The stop is the indicator's value at the entry bar (the trigger's `ref_bar_ts`), under `structural_stop`'s buffer, rounding and nudge. The indicator is the structure.
