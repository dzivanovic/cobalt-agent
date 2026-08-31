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

**NN#16 dev/prod vault split, formalized 2026-08-31.** Before this,
`configs/dev/vault.yaml` pointed straight at the real vault — every
new-core dev/test run (and every ad-hoc `uv run` from a terminal) was
one missing override away from writing into Dejan's actual Obsidian
vault. Now:
- **Dev default** (the committed `configs/dev/vault.yaml` value):
  `~/dev-vault-cobalt` — a skeleton copy, seeded once by hand, NOT
  auto-created or kept in sync:
  - `5 - Templates/{Daily,DRC,Individual Trade Template,TRADE REPORT CARD}.md`
    — copies of the real Templater templates.
  - `1 - Trading/5 - Review/Rules.md` — copy of "THE 12 RULES" (needed
    for `prefill.rules_gen.regenerate_rules_config()` to have something
    real to parse in manual/dev smoke runs; it's Dejan's rule canon,
    not a personal journal entry, so it's in scope for "no personal
    notes").
  - `1 - Trading/1- Daily Notes/`, `1 - Trading/2 - Trades/` — empty
    directories only (so `vault_writer.resolve_target`'s "directory
    must already exist" check passes) — deliberately no populated daily
    notes, no trade notes, no personal content of any kind.
  - Reseed by re-copying from the real vault's `5 - Templates/` and
    `1 - Trading/5 - Review/Rules.md` if either drifts; there's no
    script for this yet (small enough to stay manual).
- **Production** reaches the real vault (`/Users/cobalt/Vault/Think`,
  `PROD_VAULT_PATH_REFERENCE` below — documentation only, never read by
  `resolve_vault_path()` itself) by setting `COBALT_VAULT_PATH`
  explicitly in its own environment: `ops/start_aset.sh` (the ASET
  LaunchAgent's wrapper) and both `ops/com.cobalt.prefill-*.plist`
  files all do this. A bare interactive `uv run` with no override — the
  common case for dev/test work — now defaults to the SAFE dev vault;
  touching the real one always requires a visible, explicit opt-in.

## Key functions/classes
- `VaultConfigError(RuntimeError)` — the one error type for path resolution.
- `VaultWriteRefused(RuntimeError)` — the one error type for the write-safety gate.
- `VaultConfig` — one-field Pydantic model, `obsidian_vault_path: str`.
- `ENV_OVERRIDE = "COBALT_VAULT_PATH"`.
- `PROD_VAULT_PATH_REFERENCE = "/Users/cobalt/Vault/Think"` — documentation
  constant only (see dev/prod split above); nothing in this module reads it.
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
instead if it ever needs to differ per-environment (this is now the
load-bearing mechanism for the whole dev/prod split above, not just a
theoretical escape hatch).
