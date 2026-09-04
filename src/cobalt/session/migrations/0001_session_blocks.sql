-- 0001: session_blocks — every refusal the market_reset hard block makes.
--
-- WHY A TABLE AND NOT AN IN-MEMORY COUNTER: SPRINT-LADDER §S1 F1 asks
-- for a "log line + heartbeat-visible counter". The writers are separate
-- processes with separate lifetimes (the ASET web app is resident;
-- prefill-daily and prefill-drc are launchd one-shots), so an in-process
-- counter is invisible to the heartbeat by construction. A row per
-- refusal is durable, survives a restart, and answers the heartbeat's
-- question as a `count(*)` over a window (F18, S1-P3) — while doubling
-- as the audit trail of what was refused and by whom.
--
-- This is an APPEND-ONLY record. Nothing updates a row here.
CREATE TABLE IF NOT EXISTS session_blocks (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    ts TIMESTAMPTZ NOT NULL DEFAULT now(),
    session TEXT NOT NULL,
    actor TEXT NOT NULL,      -- the writer/entrypoint that was refused
    target TEXT,              -- note path, ticker, whatever was being written
    reason TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS session_blocks_ts_idx ON session_blocks (ts DESC);
