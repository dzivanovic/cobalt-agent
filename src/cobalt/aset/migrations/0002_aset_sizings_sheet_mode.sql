-- 0002: aset_sizings — iteration 4 sheet-mode fixed-dollar risk model
-- replaces the daily_stop x grade-percentage model. sheet_mode is
-- nullable so historical rows from before this migration stay readable
-- (they simply have no sheet_mode); daily_stop and risk_pct are dropped
-- outright — one-path rule, the percentage model is retired, not kept
-- around unused.
ALTER TABLE aset_sizings ADD COLUMN IF NOT EXISTS sheet_mode TEXT;
ALTER TABLE aset_sizings DROP COLUMN IF EXISTS daily_stop;
ALTER TABLE aset_sizings DROP COLUMN IF EXISTS risk_pct;
