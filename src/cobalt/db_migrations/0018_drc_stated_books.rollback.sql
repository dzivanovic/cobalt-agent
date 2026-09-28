-- 0018 rollback.
-- COST: drops every stated opening book, resolve and no-trade statement:
-- his statements live ONLY here; re-state them after a re-apply. The
-- `seed` / `book_close` rows are derived and are deleted too — re-recording
-- a day rebuilds them from its stored imports.

DO $migration$
BEGIN
    IF to_regclass('"user".drc_rows') IS NULL THEN
        RETURN;
    END IF;
    DELETE FROM "user".drc_rows WHERE kind IN ('seed', 'book_close');
    ALTER TABLE "user".drc_rows DROP CONSTRAINT IF EXISTS drc_rows_kind_check;
    ALTER TABLE "user".drc_rows ADD CONSTRAINT drc_rows_kind_check
        CHECK (kind IN ('trade', 'open_position', 'stats_row', 'day'));
END
$migration$;
DROP TABLE IF EXISTS "user".drc_stated_books;
