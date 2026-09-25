"""Float handicap H1 STEP-4A — THE DEAD COLUMN (his R54 "B"; Fable's (d)
reading; v3 [F-10] as STEP-0 amended it): a source's float or market-cap
column that is DEAD on a scan makes the handicap INOPERATIVE at factor 1
for THAT SCAN — every name — with `handicap` degraded and its reason.

DEAD: the header is absent from the source's export, or every equity row
of that source that reaches ranking has the cell blank, `-` or
unparseable. LIVE: at least one parseable cell. A source with NO equity
row reaching ranking has no column to judge and is neither (ESCALATED:
`reports/handicap-h1-build-2026-09-24.md` X1 — one of his lists carries
no equity row on any retained scan).

The scan is built from the committed real-shape exports; columns are
blanked INSIDE the test, never in the fixture (L45). Blocks are this
build's literals, never his.
"""

from __future__ import annotations

from decimal import Decimal

import pytest
from loguru import logger
from test_radar_handicap import block, pool
from test_radar_handicap_group import POOL_METRICS, RTH_NOW, SCREEN_FIXTURE, _CsvCollector, collect
from test_radar_handicap_shadow import HEADERS, NEW_FIELDS

from cobalt.radar.config import load_config
from cobalt.radar.models import Candidate, ExcludedBy, PoolBlock, SourceSet
from cobalt.radar.pool import Decision, decide

BLANKED = "screen:blanked@00000000000a"
LIVE = "screen:live@00000000000b"


def _scan(*, blank=(), drop=(), bad=(), one_blank_float=False):
    """Two sources on one scan: the redacted screen export (BLANKED, its
    columns changed here) and the pool-metrics export (LIVE)."""
    config = load_config()
    original = _CsvCollector.__init__

    def patched(self, path, cfg):
        original(self, path, cfg)
        if path != SCREEN_FIXTURE:
            return
        rows = []
        changed_one = False
        for row in self.rows:
            row = dict(row)
            for header in blank:
                row[header] = ""
            for header in bad:
                row[header] = "n/a"
            for header in drop:
                row.pop(header, None)
            if (one_blank_float and not changed_one and row["Industry"] != "Exchange Traded Fund"
                    and row["Shares Float"]):
                row["Shares Float"] = ""
                changed_one = True
            rows.append(row)
        self.rows = tuple(rows)
        self.header = tuple(h for h in self.header if h not in drop)

    _CsvCollector.__init__ = patched
    try:
        _c, _r, cand_a, sets_a = collect(SCREEN_FIXTURE)
        _c, _r, cand_b, sets_b = collect(POOL_METRICS)
    finally:
        _CsvCollector.__init__ = original
    (a,) = [s for s in sets_a if s.kind == "screen"]
    (b,) = [s for s in sets_b if s.kind == "screen"]
    a = a.model_copy(update={"source": BLANKED, "note_order": 0})
    b = b.model_copy(update={"source": LIVE, "note_order": 1})
    candidates: dict[str, Candidate] = {}
    for source, cands in ((a, cand_a), (b, cand_b)):
        for c in cands:
            prior = candidates.get(c.ticker)
            candidates[c.ticker] = Candidate(
                ticker=c.ticker,
                sources=(prior.sources if prior else []) + [source.source],
                excluded_by=c.excluded_by or (prior.excluded_by if prior else None),
            )
    return [a, b], candidates, config


def _decide(sources, candidates, **overrides) -> Decision:
    pool_block = PoolBlock(**{**pool(**block(**overrides)), "cap": 1000})
    return decide(list(candidates.values()), [], pool_block, sources, RTH_NOW, handicap_headers=HEADERS)


def _ranked(decision: Decision):
    return [t for t in decision.transitions if t.raw_rank is not None]


def _assert_inoperative(decision: Decision, *dead: str):
    ranked = _ranked(decision)
    assert ranked
    for t in ranked:
        assert t.handicap_factor == Decimal(1)                  # a computed outcome, never NULL
        assert t.handicap.effective_position == t.handicap.position == t.raw_rank
        for header in dead:
            assert f"dead column: {header} ({BLANKED})" in t.handicap.reason
    assert "handicap" in decision.degraded_sources and not decision.degraded
    reason = decision.reasons["handicap"]
    assert reason.startswith("handicap inoperative — dead column: ")
    for header in dead:
        assert f"{header} ({BLANKED})" in reason


# (i) THE CASE THE DESK NAMED: both columns of one source wholly blank
@pytest.mark.parametrize("combinator", ["any", "all"])
def test_both_columns_of_one_source_blank_make_the_whole_scan_inoperative(combinator):
    sources, candidates, _ = _scan(blank=("Shares Float", "Market Cap"))
    decision = _decide(sources, candidates, missing="apply", combinator=combinator)
    _assert_inoperative(decision, "Shares Float", "Market Cap")
    # "for that scan": the LIVE source's names carry factor 1 too.
    live_names = [t for t in _ranked(decision) if t.handicap.source == LIVE]
    assert live_names and all(t.handicap_factor == Decimal(1) for t in live_names)


# (ii) ONE dead column is enough
def test_a_wholly_blank_float_column_alone_is_enough():
    sources, candidates, _ = _scan(blank=("Shares Float",))
    _assert_inoperative(_decide(sources, candidates), "Shares Float")


# (iii) the header missing from a source's export
def test_a_missing_header_is_a_dead_column():
    sources, candidates, _ = _scan(drop=("Market Cap",))
    _assert_inoperative(_decide(sources, candidates), "Market Cap")


def test_unparseable_cells_count_as_blank_for_the_column_test():
    sources, candidates, _ = _scan(bad=("Shares Float",))
    _assert_inoperative(_decide(sources, candidates), "Shares Float")


# (iv) `missing: skip` + a dead column → the same (R54 overrides `missing`)
def test_skip_does_not_change_the_dead_column_outcome():
    sources, candidates, _ = _scan(blank=("Shares Float", "Market Cap"))
    _assert_inoperative(_decide(sources, candidates, missing="skip"), "Shares Float", "Market Cap")


# (v) a single blank cell on a LIVE column still follows `missing` (R52)
@pytest.mark.parametrize("missing,factor,line", [("apply", Decimal("0.8"), "unknown → applied"),
                                                 ("skip", Decimal(1), "unknown → not applied")])
def test_one_blank_cell_on_a_live_column_follows_missing(missing, factor, line):
    sources, candidates, _ = _scan(one_blank_float=True)
    decision = _decide(sources, candidates, missing=missing)
    blanked = [t for t in _ranked(decision) if t.handicap.verdict == "unknown" and t.handicap.source == BLANKED]
    assert blanked
    for t in blanked:
        assert t.handicap_factor == factor and line in t.handicap.reason
    assert "handicap" not in decision.degraded_sources


# (vi) INOPERATIVE IS NOT FAIL-SOFT: factor 1 stored, the catch never entered
def test_inoperative_is_a_stored_factor_one_and_no_error_is_logged():
    lines: list[str] = []
    sink = logger.add(lambda message: lines.append(str(message)), level="ERROR")
    try:
        sources, candidates, _ = _scan(blank=("Shares Float",))
        decision = _decide(sources, candidates)
    finally:
        logger.remove(sink)
    assert all(t.handicap_factor is not None and t.handicap is not None for t in _ranked(decision))
    assert lines == []


# (vii) SHADOW STILL NEVER SORTS on a dead-column scan
def test_shadow_never_sorts_on_a_dead_column_scan():
    sources, candidates, _ = _scan(blank=("Shares Float", "Market Cap"))
    pool_block = PoolBlock(**{**pool(**block()), "cap": 3})
    shadow = decide(list(candidates.values()), [], pool_block, sources, RTH_NOW, handicap_headers=HEADERS)
    absent = decide(list(candidates.values()), [], pool_block.model_copy(update={"handicap": None}),
                    sources, RTH_NOW, handicap_headers=HEADERS)
    assert [t.model_dump(exclude=NEW_FIELDS) for t in shadow.transitions] == [
        t.model_dump(exclude=NEW_FIELDS) for t in absent.transitions
    ]


def test_a_source_with_no_equity_row_reaching_ranking_is_not_dead():
    """The vacuous case (ESCALATED): a list of funds only has no column to
    judge; the handicap stays operative on the scan's other sources."""
    sources, candidates, _ = _scan()
    funds = SourceSet(
        source="list:funds@00000000000c", kind="list", tickers=["FUND1"],
        metrics={"FUND1": {"volume": 1.0, "rvol": 1.0, "float_m": None, "market_cap_m": None}}, note_order=2,
    )
    candidates["FUND1"] = Candidate(ticker="FUND1", sources=[funds.source], excluded_by=ExcludedBy.NOT_EQUITY)
    decision = _decide([*sources, funds], candidates)
    assert "handicap" not in decision.degraded_sources
    assert any(t.handicap_factor == Decimal("0.8") for t in _ranked(decision))
