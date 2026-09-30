"""DRC D3 — the first-gate experiments (`prompts/2026-09-28/10-drc-d3-build.md`
`## E1`, L70), run BEFORE any src edit.

X-K (the kind CHECK; drafter-named from reads — pass condition: "a
`build_day` row inserts into `drc_rows` with the CHECK as `0018` left it"):
inside the suite's rollback (`test_drc_store.py`'s `migrated`, never
committed — L76), with `0016`, `0018` and `08`'s `0019` applied, a direct
insert of a `drc_rows` row `kind = 'build_day'`. EXPECTED at E1: refused by
`drc_rows_kind_check` — the reason the drafter pinned `0020` (D3-M).

X-T (the template shape) is a read of his template, recorded in the report
by its counts only; it has no test here.
"""

from __future__ import annotations

import psycopg

from cobalt.db_migrations import FORWARD
from cobalt.drc.store import DrcStore

from test_drc_k1_store import _raises
from test_drc_store import D, migrated, requires_db  # noqa: F401 — fixtures are used by name

INSERT = (
    'INSERT INTO "user".drc_rows (day, kind, ref, inputs, derived, fn_version) '
    "VALUES (%s, 'build_day', 'build', '{}'::jsonb, '{}'::jsonb, 'drc.build/1')"
)


def _kind_check(conn) -> str:
    ((definition,),) = conn.execute(
        "SELECT pg_get_constraintdef(oid) FROM pg_constraint "
        "WHERE conrelid = '\"user\".drc_rows'::regclass AND conname = 'drc_rows_kind_check'"
    ).fetchall()
    return definition


@requires_db
def test_xk_drc_rows_refuses_a_build_kind_before_0020(migrated):
    """X-K at E1 — REVERSED at E4 (a NAMED REVERSAL, `## E4` D3-M): at E1
    FORWARD ended at `0019` and the insert was REFUSED by
    `drc_rows_kind_check` (`0018`'s six kinds) — the experiment's recorded
    result. With `0020` applied (FORWARD's last) the SAME insert PASSES;
    rolled back to `0019` (`0020`'s rollback) it is refused again."""
    from cobalt.db_migrations import MIGRATIONS_DIR
    from cobalt.db_migrations.cli import _apply

    assert FORWARD[-2].name == "0020_drc_build_kinds.sql"  # S3 exits C1's 0021 follows it
    assert "build_day" in _kind_check(migrated) and "build_trade" in _kind_check(migrated)
    with DrcStore()._connect() as conn:
        conn.execute(INSERT, (D,))
    _apply(migrated, [MIGRATIONS_DIR / "0020_drc_build_kinds.rollback.sql"])
    assert "build_day" not in _kind_check(migrated)
    assert migrated.execute("""SELECT count(*) FROM "user".drc_rows WHERE kind = 'build_day'""").fetchone()[0] == 0
    _raises(psycopg.errors.CheckViolation, INSERT, (D,))
    _apply(migrated, [MIGRATIONS_DIR / "0020_drc_build_kinds.rollback.sql"])  # repeated: a no-op
    _apply(migrated, [MIGRATIONS_DIR / "0020_drc_build_kinds.sql", MIGRATIONS_DIR / "0020_drc_build_kinds.sql"])
    assert "build_day" in _kind_check(migrated)


@requires_db
def test_the_0020_rollback_is_a_no_op_when_drc_rows_is_absent(migrated):
    """The rollback contract (`0014`–`0019`): its objects absent → nothing."""
    from cobalt.db_migrations import MIGRATIONS_DIR
    from cobalt.db_migrations.cli import _apply, _rollback_paths

    _apply(migrated, _rollback_paths("0015"))  # 0020 → 0016 in order: drc_rows gone
    assert migrated.execute("""SELECT to_regclass('"user".drc_rows')""").fetchone()[0] is None
    _apply(migrated, [MIGRATIONS_DIR / "0020_drc_build_kinds.rollback.sql"])
    _apply(migrated, FORWARD)
    assert "build_trade" in _kind_check(migrated)


def test_0020_is_registered_last_and_its_rollback_first():
    from cobalt.db_migrations import MIGRATIONS_DIR, REVERSE
    from cobalt.db_migrations.cli import _rollback_paths

    # S3 exits C1's 0021 now follows it (the last of the DRC lane, second-last overall).
    assert FORWARD[-2] == MIGRATIONS_DIR / "0020_drc_build_kinds.sql"
    assert FORWARD[-3].name == "0019_drc_events.sql"
    assert REVERSE[1] == MIGRATIONS_DIR / "0020_drc_build_kinds.rollback.sql"
    assert REVERSE[2].name == "0019_drc_events.rollback.sql"
    assert [p.name for p in _rollback_paths("0019")] == [
        "0021_legs.rollback.sql", "0020_drc_build_kinds.rollback.sql"]
    code = "\n".join(l for l in FORWARD[-2].read_text().splitlines() if not l.strip().startswith("--"))
    assert "CREATE TABLE" not in code and "'build_trade', 'build_day'" in code
    back = REVERSE[1].read_text()
    assert "-- COST:" in back and "to_regclass('\"user\".drc_rows')" in back
