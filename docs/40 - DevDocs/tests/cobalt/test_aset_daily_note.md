# `tests/cobalt/test_aset_daily_note.py`

## What it does
Tests the outside-the-repo safety gate, vault-root resolution,
append-only behavior, stub-with-banner creation, and (since iteration 4)
the FILL UPDATE linkage of `daily_note.py`. A `fake_vault` fixture
monkeypatches `resolve_vault_path()` to a pytest `tmp_path` — genuinely
outside the repo tree — so most tests exercise the real safety invariant
without ever touching Dejan's real vault.

**Iteration 4 (2026-08-28):** `make_result()` builds sheet-mode inputs
(`sheet_mode`, `risk_dollars`) instead of `daily_stop`; every
`save_card(...)` call-site updated for its new `(path, when)` return
value; a new `TestFillUpdate` class covers `save_fill_update` and
`format_fill_update_card`.

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
  card; also asserts `save_card`'s returned `when` matches the input and
  that the card body contains `sheet_mode: full`.
- `test_append_only_no_banner_on_existing_note` — two saves in a row:
  second save's content starts with the first's byte-for-byte (append-
  only proof), and the banner appears exactly once (only on creation).
- `test_pre_existing_note_gets_no_banner` — simulates the normal real-
  world case (Dejan's own Obsidian daily-notes plugin already created
  today's note from `5 - Templates/Daily.md`): no banner gets written,
  his existing content survives untouched, the card still appends.
- `TestFillUpdate.test_fill_update_appends_linked_block` — a card is
  saved, then a `FillRecompute` is saved via `save_fill_update` with the
  card's returned timestamp; asserts both land in the same file and the
  FILL UPDATE block's header contains the original card's ISO timestamp
  and the correct `actual_fill`.
- `TestFillUpdate.test_structural_warning_appears_in_note` — a fill far
  enough from the plan to trigger `structural_warning` gets that warning
  text written into the note as a visible `> ⚠️` line.
- `TestFillUpdate.test_fill_update_refuses_inside_repo` — same safety
  gate, exercised through `save_fill_update` this time; deliberately
  targets an already-existing in-repo directory (`tests/cobalt/`) rather
  than creating one, so the "directory missing" check doesn't mask the
  "inside the repo" gate under test.

## Data flow in/out
Writes real files under a `tmp_path`-backed fake vault for every test
except the two `assert_safe_target`-style unit tests (which touch no
filesystem beyond `Path.resolve()`) and `test_fill_update_refuses_inside_repo`
(which raises before ever opening a file). Never touches
`/Users/cobalt/Vault/Think` or writes into the repo's `docs/`.

## Config it reads
None from disk — `make_cfg()` constructs an `AsetConfig` in-memory; the
vault root comes from the monkeypatched `fake_vault` fixture (or
`REPO_ROOT` directly, for the refusal test), not from
`configs/dev/vault.yaml`.
