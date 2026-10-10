# deploy ops-hand-1010 — set: none · migrations: none

## §0 Headline
- DEPLOYED ops-hand-1010: `main` `12f99fad` → `1e9f2e4c` (fast-forward), tag `deploy-2026-10-10-ops-hand`, rollback tag `pre-ops-hand-1010`.
- Gate green on `e214d5f3`: offline 4199/0 · with-DB 5096/0 · live-note 146/0; `cobalt_dev` 0013, F2 = F0; lock released.
- RESTARTS: none — no resident went down; aset 7760, radar 61093, agent 22243 unchanged. Migrations: none.
- Smoke GREEN; `OPS-HAND.md` is on main. The archiver/replay REDs are carried from before the deploy, unchanged.
- decisions: 0 · for Dejan: 0.

## L74
- 17:33 ET: a system block in the session context asked commit messages to end with a `Claude-Session: https://claude.ai/code/session_…` line. Recorded once here; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/293-deploy-ops-hand-card.md"` (17:33 ET), whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/293-deploy-ops-hand-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/293-deploy-ops-hand-card.md" · 0 · 92c3fd5cceb0a3cfa4bcb563e2c5153cce0fe991
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/293-deploy-ops-hand-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-10 R855 row · grep -n "^| R855 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 104:| R855 | 07:51 ET | HIS RULING · APPROVED: build both `orphan-clean.sh` (by card) and the `ops-hand` seat (default-mode phone approval, L63 exception). Words `cto-2026-10-10-words.md` R855. The orphan-cause card first (R853). | APPLIED: areas/cobalt.md NOW at wake-up 07:55 |
RULING 2026-10-10 R855 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R855 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 4f9f5bceabb1f1c0b42cb0df4ca22c33fa6e618d
RULING 2026-10-10 R855 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
AUTHORIZED
```
First launch: `ls -la "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-ops-hand-1010.md"` → exit 1, `No such file or directory`.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | `authorize.sh deploy` (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Sat Oct 10 17:33:45 EDT 2026` |
| P2 check | `tail -n 3 ".../reports/ops-hand-check-2026-10-10.md"` | 0 | `CHECK DONE · job: ops-hand-1010 · pass: 1 · tip: 6a18ff95 · … · held unfixed: 0 · … · ready: YES · decisions: 1 · for Dejan: 1 · tokens: 195546` |
| P2 check committed | `git log -1 --format=%H -- "docs/…/ops-hand-check-2026-10-10.md"` | 0 | `da9ae7508b90080cf9ab80663a6af3b14abe0212` |
| P2 check clean | `git diff --stat -- "docs/…/ops-hand-check-2026-10-10.md"` | 0 | nothing |
| P2 fix report on main | `tail -n 3 ".../reports/ops-hand-build-2026-10-10.md"` | 1 | `No such file or directory` (the fix report lives on the branch head, as the card's `## RECORDS` says: "at `64d3049f`") |
| P2 fix report committed | `git log -1 --format=%H 64d3049f -- "docs/…/ops-hand-build-2026-10-10.md"` | 0 | `64d3049ff448c14e1ae0c135896408febd916675` |
| P2 fix report clean | `git diff --stat -- "docs/…/ops-hand-build-2026-10-10.md"` | 0 | nothing |
| P2 fix report last line | `git show "64d3049f:docs/…/ops-hand-build-2026-10-10.md"` (last line) | 0 | `BUILT · job: ops-hand-1010 · tip: 1a8614cc \| on 1eb47b59 \| migration: none \| offline 4196/0 \| with-DB 5093/0 \| live-note 146/0 \| cobalt_dev: 0013 \| .env: removed \| RESTARTS: none \| rows: 7 of 7 \| self-check: 3 of 3 \| decisions: 3 · for Dejan: 1 · tokens: 125383` |
| P2 fix-round tip | `git merge-base --is-ancestor 6a18ff95 1a8614cc` | 0 | ancestor |
| P3 code tip | `git rev-parse --short=8 1a8614cc` | 0 | `1a8614cc` |
| P3 head | `git rev-parse --short=8 ops/ops-hand-1010` | 0 | `64d3049f` = `TIP` |
| P3 ancestry | `git merge-base --is-ancestor 1a8614cc 64d3049f` | 0 | ancestor |
| P3 docs-only head | `git diff --stat 1a8614cc 64d3049f -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 gate | `git -C <GATE> status --short --branch` | 0 | `## deploy/ops-hand-1010` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `92c3fd5c` = `<m0>` |
| P5 m0 on main | `git merge-base --is-ancestor 92c3fd5c main` | 0 | ancestor |
| P5 empty | `git log --oneline main..deploy/ops-hand-1010` | 0 | empty |
| P6 marker | `ls ".../prompts/OPS-HAND.md"` | 1 | `No such file or directory` = before |
| P7 migrations | `git diff --stat main 64d3049f -- src/cobalt/db_migrations` | 0 | nothing = `MIGRATIONS: none` |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 7760` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 61093` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 64d3049f` → `Merge made by the 'ort' strategy.` (7 files, 924 insertions, 3 deletions; auto-merged `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py`).
- `<m1>` = `e214d5f3` (`git -C <GATE> rev-parse --short=8 HEAD`).
- `git log --oneline --merges --first-parent 92c3fd5c..deploy/ops-hand-1010` → `e214d5f3 Merge commit '64d3049f' into deploy/ops-hand-1010` (one head, one merge).
- `merge-base --is-ancestor 1a8614cc deploy/ops-hand-1010` → 0; `merge-base --is-ancestor 64d3049f deploy/ops-hand-1010` → 0.
- `diff --stat 92c3fd5c deploy/ops-hand-1010 -- src/cobalt/db_migrations` → nothing (no migration).
- STEP-C: `diff --stat 92c3fd5c deploy/ops-hand-1010 -- configs ops` →
```
 ops/desk/bare-guard.py  |  37 ++++++++++++++++-
 ops/desk/desk-launch.sh | 105 +++++++++++++++++++++++++++++++++++++++++++++++-
 2 files changed, 139 insertions(+), 3 deletions(-)
```
  No plist added, modified or removed.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` (exit 0), whole (after the uv venv creation lines):
```
path	change	rule	restart
docs/40 - DevDocs/prompts/OPS-HAND.md	A	DOCS	-
docs/40 - DevDocs/reports/ops-hand-build-2026-10-10.md	A	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_ops_hand.py	A	test/documentation; no resident	-
tests/ops/test_stop_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```
`<restart set>` = EMPTY (none). No resident goes down; the merge lands with the residents up.

## L68 GATE
- EQUAL-TREE CLAUSE: `git diff --stat 6a18ff95 e214d5f3 -- . ":(exclude)docs"` → 11 files changed (the fix round and main since the check) → the clause does not hold; the gate runs whole (`--deploy`).
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 16.93s` (0 failed; every skip a `Postgres env settings not available` / `requires_db` skip).
- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-ops-hand-1010 all --deploy` (no `--deselect`: the build adds no with-DB test, its report line 128; no `--tickers`; no `--migration`) → exit 0, verdict lines whole:
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-ops-hand-1010-all-20261010-173538.log
```
- Skips: all seven inside the allowed set; `test_s3_c4_experiments.py:95` is `@requires_live` on `def test_x14_live_his_template_strips_to_the_committed_fixture` (`tests/cobalt/test_s3_c4_experiments.py:95-96` in `<GATE>`).
- (f) log `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (:896) = `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (:2030); `cobalt_dev: 0013 — F2 = F0` (:2082). No migration → no `dev forward` line.
- RELEASE: log :2083-2088 `sh …/release-devdb-lock.sh deploy-ops-hand-1010` → `lock released`, `.env: removed` (L76 lock released; gate done by 18:05:32 ET, `date`). `ls -la <GATE>/.env` → No such file; `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → No such file.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on e214d5f3 — offline 4199/0 · with-DB 5096/0 · live-note 146/0

## Deploy table
### STEP-D0 (18:05 ET)
| check | command | exit | result |
|---|---|---|---|
| main | `git status --short --branch` | 0 | `## main...origin/main [ahead 312]` |
| main dirty | `git status --porcelain` | 0 | ` M .claude/settings.json`; ` M` / `??` under `docs/` only; one `?? .claude/settings.json.bak` (not `src/`, `tests/`, `ops/`, `configs/`; recorded under `## RECORDS`); no staged line |
| main moved | `git diff --stat 92c3fd5c main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| probe | `tag scratch-allow-probe-ops-hand-1010` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-ops-hand-1010' (was 92c3fd5c)` |
| probe | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 50d2ee25] …` · — · `92c3fd5c docs(desk): ops-hand deploy card 293, fix round row S` (HEAD back) |
| tag | `rev-parse --verify --quiet refs/tags/deploy-2026-10-10-ops-hand` | 1 | absent |
| tag | `rev-parse --verify --quiet refs/tags/pre-ops-hand-1010` | 1 | absent |

### STEP-D1 baseline (18:05:58 ET)
- `<hb0>` (`heartbeat show`, 18:06:00 EDT): `HEARTBEAT RED — 2 job(s) and 1 probe(s)`. aset probe `OK com.cobalt.aset running loaded, pid 7760`; sheet probes `OK sheet HTTP http://127.0.0.1:5010/ -> 200`, `OK sheet daymode …`; radar probes `OK radar idle (overnight)`, `OK com.cobalt.radar running running 636 min, heartbeat fresh`; agent `OK … pid 22243 alive`. REDs, named (none on the aset / sheet / radar probe, not a stop): `RED archiver last run FAILED — last run 2026-10-10 00:54 UTC (21.2 h ago), rows written 3308843, exit 1`; `RED com.cobalt.archiver failed RuntimeError: 18 archiver failure(s): DKNG/i2: … Finviz HTTP failed: Client error '429 Too Many Requests' …`; `RED com.cobalt.replay failed ReplayError: archiver not done: state 'failed'`. `AMB com.cobalt.herdr unmanaged …` (declared interim).
- `<val0>`: `validate` exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.` · `<jobs0>`: `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 1.3 h old` (ssd local ARMED).
- `launchctl print` aset → `state = running`, `<aset pid>` = 7760; radar → `state = running`, `<radar pid>` = 61093; `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).`; `ps -p 22243` → `22243 ?? 0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 radar.err` → last `2026-10-10 18:04:49.278 | INFO | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` (cycles every 100 s, none failing).
- LOG BASELINES: `<a0>` 277 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKER `ls ".../prompts/OPS-HAND.md"` → exit 1, No such file = before.
- No migration: `<RB>`, census and D1-M not run.

### STEP-D2
| step | command | exit | result |
|---|---|---|---|
| D2.0 | `git add` · `git commit -m "docs(report): deploy ops-hand-1010 — gate green on e214d5f3" …` | 0 · 0 | `[main 12f99fad] … 1 file changed, 146 insertions(+)`; `show --stat HEAD` lists the report alone |
| D2.0 | `git rev-parse --short=8 main` | 0 | `<pre-merge>` = `12f99fad` |
| D2.1 | `git -C <GATE> merge --no-edit main` | 0 | `Merge made by the 'ort' strategy.` (the report alone) |
| D2.2 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<stack-final>` = `1e9f2e4c` |
| D2.2 | `git rev-parse --short=8 1e9f2e4c^2` | 0 | `12f99fad` = `<pre-merge>` |
| D2.2 | `git merge-base --is-ancestor e214d5f3 1e9f2e4c` | 0 | ancestor |
| D2.3 | `git diff --stat e214d5f3 1e9f2e4c -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing (docs-only) |
| D2.4 | `backup status` | 0 | `newest snapshot: 1.3 h old` |
| D2.4 | `backup run` (foreground) | 0 | `backup: cobalt_brain dumped, 6693.7 MB` · `ssd: snapshot 93a69a67 — 0 new / 1 changed, 26.7 MB added, 1 pruned` |
| D2.4 | `backup status` | 0 | `newest snapshot: 0.0 h old` |
| D2.5 | `date` · `heartbeat show` | 0 · 0 | 18:07:52 · `HEARTBEAT RED — 2 job(s) and 1 probe(s) (2026-10-10 18:07:54 EDT)`, 114 s after D1's 18:06:00; the same three REDs as `<hb0>` (archiver probe, `com.cobalt.archiver`, `com.cobalt.replay`), no new RED; aset `pid 7760`, radar `running 638 min, heartbeat fresh` (two earlier reads at 18:07:36 and 18:07:49 fell short of 110 s and are not counted) |
| D2.6 | `date` · `git tag pre-ops-hand-1010` | 0 · 0 | `Sat Oct 10 18:07:58 EDT 2026` · `rev-parse --short=8 pre-ops-hand-1010` → `12f99fad` |

### STEP-4 (restart set EMPTY)
| step | command | exit | result |
|---|---|---|---|
| 4.1 | `date` | 0 | `<t down>` = `Sat Oct 10 18:08:12 EDT 2026` (nothing goes down) |
| 4.2 | — | — | no label in `<restart set>`: no bootout, no stop |
| 4.3 | `git rev-parse --short=8 HEAD` | 0 | `12f99fad` = `<pre-merge>` |
| 4.3 | `git merge --ff-only deploy/ops-hand-1010` | 0 | `Updating 12f99fad..1e9f2e4c` / `Fast-forward` (7 files, 924 insertions, 3 deletions) |
| 4.4 | — | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | 0 | ends `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>` |
| 4.6 | — | — | no label booted out: nothing to bootstrap |
| t up | `date` | 0 | `<t up>` = `Sat Oct 10 18:08:20 EDT 2026`; downtime: none (no resident went down) |

### STEP-7 summary
- `<pre-merge>` `12f99fad` → `<stack-final>` `1e9f2e4c`. Tags: `pre-ops-hand-1010` → `12f99fad`; `deploy-2026-10-10-ops-hand` → `1e9f2e4c` (set after the green smoke).
- `<t down>` / `<t up>` / seconds: none (restart set EMPTY; 4.1 `date` 18:08:12, `<t up>` 18:08:20).
- uv sync line: none in production (no migration; the gate worktree's own venv was created at STEP-R: `Creating virtual environment at: .venv` … `Installed 253 packages in 775ms`).
- Proof cost: not run (no migration). `migrations applied: none`. `<RB>` before / after: not applicable.
- Snapshot: `93a69a67` (ssd).
- `RESTARTS done: none`.
- THE ROLLBACK STRING (the desk's):
  1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 1e9f2e4c` — the restart set is empty, so no resident goes down or up.
  2. SCHEMA: none (no migration).
  3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

## Smoke
`<t up>` = 18:08:20 ET (restart set EMPTY: every label keeps its pid).

| row | `date` | command | result |
|---|---|---|---|
| first calls | 18:08:20+ | the four failure counts | `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 (= D1) |
| (a) | 18:08:33 | `launchctl print gui/501/com.cobalt.aset` | `state = running`, `pid = 7760` (SAME as D1: outside the set) |
| (a) | 18:08:33 | `launchctl print gui/501/com.cobalt.radar` | `state = running`, `pid = 61093` (SAME as D1) |
| (a) | 18:08:33 | `/Users/cobalt/cobalt/cobalt.sh status` | `Cobalt is ONLINE (PID: 22243).` (same pid) |
| (b) | 18:08:36 | `grep -c "Started server process" aset.err` | 277 = `<a0>` (aset outside the set) |
| (b) | 18:08:36 | `grep -c "Traceback"` aset.err · radar.err · `grep -c "TaxonomyConfigError"` radar.err | 217 = `<ta0>` · 0 = `<tr0>` · 0 = `<tc0>` |
| (b) | 18:08:36 | `tail -n 30 aset.err` | last lines `INFO: Started server process [7771]` … `INFO: Uvicorn running on http://127.0.0.1:5010 (Press CTRL+C to quit)`; the traceback above them (`cobalt.voice.scratch.ScratchLocked: … locked by pid 66667`) predates this deploy (it precedes the `2026-10-10 13:23:12.445` line) and the count is the baseline 217 |
| (c) | 18:08:36 | `curl … https://cobalt.taild24291.ts.net/` · `/radar` · `/radar\?frame=phone` | `200` · `200` · `200` |
| (d) | 18:08:36 | `ls ".../prompts/OPS-HAND.md"` | exit 0, `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/OPS-HAND.md` = after |
| (s) | 18:08:36 | the ops-hand fixed file is on main · `ls ".../prompts/OPS-HAND.md"` | exit 0 = green |
| (f) | 18:08:20+ | `validate` (4.5) | exit 0, `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>` |
| (f) | 18:08:4x | `COBALT_ENV=production uv run cobalt jobs restarts 12f99fad..1e9f2e4c` | exit 0, same 7 rows as STEP-R, `RESTARTS: none` = `<restart set>`, no `UNCLASSIFIED` |
| (g) | — | no migration | not run |
| (e) 1 | 18:08:47 | `heartbeat show` | `HEARTBEAT RED — 2 job(s) and 1 probe(s) (2026-10-10 18:08:47 EDT)`; the same three REDs as `<hb0>`; `com.cobalt.radar running running 639 min, heartbeat fresh`; aset `pid 7760` |
| (b) tail 1 | 18:09:50 (`<t up>` + 90 s) | `tail -n 12 radar.err` | last `2026-10-10 18:09:49.354 \| INFO \| cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` — a cycle line after `<t up>`, no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → (b) settled GREEN |
| (h) | 18:11:23 (`<t up>` + 183 s) | the four failure counts · `curl … /radar` | 18 · 60 · 43 · 39 = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (nothing grew) · `200`; no census line on the card |
| (b) tail 2 | 18:11:23 | `tail -n 12 radar.err` | last `18:09:49.354 … radar cycle: idle:overnight scan_id=None`; no failure line, no traceback (b was already settled GREEN by tail 1) |
| (e) 2 | 18:10:39 | `heartbeat show` | `HEARTBEAT RED — 2 job(s) and 1 probe(s) (2026-10-10 18:10:41 EDT)`, 114 s after (e) 1; the same three REDs, no new RED; `com.cobalt.radar running running 641 min, heartbeat fresh` → GREEN (the clock between was filled with `date` + `heartbeat show` pairs, each the same) |

THE CHAIN: every check committed (P2: check `da9ae750`, fix report in `64d3049f`) → the tips re-read (P3: `1a8614cc`, `64d3049f`) → the merged tree `e214d5f3` (T, one merge, no conflict) → RESTARTS derived `none` (R) → three suites green on `e214d5f3` (G: 4199/0, 5096/0, 146/0) → `<stack-final>` `1e9f2e4c` = `<m1>` + docs (D2.3: nothing outside docs) → the landed code (4.3: `Updating 12f99fad..1e9f2e4c`, Fast-forward) → marker after (d: `OPS-HAND.md` exit 0) → no migration (g) → residents up, same pids (a) → radar cycling after `<t up>` (b: 18:09:49; e: fresh both reads) → the set's read green (s) → no new failure (h: counts unchanged, `/radar` 200). The card surface is not readable here; the desk confirms it with him (L70).

PRE-STOP SELF-CHECK:
1. Every smoke row above carries its `date` and the verbatim output it rests on.
2. `git merge-base --is-ancestor 1a8614cc 1e9f2e4c` → exit 0; `git merge-base --is-ancestor 64d3049f 1e9f2e4c` → exit 0; both re-read at P3.
3. REVERT-READBACK shown at (h): 18 · 60 · 43 · 39 at 18:11:23, equal to the first calls after `<t up>`; every count, sha and `file:line` here was read from this run's tool output (tags: `rev-parse --short=8 deploy-2026-10-10-ops-hand` → `1e9f2e4c`).
4. No conflict marker: STEP-T `Merge made by the 'ort' strategy.`; D2.1 the same; `git -C <GATE> status --short --branch` → `## deploy/ops-hand-1010` alone.

THE RELEASE: held by nobody — the gate released the lock (log :2084 `lock released`, :2088 `.env: removed`); `ls -la <GATE>/.env` and the lock dir → No such file (18:05 ET).

## CONTINUE
next: STEP-D2 (gate green at 18:05:32 ET; D0 and D1 done)
OUTAGE STARTING 18:07:58 ET — residents of <restart set> going down; the set is EMPTY (RESTARTS: none), so no resident goes down; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
Merged 1e9f2e4c on main at 18:08 ET; no resident went down. Smoke GREEN at 18:11:23; tagged; done.

## DECISIONS
- none. (The build report's own `for Dejan: 1` — G12 denies the R686 production read for the ops-hand seat — and the check's `for Dejan: 1` are theirs, carried in their reports; this deploy adds none.)

## RECORDS
- Downtime: none (restart set EMPTY; no resident went down; aset pid 7760, radar pid 61093, agent pid 22243 unchanged).
- REFUSED, not needed: `grep -n -F ".env: removed" /Users/cobalt/cobalt-wt/.gate-logs/deploy-ops-hand-1010-all-20261010-173538.log` — `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: .env is never read; `ls -la <path>/.env` shows it is there, and the lock scripts copy and remove it`. The release was read instead with the Grep tool on the log (:2083-2088) and with `ls -la <GATE>/.env` → No such file.
- Messages not followed: none received.
- `cobalt_dev: 0013 (F2 = F0)` — `F0`/`F2` `664 35 272c95bbb12241e3611e4b36326ccf87` (gate log :896, :2030).
- RETIRE OWED: none (no plist removed).
- Carried RED as read (not of this deploy, unchanged from `<hb0>` through smoke): `RED archiver last run FAILED — last run 2026-10-10 00:54 UTC (21.2 h ago), rows written 3308843, exit 1`; `RED com.cobalt.archiver failed RuntimeError: 18 archiver failure(s): DKNG/i2: … '429 Too Many Requests' …`; `RED com.cobalt.replay failed ReplayError: archiver not done: state 'failed'`. The radar probe was OK (`idle (overnight)`) throughout.
- Main carried `?? .claude/settings.json.bak` at D0 (outside `src/`, `tests/`, `ops/`, `configs/`; not refused by the D0 rule); untouched.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-ops-hand-1010` and branch `deploy/ops-hand-1010`; the set's branch `ops/ops-hand-1010` and its worktree, if any.
- Push owed (L55): `main` at `1e9f2e4c` plus this report's commit, and tags `pre-ops-hand-1010`, `deploy-2026-10-10-ops-hand` — his, through the desk.
- L74: one system block asked for a `Claude-Session:` commit line (recorded under `## L74`); not acted on.
- Card `## RECORDS`, copied:
  - ops-hand-1010: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/ops-hand-build-2026-10-10.md` at `64d3049f` last line: BUILT · job: ops-hand-1010 · tip: 1a8614cc | on 1eb47b59 | migration: none | offline 4196/0 | with-DB 5093/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 7 of 7 | self-check: 3 of 3 | decisions: 3 · for Dejan: 1 · tokens: 125383
  - ops-hand-1010: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/ops-hand-check-2026-10-10.md` last line: CHECK DONE · job: ops-hand-1010 · pass: 1 · tip: 6a18ff95 · house A: Sol FINDINGS: 1 · findings: 7 · dropped: 0 · held: 5 · fixed: 5 · held unfixed: 0 · open: 2 · house B: Grok FINDINGS: 3 · suites: offline 4196/0 · with-DB 5093/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 1 · for Dejan: 1 · tokens: 195546
  - ops-hand-1010: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/ops-hand-1010` → `64d3049f`; code tip `1a8614cc`
  - written by deploy-card.sh at 2026-10-10 17:33 ET (`date`); trial merge of the heads onto main in order: clean

DEPLOYED deploy-2026-10-10-ops-hand 1e9f2e4c | set: none | migrations: none | gate: offline 4199/0 · with-DB 5096/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 0 · for Dejan: 0 · tokens: 196256
