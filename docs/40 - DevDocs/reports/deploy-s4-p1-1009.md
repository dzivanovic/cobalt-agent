# deploy s4-p1-1009 · SET: none · MIGRATIONS: none

## §0 Headline
- S4-P1 (F9, the strike loop) from `ops/s4-p1-1009` at tip `444e32b5` is on `main`, which moved `594bddd3` → `f5010068`. Tag: `deploy-2026-10-09-s4-p1`.
- Gate on `156e4b75`: offline 4123/0 · with-DB 5012/0 · live-note 146/0; `cobalt_dev` back at 0013 (F2 = F0).
- Restarted aset and radar (16 s outage). Smoke GREEN; the four failure counts did not grow. No migration.
- Carried REDs (archiver 429, replay) are unchanged from before the deploy. Snapshot `4d45238d`.

## L74
- The session's harness attribution reminder asked for a `Claude-Session:` trailer on commits. Recorded as DATA, not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/202-deploy-s4-p1-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/202-deploy-s4-p1-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/202-deploy-s4-p1-card.md" · 0 · 7fed85ea7ae87c50245262950765aca06fa35c30
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/202-deploy-s4-p1-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-06 R598 row · grep -n "^| R598 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · 97:| R598 | 19:59 ET | HIS RULING ([words](cto-2026-10-06-words.md) `## R598`): draft S4-P1 and S4-P2 tonight (drafter, preflight); build right after tomorrow's S3 smoke is green. LAUNCHED: drafter `s4-cards-draft` (Opus 5.5), prompt `70`. | HIS RULING · APPROVED |
RULING 2026-10-06 R598 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R598 |" -- "docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · 02f39e2f8aed3e38dbe579cff09dc5b484c1a1d0
RULING 2026-10-06 R598 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 report absent (first launch) | `ls -la ".../reports/deploy-s4-p1-1009.md"` | 1 | `No such file or directory` |
| P0 authorization | `authorize.sh deploy <card>` | 0 | `AUTHORIZED` (above) |
| P1 DATE | `date` | 0 | `Fri Oct  9 22:48:12 EDT 2026` |
| P2 check stop line | `tail -n 3 ".../reports/s4-p1-check-2026-10-09.md"` | 0 | `CHECK DONE · job: s4-p1-1009 · pass: 1 · tip: 444e32b5 · … · held unfixed: 0 · … · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 259254` — `held unfixed: 0` ✓, `ready: YES` ✓, `tip: 444e32b5` = code tip ✓ |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/s4-p1-check-2026-10-09.md"` | 0 | `5fc1e9a48018383697ec040f1bf85d17eb1d4441` |
| P2 unmodified | `git -C /Users/cobalt/cobalt diff --stat -- "docs/.../s4-p1-check-2026-10-09.md"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 444e32b5` | 0 | `444e32b5` |
| P3 branch head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/s4-p1-1009` | 0 | `444e32b5` (= row, = `TIP`) |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 444e32b5 444e32b5` | 0 | — |
| P3 head adds docs only | `git -C /Users/cobalt/cobalt diff --stat 444e32b5 444e32b5 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no lock held |
| P5 gate status | `git -C /Users/cobalt/cobalt-wt/deploy-s4-p1-1009 status --short --branch` | 0 | `## deploy/s4-p1-1009` |
| P5 m0 | `git -C /Users/cobalt/cobalt-wt/deploy-s4-p1-1009 rev-parse --short=8 HEAD` | 0 | `7fed85ea` = `<m0>` |
| P5 m0 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 7fed85ea main` | 0 | — |
| P5 gate empty vs main | `git -C /Users/cobalt/cobalt log --oneline main..deploy/s4-p1-1009` | 0 | empty |
| P6 marker | `grep -c -F "def start_strike_thread" /Users/cobalt/cobalt/src/cobalt/radar/runner.py` | 1 | `0` (= before) |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main 444e32b5 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none ✓) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 55969` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 55984` |
| P8 aset plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | `/Users/cobalt/cobalt/ops/com.cobalt.aset.plist` |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-s4-p1-1009 merge --no-edit 444e32b5` → `Merge made by the 'ort' strategy.` (29 files changed, 2591 insertions(+), 5 deletions(-))
- `git -C /Users/cobalt/cobalt-wt/deploy-s4-p1-1009 rev-parse --short=8 HEAD` → `156e4b75` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 7fed85ea..deploy/s4-p1-1009` → `156e4b75 Merge commit '444e32b5' into deploy/s4-p1-1009`
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor 444e32b5 deploy/s4-p1-1009` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat 7fed85ea deploy/s4-p1-1009 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none ✓)
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 7fed85ea deploy/s4-p1-1009 -- configs ops` →
```
 configs/cobalt/taxonomy/tunables.yaml | 40 +++++++++++++++++++++++++++++++++++
 ops/desk/gate-lists.md                |  4 ++--
 2 files changed, 42 insertions(+), 2 deletions(-)
```
  No plist added, modified or removed.

## RESTARTS
`cd /Users/cobalt/cobalt-wt/deploy-s4-p1-1009` · `ls -la …/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created the worktree `.venv`: `Installed 253 packages in 820ms`):
```
path	change	rule	restart
configs/cobalt/taxonomy/tunables.yaml	M	resident reads	com.cobalt.aset,com.cobalt.radar
docs/... (11 rows)	M/A	DOCS	-
ops/desk/gate-lists.md	M	operator script; no Cobalt reader	-
src/cobalt/cards/store.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/radar/runner.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/strike/__init__.py	A	static import reach	com.cobalt.radar
src/cobalt/strike/cli.py	A	static import reach	com.cobalt.radar
src/cobalt/strike/config.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/strike/detector.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/strike/measure.py	A	static import reach	com.cobalt.radar
src/cobalt/strike/policy.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/... (9 rows)	M/A	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.aset com.cobalt.radar`.

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 444e32b5 156e4b75 -- . ":(exclude)docs"` → 10 files (`configs/cobalt/rules.yaml`, `src/cobalt/voice/{agent,tools,turn,web}.py`, voice tests, fixture) — main moved since the check; the clause does not hold, the gate runs whole (`--deploy`).
- Deselect from the build report (`s4-p1-build-2026-10-09.md:126`): `tests/cobalt/test_strike_detector_db.py`. Card `TICKERS: none` → no `--tickers`; `MIGRATIONS: none` → no `--migration`.
- (a0) `ls -la …/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `262 passed, 163 skipped in 16.85s` (0 failed; the skips are with-DB tests, `Postgres env settings not available` / `requires_db`).
- `ls -la …/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-s4-p1-1009 all --deploy --deselect tests/cobalt/test_strike_detector_db.py` (background) → exit 0, verdict lines WHOLE:
```
offline 4123/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5012/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-s4-p1-1009-all-20261009-224956.log
```
- Log reads (`grep -n -F`): (a) offline `4123 passed, 792 skipped, 1 xfailed` (:870) · `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (:887) · (c) pass 1 `4815 passed, 7 skipped, 91 deselected, 3 xfailed` (:1098) · (c2) `dev forward: APPLIED 23:14:16` (:1100) · (c3) pass 2 `197 passed, 1 deselected` (:1913), with `PASSED tests/cobalt/test_strike_detector_db.py::test_an_armed_radar_card_is_triggered_by_one_tick` (:1911) and `…::test_a_watch_radar_card_whose_bars_cross_is_missed` (:1912) · (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (:1979), `cobalt_dev: 0013 — F2 = F0` (:2030), `lock released` (:2032) · (e) live-note `146 passed, 1 skipped` (:2101).
- SKIPS: all 7 inside the allowed set; `test_s3_c4_experiments.py:95` is `test_x14_live_his_template_strips_to_the_committed_fixture` (read at the source, line 96). Live-note's 1 skip is the `COBALT_TEST_LIVE_DRC` one (allowed).
- THE RELEASE: `ls -la /Users/cobalt/cobalt-wt/deploy-s4-p1-1009/.env` → No such file; `grep -c -x -F "deploy-s4-p1-1009" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `0`. `.env: removed (L76 lock released, log :2032)`.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 156e4b75 (`date` → `Fri Oct  9 23:19:24 EDT 2026`): offline 4123/0 · with-DB 5012/0 (4815 + 197) · live-note 146/0.

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| main branch | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 17]` |
| main dirty | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`; ` M` / `??` under `docs/40 - DevDocs/` only; `?? .claude/settings.json.bak` (outside `src/ tests/ ops/ configs/`, not refused — recorded); no staged line |
| main moved | `git -C /Users/cobalt/cobalt diff --stat 7fed85ea main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| probe | `tag scratch-allow-probe-s4-p1-1009` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-s4-p1-1009' (was 7fed85ea)` |
| probe | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 6ee5185c] scratch: …` · — · `7fed85ea docs(desk): S4-P1 deploy card 202` |
| TAG free | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/deploy-2026-10-09-s4-p1` | 1 | — |
| rollback tag free | `git -C /Users/cobalt/cobalt rev-parse --verify --quiet refs/tags/pre-s4-p1-1009` | 1 | — |

### STEP-D1 baseline
- `date` → `Fri Oct  9 23:19:50 EDT 2026` · `COBALT_ENV=production uv run cobalt heartbeat show` → `<hb0>`: `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-09 23:19:52 EDT)`. RED lines: `RED  archiver  last run FAILED — last run 2026-10-10 00:54 UTC (2.4 h ago), rows written 3308843, exit 1` · `RED  com.cobalt.archiver  failed  RuntimeError: 18 archiver failure(s): DKNG/i2: Fetch failed for DKNG/i2: Finviz HTTP failed: Client error '429 Too Many Requests' …` · `RED  com.cobalt.replay  failed  ReplayError: archiver not done: state 'failed'`. Named, not a stop (not the aset / sheet / radar probe). `OK sheet HTTP … -> 200` · `OK radar idle (overnight)` · `OK com.cobalt.aset running loaded, pid 55969` · `OK com.cobalt.radar running running 37 min, heartbeat fresh` · `OK com.cobalt.agent running pid 22243 alive` · `AMB com.cobalt.herdr unmanaged …`.
- `COBALT_ENV=production uv run cobalt validate` → exit 0, `<val0>` (no `docs/_inflight/` line; ends `Placement (docs/PLACEMENT.md): tree clean.`); `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 0.6 h old` (ssd local ARMED).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 55969` · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 55984` · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ??  0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → 8 lines `radar cycle: idle:overnight scan_id=None`, last `2026-10-09 23:19:28.911`; no traceback.
- Counts: `<a0>` Started server process (aset.err) `55` · `<ta0>` Traceback (aset.err) `2` · `<tr0>` Traceback (radar.err) `0` · `<tc0>` TaxonomyConfigError `0` · `<rp0>` radar panel FAILED `18` · `<rpr0>` radar pool refresh FAILED `60` · `<re0>` radar S5 evaluate FAILED `43` · `<lc0>` lifecycle card read failed `39`.
- `curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/radar` → `200` · marker `grep -c -F "def start_strike_thread" …/runner.py` → `0` (before ✓).
- MIGRATIONS: none → no `<RB>`, no D1-M.

### STEP-D2
- D2.0 `git -C /Users/cobalt/cobalt add "docs/40 - DevDocs/reports/deploy-s4-p1-1009.md"` · `commit … -- "<report>"` → `[main 594bddd3] docs(report): deploy s4-p1-1009 — gate green on 156e4b75` · `show --stat HEAD` → that one file (148 insertions) · `rev-parse --short=8 main` → `594bddd3` = `<pre-merge>`.
- D2.1 `git -C /Users/cobalt/cobalt-wt/deploy-s4-p1-1009 merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `rev-parse --short=8 HEAD` → `f5010068` = `<stack-final>`; `rev-parse --short=8 f5010068^2` → `594bddd3` = `<pre-merge>` ✓; `merge-base --is-ancestor 156e4b75 f5010068` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat 156e4b75 f5010068 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing ✓.
- D2.4 `backup status` → `newest snapshot: 0.6 h old` · `COBALT_ENV=production uv run cobalt backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 6694.4 MB` · `ssd: snapshot 4d45238d — 0 new / 2 changed, 27.5 MB added, 1 pruned` · `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `date` → `23:21:41` · `heartbeat show` → `(2026-10-09 23:21:43 EDT)`, 111 s after D1's `23:19:52`; RED lines identical to `<hb0>` (archiver, com.cobalt.archiver, com.cobalt.replay); aset / sheet / radar probes OK. No new RED. (Clock filled with two more `heartbeat show` reads at 23:21:33 and 23:21:38, same content.)
- D2.6 `date` → `Fri Oct  9 23:21:47 EDT 2026` · `git -C /Users/cobalt/cobalt tag pre-s4-p1-1009` → `rev-parse --short=8 pre-s4-p1-1009` → `594bddd3`.

### STEP-4 — the outage
| step | command | result |
|---|---|---|
| 4.1 | `date` | `Fri Oct  9 23:22:00 EDT 2026` = `<t down>` |
| 4.2 | `launchctl bootout gui/501/com.cobalt.aset` · `launchctl print …/com.cobalt.aset` | — · exit 113 `Could not find service "com.cobalt.aset" in domain for user gui: 501` |
| 4.2 | `launchctl bootout gui/501/com.cobalt.radar` · `launchctl print …/com.cobalt.radar` | — · exit 113 `Could not find service "com.cobalt.radar" in domain for user gui: 501` |
| 4.3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` | `594bddd3` = `<pre-merge>` |
| 4.3 | `git -C /Users/cobalt/cobalt merge --ff-only deploy/s4-p1-1009` | `Updating 594bddd3..f5010068` / `Fast-forward` (29 files changed, 2591 insertions(+), 5 deletions(-)) |
| 4.4 | — | `migrations applied: none` (MIGRATIONS: none) |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | exit 0; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`; new block `Strike (S4-P1): 4 tunables rows resolved.`; engine tunables `92` (was `88`); `Placement (docs/PLACEMENT.md): tree clean.` |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | — (no retry needed) |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` | — (no retry needed) |
| 4.6 | `launchctl print gui/501/com.cobalt.aset` | `state = running`, `pid = 79051` (≠ 55969) |
| 4.6 | `launchctl print gui/501/com.cobalt.radar` | `state = running`, `pid = 79064` (≠ 55984) |
| 4.6 | `date` | `Fri Oct  9 23:22:16 EDT 2026` = `<t up>` — downtime 16 s |

## Smoke
- FIRST CALLS after `<t up>` 23:22:16: `<rp_up>` `18` · `<rpr_up>` `60` · `<re_up>` `43` · `<lc_up>` `39` (each = its D1 baseline).
- (a) `date` 23:22:32 · `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 79051` (NEW, ≠ 55969) · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 79064` (NEW, ≠ 55984) · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` (agent not in the set: same pid). GREEN.
- (b) `date` 23:22:35 · `grep -c "Started server process" …/aset.err` → `56` (`<a0>` 55; > 55, ≤ 57 ✓) · `tail -n 30 …/aset.err` → last `INFO:     Started server process [79058]` followed by `2026-10-09 23:22:13.388 | INFO | cobalt.voice.web:voice_startup:183 - voice: scratch dir … locked by this process; start sweep deleted 0 file(s), 0 failed`, `INFO:     Application startup complete.`, `INFO:     Uvicorn running on http://0.0.0.0:5010 (Press CTRL+C to quit)` ✓ · Traceback aset.err `2` (= `<ta0>`) · Traceback radar.err `0` (= `<tr0>`) · TaxonomyConfigError `0` (= `<tc0>`).
- (c) `date` 23:22:39 · `curl … http://127.0.0.1:5010/` → `200` · `…/radar` → `200` · `…/radar\?frame=phone` → `200` (first attempt each). GREEN.
- (d) MARKER `grep -c -F "def start_strike_thread" /Users/cobalt/cobalt/src/cobalt/radar/runner.py` → `1` (after ✓).
- (f) `date` 23:22:43 · `COBALT_ENV=production uv run cobalt jobs restarts 594bddd3..f5010068` → exit 0, same table as STEP-R, no `UNCLASSIFIED`, `RESTARTS: com.cobalt.aset com.cobalt.radar` (= `<restart set>`) · `COBALT_ENV=production uv run cobalt validate` → exit 0, as 4.5 (`Jobs (F17): 15 registered — 6 resident, 9 one-shot.`; `Strike (S4-P1): 4 tunables rows resolved.`; `Placement … tree clean.`). GREEN.
- (s) SMOKE READS: the strike loop starter, `grep -c -F "def start_strike_thread" /Users/cobalt/cobalt/src/cobalt/radar/runner.py` → exit 0, `1` (green: a count of 1 or more). GREEN.
- (e) first: `heartbeat show` `(2026-10-09 23:22:46 EDT)` → RED lines = `<hb0>`'s three (archiver, com.cobalt.archiver, com.cobalt.replay); `OK com.cobalt.aset running loaded, pid 79051` · `OK com.cobalt.radar running running 1 min, heartbeat fresh` · `OK radar idle (overnight)` · `OK sheet HTTP … -> 200`.
- (b) radar tail 1: `date` 23:23:48 (`<t up>` + 92 s) · `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` → startup lines (vault unlock, finviz token resolved) and `2026-10-09 23:22:14.966 | INFO | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None`; no traceback, no `S5 evaluate FAILED`, no `lifecycle card read failed`. That cycle line is stamped 1 s BEFORE `<t up>` (the bootstrap returned at ~23:22:14, `date` read 23:22:16): not settling; tail 2 decides.
- (e) second: `date` 23:24:36 · `heartbeat show` `(2026-10-09 23:24:38 EDT)`, 112 s after the first → RED lines the same three as `<hb0>`; no new RED; `OK com.cobalt.radar running running 2 min, heartbeat fresh`; `OK com.cobalt.aset running loaded, pid 79051`. GREEN. (Clock filled with `date` + `heartbeat show` pairs 23:22:56–23:24:33, same content each.)
- (b) radar tail 2: `date` 23:25:19 (`<t up>` + 183 s) · `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` → last line `2026-10-09 23:23:54.987 | INFO | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` — a cycle line stamped after `<t up>`, no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback. (b) SETTLED GREEN.
- (g) no migration — not run.
- (h) REVERT-READBACK `date` 23:25:22 (`<t up>` + 186 s, after (b) settled): `radar panel FAILED` `18` = `<rp_up>` · `radar pool refresh FAILED` `60` = `<rpr_up>` · `radar S5 evaluate FAILED` `43` = `<re_up>` · `lifecycle card read failed` `39` = `<lc_up>` · `curl … /radar` → `200`. No `census` reads on the card. No growing count. GREEN.

SMOKE: GREEN.

THE CHAIN: every check committed (P2: `5fc1e9a4…`, unmodified, `held unfixed: 0` · `ready: YES`) → the tips (P3: `444e32b5` = code tip = head) → the merged tree (T: `156e4b75`, one merge, no migration) → RESTARTS derived (R: `com.cobalt.aset com.cobalt.radar`, no UNCLASSIFIED) → three suites green on `<m1>` (G: offline 4123/0 · with-DB 5012/0 · live-note 146/0, `F2 = F0`) → `<stack-final>` `f5010068` = `<m1>` + docs (D2.3: nothing) → the landed code (4.3: `Updating 594bddd3..f5010068`) → marker (d: `0` → `1`) → no migration (g) → residents up after the merge with new pids (a: aset 79051, radar 79064) → radar cycling (b: 23:23:54 cycle; e: heartbeat fresh, no new RED) → the set's read (s: `1`) → no new failure (h: four counts unchanged). The card surface is not readable here; the desk confirms it with him (L70).

### Deploy close (STEP-7)
| field | value |
|---|---|
| merge | `<pre-merge>` `594bddd3` → `<stack-final>` `f5010068` (fast-forward) |
| tags | `pre-s4-p1-1009` at `594bddd3` · `deploy-2026-10-09-s4-p1` at `f5010068` |
| outage | `<t down>` 23:22:00 · `<t up>` 23:22:16 · 16 s |
| uv sync | none in production (the gate worktree's `.venv` was created at STEP-R: `Installed 253 packages in 820ms`) |
| proof cost | n/a (no migration) |
| migrations applied | none |
| `<RB>` | n/a |
| snapshot | `4d45238d` (ssd; `cobalt_brain` 6694.4 MB) |
| RESTARTS done | `com.cobalt.aset com.cobalt.radar` |
| ROLLBACK STRING | 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 f5010068` — aset and radar down first, up after. 2. SCHEMA: none (no migration). 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`. |

### PRE-STOP SELF-CHECK
1. Every smoke row's evidence is quoted above with its `date` (23:22:32 a · 23:22:35 b · 23:22:39 c/d · 23:22:43 f/s · 23:22:46 e1 · 23:23:48 b-tail1 · 23:24:38 e2 · 23:25:19 b-tail2 · 23:25:22 h).
2. Code tip and head `444e32b5` re-read at P3 (`rev-parse` → `444e32b5` both); `git -C /Users/cobalt/cobalt merge-base --is-ancestor 444e32b5 f5010068` → exit 0.
3. REVERT-READBACK (h) shown: four counts 18/60/43/39 = `<rp_up>`/`<rpr_up>`/`<re_up>`/`<lc_up>`; every count, sha and `file:line` in this report was read from tool output this run.
4. No conflict marker: STEP-T `Merge made by the 'ort' strategy.`, D2.1 the same; `grep -c -F "<<<<<<<" /Users/cobalt/cobalt/src/cobalt/radar/runner.py` → `0`.
5. THE RELEASE: done at STEP-G (gate's `.env: removed`, `cobalt_dev: 0013 — F2 = F0`); the lock is not held by this run.

## CONTINUE
- D2 done (pre-merge 594bddd3, stack-final f5010068, tag pre-s4-p1-1009).
- OUTAGE STARTING 23:21:47 ET — residents of com.cobalt.aset com.cobalt.radar going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
- OUTAGE ENDED 23:22:16 ET (16 s): main at f5010068, aset pid 79051, radar pid 79064 running.
- next: none — smoke GREEN, tag set, report committed (STEP-7).

## DECISIONS
none

## RECORDS
- Downtime 16 s (23:22:00 → 23:22:16 ET); under 300 s.
- `REFUSED, not needed`: none. Messages not followed: none (no `CONTINUE` message arrived).
- `cobalt_dev: 0013 (F2 = F0)` — `F0`/`F2` `664 35 272c95bbb12241e3611e4b36326ccf87` (gate log :887, :1979).
- `RETIRE OWED`: none (no plist removed).
- Carried RED as read at D1 and through smoke (not the radar family; not aset/sheet/radar probes): `RED archiver last run FAILED — … exit 1`; `RED com.cobalt.archiver failed RuntimeError: 18 archiver failure(s): DKNG/i2: … Finviz HTTP failed: Client error '429 Too Many Requests' …`; `RED com.cobalt.replay failed ReplayError: archiver not done: state 'failed'`. Unchanged across the deploy; the desk's to chase.
- Gate stray-rows read: `stray rows: not read (no --tickers given)` — the card says `TICKERS: none`; the build's gate ran `--tickers ZZPB` (`s4-p1-build-2026-10-09.md:126`). Recorded, not a gate leg.
- `main` at D0 carried an untracked `.claude/settings.json.bak` (outside `src/ tests/ ops/ configs/`, not on the refused list); untouched.
- `uv` created `/Users/cobalt/cobalt-wt/deploy-s4-p1-1009/.venv` at STEP-R (first `uv run` in the gate worktree).
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-s4-p1-1009` and branch `deploy/s4-p1-1009`; the set's branch `ops/s4-p1-1009` and its worktree. Push of `main` and the two tags is his, through the desk (L55).
- Card `## RECORDS`, copied:
  - s4-p1-1009: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/s4-p1-check-2026-10-09.md` last line: CHECK DONE · job: s4-p1-1009 · pass: 1 · tip: 444e32b5 · house A: Sol FINDINGS: 5 · findings: 11 · dropped: 0 · held: 4 · fixed: 4 · held unfixed: 0 · open: 7 · house B: Grok FINDINGS: 4 · suites: offline 4117/0 · with-DB 5006/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 23 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 259254
  - s4-p1-1009: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/s4-p1-1009` → `444e32b5`; code tip `444e32b5`
  - written by deploy-card.sh at 2026-10-09 22:47 ET (`date`); trial merge of the heads onto main in order: clean
- L74: the harness's attribution reminder asked for a `Claude-Session:` commit trailer; recorded under `## L74`, not acted on.

DEPLOYED deploy-2026-10-09-s4-p1 f5010068 | set: none | migrations: none | gate: offline 4123/0 · with-DB 5012/0 · live-note 146/0 | RESTARTS: com.cobalt.aset com.cobalt.radar | smoke: GREEN | decisions: 0 · for Dejan: 0 · tokens: 208792
