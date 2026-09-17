"""S2-P4 STEP-6 / L53 — ONE total Finviz demand across every consumer.

L53: "A budget check that measures one consumer is not a budget check: the
total-demand computation across every consumer of a shared transport is the
rule, with a test proving refusal when the total exceeds the ceiling while
one consumer alone would pass." Astra R1-13/R2-5: one named shared gate,
`check_total_demand`, called before the request at every pre-request site —
radar's `load_sources`, the archiver's runner, and replay's movers exports
and bar fetches — and the refusal test exercises those call sites.
"""

from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from pathlib import Path

import pytest

from cobalt.archiver import runner as archiver_runner
from cobalt.radar import notes as notes_mod
from cobalt.radar.notes import (
    DemandConsumer,
    DemandWindow,
    TotalDemandExceeded,
    check_total_demand,
    load_sources,
    scheduled_consumers,
    total_demand,
)
from cobalt.replay import movers as movers_mod

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures" / "radar"


def w(start: str, end: str) -> DemandWindow:
    return DemandWindow.between(start, end)


def test_total_finviz_demand_refuses_when_sum_exceeds_ceiling_while_replay_alone_passes(monkeypatch):
    replay = DemandConsumer(name="replay", rpm=30, window=w("21:05", "21:35"), basis="2 + 2 x top_n")
    archiver = DemandConsumer(name="archiver", rpm=20, window=w("20:30", "22:00"), basis="pacing bound")
    # alone, replay fits under 40
    assert check_total_demand([replay], subject="replay", ceiling=40).peak_rpm == 30
    # together, over the same minutes, they do not
    with pytest.raises(TotalDemandExceeded, match="replay"):
        check_total_demand([replay, archiver], subject="replay", ceiling=40)

    # -- and the CALL SITES refuse before any request --------------------
    monkeypatch.setattr(notes_mod, "scheduled_consumers", lambda **kw: [replay, archiver])
    monkeypatch.setattr(notes_mod, "_ceiling", lambda: 40)

    requested: list[str] = []

    async def fetch_forbidden(*args, **kwargs):
        requested.append("request")
        raise AssertionError("a request was made past a refusing demand gate")

    # replay's movers exports and bar fetches
    collector = movers_mod.MoversCollector(
        "token", config=movers_mod.load_radar_config(), bucket=_NoWaitBucket(), cache_root=Path("/nonexistent"),
        get=fetch_forbidden, fetch_bars=fetch_forbidden,
    )
    with pytest.raises(TotalDemandExceeded):
        asyncio.run(collector.exports(top_n=10, now=datetime(2026, 9, 3, 1, 5, tzinfo=timezone.utc), cache=False))
    with pytest.raises(TotalDemandExceeded):
        asyncio.run(collector.bars(["AAA"], top_n=10))

    # the archiver's runner path
    monkeypatch.setattr(archiver_runner, "resolve_token", fetch_forbidden)
    monkeypatch.setattr(archiver_runner, "fetch_bars", fetch_forbidden)
    with pytest.raises(TotalDemandExceeded):
        asyncio.run(archiver_runner._run_targets([("AAA", archiver_runner.Interval.I1)], mode="full"))
    assert requested == []


def test_radar_load_sources_counts_the_other_consumers_in_its_window():
    screens, lists = FIXTURES / "radar-screens.example.md", FIXTURES / "radar-lists.example.md"
    # context_tickers is S2-P2's required kwarg: these fixtures poll none.
    kwargs = dict(scan_interval=60, poll_interval=60, finviz_max_rpm=100,
                  list_chunk_size=50, context_tickers=0)
    alone = load_sources(screens, lists, **kwargs)
    assert alone.pool_error is None, alone.pool_error
    planned = alone.planned_rpm
    overlapping = DemandConsumer(name="archiver", rpm=101 - planned, window=None, basis="test")
    crowded = load_sources(screens, lists, radar_window=w("04:00", "20:00"),
                           other_consumers=[overlapping], **kwargs)
    assert "pool budget exceeded" in crowded.pool_error
    assert "archiver" in crowded.pool_error
    disjoint = overlapping.model_copy(update={"window": w("20:30", "22:00")})
    fine = load_sources(screens, lists, radar_window=w("04:00", "20:00"), other_consumers=[disjoint], **kwargs)
    assert fine.pool_error is None


def test_disjoint_windows_contribute_zero_and_unbounded_windows_always_count():
    radar = DemandConsumer(name="radar", rpm=36, window=w("04:00", "20:00"), basis="planned")
    archiver = DemandConsumer(name="archiver", rpm=50, window=w("20:30", "22:00"), basis="bound")
    assert total_demand([radar, archiver], subject="radar", ceiling=40).peak_rpm == 36
    assert total_demand([radar, archiver], subject="archiver", ceiling=40).peak_rpm == 50
    forever = DemandConsumer(name="p2_daily", rpm=5, window=None, basis="unbounded")
    assert total_demand([radar, archiver, forever], subject="radar", ceiling=40).peak_rpm == 41


def test_unmeasured_ceiling_refuses():
    replay = DemandConsumer(name="replay", rpm=1, window=None, basis="x")
    with pytest.raises(TotalDemandExceeded, match="unmeasured"):
        check_total_demand([replay], subject="replay", ceiling=None)


def test_scheduled_consumers_read_the_registry_and_never_omit_the_archiver():
    consumers = {c.name: c for c in scheduled_consumers(replay_top_n=20, ceiling=40)}
    assert {"radar", "archiver", "replay"} <= set(consumers)
    assert consumers["archiver"].window.start_min == 20 * 60 + 30
    assert consumers["archiver"].rpm == pytest.approx(60 / archiver_runner.GENTLE_SLEEP_SECONDS)
    assert consumers["replay"].window.start_min == 21 * 60 + 5
    assert consumers["replay"].rpm == 40            # min(2 + 2 x 20, bucket ceiling)
    # the replay window closes before the 21:40 backup
    assert consumers["replay"].window.end_min <= 21 * 60 + 40


class _NoWaitBucket:
    async def acquire(self) -> None:
        return None
