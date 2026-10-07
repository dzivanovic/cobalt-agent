# deploy radar-direction-color-1007 · SET: none · MIGRATIONS: none

## §0 Headline
- Deploy of `ops/radar-direction-color-1007` (`541adf0c`, his R625) on gate branch `deploy/radar-direction-color-1007-attempt2`. Started 2026-10-07 13:50:43 EDT.
- Shipped: `main` 2e1e8317 → 8c91922b. Gate green on 08c6dad1 (offline 3975/0 · with-DB 4859/0 · live-note 146/0). aset and radar restarted, down 11 s. Smoke GREEN. No migration.
- One decision, not his: an untracked `.claude/settings.json.bak` on main (see DECISIONS).

## L74
- An attribution block arrived in the session context asking for a `Claude-Session:` line on commits. Recorded here once as data. No action taken: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-07/97-deploy-radar-direction-color-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-07/97-deploy-radar-direction-color-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-07/97-deploy-radar-direction-color-card.md" · 0 · 43fb2a3fc7deebd42758e4dc8b88eca9984cfd72
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-07/97-deploy-radar-direction-color-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-07 R625 row · grep -n "^| R625 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · 19:| R625 | 10:15 ET | HIS RULING (words: `cto-2026-10-07-words.md` R625): a radar card's header row and title are green for long, red for short; a short fix or a rework, the drafter sizes it. LAUNCHING a drafter, prompt `88`. | HIS RULING · APPROVED |
RULING 2026-10-07 R625 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R625 |" -- "docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · 33a49ab6048bcc5ae6f489310beb5e99978eadfd
RULING 2026-10-07 R625 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la "<REPORT>"` | 1 | No such file or directory |
| P0 | authorize.sh (above) | 0 | AUTHORIZED |
| P1 | `date` | 0 | Wed Oct  7 13:50:43 EDT 2026 |
| P2 | `tail -n 3 ".../radar-direction-color-check-2026-10-07.md"` | 0 | `CHECK DONE · job: radar-direction-color · pass: 1 · tip: 541adf0c · … · held unfixed: 0 · open: 2 · … · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 148149` |
| P2 | `git log -1 --format=%H -- <check report>` | 0 | 83792ec067e46c5395266bb776a34bc0a9346377 |
| P2 | `git diff --stat -- <check report>` | 0 | (nothing) |
| P3 | `rev-parse --short=8 541adf0c` | 0 | 541adf0c |
| P3 | `rev-parse --short=8 ops/radar-direction-color-1007` | 0 | 541adf0c |
| P3 | `merge-base --is-ancestor 541adf0c 541adf0c` | 0 | — |
| P3 | `diff --stat 541adf0c ops/radar-direction-color-1007 -- . ':(exclude)docs'` | 0 | (nothing) |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` — no lock held |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/radar-direction-color-1007-attempt2` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m0>` = 43fb2a3f |
| P5 | `merge-base --is-ancestor 43fb2a3f main` | 0 | — |
| P5 | `log --oneline main..deploy/radar-direction-color-1007-attempt2` | 0 | (empty) |
| P6 | `grep -c -F "dir-long" .../radar_panel.py` | 1 | 0 (before 0) |
| P6 | `grep -c -F "def test_radar_direction_touches_only_strip_and_title" .../test_radar_panel_cards.py` | 1 | 0 (before 0) |
| P7 | `diff --stat main 541adf0c -- src/cobalt/db_migrations` | 0 | (nothing) — MIGRATIONS: none holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, pid 64112 |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, pid 64129 |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 541adf0c` → `Merge made by the 'ort' strategy.` (4 files: `docs/40 - DevDocs/cobalt/aset/radar_panel.md`, `.../radar-direction-color-build-2026-10-07.md`, `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_radar_panel_cards.py`; 408 insertions, 5 deletions).
- `<m1>` = `git -C <GATE> rev-parse --short=8 HEAD` → `08c6dad1`.
- `log --oneline --merges --first-parent 43fb2a3f..deploy/radar-direction-color-1007-attempt2` → `08c6dad1 Merge commit '541adf0c' into deploy/radar-direction-color-1007-attempt2`.
- `merge-base --is-ancestor 541adf0c deploy/radar-direction-color-1007-attempt2` → exit 0.
- `diff --stat 43fb2a3f deploy/radar-direction-color-1007-attempt2 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `diff --stat 43fb2a3f deploy/radar-direction-color-1007-attempt2 -- configs ops` → nothing. No plist added, changed or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-direction-color-build-2026-10-07.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
(uv created the gate's `.venv`: CPython 3.14.3, 253 packages installed.) `<restart set>` = `com.cobalt.aset com.cobalt.radar`.

## L68 GATE
- EQUAL-TREE CLAUSE does not hold: `git -C /Users/cobalt/cobalt diff --stat 541adf0c 08c6dad1 -- . ":(exclude)docs"` → `ops/desk/job-clean.sh | 166 ++++++++++++++++-` · `tests/ops/test_gate_clean.py | 430 +++++++++++++++++++++++++++++++++++++++++++` · `2 files changed, 587 insertions(+), 9 deletions(-)` (main moved since the check). The gate runs whole.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `261 passed, 163 skipped in 16.39s` (0 failed; the skips are with-DB tests, `Postgres env settings not available` / `requires_db`).
- Build-report deselects: `grep -n -F "deselect" <build report>` → line 121: `no --deselect: this build adds no with-DB test; no --tickers: no new test writes a row; no --migration`. Gate launched: `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-radar-direction-color-1007-attempt2 all --deploy` (background).
- Gate exit 0. Verdict lines, whole:
```
offline 3975/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4859/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-radar-direction-color-1007-attempt2-all-20261007-135216.log
```
- Skips: all seven are in the allowed set. `test_s3_c4_experiments.py:95` is the skip of `test_x14_live_his_template_strips_to_the_committed_fixture`: `grep -n -F` → `96:def test_x14_live_his_template_strips_to_the_committed_fixture():`. The `test_replay_line.py` skip names `COBALT_TEST_LIVE_DRC`.
- (b) `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log :880). (c2) `dev forward: APPLIED 14:15:14` (log :1089). (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log :1864) → `cobalt_dev: 0013 — F2 = F0` (log :1915).
- THE RELEASE: log :1916–1921 → `release-devdb-lock.sh` → `lock released` · `.env: removed` (L76 lock released; read at 14:20:15 EDT, `date`). `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-radar-direction-color-1007-attempt2" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → No such file (no lock dir).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 08c6dad1

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN | `git status --short --branch` | 0 | `## main...origin/main [ahead 75]`; dirty lines: ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, ` M`/`??` under `docs/40 - DevDocs/` only, plus `?? .claude/settings.json.bak` (see DECISIONS); no staged line, no dirty `src/`, `tests/`, `ops/` path |
| MAIN | `diff --stat 43fb2a3f main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | (nothing) |
| PROBE | `tag scratch-allow-probe-radar-direction-color-1007` / `tag -d …` | 0 / 0 | `Deleted tag 'scratch-allow-probe-radar-direction-color-1007' (was 43fb2a3f)` |
| PROBE | `commit --allow-empty -m "scratch: …"` / `reset --soft HEAD~1` / `log --oneline -1` | 0 / 0 / 0 | `[main 93354aa9] …` → `43fb2a3f docs(desk): RECUT radar-direction-color-1007 attempt 2` (HEAD back) |
| TAGS | `rev-parse --verify --quiet refs/tags/deploy-2026-10-07-radar-direction-color-attempt2` | 1 | free |
| TAGS | `rev-parse --verify --quiet refs/tags/pre-radar-direction-color-1007` | 1 | free |

### STEP-D1 (baseline, 14:20:37 EDT)
- `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 1 probe(s)  (2026-10-07 14:20:39 EDT)`; the one RED: `RED  radar                    failed_stage bars: poll failures: 1` — the CARRIED FAMILY: `com.cobalt.radar running … running 1176 min, heartbeat fresh`; `radar.err` tail shows `2026-10-07 14:19:41.749 | INFO | cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791397097887` (inside 5 minutes of 14:20:48), no traceback. Every other probe OK (sheet HTTP 200, `com.cobalt.aset running loaded, pid 64112`, `com.cobalt.agent running pid 22243 alive`); `AMB com.cobalt.herdr unmanaged` (declared interim).
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.` `<jobs0>`: `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 2.6 h old` (ssd ARMED).
- `launchctl print` aset → `state = running`, `<aset pid>` 64112; radar → `state = running`, `<radar pid>` 64129; `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).`; `ps -p 22243` → `22243 ?? 0:00.04 uv run src/cobalt_agent/main.py`.
- Log baselines: `<a0>` 47 · `<ta0>` 2 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 17 · `<rpr0>` 58 · `<re0>` 40 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS: `dir-long` → 0; `def test_radar_direction_touches_only_strip_and_title` → 0 (both `before`).
- No migration: `<RB>` and D1-M not run.

### STEP-D2
- D2.0 `add` + `commit … -- <REPORT>` → `[main 2e1e8317] docs(report): deploy radar-direction-color-1007 — gate green on 08c6dad1` · `show --stat HEAD` → one file, `deploy-radar-direction-color-1007-attempt2.md | 126 +++`. `<pre-merge>` = `rev-parse --short=8 main` → `2e1e8317`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `<stack-final>` = `8c91922b`; `rev-parse --short=8 8c91922b^2` → `2e1e8317` = `<pre-merge>`; `merge-base --is-ancestor 08c6dad1 8c91922b` → exit 0.
- D2.3 `diff --stat 08c6dad1 8c91922b -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing (docs only).
- D2.4 `backup status` → `newest snapshot: 2.6 h old`; `backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 5589.5 MB` · `ssd: snapshot 77ecb2ee — 0 new / 2 changed, 113.4 MB added, 1 pruned`; `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `date` 14:22:32 EDT · `heartbeat show` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-07 14:22:33 EDT)` (114 s after D1's 14:20:39; `OK radar scanning (rth), members 50`). The 14:22:01–14:22:28 fill reads carried the same `RED radar failed_stage bars: poll failures: 1` as `<hb0>`.
- D2.6 `date` 14:22:37 EDT · `git -C /Users/cobalt/cobalt tag pre-radar-direction-color-1007` at `<pre-merge>` 2e1e8317 → exit 0.

### STEP-4 (the outage)
| step | command | result |
|---|---|---|
| 4.1 | `date` | `<t down>` = 14:22:46 EDT |
| 4.2 | `launchctl bootout gui/501/com.cobalt.aset` · print | exit 0 · `Could not find service "com.cobalt.aset" in domain for user gui: 501` (113) |
| 4.2 | `launchctl bootout gui/501/com.cobalt.radar` · print | exit 0 · `Could not find service "com.cobalt.radar" in domain for user gui: 501` (113) |
| 4.3 | `rev-parse --short=8 HEAD` | `2e1e8317` = `<pre-merge>` |
| 4.3 | `merge --ff-only deploy/radar-direction-color-1007-attempt2` | `Updating 2e1e8317..8c91922b` / `Fast-forward` (4 files, 408+/5-) |
| 4.4 | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | exit 0, `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>` |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | exit 0 · print `state = running`, pid 96145 (≠ 64112) |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` | exit 0 · print `state = running`, pid 96165 (≠ 64129) |
| 4.6 | `date` | `<t up>` = 14:22:57 EDT · downtime 11 s |

## Smoke
- FIRST CALLS after `<t up>`: `<rp_up>` 17 · `<rpr_up>` 58 · `<re_up>` 40 · `<lc_up>` 39.
- (a) [14:22:57 prints, 14:23:08 `date`] `launchctl print` aset → `state = running`, pid 96145 (new, ≠ 64112); radar → `state = running`, pid 96165 (new, ≠ 64129); `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` (agent not in the set, same pid).
- (b) [14:23:09] `grep -c "Started server process" aset.err` → 48 (`<a0>` 47; > 47, ≤ 49). `tail -n 30 aset.err` → `INFO:     Started server process [96151]` … `INFO:     Application startup complete.` / `INFO:     Uvicorn running on http://0.0.0.0:5010 (Press CTRL+C to quit)`. Traceback aset.err 2 = `<ta0>`; Traceback radar.err 0 = `<tr0>`; TaxonomyConfigError 0 = `<tc0>`.
- (c) [14:23:13] `/` → `200` · `/radar` → `200` · `/radar\?frame=phone` → `200` (first attempt each).
- (d) [14:23:15] MARKERS: `grep -c -F "dir-long" …/radar_panel.py` → `2` (after 2) · `grep -c -F "def test_radar_direction_touches_only_strip_and_title" …/test_radar_panel_cards.py` → `1` (after 1).
- (f) `COBALT_ENV=production uv run cobalt jobs restarts 2e1e8317..8c91922b` → exit 0, `RESTARTS: com.cobalt.aset com.cobalt.radar` (= STEP-R), no `UNCLASSIFIED`; `validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.`, `Jobs (F17): 15 registered — 6 resident, 9 one-shot.`
- (g) no migration.
- (s) SMOKE READS: the long tint class → `2` (exit 0, ≥ 1: GREEN); the control test → `1` (exit 0, ≥ 1: GREEN). The control test ran green in the gate (with-DB 4859/0, offline 3975/0).
- (e) read 1 [14:23:22 `date`] `heartbeat show` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-07 14:23:23 EDT)`; `OK radar scanning (rth), members 50`; `com.cobalt.radar running running 0 min, heartbeat fresh`; `com.cobalt.aset running loaded, pid 96145`.
- (b) radar tail 1 [14:24:28 `date`, `<t up>` + 91 s] `tail -n 12 radar.err` → last line `2026-10-07 14:24:20.715 | INFO     | cobalt.radar.runner:resident:467 - radar cycle: scanning scan_id=1791397376589`, preceded by `cards.expire` INFO lines only; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback (counts after: Traceback radar.err 0, S5 40, lifecycle 39 — unchanged). A cycle line stamped after `<t up>` settles (b) GREEN.
- Fill reads 14:23:28–14:24:25: GREEN until 14:24:07, then from 14:24:11 `RED  radar  failed_stage bars: poll failures: 1` — the carried family, same text as `<hb0>`, with `com.cobalt.radar running … heartbeat fresh` and a cycle line inside 5 minutes; not new.

- (e) read 2 [14:25:12 `date`, 110 s after read 1] `heartbeat show` → `HEARTBEAT RED — 1 probe(s)  (2026-10-07 14:25:13 EDT)`; the one RED `RED  radar  failed_stage bars: poll failures: 1` (carried family, as `<hb0>`); `com.cobalt.radar running running 2 min, heartbeat fresh`; `com.cobalt.aset running loaded, pid 96145`. No new RED.
- (h) REVERT-READBACK [14:25:59 `date`, `<t up>` + 182 s]: `radar panel FAILED` 17 = `<rp_up>` · `radar pool refresh FAILED` 58 = `<rpr_up>` · `radar S5 evaluate FAILED` 40 = `<re_up>` · `lifecycle card read failed` 39 = `<lc_up>` — none growing. `/radar` → `200`. Traceback radar.err 0, aset.err 2 (baselines). `tail -n 12 radar.err` → the same 14:24:20.715 `radar cycle: scanning scan_id=1791397376589` line, no failure line. No `census` reads on this card.
- SMOKE: GREEN.

THE CHAIN: every check committed (P2: `83792ec0…`, clean) · tips re-read (P3: `541adf0c` = head) · merged tree (T: `08c6dad1`, one merge, no migration) · RESTARTS derived (R: `com.cobalt.aset com.cobalt.radar`) · three suites green on `08c6dad1` (G: offline 3975/0 · with-DB 4859/0 · live-note 146/0) · `<stack-final>` `8c91922b` = `<m1>` + docs (D2.3) · landed code (4.3 `Updating 2e1e8317..8c91922b`) · markers 0→2, 0→1 (d) · no migration (g) · residents up on new pids after the merge (a) · radar cycling (b, e) · the set's reads (s) · no new failure (h). The card surface (green strip and title for long, red for short) is not readable here; the desk confirms it with him (L70).

### STEP-7 close
- `git -C /Users/cobalt/cobalt tag deploy-2026-10-07-radar-direction-color-attempt2` → exit 0 (after the green smoke). `rev-parse --short=8 main` → `8c91922b`.
- `<pre-merge>` 2e1e8317 → `<stack-final>` 8c91922b · tags `pre-radar-direction-color-1007` (2e1e8317) and `deploy-2026-10-07-radar-direction-color-attempt2` (8c91922b) · `<t down>` 14:22:46 / `<t up>` 14:22:57 / 11 s · uv sync: none in production (the gate's `.venv` was created at STEP-R in `<GATE>`) · proof cost: n/a (no migration) · `migrations applied: none` · `<RB>`: n/a · snapshot `77ecb2ee` · RESTARTS done: com.cobalt.aset com.cobalt.radar.
- THE ROLLBACK STRING (the desk's): 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 8c91922b`, with com.cobalt.aset and com.cobalt.radar down first, up after. 2. SCHEMA: none (no migration). 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.
- PRE-STOP SELF-CHECK: (1) every smoke row above quotes its output with its `date`; (2) `541adf0c` re-read at P3 and `merge-base --is-ancestor 541adf0c 8c91922b` → exit 0; (3) REVERT-READBACK shown at (h), and every count, sha and line in this report was read from tool output this run; (4) STEP-T ran clean (`Merge made by the 'ort' strategy.`), no conflict.
- THE RELEASE: the gate released the lock at its end (`lock released`, `.env: removed`); `ls -la <GATE>/.env` → No such file. Nothing held.
- `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 80c13d52-6dbe-4d0f-bb24-b05b2e6b8e3b` → `context 200237 of 400000 — ok`.

## CONTINUE
done — DEPLOYED (stop line below).

## DECISIONS
1. ASK DESK: at D0, `git status` on main showed `?? .claude/settings.json.bak`. It is not on the ACCEPTED list and not on the REFUSED list (it is not under `src/`, `tests/`, `ops/`, `configs/`), and it is untracked, so it cannot ride the merge. Safe default taken: not a refusal; the run went on. Whether the desk adds it to the accepted list or deletes the file is the desk's call. [14:20:15]

## RECORDS
- Downtime: 11 s (14:22:46 → 14:22:57), under 300 s.
- `cobalt_dev: 0013 (F2 = F0)`, with F0 = F2 = `664 35 272c95bbb12241e3611e4b36326ccf87`.
- Carried RED, as read: `RED  radar  failed_stage bars: poll failures: 1`, at D1 (14:20:39), at the D2.5 fill reads and after `<t up>` from 14:24:11. GREEN at D2.5 (14:22:33) and at (e) read 1 (14:23:23).
- No `RETIRE OWED`: no plist changed. No `REFUSED, not needed` lines. No message from another session.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-radar-direction-color-1007-attempt2` and branch `deploy/radar-direction-color-1007-attempt2`; the set's branch `ops/radar-direction-color-1007` and its worktree, if any.
- Push is his (L55): `main` at `8c91922b` plus this report's commit, and the two tags, are local only.
- L74: one attribution block asked for a `Claude-Session:` commit line. It is recorded under `## L74` and was not acted on.
- Card RECORDS (the desk's, copied):
  - radar-direction-color: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-direction-color-check-2026-10-07.md` last line: CHECK DONE · job: radar-direction-color · pass: 1 · tip: 541adf0c · house A: Sol FINDINGS: 2 · findings: 3 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 2 · house B: Grok FINDINGS: 1 · suites: offline 3975/0 · with-DB 4859/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 13 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 148149
  - radar-direction-color: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/radar-direction-color-1007` → `541adf0c`; code tip `541adf0c`
  - written by deploy-card.sh at 2026-10-07 12:30 ET (`date`); trial merge of the heads onto main in order: clean

DEPLOYED deploy-2026-10-07-radar-direction-color-attempt2 8c91922b | set: none | migrations: none | gate: offline 3975/0 · with-DB 4859/0 · live-note 146/0 | RESTARTS: com.cobalt.aset com.cobalt.radar | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 200237
