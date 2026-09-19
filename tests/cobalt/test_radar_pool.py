"""D3 rank/stickiness precedence tests."""

import random
from datetime import datetime, timezone
from decimal import Decimal
from zoneinfo import ZoneInfo

from cobalt.radar.models import Candidate, ExcludeBlock, ExcludedBy, OpenMember, PoolBlock, ScreenBlock, SourceHealth, SourceSet
from cobalt.radar.pool import Action, decide

NOW = datetime(2026, 9, 3, 14, 30, tzinfo=timezone.utc)


def _pool(cap=1, stickiness=3):
    return PoolBlock(kind="pool", cap=cap, stickiness_scans=stickiness,
        priority=["screens", "lists"],
        rank_metric={"premarket": "volume", "rth": "rvol", "aftermarket": "volume"},
        overrides={})


def _source():
    return SourceSet(source="list:synthetic@abc", kind="list", tickers=["BBB", "AAA"],
        metrics={"BBB": {"volume": 1, "rvol": 5}, "AAA": {"volume": 1000, "rvol": 1}})


def test_cap_one_incumbent_leaves_on_n_plus_one_and_streak_never_resets():
    incumbent = OpenMember(ticker="AAA", sources=["list:synthetic@abc"], entered_at=NOW,
        below_cap_streak=0, last_rank=1, trade_date="2026-09-03")
    candidates = [Candidate(ticker=x, sources=["list:synthetic@abc"]) for x in ("AAA", "BBB")]
    for expected in (1, 2, 3):
        result = decide(candidates, [incumbent], _pool(), [_source()], NOW)
        transition = next(x for x in result.transitions if x.ticker == "AAA")
        assert transition.action is Action.RETAIN
        assert transition.below_cap_streak == expected
        incumbent = incumbent.model_copy(update={"below_cap_streak": expected, "last_rank": transition.rank})
    result = decide(candidates, [incumbent], _pool(), [_source()], NOW)
    assert next(x for x in result.transitions if x.ticker == "AAA").action is Action.LEAVE
    assert next(x for x in result.transitions if x.ticker == "BBB").action is Action.ADMIT


def test_missing_pool_freezes_and_manual_exclude_wins():
    member = OpenMember(ticker="AAA", sources=["list:x"], entered_at=NOW, below_cap_streak=0)
    frozen = decide([], [member], None, [], NOW)
    assert frozen.frozen and frozen.transitions == []
    result = decide([Candidate(ticker="AAA", sources=["list:x"])], [member],
        [_pool(), ExcludeBlock(kind="exclude", tickers=["AAA"])], [_source()], NOW)
    row = next(x for x in result.transitions if x.ticker == "AAA")
    assert row.action is Action.LEAVE and row.excluded_by.value == "manual"


def test_never_admitted_episode_closes_when_candidate_disappears():
    episode = OpenMember(ticker="AAA", sources=["list:x"], entered_at=None,
        below_cap_streak=0, last_rank=2, trade_date="2026-09-03")
    result = decide([], [episode], _pool(), [], NOW)
    row = next(x for x in result.transitions if x.ticker == "AAA")
    assert row.action is Action.LEAVE and row.excluded_by is None


def test_rollover_closes_at_prior_aftermarket_close():
    member = OpenMember(ticker="AAA", sources=["list:x"], entered_at=NOW,
        below_cap_streak=0, trade_date="2026-09-02")
    result = decide([], [member], _pool(), [], NOW)
    row = next(x for x in result.transitions if x.ticker == "AAA")
    assert row.rollover
    assert row.left_at.astimezone(ZoneInfo("America/New_York")).strftime("%Y-%m-%d %H:%M") == "2026-09-02 20:00"


def test_10000_seeded_scans_never_break_the_hard_cap():
    rng = random.Random(20260910)
    names = [f"T{index:02d}" for index in range(8)]
    for _ in range(10_000):
        cap = rng.randint(1, 5)
        tickers = rng.sample(names, rng.randint(0, len(names)))
        source = SourceSet(source="list:synthetic@abc", kind="list", tickers=tickers,
            metrics={ticker: {"volume": rng.random(), "rvol": rng.random()} for ticker in tickers})
        opens = [OpenMember(ticker=ticker, sources=[source.source], entered_at=NOW,
            below_cap_streak=rng.randint(0, 3), last_rank=rng.randint(1, 8), trade_date="2026-09-03")
            for ticker in rng.sample(names, rng.randint(0, len(names)))]
        candidates = [Candidate(ticker=ticker, sources=[source.source]) for ticker in tickers]
        result = decide(candidates, opens, _pool(cap=cap, stickiness=rng.randint(0, 3)), [source], NOW)
        admitted = sum(row.action in {Action.ADMIT, Action.RETAIN, Action.HOLD} for row in result.transitions)
        assert admitted <= cap


def test_first_from_screen_moves_first_only_at_its_time():
    pool = _pool(cap=1, stickiness=0).model_copy(update={
        "overrides": {"day": {"first_from": "10:00"}}
    })
    screens = [
        SourceSet(source="screen:other@a", kind="screen", tickers=["AAA"], note_order=0),
        SourceSet(source="screen:day@b", kind="screen", tickers=["BBB"], note_order=1),
    ]
    candidates = [Candidate(ticker=x, sources=[screens[i].source]) for i, x in enumerate(("AAA", "BBB"))]
    before = decide(candidates, [], pool, screens, datetime(2026, 9, 3, 13, 59, tzinfo=timezone.utc))
    after = decide(candidates, [], pool, screens, datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc))
    assert next(x for x in before.transitions if x.action is Action.ADMIT).ticker == "AAA"
    assert next(x for x in after.transitions if x.action is Action.ADMIT).ticker == "BBB"


def test_screen_metric_override_uses_position_not_cross_metric_magnitude():
    pool = _pool(cap=1, stickiness=0).model_copy(update={
        "overrides": {"morning": {"rank_metric": "volume"}}
    })
    source = SourceSet(source="screen:morning@a", kind="screen", tickers=["AAA", "BBB"],
        metrics={"AAA": {"volume": 10, "rvol": 1}, "BBB": {"volume": 1, "rvol": 1000}})
    result = decide([Candidate(ticker=x, sources=[source.source]) for x in source.tickers], [], pool, [source], NOW)
    assert next(x for x in result.transitions if x.action is Action.ADMIT).ticker == "AAA"


def test_inactive_degraded_and_not_equity_precedence():
    inactive = SourceSet(source="screen:closed@a", kind="screen", tickers=["AAA"], active=False)
    member = OpenMember(ticker="AAA", sources=[inactive.source], entered_at=NOW, below_cap_streak=0)
    left = decide([], [member], _pool(), [inactive], NOW)
    assert next(x for x in left.transitions if x.ticker == "AAA").excluded_by is ExcludedBy.SCREEN_INACTIVE

    degraded = SourceSet(source="list:bad@a", kind="list", tickers=["AAA", "BBB"], health=SourceHealth.DEGRADED)
    members = [
        OpenMember(ticker="AAA", sources=[degraded.source], entered_at=NOW, below_cap_streak=1, last_rank=1),
        OpenMember(ticker="BBB", sources=[degraded.source], entered_at=NOW, below_cap_streak=1, last_rank=8),
    ]
    held = decide([], members, _pool(cap=1), [degraded], NOW)
    assert next(x for x in held.transitions if x.ticker == "AAA").action is Action.HOLD
    assert next(x for x in held.transitions if x.ticker == "BBB").excluded_by is ExcludedBy.CONFIG_CAP

    excluded = decide([Candidate(ticker="AAA", sources=["list:x"], excluded_by=ExcludedBy.NOT_EQUITY)], [], _pool(), [], NOW)
    assert excluded.transitions[0].excluded_by is ExcludedBy.NOT_EQUITY


# ---------------------------------------------------------------------
# S2-P4 STEP-2 (R1): the value of the metric that actually ranked a name
# ---------------------------------------------------------------------


def _by_ticker(result):
    return {item.ticker: item for item in result.transitions}


def test_ranked_transitions_carry_the_session_metric_and_value_on_retain_admit_exclude():
    """10:30 ET is rth -> the session metric is rvol; a None value stays None."""
    source = SourceSet(source="list:synthetic@abc", kind="list", tickers=["AAA", "BBB", "CCC"],
        metrics={"AAA": {"volume": 10, "rvol": 7.5}, "BBB": {"volume": 20, "rvol": 3.25},
                 "CCC": {"volume": 30, "rvol": None}})
    incumbent = OpenMember(ticker="AAA", sources=[source.source], entered_at=NOW, below_cap_streak=0,
        last_rank=1, trade_date="2026-09-03", rank_metric="volume", rank_value=Decimal("1"))
    candidates = [Candidate(ticker=x, sources=[source.source]) for x in source.tickers]
    by = _by_ticker(decide(candidates, [incumbent], _pool(cap=2, stickiness=0), [source], NOW))
    assert (by["AAA"].action, by["AAA"].rank_metric, by["AAA"].rank_value) == (Action.RETAIN, "rvol", Decimal("7.5"))
    assert (by["BBB"].action, by["BBB"].rank_metric, by["BBB"].rank_value) == (Action.ADMIT, "rvol", Decimal("3.25"))
    assert (by["CCC"].action, by["CCC"].rank_metric, by["CCC"].rank_value) == (Action.EXCLUDE, "rvol", None)


def test_screen_override_metric_value_recorded_under_override_name():
    pool = _pool(cap=1, stickiness=0).model_copy(update={
        "overrides": {"morning": {"rank_metric": "volume"}}
    })
    source = SourceSet(source="screen:morning@a", kind="screen", tickers=["AAA", "BBB"],
        metrics={"AAA": {"volume": 10, "rvol": 1}, "BBB": {"volume": 1, "rvol": 1000}})
    by = _by_ticker(decide([Candidate(ticker=x, sources=[source.source]) for x in source.tickers], [], pool, [source], NOW))
    assert (by["AAA"].rank_metric, by["AAA"].rank_value) == ("volume", Decimal("10"))
    assert (by["BBB"].rank_metric, by["BBB"].rank_value) == ("volume", Decimal("1"))


def test_list_sourced_value_is_max_across_lists():
    one = SourceSet(source="list:one@a", kind="list", tickers=["AAA"], metrics={"AAA": {"volume": 1, "rvol": 2.5}})
    two = SourceSet(source="list:two@b", kind="list", tickers=["AAA"], note_order=1,
        metrics={"AAA": {"volume": 1, "rvol": 4.75}})
    three = SourceSet(source="list:three@c", kind="list", tickers=["AAA"], note_order=2,
        metrics={"AAA": {"volume": 1, "rvol": None}})
    by = _by_ticker(decide([Candidate(ticker="AAA", sources=[one.source, two.source, three.source])],
        [], _pool(cap=1), [one, two, three], NOW))
    assert (by["AAA"].action, by["AAA"].rank_metric, by["AAA"].rank_value) == (Action.ADMIT, "rvol", Decimal("4.75"))


def test_hold_keeps_prior_value():
    degraded = SourceSet(source="list:bad@a", kind="list", tickers=["AAA", "BBB"], health=SourceHealth.DEGRADED)
    members = [
        OpenMember(ticker="AAA", sources=[degraded.source], entered_at=NOW, below_cap_streak=0, last_rank=1,
            rank_metric="volume", rank_value=Decimal("123.5")),
        OpenMember(ticker="BBB", sources=[degraded.source], entered_at=NOW, below_cap_streak=0, last_rank=2),
    ]
    by = _by_ticker(decide([], members, _pool(cap=2), [degraded], NOW))
    assert (by["AAA"].action, by["AAA"].rank_metric, by["AAA"].rank_value) == (Action.HOLD, "volume", Decimal("123.5"))
    assert (by["BBB"].action, by["BBB"].rank_metric, by["BBB"].rank_value) == (Action.HOLD, None, None)


# ---------------------------------------------------------------------
# The list `union` ordering, PINNED (tribunal A3, L52)
#
# `_ranked`'s union sort key (`pool.py:179-205`) is a 3-tuple:
#   (max(<list values>, default=None) is None, -(max(<list values>, default=0)), name)
# i.e. names WITH a value first, then by that value descending, then by
# name ascending; and `union` feeds only `position = union.index(ticker)
# + 1` (`pool.py:206`), never the candidate set itself.
#
# These two tests pin that order as it stands TODAY. They deliberately do
# NOT assert the one input whose behaviour the S2-P4 STEP-2 None-filter
# changed — a name carrying a value on one list and None on another, which
# raised `TypeError` before the filter and now places normally. That edit
# is undisclosed under L52 and Dejan's ruling (waive-and-disclose, or
# revert) is owed; a test asserting it either way would settle his ruling
# from inside the suite. Both tests below pass under the filtered AND the
# unfiltered key, so a revert does not silently break them.
# ---------------------------------------------------------------------


def _ranks(result):
    return {item.ticker: item.rank for item in result.transitions}


def test_list_union_orders_by_value_descending_then_name_when_every_value_is_present():
    """All values present: the order and the rank map are exactly what the
    key tuple above dictates — value descending, ties broken by name."""
    source = SourceSet(source="list:synthetic@abc", kind="list",
        tickers=["AAA", "BBB", "CCC", "DDD"],
        metrics={"AAA": {"volume": 1, "rvol": 1.0}, "BBB": {"volume": 1, "rvol": 4.0},
                 "CCC": {"volume": 1, "rvol": 4.0}, "DDD": {"volume": 1, "rvol": 9.0}})
    candidates = [Candidate(ticker=x, sources=[source.source]) for x in source.tickers]
    result = decide(candidates, [], _pool(cap=4, stickiness=0), [source], NOW)
    # 10:30 ET is rth, so the session metric is rvol (as `_pool` declares).
    # DDD 9.0 · BBB 4.0 = CCC 4.0, name breaks the tie · AAA 1.0
    assert _ranks(result) == {"DDD": 1, "BBB": 2, "CCC": 3, "AAA": 4}
    assert all(item.action is Action.ADMIT for item in result.transitions)


def test_a_name_with_no_value_on_any_list_sorts_after_every_name_that_has_one():
    """Element 1 of the key (`… is None`) puts the valueless names last,
    and among them element 2 is equal (`default=0`), so `name` decides —
    deterministically, never by dict order."""
    source = SourceSet(source="list:synthetic@abc", kind="list",
        tickers=["AAA", "BBB", "YYY", "ZZZ"],
        metrics={"AAA": {"volume": 1, "rvol": 1.0}, "BBB": {"volume": 1, "rvol": 4.0},
                 "ZZZ": {"volume": 1, "rvol": None}, "YYY": {"volume": 1, "rvol": None}})
    candidates = [Candidate(ticker=x, sources=[source.source]) for x in source.tickers]
    result = decide(candidates, [], _pool(cap=4, stickiness=0), [source], NOW)
    assert _ranks(result) == {"BBB": 1, "AAA": 2, "YYY": 3, "ZZZ": 4}
    by = _by_ticker(result)
    assert (by["YYY"].rank_value, by["ZZZ"].rank_value) == (None, None)
