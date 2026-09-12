-- 0005: positively identified absence of today's note is a benign deferral.
--
-- 0003 owns these columns. This migration changes only its named CHECK and
-- fails rather than dropping a constraint whose definition is not exactly the
-- deployed old domain or this migration's new domain.
DO $migration$
DECLARE
    actual_definition TEXT;
    old_definition CONSTANT TEXT :=
        'CHECK (((vault_outcome IS NULL) OR (vault_outcome = ANY (ARRAY[''written''::text, ''deferred_market_reset''::text, ''failed''::text]))))';
    new_definition CONSTANT TEXT :=
        'CHECK (((vault_outcome IS NULL) OR (vault_outcome = ANY (ARRAY[''written''::text, ''deferred_market_reset''::text, ''deferred_note_absent''::text, ''failed''::text]))))';
BEGIN
    SELECT pg_get_constraintdef(c.oid)
      INTO actual_definition
      FROM pg_constraint AS c
      JOIN pg_class AS t ON t.oid = c.conrelid
      JOIN pg_namespace AS n ON n.oid = t.relnamespace
     WHERE n.nspname = 'system'
       AND t.relname = 'cobalt_jobs'
       AND c.conname = 'cobalt_jobs_vault_outcome_check';

    IF actual_definition IS NULL THEN
        RAISE EXCEPTION '0005 expected constraint system.cobalt_jobs.cobalt_jobs_vault_outcome_check, but it is absent';
    ELSIF actual_definition = new_definition THEN
        RETURN;
    ELSIF actual_definition <> old_definition THEN
        RAISE EXCEPTION '0005 refusing unexpected definition for cobalt_jobs_vault_outcome_check: %', actual_definition;
    END IF;

    ALTER TABLE system.cobalt_jobs
        DROP CONSTRAINT cobalt_jobs_vault_outcome_check;
    ALTER TABLE system.cobalt_jobs
        ADD CONSTRAINT cobalt_jobs_vault_outcome_check
        CHECK (vault_outcome IS NULL OR vault_outcome IN (
            'written', 'deferred_market_reset', 'deferred_note_absent', 'failed'
        ));
END
$migration$;
