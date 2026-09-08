# `src/cobalt/vaultwrite/store.py`

## What it does
`VaultWriteStore` — the LAW L28 audit trail. `vault_writes` holds every
touched section (before + after, plus the unit body that becomes the next
run's merge base, plus full-file hashes); `vault_overrides` holds every
place a human's text beat Cobalt's.

## Key functions/classes
- `ensure_schema()` — runs `migrations/*.sql`.
- `pending_write(...)` — the context manager the writer commits inside, so
  the row and the file land together or neither does.
- `last_after(note, section, unit)` — the baseline for the three-way merge.
- `purge_expired()` — 30-day retention, called by the writer on every run.
- `recent()`, `overrides_for(note)`, `get_write(id)`.

## Retention
`vault_writes` is purged at 30 days. `vault_overrides` is NEVER purged —
an override is a calibration signal about real preferences, not an
operational log.

---

## 2026-09-08 — ADR-0008 (two-layer data model)

Declares `SIDE = Side.USER` (ADR-0008 D2 — the side is chosen PER STORE,
never per process).
The L28 audit trail holds NOTE TEXT, before and after, plus every place a
human's words beat Cobalt's. That is user data outright.

`_connect()` passes it to the factory; `ensure_schema()` asserts the
two-layer schemas exist before running its own DDL, naming
`cobalt db migrate` if they do not.
