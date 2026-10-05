"""F15 P2 — `replay` and `corpus` on cobalt_dev (card 2026-10-04/02 rows
P2-1, P2-2, P2-3; FINAL `## CHUNKS` row P2's pass list).

Everything runs inside the suite's rolled-back `cobalt_dev` transaction
(`conftest.dev_db_tx`) on the real-shape `world` fixture
(`test_radar_cards_db.py:44-96`, L45): the S5 stage on the real stores
writes the cards, receipts and records, then `replay` and `corpus` read
them. `0021` (legs) and `0022` (records) are applied inside that
transaction only (L76). Every value is constructed (L32): ticker `ZZPB`
and the manual `TEST` card.
"""

from __future__ import annotations

import argparse
import os
from datetime import timedelta
from decimal import Decimal

import pytest

from legs_db_support import apply_0021, fill_kwargs, patch_daymode, sizing
from predictions_db_support import apply_0022, records_of
from test_radar_cards_db import ENABLED, SCAN0, world  # noqa: F401 — the with-DB fixture

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)
pytestmark = [requires_db, pytest.mark.integration]


def _settings():
    from cobalt.settings.card import CardSettings

    return CardSettings.from_rows(ENABLED)


def _enabled():
    from cobalt.aset.models import Grade

    return [Grade.A, Grade.B, Grade.C]


def _arm(world, card_id, at):
    from cobalt.aset.engine import size_at_key
    from cobalt.aset.models import Direction, Grade
    from cobalt.cards import Actor, CardState
    from cobalt.settings.models import TraderSettings

    cards = world["cards"]
    trader = TraderSettings.from_db(world["settings"])
    record = cards.radar_card(card_id)
    sized = size_at_key(
        Grade.A_PLUS, ticker=record["ticker"], entry=record["entry"], stop=record["stop"],
        direction=Direction(record["direction"]), sheet_modes=trader.sheet_modes, sheet="half",
        enabled=trader.daymode.enabled_grades_for("reduced"), max_stop_distance_pct=Decimal("10"),
    )
    cards.tap_key(card_id, sized, now=at)
    return cards.transition(card_id, CardState.ARMED, actor=Actor.YOU, now=at)


def _reads(world):
    from cobalt.cards.predictions import CardReads

    return CardReads(world["cards"])


def _tables(store):
    """`0021` (legs: the corpus calls `realized_r` on `legs_current_v`) and
    `0022` (records), inside the suite's rollback only (L76)."""
    apply_0021(store)
    apply_0022(store)


def _write(world, card_id, *, like, **over):
    """A record through THE writer, on a copy of `like` (a stored record)."""
    from cobalt.cards.predictions import write_record

    output = dict(like["output"])
    output.update(over.pop("output", {}))
    fields = dict(kind=like["kind"], at=like["at"], run_id=like["run_id"], scorer_version=like["scorer_version"],
                  formula_sha256=like["formula_sha256"], settings_sha256=like["settings_sha256"],
                  inputs=like["inputs"], output=output)
    fields.update(over)
    with world["cards"]._connect() as conn:
        conn.execute("SELECT id FROM aset_sizings WHERE id = %s FOR UPDATE", (card_id,))
        return write_record(conn, card_id=card_id, **fields)


def _set_row(world, card_id, output):
    """The card row's numbers set to a record's (the constructed walk only)."""
    with world["cards"]._connect() as conn:
        conn.execute("UPDATE aset_sizings SET card_score = %s WHERE id = %s", (output["card_score"], card_id))


# ---------------------------------------------------------------------
# P2-1 — the CHUNKS pass list
# ---------------------------------------------------------------------


def test_create_tap_refresh_fill_exit_closed_replays_match_and_exits_0(world, monkeypatch):
    from cobalt.aset.store import AsetStore
    from cobalt.cards import Actor, CardState, legs
    from cobalt.cards.predictions import render_replay, replay

    cards = world["cards"]
    _tables(cards)
    card_id = world["scan"](SCAN0).created[0]
    cards.tap_dot(card_id, "trail_fit", 8, settings=_settings(), enabled=_enabled(),
                  now=SCAN0 + timedelta(seconds=30))
    assert world["scan"](SCAN0 + timedelta(seconds=100)).refreshed == [card_id]
    _arm(world, card_id, SCAN0 + timedelta(seconds=110))
    cards.transition(card_id, CardState.TRIGGERED, actor=Actor.YOU, now=SCAN0 + timedelta(seconds=120))
    patch_daymode(monkeypatch)
    entry = cards.radar_card(card_id)["entry"]
    AsetStore("cobalt_dev").mark_filled(card_id, now=SCAN0 + timedelta(seconds=130),
                                        **fill_kwargs(price=str(entry), shares=40))
    exited = legs.record_exit(card_id, preset="flat", price=Decimal(entry) - Decimal("0.10"),
                              price_source="last_poll", price_asof=SCAN0 + timedelta(seconds=140),
                              flag="estimated", source="panel", running_before=40,
                              now=SCAN0 + timedelta(seconds=140))
    assert exited.closed and cards.state_of(card_id) is CardState.CLOSED

    report = replay(card_id, reads=_reads(world))
    assert [(r.seq, r.kind, r.verdict) for r in report.records] == [
        (1, "create", "MATCH"), (2, "tap", "MATCH"), (3, "refresh", "MATCH")], [r.diff for r in report.records]
    assert report.decision_seq == 3  # the last record before the ARM
    assert report.row.verdict == "MATCH" and report.row.record_seq == 3
    assert report.exit == 0
    assert report.outcome.state == "CLOSED" and report.outcome.outcome_status == "provisional"
    assert report.outcome.realized_provisional is True and report.outcome.realized_r is not None
    text = render_replay(report)
    assert text.splitlines()[0].startswith(f"card {card_id} ZZPB ")
    assert "← decision grade (last record before ARMED)" in text
    assert "ROW: matches record #3" in text and "provisional" in text


def test_a_tampered_output_is_a_diff_and_exits_1(world):
    from cobalt.cards.predictions import replay

    cards = world["cards"]
    _tables(cards)
    card_id = world["scan"](SCAN0).created[0]
    world["scan"](SCAN0 + timedelta(seconds=100))
    last = records_of(cards, card_id)[-1]
    _write(world, card_id, like=last, output={"proposed_key_reason": "tampered"})
    report = replay(card_id, reads=_reads(world))
    assert [r.verdict for r in report.records] == ["MATCH", "MATCH", "DIFF"]
    assert report.records[-1].diff == ["proposed_key_reason", "why"]
    assert report.exit == 1


def test_a_record_at_another_scorer_version_is_not_replayable_and_exits_2(world):
    from cobalt.cards.predictions import replay

    cards = world["cards"]
    _tables(cards)
    card_id = world["scan"](SCAN0).created[0]
    last = records_of(cards, card_id)[-1]
    _write(world, card_id, like=last, scorer_version="s0.9")
    report = replay(card_id, reads=_reads(world))
    assert [r.verdict for r in report.records] == ["MATCH", "NOT_REPLAYABLE"]
    assert report.records[-1].reason.startswith("recorded scorer s0.9, this code s")
    assert report.row.verdict == "MATCH" and report.exit == 2


def test_a_record_whose_run_has_no_receipt_is_not_replayable(world):
    from cobalt.cards.predictions import replay
    from cobalt.radar.evaluate import EvaluateError
    from test_radar_cards_db import POOL

    cards, radar = world["cards"], world["radar"]
    _tables(cards)
    card_id = world["scan"](SCAN0).created[0]
    original = cards.write_receipt

    def boom(row, **kw):
        raise RuntimeError("synthetic receipt failure")

    cards.write_receipt = boom
    with pytest.raises(EvaluateError):
        world["scan"](SCAN0 + timedelta(seconds=100))
    cards.write_receipt = original
    failed = radar.latest_run_id(POOL)
    report = replay(card_id, reads=_reads(world))
    assert [r.verdict for r in report.records] == ["MATCH", "NOT_REPLAYABLE"]
    assert report.records[-1].reason == f"run {failed} has no receipt: it failed after this card was written (L57)"
    assert report.exit == 2


def test_a_pre_f15_card_exits_2_with_the_audit_export_line(world, monkeypatch):
    from cobalt.cards import predictions
    from cobalt.cards.predictions import render_replay, replay

    cards = world["cards"]
    _tables(cards)
    with monkeypatch.context() as before_f15:  # the code before F15's hook wrote no record
        before_f15.setattr(predictions, "write_record", lambda conn, **kw: None)
        first = world["scan"](SCAN0)
    card_id = first.created[0]
    assert records_of(cards, card_id) == []
    with cards._connect() as conn:
        run_id = conn.execute(
            "SELECT r.run_id FROM aset_sizings s JOIN system.radar_score r ON r.id = s.radar_score_id "
            "WHERE s.id = %s", (card_id,),
        ).fetchone()[0]
    report = replay(card_id, reads=_reads(world))
    text = render_replay(report)
    assert "NO PREDICTION RECORDS — graded before F15 lands" in text
    assert f"cobalt radar audit-export --run {run_id}" in text and run_id == first.run_id
    assert report.exit == 2


def test_a_manual_card_exits_2(world, monkeypatch):
    from cobalt.aset.store import AsetStore
    from cobalt.cards.predictions import render_replay, replay

    _tables(world["cards"])
    patch_daymode(monkeypatch)
    card_id = AsetStore("cobalt_dev").save(sizing())
    report = replay(card_id, reads=_reads(world))
    assert "manual card: the key is the trader's; there is no derived grade" in render_replay(report)
    assert report.exit == 2


def test_arm_then_disarm_picks_the_record_before_the_arm(world):
    from cobalt.cards import Actor, CardState
    from cobalt.cards.predictions import replay

    cards = world["cards"]
    _tables(cards)
    card_id = world["scan"](SCAN0).created[0]
    cards.tap_dot(card_id, "trail_fit", 8, settings=_settings(), enabled=_enabled(),
                  now=SCAN0 + timedelta(seconds=30))
    world["scan"](SCAN0 + timedelta(seconds=100))
    _arm(world, card_id, SCAN0 + timedelta(seconds=110))
    cards.transition(card_id, CardState.WATCH, actor=Actor.YOU, reason="p2 disarm", now=SCAN0 + timedelta(seconds=140))
    world["scan"](SCAN0 + timedelta(seconds=200))
    cards.transition(card_id, CardState.EXPIRED, actor=Actor.COBALT, reason="p2 expiry",
                     now=SCAN0 + timedelta(seconds=300))
    report = replay(card_id, reads=_reads(world))
    assert [(r.seq, r.kind) for r in report.records] == [(1, "create"), (2, "tap"), (3, "refresh"), (4, "refresh")]
    assert report.decision_seq == 3
    assert report.outcome.outcome_status == "awaiting nightly replay" and report.outcome.missed is None


def test_row_against_the_last_record_by_seq_holds_numbers_no_record_stores(world):
    from cobalt.cards.predictions import render_replay, replay

    cards = world["cards"]
    _tables(cards)
    card_id = world["scan"](SCAN0).created[0]
    world["scan"](SCAN0 + timedelta(seconds=100))
    clean = replay(card_id, reads=_reads(world))
    assert clean.row.verdict == "MATCH" and clean.row.record_seq == 2 and clean.exit == 0
    _set_row(world, card_id, {"card_score": 99})
    report = replay(card_id, reads=_reads(world))
    assert report.row.verdict == "DIFF" and report.row.diff == ["card_score"] and report.row.record_seq == 2
    assert "ROW: holds numbers no record stores" in render_replay(report)
    assert report.exit == 1


def test_no_decision_grade_while_watch(world):
    from cobalt.cards.predictions import render_replay, replay

    cards = world["cards"]
    _tables(cards)
    card_id = world["scan"](SCAN0).created[0]
    report = replay(card_id, reads=_reads(world))
    assert report.decision_seq is None and report.outcome.decision_seq is None
    assert "decision grade: none — the card is still WATCH" in render_replay(report)
    assert report.outcome.outcome_status == "open"


# ---------------------------------------------------------------------
# P2-2 — `--json` through the command
# ---------------------------------------------------------------------


def test_the_json_command_prints_the_one_object(world, capsys):
    import json

    from cobalt.cards import cli

    cards = world["cards"]
    _tables(cards)
    card_id = world["scan"](SCAN0).created[0]
    cli.cmd_replay(argparse.Namespace(card_id=card_id, json=True))
    obj = json.loads(capsys.readouterr().out)
    assert list(obj) == ["card_id", "records", "row", "outcome", "exit"]
    assert obj["exit"] == 0 and obj["records"][0]["verdict"] == "MATCH"
    assert obj["records"][0]["recomputed"]["proposed_key_reason"] == obj["records"][0]["output"]["proposed_key_reason"]


# ---------------------------------------------------------------------
# P2-3 — the corpus on the real reads
# ---------------------------------------------------------------------


def test_the_corpus_lists_cards_with_records_status_first(world, capsys):
    from cobalt.cards import Actor, CardState, cli
    from cobalt.cards.predictions import corpus

    cards = world["cards"]
    _tables(cards)
    card_id = world["scan"](SCAN0).created[0]
    cards.transition(card_id, CardState.EXPIRED, actor=Actor.COBALT, reason="p2 expiry",
                     now=SCAN0 + timedelta(seconds=300))
    rows = [r for r in corpus(None, reads=_reads(world)) if r.card_id == card_id]
    assert len(rows) == 1 and rows[0].outcome_status == "awaiting nightly replay" and rows[0].records == 1
    assert rows[0].realized_r is None and rows[0].realized_r_reason == "not computed — no entry leg"
    cli.cmd_corpus(argparse.Namespace(since=None, json=False))
    out = capsys.readouterr().out.splitlines()
    assert out[0].startswith("corpus: n=")
    assert any(line.startswith(f"card {card_id} ") and "awaiting nightly replay" in line for line in out[1:])
    assert not any("missed: none" in line for line in out)
