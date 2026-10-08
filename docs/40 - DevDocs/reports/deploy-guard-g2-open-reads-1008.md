# deploy guard-g2-open-reads-1008 · SET: none · MIGRATIONS: none

## §0 Headline
- Deploy of `ops/guard-g2-open-reads-1008` (tip `828f28dc`) on DEPLOY-HUB, card `prompts/2026-10-08/147-deploy-guard-g2-open-reads-card.md`.

## L74
- A system notice in this session asked for a `Claude-Session:` trailer on commits. Recorded once here as data; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/147-deploy-guard-g2-open-reads-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/147-deploy-guard-g2-open-reads-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-08/147-deploy-guard-g2-open-reads-card.md" · 0 · 87f9d3f3b3c56bb112175d3d2479e60e7357efea
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-08/147-deploy-guard-g2-open-reads-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R686 row · grep -n "^| R686 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 39:| R686 | 11:28 ET | HIS RULING (words R686, standing): every seat may run read-only production reads, no stamp; writes and secrets stay refused. Card `120`. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW; LAWS L62 at deploy |
RULING 2026-10-08 R686 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R686 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 4125ff02c9587ca901d9d5c418f378b8c77593a9
RULING 2026-10-08 R686 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | `ls -la <REPORT>` (first launch) | 1 | No such file or directory |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Thu Oct  8 12:51:53 EDT 2026` |
| P2 | `tail -n 3 ".../guard-g2-open-reads-check-2026-10-08.md"` | 0 | `CHECK DONE · job: guard-g2-open-reads-1008 · pass: 1 · tip: 828f28dc · … · held unfixed: 0 · … · suites: offline 3991/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 17 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 227244` — carries `held unfixed: 0`, `ready: YES`, `tip: 828f28dc` = code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/guard-g2-open-reads-check-2026-10-08.md"` | 0 | `37a36315ed8de4dbbba66c7bf9f9a7433be34df3` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "<same>"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 828f28dc` | 0 | `828f28dc` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/guard-g2-open-reads-1008` | 0 | `828f28dc` |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 828f28dc ops/guard-g2-open-reads-1008` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 828f28dc ops/guard-g2-open-reads-1008 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/guard-g2-open-reads-1008` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `87f9d3f3` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 87f9d3f3 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/guard-g2-open-reads-1008` | 0 | empty |
| P6 | `grep -c -F "def prod_read(" /Users/cobalt/cobalt/ops/desk/bare-guard.py` | 1 | `0` (before `0`) |
| P6 | `grep -c -F "def keychain_read(" /Users/cobalt/cobalt/ops/desk/bare-guard.py` | 1 | `0` (before `0`) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 828f28dc -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 37788` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 37799` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
| check | command | exit | result |
|---|---|---|---|
| merge | `git -C <GATE> merge --no-edit 828f28dc` | 0 | `Merge made by the 'ort' strategy.` — 4 files: build report (A), `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `tests/ops/test_bare_guard.py` |
| `<m1>` | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `0562f99f` |
| merges | `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 87f9d3f3..deploy/guard-g2-open-reads-1008` | 0 | `0562f99f Merge commit '828f28dc' into deploy/guard-g2-open-reads-1008` |
| ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 828f28dc deploy/guard-g2-open-reads-1008` | 0 | — |
| migrations | `git -C /Users/cobalt/cobalt diff --stat 87f9d3f3 deploy/guard-g2-open-reads-1008 -- src/cobalt/db_migrations` | 0 | nothing (none) |
| STEP-C | `git -C /Users/cobalt/cobalt diff --stat 87f9d3f3 deploy/guard-g2-open-reads-1008 -- configs ops` | 0 | ` ops/desk/bare-guard.py  \| 73 +++…` · ` ops/desk/desk-launch.sh \|  5 ++--` · ` 2 files changed, 60 insertions(+), 18 deletions(-)` — no plist added, modified or removed |

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (after uv created the gate `.venv`: `Installed 253 packages in 769ms`):
```
path	change	rule	restart
docs/40 - DevDocs/reports/guard-g2-open-reads-build-2026-10-08.md	A	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```
`<restart set>` = EMPTY (none). No `UNCLASSIFIED` row. MIGRATIONS none → no L66 conflict.

## L68 GATE
- EQUAL-TREE CLAUSE: not applied — the check's stop line carries `with-DB 0/0` (DB: none) → the gate runs whole (`--deploy`). No with-DB deselect named by the build report (its one `deselected` is a `-k g2` count in `tests/ops`). TICKERS none, MIGRATIONS none.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `261 passed, 163 skipped in 17.96s` (0 failed; with-DB skips).
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-guard-g2-open-reads-1008 all --deploy` → exit 0, verdict lines whole:
```
offline 3991/0
lock: waited 8 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4875/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-guard-g2-open-reads-1008-all-20261008-125326.log
```
- (c) every pass-1 SKIPPED line is in the allowed set; `test_s3_c4_experiments.py:95` is `test_x14_live_his_template_strips_to_the_committed_fixture` (read at `<GATE>/tests/cobalt/test_s3_c4_experiments.py:95-96`).
- (c2) log line 1090: `dev forward: APPLIED 13:25:41` (level 0013 already the top; nothing above it).
- log line 880: `F0: 664 35 272c95bbb12241e3611e4b36326ccf87`; line 1916: `cobalt_dev: 0013 — F2 = F0`.
- RELEASE: log 1917–1922 `lock released` · `.env: removed`; `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-guard-g2-open-reads-1008" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `0`.
- (e) live-note: log 1986–1987 `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …` (allowed) · `146 passed, 1 skipped`.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 0562f99f

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| main | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 117]` |
| main | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`; ` M` ×6 and `??` ×17 under `docs/40 - DevDocs/` (this report among them); `?? .claude/settings.json.bak` (see `## DECISIONS` 1). No staged line, no dirty `src/` `tests/` `ops/` `configs/` path. |
| main | `git -C /Users/cobalt/cobalt diff --stat 87f9d3f3 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| probe | `git -C /Users/cobalt/cobalt tag scratch-allow-probe-guard-g2-open-reads-1008` | 0 | — |
| probe | `git -C /Users/cobalt/cobalt tag -d scratch-allow-probe-guard-g2-open-reads-1008` | 0 | `Deleted tag 'scratch-allow-probe-guard-g2-open-reads-1008' (was 87f9d3f3)` |
| probe | `git -C /Users/cobalt/cobalt commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` | 0 | `[main a14dbba1] scratch: allowlist probe (reverted next line)` |
| probe | `git -C /Users/cobalt/cobalt reset --soft HEAD~1` | 0 | — |
| probe | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | `87f9d3f3 docs(desk): deploy card 147 guard-g2 open-reads (R587)` — HEAD back |
| tag | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/deploy-2026-10-08-guard-g2-open-reads` | 1 | free |
| tag | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/pre-guard-g2-open-reads-1008` | 1 | free |

### STEP-D1 (baseline, read-only)
| read | command | result |
|---|---|---|
| time | `date` | `Thu Oct  8 13:31:16 EDT 2026` |
| `<hb0>` | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-08 13:31:18 EDT)`; `OK   radar                    scanning (rth), members 50`; `OK   com.cobalt.aset              running   loaded, pid 37788`; `OK   com.cobalt.radar             running   running 1292 min, heartbeat fresh`; `AMB  com.cobalt.herdr             unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0) …` (declared interim). No RED. |
| `<val0>` | `COBALT_ENV=production uv run cobalt validate` | exit 0; `13 trade_def(s) validated OK from the vault.` · `Placement (docs/PLACEMENT.md): tree clean.` |
| `<jobs0>` | (same) | `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` |
| backup | `COBALT_ENV=production uv run cobalt backup status` | `newest snapshot: 2.8 h old` |
| aset | `launchctl print gui/501/com.cobalt.aset` | `state = running`, `pid = 37788` |
| radar | `launchctl print gui/501/com.cobalt.radar` | `state = running`, `pid = 37799` |
| agent | `/Users/cobalt/cobalt/cobalt.sh status` · `ps -p 22243` | `Cobalt is ONLINE (PID: 22243).` · `22243 ??         0:00.04 uv run src/cobalt_agent/main.py` |
| radar.err | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | last: `2026-10-08 13:31:11.852 \| INFO     \| cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791480584020` |
| `<a0>` | `grep -c "Started server process" …/aset.err` | `49` |
| `<ta0>` | `grep -c "Traceback" …/aset.err` | `2` |
| `<tr0>` | `grep -c "Traceback" …/radar.err` | `0` |
| `<tc0>` | `grep -c "TaxonomyConfigError" …/radar.err` | `0` |
| `<rp0>` | `grep -c "radar panel FAILED" …/aset.err` | `17` |
| `<rpr0>` | `grep -c "radar pool refresh FAILED" …/aset.err` | `59` |
| `<re0>` | `grep -c "radar S5 evaluate FAILED" …/radar.err` | `41` |
| `<lc0>` | `grep -c "lifecycle card read failed" …/radar.err` | `39` |
| curl | `curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/radar` | `200` |
| markers | `grep -c -F "def prod_read(" …/bare-guard.py` · `grep -c -F "def keychain_read(" …/bare-guard.py` | `0` · `0` (before values) |
| migration | — | MIGRATIONS none: no `<RB>`, no census, no D1-M |

## CONTINUE
next: STEP-D2 (D2.0 report commit)

## DECISIONS
1. ASK DESK: `?? .claude/settings.json.bak` on `main` is outside D0's ACCEPTED list and outside its REFUSED classes (not staged; not `src/` `tests/` `ops/` `configs/`). It was there at session start. Safe default taken: not a refusal — the file is untracked, outside the set's paths, and `merge --ff-only` does not touch it; recorded, deploy continues. [13:31:16]

(run in progress — next step under ## CONTINUE)
