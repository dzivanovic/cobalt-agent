# deploy-freeze-1015 — SET: none — MIGRATIONS: none

## §0 Headline
- Deploy of `ops/deploy-freeze-1014` (`b544abfb`), card `prompts/2026-10-15/601-deploy-freeze-card.md`. In progress.

## L74
- A system reminder that arrived mid-run (2026-10-15 13:05 ET, after the hub's Read) asked commits to carry a `Claude-Session:` line. It is recorded here as data and not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/601-deploy-freeze-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/601-deploy-freeze-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-15/601-deploy-freeze-card.md" · 0 · 5a8cad6695a53cdd0f4853f8bda7c585c13cf41a
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-15/601-deploy-freeze-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-14 R1471 row · grep -n "^| R1471 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 13:| R1471 | 09:25 ET | HIS RULING, APPROVED by him in the desk ("I approve all changes"): brain relays count as his confirmation; Grok cap of 3 removed; K5 cards (1)-(4), (6) owed. Words: `cto-2026-10-14-words.md`. | APPLIED: LAWS L79, checklist L15 at 09:40 |
RULING 2026-10-14 R1471 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1471 |" -- "docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 8b813ca721cd934ebfb82cc59d27495d15f1c79a
RULING 2026-10-14 R1471 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| first launch | `ls -la "…/reports/deploy-deploy-freeze-1015.md"` | 1 | `No such file or directory` |
| P1 | `date` | 0 | `Thu Oct 15 13:05:07 EDT 2026` (outside 21:30-22:30) |
| P2 | `tail -n 3 "…/reports/deploy-freeze-check-2026-10-14.md"` | 0 | `CHECK DONE · job: deploy-freeze-1014 · pass: 1 · tip: b544abfb · house A: Grok FINDINGS: 0 · findings: 2 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8090/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 16 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 173194` — carries `held unfixed: 0`, `ready: YES`, `tip: b544abfb` |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/deploy-freeze-check-2026-10-14.md"` | 0 | `73258a310cc1b2ed7fc16d4291395ec30bcbd028` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/…/deploy-freeze-check-2026-10-14.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 b544abfb` | 0 | `b544abfb` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/deploy-freeze-1014` | 0 | `b544abfb` |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor b544abfb ops/deploy-freeze-1014` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat b544abfb ops/deploy-freeze-1014 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` (no lock holder) |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/deploy-freeze-1015` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `5a8cad66` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 5a8cad66 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/deploy-freeze-1015` | 0 | empty |
| P6 | `grep -c -F "deploy-shipped.sh" …/prompts/DEPLOY-HUB.md` | 1 | `0` (before `0`) |
| P6 | `grep -c -F "deploy-shipped.sh" /Users/cobalt/cobalt/ops/desk/pre-commit` | 1 | `0` (before `0`) |
| P6 | `ls /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh` | 1 | `No such file or directory` (before) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main b544abfb -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 40377` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 8646` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 14763).` |

## THE TREE
- `git -C <GATE> merge --no-edit b544abfb` → `Merge made by the 'ort' strategy.` (6 files: `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `reports/deploy-freeze-build-2026-10-14.md`, `.result`, `ops/desk/deploy-shipped.sh`, `ops/desk/pre-commit`, `tests/ops/test_deploy_freeze_1014.py`; 673 insertions, 7 deletions)
- `git -C <GATE> rev-parse --short=8 HEAD` → `2232a194` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 5a8cad66..deploy/deploy-freeze-1015` → `2232a194 Merge commit 'b544abfb' into deploy/deploy-freeze-1015`
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor b544abfb deploy/deploy-freeze-1015` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat 5a8cad66 deploy/deploy-freeze-1015 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none)
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 5a8cad66 deploy/deploy-freeze-1015 -- configs ops` →
```
 ops/desk/deploy-shipped.sh | 103 +++++++++++++++++++++++++++++++++++++++++++++
 ops/desk/pre-commit        |  52 ++++++++++++++++++++---
 2 files changed, 150 insertions(+), 5 deletions(-)
```
- `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 5a8cad66 deploy/deploy-freeze-1015` → exit 0, `STEP-C: ADMITTED 0` → `<launchd set>` empty.

## RESTARTS
`COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` (in `<GATE>`, `.env` No such file) → exit 0 (after uv created the gate's `.venv`: `Installed 254 packages in 889ms`):
```
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/deploy-freeze-build-2026-10-14.md	A	DOCS	-
docs/40 - DevDocs/reports/deploy-freeze-build-2026-10-14.result	A	DOCS	-
ops/desk/deploy-shipped.sh	A	operator script; no Cobalt reader	-
ops/desk/pre-commit	M	operator script; no Cobalt reader	-
tests/ops/test_deploy_freeze_1014.py	A	test/documentation; no resident	-
RESTARTS: none
```
- `<restart set>` = EMPTY: no resident goes down; the merge lands with the residents up. `<launchd set>` = empty.

## L68 GATE
- Equal-tree clause: not applied (the check's stop line carries `with-DB 0/0`); the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 18.94s` (0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db` skip).
- Deselects: none (the build report's one `deselected` line is a `-k test_d1` run, not a with-DB deselect).
- `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-deploy-freeze-1015 all --deploy --deploy-gate` launched in the background (no `--tickers`, no `--migration`) → exit 0, verdict lines whole:
```
tests/ops: run (deploy gate)
offline 8095/0
lock: waited 15 min
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-deploy-freeze-1015-all-20261015-130705.log
```
- (a) offline `8095/0`; W line `tests/ops: run (deploy gate)`.
- (b) lock taken after `lock: waited 15 min`; `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log:972); proof-only at `0013`, nothing CHANGED.
- (c) pass 1 whole. Every SKIPPED line is inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`, the `test_replay_line.py` skip naming `COBALT_TEST_LIVE_DRC`, and `test_s3_c4_experiments.py:95` = `test_x14_live_his_template_strips_to_the_committed_fixture` (Read of `<GATE>/tests/cobalt/test_s3_c4_experiments.py:95-96`: `@requires_live` / `def test_x14_live_his_template_strips_to_the_committed_fixture():`).
- (c2) no migration above `0013` on this set: nothing applied forward.
- (c3)+(c) with-DB `5231/0`.
- (f) `cobalt_dev: 0013 — F2 = F0` (log:2159; `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` log:2156).
- THE RELEASE: log:2160-2165 `release-devdb-lock.sh deploy-deploy-freeze-1015` → `lock released`, `.env: removed`; `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-deploy-freeze-1015" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- (e) live-note `146/0`; no skip naming `COBALT_LIVE_VAULT_ROOT` in that leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 2232a194

## Deploy table
### STEP-D0
| row | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 116]` |
| MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | no staged line; ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, ` M` / `??` under `docs/40 - DevDocs/`, and `?? .claude/settings.json.bak` (outside `src/` `tests/` `ops/` `configs/`: not refused; present at session start) |
| MAIN | `git -C /Users/cobalt/cobalt diff --stat 5a8cad66 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `tag scratch-allow-probe-deploy-freeze-1015` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-deploy-freeze-1015' (was 5a8cad66)` |
| PROBE | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main c9574f5e] …` · — · `5a8cad66 docs(card): 601 deploy-freeze deploy card, R1594` |
| TAGS | `rev-parse --verify --quiet refs/tags/deploy-2026-10-15-deploy-freeze` · `… refs/tags/pre-deploy-freeze-1015` | 1 · 1 | free |

### STEP-D1 (baseline)
| row | command | result |
|---|---|---|
| `<hb0>` | `date` · `COBALT_ENV=production uv run cobalt heartbeat show` | `Thu Oct 15 14:07:41 EDT 2026` · `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-15 14:07:42 EDT)`; `OK   radar  scanning (rth), members 50`; `OK   com.cobalt.radar  running   running 2397 min, heartbeat fresh`; `AMB  com.cobalt.herdr  unmanaged AMBER …` (declared interim); no RED |
| `<val0>` | `COBALT_ENV=production uv run cobalt validate` | exit 0; `13 trade_def(s) validated OK from the vault.`; `Placement (docs/PLACEMENT.md): tree clean.` |
| `<jobs0>` | (validate) | `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` |
| backup | `COBALT_ENV=production uv run cobalt backup status` | `newest snapshot: 2.0 h old` |
| aset | `launchctl print gui/501/com.cobalt.aset` | `state = running`, `pid = 40377` |
| radar | `launchctl print gui/501/com.cobalt.radar` | `state = running`, `pid = 8646` |
| agent | `/Users/cobalt/cobalt/cobalt.sh status` · `ps -p 14763` | `Cobalt is ONLINE (PID: 14763).` · `14763 ??  0:00.03 uv run src/cobalt_agent/main.py` |
| radar.err | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | last line `2026-10-15 14:07:03.348 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792087537286`; no traceback |
| counts | `grep -c` | `<a0>` 279 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39 |
| curl | `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` | `200` |
| markers | the three `## MARKERS` | `0` · `0` · `No such file or directory` (before values) |
| launchd set | — | empty: nothing |
| migration | — | MIGRATIONS: none: no `<RB>`, no proof-only |

## Smoke

## CONTINUE
- next: STEP-D2 (D2.0 report commit)

## DECISIONS

## RECORDS

(run in progress — next step under ## CONTINUE)
