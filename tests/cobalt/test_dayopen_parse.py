"""Pure parsers over the real `logs/heartbeat.log`, `logs/heartbeat.err`
and `docs/30 - Design/archiver-runs.md` shapes (L45): every fixture in
`tests/fixtures/dayopen/*.excerpt` is a verbatim slice of the real
production files, not an invented shape.
"""

from datetime import datetime
from pathlib import Path

from cobalt.dayopen.parse import (
    ET,
    all_beat_headers,
    failed_lines,
    last_markdown_table_row,
    newest_beat_header,
    newest_radar_probe_line,
)

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures" / "dayopen"


def _lines(name: str) -> list[str]:
    return (FIXTURES / name).read_text().splitlines()


def test_newest_radar_probe_line_is_the_last_one_in_the_file():
    lines = _lines("heartbeat.log.excerpt")
    line = newest_radar_probe_line(lines)
    assert line is not None
    assert line.state == "RED"
    assert line.is_red
    assert "last_scan_at stale" in line.detail


def test_newest_radar_probe_line_can_be_ok():
    # Truncate before the file's final (RED) beat, landing on the
    # 11:23:43 beat's "OK   radar   scanning (rth), members 50" line.
    lines = _lines("heartbeat.log.excerpt")[:200]
    line = newest_radar_probe_line(lines)
    assert line is not None
    assert line.state == "OK"
    assert not line.is_red
    assert "scanning (rth)" in line.detail


def test_no_radar_line_returns_none():
    assert newest_radar_probe_line(["nothing here"]) is None


def test_newest_beat_header():
    lines = _lines("heartbeat.log.excerpt")
    header = newest_beat_header(lines)
    assert header is not None
    assert header.state == "RED"
    assert header.at == datetime(2026, 9, 14, 11, 38, 48, tzinfo=ET)


def test_all_beat_headers_in_file_order():
    lines = _lines("heartbeat.log.excerpt")
    headers = all_beat_headers(lines)
    assert [h.at.strftime("%H:%M:%S") for h in headers] == [
        "10:53:33", "11:08:38", "11:23:43", "11:38:48",
    ]
    assert [h.state for h in headers] == ["RED", "RED", "RED", "RED"]


def test_failed_lines_finds_the_real_wrapper_failure_not_the_red_beat_line():
    lines = _lines("heartbeat.err.excerpt")
    found = failed_lines(lines)
    assert len(found) == 1
    ts, line = found[0]
    assert ts == datetime(2026, 9, 12, 11, 16, 16, tzinfo=ET)
    assert "vault unit FAILED" in line
    # The RED beat's own line ("heartbeat: RED — 1 job(s) and vault
    # write") is also ERROR-level in this excerpt and must NOT match —
    # it does not contain the literal substring "FAILED".
    assert not any("RED — 1 job(s)" in line for _ts, line in found)


def test_last_markdown_table_row_picks_the_second_table():
    text = (FIXTURES / "archiver-runs.md.excerpt").read_text()
    parsed = last_markdown_table_row(text)
    assert parsed is not None
    header, row = parsed
    assert header == [
        "Date (UTC)", "Mode", "Database", "Tickers", "Requests",
        "Rows Written", "Failures", "Duration",
    ]
    assert row == ["2026-09-12T00:30:05Z", "full", "cobalt_brain", "210", "975", "3160954", "0", "23m18s"]


def test_last_markdown_table_row_none_without_a_table():
    assert last_markdown_table_row("no tables here") is None
