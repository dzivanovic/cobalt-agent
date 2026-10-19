"""`"user".genesis_chunk`, the one table of F21 chunk 1 (migration 0026; card 468 G2, G3).

ONE SOURCE, ONE TRANSACTION (DECISION D4). `replace` deletes that
(user_id, source)'s rows and writes the new chunks in one transaction, so a
source is never half-imported and another source's rows are never touched.

READ EVERYTHING FIRST (L1, F-14). `import_paths` reads and chunks every path
of the call before the first write: one bad path raises `GenesisImportError`
and no source of that call is written. It reads only the paths it is given;
there is no default path.

THE VECTOR COLUMN (F21 chunk 2, migration 0028; card 469 V4, FINAL F-02).
`check_embed_dim(dim)` reads `embedding`'s declared dimension from
`pg_attribute.atttypmod` and raises `GenesisEmbedError` when it is not the
route's `dim`; `set_embedding` refuses to write until that check passed, and
refuses a vector of any other length, an empty one or an all-zero one, before
the database sees it (the column refuses a wrong length too, X10).
"""

from __future__ import annotations

import math
from typing import Optional, Sequence

from cobalt import db, env
from cobalt.db import Side

from .chunk import GenesisImportError, Source, read_source

#: The tenant of every statement: the GUC `db.apply_side` pins (ADR-0008).
_TRADER = "current_setting('cobalt.trader_id')::int"


class GenesisEmbedError(RuntimeError):
    """A vector that must not be written, or a column that does not fit the route (L1, F-02, F-14)."""


class GenesisStore:
    #: ADR-0008 D2 / L32: his ledger and vault history are one trader's own
    #: text, on the user side (F21 FINAL F-02).
    SIDE = Side.USER

    def __init__(self, db_name: Optional[str] = None):
        self.db_name = db_name or env.resolve_db_name()
        #: The column dimension `check_embed_dim` proved; None = nothing may be written.
        self._embed_dim: Optional[int] = None

    def _connect(self):
        return db.connect(self.db_name, side=self.SIDE)

    def replace(self, source: Source) -> int:
        """Swap `source`'s rows for its chunks in ONE transaction; the count written."""
        rows = [(source.source, source.sha256, c.seq, c.line_start, c.line_end, c.body)
                for c in source.chunks]
        with self._connect() as conn:
            # db.connect opens autocommit=True: without this the DELETE commits
            # on its own and a failed INSERT leaves a partial source (check O1).
            conn.autocommit = False
            conn.execute(f"DELETE FROM genesis_chunk WHERE user_id = {_TRADER} AND source = %s",
                         (source.source,))
            with conn.cursor() as cur:
                cur.executemany(
                    "INSERT INTO genesis_chunk (source, source_sha256, seq, line_start, line_end, body) "
                    "VALUES (%s, %s, %s, %s, %s, %s)", rows)
            conn.commit()
        return len(rows)

    def column_embed_dim(self) -> Optional[int]:
        """`genesis_chunk.embedding`'s declared dimension (pgvector keeps it in
        `atttypmod`); None when the column is absent (0028 not applied) or
        declares none."""
        with self._connect() as conn:
            row = conn.execute(
                "SELECT a.atttypmod FROM pg_catalog.pg_attribute a "
                """WHERE a.attrelid = '"user".genesis_chunk'::regclass AND a.attname = 'embedding' """
                "AND NOT a.attisdropped").fetchone()
        return row[0] if row and row[0] > 0 else None

    def check_embed_dim(self, dim: int) -> None:
        """At load, before any write: the route's `dim` is the column's, or raise (F-02, L1)."""
        column = self.column_embed_dim()
        if column is None:
            raise GenesisEmbedError(
                "genesis_chunk.embedding does not exist or declares no dimension: "
                "run `cobalt db migrate` (0028_genesis_vectors) before `cobalt genesis embed`")
        if column != dim:
            raise GenesisEmbedError(
                f"the route's dim {dim} is not genesis_chunk.embedding's declared dimension {column}: "
                "a model swap that changes the dimension is a migration of this table (F-02); nothing written")
        self._embed_dim = column

    def null_chunks(self) -> list[tuple[int, str]]:
        """(id, body) of every chunk of this trader with no vector yet, oldest first."""
        with self._connect() as conn:
            return [(r[0], r[1]) for r in conn.execute(
                f"SELECT id, body FROM genesis_chunk WHERE user_id = {_TRADER} AND embedding IS NULL "
                "ORDER BY id").fetchall()]

    def set_embedding(self, chunk_id: int, vector: Sequence[float], *, model: str, dim: int) -> None:
        """Write one chunk's vector, the model as returned and the dimension;
        it commits on its own (the connection is autocommit), so a run that
        stops keeps every vector already written."""
        if self._embed_dim is None:
            raise GenesisEmbedError("set_embedding before check_embed_dim: the column's dimension is unproven")
        if dim != self._embed_dim or len(vector) != self._embed_dim:
            raise GenesisEmbedError(
                f"a vector of length {len(vector)} (dim {dim}) for a vector({self._embed_dim}) column; not written")
        if not all(math.isfinite(x) for x in vector) or not any(vector):
            raise GenesisEmbedError("a zero or non-finite vector is never written (F-14)")
        if not model:
            raise GenesisEmbedError("a vector with no model as returned is never written (F-02)")
        literal = "[" + ",".join(repr(float(x)) for x in vector) + "]"
        with self._connect() as conn:
            done = conn.execute(
                f"UPDATE genesis_chunk SET embedding = %s, embed_model = %s, embed_dim = %s "
                f"WHERE id = %s AND user_id = {_TRADER} AND embedding IS NULL",
                (literal, model, dim, chunk_id)).rowcount
        if done != 1:
            raise GenesisEmbedError(f"chunk {chunk_id}: no NULL-vector row of this trader to write")


def import_paths(paths: Sequence[str], *, store) -> list[Source]:
    """Read and chunk every path, then write each source; nothing is written
    unless every path reads."""
    if not paths:
        raise GenesisImportError("no path given: genesis import reads only the paths it is given")
    sources = [read_source(path) for path in paths]
    for source in sources:
        store.replace(source)
    return sources


__all__ = ["GenesisEmbedError", "GenesisStore", "import_paths"]
