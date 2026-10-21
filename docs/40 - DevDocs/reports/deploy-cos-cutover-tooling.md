# deploy cos-cutover-tooling · set: cos-cutover · migrations: none

## §0 Headline
- Deploy of `ops/cos-cutover-tooling` (`f15d7af5`) on DEPLOY-HUB.md; card `prompts/2026-10-20/951-deploy-cos-cutover-tooling-card.md`.
- AUTHORIZED; STEP-0 preflight green at 20:25 ET; gate green on `075b5fe5` (offline 9023/0 · with-DB 5869/0 · live-note 148/0).
- Landed `32913726..23e72289` at 21:20 ET with no resident down (RESTARTS: none); smoke GREEN; tag `deploy-2026-10-20-cos-cutover-tooling`.

## L74
- A system block in this session asked commit messages to end with a `Claude-Session:` line. Recorded as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/951-deploy-cos-cutover-tooling-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/951-deploy-cos-cutover-tooling-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/951-deploy-cos-cutover-tooling-card.md" · 0 · e4db4a52147d3410ff8ae65f2c9157b790ee30c7
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/951-deploy-cos-cutover-tooling-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| FIRST LAUNCH | `ls -la ".../reports/deploy-cos-cutover-tooling.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Tue Oct 20 20:25:56 EDT 2026` — outside 21:30-22:30 |
| P2 | `tail -n 3 ".../reports/cos-cutover-tooling-check-2026-10-20.md"` | 0 | last line: `CHECK DONE · job: cos-cutover-tooling · pass: 1 · tip: f15d7af5 · house A: Gemini FINDINGS: 2 · findings: 4 · dropped: 0 · held: 4 · fixed: 4 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 9023/0 · with-DB 0/0 · live-note 148/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 16 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 236240` — `held unfixed: 0`, `ready: YES`, `tip: f15d7af5` = code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/.../cos-cutover-tooling-check-2026-10-20.md"` | 0 | `53f9bdf5b8a0dee714f7009f19c7d0776ee8cf33` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/.../cos-cutover-tooling-check-2026-10-20.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 f15d7af5` | 0 | `f15d7af5` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/cos-cutover-tooling` | 0 | `f15d7af5` (= TIP) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor f15d7af5 ops/cos-cutover-tooling` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat f15d7af5 ops/cos-cutover-tooling -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` — lock free |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/cos-cutover-tooling` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m0>` = `e4db4a52` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor e4db4a52 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/cos-cutover-tooling` | 0 | empty |
| P6 | `grep -c -F "card 931 T2" .../ops/desk/desk-launch.sh` | 1 | `0` (before) |
| P6 | `grep -c -F "is retired; a retired label is never restarted" .../ops/desk/deploy-outage.sh` | 1 | `0` (before) |
| P6 | `grep -c -F "retired (recorded)" .../ops/desk/deploy-step0.sh` | 1 | `0` (before) |
| P6 | `grep -c -F "com.cobalt.agent recorded retired" ".../prompts/DEPLOY-HUB.md"` | 1 | `0` (before) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main f15d7af5 -- src/cobalt/db_migrations` | 0 | nothing — MIGRATIONS: none holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 77363` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 22089` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 35845).` |

## THE TREE
| check | command | exit | result |
|---|---|---|---|
| merge | `git -C <GATE> merge --no-edit f15d7af5` | 0 | `Merge made by the 'ort' strategy.` (10 files, 817 insertions, 20 deletions) |
| `<m1>` | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `075b5fe5` |
| merges | `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent e4db4a52..deploy/cos-cutover-tooling` | 0 | `075b5fe5 Merge commit 'f15d7af5' into deploy/cos-cutover-tooling` |
| ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor f15d7af5 deploy/cos-cutover-tooling` | 0 | — |
| migrations | `git -C /Users/cobalt/cobalt diff --stat e4db4a52 deploy/cos-cutover-tooling -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| STEP-C | `git -C /Users/cobalt/cobalt diff --stat e4db4a52 deploy/cos-cutover-tooling -- configs ops` | 0 | `ops/desk/deploy-outage.sh \| 27`, `ops/desk/deploy-step0.sh \| 15`, `ops/desk/desk-launch.sh \| 48` — `3 files changed, 78 insertions(+), 12 deletions(-)` |
| STEP-C | `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" e4db4a52 deploy/cos-cutover-tooling` | 0 | `STEP-C: ADMITTED 0` |

## RESTARTS
`COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` (from `<GATE>`, `.env` absent) → exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/cos-cutover-tooling-build-2026-10-20.md	A	DOCS	-
docs/40 - DevDocs/reports/cos-cutover-tooling-build-2026-10-20.result	A	DOCS	-
docs/40 - DevDocs/reports/cto-2026-10-20.md	M	DOCS	-
ops/desk/deploy-outage.sh	M	operator script; no Cobalt reader	-
ops/desk/deploy-step0.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_deploy_outage.py	M	test/documentation; no resident	-
tests/ops/test_deploy_step0.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_bootstrap_only.py	A	test/documentation; no resident	-
tests/ops/test_hub_agent_retired_1020.py	A	test/documentation; no resident	-
RESTARTS: none
```
(uv created the gate's `.venv` first: `Installed 257 packages in 952ms`.)
- `<restart set>`: EMPTY — no resident goes down. `<deferred set>`: empty. `<launchd set>`: empty.

## L68 GATE
- (a0) `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `265 passed, 163 skipped in 19.39s` (0 failed; the skips are with-DB tests, `.env` absent).
- EQUAL-TREE CLAUSE: not applied — the check's stop line carries `with-DB 0/0`; the gate runs whole (`--deploy`).
- No `--deselect` (the build report names none for pass 1), no `--tickers` (TICKERS: none), no `--migration`.
- `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-cos-cutover-tooling all --deploy --deploy-gate` → exit 0, verdict lines whole:
```
tests/ops: run (deploy gate)
offline 9023/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5869/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_checkpoints_live.py:36: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live checkpoint dry run
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 148/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-cos-cutover-tooling-all-20261020-202745.log
```
- (a) `offline 9023/0`; W line `tests/ops: run (deploy gate)`. (c) every SKIPPED line inside the allowed set (test and reason as listed in STEP-G (c)). (c2) no forward (MIGRATIONS: none). (c3) `with-DB 5869/0`. (f) log line 1048 `F0: 664 35 272c95bbb12241e3611e4b36326ccf87`, line 2330 `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` → `cobalt_dev: 0013 — F2 = F0`. (e) `live-note 148/0`.
- THE RELEASE: log line 2386 `lock released`; `.env: removed (L76 lock released; gate end read at 21:16:58 EDT by date)`; `ls -la <GATE>/.env` → No such file; `.cobalt_dev.lock/owner` → No such file.

GATE GREEN on 075b5fe5

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| cwd back | `ls -la /Users/cobalt/cobalt/.env` | 0 | listed |
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 271]` |
| MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | no staged line; ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, ` M`/`??` under `docs/40 - DevDocs/`, and ` M "docs/30 - Design/archiver-runs.md"` (see DECISIONS); no dirty `src/`, `tests/`, `ops/`, other `configs/` path |
| MAIN | `git -C /Users/cobalt/cobalt diff --stat e4db4a52 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `tag scratch-allow-probe-cos-cutover-tooling` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-cos-cutover-tooling' (was acb38cdc)` |
| PROBE | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 65eadbb5] …` → `acb38cdc docs(desk): R2251-R2252 card 958 option C, amend drafter prompt 959` (HEAD back) |
| TAG | `rev-parse --verify --quiet refs/tags/deploy-2026-10-20-cos-cutover-tooling` | 1 | free |
| TAG | `rev-parse --verify --quiet refs/tags/pre-cos-cutover-tooling` | 1 | free |

### STEP-D1 baseline
| read | result |
|---|---|
| `date` | `Tue Oct 20 21:17:28 EDT 2026` |
| `<hb0>` heartbeat | `HEARTBEAT RED — 3 job(s) and 1 probe(s)  (2026-10-20 21:17:29 EDT)`; OK database, sheet HTTP (`-> 200`), sheet daymode, `radar idle (overnight)`, `com.cobalt.aset running pid 77363`, `com.cobalt.agent running pid 35845`, `com.cobalt.radar running 237 min, heartbeat fresh`, `com.cobalt.cos disabled … NOT LOADED BY DESIGN`; RED (named, not a stop — not the aset / sheet / radar probe): `archiver last run FAILED — last run 2026-10-21 00:54 UTC (0.4 h ago), rows written 3373447, exit 1`, `com.cobalt.archiver failed RuntimeError: 5 archiver failure(s): WBD/i1: … Finviz HTTP failed: Client error '400 Bad Request'`, `com.cobalt.replay failed ReplayError: archiver not done: state 'failed'`, `com.cobalt.generated failed GeneratedCommitRefused: … a deploy hub is live — no desk commit on main until its stop line: 79a459de deploy-hub-hub-cos-restart-fr1`; AMB `com.cobalt.herdr unmanaged`; OWED (deferred bootstrap): prefill-refresh, checkpoint-0715/0745/0815/0845, playbook |
| `<val0>` validate | exit 0; ends `Placement (docs/PLACEMENT.md): tree clean.` |
| `<jobs0>` | `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.` · `NOT LOADED BY DESIGN (1): com.cobalt.cos` |
| backup status | `newest snapshot: 4.0 h old` (ssd ARMED) |
| aset | `state = running`, `pid = 77363` |
| radar | `state = running`, `pid = 22089` |
| agent | `Cobalt is ONLINE (PID: 35845).`; `ps -p 35845` → `35845 ?? 0:00.03 uv run src/cobalt_agent/main.py` |
| radar.err tail 8 | last `2026-10-20 21:16:19.437 … radar cycle: idle:overnight scan_id=None`, no traceback |
| counts | `<a0>` 289 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39 |
| `/radar` curl | `200` |
| MARKERS | `0` · `0` · `0` · `0` (each its `before`) |
| LAUNCHD SET | empty — nothing |
| MIGRATION | none — `<RB>`, census and D1-M not run |

### STEP-D2
| step | command | exit | result |
|---|---|---|---|
| D2.0 | `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --moved e4db4a52 "<card>"` | 0 | nothing |
| D2.0 | `add` + `commit … -- "docs/40 - DevDocs/reports/deploy-cos-cutover-tooling.md"` | 0 | `[main 32913726] docs(report): deploy cos-cutover-tooling — gate green on 075b5fe5`; `show --stat HEAD` → that one file |
| D2.0 | `git -C /Users/cobalt/cobalt rev-parse --short=8 main` | 0 | `<pre-merge>` = `32913726` |
| D2.1 | `git -C <GATE> merge --no-edit main` | 0 | `Merge made by the 'ort' strategy.` (24 files, all under `docs/`) |
| D2.2 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<stack-final>` = `23e72289` |
| D2.2 | `git -C /Users/cobalt/cobalt rev-parse --short=8 deploy/cos-cutover-tooling^2` | 0 | `32913726` = `<pre-merge>` |
| D2.2 | `merge-base --is-ancestor 075b5fe5 deploy/cos-cutover-tooling` | 0 | — |
| D2.3 | `git -C /Users/cobalt/cobalt diff --stat 075b5fe5 deploy/cos-cutover-tooling -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing — docs only |
| D2.4 | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 4.0 h old` |
| D2.4 | `COBALT_ENV=production uv run cobalt backup run` (21:18:26 start) | 0 | `backup: cobalt_brain via pg_dump inside cobalt_memory — 9799.9 MB` · `ssd: snapshot a5c85b30 — 0 new / 3 changed, 1379.1 MB added, 1 pruned` |
| D2.4 | `backup status` | 0 | `newest snapshot: 0.0 h old` |
| D2.5 | `date` · heartbeat | 0 | `Tue Oct 20 21:19:43 EDT 2026` (135 s after D1's 21:17:29); `HEARTBEAT RED — 3 job(s) and 1 probe(s)` — the same REDs as `<hb0>` (archiver, com.cobalt.archiver, com.cobalt.replay, com.cobalt.generated); aset `running pid 77363`, radar `running 239 min, heartbeat fresh`, `backup newest snapshot 0.0 h old` — no new RED |
| D2.6 | `date` | 0 | `Tue Oct 20 21:19:50 EDT 2026` |
| D2.6 | `git -C /Users/cobalt/cobalt tag pre-cos-cutover-tooling` | 0 | at `32913726` |

### STEP-4 (`<restart set>` EMPTY: no resident down)
| step | command | exit | result |
|---|---|---|---|
| 4.1 | `date` | 0 | `<t down>` `Tue Oct 20 21:20:05 EDT 2026` |
| 4.2 | — | — | nothing (empty set; no bootout, no orphan-clean, no agent stop) |
| 4.3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` | 0 | `32913726` = `<pre-merge>` |
| 4.3 | `git -C /Users/cobalt/cobalt merge --ff-only deploy/cos-cutover-tooling` | 0 | `Updating 32913726..23e72289` / `Fast-forward` (10 files, 817 insertions, 20 deletions) |
| 4.4 | — | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | 0 | ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 22 registered — 7 resident, 15 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>` |
| 4.6 | — | — | nothing to bootstrap; `<t up>` = 4.1's `date` 21:20:05 (no read between it and the merge); downtime: none |
| 4.6L | — | — | `<launchd set>` empty: `LAUNCHD done: none` |

## Smoke
| row | `date` | command | result |
|---|---|---|---|
| first | 21:20:12 | the four failure counts | `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 (= D1) |
| (a) | 21:20:17 | `launchctl print` aset / radar · `cobalt.sh status` | aset `state = running`, `pid = 77363` (SAME as D1: outside the set) · radar `state = running`, `pid = 22089` (SAME) · `Cobalt is ONLINE (PID: 35845).` (same pid) |
| (b) | 21:20:17 | `grep -c` counts | `Started server process` 289 = `<a0>` (aset outside the set) · aset `Traceback` 217 = `<ta0>` · radar `Traceback` 0 = `<tr0>` · `TaxonomyConfigError` 0 = `<tc0>` |
| (b) | 21:20:17 | `tail -n 30 /Users/cobalt/cobalt/logs/aset.err` | last line stamped `2026-10-20 10:32:51` (a daily-note write); no new start, no traceback since D1 (content is vault data, not copied here) |
| (c) | 21:20:17 | three curls | `/` `200` · `/radar` `200` · `/radar\?frame=phone` `200` |
| (d) | 21:20:17 | `## MARKERS` | `1` · `1` · `1` · `8` — each its `after` |
| (f) | 21:20:17 | `jobs restarts 32913726..23e72289` | exit 0, `RESTARTS: none` = `<restart set>`, no `UNCLASSIFIED` |
| (f) | 21:20:12 | validate (4.5) | exit 0, `<jobs0>` unchanged |
| (g) | — | — | no migration |
| (s) | — | `## SMOKE READS` | its one line is a note on the marker counts (line counts via `grep -c -F`), read by (d); `<launchd set>` empty — no dry run |
| (e) 1 | 21:20:35 | heartbeat | `HEARTBEAT RED — 3 job(s) and 1 probe(s)  (2026-10-20 21:20:36 EDT)` — the same REDs as `<hb0>`; `com.cobalt.radar running 240 min, heartbeat fresh`; no new RED |
| (b) tail 1 | 21:21:40 (`<t up>` + 95 s) | `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` | last `2026-10-20 21:21:19.502 … radar cycle: idle:overnight scan_id=None` — a cycle after `<t up>`, no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → GREEN (settled) |
| (e) 2 | 21:22:26 | heartbeat | `HEARTBEAT RED — 3 job(s) and 1 probe(s)  (2026-10-20 21:22:29 EDT)` (113 s after (e) 1) — the same REDs as `<hb0>`; `com.cobalt.radar running 242 min, heartbeat fresh`; no new RED |
| (h) | 21:23:05 (`<t up>` + 180 s) | the four counts · `/radar` curl · radar tail | 18 · 60 · 43 · 39 = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (no growth) · `200` · last `2026-10-20 21:22:59.522 … radar cycle: idle:overnight scan_id=None`; census: none on the card |

THE CHAIN: every check committed (P2 `53f9bdf5`) · the tips re-read (P3 `f15d7af5`) · the merged tree `075b5fe5` (T) · RESTARTS derived `none` (R) · three suites green on `075b5fe5` — offline 9023/0, with-DB 5869/0, live-note 148/0 (G) · `<stack-final>` `23e72289` = `<m1>` + docs (D2.3) · the landed code `32913726..23e72289` fast-forward (4.3) · markers 1/1/1/8 (d) · no migration (g) · residents up, same pids, nothing restarted (a) · radar cycling at 21:21:19 and 21:22:59 (b, e) · the set's reads (s) · no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

**smoke: GREEN**

PRE-STOP SELF-CHECK: (1) every smoke row above is quoted with its `date`; (2) `f15d7af5` re-read at P3 and `merge-base --is-ancestor f15d7af5 23e72289` → exit 0; (3) REVERT-READBACK shown in (h); every count and sha above re-read from this run's tool output; (4) STEP-T ran clean (`Merge made by the 'ort' strategy.`), no conflict marker.

### STEP-7 close
| item | value |
|---|---|
| `<pre-merge>` → `<stack-final>` | `32913726` → `23e72289` |
| tags | `pre-cos-cutover-tooling` at `32913726` · `deploy-2026-10-20-cos-cutover-tooling` at `23e72289` |
| `<t down>` / `<t up>` / seconds | none (empty `<restart set>`) |
| uv sync line | gate `.venv` created at STEP-R: `Installed 257 packages in 952ms`; none in production |
| proof cost | none (no migration); the gate's dev proof-only: `Proof cost: total 5.5 s` |
| migrations applied | none |
| `<RB>` before / after | none |
| snapshot id | `a5c85b30` (ssd) |
| RESTARTS done | none |
| LAUNCHD done | none; BOOTSTRAP OWED: none from this run |
| ROLLBACK STRING | 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 23e72289` (no resident to take down: `<restart set>` empty; no `<launchd set>` label). 2. SCHEMA: none. 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>` |

## CONTINUE
- next: STEP-D2 (gate green at 21:16 ET; D0, D1 done)
- OUTAGE STARTING 21:19:50 EDT — residents of <restart set> (EMPTY: none) going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
- 4.6 ended 21:20:12 (nothing down); smoke GREEN 21:23:05; STEP-7 done

## DECISIONS
- ASK DESK: `git status --porcelain` on `main` shows ` M "docs/30 - Design/archiver-runs.md"` — a dirty docs path outside `docs/40 - DevDocs/`, neither in D0's ACCEPTED list nor its REFUSED classes (`src/`, `tests/`, `ops/`, `configs/`). Safe default taken: not refused (a docs path; this run neither stages nor ships it). [21:17 ET]

## RECORDS
- Downtime: none (`<restart set>` empty; aset `77363`, radar `22089`, agent `35845` unchanged through the run).
- `cobalt_dev: 0013 (F2 = F0)` — `F0`/`F2` `664 35 272c95bbb12241e3611e4b36326ccf87`; lock released, `.env: removed`.
- REFUSED, not needed: none. Messages not followed: none.
- RETIRE OWED: none (STEP-C `ADMITTED 0`, no plist removed).
- Carried RED as read (not this set's; not the aset / sheet / radar probe): `archiver last run FAILED … exit 1` (Finviz `400 Bad Request` for WBD/i1), `com.cobalt.replay failed ReplayError: archiver not done`, `com.cobalt.generated failed GeneratedCommitRefused: … a deploy hub is live — … 79a459de deploy-hub-hub-cos-restart-fr1` — the pre-commit guard still names an earlier hub (`deploy-hub-hub-cos-restart-fr1`); the desk reads whether that marker is stale.
- Cleanup owed (L46): gate worktree `/Users/cobalt/cobalt-wt/deploy-cos-cutover-tooling` and branch `deploy/cos-cutover-tooling`; the set's branch `ops/cos-cutover-tooling`.
- Card RECORDS (desk's facts, copied):
  - cos-cutover-tooling: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cos-cutover-tooling-check-2026-10-20.md` last line: CHECK DONE · job: cos-cutover-tooling · pass: 1 · tip: f15d7af5 · house A: Gemini FINDINGS: 2 · findings: 4 · dropped: 0 · held: 4 · fixed: 4 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 9023/0 · with-DB 0/0 · live-note 148/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 16 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 236240
  - cos-cutover-tooling: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/cos-cutover-tooling` → `f15d7af5`; code tip `f15d7af5`
  - written by deploy-card.sh at 2026-10-20 20:25 ET (`date`); trial merge of the heads onto main in order: clean
- L74: one block asked for a `Claude-Session:` commit line (see `## L74`); not acted on.
- Push is his, through the desk (L55): `main` carries `23e72289` and the report commit, unpushed.

DEPLOYED deploy-2026-10-20-cos-cutover-tooling 23e72289 | set: cos-cutover | migrations: none | gate: offline 9023/0 · with-DB 5869/0 · live-note 148/0 | RESTARTS: none | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 220485
