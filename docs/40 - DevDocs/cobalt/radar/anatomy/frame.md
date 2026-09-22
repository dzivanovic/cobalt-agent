# `cobalt.radar.anatomy.frame` — the Frame (side binding by mirroring)

Added 2026-09-21 in STEP-2 of the setups one build (FINAL §2.1 [F-04], [R2F-12], §3).

Every def is evaluated twice per scan, once per side, on a `Frame` built once per (member, scan, side):

- **Long** is the stored working bars.
- **Short** is the same detectors run on mirrored bars. `mirror_bars` maps price to −price and swaps high and low; volume and time are unchanged. `mirror_daily` does the same to the daily series ([R2F-12]), so the HTF range break of a mirrored run is the real opposite break with the same day count.

`build_frame(side, run, daily=, daily_ok=, trade_date=, params=, last_close=)` takes the REAL series and mirrors them for `short`. It runs the detectors (`detect_extension`, `htf_range_break`) and fills `atoms` (moved here from `evaluate.py`). The stage asks the frame for atoms and never runs a detector itself. `Frame.real(price)` converts a frame price back to real-world coordinates.

The acceptance property is F-04's, proved over every scan of the committed day in `tests/cobalt/test_setups_registries.py`:

- for price outputs, `negate_prices(eval_as_long(mirror(bars))) == eval_as_short(bars)`;
- for predicates, `pred_as_long(mirror(bars)) == pred_as_short(bars)`.

The mirror wraps `WorkingBar` / `DailyBar` only. It never round-trips through the archiver's `Bar` (X6: a negative-price `Bar` constructs, so nothing would stop such a round trip).

## 2026-09-21 — the warm series and the D1 atoms (setups one build STEP-3; FINAL §3 D1, §5)

The frame now holds two series:

- **run** is unchanged: the RTH working bars. Every session-anchored object uses it.
- **warm** is `premarket` + `run`. `premarket` holds the complete working buckets that open and close in the premarket (`premarket_buckets`); absent and incomplete buckets are dropped. The warm series only seeds `EMA9`, `EMA21` and `ATR(working_tf)`, through `indicators.seeded`.

`SessionInputs` carries the other real-coordinate inputs:

- the seed buckets;
- the closed i1 bars as one-minute working bars, split into premarket and RTH (`minute_bars`, over the one aggregation path);
- the member's pool admission.

The short frame mirrors all of it, the same way it mirrors the run and the daily series.

`atoms` is a `LazyAtoms` mapping. The Extension and HTF atoms are computed eagerly, as before. Each D1 atom is computed on first read and kept for the scan: `price`, the EMAs, `ATR(working_tf)`, `EMA9.slope`, `slope_norm(EMA9|VWAP)`, `VWAP`, `DayRange.*`, `PMH/PML`, `PDH/PDL` and `InPlay.state`. So a def reads a tunable only when it names the atom behind it; a Rubberband def reads none of the new keys (X22). An EMA atom's period is its own name (`EMA_PERIODS`): `ma.slow` is 20 while the atom says 21, so the atom does not take the period from config.

Two reads are sampled differently:

- `VWAP` now is taken over every closed RTH i1 bar;
- the series behind `slope_norm(VWAP)` is sampled at working-bar ends.

`Frame.number(name)` returns a number atom's value or `None`. The F-04 property for the new atoms is proved on the committed day (`tests/cobalt/test_setups_d1.py`):

- a mirrored price, negated back, is the real price;
- a mirrored slope is the negated real slope;
- the ATR is equal on both sides;
- the short frame's `DayRange.high` / `PMH` / `PDH` read the real low-side levels.

## 2026-09-22 — Range(micro) and the opening drive (setups one build STEP-4; FINAL §3 D2/D3)

The same lazy closure now serves the D2 / D3 atoms:

- `Range(micro).{instantiated, duration, low, top, base, bound, height, wick_ratio}` come from `micro_range.detect_micro_range`, fed the frame's seeded ATR. `low` is `base` and `bound` is `top`: the long-side text's trade-side bound.
- `Leg(opening_drive).direction` comes from `leg.legs`; `Leg(opening_drive).terminated_by` from `leg_roles.opening_drive`, under `A-07`.

How missing inputs read:

- a null detector key reads `<key>_unset`, a missing seed `insufficient_seed`, an incomplete last bucket `incomplete_bucket`;
- no Range reads `instantiated = False`, with the numbers `null`;
- a drive that has not ended reads `terminated_by = null`.

`Frame.objects` is a second lazy map: `Range(micro)` → the observation (or its `_unset` reason), and `Leg(opening_drive)` → the `OpeningDrive`. The `range_break` trigger, the `consolidation_low` stop and the `Range(micro)` anchor read it, so each computes nothing a scan has not already computed. A def that names none of these atoms still reads none of their keys (X22).

## 2026-09-22 — the lifecycle and the series (setups one build STEP-5; FINAL §3 D4)

`Extension.state` is now served lazily whenever the Extension is available:

- today's `culminating | none` while `A-08` is null;
- otherwise `extension_lifecycle`'s state, fed the seeded EMA9 at every run bar.

`Frame.objects` gains the pieces the new resolvers read:

- `series(<EMA9|EMA21|VWAP>)`: the indicator at every run bar;
- `turn_index`: the tracked extreme's bar;
- `cross_index(a, b, direction)`: the latest bar where `a` crossed `b`;
- the seeded `atr`;
- the scan's `tunables`.

The `indicator_cross` trigger, the `recent_higher_low` / `measured_fraction` stops and the `between` relation all read these, so each is computed once per scan.

**2026-09-22 — roles and the catalyst resolver (STEP-6).** New lazy atoms:

- `Leg(pullback).{direction, end, index}`, `Leg(impulse).direction` and `Leg(opening_drive OR impulse).direction`, over `leg_roles.pullback_roles`;
- `catalyst_ref`: `A-13`, `True` for an admitted member, `null` for a departed one.

New objects: `pullback_roles` and `pre_test_bars`. The `touched` and `on` relations, the `Leg(pullback)` anchor and the `indicator_rejection` / `indicator` bricks read them.

**2026-09-22 — `Level_ref(resistance).rejected` (STEP-7).** It is served lazily over the frame's own `PMH` / `PDH`: the level set `A-17`, resistance for the long-side text. On the mirrored frame these are the real PML / PDL. A level reads `rejected` when some RTH bar's high reached it and closed back below it, and the last close is still below it (`A-18`). A missing premarket print skips PMH; missing daily bars leave the answer unknown (`no_daily_bars`) unless PMH already decided it.

**2026-09-22 — the RangeBreak (STEP-8).** The object `range_break` is `range_break.choose` over the frame's PMH / PDH, with the seeded ATR. It serves these atoms:

- `RangeBreak(level).state`, with the alias `RangeBreak.state`;
- `event(retest)`;
- `event(stop_hit)` (`A-22`): the sequence's stop, the turn candle's low less the buffer, touched by a LATER bar's low. It is computed from bars, never from the card ledger.

The `sequence` trigger, the `turn_candle` stop, the `RangeBreak(level)` anchor, and the `after` / `inside` relations read the same object.

**2026-09-22 (fix round 3, F1 — R47, Grok's fix for X10).** `binds_side_by_frame(td)` is True when a precondition compares the unqualified `Extension.state` to a state past the culmination (`PAST_CULMINATION` = the atom's domain minus `culminating` / `none`). For such a def `build_frame(..., bind_side=True)` builds `Frame.extension` with `detect_extension(..., direction=BOUND_EXTENSION_DIRECTION)` — the down Extension the long-side text opposes (A-01), in BOTH frames — so every reader of `frame.extension` (the atoms, the D4 lifecycle, the turn, the anchor, the stops) binds to it, and the mirrored frame gives the short side. A day that recovers past the session open no longer flips it. `Frame.observed` is always the detector's own Extension (the run's sign); the stage publishes the factor / seam observations from it. Every other def (Rubberband included) is unchanged: there `extension` and `observed` are the same object.
