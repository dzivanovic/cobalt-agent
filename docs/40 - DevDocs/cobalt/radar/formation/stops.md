# `cobalt.radar.formation.stops` — STOPS and STRUCTURAL_REFS

Added 2026-09-21 in STEP-2 of the setups one build (FINAL §2.3).

The two tables:

- `STOPS: dict[placement type, StopResolver]`. Each resolver has `serves(placement)` and `resolve(frame, placement, value) -> StopOutcome`.
- `STRUCTURAL_REFS: dict[StructuralRef, resolver]`. Each maps a §3.6 reference to the extreme it names.

A `StopOutcome` carries `price`, `placement`, `ref`, `inputs`, a `why` fragment, the buffered and nudged `structural` stop (`structure.structural_stop`, unchanged), and the protected `extreme`. It is resolved in frame coordinates. `unmirrored(side)` negates every price field and flips the extreme's `high` / `low` for a short. X4 checked this over the cent grid and found no case where the nudge law breaks under negation.

The geometry guard (FINAL §9 point (5)) is not here. It is written once in the stage (`evaluate.stop_on_protective_side`), so every placement registered here inherits it.

Registered so far: `structural_extreme` on `snapback_candle` and `turn_low`, the run's tracked extreme. Both are re-registered with byte-identical output.
