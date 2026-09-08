"""The two-layer data model's migrations (ADR-0008).

`0001_schemas.sql`  — schemas, roles, grants, ownership, `"user".traders`,
                      the `cobalt.trader_id` GUC convention.
`0002_move_tables.sql` — every new-core table onto its side, plus
                      `user_id` on the user side.
`0002_move_tables.rollback.sql` — the reverse, catalog-only.

These are the DATABASE-WIDE migrations and they are the only ones that
live outside a feature module. A module's own DDL still lives in its own
`migrations/` directory and is still executed by its store's
`ensure_schema()`; those files create tables UNQUALIFIED and land them in
whichever schema the factory pinned on the connection.

Run them with `cobalt db migrate` (`--allow-prod` from ~/cobalt only,
`--rollback` to reverse 0002). Nothing runs them implicitly: a store's
`ensure_schema()` asserts the schemas exist and tells you to run the CLI.
"""

from pathlib import Path

MIGRATIONS_DIR = Path(__file__).parent

#: Applied in this order, every time, both idempotent.
FORWARD = (
    MIGRATIONS_DIR / "0001_schemas.sql",
    MIGRATIONS_DIR / "0002_move_tables.sql",
)

#: `--rollback`. 0001 is deliberately NOT reversed — see the file header.
REVERSE = (MIGRATIONS_DIR / "0002_move_tables.rollback.sql",)

__all__ = ["FORWARD", "MIGRATIONS_DIR", "REVERSE"]
