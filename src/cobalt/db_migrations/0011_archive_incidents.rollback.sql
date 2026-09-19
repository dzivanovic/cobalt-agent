-- 0011 rollback. ADDITIVE migration, ADDITIVE rollback: this drops the
-- one table 0011 created (its two indexes and its sequence go with it)
-- and touches no other object.
--
-- COST: every unresolved incident is lost, and with it the heartbeat's
-- reason for being non-green. A target that was WITHHELD for a
-- `restated` difference is still withheld — the condition lives in the
-- vendor's data, not in this table — but nothing on the dashboard says
-- so any more. Read `cobalt archiver incidents` and keep the output
-- before running this.
--
-- Runs FIRST in a `--down-to 0007` reverse (REVERSE is newest-first).

DROP TABLE IF EXISTS system.archive_incidents;
