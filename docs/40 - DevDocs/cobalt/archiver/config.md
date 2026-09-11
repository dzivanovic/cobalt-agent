# `src/cobalt/archiver/config.py`

## What it does
Resolves, reads once, and validates the configured Radar Lists note at
the beginning of an archiver run. It is read-only: no mirror or vault
write occurs. A missing, unreadable, or invalid note raises loudly, with
no YAML or built-in target fallback.

## Key functions/classes
- `ArchiverConfig` — retains the one parsed note and delegates
  `.archive_targets()` / `.backfill_targets(ticker)` directly to
  `cobalt.radar.sources`.
- `ConfigError(RuntimeError)` — the fail-loud, scrubbed error boundary.
- `load_config(note_path=None) -> ArchiverConfig` — resolves the vault
  root plus `radar.yaml`'s `notes.lists` path unless a test supplies a
  `tmp_path`; parses once and exercises both target derivations before
  returning.

## Data flow in/out
**In:** the configured Radar Lists note.
**Out:** a validated `ArchiverConfig`, or a raised `ConfigError`.
Called fresh by `runner.py` at the start of every run — no caching.

## Config it reads
`configs/cobalt/radar.yaml` supplies the relative Lists-note path.
