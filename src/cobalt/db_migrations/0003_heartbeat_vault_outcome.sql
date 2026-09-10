-- 0003: make the heartbeat's vault delivery outcome durable.
--
-- `cobalt_jobs` is system-side by declaration
-- (`db_migrations/placement.py`). These columns belong on that row rather
-- than in `last_result`: operators need to distinguish a healthy deferred
-- write from a failed write without decoding an application-owned JSON blob.
ALTER TABLE system.cobalt_jobs
    ADD COLUMN IF NOT EXISTS vault_outcome TEXT
        CHECK (vault_outcome IS NULL OR vault_outcome IN (
            'written', 'deferred_market_reset', 'failed'
        )),
    ADD COLUMN IF NOT EXISTS vault_reason TEXT;
