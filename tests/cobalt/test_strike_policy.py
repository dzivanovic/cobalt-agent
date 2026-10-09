"""S4-P1 C1: the confirmation policy over i1 bars, pure (offline).

Bars are constructed (L32): a synthetic ticker, a constructed date, round
prices. Bar ts = the bar's START, UTC (`archiver/collector.py:19-31`).
2026-01-06 is an EST day, so 15:00 UTC is 10:00 ET.
"""

from __future__ import annotations

from datetime import date, datetime, timedelta, timezone
from decimal import Decimal

import pytest

from cobalt.archiver.models import Bar, Interval
from cobalt.strike.policy import Cross, Unwatchable, crossed, policy_of
from cobalt.taxonomy.trade_def import ConfirmationPolicy

UTC = timezone.utc
T0 = datetime(2026, 1, 6, 15, 0, tzinfo=UTC)  # 10:00 ET
MIN = timedelta(minutes=1)
ENTRY = Decimal("10.00")


def bar(minute: int, *, high="9.90", low="9.80", close="9.85", open_="9.85", ticker="ZZST") -> Bar:
    return Bar(ticker=ticker, interval=Interval.I1, ts=T0 + minute * MIN, open=Decimal(open_),
               high=Decimal(high), low=Decimal(low), close=Decimal(close), volume=100)


def pol(kind: str, **kw) -> ConfirmationPolicy:
    return ConfirmationPolicy(type=kind, **kw)


# -- intrabar ----------------------------------------------------------------


def test_intrabar_long_crosses_on_the_first_touching_bar():
    bars = [bar(0), bar(1), bar(2, high="10.00"), bar(3, high="10.20")]
    got = crossed(pol("intrabar"), "long", ENTRY, bars, since=T0, now=T0 + 4 * MIN)
    assert isinstance(got, Cross)
    assert got.policy == "intrabar"
    assert got.bar_ts == T0 + 2 * MIN
    assert got.bar_close_at == T0 + 3 * MIN
    assert got.cross_price == Decimal("10.00")


def test_intrabar_short_crosses_on_the_first_bar_whose_low_touches():
    bars = [bar(0, high="10.30", low="10.10"), bar(1, high="10.20", low="9.95")]
    got = crossed(pol("intrabar"), "short", ENTRY, bars, since=T0, now=T0 + 2 * MIN)
    assert got.bar_ts == T0 + MIN and got.cross_price == Decimal("9.95")


def test_negative_control_intrabar_high_short_of_entry_is_no_cross():
    bars = [bar(0, high="9.99"), bar(1, high="9.99")]
    assert crossed(pol("intrabar"), "long", ENTRY, bars, since=T0, now=T0 + 2 * MIN) is None


def test_negative_control_short_whose_low_stays_above_entry_is_no_cross():
    bars = [bar(0, high="10.30", low="10.01"), bar(1, high="10.20", low="10.05")]
    assert crossed(pol("intrabar"), "short", ENTRY, bars, since=T0, now=T0 + 2 * MIN) is None


def test_a_forming_bar_touching_entry_crosses_intrabar_but_not_close_through():
    bars = [bar(0), bar(1, high="10.10", close="10.05")]
    now = T0 + MIN + timedelta(seconds=20)  # the 10:01 bar is still forming
    got = crossed(pol("intrabar"), "long", ENTRY, bars, since=T0, now=now)
    assert got is not None and got.bar_ts == T0 + MIN
    assert crossed(pol("close_through"), "long", ENTRY, bars, since=T0, now=now) is None


def test_a_bar_that_starts_before_since_never_counts():
    bars = [bar(0, high="10.10"), bar(1), bar(2, high="10.05")]
    since = T0 + timedelta(seconds=30)  # 10:00:30 — the 10:00 bar touched, but started before
    got = crossed(pol("intrabar"), "long", ENTRY, bars, since=since, now=T0 + 3 * MIN)
    assert got.bar_ts == T0 + 2 * MIN
    only_early = [bar(0, high="10.10"), bar(1)]
    assert crossed(pol("intrabar"), "long", ENTRY, only_early, since=since, now=T0 + 2 * MIN) is None


# -- close-based policies ------------------------------------------------------


def test_close_through_long_and_short():
    bars = [bar(0, high="10.10", close="9.99"), bar(1, high="10.10", close="10.02"), bar(2)]
    got = crossed(pol("close_through"), "long", ENTRY, bars, since=T0, now=T0 + 3 * MIN)
    assert got.policy == "close_through" and got.bar_ts == T0 + MIN and got.cross_price == Decimal("10.02")
    short = [bar(0, low="9.90", close="10.01"), bar(1, low="9.90", close="9.97")]
    got = crossed(pol("close_through"), "short", ENTRY, short, since=T0, now=T0 + 2 * MIN)
    assert got.bar_ts == T0 + MIN and got.cross_price == Decimal("9.97")


def test_two_bar_needs_two_consecutive_completed_closes():
    bars = [bar(0, high="10.2", close="10.05"), bar(1, close="9.95"), bar(2, high="10.2", close="10.05"),
            bar(3, high="10.2", close="10.10")]
    got = crossed(pol("two_bar"), "long", ENTRY, bars, since=T0, now=T0 + 4 * MIN)
    assert got.policy == "two_bar" and got.bar_ts == T0 + 3 * MIN
    # the second close is still forming: no cross yet
    assert crossed(pol("two_bar"), "long", ENTRY, bars, since=T0, now=T0 + 3 * MIN + timedelta(seconds=5)) is None
    short = [bar(0, low="9.8", close="9.95"), bar(1, low="9.8", close="9.90")]
    assert crossed(pol("two_bar"), "short", ENTRY, short, since=T0, now=T0 + 2 * MIN).bar_ts == T0 + MIN


def test_acceptance_by_bars_and_by_time():
    bars = [bar(i, high="10.2", close="10.05") for i in range(3)]
    got = crossed(pol("acceptance", bars=3), "long", ENTRY, bars, since=T0, now=T0 + 3 * MIN)
    assert got.policy == "acceptance" and got.bar_ts == T0 + 2 * MIN
    assert crossed(pol("acceptance", bars=4), "long", ENTRY, bars, since=T0, now=T0 + 3 * MIN) is None
    got = crossed(pol("acceptance", time="2 min"), "long", ENTRY, bars, since=T0, now=T0 + 3 * MIN)
    assert got.bar_ts == T0 + MIN
    short = [bar(i, low="9.8", close="9.95") for i in range(2)]
    assert crossed(pol("acceptance", bars=2), "short", ENTRY, short, since=T0, now=T0 + 2 * MIN).bar_ts == T0 + MIN


def test_acceptance_with_nothing_to_count_or_an_unparseable_time_is_unwatchable():
    bars = [bar(0, high="10.2", close="10.05")]
    assert isinstance(crossed(pol("acceptance"), "long", ENTRY, bars, since=T0, now=T0 + MIN), Unwatchable)
    got = crossed(pol("acceptance", time="two minutes"), "long", ENTRY, bars, since=T0, now=T0 + MIN)
    assert isinstance(got, Unwatchable) and "two minutes" in got.reason


def test_no_policy_and_a_sequence_trigger_are_unwatchable():
    got = crossed(None, "long", ENTRY, [bar(0, high="10.2")], since=T0, now=T0 + MIN)
    assert isinstance(got, Unwatchable) and got.reason
    from cobalt.taxonomy.trade_def import SequenceTrigger, SimpleTrigger

    seq = SequenceTrigger(steps=[{"name": "retest", "predicate": {"text": "a retest"}}])
    assert isinstance(policy_of(seq), Unwatchable)
    simple = SimpleTrigger(type="bar_break", confirmation_policy={"type": "close_through"})
    assert policy_of(simple).type.value == "close_through"


# -- AGREEMENT with the F12 replay (L3: one formula) ---------------------------


@pytest.mark.parametrize("offset_s", [0, 30])
def test_intrabar_agrees_with_replay_card_trigger_bar(offset_s):
    from cobalt.replay.cards import replay_card
    from cobalt.replay.models import CardCandidate, TransitionRow, WindowResolution

    created_at = T0 + timedelta(seconds=offset_s)
    # 09:59 ET to the close (21:00 UTC); the 10:00 and 10:03 bars touch 10.00.
    bars = [bar(m) for m in range(-1, 360)]
    bars[1] = bar(0, high="10.01")
    bars[4] = bar(3, high="10.04")
    card = CardCandidate(
        id=1, ticker="ZZST", direction="long", entry=ENTRY, stop=Decimal("9.50"), created_at=created_at,
        transitions=(TransitionRow(id=1, card_id=1, to_state="WATCH", at=created_at),),
    )
    close = datetime(2026, 1, 6, 21, 0, tzinfo=UTC)
    replay = replay_card(
        card, bars, trade_date=date(2026, 1, 6),
        window=WindowResolution(resolved_end=close, source="constructed", detail="constructed"),
        session_close=close, positions=[],
    )
    assert replay.status == "miss"
    trigger_ts = datetime.fromisoformat(replay.miss.receipt["outputs"]["trigger_bar"]["ts"])
    got = crossed(pol("intrabar"), "long", ENTRY, bars, since=created_at, now=close)
    assert got.bar_ts == trigger_ts
    assert trigger_ts == (T0 if offset_s == 0 else T0 + 3 * MIN)
