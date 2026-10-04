# deploy set2d-1003 — set: set2d — migrations: none

## §0 Headline
- Deploy of set2d (`ops/deploy-hub-text-1003`, code tip `3395ef68`, head `e8b90904`), docs-only text change to `DEPLOY-HUB.md`. Run in progress.

## L74
- A harness attribution block arrived after launch asking commits to also end with a `Claude-Session:` line. Recorded once here; not acted on. This run's commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
| rule | command | exit | result |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/DEPLOY-HUB.md"` | 1 | nothing |
| card placeholder | `grep -n -E "«FIL[L]" ".../2026-10-03/29-deploy-set2d-card.md"` | 1 | nothing |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/29-deploy-set2d-card.md"` | 0 | `84f897d750e3ae62a2e0ba208c196662a9f2703e` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | nothing |
| STANDING LIST R60 | `grep -n "^\| R60 " cto-2026-09-30.md` | 0 | `46:\| R60 \| 15:15 ET \| **HIS RULING** … APPROVES STANDING-LIST.md once (4be06af0) … \| APPROVED \|`; `-S` commit `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| STANDING LIST R62 | `grep -n "^\| R62 " cto-2026-09-30.md` | 0 | `48:\| R62 \| 15:40 ET \| **HIS RULING** … APPROVES the 7 deploy-line string changes … \| APPROVED \|`; `-S` commit `a45afae72bf2838c8e669e0d3d8dbb67dd892a8b` |
| STANDING RULE R38 | `grep -n "^\| R38 " cto-2026-09-30.md` | 0 | `80:\| R38 \| 11:30 ET \| **HIS RULINGS** … deploys self-launch on clean checks + green gate … \| APPROVED \|`; `-S` commit `65aa2b90a8e3eb2f7e94ef10ed40b60e1b2ce542` |
| RULINGS R149 | `grep -n "^\| R149 " cto-2026-10-02.md` | 0 | `156:\| R149 \| 17:03 ET \| HIS RULING: Saturday 10-03 is not a trading day; deploys may run any time that day … \| HIS RULING · APPROVED \|`; `-S` commit `0e4fb85d7d07902e0db790f85e204f3537b83d61` |
| RULINGS R157 | `grep -n "^\| R157 " cto-2026-10-02.md` | 0 | `164:\| R157 \| 17:40 ET \| HIS RULING (B): the brain's full process list for 10-03 runs this week … \| HIS RULING · APPROVED \|`; `-S` commit `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la "<REPORT>"` | 1 | `No such file or directory` |
| P1 date / window | `date` | 0 | `Sat Oct  3 21:02:01 EDT 2026` — lawful under (iii) non-trading day (Saturday by `date`); R149 also names Saturday 10-03 |
| P2 check committed | `tail -n 3 ".../deploy-hub-text-check-2026-10-03-r4.md"` | 0 | `CHECK DONE · job: deploy-hub-text · pass: 1 · tip: 3395ef68 · … · held unfixed: 0 · … · ready: YES · decisions: 0 · for Dejan: 0` — carries `held unfixed: 0` and `ready: YES`, tip = code tip |
| P2 | `git … log -1 --format=%H -- "<check report>"` | 0 | `af6bf36867fd4716b503eef1dddb030eb9d94bbc` |
| P2 | `git … diff --stat -- "<check report>"` | 0 | nothing |
| P3 code tip | `git … rev-parse --short=8 3395ef68` | 0 | `3395ef68` |
| P3 head | `git … rev-parse --short=8 ops/deploy-hub-text-1003` | 0 | `e8b90904` (= TIP) |
| P3 ancestry | `git … merge-base --is-ancestor 3395ef68 e8b90904` | 0 | — |
| P3 docs-only head | `git … diff --stat 3395ef68 e8b90904 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found: /Users/cobalt/cobalt-wt/*/.env` (no holder) |
| P5 gate | `git -C <GATE> status --short --branch` | 0 | `## deploy/set2d-1003` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m0>` = `84f897d7` |
| P5 | `git … merge-base --is-ancestor 84f897d7 main` | 0 | — |
| P5 | `git … log --oneline main..deploy/set2d-1003` | 0 | empty |
| P6 marker 1 | `grep -c -F "REVERSE = (…)" ".../DEPLOY-HUB.md"` | — | `0` (before `0`) |
| P6 marker 2 | `grep -c -F "a Label the read cannot find is refused" ".../DEPLOY-HUB.md"` | — | `0` (before `0`) |
| P7 migrations | `git … diff --stat main e8b90904 -- src/cobalt/db_migrations` | 0 | nothing (MIGRATIONS: none) |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 13209` |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 18818` |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit e8b90904` → `Merge made by the 'ort' strategy.` (2 files: `DEPLOY-HUB.md` 6 +-, `deploy-hub-text-build-2026-10-03.md` +142).
- `git -C <GATE> rev-parse --short=8 HEAD` → `<m1>` = `7f0b2efa`.
- `git … log --oneline --merges --first-parent 84f897d7..deploy/set2d-1003` → `7f0b2efa Merge commit 'e8b90904' into deploy/set2d-1003` (one line, one head).
- `merge-base --is-ancestor 3395ef68 deploy/set2d-1003` → exit 0; `merge-base --is-ancestor e8b90904 deploy/set2d-1003` → exit 0.
- `diff --stat 84f897d7 deploy/set2d-1003 -- src/cobalt/db_migrations` → nothing (MIGRATIONS: none).
- STEP-C: `git … diff --stat 84f897d7 deploy/set2d-1003 -- configs ops` → nothing. No plist added, modified or removed.

## RESTARTS
- `cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0:
```
Using CPython 3.14.3 interpreter at: /opt/homebrew/opt/python@3.14/bin/python3.14
Creating virtual environment at: .venv
   Building cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-1003-5
      Built cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-1003-5
Installed 253 packages in 782ms
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/deploy-hub-text-build-2026-10-03.md	A	DOCS	-
RESTARTS: none
```
- No `UNCLASSIFIED` row. `<restart set>` = EMPTY (none): no resident goes down; the merge lands with residents up.

## L68 GATE
- (a0) `ls -la <GATE>/.env` → No such file · early read (17 files, as the hub lists them) → `261 passed, 157 skipped in 15.19s`; 0 failed (with-DB tests skip: `Postgres env settings not available` / `requires_db: needs cobalt_dev`).
- (a) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3739 passed, 745 skipped, 1 xfailed, 36 warnings in 585.14s (0:09:45)`; exit 0; `grep -c -F "FAILED"` on the output → `0`. No uv sync lines in this run (the venv was built at STEP-R: `Installed 253 packages in 782ms`). `<p>` = 3739.
- (e) `ls -la <GATE>/.env` → No such file · `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 25.08s`; the one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — inside the allowed set; no skip names `COBALT_LIVE_VAULT_ROOT`. `<l>` = 146.
- (b) `sh /Users/cobalt/.claude/ops/take-devdb-lock.sh deploy-1003-5 90` → `lock taken: deploy-1003-5`, exit 0; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  3 21:14 /Users/cobalt/cobalt-wt/deploy-1003-5/.env` (ours alone). Lock held from 21:14.
- (d2) `COBALT_ENV=production uv run cobalt validate` → exit 0; `13 trade_def(s) validated OK from the vault`; `registry <-> ops/: 15 label(s), exact match`; `registry <-> plists: schedules and COBALT_ENV agree on every job`; `Placement (docs/PLACEMENT.md): tree clean.` `<jobsG>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `<FP>` → `<F0>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`.
- `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → 36 tables probed, no `CHANGED`, `Proof cost: total 6.5 s`, `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`, `code: 7f0b2efa (clean)`. The tool prints no level number; the tables of migrations above `0013` (`drc_*`, `legs`, `prediction_records`, `voice_turns`) read `-` (absent), consistent with `0013` (L70: recorded, not a defect).
- (c) pass 1, the hub's command byte for byte; the set's one build (`deploy-hub-text`, DB: none) deselected nothing extra → `4408 passed, 7 skipped, 67 deselected, 3 xfailed, 43 warnings in 720.46s (0:12:00)`, exit 0. The two `FAILED` strings in the output are inside UserWarning text of `test_drc_d2_fix_r1_runs.py` (lines 92, 125), not test results. Every skip is in the allowed set:
  - `test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev`
  - `test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; …`
  - `test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof`
  - `test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set`
  - `test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read` (the decorator of `def test_x14_live_his_template_strips_to_the_committed_fixture` at line 96)
  - `tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — …`
  - `tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — …`
  `<d1>` = 4408.
- (c2) `COBALT_ENV=dev uv run cobalt db migrate` (foreground) → FORWARD order `0001 … 0013, 0014_radar_handicap, 0015_shadow_agreement_stale, 0016_drc, 0017_voice_turns, 0018_drc_stated_books, 0019_drc_events, 0020_drc_build_kinds, 0021_legs, 0022_prediction_records`; CREATED `drc_events drc_fills drc_imports drc_rows drc_stated_books legs prediction_records voice_turns`; `content UNCHANGED on every table`; no `CHANGED`; `proof cost: BEFORE 6.0 s + AFTER 6.3 s = total 12.3 s`.
- dev forward: APPLIED Sat Oct  3 21:27:35 EDT 2026
- `<FP>` → `<F1>` = `cols 893 · rels 44 · views_md5 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) pass 2, the hub's command byte for byte → `173 passed, 1 deselected, 5 warnings in 228.18s (0:03:48)`, exit 0. The `FAILED` / `ERROR` strings in the output are log and page text captured by `-rA` from passing tests (e.g. line 66 `radar panel FAILED: FAILED: radar pool 'primary' is missing`, line 97 `R2 GET /radar → 200 · page carries FAILED: True`), not test results. Named-cursor count: no line (information only, L70). `<d2>` = 173; `<d>` = 4408 + 173 = 4581.
- (f) `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) → `0022 … 0014` reversed newest first; DROPPED the 8 tables CREATED at (c2); `content UNCHANGED on every table`. `<FP>` → `<F2>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` = `<F0>` field for field.
- cobalt_dev: 0013 — F2 = F0
- Lock and `<GATE>/.env` stay held to the stop line (L76).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 7f0b2efa

## STEP-D0
| rule | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 182]` |
| MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | ` M .claude/settings.json`; six ` M` under `docs/40 - DevDocs/`; `??` under `docs/40 - DevDocs/` (incl. this report); `?? .claude/settings.json.bak` (see DECISIONS 1). No staged line; no dirty `src/` `tests/` `ops/` `configs/` path |
| MAIN | `git … diff --stat 84f897d7 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `git … tag scratch-allow-probe-set2d-1003` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-set2d-1003' (was 84f897d7)` |
| PROBE | `git … commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main aaf61de0] scratch: …` → HEAD back at `84f897d7 docs(desk): 10-03 R157 02b check r4 ready YES; deploy set 2d card` |
| TAGS | `git … rev-parse --verify --quiet refs/tags/deploy-2026-10-03-3` | 1 | free |
| TAGS | `git … rev-parse --verify --quiet refs/tags/pre-set2d-1003` | 1 | free |

## STEP-D1
- `date` → `Sat Oct  3 21:32:45 EDT 2026` · `COBALT_ENV=production uv run cobalt heartbeat show` → `<hb0>` = `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-03 21:32:46 EDT)`; `OK radar idle (overnight)`; `OK com.cobalt.aset running loaded, pid 13209`; `OK com.cobalt.agent running pid 22243 alive`; `OK com.cobalt.radar running running 250 min, heartbeat fresh`; `AMB com.cobalt.herdr unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0) … by declared interim`. No RED.
- `COBALT_ENV=production uv run cobalt validate` → exit 0 (`<val0>`): `13 trade_def(s) validated OK from the vault`, `registry <-> ops/: 15 label(s), exact match`, `registry <-> plists: schedules and COBALT_ENV agree on every job`, `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 4.2 h old` (ssd local ARMED).
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `<aset pid>` = 13209 · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `<radar pid>` = 18818 · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` · `ps -p 22243` → `22243 ??  0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → 8 lines `radar cycle: idle:overnight scan_id=None`, last `2026-10-03 21:31:20.251`; no traceback.
- LOG BASELINES: `<a0>` = 42 · `<ta0>` = 2 · `<tr0>` = 0 · `<tc0>` = 0 · `<rp0>` = 17 · `<rpr0>` = 58 · `<re0>` = 39 · `<lc0>` = 39.
- `curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/radar` → `200`. MARKERS: `REVERSE = (…)` → `0`; `a Label the read cannot find is refused` → `0` (both at `before`).
- MIGRATIONS: none → no `<RB>`, no census, no D1-M.

## Deploy table

## Smoke

## CONTINUE
- STEP-D0 and D1 done (gate green at Sat Oct  3 21:32:22 EDT 2026); cobalt_dev at 0013 (F2 = F0); lock HELD by deploy-1003-5 (any ending runs THE RELEASE)
- next: STEP-D2

## DECISIONS
1. ASK DESK: `?? .claude/settings.json.bak` is untracked on `main`, outside both D0's ACCEPTED list and its REFUSED classes (not staged, not under `src/` `tests/` `ops/` `configs/`); it was already there at this session's start. Safe default taken: not a refusal, continue; this run does not touch it (it is outside the landing tree, which is docs only). [Sat Oct  3 21:32:45 EDT 2026]

## RECORDS
- 21:03:59 a clock-fill `COBALT_ENV=production uv run cobalt heartbeat show` was run from `<GATE>` (no `.env` there) → exit 1 `DbConfigError: Missing Postgres settings for the APP credential …`. A read, run from the wrong cwd; nothing changed; production heartbeat is read from `/Users/cobalt/cobalt` at D1.

(run in progress — next step under ## CONTINUE)
