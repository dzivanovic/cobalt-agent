-- 0001: bars — nightly-archived Finviz intraday bars (Bar Archiver,
-- pre-beta). PK (ticker, interval, ts) makes every insert an idempotent
-- upsert: re-running a night, or backfilling a ticker that already has
-- some bars, never duplicates a row.
--
-- MIGRATION LOG NOTE: this table may be RESHAPED by the data-model ADR
-- (Data-Model + Vault design session), same caveat as aset_sizings.
--
-- Volume/index note: ~280K rows/day at ~185 tier_a names x 5 intervals
-- (+ tier_b's ~25 names x 2 intervals). The composite PK IS a B-tree
-- index on (ticker, interval, ts) — sufficient for both the upsert's
-- lookup and the expected query shape (one ticker+interval's bars over
-- a time range). At this volume (order 10^8 rows/year), Postgres
-- handles a single B-tree PK comfortably; no supplemental index is
-- needed to launch. If a future query pattern needs "all tickers at
-- one interval/timestamp" (e.g. a cross-sectional scan), add a
-- secondary index on (interval, ts) then — not before it's needed.
CREATE TABLE IF NOT EXISTS bars (
    ticker TEXT NOT NULL,
    interval TEXT NOT NULL,
    ts TIMESTAMPTZ NOT NULL,
    open NUMERIC(14, 4) NOT NULL,
    high NUMERIC(14, 4) NOT NULL,
    low NUMERIC(14, 4) NOT NULL,
    close NUMERIC(14, 4) NOT NULL,
    volume BIGINT NOT NULL,
    PRIMARY KEY (ticker, interval, ts)
);
