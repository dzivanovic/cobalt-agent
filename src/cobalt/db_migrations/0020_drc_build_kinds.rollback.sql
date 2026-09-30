-- 0020 rollback.
-- COST: deletes every `build_trade` / `build_day` row — derived, not his
-- input: re-running the DRC build for a day (`cobalt drc build --date D`)
-- rebuilds them from the day's stored rows. The notes are untouched.
-- A no-op when `"user".drc_rows` is absent (the 0014–0019 contract).

DO $migration$
BEGIN
    IF to_regclass('"user".drc_rows') IS NULL THEN
        RETURN;
    END IF;
    DELETE FROM "user".drc_rows WHERE kind IN ('build_trade', 'build_day');
    ALTER TABLE "user".drc_rows DROP CONSTRAINT IF EXISTS drc_rows_kind_check;
    ALTER TABLE "user".drc_rows ADD CONSTRAINT drc_rows_kind_check
        CHECK (kind IN ('trade', 'open_position', 'stats_row', 'day', 'seed', 'book_close'));
END
$migration$;
