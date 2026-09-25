"""X29 (v2 §7, measurement only; Fable X16; R43): after a scan nulls a
score, when do the strip's chip and slot change, and when does the STALE
badge appear?

Measured OFFLINE on the panel's own code: the server render (`/radar`,
`build_ladder_view` + `render_ladder`) over `radar_cards_v`-shaped rows
from the real evaluator (`test_radar_panel_cards`' own adapter), and the
page's own JavaScript source — which function re-renders the ladder and
which one only the pool layer. The browser's timing is NOT driven here (no
browser in the suite): that half is read from the script, and said so."""

from __future__ import annotations

import copy
import re
from pathlib import Path

import radar_p2_support as sup
from cobalt.aset import radar_panel as panel

from stale_support import SCAN0


def _row():
    import test_radar_panel_cards as tpc

    radar = sup.FakeRadarStore(sup.members("FTFT"), {"FTFT": sup.fixture_bars("FTFT")})
    cards = sup.FakeCardStore()
    instant = [SCAN0]
    tpc._scan(tpc._stage(radar, cards, instant), radar, instant, SCAN0)
    base = copy.deepcopy(cards.cards[1])
    return tpc, tpc._view_row({**base, "id": 1, "state": "WATCH"}, radar, run_id=max(radar.runs), state_at=SCAN0)


def _order(tpc, rows) -> list[int]:
    html = panel.render_ladder(tpc._ladder(rows))
    return [int(x) for x in re.findall(r'class="ladder-item[^"]*" data-card-id="(\d+)"', html)]


def _js_function(source: str, head: str) -> str:
    return source.split(head, 1)[1].split("\n }\n", 1)[0]


def test_x29_chip_and_slot_move_at_the_next_render_not_on_the_periodic_refresh():
    tpc, row = _row()
    # Two WATCH cards; the scores are this test's own: card 1 outranks card 2 while fresh.
    scored = {**row, "card_id": 1, "card_score": 50, "pool_position": 2}
    other = {**copy.deepcopy(row), "card_id": 2, "card_score": 12, "pool_position": 1}
    stale = {**scored, "card_score": None, "proximity": None,
             "score_suppressed": "bars stale — last close 11:29:00 ET, older than 2 × radar.scan_interval"}
    before = _order(tpc, [scored, other])
    after = _order(tpc, [stale, other])
    source = Path(panel.__file__).read_text()
    refresh_pool = _js_function(source, "async function refreshPool(){")
    post = _js_function(source, "async function post(cardId,path,body){")
    pool_rerenders_ladder = "refreshLadder" in refresh_pool or "fetch('/radar'" in refresh_pool
    tap_rerenders_ladder = "await refreshLadder()" in post
    badge_each_pool_refresh = "mirrorStale(next)" in refresh_pool
    print(f"X29: server_order_before={before} server_order_after_reload={after} "
          f"periodic_refreshPool_rerenders_ladder={pool_rerenders_ladder} tap_post_rerenders_ladder={tap_rerenders_ladder} "
          f"stale_badge_mirrored_each_refreshPool={badge_each_pool_refresh} browser_timing=UNPROVEN(no browser in the suite)")
    assert before[:2] == [1, 2] and after[:2] == [2, 1]
    assert not pool_rerenders_ladder and tap_rerenders_ladder and badge_each_pool_refresh
