"""S2-P4 STEP-6 — F13: unfiltered top movers, their i1 archive, the benchmark.

Charter F13: "a Tesla-class mover absent from the pool appears in the miss
line with excluded_by". Fixtures are hub-cut (L45): one unfiltered export
per side (movers-*.real-shape.csv) and the same day's membership episodes.

SHAPE (AT-1 2.5): the movers fixtures are now cut from unfiltered exports
fetched at the radar's own column set — 151 columns including `Asset
Type`, the same header the radar's screen export carries, byte for byte
(`test_the_collector_receives_one_export_shape`). Finviz fills `Asset
Type` only for funds, so most rows are blank and a handful are not; both
cases are in the fixture.

THE RULE (R16 "C", ruled 2026-09-19): a row is not equity when its
`Asset Type` is non-blank OR its `Industry` is a fund industry. Both
columns are REQUIRED of a movers export now, so an absent column is a
FAILED parse naming the header and `unreported` means only what it always
should have: the column is there and this row's cell is blank.

The exports are a different trading day from `membership-day.real-shape
.json` (the 21-column first cut could not be re-fetched at the real
column set). Every ticker, rank and percentage below therefore comes from
the new exports; the pool overlap is real but smaller, and the tests name
the rows that actually carry each case.
"""

from __future__ import annotations

import asyncio
import csv
import hashlib
import io
import os
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path

import pytest
from pydantic import ValidationError

from cobalt.archiver.models import Bar, Interval
from cobalt.radar.collector import SourceFailure
from cobalt.radar.config import is_not_equity
from cobalt.replay import movers as movers_mod
from cobalt.replay.line import render_line
from cobalt.replay.models import (
    Episode,
    MoversSideCount,
    ReplayError,
    ReplayInputError,
    StoredMover,
)
from cobalt.replay.movers import (
    REQUIRED_HEADERS,
    SIDES,
    MoversStore,
    archive_movers,
    benchmark_misses,
    export_counts,
    mover_is_not_equity,
    not_equity_verdicts,
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
    """What comes back OUT of `movers_daily`: `StoredMover` has no
    `industry` field and `MoversStore._COLUMNS` has no such column, so a
    round trip drops the second half of the R16 rule. Every benchmark
    test below therefore reads its verdicts from the export, not here."""
    return [
        StoredMover(id=start_id + i, trade_date=trade_date, side=row.side, rank=row.rank, ticker=row.ticker,
                    change_pct=row.change_pct, asset_type=row.asset_type, volume=row.volume, rvol=row.rvol,
                    export_sha256=export.export_sha256, fetched_at=export.fetched_at)
        for i, row in enumerate(export.rows)
    ]


#: The shipped R16 "C" rule, as every call site reads it.
RULE = movers_mod.load_radar_config().not_equity


def _both(top_n=61):
    """Both committed exports, whole — `top_n=61` because the blank-`Asset
    Type` fund row each side carries is rank 61 (FR-1)."""
    return [_export(side, top_n=top_n) for side in SIDES]


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
                            not_equity=RULE, verdicts=not_equity_verdicts([gainers, losers]))
    by_ticker = {r.ticker: r for r in rows}
    # QNME, +92.25%, rank 2 of the day's gainers, has no membership episode
    # at all (rank 1 IMCC was admitted, so it is correctly not a miss)
    assert by_ticker["QNME"].excluded_by == "not_in_any_source"
    assert by_ticker["QNME"].mover_id == 2
    assert by_ticker["QNME"].gate_detail["change_pct"] == "92.25"
    assert "IMCC" not in by_ticker
    line = render_line(DAY, card_rows=[], mover_rows=[r.model_dump() for r in rows], settings=SETTINGS,
                       formation_replay="unavailable", input_stale=0)
    assert "QNME +92.3% not_in_any_source" in line


def test_admitted_mover_is_not_a_miss(episodes):
    gainers = _export("gainers")
    movers = _stored(gainers)
    rows = benchmark_misses(movers, episodes, settings=BenchmarkSettings(top_n=60, min_move_pct=Decimal("1")),
                            trade_date=DAY, not_equity=RULE, verdicts=not_equity_verdicts([gainers]))
    tickers = {r.ticker for r in rows}
    admitted = {e.ticker for e in episodes if e.entered_at is not None}
    in_both = {m.ticker for m in movers} & admitted
    assert "IMCC" in in_both                 # the day's top gainer, admitted
    assert not (tickers & in_both)


def test_never_admitted_episode_supplies_its_excluded_by(episodes):
    gainers = _export("gainers")
    movers = _stored(gainers)
    rows = {r.ticker: r for r in benchmark_misses(movers, episodes, settings=SETTINGS, trade_date=DAY,
                                                  not_equity=RULE,
                                                  verdicts=not_equity_verdicts([gainers]))}
    usde = rows["USDE"]                      # +32.17%, never admitted, config_cap
    assert usde.excluded_by == "config_cap"
    assert usde.pool_member_id is None or isinstance(usde.pool_member_id, int)
    assert usde.gate_detail["episodes"][0]["excluded_by"] == "config_cap"


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
    assert fetched == ["IMCC", "QNME", "REFR"]
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
        (1, "IMCC", Decimal("143.10")), (2, "QNME", Decimal("92.25")), (3, "REFR", Decimal("68.49"))]
    assert gainers.rows[0].volume == 104981193 and gainers.rows[0].rvol == Decimal("876.54")
    assert gainers.rows[0].asset_type is None          # an ordinary stock: the cell is blank
    losers = _export("losers", top_n=2)
    assert losers.rows[0].change_pct == Decimal("-69.89")


def test_asset_type_is_read_from_the_movers_export_itself():
    """The column the replay's not-equity branch depends on is in the
    real movers shape, and the fixture carries both cases: blank for an
    ordinary stock (-> None, `unreported`), a real value for a fund. No
    row here is a fund by our rule — that rule is not built (AT-1) — the
    assertion is only that the value is READ, never invented."""
    for side, rank, value in (("gainers", 5, "Equities (Stocks)"), ("losers", 7, "Equities (Stocks)")):
        export = _export(side)
        assert "Asset Type" in export.header
        by_rank = {row.rank: row.asset_type for row in export.rows}
        assert by_rank[rank] == value
        assert by_rank[1] is None
        assert sum(1 for v in by_rank.values() if v is not None) > 1


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


def test_the_collector_receives_one_export_shape():
    """L45. The radar's screen export and both unfiltered movers exports
    are one request shape (`test_every_finviz_consumer_asks_for_the_same
    _column_set`), so they are one CSV shape: all three committed
    fixtures carry the same header row, byte for byte. The first movers
    cut came from a 21-column default view — a shape the collector never
    receives — and this is the assertion that would have caught it."""
    header = (FIX / "radar" / "pool-metrics.real-shape.csv").read_bytes().split(b"\n", 1)[0]
    for side in SIDES:
        cut = (FIX / "replay" / f"movers-{side}.real-shape.csv").read_bytes().split(b"\n", 1)[0]
        assert cut == header, side
    columns = next(csv.reader([header.decode("utf-8-sig")]))
    assert len(columns) == 151
    assert "Asset Type" in columns


def test_both_movers_fixtures_hold_a_real_row_with_a_non_blank_asset_type():
    """Finviz fills `Asset Type` only for funds. A cut with none would
    leave "reads Asset Type when present" asserted against blanks alone;
    the cutter's `movers` mode guarantees at least one, and appends one
    from further down the file if the top rows have none.

    61 rows, not 60: the top 60 of the export plus the one row the cutter
    appends per side for the OTHER guaranteed class — a fund named by
    `Industry` alone, its `Asset Type` cell blank (AT-1 FR-1). That row is
    rank 61, so a `parse_movers(top_n=60)` never sees it; the blank-type
    fund class is asserted in `test_p4_asset_type_evidence.py`, against
    the file, where the cutter's guarantee lives."""
    for side in SIDES:
        rows = list(csv.DictReader(io.StringIO(
            (FIX / "replay" / f"movers-{side}.real-shape.csv").read_text(encoding="utf-8"))))
        assert len(rows) == 61
        non_blank = [row for row in rows if (row["Asset Type"] or "").strip()]
        assert non_blank, f"movers-{side} has no non-blank Asset Type row"


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
# Export bookkeeping: what the export really had (build 2 §4 row 3)
# =====================================================================


def test_the_export_records_how_many_rows_it_really_had_and_keeps_the_same_top_rows():
    """`exported_rows` counts the export; `rows` is still `rows[:top_n]`.

    Recording the count selects nothing: at every cap the kept rows are
    the first N of the same ranking, and the raw bytes hash the same.
    """
    full = _export("gainers", top_n=61)
    assert (full.exported_rows, len(full.rows)) == (61, 61)
    capped = _export("gainers", top_n=10)
    assert (capped.exported_rows, len(capped.rows)) == (61, 10)
    # A cap ABOVE what the export had: the export is short, not wrong.
    over = _export("gainers", top_n=1000)
    assert (over.exported_rows, len(over.rows)) == (61, 61)
    assert list(capped.rows) == list(full.rows[:10]) == list(over.rows[:10])
    assert full.export_sha256 == capped.export_sha256 == over.export_sha256
    assert list(full.rows) == list(over.rows)


def test_export_counts_record_min_top_n_exported_per_side():
    """`expected` = min(top_n, exported) — the only number a stored-row
    count may be checked against, because a short export is a fact about
    the source, not a failure of the run."""
    counts = export_counts([_export(side, top_n=60) for side in SIDES], top_n=60)
    assert set(counts) == {"gainers", "losers"}
    assert [(c.exported, c.top_n, c.expected) for c in counts.values()] == [(61, 60, 60), (61, 60, 60)]
    # the export ran out first
    short = export_counts([_export(side, top_n=1000) for side in SIDES], top_n=1000)
    assert all((c.exported, c.top_n, c.expected) == (61, 1000, 61) for c in short.values())
    # the cap came first
    capped = export_counts([_export(side, top_n=10) for side in SIDES], top_n=10)
    assert all((c.exported, c.top_n, c.expected) == (61, 10, 10) for c in capped.values())


def test_export_counts_refuse_a_disagreement_and_a_repeated_side():
    export = _export("gainers", top_n=60)
    # the count and the rows kept must tell the same story
    with pytest.raises(ReplayInputError, match="kept 60 of 61"):
        export_counts([export], top_n=10)
    with pytest.raises(ReplayInputError, match="two exports for side"):
        export_counts([export, export], top_n=60)
    # `expected` is min(top_n, exported) or the model refuses to exist
    with pytest.raises(ValidationError):
        MoversSideCount(exported=5, top_n=60, expected=60)
    with pytest.raises(ValidationError):
        MoversSideCount(exported=60, top_n=25, expected=60)
    assert MoversSideCount(exported=5, top_n=60, expected=5).expected == 5


# =====================================================================
# R1-20 — reruns, both sides, history
# =====================================================================


def test_r1_20_a_ticker_on_both_sides_resolves_to_one_missed_row(episodes):
    gainers = _export("gainers", top_n=2)
    losers = _export("losers", top_n=1)
    twin = _stored(gainers)[1]               # rank 2: rank 1 was admitted, so it is no miss
    other = _stored(losers, start_id=50)[0].model_copy(update={"ticker": twin.ticker, "change_pct": Decimal("-170")})
    # the losers export row follows the stored copy: the verdict lookup is
    # keyed by (side, ticker) and every stored row must have its own.
    verdicts = not_equity_verdicts([gainers])
    verdicts[("losers", twin.ticker)] = losers.rows[0].model_copy(update={"ticker": twin.ticker})
    rows = benchmark_misses([twin, other], episodes, settings=SETTINGS, trade_date=DAY,
                            not_equity=RULE, verdicts=verdicts)
    assert len(rows) == 1
    assert rows[0].mover_id == 50                           # the larger |change| carries the row
    assert sorted(rows[0].gate_detail["sides"]) == ["gainers", "losers"]


def test_r1_20_multiple_never_admitted_episodes_pick_the_most_recent(episodes):
    gainers = _export("gainers", top_n=1)
    mover = _stored(gainers)[0]
    older = Episode(id=1, ticker=mover.ticker, trade_date=DAY, excluded_by="not_equity",
                    first_seen_at=datetime(2026, 2, 10, 9, tzinfo=timezone.utc))
    newer = Episode(id=2, ticker=mover.ticker, trade_date=DAY, excluded_by="screen_inactive",
                    first_seen_at=datetime(2026, 2, 10, 15, tzinfo=timezone.utc))
    rows = benchmark_misses([mover], [older, newer], settings=SETTINGS, trade_date=DAY,
                            not_equity=RULE, verdicts=not_equity_verdicts([gainers]))
    assert rows[0].excluded_by == "screen_inactive"
    assert rows[0].pool_member_id == 2


def test_not_equity_movers_leave_the_benchmark_and_unreported_asset_type_stays_in(episodes):
    """R16 "C" rewrote what this scenario means. It used to be "a
    non-blank `Asset Type` in the configured value list leaves, a blank
    one stays". Now the deciding column may be either one:

    * GEMG — non-blank `Asset Type`, fund `Industry`: leaves
    * SCOP — BLANK `Asset Type`, fund `Industry`: leaves too, and the old
      one-column rule could not see it at all
    * IMCC — blank `Asset Type`, an ordinary industry: STAYS, and its
      blank value is still labelled `unreported`

    All three are real rows of the committed gainers export.
    """
    gainers = _export("gainers", top_n=61)
    by_ticker = {m.ticker: m for m in _stored(gainers)}
    movers = [by_ticker[t] for t in ("GEMG", "SCOP", "IMCC")]
    settings = BenchmarkSettings(top_n=61, min_move_pct=Decimal("1"))
    rows = benchmark_misses(movers, [], settings=settings, trade_date=DAY,
                            not_equity=RULE, verdicts=not_equity_verdicts([gainers]))
    assert [r.ticker for r in rows] == ["IMCC"]
    assert rows[0].gate_detail["asset_type"] == "unreported"
    assert rows[0].gate_detail["industry"] == "Drug Manufacturers - Specialty & Generic"


# =====================================================================
# S2-P4 FR-2 — R16 "C": one rule, one evaluator, decided AT INGEST
# =====================================================================


def test_the_r16_rule_on_real_rows_drops_a_fund_by_either_column_and_keeps_a_stock():
    """Three of the rule's four cases, each on a row taken verbatim from
    a committed real-shape export (L45):

    * non-blank `Asset Type` + fund `Industry`  -> dropped (GEMG, TDNA's side has ASTT/ASTX)
    * BLANK `Asset Type` + fund `Industry`      -> dropped (SCOP, TDNA)
    * blank `Asset Type` + ordinary `Industry`  -> kept    (IMCC, DCX)

    The fourth case — a non-blank `Asset Type` on a NON-fund `Industry` —
    has no row anywhere in the sample (table C(i) = 0), so it is tested
    as the boolean it is, from an explicit mapping, never from a
    fabricated fixture row.
    """
    gainers, losers = ({row.ticker: row for row in export.rows} for export in _both())
    assert mover_is_not_equity(gainers["GEMG"], RULE) is True
    assert mover_is_not_equity(losers["ASTT"], RULE) is True
    assert mover_is_not_equity(gainers["SCOP"], RULE) is True
    assert mover_is_not_equity(losers["TDNA"], RULE) is True
    assert mover_is_not_equity(gainers["IMCC"], RULE) is False
    assert mover_is_not_equity(losers["DCX"], RULE) is False
    # the arm with no real row: the boolean, stated outright
    assert is_not_equity({RULE.asset_type_header: "Preferred Stock",
                          RULE.industry_header: "Capital Markets"}, RULE) is True


def test_the_asset_type_only_arm_hits_no_row_of_any_committed_export():
    """Table C(i): a non-blank `Asset Type` sitting on a NON-fund
    `Industry` — an ordinary stock the type arm alone would drop. The
    count is asserted and printed rather than folded into a boolean, so
    the day a real export carries one it is visible. Counts only (L32)."""
    hit = total = 0
    paths = [FIX / "radar" / "pool-metrics.real-shape.csv"]
    paths += [FIX / "replay" / f"movers-{side}.real-shape.csv" for side in SIDES]
    for path in paths:
        for raw in csv.DictReader(io.StringIO(path.read_text(encoding="utf-8"))):
            total += 1
            hit += bool(
                (raw["Asset Type"] or "").strip()
                and (raw["Industry"] or "").strip() not in RULE.industry_values
            )
    print(f"asset-type-only arm: {hit} of {total} committed real-shape rows")
    assert (hit, total) == (0, 142)


def test_parse_reads_industry_beside_asset_type_on_every_row():
    """Both columns are required now, so both are read unconditionally —
    a blank CELL is `None`, and a missing COLUMN cannot happen."""
    by_ticker = {row.ticker: row for row in _export("gainers", top_n=61).rows}
    assert (by_ticker["IMCC"].asset_type, by_ticker["IMCC"].industry) == (
        None, "Drug Manufacturers - Specialty & Generic")
    assert (by_ticker["GEMG"].asset_type, by_ticker["GEMG"].industry) == (
        "Equities (Stocks)", "Exchange Traded Fund")
    assert (by_ticker["SCOP"].asset_type, by_ticker["SCOP"].industry) == (None, "Exchange Traded Fund")


def test_required_headers_carry_both_columns_and_a_missing_one_is_loud():
    """L1: a column that is simply absent is a FAILED export naming the
    header, on the same path as a missing `Ticker`/`Change`/`Volume` —
    never a silent `None` that reads downstream as `unreported`."""
    assert REQUIRED_HEADERS == ["Ticker", "Change", "Volume", "Asset Type", "Industry"]
    losers = (FIX / "replay" / "movers-losers.real-shape.csv").read_bytes()
    header, _, rest = losers.partition(b"\n")
    for column in ("Asset Type", "Industry"):
        narrowed = header.replace(f',"{column}"'.encode(), b"")
        assert narrowed != header, column
        with pytest.raises(SourceFailure, match=column):
            parse_movers(narrowed + b"\n" + rest, side="losers", top_n=10, content_type="text/csv",
                         config=movers_mod.load_radar_config(), fetched_at=FETCHED, source="live")


def test_the_verdict_lookup_covers_both_exports_and_refuses_a_repeated_key():
    """One lookup per run, built once from the parsed exports. A repeated
    (side, ticker) is loud — silently keeping the last row would make the
    rule depend on export order."""
    exports = _both()
    verdicts = not_equity_verdicts(exports)
    assert len(verdicts) == sum(len(e.rows) for e in exports) == 122
    assert {key[0] for key in verdicts} == set(SIDES)
    # 29 + 1 gainers, 19 + 1 losers: what R16 drops out of these two cuts
    assert sum(1 for row in verdicts.values() if mover_is_not_equity(row, RULE)) == 50
    doubled = exports[0].model_copy(update={"rows": (*exports[0].rows, exports[0].rows[0])})
    with pytest.raises(ReplayInputError, match="gainers"):
        not_equity_verdicts([doubled])


def test_the_benchmark_decides_from_the_export_row_the_db_round_trip_never_carried():
    """`movers_daily` has no `industry` column and `StoredMover` has no
    such field, so on the live path a blank-`Asset Type` fund is
    invisible in the rows the benchmark receives. The verdict lookup
    built at ingest is what decides."""
    exports = _both()
    stored = _stored(exports[0]) + _stored(exports[1], start_id=1000)
    assert not any(hasattr(m, "industry") for m in stored)
    settings = BenchmarkSettings(top_n=61, min_move_pct=Decimal("1"))
    tickers = {r.ticker for r in benchmark_misses(stored, [], settings=settings, trade_date=DAY,
                                                  not_equity=RULE,
                                                  verdicts=not_equity_verdicts(exports))}
    assert not ({"SCOP", "TDNA"} & tickers)          # blank type, fund industry
    assert not ({"GEMG", "ASTT", "ASTX"} & tickers)  # non-blank type
    assert {"IMCC", "QNME", "DCX", "USDE"} <= tickers


def test_a_staled_stored_asset_type_never_decides_the_benchmark():
    """L57: the deciding values are this run's export row, not whatever
    the DB round trip returned. A fund whose stored `asset_type` came
    back blank still leaves; a stock whose stored `asset_type` came back
    as a fund value still stays."""
    gainers = _export("gainers", top_n=61)
    staled = [
        m.model_copy(update={"asset_type": None}) if m.ticker == "GEMG"
        else m.model_copy(update={"asset_type": "Exchange Traded Fund"}) if m.ticker == "IMCC"
        else m
        for m in _stored(gainers)
    ]
    settings = BenchmarkSettings(top_n=61, min_move_pct=Decimal("1"))
    rows = {r.ticker: r for r in benchmark_misses(staled, [], settings=settings, trade_date=DAY,
                                                  not_equity=RULE,
                                                  verdicts=not_equity_verdicts([gainers]))}
    assert "GEMG" not in rows
    assert "IMCC" in rows
    assert rows["IMCC"].gate_detail["asset_type"] == "unreported"
    assert rows["IMCC"].receipt["inputs"]["movers"][0]["asset_type"] is None


def test_a_stored_mover_with_no_verdict_is_loud():
    """Every `StoredMover` came from an export row of this same run, so a
    lookup miss is a bug — named, never guessed around."""
    gainers = _export("gainers", top_n=2)
    verdicts = not_equity_verdicts([gainers])
    verdicts.pop(("gainers", "QNME"))
    with pytest.raises(ReplayInputError, match="QNME"):
        benchmark_misses(_stored(gainers), [], settings=SETTINGS, trade_date=DAY,
                         not_equity=RULE, verdicts=verdicts)


def test_the_miss_rows_stored_inputs_carry_the_deciding_values_and_the_rule_marker():
    """L57. The receipt records both deciding columns per mover row plus
    the rule that read them, so the row replays without `movers_daily`
    (which never carried `Industry`) and without radar.yaml."""
    gainers = _export("gainers", top_n=3)
    rows = benchmark_misses(_stored(gainers), [], settings=SETTINGS, trade_date=DAY,
                            not_equity=RULE, verdicts=not_equity_verdicts([gainers]))
    row = next(r for r in rows if r.ticker == "IMCC")
    inputs = row.receipt["inputs"]
    assert inputs["not_equity_rule"] == "asset_type_or_etf_industry"
    assert inputs["not_equity_industry_values"] == ["Exchange Traded Fund"]
    assert "not_equity_values" not in inputs
    assert [(m["asset_type"], m["industry"]) for m in inputs["movers"]] == [
        (None, "Drug Manufacturers - Specialty & Generic")]
    assert row.gate_detail["asset_type"] == "unreported"
    assert row.gate_detail["industry"] == "Drug Manufacturers - Specialty & Generic"


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
            return ({"IMCC": _session_bars("IMCC"), "QNME": _session_bars("QNME")[:30]},
                    {"REFR": "CollectorError: HTTP 429"})

    outcome = asyncio.run(archive_movers(movers, collector=Collector(), bar_store=_FakeBars(), trade_date=SYN_DAY,
                                         rth_open=RTH_OPEN, close=CLOSE, top_n=3, dry_run=False))
    assert outcome.archived_ids == [1]
    assert outcome.incomplete == ["QNME"]
    assert outcome.failures == {"REFR": "CollectorError: HTTP 429"}


def test_archive_skips_tickers_already_covered_and_dry_run_fetches_nothing():
    movers = _stored(_export("gainers", top_n=2))
    store = _FakeBars(existing={"IMCC": _session_bars("IMCC")})

    class Collector:
        async def bars(self, tickers, *, top_n):
            raise AssertionError("dry run fetched")

    outcome = asyncio.run(archive_movers(movers, collector=Collector(), bar_store=store, trade_date=SYN_DAY,
                                         rth_open=RTH_OPEN, close=CLOSE, top_n=2, dry_run=True))
    assert outcome.archived_ids == [1]
    assert outcome.would_fetch == ["QNME"]
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

    def bars_in_range(self, conn, ticker, interval, start, end,
                      *, end_inclusive=True, as_bars=False):
        assert (conn, end_inclusive, as_bars) == (None, False, True), (
            "replay owns no transaction and reads [start, end) as bars"
        )
        return [b for b in self.existing.get(ticker, []) if start <= b.ts < end]

    def upsert_bars(self, bars):
        for b in bars:
            self.existing.setdefault(b.ticker, []).append(b)
        self.upserted += len(bars)
        return len(bars)


class _NoWait:
    async def acquire(self):
        return None
