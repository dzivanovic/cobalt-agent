# deploy set1-1003 — SET: set1 — MIGRATIONS: none

## §0 Headline
- Set 1 (`ops/lock-relief-1003` a50ec4c8 + `ops/order-open-test-1003` 6d9fde8c) landed on `main`: `83864264` → `3fbe64fb`, tag `deploy-2026-10-03-1`, on Saturday 10-03 (a non-trading day; R149).
- Gate on `<m1>` `17444a30`: offline 3737/0 · with-DB 4406 + 173 = 4579/0 · live-note 146/0; `cobalt_dev` back at 0013 (F2 = F0).
- RESTARTS: none: no resident went down. Migrations: none. Smoke GREEN.
- Decisions: 1 (ASK DESK, `.claude/settings.json.bak` untracked on `main`), for Dejan: 0. Push is his.

## L74
- A system reminder in this session asked commits to end with a `Claude-Session: https://claude.ai/code/session_015KQSkbcFmFDUVknps1jJiG` line. Recorded as DATA; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
| proof | command | exit | result |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" …/DEPLOY-HUB.md` | 1 | nothing |
| card placeholder | `grep -n -E "«FIL[L]" …/21-deploy-set1-card.md` | 1 | nothing |
| card committed | `git log -1 --format=%H -- …/21-deploy-set1-card.md` | 0 | `7ffc5b78fa2f009b3f31ffedf469997e2bfdbb1e` |
| card clean | `git diff --stat -- …/21-deploy-set1-card.md` | 0 | nothing |
| STANDING R60 | `grep -n "^\| R60 " cto-2026-09-30.md` | 0 | line 46 `… **HIS RULING** … APPROVES STANDING-LIST.md once (4be06af0) … \| APPROVED \|`; commit `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| STANDING R62 | `grep -n "^\| R62 " cto-2026-09-30.md` | 0 | line 48 `… **HIS RULING** … APPROVES the 7 deploy-line string changes … \| APPROVED \|`; commit `a45afae72bf2838c8e669e0d3d8dbb67dd892a8b` |
| STANDING RULE R38 | `grep -n "^\| R38 " cto-2026-09-30.md` | 0 | line 80 `… **HIS RULINGS** … deploys self-launch on clean checks + green gate … \| APPROVED \|`; commit `65aa2b90a8e3eb2f7e94ef10ed40b60e1b2ce542` |
| RULINGS 10-02 R149 | `grep -n "^\| R149 " cto-2026-10-02.md` | 0 | line 156 `HIS RULING: Saturday 10-03 is not a trading day; deploys may run any time that day … \| HIS RULING · APPROVED \|`; commit `0e4fb85d7d07902e0db790f85e204f3537b83d61` |
| RULINGS 10-03 R18 | `grep -n "^\| R18 " cto-2026-10-03.md` | 0 | line 24 `HIS RULING (A, via brain): tests/ops/ stays in the DB: none no-lock class … \| HIS RULING · APPROVED \|`; commit `f64e257a4eef00ebb1cf1ed87243e22477af7946` |
| RULINGS 10-03 R29 | `grep -n "^\| R29 " cto-2026-10-03.md` | 0 | line 35 `HIS RULING: deploy set 1 — card prompts/2026-10-03/21-deploy-set1-card.md, TIP a50ec4c8 6d9fde8c … \| HIS RULING · APPROVED \|`; commit `7ffc5b78fa2f009b3f31ffedf469997e2bfdbb1e` |

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la …/reports/deploy-set1-1003.md` | 1 | No such file or directory |
| P1 | `date` | 0 | `Sat Oct  3 10:49:35 EDT 2026` — (iii) a non-trading day (Saturday); also R149 |
| P2 lock-relief | `tail -n 3 …/lock-relief-check-2026-10-03.md` | 0 | `CHECK DONE · job: lock-relief · pass: 1 · tip: a50ec4c8 · … · held unfixed: 0 · open: 0 · … · ready: YES · decisions: 2 · for Dejan: 0`; committed `8778b86beda15b06bf059390831af58110bec6be`; diff nothing |
| P2 order-open-test | `tail -n 3 …/order-open-test-check-2026-10-03.md` | 0 | `CHECK DONE · job: order-open-test · pass: 1 · tip: 4b4b9f4a · … · held unfixed: 0 · open: 0 · … · ready: YES · decisions: 0 · for Dejan: 0`; committed `8778b86beda15b06bf059390831af58110bec6be`; diff nothing |
| P3 lock-relief | `rev-parse --short=8 a50ec4c8` / `ops/lock-relief-1003` | 0 | `a50ec4c8` / `a50ec4c8`; is-ancestor exit 0; diff outside docs nothing |
| P3 order-open-test | `rev-parse --short=8 4b4b9f4a` / `ops/order-open-test-1003` | 0 | `4b4b9f4a` / `6d9fde8c`; is-ancestor 4b4b9f4a 6d9fde8c exit 0; diff outside docs nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/set1-1003` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m0>` = `7ffc5b78`; is-ancestor of main exit 0; `log --oneline main..deploy/set1-1003` empty |
| P6 | `grep -c -F -e "--db-only" tests/cobalt/conftest.py` | 1 | `0` (before 0) |
| P6 | `grep -c -F "DB: none" …/BUILD-HUB.md` | 1 | `0` (before 0) |
| P6 | `ls tests/cobalt/test_db_only_selection.py` | 1 | `No such file or directory` (before) |
| P6 | `grep -c -F "house-probe.sh" tests/ops/test_order_open.py` | 0 | `1` (before 1) |
| P7 | `diff --stat main a50ec4c8 -- src/cobalt/db_migrations` · `main 6d9fde8c` | 0 | nothing · nothing (MIGRATIONS: none) |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, pid 13209 |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, pid 13225 |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
| check | command | exit | result |
|---|---|---|---|
| merge head 1 | `git -C <GATE> merge --no-edit a50ec4c8` | 0 | `Merge made by the 'ort' strategy.` 19 files changed, 1170 insertions(+), 10 deletions(-) |
| merge head 2 | `git -C <GATE> merge --no-edit 6d9fde8c` | 0 | `Merge made by the 'ort' strategy.` 2 files changed, 259 insertions(+), 13 deletions(-) |
| `<m1>` | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `17444a30` |
| merges | `log --oneline --merges --first-parent 7ffc5b78..deploy/set1-1003` | 0 | `17444a30 Merge commit '6d9fde8c' into deploy/set1-1003` · `4484c507 Merge commit 'a50ec4c8' into deploy/set1-1003` |
| ancestry | `merge-base --is-ancestor <a50ec4c8 / 4b4b9f4a / 6d9fde8c> deploy/set1-1003` | 0 · 0 · 0 | all in the gate |
| migrations | `diff --stat 7ffc5b78 deploy/set1-1003 -- src/cobalt/db_migrations` | 0 | nothing (none) |
| STEP-C | `diff --stat 7ffc5b78 deploy/set1-1003 -- configs ops` | 0 | nothing — no plist added, modified or removed |

## RESTARTS
`COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` in `<GATE>` (`.env`: No such file), exit 0. uv: `Creating virtual environment at: .venv` · `Installed 253 packages in 969ms`.
```
path	change	rule	restart
docs/40 - DevDocs/prompts/BUILD-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/CARD.md	M	DOCS	-
docs/40 - DevDocs/prompts/CHECK-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/lock-relief-build-2026-10-03.md	A	DOCS	-
docs/40 - DevDocs/reports/order-open-test-build-2026-10-03.md	A	DOCS	-
tests/cobalt/conftest.py	M	test/documentation; no resident	-
tests/cobalt/test_aset_web.py	M	test/documentation; no resident	-
tests/cobalt/test_db_only_selection.py	A	test/documentation; no resident	-
tests/cobalt/test_drc_d3_fix_r2.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_d4_fix_r1_runs.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_settings.py	M	test/documentation; no resident	-
tests/cobalt/test_fill_c1_offline.py	M	test/documentation; no resident	-
tests/cobalt/test_modelaccess_client.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
tests/cobalt/test_s3_c3_panel_offline.py	M	test/documentation; no resident	-
tests/cobalt/test_s3_c4_trade_note_offline.py	M	test/documentation; no resident	-
tests/cobalt/test_settings_optional.py	M	test/documentation; no resident	-
tests/cobalt/test_voice_plan.py	M	test/documentation; no resident	-
tests/cobalt/test_voice_web.py	M	test/documentation; no resident	-
tests/ops/test_order_open.py	M	test/documentation; no resident	-
tests/ops/test_pass1_db_only.py	A	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row. `<restart set>` = EMPTY (none). MIGRATIONS none, so an empty set is lawful: no resident goes down; the merge lands with the residents up.

## L68 GATE
| leg | command | result |
|---|---|---|
| (a0) early read | `uv run pytest -q -rs -p no:cacheprovider <17 files>` (`.env`: No such file) | `259 passed, 157 skipped in 14.73s` — 0 failed; every skip `Postgres env settings not available` / `requires_db: needs cobalt_dev` |
| (a) offline | `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (`.env`: No such file; background) | `3737 passed, 745 skipped, 1 xfailed, 36 warnings in 578.67s (0:09:38)` — 0 failed, 0 errors; no uv sync line → `<p>` = 3737 |
| (e) live-note | `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest … test_radar_evaluate.py test_replay_line.py test_catalyst.py test_predicate.py` (`.env`: No such file) | `146 passed, 1 skipped, 15 warnings in 24.96s`; the one skip `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — inside the allowed set; none names `COBALT_LIVE_VAULT_ROOT` → `<l>` = 146 |
| (b) lock | `sh /Users/cobalt/.claude/ops/take-devdb-lock.sh deploy-1003-1 90` (background) | `lock taken: deploy-1003-1`, exit 0; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  3 11:02 /Users/cobalt/cobalt-wt/deploy-1003-1/.env` — ours alone |
| (d2) validate | `COBALT_ENV=production uv run cobalt validate` | exit 0; `<jobsG>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot.`; `registry <-> ops/: 15 label(s), exact match.`; `registry <-> plists: schedules and COBALT_ENV agree on every job.`; `Placement (docs/PLACEMENT.md): tree clean.` |
| `<F0>` | `<FP>` | `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` |
| proof-only | `COBALT_ENV=dev uv run cobalt db migrate --proof-only` | `36 table(s) probed on cobalt_dev`; no `CHANGED`; the tables of migrations above 0013 (`drc_*`, `legs`, `prediction_records`, `voice_turns`) show `-` (absent); `Proof cost: total 5.6 s`; `NOTHING WAS APPLIED`; `code: 17444a30 (clean)`. The tool prints no level string; level 0013 is read from the absent tables and confirmed by (c2)'s applied list |
| (c) pass 1 at 0013 | the hub's pass-1 command byte for byte, no added deselect (background) | `4406 passed, 7 skipped, 67 deselected, 3 xfailed, 43 warnings in 706.60s (0:11:46)`; 0 failed, 0 errors (`grep -c -F "FAILED "` → 0). The 7 SKIPPED, each inside the allowed set: `test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev` · `test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged` · `test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof` · `test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` · `test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read` (line 95 = `@requires_live` on `test_x14_live_his_template_strips_to_the_committed_fixture`, line 96) · `test_catalyst.py:365: … the live catalyst review draft` · `test_predicate.py:262: … the live-note grammar proof` → `<d1>` = 4406 |
| (c2) forward | `COBALT_ENV=dev uv run cobalt db migrate` (foreground) | `-- applying` 0001 … 0013, then `0014_radar_handicap.sql` … `0022_prediction_records.sql` in FORWARD order; CREATED `drc_events`, `drc_fills`, `drc_imports`, `drc_rows`, `drc_stated_books`, `legs`, `prediction_records`, `voice_turns`; every other table `OK`; `content UNCHANGED on every table.`; no `CHANGED`; `proof cost: BEFORE 5.6 s + AFTER 5.5 s = total 11.1 s`. **dev forward: APPLIED Sat Oct  3 11:15:36 EDT 2026** |
| `<F1>` | `<FP>` | `cols 893 · rels 44 · views_md5 126f2d6983fa59f9d0eaaff7da7dd29c` |
| (c3) pass 2 | the hub's pass-2 command byte for byte, nothing added (background) | `173 passed, 1 deselected, 5 warnings in 219.45s (0:03:39)`; 0 failed, 0 errors; `grep -c -F "SKIPPED"` → 0 → `<d2>` = 173; `<d>` = 4406 + 173 = 4579 |
| (f) rollback | `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) | `0022` … `0014` `.rollback.sql`, newest first; the 8 created tables DROPPED; every other table `OK`; `content UNCHANGED on every table.` |
| `<F2>` | `<FP>` | `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` = `<F0>` field for field → **cobalt_dev: 0013 — F2 = F0** |
| build deselects | `grep -n -F "deselect"` over both build reports | neither build added a `--deselect` to its pass 1 (lock-relief line 218: "no deselect added"; order-open-test line 135: "no `--deselect` added") |

Back: `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` listed. The lock and `<GATE>/.env` stay held to the stop line (L76).

GATE GREEN on 17444a30

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| main | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 34]` |
| main porcelain | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | no staged line; ` M .claude/settings.json`; ` M` / `??` under `docs/40 - DevDocs/` only; plus `?? .claude/settings.json.bak` (see `## DECISIONS` 1) |
| main moved | `git diff --stat 7ffc5b78 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| probe | `tag scratch-allow-probe-set1-1003` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-set1-1003' (was 7ffc5b78)` |
| probe | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main b62666d9] scratch: …` · — · `7ffc5b78 docs(desk): 10-03 R29 his word, deploy set 1; card 21 RULINGS` (HEAD back) |
| tags | `rev-parse --verify --quiet refs/tags/deploy-2026-10-03-1` · `refs/tags/pre-set1-1003` | 1 · 1 | both free |

### STEP-D1 (baseline)
| read | command | result |
|---|---|---|
| `<hb0>` | `date` · `COBALT_ENV=production uv run cobalt heartbeat show` | `Sat Oct  3 11:20:41 EDT 2026` · `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-03 11:20:43 EDT)`; `OK radar idle (overnight)`; `OK com.cobalt.aset running loaded, pid 13209`; `OK com.cobalt.agent running pid 22243 alive`; `OK com.cobalt.radar running running 1053 min, heartbeat fresh`; `AMB com.cobalt.herdr unmanaged AMBER … declared interim`. No RED |
| `<val0>` | `COBALT_ENV=production uv run cobalt validate` | exit 0; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot.`; `registry <-> plists: schedules and COBALT_ENV agree on every job.`; `literal guard: ACTIVE — 20 vault value(s)`; `Placement (docs/PLACEMENT.md): tree clean.` |
| backup | `COBALT_ENV=production uv run cobalt backup status` | `ssd local ARMED /Volumes/COBALT-BACKUP/restic` · `newest snapshot: 13.7 h old` |
| residents | `launchctl print` aset · radar · `cobalt.sh status` · `ps -p 22243` | `state = running` pid 13209 · `state = running` pid 13225 · `Cobalt is ONLINE (PID: 22243).` · `22243 ?? 0:00.04 uv run src/cobalt_agent/main.py` |
| radar.err | `tail -n 8 logs/radar.err` | last `2026-10-03 11:20:18.975 \| INFO \| cobalt.radar.runner:resident:467 - radar cycle: idle:overnight scan_id=None`, every 100 s, no traceback |
| log baselines | `grep -c` | `<a0>` 42 · `<ta0>` 2 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 17 · `<rpr0>` 58 · `<re0>` 39 · `<lc0>` 39 |
| /radar | `curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/radar` | `200` |
| markers | the four `## MARKERS` | `0` · `0` · `No such file or directory` · `1` — each its `before` |
| migration | — | MIGRATIONS: none — no `<RB>`, no census, no D1-M |

### STEP-D2
| step | command | result |
|---|---|---|
| D2.0 | `add` · `commit -m "docs(report): deploy set1-1003 — gate green on 17444a30" …` · `show --stat HEAD` | `[main 83864264]`; one file `docs/40 - DevDocs/reports/deploy-set1-1003.md \| 142 +`; `<pre-merge>` = `83864264` |
| D2.1 | `git -C <GATE> merge --no-edit main` | `Merge made by the 'ort' strategy.` (the report alone) |
| D2.2 | `rev-parse --short=8 HEAD` · `3fbe64fb^2` · `is-ancestor 17444a30 3fbe64fb` | `<stack-final>` = `3fbe64fb` · `83864264` = `<pre-merge>` · exit 0 |
| D2.3 | `diff --stat 17444a30 3fbe64fb -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | nothing — docs only |
| D2.4 | `backup status` · `backup run` · `backup status` | `newest snapshot: 13.7 h old` · `backup: cobalt_brain … 4460.2 MB` · `ssd: snapshot 2222f0ed — 0 new / 4 changed, 11.4 MB added, 0 pruned` · `newest snapshot: 0.0 h old` |
| D2.5 | `date` · `heartbeat show` | `Sat Oct  3 11:23:40 EDT 2026` (179 s after D1's read) · `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-03 11:23:42 EDT)`; no new RED |
| D2.6 | `date` · `tag pre-set1-1003` | `Sat Oct  3 11:23:49 EDT 2026` — window (iii) Saturday, non-trading, holds · tag set at `83864264` |

### STEP-4 (restart set EMPTY)
| step | command | result |
|---|---|---|
| 4.1 | `date` | `<t down>` = `Sat Oct  3 11:24:02 EDT 2026` (nothing goes down) |
| 4.2 | — | no label in the set: no bootout, no stop |
| 4.3 | `rev-parse --short=8 HEAD` · `merge --ff-only deploy/set1-1003` | `83864264` = `<pre-merge>` · `Updating 83864264..3fbe64fb` / `Fast-forward`, 21 files changed, 1429 insertions(+), 23 deletions(-) |
| 4.4 | — | `migrations applied: none` |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | exit 0; `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>`; `Placement (docs/PLACEMENT.md): tree clean.` |
| 4.6 | — | nothing to restore; `<t up>` = 4.3's `date` = `Sat Oct  3 11:24:02 EDT 2026`; downtime: none |

### STEP-7 — close
| item | value |
|---|---|
| landed | `<pre-merge>` `83864264` → `<stack-final>` `3fbe64fb` (fast-forward); `main` = `3fbe64fb` |
| tags | `pre-set1-1003` at `83864264` · `deploy-2026-10-03-1` at `3fbe64fb` (after the green smoke) |
| outage | `<t down>` / `<t up>` / seconds: none (restart set EMPTY; no resident went down) |
| uv sync | `Creating virtual environment at: .venv` · `Installed 253 packages in 969ms` (gate `.venv`, STEP-R); none in production |
| proof cost | none in production (no migration); dev forward `total 11.1 s` |
| migrations applied | none; `<RB>` before / after: not applicable |
| snapshot | `ssd: snapshot 2222f0ed` (D2.4, 4460.2 MB dump) |
| RESTARTS done | none |
| ROLLBACK STRING (the desk's) | 1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 3fbe64fb` — ONE revert of the main-into-gate merge; the restart set is empty, so no resident goes down or up. 2. SCHEMA: none (no migration). 3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>` — git titles it `Reapply "Merge branch 'main' into deploy/set1-1003"` |
| lock | THE RELEASE: `sh /Users/cobalt/.claude/ops/release-devdb-lock.sh deploy-1003-1` → `lock released`; `ls -la <GATE>/.env` → No such file. `.env: removed (L76 lock released Sat Oct  3 11:27:28 EDT 2026)` |

**PRE-STOP SELF-CHECK (K25)**
1. Every smoke row's evidence is quoted verbatim with its `date` (`## Smoke`: 11:24:19, 11:24:23, 11:24:38, 11:25:33, 11:26:29, 11:27:03).
2. Every code tip and head re-read at P3 (`a50ec4c8`, `4b4b9f4a`, `6d9fde8c`) and each is an ancestor of `<stack-final>`: `merge-base --is-ancestor <tip> 3fbe64fb` → exit 0 · 0 · 0.
3. REVERT-READBACK shown on green: (h) four counts `17 · 58 · 39 · 39` = the first calls after `<t up>`. Every count, sha and `file:line` above was read from tool output this run.
4. No conflict marker: STEP-T ran clean (`Merge made by the 'ort' strategy.` twice, D2.1 once); `grep -c -F "<<<<<<<" tests/cobalt/conftest.py` → `0`.

## Smoke
`<t up>` = `Sat Oct  3 11:24:02 EDT 2026` (4.3's `date`; empty set). First calls: `<rp_up>` 17 · `<rpr_up>` 58 · `<re_up>` 39 · `<lc_up>` 39.

| row | `date` | command | result |
|---|---|---|---|
| (a) | 11:24:19 | `launchctl print` aset · radar · `cobalt.sh status` | `state = running` pid 13209 (= D1, outside the set) · `state = running` pid 13225 (= D1) · `Cobalt is ONLINE (PID: 22243).` (= D1) — GREEN |
| (b) | 11:24:23 | `grep -c "Started server process" aset.err` · Traceback aset · Traceback radar · TaxonomyConfigError | `42` = `<a0>` (aset outside the set) · `2` = `<ta0>` · `0` = `<tr0>` · `0` = `<tc0>`; `tail -n 30 aset.err` ends `INFO: Started server process [13215]` … `INFO: Uvicorn running on http://0.0.0.0:5010 (Press CTRL+C to quit)` (the 10-02 17:47 start, unchanged) |
| (c) | 11:24:23+ | `curl … /` · `/radar` · `/radar\?frame=phone` | `200` · `200` · `200` — GREEN |
| (d) | 11:24:23+ | the four `## MARKERS` | `5` · `5` · `/Users/cobalt/cobalt/tests/cobalt/test_db_only_selection.py` listed · `3` — each its `after` — GREEN |
| (s) | 11:24:38− | `ls tests/ops/test_pass1_db_only.py` · `grep -c -F "not probed" tests/ops/test_order_open.py` | exit 0 listed · exit 0 `2` (1 or more) — GREEN. Both files sit under `tests/ops/`, which none of the gate's three suites names (`tests/cobalt tests/taxonomy` and the live-note files); the gate did not run them, and no test runs in production. Their runs are the build and check reports' (R18: `tests/ops/` is the `DB: none` class) — not re-proven here (L70) |
| (b) tails | 11:25:33 · 11:27:03 | `tail -n 12 logs/radar.err` at `<t up>` + 91 s and + 181 s | `2026-10-03 11:25:19.067 \| INFO \| cobalt.radar.runner:resident:467 - radar cycle: idle:overnight scan_id=None` (after `<t up>`), then `… 11:26:59.086 … radar cycle: idle:overnight scan_id=None`; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback — settled GREEN at the first tail |
| (e) 2 | 11:26:29 | `heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-03 11:26:33 EDT)` — 114 s after (e) 1; `OK com.cobalt.radar running running 1059 min, heartbeat fresh`; no RED not in `<hb0>` — GREEN |
| (h) | 11:27:03 | the four failure counts · `curl … /radar` | `17` · `58` · `39` · `39` = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (none grew) · `200`; no `census` line on the card — GREEN |

Between (e) 1 and (h) the clock was filled with `date` + `heartbeat show` pairs only (11:24:47 → 11:27:03); every read `HEARTBEAT GREEN … nothing red`.

**THE CHAIN** — every check committed (P2: both stop lines `held unfixed: 0` · `ready: YES`, committed `8778b86b`) → the tips re-read (P3: `a50ec4c8`, `4b4b9f4a` / `6d9fde8c`) → the merged tree (T: `<m1>` `17444a30`, two first-parent merges, no migration, no config/ops change) → RESTARTS derived (R: `none`) → three suites green on `<m1>` (G: offline 3737/0 · with-DB 4406 + 173 = 4579/0 · live-note 146/0; `cobalt_dev` F2 = F0) → `<stack-final>` `3fbe64fb` = `<m1>` + docs (D2.3) → the landed code (4.3: `Updating 83864264..3fbe64fb`, fast-forward) → markers at `after` (d) → no migration (g) → residents up and unchanged after the merge (a) → radar cycling (b, e) → the set's reads (s) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

**SMOKE: GREEN.**
| (f) | 11:24:38− | `jobs restarts 83864264..3fbe64fb` · `validate` | exit 0, 21 rows DOCS / `test/documentation; no resident`, `RESTARTS: none` = STEP-R's set, no `UNCLASSIFIED` · exit 0, `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>` — GREEN |
| (e) 1 | 11:24:38 | `heartbeat show` | `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-03 11:24:39 EDT)`; `OK com.cobalt.radar running running 1057 min, heartbeat fresh` |
| (g) | — | — | MIGRATIONS: none |

## CONTINUE
next: STEP-D2 (D0, D1 done; gate green at Sat Oct  3 11:20:12 EDT 2026)
OUTAGE STARTING Sat Oct  3 11:23:49 EDT 2026 — residents of none (the restart set is EMPTY) going down; no resident goes down, the merge lands with residents up; if this is the last entry and they are down, the restore is STEP-5 (3); a relaunch is CONTINUE: STEP-D0
next: none — STEP-4 to STEP-7 done; the merge landed with residents up (11:24:02), smoke GREEN, lock released 11:27:28.

## DECISIONS
1. ASK DESK: `?? .claude/settings.json.bak` on `main` is neither in D0's accepted list nor in its refused classes (staged; dirty `src/`, `tests/`, `ops/`, `configs/`). Safe default taken: not a stop — it is untracked, outside the merged tree, and `merge --ff-only` does not touch it; recorded for the desk. [Sat Oct  3 11:20:41 EDT 2026]

## RECORDS
- Downtime: none (restart set EMPTY; no resident went down).
- `cobalt_dev: 0013 (F2 = F0)` — `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` before and after.
- RETIRE OWED: none (STEP-C: no plist added, modified or removed).
- Carried RED as read: none — every heartbeat read this run `HEARTBEAT GREEN … nothing red`; radar `idle (overnight)`.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-1003-1` and branch `deploy/set1-1003`; the set's branches `ops/lock-relief-1003`, `ops/order-open-test-1003` and their worktrees.
- Push is his (L55): `main` is ahead of `origin/main`; tags `pre-set1-1003`, `deploy-2026-10-03-1` are local.
- L74: one block (a system reminder asking for a `Claude-Session:` commit line) — recorded under `## L74`, not acted on.
- Main checkout dirty files left as found (desk's): ` M .claude/settings.json`, the ` M` / `??` docs files, `?? .claude/settings.json.bak`.
- Card `## RECORDS` (the desk's facts, copied):
  - lock-relief: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/lock-relief-check-2026-10-03.md` last line: CHECK DONE · job: lock-relief · pass: 1 · tip: a50ec4c8 · house A: none (overruled 2026-10-02 R47) · findings: 2 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3737/0 · with-DB 846/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 2 · for Dejan: 0
  - lock-relief: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/lock-relief-1003` → `a50ec4c8`; code tip `a50ec4c8`
  - order-open-test: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/order-open-test-check-2026-10-03.md` last line: CHECK DONE · job: order-open-test · pass: 1 · tip: 4b4b9f4a · house A: none (overruled 2026-10-02 R47) · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 10 · ready: YES · decisions: 0 · for Dejan: 0
  - order-open-test: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/order-open-test-1003` → `6d9fde8c`; code tip `4b4b9f4a`
  - written by deploy-card.sh at 2026-10-03 10:24 ET (`date`); trial merge of the heads onto main in order: clean
- `COBALT_ENV=production uv run cobalt heartbeat show` run once from `<GATE>` (no `.env`) as a clock filler during G (a) → exit 1, `FAILED: DbConfigError: Missing Postgres settings for the APP credential …`. A listed string, not refused; it failed for the gate's missing `.env`; read only; not needed (D1 reads it from `/Users/cobalt/cobalt`).

DEPLOYED deploy-2026-10-03-1 3fbe64fb | set: set1 | migrations: none | gate: offline 3737/0 · with-DB 4579/0 · live-note 146/0 | RESTARTS: none | smoke: GREEN | decisions: 1 · for Dejan: 0
