"""S3 exits C3 — the first-gate experiments (v3 First-gate table; L70).

Run BEFORE any src edit, on the code at C2's checked tip (`5e77800f`).
Each test is one experiment row of the C3 build report (`## E1
EXPERIMENTS`): X5 and X-M (X6-R is a read, recorded in the report).

With-DB, inside the suite's rolled-back `cobalt_dev` transaction. The
radar card is the one the S2-P2 `world` fixture's evaluator makes
(`test_radar_cards_db.py`: synthetic ticker `ZZPB`, the hub-cut real-shape
bars); the manual card is `legs_db_support.manual_card` (ticker `TEST`,
the design's 10.0000 / 9.9000). Constructed values only (L32).
"""

from __future__ import annotations

import os
from datetime import datetime, timezone

import pytest

from legs_db_support import apply_0021, fill_kwargs, manual_card, patch_daymode
from test_radar_cards_db import SCAN0, TICKER, world  # noqa: F401  (the fixture)

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)

#: The next trading day after the suite's frozen instant (Thu 2026-09-03
#: 10:00 ET): Fri 2026-09-04 10:00 ET — C2's X-OPEN instant.
NEXT_DAY = datetime(2026, 9, 4, 14, 0, tzinfo=timezone.utc)


def _triggered_radar_card(world) -> int:  # noqa: F811
    """The evaluator's WATCH card, key-tapped (A+ → A), ARMED and TRIGGERED
    by his taps, with its creation day pinned to the scan's (2026-01-06)."""
    from decimal import Decimal

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
    cards.transition(card_id, CardState.TRIGGERED, actor=Actor.YOU)
    with cards._connect() as conn:
        conn.execute("UPDATE aset_sizings SET created_at = %s WHERE id = %s", (SCAN0, card_id))
    return card_id


# ---------------------------------------------------------------------
# X5 — does the expiry caller pass a TRIGGERED radar card past its window?
# ---------------------------------------------------------------------


@requires_db
def test_x5_a_triggered_radar_card_past_its_window_is_expired_by_one_expiry_cycle(world):  # noqa: F811
    from cobalt.cards import CardState
    from cobalt.cards.expire import expire_due

    card_id = _triggered_radar_card(world)
    cards = world["cards"]
    with cards._connect() as conn:
        expires_at = conn.execute("SELECT expires_at FROM aset_sizings WHERE id = %s", (card_id,)).fetchone()[0]
    assert expires_at is not None and expires_at < NEXT_DAY, "the card's window has passed"
    assert cards.state_of(card_id) is CardState.TRIGGERED

    moved = expire_due(cards, now=NEXT_DAY)

    row = next((m for m in moved if m["card_id"] == card_id), None)
    assert row is not None, "X5: the expiry caller skipped the TRIGGERED radar card"
    assert row["from_state"] == "TRIGGERED"
    assert cards.state_of(card_id) is CardState.EXPIRED
    last = cards.history(card_id)[-1]
    assert (last["from_state"], last["to_state"], last["actor"]) == ("TRIGGERED", "EXPIRED", "cobalt")


# ---------------------------------------------------------------------
# X-M — does `/radar` render a FILLED manual card?
# ---------------------------------------------------------------------


@requires_db
def test_x_m_the_radar_ladder_read_does_not_carry_a_filled_manual_card(monkeypatch):
    from cobalt.aset.store import AsetStore
    from cobalt.cards.store import CardStore
    from cobalt.session import clock, session_clock

    patch_daymode(monkeypatch)
    aset = AsetStore("cobalt_dev")
    aset.ensure_schema()
    apply_0021(aset)
    card_id = manual_card(aset)
    aset.mark_filled(card_id, **fill_kwargs(price="10.10", shares=100, p=20))
    cards = CardStore(aset.db_name)
    assert cards.state_of(card_id).value == "FILLED"

    rows = cards.radar_board_cards(session_clock().to_et(clock.now_utc()).date())
    assert card_id not in [r["card_id"] for r in rows], "X-M: /radar renders the FILLED manual card"
    assert card_id in [c["id"] for c in cards.open_cards()], "the sheet's open-cards read carries it"
