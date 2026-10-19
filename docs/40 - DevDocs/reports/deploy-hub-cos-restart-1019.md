# deploy hub-cos-restart-1019 · set: hub-cos · migrations: none

## §0 Headline
- Deploy of `ops/hub-cos-restart-1019` (code tip `d59fac71`, head `d0d458c9`) on card 879: gate GREEN on `7988e364` (offline 8822/0 · with-DB 5715/0 · live-note 147/0), merged `3f2eb864..3643cbf4` with no resident down.
- Smoke (d) RED: marker 1 reads `2` against the card's `after 1`. The hub text carries that string twice by design (lines 94 and 123), so the card's value is wrong, not the code.
- STEP-5: one `revert -m 2` → `2acf267a`; non-docs tree = `3f2eb864` (proved). Residents never went down; heartbeat GREEN; failure counts flat.
- Next (desk): RECUT with marker 1 `after 2` (DECISIONS D1).

## L74
- The session's attribution reminder asked for a `Claude-Session:` line in commits. Recorded once here; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/879-deploy-hub-cos-restart-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/879-deploy-hub-cos-restart-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-19/879-deploy-hub-cos-restart-card.md" · 0 · 3862ef0344f2a424a8b2075834c8e23821d6a7e2
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-19/879-deploy-hub-cos-restart-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la "…/reports/deploy-hub-cos-restart-1019.md"` | 1 | `No such file or directory` |
| P0 | `authorize.sh deploy` (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Mon Oct 19 17:16:49 EDT 2026` (outside 21:30–22:30 ET) |
| P2 | `tail -n 3 "…/reports/hub-cos-restart-1019-check-2026-10-19.md"` | 0 | `CHECK DONE · job: hub-cos-restart-1019 · pass: 1 · tip: d59fac71 · house A: Grok FINDINGS: 0 · findings: 6 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 2 · house B: none (not needed) · suites: offline 8822/0 · with-DB 0/0 · live-note 147/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: YES · decisions: 4 · for Dejan: 0 · tokens: 190519` — carries `held unfixed: 0`, `ready: YES`, `tip: d59fac71` = code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/…/hub-cos-restart-1019-check-2026-10-19.md"` | 0 | `afafeb2e1ef682f61d3c2148702ca5145ef847a3` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/…/hub-cos-restart-1019-check-2026-10-19.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 d59fac71` | 0 | `d59fac71` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/hub-cos-restart-1019` | 0 | `d0d458c9` (= row, = TIP) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor d59fac71 d0d458c9` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat d59fac71 d0d458c9 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (no holder) |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/hub-cos-restart-1019` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `3862ef03` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 3862ef03 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/hub-cos-restart-1019` | 0 | empty |
| P6 | marker 1 `grep -c -F "com.cobalt.cos: not loaded — skipped" "…/DEPLOY-HUB.md"` | 1 | `0` (= before) |
| P6 | marker 2 `grep -c -F "com.cobalt.cos is loaded; its bootout and bootstrap strings are not on the deploy list (R60)" "…/DEPLOY-HUB.md"` | 1 | `0` (= before) |
| P6 | marker 3 `grep -c -F "launchctl kickstart -k gui/501/com.cobalt.cos" "…/DEPLOY-HUB.md"` | 1 | `0` (= before) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main d0d458c9 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none holds) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 35793` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 57565` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 35845).` |

## THE TREE
- `git -C <GATE> merge --no-edit d0d458c9` → `Merge made by the 'ort' strategy.` (5 files: `DEPLOY-HUB.md` 7 +-, build report + `.result`, `tests/ops/test_hub_cos_restart_1019.py` +93, `tests/ops/test_hub_deferred_1018.py` 4 +-).
- `git -C <GATE> rev-parse --short=8 HEAD` → `7988e364` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 3862ef03..deploy/hub-cos-restart-1019` → `7988e364 Merge commit 'd0d458c9' into deploy/hub-cos-restart-1019` (one line, one head).
- `merge-base --is-ancestor d59fac71 deploy/hub-cos-restart-1019` → exit 0; `merge-base --is-ancestor d0d458c9 deploy/hub-cos-restart-1019` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat 3862ef03 deploy/hub-cos-restart-1019 -- src/cobalt/db_migrations` → nothing (no migration path; `MIGRATIONS: none`).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 3862ef03 deploy/hub-cos-restart-1019 -- configs ops` → nothing. `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 3862ef03 deploy/hub-cos-restart-1019` → exit 0, whole output: `STEP-C: ADMITTED 0`. `<launchd set>`: empty. `<deferred set>`: empty.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0:
```
Using CPython 3.14.3 interpreter at: /opt/homebrew/opt/python@3.14/bin/python3.14
Creating virtual environment at: .venv
   Building cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-hub-cos-restart-1019
      Built cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-hub-cos-restart-1019
Installed 257 packages in 905ms
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/hub-cos-restart-1019-build-2026-10-19.md	A	DOCS	-
docs/40 - DevDocs/reports/hub-cos-restart-1019-build-2026-10-19.result	A	DOCS	-
tests/ops/test_hub_cos_restart_1019.py	A	test/documentation; no resident	-
tests/ops/test_hub_deferred_1018.py	M	test/documentation; no resident	-
RESTARTS: none
```
- No `UNCLASSIFIED` row. `<restart set>`: EMPTY (no resident goes down; the merge lands with residents up). `<deferred set>`: empty. `<launchd set>`: empty. `MIGRATIONS: none`, so an empty set is consistent.

## L68 GATE
- EQUAL-TREE CLAUSE: does not hold — the check's stop line carries `with-DB 0/0` (DB: none), so the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `264 passed, 163 skipped in 19.00s` (0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db` skip).
- No `--deselect` (the build report names none), no `--tickers` (`TICKERS: none`), no `--migration` (`MIGRATIONS: none`). `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-hub-cos-restart-1019 all --deploy --deploy-gate` launched in the background.
- Verdict lines WHOLE (exit 0):
```
tests/ops: run (deploy gate)
offline 8822/0
lock: waited 4 min
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-hub-cos-restart-1019-all-20261019-171901.log
```
- (a) offline `8822/0`; W line `tests/ops: run (deploy gate)`.
- (b) lock taken (waited 4 min); proof-only at `0013`, nothing CHANGED.
- (c) every SKIPPED line inside the allowed set: `test_cards_picks.py:388`, `:401`; `test_playbook_live.py:31` = `test_live_vault_renders_six_decks` (def at :32), reason `COBALT_LIVE_VAULT_ROOT not set`; `test_radar_evaluate.py:695`; `test_replay_line.py:266` reason `COBALT_TEST_LIVE_DRC`; `test_s3_c4_experiments.py:95` = `test_x14_live_his_template_strips_to_the_committed_fixture` (def at :96); `test_catalyst.py:365`; `test_predicate.py:262`.
- (c2) `grep -n -F "dev forward" <log>` → `1262:dev forward: APPLIED 18:05:25`. `grep -n -F "CHANGED" <log>` → 3 lines: `1091:proof-only: on cobalt_dev, nothing CHANGED …` and two proof tables (`1333`, `2270`) each `content UNCHANGED on every table.` — no `CHANGED` object.
- (c3)/(c) with-DB `5715/0`.
- (f) `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: `.env: removed`; `grep -n -F "released" <log>` → `2335:lock released` (the log stamps no time on it; gate ended before 18:10:57). `ls -la <GATE>/.env` → No such file. `grep -c -x -F "deploy-hub-cos-restart-1019" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `0` (the lock dir is another session's, not this worktree's).
- (e) live-note `147/0`; no skip naming `COBALT_LIVE_VAULT_ROOT` in the live-note leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 7988e364

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 220]` |
| MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | no staged line; ` M` lines are `.claude/settings.json`, `configs/cobalt/rules.yaml` and `docs/40 - DevDocs/…` only; `??` lines are under `docs/40 - DevDocs/` plus `.claude/settings.json.bak` (not `src/`, `tests/`, `ops/`, `configs/`) |
| MAIN | `git -C /Users/cobalt/cobalt diff --stat 3862ef03 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `tag scratch-allow-probe-hub-cos-restart-1019` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-hub-cos-restart-1019' (was 7bb031e4)` |
| PROBE | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main fc8c5b39] …` · — · `7bb031e4 docs(desk): REFRESH 6cf2ce55 to f3a3ff5e, section 5 rewritten R2090` (HEAD back) |
| TAG | `rev-parse --verify --quiet refs/tags/deploy-2026-10-19-hub-cos-restart-1019` | 1 | — |
| TAG | `rev-parse --verify --quiet refs/tags/pre-hub-cos-restart-1019` | 1 | — |

### STEP-D1 baseline
- `date` → `Mon Oct 19 18:11:39 EDT 2026`. `COBALT_ENV=production uv run cobalt heartbeat show` → `<hb0>`: `HEARTBEAT GREEN — 18 job(s), 14 probe(s), nothing red  (2026-10-19 18:11:41 EDT)`; aset pid 35793 running, radar `running 419 min, heartbeat fresh`, agent pid 35845 alive; `AMB com.cobalt.herdr unmanaged` (declared interim); `com.cobalt.cos disabled — NOT LOADED BY DESIGN`; `com.cobalt.prefill-refresh` and `com.cobalt.playbook` `OWED (deferred bootstrap)`. No RED.
- `COBALT_ENV=production uv run cobalt validate` → exit 0 (`<val0>`: 13 trade_defs OK, `Placement (docs/PLACEMENT.md): tree clean.`); `<jobs0>` = `Jobs (F17): 18 registered — 7 resident, 11 one-shot. Kill phrase 'COBALT STOP'.` with `NOT LOADED BY DESIGN (1): com.cobalt.cos`.
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 6.0 h old`.
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 35793` (`<aset pid>`). `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 57565` (`<radar pid>`). `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 35845).`; `ps -p 35845` → `35845 ??         0:00.03 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → seven `cards.expire: falling back to the session close (16:00:00)` INFO lines, last `2026-10-19 18:11:34.966 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792447804056`.
- LOG BASELINES: `<a0>` = 284 · `<ta0>` = 217 · `<tr0>` = 0 · `<tc0>` = 0 · `<rp0>` = 18 · `<rpr0>` = 60 · `<re0>` = 43 · `<lc0>` = 39.
- `curl … /radar` → `200`. MARKERS → `0`, `0`, `0` (each = before).
- THE LAUNCHD SET: empty — nothing. MIGRATIONS: none — no `<RB>`, no D1-M.

### STEP-D2
- D2.0 `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --moved 3862ef03 "<card>"` → prints nothing. Report committed `3f2eb864` (`docs(report): deploy hub-cos-restart-1019 — gate green on 7988e364`); `show --stat HEAD` → that one file, 153 insertions. `rev-parse --short=8 main` → `3f2eb864` = `<pre-merge>`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (`877-cos-probe-card.md`, `cto-2026-10-19.md`, this report).
- D2.2 `<stack-final>` = `3643cbf4`; `rev-parse --short=8 3643cbf4^2` → `3f2eb864` = `<pre-merge>`; `merge-base --is-ancestor 7988e364 3643cbf4` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat 7988e364 3643cbf4 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing (docs-only).
- D2.4 `backup status` → `newest snapshot: 6.0 h old`; `backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 9284.1 MB` · `ssd: snapshot d5ae3327 — 0 new / 3 changed, 208.6 MB added, 1 pruned`; `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `date` → `Mon Oct 19 18:13:53 EDT 2026` (134 s after D1's 18:11:39); `heartbeat show` → `HEARTBEAT GREEN — 18 job(s), 14 probe(s), nothing red  (2026-10-19 18:13:56 EDT)`; radar `running 421 min, heartbeat fresh`. No new RED.
- D2.6 `date` → `Mon Oct 19 18:14:00 EDT 2026`; `git -C /Users/cobalt/cobalt tag pre-hub-cos-restart-1019` at `3f2eb864` → exit 0.

### STEP-4 (empty `<restart set>`)
- 4.1 `date` → `Mon Oct 19 18:14:16 EDT 2026` = `<t down>` (nothing went down) = `<t up>` (4.3's date, set empty).
- 4.2 nothing (no label in the set; no orphan-clean; agent not in the set).
- 4.3 `rev-parse --short=8 HEAD` → `3f2eb864` = `<pre-merge>`. `git -C /Users/cobalt/cobalt merge --ff-only deploy/hub-cos-restart-1019` → `Updating 3f2eb864..3643cbf4` / `Fast-forward` (5 files, 285 insertions, 5 deletions).
- 4.4 `migrations applied: none`.
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0; `Jobs (F17): 18 registered — 7 resident, 11 one-shot. Kill phrase 'COBALT STOP'.` (= `<jobs0>`).
- 4.6 nothing (no label taken down). Downtime: none.
- 4.6L nothing (`<launchd set>` empty).

### THE ROLLBACK STRING (L54; the desk's beyond STEP-5)
1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 3643cbf4` — USED by STEP-5 below (revert commit `2acf267a`). `<restart set>` empty: no resident down or up; `<launchd set>` empty.
2. SCHEMA: none (no migration).
3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit 2acf267a` — git titles it `Reapply "Merge branch 'main' into deploy/hub-cos-restart-1019"`.

Tags: `pre-hub-cos-restart-1019` at `3f2eb864`; `deploy-2026-10-19-hub-cos-restart-1019` NOT set (smoke RED). `<t down>` / `<t up>`: none (empty set). uv sync line: none at the merge (the gate worktree's first `uv run` built its own `.venv`, `Installed 257 packages in 905ms`). Proof cost: none (no migration). `migrations applied: none`. `<RB>`: none. Snapshot `d5ae3327`. `RESTARTS done: none`. `LAUNCHD done: none`. No `BOOTSTRAP OWED` line from this set.

## Smoke
### STEP-4.7 (on `3643cbf4`)
- FIRST CALLS (`<t up>` = 18:14:16): `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39.
- (a) `date` 18:14:41 · `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 35793` (SAME as D1, outside the set) · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 57565` (SAME) · `cobalt.sh status` → `Cobalt is ONLINE (PID: 35845).` (SAME). GREEN.
- (b) `date` 18:14:45 · `grep -c "Started server process" aset.err` → `284` (= `<a0>`, aset outside the set) · `tail -n 30 aset.err` → last lines a 10:36:34 aset card write for SPCX (no traceback) · Traceback aset `217` (= 217), radar `0` (= 0), TaxonomyConfigError `0` (= 0). Counts GREEN; radar tails not reached before (d).
- (c) `date` 18:14:49 · `/` → `200` · `/radar` → `200` · `/radar\?frame=phone` → `200`. GREEN.
- (d) `date` 18:14:53 · MARKERS:
  - marker 1 `grep -c -F "com.cobalt.cos: not loaded — skipped" "…/DEPLOY-HUB.md"` → `2`; the card's after is `1`. **RED.** `grep -n -F` → lines `94` (the `## RESTARTS` rule: "write the line `com.cobalt.cos: not loaded — skipped` under `## RESTARTS`") and `123` (D1: "`## RESTARTS` holding `com.cobalt.cos: not loaded — skipped`"). The merged hub text carries the string twice by design; the card's `after 1` undercounts it.
  - marker 2 → `1` (= after). marker 3 → `0` (= after).
- RED → STEP-5.

### STEP-5 (ROLLBACK)
- (0) `date` → `Mon Oct 19 18:15:11 EDT 2026`.
- (1) `<restart set>` empty: nothing booted out, agent not stopped. Counts `<rp5>` 18 · `<rpr5>` 60 · `<re5>` 43 · `<lc5>` 39.
- (1L) `<launchd set>` empty: nothing.
- (2) `git -C /Users/cobalt/cobalt log --oneline -1` → `3643cbf4 Merge branch 'main' into deploy/hub-cos-restart-1019`. `git -C /Users/cobalt/cobalt revert --no-edit -m 2 3643cbf4` → `[main 2acf267a] Revert "Merge branch 'main' into deploy/hub-cos-restart-1019"` (5 files, 5 insertions, 285 deletions). PROOF: `git -C /Users/cobalt/cobalt diff --stat 3f2eb864 HEAD -- . ':(exclude)docs'` → nothing. Restored.
- (2L) nothing. (2a) not applicable (`migrations applied: none`). (2b) no migration ran.
- (3) nothing booted out: no orphan-clean, no bootstrap, no kickstart.
- (4) re-run on the reverted tree:
  - (a) `date` 18:15:21 · aset `state = running`, `pid = 35793` · radar `state = running`, `pid = 57565` · `Cobalt is ONLINE (PID: 35845).` GREEN.
  - (b) `Started server process` `284` (= `<a0>`) · Traceback aset `217`, radar `0` · TaxonomyConfigError `0` (all = baseline). `date` 18:15:46 (≥ `<t up>` + 90 s) · `tail -n 12 radar.err` → `2026-10-19 18:14:44.915 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792447994978` (after `<t up>`), no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → GREEN, settled.
  - (c) `/` `200` · `/radar` `200` · `/radar\?frame=phone` `200`.
  - (f) `COBALT_ENV=production uv run cobalt jobs restarts 3f2eb864..3643cbf4` → exit 0, five rows (DOCS / test), `RESTARTS: none` (= STEP-R's empty set), no `UNCLASSIFIED`. `validate` → exit 0, `Jobs (F17): 18 registered — 7 resident, 11 one-shot.` (= `<jobs0>`), `Placement (docs/PLACEMENT.md): tree clean.`
  - (g) no migration.
  - (e) `date` 18:15:32 · `heartbeat show` → `HEARTBEAT GREEN — 18 job(s), 14 probe(s), nothing red  (2026-10-19 18:15:32 EDT)`; radar `running 423 min, heartbeat fresh`.
  - (e) second read: `date` 18:17:22 (110 s after 18:15:32) · `heartbeat show` → `HEARTBEAT GREEN — 18 job(s), 14 probe(s), nothing red  (2026-10-19 18:17:24 EDT)`; `com.cobalt.radar running 425 min, heartbeat fresh`. No RED.
  - radar tail at 18:17:16 (+180 s): a `radar price floor 5.0` collect at `18:16:37`, no failure, no traceback (already settled at the first tail).
  - `grep -c -F "com.cobalt.cos: not loaded — skipped" "…/DEPLOY-HUB.md"` → `0` (hub text back to before). `launchctl print gui/501/com.cobalt.cos` → exit 113 `Could not find service` (cos untouched, not loaded).
  - REVERT-READBACK, after the settled tail: `radar panel FAILED` 18 · `radar pool refresh FAILED` 60 · `radar S5 evaluate FAILED` 43 · `lifecycle card read failed` 39 (each = `<rp5>` `<rpr5>` `<re5>` `<lc5>`; none growing). No `census` read on the card.

## CONTINUE
- STEP-D0 done; STEP-D1 baseline done.
- STEP-D2 done.
- OUTAGE STARTING 18:14:00 — residents of <restart set> going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0. (`<restart set>` is EMPTY: no resident goes down; the merge lands with the residents up.)
- STEP-4 done: merged `3f2eb864..3643cbf4` at 18:14:16, residents never down.
- STEP-4.7 smoke: (a), (b) counts, (c) green; (d) RED — marker 1 reads `2`, the card's after is `1`.
- STEP-5 done at 18:17:24: reverted `2acf267a`, smoke re-read green on the reverted tree.
- next: none from this session — the desk's RECUT (`desk-launch.sh recut "<card>"`).
- PRE-STOP SELF-CHECK: (1) every smoke row quoted with its `date` (18:14:41 → 18:17:22); (2) P3 re-read `d59fac71` / `d0d458c9`, both `merge-base --is-ancestor … 3643cbf4` → exit 0; (3) REVERT-READBACK shown under STEP-5 (4), counts 18/60/43/39 re-read this run; (4) STEP-T ran clean (`Merge made by the 'ort' strategy.`), no conflict marker.
- THE RELEASE: the gate released the lock (`.env: removed`, `lock released`); `<GATE>/.env` absent; nothing held.

## DECISIONS
- D1 · ASK DESK: smoke (d) went RED on marker 1 only because the card's `after 1` undercounts. The merged `DEPLOY-HUB.md` carries `com.cobalt.cos: not loaded — skipped` on two lines by design (line 94, the STEP-R rule that writes it; line 123, the D1 rule that reads it back). The code, the gate (offline 8822/0 · with-DB 5715/0 · live-note 147/0) and every other smoke row were green. Safe default taken: the hub's rule — (d) wrong → STEP-5, one revert, no re-judging of the card's value inside the run. The desk's next step is the RECUT (`desk-launch.sh recut "<card>"`) with marker 1's `after` corrected to `2` (or the marker made line-unique); the re-land string is above as an alternative. Not his: a card value, no scope, money or schema. [18:16:34]

## RECORDS
- Downtime: none (`<restart set>` empty; residents never went down; aset 35793, radar 57565, agent 35845 throughout).
- `main` now carries `3643cbf4` (the deploy merge) and `2acf267a` (its revert); the tree's non-docs paths equal `3f2eb864`. `pre-hub-cos-restart-1019` tag stays at `3f2eb864`.
- `cobalt_dev: 0013 (F2 = F0)` — from the gate.
- RETIRE OWED: none. BOOTSTRAP OWED: none from this set (heartbeat shows the earlier `com.cobalt.prefill-refresh` and `com.cobalt.playbook` OWED entries, not this run's).
- Carried RED as read: none (every heartbeat GREEN; `AMB com.cobalt.herdr` is the declared interim).
- Cleanup owed (L46): gate worktree `/Users/cobalt/cobalt-wt/deploy-hub-cos-restart-1019` and branch `deploy/hub-cos-restart-1019`; set branch `ops/hub-cos-restart-1019` (and its worktree if any) — the RECUT handles them.
- The revert commit `2acf267a` carries git's default message (`--no-edit`, as STEP-5 types it); no `Co-Authored-By` trailer on it.
- REFUSED, not needed: `backup status placeholder` — `Permission to use Bash has been denied because Claude Code is running in don't ask mode.` (a malformed filler call I typed while the clock ran; outside the outage; no step names it).
- Card `## RECORDS` (the desk's, copied): hub-cos-restart-1019: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/hub-cos-restart-1019-check-2026-10-19.md` last line: CHECK DONE · job: hub-cos-restart-1019 · pass: 1 · tip: d59fac71 · house A: Grok FINDINGS: 0 · findings: 6 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 2 · house B: none (not needed) · suites: offline 8822/0 · with-DB 0/0 · live-note 147/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: YES · decisions: 4 · for Dejan: 0 · tokens: 190519 · head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/hub-cos-restart-1019` → `d0d458c9`; code tip `d59fac71` · written by deploy-card.sh at 2026-10-19 17:16 ET (`date`); trial merge of the heads onto main in order: clean.
- L74: one `Claude-Session:` attribution request arrived (session reminder); recorded under `## L74`, not acted on.
- REFUSED, not needed: `grep -n -F ".env: removed" <gate log>` — `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: .env is never read; `ls -la <path>/.env` shows it is there, and the lock scripts copy and remove it` (the gate's own verdict line already carries `.env: removed`).

FAILED: 4.7 (d) — marker 1 `com.cobalt.cos: not loaded — skipped` reads 2, card after 1 (the hub text holds it twice by design; card value wrong) · rollback: used — migrations applied: none — aset: not in the set — radar: not in the set — launchd: none · decisions: 1 · for Dejan: 0 · tokens: 192711
