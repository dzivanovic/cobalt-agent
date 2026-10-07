# deploy worktree-salvage-1007 · SET: none · MIGRATIONS: none

## §0 Headline
- Deploy of `ops/worktree-salvage-1007` (tip `71d34bd9`), RESTARTS per the tool, no migration. In progress.

## L74
- A system reminder in this session asked commits to end with a `Claude-Session:` line. Recorded as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (DEPLOY-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-07/96-deploy-worktree-salvage-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-07/96-deploy-worktree-salvage-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-07/96-deploy-worktree-salvage-card.md" · 0 · e884dd5157ff6c37e444cfdab6df88091aba3e8a
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-07/96-deploy-worktree-salvage-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-07 R613 row · grep -n "^| R613 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · 8:| R613 | 06:37 ET | HIS RULING (words: `cto-2026-10-07-words.md` R613): worktree cleanup is the desk's. Inspect, report, remove; real unsaved work becomes a side job first, nothing waits on him; the desk gets the remove command. | APPROVED — pending fold |
RULING 2026-10-07 R613 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R613 |" -- "docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · 02c6b37b7a4e33033071e35d977620deb0f93068
RULING 2026-10-07 R613 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · the row as grepped
AUTHORIZED
```
First launch: `ls -la "<REPORT>"` → `No such file or directory` (exit 1).

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Wed Oct  7 11:11:55 EDT 2026` |
| P2 | `tail -n 3 ".../worktree-salvage-check-2026-10-07.md"` | 0 | `CHECK DONE · job: worktree-salvage · pass: 1 · tip: 71d34bd9 · … · held unfixed: 0 · … · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 175727` — literals present, tip = code tip |
| P2 | `git log -1 --format=%H -- "<check>"` | 0 | `74b8bbce3bc0381e83ed5ecf7cb1f4e521fb2056` |
| P2 | `git diff --stat -- "<check>"` | 0 | nothing |
| P3 | `rev-parse --short=8 71d34bd9` | 0 | `71d34bd9` |
| P3 | `rev-parse --short=8 ops/worktree-salvage-1007` | 0 | `71d34bd9` |
| P3 | `merge-base --is-ancestor 71d34bd9 71d34bd9` | 0 | — |
| P3 | `diff --stat 71d34bd9 71d34bd9 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/worktree-salvage-1007` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `e884dd51` = `<m0>` |
| P5 | `merge-base --is-ancestor e884dd51 main` | 0 | — |
| P5 | `log --oneline main..deploy/worktree-salvage-1007` | 0 | empty |
| P6 | `grep -c -F "SALVAGED:" .../ops/desk/job-clean.sh` | 1 | `0` (= before) |
| P6 | `grep -c -F "def test_salvage_usage_names_the_salvage_form" .../tests/ops/test_gate_clean.py` | 1 | `0` (= before) |
| P7 | `diff --stat main 71d34bd9 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 64112` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 64129` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 71d34bd9` → `Merge made by the 'ort' strategy.` (3 files: `worktree-salvage-build-2026-10-07.md`, `ops/desk/job-clean.sh`, `tests/ops/test_gate_clean.py`; 769 insertions, 9 deletions)
- `rev-parse --short=8 HEAD` → `deb14f07` = `<m1>`
- `log --oneline --merges --first-parent e884dd51..deploy/worktree-salvage-1007` → `deb14f07 Merge commit '71d34bd9' into deploy/worktree-salvage-1007`
- `merge-base --is-ancestor 71d34bd9 deploy/worktree-salvage-1007` → exit 0
- `diff --stat e884dd51 deploy/worktree-salvage-1007 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none)
- STEP-C: `diff --stat e884dd51 deploy/worktree-salvage-1007 -- configs ops` → ` ops/desk/job-clean.sh | 166 +++…---` / ` 1 file changed, 157 insertions(+), 9 deletions(-)`. No plist added, changed or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (after a fresh `.venv`: `Installed 253 packages in 910ms`):
```
path	change	rule	restart
docs/40 - DevDocs/reports/worktree-salvage-build-2026-10-07.md	A	DOCS	-
ops/desk/job-clean.sh	M	operator script; no Cobalt reader	-
tests/ops/test_gate_clean.py	M	test/documentation; no resident	-
RESTARTS: none
```
`<restart set>` = EMPTY. No UNCLASSIFIED row. No resident goes down.

## L68 GATE
- EQUAL-TREE CLAUSE: not applied — the check's stop line carries `with-DB 0/0`; the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `261 passed, 163 skipped in 16.07s` (0 failed; skips are with-DB, `Postgres env settings not available` / `requires_db`).
- Deselects: the build report `worktree-salvage-build-2026-10-07.md` names none (`grep -c -F "deselect"` → `0`). TICKERS: none. MIGRATIONS: none (no `--migration`).
- `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-worktree-salvage-1007 all --deploy` → exit 0, verdict lines whole:
```
offline 3963/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4847/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-worktree-salvage-1007-all-20261007-111326.log
```
- (c) every SKIPPED line is inside the allowed set; `test_s3_c4_experiments.py:95` is the decorator of `def test_x14_live_his_template_strips_to_the_committed_fixture` (`grep -n -F` → line 96).
- (c2) log line 1089: `dev forward: APPLIED 11:36:26`. (f) log `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (line 879) = `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (line 1865) → `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: log line 1918 `lock released`; `.env: removed (L76 lock released, log line 1918)`. `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-worktree-salvage-1007" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → No such file (lock dir absent).
- (e) live-note `146 passed, 1 skipped` — the skip names `COBALT_TEST_LIVE_DRC` (allowed); none names `COBALT_LIVE_VAULT_ROOT`.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on deb14f07 — offline 3963/0 · with-DB 4847/0 · live-note 146/0 · `Wed Oct  7 11:41:27 EDT 2026`

## Deploy table
### D0
| check | command | exit | result |
|---|---|---|---|
| main | `status --short --branch` | 0 | `## main...origin/main [ahead 49]` |
| main | `status --porcelain` | 0 | ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, ` M`/`??` under `docs/40 - DevDocs/` only (incl. ` M .../reports/cto-2026-10-07.md`, ` M .../prompts/2026-10-07/89-radar-direction-color-card.md`), `?? .claude/settings.json.bak` — no staged line, no dirty `src/`/`tests/`/`ops/` path |
| main | `diff --stat e884dd51 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| probe | `tag scratch-allow-probe-worktree-salvage-1007` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-worktree-salvage-1007' (was e884dd51)` |
| probe | `commit --allow-empty -m "scratch: …"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main acc1830b] scratch: allowlist probe (reverted next line)` · — · `e884dd51 docs(desk): salvage CHECK DONE 71d34bd9, deploy card 96, R634` |
| tags | `rev-parse --verify --quiet refs/tags/deploy-2026-10-07-worktree-salvage` | 1 | free |
| tags | `rev-parse --verify --quiet refs/tags/pre-worktree-salvage-1007` | 1 | free |

### D1 (`Wed Oct  7 11:41:50 EDT 2026`)
- `<hb0>`: `HEARTBEAT RED — 1 probe(s)  (2026-10-07 11:41:52 EDT)`; the one RED: `RED  radar                    failed_stage bars: poll failures: 1` — the CARRIED FAMILY (radar `running   running 1017 min, heartbeat fresh`; `radar.err` `2026-10-07 11:41:06.699 | INFO | cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791387584669`, inside 5 min of `11:42:03`, no traceback in the tail). Every other probe OK, `AMB com.cobalt.herdr … unmanaged` (declared interim). aset / sheet probes OK.
- `<val0>`: exit 0; `13 trade_def(s) validated OK`; `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 3.9 h old` (ssd ARMED).
- aset `state = running`, `pid = 64112`, path `/Users/cobalt/cobalt/ops/com.cobalt.aset.plist`; radar `state = running`, `pid = 64129`; `Cobalt is ONLINE (PID: 22243).`; `ps -p 22243` → `22243 ?? 0:00.04 uv run src/cobalt_agent/main.py`.
- Baselines: `<a0>` 47 · `<ta0>` 2 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 17 · `<rpr0>` 58 · `<re0>` 40 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS → `0`, `0` (= before). No migration: no `<RB>`, no D1-M.

## Smoke

## CONTINUE
next: STEP-D0 (gate green at 11:41:27) — D0, D1 done; next: D2.0

## DECISIONS

## RECORDS

(run in progress — next step under ## CONTINUE)
