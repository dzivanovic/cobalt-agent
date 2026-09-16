"""Dots and the card score — the ONE ranking authority that reaches a
radar card (S2-P2 STEP-5; rulings R6, R7; plan §L52-b).

    card_score = round(conviction × proximity × 100)

Pure functions over Pydantic values: no database, no clock, no config
read. The S5 evaluate stage and the tap routes hand in the dots, the
prices and the trader's settings; everything stored comes back out.

THE DOTS. One per `quality_factors[]` entry, in order (`position`):

* COMPUTED — `source: cobalt | cobalt-degraded` and `tier: deterministic`.
  The evaluator supplies a `FactorObservation` (value, inputs, formula);
  the grade is the value through `card.curves[factor]` (piecewise-linear,
  clipped to 1–10, rounded half-up ONCE). Role **shadow** (R6): stored,
  shown hollow, tappable, never in conviction until a curve tribunal and
  an L7 run promote it. No anchors → `curve_unset`; no computer for the
  factor → `MANUAL` (today: `trail_fit`, R5); a stale input →
  `input_stale`, and the prior grade moves into `history` labelled.
* DESK — `catalyst`, `market_alignment`, `sector_alignment`. Shadow, and
  N/A through S2: `catalyst` → `DESK_NA` (the desk supplies it in S3);
  both alignments → `DEFAULT_UNRULED` (plan §8 ESCALATE 4: the default
  with/flat/against map is not authorized by a dated ruling, and the STEP-0
  context-ticker feed is stale, so no map is revived here).
* HUMAN — everything else. Hollow until tapped. Never a neutral 5.

CONVICTION = mean of the TAPPED trader grades ÷ 10 — shadow grades do not
count, and an empty tap set is null, never zero.

SUPPRESSION (the settled rule): a required computed dot that is N/A and
untapped suppresses `card_score`, with the reason. Tapping it lifts it.

PROXIMITY = clamp(1 − |last − trigger| ÷ (3 × |trigger − stop|), 0, 1).
The caller passes the card's LIVE sizing inputs (`entry`, `stop`): a
stop he moved changes the risk the proximity is measured in. The
formation evidence (`trigger_price`, `structural_stop`) stays immutable
on the row for replay (Astra R1-7).

ROUNDING, once and on stored values: conviction and proximity are
quantized to 6 dp half-up (the NUMERIC(8,6) columns), and `card_score` is
computed FROM those stored values, so a recompute from the row is exact.

PROPOSED KEY (R7): the highest `card.proposed_key` band the conviction
meets, snapped down to an enabled key through `aset.engine.snap_down` —
the same function the key tap sizes through, so the highlight can never
propose a key the tap would refuse. No conviction → none ("tap to
propose").
"""

from __future__ import annotations

from datetime import datetime
from decimal import ROUND_HALF_UP, Decimal, localcontext
from typing import Any, Iterable, Literal, Mapping

from pydantic import BaseModel, ConfigDict, Field

from cobalt.aset.engine import snap_down
from cobalt.aset.models import Grade
from cobalt.settings.card import Curve, ProposedKeyBands
from cobalt.taxonomy.trade_def import QualityFactor

#: The three desk-graded dots (09-14 group-2 ruling).
DESK_FACTORS: frozenset[str] = frozenset({"catalyst", "market_alignment", "sector_alignment"})
DESK_NA_REASON = {"catalyst": "DESK_NA", "market_alignment": "DEFAULT_UNRULED", "sector_alignment": "DEFAULT_UNRULED"}

COMPUTED_SOURCES = frozenset({"cobalt", "cobalt-degraded"})
SIX_DP = Decimal("0.000001")
ONE = Decimal(1)
TEN = Decimal(10)

NaReason = Literal["curve_unset", "MANUAL", "input_stale", "input_unavailable", "DESK_NA", "DEFAULT_UNRULED"]


class FactorObservation(BaseModel):
    """What the evaluator measured for one computed factor, with the inputs
    that make it replayable (L57)."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    value: Decimal | None
    stale: bool = False
    inputs: dict[str, Any] = Field(default_factory=dict)
    formula: str = ""
    #: Why `value` is None when it is (the detector's reason code).
    unavailable: str | None = None


class Dot(BaseModel):
    """One `"user".card_dots` row, in memory."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    factor: str = Field(min_length=1)
    position: int = Field(ge=0)
    source: Literal["cobalt", "cobalt-degraded", "human"]
    tier: Literal["deterministic", "judgment"]
    role: Literal["shadow", "live", "human"]
    engine_value: Decimal | None = None
    engine_grade: int | None = Field(default=None, ge=1, le=10)
    engine_why: str | None = None
    engine_inputs: dict[str, Any] | None = None
    engine_formula: str | None = None
    na_reason: NaReason | None = None
    history: list[dict[str, Any]] = Field(default_factory=list)
    trader_grade: int | None = Field(default=None, ge=1, le=10)
    tapped_at: datetime | None = None

    @property
    def computed(self) -> bool:
        return self.source in COMPUTED_SOURCES and self.tier == "deterministic" and self.factor not in DESK_FACTORS


def _half_up(value: Decimal, exp: Decimal = ONE) -> Decimal:
    return value.quantize(exp, rounding=ROUND_HALF_UP)


def grade_from_curve(value: Decimal, curve: Curve) -> tuple[Decimal, int]:
    """(unrounded, grade). Piecewise-linear between anchors, flat beyond
    the ends, clipped to 1–10, rounded half-up once."""
    anchors = curve.anchors
    with localcontext() as ctx:
        ctx.prec = 28
        if value <= anchors[0].x:
            raw = anchors[0].grade
        elif value >= anchors[-1].x:
            raw = anchors[-1].grade
        else:
            raw = anchors[-1].grade
            for lo, hi in zip(anchors, anchors[1:]):
                if lo.x <= value <= hi.x:
                    raw = lo.grade + (value - lo.x) * (hi.grade - lo.grade) / (hi.x - lo.x)
                    break
        raw = min(max(raw, ONE), TEN)
    return raw, int(_half_up(raw))


def _why(factor: QualityFactor, value: Decimal, grade: int) -> str:
    if factor.why_template:
        return factor.why_template.format(value=value, grade=grade)
    return f"{factor.name} {value} → {grade}"


def compute_dots(
    factors: Iterable[QualityFactor],
    observations: Mapping[str, FactorObservation],
    curves: Mapping[str, Curve] | None,
    *,
    at: datetime,
) -> list[Dot]:
    """Fresh dots for one scan. No taps, no history — `refresh_dots`
    carries those across from the stored row."""
    out: list[Dot] = []
    for position, factor in enumerate(factors):
        base = dict(factor=factor.name, position=position, tier=factor.tier)
        if factor.name in DESK_FACTORS:
            reason = DESK_NA_REASON[factor.name]
            out.append(Dot(
                **base, source="cobalt-degraded", role="shadow",
                na_reason=reason, engine_why=f"desk shadow: n/a ({reason})",
            ))
            continue
        if factor.source not in COMPUTED_SOURCES or factor.tier != "deterministic":
            out.append(Dot(**base, source="human", role="human"))
            continue
        obs = observations.get(factor.name)
        common = dict(**base, source=factor.source, role="shadow")
        if obs is None:
            out.append(Dot(**common, na_reason="MANUAL", engine_why=f"{factor.name}: no Cobalt computer — MANUAL"))
            continue
        inputs = dict(obs.inputs)
        if obs.stale:
            out.append(Dot(
                **common, engine_value=obs.value, engine_inputs=inputs, engine_formula=obs.formula,
                na_reason="input_stale", engine_why=f"{factor.name}: input stale — grade suppressed",
            ))
            continue
        if obs.value is None:
            out.append(Dot(
                **common, engine_inputs=inputs, engine_formula=obs.formula, na_reason="input_unavailable",
                engine_why=f"{factor.name}: unavailable ({obs.unavailable or 'no value'})",
            ))
            continue
        curve = (curves or {}).get(factor.name)
        if curve is None:
            out.append(Dot(
                **common, engine_value=obs.value, engine_inputs=inputs, engine_formula=obs.formula,
                na_reason="curve_unset", engine_why=f"{factor.name} {obs.value} — card.curves anchors unset",
            ))
            continue
        unrounded, grade = grade_from_curve(obs.value, curve)
        inputs["curve"] = curve.pairs()
        inputs["unrounded_grade"] = str(unrounded)
        out.append(Dot(
            **common, engine_value=obs.value, engine_grade=grade, engine_why=_why(factor, obs.value, grade),
            engine_inputs=inputs, engine_formula=obs.formula,
        ))
    return out


def refresh_dots(
    previous: Iterable[Dot], fresh: Iterable[Dot], *, at: datetime, added_by: Mapping[str, Any] | None = None
) -> list[Dot]:
    """The stored dots updated by this scan's fresh dots.

    Taps (`trader_grade`, `tapped_at`) and `history` carry over. When a
    fresh dot is stale and the stored one had an engine grade, that grade
    moves into history labelled `input_stale` (09-14 group-2 B) — the
    card shows the suppression, not the old number. A factor absent from
    a non-empty previous set (a def that gained a factor — taxonomy v0.8's
    `catalyst`, Astra R2-4) is added untapped, with a `factor_added`
    history record naming `added_by` (the definition md5 and run)."""
    previous = list(previous)
    prior = {d.factor: d for d in previous}
    out: list[Dot] = []
    for dot in fresh:
        old = prior.get(dot.factor)
        if old is None:
            if previous:
                dot = dot.model_copy(update={"history": [
                    *dot.history, {"label": "factor_added", "at": at.isoformat(), **dict(added_by or {})},
                ]})
            out.append(dot)
            continue
        history = list(old.history)
        if dot.na_reason == "input_stale" and old.engine_grade is not None:
            history.append({
                "label": "input_stale", "at": at.isoformat(),
                "engine_value": str(old.engine_value) if old.engine_value is not None else None,
                "engine_grade": old.engine_grade,
            })
        out.append(dot.model_copy(update={
            "history": history, "trader_grade": old.trader_grade, "tapped_at": old.tapped_at,
        }))
    return out


def conviction(dots: Iterable[Dot]) -> Decimal | None:
    grades = [d.trader_grade for d in dots if d.trader_grade is not None]
    if not grades:
        return None
    with localcontext() as ctx:
        ctx.prec = 28
        return _half_up(Decimal(sum(grades)) / len(grades) / TEN, SIX_DP).normalize()


def suppression(dots: Iterable[Dot]) -> str | None:
    blocked = [f"{d.factor}: {d.na_reason}" for d in dots if d.computed and d.na_reason and d.trader_grade is None]
    if not blocked:
        return None
    return "required computed dot N/A and untapped — " + "; ".join(blocked) + " (tap to grade)"


def proximity(*, last: Decimal, trigger: Decimal, stop: Decimal) -> Decimal:
    risk = abs(trigger - stop)
    if risk == 0:
        raise ValueError(f"proximity undefined: trigger {trigger} equals stop {stop}")
    with localcontext() as ctx:
        ctx.prec = 28
        raw = ONE - abs(last - trigger) / (3 * risk)
    return _half_up(min(max(raw, Decimal(0)), ONE), SIX_DP).normalize()


def card_score(conv: Decimal | None, prox: Decimal | None, suppressed: str | None) -> int | None:
    if conv is None or prox is None or suppressed:
        return None
    return int(_half_up(conv * prox * 100))


_BAND_KEYS = ((Grade.A_PLUS, "a_plus_min"), (Grade.A, "a_min"), (Grade.B, "b_min"), (Grade.C, "c_min"))


def proposed_key(
    conv: Decimal | None, bands: ProposedKeyBands | None, enabled: Iterable[Grade]
) -> tuple[Grade | None, str | None]:
    if conv is None:
        return None, "no conviction — tap to propose"
    if bands is None:
        return None, "card.proposed_key bands unset"
    met = next((grade for grade, field in _BAND_KEYS if conv >= getattr(bands, field)), None)
    if met is None:
        return None, "below every band"
    key, notice = snap_down(met, enabled)
    if key is None:
        return None, notice
    return key, None


def dot_colour(grade: int | None, *, red_max: int, amber_max: int) -> int | None:
    """0 red / 1 amber / 2 green, from `card.dot.red_max` / `amber_max`."""
    if grade is None:
        return None
    if grade <= red_max:
        return 0
    return 1 if grade <= amber_max else 2


def colour_thresholds(tunables: Mapping[str, Any]) -> tuple[int, int]:
    try:
        red, amber = int(tunables["card.dot.red_max"].value), int(tunables["card.dot.amber_max"].value)
    except (KeyError, TypeError, ValueError) as e:
        raise ValueError(f"card.dot.red_max / card.dot.amber_max tunables missing or invalid: {e}") from e
    if not 1 <= red < amber < 10:
        raise ValueError(f"card.dot colour thresholds must satisfy 1 <= red_max < amber_max < 10, got {red}, {amber}")
    return red, amber


class CardScore(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    conviction: Decimal | None
    proximity: Decimal
    card_score: int | None
    score_suppressed: str | None
    proposed_key: Grade | None
    proposed_key_reason: str | None


def score_card(
    dots: Iterable[Dot],
    *,
    last: Decimal,
    trigger: Decimal,
    stop: Decimal,
    bands: ProposedKeyBands | None,
    enabled: Iterable[Grade],
) -> CardScore:
    dots = list(dots)
    conv = conviction(dots)
    prox = proximity(last=last, trigger=trigger, stop=stop)
    suppressed = suppression(dots)
    key, reason = proposed_key(conv, bands, list(enabled))
    return CardScore(
        conviction=conv, proximity=prox, card_score=card_score(conv, prox, suppressed),
        score_suppressed=suppressed, proposed_key=key, proposed_key_reason=reason,
    )


__all__ = [
    "COMPUTED_SOURCES", "CardScore", "DESK_FACTORS", "Dot", "FactorObservation",
    "card_score", "colour_thresholds", "compute_dots", "conviction", "dot_colour",
    "grade_from_curve", "proposed_key", "proximity", "refresh_dots", "score_card", "suppression",
]
