# deploy dml-roles — set: radar — migrations: 0025

## §0 Headline
Deploy of card 804 (`ops/dml-roles-1013`, migration 0025) is under way. Authorization and preflight are green.

## L74
One system notice in this session asked for a `Claude-Session:` line on commits. It is recorded here and not followed: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/804-deploy-dml-roles-card.md"` → exit 0:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/804-deploy-dml-roles-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/804-deploy-dml-roles-card.md" · 0 · ec76e5137c6fce79805de8be4e4db23e261ec169
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/804-deploy-dml-roles-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la "…/reports/deploy-dml-roles.md"` | 1 | `No such file or directory` |
| P0 | `authorize.sh deploy` (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Mon Oct 19 00:43:54 EDT 2026`: outside the 21:30-22:30 backup window |
| P2 | `tail -n 3 ".../dml-roles-check-2026-10-13.md"` | 0 | `CHECK DONE · job: dml-roles-1013 · pass: 1 · tip: ce3b9dc1 · … · held: 2 · fixed: 1 · held unfixed: 1 · open: 3 · … · ready: NO · decisions: 2 · for Dejan: 0 · tokens: 255901`: carries `held unfixed: 1` and `ready: NO` as the row names |
| P2 | `git log -1 --format=%H -- ".../dml-roles-check-2026-10-13.md"` | 0 | `8b531a9f0cf43b2811c5168977ee9c4ac97448ee` |
| P2 | `git diff --stat -- ".../dml-roles-check-2026-10-13.md"` | 0 | nothing |
| P2 fix-round | `merge-base --is-ancestor ce3b9dc1 ce3b9dc1` (check tip → code tip) | 0 | ancestor |
| P2 fix-round | `git show "b4d8dbf9:docs/…/dml-roles-build-2026-10-13.md"` (the fix report at the branch head) | 0 | last line `BUILT · job: dml-roles-1013 · tip: ce3b9dc1 \| on e7ef198a \| migration: 0025, rolled back \| offline 8653/0 \| with-DB 5610/0 \| live-note 147/0 \| cobalt_dev: 0013 \| .env: removed \| RESTARTS: com.cobalt.radar \| rows: 8 of 8 \| self-check: 3 of 3 \| decisions: 0 · for Dejan: 0 · tokens: 105131` |
| P2 fix-round | check `## FIXES` / `## RUNS` `HELD, NOT FIXED` ids | — | `A2` only (`dml-roles-check-2026-10-13.md:121`, `:167`) |
| P2 fix-round | fix report line 157 | — | `FIXED: A2 — tests/cobalt/test_db_apply_db.py::test_t5_a_failing_second_statement_rolls_the_first_back` |
| P2 fix-round | `git show ce3b9dc1:tests/cobalt/test_db_apply_db.py` | 0 | `test_t5_a_failing_second_statement_rolls_the_first_back` exists, marked `@requires_db` only, no xfail |
| P2 | the fix report is committed at the branch head `b4d8dbf9` (read with `git show`); it is not on `main` (`log -1` and `diff --stat` on `main` print nothing) | — | committed, unmodified |
| P3 | `rev-parse --short=8 ce3b9dc1` | 0 | `ce3b9dc1` |
| P3 | `rev-parse --short=8 ops/dml-roles-1013` | 0 | `b4d8dbf9` = `TIP` |
| P3 | `merge-base --is-ancestor ce3b9dc1 b4d8dbf9` | 0 | ancestor |
| P3 | `diff --stat ce3b9dc1 b4d8dbf9 -- . ":(exclude)docs"` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found: /Users/cobalt/cobalt-wt/*/.env`: nobody holds the lock |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/dml-roles` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m0>` = `ec76e513` |
| P5 | `merge-base --is-ancestor ec76e513 main` | 0 | ancestor |
| P5 | `log --oneline main..deploy/dml-roles` | 0 | empty |
| P6 | `grep -c -F "0025_dml_roles" …/__init__.py` | 1 | `0` = before |
| P7 | `diff --stat main b4d8dbf9 -- src/cobalt/db_migrations` | 0 | `0025_dml_roles.rollback.sql \| 33`, `0025_dml_roles.sql \| 77`, `__init__.py \| 8`: 3 files, 118 insertions |
| P7 | `diff main b4d8dbf9 -- …/__init__.py` | 0 | FORWARD gains `MIGRATIONS_DIR / "0025_dml_roles.sql"` last; REVERSE gains `MIGRATIONS_DIR / "0025_dml_roles.rollback.sql"` first; the rest is docstring. Only the card's 0025 |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 89330` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 70450` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 89351).` |

## THE TREE
- `git -C <GATE> merge --no-edit b4d8dbf9` → `Merge made by the 'ort' strategy.` (33 files changed, 780 insertions(+), 77 deletions(-)). No conflict.
- `git -C <GATE> rev-parse --short=8 HEAD` → `<m1>` = `db436d61`.
- `log --oneline --merges --first-parent ec76e513..deploy/dml-roles` → `db436d61 Merge commit 'b4d8dbf9' into deploy/dml-roles`: one merge for one head.
- `merge-base --is-ancestor ce3b9dc1 deploy/dml-roles` → exit 0; `merge-base --is-ancestor b4d8dbf9 deploy/dml-roles` → exit 0.
- `diff --stat ec76e513 deploy/dml-roles -- src/cobalt/db_migrations` → `0025_dml_roles.rollback.sql | 33`, `0025_dml_roles.sql | 77`, `__init__.py | 8`: the card's 0025 and the registry file it edits.
- `diff ec76e513 deploy/dml-roles -- …/__init__.py` → FORWARD gains `0025_dml_roles.sql`, REVERSE gains `0025_dml_roles.rollback.sql`; the other lines are docstring.
- FORWARD check, `grep -n -F 'MIGRATIONS_DIR / "' <GATE>/src/cobalt/db_migrations/__init__.py` → FORWARD ends `175: MIGRATIONS_DIR / "0025_dml_roles.sql",`; REVERSE begins `180: MIGRATIONS_DIR / "0025_dml_roles.rollback.sql",`.
- STEP-C: `diff --stat ec76e513 deploy/dml-roles -- configs ops` → ` ops/desk/gate-lists.md | 4 ++--` / ` 1 file changed, 2 insertions(+), 2 deletions(-)`. `sh /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh "<card>" ec76e513 deploy/dml-roles` → exit 0, `STEP-C: ADMITTED 0`. `<launchd set>`: empty. `<deferred set>`: empty.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0. uv made the gate's `.venv` first (`Creating virtual environment at: .venv` · `Installed 256 packages in 932ms`). The table, whole:

```
path	change	rule	restart
docs/40 - DevDocs/cobalt/db_apply.md	M	DOCS	-
docs/40 - DevDocs/cobalt/db_migrations/__init__.md	M	DOCS	-
docs/40 - DevDocs/prompts/CARD.md	M	DOCS	-
docs/40 - DevDocs/reports/dml-roles-build-2026-10-13.md	A	DOCS	-
docs/40 - DevDocs/reports/dml-roles-build-2026-10-13.result	A	DOCS	-
ops/desk/gate-lists.md	M	operator script; no Cobalt reader	-
src/cobalt/db_apply.py	M	static import reach	com.cobalt.radar
src/cobalt/db_migrations/0025_dml_roles.rollback.sql	A	non-Python src asset	-
src/cobalt/db_migrations/0025_dml_roles.sql	A	non-Python src asset	-
src/cobalt/db_migrations/__init__.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_archiver_migrations.py	M	test/documentation; no resident	-
tests/cobalt/test_assumed_store.py	M	test/documentation; no resident	-
tests/cobalt/test_db_apply.py	M	test/documentation; no resident	-
tests/cobalt/test_db_apply_db.py	M	test/documentation; no resident	-
tests/cobalt/test_db_credentials.py	M	test/documentation; no resident	-
tests/cobalt/test_dml_roles_db.py	A	test/documentation; no resident	-
tests/cobalt/test_dml_roles_offline.py	A	test/documentation; no resident	-
tests/cobalt/test_drc_d2_fix_r1_db.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_d3_experiments.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_k1_store.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_store.py	M	test/documentation; no resident	-
tests/cobalt/test_f15_p1_records_offline.py	M	test/documentation; no resident	-
tests/cobalt/test_legs_migration.py	M	test/documentation; no resident	-
tests/cobalt/test_p4_migrations.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_handicap_store.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_migration.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_price_floor_db.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_score_migration.py	M	test/documentation; no resident	-
tests/cobalt/test_seam_drc_s3_registry.py	M	test/documentation; no resident	-
tests/cobalt/test_stale_score_db.py	M	test/documentation; no resident	-
tests/cobalt/test_tenancy.py	M	test/documentation; no resident	-
tests/cobalt/test_voice_store.py	M	test/documentation; no resident	-
tests/ops/test_card_md_migration_checklist.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```

No `UNCLASSIFIED` row. `<restart set>` = `com.cobalt.radar`. `<deferred set>` = empty. `<launchd set>` = empty. The migration has a resident going down (radar), so L66 holds.

## L68 GATE
- THE EQUAL-TREE CLAUSE does not hold: `git -C /Users/cobalt/cobalt diff --stat ce3b9dc1 db436d61 -- . ":(exclude)docs"` → ` tests/ops/test_hub_deferred_1018.py | 108 +++…` (1 file changed, 108 insertions(+), from `main`). The gate runs whole.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `264 passed, 163 skipped in 18.39s`: 0 failed. Every skip is a with-DB skip (`Postgres env settings not available` / `requires_db: …`).
- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-dml-roles all --deploy --deploy-gate --deselect tests/cobalt/test_db_apply_db.py --deselect tests/cobalt/test_dml_roles_db.py --migration`. The two deselects are the build's pass-1 deselects (build report `## W`, W1 and the gate line). There is no `--tickers` (`TICKERS: none`). It ran in the background and exited 0. Verdict lines, whole:

```
tests/ops: run (deploy gate)
offline 8658/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
forward, back, forward, back — F = F0 twice
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5610/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-dml-roles-all-20261019-004634.log
```

- (a) OFFLINE → `offline 8658/0`. The W line is `tests/ops: run (deploy gate)`. Log `:935` `4654 passed, 861 skipped, 4 xfailed` and `:1008` `4004 passed, 1 xfailed`.
- (b) `lock: waited 0 min`. `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:1025`). The proof-only ran at `0013`: `NOTHING WAS APPLIED` (`:1071`), no `CHANGED`.
- (c) PASS 1 → `5377 passed, 8 skipped, 127 deselected, 7 xfailed` (log `:1245`) = `<d1>` 5377. All 8 skips are in the allowed set. `test_playbook_live.py:31` is the decorator of `test_live_vault_renders_six_decks` (`:32`). `test_s3_c4_experiments.py:95` is the decorator of `test_x14_live_his_template_strips_to_the_committed_fixture` (`:96`). The rest are the listed lines and reasons.
- (c2) FORWARD → `dev forward: APPLIED 01:27:06` (log `:1247`). `F1: 908 45 126f2d6983fa59f9d0eaaff7da7dd29c` (`:1326`). `content UNCHANGED on every table`.
- (c3) PASS 2 → `233 passed, 1 deselected` (log `:2168`) = `<d2>` 233. with-DB = 5377 + 233 = 5610/0.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:2237`) = F0 field for field. `F (c4): 664 35 272c95bbb12241e3611e4b36326ccf87` (`:2428`). `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: `release-devdb-lock.sh deploy-dml-roles` → `lock released` (log `:2432`), then `.env: removed`. The log carries no clock time on that line. It falls between `dev forward: APPLIED 01:27:06` and my `date` of `Mon Oct 19 01:32:58 EDT 2026`. After the gate: `ls -la <GATE>/.env` → No such file. `grep -c -x -F "deploy-dml-roles" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory` (lock dir absent).
- (e) LIVE-NOTE → `147 passed, 1 skipped` (log `:2502`). The one skip is `test_replay_line.py:266` `COBALT_TEST_LIVE_DRC`, which is in the allowed set. No skip names `COBALT_LIVE_VAULT_ROOT`.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on db436d61

## Deploy table
### STEP-D0
| check | command | result |
|---|---|---|
| main | `status --short --branch` | first line `## main...origin/main [ahead 5]` |
| main | `status --porcelain` | ` M .claude/settings.json`, ` M` and `??` under `docs/40 - DevDocs/` only, plus `?? .claude/settings.json.bak` (not a `src/`, `tests/`, `ops/` or `configs/` path). No staged line |
| main moved | `diff --stat ec76e513 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | nothing |
| probe | `tag scratch-allow-probe-dml-roles` · `tag -d …` | `Deleted tag 'scratch-allow-probe-dml-roles' (was ec76e513)` |
| probe | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | `[main 95872173] …` → HEAD back at `ec76e513 docs(desk): deploy card 804 dml-roles, A2 fixed, rows` |
| tags | `rev-parse --verify --quiet refs/tags/deploy-2026-10-18-dml-roles` · `…/pre-dml-roles` | exit 1 · exit 1 |

### STEP-D1 (`Mon Oct 19 01:33:36 EDT 2026`)
- `<hb0>`: `HEARTBEAT GREEN — 17 job(s), 12 probe(s), nothing red  (2026-10-19 01:33:37 EDT)`. `radar idle (overnight)`. `com.cobalt.radar running 552 min, heartbeat fresh`. `com.cobalt.herdr` AMB (unmanaged, declared interim). `com.cobalt.prefill-refresh` and `com.cobalt.playbook` are `OWED (deferred bootstrap)`. No RED.
- `<val0>`: `validate` exit 0, ends `Placement (docs/PLACEMENT.md): tree clean.`. `<jobs0>` = `Jobs (F17): 17 registered — 6 resident, 11 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 3.9 h old` (ssd ARMED, b2 off).
- aset `state = running`, `<aset pid>` 89330 · radar `state = running`, `<radar pid>` 70450 · `Cobalt is ONLINE (PID: 89351).` · `ps -p 89351` → `89351 ?? 0:00.03 uv run src/cobalt_agent/main.py`.
- `tail -n 8 radar.err` → 8 lines `radar cycle: idle:overnight scan_id=None`, the last at `2026-10-19 01:32:56.390`.
- Log baselines: `<a0>` 283 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39.
- `curl … /radar` → `200`. Marker `grep -c -F "0025_dml_roles" …/__init__.py` → `0` (before).
- THE LAUNCHD SET: empty, nothing read.
- `<RB>` → `m0025` / `False`. That is the card's BEFORE `f`: the tool prints a Postgres boolean as Python `True`/`False`, as in `deploy-2026-09-24.md:205` and `deploy-d3-2026-09-19.md:391`. See `## DECISIONS` 1. No `## SMOKE READS` line is marked `census`.
- D1-M `COBALT_ENV=production uv run cobalt db migrate --allow-prod --proof-only` → exit 0. 37 tables probed. `Proof cost: total 292.1 s — and a migration pays it TWICE (before and after), inside the outage.` · `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.` · `SLOTS ok · highest user.aset_sizings 60 of 1600` · `FINGERPRINT cols 908 · rels 45 · views_md5 126f2d6983fa59f9d0eaaff7da7dd29c` · `TABLES 0024`. No `CHANGED`.

## Smoke

## CONTINUE
gate green at 01:32:58; D0 and D1 done
next: STEP-D2

## DECISIONS
1. ASK DESK: the card's `## READ-BACK` writes BEFORE `f` and AFTER `t`, and `db query` prints `False` / `True`. Safe default taken: I read `False` as `f` and `True` as `t`. They are the same Postgres boolean; earlier deploys quoted this tool's `True`/`False` the same way. A future card could write the tool's spelling. [Mon Oct 19 01:33:36 EDT 2026]

## RECORDS

(run in progress — next step under ## CONTINUE)
