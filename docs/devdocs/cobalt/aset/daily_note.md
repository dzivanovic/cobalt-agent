# `src/cobalt/aset/daily_note.py`

## What it does
The "Save to Daily Note" writer: appends the current sizing as a
timestamped, fenced markdown block to today's daily note under the
**configured** vault path (currently the `docs/` playground vault —
Dejan's live vault isn't on this machine yet; that migration is a
scheduled design decision). Creates the note on first save of the day;
**append-only forever after** — the file is only ever opened in append
mode, existing content is never read back, modified, or reordered.

The load-bearing piece: a **safety gate** runs before every write. The
target path must be confirmed git-ignored (`git check-ignore -q`) **and**
untracked (`git ls-files --error-unmatch`); either check failing —
including the git subprocess call itself failing — refuses the write
with a loud `DailyNoteRefused`. This is the mechanism that makes it
structurally impossible for this module to ever write something that
could end up committed: vault content must never become committable.

## Key functions/classes
- `DailyNoteRefused(RuntimeError)` — the one error type; raised for a
  failed safety gate, a missing inbox directory, or a git-check failure.
- `target_path(cfg, when) -> Path` — resolves
  `<vault_path>/<inbox_dir>/<when.strftime(filename_pattern)>`,
  resolving a relative `vault_path` against `REPO_ROOT` (imported from
  `config.py`).
- `_git(*args) -> CompletedProcess` — runs `git -C <REPO_ROOT> <args>`,
  10s timeout, output captured (never printed raw).
- `assert_safe_target(path)` — the safety gate itself: raises unless
  `path` is both git-ignored and untracked.
- `format_card(result, when) -> str` — renders the fenced ` ```aset `
  block: ticker, direction, grade (+ %), entry, stop, daily_stop,
  risk_budget, shares, ISO timestamp.
- `save_card(cfg, result, when=None) -> Path` — the entry point. Refuses
  if the inbox directory doesn't exist (never creates vault structure —
  folder policy is a Vault Session decision, not this module's call),
  runs the safety gate, writes a `# YYYY-MM-DD` header only if the file
  is new, then appends the card. Returns the path written.

## Data flow in/out
**In:** an `AsetConfig` (for `daily_note.*` settings) and a
`SizingResult` (from `engine.compute_sizing`, recomputed fresh in
`web.py`'s `/note` handler rather than reusing a persisted row).
**Out:** a `Path` on success (which `web.py` shows in a "Saved" banner),
or a raised `DailyNoteRefused`. Side effect: appends to (or creates) one
file under `docs/0 - Inbox/`.

## Config it reads
`AsetConfig.daily_note` (`vault_path`, `inbox_dir`, `filename_pattern`)
via the `cfg` argument — this module never calls `load_config()` itself,
the caller (`web.py`) does.
