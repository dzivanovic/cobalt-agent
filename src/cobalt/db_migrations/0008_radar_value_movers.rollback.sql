-- 0008 rollback. COST: drops the nightly movers corpus and the rank-metric
-- value columns. Membership rows themselves are untouched (the proof digest
-- excludes the two columns). 0009 must be reversed first: "user".missed
-- references system.movers_daily. Take the plan's pg_dump snapshot first.

DROP TABLE IF EXISTS system.movers_daily;

ALTER TABLE system.radar_membership
    DROP COLUMN IF EXISTS rank_value,
    DROP COLUMN IF EXISTS rank_metric;
