"""The placement map: which side every table is on (ADR-0008 D2).

ONE MAP, THREE READERS. The suite's placement test compares it against
what the database actually holds; the lint test compares every store's
SQL against its own `SIDE`; and a test asserts this map and
`0002_move_tables.sql` name the same tables on the same sides, so the
Python copy and the SQL copy cannot drift apart in silence.

FUTURE TABLES ARE DECLARED HERE BEFORE THEY EXIST. That is the point of
the map: ADR-0008 D2 names the S2/S3 tables (`trade_defs`, `tunables`,
`trader_settings`, `radar_pool`, `radar_membership`, the legs/fills and
missed rows, the taxonomy anatomy instances) so that when one of them is
created it lands on a side someone already ruled on. A table that exists
in `"user"` or `system` and is NOT in this map fails the placement test;
so does a table on the wrong side.

`public` IS FROZEN. The 17 old-tree tables are listed and untouched
(strangler rule). A NEW table landing in `public` fails the suite — that
is the whole enforcement behind "every new table is declared on a side".
"""

from cobalt.db import Side

#: The 12 tables `0002_move_tables.sql` moves out of `public`.
#: `"user".traders` is not here: 0001 creates it directly on its side.
MOVED_TABLES: dict[str, Side] = {
    # --- user side -----------------------------------------------------
    "aset_sizings": Side.USER,
    "card_transitions": Side.USER,
    "card_stop_edits": Side.USER,
    "day_modes": Side.USER,
    "vault_writes": Side.USER,
    "vault_overrides": Side.USER,
    # --- system side ---------------------------------------------------
    "bars": Side.SYSTEM,
    "cobalt_jobs": Side.SYSTEM,
    "cobalt_kill_switch": Side.SYSTEM,
    "cobalt_redactions": Side.SYSTEM,
    "cobalt_email_sends": Side.SYSTEM,
    "session_blocks": Side.SYSTEM,
}

#: Created by 0001 on its side, never moved.
SEEDED_TABLES: dict[str, Side] = {
    "traders": Side.USER,
}

#: Declared by ADR-0008 D2 before they are built, so the first migration
#: that creates one has a ruled side to create it on. Nothing here exists
#: yet; the placement test only checks tables that DO exist.
DECLARED_TABLES: dict[str, Side] = {
    # D3 — loaded copies of the vault's trade_def units and the trader's
    # own settings. User data by definition (L32).
    "trade_defs": Side.USER,
    "tunables": Side.USER,
    "trader_settings": Side.USER,
    "setup_trade_matrix": Side.USER,   # a VIEW unnested from trade_defs
    # S2-P4 / S3 — named now so the placement test knows them on sight.
    "legs": Side.USER,
    "fills": Side.USER,
    "missed": Side.USER,
    "drc_rows": Side.USER,
    "prediction_records": Side.USER,
    # S2-P1 — the radar. System: the pool and its membership history are
    # engine artefacts any trader's strategies plug into.
    "radar_pool": Side.SYSTEM,
    "radar_membership": Side.SYSTEM,
    # S2-P2 — taxonomy anatomy instances (regime, range, gap, extension,
    # leg, session clock). The anatomy IS the system.
    "anatomy_instances": Side.SYSTEM,
}

#: Every table this codebase has ruled on.
PLACEMENT: dict[str, Side] = {**MOVED_TABLES, **SEEDED_TABLES, **DECLARED_TABLES}

#: The old tree's tables, frozen in `public` and never touched
#: (strangler rule). They exist in `cobalt_brain`; `cobalt_dev` has none
#: of them, so the test asserts containment, not equality.
OLD_TREE_PUBLIC_TABLES: frozenset[str] = frozenset({
    "memory_logs",
    "graph_nodes",
    "graph_edges",
    "hitl_proposals",
    "browser_fast_path",
    "instruments",
    "market_snapshots",
    "daily_in_play",
    "key_levels",
    "news_events",
    "news_mentions",
    "order_fills",
    "strategy_signals",
    "system_alerts",
    "themes",
    "trades",
    "trading_accounts",
})


def side_of(table: str) -> Side:
    """The ruled side of `table`, or a loud failure naming this file."""
    try:
        return PLACEMENT[table]
    except KeyError:
        raise KeyError(
            f"table {table!r} has no ruled side. Every new table is declared on "
            "exactly one side in cobalt/db_migrations/placement.py (ADR-0008 D2) "
            "before it is created."
        ) from None


def tables_on(side: Side) -> frozenset[str]:
    """Every ruled table on `side`, declared-but-unbuilt ones included."""
    return frozenset(t for t, s in PLACEMENT.items() if s is side)


__all__ = [
    "DECLARED_TABLES",
    "MOVED_TABLES",
    "OLD_TREE_PUBLIC_TABLES",
    "PLACEMENT",
    "SEEDED_TABLES",
    "side_of",
    "tables_on",
]
