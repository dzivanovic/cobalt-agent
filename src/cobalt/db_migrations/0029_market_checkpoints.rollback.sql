-- 0029 rollback. COST: drops every stored checkpoint row (figures, base copies,
-- deltas, narratives), so a past checkpoint can no longer be replayed from the
-- database; the units already in the daily notes are untouched. Snapshot the
-- table first if its rows must survive.
DROP TABLE IF EXISTS system.market_checkpoints;
