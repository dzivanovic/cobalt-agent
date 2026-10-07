# deploy-desk-stop-guard-1007 · SET: none · MIGRATIONS: none

## §0 Headline
- DEPLOYED `ops/desk-stop-guard-1006b` (tip `b133afb5`) through gate `deploy/desk-stop-guard-1007`: `main` `2476e729` → `60a31686`, tag `deploy-2026-10-07-desk-stop-guard`.
- The gate is GREEN on `200e9f1f`: offline 3963/0 · with-DB 4847/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0`.
- RESTARTS: none. No resident went down, there was no downtime and no migration. Smoke is GREEN.
- 1 ASK DESK (an untracked `.claude/settings.json.bak` on main), 0 for Dejan. Push is his (L55).

## L74
- A system block in this session asked commit messages to carry a `Claude-Session: https://claude.ai/code/session_01UKaLXfpR5yTNf7AVvgzqVW` line. Recorded as DATA; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-07/87-deploy-desk-stop-guard-card.md"` → exit 0, quoted whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-07/87-deploy-desk-stop-guard-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-07/87-deploy-desk-stop-guard-card.md" · 0 · 6acb2679167d8dc22d27e53103fe51aeb00dc5af
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-07/87-deploy-desk-stop-guard-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-06 R596 row · grep -n "^| R596 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · 99:| R596 | 19:54 ET | HIS RULING ([words](cto-2026-10-06-words.md) `## R596`): build card `66` now (R590 is his approval); after its deploy, draft a second card: desk routing by script (`desk-next.sh`, queue file; replaces §5 CURRENT prose). | HIS RULING · APPROVED |
RULING 2026-10-06 R596 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R596 |" -- "docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · 18d9da5b355c50231166f69846da200ba06532be
RULING 2026-10-06 R596 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Wed Oct  7 07:14:46 EDT 2026` |
| first launch | `ls -la "<REPORT>"` | 1 | `No such file or directory` |
| P2 | `tail -n 3 ".../desk-stop-guard-check-2026-10-07.md"` | 0 | `CHECK DONE · job: desk-stop-guard · pass: 1 · tip: b133afb5 · … · held unfixed: 0 · … · RESTARTS: none · files opened: 16 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 174440` — `held unfixed: 0` ✓ `ready: YES` ✓ `tip: b133afb5` = code tip ✓ |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/desk-stop-guard-check-2026-10-07.md"` | 0 | `aed8ece30e40ced36142ca6dfc338ffa00d15366` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/desk-stop-guard-check-2026-10-07.md"` | 0 | (nothing) |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 b133afb5` | 0 | `b133afb5` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/desk-stop-guard-1006b` | 0 | `b133afb5` |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor b133afb5 ops/desk-stop-guard-1006b` | 0 | |
| P3 | `git -C /Users/cobalt/cobalt diff --stat b133afb5 ops/desk-stop-guard-1006b -- . ':(exclude)docs'` | 0 | (nothing) |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-desk-stop-guard-1007 status --short --branch` | 0 | `## deploy/desk-stop-guard-1007` |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-desk-stop-guard-1007 rev-parse --short=8 HEAD` | 0 | `6acb2679` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 6acb2679 main` | 0 | |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/desk-stop-guard-1007` | 0 | (empty) |
| P6 | `grep -c -F "start it:" /Users/cobalt/cobalt/ops/desk/stop-guard.py` | 0 | `0` (before `0`) |
| P6 | `grep -c -F "def test_g1_the_desk_with_no_owed_block_is_blocked" /Users/cobalt/cobalt/tests/ops/test_stop_guard.py` | 0 | `0` (before `0`) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main b133afb5 -- src/cobalt/db_migrations` | 0 | (nothing) — MIGRATIONS: none ✓ |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 64112` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 64129` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-desk-stop-guard-1007 merge --no-edit b133afb5` → `Merge made by the 'ort' strategy.` (4 files: `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md`, `docs/40 - DevDocs/reports/desk-stop-guard-build-2026-10-06.md`, `ops/desk/stop-guard.py`, `tests/ops/test_stop_guard.py`; 793 insertions, 19 deletions)
- `git -C /Users/cobalt/cobalt-wt/deploy-desk-stop-guard-1007 rev-parse --short=8 HEAD` → `200e9f1f` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 6acb2679..deploy/desk-stop-guard-1007` → `200e9f1f Merge commit 'b133afb5' into deploy/desk-stop-guard-1007`
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor b133afb5 deploy/desk-stop-guard-1007` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat 6acb2679 deploy/desk-stop-guard-1007 -- src/cobalt/db_migrations` → (nothing): no migration path, MIGRATIONS: none ✓
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 6acb2679 deploy/desk-stop-guard-1007 -- configs ops` → ` ops/desk/stop-guard.py | 230 ++++++++++++++++++++++++++++++++++++++++++++++---` / ` 1 file changed, 216 insertions(+), 14 deletions(-)`. No plist added, modified or removed.

## RESTARTS
- `cd /Users/cobalt/cobalt-wt/deploy-desk-stop-guard-1007` · `ls -la …/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (after uv created the gate `.venv`: `Installed 253 packages in 704ms`):
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md	M	DOCS	-
docs/40 - DevDocs/reports/desk-stop-guard-build-2026-10-06.md	A	DOCS	-
ops/desk/stop-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_stop_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```
- No `UNCLASSIFIED` row. `<restart set>` = EMPTY (none). MIGRATIONS none, so the empty set is consistent.

## L68 GATE
- EQUAL-TREE CLAUSE: does not hold — the check's stop line carries `with-DB 0/0` (not above 0), so the gate runs whole (`--deploy`).
- (a0) `ls -la …/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_archiver_migrations.py … tests/cobalt/test_jobs_restarts.py` (the 17 files) → `261 passed, 163 skipped in 18.26s`; 0 failed (with-DB tests skip: `Postgres env settings not available` / `requires_db`).
- Deselects: none. The build report `desk-stop-guard-build-2026-10-06.md:83` names only a red-first `-k "g1 or …"` filter (`30 deselected`), not a with-DB pass-1 deselect. TICKERS none, no `--migration`.
- `ls -la …/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-desk-stop-guard-1007 all --deploy` → exit 0. Verdict lines, whole:
```
offline 3963/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4847/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-desk-stop-guard-1007-all-20261007-071624.log
```
- (a) offline `3963/0` → `<p>` = 3963.
- (c) PASS 1 skips: all seven are inside the allowed set. `test_s3_c4_experiments.py:95` is the `@requires_live` decorator of `test_x14_live_his_template_strips_to_the_committed_fixture` (Read of the gate tree, lines 95–96).
- (c2) log:1089 `dev forward: APPLIED 07:40:00`. No `CHANGED`.
- (c3) `with-DB 4847/0` → `<d>` = 4847.
- (f) log:879 `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` · log:1865 `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` → `cobalt_dev: 0013 — F2 = F0` (log:1916).
- THE RELEASE: log:1917–1922 `$ sh /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh deploy-desk-stop-guard-1007` → `lock released` · `.env: removed`. The log puts no clock on the release; it falls between `dev forward: APPLIED 07:40:00` and the gate's exit, before `date` → `Wed Oct  7 07:45:10 EDT 2026`. `ls -la <GATE>/.env` → No such file. `grep -c -x -F "deploy-desk-stop-guard-1007" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (no lock dir).
- (e) LIVE-NOTE, `.env` absent (log:1932–1989): `146 passed, 1 skipped`. The one skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …`, which is in the allowed set. No skip names `COBALT_LIVE_VAULT_ROOT`. → `<l>` = 146.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 200e9f1f

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 20]` |
| MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, ` M` × 6 and `??` × 13 under `docs/40 - DevDocs/`, plus `?? .claude/settings.json.bak` (see ASK DESK 1). No staged line, no dirty `src/` `tests/` `ops/` `configs/` path other than `configs/cobalt/rules.yaml`. |
| MAIN | `git -C /Users/cobalt/cobalt diff --stat 6acb2679 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | (nothing) |
| PROBE | `git -C /Users/cobalt/cobalt tag scratch-allow-probe-desk-stop-guard-1007` | 0 | |
| PROBE | `git -C /Users/cobalt/cobalt tag -d scratch-allow-probe-desk-stop-guard-1007` | 0 | `Deleted tag 'scratch-allow-probe-desk-stop-guard-1007' (was 6acb2679)` |
| PROBE | `git -C /Users/cobalt/cobalt commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` | 0 | `[main 1370cbbd] scratch: allowlist probe (reverted next line)` |
| PROBE | `git -C /Users/cobalt/cobalt reset --soft HEAD~1` | 0 | |
| PROBE | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | `6acb2679 docs(desk): deploy card 87 rulings narrowed to R596` (HEAD back) |
| TAG | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/deploy-2026-10-07-desk-stop-guard` | 1 | free |
| TAG | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/pre-desk-stop-guard-1007` | 1 | free |

### STEP-D1 (baseline)
- `date` → `Wed Oct  7 07:45:39 EDT 2026` · `COBALT_ENV=production uv run cobalt heartbeat show` → `<hb0>`: `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-07 07:45:40 EDT)`. The one non-OK row is `AMB  com.cobalt.herdr  unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0) [launchd probe]; runs outside launchd by declared interim`, which is not RED. Rows: `OK sheet HTTP http://127.0.0.1:5010/ -> 200`, `OK radar scanning (premarket), members 50`, `OK com.cobalt.aset running loaded, pid 64112`, `OK com.cobalt.agent running pid 22243 alive`, `OK com.cobalt.radar running running 781 min, heartbeat fresh`. No carried RED.
- `COBALT_ENV=production uv run cobalt validate` → exit 0, `<val0>` ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 10.1 h old`
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 64112` · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 64129` · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ??  0:00.04 uv run src/cobalt_agent/main.py`
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → `radar cycle: scanning` lines every ~3 min, the last at `2026-10-07 07:44:42.071`; no traceback.
- LOG BASELINES: `<a0>` 47 · `<ta0>` 2 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 17 · `<rpr0>` 58 · `<re0>` 40 · `<lc0>` 39
- `curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/radar` → `200`. MARKERS: `start it:` → `0`, `def test_g1_…` → `0` (both at their before values).
- MIGRATIONS none: no `<RB>`, no census read, no D1-M.

### STEP-D2
- D2.0 `git -C /Users/cobalt/cobalt add "docs/40 - DevDocs/reports/deploy-desk-stop-guard-1007.md"` · `git -C /Users/cobalt/cobalt commit -m "docs(report): deploy desk-stop-guard-1007 — gate green on 200e9f1f" -m "Co-Authored-By: …" -- "<REPORT>"` → `[main 2476e729] … 1 file changed, 138 insertions(+)`. `git -C /Users/cobalt/cobalt show --stat HEAD` lists the one file. `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `2476e729` = `<pre-merge>`.
- D2.1 `git -C /Users/cobalt/cobalt-wt/deploy-desk-stop-guard-1007 merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `git -C /Users/cobalt/cobalt-wt/deploy-desk-stop-guard-1007 rev-parse --short=8 HEAD` → `60a31686` = `<stack-final>`. `git -C /Users/cobalt/cobalt rev-parse --short=8 60a31686^2` → `2476e729` = `<pre-merge>` ✓. `git -C /Users/cobalt/cobalt merge-base --is-ancestor 200e9f1f 60a31686` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat 200e9f1f 60a31686 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → (nothing): docs-only ✓.
- D2.4 `backup status` before: `newest snapshot: 10.1 h old`. `COBALT_ENV=production uv run cobalt backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 5419.4 MB` · `ssd: snapshot a37ac379 — 1 new / 8 changed, 319.1 MB added, 1 pruned`. `backup status` after: `newest snapshot: 0.0 h old`.
- D2.5 `date` → `Wed Oct  7 07:47:29 EDT 2026` · `heartbeat show` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-07 07:47:30 EDT)`, 110 s after D1's 07:45:40. Same rows as `<hb0>`; no new RED. (The reads at 07:47:11, :17, :23 and :26, also all GREEN, filled the clock.)
- D2.6 `date` → `Wed Oct  7 07:47:35 EDT 2026` · `git -C /Users/cobalt/cobalt tag pre-desk-stop-guard-1007` → `rev-parse --short=8` → `2476e729` ✓.

### STEP-4 (restart set EMPTY)
- 4.1 `date` → `Wed Oct  7 07:47:48 EDT 2026` = `<t down>` (nothing goes down).
- 4.2 no label in the set: no bootout, no `cobalt.sh stop`.
- 4.3 `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `2476e729` = `<pre-merge>` ✓. `git -C /Users/cobalt/cobalt merge --ff-only deploy/desk-stop-guard-1007` → `Updating 2476e729..60a31686` / `Fast-forward` (4 files: CTO-DESK-WAKEUP.md, desk-stop-guard-build-2026-10-06.md, ops/desk/stop-guard.py, tests/ops/test_stop_guard.py). `date` → `Wed Oct  7 07:47:51 EDT 2026` = `<t up>`.
- 4.4 `migrations applied: none`.
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`.
- 4.6 nothing taken down: no bootstrap. Downtime: none (0 s).

## Smoke
- FIRST CALLS after `<t up>` 07:47:51: `<rp_up>` 17 · `<rpr_up>` 58 · `<re_up>` 40 · `<lc_up>` 39 (each equal to the D1 baseline).
- (a) `date` → `Wed Oct  7 07:48:05 EDT 2026` · `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 64112` (SAME as D1; aset not in the set ✓) · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 64129` (SAME ✓) · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` (SAME ✓). GREEN.
- (b) `date` → `Wed Oct  7 07:48:08 EDT 2026` · `grep -c "Started server process" …/aset.err` → `47` = `<a0>` (aset outside the set ✓) · aset Traceback `2` = `<ta0>` · radar Traceback `0` = `<tr0>` · TaxonomyConfigError `0` = `<tc0>`. `tail -n 30 …/aset.err`: the last `Started server process [64118]` is followed by `Uvicorn running on http://0.0.0.0:5010`, the last line is `2026-10-07 06:15:14.406 … vault_writes: purged 1 row(s) past 30-day retention`, and nothing comes after the merge.
- (c) `date` → 07:48:08 · `curl … http://127.0.0.1:5010/` → `200` · `…/radar` → `200` · `…/radar\?frame=phone` → `200`. GREEN.
- (d) MARKERS: `grep -c -F "start it:" /Users/cobalt/cobalt/ops/desk/stop-guard.py` → `4` (after `4` ✓) · `grep -c -F "def test_g1_the_desk_with_no_owed_block_is_blocked" /Users/cobalt/cobalt/tests/ops/test_stop_guard.py` → `1` (after `1` ✓). GREEN.
- (f) `COBALT_ENV=production uv run cobalt jobs restarts 2476e729..60a31686` → exit 0, the same four rows as STEP-R, `RESTARTS: none` = `<restart set>`, no `UNCLASSIFIED`. 4.5's validate stands for the validate half. GREEN.
- (g) no migration.
- (s) SMOKE READS: `stop-guard desk seat in the script` → `4` (exit 0, ≥1 ✓) · `G1 test present` → `1` (exit 0, ≥1 ✓). The stop-guard's tests were run by the gate (offline `3963/0` on `200e9f1f`). Nothing runs in production for them. GREEN.
- (e) heartbeat 1: `date` → `Wed Oct  7 07:48:20 EDT 2026` · `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-07 07:48:21 EDT)`; `com.cobalt.radar running running 783 min, heartbeat fresh`.

- (e) heartbeat 2: `date` → `Wed Oct  7 07:50:13 EDT 2026` · `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-07 07:50:14 EDT)`, 113 s after heartbeat 1; `com.cobalt.radar running running 785 min, heartbeat fresh`; no RED that is not in `<hb0>`. GREEN. (The reads at 07:48:31 through 07:50:51 that filled the clock were all `HEARTBEAT GREEN … nothing red`.)
- (b) radar tails: tail 1 at `date` → `Wed Oct  7 07:49:22 EDT 2026` (`<t up>` + 91 s) → last line `2026-10-07 07:47:38.869 … radar cycle: scanning scan_id=1791373582105`, from before `<t up>`. Tail 2 at `date` → `Wed Oct  7 07:50:55 EDT 2026` (+184 s) → `2026-10-07 07:50:35.839 | INFO | cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791373758897`: a cycle line stamped after `<t up>`, with no `radar S5 evaluate FAILED`, no `lifecycle card read failed` and no traceback. Settled GREEN at tail 2; a third tail is not needed.
- (h) REVERT-READBACK at 07:50:55 (≥ `<t up>` + 180 s, after (b) settled): `radar panel FAILED` `17` = `<rp_up>` · `radar pool refresh FAILED` `58` = `<rpr_up>` · `radar S5 evaluate FAILED` `40` = `<re_up>` · `lifecycle card read failed` `39` = `<lc_up>`. No count grew. `curl … /radar` → `200`; radar Traceback `0`. No census reads (none on the card). GREEN.

THE CHAIN:
- every check was committed (P2: `aed8ece3`, `ready: YES`, `held unfixed: 0`);
- the tips were re-read (P3: `b133afb5` = head);
- the tree merged clean (T: `200e9f1f`);
- RESTARTS was derived (R: none);
- the three suites were green on `200e9f1f` (G: offline 3963/0 · with-DB 4847/0 · live-note 146/0);
- `60a31686` = `200e9f1f` + docs (D2.3);
- the code landed (4.3: `2476e729..60a31686` fast-forward);
- markers 4 / 1 (d);
- no migration (g);
- the residents stayed up with unchanged pids (a);
- radar is cycling (b: 07:50:35; e: fresh);
- the set's reads pass (s: 4, 1);
- there is no new failure (h).

The card surface is not readable here; the desk confirms it with him (L70).

### STEP-7 close
- `git -C /Users/cobalt/cobalt tag deploy-2026-10-07-desk-stop-guard` → exit 0 (after the green smoke).
- DEPLOY TABLE SUMMARY: `<pre-merge>` `2476e729` → `<stack-final>` `60a31686` · tags `pre-desk-stop-guard-1007` (at `2476e729`), `deploy-2026-10-07-desk-stop-guard` (at `60a31686`) · `<t down>` / `<t up>` / seconds: `none` (empty set; the merge ran 07:47:48 → 07:47:51) · uv sync line: none in production. The gate worktree's first `uv run` created its own `.venv` (`Installed 253 packages in 704ms`). · proof cost: n/a (no migration) · `migrations applied: none` · `<RB>` before / after: n/a · snapshot `a37ac379` · `RESTARTS done: none`.
- THE ROLLBACK STRING (the desk's):
  1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 60a31686`. ONE revert of the main-into-gate merge. No resident is in the set, so none goes down or up.
  2. SCHEMA: none (no migration).
  3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.
- PRE-STOP SELF-CHECK:
  - (1) Every smoke row's evidence is quoted above with its `date` (07:48:05, 07:48:08, 07:48:20, 07:49:22, 07:50:13, 07:50:55).
  - (2) `git -C /Users/cobalt/cobalt merge-base --is-ancestor b133afb5 60a31686` → exit 0, and the same for `ops/desk-stop-guard-1006b` → exit 0. `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `60a31686`.
  - (3) REVERT-READBACK (h) is shown. Every count, sha and `file:line` here was re-read from tool output this run.
  - (4) STEP-T merged clean (`Merge made by the 'ort' strategy.`), and D2.1 too, so no conflict marker exists.
- THE RELEASE: the lock was released by `gate.sh` at STEP-G (`lock released`, `.env: removed`). Nothing has been held since.

## CONTINUE
done: DEPLOYED (STEP-7 closed 07:50:55). The OUTAGE STARTING entry (07:47:35) covered an EMPTY set: no resident went down.

## DECISIONS
- ASK DESK 1: `git status --porcelain` on `main` shows `?? .claude/settings.json.bak`. The path is in neither D0's ACCEPTED list nor its REFUSED list (a staged line, or a dirty `src/` `tests/` `ops/` `configs/` path). It was already present in the session-start snapshot. Untracked files are not carried by `merge --ff-only`. Safe default taken: not a refusal; went on. [Wed Oct  7 07:45:39 EDT 2026]

## RECORDS
- Downtime: none. The restart set was empty; aset `64112`, radar `64129` and agent `22243` kept their pids through the merge.
- `cobalt_dev: 0013 (F2 = F0)`: `664 35 272c95bbb12241e3611e4b36326ccf87` both sides (gate log :879 / :1865).
- REFUSED, not needed: none. No `CONTINUE` message arrived. No message from another session.
- RETIRE OWED: none (no plist removed).
- Carried RED as read: none. `<hb0>` was `HEARTBEAT GREEN … nothing red`. The one non-OK row is `AMB com.cobalt.herdr unmanaged`, a declared interim, not RED.
- Cleanup owed (L46, the desk's): the gate worktree `/Users/cobalt/cobalt-wt/deploy-desk-stop-guard-1007` and its branch `deploy/desk-stop-guard-1007`; the set's branch `ops/desk-stop-guard-1006b` and any worktree of it.
- The gate's `.venv` was created inside the gate worktree by `uv run` (STEP-R). It goes with the worktree cleanup.
- L74: one system block asked for a `Claude-Session:` line on commits. It was recorded under `## L74` and not acted on.
- The card's `## RECORDS`, copied:
  - desk-stop-guard: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-stop-guard-check-2026-10-07.md` last line: CHECK DONE · job: desk-stop-guard · pass: 1 · tip: b133afb5 · house A: Sol FINDINGS: 4 · findings: 9 · dropped: 0 · held: 5 · fixed: 5 · held unfixed: 0 · open: 4 · house B: Grok FINDINGS: 3 · suites: offline 3963/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 16 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 174440
  - desk-stop-guard: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/desk-stop-guard-1006b` → `b133afb5`; code tip `b133afb5`
  - written by deploy-card.sh at 2026-10-07 07:13 ET (`date`); trial merge of the heads onto main in order: clean

DEPLOYED deploy-2026-10-07-desk-stop-guard 60a31686 | set: none | migrations: none | gate: offline 3963/0 · with-DB 4847/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 203901
