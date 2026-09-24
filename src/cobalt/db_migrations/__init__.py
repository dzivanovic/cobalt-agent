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
`0005_heartbeat_note_absent.sql` — adds the benign note-absence outcome.
`0005_heartbeat_note_absent.rollback.sql` — restores the 0003 outcome domain
                                         only when no new-domain row exists.
`0006_radar_score.sql` — the system-side radar scoring seam (runs, scores,
                         board view, empty desk tables); `failed_stage`
                         gains 'evaluate'.
`0006_radar_score.rollback.sql` — drops the seam; clears 'evaluate' stages
                                  before restoring the 0004 CHECK.
`0007_radar_cards.sql` — user-side radar cards: nullable sizing, card
                         columns, dots, taps, run receipt, views.
`0007_radar_cards.rollback.sql` — deletes radar-origin cards, drops the
                                  card tables/columns, restores NOT NULL.
`0008_radar_value_movers.sql` — membership rank_metric/rank_value and the
                              system movers_daily table (S2-P4).
`0008_radar_value_movers.rollback.sql` — drops movers_daily and both columns.
`0009_picks_missed.sql` — "user".picks and "user".missed (S2-P4).
`0009_picks_missed.rollback.sql` — drops both tables.
`0010_archive_progress.sql` — the Bar Archiver's own per-(ticker,
                         interval) watermark, system side (append-only
                         FINAL design §4, §11). Additive.
`0010_archive_progress.rollback.sql` — drops that one table; the next
                         `append` night bootstraps each target again.
`0011_archive_incidents.sql` — what an append night refused to do and
                         why: the five kinds, one unresolved row per
                         condition, read by the heartbeat. Additive.
`0011_archive_incidents.rollback.sql` — drops that one table.

0006/0007 are S2-P2's, 0008/0009 are S2-P4's. Both tuples stay ordered by
version; every file is idempotent and neither 0008 nor 0009 names a P2
object (`--down-to` selects by version, never by position).

THE 0008/0009 GAP IS CLOSED. Those two numbers belonged to the then
unmerged `sprint-2/p4`, which shipped on 2026-09-19 (deploy 2); this
branch rebased onto it and keeps BOTH sets in numeric order, exactly as
the gap note said the second lander would. This registry is an EXPLICIT
ordered tuple and nothing asserts contiguity. `_rollback_paths` selects
by the numeric prefix, so `--down-to 0009` reverses exactly 0011 then
0010, and `--down-to 0007` reverses those two plus P4's pair.

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

#: Applied in this order, every time, every file idempotent.
FORWARD = (
    MIGRATIONS_DIR / "0001_schemas.sql",
    MIGRATIONS_DIR / "0002_move_tables.sql",
    MIGRATIONS_DIR / "0003_heartbeat_vault_outcome.sql",
    MIGRATIONS_DIR / "0004_radar_pool.sql",
    MIGRATIONS_DIR / "0005_heartbeat_note_absent.sql",
    MIGRATIONS_DIR / "0006_radar_score.sql",
    MIGRATIONS_DIR / "0007_radar_cards.sql",
    MIGRATIONS_DIR / "0008_radar_value_movers.sql",
    MIGRATIONS_DIR / "0009_picks_missed.sql",
    MIGRATIONS_DIR / "0010_archive_progress.sql",
    MIGRATIONS_DIR / "0011_archive_incidents.sql",
)

#: `--rollback`, newest first. 0001 is deliberately NOT reversed.
REVERSE = (
    MIGRATIONS_DIR / "0011_archive_incidents.rollback.sql",
    MIGRATIONS_DIR / "0010_archive_progress.rollback.sql",
    MIGRATIONS_DIR / "0009_picks_missed.rollback.sql",
    MIGRATIONS_DIR / "0008_radar_value_movers.rollback.sql",
    MIGRATIONS_DIR / "0007_radar_cards.rollback.sql",
    MIGRATIONS_DIR / "0006_radar_score.rollback.sql",
    MIGRATIONS_DIR / "0005_heartbeat_note_absent.rollback.sql",
    MIGRATIONS_DIR / "0004_radar_pool.rollback.sql",
    MIGRATIONS_DIR / "0003_heartbeat_vault_outcome.rollback.sql",
    MIGRATIONS_DIR / "0002_move_tables.rollback.sql",
)

__all__ = ["FORWARD", "MIGRATIONS_DIR", "REVERSE"]
