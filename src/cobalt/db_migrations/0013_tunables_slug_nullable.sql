-- 0013 — "user".tunables.slug becomes NULLABLE (setups one build STEP-2;
-- FINAL §8, R2-3 = B by X20: a sync with one NULL-slug row raised
-- NotNullViolation and rolled the whole transaction back).
--
-- A `global` assumed default (`1 - Trading/Assumed Defaults.md`, unit
-- `tunables:assumed`) belongs to no trade_def, so it stores slug NULL; a
-- per-trade row still stores its slug and keeps the foreign key.
-- `taxonomy/migrations/0001_trade_defs.sql` is untouched: its CREATE TABLE
-- IF NOT EXISTS never re-imposes the constraint on an existing table.
--
-- Idempotent. When the table does not exist yet (a fresh database whose
-- taxonomy store has never run) this is a NOTICE, not an error: the store
-- creates the table later with the 0001 DDL, and the first global assumed
-- row then fails that sync loudly (NotNullViolation) until 0013 is re-run.
DO $migration$
BEGIN
    IF to_regclass('"user".tunables') IS NULL THEN
        RAISE NOTICE '0013: "user".tunables does not exist yet — nothing to alter';
        RETURN;
    END IF;
    ALTER TABLE "user".tunables ALTER COLUMN slug DROP NOT NULL;
END
$migration$;
