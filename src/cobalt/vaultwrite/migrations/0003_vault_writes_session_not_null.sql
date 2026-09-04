-- 0003: vault_writes.session NOT NULL. Runs clean on an empty table and
-- on a backfilled one; on a populated table that was never backfilled it
-- CRASHES — which is the intent (fail-loud), and `cobalt session
-- backfill` is the fix it is telling you to run.
ALTER TABLE vault_writes ALTER COLUMN session SET NOT NULL;
