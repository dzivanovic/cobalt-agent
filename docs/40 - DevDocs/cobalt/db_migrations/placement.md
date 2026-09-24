# `src/cobalt/db_migrations/placement.py`

`radar_pool` and `radar_membership` are system-side `CREATED_TABLES` in both placement and the migration proof set.

S2-P2: `radar_score_run`, `radar_score`, `desk_regime`, `desk_packet` and `desk_grade` are SYSTEM `CREATED_TABLES`; `card_dots`, `card_dot_taps` and `radar_score_receipt` are USER. The three views sit in `CREATED_VIEWS`: `radar_board_v` on the system side, `radar_cards_v` and `shadow_agreement_v` on the user side. They are in `PLACEMENT` like any table, but kept out of `CREATED_TABLES` because the migrate proof digests tables by primary key and a view has none. Every USER entry in `CREATED_TABLES` gets the same `user_id NOT NULL` + FK + GUC-default assertion as the moved tables.

2026-09-19, the append-only Bar Archiver: `archive_progress` and `archive_incidents` join `CREATED_TABLES` on the SYSTEM side (created directly there by `0010`/`0011`, so a rollback's `DROP` reads `DROPPED` in the migrate proof rather than `CHANGED`). Both are SYSTEM under L32 for the same reason `bars` is — they are bookkeeping ABOUT market data (a per-(ticker, interval) watermark, and what a night refused to write), not one trader's choice — and `cobalt_user` is granted nothing on either, so a wrong-side query fails loud.

## What it does
The map of which side every table is on. One map, three readers: the
suite's placement test (against what the database actually holds), the
store-side lint (every store names only its own side unqualified), and a
test asserting this map and `0002_move_tables.sql` agree.

## Key functions/classes
- `MOVED_TABLES` — the 12 that `0002` moves out of `public`.
- `SEEDED_TABLES` — created by `0001` on its side (`traders`).
- `MODULE_TABLES` — created by a feature module's own migration
  (`trade_defs`, `tunables`, `setup_trade_matrix`, `trader_settings`).
- `DECLARED_TABLES` — ruled before they are built (S2/S3), so the first
  migration that creates one has a side to create it on.
- `OLD_TREE_PUBLIC_TABLES` — the frozen 17. `public` is untouched
  (strangler rule) and a NEW table landing there fails the suite.
- `side_of(table)` / `tables_on(side)`.

## Gotchas
Two copies of the map exist — this one and the SQL's — because SQL
cannot import Python. A test makes a drift between them a failure rather
than a surprise.

---

## 2026-09-17 — S2-P4

`CREATED_TABLES` gains `movers_daily` (SYSTEM, from 0008), and `picks` and
`missed` (USER, from 0009). `missed` leaves `DECLARED_TABLES` now that it
is built. Every table still sits in exactly one part of the map
(`test_placement_movers_daily_system_picks_and_missed_user`).
`TestTenantGuc` now checks `user_id` NOT NULL + GUC default on every USER
table in `CREATED_TABLES` as well as the moved ones.

## 2026-09-23 — DRC D1

`CREATED_TABLES` gains `drc_imports`, `drc_fills` and `drc_rows`, all
USER, from `0016_drc.sql`: his imported files, their executions, and the
derived DRC rows (L32). `drc_rows` leaves `DECLARED_TABLES` now that it
is built.

`fills` stays declared and unbuilt. DRC D1 stores executions in
`drc_fills` (v2 `[F-35]`), and `legs` remains S3's.

The live `user_id` assertion in `test_tenancy` reads `CREATED_TABLES`,
so it covers the three new tables wherever 0016 has been applied.
`test_drc_store.py` runs the same assertion inside its never-committed
migration transaction.

## 2026-09-24 — DRC K1

`CREATED_TABLES` gains `drc_stated_books`, on the USER side, from `0018`.
It holds his own statements (L32).
