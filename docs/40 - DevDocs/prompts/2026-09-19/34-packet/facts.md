FACTS — round-3 fold verification (Sonnet hub, Task 1), measured 2026-09-19

## Why round 3 exists
Round 2 reviewed the fold up to tip `d860bf7` (its own report tip; `fc1d967..d860bf7 -- src
tests` was round 2's `fold.diff`). A DB-run session then made a CODE change on top of that
tip — the R1/R11 `SET LOCAL lock_timeout` placement move — which is new code no house has
read. L67: the houses' LAST round (round 3 of ≤3), on that fold only, not the whole branch
again.

## Worktree / tree state (checked directly, this hub)
- `git -C /Users/cobalt/cobalt-wt/ops-2026-09-19 status --short` → EMPTY.
- `ls -la /Users/cobalt/cobalt-wt/ops-2026-09-19/.env` → No such file or directory (only
  `.env.example` present).

## Commits d860bf7..ops/2026-09-19 (log --oneline, newest first)
```
a868a69 docs(report): ops 0919 db run — R1/R11 settled on cobalt_dev, with-DB suite green 61/0, ESCALATE 12
be00506 fix(db-migrate): test (j) probes through a transaction, not an autocommit connection (first real run on cobalt_dev)
e5802df docs(report): ops-2026-09-19 — F3/F4/F5 report-text folds (tribunal round 2)
d013b6b fix(db-migrate): test (g)'s finally nests other/watcher cleanup so the worker cleanup always runs (tribunal round 2, F1)
65ee9e8 fix(db-migrate): SET LOCAL lock_timeout moved ahead of the BEFORE probe — R1/R11 settled on cobalt_dev (ops DB run)
```
`d860bf7` is round 2's own reviewed tip (base, not in the range). `e5802df` and `a868a69` are
docs-only (the report file) — `git diff --stat d860bf7..ops/2026-09-19 -- docs` shows only
`docs/40 - DevDocs/reports/ops-2026-09-19.md`, 822 insertions / 3 deletions, no `src`/`tests`
path. `fold.diff` in this packet is `git diff d860bf7..ops/2026-09-19 -- src tests`, so it
carries exactly the other three commits' code: 65ee9e8 (R1/R11 move + its new §12 tests),
d013b6b (F1 nesting), be00506 (the (j) test's autocommit-cursor fix).

## `git diff --stat d860bf7..ops/2026-09-19 -- src tests`
```
 src/cobalt/db_migrations/cli.py    |  76 +++---
 tests/cobalt/test_migrate_proof.py | 504 ++++++++++++++++++++++++++++++++-----
 2 files changed, 495 insertions(+), 85 deletions(-)
```
Exactly two paths. Nothing under `configs/`, `ops/`, `.env`, or `scratch/`. No secret,
credential, or connection-string text in `fold.diff` (checked: `password|secret|api_key|
COBALT_MASTER_KEY` all zero hits).

## New test functions in `fold.diff` (`grep -n '^+def test_'`)
```
test_connects_show_server_encoding_does_not_take_the_snapshot            (k)
test_a_bare_set_local_does_not_take_the_snapshot_either                  (l)
test_the_instrument_can_see_a_snapshot_that_is_already_fixed             (m, negative control)
test_a_blocked_before_probe_is_under_the_lock_ceiling_too                (n, the coverage test)
```
All four are new §12 tests for R1/R11, all `@requires_db` (skip offline). `be00506`'s (j) fix
edits an EXISTING test function, no new `def`; `d013b6b`'s F1 fix edits the EXISTING `finally`
block of `test_the_alter_waits_for_an_open_transaction_and_then_completes`, no new `def`. This
is why the report's offline count stays `1608 passed` (no new offline-visible test), with
`302 skipped` (+4 over round 2's 298 — exactly these four).

## The R1/R11 code change itself (`src/cobalt/db_migrations/cli.py`, `cmd_migrate`)
Two lines swap order in the `try:` block: `conn.execute(f"SET LOCAL lock_timeout = …")` now
runs BEFORE `before = _probe_all(conn)` (previously after). One statement, one line moved —
covers forward and rollback alike (`cmd_migrate` has one non-`--proof-only` path). The
docstring section "THE LOCK CEILING, AND WHERE THE `SET LOCAL` SITS" is rewritten in the same
hunk to state the settled result and name the three tests.

## Report claims this packet does NOT let a house independently confirm
- **The coverage test's red-first** (`### The probe-coverage test, and its red-first`,
  `db-run-section.md`): the report narrates reverting the code, re-running
  `test_a_blocked_before_probe_is_under_the_lock_ceiling_too`, seeing `1 failed in 35.47s`,
  then restoring the fix. That revert-and-rerun is NOT itself a commit — `git log` has no
  intermediate state — so a house reading only `fold.diff` (the final state) cannot verify the
  red run happened; it can only check that the test's own logic (a 30s server-side
  `statement_timeout` backstop, a real `LOCK TABLE … ACCESS EXCLUSIVE` held by another
  session, `_probe_all` NOT stubbed) would in fact depend on the move — i.e., that the test is
  SHAPED to fail under the old placement, not that it was observed to. Treat the timing
  numbers (7.65s green, 35.47s red) as the hub's own report's claim (`facts.md` standing, per
  L35) — same as round 2's Q6 treated the offline-count claim.
- **RESTARTS**: `db-run-section.md`'s own RESTARTS table (`com.cobalt.radar`, 0 UNCLASSIFIED,
  `d860bf7..HEAD`) is a command-output quote in the packet, not re-run by this hub (this
  launch line carries no `Bash(uv run cobalt jobs restarts *)` rule, same gap round 2 named).
  Checkable only by reasoning: the only `src/` path in `fold.diff` is
  `src/cobalt/db_migrations/cli.py`, which round 1 already classified to `com.cobalt.radar`'s
  static import reach — no new path, so no reason for a different restart target.

## Scope check (this hub, against the real worktree)
`fold.diff` touches only `src/cobalt/db_migrations/cli.py` and
`tests/cobalt/test_migrate_proof.py`. No scoring/ranking/card reach (L52) — the only
production hunk is the `SET LOCAL`/probe reorder and its docstring, diagnostic/DDL-ordering
code, not a card value. No second copy of the cleanup or the lock-timeout logic introduced
(L3) — one `SET LOCAL lock_timeout` call site, before and after.

## Packet fidelity note
`fold.diff` has 15 blank-context lines (`grep -c "^ $"`) — expect Write-tool copies into
`scratch/` to land a few bytes short, same LESSON as rounds 1 and 2; note it in `## Packet`,
not as a defect.
