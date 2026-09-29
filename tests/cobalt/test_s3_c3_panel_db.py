"""S3 exits C3 — the panel end to end on `cobalt_dev` (v3 §2 / §3 / §5;
R67, R38).

With-DB, inside the suite's rolled-back transaction with M1 applied there
(`legs_db_support.apply_0021`), so these hold at `0013` and at `0021`
alike and leave nothing applied (L76). The radar card is the S2-P2
`world` fixture's evaluator card (synthetic ticker `ZZPB`, the hub-cut
real-shape bars), key-tapped and ARMED by his taps; every later move is a
POST through TestClient to the C3 routes, and every "from the rendered
page" value is read out of the ladder's own HTML. The manual card is
`legs_db_support.manual_card` (ticker `TEST`, 10.0000 / 9.9000).

Constructed values only (L32): the last price 5.4800 is set on the test's
own card inside the rolled-back transaction.
"""

from __future__ import annotations

import html as html_lib
import os
import re
from datetime import datetime, timezone
from decimal import Decimal

import pytest
from fastapi.testclient import TestClient

from legs_db_support import apply_0021, fill_kwargs, manual_card, patch_daymode
from test_radar_cards_db import SCAN0, TICKER, world  # noqa: F401  (the fixture)

pytestmark = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)

#: 20:30 ET on 2026-09-02 — inside market_reset (the C1 / C2 tests' instant).
RESET = datetime(2026, 9, 3, 0, 30, tzinfo=timezone.utc)
LAST = Decimal("5.4800")
COUNTED = ("aset_sizings", "legs", "card_transitions", "card_stop_edits", "picks")


@pytest.fixture
def panel_world(world, monkeypatch):  # noqa: F811
    from cobalt.aset import web as web_module
    from cobalt.aset.store import AsetStore

    patch_daymode(monkeypatch)
    monkeypatch.setenv("COBALT_ALLOW_DEV_ENTRY", "1")
    aset = AsetStore("cobalt_dev")
    aset.ensure_schema()
    apply_0021(aset)
    world["aset"] = aset
    world["client"] = TestClient(web_module.app)
    return world


def _armed(world) -> int:  # noqa: F811
    from cobalt.aset.engine import size_at_key
    from cobalt.aset.models import Direction, Grade
    from cobalt.cards import Actor, CardState
    from cobalt.settings.models import TraderSettings

    card_id = world["scan"](SCAN0).created[0]
    cards = world["cards"]
    trader = TraderSettings.from_db(world["settings"])
    record = cards.radar_card(card_id)
    sizing = size_at_key(
        Grade.A_PLUS, ticker=TICKER, entry=record["entry"], stop=record["stop"],
        direction=Direction(record["direction"]), sheet_modes=trader.sheet_modes, sheet="half",
        enabled=trader.daymode.enabled_grades_for("reduced"), max_stop_distance_pct=Decimal("10"),
    )
    cards.tap_key(card_id, sizing)
    cards.transition(card_id, CardState.ARMED, actor=Actor.YOU)
    with cards._connect() as conn:
        conn.execute("UPDATE aset_sizings SET last_price = %s WHERE id = %s", (LAST, card_id))
    return card_id


def _filled(world, *, shares: int = 100, price: str = "5.4800") -> int:  # noqa: F811
    card_id = _armed(world)
    client = world["client"]
    assert client.post(f"/radar/card/{card_id}/triggered").status_code == 200
    response = client.post(f"/radar/card/{card_id}/fill",
                           data={"price": price, "shares": str(shares), "prefill": str(LAST)})
    assert response.status_code == 200, response.text
    return card_id


def _render(world) -> str:  # noqa: F811
    from cobalt.aset import radar_panel as panel
    from cobalt.session import clock, session_clock

    view = panel.build_ladder_view(
        card_store=world["cards"], settings_store=world["settings"], clock=session_clock(),
        now=clock.now_utc(), rung_source=lambda _at, _cfg: "reduced",
    )
    return panel.render_ladder(view)


def _fragment(rendered: str, card_id: int) -> str:
    """The card's ladder item (active) and / or its terminal legs block."""
    starts = [m.start() for m in re.finditer(
        rf'<(?:article|div) class="(?:ladder-item[^"]*|terminal-legs)" data-card-id="{card_id}"', rendered)]
    if not starts:
        raise AssertionError(f"card {card_id} not rendered")
    parts = []
    for start in starts:
        stop = re.search(r'<article |<div class="terminal-row"|<div class="terminal-legs"|</section>',
                         rendered[start + 1:])
        parts.append(rendered[start:start + 1 + stop.start() if stop else len(rendered)])
    return "".join(parts)


def _form(fragment: str, path: str, **match) -> dict:
    """The fields a submit of one rendered form posts (checkboxes left out)."""
    for form in re.findall(rf'<form[^>]*action="{re.escape(path)}"[^>]*>(.*?)</form>', fragment, re.S):
        fields = {}
        for tag in re.findall(r"<input[^>]*>", form):
            if 'type="checkbox"' in tag:
                continue
            name = re.search(r'name="([^"]+)"', tag)
            value = re.search(r'value="([^"]*)"', tag)
            if name:
                fields[name.group(1)] = html_lib.unescape(value.group(1)) if value else ""
        if all(fields.get(k) == v for k, v in match.items()):
            return fields
    raise AssertionError(f"no form {path} {match} in the fragment")


def _history(world, card_id):  # noqa: F811
    return world["cards"].history(card_id)


def _legs(world, card_id):  # noqa: F811
    with world["aset"]._connect() as conn:
        cur = conn.execute("SELECT * FROM legs_current_v WHERE card_id = %s ORDER BY seq", (card_id,))
        return [dict(zip([d.name for d in cur.description], r)) for r in cur.fetchall()]


def _running(world, card_id):  # noqa: F811
    from cobalt.cards import legs

    return legs.read_position(card_id).running.shares


def _counts(world) -> dict:  # noqa: F811
    with world["aset"]._connect() as conn:
        return {t: conn.execute(f"SELECT count(*) FROM {t}").fetchone()[0] for t in COUNTED}


# ---------------------------------------------------------------------
# TRIGGERED, FILLED
# ---------------------------------------------------------------------


def test_the_triggered_tap_writes_one_transition_by_you_with_the_last_price(panel_world):
    card_id = _armed(panel_world)
    before = len(_history(panel_world, card_id))
    response = panel_world["client"].post(f"/radar/card/{card_id}/triggered")
    assert response.status_code == 200, response.text
    history = _history(panel_world, card_id)
    assert len(history) == before + 1
    last = history[-1]
    assert (last["from_state"], last["to_state"], last["actor"]) == ("ARMED", "TRIGGERED", "you")
    assert last["evidence"]["last_price"] == str(LAST) and last["evidence"]["last_price_at"] is None


def test_the_triggered_card_renders_its_fill_form_prefilled_from_the_last_price(panel_world):
    card_id = _armed(panel_world)
    panel_world["client"].post(f"/radar/card/{card_id}/triggered")
    fields = _form(_fragment(_render(panel_world), card_id), f"/radar/card/{card_id}/fill")
    assert fields["price"] == str(LAST) and fields["prefill"] == str(LAST)


def test_a_fill_from_the_untouched_prefill_is_an_estimated_last_poll_entry_leg(panel_world):
    card_id = _armed(panel_world)
    client = panel_world["client"]
    client.post(f"/radar/card/{card_id}/triggered")
    fields = _form(_fragment(_render(panel_world), card_id), f"/radar/card/{card_id}/fill")
    response = client.post(f"/radar/card/{card_id}/fill", data=fields)
    assert response.status_code == 200, response.text
    (entry,) = _legs(panel_world, card_id)
    assert (entry["kind"], entry["price_source"], entry["flag"], entry["source"]) == (
        "entry", "last_poll", "estimated", "panel")
    assert entry["price"] == LAST
    assert panel_world["cards"].state_of(card_id).value == "FILLED"


def test_a_fill_with_an_edited_price_is_a_typed_confirmed_entry_leg(panel_world):
    card_id = _filled(panel_world, price="5.4700")
    (entry,) = _legs(panel_world, card_id)
    assert (entry["price"], entry["price_source"], entry["flag"]) == (Decimal("5.4700"), "typed", "confirmed")


def test_a_fill_with_no_price_is_refused_and_nothing_is_written(panel_world):
    card_id = _armed(panel_world)
    client = panel_world["client"]
    client.post(f"/radar/card/{card_id}/triggered")
    before = _counts(panel_world)
    response = client.post(f"/radar/card/{card_id}/fill", data={"price": "", "shares": "100", "prefill": ""})
    assert response.status_code == 422
    assert response.json()["reason"].startswith(f"REFUSED card {card_id}: a fill with no price.")
    assert _counts(panel_world) == before


def test_pass_moves_a_triggered_card_to_passed(panel_world):
    card_id = _armed(panel_world)
    client = panel_world["client"]
    client.post(f"/radar/card/{card_id}/triggered")
    assert client.post(f"/radar/card/{card_id}/pass").status_code == 200
    last = _history(panel_world, card_id)[-1]
    assert (last["to_state"], last["actor"]) == ("PASSED", "you")


# ---------------------------------------------------------------------
# IN-TRADE: exits from the rendered page
# ---------------------------------------------------------------------


def test_a_half_from_the_rendered_page_then_the_same_half_again_is_refused(panel_world):
    card_id = _filled(panel_world, shares=100)
    client = panel_world["client"]
    fragment = _fragment(_render(panel_world), card_id)
    half = _form(fragment, f"/radar/card/{card_id}/exit", preset="half")
    assert half["running_before"] == "100"
    assert client.post(f"/radar/card/{card_id}/exit", data=half).status_code == 200
    assert _running(panel_world, card_id) == 50
    again = client.post(f"/radar/card/{card_id}/exit", data=half)
    assert again.status_code == 409
    assert again.json()["reason"] == "REFUSED: screen said 100, now 50 — tap again"
    assert len([l for l in _legs(panel_world, card_id) if l["kind"] == "exit"]) == 1


def test_an_untouched_flat_is_estimated_closes_the_card_and_is_listed_for_correction(panel_world):
    card_id = _filled(panel_world, shares=100)
    client = panel_world["client"]
    flat = _form(_fragment(_render(panel_world), card_id), f"/radar/card/{card_id}/exit", preset="flat")
    assert client.post(f"/radar/card/{card_id}/exit", data=flat).status_code == 200
    exits = [l for l in _legs(panel_world, card_id) if l["kind"] == "exit"]
    assert [(l["flag"], l["price_source"], l["shares"]) for l in exits] == [("estimated", "last_poll", 100)]
    assert panel_world["cards"].state_of(card_id).value == "CLOSED"
    listed = _fragment(_render(panel_world), card_id)
    correct = _form(listed, f"/radar/card/{card_id}/correct", leg_id=str(exits[0]["id"]))
    # the ✓ on the listed leg: a correction with his typed price → confirmed
    correct["price"] = "5.3900"
    response = client.post(f"/radar/card/{card_id}/correct", data=correct)
    assert response.status_code == 200, response.text
    (fixed,) = [l for l in _legs(panel_world, card_id) if l["kind"] == "exit"]
    assert (fixed["flag"], fixed["price_source"], fixed["price"], fixed["corrects"]) == (
        "confirmed", "typed", Decimal("5.3900"), exits[0]["id"])


def test_a_flat_with_the_check_and_a_typed_price_is_confirmed_and_closes(panel_world):
    card_id = _filled(panel_world, shares=100)
    flat = _form(_fragment(_render(panel_world), card_id), f"/radar/card/{card_id}/exit", preset="flat")
    flat.update(price="5.3800", confirm="1")
    response = panel_world["client"].post(f"/radar/card/{card_id}/exit", data=flat)
    assert response.status_code == 200, response.text
    (leg,) = [l for l in _legs(panel_world, card_id) if l["kind"] == "exit"]
    assert (leg["flag"], leg["price_source"], leg["price"]) == ("confirmed", "typed", Decimal("5.3800"))
    assert panel_world["cards"].state_of(card_id).value == "CLOSED"
    assert _history(panel_world, card_id)[-1]["evidence"]["leg_id"] == leg["id"]


def test_holding_50_is_the_entry_correction_and_running_is_50(panel_world):
    card_id = _filled(panel_world, shares=100)
    fields = _form(_fragment(_render(panel_world), card_id), f"/radar/card/{card_id}/held")
    fields["held"] = "50"
    response = panel_world["client"].post(f"/radar/card/{card_id}/held", data=fields)
    assert response.status_code == 200, response.text
    entry = next(l for l in _legs(panel_world, card_id) if l["kind"] == "entry")
    assert (entry["held_stated"], entry["shares"], entry["flag"]) == (50, 50, "confirmed")
    assert _running(panel_world, card_id) == 50


def test_a_correction_of_an_estimated_leg_is_confirmed(panel_world):
    card_id = _filled(panel_world, shares=100, price=str(LAST))  # untouched prefill → estimated entry
    fragment = _fragment(_render(panel_world), card_id)
    (entry,) = _legs(panel_world, card_id)
    fields = _form(fragment, f"/radar/card/{card_id}/correct", leg_id=str(entry["id"]))
    fields["price"] = "5.4600"
    response = panel_world["client"].post(f"/radar/card/{card_id}/correct", data=fields)
    assert response.status_code == 200, response.text
    (fixed,) = _legs(panel_world, card_id)
    assert (fixed["flag"], fixed["price_source"], fixed["price"]) == ("confirmed", "typed", Decimal("5.4600"))


# ---------------------------------------------------------------------
# the stop: YOURS, Cobalt's beside it, ↺
# ---------------------------------------------------------------------


def test_a_stop_edit_shows_yours_and_the_delta_and_the_reset_gives_it_back(panel_world):
    card_id = _filled(panel_world, shares=100)
    client = panel_world["client"]
    structural = panel_world["cards"].radar_card(card_id)["stop"]
    assert client.post(f"/radar/card/{card_id}/stop", data={"to_stop": "5.7000"}).status_code == 200
    assert panel_world["cards"].stop_owner(card_id) == "yours"
    fragment = _fragment(_render(panel_world), card_id)
    assert '<span class="yours">YOURS</span>' in fragment
    assert f"Δ {Decimal('5.7000') - structural}" in fragment
    assert f"Cobalt stop {structural}" in fragment and f"↺ {structural}" in fragment
    response = client.post(f"/radar/card/{card_id}/stop/reset", data={})
    assert response.status_code == 200, response.text
    assert panel_world["cards"].stop_owner(card_id) == "cobalt"
    with panel_world["aset"]._connect() as conn:
        kind, to_stop = conn.execute(
            "SELECT kind, to_stop FROM card_stop_edits WHERE card_id = %s ORDER BY id DESC LIMIT 1", (card_id,)
        ).fetchone()
    assert (kind, to_stop) == ("reset", structural)
    fragment = _fragment(_render(panel_world), card_id)
    assert '<span class="yours">YOURS</span>' not in fragment and f"Cobalt stop {structural}" in fragment


def test_p_missing_renders_the_re_read_stop_line(panel_world):
    card_id = _filled(panel_world, shares=100)  # the world's settings carry no fills.drift_warning_pct
    fragment = _fragment(_render(panel_world), card_id)
    assert "RE-READ STOP — setting fills.drift_warning_pct missing, warning not evaluated" in fragment


def test_a_manual_card_gets_its_in_trade_controls_on_the_sheet_and_no_reset(panel_world):
    from cobalt.aset import web as web_module

    aset = panel_world["aset"]
    card_id = manual_card(aset)
    aset.mark_filled(card_id, **fill_kwargs(price="10.10", shares=100, p=20))
    sheet = web_module._open_cards_section()
    start = sheet.index(f"#{card_id} ·")
    end = sheet.find('<div class="crow">', start)
    fragment = sheet[start:] if end < 0 else sheet[start:end]
    fields = _form(fragment, f"/radar/card/{card_id}/exit", preset="half")
    assert fields["source"] == "sheet" and fields["running_before"] == "100"
    assert "↺" not in fragment and "/stop/reset" not in fragment
    assert "Cobalt stop NULL — no Cobalt stop" in fragment
    refused = panel_world["client"].post(f"/radar/card/{card_id}/stop/reset", data={"source": "sheet"})
    assert refused.status_code == 409
    assert "this card has none (a manual card) — no Cobalt stop to reset to" in html_lib.unescape(refused.text)
    # the sheet's own half, through the same route
    response = panel_world["client"].post(f"/radar/card/{card_id}/exit", data={**fields, "price": "10.20"})
    assert response.status_code == 200, response.text
    (leg,) = [l for l in _legs(panel_world, card_id) if l["kind"] == "exit"]
    assert (leg["source"], leg["shares"], leg["flag"]) == ("sheet", 50, "confirmed")


# ---------------------------------------------------------------------
# nothing written where nothing may be
# ---------------------------------------------------------------------


def test_market_reset_refuses_every_post_and_writes_nothing(panel_world, monkeypatch):
    from cobalt.session import clock

    card_id = _filled(panel_world, shares=100)
    entry = _legs(panel_world, card_id)[0]
    before = _counts(panel_world)
    monkeypatch.setattr(clock, "now_utc", lambda: RESET)
    client = panel_world["client"]
    posts = [
        ("triggered", {}), ("fill", {"price": "5.48", "shares": "10", "prefill": "5.48"}), ("pass", {}),
        ("exit", {"preset": "half", "price": "5.40", "prefill": "5.40", "running_before": "100"}),
        ("held", {"held": "50"}), ("correct", {"leg_id": str(entry["id"]), "price": "5.39"}),
        ("stop", {"to_stop": "5.70"}), ("stop/reset", {}),
    ]
    for path, data in posts:
        response = client.post(f"/radar/card/{card_id}/{path}", data=data)
        assert response.status_code == 409, (path, response.text)
        assert "inside MARKET RESET" in response.json()["reason"], path
    assert _counts(panel_world) == before


def test_get_radar_and_the_in_trade_render_write_nothing(panel_world):
    card_id = _filled(panel_world, shares=100)
    before = _counts(panel_world)
    assert panel_world["client"].get("/radar").status_code == 200
    fragment = _fragment(_render(panel_world), card_id)
    assert "running 100 sh" in fragment
    assert _counts(panel_world) == before
