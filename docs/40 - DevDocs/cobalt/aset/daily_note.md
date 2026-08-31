# `src/cobalt/aset/daily_note.py`

## What it does
The daily-note writer: appends timestamped, fenced markdown blocks to
today's **real** daily note, under the vault root resolved by
`cobalt.vault.resolve_vault_path()` (never configured in this module or
in `AsetConfig` — that's the one resolver's job). **Append-only
forever** — files are only ever opened in append mode, existing content
is never read back, modified, or reordered. If the note doesn't exist
yet, a stub is created first, with a visible banner
(`> ⚠️ Created by Cobalt — apply daily template.`) since Cobalt doesn't
apply Dejan's real Obsidian daily-note template — that's still a
manual/Obsidian step.

The load-bearing piece: a **safety gate** runs before every write. The
resolved target's real path must **not** start with the repo root. A
target that resolves inside the repo, or any failure resolving the
vault at all, refuses the write with a loud `DailyNoteRefused`.

**Iteration 4 (2026-08-28, ruled by Dejan):** "Compute & persist" now
appends the card in the *same* action as the Postgres save — there is
no more separate "Save to Daily Note" step (a card that isn't in the
journal didn't happen; the second click was forgotten twice in one
session, per Dejan's live finding). `save_card` now returns
`(path, when)` instead of just `path` — `when` is the canonical card
timestamp, threaded forward by `web.py` into a hidden `orig_timestamp`
form field so a later actual-fill entry can link back to the exact card
it recomputes. A new `save_fill_update` appends a **FILL UPDATE** block
instead of mutating the original card — both stay in the audit trail,
linked by that timestamp. `format_card` drops the retired `grade (%)`/
`daily_stop` lines and gains a `sheet_mode` line.

## Key functions/classes
- `STUB_BANNER` — the exact banner line written into a newly-created note.
- `DailyNoteRefused(RuntimeError)` — the one error type; raised for a
  failed safety gate, an unresolvable vault, or a missing daily-notes
  directory.
- `target_path(cfg, when) -> Path` — resolves the vault root (wrapping
  any `VaultConfigError` into `DailyNoteRefused` — callers only need to
  catch one exception type), then
  `<vault_root>/<daily_notes_dir>/<when.strftime(filename_pattern)>`.
- `assert_safe_target(path)` — **(Slice 2 refactor)** now a thin wrapper
  over the shared gate, `cobalt.vault.assert_within_vault` (one-path
  rule — the actual "inside the repo" check moved there so
  `prefill/*`'s writers reuse it too); catches `VaultWriteRefused` and
  re-raises as `DailyNoteRefused` so existing callers/tests (which
  depend on that specific exception type) are unaffected. Behavior is
  byte-identical to the pre-refactor version.
- `format_card(result, when) -> str` — renders the fenced ` ```aset `
  block: ticker, direction, grade, `sheet_mode`, entry, stop,
  risk_budget, shares, ISO timestamp.
- `format_fill_update_card(fill, when, orig_timestamp) -> str` — renders
  the fenced ` ```aset-fill ` block: ticker, `orig_timestamp` (linking
  back to the original card), actual fill, stop, planned vs. recomputed
  shares, share delta, recomputed used risk, distance-change %, ISO
  timestamp — plus a visible `> ⚠️` line if `fill.structural_warning` is
  set.
- `_append(cfg, when, body)` — shared private helper: resolves the
  target, refuses if the daily-notes directory doesn't exist (never
  creates vault structure — folder policy is a Vault Session decision,
  not this module's call), runs the safety gate, writes `# YYYY-MM-DD` +
  `STUB_BANNER` only if the file is new, then appends `body`.
- `save_card(cfg, result, when=None) -> (Path, datetime)` — the entry
  point for a fresh sizing card. Returns the canonical `when` alongside
  the path so the caller can carry it forward for fill linkage.
- `save_fill_update(cfg, fill, orig_timestamp, when=None) -> Path` — the
  entry point for a FILL UPDATE block. Targets the note for `when`
  (today by default), not the original card's date — cross-day fills
  are expected to be rare but not refused.

## Data flow in/out
**In:** an `AsetConfig` (for `daily_note.daily_notes_dir` /
`filename_pattern`); a `SizingResult` (`save_card`) or a `FillRecompute`
+ the original card's timestamp (`save_fill_update`), both from
`engine.py`, recomputed fresh in `web.py`'s `/size` and `/fill`
handlers rather than reusing a persisted row. Calls
`cobalt.vault.resolve_vault_path()` internally.
**Out:** `(Path, datetime)` or `Path` on success, or a raised
`DailyNoteRefused`. Side effect: appends to (or creates) one file under
`<vault_root>/1 - Trading/1- Daily Notes/` — Dejan's real Obsidian
vault, not repo content.

## Config it reads
`AsetConfig.daily_note` via the `cfg` argument (this module never calls
`load_config()` itself — the caller, `web.py`, does) — plus, indirectly,
`configs/dev/vault.yaml` via `cobalt.vault.resolve_vault_path()`.
