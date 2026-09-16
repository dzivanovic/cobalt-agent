"""S2-P2 STEP-1 amendment (Astra R1-1): the system seam payload is closed.

`system.radar_score.detail` / `desk_shadow` may carry generic atom names,
symbols, numeric observations and numeric shadow grades — never authored
predicate text, a trade's resolved thresholds, a WHY sentence or trader
settings content (those stay user-side, L32).
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from decimal import Decimal

import pytest
from pydantic import ValidationError

from cobalt.db import Side
from cobalt.radar.seam import (
    AtomOutcome,
    DeskShadow,
    DeskShadowEntry,
    RadarScoreDetail,
    SeamObservation,
)
from cobalt.taxonomy.loader import EXAMPLE_NOTE_PATH
from cobalt.taxonomy.vault_loader import STRATEGIES_DIR, load_vault_trade_defs

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)

AT = datetime(2026, 1, 6, 15, 0, tzinfo=timezone.utc)


def _detail(**overrides) -> RadarScoreDetail:
    values = dict(
        atoms=(
            AtomOutcome(atom="Extension.state", value_kind="symbol", symbol="culminating"),
            AtomOutcome(atom="RangeBreak(HTF).day_count", value_kind="number", number=Decimal("2")),
            AtomOutcome(atom="Extension.instantiated", value_kind="boolean", boolean=True),
        ),
        missing_atoms=(),
        observations=(
            SeamObservation(name="atr_working_tf", value=Decimal("0.123456"), bar_ts=AT),
        ),
        extension_path="A",
        formed_bar_ts=AT,
    )
    values.update(overrides)
    return RadarScoreDetail(**values)


def _desk() -> DeskShadow:
    na = DeskShadowEntry(grade=None, na_reason="DESK_NA", why_code="desk_not_run", formula_version="p2.0")
    return DeskShadow(catalyst=na, market_alignment=na, sector_alignment=na)


def test_a_generic_detail_and_desk_shadow_validate_and_round_trip():
    detail = _detail()
    assert RadarScoreDetail.model_validate_json(detail.model_dump_json()) == detail
    desk = _desk()
    assert DeskShadow.model_validate_json(desk.model_dump_json()) == desk


@pytest.mark.parametrize(
    "overrides",
    [
        {"why": "fresh negative news against"},
        {"expr": "Extension.state == culminating"},
        {"thresholds": {"bars_cleared": 2}},
    ],
)
def test_unknown_keys_are_refused(overrides):
    with pytest.raises(ValidationError):
        RadarScoreDetail(**{**_detail().model_dump(), **overrides})


@pytest.mark.parametrize(
    "atom",
    [
        "Range(micro).duration IN cfg(example_range_break.range_duration_band) min",
        "cfg(example_range_break.range_duration_band)",
        'Level_ref("my personal level")',
        "fresh negative news against",
    ],
)
def test_an_atom_must_be_a_bare_reference_without_cfg_or_prose(atom):
    with pytest.raises(ValidationError):
        AtomOutcome(atom=atom, value_kind="boolean", boolean=True)


def test_a_symbol_is_one_lowercase_word_and_observation_names_are_identifiers():
    with pytest.raises(ValidationError):
        AtomOutcome(atom="Extension.state", value_kind="symbol", symbol="culminating hard")
    with pytest.raises(ValidationError):
        SeamObservation(name="the trader's stop", value=Decimal("1"), bar_ts=AT)


def test_desk_shadow_grade_bounds_and_na_reasons_are_closed():
    with pytest.raises(ValidationError):
        DeskShadowEntry(grade=11, na_reason=None, why_code="x", formula_version="p2.0")
    with pytest.raises(ValidationError):
        DeskShadowEntry(grade=None, na_reason="because I said so", why_code="x", formula_version="p2.0")
    with pytest.raises(ValidationError):
        DeskShadowEntry(grade=5, na_reason="DESK_NA", why_code="x", formula_version="p2.0")


def test_radar_score_carries_no_trade_def_content(tmp_path):
    """md5 only: nothing from the def's prose, identity or tunables can be
    expressed in a valid payload built from its own atoms."""
    strategies = tmp_path / STRATEGIES_DIR
    strategies.mkdir(parents=True)
    (strategies / "Example Range Break.md").write_text(EXAMPLE_NOTE_PATH.read_text())
    loaded = load_vault_trade_defs(vault_root=tmp_path)
    (item,) = loaded.defs
    td = item.definition
    atoms = sorted({a for p in [*td.preconditions, *td.avoid] for a in p.required_atoms})
    detail = _detail(
        atoms=tuple(AtomOutcome(atom=a, value_kind="boolean", boolean=True) for a in atoms),
        missing_atoms=tuple(atoms),
    )
    blob = detail.model_dump_json() + _desk().model_dump_json()
    forbidden = [item.slug, item.name, *td.aliases, "example_range_break", "cfg(",
                 td.preferred_windows_ref or "", *(p.text for p in td.preconditions if p.text)]
    for needle in filter(None, forbidden):
        assert needle not in blob, needle


@requires_db
def test_no_system_side_row_contains_trade_def_or_settings_content(real_connect):
    """Hub, cobalt_dev: every stored seam payload against every loaded
    def's slug/name/aliases and every trader_settings key."""
    conn = real_connect(side=Side.USER)
    defs = conn.execute('SELECT slug, def FROM "user".trade_defs').fetchall()
    keys = [r[0] for r in conn.execute('SELECT key FROM "user".trader_settings').fetchall()]
    payloads = conn.execute(
        "SELECT id, detail::text || desk_shadow::text FROM system.radar_score"
    ).fetchall()
    needles = set(keys)
    for slug, definition in defs:
        body = definition if isinstance(definition, dict) else json.loads(definition)
        needles.add(slug)
        needles.update(body.get("aliases") or [])
        if body.get("preferred_windows_ref"):
            needles.add(body["preferred_windows_ref"])
    for row_id, text in payloads:
        for needle in needles:
            assert needle not in text, (row_id, needle)
