# `src/cobalt/session/cli.py`

## What it does
The `cobalt session` command group, mounted by `cobalt/cli.py`:

    cobalt session now [--at ISO8601]
    cobalt session backfill [--dry-run]
    cobalt session blocks [--limit N]

## `now`
Answers the two questions Dejan actually asks at 18:30 on a Thursday —
what session is it, and when does that change — and prints **what makes
the day what it is**, because "overnight" on its own is not an
explanation:

    session   : aftermarket
    clock     : 2026-09-04 18:48:12 EDT  (22:48:12 UTC)
    day       : 2026-09-04 is a full trading day
    next      : market_reset at 2026-09-04 20:00 EDT (in 1h 11m)

Inside the block it adds `STATUS : WRITES BLOCKED`. `--at` requires an
offset — a naive value is refused with the same reasoning as the
resolver's.

## `backfill`
The migration half of the `session` column. The session of an existing
row **cannot be derived in SQL**: it depends on the NYSE calendar, and
the calendar is config. So it is computed here, through the same
resolver every write uses.

Order matters and is the reason the DDL is split across two migrations
per table:

1. run only the migration that ADDS the nullable column
   (`aset/0004`, `vaultwrite/0002`);
2. `SELECT id, <ts_col> WHERE session IS NULL` → `clock.session(ts)` →
   `UPDATE`, all in one transaction, with a post-condition check that no
   NULL survives;
3. commit, then `ensure_schema()` — which now reaches the `SET NOT NULL`
   migrations (`aset/0005`, `vaultwrite/0003`) and applies them cleanly.

`--dry-run` rolls the whole thing back after printing the distribution.

Run 2026-09-04 against both databases: `cobalt_dev` (0 rows, proves the
path), then `cobalt_brain` — 92 `aset_sizings` (rth 80, premarket 11,
aftermarket 1) and 22 `vault_writes` (rth 18, premarket 4).

## `blocks`
Recent `session_blocks` rows, timestamps in ET.

## Gotchas
- `backfill` opens the database with `allow_prod=True` — it is migration
  tooling, which is the exact carve-out `db.connect` keeps for it
  (ADR-0005 §3). It still reads `COBALT_ENV` to decide *which* database,
  and prints it.
- A populated table that has never been backfilled makes **every**
  `ensure_schema()` crash on the `SET NOT NULL`. That is intended
  fail-loud behaviour, and the crash is telling you to run `backfill`.

---

## 2026-09-08 — ADR-0008 (two-layer data model)

`session backfill` targets `aset_sizings` and `vault_writes`, both user
side, so one `side=Side.USER` connection covers it.
