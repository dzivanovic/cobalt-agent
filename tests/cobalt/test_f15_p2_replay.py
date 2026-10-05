"""F15 P2 — `replay` and `corpus`, offline (card 2026-10-04/02 rows P2-1,
P2-2, P2-3; FINAL §5 `[F-08]` / `[F-33]` / `[F-35]` / `[F-44]`, §6 `[F-09]`,
R2-1 (c) B).

The reads are a constructed `FakeReads` (the same methods `CardReads`
answers from Postgres), so nothing here reaches a database. Every value is
constructed (L32): ticker `ZZRP`, ids in the 4xxx / 9xxx range.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from decimal import Decimal

import pytest

UTC = timezone.utc
AT = datetime(2026, 1, 6, 15, 0, tzinfo=UTC)
BANDS = {"a_plus_min": "0.9", "a_min": "0.8", "b_min": "0.6", "c_min": "0.4"}
SHA = "a" * 64


def _tap_inputs(grades=(8, 6), proximity="0.500000"):
    return {
        "tap_id": 9001,
        "dots": [{"factor": f"f{i}", "source": "human", "tier": "judgment", "na_reason": None,
                  "engine_grade": None, "trader_grade": g} for i, g in enumerate(grades)],
        "proximity": proximity, "score_suppressed_before": None, "bands": BANDS, "enabled": ["A", "B", "C"],
    }


def _tap_output(card_score=35, conviction="0.7", proposed_key="B"):
    return {
        "proximity": "0.500000", "conviction": conviction, "card_score": card_score, "score_suppressed": None,
        "proposed_key": proposed_key, "proposed_key_reason": None,
        "dots": [{"factor": "f0", "engine_value": None, "engine_grade": None, "na_reason": None, "trader_grade": 8},
                 {"factor": "f1", "engine_value": None, "engine_grade": None, "na_reason": None, "trader_grade": 6}],
    }


def _record(seq, *, kind="tap", transition_id=4001, output=None, inputs=None, run_id=None, version=None, why=None):
    from cobalt.cards.scoring import grade_why
    from cobalt.radar.evaluate import EVALUATOR_VERSION, formula_sha256

    output = output or _tap_output()
    return {
        "id": 9000 + seq, "card_id": 4242, "seq": seq, "transition_id": transition_id, "kind": kind,
        "at": AT, "scorer_id": "card_grade", "scorer_version": version or EVALUATOR_VERSION,
        "formula_sha256": formula_sha256(), "settings_sha256": SHA, "run_id": run_id,
        "inputs": inputs if inputs is not None else _tap_inputs(), "output": output,
        "why": why if why is not None else grade_why(output),
    }


def _card(**over):
    card = {"id": 4242, "ticker": "ZZRP", "direction": "long", "state": "WATCH", "origin": "radar",
            "radar_score_id": 7701, "conviction": Decimal("0.700000"), "proximity": Decimal("0.500000"),
            "card_score": 35, "score_suppressed": None, "proposed_key": "B"}
    card.update(over)
    return card


class FakeReads:
    """The `CardReads` methods, answered from constructed values."""

    def __init__(self, card, records=(), transitions=((4001, None, "WATCH"),), runs=None, chains=None,
                 legs=(), missed=(), pick=None, corpus_ids=None):
        self._card, self._records, self._transitions = card, list(records), list(transitions)
        self._runs, self._chains = runs or {}, chains or {}
        self._legs, self._missed, self._pick = list(legs), list(missed), pick
        self._corpus_ids = corpus_ids
        self.cards = {card["id"]: card} if card else {}

    def card(self, card_id):
        return self.cards.get(card_id)

    def records(self, card_id):
        return list(self._records)

    def transitions(self, card_id):
        return list(self._transitions)

    def score_run(self, radar_score_id):
        return self._runs.get(radar_score_id)

    def receipt_chain(self, run_id):
        return self._chains.get(run_id)

    def current_legs(self, card_id):
        return list(self._legs)

    def missed(self, card_id):
        return list(self._missed)

    def pick(self, card_id):
        return self._pick

    def corpus_card_ids(self, since):
        return list(self._corpus_ids if self._corpus_ids is not None else self.cards)


# ---------------------------------------------------------------------
# P2-1 — per record, decision grade, ROW, exit codes
# ---------------------------------------------------------------------


def test_a_tap_record_replays_from_its_own_inputs_match_exit_0():
    from cobalt.cards.predictions import replay

    report = replay(4242, reads=FakeReads(_card(), [_record(1)]))
    assert [r.verdict for r in report.records] == ["MATCH"]
    assert report.row.verdict == "MATCH" and report.row.record_seq == 1
    assert report.exit == 0


def test_a_tampered_output_is_a_diff_and_exits_1():
    from cobalt.cards.predictions import render_replay, replay

    tampered = _tap_output(card_score=36)
    report = replay(4242, reads=FakeReads(_card(card_score=36), [_record(1, output=tampered)]))
    rec = report.records[0]
    assert rec.verdict == "DIFF" and rec.diff == ["card_score", "why"]
    assert report.exit == 1
    assert "DIFF card_score recorded 36 → replayed 35" in render_replay(report)


def test_numbers_compare_as_decimal_values_never_as_strings():
    """X7: NUMERIC(8,6) reads back padded — `0.700000` is `0.7`."""
    from cobalt.cards.predictions import output_diff

    stored = _tap_output(conviction="0.700000")
    assert output_diff(stored, None, {**_tap_output(), "dots": stored["dots"]}) == []
    assert output_diff(stored, None, _tap_output(conviction="0.71")) == ["conviction"]


def test_an_engine_value_compares_at_its_columns_scale():
    """`card_dots.engine_value NUMERIC(18, 6)`: a refresh record's dots are
    re-read from it, so the full-precision recompute is compared at 6 dp —
    and a difference at that scale is still a DIFF."""
    from cobalt.cards.predictions import output_diff

    dot = {"factor": "rvol", "engine_grade": 7, "na_reason": None, "trader_grade": None}
    stored = {**_tap_output(), "dots": [{**dot, "engine_value": "5.240310"}]}
    full = {**_tap_output(), "dots": [{**dot, "engine_value": "5.240309641446676554619604065"}]}
    off = {**_tap_output(), "dots": [{**dot, "engine_value": "5.240311"}]}
    assert output_diff(stored, None, full) == []
    assert output_diff(stored, None, off) == ["dots"]


def test_another_scorer_version_is_not_replayable_and_exits_2():
    from cobalt.cards.predictions import render_replay, replay
    from cobalt.radar.evaluate import EVALUATOR_VERSION

    report = replay(4242, reads=FakeReads(_card(), [_record(1, version="s0.9")]))
    rec = report.records[0]
    assert rec.verdict == "NOT_REPLAYABLE" and rec.recomputed is None
    assert rec.reason == f"recorded scorer s0.9, this code {EVALUATOR_VERSION}; replay from the deploy that wrote it"
    assert report.exit == 2
    assert "#1 " in render_replay(report) and "NOT REPLAYABLE — recorded scorer s0.9" in render_replay(report)


def test_a_record_whose_run_has_no_receipt_is_not_replayable():
    from cobalt.cards.predictions import replay

    rec = _record(1, kind="refresh", run_id=4411, inputs={"taps_moved": False, "locked": None})
    report = replay(4242, reads=FakeReads(_card(), [rec], chains={}))
    assert report.records[0].verdict == "NOT_REPLAYABLE"
    assert report.records[0].reason == "run 4411 has no receipt: it failed after this card was written (L57)"
    assert report.exit == 2


def test_a_pre_f15_card_exits_2_with_the_audit_export_line_of_its_radar_score_run():
    from cobalt.cards.predictions import render_replay, replay

    report = replay(4242, reads=FakeReads(_card(radar_score_id=7701), [], runs={7701: 4411}))
    text = render_replay(report)
    assert "NO PREDICTION RECORDS — graded before F15 lands" in text
    assert "cobalt radar audit-export --run 4411" in text and "--run 7701" not in text
    assert report.exit == 2 and report.records == []


def test_a_manual_card_exits_2_with_its_line():
    from cobalt.cards.predictions import render_replay, replay

    report = replay(4242, reads=FakeReads(_card(origin="manual", radar_score_id=None), []))
    assert "manual card: the key is the trader's; there is no derived grade" in render_replay(report)
    assert report.exit == 2


def test_a_card_that_does_not_exist_is_refused_loud():
    from cobalt.cards.predictions import ReplayRefused, replay

    with pytest.raises(ReplayRefused, match="no card 4243"):
        replay(4243, reads=FakeReads(_card(), []))


def test_the_decision_grade_is_the_last_record_before_the_first_leave_from_watch():
    """R2-1 (c) B: arm then disarm — the record after the disarm is not it."""
    from cobalt.cards.predictions import decision_seq

    transitions = [(4001, None, "WATCH"), (4002, "WATCH", "ARMED"), (4003, "ARMED", "WATCH"),
                   (4004, "WATCH", "EXPIRED")]
    records = [{"seq": 1, "transition_id": 4001}, {"seq": 2, "transition_id": 4001},
               {"seq": 3, "transition_id": 4001}, {"seq": 4, "transition_id": 4003}]
    assert decision_seq(records, transitions) == 3


def test_no_decision_grade_while_the_card_is_watch():
    from cobalt.cards.predictions import decision_seq, render_replay, replay

    assert decision_seq([{"seq": 1, "transition_id": 4001}], [(4001, None, "WATCH")]) is None
    report = replay(4242, reads=FakeReads(_card(), [_record(1)]))
    assert report.decision_seq is None
    assert "decision grade: none — the card is still WATCH" in render_replay(report)


def test_the_decision_grade_is_marked_on_its_record():
    from cobalt.cards.predictions import render_replay, replay

    transitions = [(4001, None, "WATCH"), (4002, "WATCH", "ARMED")]
    records = [_record(1), _record(2, transition_id=4002)]
    report = replay(4242, reads=FakeReads(_card(state="ARMED"), records, transitions=transitions))
    assert report.decision_seq == 1
    line = next(line for line in render_replay(report).splitlines() if line.startswith("#1 "))
    assert "← decision grade (last record before ARMED)" in line


def test_row_holds_numbers_no_record_stores_exits_1():
    from cobalt.cards.predictions import render_replay, replay

    report = replay(4242, reads=FakeReads(_card(card_score=99), [_record(1)]))
    assert report.records[0].verdict == "MATCH"
    assert report.row.verdict == "DIFF" and report.row.diff == ["card_score"] and report.row.record_seq == 1
    assert "ROW: holds numbers no record stores" in render_replay(report)
    assert report.exit == 1


def test_row_is_compared_with_the_last_record_by_seq():
    from cobalt.cards.predictions import replay

    first = _record(1, output=_tap_output(card_score=40, conviction="0.8", proposed_key="A"),
                    inputs=_tap_inputs(grades=(8, 8)))
    report = replay(4242, reads=FakeReads(_card(), [_record(2), first]))  # out of order on purpose
    assert [r.seq for r in report.records] == [1, 2]
    assert report.row.record_seq == 2 and report.row.verdict == "MATCH"


# ---------------------------------------------------------------------
# the taps-moved refresh rebuild ([F-08], [F-44]) — a pure function
# ---------------------------------------------------------------------


def test_a_taps_moved_refresh_is_rebuilt_from_the_locked_numbers_and_the_preceding_trader_grades():
    from cobalt.cards.predictions import scan_recompute

    replayed = {"proximity": "0.5", "conviction": "0.6", "card_score": 30, "score_suppressed": None,
                "proposed_key": "B", "dots": [{"factor": "f0", "engine_value": "1.5", "engine_grade": 4,
                                               "na_reason": None, "trader_grade": None}]}
    preceding = {"dots": [{"factor": "f0", "engine_value": "1.5", "engine_grade": 4, "na_reason": None,
                           "trader_grade": 9}]}
    inputs = {"taps_moved": True, "locked": {"conviction": "0.9", "score_suppressed": None, "proposed_key": "A"}}
    got = scan_recompute(inputs, replayed=replayed, published=replayed, bands=None, enabled=[],
                         preceding_output=preceding)
    assert got["conviction"] == "0.9" and got["proposed_key"] == "A" and got["proposed_key_reason"] is None
    assert got["card_score"] == 45 and got["proximity"] == "0.5"
    assert got["dots"][0]["trader_grade"] == 9 and got["dots"][0]["engine_grade"] == 4


def test_a_taps_moved_refresh_with_null_proximity_keeps_the_published_sentence():
    from cobalt.cards.predictions import scan_recompute

    replayed = {"proximity": None, "conviction": "0.6", "card_score": None, "score_suppressed": "bars stale — x",
                "proposed_key": None, "dots": []}
    inputs = {"taps_moved": True, "locked": {"conviction": "0.9", "score_suppressed": "other", "proposed_key": "A"}}
    got = scan_recompute(inputs, replayed=replayed, published=replayed, bands=None, enabled=[],
                         preceding_output={"dots": []})
    assert got["score_suppressed"] == "bars stale — x" and got["card_score"] is None


def test_a_plain_scan_record_takes_the_receipt_recompute_and_the_receipt_settings_reason():
    from cobalt.aset.models import Grade
    from cobalt.cards.predictions import scan_recompute
    from cobalt.settings.card import ProposedKeyBands

    replayed = {"proximity": "0.5", "conviction": None, "card_score": None, "score_suppressed": None,
                "proposed_key": None, "dots": []}
    got = scan_recompute({"taps_moved": False, "locked": None}, replayed=replayed, published=replayed,
                         bands=ProposedKeyBands(**BANDS), enabled=[Grade.A], preceding_output=None)
    assert got == {**replayed, "proposed_key_reason": "no conviction — tap to propose"}


# ---------------------------------------------------------------------
# P2-2 — `--json`: the ONE object of [F-44]
# ---------------------------------------------------------------------


def test_json_is_the_one_object_of_f44():
    from cobalt.cards.predictions import replay

    tampered = _tap_output(card_score=36)
    obj = replay(4242, reads=FakeReads(_card(card_score=36), [_record(1, output=tampered)])).as_json()
    assert list(obj) == ["card_id", "records", "row", "outcome", "exit"]
    assert obj["card_id"] == 4242 and obj["exit"] == 1
    rec = obj["records"][0]
    assert list(rec) == ["seq", "id", "kind", "at", "run_id", "transition_id", "scorer_version", "formula_sha256",
                         "inputs", "output", "recomputed", "verdict", "reason", "diff"]
    assert rec["verdict"] == "DIFF" and rec["diff"] == ["card_score", "why"] and rec["reason"] is None
    assert rec["at"] == AT.isoformat() and rec["output"] == tampered
    assert rec["recomputed"]["card_score"] == 35 and rec["recomputed"]["conviction"] == "0.7"
    assert obj["row"] == {"verdict": "MATCH", "record_seq": 1, "diff": []}
    assert obj["outcome"]["card_id"] == 4242 and obj["outcome"]["outcome_status"] == "open"


def test_json_of_a_not_replayable_record_names_its_reason_and_no_recompute():
    from cobalt.cards.predictions import replay

    obj = replay(4242, reads=FakeReads(_card(), [_record(1, version="s0.9")])).as_json()
    rec = obj["records"][0]
    assert rec["verdict"] == "NOT_REPLAYABLE" and rec["recomputed"] is None and rec["diff"] == []
    assert rec["reason"].startswith("recorded scorer s0.9")


def test_json_of_a_card_with_no_records_has_no_row_verdict():
    from cobalt.cards.predictions import replay

    obj = replay(4242, reads=FakeReads(_card(), [], runs={7701: 4411})).as_json()
    assert obj["records"] == [] and obj["row"] == {"verdict": None, "record_seq": None, "diff": []}
    assert obj["exit"] == 2


# ---------------------------------------------------------------------
# P2-3 — corpus and its outcome status ([F-09])
# ---------------------------------------------------------------------

ENTRY = {"kind": "entry", "seq": 0, "price": Decimal("10.00"), "stop_in_force": Decimal("9.90"), "shares": 100,
         "flag": "confirmed"}


def test_a_closed_card_with_an_estimated_leg_is_provisional():
    from cobalt.cards.predictions import corpus

    exit_leg = {"kind": "exit", "seq": 1, "price": Decimal("10.20"), "shares": 100, "flag": "estimated"}
    reads = FakeReads(_card(state="CLOSED"), [_record(1)], legs=[ENTRY, exit_leg])
    (row,) = corpus(None, reads=reads)
    assert row.outcome_status == "provisional" and row.realized_provisional is True
    assert Decimal(row.realized_r) == Decimal("2") and row.realized_function == "realized_r.1"


def test_a_closed_card_with_confirmed_legs_is_final():
    from cobalt.cards.predictions import corpus

    exit_leg = {"kind": "exit", "seq": 1, "price": Decimal("10.20"), "shares": 100, "flag": "confirmed"}
    (row,) = corpus(None, reads=FakeReads(_card(state="CLOSED"), [_record(1)], legs=[ENTRY, exit_leg]))
    assert row.outcome_status == "final" and row.realized_provisional is False


def test_an_expired_card_with_no_missed_row_awaits_the_nightly_replay_never_missed_none():
    from cobalt.cards.predictions import corpus, render_corpus

    rows = corpus(None, reads=FakeReads(_card(state="EXPIRED"), [_record(1)]))
    assert rows[0].outcome_status == "awaiting nightly replay" and rows[0].missed is None
    text = render_corpus(rows)
    assert "missed: none" not in text and "awaiting nightly replay" in text


def test_an_expired_card_with_its_current_missed_row_is_final():
    from cobalt.cards.predictions import corpus

    missed = [{"cf_r": Decimal("1.2500"), "mfe_r": Decimal("2.0000"), "excluded_by": "window"}]
    (row,) = corpus(None, reads=FakeReads(_card(state="EXPIRED"), [_record(1)], missed=missed))
    assert row.outcome_status == "final"
    assert row.missed == {"cf_r": "1.2500", "mfe_r": "2.0000", "excluded_by": "window"}


def test_two_current_missed_rows_for_one_card_are_refused_loud():
    from cobalt.cards.predictions import ReplayRefused, corpus

    missed = [{"cf_r": None, "mfe_r": None, "excluded_by": "window"}] * 2
    with pytest.raises(ReplayRefused, match="2 current"):
        corpus(None, reads=FakeReads(_card(state="EXPIRED"), [_record(1)], missed=missed))


def test_the_corpus_row_carries_the_decision_and_final_records_and_the_count():
    from cobalt.cards.predictions import corpus

    transitions = [(4001, None, "WATCH"), (4002, "WATCH", "ARMED")]
    records = [_record(1), _record(2), _record(3, transition_id=4002)]
    (row,) = corpus(None, reads=FakeReads(_card(state="ARMED"), records, transitions=transitions,
                                          pick={"id": 5, "pool_rank": 2}))
    assert (row.records, row.decision_seq, row.final_seq) == (3, 2, 3)
    assert row.outcome_status == "open" and row.pick == {"id": 5, "pool_rank": 2}


def test_the_n_per_status_line_is_printed_before_the_first_row():
    from cobalt.cards.predictions import CorpusRow, render_corpus

    def row(card_id, status):
        return CorpusRow(card_id=card_id, ticker="ZZRP", direction="long", origin="radar", state="WATCH",
                         records=1, decision_seq=None, final_seq=1, realized_r=None,
                         realized_r_reason="not computed — no entry leg", realized_provisional=False,
                         realized_function="realized_r.1", missed=None, pick=None, outcome_status=status)

    lines = render_corpus([row(1, "open"), row(2, "awaiting nightly replay")]).splitlines()
    assert lines[0] == "corpus: n=2 · open 1 · provisional 0 · final 0 · awaiting nightly replay 1"
    assert lines[1].startswith("card 1 ")


def test_replay_outcome_line_is_the_corpus_row_of_its_card():
    from cobalt.cards.predictions import render_replay, replay

    report = replay(4242, reads=FakeReads(_card(state="EXPIRED"), [_record(1)],
                                          transitions=[(4001, None, "WATCH"), (4002, "WATCH", "EXPIRED")]))
    assert report.outcome.outcome_status == "awaiting nightly replay"
    outcome = next(line for line in render_replay(report).splitlines() if line.startswith("OUTCOME: "))
    assert "awaiting nightly replay" in outcome and "missed: none" not in outcome


# ---------------------------------------------------------------------
# the CLI surface
# ---------------------------------------------------------------------


def test_the_cards_family_mounts_replay_and_corpus():
    from cobalt.cards import cli

    parser = argparse.ArgumentParser()
    cli.add_parser(parser.add_subparsers(dest="group"))
    args = parser.parse_args(["cards", "replay", "4242", "--json"])
    assert (args.card_id, args.json, args.func) == (4242, True, cli.cmd_replay)
    args = parser.parse_args(["cards", "corpus", "--since", "2026-01-06", "--json"])
    assert (args.since, args.json, args.func) == ("2026-01-06", True, cli.cmd_corpus)


def test_the_replay_command_exits_with_the_reports_code(monkeypatch, capsys):
    from cobalt.cards import cli, predictions

    reads = FakeReads(_card(card_score=99), [_record(1)])
    monkeypatch.setattr(predictions, "CardReads", lambda *a, **k: reads)
    with pytest.raises(SystemExit) as stop:
        cli.cmd_replay(argparse.Namespace(card_id=4242, json=False))
    assert stop.value.code == 1
    assert "ROW: holds numbers no record stores" in capsys.readouterr().out
