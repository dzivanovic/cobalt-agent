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

STEP-3 (FINAL §5, `A-05`) gives the frame its second series. **run** = the
RTH working bars, exactly as before — every session-anchored object uses it.
**warm** = the complete premarket working buckets (04:00 → 09:30; absent and
incomplete buckets dropped) followed by the run; it is used ONLY to seed
`EMA9`, `EMA21` and `ATR(working_tf)` (`indicators.seeded`). The closed i1
bars, split into premarket and RTH one-minute bars, feed VWAP and PMH/PML.
The D1 atoms are served LAZILY (`LazyAtoms`): a resolver runs, and reads its
tunable, only when a predicate or the stage asks for its atom — so a def's
instrumented reads stay inside its declared closure (X22).
"""

from __future__ import annotations

from collections.abc import Callable, Iterator, Mapping, Sequence
from datetime import date, datetime, timedelta
from decimal import Decimal
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict

from cobalt.session.models import Session
from cobalt.taxonomy.tunables import TunableRow

from ..formation.atoms import AtomValue
from .bars import WorkingBar, working_bars
from .daily import DailySeries, HtfRangeBreak, NoDailyBars, htf_range_break
from .extension import (
    ExtensionObservation,
    ExtensionParams,
    LifecycleObservation,
    detect_extension,
    extension_lifecycle,
    lifecycle_params,
)
from .structure import tracked_extreme
from .in_play import in_play_state
from .indicators import ATR_PERIOD, ema, seeded, wilder_atr
from .leg import legs
from .leg_roles import OpeningDrive, PullbackRoles, max_retrace, opening_drive, pre_test_bars, pullback_roles
from .micro_range import MicroRangeObservation, detect_micro_range, range_params
from .session_levels import day_range, premarket_levels, prior_day_levels, vwap
from .slope import slope, slope_bars, slope_norm

Side = Literal["long", "short"]
#: The EMA atoms the frame serves; the period is the atom's own name.
EMA_PERIODS = {"EMA9": 9, "EMA21": 21}


def _inside(bar: WorkingBar, clock, session: Session) -> bool:
    return clock.session(bar.ts) is session and clock.session(bar.end - timedelta(seconds=1)) is session


def premarket_buckets(bars: Sequence[WorkingBar], clock) -> tuple[WorkingBar, ...]:
    """The seed: complete working buckets that open and close in the premarket."""
    return tuple(b for b in bars if b.complete and _inside(b, clock, Session.PREMARKET))


def minute_bars(closed_i1, *, as_of: datetime, clock) -> tuple[tuple[WorkingBar, ...], tuple[WorkingBar, ...]]:
    """(premarket, RTH) closed i1 bars as one-minute working bars."""
    series = working_bars(closed_i1, 1, as_of=as_of).bars
    return (tuple(b for b in series if _inside(b, clock, Session.PREMARKET)),
            tuple(b for b in series if _inside(b, clock, Session.RTH)))


class SessionInputs(BaseModel):
    """What the D1 detectors read beyond the run, in REAL coordinates."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    premarket: tuple[WorkingBar, ...] = ()
    premarket_i1: tuple[WorkingBar, ...] = ()
    rth_i1: tuple[WorkingBar, ...] = ()
    departed: bool = False


class LazyAtoms(Mapping[str, AtomValue]):
    """Atom values, each computed on first read and kept for the scan."""

    def __init__(self, eager: dict[str, AtomValue], lazy: dict[str, Callable[[], AtomValue]]):
        self._values = dict(eager)
        self._lazy = lazy

    def __getitem__(self, name: str) -> AtomValue:
        if name not in self._values:
            if name not in self._lazy:
                raise KeyError(name)
            self._values[name] = self._lazy[name]()
        return self._values[name]

    def __contains__(self, name: object) -> bool:
        return name in self._values or name in self._lazy

    def __iter__(self) -> Iterator[str]:
        return iter(dict.fromkeys([*self._values, *self._lazy]))

    def __len__(self) -> int:
        return len(set(self._values) | set(self._lazy))


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
    #: The complete premarket working buckets (the seed), frame coordinates.
    premarket: tuple[WorkingBar, ...] = ()
    extension: ExtensionObservation
    htf: HtfRangeBreak | None
    #: A `LazyAtoms` (typed `Any` so validation never copies — and so never
    #: computes — the lazy values).
    atoms: Any
    #: The lazy observations a trigger / stop resolver reads by object name
    #: (`Range(micro)` → `MicroRangeObservation` or its `_unset` reason).
    objects: Any = None
    #: The last closed i1 close, in the frame's coordinates.
    last_close: Decimal | None

    @property
    def warm(self) -> tuple[WorkingBar, ...]:
        """FINAL §5: working bars 04:00 → now, complete premarket buckets only."""
        return (*self.premarket, *self.run)

    def real(self, price: Decimal) -> Decimal:
        """A frame price in real-world coordinates."""
        return price if self.side == "long" else -price

    def number(self, name: str) -> Decimal | None:
        atom = self.atoms[name]
        return atom.number if atom.kind == "number" else None


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


def _num(value: Decimal | None, reason: str) -> AtomValue:
    return AtomValue(kind="number", number=value) if value is not None else AtomValue(kind="unavailable", reason=reason)


def _d1_resolvers(
    run: tuple[WorkingBar, ...],
    session: SessionInputs,
    *,
    daily: DailySeries | None,
    daily_ok: bool,
    trade_date: date,
    last_close: Decimal | None,
    tunables: Mapping[str, TunableRow],
    objects: dict[str, Callable[[], Any]],
    ext: ExtensionObservation,
) -> dict[str, Callable[[], AtomValue]]:
    """The lazy atoms of one frame (every input already in frame coordinates);
    `objects` receives the observations a trigger / stop resolver reads."""
    pre = session.premarket
    cache: dict[str, Any] = {}

    def once(key: str, compute: Callable[[], Any]) -> Any:
        if key not in cache:
            cache[key] = compute()
        return cache[key]

    def atr() -> Decimal | None:
        return once("atr", lambda: seeded(wilder_atr, pre, run, ATR_PERIOD).value)

    def ema_back(period: int, back: int) -> list[Decimal | None]:
        """The seeded EMA at the last `back + 1` bars, oldest first, on the ONE
        series `seeded` chooses at the last bar."""
        def compute():
            chosen = seeded(ema, pre, run, period)
            series = [*pre, *run] if chosen.source == "premarket" else list(run)
            out = []
            for k in range(back, -1, -1):
                head = series[:max(len(series) - k, 0)]
                out.append(ema(head, period).value if len(head) >= period else None)
            return out
        return once(f"ema{period}:{back}", compute)

    def vwap_back(back: int) -> list[Decimal | None]:
        def compute():
            out = []
            for k in range(back, -1, -1):
                if len(run) <= k:
                    out.append(None)
                    continue
                end = run[-1 - k].end
                out.append(vwap([b for b in session.rth_i1 if b.end <= end]).value)
            return out
        return once(f"vwap:{back}", compute)

    def ema_atom(period: int) -> Callable[[], AtomValue]:
        return lambda: _num(ema_back(period, 0)[-1], "insufficient_seed")

    def slope_atom(of: str, normalised: bool) -> Callable[[], AtomValue]:
        def resolve() -> AtomValue:
            n = slope_bars(tunables)
            if n is None:
                return AtomValue(kind="unavailable", reason="slope_norm.bars_unset")
            if of == "VWAP":
                values = vwap_back(n)
            else:
                values = ema_back(EMA_PERIODS[of], n)
                if values[-1] is None:
                    return AtomValue(kind="unavailable", reason="insufficient_seed")
            if any(v is None for v in values):
                return AtomValue(kind="unavailable", reason="insufficient_bars")
            if not normalised:
                return _num(slope(values, n).value, "insufficient_bars")
            if atr() is None:
                return AtomValue(kind="unavailable", reason="insufficient_seed")
            return _num(slope_norm(values, n, atr=atr()).value, "insufficient_bars")
        return resolve

    def day(part: str) -> Callable[[], AtomValue]:
        def resolve() -> AtomValue:
            dr = once("dayrange", lambda: day_range(run))
            return _num(getattr(dr, part) if dr else None, "insufficient_bars")
        return resolve

    def premarket(part: str) -> Callable[[], AtomValue]:
        def resolve() -> AtomValue:
            levels = once("pm", lambda: premarket_levels(session.premarket_i1))
            if levels is None:
                return AtomValue(kind="null", reason="not_instantiated")
            return AtomValue(kind="number", number=getattr(levels, part))
        return resolve

    def prior(part: str) -> Callable[[], AtomValue]:
        def resolve() -> AtomValue:
            if not daily_ok or daily is None:
                return AtomValue(kind="unavailable", reason="no_daily_bars")
            try:
                levels = once("pd", lambda: prior_day_levels(daily, trade_date))
            except NoDailyBars:
                return AtomValue(kind="unavailable", reason="no_daily_bars")
            return AtomValue(kind="number", number=getattr(levels, part))
        return resolve

    # --- D2 / D3 (STEP-4): Range(micro) and the opening drive's role ----------
    def micro() -> MicroRangeObservation:
        def compute():
            params, unset = range_params(tunables)
            if unset is not None:
                return unset
            return detect_micro_range(run, params, atr=atr())
        return once("range", compute)

    def range_atom(part: str) -> Callable[[], AtomValue]:
        def resolve() -> AtomValue:
            obs = micro()
            if isinstance(obs, str):
                return AtomValue(kind="unavailable", reason=obs)
            if obs.unavailable is not None:
                return AtomValue(kind="unavailable", reason=obs.unavailable)
            r = obs.range
            if part == "instantiated":
                return AtomValue(kind="boolean", boolean=r is not None)
            if r is None:
                return AtomValue(kind="null", reason="not_instantiated")
            value = {"duration": r.duration_min, "low": r.base, "top": r.top, "base": r.base,
                     "bound": r.top, "height": r.height, "wick_ratio": r.wick_ratio}[part]
            return _num(value, "insufficient_bars")
        return resolve

    def drive_legs():
        return once("legs", lambda: legs(run))

    def drive_direction() -> AtomValue:
        lg = drive_legs()
        if not run:
            return AtomValue(kind="unavailable", reason="insufficient_bars")
        if not lg:
            return AtomValue(kind="null", reason="not_instantiated")
        return AtomValue(kind="symbol", symbol=lg[0].direction)

    def drive() -> OpeningDrive | str:
        def compute():
            if not run:
                return "insufficient_bars"
            bound = max_retrace(tunables)
            if bound is None:
                return "leg.consolidation_max_retrace_unset"
            obs = micro()
            if isinstance(obs, str):
                return obs
            if obs.unavailable is not None:
                return obs.unavailable
            return opening_drive(run, drive_legs(), obs.range, max_retrace=bound)
        return once("drive", compute)

    def terminated_by() -> AtomValue:
        od = drive()
        if isinstance(od, str):
            return AtomValue(kind="unavailable", reason=od)
        if od.terminated_by is None:
            return AtomValue(kind="null", reason="not_instantiated")
        return AtomValue(kind="symbol", symbol=od.terminated_by)

    # --- D4 (STEP-5): the Extension lifecycle, indicator series, turn, cross ---
    def series(name: str) -> list[Decimal | None]:
        """`name` at every run bar, oldest first (EMA seeded; VWAP at bar ends)."""
        if not run:
            return []
        if name in EMA_PERIODS:
            return ema_back(EMA_PERIODS[name], len(run) - 1)
        if name == "VWAP":
            return vwap_back(len(run) - 1)
        raise KeyError(f"no series for {name!r}")

    def lifecycle() -> LifecycleObservation | None:
        """None while `A-08` is null: `Extension.state` then reads today's value."""
        def compute():
            params, unset = lifecycle_params(tunables)
            if unset is not None:
                return None
            return extension_lifecycle(run, ext, params, ema9=series("EMA9"), slope_bars=slope_bars(tunables))
        return once("lifecycle", compute)

    def extension_state() -> AtomValue:
        life = lifecycle()
        if life is None or ext.state != "culminating":
            return AtomValue(kind="symbol", symbol=ext.state)
        if life.state is None:
            return AtomValue(kind="unavailable", reason=life.unavailable)
        return AtomValue(kind="symbol", symbol=life.state)

    def turn_index() -> int | None:
        if not run or ext.direction is None:
            return None
        turn = tracked_extreme(run, ext.direction)
        return max(i for i, b in enumerate(run) if b.ts == turn.bar_ts)

    def cross_index(a: str, b: str, direction: str) -> int | None:
        """The latest run bar where `a` crossed `b` in `direction` (frame coordinates)."""
        sa, sb = series(a), series(b)
        for i in range(len(run) - 1, 0, -1):
            if None in (sa[i], sb[i], sa[i - 1], sb[i - 1]):
                continue
            if direction == "a_crosses_above_b" and sa[i - 1] <= sb[i - 1] and sa[i] > sb[i]:
                return i
            if direction == "a_crosses_below_b" and sa[i - 1] >= sb[i - 1] and sa[i] < sb[i]:
                return i
        return None

    # --- STEP-6: pullback / impulse roles, pre_test, the catalyst resolver ------
    def roles() -> PullbackRoles:
        return once("pullback_roles", lambda: pullback_roles(drive_legs()))

    def role_atom(which: str, part: str) -> Callable[[], AtomValue]:
        def resolve() -> AtomValue:
            if not run:
                return AtomValue(kind="unavailable", reason="insufficient_bars")
            r = roles()
            if which == "pullback":
                leg = r.pullback
            elif which == "impulse":
                leg = r.before if r.before_role == "impulse" else None
            else:  # "opening_drive OR impulse": the leg before the pullback, of either role
                leg = r.before
            if leg is None:
                return AtomValue(kind="null", reason="not_instantiated")
            if part == "direction":
                return AtomValue(kind="symbol", symbol=leg.direction)
            if part == "end":
                return AtomValue(kind="number", number=leg.low if leg.direction == "down" else leg.high)
            return AtomValue(kind="number", number=Decimal(r.index))
        return resolve

    def catalyst_ref() -> AtomValue:
        """`A-13` (FINAL §6): the def's "or setup" branch read as met by the
        name's radar in-play admission; a departed member has none."""
        if session.departed:
            return AtomValue(kind="null", reason="not_instantiated")
        return AtomValue(kind="boolean", boolean=True)

    objects.update({
        "Range(micro)": micro, "Leg(opening_drive)": drive,
        "series": lambda: series, "turn_index": turn_index, "cross_index": lambda: cross_index,
        "atr": atr, "tunables": lambda: tunables,
        "pullback_roles": roles, "pre_test_bars": lambda: pre_test_bars(run, roles()),
    })
    extension_lazy = {} if ext.unavailable is not None else {"Extension.state": extension_state}
    extension_lazy.update({
        "Leg(pullback).direction": role_atom("pullback", "direction"),
        "Leg(pullback).end": role_atom("pullback", "end"),
        "Leg(pullback).index": role_atom("pullback", "index"),
        "Leg(impulse).direction": role_atom("impulse", "direction"),
        "Leg(opening_drive OR impulse).direction": role_atom("either", "direction"),
        "catalyst_ref": catalyst_ref,
    })

    return {
        **extension_lazy,
        **{f"Range(micro).{part}": range_atom(part)
           for part in ("instantiated", "duration", "low", "top", "base", "bound", "height", "wick_ratio")},
        "Leg(opening_drive).direction": drive_direction,
        "Leg(opening_drive).terminated_by": terminated_by,
        "price": lambda: _num(last_close, "insufficient_bars"),
        **{name: ema_atom(period) for name, period in EMA_PERIODS.items()},
        "ATR(working_tf)": lambda: _num(atr(), "insufficient_seed"),
        "EMA9.slope": slope_atom("EMA9", normalised=False),
        "slope_norm(EMA9)": slope_atom("EMA9", normalised=True),
        "slope_norm(VWAP)": slope_atom("VWAP", normalised=True),
        # VWAP now: every closed RTH i1 bar; its slope samples working-bar ends.
        "VWAP": lambda: _num(once("vwap", lambda: vwap(session.rth_i1).value), "insufficient_bars"),
        "DayRange.high": day("high"), "DayRange.low": day("low"), "DayRange.upper_third": day("upper_third"),
        "PMH": premarket("high"), "PML": premarket("low"),
        "PDH": prior("high"), "PDL": prior("low"),
        "InPlay.state": lambda: AtomValue(kind="symbol", symbol=in_play_state(departed=session.departed)),
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
    session: SessionInputs | None = None,
    tunables: Mapping[str, TunableRow] | None = None,
) -> Frame:
    """One frame. `run`, `session`, `daily` and `last_close` are REAL; the
    short frame mirrors them here."""
    session = session or SessionInputs()
    if side == "short":
        run = mirror_bars(run)
        daily = mirror_daily(daily) if daily is not None else None
        last_close = -last_close if last_close is not None else None
        session = session.model_copy(update={
            "premarket": mirror_bars(session.premarket), "premarket_i1": mirror_bars(session.premarket_i1),
            "rth_i1": mirror_bars(session.rth_i1),
        })
    run = tuple(run)
    ext = detect_extension(run, params)
    atoms = _extension_atoms(ext)
    if ext.unavailable is None:
        del atoms["Extension.state"]  # served lazily: the D4 lifecycle (STEP-5)
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
    objects: dict[str, Callable[[], Any]] = {}
    lazy = _d1_resolvers(run, session, daily=daily, daily_ok=daily_ok, trade_date=trade_date,
                         last_close=last_close, tunables=tunables if tunables is not None else {}, objects=objects,
                         ext=ext)
    return Frame(side=side, run=run, premarket=session.premarket, extension=ext, htf=htf,
                 atoms=LazyAtoms(atoms, lazy), objects=LazyAtoms({}, objects), last_close=last_close)


__all__ = [
    "EMA_PERIODS", "Frame", "LazyAtoms", "SessionInputs", "Side", "build_frame", "minute_bars", "mirror_bars",
    "mirror_daily", "premarket_buckets",
]
