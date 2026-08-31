# `src/cobalt/vault.py`

## What it does
The ONE vault-path resolver for the new core (TRIAGE 2.6 ruling — "ONE
resolver; closes CLAUDE.md's OPEN ITEM"). Single source of truth:
`configs/dev/vault.yaml`'s `obsidian_vault_path`, overridable by the
`COBALT_VAULT_PATH` env var. Fail-loud: no config and no env override,
or a resolved path that doesn't exist on disk, both raise
`VaultConfigError` — never a guess.

Deliberately scoped to `src/cobalt/*` only. The old tree's four-way
ambiguity (`.env` `OBSIDIAN_VAULT_PATH` vs `configs/config.yaml` vs
`config.py:69`'s hardcoded default vs `scribe.py`'s own env/~/Documents
fallback) is untouched — the old tree's scribe keeps resolving however
it already does. `COBALT_VAULT_PATH` is a deliberately different env var
name from `OBSIDIAN_VAULT_PATH` specifically so setting it can never
bleed into old-tree behavior.

## Key functions/classes
- `VaultConfigError(RuntimeError)` — the one error type for path resolution.
- `VaultWriteRefused(RuntimeError)` — the one error type for the write-safety gate.
- `VaultConfig` — one-field Pydantic model, `obsidian_vault_path: str`.
- `ENV_OVERRIDE = "COBALT_VAULT_PATH"`.
- `resolve_vault_path() -> Path` — checks the env override first; if
  unset, reads and validates `configs/dev/vault.yaml`. Either way,
  `expanduser()`s the result and requires it to be a real, existing
  directory before returning it `.resolve()`d (symlinks followed, e.g.
  the vault's own `0 - Projects/Cobalt -> .../cobalt/docs` symlink
  doesn't confuse the "outside the repo" check below).
- `assert_within_vault(path)` — **the shared write-safety gate** (added
  Slice 2, extracted from `aset/daily_note.py`'s original private
  `assert_safe_target`, one-path rule): refuses via `VaultWriteRefused`
  unless `path.resolve()` is NOT inside `REPO_ROOT` (the vault lives
  outside the repo by design). `aset/daily_note.py` and every
  `prefill/*` writer (via `prefill/vault_writer.py`) call this instead
  of carrying their own copy.

## Data flow in/out
**In:** `configs/dev/vault.yaml` (committed — the path itself isn't a
secret) or the `COBALT_VAULT_PATH` env var.
**Out:** an absolute, resolved `Path` to the vault root, or a raised
`VaultConfigError`; `assert_within_vault` raises `VaultWriteRefused` or
returns `None`. Consumed by `aset/daily_note.py` and
`prefill/vault_writer.py` (and transitively, everything in
`src/cobalt/prefill/`).

## Config it reads
`configs/dev/vault.yaml` — no local/private variant exists (unlike
`aset.local.yaml`) since the path isn't sensitive; override via env var
instead if it ever needs to differ per-environment.
