# deploy-d5-1005 · set: s3 · migrations: none

## §0 Headline
- D5 (`drc/d5-reconcile-1004` at `c96b5118`) is live: `main` `62b9dfe0` → `c8503415`, tag `deploy-2026-10-05-d5`, rollback tag `pre-deploy-d5-1005`.
- Gate green on `55f0bf75`: offline 3900/0 · with-DB 4766/0 · live-note 146/0; `cobalt_dev: 0013 — F2 = F0`, lock released.
- aset and radar restarted (49 s down, 23:21:22 → 23:22:11); smoke GREEN on every row; no migration.
- O1 ships pinned as a strict xfail, carried by his R326 / R350.
- Decisions 2 (both ASK DESK, safe default taken), none for Dejan.

## L74
- A harness system reminder at the start of the session asked commits to end with a `Claude-Session:` line. Recorded once as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/64-deploy-d5-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/64-deploy-d5-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-05/64-deploy-d5-card.md" · 0 · 495b7bcee4471a49ea8dee91e10fd5b2c8468e2f
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-05/64-deploy-d5-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-03 R326 row · grep -n "^| R326 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · 332:| R326 | 10-05 06:19 ET | HIS RULING: A on all three — D5 ships at `c96b5118` with O1 pinned (follow-up card: items' store + B2 wording); second-writer survey gets its 5 read strings, this seat only; F15 P2 X11 → follow-up card. Words: `cto-2026-10-05-words.md` R326–R327. | HIS RULING · APPROVED |
RULING 2026-10-03 R326 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R326 |" -- "docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · b133743171ec855e164c445ceef03e657eb50eeb
RULING 2026-10-03 R326 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · the row as grepped
RULING 2026-10-05 R350 row · grep -n "^| R350 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 23:| R350 | 10-05 06:47 ET | HIS RULING (brain relay, same section, D): 10-02 R4 already let D5 ship with O1 pinned on 10-04; the brain's A/B was its error; the 10-05 standing row restates it. Order: rows + memory → his installs → desk restarts → brain restarts. | HIS RULING · APPROVED |
RULING 2026-10-05 R350 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R350 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · e89ef63a7003b1a9abe0f1377a3994cf525e00d4
RULING 2026-10-05 R350 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
RULING 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
RULING 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
RULING 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```
- R412 carries "production HOLD". Its words (`cto-2026-10-05-words.md` `## R412`): "Production stays on hold until the workflow set is deployed." Read in `cto-2026-10-05.md`: R454 (10-05 19:05 ET) "WORKFLOW SET COMPLETE; S3 resumes (K3 first)", and R471 K3 DEPLOYED. The hold's own condition is met, so it does not block this deploy.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| first launch | `ls -la "<REPORT>"` | 1 | `No such file or directory` |
| P1 | `date` | 0 | `Mon Oct  5 22:48:01 EDT 2026` |
| P2 tail | `tail -n 3 "…/drc-d5-check-2026-10-04.md"` | 0 | last line: `CHECK DONE · job: drc-d5 · pass: 2 · tip: c96b5118 · house B: Grok FINDINGS: 4 · findings: 4 · dropped: 0 · held: 2 · fixed: 1 · held unfixed: 1 · open: 3 · suites: offline 3898/0 · with-DB 867/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 18 · ready: NO · decisions: 5 · for Dejan: 3` — carries `held unfixed: 1` and `ready: NO` (the row's literals); `tip: c96b5118` = code tip. The held defect (O1) is carried by RULINGS R326 and R350 |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/drc-d5-check-2026-10-04.md"` | 0 | `a1a1f33fb217d3df4e9e133f5d84357e4a046243` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/drc-d5-check-2026-10-04.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 c96b5118` | 0 | `c96b5118` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 drc/d5-reconcile-1004` | 0 | `c96b5118` (= row, = `TIP`) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor c96b5118 drc/d5-reconcile-1004` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat c96b5118 drc/d5-reconcile-1004 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no worktree holds a `.env` |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/deploy-d5-1005` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `784b885c` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 784b885c main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/deploy-d5-1005` | 0 | empty |
| P6 | `ls /Users/cobalt/cobalt/src/cobalt/drc/reconcile.py` | 1 | `No such file or directory` (before) |
| P6 | `ls /Users/cobalt/cobalt/tests/cobalt/test_drc_d5.py` | 1 | `No such file or directory` (before) |
| P6 | `ls /Users/cobalt/cobalt/tests/cobalt/test_drc_d5_db.py` | 1 | `No such file or directory` (before) |
| P6 | `ls /Users/cobalt/cobalt/tests/cobalt/test_drc_d5_experiments_db.py` | 1 | `No such file or directory` (before) |
| P6 | `grep -c -F "reconcile" /Users/cobalt/cobalt/src/cobalt/drc/units.py` | 0 | `5` (before) |
| P6 | `grep -c -F "refused_cards" /Users/cobalt/cobalt/src/cobalt/drc/build.py` | 1 | `0` (before) |
| P6 | `grep -c -F "NO_WRITER_CODE" …/drc/reconcile.py` | 2 | `grep: …/reconcile.py: No such file or directory` — the card's before is `0` "(the file is absent on main)"; the file is absent, so production does not carry it |
| P6 | `grep -c -F "requires_db" …/test_drc_d5_db.py` | 2 | `grep: …/test_drc_d5_db.py: No such file or directory` — same reading as the row above |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main c96b5118 -- src/cobalt/db_migrations` | 0 | nothing — no migration (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 17342` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 17353` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit c96b5118` → `Merge made by the 'ort' strategy.` (15 files changed, 2124 insertions(+), 29 deletions(-)); no conflict.
- `git -C <GATE> rev-parse --short=8 HEAD` → `55f0bf75` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 784b885c..deploy/deploy-d5-1005` → `55f0bf75 Merge commit 'c96b5118' into deploy/deploy-d5-1005` (one line, one head).
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor c96b5118 deploy/deploy-d5-1005` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat 784b885c deploy/deploy-d5-1005 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 784b885c deploy/deploy-d5-1005 -- configs ops` → whole: ` ops/desk/gate-lists.md | 4 ++--` / ` 1 file changed, 2 insertions(+), 2 deletions(-)`. No plist added, changed or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created the worktree's `.venv`: `Installed 253 packages in 776ms`), the table whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/drc_page.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/build.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/imports.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/reconcile.md	A	DOCS	-
docs/40 - DevDocs/cobalt/drc/units.md	M	DOCS	-
docs/40 - DevDocs/reports/drc-d5-build-2026-10-04.md	A	DOCS	-
ops/desk/gate-lists.md	M	operator script; no Cobalt reader	-
src/cobalt/aset/drc_page.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/drc/build.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/drc/imports.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/drc/reconcile.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/drc/units.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_drc_d5.py	A	test/documentation; no resident	-
tests/cobalt/test_drc_d5_db.py	A	test/documentation; no resident	-
tests/cobalt/test_drc_d5_experiments_db.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.aset com.cobalt.radar`.

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat c96b5118 55f0bf75 -- . ":(exclude)docs"` → 14 files (main's work since the check's base: `configs/cobalt/rules.yaml`, `ops/desk/*`, `src/cobalt/cli.py`, tests). Not empty → the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `261 passed, 157 skipped in 15.61s`, 0 failed (every skip a with-DB `Postgres env settings not available` / `requires_db` skip).
- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-d5-1005 all --deploy --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py` (the two deselects the build report names, `drc-d5-build-2026-10-04.md:142,213`; no `--tickers`, none on the card; no `--migration`) → exit 0. Verdict lines WHOLE:
```
offline 3900/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4766/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-d5-1005-all-20261005-225012.log
```
- (a) OFFLINE `offline 3900/0` (log:843 `3900 passed, 769 skipped, 2 xfailed`; the 2 xfailed include the pinned O1 strict xfail).
- (c) PASS 1 at `0013` / (c3) PASS 2: `with-DB 4766/0` (log:1066 `4589 passed, 7 skipped, 71 deselected, 4 xfailed` + log:1741 `177 passed, 1 deselected`). The seven SKIPPED lines are each inside the allowed set by test and reason: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`, the `test_replay_line.py` skip naming `COBALT_TEST_LIVE_DRC`, and `test_s3_c4_experiments.py:95` — the skip of `test_x14_live_his_template_strips_to_the_committed_fixture` (`grep -n -F "test_x14_live_his_template" tests/cobalt/test_s3_c4_experiments.py` → `96:def test_x14_live_his_template_strips_to_the_committed_fixture():`, the decorator on line 95).
- (b) proof-only at `0013`: nothing `CHANGED` (log:911); (c2) `dev forward: APPLIED 23:12:57` (log:1068); proof tables after forward and after rollback: `content UNCHANGED on every table` (log:1133, :1796).
- (f) `cobalt_dev: 0013 — F2 = F0` (log:1857).
- THE RELEASE: `.env: removed`; log:1858–1859 `release-devdb-lock.sh deploy-d5-1005` → `lock released` (the log prints no clock for it; it falls between `dev forward: APPLIED 23:12:57` and my `date` 23:18:03). `ls -la <GATE>/.env` → No such file; `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → No such file.
- (e) LIVE-NOTE `live-note 146/0` (log:1928 `146 passed, 1 skipped`; the one skip is the `COBALT_TEST_LIVE_DRC` one, inside the set; no skip names `COBALT_LIVE_VAULT_ROOT`).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 55f0bf75

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| main | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 20]` |
| main | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`; ` M` ×5 and `??` ×11 under `docs/40 - DevDocs/` (this report among them); `?? .claude/settings.json.bak` (see `## DECISIONS` 1). No staged line; no dirty `src/`, `tests/`, `ops/`, `configs/` path |
| main | `git -C /Users/cobalt/cobalt diff --stat 784b885c main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| probe | `tag scratch-allow-probe-deploy-d5-1005` · `tag -d …` | 0 · 0 | — · `Deleted tag 'scratch-allow-probe-deploy-d5-1005' (was 784b885c)` |
| probe | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 38d297f5] scratch: …` · — · `784b885c docs(report): D5 deploy card preflight — 8 checks, 0 fails, ready YES` (HEAD back) |
| tags | `rev-parse --verify --quiet refs/tags/deploy-2026-10-05-d5` | 1 | absent |
| tags | `rev-parse --verify --quiet refs/tags/pre-deploy-d5-1005` | 1 | absent (first launch) |

### STEP-D1 (baseline, read-only)
- `date` → `Mon Oct  5 23:18:43 EDT 2026`. `<hb0>` = `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-05 23:18:44 EDT)`; `OK radar idle (overnight)`; `OK com.cobalt.aset running loaded, pid 17342`; `OK com.cobalt.agent running pid 22243 alive`; `OK com.cobalt.radar running running 120 min, heartbeat fresh`; `AMB com.cobalt.herdr unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0) … runs outside launchd by declared interim` (amber, not red). No RED.
- `<val0>` = `COBALT_ENV=production uv run cobalt validate` → exit 0, `13 trade_def(s) validated OK from the vault.`, `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` / `registry <-> ops/: 15 label(s), exact match.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 0.8 h old`.
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` = `17342`; `launchctl print gui/501/com.cobalt.radar` → `state = running`, `<radar pid>` = `17353`; `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).`; `ps -p 22243` → `22243 ??         0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → eight `radar cycle: idle:overnight scan_id=None` lines, 23:07:10 to `2026-10-05 23:18:51.012`; no traceback.
- LOG BASELINES: `<a0>` `Started server process` (aset.err) = `43` · `<ta0>` Traceback aset.err = `2` · `<tr0>` Traceback radar.err = `0` · `<tc0>` TaxonomyConfigError radar.err = `0` · `<rp0>` `radar panel FAILED` = `17` · `<rpr0>` `radar pool refresh FAILED` = `58` · `<re0>` `radar S5 evaluate FAILED` = `40` · `<lc0>` `lifecycle card read failed` = `39`.
- `curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/radar` → `200`.
- MARKERS again: the four `ls` → `No such file or directory`; `reconcile` in units.py `5`; `refused_cards` in build.py `0`; `NO_WRITER_CODE` / `requires_db` → `No such file or directory` (exit 2; file absent) — each its `before`.
- No migration: no `<RB>`, no census, no D1-M proof-only.

### STEP-D2
- D2.0 report committed `62b9dfe0` (`docs(report): deploy deploy-d5-1005 — gate green on 55f0bf75`); `show --stat HEAD` → that one file, 164 insertions. `<pre-merge>` = `62b9dfe0`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `<stack-final>` = `c8503415`; `c8503415^2` → `62b9dfe0` = `<pre-merge>`; `merge-base --is-ancestor 55f0bf75 c8503415` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat 55f0bf75 c8503415 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing (docs only).
- D2.4 `backup status` before → `newest snapshot: 0.8 h old`; `COBALT_ENV=production uv run cobalt backup run` → `backup: cobalt_brain dumped, 4889.4 MB` · `ssd: snapshot ad0cb2b7 — 0 new / 2 changed, 12.8 MB added, 1 pruned`; `backup status` after → `newest snapshot: 0.0 h old`.
- D2.5 `date` 23:20:33 · `heartbeat show` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-05 23:20:36 EDT)` — 112 s after D1's 23:18:44; aset pid 17342, radar `running 122 min, heartbeat fresh`; no new RED.
- D2.6 `date` → `Mon Oct  5 23:20:41 EDT 2026`; `git -C /Users/cobalt/cobalt tag pre-deploy-d5-1005` at `62b9dfe0`.

### STEP-4 (the outage)
| step | command | result |
|---|---|---|
| 4.1 | `date` | `Mon Oct  5 23:21:22 EDT 2026` = `<t down>` |
| 4.2 | `launchctl bootout gui/501/com.cobalt.aset` · `launchctl print gui/501/com.cobalt.aset` | exit 0 · exit 113 `Could not find service "com.cobalt.aset" in domain for user gui: 501` |
| 4.2 | `launchctl bootout gui/501/com.cobalt.radar` · `launchctl print gui/501/com.cobalt.radar` | exit 0 · exit 113 `Could not find service "com.cobalt.radar" in domain for user gui: 501` |
| 4.3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` | `62b9dfe0` = `<pre-merge>` |
| 4.3 | `git -C /Users/cobalt/cobalt merge --ff-only deploy/deploy-d5-1005` | `Updating 62b9dfe0..c8503415` / `Fast-forward` (15 files, 2124 insertions, 29 deletions) |
| 4.4 | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | exit 0; `13 trade_def(s) validated OK from the vault.`; `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>`; no uv sync line |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | exit 0, no output |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` | exit 0, no output |
| 4.6 | `launchctl print` aset · radar | `state = running`, `pid = 47333` (≠ 17342) · `state = running`, `pid = 47343` (≠ 17353) |
| 4.6 | `date` | `Mon Oct  5 23:22:11 EDT 2026` = `<t up>`; downtime 49 s |

### STEP-7 summary
| item | value |
|---|---|
| main | `62b9dfe0` (`<pre-merge>`) → `c8503415` (`<stack-final>`); `git -C /Users/cobalt/cobalt log --oneline -1` → `c8503415 Merge branch 'main' into deploy/deploy-d5-1005` |
| tags | `pre-deploy-d5-1005` at `62b9dfe0`; `deploy-2026-10-05-d5` at `c8503415` (set after the green smoke) |
| outage | `<t down>` 23:21:22 · `<t up>` 23:22:11 · 49 s |
| uv sync line | none on production (the gate worktree's own `.venv` was created at STEP-R) |
| proof cost | none (no migration; no production proof-only run) |
| migrations applied | none |
| `<RB>` before / after | none (no migration) |
| snapshot | `ad0cb2b7` (ssd; `cobalt_brain dumped, 4889.4 MB`) |
| RESTARTS done | `com.cobalt.aset com.cobalt.radar` |
| ROLLBACK STRING | 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 c8503415` — ONE revert of the main-into-gate merge; `com.cobalt.aset` and `com.cobalt.radar` down first, up after. 2. SCHEMA: none (no migration). 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>` (`Reapply "Merge branch 'main' into deploy/deploy-d5-1005"`). |

### PRE-STOP SELF-CHECK
1. Every smoke row's evidence is quoted verbatim with its `date` (`## Smoke`: 23:22:35, :39, :44, :54, 23:23:43, 23:24:48, 23:25:15).
2. Code tip and head `c96b5118` re-read at P3; `git -C /Users/cobalt/cobalt merge-base --is-ancestor c96b5118 c8503415` → exit 0.
3. REVERT-READBACK shown ((h): 17 / 58 / 40 / 39 at 23:25:15, = the counts at `<t up>`); every count, sha and `file:line` above comes from tool output in this run.
4. No conflict marker: STEP-T and D2.1 were clean ort merges; `grep -c -F "<<<<<<<" /Users/cobalt/cobalt/src/cobalt/drc/reconcile.py` → `0`.
- THE RELEASE: done at STEP-G (lock released by `gate.sh`; `<GATE>/.env` absent; no lock dir). Nothing held.

## Smoke
- FIRST CALLS after `<t up>` 23:22:11: `<rp_up>` `17` · `<rpr_up>` `58` · `<re_up>` `40` · `<lc_up>` `39` (= D1's baselines).
- (a) `date` 23:22:35 · `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 47333` (NEW, ≠ 17342) · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 47343` (NEW, ≠ 17353) · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` (agent not in the set; same pid). GREEN.
- (b) `date` 23:22:39 · `grep -c "Started server process" …/aset.err` → `44` (> `<a0>` 43, ≤ 45) · `tail -n 30 …/aset.err` → `INFO:     Started server process [47339]` … `2026-10-05 23:21:59.488 | INFO | cobalt.voice.web:voice_startup:183 - voice: scratch dir … locked by this process; start sweep deleted 0 file(s), 0 failed` · `INFO:     Application startup complete.` · `INFO:     Uvicorn running on http://0.0.0.0:5010 (Press CTRL+C to quit)` · Traceback aset.err `2` (= `<ta0>`) · Traceback radar.err `0` (= `<tr0>`) · TaxonomyConfigError radar.err `0` (= `<tc0>`). Radar tails: below.
- (c) `date` 23:22:44 · `curl … http://127.0.0.1:5010/` → `200` · `…/radar` → `200` · `…/radar\?frame=phone` → `200` (first attempt each). GREEN.
- (d) MARKERS (same call block, 23:22:44): `ls …/drc/reconcile.py` → `/Users/cobalt/cobalt/src/cobalt/drc/reconcile.py` · `ls …/test_drc_d5.py` → listed · `ls …/test_drc_d5_db.py` → listed · `ls …/test_drc_d5_experiments_db.py` → listed · `reconcile` in units.py → `8` · `refused_cards` in build.py → `2` · `NO_WRITER_CODE` in reconcile.py → `4` · `requires_db` in test_drc_d5_db.py → `4`. Each its `after`. GREEN.
- (s) SMOKE READS: `grep -c -F "def test_" …/test_drc_d5.py` → `27` (exit 0, ≥1) · `grep -c -F "NO_WRITER_CODE" …/reconcile.py` → `4` (exit 0, ≥1). GREEN. The tests themselves are quoted from the gate (`## L68 GATE`); none ran in production.
- (f) `date` 23:22:54 · `COBALT_ENV=production uv run cobalt jobs restarts 62b9dfe0..c8503415` → exit 0, the same 15 rows, no `UNCLASSIFIED`, `RESTARTS: com.cobalt.aset com.cobalt.radar` (= STEP-R's set) · `COBALT_ENV=production uv run cobalt validate` → exit 0, `13 trade_def(s) validated OK from the vault.`, `Jobs (F17): 15 registered — 6 resident, 9 one-shot.`, `Placement (docs/PLACEMENT.md): tree clean.` (as 4.5). GREEN.
- (e) first read: `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-05 23:22:57 EDT)`; `OK com.cobalt.aset running loaded, pid 47333`; `OK com.cobalt.radar running running 1 min, heartbeat fresh`. (A clock-filler read at 23:23:08 was also GREEN, same lines.)
- (g) no migration.
- (b) radar tail 1: `date` 23:23:43 (`<t up>` + 92 s) · `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` → the restart's start lines from `2026-10-05 23:21:59.850 | INFO | cobalt.jobs.wrapper:job_run:173 - F17: com.cobalt.radar RUNNING (timeout 300s, heartbeat every 100s)`, then `2026-10-05 23:21:59.964 … radar cycle: idle:overnight scan_id=None` and `2026-10-05 23:23:40.005 | INFO     | cobalt.radar.runner:resident:467 - radar cycle: idle:overnight scan_id=None` — a cycle line stamped after `<t up>`, no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → settled GREEN at the first tail.
- (e) second read: `date` 23:24:48 · `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-05 23:24:55 EDT)` — 118 s after the first (23:22:57); `OK com.cobalt.radar running running 3 min, heartbeat fresh`; no RED not in `<hb0>`. GREEN. (Clock-filler reads at 23:23:29, :23:36, :23:52, :24:22, :24:36, :24:43, :25:03, :25:10: all `HEARTBEAT GREEN … nothing red`.)
- (h) REVERT-READBACK: `date` 23:25:15 (`<t up>` + 184 s) · `radar panel FAILED` `17` · `radar pool refresh FAILED` `58` · `radar S5 evaluate FAILED` `40` · `lifecycle card read failed` `39` — each = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>`, nothing grew · `curl … /radar` → `200`. No census reads (no migration). GREEN.

SMOKE: GREEN.

THE CHAIN: every check committed (P2: `a1a1f33f`, clean, its held O1 carried by R326/R350) → the tips re-read (P3: `c96b5118` = head = code tip) → the merged tree (T: `55f0bf75`, clean ort merge) → RESTARTS derived (R: `com.cobalt.aset com.cobalt.radar`, no UNCLASSIFIED) → three suites green on `<m1>` (G: offline 3900/0 · with-DB 4766/0 · live-note 146/0) → `<stack-final>` `c8503415` = `<m1>` + docs (D2.3: nothing outside docs) → the landed code (4.3: `Updating 62b9dfe0..c8503415`, Fast-forward) → markers at their `after` (d) → no migration (g) → residents up on new pids after the merge (a: aset 47333, radar 47343) → radar cycling (b: 23:23:40 cycle line; e: heartbeat fresh twice) → the set's reads (s: 27 tests, 4 `NO_WRITER_CODE`) → no new failure (h: the four counts unchanged). The card surface is not readable here; the desk confirms it with him (L70).

## CONTINUE
- OUTAGE STARTING 23:20:41 — residents of com.cobalt.aset com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
- OUTAGE ENDED 23:22:11 — both residents running on `c8503415`.
- Smoke GREEN 23:25:15; tag set; report closed. Nothing left for this session.

## DECISIONS
1. ASK DESK: `?? .claude/settings.json.bak` on `main` is not on D0's ACCEPTED list (only ` M .claude/settings.json` is) and not on its REFUSED list (no staged line; not under `src/`, `tests/`, `ops/`, `configs/`). Safe default taken: not a refusal, left untouched, deploy goes on. The same file was recorded the same way by guard-b (R399) and launcher F5 (R476). [23:18:43]
2. ASK DESK: the gate ran with no `--tickers` (the card names none; the build and check gates used `--tickers TEST`), so the stray-row read printed `stray rows: not read (no --tickers given)`. Safe default: followed the card; the gate's other legs are green.

## RECORDS
- Downtime: aset and radar down 49 s (`<t down>` 23:21:22 → `<t up>` 23:22:11); under 300 s.
- `cobalt_dev: 0013 (F2 = F0)` (gate log:1857); lock released by `gate.sh` (log:1859); `.env` absent.
- RETIRE OWED: none (no plist removed).
- Carried RED as read: none. `<hb0>` was GREEN with nothing red; the only non-OK row is `AMB com.cobalt.herdr` (amber, a declared interim), the same before and after.
- REFUSED, not needed: none. Messages not followed: none.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-d5-1005` and branch `deploy/deploy-d5-1005`; the set's branch `drc/d5-reconcile-1004` and its worktree `drc-d5-1004` if present. The desk's job.
- Markers 7 and 8 at P6/D1 read `grep: … No such file or directory` (exit 2), not a printed `0`: the card's `before` says `0` "(the file is absent on main)", so the absent file was read as that before value.
- The L74 line: one system reminder asked for a `Claude-Session:` line on commits; recorded under `## L74`, not acted on.
- From the card's `## RECORDS` (the desk's facts, copied):
  - drc-d5: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/drc-d5-check-2026-10-04.md` last line: CHECK DONE · job: drc-d5 · pass: 2 · tip: c96b5118 · house B: Grok FINDINGS: 4 · findings: 4 · dropped: 0 · held: 2 · fixed: 1 · held unfixed: 1 · open: 3 · suites: offline 3898/0 · with-DB 867/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 18 · ready: NO · decisions: 5 · for Dejan: 3
  - drc-d5: head `c96b5118`; code tip `c96b5118`. The held item, from the check (`## DECISIONS` 3): "O1 HELD, NOT FIXED (a carried held defect; confirmed again by house B, B3). An unresolved item stored on a date that a later statement re-pairs is lost (`store.py:935`). Its red is pinned as `test_check_o1_…` (strict xfail). Fixing it needs a build: a card row naming `src/cobalt/drc/store.py`, or a store for the items (a migration). Default: ships as a known gap, pinned."
  - THE O1 CARRY (his ruling): R326 (`cto-2026-10-03.md`, `HIS RULING · APPROVED`, committed `b1337431`) "A on all three — D5 ships at `c96b5118` with O1 pinned (follow-up card: items' store + B2 wording)"; R350 (`cto-2026-10-05.md`, committed `e89ef63a`) restates it. D5 ships with O1 pinned as a strict `xfail` (`tests/cobalt/test_drc_d5.py`, `test_check_o1_a_re_paired_date_keeps_its_stored_unresolved_item`). The O1 store and the B2 wording are owed rows on card `03` (R381), NOT part of this deploy.
  - G (d2): per the sibling cards' RECORDS wording on its state at deploy time; no Grok read (R412).
  - K3/D5 seam: fixed on main by K3-F1 `0ebdf95e`, inside `07a4b8fe` (K3 DEPLOYED). D5 never touches `tests/cobalt/test_drc_k3.py`.
  - A D5 test that reaches the database without `requires_db` would be K3's pattern (a fix row on card `03`); read at `c96b5118`: none found. The gate here was green.
  - Merge base `3e40359a`; no overlap by name with main's files; the trial merge at old main `57c7502c` was clean. This run's STEP-T merge at main `784b885c` was clean.
  - Gate history of the check: earlier red gates on a `cobalt_dev` migration-0002 `DeadlockDetected` outside this job's files; final gates green. This run's gate: no `DeadlockDetected`, green.
  - Open items carried by the check, not part of this deploy: A3 (R314 KEEP) and B2 (owed on card `03` by R326). After this deploy the P2 trial merge `c96b5118 6269f05e` → clean `c02eeec7` (`02-deploy-s3-card.md`).
  - One feature per deploy (R390): S3 on resume = K3 (DEPLOYED `07a4b8fe`), D5 now, then P2 alone.
  - Card written by the drafter `d5-deploy-draft` on 2026-10-05 22:4x EDT by hand; `deploy-card.sh` refuses `held unfixed: 1`.

DEPLOYED deploy-2026-10-05-d5 c8503415 | set: s3 | migrations: none | gate: offline 3900/0 · with-DB 4766/0 · live-note 146/0 | RESTARTS: com.cobalt.aset com.cobalt.radar | smoke: GREEN | decisions: 2 · for Dejan: 0 · tokens: 186102
