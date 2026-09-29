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

from test_drc_k1_store import _raises
from test_drc_store import D, migrated, requires_db  # noqa: F401 — fixtures are used by name

INSERT = (
    'INSERT INTO "user".drc_rows (day, kind, ref, inputs, derived, fn_version) '
    "VALUES (%s, 'build_day', 'build', '{}'::jsonb, '{}'::jsonb, 'drc.build/1')"
)


@requires_db
def test_xk_drc_rows_refuses_a_build_kind_before_0020(migrated):
    """X-K at E1: FORWARD ends at `0019`; the CHECK is `0018`'s six kinds,
    so a `build_day` row is refused by `drc_rows_kind_check`."""
    assert FORWARD[-1].name == "0019_drc_events.sql"
    ((definition,),) = migrated.execute(
        "SELECT pg_get_constraintdef(oid) FROM pg_constraint "
        "WHERE conrelid = '\"user\".drc_rows'::regclass AND conname = 'drc_rows_kind_check'"
    ).fetchall()
    assert "build_day" not in definition
    _raises(psycopg.errors.CheckViolation, INSERT, (D,))
