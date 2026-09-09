"""Minting a Postgres LOGIN role without the password ever being visible.

Extracted from `ops/mattermost_role_provision.py` (2026-09-05) on
2026-09-09, when `cobalt_app` became the second role to need exactly this
mechanism. ONE-PATH RULE: a second copy of the SCRAM computation is a
second chance to get RFC 5802 subtly wrong, and the failure mode of that
is a role nobody can log in as, discovered at 05:15 on a Monday. So the
mechanism lives here and both provisioning scripts import it; each script
keeps its own ROLE, its own key names, its own `.env` block and its own
reasoning, because those are the parts that differ.

THE RULE THIS MODULE EXISTS TO KEEP — the password is generated, used and
stored WITHOUT EVER LEAVING THE PROCESS AS PLAINTEXT. It appears in no
argv, no shell history, no log line, no commit, no terminal output and no
operator's transcript. Two mechanisms, not one:

1. **It is never an argument.** Nothing is shelled out to. `psql -c`,
   `docker exec`, `echo >> .env` would each put the value on a command
   line, which on this host means the operator's transcript. The role is
   created over a psycopg connection and `.env` is written with Python
   file I/O.

2. **It is never sent to Postgres either.** `CREATE ROLE ... PASSWORD`
   takes a string literal — a utility statement cannot carry `$1` — so
   rather than settle for client-side quoting of the plaintext, this
   computes the SCRAM-SHA-256 verifier LOCALLY (the format Postgres
   stores in `pg_authid.rolpassword`) and sends only that. The plaintext
   never crosses the socket, so it cannot reach a server log, a wire
   capture, or `pg_stat_statements` if one is switched on later.
   `psycopg.sql.Literal` quotes the verifier; no value is ever pasted
   into SQL by string formatting.

WHY THE ALPHABET IS ALPHANUMERIC. 32 characters from 62 is ~190 bits, far
past any margin that matters, and dropping punctuation buys three real
properties: the value needs no percent-encoding inside a
`postgres://user:pass@host/db` DSN (the `@`-in-password bug class
`cobalt/db.py` documents), Compose cannot interpolate a `$` out of it,
and it is pure ASCII so SASLprep is the identity function and the
verifier computed here is the one Postgres would have computed itself.
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
from urllib.parse import quote

REPO_ROOT = Path(__file__).resolve().parents[1]
ENV_FILE = REPO_ROOT / ".env"

#: See "WHY THE ALPHABET IS ALPHANUMERIC" above.
ALPHABET = string.ascii_letters + string.digits
LENGTH = 32


class ProvisionError(RuntimeError):
    """Fail loud. Every abort leaves the host exactly as it was found."""


def generate_password(length: int = LENGTH) -> str:
    """`secrets.choice`, never `random`. Returned, never printed."""
    return "".join(secrets.choice(ALPHABET) for _ in range(length))


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


# ---------------------------------------------------------------------
# .env — the bootstrap tier
# ---------------------------------------------------------------------
#
# `.env` holds only what must be readable BEFORE the vault can be opened.
# `POSTGRES_PASSWORD` is there because docker-compose interpolates it at
# container-create time; `MATTERMOST_DB_PASSWORD` because Compose
# interpolates the Mattermost DSN the same way; `COBALT_DB_PASSWORD`
# because `cobalt.db._open()` composes its DSN from the environment and
# a process that could not open the database also could not open a vault
# whose master key it would have had to read from... the database.
#
# `.env` is git-ignored and mode 0600; both are checked before writing,
# and the mode is preserved through the rewrite.


def preflight_env(keys: tuple[str, ...]) -> None:
    """Refuse unless the landing ground is exactly as expected.

    Partial state is the dangerous case: a role that exists with a
    password nobody holds is worse than no role at all. So anything
    already in place aborts, and says which half it found. ADD-ONLY —
    this mints a NEW credential and never rotates one.
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
    for key in keys:
        if any(line.strip().startswith(f"{key}=") for line in text.splitlines()):
            raise ProvisionError(
                f"{key} is already present in .env. This script mints a NEW "
                "credential; it does not rotate one. Remove the existing block "
                "deliberately, or write a rotation path."
            )


def append_env_block(block: str) -> None:
    """Append `block`, preserving mode 0600 through the rewrite."""
    text = ENV_FILE.read_text()
    if not text.endswith("\n"):
        text += "\n"
    ENV_FILE.write_text(text + block)
    os.chmod(ENV_FILE, 0o600)


# ---------------------------------------------------------------------
# Postgres
# ---------------------------------------------------------------------


def role_exists(conn, role: str) -> bool:
    with conn.cursor() as cur:
        cur.execute("SELECT 1 FROM pg_roles WHERE rolname = %s", (role,))
        return cur.fetchone() is not None


def create_login_role(conn, role: str, verifier: str, *, inherit: bool) -> None:
    """LOGIN and nothing else. Every other attribute is explicitly OFF —
    written out rather than left to defaults, so the grant a reader sees
    in `\\du` is the grant this script asked for.

    `inherit` is the one axis that differs between the two callers, and
    it is not a style choice. `mattermost` owns its own database and
    holds its privileges directly, so INHERIT. `cobalt_app` holds NOTHING
    directly — every privilege it has comes from membership of
    `cobalt_system` / `cobalt_user` / `cobalt_backup` — so NOINHERIT, and
    a connection that never calls `SET ROLE` can read nothing at all.
    That is the whole point of the role.
    """
    from psycopg import sql

    with conn.cursor() as cur:
        cur.execute(
            sql.SQL(
                "CREATE ROLE {role} WITH LOGIN NOSUPERUSER NOCREATEDB "
                "NOCREATEROLE NOREPLICATION NOBYPASSRLS " + ("INHERIT" if inherit else "NOINHERIT")
                + " PASSWORD {pw}"
            ).format(role=sql.Identifier(role), pw=sql.Literal(verifier))
        )


def verify_login(role: str, password: str, *, dbname: str = "postgres") -> None:
    """Prove the verifier is right by USING it — the one check that
    catches a botched SCRAM computation before anything depends on it.
    Connects to `postgres` by default: this asks whether the credential
    authenticates, nothing more."""
    import psycopg

    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT", "5432")
    dsn = f"postgresql://{role}:{quote(password, safe='')}@{host}:{port}/{dbname}"
    with psycopg.connect(dsn, connect_timeout=10) as conn, conn.cursor() as cur:
        cur.execute("SELECT current_user, current_database()")
        who, where = cur.fetchone()
    if who != role:
        raise ProvisionError(f"Authenticated as {who}, expected {role}.")
    print(f"  login verified: authenticated as {who} on {where}")


# ---------------------------------------------------------------------
# VaultManager — the system of record, and the F19 enrolment
# ---------------------------------------------------------------------


def store_in_vault(key: str, password: str) -> None:
    """VaultManager is the sanctioned secrets store (CLAUDE.md: "All
    secrets live in VaultManager"), and storing the value under `key` IS
    its F19 enrolment: `cobalt.redact.secrets.load_literals()` walks every
    vault leaf >= 8 chars, so the copy is the guard entry. There is no
    separate list to edit, and a pattern file carrying the value would be
    the leak it is meant to stop.

    It lives in the old tree, and this is the one place an ops script may
    reach across the strangler line: the alternative — a second Fernet
    writer in the new core — would be a duplicate write path to the
    credential store, which the one-path rule forbids outright.
    """
    sys.path.insert(0, str(REPO_ROOT / "src"))
    from cobalt.redact.secrets import VAULT_FILE_ENV, vault_file
    from cobalt_agent.security.vault import VaultManager

    master_key = os.getenv("COBALT_MASTER_KEY")
    if not master_key:
        raise ProvisionError("COBALT_MASTER_KEY is not set — cannot open the vault.")

    # WHICH FILE is `cobalt.redact.secrets`'s answer, not ours — it is the
    # new core's reader of this vault, and two ways to locate one file is
    # one way too many. It also honours `COBALT_VAULT_FILE`, which is what
    # lets a worktree run reach the host's single vault instead of
    # inventing an empty one beside itself.
    path = vault_file()

    # ADDED 2026-09-09. `VaultManager.unlock()` on a MISSING file logs a
    # warning, creates an empty vault in memory and returns True — so a
    # run from a checkout that cannot see the vault would "succeed" and
    # write a brand-new one-key file that no other process reads. That is
    # a plausible-empty artifact; the fail-loud law forbids it, and this
    # is the caller that would have produced it.
    if not path.exists():
        raise ProvisionError(
            f"{path} does not exist. There is ONE vault on this host and this "
            f"checkout cannot see it — a run from here would create a new, empty "
            f"one and store the credential where nothing reads it. Set "
            f"{VAULT_FILE_ENV} to the host's vault before running."
        )

    vault = VaultManager(str(path))
    if not vault.unlock(master_key):
        raise ProvisionError("Vault unlock failed.")
    if key in (vault.list_secrets() or []):
        raise ProvisionError(
            f"vault key {key!r} already exists. ADD-ONLY: this script mints a new "
            "credential and never modifies or rotates one."
        )
    if not vault.set_secret(master_key, key, password):
        raise ProvisionError("Vault write failed.")
    vault.lock()


__all__ = [
    "ALPHABET",
    "ENV_FILE",
    "LENGTH",
    "REPO_ROOT",
    "ProvisionError",
    "append_env_block",
    "create_login_role",
    "generate_password",
    "preflight_env",
    "role_exists",
    "scram_sha256_verifier",
    "store_in_vault",
    "verify_login",
]
