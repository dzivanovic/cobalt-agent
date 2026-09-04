# `src/cobalt/devdb.py`

## What it does
The **guarded destructive helper** — RULING 7.1c. Every truncate/drop/
reset in the new core goes through here, and it refuses any database but
`cobalt_dev`.

## Key functions/classes
- `DestructiveRefused(RuntimeError)` — a guard fired; nothing executed.
- `TRUNCATABLE_TABLES = ("aset_sizings", "vault_writes", "vault_overrides")`
- `CONFIRM_FLAG = "--yes-truncate-cobalt-dev"`
- `counts(tables, *, db_name=DEV_DB_NAME) -> dict[str, int]`
- `truncate(tables, *, db_name=DEV_DB_NAME, confirm=False) -> dict[str, tuple[int, int]]`
  — returns `{table: (before, after)}`.

## Three guards, all of which must pass
1. **The database is `cobalt_dev`** —
   `env.assert_destructive_target()`. Hard-coded, NOT keyed on
   `COBALT_ENV`, not overridable by a flag or an env var. A truncate
   typed into a production shell still refuses. `COBALT_ENV` decides
   where the *application* reads and writes; it must never decide where
   a TRUNCATE lands, because that failure mode is unbounded and
   `cobalt_brain` now holds the live trading record.
2. **The table is on the allowlist** — orthogonal to the database
   guard. `bars` (4.5M rows), the memory layer's five pillars and
   Mattermost's 116 tables are out of reach *by name*.
3. **`confirm=True` / `--yes-truncate-cobalt-dev`** is explicit. There
   is deliberately no `--force` that reaches another database.

`counts()` is read-only and guarded identically, so a typo'd database
name cannot even be *inspected* through this tool.

## Data flow in/out
**In:** `.env` (loaded deliberately and visibly, same as `cobalt/cli.py`
— this module has no transitive old-tree import to load it by accident),
CLI args.
**Out:** row counts to stdout; `TRUNCATE ... RESTART IDENTITY`.

`RESTART IDENTITY` is deliberate: after the migration the ids of record
live in `cobalt_brain`, and a dev row reusing one of them would be
actively confusing in forensics.

## Usage
```
uv run python -m cobalt.devdb --list
uv run python -m cobalt.devdb --truncate aset_sizings,vault_writes,vault_overrides --yes-truncate-cobalt-dev
```

## Tests
`tests/cobalt/test_env.py::TestDestructiveGuard` — refuses
`cobalt_brain`, `postgres`, `template1`, `COBALT_DEV`, `cobalt_dev2` and
`""`; allows `cobalt_dev`; refuses from inside a production shell;
refuses a non-allowlisted table; refuses without confirmation; refuses
an empty table list; guards the read path too.

## Field use (2026-09-04)
Performed RULING 7 §2g after the migration was proven:
`aset_sizings 177 -> 0`, `vault_writes 871 -> 0`, `vault_overrides 0 -> 0`.
Both other guards were exercised first and both refused as specified.
