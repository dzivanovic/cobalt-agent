-- Bounded reverse for 0013. Refuse atomically while any global (slug NULL)
-- row exists — restoring NOT NULL would have to drop the trader's assumed
-- defaults, and a rollback never deletes his rows. Otherwise SET NOT NULL.
DO $migration$
BEGIN
    IF to_regclass('"user".tunables') IS NULL THEN
        RETURN;
    END IF;
    IF EXISTS (SELECT 1 FROM "user".tunables WHERE slug IS NULL) THEN
        RAISE EXCEPTION 'REFUSING 0013 reverse: "user".tunables holds rows with slug NULL (global assumed defaults)';
    END IF;
    ALTER TABLE "user".tunables ALTER COLUMN slug SET NOT NULL;
END
$migration$;
