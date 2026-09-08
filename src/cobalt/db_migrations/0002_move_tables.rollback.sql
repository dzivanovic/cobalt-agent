-- 0002 REVERSE: put every new-core table back in `public` and drop the
-- `user_id` columns (ADR-0008, "Migration and rollback — two domains").
--
-- Run by `cobalt db migrate --rollback`. CATALOG-ONLY, like the forward
-- script: `ALTER TABLE ... SET SCHEMA public` rewrites one pg_class row
-- per relation and `DROP COLUMN` marks one pg_attribute row dropped. No
-- heap is rewritten, no row is read, `bars`'s 4.84M rows are not touched.
-- That is what makes this the DATABASE domain's rollback and the pg_dump
-- taken before the migration only the belt to this pair of braces.
--
-- WHAT IT DOES NOT DO, deliberately:
--   * it does not DROP the schemas. `"user"` still holds `traders`, and
--     dropping a schema is not reversible by a catalog flip.
--   * it does not DROP the roles. They are cluster-wide, NOLOGIN, and
--     harmless; dropping a role that owns nothing is a separate,
--     deliberate act, not part of a data rollback.
--   * it does not undo 0001's grants. A grant on a schema nothing uses
--     is inert, and re-running 0001 after this file is clean.
-- The result is a `public` that looks exactly as it did before 0002, with
-- 0001's (unused) scaffolding still standing — which is precisely what a
-- re-run of `cobalt db migrate` expects to find.
--
-- OWNERSHIP goes back to the login role (`current_user`), which is what
-- owned every table before 0002 ran.

-- ---------------------------------------------------------------------
-- 1. Drop `user_id` from every user-side table. Before the move, so the
--    FK to `"user".traders` is gone by the time the table leaves the
--    schema (a cross-schema FK would otherwise survive the move and be a
--    dependency `public` has no business carrying).
-- ---------------------------------------------------------------------
DO $$
DECLARE
    t text;
BEGIN
    FOREACH t IN ARRAY ARRAY[
        'aset_sizings', 'card_transitions', 'card_stop_edits',
        'day_modes', 'vault_writes', 'vault_overrides'
    ] LOOP
        IF EXISTS (
            SELECT 1 FROM pg_tables WHERE schemaname = 'user' AND tablename = t
        ) THEN
            EXECUTE format('ALTER TABLE %I.%I DROP COLUMN IF EXISTS user_id', 'user', t);
        END IF;
    END LOOP;
END
$$;

-- ---------------------------------------------------------------------
-- 2. SET SCHEMA public + OWNER back to the login role.
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
            WHERE schemaname = rec.side AND tablename = rec.tbl
        ) THEN
            EXECUTE format('ALTER TABLE %I.%I SET SCHEMA public', rec.side, rec.tbl);
            EXECUTE format(
                'ALTER TABLE public.%I OWNER TO %I', rec.tbl, current_user);
            RAISE NOTICE 'reversed %.% -> public.%', rec.side, rec.tbl, rec.tbl;
        END IF;
    END LOOP;
END
$$;
