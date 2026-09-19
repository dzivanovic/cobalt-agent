You are an independent reviewer from another house, one of three reading this packet separately.
Read ONLY the files in this folder; you cannot run commands — everything you need is already here
as a file. `spec-final-design.md` is the tribunal-derived FINAL design this build was told to build;
`spec-17-build-prompt.md` is the literal build prompt the builder read. `code-01` through `code-05`
are five files, split by area, that together ARE the whole non-docs diff `main...archiver/append-0919
-- src tests configs ops` (328,366 bytes total, split only because that exceeds a comfortable single
read). `facts.md` is the desk's own pre-computed measurements (commits, tip, merge-base, diff-stat,
file:line per claimed item) — read it, but VERIFY its claims against the `code-*.diff` files yourself
where you can; it is the desk's own account, not settled fact. `build-report.md` is the builder's own
account of its work — treat every claim in it as a CLAIM to verify against the diffs, never as settled
fact.

This code has not merged, does not run against production today, and its 18 `requires_db` tests have
NEVER run (offline build, no `.env`, no `cobalt_dev`). It is queued for a deploy that will run two new
migrations against a live production Postgres 16 database with an 8.4M-row `bars` table, for a
trading-support system, and then run in `upsert` mode (today's behaviour, unchanged except for one new
advisory lock) for N shadow nights before anyone considers switching it to `append`.

For every finding give SEVERITY (BLOCKER = the code does not do what the design required, breaks an
existing invariant, or contradicts a LAW (L1 fail-loud, L3 one-path, L10 config-validated-on-load, L45
real-shape fixtures, L52 nothing here may touch scoring/ranking/cards, L57 replayable/reconciling
values) / MAJOR / MINOR), FILE + LINE (from the `code-*.diff` files), the EVIDENCE you read (quote it),
and the FAILING SCENARIO; say "none found" rather than inventing.

(Q1) MODE ISOLATION (design §5): does `code-03-runner-shadow-quiet-cli-heartbeat.diff` show the
`write_mode` dispatch happening BEFORE any append-specific step, with the `upsert` branch sending the
WHOLE export through `upsert_bars` exactly as today, no completeness filter, no range cut, no
comparison gate, no withholding, no `archive_progress` write, no incident write? Is the "complete list"
of what an `upsert` night now does beyond today (the advisory lock, the pre-write shadow compare, one
`shadow` key in `job.result` plus one artifact file) actually the COMPLETE list — does anything else
change in the `upsert` path?

(Q2) THE SHADOW COMPARE (design §5): does it run strictly AFTER the fetch and BEFORE that target's
write? Is it read-only (no write method of the store called)? Does an exception or timeout inside it
leave the target's `upsert_bars` call and the run summary IDENTICAL to a shadow-off night — i.e. can a
shadow failure ever change what gets written or how the night is reported?

(Q3) THE RE-CHECK INSIDE THE REPAIR TRANSACTION BEFORE COMMIT (design §8): `facts.md` names
`src/cobalt/archiver/quiet.py:311` (`check_before_commit`) and `src/cobalt/archiver/cli.py:287,315`
as the call sites inside `_cmd_restate` / `_cmd_backfill_missing`. Confirm from `code-01`/`code-03`
(quiet.py is in `code-03`) that Q1–Q3 are genuinely re-evaluated a second time, immediately before
COMMIT, not merely at command start — and that a failed re-check actually rolls the transaction back
(no bar row surviving the write). Do the two NAMED tests in `code-05-tests-quiet-reconcile-runner.diff`
(`test_gemini_close_boundary_poller_lag`, `test_astra_open_boundary_repair_crosses_open`) genuinely
exercise this, or only the start-time check?

(Q4) `late` = key ≤ PREVIOUS `archived_through` (design §7's counting identities): find the exact
comparator in `reconcile.py` (`code-02-reconcile-store.diff`). Is it `<=` (matching the design's "key
≤ the previous archived_through") or something else (`<`, or a derived boundary)? Quote the line.

(Q5) THE FIVE INCIDENT KINDS (design §11): does `code-01-settings-migrations-config.diff`'s
`0011_archive_incidents.sql` CHECK constraint enumerate EXACTLY `gap, restated, stored_only,
empty_export, regression` — five, no more, no fewer? Is the partial unique index genuinely
`WHERE resolved_at IS NULL`, and does it use `NULLS NOT DISTINCT` (the report claims this was a
deliberate addition for `empty_export` rows, which have no `range_start`) — is that addition actually
present in the SQL, and is it syntactically valid for Postgres 15+/16?

(Q6) MODE ISOLATION + THE ADVISORY LOCK IN `upsert` MODE (design §9): `facts.md` cites
`src/cobalt/archiver/runner.py:95-97` for "the lock, in BOTH write modes." Confirm from `code-03` that
the lock genuinely wraps BOTH the `upsert` and `append` dispatch paths (not just one), that it is
SESSION-level (not transaction-level), ONE constant key, and that a second holder refuses loudly rather
than silently interleaving.

(Q7) IS PRODUCTION BEHAVIOUR IN `upsert` MODE UNCHANGED apart from that lock (plus the shadow read and
its one `job.result` key)? Walk the `upsert` branch in `code-03` end to end and name anything you find
that is NOT on the design's short list.

(Q8) ARE THE MIGRATIONS SAFE ON A LIVE POSTGRES 16 WITH A LARGE `bars` TABLE? Both new tables are
additive and unrelated to `bars` (no ALTER, no index, no trigger on `bars` itself) — confirm this from
`code-01`. Is there anything in the two `CREATE TABLE` statements or their rollbacks that could lock or
scan `bars`, or that is not a plain additive `CREATE TABLE IF NOT EXISTS` / `DROP TABLE`?

(Q9) DO THE TESTS PROVE WHAT THEY CLAIM? Spot-check `code-04` and `code-05` against `build-report.md`'s
per-chunk tables: pick at least three test names the report cites as proving a specific requirement,
read the actual test body in the diff, and say whether it proves what the report says it proves, or
merely runs without asserting the claimed property.

(Q10) THE ONE NAMED GAP THIS HUB ALREADY FOUND: `facts.md`'s "Design test list (§15) vs tests actually
in the diff" section says the design's quiet-window bullet asks for "differing-value and equal-value
races" and this hub could not find a test with that shape — the two named boundary tests and the
pre-commit-recheck test all assert only "no bar row changed," never a scenario where the poller and a
repair write DIFFERENT values vs the SAME value in a race and the outcome is checked. CONFIRM OR REFUTE
this from the real diff (`code-05`): is there a test that actually races a differing value against an
equal value, and if you find one, name it exactly (file:line); if you agree none exists, say so plainly
— this is the single most load-bearing verification of this review.

(Q11) CROSS-CUTTING: does anything in the diff touch `src/cobalt/radar/` (the report and `facts.md`
both claim EMPTY — verify from `code-01` through `code-05`, which together are the WHOLE non-docs
diff, so a radar path would have to appear in one of them if it existed)? Does anything reach scoring,
ranking, or a value that lands on a trading card (L52)? Any secret, credential, path, or connection
string visible anywhere in the five `code-*.diff` files? Is `configs/cobalt/taxonomy/tunables.yaml`
the ONLY config file touched, and is it an edit to an EXISTING file (not a new file under a location
the config boundary law would forbid)?

(Q12) Does `build-report.md`'s own narrative (the BASELINE/CLOSE numbers, the 8 numbered ESCALATE
items, the §14 OPEN-item table, the RESTARTS line) hold up against the `code-*.diff` files and
`facts.md`? Name any claim in the report you cannot confirm from the files given, marking it
UNVERIFIABLE FROM READS rather than assuming it is true.

End with exactly one line: `VERDICT: BUILD CLEAN / FIX FIRST <finding numbers> / BUILD UNSAFE`.
