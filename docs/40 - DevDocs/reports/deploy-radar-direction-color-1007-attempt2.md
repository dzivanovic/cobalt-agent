# deploy radar-direction-color-1007 · SET: none · MIGRATIONS: none

## §0 Headline
- Deploy of `ops/radar-direction-color-1007` (`541adf0c`, his R625) on gate branch `deploy/radar-direction-color-1007-attempt2`. Started 2026-10-07 13:50:43 EDT.

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

## CONTINUE
next: STEP-D2

(run in progress — next step under ## CONTINUE)
