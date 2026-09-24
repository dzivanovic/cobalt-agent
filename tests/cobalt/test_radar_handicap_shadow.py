"""Float handicap H1 STEP-4 (R26 B; v3 §1, §6, §7 (2); `29` §2, §5, §6):
the shadow computation inside `decide()` — the would-be pool-wide rank,
computed and stored, NEVER sorting.

Blocks are this build's literals (via `test_radar_handicap.block()`), never
his; every number asserted below is a literal of this file's construction.
"""

from __future__ import annotations

from decimal import Decimal

import pytest
from loguru import logger
from test_radar_handicap import block, pool
from test_radar_handicap_group import RTH_NOW, homogeneous

from cobalt.radar import handicap as handicap_module
from cobalt.radar.config import load_config
from cobalt.radar.handicap import HandicapRecord
from cobalt.radar.models import Candidate, OpenMember, PoolBlock, SourceHealth, SourceSet
from cobalt.radar.pool import Action, Decision, Transition, decide

HEADERS = load_config().export.handicap_headers
NEW_FIELDS = {"handicap_factor", "handicap"}


def _decide(pool_block, sources, candidates, opens=(), now=RTH_NOW):
    return decide(list(candidates.values()), list(opens), pool_block, sources, now, handicap_headers=HEADERS)


def _by(decision: Decision) -> dict[str, Transition]:
    return {t.ticker: t for t in decision.transitions}


def _without_handicap(pool_block: PoolBlock) -> PoolBlock:
    return pool_block.model_copy(update={"handicap": None})


def _screen(names: list[str], in_group: set[str], note_order=0, source="screen:one@000000000003"):
    """One screen whose metric orders `names` as given (first = best)."""
    size = len(names)
    metrics = {
        t: {"volume": float(size - i), "rvol": float(size - i),
            "float_m": 5.0 if t in in_group else 90.0, "market_cap_m": 900.0}
        for i, t in enumerate(names)
    }
    return SourceSet(source=source, kind="screen", tickers=names, metrics=metrics, note_order=note_order)


def _cands(*sources: SourceSet) -> dict[str, Candidate]:
    return {t: Candidate(ticker=t, sources=[s.source]) for s in sources for t in s.tickers}


# ---------------------------------------------------------------------
# (i) B exactly: eff = Decimal(raw) ÷ factor; order (eff, in_group, raw)
# ---------------------------------------------------------------------


def test_the_would_be_rank_is_the_pool_wide_re_sort_and_the_factor_is_the_blocks():
    pool_block, sources, candidates = homogeneous()
    by = _by(_decide(pool_block, sources, candidates))
    for ticker in "ABC":
        assert by[ticker].handicap_factor == Decimal("0.5")
        assert by[ticker].handicap.verdict == "yes"
    for ticker in "XYZ":
        assert by[ticker].handicap_factor == Decimal("1")
        assert by[ticker].handicap.verdict == "no"
    assert {t: by[t].handicap.effective_position for t in "AXBYCZ"} == {
        "A": 2, "X": 1, "B": 5, "Y": 3, "C": 6, "Z": 4,
    }
    for t in by.values():
        assert t.handicap.position == t.raw_rank == t.rank


def test_an_exact_tie_puts_the_unhandicapped_name_first():
    # raw 1 in group at factor 0.5 → eff 2; raw 2 not in group → eff 2.
    source = _screen(["H", "U"], {"H"})
    by = _by(_decide(PoolBlock(**pool(**block(factor="0.5"))), [source], _cands(source)))
    assert (by["U"].handicap.effective_position, by["H"].handicap.effective_position) == (1, 2)


def test_decimal_keeps_a_tie_that_float_division_would_break():
    names = [f"T{i:02d}" for i in range(1, 26)]
    source = _screen(names, {"T07"})
    # float: 7 / 0.28 is 24.999999999999996 (a probe's printed output, copied
    # verbatim), so a float key would put T07 AHEAD of T25.
    assert 7 / 0.28 < 25
    by = _by(_decide(PoolBlock(**pool(**block(factor="0.28"))), [source], _cands(source)))
    assert (by["T07"].raw_rank, by["T25"].raw_rank) == (7, 25)
    # Decimal: 7 ÷ 0.28 == 25 exactly — a tie — the unhandicapped T25 first.
    assert Decimal(7) / Decimal("0.28") == 25
    assert by["T25"].handicap.effective_position == 24
    assert by["T07"].handicap.effective_position == 25


# ---------------------------------------------------------------------
# (ii) SHADOW NEVER SORTS
# ---------------------------------------------------------------------


def _core(decision: Decision) -> list[dict]:
    return [t.model_dump(exclude=NEW_FIELDS) for t in decision.transitions]


@pytest.mark.parametrize("missing", ["apply", "skip"])
@pytest.mark.parametrize("combinator", ["any", "all"])
def test_shadow_changes_nothing_but_the_new_fields(missing, combinator):
    _pool_block, sources, candidates = homogeneous()
    pool_block = PoolBlock(**{**pool(**block(factor="0.5", missing=missing, combinator=combinator)), "cap": 3})
    opens = [OpenMember(ticker="C", sources=[sources[0].source], entered_at=RTH_NOW, below_cap_streak=0, last_rank=5)]
    shadow = _decide(pool_block, sources, candidates, opens)
    absent = _decide(_without_handicap(pool_block), sources, candidates, opens)
    assert _core(shadow) == _core(absent)
    assert [t.action for t in shadow.transitions] == [t.action for t in absent.transitions]
    assert shadow.degraded_sources == absent.degraded_sources == []
    assert all(t.handicap_factor is None and t.handicap is None for t in absent.transitions)
    assert any(t.handicap is not None for t in shadow.transitions)


# ---------------------------------------------------------------------
# (iii) the Transition fields and the HandicapRecord
# ---------------------------------------------------------------------


def test_the_record_has_exactly_v3s_ten_keys_and_no_decisive():
    assert set(HandicapRecord.model_fields) == {
        "float_m", "market_cap_m", "verdict", "reason", "missing_rule", "mode",
        "position", "effective_position", "source", "block_sha256",
    }
    assert HandicapRecord.model_config["extra"] == "forbid"
    assert {"raw_rank", "handicap_factor", "handicap"} <= set(Transition.model_fields)


def test_an_absent_block_stores_raw_rank_and_null_handicap_fields():
    pool_block, sources, candidates = homogeneous()
    decision = _decide(_without_handicap(pool_block), sources, candidates)
    for t in decision.transitions:
        assert t.raw_rank == t.rank is not None
        assert (t.handicap_factor, t.handicap) == (None, None)


def test_the_record_names_the_source_the_mode_the_missing_rule_and_the_block_hash():
    from cobalt.radar.evaluate import canonical_sha256

    pool_block, sources, candidates = homogeneous()
    record = _by(_decide(pool_block, sources, candidates))["A"].handicap
    assert (record.source, record.mode, record.missing_rule) == (sources[0].source, "shadow", "apply")
    assert record.block_sha256 == canonical_sha256(pool_block.handicap.model_dump(mode="json"))
    assert (record.float_m, record.market_cap_m) == (Decimal("5.0"), Decimal("900.0"))


@pytest.mark.parametrize("missing,factor,line", [("apply", "0.8", "unknown → applied"),
                                                 ("skip", "1", "unknown → not applied")])
def test_an_unknown_name_follows_missing(missing, factor, line):
    source = _screen(["K", "N"], set())
    source.metrics["N"]["float_m"] = None
    source.metrics["N"]["market_cap_m"] = None
    by = _by(_decide(PoolBlock(**pool(**block(missing=missing))), [source], _cands(source)))
    assert by["N"].handicap.verdict == "unknown"
    assert by["N"].handicap_factor == Decimal(factor)
    assert line in by["N"].handicap.reason


# ---------------------------------------------------------------------
# (iv) FAIL-SOFT, ONE CATCH (`29` §5)
# ---------------------------------------------------------------------


def test_a_raising_handicap_step_ranks_raw_flags_the_source_and_logs_one_error(monkeypatch):
    def boom(*_args, **_kwargs):
        raise ZeroDivisionError("synthetic")

    monkeypatch.setattr(handicap_module, "shadow_rank", boom)
    lines: list[str] = []
    sink = logger.add(lambda message: lines.append(str(message)), level="ERROR")
    try:
        pool_block, sources, candidates = homogeneous()
        decision = _decide(pool_block, sources, candidates)
    finally:
        logger.remove(sink)
    absent = _decide(_without_handicap(pool_block), sources, candidates)
    assert _core(decision) == _core(absent)
    for t in decision.transitions:
        assert t.raw_rank == t.rank is not None
        assert (t.handicap_factor, t.handicap) == (None, None)
    assert "handicap" in decision.degraded_sources
    # The pool-level flag is the SOURCES' (unchanged): a handicap problem
    # leaves every raw rank valid (picks and the heartbeat read that flag).
    assert decision.degraded is absent.degraded is False
    assert "ZeroDivisionError" in decision.reasons["handicap"]
    assert len(lines) == 1 and "ZeroDivisionError" in lines[0]


def test_the_catch_never_sees_a_block_refused_at_parse():
    """A present block missing a key is refused by `PoolBlock` (STEP-2): the
    pool freezes before `decide()` runs; nothing reaches the catch."""
    raw = pool(**block())
    del raw["handicap"]["combinator"]
    with pytest.raises(Exception, match="combinator"):
        PoolBlock(**raw)
    frozen = decide([], [], None, [], RTH_NOW, handicap_headers=HEADERS)
    assert frozen.frozen and frozen.degraded_sources == ["pool_block"]


# ---------------------------------------------------------------------
# (v) `mode: live` under H1 (`29` §6): stored as shadow, sorted raw, flagged
# ---------------------------------------------------------------------


def test_mode_live_stores_what_shadow_stores_sorts_raw_and_is_flagged():
    _pool_block, sources, candidates = homogeneous()
    live = PoolBlock(**pool(**block(factor="0.5", mode="live")))
    shadow = PoolBlock(**pool(**block(factor="0.5", mode="shadow")))
    live_d, shadow_d = _decide(live, sources, candidates), _decide(shadow, sources, candidates)
    assert _core(live_d) == _core(shadow_d)
    for a, b in zip(live_d.transitions, shadow_d.transitions):
        assert a.handicap_factor == b.handicap_factor
        assert a.handicap.model_dump(exclude={"mode", "block_sha256"}) == b.handicap.model_dump(
            exclude={"mode", "block_sha256"})
    assert "handicap" in live_d.degraded_sources and not live_d.degraded
    assert live_d.reasons["handicap"] == "mode live needs H2 — ranking raw"
    assert "handicap" not in shadow_d.degraded_sources


# ---------------------------------------------------------------------
# (vii) held members are not re-ranked
# ---------------------------------------------------------------------


def test_a_hold_carries_no_raw_rank_and_no_handicap():
    healthy = _screen(["A", "B"], {"A"})
    degraded = SourceSet(source="list:down@000000000009", kind="list", health=SourceHealth.DEGRADED, tickers=["H"])
    opens = [OpenMember(ticker="H", sources=[degraded.source], entered_at=RTH_NOW, below_cap_streak=0, last_rank=1)]
    by = _by(_decide(PoolBlock(**pool(**block())), [healthy, degraded], _cands(healthy), opens))
    assert by["H"].action is Action.HOLD
    assert (by["H"].raw_rank, by["H"].handicap_factor, by["H"].handicap) == (None, None, None)
    assert by["A"].raw_rank is not None and by["A"].handicap is not None
