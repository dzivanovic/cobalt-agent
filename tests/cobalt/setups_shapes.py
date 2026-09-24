"""Neutral shape notes for the setups one build (support, not a test module).

Adapted from the proof's helpers (`tests/cobalt/test_rubberband_card_proof.py`
on the unmerged proof branch `s2/rubberband-proof-0921`: `NOTE`, `_mapping`,
`load_through_the_real_loader`, `every_scan`) — not the proof file itself.

REAL SHAPE, NO USER DATA (L32, L45, L69). Each note is written into a
`tmp_path` vault in the real strategy-note layout and loaded through the
real `load_vault_trade_defs`. A note mirrors a definition's SHAPE only —
which atoms, relation words, trigger type, stop placement and avoids it
uses — with anatomy vocabulary and literals of this file's own choosing
(`bars_cleared`, buffers, bands). No value, wording or comment of a
strategy note is copied; the note slugs are this file's own.

Bars, daily bars and settings are the committed real-shape radar
fixtures (`tests/fixtures/radar/`): ONE trade date, tickers FTFT (forms)
and BGFI (stale by design).
"""

from __future__ import annotations

import tempfile
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable

import yaml

import radar_p2_support as sup
from cobalt.radar.anatomy.freshness import RvolObservation
from cobalt.radar.evaluate import MemberInput, evaluate_member
from cobalt.session import session_clock
from cobalt.taxonomy.loader import EXAMPLE_NOTE_PATH
from cobalt.taxonomy.vault_loader import STRATEGIES_DIR, load_vault_trade_defs

UTC = timezone.utc
#: The scan the proof's test A reads: the FTFT Extension culminated (path A,
#: up-run) on the 16:22 UTC working bar.
SCAN0 = datetime(2026, 1, 6, 16, 30, tzinfo=UTC)
DAY_START = datetime(2026, 1, 6, 14, 30, tzinfo=UTC)

NOTE = """---
trade_def: {slug}
name: {name}
class: scalp
family: [range_break]
status: defined
---
## Definition
<!-- cobalt:section definition -->
<!-- cobalt:unit trade_def:{slug} -->
```yaml
{body}
```
<!-- /cobalt:unit trade_def:{slug} -->
{tunables}<!-- /cobalt:section definition -->
"""

TUNABLES_UNIT = """<!-- cobalt:unit tunables:{slug} -->
```yaml
{body}
```
<!-- /cobalt:unit tunables:{slug} -->
"""

#: This build's OWN constructed values for the engine holes of STEP-4's
#: detectors (L69: literals of this file's choosing, never a value of his or
#: of the assumed-values companion). A shape that names these atoms evaluates
#: with them; committed config keeps the rows null.
D2_CONSTRUCTED: dict[str, tuple[str, str]] = {
    "range.micro.touch_tolerance_atr": ("atr", "0.3"),
    "range.micro.bound_flat_slope_atr": ("atr", "0.2"),
    "leg.consolidation_max_retrace": ("ratio", "0.6"),
    "range.wick_ratio_max": ("ratio", "0.8"),
}

#: The relation MIX of the rubberband definition's shape: four countertrend
#: refs and one with_trend ref, in the schema's own `SetupRef` vocabulary.
MIXED = [
    {"setup_ref": "gap_down_into_support", "relation": "countertrend"},
    {"setup_ref": "gap_up_into_resistance", "relation": "countertrend"},
    {"setup_ref": "day2_continuation", "relation": "with_trend"},
    {"setup_ref": "overextension", "relation": "countertrend"},
    {"setup_ref": "volatility_in_range", "relation": "countertrend"},
]
COUNTERTREND_ONLY = [{"setup_ref": "overextension", "relation": "countertrend"}]
WITH_TREND_ONLY = [{"setup_ref": "overextension", "relation": "with_trend"}]
HTF_AVOID = {"expr": "RangeBreak(HTF).day_count == 1"}


def example_mapping() -> dict[str, Any]:
    """The shipped synthetic example's `trade_def` mapping (the base every
    neutral shape edits)."""
    text = EXAMPLE_NOTE_PATH.read_text()
    return yaml.safe_load(text.split("```yaml\n", 1)[1].split("\n```", 1)[0])["trade_def"]


def rubberband_mapping(valid_setups: list[dict], *, htf_avoid: bool) -> dict[str, Any]:
    """The Extension-reversal SHAPE: culminating Extension precondition, the
    not-instantiated avoid, the optional day-1 HTF avoid, a human text avoid,
    a `bar_break` trigger and the tracked-extreme stop. `bars_cleared` is a
    literal of this file's choosing."""
    mapping = example_mapping()
    mapping.update(
        valid_setups=valid_setups,
        tf_ceiling=15,
        entry_mode="front_side",
        preconditions=[{"expr": "Extension.state == culminating"}],
        avoid=[
            {"expr": "NOT Extension.instantiated"},
            *([HTF_AVOID] if htf_avoid else []),
            {"text": "human-only context read"},
        ],
        trigger={"type": "bar_break", "params": {"bars_cleared": 2, "direction": "any"},
                 "confirmation_policy": {"type": "intrabar"}},
        quality_factors=sup.ANATOMY_FACTORS,
        preferred_windows=["morning", "midday"],
        preferred_windows_ref="anatomy: 09:45-15:30",
    )
    mapping["stop"]["placement"]["ref"] = "snapback_candle"
    return mapping


#: The user rows each loaded neutral note carries (its own tunables unit), and
#: the constructed engine fills its shape declares — by def slug.
_USER_ROWS: dict[str, dict] = {}
_ENGINE_FILLS: dict[str, dict[str, tuple[str, str]]] = {}


def load_note(root: Path, slug: str, mapping: dict[str, Any], *, name: str | None = None,
              rows: list[dict] | None = None, engine: dict[str, tuple[str, str]] | None = None) -> sup.LoadedDef:
    """Write ONE neutral note into `root` and load it through the real loader.
    `rows` become the note's own tunables unit (per-trade keys)."""
    directory = root / STRATEGIES_DIR
    directory.mkdir(parents=True, exist_ok=True)
    body = yaml.safe_dump({"trade_def": mapping}, sort_keys=False).rstrip("\n")
    unit = "" if not rows else TUNABLES_UNIT.format(
        slug=slug, body=yaml.safe_dump({"tunables": rows}, sort_keys=False).rstrip("\n"))
    title = name or " ".join(part.capitalize() for part in slug.split("-"))
    (directory / f"{slug}.md").write_text(NOTE.format(slug=slug, name=title, body=body, tunables=unit))
    result = load_vault_trade_defs(vault_root=root)
    assert result.drafts == [], result.drafts
    loaded = next(d for d in result.defs if d.slug == slug)
    _USER_ROWS[slug] = {t.key: t.row for t in result.user_tunables if t.slug == slug}
    if engine:
        _ENGINE_FILLS[slug] = dict(engine)
    return sup.LoadedDef(slug=loaded.slug, md5=loaded.md5, definition=loaded.definition)


def user_rows(ld: sup.LoadedDef) -> dict:
    return dict(_USER_ROWS.get(ld.slug, {}))


def tunables_for(ld: sup.LoadedDef) -> dict:
    """What the stage would merge for this def: the committed engine rows,
    the shape's constructed fills of engine holes (L69), the note's own rows."""
    from cobalt.taxonomy.tunables import TunableRow

    rows = dict(sup.engine_tunables())
    for key, (unit, value) in _ENGINE_FILLS.get(ld.slug, {}).items():
        filled = Decimal(value)
        rows[key] = rows[key].model_copy(update={"value": filled}) if key in rows else TunableRow(
            key=key, value=filled, unit=unit, scope="global", dynamic=True, status="proposed", source="dwv",
            consumers=["constructed"])
    return {**rows, **user_rows(ld)}


@lru_cache(maxsize=None)
def bars(ticker: str) -> tuple:
    return tuple(sup.fixture_bars(ticker))


def member(ticker: str, at: datetime) -> MemberInput:
    return MemberInput(
        membership_id=100, ticker=ticker, trade_date=sup.TRADE_DATE, as_of=at,
        bars=bars(ticker), daily=sup.fixture_daily(ticker, at), daily_status="cache-hit",
        rvol=RvolObservation(ticker=ticker, value=4.2, observed_at=at, source="screen:s", candidates=("screen:s",)),
    )


def evaluate(ld: sup.LoadedDef, ticker: str, at: datetime, *, tunables=None):
    return evaluate_member(
        ld, member(ticker, at), tunables=tunables if tunables is not None else tunables_for(ld),
        defaults=sup.defaults(), scan_interval=100, clock=session_clock(),
    )


_SCANS: dict[tuple[str, str], list] = {}


def _grid(ld: sup.LoadedDef, ticker: str, tunables=None) -> list:
    return [(DAY_START + timedelta(minutes=m),
             evaluate(ld, ticker, DAY_START + timedelta(minutes=m), tunables=tunables))
            for m in range(0, 391, 2)]


def every_scan(ld: sup.LoadedDef, ticker: str, *, tunables=None) -> list:
    """One evaluation per two-minute scan across the whole RTH fixture day
    (computed once per (def slug, md5, ticker) — two notes with the same YAML
    body share an md5, the slug being frontmatter). `tunables` given (a live
    def's merged rows): evaluated with them, never cached."""
    if tunables is not None:
        return _grid(ld, ticker, tunables)
    key = (ld.slug, ld.md5, ticker)
    if key not in _SCANS:
        _SCANS[key] = _grid(ld, ticker)
    return _SCANS[key]


@dataclass(frozen=True)
class Shape:
    """One setup's corpus shape: the neutral note slug, the mapping builder
    and the committed fixture tickers it is evaluated on."""

    note_slug: str
    mapping: Callable[[], dict[str, Any]]
    tickers: tuple[str, ...] = ("FTFT", "BGFI")
    notes: str = field(default="")
    #: The note's own per-trade tunable rows (its tunables unit).
    rows: Callable[[], list[dict]] = field(default=lambda: [])
    #: Constructed values for the ENGINE holes its atoms read (L69).
    engine: dict[str, tuple[str, str]] = field(default_factory=dict)


def drive_then_range_mapping() -> dict[str, Any]:
    """The drive-then-range SHAPE (hitchhiker's): the pool admission, an
    opening drive terminated by consolidation, an instantiated micro-Range
    whose duration sits in a per-trade band and whose low is in the day's
    upper third; the `range_break` trigger on the trade-side bound; the
    `consolidation_low` stop; the pullback-termination and wick-ratio avoids
    and a human text avoid. The band and every threshold are this file's."""
    mapping = example_mapping()
    mapping.update(
        valid_setups=[{"setup_ref": "range_break", "relation": "with_trend"},
                      {"setup_ref": "volatility_in_range", "relation": "with_trend"}],
        preconditions=[
            {"expr": "InPlay.state == active"},
            {"expr": "Leg(opening_drive).terminated_by == consolidation"},
            {"expr": "Range(micro).instantiated"},
            {"expr": "Range(micro).duration IN cfg(example_drive_then_range.range_duration_band) min"},
            {"expr": "Range(micro).low >= DayRange.upper_third"},
        ],
        trigger={"type": "range_break", "params": {"ref": "Range(micro).bound"},
                 "confirmation_policy": {"type": "intrabar"}},
        avoid=[
            {"expr": "Leg(opening_drive).terminated_by == pullback"},
            {"expr": "Range(micro).wick_ratio > cfg(range.wick_ratio_max)"},
            {"text": "human-only read of the consolidation"},
        ],
        quality_factors=sup.ANATOMY_FACTORS,
        preferred_windows=["morning"],
        preferred_windows_ref="anatomy: after the opening drive",
    )
    mapping.pop("radar_watch", None)
    mapping["stop"]["placement"]["ref"] = "consolidation_low"
    return mapping


#: STEP-5's constructed fills (L69; none a value of his or of the companion):
#: the snapback count (`A-08`), the slope window (`A-11`), the two
#: `per_indicator` flat thresholds (F1 — filled HERE only; production keeps them
#: null), and the D2 fills the backside shape's micro-Range needs.
D4_CONSTRUCTED: dict[str, tuple[str, str]] = {
    **D2_CONSTRUCTED,
    "extension.snapback_bars_cleared": ("bars", "3"),
    "slope_norm.bars": ("bars", "4"),
    "flat_threshold.ema9": ("ratio", "0.08"),
    "flat_threshold.vwap": ("ratio", "0.09"),
}


def backside_mapping() -> dict[str, Any]:
    """The backside SHAPE: an unqualified Extension in its `backside` state; an
    instantiated micro-Range whose low is above the EMA9, the EMA9 rising;
    `range_break` on the top; the `recent_higher_low` stop; the day-1 HTF avoid
    and a human text avoid."""
    mapping = example_mapping()
    mapping.update(
        valid_setups=MIXED, entry_mode="front_side",
        preconditions=[
            {"expr": "Extension.state == backside"},
            {"expr": "Range(micro).instantiated AND Range(micro).low > EMA9 AND EMA9.slope > 0"},
        ],
        trigger={"type": "range_break", "params": {"ref": "Range(micro).top"},
                 "confirmation_policy": {"type": "intrabar"}},
        avoid=[HTF_AVOID, {"text": "human-only read of the backside"}],
        quality_factors=sup.ANATOMY_FACTORS, preferred_windows=["morning", "midday"],
        preferred_windows_ref="anatomy: after the turn",
    )
    mapping.pop("radar_watch", None)
    mapping["stop"]["placement"]["ref"] = "recent_higher_low"
    return mapping


def late_mapping() -> dict[str, Any]:
    """The fashionably-late SHAPE: an unqualified Extension reverting or on its
    backside; the EMA9 sloping while the VWAP is flat or falling; the EMA9
    crossing above the VWAP; a measured-fraction stop between the entry and
    the turn; the flat-EMA9-between-turn-and-cross avoid and a human text avoid.
    The fraction is this file's literal."""
    mapping = example_mapping()
    mapping.update(
        valid_setups=MIXED, entry_mode="front_side",
        preconditions=[
            {"expr": "Extension.state IN {reverting, backside}"},
            {"expr": "slope_norm(EMA9) > cfg(flat_threshold.ema9) AND slope_norm(VWAP) <= cfg(flat_threshold.vwap)"},
        ],
        trigger={"type": "indicator_cross", "params": {"a": "EMA9", "b": "VWAP", "direction": "a_crosses_above_b"},
                 "confirmation_policy": {"type": "intrabar"}},
        avoid=[{"expr": "flat(EMA9, window: 15 min / working_tf) between turn and cross"},
               {"text": "human-only read of the cross"}],
        quality_factors=sup.ANATOMY_FACTORS, preferred_windows=["morning", "midday"],
        preferred_windows_ref="anatomy: after the turn",
    )
    mapping.pop("radar_watch", None)
    mapping["stop"]["placement"] = {"type": "measured_fraction", "anchor_a": "entry", "anchor_b": "turn_low",
                                    "fraction": 0.4}
    return mapping


def pullback_to_ema_mapping() -> dict[str, Any]:
    """The pullback-to-EMA9 SHAPE (nine-ema-scalp's): the pool admission; the
    catalyst read (`catalyst_ref`, served by `A-13`); the morning move with the
    trade; a pullback that touches the EMA9 while price holds above the EMA21;
    the EMA9 rejection trigger; the EMA21 stop at entry; the too-big-a-move-
    before-the-test avoid and a human text avoid."""
    mapping = example_mapping()
    mapping.update(
        valid_setups=[{"setup_ref": "range_break", "relation": "with_trend"},
                      {"setup_ref": "volatility_in_range", "relation": "with_trend"}],
        preconditions=[
            {"expr": "InPlay.state == active"},
            {"expr": "catalyst_ref != null"},
            {"expr": "Leg(opening_drive OR impulse).direction == trade_direction"},
            {"expr": "Leg(pullback) touched EMA9 AND price > EMA21"},
        ],
        trigger={"type": "indicator_rejection", "params": {"indicator": "EMA9", "contact": ["touch", "penetrate"]},
                 "confirmation_policy": {"type": "close_through"}},
        avoid=[{"expr": "Extension.instantiated on Leg(pre_test)"}, {"text": "human-only read of the bids"}],
        quality_factors=sup.ANATOMY_FACTORS, preferred_windows=["morning"],
        preferred_windows_ref="anatomy: the pullback after the morning move",
    )
    mapping.pop("radar_watch", None)
    mapping["stop"]["placement"] = {"type": "indicator", "indicator": "EMA21",
                                    "buffer": {"type": "fixed", "cents": {"value": "cfg(stop.buffer)",
                                                                          "dynamic": False}},
                                    "snapshot": "at_entry"}
    return mapping


def pullback_to_vwap_mapping() -> dict[str, Any]:
    """The pullback-to-VWAP continuation SHAPE: the pool admission; the morning
    move with the trade; a pullback against it that ends near the VWAP (within
    `cfg(dist.k.vwap)` ATR); the trendline break of the pullback (flat case: the
    micro-Range top); the VWAP stop at entry; the rejected-resistance avoid and
    a human text avoid."""
    mapping = example_mapping()
    mapping.update(
        valid_setups=[{"setup_ref": "range_break", "relation": "with_trend"},
                      {"setup_ref": "volatility_in_range", "relation": "with_trend"}],
        preconditions=[
            {"expr": "InPlay.state == active"},
            {"expr": "Leg(opening_drive OR impulse).direction == trade_direction"},
            {"expr": "Leg(pullback).direction == opposite(trade_direction) AND "
                     "dist(Leg(pullback).end, VWAP) <= cfg(dist.k.vwap) * ATR(working_tf)"},
        ],
        trigger={"type": "trendline_break",
                 "params": {"ref": "Level_ref(trendline)", "anchor_leg": "Leg(pullback)",
                            "pivots": "cfg(trendline.min_pivots)"},
                 "confirmation_policy": {"type": "intrabar"}},
        avoid=[{"text": "human-only read of the open"}, {"expr": "Level_ref(resistance).rejected"}],
        quality_factors=sup.ANATOMY_FACTORS, preferred_windows=["morning", "midday"],
        preferred_windows_ref="anatomy: after the morning move",
    )
    mapping.pop("radar_watch", None)
    mapping["stop"]["placement"] = {"type": "indicator", "indicator": "VWAP",
                                    "buffer": {"type": "fixed", "cents": {"value": "cfg(stop.buffer)",
                                                                          "dynamic": False}},
                                    "snapshot": "at_entry"}
    return mapping


def break_retest_turn_mapping() -> dict[str, Any]:
    """The break-retest-turn SHAPE (second-chance's): a level break accepted,
    and a retest of THAT break; the `sequence` trigger (break close-through →
    retest → a close above the prior bar); the `turn_candle` stop; the
    failed-trap-after-retest and stop-hit-back-inside avoids."""
    mapping = example_mapping()
    mapping.update(
        valid_setups=[{"setup_ref": "range_break", "relation": "with_trend"},
                      {"setup_ref": "volatility_in_range", "relation": "with_trend"}],
        preconditions=[{"expr": "RangeBreak(level).state == accepted"},
                       {"expr": "event(retest) on that RangeBreak"}],
        trigger={"type": "sequence", "steps": [
            {"name": "break", "predicate": {"expr": "price close_through Level_ref"},
             "confirmation_policy": {"type": "close_through"}},
            {"name": "retest", "predicate": {"expr": "event(retest)"}},
            {"name": "turn", "predicate": {"expr": "close_above(prior_bar)"},
             "confirmation_policy": {"type": "close_through"}},
        ]},
        avoid=[{"expr": "RangeBreak.state == failed_trap after event(retest)"},
               {"expr": "event(stop_hit) AND price inside Range(prior)"}],
        quality_factors=sup.ANATOMY_FACTORS, preferred_windows=["morning", "midday"],
        preferred_windows_ref="anatomy: after the break",
    )
    mapping.pop("radar_watch", None)
    mapping["stop"]["placement"]["ref"] = "turn_candle"
    return mapping


#: STEP-7: + the `per_indicator` distance hole (F1 — filled HERE only).
D5_CONSTRUCTED: dict[str, tuple[str, str]] = {**D4_CONSTRUCTED, "dist.k.vwap": ("atr", "1.7")}
#: STEP-8: the failed-trap window (`A-19`) and the retest tolerance (`A-20`).
D6_CONSTRUCTED: dict[str, tuple[str, str]] = {**D5_CONSTRUCTED, "range_break.failed_trap_bars": ("bars", "3"),
                                              "range_break.retest_tolerance_atr": ("atr", "0.35")}


def drive_then_range_rows() -> list[dict]:
    # L31 / ADR-0008 D5 (`tests/taxonomy/test_names_rule.py`): a per-trade key
    # in the repo is an `example_` key — the note slug is `example-…` for it.
    return [{"key": "example_drive_then_range.range_duration_band", "value": [5, 30], "unit": "min",
             "scope": "per_trade(example_drive_then_range)", "dynamic": True, "status": "proposed",
             "source": "ruling", "consumers": ["preconditions: Range(micro).duration band"]}]


#: THE CORPUS — one neutral shape per setup, keyed by the setup's slug. It
#: grows step by step as each setup is unlocked.
SHAPES: dict[str, Shape] = {
    "rubberband": Shape(
        note_slug="shape-extension-reversal",
        mapping=lambda: rubberband_mapping(MIXED, htf_avoid=True),
        notes="4 countertrend + 1 with_trend setup refs; the day-1 HTF avoid; a human text avoid",
    ),
    "hitchhiker": Shape(
        note_slug="example-drive-then-range",
        mapping=drive_then_range_mapping,
        rows=drive_then_range_rows,
        engine=D2_CONSTRUCTED,
        notes="pool admission, opening drive ended by consolidation, micro-Range band + upper third; "
              "range_break on the bound, consolidation_low; two avoids + a human text avoid",
    ),
    "backside": Shape(
        note_slug="example-extension-backside",
        mapping=backside_mapping,
        engine=D4_CONSTRUCTED,
        notes="Extension backside + micro-Range above a rising EMA9; range_break top; recent_higher_low; "
              "day-1 HTF avoid + a human text avoid",
    ),
    "fashionably-late": Shape(
        note_slug="example-extension-late-cross",
        mapping=late_mapping,
        engine=D4_CONSTRUCTED,
        notes="Extension reverting/backside + EMA9 sloping, VWAP flat; EMA9 crosses above VWAP; "
              "measured_fraction(entry, turn_low); flat-between avoid + a human text avoid",
    ),
    "nine-ema-scalp": Shape(
        note_slug="example-pullback-to-ema",
        mapping=pullback_to_ema_mapping,
        engine=D4_CONSTRUCTED,
        notes="pool admission + catalyst_ref (A-13); morning move with the trade; pullback touches EMA9 above "
              "EMA21; indicator_rejection EMA9; indicator stop EMA21 at_entry; Extension-on-pre_test avoid",
    ),
    "vwap-continuation": Shape(
        note_slug="example-pullback-to-vwap",
        mapping=pullback_to_vwap_mapping,
        engine=D5_CONSTRUCTED,
        notes="pool admission; morning move with the trade; pullback near VWAP by dist/ATR; trendline_break "
              "(flat case: micro-Range top); indicator stop VWAP at_entry; rejected-resistance avoid",
    ),
    "second-chance": Shape(
        note_slug="example-break-retest-turn",
        mapping=break_retest_turn_mapping,
        engine=D6_CONSTRUCTED,
        notes="RangeBreak(level) accepted + retest on that RangeBreak; sequence break→retest→turn; turn_candle "
              "stop; failed-trap-after-retest and stop-hit-inside-prior avoids",
    ),
}

#: Evaluable shapes that are not a setup's full corpus shape but must form on
#: the committed day (the relation path of the rubberband shape WITHOUT its
#: day-1 HTF avoid — the proof's test A shape).
VARIANTS: dict[str, Shape] = {
    "rubberband-without-htf-avoid": Shape(
        note_slug="shape-extension-reversal-mixed",
        mapping=lambda: rubberband_mapping(MIXED, htf_avoid=False),
        tickers=("FTFT",),
    ),
}


def load_shape(root: Path, shape: Shape) -> sup.LoadedDef:
    return load_note(root, shape.note_slug, shape.mapping(), rows=shape.rows(), engine=shape.engine)


@lru_cache(maxsize=None)
def load_shape_fresh(key: str) -> sup.LoadedDef:
    """A corpus shape loaded into its own temporary vault (once per session)."""
    return load_shape(Path(tempfile.mkdtemp(prefix=f"shape-{key}-")), {**SHAPES, **VARIANTS}[key])
