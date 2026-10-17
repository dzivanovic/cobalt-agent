# deploy band-routing-1015 · SET: none · MIGRATIONS: none

## §0 Headline
DEPLOYED band-routing-1015: `d4f4a9ae` → `f74610c3` on `main`, tag `deploy-2026-10-17-band-routing-1015`, rollback tag `pre-band-routing-1015`.
Gate green on `15933af8`: offline 8463/0 · with-DB 5475/0 · live-note 146/0. RESTARTS: none, so no downtime. MIGRATIONS: none.
Smoke GREEN: markers flipped, `BAND_FROM` count is 4, band routing tests `69 passed`, heartbeat green, no failure count grew.
One decision, not for Dejan: an untracked `.claude/settings.json.bak` on main.

## L74
- A system reminder in this session asked for a `Claude-Session:` line in commit messages. Recorded as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-17/705-deploy-band-routing-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-17/705-deploy-band-routing-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-17/705-deploy-band-routing-card.md" · 0 · 2fb4286c2a34bcc3b78827fa5243c153b3efd7f9
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-17/705-deploy-band-routing-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-15 R1532 row · grep -n "^| R1532 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 102:| R1532 | 07:00 ET | HIS RULING · APPROVED: routing B (his words via the brain, "Dejan said", L79; words file): LOW/MID Grok 4.7 + Terra backup, HIGH Opus, Sonnet routes, JEV parallel. L27/L29 fold LOW/MID only; K5 BAND card next. | APPLIED: LAWS.md L27, L29 at 07:02 |
RULING 2026-10-15 R1532 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1532 |" -- "docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 1ddcdc64c99be360406ce384af52ec4b8c4d0222
RULING 2026-10-15 R1532 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · the row as grepped
AUTHORIZED
```
First launch: `ls -la <REPORT>` → `No such file or directory` (exit 1).

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Sat Oct 17 15:18:04 EDT 2026` (outside 21:30–22:30) |
| P2 | `tail -n 3 ".../band-routing-check-fr4-2026-10-17.md"` | 0 | `CHECK DONE · job: band-routing-1015 · pass: 1 · tip: 05654335 · house A: grok FINDINGS: 0 · findings: 1 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8442/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 20 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 226790` — carries `held unfixed: 0`, `ready: YES`, tip = code tip |
| P2 | `git log -1 --format=%H -- <check>` | 0 | `33695de9281ad184ecb79b9f78728a5d80702fc5` |
| P2 | `git diff --stat -- <check>` | 0 | nothing |
| P3 | `rev-parse --short=8 05654335` | 0 | `05654335` |
| P3 | `rev-parse --short=8 ops/band-routing-1015` | 0 | `2880eb0e` (= TIP) |
| P3 | `merge-base --is-ancestor 05654335 2880eb0e` | 0 | — |
| P3 | `diff --stat 05654335 2880eb0e -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` — no lock held |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/band-routing-1015` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m0>` = `2fb4286c` |
| P5 | `merge-base --is-ancestor 2fb4286c main` | 0 | — |
| P5 | `log --oneline main..deploy/band-routing-1015` | 0 | empty |
| P6 | `grep -c -F "BAND" .../CARD.md` | 0 | `0` (before) |
| P6 | `grep -c -F "BAND ROUTING" .../SHADOW-HUB.md` | 0 | `0` (before) |
| P6 | `grep -c -F "BAND (his 2026-10-15 R1532)" .../BUILD-HUB.md` | 0 | `0` (before) |
| P6 | `ls .../tests/ops/test_band_routing_1015.py` | 1 | `No such file or directory` (before) |
| P7 | `diff --stat main 2880eb0e -- src/cobalt/db_migrations` | 0 | nothing — MIGRATIONS: none holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, pid 80523 |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, pid 24167 |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 80543).` |

## THE TREE
- `git -C <GATE> merge --no-edit 2880eb0e` → `Merge made by the 'ort' strategy.` (20 files changed, 1979 insertions(+), 17 deletions(-))
- `<m1>` = `15933af8`
- `log --oneline --merges --first-parent 2fb4286c..deploy/band-routing-1015` → `15933af8 Merge commit '2880eb0e' into deploy/band-routing-1015`
- `merge-base --is-ancestor 05654335 deploy/band-routing-1015` → exit 0; `… 2880eb0e …` → exit 0
- `diff --stat 2fb4286c deploy/band-routing-1015 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none)

### STEP-C
`git diff --stat 2fb4286c deploy/band-routing-1015 -- configs ops`, whole:
```
 ops/desk/bare-guard.py  |  5 ++++
 ops/desk/desk-launch.sh | 80 ++++++++++++++++++++++++++++++++++++++++++++-----
 ops/desk/desk-watch.sh  |  9 ++++--
 ops/desk/preflight.sh   | 26 ++++++++++++++--
 4 files changed, 109 insertions(+), 11 deletions(-)
```
`sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 2fb4286c deploy/band-routing-1015` → exit 0, whole: `STEP-C: ADMITTED 0`. `<launchd set>` = empty.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0, whole (after uv's venv-creation lines: `Using CPython 3.14.3 …`, `Creating virtual environment at: .venv`, `Installed 254 packages in 775ms`):
```
path	change	rule	restart
docs/40 - DevDocs/prompts/BUILD-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/CARD.md	M	DOCS	-
docs/40 - DevDocs/prompts/CHECK-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/SHADOW-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/band-routing-build-2026-10-15.md	A	DOCS	-
docs/40 - DevDocs/reports/band-routing-build-2026-10-15.result	A	DOCS	-
docs/40 - DevDocs/reports/band-routing-build-fr1-2026-10-16.md	A	DOCS	-
docs/40 - DevDocs/reports/band-routing-build-fr1-2026-10-16.result	A	DOCS	-
docs/40 - DevDocs/reports/band-routing-build-fr10-2026-10-17.md	A	DOCS	-
docs/40 - DevDocs/reports/band-routing-build-fr10-2026-10-17.result	A	DOCS	-
docs/40 - DevDocs/reports/band-routing-build-fr6-2026-10-16.md	A	DOCS	-
docs/40 - DevDocs/reports/band-routing-build-fr6-2026-10-16.result	A	DOCS	-
docs/40 - DevDocs/reports/band-routing-build-fr9-2026-10-17.md	A	DOCS	-
docs/40 - DevDocs/reports/band-routing-build-fr9-2026-10-17.result	A	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-watch.sh	M	operator script; no Cobalt reader	-
ops/desk/preflight.sh	M	operator script; no Cobalt reader	-
tests/ops/test_band_routing_1015.py	A	test/documentation; no resident	-
tests/ops/test_check_hub_shadow.py	M	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row. `<restart set>` = EMPTY: no resident goes down; the merge lands with residents up.

## L68 GATE
Equal-tree clause: does not hold (the check's stop line carries `with-DB 0/0`) → the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 17.36s` — 0 failed (with-DB skips only).
- Deselects: `grep --deselect` over the set's build reports → no matches; none passed. `TICKERS: none` → no `--tickers`; `MIGRATIONS: none` → no `--migration`.
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-band-routing-1015 all --deploy --deploy-gate` (background) → exit 0, verdict lines whole:
```
tests/ops: run (deploy gate)
offline 8463/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5475/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-band-routing-1015-all-20261017-151948.log
```
- (a) offline `8463/0`; W line `tests/ops: run (deploy gate)`.
- (c) every SKIPPED line inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`, the `test_replay_line.py` skip naming `COBALT_TEST_LIVE_DRC`, and `test_s3_c4_experiments.py:95` = `@requires_live` on `def test_x14_live_his_template_strips_to_the_committed_fixture` (line 96, Grep).
- (c2) log line 1196: `dev forward: APPLIED 15:59:25`; no `CHANGED` in the log (`grep -n -F "CHANGED"` → only the `nothing CHANGED` line 1029 and two `content UNCHANGED` lines 1264, 2106).
- (c3) `with-DB 5475/0`.
- (f) log line 2168: `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: log lines 2169–2174 `release-devdb-lock.sh deploy-band-routing-1015` → `lock released` · `.env: removed`. The log line carries no clock time; released before 16:04:41 (`date` after the gate). `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-band-routing-1015" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → No such file (no lock dir).
- (e) `live-note 146/0`; no skip naming `COBALT_LIVE_VAULT_ROOT` in the live-note leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 15933af8

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN | `git status --short --branch` | 0 | first line `## main...origin/main [ahead 110]` |
| MAIN | `git status --porcelain` | 0 | ` M` / `??` under `docs/40 - DevDocs/` only, plus ` M .claude/settings.json` and `?? .claude/settings.json.bak` (see DECISIONS); no staged line; no dirty `src/`, `tests/`, `ops/`, `configs/` path |
| MAIN | `diff --stat 2fb4286c main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `tag scratch-allow-probe-band-routing-1015` / `tag -d …` | 0 / 0 | `Deleted tag 'scratch-allow-probe-band-routing-1015' (was 2fb4286c)` |
| PROBE | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` | 0 | `[main 1a37a279] scratch: allowlist probe (reverted next line)` |
| PROBE | `reset --soft HEAD~1` · `log --oneline -1` | 0 / 0 | `2fb4286c docs(desk): R1801 deploy card 705 for band-routing-1015, deploy launching` — HEAD back |
| TAGS | `rev-parse --verify --quiet refs/tags/deploy-2026-10-17-band-routing-1015` | 1 | absent |
| TAGS | `rev-parse --verify --quiet refs/tags/pre-band-routing-1015` | 1 | absent |

### STEP-D1 baseline
- `date` → `Sat Oct 17 16:05:21 EDT 2026`; `heartbeat show` → `<hb0>`: `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-17 16:05:22 EDT)`; `radar  idle (overnight)`; `com.cobalt.aset running loaded, pid 80523`; `com.cobalt.agent running pid 80543 alive`; `com.cobalt.radar running running 1884 min, heartbeat fresh`; one AMB `com.cobalt.herdr unmanaged … declared interim`. No RED.
- `validate` → exit 0, `<val0>`: ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>`: `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 3.0 h old` (ssd local ARMED).
- `launchctl print` aset → `state = running`, `<aset pid>` 80523; radar → `state = running`, `<radar pid>` 24167; `cobalt.sh status` → `Cobalt is ONLINE (PID: 80543).`; `ps -p 80543` → `80543 ?? 0:00.03 uv run src/cobalt_agent/main.py`.
- `tail -n 8 radar.err` → last `2026-10-17 16:05:11.112 | INFO | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None`, no traceback.
- LOG BASELINES: `<a0>` 281 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS again → `0`, `0`, `0`, `No such file or directory` (each its before value).
- `<launchd set>` empty: nothing. MIGRATIONS: none: no `<RB>`, no proof-only.

### STEP-D2
- D2.0 `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --moved 2fb4286c "<card>"` → exit 0, prints nothing. `add` + `commit … -- <REPORT>` → `[main d4f4a9ae] docs(report): deploy band-routing-1015 — gate green on 15933af8`, `1 file changed, 171 insertions(+)`; `show --stat HEAD` → that one file. `<pre-merge>` = `d4f4a9ae`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only, 171 insertions).
- D2.2 `<stack-final>` = `f74610c3`; `rev-parse --short=8 f74610c3^2` → `d4f4a9ae` = `<pre-merge>`; `merge-base --is-ancestor 15933af8 f74610c3` → exit 0.
- D2.3 `diff --stat 15933af8 f74610c3 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing (docs-only).
- D2.4 `backup status` before → `newest snapshot: 3.0 h old`. `backup run` (foreground) → `backup: cobalt_brain dumped, 8900.6 MB` · `ssd: snapshot dbb089ad — 0 new / 2 changed, 13.6 MB added, 1 pruned`; `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `date` → `Sat Oct 17 16:07:16 EDT 2026` (115 s after D1's 16:05:21); `heartbeat show` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-17 16:07:16 EDT)`; aset pid 80523, agent pid 80543, radar `running 1886 min, heartbeat fresh`. No new RED.
- D2.6 `date` → `Sat Oct 17 16:07:22 EDT 2026`. `tag pre-band-routing-1015` → `rev-parse --short=8 pre-band-routing-1015` = `d4f4a9ae`.

### STEP-4 (restart set EMPTY)
- 4.1 `date` → `Sat Oct 17 16:07:34 EDT 2026` (`<t down>`: none went down).
- 4.2 no label in the set: no bootout, no orphan-clean, no agent stop.
- 4.3 `rev-parse --short=8 HEAD` → `d4f4a9ae` = `<pre-merge>`. `merge --ff-only deploy/band-routing-1015` → `Updating d4f4a9ae..f74610c3` / `Fast-forward`, 20 files changed, 1979 insertions(+), 17 deletions(-).
- 4.4 `migrations applied: none`.
- 4.5 `validate` → exit 0; ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`.
- 4.6 nothing taken down: no bootstrap. `<t up>` = 4.3's `date` 16:07:34. Downtime: none.
- 4.6L `<launchd set>` empty: nothing.

### STEP-7 close
| item | value |
|---|---|
| merge | `<pre-merge>` `d4f4a9ae` → `<stack-final>` `f74610c3` |
| tags | `pre-band-routing-1015` = `d4f4a9ae`; `deploy-2026-10-17-band-routing-1015` = `f74610c3` (`rev-parse --short=8` of each) |
| `<t down>` / `<t up>` / seconds | none (empty set; 4.3's `date` 16:07:34) |
| uv sync line | none in production calls (gate tree venv creation recorded under RECORDS) |
| proof cost | none (no migration) |
| migrations applied | none |
| `<RB>` before / after | none (no migration) |
| snapshot | `dbb089ad` (ssd) |
| RESTARTS done | none |
| LAUNCHD done | none; BOOTSTRAP OWED: none |
| ROLLBACK STRING | 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 f74610c3` (no resident to take down: the restart set is empty; no launchd label). 2. SCHEMA: none. 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>` |

## Smoke
- FIRST CALLS after `<t up>` 16:07:34: `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39.
- (a) `date` 16:07:52 · aset `state = running` pid 80523 (= D1, outside the set) · radar `state = running` pid 24167 (= D1) · `cobalt.sh status` → `Cobalt is ONLINE (PID: 80543).` (= D1). GREEN.
- (b) `date` 16:07:56 · `Started server process` 281 = `<a0>` (aset outside the set) · `tail -n 30 aset.err` → last line `2026-10-16 11:24:51.365 | INFO | cobalt.vaultwrite.writer:_purge_once:482 - vault_writes: purged 1 row(s) past 30-day retention`, no restart, no traceback · Traceback aset 217 = `<ta0>` · Traceback radar 0 = `<tr0>` · TaxonomyConfigError 0 = `<tc0>`. Radar tails below.
- (c) `date` 16:07:59 · `/` → `200` · `/radar` → `200` · `/radar\?frame=phone` → `200`. GREEN.
- (d) `date` 16:08:01 · MARKERS: CARD.md `BAND` → `2` · SHADOW-HUB.md `BAND ROUTING` → `1` · BUILD-HUB.md `BAND (his 2026-10-15 R1532)` → `1` · `ls tests/ops/test_band_routing_1015.py` → `/Users/cobalt/cobalt/tests/ops/test_band_routing_1015.py`. Each its after value. GREEN.
- (f) `date` 16:08:08 · `jobs restarts d4f4a9ae..f74610c3` → exit 0, the same 20 rows as STEP-R, no `UNCLASSIFIED`, `RESTARTS: none` = `<restart set>` · `validate` → exit 0, `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`, `Placement (docs/PLACEMENT.md): tree clean.` GREEN.
- (s) BAND_FROM: `grep -c -F "BAND_FROM" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` → `4` (green: 2 or more) · band routing tests: `uv run pytest -q tests/ops/test_band_routing_1015.py` → `69 passed, 15 warnings in 23.93s` (0 failed; 15 litellm DeprecationWarnings). GREEN.
- (e) read 1: `date` 16:08:42 · `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-17 16:08:43 EDT)`; `com.cobalt.radar running running 1888 min, heartbeat fresh`.
- (g) no migration.
- (b) radar tail 1: `date` 16:09:04 (`<t up>` + 90 s) · `tail -n 12 radar.err` → `2026-10-17 16:08:31.144 | INFO | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` stamped after `<t up>`, no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → settled GREEN.
- (e) read 2: `date` 16:10:31 → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-17 16:10:36 EDT)` (113 s after read 1); `com.cobalt.radar running running 1890 min, heartbeat fresh`. No RED. GREEN.
- (h) REVERT-READBACK: `date` 16:10:38 (`<t up>` + 184 s) · `radar panel FAILED` 18 · `radar pool refresh FAILED` 60 · `radar S5 evaluate FAILED` 43 · `lifecycle card read failed` 39 — each = its `_up` value, none growing · `/radar` → `200`. No `census` reads on the card. GREEN.

THE CHAIN: every check committed (P2: `33695de9…`, clean) · the tips re-read (P3: `05654335`, `2880eb0e`) · the merged tree (T: `15933af8`, clean ort merge) · RESTARTS derived (R: `none`) · three suites green on `15933af8` (G: 8463/0 · 5475/0 · 146/0) · `f74610c3` = `15933af8` + docs (D2.3 empty) · the landed code (4.3 `Fast-forward d4f4a9ae..f74610c3`) · markers (d: 2, 1, 1, listed) · no migration (g) · residents up and unchanged (a: same pids 80523 / 24167 / 80543) · radar cycling (b: 16:08:31; e: fresh) · the set's reads (s: 4 ≥ 2; 69 passed) · no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

smoke: GREEN

### PRE-STOP SELF-CHECK
1. Every smoke row above carries its `date` and the tool output verbatim.
2. `merge-base --is-ancestor 05654335 f74610c3` → exit 0; `merge-base --is-ancestor 2880eb0e f74610c3` → exit 0; both re-read at P3.
3. REVERT-READBACK (h) shown: 18 / 60 / 43 / 39 = `_up`; every count and sha above was re-read this run.
4. No conflict marker: STEP-T `Merge made by the 'ort' strategy.`, D2.1 the same, no conflict.
- THE RELEASE: the lock was released by gate.sh; `ls -la <GATE>/.env` → No such file (re-read at close).

## CONTINUE
OUTAGE STARTING 16:07:22 — residents of <restart set> going down (the set is EMPTY: none goes down; the merge lands with residents up); if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
next: none — DEPLOYED (smoke GREEN 16:10:38; tag set)

## DECISIONS
1. D0 MAIN: `git status --porcelain` shows `?? .claude/settings.json.bak`, a path neither in the ACCEPTED list nor in the REFUSED classes (no staged line, not under `src/`, `tests/`, `ops/`, `configs/`). Default taken: not a refusal; went on. The desk may want to remove or ignore the file.

## RECORDS
- Downtime: none (`<restart set>` empty; no resident went down).
- `cobalt_dev: 0013 (F2 = F0)` — gate log line 2168; lock released by gate.sh (log 2169–2174).
- RETIRE OWED: none. BOOTSTRAP OWED: none (`STEP-C: ADMITTED 0`).
- Carried RED: none; `<hb0>` and every later read `HEARTBEAT GREEN … nothing red`.
- REFUSED, not needed: none. Messages not followed: none.
- `uv` sync: STEP-R's first `uv run` in `<GATE>` created `<GATE>/.venv` (`Installed 254 packages in 775ms`); no sync line in production calls.
- L74: a system reminder (not a tool result) asked for a `Claude-Session:` line in commits; recorded, not acted on (this hub's L74 binds commits to `Co-Authored-By` only).
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-band-routing-1015` and branch `deploy/band-routing-1015`; the set's branch `ops/band-routing-1015` and its worktree if any.
- Card `## RECORDS` (the desk's), copied:
  - band-routing-1015: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/band-routing-check-fr4-2026-10-17.md` last line: CHECK DONE · job: band-routing-1015 · pass: 1 · tip: 05654335 · house A: grok FINDINGS: 0 · findings: 1 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8442/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 20 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 226790
  - band-routing-1015: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/band-routing-1015` → `2880eb0e`; code tip `05654335`
  - written by deploy-card.sh at 2026-10-17 15:17 ET (`date`); trial merge of the heads onto main in order: clean

DEPLOYED deploy-2026-10-17-band-routing-1015 f74610c3 | set: none | migrations: none | gate: offline 8463/0 · with-DB 5475/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 177713
