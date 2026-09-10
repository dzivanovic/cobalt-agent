-- Rollback for 0003_heartbeat_vault_outcome.sql.
--
-- These two nullable columns contain only heartbeat delivery metadata. The
-- previous code cannot read them, so dropping them restores the prior shape.
ALTER TABLE IF EXISTS system.cobalt_jobs
    DROP COLUMN IF EXISTS vault_reason,
    DROP COLUMN IF EXISTS vault_outcome;
