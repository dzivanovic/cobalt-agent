"""`runner.run()` assembles the six checks in order into one report.
Every individual check is monkeypatched — this is an assembly test, not
a re-test of C1-C6's own logic (see `test_dayopen_checks.py`)."""

from datetime import date, datetime, timezone

from cobalt.dayopen import checks, runner
from cobalt.dayopen.config import DayOpenConfig
from cobalt.dayopen.models import CheckResult, Overall, Verdict

NOW = datetime(2026, 9, 14, 11, 5, tzinfo=timezone.utc)


def _stub(id_, verdict):
    return CheckResult(id_, f"title {id_}", verdict, f"detail {id_}", f"raw {id_}")


def test_run_calls_all_six_checks_in_order_and_rolls_up(monkeypatch):
    calls = []

    def _make(id_, verdict):
        def _fn(*args, **kwargs):
            calls.append(id_)
            return _stub(id_, verdict)
        return _fn

    monkeypatch.setattr(checks, "check_c1_radar_launchd", _make("C1", Verdict.PASS))
    monkeypatch.setattr(checks, "check_c2_radar_membership", _make("C2", Verdict.PASS))
    monkeypatch.setattr(checks, "check_c3_radar_beat_line", _make("C3", Verdict.PASS))
    monkeypatch.setattr(checks, "check_c4_session_blocks", _make("C4", Verdict.FAIL))
    monkeypatch.setattr(checks, "check_c5_archiver_last_run", _make("C5", Verdict.PASS))
    monkeypatch.setattr(checks, "check_c6_beats_since_prior_evening", _make("C6", Verdict.PASS))
    monkeypatch.setattr(runner, "load_dayopen_config", lambda: DayOpenConfig(8, 20))

    report = runner.run(report_date=date(2026, 9, 14), now=NOW)

    assert calls == ["C1", "C2", "C3", "C4", "C5", "C6"]
    assert [c.id for c in report.checks] == ["C1", "C2", "C3", "C4", "C5", "C6"]
    assert report.overall is Overall.AMBER  # one FAIL (C4), no ERROR
    assert report.report_date == date(2026, 9, 14)
    assert report.generated_at == NOW


def test_run_defaults_report_date_to_todays_et_date(monkeypatch):
    monkeypatch.setattr(checks, "check_c1_radar_launchd", lambda *a, **k: _stub("C1", Verdict.PASS))
    monkeypatch.setattr(checks, "check_c2_radar_membership", lambda *a, **k: _stub("C2", Verdict.PASS))
    monkeypatch.setattr(checks, "check_c3_radar_beat_line", lambda *a, **k: _stub("C3", Verdict.PASS))
    monkeypatch.setattr(checks, "check_c4_session_blocks", lambda *a, **k: _stub("C4", Verdict.PASS))
    monkeypatch.setattr(checks, "check_c5_archiver_last_run", lambda *a, **k: _stub("C5", Verdict.PASS))
    monkeypatch.setattr(checks, "check_c6_beats_since_prior_evening", lambda *a, **k: _stub("C6", Verdict.PASS))
    monkeypatch.setattr(runner, "load_dayopen_config", lambda: DayOpenConfig(8, 20))

    report = runner.run(now=NOW)  # 2026-09-14 11:05 UTC = 07:05 ET
    assert report.report_date == date(2026, 9, 14)
    assert report.overall is Overall.GREEN
