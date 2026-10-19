"""F21 chunk 1 on cobalt_dev (card 2026-10-13 468, rows G1–G4; `requires_db`, hub-run).

`"user".genesis_chunk` comes from migration 0026, so the file needs a level
above 0013: the gate deselects it in PASS 1 and runs it in PASS 2, after the
FORWARD (`ops/desk/gate-lists.md`). Every row is written inside the suite's
rolled-back transaction (RULING 7.1d, L76). Every text is a synthetic fixture
(`tests/cobalt/fixtures/genesis/`) or written into `tmp_path` (L28, L32).
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest

from cobalt import db
from cobalt.db import Side

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)
pytestmark = [requires_db, pytest.mark.integration]

FIXTURES = Path(__file__).parent / "fixtures" / "genesis"
#: The X1 / X7 (a) question; 0.37 is the fixture's constructed figure (L32).
QUESTION = "why is the stop buffer 0.37"
#: The one fixture entry that states the default with its reason.
TARGET = "E141 · Stop buffer default set to 0.37"


def _rows(store, source: str) -> list[tuple]:
    with store._connect() as conn:
        return conn.execute(
            "SELECT seq, line_start, line_end, body, source_sha256 FROM genesis_chunk "
            "WHERE source = %s ORDER BY seq", (source,)).fetchall()


def _count(store) -> int:
    with store._connect() as conn:
        return conn.execute("SELECT count(*) FROM genesis_chunk").fetchone()[0]


# ---------------------------------------------------------------------
# G1 — the table, as 0026 leaves it
# ---------------------------------------------------------------------


def test_the_table_is_user_side_with_user_id_fk_and_a_generated_tsv():
    with db.connect("cobalt_dev", side=Side.USER) as conn:
        rel = conn.execute("""SELECT '"user".genesis_chunk'::regclass::oid""").fetchone()[0]
        cols = {name: (notnull, generated) for name, notnull, generated in conn.execute(
            "SELECT attname, attnotnull, attgenerated::text FROM pg_attribute "
            "WHERE attrelid = %s AND attnum > 0 AND NOT attisdropped", (rel,)).fetchall()}
        assert cols["user_id"][0] is True and cols["user_id"][1] != "s"
        assert cols["tsv"][1] == "s", "tsv is GENERATED ALWAYS … STORED"
        assert cols["body"][0] and cols["source"][0] and cols["source_sha256"][0]
        # F21 vectors (0028, card 469 V4): chunk 2 adds `embedding`, `embed_model`, `embed_dim`
        # (pinned in test_genesis_vectors_db.py); 0026 alone adds no vector column.
        assert not [c for c in cols if "vector" in c], "no column named for a vector"
        gin = conn.execute(
            "SELECT count(*) FROM pg_index i JOIN pg_class c ON c.oid = i.indexrelid "
            "JOIN pg_am am ON am.oid = c.relam JOIN pg_attribute a "
            "ON a.attrelid = i.indrelid AND a.attnum = ANY(i.indkey) "
            "WHERE i.indrelid = %s AND am.amname = 'gin' AND a.attname = 'tsv'", (rel,)).fetchone()[0]
        assert gin == 1
        fk = conn.execute(
            """SELECT count(*) FROM pg_constraint WHERE conrelid = %s AND contype = 'f' """
            """AND confrelid = '"user".traders'::regclass""", (rel,)).fetchone()[0]
        assert fk == 1
        unique = conn.execute(
            "SELECT pg_get_constraintdef(oid) FROM pg_constraint WHERE conrelid = %s AND contype = 'u'",
            (rel,)).fetchall()
        assert [r[0] for r in unique] == ["UNIQUE (user_id, source, seq)"]
        nsp, owner = conn.execute(
            "SELECT n.nspname, pg_get_userbyid(c.relowner) FROM pg_class c "
            "JOIN pg_namespace n ON n.oid = c.relnamespace WHERE c.oid = %s", (rel,)).fetchone()
        assert (nsp, owner) == ("user", "cobalt_user")


# ---------------------------------------------------------------------
# G2 — a re-import replaces one source and leaves the others
# ---------------------------------------------------------------------


def test_reimport_replaces_one_source_and_leaves_others(tmp_path):
    from cobalt.genesis.chunk import read_source
    from cobalt.genesis.store import GenesisStore, import_paths

    store = GenesisStore("cobalt_dev")
    a, b = tmp_path / "a.md", tmp_path / "b.md"
    a.write_text("# A\n\nfirst drill paragraph\n\n- one\n- two\n", encoding="utf-8")
    b.write_bytes((FIXTURES / "structure.md").read_bytes())
    import_paths([str(a)], store=store)
    import_paths([str(b)], store=store)
    b_before = _rows(store, str(b))
    assert len(b_before) == 8 and len(_rows(store, str(a))) == 3

    a.write_text("# A\n\nthe drill paragraph changed\n", encoding="utf-8")
    new_a = read_source(str(a))
    import_paths([str(a)], store=store)
    a_after = _rows(store, str(a))
    assert len(a_after) == len(new_a.chunks) == 1
    assert {r[4] for r in a_after} == {new_a.sha256}
    assert a_after[0][3] == "# A\nthe drill paragraph changed"
    assert _rows(store, str(b)) == b_before


# ---------------------------------------------------------------------
# G3 — a bad second path writes nothing for the first
# ---------------------------------------------------------------------


def test_a_bad_second_path_writes_nothing_for_the_first(tmp_path):
    from cobalt.genesis.chunk import GenesisImportError
    from cobalt.genesis.store import GenesisStore, import_paths

    store = GenesisStore("cobalt_dev")
    good = tmp_path / "good.md"
    good.write_bytes((FIXTURES / "structure.md").read_bytes())
    before = _count(store)
    with pytest.raises(GenesisImportError):
        import_paths([str(good), str(tmp_path / "missing.md")], store=store)
    assert _count(store) == before
    assert _rows(store, str(good)) == []


# ---------------------------------------------------------------------
# G4 — X1 / X7 (a): the reason line ranks in the top three
# ---------------------------------------------------------------------


def _rank(hits, needle: str):
    return next((i for i, h in enumerate(hits, 1) if needle in h.body), None)


def test_x1_x7a_the_reason_line_is_in_the_top_three():
    from cobalt.genesis.search import search
    from cobalt.genesis.store import GenesisStore, import_paths

    store = GenesisStore("cobalt_dev")
    [source] = import_paths([str(FIXTURES / "ledger-200.md")], store=store)
    assert len(source.chunks) == 201, "the preamble and the 200 entries"

    web = search(QUESTION, limit=10)
    plain = search(QUESTION, limit=10, form="plain")
    web_rank, plain_rank = _rank(web, TARGET), _rank(plain, TARGET)
    target = next(h for h in web if TARGET in h.body) if web_rank else None
    message = (f"websearch_to_tsquery rank {web_rank} of {len(web)} hits; "
               f"plainto_tsquery rank {plain_rank} of {len(plain)} hits")
    print(message)
    assert web_rank is not None and web_rank <= 3, message
    assert (target.source, target.line_start, target.line_end) == (source.source, 147, 147), message
    assert target.rank > 0
