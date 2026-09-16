-- 0006: the radar scoring seam, SYSTEM side (S2-P2 STEP-1, plan L52-c).
--
-- `radar_score_run` is one evaluate pass (scan-job stage S5) per pool
-- scan; `radar_score` is one (member x trade_def) evaluation inside it;
-- `radar_board_v` is the latest COMPLETE run per pool. The three desk
-- tables are created empty for S3-P0.
--
-- SYSTEM PAYLOAD ONLY (L32, Astra R1-1). No slug, no def text, no WHY
-- prose and no trader settings content cross to this side: a trade_def
-- is referenced by md5 alone, settings by hash alone. `detail` and
-- `desk_shadow` are closed payloads validated by `cobalt.radar.seam`
-- before they are written; the database only insists they are objects.
-- The stored inputs behind every number live user-side, in
-- "user".radar_score_receipt (0007, L57).
--
-- IDEMPOTENT (Astra R1-3): every CREATE is IF NOT EXISTS / OR REPLACE,
-- the CHECK widening is guarded against the catalog, and a second
-- `cobalt db migrate` is a no-op.

-- ---------------------------------------------------------------------
-- 1. radar_pool.failed_stage gains 'evaluate'. 0004 declared the CHECK
--    inline, so its name is read from pg_constraint rather than assumed.
-- ---------------------------------------------------------------------
DO $migration$
DECLARE
    found_count INTEGER;
    found_name TEXT;
    found_definition TEXT;
BEGIN
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
        RAISE EXCEPTION '0006 expected exactly one failed_stage CHECK on system.radar_pool, found %', found_count;
    END IF;
    IF found_name = 'radar_pool_failed_stage_check'
       AND found_definition LIKE '%''evaluate''%' THEN
        RETURN;
    END IF;
    IF found_definition LIKE '%''evaluate''%' THEN
        RAISE EXCEPTION '0006 refusing unexpected failed_stage constraint %: %', found_name, found_definition;
    END IF;
    IF found_definition NOT LIKE '%''membership''%'
       OR found_definition NOT LIKE '%''pool_row''%'
       OR found_definition NOT LIKE '%''mirror''%'
       OR found_definition NOT LIKE '%''bars''%' THEN
        RAISE EXCEPTION '0006 refusing unexpected failed_stage constraint %: %', found_name, found_definition;
    END IF;

    EXECUTE format('ALTER TABLE system.radar_pool DROP CONSTRAINT %I', found_name);
    ALTER TABLE system.radar_pool ADD CONSTRAINT radar_pool_failed_stage_check
        CHECK (failed_stage IN ('membership', 'pool_row', 'mirror', 'bars', 'evaluate'));
END
$migration$;

-- ---------------------------------------------------------------------
-- 2. One evaluate pass per (pool, scan).
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS system.radar_score_run (
    id                BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    pool_key          TEXT NOT NULL REFERENCES system.radar_pool(pool_key),
    scan_id           BIGINT NOT NULL,
    previous_run_id   BIGINT REFERENCES system.radar_score_run(id),
    session           TEXT NOT NULL,
    started_at        TIMESTAMPTZ NOT NULL,
    finished_at       TIMESTAMPTZ,
    status            TEXT NOT NULL CHECK (status IN ('running', 'complete', 'failed')),
    cards_enabled     BOOLEAN NOT NULL,
    evaluator_version TEXT NOT NULL,
    formula_sha256    TEXT NOT NULL,
    tunables_sha256   TEXT NOT NULL,
    settings_sha256   TEXT NOT NULL,
    cohort_sha256     TEXT NOT NULL,
    failed_detail     TEXT,
    UNIQUE (pool_key, scan_id)
);

ALTER TABLE system.radar_score_run OWNER TO cobalt_system;
CREATE INDEX IF NOT EXISTS radar_score_run_latest
    ON system.radar_score_run (pool_key, status, started_at DESC);

-- ---------------------------------------------------------------------
-- 3. One evaluation per (run, member, trade_def md5).
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS system.radar_score (
    id                BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    run_id            BIGINT NOT NULL REFERENCES system.radar_score_run(id) ON DELETE CASCADE,
    membership_id     BIGINT NOT NULL REFERENCES system.radar_membership(id),
    ticker            TEXT NOT NULL,
    trade_def_md5     TEXT NOT NULL,
    direction         TEXT CHECK (direction IN ('long', 'short')),
    evaluation        TEXT NOT NULL CHECK (evaluation IN (
                          'formed', 'not_formed', 'avoided', 'not_evaluable', 'input_stale')),
    detail            JSONB NOT NULL CHECK (jsonb_typeof(detail) = 'object'),
    desk_shadow       JSONB NOT NULL CHECK (jsonb_typeof(desk_shadow) = 'object'),
    proximity         NUMERIC(8, 6),
    conviction        NUMERIC(8, 6),
    card_score        INTEGER,
    suppressed_reason TEXT,
    inputs_sha256     TEXT NOT NULL,
    UNIQUE (run_id, membership_id, trade_def_md5)
);

ALTER TABLE system.radar_score OWNER TO cobalt_system;
CREATE INDEX IF NOT EXISTS radar_score_membership
    ON system.radar_score (membership_id, trade_def_md5);

-- ---------------------------------------------------------------------
-- 4. The board: rows of the latest COMPLETE run per pool, by started_at.
-- ---------------------------------------------------------------------
CREATE OR REPLACE VIEW system.radar_board_v AS
    SELECT s.*, r.pool_key, r.scan_id, r.started_at
      FROM system.radar_score AS s
      JOIN system.radar_score_run AS r ON r.id = s.run_id
     WHERE r.id = (
         SELECT r2.id FROM system.radar_score_run AS r2
          WHERE r2.pool_key = r.pool_key AND r2.status = 'complete'
          ORDER BY r2.started_at DESC, r2.id DESC
          LIMIT 1
     );

ALTER VIEW system.radar_board_v OWNER TO cobalt_system;

-- ---------------------------------------------------------------------
-- 5. Desk tables, created empty (S3-P0 fills them).
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS system.desk_regime (
    id              BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    as_of           TIMESTAMPTZ NOT NULL,
    snapshot        JSONB NOT NULL,
    snapshot_sha256 TEXT NOT NULL,
    sources         JSONB NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

ALTER TABLE system.desk_regime OWNER TO cobalt_system;

CREATE TABLE IF NOT EXISTS system.desk_packet (
    id                  BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    job_id              BIGINT,
    ticker              TEXT NOT NULL,
    as_of               TIMESTAMPTZ NOT NULL,
    schema_version      TEXT NOT NULL,
    status              TEXT NOT NULL CHECK (status IN ('complete', 'partial', 'failed')),
    packet              JSONB NOT NULL,
    packet_sha256       TEXT NOT NULL,
    input_bundle_sha256 TEXT NOT NULL,
    regime_id           BIGINT REFERENCES system.desk_regime(id),
    formula_version     TEXT NOT NULL,
    expires_at          TIMESTAMPTZ NOT NULL,
    created_at          TIMESTAMPTZ NOT NULL DEFAULT now()
);

ALTER TABLE system.desk_packet OWNER TO cobalt_system;

CREATE TABLE IF NOT EXISTS system.desk_grade (
    id               BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    packet_id        BIGINT NOT NULL REFERENCES system.desk_packet(id),
    factor           TEXT NOT NULL CHECK (factor IN ('catalyst', 'market_alignment', 'sector_alignment')),
    direction        TEXT NOT NULL CHECK (direction IN ('long', 'short')),
    applicable       BOOLEAN NOT NULL,
    na_reason        TEXT,
    baseline         NUMERIC(10, 6),
    analyst_input    SMALLINT,
    cap              SMALLINT,
    unrounded        NUMERIC(10, 6),
    published_grade  SMALLINT CHECK (published_grade BETWEEN 1 AND 10),
    colour           SMALLINT CHECK (colour IN (0, 1, 2)),
    why              TEXT,
    source           TEXT NOT NULL,
    formula_version  TEXT NOT NULL,
    evaluator_sha256 TEXT NOT NULL,
    audit_result     TEXT,
    created_at       TIMESTAMPTZ NOT NULL DEFAULT now()
);

ALTER TABLE system.desk_grade OWNER TO cobalt_system;

-- ---------------------------------------------------------------------
-- 6. Grants. Sequences explicitly (Astra R1-2), not assumed from 0001's
--    default privileges. REFERENCES on radar_score for
--    "user".aset_sizings.radar_score_id, and on radar_score_run for
--    "user".radar_score_receipt.run_id (Astra R3-1).
-- ---------------------------------------------------------------------
GRANT USAGE, SELECT ON SEQUENCE system.radar_score_run_id_seq TO cobalt_system;
GRANT USAGE, SELECT ON SEQUENCE system.radar_score_id_seq TO cobalt_system;
GRANT USAGE, SELECT ON SEQUENCE system.desk_regime_id_seq TO cobalt_system;
GRANT USAGE, SELECT ON SEQUENCE system.desk_packet_id_seq TO cobalt_system;
GRANT USAGE, SELECT ON SEQUENCE system.desk_grade_id_seq TO cobalt_system;

GRANT SELECT, REFERENCES ON system.radar_score TO cobalt_user;
GRANT SELECT, REFERENCES ON system.radar_score_run TO cobalt_user;
GRANT SELECT ON system.radar_board_v TO cobalt_user;
