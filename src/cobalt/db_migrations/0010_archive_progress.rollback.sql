-- 0010 rollback. ADDITIVE migration, ADDITIVE rollback: this drops the
-- one table 0010 created and touches no other object. `system.bars` is
-- not read, not written and not altered here.
--
-- COST: every target's `archived_through` is lost, so the next `append`
-- night BOOTSTRAPS each target again (compare + DO NOTHING over the whole
-- available export, §4). No stored bar is affected — a bootstrap writes
-- nothing that is already there, it only re-reads. The run report says
-- `bootstrap` and states that history before the export's bounds is
-- UNASSESSED.
--
-- Run after 0011's rollback; `--down-to 0007` does both in REVERSE order
-- in one invocation.

DROP TABLE IF EXISTS system.archive_progress;
