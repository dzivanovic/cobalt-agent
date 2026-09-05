-- 0007: aset_sizings.state NOT NULL — "no card exists without a state"
-- (Charter §3 F7's acceptance line) as a database constraint rather than
-- a convention.
--
-- Runs only after `cobalt cards backfill` has stamped every existing
-- row through the state machine and written its genesis transition. On a
-- database with an unbackfilled row this migration FAILS, loudly, which
-- is the intended behaviour: the alternative is a DEFAULT that invents a
-- state for a card nobody classified.
ALTER TABLE aset_sizings ALTER COLUMN state SET NOT NULL;
