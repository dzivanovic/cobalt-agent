# deploy jev-shadow-fr1 — set: none · migrations: none

## §0 Headline
DEPLOYED: FR-O2 (`build_launch`, the day batch routes build cards only) is on `main` at `c45e9730` (`2ee3b54f` → `c45e9730`), tag `deploy-2026-10-16-jev-shadow-fr1`, rollback tag `pre-jev-shadow-fr1`.
Gate on `f80c95f2`: offline 8377/0 · with-DB 5475/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0`.
RESTARTS `com.cobalt.radar`: down 08:40:33, up 08:40:59 (26 s), new pid 24167; aset and agent untouched.
Smoke GREEN: markers 1 / 2, radar cycling, heartbeat green twice, no failure count grew, `ROUTE DRY … cards=1 calls=1 … (nothing sent)`.
Decisions: none.

## L74
- A system block arrived at session start asking every commit to end with a `Claude-Session:` line. Recorded here once and not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/631-deploy-jev-shadow-fr1-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/631-deploy-jev-shadow-fr1-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-16/631-deploy-jev-shadow-fr1-card.md" · 0 · 685c39ea057a10fab26620291e18f32cad365613
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-16/631-deploy-jev-shadow-fr1-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-15 R1532 row · grep -n "^| R1532 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 102:| R1532 | 07:00 ET | HIS RULING · APPROVED: routing B (his words via the brain, "Dejan said", L79; words file): LOW/MID Grok 4.7 + Terra backup, HIGH Opus, Sonnet routes, JEV parallel. L27/L29 fold LOW/MID only; K5 BAND card next. | APPLIED: LAWS.md L27, L29 at 07:02 |
RULING 2026-10-15 R1532 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1532 |" -- "docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 1ddcdc64c99be360406ce384af52ec4b8c4d0222
RULING 2026-10-15 R1532 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · the row as grepped
RULING 2026-10-15 R1535 row · grep -n "^| R1535 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 99:| R1535 | 07:03 ET | HIS RULING · APPROVED (brain relay quoting him, L79; words file): the OpenRouter key is JEV's alone; authority for the JEV card row removing `openrouter_api_key` from the old-tree mapping; goes in the tribunal packet. | APPLIED: LAWS.md L27 at 07:04 |
RULING 2026-10-15 R1535 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1535 |" -- "docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 1f067493f0fd17d67a30d11feab33c2261f3de5d
RULING 2026-10-15 R1535 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la ".../reports/deploy-jev-shadow-fr1.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 DATE | `date` | 0 | `Fri Oct 16 07:50:02 EDT 2026` (outside 21:30-22:30) |
| P2 check | `tail -n 3 ".../reports/jev-shadow-check-2026-10-15.md"` | 0 | `CHECK DONE · job: jev-shadow-1015 · pass: 1 · tip: 5316fafe · house A: grok FINDINGS: 2 · findings: 8 · dropped: 0 · held: 7 · fixed: 7 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8307/0 · with-DB 5471/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar · files opened: 21 · ready: YES · decisions: 3 · for Dejan: 1 · tokens: 329407` — carries `held unfixed: 0` and `ready: YES` |
| P2 check committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/jev-shadow-check-2026-10-15.md"` | 0 | `223e0859f121289334e1b9239d9f7311db9eeb35` |
| P2 check clean | `git -C /Users/cobalt/cobalt diff --stat -- "<check>"` | 0 | nothing |
| P2 fix-round tip | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 5316fafe 6a74fa0c` | 0 | — |
| P2 fix report | `git -C /Users/cobalt/cobalt show "d2066509:docs/40 - DevDocs/reports/jev-shadow-build-fr1-2026-10-16.md"` | 0 | last line `BUILT · job: jev-shadow-fr1 · tip: 6a74fa0c \| on f6ca1455 \| migration: none \| offline 4572/0 \| with-DB 5475/0 \| live-note 146/0 \| cobalt_dev: 0013 \| .env: removed \| RESTARTS: com.cobalt.radar \| rows: 1 of 1 \| self-check: 3 of 3 \| decisions: 3 · for Dejan: 0 · tokens: 187978` |
| P2 fix report committed | `git -C /Users/cobalt/cobalt log -1 --format=%H d2066509 -- "<fix report>"` | 0 | `d2066509b240a1c8c449f3e56d76d92c792e81d8` (on the branch; `log -1 -- <path>` on main → empty, the report is not on `main` yet) |
| P2 fix report unmodified | `git -C /Users/cobalt/cobalt diff --stat -- "<fix report>"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 6a74fa0c` | 0 | `6a74fa0c` |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 feat/jev-shadow-fr1` | 0 | `d2066509` = `TIP` |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 6a74fa0c d2066509` | 0 | — |
| P3 docs-only head | `git -C /Users/cobalt/cobalt diff --stat 6a74fa0c d2066509 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 gate | `git -C /Users/cobalt/cobalt-wt/deploy-jev-shadow-fr1 status --short --branch` | 0 | `## deploy/jev-shadow-fr1` |
| P5 m0 | `git -C /Users/cobalt/cobalt-wt/deploy-jev-shadow-fr1 rev-parse --short=8 HEAD` | 0 | `685c39ea` = `<m0>` |
| P5 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 685c39ea main` | 0 | — |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/jev-shadow-fr1` | 0 | empty |
| P6 marker 1 | `grep -c -F "def build_launch" /Users/cobalt/cobalt/src/cobalt/classify/route.py` | 1 | `0` = before |
| P6 marker 2 | `grep -c -F "NOT_BUILD_HEADERS" /Users/cobalt/cobalt/src/cobalt/classify/route.py` | 1 | `0` = before |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main d2066509 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `pid = 80523` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `pid = 80533` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 80543).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-jev-shadow-fr1 merge --no-edit d2066509` → `Merge made by the 'ort' strategy.` (5 files: `route.md`, `jev-shadow-build-fr1-2026-10-16.md`, `jev-shadow-build-fr1-2026-10-16.result`, `src/cobalt/classify/route.py`, `tests/cobalt/test_jev_shadow_1015.py`; 292 insertions, 6 deletions).
- `rev-parse --short=8 HEAD` → `<m1>` = `f80c95f2`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 685c39ea..deploy/jev-shadow-fr1` → `f80c95f2 Merge commit 'd2066509' into deploy/jev-shadow-fr1` (one per head).
- `merge-base --is-ancestor 6a74fa0c deploy/jev-shadow-fr1` → exit 0; `merge-base --is-ancestor d2066509 deploy/jev-shadow-fr1` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat 685c39ea deploy/jev-shadow-fr1 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 685c39ea deploy/jev-shadow-fr1 -- configs ops` → nothing. `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 685c39ea deploy/jev-shadow-fr1` → exit 0, whole: `STEP-C: ADMITTED 0`. `<launchd set>` = empty.

## RESTARTS
`cd /Users/cobalt/cobalt-wt/deploy-jev-shadow-fr1` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0:
```
Using CPython 3.14.3 interpreter at: /opt/homebrew/opt/python@3.14/bin/python3.14
Creating virtual environment at: .venv
   Building cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-jev-shadow-fr1
      Built cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-jev-shadow-fr1
Installed 254 packages in 765ms
path	change	rule	restart
docs/40 - DevDocs/cobalt/classify/route.md	M	DOCS	-
docs/40 - DevDocs/reports/jev-shadow-build-fr1-2026-10-16.md	A	DOCS	-
docs/40 - DevDocs/reports/jev-shadow-build-fr1-2026-10-16.result	A	DOCS	-
src/cobalt/classify/route.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_jev_shadow_1015.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.radar` (matches the card's expectation). `<launchd set>` = empty.

## L68 GATE
- EQUAL-TREE CLAUSE: not applied — the check's tip `5316fafe` is not the tree at `<m1>` (the fix round changed `route.py`); the gate runs whole.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 17.69s` (0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db`).
- `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-jev-shadow-fr1 all --deploy --deploy-gate` (no `--deselect`: the build report names none; no `--tickers`; no `--migration`) → exit 0. Verdict lines, whole:
```
tests/ops: run (deploy gate)
offline 8377/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5475/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-jev-shadow-fr1-all-20261016-075221.log
```
- (a) offline `8377/0`; W line `tests/ops: run (deploy gate)`.
- (b) lock waited 0 min; `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:975`); proof-only nothing CHANGED; `LEVEL 0013`.
- (c) pass 1 whole; every SKIPPED line is inside the allowed set (`test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_replay_line.py` COBALT_TEST_LIVE_DRC, `test_s3_c4_experiments.py` live template read, `test_catalyst.py:365`, `test_predicate.py:262`).
- (c2) `dev forward: APPLIED 08:32:24` (log `:1194`).
- (c3) `with-DB 5475/0`.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:2114`) = F0 field for field: `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: log `:2167-2168` `sh /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh deploy-jev-shadow-fr1` → `lock released`; `.env: removed` (L76 lock released after 08:32:24, before 08:37:27 — the log line carries no clock). `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-jev-shadow-fr1" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- (e) `live-note 146/0`; its one skip names `COBALT_TEST_LIVE_DRC` (allowed).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on f80c95f2

## Deploy table
| step | command | exit | result |
|---|---|---|---|
| D0 main | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 23]` |
| D0 porcelain | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`, ` M configs/cobalt/rules.yaml`, ` M`/`??` under `docs/40 - DevDocs/` only, and `?? .claude/settings.json.bak` (not under src/tests/ops/configs; not refused — recorded); no staged line |
| D0 moved | `git -C /Users/cobalt/cobalt diff --stat 685c39ea main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| D0 probe | `tag scratch-allow-probe-jev-shadow-fr1` · `tag -d …` | 0 · 0 | — · `Deleted tag 'scratch-allow-probe-jev-shadow-fr1' (was 685c39ea)` |
| D0 probe | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 01becf82] scratch: …` · — · `685c39ea docs(card): R1644 FR-O2 BUILT, deploy card 631 jev-shadow-fr1` |
| D0 tags | `rev-parse --verify --quiet refs/tags/deploy-2026-10-16-jev-shadow-fr1` · `… refs/tags/pre-jev-shadow-fr1` | 1 · 1 | absent · absent |
| D1 date | `date` | 0 | `Fri Oct 16 08:38:03 EDT 2026` |
| D1 `<hb0>` | `COBALT_ENV=production uv run cobalt heartbeat show` | 0 | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-16 08:38:04 EDT)`; `OK   radar                    scanning (premarket), members 50`; `OK   com.cobalt.radar             running   running 852 min, heartbeat fresh`; one `AMB  com.cobalt.herdr unmanaged` (declared interim) |
| D1 `<val0>` | `COBALT_ENV=production uv run cobalt validate` | 0 | `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` |
| D1 backup | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 11.0 h old` |
| D1 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `<aset pid>` = `80523` |
| D1 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `<radar pid>` = `80533` |
| D1 agent | `/Users/cobalt/cobalt/cobalt.sh status` · `ps -p 80543` | 0 · 0 | `Cobalt is ONLINE (PID: 80543).` · `80543 ??         0:00.03 uv run src/cobalt_agent/main.py` |
| D1 radar.err | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | 0 | last `2026-10-16 08:38:12.378 \| INFO \| cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792154208288`; no traceback |
| D1 counts | `grep -c` Started server process (aset.err) · Traceback (aset.err) · Traceback (radar.err) · TaxonomyConfigError (radar.err) · radar panel FAILED (aset.err) · radar pool refresh FAILED (aset.err) · radar S5 evaluate FAILED (radar.err) · lifecycle card read failed (radar.err) | — | `<a0>` 281 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39 |
| D1 curl | `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` | 0 | `200` |
| D1 markers | the two `## MARKERS` greps | 1 · 1 | `0` · `0` (= before) |
| D1 launchd set | — | — | empty: nothing |
| D1 migration | — | — | MIGRATIONS: none: no `<RB>`, no proof-only |
| D2.0 shipped | `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --moved 685c39ea "<card>"` | 0 | nothing |
| D2.0 commit | `git -C /Users/cobalt/cobalt commit -m "docs(report): deploy jev-shadow-fr1 — gate green on f80c95f2" …` · `show --stat HEAD` | 0 · 0 | `[main 2ee3b54f] …` · one file `docs/40 - DevDocs/reports/deploy-jev-shadow-fr1.md \| 152 +++` |
| D2.0 pre-merge | `git -C /Users/cobalt/cobalt rev-parse --short=8 main` | 0 | `<pre-merge>` = `2ee3b54f` |
| D2.1 | `git -C /Users/cobalt/cobalt-wt/deploy-jev-shadow-fr1 merge --no-edit main` | 0 | `Merge made by the 'ort' strategy.` (the report, 152 +) |
| D2.2 | `rev-parse --short=8 HEAD` · `rev-parse --short=8 c45e9730^2` · `merge-base --is-ancestor f80c95f2 c45e9730` | 0 · 0 · 0 | `<stack-final>` = `c45e9730` · `2ee3b54f` = `<pre-merge>` · — |
| D2.3 | `git -C /Users/cobalt/cobalt diff --stat f80c95f2 c45e9730 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| D2.4 status | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 11.0 h old` |
| D2.4 run | `COBALT_ENV=production uv run cobalt backup run` (08:39:10) | 0 | `backup: cobalt_brain via pg_dump inside cobalt_memory — 8580.1 MB` · `ssd: snapshot d604b539 — 1 new / 2 changed, 314.5 MB added, 1 pruned` |
| D2.4 status | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 0.0 h old` |
| D2.5 | `date` · `heartbeat show` | 0 · 0 | `Fri Oct 16 08:40:14 EDT 2026` · `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-16 08:40:15 EDT)` (131 s after D1's 08:38:04); radar `running 854 min, heartbeat fresh` |
| D2.6 | `date` · `git -C /Users/cobalt/cobalt tag pre-jev-shadow-fr1` | 0 · 0 | `Fri Oct 16 08:40:20 EDT 2026` · tag at `2ee3b54f` |
| 4.1 | `date` | 0 | `<t down>` = `Fri Oct 16 08:40:33 EDT 2026` |
| 4.2 | `launchctl bootout gui/501/com.cobalt.radar` · `launchctl print gui/501/com.cobalt.radar` | 0 · 113 | — · `Could not find service "com.cobalt.radar" in domain for user gui: 501` (aset, agent not in the set: no call; no orphan-clean) |
| 4.3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` · `merge --ff-only deploy/jev-shadow-fr1` | 0 · 0 | `2ee3b54f` = `<pre-merge>` · `Updating 2ee3b54f..c45e9730` `Fast-forward` (5 files, 292 +, 6 −) |
| 4.4 | — | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | 0 | `13 trade_def(s) validated OK from the vault.` … `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>` |
| 4.6 | `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `launchctl print gui/501/com.cobalt.radar` | 0 · 0 | — · `state = running`, `pid = 24167` (≠ D1's 80533), `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` |
| 4.6 | `date` | 0 | `<t up>` = `Fri Oct 16 08:40:59 EDT 2026` · downtime 26 s |
| 4.6L | — | — | `<launchd set>` empty: `LAUNCHD done: none` |
| STEP-7 tag | `git -C /Users/cobalt/cobalt tag deploy-2026-10-16-jev-shadow-fr1` (after green smoke) | 0 | at `c45e9730` |

Summary: `<pre-merge>` `2ee3b54f` → `<stack-final>` `c45e9730` · tags `pre-jev-shadow-fr1` (`2ee3b54f`), `deploy-2026-10-16-jev-shadow-fr1` (`c45e9730`) · `<t down>` 08:40:33 / `<t up>` 08:40:59 / 26 s · uv sync: none on the production tree (the gate's `.venv` creation at STEP-R was in `<GATE>`) · proof cost: none (no migration) · `migrations applied: none` · `<RB>`: none · snapshot `d604b539` · `RESTARTS done: com.cobalt.radar` · `LAUNCHD done: none` · no `BOOTSTRAP OWED`.

THE ROLLBACK STRING (the desk's):
1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 c45e9730`, with `com.cobalt.radar` booted out first and bootstrapped (`/Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`) after; no launchd set.
2. SCHEMA: none (no migration).
3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

## Smoke
| row | date | command | result |
|---|---|---|---|
| first calls | 08:40:59+ | the four failure counts | `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 |
| (a) | 08:41:15 | `launchctl print gui/501/com.cobalt.aset` · radar (4.6) · `cobalt.sh status` | aset `state = running`, `pid = 80523` (same, outside the set) · radar `state = running`, `pid = 24167` (new) · `Cobalt is ONLINE (PID: 80543).` (same) |
| (b) counts | 08:41:15 | `grep -c` Started server process · Traceback aset · Traceback radar · TaxonomyConfigError | `281` = `<a0>` (aset outside the set) · `217` = `<ta0>` · `0` = `<tr0>` · `0` = `<tc0>` |
| (c) | 08:41:15 | the three curls | `200` · `200` · `200` |
| (d) | 08:41:15 | `grep -c -F "def build_launch" …/route.py` · `grep -c -F "NOT_BUILD_HEADERS" …/route.py` | `1` · `2` (= after) |
| (f) | 08:41:39 | `COBALT_ENV=production uv run cobalt validate` (4.5, 08:40:4x) · `COBALT_ENV=production uv run cobalt jobs restarts 2ee3b54f..c45e9730` | validate exit 0, as 4.5 · exit 0, `RESTARTS: com.cobalt.radar` = STEP-R, no `UNCLASSIFIED` |
| (s) 1 | — | `uv run pytest -q tests/cobalt/test_jev_shadow_1015.py` — quoted from the gate (hub (s): a test the gate ran is quoted from the gate; no test runs in production) | gate log `:123` and `:1179` `tests/cobalt/test_jev_shadow_1015.py: 15 warnings` (offline and pass 1 ran it) inside `offline 8377/0` and `with-DB 5475/0`: 0 failed |
| (s) 2 | 08:41:4x | `uv run cobalt classify route --card "docs/40 - DevDocs/prompts/2026-10-15/580-close-automation-card.md" --dry-run` | exit 0: `ROUTE DRY card=docs/40 - DevDocs/prompts/2026-10-15/580-close-automation-card.md launch=1bd425f59159b95f29d90a14763098699dbf2301 bytes=35773 tokens_est=8944 projected_usd=0.00037565 guard=ok` · `ROUTE DRY TOTAL cards=1 calls=1 projected_usd=0.00037565 (nothing sent)` — one `ROUTE DRY` line, `cards=1 calls=1`, nothing sent |
| (e) 1 | 08:41:49 | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-16 08:41:50 EDT)`; `OK   com.cobalt.radar             running   running 1 min, heartbeat fresh` |
| (g) | — | — | no migration |
| (b) radar tail 1 | 08:42:29 (`<t up>` + 90 s) | `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` | `2026-10-16 08:42:15.239 \| INFO \| cobalt.radar.runner:resident:638 - radar cycle: scanning scan_id=1792154455855` (after `<t up>` 08:40:59); no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback in the tail → GREEN, settled |
| (e) 2 | 08:43:41 | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-16 08:43:42 EDT)` (112 s after (e) 1); `OK   com.cobalt.radar             running   running 3 min, heartbeat fresh`; no RED (none in `<hb0>` either) |
| (h) | 08:43:59 (`<t up>` + 180 s) | the four failure counts · `/radar` curl | `18` · `60` · `43` · `39` = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (none grew) · `200`; no `census` reads on the card |
| (b) radar tail 2 | 08:43:59 | `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` | `08:44:06` collect lines after the `08:42:15.239 … radar cycle: scanning scan_id=1792154455855` line; no failure, no traceback |

THE CHAIN: every check committed (P2: check `223e0859`, fix report at `d2066509`) → the tips re-read (P3: `6a74fa0c`, `d2066509`) → the merged tree `f80c95f2` (T, clean) → RESTARTS derived `com.cobalt.radar` (R) → three suites green on `f80c95f2` (G) → `<stack-final>` `c45e9730` = `f80c95f2` + docs (D2.3) → the landed code (4.3 `Updating 2ee3b54f..c45e9730`) → markers `1` / `2` (d) → no migration (g) → radar up on a new pid after the merge, aset / agent same pid (a) → radar cycling (b) and heartbeat fresh twice (e) → the set's reads green (s) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

## CONTINUE
- The outage entry written at D2.6 (08:40:20) ended at 4.6 (`<t up>` 08:40:59, radar running).
- next: none — DEPLOYED; push is his, through the desk (L55).

## PRE-STOP SELF-CHECK
1. Every smoke row's evidence is quoted verbatim with its `date` (`## Smoke`).
2. Every code tip and head was re-read (P3: `6a74fa0c`, `d2066509`), and each is an ancestor of `<stack-final>`: `git -C /Users/cobalt/cobalt merge-base --is-ancestor 6a74fa0c c45e9730` → exit 0; `… d2066509 c45e9730` → exit 0; `rev-parse --short=8 main` → `c45e9730`.
3. REVERT-READBACK (h) is shown: counts `18 · 60 · 43 · 39` at 08:43:59, equal to `<rp_up>` … `<lc_up>`. Every count, sha and `file:line` here was read from tool output in this run.
4. No conflict marker: STEP-T `Merge made by the 'ort' strategy.`, and D2.1 the same.

## DECISIONS
none

## RECORDS
- Run: opened 07:50:02 EDT (`date`), closed 08:44:13 EDT. Downtime 26 s (radar only), under 300 s.
- `cobalt_dev: 0013 (F2 = F0)` — F0 / F2 `664 35 272c95bbb12241e3611e4b36326ccf87`; lock released inside `gate.sh` (log `:2167-2168`); `<GATE>/.env` absent.
- L74: the `Claude-Session:` commit-line request (a system block at session start) was recorded under `## L74` and not acted on.
- No `REFUSED, not needed` line; no `CONTINUE` message arrived from any session.
- No `RETIRE OWED`, no `BOOTSTRAP OWED`. Carried RED: none. `<hb0>` held no RED, only the declared-interim `AMB com.cobalt.herdr unmanaged`.
- D0 porcelain held `?? .claude/settings.json.bak`. It is not under `src/`, `tests/`, `ops/` or `configs/` and is not staged, so D0 does not refuse it. Recorded here for the desk.
- The fix report is on `main` only through this merge. Before 4.3, `git log -1 -- <fix report>` on `main` printed nothing; the P2 commit proof was read at the branch head (`d2066509`).
- The (s) pytest line was quoted from the gate log (hub (s): no test runs in production). The `classify route --dry-run` ran from `/Users/cobalt/cobalt` with exit 0 and sent nothing.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-jev-shadow-fr1` and branch `deploy/jev-shadow-fr1`; the set's branch `feat/jev-shadow-fr1` and its worktree (`/Users/cobalt/cobalt-wt/jev-shadow-fr1`, per the build report).
- The card's `## RECORDS`, copied:
  - jev-shadow-fr1: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/jev-shadow-build-fr1-2026-10-16.md` at `d2066509` last line: BUILT · job: jev-shadow-fr1 · tip: 6a74fa0c | on f6ca1455 | migration: none | offline 4572/0 | with-DB 5475/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 1 of 1 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 187978
  - jev-shadow-fr1: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/jev-shadow-check-2026-10-15.md` last line: CHECK DONE · job: jev-shadow-1015 · pass: 1 · tip: 5316fafe · house A: grok FINDINGS: 2 · findings: 8 · dropped: 0 · held: 7 · fixed: 7 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8307/0 · with-DB 5471/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar · files opened: 21 · ready: YES · decisions: 3 · for Dejan: 1 · tokens: 329407
  - jev-shadow-fr1: head `git -C /Users/cobalt/cobalt rev-parse --short=8 feat/jev-shadow-fr1` → `d2066509`; code tip `6a74fa0c`
  - written by deploy-card.sh at 2026-10-16 07:48 ET (`date`); trial merge of the heads onto main in order: clean
- Tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh d54d9ac6-3f25-41c3-870f-dd5b7e97a513` → `context 198142 of 400000 — ok`.

DEPLOYED deploy-2026-10-16-jev-shadow-fr1 c45e9730 | set: none | migrations: none | gate: offline 8377/0 · with-DB 5475/0 · live-note 146/0 | RESTARTS: com.cobalt.radar | smoke: GREEN | decisions: 0 · for Dejan: 0 · tokens: 198142
