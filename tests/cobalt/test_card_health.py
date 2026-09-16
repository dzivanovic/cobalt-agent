"""S2-P2 STEP-7 — health pills for FILLED radar cards (P3 2026-09-14 R2
threshold table, copied, not re-ruled).

    participation (RVOL vs entry)  < 0.70 warn · < 0.45 bad
    cost (spread vs entry)         >= 1.5× warn · >= 2.5× bad · no source = loud n/a
    graded dot                     down >= 2 warn · <= 3 bad (judgment dots never)
    structural (stop, EMA9)        touched warn · lost on a closed working bar bad
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from decimal import Decimal

import pytest

from cobalt.cards.health import (
    EntrySnapshot,
    HealthThresholds,
    card_health,
    cost_pill,
    dot_pills,
    participation_pill,
    structural_pill,
)
from cobalt.cards.scoring import Dot
from cobalt.radar.anatomy.bars import WorkingBar
from cobalt.radar.anatomy.indicators import InsufficientBars, ema
from cobalt.taxonomy.loader import load_tunables

T0 = datetime(2026, 1, 6, 16, 0, tzinfo=timezone.utc)


@pytest.fixture(scope="module")
def t() -> HealthThresholds:
    return HealthThresholds.from_tunables(load_tunables().by_key)


def test_the_eight_rows_are_the_p3_table(t):
    assert (t.participation_warn, t.participation_bad) == (Decimal("0.70"), Decimal("0.45"))
    assert (t.cost_warn, t.cost_bad) == (Decimal("1.5"), Decimal("2.5"))
    assert (t.dot_warn_drop, t.dot_bad_max) == (2, 3)
    assert (t.structural_warn, t.structural_bad) == ("touched", "lost_on_close")


def test_a_missing_health_row_fails_loud():
    rows = dict(load_tunables().by_key)
    rows.pop("card.health.cost_bad")
    with pytest.raises(ValueError, match="card.health.cost_bad"):
        HealthThresholds.from_tunables(rows)


@pytest.mark.parametrize(
    "current, status",
    [("1.0", "ok"), ("0.70", "ok"), ("0.69", "warn"), ("0.45", "warn"), ("0.44", "bad")],
)
def test_participation_ok_warn_bad_at_the_thresholds(t, current, status):
    pill = participation_pill(entry_rvol=Decimal("1"), current_rvol=Decimal(current), t=t)
    assert pill.status == status and Decimal(pill.inputs["ratio"]) == Decimal(current)


@pytest.mark.parametrize("entry, current", [(None, "1"), ("0", "1"), ("2", None)])
def test_participation_missing_or_zero_baseline_is_loud_na(t, entry, current):
    pill = participation_pill(
        entry_rvol=None if entry is None else Decimal(entry),
        current_rvol=None if current is None else Decimal(current), t=t,
    )
    assert pill.status == "n/a" and "n/a" in pill.note.lower() and pill.inputs.get("ratio") is None


@pytest.mark.parametrize("current, status", [("0.10", "ok"), ("0.149", "ok"), ("0.15", "warn"), ("0.249", "warn"), ("0.25", "bad")])
def test_cost_ok_warn_bad_at_the_thresholds(t, current, status):
    assert cost_pill(entry_spread=Decimal("0.10"), current_spread=Decimal(current), t=t).status == status


def test_missing_spread_is_loud_na(t):
    pill = cost_pill(entry_spread=None, current_spread=None, t=t)
    assert pill.status == "n/a" and "no spread source" in pill.note
    assert cost_pill(entry_spread=Decimal("0"), current_spread=Decimal("0.1"), t=t).status == "n/a"


def _dot(factor, grade, *, source="cobalt", tier="deterministic", role="shadow", trader=None):
    return Dot(factor=factor, position=0, source=source, tier=tier, role=role,
               engine_grade=grade, trader_grade=trader)


def test_graded_dot_ok_warn_bad_and_judgment_dots_never_scored(t):
    entry = {"rvol": 8, "atrs_from_open": 8, "leg": 5, "gone": 7}
    dots = [_dot("rvol", 7), _dot("atrs_from_open", 6), _dot("leg", 3), _dot("gone", None),
            _dot("tape_read", None, source="human", tier="judgment", role="human", trader=2)]
    pills = {p.label: p for p in dot_pills(entry_grades=entry, dots=dots, t=t)}
    assert pills["rvol"].status == "ok"             # down 1
    assert pills["atrs_from_open"].status == "warn"  # down 2
    assert pills["leg"].status == "bad"             # <= 3
    assert pills["gone"].status == "n/a"
    assert "tape_read" not in pills


def _wb(minute, o, h, low, c):
    return WorkingBar(ts=T0 + timedelta(minutes=2 * minute), minutes=2, open=Decimal(o), high=Decimal(h),
                      low=Decimal(low), close=Decimal(c), volume=100, complete=True, minutes_present=2)


def test_structural_touched_warn_lost_on_close_bad_long_and_short(t):
    level = Decimal("10.00")
    ok = structural_pill("stop", level=level, direction="long", intrabar=[_wb(0, "10.2", "10.3", "10.1", "10.2")],
                         closed=[_wb(0, "10.2", "10.3", "10.1", "10.2")], t=t)
    assert ok.status == "ok"
    touched = structural_pill("stop", level=level, direction="long", intrabar=[_wb(0, "10.2", "10.3", "10.0", "10.2")],
                              closed=[_wb(0, "10.2", "10.3", "10.0", "10.2")], t=t)
    assert touched.status == "warn"
    lost = structural_pill("stop", level=level, direction="long", intrabar=[_wb(0, "10.2", "10.3", "9.9", "9.95")],
                           closed=[_wb(0, "10.2", "10.3", "9.9", "9.95")], t=t)
    assert lost.status == "bad"
    short_lost = structural_pill("stop", level=level, direction="short", intrabar=[_wb(0, "9.8", "10.1", "9.7", "10.05")],
                                 closed=[_wb(0, "9.8", "10.1", "9.7", "10.05")], t=t)
    assert short_lost.status == "bad"
    assert structural_pill("EMA9", level=None, direction="long", intrabar=[], closed=[], t=t).status == "n/a"


def test_ema_seed_warmup_and_independent_recompute():
    closes = [Decimal(str(10 + i % 3)) for i in range(12)]
    bars = [_wb(i, str(c), str(c), str(c), str(c)) for i, c in enumerate(closes)]
    with pytest.raises(InsufficientBars):
        ema(bars[:8], 9)
    obs = ema(bars, 9)
    value = sum(float(c) for c in closes[:9]) / 9
    alpha = 2 / 10
    for c in closes[9:]:
        value = alpha * float(c) + (1 - alpha) * value
    assert abs(float(obs.value) - value) <= 1e-6
    assert obs.period == 9 and obs.seed == "sma_first_period" and obs.bars_used == 12


def test_card_health_is_every_class_with_alignment_na(t):
    snapshot = EntrySnapshot(captured_at=T0, rvol=Decimal("2"), spread=None, dot_grades={"rvol": 8})
    bars = [_wb(i, "10.2", "10.3", "10.1", "10.2") for i in range(10)]
    pills = card_health(
        snapshot=snapshot, current_rvol=Decimal("1.8"), current_spread=None,
        dots=[_dot("rvol", 8)], stop=Decimal("10.0"), direction="long",
        intrabar=bars, closed=bars, ema9=None, t=t,
    )
    by_class = {}
    for pill in pills:
        by_class.setdefault(pill.klass, []).append(pill)
    assert set(by_class) == {"participation", "cost", "dot", "structural"}
    assert by_class["participation"][0].status == "ok"
    assert by_class["cost"][0].status == "n/a"
    labels = {p.label: p.status for p in by_class["structural"]}
    assert labels["stop"] == "ok" and labels["EMA9"] == "n/a" and labels["alignment"] == "n/a"
