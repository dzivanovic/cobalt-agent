-- Bounded reverse for 0005. 0003's columns and 0004's radar objects stay.
-- Refuse atomically while any row needs the expanded outcome domain.
DO $migration$
DECLARE
    actual_definition TEXT;
    old_definition CONSTANT TEXT :=
        'CHECK (((vault_outcome IS NULL) OR (vault_outcome = ANY (ARRAY[''written''::text, ''deferred_market_reset''::text, ''failed''::text]))))';
    new_definition CONSTANT TEXT :=
        'CHECK (((vault_outcome IS NULL) OR (vault_outcome = ANY (ARRAY[''written''::text, ''deferred_market_reset''::text, ''deferred_note_absent''::text, ''failed''::text]))))';
BEGIN
    IF EXISTS (
        SELECT 1 FROM system.cobalt_jobs
         WHERE vault_outcome = 'deferred_note_absent'
    ) THEN
        RAISE EXCEPTION 'REFUSING 0005 reverse: system.cobalt_jobs contains deferred_note_absent rows';
    END IF;

    SELECT pg_get_constraintdef(c.oid)
      INTO actual_definition
      FROM pg_constraint AS c
      JOIN pg_class AS t ON t.oid = c.conrelid
      JOIN pg_namespace AS n ON n.oid = t.relnamespace
     WHERE n.nspname = 'system'
       AND t.relname = 'cobalt_jobs'
       AND c.conname = 'cobalt_jobs_vault_outcome_check';

    IF actual_definition IS NULL THEN
        RAISE EXCEPTION '0005 reverse expected constraint system.cobalt_jobs.cobalt_jobs_vault_outcome_check, but it is absent';
    ELSIF actual_definition = old_definition THEN
        RETURN;
    ELSIF actual_definition <> new_definition THEN
        RAISE EXCEPTION '0005 reverse refusing unexpected definition for cobalt_jobs_vault_outcome_check: %', actual_definition;
    END IF;

    ALTER TABLE system.cobalt_jobs
        DROP CONSTRAINT cobalt_jobs_vault_outcome_check;
    ALTER TABLE system.cobalt_jobs
        ADD CONSTRAINT cobalt_jobs_vault_outcome_check
        CHECK (vault_outcome IS NULL OR vault_outcome IN (
            'written', 'deferred_market_reset', 'failed'
        ));
END
$migration$;
