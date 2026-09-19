You are an independent reviewer from another house, one of three reading this packet
separately. Read ONLY the files in this folder; you cannot run commands — everything you
need is already here as a file. This is ROUND 2 of the three-house check of branch
`ops/2026-09-19`. Round 1 (`verdicts-r1.md`, the `## Verdict table` from
`/Users/cobalt/cobalt-wt/agy-trial/scratch/review-ops-0919/REVIEW.md`) found 8 REAL findings
(R1-R3, R5-R9; R4 was NOT REAL; R10-R11 were UNVERIFIABLE FROM READS at the time). A build
session then folded fixes for R2, R3, R5, R6, R7, R8, R9 — R1 and R11 are CARRIED (they ride
with an owed `cobalt_dev` experiment another session holds) and R4 got no change (it was
NOT REAL). `fold.diff` is `git diff fc1d967..ops/2026-09-19 -- src tests` — the code and
test changes since round 1's build tip, covering R2/R3/R5. `fold-report.diff` is the same
commit range for the report file only, covering R6-R9's wording corrections and the new
`## ROUND 2` section. `facts.md` is the hub's own pre-computed measurements (commit list,
diff-stat, per-item file:line, the offline-count explanation, the ESCALATE carry-forward) —
treat facts.md as a claim to spot-check against the diffs, same as you would the build's own
report, not as settled truth you may skip verifying.

For each finding give SEVERITY (BLOCKER = the fix does not do what round 1 asked, breaks an
existing invariant, or contradicts a LAW (L1 fail-loud, L3 one-path, L45 real-shape
fixtures, L52 nothing here may touch scoring/ranking/cards) / MAJOR / MINOR), FILE + LINE
(from the diff), the EVIDENCE you read (quote it), and the FAILING SCENARIO; say "none
found" rather than inventing.

(Q1) R2 — `test_the_alter_waits_for_an_open_transaction_and_then_completes`'s cleanup. Does
`fold.diff` move `conn.cancel()` + `thread.join(...)` into the `finally` block
UNCONDITIONALLY (not gated on `if hung:` anymore), ahead of the `if not
thread.is_alive(): conn.rollback(); conn.close()` line? Is the old `try`-body copy of
`cancel`/`join` actually REMOVED (one copy only, L3), or does the diff leave a second copy
behind? Does the fix change what the test's own assertions check (`assert not hung`, the
`_verdict(...)` check) — it should not; this is cleanup-path hygiene only.

(Q2) R3 — the "20 s join fires first" docstring. Does `fold.diff` show the docstring's claim
made CONDITIONAL (naming the 5 s headroom / probe-speed dependency it actually relies on),
rather than removed or left unconditional? Is this a docstring-only change (`fix (a)` per
`facts.md`), or does the diff also touch the join/timeout CODE (`fix (b)`) — if both a
docstring AND a timing change appear, is that consistent with round 1's verdict table, which
asked for "your call, name which you chose," or is a mix undisclosed?

(Q3) R5 — the lock-timeout message. Does `fold.diff` show the `except
psycopg.errors.LockNotAvailable` hint text in `db_migrations/cli.py` changed away from
`pg_locks WHERE NOT granted`? Does the new text query for a GRANTED lock (or use
`pg_blocking_pids`/`pg_stat_activity`), i.e. does it now identify a HOLDER rather than a
waiter? Does the rest of the message (NOTHING WAS APPLIED, the lock_timeout value, the
retry guidance, `Postgres said: {e}`) stay untouched — quote the surrounding lines to check.
Does `fold.diff` show a NEW or CHANGED assertion in
`test_a_lock_it_cannot_get_rolls_back_and_says_nothing_was_applied` that is FALSE against
the OLD message text and TRUE against the new one (i.e. is this genuinely tests-first, not
just a code edit with no test change)? Is the existing `assert "pg_locks" in message`
removed — if so, is that consistent with the fix (did the fix actually drop `pg_locks`
entirely), and if not removed, is `pg_locks` really still present in the new message text?

(Q4) R6-R9 — read `fold-report.diff` for the corrected lines only (ignore the ~430-line new
`## ROUND 2` section for this question). For each of R6 (the "13 failed" → recount), R7 (the
"1 new + 2 edited" → "1 new + 1 edited," both the headline bullet and the stop line), R8
(the "all as DELETIONS" wording), and R9 (the dangling ESCALATE-1 pointer): does the diff
show the exact correction the verdict table asked for? Quote before/after from the diff.
Is each correction marked INLINE as a correction (not a silent rewrite that erases the
original wrong text with no trace)?

(Q5) R9 specifically — `facts.md` says the fix took "option (ii): pointer dropped," and that
the premarket-before-open case is instead carried in the report's NEW `## ROUND 2 ESCALATE`
section (not added to round 1's own `## ESCALATE` list, to avoid invalidating round 1's
already-committed "ESCALATE: 9" stop line). Does `fold-report.diff` support that account —
is round 1's `## ESCALATE` section actually left untouched (no new entry inserted, no
renumbering), and does a genuinely new numbered item appear in a `## ROUND 2 ESCALATE`
section instead? Is this an honest resolution of R9, or does it just move the same gap
somewhere a reader of round 1's list alone would still miss it — say which, and if you think
it is dishonest or inadequate, say exactly why.

(Q6) THE OFFLINE COUNT. `facts.md` claims the suite stayed at "1608 passed, 298 skipped, 0
failed" in both rounds because no new test FUNCTION was added — R2/R3 edit the body of an
EXISTING `@requires_db` test (skipped offline either way), and R5 adds assertions to an
EXISTING offline test. Does `fold.diff` support this — grep-style, does any `+def test_`
line appear anywhere in the diff? Is the test R5 modifies actually NOT decorated
`@requires_db` (i.e. does it really run offline, so its new assertions are real red/green
evidence and not silently skipped too)? Is the test R2/R3 modify actually decorated
`@requires_db` (confirm the decorator sits directly above it)? If any of this doesn't hold,
say so plainly — it would mean the round-2 report's RED/GREEN claim for R5 is unverified
too.

(Q7) DID THE FOLD BREAK ANYTHING new — cross-cutting. Does `fold.diff` touch anything
outside `src/cobalt/db_migrations/cli.py` and `tests/cobalt/test_migrate_proof.py`? Does it
touch `configs/` or `ops/`? Does anything in the diff reach scoring, ranking, or a value
that lands on a trading card (L52)? Any secret, credential, path, or connection string
visible in either diff? Does the diff introduce a second copy of a rule/helper that already
exists elsewhere (L3), beyond what R2's own comment claims ("only one copy")?

(Q8) CARRIED ITEMS — R1, R4, R11. `facts.md` and the round-2 report both say R1 (the BEFORE
probe outside the lock_timeout ceiling) and R11 (whether `SET LOCAL` moves a REPEATABLE READ
snapshot) are CARRIED, out of scope for this fold, owed to a `cobalt_dev` experiment another
session holds — and R4 (the `code:` line ordering) was NOT REAL in round 1 and got no
change. Does `fold.diff` show ANY change touching R1's or R4's code (the `_probe_all`/`SET
LOCAL lock_timeout` placement at the top of `cmd_migrate`, or the `code:`/`FAILED:` ordering
at the bottom)? It should show none — if it shows any, name exactly what changed and whether
it was authorized.

End with exactly one line, per round-1 finding, in this exact order: `R2: FIXED / NOT FIXED
/ REGRESSED`, `R3: FIXED / NOT FIXED / REGRESSED`, `R5: FIXED / NOT FIXED / REGRESSED`, `R6:
FIXED / NOT FIXED / REGRESSED`, `R7: FIXED / NOT FIXED / REGRESSED`, `R8: FIXED / NOT FIXED /
REGRESSED`, `R9: FIXED / NOT FIXED / REGRESSED`. Then, on its own final line: `VERDICT: FOLD
CLEAN / FIX FIRST <finding numbers> / FOLD UNSAFE`.
