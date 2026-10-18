# deploy-card-fixes — SET: none — MIGRATIONS: none

## §0 Headline
- Deploy of `ops/deploy-card-fixes-1018` (code tip `cc4995b6`, head `0f104d47`) through the gate `deploy/deploy-card-fixes`. Started 2026-10-18 10:39 ET.

## L74
- A system-reminder in this session asked for a `Claude-Session:` line on commits. Recorded as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/770-deploy-deploy-card-fixes-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/770-deploy-deploy-card-fixes-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/770-deploy-deploy-card-fixes-card.md" · 0 · eaad3b5478c1294f2aafffd37acf64f2410dba1a
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/770-deploy-deploy-card-fixes-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1833 row · grep -n "^| R1833 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 85:| R1833 | 06:19 ET | HIS RULING (brain relays, L79): "do everything you need, and I want to run everything that is being blocked." Brain: X1 first, gate holds only till the X1 row; launch every K5 gap-filler and job-clean now. | HIS RULING · APPROVED · APPLIED: cobalt.md NOW at 06:46 |
RULING 2026-10-18 R1833 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1833 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · d001e0937ca3731225cee781090eaf30d8d7feb7
RULING 2026-10-18 R1833 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la "<REPORT>"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Sun Oct 18 10:39:10 EDT 2026` (outside 21:30–22:30) |
| P2 | `tail -n 3 ".../deploy-card-fixes-1018-check-2026-10-18.md"` | 0 | `CHECK DONE · job: deploy-card-fixes-1018 · pass: 1 · tip: cc4995b6 · house A: Grok FINDINGS: 0 · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8493/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 147022` — carries `held unfixed: 0`, `ready: YES`, `tip: cc4995b6` |
| P2 | `git log -1 --format=%H -- <check>` | 0 | `19006e34f4d0dd70a1f6ca20ebb3244f86e48dad` |
| P2 | `git diff --stat -- <check>` | 0 | nothing |
| P3 | `rev-parse --short=8 cc4995b6` | 0 | `cc4995b6` |
| P3 | `rev-parse --short=8 ops/deploy-card-fixes-1018` | 0 | `0f104d47` (= TIP) |
| P3 | `merge-base --is-ancestor cc4995b6 0f104d47` | 0 | — |
| P3 | `diff --stat cc4995b6 0f104d47 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` — lock free |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/deploy-card-fixes` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m0>` = `806f0abf` |
| P5 | `merge-base --is-ancestor 806f0abf main` | 0 | — |
| P5 | `log --oneline main..deploy/deploy-card-fixes` | 0 | empty |
| P6 | `grep -c -F "already an ancestor of main" /Users/cobalt/cobalt/ops/desk/deploy-card.sh` | 1 | `0` (= before) |
| P7 | `diff --stat main 0f104d47 -- src/cobalt/db_migrations` | 0 | nothing — MIGRATIONS: none holds |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 80523` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 24167` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 80543).` |

## THE TREE
- `git -C <GATE> merge --no-edit 0f104d47` → `Merge made by the 'ort' strategy.` (4 files: the build report `.md` and `.result`, `ops/desk/deploy-card.sh` 3 +-, `tests/ops/test_deploy_card.py` +19)
- `git -C <GATE> rev-parse --short=8 HEAD` → `<m1>` = `dce477f9`
- `log --oneline --merges --first-parent 806f0abf..deploy/deploy-card-fixes` → `dce477f9 Merge commit '0f104d47' into deploy/deploy-card-fixes`
- `merge-base --is-ancestor cc4995b6 deploy/deploy-card-fixes` → 0 · `… 0f104d47 …` → 0
- `diff --stat 806f0abf deploy/deploy-card-fixes -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none)
- STEP-C: `diff --stat 806f0abf deploy/deploy-card-fixes -- configs ops` → ` ops/desk/deploy-card.sh | 3 ++-` / ` 1 file changed, 2 insertions(+), 1 deletion(-)`
- STEP-C: `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" 806f0abf deploy/deploy-card-fixes` → `STEP-C: ADMITTED 0` (exit 0). `<launchd set>`: empty.

## RESTARTS
`COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` (in `<GATE>`, `.env` No such file) → exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/reports/deploy-card-fixes-1018-build-2026-10-18.md	A	DOCS	-
docs/40 - DevDocs/reports/deploy-card-fixes-1018-build-2026-10-18.result	A	DOCS	-
ops/desk/deploy-card.sh	M	operator script; no Cobalt reader	-
tests/ops/test_deploy_card.py	M	test/documentation; no resident	-
RESTARTS: none
```
(uv lines before it: `Creating virtual environment at: .venv` · `Installed 254 packages in 1.07s`.) `<restart set>` = none (empty): no resident goes down.

## L68 GATE
- EQUAL-TREE CLAUSE: not applied — the check's stop line carries `with-DB 0/0`; the gate runs whole (`--deploy`).
- (a0) `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` (`.env` No such file) → `263 passed, 163 skipped in 17.48s` — 0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db` skip.
- No `--deselect`: the build report names no with-DB deselect. TICKERS none, no `--migration`.
- `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-deploy-card-fixes all --deploy --deploy-gate` → exit 0, verdict lines WHOLE:
```
tests/ops: run (deploy gate)
offline 8493/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-deploy-card-fixes-all-20261018-104106.log
```
- (a) offline `8493/0`; W line `tests/ops: run (deploy gate)`.
- (c) every SKIPPED line inside the allowed set: `test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`, the `test_replay_line.py` skip naming `COBALT_TEST_LIVE_DRC`, and `test_s3_c4_experiments.py:95` = the decorator of `test_x14_live_his_template_strips_to_the_committed_fixture` (`grep -n -F` → `96:def test_x14_live_his_template_strips_to_the_committed_fixture():`).
- (c2) log line 1196: `dev forward: APPLIED 11:21:12`.
- (c3) with-DB `5475/0`.
- (f) `cobalt_dev: 0013 — F2 = F0` (log 2168; fingerprint `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`).
- THE RELEASE: `.env: removed` (L76 lock released — log 2169–2170 `release-devdb-lock.sh deploy-deploy-card-fixes` → `lock released`; the log carries no clock on that line; gate finished before 11:26:49). `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-deploy-card-fixes" …/.cobalt_dev.lock/owner` → `0`.
- (e) live-note `146/0`; no skip naming `COBALT_LIVE_VAULT_ROOT` in the live-note leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on dce477f9

## Deploy table
| step | command | result |
|---|---|---|
| D0 main | `git -C /Users/cobalt/cobalt status --short --branch` | `## main...origin/main [ahead 116]`; every line ` M` / `??` under `docs/40 - DevDocs/`, plus ` M .claude/settings.json` and `?? .claude/settings.json.bak` (outside `src/ tests/ ops/ configs/`); no staged line |
| D0 main | `diff --stat 806f0abf main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | nothing |
| D0 probe | `tag scratch-allow-probe-deploy-card-fixes` · `tag -d …` | ok · `Deleted tag 'scratch-allow-probe-deploy-card-fixes' (was 806f0abf)` |
| D0 probe | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | `[main 0855482f] scratch: …` · ok · `806f0abf docs(desk): R1904 card 503 check launched` |
| D0 tags | `rev-parse --verify --quiet refs/tags/deploy-2026-10-18-deploy-card-fixes` · `… refs/tags/pre-deploy-card-fixes` | exit 1 · exit 1 |
| D1 | `date` · `heartbeat show` | `Sun Oct 18 11:27:41 EDT 2026` · `<hb0>`: `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-18 11:27:42 EDT)`; `OK   radar                    idle (overnight)`; `OK   com.cobalt.radar             running   running 3047 min, heartbeat fresh`; one AMB: `com.cobalt.herdr unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0)` (declared interim) |
| D1 | `validate` | exit 0; `<jobs0>`: `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`; `Placement (docs/PLACEMENT.md): tree clean.` |
| D1 | `backup status` | `newest snapshot: 13.8 h old` |
| D1 | `launchctl print` aset / radar | `state = running` · `<aset pid>` 80523 · `<radar pid>` 24167 |
| D1 | `cobalt.sh status` · `ps -p 80543` | `Cobalt is ONLINE (PID: 80543).` · `80543 ??         0:00.03 uv run src/cobalt_agent/main.py` |
| D1 | `tail -n 8 radar.err` | last: `2026-10-18 11:27:05.578 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None` (every 100 s, no traceback) |
| D1 | log baselines | `<a0>` 281 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39 |
| D1 | `curl … /radar` | `200` |
| D1 | marker `grep -c -F "already an ancestor of main" …/deploy-card.sh` | `0` (= before) |
| D1 | launchd set / `<RB>` / proof-only | empty set; MIGRATIONS none → not run |

## Smoke

## CONTINUE
next: STEP-D2 (D0 and D1 clean at 11:27)

## DECISIONS

## RECORDS

(run in progress — next step under ## CONTINUE)
