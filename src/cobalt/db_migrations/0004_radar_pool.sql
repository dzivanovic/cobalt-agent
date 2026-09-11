-- 0004: radar pool, membership episodes, and account-mode card stamps.
-- ADR-0008 placement: radar tables are system-side; trader/card choices
-- remain on the quoted "user" side. Idempotent when applied repeatedly.

CREATE TABLE IF NOT EXISTS system.radar_pool (
    pool_key         TEXT PRIMARY KEY CHECK (pool_key ~ '^[a-z0-9_]+$'),
    state            TEXT NOT NULL CHECK (state IN (
                         'scanning', 'idle', 'paused_market_reset', 'stopped')),
    degraded         BOOLEAN NOT NULL DEFAULT false,
    degraded_sources JSONB NOT NULL DEFAULT '[]'::jsonb,
    failed_stage     TEXT CHECK (failed_stage IN (
                         'membership', 'pool_row', 'mirror', 'bars')),
    failed_detail    TEXT,
    sources          JSONB NOT NULL DEFAULT '[]'::jsonb,
    session          TEXT NOT NULL,
    cap              INTEGER,
    members          INTEGER NOT NULL,
    last_scan_id     BIGINT,
    last_scan_at     TIMESTAMPTZ,
    last_scan_ms     INTEGER,
    last_poll_at     TIMESTAMPTZ,
    poll_failures    JSONB NOT NULL DEFAULT '[]'::jsonb,
    budget           JSONB,
    updated_at       TIMESTAMPTZ NOT NULL DEFAULT now()
);

ALTER TABLE system.radar_pool OWNER TO cobalt_system;

CREATE TABLE IF NOT EXISTS system.radar_membership (
    id               BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    pool_key         TEXT NOT NULL REFERENCES system.radar_pool(pool_key),
    ticker           TEXT NOT NULL,
    trade_date       DATE NOT NULL,
    first_seen_at    TIMESTAMPTZ NOT NULL,
    entered_at       TIMESTAMPTZ,
    left_at          TIMESTAMPTZ,
    source           TEXT NOT NULL,
    sources          JSONB NOT NULL,
    rank_at_entry    INTEGER,
    last_rank        INTEGER,
    below_cap_streak INTEGER NOT NULL DEFAULT 0 CHECK (below_cap_streak >= 0),
    excluded_by      TEXT CHECK (excluded_by IN (
                         'config_cap', 'not_equity', 'screen_inactive', 'manual')),
    session          TEXT NOT NULL,
    opened_scan_id   BIGINT NOT NULL,
    last_scan_id     BIGINT NOT NULL,
    closed_scan_id   BIGINT,
    CHECK (entered_at IS NOT NULL OR excluded_by IS NOT NULL),
    CHECK (left_at IS NULL OR left_at >= first_seen_at),
    UNIQUE (pool_key, opened_scan_id, ticker)
);

ALTER TABLE system.radar_membership OWNER TO cobalt_system;
CREATE UNIQUE INDEX IF NOT EXISTS radar_membership_one_open
    ON system.radar_membership (pool_key, ticker) WHERE left_at IS NULL;
CREATE INDEX IF NOT EXISTS radar_membership_trade_date_ticker
    ON system.radar_membership (trade_date, ticker);

GRANT SELECT ON system.radar_pool TO cobalt_user;
GRANT SELECT, REFERENCES ON system.radar_membership TO cobalt_user;
GRANT USAGE, SELECT ON SEQUENCE system.radar_membership_id_seq TO cobalt_system;

ALTER TABLE "user".aset_sizings
    ADD COLUMN IF NOT EXISTS account_mode TEXT
        CHECK (account_mode IN ('live', 'sim')),
    ADD COLUMN IF NOT EXISTS pool_member_id BIGINT
        REFERENCES system.radar_membership(id);

ALTER TABLE "user".day_modes
    ADD COLUMN IF NOT EXISTS account_mode TEXT
        CHECK (account_mode IN ('live', 'sim'));

INSERT INTO "user".trader_settings (user_id, key, value, source)
SELECT id, 'aset.account_mode', '"live"'::jsonb, 'db_migration:0004'
FROM "user".traders
ON CONFLICT (user_id, key) DO NOTHING;
