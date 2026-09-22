"""The setups fix, round 2 (prompt `15-setups-fix.md`) — the FIX rows' tests.

- F1: a def whose preconditions name no anchor object is NOT evaluable,
  named `anchor:none` (the registry reads `ANCHORS`, the table formation
  dispatches through — L3).

Neutral defs of this file's own words and literals (L32 / L69), written into
a `tmp_path` vault and loaded through the real `load_vault_trade_defs`
(`setups_shapes.load_note`). Bars, daily bars and settings are the committed
real-shape radar fixtures (L45).
"""

from __future__ import annotations

from datetime import timedelta

import pytest

import radar_p2_support as sup
import setups_shapes as shapes
from cobalt.radar.anatomy.registry import evaluability

# =====================================================================
# F1 — anchors: `evaluability` names `anchor:none`
# =====================================================================


def _indicator_stop(indicator: str) -> dict:
    return {"type": "indicator", "indicator": indicator,
            "buffer": {"type": "fixed", "cents": {"value": "cfg(stop.buffer)", "dynamic": False}},
            "snapshot": "at_entry"}


def no_anchor_mapping() -> dict:
    """Existing bricks only, and no anchor object among them: the pool
    admission, price above the VWAP and above the EMA21; a 4-bar `bar_break`;
    the VWAP stop at entry."""
    mapping = shapes.example_mapping()
    mapping.update(
        valid_setups=[{"setup_ref": "range_break", "relation": "with_trend"}],
        preconditions=[{"expr": "InPlay.state == active"}, {"expr": "price > VWAP"}, {"expr": "price > EMA21"}],
        avoid=[{"text": "a human read, this file's words"}],
        trigger={"type": "bar_break", "params": {"bars_cleared": 4, "direction": "any"},
                 "confirmation_policy": {"type": "intrabar"}},
        quality_factors=sup.ANATOMY_FACTORS, preferred_windows=["morning"],
        preferred_windows_ref="anatomy: above both lines",
    )
    mapping.pop("radar_watch", None)
    mapping["stop"]["placement"] = _indicator_stop("VWAP")
    return mapping


@pytest.fixture(scope="module")
def no_anchor(tmp_path_factory):
    return shapes.load_note(tmp_path_factory.mktemp("no-anchor"), "example-fix-no-anchor", no_anchor_mapping())


def test_f1_a_def_with_no_anchor_object_is_not_evaluable_named_anchor_none(no_anchor):
    result = evaluability(no_anchor.definition)
    assert result.evaluable is False
    assert result.missing_atoms == ("anchor:none",)


def test_f1_evaluate_member_reports_not_evaluable_naming_anchor_none_on_the_committed_day(no_anchor):
    for m in range(0, 391, 30):
        ev = shapes.evaluate(no_anchor, "FTFT", shapes.DAY_START + timedelta(minutes=m))
        assert ev.evaluation == "not_evaluable" and "anchor:none" in ev.missing, (m, ev.evaluation, ev.note)
