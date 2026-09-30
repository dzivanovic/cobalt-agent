"""S-FILL as built — `AsetStore.mark_filled` is THE fill (v3 §2 [F-22]).

With-DB, inside the suite's rollback transaction, with M1 applied there
(`legs_db_support.apply_0021`). The drift P comes from a CONSTRUCTED
settings store (L69) — never his `trader_settings` value. The day-mode
config is the offline fixture the sheet tests use (sheets half/full,
reduced -> half), so `half.htk` is the matching attestation.

X1 runs on a connection factory that behaves like the real one
(`db.py` opens `autocommit=True`): every statement on a connection still
in autocommit is committed the moment it runs. A fill path that forgot
`conn.autocommit = False`, or that spanned two connections, leaves its
first writes behind when the cache UPDATE fails — the X1 red.
"""

from __future__ import annotations

import itertools
import os
from decimal import Decimal

import pytest

from cobalt import db as _db
from legs_db_support import STOP, apply_0021, card_row, fill_kwargs, legs_of, manual_card, patch_daymode

#: The UNPATCHED factory, bound at import (conftest's `REAL_CONNECT`, the
#: `test_voice_store.py` precedent): `dev_db_tx` patches `db.connect` per
#: test, and collection runs before it.
REAL_CONNECT = _db.connect
X1RF = "X1RF"

pytestmark = pytest.mark.skipif(
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


def _fill(aset, card_id, *, price="10.0270", shares=77, p=20, **over):
    kwargs = fill_kwargs(price="1" if price is None else price, shares=shares, p=p, **over)
    if price is None:
        kwargs["price"] = None
    return aset.mark_filled(card_id, **kwargs)


def _attest(aset, filename):
    from cobalt.daymode.store import DayModeStore
    from cobalt.session import clock, session_clock

    DayModeStore(aset.db_name).attest_sheet(
        session_clock().to_et(clock.now_utc()).date(), filename=filename, account_mode="sim"
    )


def _history(aset, card_id):
    from cobalt.cards.store import CardStore

    return [h["to_state"] for h in CardStore(aset.db_name).history(card_id)]


def _picks(aset, card_id):
    with aset._connect() as conn:
        return conn.execute("SELECT count(*) FROM picks WHERE card_id = %s", (card_id,)).fetchone()[0]


# ---------------------------------------------------------------------
# The fill, its entry leg and the cache commit together
# ---------------------------------------------------------------------


def test_a_fill_writes_the_transition_the_entry_leg_and_the_cache_together(aset):
    card = manual_card(aset)
    out = _fill(aset, card, price="10.0270", shares=77, p=20)

    assert _history(aset, card)[-1] == "FILLED"
    row = card_row(aset, card)
    assert row["state"] == "FILLED"
    assert row["actual_fill"] == Decimal("10.0270")
    assert row["distance_change_pct"] == Decimal("27.00")
    assert row["recomputed_shares"] == out.recompute.recomputed_shares
    assert row["drift_warning_pct"] == Decimal("20.00") and row["drift_warned"] is True

    (leg,) = legs_of(aset, card)
    assert leg["id"] == out.leg_id
    assert (leg["kind"], leg["seq"], leg["shares"], leg["price"]) == ("entry", 0, 77, Decimal("10.0270"))
    assert (leg["flag"], leg["price_source"], leg["source"]) == ("confirmed", "typed", "sheet")
    assert leg["running_before"] == 0 and leg["corrects"] is None and leg["preset"] is None
    assert leg["stop_in_force"] == STOP, "the card's stop read under the lock"
    assert leg["account_mode"] == row["account_mode"] and leg["session"] == "rth"


def test_x1_a_failing_cache_update_rolls_the_whole_fill_back_on_an_autocommit_factory(aset, monkeypatch):
    from cobalt import db
    from cobalt.aset.store import AsetStore

    card = manual_card(aset)
    before = _history(aset, card)

    suite_connect = db.connect
    settled = itertools.count()

    class Autocommitting:
        """The real factory's shape: autocommit until told otherwise."""

        def __init__(self, inner):
            self._inner = inner
            self._auto = True
            self._base = inner._name

        def __getattr__(self, item):
            return getattr(self._inner, item)

        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return self._inner.__exit__(*exc)

        @property
        def autocommit(self):
            return self._auto

        @autocommit.setter
        def autocommit(self, value):
            self._auto = bool(value)

        def _settle(self):
            if self._auto:  # the statement is durable the moment it ran
                self._inner.commit()
                self._inner.__init__(self._inner._conn, f"{self._base}_ac{next(settled)}")

        def execute(self, *a, **k):
            result = self._inner.execute(*a, **k)
            self._settle()
            return result

        def cursor(self, *a, **k):
            outer = self
            cur = self._inner.cursor(*a, **k)

            class Cur:
                def __enter__(self):
                    return self

                def __exit__(self, *exc):
                    return cur.__exit__(*exc)

                def __getattr__(self, item):
                    return getattr(cur, item)

                def execute(self, *a, **k):
                    result = cur.execute(*a, **k)
                    outer._settle()
                    return result

            return Cur()

    monkeypatch.setattr(db, "connect", lambda *a, **k: Autocommitting(suite_connect(*a, **k)))

    def broken_cache(self, conn, *args, **kwargs):
        conn.execute("UPDATE aset_sizings SET no_such_column = 1")

    monkeypatch.setattr(AsetStore, "_update_fill_cache", broken_cache)
    with pytest.raises(Exception, match="no_such_column"):
        _fill(aset, card)
    monkeypatch.setattr(db, "connect", suite_connect)

    assert _history(aset, card) == before, "no FILLED transition row"
    assert card_row(aset, card)["state"] == "TRIGGERED"
    assert legs_of(aset, card) == [], "no entry leg"
    assert _picks(aset, card) == 0, "no pick"
    assert card_row(aset, card)["actual_fill"] is None


def _real_read(sql, params):
    """One statement on a FRESH real connection — what another session sees."""
    from cobalt import env

    conn = REAL_CONNECT(env.DEV_DB_NAME, side=_db.Side.USER)
    try:
        return conn.execute(sql, params).fetchall()
    finally:
        conn.close()


def test_x1_real_factory_a_failing_cache_update_rolls_the_whole_fill_back(monkeypatch):
    """X1 on the REAL `db.connect` (fix r1 F1): no wrapper, no savepoint
    proxy — every connection the test and the stores open is a real
    autocommit connection to `cobalt_dev`, so a write outside the fill's
    one transaction would be durable and visible here.

    Runs at the real `0021` (with-DB pass 2); the rows it writes are
    deleted by card id in `finally` and proven gone.
    """
    from cobalt import env
    from cobalt.aset.engine import compute_sizing
    from cobalt.aset.models import Direction, Grade, SheetMode, SizingInput
    from cobalt.aset.store import AsetStore
    from cobalt.cards.models import Actor, CardState
    from cobalt.cards.store import CardStore
    from legs_db_support import ENTRY

    assert _db.connect is not REAL_CONNECT, "the suite patches db.connect; this test undoes it"
    monkeypatch.setattr(_db, "connect", REAL_CONNECT)
    patch_daymode(monkeypatch)
    aset = AsetStore(env.DEV_DB_NAME)
    cards = CardStore(aset.db_name)

    def triggered_card() -> int:
        card_id = aset.save(compute_sizing(
            SizingInput(ticker=X1RF, grade=Grade.B, direction=Direction.LONG,
                        sheet_mode=SheetMode.FULL, risk_dollars=Decimal("60"), entry=ENTRY, stop=STOP),
            (Grade.A, Grade.B),
            Decimal("10"),
        ))
        written.append(card_id)
        cards.transition(card_id, CardState.ARMED, actor=Actor.YOU)
        cards.transition(card_id, CardState.TRIGGERED, actor=Actor.YOU)
        return card_id

    def seen(card_id):
        (state, actual_fill), = _real_read(
            "SELECT state, actual_fill FROM aset_sizings WHERE id = %s", (card_id,))
        filled = _real_read(
            "SELECT count(*) FROM card_transitions WHERE card_id = %s AND to_state = 'FILLED'", (card_id,))[0][0]
        legs = _real_read("SELECT count(*) FROM legs WHERE card_id = %s", (card_id,))[0][0]
        picks = _real_read("SELECT count(*) FROM picks WHERE card_id = %s", (card_id,))[0][0]
        return dict(state=state, actual_fill=actual_fill, filled_rows=filled, legs=legs, picks=picks)

    written: list[int] = []
    try:
        failing = triggered_card()
        control = triggered_card()

        # (b) the cache UPDATE fails -> the fill raises, and a fresh real
        # connection sees nothing of it. Run before the control so that a
        # fill path writing outside its transaction is named by what it
        # left behind (the transition row, the leg), not by the control.
        before = seen(failing)
        assert before == dict(state="TRIGGERED", actual_fill=None, filled_rows=0, legs=0, picks=0)
        real_cache = AsetStore._update_fill_cache

        def broken_cache(self, conn, *args, **kwargs):
            conn.execute("UPDATE aset_sizings SET no_such_column = 1")

        monkeypatch.setattr(AsetStore, "_update_fill_cache", broken_cache)
        with pytest.raises(Exception) as raised:
            aset.mark_filled(failing, **fill_kwargs(price="10.0270", shares=77, p=20))
        monkeypatch.setattr(AsetStore, "_update_fill_cache", real_cache)

        after = seen(failing)
        assert after["filled_rows"] == 0, f"a FILLED transition row survived the failed fill: {after}"
        assert after["legs"] == 0, f"an entry leg survived the failed fill: {after}"
        assert after["state"] == "TRIGGERED", f"the card left TRIGGERED: {after}"
        assert after["picks"] == before["picks"], f"a pick survived the failed fill: {after}"
        assert after["actual_fill"] is None, f"the fill cache survived the failed fill: {after}"
        assert "no_such_column" in str(raised.value), raised.value

        # (a) CONTROL — the same fill of an identical card, real factory,
        # nothing broken: every assertion above, inverted.
        out = aset.mark_filled(control, **fill_kwargs(price="10.0270", shares=77, p=20))
        done = seen(control)
        assert done["state"] == "FILLED" and done["filled_rows"] == 1 and done["legs"] == 1
        assert done["actual_fill"] == Decimal("10.0270")
        assert out.result.pick_recorded, f"the control fill wrote no pick: {out.result.pick_error}"
        assert done["picks"] == 1, "a manual card's real fill writes one pick — the count (b) did not grow"
    finally:
        cleanup = REAL_CONNECT(env.DEV_DB_NAME, side=_db.Side.USER)
        try:
            for table in ("legs", "picks"):
                cleanup.execute(f"DELETE FROM {table} WHERE card_id = ANY(%s)", (written,))
            cleanup.execute("DELETE FROM aset_sizings WHERE id = ANY(%s)", (written,))
        finally:
            cleanup.close()
        assert _real_read("SELECT count(*) FROM aset_sizings WHERE ticker = %s", (X1RF,))[0][0] == 0
        assert _real_read(
            "SELECT count(*) FROM legs l JOIN aset_sizings a ON a.id = l.card_id WHERE a.ticker = %s", (X1RF,)
        )[0][0] == 0


def test_a_fill_with_no_price_is_refused_and_writes_nothing(aset):
    card = manual_card(aset)
    with pytest.raises(Exception, match="no price"):
        _fill(aset, card, price=None)
    assert card_row(aset, card)["state"] == "TRIGGERED"
    assert legs_of(aset, card) == []


def test_a_manual_fill_with_a_null_structural_stop_succeeds_and_its_leg_carries_the_card_stop(aset):
    card = manual_card(aset, triggered=False)  # WATCH: the one-click walk
    assert card_row(aset, card)["structural_stop"] is None
    _fill(aset, card)
    assert card_row(aset, card)["state"] == "FILLED"
    assert _history(aset, card) == ["WATCH", "ARMED", "TRIGGERED", "FILLED"]
    (leg,) = legs_of(aset, card)
    assert leg["stop_in_force"] == card_row(aset, card)["stop"] == STOP


def test_sheet_mismatch_is_true_with_nothing_attested(aset):
    from cobalt.session import clock, session_clock

    # cobalt_dev may hold a real row for the suite's frozen day: its
    # attestation is cleared inside the rolled-back transaction.
    with aset._connect() as conn:
        conn.execute("UPDATE day_modes SET attested_sheet = NULL WHERE trade_date = %s",
                     (session_clock().to_et(clock.now_utc()).date(),))
    card = manual_card(aset)
    _fill(aset, card)
    (leg,) = legs_of(aset, card)
    assert leg["sheet_mismatch"] is True
    assert leg["attested_sheet"] is None


def test_sheet_mismatch_is_false_when_the_attested_sheet_is_the_day_modes_sheet(aset):
    _attest(aset, "half.htk")
    card = manual_card(aset)
    _fill(aset, card)
    (leg,) = legs_of(aset, card)
    assert leg["sheet_mismatch"] is False
    assert leg["attested_sheet"] == "half.htk" and leg["day_mode_id"] is not None


def test_sheet_mismatch_is_true_when_the_attested_sheet_is_another_sheet(aset):
    _attest(aset, "full.htk")
    card = manual_card(aset)
    _fill(aset, card)
    (leg,) = legs_of(aset, card)
    assert leg["sheet_mismatch"] is True and leg["attested_sheet"] == "full.htk"


@pytest.mark.parametrize(("p", "warned"), [(20, True), (30, False)])
def test_the_27_percent_fill_warns_at_p20_and_not_at_p30(aset, p, warned):
    card = manual_card(aset)
    out = _fill(aset, card, price="10.0270", p=p)
    row = card_row(aset, card)
    assert row["distance_change_pct"] == Decimal("27.00")
    assert row["drift_warning_pct"] == Decimal(p) and row["drift_warned"] is warned
    assert out.recompute.drift_warned is warned


def test_p_missing_records_the_fill_and_leaves_the_warning_unevaluated(aset):
    card = manual_card(aset)
    out = _fill(aset, card, p=None)
    row = card_row(aset, card)
    assert row["state"] == "FILLED" and len(legs_of(aset, card)) == 1
    assert row["drift_warning_pct"] is None and row["drift_warned"] is None
    assert out.recompute.drift_warned is None and out.recompute.drift_warning_pct is None


def test_market_reset_refuses_the_fill_and_writes_nothing(aset):
    from datetime import datetime, timezone

    from cobalt.session import SessionBlocked

    card = manual_card(aset)
    reset = datetime(2026, 9, 3, 0, 30, tzinfo=timezone.utc)  # 20:30 ET on 09-02
    with pytest.raises(SessionBlocked):
        _fill(aset, card, now=reset)
    assert card_row(aset, card)["state"] == "TRIGGERED"
    assert legs_of(aset, card) == [] and _picks(aset, card) == 0


def test_for_date_keeps_its_columns(aset):
    from cobalt.session import session_clock

    card = manual_card(aset)
    _fill(aset, card)
    day = session_clock().to_et(card_row(aset, card)["created_at"]).date()
    rows = [r for r in aset.for_date(day) if r["id"] == card]
    assert list(rows[0]) == [
        "id", "created_at", "session", "account_mode", "ticker", "grade", "direction", "sheet_mode",
        "risk_budget", "entry", "stop", "per_share_risk", "shares", "used_risk",
        "state", "state_at", "status", "filled_at", "actual_fill", "recomputed_shares",
        "recomputed_used_risk", "share_delta", "distance_change_pct",
    ]
