# deploy gemini-read-grant-1019 · SET: gemini-grant · MIGRATIONS: none

Card: `docs/40 - DevDocs/prompts/2026-10-19/849-deploy-gemini-read-grant-card.md` (committed `d1af946e`). Hub: `DEPLOY-HUB.md`. Seat: deploy-hub-gemini-read-grant-1019, Opus 5.5, `--permission-mode dontAsk`.

## §0 Headline
- DEPLOYED: `ops/gemini-read-grant-1019` (`7e165648`) is on `main` at `958ab78c`, tag `deploy-2026-10-19-gemini-read-grant-1019`. No migration, no resident restarted, no downtime.
- Gate green on `f93aef81`: offline 8818/0 · with-DB 5715/0 · live-note 147/0; `cobalt_dev` back at 0013 (F2 = F0).
- Smoke GREEN: the seven markers read `after`, x1-copy refuses a foreign worktree, heartbeat GREEN throughout, failure counts flat.
- One card smoke read ("sweep, dry") was not run: its `DESK_LAUNCH_DRY=1` prefix is not admitted on this line. It is UNPROVEN and owed to the desk (DECISION 3). Decisions: 3, for Dejan: 0.

## L74
- A session-start system reminder asked that commits end with a `Claude-Session:` line. Recorded here once and not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/849-deploy-gemini-read-grant-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/849-deploy-gemini-read-grant-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-19/849-deploy-gemini-read-grant-card.md" · 0 · d1af946e594893a6502e961913cdb1ebd74984ee
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-19/849-deploy-gemini-read-grant-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
RULING 2026-10-18 R1942 row · grep -n "^| R1942 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 30:| R1942 | 20:47 ET | HIS RULING · APPROVED (relayed by the brain 20:46, L79): "A for gemini" — a K5 card in which desk-launch.sh shadow adds and removes the one write_file rule in the agy settings.json; NEEDS HIS HAND entry closed. | APPLIED: areas/cobalt.md NOW at wake-up 01:57 |
RULING 2026-10-18 R1942 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1942 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 55d8b50e607b5d4eb1b86354e336323252aec34c
RULING 2026-10-18 R1942 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | `authorize.sh deploy "<card>"` | 0 | `AUTHORIZED` (above) |
| P1 | `date` | 0 | `Mon Oct 19 11:18:34 EDT 2026` — outside 21:30–22:30 |
| first launch | `ls -la "…/reports/deploy-gemini-read-grant-1019.md"` | 1 | `No such file or directory` |
| P2 | `tail -n 3 "…/reports/gemini-read-grant-1019-check-2026-10-19.md"` | 0 | `CHECK DONE · job: gemini-read-grant-1019 · pass: 1 · tip: 7e165648 · house A: Grok FINDINGS: 3 · findings: 4 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 1 · house B: none (not needed) · suites: offline 8799/0 · with-DB 0/0 · live-note 147/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 26 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 197976` — carries `held unfixed: 0` and `ready: YES`; `tip: 7e165648` = code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/…/gemini-read-grant-1019-check-2026-10-19.md"` | 0 | `f61601195541a6c4d3fadc573467313680896559` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/…/gemini-read-grant-1019-check-2026-10-19.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 7e165648` | 0 | `7e165648` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/gemini-read-grant-1019` | 0 | `7e165648` = row and `TIP` |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 7e165648 ops/gemini-read-grant-1019` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 7e165648 ops/gemini-read-grant-1019 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no holder |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/gemini-read-grant-1019` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `d1af946e` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor d1af946e main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/gemini-read-grant-1019` | 0 | empty |
| P6 | `grep -c -F "R2011: a Gemini call only from its worktree" …/ops/desk/bare-guard.py` | 1 | `0` = before |
| P6 | `grep -c -F "kind x1-copy: the X1 leg's agy transcript" …/ops/desk/desk-launch.sh` | 1 | `0` = before |
| P6 | `grep -c -F "a Gemini call only while the seat's cwd is exactly <worktree> (R2011)" …/SHADOW-HUB.md` | 1 | `0` = before |
| P6 | `grep -c -F "leg 0f, the outside-cwd leg" …/SHADOW-HUB.md` | 1 | `0` = before |
| P6 | `grep -c -F "one agy launch per leg, R2007" …/SHADOW-HUB.md` | 1 | `0` = before |
| P6 | `grep -c -F "X1 WRITE OK" …/SHADOW-HUB.md` | 0 | `1` = before |
| P6 | `grep -c -F "Run NO shell command and no URL fetch; read and write files with your file tools only; a denial ends your run." …/SHADOW-HUB.md` | 1 | `0` = before |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 7e165648 -- src/cobalt/db_migrations` | 0 | `0026_genesis_chunk.rollback.sql | 5 -----`, `0026_genesis_chunk.sql | 30 ---`, `__init__.py | 6 -----`, `placement.py | 4 ----` (4 files, 45 deletions) — ALL DELETIONS: `main`'s own 0026, newer than the branch base (see `## DECISIONS` 1) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main...7e165648 -- src/cobalt/db_migrations` | 0 | nothing — the head changes nothing under the folder since its base |
| P7 | `git -C /Users/cobalt/cobalt merge-base main 7e165648` | 0 | `0ac7746ecb5b801158f845188475ecc2d00d0bc7` |
| P7 | `git -C /Users/cobalt/cobalt log --oneline -3 -- src/cobalt/db_migrations/0026_genesis_chunk.sql` | 0 | `2cd0219a feat(f21-genesis-fr1): port Genesis chunk 1 …` (deployed `bc990598`) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, pid 35793 |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, pid 57565 |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 35845).` |

## THE TREE
- `git -C <GATE> merge --no-edit 7e165648` → `Merge made by the 'ort' strategy.` (8 files: `SHADOW-HUB.md`, the build report and `.result`, `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `tests/ops/test_bare_guard.py`, `tests/ops/test_desk_launch_shadow.py`, `tests/ops/test_shadow_hub_file.py`; 600 insertions, 12 deletions)
- `git -C <GATE> rev-parse --short=8 HEAD` → `f93aef81` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent d1af946e..deploy/gemini-read-grant-1019` → `f93aef81 Merge commit '7e165648' into deploy/gemini-read-grant-1019` (one line, one head)
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor 7e165648 deploy/gemini-read-grant-1019` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat d1af946e deploy/gemini-read-grant-1019 -- src/cobalt/db_migrations` → nothing: no migration path, `MIGRATIONS: none` holds (closes `## DECISIONS` 1 on the merged tree)
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat d1af946e deploy/gemini-read-grant-1019 -- configs ops` →
```
 ops/desk/bare-guard.py  |  5 ++-
 ops/desk/desk-launch.sh | 97 ++++++++++++++++++++++++++++++++++++++++++++++---
 2 files changed, 96 insertions(+), 6 deletions(-)
```
- `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" d1af946e deploy/gemini-read-grant-1019` → exit 0, whole: `STEP-C: ADMITTED 0` → `<launchd set>` empty, `<deferred set>` empty

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created the gate's `.venv`: `Installed 257 packages in 805ms`), table whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/SHADOW-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/gemini-read-grant-1019-build-2026-10-19.md	A	DOCS	-
docs/40 - DevDocs/reports/gemini-read-grant-1019-build-2026-10-19.result	A	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_shadow.py	M	test/documentation; no resident	-
tests/ops/test_shadow_hub_file.py	M	test/documentation; no resident	-
RESTARTS: none
```
- `<restart set>`: EMPTY (no `UNCLASSIFIED`) · `<deferred set>`: empty · `<launchd set>`: empty. No resident goes down; the merge lands with the residents up.

## L68 GATE
- Equal-tree clause: not applied — the check's stop line carries `with-DB 0/0` (DB: none), so the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `264 passed, 163 skipped in 20.72s` (0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db`).
- Deselects: none (the build report `gemini-read-grant-1019-build-2026-10-19.md` names no pass-1 with-DB deselect; its `deselected` lines are `-k` filters). `--tickers` omitted (`TICKERS: none`); no `--migration` (`MIGRATIONS: none`).
- `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-gemini-read-grant-1019 all --deploy --deploy-gate` → exit 0, verdict lines whole:
```
tests/ops: run (deploy gate)
offline 8818/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5715/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-gemini-read-grant-1019-all-20261019-112040.log
```
- (a) offline `8818/0`; W line `tests/ops: run (deploy gate)`.
- (c) PASS 1 skips: all eight inside the allowed set (`test_cards_picks.py:388`, `:401`; `test_playbook_live.py` `test_live_vault_renders_six_decks` with `COBALT_LIVE_VAULT_ROOT not set`; `test_radar_evaluate.py:695`; `test_replay_line.py` `COBALT_TEST_LIVE_DRC`; `test_s3_c4_experiments.py` X14 live template; `test_catalyst.py:365`; `test_predicate.py:262`).
- (c2) `dev forward: APPLIED 12:03:46` (log line 1262).
- (c3) `with-DB 5715/0`.
- (f) `cobalt_dev: 0013 — F2 = F0` — log `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (line 1038), `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (line 2280).
- THE RELEASE: `.env: removed` (L76 lock released, log line 2335 `lock released`, before live-note); `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-gemini-read-grant-1019" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- (e) `live-note 147/0` (`147 passed, 1 skipped` — the `COBALT_TEST_LIVE_DRC` skip, inside the set).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on f93aef81

## Deploy table
### STEP-D0 (12:08:56 →)
- `git -C /Users/cobalt/cobalt status --short --branch` → `## main...origin/main [ahead 145]`; `status --porcelain` → only ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, ` M`/`??` under `docs/40 - DevDocs/`, and `?? .claude/settings.json.bak` (DECISION 2). No staged line; no dirty `src/` `tests/` `ops/` `configs/` path but the accepted `rules.yaml`.
- `git -C /Users/cobalt/cobalt diff --stat d1af946e main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- ALLOWLIST PROBE: `tag scratch-allow-probe-gemini-read-grant-1019` → ok; `tag -d …` → `Deleted tag 'scratch-allow-probe-gemini-read-grant-1019' (was d1af946e)`; `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` → `[main 8d6be920] scratch: allowlist probe (reverted next line)`; `reset --soft HEAD~1` → ok; `log --oneline -1` → `d1af946e docs(desk): Gemini read-grant deploy card 849` (HEAD back).
- TAG NAMES: `rev-parse --verify --quiet refs/tags/deploy-2026-10-19-gemini-read-grant-1019` → exit 1; `… refs/tags/pre-gemini-read-grant-1019` → exit 1.

### STEP-D1 (12:09:23)
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT GREEN — 18 job(s), 14 probe(s), nothing red  (2026-10-19 12:09:25 EDT)`; `OK   radar                    scanning (rth), members 50`; `OK   com.cobalt.radar             running   running 57 min, heartbeat fresh`; `AMB  com.cobalt.herdr  unmanaged …` (declared interim); `com.cobalt.prefill-refresh` and `com.cobalt.playbook` `OWED (deferred bootstrap)` (standing, predate this run). No RED.
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0, `13 trade_def(s) validated OK from the vault.`, `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` `Jobs (F17): 18 registered — 7 resident, 11 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 1.1 h old` (ssd ARMED).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 35793`; `…/com.cobalt.radar` → `state = running`, `pid = 57565`; `cobalt.sh status` → `Cobalt is ONLINE (PID: 35845).`; `ps -p 35845` → `35845 ??         0:00.03 uv run src/cobalt_agent/main.py`.
- `tail -n 8 logs/radar.err` → last line `2026-10-19 12:08:59.794 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792426056851` (the seven above it `cards.expire: falling back to the session close` INFO lines); no traceback.
- LOG BASELINES: `<a0>` Started server process 284 · `<ta0>` aset Traceback 217 · `<tr0>` radar Traceback 0 · `<tc0>` TaxonomyConfigError 0 · `<rp0>` radar panel FAILED 18 · `<rpr0>` radar pool refresh FAILED 60 · `<re0>` radar S5 evaluate FAILED 43 · `<lc0>` lifecycle card read failed 39.
- `curl … /radar` → `200`. MARKERS again: `0`, `0`, `0`, `0`, `0`, `1`, `0` = every `before`.
- THE LAUNCHD SET: empty — nothing. No migration: no `<RB>`, no D1-M.

### STEP-D2
- D2.0: `deploy-shipped.sh --moved d1af946e "<card>"` → nothing · `add` + `commit … -- "<REPORT>"` → `[main ef97f609] docs(report): deploy gemini-read-grant-1019 — gate green on f93aef81` · `show --stat HEAD` → the one report file (`164 insertions(+)`) · `rev-parse --short=8 main` → `ef97f609` = `<pre-merge>`.
- D2.1: `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2: `<stack-final>` = `958ab78c`; `rev-parse --short=8 958ab78c^2` → `ef97f609` = `<pre-merge>`; `merge-base --is-ancestor f93aef81 958ab78c` → exit 0.
- D2.3: `diff --stat f93aef81 958ab78c -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing (docs only).
- D2.4: `backup status` → `newest snapshot: 1.1 h old` · `backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 9141.0 MB`, `ssd: snapshot e7b0a161 — 0 new / 2 changed, 93.4 MB added, 1 pruned`, `F17: com.cobalt.backup DONE` · `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 [12:11:40]: `heartbeat show` → `HEARTBEAT GREEN — 18 job(s), 14 probe(s), nothing red  (2026-10-19 12:11:41 EDT)` (136 s after D1's 12:09:25); no new RED.
- D2.6 [12:11:45]: `git -C /Users/cobalt/cobalt tag pre-gemini-read-grant-1019` at `ef97f609`.

### STEP-4 (`<restart set>` EMPTY)
- 4.1 `date` → `Mon Oct 19 12:11:56 EDT 2026` = `<t down>` (nothing goes down).
- 4.2: no label in the set — no bootout, no orphan-clean, no agent stop.
- 4.3: `rev-parse --short=8 HEAD` → `ef97f609` = `<pre-merge>` · `git -C /Users/cobalt/cobalt merge --ff-only deploy/gemini-read-grant-1019` → `Updating ef97f609..958ab78c` / `Fast-forward` (8 files, 600 insertions, 12 deletions).
- 4.4: `migrations applied: none`.
- 4.5: `COBALT_ENV=production uv run cobalt validate` → exit 0; `13 trade_def(s) validated OK from the vault.`; `Jobs (F17): 18 registered — 7 resident, 11 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`; `Placement (docs/PLACEMENT.md): tree clean.`
- 4.6: no label to bring up. `<t up>` = 12:11:56 (4.3's `date`, the set empty). Downtime: none. 4.6L: `<launchd set>` empty — nothing.

### SUMMARY (STEP-7.2)
- `<pre-merge>` `ef97f609` → `<stack-final>` `958ab78c` (main tip). Tags: `pre-gemini-read-grant-1019` (at `ef97f609`), `deploy-2026-10-19-gemini-read-grant-1019` (at `958ab78c`).
- `<t down>` / `<t up>` / seconds: none (empty set; 12:11:56 merge).
- uv sync line: none in production (the gate's `.venv` only: `Installed 257 packages in 805ms`). Proof cost: none (no migration). `migrations applied: none`. `<RB>`: none on the card.
- Snapshot: `e7b0a161` (ssd).
- RESTARTS done: none. LAUNCHD done: none. BOOTSTRAP OWED: none.
- THE ROLLBACK STRING (L54; the desk's): 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 958ab78c` — residents: none to take down (`<restart set>` empty); `<launchd set>` empty. 2. SCHEMA: none (no migration). 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

## Smoke
`<t up>` = 12:11:56 (4.3's `date`; the set empty). FIRST CALLS: `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 (= D1).
- (a) [12:12:12] `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 35793` (SAME as D1: outside the set) · `…/com.cobalt.radar` → `state = running`, `pid = 57565` (SAME) · `cobalt.sh status` → `Cobalt is ONLINE (PID: 35845).` (same pid). GREEN.
- (b) [12:12:12] `grep -c "Started server process" logs/aset.err` → `284` = `<a0>` (aset outside the set) · `tail -n 30 logs/aset.err` → aset card writes of 10:36 (`[WRITE] updated: …/2026-10-19.md · section=aset-cards · unit=card-20261019T103634 · write_id=5903`), no restart, no traceback · aset Traceback `217` = `<ta0>` · radar Traceback `0` = `<tr0>` · TaxonomyConfigError `0` = `<tc0>`. Radar tails: below.
- (c) [12:12:12] `curl … /` → `200` · `curl … /radar` → `200` · `curl … /radar\?frame=phone` → `200`. GREEN.
- (d) [12:12:12+] MARKERS: `bare-guard.py` R2011 → `1` · `desk-launch.sh` x1-copy → `1` · SHADOW-HUB R2011 cwd → `1` · `leg 0f, the outside-cwd leg` → `1` · `one agy launch per leg, R2007` → `1` · `X1 WRITE OK` → `0` · `Run NO shell command and no URL fetch; …` → `1`. Every `after`. GREEN.
- (s) read 1 "x1-copy refuses a foreign worktree" [12:12:12+] `sh /Users/cobalt/cobalt/ops/desk/desk-launch.sh x1-copy x1-canary 0a` → exit 1, stderr `REFUSED: x1-copy: worktree 'x1-canary' is never a job's` (holds `REFUSED: x1-copy`; wrote nothing). GREEN.
- (s) read 2 "sweep, dry" `DESK_LAUNCH_DRY=1 sh /Users/cobalt/cobalt/ops/desk/desk-launch.sh grant-sweep`: NOT RUN — UNPROVEN (L70); its `VAR=` prefix is not admitted on this line (DECISION 3). The landed `tests/ops` ran in the gate's offline `8818/0`.
- (f) [12:12:33−] `jobs restarts ef97f609..958ab78c` → exit 0, `RESTARTS: none` (= STEP-R's empty set), no `UNCLASSIFIED` · `validate` → exit 0, `13 trade_def(s) validated OK from the vault.`, `Jobs (F17): 18 registered — 7 resident, 11 one-shot. Kill phrase 'COBALT STOP'.`, `Placement (docs/PLACEMENT.md): tree clean.` GREEN.
- (g) no migration.
- (e) read 1 [12:12:33] `heartbeat show` → `HEARTBEAT GREEN — 18 job(s), 14 probe(s), nothing red  (2026-10-19 12:12:33 EDT)`; `com.cobalt.radar  running   running 60 min, heartbeat fresh`. Read 2 [12:14:24] → `HEARTBEAT GREEN — 18 job(s), 14 probe(s), nothing red  (2026-10-19 12:14:26 EDT)` (113 s after read 1); `com.cobalt.radar  running   running 62 min, heartbeat fresh`. No RED that `<hb0>` lacks. GREEN. (The clock between was filled with `date` + `heartbeat show` pairs, every one GREEN.)
- (b) radar tail 1 [12:13:28, `<t up>` + 92 s] `tail -n 12 logs/radar.err` → `2026-10-19 12:12:02.806 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792426239804` (after `<t up>` 12:11:56), the eleven lines above it `cards.expire: falling back to the session close` INFO; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → SETTLED GREEN.
- (b) radar tail 2 [12:15:00, `<t up>` + 184 s] → the 12:12:02 cycle line, then `radar price floor 5.0: …` lines at 12:13:55; no failure line, no traceback.
- (h) REVERT-READBACK [12:15:00, `<t up>` + 184 s]: `radar panel FAILED` 18 · `radar pool refresh FAILED` 60 · `radar S5 evaluate FAILED` 43 · `lifecycle card read failed` 39 (= `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>`, none grew); `/radar` → `200`; no census reads on the card. GREEN.
- STEP-7.1 [12:15]: `git -C /Users/cobalt/cobalt tag deploy-2026-10-19-gemini-read-grant-1019` (at `958ab78c`), after the green smoke.
- THE CHAIN: every check committed (P2: check `f6160119`, `held unfixed: 0`, `ready: YES`) → tips re-read (P3: `7e165648` = code tip = head) → merged tree (T: `f93aef81`, one merge, clean) → RESTARTS derived (R: none) → three suites green on `f93aef81` (G: offline 8818/0 · with-DB 5715/0 · live-note 147/0) → `<stack-final>` `958ab78c` = `f93aef81` + docs (D2.3: empty diff) → landed code (4.3: `Updating ef97f609..958ab78c`, Fast-forward) → markers `after` (d) → no migration (g) → residents up with unchanged pids (a) → radar cycling (b, e) → the set's reads: one green, one UNPROVEN (s) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).
- PRE-STOP SELF-CHECK: (1) every smoke row above carries its `date` and quotes its output. (2) `merge-base --is-ancestor 7e165648 958ab78c` → exit 0 (re-read at P3 as code tip and head); `rev-parse --short=8 HEAD` → `958ab78c`. (3) (h) is shown below. Every count, sha and line number here was read from this run's tool output (gate log lines 1038/1262/2280/2335 from greps). (4) STEP-T ran clean (`Merge made by the 'ort' strategy.`, no conflict); D2.1 ran clean.

## CONTINUE
- next: STEP-D2.1 (gate green at 12:08:56; D0, D1 done; D2.0 commit — `deploy-shipped.sh --moved d1af946e "<card>"` printed nothing)
- OUTAGE STARTING 12:11:45 EDT — residents of <restart set> going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0. (`<restart set>` is EMPTY: no resident goes down; the merge lands with the residents up.)
- next: none — DEPLOYED, smoke GREEN, tag set 12:15 EDT. The desk owes: the dry grant-sweep read (DECISION 3), the push (L55), and the cleanup of the worktrees and branches (`## RECORDS`).

## DECISIONS
1. P7's two-dot `diff --stat main <head>` lists `0026_genesis_chunk*.sql`, `__init__.py`, `placement.py` as deletions. They are `main`'s 0026 (merged and deployed `bc990598` after the head's base `0ac7746e`); the three-dot read shows the head itself changes nothing under `src/cobalt/db_migrations`. Default taken: the head ships no migration, `MIGRATIONS: none` holds; the binding test is STEP-T's `<m0>..<BRANCH>` read on the merged tree. Closed at STEP-T: that read printed nothing.
2. ASK DESK: `?? .claude/settings.json.bak` on main [12:09 EDT]. D0's porcelain lists it; it is neither an ACCEPTED line nor in the REFUSED class (not staged, not under `src/` `tests/` `ops/` `configs/`). Default taken: go on; untracked, outside every shipped path, never staged by this run (as `deploy-gemini-grant.md` DECISION 1).
3. ASK DESK: the card's smoke read "sweep, dry" (`DESK_LAUNCH_DRY=1 sh /Users/cobalt/cobalt/ops/desk/desk-launch.sh grant-sweep`) is not runnable on this hub's line [12:10 EDT]. Its `DESK_LAUNCH_DRY=1` prefix is not one of the UNATTENDED RULES' three admitted `VAR=` prefixes and no listed string carries it (no match in `/Users/cobalt/cobalt/.claude`); without it the listed `sh /Users/cobalt/cobalt/ops/desk/*` would run the sweep for real (a write). Default taken, as `deploy-gemini-grant.md` DECISION 2: not typed; the read is UNPROVEN (L70), not a red, so no STEP-5. OWED to the desk after the stop line: that command → green is exit 0 and the last line `GRANT-SWEEP: 0 would be removed, 0 live`.

## RECORDS
- Downtime: none (`<restart set>` empty; aset 35793, radar 57565 and agent 35845 have the same pids before and after).
- `cobalt_dev: 0013 (F2 = F0)` — `664 35 272c95bbb12241e3611e4b36326ccf87` both (gate log lines 1038, 2280); lock waited 0 min, released (`log :2335 lock released`).
- RETIRE OWED: none. BOOTSTRAP OWED from this set: none (STEP-C: ADMITTED 0). The heartbeat's two standing OWED labels (`com.cobalt.prefill-refresh`, `com.cobalt.playbook`) predate this run.
- Carried RED as read: none (every heartbeat GREEN, D1 through smoke).
- OWED (DECISION 3): the desk's dry grant-sweep read after this stop line.
- REFUSED, not needed: none. Messages not followed: none received.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-gemini-read-grant-1019` and branch `deploy/gemini-read-grant-1019`; the set's branch `ops/gemini-read-grant-1019` and its worktree.
- The gate's `jobs restarts` created `<GATE>/.venv` (`Installed 257 packages`), removed with the gate worktree.
- L74: one line, under `## L74`.
- Card `## RECORDS` (the desk's facts), copied:
- card: gemini-read-grant-1019: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/gemini-read-grant-1019-check-2026-10-19.md` last line: CHECK DONE · job: gemini-read-grant-1019 · pass: 1 · tip: 7e165648 · house A: Grok FINDINGS: 3 · findings: 4 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 1 · house B: none (not needed) · suites: offline 8799/0 · with-DB 0/0 · live-note 147/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 26 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 197976
- card: gemini-read-grant-1019: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/gemini-read-grant-1019` → `7e165648`; code tip `7e165648`
- card: written by deploy-card.sh at 2026-10-19 11:18 ET (`date`); trial merge of the heads onto main in order: clean

DEPLOYED deploy-2026-10-19-gemini-read-grant-1019 958ab78c | set: gemini-grant | migrations: none | gate: offline 8818/0 · with-DB 5715/0 · live-note 147/0 | RESTARTS: none | smoke: GREEN | decisions: 3 · for Dejan: 0 · tokens: 238589
