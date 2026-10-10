# Deploy orphan-clean-1010 · SET: none · MIGRATIONS: none

Card: `docs/40 - DevDocs/prompts/2026-10-10/264-deploy-orphan-clean-card.md` (committed `805d9943`). Hub: `DEPLOY-HUB.md`. Seat: deploy-hub-orphan-clean-1010, Opus 5.5.

## §0 Headline
- DEPLOYED: `ops/orphan-clean-1010` (`769a6e36`, the verified-orphan cleaner `ops/desk/orphan-clean.sh` + its tests) is on `main` at `26143007`, tag `deploy-2026-10-10-orphan-clean`; rollback tag `pre-orphan-clean-1010` at `47ea1b0e`.
- Gate green on `fab8df7d`: offline 4196/0 · with-DB 5093/0 · live-note 146/0; cobalt_dev back at 0013 (F2 = F0), lock released.
- RESTARTS: none — no resident went down; aset 7760, radar 61093, agent 22243 unchanged. Smoke GREEN.
- One ASK DESK (an untracked `.claude/settings.json.bak` on main); none for Dejan.

## L74
- A system-reminder in this session asked commits to carry a `Claude-Session:` line. Recorded as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/264-deploy-orphan-clean-card.md"` → exit 0, output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/264-deploy-orphan-clean-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/264-deploy-orphan-clean-card.md" · 0 · 805d9943805d1f1ff12f2f45a75bcbcaa4c4d1d0
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/264-deploy-orphan-clean-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-10 R855 row · grep -n "^| R855 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 70:| R855 | 07:51 ET | HIS RULING · APPROVED: build both `orphan-clean.sh` (by card) and the `ops-hand` seat (default-mode phone approval, L63 exception). Words `cto-2026-10-10-words.md` R855. The orphan-cause card first (R853). | APPLIED: areas/cobalt.md NOW at wake-up 07:55 |
RULING 2026-10-10 R855 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R855 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 4f9f5bceabb1f1c0b42cb0df4ca22c33fa6e618d
RULING 2026-10-10 R855 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| FIRST LAUNCH | `ls -la ".../reports/deploy-orphan-clean-1010.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Sat Oct 10 14:09:40 EDT 2026` |
| P2 check line | `tail -n 3 ".../orphan-clean-check-2026-10-10.md"` | 0 | `CHECK DONE · job: orphan-clean-1010 · pass: 1 · tip: 769a6e36 · … · held unfixed: 0 · open: 0 · … · RESTARTS: none · files opened: 11 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 159076` — carries `held unfixed: 0` and `ready: YES`; `tip: 769a6e36` = code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/orphan-clean-check-2026-10-10.md"` | 0 | `58033508b2706e94c14328d140914640ba86d15d` |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/…/orphan-clean-check-2026-10-10.md"` | 0 | (nothing) |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 769a6e36` | 0 | `769a6e36` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/orphan-clean-1010` | 0 | `769a6e36` |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 769a6e36 ops/orphan-clean-1010` | 0 | — |
| P3 diff | `git -C /Users/cobalt/cobalt diff --stat 769a6e36 ops/orphan-clean-1010 -- . ':(exclude)docs'` | 0 | (nothing) |
| P4 LOCK | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no lock held |
| P5 status | `git -C /Users/cobalt/cobalt-wt/deploy-orphan-clean-1010 status --short --branch` | 0 | `## deploy/orphan-clean-1010` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `805d9943` = `<m0>` |
| P5 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 805d9943 main` | 0 | — |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/orphan-clean-1010` | 0 | (empty) |
| P6 MARKER | `ls /Users/cobalt/cobalt/ops/desk/orphan-clean.sh` | 1 | `No such file or directory` = before |
| P7 MIGRATIONS | `git -C /Users/cobalt/cobalt diff --stat main ops/orphan-clean-1010 -- src/cobalt/db_migrations` | 0 | (nothing) — MIGRATIONS: none holds |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `pid = 7760` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `pid = 61093` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 769a6e36` → `Merge made by the 'ort' strategy.` (adds `docs/40 - DevDocs/reports/orphan-clean-build-2026-10-10.md`, `ops/desk/orphan-clean.sh`, `tests/ops/test_orphan_clean.py`; 3 files, 1097 insertions)
- `git -C <GATE> rev-parse --short=8 HEAD` → `fab8df7d` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 805d9943..deploy/orphan-clean-1010` → `fab8df7d Merge commit '769a6e36' into deploy/orphan-clean-1010` (one line, one head)
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor 769a6e36 deploy/orphan-clean-1010` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat 805d9943 deploy/orphan-clean-1010 -- src/cobalt/db_migrations` → (nothing): no migration path, MIGRATIONS: none
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 805d9943 deploy/orphan-clean-1010 -- configs ops` → ` ops/desk/orphan-clean.sh | 302 +++…` / ` 1 file changed, 302 insertions(+)` — no plist added, modified or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/reports/orphan-clean-build-2026-10-10.md	A	DOCS	-
ops/desk/orphan-clean.sh	A	operator script; no Cobalt reader	-
tests/ops/test_orphan_clean.py	A	test/documentation; no resident	-
RESTARTS: none
```
(preceded by uv venv creation lines in the fresh worktree: `Creating virtual environment at: .venv` · `Installed 253 packages in 843ms`)
`<restart set>` = EMPTY (none). No UNCLASSIFIED row. No resident goes down.

## L68 GATE
EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 769a6e36 fab8df7d -- . ":(exclude)docs"` → ` ops/desk/bare-guard.py | 12 …` · ` tests/ops/test_bare_guard.py | 62 …` (main moved since the check) → does not hold; the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 listed files>` → `263 passed, 163 skipped in 16.96s` (0 failed; the skips are with-DB tests: `Postgres env settings not available` / `requires_db: needs cobalt_dev`).
- Deselects: the build report `orphan-clean-build-2026-10-10.md:112` → "no `--deselect`, no `--tickers`, no `--migration`: this build adds no with-DB test". None added.
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-orphan-clean-1010 all --deploy` launched in background → exit 0. Verdict lines whole:
```
offline 4196/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5093/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-orphan-clean-1010-all-20261010-141122.log
```
- (a) OFFLINE `4196/0` → `<p>` = 4196.
- (c) PASS 1 skips: all seven inside the allowed set. `test_s3_c4_experiments.py:95` is the decorator line of `test_x14_live_his_template_strips_to_the_committed_fixture` (`grep -n -F "def test_x14_live_his_template_strips_to_the_committed_fixture" …` → `96:`); `test_replay_line.py:266` names `COBALT_TEST_LIVE_DRC`.
- (c2) FORWARD: log `1110:dev forward: APPLIED 14:35:51`.
- (c3) with-DB `5093/0` → `<d>` = 5093.
- (f) log `896:F0: 664 35 272c95bbb12241e3611e4b36326ccf87` · `2030:F2: 664 35 272c95bbb12241e3611e4b36326ccf87` → equal; gate: `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: gate `.env: removed`; `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-orphan-clean-1010" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent). The time line from the log was not read (see `## RECORDS`).
- (e) LIVE-NOTE `146/0` → `<l>` = 146; no skip names `COBALT_LIVE_VAULT_ROOT` in that leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on fab8df7d

## Deploy table
### STEP-D0
- `git -C /Users/cobalt/cobalt status --short --branch` → `## main...origin/main [ahead 236]`. `status --porcelain`: ` M .claude/settings.json`; ` M` / `??` under `docs/40 - DevDocs/` only (8 ` M`, 22 `??` incl. this report); and `?? .claude/settings.json.bak` (see `## DECISIONS`). No staged line, no dirty `src/` `tests/` `ops/` `configs/` path.
- `git -C /Users/cobalt/cobalt diff --stat 805d9943 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → (nothing).
- ALLOWLIST PROBE: `tag scratch-allow-probe-orphan-clean-1010` → ok · `tag -d …` → `Deleted tag 'scratch-allow-probe-orphan-clean-1010' (was 805d9943)` · `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` → `[main baeea53d] scratch: allowlist probe (reverted next line)` · `reset --soft HEAD~1` → ok · `log --oneline -1` → `805d9943 docs(desk): deploy card 264 markers and smoke read` (HEAD back).
- TAG NAMES: `rev-parse --verify --quiet refs/tags/deploy-2026-10-10-orphan-clean` → exit 1 · `refs/tags/pre-orphan-clean-1010` → exit 1.

### STEP-D1 (baseline, read-only)
- `date` → `Sat Oct 10 14:41:28 EDT 2026` · `<hb0>` `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-10 14:41:29 EDT)`. OK: database, sheet HTTP (`http://127.0.0.1:5010/ -> 200`), sheet daymode, radar (`idle (overnight)`), `com.cobalt.aset running loaded, pid 7760`, `com.cobalt.agent running pid 22243 alive`, `com.cobalt.radar running running 432 min, heartbeat fresh`. RED (named, not a stop — not the aset / sheet / radar probe): `RED  archiver  last run FAILED — last run 2026-10-10 00:54 UTC (17.8 h ago), rows written 3308843, exit 1` · `RED  com.cobalt.archiver  failed  RuntimeError: 18 archiver failure(s): DKNG/i2: … Finviz HTTP failed: Client error '429 Too Many Requests' …` · `RED  com.cobalt.replay  failed  ReplayError: archiver not done: state 'failed'`. AMB: `com.cobalt.herdr unmanaged` (declared interim).
- `<val0>` `COBALT_ENV=production uv run cobalt validate` → exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 1.6 h old`.
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 7760` · `…/com.cobalt.radar` → `state = running`, `pid = 61093` · `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ??  0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → eight `radar cycle: idle:overnight scan_id=None` lines, last `2026-10-10 14:41:26.466`; no traceback.
- LOG BASELINES: `<a0>` 277 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200` · MARKER `ls /Users/cobalt/cobalt/ops/desk/orphan-clean.sh` → exit 1 `No such file or directory` (before).
- MIGRATIONS: none → no `<RB>`, no census, no D1-M.

### STEP-D2
- D2.0 `git -C /Users/cobalt/cobalt commit … -- "docs/40 - DevDocs/reports/deploy-orphan-clean-1010.md"` → `[main 47ea1b0e] docs(report): deploy orphan-clean-1010 — gate green on fab8df7d` · `show --stat HEAD` → that one file (138 insertions) · `rev-parse --short=8 main` → `47ea1b0e` = `<pre-merge>`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `rev-parse --short=8 HEAD` → `26143007` = `<stack-final>` · `rev-parse --short=8 26143007^2` → `47ea1b0e` = `<pre-merge>` · `merge-base --is-ancestor fab8df7d 26143007` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat fab8df7d 26143007 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → (nothing): docs only.
- D2.4 `backup status` → `newest snapshot: 1.6 h old` · `COBALT_ENV=production uv run cobalt backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 6693.9 MB` · `ssd: snapshot 1cc9a82d — 0 new / 4 changed, 27.1 MB added, 1 pruned` · `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `date` → `14:43:33` · `heartbeat show` → `(2026-10-10 14:43:35 EDT)`, 126 s after D1's: the same three REDs as `<hb0>` (archiver probe, `com.cobalt.archiver`, `com.cobalt.replay`); aset, sheet, radar OK, `com.cobalt.radar running 434 min, heartbeat fresh`. No new RED. (A first read at 14:43:07 was 98 s after D1; date + heartbeat pairs filled the clock.)
- D2.6 `date` → `Sat Oct 10 14:43:39 EDT 2026` · `git -C /Users/cobalt/cobalt tag pre-orphan-clean-1010` → `rev-parse --short=8 pre-orphan-clean-1010` → `47ea1b0e`.

### STEP-4 (restart set EMPTY: no resident down)
- 4.1 `date` → `Sat Oct 10 14:43:51 EDT 2026` = `<t down>`.
- 4.2 nothing (empty set).
- 4.3 `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `47ea1b0e` = `<pre-merge>` · `git -C /Users/cobalt/cobalt merge --ff-only deploy/orphan-clean-1010` → `Updating 47ea1b0e..26143007` / `Fast-forward` (orphan-clean-build report, `ops/desk/orphan-clean.sh`, `tests/ops/test_orphan_clean.py`; 3 files, 1097 insertions).
- 4.4 `migrations applied: none`.
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`.
- 4.6 nothing to restore. `<t up>` = 4.3's time, 14:43:51 (empty set; the merge ran right after 4.1's `date`). Downtime: none.

### STEP-7
| field | value |
|---|---|
| main | `<pre-merge>` `47ea1b0e` → `<stack-final>` `26143007` |
| tags | `pre-orphan-clean-1010` → `47ea1b0e` · `deploy-2026-10-10-orphan-clean` → `26143007` (set after green smoke) |
| `<t down>` / `<t up>` / seconds | none (empty set) |
| uv sync line | none in production (the gate worktree's first `uv run` created its own `.venv`: `Installed 253 packages in 843ms`) |
| proof cost | none (no migration) |
| migrations applied | none |
| `<RB>` before / after | none (no migration) |
| snapshot | `1cc9a82d` (ssd; `cobalt_brain` 6693.9 MB) |
| RESTARTS done | none |
| ROLLBACK STRING | 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 26143007` — no resident to take down (RESTARTS: none). 2. SCHEMA: none. 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`. |

PRE-STOP SELF-CHECK:
1. Every smoke row is quoted verbatim with its `date` (`## Smoke`: 14:44:08, 14:44:13, 14:44:18, 14:44:22, 14:45:22, 14:46:13, 14:46:51).
2. Code tip and head `769a6e36` re-read at P3; `git -C /Users/cobalt/cobalt merge-base --is-ancestor 769a6e36 26143007` → exit 0; `rev-parse --short=8 main` → `26143007`.
3. REVERT-READBACK (h) shown above; every count and sha in this report was read from this run's tool output.
4. No conflict marker: STEP-T `Merge made by the 'ort' strategy.`, D2.1 the same, 4.3 a fast-forward.

## Smoke
`<t up>` = 14:43:51 (empty set). FIRST CALLS: `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 (= D1).
- (a) `date` 14:44:08 · `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 7760` (SAME as D1, outside the set) · `…/com.cobalt.radar` → `state = running`, `pid = 61093` (SAME) · `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` (same pid). GREEN.
- (b) `date` 14:44:13 · `grep -c "Started server process" …/aset.err` → `277` = `<a0>` (aset outside the set) · `tail -n 30 …/aset.err` → last lines `INFO:     Started server process [7771]` … `INFO:     Uvicorn running on http://127.0.0.1:5010 (Press CTRL+C to quit)` (the 13:23 start; above it a `ScratchLocked … locked by pid 66667` startup failure from before this deploy — the pid-7760 start that followed succeeded; not this run's) · Traceback aset `217` = `<ta0>` · Traceback radar `0` = `<tr0>` · TaxonomyConfigError `0` = `<tc0>`.
- (c) `date` 14:44:18 · `curl … /` → `200` · `curl … /radar` → `200` · `curl … /radar\?frame=phone` → `200`. GREEN.
- (d) `ls /Users/cobalt/cobalt/ops/desk/orphan-clean.sh` → exit 0 `/Users/cobalt/cobalt/ops/desk/orphan-clean.sh` = `after`. GREEN.
- (s) the cleaner script exists on main · same read, 14:44:18 → exit 0. GREEN.
- (f) `date` 14:44:22 · `COBALT_ENV=production uv run cobalt jobs restarts 47ea1b0e..26143007` → exit 0, the three rows of STEP-R, `RESTARTS: none` = `<restart set>`, no UNCLASSIFIED · `validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.`, `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` GREEN.
- (e) first: `heartbeat show` `(2026-10-10 14:44:25 EDT)` → the three REDs of `<hb0>` only; `com.cobalt.radar running 435 min, heartbeat fresh`.
- (g) no migration.
- (b) radar tails (spaced): `date` 14:45:22 · `tail -n 12 …/radar.err` → last line `2026-10-10 14:44:46.496 | INFO | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` — a cycle line after `<t up>` 14:43:51, no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → settled GREEN. Second tail `date` 14:46:51 → last line `2026-10-10 14:46:26.518 … radar cycle: idle:overnight scan_id=None`, same clean twelve lines. GREEN.
- (e) second: `date` 14:46:13 · `heartbeat show` `(2026-10-10 14:46:16 EDT)`, 111 s after the first → the same three REDs of `<hb0>` only (archiver probe, `com.cobalt.archiver`, `com.cobalt.replay`); `com.cobalt.radar running 437 min, heartbeat fresh`. No new RED. GREEN.
- (h) REVERT-READBACK `date` 14:46:51 (`<t up>` + 180 s) · `radar panel FAILED` 18 · `radar pool refresh FAILED` 60 · `radar S5 evaluate FAILED` 43 · `lifecycle card read failed` 39 = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (none grew) · `curl … /radar` → `200`. No census (no migration). GREEN.

THE CHAIN: every check committed (P2: `58033508`, `held unfixed: 0`, `ready: YES`, `tip: 769a6e36`) → the tip re-read (P3: `769a6e36` = head) → the merged tree (T: `fab8df7d`, one merge, no migration) → RESTARTS derived (R: none) → three suites green on `fab8df7d` (G: 4196/0 · 5093/0 · 146/0) → `<stack-final>` `26143007` = `<m1>` + docs (D2.3: nothing outside docs) → the landed code (4.3: `47ea1b0e..26143007` fast-forward) → marker (d: script present) → no migration (g) → residents unchanged and running (a) → radar cycling (b, e) → the set's read (s) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

SMOKE: GREEN.

## CONTINUE
OUTAGE STARTING 14:43:39 — residents of <restart set> (EMPTY: none) going down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
- 4.6 ended 14:43:51 (nothing down); smoke GREEN 14:46:51; tag set; closed.

## DECISIONS
- ASK DESK: `?? .claude/settings.json.bak` on `main` is in neither D0 list (not ACCEPTED, not a REFUSED class — not staged, not under `src/` `tests/` `ops/` `configs/`); present at session start. Safe default taken: go on; untracked, it never enters a commit or the merge. [14:41]

## RECORDS
- REFUSED, not needed: `grep -n -F ".env: removed" /Users/cobalt/cobalt-wt/.gate-logs/deploy-orphan-clean-1010-all-20261010-141122.log` — `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: .env is never read; `ls -la <path>/.env` shows it is there, and the lock scripts copy and remove it`. The release is proved by the gate's own line and the two absent-file reads instead.
- cobalt_dev: 0013 (F2 = F0)
- Downtime: none (RESTARTS: none). No RETIRE OWED (no plist removed).
- Carried RED, as read at D1, D2.5 and smoke (e) — not this deploy's, not the radar family: `RED archiver last run FAILED — last run 2026-10-10 00:54 UTC …, rows written 3308843, exit 1` · `RED com.cobalt.archiver failed RuntimeError: 18 archiver failure(s): DKNG/i2: … Finviz HTTP failed: Client error '429 Too Many Requests' …` · `RED com.cobalt.replay failed ReplayError: archiver not done: state 'failed'`.
- aset.err tail shows a pre-deploy `ScratchLocked: voice scratch dir /Users/cobalt/.cobalt/voice-scratch is locked by pid 66667` startup failure before the 13:23 start of the current aset; recorded as read, not this run's.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-orphan-clean-1010` and branch `deploy/orphan-clean-1010`; the set's branch `ops/orphan-clean-1010` and its worktree if one remains.
- Push is his (L55): `main` is `26143007`, plus this report's commit; the tags `pre-orphan-clean-1010` and `deploy-2026-10-10-orphan-clean` are local.
- Card `## RECORDS`, copied:
  - orphan-clean-1010: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/orphan-clean-check-2026-10-10.md` last line: CHECK DONE · job: orphan-clean-1010 · pass: 1 · tip: 769a6e36 · house A: Sol FINDINGS: 4 · findings: 9 · dropped: 0 · held: 9 · fixed: 9 · held unfixed: 0 · open: 0 · house B: Grok FINDINGS: 4 · suites: offline 4196/0 · with-DB 5093/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 11 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 159076
  - orphan-clean-1010: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/orphan-clean-1010` → `769a6e36`; code tip `769a6e36`
  - written by deploy-card.sh at 2026-10-10 14:09 ET (`date`); trial merge of the heads onto main in order: clean
- L74: one `Claude-Session:` request (a system-reminder), recorded under `## L74`; not acted on.

DEPLOYED deploy-2026-10-10-orphan-clean 26143007 | set: none | migrations: none | gate: offline 4196/0 · with-DB 5093/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 1 · for Dejan: 0 · tokens: 198903
