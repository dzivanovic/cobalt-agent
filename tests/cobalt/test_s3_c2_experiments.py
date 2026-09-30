"""S3 exits C2 — the first-gate experiments (v3 First-gate table; L70).

Run BEFORE any src edit, on the code at C1's checked tip. Each test is one
experiment row of the C2 build report (`## E1 EXPERIMENTS`): X21, X19,
X20 and X-OPEN (X-UR is a read, recorded in the report). Constructed
values only (L32): ticker `TEST` / `X21LK`, the design's own X20 card
(long, planned entry 10.00 / stop 9.90 / 100 sh, filled at 10.05).

X21 runs on the REAL `db.connect` (two real sessions, the X1 real-factory
pattern of `test_fill_transaction_db.py`): the rows it writes are deleted
by card id in `finally` and proven gone. X19 / X20 / X-OPEN run inside
the suite's rollback transaction with M1 applied there (`apply_0021`).
"""

from __future__ import annotations

import os
from datetime import datetime, timezone
from decimal import Decimal

import pytest

from cobalt import db as _db
from legs_db_support import apply_0021, card_row, fill_kwargs, patch_daymode, sizing

#: The UNPATCHED factory, bound at import (`dev_db_tx` patches per test).
REAL_CONNECT = _db.connect
X21LK = "X21LK"

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)


@pytest.fixture
def aset(monkeypatch):
    from cobalt.aset.store import AsetStore

    patch_daymode(monkeypatch)
    store = AsetStore("cobalt_dev")
    store.ensure_schema()
    apply_0021(store)
    return store


def _x20_filled(aset, *, shares: int = 66) -> int:
    """The design's X20 card: long, planned 10.00 / 9.90, $10 -> 100 sh;
    filled at 10.05 (recomputed_shares 66) for `shares`."""
    from cobalt.cards.models import Actor, CardState
    from cobalt.cards.store import CardStore

    card_id = aset.save(sizing(risk="10"))
    cards = CardStore(aset.db_name)
    cards.transition(card_id, CardState.ARMED, actor=Actor.YOU)
    cards.transition(card_id, CardState.TRIGGERED, actor=Actor.YOU)
    aset.mark_filled(card_id, **fill_kwargs(price="10.05", shares=shares, p=20))
    row = card_row(aset, card_id)
    assert (row["shares"], row["recomputed_shares"], row["state"]) == (100, 66, "FILLED")
    return card_id


# ---------------------------------------------------------------------
# X21 — does today's `record_stop_edit` hold the card lock past its
# SELECT … FOR UPDATE? Two real sessions.
# ---------------------------------------------------------------------


class _PausedAfterLock:
    """A real connection that runs `on_lock()` right after its first
    `… FOR UPDATE` statement — session A paused while it should hold the
    card lock."""

    def __init__(self, inner, on_lock):
        object.__setattr__(self, "_inner", inner)
        object.__setattr__(self, "_on_lock", on_lock)
        object.__setattr__(self, "_fired", False)

    def __getattr__(self, item):
        return getattr(self._inner, item)

    def __setattr__(self, key, value):
        setattr(self._inner, key, value)

    def __enter__(self):
        self._inner.__enter__()
        return self

    def __exit__(self, *exc):
        return self._inner.__exit__(*exc)

    def execute(self, query, params=None, *args, **kwargs):
        result = self._inner.execute(query, params, *args, **kwargs)
        if "FOR UPDATE" in str(query) and not self._fired:
            object.__setattr__(self, "_fired", True)
            self._on_lock()
        return result


def _real_read(sql, params):
    from cobalt import env

    conn = REAL_CONNECT(env.DEV_DB_NAME, side=_db.Side.USER)
    try:
        return conn.execute(sql, params).fetchall()
    finally:
        conn.close()


def x21_session_b_outcome(monkeypatch) -> str:
    """Run the X21 experiment; return what session B met: `acquired`
    (B did not wait — A's lock was already released) or `waits` (A still
    held the card lock). Cleans up every real row it wrote."""
    import psycopg

    from cobalt import env
    from cobalt.aset.engine import compute_sizing
    from cobalt.aset.models import Direction, Grade, SheetMode, SizingInput
    from cobalt.aset.store import AsetStore
    from cobalt.cards.store import CardStore

    assert _db.connect is not REAL_CONNECT, "the suite patches db.connect; this test undoes it"
    monkeypatch.setattr(_db, "connect", REAL_CONNECT)
    patch_daymode(monkeypatch)
    aset = AsetStore(env.DEV_DB_NAME)
    written: list[int] = []
    outcome: list[str] = []

    def session_b(card_id):
        def attempt():
            b = REAL_CONNECT(env.DEV_DB_NAME, side=_db.Side.USER)
            try:
                b.execute("SELECT id FROM aset_sizings WHERE id = %s FOR UPDATE NOWAIT", (card_id,))
                outcome.append("acquired")
            except psycopg.errors.LockNotAvailable:
                outcome.append("waits")
            finally:
                b.close()
        return attempt

    try:
        card_id = aset.save(compute_sizing(
            SizingInput(ticker=X21LK, grade=Grade.B, direction=Direction.LONG, sheet_mode=SheetMode.FULL,
                        risk_dollars=Decimal("10"), entry=Decimal("10.00"), stop=Decimal("9.90")),
            (Grade.A, Grade.B),
            Decimal("10"),
        ))
        written.append(card_id)
        cards = CardStore(aset.db_name)
        real_connect = CardStore._connect
        monkeypatch.setattr(
            CardStore, "_connect",
            lambda self, allow_prod=False: _PausedAfterLock(real_connect(self, allow_prod=allow_prod),
                                                            session_b(card_id)),
        )
        cards.record_stop_edit(card_id, from_stop=Decimal("9.90"), to_stop=Decimal("9.85"))
        monkeypatch.setattr(CardStore, "_connect", real_connect)
        (stop,), = _real_read("SELECT stop FROM aset_sizings WHERE id = %s", (card_id,))
        assert stop == Decimal("9.8500"), "the edit itself landed"
    finally:
        cleanup = REAL_CONNECT(env.DEV_DB_NAME, side=_db.Side.USER)
        try:
            cleanup.execute("DELETE FROM aset_sizings WHERE id = ANY(%s)", (written,))
        finally:
            cleanup.close()
        assert _real_read("SELECT count(*) FROM aset_sizings WHERE ticker = %s", (X21LK,))[0][0] == 0
    assert len(outcome) == 1, f"session B ran {len(outcome)} times"
    return outcome[0]


@requires_db
def test_x21_after_c2_session_b_waits_on_the_stop_edit_lock(monkeypatch):
    """E1 recorded today's result (B did NOT wait: `acquired`, commit
    80e0c8a2). After C2-6 the stop edit is ONE transaction holding the
    card lock to its commit, so B meets the lock."""
    assert x21_session_b_outcome(monkeypatch) == "waits"


# ---------------------------------------------------------------------
# X19 / X20 — today's FILLED stop edit (the live defect, v3 §5)
# ---------------------------------------------------------------------


@requires_db
def test_x20_after_c2_a_stop_between_planned_entry_and_fill_is_accepted(aset):
    """E1 recorded today: `SizingError` (the planned-entry side check).
    After C2: side-checked against the fill 10.05 — accepted."""
    from cobalt.cards.store import CardStore

    card_id = _x20_filled(aset)
    CardStore(aset.db_name).record_stop_edit(card_id, from_stop=Decimal("9.90"), to_stop=Decimal("10.02"))
    row = card_row(aset, card_id)
    assert row["stop"] == Decimal("10.0200")
    assert row["per_share_risk"] == Decimal("0.0300") and row["used_risk"] == Decimal("1.98"), "0.03 x 66 held"
    assert row["shares"] == 100


@requires_db
def test_x20_after_c2_used_risk_is_the_fill_distance_on_the_running_shares(aset):
    """E1 recorded today: 5.00 (0.05 x 100). After C2: 0.10 x running."""
    from cobalt.cards.store import CardStore

    card_id = _x20_filled(aset)
    CardStore(aset.db_name).record_stop_edit(card_id, from_stop=Decimal("9.90"), to_stop=Decimal("9.95"))
    row = card_row(aset, card_id)
    assert row["used_risk"] == Decimal("6.60"), "0.10 (fill 10.05 - 9.95) x 66 running"
    assert row["shares"] == 100, "aset_sizings.shares still 100"


@requires_db
def test_x19_after_c2_used_risk_is_priced_on_the_shares_he_holds(aset):
    """Filled 66 at a drifted 10.05; stop to 9.85. E1 recorded today:
    15.00 (|10.00 - 9.85| x 100 planned). After C2: 0.20 x 66 = 13.20."""
    from cobalt.cards.store import CardStore

    card_id = _x20_filled(aset, shares=66)
    CardStore(aset.db_name).record_stop_edit(card_id, from_stop=Decimal("9.90"), to_stop=Decimal("9.85"))
    row = card_row(aset, card_id)
    assert row["used_risk"] == Decimal("13.20")
    assert row["per_share_risk"] == Decimal("0.2000")


# ---------------------------------------------------------------------
# X-OPEN — R67 (4): an open position carries to the next day
# ---------------------------------------------------------------------

#: The next trading day after the suite's frozen instant (Thu 2026-09-03
#: 10:00 ET): Fri 2026-09-04 10:00 ET.
NEXT_DAY = datetime(2026, 9, 4, 14, 0, tzinfo=timezone.utc)


@requires_db
def test_x_open_a_filled_card_survives_the_session_boundary_and_one_expiry_cycle(aset):
    from cobalt.cards.expire import expire_due
    from cobalt.cards.store import CardStore

    card_id = _x20_filled(aset, shares=66)
    cards = CardStore(aset.db_name)
    moved = expire_due(cards, now=NEXT_DAY)
    assert card_id not in [m["card_id"] for m in moved], "the expiry cycle moved a FILLED card"
    assert card_row(aset, card_id)["state"] == "FILLED"
    assert cards.history(card_id)[-1]["to_state"] == "FILLED"
