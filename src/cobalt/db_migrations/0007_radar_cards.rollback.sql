-- 0007 rollback. COST: deletes every radar-origin card (their transitions,
-- stop edits, dots and taps cascade), every run receipt, and the card
-- columns on the surviving manual rows. Manual cards are untouched.
-- Order (Astra R1-18): views, then radar rows, then dependent tables, then
-- columns and constraints, and only then the old NOT NULLs, which hold
-- once no unsized radar row remains. Take the D1 pg_dump first.

DROP VIEW IF EXISTS "user".shadow_agreement_v;
DROP VIEW IF EXISTS "user".radar_cards_v;

DO $migration$
DECLARE
    deleted INTEGER;
BEGIN
    IF EXISTS (
        SELECT 1 FROM information_schema.columns
         WHERE table_schema = 'user' AND table_name = 'aset_sizings'
           AND column_name = 'origin'
    ) THEN
        DELETE FROM "user".aset_sizings WHERE origin = 'radar';
        GET DIAGNOSTICS deleted = ROW_COUNT;
        IF deleted > 0 THEN
            RAISE NOTICE '0007 reverse deleted % radar-origin card row(s)', deleted;
        END IF;
    END IF;
END
$migration$;

DROP TABLE IF EXISTS "user".radar_score_receipt;
DROP TABLE IF EXISTS "user".card_dot_taps;
DROP TABLE IF EXISTS "user".card_dots;
DROP FUNCTION IF EXISTS "user".refuse_row_update();

DROP INDEX IF EXISTS "user".aset_sizings_one_promoted_radar_card;
DROP INDEX IF EXISTS "user".aset_sizings_one_open_radar_card;

ALTER TABLE "user".aset_sizings
    DROP CONSTRAINT IF EXISTS aset_sizings_radar_provenance,
    DROP CONSTRAINT IF EXISTS aset_sizings_manual_sized,
    DROP COLUMN IF EXISTS promoted_at,
    DROP COLUMN IF EXISTS health,
    DROP COLUMN IF EXISTS settings_sha256,
    DROP COLUMN IF EXISTS tunables_sha256,
    DROP COLUMN IF EXISTS formula_sha256,
    DROP COLUMN IF EXISTS scan_id,
    DROP COLUMN IF EXISTS radar_score_id,
    DROP COLUMN IF EXISTS score_suppressed,
    DROP COLUMN IF EXISTS card_score,
    DROP COLUMN IF EXISTS proximity,
    DROP COLUMN IF EXISTS conviction,
    DROP COLUMN IF EXISTS snap_notice,
    DROP COLUMN IF EXISTS sized_grade,
    DROP COLUMN IF EXISTS tapped_grade,
    DROP COLUMN IF EXISTS proposed_key,
    DROP COLUMN IF EXISTS why,
    DROP COLUMN IF EXISTS expires_at,
    DROP COLUMN IF EXISTS formed_at,
    DROP COLUMN IF EXISTS structural_stop,
    DROP COLUMN IF EXISTS stop_ref,
    DROP COLUMN IF EXISTS trigger_price,
    DROP COLUMN IF EXISTS trigger_type,
    DROP COLUMN IF EXISTS setup_ref,
    DROP COLUMN IF EXISTS trade_def_md5,
    DROP COLUMN IF EXISTS trade_def_slug;

ALTER TABLE "user".aset_sizings
    ALTER COLUMN grade SET NOT NULL,
    ALTER COLUMN risk_budget SET NOT NULL,
    ALTER COLUMN shares SET NOT NULL,
    ALTER COLUMN used_risk SET NOT NULL;
