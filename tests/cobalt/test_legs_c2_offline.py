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


def test_the_move_route_refuses_closed(monkeypatch):
    from fastapi.testclient import TestClient

    from cobalt.aset import web as web_module

    monkeypatch.setenv("COBALT_ALLOW_DEV_ENTRY", "1")

    class Cards:
        def ensure_schema(self):
            pass

        def state_of(self, card_id):
            from cobalt.cards.models import CardState

            return CardState.FILLED

        def transition(self, *a, **k):
            raise AssertionError("the move route must never write CLOSED")

    monkeypatch.setattr(web_module, "CardStore", Cards)
    monkeypatch.setattr(web_module, "_render",
                        lambda banner="", result="", form=None: banner + result)
    r = TestClient(web_module.app).post("/card/7/move", data={"to": "CLOSED"})
    assert "FAILED" in r.text and "this route never closes" in r.text
    assert "must never" not in r.text


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
