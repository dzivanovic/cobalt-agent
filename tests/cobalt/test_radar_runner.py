"""Runner session-first behavior and commit gate tests."""

import asyncio
from copy import deepcopy
from datetime import datetime, time, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import pytest

from cobalt.archiver.collector import scrub
from cobalt.radar.config import load_config
from cobalt.radar.collector import ScreenerSnapshot
from cobalt.radar.notes import load_sources
from cobalt.radar.poller import PollResult
from cobalt.radar.pool import Action
from cobalt.radar.runner import RadarRunner, StageDropped, gate
from cobalt.session.models import Session


class Clock:
    def __init__(self, session):
        self.value = session

    def session(self, _now):
        return self.value


class Never:
    def __getattr__(self, name):
        raise AssertionError(f"idle cycle touched {name}")


def _runner(session):
    return RadarRunner(config=load_config(), sources_loader=Never(), collector=Never(),
        radar_store=Never(), settings_store=Never(), poller=Never(), clock=Clock(session),
        now=lambda: datetime(2026, 9, 3, 4, 0, tzinfo=timezone.utc))


def test_idle_and_market_reset_make_no_fetch_or_write_calls():
    assert asyncio.run(_runner(Session.OVERNIGHT).cycle()).state == "idle:overnight"
    assert asyncio.run(_runner(Session.MARKET_RESET).cycle()).state == "paused_market_reset"


def test_gate_raises_at_transaction_boundary():
    clock = Clock(Session.RTH)
    check = gate("membership", clock=clock,
        now=lambda: datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc))
    check()
    clock.value = Session.MARKET_RESET
    with pytest.raises(StageDropped, match="membership"):
        check()


class ActiveClock(Clock):
    def to_et(self, value):
        return value.astimezone(ZoneInfo("America/New_York"))


class Collector:
    async def screen(self, _block, now):
        return ScreenerSnapshot("screen-synthetic", now,
            ({"Ticker": "AAA", "Volume": "2", "Relative Volume": "1", "Asset Type": "Stock"},),
            ("Ticker", "Volume", "Relative Volume", "Asset Type"))

    async def listed(self, _block, now):
        return [ScreenerSnapshot("list-synthetic", now, (),
            ("Ticker", "Volume", "Relative Volume", "Asset Type"))]


class Radar:
    def __init__(self, events): self.events = events
    def pool_row(self, _key): return None
    def open_members(self, _key): return []
    def apply_membership(self, **kwargs):
        self.events.append("membership"); kwargs["before_commit"]()
    def put_pool(self, _row, **kwargs):
        self.events.append("pool"); kwargs["before_commit"]()
    def stamp_failure(self, *_args, **kwargs):
        self.events.append("failure"); kwargs["before_commit"]()
    def stamp_poll(self, *_args, **kwargs):
        self.events.append("poll_status"); kwargs["before_commit"]()


class Settings:
    def __init__(self, events, fail=False): self.events, self.fail = events, fail
    def values(self): return {}
    def put(self, _rows, *, source, before_commit=None):
        self.events.append("mirror")
        if self.fail: raise RuntimeError("synthetic mirror failure")
        before_commit()
        return {}


class Poller:
    def __init__(self, events): self.events = events
    async def poll(self, members, *, before_commit, **_kwargs):
        self.events.append("bars")
        for member in members: before_commit(member.ticker)()
        return PollResult([], {item.ticker: 0 for item in members})


def _active_runner(events, *, mirror_fail=False):
    parsed = load_sources(
        Path("tests/fixtures/radar/radar-screens.example.md"),
        Path("tests/fixtures/radar/radar-lists.example.md"),
        scan_interval=60, poll_interval=60, finviz_max_rpm=100, list_chunk_size=50,
    )
    return RadarRunner(config=load_config(), sources_loader=lambda: parsed, collector=Collector(),
        radar_store=Radar(events), settings_store=Settings(events, mirror_fail),
        poller=Poller(events), clock=ActiveClock(Session.RTH),
        now=lambda: datetime(2026, 9, 3, 14, 30, tzinfo=timezone.utc))


def test_stage_order_is_membership_pool_mirror_then_bars():
    events = []
    result = asyncio.run(_active_runner(events).cycle())
    assert result.state == "scanning"
    assert events == ["membership", "pool", "mirror", "bars", "poll_status"]


def test_mirror_failure_is_stamped_and_bars_continue():
    events = []
    result = asyncio.run(_active_runner(events, mirror_fail=True).cycle())
    assert result.failed_stage == "mirror"
    assert events == ["membership", "pool", "mirror", "failure", "bars", "poll_status"]


ET = ZoneInfo("America/New_York")
BEFORE_RESET = datetime(2026, 9, 3, 19, 59, 59, 500000, tzinfo=ET)
AT_RESET = datetime(2026, 9, 3, 20, 0, 0, tzinfo=ET)
NEXT_ACTIVE = datetime(2026, 9, 4, 10, 0, 0, tzinfo=ET)


class CrossingClock:
    def __init__(self):
        self.value = BEFORE_RESET

    def session(self, instant):
        wall = instant.astimezone(ET).time()
        if time(20) <= wall < time(21):
            return Session.MARKET_RESET
        if time(9, 30) <= wall < time(16):
            return Session.RTH
        if time(16) <= wall < time(20):
            return Session.AFTERMARKET
        if time(4) <= wall < time(9, 30):
            return Session.PREMARKET
        return Session.OVERNIGHT

    def to_et(self, instant):
        return instant.astimezone(ET)

    def cross(self):
        self.value = AT_RESET


class CrossingCollector:
    async def screen(self, _block, now):
        return ScreenerSnapshot(
            "screen-synthetic",
            now,
            tuple(
                {
                    "Ticker": ticker,
                    "Volume": str(volume),
                    "Relative Volume": str(rvol),
                    "Asset Type": "Stock",
                }
                for ticker, volume, rvol in (("AAA", 30, 1), ("BBB", 20, 2), ("CCC", 10, 3))
            ),
            ("Ticker", "Volume", "Relative Volume", "Asset Type"),
        )

    async def listed(self, _block, now):
        return [await self.screen(_block, now)]


class CrossingRadarStore:
    def __init__(self, clock, crossing):
        self.clock = clock
        self.crossing = crossing
        self.members = {}
        self.pool = None
        self.commits = []
        self.membership_scan_ids = set()

    def pool_row(self, _key):
        return deepcopy(self.pool)

    def open_members(self, _key):
        return [deepcopy(row) for row in self.members.values()]

    def _commit(self, stage, payload):
        self.commits.append((stage, self.clock.value))
        return payload

    def apply_membership(self, *, transitions, scan_id, before_commit, now, **_kwargs):
        if scan_id in self.membership_scan_ids:
            return
        staged = deepcopy(self.members)
        for row in transitions:
            if row.action in {Action.ADMIT, Action.RETAIN, Action.HOLD}:
                staged[row.ticker] = {
                    "ticker": row.ticker,
                    "sources": row.sources,
                    "entered_at": staged.get(row.ticker, {}).get("entered_at", now),
                    "below_cap_streak": row.below_cap_streak,
                    "last_rank": row.rank,
                    "trade_date": now.astimezone(ET).date().isoformat(),
                }
            elif row.action is Action.LEAVE:
                staged.pop(row.ticker, None)
        if self.crossing == "inside_s1":
            self.clock.cross()
        before_commit()
        self.members = self._commit("membership", staged)
        self.membership_scan_ids.add(scan_id)
        if self.crossing == "between_s1_s2":
            self.clock.cross()

    def put_pool(self, row, *, before_commit, **_kwargs):
        staged = deepcopy(row)
        if self.crossing == "inside_s2":
            self.clock.cross()
        before_commit()
        self.pool = self._commit("pool_row", staged)

    def stamp_failure(self, _key, *, failed_stage, failed_detail, before_commit, **_kwargs):
        staged = deepcopy(self.pool or {})
        staged.update(failed_stage=failed_stage, failed_detail=scrub(failed_detail))
        before_commit()
        self.pool = self._commit("failure", staged)

    def stamp_poll(self, _key, *, before_commit, **_kwargs):
        staged = deepcopy(self.pool or {})
        before_commit()
        self.pool = self._commit("poll_status", staged)


class CrossingSettingsStore:
    def __init__(self, clock, crossing, commits):
        self.clock = clock
        self.crossing = crossing
        self.commits = commits
        self.rows = {}

    def values(self):
        return deepcopy(self.rows)

    def put(self, rows, *, before_commit, **_kwargs):
        staged = deepcopy(rows)
        if self.crossing == "inside_s3":
            self.clock.cross()
        before_commit()
        self.rows = staged
        self.commits.append(("mirror", self.clock.value))
        return {key: "created" for key in rows}


class CrossingPoller:
    def __init__(self, clock, crossing, commits, k=1):
        self.clock = clock
        self.crossing = crossing
        self.commits = commits
        self.k = k
        self.written = []
        self.attempted = []

    async def poll(self, members, *, before_commit, **_kwargs):
        for index, member in enumerate(members):
            self.attempted.append(member.ticker)
            if self.crossing == "inside_s4" and index == self.k:
                self.clock.cross()
            check = before_commit(member.ticker)
            check()
            self.written.append(member.ticker)
            self.commits.append((f"bars:{member.ticker}", self.clock.value))
            if self.crossing == "between_s4" and index == self.k:
                self.clock.cross()
        return PollResult([], {ticker: 1 for ticker in self.written})


def _crossing_runner(crossing):
    clock = CrossingClock()
    radar = CrossingRadarStore(clock, crossing)
    settings = CrossingSettingsStore(clock, crossing, radar.commits)
    poller = CrossingPoller(clock, crossing, radar.commits)
    parsed = load_sources(
        Path("tests/fixtures/radar/radar-screens.example.md"),
        Path("tests/fixtures/radar/radar-lists.example.md"),
        scan_interval=60,
        poll_interval=60,
        finviz_max_rpm=100,
        list_chunk_size=50,
    )
    runner = RadarRunner(
        config=load_config(),
        sources_loader=lambda: parsed,
        collector=CrossingCollector(),
        radar_store=radar,
        settings_store=settings,
        poller=poller,
        clock=clock,
        now=lambda: clock.value,
    )
    return runner, clock, radar, settings, poller


@pytest.mark.parametrize(
    ("crossing", "crossed_stage", "committed_before"),
    [
        ("inside_s1", "membership", []),
        ("between_s1_s2", "pool_row", ["membership"]),
        ("inside_s2", "pool_row", ["membership"]),
        ("inside_s3", "mirror", ["membership", "pool_row"]),
        ("inside_s4", "bars", ["membership", "pool_row", "mirror"]),
        ("between_s4", "bars", ["membership", "pool_row", "mirror"]),
    ],
)
def test_stage_crossing_matrix(crossing, crossed_stage, committed_before):
    runner, clock, radar, settings, poller = _crossing_runner(crossing)
    result = asyncio.run(runner.cycle())
    committed = [stage for stage, _instant in radar.commits]

    assert result.failed_stage == crossed_stage
    assert committed[: len(committed_before)] == committed_before
    if crossed_stage != "bars":
        assert crossed_stage not in committed
    assert all(instant < AT_RESET for _stage, instant in radar.commits)
    if crossing == "inside_s4":
        assert poller.written == poller.attempted[: poller.k]
    if crossing == "between_s4":
        assert poller.written == poller.attempted[: poller.k + 1]

    # A committed scan is idempotent when the same scan_id is re-applied.
    clock.value = NEXT_ACTIVE
    radar.crossing = None
    settings.crossing = None
    radar.apply_membership(
        pool_key=runner.config.pool_key,
        transitions=result.decision.transitions,
        scan_id=result.scan_id,
        now=clock.value,
        session=Session.RTH.value,
        before_commit=lambda: None,
    )
    before = deepcopy(radar.members)
    radar.apply_membership(
        pool_key=runner.config.pool_key,
        transitions=result.decision.transitions,
        scan_id=result.scan_id,
        now=clock.value,
        session=Session.RTH.value,
        before_commit=lambda: None,
    )
    assert radar.members == before

    # The first cycle after the pause must make the dropped stage observable.
    poller.crossing = None
    next_result = asyncio.run(runner.cycle())
    assert next_result.state == "scanning"
    assert radar.pool["failed_stage"] == crossed_stage
