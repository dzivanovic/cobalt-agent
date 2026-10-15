# deploy gate-tests-ops-fr1 · SET: none · MIGRATIONS: none

Card: `docs/40 - DevDocs/prompts/2026-10-15/577-deploy-gate-tests-ops-card.md` · hub: `DEPLOY-HUB.md` · seat: deploy-hub-gate-tests-ops-fr1 · started `Thu Oct 15 08:15:09 EDT 2026`.

## §0 Headline
- DEPLOYED `deploy-2026-10-15-gate-tests-ops` at `174cb974`: `ops/gate-tests-ops-fr1` (code `ec3fabc1`) landed on `main` by fast-forward from `326c7792` at 09:03 ET.
- The gate was green on `254ec10f`: offline 4328/0 · with-DB 5231/0 · live-note 146/0. `cobalt_dev` is back at 0013 with F2 = F0. The card's `tests/ops` read passed 3734 (1 xfailed).
- RESTARTS: none. No resident went down and there was no downtime. No migration, and the launchd set is empty.
- The 521 self-proof is green: the merged `gate.sh … offline --deploy-gate` prints `tests/ops: run (deploy gate)` and `offline 8062/0`.
- Smoke GREEN. Decisions: none.

## L74
- The harness's attribution reminder asked for a `Claude-Session:` trailer on commits. Recorded once as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/577-deploy-gate-tests-ops-card.md"`, exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/577-deploy-gate-tests-ops-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-15/577-deploy-gate-tests-ops-card.md" · 0 · c80ba54443240999b52273c9d0fd3897b80ed0dc
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-15/577-deploy-gate-tests-ops-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-gate-tests-ops-fr1.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Thu Oct 15 08:15:09 EDT 2026` (outside 21:30–22:30 ET) |
| P2 | `tail -n 3 ".../gate-tests-ops-check-fr1-2026-10-15.md"` | 0 | `CHECK DONE · job: gate-tests-ops-fr1 · pass: 1 · tip: ec3fabc1 · house A: Grok FINDINGS: 0 · findings: 0 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4328/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 8 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 212760` — carries `held unfixed: 0` and `ready: YES`; `tip: ec3fabc1` = row code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/gate-tests-ops-check-fr1-2026-10-15.md"` | 0 | `77a73af3d129cf6019dc9ea186a63e9482bcf9d0` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/gate-tests-ops-check-fr1-2026-10-15.md"` | 0 | nothing |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ec3fabc1` | 0 | `ec3fabc1` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/gate-tests-ops-fr1` | 0 | `b6370b5f` (= row, = `TIP`) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor ec3fabc1 b6370b5f` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat ec3fabc1 b6370b5f -- . ':(exclude)docs'` | 0 | nothing |
| P4 LOCK | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-gate-tests-ops-1015 status --short --branch` | 0 | `## deploy/gate-tests-ops-fr1` |
| P5 | `git -C /Users/cobalt/cobalt-wt/deploy-gate-tests-ops-1015 rev-parse --short=8 HEAD` | 0 | `0992fc96` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 0992fc96 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/gate-tests-ops-fr1` | 0 | empty |
| P6 | `grep -c -F "## OFFLINE OPS" /Users/cobalt/cobalt/ops/desk/gate-lists.md` | — | `0` (before `0`) |
| P6 | `grep -c -F "tests/ops: run" /Users/cobalt/cobalt/ops/desk/gate.sh` | — | `0` (before `0`) |
| P6 | `grep -c -F -e "--deploy-gate" /Users/cobalt/cobalt/ops/desk/gate.sh` | — | `0` (before `0`) |
| P6 | `grep -c -F -e "--deploy-gate" ".../prompts/DEPLOY-HUB.md"` | — | `0` (before `0`) |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main b6370b5f -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `pid = 40377` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `pid = 8646` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 14763).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-gate-tests-ops-1015 merge --no-edit b6370b5f` → `Merge made by the 'ort' strategy.` (9 files, 509 insertions, 25 deletions: `BUILD-HUB.md`, `CHECK-HUB.md`, `DEPLOY-HUB.md`, the build report + `.result`, `ops/desk/gate-lists.md`, `ops/desk/gate.sh`, `tests/ops/test_build_hub_no_clutter.py`, `tests/ops/test_gate.py`)
- `rev-parse --short=8 HEAD` → `254ec10f` = `<m1>`
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 0992fc96..deploy/gate-tests-ops-fr1` → `254ec10f Merge commit 'b6370b5f' into deploy/gate-tests-ops-fr1` (one line, one head)
- `merge-base --is-ancestor ec3fabc1 deploy/gate-tests-ops-fr1` → exit 0 · `merge-base --is-ancestor b6370b5f deploy/gate-tests-ops-fr1` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat 0992fc96 deploy/gate-tests-ops-fr1 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none)
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 0992fc96 deploy/gate-tests-ops-fr1 -- configs ops` →
```
 ops/desk/gate-lists.md |  3 +++
 ops/desk/gate.sh       | 42 +++++++++++++++++++++++++++++++++++++++---
 2 files changed, 42 insertions(+), 3 deletions(-)
```
- STEP-C: `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 0992fc96 deploy/gate-tests-ops-fr1` → exit 0, whole output: `STEP-C: ADMITTED 0` → `<launchd set>` empty.

## RESTARTS
`cd /Users/cobalt/cobalt-wt/deploy-gate-tests-ops-1015` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created `.venv` in the gate: `Installed 254 packages in 782ms`):
```
path	change	rule	restart
docs/40 - DevDocs/prompts/BUILD-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/CHECK-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/gate-tests-ops-build-fr1-p1-2026-10-14.md	A	DOCS	-
docs/40 - DevDocs/reports/gate-tests-ops-build-fr1-p1-2026-10-14.result	A	DOCS	-
ops/desk/gate-lists.md	M	operator script; no Cobalt reader	-
ops/desk/gate.sh	M	operator script; no Cobalt reader	-
tests/ops/test_build_hub_no_clutter.py	M	test/documentation; no resident	-
tests/ops/test_gate.py	M	test/documentation; no resident	-
RESTARTS: none
```
- No `UNCLASSIFIED` row. `<restart set>` = EMPTY (no resident goes down). `<launchd set>` = empty. MIGRATIONS none, so the L66 empty-set rule does not apply.

## L68 GATE
- EQUAL-TREE CLAUSE: not applied. The check's stop line carries `with-DB 0/0` (not above 0), so the gate runs whole.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 16.76s`: 0 failed. Every skip is a with-DB skip (`Postgres env settings not available` / `requires_db: …`).
- Deselects: none. The build report names no with-DB deselect (set DB: none). `--tickers`: none (TICKERS: none). `--migration`: none.
- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-gate-tests-ops-1015 all --deploy` (background) → exit 0. Verdict lines, whole:
```
offline 4328/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5231/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-gate-tests-ops-1015-all-20261015-081717.log
```
- (a) offline `4328/0`. (b) lock waited 0 min; proof-only at `0013` with nothing `CHANGED` (log :954); `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log :902).
- (c) PASS 1 whole: all seven SKIPPED lines are inside the allowed set. `test_s3_c4_experiments.py:95` is `test_x14_live_his_template_strips_to_the_committed_fixture` (read at `<GATE>/tests/cobalt/test_s3_c4_experiments.py:95-96`). (c2) `dev forward: APPLIED 08:41:54` (log :1118). Content is `UNCHANGED on every table` (log :1186, :2029). (c3) with-DB `5231/0`.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log :2039) = F0 field for field. `cobalt_dev: 0013 — F2 = F0` (log :2091).
- THE RELEASE: `lock released` (log :2093), then `.env: removed` (log :2097). The log carries no clock on the release; it ran before 08:47:11 (`date` at the read). `ls -la <GATE>/.env` → No such file · `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → No such file.
- (e) live-note `146/0`. Its only skip (log :2161) is `test_replay_line.py:266` `COBALT_TEST_LIVE_DRC`, which is in the allowed set. No skip names `COBALT_LIVE_VAULT_ROOT`.
- Sums: offline 4328/0 · with-DB 5231/0 · live-note 146/0.

GATE GREEN on 254ec10f

- CARD (BEFORE THE MERGE, brain 0e848919): `ls -la <GATE>/.env` → No such file · `uv run pytest -q tests/ops` in `<GATE>` at `254ec10f` → `3734 passed, 1 xfailed, 16 warnings in 804.48s (0:13:24)`, exit 0.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed (cwd back). `date` → `Thu Oct 15 09:00:52 EDT 2026`.

## Deploy table
| step | command | exit | result |
|---|---|---|---|
| D0 MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 44]` |
| D0 MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | only ` M` / `??` under `docs/40 - DevDocs/`, ` M configs/cobalt/rules.yaml`, ` M .claude/settings.json`, plus `?? .claude/settings.json.bak` (not staged, not under `src/` `tests/` `ops/` `configs/`: not refused, recorded). No staged line. |
| D0 MAIN | `git -C /Users/cobalt/cobalt diff --stat 0992fc96 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| D0 PROBE | `tag scratch-allow-probe-gate-tests-ops-fr1` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-gate-tests-ops-fr1' (was 0992fc96)` |
| D0 PROBE | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 8b836d0e] …` → `0992fc96 docs(desk): install-ops run R1542, 521 deploy launch R1543` (HEAD back) |
| D0 TAGS | `rev-parse --verify --quiet refs/tags/deploy-2026-10-15-gate-tests-ops` · `… refs/tags/pre-gate-tests-ops-fr1` | 1 · 1 | neither exists |
| D1 | `date` · `COBALT_ENV=production uv run cobalt heartbeat show` | 0 · 0 | `Thu Oct 15 09:01:11 EDT 2026` · `<hb0>`: `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-15 09:01:12 EDT)`. The one non-OK row is `AMB  com.cobalt.herdr  unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0) …; runs outside launchd by declared interim`. `radar scanning (premarket), members 50` · `com.cobalt.radar running 2090 min, heartbeat fresh` |
| D1 | `COBALT_ENV=production uv run cobalt validate` | 0 | `<val0>`: 13 trade_defs OK, `Placement (docs/PLACEMENT.md): tree clean.` · `<jobs0>`: `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` |
| D1 | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 9.9 h old` |
| D1 | `launchctl print gui/501/com.cobalt.aset` · `…/com.cobalt.radar` | 0 · 0 | `state = running`, `<aset pid>` `40377` · `state = running`, `<radar pid>` `8646` |
| D1 | `/Users/cobalt/cobalt/cobalt.sh status` · `ps -p 14763` | 0 · 0 | `Cobalt is ONLINE (PID: 14763).` · `14763 ?? 0:00.03 uv run src/cobalt_agent/main.py` |
| D1 | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | 0 | last `2026-10-15 09:01:09.939 \| INFO \| cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792069190341`, no traceback |
| D1 | log baselines | — | `<a0>` 279 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39 |
| D1 | `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` | 0 | `200` |
| D1 | the four `## MARKERS` | — | `0` · `0` · `0` · `0` (each = before) |
| D1 | THE LAUNCHD SET · MIGRATION | — | empty set: nothing · MIGRATIONS none: no `<RB>`, no D1-M |
| D2.0 | `git -C /Users/cobalt/cobalt add …` · `commit -m "docs(report): deploy gate-tests-ops-fr1 — gate green on 254ec10f" …` · `show --stat HEAD` | 0 · 0 · 0 | `[main 326c7792]`, one file (`deploy-gate-tests-ops-fr1.md`, 152 insertions) |
| D2.0 | `git -C /Users/cobalt/cobalt rev-parse --short=8 main` | 0 | `326c7792` = `<pre-merge>` |
| D2.1 | `git -C <GATE> merge --no-edit main` | 0 | `Merge made by the 'ort' strategy.` (the report only) |
| D2.2 | `git -C <GATE> rev-parse --short=8 HEAD` · `rev-parse --short=8 174cb974^2` · `merge-base --is-ancestor 254ec10f 174cb974` | 0 · 0 · 0 | `174cb974` = `<stack-final>` · `326c7792` = `<pre-merge>` · ancestor |
| D2.3 | `git -C /Users/cobalt/cobalt diff --stat 254ec10f 174cb974 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing (docs only) |
| D2.4 | `backup status` · `backup run` (foreground) · `backup status` | 0 · 0 · 0 | `newest snapshot: 9.9 h old` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 8116.7 MB` · `ssd: snapshot 2421002d — 1 new / 5 changed, 298.9 MB added, 1 pruned` → `newest snapshot: 0.0 h old` |
| D2.5 | `date` · `heartbeat show` | 0 · 0 | `Thu Oct 15 09:03:11 EDT 2026` · `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-15 09:03:12 EDT)`, 120 s after D1's read. No new RED; the same herdr AMB row as `<hb0>`. |
| D2.6 | `date` · `git -C /Users/cobalt/cobalt tag pre-gate-tests-ops-fr1` | 0 · 0 | `Thu Oct 15 09:03:17 EDT 2026` · tag `pre-gate-tests-ops-fr1` at `326c7792` |
| 4.1 | `date` | 0 | `Thu Oct 15 09:03:32 EDT 2026` = `<t down>` (empty set: nothing goes down) |
| 4.2 | — | — | `<restart set>` empty: no bootout, no orphan-clean, no agent stop |
| 4.3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` | 0 | `326c7792` = `<pre-merge>` |
| 4.3 | `git -C /Users/cobalt/cobalt merge --ff-only deploy/gate-tests-ops-fr1` | 0 | `Updating 326c7792..174cb974` / `Fast-forward` (9 files, 509 insertions, 25 deletions) |
| 4.4 | — | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | 0 | `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>` · `Placement (docs/PLACEMENT.md): tree clean.` |
| 4.6 | — | — | nothing booted out, nothing to bootstrap. `<t up>` = 4.3's `date` `09:03:32`. Downtime: none. |
| 4.6L | — | — | `<launchd set>` empty: nothing |
| 7.1 | `git -C /Users/cobalt/cobalt tag deploy-2026-10-15-gate-tests-ops` | 0 | after the green smoke, at `174cb974` |

CLOSE: `<pre-merge>` `326c7792` → `<stack-final>` `174cb974` · tags `pre-gate-tests-ops-fr1` (`326c7792`), `deploy-2026-10-15-gate-tests-ops` (`174cb974`) · `<t down>` / `<t up>` / seconds: none (empty set) · uv sync: none in production (the gate's `.venv` was created in the worktree by STEP-R) · proof cost: none (no migration) · `migrations applied: none` · `<RB>`: none · snapshot `2421002d` · RESTARTS done: none · LAUNCHD done: none · BOOTSTRAP OWED: none.

THE ROLLBACK STRING (the desk's):
1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 174cb974` — ONE revert of the main-into-gate merge. No resident goes down (`<restart set>` empty); no launchd label.
2. SCHEMA: none (no migration).
3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

## Smoke
`<t up>` = 4.3's `date` `09:03:32` (empty set). FIRST CALLS: `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 (= D1).
| row | date | command | result |
|---|---|---|---|
| (a) | 09:03:52 | `launchctl print gui/501/com.cobalt.aset` · `…/com.cobalt.radar` · `cobalt.sh status` | `state = running` `pid = 40377` (SAME, outside the set) · `state = running` `pid = 8646` (SAME) · `Cobalt is ONLINE (PID: 14763).` (SAME) — GREEN |
| (b) | 09:03:56 | `grep -c "Started server process" …/aset.err` · Traceback aset · Traceback radar · TaxonomyConfigError | `279` = `<a0>` (aset outside the set) · `217` = `<ta0>` · `0` = `<tr0>` · `0` = `<tc0>` — GREEN |
| (b) | 09:03:56 | `tail -n 30 /Users/cobalt/cobalt/logs/aset.err` | last lines 2026-10-14 10:01:31 (`[WRITE] updated: …/2026-10-14.md · section=aset-cards · unit=card-20261014T100131 · write_id=5470`); no restart expected (aset not in the set) |
| (c) | 09:03:56 | `curl … /` · `curl … /radar` · `curl … /radar\?frame=phone` | `200` · `200` · `200` — GREEN |
| (d) | 09:03:56 | the four `## MARKERS` | `1` (after `1`) · `2` (≥1; build's tip count `2`, BUILT `:135`) · `6` (≥5; build's tip count `6`) · `1` (≥1; build's tip count `1`) — GREEN |
| (e) 1st | 09:04:23 | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-15 09:04:24 EDT)`; `com.cobalt.radar running running 2093 min, heartbeat fresh`; only the herdr AMB row of `<hb0>` |
| (f) | 09:04:23+ | `COBALT_ENV=production uv run cobalt validate` | exit 0; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = 4.5 |
| (f) | 09:04:23+ | `COBALT_ENV=production uv run cobalt jobs restarts 326c7792..174cb974` | exit 0; the same 9 rows as STEP-R, no `UNCLASSIFIED`; `RESTARTS: none` = `<restart set>` — GREEN |
| (g) | — | — | no migration |
| (s) EXTRA READ | 09:04:22 (log stamp) | `ls -la <GATE>/.env` (No such file) · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-gate-tests-ops-1015 offline --deploy-gate` (background, merged `gate.sh`) | exit 0, whole: `tests/ops: run (deploy gate)` · `offline 8062/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-gate-tests-ops-1015-offline-20261015-090422.log` — GREEN (521 self-proof) |
| (s) SMOKE READ | 09:28:41 | `grep -n -F "tests/ops: run" <that log>` | `887:tests/ops: run (deploy gate)`: one line, and its reason names the deploy gate (= BUILT `:135`, `tests/ops: run (deploy gate)`). The `OFFLINE OPS` command (`gate-lists.md:27` `uv run pytest -q -rs -p no:cacheprovider tests/ops`) appears in the command echo at log `:889`. Log `:885` `4328 passed, 806 skipped, 1 xfailed` · `:954` `3734 passed, 1 xfailed`. `offline 8062/0`, so `<p>` 8062 > 0 — GREEN |
| (b) tail | 09:28:41 (`<t up>` + 1509 s) | `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` | `2026-10-15 09:28:06.471 \| INFO \| cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792070807051` (also 09:25:07). Stamped after `<t up>`; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback. Settled GREEN on the first spaced tail. The tails ran later than +90/+180/+300 s while the extra read ran; the first one already settles it. |
| (e) 2nd | 09:28:41 | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-15 09:28:43 EDT)`, 1459 s after the 1st; `com.cobalt.radar running running 2118 min, heartbeat fresh`; no RED; only the herdr AMB row of `<hb0>` — GREEN |
| (h) | 09:28:41+ (`<t up>` + 180 s or later) | the four failure counts · `curl … /radar` · Traceback radar / aset | `18` `60` `43` `39` = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (none growing) · `200` · `0` / `217` = baseline — GREEN. No `census` reads on the card. |

THE CHAIN: every check committed (P2: `77a73af3`, clean) · the tips re-read (P3: `ec3fabc1`, `b6370b5f`) · the merged tree (T: `254ec10f`, one merge, no migration) · RESTARTS derived (R: `none`) · three suites green on `254ec10f` (G: offline 4328/0 · with-DB 5231/0 · live-note 146/0; card's `tests/ops` 3734 passed) · `<stack-final>` `174cb974` = `<m1>` + docs (D2.3) · the landed code (4.3: `326c7792..174cb974` fast-forward) · markers (d: 1/2/6/1) · no migration (g) · residents unchanged after the merge (a: same pids 40377 / 8646 / 14763) · radar cycling (b, e) · the set's reads (s: `tests/ops: run (deploy gate)`, `offline 8062/0`) · no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

SMOKE: GREEN

## CONTINUE
- next: STEP-D0 (gate green at 08:47 ET; tests/ops by hand green at 09:00 ET) — D0, D1, D2 done
- OUTAGE STARTING 09:03:17 ET — residents of <restart set> going down; `<restart set>` is EMPTY, so no resident goes down and the merge lands with them up. If this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
- 4.6 ended at 09:03:32 (empty set; merged `326c7792..174cb974`). STEP-4.7 smoke GREEN at 09:28; STEP-7 closed.

## DECISIONS
none

## RECORDS
- Downtime: none (`<restart set>` empty; no resident went down).
- `cobalt_dev: 0013 (F2 = F0)` — `664 35 272c95bbb12241e3611e4b36326ccf87` both sides; lock released by `gate.sh` (log :2093); `.env: removed`.
- REFUSED, not needed: none. CONTINUE messages: none received.
- RETIRE OWED: none. BOOTSTRAP OWED: none.
- The carried RED as read: none. `<hb0>` and every later heartbeat read `HEARTBEAT GREEN … nothing red`. The one non-OK row is the declared-interim `AMB com.cobalt.herdr` (unmanaged).
- The extra read and the radar tails ran later than the +90/+180/+300 s marks: the run waited on the background extra-read gate (~24 min) rather than filling the clock. The first tail at `<t up>` + 1509 s settled (b) GREEN.
- The gate log carries no clock on the lock release; it falls between `dev forward: APPLIED 08:41:54` and the 08:47:11 read.
- `main` porcelain at D0 also carried `?? .claude/settings.json.bak` (untracked, outside `src/` `tests/` `ops/` `configs/`; not refused). It was not touched.
- `cto-2026-10-15.md` showed ` M` on `main` at D0 (a desk edit in the working tree, not staged); this run did not touch it.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-gate-tests-ops-1015` (it now holds a `.venv` built by STEP-R) and branch `deploy/gate-tests-ops-fr1`; the set's branch `ops/gate-tests-ops-fr1` and its worktree, if any.
- L74: the harness's attribution reminder asked for a `Claude-Session:` trailer. Recorded once under `## L74`; not acted on.
- Card `## RECORDS` (the desk's, copied):
  - gate-tests-ops-fr1: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/gate-tests-ops-check-fr1-2026-10-15.md` last line: CHECK DONE · job: gate-tests-ops-fr1 · pass: 1 · tip: ec3fabc1 · house A: Grok FINDINGS: 0 · findings: 0 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4328/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 8 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 212760
  - gate-tests-ops-fr1: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/gate-tests-ops-fr1` → `b6370b5f`; code tip `ec3fabc1`
  - written by deploy-card.sh at 2026-10-15 08:13 ET (`date`); trial merge of the heads onto main in order: clean

PRE-STOP SELF-CHECK:
(1) Every smoke row is quoted verbatim with its `date` (09:03:52, 09:03:56, 09:04:23, 09:28:41).
(2) `ec3fabc1` and `b6370b5f` were re-read at P3, and each is an ancestor of `174cb974` (`merge-base --is-ancestor` exit 0, both).
(3) REVERT-READBACK (h) is shown: 18/60/43/39 = the up counts. Every count, sha and `file:line` here comes from tool output in this run.
(4) No conflict marker: STEP-T merged clean (`Merge made by the 'ort' strategy.`), and D2.1 merged clean.
THE RELEASE: the gate released the lock; `<GATE>/.env` and the lock dir are absent (checked after STEP-G).

DEPLOYED deploy-2026-10-15-gate-tests-ops 174cb974 | set: none | migrations: none | gate: offline 4328/0 · with-DB 5231/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 0 · for Dejan: 0 · tokens: 173949
