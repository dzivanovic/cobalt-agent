-- 0023_radar_price_floor — the radar's price floor (his R692, card 137).
--
-- An admitted member read at or below `radar.yaml` `price_floor` departs
-- at once with `excluded_by = 'price_floor'` (`RadarRunner._collect`,
-- `decide()`'s excluded-candidate LEAVE). 0004 declared the
-- `excluded_by` CHECK inline with four values, so `price_floor` is
-- refused there. No table is created; the CHECK is widened in place.
--
-- 0004 declared it inline, so its name is read from pg_constraint as 0006
-- does. The table carries a second CHECK naming `excluded_by`
-- (`entered_at IS NOT NULL OR excluded_by IS NOT NULL`); the one widened
-- is the CHECK whose definition holds 'config_cap', and anything but
-- exactly one match raises. IDEMPOTENT: a second run is a no-op.

DO $migration$
DECLARE
    found_count INTEGER;
    found_name TEXT;
    found_definition TEXT;
BEGIN
    SELECT count(*), min(c.conname), min(pg_get_constraintdef(c.oid))
      INTO found_count, found_name, found_definition
      FROM pg_constraint AS c
      JOIN pg_class AS t ON t.oid = c.conrelid
      JOIN pg_namespace AS n ON n.oid = t.relnamespace
     WHERE n.nspname = 'system'
       AND t.relname = 'radar_membership'
       AND c.contype = 'c'
       AND pg_get_constraintdef(c.oid) LIKE '%''config_cap''%';

    IF found_count <> 1 THEN
        RAISE EXCEPTION '0023 expected exactly one excluded_by CHECK on system.radar_membership, found %', found_count;
    END IF;
    IF found_name = 'radar_membership_excluded_by_check'
       AND found_definition LIKE '%''price_floor''%' THEN
        RETURN;
    END IF;
    IF found_definition NOT LIKE '%''not_equity''%'
       OR found_definition NOT LIKE '%''screen_inactive''%'
       OR found_definition NOT LIKE '%''manual''%' THEN
        RAISE EXCEPTION '0023 refusing unexpected excluded_by constraint %: %', found_name, found_definition;
    END IF;

    EXECUTE format('ALTER TABLE system.radar_membership DROP CONSTRAINT %I', found_name);
    ALTER TABLE system.radar_membership ADD CONSTRAINT radar_membership_excluded_by_check
        CHECK (excluded_by IN ('config_cap', 'not_equity', 'screen_inactive', 'manual', 'price_floor'));
END
$migration$;
