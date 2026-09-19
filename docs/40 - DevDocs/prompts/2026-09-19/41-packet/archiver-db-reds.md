## DB RUN — WITH-DB SUITE

Scope, exactly as the prompt narrows it: `tests/cobalt/test_archiver_migrations.py`,
`tests/cobalt/test_archiver_append_store.py`, `tests/cobalt/test_archiver_quiet.py`. Repo-wide
`requires_db` tests this branch merely touched in passing (`test_radar_score_migration.py`,
`test_tenancy.py`) were NOT run and are not verified by this run. The whole `tests/cobalt` tree was never
run with `.env` present.

### Run 1 (12:45 ET) — the prompt's own ordering, run first so the finding is PROVEN, not asserted (L70)

```
12 failed, 145 passed in 4.38s
```

**THE PROMPT'S STEP ORDER IS WRONG, and this is the evidence.** Step 1 ends with `cobalt_dev` at 0001–0009 —
`archive_progress` and `archive_incidents` DROPPED. Step 2's own note assumes "every test that writes cleans
up; the migration-harness tests … are self-contained round trips". That is true of only 3 of the 23
(`…forward_creates_both_tables…`, `…migrate_twice_is_idempotent…`, `…rollback_down_to_0007_drops_exactly…`,
which call `_apply`/`_rollback_paths` on their own connection and roll back). **The other 20 need the two
tables to already EXIST**: seven via the `real_connect` fixture (which conftest documents as a REAL
`db.connect` that applies no migrations, `conftest.py:196-223`) and thirteen via `BarStore().ensure_schema()`,
### The four reds, one row each

**F-DB1 / F-DB2 — `cobalt_user` CAN read both new tables. GENUINE FINDING, ESCALATED, not "fixed".**
`AssertionError: cobalt_user can read system.archive_progress` (and `…archive_incidents`).
`has_table_privilege('cobalt_user', 'system.archive_progress', 'SELECT')` returns **true** on real
`cobalt_dev`. Cause, read from the SQL and not guessed: `0001_schemas.sql:124`
`GRANT SELECT ON ALL TABLES IN SCHEMA system TO cobalt_user;` — which 0001 replays on every migrate, after
0010/0011 have created their tables — and `:150-152`
`ALTER DEFAULT PRIVILEGES FOR ROLE cobalt_system, <login> IN SCHEMA system GRANT SELECT ON TABLES TO cobalt_user`,
a standing default privilege on every future system table. **The spec contradicts itself** (§11): it asks
for "`cobalt_user` is granted nothing on them" AND for "Ownership and grants follow `0006_radar_score.sql`'s
pattern for a system table — the builder reads it, never invents one" — and `0006_radar_score.sql:198-200`
does the opposite, granting `cobalt_user` SELECT on its own system tables explicitly. **The branch's code is
consistent with every other system table; the spec sentence is the thing that is not achievable** without an
explicit `REVOKE SELECT … FROM cobalt_user` that nobody wrote. Per the index card the CODE wins and the
difference is an ESCALATE line — so it is one, and the test stays RED for the desk to rule. This is exactly
the L45/L70 class: the offline twin `test_nothing_is_granted_to_cobalt_user` PASSES because it only greps
the migration TEXT for the string `cobalt_user`; the database says otherwise. **Not fixed here — I do not
rule a tenancy question, and I do not change real grants.**

**F-DB3 — the advisory-lock test could not observe its own property. TEST-SIDE, FIXED, tests-first.**
`assert try_acquire_run_lock(second) is False` → `assert True is False`, `where True = try_acquire_run_lock(<conftest._SavepointConnection object …>)`.
§9's lock is SESSION level (`store.py:53-66`, `pg_try_advisory_lock`, deliberately not `…_xact_lock`), and
`pg_try_advisory_lock` is re-entrant within one session. The test opened `BarStore()._connect()` twice —
both of which go through the autouse `dev_db_tx` fixture and come back as savepoint proxies over **one**
session — so the "second holder" was the first holder. The code is correct; the test could not see it.
Fixed by taking the two connections from the `real_connect` fixture, which conftest documents for exactly
this ("a savepoint proxy over one shared connection cannot show that a SYSTEM role is refused a `"user"`
table, because both proxies are the same session"). It writes no rows, so RULING 7 is untouched. RED before
(`assert True is False`) → GREEN after (`1 passed`). Own commit.

**F-DB4 — `test_the_own_connection_upsert_survives_another_transactions_rollback`. GENUINE, ESCALATED, left RED.**
`AssertionError: \`upsert_bars\` is expected to commit on its OWN connection; if this now rolls back, the
nightly night's write semantics changed`. Same root cause as F-DB3 — under `dev_db_tx` the "own connection"
`upsert_bars` opens is a savepoint of the SAME transaction as the enclosing `target_transaction()`, so the
outer rollback takes the inner write with it and the close reads `100.0000` instead of `999.0000`. **But
unlike F-DB3 there is no fix that does not either narrow the test or break a standing ruling:** the property
under test is that `upsert_bars` **COMMITS**, and a committing test is what conftest's RULING 7 exists to
forbid ("Before RULING 7 the test suite wrote REAL rows into the same `cobalt_dev` tables the PRODUCTION
ASET sheet and both prefill jobs wrote to"). Rewriting it to prove anything weaker is narrowing, which L45's
companion ruling refuses. **This is a ruling for the desk, not for me** — two options, named: (a) delete the
`requires_db` twin and rely on the offline pins that already assert `upsert_bars` opens its own connection
and holds the only `DO UPDATE` (`test_upsert_bars_still_does_update_and_never_do_nothing`,
`test_upsert_bars_on_takes_the_callers_connection_and_never_opens_one`,
`test_only_one_copy_of_the_upsert_statement_exists`); or (b) give the suite a sanctioned committing lane
with mandatory cleanup, which amends RULING 7. I took neither.

**Companion note, not a finding:** F-DB4's sibling `test_a_rollback_unwrites_an_upsert_made_on_the_targets_connection`
PASSES — but under one shared transaction it would pass whether or not the property held, since everything
rolls back. Its verdict should be read as UNPROVEN until F-DB4's ruling lands, not as evidence for F1.

## DB RUN ESCALATE

**CARRIED FORWARD UNTOUCHED — round 1's `## ESCALATE` in full:** (i) the spec §14 OPEN table O-1…O-7 with
what was built as the safe default; (ii) the never-run `requires_db` tests — **CLOSED by this run, see
below**; (iii) the cross-branch table (`sprint-2/p4` shares `db_migrations/__init__.py`, `placement.py`,
`tunables.yaml`, `cli.py`, `archiver/runner.py`, `archiver/store.py`; P4's `_check_demand` call must be
re-applied at the top of the rewritten `_run_targets`); (iv) the deploy-prompt list 1–6; (v) the five known
limits of §12; and its numbered findings 1–8. **And round 2's `## ROUND 2 ESCALATE` in full:** R2-1 (the
shadow artifact's timezone, ET — a ruling still OWED from the desk or the owner), R2-2 (`backfill-missing`
needed no F1-shaped fix), **R2-3 (the `requires_db` first run) — now CLOSED**, R2-4 (one test rewritten to
follow F1's refactor). Nothing in this run resolves or supersedes any of the rest.

**NEW THIS RUN — 4 items.**

**DB-1. `cobalt_user` CAN read both new tables; §11's grant sentence is not achievable as written. TWO TESTS RED.**
Detail and cause above (`0001_schemas.sql:124` + `:150-152`, vs `0006_radar_score.sql:198-200` which §11 told
the builder to copy). **The desk or the tribunal rules one of two ways:** (a) add an explicit
`REVOKE SELECT ON system.archive_progress, system.archive_incidents FROM cobalt_user;` to 0010/0011, making
the spec sentence true and making these two tables the ONLY system tables the user role cannot read — a real
tenancy decision, not a typo fix; or (b) amend §11 to match 0006's pattern and relax the two tests to assert
no WRITE grant. **This is the first thing this branch's DB run found that reads clean from the SQL text and
false from the database — precisely the L45/L70 class, and precisely why the run was owed.**

**DB-2. `test_the_own_connection_upsert_survives_another_transactions_rollback` is unobservable under
conftest's autouse single-transaction fixture. ONE TEST RED.** Detail and the two options above. Neither
was taken: (a) narrows the test (L45 companion ruling forbids), (b) amends RULING 7 (not mine).

**DB-3. `35`'s step order is wrong and the next prompt of this shape should not repeat it.** Step 1's
rollback removes the two tables that 20 of the 23 `requires_db` tests need. Proven, not asserted: run 1 went
`12 failed, 145 passed` with the ten missing-table reds listed above. The safe default taken (re-apply, run,
roll back again) delivered both steps' stated outcomes. **ASK DESK line raised in the suite section, 12:45 ET.**

**DB-4. Two index-card drifts, named in PREFLIGHT** — `test_archiver_quiet.py` holds ZERO `requires_db`
tests (the F3/Q10 twin is in `test_archiver_append_store.py`), and the 0010/0011 `requires_db` half is 10
tests, not ≈17. The total of 23 is correct.

**IS THE BRANCH'S DB DEBT CLOSED? YES — the debt itself, not every question it opened.** Round 1's ESCALATE
(ii) and round 2's R2-3 were both "23 `requires_db` tests written, NEVER RUN". **All 23 have now run on real
`cobalt_dev`: 20 pass, 3 are red and every one of the three is named, explained and escalated above.** The
migrations are proven applied AND reversed on real Postgres. What the branch now carries in place of the
debt is two rulings (DB-1, DB-2) and three red tests — which is a shipping gate the house check and Dejan
decide on, not an unknown.

**The three REVIEW.md UNVERIFIABLE items, by name, with how each was settled:**

| # | item | settled how |
|---|---|---|
| 1 | a fresh `git diff` of `c974fbf..archiver/append-0919` | PREFLIGHT ran it: nine paths, identical to round 2's own close listing, no surprise path |
| 2 | the `1866/0/320` suite pass and the 23 `requires_db` tests | step 3's offline run: **1866 passed / 0 failed / 320 skipped**, exact match; step 2 ran the 23 for real: **20 pass, 3 red** (DB-1 ×2, DB-2) |
| 3 | the `RESTARTS: com.cobalt.aset com.cobalt.radar` line | `uv run cobalt jobs restarts 8838dda..HEAD` printed above: **0 UNCLASSIFIED**, the line is derived and correct |

**MEMORY:** none proposed — this run changed no law and no standing practice.
**RULING:** two are owed by the desk or the tribunal — **DB-1** (the `cobalt_user` grant on the two archiver
tables: REVOKE, or amend §11) and **DB-2** (whether a `requires_db` test may commit, or the twin retires).
R2-1 (the shadow artifact's timezone) remains owed from round 2 and is untouched by this run.

ARCHIVER DB d2099e1 (code tip; report 2e4ca6f, and this line's own docs-only commit on top) | offline 1866/0 (320 skipped vs round-2 320 — unchanged, and correct: step 3 runs with `.env` removed so all 23 `requires_db` skip again) | db 154/3 (the 23 archiver requires_db tests: 20 pass, 3 red — DB-1 ×2 cobalt_user grant, DB-2 unobservable commit) | migrations 0010/0011: applied on real cobalt_dev (both CREATED system-side, every pre-existing digest unchanged) and reversed (`--rollback --down-to 0009` dropped exactly those two, proof-only byte-identical to the step-0 baseline) | UNVERIFIABLE settled: (1) fresh c974fbf..HEAD diff = round 2's nine paths, no surprise; (2) 1866/0/320 real + the 23 ran for the first time; (3) RESTARTS derived, 0 UNCLASSIFIED | cobalt_dev: 0001–0009, unchanged (every row count and digest identical to this run's step-0 proof) | .env: removed, proven gone | RESTARTS: com.cobalt.aset com.cobalt.radar | OWED: whole-build house check close (Astra), rulings DB-1 + DB-2 + R2-1, next deploy prompt (deploy 3, after P4) | ESCALATE: 4
