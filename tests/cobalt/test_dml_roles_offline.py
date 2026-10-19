"""Migration 0025 `dml_roles`, offline (card 2026-10-13 448 M1): the registry and the text.

No database. The forward and the rollback are read as text with their `--` comment lines
dropped, as `test_tenancy.py` drops them; what the roles may do on `cobalt_dev` is
`test_dml_roles_db.py`'s.
"""

from __future__ import annotations

from cobalt.db_migrations import FORWARD, MIGRATIONS_DIR, REVERSE

SQL = MIGRATIONS_DIR / "0025_dml_roles.sql"
ROLLBACK = MIGRATIONS_DIR / "0025_dml_roles.rollback.sql"


def _code(path) -> str:
    return "\n".join(l for l in path.read_text().splitlines() if not l.strip().startswith("--"))


def test_o1_the_pair_is_registered_last_and_first():
    assert FORWARD[-1].name == "0025_dml_roles.sql"
    assert REVERSE[0].name == "0025_dml_roles.rollback.sql"


def test_o2_the_forward_makes_two_nologin_roles_the_door_and_dml_grants_only():
    code = _code(SQL)
    for want in (
        "CREATE ROLE cobalt_apply_user NOLOGIN",
        "CREATE ROLE cobalt_apply_system NOLOGIN",
        "GRANT cobalt_apply_user, cobalt_apply_system TO cobalt_app",
    ):
        assert want in code, want
    assert code.count("GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA") == 2
    for never in ("OWNER", "USAGE, CREATE", "CREATE ON", "TRUNCATE", "REFERENCES", "TRIGGER",
                  "ALL PRIVILEGES", "DROP"):
        assert never not in code, never


def test_o3_the_rollback_revokes_grants_and_never_a_role_or_a_membership():
    code = _code(ROLLBACK)
    assert "REVOKE" in code
    for never in ("DROP", "REVOKE cobalt_apply_", "CREATE ROLE"):
        assert never not in code, never


def test_o4_the_rollback_revokes_every_grant_the_forward_makes():
    code = _code(ROLLBACK)
    for schema, role in (('"user"', "cobalt_apply_user"), ("system", "cobalt_apply_system")):
        for want in (
            f"REVOKE SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA {schema} FROM {role}",
            f"REVOKE USAGE ON ALL SEQUENCES IN SCHEMA {schema} FROM {role}",
            f"REVOKE USAGE ON SCHEMA {schema} FROM {role}",
            f"REVOKE SELECT, INSERT, UPDATE, DELETE ON TABLES FROM {role}",
            f"REVOKE USAGE ON SEQUENCES FROM {role}",
        ):
            assert want in code, want
