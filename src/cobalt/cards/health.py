"""Health pills for a FILLED radar card (S2-P2 STEP-7).

The threshold table is P3's 2026-09-14 R2, COPIED, not re-ruled, and it
lives in `tunables.yaml` as eight `card.health.*` rows (engine tunables,
L53 — never trader settings):

    class          warn                         bad
    participation  RVOL ratio vs entry < 0.70   < 0.45
    cost           spread vs entry >= 1.5×      >= 2.5×
    dot            graded dot down >= 2         graded dot <= 3
    structural     stop / EMA9 touched          lost on a closed working-TF bar

THE ENTRY SNAPSHOT (Astra R1-12). "vs entry" needs an entry: the S5 stage
captures an `EntrySnapshot` (RVOL, spread, computed dot grades) on the
first scan that sees the card FILLED and stores it in the card's `health`
JSONB, where every later scan compares against it. `captured_at` says
when — the scan after the fill, not the fill tick, and the pill says so.

NO FABRICATED RATIO. A missing or zero baseline, a missing current value
or no spread source at all renders the pill `n/a` with a loud note —
never a ratio computed from a stand-in. Cobalt has no spread source in
S2, so `cost` is `n/a` on every card until one exists; `alignment` is
`n/a` until the alignment default is ruled (plan §8 ESCALATE 4).

JUDGMENT DOTS ARE NEVER HEALTH-SCORED (L11): only computed dots
(`source: cobalt*`, `tier: deterministic`) enter the dot class.

Pure functions; the stage hands in the bars, the snapshot and the dots.
"""

from __future__ import annotations

from datetime import datetime
from decimal import Decimal, localcontext
from typing import Any, Literal, Mapping, Sequence

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

from .scoring import ASSUMED_FORMATION, Dot

HEALTH_KEYS = (
    "card.health.participation_warn", "card.health.participation_bad",
    "card.health.cost_warn", "card.health.cost_bad",
    "card.health.dot_warn_drop", "card.health.dot_bad_max",
    "card.health.structural_warn", "card.health.structural_bad",
)

Status = Literal["ok", "warn", "bad", "n/a"]


class HealthThresholds(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    participation_warn: Decimal
    participation_bad: Decimal
    cost_warn: Decimal
    cost_bad: Decimal
    dot_warn_drop: int = Field(gt=0)
    dot_bad_max: int = Field(ge=1, le=10)
    structural_warn: Literal["touched"]
    structural_bad: Literal["lost_on_close"]

    @classmethod
    def from_tunables(cls, rows: Mapping[str, Any]) -> HealthThresholds:
        missing = [key for key in HEALTH_KEYS if key not in rows or rows[key].value is None]
        if missing:
            raise ValueError(f"health tunables missing or unmeasured: {missing}")
        values = {key.rsplit(".", 1)[1]: rows[key].value for key in HEALTH_KEYS}
        for key in ("participation_warn", "participation_bad", "cost_warn", "cost_bad"):
            values[key] = Decimal(str(values[key]))
        return cls(**values)


class EntrySnapshot(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    captured_at: AwareDatetime
    rvol: Decimal | None
    spread: Decimal | None
    dot_grades: dict[str, int]


class HealthPill(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    klass: Literal["participation", "cost", "dot", "structural"]
    label: str
    status: Status
    note: str
    inputs: dict[str, Any] = Field(default_factory=dict)


def _ratio(current: Decimal, entry: Decimal) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = 28
        return current / entry


def participation_pill(*, entry_rvol: Decimal | None, current_rvol: Decimal | None, t: HealthThresholds) -> HealthPill:
    if entry_rvol is None or entry_rvol == 0 or current_rvol is None:
        return HealthPill(
            klass="participation", label="participation", status="n/a",
            note="N/A — no entry RVOL baseline or no current RVOL; no ratio fabricated",
            inputs={"entry_rvol": _s(entry_rvol), "current_rvol": _s(current_rvol), "ratio": None},
        )
    ratio = _ratio(current_rvol, entry_rvol)
    status: Status = "bad" if ratio < t.participation_bad else "warn" if ratio < t.participation_warn else "ok"
    return HealthPill(
        klass="participation", label="participation", status=status,
        note=f"RVOL {current_rvol} vs {entry_rvol} at entry ({ratio.normalize()}×)",
        inputs={"entry_rvol": str(entry_rvol), "current_rvol": str(current_rvol), "ratio": str(ratio.normalize())},
    )


def cost_pill(*, entry_spread: Decimal | None, current_spread: Decimal | None, t: HealthThresholds) -> HealthPill:
    if entry_spread is None or current_spread is None or entry_spread == 0:
        return HealthPill(
            klass="cost", label="cost", status="n/a",
            note="N/A — no spread source (or no entry spread); no ratio fabricated",
            inputs={"entry_spread": _s(entry_spread), "current_spread": _s(current_spread), "ratio": None},
        )
    ratio = _ratio(current_spread, entry_spread)
    status: Status = "bad" if ratio >= t.cost_bad else "warn" if ratio >= t.cost_warn else "ok"
    return HealthPill(
        klass="cost", label="cost", status=status,
        note=f"spread {current_spread} vs {entry_spread} at entry ({ratio.normalize()}×)",
        inputs={"entry_spread": str(entry_spread), "current_spread": str(current_spread), "ratio": str(ratio.normalize())},
    )


def dot_pills(*, entry_grades: Mapping[str, int], dots: Sequence[Dot], t: HealthThresholds) -> list[HealthPill]:
    pills: list[HealthPill] = []
    for dot in dots:
        if not dot.computed:
            continue  # L11: judgment and desk dots are never health-scored
        if dot.factor == ASSUMED_FORMATION:
            continue  # R50 (fix r3 F4): no graded value; the card's ASSUMED mark carries it
        entry = entry_grades.get(dot.factor)
        current = dot.engine_grade
        if entry is None or current is None:
            pills.append(HealthPill(
                klass="dot", label=dot.factor, status="n/a",
                note=f"N/A — {dot.factor} has no graded value {'at entry' if entry is None else 'now'}",
                inputs={"entry_grade": entry, "current_grade": current},
            ))
            continue
        drop = entry - current
        status: Status = "bad" if current <= t.dot_bad_max else "warn" if drop >= t.dot_warn_drop else "ok"
        pills.append(HealthPill(
            klass="dot", label=dot.factor, status=status,
            note=f"{dot.factor} {current} (was {entry} at entry)",
            inputs={"entry_grade": entry, "current_grade": current, "drop": drop},
        ))
    return pills


def structural_pill(
    label: str,
    *,
    level: Decimal | None,
    direction: Literal["long", "short"],
    intrabar: Sequence[Any],
    closed: Sequence[Any],
    t: HealthThresholds,
) -> HealthPill:
    """`intrabar`: bars whose extremes can TOUCH the level (i1 or working);
    `closed`: closed working-TF bars whose CLOSE can lose it."""
    if level is None:
        return HealthPill(klass="structural", label=label, status="n/a",
                          note=f"N/A — no {label} level available", inputs={"level": None})
    if direction == "long":
        lost = [b.ts for b in closed if b.close < level]
        touched = [b.ts for b in intrabar if b.low <= level]
    else:
        lost = [b.ts for b in closed if b.close > level]
        touched = [b.ts for b in intrabar if b.high >= level]
    if lost:
        status: Status = "bad"
        note = f"{label} {level} {t.structural_bad} at {lost[0].isoformat()}"
    elif touched:
        status = "warn"
        note = f"{label} {level} {t.structural_warn} at {touched[0].isoformat()}"
    else:
        status, note = "ok", f"{label} {level} held"
    return HealthPill(
        klass="structural", label=label, status=status, note=note,
        inputs={"level": str(level), "direction": direction,
                "first_lost": lost[0].isoformat() if lost else None,
                "first_touched": touched[0].isoformat() if touched else None},
    )


def card_health(
    *,
    snapshot: EntrySnapshot,
    current_rvol: Decimal | None,
    current_spread: Decimal | None,
    dots: Sequence[Dot],
    stop: Decimal,
    direction: Literal["long", "short"],
    intrabar: Sequence[Any],
    closed: Sequence[Any],
    ema9: Decimal | None,
    t: HealthThresholds,
) -> list[HealthPill]:
    return [
        participation_pill(entry_rvol=snapshot.rvol, current_rvol=current_rvol, t=t),
        cost_pill(entry_spread=snapshot.spread, current_spread=current_spread, t=t),
        *dot_pills(entry_grades=snapshot.dot_grades, dots=dots, t=t),
        structural_pill("stop", level=stop, direction=direction, intrabar=intrabar, closed=closed, t=t),
        structural_pill("EMA9", level=ema9, direction=direction, intrabar=intrabar[-1:], closed=closed[-1:], t=t),
        HealthPill(klass="structural", label="alignment", status="n/a",
                   note="N/A — alignment default unruled (DEFAULT_UNRULED)", inputs={}),
    ]


def _s(value: Decimal | None) -> str | None:
    return None if value is None else str(value)


__all__ = [
    "EntrySnapshot", "HEALTH_KEYS", "HealthPill", "HealthThresholds", "card_health",
    "cost_pill", "dot_pills", "participation_pill", "structural_pill",
]
