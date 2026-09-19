"You are an independent reviewer from another house, one of three (Astra's Codex meter is
expected OUT this round — if you are Astra and cannot run, say so and stop) reading this
packet separately. Read ONLY the files in this folder; you cannot run commands — everything
you need is already here as a file. This is ROUND 3 of the three-house check of branch
`ops/2026-09-19` (LAWS L67 — this is the LAST allowed round on this fold). Round 2
(`verdicts-r2.md`, the `## Verdict table` from round 2's own review) found four REAL findings
against the round-2 fold (F1 MINOR residual, F3/F4/F5 MINOR disclosed-trade-off items) and one
NOT REAL (F2). A DB-run session then: (a) fixed F1 (nested the nested-cleanup residual), (b)
made a NEW code change unrelated to any prior finding — moved `SET LOCAL lock_timeout` ahead
of the BEFORE probe to settle carried items R1 and R11 from round 1, backed by three new
experiment tests and one new coverage test, and (c) fixed a test-side defect in test (j),
found when the coverage test's sibling first ran for real. `fold.diff` is
`git diff d860bf7..ops/2026-09-19 -- src tests` — round 2's own reviewed tip to the current
branch tip, code and tests only (the report file is excluded; `db-run-section.md` below is
that report's own account of this work, not code). `verdicts-r2.md` is round 2's own verdict
table, given as the SPEC for what F1's fix must satisfy. `db-run-section.md` is the ops
report's own DB-RUN section — the hub's account of this work; treat it as a CLAIM to
spot-check against `fold.diff`, same standing as any build report, never as settled fact you
may skip verifying. `facts.md` is this hub's own pre-computed measurements (commit list,
diff-stat, new test names, scope check) — also a claim to spot-check, not to relay. For each
finding give SEVERITY (BLOCKER = the fold does not do what it claims, breaks an existing
invariant, or contradicts a LAW (L1 fail-loud, L3 one-path, L45 real-shape fixtures, L52
nothing here may touch scoring/ranking/cards) / MAJOR / MINOR), FILE + LINE (from
`fold.diff`), the EVIDENCE you read (quote it), and the FAILING SCENARIO; say 'none found'
rather than inventing.

(Q1) THE SET LOCAL MOVE — correct and complete. Does `fold.diff` show
`conn.execute(f\"SET LOCAL lock_timeout = …\")` now running BEFORE `before = _probe_all(conn)`
in `cmd_migrate` (previously after)? Is this a single statement moved (one hunk, one call
site) rather than a second copy added (L3)? Does the docstring rewrite in the same hunk
correctly describe the NEW order (ceiling covers the probe's ACCESS SHARE, not just
`_apply`'s ACCESS EXCLUSIVE), without leaving the OLD claim ("issued AFTER the BEFORE probe")
anywhere uncorrected in the same docstring?

(Q2) DOES THE COVERAGE TEST ACTUALLY DEPEND ON THE MOVE. Read
`test_a_blocked_before_probe_is_under_the_lock_ceiling_too` in `fold.diff`: does it hold a
real `LOCK TABLE … ACCESS EXCLUSIVE` from another session, run `cmd_migrate` with `_probe_all`
NOT stubbed, and carry its own server-side `statement_timeout` backstop (so a regression fails
in ~30s rather than hanging)? Is this shaped so that, AT THE OLD PLACEMENT, the BEFORE probe
would run unbounded against the held lock and the test would time out — i.e., does the test's
own logic depend on the move, even though the actual red-before/green-after run
(`db-run-section.md`'s "7.65s green … 35.47s red") is not itself capturable in `fold.diff` and
is UNVERIFIABLE FROM READS as an executed fact? Say which parts you can confirm from the diff
alone and which parts you cannot.

(Q3) F1 — the nested cleanup. Does `fold.diff` show `other.commit()`/`other.close()`/
`watcher.close()` now nested INSIDE a `try` whose own `finally` runs the worker cleanup
(`conn.cancel()`/`thread.join(...)`/rollback/close), rather than those three statements
sitting unguarded ahead of it? Is this one copy of the cleanup logic, not two (L3)? Do the
test's assertions change, or only the cleanup path (they should only be the latter)?

(Q4) THE (j) TEST FIX. Does `fold.diff` show `test_a_migration_that_cannot_get_its_lock_fails
_in_about_a_second` switched from `db.connect_migration(...)` to `cli._connect(read_only=True)`
for its probe connections (both BEFORE and AFTER, and BEFORE the connection cli._connect is
monkeypatched)? Is this a connection-type fix only — does any assertion change or weaken?

(Q5) ANYTHING ELSE THE FOLD TOUCHED. Does `fold.diff` touch anything beyond
`src/cobalt/db_migrations/cli.py` and `tests/cobalt/test_migrate_proof.py`? Does it touch
`configs/`, `ops/`, or anything reaching scoring, ranking, or a value that lands on a trading
card (L52)? Any secret, credential, path, or connection string visible in the diff? Does it
touch any code belonging to R2, R3, R5, R6-R9 (already closed) or R4 (NOT REAL) — it should
not; name exactly what changed if it does.

(Q6) THE OFFLINE/DB COUNTS, cross-checked against the diff, not just quoted from the report.
`facts.md` says `fold.diff` adds exactly four new `@requires_db` test functions and no other
new `def test_`. Confirm from the diff itself (search for `^+def test_` and for
`@requires_db` immediately above each). Does this account for the report's claimed
`302 skipped` (round 2's 298 + 4) with `1608 passed` unchanged? If the diff shows a different
count of new functions or a missing/misplaced decorator, say so — it would mean the DB-RUN
section's RED/GREEN and skip-count claims are unverified too.

(Q7) THE RESTARTS CLAIM. `db-run-section.md`'s RESTARTS table (for `d860bf7..HEAD`) says only
`com.cobalt.radar`, 0 UNCLASSIFIED. Given `fold.diff` touches only
`src/cobalt/db_migrations/cli.py` under `src/` (tests never restart anything), and round 1's
own classification already put that file's static import reach at `com.cobalt.radar`, is that
claim consistent with the diff's scope? You cannot re-run the command (no rule for it) — say
UNVERIFIABLE FROM READS for the command's own execution, but state whether the SCOPE argument
holds.

(Q8) CARRIED ITEMS UNTOUCHED. Does `fold.diff` show any change to R2's, R3's, R5's, R6-R9's,
or R4's code (already closed or NOT REAL, per `verdicts-r2.md` and round 1's table)? It should
show none beyond F1's own nesting (Q3) — if it shows any other change to those items' code,
name exactly what and whether it was authorized.

End with exactly one line per item, in this exact order:
`R1/R11 (the SET LOCAL move): FIXED / NOT FIXED / REGRESSED`,
`F1 (nested cleanup): FIXED / NOT FIXED / REGRESSED`,
`(j) test fix: FIXED / NOT FIXED / REGRESSED`.
Then, on its own final line:
`VERDICT: FOLD CLEAN / FIX FIRST <item(s)> / FOLD UNSAFE`."
