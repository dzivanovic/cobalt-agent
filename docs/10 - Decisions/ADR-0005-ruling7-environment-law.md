# ADR-0005 — RULING 7: two databases, one resolver, no defaults

Date: 2026-09-04
Status: Accepted
Relates to: ADR-0004 (LAW L28, the one vault write path). Closes the
open item ADR-0004 left explicitly unresolved — *"Production ASET and
prefill write their cards to `cobalt_dev` … the prod/dev database split
itself needs a ruling."*

## Context

`configs/dev/aset.local.yaml:12` said `db_name: cobalt_dev`, and every
caller took it: the production ASET sheet, `prefill daily`, `prefill
drc`, the trade-note writer and the `cobalt vault` CLI all constructed
their stores as `AsetStore(aset_cfg.db_name)` /
`VaultWriteStore(aset_cfg.db_name)`. There was no code path by which a
production process could reach a production database, because there was
no production database — `cobalt_brain` had no `aset_sizings` table at
all.

Three measured consequences, all from the 09-03/09-04 incident thread:

1. **Live trading data and test data shared a table.** 15 stray
   `TEST`/`FORDATE` rows written by `tests/cobalt/test_aset_store.py`
   made `DRC-2026-09-03.md` report "17 cards" when 2 were real.
2. **The production audit trail lived in the dev database.** The whole
   2026-09-04 reconstruction — proving Cobalt wrote the daily note at
   05:15 and Obsidian destroyed it at 06:30 — rested on `vault_writes`
   rows 525-528, sitting in `cobalt_dev` next to pytest temp-vault rows.
3. **The leak was ongoing and unbounded.** One full test run on
   2026-09-04 grew `vault_writes` from 383 to 529: +146 rows into the
   same table production wrote to.

Underneath, the database and the vault disagreed about what "no flag"
meant. `resolve_vault_path()` treated an unset `COBALT_ENV` as dev — the
NN#16-safe default. The database had no such notion: it read
`cobalt_dev` from a config file unconditionally, in every environment.
Two silent defaults, two different answers, and the only thing standing
between production and the dev database was a YAML key nobody read.

## Decision

**`COBALT_ENV` is the ONE resolver, for the database and the vault
alike, and it has no default.**

1. **Two databases, named by the environment, not by config.**
   `COBALT_ENV=production` → `cobalt_brain` + `/Users/cobalt/Vault/Think`.
   `COBALT_ENV=dev` → `cobalt_dev` + `configs/dev/vault.yaml`'s root.
   Unset or unknown raises `EnvConfigError` at boot with a one-line
   message — for the vault exactly as for the database. `cobalt/env.py`
   is the definition of record; `cobalt/vault.py` calls `resolve_env()`
   first and unconditionally.

2. **`db_name` is deleted from `AsetConfig`, not defaulted.** With
   `extra="forbid"`, a leftover `db_name:` key in either config file is
   now a loud crash. `AsetStore` and `VaultWriteStore` take
   `db_name=None` and ask the resolver; the explicit argument survives
   as a test/tooling seam only. **The database is not a per-component
   setting.** That is the specific shape of the bug: a component-level
   knob that a config file could turn for every environment at once.

3. **`db.connect()` gates `cobalt_brain` on a production declaration**
   rather than on an `allow_prod` kwarg that each caller had to
   remember. `allow_prod=True` remains for migration tooling that must
   reach production deliberately without flipping the whole process.

4. **Destructive helpers are hard-coded to `cobalt_dev`.**
   `env.assert_destructive_target()` refuses any other database — not
   read from config, not keyed on `COBALT_ENV`, not overridable by a
   flag. `COBALT_ENV` decides where the *application* reads and writes;
   it must never decide where a TRUNCATE lands, because that failure
   mode is unbounded and `cobalt_brain` now holds the live record.
   `cobalt/devdb.py` adds a second, orthogonal guard: only the three
   tables this ruling migrates may be named, so `bars` (4.5M rows) and
   Mattermost's 116 tables are out of reach by name.

5. **The test suite runs in a transaction that is never committed.**
   `tests/cobalt/conftest.py` pins `COBALT_ENV=dev` and monkeypatches
   `db.connect` to hand out savepoint-scoped proxies over one real
   connection, rolled back per test. Per-test cleanup was the previous
   answer and it is structurally insufficient: it only removes what a
   test remembers to name, it cannot help a test that fails before its
   teardown, and `test_vaultwrite.py` cleaned up at *setup*, so its rows
   survived every run.

6. **Every `ops/` plist declares `COBALT_ENV=production`.** A launcher
   that loses the key now fails loud instead of resolving silently.

## Consequences, and the judgement calls inside them

**The migration copied everything, including the pollution.** Of 871
`vault_writes` rows in `cobalt_dev`, **18 were production** (ids
525-542, under `/Users/cobalt/Vault/Think`) and **853 were pytest
temp-vault rows**. `aset_sizings` was 177 rows, of which roughly 95 are
real cards spanning 2026-08-24 → 09-04 and the rest are
`TEST`/`FORDATE`/`SMOKETEST`/`SMOKEAB`/`TESTHALF`.

The ruling's proof (§2e) demands identical row counts and an identical
md5 over ordered row contents between source and target, so the
migration was an exact copy — and filtering `aset_sizings` would have
meant *guessing* which tickers were tests, interleaved with real cards
across three weeks, with data loss as the cost of guessing wrong. So
`cobalt_brain` now carries 853 pytest rows in `vault_writes`.

**This is logged, not fixed, and it wants its own ruling.** It is not a
data-loss risk and it is bounded — the transaction fixture means no new
test row can reach either database — but a live audit trail that is 98 %
test noise is a poor forensics surface, and the last time test rows were
purged (ids 171-185, 09-03) it was done as an explicitly sanctioned,
counted, transactional delete. The same shape applies here. The rows are
identifiable with certainty by note path (`%pytest-of-cobalt%`).

**`bars` did not move.** 4,563,539 rows are still in `cobalt_dev`, and
the archiver still names its database explicitly rather than asking the
resolver. RULING 7 named three tables; migrating a 4.5M-row table was
not in scope and doing it silently would have been worse. It is a real
inconsistency with "cobalt_dev = dev only" and it is the second item
this ADR hands forward.

**A latent ordering bug surfaced and was fixed.**
`AsetStore.for_date()` ordered by `created_at` alone. `created_at`
defaults to `now()`, which in Postgres is the *transaction* timestamp,
so two cards written inside one transaction tie and the sort between
them was arbitrary — the DRC's re-entry numbering could silently invert.
Now `ORDER BY created_at, id`. The transaction fixture found it; it was
always reachable in production.

**A stale process still predates the flag.** `com.cobalt.agent` was
reloaded and its job now declares `COBALT_ENV=production`, but the
running process (pid 1362, started 09-03 19:02) survived the bootout —
`AbandonProcessGroup` detaches it — and its environment has no
`COBALT_ENV`. This is inert: the old tree imports nothing from
`src/cobalt/` and reads no `COBALT_ENV`. It is the same class as Defect
1 (2026-09-01): env vars are fixed at process launch, and a config
deploy alone cannot fix a live process.

## Alternatives rejected

- **Keep `db_name` in config and just change its value to
  `cobalt_brain` for production.** This is the bug, restated. The
  failure was never the value; it was that a file could set it for every
  environment and nothing downstream could disagree.
- **Filter the migration to production rows only.** Safe and obviously
  right for `vault_writes`, where the note path is decisive.
  Unacceptable for `aset_sizings`, where "is this a test ticker?" is a
  guess and the cost of guessing wrong is deleted trading history. A
  policy that differs per table is worse than one exact copy plus a
  reported follow-up.
- **Delete the pytest rows from `cobalt_brain` after loading them.**
  Leaves the live database clean, but it is an unsanctioned destructive
  operation against production inside a migration session. Precedent
  (09-03, ids 171-185) is that such deletions are proposed, counted, and
  ruled on first.
- **Treat an unset `COBALT_ENV` as dev** (the pre-ruling vault
  behaviour, extended to the database). It is the safe default and it is
  still a default. "Nothing resolves silently to either" is the property
  being bought; a safe silent answer is still a silent answer, and it is
  what let a production process run for six hours against the dev vault
  in the 2026-09-01 defect.

## Follow-ups (not done here)

- **853 pytest `vault_writes` rows in `cobalt_brain`** — needs a
  cleanup ruling (see above).
- **`bars` is still in `cobalt_dev`** and the archiver still passes an
  explicit `db_name`.
- **RULING 6.3c, the heartbeat probe, has no host.** The
  "Obsidian process running" probe is built and tested
  (`src/cobalt/obsidian.py`), and the vault writer reports on it — but
  there is no heartbeat on this machine to turn red. It remains an
  unchecked BACKLOG item, sequenced after slice 2.
- **The production vault still has no backup.** Unchanged by this
  session and still the largest open risk in the incident report.
