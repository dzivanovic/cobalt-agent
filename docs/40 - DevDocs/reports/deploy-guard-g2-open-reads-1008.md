# deploy guard-g2-open-reads-1008 · SET: none · MIGRATIONS: none

## §0 Headline
- DEPLOYED `ops/guard-g2-open-reads-1008` (tip `828f28dc`): `main` `022d2c4c` → `f37e88d8`, tag `deploy-2026-10-08-guard-g2-open-reads`.
- Gate green on `0562f99f`: offline 3991/0 · with-DB 4875/0 · live-note 146/0; `cobalt_dev` 0013, F2 = F0, lock released.
- RESTARTS: none — no resident went down; migrations: none; snapshot `6cdcfa7a`.
- Smoke GREEN: markers `prod_read` / `keychain_read` 0 → 1; failure counts flat; radar cycling; all three curls 200.
- Decisions: 1 (untracked `.claude/settings.json.bak` on main, not a refusal) · for Dejan: 0.

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

### STEP-D2
| step | command | exit | result |
|---|---|---|---|
| D2.0 | `git -C /Users/cobalt/cobalt add "docs/40 - DevDocs/reports/deploy-guard-g2-open-reads-1008.md"` · `git -C /Users/cobalt/cobalt commit -m "docs(report): deploy guard-g2-open-reads-1008 — gate green on 0562f99f" …` | 0 | `[main 022d2c4c] docs(report): deploy guard-g2-open-reads-1008 — gate green on 0562f99f` |
| D2.0 | `git -C /Users/cobalt/cobalt show --stat HEAD` | 0 | one file: `.../reports/deploy-guard-g2-open-reads-1008.md \| 151 +++` |
| D2.0 | `git -C /Users/cobalt/cobalt rev-parse --short=8 main` | 0 | `022d2c4c` = `<pre-merge>` |
| D2.1 | `git -C <GATE> merge --no-edit main` | 0 | `Merge made by the 'ort' strategy.` (the report only) |
| D2.2 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `f37e88d8` = `<stack-final>` |
| D2.2 | `git -C /Users/cobalt/cobalt rev-parse --short=8 f37e88d8^2` | 0 | `022d2c4c` = `<pre-merge>` |
| D2.2 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 0562f99f f37e88d8` | 0 | — |
| D2.3 | `git -C /Users/cobalt/cobalt diff --stat 0562f99f f37e88d8 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing — docs only |
| D2.4 | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 2.8 h old` |
| D2.4 | `COBALT_ENV=production uv run cobalt backup run` | 0 | `backup: cobalt_brain via pg_dump inside cobalt_memory — 6015.7 MB` · `ssd: snapshot 6cdcfa7a — 0 new / 3 changed, 145.9 MB added, 1 pruned` |
| D2.4 | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 0.0 h old` |
| D2.5 | `date` · `COBALT_ENV=production uv run cobalt heartbeat show` | 0 | `13:33:09` · `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-08 13:33:11 EDT)` — 113 s after D1's 13:31:18; no RED |
| D2.6 | `date` · `git -C /Users/cobalt/cobalt tag pre-guard-g2-open-reads-1008` | 0 | `Thu Oct  8 13:33:15 EDT 2026` · tag at `022d2c4c` |

### STEP-4 (empty restart set: no resident down)
| step | command | exit | result |
|---|---|---|---|
| 4.1 | `date` | 0 | `Thu Oct  8 13:33:25 EDT 2026` = `<t down>` = `<t up>` (set empty) |
| 4.2 | — | — | set empty: no bootout, no stop |
| 4.3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` | 0 | `022d2c4c` = `<pre-merge>` |
| 4.3 | `git -C /Users/cobalt/cobalt merge --ff-only deploy/guard-g2-open-reads-1008` | 0 | `Updating 022d2c4c..f37e88d8` · `Fast-forward` · 4 files, 421 insertions(+), 42 deletions(-) |
| 4.4 | — | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | 0 | `13 trade_def(s) validated OK from the vault.` · `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>` · `Placement (docs/PLACEMENT.md): tree clean.` |
| 4.6 | — | — | set empty: nothing to bootstrap; downtime none |

## Smoke
`<t up>` = 13:33:25 (4.3's `date`; set empty).

| row | date | command | result | verdict |
|---|---|---|---|---|
| first counts | 13:33:41 (before (a)) | `grep -c` the four failure counts | `<rp_up>` 17 · `<rpr_up>` 59 · `<re_up>` 41 · `<lc_up>` 39 (= D1) | — |
| (a) | 13:33:41 | `launchctl print gui/501/com.cobalt.aset` · `…/com.cobalt.radar` · `/Users/cobalt/cobalt/cobalt.sh status` | aset `state = running` `pid = 37788` (SAME, outside the set) · radar `state = running` `pid = 37799` (SAME) · `Cobalt is ONLINE (PID: 22243).` (same) | GREEN |
| (b) aset | 13:33:45 | `grep -c "Started server process" …/aset.err` · `grep -c "Traceback" …/aset.err` · `grep -c "Traceback" …/radar.err` · `grep -c "TaxonomyConfigError" …/radar.err` · `tail -n 30 …/aset.err` | `49` = `<a0>` (aset outside the set) · `2` = `<ta0>` · `0` = `<tr0>` · `0` = `<tc0>` · tail: no new `Started server process`, no traceback (its lines are vault-note write logs, not quoted here) | GREEN |
| (c) | 13:33:51 | `curl … http://127.0.0.1:5010/` · `…/radar` · `…/radar\?frame=phone` | `200` · `200` · `200` | GREEN |
| (d) | 13:33:51 | `grep -c -F "def prod_read(" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · `grep -c -F "def keychain_read(" …` | `1` · `1` (after `1`, `1`) | GREEN |
| (s) | 13:33:51 | `grep -c -F "def prod_read(" …/bare-guard.py` · `grep -c -F "def is_secret(" …/bare-guard.py` | `1` · `1` (exit 0, ≥1 each) | GREEN |
| (f) | 13:33:59 | `COBALT_ENV=production uv run cobalt jobs restarts 022d2c4c..f37e88d8` | the same four rows as STEP-R · `RESTARTS: none` = `<restart set>`, no `UNCLASSIFIED` | GREEN |
| (f) | 13:34:06 | `COBALT_ENV=production uv run cobalt validate` | exit 0 · `13 trade_def(s) validated OK from the vault.` · `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` · `Placement (docs/PLACEMENT.md): tree clean.` | GREEN |
| (e) 1 | 13:33:59 | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-08 13:33:59 EDT)` · `com.cobalt.radar running running 1295 min, heartbeat fresh` | — |
| (b) radar tail 1 | 13:34:56 (`<t up>` + 91 s) | `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` | last: `2026-10-08 13:34:19.849 \| INFO     \| cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791480771872` — a cycle line after `<t up>`, no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback | GREEN (settled) |
| (e) 2 | 13:35:48 | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-08 13:35:50 EDT)` — 111 s after (e) 1 · `com.cobalt.radar running running 1296 min, heartbeat fresh`; no RED not in `<hb0>` | GREEN |
| (h) | 13:36:25 (`<t up>` + 180 s) | the four failure counts · `curl … /radar` · `tail -n 12 …/radar.err` · `grep -c "Traceback" …/radar.err` | `17` · `59` · `41` · `39` = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (no growth) · `200` · last cycle line unchanged `13:34:19.849 … radar cycle: scanning` · `0` | GREEN |

Between (e) 1 and (e) 2 the clock was filled with `date` + `heartbeat show` pairs (13:34:11 → 13:36:21); every read `HEARTBEAT GREEN … nothing red`.

THE CHAIN: every check committed (P2: `37a36315`, clean) · the tips (P3: `828f28dc` = head) · the merged tree (T: `0562f99f`, one merge, no migration) · RESTARTS derived (R: none) · three suites green on `0562f99f` (G: offline 3991/0, with-DB 4875/0, live-note 146/0) · `<stack-final>` `f37e88d8` = `<m1>` + docs (D2.3: nothing outside docs) · the landed code (4.3: `Updating 022d2c4c..f37e88d8` Fast-forward) · markers (d: 1, 1) · no migration (g: n/a) · residents unchanged and up (a: same pids 37788 / 37799 / 22243) · radar cycling (b, e) · the set's reads (s: 1, 1) · no new failure (h: counts flat). The card surface is not readable here; the desk confirms it with him (L70).

### STEP-7
| item | value |
|---|---|
| merge | `<pre-merge>` `022d2c4c` → `<stack-final>` `f37e88d8` (`main` tip `f37e88d8`) |
| tags | `pre-guard-g2-open-reads-1008` at `022d2c4c` · `deploy-2026-10-08-guard-g2-open-reads` at `f37e88d8` (after green smoke) |
| `<t down>` / `<t up>` / seconds | none (empty restart set) — 13:33:25 merge time |
| uv sync line | none in production calls; the gate worktree's first `uv run` created its own `.venv` (`Installed 253 packages in 769ms`) |
| proof cost | n/a (no migration; the gate's dev proof-only: `Proof cost: total 5.3 s`) |
| migrations applied | none |
| `<RB>` before / after | n/a |
| snapshot | `6cdcfa7a` |
| RESTARTS done | none |
| ROLLBACK STRING | 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 f37e88d8` (no resident to take down: restart set empty). 2. SCHEMA: none. 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`. |

PRE-STOP SELF-CHECK: (1) every smoke row above is quoted with its `date`. (2) `828f28dc` re-read at P3 (`rev-parse` → `828f28dc`, head the same); `git -C /Users/cobalt/cobalt merge-base --is-ancestor 828f28dc f37e88d8` → exit 0. (3) REVERT-READBACK (h) shown; every count, sha and line above came from tool output in this run. (4) STEP-T merged clean (`Merge made by the 'ort' strategy.`); D2.1 clean; no conflict marker.

## CONTINUE
OUTAGE STARTING 13:33:15 — residents of none (empty restart set) going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
- 4.6 ended 13:33:25 (nothing down). Smoke GREEN 13:36:25. next: none — DEPLOYED.

## DECISIONS
1. ASK DESK: `?? .claude/settings.json.bak` on `main` is outside D0's ACCEPTED list and outside its REFUSED classes (not staged; not `src/` `tests/` `ops/` `configs/`). It was there at session start. Safe default taken: not a refusal — the file is untracked, outside the set's paths, and `merge --ff-only` does not touch it; recorded, deploy continues. [13:31:16]

## RECORDS
- Downtime: none (restart set empty; no resident stopped). No line over 300 s.
- REFUSED, not needed: none. No `CONTINUE` message received; none followed.
- `cobalt_dev: 0013 (F2 = F0)` — gate log line 1916; `F0: 664 35 272c95bbb12241e3611e4b36326ccf87`; lock released (log 1918), `<GATE>/.env` absent. The gate waited 8 min for the lock (`lock: waited 8 min`).
- RETIRE OWED: none (no plist removed).
- Carried RED as read: none — `<hb0>` GREEN; the only non-OK row is `AMB com.cobalt.herdr … unmanaged` (declared interim), unchanged through smoke.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-guard-g2-open-reads-1008` and branch `deploy/guard-g2-open-reads-1008`; the set's branch `ops/guard-g2-open-reads-1008` (and its worktree, if any).
- Push is his (L55): `main` is at `f37e88d8` plus this report commit, ahead of `origin/main`; tags `pre-guard-g2-open-reads-1008` and `deploy-2026-10-08-guard-g2-open-reads` are local.
- L74: one system notice in this session asked for a `Claude-Session:` commit trailer; recorded under `## L74`, not acted on.
- Card `## RECORDS`, copied:
  - guard-g2-open-reads-1008: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/guard-g2-open-reads-check-2026-10-08.md` last line: CHECK DONE · job: guard-g2-open-reads-1008 · pass: 1 · tip: 828f28dc · house A: Sol FINDINGS: 4 · findings: 11 · dropped: 0 · held: 7 · fixed: 7 · held unfixed: 0 · open: 4 · house B: Grok FINDINGS: 3 · suites: offline 3991/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 17 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 227244
  - guard-g2-open-reads-1008: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/guard-g2-open-reads-1008` → `828f28dc`; code tip `828f28dc`
  - RESTARTS: none. Every path is under `ops/` or `tests/ops/` (the check's stop line: `RESTARTS: none`). No `src/` path, no migration, no resident.
  - written by deploy-card.sh at 2026-10-08 12:51 ET (`date`); trial merge of the heads onto main in order: clean

DEPLOYED deploy-2026-10-08-guard-g2-open-reads f37e88d8 | set: none | migrations: none | gate: offline 3991/0 · with-DB 4875/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 192431
