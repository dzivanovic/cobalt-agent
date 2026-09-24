"""S2-P2 chunk B — the store halves on cobalt_dev (`requires_db`, hub-run).

Everything runs inside the suite's rolled-back `cobalt_dev` transaction
(`conftest.dev_db_tx`), each store on its own side role. Real
concurrency cannot be shown on the shared rollback connection, so the
lock tests prove the ordering each lock enforces (state re-read under the
lock, the partial unique indexes) rather than racing two sessions.

Bars are the hub-cut real-shape fixture rows under a synthetic ticker so
they can never collide with archived rows.
"""

from __future__ import annotations

import asyncio
import os
from datetime import datetime, timedelta, timezone
from decimal import Decimal

import psycopg
import pytest

import radar_p2_support as sup

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)
pytestmark = [requires_db, pytest.mark.integration]

UTC = timezone.utc
TICKER = "ZZPB"
POOL = "p2_chunk_b"
SCAN0 = datetime(2026, 1, 6, 16, 30, tzinfo=UTC)

ENABLED = {
    "radar.cards_enabled": True,
    "card.proposed_key": {"a_plus_min": 0.9, "a_min": 0.8, "b_min": 0.6, "c_min": 0.4},
    "card.curves": {"atrs_from_open": [[1, 2], [6, 9]], "rvol": [[1, 1], [3, 6], [10, 10]],
                    "Extension.leg_count": [[2, 3], [20, 9]], "htf_level_proximity": [[0, 9], [2, 2]]},
}


@pytest.fixture
def world():
    from cobalt.archiver.store import BarStore
    from cobalt.cards.store import CardStore
    from cobalt.radar.evaluate import EvaluateStage
    from cobalt.radar.store import RadarStore
    from cobalt.session import session_clock
    from cobalt.settings.store import TraderSettingsStore

    radar, cards, settings = RadarStore("cobalt_dev"), CardStore("cobalt_dev"), TraderSettingsStore("cobalt_dev")
    cards.ensure_schema()
    with radar._connect() as conn:
        conn.execute(
            "INSERT INTO radar_pool (pool_key, state, session, members) VALUES (%s, 'scanning', 'rth', 1) "
            "ON CONFLICT DO NOTHING", (POOL,),
        )
        member_id = conn.execute(
            "INSERT INTO radar_membership (pool_key, ticker, trade_date, first_seen_at, entered_at, source, "
            "sources, rank_at_entry, last_rank, session, opened_scan_id, last_scan_id) VALUES "
            "(%s, %s, %s, %s, %s, 'screen', '[]', 1, 1, 'rth', -77, -77) RETURNING id",
            (POOL, TICKER, sup.TRADE_DATE, SCAN0 - timedelta(hours=2), SCAN0 - timedelta(hours=2)),
        ).fetchone()[0]
    BarStore("cobalt_dev").upsert_bars([b.model_copy(update={"ticker": TICKER}) for b in sup.fixture_bars("FTFT")])
    rows = sup.fixture_settings_rows(**ENABLED)
    rows["aset.account_mode"] = "sim"
    settings.put(rows, source="test")

    async def daily(ticker, now):
        series = sup.fixture_daily("FTFT", now)
        return series.model_copy(update={"ticker": ticker})

    stage = EvaluateStage(
        radar_store=radar, card_store=cards, defs_source=lambda: ([sup.loaded()], {}),
        settings_values=settings.values, daily_source=daily, tunables_loader=sup.engine_tunables,
        defaults_loader=sup.defaults, clock=session_clock(), now=lambda: SCAN0,
        members_at=lambda _pool, _at: radar.admitted_members(POOL),
    )

    def scan(at):
        from cobalt.radar.anatomy.freshness import RvolObservation

        stage.now = lambda: at
        return asyncio.run(stage.run(
            pool_key=POOL, scan_id=int(at.timestamp() * 1000), session="RTH", instant=at,
            rvol={TICKER: RvolObservation(ticker=TICKER, value=4.2, observed_at=at, source="screen:s",
                                          candidates=("screen:s",))},
            pool_unit={"pool_block": None}, gate=lambda _label: (lambda: None),
        ))

    return {"radar": radar, "cards": cards, "settings": settings, "member_id": member_id, "scan": scan}


def test_s5_end_to_end_writes_on_cobalt_dev_and_replays(world):
    from cobalt.radar.evaluate import replay_receipt
    from cobalt.session import session_clock

    first = world["scan"](SCAN0)
    assert first.created, first.refusals
    card_id = first.created[0]
    second = world["scan"](SCAN0 + timedelta(seconds=100))
    assert second.refreshed == [card_id]
    radar, cards = world["radar"], world["cards"]
    with radar._connect() as conn:
        statuses = conn.execute(
            "SELECT status FROM radar_score_run WHERE pool_key = %s ORDER BY id", (POOL,)
        ).fetchall()
    assert [s[0] for s in statuses] == ["complete", "complete"]
    board = radar.board(POOL)
    assert len(board) == 1 and board[0]["evaluation"] == "formed" and board[0]["proximity"] is not None
    with cards._connect() as conn:
        card = conn.execute(
            "SELECT origin, state, grade, risk_budget, shares, used_risk, trigger_price, entry, radar_score_id "
            "FROM aset_sizings WHERE id = %s", (card_id,),
        ).fetchone()
        dots = conn.execute("SELECT count(*) FROM card_dots WHERE card_id = %s", (card_id,)).fetchone()[0]
        genesis = conn.execute(
            "SELECT from_state, to_state, actor, evidence->>'run_id' FROM card_transitions WHERE card_id = %s",
            (card_id,),
        ).fetchall()
        view = conn.execute("SELECT outside_pool, board_evaluation FROM radar_cards_v WHERE card_id = %s",
                            (card_id,)).fetchone()
    assert card[:6] == ("radar", "WATCH", None, None, None, None)
    assert card[6] == card[7] and card[8] == board[0]["id"]
    assert dots == len(sup.ANATOMY_FACTORS)
    assert genesis == [(None, "WATCH", "cobalt", str(first.run_id))]
    assert view == (False, "formed")
    chain = cards.receipts_chain(second.receipt_id)
    assert len(chain) == 2
    _evaluations, replayed = replay_receipt(chain, clock=session_clock())
    assert replayed and all(r.recomputed == r.published for r in replayed)


def test_the_database_holds_one_open_radar_card_per_member_def_direction(world):
    first = world["scan"](SCAN0)
    cards = world["cards"]
    spec_row = first.created[0]
    with cards._connect() as conn:
        row = conn.execute(
            "SELECT pool_member_id, trade_def_slug, direction, trade_def_md5, radar_score_id FROM aset_sizings "
            "WHERE id = %s", (spec_row,),
        ).fetchone()
    from cobalt.cards.radar import RadarCardSpec

    spec = RadarCardSpec(
        ticker=TICKER, direction=row[2], session="RTH", pool_member_id=row[0], trade_def_slug=row[1],
        trade_def_md5=row[3], setup_ref="overextension", trigger_type="bar_break", trigger_price=Decimal("5.50"),
        stop_ref="snapback_candle", structural_stop=Decimal("5.81"), formed_at=SCAN0 - timedelta(minutes=5),
        expires_at=SCAN0 + timedelta(hours=1), why="retry", radar_score_id=row[4], scan_id=1,
        formula_sha256="a" * 64, tunables_sha256="b" * 64, settings_sha256="c" * 64, proximity=Decimal("0.5"),
        dots=[], evidence={"retry": True},
    )
    assert cards.create_radar_card(spec, now=SCAN0) is None  # a retry: already open, not a second card


def test_unsized_arm_is_refused_inside_the_locked_transition_and_sized_arm_passes(world):
    from cobalt.aset.engine import size_at_key
    from cobalt.aset.models import Direction, Grade
    from cobalt.cards import Actor, CardState, CardStateError
    from cobalt.settings.models import TraderSettings

    card_id = world["scan"](SCAN0).created[0]
    cards = world["cards"]
    with pytest.raises(CardStateError, match="UNSIZED"):
        cards.transition(card_id, CardState.ARMED, actor=Actor.YOU)
    assert cards.state_of(card_id) is CardState.WATCH
    assert len(cards.history(card_id)) == 1

    trader = TraderSettings.from_db(world["settings"])
    record = cards.radar_card(card_id)
    sizing = size_at_key(
        Grade.A_PLUS, ticker=TICKER, entry=record["entry"], stop=record["stop"], direction=Direction(record["direction"]),
        sheet_modes=trader.sheet_modes, sheet="half", enabled=trader.daymode.enabled_grades_for("reduced"),
        max_stop_distance_pct=Decimal("10"),
    )
    written = cards.tap_key(card_id, sizing)
    assert written["tapped_grade"] == "A+" and written["sized_grade"] == "A" and written["risk_budget"] == "70.00"
    cards.transition(card_id, CardState.ARMED, actor=Actor.YOU)
    assert cards.state_of(card_id) is CardState.ARMED
    with pytest.raises(CardStateError, match="frozen in ARMED"):
        cards.tap_key(card_id, sizing)  # key/ARM race: the loser re-reads ARMED under the lock


def test_a_stop_edit_before_the_first_key_tap_keeps_sizing_null(world):
    from cobalt.cards import Actor

    card_id = world["scan"](SCAN0).created[0]
    cards = world["cards"]
    cards.record_stop_edit(card_id, from_stop=Decimal("5.81"), to_stop=Decimal("5.90"), actor=Actor.YOU)
    with cards._connect() as conn:
        row = conn.execute(
            "SELECT stop, per_share_risk, grade, risk_budget, shares, used_risk, structural_stop FROM aset_sizings "
            "WHERE id = %s", (card_id,),
        ).fetchone()
    assert row[0] == Decimal("5.90") and row[1] == Decimal("0.40")
    assert row[2:6] == (None, None, None, None)
    assert row[6] == Decimal("5.81")  # formation evidence is immutable


def test_manual_cards_are_unaffected(world):
    from cobalt.aset.engine import compute_sizing
    from cobalt.aset.models import Grade, SheetMode, SizingInput
    from cobalt.aset.store import AsetStore
    from cobalt.cards import Actor, CardState

    aset = AsetStore("cobalt_dev")
    result = compute_sizing(
        SizingInput(ticker="ZZMAN", grade=Grade.B, direction="long", sheet_mode=SheetMode.FULL,
                    risk_dollars=Decimal("60"), entry=Decimal("10"), stop=Decimal("9.5")),
        [Grade.B], Decimal("10"),
    )
    card_id = aset.save(result)
    cards = world["cards"]
    # a sized WATCH stop edit still resizes (the pre-S2-P2 path)
    cards.record_stop_edit(card_id, from_stop=Decimal("9.5"), to_stop=Decimal("9.0"), actor=Actor.YOU)
    with cards._connect() as conn:
        shares = conn.execute("SELECT shares FROM aset_sizings WHERE id = %s", (card_id,)).fetchone()[0]
    assert shares == 60
    cards.transition(card_id, CardState.ARMED, actor=Actor.YOU)
    assert cards.state_of(card_id) is CardState.ARMED
    # `fill` returns a FillResult (S2-P4 R1-5), not a list of ids: the two
    # rows are the one-click manual route's TRIGGERED hop and the FILLED hop.
    result = cards.fill(card_id, actor=Actor.YOU)
    assert len(result.transition_ids) == 2


def test_dot_taps_append_recompute_and_are_never_overwritten_by_a_scan(world):
    from cobalt.aset.models import Grade
    from cobalt.settings.card import CardSettings

    card_id = world["scan"](SCAN0).created[0]
    cards = world["cards"]
    bands = CardSettings.from_rows(ENABLED).proposed_key
    cards.tap_dot(card_id, "trail_fit", 8, bands=bands, enabled=[Grade.A, Grade.B, Grade.C])
    result = cards.tap_dot(card_id, "trail_fit", 9, bands=bands, enabled=[Grade.A, Grade.B, Grade.C])
    assert result["conviction"] == "0.9" and result["card_score"] is not None
    with cards._connect() as conn:
        taps = conn.execute("SELECT grade FROM card_dot_taps WHERE card_id = %s ORDER BY id", (card_id,)).fetchall()
        conn.execute("SAVEPOINT immutable_probe")
        with pytest.raises(psycopg.errors.RaiseException):
            conn.execute("UPDATE card_dot_taps SET grade = 1 WHERE card_id = %s", (card_id,))
        conn.execute("ROLLBACK TO SAVEPOINT immutable_probe")
    assert [t[0] for t in taps] == [8, 9]
    world["scan"](SCAN0 + timedelta(seconds=100))
    with cards._connect() as conn:
        grade = conn.execute(
            "SELECT trader_grade FROM card_dots WHERE card_id = %s AND factor = 'trail_fit'", (card_id,)
        ).fetchone()[0]
    assert grade == 9


def test_shadow_agreement_v_pairs_taps_with_the_engine_grade_per_factor_and_et_day(world):
    """STEP-10: the view the shadow report reads, on real taps."""
    from datetime import date

    from cobalt.aset.models import Grade
    from cobalt.cards import shadow_report as sr
    from cobalt.settings.card import CardSettings

    card_id = world["scan"](SCAN0).created[0]
    cards = world["cards"]
    bands = CardSettings.from_rows(ENABLED).proposed_key
    with cards._connect() as conn:
        engine = conn.execute(
            "SELECT engine_grade FROM card_dots WHERE card_id = %s AND factor = 'rvol'", (card_id,)
        ).fetchone()[0]
    assert engine is not None
    enabled = [Grade.A, Grade.B, Grade.C]
    next_day = SCAN0 + timedelta(days=1)
    cards.tap_dot(card_id, "rvol", engine, bands=bands, enabled=enabled, now=SCAN0)
    cards.tap_dot(card_id, "rvol", max(1, engine - 3), bands=bands, enabled=enabled, now=SCAN0 + timedelta(minutes=1))
    cards.tap_dot(card_id, "setup_relation", 7, bands=bands, enabled=enabled, now=SCAN0)  # no engine grade: no pair
    cards.tap_dot(card_id, "rvol", engine, bands=bands, enabled=enabled, now=next_day)
    rows = [r for r in cards.shadow_agreement(None)
            if r["trade_date"] in (date(2026, 1, 6), date(2026, 1, 7))]
    assert {r["factor"] for r in rows} == {"rvol"}
    assert [(r["trade_date"], r["pairs"], list(r["deltas"])) for r in sorted(rows, key=lambda r: r["trade_date"])] == [
        (date(2026, 1, 6), 2, [0, engine - max(1, engine - 3)]), (date(2026, 1, 7), 1, [0]),
    ]
    report = sr.shadow_report(rows, bar=CardSettings.from_rows(
        {"radar.cards_enabled": False,
         "card.shadow_promotion_bar": {"sessions": 10, "pairs": 30, "median_max": 1, "within2_min": 0.9}},
    ).shadow_promotion_bar, since=None)
    assert report.factors[0].sessions == 2 and report.factors[0].pairs == 3 and not report.factors[0].gate_met


def test_one_promoted_card_and_release(world):
    card_id = world["scan"](SCAN0).created[0]
    cards = world["cards"]
    cards.set_promoted(card_id, True)
    assert cards.radar_card(card_id)["promoted_at"] is not None
    cards.set_promoted(card_id, False)
    assert cards.radar_card(card_id)["promoted_at"] is None


def test_a_publish_failure_leaves_the_run_unpublished_on_cobalt_dev(world):
    from cobalt.radar.evaluate import EvaluateError

    world["scan"](SCAN0)
    cards = world["cards"]
    original = cards.write_receipt

    def boom(row, **kw):
        raise RuntimeError("synthetic receipt failure")

    cards.write_receipt = boom
    with pytest.raises(EvaluateError):
        world["scan"](SCAN0 + timedelta(seconds=100))
    cards.write_receipt = original
    radar = world["radar"]
    with radar._connect() as conn:
        statuses = [r[0] for r in conn.execute(
            "SELECT status FROM radar_score_run WHERE pool_key = %s ORDER BY id", (POOL,)
        ).fetchall()]
    assert statuses == ["complete", "failed"]
    assert {row["run_id"] for row in radar.board(POOL)} == {radar.latest_run_id(POOL) - 1}


def test_audit_export_of_a_cobalt_dev_run_verifies_and_writes_the_bundle(world, tmp_path):
    """STEP-11 against the real stores: the run row, its score rows and its
    receipt chain as Postgres returns them (JSONB, TIMESTAMPTZ, NUMERIC)."""
    import hashlib
    import json

    from cobalt.aset.models import Grade
    from cobalt.radar.audit_export import export_run
    from cobalt.session import session_clock
    from cobalt.settings.card import CardSettings

    card_id = world["scan"](SCAN0).created[0]
    world["cards"].tap_dot(card_id, "trail_fit", 7, bands=CardSettings.from_rows(ENABLED).proposed_key,
                           enabled=[Grade.A, Grade.B, Grade.C], now=SCAN0 + timedelta(seconds=30))
    second = world["scan"](SCAN0 + timedelta(seconds=100))
    out = tmp_path / "bundle"
    manifest = export_run(second.run_id, radar_store=world["radar"], card_store=world["cards"], out=out,
                          clock=session_clock(), generated_at=SCAN0 + timedelta(hours=8))
    assert manifest.self_check["all_equal"] and all(h["matches"] for h in manifest.hashes.values())
    for name, digest in manifest.files.items():
        assert hashlib.sha256((out / name).read_bytes()).hexdigest() == digest
    cards = json.loads((out / "cards.json").read_text())["cards"]
    assert cards and cards[0]["card_id"] == card_id and cards[0]["published"]["card_score"] is not None


def test_the_ladder_reads_radar_cards_v_with_its_dots_on_cobalt_dev(world):
    """STEP-8: the panel's one read is the user-side view, dots attached,
    validated by the panel's row model and rendered with its badges."""
    from cobalt.aset import radar_panel as panel
    from cobalt.cards.radar import FIELD_OWNERS
    from cobalt.session import session_clock

    first = world["scan"](SCAN0)
    card_id = first.created[0]
    rows = world["cards"].radar_board_cards(sup.TRADE_DATE)
    row = next(r for r in rows if r["card_id"] == card_id)
    assert set(row) - {"dots"} == set(FIELD_OWNERS)
    assert len(row["dots"]) == len(sup.ANATOMY_FACTORS) and row["pool_position"] == 1
    view = panel.build_ladder_view(
        card_store=world["cards"], settings_store=world["settings"], clock=session_clock(),
        now=SCAN0 + timedelta(seconds=60), rung_source=lambda _at, _cfg: "reduced",
    )
    card = next(c for c in view.active if c.id == card_id)
    assert card.state.value == "WATCH" and any(d.role == "shadow" and d.hollow for d in card.dots)
    assert 'data-key="pass"' in panel.render_ladder(view)
