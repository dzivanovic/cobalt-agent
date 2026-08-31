# `src/cobalt/prefill/vault_writer.py`

## What it does
Shared resolve/gate/read/write plumbing for every prefill writer
(daily.py, trade_note.py, drc.py) — one-path rule, no second copy of
the resolve-vault-root → check-target-dir-exists → safety-gate sequence
that `aset/daily_note.py` pioneered. Every write goes through
`cobalt.vault.assert_within_vault` before touching disk.

## Key functions/classes
- `VaultWriteError(RuntimeError)` — the one error type.
- `resolve_target(vault_relative_dir, filename) -> Path` — resolves +
  gate-checks a write target; refuses (does not create) a missing
  parent directory.
- `resolve_dir(vault_relative_dir) -> Path` — resolves a directory for
  read-only listing (drc.py matching trade notes); no existence check,
  callers already tolerate an empty/missing directory.
- `read_if_exists(path) -> str | None`.
- `write_new(path, content)` — refuses to clobber an existing file
  (belt-and-braces alongside the caller's own `read_if_exists` branch).
- `append_block(path, content)` — append-only, never reads for mutation.
- `overwrite(path, content)` — the one legitimate full-rewrite case:
  `trade_note.py` refreshing its own five owned frontmatter keys after
  merging them onto the existing file's content (the merge itself
  happens in the caller, never here).

## Data flow in/out
**In:** `cobalt.vault.resolve_vault_path()` / `assert_within_vault()`.
**Out:** `Path`s, file contents, or a raised `VaultWriteError`/
`VaultConfigError`.

## Config it reads
None directly — delegates vault-path resolution to `cobalt.vault`.
