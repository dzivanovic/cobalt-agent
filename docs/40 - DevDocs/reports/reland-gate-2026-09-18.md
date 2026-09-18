# Re-land + gate — `reland-gate-0918`, 2026-09-18

## §0 Headline

- **STACK READY on `sprint-2/stack`** — 63 commits re-landed by cherry-pick onto main `968e010` (stack tip `d72ece4`), code byte-identical to what part A left, no conflict.
- **Review finding F1 folded** (`0e1f768`): the row count comes out of the fold, so `_probe` sends ONE statement and `bars` is read once. 19 red before, green after; **every dev digest is unchanged, 23/23**.
- **Gate GREEN with the database**: migrate 0001–0007, 23/23 `OK` and 0 `CHANGED`; integrated 1845 passed / 0 failed; real-vault 93; offline 1561.
- Authorization VERIFIED rule by rule against main; PREFLIGHT 5 probes, 0 denials; `.env` removed, tree clean, nothing merged, nothing pushed, no production command run.
- **ESCALATE: 3** (production's proof timing is stale-and-conservative; the BASELINE shape that avoids the append-only table; a noisy 63-commit changelog).

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

`<T_old>` = **`6694652`** (`3a6f2b3` fix + `6694652` report).

CONTINUE: part B

## B. Re-land on `sprint-2/stack`, off main

| step | command | result |
|---|---|---|
| B.1 | `git status --porcelain` | empty |
| B.1 | `git rev-list --count d672f2d..6694652` | **`<n>` = 63** (the 53 gated + the harness-fix chain + this run's 2) |
| B.1 | `git -C /Users/cobalt/cobalt rev-parse --short HEAD` | main = **`968e010`** |
| B.2 | `git switch -c sprint-2/stack main` | `Switched to a new branch 'sprint-2/stack'` — the branch did not exist |
| B.3 | `git cherry-pick d672f2d..6694652` | 63 commits replayed oldest-first, original messages, **no conflict, no empty-commit stop, no `--continue` needed**. New tip **`d72ece4`** |

The reverts on main restored each patch's exact pre-image, so the whole range applied clean — the third confirmation today of `UNATTENDED-LAUNCH.md` §6 (a merged-then-reverted branch re-lands by cherry-pick, never by rebase).

### B.4 PROOF — all three

| proof | command | result |
|---|---|---|
| count | `git rev-list --count main..HEAD` | **63** = `<n>` ✅ |
| byte-identity | `git diff --stat 6694652 HEAD -- src tests configs ops .gitignore` | **prints nothing** ✅ — the code is byte-identical to what part A left |
| offline | `ls -la …/.env` | `No such file or directory` ✅ |
| offline | `uv run pytest -q tests/cobalt tests/taxonomy --tb=short -p no:randomly` | **1561 passed, 0 failed**, 287 skipped, 1 xfailed, 39.95 s ✅ |

Whole-tree `git diff --stat 6694652 HEAD` shows 6 files, all under `docs/` — main's own desk commits since (`cto-2026-09-18.md`, `deploy-2026-09-18.md`, four `prompts/2026-09-18/*.md`), 262 insertions. Nothing under `src`, `tests`, `configs`, `ops` or `.gitignore` differs.

CONTINUE: part C

## C. The gate, with the database (on `sprint-2/stack`)

| # | command | result |
|---|---|---|
| C.1 | `cp /Users/cobalt/cobalt/.env …/s2-p2-cards/.env` | copied by name, never printed (L41 interim) |
| C.2 | `COBALT_ENV=dev uv run cobalt db migrate --proof-only` | 23 tables, **nothing applied** — see the quoted table below |
| C.3 | `COBALT_ENV=dev uv run cobalt db migrate` | 0001–0007 applied, **23/23 `OK`, 0 `CHANGED`** |
| C.4 | `COBALT_ENV=dev uv run cobalt settings load --from …/daymode-settings-0918 --dry-run` | `no differences — the database already holds these settings.` (7 keys, all `=`; keys only, L32) |
| C.5 | `COBALT_ENV=dev uv run cobalt validate` | exit 0 · `Step-downs: … trade_count_over_band=down(1) — 7 row(s), every computable signal ruled.` |
| C.6 | `COBALT_ENV=dev uv run pytest -q tests/cobalt tests/taxonomy --tb=short -p no:randomly` | **1845 passed, 0 failed**, 3 skipped, 1 xfailed, 153.85 s |
| C.7 | `COBALT_VAULT_PATH=/Users/cobalt/Vault/Think uv run pytest -q tests/cobalt -k "requires_vault or vault" -m "" -p no:randomly` | **93 passed, 0 failed**, 1472 deselected |
| C.8 | `COBALT_ENV=dev uv run cobalt settings load --card …/p2-dark-settings.yaml --dry-run` | `+ radar.cards_enabled` (db absent → file `false`) — **ONE add, zero deletions**; `DRY RUN — 1 card setting(s) would change. Nothing written.` |
| C.9 | `shasum -a 256` dark card | `945e42f86997559267b2e7c20783f2d023b9135ae4bb437ca25a4999ca7cd3ca` = R10 (2), unchanged |
| C.9 | `shasum -a 256` over-band pair | `daa7bb72…3d5ebb` (daymode.yaml), `8eca6945…b99d58` (aset.yaml) — **both exactly R4 (b)** |
| C.10 | `rm …/.env` then `ls -la …/.env` | `No such file or directory` |
| C.11 | `uv run cobalt jobs restarts main..HEAD` | 168 paths classified, **0 UNCLASSIFIED** · `RESTARTS: com.cobalt.aset com.cobalt.radar` |
| C.12 | `git status --porcelain` | empty |

### C.2 — `--proof-only`, quoted with its seconds

```
cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)

table                side    schema   rows         digest                             secs
------------------------------------------------------------------------------------------
aset_sizings         user    user     1            0824685c130da3c7cb7f0e76191a6819   0.01
bars                 system  system   1043443      2769919a57144c7bf8720110061dbf72   5.43
cobalt_redactions    system  system   120          a9594cce035f4c845768d97546b55796   0.00
cobalt_jobs          system  system   13           8d9b0861615861e343009f33118a4931   0.00
session_blocks       system  system   6            b650702dd6fd624548e05ca940662f08   0.00
vault_writes         user    user     184          4a965c69340f112d12e6ca21a8a0602c   0.01
(17 further tables, all as printed)
------------------------------------------------------------------------------------------
23 table(s) probed on cobalt_dev; … Proof cost: total 5.5 s — and a migration pays it TWICE (before and after), inside the outage.
NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
```

**The F1 fix is digest-neutral on real data at scale.** Every one of these values equals the 16:52 pre-fix dev probe (`prod-proof-only-2026-09-18.md`) byte for byte — `bars` 1,043,443 / `2769919a…`, `aset_sizings` `0824685c…`, `cobalt_jobs` `8d9b0861…`, `session_blocks` `b650702d…`, `vault_writes` `4a965c69…`, and `cobalt_redactions` still 120 / `a9594cce…`. 23/23, including the append-only table that drifted this afternoon. Counting inside the fold changed the statement count, not one byte of any digest.

`bars` probed in 5.43 s vs 5.35 s before the fix — dev's `bars` is 1/8th of production's and dominated by row transfer, so no speed-up is visible at this size; the second pass that was removed was `count(*)`, which is index-cheap on a small table. Production is where the saving is, and it has not been re-measured (ESCALATE 2).

### C.3 — the migration's own proof

`-- applying 0001_schemas.sql … 0007_radar_cards.sql`, then all 23 tables `OK`:

```
23 table(s) proven; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id; aset_sizings: 25 card column(s) added by 0007. content UNCHANGED on every table.
proof cost: BEFORE 5.4 s + AFTER 5.1 s = total 10.5 s; slowest table bars (5.4 s before).
```

**Zero `CHANGED`** — not even `cobalt_redactions`: nothing was redacted between BEFORE and AFTER in this run, so the append-only exception the prompt allows for was not needed and is not claimed.

**P4's tables are ABSENT.** No allowlisted command in this launch line lists arbitrary relations (`db query` is not in it), so the evidence is the suite: `tests/cobalt/test_tenancy.py::TestPlacement::test_every_table_is_on_its_ruled_side` fails on any relation missing from the placement map — it is the test that went red this morning naming `user.picks` and `system.movers_daily` — and `TestMigrationRoundTrip::test_twice_is_idempotent_and_the_rollback_round_trips` dies on their FKs onto `system.radar_membership`. Both passed in C.6. `cobalt_dev` is at 0007 and clean.

## ESCALATE

1. **Production's `--proof-only` figure is now stale, and conservative.** The 46.73 s / ≈94 s outage budget in `prod-proof-only-2026-09-18.md` was measured with the separate `count(*)` still in place — one of the two passes this run removed. On `bars`, where the count is a full heap/index scan of 8.6M rows, the saving is real but unmeasured; dev is too small to show it (5.43 s vs 5.35 s). A re-run of `COBALT_ENV=production uv run cobalt db migrate --allow-prod --proof-only` would replace a guess with a number before the deploy sizes its outage — but R12 approved that line to be run ONCE, so it needs Dejan's word again. Not a blocker: the standing budget over-states the cost, it does not under-state it.
2. **The append-only BASELINE problem (carried from `prod-proof-only-2026-09-18.md` ESCALATE 1) did not bite this run, and the reason is worth keeping.** This gate compared BEFORE against AFTER inside one command rather than against a pinned BASELINE, so `cobalt_redactions` had no window to drift. That is the durable shape of the fix the earlier hub asked for: compare within the run, not against a digest pinned an hour earlier. If a future prompt does pin a BASELINE, exclude that table by name.
3. **`sprint-2/stack` carries 63 commits, 30 of which are report commits from five runs** (re-ship, gate ×3, harness fix, prod proof, this one). They re-land because the range re-lands whole, and squashing them would have broken "original messages, no squash". Nothing is wrong with the tree; it is the deploy's changelog that is noisy. If the desk wants a clean one, that is a decision for the merge, not for this branch.

## Close

MEMORY: `cobalt_dev` at 0007, clean, with the over-band row, as of 2026-09-18 17:1x ET; the gated stack now lives on `sprint-2/stack` (off main `968e010`), not on `sprint-2/cards`; the migration harness's content proof is one statement per table since `0e1f768`.

STACK READY d72ece4 on sprint-2/stack (branch tip 2f69714, the report-only commit carrying this line; 2 report commits sit above the stack) | 63 commits re-landed by cherry-pick onto main 968e010, byte-identical to 6694652 | harness: streamed proof + --proof-only + F1 | offline: 1561 passed, 0 failed | integrated with DB: 1845 passed, 0 failed | real-vault: 93 passed | dark file sha256 945e42f8…ca7cd3ca unchanged | RESTARTS: com.cobalt.aset com.cobalt.radar | ESCALATE: 3
