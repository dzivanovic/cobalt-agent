# deploy aset-orphan-1010 · SET: none · MIGRATIONS: none

## §0 Headline
- Deploy of `ops/aset-orphan-1010` (code tip `1987849b`, head `f72dbb9a`) on DEPLOY-HUB, card `prompts/2026-10-10/256-deploy-aset-orphan-card.md`.

## L74
- A system block arrived after launch asking that commits end with a `Claude-Session: https://claude.ai/code/session_0187rTUxLezEi6Suvs8DLAH7` line. Recorded as DATA (L74); not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/256-deploy-aset-orphan-card.md"` · exit 0 · output WHOLE:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/256-deploy-aset-orphan-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/256-deploy-aset-orphan-card.md" · 0 · a0a7a214acf0f6a1deccbc38bd9723e255a05733
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/256-deploy-aset-orphan-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Sat Oct 10 12:32:07 EDT 2026` |
| P0 first launch | `ls -la ".../reports/deploy-aset-orphan-1010.md"` | 1 | `No such file or directory` |
| P2 | `tail -n 3 ".../reports/aset-orphan-check-2026-10-10.md"` | 0 | `CHECK DONE · job: aset-orphan-1010 · pass: 1 · tip: 1987849b · … · held unfixed: 0 · … · RESTARTS: com.cobalt.aset · files opened: 13 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 163668` — carries `held unfixed: 0`, `ready: YES`; tip `1987849b` = row's code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/aset-orphan-check-2026-10-10.md"` | 0 | `af0b107247fcba531187d2d4b8eec553a6187f4b` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/…/aset-orphan-check-2026-10-10.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 1987849b` | 0 | `1987849b` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/aset-orphan-1010` | 0 | `f72dbb9a` (= TIP) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 1987849b f72dbb9a` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 1987849b f72dbb9a -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/aset-orphan-1010` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `e98055b1` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor e98055b1 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/aset-orphan-1010` | 0 | empty |
| P6 | `grep -c -F 'exec "$REPO_ROOT/.venv/bin/python" -m cobalt.aset' /Users/cobalt/cobalt/ops/start_aset.sh` | 1 | `0` (= before) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main f72dbb9a -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none holds) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 66658` · `runs = 120` · `last exit code = 3` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 61093` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit f72dbb9a` → `Merge made by the 'ort' strategy.` (5 files: `aset-orphan-build-2026-10-10.md`, `ops/README.md`, `ops/start_aset.sh`, `tests/cobalt/test_jobs_reads.py`, `tests/ops/test_launchd_orphan.py`).
- `git -C <GATE> rev-parse --short=8 HEAD` → `4aee2f68` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent e98055b1..deploy/aset-orphan-1010` → `4aee2f68 Merge commit 'f72dbb9a' into deploy/aset-orphan-1010` (one line, one head).
- `merge-base --is-ancestor 1987849b deploy/aset-orphan-1010` → exit 0; `merge-base --is-ancestor f72dbb9a deploy/aset-orphan-1010` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat e98055b1 deploy/aset-orphan-1010 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat e98055b1 deploy/aset-orphan-1010 -- configs ops` →
```
 ops/README.md     |  2 +-
 ops/start_aset.sh | 17 +++++++++++------
 2 files changed, 12 insertions(+), 7 deletions(-)
```
  No plist added, modified or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created `.venv` in the gate: `Installed 253 packages in 815ms`):
```
path	change	rule	restart
docs/40 - DevDocs/reports/aset-orphan-build-2026-10-10.md	A	DOCS	-
ops/README.md	M	operations documentation; no resident	-
ops/start_aset.sh	M	resident reads	com.cobalt.aset
tests/cobalt/test_jobs_reads.py	M	test/documentation; no resident	-
tests/ops/test_launchd_orphan.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.aset
```
No UNCLASSIFIED row. `<restart set>` = `com.cobalt.aset`.

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 1987849b 4aee2f68 -- . ":(exclude)docs"` → `ops/desk/bare-guard.py | 12`, `tests/ops/test_bare_guard.py | 62` (main moved since the check) → does NOT hold; the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 16.83s` (0 failed; every skip a with-DB skip: `Postgres env settings not available` / `requires_db`).
- Deselects: the build report (`aset-orphan-build-2026-10-10.md:155`) names none added by this build ("no `--deselect`: this build adds no with-DB test"). No `--tickers` (TICKERS: none), no `--migration`.
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-aset-orphan-1010 all --deploy` launched in the background (task `bvk66x54y`) → exit 0. Verdict lines WHOLE:
```
offline 4196/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5093/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-aset-orphan-1010-all-20261010-123350.log
```
- (a) offline 4196/0 · (c) pass 1: every SKIPPED line inside the allowed set — `test_s3_c4_experiments.py:95` is the decorator of `test_x14_live_his_template_strips_to_the_committed_fixture` (`grep -n -F` → `96:def test_x14_…`) · (c2) `dev forward: APPLIED 12:58:00` (log:1110) · (c3) with-DB 5093/0 · (f) `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log:896), `cobalt_dev: 0013 — F2 = F0` (log:2082) · RELEASE `lock released` (log:2084), `.env: removed (L76 lock released)`; `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-aset-orphan-1010" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → No such file · (e) live-note 146/0.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 4aee2f68

## Deploy table
### STEP-D0
| rule | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 206]` |
| MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`; ` M`/`??` under `docs/40 - DevDocs/` only; plus `?? .claude/settings.json.bak` (not staged, not under src/tests/ops/configs). No staged line |
| MAIN | `git -C /Users/cobalt/cobalt diff --stat e98055b1 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `tag scratch-allow-probe-aset-orphan-1010` / `tag -d …` | 0 / 0 | `Deleted tag 'scratch-allow-probe-aset-orphan-1010' (was e98055b1)` |
| PROBE | `commit --allow-empty -m "scratch: …"` / `reset --soft HEAD~1` / `log --oneline -1` | 0 / 0 / 0 | `[main 8689a347] scratch: allowlist probe (reverted next line)` → `e98055b1 docs(desk): OWED live ids point at the running X29 check` |
| TAGS | `rev-parse --verify --quiet refs/tags/deploy-2026-10-10-aset-orphan` | 1 | free |
| TAGS | `rev-parse --verify --quiet refs/tags/pre-aset-orphan-1010` | 1 | free |

### STEP-D1 (baseline)
- `date` → `Sat Oct 10 13:03:30 EDT 2026` · `COBALT_ENV=production uv run cobalt heartbeat show` → `<hb0>`: `HEARTBEAT RED — 2 job(s) and 1 probe(s) (2026-10-10 13:03:31 EDT)`; OK: database, sheet HTTP (`http://127.0.0.1:5010/ -> 200`), sheet daymode, obsidian, mainframe, herdr, seat usage, backup, vault blocks, redactions, `radar idle (overnight)`, `com.cobalt.aset running loaded, pid 66658`, `com.cobalt.agent running pid 22243`, `com.cobalt.radar running running 334 min, heartbeat fresh`; AMB `com.cobalt.herdr unmanaged`; RED `archiver last run FAILED — last run 2026-10-10 00:54 UTC (16.2 h ago), rows written 3308843, exit 1`; RED `com.cobalt.archiver failed RuntimeError: 18 archiver failure(s): DKNG/i2: … Finviz HTTP failed: Client error '429 Too Many Requests' …`; RED `com.cobalt.replay failed ReplayError: archiver not done: state 'failed'`. None on the aset / sheet / radar probe: named, not a stop.
- `COBALT_ENV=production uv run cobalt validate` → exit 0 (`<val0>`: 13 trade_defs OK, … `Placement (docs/PLACEMENT.md): tree clean.`); `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 1.7 h old` (ssd ARMED; b2 off).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` = `66658` · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `<radar pid>` = `61093` · `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ?? 0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → 8 lines `radar cycle: idle:overnight scan_id=None`, last `2026-10-10 13:03:05.054`.
- LOG BASELINES: `<a0>` 182 · `<ta0>` 123 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKER `grep -c -F 'exec "$REPO_ROOT/.venv/bin/python" -m cobalt.aset' …/ops/start_aset.sh` → `0` (before).
- MIGRATIONS: none → no `<RB>`, no census, no D1-M.

### STEP-D2
- D2.0 `git -C /Users/cobalt/cobalt commit … -- "docs/40 - DevDocs/reports/deploy-aset-orphan-1010.md"` → `[main 8199fa13] docs(report): deploy aset-orphan-1010 — gate green on 4aee2f68`; `show --stat HEAD` → the one file (139 +). `rev-parse --short=8 main` → `8199fa13` = `<pre-merge>`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `<stack-final>` = `a617c402`; `rev-parse --short=8 a617c402^2` → `8199fa13` = `<pre-merge>`; `merge-base --is-ancestor 4aee2f68 a617c402` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat 4aee2f68 a617c402 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- D2.4 `backup status` → `newest snapshot: 1.7 h old` · `COBALT_ENV=production uv run cobalt backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 6694.0 MB` · `ssd: snapshot 75137484 — 0 new / 1 changed, 27.0 MB added, 1 pruned` · `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `date` 13:05:04 / heartbeat 13:05:04 (93 s — under 110), clock filled with date + heartbeat pairs (13:05:08/10, 13:05:14/16), `date` `Sat Oct 10 13:05:19 EDT 2026` → `heartbeat show` `(2026-10-10 13:05:21 EDT)` = 110 s after `<hb0>` 13:03:31: same three REDs as `<hb0>` (archiver, com.cobalt.archiver 429, com.cobalt.replay); aset `pid 66658`, radar `running 336 min, heartbeat fresh`. No new RED.
- D2.6 `date` → `Sat Oct 10 13:05:26 EDT 2026` · `git -C /Users/cobalt/cobalt tag pre-aset-orphan-1010` → exit 0 (at `8199fa13`).

### STEP-4 (outage) — ended at 4.2
- 4.1 `date` → `Sat Oct 10 13:05:37 EDT 2026` = `<t down>`.
- 4.2 `launchctl bootout gui/501/com.cobalt.aset` → exit 0, no output · `launchctl print gui/501/com.cobalt.aset` → still loaded, `state = SIGTERMed`, `pid = 66658` · `date` → `13:05:41` · print again → still `state = SIGTERMed`, `pid = 66658` → STEP-5 (nothing merged).
- 4.3–4.6 NOT RUN. `main` never moved: no merge, no migration.

### STEP-5
- (0) `date` → `Sat Oct 10 13:05:47 EDT 2026`.
- (1) `launchctl print gui/501/com.cobalt.aset` → exit 113 `Could not find service "com.cobalt.aset" in domain for user gui: 501` (gone by now; no further bootout) · `ps -p 66658` → header only. Counts `<rp5>` 18 · `<rpr5>` 60 · `<re5>` 43 · `<lc5>` 39.
- (2) `git -C /Users/cobalt/cobalt log --oneline -1` → `8199fa13 docs(report): deploy aset-orphan-1010 — gate green on 4aee2f68` = `<pre-merge>`: 4.3 never merged → NO revert.
- (3) `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` → exit 0 · print → `state = spawn scheduled`, `runs = 1`, `last exit code = 3` (loaded, not running) · `launchctl kickstart -k gui/501/com.cobalt.aset` → exit 0 · print → `state = spawn scheduled`, `runs = 3`, `last exit code = 3`. STILL NOT RUNNING; the one kickstart is spent.
- CAUSE, from `tail -n 30 /Users/cobalt/cobalt/logs/aset.err`: `cobalt.voice.scratch.ScratchLocked: voice scratch dir /Users/cobalt/.cobalt/voice-scratch is locked by pid 66667 — the start sweep deleted NOTHING. A process still owns this directory (X-X22: an orphan can outlive its job); find it and stop it before this process may serve voice turns.` → `ERROR: Application startup failed. Exiting.` · `ps -p 66667` → `66667 ?? 11:45.09 /opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/Resources/Python.app/Contents/MacOS/Python -m cobalt.aset` — the OLD aset's python child, orphaned when the bootout killed `start_aset.sh` (pid 66658) and not its child: the exact defect this set (`ops/start_aset.sh` exec) fixes. No string on this run's list stops a process.
- (4) `date` → `13:06:30` · (a) radar `state = running`, `pid = 61093` (same; not in the set) · `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` · aset: `spawn scheduled`, `runs = 5`, `last exit code = 3` — RED · (b) `Started server process` 185 (`<a0>` 182) · aset `Traceback` 126 (`<ta0>` 123: the three failed starts) · radar `tail -n 12` → `radar cycle: idle:overnight` every 100 s through `13:06:25.098`, no traceback · (c) `curl …/` → `502` · `curl …/radar` → `502` — RED · (e) `heartbeat show (13:06:34)` → `HEARTBEAT RED — 3 job(s) and 3 probe(s)`: NEW `RED sheet HTTP http://127.0.0.1:5010/ unreachable: … [Errno 61] Connection refused`, `?? sheet daymode … unreachable`, `RED com.cobalt.aset failed loaded, not running (last exit 3)`; radar `running 337 min, heartbeat fresh` · (f) `jobs restarts 8199fa13..a617c402` → exit 0, `RESTARTS: com.cobalt.aset`, no UNCLASSIFIED · (g) no migration · readback counts: `radar panel FAILED` 18 = `<rp5>`, `radar S5 evaluate FAILED` 43 = `<re5>`.
- PRODUCTION STATE AT STOP: `com.cobalt.aset` DOWN (KeepAlive respawns it and it exits 3 each time while pid 66667 lives); the sheet `/`, `/radar` serve 502; radar and agent up and unchanged; `main` = `8199fa13` (old code; nothing merged); schema untouched.

ROLLBACK STRING: not applicable — nothing merged (4.3 never ran). Tags: `pre-aset-orphan-1010` at `8199fa13` (left for the desk); `deploy-2026-10-10-aset-orphan` NOT set. Snapshot `75137484`. `<t down>` 13:05:37 · `<t up>` none (aset not restored) · migrations applied: none · RESTARTS done: none.

## Smoke
Not run: the outage ended at 4.2 → STEP-5. STEP-5 (4) reads are above under `### STEP-5`: aset RED, sheet 502, radar and agent green.

## CONTINUE
- STEP-D0 green 13:03; STEP-D1 baseline taken 13:03:30.
- STEP-D2 done 13:05:26.
- OUTAGE STARTING 13:05:26 — residents of com.cobalt.aset going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
- 13:05:41 still loaded at the second print → STEP-5. STEP-5 (3) ran and did not restore aset: orphan pid 66667 holds the voice scratch lock. Ended; nothing further from this session.

## DECISIONS
1. DECISION 0 — FOR DEJAN: production DEGRADED, the sheet is DOWN. `com.cobalt.aset` cannot start while the orphan `python -m cobalt.aset` pid 66667 lives (it holds `/Users/cobalt/.cobalt/voice-scratch`). The restore needs that pid stopped (e.g. `kill 66667`, then `launchctl kickstart -k gui/501/com.cobalt.aset`), and no approved string covers it. Safe default taken: touched nothing more; residents left as they are (radar and agent up, aset respawning and exiting 3). URGENT — the first act after this line.
2. ASK DESK: the deploy itself cannot pass 4.2 on the current tree. The OLD `start_aset.sh` (the defect this set fixes) leaves the python child alive at bootout, so every deploy of this fix leaves the same orphan. The card's own DEPLOY PROOF (`ps -p <old aset pid>` → header only) checked the shell pid 66658 and not its child. Safe default: none taken. The next attempt needs a step that stops the old child (or a hub/card change for this one-time transition) before `desk-launch.sh recut`.

## RECORDS
- Downtime: aset down from 13:05:37 and NOT restored at the stop line (over 300 s).
- No REFUSED commands. No CONTINUE messages received.
- cobalt_dev: 0013 (F2 = F0) — the gate's (log `/Users/cobalt/cobalt-wt/.gate-logs/deploy-aset-orphan-1010-all-20261010-123350.log`:2082); lock released (:2084).
- No RETIRE OWED.
- Carried REDs at `<hb0>`: `archiver last run FAILED … exit 1`; `com.cobalt.archiver failed RuntimeError: 18 archiver failure(s): … 429 Too Many Requests`; `com.cobalt.replay failed ReplayError: archiver not done: state 'failed'`. None of the aset / radar family.
- Cleanup owed (L46): gate worktree `/Users/cobalt/cobalt-wt/deploy-aset-orphan-1010` and branch `deploy/aset-orphan-1010` (at `a617c402`, uv `.venv` created there by STEP-R); tag `pre-aset-orphan-1010` at `8199fa13`; set branch `ops/aset-orphan-1010`.
- `main` status at D0 also carried `?? .claude/settings.json.bak` (outside `docs/`, untracked; not refused by D0's rule).
- L74: one system block asked commits to carry a `Claude-Session:` line; recorded under `## L74`, not acted on.
- Card `## RECORDS` (the desk's):
  - aset-orphan-1010: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/aset-orphan-check-2026-10-10.md` last line: CHECK DONE · job: aset-orphan-1010 · pass: 1 · tip: 1987849b · house A: Sol FINDINGS: 1 · findings: 10 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 3 · house B: Gemini FINDINGS: 5 · suites: offline 4196/0 · with-DB 5093/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset · files opened: 13 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 163668
  - aset-orphan-1010: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/aset-orphan-1010` → `f72dbb9a`; code tip `1987849b`
  - written by deploy-card.sh at 2026-10-10 11:29 ET (`date`); trial merge of the heads onto main in order: clean
- PRE-STOP SELF-CHECK: (1) STEP-5 (4) evidence quoted with `date` 13:06:30; (2) P3 re-read both tips, and both are ancestors of `a617c402` via `4aee2f68` (T); (3) readback counts 18 / 43 re-read this run (STEP-5 (4)); no revert existed to read back; (4) STEP-T clean, no conflict marker.

FAILED: 4.2 — com.cobalt.aset still loaded (SIGTERMed) at the second print; STEP-5 (3) could not restore it: orphan pid 66667 (python -m cobalt.aset) holds the voice scratch lock, aset exits 3 · rollback: not used — migrations applied: none — aset: DOWN — radar: not in the set · FOR DEJAN · decisions: 2 · for Dejan: 1 · tokens: 141119
