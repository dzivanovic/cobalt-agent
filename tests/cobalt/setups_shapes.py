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

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
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
<!-- /cobalt:section definition -->
"""

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


def load_note(root: Path, slug: str, mapping: dict[str, Any], *, name: str | None = None) -> sup.LoadedDef:
    """Write ONE neutral note into `root` and load it through the real loader."""
    directory = root / STRATEGIES_DIR
    directory.mkdir(parents=True, exist_ok=True)
    body = yaml.safe_dump({"trade_def": mapping}, sort_keys=False).rstrip("\n")
    title = name or " ".join(part.capitalize() for part in slug.split("-"))
    (directory / f"{slug}.md").write_text(NOTE.format(slug=slug, name=title, body=body))
    result = load_vault_trade_defs(vault_root=root)
    assert result.drafts == [], result.drafts
    loaded = next(d for d in result.defs if d.slug == slug)
    return sup.LoadedDef(slug=loaded.slug, md5=loaded.md5, definition=loaded.definition)


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
        ld, member(ticker, at), tunables=tunables if tunables is not None else sup.engine_tunables(),
        defaults=sup.defaults(), scan_interval=100, clock=session_clock(),
    )


_SCANS: dict[tuple[str, str], list] = {}


def every_scan(ld: sup.LoadedDef, ticker: str) -> list:
    """One evaluation per two-minute scan across the whole RTH fixture day
    (computed once per (def slug, md5, ticker) — two notes with the same YAML
    body share an md5, the slug being frontmatter)."""
    key = (ld.slug, ld.md5, ticker)
    if key not in _SCANS:
        _SCANS[key] = [(DAY_START + timedelta(minutes=m), evaluate(ld, ticker, DAY_START + timedelta(minutes=m)))
                       for m in range(0, 391, 2)]
    return _SCANS[key]


@dataclass(frozen=True)
class Shape:
    """One setup's corpus shape: the neutral note slug, the mapping builder
    and the committed fixture tickers it is evaluated on."""

    note_slug: str
    mapping: Callable[[], dict[str, Any]]
    tickers: tuple[str, ...] = ("FTFT", "BGFI")
    notes: str = field(default="")


#: THE CORPUS — one neutral shape per setup, keyed by the setup's slug. It
#: grows step by step as each setup is unlocked.
SHAPES: dict[str, Shape] = {
    "rubberband": Shape(
        note_slug="shape-extension-reversal",
        mapping=lambda: rubberband_mapping(MIXED, htf_avoid=True),
        notes="4 countertrend + 1 with_trend setup refs; the day-1 HTF avoid; a human text avoid",
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
    return load_note(root, shape.note_slug, shape.mapping())
