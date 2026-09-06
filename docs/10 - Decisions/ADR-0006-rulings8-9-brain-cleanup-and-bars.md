# ADR-0006 — RULINGS 8 + 9: cleaning production, and `bars` onto the resolver

Date: 2026-09-04
Status: Accepted
Closes: the first two follow-ups of
[ADR-0005](ADR-0005-ruling7-environment-law.md) — "853 pytest
`vault_writes` rows in `cobalt_brain`" and "`bars` is still in
`cobalt_dev` and the archiver still passes an explicit `db_name`".
Supersedes: nothing.

## Context

RULING 7 created the two-database world and moved every store onto
`cobalt.env.resolve_db_name()`. It closed the routing hole, but it
deliberately left two things behind, both recorded as follow-ups
because acting on either inside that session would have been an
unsanctioned destructive change to production:

1. **The migration was byte-exact, so it copied the mess.** Proving
   the copy meant demanding identical md5 over ordered rows, which
   forbids filtering. `cobalt_brain` therefore received 853
   `vault_writes` rows whose note paths point at pytest temp vaults,
   and 85 `aset_sizings` rows under five synthetic tickers. The audit
   trail the 09-03 forensics depend on was interleaved with test data,
   and the DRC had already once reported "17 cards" when 2 were real
   for exactly this reason.

2. **`bars` never moved.** 4.5M rows of *production* market data sat in
   `cobalt_dev`, because `archiver/store.py` defaulted to the literal
   `"cobalt_dev"` and `runner.py` threaded a `db_name` parameter down
   from a `--db-name` CLI flag. Every other store had moved onto the
   resolver; the archiver had not, so it kept doing the exact thing
   RULING 7 existed to stop. It also made "cobalt_dev is dev only"
   false, which is the property the truncate guard
   (`env.assert_destructive_target`) is built on.

## Decision

**RULING 8 — production is cleaned, under the 09-03 delete discipline.**
Both row sets dumped first (with sha256, into the gitignored
`docs/00 - Project/incident-2026-09-03/`), then deleted in ONE
transaction whose guards abort the whole thing on any unexpected count:
the pytest `vault_writes` count must be exactly 853, no row under the
five tickers may be `status = FILLED`, each `DELETE`'s `ROW_COUNT` must
equal what was counted, and a post-condition check inside the same
transaction rolls everything back if a single target row survives.

The identification rule differs per table on purpose, and that is the
same reasoning ADR-0005 used to *refuse* filtering: `vault_writes` is
decidable from the note path (`%pytest-of-cobalt%`), so it is deleted by
predicate; `aset_sizings` is not decidable from data, so it is deleted
from an explicit five-ticker list that Dejan confirmed by hand. What was
unacceptable as a silent migration filter is acceptable as a named,
counted, ruled deletion.

**RULING 9 — `bars` moves to `cobalt_brain`, and the archiver stops
naming a database.** Same migration shape RULING 7 proved: dump (the
rollback) → schema through the store's own `ensure_schema()` → restore
data-only → identical counts and md5 over PK-ordered rows → only then
drop the source. `db_name` survives on `BarStore` solely as the
test/tooling seam the other stores keep; the runner's parameters and the
`--db-name` flag are **deleted rather than re-pointed**.

**The run report names its database.** `archiver-runs.md` gains a
Database column, resolved from the same source the store uses.

## Consequences, and the judgement calls inside them

- **`--db-name` is deleted, not re-pointed at `cobalt_brain`.** A flag
  that can send a production archiving run into another database is the
  hole RULING 7 closed for `AsetConfig.db_name`. Re-pointing it would
  have preserved a convenience nobody was using — every real call site
  passed nothing — at the cost of reopening the failure mode.
  `test_env.py` fails if the parameters or the flag return.

- **The run report gets a second table rather than a rewritten one.** A
  markdown table cannot change its column count in place. Rewriting the
  existing 130+ rows to add a column would be the cleaner-looking
  result and the wrong one: this file is an append-only record, and its
  historical rows are evidence — they are what shows three weeks of runs
  landing in `cobalt_dev`. The break is written once, says so, and
  leaves every prior row byte-identical.

- **The archiver is a batch job, not a resident collector.** Worth
  stating because the reverse was assumed when this work was scoped:
  `com.cobalt.archiver` is `StartCalendarInterval` Mon–Fri 20:30 with
  `RunAtLoad=false`. Taking it out at 16:15 and putting it back the same
  afternoon loses nothing — the day's bars are pulled from Finviz
  history in one pass at 20:30. `launchctl print` showed
  `state = not running`, `runs = 0`, and no process, before the bootout.

- **One row of test residue was left in `cobalt_brain.bars`, on
  purpose.** `TESTARCH/i5/2026-08-28 09:30Z`, written by
  `test_archiver_store.py` before the autouse transaction fixture
  existed. It is in the pre-migration dump, so it predates this session;
  it rode into `cobalt_brain` because proof (e) requires an exact copy.
  It is outside RULING 8's named scope, and RULING 8's own precedent is
  that deletions against production are *named and ruled first*, never
  taken on the operator's initiative. Reported for a ruling instead.
  `TESTARCH` is in no watchlist tier, so no real run can reproduce it
  and no real query returns it.

- **No sequence needed resetting.** Unlike RULING 7's three tables,
  `bars` has a composite PK `(ticker, interval, ts)` and no identity
  column. Stated because "reset the sequence" was expected work; the
  correct outcome was to prove there was nothing to reset.

- **`cobalt_dev` is now genuinely empty of production data**, which is
  what makes `env.assert_destructive_target`'s "destructive helpers may
  only ever touch `cobalt_dev`" a safe rule rather than a dangerous one.
  It was not safe while 4.5M production bars lived there.

## Alternatives rejected

- **Delete the pytest rows during the RULING 7 migration.** Rejected
  there and still correctly rejected: it would have been an unsanctioned
  destructive operation against production inside a migration session,
  and it would have destroyed the md5 proof that the migration was
  faithful. Cleaning is a separate, ruled, individually-dumped step.

- **Filter `bars` on the way over** (drop `TESTARCH`, drop bars older
  than some date). Same objection as ADR-0005's rejected filter: the
  proof of a migration is byte-exact equality, and any filter means the
  proof no longer proves the thing it claims. Clean afterwards, under a
  ruling, or not at all.

- **Emptying `cobalt_dev.bars` with raw SQL.** The ruling says
  truncate, and truncate is what happened — but through
  `cobalt.devdb`, not a hand-written statement, which meant adding
  `bars` to that module's `TRUNCATABLE_TABLES` allowlist. The allowlist
  previously excluded `bars` *because* it held production data; now
  that it does not, the exclusion protects nothing and only pushes the
  operation outside the one guarded path. The database guard
  (`cobalt_dev` and nothing else, hard-coded) is untouched and is what
  actually makes this safe.

- **`DROP TABLE cobalt_dev.bars` instead of truncating.** Tempting —
  an empty `bars` still answers "which one is real?" ambiguously — but
  not what was ruled, and truncate keeps a dev run from needing DDL
  before it can write. Left as ruled.

- **Defer the landing proof to Tuesday 09-08.** Available (Monday is a
  holiday) and unnecessary: `launchctl kickstart -k` runs the job in
  launchd's own environment, which proves the plist's `COBALT_ENV`
  reaches the process AND that rows land in `cobalt_brain`, in one
  observation, on the same afternoon the change was made. A change that
  can be proven now should not be left unproven over a long weekend.

## Follow-ups (not done here)

- **`TESTARCH` in `cobalt_brain.bars`** — one row, needs a ruling
  (above). One-liner in the incident report.
- **RULING 6.3c, the heartbeat probe, still has no host.** Unchanged.
- **The production vault still has no backup.** Unchanged, and still the
  largest open risk in the incident report.

---

## 2026-09-04 (later the same day) — ONE DATABASE PER PRODUCT

Status: Accepted. Ruled 2026-09-04. Delivered on branch
`ops/mattermost-split`.

RULING 8 cleaned production and RULING 9 moved `bars` into it, but both
worked *inside* a database that Cobalt was only half the owner of. The
`jobs` collision that S1-P3 found — `CREATE TABLE IF NOT EXISTS jobs`
silently doing nothing because Mattermost already had a `jobs` with
164,320 rows — was left as an open ruling: "a schema of its own, or a
prefix convention made law". The ruling went further than either.

**Mattermost gets its own database.** Cobalt keeps `cobalt_brain`, its
name, its role, and every plist and config value. Nothing on Cobalt's
side changed at all; the only edit was one `MM_SQLSETTINGS_DATASOURCE`
in `docker-compose.yml`.

### What the split actually found

**The "116 Mattermost tables" in this repo's own documentation was
wrong, and acting on it would have destroyed production data.** That
figure was arithmetic, not an inventory: 129 tables total, minus 13
assumed to be Cobalt's. Nobody had ever listed the 116.

The split needed a list it could guard a `DROP` with, so one was
derived from evidence instead: a **pristine Mattermost 11.4.0 reference
install** — the same image digest as the running container — pointed at
an empty database, allowed to run its own migrations, and then read.
It creates **103** tables, 5 materialized views, 297 indexes and 6 enum
types. Every one of those 103 was present in `cobalt_brain`, none was
missing, and the index and type sets matched name for name. `bars.ts`
aside, that is the strongest form of proof available here: the
Mattermost half of `cobalt_brain` was structurally identical to a fresh
install.

Which makes the Cobalt half **28** tables, not 13. All 28 have a
`CREATE TABLE` somewhere in this repo. **13 Cobalt tables had been
counted as Mattermost's** — among them `themes`, `instruments`,
`trades`, `trading_accounts`, `key_levels`, `market_snapshots`,
`news_events`, `news_mentions`, `order_fills`, `strategy_signals` and
`system_alerts`, all Gemini-era tables with generic names. A drop
guarded by "the 116" would have taken them.

**Two name collisions, and only two:** `jobs` and `sessions` are
Mattermost's, and the repo also contains a `CREATE TABLE` for each. The
`jobs` one is the S1-P3 defect, already resolved by the `cobalt_`
prefix; the `sessions` one is in
`docs/90 - References/claudeclaw-kit/`, which is reference material
under L15 and not live code. `themes` looks like a third and is not:
Mattermost has no `themes` table, and the live one is Cobalt's
(`uuid` PK, `example_tickers`, `ai_metadata`).

### Consequences, and the judgement calls inside them

- **The migration excluded Cobalt's tables rather than selecting
  Mattermost's.** `pg_dump -t` cannot carry enum types, and Mattermost
  has six that its tables depend on. Excluding the 28 keeps every type,
  matview, index and constraint in correct dependency order. Two
  standalone Cobalt sequences (`browser_fast_path_id_seq`,
  `memory_logs_id_seq`) rode along because they are not column-owned
  and `--exclude-table` therefore does not remove them; they and the
  `vector`/`uuid-ossp` extensions were dropped from the NEW database
  afterwards, verified against the pristine reference.

- **The three "row count mismatches" were materialized views, and they
  were right to differ.** `pg_dump` emits `REFRESH MATERIALIZED VIEW`,
  so the copies recomputed against current data while `cobalt_brain`'s
  were stale. Refreshing the source made all five identical. The 103
  base tables matched exactly, 165,520 rows, first time.

- **The drop ran behind seven guards and three post-conditions in one
  transaction**, including a row-count guard asserting every Mattermost
  table still held exactly what was migrated — a single new row would
  have meant something wrote to `cobalt_brain` after the dump, and would
  have aborted the whole thing.

- **Mattermost keeps using the `cobalt` role**, deliberately. The ruling
  said to reuse the existing Mattermost credential and create nothing
  new. There is no Mattermost-specific Postgres role and there never
  was: `\du` returns exactly one role. Mattermost has always
  authenticated as `cobalt`. Splitting the *database* was the ruling;
  minting a role would have been inventing a credential the ruling
  explicitly forbade. **This is a real remaining weakness** — one
  superuser role reaches both databases — and it is the natural next
  ruling, not something to take on an operator's initiative.

- **The container is RECREATED, never restarted.** `MM_SQLSETTINGS_
  DATASOURCE` is baked into the container at creation, which is the
  same fact the 2026-08-23 credential rotation recorded. `docker compose
  up --force-recreate mattermost` also recreates `cobalt_memory` through
  `depends_on`; Postgres came back on its bind mount with both databases
  intact, verified by row count before anything was dropped.

### Follow-ups (not done here)

- **A Postgres role per product.** Mattermost holding superuser on a
  database that also contains the trading record is the part the split
  did not fix.
- **The old tree's `CREATE TABLE IF NOT EXISTS sessions`** is now
  un-shadowed: nothing occupies that name in `cobalt_brain` any more.
  It is reference material today, so nothing runs it — but the name is
  free, and a future import would create a real table rather than
  silently no-op.
- **`mattermost` has no backup story of its own.** It is deliberately
  outside `configs/cobalt/backup.yaml`'s scope; that scope should be
  re-ruled once a backup destination exists.

## 2026-09-05 — ONE ROLE PER PRODUCT

Status: Accepted. Ruled 2026-09-05. Delivered on branch
`ops/mattermost-role`, unpushed.

The 09-04 split gave Mattermost its own database and left it
authenticating as `cobalt` — a superuser that also reaches the trading
record. That section named it "a real remaining weakness… the natural
next ruling". This is that ruling.

`mattermost` is now a role with **LOGIN and nothing else**: no
superuser, no createdb, no createrole, no replication, no bypass-RLS, no
membership in any other role. It owns database `mattermost` and all 103
tables, 5 materialized views, 297 indexes and 6 enum types in it;
`cobalt` owns nothing there any more. `cobalt` keeps superuser for now —
its demotion is a separate ruling — and the db service's initdb
variables are untouched.

### `.env` is the bootstrap tier, and that is a rule now

`MATTERMOST_DB_PASSWORD` lives in `.env` beside `POSTGRES_PASSWORD`, and
the reason generalises: **`.env` holds only credentials that must be
readable before the vault can be opened.** Docker Compose interpolates
`MM_SQLSETTINGS_DATASOURCE` at container-create time, with no process
running that could ask VaultManager for anything. That is the whole
membership test for this tier. Everything else goes to VaultManager and
only VaultManager.

A copy is stored in the vault as well — not as a second source of truth,
but because **storing it there IS its enrolment in F19's literal
guard**. `cobalt.redact.secrets.load_literals()` walks every vault leaf
of 8+ characters, so the guard went 15 values → 16 with no list to edit
and no value written into a pattern file. Belt and braces: the name ends
in `PASSWORD`, so F19's `env_assignment_secret` pattern also catches
`MATTERMOST_DB_PASSWORD=…` by name with the vault locked.

### The finding: `REASSIGN OWNED` would have taken `cobalt_brain`

The ruling's step 3 said to run `REASSIGN OWNED BY cobalt TO mattermost`
connected to `mattermost` only, on the understanding that it is
per-database. **It is not, quite.** REASSIGN OWNED also reassigns
*shared* objects — and databases are shared objects. Run as written it
would have handed `cobalt_brain`, `cobalt_dev`, `postgres`, `template0`
and `template1` to the `mattermost` role: the exact inverse of the
ruling it was implementing.

This was proven before anything production was touched, on throwaway
objects: two databases owned by one throwaway role, REASSIGN run while
connected to the first, and the **second** changed owner too.

The substitute is an explicitly scoped loop over `pg_class` and
`pg_type` in the current database, emitting one
`ALTER TABLE|MATERIALIZED VIEW|TYPE … OWNER TO mattermost` per object
inside a single transaction with `lock_timeout`. It reassigned 108
relations (103 + 5) and 6 types; indexes follow their tables. Verified
after: zero `cobalt`-owned relations remain in `mattermost`, and
`cobalt_brain` / `cobalt_dev` are still owned by `cobalt` with all 100
of `cobalt_brain`'s public relations unchanged.

The general lesson is worth more than the incident: **a command whose
scope is "the current database" may still have a shared-catalog
exception, and ownership commands are where that bites.**

### The password was never a bound parameter, because it could not be

`CREATE ROLE … PASSWORD` takes a string literal; a utility statement
cannot carry `$1`, so no server-side bind exists for it. Rather than
fall back to client-side quoting of the plaintext, the provisioning
script computes the **SCRAM-SHA-256 verifier locally** and sends only
that. The plaintext never crosses the socket at all, so it cannot reach
a server log, a wire capture or `pg_stat_statements` if any of those is
switched on later — strictly stronger than the bound parameter it
replaces. The verifier math was proven against a live server on a
throwaway role, including the negative case (a wrong password rejected),
before the real role was minted.

Generation, `.env` write, vault write, role creation and the login check
all happen inside **one process** (`ops/mattermost_role_provision.py`).
Nothing is shelled out to, because `psql -c` and `echo >> .env` both put
the value in a command line.

### The fence is one-directional, on purpose

`CONNECT` on `cobalt_brain` and `cobalt_dev` is revoked from `PUBLIC`,
which is what `mattermost` was reaching them through — it holds no grant
of its own on either, and no role membership. Proven by connection
attempt: `FATAL: permission denied for database "cobalt_brain"`.

`cobalt` can still reach `mattermost`, because it is a superuser and
superusers bypass the check. **That half of the fence does not exist
yet, and cannot until `cobalt` is demoted** — which is the next ruling,
not something to take on an operator's initiative. `TEMP` remains
granted to `PUBLIC` on both databases; it is inert without `CONNECT`,
and tightening it was outside this ruling.

Revoking from `PUBLIC` was safe to do before Mattermost was proven on
the new role: `cobalt` holds `CTc` explicitly and was unaffected, and
Mattermost was at that moment still connecting *as* `cobalt` *to*
`mattermost`, which the revoke does not touch. Nothing `cobalt` holds
was revoked, which is what "nothing is revoked until proven" protects.

### Recreated, not restarted — and `--no-deps` this time

`MM_SQLSETTINGS_DATASOURCE` is baked in at container creation (the
2026-08-23 rotation lesson), so the container is recreated. On 09-04
that recreate bounced `cobalt_memory` too, through `depends_on`. Adding
`--no-deps` prevented it: the db container's id was byte-identical
before and after, Postgres never restarted, and Mattermost's downtime
was **15 seconds** (22:17:29 → 22:17:44 ET).

### Follow-ups (not done here)

- **Demote `cobalt`.** One superuser still reaches every database; the
  fence stays one-directional until it is a plain owner role. Next
  ruling.
- **`.env` rotation path.** `ops/mattermost_role_provision.py` mints and
  refuses to rotate — it aborts if either key is already present, rather
  than guess which of role, `.env` and vault is authoritative. A
  rotation needs its own script and its own recreate.
- **`mattermost` still has no backup story** — unchanged from 09-04, and
  now it is also the only database whose owner is not `cobalt`, which a
  restore path would have to recreate.
