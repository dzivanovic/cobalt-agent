-- 0023 rollback.
-- COST: every `price_floor` departure loses its reason (`excluded_by`
-- becomes NULL); the row and its `left_at` stay. Only admitted rows ever
-- carry `price_floor` (the runner writes it on an admitted member's
-- LEAVE), so every cleared row still satisfies
-- `entered_at IS NOT NULL OR excluded_by IS NOT NULL`. Then 0004's
-- four-value CHECK is restored under the same name.
-- A no-op when `system.radar_membership` is absent (the 0014–0020 contract).

DO $migration$
BEGIN
    IF to_regclass('system.radar_membership') IS NULL THEN
        RETURN;
    END IF;
    UPDATE system.radar_membership
       SET excluded_by = NULL WHERE excluded_by = 'price_floor' AND entered_at IS NOT NULL;
    ALTER TABLE system.radar_membership DROP CONSTRAINT IF EXISTS radar_membership_excluded_by_check;
    ALTER TABLE system.radar_membership ADD CONSTRAINT radar_membership_excluded_by_check
        CHECK (excluded_by IN ('config_cap', 'not_equity', 'screen_inactive', 'manual'));
END
$migration$;
