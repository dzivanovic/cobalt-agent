# deploy worktree-salvage-1007 · SET: none · MIGRATIONS: none

## §0 Headline
- DEPLOYED `ops/worktree-salvage-1007` (tip `71d34bd9`): main `d4742df8` → `3a994357`, tag `deploy-2026-10-07-worktree-salvage`.
- Gate green on `deb14f07`: offline 3963/0 · with-DB 4847/0 · live-note 146/0; `cobalt_dev` 0013, F2 = F0.
- RESTARTS: none — no resident touched; smoke GREEN; markers 4 and 1.
- No migration; snapshot `4e275389`; no decisions.

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

### D2
- D2.0 report committed `d4742df8` (`show --stat HEAD` → the one report file, 132 insertions). `<pre-merge>` = `d4742df8`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `<stack-final>` = `3a994357`; `3a994357^2` → `d4742df8` = `<pre-merge>`; `merge-base --is-ancestor deb14f07 3a994357` → exit 0.
- D2.3 `diff --stat deb14f07 3a994357 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- D2.4 `backup status` before → `newest snapshot: 3.9 h old`; `backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 5525.9 MB` · `ssd: snapshot 4e275389 — 14 new / 2 changed, 228.4 MB added, 1 pruned`; `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `Wed Oct  7 11:43:44 EDT 2026` → `HEARTBEAT RED — 1 probe(s)  (2026-10-07 11:43:46 EDT)` (114 s after D1's 11:41:52); the one RED `RED  radar  failed_stage bars: poll failures: 1; poll RIBB stale since 2026-10-07T15:36:42.957456+00:00` — the carried family; radar `running 1019 min, heartbeat fresh`. No new RED on aset or radar. (Earlier fill reads 11:43:22, :29, :34, :40 alike.)
- D2.6 `Wed Oct  7 11:43:49 EDT 2026` · `tag pre-worktree-salvage-1007` at `d4742df8`.

### STEP-4 (restart set EMPTY: no resident down)
- 4.1 `Wed Oct  7 11:44:00 EDT 2026` = `<t down>` = `<t up>` (empty set).
- 4.2 nothing booted out (empty set).
- 4.3 `rev-parse --short=8 HEAD` → `d4742df8` = `<pre-merge>`; `merge --ff-only deploy/worktree-salvage-1007` → `Updating d4742df8..3a994357` / `Fast-forward` (3 files, 769 insertions, 9 deletions).
- 4.4 `migrations applied: none`.
- 4.5 `validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`.
- 4.6 nothing to bootstrap. Downtime: none.

### STEP-7 close
| item | value |
|---|---|
| main | `<pre-merge>` `d4742df8` → `<stack-final>` `3a994357` (`rev-parse --short=8 main` → `3a994357`) |
| tags | rollback `pre-worktree-salvage-1007` at `d4742df8`; green `deploy-2026-10-07-worktree-salvage` at `3a994357` (set after green smoke) |
| `<t down>` / `<t up>` / seconds | none (empty set; merge at 11:44:00) |
| uv sync | none in production; the gate's fresh `.venv` in `<GATE>` (`Installed 253 packages in 910ms`) |
| proof cost | n/a (MIGRATIONS: none) |
| migrations applied | none |
| `<RB>` before / after | n/a |
| snapshot | `4e275389` (ssd) |
| RESTARTS done | none |
| ROLLBACK STRING | 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 3a994357` (no resident in the set). 2. SCHEMA: none. 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`. |

PRE-STOP SELF-CHECK: (1) every smoke row quoted with its `date` (11:44:09, 11:44:24, 11:45:32, 11:46:16, 11:47:01). (2) `rev-parse` of `71d34bd9` / `ops/worktree-salvage-1007` → `71d34bd9`; `merge-base --is-ancestor 71d34bd9 3a994357` → exit 0. (3) (h) shown above; every count and sha re-read this run. (4) STEP-T `Merge made by the 'ort' strategy.`, no conflict. THE RELEASE: the lock was released by `gate.sh` (log line 1918); `<GATE>/.env` absent.

## Smoke
- FIRST CALLS: `<rp_up>` 17 · `<rpr_up>` 58 · `<re_up>` 40 · `<lc_up>` 39.
- (a) `Wed Oct  7 11:44:09 EDT 2026`: aset `state = running`, `pid = 64112` (SAME, outside the set); radar `state = running`, `pid = 64129` (SAME); `Cobalt is ONLINE (PID: 22243).` (same). GREEN.
- (b) `Started server process` 47 = `<a0>` (aset outside the set); aset Traceback 2 = `<ta0>`; radar Traceback 0 = `<tr0>`; TaxonomyConfigError 0 = `<tc0>`.
- (b) radar tail 1 `Wed Oct  7 11:45:32 EDT 2026` (`<t up>` + 92 s): `tail -n 12 …/radar.err` → last line `2026-10-07 11:44:08.568 | INFO | cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791387766710` (stamped after `<t up>` 11:44:00); the other 11 lines `cards.expire: falling back to the session close (16:00:00) …` INFO; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → SETTLED GREEN.
- (c) `/` → `200` · `/radar` → `200` · `/radar\?frame=phone` → `200`. GREEN.
- (d) MARKERS: `SALVAGED:` in `job-clean.sh` → `4` (after `4`) · `def test_salvage_usage_names_the_salvage_form` → `1` (after `1`). GREEN.
- (f) validate as 4.5 · `jobs restarts d4742df8..3a994357` → exit 0, three rows (DOCS / operator script / test), `RESTARTS: none` = STEP-R's set, no UNCLASSIFIED. GREEN.
- (g) no migration.
- (s) salvage form: `grep -c -F "SALVAGED:" …/job-clean.sh` → exit 0, `4` (≥1) GREEN · W1 test present: `grep -c -F "def test_salvage_usage_names_the_salvage_form" …/test_gate_clean.py` → exit 0, `1` (≥1) GREEN. The W1 test ran in the gate (offline 3963/0).
- (e) read 1 `Wed Oct  7 11:44:24 EDT 2026` → `HEARTBEAT RED — 1 probe(s)  (2026-10-07 11:44:25 EDT)`, the one RED `failed_stage bars: poll failures: 2; poll RIBB stale since 2026-10-07T15:36:42.957456+00:00` (carried family); radar `running 1019 min, heartbeat fresh`.
- (h) REVERT-READBACK `Wed Oct  7 11:47:01 EDT 2026` (`<t up>` + 181 s, after (b) settled): `radar panel FAILED` 17 = `<rp_up>` · `radar pool refresh FAILED` 58 = `<rpr_up>` · `radar S5 evaluate FAILED` 40 = `<re_up>` · `lifecycle card read failed` 39 = `<lc_up>` — no growth; `/radar` → `200`. No `census` line on the card. GREEN.
- THE CHAIN: every check committed (P2: `74b8bbce…`) → the tips re-read (P3: `71d34bd9`) → the merged tree (T: `deb14f07`) → RESTARTS derived (R: none) → three suites green on `deb14f07` (G: offline 3963/0 · with-DB 4847/0 · live-note 146/0) → `<stack-final>` `3a994357` = `<m1>` + docs (D2.3) → the landed code (4.3: `d4742df8..3a994357`) → markers (d: 4, 1) → no migration (g) → residents up, same pids (a) → radar cycling (b, e) → the set's reads (s) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).
- SMOKE: GREEN.
- (e) read 2 `Wed Oct  7 11:46:16 EDT 2026` → `HEARTBEAT RED — 1 probe(s)  (2026-10-07 11:46:18 EDT)` (113 s after read 1), the one RED `failed_stage bars: poll failures: 2; poll RIBB stale since 2026-10-07T15:36:42.957456+00:00` (carried family, not new); `com.cobalt.radar running 1021 min, heartbeat fresh`. No RED outside `<hb0>`'s family. GREEN. (Fill reads 11:44:43 – 11:46:13 alike.)

## CONTINUE
next: STEP-D0 (gate green at 11:41:27) — D0, D1 done; next: D2.0
OUTAGE STARTING 11:43:49 — residents of (empty set: none) going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
next: none — run closed green (STEP-7).

## DECISIONS
none

## RECORDS
- Downtime: none (restart set EMPTY; no resident went down; aset 64112, radar 64129, agent 22243 unchanged).
- REFUSED, not needed: none. Messages not followed: none (no CONTINUE message arrived).
- `cobalt_dev: 0013 (F2 = F0)` — `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` = `F2: 664 35 272c95bbb12241e3611e4b36326ccf87`; lock released by `gate.sh` (log line 1918).
- RETIRE OWED: none (no plist removed).
- Carried RED as read: `RED  radar  failed_stage bars: poll failures: <1|2>; poll RIBB stale since 2026-10-07T15:36:42.957456+00:00` — the carried family at D1, D2.5 and smoke (e); radar running, heartbeat fresh, cycling.
- Cleanup owed (L46): gate worktree `/Users/cobalt/cobalt-wt/deploy-worktree-salvage-1007` and branch `deploy/worktree-salvage-1007`; the set's branch `ops/worktree-salvage-1007` and its worktree if one exists.
- L74: a system reminder asked for a `Claude-Session:` trailer on commits; recorded once, not acted on.
- Card `## RECORDS` (the desk's, copied):
  - worktree-salvage: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/worktree-salvage-check-2026-10-07.md` last line: CHECK DONE · job: worktree-salvage · pass: 1 · tip: 71d34bd9 · house A: Sol FINDINGS: 3 · findings: 7 · dropped: 0 · held: 4 · fixed: 4 · held unfixed: 0 · open: 2 · house B: Grok FINDINGS: 2 · suites: offline 3963/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 175727
  - worktree-salvage: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/worktree-salvage-1007` → `71d34bd9`; code tip `71d34bd9`
  - written by deploy-card.sh at 2026-10-07 11:11 ET (`date`); trial merge of the heads onto main in order: clean

DEPLOYED deploy-2026-10-07-worktree-salvage 3a994357 | set: none | migrations: none | gate: offline 3963/0 · with-DB 4847/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 0 · for Dejan: 0 · tokens: 183657
