"""X5 — card 61 RUN row, the card-write half of FINAL row X5 at BASE.

Two REAL sessions on one constructed radar card: session A runs
`tap_dot`'s transaction and, while it holds the card's row lock, session B
starts `refresh_radar_card` on the same card. Prints that both commit, the
order, B's taps-moved answer and the final row. Asserts nothing (L70). The
`seq` half is W1's test in the suite transaction (card `## RECORDS`).
Cleanup is X12 (iii)'s: every row deleted by id and proven gone.
"""

from __future__ import annotations

import threading
import time
from datetime import datetime, timedelta, timezone
from decimal import Decimal

from test_x12_transition_ids_db import REAL_CONNECT, _real, cleanup, real_radar_card, requires_db

from cobalt import db as _db

UTC = timezone.utc


class _PausedAfterLock:
    """A real connection that runs `on_lock()` right after its first
    `… FOR UPDATE` — session A paused while it holds the card lock."""

    def __init__(self, inner, on_lock):
        object.__setattr__(self, "_inner", inner)
        object.__setattr__(self, "_on_lock", on_lock)
        object.__setattr__(self, "_fired", False)

    def __getattr__(self, item):
        return getattr(self._inner, item)

    def __setattr__(self, key, value):
        setattr(self._inner, key, value)

    def execute(self, query, params=None, *args, **kwargs):
        result = self._inner.execute(query, params, *args, **kwargs)
        if "FOR UPDATE" in str(query) and not self._fired:
            object.__setattr__(self, "_fired", True)
            self._on_lock()
        return result


@requires_db
def test_x5_a_tap_and_a_refresh_on_one_card_both_commit(monkeypatch):
    from cobalt.aset.models import Grade
    from cobalt.cards.scoring import Dot
    from cobalt.cards.store import CardStore
    from cobalt.radar.evaluate import CardUpdate
    from cobalt.settings.card import ProposedKeyBands

    made: dict = {"pool": "f15_x5", "ticker": "X5TR"}
    events: list[str] = []
    out: dict = {}
    now = datetime(2026, 9, 3, 14, 0, tzinfo=UTC)
    try:
        real_radar_card(monkeypatch, made)
        card_id = made["card_id"]
        update = CardUpdate(
            card_id=card_id, proximity=Decimal("0.6"), conviction=None, card_score=None, score_suppressed=None,
            proposed_key=None, dots=[Dot(factor="setup_relation", position=0, source="human", tier="judgment",
                                          role="human")],
            health=None, radar_score_id=made["score_id"], tap_version=0, last_price=Decimal("5.40"),
        )

        def session_b():
            try:
                out["b_wrote_all"] = CardStore("cobalt_dev").refresh_radar_card(update, now=now + timedelta(seconds=2))
                events.append("B (refresh) committed")
            except Exception as e:  # noqa: BLE001 — the experiment prints what happened
                events.append(f"B (refresh) raised {type(e).__name__}: {e}")

        thread = threading.Thread(target=session_b)

        def on_lock():
            thread.start()
            time.sleep(1.0)
            out["b_waiting"] = thread.is_alive()

        opened = []
        original = CardStore._connect

        def connect(self, allow_prod=False):
            conn = original(self, allow_prod=allow_prod)
            if not opened:  # session A: the tap's own connection only
                opened.append(conn)
                return _PausedAfterLock(conn, on_lock)
            return conn

        monkeypatch.setattr(CardStore, "_connect", connect)
        bands = ProposedKeyBands(a_plus_min=Decimal("0.9"), a_min=Decimal("0.8"), b_min=Decimal("0.6"),
                                 c_min=Decimal("0.4"))
        try:
            out["a_result"] = CardStore("cobalt_dev").tap_dot(card_id, "setup_relation", 7, bands=bands,
                                                              enabled=[Grade.A, Grade.B, Grade.C],
                                                              now=now + timedelta(seconds=1))
            events.append("A (tap) committed")
        except Exception as e:  # noqa: BLE001
            events.append(f"A (tap) raised {type(e).__name__}: {e}")
        thread.join(timeout=30)
        monkeypatch.setattr(CardStore, "_connect", original)
        reader = REAL_CONNECT("cobalt_dev", side=_db.Side.USER)
        try:
            row = reader.execute(
                "SELECT proximity, last_price, conviction, card_score, score_suppressed, proposed_key "
                "FROM aset_sizings WHERE id = %s", (card_id,),
            ).fetchone()
            taps = reader.execute("SELECT count(*) FROM card_dot_taps WHERE card_id = %s", (card_id,)).fetchone()[0]
        finally:
            reader.close()
        print(f"X5: B waited on A's lock: {out.get('b_waiting')}")
        print(f"X5: events in order: {events}")
        print(f"X5: A (tap) returned {out.get('a_result')}")
        print(f"X5: B (refresh) wrote all (False = taps-moved branch): {out.get('b_wrote_all')}")
        print(f"X5: final row proximity/last_price/conviction/card_score/score_suppressed/proposed_key = {row}; "
              f"tap rows {taps}")
    finally:
        left = cleanup(made)
        print(f"X5: rows left after cleanup {left}")
