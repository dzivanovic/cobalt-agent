FACTS — round-2 fold verification (Sonnet hub, Task 1), measured 2026-09-19

## Worktree / tree state
- `git -C /Users/cobalt/cobalt-wt/ops-2026-09-19 status --porcelain` → EMPTY.
- `git -C /Users/cobalt/cobalt-wt/ops-2026-09-19 status` (long form), first two lines:
  `On branch ops/2026-09-19`
  `nothing to commit, working tree clean`

## Commits fc1d967..ops/2026-09-19 (log --oneline, newest first)
```
d860bf7 docs(report): ops 0919 round 2 — tribunal fold R2/R3/R5/R6-R9 built offline, R10 settled 1608/0/298 unchanged, ESCALATE 7
0ec31f8 docs(report): ops-2026-09-19 round-1 report — four wording/count corrections (tribunal round 1, R6-R9)
be79b74 fix(db-migrate): the lock-timeout message points an operator at the lock HOLDER, not ungranted waiters (tribunal round 1, R5)
8ed2beb fix(db-migrate): test (g)'s docstring states the join-vs-probe ordering as what is actually guaranteed (tribunal round 1, R3)
543810f fix(db-migrate): test (g) closes its worker connection on every path, not only the hung one (tribunal round 1, R2)
319eaaa docs(report): ops 0919 — five small fixes built offline, tests first, 1608/0 vs baseline 1562/0, ESCALATE 9
```
`319eaaa` is ROUND 1's own report commit (sits above build tip `fc1d967`, same pattern round
1 itself noted about its own build tip vs report commit) — NOT a round-2 commit, but it IS
inside the `fc1d967..ops/2026-09-19` range because the range is "reachable from tip, not
reachable from fc1d967," and 319eaaa is round 1's report layered on top of fc1d967.

## Code tip vs the report's own stop-line tip
The round-2 report's last line names tip `0ec31f8`. The ACTUAL branch tip is `d860bf7` —
one commit above `0ec31f8`, because `d860bf7` is the commit that ADDS the `## ROUND 2
CLOSE` / `## ROUND 2 ESCALATE` / stop-line section itself (the report necessarily commits
its own closing content one commit after the line it prints, same shape as round 1's
`fc1d967` vs `319eaaa`). Not a discrepancy — matches the established pattern; name it if a
house asks "which commit is the real tip."

## `git diff --stat fc1d967..ops/2026-09-19` (full range, no path filter)
```
 docs/40 - DevDocs/reports/ops-2026-09-19.md | 1001 +++++++++++++++++++++++++++
 src/cobalt/db_migrations/cli.py             |   23 +-
 tests/cobalt/test_migrate_proof.py          |   92 ++-
 3 files changed, 1090 insertions(+), 26 deletions(-)
```
Only 3 paths touched in the whole range. All three are inside `docs/`, `src/`, or `tests/`.
NOTHING under `scratch/`, NOTHING named `.env`, nothing outside `src/`, `tests/`, `docs/`.
The 1001-line report delta is round 1's ENTIRE report body (committed at `319eaaa`, on top
of `fc1d967` which has no report file at all) plus round 2's `0ec31f8` (4 corrections) and
`d860bf7` (the `## ROUND 2` section, ~430 lines) — not evidence of anything odd, just the
report accumulating across the whole range.

## Per-item fix location (file:line, from Read of the real worktree files)
- **R2** (`tests/cobalt/test_migrate_proof.py:1323-1353`, inside the `finally:` block of
  `test_the_alter_waits_for_an_open_transaction_and_then_completes`): `if thread.is_alive():
  conn.cancel(); thread.join(timeout=WORKER_STATEMENT_TIMEOUT_S)` now runs unconditionally
  in `finally`, ahead of the `if not thread.is_alive(): conn.rollback(); conn.close()`. The
  `try` body's old `if hung: conn.cancel(); thread.join(...)` duplicate is gone (one copy,
  L3). MATCHES verdict table's "fix in one line": *"move `cancel`/`join`/`rollback`/`close`
  into the `finally` unconditionally (join with a timeout)"* — yes, exactly this shape.
- **R3** (`tests/cobalt/test_migrate_proof.py:1254-1274`, the docstring's "HOW THIS TEST'S
  CEILINGS RELATE" section): reworded from an unconditional "fires first" to a conditional
  claim — states the 5 s headroom the guarantee actually depends on, and names the failure
  shape (a slow probe / third contending session) under which the server's 25 s timeout can
  fire first instead. No code/timing change — option (a), docstring only. MATCHES the
  verdict table's fix line *"state the ordering as conditional, or start the join deadline
  from `thread.start()`"* — took the first of the two named options; the report says so
  explicitly ("R3: took fix (a) … because …" per the prompt's naming requirement, though the
  report's actual phrase is "fix (a) docstring" in its stop line).
- **R5** (`src/cobalt/db_migrations/cli.py:692-719`, the `except
  psycopg.errors.LockNotAvailable` block): hint query changed from `SELECT pid, mode,
  granted, relation::regclass FROM pg_locks WHERE NOT granted` to a `pg_locks JOIN
  pg_stat_activity … WHERE l.granted AND l.relation IS NOT NULL` (no mode filter, reasoned
  in-line: ACCESS EXCLUSIVE conflicts with every mode, so filtering to that mode would
  usually return nothing). `pg_locks` is kept (not dropped), `pg_stat_activity` is joined
  on. MATCHES verdict table's fix line *"change the hint to list *granted* locks on the
  relation, or `pg_blocking_pids`/`pg_stat_activity`"* — took the granted+`pg_stat_activity`
  join option named there.
- **R6** (report `:162`, was `:157` in round 1's numbering before the R6-R9 edits shifted
  line numbers): "13 failed" → "12 failed", with the 7+5=12 recount inline. Present.
- **R7** (report `:8` headline bullet and the round-1 stop line, now further down the file):
  "1 new + 2 edited" → "1 new + 1 edited" in both places, with the `JOBS_TABLE`-sharing
  reasoning repeated inline. Present.
- **R8** (report, the `git diff --stat main HEAD` note): "three ADDITIONAL paths, all as
  DELETIONS" → "two DELETIONS and one MODIFICATION," with `cto-2026-09-19.md` (M, −60)
  named separately from the two real deletions. Present.
- **R9** (report, item a's dangling pointer): took option (ii) — pointer dropped, replaced
  with a plain statement of the trading-day-before-open case and NO pointer to ESCALATE 1;
  the case is instead carried as `## ROUND 2 ESCALATE` 1 with its own number. Present, and
  the report explains why (ii) over (i): renumbering round 1's own already-committed
  headline/stop-line ESCALATE count (9) was judged worse than moving the item to a new
  section. This is a REAL DESIGN CHOICE, not a dodge — but it does mean round 1's `##
  ESCALATE` list is NOT itself amended to carry the premarket case; a reader who reads
  ONLY round 1's `## ESCALATE` section (not `## ROUND 2 ESCALATE`) will not find it there.

## R10 (offline count) — the 1608/1608 question
Round 1's close: `1608 passed, 298 skipped, 0 failed`. Round 2's close: **also** `1608
passed, 298 skipped, 0 failed` (report also notes `1 xfailed, 15 warnings` this run, not
present in round 1's quoted line — round 1's close line did not mention xfailed/warnings
counts, so this is not comparable either way, just noting the report shows one this time).

Why identical: **no new test FUNCTION was added.** Confirmed by diff —
`git diff fc1d967..ops/2026-09-19 -- tests/cobalt/test_migrate_proof.py | grep -E
"^\+def test_"` returns NOTHING. R2 and R3 both edit the body/docstring of the SAME
existing test function (`test_the_alter_waits_for_an_open_transaction_and_then_completes`)
that round 1 already added — no new `def`. R5 is "tests first" in the sense of adding new
ASSERTIONS to an EXISTING test function
(`test_a_lock_it_cannot_get_rolls_back_and_says_nothing_was_applied`), not a new test
function; that test is a **non-`requires_db` (offline) test** exercised via
`_StatementRecorder`/`_offline_migrate`, so its new assertions DO run in the 1608 count —
they are just assertions bolted onto a test that already existed and was already counted.
R2 and R3's target test, by contrast, IS `@requires_db` (line 1225: `@requires_db` decorator
immediately above `def test_the_alter_waits_for_an_open_transaction_and_then_completes`) —
it is SKIPPED offline in both rounds, so neither R2's nor R3's actual fix has ever executed
under a real Postgres; report says so plainly ("THE REAL RUN IS OWED," carried to ESCALATE
2). Net: R5's assertions ran and went green offline (RED-before/GREEN-after quoted in the
report); R2/R3's fixes are real but their proof is still owed on `cobalt_dev` — the 1608
count is unchanged because nothing new was added to what runs offline, not because nothing
was tested.

## Report-text-only fixes (R6-R9) — presence confirmed by grep
`grep -n "12 failed on"` → line 162, present. All four corrections are marked inline in the
report text as "[corrected in round 2, R#: …]" rather than silently rewritten — matches the
prompt's "show the correction, don't silently edit" instruction.

## Scope check
`git diff --stat fc1d967..ops/2026-09-19` touches exactly: `docs/40 - DevDocs/reports/
ops-2026-09-19.md`, `src/cobalt/db_migrations/cli.py`, `tests/cobalt/test_migrate_proof.py`.
No `configs/`, no `ops/`, no `.env`, no `scratch/`, nothing outside `src/`, `tests/`,
`docs/`. No secret/credential/connection-string text found in either diff file.

## ROUND 2's own ESCALATE section (report's `## ROUND 2 ESCALATE`, one line each)
1. A trading day before premarket open is NOT in item a's bound (new number; carries the
   case R9's dropped pointer used to point at) — unchanged behaviour, ruling owed: leave or
   widen C2.
2. `requires_db` tests never run — now THREE (round 1's two + this round's R2/R3 fix to one
   of them) — real run owed on `cobalt_dev`.
3. b2 half-set band is a design call, carried from round 1, untouched.
4. Item f (`com.cobalt.archiver` disarm) is not a build, carried from round 1, untouched.
5. Cross-branch conflict with `sprint-2/p4` on `db_migrations/cli.py` now has a second hunk
   region (R5's message edit, far from round 1's `DEFAULT_LOCK_TIMEOUT_S` hunk).
6. Round 1's `## ESCALATE` 1-5 stand, unrenumbered; round 1's ESCALATE 2 (BEFORE probe gap)
   IS the tribunal's R1 — same item, not a duplicate.
7. Two differences between the round-2 PROMPT's stated baseline and the actual files,
   both explained, neither changed any work: (a) prompt said round 1's file-suite close was
   "34 passed, 17 skipped" — that's round 1's mid-build (item c) figure; round 1's real
   final figure was "40 passed, 17 skipped" after item e; round 2 measured 40/17 before and
   after, unchanged against the CORRECT baseline. (b) prompt expected `cobalt jobs restarts
   fc1d967..HEAD` to read `com.cobalt.aset com.cobalt.radar`; it reads `com.cobalt.radar`
   only — narrower range (this round touched no day-mode file), not a reclassification; the
   branch-level range `4c14712..HEAD` still derives `com.cobalt.aset com.cobalt.radar`.

## Lessons carried from 18 (for the launched round-2 review session)
1. The Write tool strips trailing whitespace from copied diffs — a unified diff's blank
   context lines are a single space, and Write turns them into empty lines. `fold.diff` in
   this packet has 4 such lines; `fold-report.diff` has 0. When the reviewer copies these
   into `scratch/review-ops-r2-0919/` with Read → Write, expect the copy to be a few bytes
   SHORT, not corrupted — check with `grep -c "^ $"` old vs new, same as 18 did, and note it
   in `## Packet` rather than treating it as a fidelity failure.
2. `git log -- <report path>` on `/Users/cobalt/cobalt` with NO branch named returns EMPTY —
   confirmed again this round (`git -C /Users/cobalt/cobalt log --oneline -4 -- "docs/40 -
   DevDocs/reports/ops-2026-09-19.md"` → nothing) because the report is committed only on
   `ops/2026-09-19`, not on main. The ref must be named explicitly:
   `git -C /Users/cobalt/cobalt log --oneline -4 ops/2026-09-19 -- "docs/40 - DevDocs/
   reports/ops-2026-09-19.md"`.
