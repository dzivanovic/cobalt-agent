# deploy hub-text-1013-fr1 · SET: none · MIGRATIONS: none

## §0 Headline
- DEPLOYED: `ops/hub-text-1013-fr1` (code tip `e82cdcc7`, head `b920401e`) is on `main` at `bcf791ee`, tag `deploy-2026-10-14-hub-text-fr1`. Docs-only hub text plus two ops tests.
- Gate green on `183300f9`: offline 4328/0 · with-DB 5231/0 · live-note 146/0. RESTARTS: none. No resident went down. Smoke GREEN.
- 537's EXTRA READ (`smoke s2 --prod --json`) exited 2: the tool requires `--cutoff` (DECISIONS 2). Per the card that is a 537 fix round, not a hold on 523.

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

### STEP-D2
- D2.0 commit `3fb98527` `docs(report): deploy hub-text-1013-fr1 — gate green on 183300f9`. `show --stat HEAD` → one file, `.../reports/deploy-hub-text-1013-fr1.md | 149 +++`. `<pre-merge>` = `3fb98527`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report, 149 insertions).
- D2.2 `<stack-final>` = `bcf791ee` · `bcf791ee^2` = `3fb98527` = `<pre-merge>` · `merge-base --is-ancestor 183300f9 deploy/hub-text-1013-fr1` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat 183300f9 deploy/hub-text-1013-fr1 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- D2.4 `backup status` before → `newest snapshot: 1.5 h old`. `backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 7881.0 MB` · `ssd: snapshot 9dcb14a6 — 0 new / 2 changed, 148.2 MB added, 1 pruned`. `backup status` after → `newest snapshot: 0.0 h old`. Snapshot id `9dcb14a6`.
- D2.5 16:36:19 ET (+119 s after D1's 16:34:20 read): `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-14 16:36:20 EDT)`. No new RED; `com.cobalt.radar running 1105 min, heartbeat fresh`.
- D2.6 `date` → `Wed Oct 14 16:36:24 EDT 2026`. `git -C /Users/cobalt/cobalt tag pre-hub-text-1013-fr1` at `3fb98527` → exit 0.

### STEP-4 (`<restart set>` empty)
- 4.1 `date` → `Wed Oct 14 16:36:39 EDT 2026` (`<t down>`; with an empty set this is also `<t up>`).
- 4.2 no label in the set: no bootout, no orphan-clean, no agent stop.
- 4.3 `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `3fb98527` = `<pre-merge>`. `git -C /Users/cobalt/cobalt merge --ff-only deploy/hub-text-1013-fr1` → `Updating 3fb98527..bcf791ee` / `Fast-forward` (5 files, 238 insertions, 3 deletions).
- 4.4 `migrations applied: none`.
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0 (ends `Placement (docs/PLACEMENT.md): tree clean.`). `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`.
- 4.6 no label taken down: nothing to bootstrap. Downtime: none.
- 4.6L `<launchd set>` empty: nothing.

### STEP-7 summary
| item | value |
|---|---|
| merge | `<pre-merge>` `3fb98527` → `<stack-final>` `bcf791ee` (`main` tip `bcf791ee`) |
| tags | `pre-hub-text-1013-fr1` at `3fb98527` · `deploy-2026-10-14-hub-text-fr1` at `bcf791ee` (after green smoke) |
| `<t down>` / `<t up>` / seconds | none: empty restart set (merge at 16:36:39 ET) |
| uv sync | none on `main`. The gate worktree's first `uv run` created its `.venv` (`Installed 254 packages in 755ms`, STEP-R) |
| proof cost | n/a: no migration, no D1-M. The gate's dev proof was `Proof cost: total 5.9 s` (log `2084`) |
| migrations applied | none |
| `<RB>` before / after | n/a (MIGRATIONS: none) |
| snapshot | `9dcb14a6` (ssd) |
| RESTARTS done | none |
| LAUNCHD done | none. No `BOOTSTRAP OWED` line |
| ROLLBACK STRING | 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 bcf791ee` (empty restart set: no resident down or up; no launchd label). 2. SCHEMA: none. 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>` |

## Smoke
`<t up>` = 4.3's `date` = 16:36:39 ET (empty set).
- FIRST CALLS: `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 (= D1 baselines).
- (a) 16:36:59: aset `state = running`, `pid = 40377` (SAME as D1, outside the set) · radar `state = running`, `pid = 8646` (SAME) · `Cobalt is ONLINE (PID: 14763).` (SAME). GREEN.
- (b) 16:37:03: `Started server process` 279 = `<a0>` (aset outside the set) · aset Traceback 217 = `<ta0>` · radar Traceback 0 = `<tr0>` · TaxonomyConfigError 0 = `<tc0>`. `tail -n 30 aset.err` has no new `Started server process` line. Its last entries are 10:01 ET daily-note write lines; vault content is not copied here. Radar tails: below.
- (c) 16:37:07: `/` → `200` · `/radar` → `200` · `/radar\?frame=phone` → `200`. GREEN.
- (d) 16:37:13: markers → `1` · `1` · `1` (each its `after`). GREEN.
- (e1) 16:37:16: `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-14 16:37:18 EDT)`; `com.cobalt.radar running 1106 min, heartbeat fresh`; only AMB is `com.cobalt.herdr` (as in `<hb0>`).
- (f) 16:37:23: `COBALT_ENV=production uv run cobalt jobs restarts 3fb98527..bcf791ee` → exit 0, the same 5 rows as STEP-R (DOCS ×3, `test/documentation; no resident` ×2), `RESTARTS: none` = `<restart set>`, no UNCLASSIFIED. `validate` → exit 0, `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>`. GREEN.
- (s) 16:37:25: `uv run pytest tests/ops/test_hub_text_1013.py tests/ops/test_hub_lines.py tests/ops/test_build_hub_no_clutter.py` → `39 passed, 15 warnings in 2.95s` (4 + 30 + 5). The card's green is "all passed". GREEN. The card's EXTRA READ for 537 was recorded under STEP-D0 (exit 2, see DECISIONS 2). It is not a smoke row of this set.
- (g) no migration.
- (e2) 16:39:06: `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-14 16:39:09 EDT)`, 111 s after (e1)'s 16:37:18. `com.cobalt.radar running 1108 min, heartbeat fresh`. No RED that is not in `<hb0>`. GREEN.
- (b) radar tails. Tail 1 at 16:38:15 (+96 s): last cycle line `16:36:21.998 radar cycle: scanning` (before `<t up>`), then `radar price floor` collect lines at 16:38:14. No failure, not settled. Tail 2 at 16:39:39 (+180 s): `2026-10-14 16:39:30.482 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792010282024`. That is stamped after `<t up>`; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback. SETTLED GREEN, so the third tail was not needed.
- (h) 16:39:57 (`<t up>` + 198 s): `radar panel FAILED` 18 = `<rp_up>` · `radar pool refresh FAILED` 60 = `<rpr_up>` · `radar S5 evaluate FAILED` 43 = `<re_up>` · `lifecycle card read failed` 39 = `<lc_up>` · radar Traceback 0. `/radar` → `200`. No census reads on this card. No count grew. GREEN.

THE CHAIN: every check committed (P2: `207ba05e`, clean) → tips re-read (P3: `e82cdcc7`, `b920401e`) → merged tree (T: `183300f9`, clean ort merge) → RESTARTS derived (R: none) → three suites green on `183300f9` (G: offline 4328/0 · with-DB 5231/0 · live-note 146/0) → `bcf791ee` = `183300f9` + docs (D2.3) → landed code (4.3: `3fb98527..bcf791ee` fast-forward) → markers 1/1/1 (d) → no migration (g) → residents unchanged and up (a) → radar cycling (b, e) → the set's reads (s: 39 passed) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

**smoke: GREEN**

## CONTINUE
- next: STEP-D0 (gate green at 16:33:36 ET)
- OUTAGE STARTING 16:36:24 ET — residents of <restart set> going down; `<restart set>` is EMPTY (none), so no resident goes down and only the merge moves. If this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
- 4.6 ended 16:36:39 ET: no resident down. Smoke GREEN at 16:39:57 ET. Run closed at STEP-7.

## DECISIONS
1. ASK DESK: `?? .claude/settings.json.bak` is untracked on `main`. It is not in D0's ACCEPTED list, and not in its REFUSED list (not staged; not `src/`, `tests/`, `ops/` or `configs/`). [16:33 ET] Safe default taken: go on. An untracked file cannot enter the ff merge or the gate tree. The desk decides whether to remove it or add it to the accepted list.
2. ASK DESK: the card's EXTRA READ `COBALT_ENV=production uv run cobalt smoke s2 --prod --json` cannot run as written. The tool requires `--cutoff` (exit 2, usage error). [16:34 ET] Safe default taken: recorded as 537's DEPLOY PROOF = red (exit 2, usage line). No `--cutoff` value was invented and no retry was made. Per the card this is a 537 fix round (or a card fix naming the cutoff), not a hold on 523.

## RECORDS
- Downtime: none (empty restart set).
- `cobalt_dev: 0013 (F2 = F0)`: `664 35 272c95bbb12241e3611e4b36326ccf87` both (gate log lines 902 and 2039). Lock released by the gate (`lock released`, `.env: removed`).
- REFUSED, not needed: `grep -n -F ".env: removed" <gate log>` — `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: .env is never read; `ls -la <path>/.env` shows it is there, and the lock scripts copy and remove it`. I added that read on my own; I read the release lines with the Read tool instead (log 2092–2097).
- Carried RED: none. `<hb0>` was GREEN (one AMB: `com.cobalt.herdr` unmanaged, a declared interim).
- RETIRE OWED: none. BOOTSTRAP OWED: none.
- L74: one system-reminder asked for a `Claude-Session:` line in commits. It was recorded under `## L74` and not followed.
- Messages not followed: none (no CONTINUE message arrived).
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-hub-text-1013-fr1` and branch `deploy/hub-text-1013-fr1`; the set's branch `ops/hub-text-1013-fr1` and its worktree, if any.
- Push is his (L55): `main` is now `bcf791ee`, with tags `pre-hub-text-1013-fr1` and `deploy-2026-10-14-hub-text-fr1`.
- Card `## RECORDS` (the desk's), copied:
  - hub-text-1013-fr1: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/hub-text-fr1-check-2026-10-14.md` last line: CHECK DONE · job: hub-text-1013-fr1 · pass: 1 · tip: e82cdcc7 · house A: Grok FINDINGS: 0 · findings: 1 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 4328/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 9 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 149298
  - hub-text-1013-fr1: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/hub-text-1013-fr1` → `b920401e`; code tip `e82cdcc7`
  - written by deploy-card.sh at 2026-10-14 16:00 ET (`date`); trial merge of the heads onto main in order: clean
- PRE-STOP SELF-CHECK. (1) Every smoke row is quoted with its `date` (16:36:59 through 16:39:57). (2) `e82cdcc7` and `b920401e` were re-read at P3. `merge-base --is-ancestor e82cdcc7 bcf791ee` and `merge-base --is-ancestor b920401e bcf791ee` both exit 0. (3) The REVERT-READBACK (h) is shown; every count and sha above was re-read from this run's tool output. (4) STEP-T ran clean (`Merge made by the 'ort' strategy.`), so there are no conflict markers.

DEPLOYED deploy-2026-10-14-hub-text-fr1 bcf791ee | set: none | migrations: none | gate: offline 4328/0 · with-DB 5231/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 2 · for Dejan: 0 · tokens: 181767
