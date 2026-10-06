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
    "/settings/daily", "/settings/daily/apply",  # DRC D4's block, directly after /attest (the 09-30 seam)
    "/card/{card_id}/move", "/card/{card_id}/stop", "/radar/card/{card_id}/key",
    "/radar/card/{card_id}/dot/{factor}", "/radar/card/{card_id}/promote", "/radar/card/{card_id}/release",
    "/drc", "/drc/import", "/drc/no-trade", "/drc/scan",  # DRC D2's block, last in the file (S-4)
    "/drc/state-book", "/drc/resolve",  # DRC K3-9, appended inside D2's block
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
    # C3 fix r1 F2: `/correct` reads card 1's current legs (401, 301) first.
    monkeypatch.setattr(legs_module, "read_position", lambda card_id: legs_module.Position(
        {"id": card_id}, [{"id": 301}, {"id": 401}] if card_id == 1 else [], None, None))
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


@pytest.mark.skipif('not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER"))', reason="reaches cobalt_dev (lock-relief G1)")
def test_a_fill_with_the_untouched_prefill_is_last_poll_estimated(world):
    response = client.post("/radar/card/1/fill", data={"price": "5.48", "shares": "226", "prefill": "5.48"})
    assert response.status_code == 200, response.text
    (_, row_id, kw), = world.calls
    assert row_id == 1
    assert (kw["price"], kw["shares"], kw["price_source"], kw["flag"], kw["source"]) == (
        Decimal("5.48"), 226, "last_poll", "estimated", "panel")


@pytest.mark.skipif('not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER"))', reason="reaches cobalt_dev (lock-relief G1)")
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


@pytest.mark.skipif('not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER"))', reason="reaches cobalt_dev (lock-relief G1)")
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


@pytest.mark.skipif('not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER"))', reason="reaches cobalt_dev (lock-relief G1)")
def test_an_untouched_flat_stays_estimated(world):
    response = client.post("/radar/card/1/exit", data={
        "preset": "flat", "price": "5.40", "prefill": "5.40", "running_before": "100",
    })
    assert response.status_code == 200, response.text
    (_, _, kw), = world.calls
    assert (kw["preset"], kw["price_source"], kw["flag"]) == ("flat", "last_poll", "estimated")


@pytest.mark.skipif('not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER"))', reason="reaches cobalt_dev (lock-relief G1)")
def test_a_flat_with_the_check_and_a_typed_price_is_confirmed(world):
    response = client.post("/radar/card/1/exit", data={
        "preset": "flat", "price": "5.38", "prefill": "5.40", "running_before": "100", "confirm": "1",
    })
    assert response.status_code == 200, response.text
    (_, _, kw), = world.calls
    assert (kw["price"], kw["price_source"], kw["flag"]) == (Decimal("5.38"), "typed", "confirmed")


@pytest.mark.skipif('not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER"))', reason="reaches cobalt_dev (lock-relief G1)")
def test_a_flat_edited_without_the_check_is_not_confirmed(world):
    client.post("/radar/card/1/exit", data={
        "preset": "flat", "price": "5.38", "prefill": "5.40", "running_before": "100",
    })
    (_, _, kw), = world.calls
    assert kw["flag"] == "estimated"


@pytest.mark.skipif('not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER"))', reason="reaches cobalt_dev (lock-relief G1)")
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


@pytest.mark.skipif('not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER"))', reason="reaches cobalt_dev (lock-relief G1)")
def test_holding_50_calls_the_held_writer(world):
    response = client.post("/radar/card/1/held", data={"held": "50"})
    assert response.status_code == 200, response.text
    (name, args, kw), = world.calls
    assert (name, args, kw["source"]) == ("record_held", (1, 50), "panel")


@pytest.mark.skipif('not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER"))', reason="reaches cobalt_dev (lock-relief G1)")
def test_a_correction_with_a_typed_price_names_its_source(world):
    response = client.post("/radar/card/1/correct", data={"leg_id": "401", "price": "5.39"})
    assert response.status_code == 200, response.text
    (name, args, kw), = world.calls
    assert (name, args) == ("record_correction", (401,))
    assert (kw["price"], kw["price_source"], kw["source"], kw["shares"]) == (Decimal("5.39"), "typed", "panel", None)


def test_a_correction_of_another_cards_leg_is_refused_before_the_writer(world, monkeypatch):
    """C3 fix r1 F2: the URL's card binds the leg — a leg that is not one
    of card 1's current legs is refused before `record_correction`."""
    monkeypatch.setattr(legs_module, "record_correction",
                        _raise(AssertionError("the writer was reached with another card's leg")))
    response = client.post("/radar/card/1/correct", data={"leg_id": "999", "price": "5.39"})
    assert response.status_code == 422, response.text
    reason = response.json()["reason"]
    assert "is not a current leg of card" in reason
    assert reason == ("REFUSED card 1: leg 999 is not a current leg of card 1 — reload the card. "
                      "Nothing written.")
    assert world.calls == []


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


def _filled_only(card_id: int):
    """A reader that fails the test (BaseException — never caught as a
    position error) on any read but the fixture's FILLED card, id 4."""
    if card_id != 4:
        pytest.fail(f"a position read for card {card_id}, which is not FILLED / CLOSED")
    return _position()


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


def _taps(fragment: str, card_id: int, path: str) -> list[str]:
    """The bodies of the tap blocks posting to `/radar/card/{card_id}{path}`
    — `<div data-card-tap>` on the panel, `<form>` on the sheet."""
    return [body for _tag, body in re.findall(
        rf'<(div|form) class="s3-form[^"]*" data-card-id="{card_id}" data-path="{re.escape(path)}"[^>]*>(.*?)</\1>',
        fragment, re.S,
    )]


def test_a_triggered_card_shows_last_entry_stop_and_a_filled_form_prefilled_from_last(evaluated):
    view = _view(evaluated["rows"], reader=_filled_only)
    card = next(c for c in view.active if c.state is CardState.TRIGGERED)
    fragment = _card_html(panel.render_ladder(view), card.id)
    assert "last 5.48" in fragment and f"entry {card.trigger}" in fragment and f"stop {card.stop}" in fragment
    assert "bar time not stored" in fragment
    (fill,) = _taps(fragment, 3, "/fill")
    assert re.search(r'<input[^>]*name="price"[^>]*value="5.48"', fill)
    assert _hidden(fill, "prefill") == ["5.48"]
    assert re.search(rf'<input[^>]*name="shares"[^>]*value="{card.shares}"', fill)
    assert "FILLED @" in fill
    assert len(_taps(fragment, 3, "/pass")) == 1
    assert "<form" not in fragment, "the panel posts by fetch only (focus law)"


def test_a_triggered_card_with_no_last_price_leaves_the_price_empty_never_the_entry(evaluated):
    rows = copy.deepcopy(evaluated["rows"])
    next(r for r in rows if r["state"] == "TRIGGERED")["last_price"] = None
    view = _view(rows, reader=_filled_only)
    card = next(c for c in view.active if c.state is CardState.TRIGGERED)
    fragment = _card_html(panel.render_ladder(view), card.id)
    assert re.search(r'<input[^>]*name="price"[^>]*value=""', fragment)
    assert _hidden(fragment, "prefill") == [""]
    assert not re.search(rf'name="price"[^>]*value="{card.trigger}"', fragment)


def test_an_armed_card_offers_the_triggered_tap(evaluated):
    view = _view(evaluated["rows"], reader=_filled_only)
    card = next(c for c in view.active if c.state is CardState.ARMED)
    assert len(_taps(_card_html(panel.render_ladder(view), card.id), card.id, "/triggered")) == 1


def test_in_trade_render_carries_every_control_and_the_running_it_posts(evaluated):
    legs = [_leg(), _leg(id=302, seq=1, kind="exit", shares=50, price=Decimal("5.40"), preset="half",
                         stop_in_force=Decimal("5.7000"))]
    view = _view(evaluated["rows"], reader=lambda card: _position(legs=legs, running=50, owner="yours"))
    card = next(c for c in view.active if c.state is CardState.FILLED)
    fragment = _card_html(panel.render_ladder(view), card.id)
    assert "running 50 sh" in fragment
    exits = {(_hidden(body, "preset") or [None])[0]: body for body in _taps(fragment, card.id, "/exit")}
    assert set(exits) == {"half", "third", "flat", "typed"}
    for preset, label in (("half", "½"), ("third", "⅓"), ("flat", "flat"), ("typed", "typed")):
        assert _hidden(exits[preset], "running_before") == ["50"], preset
        assert label in exits[preset]
    assert 'name="confirm" value="1"' in exits["flat"] and "✓" in exits["flat"]
    assert re.search(r'<input[^>]*name="price"[^>]*value="5.48"', exits["flat"]), "flat's price: prefilled, editable"
    assert 'name="shares"' in exits["typed"]
    (held,) = _taps(fragment, card.id, "/held")
    assert "HOLDING" in held and 'name="held"' in held
    # both legs listed; the estimated one carries a correct control, naming its leg
    assert "5.4800" in fragment and "5.40" in fragment and "estimated" in fragment
    corrections = _taps(fragment, card.id, "/correct")
    assert [_hidden(f, "leg_id") for f in corrections] == [["301"], ["302"]]
    assert "realized R 0.2500" in fragment and "provisional" in fragment
    assert "drift 27.00% vs P 20%" in fragment
    # the stop: his, YOURS, the delta; Cobalt's beside it; ↺ with its value; the per-leg gap
    assert '<span class="yours">YOURS</span>' in fragment
    assert f"Cobalt stop {card.structural_stop}" in fragment
    (reset,) = _taps(fragment, card.id, "/stop/reset")
    assert f"↺ {card.structural_stop}" in reset
    assert f"Δ {card.stop - card.structural_stop}" in fragment
    for in_force in (Decimal("5.8100"), Decimal("5.7000")):  # stop_in_force − structural_stop, per leg
        assert f"gap {in_force - card.structural_stop}" in fragment
    assert len(_taps(fragment, card.id, "/stop")) == 1
    assert "<form" not in fragment and 'method="post"' not in fragment


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


def test_the_panel_script_posts_every_card_tap(evaluated):
    js = panel.PANEL_JS
    assert "closest('[data-card-tap]')" in js and "querySelectorAll('input[name]')" in js
    assert "field.type==='checkbox'&&!field.checked" in js  # an unticked ✓ posts no confirm
    assert "post(block.dataset.cardId,block.dataset.path,body)" in js


# ---------------------------------------------------------------------
# C3-4 — the manual card's IN-TRADE controls on the sheet
# ---------------------------------------------------------------------


def test_the_sheet_renders_a_manual_cards_in_trade_controls_with_the_same_routes_and_no_reset():
    fragment = panel.render_in_trade(
        9, _position(owner="yours"), direction="long", stop=Decimal("9.90"), structural_stop=None,
        last=None, source="sheet",
    )
    assert 'method="post" action="/radar/card/9/exit"' in fragment and 'action="/radar/card/9/held"' in fragment
    assert len(_taps(fragment, 9, "/exit")) == 4 and 'type="submit"' in fragment
    assert _hidden(fragment, "source").count("sheet") == len(_hidden(fragment, "source")) > 0
    assert "↺" not in fragment and "/stop/reset" not in fragment
    assert "Cobalt stop NULL — no Cobalt stop" in fragment
    assert "gap NULL — no Cobalt stop" in fragment
    assert re.search(r'<input[^>]*name="price"[^>]*value=""', fragment), "no last price on the sheet: empty"


# ---------------------------------------------------------------------
# C3 fix r1 — F1: every tap has a status sink; F3 / F4: the sheet
# ---------------------------------------------------------------------

#: The CLOSED card added to the fixture's ladder (constructed, L32).
CLOSED_ID = 7


def _with_a_closed_card(evaluated) -> list[dict]:
    rows = copy.deepcopy(evaluated["rows"])
    closed = copy.deepcopy(next(r for r in rows if r["state"] == "FILLED"))
    closed.update(card_id=CLOSED_ID, state="CLOSED")
    return rows + [closed]


def _closed_legs():
    """A confirmed entry and one `estimated` flat exit (running 0)."""
    return [_leg(flag="confirmed", price_source="typed"),
            _leg(id=307, seq=1, kind="exit", price=Decimal("5.40"), preset="flat")]


def _closed_reader(card_id: int):
    if card_id == CLOSED_ID:
        return _position(legs=_closed_legs(), running=0)
    return _position()


def _terminal_block(rendered: str, card_id: int) -> str:
    start = rendered.index(f'<div class="terminal-legs" data-card-id="{card_id}"')
    end = re.search(r'<div class="terminal-row"|<h4>|</details>', rendered[start:])
    return rendered[start:start + end.start()] if end else rendered[start:]


def test_a_closed_cards_correction_has_a_status_sink(evaluated):
    view = _view(_with_a_closed_card(evaluated), reader=_closed_reader)
    block = _terminal_block(panel.render_ladder(view), CLOSED_ID)
    (correct,) = _taps(block, CLOSED_ID, "/correct")
    assert _hidden(correct, "leg_id") == ["307"]
    assert re.search(rf'<div class="card-status[^"]*" data-card-id="{CLOSED_ID}"', block), (
        f"card {CLOSED_ID}: its terminal ✓ correct has no status sink")


def test_every_card_tap_has_a_status_sink(evaluated):
    view = _view(_with_a_closed_card(evaluated), reader=_closed_reader)
    rendered = panel.render_ladder(view)
    tapped = set(re.findall(r'data-card-id="(\d+)" data-path="[^"]*" data-card-tap="1"', rendered))
    sinks = set(re.findall(r'class="card-status[^"]*" data-card-id="(\d+)"', rendered))
    assert str(CLOSED_ID) in tapped
    missing = sorted(tapped - sinks, key=int)
    assert not missing, f"card taps with no status sink: {missing}"


class SheetCards:
    """The sheet's card reads: no live card, one CLOSED manual card filled today."""

    def __init__(self, filled):
        self.filled = filled
        self.days = []

    def ensure_schema(self):
        return None

    def open_cards(self):
        return []

    def filled_with_picks(self, day):
        self.days.append(day)
        return copy.deepcopy(self.filled)


def test_the_sheet_lists_a_closed_manual_cards_estimated_leg(monkeypatch):
    filled = [{"transition_id": 71, "card_id": 9, "filled_at": AT, "ticker": "TEST", "state": "CLOSED",
               "origin": "manual", "pick_id": None}]
    cards = SheetCards(filled)
    monkeypatch.setattr(web_module, "CardStore", lambda *a, **k: cards)
    monkeypatch.setattr(panel, "read_in_trade", lambda card_id: _position(legs=_closed_legs(), running=0))
    section = web_module._open_cards_section()
    assert 'method="post" action="/radar/card/9/correct"' in section
    (correct,) = _taps(section, 9, "/correct")
    assert _hidden(correct, "leg_id") == ["307"] and _hidden(correct, "source") == ["sheet"]
    assert "/radar/card/9/exit" not in section, "a CLOSED card lists its estimated legs only"


def test_the_sheets_failed_position_read_keeps_the_structural_stop_line(monkeypatch):
    monkeypatch.setattr(panel, "read_in_trade", _raise(RuntimeError("legs offline")))
    fragment = web_module._sheet_in_trade(
        {"id": 9, "state": "FILLED", "origin": "manual", "direction": "long", "stop": Decimal("9.90")})
    assert "FAILED" in fragment and "position unreadable" in fragment
    assert "Cobalt stop NULL — no Cobalt stop" in fragment
    assert "/stop/reset" not in fragment
