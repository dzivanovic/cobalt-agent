You are an independent reviewer from another house, one of three reading this build separately. This
is ROUND 2 of the three-house check of branch `archiver/append-0919`. Read ONLY the files named in your
launch instruction; you cannot run commands — everything you need is already here as a file.

Round 1 (`verdicts-r1.md`) found 7 REAL findings — F1 (BLOCKER: `restate --apply` writes bars via
`upsert_bars` on its own connection, so a failed pre-commit re-check cannot roll them back), F2 (MAJOR:
the two named §8 boundary tests only call `quiet_verdict`, never the real command), F3/Q10 (MAJOR: no
differing-value/equal-value race test existed), F4 (MAJOR: four tests assert on names/attributes, not
behaviour), F5 (MAJOR: exit code 2 unreachable through the production `cobalt` entry), F6 (MINOR: the
shadow artifact's night uses the UTC date of a UTC instant, not the ET trading date), F7 (MINOR: the
migration test doesn't pin `NULLS NOT DISTINCT`). A round-2 build session then fixed all seven.
`fold.diff` is `git diff c974fbf..archiver/append-0919 -- src tests configs` — everything that changed
since round 1's code tip, covering all seven fixes. `facts.md` is the desk's own pre-computed
measurements (commit list, diff-stat, a file:line confirmation for each F1–F7 fix) — treat it as a claim
to spot-check against the diff, not settled fact. `build-report.md` is the branch's own account
(round 1 + round 2 sections) — also a claim, never settled fact.

For each finding give SEVERITY (BLOCKER = the fix does not do what round 1 asked, breaks an existing
invariant, or contradicts a LAW (L1 fail-loud, L3 one-path, L45 real-shape fixtures, L52 nothing here
may touch scoring/ranking/cards, L57 replayable/reconciling values) / MAJOR / MINOR), FILE + LINE (from
`fold.diff`), the EVIDENCE you read (quote it), and the FAILING SCENARIO; say "none found" rather than
inventing.

(Q1) F1 — does `fold.diff` show `_apply_restate` now taking a `conn` parameter and writing bars through
a CONNECTION-TAKING method (not the connection-opening `upsert_bars`)? Is that write, the incident
write, and `guard.check_before_commit()` all inside the SAME `target_transaction()` block, with the
re-check running AFTER both writes (so a raise there rolls both back)? Is there now only ONE copy of the
`ON CONFLICT … DO UPDATE` SQL statement (L3), or did the fix introduce a second copy?

(Q2) F1 sibling — does `fold.diff` show ANY change to `_cmd_backfill_missing` beyond what round 1 already
had? The report claims it needed no fix because it already wrote via `insert_new_bars(conn, …)` inside
its own transaction — confirm this from the diff (or from what the diff does NOT touch), not from the
report's say-so.

(Q3) nightly `upsert` path — does `fold.diff` touch `runner.py`'s nightly `upsert`-mode write call
(`store.upsert_bars(bars)`, no connection argument) in ANY way other than the F6 date-derivation line?
Is `store.upsert_bars` (the connection-OPENING method, not the new `_on` sibling) still present,
unchanged in its own connect/commit shape, so the nightly night behaves exactly as round 1 shipped it?

(Q4) F2 — do the two named tests (`test_gemini_close_boundary_poller_lag`,
`test_astra_open_boundary_repair_crosses_open`) now take a `monkeypatch` fixture and actually invoke the
real command path (`_cmd_restate`/`_cmd_backfill_missing` or `HANDLERS[...]`), not just `quiet_verdict`
directly? Quote the call that proves it.

(Q5) F3/Q10 — does `fold.diff` contain tests for BOTH a differing-value race (poller and repair disagree
on the value, with the surviving value asserted) AND an equal-value race (poller and repair agree, and
nothing spurious happens)? Name them file:line. Are these offline (fakes) or `requires_db` twins, and
does the choice match L45 (never stretching a fake to claim a guarantee only a real transaction can
prove)?

(Q6) F4 — for each of the four tests round 1 named, does the rewritten version actually INVOKE a
command/handler (not just recompute `quiet_verdict` or monkeypatch something never called)? Quote the
invocation for at least two of the four.

(Q7) F5 — does `fold.diff` show a NEW except-clause in `cobalt/cli.py`'s `main()`, placed BEFORE the
generic `except Exception`, catching `(QuietRefused, ArchiveLockError)` and calling
`sys.exit(e.exit_code)`? Does `ArchiveLockError` gain an `exit_code = 2` class attribute? Is every OTHER
exception's behaviour (generic `Exception` → exit 1, `JobStopped` → exit 0) left untouched — quote the
surrounding lines to confirm nothing else in that `try/except` block moved.

(Q8) F6 — does the fix derive the shadow night from an ET-converted date (via the codebase's existing
`SessionClock.to_et`, not a new timezone library or a hand-rolled UTC offset)? Is this the ONLY behaviour
change in `runner.py`, or did the diff also touch anything else in that file?

(Q9) F7 — does the new assertion in `test_incidents_has_the_partial_unique_index_on_unresolved_rows`
check for `NULLS NOT DISTINCT` in the actual SQL text the test reads, and does the existing SQL genuinely
already have it (i.e. is this purely a test-coverage fix, not a code change)?

(Q10) DID THE FOLD BREAK ANYTHING NEW. Does `fold.diff` touch anything outside
`src/cobalt/archiver/{cli,runner,store}.py`, `src/cobalt/cli.py`, and the named test files? Does it
touch `configs/` or `ops/`, or anything under `src/cobalt/radar/`? Does anything in the diff reach
scoring, ranking, or a value that lands on a trading card (L52)? Any secret, credential, path, or
connection string visible anywhere?

(Q11) Does `build-report.md`'s ROUND 2 section's own numbers (the CLOSE suite line, the +16/+5 test
counts, the RESTARTS table, the four `## ROUND 2 ESCALATE` items) hold up against `fold.diff` and
`facts.md`? Name any claim you cannot confirm, marking it UNVERIFIABLE FROM READS rather than assuming
it is true.

End with exactly one line per round-1 finding, in this exact order:
`F1: FIXED / NOT FIXED / REGRESSED`, `F2: FIXED / NOT FIXED / REGRESSED`,
`F3/Q10: FIXED / NOT FIXED / REGRESSED`, `F4: FIXED / NOT FIXED / REGRESSED`,
`F5: FIXED / NOT FIXED / REGRESSED`, `F6: FIXED / NOT FIXED / REGRESSED`,
`F7: FIXED / NOT FIXED / REGRESSED`.
Then, on its own final line: `VERDICT: FOLD CLEAN / FIX FIRST <finding numbers> / FOLD UNSAFE`.
