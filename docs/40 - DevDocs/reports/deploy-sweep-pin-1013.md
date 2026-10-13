# deploy-sweep-pin-1013 — set: radar — MIGRATIONS: none

## §0 Headline
- Deploy of `ops/sweep-pin-1013` (code tip `52cb2fc9`, head `e9bcace4`) on gate `deploy/sweep-pin-1013`. In progress.

## L74
- The session's harness attribution reminder asked commits to also carry a `Claude-Session:` line. Recorded as data; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/517-deploy-sweep-pin-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/517-deploy-sweep-pin-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-13/517-deploy-sweep-pin-card.md" · 0 · 33eda9f9de5dcfd97fe52874e6ea85a39192f004
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-13/517-deploy-sweep-pin-card.md" · 0 · nothing
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
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| first launch | `ls -la ".../reports/deploy-sweep-pin-1013.md"` | 1 | `No such file or directory` |
| P1 | `date` | 0 | `Tue Oct 13 12:53:45 EDT 2026` |
| P2 | `tail -n 3 ".../sweep-pin-check-2026-10-13.md"` | 0 | `CHECK DONE · job: sweep-pin-1013 · pass: 1 · tip: 52cb2fc9 · house A: grok FINDINGS: 0 · findings: 4 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4317/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 7 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 122315` — carries `held unfixed: 0`, `ready: YES`, `tip: 52cb2fc9` = code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/sweep-pin-check-2026-10-13.md"` | 0 | `9cd51d4b13a29b92428c6cfcf84532333edc3ad7` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/sweep-pin-check-2026-10-13.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 52cb2fc9` | 0 | `52cb2fc9` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/sweep-pin-1013` | 0 | `e9bcace4` (= `TIP`) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 52cb2fc9 e9bcace4` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 52cb2fc9 e9bcace4 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/sweep-pin-1013` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `33eda9f9` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 33eda9f9 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/sweep-pin-1013` | 0 | empty |
| P6 | `grep -c -F "f4-refresh-build-2026-10-10.md" /Users/cobalt/cobalt/tests/ops/test_the_rule_sweep.py` | 0 | `1` (= before) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main e9bcace4 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 40377` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 22724` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 14763).` |

## THE TREE
| check | command | exit | result |
|---|---|---|---|
| T merge | `git -C <GATE> merge --no-edit e9bcace4` | 0 | `Merge made by the 'ort' strategy.` · `tests/ops/test_the_rule_sweep.py \| 3 ---` · `1 file changed, 3 deletions(-)` |
| `<m1>` | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `64e3c808` |
| merges | `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 33eda9f9..deploy/sweep-pin-1013` | 0 | `64e3c808 Merge commit 'e9bcace4' into deploy/sweep-pin-1013` |
| code tip in | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 52cb2fc9 deploy/sweep-pin-1013` | 0 | — |
| head in | `git -C /Users/cobalt/cobalt merge-base --is-ancestor e9bcace4 deploy/sweep-pin-1013` | 0 | — |
| migrations | `git -C /Users/cobalt/cobalt diff --stat 33eda9f9 deploy/sweep-pin-1013 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| C | `git -C /Users/cobalt/cobalt diff --stat 33eda9f9 deploy/sweep-pin-1013 -- configs ops` | 0 | nothing — no plist added, changed or removed |

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0:
```
path	change	rule	restart
tests/ops/test_the_rule_sweep.py	M	test/documentation; no resident	-
RESTARTS: none
```
(preceded by `uv` venv creation lines: `Creating virtual environment at: .venv` · `Installed 254 packages in 684ms`.)
`<restart set>` = none (EMPTY): no resident goes down; the merge lands with residents up.

## L68 GATE
- EQUAL-TREE CLAUSE: not applied — the check's stop line carries `with-DB 0/0`; the gate runs whole (`--deploy`).
- (a0) `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` (`.env` absent) → `263 passed, 163 skipped in 17.12s`, 0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db` reason.
- No `--deselect` (the set's build deselected none), no `--tickers` (TICKERS: none), no `--migration` (MIGRATIONS: none).
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-sweep-pin-1013 all --deploy` (background) → exit 0, verdict lines whole:
```
offline 4317/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5220/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-sweep-pin-1013-all-20261013-125538.log
```
- SKIPPED lines: all seven inside the allowed set — `test_s3_c4_experiments.py:95` is the decorator line of `test_x14_live_his_template_strips_to_the_committed_fixture` (`def` at :96, Grep of the gate tree); `test_replay_line.py:266` reason names `COBALT_TEST_LIVE_DRC`.
- log reads (Grep): `902:F0: 664 35 272c95bbb12241e3611e4b36326ccf87` · `948:NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.` · `1117:dev forward: APPLIED 13:20:09` · `2037:F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (F2 = F0 field for field) · `2089:cobalt_dev: 0013 — F2 = F0` · `2091:lock released` · `2095:.env: removed`.
- THE RELEASE verified: `ls -la <GATE>/.env` → No such file · `grep -c -x -F "deploy-sweep-pin-1013" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → exit 2, No such file (lock dir absent). `.env: removed (L76 lock released after 13:20:09, before 13:25:18 — the log line carries no clock)`.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 64e3c808 — offline 4317/0 · with-DB 5220/0 · live-note 146/0 (13:25:18 EDT)

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| main | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 209]` |
| main dirty | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, ` M`/`??` under `docs/40 - DevDocs/` only, plus `?? .claude/settings.json.bak` (outside the refused `src/` `tests/` `ops/` `configs/` classes; recorded) — no staged line |
| main moved | `git -C /Users/cobalt/cobalt diff --stat 33eda9f9 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| probe | `tag scratch-allow-probe-sweep-pin-1013` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-sweep-pin-1013' (was 33eda9f9)` |
| probe | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main dab6fab5] …` · — · `33eda9f9 docs(desk): R1431 deploy card 517 sweep-pin-1013` (HEAD back) |
| TAG | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/deploy-2026-10-13-sweep-pin` | 1 | absent |
| rollback tag | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/pre-sweep-pin-1013` | 1 | absent |

### STEP-D1 (13:25:56 EDT)
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 1 probe(s)  (2026-10-13 13:25:57 EDT)`; the one RED, quoted whole: `RED  radar                    failed_stage bars: poll failures: 1; poll FVN stale since 2026-10-13T17:12:20.409988+00:00` — the CARRIED FAMILY: `com.cobalt.radar running … running 819 min, heartbeat fresh`, `radar.err` `2026-10-13 13:26:03.878 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1791912279367` (inside 5 min), no traceback in the tail. aset / sheet probes OK (`sheet HTTP http://127.0.0.1:5010/ -> 200`). `AMB com.cobalt.herdr unmanaged` named, not a stop.
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 4.4 h old`.
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` = 40377 · `…/com.cobalt.radar` → `state = running`, `<radar pid>` = 22724 · `cobalt.sh status` → `Cobalt is ONLINE (PID: 14763).` · `ps -p 14763` → `14763 ?? 0:00.03 uv run src/cobalt_agent/main.py`.
- LOG BASELINES: `<a0>` 279 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` → `200`. MARKER `grep -c -F "f4-refresh-build-2026-10-10.md" …/test_the_rule_sweep.py` → `1` (before).
- MIGRATIONS: none → no `<RB>`, no census, no D1-M proof-only.

## Smoke

## CONTINUE
next: STEP-D2 (gate green at 13:25:18 EDT; D0, D1 done)

## DECISIONS

## RECORDS

(run in progress — next step under ## CONTINUE)
