"""`"user".genesis_chunk`, the one table of F21 chunk 1 (migration 0026; card 468 G2, G3).

ONE SOURCE, ONE TRANSACTION (DECISION D4). `replace` deletes that
(user_id, source)'s rows and writes the new chunks in one transaction, so a
source is never half-imported and another source's rows are never touched.

READ EVERYTHING FIRST (L1, F-14). `import_paths` reads and chunks every path
of the call before the first write: one bad path raises `GenesisImportError`
and no source of that call is written. It reads only the paths it is given;
there is no default path.
"""

from __future__ import annotations

from typing import Optional, Sequence

from cobalt import db, env
from cobalt.db import Side

from .chunk import GenesisImportError, Source, read_source

#: The tenant of every statement: the GUC `db.apply_side` pins (ADR-0008).
_TRADER = "current_setting('cobalt.trader_id')::int"


class GenesisStore:
    #: ADR-0008 D2 / L32: his ledger and vault history are one trader's own
    #: text, on the user side (F21 FINAL F-02).
    SIDE = Side.USER

    def __init__(self, db_name: Optional[str] = None):
        self.db_name = db_name or env.resolve_db_name()

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


def import_paths(paths: Sequence[str], *, store) -> list[Source]:
    """Read and chunk every path, then write each source; nothing is written
    unless every path reads."""
    if not paths:
        raise GenesisImportError("no path given: genesis import reads only the paths it is given")
    sources = [read_source(path) for path in paths]
    for source in sources:
        store.replace(source)
    return sources


__all__ = ["GenesisStore", "import_paths"]
