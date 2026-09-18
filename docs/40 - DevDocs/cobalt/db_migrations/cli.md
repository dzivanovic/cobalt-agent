# `src/cobalt/db_migrations/cli.py`

S2-P1 requires a rollback bound before connection, selects only newer reverse files, and computes direction-aware verdicts before commit. `CHANGED` always rolls back. Since 2026-09-18 the content proof is STREAMED (no size ceiling) and there is a read-only `--proof-only` mode.

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

## The digest, and why it is not the naive one
`to_jsonb(row)` minus the columns these migrations add, cast to text,
ordered by the primary key read from the catalog. It EXCLUDES `user_id`
and friends because the forward migration adds those columns, so a
whole-row digest would differ by construction and prove nothing.
`to_jsonb` also makes the value independent of column order, which both
`SET SCHEMA` and `ADD COLUMN` touch.

## How the digest is computed now (and why the values did not change)
`_probe` keeps `count(*)` in SQL, and folds the digest HERE:

* `_stream_row_texts` opens a NAMED — therefore server-side — cursor with
  `itersize = PROBE_BATCH_SIZE` (10,000) and yields one row text at a
  time. Unnamed would only move the ceiling from the server into this
  process.
* `_digest_rows` folds them into one `hashlib.md5()`, writing `b"|"`
  BETWEEN rows and never after the last; no rows at all digest `b""`.

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
that by attempting one.

Refused together with `--rollback` / `--down-to` — those exist to apply
things — with a message naming the conflict, before any connection opens.

Preflight it before a deploy window. On production it is under the same
gate as everything else here: `--allow-prod` (or a declared production
environment) is what reaches `cobalt_brain`; read-only does not relax it.

## Timing is a deliverable
The proof runs TWICE inside a resident outage (before and after), so
every run prints what it cost. On `cobalt_dev` (1,043,443 bars)
`bars` probes in ≈5.5 s and the pair costs ≈11 s; production's 8.4M rows
scale that to roughly 45 s per probe, ≈90 s of the outage. Read the
numbers off the run — do not re-derive them from this file.

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
mode would be gone before the first fetch.

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
