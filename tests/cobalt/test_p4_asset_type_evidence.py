"""S2-P4 AT-0 — the fixture cutter's read-only `evidence` mode.

WHY. Finviz fills the `Asset Type` column only for funds (a fund's asset
class) and leaves it blank for an ordinary stock, so the radar config's
`not_equity.values: [Exchange Traded Fund]` matches nothing. Before that
rule is rebuilt, the hub wants evidence from REAL exports on whether
"non-blank Asset Type" and "Industry = Exchange Traded Fund" pick out the
same rows. The mode under test produces that evidence; it is a decision
aid, not a rule, and it never writes a fixture.

The cutter is a script, not an importable package, so it is loaded by
path. Every assertion below is against committed real-shape exports
(L45): `pool-metrics.real-shape.csv` and `movers-gainers.real-shape.csv`
are both real 151-column screener exports, and since AT-1 2.5 re-cut the
movers fixtures at the radar's real column set BOTH carry `Asset Type`
and `Industry`. The movers cut is what gives tables A and B their first
real rows — 29 fund rows in 60 — so the report's row rendering is no
longer proved by hand-built report objects alone.

No committed export lacks the two columns any more, so the "counted and
listed, never silently skipped" path is exercised by `narrowed_export`:
the real movers fixture with those two columns DELETED. Every remaining
cell is the real file's. No row is invented anywhere in this module.
"""

from __future__ import annotations

import csv
import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
FIX = ROOT / "tests" / "fixtures"
CUTTER = FIX / "replay" / "_cut_p4_fixtures.py"
POOL_METRICS = FIX / "radar" / "pool-metrics.real-shape.csv"
MOVERS = FIX / "replay" / "movers-gainers.real-shape.csv"

#: Data-row counts of the two committed fixtures, as cut.
POOL_METRICS_ROWS = 20
MOVERS_ROWS = 60
#: Rows of the movers cut whose `Asset Type` is non-blank, and the two
#: values they carry. Real content of the committed fixture.
MOVERS_FUND_ROWS = 29
MOVERS_ASSET_TYPES = [("CryptoCurrency", 5), ("Equities (Stocks)", 24)]
#: The narrowed copy's name, asserted on the report's own line.
NARROWED = "movers-gainers.no-asset-type.csv"


def _load_cutter():
    """The canonical load-a-script-by-path recipe, `sys.modules` entry
    included: the cutter is `from __future__ import annotations`, so
    Pydantic resolves its model annotations through the module's entry
    and fails to build them if it is absent."""
    spec = importlib.util.spec_from_file_location("_cut_p4_fixtures", CUTTER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


cutter = _load_cutter()


def _pool_metrics_tickers() -> list[str]:
    with POOL_METRICS.open(newline="", encoding="utf-8") as handle:
        return [row["Ticker"] for row in csv.DictReader(handle)]


def _movers_tickers() -> list[str]:
    with MOVERS.open(newline="", encoding="utf-8") as handle:
        return [row["Ticker"] for row in csv.DictReader(handle)]


@pytest.fixture
def narrowed_export(tmp_path) -> Path:
    """The real movers export with `Asset Type` and `Industry` DELETED.

    A cache file written by an older column set is exactly this shape,
    and it is the only way left to exercise the "file without the
    columns" path from a real artifact: every committed export now has
    both columns. Two columns removed, every other cell untouched."""
    with MOVERS.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.reader(handle))
    drop = sorted(
        (rows[0].index(cutter.ASSET_TYPE_COL), rows[0].index(cutter.INDUSTRY_COL)), reverse=True
    )
    for row in rows:
        for index in drop:
            del row[index]
    path = tmp_path / NARROWED
    with path.open("w", newline="", encoding="utf-8") as handle:
        csv.writer(handle).writerows(rows)
    return path


# ---------------------------------------------------------------------
# the no-argument path is untouched
# ---------------------------------------------------------------------


def test_no_argument_path_untouched():
    """`main()` and every cut it calls survive beside the new mode."""
    for name in (
        "main",
        "evidence_main",
        "cut_cards_day",
        "cut_bars_day",
        "cut_membership_day",
        "cut_pool_metrics",
        "cut_movers",
    ):
        assert callable(getattr(cutter, name)), name


# ---------------------------------------------------------------------
# 1. read counts
# ---------------------------------------------------------------------


def test_rows_read_counts_both_kinds_of_file(narrowed_export):
    report = cutter.collect_evidence([POOL_METRICS, narrowed_export])
    assert report.files_read == 2
    assert report.rows_with_columns == POOL_METRICS_ROWS
    assert report.rows_without_columns == MOVERS_ROWS


def test_file_without_the_columns_is_listed_never_skipped(narrowed_export):
    report = cutter.collect_evidence([POOL_METRICS, narrowed_export])
    assert report.files_without_columns == [NARROWED]


def test_both_committed_exports_now_carry_the_two_columns():
    """AT-1 2.5: the movers fixtures were re-cut at the radar's real
    column set, so no committed export is missing either column."""
    report = cutter.collect_evidence([POOL_METRICS, MOVERS])
    assert report.files_without_columns == []
    assert report.rows_with_columns == POOL_METRICS_ROWS + MOVERS_ROWS
    assert report.rows_without_columns == 0


def test_input_dirs_are_recorded_as_given():
    report = cutter.collect_evidence([POOL_METRICS], input_dirs=["/somewhere/cache"])
    assert report.input_dirs == ["/somewhere/cache"]


# ---------------------------------------------------------------------
# 2-5. the radar fixture as it is: no fund row anywhere
# ---------------------------------------------------------------------


def test_radar_fixture_has_no_fund_rows():
    """Every `Asset Type` in the real export is blank and no row's
    `Industry` is `Exchange Traded Fund` — so A, B and C are all empty
    and both distinct counts are zero. This is the fixture's real
    content, asserted, not a stand-in for an invented one."""
    report = cutter.collect_evidence([POOL_METRICS])
    assert report.table_a == []
    assert report.table_b == []
    assert report.table_c_non_blank_not_fund == []
    assert report.table_c_fund_blank_type == []
    assert report.distinct_fund_tickers == 0
    assert report.distinct_asset_types == 0
    assert report.table_c_total == 0


def test_render_prints_none_for_every_empty_table(tmp_path):
    """One real row, header unchanged, copied verbatim out of the real
    export — table C is empty and renders as `(none)`."""
    lines = POOL_METRICS.read_text(encoding="utf-8").splitlines(keepends=True)
    one_row = tmp_path / "one-real-row.csv"
    one_row.write_text("".join(lines[:2]), encoding="utf-8")

    report = cutter.collect_evidence([one_row])
    assert report.rows_with_columns == 1
    assert report.table_c_total == 0

    text = cutter.render_evidence(report)
    # An empty table is the whole line `(none)`; the §1 prose markers are
    # never bare, so counting whole lines counts tables exactly.
    assert [line for line in text.splitlines() if line == "(none)"] == ["(none)"] * 4
    assert "- total: 0" in text


def test_render_shapes_a_non_empty_table():
    """The renderer only — NOT a parser tested against an invented
    export (L45). No committed real-shape export carries a fund row, so
    the rows the hub's real-cache run will actually print would
    otherwise render untested; the report objects here are built
    directly, and the values are labels, not data.

    Written after the implementation, so it has no red line of its own.
    """
    report = cutter.EvidenceReport(
        files_read=1,
        rows_with_columns=1,
        table_a=[
            cutter.PairCount(asset_type="Equity", industry="Shell Companies", rows=3)
        ],
        table_b=[cutter.AssetTypeCount(asset_type="<blank>", rows=2)],
        table_c_non_blank_not_fund=[
            cutter.DisagreementRow(
                file="screen.csv",
                ticker="TICK",
                asset_type="Equity",
                industry="Shell Companies",
            )
        ],
    )
    lines = cutter.render_evidence(report).splitlines()

    assert "| Asset Type | Industry | rows |" in lines
    assert "| Equity | Shell Companies | 3 |" in lines
    assert "| <blank> | 2 |" in lines
    assert "| screen.csv | TICK | Equity | Shell Companies |" in lines
    assert "- (i) non-blank `Asset Type`, `Industry` != Exchange Traded Fund: 1" in lines
    assert "- total: 1" in lines
    # only table C (ii) is empty
    assert [line for line in lines if line == "(none)"] == ["(none)"]


def test_render_reports_the_file_without_the_columns_by_name(narrowed_export):
    report = cutter.collect_evidence([POOL_METRICS, narrowed_export])
    text = cutter.render_evidence(report)
    assert NARROWED in text
    assert f"rows read (files without the columns): {MOVERS_ROWS}" in text


# ---------------------------------------------------------------------
# the movers fixture as a real input (AT-1 2.5, closing AT-0 ESCALATE 1)
# ---------------------------------------------------------------------


def test_the_movers_fixture_gives_tables_a_and_b_real_rows():
    """29 of the movers cut's 60 rows carry a non-blank `Asset Type`, in
    two values. Both are ALSO `Industry = Exchange Traded Fund`, so the
    two fund signals agree on every row of this cut and table C is empty
    — the real disagreement rows the hub counted over the whole radar
    cache are not in these 60 (see ESCALATE)."""
    report = cutter.collect_evidence([MOVERS])
    assert report.rows_with_columns == MOVERS_ROWS
    assert [(row.asset_type, row.rows) for row in report.table_b] == MOVERS_ASSET_TYPES
    assert [(row.asset_type, row.industry, row.rows) for row in report.table_a] == [
        (asset_type, cutter.FUND_INDUSTRY, rows) for asset_type, rows in MOVERS_ASSET_TYPES
    ]
    assert report.distinct_fund_tickers == MOVERS_FUND_ROWS
    assert report.distinct_asset_types == len(MOVERS_ASSET_TYPES)
    assert report.table_c_total == 0


def test_a_real_export_renders_non_empty_a_and_b_tables():
    """The row rendering, exercised from a real artifact rather than from
    report objects built in the test (AT-0 ESCALATE 1)."""
    text = cutter.render_evidence(cutter.collect_evidence([MOVERS]))
    assert f"| Equities (Stocks) | {cutter.FUND_INDUSTRY} | 24 |" in text.splitlines()
    assert "| CryptoCurrency | 5 |" in text.splitlines()
    # only table C's two halves are empty
    assert [line for line in text.splitlines() if line == "(none)"] == ["(none)"] * 2
    for ticker in _movers_tickers():
        assert ticker not in cutter.summarize_evidence(cutter.collect_evidence([MOVERS]))


# ---------------------------------------------------------------------
# stdout carries counts only — never a ticker (L32)
# ---------------------------------------------------------------------


def test_stdout_summary_carries_counts_and_no_ticker(narrowed_export):
    report = cutter.collect_evidence([POOL_METRICS, narrowed_export])
    summary = cutter.summarize_evidence(report)
    assert "files: 2" in summary
    assert f"rows: {POOL_METRICS_ROWS}" in summary
    assert "distinct fund tickers: 0" in summary
    assert "distinct Asset Type values: 0" in summary
    assert "table C total: 0" in summary
    for ticker in _pool_metrics_tickers():
        assert ticker not in summary


# ---------------------------------------------------------------------
# fail loud (L1)
# ---------------------------------------------------------------------


def test_unreadable_file_raises_with_its_name(tmp_path):
    broken = tmp_path / "not-utf8.csv"
    broken.write_bytes(b'"Ticker","Industry","Asset Type"\n"A\xff","B",""\n')
    with pytest.raises(cutter.EvidenceError) as excinfo:
        cutter.collect_evidence([broken])
    assert "not-utf8.csv" in str(excinfo.value)


def test_headerless_file_raises_with_its_name(tmp_path):
    empty = tmp_path / "empty-cache-write.csv"
    empty.write_text("", encoding="utf-8")
    with pytest.raises(cutter.EvidenceError) as excinfo:
        cutter.collect_evidence([empty])
    assert "empty-cache-write.csv" in str(excinfo.value)
