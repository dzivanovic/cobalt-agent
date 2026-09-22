"""The Frame — side binding by mirroring (FINAL §2.1 [F-04], [R2F-12], §3
"The Frame"; setups one build STEP-2).

Every def is evaluated twice, once per side, on a Frame built once per
(member, scan, side). LONG = the stored bars. SHORT = the SAME detectors on
MIRRORED bars: price -> -price, high <-> low; volume and time unchanged. The
daily series is mirrored with the intraday bars ([R2F-12]), so the HTF range
break of a mirrored run reads the real opposite break. `trade_direction` in
a frame means that frame's side; a price read off the mirrored frame is
negated before it reaches `Formation` or `RadarCardSpec` (the stage does it,
`TriggerOutcome.unmirrored` / `StopOutcome.unmirrored`).

The acceptance property is F-04's, as `tests/cobalt/test_setups_registries.py`
proves it: `negate_prices(eval_as_long(mirror(bars))) == eval_as_short(bars)`
for price outputs, `pred_as_long(mirror(bars)) == pred_as_short(bars)` for
predicates — never `detector(mirror(bars)) == mirror(detector(bars))`.

The mirror wraps `WorkingBar` / `DailyBar` only and never round-trips through
the archiver's `Bar` (X6). `evaluate_member` asks the frame for atoms; it
never runs a detector itself.
"""

from __future__ import annotations

from collections.abc import Sequence
from datetime import date
from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, ConfigDict

from ..formation.atoms import AtomValue
from .bars import WorkingBar
from .daily import DailySeries, HtfRangeBreak, htf_range_break
from .extension import ExtensionObservation, ExtensionParams, detect_extension

Side = Literal["long", "short"]


def mirror_bars(bars: Sequence[WorkingBar]) -> tuple[WorkingBar, ...]:
    return tuple(
        b.model_copy(update={"open": -b.open, "high": -b.low, "low": -b.high, "close": -b.close}) for b in bars
    )


def mirror_daily(series: DailySeries) -> DailySeries:
    return series.model_copy(update={"bars": tuple(
        b.model_copy(update={"open": -b.open, "high": -b.low, "low": -b.high, "close": -b.close})
        for b in series.bars
    )})


class Frame(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, arbitrary_types_allowed=True)

    side: Side
    run: tuple[WorkingBar, ...]
    extension: ExtensionObservation
    htf: HtfRangeBreak | None
    atoms: dict[str, AtomValue]
    #: The last closed i1 close, in the frame's coordinates.
    last_close: Decimal | None

    def real(self, price: Decimal) -> Decimal:
        """A frame price in real-world coordinates."""
        return price if self.side == "long" else -price


def _extension_atoms(ext: ExtensionObservation) -> dict[str, AtomValue]:
    if ext.unavailable is not None:
        missing = AtomValue(kind="unavailable", reason=ext.unavailable)
        leg = (
            AtomValue(kind="number", number=Decimal(ext.leg_count))
            if ext.leg_count is not None else missing
        )
        return {"Extension.state": missing, "Extension.instantiated": missing, "Extension.leg_count": leg}
    return {
        "Extension.state": AtomValue(kind="symbol", symbol=ext.state),
        "Extension.instantiated": AtomValue(kind="boolean", boolean=bool(ext.instantiated)),
        "Extension.leg_count": (
            AtomValue(kind="number", number=Decimal(ext.leg_count))
            if ext.leg_count is not None else AtomValue(kind="null", reason="not_instantiated")
        ),
    }


def build_frame(
    side: Side,
    run: Sequence[WorkingBar],
    *,
    daily: DailySeries | None,
    daily_ok: bool,
    trade_date: date,
    params: ExtensionParams,
    last_close: Decimal | None,
) -> Frame:
    """One frame. `run`, `daily` and `last_close` are REAL; the short frame
    mirrors them here."""
    if side == "short":
        run = mirror_bars(run)
        daily = mirror_daily(daily) if daily is not None else None
        last_close = -last_close if last_close is not None else None
    run = tuple(run)
    ext = detect_extension(run, params)
    atoms = _extension_atoms(ext)
    htf = None
    if not daily_ok:
        atoms["RangeBreak(HTF).day_count"] = AtomValue(kind="unavailable", reason="no_daily_bars")
    elif not run:
        atoms["RangeBreak(HTF).day_count"] = AtomValue(kind="unavailable", reason="insufficient_bars")
    else:
        htf = htf_range_break(
            daily, trade_date, session_high=max(b.high for b in run), session_low=min(b.low for b in run),
        )
        atoms["RangeBreak(HTF).day_count"] = (
            AtomValue(kind="number", number=Decimal(htf.day_count))
            if htf.day_count is not None else AtomValue(kind="null", reason="not_instantiated")
        )
    return Frame(side=side, run=run, extension=ext, htf=htf, atoms=atoms, last_close=last_close)


__all__ = ["Frame", "Side", "build_frame", "mirror_bars", "mirror_daily"]
