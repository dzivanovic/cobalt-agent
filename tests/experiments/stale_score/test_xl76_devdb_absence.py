"""XL76 (L76: no migration left applied on `cobalt_dev`), READ-ONLY: is
`0015`'s exclusion on `cobalt_dev`'s `"user".shadow_agreement_v`? One
`pg_get_viewdef` of the live view (L35 P-e: `pg_catalog`, never
`information_schema`) on `connect_migration`, autocommit off, rolled back in
`finally`. The comparison body is 0007's view as the server normalises it:
the `0015` rollback file (0007's view, exact) applied inside the SAME
rolled-back transaction and read back — nothing is committed."""

from __future__ import annotations

import stale_db_support as sds

pytestmark = sds.requires_db

VIEWDEF = "SELECT pg_get_viewdef('\"user\".shadow_agreement_v'::regclass)"


def test_xl76_cobalt_dev_does_not_carry_0015():
    from cobalt import db, env
    from cobalt.db_migrations import MIGRATIONS_DIR

    conn = db.connect_migration(env.DEV_DB_NAME)
    conn.autocommit = False
    try:
        live = conn.execute(VIEWDEF).fetchone()[0]
        conn.execute((MIGRATIONS_DIR / "0015_shadow_agreement_stale.rollback.sql").read_text())
        body_0007 = conn.execute(VIEWDEF).fetchone()[0]
    finally:
        conn.rollback()
        conn.close()
    has_exclusion = "evaluator_version" in live
    print(f"XL76: view_has_0015_exclusion={has_exclusion} view_equals_0007={live == body_0007}")
    assert not has_exclusion and live == body_0007
