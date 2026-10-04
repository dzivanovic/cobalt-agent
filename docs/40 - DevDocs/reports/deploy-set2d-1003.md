# deploy set2d-1003 — set: set2d — migrations: none

## §0 Headline
- DEPLOYED set2d: `ops/deploy-hub-text-1003` (code tip `3395ef68`, head `e8b90904`), a docs-only text change to `DEPLOY-HUB.md`. `main` `ffd0b1be` → `a8d8a848`, tagged `deploy-2026-10-03-3`; rollback tag `pre-set2d-1003`.
- Gate GREEN on `7f0b2efa`: offline 3739/0 · with-DB 4581/0 (4408 + 173) · live-note 146/0. `cobalt_dev` back at 0013 (F2 = F0).
- RESTARTS: none. No resident went down; aset, radar and agent kept their PIDs (13209, 18818, 22243). Smoke GREEN.
- Decisions: 1 (an untracked `.claude/settings.json.bak` on `main`, outside D0's lists; default: continue). For Dejan: 0. Push is his (L55).

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
- D2.0 `git … add` + `commit -m "docs(report): deploy set2d-1003 — gate green on 7f0b2efa"` → `[main ffd0b1be]`, `show --stat HEAD` lists the one report file (133 +). `<pre-merge>` = `ffd0b1be`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report file only).
- D2.2 `<stack-final>` = `a8d8a848`; `a8d8a848^2` = `ffd0b1be` = `<pre-merge>`; `merge-base --is-ancestor 7f0b2efa a8d8a848` → exit 0.
- D2.3 `git … diff --stat 7f0b2efa a8d8a848 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing: the tree that lands is the gate's tree plus docs.
- D2.4 `backup status` → `newest snapshot: 4.2 h old` · `COBALT_ENV=production uv run cobalt backup run` → `backup: cobalt_brain dumped, 4460.3 MB`; `ssd: snapshot 77a98aed — 0 new / 1 changed, 11.2 MB added, 1 pruned`; `F17: com.cobalt.backup DONE` · `backup status` → `newest snapshot: 0.0 h old`. Snapshot id `77a98aed`.
- D2.5 `date` → `Sat Oct  3 21:34:35 EDT 2026` · `heartbeat show` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-03 21:34:36 EDT)` (110 s after D1's 21:32:46); `com.cobalt.radar running … heartbeat fresh`; no new RED. (Intervening clock-fill reads at 21:34:20, :24, :29, :32: all `HEARTBEAT GREEN … nothing red`.)
- D2.6 `date` → `Sat Oct  3 21:34:41 EDT 2026`: Saturday, still inside P1's (iii). `git … rev-parse --short=8 HEAD` → `ffd0b1be`; `git -C /Users/cobalt/cobalt tag pre-set2d-1003` → exit 0 (at `<pre-merge>` `ffd0b1be`).
- 4.1 `date` → `<t down>` = `Sat Oct  3 21:34:55 EDT 2026` (restart set EMPTY: nothing goes down).
- 4.2 nothing booted out, agent not stopped (restart set EMPTY).
- 4.3 `git … rev-parse --short=8 HEAD` → `ffd0b1be` = `<pre-merge>` · `git -C /Users/cobalt/cobalt merge --ff-only deploy/set2d-1003` → `Updating ffd0b1be..a8d8a848` / `Fast-forward` (`DEPLOY-HUB.md` 6 +-, `deploy-hub-text-build-2026-10-03.md` +142).
- 4.4 migrations applied: none.
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0; `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>`; `registry <-> ops/: 15 label(s), exact match`; `Placement (docs/PLACEMENT.md): tree clean.`
- 4.6 nothing to bootstrap (restart set EMPTY). `<t up>` = 4.3's `date` = `Sat Oct  3 21:34:55 EDT 2026`. Downtime: none.

| field | value |
|---|---|
| `<pre-merge>` → `<stack-final>` | `ffd0b1be` → `a8d8a848` (main tip `a8d8a848`) |
| tags | `pre-set2d-1003` at `ffd0b1be` (rollback) · `deploy-2026-10-03-3` at `a8d8a848` (set after the green smoke) |
| `<t down>` / `<t up>` / seconds | none (restart set EMPTY; 4.1 / 4.3 `date` `21:34:55`) |
| uv sync line | STEP-R in `<GATE>`: `Installed 253 packages in 782ms` (new gate venv); none in production calls |
| proof cost | none for production (no migration); dev forward `total 12.3 s`, dev rollback `total 12.6 s` |
| migrations applied | none |
| `<RB>` before / after | n/a (no migration) |
| snapshot id | `77a98aed` (ssd, `cobalt_brain` dump 4460.3 MB) |
| RESTARTS done | none |
| ROLLBACK STRING | 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 a8d8a848` (one revert of the main-into-gate merge; the restart set is empty, so no resident goes down or up). 2. SCHEMA: none (no migration). 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`. |

## Smoke
`<t up>` = `Sat Oct  3 21:34:55 EDT 2026` (4.3's `date`; restart set EMPTY).
- FIRST CALLS: `<rp_up>` = 17 · `<rpr_up>` = 58 · `<re_up>` = 39 · `<lc_up>` = 39 (= D1's).
- (a) `date` → `Sat Oct  3 21:35:10 EDT 2026` · `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 13209` (SAME as D1: outside the set) · `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 18818` (SAME) · `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` (SAME). GREEN.
- (b) `date` → `Sat Oct  3 21:35:14 EDT 2026` · `grep -c "Started server process" aset.err` → `42` = `<a0>` (aset outside the set) · `tail -n 30 aset.err` → last start `INFO:     Started server process [13215]` … `INFO:     Uvicorn running on http://0.0.0.0:5010 (Press CTRL+C to quit)` (the 2026-10-02 17:47 start; no new start) · Traceback aset `2` = `<ta0>` · Traceback radar `0` = `<tr0>` · TaxonomyConfigError `0` = `<tc0>`.
- (c) `date` → `Sat Oct  3 21:35:19 EDT 2026` · `curl … http://127.0.0.1:5010/` → `200` · `…/radar` → `200` · `…/radar\?frame=phone` → `200`. GREEN.
- (d) MARKERS: `grep -c -F "REVERSE = (…)" …/DEPLOY-HUB.md` → `2` (after `2`) · `grep -c -F "a Label the read cannot find is refused" …/DEPLOY-HUB.md` → `1` (after `1`). GREEN.
- (s) `ls "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` → exit 0, `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md` listed. GREEN.
- (f) `date` → `Sat Oct  3 21:35:25 EDT 2026` · `COBALT_ENV=production uv run cobalt jobs restarts ffd0b1be..a8d8a848` → exit 0; 2 `DOCS` rows; `RESTARTS: none` = STEP-R's set; no `UNCLASSIFIED` · `validate` → exit 0, `Jobs (F17): 15 registered — 6 resident, 9 one-shot.`, `registry <-> plists: schedules and COBALT_ENV agree on every job`, `Placement … tree clean.` GREEN.
- (e) read 1: `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-03 21:35:29 EDT)`; `com.cobalt.radar running running 253 min, heartbeat fresh`.
- (g) no migration.
- (b) radar tail 1: `date` → `Sat Oct  3 21:36:26 EDT 2026` (`<t up>` + 91 s) · `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` → last line `2026-10-03 21:36:20.328 | INFO | cobalt.radar.runner:resident:467 - radar cycle: idle:overnight scan_id=None`, a cycle line after `<t up>`; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback in the 12 lines. (b) SETTLED GREEN on the first tail.
- Clock-fill reads between (e)'s two reads, 21:35:47 → 21:37:19, and after read 2, 21:37:33 → 21:37:51: every one `HEARTBEAT GREEN … nothing red`.
- (e) read 2: `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-03 21:37:24 EDT)` (115 s after read 1); `com.cobalt.radar running running 254 min, heartbeat fresh`; no RED not in `<hb0>` (none in `<hb0>` either). GREEN.
- (h) REVERT-READBACK: `date` → `Sat Oct  3 21:37:56 EDT 2026` (`<t up>` + 181 s, after (b) settled) · `radar panel FAILED` → `17` · `radar pool refresh FAILED` → `58` · `radar S5 evaluate FAILED` → `39` · `lifecycle card read failed` → `39` = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (no growth) · `curl … /radar` → `200`. No census reads on the card. GREEN.
- SMOKE: GREEN. No row red; STEP-5 not entered.

THE CHAIN: every check committed (P2: `deploy-hub-text-check-2026-10-03-r4.md` at `af6bf368…`, `held unfixed: 0`, `ready: YES`, tip `3395ef68`) → the tips re-read (P3: `3395ef68`, `e8b90904`) → the merged tree (T: `<m1>` `7f0b2efa`, one first-parent merge) → RESTARTS derived by the tool (R: `none`, two `DOCS` rows) → three suites green on `<m1>` (G: offline 3739/0, with-DB 4408 + 173 / 0, live-note 146/0; `cobalt_dev` F2 = F0) → `<stack-final>` `a8d8a848` = `<m1>` + docs (D2.3: nothing outside docs) → the landed code (4.3: `Fast-forward ffd0b1be..a8d8a848`) → markers at `after` (d: 2, 1) → no migration (g) → residents up and unchanged after the merge (a: same PIDs) → radar cycling (b: 21:36:20 cycle line; e: two green reads) → the set's read (s: `DEPLOY-HUB.md` listed) → no new failure (h: four counts flat). The card surface is not readable here; the desk confirms it with him (L70).

## CONTINUE
- STEP-D0 and D1 done (gate green at Sat Oct  3 21:32:22 EDT 2026); cobalt_dev at 0013 (F2 = F0); lock HELD by deploy-1003-5 (any ending runs THE RELEASE)
- STEP-D2 done: `<pre-merge>` ffd0b1be, `<stack-final>` a8d8a848, snapshot 77a98aed, tag `pre-set2d-1003`.
- OUTAGE STARTING Sat Oct  3 21:34:41 EDT 2026 — residents of <restart set> (EMPTY: none) going down; no resident goes down for this set; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
- STEP-4 done (merged `a8d8a848`, nothing went down); smoke GREEN at 21:37:56; tag `deploy-2026-10-03-3` set.
- next: none (the run is at its stop line).

## PRE-STOP SELF-CHECK (K25)
1. Every smoke row's evidence is quoted verbatim with its `date` (`## Smoke`: (a) 21:35:10, (b) 21:35:14 and 21:36:26, (c) 21:35:19, (f) 21:35:25, (e) 21:35:29 and 21:37:24, (h) 21:37:56; (d) and (s) run after (c)'s `date`).
2. Every code tip and head was re-read (P3: `3395ef68`, `e8b90904`) and is an ancestor of `<stack-final>`: `merge-base --is-ancestor 3395ef68 a8d8a848` → exit 0; `merge-base --is-ancestor e8b90904 a8d8a848` → exit 0.
3. REVERT-READBACK is shown at (h): the four counts 17 / 58 / 39 / 39 equal `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>`. Every count, sha and `file:line` here was read from tool output this run (main tip `rev-parse --short=8 HEAD` → `a8d8a848` just before the tag).
4. No conflict marker: STEP-T ran clean (`Merge made by the 'ort' strategy.`), D2.1 ran clean; `grep -c -E "^(<<<<<<<|>>>>>>>)" …/DEPLOY-HUB.md` → `0`.

## DECISIONS
1. ASK DESK: `?? .claude/settings.json.bak` is untracked on `main`, outside both D0's ACCEPTED list and its REFUSED classes (not staged, not under `src/` `tests/` `ops/` `configs/`); it was already there at this session's start. Safe default taken: not a refusal, continue; this run does not touch it (it is outside the landing tree, which is docs only). [Sat Oct  3 21:32:45 EDT 2026]

## RECORDS
- 21:03:59 a clock-fill `COBALT_ENV=production uv run cobalt heartbeat show` was run from `<GATE>` (no `.env` there) → exit 1 `DbConfigError: Missing Postgres settings for the APP credential …`. A read, run from the wrong cwd; nothing changed; production heartbeat is read from `/Users/cobalt/cobalt` at D1.
- Downtime: none (restart set EMPTY; no resident went down).
- REFUSED, not needed: none. No `CONTINUE` message and no message from another session arrived.
- cobalt_dev: 0013 (F2 = F0) — `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` at F0 and F2.
- RETIRE OWED: none (STEP-C: no plist added, modified or removed).
- Carried RED: none. `<hb0>` and every later heartbeat read `HEARTBEAT GREEN … nothing red`; the only non-OK row is `AMB com.cobalt.herdr … launchd unmanaged … by declared interim`, unchanged throughout.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-1003-5` and branch `deploy/set2d-1003`; the set's branch `ops/deploy-hub-text-1003` and its worktree, if one exists.
- THE RELEASE: `sh /Users/cobalt/.claude/ops/release-devdb-lock.sh deploy-1003-5` → `lock released`; `ls -la <GATE>/.env` → No such file. .env: removed (L76 lock released Sat Oct  3 21:38:52 EDT 2026).
- The tags `pre-set2d-1003` and `deploy-2026-10-03-3` and the `main` commits are local; push is his, through the desk (L55).
- The D0 allowlist probe made and undid the empty commit `aaf61de0` (`reset --soft HEAD~1`); HEAD returned to `84f897d7`.
- L74: one harness attribution block (`Claude-Session:` line) arrived; recorded under `## L74`; not acted on.
- Card `## RECORDS` (the desk's facts, copied):
  - deploy-hub-text: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-hub-text-check-2026-10-03-r4.md` last line: CHECK DONE · job: deploy-hub-text · pass: 1 · tip: 3395ef68 · house A: none (overruled 2026-10-02 R47) · findings: 9 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: not taken (DB: none) · .env: removed · RESTARTS: none · files opened: 9 · ready: YES · decisions: 0 · for Dejan: 0
  - deploy-hub-text: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/deploy-hub-text-1003` → `e8b90904`; code tip `3395ef68`
  - written by deploy-card.sh at 2026-10-03 21:01 ET (`date`); trial merge of the heads onto main in order: clean

DEPLOYED deploy-2026-10-03-3 a8d8a848 | set: set2d | migrations: none | gate: offline 3739/0 · with-DB 4581/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 1 · for Dejan: 0
