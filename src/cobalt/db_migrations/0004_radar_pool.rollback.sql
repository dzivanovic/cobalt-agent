-- 0004 rollback. COST: deletes radar membership history and pool state,
-- removes all persisted card account-mode stamps, and deletes the derived
-- radar mirrors. Mirror rows can be rebuilt from notes; history/stamps cannot.
-- Take the plan's pg_dump snapshot before invoking this bounded rollback.

ALTER TABLE "user".aset_sizings
    DROP COLUMN IF EXISTS pool_member_id,
    DROP COLUMN IF EXISTS account_mode;
ALTER TABLE "user".day_modes
    DROP COLUMN IF EXISTS account_mode;

DELETE FROM "user".trader_settings
WHERE (key = 'aset.account_mode' AND source = 'db_migration:0004')
   OR key LIKE 'radar.%';

DROP TABLE IF EXISTS system.radar_membership;
DROP TABLE IF EXISTS system.radar_pool;
