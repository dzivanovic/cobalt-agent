"""dev-rebuild D1 / D3 — `rebuild_table` frees every dropped column slot.

With-DB, on `cobalt_dev` through the one migration factory
(`db.connect_migration(env.DEV_DB_NAME)`), `autocommit = False`, and
EVERY test rolls back at the end: nothing these tests build or rebuild is
ever committed.

D1 builds a constructed scratch table in `"user"` that carries every kind
of thing a rebuild can lose (identity, default, NOT NULL, CHECK, index,
trigger, RLS with a policy, a grant, comments, an FK in from a child, a
view over it, three rows), adds and drops five columns, and rebuilds it.
The negative control skips the grant step and must be refused, with the
table read back exactly as BEFORE.

D3 runs the rule on the table this job exists for, `"user".aset_sizings`
at `0013`, as a dry run.
"""

from __future__ import annotations

import os

import pytest

from cobalt import db, env
import cobalt.db_migrations.dev_rebuild as dev_rebuild
from cobalt.db_migrations.dev_rebuild import RebuildMismatch, read_state, rebuild_table

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)

SCRATCH = "zz_dev_rebuild_scratch"
CHILD = "zz_dev_rebuild_child"
VIEW = "zz_dev_rebuild_v"
TOUCH = "zz_dev_rebuild_touch"
DROPPED = 5


@pytest.fixture
def conn():
    c = db.connect_migration(env.DEV_DB_NAME)
    c.autocommit = False
    try:
        c.execute("SET LOCAL lock_timeout = '30s'")
        yield c
    finally:
        c.rollback()
        c.close()


def _build_scratch(conn) -> None:
    """The constructed table, its child, its view, three rows; then five
    columns added and dropped so five slots are dead."""
    t = f'"user".{SCRATCH}'
    for stmt in (
        f"""CREATE FUNCTION "user".{TOUCH}() RETURNS trigger LANGUAGE plpgsql AS $$
            BEGIN NEW.note := coalesce(NEW.note, 'touched'); RETURN NEW; END $$""",
        f"""CREATE TABLE {t} (
                id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                label text NOT NULL,
                qty integer NOT NULL DEFAULT 7,
                note text,
                CONSTRAINT {SCRATCH}_qty_check CHECK (qty > 0)
            )""",
        f"CREATE INDEX {SCRATCH}_label_idx ON {t} (label)",
        f"""CREATE TRIGGER {SCRATCH}_touch BEFORE INSERT OR UPDATE ON {t}
            FOR EACH ROW EXECUTE FUNCTION "user".{TOUCH}()""",
        f"ALTER TABLE {t} ENABLE ROW LEVEL SECURITY",
        f"CREATE POLICY {SCRATCH}_read ON {t} FOR SELECT TO cobalt_user USING (qty > 0)",
        f"GRANT SELECT, INSERT ON {t} TO cobalt_user",
        # Grants no schema default gives, so a rebuild that skips its
        # grant step reads differently (the negative control).
        f"GRANT SELECT ON {t} TO cobalt_system WITH GRANT OPTION",
        f"GRANT UPDATE (note) ON {t} TO cobalt_system",
        f"COMMENT ON TABLE {t} IS 'constructed scratch table (dev-rebuild test)'",
        f"COMMENT ON COLUMN {t}.label IS 'constructed label'",
        f"""CREATE TABLE "user".{CHILD} (
                id bigint PRIMARY KEY,
                scratch_id bigint NOT NULL REFERENCES {t}(id)
            )""",
        f'CREATE VIEW "user".{VIEW} AS SELECT id, label, qty FROM {t}',
        f'GRANT SELECT ON "user".{VIEW} TO cobalt_user',
        f"INSERT INTO {t} (label, qty) VALUES ('alpha', 1), ('beta', 2), ('gamma', 3)",
        f'INSERT INTO "user".{CHILD} (id, scratch_id) SELECT 1, min(id) FROM {t}',
    ):
        conn.execute(stmt)
    for i in range(DROPPED):
        conn.execute(f"ALTER TABLE {t} ADD COLUMN zz_extra_{i} text")
        conn.execute(f"ALTER TABLE {t} DROP COLUMN zz_extra_{i}")


@requires_db
def test_d1_rebuild_frees_every_dropped_slot_and_keeps_rows_and_catalog(conn):
    _build_scratch(conn)
    before = read_state(conn, "user", SCRATCH)
    assert before.dropped == DROPPED
    assert before.max_attnum == before.live + DROPPED
    assert before.rows == 3
    # The digest actually SEES what a rebuild could lose — a section that
    # read nothing could not catch anything.
    s = before.sections
    assert any("cobalt_system:SELECT*" in line for line in s["grants"]), s["grants"]
    assert any(line.startswith("column note|") for line in s["grants"]), s["grants"]
    assert any(f"{SCRATCH}_read" in line for line in s["policies"])
    assert any(f"{SCRATCH}_touch" in line for line in s["triggers"])
    assert any(f"{SCRATCH}_label_idx" in line for line in s["indexes"])
    assert any(f"{SCRATCH}_qty_check" in line for line in s["constraints"])
    assert any(CHILD in line for line in s["fks_in"])
    assert any(VIEW in line for line in s["views"])
    assert len(s["sequences"]) == 1

    result = rebuild_table(conn, "user", SCRATCH, dry_run=False)

    after = read_state(conn, "user", SCRATCH)
    assert after.max_attnum == after.live == before.live
    assert after.dropped == 0
    assert (after.rows, after.row_digest) == (before.rows, before.row_digest)
    assert after.sections == before.sections
    assert after.catalog_digest == before.catalog_digest
    assert result.before == before
    assert result.after == after


@requires_db
def test_d1_negative_control_a_skipped_grant_is_refused_and_nothing_is_kept(
    conn, monkeypatch
):
    _build_scratch(conn)
    before = read_state(conn, "user", SCRATCH)
    monkeypatch.setattr(dev_rebuild, "_restore_grants", lambda *a, **k: None)

    with pytest.raises(RebuildMismatch) as caught:
        rebuild_table(conn, "user", SCRATCH, dry_run=False)

    assert caught.value.fields == ("grants",)
    assert read_state(conn, "user", SCRATCH) == before


@requires_db
def test_d1_dry_run_rolls_back_after_the_compare(conn):
    _build_scratch(conn)
    before = read_state(conn, "user", SCRATCH)

    result = rebuild_table(conn, "user", SCRATCH, dry_run=True)

    assert result.dry_run is True
    assert result.after.max_attnum == result.after.live == before.live
    assert result.after.dropped == 0
    assert read_state(conn, "user", SCRATCH) == before


@requires_db
def test_d3_aset_sizings_passes_the_rule_as_a_dry_run_at_0013(conn):
    before = read_state(conn, "user", "aset_sizings")
    # Its dependents at 0013 are inside the digest.
    assert any("radar_cards_v" in line for line in before.sections["views"])
    # FKs in: 0007's card_dots (:121) and card_dot_taps (:144), 0009's
    # picks (:19) and missed (:71), as the catalog holds them at 0013.
    for child in ("card_dots", "card_dot_taps", "picks", "missed"):
        assert any(f'"user".{child}|' in line for line in before.sections["fks_in"]), child

    result = rebuild_table(conn, "user", "aset_sizings", dry_run=True)

    after = result.after
    assert after.max_attnum == after.live == before.live
    assert after.dropped == 0
    assert (after.rows, after.row_digest) == (before.rows, before.row_digest)
    assert after.sections == before.sections
    assert after.catalog_digest == before.catalog_digest
    assert read_state(conn, "user", "aset_sizings") == before


@requires_db
def test_check_o1_toast_reloptions_survive_the_rebuild(conn):
    _build_scratch(conn)
    conn.execute(f'ALTER TABLE "user".{SCRATCH} SET (toast.autovacuum_enabled = false)')
    q = ("SELECT t.reloptions FROM pg_class c JOIN pg_class t ON t.oid = c.reltoastrelid"
         " WHERE c.oid = %s::regclass")
    rel = f'"user".{SCRATCH}'
    assert conn.execute(q, (rel,)).fetchone()[0] == ["autovacuum_enabled=false"]
    assert any("autovacuum_enabled=false" in line for line in read_state(conn, "user", SCRATCH).sections["table"])
    rebuild_table(conn, "user", SCRATCH, dry_run=False)
    assert conn.execute(q, (rel,)).fetchone()[0] == ["autovacuum_enabled=false"]


@requires_db
def test_check_o2_a_view_column_default_survives_the_rebuild(conn):
    _build_scratch(conn)
    v = f'"user".{VIEW}'
    conn.execute(f"ALTER VIEW {v} ALTER COLUMN qty SET DEFAULT 5")
    q = ("SELECT pg_get_expr(d.adbin, d.adrelid) FROM pg_attrdef d"
         " JOIN pg_attribute a ON a.attrelid = d.adrelid AND a.attnum = d.adnum"
         " WHERE d.adrelid = %s::regclass AND a.attname = 'qty'")
    assert conn.execute(q, (v,)).fetchone()[0] == "5"
    rebuild_table(conn, "user", SCRATCH, dry_run=False)
    row = conn.execute(q, (v,)).fetchone()
    assert row is not None and row[0] == "5"


@requires_db
def test_check_o3_the_table_access_method_survives_the_rebuild(conn):
    t = '"user".zz_dev_rebuild_am_t'
    conn.execute("CREATE ACCESS METHOD zz_dev_rebuild_am TYPE TABLE HANDLER heap_tableam_handler")
    conn.execute(f"CREATE TABLE {t} (id bigint PRIMARY KEY, note text) USING zz_dev_rebuild_am")
    conn.execute(f"INSERT INTO {t} VALUES (1, 'a')")
    conn.execute(f"ALTER TABLE {t} ADD COLUMN zz_extra text")
    conn.execute(f"ALTER TABLE {t} DROP COLUMN zz_extra")
    q = "SELECT am.amname FROM pg_class c JOIN pg_am am ON am.oid = c.relam WHERE c.oid = %s::regclass"
    assert conn.execute(q, (t,)).fetchone()[0] == "zz_dev_rebuild_am"
    rebuild_table(conn, "user", "zz_dev_rebuild_am_t", dry_run=False)
    assert conn.execute(q, (t,)).fetchone()[0] == "zz_dev_rebuild_am"


@requires_db
def test_check_o4_an_index_column_statistics_target_survives_the_rebuild(conn):
    _build_scratch(conn)
    idx = f'"user".{SCRATCH}_lower_idx'
    conn.execute(f'CREATE INDEX {SCRATCH}_lower_idx ON "user".{SCRATCH} (lower(label))')
    conn.execute(f"ALTER INDEX {idx} ALTER COLUMN 1 SET STATISTICS 321")
    q = "SELECT attstattarget FROM pg_attribute WHERE attrelid = %s::regclass AND attnum = 1"
    assert conn.execute(q, (idx,)).fetchone()[0] == 321
    rebuild_table(conn, "user", SCRATCH, dry_run=False)
    assert conn.execute(q, (idx,)).fetchone()[0] == 321


#: The card's `<SL>` read, the deploy hub's slot read, verbatim.
SL = (
    "SELECT max(a.attnum) AS max_attnum, count(*) FILTER (WHERE a.attisdropped) AS dropped,"
    " count(*) FILTER (WHERE NOT a.attisdropped) AS live FROM pg_catalog.pg_attribute a"
    " WHERE a.attrelid = '\"user\".aset_sizings'::regclass AND a.attnum > 0"
)


@requires_db
def test_s1_slot_report_on_cobalt_dev_matches_the_slot_read_for_aset_sizings(conn):
    """slot-guard S1: `slot_report` answers for `"user".aset_sizings` the
    same three numbers the hub's `<SL>` reads, inside this rolled-back
    transaction."""
    from cobalt.db_migrations.dev_rebuild import slot_report

    rows = slot_report(conn)
    mine = [r for r in rows if r[:2] == ("user", "aset_sizings")]
    assert len(mine) == 1, rows
    assert tuple(mine[0][2:]) == tuple(conn.execute(SL).fetchone())
    # Every relation it names is in one of the two schemas, highest first.
    assert {r[0] for r in rows} <= {"system", "user"}
    assert [r[2] for r in rows] == sorted((r[2] for r in rows), reverse=True)
