"""DRC K1 fix r1 — the RUNS of the UNPROVEN rows (L70).

A RUN is a cheap executed probe of a claim no read could settle. Its
red is a RESULT, recorded under the build report's ESCALATE and never
fixed in this round (L70 / L75). Constructed symbols and dates only
(L32 / L45); nothing here is a value of his.
"""

from __future__ import annotations

from datetime import date

from cobalt.drc import stats_log
from cobalt.drc.detect import detect_kind
from cobalt.drc.models import StatedPosition
from cobalt.drc.pairing import build_day, stated_open_positions
from cobalt.drc.stats_log import StatsLogSource
from cobalt.drc.trading_log import TradingLogSource

from test_drc_pairing import CARRIED_SHORT_DAY2, STATS, _set_stats_cell

D_NEXT = date(2001, 1, 3)


def _one_row_stats_for_ggg_short() -> bytes:
    """`stats_log_e1.csv`'s header and first row, its symbol / side cells
    set to the constructed `GGG` / short on `D_NEXT` (the fixture's own
    shape, L45)."""
    data = b"".join(STATS.read_bytes().splitlines(keepends=True)[:2])
    for column, value in (
        (stats_log.SYMBOL, "GGG"),
        ("Instrument", "GGG"),
        (stats_log.SIDE, "short"),
        (stats_log.OPEN_DATE, D_NEXT.isoformat()),
        ("Close Date", D_NEXT.isoformat()),
    ):
        data = _set_stats_cell(data, 2, column, value)
    return data


def test_run_1_a_stated_trade_against_a_stats_log():
    """RUN-1 (`drc-k1-check-2026-09-24.md:155`, row 7 / ESCALATE 7 —
    Opus `NOT CHECKABLE FROM READS`: "no test runs a stated seed with a
    stats log"). A stated `GGG` short 40 with no cost, closed by the day's
    `B`, against a one-row stats log for that short: no exception, the
    stated trade carries NO stats, and the row is `unmatched` — never
    attached to another trade. The walk read `unmatched — 0 trades match`
    (`pairing.py:366-369`); the assertion quotes it."""
    trading = TradingLogSource().parse(
        CARRIED_SHORT_DAY2, D_NEXT, detect_kind("t.md", CARRIED_SHORT_DAY2)
    )
    stats_bytes = _one_row_stats_for_ggg_short()
    stats = StatsLogSource().parse(stats_bytes, detect_kind("s.md", stats_bytes))
    assert [(r.symbol, r.side.value) for r in stats.rows] == [("GGG", "short")]
    seed = stated_open_positions(
        D_NEXT, [StatedPosition(symbol="GGG", direction="short", shares=40, avg_cost=None)]
    )

    day = build_day(trading, stats, seed=seed)

    (ggg,) = day.trades
    assert ggg.symbol == "GGG" and ggg.stats is None
    (u,) = day.unmatched
    assert u.row.line == 2 and u.row.symbol == "GGG"
    assert u.reason == "unmatched — 0 trades match"
