# F5 card 731 row FIX2 — preflight (2026-10-20)

Read-only. Card `prompts/2026-10-18/731-f5-card.md` at HEAD `ddfbd05f` (= main). Branch `ops/f5-checkpoints-fr1` tip `3c96ad2e`.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git rev-parse HEAD main ops/f5-checkpoints-fr1` | `ddfbd05f…` twice; branch `3c96ad2ec56e…` (tip `3c96ad2e`, as FIX2 says) | OK |
| 2 | `git rev-parse bd5dd70a e29cad00`; `git merge-base main ops/f5-checkpoints-fr1` | both resolve; merge-base `bd5dd70a` = header BASE. Header TIP `e29cad00` is the old build tip, now `3c96ad2e` (FIX2 names the live tip) | OK (NOTE 1) |
| 3 | `ls src/cobalt/db_migrations` at HEAD | highest `0028_genesis_vectors{,.rollback}.sql`; `0026_genesis_chunk` below it; no `0027`, no `0029`. Next free = `0029`, as FIX2 says; FIX2 (0) orders a re-proof by `ls` and the `FORWARD` end, never an assumption | OK |
| 4 | `git show HEAD:src/cobalt/db_migrations/__init__.py` | `FORWARD` ends `0026_genesis_chunk.sql`, `0028_genesis_vectors.sql`; `REVERSE` starts `0028…rollback`, `0026…rollback` (matches RECORDS) | OK |
| 5 | `git grep -n "0027" ops/f5-checkpoints-fr1 -- src tests configs ops "docs/40 - DevDocs/cobalt"` | 4 doc hits, 2 SQL, 8 `__init__.py`/`placement.py` hits, 20 test files; every hit is on a line FIX2 names (src `:1,:1,115,118,127,128,197,204`, `placement.py:127`; the 20 test files with the same lines; docs `__init__.md:293,296`, `placement.md:95`, `checkpoints.md:23`); configs and ops: no hit. The 469 gap note is `__init__.py:127-128` | OK |
| 6 | file list of the grep vs FIX2 "the 20 test files of (3)" | archiver, assumed_store, checkpoints_db, checkpoints_offline, dml_roles, drc_d2, drc_d3, drc_k1, drc_store, f15_p1, legs, p4, radar_handicap, radar_migration, radar_price_floor, radar_score, seam_drc_s3, stale_score, tenancy, voice_store = 20 | OK |
| 7 | `git grep -n "0028" ops/f5-checkpoints-fr1 -- tests` (pins that hold 0028 last) | `test_assumed_store.py:280-281`, `test_f15_p1_records_offline.py:31-32`, `test_archiver_migrations.py:102,110,146,166,215`, `test_seam_drc_s3_registry.py:26,28`, `test_checkpoints_offline.py:599,601` and the rollback-name lists: all named by FIX2 | OK |
| 8 | `__init__.py` branch tip: `FORWARD` `:196-198`, `REVERSE` `:203-205`, docstring pairs `:115-122` | FIX2 puts `<NNNN>` after `0028` (last) in `FORWARD` and before `0028…rollback` (first) in `REVERSE`; docstring pair after 469's `:119-124`; gap note rewritten. Matches STEP-T's demand | OK |
| 9 | `placement.py` branch tip | `"market_checkpoints": Side.SYSTEM` is the last `CREATED_TABLES` entry after `genesis_chunk`; only the comment `:127` names 0027; FIX2 moves the comment, keeps the entry and order | OK |
| 10 | index arithmetic for the old pins | with `0026,0028,<NNNN>` the tail, 0026 stays `[-3]/[2]`, 0025 `[-4]/[3]`, older ones keep their index; 0028 moves to `[-2]/[1]`; slices `[-18:]`/`[:18]` keep width. FIX2's drafter claim holds | OK |
| 11 | `test_archiver_migrations.py:213` | now `range(13, 29)`; FIX2 gives `[*range(1, 12), *range(13, 27), 28, <NNNN>]` (0027 stays a gap); `:215` tail `numbers[-1] == 28` is named | OK |
| 12 | FIX2 shape: one row, launch, band, builder, merge | one `FIX2` row; band HIGH (header `BAND: HIGH`); "original Opus builder", existing worktree `cobalt-wt/f5-checkpoints-fr1` (exists) and branch; "NO merge of main into the branch"; `git log --merges bd5dd70a..ops/f5-checkpoints-fr1` empty | OK (NOTE 2) |
| 13 | `git diff HEAD~1 -- <card>` (FIX1 untouched) | the diff has additions only: no removed line. FIX1 text unchanged | OK |
| 14 | `git grep -c "«FILL" HEAD -- <card>` | no match | OK |
| 15 | `## CHECK ASKS` | `:74` carries "after FIX2 (renumber) the check is scoped to the renumber: the file moves, FORWARD/REVERSE order, the pins, the old number gone from src tests configs ops, with the suites; no outside-house re-read" | OK |
| 16 | FIX2 smoke reads, hub launch line `DEPLOY-HUB.md:11` allow list | FIX2 names `## DEPLOY PROOF` f5-offline (`uv run pytest *`, admitted) and readers lines. `uv run cobalt jobs readers configs/cobalt/prefill.yaml` is not a string on the hub line (it admits `jobs restarts *`, `validate`, `heartbeat show*`, `smoke *`, `grep *`, `uv run pytest *`); the reads are run by `deploy-smoke.sh` (`sh /Users/cobalt/cobalt/ops/desk/*` is admitted). No `--no-db` spelling in FIX2 or `## DEPLOY PROOF` | OK (NOTE 3) |
| 17 | `git diff HEAD --stat -- <card>` | empty; the card is committed (status shows it clean) | OK |
| 18 | what blocks the build of FIX2 | nothing found: number free, branch and worktree present, no merge commit | OK (NOTE 2) |

## ISSUES
- NOTE 1: header `TIP: e29cad00` is the pre-fix tip; the branch is at `3c96ad2e`. FIX2 names the right tip; the desk may refresh the header.
- NOTE 2: the card line "launched `desk-launch.sh build 731 FIX2`" is shorthand: `desk-launch.sh:1240-1285` takes an absolute card path (`…/prompts/2026-10-18/731-f5-card.md`) and `FIX2` as the optional resume step, and refuses `731`. The desk types the full path.
- NOTE 3: the `jobs readers` smoke read is not a literal string on the hub line; the hub runs `## SMOKE READS` through `deploy-smoke.sh` (`:292`), which I did not run. This predates FIX2 (the failed deploy ended at STEP-T before smoke); the deploy card's recut should confirm it.

PREFLIGHT DONE · card: f5-checkpoints-fr1 FIX2 · checks: 18 · fails: 0 · ready: YES
