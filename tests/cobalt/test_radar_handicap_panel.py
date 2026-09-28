"""Float handicap H1 STEP-7 — `/radar`: the pool-row badge and the header
state (v3 §4; X6). Offline, `test_radar_panel.py`'s pattern. The three
handicap fields are this file's CONSTRUCTED values set on the committed
real-shape rows (the 800-row `panel-pool.real-shape.json` itself is not
rewritten — ESCALATED in the H1 build report)."""

from __future__ import annotations

import re
from decimal import Decimal

import pytest
from test_radar_panel import (
    NOW, FakeClock, FakeRadarStore, FakeSettingsStore, _block_values, _small_snapshot, _tunables,
)

from cobalt.aset import radar_panel as panel

RECORD = {
    "float_m": "5.1", "market_cap_m": "88.2", "verdict": "yes", "reason": "float and cap",
    "missing_rule": "apply", "mode": "shadow", "position": 3, "effective_position": 7,
    "source": "screen:x@000000000000", "block_sha256": "0" * 64,
}
BLOCK = {"float_below_m": "20", "market_cap_below_m": "300", "factor": "0.8", "missing": "apply",
         "mode": "shadow", "combinator": "any"}


def _settings(handicap=None):
    values = _block_values()
    if handicap is not None:
        values["radar.pool"]["block"]["handicap"] = handicap
    return values


def _view(members_update=None, pool_update=None, handicap=BLOCK):
    pool_row, members = _small_snapshot()
    if members_update:
        members[0].update(members_update)
    if pool_update:
        pool_row.update(pool_update)
    view = panel.build_pool_view(
        since=None, snapshot=True, radar_store=FakeRadarStore(pool_row, members),
        settings_store=FakeSettingsStore(_settings(handicap)), clock=FakeClock(), now=NOW,
        tunables_loader=_tunables(),
    )
    return view, panel.render_pool(view)


def _row_html(rendered: str, episode_id: int) -> str:
    return re.search(rf'<tr data-episode-id="{episode_id}"[^>]*>(.*?)</tr>', rendered, re.S).group(1)


def test_a_handicapped_row_shows_the_shadow_badge_and_its_line():
    view, rendered = _view({"handicap_factor": Decimal("0.8000"), "handicap": RECORD})
    row = view.current[0]
    cell = _row_html(rendered, row.episode_id)
    assert '<span class="badge badge-cobalt" title="owner COBALT">HANDICAP (shadow)</span>' in cell
    assert "float 5.1M / cap $88.2M → group (float and cap) · pos 3 → 7" in cell


@pytest.mark.parametrize("factor,record", [
    (None, None),
    (Decimal("1.0000"), {**RECORD, "verdict": "no", "reason": "neither", "effective_position": 3}),
])
def test_factor_one_or_null_renders_no_badge_and_no_line(factor, record):
    view, rendered = _view({"handicap_factor": factor, "handicap": record})
    cell = _row_html(rendered, view.current[0].episode_id)
    assert "HANDICAP" not in cell and "→ group" not in cell


def test_unknown_not_applied_renders_its_line_and_no_badge():
    record = {**RECORD, "float_m": None, "market_cap_m": None, "verdict": "unknown",
              "reason": "blank float and cap — unknown → not applied", "missing_rule": "skip",
              "effective_position": 3}
    view, rendered = _view({"handicap_factor": Decimal("1.0000"), "handicap": record})
    cell = _row_html(rendered, view.current[0].episode_id)
    assert "HANDICAP" not in cell
    assert "float —M / cap $—M → group (unknown) · unknown → not applied" in cell


def test_the_header_says_not_configured_when_the_block_is_absent():
    """Shown, never implied — on the page, above the pool layer: the pool
    layer's block-absent output is main's byte for byte (the healthy pins
    in `test_radar_panel_cards.py`, untouched)."""
    view, rendered = _view(handicap=None)
    assert view.handicap_state == "not configured"
    assert "handicap:" not in rendered
    ladder = panel.LadderView(active=[], terminal=[], empty_message="No radar cards today")
    page = panel.render_radar_page(panel.RadarPanelView(pool=view, ladder=ladder))
    assert '<div class="pool-meta" id="handicap-unconfigured">handicap: not configured</div>' in page
    configured, _ = _view()
    shadow_page = panel.render_radar_page(panel.RadarPanelView(pool=configured, ladder=ladder))
    assert "handicap-unconfigured" not in shadow_page


def test_the_header_says_shadow_when_configured():
    view, rendered = _view()
    assert view.handicap_state == "shadow" and "handicap: shadow" in rendered


def test_a_degraded_handicap_shows_degraded_with_its_reason_in_header_and_banner():
    reason = "handicap step failed: ZeroDivisionError: synthetic"
    # A handicap-only degradation leaves the pool-level flag False (the raw
    # ranks are valid); the panel still shows it — header and banner.
    view, rendered = _view(pool_update={"degraded": False, "degraded_sources": [
        {"source": "handicap", "reason": reason, "since": "2026-01-05T16:00:00+00:00"}]})
    assert view.handicap_state == "degraded" and view.handicap_detail == reason
    assert f"handicap: degraded ({reason})" in rendered
    banner = re.search(r'<div class="panel-banner degraded">.*?</div>', rendered).group(0)
    assert f"handicap ({reason})" in banner


def test_a_dead_column_shows_degraded_inoperative_naming_header_and_source():
    reason = "handicap inoperative — dead column: Shares Float (screen:x@000000000000)"
    view, rendered = _view(pool_update={"degraded": False, "degraded_sources": [
        {"source": "handicap", "reason": reason, "since": "2026-01-05T16:00:00+00:00"}]})
    assert view.handicap_state == "degraded — inoperative"
    assert "handicap: degraded — inoperative (dead column: Shares Float (screen:x@000000000000))" in rendered


def test_live_is_never_rendered_active_by_h1():
    view, rendered = _view(handicap={**BLOCK, "mode": "live"})
    assert view.handicap_state == "degraded" and "handicap: live" not in rendered


def test_a_handicapped_row_does_not_move():
    view_a, _ = _view()
    view_b, _ = _view({"handicap_factor": Decimal("0.8000"), "handicap": RECORD})
    assert [r.episode_id for r in view_a.current + view_a.departed + view_a.excluded] == [
        r.episode_id for r in view_b.current + view_b.departed + view_b.excluded]
