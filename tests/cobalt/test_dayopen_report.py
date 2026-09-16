import json
from datetime import date, datetime, timezone

import pytest

from cobalt.dayopen.models import CheckResult, DayOpenReport, Overall, Verdict
from cobalt.dayopen.report import (
    ReportPathError,
    append_verdict,
    render_json,
    render_markdown,
    report_path,
    write_report,
)


def _report(overall=Overall.GREEN) -> DayOpenReport:
    return DayOpenReport(
        report_date=date(2026, 9, 14),
        generated_at=datetime(2026, 9, 14, 11, 5, tzinfo=timezone.utc),
        checks=[
            CheckResult("C1", "radar launchd", Verdict.PASS, "PASS — state=running", "state = running"),
            CheckResult("C4", "session_blocks", Verdict.FAIL, "FAIL — count=3, expected 8", "count\t3"),
        ],
        overall=overall,
    )


def test_report_path_is_under_reports_dir(tmp_path):
    path = report_path(date(2026, 9, 14), reports_dir=tmp_path)
    assert path == tmp_path / "day-open-2026-09-14.md"


def test_render_markdown_has_one_fenced_block_per_check_and_a_verdict_table():
    text = render_markdown(_report(Overall.AMBER))
    assert "## C1 radar launchd" in text
    assert "```\nstate = running\n```" in text
    assert "## C4 session_blocks" in text
    assert "| C1 | radar launchd | PASS |" in text
    assert "| C4 | session_blocks | FAIL |" in text
    assert "OVERALL: AMBER" in text


def test_render_json_round_trips_the_shape():
    data = json.loads(render_json(_report(Overall.RED)))
    assert data["report_date"] == "2026-09-14"
    assert data["overall"] == "RED"
    assert data["checks"][0]["id"] == "C1"
    assert data["checks"][1]["verdict"] == "FAIL"


def test_write_report_creates_the_file_and_returns_its_path(tmp_path):
    path = write_report(_report(), reports_dir=tmp_path)
    assert path == tmp_path / "day-open-2026-09-14.md"
    assert path.exists()
    assert "OVERALL: GREEN" in path.read_text()


def test_a_second_run_never_replaces_the_days_report(tmp_path):
    # 2026-09-15 20:3x: the deploy smoke's run REWROTE the seat's 08:18
    # report (8.7 KB, with its SEAT VERDICT) with its own output. The dated
    # file is never replaced; a later run lands beside it, stamped HHMMSS ET.
    first = write_report(_report(Overall.GREEN), reports_dir=tmp_path)
    append_verdict(date(2026, 9, 14), "GREEN, ship it", reports_dir=tmp_path)
    before = first.read_text()
    second = write_report(_report(Overall.RED), reports_dir=tmp_path)
    assert first.read_text() == before
    assert second == tmp_path / "day-open-2026-09-14-070500.md"
    assert "OVERALL: RED" in second.read_text()


def test_a_colliding_timestamped_report_is_refused_not_replaced(tmp_path):
    write_report(_report(Overall.GREEN), reports_dir=tmp_path)
    stamped = write_report(_report(Overall.GREEN), reports_dir=tmp_path)
    stamped_text = stamped.read_text()
    with pytest.raises(ReportPathError):
        write_report(_report(Overall.RED), reports_dir=tmp_path)
    assert stamped.read_text() == stamped_text


def test_append_verdict_appends_to_an_existing_report(tmp_path):
    write_report(_report(), reports_dir=tmp_path)
    path = append_verdict(date(2026, 9, 14), "GREEN, ship it", reports_dir=tmp_path)
    text = path.read_text()
    assert text.rstrip().endswith("SEAT VERDICT: GREEN, ship it")


def test_append_verdict_refuses_when_report_missing(tmp_path):
    with pytest.raises(ReportPathError):
        append_verdict(date(2026, 9, 14), "line", reports_dir=tmp_path)


def test_writer_refuses_any_path_outside_reports(tmp_path):
    """L3/defensive: `_assert_under_reports_dir` refuses a path whose
    parent is not the reports directory itself — never a subfolder, a
    sibling, or the reports dir's own parent."""
    from cobalt.dayopen.report import _assert_under_reports_dir

    with pytest.raises(ReportPathError):
        _assert_under_reports_dir(tmp_path / "subdir" / "day-open-2026-09-14.md", reports_dir=tmp_path)
    with pytest.raises(ReportPathError):
        _assert_under_reports_dir(tmp_path.parent / "day-open-2026-09-14.md", reports_dir=tmp_path)
    # Sanity: a path directly under reports_dir is accepted (no raise).
    _assert_under_reports_dir(tmp_path / "day-open-2026-09-14.md", reports_dir=tmp_path)
