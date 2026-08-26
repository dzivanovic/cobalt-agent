# `src/cobalt/aset/daily_note.py`

## What it does
The "Save to Daily Note" writer: appends the current sizing as a
timestamped, fenced markdown block to today's **real** daily note, under
the vault root resolved by `cobalt.vault.resolve_vault_path()` (never
configured in this module or in `AsetConfig` — that's the one
resolver's job). **Append-only forever** — the file is only ever opened
in append mode, existing content is never read back, modified, or
reordered. If the note doesn't exist yet, a stub is created first, with
a visible banner (`> ⚠️ Created by Cobalt — apply daily template.`) since
Cobalt doesn't apply Dejan's real Obsidian daily-note template — that's
still a manual/Obsidian step.

The load-bearing piece: a **safety gate** runs before every write. Since
the vault-path migration (2026-08-26), the invariant is: the resolved
target's real path must **not** start with the repo root. A target that
resolves inside the repo, or any failure resolving the vault at all,
refuses the write with a loud `DailyNoteRefused`. This replaced the
earlier `git check-ignore`-based gate from when the vault lived inside
the repo at `docs/0 - Inbox/` — the vault is no longer inside the repo
at all, so "inside the repo" is now itself the thing to refuse, not
"not git-ignored."

## Key functions/classes
- `STUB_BANNER` — the exact banner line written into a newly-created note.
- `DailyNoteRefused(RuntimeError)` — the one error type; raised for a
  failed safety gate, an unresolvable vault, or a missing daily-notes
  directory.
- `target_path(cfg, when) -> Path` — resolves the vault root (wrapping
  any `VaultConfigError` into `DailyNoteRefused` — callers only need to
  catch one exception type), then
  `<vault_root>/<daily_notes_dir>/<when.strftime(filename_pattern)>`.
- `assert_safe_target(path)` — the safety gate itself: `path.resolve()`
  vs `REPO_ROOT.resolve()`, refuses if the former is inside the latter
  (via `Path.relative_to` raising `ValueError` on "not a subpath," which
  is the success case here — read the logic close, it inverts on first
  glance).
- `format_card(result, when) -> str` — renders the fenced ` ```aset `
  block: ticker, direction, grade (+ %), entry, stop, daily_stop,
  risk_budget, shares, ISO timestamp. Unchanged by the vault migration.
- `save_card(cfg, result, when=None) -> Path` — the entry point. Refuses
  if the daily-notes directory doesn't exist (never creates vault
  structure — folder policy is a Vault Session decision, not this
  module's call), runs the safety gate, writes `# YYYY-MM-DD` +
  `STUB_BANNER` only if the file is new, then appends the card. On a day
  where Dejan's own workflow already created the note (the normal case —
  his Obsidian daily-notes plugin creates it from `5 - Templates/
  Daily.md` before Cobalt ever runs), no banner is written; the card
  just appends to his real content.

## Data flow in/out
**In:** an `AsetConfig` (for `daily_note.daily_notes_dir` /
`filename_pattern`) and a `SizingResult` (from `engine.compute_sizing`,
recomputed fresh in `web.py`'s `/note` handler rather than reusing a
persisted row). Calls `cobalt.vault.resolve_vault_path()` internally.
**Out:** a `Path` on success (shown in `web.py`'s "Saved" banner), or a
raised `DailyNoteRefused`. Side effect: appends to (or creates) one file
under `<vault_root>/1 - Trading/1- Daily Notes/` — Dejan's real Obsidian
vault, not repo content.

## Config it reads
`AsetConfig.daily_note` via the `cfg` argument (this module never calls
`load_config()` itself — the caller, `web.py`, does) — plus, indirectly,
`configs/dev/vault.yaml` via `cobalt.vault.resolve_vault_path()`.
