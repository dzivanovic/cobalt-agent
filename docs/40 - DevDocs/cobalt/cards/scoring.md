# `src/cobalt/cards/scoring.py`

## What it does
Dots and the card score, the ONE ranking authority that reaches a radar card (S2-P2 STEP-5; R6, R7; plan §L52-b):

    card_score = round(conviction × proximity × 100)

Pure functions over Pydantic values: no database, clock or config read.

## Key functions/classes
- `Dot` is one `"user".card_dots` row in memory: factor, position, source, tier, role, engine value/grade/why/inputs/formula, `na_reason`, history, trader grade, `tapped_at`. `Dot.computed` means `source: cobalt*` and `tier: deterministic`, and not a desk factor.
- `FactorObservation` is what the evaluator measured for a computed factor: value, stale flag, inputs, formula, unavailable reason.
- `compute_dots(factors, observations, curves, *, at)` returns one dot per `quality_factors[]` entry, in order:
  - **Computed** dots are role `shadow` (R6) and graded through `card.curves[factor]`. When they carry no grade, the `na_reason` is one of:
    - `curve_unset`: no anchors (the value is still stored);
    - `MANUAL`: no computer for the factor (`trail_fit`);
    - `input_stale`;
    - `input_unavailable`.
  - **Desk** dots (`catalyst`, `market_alignment`, `sector_alignment`) are shadow, `cobalt-degraded`, and N/A through S2: `DESK_NA` for catalyst, `DEFAULT_UNRULED` for both alignments (plan §8 ESCALATE 4). They are mirrored as `desk shadow: n/a (…)`.
  - **Human** dots are hollow until tapped. There is never a neutral 5.
- `grade_from_curve(value, curve)` is piecewise-linear, flat beyond the end anchors, clipped to 1–10 and rounded half-up ONCE. It returns `(unrounded, grade)`; the curve and the unrounded grade are stored in `engine_inputs`.
- `refresh_dots(previous, fresh, *, at)` carries taps and history across. When a fresh dot is stale and the stored one had a grade, that grade moves into history as `{"label": "input_stale", "at", "engine_value", "engine_grade"}`.
- `conviction(dots)` is the mean of TAPPED trader grades ÷ 10, quantized to 6 dp. An empty tap set is `None`, never 0.
- `suppression(dots)` is the settled rule: a computed dot that is N/A and untapped suppresses the score, with the reason.
- `proximity(*, last, trigger, stop)` is `clamp(1 − |last − trigger| ÷ (3 × |trigger − stop|), 0, 1)`, quantized to 6 dp.
- `card_score(conviction, proximity, suppressed)` is computed from the stored 6-dp values and rounded half-up.
- `proposed_key(conviction, bands, enabled)` takes the highest `card.proposed_key` band met and snaps it down through `aset.engine.snap_down`, the same function the key tap sizes through. With no conviction it returns "tap to propose".
- `dot_colour(grade, red_max, amber_max)` and `colour_thresholds(tunables)` implement `card.dot.red_max` 3 / `card.dot.amber_max` 6.
- `score_card(dots, *, last, trigger, stop, bands, enabled)` returns `CardScore`.

## Config it reads
None directly. Callers pass `card.curves`, `card.proposed_key` (trader settings, `settings.card`), the enabled grades of today's rung, and the `card.dot.*` tunables.

## Gotchas
Shadow grades rank nothing: they are stored and shown, never counted in conviction, until a curve tribunal and an L7 run promote them. `curve_unset` also suppresses the score until the dot is tapped, which is why a dark or pre-D2 card has `card_score = NULL`.
