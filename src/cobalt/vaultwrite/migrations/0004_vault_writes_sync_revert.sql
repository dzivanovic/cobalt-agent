-- 0004: vault_writes.sync_revert_of — telling a SYNC REVERT apart from a
-- human edit (2026-09-09).
--
-- WHAT HAPPENED, and it is the reason this column exists. On 2026-09-09
-- the daily note's `heartbeat` unit was stuck on the 05:54 GREEN block
-- from 06:25 to 08:05. The 06:09 and 06:24 beats wrote RED. At 06:25:54
-- the file was rewritten back to the 05:54 content — Obsidian Sync,
-- carrying a stale copy up from another device. Every beat after that
-- read the reverted text as a HUMAN EDIT (the merge's rule: on-disk
-- differs from the baseline Cobalt last wrote, so a person changed it),
-- let the human win, and recorded overrides 30-34. Cobalt could not
-- write its own status block for an hour and forty minutes, and the
-- audit trail said a human had insisted on it five times.
--
-- The evidence that distinguishes the two is already in this table and
-- was simply never consulted: THE REVERTED TEXT IS BYTE-IDENTICAL TO
-- SOMETHING COBALT ITSELF WROTE EARLIER. A human edit is new text; a
-- sync revert is old text coming back. So the writer now looks the
-- on-disk body up in this unit's recent `unit_after` values, and when it
-- finds it, takes the on-disk text as the merge base (Cobalt's new text
-- wins cleanly, no overrides) and records WHICH write came back here.
--
-- NULLABLE, and null is the ordinary case. A non-null value is the id of
-- the earlier vault_writes row whose output reappeared on disk — so the
-- forensic question "what put this text here" has an answer that is a
-- row id rather than a guess.
--
-- NO FOREIGN KEY, deliberately. `vault_writes` is purged at 30 days by
-- the writer itself; a FK would either block that purge or cascade the
-- reverting row away with the row it points at. The id is a breadcrumb,
-- not a constraint, and a dangling one still says "this was a revert of
-- something older than retention", which is true and worth keeping.
ALTER TABLE vault_writes ADD COLUMN IF NOT EXISTS sync_revert_of INTEGER;

COMMENT ON COLUMN vault_writes.sync_revert_of IS
    'The earlier vault_writes.id whose unit_after reappeared on disk before '
    'this write — a sync revert, not a human edit. NULL for every ordinary '
    'write. No FK: 30-day retention purges the referent.';
