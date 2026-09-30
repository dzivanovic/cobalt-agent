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
- `refresh_dots(previous, fresh, *, at, added_by=None)` carries taps and history across. A factor missing from a non-empty previous set (a def that gained one — taxonomy v0.8's `catalyst`, Astra R2-4) is added untapped with a `{"label": "factor_added", "at", **added_by}` history record; the stage passes the definition md5 and run id. When a fresh dot is stale and the stored one had a grade, that grade moves into history as `{"label": "input_stale", "at", "engine_value", "engine_grade"}`.
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

## 2026-09-21 — setups one build STEP-1: `ASSUMED`
`NaReason` gains `"ASSUMED"`. `ASSUMED_FORMATION = "assumed_formation"` is the one constant that names the dot marking a formation resting on an assumed default (R2-2 = B). `radar/evaluate.py` and `cards/store.py` both import it from here, because `cards/` never imports from `radar/`. The dot is computed (`cobalt-degraded`, `deterministic`) and is never tapped, since the store refuses the tap. So `suppression()` names it on every path that recomputes, and `card_score` stays null for the card's life. The logic of `suppression()` is unchanged. Only its reason text changes: it drops ` (tap to grade)` when every blocker is `ASSUMED`, because an assumed default is ruled on the settings surface, not tapped. `conviction`, `card_score` and `score_card` are unchanged.

## 2026-09-24 — stale score S1: no fresh `last`, no proximity (STALE-SCORE v2 §2 C; `[F-06]` `[F-13]` `[F-14]` `[F-16]`)
The rule is: if there is no fresh `last`, there is no proximity, and so no score. Three new names implement it.

- `score_last(ev)` is the ONLY `last` rule for every caller of `score_card`. There are four callers: `refresh_card`, `replay_receipt`, the stage's create call, and `audit_export`'s replay scorer. It returns `None` if and only if `ev.intraday_stale` is set. It returns `ev.last_price` otherwise. A fresh evaluation that has no last price raises `EvaluateError`. It never substitutes a price: the old `card.entry` and `trigger` fallbacks are deleted, not replaced. `EvaluateError` lives in `radar/evaluate.py`, so the import is lazy, inside the function. That is the same shape as `cards/store.py`'s lazy import of `OpenRadarCard`, and it avoids a cycle, because `evaluate` imports this module.
- `stale_reason(ev)` returns the bars-stale sentence. It is a pure function of the evaluation, so the stage and the replay write the same bytes (X27):
  - `"bars stale — no closed bar"` when no bar has closed;
  - otherwise `"bars stale — last close HH:MM:SS ET, older than 2 × radar.scan_interval"`, with the close taken as `last_bar_ts + 1 minute` in New York time.

  It returns `None` for an evaluation that is not intraday-stale.
- `score_card(…, last, stale_reason=None)`:
  - A `None` last must carry its reason, and a price must carry none. Any other combination is a `ValueError`.
  - With `None`, proximity is `None`, and `card_score` is `None` through the existing `card_score()` guard.
  - `score_suppressed` is the sentence, followed by `; <suppression(dots)>` when a dot also suppresses.
- `CardScore.proximity` is now `Decimal | None`.
- `PROXIMITY_UNKNOWN = "bars stale — no proximity"` is defined once here. It is what the tap route writes when proximity is NULL and no sentence is stored (S2, `[F-06]`).

Conviction, the proposed key, the dots and `suppression()` are computed exactly as before.

## 2026-09-30 — f15-p1
`grade_why(output)` (F15 FINAL §3 `why`): the ONE deterministic sentence a prediction record carries, built from the record's `output` fields only — `card_score N` (or `no card_score`), `suppressed: …`, `conviction`, `proximity`, `key K` (or `no key (reason)`), `tapped f g, …`, `engine f g, …`, joined by ` · `. No clock, no other source, never an LLM. No number changes; the file's bytes change, so `formula_sha256` does (FINAL §8 NOTE).
