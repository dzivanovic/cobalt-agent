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
    ARCHIVER_LABEL,
    REPLAY_LABEL,
    DemandConsumer,
    DemandWindow,
    TotalDemandExceeded,
    check_scheduled_demand,
    check_total_demand,
    load_sources,
    replay_window,
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
    assert consumers["replay"].window.start_min == 21 * 60 + 10
    assert consumers["replay"].rpm == 40            # min(2 + 2 x 20, bucket ceiling)
    # the replay window closes before the 21:40 backup
    assert consumers["replay"].window.end_min <= 21 * 60 + 40


# =====================================================================
# S2-P4 R17 — ceiling 50, disjoint archiver/replay windows
#
# Ruled 2026-09-17 (Dejan, "50 is approved."): three numbers, zero pacing
# change. `radar.finviz_max_rpm` 45 -> 50 (= the archiver's own pacing
# bound 60/GENTLE_SLEEP_SECONDS = 60/1.2 = 50.0, so the archiver sits at
# EXACTLY the ceiling and `50.0 > 50` is False), the archiver's
# `timeout_s` 5400 -> 2400 (its declared window now ends at 21:10), and
# the replay's `at` 21:05 -> 21:10 (its window starts where the
# archiver's ends, so the two are disjoint under `overlaps`).
#
# These read the SHIPPED jobs.yaml/tunables.yaml through the real
# loaders — no mocked numbers. That is the point: they fail the moment
# any of the three drifts.
# =====================================================================

#: The radar's planned total transport demand — pool 30.00 + 4 screens
#: 2.40 + 7 list chunks 4.20 (cto-2026-09-17.md; the same 36.60 the
#: `screens validate` budget line prints).
RADAR_PLANNED_RPM = 36.6
#: The replay's benchmarked top-N: 2 exports + 2 x 20 movers = 42 rpm.
REPLAY_TOP_N = 20


def test_r17_every_scheduled_subject_passes_against_the_shipped_ceiling_of_50():
    assert notes_mod._ceiling() == 50
    kw = dict(radar_rpm=RADAR_PLANNED_RPM, replay_top_n=REPLAY_TOP_N)
    radar = check_scheduled_demand("radar", **kw)
    archiver = check_scheduled_demand("archiver", **kw)
    replay = check_scheduled_demand("replay", **kw)
    # each subject's window holds only its own demand — the windows are disjoint
    assert radar.peak_rpm == pytest.approx(RADAR_PLANNED_RPM)
    assert archiver.peak_rpm == pytest.approx(50.0)  # exactly the ceiling, and it passes
    assert replay.peak_rpm == pytest.approx(42.0)    # 2 + 2 x 20
    for demand in (radar, archiver, replay):
        assert demand.ceiling == 50
        assert demand.peak_rpm <= 50, demand.describe()


def test_r17_the_shipped_archiver_and_replay_windows_are_disjoint():
    consumers = {c.name: c for c in scheduled_consumers(
        ceiling=50, radar_rpm=RADAR_PLANNED_RPM, replay_top_n=REPLAY_TOP_N)}
    archiver, replay = consumers["archiver"].window, consumers["replay"].window
    # 20:30 + 2400 s = 21:10; 21:10 to the 21:40 backup less the 300 s margin
    assert archiver.describe() == "20:30-21:10 ET"
    assert replay.describe() == "21:10-21:35 ET"
    assert replay_window().describe() == "21:10-21:35 ET"
    # [20:30, 21:10) and [21:10, 21:35) touch but do not overlap
    assert not archiver.overlaps(replay)
    assert not replay.overlaps(archiver)
    # ...and the gate agrees: neither subject counts the other's rpm
    every = list(consumers.values())
    assert "replay" not in total_demand(every, subject="archiver", ceiling=50).counted
    assert "archiver" not in total_demand(every, subject="replay", ceiling=50).counted


def test_r17_at_ceiling_49_the_archiver_alone_is_refused_and_at_50_it_is_not():
    """The exact-boundary proof R17's arithmetic promises: the archiver's
    pacing bound is 60/1.2 = 50.0 rpm, so 49 refuses it and 50 does not.
    """
    consumers = scheduled_consumers(ceiling=49, radar_rpm=RADAR_PLANNED_RPM, replay_top_n=REPLAY_TOP_N)
    archiver = next(c for c in consumers if c.name == "archiver")
    assert archiver.rpm == pytest.approx(60 / archiver_runner.GENTLE_SLEEP_SECONDS)
    assert archiver.rpm == pytest.approx(50.0)
    with pytest.raises(TotalDemandExceeded, match="archiver"):
        check_total_demand(consumers, subject="archiver", ceiling=49)
    assert check_total_demand(consumers, subject="archiver", ceiling=50).peak_rpm == pytest.approx(50.0)


def test_r17_a_2105_replay_would_overlap_the_archiver_and_be_refused_at_50():
    """The overlap detection itself, independent of today's shipped `at`:
    roll the replay back to its pre-R17 21:05 against the real archiver
    window and the two windows overlap again — the archiver's 50.0 rpm is
    counted into the replay's total and 92.0 rpm is refused at 50.
    """
    from cobalt.jobs.config import load_job_registry

    shipped = load_job_registry()
    old = shipped.spec(REPLAY_LABEL)
    rolled_back = old.model_copy(update={"schedule": old.schedule.model_copy(update={"at": "21:05"})})
    registry = shipped.model_copy(update={
        "jobs": [rolled_back if j.label == REPLAY_LABEL else j for j in shipped.jobs]})
    assert registry.spec(REPLAY_LABEL).schedule.at == "21:05"
    assert registry.spec(ARCHIVER_LABEL).timeout_s == 2400, "the archiver's real window must be untouched"

    consumers = {c.name: c for c in scheduled_consumers(
        ceiling=50, radar_rpm=RADAR_PLANNED_RPM, replay_top_n=REPLAY_TOP_N, registry=registry)}
    archiver, replay = consumers["archiver"].window, consumers["replay"].window
    assert archiver.describe() == "20:30-21:10 ET"   # the shipped 2400 s, unchanged
    assert replay.describe() == "21:05-21:35 ET"
    assert archiver.overlaps(replay) and replay.overlaps(archiver)

    every = list(consumers.values())
    demand = total_demand(every, subject="replay", ceiling=50)
    assert set(demand.counted) >= {"archiver", "replay"}
    assert demand.peak_rpm == pytest.approx(50.0 + 42.0)
    with pytest.raises(TotalDemandExceeded, match="replay"):
        check_total_demand(every, subject="replay", ceiling=50)


class _NoWaitBucket:
    async def acquire(self) -> None:
        return None
