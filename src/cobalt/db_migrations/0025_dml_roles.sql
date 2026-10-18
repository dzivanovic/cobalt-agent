-- 0025: the DML-only apply roles — card 2026-10-13 448 (the 417 D1 follow-up,
-- reports/cto-2026-10-12.md R1268; direction reports/cto-2026-10-13.md R1309).
-- `cobalt db apply` does `SET LOCAL ROLE cobalt_apply_<side>` inside its one
-- transaction (db_apply.APPLY_ROLES), so a statement that slipped past the
-- allowlist still cannot drop, alter, truncate or create: the role may only
-- SELECT, INSERT, UPDATE and DELETE on its own side's tables. Ownership stays
-- with the side roles (0001 sections 3 and 6).
--
-- ROLES AND MEMBERSHIPS ARE CLUSTER-WIDE (as 0001 says of its three roles):
-- running this on `cobalt_dev` creates both roles and `cobalt_app`'s two
-- memberships for the whole server, `cobalt_brain` included, where they hold
-- no privilege until this file runs there. Every GRANT below is per database.
-- The rollback touches only this database: it revokes the grants and the
-- default privileges, never a role, never a membership.
--
-- IDEMPOTENT: the roles are guarded in a DO block; re-granting an existing
-- membership or privilege is a notice, not an error.

-- ---------------------------------------------------------------------
-- 1. The roles. NOLOGIN NOINHERIT and nothing else: a member of no role,
--    so they reach no side role's ownership.
-- ---------------------------------------------------------------------
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'cobalt_apply_user') THEN
        CREATE ROLE cobalt_apply_user NOLOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT NOREPLICATION NOBYPASSRLS;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'cobalt_apply_system') THEN
        CREATE ROLE cobalt_apply_system NOLOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT NOREPLICATION NOBYPASSRLS;
    END IF;
END
$$;

-- ---------------------------------------------------------------------
-- 2. The door. `SET ROLE` is checked against the SESSION user, the
--    application login `cobalt_app` (db.APP_ROLE), so the membership is
--    what lets the verb's SET LOCAL ROLE pass. Named literally, not
--    current_user: this file runs as the bootstrap superuser. A cluster
--    with no `cobalt_app` fails loud here.
-- ---------------------------------------------------------------------
GRANT cobalt_apply_user, cobalt_apply_system TO cobalt_app;

-- ---------------------------------------------------------------------
-- 3. The grants, own schema only: DML on its tables, USAGE on the schema
--    and its sequences. Never schema CREATE, TRUNCATE, REFERENCES,
--    TRIGGER, ownership, or the other side.
-- ---------------------------------------------------------------------
GRANT USAGE ON SCHEMA "user" TO cobalt_apply_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA "user" TO cobalt_apply_user;
GRANT USAGE ON ALL SEQUENCES IN SCHEMA "user" TO cobalt_apply_user;

GRANT USAGE ON SCHEMA system TO cobalt_apply_system;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA system TO cobalt_apply_system;
GRANT USAGE ON ALL SEQUENCES IN SCHEMA system TO cobalt_apply_system;

-- ---------------------------------------------------------------------
-- 4. Default privileges, so a table a store's ensure_schema() creates
--    later under its side role (or the migration login creates) carries
--    the same DML grant. Declared for the same two creators as 0001
--    section 5; DML and USAGE only.
-- ---------------------------------------------------------------------
DO $$
BEGIN
    EXECUTE format(
        'ALTER DEFAULT PRIVILEGES FOR ROLE cobalt_user, %I IN SCHEMA "user" '
        'GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO cobalt_apply_user', current_user);
    EXECUTE format(
        'ALTER DEFAULT PRIVILEGES FOR ROLE cobalt_user, %I IN SCHEMA "user" '
        'GRANT USAGE ON SEQUENCES TO cobalt_apply_user', current_user);
    EXECUTE format(
        'ALTER DEFAULT PRIVILEGES FOR ROLE cobalt_system, %I IN SCHEMA system '
        'GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO cobalt_apply_system', current_user);
    EXECUTE format(
        'ALTER DEFAULT PRIVILEGES FOR ROLE cobalt_system, %I IN SCHEMA system '
        'GRANT USAGE ON SEQUENCES TO cobalt_apply_system', current_user);
END
$$;
