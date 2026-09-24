"""S2-P4 STEP-5 formations — the positive half of R1-21, bound to S2-P2's
SHIPPED replay contract (chunk E2).

REAL ARTIFACTS ONLY (L45). Every formation in this module comes out of
S2-P2's own `replay_formations` run over S2-P2's own hub-cut bar fixture
(`tests/fixtures/radar/bars-rubberband.real-shape.json`) and the one
synthetic anatomy-only trade_def the repo ships, built through P2's own
test helper `radar_p2_support`. Nothing here hand-writes a
`ReplayFormation`: the contract under test is exactly what P2 produces.

The `with_trend` variant is the same shipped example note with one real
`valid_setups.relation` value swapped — P2's own helper takes those
overrides. It is used because it is the variant whose two same-day
formations of one (ticker, trade_def) both traded through their trigger
on the real tape, which is the R1-21 case ("two distinct formations
persisting under the extended key"). The shipped `countertrend` variant's
own two formations never traded through theirs — the real no-trigger
case, tested here too.

The counterfactual R is NOT recomputed here: a formation goes through the
SAME `counterfactual()` the card path uses (L3, one formula).
"""

from __future__ import annotations

import os
import re
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from functools import lru_cache

import pytest

import radar_p2_support as sup
from cobalt.radar.evaluate import EVALUATOR_VERSION
from cobalt.radar.evaluate_cli import replay_formations
from cobalt.replay.cards import resolve_window, session_close_for
from cobalt.replay.formations import (
    SUPPORTED_EVALUATORS,
    FormationContext,
    FormationSources,
    formation_candidates,
    formation_misses,
    replay_formation,
    replay_formation_from_receipt,
)
from cobalt.replay.models import FORMULA_VERSION, RadarCardRef, ReplayError, ReplayInputError
from cobalt.session import session_clock

UTC = timezone.utc
DAY = sup.TRADE_DATE                                   # 2026-01-06
CLOSE = session_close_for(DAY)                         # the real 16:00 ET close
MINUTE = timedelta(minutes=1)
MEMBER_FTFT = 100                                      # radar_p2_support.members()'s first id

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="requires_db: Postgres env settings not available",
)


# ---------------------------------------------------------------------------
# S2-P2's real replay, run exactly as its own tests run it
# ---------------------------------------------------------------------------


class ReadOnlyRadar(sup.FakeRadarStore):
    """P2's `--replay` store: every read works, every write is a failure."""

    def members_for_day(self, pool_key, day):
        return [dict(m, trade_date=day) for m in self.members]

    def __getattribute__(self, name):
        if name in {"apply_membership", "put_pool", "open_score_run", "put_scores", "finish_run"}:
            raise AssertionError(f"the read-only formation replay called the write method {name}")
        return super().__getattribute__(name)


def _daily(ticker, day):
    return sup.fixture_daily(ticker, datetime(2026, 1, 6, 12, 0, tzinfo=UTC))


def with_trend_def():
    """The shipped example def with one real relation value swapped."""
    return sup.loaded(sup.anatomy_def(valid_setups=[{"setup_ref": "overextension", "relation": "with_trend"}]))


def countertrend_def():
    """`radar_p2_support.anatomy_def()` exactly as it ships."""
    return sup.loaded()


def _p2_run(variant: str):
    """One real P2 replay: ~230 scans through the real evaluator."""
    loaded = with_trend_def() if variant == "with_trend" else countertrend_def()
    tickers = ("FTFT", "BGFI")
    radar = ReadOnlyRadar(sup.members(*tickers), {t: sup.fixture_bars(t) for t in tickers})
    report = replay_formations(
        DAY, pool_key="pool", slug_filter=None, radar_store=radar,
        defs_source=lambda: ([loaded], {}), daily_source=_daily, tunables=sup.engine_tunables(),
        defaults=sup.defaults(), clock=session_clock(), out=lambda _line: None,
    )
    return loaded, report


#: The run is the expensive part, so it happens once per variant and each
#: test reads its own deep copy.
_cached_run = lru_cache(maxsize=None)(_p2_run)


def p2_report(variant: str = "with_trend"):
    return _cached_run(variant)[1].model_copy(deep=True)


def context(*, cards=(), bars=None, trade_date=DAY, session_close=CLOSE):
    series = sup.fixture_bars("FTFT") if bars is None else bars
    return FormationContext(
        trade_date=trade_date, session_close=session_close,
        bars_for=lambda ticker: [b for b in series if b.ticker == ticker],
        radar_cards=lambda: list(cards),
    )


def misses(report, *, evaluator_version=EVALUATOR_VERSION, **ctx):
    return formation_misses(report, context=context(**ctx), evaluator_version=evaluator_version)


# =====================================================================
# P2 side: the three fields the `missed` CHECK needs (R1-21)
# =====================================================================


def test_p2_replay_formation_carries_the_membership_id_md5_and_score_receipt_reference():
    loaded, report = _p2_run("with_trend")
    assert len(report.formations) == 2, "P2's own fixture day forms twice for this def"
    for f in report.formations:
        assert f.membership_id == MEMBER_FTFT
        assert f.trade_def_md5 == loaded.md5
        assert re.fullmatch(r"[0-9a-f]{64}", f.score_inputs_sha256)
    # the reference is the evaluation's own digest: two formations, two
    # distinct evaluations, two distinct retained score receipts
    assert report.formations[0].score_inputs_sha256 != report.formations[1].score_inputs_sha256
    # and it is deterministic — a second real run replays to the same digests
    assert [f.score_inputs_sha256 for f in _p2_run("with_trend")[1].formations] == \
        [f.score_inputs_sha256 for f in report.formations]


def test_the_shipped_capability_marker_is_the_one_replay_binds_to():
    assert EVALUATOR_VERSION in SUPPORTED_EVALUATORS


# =====================================================================
# Two formations of one (ticker, trade_def) -> two rows (R1-21)
# =====================================================================


def test_two_same_day_formations_of_one_ticker_and_def_persist_as_two_rows_under_the_extended_key():
    outcome = misses(p2_report("with_trend"))
    assert outcome.status == EVALUATOR_VERSION
    rows = list(outcome.rows)
    assert (outcome.counts.candidates, outcome.counts.misses, outcome.counts.suppressed) == (2, 2, 0)
    assert [r.formation_at.isoformat() for r in rows] == [
        "2026-01-06T16:22:00+00:00", "2026-01-06T18:42:00+00:00"]
    assert {r.kind for r in rows} == {"formation"}
    assert {r.ticker for r in rows} == {"FTFT"}
    assert {r.pool_member_id for r in rows} == {MEMBER_FTFT}
    assert len({r.trade_def_md5 for r in rows}) == 1
    # the extended subject key differs in exactly the formation_at slot
    a, b = (r.subject() for r in rows)
    assert a != b
    assert [i for i, (x, y) in enumerate(zip(a, b)) if x != y] == [5]


def test_every_formation_row_satisfies_0009s_formation_check():
    for row in misses(p2_report("with_trend")).rows:
        assert row.trade_def_md5 is not None and row.formation_at is not None
        assert row.pool_member_id is not None
        assert row.card_id is None and row.mover_id is None
        assert row.excluded_by == "no_card"
        assert row.formula_version == FORMULA_VERSION


@requires_db
def test_two_formation_rows_land_under_the_live_unique_index(dev_db_tx):
    from cobalt import db
    from cobalt.replay.cards import MissedStore

    store = MissedStore()
    with db.connect(store.db_name, side=db.Side.SYSTEM) as conn:
        conn.execute("INSERT INTO system.radar_pool (pool_key,state,session,members) "
                     "VALUES ('e2_proof','scanning','rth',1) ON CONFLICT (pool_key) DO NOTHING")
        member = conn.execute(
            "INSERT INTO system.radar_membership (pool_key,ticker,trade_date,first_seen_at,entered_at,"
            "source,sources,session,opened_scan_id,last_scan_id) VALUES ('e2_proof','FTFT',%s,"
            "'2026-01-06 14:35+00','2026-01-06 14:35+00','test','[\"test\"]'::jsonb,'rth',1,1) RETURNING id",
            (DAY,),
        ).fetchone()[0]
    rows = [r.model_copy(update={"pool_member_id": member})
            for r in misses(p2_report("with_trend")).rows]
    counts = store.reconcile(run_id="e2-proof", trade_date=DAY, kind="formation", rows=rows)
    assert counts.inserted == 2
    current = store.current(DAY, "formation")
    assert len(current) == 2
    assert {r["excluded_by"] for r in current} == {"no_card"}


# =====================================================================
# Existing-card suppression (R1-21)
# =====================================================================


def _card_ref(direction="long", slug="example-anatomy-reversal", member=MEMBER_FTFT):
    return RadarCardRef(card_id=7701, pool_member_id=member, trade_def_slug=slug,
                        direction=direction, state="WATCH",
                        created_at=datetime(2026, 1, 6, 16, 25, tzinfo=UTC))


def test_an_existing_open_radar_card_for_member_def_direction_suppresses_the_miss():
    outcome = misses(p2_report("with_trend"), cards=[_card_ref()])
    assert list(outcome.rows) == []
    assert (outcome.counts.candidates, outcome.counts.misses, outcome.counts.suppressed) == (2, 0, 2)


@pytest.mark.parametrize("ref", [
    _card_ref(direction="short"),                       # the other direction
    _card_ref(slug="some-other-def"),                   # another trade_def
    _card_ref(member=101),                              # another pool member
])
def test_a_card_on_a_different_member_def_or_direction_does_not_suppress(ref):
    outcome = misses(p2_report("with_trend"), cards=[ref])
    assert (outcome.counts.misses, outcome.counts.suppressed) == (2, 0)


# =====================================================================
# cf-R through P2's evaluator values, on the ONE formula (R4, R1-9, L57)
# =====================================================================


def test_cf_r_for_a_formation_is_the_one_formula_over_p2s_own_trigger_and_stop():
    first, second = misses(p2_report("with_trend")).rows
    # P2's formation: trigger 5.3500 / stop 5.33; the trigger bar OPENED
    # beyond the trigger, so the fill is the bar open (R1-9 gap-through)
    assert (first.entry, first.stop) == (Decimal("5.3500"), Decimal("5.33"))
    assert first.trigger_ts == datetime(2026, 1, 6, 16, 25, tzinfo=UTC)
    assert first.fill_price == Decimal("5.3880")
    assert (first.exit_reason, first.exit_price) == ("stop", Decimal("5.33"))
    assert first.exit_ts == datetime(2026, 1, 6, 16, 45, tzinfo=UTC)
    assert (first.cf_r, first.mfe_r) == (Decimal("-2.9000"), Decimal("20.1000"))
    assert (second.entry, second.stop) == (Decimal("6.5900"), Decimal("6.57"))
    assert second.fill_price == Decimal("7.1100")
    assert (second.cf_r, second.mfe_r) == (Decimal("-27.0000"), Decimal("118.5000"))
    assert second.horizon_end == CLOSE


def test_every_formation_number_replays_from_its_stored_receipt():
    for row in misses(p2_report("with_trend")).rows:
        again = replay_formation_from_receipt(row.receipt)
        assert again.status == "miss"
        assert again.miss.inputs_sha256 == row.inputs_sha256
        assert (again.miss.cf_r, again.miss.mfe_r) == (row.cf_r, row.mfe_r)
        assert again.miss.subject() == row.subject()


def test_the_receipt_retains_the_p2_contract_facts_and_the_score_receipt_reference():
    row = misses(p2_report("with_trend")).rows[0]
    contract = row.receipt["inputs"]["p2_contract"]
    assert contract["evaluator_version"] == EVALUATOR_VERSION
    assert contract["module"] == "cobalt.radar.evaluate_cli"
    assert contract["callable"] == "replay_formations"
    reference = row.receipt["inputs"]["score_receipt"]
    assert reference["table"] == "system.radar_score"
    assert reference["key"] == {"membership_id": MEMBER_FTFT, "trade_def_md5": row.trade_def_md5}
    assert re.fullmatch(r"[0-9a-f]{64}", reference["inputs_sha256"])
    assert row.gate_detail["order"] == ["existing_card"]
    assert row.gate_detail["existing_card"]["fired"] is False
    assert row.gate_detail["trade_count_band"] == "unset"


def test_the_window_comes_from_the_one_public_resolver():
    row = misses(p2_report("with_trend")).rows[0]
    resolved = resolve_window(None, DAY)
    assert row.receipt["inputs"]["window"]["resolved_end"] == resolved.resolved_end.isoformat()
    assert row.receipt["inputs"]["window"]["source"] == resolved.source


# =====================================================================
# No trigger, stale bars — never a fake R (R1-12)
# =====================================================================


def test_formations_whose_trigger_never_traded_through_write_no_row():
    report = p2_report("countertrend")
    assert len(report.formations) == 2, "the shipped def's own two same-day formations"
    outcome = misses(report)
    assert list(outcome.rows) == []
    assert (outcome.counts.candidates, outcome.counts.no_trigger) == (2, 2)


def test_bars_that_do_not_cover_the_day_are_input_stale_and_write_no_row():
    truncated = [b for b in sup.fixture_bars("FTFT") if b.ts < datetime(2026, 1, 6, 19, 0, tzinfo=UTC)]
    outcome = misses(p2_report("with_trend"), bars=truncated)
    assert list(outcome.rows) == []
    assert outcome.counts.input_stale == 2


def test_a_formation_with_no_bars_at_all_is_input_stale():
    outcome = misses(p2_report("with_trend"), bars=[])
    assert (outcome.counts.misses, outcome.counts.input_stale) == (0, 2)


# =====================================================================
# Fail-loud on the contract itself (L1)
# =====================================================================


def test_an_unsupported_evaluator_version_refuses():
    with pytest.raises(ReplayError, match="evaluator version"):
        misses(p2_report("with_trend"), evaluator_version="s9p9.0")


def test_a_formation_whose_stop_sits_on_the_wrong_side_of_its_trigger_refuses():
    report = p2_report("with_trend")
    report.formations[0] = report.formations[0].model_copy(update={"stop": "9.00"})
    with pytest.raises(ReplayInputError, match="wrong side of entry"):
        misses(report)


def test_candidates_carry_every_field_the_row_needs():
    report = p2_report("with_trend")
    candidates = formation_candidates(report, evaluator_version=EVALUATOR_VERSION)
    assert [c.formed_at for c in candidates] == [f.formed_bar_ts for f in report.formations]
    assert [c.seen_at for c in candidates] == [f.seen_at for f in report.formations]
    assert [(c.entry, c.stop) for c in candidates] == [
        (Decimal(f.trigger), Decimal(f.stop)) for f in report.formations]
    assert {c.evaluator_version for c in candidates} == {EVALUATOR_VERSION}
    assert {c.score_inputs_sha256 for c in candidates} == {f.score_inputs_sha256 for f in report.formations}


def test_replay_formation_refuses_a_formation_stamped_for_another_day():
    candidate = formation_candidates(p2_report("with_trend"), evaluator_version=EVALUATOR_VERSION)[0]
    other = date(2026, 1, 7)
    with pytest.raises(ReplayInputError, match="trade date"):
        replay_formation(candidate, sup.fixture_bars("FTFT"), trade_date=other,
                         window=resolve_window(None, other), session_close=session_close_for(other),
                         radar_cards=[])


def test_formation_sources_name_every_argument_p2s_entrypoint_takes():
    import inspect

    taken = set(inspect.signature(replay_formations).parameters) - {"day", "out", "slug_filter"}
    assert taken <= set(FormationSources.__dataclass_fields__)
