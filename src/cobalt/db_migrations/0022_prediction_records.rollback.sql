-- 0022 rollback: removes exactly what 0022_prediction_records.sql adds — the
-- table (its trigger, index and sequence go with it) and the one
-- aset_sizings column. `"user".refuse_row_update()` is 0007's and stays.
-- COST: destructive by design — every prediction record and every stored
-- bar start goes with its table / column. Idempotent.
DROP TABLE IF EXISTS "user".prediction_records;
ALTER TABLE "user".aset_sizings DROP COLUMN IF EXISTS last_price_bar_ts;
