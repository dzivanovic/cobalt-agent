"""`cobalt day-open` argparse wiring: the bare command takes `--date`/
`--json` directly, and `verdict` is an optional subcommand alongside
them — both must resolve to the right `func` without one another's
flags/positionals leaking across."""

import argparse
from datetime import date

import pytest

from cobalt.dayopen import cli as dayopen_cli


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="cobalt")
    sub = parser.add_subparsers(dest="group", required=True)
    dayopen_cli.add_parser(sub)
    return parser


def test_bare_command_defaults_date_to_none_and_dispatches_run():
    args = _parser().parse_args(["day-open"])
    assert args.func is dayopen_cli.cmd_run
    assert args.date is None
    assert args.json is False


def test_date_and_json_flags_parse():
    args = _parser().parse_args(["day-open", "--date", "2026-09-14", "--json"])
    assert args.date == date(2026, 9, 14)
    assert args.json is True


def test_bad_date_is_refused():
    with pytest.raises(SystemExit):
        _parser().parse_args(["day-open", "--date", "not-a-date"])


def test_verdict_subcommand_dispatches_and_carries_the_line():
    args = _parser().parse_args(["day-open", "verdict", "GREEN, ship it"])
    assert args.func is dayopen_cli.cmd_verdict
    assert args.line == "GREEN, ship it"


def test_cmd_run_writes_report_and_prints_verdict_table(monkeypatch, tmp_path, capsys):
    from datetime import datetime, timezone

    from cobalt.dayopen.models import CheckResult, DayOpenReport, Overall, Verdict

    stub_report = DayOpenReport(
        report_date=date(2026, 9, 14),
        generated_at=datetime(2026, 9, 14, 11, 5, tzinfo=timezone.utc),
        checks=[CheckResult("C1", "radar launchd", Verdict.PASS, "PASS", "raw")],
        overall=Overall.GREEN,
    )
    monkeypatch.setattr(dayopen_cli.runner, "run", lambda **kwargs: stub_report)

    def _fake_write(report, **kwargs):
        path = tmp_path / f"day-open-{report.report_date:%Y-%m-%d}.md"
        path.write_text("stub")
        return path

    monkeypatch.setattr(dayopen_cli, "write_report", _fake_write)

    args = _parser().parse_args(["day-open"])
    args.func(args)
    out = capsys.readouterr().out
    assert "day-open-2026-09-14.md" in out
    assert "OVERALL: GREEN" in out


def test_json_alone_writes_nothing_to_disk(monkeypatch, capsys):
    # 2026-09-15: `cobalt day-open --json` in the deploy smoke rewrote the
    # day's report. `--json` prints; it never writes.
    from datetime import datetime, timezone

    from cobalt.dayopen.models import CheckResult, DayOpenReport, Overall, Verdict

    stub_report = DayOpenReport(
        report_date=date(2026, 9, 14),
        generated_at=datetime(2026, 9, 14, 11, 5, tzinfo=timezone.utc),
        checks=[CheckResult("C1", "radar launchd", Verdict.PASS, "PASS", "raw")],
        overall=Overall.GREEN,
    )
    monkeypatch.setattr(dayopen_cli.runner, "run", lambda **kwargs: stub_report)

    def _no_write(*args, **kwargs):
        raise AssertionError("--json must not write a report")

    monkeypatch.setattr(dayopen_cli, "write_report", _no_write)
    args = _parser().parse_args(["day-open", "--json"])
    args.func(args)
    assert '"overall"' in capsys.readouterr().out


def test_cmd_verdict_reports_failure_on_missing_report(monkeypatch, capsys):
    from cobalt.dayopen.report import ReportPathError

    def _raise(*args, **kwargs):
        raise ReportPathError("no report at ...")

    monkeypatch.setattr(dayopen_cli, "append_verdict", _raise)
    args = _parser().parse_args(["day-open", "verdict", "line"])
    with pytest.raises(SystemExit):
        args.func(args)
    assert "FAILED" in capsys.readouterr().err
