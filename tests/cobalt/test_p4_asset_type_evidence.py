"""S2-P4 AT-0 — the fixture cutter's read-only `evidence` mode.

WHY. Finviz fills the `Asset Type` column only for funds (a fund's asset
class) and leaves it blank for an ordinary stock, so the radar config's
former one-column rule (`not_equity.values: [Exchange Traded Fund]`) matched
nothing. Before the rule was rebuilt, the hub wanted evidence from REAL
exports on whether "non-blank Asset Type" and "Industry = Exchange Traded
Fund" pick out the same rows; R16 "C" (2026-09-19) then ruled the OR of the
two, now built as `is_not_equity`. The mode under test produces that
evidence; it is a decision aid, not a rule, and it never writes a fixture.

The cutter is a script, not an importable package, so it is loaded by
path. Every assertion below is against committed real-shape exports
(L45): `pool-metrics.real-shape.csv` and `movers-gainers.real-shape.csv`
are both real 151-column screener exports, and since AT-1 2.5 re-cut the
movers fixtures at the radar's real column set BOTH carry `Asset Type`
and `Industry`. The movers cut is what gives tables A and B their first
real rows — 29 fund rows in 61 — so the report's row rendering is no
longer proved by hand-built report objects alone, and since FR-1 its
appended 61st row per side gives table C(ii) a real row too.

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
MOVERS_BOTH = [FIX / "replay" / f"movers-{side}.real-shape.csv" for side in ("gainers", "losers")]

#: Data-row counts of the two committed fixtures, as cut.
POOL_METRICS_ROWS = 20
#: 61, not 60: the export's top 60 plus the one row the cutter appends
#: per side for the blank-`Asset Type` fund class (AT-1 FR-1).
MOVERS_ROWS = 61
#: Rows of the movers cut whose `Asset Type` is non-blank, and the two
#: values they carry. Real content of the committed fixture.
MOVERS_FUND_ROWS = 29
MOVERS_ASSET_TYPES = [("CryptoCurrency", 5), ("Equities (Stocks)", 24)]
#: The appended row: a fund named by `Industry` alone. It is table B's
#: `<blank>` row and table C(ii)'s only row in this cut, and it carries a
#: ticker none of the 29 non-blank rows carries.
MOVERS_BLANK_TYPE_FUND_ROWS = 1
MOVERS_DISTINCT_FUND_TICKERS = MOVERS_FUND_ROWS + MOVERS_BLANK_TYPE_FUND_ROWS
#: The candidate not-equity rule the hub is weighing (R16 "C"): a row is
#: dropped when its `Asset Type` is non-blank OR its `Industry` is the
#: fund industry. `MOVERS_DROPPED` is how many rows of the committed
#: movers cut it drops; `MOVERS_STOCK_ROWS_HIT` is how many of those are
#: table C(i) — an ordinary stock, dropped by mistake.
MOVERS_DROPPED = MOVERS_FUND_ROWS + MOVERS_BLANK_TYPE_FUND_ROWS
MOVERS_STOCK_ROWS_HIT = 0
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
    """29 of the movers cut's 61 rows carry a non-blank `Asset Type`, in
    two values, and every one of them is ALSO `Industry = Exchange Traded
    Fund` — so table A is those two values and table C(i) stays empty.
    The 61st row is the appended blank-`Asset Type` fund: it is in table
    B under `<blank>` and in table C(ii), and it is why the two fund
    signals no longer agree on every row of this cut."""
    report = cutter.collect_evidence([MOVERS])
    assert report.rows_with_columns == MOVERS_ROWS
    assert [(row.asset_type, row.rows) for row in report.table_b] == [
        (cutter.BLANK, MOVERS_BLANK_TYPE_FUND_ROWS)
    ] + MOVERS_ASSET_TYPES
    assert [(row.asset_type, row.industry, row.rows) for row in report.table_a] == [
        (asset_type, cutter.FUND_INDUSTRY, rows) for asset_type, rows in MOVERS_ASSET_TYPES
    ]
    assert report.distinct_fund_tickers == MOVERS_DISTINCT_FUND_TICKERS
    assert report.distinct_asset_types == len(MOVERS_ASSET_TYPES)
    assert len(report.table_c_non_blank_not_fund) == MOVERS_STOCK_ROWS_HIT
    assert len(report.table_c_fund_blank_type) == MOVERS_BLANK_TYPE_FUND_ROWS
    assert report.table_c_total == MOVERS_BLANK_TYPE_FUND_ROWS


def test_a_real_export_renders_non_empty_a_and_b_tables():
    """The row rendering, exercised from a real artifact rather than from
    report objects built in the test (AT-0 ESCALATE 1)."""
    text = cutter.render_evidence(cutter.collect_evidence([MOVERS]))
    assert f"| Equities (Stocks) | {cutter.FUND_INDUSTRY} | 24 |" in text.splitlines()
    assert "| CryptoCurrency | 5 |" in text.splitlines()
    # only table C(i) is empty: the appended row fills C(ii) from a real
    # artifact, so the disagreement table renders rows here too
    assert [line for line in text.splitlines() if line == "(none)"] == ["(none)"]
    for ticker in _movers_tickers():
        assert ticker not in cutter.summarize_evidence(cutter.collect_evidence([MOVERS]))


# ---------------------------------------------------------------------
# the candidate rule's own two numbers (R16 "C")
# ---------------------------------------------------------------------


def test_dropped_under_new_rule_counts_every_row_the_candidate_rule_drops():
    """`non-blank Asset Type OR Industry = the fund industry`, counted
    over the committed real-shape exports. The radar fixture contributes
    nothing (no fund row anywhere in it), so the whole count is the
    movers cut's."""
    assert cutter.collect_evidence([POOL_METRICS]).dropped_under_new_rule == 0
    report = cutter.collect_evidence([POOL_METRICS, MOVERS])
    assert report.dropped_under_new_rule == MOVERS_DROPPED


def test_the_summary_line_carries_the_rule_count_and_the_stock_rows_it_hits():
    """Both numbers on the one stdout line: what the rule would drop, and
    how many of those are ordinary stocks (table C(i)) — the number that
    decides whether the rule is safe."""
    summary = cutter.summarize_evidence(cutter.collect_evidence([MOVERS]))
    assert f"dropped under the new rule: {MOVERS_DROPPED}" in summary
    assert f"stock rows hit: {MOVERS_STOCK_ROWS_HIT}" in summary


def test_the_report_file_carries_the_rule_count_and_the_stock_rows_it_hits():
    lines = cutter.render_evidence(cutter.collect_evidence([MOVERS])).splitlines()
    assert (
        f"- rows dropped under the new rule (non-blank `Asset Type` OR `Industry` = "
        f"{cutter.FUND_INDUSTRY}): {MOVERS_DROPPED}"
    ) in lines
    assert (
        f"- of those, stock rows hit (table C(i), a non-fund `Industry`): "
        f"{MOVERS_STOCK_ROWS_HIT}"
    ) in lines


def test_both_movers_cuts_hold_a_real_blank_type_fund_row():
    """The half of the candidate rule that the `Asset Type` column alone
    cannot carry: a fund Finviz left the `Asset Type` cell blank on, named
    only by `Industry`. It is table C(ii)'s whole class, and a cut without
    one would leave that branch of the rule untested against a real row.
    The cutter's `movers` mode guarantees one per side, appended from the
    same side's raw export when the top rows hold none. Counts only
    (L32)."""
    for path in MOVERS_BOTH:
        with path.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        blank_type_funds = [
            row
            for row in rows
            if not (row[cutter.ASSET_TYPE_COL] or "").strip()
            and (row[cutter.INDUSTRY_COL] or "").strip() == cutter.FUND_INDUSTRY
        ]
        assert len(blank_type_funds) >= 1, f"{path.name}: no blank-`Asset Type` fund row"


def test_a_stock_row_hit_is_counted_on_both_surfaces():
    """Renderer and summary only — NOT a parser tested against an
    invented export (L45). No committed real-shape export carries a table
    C(i) row, so the number that would decide the rule would otherwise
    render untested; the report object is built directly and its cells
    are labels, not data."""
    report = cutter.EvidenceReport(
        files_read=1,
        rows_with_columns=1,
        dropped_under_new_rule=1,
        table_c_non_blank_not_fund=[
            cutter.DisagreementRow(
                file="screen.csv",
                ticker="<none>",
                asset_type="Equity",
                industry="Shell Companies",
            )
        ],
    )
    assert "dropped under the new rule: 1" in cutter.summarize_evidence(report)
    assert "stock rows hit: 1" in cutter.summarize_evidence(report)
    assert (
        "- of those, stock rows hit (table C(i), a non-fund `Industry`): 1"
        in cutter.render_evidence(report).splitlines()
    )


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


# ---------------------------------------------------------------------
# spec-01 §3's personal-data transforms (tribunal A4)
#
# `spec-01:249` commissions `cards-day.real-shape.json` with three
# transforms, verbatim: "`user_id` → 1; all timestamps shifted to a fixed
# synthetic day with intraday offsets kept; free-text reasons →
# `"<reason>"`". The date shift is implemented (`_shift_dates`). The
# other two were not: `_anonymize` is a hex-suffix scrub plus that shift,
# so the cut stayed clean only because today's raw reads happen to select
# neither column. "The read happens to omit it" is not a transform — the
# next read that selects `*` would carry them straight into a committed
# file. These tests pin the committed fixture clean AND pin the transform
# itself, so the guarantee no longer depends on the shape of a query.
# This module is where they live because it already loads the cutter by
# path (`_load_cutter`); a second loader would be a second path (L3).
# ---------------------------------------------------------------------

CARDS_FIXTURE = FIX / "replay" / "cards-day.real-shape.json"

#: Every key either array of the committed cut carries, as cut.
CARDS_SIZING_KEYS = {"created_at", "direction", "entry", "id", "state", "stop", "ticker"}
CARDS_TRANSITION_KEYS = {"at", "card_id", "from_state", "to_state"}


def test_the_committed_cards_fixture_carries_no_owner_id_and_no_free_text():
    """A REGRESSION PIN, and that is its stated purpose: the committed
    fixture is already clean (the hub's A4 read, re-verified on this tip),
    so this is green today and fails the day a re-cut lets either class of
    column in."""
    import json

    raw = json.loads(CARDS_FIXTURE.read_text())
    assert set(raw) == {"sizings", "transitions"}
    assert {key for row in raw["sizings"] for key in row} == CARDS_SIZING_KEYS
    assert {key for row in raw["transitions"] for key in row} == CARDS_TRANSITION_KEYS
    every_key = CARDS_SIZING_KEYS | CARDS_TRANSITION_KEYS
    assert not (every_key & cutter.PERSONAL_ID_FIELDS)
    assert not (every_key & cutter.FREE_TEXT_FIELDS)


def test_the_cutter_flattens_the_owner_id_and_replaces_a_free_text_reason():
    """spec-01:249's two missing transforms, over a SYNTHETIC row that
    carries both columns — the shape a future `SELECT *` read would hand
    the cutter. Nothing else on the row may move."""
    rows = [{
        "id": 302, "ticker": "CRWD", "direction": "short", "entry": "219.0500",
        "state": "EXPIRED", "created_at": "2026-02-10 13:29:30.724041+00:00",
        "user_id": 7741,
        "reason": "synthetic free text standing in for whatever the trader typed",
        "note": None,
    }]
    out = cutter.strip_personal(rows)
    assert out[0]["user_id"] == 1
    assert out[0]["reason"] == "<reason>"
    assert out[0]["note"] is None                     # a NULL is not free text; the shape is kept
    assert {k: v for k, v in out[0].items() if k not in {"user_id", "reason"}} == {
        "id": 302, "ticker": "CRWD", "direction": "short", "entry": "219.0500",
        "state": "EXPIRED", "created_at": "2026-02-10 13:29:30.724041+00:00", "note": None}
    assert rows[0]["user_id"] == 7741                 # the input row is not mutated


def test_a_row_carrying_neither_column_is_returned_unchanged():
    rows = [dict.fromkeys(CARDS_SIZING_KEYS, "x")]
    assert cutter.strip_personal(rows) == rows
