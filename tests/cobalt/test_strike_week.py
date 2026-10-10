"""S4-P2 S6 (offline): `cobalt strike week` — the F9 week report, read-only.

A fake row source: seam rows and their `strike_alerts` records, every lag
hand-computed below. Percentiles are P1's nearest rank
(`strike.measure.percentile`). Constructed values only (L32).
"""

from __future__ import annotations

from datetime import date, datetime, timedelta, timezone
from decimal import Decimal

UTC = timezone.utc
CLOSE = datetime(2001, 1, 2, 15, 0, tzinfo=UTC)  # 10:00 ET, 2001-01-02
START, END = date(2001, 1, 1), date(2001, 1, 5)


def _row(tid, *, policy="close_through", seen_s=3, via="strike.detector", to_state="TRIGGERED", actor="cobalt",
         close=CLOSE):
    from cobalt.aset.strike import SeamRow

    evidence = {"via": via, "policy": policy, "entry": "5.10", "bar_close_at": close.isoformat(),
                "seen_at": (close + timedelta(seconds=seen_s)).isoformat()}
    return SeamRow(transition_id=tid, card_id=tid, to_state=to_state, actor=actor,
                   at=close + timedelta(seconds=seen_s), evidence=evidence, ticker="ZZWK", direction="long",
                   sized_grade="B", shares=100, stop=Decimal("4.90"), sheet_mode="half")


def _record(shown_s=None, *, close=CLOSE, dm=None):
    return {"seam_at": close, "pushed_at": None,
            "shown_at": None if shown_s is None else close + timedelta(seconds=shown_s),
            "dm_at": None if dm is None else close + timedelta(seconds=12), "dm_result": dm}


def _report(rows, records, criterion=5):
    from cobalt.strike.week import week_report

    return week_report(rows, records, criterion_s=criterion, start=START, end=END)


def test_three_triggers_one_7_s_late_is_not_met_1_of_3():
    rows = [_row(1), _row(2), _row(3), _row(4, via="strike.missed", to_state="MISSED"),
            _row(5, via="panel.triggered", actor="you")]
    lines = _report(rows, {1: _record(2), 2: _record(3), 3: _record(7)})
    text = "\n".join(lines)
    assert "2001-01-02 · TRIGGERED 3 · MISSED 1" in text
    assert "DETECT lag s (close-based, seen_at − bar_close_at): n 3 · p50 3.0 · p95 3.0 · max 3.0" in text
    assert "PANEL lag s (close-based, shown_at − bar_close_at): n 3 · p50 3.0 · p95 7.0 · max 7.0" in text
    assert lines[-1] == "NOT MET — 1 of 3 over 5 s"


def test_every_trigger_within_the_criterion_is_met():
    lines = _report([_row(1), _row(2), _row(3)], {1: _record(2), 2: _record(3), 3: _record(5)})
    assert lines[-1] == "F9 CRITERION MET 3/3 ≤ 5 s"


def test_a_trigger_never_acked_is_never_shown_not_in_panel_lag_and_counts_against_the_criterion():
    lines = _report([_row(1), _row(2)], {1: _record(2), 2: _record(None, dm="DM sent — post x to @y")})
    text = "\n".join(lines)
    assert "PANEL lag s (close-based, shown_at − bar_close_at): n 1 · p50 2.0 · p95 2.0 · max 2.0" in text
    assert "never shown 1" in text
    assert "DMs 1 (DM sent — post x to @y ×1)" in text
    assert lines[-1] == "NOT MET — 1 of 2 over 5 s"


def test_intrabar_rows_are_reported_apart_against_seen_at():
    lines = _report([_row(1, policy="intrabar", seen_s=-20), _row(2)], {1: _record(-17), 2: _record(4)})
    text = "\n".join(lines)
    assert "PANEL lag s (close-based, shown_at − bar_close_at): n 1 · p50 4.0 · p95 4.0 · max 4.0" in text
    assert "intrabar PANEL lag s (shown_at − seen_at): n 1 · p50 3.0 · p95 3.0 · max 3.0" in text
    assert lines[-1] == "F9 CRITERION MET 2/2 ≤ 5 s"


def test_no_trigger_in_range_is_not_a_pass():
    assert _report([], {})[-1] == "NOT MET — no TRIGGERED in range"


def test_the_unrecorded_p1_counts_are_said_not_invented():
    text = "\n".join(_report([_row(1)], {1: _record(2)}))
    assert "unwatchable / capped: not recorded in the database" in text


def test_the_default_range_is_monday_through_today():
    from cobalt.strike.week import default_range

    assert default_range(date(2001, 1, 4)) == (date(2001, 1, 1), date(2001, 1, 4))
    assert default_range(date(2001, 1, 1)) == (date(2001, 1, 1), date(2001, 1, 1))


def test_the_verb_is_registered(monkeypatch):
    import sys

    from cobalt import cli
    from cobalt.strike import week

    seen = []
    monkeypatch.setattr(week, "command", lambda args: seen.append(args))
    monkeypatch.setattr(sys, "argv", ["cobalt", "strike", "week", "--from", "2001-01-01", "--to", "2001-01-05"])
    cli.main()
    assert seen and seen[0].start == START and seen[0].end == END


def test_the_command_reads_and_writes_nothing(monkeypatch, capsys):
    from cobalt.strike import week

    class Source:
        def seam_rows_between(self, start, end):
            assert (start, end) == (START, END)
            return [_row(1)]

        def records_for(self, ids):
            assert ids == [1]
            return {1: _record(2)}

    monkeypatch.setattr(week, "_source", lambda: Source())
    monkeypatch.setattr(week, "_criterion_s", lambda: 5)

    class Args:
        start, end = START, END

    week.command(Args())
    assert capsys.readouterr().out.strip().splitlines()[-1] == "F9 CRITERION MET 1/1 ≤ 5 s"
