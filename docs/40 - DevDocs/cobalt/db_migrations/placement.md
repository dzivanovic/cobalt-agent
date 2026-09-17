# `src/cobalt/db_migrations/placement.py`

`radar_pool` and `radar_membership` are system-side `CREATED_TABLES` in both placement and the migration proof set.

S2-P2: `radar_score_run`, `radar_score`, `desk_regime`, `desk_packet` and `desk_grade` are SYSTEM `CREATED_TABLES`; `card_dots`, `card_dot_taps` and `radar_score_receipt` are USER. The three views sit in `CREATED_VIEWS`: `radar_board_v` on the system side, `radar_cards_v` and `shadow_agreement_v` on the user side. They are in `PLACEMENT` like any table, but kept out of `CREATED_TABLES` because the migrate proof digests tables by primary key and a view has none. Every USER entry in `CREATED_TABLES` gets the same `user_id NOT NULL` + FK + GUC-default assertion as the moved tables.

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
