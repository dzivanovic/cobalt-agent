# deploy s4-p1-1009 · SET: none · MIGRATIONS: none

## §0 Headline
- Deploy of `ops/s4-p1-1009` (S4-P1 · F9) at tip `444e32b5`. In progress.

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

## Smoke

## CONTINUE
- next: STEP-D2 (gate green at 23:19:24 ET; D0, D1 done; m1 = 156e4b75, restart set = com.cobalt.aset com.cobalt.radar)

## DECISIONS

## RECORDS

(run in progress — next step under ## CONTINUE)
