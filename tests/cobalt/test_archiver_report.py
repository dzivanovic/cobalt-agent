"""Run-report writer tests: header-on-create, pure append after,
table stays contiguous (no interleaved non-table content)."""

from cobalt.archiver import report as report_module
from cobalt.archiver.report import RunSummary, append_run_report


def make_report_path(tmp_path, monkeypatch):
    path = tmp_path / "archiver-runs.md"
    monkeypatch.setattr(report_module, "REPORT_PATH", path)
    return path


def test_first_run_writes_header_then_one_row(tmp_path, monkeypatch):
    path = make_report_path(tmp_path, monkeypatch)
    summary = RunSummary(mode="full")
    summary.record_success("AAPL", 100)
    summary.record_success("MSFT", 50)

    append_run_report(summary)
    content = path.read_text()
    assert content.startswith("# Bar Archiver — Run Log")
    lines = [l for l in content.splitlines() if l.startswith("|")]
    # header row + separator row + 1 data row
    assert len(lines) == 3
    assert "| full | 2 | 2 | 150 | 0 |" in lines[-1]


def test_second_run_appends_without_rewriting_header(tmp_path, monkeypatch):
    path = make_report_path(tmp_path, monkeypatch)
    s1 = RunSummary(mode="full")
    s1.record_success("AAPL", 10)
    append_run_report(s1)

    s2 = RunSummary(mode="backfill:NVDA")
    s2.record_success("NVDA", 500)
    s2.record_failure("NVDA", "i30", "boom")
    append_run_report(s2)

    content = path.read_text()
    assert content.count("# Bar Archiver") == 1
    data_lines = [l for l in content.splitlines() if l.startswith("|") and "Date" not in l and "---" not in l]
    assert len(data_lines) == 2
    assert "backfill:NVDA" in data_lines[1]
    assert "| 1 |" in data_lines[1]  # failures count = 1


def test_table_stays_contiguous_across_failures(tmp_path, monkeypatch):
    # A run with failures must not insert non-table lines between rows —
    # that would break markdown table rendering for every run after it.
    path = make_report_path(tmp_path, monkeypatch)
    s1 = RunSummary(mode="full")
    s1.record_failure("XXX", "i1", "some very long error message")
    append_run_report(s1)
    s2 = RunSummary(mode="full")
    s2.record_success("AAPL", 10)
    append_run_report(s2)

    lines = path.read_text().splitlines()
    table_start = next(i for i, l in enumerate(lines) if l.startswith("|"))
    for line in lines[table_start:]:
        assert line.startswith("|"), f"non-table line breaks the table: {line!r}"
