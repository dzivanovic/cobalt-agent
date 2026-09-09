#!/usr/bin/env python
"""Mint Mattermost's own Postgres role — one script, one secret, no leaks.

ADR-0006's 2026-09-04 section left one weakness standing after the
one-database-per-product split: *"Mattermost keeps using the `cobalt`
role, deliberately... one superuser role reaches both databases — and it
is the natural next ruling."* This is that ruling executed.

THE MECHANISM LIVES IN `ops/pg_role.py` (extracted 2026-09-09, when
`cobalt_app` became the second role to need exactly it — one-path rule).
It is unchanged: the password is generated, used and stored WITHOUT EVER
LEAVING THE PROCESS AS PLAINTEXT — never an argv, and never sent to
Postgres either, because the SCRAM-SHA-256 verifier is computed locally
and only that crosses the socket. Read that module for the full reasoning.

WHERE THE SECRET LANDS, AND WHY IN TWO PLACES
---------------------------------------------
* **`.env` — the bootstrap tier.** `.env` holds only what must be
  readable *before* the vault can be opened. Docker Compose interpolates
  `MM_SQLSETTINGS_DATASOURCE` at container-create time, long before any
  Python runs and with no way to ask VaultManager for anything, so the
  value has to be here — exactly as `POSTGRES_PASSWORD` already is.
  `.env` is git-ignored (`.gitignore:1`) and mode 0600; both are checked
  before writing, and the mode is preserved.

* **VaultManager — the system of record, and the F19 enrolment.**
  Storing it as `MATTERMOST_DB_PASSWORD` is what puts the literal behind
  F19's exfiltration guard: `cobalt.redact.secrets.load_literals()` walks
  every vault leaf ≥ 8 chars, so the copy IS the guard entry — there is
  no separate list to edit, and a pattern file that carried the value
  would be the leak it is meant to stop. Belt and braces: the name also
  ends in `PASSWORD`, so F19's `env_assignment_secret` pattern catches
  `MATTERMOST_DB_PASSWORD=...` by name even with the vault locked.

The alphabet, the length and the SCRAM computation: `ops/pg_role.py`.

Run:  uv run python ops/mattermost_role_provision.py
"""

from __future__ import annotations

import sys
from pathlib import Path

from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).resolve().parent))

import pg_role  # noqa: E402  (same directory; the shared mechanism)
from pg_role import ProvisionError  # noqa: E402

ROLE = "mattermost"
USER_KEY = "MATTERMOST_DB_USER"
PASSWORD_KEY = "MATTERMOST_DB_PASSWORD"

ENV_BLOCK = """
# Mattermost's own Postgres role (2026-09-05, ADR-0006). Bootstrap tier:
# Compose interpolates the DSN at container-create time, before the vault
# can be opened. A copy lives in VaultManager as MATTERMOST_DB_PASSWORD,
# which is what enrols it in F19's literal guard.
# Minted by ops/mattermost_role_provision.py — never edit by hand.
{user_key}={role}
{password_key}={password}
"""


def main() -> int:
    load_dotenv(pg_role.ENV_FILE)

    from cobalt import db  # the ONE connection factory (TRIAGE secrets law)

    pg_role.preflight_env((USER_KEY, PASSWORD_KEY))

    # BOOTSTRAP credential (`connect_migration`): CREATE ROLE is a
    # superuser-class act on a shared catalog. Updated 2026-09-09 —
    # `db.connect()` now requires a `side=` and authenticates as
    # `cobalt_app`, which by design cannot create a role.
    with db.connect_migration("postgres") as conn:
        if pg_role.role_exists(conn, ROLE):
            raise ProvisionError(
                f"Role {ROLE!r} already exists in Postgres but .env holds no "
                "password for it. Resolve that by hand — do not guess."
            )

        password = pg_role.generate_password()
        # INHERIT: `mattermost` owns its own database and holds its
        # privileges directly, unlike `cobalt_app`.
        pg_role.create_login_role(
            conn, ROLE, pg_role.scram_sha256_verifier(password), inherit=True
        )
        print(f"  role {ROLE!r} created (LOGIN, no superuser/createdb/createrole)")

        pg_role.append_env_block(
            ENV_BLOCK.format(
                user_key=USER_KEY, role=ROLE, password_key=PASSWORD_KEY, password=password
            )
        )
        print(f"  .env: {USER_KEY} and {PASSWORD_KEY} written (mode 0600 preserved)")

        pg_role.store_in_vault(PASSWORD_KEY, password)
        print(f"  vault: stored as {PASSWORD_KEY} — F19 literal guard enrolment")

        pg_role.verify_login(ROLE, password)

        del password

    print(f"\n  {pg_role.LENGTH} characters, generated with secrets.choice, never printed.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except ProvisionError as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        sys.exit(1)
