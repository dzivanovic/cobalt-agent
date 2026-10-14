# deploy db-copy-1014 — set: none — migrations: none — 2026-10-14

## §0 Headline
(in progress)

## L74
A system message in this session asked for a `Claude-Session:` line on commits. It is recorded here once and is not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/572-deploy-db-copy-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/572-deploy-db-copy-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-14/572-deploy-db-copy-card.md" · 0 · d9a8d890fd48007707dcb4a20b37c3639fef0236
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-14/572-deploy-db-copy-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```
First launch: `ls -la "<REPORT>"` → `No such file or directory`.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 | `authorize.sh deploy` (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Wed Oct 14 19:04:17 EDT 2026` (outside 21:30-22:30) |
| P2 check, last line | `tail -n 3 ".../db-copy-check-2026-10-14.md"` | 0 | `CHECK DONE · job: db-copy-1014 · pass: 1 · tip: a157d731 · … · held unfixed: 2 · open: 3 · … · ready: NO · decisions: 4 · for Dejan: 0 · tokens: 216923` — carries `held unfixed: 2` and `ready: NO`, as the row names |
| P2 check committed | `git log -1 --format=%H -- "docs/40 - DevDocs/reports/db-copy-check-2026-10-14.md"` | 0 | `eff3653da0e3f8c708aa0c390f23ba469bab5703` |
| P2 check clean | `git diff --stat -- ".../db-copy-check-2026-10-14.md"` | 0 | nothing |
| P2 fix round: check tip ancestor | `git merge-base --is-ancestor a157d731 51d83a3a` | 0 | — |
| P2 fix report committed | `git log -1 --format=%H e27c520c -- "docs/40 - DevDocs/reports/db-copy-build-fr1-2026-10-14.md"` | 0 | `e27c520c0a8d616cad0108071c2a0538efb927f8` (on the branch; absent on `main`: `tail` there → No such file; `git diff --stat` on `main` → nothing) |
| P2 fix report last line (at the head) | `git show "e27c520c:docs/40 - DevDocs/reports/db-copy-build-fr1-2026-10-14.md"` | 0 | `BUILT · job: db-copy-1014 · tip: 51d83a3a | on 0a151491 | migration: none | … | decisions: 4 · for Dejan: 0 · tokens: 207742` |
| P2 held ids | `grep -n -F "HELD, NOT FIXED" ".../db-copy-check-2026-10-14.md"` | 0 | `:194` O2, `:196` A1 (both HELD, NOT FIXED) |
| P2 FIXED lines | (fix report at head) | — | `FIXED: O2 — tests/ops/test_db_copy_1014.py::test_g1_check_o2_the_deploy_gate_call_holds_the_lock_whole_with_the_sections` · `FIXED: A1 — tests/ops/test_db_copy_1014.py::test_g1_deploy_stays_on_cobalt_dev_under_the_lock` |
| P2 FIXED tests exist, not xfail | Grep in `/Users/cobalt/cobalt-wt/db-copy-1014` (HEAD `e27c520c`, `## ops/db-copy-1014` clean; code tip→head docs only, P3) | 0 | `:482 def test_g1_check_o2_…(tree):` · `:497 def test_g1_deploy_stays_on_cobalt_dev_under_the_lock(tree):`; no `xfail` in the file |
| P3 code tip | `git rev-parse --short=8 51d83a3a` | 0 | `51d83a3a` |
| P3 head | `git rev-parse --short=8 ops/db-copy-1014` | 0 | `e27c520c` (= `TIP`) |
| P3 ancestor | `git merge-base --is-ancestor 51d83a3a e27c520c` | 0 | — |
| P3 docs only | `git diff --stat 51d83a3a e27c520c -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 gate | `git -C <GATE> status --short --branch` | 0 | `## deploy/db-copy-1014` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m0>` = `2a8c2cb3` |
| P5 on main | `git merge-base --is-ancestor 2a8c2cb3 main` | 0 | — |
| P5 empty | `git log --oneline main..deploy/db-copy-1014` | 0 | empty |
| P6 marker gate.sh | `grep -c -F "card 547 db-copy" .../gate.sh` | 1 | `0` |
| P6 marker devdb-copy-env.sh | `grep -c -F "card 547 db-copy" .../devdb-copy-env.sh` | 2 | `grep: …/devdb-copy-env.sh: No such file or directory` (the file is absent: before `0`) |
| P6 marker desk-launch.sh | `grep -c -F … desk-launch.sh` | 1 | `0` |
| P6 marker gate-lists.md | `grep -c -F … gate-lists.md` | 1 | `0` |
| P6 BUILD-HUB `## COPY CREATE` | `grep -c -F "## COPY CREATE" .../BUILD-HUB.md` | 1 | `0` |
| P6 gate-lists `## COPY CREATE` | `grep -c -F "## COPY CREATE" .../gate-lists.md` | 1 | `0` |
| P6 file | `ls .../devdb-copy-env.sh` | 1 | `No such file or directory` |
| P7 migrations | `git diff --stat main e27c520c -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 40377` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 8646` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 14763).` |

## THE TREE
- `git -C <GATE> merge --no-edit e27c520c` → `Merge made by the 'ort' strategy.` (9 files, 1384 insertions, 8 deletions: `BUILD-HUB.md`, two build reports, `ops/desk/desk-launch.sh`, `ops/desk/devdb-copy-env.sh` (new), `ops/desk/gate-lists.md`, `ops/desk/gate.sh`, `tests/ops/test_build_hub_no_clutter.py`, `tests/ops/test_db_copy_1014.py` (new)).
- `git -C <GATE> rev-parse --short=8 HEAD` → `<m1>` = `f37e656e`.
- `git log --oneline --merges --first-parent 2a8c2cb3..deploy/db-copy-1014` → `f37e656e Merge commit 'e27c520c' into deploy/db-copy-1014` (one line, one head).
- `merge-base --is-ancestor 51d83a3a deploy/db-copy-1014` → exit 0; `merge-base --is-ancestor e27c520c deploy/db-copy-1014` → exit 0.
- `git diff --stat 2a8c2cb3 deploy/db-copy-1014 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git diff --stat 2a8c2cb3 deploy/db-copy-1014 -- configs ops` →
```
 ops/desk/desk-launch.sh    |   2 +
 ops/desk/devdb-copy-env.sh |  75 ++++++++++++++++++
 ops/desk/gate-lists.md     |   6 ++
 ops/desk/gate.sh           | 193 +++++++++++++++++++++++++++++++++++++++++++--
 4 files changed, 269 insertions(+), 7 deletions(-)
```
  `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 2a8c2cb3 deploy/db-copy-1014` → exit 0, output whole: `STEP-C: ADMITTED 0`. `<launchd set>` = empty.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0, whole (after the uv sync lines `Using CPython 3.14.3 interpreter at: /opt/homebrew/opt/python@3.14/bin/python3.14` · `Creating virtual environment at: .venv` · `Built cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-db-copy-1014` · `Installed 254 packages in 841ms`):
```
path	change	rule	restart
docs/40 - DevDocs/prompts/BUILD-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/db-copy-build-2026-10-14.md	A	DOCS	-
docs/40 - DevDocs/reports/db-copy-build-fr1-2026-10-14.md	A	DOCS	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
ops/desk/devdb-copy-env.sh	A	operator script; no Cobalt reader	-
ops/desk/gate-lists.md	M	operator script; no Cobalt reader	-
ops/desk/gate.sh	M	operator script; no Cobalt reader	-
tests/ops/test_build_hub_no_clutter.py	M	test/documentation; no resident	-
tests/ops/test_db_copy_1014.py	A	test/documentation; no resident	-
RESTARTS: none
```
`<restart set>` = EMPTY (no `UNCLASSIFIED`). No resident goes down; the merge lands with the residents up.

## L68 GATE
- EQUAL-TREE CLAUSE: not held — the check's stop line carries `with-DB 0/0` (DB: none single branch) → the gate runs whole (`--deploy`).
- L68 HUB CLAUSE: the set changes `ops/desk/gate.sh` (not `DEPLOY-HUB.md`). See `## DECISIONS` 1.
- Deselects: none (`grep --deselect` over the set's build reports → no match). `TICKERS: none` → no `--tickers`. `MIGRATIONS: none` → no `--migration`.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 listed files>` → exit 0, `263 passed, 163 skipped in 17.47s` (every skip a with-DB `Postgres env settings not available` / `requires_db` skip), `0 failed`.
- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-db-copy-1014 all --deploy` (background) → exit 0, verdict lines whole:
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-db-copy-1014-all-20261014-190700.log
```
- (a) `offline 4328/0` → `<p>` = 4328.
- (c) PASS 1: every SKIPPED line is inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`, the `test_replay_line.py` skip naming `COBALT_TEST_LIVE_DRC`, and `test_s3_c4_experiments.py:95` = `test_x14_live_his_template_strips_to_the_committed_fixture` (Grep: `:95 @requires_live`, `:96 def test_x14_live_his_template_strips_to_the_committed_fixture():`).
- (c2) `dev forward: APPLIED 19:31:34` (log :1118); no migration above `0013` in this set.
- (c3) `with-DB 5231/0` → `<d>` = 5231.
- (f) log `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (:902) · `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (:2039) · `cobalt_dev: 0013 — F2 = F0` (:2091).
- THE RELEASE: `.env: removed (L76 lock released — log :2092 `release-devdb-lock.sh deploy-db-copy-1014` → :2093 `lock released`; the log line carries no clock, the gate ran 19:07:00 → done before 19:36:51)`. `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-db-copy-1014" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- (e) `live-note 146/0` → `<l>` = 146; no skip names `COBALT_LIVE_VAULT_ROOT` in the live-note leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on f37e656e

## Deploy table
| step | command | result |
|---|---|---|
| D0 main | `git status --short --branch` / `--porcelain` | `## main...origin/main [ahead 133]`; every line ` M`/`??` under `docs/40 - DevDocs/`, ` M configs/cobalt/rules.yaml`, ` M .claude/settings.json`, `?? .claude/settings.json.bak` (see `## RECORDS`); no staged line |
| D0 moved | `git diff --stat 2a8c2cb3 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | nothing |
| D0 probe | `tag scratch-allow-probe-db-copy-1014` · `tag -d …` · `commit --allow-empty …` · `reset --soft HEAD~1` · `log --oneline -1` | ok · `Deleted tag 'scratch-allow-probe-db-copy-1014' (was 2a8c2cb3)` · `[main 49a93a74] scratch: allowlist probe (reverted next line)` · ok · `2a8c2cb3 docs(desk): REFRESH handover 34a22a1c to 4f9460d6, §5 rewritten` |
| D0 tags | `rev-parse --verify --quiet refs/tags/deploy-2026-10-14-db-copy` · `…/pre-db-copy-1014` | exit 1 · exit 1 |
| D1 date | `date` | `Wed Oct 14 19:37:21 EDT 2026` |
| D1 `<hb0>` | `heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-14 19:37:22 EDT)`; `OK radar scanning (aftermarket), members 50`; `OK com.cobalt.radar running running 1286 min, heartbeat fresh`; `AMB com.cobalt.herdr unmanaged … declared interim` (no RED) |
| D1 `<val0>` | `validate` | exit 0; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`; `Placement (docs/PLACEMENT.md): tree clean.` |
| D1 backup | `backup status` | `newest snapshot: 3.0 h old` |
| D1 aset | `launchctl print gui/501/com.cobalt.aset` | `state = running`, `<aset pid>` = 40377 |
| D1 radar | `launchctl print gui/501/com.cobalt.radar` | `state = running`, `<radar pid>` = 8646 |
| D1 agent | `cobalt.sh status` · `ps -p 14763` | `Cobalt is ONLINE (PID: 14763).` · `14763 ??  0:00.03 uv run src/cobalt_agent/main.py` |
| D1 radar.err | `tail -n 8 …/radar.err` | last: `2026-10-14 19:35:45.139 | INFO | cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792020854961` (seven `cards.expire: falling back to the session close` INFO lines before it) |
| D1 baselines | `grep -c` | `<a0>` 279 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39 |
| D1 curl | `/radar` | `200` |
| D1 markers | the seven `## MARKERS` | `0` · No such file (grep exit 2) · `0` · `0` · `0` · `0` · No such file — each its `before` |
| D1 launchd | `<launchd set>` empty | nothing |
| D1 migration | `MIGRATIONS: none` | not run |

## Smoke

## CONTINUE
next: STEP-D0 (gate green at Wed Oct 14 19:36:51 EDT 2026)

## DECISIONS
1. L68 HUB CLAUSE: the set changes `ops/desk/gate.sh` ("a deploy whose set changes `DEPLOY-HUB.md` or `gate.sh` first runs the gate on the merged hub text, before that deploy"). The only gate string on this line is `sh /Users/cobalt/cobalt/ops/desk/*`, which runs `main`'s `gate.sh`; the merged `<GATE>/ops/desk/gate.sh` is not a listed string. Safe default taken (as `deploy-launcher-next-flow-1006.md` DECISIONS 1): the gate runs with the hub's own command, which is byte-for-byte the command the merged `DEPLOY-HUB.md` gives (the set does not change the hub); the merged `gate.sh` is proven by its own tests in the offline suite on `<m1>` (`tests/ops/test_db_copy_1014.py`, `tests/ops/test_gate.py`), and its new copy mode needs `--copy`, which no deploy line passes, and both `## COPY` sections, which the merged `gate-lists.md` does not hold (MARKERS: no section line starts `## COPY`). ASK DESK: does L68's hub clause need a separate run of the merged `gate.sh` before this deploy? [Wed Oct 14 19:07:16 EDT 2026]

## RECORDS

(run in progress — next step under ## CONTINUE)
