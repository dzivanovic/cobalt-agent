"""S2-P2 STEP-6 routes: key tap (snap DOWN only, R8), pass, dot tap,
promote/release. Offline: the card store and the day-mode read are
replaced; dollars and ladders come from the hub-cut real-shape settings
fixture. The row-lock and ARM-invariant halves are the `requires_db` tests
in `test_radar_cards_db.py`.
"""

from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal

import pytest
from fastapi.testclient import TestClient

import radar_p2_support as sup
from cobalt.aset import web as web_module
from cobalt.cards import CardStateError
from cobalt.settings.models import TraderSettings

client = TestClient(web_module.app)
SETTINGS = TraderSettings._build(sup.fixture_settings_rows(), where="fixture")


class FakeCards:
    def __init__(self, state="WATCH"):
        self.state = state
        self.calls = []

    def radar_card(self, card_id):
        return {"id": card_id, "ticker": "FTFT", "direction": "short", "state": self.state, "origin": "radar",
                "entry": Decimal("5.50"), "stop": Decimal("5.81"), "proximity": Decimal("0.5"),
                "formed_at": datetime(2026, 1, 6, 16, 22, tzinfo=timezone.utc),
                "created_at": datetime(2026, 1, 6, 16, 30, tzinfo=timezone.utc),
                "tapped_grade": None, "sized_grade": None, "promoted_at": None}

    def tap_key(self, card_id, sizing, now=None):
        if self.state != "WATCH":
            raise CardStateError(f"REFUSED card {card_id}: the key is frozen in {self.state}")
        self.calls.append(("tap_key", sizing))
        return {"card_id": card_id, "tapped_grade": sizing.tapped_grade.value, "sized_grade": sizing.sized_grade.value,
                "shares": sizing.result.shares, "risk_budget": str(sizing.result.risk_budget),
                "snap_notice": sizing.snap_notice}

    def transition(self, card_id, to_state, **kw):
        self.calls.append(("transition", to_state.value, kw["actor"].value))
        return 77

    def tap_dot(self, card_id, factor, grade, *, bands, enabled, now=None):
        self.calls.append(("tap_dot", factor, grade, bands, [g.value for g in enabled]))
        return {"card_id": card_id, "factor": factor, "grade": grade, "card_score": 40}

    def set_promoted(self, card_id, promoted, now=None):
        self.calls.append(("promote", promoted))
        return {"card_id": card_id, "promoted": promoted}


@pytest.fixture
def cards(monkeypatch):
    fake = FakeCards()
    monkeypatch.setenv("COBALT_ALLOW_DEV_ENTRY", "1")
    monkeypatch.setattr(web_module, "CardStore", lambda: fake)
    monkeypatch.setattr(web_module, "load_sheet_modes_config", lambda: SETTINGS.sheet_modes)
    monkeypatch.setattr(web_module, "_daymode_state", lambda: {
        "cfg": SETTINGS.daymode, "mode": "reduced", "row": {"attested_sheet": "half.htk"}, "error": None,
    })
    notes = []
    monkeypatch.setattr(web_module, "save_card", lambda cfg, result, when=None, **kw: (notes.append((result, when)) or
                                                                                  ("note.md", when, None)))
    fake.notes = notes
    monkeypatch.setattr(web_module, "CardSettingsReader", lambda: type("R", (), {"current": lambda self: _card_settings()})())
    return fake


def _card_settings():
    from cobalt.settings.card import CardSettings

    return CardSettings.from_rows({"radar.cards_enabled": True,
                                   "card.proposed_key": {"a_plus_min": 0.9, "a_min": 0.8, "b_min": 0.6, "c_min": 0.4},
                                   "card.curves": {"rvol": [[1, 1], [3, 6]]}})


def test_a_plus_key_tap_on_the_half_day_records_a_plus_sizes_at_a_70_with_notice(cards):
    response = client.post("/radar/card/1/key", data={"grade": "A+"})
    assert response.status_code == 200, response.text
    body = response.json()
    assert body["tapped_grade"] == "A+" and body["sized_grade"] == "A" and body["risk_budget"] == "70.00"
    assert "A+" in body["snap_notice"] and "$70" in body["snap_notice"]
    sizing = cards.calls[0][1]
    assert sizing.result.input.entry == Decimal("5.50") and sizing.result.input.stop == Decimal("5.81")
    # the daily-note block is bound to the card's stable unit (its creation instant), not the tap time
    assert cards.notes and cards.notes[0][1] == datetime(2026, 1, 6, 16, 30, tzinfo=timezone.utc)


def test_nothing_enabled_below_is_a_409_with_the_reason_and_no_write(cards, monkeypatch):
    daymode = SETTINGS.daymode.model_copy(update={"reduced_enabled_grades": [SETTINGS.daymode.reduced_enabled_grades[0]]})
    monkeypatch.setattr(web_module, "_daymode_state", lambda: {
        "cfg": daymode, "mode": "reduced", "row": {"attested_sheet": "half.htk"}, "error": None,
    })
    response = client.post("/radar/card/1/key", data={"grade": "B"})
    assert response.status_code == 409
    assert "nothing enabled below" in response.json()["reason"]
    assert cards.calls == [] and cards.notes == []


def test_key_tap_refused_once_armed(cards):
    cards.state = "ARMED"
    response = client.post("/radar/card/1/key", data={"grade": "A"})
    assert response.status_code == 409 and "frozen in ARMED" in response.json()["reason"]
    assert cards.notes == []


def test_the_hotkey_file_mismatch_refusal_is_unchanged(cards, monkeypatch):
    monkeypatch.setattr(web_module, "_daymode_state", lambda: {
        "cfg": SETTINGS.daymode, "mode": "reduced", "row": {"attested_sheet": "full.htk"}, "error": None,
    })
    response = client.post("/radar/card/1/key", data={"grade": "A"})
    assert response.status_code == 409 and "reload half.htk" in response.json()["reason"]
    assert cards.calls == []


def test_pass_moves_watch_to_passed_by_you(cards):
    response = client.post("/radar/card/1/key", data={"grade": "pass"})
    assert response.status_code == 200
    assert cards.calls == [("transition", "PASSED", "you")]


def test_a_bad_key_is_refused(cards):
    assert client.post("/radar/card/1/key", data={"grade": "Z"}).status_code == 422


def test_dot_tap_recomputes_with_the_bands_and_todays_enabled_grades(cards):
    response = client.post("/radar/card/1/dot/trail_fit", data={"grade": "7"})
    assert response.status_code == 200 and response.json()["card_score"] == 40
    _, factor, grade, bands, enabled = cards.calls[0]
    assert (factor, grade) == ("trail_fit", 7) and bands.a_min == Decimal("0.8") and enabled == ["A", "B", "C"]
    assert client.post("/radar/card/1/dot/trail_fit", data={"grade": "11"}).status_code == 422


def test_promote_and_release_routes(cards):
    assert client.post("/radar/card/1/promote").json() == {"card_id": 1, "promoted": True}
    assert client.post("/radar/card/1/release").json() == {"card_id": 1, "promoted": False}
    assert cards.calls == [("promote", True), ("promote", False)]


def test_card_routes_refuse_a_dev_instance_without_the_opt_in(cards, monkeypatch):
    monkeypatch.delenv("COBALT_ALLOW_DEV_ENTRY")
    assert client.post("/radar/card/1/key", data={"grade": "A"}).status_code == 403
    assert cards.calls == []
