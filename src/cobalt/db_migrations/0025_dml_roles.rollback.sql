-- 0025 rollback — card 2026-10-13 448. THIS DATABASE ONLY: the default
-- privileges, then the table, sequence and schema grants, per side. It never
-- drops a role and never revokes `cobalt_app`'s membership: both are shared-
-- catalog state, and a rollback on `cobalt_dev` (the gate's --down-to 0013)
-- would otherwise cut `cobalt_brain`'s door once 0025 runs there. The roles
-- stay, holding no privilege in this database. A no-op unless both roles exist.
DO $$
BEGIN
    IF (SELECT count(*) FROM pg_roles
        WHERE rolname IN ('cobalt_apply_user', 'cobalt_apply_system')) = 2 THEN
        EXECUTE format(
            'ALTER DEFAULT PRIVILEGES FOR ROLE cobalt_user, %I IN SCHEMA "user" '
            'REVOKE SELECT, INSERT, UPDATE, DELETE ON TABLES FROM cobalt_apply_user', current_user);
        EXECUTE format(
            'ALTER DEFAULT PRIVILEGES FOR ROLE cobalt_user, %I IN SCHEMA "user" '
            'REVOKE USAGE ON SEQUENCES FROM cobalt_apply_user', current_user);
        EXECUTE format(
            'ALTER DEFAULT PRIVILEGES FOR ROLE cobalt_system, %I IN SCHEMA system '
            'REVOKE SELECT, INSERT, UPDATE, DELETE ON TABLES FROM cobalt_apply_system', current_user);
        EXECUTE format(
            'ALTER DEFAULT PRIVILEGES FOR ROLE cobalt_system, %I IN SCHEMA system '
            'REVOKE USAGE ON SEQUENCES FROM cobalt_apply_system', current_user);

        REVOKE SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA "user" FROM cobalt_apply_user;
        REVOKE USAGE ON ALL SEQUENCES IN SCHEMA "user" FROM cobalt_apply_user;
        REVOKE USAGE ON SCHEMA "user" FROM cobalt_apply_user;

        REVOKE SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA system FROM cobalt_apply_system;
        REVOKE USAGE ON ALL SEQUENCES IN SCHEMA system FROM cobalt_apply_system;
        REVOKE USAGE ON SCHEMA system FROM cobalt_apply_system;
    END IF;
END
$$;
