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


# ---------------------------------------------------------------------
# D1-2a — the ONE header classifier (R114, R17 (5))
# ---------------------------------------------------------------------

from datetime import date  # noqa: E402

import pytest  # noqa: E402

from cobalt.drc import detect, stats_log, trading_log  # noqa: E402
from cobalt.drc.models import Kind, Outcome  # noqa: E402


def _header_names(path: Path) -> list[str]:
    return next(csv.reader([_first_line(path).decode()]))


def _with_header(path: Path, names: list[str]) -> bytes:
    """The fixture's bytes with its first line replaced — the header is
    rebuilt from the fixture's OWN names, never retyped (L31)."""
    rest = path.read_bytes().split(b"\n", 1)[1]
    return ",".join(names).encode() + b"\n" + rest


def test_each_kind_owns_its_required_set_and_detect_copies_neither():
    """ONE constant per kind, owned by its parser module (L3)."""
    assert detect.TRADING_REQUIRED is trading_log.REQUIRED
    assert detect.STATS_REQUIRED is stats_log.REQUIRED
    assert len(trading_log.REQUIRED) == 10
    assert len(stats_log.REQUIRED) == 48


def test_the_required_sets_are_e1s_names_minus_the_one_vendor_named_column():
    assert list(trading_log.REQUIRED) == [n for n in _header_names(TRADING_LOG_E1) if n]
    names = _header_names(STATS_LOG_E1)
    left_out = [n for n in names if n not in stats_log.REQUIRED]
    assert len(left_out) == 1 and left_out[0] == names[-1]
    assert list(stats_log.REQUIRED) == names[:-1]


def test_the_shared_set_is_computed_from_the_two_constants():
    assert detect.SHARED == frozenset(trading_log.REQUIRED) & frozenset(stats_log.REQUIRED)
    assert detect.SHARED == frozenset({"Symbol", "Side"})


@pytest.mark.parametrize("name", ["his file.md", "his file.csv", "his file", "x.txt"])
@pytest.mark.parametrize(
    "path,kind",
    [
        (TRADING_LOG_E1, Kind.TRADING_LOG),
        (CARRY_DAY1, Kind.TRADING_LOG),
        (CARRY_SEED, Kind.TRADING_LOG),
        (STATS_LOG_E1, Kind.STATS_LOG),
    ],
)
def test_the_name_and_extension_are_never_read(path, kind, name):
    d = detect.detect_kind(name, path.read_bytes())
    assert d.kind is kind and d.outcome is Outcome.PARSED
    assert d.name == name


def test_a_file_named_like_the_other_kind_is_still_detected_by_its_header():
    d = detect.detect_kind("stats_log_e1.csv", TRADING_LOG_E1.read_bytes())
    assert d.kind is Kind.TRADING_LOG


def test_the_trading_log_header_is_complete_with_no_extras():
    d = detect.detect_kind("t", TRADING_LOG_E1.read_bytes())
    assert d.extras == [] and d.missing == [] and d.degraded is None


def test_the_stats_logs_vendor_column_is_an_extra_and_raises_the_shape_flag():
    """The literal D1-2a rule: every name outside the required set is an
    extra → `stats_log_shape`, loud. On E1 that is the vendor-named
    column (ASK DESK in the report)."""
    d = detect.detect_kind("s", STATS_LOG_E1.read_bytes())
    assert d.extras == [_header_names(STATS_LOG_E1)[-1]]
    assert d.degraded == "stats_log_shape"


def test_a_bom_and_a_crlf_ending_do_not_change_the_kind():
    data = b"\xef\xbb\xbf" + TRADING_LOG_E1.read_bytes().replace(b"\n", b"\r\n")
    d = detect.detect_kind("t", data)
    assert d.kind is Kind.TRADING_LOG and d.outcome is Outcome.PARSED


@pytest.mark.parametrize(
    "data,why",
    [
        (b"# DRC notes\n\nsome text he wrote\n", "header matches neither kind"),
        (b"just a line of text\n", "header matches neither kind"),
        (b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00", "not text"),
        (b"\xff\xd8\xff\xe0\x00\x10JFIF\x00", "not text"),
        (b"", "header matches neither kind"),
    ],
)
def test_a_note_a_text_file_or_an_image_is_ignored_and_listed(data, why):
    d = detect.detect_kind("thing", data)
    assert d.kind is None and d.outcome is Outcome.IGNORED
    assert why in d.reason and "thing" in d.reason


@pytest.mark.parametrize("path,kind", [(TRADING_LOG_E1, Kind.TRADING_LOG), (STATS_LOG_E1, Kind.STATS_LOG)])
def test_one_required_name_removed_is_partial_of_its_kind_naming_it(path, kind):
    names = _header_names(path)
    required = trading_log.REQUIRED if kind is Kind.TRADING_LOG else stats_log.REQUIRED
    victim = [n for n in required if n not in detect.SHARED][2]
    d = detect.detect_kind("p", _with_header(path, [n for n in names if n != victim]))
    assert d.kind is kind and d.outcome is Outcome.PARTIAL
    assert d.missing == [victim]
    assert d.partial_flag == f"PARTIAL — missing: {victim}"


def test_partial_missing_names_come_in_the_kinds_column_order():
    names = _header_names(TRADING_LOG_E1)
    drop = {trading_log.QTY, trading_log.TIME, trading_log.ACCOUNT}
    d = detect.detect_kind("p", _with_header(TRADING_LOG_E1, [n for n in names if n not in drop]))
    assert d.missing == [trading_log.TIME, trading_log.QTY, trading_log.ACCOUNT]


def test_a_header_of_only_the_shared_names_is_ignored():
    d = detect.detect_kind("x", b"Symbol,Side\nAAA,B\n")
    assert d.outcome is Outcome.IGNORED and "neither" in d.reason


def test_unique_names_of_both_kinds_fail_the_file():
    t = [n for n in trading_log.REQUIRED if n not in detect.SHARED][:2]
    s = [n for n in stats_log.REQUIRED if n not in detect.SHARED][:2]
    d = detect.detect_kind("mix", ",".join(t + s).encode() + b"\n")
    assert d.outcome is Outcome.FAILED and "header matches both kinds" in d.reason


def test_every_name_of_both_kinds_fails_the_file():
    names = list(trading_log.REQUIRED) + [n for n in stats_log.REQUIRED if n not in detect.SHARED]
    d = detect.detect_kind("both", ",".join(names).encode() + b"\n")
    assert d.outcome is Outcome.FAILED and "header matches both kinds" in d.reason


def test_an_added_name_keeps_the_kind_and_raises_the_shape_flag():
    names = _header_names(TRADING_LOG_E1)
    d = detect.detect_kind("t", _with_header(TRADING_LOG_E1, names[:-1] + ["New Column", ""]))
    assert d.kind is Kind.TRADING_LOG and d.outcome is Outcome.PARSED
    assert d.extras == ["New Column"] and d.degraded == "trading_log_shape"


def test_a_reordered_header_is_not_a_failure():
    names = [n for n in _header_names(TRADING_LOG_E1) if n]
    d = detect.detect_kind("t", ",".join(reversed(names)).encode() + b"\n")
    assert d.kind is Kind.TRADING_LOG and d.outcome is Outcome.PARSED


def test_a_duplicated_required_name_fails_the_file():
    names = _header_names(TRADING_LOG_E1)
    d = detect.detect_kind("dup", _with_header(TRADING_LOG_E1, [names[0]] + names))
    assert d.outcome is Outcome.FAILED and "duplicate" in d.reason


# --- sets -------------------------------------------------------------


def _drop(path: Path) -> bytes:
    """`path`'s bytes with one unique required name removed → partial."""
    names = _header_names(path)
    required = trading_log.REQUIRED if path != STATS_LOG_E1 else stats_log.REQUIRED
    victim = [n for n in required if n not in detect.SHARED][0]
    return _with_header(path, [n for n in names if n != victim])


def test_a_set_of_one_file_per_kind_passes_and_lists_the_ignored():
    s = detect.detect_set([
        ("a.md", TRADING_LOG_E1.read_bytes()),
        ("b.md", STATS_LOG_E1.read_bytes()),
        ("note.md", b"# my notes\n"),
        ("shot.png", b"\x89PNG\r\n\x1a\n\x00"),
    ])
    assert s.status == "pass", s.reason
    assert s.by_kind[Kind.TRADING_LOG].name == "a.md"
    assert s.by_kind[Kind.STATS_LOG].name == "b.md"
    assert [d.name for d in s.ignored] == ["note.md", "shot.png"]


def test_two_trading_logs_in_one_set_fail_naming_both_and_picking_neither():
    s = detect.detect_set([
        ("one.md", TRADING_LOG_E1.read_bytes()),
        ("two.csv", CARRY_DAY1.read_bytes()),
        ("b.md", STATS_LOG_E1.read_bytes()),
    ])
    assert s.status == "failed"
    assert s.reason == "FAILED: trading_log ambiguous — one.md, two.csv"
    assert Kind.TRADING_LOG not in s.by_kind


def test_a_partial_and_a_complete_file_of_one_kind_are_ambiguous():
    s = detect.detect_set([
        ("whole.md", STATS_LOG_E1.read_bytes()),
        ("half.md", _drop(STATS_LOG_E1)),
        ("t.md", TRADING_LOG_E1.read_bytes()),
    ])
    assert s.status == "failed"
    assert s.reason == "FAILED: stats_log ambiguous — whole.md, half.md"


def test_a_partial_file_passes_the_set_and_is_listed():
    s = detect.detect_set([("t.md", _drop(TRADING_LOG_E1)), ("s.md", STATS_LOG_E1.read_bytes())])
    assert s.status == "pass"
    assert [d.name for d in s.partial] == ["t.md"]
    assert s.by_kind[Kind.TRADING_LOG].outcome is Outcome.PARTIAL


def test_a_set_missing_a_kind_is_incomplete_not_passed():
    s = detect.detect_set([("t.md", TRADING_LOG_E1.read_bytes())])
    assert s.status == "incomplete" and "stats_log" in s.reason


def test_a_set_with_a_both_kinds_file_lists_it_failed():
    t = [n for n in trading_log.REQUIRED if n not in detect.SHARED][:1]
    s_ = [n for n in stats_log.REQUIRED if n not in detect.SHARED][:1]
    s = detect.detect_set([
        ("t.md", TRADING_LOG_E1.read_bytes()),
        ("s.md", STATS_LOG_E1.read_bytes()),
        ("mix.md", ",".join(t + s_).encode() + b"\n"),
    ])
    assert [d.name for d in s.failed] == ["mix.md"]


# --- the _imports/drc/ tree -------------------------------------------


@pytest.mark.parametrize("folder", ["_reference", "2026-9-18", "20260918", "2026-09-18x", "notes"])
def test_only_a_yyyy_mm_dd_folder_is_an_import_folder(folder):
    assert detect.import_folder_date(folder) is None


def test_a_date_folder_names_its_import_date():
    assert detect.import_folder_date("2026-09-18") == date(2026, 9, 18)


def test_a_reference_folder_beside_a_date_folder_is_never_read(tmp_path):
    (tmp_path / "2001-01-02").mkdir()
    (tmp_path / "_reference").mkdir()
    (tmp_path / "_reference" / "trap.md").write_bytes(TRADING_LOG_E1.read_bytes())
    assert [p.name for p in detect.import_folders(tmp_path)] == ["2001-01-02"]
