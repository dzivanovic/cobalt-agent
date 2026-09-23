"""DRC D1 — the stripped real-shape fixtures (D1-0) and the ONE header
classifier (D1-2a, R114 / R17 (5)).

Every fixture here is E1's SHAPE with constructed values (L45 / L32,
R103's consent): the header line is E1's byte for byte, every value is
ours. Nothing in this file types a column name of his export — a test
that needs a header takes it from a fixture's first line or from the
parser module's REQUIRED constant.
"""

from __future__ import annotations

import csv
import io
from pathlib import Path

FIXTURES = Path(__file__).resolve().parent.parent / "fixtures" / "drc"

TRADING_LOG_E1 = FIXTURES / "trading_log_e1.csv"
STATS_LOG_E1 = FIXTURES / "stats_log_e1.csv"
CARRY_DAY1 = FIXTURES / "trading_log_carry_day1.csv"
CARRY_SEED = FIXTURES / "trading_log_carry_seed.csv"

ALL_FIXTURES = (TRADING_LOG_E1, STATS_LOG_E1, CARRY_DAY1, CARRY_SEED)


def _first_line(path: Path) -> bytes:
    return path.read_bytes().split(b"\n", 1)[0]


# ---------------------------------------------------------------------
# D1-0 — the fixtures keep E1's shape
# ---------------------------------------------------------------------


def test_every_fixture_exists_and_the_readme_says_what_was_constructed():
    for path in ALL_FIXTURES:
        assert path.exists(), path
    readme = (FIXTURES / "README.md").read_text()
    for word in ("stripped", "constructed", "trading_log_carry_day1.csv", "playbook"):
        assert word in readme, word


def test_every_fixture_has_lf_line_endings_a_final_newline_and_no_bom():
    """E1: LF only, no CR, a final newline, no BOM — on both files."""
    for path in ALL_FIXTURES:
        data = path.read_bytes()
        assert b"\r" not in data, path.name
        assert data.endswith(b"\n"), path.name
        assert not data.startswith(b"\xef\xbb\xbf"), path.name


def test_the_three_trading_log_fixtures_share_one_header_byte_for_byte():
    """The carry pair is CONSTRUCTED (E1 has no overnight position) in
    E1's exact header — the same bytes as the cut of E1 itself."""
    header = _first_line(TRADING_LOG_E1)
    assert _first_line(CARRY_DAY1) == header
    assert _first_line(CARRY_SEED) == header


def test_the_trading_log_header_and_every_row_end_with_the_delimiter():
    """E1's trading-log header ends with `,` (an empty eleventh cell) and
    so does every data row."""
    for path in (TRADING_LOG_E1, CARRY_DAY1, CARRY_SEED):
        for line in path.read_text().splitlines():
            assert line.endswith(","), (path.name, line)


def test_the_stats_log_header_has_no_trailing_delimiter_and_49_names():
    header = _first_line(STATS_LOG_E1).decode()
    assert not header.endswith(",")
    assert len(header.split(",")) == 49


def test_the_trading_log_cut_keeps_e1s_row_count_and_newest_first_order():
    lines = TRADING_LOG_E1.read_text().splitlines()[1:]
    assert len(lines) == 14
    times = [line.split(",", 1)[0] for line in lines]
    assert times == sorted(times, reverse=True), "E1 is newest-first"


def test_the_stats_cut_keeps_four_rows_and_one_quoted_two_name_playbook_cell():
    rows = list(csv.reader(io.StringIO(STATS_LOG_E1.read_text())))[1:]
    assert len(rows) == 4
    assert all(len(row) == 49 for row in rows)
    multi = [cell for row in rows for cell in row if ", " in cell]
    assert len(multi) == 1, "E1: exactly one cell carries two names"
    assert f'"{multi[0]}"' in STATS_LOG_E1.read_text(), "E1 quotes that cell"
