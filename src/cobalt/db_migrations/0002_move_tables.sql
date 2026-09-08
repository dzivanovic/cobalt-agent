-- 0002: move every new-core table onto its side, and give every
-- user-side table its `user_id` (ADR-0008 D1/D2).
--
-- `ALTER TABLE ... SET SCHEMA` IS CATALOG-ONLY. It rewrites one pg_class
-- row per relation; the heap, every index, every constraint and every
-- column-owned sequence move with it untouched. That is what makes the
-- 4.84M-row `bars` move instant and what makes the reverse script
-- (0002_move_tables.rollback.sql) a real rollback rather than a restore.
--
-- PLACEMENT (ADR-0008 D2). The Python copy of this map lives in
-- `cobalt.db_migrations.placement` and the suite asserts the two name the
-- same tables on the same sides, so a table added to one and forgotten in
-- the other fails the suite rather than the next migration.
--
--   "user"  aset_sizings, card_transitions, card_stop_edits, day_modes,
--           vault_writes, vault_overrides
--   system  bars, cobalt_jobs, cobalt_kill_switch, cobalt_redactions,
--           cobalt_email_sends, session_blocks
--   public  the 17 old-tree tables — UNTOUCHED (strangler rule).
--
-- `"user".traders` is created by 0001 and is not moved here.
--
-- IDEMPOTENT. A table already on its side is skipped; `user_id` is added
-- with IF NOT EXISTS, backfilled only where NULL, and its constraint and
-- default are guarded. This file must run twice cleanly.
--
-- WHY `user_id` IS ADDED IN FOUR STEPS. Nullable, backfill to 1, SET NOT
-- NULL, then the default — the same shape as `aset_sizings.state` and
-- `vault_writes.session` before it, and for the same reason: a NOT NULL
-- applied before its own backfill has run cannot succeed on a populated
-- table. The DEFAULT is added LAST and is
-- `current_setting('cobalt.trader_id')::int` — never a literal. A literal
-- default would silently accept a write from a connection that never
-- passed through the factory, which is exactly the failure the GUC
-- exists to make loud.

-- ---------------------------------------------------------------------
-- 1. SET SCHEMA + OWNER, per side.
-- ---------------------------------------------------------------------
DO $$
DECLARE
    rec record;
BEGIN
    FOR rec IN
        SELECT * FROM (VALUES
            ('user',   'aset_sizings'),
            ('user',   'card_transitions'),
            ('user',   'card_stop_edits'),
            ('user',   'day_modes'),
            ('user',   'vault_writes'),
            ('user',   'vault_overrides'),
            ('system', 'bars'),
            ('system', 'cobalt_jobs'),
            ('system', 'cobalt_kill_switch'),
            ('system', 'cobalt_redactions'),
            ('system', 'cobalt_email_sends'),
            ('system', 'session_blocks')
        ) AS p(side, tbl)
    LOOP
        IF EXISTS (
            SELECT 1 FROM pg_tables
            WHERE schemaname = 'public' AND tablename = rec.tbl
        ) THEN
            EXECUTE format('ALTER TABLE public.%I SET SCHEMA %I', rec.tbl, rec.side);
            RAISE NOTICE 'moved public.% -> %.%', rec.tbl, rec.side, rec.tbl;
        END IF;
        IF EXISTS (
            SELECT 1 FROM pg_tables
            WHERE schemaname = rec.side AND tablename = rec.tbl
        ) THEN
            EXECUTE format(
                'ALTER TABLE %I.%I OWNER TO %I',
                rec.side, rec.tbl, 'cobalt_' || rec.side);
        END IF;
    END LOOP;
END
$$;

-- ---------------------------------------------------------------------
-- 2. `user_id` on every user-side table. Nullable -> backfill -> NOT
--    NULL -> FK -> GUC default, in that order, per table.
-- ---------------------------------------------------------------------
DO $$
DECLARE
    t text;
BEGIN
    FOREACH t IN ARRAY ARRAY[
        'aset_sizings', 'card_transitions', 'card_stop_edits',
        'day_modes', 'vault_writes', 'vault_overrides'
    ] LOOP
        CONTINUE WHEN NOT EXISTS (
            SELECT 1 FROM pg_tables WHERE schemaname = 'user' AND tablename = t
        );

        EXECUTE format(
            'ALTER TABLE %I.%I ADD COLUMN IF NOT EXISTS user_id INTEGER', 'user', t);
        EXECUTE format(
            'UPDATE %I.%I SET user_id = 1 WHERE user_id IS NULL', 'user', t);
        EXECUTE format(
            'ALTER TABLE %I.%I ALTER COLUMN user_id SET NOT NULL', 'user', t);

        IF NOT EXISTS (
            SELECT 1 FROM pg_constraint
            WHERE conname = t || '_user_id_fkey'
              AND conrelid = format('%I.%I', 'user', t)::regclass
        ) THEN
            EXECUTE format(
                'ALTER TABLE %I.%I ADD CONSTRAINT %I FOREIGN KEY (user_id) '
                'REFERENCES %I.traders(id)',
                'user', t, t || '_user_id_fkey', 'user');
        END IF;

        EXECUTE format(
            'ALTER TABLE %I.%I ALTER COLUMN user_id SET DEFAULT '
            '(current_setting(''cobalt.trader_id'')::int)', 'user', t);
    END LOOP;
END
$$;
