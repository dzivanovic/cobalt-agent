-- 0024 rollback. COST: drops every strike alert record (pushed / shown / DM
-- times and DM results), so `cobalt strike week` loses those days' panel lag
-- and DM lines. The seam rows themselves live in "user".card_transitions and
-- are untouched. Snapshot the table first if its rows must survive.
DROP TABLE IF EXISTS "user".strike_alerts;
