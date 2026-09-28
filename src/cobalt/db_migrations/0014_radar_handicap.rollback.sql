-- 0014 rollback. COST: drops the three shadow columns — every stored
-- would-be rank since the deploy. Membership rows are otherwise untouched
-- (the proof digest excludes the three). Bounded: exactly these three
-- columns, nothing else. ORDER: the desk removes the `handicap:` block from
-- his note FIRST, then the code revert, then this file.

ALTER TABLE system.radar_membership
    DROP COLUMN IF EXISTS handicap,
    DROP COLUMN IF EXISTS handicap_factor,
    DROP COLUMN IF EXISTS raw_rank;
