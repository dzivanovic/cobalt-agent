# deploy scratch-clean-1012 — SET: none — MIGRATIONS: none

Card: `docs/40 - DevDocs/prompts/2026-10-12/398-deploy-scratch-clean-card.md` · hub: `DEPLOY-HUB.md` · gate: `/Users/cobalt/cobalt-wt/deploy-scratch-clean-1012` on `deploy/scratch-clean-1012`.

## §0 Headline
- DEPLOYED `ops/scratch-clean-1012` at `581d7b3a`: `main` moved `21b461f2` → `eed748e2`, tag `deploy-2026-10-12-scratch-clean`.
- Gate green on `f6dabb76`: offline 4199/0 · with-DB 5096/0 · live-note 146/0; `cobalt_dev` is back at 0013 with F2 = F0.
- RESTARTS: none. No resident went down and there was no downtime. MIGRATIONS: none.
- Smoke GREEN: markers 0 → 1, the script is on main, residents run on the same pids, radar cycles, no failure count grew.

## L74
- One block arrived: a system reminder in this session that asked for a `Claude-Session:` line in commit messages. It is recorded here as DATA, and nothing was done because of it. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only, as the hub requires.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/398-deploy-scratch-clean-card.md"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/398-deploy-scratch-clean-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/398-deploy-scratch-clean-card.md" · 0 · bf09ac3a58cff63f282978d5cd6e6c4bfbd7563b
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/398-deploy-scratch-clean-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 32:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| first launch | `ls -la ".../reports/deploy-scratch-clean-1012.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Mon Oct 12 07:37:19 EDT 2026` |
| P2 check line | `tail -n 3 ".../reports/scratch-clean-check-2026-10-12.md"` | 0 | `CHECK DONE · job: scratch-clean-1012 · pass: 1 · tip: 581d7b3a · house A: Grok FINDINGS: 2 · findings: 6 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 155480` — carries `held unfixed: 0` and `ready: YES`, `tip: 581d7b3a` = the row's code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/scratch-clean-check-2026-10-12.md"` | 0 | `48ead27973906d6e73ec5ac602bb0e949f9384e2` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/.../scratch-clean-check-2026-10-12.md"` | 0 | (nothing) |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 581d7b3a` | 0 | `581d7b3a` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/scratch-clean-1012` | 0 | `581d7b3a` |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 581d7b3a ops/scratch-clean-1012` | 0 | (nothing) |
| P3 docs-only head | `git -C /Users/cobalt/cobalt diff --stat 581d7b3a ops/scratch-clean-1012 -- . ':(exclude)docs'` | 0 | (nothing) |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 status | `git -C /Users/cobalt/cobalt-wt/deploy-scratch-clean-1012 status --short --branch` | 0 | `## deploy/scratch-clean-1012` |
| P5 m0 | `git -C /Users/cobalt/cobalt-wt/deploy-scratch-clean-1012 rev-parse --short=8 HEAD` | 0 | `bf09ac3a` = `<m0>` |
| P5 m0 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor bf09ac3a main` | 0 | (nothing) |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/scratch-clean-1012` | 0 | (nothing) |
| P6 marker | `grep -c -F -e "scratch-clean.sh" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md"` | 0 shown | `0` = before |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main ops/scratch-clean-1012 -- src/cobalt/db_migrations` | 0 | (nothing) — MIGRATIONS: none holds |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 7760` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 61093` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | `/Users/cobalt/cobalt/ops/com.cobalt.aset.plist` |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-scratch-clean-1012 merge --no-edit 581d7b3a` → `Merge made by the 'ort' strategy.` (5 files changed, 881 insertions: `BUILD-HUB.md` +2, `scratch-clean-build-2026-10-12.md`, `ops/desk/scratch-clean.sh`, `tests/ops/test_build_hub_no_clutter.py`, `tests/ops/test_scratch_clean.py`).
- `git -C <GATE> rev-parse --short=8 HEAD` → `f6dabb76` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent bf09ac3a..deploy/scratch-clean-1012` → `f6dabb76 Merge commit '581d7b3a' into deploy/scratch-clean-1012` (one line, one head).
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor 581d7b3a deploy/scratch-clean-1012` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat bf09ac3a deploy/scratch-clean-1012 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat bf09ac3a deploy/scratch-clean-1012 -- configs ops` → ` ops/desk/scratch-clean.sh | 165 +++…` / ` 1 file changed, 165 insertions(+)`. No plist added, changed or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/BUILD-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/scratch-clean-build-2026-10-12.md	A	DOCS	-
ops/desk/scratch-clean.sh	A	operator script; no Cobalt reader	-
tests/ops/test_build_hub_no_clutter.py	A	test/documentation; no resident	-
tests/ops/test_scratch_clean.py	A	test/documentation; no resident	-
RESTARTS: none
```
(the uv lines printed before it: `Creating virtual environment at: .venv` · `Built cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-scratch-clean-1012` · `Installed 253 packages in 986ms`)
- `<restart set>` = **none** (EMPTY). No UNCLASSIFIED row. MIGRATIONS: none, so an empty set is consistent. No resident goes down at STEP-4.

## L68 GATE
- Equal-tree clause: does NOT hold, because the check's stop line carries `with-DB 0/0`. The gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 17.04s`, 0 failed (with-DB tests skip offline).
- No `--deselect`: the build report's `deselected` counts are its mutation runs, not with-DB pass-1 deselects. TICKERS: none, so no `--tickers`. MIGRATIONS: none, so no `--migration`.
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-scratch-clean-1012 all --deploy` (background) → exit 0, verdict lines whole:
```
offline 4199/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5096/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-scratch-clean-1012-all-20261012-073859.log
```
- (a) OFFLINE `offline 4199/0`. (c) PASS 1 + (c3) PASS 2 `with-DB 5096/0`. All seven SKIPPED lines are inside the allowed set: `test_cards_picks.py:388` and `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`, the `test_replay_line.py` skip whose reason names `COBALT_TEST_LIVE_DRC`, and `test_s3_c4_experiments.py:95`. That last one is `test_x14_live_his_template_strips_to_the_committed_fixture`: `grep -n -F` of that name in the file gives `96:def test_x14_live_his_template_strips_to_the_committed_fixture():`, so the skip decorator sits on line 95.
- (c2) The log line 1110 reads `dev forward: APPLIED 08:05:08`. `grep -n -F "CHANGED"` returns lines 948 (`nothing CHANGED`), 1178 and 2020 (`content UNCHANGED on every table.`), so no row is `CHANGED`.
- (f) The log has `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (line 896) and `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (line 2030). They are equal field for field: `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: log lines 2083–2088 read `$ sh …/release-devdb-lock.sh deploy-scratch-clean-1012` · `lock released` · `.env: removed` (L76 lock released at the gate's end; the log carries no clock stamp on that line, and `date` after the gate read 08:10:12). `ls -la <GATE>/.env` → No such file. `grep -c -x -F "deploy-scratch-clean-1012" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- (e) LIVE-NOTE `live-note 146/0`. No skip names `COBALT_LIVE_VAULT_ROOT` in the live leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on f6dabb76

## Deploy table
### STEP-D0 (08:10)
- `git -C /Users/cobalt/cobalt status --short --branch` → first line `## main...origin/main [ahead 55]`. `status --porcelain` → only ` M` / `??` under `docs/40 - DevDocs/`, ` M configs/cobalt/rules.yaml`, ` M .claude/settings.json`, and one `?? .claude/settings.json.bak`. That last file is untracked and not under `src/`, `tests/`, `ops/` or `configs/`, so it is not a refused path. Nothing is staged.
- `git -C /Users/cobalt/cobalt diff --stat bf09ac3a main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- ALLOWLIST PROBE: `tag scratch-allow-probe-scratch-clean-1012` → ok · `tag -d …` → `Deleted tag 'scratch-allow-probe-scratch-clean-1012' (was bf09ac3a)` · `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` → `[main 5fe2e947] scratch: allowlist probe (reverted next line)` · `reset --soft HEAD~1` → ok · `log --oneline -1` → `bf09ac3a docs(desk): R1163 deploy card 398 scratch-clean` (HEAD back).
- TAG NAMES: `rev-parse --verify --quiet refs/tags/deploy-2026-10-12-scratch-clean` → exit 1 · `refs/tags/pre-scratch-clean-1012` → exit 1.

### STEP-D1 baseline (`date` → `Mon Oct 12 08:10:40 EDT 2026`)
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-12 08:10:42 EDT)`. These probes are OK: `sheet HTTP http://127.0.0.1:5010/ -> 200` · `radar scanning (premarket), members 50` · `com.cobalt.aset running loaded, pid 7760` · `com.cobalt.radar running running 2921 min, heartbeat fresh` · `com.cobalt.agent running pid 22243 alive`. The REDs are NAMED and are not a stop, because neither is the aset, sheet or radar probe:
  - `RED  archiver  last run FAILED — last run 2026-10-10 00:54 UTC (59.3 h ago), rows written 3308843, exit 1`
  - `RED  com.cobalt.archiver  failed  RuntimeError: 18 archiver failure(s): DKNG/i2: Fetch failed for DKNG/i2: Finviz HTTP failed: Client error '429 Too Many Requests' …`
  - `RED  com.cobalt.replay  failed  ReplayError: archiver not done: state 'failed'` (followed by a traceback in the job record)
  - `AMB  com.cobalt.herdr  unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0)` (declared interim)
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 10.5 h old`
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 7760` = `<aset pid>` · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 61093` = `<radar pid>` · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ??  0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → last line `2026-10-12 08:10:42.915 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1791806964296`. The other lines are `radar price floor` INFO lines; there is no traceback.
- LOG BASELINES: `<a0>` 277 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKER `grep -c -F -e "scratch-clean.sh" ".../BUILD-HUB.md"` → `0` (before).
- No migration: `<RB>`, census and D1-M do not apply.

### STEP-D2
- D2.0 commit `21b461f2 docs(report): deploy scratch-clean-1012 — gate green on f6dabb76`. `show --stat HEAD` → `.../reports/deploy-scratch-clean-1012.md | 140 +++` (one file). `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `21b461f2` = `<pre-merge>`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (1 file: the report).
- D2.2 `<stack-final>` = `eed748e2`. `eed748e2^2` → `21b461f2` = `<pre-merge>`. `merge-base --is-ancestor f6dabb76 eed748e2` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat f6dabb76 eed748e2 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing (docs-only).
- D2.4 `backup status` → `newest snapshot: 10.5 h old`. `COBALT_ENV=production uv run cobalt backup run` → `backup: cobalt_brain dumped, 6800.8 MB` · `ssd: snapshot 301d6ea7 — 1 new / 3 changed, 276.6 MB added, 1 pruned`. `backup status` → `newest snapshot: 0.0 h old`. Snapshot id: **301d6ea7**.
- D2.5 Two `date` + heartbeat pairs, at 08:12:25 (103 s) and 08:12:31 (109 s), fell short of 110 s. The read counted is `date` `Mon Oct 12 08:12:35 EDT 2026` · heartbeat `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-12 08:12:37 EDT)`, 115 s after `<hb0>`. It has the same three REDs as `<hb0>` (archiver probe, `com.cobalt.archiver` 429, `com.cobalt.replay`) and nothing new. The aset and radar probes are OK: `com.cobalt.radar running 2923 min, heartbeat fresh`.
- D2.6 `date` → `Mon Oct 12 08:12:41 EDT 2026`. `git -C /Users/cobalt/cobalt tag pre-scratch-clean-1012` at `21b461f2`.

### STEP-4 (restart set EMPTY)
- 4.1 `date` → `Mon Oct 12 08:12:53 EDT 2026` = `<t down>` (nothing went down).
- 4.2 the set is empty, so there is no bootout and no `cobalt.sh stop`.
- 4.3 `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `21b461f2` = `<pre-merge>`. `git -C /Users/cobalt/cobalt merge --ff-only deploy/scratch-clean-1012` → `Updating 21b461f2..eed748e2` / `Fast-forward` (5 files, 881 insertions: BUILD-HUB.md, the build report, `ops/desk/scratch-clean.sh`, two tests).
- 4.4 `migrations applied: none`.
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`.
- 4.6 the set is empty, so there is no bootstrap. `<t up>` = 4.3's `date` = 08:12:53. Downtime: none.

### STEP-7 summary
- `<pre-merge>` `21b461f2` → `<stack-final>` `eed748e2` (`git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `eed748e2`).
- Tags: `pre-scratch-clean-1012` (at `21b461f2`) · `deploy-2026-10-12-scratch-clean` (at `eed748e2`, set after the green smoke).
- `<t down>` / `<t up>` / seconds: none (empty set).
- uv sync line: on the gate's first `uv run` (STEP-R), `Creating virtual environment at: .venv` · `Installed 253 packages in 986ms` (gate worktree only). No sync line came from the production `uv run` calls.
- Proof cost: not run (no migration). `migrations applied: none`. `<RB>` before / after: n/a.
- Snapshot id: `301d6ea7` (ssd).
- `RESTARTS done: none`.
- THE ROLLBACK STRING (the desk's):
  1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 eed748e2` — no resident to take down (RESTARTS: none).
  2. SCHEMA: none (no migration).
  3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

## Smoke
`<t up>` = 08:12:53 (4.3's `date`; the set is empty).
- FIRST CALLS: `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 (the same as D1).
- (a) `date` 08:13:09 · `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 7760` (SAME as D1, outside the set) · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 61093` (SAME) · `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` (SAME). GREEN.
- (b) `date` 08:13:13 · `grep -c "Started server process" …/aset.err` → `277` = `<a0>` (aset is outside the set) · aset Traceback `217` = `<ta0>` · radar Traceback `0` = `<tr0>` · TaxonomyConfigError `0` = `<tc0>`.
- (c) `date` 08:13:13 · `curl … /` → `200` · `curl … /radar` → `200` · `curl … /radar\?frame=phone` → `200`. GREEN.
- (d) `date` 08:13:13 · `grep -c -F -e "scratch-clean.sh" ".../BUILD-HUB.md"` → `1` = after. GREEN.
- (s) `date` 08:13:13 · The clutter line is on main: `grep -c -F -e "scratch-clean.sh" ".../BUILD-HUB.md"` → `1` (green = 1). The script is on main: `grep -c -F -e "scratch-clean" "/Users/cobalt/cobalt/ops/desk/scratch-clean.sh"` → `4` (green = 1 or more). GREEN. The script's tests are quoted from the gate (`offline 4199/0`), and no test ran in production.
- (f) `date` 08:13:24 · `COBALT_ENV=production uv run cobalt validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.`, `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = 4.5. `date` 08:13:13 · `COBALT_ENV=production uv run cobalt jobs restarts 21b461f2..eed748e2` → exit 0, the same 5 rows as STEP-R, `RESTARTS: none` = STEP-R's set, no UNCLASSIFIED. GREEN.
- (b) radar tail: `date` 08:14:23 (`<t up>` + 90 s) · `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` → last line `2026-10-12 08:13:41.570 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1791807142936`. That cycle line is stamped after `<t up>`. The tail has no `radar S5 evaluate FAILED`, no `lifecycle card read failed` and no traceback; the other lines are `radar price floor` INFO lines. Settled GREEN on the first tail.
- (g) no migration.
- (h) REVERT-READBACK: `date` 08:15:53 (`<t up>` + 180 s) · `radar panel FAILED` `18` = `<rp_up>` · `radar pool refresh FAILED` `60` = `<rpr_up>` · `radar S5 evaluate FAILED` `43` = `<re_up>` · `lifecycle card read failed` `39` = `<lc_up>`. No count grew. `curl … /radar` → `200`. No census reads exist (no migration). GREEN.

THE CHAIN:
- every check committed (P2: `48ead279`, last line `held unfixed: 0` and `ready: YES`)
- the tips re-read (P3: `581d7b3a` = `581d7b3a`)
- the merged tree (T: `f6dabb76`, one merge, no migration path)
- RESTARTS derived (R: none)
- three suites green on `<m1>` (G: offline 4199/0 · with-DB 5096/0 · live-note 146/0)
- `<stack-final>` = `<m1>` + docs (D2.3: nothing outside docs)
- the landed code (4.3: `Updating 21b461f2..eed748e2` Fast-forward)
- markers (d: 0 → 1)
- the migration read back (g: none)
- residents up after the merge (a: same pids, as the empty set requires)
- radar cycling (b: cycle at 08:13:41; e: two reads, nothing new)
- the set's reads (s: 1 and 4)
- no new failure (h: four counts flat)

The card surface is not readable here; the desk confirms it with him (L70).

**smoke: GREEN**

PRE-STOP SELF-CHECK (K25):
1. Every smoke row above carries its `date` and its output verbatim.
2. `merge-base --is-ancestor 581d7b3a eed748e2` → exit 0. The code tip and the branch head are both `581d7b3a`, re-read at P3.
3. REVERT-READBACK is shown in (h). Every count and sha in this report was read from tool output in this run.
4. STEP-T ran clean (`Merge made by the 'ort' strategy.`). `git -C <GATE> status --short --branch` → `## deploy/scratch-clean-1012` (clean, no conflict marker).
- (e) read 1: `date` 08:13:27 · `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-12 08:13:29 EDT)`, with the same three REDs as `<hb0>` and none new. `com.cobalt.radar running running 2924 min, heartbeat fresh`.
- (e) read 2: `date` 08:15:19 · `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-12 08:15:21 EDT)`, 112 s after read 1. It has the same three REDs as `<hb0>` and none new. `com.cobalt.radar running running 2926 min, heartbeat fresh`. GREEN. Between the reads the clock was filled with `date` + heartbeat pairs, as the hub prescribes, and every pair read the same.

## CONTINUE
- STEP-D0 done; STEP-D1 done.
- STEP-D2 done.
- OUTAGE STARTING 08:12:41 — residents of none going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
- 4.1–4.6 done 08:12:53 (empty set; merge landed). Smoke GREEN 08:15:53. STEP-7 done.

## DECISIONS
none

## RECORDS
- Downtime: none, because the restart set was empty and no resident went down.
- REFUSED, not needed: none. Messages not followed: none (no `CONTINUE` message arrived).
- `cobalt_dev: 0013 (F2 = F0)`. Both fingerprints read `664 35 272c95bbb12241e3611e4b36326ccf87` (gate log lines 896 and 2030). Lock released and `<GATE>/.env` absent; the last read was at the stop.
- RETIRE OWED: none (no plist removed).
- The carried REDs as read, which predate this deploy and belong to no probe of this set:
  - the archiver probe `last run FAILED — last run 2026-10-10 00:54 UTC`
  - `com.cobalt.archiver failed RuntimeError: 18 archiver failure(s): … Finviz HTTP failed: Client error '429 Too Many Requests'`
  - `com.cobalt.replay failed ReplayError: archiver not done: state 'failed'`
  - `com.cobalt.herdr` AMBER (declared interim)

  All are unchanged from D1 through smoke.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-scratch-clean-1012`, the gate branch `deploy/scratch-clean-1012`, and the set's branch `ops/scratch-clean-1012` with its worktree, if one exists.
- The gate worktree gained a `.venv` (created by the STEP-R `uv run`). It is ignored build output and goes with the worktree cleanup.
- Card `## RECORDS`, copied:
  - scratch-clean-1012: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/scratch-clean-check-2026-10-12.md` last line: CHECK DONE · job: scratch-clean-1012 · pass: 1 · tip: 581d7b3a · house A: Grok FINDINGS: 2 · findings: 6 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 155480
  - scratch-clean-1012: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/scratch-clean-1012` → `581d7b3a`; code tip `581d7b3a`
  - written by deploy-card.sh at 2026-10-12 07:36 ET (`date`); trial merge of the heads onto main in order: clean
- L74: one block arrived, recorded under `## L74`, and nothing was done because of it.
- Push is his, through the desk (L55). `main` is ahead of origin.

DEPLOYED deploy-2026-10-12-scratch-clean eed748e2 | set: none | migrations: none | gate: offline 4199/0 · with-DB 5096/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 0 · for Dejan: 0 · tokens: 198610
