"""F21 chunk 2 on cobalt_dev, row V4 (card 2026-10-13 469; FINAL F-02, X10; `requires_db`, hub-run).

`genesis_chunk.embedding vector(768)`, `embed_model`, `embed_dim` come from
migration 0028, so the file needs a level above 0013: the gate deselects it
in PASS 1 and runs it in PASS 2, after the FORWARD (`ops/desk/gate-lists.md`).
Every row is written inside the suite's rolled-back transaction (RULING 7.1d,
L76). Every text and vector is constructed (L28, L32).
"""

from __future__ import annotations

import os
import shutil
from pathlib import Path
from types import SimpleNamespace

import psycopg
import pytest

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)
pytestmark = [requires_db, pytest.mark.integration]

FIXTURES = Path(__file__).parent / "fixtures" / "genesis"
COLUMN_DIM = 768


def _vectors(store, source: str) -> list[tuple]:
    """(id, embedding, embed_model, embed_dim) of one source, in seq order."""
    with store._connect() as conn:
        return conn.execute(
            "SELECT id, embedding, embed_model, embed_dim FROM genesis_chunk "
            "WHERE source = %s ORDER BY seq", (source,)).fetchall()


def _imported(tmp_path):
    from cobalt.genesis.store import GenesisStore, import_paths

    store = GenesisStore("cobalt_dev")
    path = tmp_path / "structure.md"
    shutil.copyfile(FIXTURES / "structure.md", path)
    import_paths([str(path)], store=store)
    return store, str(path)


def _config(dim: int):
    from cobalt.modelaccess.config import EmbedRoute, ModelAccessConfig

    return ModelAccessConfig(routes={"local.embed": EmbedRoute(
        lane="local", kind="openai_embeddings", api_base="http://127.0.0.1:1234/v1",
        model="constructed-embed-model", timeout_s=30, dim=dim, key_name=None)})


def test_route_dim_not_column_dim_crashes_before_any_write(tmp_path):
    store, source = _imported(tmp_path)
    before = _vectors(store, source)
    assert before and all(r[1:] == (None, None, None) for r in before)

    from cobalt.genesis.embed import PREFLIGHT_TEXT, run_embed
    from cobalt.genesis.store import GenesisEmbedError

    texts: list[str] = []

    def fake_embed(route, text, *, caller, config=None):
        texts.append(text)
        return SimpleNamespace(route=route, vector=[0.5] * 8, dim=8, model_returned="constructed-embed-model")

    with pytest.raises(GenesisEmbedError) as e:
        run_embed(store, config=_config(8), embed=fake_embed, out=lambda line: None)
    # Both numbers, each in its place: "8" alone is a substring of "768" (check r2 O1).
    assert "the route's dim 8 is not" in str(e.value) and "declared dimension 768" in str(e.value)
    assert texts == [PREFLIGHT_TEXT], "no chunk was sent"
    assert _vectors(store, source) == before


def test_x10_a_wrong_length_vector_is_refused_loud(tmp_path):
    store, source = _imported(tmp_path)
    rows = _vectors(store, source)
    first, rest = rows[0][0], [r[0] for r in rows[1:]]

    # The column's declared dimension, as the store reads it at load.
    assert store.column_embed_dim() == COLUMN_DIM

    # The database refuses a wrong length on its own (X10).
    with pytest.raises(psycopg.Error) as e:
        with store._connect() as conn:
            conn.execute("UPDATE genesis_chunk SET embedding = %s, embed_model = 'm', embed_dim = 3 "
                         "WHERE id = %s", ("[0.5,0.5,0.5]", first))
    assert f"expected {COLUMN_DIM} dimensions" in str(e.value)

    # A half-stamped row is refused by the CHECK.
    with pytest.raises(psycopg.Error) as e:
        with store._connect() as conn:
            conn.execute("UPDATE genesis_chunk SET embed_model = 'm' WHERE id = %s", (first,))
    assert "check" in str(e.value).lower()

    # The store refuses before the database: unchecked, wrong length, zero.
    from cobalt.genesis.store import GenesisEmbedError

    with pytest.raises(GenesisEmbedError):
        store.set_embedding(first, [0.5] * COLUMN_DIM, model="constructed-embed-model", dim=COLUMN_DIM)
    store.check_embed_dim(COLUMN_DIM)
    for bad in ([0.5] * (COLUMN_DIM - 1), [], [0.0] * COLUMN_DIM):
        with pytest.raises(GenesisEmbedError):
            store.set_embedding(first, bad, model="constructed-embed-model", dim=len(bad))
    assert all(r[1:] == (None, None, None) for r in _vectors(store, source))

    # The right length lands with the model as returned and the dimension.
    store.set_embedding(first, [0.5] * COLUMN_DIM, model="constructed-embed-model", dim=COLUMN_DIM)
    after = {r[0]: r for r in _vectors(store, source)}
    assert after[first][1] is not None and after[first][2:] == ("constructed-embed-model", COLUMN_DIM)
    assert all(after[i][1:] == (None, None, None) for i in rest)
    assert [i for i, _ in store.null_chunks() if i in after] == rest
