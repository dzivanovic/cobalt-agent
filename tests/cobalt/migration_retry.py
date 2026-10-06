"""`open_migrated` — the ONE migration step with the autovacuum-deadlock
retry, for every with-DB test that applies migrations on its own
migration connection (flake-fix-2 F1; the loop `flake-fix` wrote into
`test_drc_store.py`'s `migrated` fixture, moved here unchanged).

An autovacuum worker can deadlock a migration's `ALTER … OWNER TO`
(`reports/second-writer-survey-2026-10-05.md`). The step — open,
autocommit off, the FIRST apply — is retried at most twice, each attempt
on a fresh connection and transaction; a failed attempt's connection is
always closed, even when its rollback raises. Any other error, or a
third deadlock, propagates. Later applies on the returned connection
are the caller's and are not retried.

A bare-name import (`from migration_retry import open_migrated`), like
`radar_migrated_support`: `tests/cobalt/` has no `__init__.py`.
"""

from __future__ import annotations

import psycopg

from cobalt import db, env


def open_migrated(apply, paths):
    """`apply(conn, paths)` on a fresh `db.connect_migration` connection
    with autocommit off; returns that open connection. `apply` is the
    caller's own, resolved at its call, so a test that patches its
    module's `_apply` still reaches this step."""
    for attempt in range(1, 4):
        conn = None
        try:
            conn = db.connect_migration(env.DEV_DB_NAME)
            conn.autocommit = False
            apply(conn, paths)
            return conn
        except BaseException as exc:
            if conn is not None:
                try:
                    conn.rollback()
                finally:
                    conn.close()
            if not isinstance(exc, psycopg.errors.DeadlockDetected) or attempt == 3:
                raise
            print(f"migration retry {attempt}: DeadlockDetected")
