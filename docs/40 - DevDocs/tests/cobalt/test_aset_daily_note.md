# `tests/cobalt/test_aset_daily_note.py`

## What it does
Tests the (now outside-the-repo) safety gate, vault-root resolution,
append-only behavior, and stub-with-banner creation of `daily_note.py`.
A `fake_vault` fixture monkeypatches `resolve_vault_path()` to a pytest
`tmp_path` — genuinely outside the repo tree — so most tests exercise
the real safety invariant without ever touching Dejan's real vault.

## Key functions/classes (what's covered, not defined)
- `test_gate_refuses_a_target_inside_the_repo` —
  `assert_safe_target(REPO_ROOT / "README.md")` raises; a real path,
  real `REPO_ROOT`, no mocking of the check itself.
- `test_gate_passes_a_target_outside_the_repo` — a `tmp_path` target
  passes cleanly.
- `test_target_path_uses_resolved_vault_root` — `target_path` composes
  `<fake_vault>/1 - Trading/1- Daily Notes/2026-08-26.md` correctly.
- `test_missing_daily_notes_dir_refuses` — `save_card` refuses rather
  than creating a missing daily-notes directory.
- `test_unresolvable_vault_refuses` — a `VaultConfigError` from the
  resolver surfaces as `DailyNoteRefused` (callers only need to catch
  one exception type).
- `test_stub_created_with_banner_on_first_save` — a brand-new note gets
  the `# YYYY-MM-DD` header + the "Created by Cobalt" banner before the
  card.
- `test_append_only_no_banner_on_existing_note` — two saves in a row:
  second save's content starts with the first's byte-for-byte (append-
  only proof), and the banner appears exactly once (only on creation).
- `test_pre_existing_note_gets_no_banner` — simulates the normal real-
  world case (Dejan's own Obsidian daily-notes plugin already created
  today's note from `5 - Templates/Daily.md`): no banner gets written,
  his existing content survives untouched, the card still appends.

## Data flow in/out
Writes real files under a `tmp_path`-backed fake vault for every test
except the two `assert_safe_target` unit tests (which touch no
filesystem beyond `Path.resolve()`). Never touches
`/Users/cobalt/Vault/Think` or the repo's `docs/`.

## Config it reads
None from disk — `make_cfg()` constructs an `AsetConfig` in-memory; the
vault root comes from the monkeypatched `fake_vault` fixture, not from
`configs/dev/vault.yaml`.
