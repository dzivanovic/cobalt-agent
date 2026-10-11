# install-shadow-hub-1011 — deploy report (SET: none · MIGRATIONS: none)

## §0 Headline
Landed at 14:46:45 ET: `main` moved `00b753fb..182e896d` by fast-forward. SHADOW-HUB.md line 1 is now `INSTALL: 2026-10-11 R1069 · HIS RULING · APPROVED`, and SPIKE-HUB.md is signed. The desk launchers no longer refuse SHADOW-HUB.
Gate green on `5fccf989`: offline 4199/0 · with-DB 5096/0 · live-note 146/0. `cobalt_dev` is back at 0013 (F2 = F0) and the lock is released.
RESTARTS: none, so no resident went down and there was no downtime. Smoke GREEN. Snapshot `e7c1685d`. Tags `pre-install-shadow-hub-1011` (00b753fb) and `deploy-2026-10-11-install-shadow-hub` (182e896d).
The check's one held finding, O1, was fixed in the fix round (`FIXED: O1`); no carried defect ships.

## L74
One system message in this session asked for a `Claude-Session:` line on commits. Recorded here, not followed: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/363-deploy-install-shadow-hub-card.md"` → exit 0, quoted whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/363-deploy-install-shadow-hub-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-11/363-deploy-install-shadow-hub-card.md" · 0 · 360ecd56b82dba31fa2d9d9836ac87502ade536d
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-11/363-deploy-install-shadow-hub-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1069 row · grep -n "^| R1069 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 28:| R1069 | 10:37 ET | HIS RULING · APPROVED (via the brain, L79; words R1069): OpenAI available, tribunal seats approved, no stops, no design round; deploy 324, install SHADOW-HUB, Grok, Sonnet, Terra arms in parallel (only the lock serializes). | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1069 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1069 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 2322ed1e5044b6ec734e2cd0d225252408f87dbd
RULING 2026-10-11 R1069 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| FIRST LAUNCH | `ls -la "<REPORT>"` | 1 | No such file or directory |
| P0 | authorize.sh (above) | 0 | AUTHORIZED |
| P1 DATE | `date` | 0 | Sun Oct 11 14:13:10 EDT 2026 |
| P2 check last line | `tail -n 3 ".../install-shadow-hub-check-2026-10-11.md"` | 0 | `CHECK DONE · job: install-shadow-hub-1011 · pass: 1 · tip: f6d698ab · … · held: 1 · fixed: 0 · held unfixed: 1 · open: 1 · … · ready: NO · decisions: 3 · for Dejan: 1 · tokens: 193760` — carries `held unfixed: 1` and `ready: NO` as the row names |
| P2 check committed | `git log -1 --format=%H -- "<check>"` | 0 | b1753ba202487698a1e72141e21d31b33a992be4 |
| P2 check clean | `git diff --stat -- "<check>"` | 0 | nothing |
| P2 fix-round: check tip ancestor | `git merge-base --is-ancestor f6d698ab d4ec4fe3` | 0 | — |
| P2 fix report committed (branch head) | `git log -1 --format=%H 8c5ce590 -- "<fix report>"` | 0 | 8c5ce590ffd176fc7863e9eab13fa957df79d817 |
| P2 fix report clean | `git diff --stat -- "<fix report>"` | 0 | nothing |
| P2 fix report last line | `git show 8c5ce590:"<fix report>"` (line 211) | 0 | `BUILT · job: install-shadow-hub-1011 · tip: d4ec4fe3 \| on 2322ed1e \| migration: none \| offline 4199/0 \| with-DB 0/0 \| live-note 146/0 \| … \| decisions: 0 · for Dejan: 0 · tokens: 124052` |
| P2 held ids | check `HELD, NOT FIXED` | — | O1 only; fix report line 209: `FIXED: O1 — tests/ops/test_authorize.py::test_check_o1_the_real_shadow_title_names_its_standing_row` |
| P2 FIXED test at code tip | `git show d4ec4fe3:tests/ops/test_authorize.py` | 0 | `def test_check_o1_the_real_shadow_title_names_its_standing_row(desk):` present, no xfail mark |
| P3 code tip | `git rev-parse --short=8 d4ec4fe3` | 0 | d4ec4fe3 |
| P3 branch head | `git rev-parse --short=8 ops/install-shadow-hub-1011` | 0 | 8c5ce590 (= TIP) |
| P3 ancestor | `git merge-base --is-ancestor d4ec4fe3 8c5ce590` | 0 | — |
| P3 head adds docs only | `git diff --stat d4ec4fe3 8c5ce590 -- . ':(exclude)docs'` | 0 | nothing |
| P4 LOCK | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` — lock free |
| P5 gate status | `git -C <GATE> status --short --branch` | 0 | `## deploy/install-shadow-hub-1011` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m0>` = 360ecd56 |
| P5 m0 on main | `git merge-base --is-ancestor 360ecd56 main` | 0 | — |
| P5 gate holds nothing | `git log --oneline main..deploy/install-shadow-hub-1011` | 0 | empty |
| P6 marker 1 | `grep -c -F -e "INSTALL: 2026-10-11 R1069 · HIS RULING · APPROVED" SHADOW-HUB.md` | 1 | 0 (= before) |
| P6 marker 2 | `grep -c -F -e "NEEDS HIS SIGN-OFF" SHADOW-HUB.md` | 0 | 3 (= before) |
| P7 migrations | `git diff --stat main 8c5ce590 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, pid 7760 |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, pid 61093 |
| P8 aset plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 8c5ce590` → `Merge made by the 'ort' strategy.` (7 files: SHADOW-HUB.md, SPIKE-HUB.md, the build report, four `tests/ops/` files; 302 insertions, 11 deletions).
- `<m1>` = `git -C <GATE> rev-parse --short=8 HEAD` → `5fccf989`.
- `git log --oneline --merges --first-parent 360ecd56..deploy/install-shadow-hub-1011` → `5fccf989 Merge commit '8c5ce590' into deploy/install-shadow-hub-1011` (one line, one head).
- `merge-base --is-ancestor d4ec4fe3 deploy/install-shadow-hub-1011` → 0 · `… 8c5ce590 …` → 0.
- `git diff --stat 360ecd56 deploy/install-shadow-hub-1011 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git diff --stat 360ecd56 deploy/install-shadow-hub-1011 -- configs ops` → nothing. No plist added, changed or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (after `uv` created the gate's `.venv`: `Installed 253 packages in 816ms`):
```
path	change	rule	restart
docs/40 - DevDocs/prompts/SHADOW-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/SPIKE-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/install-shadow-hub-build-2026-10-11.md	A	DOCS	-
tests/ops/test_authorize.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_shadow.py	M	test/documentation; no resident	-
tests/ops/test_shadow_hub_file.py	M	test/documentation; no resident	-
tests/ops/test_spike_hub_file.py	M	test/documentation; no resident	-
RESTARTS: none
```
`<restart set>` = none (EMPTY): no resident goes down; the merge lands with the residents up.

## L68 GATE
- EQUAL-TREE CLAUSE: does not hold — the check's stop line carries `with-DB 0/0` (not above 0) → the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 16.72s` (0 failed; the skips are with-DB `Postgres env settings not available` / `requires_db`).
- Deselects: none (the set's build report names no with-DB deselect). TICKERS: none. `--migration`: none.
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-install-shadow-hub-1011 all --deploy` (background) → exit 0, verdict lines whole:
```
offline 4199/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5096/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-install-shadow-hub-1011-all-20261011-141452.log
```
- (a) offline 4199/0 → `<p>` = 4199.
- (c) every SKIPPED line inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_replay_line.py` (`COBALT_TEST_LIVE_DRC`), `test_s3_c4_experiments.py:95` = the skip of `test_x14_live_his_template_strips_to_the_committed_fixture` (its `def` at `:96` in `<GATE>`), `test_catalyst.py:365`, `test_predicate.py:262`.
- (c2) log `:1110` `dev forward: APPLIED 14:38:58`; `grep CHANGED` in the log → only `nothing CHANGED` / `content UNCHANGED` lines (`:948`, `:1178`, `:2020`).
- (c3) with-DB 5096/0 → `<d>` = 5096.
- (f) log `:896` `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` · `:2030` `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` · `:2082` `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: log `:2083–2087` `release-devdb-lock.sh deploy-install-shadow-hub-1011` → `lock released`, `.env` No such file. `.env: removed (L76 lock released, after dev forward 14:38:58, before 14:44:08)`. `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-install-shadow-hub-1011" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → No such file (lock dir absent).
- (e) live-note 146/0 → `<l>` = 146; no skip names `COBALT_LIVE_VAULT_ROOT` in the live-note leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 5fccf989

## Deploy table
### STEP-D0
| rule | command | exit | result |
|---|---|---|---|
| MAIN branch | `git status --short --branch` | 0 | `## main...origin/main [ahead 189]` |
| MAIN porcelain | `git status --porcelain` | 0 | ` M .claude/settings.json`; ` M` / `??` under `docs/40 - DevDocs/` only; plus `?? .claude/settings.json.bak` (untracked, not under `src/` `tests/` `ops/` `configs/`, not staged — accepted, recorded); no staged line |
| MAIN moved | `git diff --stat 360ecd56 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE tag | `git tag scratch-allow-probe-install-shadow-hub-1011` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-install-shadow-hub-1011' (was 360ecd56)` |
| PROBE commit | `git commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 10a8b6e0] …` · — · `360ecd56 docs(desk): R1090 card 361 DEPLOYED, deploy card 363 for 355` |
| TAG | `rev-parse --verify --quiet refs/tags/deploy-2026-10-11-install-shadow-hub` | 1 | absent |
| TAG | `rev-parse --verify --quiet refs/tags/pre-install-shadow-hub-1011` | 1 | absent |

### STEP-D1 (14:44:35 EDT)
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-11 14:44:36 EDT)`. aset / sheet probes OK (`sheet HTTP http://127.0.0.1:5010/ -> 200`, `com.cobalt.aset running loaded, pid 7760`); radar OK (`radar idle (overnight)`, `com.cobalt.radar running 1875 min, heartbeat fresh`). REDs, named, not a stop: `RED archiver last run FAILED — last run 2026-10-10 00:54 UTC (41.8 h ago), rows written 3308843, exit 1` · `RED com.cobalt.archiver failed RuntimeError: 18 archiver failure(s): DKNG/i2: … Finviz HTTP failed: Client error '429 Too Many Requests' …` · `RED com.cobalt.replay failed ReplayError: archiver not done: state 'failed'`. `AMB com.cobalt.herdr unmanaged`.
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; no `docs/_inflight/` line. `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 0.6 h old` (ssd local ARMED).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` = 7760 · `…com.cobalt.radar` → `state = running`, `<radar pid>` = 61093 · `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ?? 0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 radar.err` → eight `radar cycle: idle:overnight scan_id=None` lines, 14:31:48 → 14:43:28, no traceback.
- LOG BASELINES: `<a0>` 277 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS: marker 1 → `0`, marker 2 → `3` (= before).
- No migration: `<RB>`, census and D1-M not run.

### STEP-D2
- D2.0 `git add` + `git commit … -- "docs/40 - DevDocs/reports/deploy-install-shadow-hub-1011.md"` → `[main 00b753fb] docs(report): deploy install-shadow-hub-1011 — gate green on 5fccf989`; `show --stat HEAD` → that one file (148 insertions). `<pre-merge>` = `git rev-parse --short=8 main` → `00b753fb`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `<stack-final>` = `182e896d`; `rev-parse --short=8 182e896d^2` → `00b753fb` (= `<pre-merge>`); `merge-base --is-ancestor 5fccf989 182e896d` → 0.
- D2.3 `git diff --stat 5fccf989 182e896d -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- D2.4 `backup status` → `newest snapshot: 0.6 h old` · `backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 6693.0 MB` · `ssd: snapshot e7c1685d — 0 new / 1 changed, 16.6 MB added, 1 pruned` · `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 14:46:28 `date`, `heartbeat show` → `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-11 14:46:29 EDT)` — 113 s after D1's 14:44:36; the same three REDs as `<hb0>` (archiver probe, `com.cobalt.archiver`, `com.cobalt.replay`), aset / sheet / radar OK, `com.cobalt.radar running 1877 min, heartbeat fresh`. No new RED.
- D2.6 `date` → `Sun Oct 11 14:46:34 EDT 2026`; `git tag pre-install-shadow-hub-1011` at `00b753fb` → exit 0.

### STEP-4 (`<restart set>` = none)
- 4.1 `date` → `<t down>` = 14:46:45 EDT.
- 4.2 none: no bootout, no `cobalt.sh stop` (empty set).
- 4.3 `git rev-parse --short=8 HEAD` → `00b753fb` (= `<pre-merge>`) · `git merge --ff-only deploy/install-shadow-hub-1011` → `Updating 00b753fb..182e896d` / `Fast-forward` (7 files, 302 insertions, 11 deletions).
- 4.4 `migrations applied: none`.
- 4.5 `validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`.
- 4.6 none: no bootstrap. `<t up>` = `date` 14:46:53 EDT. Downtime: none (no resident went down).
- Smoke first calls: `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39.

### STEP-7 — the close
| item | value |
|---|---|
| landed | `<pre-merge>` 00b753fb → `<stack-final>` 182e896d (`git rev-parse --short=8 main` → 182e896d) |
| tags | `pre-install-shadow-hub-1011` → 00b753fb · `deploy-2026-10-11-install-shadow-hub` → 182e896d (set after the green smoke) |
| outage | `<t down>` 14:46:45 / `<t up>` 14:46:53 / 0 s of resident downtime: none (RESTARTS: none, nothing went down) |
| uv sync | none in production; gate `.venv` created at STEP-R (`Installed 253 packages in 816ms`) |
| proof cost | n/a (no production migration; dev proof-only in the gate log) |
| migrations applied | none |
| `<RB>` before / after | n/a (MIGRATIONS: none) |
| snapshot | `e7c1685d` (ssd; cobalt_brain dump 6693.0 MB) |
| RESTARTS done | none |

THE ROLLBACK STRING (the desk's; never this session's):
1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 182e896d`. That is ONE revert of the main-into-gate merge, and it carries the set's merge with it. `<restart set>` is none, so no resident goes down.
2. SCHEMA: none (no migration).
3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`. Git titles it `Reapply "Merge branch 'main' into deploy/install-shadow-hub-1011"`.

PRE-STOP SELF-CHECK:
1. Every smoke row is quoted verbatim with its `date`: (a) 14:47:02, (b) 14:47:05 / tails 14:48:25 and 14:49:53, (c) 14:47:09, (d)(s) 14:47:11, (f) 14:47:19, (e) 14:47:22 and 14:49:14, (h) 14:49:56. YES.
2. The code tip and head were re-read at P3 and are ancestors of `<stack-final>`: `merge-base --is-ancestor d4ec4fe3 182e896d` → 0 and `… 8c5ce590 182e896d` → 0. YES.
3. REVERT-READBACK is shown in (h): the four counts equal the `_up` values, read at 14:49:56. Every count, sha and `file:line` in this report was re-read from tool output in this run. YES.
4. No conflict marker exists: STEP-T and D2.1 each printed `Merge made by the 'ort' strategy.` with no conflict. YES.

## Smoke
`<t up>` = 14:46:53 EDT (empty set; no resident restarted).
- (a) 14:47:02 · `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 7760` (SAME as D1, outside the set) · `…com.cobalt.radar` → `state = running`, `pid = 61093` (SAME) · `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` (same pid). GREEN.
- (b) 14:47:05 · `grep -c "Started server process" aset.err` → 277 (= `<a0>`, aset outside the set) · Traceback aset.err 217 (= `<ta0>`) · Traceback radar.err 0 (= `<tr0>`) · TaxonomyConfigError radar.err 0 (= `<tc0>`). Radar tails: below.
- (c) 14:47:09 · `/` → `200` · `/radar` → `200` · `/radar\?frame=phone` → `200`. GREEN.
- (d) 14:47:11 · marker 1 → `1` (after `1`; `grep -n` → `1:INSTALL: 2026-10-11 R1069 · HIS RULING · APPROVED`, line 1) · marker 2 → `0` (after `0`). GREEN.
- (s) 14:47:11 · SHADOW-HUB signed: `grep -c -F -e "2026-10-11 R1069 · HIS RULING · APPROVED" SHADOW-HUB.md` → `4` (green: 4) · SPIKE-HUB signed: `grep -c -F -e "NEEDS HIS SIGN-OFF" SPIKE-HUB.md` → `0` (green: 0). GREEN. The suites that test these files ran in the gate (offline 4199/0).
- (f) 14:47:19 · `validate` → exit 0, `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` (= `<jobs0>`), `Placement (docs/PLACEMENT.md): tree clean.` · `jobs restarts 00b753fb..182e896d` → exit 0, the same seven DOCS / test rows, `RESTARTS: none` (= STEP-R), no `UNCLASSIFIED`. GREEN.
- (e) read 1, 14:47:22 · `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-11 14:47:22 EDT)` — the same three REDs as `<hb0>` (archiver probe, `com.cobalt.archiver` 429, `com.cobalt.replay`); `com.cobalt.radar running 1878 min, heartbeat fresh`.
- (e) read 2, 14:49:14 `date` · `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-11 14:49:16 EDT)` — 114 s after read 1; the same three REDs, none new; `com.cobalt.radar running 1880 min, heartbeat fresh`. GREEN.
- (b) radar tail 1, 14:48:25 `date` (`<t up>` + 92 s) · `tail -n 12 radar.err` → last line `2026-10-11 14:46:48.567 | INFO | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` — before `<t up>`; not settled, no traceback, no FAILED line.
- (b) radar tail 2, 14:49:53 `date` (`<t up>` + 180 s) · `tail -n 12 radar.err` → last line `2026-10-11 14:48:28.597 | INFO | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None`. That cycle line is stamped after `<t up>`, with no `radar S5 evaluate FAILED`, no `lifecycle card read failed` and no traceback in the tail, so (b) settles GREEN; no third tail is needed.
- (g) no migration.
- (h) 14:49:56 (`<t up>` + 183 s, after (b) settled) · `<rp>` 18 = `<rp_up>` · `<rpr>` 60 = `<rpr_up>` · `<re>` 43 = `<re_up>` · `<lc>` 39 = `<lc_up>`. No count grew. `/radar` → `200`. No census reads (no migration). GREEN.

THE CHAIN: every check committed (P2: check `b1753ba2`, fix report at `8c5ce590`, `FIXED: O1`) · the tips re-read (P3: `d4ec4fe3`, `8c5ce590`) · the merged tree (T: `<m1>` 5fccf989, one merge) · RESTARTS derived (R: none) · three suites green on `<m1>` (G: offline 4199/0, with-DB 5096/0, live-note 146/0) · `<stack-final>` 182e896d = `<m1>` + docs (D2.3: empty diff) · the landed code (4.3: `Updating 00b753fb..182e896d`, Fast-forward) · markers (d: 1 / 0) · no migration (g) · residents up after the merge with unchanged pids (a) · radar cycling (b: 14:48:28; e: heartbeat fresh) · the set's reads (s: 4 / 0) · no new failure (h). This run cannot read the card surface; the desk confirms it with him (L70).

## CONTINUE
OUTAGE STARTING 14:46:34 — residents of none going down (RESTARTS: none: no resident goes down; the merge lands with the residents up); if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
4.6 ended at 14:46:53 with no resident down; the smoke was green at 14:49:56; STEP-7 closed. next: none — the run is ended.

## DECISIONS
none

## RECORDS
- REFUSED, not needed: `grep -n -F ".env" <gate log>` — `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: .env is never read; `ls -la <path>/.env` shows it is there, and the lock scripts copy and remove it`. Read the release from `grep -n -F "lock released"` and the log lines instead.
- Downtime: none; no resident went down (RESTARTS: none).
- `cobalt_dev: 0013 (F2 = F0)`. The L76 lock was released by `gate.sh` (log `:2082–2087`), and `<GATE>/.env` is absent at the close.
- RETIRE OWED: none (no plist was removed).
- Carried RED as read: the heartbeat REDs at D1, D2.5 and smoke (e) were `archiver` (last run FAILED 2026-10-10 00:54 UTC, Finviz `429 Too Many Requests`) and `com.cobalt.replay` (`archiver not done: state 'failed'`). None of them is on the aset, sheet or radar probe, and this deploy did not cause them. They are recorded here as baseline and are not a stop.
- `?? .claude/settings.json.bak` is untracked on `main` (outside `src/` `tests/` `ops/` `configs/`, not staged). D0 accepted it; the desk's.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-install-shadow-hub-1011` with branch `deploy/install-shadow-hub-1011`, and the set's branch `ops/install-shadow-hub-1011` with its build worktree.
- L74: one system message in this session asked for a `Claude-Session:` line on commits. It was not followed (see `## L74`).
- Card RECORDS (the desk's, copied):
  - install-shadow-hub-1011: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/install-shadow-hub-build-2026-10-11.md` at `8c5ce590` last line: BUILT · job: install-shadow-hub-1011 · tip: d4ec4fe3 | on 2322ed1e | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 124052
  - install-shadow-hub-1011: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/install-shadow-hub-check-2026-10-11.md` last line: CHECK DONE · job: install-shadow-hub-1011 · pass: 1 · tip: f6d698ab · house A: Grok FINDINGS: 1 · findings: 8 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 1 · house B: none available · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 16 · ready: NO · decisions: 3 · for Dejan: 1 · tokens: 193760
  - install-shadow-hub-1011: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/install-shadow-hub-1011` → `8c5ce590`; code tip `d4ec4fe3`
  - written by deploy-card.sh at 2026-10-11 14:12 ET (`date`); trial merge of the heads onto main in order: clean

DEPLOYED deploy-2026-10-11-install-shadow-hub 182e896d | set: none | migrations: none | gate: offline 4199/0 · with-DB 5096/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 0 · for Dejan: 0 · tokens: 233202
