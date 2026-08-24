-- 0001: aset_sizings — every computed sizing persists (future EV/Guardian
-- training truth, TRIAGE pre-beta increment 1).
-- MIGRATION LOG NOTE: this table may be RESHAPED by the data-model ADR
-- (Data-Model + Vault design session). Do not build hard dependencies on
-- its shape outside src/cobalt/aset/store.py.
CREATE TABLE IF NOT EXISTS aset_sizings (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    ticker TEXT NOT NULL,
    grade TEXT NOT NULL,
    direction TEXT NOT NULL,
    daily_stop NUMERIC(14, 2) NOT NULL,
    risk_pct NUMERIC(5, 2) NOT NULL,
    risk_budget NUMERIC(14, 2) NOT NULL,
    entry NUMERIC(14, 4) NOT NULL,
    stop NUMERIC(14, 4) NOT NULL,
    per_share_risk NUMERIC(14, 4) NOT NULL,
    shares INTEGER NOT NULL,
    used_risk NUMERIC(14, 2) NOT NULL,
    last_price NUMERIC(14, 4),
    price_source TEXT,
    warnings TEXT[] NOT NULL DEFAULT '{}'
);
