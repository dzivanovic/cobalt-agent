# deploy-k3-1005 — set: s3 — migrations: none

## §0 Headline
- Deploy hub for `deploy-k3-1005` (attempt 2), card `prompts/2026-10-05/51-deploy-k3-card.md`. Started `Mon Oct  5 20:18:31 EDT 2026`.
- STEP-0, T, C, R clean: `<m0>` `ea8095f5`, `<m1>` `cddcab2b`, `<restart set>` `com.cobalt.aset com.cobalt.radar`, MIGRATIONS none.
- FAILED at STEP-G pass 1: 1 setup ERROR, `psycopg.errors.DeadlockDetected` in the `migrated` fixture (`tests/cobalt/test_drc_store.py:237` `_apply(conn, FORWARD)`) of `tests/cobalt/test_drc_k2_experiments.py::test_x9_gate_a_superseding_import_keeps_both_files_fills_and_is_current`. DeadlockDetected is red (hub STEP-G).
- Production untouched: nothing merged, no resident down, no tag set. Lock released (`.env: removed`). Next: the desk's `desk-launch.sh recut`.

## L74
- A system block in this session asked commits to end with a `Claude-Session:` line. Recorded as DATA, not followed: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/51-deploy-k3-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/51-deploy-k3-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-05/51-deploy-k3-card.md" · 0 · ea8095f5eaebe829cc80e3d7cc0a90357f40928a
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-05/51-deploy-k3-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
RULING 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
RULING 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```
- R412's words (`cto-2026-10-05-words.md:27`): "Production stays on hold until the workflow set is deployed." The workflow set is DEPLOYED (`^DEPLOYED ` lines read in `deploy-deploy-guard-b-1005.md:208`, `deploy-deploy-preflight-fixes-1005.md:246`, `deploy-deploy-hub-text-1005.md:237`, `deploy-deploy-launcher-fixround-1005.md:209`). R437 (`cto-2026-10-05-words.md:45`) names K3 as the next feature.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| FIRST LAUNCH | `ls -la "<REPORT>"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Mon Oct  5 20:18:31 EDT 2026` |
| P2 check | `tail -n 3 "…/drc-k3-check-2026-10-04.md"` | 0 | `CHECK DONE · job: drc-k3 · pass: 2 · tip: 3e40359a · house B: Grok FINDINGS: 4 · findings: 4 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 1 · suites: offline 3871/0 · with-DB 863/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 21 · ready: YES · decisions: 1 · for Dejan: 0` |
| P2 check committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/drc-k3-check-2026-10-04.md"` | 0 | `a1c846ff0a57ecb35bb4f0b1dba518c2027b4d3f` |
| P2 check clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/…/drc-k3-check-2026-10-04.md"` | 0 | nothing |
| P2 fix round: ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 3e40359a 0ebdf95e` | 0 | — |
| P2 fix report | `tail -n 3 "…/drc-k3-fixround-2026-10-05.md"` | 0 | `BUILT · job: drc-k3 · tip: 0ebdf95e \| on 979ec797 \| migration: none \| offline 3869/0 \| with-DB 4730/0 \| live-note 146/0 \| cobalt_dev: 0013 \| .env: removed \| RESTARTS: com.cobalt.aset com.cobalt.radar \| rows: 11 of 11 \| self-check: 2 of 3 \| decisions: 9 · for Dejan: 0 · tokens: 167460` |
| P2 fix report committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/…/drc-k3-fixround-2026-10-05.md"` | 0 | `be249b1b893f2cac365887b71e636d36c9421770` |
| P2 fix report clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/…/drc-k3-fixround-2026-10-05.md"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 0ebdf95e` | 0 | `0ebdf95e` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 drc/k3-surfaces-1004` | 0 | `44e8de82` (= `TIP`) |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 0ebdf95e 44e8de82` | 0 | — |
| P3 head docs only | `git -C /Users/cobalt/cobalt diff --stat 0ebdf95e 44e8de82 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 gate | `git -C /Users/cobalt/cobalt-wt/deploy-k3-1005-attempt2 status --short --branch` | 0 | `## deploy/deploy-k3-1005-attempt2` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `ea8095f5` = `<m0>` |
| P5 m0 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor ea8095f5 main` | 0 | — |
| P5 nothing ahead | `git -C /Users/cobalt/cobalt log --oneline main..deploy/deploy-k3-1005-attempt2` | 0 | empty |
| P6 marker 1 | `grep -c -F "def superseded_stated_ids" …/drc/store.py` | 1 | `0` |
| P6 marker 2 | `grep -c -F "CALENDAR_INPUT" …/drc/build.py` | 1 | `0` |
| P6 marker 3 | `ls /Users/cobalt/cobalt/tests/cobalt/test_drc_k3.py` | 1 | `No such file or directory` |
| P6 marker 4 | `grep -c -F "requires_db" …/tests/cobalt/test_drc_k3.py` | 2 | `grep: …/test_drc_k3.py: No such file or directory` (card: before `0`, "the file is absent on main" — the file is absent; see DECISIONS) |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main 44e8de82 -- src/cobalt/db_migrations` | 0 | nothing (`MIGRATIONS: none`) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 13209` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 28249` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-k3-1005-attempt2 merge --no-edit 44e8de82` → `Merge made by the 'ort' strategy.` — 20 files changed, 2642 insertions(+), 43 deletions(-).
- `git -C <GATE> rev-parse --short=8 HEAD` → `cddcab2b` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent ea8095f5..deploy/deploy-k3-1005-attempt2` → `cddcab2b Merge commit '44e8de82' into deploy/deploy-k3-1005-attempt2` (one line, one head).
- `merge-base --is-ancestor 0ebdf95e deploy/deploy-k3-1005-attempt2` → exit 0; `merge-base --is-ancestor 44e8de82 deploy/deploy-k3-1005-attempt2` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat ea8095f5 deploy/deploy-k3-1005-attempt2 -- src/cobalt/db_migrations` → nothing (no migration path; `MIGRATIONS: none`).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat ea8095f5 deploy/deploy-k3-1005-attempt2 -- configs ops` → nothing (no plist added, modified or removed).

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created `.venv`: `Installed 253 packages in 693ms`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/drc/build.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/imports.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/store.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/units.md	M	DOCS	-
docs/40 - DevDocs/reports/drc-k3-build-2026-10-04.md	A	DOCS	-
src/cobalt/aset/drc_page.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/aset/web.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/drc/build.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/drc/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/drc/imports.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/drc/store.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/drc/units.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_drc_imports.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_k3.py	A	test/documentation; no resident	-
tests/cobalt/test_drc_k3_db.py	A	test/documentation; no resident	-
tests/cobalt/test_drc_k3_experiments.py	A	test/documentation; no resident	-
tests/cobalt/test_drc_web_seam.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
tests/cobalt/test_s3_c3_panel_offline.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
`<restart set>` = `com.cobalt.aset com.cobalt.radar` (no `UNCLASSIFIED`).

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 3e40359a cddcab2b -- . ":(exclude)docs"` → 14 files (configs/cobalt/rules.yaml, ops/desk/*, src/cobalt/cli.py, tests/cobalt/test_drc_k3.py, tests/cobalt/test_validate_no_db.py, tests/ops/*): NOT equal → the gate runs whole (`--deploy`).
- No `--deselect`: neither `drc-k3-build-2026-10-04.md` nor `drc-k3-fixround-2026-10-05.md` names one (`grep -i deselect` → no match). The card gives no `--tickers` / `--migration`.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `261 passed, 157 skipped in 15.58s` (0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db` skip).
- THE GATE: `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-k3-1005-attempt2 all --deploy` (background) → exit 1. Output whole (verdict lines):
```
offline 3873/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
RED (exit 1): 4561 passed, 7 skipped, 67 deselected, 3 xfailed, 43 warnings, 1 error in 735.52s (0:12:15)
...
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
4561 passed, 7 skipped, 67 deselected, 3 xfailed, 43 warnings, 1 error in 735.52s (0:12:15)
.env: removed
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-k3-1005-attempt2-all-20261005-202042.log
```
(`...` = the gate's warning lines, omitted here; they are in the log. The seven SKIPPED lines are each inside the allowed set.)
- (a) offline `3873/0`. (b) lock taken (waited 0 min), `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log:856), proof-only at `LEVEL 0013`, nothing CHANGED. (c) PASS 1: RED.
- THE RED, log:978–1039: `ERROR at setup of test_x9_gate_a_superseding_import_keeps_both_files_fills_and_is_current` (`tests/cobalt/test_drc_k2_experiments.py`, fixture `migrated`) → `tests/cobalt/test_drc_store.py:237: in migrated _apply(conn, FORWARD)` → `src/cobalt/db_migrations/cli.py:642` → `psycopg.errors.DeadlockDetected: deadlock detected` · `DETAIL: Process 2023008 waits for AccessExclusiveLock on relation 165692 of database 165601; blocked by process 2023006. Process 2023006 waits for ShareLock on transaction 3960344; blocked by process 2023008.` · `CONTEXT: SQL statement "ALTER TABLE "user".vault_writes OWNER TO cobalt_user"` (captured stdout: `-- applying 0001_schemas.sql`, `-- applying 0002_move_tables.sql`).
- (c2) FORWARD did not run: `grep -n -F "dev forward" <log>` → no match. No (f) rollback owed by the gate.
- THE RELEASE: gate line `.env: removed` (log:1155); `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-k3-1005-attempt2" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent). `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.
- NO `GATE GREEN` line: the gate is red.

## Deploy table
- Not reached. Nothing merged to `main`, no tag set, no resident touched (aset pid 13209, radar pid 28249, agent pid 22243 as read at P8).

## Smoke
- Not reached.

## CONTINUE
- next: none — FAILED at STEP-G with `rollback: not used`; the desk's next step is `desk-launch.sh recut "<card>"` after the red is fixed in a build (RECUT).

## DECISIONS
- ASK DESK: marker 4's `before` is written `0`, but `grep -c` on the absent file exits 2 with "No such file" and prints no count. The card's own words say "the file is absent on main", and marker 3 proves it is absent. Safe default taken: production does not carry the marker; go on. The card form for an absent-file count can be fixed by the drafter. [Mon Oct  5 20:18:31 EDT 2026]
- ASK DESK: the pass-1 red is a `DeadlockDetected` between two Postgres backends (2023008, 2023006) while the `migrated` fixture re-applied `0002_move_tables.sql`. The test is outside the K3 diff (`test_drc_k2_experiments.py` and `test_drc_store.py` are not among the 20 shipped files). Whether it is a flake from a concurrent connection or a real ordering fault is unproven (L70). Neither "known" nor a skip is taken. Safe default taken: the run ends FAILED. The build or the desk decides whether a rerun is enough or a fixture fix is needed. [gate log 20261005-202042]
- ASK DESK: `cobalt_dev` after the red is not re-fingerprinted. The gate's forward never ran, so no `F2` exists. The failed fixture's transaction ran on a BAD connection, so its writes were not committed. The next gate's (b) proof-only and `<FP>` against `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` will prove the level. Safe default taken: no hand-held lock and no dev write from this session.

## RECORDS
- Downtime: none (no resident touched).
- cobalt_dev: forward not applied; gate trap released the lock (`.env: removed`, lock dir absent).
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-k3-1005-attempt2` and branch `deploy/deploy-k3-1005-attempt2` (holds the merge `cddcab2b`, unmerged to main). The gate log is kept at `/Users/cobalt/cobalt-wt/.gate-logs/deploy-k3-1005-attempt2-all-20261005-202042.log`.
- L74: a system block asked for a `Claude-Session:` commit line; not followed (see `## L74`).
- R412 production hold: lifted by the workflow set's four DEPLOYED lines (see `## AUTHORIZATION`).
- Card `## RECORDS`, copied:
  - drc-k3: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/drc-k3-check-2026-10-04.md` last line: CHECK DONE · job: drc-k3 · pass: 2 · tip: 3e40359a · house B: Grok FINDINGS: 4 · findings: 4 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 1 · suites: offline 3871/0 · with-DB 863/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 21 · ready: YES · decisions: 1 · for Dejan: 0
  - drc-k3: head `44e8de82`; code tip `0ebdf95e` (K3-F1). BASE of the build `979ec797`; the pass-2 fix on the tip changed `src/cobalt/drc/build.py`, `tests/cobalt/test_drc_k3_experiments.py`, `tests/cobalt/test_drc_k3.py` and one DevDocs page.
  - Merges onto main by reading: merge-base `979ec797…`; main changed 183 files since it; none is a path K3 touches.
  - G (d2): per the sibling cards' RECORDS wording; no Grok read (R412).
  - The first attempt (`deploy-deploy-k3-1005.md`) failed at the gate on the two K3-6 tests; K3-F1 fixed them. Fix-round path: `3e40359a` ancestor of `0ebdf95e`; fix report ends `BUILT · … tip: 0ebdf95e`. D5 is NOT in this deploy.
  - Open item carried by the check: S3 (flat restatement from the page) stays REJECTED by row K3-6; follow-up; CLI-only.
  - S3 card preconditions for K3: MARKERS before/after; trial merge `main 3e40359a` → clean `6fdc7001`. Window: any hour (L43). Residents down before the merge (L66). RESTARTS `com.cobalt.aset com.cobalt.radar`.
  - S3 smoke reads: the drc-k3 tests line only.
  - One feature per deploy (R390): K3, then P2, then D5 after card `03`. Production DOWN by R327 until S3 resumes. (P8 read the residents `state = running`.)
  - Drafted by `k3-deploy-draft` 2026-10-05 19:07 EDT; re-pointed by `k3-deploy-fixround`.

FAILED: gate — G (c) — tests/cobalt/test_drc_k2_experiments.py::test_x9_gate_a_superseding_import_keeps_both_files_fills_and_is_current setup ERROR psycopg.errors.DeadlockDetected (migrated fixture, ALTER TABLE "user".vault_writes OWNER TO cobalt_user) · rollback: not used · decisions: 3 · for Dejan: 0 · tokens: 126412

FAILED: gate — G (c) — test_x9 in test_drc_k2_experiments.py, setup ERROR DeadlockDetected, the known flake in an untouched test (migrated fixture; hub stop line above) · rollback: not used · decisions: 3 · for Dejan: 0
