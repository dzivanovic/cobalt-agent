# `src/cobalt/db_migrations/__init__.py`

Migration 0004 is appended forward and prepended reverse so bounded rollback runs newest first.

S2-P2 adds `0006_radar_score.sql` (system side: `radar_score_run`, `radar_score`, `radar_board_v`, the empty `desk_regime`/`desk_packet`/`desk_grade`; `radar_pool.failed_stage` gains `'evaluate'`) and `0007_radar_cards.sql` (user side: nullable sizing plus the card columns on `aset_sizings`, `card_dots`, `card_dot_taps`, `radar_score_receipt`, `radar_cards_v`, `shadow_agreement_v`). Both are appended to `FORWARD` and prepended to `REVERSE`, so a single `--down-to 0005` reverses 0007 and then 0006 in one invocation (Astra R1-18).

Both are idempotent (Astra R1-3): `IF NOT EXISTS` / `OR REPLACE` everywhere, and constraints and triggers are guarded against the catalog. 0006 reads the inline 0004 `failed_stage` CHECK's name from `pg_constraint`, refuses any definition it does not recognise, and is a no-op once widened. Every new relation gets its side role as owner and explicit sequence grants (Astra R1-2). 0006 grants `cobalt_user` `REFERENCES` on `radar_score` and `radar_score_run` for the two cross-side FKs.

`radar_score_receipt` holds the stored inputs behind every seam number (L57, Astra R1-10): the actual pool unit, tunable rows, settings, definitions, tap versions and observations, each with its hash, never a hash alone. Its rows and `card_dot_taps` rows are immutable: `"user".refuse_row_update()` fires `BEFORE UPDATE`. Open-card uniqueness per (member, def slug, direction) is a partial unique index, not an application check (Astra R1-14). Chunk B added `aset_sizings_one_promoted_radar_card`, a partial unique index on `(user_id) WHERE origin='radar' AND promoted_at IS NOT NULL`: one promoted card per trader, which two concurrent promotes on different rows could otherwise break. It is idempotent, and the 0007 reverse drops it.

The 0007 reverse deletes radar-origin cards first (their transitions, stop edits, dots and taps cascade). It restores the old `NOT NULL`s only after that. The 0006 reverse clears `failed_stage='evaluate'` before restoring the 0004 CHECK.

## 2026-09-19 — the append-only Bar Archiver adds 0010 and 0011

The registered list, in `FORWARD` order:

| # | file | what it creates | side | rollback |
|---|---|---|---|---|
| 0001 | `0001_schemas.sql` | schemas, roles, grants, `"user".traders` | both | none (deliberate) |
| 0002 | `0002_move_tables.sql` | the twelve tables onto their sides + `user_id` | both | catalog-only reverse |
| 0003 | `0003_heartbeat_vault_outcome.sql` | durable heartbeat vault delivery | system | drops the two columns |
| 0004 | `0004_radar_pool.sql` | `radar_pool`, `radar_membership`, account-mode stamps | system | bounded destructive |
| 0005 | `0005_heartbeat_note_absent.sql` | the benign note-absence outcome | system | restores the 0003 domain |
| 0006 | `0006_radar_score.sql` | the scoring seam + empty desk tables | system | drops the seam |
| 0007 | `0007_radar_cards.sql` | radar cards, dots, taps, receipt, views | user | deletes radar cards, drops the columns |
| **0010** | **`0010_archive_progress.sql`** | **`system.archive_progress`** — the archiver's own watermark per (ticker, interval) | **system** | **`DROP TABLE` of that one table** |
| **0011** | **`0011_archive_incidents.sql`** | **`system.archive_incidents`** — the five kinds, one unresolved row per condition | **system** | **`DROP TABLE` of that one table** |

**`0008`/`0009` are missing on purpose.** They belong to the unmerged
branch `sprint-2/p4` and are never used here. `FORWARD`/`REVERSE` are
EXPLICIT ordered tuples and nothing in the suite asserts contiguity, so
the gap is legal; `_rollback_paths` selects by numeric prefix, so
`--down-to 0007` reverses exactly 0011 then 0010 whether or not P4's
pair is present. The branch that lands second rebases and keeps both
sets in numeric order — that rebase, and the integrated suite on the
combined tree, are the gate.

Both new migrations are ADDITIVE in the strongest sense the suite can
check: `test_archiver_migrations.py::test_neither_migration_touches_bars_or_any_existing_object`
asserts neither file contains `ALTER TABLE system.bars`, `DROP`,
`UPDATE`, `DELETE` or `radar_pool`. `system.bars` — its columns, PK and
indexes — is explicitly out of scope of the append-only design (§1
non-goals), and partitioning is Sunday's tribunal.

Both are SYSTEM side (L32: bookkeeping ABOUT market data, nothing of one
trader's choice) and **`cobalt_user` is granted nothing on either** — a
test asserts the string does not appear in any of the four files. 0011's
`BIGSERIAL` sequence is granted to `cobalt_system` explicitly, following
0006's pattern rather than relying on 0001's default privileges.

0011's uniqueness is a PARTIAL unique index `WHERE resolved_at IS NULL`
with **`NULLS NOT DISTINCT`** (Postgres 15+). The NULL clause is
load-bearing: an `empty_export` incident has no span, so its
`range_start` is NULL, and under the default rule a target failing empty
for a month would open thirty rows for one condition.

Both tables are declared in `placement.py`'s `CREATED_TABLES`, so the
migrate proof carries them and a `--down-to 0007` reads `DROPPED` rather
than `CHANGED` for each.

## What it does
Holds the DATABASE-WIDE migrations — the two-schema split itself
(ADR-0008). `FORWARD` is `0001_schemas.sql` then
`0002_move_tables.sql`; `REVERSE` is `0002_move_tables.rollback.sql`.

## Why it exists (and why it is the only directory like it)
A feature module's DDL lives in its own `migrations/` and is run by its
own store. These files belong to no feature: schemas, roles, grants,
ownership, and moving twelve tables from `public` onto a side. Anything
that DOES belong to a module stays with the module — `taxonomy/` and
`settings/` both keep their own.

## Gotchas
Nothing runs these implicitly. A store's `ensure_schema()` asserts the
schemas exist and tells you to run `cobalt db migrate`.

`0001` is idempotent and re-run on every invocation; it is deliberately
NOT reversed by `--rollback` (dropping a schema is not a catalog flip).

---

## 2026-09-17 — S2-P4: 0008 and 0009

`FORWARD` gains `0008_radar_value_movers.sql` (system) and
`0009_picks_missed.sql` (user). `REVERSE` gains their rollbacks, newest
first. 0006/0007 are reserved for S2-P2, and both tuples stay ordered by
version whichever merges first. Neither P4 file names a P2 object, so
either merge order applies. `--down-to` selects by version, never by
position.

**0008 (system).**
- `radar_membership` gains `rank_metric TEXT CHECK IN ('volume','rvol')`
  and `rank_value NUMERIC(20,6)`.
- New `system.movers_daily` table, owned by `cobalt_system`. Rows are never
  deleted: `active` is false for a row a rerun dropped (Astra R2-1), and
  the partial unique index `movers_daily_one_active` keeps one active row
  per (trade_date, side, ticker).
- `replay_run_id` names the run that selected the row.
- `cobalt_user` gets `SELECT, REFERENCES` (for `missed.mover_id`) and the
  identity sequence grant.

**0009 (user).** `"user".picks` and `"user".missed`, both owned by
`cobalt_user`, both with `user_id INTEGER NOT NULL DEFAULT
current_setting('cobalt.trader_id')::int REFERENCES "user".traders(id)`.

`picks` has one row per card (`card_id UNIQUE`), linked to its FILLED
`card_transitions` row. `pool_basis`, `score_basis` and `score_inputs`
store why a field is null and what the rank came from (L57).

`missed` carries an immutable `receipt` JSONB hashed by `inputs_sha256`
(Astra R1-8). The receipt-owned `replay_run_id` replaces the plan's
`replay_job_id`. Versioning columns (R2-1/R3-1):
- `run_seq`, `is_current`, `superseded_by → missed(id)`, `retired_by_run_id`
- CHECK: a non-current row names its retiring run.
- CHECK: a current row has no successor.
- `missed_one_current_per_subject` is a partial unique index `WHERE
  is_current`. For formations it also keys on `formation_at` and the
  member (R1-21).

A rerun reconciles in one transaction: retire, then insert, then link.

**Migration prose is checked, not trusted** (2026-09-18, chunk FY).
`0008`'s header called `movers_daily` "the unfiltered top movers the 21:05
replay fetches"; R17 moved `com.cobalt.replay` to 21:10 on 2026-09-17 and
the comment kept pointing at an occurrence that no longer exists.
`test_p4_migration_prose_names_no_retired_schedule_literal` reads
`000[89]*.sql` WITH their comments (the other lint tests strip them through
`_sql`) and refuses any retired schedule literal. Correcting a comment is
safe here because the runner's digests are of table DATA
(`cli.DIGEST_EXCLUDED_COLUMNS` and the probe), never of the file's bytes —
there is no content checksum over a `.sql` file anywhere in this package.

**Rollbacks** drop only their own tables and columns. Reverse 0009 before
0008: `missed` references `movers_daily`. The boundary is `--down-to 0007`.
If P2 is present, its 0007 rollback deleting radar cards that picks/missed
reference is blocked by the NO ACTION foreign keys and fails loud; nothing
is lost silently (plan §6 R1-23).

**2026-09-21 — `0013_tunables_slug_nullable` (setups one build STEP-2;
FINAL §8, R2-3 = B, decided by X20).**

Forward: `ALTER TABLE "user".tunables ALTER COLUMN slug DROP NOT NULL`.
It is idempotent. It raises a NOTICE and does nothing when the table
does not exist yet: on a fresh database whose taxonomy store never ran,
the store later creates the table NOT NULL, the first global assumed row
fails its sync loudly, and 0013 must be re-run.

Rollback: refuses (`REFUSING 0013 reverse`) while any `slug IS NULL` row
exists, because a rollback never deletes his rows. Otherwise it restores
`SET NOT NULL`. This is the bounded pattern of 0005's reverse.

The number 0013 skips 0012 on purpose. 0012 belongs to the unmerged
`bars/chunk-2-0920` (`0012_bars_partitioned_parent`). Whichever lands
second keeps both, in numeric order. This is an L68 seam on this
`__init__.py` and on the migration-list tests.
