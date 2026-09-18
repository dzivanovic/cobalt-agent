-- 0008: the rank metric's value on membership, and the nightly movers table.
-- S2-P4 STEP-1 (rulings R1, R5). SYSTEM side only (ADR-0008 D2): both are
-- market data, not one trader's choice. Idempotent when applied repeatedly.
--
-- rank_metric/rank_value: the metric that actually ranked the name and its
-- value at the latest scan, written by S1. No backfill (L57): rows from
-- before the deploy stay NULL and render a dash.
ALTER TABLE system.radar_membership
  ADD COLUMN IF NOT EXISTS rank_metric TEXT CHECK (rank_metric IN ('volume','rvol')),
  ADD COLUMN IF NOT EXISTS rank_value  NUMERIC(20,6);

-- movers_daily: the unfiltered top movers the 21:10 replay fetches.
-- Rows are never deleted: a rerun that drops a mover out of the selected
-- set marks it active = false (Astra R1-20/R2-1), so "user".missed.mover_id
-- never loses its target and every prior row keeps its replay inputs.
-- One ACTIVE row per (trade_date, side, ticker); retired rows may repeat.
CREATE TABLE IF NOT EXISTS system.movers_daily (
    id             BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    trade_date     DATE NOT NULL,
    side           TEXT NOT NULL CHECK (side IN ('gainers','losers')),
    rank           INTEGER NOT NULL CHECK (rank >= 1),
    ticker         TEXT NOT NULL,
    change_pct     NUMERIC(10,4) NOT NULL,
    asset_type     TEXT,
    volume         BIGINT,
    rvol           NUMERIC(12,4),
    export_sha256  TEXT NOT NULL,          -- raw CSV bytes (L57)
    fetched_at     TIMESTAMPTZ NOT NULL,
    bars_archived  BOOLEAN NOT NULL DEFAULT false,
    replay_run_id  TEXT NOT NULL,          -- the run that selected this row
    active         BOOLEAN NOT NULL DEFAULT true
);

ALTER TABLE system.movers_daily OWNER TO cobalt_system;
CREATE UNIQUE INDEX IF NOT EXISTS movers_daily_one_active
    ON system.movers_daily (trade_date, side, ticker) WHERE active;
CREATE INDEX IF NOT EXISTS movers_daily_trade_date
    ON system.movers_daily (trade_date);

-- USER reads movers for the benchmark diff and needs REFERENCES for the
-- "user".missed.mover_id foreign key (Astra R1-2).
GRANT SELECT, REFERENCES ON system.movers_daily TO cobalt_user;
GRANT USAGE, SELECT ON SEQUENCE system.movers_daily_id_seq TO cobalt_system;
GRANT SELECT ON SEQUENCE system.movers_daily_id_seq TO cobalt_user;
