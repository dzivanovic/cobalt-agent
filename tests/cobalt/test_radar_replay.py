"""Pure replay synthesis plus the bounded all-day offline gate."""

import argparse
from copy import deepcopy
from dataclasses import replace
from datetime import datetime, time, timezone
from decimal import Decimal
import json
from pathlib import Path
from types import SimpleNamespace
from zoneinfo import ZoneInfo

import pytest

from cobalt.archiver.collector import scrub
from cobalt.archiver.models import Bar, Interval
from cobalt.radar.models import ExcludeBlock, ListBlock, ScreenBlock
from cobalt.radar.notes import load_sources
from cobalt.radar.pool import Action
from cobalt.radar.replay import ReplayCollector, snapshots_from_bars
from cobalt.radar import runner as runner_module
from cobalt.session.models import Session


def _screen(f="exch_nasd,sh_avgvol_o500"):
    return ScreenBlock(screen="example_session_scan", f=f, sort="-volume", columns=[0], active_from="10:00", active_to="16:00", enabled=True)


def _bar(day, volume):
    return Bar(ticker="AAA", interval=Interval.I1, ts=datetime(2026, 9, day, 14, 0, tzinfo=timezone.utc), open=Decimal(1), high=Decimal(1), low=Decimal(1), close=Decimal(1), volume=volume)


def test_snapshot_rvol_proxy_uses_prior_session_same_minute():
    rows = snapshots_from_bars([_bar(2, 10), _bar(3, 20)], _screen(), 1)
    assert rows[-1].rows[0]["Relative Volume"] == "2.000000"


def test_unknown_fixture_filter_code_fails_loud():
    with pytest.raises(ValueError, match="does_not_exist"):
        snapshots_from_bars([_bar(2, 10), _bar(3, 20)], _screen("does_not_exist"), 1)


ET = ZoneInfo("America/New_York")
FIXTURES = Path("tests/fixtures/radar")


class ReplayClock:
    def __init__(self):
        self.seen = []

    def session(self, instant):
        wall = instant.astimezone(ET).time()
        if time(20) <= wall < time(21):
            value = Session.MARKET_RESET
        elif time(16) <= wall < time(20):
            value = Session.AFTERMARKET
        elif time(9, 30) <= wall < time(16):
            value = Session.RTH
        elif time(4) <= wall < time(9, 30):
            value = Session.PREMARKET
        else:
            value = Session.OVERNIGHT
        self.seen.append((instant, value))
        return value

    def to_et(self, instant):
        return instant.astimezone(ET)


class ReplayRadarStore:
    last = None

    def __init__(self):
        type(self).last = self
        self.pool = None
        self.open = {}
        self.events = []

    def pool_row(self, _key):
        return deepcopy(self.pool)

    def open_members(self, _key):
        return [deepcopy(value) for value in self.open.values()]

    def apply_membership(self, *, transitions, scan_id, now, before_commit, **_kwargs):
        before_commit()
        for item in transitions:
            self.events.append((now.astimezone(ET), item.model_copy()))
            if item.action in {Action.ADMIT, Action.RETAIN, Action.HOLD}:
                previous = self.open.get(item.ticker, {})
                self.open[item.ticker] = {
                    "ticker": item.ticker,
                    "sources": item.sources,
                    "entered_at": previous.get("entered_at") or now,
                    "below_cap_streak": item.below_cap_streak,
                    "last_rank": item.rank,
                    "trade_date": now.astimezone(ET).date().isoformat(),
                }
            elif item.action is Action.EXCLUDE:
                self.open[item.ticker] = {
                    "ticker": item.ticker,
                    "sources": item.sources,
                    "entered_at": None,
                    "below_cap_streak": item.below_cap_streak,
                    "last_rank": item.rank,
                    "trade_date": now.astimezone(ET).date().isoformat(),
                }
            elif item.action is Action.LEAVE:
                self.open.pop(item.ticker, None)

    def put_pool(self, row, *, before_commit, **_kwargs):
        before_commit()
        self.pool = deepcopy(row)

    def stamp_failure(self, _key, *, before_commit, **kwargs):
        before_commit()
        self.pool.update(kwargs)

    def stamp_poll(self, _key, *, polled_at, poll_failures, before_commit):
        before_commit()
        self.pool["last_poll_at"] = polled_at
        self.pool["poll_failures"] = poll_failures


class ReplaySettingsStore:
    def __init__(self):
        self.rows = {}

    def values(self):
        return deepcopy(self.rows)

    def put(self, rows, *, before_commit, **_kwargs):
        before_commit()
        self.rows = deepcopy(rows)
        return {key: "created" for key in rows}


class RecordingReplayCollector(ReplayCollector):
    calls = []

    async def screen(self, block, now):
        type(self).calls.append(("screen", now, block.model_copy()))
        return await super().screen(block, now)

    async def listed(self, block, now):
        type(self).calls.append(("list", now, block.model_copy()))
        return await super().listed(block, now)


def _generated_bars(tickers):
    prior = datetime(2026, 9, 2, tzinfo=ET)
    target = datetime(2026, 9, 3, tzinfo=ET)
    bars = []

    def add(day, hh, mm, ticker, volume):
        instant = day.replace(hour=hh, minute=mm).astimezone(timezone.utc)
        bars.append(
            Bar(
                ticker=ticker,
                interval=Interval.I1,
                ts=instant,
                open=Decimal(1),
                high=Decimal(1),
                low=Decimal(1),
                close=Decimal(1),
                volume=volume,
            )
        )

    # Prior-session same-minute cumulative baselines make the RTH rank
    # deliberately differ from the surrounding volume ranks.
    for index, ticker in enumerate(tickers):
        baseline = 1 if index in {2, 8} else 1_000_000
        for hh, mm in ((4, 0), (9, 30), (10, 0), (16, 0)):
            add(prior, hh, mm, ticker, baseline)

    for index, ticker in enumerate(tickers):
        add(target, 4, 0, ticker, 1_000 - index * 50)
    add(target, 4, 1, tickers[5], 100_000)
    for ticker in tickers:
        add(target, 9, 30, ticker, 1)
    add(target, 10, 0, tickers[8], 5_000)
    add(target, 16, 0, tickers[6], 1_000_000)
    return bars


def _at(events, hh, mm):
    return [row for instant, row in events if instant.hour == hh and instant.minute == mm]


def test_all_day_scan_replay_offline_acceptance_matrix(tmp_path, monkeypatch, capsys):
    parsed = load_sources(
        FIXTURES / "radar-screens.example.md",
        FIXTURES / "radar-lists.example.md",
        scan_interval=60,
        poll_interval=60,
        finviz_max_rpm=100,
        list_chunk_size=50,
    )
    screen_item = next(item for item in parsed.screens.blocks if isinstance(item.block, ScreenBlock))
    pool_item = next(item for item in parsed.screens.blocks if item.key == "pool")
    list_item = next(item for item in parsed.lists.blocks if isinstance(item.block, ListBlock))
    exclude = next(item.block for item in parsed.lists.blocks if isinstance(item.block, ExcludeBlock))
    candidates = [ticker for ticker in list_item.block.tickers if ticker not in exclude.tickers][:10]
    manual_ticker = exclude.tickers[0]
    tickers = candidates + [manual_ticker]
    screen_only = candidates[8]
    etf_ticker = candidates[9]

    # R2 variants are copies of the fixture models, never new definitions.
    screen_variant = screen_item.block.model_copy()
    pool_variant = pool_item.block.model_copy()
    list_variant = list_item.block.model_copy(
        update={"tickers": [ticker for ticker in list_item.block.tickers if ticker != screen_only]}
    )
    parsed.screens.blocks = [
        replace(item, block=screen_variant if item is screen_item else pool_variant)
        for item in parsed.screens.blocks
    ]
    parsed.lists.blocks = [
        replace(item, block=list_variant) if item is list_item else item
        for item in parsed.lists.blocks
    ]
    parsed.pool = pool_variant

    cfg = runner_module.load_config()
    cfg = cfg.model_copy(update={"not_equity": cfg.not_equity.model_copy()})
    snapshots = snapshots_from_bars(_generated_bars(tickers), screen_variant, prior_sessions=1)
    asset_type = next(iter(cfg.not_equity.values))
    snapshots = [
        replace(
            snapshot,
            rows=tuple(
                {**row, cfg.not_equity.header: asset_type if row["Ticker"] == etf_ticker else "Stock"}
                for row in snapshot.rows
            ),
            header=(*snapshot.header, cfg.not_equity.header),
        )
        for snapshot in snapshots
    ]
    replay_dir = tmp_path / "replay"
    replay_dir.mkdir()
    replay_file = replay_dir / "2026-09-03.json"
    replay_file.write_text(
        json.dumps([{"at": item.at.isoformat(), "rows": list(item.rows)} for item in snapshots])
    )

    clock = ReplayClock()
    finviz_calls = []

    async def no_finviz(*args, **kwargs):
        finviz_calls.append((args, kwargs))
        raise AssertionError(scrub("Finviz called during offline replay"))

    monkeypatch.setattr(runner_module, "Path", lambda value: replay_dir if str(value) == "data/radar-replay" else Path(value))
    monkeypatch.setattr(runner_module, "RadarStore", ReplayRadarStore)
    monkeypatch.setattr(runner_module, "TraderSettingsStore", ReplaySettingsStore)
    monkeypatch.setattr(runner_module, "configured_sources", lambda: parsed)
    monkeypatch.setattr(runner_module, "load_config", lambda: cfg)
    monkeypatch.setattr(runner_module, "session_clock", lambda: clock)
    monkeypatch.setattr(
        runner_module,
        "load_tunables",
        lambda: SimpleNamespace(by_key={"radar.scan_interval": SimpleNamespace(value=60)}),
    )
    monkeypatch.setattr("cobalt.radar.replay.ReplayCollector", RecordingReplayCollector)
    monkeypatch.setattr("cobalt.archiver.collector.finviz_get", no_finviz)
    monkeypatch.setattr("cobalt.radar.collector.finviz_get", no_finviz)
    RecordingReplayCollector.calls = []

    overnight = runner_module.RadarRunner(
        config=cfg,
        sources_loader=lambda: (_ for _ in ()).throw(
            AssertionError(scrub("overnight loaded sources"))
        ),
        collector=SimpleNamespace(),
        radar_store=SimpleNamespace(),
        settings_store=SimpleNamespace(),
        poller=SimpleNamespace(),
        clock=clock,
        now=lambda: datetime(2026, 9, 3, 3, 59, tzinfo=ET),
    )
    assert __import__("asyncio").run(overnight.cycle()).state == "idle:overnight"

    runner_module.scan_command(
        argparse.Namespace(replay="2026-09-03", from_time="04:00", to_time="20:30")
    )
    output = scrub(capsys.readouterr().out)
    store = ReplayRadarStore.last
    assert "admit=" in output and "leave=" in output
    assert any(row.action is Action.ADMIT for _instant, row in store.events)
    assert any(row.action is Action.LEAVE for _instant, row in store.events)

    screen_prefix = f"screen:{screen_variant.screen}@"
    assert not any(
        instant.time() < time(10) and row.action is Action.ADMIT and (row.source or "").startswith(screen_prefix)
        for instant, row in store.events
    )
    after_open = _at(store.events, 10, 0)
    assert next(row for row in after_open if row.rank == 1).source.startswith(screen_prefix)

    assert next(row.ticker for row in _at(store.events, 9, 29) if row.rank == 1) == candidates[5]
    assert next(row.ticker for row in _at(store.events, 9, 30) if row.rank == 1) == candidates[2]
    assert next(row.ticker for row in _at(store.events, 16, 0) if row.rank == 1) == candidates[6]

    assert any(row.action is Action.RETAIN and row.below_cap_streak > 0 for _, row in store.events)
    assert any(
        row.action is Action.LEAVE and row.below_cap_streak == pool_variant.stickiness_scans + 1
        for _, row in store.events
    )
    excluded = {row.excluded_by.value for _, row in store.events if row.excluded_by is not None}
    assert excluded == {"config_cap", "manual", "not_equity", "screen_inactive"}

    called_sessions = {clock.session(instant) for _kind, instant, _block in RecordingReplayCollector.calls}
    assert Session.OVERNIGHT not in called_sessions
    assert Session.MARKET_RESET not in called_sessions
    assert Session.MARKET_RESET in {session for _instant, session in clock.seen}
    assert finviz_calls == []
