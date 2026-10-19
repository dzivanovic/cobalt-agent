"""F21 chunk 1, offline (card 2026-10-13 468, rows G1, G2, G3, G5): the placement,
the chunker, the loud import failures and the CLI mount.

No database. Every file is a committed synthetic fixture
(`tests/cobalt/fixtures/genesis/`) or one written into `tmp_path` (L28, L32).
`cobalt.genesis` is imported inside each test, so a missing module fails each
test on its own rather than the collection.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

from cobalt.db import Side

FIXTURES = Path(__file__).parent / "fixtures" / "genesis"


# ---------------------------------------------------------------------
# G1 — the table's side
# ---------------------------------------------------------------------


def test_genesis_chunk_is_declared_on_the_user_side():
    from cobalt.db_migrations.placement import CREATED_TABLES, side_of

    assert side_of("genesis_chunk") is Side.USER
    assert CREATED_TABLES["genesis_chunk"] is Side.USER


# ---------------------------------------------------------------------
# G2 — chunks follow markdown structure, never a size number
# ---------------------------------------------------------------------


def test_chunks_follow_markdown_structure_with_line_ranges():
    """A heading, two paragraphs, a 3-item list and a table of a header row and
    two rows: 8 chunks. The heading rides on its section's first chunk; the
    table's separator line is no chunk."""
    from cobalt.genesis.chunk import chunk_markdown

    chunks = chunk_markdown((FIXTURES / "structure.md").read_text(encoding="utf-8"))
    assert [(c.seq, c.line_start, c.line_end, c.body) for c in chunks] == [
        (1, 1, 4, "# Drill notes\nThe first paragraph names the drill\nand runs onto a second line."),
        (2, 6, 6, "The second paragraph closes the section."),
        (3, 8, 8, "- item one of the list"),
        (4, 9, 10, "- item two of the list\n  continues on an indented line"),
        (5, 11, 11, "- item three of the list"),
        (6, 13, 13, "| column | value |"),
        (7, 15, 15, "| alpha | 1 |"),
        (8, 16, 16, "| beta | 2 |"),
    ]


def test_a_lone_heading_is_kept_and_a_fence_is_one_chunk():
    """A heading with nothing under it before the next heading is its own chunk
    (its text is never dropped); a fenced block is one chunk, blank lines and all."""
    from cobalt.genesis.chunk import chunk_markdown

    text = "# One\n\n## Two\n\n```\nfirst\n\nsecond\n```\n\n---\n\ntail\n"
    chunks = chunk_markdown(text)
    assert [(c.line_start, c.line_end, c.body) for c in chunks] == [
        (1, 1, "# One"),
        (3, 9, "## Two\n```\nfirst\n\nsecond\n```"),
        (13, 13, "tail"),
    ]


def test_a_source_carries_the_path_as_given_and_the_files_sha256(tmp_path):
    import hashlib

    from cobalt.genesis.chunk import read_source

    path = tmp_path / "notes.md"
    path.write_bytes((FIXTURES / "structure.md").read_bytes())
    source = read_source(str(path))
    assert source.source == str(path)
    assert source.sha256 == hashlib.sha256(path.read_bytes()).hexdigest()
    assert len(source.chunks) == 8


# ---------------------------------------------------------------------
# G3 — every bad input is loud, and nothing is written for any source
# ---------------------------------------------------------------------


class _RecordingStore:
    def __init__(self):
        self.calls: list = []

    def replace(self, source):
        self.calls.append(source)
        return len(source.chunks)


def _bad(kind: str, tmp_path: Path) -> Path:
    path = tmp_path / f"{kind}.md"
    if kind == "missing":
        return path
    if kind == "directory":
        path.mkdir()
        return path
    if kind == "unreadable":
        path.write_text("a paragraph\n", encoding="utf-8")
        path.chmod(0)
        return path
    if kind == "not_utf8":
        path.write_bytes(b"a paragraph \xff\xfe\n")
        return path
    if kind == "empty":
        path.write_bytes(b"")
        return path
    if kind == "no_chunks":
        path.write_text("\n\n---\n\n", encoding="utf-8")
        return path
    raise AssertionError(kind)


BAD_KINDS = ["missing", "directory", "unreadable", "not_utf8", "empty", "no_chunks"]


@pytest.mark.parametrize("kind", BAD_KINDS)
def test_every_bad_input_raises_before_any_write(kind, tmp_path):
    """The good first path is read and chunked; the bad second one raises a
    named `GenesisImportError` naming that path, and the store saw no call."""
    from cobalt.genesis.chunk import GenesisImportError
    from cobalt.genesis.store import import_paths

    good = tmp_path / "good.md"
    good.write_bytes((FIXTURES / "structure.md").read_bytes())
    bad = _bad(kind, tmp_path)
    store = _RecordingStore()
    try:
        with pytest.raises(GenesisImportError) as raised:
            import_paths([str(good), str(bad)], store=store)
    finally:
        if kind == "unreadable":
            bad.chmod(0o600)
    assert str(bad) in str(raised.value)
    assert store.calls == []


def test_an_import_of_no_path_is_refused():
    from cobalt.genesis.chunk import GenesisImportError
    from cobalt.genesis.store import import_paths

    store = _RecordingStore()
    with pytest.raises(GenesisImportError):
        import_paths([], store=store)
    assert store.calls == []


def test_the_cli_import_of_a_bad_path_exits_non_zero_and_writes_nothing(monkeypatch, tmp_path, capsys):
    from cobalt import cli as cobalt_cli
    from cobalt.genesis import cli as genesis_cli

    store = _RecordingStore()
    monkeypatch.setattr(genesis_cli, "GenesisStore", lambda: store)
    missing = tmp_path / "missing.md"
    monkeypatch.setattr(sys, "argv", ["cobalt", "genesis", "import", str(missing)])
    with pytest.raises(SystemExit) as exited:
        cobalt_cli.main()
    assert exited.value.code != 0
    assert "GenesisImportError" in capsys.readouterr().err
    assert store.calls == []


# ---------------------------------------------------------------------
# G5 — the CLI
# ---------------------------------------------------------------------


def test_the_cli_mounts_import_and_search(monkeypatch, capsys):
    from cobalt import cli as cobalt_cli

    monkeypatch.setattr(sys, "argv", ["cobalt", "genesis", "--help"])
    with pytest.raises(SystemExit) as exited:
        cobalt_cli.main()
    assert exited.value.code == 0
    out = capsys.readouterr().out
    assert "import" in out and "search" in out


def test_the_cli_import_prints_one_line_per_source(monkeypatch, tmp_path, capsys):
    import hashlib

    from cobalt import cli as cobalt_cli
    from cobalt.genesis import cli as genesis_cli

    store = _RecordingStore()
    monkeypatch.setattr(genesis_cli, "GenesisStore", lambda: store)
    path = tmp_path / "notes.md"
    path.write_bytes((FIXTURES / "structure.md").read_bytes())
    monkeypatch.setattr(sys, "argv", ["cobalt", "genesis", "import", str(path)])
    cobalt_cli.main()
    sha = hashlib.sha256(path.read_bytes()).hexdigest()
    assert capsys.readouterr().out.splitlines() == [f"{path} · 8 chunks · sha256 {sha[:12]}"]
    assert [s.source for s in store.calls] == [str(path)]


def test_the_cli_search_prints_source_and_line_range(monkeypatch, capsys):
    from cobalt import cli as cobalt_cli
    from cobalt.genesis import cli as genesis_cli
    from cobalt.genesis.search import Hit

    seen = {}

    def fake_search(question, *, limit):
        seen.update(question=question, limit=limit)
        return [Hit(source="a.md", line_start=3, line_end=5, rank=0.5, body="first line\nsecond line")]

    monkeypatch.setattr(genesis_cli, "search", fake_search)
    monkeypatch.setattr(sys, "argv", ["cobalt", "genesis", "search", "why the drill", "--limit", "3"])
    cobalt_cli.main()
    assert seen == {"question": "why the drill", "limit": 3}
    lines = capsys.readouterr().out.splitlines()
    assert lines[0].startswith("a.md:3-5 ")
    assert "first line" in lines[0]


def test_search_refuses_a_limit_below_one_and_an_unknown_form():
    from cobalt.genesis.search import search

    with pytest.raises(ValueError):
        search("why the drill", limit=0)
    with pytest.raises(ValueError):
        search("why the drill", limit=3, form="phrase")
    with pytest.raises(ValueError):
        search("   ", limit=3)


# ---------------------------------------------------------------------
# Check f21-genesis-1013 (card 820): O1 / A1, O2
# ---------------------------------------------------------------------


def test_check_o1_replace_is_one_transaction_on_an_autocommit_connection():
    """db.connect() opens autocommit=True (db.py:199): a write the store does
    not wrap commits statement by statement. A failed INSERT must leave the
    source's old rows, so the DELETE may not have committed on its own."""
    from contextlib import contextmanager

    from cobalt.genesis.chunk import read_source
    from cobalt.genesis.store import GenesisStore

    class _Cursor:
        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def executemany(self, query, rows):
            raise RuntimeError("the connection dropped mid-insert")

    class _AutocommitConnection:
        """psycopg's semantics, reduced: in autocommit a statement outside a
        transaction block commits as it runs."""

        def __init__(self):
            self.autocommit = True
            self.committed: list[str] = []
            self._pending: list[str] = []
            self._depth = 0

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            self.rollback() if exc_type is not None else self.commit()
            return False

        def execute(self, query, params=None):
            stmt = query.split()[0]
            if self.autocommit and not self._depth:
                self.committed.append(stmt)
            else:
                self._pending.append(stmt)
            return self

        def cursor(self):
            return _Cursor()

        def commit(self):
            self.committed += self._pending
            self._pending = []

        def rollback(self):
            self._pending = []

        @contextmanager
        def transaction(self):
            self._depth += 1
            try:
                yield
            except BaseException:
                self._pending = []
                raise
            finally:
                self._depth -= 1
            if self.autocommit and not self._depth:
                self.commit()

    conn = _AutocommitConnection()
    store = GenesisStore("cobalt_dev")
    store._connect = lambda: conn
    with pytest.raises(RuntimeError):
        store.replace(read_source(str(FIXTURES / "structure.md")))
    assert conn.committed == [], "the DELETE committed alone: the source lost its rows and gained none"


def test_replace_keeps_the_delete_and_the_insert_on_one_non_autocommit_transaction(monkeypatch):
    """G2: replace deletes then inserts in ONE transaction. db.connect is
    autocommit=True, so both writes must observe autocommit False."""
    from cobalt.genesis.chunk import Chunk, Source
    from cobalt.genesis.store import GenesisStore

    events = []

    class _Conn:
        def __init__(self):
            self.autocommit = True

        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def execute(self, sql, params=None):
            events.append(("execute", self.autocommit))
            return self

        def cursor(self):
            return self

        def executemany(self, sql, rows):
            events.append(("executemany", self.autocommit))

        def commit(self):
            events.append(("commit", self.autocommit))

    store = GenesisStore("cobalt_dev")
    monkeypatch.setattr(store, "_connect", lambda: _Conn())
    store.replace(Source(
        source="a.md", sha256="ab",
        chunks=(Chunk(seq=1, line_start=1, line_end=1, body="one"),
                Chunk(seq=2, line_start=2, line_end=2, body="two")),
    ))
    writes = [(kind, flag) for kind, flag in events if kind in ("execute", "executemany")]
    assert writes == [("execute", False), ("executemany", False)], writes


def test_check_o2_line_numbers_count_newlines_only():
    """A line is what `\\n` ends (grep -n, an editor, the CLI's source:line
    citation): a form feed or a Unicode line separator inside a line is no
    line break."""
    from cobalt.genesis.chunk import chunk_markdown

    line_separator = chr(0x2028)
    text = f"first half{line_separator}second half\n\nthe next paragraph\x0cstill line three\n"
    chunks = chunk_markdown(text)
    assert [(c.line_start, c.line_end) for c in chunks] == [(1, 1), (3, 3)]
