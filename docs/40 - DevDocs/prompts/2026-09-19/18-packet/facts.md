# facts.md — measured by the CTO desk, read-only, 2026-09-19, fresh `git -C` reads (no memory, no re-use of an earlier run's numbers)

## Commits `main..ops/2026-09-19`
```
319eaaa docs(report): ops 0919 — five small fixes built offline, tests first, 1608/0 vs baseline 1562/0, ESCALATE 9
fc1d967 feat(db-migrate): the proof names the code it ran from — code: <sha> (clean|DIRTY) as the last output line (09-19 deploy check, known limit)
739b14d test(db-migrate): the lock-wait test cannot leave a waiting backend behind; the blocked-lock probe looks at the worker's own ACCESS EXCLUSIVE request (Astra A1, A2)
f960715 feat(db-migrate): lock_timeout on the migrate transaction — a DDL that cannot get its lock fails in 30 s instead of hanging the deploy (proof-only-3 ESCALATE 3)
86da5a8 fix(daymode): the trade-count band refuses an inverted or non-integer band — one validator for propose and validate (09-18 review F2)
8232dcc fix(dayopen): C2 passes on a non-trading day — no session, no rows, no false AMBER (09-19 Saturday day-open)
```
Six commits: five build commits (one per item) + the report commit on top.

## Tip, main, merge-base
- `git -C /Users/cobalt/cobalt log --oneline -1 ops/2026-09-19` → `319eaaa` (the report commit; the build tip proper, i.e. the last CODE commit, is `fc1d967` — the report commits above it, as its own §0 says).
- `git -C /Users/cobalt/cobalt log --oneline -1 main` → `fc4acd6` ("docs(desk): 09-19 R11 one-time push done … ops-0919 stop line, hub ended") — main has moved AGAIN since this branch was cut, and again since this branch's own build report was written (which saw main at `3723d86`). Every move since branch point is a desk docs-only commit.
- `git -C /Users/cobalt/cobalt merge-base main ops/2026-09-19` → `4c14712` — unchanged branch point; main has not been rebased onto or merged into this branch.

## Diff-stat, `main..ops/2026-09-19 -- src tests configs ops`
```
 src/cobalt/cli.py                   |  18 +-
 src/cobalt/daymode/cli.py           |  19 +-
 src/cobalt/daymode/propose.py       |  65 +++++
 src/cobalt/dayopen/checks.py        |  14 +-
 src/cobalt/db_migrations/cli.py     | 140 +++++++++++
 tests/cobalt/test_daymode.py        | 152 ++++++++++++
 tests/cobalt/test_dayopen_checks.py |  45 ++++
 tests/cobalt/test_migrate_proof.py  | 477 +++++++++++++++++++++++++++++++++++-
 8 files changed, 917 insertions(+), 13 deletions(-)
```
`git -C /Users/cobalt/cobalt diff --stat main..ops/2026-09-19 -- configs ops` → EMPTY: neither `configs/` nor `ops/` is touched by this branch.
`code.diff` in this packet was re-diffed fresh against this same range/pathspec just now and is **BYTE-IDENTICAL** to this stat (`diff` of the two exit-0) — main's docs-only advances since the branch was cut do not touch `src`/`tests`/`configs`/`ops`, so the scoped diff is unaffected and does not need to be regenerated again before the reviewers read it.

## File:line confirmation, per item (read fresh off `git -C /Users/cobalt/cobalt show ops/2026-09-19:<path>`, not off any report's claim)
- **a — C2 guard**, `src/cobalt/dayopen/checks.py`: `:173` comment naming C3's guard, `:174` `windows = clock.windows_for(report_date)`, `:175-176` `if not windows and count == 0:` (the PASS branch) — the calendar read sits ahead of the old FAIL check, matching the spec's bound. C3's own `windows_for` read is a separate line, `:242`.
- **b1 — band validator**, `src/cobalt/daymode/propose.py`: `:89` `class BandError(ValueError):`, `:94` `def validate_band(band_min, band_max) -> None:`. Callers: `src/cobalt/cli.py` `:166` imports it, `:234` calls `validate_band(band[0], band[1])`; `src/cobalt/daymode/cli.py` `:34` imports it, `:78` calls `validate_band(out[0], out[1])`. Exactly two call sites — no third copy found.
- **c — lock_timeout**, `src/cobalt/db_migrations/cli.py`: `:122` `DEFAULT_LOCK_TIMEOUT_S = 30`, `:616` reads `args.lock_timeout_s` via `getattr(..., DEFAULT_LOCK_TIMEOUT_S)`, `:664` `conn.execute(f"SET LOCAL lock_timeout = '{lock_timeout_s}s'")`, `:769/:772` the CLI flag and its help text, `:790` exported in `__all__`.
- **d — A1/A2**, `tests/cobalt/test_migrate_proof.py`: `:1009` `WORKER_STATEMENT_TIMEOUT_S = 25`, `:1056` `def _wait_for_a_blocked_lock(watcher, table, ceiling, pid) -> bool:` (the `pid` parameter is present), `:1281` `SET LOCAL statement_timeout`, `:1289` the call site passing the new arg, `:1307` `thread.join(timeout=WORKER_STATEMENT_TIMEOUT_S)` on the cleanup path.
- **e — code line**, `src/cobalt/db_migrations/cli.py`: `:128` `CODE_ROOT = Path(__file__).resolve().parents[3]`, `:131` `def _code_line() -> str:`, `:159/:161` calls into `_git(CODE_ROOT, ...)`, `:165` builds the `code: {sha} ({state}) · {CODE_ROOT}` line, `:789` exported in `__all__`.

## Worktree state
`git -C /Users/cobalt/cobalt-wt/ops-2026-09-19 status --porcelain` → EMPTY (clean), read fresh just now.

## Not re-verified here (out of this facts file's scope, already covered elsewhere)
The suite counts, the `RESTARTS:` table, and the nine `## ESCALATE` items are `build-report.md`'s own claims in this packet — the reviewers are told in `QUESTIONS.md` to treat them as claims, not as facts pre-confirmed by this file.
