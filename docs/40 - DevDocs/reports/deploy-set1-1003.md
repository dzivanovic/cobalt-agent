# deploy set1-1003 — SET: set1 — MIGRATIONS: none

## §0 Headline
- Deploy of set 1 (`ops/lock-relief-1003` a50ec4c8 + `ops/order-open-test-1003` 6d9fde8c) on a non-trading Saturday. In progress.

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

## Smoke

## CONTINUE
next: STEP-D2 (D0, D1 done; gate green at Sat Oct  3 11:20:12 EDT 2026)

## DECISIONS
1. ASK DESK: `?? .claude/settings.json.bak` on `main` is neither in D0's accepted list nor in its refused classes (staged; dirty `src/`, `tests/`, `ops/`, `configs/`). Safe default taken: not a stop — it is untracked, outside the merged tree, and `merge --ff-only` does not touch it; recorded for the desk. [Sat Oct  3 11:20:41 EDT 2026]

## RECORDS
- `COBALT_ENV=production uv run cobalt heartbeat show` run once from `<GATE>` (no `.env`) as a clock filler during G (a) → exit 1, `FAILED: DbConfigError: Missing Postgres settings for the APP credential …`. A listed string, not refused; it failed for the gate's missing `.env`; read only; not needed (D1 reads it from `/Users/cobalt/cobalt`).

(run in progress — next step under ## CONTINUE)
