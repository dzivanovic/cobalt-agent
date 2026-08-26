# `tests/cobalt/test_aset_daily_note.py`

## What it does
Tests the safety gate and append-only behavior of `daily_note.py`
against the **real repo and real git**, not mocks — the whole point of
the gate is that it calls actual `git check-ignore`/`git ls-files`, so
faking those out would test nothing meaningful.

## Key functions/classes (what's covered, not defined)
- `test_gate_refuses_tracked_file` — `assert_safe_target(REPO_ROOT /
  "README.md")` raises (a real tracked file).
- `test_gate_refuses_unignored_untracked_path` — a hypothetical new file
  at the repo root (not ignored, not tracked) also raises — the gate
  requires ignored, not just untracked.
- `test_gate_passes_playground_inbox_path` — a path under `docs/0 -
  Inbox/` passes cleanly (proves the carve-out setup is correct).
- `test_missing_inbox_dir_refuses` — `save_card` refuses rather than
  creating a missing inbox directory.
- `test_append_only_roundtrip_real_gate` — the real integration test:
  saves two cards at different timestamps to a `aset-test-*.md`-pattern
  file (kept out of the way of the real daily note via
  `make_cfg()`'s custom `filename_pattern`), asserts the first save
  creates the `# YYYY-MM-DD` header, the second save's content starts
  with the first save's content byte-for-byte (proves append-only —
  nothing was rewritten), and the header appears exactly once. Cleans
  up the test file in a `finally` block.

## Data flow in/out
Writes a real (test-prefixed) file under `docs/0 - Inbox/` during
`test_append_only_roundtrip_real_gate`, deleted afterward. Runs real
`git` subprocess calls via `assert_safe_target`.

## Config it reads
None from disk — `make_cfg()` constructs an `AsetConfig` in-memory with
a custom `filename_pattern` so this test never touches the real daily
note file.
