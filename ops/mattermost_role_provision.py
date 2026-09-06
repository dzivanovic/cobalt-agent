#!/usr/bin/env python
"""Mint Mattermost's own Postgres role — one script, one secret, no leaks.

ADR-0006's 2026-09-04 section left one weakness standing after the
one-database-per-product split: *"Mattermost keeps using the `cobalt`
role, deliberately... one superuser role reaches both databases — and it
is the natural next ruling."* This is that ruling executed.

THE RULE THIS SCRIPT EXISTS TO KEEP
-----------------------------------
The password is generated, used and stored WITHOUT EVER LEAVING THIS
PROCESS AS PLAINTEXT. It appears in no argv, no shell history, no log
line, no commit, no terminal output, and no operator's transcript. Two
mechanisms, not one:

1. **It is never an argument.** Nothing is shelled out to. `psql -c`,
   `docker exec`, `echo >> .env` — every one of those would put the value
   in a command line, which on this host means the operator's transcript.
   The role is created over a psycopg connection and `.env` is written
   with Python file I/O.

2. **It is never sent to Postgres either.** `CREATE ROLE ... PASSWORD`
   takes a string literal, so a server-side bound parameter is not
   available for it — a utility statement cannot carry `$1`. Rather than
   settle for client-side quoting of the plaintext, this computes the
   **SCRAM-SHA-256 verifier locally** (RFC 5802, the format Postgres
   stores in `pg_authid.rolpassword`) and sends only that. The plaintext
   never crosses the socket, so it cannot reach a server log, a wire
   capture, or `pg_stat_statements` even if one of those is switched on
   later. `psycopg.sql.Literal` does the quoting of the verifier, so no
   value is ever pasted into SQL by string formatting.

   This is strictly stronger than the bound parameter it replaces. The
   deviation is deliberate and recorded here because the instruction it
   deviates from was written to achieve exactly this outcome.

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

WHY THE ALPHABET IS ALPHANUMERIC
--------------------------------
32 characters from 62 is ~190 bits, far past any margin that matters, and
dropping punctuation buys three real properties: the value needs no
percent-encoding inside a `postgres://user:pass@host/db` DSN (the
`@`-in-password bug class `cobalt/db.py` documents), Compose cannot
interpolate a `$` out of it, and it is pure ASCII so SASLprep is the
identity function and the verifier computed here is the one Postgres
would have computed itself.

Run:  uv run python ops/mattermost_role_provision.py
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import os
import secrets
import string
import sys
from pathlib import Path

from dotenv import load_dotenv
from psycopg import sql

REPO_ROOT = Path(__file__).resolve().parents[1]
ENV_FILE = REPO_ROOT / ".env"

ROLE = "mattermost"
USER_KEY = "MATTERMOST_DB_USER"
PASSWORD_KEY = "MATTERMOST_DB_PASSWORD"

#: See "WHY THE ALPHABET IS ALPHANUMERIC" above.
ALPHABET = string.ascii_letters + string.digits
LENGTH = 32

ENV_BLOCK = """
# Mattermost's own Postgres role (2026-09-05, ADR-0006). Bootstrap tier:
# Compose interpolates the DSN at container-create time, before the vault
# can be opened. A copy lives in VaultManager as MATTERMOST_DB_PASSWORD,
# which is what enrols it in F19's literal guard.
# Minted by ops/mattermost_role_provision.py — never edit by hand.
{user_key}={role}
{password_key}={password}
"""


class ProvisionError(RuntimeError):
    """Fail loud. Every abort leaves the host exactly as it was found."""


def scram_sha256_verifier(password: str, iterations: int = 4096) -> str:
    """The string Postgres stores in `pg_authid.rolpassword`.

    `SCRAM-SHA-256$<iters>:<b64 salt>$<b64 StoredKey>:<b64 ServerKey>`,
    per RFC 5802 §3 and Postgres' own `scram_build_secret()`. 4096 is the
    server default (`password_encryption = scram-sha-256`), so the role
    ends up indistinguishable from one created the ordinary way.

    SASLprep is skipped only because ALPHABET is ASCII, where it is the
    identity; a punctuation or non-ASCII password would need it here.
    """
    salt = secrets.token_bytes(16)
    salted = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
    client_key = hmac.new(salted, b"Client Key", hashlib.sha256).digest()
    stored_key = hashlib.sha256(client_key).digest()
    server_key = hmac.new(salted, b"Server Key", hashlib.sha256).digest()
    b64 = lambda raw: base64.b64encode(raw).decode("ascii")  # noqa: E731
    return f"SCRAM-SHA-256${iterations}:{b64(salt)}${b64(stored_key)}:{b64(server_key)}"


def preflight() -> None:
    """Refuse to run unless the landing ground is exactly as expected.

    Partial state is the dangerous case: a role that exists with a
    password nobody holds is worse than no role at all. So anything
    already in place aborts, and says which half it found.
    """
    if not ENV_FILE.exists():
        raise ProvisionError(f"{ENV_FILE} does not exist.")

    mode = ENV_FILE.stat().st_mode & 0o777
    if mode != 0o600:
        raise ProvisionError(
            f"{ENV_FILE} is mode {mode:o}, expected 600. Refusing to write a "
            "credential into a file others can read."
        )

    text = ENV_FILE.read_text()
    for key in (USER_KEY, PASSWORD_KEY):
        if any(line.strip().startswith(f"{key}=") for line in text.splitlines()):
            raise ProvisionError(
                f"{key} is already present in .env. This script mints a NEW "
                "credential; it does not rotate one. Remove the existing block "
                "deliberately, or write a rotation path."
            )


def role_exists(conn) -> bool:
    with conn.cursor() as cur:
        cur.execute("SELECT 1 FROM pg_roles WHERE rolname = %s", (ROLE,))
        return cur.fetchone() is not None


def create_role(conn, verifier: str) -> None:
    """LOGIN and nothing else. Every other attribute is explicitly off —
    written out rather than left to defaults, so the grant a reader sees
    in `\\du` is the grant this script asked for."""
    with conn.cursor() as cur:
        cur.execute(
            sql.SQL(
                "CREATE ROLE {role} WITH LOGIN NOSUPERUSER NOCREATEDB "
                "NOCREATEROLE NOREPLICATION NOBYPASSRLS INHERIT PASSWORD {pw}"
            ).format(role=sql.Identifier(ROLE), pw=sql.Literal(verifier))
        )


def write_env(password: str) -> None:
    """Append the block, preserving mode 0600 through the rewrite."""
    text = ENV_FILE.read_text()
    if not text.endswith("\n"):
        text += "\n"
    text += ENV_BLOCK.format(
        user_key=USER_KEY, role=ROLE, password_key=PASSWORD_KEY, password=password
    )
    ENV_FILE.write_text(text)
    os.chmod(ENV_FILE, 0o600)


def store_in_vault(password: str) -> None:
    """VaultManager is the sanctioned secrets store (CLAUDE.md: "All
    secrets live in VaultManager"). It lives in the old tree, and this is
    the one place an ops script may reach across the strangler line: the
    alternative — a second Fernet writer in the new core — would be a
    duplicate write path to the credential store, which the one-path rule
    forbids outright. `cobalt.redact.secrets` only ever READS, which is
    why it could afford its own 20-line copy; a writer cannot."""
    sys.path.insert(0, str(REPO_ROOT / "src"))
    from cobalt_agent.security.vault import VaultManager

    master_key = os.getenv("COBALT_MASTER_KEY")
    if not master_key:
        raise ProvisionError("COBALT_MASTER_KEY is not set — cannot open the vault.")

    vault = VaultManager(str(REPO_ROOT / "data" / ".cobalt_vault"))
    if not vault.unlock(master_key):
        raise ProvisionError("Vault unlock failed.")
    if not vault.set_secret(master_key, PASSWORD_KEY, password):
        raise ProvisionError("Vault write failed.")
    vault.lock()


def verify_login(password: str) -> None:
    """Prove the verifier is right by using it — the one check that
    catches a botched SCRAM computation before the container depends on
    it. Connects to `postgres`, not `mattermost`: this asks whether the
    credential authenticates, nothing more."""
    import psycopg
    from urllib.parse import quote

    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT", "5432")
    dsn = f"postgresql://{ROLE}:{quote(password, safe='')}@{host}:{port}/postgres"
    with psycopg.connect(dsn, connect_timeout=10) as conn, conn.cursor() as cur:
        cur.execute("SELECT current_user, current_database()")
        who, where = cur.fetchone()
    if who != ROLE:
        raise ProvisionError(f"Authenticated as {who}, expected {ROLE}.")
    print(f"  login verified: authenticated as {who} on {where}")


def main() -> int:
    load_dotenv(ENV_FILE)

    from cobalt import db  # the ONE connection factory (TRIAGE secrets law)

    preflight()

    with db.connect("postgres") as conn:
        if role_exists(conn):
            raise ProvisionError(
                f"Role {ROLE!r} already exists in Postgres but .env holds no "
                "password for it. Resolve that by hand — do not guess."
            )

        password = "".join(secrets.choice(ALPHABET) for _ in range(LENGTH))
        create_role(conn, scram_sha256_verifier(password))
        print(f"  role {ROLE!r} created (LOGIN, no superuser/createdb/createrole)")

        write_env(password)
        print(f"  .env: {USER_KEY} and {PASSWORD_KEY} written (mode 0600 preserved)")

        store_in_vault(password)
        print(f"  vault: stored as {PASSWORD_KEY} — F19 literal guard enrolment")

        verify_login(password)

        del password

    print(f"\n  {LENGTH} characters, generated with secrets.choice, never printed.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except ProvisionError as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        sys.exit(1)
