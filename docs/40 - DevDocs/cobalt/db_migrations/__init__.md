# `src/cobalt/db_migrations/__init__.py`

Migration 0004 is appended forward and prepended reverse so bounded rollback runs newest first.

S2-P2 adds `0006_radar_score.sql` (system side: `radar_score_run`, `radar_score`, `radar_board_v`, the empty `desk_regime`/`desk_packet`/`desk_grade`; `radar_pool.failed_stage` gains `'evaluate'`) and `0007_radar_cards.sql` (user side: nullable sizing plus the card columns on `aset_sizings`, `card_dots`, `card_dot_taps`, `radar_score_receipt`, `radar_cards_v`, `shadow_agreement_v`). Both are appended to `FORWARD` and prepended to `REVERSE`, so a single `--down-to 0005` reverses 0007 and then 0006 in one invocation (Astra R1-18).

Both are idempotent (Astra R1-3): `IF NOT EXISTS` / `OR REPLACE` everywhere, and constraints and triggers are guarded against the catalog. 0006 reads the inline 0004 `failed_stage` CHECK's name from `pg_constraint`, refuses any definition it does not recognise, and is a no-op once widened. Every new relation gets its side role as owner and explicit sequence grants (Astra R1-2). 0006 grants `cobalt_user` `REFERENCES` on `radar_score` and `radar_score_run` for the two cross-side FKs.

`radar_score_receipt` holds the stored inputs behind every seam number (L57, Astra R1-10): the actual pool unit, tunable rows, settings, definitions, tap versions and observations, each with its hash, never a hash alone. Its rows and `card_dot_taps` rows are immutable: `"user".refuse_row_update()` fires `BEFORE UPDATE`. Open-card uniqueness per (member, def slug, direction) is a partial unique index, not an application check (Astra R1-14). Chunk B added `aset_sizings_one_promoted_radar_card`, a partial unique index on `(user_id) WHERE origin='radar' AND promoted_at IS NOT NULL`: one promoted card per trader, which two concurrent promotes on different rows could otherwise break. It is idempotent, and the 0007 reverse drops it.

The 0007 reverse deletes radar-origin cards first (their transitions, stop edits, dots and taps cascade). It restores the old `NOT NULL`s only after that. The 0006 reverse clears `failed_stage='evaluate'` before restoring the 0004 CHECK.

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
