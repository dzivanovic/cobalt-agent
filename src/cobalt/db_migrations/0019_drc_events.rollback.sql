-- 0019 rollback.
-- COST: bounded destructive — drops `"user".drc_events` and with it every
-- event's history (state, error, note path); a re-apply starts with no
-- event rows, and the next drop or no-trade action fires the day again.
-- The three `drc_imports` columns and both CHECKs come back exactly as
-- `0016_drc.sql:35`–`:37`, `:42` declare them, empty.
-- A no-op when its objects are absent: the table by `IF EXISTS`, the
-- `drc_imports` statements behind the `to_regclass` guard (a table 0016
-- owns; `0013_tunables_slug_nullable.rollback.sql`, `0018`'s shape).

DROP TABLE IF EXISTS "user".drc_events;
DO $migration$
BEGIN
    IF to_regclass('"user".drc_imports') IS NULL THEN
        RETURN;
    END IF;
    IF NOT EXISTS (
        SELECT 1 FROM pg_attribute
         WHERE attrelid = '"user".drc_imports'::regclass AND attname = 'event_state' AND NOT attisdropped
    ) THEN
        ALTER TABLE "user".drc_imports
            ADD COLUMN event_state     TEXT CHECK (event_state IN ('pending', 'running', 'done', 'failed')),
            ADD COLUMN event_updated_at TIMESTAMPTZ,
            ADD COLUMN event_error     TEXT,
            ADD CHECK (event_state IS NULL OR event_updated_at IS NOT NULL);
    END IF;
END
$migration$;
