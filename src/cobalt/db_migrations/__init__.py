"""The two-layer data model's migrations (ADR-0008).

`0001_schemas.sql`  — schemas, roles, grants, ownership, `"user".traders`,
                      the `cobalt.trader_id` GUC convention.
`0002_move_tables.sql` — every new-core table onto its side, plus
                      `user_id` on the user side.
`0002_move_tables.rollback.sql` — the reverse, catalog-only.
`0003_heartbeat_vault_outcome.sql` — durable heartbeat vault delivery.
`0003_heartbeat_vault_outcome.rollback.sql` — removes those two columns.
`0004_radar_pool.sql` — radar pool/membership and account-mode stamps.
`0004_radar_pool.rollback.sql` — bounded destructive reverse of 0004.

These are the DATABASE-WIDE migrations and they are the only ones that
live outside a feature module. A module's own DDL still lives in its own
`migrations/` directory and is still executed by its store's
`ensure_schema()`; those files create tables UNQUALIFIED and land them in
whichever schema the factory pinned on the connection.

Run them with `cobalt db migrate` (`--allow-prod` from ~/cobalt only,
`--rollback` to reverse 0003 then 0002). Nothing runs them implicitly: a store's
`ensure_schema()` asserts the schemas exist and tells you to run the CLI.
"""

from pathlib import Path

MIGRATIONS_DIR = Path(__file__).parent

#: Applied in this order, every time, both idempotent.
FORWARD = (
    MIGRATIONS_DIR / "0001_schemas.sql",
    MIGRATIONS_DIR / "0002_move_tables.sql",
    MIGRATIONS_DIR / "0003_heartbeat_vault_outcome.sql",
    MIGRATIONS_DIR / "0004_radar_pool.sql",
)

#: `--rollback`, newest first. 0001 is deliberately NOT reversed.
REVERSE = (
    MIGRATIONS_DIR / "0004_radar_pool.rollback.sql",
    MIGRATIONS_DIR / "0003_heartbeat_vault_outcome.rollback.sql",
    MIGRATIONS_DIR / "0002_move_tables.rollback.sql",
)

__all__ = ["FORWARD", "MIGRATIONS_DIR", "REVERSE"]
