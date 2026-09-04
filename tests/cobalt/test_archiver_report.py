"""Run-report writer tests: header-on-create, pure append after,
table stays contiguous (no interleaved non-table content), and every
row names the database it wrote to (RULING 9)."""

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
    assert "| full | cobalt_dev | 2 | 2 | 150 | 0 |" in lines[-1]


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
    assert "| cobalt_dev |" in data_lines[1]  # conftest pins COBALT_ENV=dev


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


def test_every_row_names_its_database(tmp_path, monkeypatch):
    """RULING 9: the archiver wrote production bars into `cobalt_dev`
    for three weeks and this log could not show it, because no column
    named a database. The name comes from the same resolver the store
    uses, so the log cannot disagree with where rows actually went."""
    path = make_report_path(tmp_path, monkeypatch)
    monkeypatch.setenv("COBALT_ENV", "production")
    s = RunSummary(mode="full")
    s.record_success("AAPL", 10)
    append_run_report(s)
    assert "| cobalt_brain |" in path.read_text()


def test_pre_ruling9_file_gets_one_schema_break_not_misaligned_rows(tmp_path, monkeypatch):
    """A markdown table cannot change its column count in place. An
    existing 7-column log gets a second table, once — never a silent
    append of 8-column rows under a 7-column header."""
    path = make_report_path(tmp_path, monkeypatch)
    path.write_text(
        "# Bar Archiver — Run Log\n\n"
        "| Date (UTC) | Mode | Tickers | Requests | Rows Written | Failures | Duration |\n"
        "|---|---|---|---|---|---|---|\n"
        "| 2026-09-04T00:30:05Z | full | 210 | 975 | 3165838 | 0 | 23m06s |\n"
    )
    for _ in range(2):
        s = RunSummary(mode="full")
        s.record_success("AAPL", 10)
        append_run_report(s)

    content = path.read_text()
    assert content.count("## Database column added") == 1
    assert content.count(report_module.COLUMNS) == 1
    # The pre-existing row is untouched — append-only, nothing rewritten.
    assert "| 2026-09-04T00:30:05Z | full | 210 | 975 | 3165838 | 0 | 23m06s |" in content
    assert content.count("| cobalt_dev |") == 2
