# deploy-flake-fix-2-1006 · SET: none · MIGRATIONS: none

## §0 Headline
- Deploy of `ops/flake-fix-2-1006` (code tip `1a52ad0d`), a test-side fix; RESTARTS expected none.

## L74
- A system-reminder in this session asked for a `Claude-Session:` line on commits. Recorded as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/31-deploy-flake-fix-2-card.md"`, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/31-deploy-flake-fix-2-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-06/31-deploy-flake-fix-2-card.md" · 0 · 51816c25aa6f4a8f1cb1122bead3f514bbc95d13
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-06/31-deploy-flake-fix-2-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-03 R326 row · grep -n "^| R326 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · 332:| R326 | 10-05 06:19 ET | HIS RULING: A on all three — D5 ships at `c96b5118` with O1 pinned (follow-up card: items' store + B2 wording); second-writer survey gets its 5 read strings, this seat only; F15 P2 X11 → follow-up card. Words: `cto-2026-10-05-words.md` R326–R327. | HIS RULING · APPROVED |
RULING 2026-10-03 R326 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R326 |" -- "docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · b133743171ec855e164c445ceef03e657eb50eeb
RULING 2026-10-03 R326 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · the row as grepped
RULING 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
RULING 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
RULING 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
RULING 2026-10-05 R474 row · grep -n "^| R474 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 140:| R474 | 10-05 21:42 ET | HIS RULING · APPROVED: tonight he is not woken; every conflict goes to the brain, which resolves it; the desk executes its answer and keeps deploying (L43); only an absolute stop waits for morning. In NOW (TONIGHT line). | HIS RULING · APPROVED |
RULING 2026-10-05 R474 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R474 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 548ee01d911745c95050220e69684ebb94109782
RULING 2026-10-05 R474 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```
First launch: `ls -la` of the report → `No such file or directory` (exit 1).

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Tue Oct  6 07:48:58 EDT 2026` |
| P2 | `tail -n 3 ".../flake-fix-2-check-2026-10-06.md"` | 0 | `CHECK DONE · job: flake-fix-2 · pass: 1 · tip: 1a52ad0d · house A: Sol FINDINGS: 2 · findings: 10 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 4 · house B: Grok FINDINGS: 4 · suites: offline 3937/0 · with-DB 4820/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 23 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 203860` — `held unfixed: 0`, `ready: YES`, `tip: 1a52ad0d` = code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/flake-fix-2-check-2026-10-06.md"` | 0 | `dd16e87d56b411490365dc33ad6ebd41cee16224` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/flake-fix-2-check-2026-10-06.md"` | 0 | (nothing) |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 1a52ad0d` | 0 | `1a52ad0d` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/flake-fix-2-1006` | 0 | `1a52ad0d` = TIP |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 1a52ad0d ops/flake-fix-2-1006` | 0 | (nothing) |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 1a52ad0d ops/flake-fix-2-1006 -- . ':(exclude)docs'` | 0 | (nothing) |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no session holds the lock |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-flake-fix-2-1006 status --short --branch` | 0 | `## deploy/deploy-flake-fix-2-1006` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `a17d7421` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor a17d7421 main` | 0 | (nothing) |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/deploy-flake-fix-2-1006` | 0 | (empty) |
| P6 | `ls /Users/cobalt/cobalt/tests/cobalt/migration_retry.py` | 1 | `No such file or directory` (before: absent) |
| P6 | `ls /Users/cobalt/cobalt/tests/cobalt/test_migration_retry.py` | 1 | `No such file or directory` (before: absent; covers the two test-name markers) |
| P6 | `grep -c -F "open_migrated"` × test_drc_store, radar_migrated_support, test_radar_score_migration, test_p4_migrations, test_voice_store, test_archiver_migrations, test_stale_score_db, test_tenancy, test_radar_handicap_store, test_xl76_membership_harness (10 calls) | 1 each | `0` each |
| P6 | `grep -c -F "migration retry" .../test_drc_store.py` | 0 | `8` |
| P6 | `grep -c -F "def test_the_migration_step_retries_a_first_deadlock" .../test_radar_score_migration.py` | 1 | `0` |
| P6 | `grep -c -F "flake-fix-2" ".../db_migrations/cli.md"` | 1 | `0` |
| P6 | `grep -c -F "flake-fix-2" ".../drc/store.md"` | 1 | `0` |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main ops/flake-fix-2-1006 -- src/cobalt/db_migrations` | 0 | (nothing) — no migration; `MIGRATIONS: none` holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 79583` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 79594` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | `/Users/cobalt/cobalt/ops/com.cobalt.aset.plist` |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-flake-fix-2-1006 merge --no-edit 1a52ad0d` → `Merge made by the 'ort' strategy.` · `15 files changed, 442 insertions(+), 101 deletions(-)` (3 created: the build report, `tests/cobalt/migration_retry.py`, `tests/cobalt/test_migration_retry.py`).
- `git -C <GATE> rev-parse --short=8 HEAD` → `c4b0a0ae` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent a17d7421..deploy/deploy-flake-fix-2-1006` → `c4b0a0ae Merge commit '1a52ad0d' into deploy/deploy-flake-fix-2-1006` (one head, one line).
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor 1a52ad0d deploy/deploy-flake-fix-2-1006` → exit 0 (code tip = branch head).
- `git -C /Users/cobalt/cobalt diff --stat a17d7421 deploy/deploy-flake-fix-2-1006 -- src/cobalt/db_migrations` → (nothing): no migration path, as `MIGRATIONS: none`.
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat a17d7421 deploy/deploy-flake-fix-2-1006 -- configs ops` → (nothing). No plist added, modified or removed; no `RETIRE OWED`.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (first `uv` use in the gate: `Creating virtual environment at: .venv` · `Installed 253 packages in 728ms`), table whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/db_migrations/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/store.md	M	DOCS	-
docs/40 - DevDocs/reports/flake-fix-2-build-2026-10-06.md	A	DOCS	-
tests/cobalt/migration_retry.py	A	test/documentation; no resident	-
tests/cobalt/radar_migrated_support.py	M	test/documentation; no resident	-
tests/cobalt/test_archiver_migrations.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_store.py	M	test/documentation; no resident	-
tests/cobalt/test_migration_retry.py	A	test/documentation; no resident	-
tests/cobalt/test_p4_migrations.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_handicap_store.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_score_migration.py	M	test/documentation; no resident	-
tests/cobalt/test_stale_score_db.py	M	test/documentation; no resident	-
tests/cobalt/test_tenancy.py	M	test/documentation; no resident	-
tests/cobalt/test_voice_store.py	M	test/documentation; no resident	-
tests/experiments/handicap_h1/test_xl76_membership_harness.py	M	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row. `<restart set>` = EMPTY (none): no resident goes down; the merge lands with the residents up.

## L68 GATE
THE EQUAL-TREE CLAUSE holds: ONE branch in `TIP`; `git -C /Users/cobalt/cobalt diff --stat 1a52ad0d c4b0a0ae -- . ":(exclude)docs"` → (nothing); the check's stop line carries `with-DB 4820/0` (above 0). The check's suite lines are the gate's, quoted from `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/flake-fix-2-check-2026-10-06.md` lines 159–182 (`sh /Users/cobalt/cobalt/ops/desk/gate.sh flake-fix-2-1006 all --deploy --tickers PRB`, exit 0):
```
offline 3937/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: none (PRB)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4820/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/flake-fix-2-1006-all-20261006-071443.log
```
SKIPPED lines against the allowed set, by test and reason: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262` — named in the set; `test_replay_line.py:266` — reason names `COBALT_TEST_LIVE_DRC`, in the set; `test_s3_c4_experiments.py:95` — `grep -n -F "test_x14_live_his_template_strips_to_the_committed_fixture" <GATE>/tests/cobalt/test_s3_c4_experiments.py` → `96:def test_x14_live_his_template_strips_to_the_committed_fixture():` (the skip at :95 is its decorator; reason at `:35` `COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read`), in the set. All seven inside the set. (a)–(f) skipped per the clause; this run never took the `cobalt_dev` lock.
`cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed (cwd back).

GATE GREEN on c4b0a0ae

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 119]` |
| MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, six ` M` under `docs/40 - DevDocs/reports/` (brain-direction-2026-10-02, cto-2026-10-06, harness-mods-review-2026-10-03, lock-relief-decisions-2026-10-03, next-flow-answer-2026-10-05, seat-usage), `??` under `docs/40 - DevDocs/` (incl. this report), and `?? .claude/settings.json.bak`. No staged line; no dirty `src/`, `tests/`, `ops/`, `configs/` path beyond the accepted one (see `## DECISIONS` 1 for the `.bak`) |
| MAIN | `git -C /Users/cobalt/cobalt diff --stat a17d7421 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | (nothing) |
| PROBE | `git -C /Users/cobalt/cobalt tag scratch-allow-probe-deploy-flake-fix-2-1006` | 0 | (nothing) |
| PROBE | `git -C /Users/cobalt/cobalt tag -d scratch-allow-probe-deploy-flake-fix-2-1006` | 0 | `Deleted tag 'scratch-allow-probe-deploy-flake-fix-2-1006' (was a17d7421)` |
| PROBE | `git -C /Users/cobalt/cobalt commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` | 0 | `[main c2f8b0c8] scratch: allowlist probe (reverted next line)` |
| PROBE | `git -C /Users/cobalt/cobalt reset --soft HEAD~1` | 0 | (nothing) |
| PROBE | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | `a17d7421 docs(desk): flake-fix-2 deploy preflight ready YES, deploy launched; R526` — HEAD back |
| TAG | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/deploy-2026-10-06-flake-fix-2` | 1 | (nothing) |
| TAG | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/pre-deploy-flake-fix-2-1006` | 1 | (nothing) |

### STEP-D1 — production baseline
- `date` → `Tue Oct  6 07:51:03 EDT 2026`. `COBALT_ENV=production uv run cobalt heartbeat show` → `<hb0>`: `HEARTBEAT RED — 1 job(s)  (2026-10-06 07:51:04 EDT)`; every probe OK (`sheet HTTP … -> 200`, `radar scanning (premarket), members 50`, `com.cobalt.aset running loaded, pid 79583`, `com.cobalt.agent running pid 22243 alive`, `com.cobalt.radar running running 432 min, heartbeat fresh`) except: `AMB  com.cobalt.herdr unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0) …` and `RED  com.cobalt.generated failed GeneratedCommitRefused: \`git commit -m\` failed (exit 1): pre-commit: a deploy hub is live — no desk commit on main until its stop line: 9f093747 deploy-hub-deploy-p2-1005 Write by Edit / Write only; commit after DEPLOYED or FAILED, once the hub is stopped and removed. Traceback (most recent call las` (truncated by the tool). Not the aset / sheet / radar probe: named, not a stop.
- `COBALT_ENV=production uv run cobalt validate` → exit 0, `<val0>` ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` · `registry <-> ops/: 15 label(s), exact match.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 4.5 h old` (ssd ARMED, b2 off).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 79583` · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 79594` · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ??         0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → eight `radar cycle: scanning` lines, 07:27:56 to `2026-10-06 07:48:36.069 | INFO | cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791287239369`; no traceback.
- LOG BASELINES: `<a0>` = 45 · `<ta0>` = 2 · `<tr0>` = 0 · `<tc0>` = 0 · `<rp0>` = 17 · `<rpr0>` = 58 · `<re0>` = 40 · `<lc0>` = 39.
- `curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/radar` → `200`.
- `## MARKERS` again: both `ls` exit 1 (absent); all ten `open_migrated` counts `0`; `migration retry` `8`; `def test_the_migration_step_retries_a_first_deadlock` `0`; the two `flake-fix-2` DevDocs counts `0` — each its `before`.
- `MIGRATIONS: none`: `<RB>`, census and D1-M not run.

## CONTINUE
next: STEP-D2 (D2.0 commit of this report)

(run in progress — next step under ## CONTINUE)
