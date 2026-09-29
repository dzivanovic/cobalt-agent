"""S3 exits C3 — the panel routes and render, offline (v3 §2 / §3 / §5;
R67, R38).

The routes are driven through TestClient with the writers replaced by
recorders (a route owns no side effect, L40: it calls C1 / C2's functions
and the store's reads, nothing else); every refusal the writers raise is
shown verbatim. The render is `build_ladder_view` over the real-shape
evaluator rows of `test_radar_panel_cards.py` with a constructed position
reader. The with-DB halves are `test_s3_c3_panel_db.py`.

Constructed values only (L32): the fixture's FTFT rows, prices 5.48 /
5.40 / 5.30, the design's 100-share examples.
"""

from __future__ import annotations

import copy
import re
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path
from types import SimpleNamespace

import pytest
from fastapi.testclient import TestClient

from cobalt.aset import radar_panel as panel
from cobalt.aset import web as web_module
from cobalt.cards import CardStateError
from cobalt.cards import legs as legs_module
from cobalt.cards.legs import LegRefused
from cobalt.cards.models import CardState
from cobalt.session import clock as session_clock_module
from test_radar_panel_cards import SCAN0, SETTINGS_ROWS, RowStore, Settings, _tunables, evaluated  # noqa: F401

client = TestClient(web_module.app)

#: 20:30 ET on 2026-09-02 — inside market_reset (the C1 / C2 tests' instant).
RESET = datetime(2026, 9, 3, 0, 30, tzinfo=timezone.utc)
AT = datetime(2026, 9, 3, 14, 5, tzinfo=timezone.utc)

NEW_ROUTES = [
    "/radar/card/{card_id}/triggered",
    "/radar/card/{card_id}/fill",
    "/radar/card/{card_id}/pass",
    "/radar/card/{card_id}/exit",
    "/radar/card/{card_id}/held",
    "/radar/card/{card_id}/correct",
    "/radar/card/{card_id}/stop",
    "/radar/card/{card_id}/stop/reset",
]

#: Every route of `web.py` at `<base>` (`5e77800f`), in file order.
BASE_ROUTES = [
    "/", "/radar", "/api/radar/pool", "/api/health", "/api/prefill", "/size", "/fill", "/attest",
    "/card/{card_id}/move", "/card/{card_id}/stop", "/radar/card/{card_id}/key",
    "/radar/card/{card_id}/dot/{factor}", "/radar/card/{card_id}/promote", "/radar/card/{card_id}/release",
]


# ---------------------------------------------------------------------
# recorders
# ---------------------------------------------------------------------


class Cards:
    """The card store's reads + `transition` / `record_stop_edit`, recorded."""

    def __init__(self, *, state="ARMED", last_price=Decimal("5.48"), structural=Decimal("5.81"), radar=True):
        self.state = state
        self.calls = []
        self.board = [] if not radar else [{
            "card_id": 1, "state": state, "last_price": last_price, "structural_stop": structural,
            "stop": Decimal("5.81"), "entry": Decimal("5.50"),
        }]
        self.open = [{"id": 1, "stop": Decimal("5.81"), "state": state}]

    def radar_board_cards(self, day):
        return copy.deepcopy(self.board)

    def open_cards(self):
        return copy.deepcopy(self.open)

    def ensure_schema(self):
        return None

    def transition(self, card_id, to_state, **kw):
        self.calls.append(("transition", card_id, to_state.value, kw["actor"].value, kw.get("evidence")))
        return 77

    def record_stop_edit(self, card_id, **kw):
        self.calls.append(("record_stop_edit", card_id, kw))
        return 91


class Aset:
    def __init__(self, calls):
        self.calls = calls

    def mark_filled(self, row_id, **kw):
        self.calls.append(("mark_filled", row_id, kw))
        recompute = SimpleNamespace(drift_warned=None, actual_fill=kw["price"])
        result = SimpleNamespace(pick_recorded=True, pick_error=None, transition_ids=[78])
        return SimpleNamespace(result=result, recompute=recompute, leg_id=301, sheet_mismatch=False)


@pytest.fixture
def world(monkeypatch):
    cards = Cards()
    monkeypatch.setenv("COBALT_ALLOW_DEV_ENTRY", "1")
    monkeypatch.setattr(web_module, "CardStore", lambda *a, **k: cards)
    monkeypatch.setattr(web_module, "AsetStore", lambda *a, **k: Aset(cards.calls))
    for name in ("record_exit", "record_held", "record_correction"):
        monkeypatch.setattr(
            legs_module, name,
            (lambda n: lambda *a, **k: cards.calls.append((n, a, k)) or _result(n))(name),
        )
    return cards


def _result(name):
    if name == "record_exit":
        return legs_module.ExitResult(401, 50, 100, 50, False, None)
    return legs_module.CorrectionResult(402, 301, 50, False, None)


def _raise(exc):
    def _f(*a, **k):
        raise exc
    return _f


# ---------------------------------------------------------------------
# C3-1 — TRIGGERED, FILLED, PASS
# ---------------------------------------------------------------------


def test_the_triggered_tap_writes_one_transition_by_you_carrying_the_last_price(world):
    response = client.post("/radar/card/1/triggered")
    assert response.status_code == 200, response.text
    (call,) = world.calls
    assert call[:4] == ("transition", 1, "TRIGGERED", "you")
    assert call[4]["last_price"] == "5.48"
    assert "last_price_at" in call[4] and call[4]["last_price_at"] is None  # X6-R: no bar time stored


def test_a_fill_with_the_untouched_prefill_is_last_poll_estimated(world):
    response = client.post("/radar/card/1/fill", data={"price": "5.48", "shares": "226", "prefill": "5.48"})
    assert response.status_code == 200, response.text
    (_, row_id, kw), = world.calls
    assert row_id == 1
    assert (kw["price"], kw["shares"], kw["price_source"], kw["flag"], kw["source"]) == (
        Decimal("5.48"), 226, "last_poll", "estimated", "panel")


def test_a_fill_with_an_edited_price_is_typed_confirmed(world):
    response = client.post("/radar/card/1/fill", data={"price": "5.47", "shares": "226", "prefill": "5.48"})
    assert response.status_code == 200, response.text
    (_, _, kw), = world.calls
    assert (kw["price"], kw["price_source"], kw["flag"]) == (Decimal("5.47"), "typed", "confirmed")


def test_a_fill_with_no_price_is_refused_by_the_fill_itself_and_nothing_is_written(world, monkeypatch):
    from cobalt.aset.store import AsetStore

    monkeypatch.setattr(web_module, "AsetStore", AsetStore)  # the real fill: it refuses before connecting
    response = client.post("/radar/card/1/fill", data={"price": "", "shares": "226", "prefill": ""})
    assert response.status_code == 422
    assert response.json()["reason"].startswith("REFUSED card 1: a fill with no price.")
    assert world.calls == []


def test_pass_moves_the_card_to_passed_by_you(world):
    world.state = "TRIGGERED"
    response = client.post("/radar/card/1/pass")
    assert response.status_code == 200, response.text
    assert world.calls[0][:4] == ("transition", 1, "PASSED", "you")


# ---------------------------------------------------------------------
# C3-1 — exits, held, corrections
# ---------------------------------------------------------------------


def test_a_half_tap_posts_the_running_count_its_screen_showed(world):
    response = client.post("/radar/card/1/exit", data={
        "preset": "half", "price": "5.40", "prefill": "5.40", "running_before": "100",
    })
    assert response.status_code == 200, response.text
    (name, args, kw), = world.calls
    assert name == "record_exit" and args == (1,)
    assert (kw["preset"], kw["running_before"], kw["price"], kw["price_source"], kw["flag"], kw["source"]) == (
        "half", 100, Decimal("5.40"), "last_poll", "estimated", "panel")
    assert kw["shares"] is None


def test_a_stale_tap_is_refused_with_c2s_text_verbatim(world, monkeypatch):
    monkeypatch.setattr(legs_module, "record_exit",
                        _raise(LegRefused("stale", "REFUSED: screen said 100, now 50 — tap again")))
    response = client.post("/radar/card/1/exit", data={
        "preset": "half", "price": "5.40", "prefill": "5.40", "running_before": "100",
    })
    assert response.status_code == 409
    assert response.json()["reason"] == "REFUSED: screen said 100, now 50 — tap again"


def test_an_untouched_flat_stays_estimated(world):
    response = client.post("/radar/card/1/exit", data={
        "preset": "flat", "price": "5.40", "prefill": "5.40", "running_before": "100",
    })
    assert response.status_code == 200, response.text
    (_, _, kw), = world.calls
    assert (kw["preset"], kw["price_source"], kw["flag"]) == ("flat", "last_poll", "estimated")


def test_a_flat_with_the_check_and_a_typed_price_is_confirmed(world):
    response = client.post("/radar/card/1/exit", data={
        "preset": "flat", "price": "5.38", "prefill": "5.40", "running_before": "100", "confirm": "1",
    })
    assert response.status_code == 200, response.text
    (_, _, kw), = world.calls
    assert (kw["price"], kw["price_source"], kw["flag"]) == (Decimal("5.38"), "typed", "confirmed")


def test_a_flat_edited_without_the_check_is_not_confirmed(world):
    client.post("/radar/card/1/exit", data={
        "preset": "flat", "price": "5.38", "prefill": "5.40", "running_before": "100",
    })
    (_, _, kw), = world.calls
    assert kw["flag"] == "estimated"


def test_a_typed_exit_carries_its_share_count(world):
    client.post("/radar/card/1/exit", data={
        "preset": "typed", "shares": "30", "price": "5.41", "prefill": "5.40", "running_before": "100",
    })
    (_, _, kw), = world.calls
    assert (kw["preset"], kw["shares"], kw["price_source"], kw["flag"]) == ("typed", 30, "typed", "confirmed")


def test_an_exit_with_no_price_is_refused_and_nothing_is_written(world):
    response = client.post("/radar/card/1/exit", data={
        "preset": "half", "price": "", "prefill": "", "running_before": "100",
    })
    assert response.status_code == 422 and "no price" in response.json()["reason"]
    assert world.calls == []


def test_holding_50_calls_the_held_writer(world):
    response = client.post("/radar/card/1/held", data={"held": "50"})
    assert response.status_code == 200, response.text
    (name, args, kw), = world.calls
    assert (name, args, kw["source"]) == ("record_held", (1, 50), "panel")


def test_a_correction_with_a_typed_price_names_its_source(world):
    response = client.post("/radar/card/1/correct", data={"leg_id": "401", "price": "5.39"})
    assert response.status_code == 200, response.text
    (name, args, kw), = world.calls
    assert (name, args) == ("record_correction", (401,))
    assert (kw["price"], kw["price_source"], kw["source"], kw["shares"]) == (Decimal("5.39"), "typed", "panel", None)


def test_a_held_refusal_reaches_the_page_verbatim(world, monkeypatch):
    monkeypatch.setattr(legs_module, "record_held",
                        _raise(LegRefused("closed_held", "CLOSED has no way back — correct the exit instead")))
    response = client.post("/radar/card/1/held", data={"held": "0"})
    assert response.status_code == 409
    assert response.json()["reason"] == "CLOSED has no way back — correct the exit instead"


def test_the_sheet_source_gets_a_page_carrying_the_refusal(world, monkeypatch):
    monkeypatch.setattr(legs_module, "record_held",
                        _raise(LegRefused("closed_held", "CLOSED has no way back — correct the exit instead")))
    monkeypatch.setattr(web_module, "_render", lambda banner="", result="", form=None: f"<html>{banner}</html>")
    response = client.post("/radar/card/1/held", data={"held": "0", "source": "sheet"})
    assert response.status_code == 409
    assert "CLOSED has no way back — correct the exit instead" in response.text
    assert response.headers["content-type"].startswith("text/html")


# ---------------------------------------------------------------------
# C3-1 — the stop: edit and ↺
# ---------------------------------------------------------------------


def test_a_stop_edit_goes_through_the_one_card_stop_function(world, monkeypatch):
    from cobalt.aset import card_stop

    seen = []
    monkeypatch.setattr(card_stop, "set_card_stop", lambda card_id, to_stop, **k: seen.append((card_id, to_stop))
                        or card_stop.StopEdit(card_id, Decimal("5.81"), Decimal(to_stop), 91))
    response = client.post("/radar/card/1/stop", data={"to_stop": "5.70"})
    assert response.status_code == 200, response.text
    assert seen == [(1, "5.70")]


def test_the_reset_returns_the_stop_to_the_structural_stop_as_a_reset(world):
    response = client.post("/radar/card/1/stop/reset")
    assert response.status_code == 200, response.text
    (name, card_id, kw), = world.calls
    assert (name, card_id) == ("record_stop_edit", 1)
    assert (kw["kind"], kw["to_stop"], kw["from_stop"]) == ("reset", Decimal("5.81"), Decimal("5.81"))


def test_a_reset_on_a_card_with_no_structural_stop_shows_the_writers_refusal(world, monkeypatch):
    world.board = []  # a manual card: not on the radar board, no structural stop
    text = ("REFUSED card 1: a reset returns the stop to Cobalt's structural stop, and this card has none "
            "(a manual card) — no Cobalt stop to reset to. Type the stop instead. Nothing written.")
    world.record_stop_edit = _raise(CardStateError(text))
    response = client.post("/radar/card/1/stop/reset")
    assert response.status_code == 409 and response.json()["reason"] == text


# ---------------------------------------------------------------------
# market_reset: every POST refused, nothing written
# ---------------------------------------------------------------------


@pytest.mark.parametrize("path,data", [
    ("/radar/card/1/triggered", {}),
    ("/radar/card/1/fill", {"price": "5.48", "shares": "10", "prefill": "5.48"}),
    ("/radar/card/1/pass", {}),
    ("/radar/card/1/exit", {"preset": "half", "price": "5.4", "prefill": "5.4", "running_before": "100"}),
    ("/radar/card/1/held", {"held": "50"}),
    ("/radar/card/1/correct", {"leg_id": "401", "price": "5.39"}),
    ("/radar/card/1/stop", {"to_stop": "5.70"}),
    ("/radar/card/1/stop/reset", {}),
])
def test_market_reset_refuses_every_post_and_writes_nothing(world, monkeypatch, path, data):
    from cobalt.session import store as session_store

    monkeypatch.setattr(session_clock_module, "now_utc", lambda: RESET)
    monkeypatch.setattr(session_store.SessionBlockStore, "record", lambda self, **kw: None)
    response = client.post(path, data=data)
    assert response.status_code == 409, response.text
    assert "inside MARKET RESET" in response.json()["reason"]
    assert world.calls == []


# ---------------------------------------------------------------------
# S-WEB — the block sits directly after `/release`
# ---------------------------------------------------------------------


def _routes_in_file_order() -> list[str]:
    source = Path(web_module.__file__).read_text(encoding="utf-8")
    return re.findall(r'^@app\.(?:get|post)\("([^"]+)"', source, re.M)


def test_the_new_routes_sit_in_one_block_directly_after_release():
    routes = _routes_in_file_order()
    pre_existing = [r for r in routes if r not in NEW_ROUTES]
    assert pre_existing == BASE_ROUTES, "a pre-existing route moved, or a route was added outside the block"
    start = routes.index("/radar/card/{card_id}/release") + 1
    assert routes[start:start + len(NEW_ROUTES)] == NEW_ROUTES
    assert routes.index("/attest") < routes.index("/radar/card/{card_id}/release")
    # nothing of the block after a pre-existing route that follows /release (none at <base>)
    assert all(routes.index(r) > routes.index("/radar/card/{card_id}/release") for r in NEW_ROUTES)


# ---------------------------------------------------------------------
# C3-2 / C3-3 — the render
# ---------------------------------------------------------------------


def _leg(**over):
    base = dict(id=301, seq=0, kind="entry", shares=100, price=Decimal("5.4800"), flag="estimated",
                price_source="last_poll", at=AT, stop_in_force=Decimal("5.8100"), preset=None, held_stated=None)
    base.update(over)
    return base


def _position(*, legs=None, running=100, basis="legs", owner="cobalt", drift=(Decimal("27.00"), Decimal("20"), True),
              realized=(Decimal("0.2500"), True, None)):
    return panel.InTradeView(
        running=running, basis=basis, legs=[panel.LegView(**l) for l in (legs or [_leg()])],
        realized_value=realized[0], realized_provisional=realized[1], realized_reason=realized[2],
        stop_owner=owner, distance_change_pct=drift[0], drift_warning_pct=drift[1], drift_warned=drift[2],
    )


def _view(rows, reader):
    return panel.build_ladder_view(
        card_store=RowStore(rows), settings_store=Settings(SETTINGS_ROWS), clock=None,
        now=SCAN0 + timedelta(seconds=200), tunables_loader=_tunables(), rung_source=lambda i, c: "reduced",
        position_reader=reader,
    )


def _card_html(rendered: str, card_id: int) -> str:
    start = rendered.index(f'<article class="ladder-item')
    for match in re.finditer(r'<article class="ladder-item[^"]*" data-card-id="(\d+)"', rendered):
        if int(match.group(1)) == card_id:
            start = match.start()
            end = rendered.find("<article", start + 1)
            return rendered[start:end if end > 0 else len(rendered)]
    raise AssertionError(f"card {card_id} not rendered")


def _hidden(fragment: str, name: str) -> list[str]:
    return re.findall(rf'<input type="hidden" name="{name}" value="([^"]*)"', fragment)


def test_a_triggered_card_shows_last_entry_stop_and_a_filled_form_prefilled_from_last(evaluated):
    view = _view(evaluated["rows"], reader=lambda card: pytest.fail("no position read for TRIGGERED"))
    card = next(c for c in view.active if c.state is CardState.TRIGGERED)
    fragment = _card_html(panel.render_ladder(view), card.id)
    assert "last 5.48" in fragment and f"entry {card.trigger}" in fragment and f"stop {card.stop}" in fragment
    assert "bar time not stored" in fragment
    assert re.search(r'action="/radar/card/3/fill"', fragment)
    assert re.search(r'<input[^>]*name="price"[^>]*value="5.48"', fragment)
    assert _hidden(fragment, "prefill") == ["5.48"]
    assert re.search(rf'<input[^>]*name="shares"[^>]*value="{card.shares}"', fragment)
    assert 'action="/radar/card/3/pass"' in fragment


def test_a_triggered_card_with_no_last_price_leaves_the_price_empty_never_the_entry(evaluated):
    rows = copy.deepcopy(evaluated["rows"])
    next(r for r in rows if r["state"] == "TRIGGERED")["last_price"] = None
    view = _view(rows, reader=lambda card: pytest.fail("no position read"))
    card = next(c for c in view.active if c.state is CardState.TRIGGERED)
    fragment = _card_html(panel.render_ladder(view), card.id)
    assert re.search(r'<input[^>]*name="price"[^>]*value=""', fragment)
    assert _hidden(fragment, "prefill") == [""]
    assert not re.search(rf'name="price"[^>]*value="{card.trigger}"', fragment)


def test_an_armed_card_offers_the_triggered_tap(evaluated):
    view = _view(evaluated["rows"], reader=lambda card: pytest.fail("no position read"))
    card = next(c for c in view.active if c.state is CardState.ARMED)
    assert f'action="/radar/card/{card.id}/triggered"' in _card_html(panel.render_ladder(view), card.id)


def test_in_trade_render_carries_every_control_and_the_running_it_posts(evaluated):
    legs = [_leg(), _leg(id=302, seq=1, kind="exit", shares=50, price=Decimal("5.40"), preset="half",
                         stop_in_force=Decimal("5.7000"))]
    view = _view(evaluated["rows"], reader=lambda card: _position(legs=legs, running=50, owner="yours"))
    card = next(c for c in view.active if c.state is CardState.FILLED)
    fragment = _card_html(panel.render_ladder(view), card.id)
    assert "running 50 sh" in fragment
    for preset, label in (("half", "½"), ("third", "⅓"), ("flat", "flat"), ("typed", "typed")):
        form = re.search(rf'<form[^>]*action="/radar/card/{card.id}/exit"[^>]*>(?:(?!</form>).)*'
                         rf'name="preset" value="{preset}"(?:(?!</form>).)*</form>', fragment, re.S)
        assert form, preset
        assert _hidden(form.group(0), "running_before") == ["50"], preset
        assert label in form.group(0)
    flat = re.search(r'<form(?:(?!</form>).)*value="flat"(?:(?!</form>).)*</form>', fragment, re.S).group(0)
    assert 'name="confirm" value="1"' in flat and "✓" in flat
    assert re.search(r'<input[^>]*name="price"[^>]*value="5.48"', flat), "flat's price is prefilled, editable"
    assert f'action="/radar/card/{card.id}/held"' in fragment and "HOLDING" in fragment
    # both legs listed; the estimated one carries a correct control, naming its leg
    assert "5.4800" in fragment and "5.40" in fragment and "estimated" in fragment
    corrections = re.findall(r'<form[^>]*action="/radar/card/\d+/correct"(?:(?!</form>).)*</form>', fragment, re.S)
    assert [_hidden(f, "leg_id") for f in corrections] == [["301"], ["302"]]
    assert "realized R 0.2500" in fragment and "provisional" in fragment
    assert "drift 27.00% vs P 20%" in fragment
    # the stop: his, YOURS, the delta; Cobalt's beside it; ↺ with its value; the per-leg gap
    assert '<span class="yours">YOURS</span>' in fragment
    assert f"Cobalt stop {card.structural_stop}" in fragment
    assert f"↺ {card.structural_stop}" in fragment and f'action="/radar/card/{card.id}/stop/reset"' in fragment
    assert f"Δ {card.stop - card.structural_stop}" in fragment
    for in_force in (Decimal("5.8100"), Decimal("5.7000")):  # stop_in_force − structural_stop, per leg
        assert f"gap {in_force - card.structural_stop}" in fragment
    assert f'action="/radar/card/{card.id}/stop"' in fragment


def test_in_trade_render_names_a_pre_c1_basis_and_the_missing_p(evaluated):
    view = _view(evaluated["rows"], reader=lambda card: _position(
        legs=[], running=66, basis="recomputed_shares", drift=(None, None, None),
        realized=(None, False, "not computed — no entry leg")))
    card = next(c for c in view.active if c.state is CardState.FILLED)
    fragment = _card_html(panel.render_ladder(view), card.id)
    assert "running 66 sh (basis recomputed_shares)" in fragment
    assert "RE-READ STOP — setting fills.drift_warning_pct missing, warning not evaluated" in fragment
    assert "realized R not computed — no entry leg" in fragment
    assert '<span class="yours">YOURS</span>' not in fragment  # owner cobalt: no badge
    assert f"Cobalt stop {card.structural_stop}" in fragment


def test_a_position_that_cannot_be_read_is_said_on_the_card(evaluated):
    def broken(card):
        raise RuntimeError("legs offline")
    view = _view(evaluated["rows"], reader=broken)
    card = next(c for c in view.active if c.state is CardState.FILLED)
    fragment = _card_html(panel.render_ladder(view), card.id)
    assert "FAILED · position unreadable: RuntimeError: legs offline" in fragment
    assert f"Cobalt stop {card.structural_stop}" in fragment


def test_the_notes_line_keeps_its_text(evaluated):
    view = _view(evaluated["rows"], reader=lambda card: _position())
    assert "no notes source wired to radar cards (S3)" in panel.render_ladder(view)


def test_the_panel_script_posts_every_card_form(evaluated):
    assert "data-card-form" in panel.PANEL_JS and "new FormData" in panel.PANEL_JS


# ---------------------------------------------------------------------
# C3-4 — the manual card's IN-TRADE controls on the sheet
# ---------------------------------------------------------------------


def test_the_sheet_renders_a_manual_cards_in_trade_controls_with_the_same_routes_and_no_reset():
    fragment = panel.render_in_trade(
        9, _position(owner="yours"), direction="long", stop=Decimal("9.90"), structural_stop=None,
        last=None, source="sheet",
    )
    assert 'action="/radar/card/9/exit"' in fragment and 'action="/radar/card/9/held"' in fragment
    assert _hidden(fragment, "source").count("sheet") == len(_hidden(fragment, "source")) > 0
    assert "↺" not in fragment and "/stop/reset" not in fragment
    assert "Cobalt stop NULL — no Cobalt stop" in fragment
    assert "gap NULL — no Cobalt stop" in fragment
    assert re.search(r'<input[^>]*name="price"[^>]*value=""', fragment), "no last price on the sheet: empty"
