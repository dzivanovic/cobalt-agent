# `src/cobalt/db_migrations/cli.py`

S2-P1 requires a rollback bound before connection, selects only newer reverse files, and computes direction-aware verdicts before commit. `CHANGED` always rolls back. Since 2026-09-18 the content proof is STREAMED (no size ceiling), runs at REPEATABLE READ (one snapshot for both probes), and there is a read-only `--proof-only` mode. Since 2026-09-19 (the tribunal's round 1) an ambiguous table name is REFUSED rather than resolved, and what `OK` means is written down rather than inferred.

## What it does
`cobalt db migrate [--allow-prod] [--rollback --down-to NNNN] [--proof-only] [--lock-timeout-s N]`.
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
than re-raised. The dev round trip (`--rollback --down-to 0005` →
`migrate`, 8 tables DROPPED then CREATED, every persistent digest
identical) is the standing proof that DDL commits under this isolation
level at all.

**DDL after a concurrent commit, MEASURED (2026-09-19, U1).** The earlier
claim here — "DDL under REPEATABLE READ is unaffected, catalog reads use
their own snapshot" — was true but too broad to rest a deploy on, and no
house could settle it from reads. Run on `cobalt_dev` as tests (f) and
(g): with another session committing an UPDATE to `system.cobalt_jobs`
between the BEFORE probe and `0003`'s `ALTER TABLE … ADD COLUMN IF NOT
EXISTS`, the ALTER **completes with no serialization error and the table
still reads unchanged**; with that other session holding the transaction
OPEN, the ALTER **waits for ACCESS EXCLUSIVE and completes the moment it
commits** (asserted as a real lock wait in `pg_locks`, under a 20 s
ceiling so a hang fails the test instead of the suite). That is the
interleaving a production deploy runs every time, because the runner
re-applies `0003` on every run while the heartbeat writes to that table
every 15 minutes.

## `--lock-timeout-s N` — the migrate transaction's lock ceiling
`DEFAULT_LOCK_TIMEOUT_S = 30`. The READ-WRITE transaction issues
`SET LOCAL lock_timeout = '<N>s'` before the BEFORE probe (so before
`_apply`'s first statement too), forward and rollback alike, so a DDL that
cannot get its lock **fails in N seconds with nothing applied** instead of
waiting.

**Why it exists.** Until 2026-09-19 nothing in this file set a
`lock_timeout` or a `statement_timeout`
(`prod-proof-only-3-2026-09-19.md` ESCALATE 3), so the only ceiling on a
deploy-time ALTER was whatever timeout the LAUNCHER happened to carry —
600 s for the Bash tool that ran the last deploy. That is a property of
the operator's shell, not of the code, and it is not a ceiling anyone
chose.

**Why 30 s.** A deploy takes its residents down before the merge (L66),
so at that moment an honest lock wait is sub-second; the suite's own
in-test ceiling for a deliberate lock wait is 20 s. 30 s is generous for
the legitimate case and still fails inside the deploy's own window.
Decided-with-veto by the desk. It is an ENGINE TUNABLE, not an L53
ceiling: it decides how long to wait for a lock, never what the system
may do. `0` is refused — "wait forever" is the defect this closes — as
is any negative or non-integer value, and the refusal happens **before
any connection is opened**, like the `--proof-only`/`--rollback`
conflict.

**What the operator sees on a timeout.** `psycopg.errors.
LockNotAvailable` is wrapped exactly the way `SerializationFailure` is:
roll back, then a `MigrationError` that says NOTHING WAS APPLIED, names
the timeout that fired, gives the `pg_locks` query that finds the session
holding the lock, and says plainly that raising `--lock-timeout-s` only
makes a stuck deploy wait longer. The CLI renders it as
`FAILED: MigrationError: …` on stderr and exits 1, which is what a deploy
reads. **The operator's next step is to find and stop the holder, not to
retry with a bigger number.**

**Where the `SET LOCAL` sits, and what that costs.** It is the first
statement `cmd_migrate` issues after `_connect` returns — BEFORE the
BEFORE probe, forward and rollback alike — so every lock the transaction
waits for is under the ceiling: the probe's ACCESS SHARE as well as
`_apply`'s ACCESS EXCLUSIVE. The probe's lock can only be blocked by an
ACCESS EXCLUSIVE holder (another DDL, never a resident's INSERT or
UPDATE); before the move such a holder made the probe wait with no bound
at all.

**It used to sit after the probe, and the reason it moved.** The
property that must hold is that the BEFORE probe and the migration share
ONE REPEATABLE READ snapshot. Whether a bare `SET` is itself the
statement that TAKES the snapshot could not be settled from a citable
source by the offline build that wrote the first version, so the
statement was parked after the probe, at the price that the probe was not
under the ceiling. It moved on 2026-09-19 (R1/R11) once two `requires_db`
tests in `tests/cobalt/test_migrate_proof.py` settled it by experiment on
`cobalt_dev`, timing the snapshot against another session's commit by
reading the same row's `xmin` from both sides:

* `test_connects_show_server_encoding_does_not_take_the_snapshot` —
  `_assert_utf8`'s `SHOW server_encoding`, the transaction's literal
  first statement, does NOT take the snapshot.
* `test_a_bare_set_local_does_not_take_the_snapshot_either` — neither
  does a bare `SET LOCAL lock_timeout`.
* `test_the_instrument_can_see_a_snapshot_that_is_already_fixed` — the
  negative control: once a REAL query has run, the same reading DOES pin
  the old row version, so the two results above are an observation and
  not a vacuous pass.

So the BEFORE probe is still the statement that takes the snapshot,
exactly as before the move, and the probe and the migration still share
one snapshot. `test_a_blocked_before_probe_is_under_the_lock_ceiling_too`
holds the ACCESS EXCLUSIVE lock for real and runs `cmd_migrate` with the
probe unstubbed.

**`--proof-only` is deliberately NOT given a ceiling.** It takes ACCESS
SHARE and applies nothing, and it is the command a deploy preflights
while everything is still up; giving it a lock ceiling would make it
start failing on a busy evening. A test asserts it sends no
`lock_timeout` at all.

## The output names the code it ran from
Both modes end with the same LAST line:

```
code: 8232dcc (clean) · /Users/cobalt/cobalt
code: 8232dcc (DIRTY: 2 path(s)) · /Users/cobalt/cobalt-wt/ops-2026-09-19
code: UNKNOWN — RestartError: git rev-parse --short HEAD failed: …
```

**Who reads it, and what they do with it.** The proof report is carried
out of the deploy window and compared later, and until 2026-09-19 the
only binding between a report and its code was git history — which proves
when the report was COMMITTED, not which code EXECUTED. The desk closed
that gap by hand on the 09-19 deploy (`cto-2026-09-19.md` §14). Now it is
a field. **The deploy gate — the desk's prompt — compares this line's sha
with the branch tip it was approved for, and refuses an `UNKNOWN` or a
`DIRTY` tip.** This command does not: a migration that is otherwise fine
is never blocked by a question about the checkout.

`CODE_ROOT` is derived from this module's own `__file__`, never from the
current directory, because a deploy hub `cd`s between `~/cobalt` and a
worktree and the answer must not follow it. The git call goes through an
EXISTING helper — `cobalt.generated.committer._git`, which takes the repo
root explicitly and runs `git -C` — imported inside the function so this
module keeps no import-time dependency on that package. **There is no
third git helper in the repo (L3).**

A git failure NEVER fails a migration or a proof. Not a repository, git
absent, a broken index: the line reads `code: UNKNOWN — <reason>`, which
is explicit and is not a plausible value (L1) — a reader can tell "we
could not read it" from "it was clean".

## What `OK` means, exactly
Written down here and in `cmd_migrate`'s docstring rather than inferred,
because all three houses read the same property out of the code in round
1 and one of them rated it a blocker:

> `OK` means the content that existed at the transaction's SNAPSHOT, plus
> this transaction's own writes, is unchanged except where the migration
> meant to change it.

It does NOT mean "the live database did not change while this ran". One
REPEATABLE READ snapshot is held from the first statement, so a row
another session INSERTs after that moment is invisible to both probes and
to the migration's own statements.

**The rule for migration authors.** A future migration that BACK-FILLS
rows of a table other sessions insert into cannot rely on this proof to
notice rows inserted after the snapshot. Such a migration either runs
with EVERY writer of that table stopped, or is followed by a SECOND
IDEMPOTENT PASS that catches what arrived in between. Nothing in the
registered set back-fills today — every row-level statement in `FORWARD`
is a seed `INSERT … ON CONFLICT DO NOTHING` or an `UPDATE … WHERE
user_id IS NULL` that matches no row on a database already past `0002` —
so this is a rule for the next migration, not a defect in these.

## An ambiguous table name is refused
`_schema_of` fetches EVERY row `pg_tables` returns for the name across
`SEARCHED_SCHEMAS`. One match behaves as it always did; no match is
`None` (which is how the proof says `ABSENT`); **more than one raises a
`MigrationError` naming the table and all of its schemas**, and nothing
is digested.

It used to end `LIMIT 1` with no `ORDER BY`, so a name present in two
searched schemas resolved to whichever row the server handed over first.
The proof would then digest THAT relation before and after while the
migration changed the other one, and print `OK` — a verifier that lies,
sitting on the production write path. Production carries no such
duplicate today, so it never lied in practice; L1 is why it now refuses
instead of choosing. The comment above `SEARCHED_SCHEMAS` says so: there
is no look-up order, and there never was one in the SQL.

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
a transaction has opened raises. `conn.read_only = read_only` is assigned
on BOTH paths (2026-09-19): the migrate transaction's read-write state is
a property of this harness, not of whatever default the server carries.

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

---

## 2026-09-17 — S2-P4

`DIGEST_EXCLUDED_COLUMNS` gains `rank_metric` and `rank_value` (Astra
R1-1). Adding two nullable columns to a populated `radar_membership` is not
content corruption, and dropping them on rollback must not read as CHANGED.
