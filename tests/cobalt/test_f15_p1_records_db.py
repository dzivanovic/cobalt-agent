"""F15 P1 — the prediction records on cobalt_dev (card 61 rows M1 X8, W1,
H1, H2, H3; FINAL §3 `[F-32]`, `[F-33]`, `[F-40]`, R2-1 (c), R2-2 B).

Everything runs inside the suite's rolled-back `cobalt_dev` transaction
(`conftest.dev_db_tx`) with `0022` applied there by `apply_0022` (L76):
these tests hold at `0013` and at `0022` alike and commit nothing. The
worlds are the real-shape ones (L45): `test_radar_cards_db.world` (the S5
stage on the real stores) and `stale_db_support.DevWorld` (bars fed by the
test). Every value is constructed (L32): tickers `ZZPB`, `ZZF15B`,
`ZZF15X`, `ZZF15N`.
"""

from __future__ import annotations

import os
from datetime import timedelta
from decimal import Decimal

import psycopg
import pytest

import stale_db_support as sds
from predictions_db_support import (
    apply_0022,
    assert_output_is_the_row,
    card_numbers,
    insert_raw_record,
    record_count,
    records_of,
    rollback_0022,
    transition_ids,
)
from test_radar_cards_db import ENABLED, SCAN0, world  # noqa: F401 — the with-DB fixture

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)
pytestmark = [requires_db, pytest.mark.integration]

OUTPUT = {"proximity": "0.5", "conviction": None, "card_score": None, "score_suppressed": None,
          "proposed_key": None, "proposed_key_reason": "no conviction — tap to propose", "dots": []}


def _settings():
    from cobalt.settings.card import CardSettings

    return CardSettings.from_rows(ENABLED)


def _enabled():
    from cobalt.aset.models import Grade

    return [Grade.A, Grade.B, Grade.C]


def _arm(world, card_id, at):
    """Size the card at a key (the tap route's store half), then ARM it."""
    from cobalt.aset.engine import size_at_key
    from cobalt.aset.models import Direction, Grade
    from cobalt.cards import Actor, CardState
    from cobalt.settings.models import TraderSettings

    cards = world["cards"]
    trader = TraderSettings.from_db(world["settings"])
    record = cards.radar_card(card_id)
    sizing = size_at_key(
        Grade.A_PLUS, ticker=record["ticker"], entry=record["entry"], stop=record["stop"],
        direction=Direction(record["direction"]), sheet_modes=trader.sheet_modes, sheet="half",
        enabled=trader.daymode.enabled_grades_for("reduced"), max_stop_distance_pct=Decimal("10"),
    )
    cards.tap_key(card_id, sizing, now=at)
    return cards.transition(card_id, CardState.ARMED, actor=Actor.YOU, now=at)


# ---------------------------------------------------------------------
# M1 — X8: the 0022 DDL on one constructed radar card (R2-2 B)
# ---------------------------------------------------------------------


def test_x8_the_0022_ddl_refuses_every_edit_and_its_rollback_leaves_nothing(world):
    cards = world["cards"]
    apply_0022(cards)
    first = world["scan"](SCAN0)
    card_id = first.created[0]

    def refused(conn, sql, params, error, match=None):
        conn.execute("SAVEPOINT x8_probe")
        with pytest.raises(error, match=match):
            conn.execute(sql, params)
        conn.execute("ROLLBACK TO SAVEPOINT x8_probe")

    with cards._connect() as conn:
        rid = insert_raw_record(conn, card_id, seq=900, run_id=first.run_id)
        immutable = r"user\.prediction_records is immutable"
        refused(conn, "UPDATE prediction_records SET why = 'edited' WHERE id = %s", (rid,),
                psycopg.errors.RaiseException, immutable)
        refused(conn, "DELETE FROM prediction_records WHERE id = %s", (rid,), psycopg.errors.RaiseException, immutable)
        refused(conn, "DELETE FROM aset_sizings WHERE id = %s", (card_id,), psycopg.errors.ForeignKeyViolation)
        conn.execute("SAVEPOINT x8_probe")
        with pytest.raises(psycopg.errors.UniqueViolation):
            insert_raw_record(conn, card_id, seq=900, run_id=first.run_id)
        conn.execute("ROLLBACK TO SAVEPOINT x8_probe")
        conn.execute("SAVEPOINT x8_probe")
        with pytest.raises(psycopg.errors.CheckViolation):
            insert_raw_record(conn, card_id, seq=901, kind="tap", run_id=first.run_id)
        conn.execute("ROLLBACK TO SAVEPOINT x8_probe")
        conn.execute("SAVEPOINT x8_probe")
        with pytest.raises(psycopg.errors.CheckViolation):
            insert_raw_record(conn, card_id, seq=902, kind="refresh", run_id=None)
        conn.execute("ROLLBACK TO SAVEPOINT x8_probe")
    rollback_0022(cards)
    with cards._connect() as conn:
        assert conn.execute("SELECT to_regclass('\"user\".prediction_records')").fetchone()[0] is None
        assert conn.execute(
            "SELECT count(*) FROM pg_catalog.pg_attribute WHERE attrelid = '\"user\".aset_sizings'::regclass "
            "AND attname = 'last_price_bar_ts' AND NOT attisdropped"
        ).fetchone()[0] == 0


# ---------------------------------------------------------------------
# W1 — the one writer: seq and transition_id under the caller's lock
# ---------------------------------------------------------------------


class _Spy:
    """The caller's connection, counting any commit / rollback the writer issues."""

    def __init__(self, conn):
        self.conn, self.ended = conn, []

    def execute(self, *args, **kwargs):
        return self.conn.execute(*args, **kwargs)

    def cursor(self, *args, **kwargs):
        return self.conn.cursor(*args, **kwargs)

    def commit(self):
        self.ended.append("commit")

    def rollback(self):
        self.ended.append("rollback")


def test_write_record_takes_seq_and_transition_id_under_the_callers_lock(world, dev_db_tx, monkeypatch):
    from cobalt.aset.store import AsetStore
    from cobalt.cards.predictions import write_record
    from legs_db_support import patch_daymode, sizing

    cards = world["cards"]
    apply_0022(cards)
    run_id = world["scan"](SCAN0).run_id
    patch_daymode(monkeypatch)
    card_id = AsetStore("cobalt_dev").save(sizing())  # a card with no record yet: its genesis row only
    with cards._connect() as conn:
        spy = _Spy(conn)
        conn.execute("SELECT id FROM aset_sizings WHERE id = %s FOR UPDATE", (card_id,))
        for _ in range(2):
            write_record(spy, card_id=card_id, kind="refresh", at=SCAN0, run_id=run_id, scorer_version="s2p2.3",
                         formula_sha256="a" * 64, settings_sha256="b" * 64, inputs={"taps_moved": False,
                                                                                    "locked": None}, output=OUTPUT)
        assert spy.ended == [], "the writer never commits or rolls back the caller's transaction"
        assert dev_db_tx.info.transaction_status is psycopg.pq.TransactionStatus.INTRANS
    rows = records_of(cards, card_id)
    genesis = transition_ids(cards, card_id)[-1][0]
    assert [r["seq"] for r in rows] == [1, 2]
    assert [r["transition_id"] for r in rows] == [genesis, genesis]
    assert rows[0]["why"] and rows[0]["scorer_id"] == "card_grade"


# ---------------------------------------------------------------------
# H1 — the create hook
# ---------------------------------------------------------------------


def test_a_create_writes_one_record_seq_1_on_the_genesis_transition(world):
    from cobalt.cards.radar import RadarCardSpec

    cards = world["cards"]
    apply_0022(cards)
    first = world["scan"](SCAN0)
    card_id = first.created[0]
    rows = records_of(cards, card_id)
    assert len(rows) == 1
    rec = rows[0]
    genesis = transition_ids(cards, card_id)
    assert genesis[0][1] is None and len(genesis) == 1
    assert (rec["seq"], rec["kind"], rec["run_id"], rec["transition_id"]) == (1, "create", first.run_id, genesis[0][0])
    assert rec["inputs"] == {"taps_moved": False, "locked": None}
    assert rec["scorer_version"] == "s2p2.3" and rec["run_id"] is not None
    assert_output_is_the_row(rec["output"], card_numbers(cards, card_id))
    assert rec["output"]["proposed_key_reason"] == "no conviction — tap to propose"
    assert rec["why"]

    with cards._connect() as conn:
        row = conn.execute(
            "SELECT pool_member_id, trade_def_slug, direction, trade_def_md5, radar_score_id FROM aset_sizings "
            "WHERE id = %s", (card_id,),
        ).fetchone()
    spec = dict(
        ticker="ZZPB", direction=row[2], session="RTH", pool_member_id=row[0], trade_def_slug=row[1],
        trade_def_md5=row[3], setup_ref="overextension", trigger_type="bar_break", trigger_price=Decimal("5.50"),
        stop_ref="snapback_candle", structural_stop=Decimal("5.81"), formed_at=SCAN0 - timedelta(minutes=5),
        expires_at=SCAN0 + timedelta(hours=1), why="retry", radar_score_id=row[4], scan_id=1,
        formula_sha256="a" * 64, tunables_sha256="b" * 64, settings_sha256="c" * 64, proximity=Decimal("0.5"),
        dots=[], evidence={"run_id": first.run_id},
    )
    before = record_count(cards)
    assert cards.create_radar_card(RadarCardSpec(**spec), proposed_key_reason=None, now=SCAN0) is None  # a retry
    assert record_count(cards) == before, "a retried create writes no second record"

    def boom():
        raise RuntimeError("synthetic before_commit failure")

    other = RadarCardSpec(**{**spec, "trade_def_slug": "f15-other-def"})
    with pytest.raises(RuntimeError, match="synthetic"):
        cards.create_radar_card(other, proposed_key_reason=None, now=SCAN0, before_commit=boom)
    assert record_count(cards) == before
    with cards._connect() as conn:
        assert conn.execute("SELECT count(*) FROM aset_sizings WHERE trade_def_slug = 'f15-other-def'").fetchone()[0] == 0


# ---------------------------------------------------------------------
# H2 — the refresh hook, `run_id=` and `last_price_bar_ts`
# ---------------------------------------------------------------------


def test_a_second_scan_writes_a_refresh_record_seq_2_with_the_numbers_the_update_wrote(world):
    cards = world["cards"]
    apply_0022(cards)
    card_id = world["scan"](SCAN0).created[0]
    second = world["scan"](SCAN0 + timedelta(seconds=100))
    assert second.refreshed == [card_id]
    rows = records_of(cards, card_id)
    assert [(r["seq"], r["kind"]) for r in rows] == [(1, "create"), (2, "refresh")]
    rec = rows[-1]
    assert rec["run_id"] == second.run_id
    assert rec["inputs"] == {"taps_moved": False, "locked": None}
    assert_output_is_the_row(rec["output"], card_numbers(cards, card_id))
    assert len(rec["output"]["dots"]) == len(rows[0]["output"]["dots"])
    with cards._connect() as conn:
        run = conn.execute("SELECT evaluator_version, formula_sha256, settings_sha256 FROM system.radar_score_run "
                           "WHERE id = %s", (second.run_id,)).fetchone()
    assert (rec["scorer_version"], rec["formula_sha256"], rec["settings_sha256"]) == tuple(run)


def _dev_world(ticker, pool):
    world = sds.DevWorld(ticker=ticker, pool=pool)
    apply_0022(world.cards)
    return world


def test_last_price_bar_ts_is_the_evaluations_bar_start_in_both_arms_and_null_keeps_it():
    world = _dev_world("ZZF15B", "f15_bar_ts")
    card_id = sds.scored_pre_c1_card(world)
    run_id = world.radar.latest_run_id("f15_bar_ts")
    later = sds.SCAN0 + timedelta(minutes=10)
    world.feed(later)
    update = sds.update_for(world, card_id, later, sds.bars_before(later))
    assert update.last_price_bar_ts is not None
    assert world.cards.refresh_radar_card(update, run_id=run_id, now=later + timedelta(seconds=2)) is True
    assert card_numbers(world.cards, card_id)["last_price_bar_ts"] == update.last_price_bar_ts
    later2 = later + timedelta(minutes=5)
    world.feed(later2)
    update2 = sds.update_for(world, card_id, later2, sds.bars_before(later2))
    world.tap(card_id, "trail_fit", 3, later2 + timedelta(seconds=1))
    assert world.cards.refresh_radar_card(update2, run_id=run_id, now=later2 + timedelta(seconds=2)) is False
    assert update2.last_price_bar_ts not in (None, update.last_price_bar_ts)
    assert card_numbers(world.cards, card_id)["last_price_bar_ts"] == update2.last_price_bar_ts  # the taps-moved arm
    kept = update2.model_copy(update={"last_price_bar_ts": None, "last_price": None})
    world.cards.refresh_radar_card(kept, run_id=run_id, now=later2 + timedelta(seconds=3))
    assert card_numbers(world.cards, card_id)["last_price_bar_ts"] == update2.last_price_bar_ts  # NULL keeps it
    with pytest.raises(TypeError):
        world.cards.refresh_radar_card(update2, now=later2 + timedelta(seconds=4))
    with pytest.raises(Exception, match="run_id"):
        world.cards.refresh_radar_card(update2, run_id=None, now=later2 + timedelta(seconds=4))


def test_x6a_a_tap_between_the_stage_read_and_the_refresh_records_the_locked_triple():
    world = _dev_world("ZZF15X", "f15_x6a")
    card_id = sds.scored_pre_c1_card(world)
    run_id = world.radar.latest_run_id("f15_x6a")
    later = sds.SCAN0 + timedelta(minutes=10)
    world.feed(later)
    update = sds.update_for(world, card_id, later, sds.bars_before(later))  # the stage reads the card
    world.tap(card_id, "trail_fit", 3, later + timedelta(seconds=1))  # a tap lands before the write
    locked = card_numbers(world.cards, card_id)  # what the refresh's lock SELECT reads
    assert world.cards.refresh_radar_card(update, run_id=run_id, now=later + timedelta(seconds=2)) is False
    rec = records_of(world.cards, card_id)[-1]
    assert rec["kind"] == "refresh" and rec["inputs"]["taps_moved"] is True
    got = rec["inputs"]["locked"]
    assert set(got) == {"conviction", "score_suppressed", "proposed_key"}
    assert Decimal(got["conviction"]) == locked["conviction"]
    assert got["score_suppressed"] == locked["score_suppressed"] and got["proposed_key"] == locked["proposed_key"]
    row = card_numbers(world.cards, card_id)
    assert_output_is_the_row(rec["output"], row)
    assert rec["output"]["card_score"] == row["card_score"] and rec["output"]["proposed_key_reason"] is None


def test_x6c_a_receipt_failure_after_the_card_writes_leaves_every_record_and_no_receipt(world):
    from cobalt.radar.evaluate import EvaluateError
    from test_radar_cards_db import POOL

    cards, radar = world["cards"], world["radar"]
    apply_0022(cards)
    card_id = world["scan"](SCAN0).created[0]
    original = cards.write_receipt

    def boom(row, **kw):
        raise RuntimeError("synthetic receipt failure")

    cards.write_receipt = boom
    with pytest.raises(EvaluateError):
        world["scan"](SCAN0 + timedelta(seconds=100))
    cards.write_receipt = original
    failed_run = radar.latest_run_id(POOL)
    rows = records_of(cards, card_id)
    assert [(r["seq"], r["kind"]) for r in rows] == [(1, "create"), (2, "refresh")]
    assert rows[-1]["run_id"] == failed_run and cards.receipt_for_run(failed_run) is None
    assert_output_is_the_row(rows[-1]["output"], card_numbers(cards, card_id))


# ---------------------------------------------------------------------
# H3 — the tap hook, with `settings`
# ---------------------------------------------------------------------


def test_a_tap_writes_a_self_contained_tap_record(world):
    cards = world["cards"]
    apply_0022(cards)
    card_id = world["scan"](SCAN0).created[0]
    settings = _settings()
    result = cards.tap_dot(card_id, "trail_fit", 8, settings=settings, enabled=_enabled(),
                           now=SCAN0 + timedelta(seconds=30))
    rows = records_of(cards, card_id)
    rec = rows[-1]
    assert (rec["seq"], rec["kind"], rec["run_id"]) == (2, "tap", None)
    assert set(rec["inputs"]) == {"tap_id", "dots", "proximity", "score_suppressed_before", "bands", "enabled"}
    assert rec["settings_sha256"] == settings.sha256()
    assert rec["inputs"]["bands"] == settings.proposed_key.model_dump(mode="json")
    assert rec["inputs"]["enabled"] == ["A", "B", "C"]
    with cards._connect() as conn:
        tap_id = conn.execute("SELECT max(id) FROM card_dot_taps WHERE card_id = %s", (card_id,)).fetchone()[0]
    assert rec["inputs"]["tap_id"] == tap_id
    assert {"factor": "trail_fit", "trader_grade": 8}.items() <= next(
        d for d in rec["inputs"]["dots"] if d["factor"] == "trail_fit").items()
    assert_output_is_the_row(rec["output"], card_numbers(cards, card_id))
    assert rec["output"]["proposed_key_reason"] == result["proposed_key_reason"]
    for missing in ({"settings": None}, {"enabled": None}):
        kwargs = {"settings": settings, "enabled": _enabled(), **missing}
        with pytest.raises(Exception, match="settings|enabled"):
            cards.tap_dot(card_id, "trail_fit", 7, **kwargs)
    assert len(records_of(cards, card_id)) == len(rows)


def test_a_tap_on_a_terminal_card_is_refused_and_writes_no_record(world):
    from cobalt.cards import Actor, CardState, CardStateError

    cards = world["cards"]
    apply_0022(cards)
    card_id = world["scan"](SCAN0).created[0]
    cards.transition(card_id, CardState.EXPIRED, actor=Actor.COBALT, reason="f15 terminal",
                     now=SCAN0 + timedelta(seconds=30))
    before = len(records_of(cards, card_id))
    with pytest.raises(CardStateError, match="terminal"):
        cards.tap_dot(card_id, "trail_fit", 8, settings=_settings(), enabled=_enabled(),
                      now=SCAN0 + timedelta(seconds=40))
    assert len(records_of(cards, card_id)) == before


def test_a_tap_while_proximity_is_null_keeps_the_sentence_and_its_record_says_so():
    world = _dev_world("ZZF15N", "f15_null_prox")
    card_id = sds.scored_pre_c1_card(world)
    stale_at = sds.stale_as_of(sds.bars_before(sds.SCAN0))
    world.scan(stale_at)
    before = card_numbers(world.cards, card_id)
    assert before["proximity"] is None and before["score_suppressed"].startswith("bars stale — ")
    world.tap(card_id, "trail_fit", 9, stale_at + timedelta(seconds=5))
    rec = records_of(world.cards, card_id)[-1]
    assert rec["kind"] == "tap"
    assert rec["inputs"]["proximity"] is None
    assert rec["inputs"]["score_suppressed_before"] == before["score_suppressed"]
    assert rec["output"]["score_suppressed"] == before["score_suppressed"] and rec["output"]["card_score"] is None
    assert_output_is_the_row(rec["output"], card_numbers(world.cards, card_id))


def test_after_an_arm_a_tap_records_the_arm_rows_transition_id(world):
    cards = world["cards"]
    apply_0022(cards)
    card_id = world["scan"](SCAN0).created[0]
    arm_id = _arm(world, card_id, SCAN0 + timedelta(seconds=20))
    cards.tap_dot(card_id, "trail_fit", 8, settings=_settings(), enabled=_enabled(),
                  now=SCAN0 + timedelta(seconds=30))
    rec = records_of(cards, card_id)[-1]
    assert rec["kind"] == "tap" and rec["transition_id"] == arm_id
    assert transition_ids(cards, card_id)[-1] == (arm_id, "WATCH", "ARMED")
