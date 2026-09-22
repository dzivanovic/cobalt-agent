"""Scan-job stage S5 — evaluate (S2-P2 STEP-4; rulings R1, R2, R4, R9).

    S1 membership -> S2 pool row -> S3 mirror -> S4 bars -> S5 evaluate

Zero tokens. Every trade_def the trader has loaded is evaluated against
every admitted pool member on stored i1 bars aggregated to the working
timeframe; a formation on an evaluable def lands a WATCH card when
`radar.cards_enabled` is true; every run writes the system-side seam
rows and the user-side receipt, dark or not.

THE PARTS

* `evaluate_member` — PURE. One (member, def) -> `MemberEvaluation`:
  `formed | not_formed | avoided | not_evaluable | input_stale`, the
  closed seam payload (`seam.RadarScoreDetail`), the formation (trigger,
  structural stop, formed bar) and the computed-factor observations.
* `EvaluateStage` — the orchestration: read settings (per cycle), defs
  and tunables; open the run; evaluate; write seam rows; create / refresh
  / expire cards; write the receipt; publish the run.
* `replay_receipt` — PURE. Recomputes every published number from a
  receipt chain alone (L57, Astra R1-10).

THE PREDICATE INTERPRETER. Three-valued over the §10.5 AST: an atom the
detectors could not measure is UNKNOWN, never False. A precondition set
forms only when every expr is True. An unknown precondition is
`not_evaluable` when the reason is the unknown catalyst of an Extension
path-B-only run (R4), `input_stale` when the daily series is missing or
stale, and `not_formed` otherwise (warm-up, an incomplete bucket) with
the reason on the atom. A `RangeBreak(HTF).day_count` on a day that broke
nothing is a definite null (`not_instantiated`): `== 1` is False, not
unknown. AST shapes the S2 detectors do not serve are `not_evaluable`,
named — never a guessed truth value.

DIRECTION (FINAL §1, key `A-01`). Direction comes from the trade's own
anatomy; `valid_setups[].relation` is NEVER read for it — `relation` is
the trade's relation to the SETUP's trend (day / higher-timeframe
context), not to the intraday Extension. A def written long-side trades
AGAINST an unqualified Extension: up-run -> short, down-run -> long. That
orientation is the assumed convention `A-01` (`ASSUMED_CONVENTIONS`), so
every formation carries it in `Formation.assumed_keys` and its card the
untappable `assumed_formation` dot (R2-2 = B). No setup is detected: the
card's `setup_ref` is the token `UNCLASSIFIED_SETUP`.

GEOMETRY GUARD (FINAL §9 point (5), X17 PASS): a resolved stop must be on
the protective side of BOTH the trigger and the last close — long: stop <
min(trigger, last close); short: stop > max(trigger, last close) — else
`not_formed`, note `stop_wrong_side`, never a card.

STALENESS (Astra R1-12, `anatomy.freshness`): intraday bars and RVOL use
2 × `radar.scan_interval`; daily bars the last-completed-session rule;
tunables and settings are versioned by hash, never aged out.

PUBLISH ORDERING ACROSS THE TWO SIDES (Astra R1-14). System rows and user
rows cannot share a transaction (ADR-0008). The run is opened `running`,
seam rows are written, user-side cards and the receipt are written, the
card values are copied back to the seam rows, and ONLY THEN is the run
marked `complete` — `radar_board_v` shows complete runs only, so a crash
anywhere before that leaves no published partial. The next cycle marks
an abandoned `running` run `failed`. A card created before the crash is
not duplicated on retry: open-card uniqueness is the DB's partial unique
index, and the creation path treats a conflict as "already open".

RECEIPT CHAINING. Retaining every consumed datum's VALUE (not a hash) on
every scan is ~a megabyte a scan; so a receipt stores the rows that are
new or changed since the previous receipt of the same (pool, trade date)
chain in this process, `base_receipt_id` names that previous receipt,
and every snapshot that did not change is `{"unchanged_since_receipt":
id, "sha256": …}`. Each member's full consumed set is still verified: the
receipt stores its row count and sha256, and replay refuses a chain whose
rebuilt rows do not hash to it. A process restart starts a new full base.
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Callable, Iterable, Mapping, Sequence
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal, localcontext
from pathlib import Path
from typing import Any, Literal
from zoneinfo import ZoneInfo

from loguru import logger
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

from cobalt.archiver.models import Bar, Interval
from cobalt.aset.models import Grade
from cobalt.cards.expire import radar_deadline, radar_expiry
from cobalt.cards.health import EntrySnapshot, HealthThresholds, card_health
from cobalt.cards.radar import RadarCardSpec
from cobalt.cards.scoring import (
    ASSUMED_FORMATION,
    Dot,
    FactorObservation,
    colour_thresholds,
    compute_dots,
    refresh_dots,
    score_card,
)
from cobalt.settings.card import CardSettings
from cobalt.taxonomy.defaults import TaxonomyDefaults
from cobalt.taxonomy.loader import iter_cfg_tokens, resolve_cfg
from cobalt.taxonomy.predicate import (
    And,
    Arith,
    Between,
    Cfg,
    Compare,
    EventAtom,
    InTest,
    Node,
    Not,
    Null,
    Number,
    Or,
    Qualified,
    Quantity,
    Relation,
    Ref,
    SetLiteral,
    Symbol,
    render,
)
from cobalt.taxonomy.trade_def import TradeDef
from cobalt.taxonomy.tunables import TunableRow, TunableSource

from .anatomy.bars import IncompleteBucket, WorkingBar, rth_only, working_bars
from .anatomy.daily import DailySeries, NoDailyBars, htf_level_proximity
from .anatomy.extension import ExtensionObservation, ExtensionParams
from .anatomy.frame import Frame, SessionInputs, binds_side_by_frame, build_frame, minute_bars, premarket_buckets
from .anatomy.freshness import RvolObservation, daily_staleness, intraday_staleness
from .anatomy.indicators import PRECISION as INDICATOR_PRECISION
from .anatomy.indicators import InsufficientBars, WARMUP_CONVENTION
from .anatomy.leg_roles import PRE_TEST_CONVENTION
from .anatomy.range_break import PRIOR_RANGE_CONVENTION, STOP_HIT_CONVENTION, TURN_CANDLE_CONVENTION
from .anatomy.session_levels import DAYRANGE_CONVENTION, VWAP_CONVENTION
from .anatomy.registry import evaluability
from .anatomy.structure import StructuralStop, TrackedExtreme, TriggerLevel
from .formation.anchors import anchor_for
from .formation.atoms import (
    ATOMS,
    CATALYST_CONVENTION,
    ON_LEG_CONVENTION,
    RELATIONS,
    LEVELS_CONVENTION,
    REJECTED_CONVENTION,
    AtomValue,
    bound_direction,
    dist_operands,
    unit_mismatch,
)
from .formation.stops import StopOutcome, stop_resolver
from .formation.triggers import TriggerOutcome, trigger_resolver, trigger_tunable_keys
from .seam import AtomOutcome, DeskShadow, DeskShadowEntry, RadarScoreDetail, SeamObservation, validate_atom

ET = ZoneInfo("America/New_York")
#: Bumped ONCE for the whole setups one build (R44: nothing deploys between
#: its steps). A receipt of another version is refused by replay (§9 gate 5).
EVALUATOR_VERSION = "s2p2.2"
DESK_FORMULA_VERSION = "s2p2.1"
#: FINAL [F-07]: the card's setup token — NOT a `SetupRef` member, so no
#: definition can list it in `valid_setups`. No setup is detected.
UNCLASSIFIED_SETUP = "unclassified"
TIE_POLICY = (
    "pinned(ARMED,TRIGGERED,FILLED) by pool_position nulls last, score desc nulls last, ticker, card_id; "
    "WATCH by card_score desc nulls last, pool_position nulls last, ticker, card_id; "
    "one promoted WATCH card to #2 or below pinned, never demoted"
)

Evaluation = Literal["formed", "not_formed", "avoided", "not_evaluable", "input_stale"]

_SRC = Path(__file__).resolve().parent
#: The source files whose bytes ARE the formula (`formula_sha256`).
FORMULA_FILES: tuple[Path, ...] = (
    _SRC / "evaluate.py",
    *sorted((_SRC / "anatomy").glob("*.py")),
    *sorted((_SRC / "formation").glob("*.py")),
    _SRC.parent / "cards" / "scoring.py",
    _SRC.parent / "cards" / "health.py",
    _SRC.parent / "cards" / "radar.py",
    _SRC.parent / "cards" / "expire.py",
    _SRC.parent / "aset" / "engine.py",
)


def canonical_sha256(payload: Any) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str).encode()
    ).hexdigest()


def formula_sha256() -> str:
    digest = hashlib.sha256()
    for path in sorted(FORMULA_FILES, key=lambda p: p.relative_to(_SRC.parent).as_posix()):
        digest.update(path.relative_to(_SRC.parent).as_posix().encode())
        digest.update(path.read_bytes())
    return digest.hexdigest()


class EvaluateError(RuntimeError):
    """S5 failed; the runner stamps `failed_stage='evaluate'`."""


# ---------------------------------------------------------------------
# Atoms and the three-valued interpreter
# ---------------------------------------------------------------------


class Unsupported(ValueError):
    """An AST shape no served resolver evaluates. Carries a generic seam atom."""

    def __init__(self, atom: str, detail: str):
        self.atom = atom
        super().__init__(detail)


def _value(node: Node, atoms: Mapping[str, AtomValue], cfg: Callable[[str], Any], consulted: set[str]):
    """-> ("value", python value) | ("null", None) | ("unknown", reason)."""
    if isinstance(node, Number):
        return "value", node.value
    if isinstance(node, Null):
        return "null", None
    if isinstance(node, Symbol):
        bound = bound_direction(node)  # `trade_direction` is the frame's side (FINAL §4)
        return "value", bound if bound is not None else node.name
    if isinstance(node, Ref) and bound_direction(node) is not None:
        return "value", bound_direction(node)  # `opposite(…)` / `against(…)`
    if isinstance(node, Ref) and dist_operands(node) is not None:  # `dist(a, b)` = |a − b| (STEP-7)
        states = [_value(side, atoms, cfg, consulted) for side in dist_operands(node)]
        for state, value in states:
            if state == "unknown":
                return state, value
        if any(state == "null" for state, _ in states):
            return "null", None
        (_, a), (_, b) = states
        if not isinstance(a, Decimal) or not isinstance(b, Decimal):
            raise Unsupported("Unsupported(dist)", f"dist over non-numbers {a!r}, {b!r}")
        return "value", abs(a - b)
    if isinstance(node, Cfg):
        raw = cfg(node.key)
        if raw is None:  # a null row is unknown, named — never compared (STEP-5)
            return "unknown", f"{node.key}_unset"
        return "value", Decimal(str(raw)) if isinstance(raw, (int, float, Decimal)) else raw
    if isinstance(node, Arith) and node.op in ("*", "/"):
        # FINAL §4 row 2: Decimal at the indicator module's precision; a zero
        # divisor is unknown with a reason, never inf.
        states = [_value(side, atoms, cfg, consulted) for side in (node.left, node.right)]
        for state, value in states:
            if state == "unknown":
                return state, value
        if any(state == "null" for state, _ in states):
            return "null", None
        (_, left), (_, right) = states
        if not isinstance(left, Decimal) or not isinstance(right, Decimal):
            raise Unsupported(f"Unsupported({node.kind})", f"arith over non-numbers {left!r} {node.op} {right!r}")
        if node.op == "/" and right == 0:
            return "unknown", "division_by_zero"
        with localcontext() as ctx:
            ctx.prec = INDICATOR_PRECISION
            return "value", left * right if node.op == "*" else left / right
    if isinstance(node, Ref):
        text = render(node)
        if text not in atoms:
            raise Unsupported(text, f"atom {text} has no S2 detector")
        consulted.add(text)
        atom = atoms[text]
        if atom.kind == "unavailable":
            return "unknown", atom.reason
        if atom.kind == "null":
            return "null", None
        return "value", {"boolean": atom.boolean, "number": atom.number, "symbol": atom.symbol}[atom.kind]
    raise Unsupported(f"Unsupported({node.kind})", f"operand shape {node.kind!r} is not evaluable in S2")


_CMP = {
    "==": lambda a, b: a == b, "!=": lambda a, b: a != b, ">=": lambda a, b: a >= b,
    "<=": lambda a, b: a <= b, ">": lambda a, b: a > b, "<": lambda a, b: a < b,
}


def _in_band(node: InTest, atoms, cfg, consulted: set[str], unknowns: set[str], units) -> bool | None:
    """FINAL §4 row 1: `<atom> IN cfg(band) <unit>` — an inclusive [lo, hi]
    band. The atom's unit, the Quantity's unit and the band row's own unit
    must all agree; any mismatch is `Unsupported`, named."""
    q = node.right
    atom = ATOMS.get(render(node.left)) if isinstance(node.left, Ref) else None
    gap = unit_mismatch(q.unit, atom.unit if atom else None)
    row_unit = units(q.value.key) if units is not None else None
    if gap is None and row_unit is not None:  # an absent row fails loud in `cfg()` below
        gap = unit_mismatch(q.unit, row_unit)
    if gap is not None:
        raise Unsupported(gap, f"band unit {q.unit!r} does not match")
    ls, lv = _value(node.left, atoms, cfg, consulted)
    if ls == "unknown":
        unknowns.add(lv or "unavailable")
        return None
    if ls == "null":
        return False
    band = cfg(q.value.key)
    if not isinstance(band, (list, tuple)) or len(band) != 2:
        raise Unsupported("Unsupported(band)", f"cfg({q.value.key}) is not a [lo, hi] band")
    lo, hi = (Decimal(str(v)) for v in band)
    return lo <= lv <= hi


def _between(node: Between, context: Mapping[str, Any] | None, unknowns: set[str]) -> bool | None:
    """`flat(<ind>, window: <w>) between turn and cross` (FINAL §4; STEP-5) on
    the frame in `context`: some window of that many working bars between the
    move's turn and the def's own cross in which |slope_norm(<ind>)| stays
    within `cfg(flat_threshold.<ind>)`."""
    from .anatomy.slope import FLAT_KEYS, flat_threshold, slope_bars
    from .formation.atoms import _flat_subject, flat_between, window_bars

    if context is None or _flat_subject(node.subject) is None:
        raise Unsupported(f"Unsupported(between:{render(node.subject)})", "between needs its frame and flat subject")
    indicator, window_node = _flat_subject(node.subject)
    frame, tunables, trigger = context["frame"], context["tunables"], context["trigger"]
    window = window_bars(window_node, context["minutes"])
    threshold = flat_threshold(tunables, indicator)
    if threshold is None:
        unknowns.add(f"{FLAT_KEYS[indicator]}_unset")
        return None
    n = slope_bars(tunables)
    if n is None:
        unknowns.add("slope_norm.bars_unset")
        return None
    atr = frame.objects["atr"]
    if atr is None or atr == 0:
        unknowns.add("insufficient_seed")
        return None
    edges = {}
    edges["turn"] = frame.objects["turn_index"]
    p = getattr(trigger, "params", {}) or {}
    edges["cross"] = (frame.objects["cross_index"](p["a"], p["b"], p["direction"])
                      if trigger.type == "indicator_cross" else None)
    start, end = edges[render(node.start)], edges[render(node.end)]
    if start is None or end is None:
        unknowns.add("insufficient_bars")
        return None
    values = frame.objects["series"](indicator)
    with localcontext() as ctx:
        ctx.prec = INDICATOR_PRECISION
        norm = [None if i < n or values[i] is None or values[i - n] is None else (values[i] - values[i - n]) / (n * atr)
                for i in range(len(values))]
    return flat_between(norm, start=start, end=end, window=window, threshold=threshold)


def _touched(node: Relation, context: Mapping[str, Any] | None, unknowns: set[str]) -> bool | None:
    """`touched(Leg, indicator)` (taxonomy §3.1; STEP-6): the leg's extreme
    reached the indicator on one of its bars — a down leg's low at or under
    it, an up leg's high at or over it (contact, not proximity)."""
    from .formation.atoms import _touched_gaps

    gaps = _touched_gaps(node)
    if context is None or gaps:
        raise Unsupported(min(gaps) if gaps else "touched", "touched needs a served leg and indicator")
    frame = context["frame"]
    roles = frame.objects["pullback_roles"]
    leg = roles.pullback if render(node.left) == "Leg(pullback)" else (
        roles.before if roles.before_role == "impulse" else None)
    if leg is None:
        return False  # no such leg: nothing touched
    values = frame.objects["series"](render(node.right))
    seen = False
    for i, bar in enumerate(frame.run):
        if not (leg.start_ts <= bar.ts <= leg.end_ts) or values[i] is None:
            continue
        seen = True
        if (bar.low <= values[i]) if leg.direction == "down" else (bar.high >= values[i]):
            return True
    if not seen:
        unknowns.add("insufficient_seed")
        return None
    return False


def _on(node: Qualified, context: Mapping[str, Any] | None, unknowns: set[str]) -> bool | None:
    """`Extension.instantiated on Leg(pre_test)` (`A-15`, convention
    `extension.on_leg.form`; STEP-6): the Extension detector run over the
    leg's bars — `Leg(pre_test)` is the run from the open to the pullback
    (`A-14`). No pullback → no pre-test move → False."""
    from .anatomy.extension import detect_extension
    from .formation.atoms import _on_gaps

    gaps = _on_gaps(node)
    if context is None or gaps:
        raise Unsupported(min(gaps) if gaps else "on", "on needs a served subject and leg")
    frame = context["frame"]
    bars = frame.objects["pre_test_bars"]
    if not bars:
        return False
    ext = detect_extension(bars, frame.extension.params)
    if ext.instantiated is None:
        unknowns.add(ext.unavailable or "insufficient_bars")
        return None
    return bool(ext.instantiated)


def _on_that_range_break(node: Qualified, atoms, cfg, consulted, unknowns, context) -> bool | None:
    """`event(retest) on that RangeBreak` (FINAL §4; STEP-8): the anaphora binds
    to the RangeBreak the previous precondition evaluated True; with no
    antecedent it is unknown (`no_antecedent`), never "any"."""
    if context is None or context.get("antecedent") != "RangeBreak":
        unknowns.add("no_antecedent")
        return None
    return evaluate_node(node.subject, atoms, cfg, consulted, unknowns, context=context)


def _after(node: Qualified, atoms, cfg, consulted, unknowns, context) -> bool | None:
    """`RangeBreak.state == failed_trap after event(retest)` (STEP-8): the state
    holds AND its trap close came after the retest bar."""
    if context is None:
        raise Unsupported("after", "after needs its frame")
    held = evaluate_node(node.subject, atoms, cfg, consulted, unknowns, context=context)
    if held is not True:
        return held
    obs = context["frame"].objects["range_break"]
    if isinstance(obs, str) or obs is None or obs.retest_index is None or obs.trap_index is None:
        return False
    return obs.trap_index > obs.retest_index


def _inside(node: Relation, context, unknowns) -> bool | None:
    """`price inside Range(prior)` (`A-21`, convention `range_prior.rule`;
    STEP-8): the last close back under the broken level, above the lowest low
    before the break."""
    if context is None:
        raise Unsupported("inside", "inside needs its frame")
    frame = context["frame"]
    obs = frame.objects["range_break"]
    if isinstance(obs, str):
        unknowns.add(obs)
        return None
    if obs is None or obs.accept_index is None or frame.last_close is None:
        return False
    return obs.prior_low <= frame.last_close < obs.level


def evaluate_node(
    node: Node, atoms: Mapping[str, AtomValue], cfg: Callable[[str], Any], consulted: set[str], unknowns: set[str],
    *, units: Callable[[str], str | None] | None = None, context: Mapping[str, Any] | None = None,
) -> bool | None:
    """Kleene three-valued truth. `unknowns` collects the reasons. `units`
    names a tunable row's unit (the band shape checks it); `context` carries
    the frame and the def's trigger for a relation (`between`)."""
    kw = dict(units=units, context=context)
    if isinstance(node, Not):
        inner = evaluate_node(node.operand, atoms, cfg, consulted, unknowns, **kw)
        return None if inner is None else not inner
    if isinstance(node, And):
        results = [evaluate_node(op, atoms, cfg, consulted, unknowns, **kw) for op in node.operands]
        if any(r is False for r in results):
            return False
        return None if any(r is None for r in results) else True
    if isinstance(node, Between):
        return _between(node, context, unknowns)
    if isinstance(node, EventAtom):  # STEP-8: an event is a boolean atom of the frame
        text = render(node)
        if text not in atoms:
            raise Unsupported(text, f"event {text} has no detector")
        consulted.add(text)
        atom = atoms[text]
        if atom.kind == "unavailable":
            unknowns.add(atom.reason or "unavailable")
            return None
        return bool(atom.boolean)
    if isinstance(node, Relation) and node.op == "touched":
        return _touched(node, context, unknowns)
    if isinstance(node, Relation) and node.op == "inside":
        return _inside(node, context, unknowns)
    if isinstance(node, Qualified) and node.op == "on" and render(node.anchor) == "that RangeBreak":
        return _on_that_range_break(node, atoms, cfg, consulted, unknowns, context)
    if isinstance(node, Qualified) and node.op == "on":
        return _on(node, context, unknowns)
    if isinstance(node, Qualified) and node.op == "after":
        return _after(node, atoms, cfg, consulted, unknowns, context)
    if isinstance(node, Or):
        results = [evaluate_node(op, atoms, cfg, consulted, unknowns, **kw) for op in node.operands]
        if any(r is True for r in results):
            return True
        return None if any(r is None for r in results) else False
    if isinstance(node, Ref):
        state, value = _value(node, atoms, cfg, consulted)
        if state == "unknown":
            unknowns.add(value or "unavailable")
            return None
        if state == "null":
            return False
        if not isinstance(value, bool):
            raise Unsupported(render(node), f"{render(node)} is not a boolean atom")
        return value
    if isinstance(node, Compare):
        ls, lv = _value(node.left, atoms, cfg, consulted)
        rs, rv = _value(node.right, atoms, cfg, consulted)
        for state, value in ((ls, lv), (rs, rv)):
            if state == "unknown":
                unknowns.add(value or "unavailable")
                return None
        if ls == "null" and rs == "null":
            return node.op == "=="  # both absent: equal (STEP-6, `x != null`)
        if ls == "null" or rs == "null":
            return node.op == "!="
        try:
            return bool(_CMP[node.op](lv, rv))
        except TypeError as e:
            raise Unsupported(render(node), f"cannot compare {lv!r} {node.op} {rv!r}") from e
    if isinstance(node, InTest) and isinstance(node.right, Quantity) and isinstance(node.right.value, Cfg):
        return _in_band(node, atoms, cfg, consulted, unknowns, units)
    if isinstance(node, InTest) and isinstance(node.right, SetLiteral):
        ls, lv = _value(node.left, atoms, cfg, consulted)
        if ls == "unknown":
            unknowns.add(lv or "unavailable")
            return None
        if ls == "null":
            return False
        items = [_value(item, atoms, cfg, consulted)[1] for item in node.right.items]
        return lv in items
    raise Unsupported(f"Unsupported({node.kind})", f"predicate shape {node.kind!r} is not evaluable in S2")


# ---------------------------------------------------------------------
# One member x one def
# ---------------------------------------------------------------------


class LoadedDef(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    slug: str
    md5: str = Field(pattern=r"^[0-9a-f]{32}$")
    definition: TradeDef


class MemberInput(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    membership_id: int
    ticker: str
    trade_date: date
    as_of: AwareDatetime
    bars: tuple[Bar, ...]
    daily: DailySeries | None = None
    daily_status: str = "absent"
    rvol: RvolObservation | None = None
    departed: bool = False
    pool_position: int | None = None


class Anchor(BaseModel):
    """FINAL §2.4: what a formation hangs on (`extension_direction` becomes
    this; the old field stays for byte identity)."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    object: str
    direction: Literal["up", "down"] | None
    bar_ts: AwareDatetime | None


class Formation(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    extension_direction: Literal["up", "down"]
    trade_direction: Literal["long", "short"]
    setup_ref: str
    trigger: TriggerLevel
    extreme: TrackedExtreme
    stop: StructuralStop
    stop_ref: str
    formed_bar_ts: AwareDatetime
    formed_bar_end: AwareDatetime
    leg_count: int | None
    #: The assumed keys this formation rests on (R2-2 = B): the static
    #: closure of the definition (R2-2.2), stored on the card's
    #: `assumed_formation` dot at creation, never re-read from live rows.
    assumed_keys: tuple[str, ...]
    #: FINAL §2.4: the frame it formed on — `long` = the stored bars,
    #: `mirrored` = the short side's mirrored bars (prices already negated back).
    side_frame: Literal["long", "mirrored"] = "long"
    #: FINAL §2.4: the object the formation hangs on, in real coordinates.
    anchor: Anchor | None = None
    #: FINAL §2.2 / §2.3: the resolvers' outcomes, in real coordinates.
    trigger_outcome: TriggerOutcome | None = None
    stop_outcome: StopOutcome | None = None


class SideOutcome(BaseModel):
    """One frame's outcome for the scan that computed it (R2-4.1 B): an
    internal model on `MemberEvaluation`, never the seam."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    evaluation: Evaluation
    formation: Formation | None = None
    note: str | None = None


class MemberEvaluation(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    membership_id: int
    ticker: str
    slug: str
    md5: str
    departed: bool
    evaluation: Evaluation
    direction: Literal["long", "short"] | None
    detail: RadarScoreDetail
    #: Every missing item by name, including trigger/stop types (user side).
    missing: tuple[str, ...] = ()
    formation: Formation | None = None
    last_price: Decimal | None = None
    last_bar_ts: AwareDatetime | None = None
    observations: dict[str, FactorObservation] = Field(default_factory=dict)
    inputs_sha256: str
    #: Consumed rows as JSON-ready dicts (the receipt's values, L57).
    consumed_bars: tuple[dict[str, str], ...] = ()
    #: Closed i1 bars after the formation bar (stop-before-arm), and the
    #: closed working bars (health).
    i1_after: tuple[Bar, ...] = ()
    working: tuple[WorkingBar, ...] = ()
    ema9: Decimal | None = None
    note: str | None = None
    #: R2-4.1 B: both frames' outcomes for this scan. Every per-card
    #: decision reads the CARD'S OWN side here, never the published row.
    by_side: dict[Literal["long", "short"], SideOutcome] = Field(default_factory=dict)


def seam_atom(name: str) -> str:
    """`trigger:<type>` -> `Trigger(<type>)`, `stop:<type>[:<ref>]` ->
    `Stop(<type>)[.<ref>]` — generic anatomy spellings the closed seam
    atom validator accepts (the registry's colon form is for humans)."""
    if name.startswith("trigger:"):
        return f"Trigger({name.split(':', 1)[1]})"
    if name.startswith("stop:"):
        parts = name.split(":")
        return f"Stop({parts[1]})" + (f".{parts[2]}" if len(parts) > 2 else "")
    return name


#: S3 detectors are unbuilt, so a def's precondition is free to name an
#: atom that has no anatomy spelling yet — a human placeholder, not an
#: authoring error. `RadarScoreDetail.missing_atoms` (the seam) still
#: refuses free text (L32), so a placeholder collapses to this generic,
#: content-free marker rather than crashing the whole evaluate run for
#: every OTHER member and def. `MemberEvaluation.missing` (user side,
#: below) keeps the real, raw text for local/CLI reporting.
UNSPECIFIED_ATOM = "unspecified_atom"


def seam_safe_missing_atoms(raw: Sequence[str]) -> tuple[str, ...]:
    safe = set()
    for name in raw:
        atom = seam_atom(name)
        try:
            validate_atom(atom)
        except ValueError:
            safe.add(UNSPECIFIED_ATOM)
        else:
            safe.add(atom)
    return tuple(sorted(safe))


def bar_row(bar: Bar) -> dict[str, str]:
    return {"ts": bar.ts.isoformat(), "open": str(bar.open), "high": str(bar.high),
            "low": str(bar.low), "close": str(bar.close), "volume": str(bar.volume)}


def daily_row(bar) -> dict[str, str]:
    return {"session_date": bar.session_date.isoformat(), "open": str(bar.open), "high": str(bar.high),
            "low": str(bar.low), "close": str(bar.close), "volume": str(bar.volume)}


def working_minutes(defaults: TaxonomyDefaults) -> int:
    raw = defaults.working_timeframe.strip()
    if not raw.endswith("m") or not raw[:-1].isdigit():
        raise EvaluateError(f"working_timeframe {raw!r} is not '<n>m'")
    return int(raw[:-1])


def _cfg_value(raw: Any, tunables: Mapping[str, TunableRow], defaults: TaxonomyDefaults) -> Any:
    if isinstance(raw, str) and raw.startswith("cfg(") and raw.endswith(")"):
        return resolve_cfg(raw[4:-1], tunables, defaults)
    return raw


def _obs(name: str, value, bar_ts=None) -> SeamObservation:
    return SeamObservation(name=name, value=None if value is None else Decimal(str(value)), bar_ts=bar_ts)


FACTOR_COMPUTERS = ("atrs_from_open", "rvol", "Extension.leg_count", "htf_level_proximity")


def _factor_observations(
    ext: ExtensionObservation, member: MemberInput, *, intraday_stale: bool, daily_ok: bool,
    last_price: Decimal | None, scan_interval: int,
) -> dict[str, FactorObservation]:
    out: dict[str, FactorObservation] = {}
    atr = ext.atr
    out["atrs_from_open"] = FactorObservation(
        value=ext.distance_from_open_atr, stale=intraday_stale,
        unavailable=ext.unavailable if ext.distance_from_open_atr is None else None,
        inputs={"session_open": _s(ext.session_open), "last_close": _s(ext.last_close),
                "atr": _s(atr.value) if atr else None, "atr_period": atr.period if atr else None,
                "atr_bars_used": atr.bars_used if atr else None},
        formula="|last_close - session_open| / ATR(working_tf, 14) wilder, sma seed",
    )
    if member.rvol is None or member.rvol.value is None:
        out["rvol"] = FactorObservation(value=None, unavailable="no_rvol_observation", formula="screener RVOL")
    else:
        stale = intraday_staleness(
            observed_at=member.rvol.observed_at, as_of=member.as_of, scan_interval=scan_interval
        ).stale
        out["rvol"] = FactorObservation(
            value=Decimal(str(member.rvol.value)), stale=stale,
            inputs={"rvol": str(member.rvol.value), "observed_at": member.rvol.observed_at.isoformat(),
                    "source": member.rvol.source, "precedence": member.rvol.precedence},
            formula="screener RVOL (precedence screen>list, note order, source id)",
        )
    out["Extension.leg_count"] = FactorObservation(
        value=None if ext.leg_count is None else Decimal(ext.leg_count), stale=intraday_stale,
        unavailable=ext.unavailable, inputs={"leg_count": ext.leg_count},
        formula="legs in the run direction, terminated by one opposing bar",
    )
    if not daily_ok or member.daily is None or last_price is None:
        out["htf_level_proximity"] = FactorObservation(
            value=None, stale=member.daily is not None and not daily_ok,
            unavailable=member.daily_status if member.daily is None else "no_last_price",
            formula="min(|last - prior high|, |last - prior low|) / daily ATR(14)",
        )
    else:
        try:
            prox = htf_level_proximity(member.daily, member.trade_date, last_price)
            out["htf_level_proximity"] = FactorObservation(
                value=prox.value,
                inputs={"reference": prox.reference, "level": str(prox.level), "last_price": str(last_price),
                        "daily_atr": str(prox.atr.value), "prior_session": prox.prior.session_date.isoformat()},
                formula="min(|last - prior high|, |last - prior low|) / daily ATR(14)",
            )
        except (NoDailyBars, InsufficientBars) as e:
            out["htf_level_proximity"] = FactorObservation(value=None, unavailable=type(e).__name__, formula="")
    return out


def _s(value) -> str | None:
    return None if value is None else str(value)


#: FINAL §1 / R2-2.2 term (3): the conventions the side-binding line below
#: implements, by their engine ROW key — `A-01` (key
#: `anatomy.orientation.extension`): a def written long-side trades against an
#: unqualified Extension (a DOWN Extension for the long frame). From C2 every
#: convention is also a row (`tunables.yaml`, unit `label`); a null row
#: counts as assumed unconditionally (the C1 rule, carried until he rules it).
ASSUMED_CONVENTIONS: tuple[str, ...] = ("anatomy.orientation.extension",)
#: The label each implemented convention's row may carry; any other non-null
#: label is refused (`not_evaluable: <key>=<label>`), never guessed.
CONVENTION_LABELS: dict[str, str] = {
    "anatomy.orientation.extension": "long_opposes_unqualified_extension",
    # STEP-3 (D1): the conventions the frame's resolvers implement.
    WARMUP_CONVENTION: "premarket_complete_buckets_else_rth_only",  # A-05, `indicators.seeded`
    DAYRANGE_CONVENTION: "rth_high_low_since_open",  # A-06, `session_levels.day_range`
    VWAP_CONVENTION: "rth_anchored_typical_price_i1",  # A-12, `session_levels.vwap`
    # STEP-6 (C5).
    CATALYST_CONVENTION: "radar_in_play_admission",  # A-13, the `catalyst_ref` resolver (FINAL §6)
    PRE_TEST_CONVENTION: "session_open_to_pullback_start",  # A-14, `leg_roles.pre_test_bars`
    ON_LEG_CONVENTION: "extension_detector_over_leg_bars",  # A-15, `evaluate._on`
    # STEP-7 (C6).
    LEVELS_CONVENTION: "pmh_pdh",  # A-17, the level set of `Level_ref(resistance)`
    REJECTED_CONVENTION: "wick_through_close_back_below_still_below",  # A-18, `frame.rejected`
    # STEP-8 (C7), `anatomy.range_break`.
    PRIOR_RANGE_CONVENTION: "session_low_before_break_to_level",  # A-21
    STOP_HIT_CONVENTION: "computed_from_bars_turn_low_less_buffer",  # A-22
    TURN_CANDLE_CONVENTION: "turn_bar_low",  # A-23
}


def _anchored_on_extension(td: TradeDef) -> bool:
    """A-01 applies to a def whose precondition anchor is an unqualified Extension."""
    return any(atom.startswith("Extension.") for p in td.preconditions for atom in p.required_atoms)


def _conventions(td: TradeDef) -> set[str]:
    conventions: set[str] = set(ASSUMED_CONVENTIONS) if _anchored_on_extension(td) else set()
    for predicate in [*td.preconditions, *td.avoid]:
        for atom in predicate.required_atoms:
            if atom in ATOMS:
                conventions |= set(ATOMS[atom].conventions)
            elif atom in RELATIONS:  # STEP-6: a relation's resolver declares its own
                conventions |= set(RELATIONS[atom].conventions)
    return conventions


def convention_refusals(td: TradeDef, tunables: Mapping[str, TunableRow]) -> tuple[str, ...]:
    """`<key>=<label>` for every convention row whose non-null label the code
    does not implement. A declared convention with no row is a loud error."""
    out = []
    for key in sorted(_conventions(td)):
        if key not in tunables:
            raise EvaluateError(f"convention {key!r} has no tunable row — a declared convention must have one")
        value = tunables[key].value
        if value is not None and value != CONVENTION_LABELS[key]:
            out.append(f"{key}={value}")
    return tuple(out)


def closure_keys(td: TradeDef) -> frozenset[str]:
    """R2-2.2 B — the static closure of a definition, the union of (1) every
    `cfg(<key>)` the def names (`iter_cfg_tokens`), (2) the `TUNABLE_KEYS` of
    every detector serving an atom its preconditions or avoids name — and
    (fix round 2 F3) the keys its TRIGGER resolver declares it reads — and
    (3) the conventions of the branches and resolvers it uses."""
    keys: set[str] = set(iter_cfg_tokens(td)) | _conventions(td) | set(trigger_tunable_keys(td.trigger))
    for predicate in [*td.preconditions, *td.avoid]:
        for atom in predicate.required_atoms:
            if atom in ATOMS:
                keys |= set(ATOMS[atom].tunable_keys)
    return frozenset(keys)


def assumed_closure(td: TradeDef, tunables: Mapping[str, TunableRow]) -> tuple[str, ...]:
    """Computed ONCE at formation: the closure's keys whose resolved row reads
    `source: assumed`, plus every convention whose row is still null."""
    keys = closure_keys(td) - _conventions(td)
    out = {key for key in keys if key in tunables and tunables[key].source is TunableSource.ASSUMED}
    for key in _conventions(td):
        row = tunables[key]
        if row.value is None or row.source is TunableSource.ASSUMED:
            out.add(key)
    return tuple(sorted(out))


def publish_frames(*, long: MemberEvaluation, short: MemberEvaluation) -> MemberEvaluation:
    """R2-4.1 B — the ONE row per (run, member, def): the frame that formed
    when exactly one did; `not_formed`, note `both_sides`, with the long
    frame's detail when both did; the LONG frame's evaluation (the def as
    written) when neither did. No order among the non-formed states is
    defined. Both frames' outcomes ride along in `by_side`."""
    by_side = {
        "long": SideOutcome(evaluation=long.evaluation, formation=long.formation, note=long.note),
        "short": SideOutcome(evaluation=short.evaluation, formation=short.formation, note=short.note),
    }
    if long.evaluation == "formed" and short.evaluation == "formed":
        chosen = long.model_copy(update={"evaluation": "not_formed", "note": "both_sides", "formation": None,
                                         "direction": None, "i1_after": ()})
    elif short.evaluation == "formed":
        chosen = short
    else:
        chosen = long
    return chosen.model_copy(update={"by_side": by_side})


def stop_on_protective_side(direction: str, *, trigger: Decimal, stop: Decimal, last_close: Decimal) -> bool:
    """FINAL §9 point (5) — the geometry guard, written ONCE (X17 PASS)."""
    if direction == "long":
        return stop < min(trigger, last_close)
    return stop > max(trigger, last_close)


def _closed_i1(member: MemberInput) -> list[Bar]:
    today = [bar for bar in member.bars if bar.ts.astimezone(ET).date() == member.trade_date]
    return [bar for bar in today if bar.ts + timedelta(minutes=1) <= member.as_of]


def _daily_ok(member: MemberInput, clock) -> bool:
    if member.daily is None:
        return False
    return not daily_staleness(
        member.daily, trade_date=member.trade_date, is_trading_day=clock.calendar.is_trading_day
    ).stale


def _build_frames(
    member: MemberInput, closed_i1: Sequence[Bar], series, run: tuple[WorkingBar, ...], *, daily_ok: bool,
    tunables: Mapping[str, TunableRow], params: ExtensionParams, last_price: Decimal | None, clock,
    bind_side: bool = False,
) -> dict[str, Frame]:
    """FINAL §2.1: one frame per side; the detectors run inside the frame.
    §5: the seed is the complete premarket working buckets of `series`.
    `bind_side`: fix r3 F1 (`frame.binds_side_by_frame`)."""
    premarket_i1, rth_i1 = minute_bars(closed_i1, as_of=member.as_of, clock=clock)
    session = SessionInputs(premarket=premarket_buckets(series.bars, clock), premarket_i1=premarket_i1,
                            rth_i1=rth_i1, departed=member.departed)
    return {
        side: build_frame(side, run, daily=member.daily, daily_ok=daily_ok, trade_date=member.trade_date,
                          params=params, last_close=last_price, session=session, tunables=tunables,
                          bind_side=bind_side)
        for side in ("long", "short")
    }


def member_frames(
    member: MemberInput, *, tunables: Mapping[str, TunableRow], defaults: TaxonomyDefaults, clock,
) -> dict[str, Frame]:
    """Both frames of one member at its `as_of`, built exactly as
    `evaluate_member` builds them."""
    closed_i1 = _closed_i1(member)
    series = working_bars(closed_i1, working_minutes(defaults), as_of=member.as_of)
    return _build_frames(
        member, closed_i1, series, tuple(rth_only(series, clock)), daily_ok=_daily_ok(member, clock),
        tunables=tunables, params=ExtensionParams.from_tunables(tunables),
        last_price=closed_i1[-1].close if closed_i1 else None, clock=clock,
    )


def evaluate_member(
    ld: LoadedDef,
    member: MemberInput,
    *,
    tunables: Mapping[str, TunableRow],
    defaults: TaxonomyDefaults,
    scan_interval: int,
    clock,
) -> MemberEvaluation:
    td = ld.definition
    minutes = working_minutes(defaults)
    closed_i1 = _closed_i1(member)
    consumed = tuple(bar_row(bar) for bar in closed_i1)
    last_bar = closed_i1[-1] if closed_i1 else None
    last_price = last_bar.close if last_bar else None
    base = dict(
        membership_id=member.membership_id, ticker=member.ticker, slug=ld.slug, md5=ld.md5,
        departed=member.departed, consumed_bars=consumed, last_price=last_price,
        last_bar_ts=last_bar.ts if last_bar else None,
    )
    inputs_sha = canonical_sha256({
        "def_md5": ld.md5, "bars": consumed, "as_of": member.as_of.isoformat(),
        "daily": [daily_row(b) for b in member.daily.before(member.trade_date)] if member.daily else None,
        "rvol": member.rvol.model_dump(mode="json") if member.rvol else None,
    })

    def result(evaluation: Evaluation, detail: RadarScoreDetail, **kw) -> MemberEvaluation:
        return MemberEvaluation(**base, evaluation=evaluation, detail=detail, inputs_sha256=inputs_sha, **kw)

    def both(ev: MemberEvaluation) -> MemberEvaluation:
        """A result that does not depend on the side: the same for both frames."""
        return publish_frames(long=ev, short=ev)

    ev = evaluability(td)
    if not ev.evaluable:
        return both(result(
            "not_evaluable", RadarScoreDetail(
                atoms=(), missing_atoms=seam_safe_missing_atoms(ev.missing_atoms), observations=(),
            ),
            direction=None, missing=ev.missing_atoms,
        ))
    refusals = convention_refusals(td, tunables)
    if refusals:
        return both(result(
            "not_evaluable", RadarScoreDetail(
                atoms=(), missing_atoms=seam_safe_missing_atoms(refusals), observations=(),
            ),
            direction=None, missing=refusals, note="a convention row names a rule the code does not implement",
        ))

    series = working_bars(closed_i1, minutes, as_of=member.as_of)
    run = tuple(rth_only(series, clock))
    params = ExtensionParams.from_tunables(tunables)
    if last_bar is None:
        intraday_stale = True
    else:
        intraday_stale = intraday_staleness(
            observed_at=last_bar.ts + timedelta(minutes=1), as_of=member.as_of, scan_interval=scan_interval
        ).stale
    daily_ok = _daily_ok(member, clock)
    frames = _build_frames(member, closed_i1, series, run, daily_ok=daily_ok, tunables=tunables, params=params,
                           last_price=last_price, clock=clock, bind_side=binds_side_by_frame(td))
    # R2-4.2 B: factor and seam observations ONCE, on the real bars (the
    # detector's own Extension, also for a def that binds side by the frame).
    ext, htf = frames["long"].observed, frames["long"].htf

    observations = _factor_observations(
        ext, member, intraday_stale=intraday_stale, daily_ok=daily_ok, last_price=last_price,
        scan_interval=scan_interval,
    )
    # [F-10]: EMA9 has ONE definition — seeded, falling back to RTH-only —
    # and `ema9` (the FILLED card's health input) takes it. `atr_working`
    # stays the Extension's RTH-run ATR; `atr_seeded` is published beside it.
    ema9 = frames["long"].number("EMA9")
    atr_seeded = frames["long"].number("ATR(working_tf)")
    seam_obs = [
        _obs("session_open", ext.session_open, run[0].ts if run else None),
        _obs("last_close", last_price, last_bar.ts if last_bar else None),
        _obs("atr_working", ext.atr.value if ext.atr else None, ext.atr.last_bar_ts if ext.atr else None),
        _obs("atr_seeded", atr_seeded, frames["long"].warm[-1].ts if atr_seeded is not None else None),
        _obs("distance_from_open_atr", ext.distance_from_open_atr),
        _obs("volume_threshold", ext.band.threshold if ext.band else None, ext.culminating_bar_ts),
        _obs("culminating_volume", ext.culminating_volume, ext.culminating_bar_ts),
        _obs("culminating_body", ext.culminating_body, ext.culminating_bar_ts),
        _obs("widest_prior_body", ext.widest_prior_body, ext.culminating_bar_ts),
        _obs("leg_count", ext.leg_count),
        _obs("htf_day_count", htf.day_count if htf else None),
        _obs("rvol", member.rvol.value if member.rvol else None, member.rvol.observed_at if member.rvol else None),
    ]
    extra = dict(
        observations=observations, working=run, ema9=ema9,
        direction=None,
    )

    def detail(frame: Frame, consulted: set[str], path=None, formed_ts=None) -> RadarScoreDetail:
        outcomes = []
        for name in sorted(consulted):
            atom = frame.atoms[name]
            if atom.kind == "unavailable":
                outcomes.append(AtomOutcome(atom=name, value_kind="unavailable", unavailable=atom.reason))
            elif atom.kind == "null":
                outcomes.append(AtomOutcome(atom=name, value_kind="unavailable", unavailable="not_instantiated"))
            else:
                value = getattr(atom, atom.kind)
                if atom.kind == "number" and name in ATOMS and ATOMS[name].price:
                    value = frame.real(value)  # X12: a mirrored price is negated back before publication
                outcomes.append(AtomOutcome(atom=name, value_kind=atom.kind, **{atom.kind: value}))
        return RadarScoreDetail(
            atoms=tuple(outcomes), missing_atoms=(), observations=tuple(seam_obs),
            extension_path=path, formed_bar_ts=formed_ts,
        )

    if intraday_stale:
        return both(result("input_stale", detail(frames["long"], set()),
                           note="intraday bars older than 2 x radar.scan_interval", **extra))

    def cfg(key: str) -> Any:
        return resolve_cfg(key, tunables, defaults)

    def value(raw: Any) -> Any:
        return _cfg_value(raw, tunables, defaults)

    anchored = _anchored_on_extension(td)
    anchor_row = anchor_for(td)
    on_extension = anchor_row is not None and anchor_row.object == "Extension"

    def units(key: str) -> str | None:
        return tunables[key].unit.value if key in tunables else None

    def on_side(frame: Frame) -> MemberEvaluation:
        """One frame's evaluation of the def's LONG-side text; prices in the
        returned formation are real-world (FINAL §2.1 [F-04])."""
        ext = frame.extension
        consulted: set[str] = set()
        context = {"frame": frame, "tunables": tunables, "trigger": td.trigger, "minutes": minutes}
        try:
            pre_unknown: set[str] = set()
            pre = []
            for p in td.preconditions:
                if not p.expr:
                    continue
                pre.append(evaluate_node(p.ast, frame.atoms, cfg, consulted, pre_unknown, units=units,
                                         context=context))
                # STEP-8: the anaphora's antecedent — the RangeBreak a precondition evaluated True on
                if pre[-1] is True and any(a.startswith("RangeBreak") for a in p.required_atoms):
                    context["antecedent"] = "RangeBreak"
            avoid_unknown: set[str] = set()
            avoid = [evaluate_node(p.ast, frame.atoms, cfg, consulted, avoid_unknown, units=units, context=context)
                     for p in td.avoid if p.expr]
        except Unsupported as e:
            return result(
                "not_evaluable",
                RadarScoreDetail(atoms=(), missing_atoms=seam_safe_missing_atoms((e.atom,)),
                                 observations=tuple(seam_obs)),
                missing=(e.atom,), note=str(e), **extra,
            )
        # The Extension path is an Extension formation's evidence only.
        path = ext.path if on_extension or anchor_row is None else None
        avoided_ts = ext.culminating_bar_ts if on_extension or anchor_row is None else None
        if any(r is False for r in pre):
            return result("not_formed", detail(frame, consulted, path), **extra)
        if any(r is None for r in pre):
            if "catalyst_ref_unknown" in pre_unknown:
                return result("not_evaluable", detail(frame, consulted, "B_only"),
                              note="Extension path B only — catalyst unknown in S2 (R4)", **extra)
            if "no_daily_bars" in pre_unknown:
                return result("input_stale", detail(frame, consulted, path), note="daily bars missing or stale",
                              **extra)
            return result("not_formed", detail(frame, consulted, path), note=f"unknown: {sorted(pre_unknown)}",
                          **extra)
        if any(r is True for r in avoid):
            return result("avoided", detail(frame, consulted, path, avoided_ts), **extra)
        if any(r is None for r in avoid):
            state: Evaluation = "input_stale" if "no_daily_bars" in avoid_unknown else "not_formed"
            return result(state, detail(frame, consulted, path), note=f"avoid unknown: {sorted(avoid_unknown)}",
                          **extra)

        # --- formed: the anchor (FINAL §2.4), side binding, trigger, stop --
        if anchor_row is None:
            return result("not_formed", detail(frame, consulted, path), note="no formation anchor", **extra)
        anchor = anchor_row.resolve(frame)
        if isinstance(anchor, str):
            return result("not_formed", detail(frame, consulted, path), note=anchor, **extra)
        # A-01 (FINAL §1): the long-side text trades against an unqualified
        # Extension — in the frame's coordinates, a DOWN one.
        if anchored and on_extension and anchor.direction != "down":
            return result("not_formed", detail(frame, consulted, path),
                          note="the unqualified Extension runs with this side (A-01)", **extra)
        placement = td.stop.placement
        try:
            trigger = trigger_resolver(td.trigger).resolve(frame, td.trigger, value)
            stop = stop_resolver(placement).resolve(frame, placement, value, trigger=trigger)
        except (InsufficientBars, IncompleteBucket) as e:
            return result("not_formed", detail(frame, consulted, path), note=f"trigger/stop unavailable: {e}",
                          **extra)
        if not stop_on_protective_side("long", trigger=trigger.price, stop=stop.price, last_close=frame.last_close):
            return result("not_formed", detail(frame, consulted, path), note="stop_wrong_side", **extra)
        side = frame.side
        trigger, stop = trigger.unmirrored(side), stop.unmirrored(side)
        real_direction = anchor.direction if side == "long" else ("up" if anchor.direction == "down" else "down")
        formed_end = anchor.bar_ts + timedelta(minutes=minutes)
        formation = Formation(
            # `extension_direction` stays for byte identity; for another
            # anchor it carries that anchor's (real) direction (§2.4).
            extension_direction=real_direction, trade_direction=side, setup_ref=UNCLASSIFIED_SETUP,
            trigger=trigger.level, extreme=stop.extreme, stop=stop.structural, stop_ref=stop.ref,
            formed_bar_ts=anchor.bar_ts, formed_bar_end=formed_end, leg_count=ext.leg_count,
            assumed_keys=assumed_closure(td, tunables), side_frame="long" if side == "long" else "mirrored",
            anchor=Anchor(object=anchor.object, direction=real_direction, bar_ts=anchor.bar_ts),
            trigger_outcome=trigger, stop_outcome=stop,
        )
        i1_after = tuple(bar for bar in closed_i1 if bar.ts >= formed_end)
        return result(
            "formed", detail(frame, consulted, path, anchor.bar_ts), formation=formation,
            i1_after=i1_after, **{**extra, "direction": side},
        )

    return publish_frames(long=on_side(frames["long"]), short=on_side(frames["short"]))


def card_why(td: TradeDef, formation: Formation) -> str:
    """FINAL §2.4 [F-05]: assembled from the resolvers' own fragments. The
    Extension formation keeps its sentence byte for byte."""
    if formation.anchor is not None and formation.anchor.object != "Extension":
        t, s = formation.trigger_outcome, formation.stop_outcome
        return (
            f"{formation.setup_ref} · {formation.anchor.object} (bar "
            f"{formation.formed_bar_ts.astimezone(ET):%H:%M} ET) — {formation.trade_direction} on the "
            f"{t.why if t else 'trigger'} at {formation.trigger.price}; stop {formation.stop.price} "
            f"{s.why if s else ''}".rstrip()
        )
    return (
        f"{formation.setup_ref} · Extension culminating (path A, {formation.leg_count} legs, "
        f"bar {formation.formed_bar_ts.astimezone(ET):%H:%M} ET) — {formation.trade_direction} on a "
        f"{formation.trigger.bars_cleared}-bar break at {formation.trigger.price}; stop "
        f"{formation.stop.price} beyond the {formation.stop_ref} extreme {formation.extreme.price}"
    )


def assumed_keys_of(dots: Iterable[Dot]) -> tuple[str, ...]:
    """The keys a card's OWN stored `assumed_formation` dot names — never a
    live tunable row, so a row ruled later does not lift an open card. No
    dot -> no keys."""
    for dot in dots:
        if dot.factor == ASSUMED_FORMATION:
            return tuple(dot.engine_inputs["assumed_keys"])
    return ()


def card_dots(
    ld: LoadedDef,
    ev: MemberEvaluation,
    settings: CardSettings,
    at: datetime,
    assumed_keys: Sequence[str],
    *,
    previous: Iterable[Dot] | None = None,
    added_by: Mapping[str, Any] | None = None,
) -> list[Dot]:
    """THE one builder of a card's dots (R2-2.1, L3), at all four sites:
    create, `refresh_card`, `replay_receipt`, the audit export. The quality
    factors' dots (carried across `refresh_dots` from `previous` when given),
    then — when `assumed_keys` is non-empty — the ONE untappable
    `assumed_formation` dot, appended after the refresh."""
    dots = compute_dots(ld.definition.quality_factors, ev.observations, settings.curves, at=at)
    if previous is not None:
        dots = refresh_dots(previous, dots, at=at, added_by=added_by)
    if assumed_keys:
        keys = list(assumed_keys)
        dots.append(Dot(
            factor=ASSUMED_FORMATION, position=len(ld.definition.quality_factors), source="cobalt-degraded",
            tier="deterministic", role="shadow", na_reason="ASSUMED", engine_inputs={"assumed_keys": keys},
            engine_why=f"formed on assumed defaults: {', '.join(keys)}",
        ))
    return dots


def desk_shadow() -> DeskShadow:
    """S2: the desk supplies nothing — catalyst DESK_NA, both alignments
    DEFAULT_UNRULED (plan §8 ESCALATE 4)."""
    def entry(reason: str) -> DeskShadowEntry:
        return DeskShadowEntry(na_reason=reason, why_code=reason.lower(), formula_version=DESK_FORMULA_VERSION)

    return DeskShadow(
        catalyst=entry("DESK_NA"), market_alignment=entry("DEFAULT_UNRULED"),
        sector_alignment=entry("DEFAULT_UNRULED"),
    )


# ---------------------------------------------------------------------
# Open cards (read model the stage refreshes)
# ---------------------------------------------------------------------


class OpenRadarCard(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    card_id: int
    pool_member_id: int
    ticker: str
    direction: Literal["long", "short"]
    state: str
    trade_def_slug: str
    trade_def_md5: str
    trigger_price: Decimal
    structural_stop: Decimal
    entry: Decimal
    stop: Decimal
    formed_at: AwareDatetime
    expires_at: AwareDatetime
    promoted_at: datetime | None = None
    health: dict[str, Any] | None = None
    dots: list[Dot] = Field(default_factory=list)
    taps: list[dict[str, Any]] = Field(default_factory=list)


class CardUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    card_id: int
    proximity: Decimal
    conviction: Decimal | None
    card_score: int | None
    score_suppressed: str | None
    proposed_key: str | None
    dots: list[Dot]
    health: dict[str, Any] | None
    radar_score_id: int | None
    #: The newest tap id the update was computed from; the store leaves
    #: conviction/score/key alone when a newer tap landed under the lock.
    tap_version: int = 0
    #: The scan's last closed i1 close ("updates proximity/last", STEP-4).
    last_price: Decimal | None = None


#: The TradeDef fields the catalyst-review workflow may edit under an open
#: card (Astra R2-4). Every other field shaped the card's formation.
CATALYST_REVIEW_FIELDS = frozenset(
    {"quality_factors", "preferred_windows", "preferred_windows_ref", "aliases", "name", "reference_stats"}
)


def formation_changes(original: TradeDef, current: TradeDef) -> list[str]:
    """The formation fields `current` changed against `original`, named;
    empty = an edit scoped to `CATALYST_REVIEW_FIELDS` only."""
    before, after = original.model_dump(mode="json"), current.model_dump(mode="json")
    return [
        f"{name} changed since formation"
        for name in TradeDef.model_fields
        if name not in CATALYST_REVIEW_FIELDS and before[name] != after[name]
    ]


def refresh_card(
    card: OpenRadarCard,
    ev: MemberEvaluation,
    ld: LoadedDef,
    settings: CardSettings,
    enabled: Sequence[Grade],
    *,
    at: datetime,
    thresholds: HealthThresholds | None,
    run_id: int | None = None,
) -> CardUpdate:
    """The per-scan numbers for an existing card, from this scan's
    evaluation. Formation evidence is never touched. `ld` is the def of
    the card's slug as loaded NOW — after a note edit its md5 differs from
    the card's formation md5, and a factor it gained is added once."""
    dots = card_dots(ld, ev, settings, at, assumed_keys_of(card.dots), previous=card.dots,
                     added_by={"definition_md5": ld.md5, "run_id": run_id})
    last = ev.last_price if ev.last_price is not None else card.entry
    score = score_card(dots, last=last, trigger=card.entry, stop=card.stop,
                       bands=settings.proposed_key, enabled=enabled)
    health = card.health
    if card.state == "FILLED" and thresholds is not None:
        snapshot = (health or {}).get("entry_snapshot")
        if snapshot is None:
            snapshot = EntrySnapshot(
                captured_at=at,
                rvol=ev.observations["rvol"].value if "rvol" in ev.observations else None,
                spread=None,
                dot_grades={d.factor: d.engine_grade for d in dots if d.computed and d.engine_grade is not None},
            ).model_dump(mode="json")
        snap = EntrySnapshot.model_validate(snapshot)
        filled_bars = [b for b in ev.working if b.ts >= snap.captured_at - timedelta(minutes=b.minutes)]
        pills = card_health(
            snapshot=snap, current_rvol=ev.observations["rvol"].value if "rvol" in ev.observations else None,
            current_spread=None, dots=dots, stop=card.stop, direction=card.direction,
            intrabar=filled_bars, closed=filled_bars, ema9=ev.ema9, t=thresholds,
        )
        health = {"entry_snapshot": snapshot, "pills": [p.model_dump(mode="json") for p in pills],
                  "checked_at": at.isoformat()}
    return CardUpdate(
        card_id=card.card_id, proximity=score.proximity, conviction=score.conviction,
        card_score=score.card_score, score_suppressed=score.score_suppressed,
        proposed_key=score.proposed_key.value if score.proposed_key else None, dots=dots,
        health=health, radar_score_id=None, tap_version=max((int(t["id"]) for t in card.taps), default=0),
        last_price=ev.last_price,
    )


def overlay_taps(dots: Iterable[Dot], taps: Iterable[Mapping[str, Any]]) -> list[Dot]:
    """The latest tap per factor, applied — how replay rebuilds trader grades."""
    latest: dict[str, Mapping[str, Any]] = {}
    for tap in sorted(taps, key=lambda t: t["id"]):
        latest[tap["factor"]] = tap
    return [
        d.model_copy(update={"trader_grade": int(latest[d.factor]["grade"])}) if d.factor in latest else d
        for d in dots
    ]


# ---------------------------------------------------------------------
# Receipt chaining and replay
# ---------------------------------------------------------------------


class ReceiptChain:
    """What this process already stored for a (pool, trade date) chain."""

    def __init__(self):
        self.key: tuple[str, date] | None = None
        self.last_receipt_id: int | None = None
        self.bar_rows: dict[str, dict[str, str]] = {}
        self.daily_sha: dict[str, str] = {}
        self.snapshot_sha: dict[str, str] = {}

    def reset(self, key: tuple[str, date]) -> None:
        self.__init__()
        self.key = key

    def row_sha(self, row: Mapping[str, str]) -> str:
        return canonical_sha256(row)


def _snapshot(chain: ReceiptChain, name: str, payload: Any) -> Any:
    sha = canonical_sha256(payload)
    if chain.last_receipt_id is not None and chain.snapshot_sha.get(name) == sha:
        return {"unchanged_since_receipt": chain.last_receipt_id, "sha256": sha}
    return {"sha256": sha, "value": payload}


def build_receipt(
    chain: ReceiptChain,
    *,
    run_id: int,
    pool_key: str,
    scan_id: int,
    evaluated_at: datetime,
    trade_date: date,
    cohort: list[dict[str, Any]],
    pool_unit: dict[str, Any],
    tunables_snapshot: dict[str, Any],
    settings_snapshot: dict[str, Any],
    definitions_snapshot: dict[str, Any],
    members: list[MemberInput],
    cards: list[dict[str, Any]],
    scan_interval: int,
) -> dict[str, Any]:
    """The receipt row (values, not hashes) and the chain bookkeeping it
    implies. The caller commits `chain_commit` only after the INSERT.

    `valid_until` per dependency type (Astra R1-12): intraday bars stay
    valid 2 × scan_interval past `as_of`; daily bars until the trade
    date's session boundary (ET midnight after it)."""
    daily_valid_until = datetime.combine(trade_date + timedelta(days=1), datetime.min.time(), ET).isoformat()
    if chain.key != (pool_key, trade_date):
        chain.reset((pool_key, trade_date))
    observations_members = []
    staged_rows: dict[str, dict[str, str]] = {}
    staged_daily: dict[str, str] = {}
    for member in members:
        rows = [bar_row(b) for b in member.bars if b.ts.astimezone(ET).date() == trade_date
                and b.ts + timedelta(minutes=1) <= member.as_of]
        full_sha = canonical_sha256(rows)
        delta = []
        for row in rows:
            key = f"{member.ticker}|{row['ts']}"
            sha = chain.row_sha(row)
            if chain.bar_rows.get(key) != sha:
                delta.append(row)
            staged_rows[key] = sha
        daily_rows = [daily_row(b) for b in member.daily.bars] if member.daily else None
        daily_sha = canonical_sha256(daily_rows)
        if daily_rows is not None and chain.last_receipt_id is not None and chain.daily_sha.get(member.ticker) == daily_sha:
            daily_payload: Any = {"unchanged_since_receipt": chain.last_receipt_id, "sha256": daily_sha}
        else:
            daily_payload = {"sha256": daily_sha, "rows": daily_rows}
        staged_daily[member.ticker] = daily_sha
        observations_members.append({
            "membership_id": member.membership_id, "ticker": member.ticker, "departed": member.departed,
            "trade_date": trade_date.isoformat(), "as_of": member.as_of.isoformat(),
            "pool_position": member.pool_position,
            "bars": {
                "locator": f"system.bars:i1:{member.ticker}:{trade_date.isoformat()}",
                "collector": "cobalt.radar.poller", "status": "ok" if rows else "empty",
                "row_count": len(rows), "sha256": full_sha, "rows_delta": delta,
                "valid_until": (member.as_of + timedelta(seconds=2 * scan_interval)).isoformat(),
            },
            "daily": {
                "locator": f"radar-cache/{trade_date.isoformat()}/daily/{member.ticker}.csv",
                "collector": "cobalt.radar.collector.FinvizDailyBarsCollector",
                "status": member.daily_status, "valid_until": daily_valid_until,
                "fetched_at": member.daily.fetched_at.isoformat() if member.daily and member.daily.fetched_at else None,
                **daily_payload,
            },
            "rvol": (
                {**member.rvol.model_dump(mode="json"), "sha256": canonical_sha256(member.rvol.model_dump(mode="json"))}
                if member.rvol else None
            ),
        })
    receipt = {
        "run_id": run_id, "pool_key": pool_key, "scan_id": scan_id, "evaluated_at": evaluated_at,
        "ordered_cohort": cohort, "tie_policy": TIE_POLICY,
        "pool_unit": _snapshot(chain, "pool_unit", pool_unit),
        "pool_unit_sha256": canonical_sha256(pool_unit),
        "tunables_snapshot": _snapshot(chain, "tunables", tunables_snapshot),
        "settings_snapshot": _snapshot(chain, "settings", settings_snapshot),
        "definitions_snapshot": _snapshot(chain, "definitions", definitions_snapshot),
        "tap_versions": {"cards": cards},
        "observations": {
            "base_receipt_id": chain.last_receipt_id, "trade_date": trade_date.isoformat(),
            "evaluator_version": EVALUATOR_VERSION, "members": observations_members,
        },
    }
    staged = {
        "bar_rows": staged_rows, "daily": staged_daily,
        "snapshots": {
            "pool_unit": canonical_sha256(pool_unit), "tunables": canonical_sha256(tunables_snapshot),
            "settings": canonical_sha256(settings_snapshot), "definitions": canonical_sha256(definitions_snapshot),
        },
    }
    return {"row": receipt, "staged": staged}


def chain_commit(chain: ReceiptChain, receipt_id: int, staged: Mapping[str, Any]) -> None:
    chain.bar_rows.update(staged["bar_rows"])
    chain.daily_sha.update(staged["daily"])
    chain.snapshot_sha.update(staged["snapshots"])
    chain.last_receipt_id = receipt_id


class ReplayError(ValueError):
    """A receipt chain that does not rebuild to the hashes it recorded."""


def _resolve_snapshot(receipts: Sequence[Mapping[str, Any]], column: str, index: int) -> Any:
    entry = receipts[index][column]
    while "unchanged_since_receipt" in entry:
        target = entry["unchanged_since_receipt"]
        found = [i for i, r in enumerate(receipts) if r["id"] == target]
        if not found:
            raise ReplayError(f"{column} references receipt {target}, not in the chain")
        entry = receipts[found[0]][column]
    if canonical_sha256(entry["value"]) != entry["sha256"]:
        raise ReplayError(f"{column} value does not hash to its recorded sha256")
    return entry["value"]


def rebuild_members(receipts: Sequence[Mapping[str, Any]]) -> list[MemberInput]:
    """The target (last) receipt's members, rebuilt from the chain."""
    rows: dict[str, dict[str, dict[str, str]]] = {}
    daily: dict[str, list[dict[str, str]] | None] = {}
    for receipt in receipts:
        for member in receipt["observations"]["members"]:
            ticker = member["ticker"]
            for row in member["bars"]["rows_delta"]:
                rows.setdefault(ticker, {})[row["ts"]] = row
            if "rows" in member["daily"]:
                daily[ticker] = member["daily"]["rows"]
    target = receipts[-1]
    out = []
    for member in target["observations"]["members"]:
        ticker = member["ticker"]
        as_of = datetime.fromisoformat(member["as_of"])
        trade_date = date.fromisoformat(member["trade_date"])
        ticker_rows = sorted(
            (r for ts, r in rows.get(ticker, {}).items() if datetime.fromisoformat(ts) + timedelta(minutes=1) <= as_of
             and datetime.fromisoformat(ts).astimezone(ET).date() == trade_date),
            key=lambda r: r["ts"],
        )
        if len(ticker_rows) != member["bars"]["row_count"] or canonical_sha256(ticker_rows) != member["bars"]["sha256"]:
            raise ReplayError(f"{ticker}: rebuilt bars do not match the receipt's row count / sha256")
        bars = tuple(
            Bar(ticker=ticker, interval=Interval.I1, ts=datetime.fromisoformat(r["ts"]), open=Decimal(r["open"]),
                high=Decimal(r["high"]), low=Decimal(r["low"]), close=Decimal(r["close"]), volume=int(r["volume"]))
            for r in ticker_rows
        )
        daily_rows = daily.get(ticker)
        if canonical_sha256(daily_rows) != member["daily"]["sha256"]:
            raise ReplayError(f"{ticker}: rebuilt daily rows do not match the receipt's sha256")
        series = None
        if daily_rows is not None:
            from .anatomy.daily import DailyBar

            series = DailySeries(
                ticker=ticker,
                bars=tuple(DailyBar(session_date=date.fromisoformat(r["session_date"]), open=Decimal(r["open"]),
                                    high=Decimal(r["high"]), low=Decimal(r["low"]), close=Decimal(r["close"]),
                                    volume=int(r["volume"])) for r in daily_rows),
                fetched_at=datetime.fromisoformat(member["daily"]["fetched_at"]) if member["daily"]["fetched_at"] else None,
                source=member["daily"]["status"],
            )
        rvol = None
        if member["rvol"] is not None:
            payload = {k: v for k, v in member["rvol"].items() if k != "sha256"}
            rvol = RvolObservation.model_validate(payload)
        out.append(MemberInput(
            membership_id=member["membership_id"], ticker=ticker, trade_date=trade_date, as_of=as_of,
            bars=bars, daily=series, daily_status=member["daily"]["status"], rvol=rvol,
            departed=member["departed"], pool_position=member["pool_position"],
        ))
    return out


class ReplayedCard(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    card_id: int
    published: dict[str, Any]
    recomputed: dict[str, Any]


def published_numbers(update: CardUpdate) -> dict[str, Any]:
    return {
        "proximity": str(update.proximity),
        "conviction": None if update.conviction is None else str(update.conviction),
        "card_score": update.card_score, "score_suppressed": update.score_suppressed,
        "proposed_key": update.proposed_key,
        "dots": [
            {"factor": d.factor, "engine_value": None if d.engine_value is None else str(d.engine_value),
             "engine_grade": d.engine_grade, "na_reason": d.na_reason, "trader_grade": d.trader_grade}
            for d in update.dots
        ],
    }


def replay_receipt(receipts: Sequence[Mapping[str, Any]], *, clock) -> tuple[list[MemberEvaluation], list[ReplayedCard]]:
    """Recompute every seam evaluation and card number of the LAST receipt
    in `receipts` (ordered oldest -> newest, `id` present) from receipt
    values only."""
    index = len(receipts) - 1
    for receipt in receipts:  # §9 gate 5: never recompute another version's receipt with this code
        written = receipt["observations"]["evaluator_version"]
        if written != EVALUATOR_VERSION:
            raise ReplayError(
                f"receipt {receipt.get('id')} was written by evaluator {written!r}; this code is "
                f"{EVALUATOR_VERSION!r} — refusing to recompute it"
            )
    tunables_raw = _resolve_snapshot(receipts, "tunables_snapshot", index)
    settings_raw = _resolve_snapshot(receipts, "settings_snapshot", index)
    defs_raw = _resolve_snapshot(receipts, "definitions_snapshot", index)
    tunables = {key: TunableRow.model_validate(row) for key, row in tunables_raw["rows"].items()}
    defaults = TaxonomyDefaults.model_validate(tunables_raw["defaults"])
    scan_interval = int(tunables["radar.scan_interval"].value)
    settings = CardSettings.from_rows(settings_raw["card"])
    enabled = [Grade(g) for g in settings_raw["enabled_grades_today"]]
    defs = {d["md5"]: LoadedDef(slug=d["slug"], md5=d["md5"], definition=TradeDef.model_validate(d["definition"]))
            for d in defs_raw["defs"]}
    members = rebuild_members(receipts)
    evaluations = []
    by_key: dict[tuple[int, str], MemberEvaluation] = {}
    for member in members:
        for ld in defs.values():
            ev = evaluate_member(ld, member, tunables=tunables, defaults=defaults, scan_interval=scan_interval, clock=clock)
            evaluations.append(ev)
            by_key[(member.membership_id, ld.md5)] = ev
    cards = []
    at = receipts[index]["evaluated_at"]
    at = datetime.fromisoformat(at) if isinstance(at, str) else at
    for card in receipts[index]["tap_versions"]["cards"]:
        # The def the stage refreshed the card with (a later edit of the
        # same slug may differ from the card's formation md5, R2-4).
        md5 = card.get("definition_md5") or card["trade_def_md5"]
        ev = by_key.get((card["pool_member_id"], md5))
        if ev is None:
            raise ReplayError(f"card {card['card_id']}: no evaluation for its member/def in the receipt")
        ld = defs[md5]
        dots = overlay_taps(card_dots(ld, ev, settings, at, card["assumed_keys"]), card["taps"])
        last = ev.last_price if ev.last_price is not None else Decimal(card["entry"])
        score = score_card(dots, last=last, trigger=Decimal(card["entry"]), stop=Decimal(card["stop"]),
                           bands=settings.proposed_key, enabled=enabled)
        recomputed = published_numbers(CardUpdate(
            card_id=card["card_id"], proximity=score.proximity, conviction=score.conviction,
            card_score=score.card_score, score_suppressed=score.score_suppressed,
            proposed_key=score.proposed_key.value if score.proposed_key else None, dots=dots, health=None,
            radar_score_id=None,
        ))
        cards.append(ReplayedCard(card_id=card["card_id"], published=card["published"], recomputed=recomputed))
    return evaluations, cards


# ---------------------------------------------------------------------
# The stage
# ---------------------------------------------------------------------


class StageOutcome(BaseModel):
    model_config = ConfigDict(extra="forbid")

    run_id: int
    status: Literal["complete"]
    cards_enabled: bool
    evaluations: list[MemberEvaluation]
    created: list[int] = Field(default_factory=list)
    refreshed: list[int] = Field(default_factory=list)
    expired: list[int] = Field(default_factory=list)
    refusals: list[str] = Field(default_factory=list)
    receipt_id: int


class EvaluateStage:
    """S5. Dependencies are injected so the stage runs against fakes in
    tests and against the side-scoped stores in the resident.

    radar_store  (SYSTEM) admitted_members, memberships, i1_bars,
                 latest_run_id, abandon_running_runs, open_score_run,
                 put_scores, copy_card_values, finish_run
    card_store   (USER)   open_radar_cards, formation_consumed,
                 create_radar_card, refresh_radar_card, expire_radar_card,
                 write_receipt
    defs_source  () -> (list[LoadedDef], {key: TunableRow} user rows)
    settings     () -> raw trader_settings values (read per cycle)
    daily_source async (ticker, now) -> DailySeries
    """

    def __init__(
        self,
        *,
        radar_store,
        card_store,
        defs_source: Callable[[], tuple[list[LoadedDef], dict[str, TunableRow]]],
        settings_values: Callable[[], dict[str, Any]],
        daily_source,
        tunables_loader: Callable[[], Mapping[str, TunableRow]],
        defaults_loader: Callable[[], TaxonomyDefaults],
        clock,
        now: Callable[[], datetime],
        members_at: Callable[[str, datetime], list[dict]] | None = None,
        rung_source: Callable[[datetime, Any], str] | None = None,
    ):
        # `rung_source(instant, daymode_cfg)` is today's day-mode rung, whose
        # enabled grades the proposed key respects. The resident wires the
        # decided day mode (`DayModeStore` + `decided_or_stage1`); `None` is
        # the stage-1 system rule with no decision read (tests, harness).
        self.rung_source = rung_source
        # `members_at` lets the dev-persistence harness evaluate a PAST day's
        # cohort; the resident reads the open admitted episodes.
        self.members_at = members_at
        self.radar_store = radar_store
        self.card_store = card_store
        self.defs_source = defs_source
        self.settings_values = settings_values
        self.daily_source = daily_source
        self.tunables_loader = tunables_loader
        self.defaults_loader = defaults_loader
        self.clock = clock
        self.now = now
        self.chain = ReceiptChain()
        self._formation_defs: dict[str, TradeDef] = {}

    def lifecycle_tickers(self, admitted: Iterable[str]) -> list[str]:
        """Tickers of open radar cards whose member left the pool — S4
        keeps polling them (Astra R1-15) inside the demand ceiling."""
        held = set(admitted)
        cards = self.card_store.open_radar_cards()
        return sorted({c.ticker for c in cards if c.ticker not in held})

    async def run(
        self,
        *,
        pool_key: str,
        scan_id: int,
        session: str,
        instant: datetime,
        rvol: Mapping[str, RvolObservation],
        pool_unit: dict[str, Any],
        gate: Callable[[str], Callable[[], None]],
    ) -> StageOutcome:
        from cobalt.settings.models import TraderSettings
        from cobalt.taxonomy.loader import merge_tunables

        raw_settings = self.settings_values()
        settings = CardSettings.from_rows(raw_settings)
        trader = TraderSettings._build(raw_settings, where='"user".trader_settings')
        engine_rows = dict(self.tunables_loader())
        defs, user_rows = self.defs_source()
        tunables = merge_tunables(engine_rows, user_rows)
        defaults = self.defaults_loader()
        scan_interval = int(tunables["radar.scan_interval"].value)
        trade_date = self.clock.to_et(instant).date()
        if self.rung_source is not None:
            mode = self.rung_source(instant, trader.daymode)
        else:
            from cobalt.daymode.propose import decided_or_stage1

            mode = decided_or_stage1(None, trader.daymode, now=instant)
        enabled = trader.daymode.enabled_grades_for(mode)
        red, amber = colour_thresholds(tunables)
        thresholds = HealthThresholds.from_tunables(tunables)

        members_raw = sorted(
            self.members_at(pool_key, instant) if self.members_at else self.radar_store.admitted_members(pool_key),
            key=lambda m: m["id"],
        )
        open_cards = self.card_store.open_radar_cards() if settings.cards_enabled else []
        admitted_ids = {m["id"] for m in members_raw}
        departed_ids = sorted({c.pool_member_id for c in open_cards} - admitted_ids)
        departed_raw = self.radar_store.memberships(departed_ids) if departed_ids else []

        start = datetime.combine(trade_date, datetime.min.time(), ET).astimezone(timezone.utc)
        members: list[MemberInput] = []
        for raw, departed in [*((m, False) for m in members_raw), *((m, True) for m in departed_raw)]:
            ticker = raw["ticker"]
            bars = tuple(self.radar_store.i1_bars(ticker, start, instant))
            daily, status = None, "absent"
            try:
                daily = await self.daily_source(ticker, instant)
                status = daily.source or "ok"
            except Exception as e:  # a dead source is loud on the receipt, not a crash of the run
                status = f"failed: {type(e).__name__}: {e}"[:200]
                logger.error("radar S5 daily bars for {} failed: {}", ticker, status)
            members.append(MemberInput(
                membership_id=raw["id"], ticker=ticker, trade_date=trade_date, as_of=instant, bars=bars,
                daily=daily, daily_status=status, rvol=rvol.get(ticker), departed=departed,
                pool_position=raw.get("last_rank"),
            ))

        cohort = [
            {"membership_id": m.membership_id, "ticker": m.ticker, "departed": m.departed,
             "pool_position": m.pool_position,
             "bar_watermark": m.bars[-1].ts.isoformat() if m.bars else None}
            for m in members
        ]
        tunables_snapshot = {
            "rows": {k: row.model_dump(mode="json") for k, row in sorted(tunables.items())},
            "defaults": defaults.model_dump(mode="json"),
        }
        definitions_snapshot = {"defs": [
            {"slug": d.slug, "md5": d.md5, "definition": d.definition.model_dump(mode="json", by_alias=True)}
            for d in sorted(defs, key=lambda d: d.slug)
        ]}
        settings_snapshot = {
            "card": settings.rows(), "mode": mode, "sheet": trader.daymode.sheet_for(mode),
            "enabled_grades_today": [g.value for g in enabled],
        }

        self.radar_store.abandon_running_runs(pool_key, now=instant, before_commit=gate("evaluate:abandon"))
        run_id = self.radar_store.open_score_run(
            {
                "pool_key": pool_key, "scan_id": scan_id,
                "previous_run_id": self.radar_store.latest_run_id(pool_key),
                "session": session, "started_at": instant, "cards_enabled": settings.cards_enabled,
                "evaluator_version": EVALUATOR_VERSION, "formula_sha256": formula_sha256(),
                "tunables_sha256": canonical_sha256(tunables_snapshot),
                "settings_sha256": settings.sha256(), "cohort_sha256": canonical_sha256(cohort),
            },
            before_commit=gate("evaluate:run"),
        )
        try:
            return await self._evaluate(
                run_id=run_id, pool_key=pool_key, scan_id=scan_id, instant=instant, trade_date=trade_date,
                members=members, defs=defs, tunables=tunables, defaults=defaults, scan_interval=scan_interval,
                settings=settings, enabled=enabled, open_cards=open_cards, thresholds=thresholds,
                cohort=cohort, pool_unit=pool_unit, tunables_snapshot=tunables_snapshot,
                settings_snapshot=settings_snapshot, definitions_snapshot=definitions_snapshot,
                session=session, gate=gate, colours=(red, amber),
            )
        except Exception as e:
            from .runner import StageDropped

            if isinstance(e, StageDropped):
                raise  # nothing commits in market_reset; the next cycle abandons the run
            detail = f"{type(e).__name__}: {e}"[:500]
            self.radar_store.finish_run(run_id, status="failed", finished_at=self.now(), detail=detail,
                                        before_commit=gate("evaluate:fail"))
            raise EvaluateError(detail) from e

    async def _evaluate(self, *, run_id, pool_key, scan_id, instant, trade_date, members, defs, tunables,
                        defaults, scan_interval, settings, enabled, open_cards, thresholds, cohort, pool_unit,
                        tunables_snapshot, settings_snapshot, definitions_snapshot, session, gate, colours):
        by_md5 = {d.md5: d for d in defs}
        by_slug = {d.slug: d for d in defs}
        card_defs = {(c.pool_member_id, c.trade_def_slug) for c in open_cards}
        evaluations: list[MemberEvaluation] = []
        for member in members:
            for ld in defs:
                if member.departed and (member.membership_id, ld.slug) not in card_defs:
                    continue  # a departed member forms no new card
                evaluations.append(evaluate_member(
                    ld, member, tunables=tunables, defaults=defaults, scan_interval=scan_interval, clock=self.clock,
                ))
        score_ids = self.radar_store.put_scores(
            run_id,
            [
                {"membership_id": ev.membership_id, "ticker": ev.ticker, "trade_def_md5": ev.md5,
                 "direction": ev.direction, "evaluation": ev.evaluation,
                 "detail": ev.detail.model_dump(mode="json"), "desk_shadow": desk_shadow().model_dump(mode="json"),
                 "inputs_sha256": ev.inputs_sha256}
                for ev in evaluations
            ],
            before_commit=gate("evaluate:scores"),
        )
        outcome = StageOutcome(
            run_id=run_id, status="complete", cards_enabled=settings.cards_enabled, evaluations=evaluations,
            receipt_id=0,
        )
        receipt_cards: list[dict[str, Any]] = []
        copies: list[dict[str, Any]] = []
        if settings.cards_enabled:
            ev_by = {(ev.membership_id, ev.md5): ev for ev in evaluations}
            # Keyed by TICKER, not membership id: a name that leaves and
            # re-enters the pool is a new membership episode, and its still
            # open card must block a second card for the same trade
            # (Astra R1-15 re-entry). The DB index keys on the member id
            # and backs the same-episode race.
            open_keys = set()
            for card in open_cards:
                open_keys.add((card.ticker, card.trade_def_slug, card.direction))
                # Same md5 first; else the same SLUG's current def (the note
                # was edited since formation — R2-4's catalyst batch), but
                # only when the edit left every formation field identical.
                ld = by_md5.get(card.trade_def_md5)
                changed: list[str] = []
                if ld is None and card.trade_def_slug in by_slug:
                    candidate = by_slug[card.trade_def_slug]
                    original, why = self._formation_definition(card, pool_key)
                    changed = [why] if original is None else formation_changes(original, candidate.definition)
                    ld = None if changed else candidate
                ev = ev_by.get((card.pool_member_id, ld.md5)) if ld is not None else None
                if ev is None or ld is None:
                    detail = f" ({'; '.join(changed)})" if changed else ""
                    outcome.refusals.append(
                        f"card {card.card_id}: its trade_def {card.trade_def_slug} (md5 {card.trade_def_md5}) "
                        f"is no longer loaded{detail} — not refreshed"
                    )
                    continue
                # Chronology: only i1 bars that opened after the formation
                # bar closed can touch the stop "before arm".
                formed_end = card.formed_at + timedelta(minutes=working_minutes(defaults))
                # R2-4.1 B: the avoid that expires a card is the CARD'S OWN
                # side's, never the published row's. The refresh reads only
                # frame-independent inputs (observations once on the real
                # bars, R2-4.2 B; last price; working bars; EMA9).
                own_side = ev.by_side[card.direction]
                expiry = radar_expiry(
                    state=_state(card.state), now=instant, expires_at=card.expires_at,
                    avoided=own_side.evaluation == "avoided", direction=card.direction, stop=card.stop,
                    bars_after_formation=[b for b in self._i1_closed(members, card) if b.ts >= formed_end],
                )
                update = refresh_card(card, ev, ld, settings, enabled, at=instant, thresholds=thresholds,
                                      run_id=run_id)
                update = update.model_copy(update={"radar_score_id": score_ids[(ev.membership_id, ev.md5)]})
                self.card_store.refresh_radar_card(update, now=instant, before_commit=gate("evaluate:card"))
                outcome.refreshed.append(card.card_id)
                if expiry is not None:
                    moved = self.card_store.expire_radar_card(
                        card.card_id, expiry, run_id=run_id, now=instant, before_commit=gate("evaluate:expire"),
                    )
                    if moved:
                        outcome.expired.append(card.card_id)
                copies.append({"score_id": update.radar_score_id, "proximity": update.proximity,
                               "conviction": update.conviction, "card_score": update.card_score,
                               "suppressed_reason": update.score_suppressed})
                receipt_cards.append(self._receipt_card(card, update, definition_md5=ld.md5))

            for ev in evaluations:
                if ev.evaluation != "formed" or ev.departed or ev.formation is None:
                    continue
                ld = by_md5[ev.md5]
                f = ev.formation
                if (ev.ticker, ld.slug, f.trade_direction) in open_keys:
                    continue
                if self.card_store.formation_consumed(ev.ticker, ld.slug, f.trade_direction, f.formed_bar_ts):
                    continue
                deadline = radar_deadline(ld.definition.preferred_windows_ref, trade_date)
                if instant > deadline.expires_at:
                    continue
                touched = radar_expiry(
                    state=_state("WATCH"), now=instant, expires_at=deadline.expires_at, avoided=False,
                    direction=f.trade_direction, stop=f.stop.price, bars_after_formation=list(ev.i1_after),
                )
                if touched is not None:
                    # An unclosed minute already prints through the stop over
                    # the tracked extreme: the run is still extending. No card
                    # this scan; the formation is NOT consumed and is
                    # re-evaluated next scan with the extreme where it lands.
                    continue
                fresh = card_dots(ld, ev, settings, instant, f.assumed_keys)
                score = score_card(fresh, last=ev.last_price, trigger=f.trigger.price, stop=f.stop.price,
                                   bands=settings.proposed_key, enabled=enabled)
                score_id = score_ids[(ev.membership_id, ev.md5)]
                spec = RadarCardSpec(
                    ticker=ev.ticker, direction=f.trade_direction, session=session, pool_member_id=ev.membership_id,
                    trade_def_slug=ld.slug, trade_def_md5=ld.md5, setup_ref=f.setup_ref,
                    trigger_type=ld.definition.trigger.type, trigger_price=f.trigger.price, stop_ref=f.stop_ref,
                    structural_stop=f.stop.price, formed_at=f.formed_bar_ts, expires_at=deadline.expires_at,
                    why=card_why(ld.definition, f), radar_score_id=score_id, scan_id=scan_id,
                    formula_sha256=formula_sha256(), tunables_sha256=canonical_sha256(tunables_snapshot),
                    settings_sha256=settings.sha256(), proximity=score.proximity, conviction=score.conviction,
                    card_score=score.card_score, score_suppressed=score.score_suppressed,
                    proposed_key=score.proposed_key.value if score.proposed_key else None, dots=fresh,
                    evidence={
                        "run_id": run_id, "scan_id": scan_id, "formation_bar_ts": f.formed_bar_ts.isoformat(),
                        "atoms": [a.model_dump(mode="json") for a in ev.detail.atoms],
                        "trigger": f.trigger.model_dump(mode="json"), "stop": f.stop.model_dump(mode="json"),
                        "extreme": f.extreme.model_dump(mode="json"),
                        "deadline": deadline.model_dump(mode="json"),
                    },
                )
                try:
                    card_id = self.card_store.create_radar_card(spec, now=instant, before_commit=gate("evaluate:create"))
                except Exception as e:
                    from .runner import StageDropped

                    if isinstance(e, StageDropped):
                        raise
                    outcome.refusals.append(f"{ev.ticker} {ld.slug}: card refused: {type(e).__name__}: {e}")
                    continue
                if card_id is None:
                    continue  # the database already holds an open card for this key
                open_keys.add((ev.ticker, ld.slug, f.trade_direction))
                outcome.created.append(card_id)
                update = CardUpdate(
                    card_id=card_id, proximity=score.proximity, conviction=score.conviction,
                    card_score=score.card_score, score_suppressed=score.score_suppressed,
                    proposed_key=spec.proposed_key, dots=fresh, health=None, radar_score_id=score_id,
                )
                copies.append({"score_id": score_id, "proximity": score.proximity, "conviction": score.conviction,
                               "card_score": score.card_score, "suppressed_reason": score.score_suppressed})
                receipt_cards.append({
                    "card_id": card_id, "pool_member_id": ev.membership_id, "trade_def_md5": ld.md5,
                    "definition_md5": ld.md5, "entry": str(spec.entry), "stop": str(spec.stop), "taps": [],
                    "assumed_keys": list(f.assumed_keys), "published": published_numbers(update),
                })
            if copies:
                self.radar_store.copy_card_values(copies, before_commit=gate("evaluate:copy"))

        built = build_receipt(
            self.chain, run_id=run_id, pool_key=pool_key, scan_id=scan_id, evaluated_at=instant,
            trade_date=trade_date, cohort=cohort, pool_unit=pool_unit, tunables_snapshot=tunables_snapshot,
            settings_snapshot=settings_snapshot, definitions_snapshot=definitions_snapshot, members=members,
            cards=receipt_cards, scan_interval=scan_interval,
        )
        receipt_id = self.card_store.write_receipt(built["row"], before_commit=gate("evaluate:receipt"))
        chain_commit(self.chain, receipt_id, built["staged"])
        self.radar_store.finish_run(run_id, status="complete", finished_at=self.now(), detail=None,
                                    before_commit=gate("evaluate:publish"))
        outcome.receipt_id = receipt_id
        return outcome

    def _formation_definition(self, card: OpenRadarCard, pool_key: str) -> tuple[TradeDef | None, str]:
        """The def a card formed under, by its formation md5, from the
        definitions snapshots of its formation day's receipts — the run
        that created the card stored it. An md5 names immutable content,
        so a found def is memoised for the process."""
        md5 = card.trade_def_md5
        if md5 in self._formation_defs:
            return self._formation_defs[md5], ""
        trade_date = self.clock.to_et(card.formed_at).date()
        for receipt in self.card_store.receipts_for_day(pool_key, trade_date):
            entry = receipt["definitions_snapshot"]
            if "value" not in entry:
                continue  # an unchanged pointer: its value sits in an earlier receipt of the day
            if canonical_sha256(entry["value"]) != entry["sha256"]:
                return None, f"receipt {receipt['id']} definitions snapshot does not hash to its sha256"
            for d in entry["value"]["defs"]:
                if d["md5"] == md5:
                    self._formation_defs[md5] = TradeDef.model_validate(d["definition"])
                    return self._formation_defs[md5], ""
        return None, f"its formation def is in no {pool_key} receipt of {trade_date.isoformat()}"

    @staticmethod
    def _i1_closed(members: list[MemberInput], card: OpenRadarCard) -> list[Bar]:
        for member in members:
            if member.membership_id == card.pool_member_id:
                return [b for b in member.bars if b.ts + timedelta(minutes=1) <= member.as_of]
        return []

    @staticmethod
    def _receipt_card(card: OpenRadarCard, update: CardUpdate, *, definition_md5: str) -> dict[str, Any]:
        return {
            "card_id": card.card_id, "pool_member_id": card.pool_member_id, "trade_def_md5": card.trade_def_md5,
            "definition_md5": definition_md5, "entry": str(card.entry), "stop": str(card.stop), "taps": card.taps,
            "assumed_keys": list(assumed_keys_of(update.dots)), "published": published_numbers(update),
        }


def _state(value: str):
    from cobalt.cards.models import CardState

    return CardState(value)


__all__ = [
    "ASSUMED_CONVENTIONS", "Anchor", "AtomValue", "CATALYST_REVIEW_FIELDS", "CONVENTION_LABELS", "CardUpdate",
    "EVALUATOR_VERSION", "SideOutcome", "assumed_closure", "closure_keys", "convention_refusals", "member_frames",
    "publish_frames",
    "EvaluateError", "EvaluateStage", "FACTOR_COMPUTERS", "Formation", "LoadedDef", "MemberEvaluation",
    "MemberInput", "OpenRadarCard", "ReceiptChain", "ReplayError", "ReplayedCard", "StageOutcome",
    "UNCLASSIFIED_SETUP", "assumed_keys_of", "build_receipt", "canonical_sha256", "card_dots",
    "card_why", "chain_commit", "desk_shadow", "evaluate_member", "evaluate_node", "formation_changes",
    "stop_on_protective_side",
    "formula_sha256", "overlay_taps",
    "published_numbers", "rebuild_members", "refresh_card", "replay_receipt", "seam_atom",
]
