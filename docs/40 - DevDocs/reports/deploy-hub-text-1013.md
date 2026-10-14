# deploy hub-text-1013 · SET: none · MIGRATIONS: none

## §0 Headline
- Docs/test-only deploy of `ops/hub-text-1013` (head `0f4a49c5`, code tip `3894a878`). Run in progress.

## L74
- One block arrived in a system reminder asking for a `Claude-Session:` line on commits. DATA (L74): not acted on; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/535-deploy-hub-text-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/535-deploy-hub-text-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-14/535-deploy-hub-text-card.md" · 0 · 68183da73bb75d79e295eabfdaa99c9fc5c64faa
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-14/535-deploy-hub-text-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```
First launch: `ls -la "<REPORT>"` → `No such file or directory` (exit 1).

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Wed Oct 14 06:47:50 EDT 2026` |
| P2 | `tail -n 3 ".../hub-text-check-2026-10-13.md"` | 0 | `CHECK DONE · job: hub-text-1013 · pass: 1 · tip: 3894a878 · house A: Grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 4317/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 8 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 138522` — carries `held unfixed: 0`, `ready: YES`, `tip: 3894a878` = row's code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/hub-text-check-2026-10-13.md"` | 0 | `06b2ac9b006d05e5371077f7690849c82935c8f0` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/hub-text-check-2026-10-13.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 3894a878` | 0 | `3894a878` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/hub-text-1013` | 0 | `0f4a49c5` (= row, = `TIP`) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 3894a878 0f4a49c5` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 3894a878 0f4a49c5 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — lock free |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-hub-text-1013 status --short --branch` | 0 | `## deploy/hub-text-1013` |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-hub-text-1013 rev-parse --short=8 HEAD` | 0 | `68183da7` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 68183da7 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/hub-text-1013` | 0 | EMPTY |
| P6 | `grep -c -F "21:30-22:30 ET" ".../DEPLOY-HUB.md"` | 1 | `0` (before `0`) |
| P6 | `grep -c -F "FIX-ROUND REPORT (brain R1309):" ".../BUILD-HUB.md"` | 1 | `0` (before `0`) |
| P6 | `grep -c -F "no untracked file at the stop line" ".../BUILD-HUB.md"` | 1 | `0` (before `0`) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 0f4a49c5 -- src/cobalt/db_migrations` | 0 | nothing — MIGRATIONS: none holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 40377` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 8646` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 14763).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-hub-text-1013 merge --no-edit 0f4a49c5` → `Auto-merging docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `Merge made by the 'ort' strategy.` · 5 files changed, 317 insertions(+), 3 deletions(-) (BUILD-HUB.md, DEPLOY-HUB.md, hub-text-build-2026-10-13.md, tests/ops/test_build_hub_no_clutter.py, tests/ops/test_hub_text_1013.py)
- `git -C /Users/cobalt/cobalt-wt/deploy-hub-text-1013 rev-parse --short=8 HEAD` → `1bdc32b8` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 68183da7..deploy/hub-text-1013` → `1bdc32b8 Merge commit '0f4a49c5' into deploy/hub-text-1013`
- `merge-base --is-ancestor 3894a878 deploy/hub-text-1013` → exit 0 · `merge-base --is-ancestor 0f4a49c5 deploy/hub-text-1013` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat 68183da7 deploy/hub-text-1013 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none)
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 68183da7 deploy/hub-text-1013 -- configs ops` → nothing · `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 68183da7 deploy/hub-text-1013` → `STEP-C: ADMITTED 0` (exit 0) → `<launchd set>` empty

## RESTARTS
`cd /Users/cobalt/cobalt-wt/deploy-hub-text-1013` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created `.venv`, `Installed 254 packages in 548ms`):
```
path	change	rule	restart
docs/40 - DevDocs/prompts/BUILD-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/hub-text-build-2026-10-13.md	A	DOCS	-
tests/ops/test_build_hub_no_clutter.py	M	test/documentation; no resident	-
tests/ops/test_hub_text_1013.py	A	test/documentation; no resident	-
RESTARTS: none
```
`<restart set>` = EMPTY · `<launchd set>` = EMPTY. No resident goes down.

## L68 GATE
- EQUAL-TREE CLAUSE: not held — the check's stop line carries `with-DB 0/0` (DB: none single branch) → the gate runs whole (`--deploy`). The set changes `DEPLOY-HUB.md`: `gate.sh` runs on the merged hub text (L68).
- Deselects: none (build report `hub-text-build-2026-10-13.md` names none; DB: none). TICKERS: none. Migration: none.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_archiver_migrations.py … tests/cobalt/test_jobs_restarts.py` (the 17 files) → `263 passed, 163 skipped in 18.45s` — 0 failed.
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-hub-text-1013 all --deploy` → exit 0, verdict lines WHOLE:
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-hub-text-1013-all-20261014-064947.log
```
- (a) offline: log `:885` `4328 passed, 806 skipped, 1 xfailed, 36 warnings in 697.23s (0:11:37)` → `offline 4328/0`.
- (b) lock waited 0 min; `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:902`); proof-only at `0013`, nothing CHANGED (log `:954`).
- (c) pass 1 (log `:1116`): `5026 passed, 7 skipped, 99 deselected, 3 xfailed, 43 warnings in 827.39s (0:13:47)`. Every SKIPPED line inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_replay_line.py:266` (reason names `COBALT_TEST_LIVE_DRC`), `test_s3_c4_experiments.py:95` (= `test_x14_live_his_template_strips_to_the_committed_fixture`, read at `<GATE>/tests/cobalt/test_s3_c4_experiments.py:95-96`), `test_catalyst.py:365`, `test_predicate.py:262`.
- (c2) `dev forward: APPLIED 07:15:38` (log `:1118`); `F1: 908 45 126f2d6983fa59f9d0eaaff7da7dd29c` (log `:1196`); no `CHANGED` (proof lines `content UNCHANGED on every table`, log `:1186`).
- (c3) pass 2 (log `:1971`): `205 passed, 1 deselected, 5 warnings in 230.99s (0:03:50)` → `with-DB 5231/0`.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:2039`) = F0 → `cobalt_dev: 0013 — F2 = F0` (log `:2091`).
- THE RELEASE: log `:2092-2097` `release-devdb-lock.sh deploy-hub-text-1013` → `lock released`, `.env: removed` (L76 lock released; the log stamps no clock on it — after `dev forward` 07:15:38, before my `date` 07:20:49). `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-hub-text-1013" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- (e) live-note (log `:2162`): `146 passed, 1 skipped, 15 warnings in 27.90s`; the one skip is `test_replay_line.py:266` naming `COBALT_TEST_LIVE_DRC` (allowed); none names `COBALT_LIVE_VAULT_ROOT` → `live-note 146/0`.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 1bdc32b8

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 31]` |
| MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | no staged line; ` M` / `??` under `docs/40 - DevDocs/`, ` M configs/cobalt/rules.yaml`, ` M .claude/settings.json`; plus `?? .claude/settings.json.bak` and `?? "docs/30 - Design/jev-shadow-design-2026-10-14.md"` (neither a refused class: not staged, not under `src/`, `tests/`, `ops/`, `configs/`; recorded) |
| MAIN | `git -C /Users/cobalt/cobalt diff --stat 68183da7 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `git -C /Users/cobalt/cobalt tag scratch-allow-probe-hub-text-1013` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-hub-text-1013' (was 68183da7)` |
| PROBE | `git -C /Users/cobalt/cobalt commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main ff76f7d0] scratch: …` · — · `68183da7 docs(card): deploy card 535 for hub-text 523` (HEAD back) |
| TAGS | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/deploy-2026-10-14-hub-text` | 1 | free |
| TAGS | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/pre-hub-text-1013` | 1 | free |

### STEP-D1 (read-only)
| read | command | exit | result |
|---|---|---|---|
| time | `date` | 0 | `Wed Oct 14 07:21:20 EDT 2026` |
| `<hb0>` | `COBALT_ENV=production uv run cobalt heartbeat show` | 0 | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-14 07:21:21 EDT)`; `OK   radar                    scanning (premarket), members 50`; `OK   com.cobalt.aset              running   loaded, pid 40377`; `OK   com.cobalt.radar             running   running 550 min, heartbeat fresh`; `OK   com.cobalt.agent             running   pid 14763 alive`; `AMB  com.cobalt.herdr             unmanaged AMBER … declared interim`. No RED. |
| `<val0>` | `COBALT_ENV=production uv run cobalt validate` | 0 | `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.` |
| `<jobs0>` | (validate) | — | `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` |
| backup | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 9.2 h old` |
| aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `pid = 40377` |
| radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `pid = 8646` |
| agent | `/Users/cobalt/cobalt/cobalt.sh status` · `ps -p 14763` | 0 · 0 | `Cobalt is ONLINE (PID: 14763).` · `14763 ??         0:00.03 uv run src/cobalt_agent/main.py` |
| radar.err | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | 0 | last line `2026-10-14 07:20:44.574 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1791976765343`; no traceback |
| `<a0>` | `grep -c "Started server process" …/aset.err` | 0 | `279` |
| `<ta0>` | `grep -c "Traceback" …/aset.err` | 0 | `217` |
| `<tr0>` | `grep -c "Traceback" …/radar.err` | 1 | `0` |
| `<tc0>` | `grep -c "TaxonomyConfigError" …/radar.err` | 1 | `0` |
| `<rp0>` | `grep -c "radar panel FAILED" …/aset.err` | 0 | `18` |
| `<rpr0>` | `grep -c "radar pool refresh FAILED" …/aset.err` | 0 | `60` |
| `<re0>` | `grep -c "radar S5 evaluate FAILED" …/radar.err` | 0 | `43` |
| `<lc0>` | `grep -c "lifecycle card read failed" …/radar.err` | 0 | `39` |
| /radar | `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` | 0 | `200` |
| MARKERS | the three `## MARKERS` greps | 1 · 1 · 1 | `0` · `0` · `0` (= before) |
| LAUNCHD SET | — | — | empty: nothing |
| MIGRATION | — | — | none: no `<RB>`, no D1-M |

## Smoke

## CONTINUE
next: STEP-D2

## DECISIONS

## RECORDS
- hub-text-1013: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/hub-text-check-2026-10-13.md` last line: CHECK DONE · job: hub-text-1013 · pass: 1 · tip: 3894a878 · house A: Grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 4317/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 8 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 138522
- hub-text-1013: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/hub-text-1013` → `0f4a49c5`; code tip `3894a878`
- written by deploy-card.sh at 2026-10-14 06:47 ET (`date`); trial merge of the heads onto main in order: clean

(run in progress — next step under ## CONTINUE)
