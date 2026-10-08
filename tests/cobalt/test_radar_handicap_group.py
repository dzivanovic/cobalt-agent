"""Float handicap H1 STEP-3 (v3 §3 [F-10]): float and cap into
`SourceSet.metrics`, the ONE group verdict, the redacted real-shape screen
export, and the homogeneous-screen case (RED here, GREEN at STEP-4).

Thresholds are this file's literals 20 / 300 (via `test_radar_handicap`'s
`block()`), never his (L32, L69).
"""

from __future__ import annotations

import asyncio
import csv
import io
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path
from zoneinfo import ZoneInfo

import pytest
from test_radar_handicap import FIXTURES, block, pool

from cobalt.radar.collector import ScreenerSnapshot, parse_screener_csv
from cobalt.radar.config import is_not_equity, load_config
from cobalt.radar.handicap import GroupVerdict, handicap_group
from cobalt.radar.models import Candidate, HandicapBlock, PoolBlock, SourceSet
from cobalt.radar.notes import load_sources
from cobalt.radar.pool import _ranked
from cobalt.radar.runner import RadarRunner, _number

REPLAY_FIXTURES = Path(__file__).resolve().parents[1] / "fixtures" / "replay"
POOL_METRICS = FIXTURES / "pool-metrics.real-shape.csv"
SCREEN_FIXTURE = FIXTURES / "screen-handicap.real-shape.csv"
#: 10:30 ET on a constructed trading day: the example screen is active.
INSTANT = datetime(2026, 9, 3, 14, 30, tzinfo=timezone.utc)


# ---------------------------------------------------------------------
# (i) float and cap enter SourceSet.metrics through `_collect`
# ---------------------------------------------------------------------


class _Clock:
    def to_et(self, value):
        return value.astimezone(ZoneInfo("America/New_York"))


class _CsvCollector:
    """The collector's `screen` call, serving one committed export."""

    def __init__(self, path: Path, config):
        self.header, self.rows = parse_screener_csv(
            path.read_bytes(), source="screen-fixture",
            required_headers=config.export.required_headers, content_type="text/csv",
        )

    async def screen(self, _block, now):
        return ScreenerSnapshot("screen-fixture", now, self.rows, self.header)

    async def listed(self, _block, now):
        return []


def collect(path: Path):
    config = load_config()
    parsed = load_sources(
        FIXTURES / "radar-screens.example.md", FIXTURES / "radar-lists.example.md",
        scan_interval=60, poll_interval=60, finviz_max_rpm=None, list_chunk_size=1, context_tickers=0,
    )
    collector = _CsvCollector(path, config)
    runner = RadarRunner(config=config, sources_loader=lambda: parsed, collector=collector,
                         radar_store=None, settings_store=None, poller=None, clock=_Clock())
    candidates, source_sets = asyncio.run(runner._collect(parsed, INSTANT, []))
    return config, collector.rows, candidates, source_sets


def test_collect_puts_float_and_cap_into_metrics_through_number_and_the_config_headers():
    config, rows, _candidates, source_sets = collect(POOL_METRICS)
    (screen,) = [s for s in source_sets if s.kind == "screen"]
    headers = config.export.handicap_headers
    assert rows
    for row in rows:
        ticker = row["Ticker"].strip().upper()
        assert screen.metrics[ticker] == {
            "volume": _number(row.get(config.export.metric_headers.volume)),
            "rvol": _number(row.get(config.export.metric_headers.rvol)),
            "float_m": _number(row.get(headers.float)),
            "market_cap_m": _number(row.get(headers.market_cap)),
            "price": _number(row.get(config.export.metric_headers.price)),
        }
    assert all(m["float_m"] is not None and m["market_cap_m"] is not None for m in screen.metrics.values())


def test_a_blank_cell_reaches_metrics_as_none_never_zero():
    _config, rows, _candidates, source_sets = collect(SCREEN_FIXTURE)
    (screen,) = [s for s in source_sets if s.kind == "screen"]
    blank = [row["Ticker"] for row in rows if not row["Shares Float"].strip()]
    assert blank
    for ticker in blank:
        assert screen.metrics[ticker]["float_m"] is None


# ---------------------------------------------------------------------
# (ii) handicap_group — [F-10]'s verdict table, `any` AND `all`
# ---------------------------------------------------------------------

#: float / cap cells against the thresholds 20 / 300 (strict `<`).
BELOW_F, AT_F, ABOVE_F = 19.99, 20.0, 40.0
BELOW_C, AT_C, ABOVE_C = 299.99, 300.0, 900.0


def _verdict(float_m, cap_m, combinator):
    return handicap_group(
        {"volume": 1.0, "rvol": 1.0, "float_m": float_m, "market_cap_m": cap_m},
        HandicapBlock(**block(combinator=combinator)),
    )


@pytest.mark.parametrize(
    "float_m,cap_m,expected,reason",
    [
        (BELOW_F, BELOW_C, "yes", "float and cap"),   # both known, both meet
        (BELOW_F, ABOVE_C, "yes", "float"),           # one meets
        (ABOVE_F, BELOW_C, "yes", "cap"),
        (ABOVE_F, ABOVE_C, "no", "neither"),          # none meets
        (AT_F, AT_C, "no", "neither"),                # strict `<` at the threshold
        (None, BELOW_C, "yes", "cap"),                # a blank that cannot change the result
        (None, ABOVE_C, "unknown", "blank float"),    # a blank that could change it
        (ABOVE_F, None, "unknown", "blank cap"),
        (None, None, "unknown", "blank float and cap"),
    ],
)
def test_the_any_verdict_table(float_m, cap_m, expected, reason):
    verdict = _verdict(float_m, cap_m, "any")
    assert isinstance(verdict, GroupVerdict)
    assert (verdict.in_group, verdict.reason) == (expected, reason)


@pytest.mark.parametrize(
    "float_m,cap_m,expected,reason",
    [
        (BELOW_F, BELOW_C, "yes", "float and cap"),   # both known and both meet
        (BELOW_F, ABOVE_C, "no", "neither"),          # both known, one fails
        (ABOVE_F, BELOW_C, "no", "neither"),
        (ABOVE_F, ABOVE_C, "no", "neither"),
        (AT_F, BELOW_C, "no", "neither"),             # strict `<`
        (None, BELOW_C, "unknown", "blank float"),    # either blank → unknown
        (BELOW_F, None, "unknown", "blank cap"),
        (None, ABOVE_C, "unknown", "blank float"),
        (None, None, "unknown", "blank float and cap"),
    ],
)
def test_the_all_verdict_table(float_m, cap_m, expected, reason):
    verdict = _verdict(float_m, cap_m, "all")
    assert (verdict.in_group, verdict.reason) == (expected, reason)


def test_the_verdict_carries_the_cells_as_decimal_from_their_text():
    verdict = _verdict(BELOW_F, None, "any")
    assert verdict.float_m == Decimal(str(BELOW_F)) and verdict.market_cap_m is None


def test_a_missing_metrics_row_is_unknown_never_no():
    for combinator in ("any", "all"):
        verdict = handicap_group(None, HandicapBlock(**block(combinator=combinator)))
        assert verdict.in_group == "unknown"


# ---------------------------------------------------------------------
# (iii) the real blank rows of the movers fixtures are never a silent `no`
# ---------------------------------------------------------------------


def _equity_rows(path: Path):
    config = load_config()
    rows = list(csv.DictReader(io.StringIO(path.read_text(encoding="utf-8-sig"))))
    return config, [row for row in rows if not is_not_equity(row, config.not_equity)]


@pytest.mark.parametrize("name", ["movers-gainers.real-shape.csv", "movers-losers.real-shape.csv"])
@pytest.mark.parametrize("combinator", ["any", "all"])
def test_blank_float_or_cap_equity_rows_of_the_movers_fixtures_are_never_a_silent_no(name, combinator):
    config, rows = _equity_rows(REPLAY_FIXTURES / name)
    headers = config.export.handicap_headers
    blank = [
        row for row in rows
        if _number(row.get(headers.float)) is None or _number(row.get(headers.market_cap)) is None
    ]
    assert blank, "the fixture's blank rows (v3 F6) are gone"
    for row in blank:
        metrics = {"float_m": _number(row.get(headers.float)), "market_cap_m": _number(row.get(headers.market_cap))}
        verdict = handicap_group(metrics, HandicapBlock(**block(combinator=combinator)))
        assert verdict.in_group != "no"
        if combinator == "all":
            assert verdict.in_group == "unknown"


# ---------------------------------------------------------------------
# (iv) the redacted real-shape screen export (L45)
# ---------------------------------------------------------------------


def test_the_screen_fixture_is_a_real_shape_export_with_a_blank_float_equity_row_and_a_fund():
    header = SCREEN_FIXTURE.read_bytes().split(b"\n", 1)[0]
    assert header == POOL_METRICS.read_bytes().split(b"\n", 1)[0]
    raw = list(csv.reader(io.StringIO(SCREEN_FIXTURE.read_text(encoding="utf-8-sig"))))
    assert 1 <= len(raw) - 1 <= 20
    assert all(len(line) == len(raw[0]) for line in raw)
    config, equity = _equity_rows(SCREEN_FIXTURE)
    rows = list(csv.DictReader(io.StringIO(SCREEN_FIXTURE.read_text(encoding="utf-8-sig"))))
    assert any(not row["Shares Float"].strip() for row in equity)
    assert any(is_not_equity(row, config.not_equity) for row in rows)
    for column in ("News Time", "News URL", "News Title", "Daily Digest", "Earnings Date", "IPO Date",
                   "Dividend Ex Date"):
        assert all(not row[column].strip() for row in rows), column


# ---------------------------------------------------------------------
# (v) the homogeneous screen — B moves it, a metric multiplier provably
# does not (v3 §1, §9 Tests). RED at STEP-3; GREEN at STEP-4.
# ---------------------------------------------------------------------

RTH_NOW = datetime(2026, 9, 3, 15, 0, tzinfo=timezone.utc)  # 11:00 ET


def homogeneous(scale: float = 1.0, factor: str = "0.5"):
    """Screen HOT: A, B, C — every one in the group (float 5). Screen COLD:
    X, Y, Z — none in it (float 90, cap 900). Same tier, interleaved."""
    hot = {t: {"volume": v * scale, "rvol": v * scale, "float_m": 5.0, "market_cap_m": 900.0}
           for t, v in (("A", 30.0), ("B", 20.0), ("C", 10.0))}
    cold = {t: {"volume": v, "rvol": v, "float_m": 90.0, "market_cap_m": 900.0}
            for t, v in (("X", 30.0), ("Y", 20.0), ("Z", 10.0))}
    sources = [
        SourceSet(source="screen:hot@000000000001", kind="screen", tickers=list(hot), metrics=hot, note_order=0),
        SourceSet(source="screen:cold@000000000002", kind="screen", tickers=list(cold), metrics=cold, note_order=1),
    ]
    candidates = {t: Candidate(ticker=t, sources=[s.source]) for s in sources for t in s.tickers}
    return PoolBlock(**pool(**block(factor=factor))), sources, candidates


def test_a_metric_multiplier_leaves_a_homogeneous_screen_exactly_where_it_was():
    pool_block, sources, candidates = homogeneous()
    _pool_scaled, scaled, _ = homogeneous(scale=0.5)
    assert _ranked(candidates, pool_block, sources, RTH_NOW)[0] == _ranked(candidates, pool_block, scaled, RTH_NOW)[0]


def test_the_pool_wide_re_sort_moves_the_homogeneous_screen():
    from cobalt.radar.handicap import shadow_rank

    pool_block, sources, candidates = homogeneous()
    ordered, ranks, source_for, _values = _ranked(candidates, pool_block, sources, RTH_NOW)
    assert ordered == ["A", "X", "B", "Y", "C", "Z"]
    shadow = shadow_rank(ordered, ranks, source_for, sources, pool_block.handicap,
                         load_config().export.handicap_headers)
    would_be = sorted(ordered, key=lambda t: shadow.records[t].effective_position)
    # eff = raw ÷ 0.5 for A, B, C: A 2, B 6, C 10; X 2, Y 4, Z 6 — a tie goes
    # to the unhandicapped name (R57), so X before A and Z before B.
    assert would_be == ["X", "A", "Y", "Z", "B", "C"]
    assert [shadow.records[t].effective_position for t in ("A", "B", "C")] == [2, 5, 6]
