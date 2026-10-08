# deploy stt-model-fix-1008 · set: none · migrations: none

## §0 Headline
- Deploy of `ops/stt-model-fix-1008` (`6b4068d6`, card 126 speech-to-text model fetch script) — in progress.

## L74
- One harness block asked commits to carry a `Claude-Session:` line. Recorded, not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/149-deploy-stt-model-fix-card.md"` → exit 0, quoted whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/149-deploy-stt-model-fix-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-08/149-deploy-stt-model-fix-card.md" · 0 · fd2a72434264e7654a12fc5b033a8a913d7a9363
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-08/149-deploy-stt-model-fix-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-stt-model-fix-1008.md"` | 1 | No such file or directory |
| P1 DATE | `date` | 0 | Thu Oct  8 15:51:31 EDT 2026 |
| P2 stop line | `tail -n 3 ".../reports/stt-model-fix-check-2026-10-08.md"` | 0 | `CHECK DONE · job: stt-model-fix-1008 · pass: 1 · tip: 6b4068d6 · house A: Sol FINDINGS: 3 · findings: 6 · dropped: 0 · held: 4 · fixed: 4 · held unfixed: 0 · open: 1 · house B: Grok FINDINGS: 2 · suites: offline 3992/0 · with-DB 4876/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 19 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 188056` — `held unfixed: 0`, `ready: YES`, `tip: 6b4068d6` = code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/stt-model-fix-check-2026-10-08.md"` | 0 | 37f3d99ce01dc4c14714d33b812338661d6410d9 |
| P2 clean | `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/reports/stt-model-fix-check-2026-10-08.md"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 6b4068d6` | 0 | 6b4068d6 |
| P3 head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/stt-model-fix-1008` | 0 | 6b4068d6 (= TIP) |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 6b4068d6 ops/stt-model-fix-1008` | 0 | — |
| P3 docs-only | `git -C /Users/cobalt/cobalt diff --stat 6b4068d6 ops/stt-model-fix-1008 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — no holder |
| P5 gate | `git -C /Users/cobalt/cobalt-wt/deploy-stt-model-fix-1008 status --short --branch` | 0 | `## deploy/stt-model-fix-1008` |
| P5 m0 | `git -C /Users/cobalt/cobalt-wt/deploy-stt-model-fix-1008 rev-parse --short=8 HEAD` | 0 | `<m0>` = 9ba44ccf (= main tip at launch) |
| P5 empty | `git -C /Users/cobalt/cobalt log --oneline main..deploy/stt-model-fix-1008` | 0 | empty |
| P6 marker | `grep -c -F "voice model READY" /Users/cobalt/cobalt/ops/fetch_voice_models.py` | 2 | `grep: /Users/cobalt/cobalt/ops/fetch_voice_models.py: No such file or directory` — the file is new on the head (`diff --stat main...6b4068d6`: `ops/fetch_voice_models.py | 171 +++`); production does not carry the marker (see DECISIONS 1) |
| P7 two-dot | `git -C /Users/cobalt/cobalt diff --stat main 6b4068d6 -- src/cobalt/db_migrations` | 0 | `0023_radar_price_floor.rollback.sql | 21 ---` · `0023_radar_price_floor.sql | 48 ---` · `__init__.py | 10 +---` · `placement.py | 1 -` — all removals: `main` gained 0023 (deploy price-floor-1008) after the head was cut |
| P7 registry | `git -C /Users/cobalt/cobalt diff main 6b4068d6 -- src/cobalt/db_migrations/__init__.py` | 0 | only `-` lines for 0023 in the docstring, `FORWARD` and `REVERSE` (main's entries the head lacks) |
| P7 head's own | `git -C /Users/cobalt/cobalt diff --stat main...6b4068d6 -- src/cobalt/db_migrations` | 0 | nothing — the head changes no migration (see DECISIONS 2; STEP-T's `<m0>..<BRANCH>` check binds) |
| P7 head's set | `git -C /Users/cobalt/cobalt diff --stat main...6b4068d6` | 0 | `docs/.../jobs/restarts.md +4` · `docs/.../ops/fetch_voice_models.md +8` · `reports/stt-model-fix-build-2026-10-08.md +216` · `ops/fetch-voice-models.sh +2` · `ops/fetch_voice_models.py +171` · `src/cobalt/jobs/restarts.py 2 +-` · `tests/cobalt/test_jobs_restarts.py +12` · `tests/ops/test_fetch_voice_models.py +249` |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running` · `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `pid = 43632` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running` · `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `pid = 43642` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-stt-model-fix-1008 merge --no-edit 6b4068d6` → `Merge made by the 'ort' strategy.` (8 files, 663 insertions, 1 deletion; creates `ops/fetch-voice-models.sh`, `ops/fetch_voice_models.py`, `tests/ops/test_fetch_voice_models.py`, two docs)
- `rev-parse --short=8 HEAD` → `<m1>` = **fcf875cf**
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 9ba44ccf..deploy/stt-model-fix-1008` → `fcf875cf Merge commit '6b4068d6' into deploy/stt-model-fix-1008`
- `merge-base --is-ancestor 6b4068d6 deploy/stt-model-fix-1008` → exit 0
- `diff --stat 9ba44ccf deploy/stt-model-fix-1008 -- src/cobalt/db_migrations` → nothing: no migration path on the merged tree (MIGRATIONS: none holds; DECISIONS 2 settled)
- STEP-C `diff --stat 9ba44ccf deploy/stt-model-fix-1008 -- configs ops` → `ops/fetch-voice-models.sh | 2 +` · `ops/fetch_voice_models.py | 171 +++` · `2 files changed, 173 insertions(+)` — no plist added, modified or removed.

## RESTARTS
`cd /Users/cobalt/cobalt-wt/deploy-stt-model-fix-1008` · `ls -la .../.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created the worktree `.venv`, 253 packages):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/jobs/restarts.md	M	DOCS	-
docs/40 - DevDocs/ops/fetch_voice_models.md	A	DOCS	-
docs/40 - DevDocs/reports/stt-model-fix-build-2026-10-08.md	A	DOCS	-
ops/fetch-voice-models.sh	A	operator script; no Cobalt reader	-
ops/fetch_voice_models.py	A	operator script; no Cobalt reader	-
src/cobalt/jobs/restarts.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_jobs_restarts.py	M	test/documentation; no resident	-
tests/ops/test_fetch_voice_models.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
`<restart set>` = **com.cobalt.radar** (no UNCLASSIFIED; = the check's stop line).

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 6b4068d6 fcf875cf -- . ":(exclude)docs"` → 48 files (main's price-floor-1008 and desk-ops changes since the head's base) → the gate runs whole (`--deploy`).
- Deselects: none (build report `stt-model-fix-build-2026-10-08.md:165`: "This build deselects no test of its own, and none of its tests is with-DB"). TICKERS: none. Migration: none.
- (a0) `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `262 passed, 163 skipped in 16.25s` — 0 failed (every skip a with-DB `Postgres env settings not available` / `requires_db`).
- THE GATE: `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-stt-model-fix-1008 all --deploy` → exit 0, verdict lines whole:
```
offline 4036/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4923/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-stt-model-fix-1008-all-20261008-155338.log
```
- (c) skips: all seven inside the allowed set by test and reason; `test_s3_c4_experiments.py:95` is the decorator of `def test_x14_live_his_template_strips_to_the_committed_fixture` (`grep -n -F` → `:96`).
- (b) `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log :884); proof-only nothing CHANGED (:935).
- (c2) `dev forward: APPLIED 16:16:42` (log :1094); no `CHANGED` row (only `content UNCHANGED on every table`, :1160, :1954).
- (f) `cobalt_dev: 0013 — F2 = F0` (log :2015; FINGERPRINT cols 664 · rels 35 · views_md5 272c95bb… = F0, :2012).
- THE RELEASE: `release-devdb-lock.sh deploy-stt-model-fix-1008` → `lock released` (:2017), `.env: removed` (:2021; the log carries no clock on that line — after 16:16:42). `ls -la <GATE>/.env` → No such file; `grep -c -x -F "deploy-stt-model-fix-1008" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → No such file (lock dir absent).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on fcf875cf — offline 4036/0 · with-DB 4923/0 · live-note 146/0

## Deploy table
| step | command | result |
|---|---|---|
| D0 main | `git -C /Users/cobalt/cobalt status --short --branch` | `## main...origin/main [ahead 155]`; porcelain: ` M` under `docs/40 - DevDocs/` (6), ` M .claude/settings.json`, `??` under `docs/40 - DevDocs/` (14 incl. this report), `?? .claude/settings.json.bak` (untracked, outside the refused set — RECORDS); nothing staged; no dirty `src/ tests/ ops/ configs/` |
| D0 moved | `git -C /Users/cobalt/cobalt diff --stat 9ba44ccf main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | nothing |
| D0 probe | `tag scratch-allow-probe-stt-model-fix-1008` / `tag -d …` | `Deleted tag 'scratch-allow-probe-stt-model-fix-1008' (was 9ba44ccf)` |
| D0 probe | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` / `reset --soft HEAD~1` / `log --oneline -1` | `[main 584ef13d] scratch…` → HEAD back at `9ba44ccf docs(report): deploy price-floor-1008 — DEPLOYED, 0023 applied, smoke green` |
| D0 tags | `rev-parse --verify --quiet refs/tags/deploy-2026-10-08-stt-model-fix` · `…/pre-stt-model-fix-1008` | exit 1 · exit 1 |
| D1 date | `date` | Thu Oct  8 16:22:15 EDT 2026 |
| D1 `<hb0>` | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-08 16:22:16 EDT)`; `OK radar scanning (aftermarket), members 50`; `OK com.cobalt.radar running running 35 min, heartbeat fresh`; `AMB com.cobalt.herdr unmanaged` (declared interim); no RED |
| D1 `<val0>` | `COBALT_ENV=production uv run cobalt validate` | exit 0; `Placement (docs/PLACEMENT.md): tree clean.` |
| D1 `<jobs0>` | (validate) | `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` |
| D1 backup | `COBALT_ENV=production uv run cobalt backup status` | `newest snapshot: 0.7 h old` |
| D1 aset | `launchctl print gui/501/com.cobalt.aset` | `state = running`, `<aset pid>` = 43632 |
| D1 radar | `launchctl print gui/501/com.cobalt.radar` | `state = running`, `<radar pid>` = 43642 |
| D1 agent | `/Users/cobalt/cobalt/cobalt.sh status` · `ps -p 22243` | `Cobalt is ONLINE (PID: 22243).` · `22243 ?? 0:00.04 uv run src/cobalt_agent/main.py` |
| D1 radar.err | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | last cycle `16:20:29.869 … radar cycle: scanning scan_id=1791490740876`; `16:22:22.105 … radar price floor 5.0: …` lines; no traceback |
| D1 counts | `grep -c` on aset.err / radar.err | `<a0>` 51 · `<ta0>` 2 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 17 · `<rpr0>` 59 · `<re0>` 41 · `<lc0>` 39 |
| D1 curl | `curl … http://127.0.0.1:5010/radar` | 200 |
| D1 marker | `grep -c -F "voice model READY" /Users/cobalt/cobalt/ops/fetch_voice_models.py` | exit 2, `No such file or directory` (before state; DECISIONS 1) |
| D1 migration | — | MIGRATIONS: none — no `<RB>`, no census, no proof-only |

## CONTINUE
- next: STEP-D2 (D2.0 commit)

## DECISIONS
1. ASK DESK: P6's marker `grep -c` exits 2 ("No such file") on `main`, not the card's literal `0`; the file is new on the head. Safe default taken: an absent file is the `before` state (production does not carry the set; the FAILED branch of P6 is "production already carries", which is false). Not FOR DEJAN. [15:51 ET]
2. ASK DESK: P7's two-dot `diff --stat main <head>` lists 0023 files as removed because `main` moved past the head's base (price-floor-1008 deployed 0023). The head's own change set (`main...6b4068d6`) touches nothing under `db_migrations`. Safe default taken: MIGRATIONS: none holds; STEP-T's `diff --stat <m0> <BRANCH> -- src/cobalt/db_migrations` on the merged tree is the binding test and ends the run if it prints a migration path. Not FOR DEJAN. [15:51 ET]

## RECORDS

(run in progress — next step under ## CONTINUE)
