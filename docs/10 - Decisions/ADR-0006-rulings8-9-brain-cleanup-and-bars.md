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
