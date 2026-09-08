-- 0001: the two-layer data model — schemas, roles, grants, ownership,
-- the tenant table and the tenant GUC convention (ADR-0008 D1, L32).
--
-- WHY TWO SCHEMAS AND NOT TWO DATABASES. Cobalt-the-system is the schema
-- and engine any trader plugs strategies into; everything named after a
-- trade, every setting that is one trader's choice, and every note in
-- `1 - Trading` is USER data and is never shipped to or visible to
-- another Cobalt user. One database keeps a cross-side reference a plain
-- foreign key (S2-P2's `"user".aset_sizings.pool_member_id ->
-- system.radar_membership(id)`); two databases would make it an
-- application-level join with no constraint behind it.
--
-- `user` IS A RESERVED WORD in PostgreSQL 16 (pg_get_keywords catcode R).
-- The name was ruled 09-08 ("user will have more roles and more user
-- settings outside of being trader only"), so it is ALWAYS quoted:
-- `"user"` in every migration, grant, search_path and hand query, and
-- `psycopg.sql.Identifier` in Python. A suite lint test fails on any
-- unquoted `user.` reference under src/cobalt. `system` is unreserved and
-- needs no quoting, but is written the same way for symmetry.
--
-- THE SIDE IS CHOSEN PER STORE, NEVER PER PROCESS. Every store declares
-- `SIDE = Side.USER | Side.SYSTEM` and opens its connections through the
-- one factory, `cobalt.db.connect(dbname, side=...)`, which does
-- `SET ROLE <side role>` and `SET search_path TO <own schema only>` (no
-- `public`). A job that touches both sides holds one connection per side;
-- there is no "both" role. A wrong-side statement fails loud twice over:
-- relation-not-found (search_path) or permission denied (grants).
--
-- OWNERSHIP, NOT JUST GRANTS. Each schema and every new-core table is
-- OWNED by its side role. Ownership is not a grant: leaving the login
-- role as owner would leak every privilege back to it and the per-store
-- enforcement would be decorative.
--
-- KNOWN LIMIT, ruled and split (ADR-0008 D1 Revision 2). The login role
-- is still the docker superuser, and a superuser bypasses every grant
-- check. After the factory's SET ROLE the session's CURRENT role is a
-- non-superuser and the grants bite, so per-store enforcement is real —
-- but a connection that skips the factory keeps full power. The closure
-- is a non-superuser `cobalt_app` LOGIN role, owed as its own ops prompt:
-- no credential change rides inside a data-model migration.
--
-- THE TENANT GUC CONVENTION. Every user-side table carries
-- `user_id INTEGER NOT NULL REFERENCES "user".traders(id)` with
-- `DEFAULT current_setting('cobalt.trader_id')::int` (added by 0002).
-- The factory sets that GUC, session-scoped, from
-- `configs/cobalt/tenant.yaml` (`trader_id: 1` — which local trader this
-- install serves). There is NO literal default anywhere: a connection
-- that did not pass through the factory has no GUC and every INSERT into
-- a user-side table fails loud.
--
-- IDEMPOTENT. Every statement is IF NOT EXISTS or guarded in a DO block:
-- this file must run twice cleanly, and `cobalt db migrate` runs it
-- before 0002 on every invocation.
--
-- ROLES ARE CLUSTER-WIDE. CREATE ROLE is a shared-catalog operation, so
-- running this migration on `cobalt_dev` creates the three roles for the
-- whole cluster (`cobalt_brain` included). That is harmless and
-- deliberate: all three are NOLOGIN, and every privilege they hold is a
-- per-database grant made by this file in the database it ran against.

-- ---------------------------------------------------------------------
-- 1. Schemas
-- ---------------------------------------------------------------------
CREATE SCHEMA IF NOT EXISTS system;
CREATE SCHEMA IF NOT EXISTS "user";

-- ---------------------------------------------------------------------
-- 2. Roles. NOLOGIN: nothing authenticates as these, the factory SET
--    ROLEs into them. `cobalt_backup` is a member of pg_read_all_data
--    (PG14+) so `pg_dump --role=cobalt_backup` can read both sides
--    without owning either.
-- ---------------------------------------------------------------------
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'cobalt_system') THEN
        CREATE ROLE cobalt_system NOLOGIN;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'cobalt_user') THEN
        CREATE ROLE cobalt_user NOLOGIN;
    END IF;
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'cobalt_backup') THEN
        CREATE ROLE cobalt_backup NOLOGIN;
    END IF;
END
$$;

GRANT pg_read_all_data TO cobalt_backup;

-- The login role must be able to SET ROLE into all three. `current_user`
-- rather than a hard-coded name: the login role is `cobalt` today and
-- becomes `cobalt_app` when D1's ops prompt lands, and this file must not
-- have to change for that.
DO $$
BEGIN
    EXECUTE format('GRANT cobalt_system, cobalt_user, cobalt_backup TO %I', current_user);
END
$$;

-- ---------------------------------------------------------------------
-- 3. Ownership. The schema belongs to its side role.
-- ---------------------------------------------------------------------
ALTER SCHEMA system OWNER TO cobalt_system;
ALTER SCHEMA "user" OWNER TO cobalt_user;

-- ---------------------------------------------------------------------
-- 4. Grants.
--    cobalt_system : ALL on system, NOTHING on "user" (system never
--                    reads user data — that is the whole law).
--    cobalt_user   : ALL on "user", USAGE + SELECT on system (a user-side
--                    job reads bars and radar membership; it never
--                    writes them).
--    cobalt_backup : reads everything via pg_read_all_data; it still
--                    needs USAGE on the schemas to name the tables.
-- ---------------------------------------------------------------------
GRANT USAGE, CREATE ON SCHEMA system TO cobalt_system;
GRANT ALL ON ALL TABLES IN SCHEMA system TO cobalt_system;
GRANT ALL ON ALL SEQUENCES IN SCHEMA system TO cobalt_system;

GRANT USAGE, CREATE ON SCHEMA "user" TO cobalt_user;
GRANT ALL ON ALL TABLES IN SCHEMA "user" TO cobalt_user;
GRANT ALL ON ALL SEQUENCES IN SCHEMA "user" TO cobalt_user;

GRANT USAGE ON SCHEMA system TO cobalt_user;
GRANT SELECT ON ALL TABLES IN SCHEMA system TO cobalt_user;
GRANT SELECT ON ALL SEQUENCES IN SCHEMA system TO cobalt_user;

GRANT USAGE ON SCHEMA system, "user" TO cobalt_backup;

-- Said out loud rather than left implicit: the system side has no reach
-- into the user side, and neither side is open to PUBLIC.
REVOKE ALL ON SCHEMA "user" FROM cobalt_system;
REVOKE ALL ON SCHEMA "user", system FROM PUBLIC;

-- ---------------------------------------------------------------------
-- 5. Default privileges, so a table created LATER inherits the same
--    grants without anyone remembering to re-run a GRANT. Declared for
--    every role that can create in these schemas: the side role itself
--    (a store's `ensure_schema()` creates its tables after SET ROLE) and
--    the login role (the migration harness).
-- ---------------------------------------------------------------------
DO $$
BEGIN
    EXECUTE format(
        'ALTER DEFAULT PRIVILEGES FOR ROLE cobalt_system, %I IN SCHEMA system '
        'GRANT ALL ON TABLES TO cobalt_system', current_user);
    EXECUTE format(
        'ALTER DEFAULT PRIVILEGES FOR ROLE cobalt_system, %I IN SCHEMA system '
        'GRANT ALL ON SEQUENCES TO cobalt_system', current_user);
    EXECUTE format(
        'ALTER DEFAULT PRIVILEGES FOR ROLE cobalt_system, %I IN SCHEMA system '
        'GRANT SELECT ON TABLES TO cobalt_user', current_user);
    EXECUTE format(
        'ALTER DEFAULT PRIVILEGES FOR ROLE cobalt_system, %I IN SCHEMA system '
        'GRANT SELECT ON SEQUENCES TO cobalt_user', current_user);
    EXECUTE format(
        'ALTER DEFAULT PRIVILEGES FOR ROLE cobalt_user, %I IN SCHEMA "user" '
        'GRANT ALL ON TABLES TO cobalt_user', current_user);
    EXECUTE format(
        'ALTER DEFAULT PRIVILEGES FOR ROLE cobalt_user, %I IN SCHEMA "user" '
        'GRANT ALL ON SEQUENCES TO cobalt_user', current_user);
END
$$;

-- ---------------------------------------------------------------------
-- 6. The tenant table. `handle`, not a name: the product installs empty
--    and the seed row says only that there is one local trader.
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS "user".traders (
    id         INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    handle     TEXT NOT NULL UNIQUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

ALTER TABLE "user".traders OWNER TO cobalt_user;

INSERT INTO "user".traders (id, handle) VALUES (1, 'primary')
    ON CONFLICT (id) DO NOTHING;

-- Keep the identity sequence ahead of the seeded id, so a second trader
-- inserted without an explicit id does not collide with row 1.
SELECT setval(
    pg_get_serial_sequence('"user".traders', 'id'),
    GREATEST((SELECT max(id) FROM "user".traders), 1)
);
