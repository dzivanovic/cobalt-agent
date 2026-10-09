# deploy guard-d2-g7-1009 · SET: none · MIGRATIONS: none

## §0 Headline
- DEPLOYED `deploy-2026-10-09-guard-d2-g7`: `ops/guard-d2-1009` (`8c6b5f7f`, D2: G3 reads every verb's words) and `ops/stop-guard-g7-1009` (`c8a31812`, G7: a QUEUE row blocks the stop) landed on `main` `b871dc97..ed4652f4`.
- Gate green on `77311f07`: offline 4036/0 · with-DB 4923/0 · live-note 146/0; `cobalt_dev` back at 0013 (F2 = F0), lock released.
- RESTARTS: none — operator scripts under `ops/desk/` only; no resident went down, downtime none. Smoke GREEN, markers `0 → 1`.
- Rollback tag `pre-guard-d2-g7-1009` at `b871dc97`; snapshot `983ff939`. Push is Dejan's, through the desk.

## L74
- One block arrived in a system reminder after launch asking that commits end with a `Claude-Session: https://claude.ai/code/session_01USsCCu1sbmzv84SpqgNdTo` line. Recorded here as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/175-deploy-guard-d2-g7-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/175-deploy-guard-d2-g7-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/175-deploy-guard-d2-g7-card.md" · 0 · 1f102ac3ef5bda1df17fcbddbe1ed6b93198d65d
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/175-deploy-guard-d2-g7-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R686 row · grep -n "^| R686 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 39:| R686 | 11:28 ET | HIS RULING (words R686, standing): every seat may run read-only production reads, no stamp; writes and secrets stay refused. Card `120`. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW; LAWS L62 at deploy |
RULING 2026-10-08 R686 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R686 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 4125ff02c9587ca901d9d5c418f378b8c77593a9
RULING 2026-10-08 R686 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| FIRST LAUNCH | `ls -la "<REPORT>"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Fri Oct  9 13:09:58 EDT 2026` |
| P2 D2 | `tail -n 3 ".../guard-d2-check-2026-10-09.md"` | 0 | `CHECK DONE · job: guard-d2-1009 · pass: 1 · tip: 8c6b5f7f · … · held unfixed: 0 · … · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 184393` (tip = row's code tip) |
| P2 D2 | `git log -1 --format=%H -- ".../guard-d2-check-2026-10-09.md"` | 0 | `32f2550c400e8bdb97ad06851138f93bdd8f6e7f` |
| P2 D2 | `git diff --stat -- ".../guard-d2-check-2026-10-09.md"` | 0 | nothing |
| P2 G7 | `tail -n 3 ".../stop-guard-g7-check-2026-10-09.md"` | 0 | `CHECK DONE · job: stop-guard-g7-1009 · pass: 1 · tip: c8a31812 · … · held unfixed: 0 · … · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 160632` (tip = row's code tip) |
| P2 G7 | `git log -1 --format=%H -- ".../stop-guard-g7-check-2026-10-09.md"` | 0 | `32f2550c400e8bdb97ad06851138f93bdd8f6e7f` |
| P2 G7 | `git diff --stat -- ".../stop-guard-g7-check-2026-10-09.md"` | 0 | nothing |
| P3 D2 | `rev-parse --short=8 8c6b5f7f` / `ops/guard-d2-1009` | 0 / 0 | `8c6b5f7f` / `8c6b5f7f` |
| P3 D2 | `merge-base --is-ancestor 8c6b5f7f ops/guard-d2-1009` · `diff --stat 8c6b5f7f ops/guard-d2-1009 -- . ':(exclude)docs'` | 0 · 0 | — · nothing |
| P3 G7 | `rev-parse --short=8 c8a31812` / `ops/stop-guard-g7-1009` | 0 / 0 | `c8a31812` / `c8a31812` |
| P3 G7 | `merge-base --is-ancestor c8a31812 ops/stop-guard-g7-1009` · `diff --stat c8a31812 ops/stop-guard-g7-1009 -- . ':(exclude)docs'` | 0 · 0 | — · nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 0 | `-rw-------  1 cobalt  staff  2186 Oct  9 13:09 /Users/cobalt/cobalt-wt/radar-top50-1009/.env` (another session holds the lock now) |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/guard-d2-g7-1009` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `c75d0046` = `<m0>` |
| P5 | `merge-base --is-ancestor c75d0046 main` | 0 | — |
| P5 | `log --oneline main..deploy/guard-d2-g7-1009` | 0 | empty |
| P6 | `grep -c -F "def secret_part(" /Users/cobalt/cobalt/ops/desk/bare-guard.py` | 1 | `0` (before `0`) |
| P6 | `grep -c -F "def queued(" /Users/cobalt/cobalt/ops/desk/stop-guard.py` | 1 | `0` (before `0`) |
| P7 | `diff --stat main 8c6b5f7f -- src/cobalt/db_migrations` · `diff --stat main c8a31812 -- src/cobalt/db_migrations` | 0 · 0 | nothing · nothing (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `pid = 43632` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `pid = 60578` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 8c6b5f7f` → `Merge made by the 'ort' strategy.` (`ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py`, build report; 3 files, 329+/11-)
- `git -C <GATE> merge --no-edit c8a31812` → `Merge made by the 'ort' strategy.` (`ops/desk/stop-guard.py`, `tests/ops/test_stop_guard.py`, build report; 3 files, 279+/19-)
- `git -C <GATE> rev-parse --short=8 HEAD` → `77311f07` = `<m1>`
- `log --oneline --merges --first-parent c75d0046..deploy/guard-d2-g7-1009` → `77311f07 Merge commit 'c8a31812' into deploy/guard-d2-g7-1009` · `ea76a0ef Merge commit '8c6b5f7f' into deploy/guard-d2-g7-1009`
- `merge-base --is-ancestor 8c6b5f7f deploy/guard-d2-g7-1009` → 0 · `merge-base --is-ancestor c8a31812 deploy/guard-d2-g7-1009` → 0 (code tips = branch heads)
- `diff --stat c75d0046 deploy/guard-d2-g7-1009 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none)
- STEP-C `diff --stat c75d0046 deploy/guard-d2-g7-1009 -- configs ops` →
```
 ops/desk/bare-guard.py | 47 +++++++++++++++++++++++++-------
 ops/desk/stop-guard.py | 72 ++++++++++++++++++++++++++++++++++++++++----------
 2 files, 96 insertions(+), 23 deletions(-)
```
  No plist added, modified or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/reports/guard-d2-build-2026-10-09.md	A	DOCS	-
docs/40 - DevDocs/reports/stop-guard-g7-build-2026-10-09.md	A	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
ops/desk/stop-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
tests/ops/test_stop_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```
(preceded by uv lines: `Creating virtual environment at: .venv` · `Installed 253 packages in 1.00s`)
`<restart set>` = EMPTY (none). No UNCLASSIFIED row.

## L68 GATE
- EQUAL-TREE CLAUSE: does not hold (two branches in `TIP`; both checks `with-DB 0/0`) → the gate runs whole.
- Deselects: none (the two build reports' `deselected` lines are `-k` mutation runs, not with-DB pass-1 deselections).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `262 passed, 163 skipped in 17.55s` (0 failed; skips are with-DB `Postgres env settings not available` / `requires_db`).
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-guard-d2-g7-1009 all --deploy` → exit 0. Verdict lines WHOLE:
```
offline 4036/0
lock: waited 5 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4923/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-guard-d2-g7-1009-all-20261009-131149.log
```
- (a) offline `4036/0`. (b) the lock waited 5 min (the radar-top50-1009 holder of P4), then taken; `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log :884); proof-only at `0013` nothing CHANGED.
- (c) pass-1 skips, each inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_replay_line.py:266` (reason names `COBALT_TEST_LIVE_DRC`), `test_s3_c4_experiments.py:95` = the decorator of `def test_x14_live_his_template_strips_to_the_committed_fixture` (line 96 in `<GATE>`), `tests/taxonomy/test_catalyst.py:365`, `tests/taxonomy/test_predicate.py:262`.
- (c2) `dev forward: APPLIED 13:40:16` (log :1094). (c3) with-DB `4923/0`.
- (f) `cobalt_dev: 0013 — F2 = F0` (log :2015); release `sh /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh deploy-guard-d2-g7-1009` → `lock released` (log :2016–2017); `.env: removed` (log :2021; no time stamped in the log; gate finished before `13:45:25`).
- (e) live-note `146 passed, 1 skipped` — the one skip is `test_replay_line.py:266` naming `COBALT_TEST_LIVE_DRC` (allowed); no skip naming `COBALT_LIVE_VAULT_ROOT`.
- After: `ls -la <GATE>/.env` → No such file · `grep -c -x -F "deploy-guard-d2-g7-1009" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent) · `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed · `date` → `Fri Oct  9 13:45:25 EDT 2026`.

GATE GREEN on 77311f07

## Deploy table
### STEP-D0 (deploy preflight)
| rule | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 36]` |
| MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, ` M`/`??` under `docs/40 - DevDocs/` only, plus `?? .claude/settings.json.bak` (untracked, not under src/tests/ops/configs); no staged line |
| MAIN | `diff --stat c75d0046 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `tag scratch-allow-probe-guard-d2-g7-1009` · `tag -d …` | 0 · 0 | — · `Deleted tag 'scratch-allow-probe-guard-d2-g7-1009' (was c75d0046)` |
| PROBE | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main b4b50472] …` · — · `c75d0046 docs(desk): D2 and G7 checked, deploy card waits for the cobalt_dev lock` |
| TAG | `rev-parse --verify --quiet refs/tags/deploy-2026-10-09-guard-d2-g7` | 1 | free |
| TAG | `rev-parse --verify --quiet refs/tags/pre-guard-d2-g7-1009` | 1 | free |

### STEP-D1 (production baseline)
- `date` → `Fri Oct  9 13:45:50 EDT 2026` · `<hb0>` = `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-09 13:45:51 EDT)`; one AMB: `com.cobalt.herdr unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0)` (declared interim); `com.cobalt.radar running 1281 min, heartbeat fresh`. No RED.
- `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.` · `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 16.1 h old` (ssd ARMED).
- aset `state = running`, `pid = 43632` · radar `state = running`, `pid = 60578` · `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ??  0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 radar.err` → last cycle `13:43:57.761 … radar cycle: scanning scan_id=1791567752779`, no traceback.
- Baselines: `<a0>` 51 · `<ta0>` 2 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 42 · `<lc0>` 39.
- `curl … /radar` → `200` · MARKERS: `def secret_part(` → `0`, `def queued(` → `0` (before values).
- MIGRATIONS: none → no `<RB>`, no census, no D1-M.

### STEP-D2
- D2.0 `add` + `commit … -- "docs/40 - DevDocs/reports/deploy-guard-d2-g7-1009.md"` → `[main b871dc97] docs(report): deploy guard-d2-g7-1009 — gate green on 77311f07` · `show --stat HEAD` → that one file (143+) · `rev-parse --short=8 main` → `b871dc97` = `<pre-merge>`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `<GATE>` HEAD → `ed4652f4` = `<stack-final>` · `ed4652f4^2` → `b871dc97` = `<pre-merge>` · `merge-base --is-ancestor 77311f07 ed4652f4` → 0.
- D2.3 `diff --stat 77311f07 ed4652f4 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- D2.4 `backup status` → `newest snapshot: 16.1 h old` · `backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 6493.2 MB` · `ssd: snapshot 983ff939 — 2 new / 4 changed, 491.9 MB added, 1 pruned` · `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `date` `13:47:21` → heartbeat `13:47:22` (91 s, short); filled with date + heartbeat pairs at 13:47:28, :33, :37 → `date` `13:47:41` · `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-09 13:47:42 EDT)` = 111 s after D1's `13:45:51`. No new RED; radar `running 1283 min, heartbeat fresh`.
- D2.6 `date` → `Fri Oct  9 13:47:46 EDT 2026` · `tag pre-guard-d2-g7-1009` → `b871dc97`.
- `<restart set>` EMPTY: no resident goes down; 4.1, 4.2, 4.6 act on nothing.

### STEP-4
- 4.1 `date` → `Fri Oct  9 13:47:56 EDT 2026` = `<t down>` (nothing down).
- 4.2 empty set: no bootout, no stop.
- 4.3 `rev-parse --short=8 HEAD` → `b871dc97` = `<pre-merge>` · `merge --ff-only deploy/guard-d2-g7-1009` → `Updating b871dc97..ed4652f4` / `Fast-forward` (6 files, 608+/30-).
- 4.4 `migrations applied: none`.
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.` · `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`.
- 4.6 empty set: nothing to bootstrap. `<t up>` = 4.3's `date` `13:47:56`; downtime: none.

## Smoke
`<t up>` = `13:47:56` (empty set: 4.3's `date`).
- FIRST CALLS: `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 42 · `<lc_up>` 39 (= D1).
- (a) `13:48:10` · aset `state = running`, `pid = 43632` (SAME, outside the set) · radar `state = running`, `pid = 60578` (SAME) · `Cobalt is ONLINE (PID: 22243).` (SAME). GREEN.
- (b) `13:48:14` · `Started server process` 51 = `<a0>` (aset outside the set) · aset Traceback 2 = `<ta0>` · radar Traceback 0 = `<tr0>` · TaxonomyConfigError 0 = `<tc0>` · `tail -n 30 aset.err` → last lines `10:36:13.585 … vault_writes: purged 1 row(s) past 30-day retention` / `WARNING:  Invalid HTTP request received.`; no traceback. Radar tails below.
- (c) `13:48:19` · `/` → `200` · `/radar` → `200` · `/radar\?frame=phone` → `200`. GREEN.
- (d) `13:48:23` · `def secret_part(` → `1` (after `1`) · `def queued(` → `1` (after `1`). GREEN.
- (s) `13:48:23` · D2 function present `def secret_part(` → `1` · secret guard still present `def is_secret(` → `1` · G7 function present `def queued(` → `1` · stop guard still reads the OWED block `def owed_block(` → `1`; each exit 0. GREEN. (The tests of both guards ran in the gate: offline 4036/0.)
- (f) `13:48:27` · `jobs restarts b871dc97..ed4652f4` → exit 0, the same six rows, `RESTARTS: none` = STEP-R's set, no UNCLASSIFIED · `validate` → exit 0, `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` GREEN.
- (g) no migration.
- (e) read 1 `13:48:29` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-09 13:48:30 EDT)`; radar `running 1284 min, heartbeat fresh`. Read 2 `13:50:20` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-09 13:50:21 EDT)` (111 s apart); radar `running 1286 min, heartbeat fresh`. No RED; the only non-OK row is the declared `AMB com.cobalt.herdr` of `<hb0>`. GREEN. (The interval was filled with date + heartbeat pairs, every one GREEN.)
- (b) radar tails: `13:49:26` (+90 s) `tail -n 12 radar.err` → last cycle `13:47:04.229 … radar cycle: scanning scan_id=1791567938128` (before `<t up>`), no failure, no traceback · `13:50:57` (+181 s) → `2026-10-09 13:50:09.483 | INFO | cobalt.radar.runner:resident:576 - radar cycle: scanning scan_id=1791568124256`, after `<t up>`, with no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback in the tail (radar Traceback count 0). SETTLED GREEN; the +300 s tail is not needed.
- (h) `13:51:01` (+185 s) · `<rp>` 18 · `<rpr>` 60 · `<re>` 42 · `<lc>` 39 = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (no growth) · `/radar` → `200`. No census reads (no migration). GREEN.

THE CHAIN: every check committed (P2: both check reports at `32f2550c`, unmodified, `held unfixed: 0` · `ready: YES`) → the tips re-read (P3: `8c6b5f7f`, `c8a31812`, heads equal) → the merged tree (T: `77311f07`, two clean `ort` merges, no migration path) → RESTARTS derived (R: none, no UNCLASSIFIED) → three suites green on `77311f07` (G: 4036/0 · 4923/0 · 146/0) → `<stack-final>` `ed4652f4` = `77311f07` + docs (D2.3: nothing outside docs) → the landed code (4.3: `Updating b871dc97..ed4652f4`, Fast-forward) → markers `0 → 1` (d) → no migration (g) → residents untouched and running on the same pids (a) → radar cycling after `<t up>` (b, e) → the set's four reads `1` each (s) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

### STEP-7 close
- `git -C /Users/cobalt/cobalt tag deploy-2026-10-09-guard-d2-g7` → `ed4652f4`.
- `<pre-merge>` `b871dc97` → `<stack-final>` `ed4652f4` · tags `pre-guard-d2-g7-1009` (`b871dc97`), `deploy-2026-10-09-guard-d2-g7` (`ed4652f4`) · `<t down>` / `<t up>` / seconds: none (empty set; 4.1 `13:47:56`) · uv sync line: `Creating virtual environment at: .venv` / `Installed 253 packages in 1.00s` (in `<GATE>`, STEP-R; none in production) · proof cost: n/a (no migration) · `migrations applied: none` · `<RB>`: none · snapshot `983ff939` · `RESTARTS done: none`.
- THE ROLLBACK STRING: 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 ed4652f4` — ONE revert of the main-into-gate merge (it carries the set's merges with it); `<restart set>` is empty, so no resident goes down or up. 2. SCHEMA: none (no migration). 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.
- PRE-STOP SELF-CHECK: (1) every smoke row above carries its `date` and its output verbatim. (2) P3 re-read `8c6b5f7f` and `c8a31812`; `merge-base --is-ancestor 8c6b5f7f ed4652f4` → 0 and `merge-base --is-ancestor c8a31812 ed4652f4` → 0; `rev-parse --short=8 HEAD` → `ed4652f4`. (3) REVERT-READBACK (h) shown, counts 18/60/42/39 re-read at `13:51:01`; every sha and count in this report was read from tool output this run. (4) STEP-T ran clean; `grep -c -F "<<<<<<<"` over the four landed code and test files → `0` each.

## CONTINUE
done — DEPLOYED; nothing to resume.

## DECISIONS
none

## RECORDS
- Downtime: none (empty restart set; no resident booted out).
- `cobalt_dev: 0013 (F2 = F0)` — `F0: 664 35 272c95bbb12241e3611e4b36326ccf87`; gate lock released by `release-devdb-lock.sh` (`lock released`), `.env: removed`.
- The gate waited 5 min for the `cobalt_dev` lock held by `radar-top50-1009` (P4), then took it; not a failure.
- No `REFUSED` line; no message from another session; no `RETIRE OWED`; no carried RED (heartbeat GREEN at every read; `com.cobalt.herdr` AMBER is the declared `launchd_unmanaged` interim).
- L74: one system-reminder block asked for a `Claude-Session:` trailer on commits; recorded under `## L74`, not followed.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-guard-d2-g7-1009` and branch `deploy/guard-d2-g7-1009`; the set's branches `ops/guard-d2-1009` and `ops/stop-guard-g7-1009` and their worktrees, if any.
- Card RECORDS (the desk's, copied):
  - guard-d2-1009: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/guard-d2-check-2026-10-09.md` last line: CHECK DONE · job: guard-d2-1009 · pass: 1 · tip: 8c6b5f7f · house A: Sol FINDINGS: 2 · findings: 8 · dropped: 0 · held: 7 · fixed: 7 · held unfixed: 0 · open: 1 · house B: Grok FINDINGS: 1 · suites: offline 4036/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 184393
  - guard-d2-1009: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/guard-d2-1009` → `8c6b5f7f`; code tip `8c6b5f7f`
  - stop-guard-g7-1009: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/stop-guard-g7-check-2026-10-09.md` last line: CHECK DONE · job: stop-guard-g7-1009 · pass: 1 · tip: c8a31812 · house A: Sol FINDINGS: 4 · findings: 11 · dropped: 0 · held: 4 · fixed: 4 · held unfixed: 0 · open: 2 · house B: Grok FINDINGS: 2 · suites: offline 4036/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 160632
  - stop-guard-g7-1009: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/stop-guard-g7-1009` → `c8a31812`; code tip `c8a31812`
  - written by deploy-card.sh at 2026-10-09 12:51 ET (`date`); trial merge of the heads onto main in order: clean

DEPLOYED deploy-2026-10-09-guard-d2-g7 ed4652f4 | set: none | migrations: none | gate: offline 4036/0 · with-DB 4923/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 0 · for Dejan: 0 · tokens: 206502
