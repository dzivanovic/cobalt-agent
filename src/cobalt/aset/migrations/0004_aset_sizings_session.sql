-- 0004: aset_sizings.session — F1 session clock (Charter §3 F1).
-- Same reasoning as vaultwrite/0002: the session of a card is a calendar
-- question, not a `created_at` question, so it is stamped at write time
-- and backfilled through the resolver, never derived in SQL.
ALTER TABLE aset_sizings ADD COLUMN IF NOT EXISTS session TEXT;
