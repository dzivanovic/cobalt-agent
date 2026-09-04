-- 0005: aset_sizings.session NOT NULL. See vaultwrite/0003 — a populated,
-- un-backfilled table crashes here on purpose; `cobalt session backfill`
-- is the fix.
ALTER TABLE aset_sizings ALTER COLUMN session SET NOT NULL;
