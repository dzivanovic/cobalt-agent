# `src/cobalt/redact/secrets.py`

## What it does
Loads the vault's values into memory so `redact()` can match the ones no
regex can describe — the four username/password rotations from
2026-08-23.

`load_literals(min_length)` returns a `LiteralGuard`:
`available`, `reason`, `names` (vault key names **only**), `items()`
(name, value pairs, longest first).

## The rules it keeps
- values live in memory only, for the life of the process;
- **nothing is ever logged, printed, persisted or returned** — a hit is
  reported by vault key name;
- a **locked vault is not an error**. `COBALT_MASTER_KEY` is absent from
  most environments; the pattern half still runs and this half reports
  itself INACTIVE, so "no literals loaded" is visible rather than
  assumed;
- a decryption failure reports only the exception **type**, never its
  text, which can echo material back.

## Why it does not import the old tree
The strangler rule (CLAUDE.md): the old tree stays untouched and no
new-core module imports it. This reads the same Fernet-encrypted
`data/.cobalt_vault` with the same key in ~20 lines, and never writes —
the same carve-out `cobalt.vault` took from the old resolver.

## `_leaves()`
`MATTERMOST_CREDS` holds a JSON object with a `url` and a `token`, so
entries are flattened: the token is guarded even though its parent entry
is not itself a string.

## Caching
`lru_cache(maxsize=1)`. The alternative is decrypting the vault on every
outbound line, putting the master key through a hot path for no gain.
`reset_cache()` is a test seam; production never calls it.

---

## 2026-09-08 — ADR-0008 (two-layer data model)

The docstring no longer lists the four credential HOSTS. Which services a
trader subscribes to is his, and a list of them in a committed file is
the same leak as a list of his trades (L31 / ADR-0008 D5). The vault
names them; the code does not. The `redact.yaml` pattern VALUES stay —
ESCALATE, because F19 must not depend on the database.
