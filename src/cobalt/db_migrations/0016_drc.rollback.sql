-- 0016 rollback. COST: drops every DRC import record, every stored
-- execution and every derived DRC row. The dropped files themselves live
-- in the vault's `_imports/drc/<date>/` and are untouched; re-importing
-- them rebuilds all three tables. Children first (FKs).

DROP TABLE IF EXISTS "user".drc_rows;
DROP TABLE IF EXISTS "user".drc_fills;
DROP TABLE IF EXISTS "user".drc_imports;
