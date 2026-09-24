"""C8 — `set_card_stop` extracted from the `/card/{id}/stop` route (FINAL [F-06]).

THE PIN FIRST. The route's rendered output for a constructed open card, a
refused (not-open) card, a bad decimal, the dev-entry refusal and a store
refusal — captured on the base (`04b05cd4`) as the literal strings below
and asserted byte-identical after the extraction. `_render` is replaced
by a recorder, so the pin is exactly what the route hands the page shell
(C12 adds the widget to that shell by design).

Then the shared function: the route and the voice act both call ONE
`set_card_stop(card_id, to_stop)` — the entry guard, the open-card lookup,
the `Decimal` parse and `CardStore.record_stop_edit` (which recomputes
shares / per-share risk through the EXISTING engine, FINAL [F-26]).
"""

from __future__ import annotations

from decimal import Decimal

import pytest
from fastapi.testclient import TestClient

from cobalt.aset import web as web_module
from cobalt.cards import CardStateError

client = TestClient(web_module.app)

OPEN = [{"id": 11, "ticker": "XYZ", "direction": "long", "state": "WATCH", "stop": Decimal("4.4000"),
         "entry": Decimal("4.6000"), "shares": 250, "grade": "B"}]


class FakeCards:
    edits: list = []
    refuse: str | None = None

    def __init__(self, db_name=None):
        pass

    def ensure_schema(self):
        pass

    def open_cards(self):
        return list(OPEN)

    def record_stop_edit(self, card_id, *, from_stop, to_stop):
        if FakeCards.refuse:
            raise CardStateError(FakeCards.refuse)
        FakeCards.edits.append((card_id, from_stop, to_stop))
        return 501


@pytest.fixture
def pinned(monkeypatch):
    FakeCards.edits = []
    FakeCards.refuse = None
    monkeypatch.setattr(web_module, "CardStore", FakeCards)
    monkeypatch.setattr(web_module, "_render",
                        lambda banner="", result="", form=None: f"BANNER={banner!r}|RESULT={result!r}|FORM={form!r}")
    monkeypatch.setenv("COBALT_ALLOW_DEV_ENTRY", "1")


# --- THE PIN (strings captured on the base) -------------------------------------------

PIN_OK = ("BANNER='<div class=\"saved\">card 11: stop 4.4000 → 4.50 (YOURS — not a state change; "
          "it rides in the next transition\\'s evidence)</div>'|RESULT=''|FORM=None")
PIN_NOT_OPEN = "BANNER='<div class=\"failed\">FAILED\\ncard 99 is not open — its stop is settled.</div>'|RESULT=''|FORM=None"
PIN_BAD_DECIMAL = ("BANNER='<div class=\"failed\">FAILED\\n[&lt;class &#x27;decimal.ConversionSyntax&#x27;&gt;]"
                   "</div>'|RESULT=''|FORM=None")
PIN_DEV_REFUSED = ("BANNER='<div class=\"failed\">FAILED\\nRefused: this is a DEV instance (no COBALT_ENV=production). "
                   "Set COBALT_ALLOW_DEV_ENTRY=1 on this process to allow ticker fetch / sizing / fill here — "
                   "otherwise use the production sheet.</div>'|RESULT=''|FORM=None")
PIN_STORE_REFUSED = ("BANNER='<div class=\"failed\">FAILED\\nREFUSED: constructed store refusal</div>'"
                     "|RESULT=''|FORM=None")


def test_pin_a_constructed_open_card(pinned):
    r = client.post("/card/11/stop", data={"stop": "4.50"})
    assert r.text == PIN_OK
    assert FakeCards.edits == [(11, Decimal("4.4000"), Decimal("4.50"))]


def test_pin_a_card_that_is_not_open(pinned):
    assert client.post("/card/99/stop", data={"stop": "4.50"}).text == PIN_NOT_OPEN
    assert FakeCards.edits == []


def test_pin_a_bad_decimal(pinned):
    assert client.post("/card/11/stop", data={"stop": "four fifty"}).text == PIN_BAD_DECIMAL
    assert FakeCards.edits == []


def test_pin_the_dev_entry_refusal(pinned, monkeypatch):
    monkeypatch.delenv("COBALT_ALLOW_DEV_ENTRY", raising=False)
    assert client.post("/card/11/stop", data={"stop": "4.50"}).text == PIN_DEV_REFUSED
    assert FakeCards.edits == []


def test_pin_a_store_refusal(pinned):
    FakeCards.refuse = "REFUSED: constructed store refusal"
    assert client.post("/card/11/stop", data={"stop": "4.50"}).text == PIN_STORE_REFUSED


# --- the shared function ------------------------------------------------------------------


def test_set_card_stop_is_the_one_function_and_returns_the_write(pinned):
    from cobalt.aset.card_stop import set_card_stop

    out = set_card_stop(11, "4.50")
    assert (out.card_id, out.from_stop, out.to_stop, out.stop_edit_id) == (11, Decimal("4.4000"), Decimal("4.50"), 501)
    assert FakeCards.edits == [(11, Decimal("4.4000"), Decimal("4.50"))]


def test_set_card_stop_raises_what_the_route_renders(pinned, monkeypatch):
    from decimal import InvalidOperation

    from cobalt.aset.card_stop import set_card_stop

    with pytest.raises(CardStateError):
        set_card_stop(99, "4.50")
    with pytest.raises(InvalidOperation):
        set_card_stop(11, "four fifty")
    monkeypatch.delenv("COBALT_ALLOW_DEV_ENTRY", raising=False)
    with pytest.raises(web_module.DevEntryRefused):
        set_card_stop(11, "4.50")
    assert FakeCards.edits == []


# --- the voice act ([F-09]): re-read, re-hash, then the ONE function ---------------------


def _pending(to="4.50"):
    from datetime import datetime, timezone

    from cobalt.voice import tools as tl

    return tl.stop_dry_run(OPEN[0], Decimal(to), ttl_s=60, now=datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc))


def test_execute_rechecks_and_writes_once(pinned):
    from cobalt.voice import tools as tl

    edit = tl.execute_stop(_pending())
    assert edit.stop_edit_id == 501
    assert FakeCards.edits == [(11, Decimal("4.4000"), Decimal("4.50"))]


def test_a_target_that_changed_is_refused_with_the_new_readback(pinned, monkeypatch):
    from cobalt.voice import tools as tl

    p = _pending()
    monkeypatch.setitem(OPEN[0], "stop", Decimal("4.4200"))  # the sheet moved it in between
    try:
        with pytest.raises(tl.TargetChanged) as e:
            tl.execute_stop(p)
    finally:
        OPEN[0]["stop"] = Decimal("4.4000")
    assert FakeCards.edits == []
    assert e.value.new.from_stop == "4.42" and e.value.new.to_stop == "4.50"
    assert "from 4.42 to 4.50" in e.value.new.readback


def test_a_changed_card_state_alone_refuses_the_act(pinned, monkeypatch):
    """A2 (voice-v1-check-a-2026-09-24.md FOR THE CLASSIFIER 2; FINAL :90
    [F-09]): only the card's STATE moves between the read-back and the
    confirm — the stop is unchanged, so `diff_sha256` is unchanged and only
    the `target_sha256` clause (tools.execute_stop) can refuse it."""
    from cobalt.voice import tools as tl

    p = _pending()
    monkeypatch.setitem(OPEN[0], "state", "ARMED")  # the sheet moved the card, not its stop
    with pytest.raises(tl.TargetChanged) as e:
        tl.execute_stop(p)
    assert FakeCards.edits == []
    assert e.value.new.diff_sha256 == p.diff_sha256, "the change itself is identical"
    assert e.value.new.target_sha256 != p.target_sha256
    assert e.value.new.card_state == "ARMED" and "from 4.40 to 4.50" in e.value.new.readback


def test_a_card_that_closed_is_refused(pinned, monkeypatch):
    from cobalt.voice import tools as tl

    p = _pending()
    monkeypatch.setattr(FakeCards, "open_cards", lambda self: [])
    with pytest.raises(CardStateError):
        tl.execute_stop(p)
    assert FakeCards.edits == []


def test_in_dev_the_entry_guard_refuses_the_act_and_says_why(pinned, monkeypatch):
    from cobalt.voice import tools as tl

    monkeypatch.delenv("COBALT_ALLOW_DEV_ENTRY", raising=False)
    with pytest.raises(web_module.DevEntryRefused) as e:
        tl.execute_stop(_pending())
    assert "COBALT_ALLOW_DEV_ENTRY=1" in str(e.value)
    assert FakeCards.edits == []


def test_the_voice_act_reaches_the_card_only_through_set_card_stop():
    import inspect

    from cobalt.voice import tools as tl

    src = inspect.getsource(tl)
    assert "set_card_stop(" in src and "record_stop_edit(" not in src  # a CALL; docstrings may name it


def test_the_route_body_calls_set_card_stop_and_is_not_a_copy():
    import inspect

    from cobalt.aset import card_stop

    route_src = inspect.getsource(web_module.card_stop)
    assert "set_card_stop(" in route_src
    assert "record_stop_edit" not in route_src and "open_cards" not in route_src
    fn_src = inspect.getsource(card_stop.set_card_stop)
    assert "_check_entry_allowed()" in fn_src and "record_stop_edit(" in fn_src
    # `_check_entry_allowed` is IMPORTED, never moved or copied (the prompt's rule)
    assert "def _check_entry_allowed" not in inspect.getsource(card_stop)
    assert "def _check_entry_allowed" in inspect.getsource(web_module)
