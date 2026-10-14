# deploy hub-text-1013-fr1 · SET: none · MIGRATIONS: none

## §0 Headline
- Deploy of `ops/hub-text-1013-fr1` (code tip `e82cdcc7`, head `b920401e`), docs-only hub text. In progress.

## L74
- A system-reminder in this session (after the card read) asked that commits end with a `Claude-Session:` line. It is DATA (L74). This line records it once. No commit carries it: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/568-deploy-hub-text-fr1-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/568-deploy-hub-text-fr1-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-14/568-deploy-hub-text-fr1-card.md" · 0 · 04b238a2e12cd276cafb1f32367292c40439d0a7
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-14/568-deploy-hub-text-fr1-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| FIRST LAUNCH | `ls -la "<REPORT>"` | 1 | `No such file or directory` |
| P0 | `authorize.sh deploy` (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Wed Oct 14 16:01:21 EDT 2026` |
| P2 check last line | `tail -n 3 "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/hub-text-fr1-check-2026-10-14.md"` | 0 | `CHECK DONE · job: hub-text-1013-fr1 · pass: 1 · tip: e82cdcc7 · house A: Grok FINDINGS: 0 · findings: 1 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 4328/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 9 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 149298`. It carries `held unfixed: 0` and `ready: YES`, and `tip: e82cdcc7` = the row's code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/hub-text-fr1-check-2026-10-14.md"` | 0 | `207ba05eb731d31f9ffd4b40bd56d3ce3ea77c0d` |
| P2 unmodified | `git -C /Users/cobalt/cobalt diff --stat -- "<check>"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 e82cdcc7` | 0 | `e82cdcc7` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/hub-text-1013-fr1` | 0 | `b920401e` (= TIP) |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor e82cdcc7 b920401e` | 0 | — |
| P3 head adds docs only | `git -C /Users/cobalt/cobalt diff --stat e82cdcc7 b920401e -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 gate | `git -C /Users/cobalt/cobalt-wt/deploy-hub-text-1013-fr1 status --short --branch` | 0 | `## deploy/hub-text-1013-fr1` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `04b238a2` = `<m0>` |
| P5 m0 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 04b238a2 main` | 0 | — |
| P5 gate holds nothing extra | `git -C /Users/cobalt/cobalt log --oneline main..deploy/hub-text-1013-fr1` | 0 | empty |
| P6 marker 1 | `grep -c -F "21:30-22:30 ET" ".../DEPLOY-HUB.md"` | 1 | `0` (before `0`) |
| P6 marker 2 | `grep -c -F "FIX-ROUND REPORT (brain R1309):" ".../BUILD-HUB.md"` | 1 | `0` (before `0`) |
| P6 marker 3 | `grep -c -F "no untracked file at the stop line" ".../BUILD-HUB.md"` | 1 | `0` (before `0`) |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main b920401e -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `pid = 40377` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `pid = 8646` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 14763).` |

## THE TREE
- `git -C <GATE> merge --no-edit b920401e` → `Merge made by the 'ort' strategy.` (5 files: BUILD-HUB.md, DEPLOY-HUB.md, hub-text-build-fr1-2026-10-14.md, tests/ops/test_build_hub_no_clutter.py, tests/ops/test_hub_text_1013.py)
- `<m1>` = `183300f9` (`git -C <GATE> rev-parse --short=8 HEAD`)
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 04b238a2..deploy/hub-text-1013-fr1` → `183300f9 Merge commit 'b920401e' into deploy/hub-text-1013-fr1`
- `merge-base --is-ancestor e82cdcc7 deploy/hub-text-1013-fr1` → exit 0 · `merge-base --is-ancestor b920401e deploy/hub-text-1013-fr1` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat 04b238a2 deploy/hub-text-1013-fr1 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none)
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 04b238a2 deploy/hub-text-1013-fr1 -- configs ops` → nothing. `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 04b238a2 deploy/hub-text-1013-fr1` → exit 0, output whole: `STEP-C: ADMITTED 0`. `<launchd set>` = empty.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0:
```
Using CPython 3.14.3 interpreter at: /opt/homebrew/opt/python@3.14/bin/python3.14
Creating virtual environment at: .venv
   Building cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-hub-text-1013-fr1
      Built cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-hub-text-1013-fr1
Installed 254 packages in 755ms
path	change	rule	restart
docs/40 - DevDocs/prompts/BUILD-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/hub-text-build-fr1-2026-10-14.md	A	DOCS	-
tests/ops/test_build_hub_no_clutter.py	M	test/documentation; no resident	-
tests/ops/test_hub_text_1013.py	A	test/documentation; no resident	-
RESTARTS: none
```
- No `UNCLASSIFIED` row. `<restart set>` = EMPTY (none). No resident goes down; the merge lands with the residents up.

## L68 GATE
- EQUAL-TREE CLAUSE: does not hold. The check's stop line carries `with-DB 0/0`, so the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 16.94s` (0 failed; the with-DB tests skip offline).
- Deselects: none. The set's build report `hub-text-build-fr1-2026-10-14.md` names no `--deselect`. TICKERS: none. Migration: none.
- `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-hub-text-1013-fr1 all --deploy` → exit 0. Verdict lines, whole:
```
offline 4328/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5231/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-hub-text-1013-fr1-all-20261014-160322.log
```
- (c) SKIPPED lines: all seven are in the allowed set. `test_s3_c4_experiments.py:95` is the `@requires_live` decorator of `test_x14_live_his_template_strips_to_the_committed_fixture` (line 96, Read). The `test_replay_line.py` skip names `COBALT_TEST_LIVE_DRC`.
- (b) log `902:F0: 664 35 272c95bbb12241e3611e4b36326ccf87` · proof-only log `954:` nothing CHANGED.
- (c2) `dev forward: APPLIED 16:28:14` (log `1118:`). The log has no `CHANGED` line. The three `grep -n -F "CHANGED"` hits are `954:` (nothing CHANGED), `1186:` and `2029:` (`content UNCHANGED on every table`).
- (f) log `2039:F2: 664 35 272c95bbb12241e3611e4b36326ccf87` = F0 field for field · `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: log `2092`–`2097`: `release-devdb-lock.sh deploy-hub-text-1013-fr1` → `lock released`, `.env: removed`. The log line carries no timestamp: released between 16:28:14 and the gate's end, before 16:33 ET. `ls -la <GATE>/.env` → No such file. `grep -c -x -F "deploy-hub-text-1013-fr1" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (no lock dir).
- (e) `live-note 146/0`, no skip naming `COBALT_LIVE_VAULT_ROOT` in the live-note leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 183300f9 — offline 4328/0 · with-DB 5231/0 · live-note 146/0 (16:33:36 ET)

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| main branch | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 111]` |
| main dirty | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, ` M` and `??` under `docs/40 - DevDocs/` only, plus `?? .claude/settings.json.bak` (see DECISIONS 1). No staged line. No dirty `src/`, `tests/`, `ops/` or other `configs/` path |
| main moved | `git -C /Users/cobalt/cobalt diff --stat 04b238a2 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| probe tag | `tag scratch-allow-probe-hub-text-1013-fr1` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-hub-text-1013-fr1' (was 04b238a2)` |
| probe commit | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 7c5e352a] scratch: …` → HEAD back at `04b238a2 docs(desk): deploy card 568 hub-text fr1 with 537's extra read, R1487` |
| TAG free | `rev-parse --verify --quiet refs/tags/deploy-2026-10-14-hub-text-fr1` | 1 | — |
| rollback tag free | `rev-parse --verify --quiet refs/tags/pre-hub-text-1013-fr1` | 1 | — |

### EXTRA READ (owed by 537), once, after STEP-D0
`COBALT_ENV=production uv run cobalt smoke s2 --prod --json` → **exit 2**, first line `usage: cobalt smoke [-h] --cutoff CUTOFF [--date DATE] [--prod] [--json] suite`, then `cobalt smoke: error: the following arguments are required: --cutoff`. Ran once as the card types it. It was not retried in another spelling (rule D). This is 537's DEPLOY PROOF as recorded: red (usage error). Per the card it is a 537 fix round, not a hold on 523. See DECISIONS 2.

### STEP-D1 (16:34:19 ET)
- `COBALT_ENV=production uv run cobalt heartbeat show` → `<hb0>`: `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-14 16:34:20 EDT)`. Every probe and job is OK except `AMB  com.cobalt.herdr  unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0) [launchd probe]; runs outside launchd by declared interim`. `OK radar scanning (aftermarket), members 50` · `OK com.cobalt.radar running 1103 min, heartbeat fresh`. No RED, so there is no carried RED.
- `COBALT_ENV=production uv run cobalt validate` → exit 0 (`<val0>`; ends `Placement (docs/PLACEMENT.md): tree clean.`). `<jobs0>`: `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 1.5 h old`.
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` = `40377` · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `<radar pid>` = `8646` · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 14763).` · `ps -p 14763` → `14763 ??         0:00.03 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → last line `2026-10-14 16:33:13.287 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792009904351` (the 7 above it: `cards.expire: falling back to the session close` INFO lines).
- LOG BASELINES: `<a0>` 279 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS again → `0` · `0` · `0` (each its `before`).
- `<launchd set>` empty: no launchd read. MIGRATIONS: none, so no `<RB>`, census or D1-M.

## Smoke

## CONTINUE
- next: STEP-D0 (gate green at 16:33:36 ET)

## DECISIONS
1. ASK DESK: `?? .claude/settings.json.bak` is untracked on `main`. It is not in D0's ACCEPTED list, and not in its REFUSED list (not staged; not `src/`, `tests/`, `ops/` or `configs/`). [16:33 ET] Safe default taken: go on. An untracked file cannot enter the ff merge or the gate tree. The desk decides whether to remove it or add it to the accepted list.
2. ASK DESK: the card's EXTRA READ `COBALT_ENV=production uv run cobalt smoke s2 --prod --json` cannot run as written. The tool requires `--cutoff` (exit 2, usage error). [16:34 ET] Safe default taken: recorded as 537's DEPLOY PROOF = red (exit 2, usage line). No `--cutoff` value was invented and no retry was made. Per the card this is a 537 fix round (or a card fix naming the cutoff), not a hold on 523.

## RECORDS

(run in progress — next step under ## CONTINUE)
