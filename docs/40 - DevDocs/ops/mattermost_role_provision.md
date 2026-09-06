# `ops/mattermost_role_provision.py`

## What it does
Mints `mattermost`, Mattermost's own Postgres role, in one run: generates
a 32-character password, creates the role with LOGIN and nothing else,
writes `MATTERMOST_DB_USER` / `MATTERMOST_DB_PASSWORD` into `.env`,
stores a copy in VaultManager, and proves the credential by logging in
with it. One-shot — ADR-0006's 2026-09-05 section is the ruling.

The first DevDoc outside `cobalt/` and `tests/`. It is here because
CLAUDE.md's rule is *per `.py` file*, and the tree mirrors the source
path, so `ops/x.py` gets `docs/40 - DevDocs/ops/x.md`.

## The rule the whole file is shaped around
The password never leaves the process as plaintext — no argv, no shell
history, no log line, no commit, no terminal output, no transcript. Two
independent mechanisms:

- **Nothing is shelled out to.** `psql -c "CREATE ROLE … PASSWORD 'x'"`
  and `echo "K=v" >> .env` both put the value in a command line, which on
  this host means the operator's transcript. The role is created over a
  psycopg connection; `.env` is written with Python file I/O.
- **Postgres never receives the plaintext either.** See below.

## Why a SCRAM verifier instead of a bound parameter
`CREATE ROLE … PASSWORD` takes a string literal. A utility statement
cannot carry `$1`, so there is no server-side bind for it — the choice is
client-side quoting of the plaintext, or not sending the plaintext.

`scram_sha256_verifier()` computes what Postgres would have stored
anyway: PBKDF2-HMAC-SHA256 at 4096 iterations over a 16-byte salt, then
`StoredKey` = SHA256(HMAC(salted, "Client Key")) and
`ServerKey` = HMAC(salted, "Server Key"), formatted as
`SCRAM-SHA-256$<iters>:<b64 salt>$<b64 StoredKey>:<b64 ServerKey>`
(RFC 5802 §3; Postgres' `scram_build_secret()`). Only that string is
sent, quoted by `psycopg.sql.Literal`. The plaintext cannot reach a
server log, a wire capture or `pg_stat_statements` even if one of those
is enabled later.

4096 iterations is the server default, so the role is indistinguishable
from one created the ordinary way.

**This math is load-bearing and silent when wrong** — a bad verifier
produces a role that simply cannot log in. `verify_login()` therefore
connects with the plaintext before the script reports success, and the
formula was proven against a live server on a throwaway role first,
including the negative case.

## Why the alphabet is alphanumeric
32 from 62 is ~190 bits, far past what matters, and dropping punctuation
buys three real properties:

- no percent-encoding inside `postgres://user:pass@host/db` — the
  `@`-in-password bug class `cobalt/db.py` documents;
- Compose cannot interpolate a `$` out of it;
- pure ASCII, so SASLprep is the identity and the verifier computed here
  is the one the server would compute.

## Where the secret lands, and why in two places
- **`.env` — the bootstrap tier.** Compose interpolates the DSN at
  container-create time, before any process could open the vault. That is
  the entire membership test for this tier. `.env` is git-ignored
  (`.gitignore:1`) and mode 0600; both are checked before writing and the
  mode is preserved through the rewrite.
- **VaultManager — and F19.** Storing it as `MATTERMOST_DB_PASSWORD` *is*
  the enrolment in F19's literal guard: `cobalt.redact.secrets.
  load_literals()` walks every vault leaf of 8+ chars, so the guard went
  15 → 16 with no list to edit. A pattern file carrying the value would
  be the leak it exists to stop. The name also ends in `PASSWORD`, so
  F19's `env_assignment_secret` pattern catches it by name with the vault
  locked.

## The one strangler crossing, and why it is allowed
`store_in_vault()` imports `cobalt_agent.security.vault.VaultManager`
from the old tree. CLAUDE.md names VaultManager as *the* secrets store;
the alternative — a second Fernet writer in the new core — would be a
duplicate **write** path to the credential store, which the one-path law
forbids outright. `cobalt.redact.secrets` could afford its own 20-line
copy precisely because it only ever READS. A writer cannot.

Everything else goes through sanctioned new-core paths: `cobalt.db`'s
`connect()` is the ONE connection factory (TRIAGE secrets law), so the
`cobalt` DSN is composed from parts and URL-encoded, not assembled here.

## `preflight()` — why it refuses rather than rotates
Partial state is the dangerous case: a role that exists with a password
nobody holds is worse than no role at all. So the script aborts if either
key is already in `.env`, and aborts if the role exists in Postgres while
`.env` holds nothing for it — naming which half it found. It mints; it
does not rotate. A rotation needs its own script and its own container
recreate.

It also refuses to write into a `.env` that is not mode 0600.

## What it does NOT do
No grants, no ownership transfer, no fence, no Compose edit. Those were
run as reviewed SQL and a reviewed diff, not automated — a script that
can reassign ownership is a script that can reassign the wrong thing.
Notably absent, and deliberately: `REASSIGN OWNED`, which also moves
shared objects and would have handed `cobalt_brain` to this role. ADR-0006
(2026-09-05) has the proof and the substitute.

## Run it
```
uv run python ops/mattermost_role_provision.py
```
Output is five lines, none of which contain the credential.
