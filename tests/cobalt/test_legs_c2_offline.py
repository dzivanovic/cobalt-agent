"""S3 exits C2 fix r1, offline: CLOSED is written only by the zero-running
leg (v3 §2 — the sheet's move route and `cobalt cards move` refuse it, the
shape of C1's two FILLED refusals), and the fill cache has ONE writer (L3,
v3 Q4 [F-04]).

Constructed values only (L32).
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pytest

SRC = Path(__file__).resolve().parents[2] / "src" / "cobalt"


# ---------------------------------------------------------------------
# F1 — CLOSED only by the zero-running leg
# ---------------------------------------------------------------------


def test_the_move_route_closes_only_through_the_zero_running_leg(monkeypatch):
    """aset-interim-close S3 (his R13) changed this pin: the sheet's CLOSE
    no longer refuses. It writes ONE flat exit leg through `legs.record_exit`,
    whose `_close_if_zero` writes FILLED -> CLOSED — the route itself never
    writes CLOSED (the C2 rule stands: CLOSED only by the zero-running leg)."""
    from decimal import Decimal

    from fastapi.testclient import TestClient

    from cobalt.aset import web as web_module
    from cobalt.cards import legs

    monkeypatch.setenv("COBALT_ALLOW_DEV_ENTRY", "1")

    class Cards:
        def ensure_schema(self):
            pass

        def state_of(self, card_id):
            from cobalt.cards.models import CardState

            return CardState.FILLED

        def transition(self, *a, **k):
            raise AssertionError("the move route must never write CLOSED")

    entry = {"id": 70, "seq": 0, "kind": "entry", "shares": 5, "price": Decimal("7.2500"),
             "flag": "confirmed", "price_source": "typed"}
    position = legs.Position(
        card={"id": 7, "state": "FILLED"}, legs=[entry],
        running=legs.Running(5, legs.BASIS_LEGS, 5, 0, 70, Decimal("7.2500"), "FILLED"),
        realized=legs.RealizedR(legs.REALIZED_R_ID, None, False, None, "constructed"),
    )
    exits = []

    def record_exit(card_id, **kwargs):
        exits.append((card_id, kwargs["preset"], kwargs["running_before"]))
        return legs.ExitResult(71, 5, 5, 0, True, 72)

    monkeypatch.setattr(legs, "read_position", lambda card_id: position)
    monkeypatch.setattr(legs, "record_exit", record_exit)
    monkeypatch.setattr(web_module, "_leg_note", lambda *a, **k: None)
    monkeypatch.setattr(web_module, "CardStore", Cards)
    monkeypatch.setattr(web_module, "_render",
                        lambda banner="", result="", form=None: banner + result)
    r = TestClient(web_module.app).post("/card/7/move", data={"to": "CLOSED"})
    assert "this route never closes" not in r.text, r.text
    assert exits == [(7, "flat", 5)], "CLOSED comes from the one flat exit leg"
    assert "FAILED" not in r.text and "must never" not in r.text


def test_the_cli_refuses_closed(monkeypatch):
    from cobalt.cards import cli

    class Store:
        def state_of(self, card_id):
            from cobalt.cards.models import CardState

            return CardState.FILLED

        def transition(self, *a, **k):
            raise AssertionError("the CLI must never write CLOSED")

    monkeypatch.setattr(cli, "_store", lambda: Store())
    with pytest.raises(SystemExit, match="never closes"):
        cli.cmd_move(argparse.Namespace(card_id=7, to="CLOSED", actor="you", reason=None))


# ---------------------------------------------------------------------
# F2 — ONE writer of the fill cache
# ---------------------------------------------------------------------


def test_the_fill_cache_has_one_writer():
    hits = [
        f"{path.relative_to(SRC)}:{n}: {line.strip()}"
        for path in sorted(SRC.rglob("*.py"))
        for n, line in enumerate(path.read_text().splitlines(), start=1)
        if "actual_fill = %s" in line
    ]
    assert len(hits) == 1, hits
    assert hits[0].startswith("aset/store.py:"), hits
