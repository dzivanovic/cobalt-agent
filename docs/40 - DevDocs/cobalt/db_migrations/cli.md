# `src/cobalt/db_migrations/cli.py`

S2-P1 requires a rollback bound before connection, selects only newer reverse files, and computes direction-aware verdicts before commit. `CHANGED` always rolls back. Since 2026-09-18 the content proof is STREAMED (no size ceiling), runs at REPEATABLE READ (one snapshot for both probes), and there is a read-only `--proof-only` mode.

## What it does
`cobalt db migrate [--allow-prod] [--rollback --down-to NNNN] [--proof-only]`.
Runs the migrations and prints a per-table proof: where the table lives,
its row count, a content digest, and what taking the proof cost in wall
seconds — before and after.

## The 2026-09-18 incident, in two lines
The stacked production deploy died in the BEFORE probe with
`ProgramLimitExceeded: out of memory — Cannot enlarge string buffer
containing 1073741677 bytes by 155 more bytes`: the digest was one
server-side `string_agg` over `system.bars`, and production holds
8,410,174 rows. One transaction, rolled back, nothing applied — but the
residents were already down, because there was no way to take the proof
without a migration attached to it.

## The second 2026-09-18 finding, in two lines
The desk read the production `--proof-only` numbers and found the proof
was not snapshot-consistent: `cmd_migrate`'s transaction ran at
Postgres's default READ COMMITTED, where every probe STATEMENT takes its
own snapshot, and the streamed `bars` probe takes ≈46 s each way — so any
commit by any other session inside that ≈100 s window made a GOOD
migration read `CHANGED` and roll back. A deploy only stops the two
residents; `com.cobalt.heartbeat` (every 15 min) and `com.cobalt.seat-usage`
(hourly) keep updating `system.cobalt_jobs`, `cobalt_redactions` drifted
118 → 121 rows in one afternoon on dev, and `vault_writes` grows with any
vault write — roughly a 1-in-6 chance of an outage for nothing per attempt.

## Why the harness runs at REPEATABLE READ
`_connect` sets `conn.isolation_level = IsolationLevel.REPEATABLE_READ`
on both the migrate and the `--proof-only` connection (`--proof-only` is
REPEATABLE READ **and** READ ONLY). The snapshot is taken at the
transaction's first statement, and BOTH probes read THAT snapshot plus
this transaction's OWN changes — so the proof answers exactly the
question it was written for, *"did THIS migration change existing
content?"*, and other sessions' commits are invisible to both probes.
`--proof-only` gains the same property: its whole table is one picture of
the database, not a different snapshot per table.

It is set where the connection is configured, before the first statement,
because psycopg refuses to change the isolation level of a transaction
already in progress and applies the attribute at the next `BEGIN`.
`db.connect_migration` hands back an autocommit connection whose
`SET search_path` / `set_config` have already committed, so nothing is
open yet.

**The price, named and accepted.** If another session commits a change to
a row the migration then modifies, Postgres raises
`could not serialize access due to concurrent update`. `cmd_migrate`
catches `psycopg.errors.SerializationFailure` specifically, rolls back
(the existing `except` path) and raises a `MigrationError` that says what
happened: nothing was applied, something is still writing to a table this
migration touches, stop it and run again. The bare driver text tells an
operator nothing at 20:40 on a deploy, which is why it is wrapped rather
than re-raised. DDL under REPEATABLE READ is unaffected — catalog reads
use their own snapshot, and the dev round trip (`--rollback --down-to
0005` → `migrate`, 8 tables DROPPED then CREATED, every persistent
digest identical) is the standing proof that it works.

### Two designs rejected, and why (the snapshot fix)
* **Exclude the job/telemetry tables from the proof.** A weaker proof —
  `cobalt_jobs`, `cobalt_redactions` and `vault_writes` stop being
  covered at all — and the exclusion list would rot the moment a new
  scheduled writer appears.
* **Stop every scheduled job for a deploy.** A bigger outage surface than
  the two residents, and it still does not cover an ad-hoc writer: a
  session someone opened by hand is not on any launchd list.

## The digest, and why it is not the naive one
`to_jsonb(row)` minus the columns these migrations add, cast to text,
ordered by the primary key read from the catalog. It EXCLUDES `user_id`
and friends because the forward migration adds those columns, so a
whole-row digest would differ by construction and prove nothing.
`to_jsonb` also makes the value independent of column order, which both
`SET SCHEMA` and `ADD COLUMN` touch.

## How the digest is computed now (and why the values did not change)
`_probe` sends ONE statement for the whole proof and folds it HERE:

* `_stream_row_texts` opens a NAMED — therefore server-side — cursor with
  `itersize = PROBE_BATCH_SIZE` (10,000): the server hands the rows over
  a batch at a time, and that batch is what this process buffers — never
  the table, never the concatenation of it. Unnamed would only move the
  ceiling from the server into this process.
* `_digest_rows` folds them into one `hashlib.md5()`, writing `b"|"`
  BETWEEN rows and never after the last; no rows at all digest `b""`. It
  returns `(rows, digest)`: the ROW COUNT IS THE ROWS IT FOLDED.

That last point is review finding F1 (2026-09-18, Grok MAJOR + Gemini
Q5), folded before the re-land. The probe used to run `SELECT count(*)`
and then the digest — two statements, and under READ COMMITTED two
snapshots. On a table being written to, the printed `rows` could belong
to one snapshot and the digest to another (a line that contradicts
itself, or a false `CHANGED`), and `bars` paid for two full passes. One
statement removes both: the pair is self-consistent by construction, and
8.4M rows are read once. The digest VALUES are untouched — the same
bytes in the same order — so the comparability below still holds.

Those are exactly the bytes `string_agg(…, '|' ORDER BY …)` produced
(and `coalesce(…, '')` for the empty case), so **every digest keeps its
old value** and proof tables printed before 2026-09-18 remain comparable.
The suite proves that table by table against the old expression, which
now survives only as the oracle inside `tests/cobalt/test_migrate_proof.py`
— L3: there is no switch, no second code path.

Memory is constant on both sides, so there is no row count at which this
fails.

### Two designs rejected, and why
* **Digest the per-row md5s** (`md5(string_agg(md5(row::text), ''))`).
  Still one server-side string: 32 bytes per row is 269 MB at today's
  8.4M rows and passes 1 GB again near 33M. A later ceiling is still a
  ceiling, and `bars` grows every trading day.
* **Exempt bulk tables** (`bars`) and prove them with `count(*)` +
  `min/max(ts)`. That weakens the proof exactly where the most data
  lives — the one table whose loss would be hardest to notice.

## `--proof-only`
Runs the BEFORE probe over every table the harness knows, prints rows,
the FULL digest (32 characters, not the migrate table's 8 — this output
exists to be carried out of the window and compared later), and per-table
plus total seconds. Applies nothing and exits 0.

It is not merely a code path that declines to write: `_connect(...,
read_only=True)` sets `conn.read_only`, so psycopg opens the transaction
`BEGIN ... READ ONLY` and the SERVER refuses any write. The suite proves
that by attempting one, and asserts both properties at the server
(`SHOW transaction_isolation` = `repeatable read`,
`SHOW transaction_read_only` = `on`) rather than on the Python attributes.

Refused together with `--rollback` / `--down-to` — those exist to apply
things — with a message naming the conflict, before any connection opens.

Preflight it before a deploy window. On production it is under the same
gate as everything else here: `--allow-prod` (or a declared production
environment) is what reaches `cobalt_brain`; read-only does not relax it.

## Timing is a deliverable
The proof runs TWICE inside a resident outage (before and after), so
every run prints what it cost. On `cobalt_dev` (1,043,443 bars) `bars`
probed in ≈5.4 s and the pair costs ≈11 s; the 2026-09-18 production
`--proof-only` run measured `system.bars` at 8,591,339 rows in 46.73 s,
46.9 s for the whole probe, so the BEFORE+AFTER pair is ≈94 s of the
outage. Both figures were measured while `_probe` still ran a separate
`count(*)`; folding F1 removed that pass, so expect the same or less —
read the numbers off the run, never re-derive them from this file.

## Data flow in/out
**In:** `_connect()` → `db.connect_migration()` (no `SET ROLE` — see
`db.md`), the `.sql` files, whole, in one transaction. **Out:** the proof
table; a non-zero exit if any digest changed.

## Gotchas
Each file is handed to the server ENTIRE rather than split on `;`: they
are `DO` blocks, and a splitter would cut them at the first semicolon
inside the body.

`_assert_utf8` runs once per connection. The old aggregate hashed a
server-side text value, whose bytes are in the DATABASE encoding; the
fold hashes `str.encode("utf-8")`. They agree exactly when that encoding
is UTF-8, and would disagree silently on non-ASCII rows otherwise — the
one way this rewrite could lie, so it is checked rather than assumed.

The named cursor needs a transaction: `_connect` turns autocommit off
before anything probes. A `WITHOUT HOLD` cursor declared in autocommit
mode would be gone before the first fetch. The ORDER inside `_connect`
matters: `read_only` and `isolation_level` are set while the connection
is still in autocommit and idle, then autocommit goes off, then
`_assert_utf8` runs the first statement — setting either attribute after
a transaction has opened raises.

`TABLE_DIGEST_EXCLUDED_COLUMNS` (S2-P2) excludes the 25 card columns
that 0007 adds to `aset_sizings`, from THAT table's digest only. It is
per table on purpose: `scan_id` and `why` are real content on other
tables, and a global exclusion would silently drop them from those
digests. The proof line counts them per table.

Running it twice is a no-op. Rollback then re-migrate lands on identical
digests — the suite asserts that round trip on `cobalt_dev`.

There is no `schema_migrations` ledger: `FORWARD` is re-applied in full
every run and every file is idempotent. So "applied nothing" is proven by
the absence of any `-- applying` line and by the relation set being
unchanged, not by a version row.
