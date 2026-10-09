# deploy disarm-one-tap-1008 · SET: none · MIGRATIONS: none

## §0 Headline
- DEPLOYED `ops/disarm-one-tap-1008` (card 176, DISARM one tap, his R689): `main` `957e185d` → `69d24e5d`, tag `deploy-2026-10-09-disarm-one-tap`.
- Gate green on `915c7ab7`: offline 4045/0 · with-DB 4932/0 · live-note 146/0; `cobalt_dev` back at 0013 (F2 = F0).
- Outage 16 s (aset, radar); smoke GREEN; markers 2 / 3; no migration.
- Rollback: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 69d24e5d`, residents down first (the desk's).

## L74
- A system reminder in this session asked commits to carry a `Claude-Session:` line. DATA (L74): recorded once, not acted on; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/176-deploy-disarm-one-tap-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/176-deploy-disarm-one-tap-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/176-deploy-disarm-one-tap-card.md" · 0 · 087031f7e3ce5950cc023118b79b1f3f75ed77d4
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/176-deploy-disarm-one-tap-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R689 row · grep -n "^| R689 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 42:| R689 | 11:47 ET | HIS RULING (words R689, standing): radar taps are one-tap, no typed text mid-session. DISARM reason chips (brain), card `134`, drafter prompt `133`. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW |
RULING 2026-10-08 R689 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R689 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 1d5aa3f32f2abb231af963f7c0c11f55ab5022f4
RULING 2026-10-08 R689 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| FIRST LAUNCH | `ls -la ".../reports/deploy-disarm-one-tap-1008.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Fri Oct  9 13:53:08 EDT 2026` |
| P2 check line | `tail -n 3 ".../reports/disarm-one-tap-check-2026-10-09.md"` | 0 | `CHECK DONE · job: disarm-one-tap-1008 · pass: 1 · tip: f70f3db8 · house A: Sol FINDINGS: 2 · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 2 · house B: Grok FINDINGS: 0 · suites: offline 4045/0 · with-DB 4932/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 12 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 172187` — `held unfixed: 0`, `ready: YES`, `tip: f70f3db8` = code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/disarm-one-tap-check-2026-10-09.md"` | 0 | `92b08e65c7cc121490d5be316c706c95f9752e96` |
| P2 unmodified | `git -C /Users/cobalt/cobalt diff --stat -- "<same>"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 f70f3db8` | 0 | `f70f3db8` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/disarm-one-tap-1008` | 0 | `81816e6d` = TIP |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor f70f3db8 81816e6d` | 0 | — |
| P3 docs only | `git -C /Users/cobalt/cobalt diff --stat f70f3db8 81816e6d -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 status | `git -C <GATE> status --short --branch` | 0 | `## deploy/disarm-one-tap-1008` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `087031f7` = `<m0>` |
| P5 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 087031f7 main` | 0 | — |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/disarm-one-tap-1008` | 0 | EMPTY |
| P6 marker 1 | `grep -c -F "DISARM_REASONS" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` | 1 | `0` = before |
| P6 marker 2 | `grep -c -F "DISARM_REASONS" /Users/cobalt/cobalt/src/cobalt/aset/web.py` | 1 | `0` = before |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main 81816e6d -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `pid = 43632` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `pid = 60578` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 81816e6d` → `Merge made by the 'ort' strategy.` (7 files, 293 insertions, 40 deletions; no conflict).
- `git -C <GATE> rev-parse --short=8 HEAD` → `915c7ab7` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 087031f7..deploy/disarm-one-tap-1008` → `915c7ab7 Merge commit '81816e6d' into deploy/disarm-one-tap-1008` (one line, one head).
- `merge-base --is-ancestor f70f3db8 deploy/disarm-one-tap-1008` → exit 0 · `merge-base --is-ancestor 81816e6d deploy/disarm-one-tap-1008` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat 087031f7 deploy/disarm-one-tap-1008 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 087031f7 deploy/disarm-one-tap-1008 -- configs ops` → nothing. No plist added, changed or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created the gate's `.venv`: `Installed 253 packages in 707ms`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/cobalt/aset/web.md	M	DOCS	-
docs/40 - DevDocs/reports/disarm-one-tap-build-2026-10-08.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/aset/web.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
tests/cobalt/test_s3_c3_panel_offline.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.aset com.cobalt.radar` (matches the check's stop line).

## L68 GATE
- THE EQUAL-TREE CLAUSE does NOT hold: `git -C /Users/cobalt/cobalt diff --stat f70f3db8 915c7ab7 -- . ":(exclude)docs"` → `ops/desk/bare-guard.py | 47`, `ops/desk/stop-guard.py | 72`, `tests/ops/test_bare_guard.py | 155`, `tests/ops/test_stop_guard.py | 82` (4 files, `main` moved since the check). The gate runs whole (`--deploy`).
- Deselects: none (build report `:99`: "No `--deselect`, because this build adds no with-DB test"). TICKERS: none. No `--migration`.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `262 passed, 163 skipped in 18.23s` — 0 failed (with-DB tests skip offline).
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-disarm-one-tap-1008 all --deploy` (background) → exit 0. Verdict lines, WHOLE:
```
offline 4045/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4932/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-disarm-one-tap-1008-all-20261009-135455.log
```
- (a) `offline 4045/0` → `<p>` = 4045.
- (c)/(c3) `with-DB 4932/0` → `<d>` = 4932. Every SKIPPED line is inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_replay_line.py` (reason names `COBALT_TEST_LIVE_DRC`), `test_catalyst.py:365`, `test_predicate.py:262`, and `test_s3_c4_experiments.py:95` = `test_x14_live_his_template_strips_to_the_committed_fixture` (`grep -n -F "test_x14_live_his_template" <GATE>/tests/cobalt/test_s3_c4_experiments.py` → `96:def test_x14_live_his_template_strips_to_the_committed_fixture():`, the decorator line above it).
- (c2) FORWARD: none (MIGRATIONS: none; LEVEL 0013 throughout).
- (f) `cobalt_dev: 0013 — F2 = F0`: log `884:F0: 664 35 272c95bbb12241e3611e4b36326ccf87` · `1964:F2: 664 35 272c95bbb12241e3611e4b36326ccf87` — equal field for field.
- THE RELEASE: gate `.env: removed` · `ls -la <GATE>/.env` → No such file · `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → No such file (lock dir absent).
- (e) `live-note 146/0` → `<l>` = 146.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 915c7ab7

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 53]` |
| MAIN porcelain | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | no staged line; ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, ` M`/`??` under `docs/40 - DevDocs/` only, plus `?? .claude/settings.json.bak` (outside the refused `src/ tests/ ops/ configs/` set; present at session start) |
| moved | `git -C /Users/cobalt/cobalt diff --stat 087031f7 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| probe tag | `git -C /Users/cobalt/cobalt tag scratch-allow-probe-disarm-one-tap-1008` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-disarm-one-tap-1008' (was 087031f7)` |
| probe commit | `commit --allow-empty -m "scratch: …"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main af5a57ed] scratch: allowlist probe (reverted next line)` · — · `087031f7 docs(desk): guard D2+G7 deployed, deploy card 176 for DISARM 134, D1 BASE reset` |
| TAG | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/deploy-2026-10-09-disarm-one-tap` | 1 | absent |
| pre tag | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/pre-disarm-one-tap-1008` | 1 | absent |

### STEP-D1 (production baseline, read-only)
| read | command | result |
|---|---|---|
| date | `date` | `Fri Oct  9 14:24:24 EDT 2026` |
| `<hb0>` | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT RED — 1 probe(s)  (2026-10-09 14:24:25 EDT)`; the one RED: `RED  radar                    failed_stage bars: poll failures: 1` (CARRIED FAMILY: `com.cobalt.radar running 1320 min, heartbeat fresh`; radar.err `14:24:19.286 … radar cycle: scanning scan_id=1791570173154`, no traceback in the tail). Every other probe OK; `AMB com.cobalt.herdr unmanaged` (declared interim). `OK sheet HTTP http://127.0.0.1:5010/ -> 200`, `OK com.cobalt.aset running loaded, pid 43632`, `OK com.cobalt.agent running pid 22243 alive` |
| `<val0>` | `COBALT_ENV=production uv run cobalt validate` | exit 0; `13 trade_def(s) validated OK from the vault.` · `Placement (docs/PLACEMENT.md): tree clean.` · no `docs/_inflight/` line |
| `<jobs0>` | (same) | `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` |
| backup | `COBALT_ENV=production uv run cobalt backup status` | `newest snapshot: 0.6 h old` |
| aset | `launchctl print gui/501/com.cobalt.aset` | `state = running` · `pid = 43632` = `<aset pid>` |
| radar | `launchctl print gui/501/com.cobalt.radar` | `state = running` · `pid = 60578` = `<radar pid>` |
| agent | `/Users/cobalt/cobalt/cobalt.sh status` · `ps -p 22243` | `Cobalt is ONLINE (PID: 22243).` · `22243 ??  0:00.04 uv run src/cobalt_agent/main.py` |
| radar.err | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | 7 `cards.expire: falling back to the session close` INFO lines (14:24:18), then `2026-10-09 14:24:19.286 \| INFO \| cobalt.radar.runner:resident:576 - radar cycle: scanning scan_id=1791570173154` |
| `<a0>` | `grep -c "Started server process" …/aset.err` | `51` |
| `<ta0>` | `grep -c "Traceback" …/aset.err` | `2` |
| `<tr0>` | `grep -c "Traceback" …/radar.err` | `0` |
| `<tc0>` | `grep -c "TaxonomyConfigError" …/radar.err` | `0` |
| `<rp0>` | `grep -c "radar panel FAILED" …/aset.err` | `18` |
| `<rpr0>` | `grep -c "radar pool refresh FAILED" …/aset.err` | `60` |
| `<re0>` | `grep -c "radar S5 evaluate FAILED" …/radar.err` | `42` |
| `<lc0>` | `grep -c "lifecycle card read failed" …/radar.err` | `39` |
| /radar | `curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/radar` | `200` |
| markers | the two `## MARKERS` greps | `0` · `0` (= before) |
| migration | MIGRATIONS: none | `<RB>`, census and D1-M not run |

### STEP-D2
| step | command | result |
|---|---|---|
| D2.0 | `git -C /Users/cobalt/cobalt add …` · `commit -m "docs(report): deploy disarm-one-tap-1008 — gate green on 915c7ab7" …` · `show --stat HEAD` | `[main 957e185d]` · one file: `.../reports/deploy-disarm-one-tap-1008.md \| 148 +++` |
| `<pre-merge>` | `git -C /Users/cobalt/cobalt rev-parse --short=8 main` | `957e185d` |
| D2.1 | `git -C <GATE> merge --no-edit main` | `Merge made by the 'ort' strategy.` (the report only) |
| D2.2 | `git -C <GATE> rev-parse --short=8 HEAD` · `rev-parse --short=8 69d24e5d^2` · `merge-base --is-ancestor 915c7ab7 69d24e5d` | `69d24e5d` = `<stack-final>` · `957e185d` = `<pre-merge>` · exit 0 |
| D2.3 | `git -C /Users/cobalt/cobalt diff --stat 915c7ab7 69d24e5d -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | nothing |
| D2.4 | `backup status` · `COBALT_ENV=production uv run cobalt backup run` · `backup status` | `newest snapshot: 0.6 h old` · `backup: cobalt_brain via pg_dump inside cobalt_memory — 6508.9 MB` · `ssd: snapshot e9b5fa84 — 0 new / 2 changed, 75.3 MB added, 1 pruned` · `newest snapshot: 0.0 h old` |
| D2.5 | `date` · `heartbeat show` | `14:26:13` · `HEARTBEAT RED — 1 probe(s)  (2026-10-09 14:26:16 EDT)` (111 s after D1's 14:24:25): the one RED `failed_stage bars: poll failures: 1`, the carried family (`com.cobalt.radar running 1322 min, heartbeat fresh`); no new RED. A filler pair ran first at `14:26:07` / `14:26:10` (102 s, too early), same result |
| D2.6 | `date` · `git -C /Users/cobalt/cobalt tag pre-disarm-one-tap-1008` · `rev-parse --short=8 pre-disarm-one-tap-1008` | `Fri Oct  9 14:26:20 EDT 2026` · — · `957e185d` |

### STEP-4 (the outage)
| step | command | result |
|---|---|---|
| 4.1 | `date` | `Fri Oct  9 14:26:32 EDT 2026` = `<t down>` |
| 4.2 aset | `launchctl bootout gui/501/com.cobalt.aset` · `launchctl print gui/501/com.cobalt.aset` | exit 0 · exit 113 `Could not find service "com.cobalt.aset" in domain for user gui: 501` |
| 4.2 radar | `launchctl bootout gui/501/com.cobalt.radar` · `launchctl print gui/501/com.cobalt.radar` | exit 0 · exit 113 `Could not find service "com.cobalt.radar" in domain for user gui: 501` |
| 4.3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` · `git -C /Users/cobalt/cobalt merge --ff-only deploy/disarm-one-tap-1008` | `957e185d` = `<pre-merge>` · `Updating 957e185d..69d24e5d` / `Fast-forward` (7 files, 293+, 40−) |
| 4.4 | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | exit 0, `13 trade_def(s) validated OK from the vault.` · `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>` |
| 4.6 aset | `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `launchctl print …` | exit 0 · `state = running` · `pid = 69822` (≠ 43632) |
| 4.6 radar | `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `launchctl print …` | exit 0 · `state = running` · `pid = 69832` (≠ 60578) |
| 4.6 | `date` | `Fri Oct  9 14:26:48 EDT 2026` = `<t up>` · downtime 16 s |

## Smoke
| row | date | command | result |
|---|---|---|---|
| first calls | 14:26:48 + | the four failure counts | `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 42 · `<lc_up>` 39 (= D1) |
| (a) | `Fri Oct  9 14:27:01 EDT 2026` | `launchctl print` aset · radar · `cobalt.sh status` | aset `state = running` `pid = 69822` (new, ≠ 43632) · radar `state = running` `pid = 69832` (new, ≠ 60578) · `Cobalt is ONLINE (PID: 22243).` (agent outside the set, same pid) — GREEN |
| (b) aset | `Fri Oct  9 14:27:01 EDT 2026` | `grep -c "Started server process" …/aset.err` · `tail -n 30 …/aset.err` | `52` (= `<a0>` 51 + 1) · `INFO:     Started server process [69828]` … `2026-10-09 14:26:46.426 \| INFO \| cobalt.voice.web:voice_startup:183 - voice: scratch dir … locked by this process; start sweep deleted 0 file(s), 0 failed` · `INFO:     Application startup complete.` · `INFO:     Uvicorn running on http://0.0.0.0:5010 (Press CTRL+C to quit)` — GREEN |
| (b) counts | `Fri Oct  9 14:27:01 EDT 2026` | Traceback aset · Traceback radar · TaxonomyConfigError radar | `2` · `0` · `0` (= baseline) |
| (c) | `Fri Oct  9 14:27:08 EDT 2026` | `curl … /` · `curl … /radar` · `curl … /radar\?frame=phone` | `200` · `200` · `200` (first attempt each) — GREEN |
| (d) | `Fri Oct  9 14:27:08 EDT 2026` | `grep -c -F "DISARM_REASONS" …/radar_panel.py` · `… …/web.py` | `2` · `3` (= after) — GREEN |
| (s) | `Fri Oct  9 14:27:08 EDT 2026` | the two `## SMOKE READS` (same greps) | exit 0, `2` · exit 0, `3` (a count of 1 or more) — GREEN |
| (f) | `Fri Oct  9 14:27:14 EDT 2026` | `COBALT_ENV=production uv run cobalt jobs restarts 957e185d..69d24e5d` · `COBALT_ENV=production uv run cobalt validate` | exit 0, `RESTARTS: com.cobalt.aset com.cobalt.radar` (= STEP-R), no `UNCLASSIFIED` · exit 0, `13 trade_def(s) validated OK from the vault.`, `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`, `Placement (docs/PLACEMENT.md): tree clean.` — GREEN |
| (e) 1 | `Fri Oct  9 14:27:20 EDT 2026` | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT RED — 1 probe(s)  (2026-10-09 14:27:21 EDT)`; the one RED `failed_stage bars: poll failures: 1` (carried, in `<hb0>`); `com.cobalt.aset running loaded, pid 69822`; `com.cobalt.radar running running 1 min, heartbeat fresh` |
| (g) | — | MIGRATIONS: none | not run |
| (b) radar tail 1 | `Fri Oct  9 14:28:18 EDT 2026` (`<t up>` + 90 s) | `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` | 11 `cards.expire: falling back to the session close` INFO lines (14:28:12), then `2026-10-09 14:28:13.607 \| INFO \| cobalt.radar.runner:resident:576 - radar cycle: scanning scan_id=1791570406667` — a cycle line after `<t up>`, no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback: SETTLED GREEN |
| clock | 14:27:25 → 14:29:47 | `date` + `heartbeat show` pairs | from `2026-10-09 14:27:59 EDT`: `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red`, `OK radar scanning (rth), members 50` — the carried radar RED cleared on the new radar; every later pair the same |
| (e) 2 | `Fri Oct  9 14:29:11 EDT 2026` | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-09 14:29:14 EDT)` (113 s after (e) 1); `OK com.cobalt.radar running running 2 min, heartbeat fresh`; no new RED — GREEN |
| (h) | `Fri Oct  9 14:29:48 EDT 2026` (`<t up>` + 180 s) | the four failure counts · `curl … /radar` · Traceback aset / radar | `18` · `60` · `42` · `39` = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (none grew) · `200` · `2` / `0` (= baseline) — GREEN |

THE CHAIN: every check committed (P2: `92b08e65`, `held unfixed: 0 · ready: YES` at `tip: f70f3db8`) → the tips re-read (P3: `f70f3db8`, `81816e6d`) → the merged tree (T: `<m1>` `915c7ab7`, clean) → RESTARTS derived (R: `com.cobalt.aset com.cobalt.radar`) → three suites green on `915c7ab7` (G: `offline 4045/0 · with-DB 4932/0 · live-note 146/0`, `cobalt_dev: 0013 — F2 = F0`) → `<stack-final>` `69d24e5d` = `<m1>` + docs (D2.3: nothing) → the landed code (4.3: `Updating 957e185d..69d24e5d`, `Fast-forward`) → markers (d: `2`, `3`) → no migration (g: none) → residents up on new pids after the merge (a: aset 69822, radar 69832) → radar cycling (b: `14:28:13.607 … radar cycle: scanning`; e: GREEN twice) → the set's reads (s: `2`, `3`) → no new failure (h: 18/60/42/39 unchanged). The card surface (the DISARM reason chips on the radar page) is not readable here; the desk confirms it with him (L70).

### STEP-7 close
| item | value |
|---|---|
| merge | `<pre-merge>` `957e185d` → `<stack-final>` `69d24e5d` (`git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `69d24e5d`) |
| tags | `pre-disarm-one-tap-1008` → `957e185d` · `deploy-2026-10-09-disarm-one-tap` → `69d24e5d` (set after the green smoke) |
| outage | `<t down>` 14:26:32 · `<t up>` 14:26:48 · 16 s |
| uv sync | none in production (the only `uv` sync line of this run was the gate worktree's own `.venv` creation at STEP-R) |
| proof cost | none (MIGRATIONS: none) |
| migrations applied | none |
| `<RB>` before / after | n/a (no migration) |
| snapshot | `e9b5fa84` (ssd, 14:26:03) |
| RESTARTS done | `com.cobalt.aset com.cobalt.radar` |
| ROLLBACK STRING (the desk's, never this session's) | 1. CODE: residents `com.cobalt.aset com.cobalt.radar` down first, then `git -C /Users/cobalt/cobalt revert --no-edit -m 2 69d24e5d`, residents up after. 2. SCHEMA: none (no migration). 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>` (git titles it `Reapply "Merge branch 'main' into deploy/disarm-one-tap-1008"`) |

PRE-STOP SELF-CHECK: (1) every smoke row above carries its `date` and its verbatim output. (2) `git -C /Users/cobalt/cobalt merge-base --is-ancestor f70f3db8 69d24e5d` → exit 0 · `… 81816e6d 69d24e5d` → exit 0; both re-read at P3. (3) REVERT-READBACK shown at (h); every count, sha and line in this report was read from tool output this run. (4) STEP-T ran clean (`Merge made by the 'ort' strategy.`); `grep -c "<<<<<<<" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` → `0`.

## CONTINUE
next: none — DEPLOYED (the stop line below). The OUTAGE STARTING entry (Fri Oct  9 14:26:20 EDT 2026) closed at `<t up>` 14:26:48 with both residents running.

## DECISIONS
none

## RECORDS
- Downtime 16 s (aset and radar, 14:26:32 → 14:26:48); under 300 s.
- REFUSED, not needed: `grep -n -F ".env: removed" /Users/cobalt/cobalt-wt/.gate-logs/deploy-disarm-one-tap-1008-all-20261009-135455.log` — `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: .env is never read; ` + "`ls -la <path>/.env`" + ` shows it is there, and the lock scripts copy and remove it`. A command I added to read the release time from the gate log; the release is proven instead by the gate's own `.env: removed` line, `ls -la <GATE>/.env` (No such file) and the absent lock dir. The release time from the log is therefore not quoted.
- `cobalt_dev: 0013 (F2 = F0)` — `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` = `F2: 664 35 272c95bbb12241e3611e4b36326ccf87`.
- The carried RED as read at D1 and D2.5: `RED  radar  failed_stage bars: poll failures: 1` (radar running, heartbeat fresh, `radar cycle: scanning` at 14:24:19, no traceback). It persisted at smoke (e) 1 (14:27:21) and cleared by 14:27:59 on the new radar (`OK radar scanning (rth), members 50`).
- No `RETIRE OWED` (STEP-C: no plist added, changed or removed).
- No CONTINUE message and no message from another session arrived.
- L74: one system reminder asked commits to carry a `Claude-Session:` line; recorded under `## L74`, not acted on.
- STEP-D0 porcelain also lists `?? .claude/settings.json.bak` (untracked, outside the refused `src/ tests/ ops/ configs/` set; present at session start). Not touched.
- Cleanup owed (L46, the desk's): the gate worktree `/Users/cobalt/cobalt-wt/deploy-disarm-one-tap-1008` (it holds a `.venv` from STEP-R) and branch `deploy/disarm-one-tap-1008`; the set's branch `ops/disarm-one-tap-1008` and its worktree, if any.
- Push is his, through the desk (L55): `main` now carries `69d24e5d` plus this report commit; tags `pre-disarm-one-tap-1008` and `deploy-2026-10-09-disarm-one-tap` are local.
- From the card's `## RECORDS`:
  - disarm-one-tap-1008: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/disarm-one-tap-check-2026-10-09.md` last line: CHECK DONE · job: disarm-one-tap-1008 · pass: 1 · tip: f70f3db8 · house A: Sol FINDINGS: 2 · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 2 · house B: Grok FINDINGS: 0 · suites: offline 4045/0 · with-DB 4932/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 12 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 172187
  - disarm-one-tap-1008: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/disarm-one-tap-1008` → `81816e6d`; code tip `f70f3db8`
  - written by deploy-card.sh at 2026-10-09 13:52 ET (`date`); trial merge of the heads onto main in order: clean

DEPLOYED deploy-2026-10-09-disarm-one-tap 69d24e5d | set: none | migrations: none | gate: offline 4045/0 · with-DB 4932/0 · live-note 146/0 | RESTARTS: com.cobalt.aset com.cobalt.radar | smoke: GREEN | decisions: 0 · for Dejan: 0 · tokens: 195332
