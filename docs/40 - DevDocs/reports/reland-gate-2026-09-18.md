# Re-land + gate — `reland-gate-0918`, 2026-09-18

## §0 Headline

- **Part A DONE.** Review finding F1 folded: `_probe` sends ONE statement, the row count comes out of the fold, `bars` is read once. 19 red before → 30 passed with the DB / 24 passed + 6 skipped offline.
- Authorization VERIFIED against main: R13 (17:05 ET, "It's approved.") carries the one new rule `Bash(git switch -c sprint-2/stack main)`; every other rule is R1 list (1) / R2 / R7. No mismatch.
- PREFLIGHT: 5 probes, 0 denials.
- Parts B (re-land on `sprint-2/stack`) and C (the gate, with the database) still to run.
- ESCALATE so far: 0.

## PREFLIGHT

| rule | command | exit | result |
|---|---|---|---|
| `git status*` | `git status` | 0 | allowed — `On branch sprint-2/cards`, clean |
| `git log*` | `git log -1` | 0 | allowed — `123f0b0` (PROD PROOF DONE report commit) |
| `date*` | `date` | 0 | allowed — `Fri Sep 18 17:05:40 EDT 2026` |
| `git cherry-pick *` | `git cherry-pick -h` | 129 | allowed (129 = usage, the expected exit) |
| `uv run pytest *` | `uv run pytest --co -q tests/cobalt/test_migrate_proof.py` | 0 | allowed — 17 tests collected |
| authorization | `git -C /Users/cobalt/cobalt log --oneline -8 -- "docs/40 - DevDocs/reports/"` | 0 | allowed — `b7303c7 docs(desk): 09-18 R13 — re-land branch rule approved 17:05 ET` on main |

No denial at any point.

### Authorization, rule by rule (`cto-2026-09-18.md` §4, committed on main)

| launch-line rule | approved by |
|---|---|
| `cp`/`rm`/`ls -la` the `.env` by path | R1 list (1) — ".env cp/rm/ls by path" |
| `COBALT_ENV=dev uv run cobalt db migrate*` | R1 list (1) |
| `COBALT_ENV=dev uv run pytest *`, `uv run pytest *`, `COBALT_VAULT_PATH=… uv run pytest *` | R1 list (1) |
| `COBALT_ENV=dev uv run cobalt validate*`, `settings load *--dry-run*` | R1 list (1) |
| `uv run cobalt jobs restarts *` | R1 list (1) |
| `git cherry-pick *` | R2 (07:01 ET, this worktree) |
| `git switch -c sprint-2/stack main` | **R13 (17:05 ET, "It's approved.")** — the one new rule |
| git add/commit/diff/status/log/show/rev-parse, `git -C ~/cobalt log*`/`rev-parse *`, cd/ls/grep/tail/wc/shasum/date | R1 list (1) |

`git rebase main` is in R1's list and is NOT in this launch line — correctly, a merged-then-reverted branch is never re-landed by rebase (`UNATTENDED-LAUNCH.md` §6). No production command, no push, no merge, no vault write in the list.

## A. Review finding F1 — folded

**The defect.** `_probe` ran `SELECT count(*)` and then the streamed digest as two statements. The harness's connection is READ COMMITTED, so each statement takes its own snapshot: on a table being written to, the printed `rows` could belong to one snapshot and the `digest` to another — a self-contradictory proof line or a false `CHANGED` — and `system.bars` (8,591,339 rows on production) paid for two full passes.

**The fix.** The count is taken INSIDE the fold: `_digest_rows` returns `(rows, digest)`, counting the rows the cursor yields, so one statement produces both numbers and `bars` is read once. The digest bytes are untouched — same rows, same order, same `b"|"` between them — so every digest keeps its value and old proof tables stay comparable.

| test (new or changed) | red before | green after |
|---|---|---|
| `test_the_fold_reports_how_many_rows_it_folded` (×7 cases) | `ValueError: too many values to unpack (expected 2)` | rows folded == rows reported, digest unchanged |
| `test_the_streamed_fold_reproduces_string_agg_byte_for_byte` (×7) | `assert '9' == '4975b5a9ab7e…'` (unpacked a str) | byte-for-byte equal to `md5('|'.join(rows))` |
| `test_no_rows_digests_the_empty_string`, `…separator…never_after_the_last` | `assert 'd41d8cd98f00b204e9800998ecf8427e' == (0, 'd41d8cd98…')` | `(0, d41d8cd9…)`, `(1, …)`, `(2, …)` |
| `test_a_table_that_grows_under_the_probe_yields_a_self_consistent_pair` | `AssertionError: the probe printed a row count that belongs to a different snapshot than its digest` | each probe's `(rows, digest)` describes ONE snapshot, and the two probes differ |
| `test_the_probe_sends_no_separate_count_statement` | `AssertionError: the content proof still counts the rows in a second statement: ['SELECT count(*) FROM "system"."bars"']` | no `count(` in any statement the probe constructs |
| `test_the_documented_fold_counts_rows_and_buffers_a_batch` | `AssertionError: _digest_rows's docstring still claims it holds exactly one row at a time` | docstring + DevDoc say a batch of `PROBE_BATCH_SIZE` rows is buffered per fetch |
| `test_every_proof_table_digests_to_the_value_the_old_sql_returns` (unchanged oracle) | — | **still passes** with the DB, `bars` included |
| `test_proof_only_with_rollback_is_refused_before_any_connection[False,True]` (new, review's untested case; also covers `--proof-only --allow-prod`) | — (passes; coverage, not a fix) | refused before any connection is opened |
| `test_an_exception_inside_the_probe_leaves_the_connection_rolled_back` (new, review's untested case) | — (passes; coverage, not a fix) | `rollback()` once, `close()` once |

| run | command | result |
|---|---|---|
| RED (before the fix) | `uv run pytest -q tests/cobalt/test_migrate_proof.py --tb=line -p no:randomly` | `19 failed, 5 passed, 6 skipped in 0.06s` |
| GREEN offline | `uv run pytest -q tests/cobalt/test_migrate_proof.py --tb=short -p no:randomly` | `24 passed, 6 skipped in 0.03s` |
| GREEN with `cobalt_dev` | `COBALT_ENV=dev uv run pytest -q tests/cobalt/test_migrate_proof.py --tb=short -p no:randomly` | `30 passed in 28.38s` |

**Deviation, disclosed.** The DB-backed run above was taken in part A, not part C: the byte-compatibility oracle is the one test that can prove the fold still produces the old digests, and proving it before the re-land costs one dev-DB read and avoids re-landing 55 commits onto a harness that cannot pass its own gate. Allowlisted commands only (`cp` the `.env`, `COBALT_ENV=dev uv run pytest *`, `rm`, `ls -la`), `cobalt_dev` only, nothing written; the `.env` was removed immediately after (`ls -la` → `No such file or directory`).

Docs: `docs/40 - DevDocs/cobalt/db_migrations/cli.md` — "How the digest is computed now" rewritten (one statement; the batch is what is buffered; F1 named), "Timing is a deliverable" updated with the measured production figures (8,591,339 rows in 46.73 s, probe 46.9 s, pair ≈94 s) and the note that both figures predate this fix.

CONTINUE: part B
