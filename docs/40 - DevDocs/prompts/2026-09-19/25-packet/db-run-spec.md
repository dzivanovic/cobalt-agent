# DB run spec — R1/R11 experiment, F1, F3, F4, F5 (binding on `25-ops-db-run.md`)

Where your reading of the code differs from this packet, the CODE wins and the
difference is an ESCALATE line, same convention as `16-packet/facts.md` and
`19-packet/verdicts.md`.

## A. R1/R11 — does `SET LOCAL lock_timeout` take/move the REPEATABLE READ snapshot?

**Why this is still open.** `src/cobalt/db_migrations/cli.py`'s `_connect` docstring
(≈:520-526) states as settled fact "the snapshot is taken at this transaction's first
statement" for a REPEATABLE READ transaction. `cmd_migrate`'s own docstring (≈:583-606)
could not settle whether a bare `SET LOCAL <guc>` command — which touches no table —
counts as "the first statement" for that purpose, because "the Postgres manual could not
be read from the run that wrote this" (≈:596). Today's code places `SET LOCAL
lock_timeout` (`:664`) AFTER the BEFORE probe (`:659`), specifically so the question
cannot matter — at the cost of the probe itself running with no lock ceiling (stated
≈:600-604). `cobalt_dev` is reachable today; the question is answerable by experiment.

**The experiment, as a new `@requires_db` test in `tests/cobalt/test_migrate_proof.py`**
(place it in a new section after §9, e.g. "10. THE TRIBUNAL'S CARRIED ITEMS (R1/R11,
2026-09-19 DB run)"):

1. Session A: `conn = cli._connect(env.DEV_DB_NAME, allow_prod=False, read_only=False)`
   — this is the REAL harness connection, REPEATABLE READ / READ WRITE, exactly as
   `cmd_migrate` opens it, and no statement has run on it yet.
2. Session A issues `conn.execute("SET LOCAL lock_timeout = '5s'")` and NOTHING else —
   no query against any table yet.
3. Session B (`other = db.connect_migration(env.DEV_DB_NAME)`, autocommit) makes an
   OBSERVABLE change to one row of `cobalt_jobs` and commits it. **Do not reuse
   `_touch_a_job_row`'s no-op `SET last_result = last_result`** — that update leaves the
   VALUE unchanged by design (test (g)'s cleanup-free pattern) and cannot prove which
   snapshot Session A sees. Instead read the target row's `xmin` system column from
   Session B BEFORE its own update (`SELECT xmin, last_result FROM … WHERE label = …`),
   run the same cleanup-free `SET last_result = last_result` (or increment a scratch
   integer column if one is safe to touch and restore), and read `xmin` again — `xmin`
   changes on any UPDATE even when the visible value does not, and reading `xmin` never
   requires inventing a new mutable column.
4. Session A now runs its FIRST real query against that same row (`SELECT xmin, … FROM
   {rel} WHERE label = …`) and records the `xmin` it sees.
5. Assert and branch:
   - **A sees Session B's NEW `xmin`** → `SET LOCAL` did NOT take/move the snapshot; the
     snapshot forms at the first real query, same as if `SET LOCAL` were never issued.
     **Outcome: SAFE TO MOVE.** Do part B below.
   - **A sees the OLD `xmin`** (pre-B's-update) → `SET LOCAL` already fixed the
     snapshot. **Outcome: R1 CANNOT BE COVERED THIS WAY.** Do part C below.
6. Teardown: Session A rolls back (never commits — it never applied anything), Session B
   restores the row to its original `xmin`-bearing state is not possible (xmin always
   advances) but the VALUE must be restored to what it was before step 3 if you touched
   anything besides the no-op update; if you used the no-op pattern for step 3's mutation
   itself (toggle `last_result` to itself twice, reading `xmid` in between via a separate
   statement) no value-level cleanup is needed. Close both connections in `finally`.

**B. If SAFE TO MOVE (no snapshot taken by `SET LOCAL`):**
- Move `conn.execute(f"SET LOCAL lock_timeout = '{lock_timeout_s}s'")` in `cmd_migrate`
  to BEFORE `before = _probe_all(conn)` (i.e., swap the two lines at `:659` and `:664`),
  for BOTH the forward and rollback transaction (the docstring says it applies "forward
  and rollback alike").
- Add a NEW `@requires_db` test proving the probe is now covered: another session holds
  `LOCK TABLE {a table `_probe_all` reads} IN ACCESS EXCLUSIVE MODE` (use `cobalt_jobs`,
  consistent with the rest of this file), then `cmd_migrate` with a short
  `--lock-timeout-s` (e.g. 1–2s, well under `LOCK_CEILING_S`) must raise
  `MigrationError` — via the `LockNotAvailable` path — in about that many seconds rather
  than hanging on the probe's ACCESS SHARE request. Model it on
  `test_a_migration_that_cannot_get_its_lock_fails_in_about_a_second` (`:1601-1660`) but
  do NOT stub `_probe_all` this time — the whole point is that the (now-covered) probe is
  what waits and times out.
- Update `cmd_migrate`'s docstring (≈:582-606): replace "NOT SETTLED … the statement was
  placed where the question cannot matter" with the proved fact, the date, and how it was
  proved (this test, on `cobalt_dev`), and update "THE PRICE OF THAT POSITION… the BEFORE
  PROBE IS NOT UNDER THE CEILING" — that price no longer applies once moved.

**C. If CANNOT BE COVERED (snapshot already taken by `SET LOCAL`):**
- Leave `cli.py`'s `SET LOCAL` placement exactly as it is (`:664`, after the probe) — do
  not move it; moving it would not help (the snapshot would just form one statement
  earlier, still not covering the probe any differently than today's `SHOW
  server_encoding` in `_assert_utf8` already does).
- Update the docstring (≈:596-599) to record the proof: `SET LOCAL` DOES fix the
  transaction's snapshot, cited to this test, and state R1 as closed "cannot be covered
  by reordering `SET LOCAL`" rather than "not settled."
- No new probe-coverage test in this branch — the price named at ≈:600-604 stands.

Either outcome is a real answer; do not force B. Whichever branch you take, say so
plainly in the new report section: "R1/R11: SET LOCAL <does/does not> take the
snapshot — proved by `<test name>` — <moved lock_timeout ahead of the probe and added
its coverage test | left placement, docstring records the proof>."

## B. F1 — nest test (g)'s `finally` so worker cleanup runs on every path

File: `tests/cobalt/test_migrate_proof.py`, function
`test_the_alter_waits_for_an_open_transaction_and_then_completes` (`:1226-1372`
currently; the `finally:` block is `:1322-1353`).

Today, in order: `if not committed: other.commit()` → `other.close()` → `watcher.close()`
→ (comment) → `if thread.is_alive(): conn.cancel(); thread.join(...)` → `if not
thread.is_alive(): conn.rollback(); conn.close()`. Round 1's R2 fix (commit `543810f`)
made the cancel/join/rollback/close UNCONDITIONAL — but `other.commit()`, `other.close()`
and `watcher.close()` still run FIRST, un-nested, ahead of the worker cleanup. If any of
those three raises (a review-identified residual, F1, hub severity MINOR, not a
blocker), the worker cleanup below it never runs and the worker's backend can be left
holding its ACCESS EXCLUSIVE request against `cobalt_dev`.

FIX: nest it —

```python
finally:
    try:
        if not committed:
            other.commit()
        other.close()
        watcher.close()
    finally:
        # R2 (round 1) + F1 (round-2 review, this DB run): the worker
        # cleanup below must run even if closing `other`/`watcher` above
        # raises — nothing may leave a backend queued for ACCESS
        # EXCLUSIVE on cobalt_dev.
        if thread.is_alive():
            conn.cancel()
            thread.join(timeout=WORKER_STATEMENT_TIMEOUT_S)
        if not thread.is_alive():
            conn.rollback()
            conn.close()
```

Keep every comment's substance (R2's own comment about why `cancel()`/rejoin/timing is
correct); add one line crediting this nesting to F1. The test's assertions
(`:1355-1372`) are UNCHANGED — this is cleanup-path hygiene only, same class as R2. This
is the SAME `requires_db` test as R2/R3 — there is no offline red/green for the nesting
itself; say so plainly, as round 2 did for R2/R3.

## C. F3 — R9's carry-forward gap (disclosed trade-off; no forced edit)

Round 2's F3: R9 option (ii) (drop the dangling ESCALATE pointer at round 1 `:130`
instead of adding a new numbered item) leaves a reader of round 1's `## ESCALATE` list
ALONE without the premarket-before-open case — disclosed and accepted, not a defect
(hub verdict: REAL, MINOR, "a ruling, not a bug"). This DB run does not edit round 1's
`## ESCALATE` list or its `ESCALATE: 9` count on its own authority. Record F3's
disposition in the new report section as: "F3 — ACCEPTED AS DISCLOSED, no edit; adding a
tenth `## ESCALATE` entry (and correcting the headline/stop-line count to 10) is
Dejan's/the desk's call, not built here." If you judge this wrong, ESCALATE it instead of
silently building it.

## D. F4 — mark the round-1 stop line's silent `+2`→`+1` correction

Round-1 report `docs/40 - DevDocs/reports/ops-2026-09-19.md:577` (the `OPS 0919 fc1d967
…` stop line) still reads `db: OWED — 1 requires_db test written, never run (+1 edited,
never re-run)` — the `+1` is already CORRECT (R7 already fixed the number in round 2),
but the stop line carries no inline marker showing it was corrected, unlike the headline
bullet at `:8` which does (`[corrected in round 2, R7: …]`). FIX: append `[R7 corrected
in round 2]` to the end of line 577's stop line, changing NOTHING else on that line (not
the counts, not the tip, not any other field). Quote before/after in the new report
section.

## E. F5 — mark the "20 s join fires first" unconditional claims as historical/corrected

Round-1 report, two places still state the ordering unconditionally after round 2's R3
made it conditional in the code docstring:
- `:311` "the main thread's join gives up **first**, so the message a reader sees is
  this test's own assertion, never a driver error"
- `:528` (inside `## ESCALATE` item 2(b)) "the 20 s join fires first (so the reader still
  sees the test's own message)"

FIX: append `[see round 2, R3: conditional on the probe returning quickly relative to
`LOCK_CEILING_S` — not unconditional]` to the end of BOTH sentences (adjust wording to
fit each sentence's grammar; do not otherwise alter either line). Quote before/after for
both in the new report section, same style as R6-R9's quotes in round 2.
