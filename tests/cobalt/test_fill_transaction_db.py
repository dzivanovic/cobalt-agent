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

from legs_db_support import STOP, apply_0021, card_row, fill_kwargs, legs_of, manual_card, patch_daymode

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
