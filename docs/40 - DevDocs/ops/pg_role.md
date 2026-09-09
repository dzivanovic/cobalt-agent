# `ops/pg_role.py`

## What it does
Mints a Postgres LOGIN role **without the password ever being visible**.

Extracted from `ops/mattermost_role_provision.py` on 2026-09-09, when
`cobalt_app` became the second role to need exactly this mechanism.
One-path rule: a second copy of the SCRAM computation is a second chance
to get RFC 5802 subtly wrong, and the failure mode of that is a role
nobody can log in as, discovered at 05:15 on a Monday.

Each provisioning script keeps its own ROLE, key names, `.env` block and
reasoning — those are the parts that differ. The mechanism lives here.

## The two mechanisms that keep the secret invisible
1. **It is never an argument.** Nothing is shelled out to. `psql -c`,
   `docker exec`, `echo >> .env` would each put the value on a command
   line, which on this host means the operator's transcript. The role is
   created over a psycopg connection; `.env` is written with Python
   file I/O.
2. **It is never sent to Postgres either.** `CREATE ROLE ... PASSWORD`
   takes a string literal (a utility statement cannot carry `$1`), so
   rather than settle for client-side quoting of the plaintext this
   computes the **SCRAM-SHA-256 verifier locally** and sends only that.
   The plaintext never crosses the socket, so it cannot reach a server
   log, a wire capture, or `pg_stat_statements` if one is switched on
   later. `sql.Literal` quotes the verifier.

## Why the alphabet is alphanumeric
62 characters, length 32, ~190 bits. Dropping punctuation buys three
real properties: no percent-encoding needed inside a
`postgres://user:pass@host/db` DSN (the `@`-in-password bug class
`cobalt/db.py` documents), Compose cannot interpolate a `$` out of it,
and it is pure ASCII so SASLprep is the identity and the verifier
computed here is the one Postgres would have computed itself.

## `inherit` is the one axis the two callers differ on
Not a style choice. `mattermost` owns its own database and holds its
privileges directly → `INHERIT`. `cobalt_app` holds **nothing** directly
— every privilege comes from membership of `cobalt_system` /
`cobalt_user` / `cobalt_backup` → **`NOINHERIT`**, so a connection that
never calls `SET ROLE` can read nothing at all. That is the whole point
of the role.

## `preflight_env` is add-only
Anything already present in `.env` aborts the run and says which half it
found. Partial state is the dangerous case: **a role that exists with a
password nobody holds is worse than no role at all.** `store_in_vault`
refuses an existing key for the same reason. This mints; it does not
rotate.

## `store_in_vault` — and the fail-loud guard added with it
Storing the value under its key **is** the F19 enrolment:
`cobalt.redact.secrets.load_literals()` walks every vault leaf ≥ 8 chars,
so the copy is the guard entry. There is no separate list to edit, and a
pattern file carrying the value would be the leak it is meant to stop.

Reaching into the old tree's `VaultManager` is the one sanctioned
strangler crossing: the alternative — a second Fernet **writer** in the
new core — would be a duplicate write path to the credential store.

Guard added 2026-09-09: `VaultManager.unlock()` on a **missing** vault
file logs a warning, creates an empty vault in memory and returns
`True`. A run from a checkout that cannot see the vault would therefore
"succeed" and write a brand-new one-key file nothing else reads. This
module refuses instead, and it asks `cobalt.redact.secrets.vault_file()`
which file that is — one answer to "which vault", not two.

## Neighbours
`ops/cobalt_app_role_provision.py`, `ops/mattermost_role_provision.py`,
`src/cobalt/redact/secrets.py`, `src/cobalt/db.py`.
