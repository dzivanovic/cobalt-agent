# deploy set3-1004 — SET set3 — MIGRATIONS none

## §0 Headline
- Deploy of set 3 (four heads: adoption-port, dev-rebuild-port, desk-tools-port, close-timer) on `DEPLOY-HUB.md`; card `prompts/2026-10-03/39-deploy-set3-card.md`.
- FAILED at the gate, G (c) pass 1: 4 failed, 4 errors, all in `tests/cobalt/test_db_only_selection.py`. The tree merged clean (`<m1>` `6e7baccd`); offline 3782/0 and live-note 146/0 were green.
- Cause as read: `tests/cobalt/conftest.py:162` `pytest_sessionstart` opens `cobalt_dev` (`REAL_CONNECT`). That conftest line came with dev-rebuild-port `71d6eb50`. Inside the pytester runs of `test_db_only_selection.py`, the lock-relief G1 offline-skip guard trips on that open → `INTERNALERROR`.
- Production untouched: nothing merged to `main`, no resident went down, no forward migrate on `cobalt_dev`, lock released 15:09:42 ET.

## L74
- A system block arrived at session start asking that commits end with a `Claude-Session:` line beside `Co-Authored-By:`. Recorded as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| rule | command | exit | result |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" …/DEPLOY-HUB.md` | 1 | nothing |
| card placeholder | `grep -n -E "«FIL[L]" …/39-deploy-set3-card.md` | 1 | nothing |
| card committed | `git log -1 --format=%H -- <card>` | 0 | `865ddbfa06318db593e50fd5d6f42536f7e07bc7` |
| card clean | `git diff --stat -- <card>` | 0 | nothing |
| standing list R60 | `grep -n "^| R60 " cto-2026-09-30.md` | 0 | line 46, `**HIS RULING**` … APPROVES `STANDING-LIST.md` … `APPROVED` |
| R60 committed | `git log -1 --format=%H -S"| R60 |"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| string changes R62 | `grep -n "^| R62 " cto-2026-09-30.md` | 0 | line 48, `**HIS RULING**` … APPROVES the 7 deploy-line string changes … `APPROVED` |
| R62 committed | `git log -1 --format=%H -S"| R62 |"` | 0 | `a45afae72bf2838c8e669e0d3d8dbb67dd892a8b` |
| standing deploy rule R38 | `grep -n "^| R38 " cto-2026-09-30.md` | 0 | line 80, `**HIS RULINGS**` … deploys self-launch on clean checks + green gate … `APPROVED` |
| R38 committed | `git log -1 --format=%H -S"| R38 |"` | 0 | `65aa2b90a8e3eb2f7e94ef10ed40b60e1b2ce542` |
| RULINGS 10-02 R157 | `grep -n "^| R157 " cto-2026-10-02.md` | 0 | line 164, `HIS RULING (B)` … `HIS RULING · APPROVED` |
| R157 committed | `git log -1 --format=%H -S"| R157 |"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| RULINGS 10-03 R216 | `grep -n "^| R216 " cto-2026-10-03.md` | 0 | line 222, `HIS RULING: deploy set 3 whenever the desk is ready, Sunday, no window to wait for` … `HIS RULING · APPROVED` |
| R216 committed | `git log -1 --format=%H -S"| R216 |"` | 0 | `58094781af1a5b2397dda1827098b38b9d7fbb62` |
| first launch | `ls -la <REPORT>` | 1 | No such file or directory |

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P1 | `date` | 0 | `Sun Oct  4 14:42:56 EDT 2026` — lawful under (iii) a non-trading day (Sunday); R216 also names this set's deploy with no window |
| P2 #1 | `tail -n 3 adoption-port-check-2026-10-03-r3.md` | 0 | `CHECK DONE · job: adoption-port · pass: 1 · tip: 685b88d6 · … · held unfixed: 0 · open: 0 · … · ready: YES · decisions: 0 · for Dejan: 0`; log `d41326ab…`; diff clean |
| P2 #2 | `tail -n 3 dev-rebuild-port-check-2026-10-03.md` | 0 | `CHECK DONE · job: dev-rebuild-port · pass: 1 · tip: f5689418 · … · held: 1 · fixed: 0 · held unfixed: 0 · open: 0 · … · ready: YES · decisions: 1 · for Dejan: 0`; log `d41326ab…`; diff clean |
| P2 #3 | `tail -n 3 desk-tools-port-check-2026-10-03.md` | 0 | `CHECK DONE · job: desk-tools-port · pass: 1 · tip: 5c1d629f · … · held unfixed: 0 · open: 0 · … · ready: YES · decisions: 0 · for Dejan: 0`; log `d41326ab…`; diff clean |
| P2 #4 | `tail -n 3 close-timer-check-2026-10-03.md` | 0 | `CHECK DONE · job: close-timer · pass: 1 · tip: 47a689a1 · … · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · … · ready: YES · decisions: 0 · for Dejan: 0`; log `903bf19a…`; diff clean |
| P3 #1 | rev-parse `685b88d6` / `ops/adoption-port-1003`; is-ancestor; diff excl docs | 0 / 0 / 0 / 0 | `685b88d6` · `15ba4b75` · ancestor · nothing |
| P3 #2 | rev-parse `f5689418` / `ops/dev-rebuild-port-1003`; is-ancestor; diff excl docs | 0 / 0 / 0 / 0 | `f5689418` · `53fed116` · ancestor · nothing |
| P3 #3 | rev-parse `5c1d629f` / `ops/desk-tools-port-1003`; is-ancestor; diff excl docs | 0 / 0 / 0 / 0 | `5c1d629f` · `525b5ae1` · ancestor · nothing |
| P3 #4 | rev-parse `47a689a1` / `ops/close-timer-1003`; is-ancestor; diff excl docs | 0 / 0 / 0 / 0 | `47a689a1` · `47a689a1` · ancestor · nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found: /Users/cobalt/cobalt-wt/*/.env` — no session holds the lock |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/set3-1004` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `845c77ff` = `<m0>` |
| P5 | `merge-base --is-ancestor 845c77ff main` | 0 | ancestor |
| P5 | `git log --oneline main..deploy/set3-1004` | 0 | empty |
| P6 | `grep -c -F "window (v) does not hold" …/DEPLOY-HUB.md` | 1 | `0` (before `0`) |
| P6 | `ls …/db_migrations/dev_rebuild.py` | 1 | No such file or directory (before) |
| P6 | `grep -c -F "claude-fable-5-1" …/ops/desk/desk-launch.sh` | 1 | `0` (before `0`) |
| P6 | `ls …/ops/desk/close-timer.sh` | 1 | No such file or directory (before) |
| P7 #1 | `diff --stat main 15ba4b75 -- src/cobalt/db_migrations` | 0 | `cli.py | 115` — code, no `.sql`, no `__init__.py` |
| P7 #2 | `diff --stat main 53fed116 -- src/cobalt/db_migrations` | 0 | `cli.py | 350`, `dev_rebuild.py | 879` — code, no `.sql`, no `__init__.py` |
| P7 #3 | `diff --stat main 525b5ae1 -- src/cobalt/db_migrations` | 0 | `cli.py | 115` — code, no `.sql`, no `__init__.py` |
| P7 #4 | `diff --stat main 47a689a1 -- src/cobalt/db_migrations` | 0 | nothing |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, pid 13209 |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, pid 18818 |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
| head | command | result |
|---|---|---|
| 15ba4b75 | `git -C <GATE> merge --no-edit 15ba4b75` | `Merge made by the 'ort' strategy.` (57 files) |
| 53fed116 | `git -C <GATE> merge --no-edit 53fed116` | `Merge made by the 'ort' strategy.` (11 files) |
| 525b5ae1 | `git -C <GATE> merge --no-edit 525b5ae1` | `Merge made by the 'ort' strategy.` (17 files) |
| 47a689a1 | `git -C <GATE> merge --no-edit 47a689a1` | `Merge made by the 'ort' strategy.` (4 files) |
- `<m1>` = `6e7baccd` (`git -C <GATE> rev-parse --short=8 HEAD`).
- `log --oneline --merges --first-parent 845c77ff..deploy/set3-1004`: `6e7baccd Merge commit '47a689a1'` · `8af240df Merge commit '525b5ae1'` · `e33a5d6e Merge commit '53fed116'` · `54aff891 Merge commit '15ba4b75'` — one per head.
- `merge-base --is-ancestor <x> deploy/set3-1004` exit 0 for each of 685b88d6, 15ba4b75, f5689418, 53fed116, 5c1d629f, 525b5ae1, 47a689a1.
- `diff --stat 845c77ff deploy/set3-1004 -- src/cobalt/db_migrations`: `cli.py | 350`, `dev_rebuild.py | 879` — code; no `.sql`, no `__init__.py`: no migration path, matching `MIGRATIONS: none`.
- STEP-C `diff --stat 845c77ff deploy/set3-1004 -- configs ops`: 30 files, all under `ops/desk/` (authorize.sh, card-fill.sh, close-timer.sh, com.cobalt.close-timer.plist, deploy-card.sh, desk-commit.sh, desk-context.sh, desk-done.sh, desk-handover.sh, desk-launch.sh, desk-list.sh, desk-row.sh, desk-wake.sh, desk-watch.sh, gate-clean.sh, gate-lists.md, gate.sh, house-probe.sh, idle-wake.py, install-fixed.sh, job-clean.sh, order-open.sh, preflight.sh, release-devdb-lock.sh, stage-copy.sh, stage-set.sh, stop-guard.py, take-devdb-lock.sh, wait-desk-idle.sh, wait-stop-line.sh); `30 files changed, 939 insertions(+), 132 deletions(-)`; nothing under `configs`.
- STEP-C plist: `ops/desk/com.cobalt.close-timer.plist` ADDED. Label (`grep -n -A1 -F "<key>Label</key>"`): line 6 `<string>com.cobalt.close-timer</string>`. `grep -n -F "close-timer" <GATE>/configs/cobalt/jobs.yaml` → nothing (exit 1): not a registry label; path is not `ops/com.cobalt.close-timer.plist`. Passes the ops/desk/ exception. No plist removed.

## RESTARTS
- `cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` exit 0. uv lines: `Creating virtual environment at: .venv` · `Built cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-1004-1` · `Installed 253 packages in 779ms`.
- Table (rows grouped; every row read): 22 `docs/…` rows `DOCS -`; 30 `ops/desk/…` rows `operator script; no Cobalt reader -`; `src/cobalt/db_migrations/cli.py M static import reach com.cobalt.radar`; `src/cobalt/db_migrations/dev_rebuild.py A static import reach com.cobalt.radar`; 26 `tests/…` rows `test/documentation; no resident -`. No `UNCLASSIFIED` row.
- `RESTARTS: com.cobalt.radar` → `<restart set>` = `com.cobalt.radar`.

## L68 GATE
- No build of this set added a pass-1 `--deselect` (adoption-port build: "no added deselect"; dev-rebuild-port: "`test_dev_rebuild_db.py` runs in pass 1 at `0013`, no deselect, no pass-2 id"; close-timer: "no `--deselect` added"; desk-tools-port: ops tests only). Pass 1 and pass 2 run as the hub has them.
- (a0) `ls -la <GATE>/.env` No such file · the hub's 17-file early read → `261 passed, 157 skipped in 15.93s`; 0 failed (skips are with-DB `Postgres env settings not available` / `requires_db`).
- (a) `ls -la <GATE>/.env` No such file · `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, exit 0) → `3782 passed, 755 skipped, 1 xfailed, 36 warnings in 606.91s (0:10:06)`; `grep -c -F "FAILED"` on its output → `0`. 0 failed, 0 errors. `<p>` = 3782. No uv sync line (the venv was built at STEP-R).
- (e) `ls -la <GATE>/.env` No such file · `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest … test_radar_evaluate.py test_replay_line.py test_catalyst.py test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 27.02s`; the one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — inside the allowed set; no skip names `COBALT_LIVE_VAULT_ROOT`. `<l>` = 146.
- (b) `sh /Users/cobalt/.claude/ops/take-devdb-lock.sh deploy-1004-1 90` (background, exit 0) → `lock taken: deploy-1004-1`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  4 14:56 /Users/cobalt/cobalt-wt/deploy-1004-1/.env` — ours alone.
- (d2) `COBALT_ENV=production uv run cobalt validate` → exit 0; `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobsG>`; `registry <-> ops/: 15 label(s), exact match.`; `registry <-> plists: schedules and COBALT_ENV agree on every job.`; `Placement (docs/PLACEMENT.md): tree clean.`
- `<FP>` → `<F0>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`.
- `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → 36 tables probed, `NOTHING WAS APPLIED`, no `CHANGED`; `code: 6e7baccd (clean)`; `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`; `TABLES 0011` — level `0013` (the highest table-creating migration at or below `0013` is `0011`: adoption-scripts build, its row "TABLES at 0013"). Also printed: `SLOTS WARN user.aset_sizings max_attnum 1358 of 1600 · dropped 1304 · live 54` (information, L70).
- (c) PASS 1 at `0013`: `ls -la <GATE>/.env` printed the file · the hub's pass-1 command byte for byte, no `--deselect` added (background, exit 1) → `4 failed, 4457 passed, 7 skipped, 67 deselected, 3 xfailed, 43 warnings, 4 errors in 713.38s (0:11:53)`. **RED.**
  - FAILED `tests/cobalt/test_db_only_selection.py::test_with_db_only_a_run_deselects_every_unmarked_item`: `E IndexError: list index out of range`.
  - FAILED `tests/cobalt/test_db_only_selection.py::test_without_db_only_a_run_keeps_every_item`: `E IndexError: list index out of range`.
  - FAILED `tests/cobalt/test_db_only_selection.py::test_a_reach_a_store_swallowed_still_fails_the_test_at_teardown`: `E AssertionError: assert [] == ['passed']`.
  - FAILED `tests/cobalt/test_db_only_selection.py::test_an_unmarked_open_through_real_connect_is_refused_before_any_connection`: `E AssertionError: assert [] == ['failed']`.
  - ERROR at teardown of each of the same four: `tests/cobalt/conftest.py:124: Failed` — `E Failed: with-DB test without an offline skip mark: tests/cobalt/test_db_only_selection.py::<test>`. Captured stdout, each: `INTERNALERROR> … tests/cobalt/conftest.py, line 162, in pytest_sessionstart` → `conn = REAL_CONNECT(env.DEV_DB_NAME, side=db.Side.SYSTEM)` → `src/cobalt/db.py:260 connect` → `conftest.py:331 guarded_psycopg_connect` → `_guarded_reach … # lock-relief G1, check X1` → `conftest.py:78 require_offline_skip` → `AssertionError: with-DB test without an offline skip mark: …`.
  - Every SKIPPED line is in the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_replay_line.py:266` (`COBALT_TEST_LIVE_DRC`), `test_s3_c4_experiments.py:95` (the live template read), `test_catalyst.py:365`, `test_predicate.py:262`.
  - `git log --oneline -3 deploy/set3-1004 -- tests/cobalt/conftest.py` → `71d6eb50 wip(dev-rebuild-port): E3 — …` (newest) · `18f03c41 fix(lock-relief): G1 guards every psycopg.connect …` · `377c83b2 feat(lock-relief): offline-skip guard, --db-only pass 1 …`. `test_db_only_selection.py` is on `main` from `377c83b2` / `08483019` (lock-relief).
- (c2) forward NOT run; (f) not owed (`dev forward` never APPLIED; `cobalt_dev` stays at `0013` as `<F0>` read it). Pass 2 not run.
- THE RELEASE: `sh /Users/cobalt/.claude/ops/release-devdb-lock.sh deploy-1004-1` → `lock released`; `date` `Sun Oct  4 15:09:42 EDT 2026`; `ls -la <GATE>/.env` → No such file. `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` listed. `git -C <GATE> status --short --branch` → `## deploy/set3-1004` (clean).
- NO `GATE GREEN` line: the gate is red on `6e7baccd`.

## Deploy table
- Not reached. `main` not moved by this run; no tag set (`pre-set3-1004`, `deploy-2026-10-04-1` not created); no snapshot; `migrations applied: none`; residents untouched (aset pid 13209, radar pid 18818, agent pid 22243 at P8). No rollback string: nothing merged.

## Smoke
- Not reached.

## CONTINUE
- ended at STEP-G (c), gate red. The continuation is a build (rule B), then a new deploy card; this run makes no fix.

## DECISIONS
1. The red is a shared seam between this set's dev-rebuild-port (`tests/cobalt/conftest.py` session-start connect, `71d6eb50`) and lock-relief's `test_db_only_selection.py` on `main` under `COBALT_ENV=dev` with `.env` present. Which build owns the fix (dev-rebuild-port marks or skips its session-start open under the G1 guard, or the pytester tests isolate the inner session) is the desk's. Safe default taken: nothing merged, set held whole. Not his.
2. The hub's pass 1 (no `--db-only`) ran `4457 passed, 67 deselected`. The set's builds report a pass 1 of `683 passed … 3846 deselected` (dev-rebuild-port) and `673 passed … 3801 deselected` (close-timer), and lock-relief added a `--db-only pass 1` (`377c83b2`). That pass 1 deselects the tests that went red here. So this gate and the builds' gates ran different selections. The desk decides whether `DEPLOY-HUB.md`'s pass-1 line should match before the next deploy (adoption-port carries a 50-line `DEPLOY-HUB.md` change in this set). Safe default: ran the hub's line byte for byte as `main` has it. Not his.

## RECORDS
- cobalt_dev: no forward run; level `0013` as read by `--proof-only` (`<F0>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`); `.env: removed (L76 lock released 15:09:42 ET)`.
- No downtime. No `RETIRE OWED` (no plist removed). Carried RED: not read (D1 not reached).
- Cleanup owed (L46): gate worktree `/Users/cobalt/cobalt-wt/deploy-1004-1` and branch `deploy/set3-1004` (now at `6e7baccd`, four merges above `845c77ff`); the set's branches stay for the fix.
- L74: one block asked for a `Claude-Session:` commit line; recorded under `## L74`, not followed.
- No `CONTINUE` message received; no command refused.
- Card `## RECORDS`, copied:
  - adoption-port: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/adoption-port-check-2026-10-03-r3.md` last line: CHECK DONE · job: adoption-port · pass: 1 · tip: 685b88d6 · house A: none (overruled 2026-10-02 R47) · findings: 8 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 16 · ready: YES · decisions: 0 · for Dejan: 0
  - adoption-port: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/adoption-port-1003` → `15ba4b75`; code tip `685b88d6`
  - dev-rebuild-port: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/dev-rebuild-port-check-2026-10-03.md` last line: CHECK DONE · job: dev-rebuild-port · pass: 1 · tip: f5689418 · house A: none (overruled 2026-10-02 R47) · findings: 9 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 8 · ready: YES · decisions: 1 · for Dejan: 0
  - dev-rebuild-port: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/dev-rebuild-port-1003` → `53fed116`; code tip `f5689418`
  - desk-tools-port: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-tools-port-check-2026-10-03.md` last line: CHECK DONE · job: desk-tools-port · pass: 1 · tip: 5c1d629f · house A: none (overruled 2026-10-02 R47) · findings: 9 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 22 · ready: YES · decisions: 0 · for Dejan: 0
  - desk-tools-port: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/desk-tools-port-1003` → `525b5ae1`; code tip `5c1d629f`
  - close-timer: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/close-timer-check-2026-10-03.md` last line: CHECK DONE · job: close-timer · pass: 1 · tip: 47a689a1 · house A: none (overruled 2026-10-02 R47) · findings: 4 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3737/0 · with-DB not run (DB: none) · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 12 · ready: YES · decisions: 0 · for Dejan: 0
  - close-timer: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/close-timer-1003` → `47a689a1`; code tip `47a689a1`
  - written by deploy-card.sh at 2026-10-04 14:40 ET (`date`); trial merge of the heads onto main in order: clean
  - MIGRATIONS none: the build stop lines say `migration: none`; `db_migrations/cli.py` and `dev_rebuild.py` are code, no `.sql`. MARKERS, SMOKE READS filled by the desk (R216); `10` cobalt-guard deploys after its check.

FAILED: gate — G (c) — tests/cobalt/test_db_only_selection.py (4 failed, 4 errors: conftest.py:162 session-start cobalt_dev open trips the G1 offline-skip guard) · rollback: not used · decisions: 2 · for Dejan: 0
