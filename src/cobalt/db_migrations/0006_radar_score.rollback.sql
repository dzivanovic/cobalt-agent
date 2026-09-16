-- 0006 rollback. Run after 0007's rollback (REVERSE order does that in one
-- `--down-to 0005` invocation). COST: drops every seam run/score row and the
-- empty desk tables; resets any radar_pool row whose failed_stage is
-- 'evaluate' (a per-scan status field the next scan rewrites) before the
-- 0004 CHECK domain is restored. Take the D1 pg_dump first.

DROP VIEW IF EXISTS system.radar_board_v;

DROP TABLE IF EXISTS system.desk_grade;
DROP TABLE IF EXISTS system.desk_packet;
DROP TABLE IF EXISTS system.desk_regime;
DROP TABLE IF EXISTS system.radar_score;
DROP TABLE IF EXISTS system.radar_score_run;

DO $migration$
DECLARE
    cleaned INTEGER;
    found_count INTEGER;
    found_name TEXT;
    found_definition TEXT;
BEGIN
    UPDATE system.radar_pool
       SET failed_stage = NULL, failed_detail = NULL
     WHERE failed_stage = 'evaluate';
    GET DIAGNOSTICS cleaned = ROW_COUNT;
    IF cleaned > 0 THEN
        RAISE NOTICE '0006 reverse cleared failed_stage=evaluate on % radar_pool row(s)', cleaned;
    END IF;

    SELECT count(*), min(c.conname), min(pg_get_constraintdef(c.oid))
      INTO found_count, found_name, found_definition
      FROM pg_constraint AS c
      JOIN pg_class AS t ON t.oid = c.conrelid
      JOIN pg_namespace AS n ON n.oid = t.relnamespace
     WHERE n.nspname = 'system'
       AND t.relname = 'radar_pool'
       AND c.contype = 'c'
       AND pg_get_constraintdef(c.oid) LIKE '%failed_stage%';

    IF found_count <> 1 THEN
        RAISE EXCEPTION '0006 reverse expected exactly one failed_stage CHECK on system.radar_pool, found %', found_count;
    END IF;
    IF found_definition NOT LIKE '%''evaluate''%' THEN
        RETURN;
    END IF;

    EXECUTE format('ALTER TABLE system.radar_pool DROP CONSTRAINT %I', found_name);
    ALTER TABLE system.radar_pool ADD CONSTRAINT radar_pool_failed_stage_check
        CHECK (failed_stage IN ('membership', 'pool_row', 'mirror', 'bars'));
END
$migration$;
