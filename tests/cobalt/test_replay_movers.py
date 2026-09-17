"""S2-P4 STEP-6 — F13: unfiltered top movers, their i1 archive, the benchmark.

Charter F13: "a Tesla-class mover absent from the pool appears in the miss
line with excluded_by". Fixtures are hub-cut (L45): one unfiltered export
per side (movers-*.real-shape.csv) and the same day's membership episodes.

KNOWN SHAPE FACT (hub report §STEP-1): the movers exports were cut with
`v=152` and no `c=` column list, so they carry no `Asset Type` column. The
replay's live request sends radar.yaml's column list (which does); the
parser therefore requires only Ticker/Change/Volume, reads Asset Type when
present (proved on pool-metrics.real-shape.csv, a real c=0-150 export), and
records an absent one as `unreported` — never guessed to be an equity or
not.
"""

from __future__ import annotations

import asyncio
import hashlib
import os
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path

import pytest

from cobalt.archiver.models import Bar, Interval
from cobalt.radar.collector import SourceFailure
from cobalt.replay import movers as movers_mod
from cobalt.replay.line import render_line
from cobalt.replay.models import Episode, ReplayError, StoredMover
from cobalt.replay.movers import (
    SIDES,
    MoversStore,
    archive_movers,
    benchmark_misses,
    parse_change_pct,
    parse_movers,
    replay_request_count,
    retained_exports,
)
from cobalt.settings.models import SETTING_KEYS, BenchmarkSettings, TraderSettingsError

FIX = Path(__file__).resolve().parents[1] / "fixtures"
DAY = date(2026, 2, 10)
FETCHED = datetime(2026, 2, 11, 2, 5, tzinfo=timezone.utc)

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="requires_db: Postgres env settings not available",
)


def _export(side: str, top_n: int = 60):
    payload = (FIX / "replay" / f"movers-{side}.real-shape.csv").read_bytes()
    return parse_movers(payload, side=side, top_n=top_n, content_type="text/csv",
                        config=movers_mod.load_radar_config(), fetched_at=FETCHED, source="live")


def _stored(export, trade_date=DAY, start_id=1):
    return [
        StoredMover(id=start_id + i, trade_date=trade_date, side=row.side, rank=row.rank, ticker=row.ticker,
                    change_pct=row.change_pct, asset_type=row.asset_type, volume=row.volume, rvol=row.rvol,
                    export_sha256=export.export_sha256, fetched_at=export.fetched_at)
        for i, row in enumerate(export.rows)
    ]


@pytest.fixture(scope="module")
def episodes():
    import json

    raw = json.loads((FIX / "replay" / "membership-day.real-shape.json").read_text())["membership"]
    return [Episode(**{k: (datetime.fromisoformat(v) if k.endswith("_at") and v else v) for k, v in e.items()})
            for e in raw]


SETTINGS = BenchmarkSettings(top_n=60, min_move_pct=Decimal("30"))


# =====================================================================
# §4 F13
# =====================================================================


def test_tesla_class_mover_absent_from_pool_appears_in_miss_line_with_excluded_by(episodes):
    gainers, losers = _export("gainers"), _export("losers")
    movers = _stored(gainers) + _stored(losers, start_id=1000)
    rows = benchmark_misses(movers, episodes, settings=SETTINGS, trade_date=DAY,
                            not_equity_values=["Exchange Traded Fund"])
    by_ticker = {r.ticker: r for r in rows}
    # CTNT, the day's top gainer (+164.99%), has no membership episode at all
    assert by_ticker["CTNT"].excluded_by == "not_in_any_source"
    assert by_ticker["CTNT"].mover_id == 1
    assert by_ticker["CTNT"].gate_detail["change_pct"] == "164.99"
    line = render_line(DAY, card_rows=[], mover_rows=[r.model_dump() for r in rows], settings=SETTINGS,
                       formation_replay="unavailable", input_stale=0)
    assert "CTNT +165.0% not_in_any_source" in line


def test_admitted_mover_is_not_a_miss(episodes):
    movers = _stored(_export("gainers"))
    rows = benchmark_misses(movers, episodes, settings=BenchmarkSettings(top_n=60, min_move_pct=Decimal("1")),
                            trade_date=DAY, not_equity_values=[])
    tickers = {r.ticker for r in rows}
    admitted = {e.ticker for e in episodes if e.entered_at is not None}
    in_both = {m.ticker for m in movers} & admitted
    assert "AEHL" in in_both
    assert not (tickers & in_both)


def test_never_admitted_episode_supplies_its_excluded_by(episodes):
    movers = _stored(_export("gainers"))
    rows = {r.ticker: r for r in benchmark_misses(movers, episodes, settings=SETTINGS, trade_date=DAY,
                                                   not_equity_values=[])}
    daic = rows["DAIC"]                      # +106.47%, never admitted, config_cap
    assert daic.excluded_by == "config_cap"
    assert daic.pool_member_id is None or isinstance(daic.pool_member_id, int)
    assert daic.gate_detail["episodes"][0]["excluded_by"] == "config_cap"


def test_movers_archived_regardless_of_watchlist():
    movers = _stored(_export("gainers", top_n=3))
    fetched: list[str] = []
    store = _FakeBars()

    class Collector:
        async def bars(self, tickers, *, top_n):
            fetched.extend(tickers)
            return {t: _session_bars(t) for t in tickers}, {}

    outcome = asyncio.run(archive_movers(
        movers, collector=Collector(), bar_store=store, trade_date=SYN_DAY, rth_open=RTH_OPEN,
        close=CLOSE, top_n=3, dry_run=False,
    ))
    # no Lists note, no watchlist, no pool: the top-N are archived because they moved
    assert fetched == ["CTNT", "DAIC", "KXIN"]
    assert outcome.archived_ids == [1, 2, 3]
    assert outcome.failures == {}
    assert store.upserted == 3 * len(_session_bars("X"))


def test_benchmark_settings_absent_or_malformed_fails_loud():
    with pytest.raises(TraderSettingsError, match="no 'radar.benchmark' row"):
        BenchmarkSettings.from_rows({})
    for bad in ({"top_n": 0, "min_move_pct": 10}, {"top_n": 20}, {"top_n": 20, "min_move_pct": 10, "x": 1}, "20"):
        with pytest.raises(TraderSettingsError):
            BenchmarkSettings.from_rows({"radar.benchmark": bad})


def test_benchmark_key_not_in_required_setting_keys():
    assert "radar.benchmark" not in SETTING_KEYS


# =====================================================================
# Parsing against the real shapes
# =====================================================================


def test_parse_real_movers_exports_rank_in_export_order_and_hash_the_raw_bytes():
    gainers = _export("gainers", top_n=5)
    raw = (FIX / "replay" / "movers-gainers.real-shape.csv").read_bytes()
    assert gainers.export_sha256 == hashlib.sha256(raw).hexdigest()
    assert [(r.rank, r.ticker, r.change_pct) for r in gainers.rows[:3]] == [
        (1, "CTNT", Decimal("164.99")), (2, "DAIC", Decimal("106.47")), (3, "KXIN", Decimal("91.15"))]
    assert gainers.rows[0].volume == 534716664 and gainers.rows[0].rvol == Decimal("1007.37")
    assert gainers.rows[0].asset_type is None
    losers = _export("losers", top_n=2)
    assert losers.rows[0].change_pct == Decimal("-58.38")


def test_parse_reads_asset_type_from_a_full_column_export():
    payload = (FIX / "radar" / "pool-metrics.real-shape.csv").read_bytes()
    # A real c=0-150 export: the column is there, and for these stocks its
    # cells are BLANK — so blank reads as None (unreported), never as a guess.
    # It is not change-sorted, so only the column read is asserted.
    export = parse_movers(payload, side="gainers", top_n=20, content_type="text/csv",
                          config=movers_mod.load_radar_config(), fetched_at=FETCHED, source="live",
                          check_order=False)
    assert "Asset Type" in export.header
    assert {row.asset_type for row in export.rows} == {None}
    assert export.rows[0].rvol == Decimal("0.00")


def test_parse_refuses_the_wrong_sort_and_a_missing_column():
    losers = (FIX / "replay" / "movers-losers.real-shape.csv").read_bytes()
    with pytest.raises(SourceFailure, match="sort"):
        parse_movers(losers, side="gainers", top_n=10, content_type="text/csv",
                     config=movers_mod.load_radar_config(), fetched_at=FETCHED, source="live")
    header, _, rest = losers.partition(b"\n")
    with pytest.raises(SourceFailure, match="Change"):
        parse_movers(header.replace(b',"Change"', b"") + b"\n" + rest, side="losers", top_n=10,
                     content_type="text/csv", config=movers_mod.load_radar_config(), fetched_at=FETCHED,
                     source="live")


def test_change_pct_parsing_is_strict():
    assert parse_change_pct("164.99%") == Decimal("164.99")
    assert parse_change_pct("-0.60%") == Decimal("-0.60")
    for bad in ("", "-", "abc%", "12"):
        with pytest.raises(SourceFailure):
            parse_change_pct(bad)


def test_request_count_and_sides():
    assert replay_request_count(20) == 42
    assert SIDES == {"gainers": "-change", "losers": "change"}


# =====================================================================
# R1-20 — reruns, both sides, history
# =====================================================================


def test_r1_20_a_ticker_on_both_sides_resolves_to_one_missed_row(episodes):
    gainers = _export("gainers", top_n=1)
    losers = _export("losers", top_n=1)
    twin = _stored(gainers)[0]
    other = _stored(losers, start_id=50)[0].model_copy(update={"ticker": twin.ticker, "change_pct": Decimal("-170")})
    rows = benchmark_misses([twin, other], episodes, settings=SETTINGS, trade_date=DAY, not_equity_values=[])
    assert len(rows) == 1
    assert rows[0].mover_id == 50                           # the larger |change| carries the row
    assert sorted(rows[0].gate_detail["sides"]) == ["gainers", "losers"]


def test_r1_20_multiple_never_admitted_episodes_pick_the_most_recent(episodes):
    mover = _stored(_export("gainers", top_n=1))[0]
    older = Episode(id=1, ticker=mover.ticker, trade_date=DAY, excluded_by="not_equity",
                    first_seen_at=datetime(2026, 2, 10, 9, tzinfo=timezone.utc))
    newer = Episode(id=2, ticker=mover.ticker, trade_date=DAY, excluded_by="screen_inactive",
                    first_seen_at=datetime(2026, 2, 10, 15, tzinfo=timezone.utc))
    rows = benchmark_misses([mover], [older, newer], settings=SETTINGS, trade_date=DAY, not_equity_values=[])
    assert rows[0].excluded_by == "screen_inactive"
    assert rows[0].pool_member_id == 2


def test_not_equity_movers_leave_the_benchmark_and_unreported_asset_type_stays_in(episodes):
    movers = _stored(_export("gainers", top_n=2))
    etf = movers[0].model_copy(update={"asset_type": "Exchange Traded Fund"})
    rows = benchmark_misses([etf, movers[1]], [], settings=SETTINGS, trade_date=DAY,
                            not_equity_values=["Exchange Traded Fund"])
    assert [r.ticker for r in rows] == [movers[1].ticker]
    assert rows[0].gate_detail["asset_type"] == "unreported"


def test_r1_20_an_unavailable_historical_date_refuses(tmp_path):
    with pytest.raises(ReplayError, match="no retained movers export"):
        retained_exports(tmp_path, DAY, top_n=10, config=movers_mod.load_radar_config())


def test_r1_20_a_retained_historical_export_is_read_not_refetched(tmp_path):
    folder = tmp_path / DAY.isoformat()
    folder.mkdir()
    for side in SIDES:
        (folder / f"movers-{side}-210512.csv").write_bytes((FIX / "replay" / f"movers-{side}.real-shape.csv").read_bytes())
    exports = retained_exports(tmp_path, DAY, top_n=3, config=movers_mod.load_radar_config())
    assert [(e.side, e.source, len(e.rows)) for e in exports] == [("gainers", "retained", 3), ("losers", "retained", 3)]
    assert exports[0].fetched_at == datetime(2026, 2, 10, 21, 5, 12, tzinfo=movers_mod.ET)


def test_dry_run_export_is_not_cached(tmp_path, monkeypatch):
    payload = (FIX / "replay" / "movers-gainers.real-shape.csv").read_bytes()
    losers = (FIX / "replay" / "movers-losers.real-shape.csv").read_bytes()
    monkeypatch.setattr(movers_mod, "check_scheduled_demand", lambda *a, **k: None)

    class Response:
        def __init__(self, content):
            self.content = content

    async def get(path, params, token, on_metrics=None):
        from cobalt.archiver.collector import FetchMetrics

        on_metrics(FetchMetrics(status=200, elapsed_ms=1.0, bytes=1, content_type="text/csv"))
        assert "f" not in params                     # unfiltered: no filter string, ever
        return Response(payload if params["o"] == "-change" else losers)

    collector = movers_mod.MoversCollector("t", config=movers_mod.load_radar_config(), bucket=_NoWait(),
                                           cache_root=tmp_path, get=get)
    exports = asyncio.run(collector.exports(top_n=2, now=FETCHED, cache=False, trade_date=DAY))
    assert [e.side for e in exports] == ["gainers", "losers"]
    assert list(tmp_path.iterdir()) == []
    cached = asyncio.run(collector.exports(top_n=2, now=FETCHED, cache=True, trade_date=DAY))
    assert sorted(p.name.split("-")[1] for p in (tmp_path / DAY.isoformat()).iterdir()) == ["gainers", "losers"]
    assert cached[0].cache_path


def test_archive_counts_failures_and_incomplete_coverage_and_never_marks_them_archived():
    movers = _stored(_export("gainers", top_n=3))

    class Collector:
        async def bars(self, tickers, *, top_n):
            return ({"CTNT": _session_bars("CTNT"), "DAIC": _session_bars("DAIC")[:30]},
                    {"KXIN": "CollectorError: HTTP 429"})

    outcome = asyncio.run(archive_movers(movers, collector=Collector(), bar_store=_FakeBars(), trade_date=SYN_DAY,
                                         rth_open=RTH_OPEN, close=CLOSE, top_n=3, dry_run=False))
    assert outcome.archived_ids == [1]
    assert outcome.incomplete == ["DAIC"]
    assert outcome.failures == {"KXIN": "CollectorError: HTTP 429"}


def test_archive_skips_tickers_already_covered_and_dry_run_fetches_nothing():
    movers = _stored(_export("gainers", top_n=2))
    store = _FakeBars(existing={"CTNT": _session_bars("CTNT")})

    class Collector:
        async def bars(self, tickers, *, top_n):
            raise AssertionError("dry run fetched")

    outcome = asyncio.run(archive_movers(movers, collector=Collector(), bar_store=store, trade_date=SYN_DAY,
                                         rth_open=RTH_OPEN, close=CLOSE, top_n=2, dry_run=True))
    assert outcome.archived_ids == [1]
    assert outcome.would_fetch == ["DAIC"]
    assert store.upserted == 0


def test_archive_refuses_work_that_cannot_fit_before_the_deadline():
    movers = _stored(_export("gainers", top_n=3))

    class Collector:
        rpm = 1

        async def bars(self, tickers, *, top_n):
            raise AssertionError("fetched past the deadline")

    with pytest.raises(ReplayError, match="deadline"):
        asyncio.run(archive_movers(movers, collector=Collector(), bar_store=_FakeBars(), trade_date=SYN_DAY,
                                   rth_open=RTH_OPEN, close=CLOSE, top_n=3, dry_run=False,
                                   now=CLOSE, deadline=CLOSE + timedelta(minutes=2), rpm=1))


@requires_db
def test_r1_20_changed_top_n_rerun_deactivates_never_deletes_and_identical_rerun_is_a_noop(dev_db_tx):
    store = MoversStore()
    first = [_export("gainers", top_n=3), _export("losers", top_n=3)]
    active = store.reconcile(run_id="m1", trade_date=SYN_DAY, exports=first)
    assert len(active) == 6
    again = store.reconcile(run_id="m2", trade_date=SYN_DAY, exports=first)
    assert sorted(m.id for m in again) == sorted(m.id for m in active)
    narrower = [_export("gainers", top_n=2), _export("losers", top_n=2)]
    after = store.reconcile(run_id="m3", trade_date=SYN_DAY, exports=narrower)
    assert len(after) == 4
    from cobalt import db

    with db.connect(store.db_name, side=db.Side.SYSTEM) as conn:
        total, inactive = conn.execute(
            "SELECT count(*), count(*) FILTER (WHERE NOT active) FROM movers_daily WHERE trade_date = %s",
            (SYN_DAY,)).fetchone()
    assert (total, inactive) == (6, 2)
    store.mark_bars_archived([after[0].id])
    assert {m.id for m in store.active(SYN_DAY) if m.bars_archived} == {after[0].id}


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

SYN_DAY = date(2026, 9, 3)
RTH_OPEN = datetime(2026, 9, 3, 13, 30, tzinfo=timezone.utc)
CLOSE = datetime(2026, 9, 3, 20, 0, tzinfo=timezone.utc)


def _session_bars(ticker: str) -> list[Bar]:
    return [Bar(ticker=ticker, interval=Interval.I1, ts=RTH_OPEN + timedelta(minutes=m - 1), open=Decimal(1),
                high=Decimal(1), low=Decimal(1), close=Decimal(1), volume=1) for m in range(0, 391)]


class _FakeBars:
    def __init__(self, existing=None):
        self.existing = dict(existing or {})
        self.upserted = 0

    def bars_between(self, ticker, interval, start, end):
        return [b for b in self.existing.get(ticker, []) if start <= b.ts < end]

    def upsert_bars(self, bars):
        for b in bars:
            self.existing.setdefault(b.ticker, []).append(b)
        self.upserted += len(bars)
        return len(bars)


class _NoWait:
    async def acquire(self):
        return None
