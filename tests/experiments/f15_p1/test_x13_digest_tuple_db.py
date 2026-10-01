"""X13 — card 61 RUN row, FINAL row X13 (`[F-38]`), at BASE inside the
suite's rolled-back transaction.

One constructed `aset_sizings` row; the table's migrate-proof digest taken
through `db_migrations/cli.py` `_row_json('aset_sizings')` — the ONE digest
expression the streamed proof builds on — before and after
`ADD COLUMN IF NOT EXISTS last_price_bar_ts`: (i) with BASE's tuple, (ii)
with the tuple plus `last_price_bar_ts` (monkeypatched here). Prints the
three digests and whether each differs. Asserts nothing (L70). The
migrate-level half is W: (c2) forward with no `CHANGED`, (f) back to 0013
with F2 = F0, (c4) forward and back twice.
"""

from __future__ import annotations

from test_x12_transition_ids_db import requires_db

pytestmark = [requires_db]


def _digest(conn) -> str:
    from psycopg import sql

    from cobalt.db_migrations.cli import _row_json

    query = sql.SQL("SELECT md5(string_agg(({row})::text, ',' ORDER BY t.id)) FROM aset_sizings AS t").format(
        row=_row_json("aset_sizings"))
    return conn.execute(query).fetchone()[0]


def test_x13_the_aset_sizings_digest_with_and_without_the_tuple_entry(monkeypatch):
    from cobalt.aset.store import AsetStore
    from cobalt.db_migrations import cli
    from legs_db_support import patch_daymode, sizing

    patch_daymode(monkeypatch)
    aset = AsetStore("cobalt_dev")
    card_id = aset.save(sizing())
    with aset._connect() as conn:
        rows = conn.execute("SELECT count(*) FROM aset_sizings").fetchone()[0]
        before = _digest(conn)
        conn.execute('ALTER TABLE "user".aset_sizings ADD COLUMN IF NOT EXISTS last_price_bar_ts TIMESTAMPTZ')
        base_tuple = _digest(conn)
        monkeypatch.setitem(cli.TABLE_DIGEST_EXCLUDED_COLUMNS, "aset_sizings",
                            (*cli.TABLE_DIGEST_EXCLUDED_COLUMNS["aset_sizings"], "last_price_bar_ts"))
        with_entry = _digest(conn)
    print(f"X13: one constructed row (card {card_id}); aset_sizings rows in the transaction {rows}")
    print(f"X13: digest before the column          {before}")
    print(f"X13: (i)  after, BASE's tuple           {base_tuple} — differs: {base_tuple != before}")
    print(f"X13: (ii) after, tuple + last_price_bar_ts {with_entry} — differs: {with_entry != before}")
