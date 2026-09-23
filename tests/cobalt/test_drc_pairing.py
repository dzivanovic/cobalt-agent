"""DRC D1 — the typed records (D1-1) and FIFO pairing + carry (D1-3).

Every input is a D1-0 fixture or a constructed literal (L69); nothing
here is a value of his.
"""

from __future__ import annotations

from datetime import date, datetime, timedelta, timezone
from decimal import Decimal

import pytest
from pydantic import ValidationError

from cobalt.drc.models import (
    Detection,
    Direction,
    ExecSide,
    Execution,
    ImportResult,
    Kind,
    Leg,
    Outcome,
    StatsRow,
    Trade,
    TradeStatus,
)

ET = timezone(timedelta(hours=-5))
T0 = datetime(2001, 1, 2, 9, 40, tzinfo=ET)


# ---------------------------------------------------------------------
# D1-1 — models
# ---------------------------------------------------------------------


def test_the_side_enum_is_exactly_the_three_codes_e1_shows():
    assert {s.value for s in ExecSide} == {"B", "S", "SS"}


def test_an_execution_refuses_a_naive_time_an_unknown_side_and_a_zero_qty():
    with pytest.raises(ValidationError):
        Execution(line=2, time=datetime(2001, 1, 2, 9, 40))
    with pytest.raises(ValidationError):
        Execution(line=2, time=T0, side="X")
    with pytest.raises(ValidationError):
        Execution(line=2, time=T0, qty=0)


def test_an_execution_of_a_partial_file_carries_none_for_an_absent_column():
    e = Execution(line=2, time=T0, symbol="AAA", side="B", qty=10)
    assert e.price is None and e.account is None


def test_a_stats_row_is_all_optional_and_its_stop_defaults_to_none():
    row = StatsRow(line=2)
    assert row.stop is None and row.entry is None and row.playbooks == []


def _trade(**over):
    fields = dict(
        trade_id="AAA-long-x",
        symbol="AAA",
        direction=Direction.LONG,
        status=TradeStatus.CLOSED,
        entry_time=T0,
        avg_entry=Decimal("10"),
        shares=10,
        held_shares=0,
        gross_pnl=Decimal("1"),
        entries=[Leg(kind="entry", time=T0, price=Decimal("10"), shares=10, line=3)],
        legs=[Leg(kind="exit", time=T0, price=Decimal("10.1"), shares=10, line=2)],
    )
    fields.update(over)
    return Trade(**fields)


def test_a_trade_keeps_every_playbook_in_order_and_defaults_to_none():
    assert _trade().playbooks == []
    t = _trade(playbooks=["Beta", "Alpha", "Beta"])
    assert t.playbooks == ["Beta", "Alpha", "Beta"]


def test_net_and_commissions_are_the_stats_logs_own_never_computed():
    assert _trade().net_pnl is None and _trade().commissions is None
    row = StatsRow(line=2, net_pnl=Decimal("0.5"), commission=Decimal("0.1"))
    assert _trade(stats=row).net_pnl == Decimal("0.5")
    assert _trade(stats=row).commissions == Decimal("0.1")


def test_an_open_trades_unrealized_is_not_computed():
    assert _trade(status=TradeStatus.OPEN, held_shares=5).unrealized == "not computed"


def test_the_partial_flag_names_the_missing_columns_loudly():
    d = Detection(name="x", kind=Kind.STATS_LOG, outcome=Outcome.PARTIAL, reason="r",
                  missing=["A", "B"])
    assert d.partial_flag == "PARTIAL — missing: A, B"
    r = ImportResult(name="x", kind=Kind.TRADING_LOG, outcome=Outcome.PARTIAL,
                     missing=["C"])
    assert r.partial_flag == "PARTIAL — missing: C"


def test_an_extra_column_is_the_kinds_shape_flag():
    r = ImportResult(name="x", kind=Kind.TRADING_LOG, outcome=Outcome.PARSED, extras=["New"])
    assert r.degraded == "trading_log_shape"
    d = Detection(name="x", kind=Kind.STATS_LOG, outcome=Outcome.PARSED, reason="r",
                  extras=["New"])
    assert d.degraded == "stats_log_shape"
    assert ImportResult(name="x", kind=Kind.STATS_LOG, outcome=Outcome.PARSED).degraded is None


def test_the_outcome_domain_is_parsed_partial_failed_ignored():
    assert {o.value for o in Outcome} == {"parsed", "partial", "failed", "ignored"}


def test_records_are_frozen_and_refuse_unknown_fields():
    with pytest.raises(ValidationError):
        StatsRow(line=2, invented=1)
    row = StatsRow(line=2)
    with pytest.raises(ValidationError):
        row.stop = Decimal("1")
