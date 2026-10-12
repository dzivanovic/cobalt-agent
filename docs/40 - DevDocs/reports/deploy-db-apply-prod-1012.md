# deploy db-apply-prod-1012 · SET: none · MIGRATIONS: none

## §0 Headline
In progress.

## L74
none yet

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/432-deploy-db-apply-prod-card.md"` → exit 0, quoted whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/432-deploy-db-apply-prod-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/432-deploy-db-apply-prod-card.md" · 0 · ad5d36c9f2072a3938420cfca56b31a919078671
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/432-deploy-db-apply-prod-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 138:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| first launch | `ls -la "<REPORT>"` | 1 | No such file or directory |
| P0 | authorize.sh (above) | 0 | AUTHORIZED |
| P1 DATE | `date` | 0 | Mon Oct 12 18:19:29 EDT 2026 |
| P2 check last line | `tail -n 3 ".../reports/db-apply-prod-check-2026-10-12.md"` | 0 | `CHECK DONE · job: db-apply-prod-1012 · pass: 1 · tip: fba1454e · … · held unfixed: 0 · open: 1 · … · ready: YES · decisions: 3 · for Dejan: 0 · tokens: 290333` — carries `held unfixed: 0` and `ready: YES`; `tip: fba1454e` = code tip |
| P2 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/db-apply-prod-check-2026-10-12.md"` | 0 | 314908fe30bb24431984909558a3ba6708363aea |
| P2 unmodified | `git -C /Users/cobalt/cobalt diff --stat -- "<same>"` | 0 | nothing |
| P3 code tip | `git -C /Users/cobalt/cobalt rev-parse --short=8 fba1454e` | 0 | fba1454e |
| P3 branch head | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/db-apply-prod-1012` | 0 | fba1454e (= row, = TIP) |
| P3 ancestor | `git -C /Users/cobalt/cobalt merge-base --is-ancestor fba1454e ops/db-apply-prod-1012` | 0 | — |
| P3 head adds docs only | `git -C /Users/cobalt/cobalt diff --stat fba1454e ops/db-apply-prod-1012 -- . ':(exclude)docs'` | 0 | nothing |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 gate status | `git -C /Users/cobalt/cobalt-wt/deploy-db-apply-prod-1012 status --short --branch` | 0 | `## deploy/db-apply-prod-1012` |
| P5 m0 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `<m0>` = ad5d36c9 |
| P5 m0 on main | `git -C /Users/cobalt/cobalt merge-base --is-ancestor ad5d36c9 main` | 0 | — |
| P5 gate holds nothing | `git -C /Users/cobalt/cobalt log --oneline main..deploy/db-apply-prod-1012` | 0 | EMPTY |
| P6 marker 1 | `grep -c -F -e "PARSER_PG_MAJOR" "/Users/cobalt/cobalt/src/cobalt/db_apply.py"` | 2 | `grep: /Users/cobalt/cobalt/src/cobalt/db_apply.py: No such file or directory` = before (file absent) |
| P6 marker 2 | `grep -c -F -e "pglast" "/Users/cobalt/cobalt/pyproject.toml"` | 1 | `0` = before |
| P7 migrations | `git -C /Users/cobalt/cobalt diff --stat main fba1454e -- src/cobalt/db_migrations` | 0 | `src/cobalt/db_migrations/cli.py \| 2 ++` — CODE, no migration; matches `MIGRATIONS: none` |
| P8 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, pid 7760 |
| P8 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, pid 61093 |
| P8 plist | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 agent | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C /Users/cobalt/cobalt-wt/deploy-db-apply-prod-1012 merge --no-edit fba1454e` → `Merge made by the 'ort' strategy.` (21 files changed, 1921 insertions(+), 7 deletions(-))
- `git -C <GATE> rev-parse --short=8 HEAD` → `<m1>` = **0fa71f43**
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent ad5d36c9..deploy/db-apply-prod-1012` → `0fa71f43 Merge commit 'fba1454e' into deploy/db-apply-prod-1012` (one line, one head)
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor fba1454e deploy/db-apply-prod-1012` → exit 0
- `git -C /Users/cobalt/cobalt diff --stat ad5d36c9 deploy/db-apply-prod-1012 -- src/cobalt/db_migrations` → `src/cobalt/db_migrations/cli.py | 2 ++` — CODE; no migration path (MIGRATIONS: none)
- STEP-C `git -C /Users/cobalt/cobalt diff --stat ad5d36c9 deploy/db-apply-prod-1012 -- configs ops` → `ops/desk/authorize.sh | 71 +++…` · `ops/desk/desk-launch.sh | 43 +++…-` · `2 files changed, 113 insertions(+), 1 deletion(-)` — no plist added, modified or removed. The set changes neither `DEPLOY-HUB.md` nor `gate.sh`.

## RESTARTS
`cd /Users/cobalt/cobalt-wt/deploy-db-apply-prod-1012` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (first run in the gate created `.venv`, `Installed 254 packages in 800ms`):
```
path	change	rule	restart
.gitignore	M	META	-
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/db_apply.md	A	DOCS	-
docs/40 - DevDocs/cobalt/db_migrations/cli.md	M	DOCS	-
docs/40 - DevDocs/prompts/CARD.md	M	DOCS	-
docs/40 - DevDocs/prompts/PRODWRITE-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/db-apply-prod-build-2026-10-12.md	A	DOCS	-
ops/desk/authorize.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
pyproject.toml	M	resident reads	com.cobalt.agent,com.cobalt.aset,com.cobalt.radar
src/cobalt/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/db_apply.py	A	static import reach	com.cobalt.radar
src/cobalt/db_migrations/cli.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_db_apply.py	A	test/documentation; no resident	-
tests/cobalt/test_db_apply_db.py	A	test/documentation; no resident	-
tests/cobalt/test_jobs_restarts.py	M	test/documentation; no resident	-
tests/ops/test_authorize.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_prodwrite.py	M	test/documentation; no resident	-
tests/ops/test_gitignore_apply_sql.py	A	test/documentation; no resident	-
tests/ops/test_prodwrite_hub.py	M	test/documentation; no resident	-
uv.lock	M	resident reads	com.cobalt.agent,com.cobalt.aset,com.cobalt.radar
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row. `<restart set>` = **com.cobalt.agent com.cobalt.aset com.cobalt.radar** (= the check's RESTARTS).

## L68 GATE
- THE EQUAL-TREE CLAUSE HOLDS: ONE branch in `TIP`; `git -C /Users/cobalt/cobalt diff --stat fba1454e 0fa71f43 -- . ":(exclude)docs"` → prints nothing; the check's stop line carries `with-DB 5212/0` (> 0). The check's three suite lines are the gate's; (a)–(f) skipped; `gate.sh` not run, `cobalt_dev` not touched, the lock never taken.
- Quoted from `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/db-apply-prod-check-2026-10-12.md`: line 6 `Suites green on fba1454e: offline 4309/0 · with-DB 5212/0 · live-note 146/0 · cobalt_dev: 0013 — F2 = F0 · .env removed · tests/ops 3447 passed. RESTARTS: agent, aset, radar.`; line 220 `offline :885 4309 passed, 806 skipped, 1 xfailed, 36 warnings in 630.52s … pass 1 :1115 5007 passed, 7 skipped, 99 deselected, 3 xfailed, 43 warnings in 772.82s; pass 2 :1969 205 passed, 1 deselected, 5 warnings in 228.17s (5007 + 205 = 5212); live-note :2160 146 passed, 1 skipped, 15 warnings in 25.66s. No skip is marked OUTSIDE the allowed set.`
- (c)'s judgment kept — the check's SKIPPED lines (its lines 210–216) against the allowed set, each by test and reason:
  - `tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev` — inside
  - `tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: …` — inside
  - `tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof` — inside
  - `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …` — inside (reason names `COBALT_TEST_LIVE_DRC`)
  - `tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read` — inside: line 95 is `@requires_live` on `def test_x14_live_his_template_strips_to_the_committed_fixture` (grep, gate tree line 96)
  - `tests/taxonomy/test_catalyst.py:365: …` — inside
  - `tests/taxonomy/test_predicate.py:262: …` — inside
  All seven inside; the gate does not run whole.
- (a0) THE EARLY READ, run anyway (L73): `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_archiver_migrations.py … tests/cobalt/test_jobs_restarts.py` (the 17 files) → `263 passed, 163 skipped in 17.48s` — `0 failed` (every skip a with-DB `Postgres env settings not available` / `requires_db` skip).
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.
- `cobalt_dev: 0013 — F2 = F0` (the check's; this run made no dev forward). `.env: removed` (never created by this run).

GATE GREEN on 0fa71f43

## Deploy table
| step | command | exit | result |
|---|---|---|---|
| D0 main | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | `## main...origin/main [ahead 194]` |
| D0 porcelain | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | only ` M` / `??` under `docs/40 - DevDocs/`, ` M configs/cobalt/rules.yaml`, ` M .claude/settings.json`, and `?? .claude/settings.json.bak` (untracked, not src/tests/ops/configs; no staged line) |
| D0 main unmoved | `git -C /Users/cobalt/cobalt diff --stat ad5d36c9 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| D0 probe | `tag scratch-allow-probe-db-apply-prod-1012` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-db-apply-prod-1012' (was ad5d36c9)` |
| D0 probe | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 26b48f5e] scratch: …` → `ad5d36c9 docs(desk): R1271 his word deploy 417, deploy card 432` (HEAD back) |
| D0 tags | `rev-parse --verify --quiet refs/tags/deploy-2026-10-12-db-apply-prod` · `refs/tags/pre-db-apply-prod-1012` | 1 · 1 | both free |
| D1 date | `date` | 0 | Mon Oct 12 18:21:40 EDT 2026 |
| D1 `<hb0>` | `COBALT_ENV=production uv run cobalt heartbeat show` | 0 | `HEARTBEAT RED — 2 job(s) and 1 probe(s) (2026-10-12 18:21:41 EDT)`; REDs: `archiver last run FAILED — last run 2026-10-10 00:54 UTC (69.5 h ago) …` · `com.cobalt.archiver failed RuntimeError: 18 archiver failure(s): DKNG/i2: … Finviz HTTP failed: Client error '429 Too Many Requests' …` · `com.cobalt.replay failed ReplayError: archiver not done: state 'failed'` + traceback. Named, not a stop (not aset / sheet / radar). OK: database, sheet HTTP 200, sheet daymode, radar `scanning (aftermarket), members 50`, aset pid 7760, agent pid 22243, `com.cobalt.radar running 3532 min, heartbeat fresh`. AMB herdr (declared interim). |
| D1 `<val0>` | `COBALT_ENV=production uv run cobalt validate` | 0 | `13 trade_def(s) validated OK` … `Placement (docs/PLACEMENT.md): tree clean.`; no failing line |
| D1 `<jobs0>` | (same) | — | `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` · `registry <-> ops/: 15 label(s), exact match.` |
| D1 backup | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 3.9 h old` |
| D1 aset | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `<aset pid>` = 7760 |
| D1 radar | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `<radar pid>` = 61093 |
| D1 agent | `/Users/cobalt/cobalt/cobalt.sh status` · `ps -p 22243` | 0 · 0 | `Cobalt is ONLINE (PID: 22243).` · `22243 ?? 0:00.04 uv run src/cobalt_agent/main.py` |
| D1 radar.err | `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` | 0 | `2026-10-12 18:18:48.236 … radar cycle: scanning scan_id=1791843439128`, then price-floor lines to 18:20:40; no traceback |
| D1 counts | `grep -c` aset `Started server process` / aset `Traceback` / radar `Traceback` / radar `TaxonomyConfigError` / aset `radar panel FAILED` / aset `radar pool refresh FAILED` / radar `radar S5 evaluate FAILED` / radar `lifecycle card read failed` | — | `<a0>` 277 · `<ta0>` 217 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 18 · `<rpr0>` 60 · `<re0>` 43 · `<lc0>` 39 |
| D1 curl | `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/radar` | 0 | `200` |
| D1 markers | the two `## MARKERS` | 2 · 1 | `No such file or directory` (absent) · `0` = before |
| D1 migration | — | — | MIGRATIONS: none; `<RB>` and D1-M not run |

## CONTINUE
next: STEP-D2 (D2.0 commit)

## DECISIONS

## RECORDS

(run in progress — next step under ## CONTINUE)
