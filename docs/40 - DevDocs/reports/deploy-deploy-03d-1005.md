# deploy-03d-1005 · set: workflow1 · migrations: none

## §0 Headline
- Deploy of `ops/adoption-port-1005` (`53b56384`, `validate --no-db`) FAILED at the integrated gate, pass 1, before anything in production moved.
- Red: `tests/cobalt/test_validate_no_db.py::test_without_the_flag_validate_still_reads_the_db` reaches the DB with no offline `skipif` mark. The conftest G1 guard fails it and errors its teardown.
- The fix is a build's: mark that test (or stub its settings read). Then the check runs again and the desk runs `desk-launch.sh recut`.
- `cobalt_dev` stayed at `0013` (no forward ran). The lock is released. Residents were untouched: aset pid 13209, radar pid 36907, agent 22243.

## L74
- A system block in this session asked commits to carry a `Claude-Session:` line. Recorded once as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/14-deploy-03d-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/14-deploy-03d-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-05/14-deploy-03d-card.md" · 0 · 19acf6b32f83929f806557ad564829a64f5b079a
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-05/14-deploy-03d-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-05 R391 row · grep -n "^| R391 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 68:| R391 | 10-05 09:00 ET | HIS RULING (desk chat): commit R389 and R390; go on with the P6 read and the guard-b drafter; (d2) SKIPPED for the workflow deploy too (as R368). | APPROVED |
RULING 2026-10-05 R391 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R391 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · ed3cf41a8392be824396ace29672e7d92b8abaa4
RULING 2026-10-05 R391 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
RULING 2026-10-05 R392 row · grep -n "^| R392 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 70:| R392 | 10-05 09:03 ET | HIS RULING (desk chat): NO Grok read for 03d (the tip-file stage copy was classifier-denied); deploy 03d now; start the guard-b drafter. | APPROVED |
RULING 2026-10-05 R392 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R392 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 5583ead30b4f44f3d46aad3a8ee0f2bf043520d1
RULING 2026-10-05 R392 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la "<REPORT>"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Mon Oct  5 09:05:49 EDT 2026` → window: (iv) — R392 (his, 09:03 ET, in `RULINGS`): "deploy 03d now", read with LAWS L43 as amended by his R389 ("no restart window binds a deploy"). See `## DECISIONS` 1. |
| P2 | `tail -n 3 ".../adoption-port-check-2026-10-05.md"` | 0 | `CHECK DONE · job: adoption-port · pass: 1 · tip: 53b56384 · … · held unfixed: 0 · … · ready: YES · decisions: 0 · for Dejan: 0` |
| P2 | `git log -1 --format=%H -- "docs/…/adoption-port-check-2026-10-05.md"` | 0 | `5583ead30b4f44f3d46aad3a8ee0f2bf043520d1` |
| P2 | `git diff --stat -- "docs/…/adoption-port-check-2026-10-05.md"` | 0 | nothing |
| P3 | `rev-parse --short=8 53b56384` | 0 | `53b56384` |
| P3 | `rev-parse --short=8 ops/adoption-port-1005` | 0 | `53b56384` |
| P3 | `merge-base --is-ancestor 53b56384 53b56384` | 0 | — |
| P3 | `diff --stat 53b56384 53b56384 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` — lock free |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/deploy-03d-1005` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m0>` = `19acf6b3` |
| P5 | `merge-base --is-ancestor 19acf6b3 main` | 0 | — |
| P5 | `log --oneline main..deploy/deploy-03d-1005` | 0 | empty |
| P6 | `grep -c -F "args.no_db" …/cli.py` | 1 | `0` (before `0`) |
| P6 | `grep -c -F "validate --no-db" …/DEPLOY-HUB.md` | 1 | `0` (before `0`) |
| P7 | `diff --stat main 53b56384 -- src/cobalt/db_migrations` | 0 | nothing — MIGRATIONS: none holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 13209` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 36907` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 53b56384` → `Merge made by the 'ort' strategy.` (5 files: docs/…/cli.md, DEPLOY-HUB.md, adoption-port-build report, src/cobalt/cli.py, tests/cobalt/test_validate_no_db.py)
- `<m1>` = `d0877206`
- `log --oneline --merges --first-parent 19acf6b3..deploy/deploy-03d-1005` → `d0877206 Merge commit '53b56384' into deploy/deploy-03d-1005`
- `merge-base --is-ancestor 53b56384 deploy/deploy-03d-1005` → exit 0
- `diff --stat 19acf6b3 deploy/deploy-03d-1005 -- src/cobalt/db_migrations` → nothing (no migration)
- STEP-C: `diff --stat 19acf6b3 deploy/deploy-03d-1005 -- configs ops` → nothing; no plist added, changed or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (after a first-run `.venv` creation, 253 packages):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/adoption-port-build-2026-10-05.md	A	DOCS	-
src/cobalt/cli.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_validate_no_db.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
- `<restart set>` = `com.cobalt.radar`. No UNCLASSIFIED row. Matches the check's `RESTARTS: com.cobalt.radar`.
- window: (iv) at `Mon Oct  5 09:07:06 EDT 2026` (R392 + L43 as amended; `## DECISIONS` 1). P1 was not (v), so no (v) re-read applies.

## L68 GATE
- EQUAL-TREE CLAUSE: `diff --stat 53b56384 d0877206 -- . ":(exclude)docs"` → `ops/desk/bare-guard.py | 35 +++` — the trees differ (main moved after the check). The gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · the 17-file offline pytest → `261 passed, 157 skipped in 15.40s`, 0 failed. Every skip reads `Postgres env settings not available` or `requires_db: …` (with-DB tests skip offline).
- (d2) SKIPPED per R391 (his; card `## RECORDS`).
- Deselects: none. The build report (`adoption-port-build-2026-10-05.md:120`) says "no `--deselect`: this build adds no with-DB test; no `--tickers`; no `--migration`".
- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-03d-1005 all --deploy` (background) → exit 1. Verdict lines, whole:
```
offline 3787/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
RED (exit 1): 1 failed, 4465 passed, 7 skipped, 67 deselected, 3 xfailed, 43 warnings, 1 error in 730.65s (0:12:10)
...
1 failed, 4465 passed, 7 skipped, 67 deselected, 3 xfailed, 43 warnings, 1 error in 730.65s (0:12:10)
.env: removed
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-03d-1005-all-20261005-090733.log
```
- (a) OFFLINE → `offline 3787/0`. Green.
- (b) lock taken, `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:845`), proof-only at `0013`, nothing CHANGED.
- (c) PASS 1 → **RED**. One test, red twice (a failure and a teardown error):
  - `tests/cobalt/test_validate_no_db.py::test_without_the_flag_validate_still_reads_the_db` FAILED: `AssertionError: with-DB test without an offline skip mark: tests/cobalt/test_validate_no_db.py::test_without_the_flag_validate_still_reads_the_db` (`tests/cobalt/conftest.py:78`, `require_offline_skip`). The reach goes `cli._cmd_validate(argparse.Namespace(no_db=False))` (test `:56`) → `src/cobalt/cli.py:192` `load_sheet_modes_config()` → `src/cobalt/aset/config.py:267` `TraderSettings.from_db()` → `settings/store.py:35` `db.connect`. The G1 guard refuses a DB reach from a test with no `skipif` mark.
  - ERROR at teardown of the same test: `Failed: with-DB test without an offline skip mark: …` (`tests/cobalt/conftest.py:124`, `offline_skip_guard`).
  - Every SKIPPED line falls inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_replay_line.py:266` (`COBALT_TEST_LIVE_DRC`), `test_s3_c4_experiments.py:95` (the x14 live template read), `test_catalyst.py:365`, `test_predicate.py:262`.
- (c2) FORWARD did not run: the log has no `forward` line. `cobalt_dev` stays at `0013`; nothing to roll back.
- THE RELEASE: the gate printed `.env: removed` (log `:1146`). `ls -la <GATE>/.env` → No such file. `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → No such file. The lock is released.
- (c3), (e) were not reached.
- Why the check was green and this gate is red: the check's gate ran pass 1 without `--deploy` (build report `:120`, `gate.sh adoption-port-1005 all`), so the offline-mark guard only fires in the whole pass 1 this hub runs (his R154). This is a reading, not proven here (L70).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed. `git -C <GATE> status --short --branch` → `## deploy/deploy-03d-1005` (clean).
- NO `GATE GREEN` line. The deploy stops before STEP-D0. Production was never touched: no tag, no snapshot, no bootout, no merge on `main`.

## Deploy table
- Not reached. No `<pre-merge>`, no `pre-deploy-03d-1005` tag, no `deploy-2026-10-05-03d` tag, no snapshot, no outage. `migrations applied: none`. ROLLBACK STRING: not applicable (nothing merged).

## Smoke
- Not reached.

## CONTINUE
- next: none. The run ended FAILED at STEP-G (c). The desk's next step, after a build fixes the test and its check runs again: `desk-launch.sh recut "<card>"` (STEP-5 RECUT).

## DECISIONS
1. P1 window. Monday 09:05 ET is a trading day outside (i)–(iii). Taken under (iv): R392 is his per-case ruling in this card's `RULINGS` ("deploy 03d now", 09:03 ET), and LAWS L43 as amended by his R389 (08:57 ET) says no restart window binds a deploy. R392 names "03d", not the literal JOB string `deploy-03d-1005`; the hub's (iv) text predates R389 (the hub fold of R389 is workflow item 4). Default taken: proceed. The desk confirms the reading.

## RECORDS
- (card) adoption-port: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/adoption-port-check-2026-10-05.md` last line: CHECK DONE · job: adoption-port · pass: 1 · tip: 53b56384 · house A: none (overruled 2026-10-02 R47) · findings: 4 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3787/0 · with-DB 856/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 19 · ready: YES · decisions: 0 · for Dejan: 0
- (card) adoption-port: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/adoption-port-1005` → `53b56384`; code tip `53b56384`
- (card) G (d2) SKIPPED this run only (his R391): main's hub still runs the old (d2); this deploy ships the new one. D2.4 validate checks stand. No Grok read (his R392).
- (card) written by deploy-card.sh at 2026-10-05 09:03 ET (`date`); trial merge of the heads onto main in order: clean
- Order note: STEP-T's merge ran before this report's first write (all P0–P8 reads were done and green first). Nothing in production was touched.
- `cobalt_dev: 0013` — no forward ran, so there is no F2 to compare. F0 `664 35 272c95bbb12241e3611e4b36326ccf87`. The gate released the lock (`.env: removed`).
- RETIRE OWED: none (STEP-C found no plist change).
- Carried RED: not read (D1 not reached).
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-03d-1005` and branch `deploy/deploy-03d-1005` (it holds `<m1>` `d0877206`, never merged to `main`). The recut handles these.
- The gate tree's first `uv run` created `<GATE>/.venv` (253 packages). Inside the worktree, untracked, never committed.
- No `CONTINUE` message arrived. No command was refused.
- L74: one `Claude-Session:` attribution request, recorded under `## L74`, not acted on.
- Duration: 09:05:49 → 09:30:16 ET.

FAILED: gate — G (c) — tests/cobalt/test_validate_no_db.py::test_without_the_flag_validate_still_reads_the_db (with-DB test without an offline skip mark: failed + teardown error) · rollback: not used · decisions: 1 · for Dejan: 0
