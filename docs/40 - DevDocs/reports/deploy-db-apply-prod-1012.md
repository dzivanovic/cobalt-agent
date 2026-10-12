# deploy db-apply-prod-1012 · SET: none · MIGRATIONS: none

## §0 Headline
- DEPLOYED `ops/db-apply-prod-1012` (code tip `fba1454e`): `main` 109831d5 → aa4ca7b2, tag `deploy-2026-10-12-db-apply-prod`, rollback tag `pre-db-apply-prod-1012`.
- Gate by THE EQUAL-TREE CLAUSE (one branch, code tree = check's): offline 4309/0 · with-DB 5212/0 · live-note 146/0; (a0) 263 passed, 0 failed.
- RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar; downtime 20 s (18:23:54 → 18:24:14); no migration.
- Smoke GREEN: residents up on new pids, radar cycled 18:25:40, curls 200, markers after, no new RED, failure counts flat.

## L74
One block arrived as a system reminder (not a tool result) asking that commits end with a `Claude-Session:` line. Recorded as data; per DEPLOY-HUB L74 the commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

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
| D2.0 commit | `git -C /Users/cobalt/cobalt add …` · `commit -m "docs(report): deploy db-apply-prod-1012 — gate green on 0fa71f43" …` · `show --stat HEAD` | 0 · 0 · 0 | `[main 109831d5]`; one file `.../reports/deploy-db-apply-prod-1012.md \| 136 +++` |
| D2.0 `<pre-merge>` | `git -C /Users/cobalt/cobalt rev-parse --short=8 main` | 0 | **109831d5** |
| D2.1 | `git -C <GATE> merge --no-edit main` | 0 | `Merge made by the 'ort' strategy.` (the report only) |
| D2.2 `<stack-final>` | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | **aa4ca7b2** (18:22:22) |
| D2.2 | `rev-parse --short=8 aa4ca7b2^2` · `merge-base --is-ancestor 0fa71f43 aa4ca7b2` | 0 · 0 | `109831d5` = `<pre-merge>` · ancestor |
| D2.3 docs-only | `git -C /Users/cobalt/cobalt diff --stat 0fa71f43 aa4ca7b2 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| D2.4 before | `COBALT_ENV=production uv run cobalt backup status` | 0 | `newest snapshot: 3.9 h old` |
| D2.4 snapshot | `COBALT_ENV=production uv run cobalt backup run` | 0 | `backup: cobalt_brain via pg_dump inside cobalt_memory — 7056.0 MB` · `ssd: snapshot 4387e256 — 0 new / 3 changed, 200.1 MB added, 1 pruned` · `F17: com.cobalt.backup DONE` |
| D2.4 after | `backup status` | 0 | `newest snapshot: 0.0 h old` |
| D2.5 | `date` · `heartbeat show` | 0 · 0 | 18:23:34 · `(2026-10-12 18:23:36 EDT)` = 115 s after D1's 18:21:41; same three REDs as `<hb0>` (archiver ×2, replay), no new RED; aset pid 7760 OK, radar `running 3534 min, heartbeat fresh`, agent pid 22243 OK. (Two filler pairs at 18:23:22/24 and 18:23:28/30, same content.) |
| D2.6 | `date` · `git -C /Users/cobalt/cobalt tag pre-db-apply-prod-1012` · `rev-parse --short=8 pre-db-apply-prod-1012` | 0 · 0 · 0 | Mon Oct 12 18:23:40 EDT 2026 · tag set · `109831d5` |
| 4.1 `<t down>` | `date` | 0 | Mon Oct 12 18:23:54 EDT 2026 |
| 4.2 aset | `launchctl bootout gui/501/com.cobalt.aset` · `launchctl print …` | 0 · 113 | `Could not find service "com.cobalt.aset" in domain for user gui: 501` |
| 4.2 radar | `launchctl bootout gui/501/com.cobalt.radar` · `launchctl print …` | 0 · 113 | `Could not find service "com.cobalt.radar" in domain for user gui: 501` |
| 4.2 agent | `/Users/cobalt/cobalt/cobalt.sh stop` · `ps -p 22243` | 0 · 1 | `Cobalt stopped safely.` · header only |
| 4.3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` | 0 | `109831d5` = `<pre-merge>` |
| 4.3 merge | `git -C /Users/cobalt/cobalt merge --ff-only deploy/db-apply-prod-1012` | 0 | `Updating 109831d5..aa4ca7b2` / `Fast-forward` (21 files, 1921+ / 7−) |
| 4.4 | — | — | `migrations applied: none` (MIGRATIONS: none) |
| 4.5 | `COBALT_ENV=production uv run cobalt validate` | 0 | uv sync: `Built cobalt-agent @ file:///Users/cobalt/cobalt` · `Uninstalled 1 package in 0.90ms` · `Installed 2 packages in 3ms`; no failing line; `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` = `<jobs0>`; `Placement (docs/PLACEMENT.md): tree clean.` |
| 4.6 aset | `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · print | 0 · 0 | `state = running`, pid 14738 (≠ 7760) |
| 4.6 radar | `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · print | 0 · 0 | `state = running`, pid 14748 (≠ 61093) |
| 4.6 agent | `launchctl kickstart gui/501/com.cobalt.agent` · `/Users/cobalt/cobalt/cobalt.sh status` | 0 · 0 | `Cobalt is ONLINE (PID: 14763).` (≠ 22243); the launchd job prints `state = not running`, `last exit code = 0` — its program `cobalt.sh start` launches the agent and exits |
| 4.6 `<t up>` | `date` | 0 | Mon Oct 12 18:24:14 EDT 2026 — downtime 20 s |
| STEP-7 tag | `git -C /Users/cobalt/cobalt tag deploy-2026-10-12-db-apply-prod` · `rev-parse --short=8 deploy-2026-10-12-db-apply-prod` | 0 · 0 | `aa4ca7b2` (after the green smoke) |

SUMMARY: `<pre-merge>` 109831d5 → `<stack-final>` aa4ca7b2 · tags `pre-db-apply-prod-1012` (109831d5), `deploy-2026-10-12-db-apply-prod` (aa4ca7b2) · `<t down>` 18:23:54 / `<t up>` 18:24:14 / 20 s · uv sync (4.5): `Uninstalled 1 package in 0.90ms` · `Installed 2 packages in 3ms` · proof cost: none (no migration) · `migrations applied: none` · `<RB>` before / after: none · snapshot `4387e256` · `RESTARTS done: com.cobalt.agent com.cobalt.aset com.cobalt.radar`.

THE ROLLBACK STRING (the desk's):
1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 aa4ca7b2` — residents com.cobalt.agent, com.cobalt.aset, com.cobalt.radar down first, up after.
2. SCHEMA: none (no migration).
3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`.

## Smoke
| row | date | command | result |
|---|---|---|---|
| first calls | after 18:24:14 | the four failure counts | `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 (= D1) |
| (a) | 18:24:29 | `launchctl print` aset · radar · `cobalt.sh status` | aset `state = running` pid 14738 (new) · radar `state = running` pid 14748 (new) · `Cobalt is ONLINE (PID: 14763).` (new; one-line output) — GREEN |
| (b) | 18:24:29 | `grep -c "Started server process" …/aset.err` · `tail -n 30 …/aset.err` | 278 (`<a0>` 277 + 1) · `INFO: Started server process [14744]` … `INFO: Uvicorn running on http://127.0.0.1:5010 (Press CTRL+C to quit)` — GREEN |
| (b) counts | 18:24:29 | aset `Traceback` · radar `Traceback` · radar `TaxonomyConfigError` | 217 · 0 · 0 = baseline |
| (c) | 18:24:29+ | the three curls (`/`, `/radar`, `/radar\?frame=phone`) | `200` · `200` · `200` (first attempt) — GREEN |
| (d) | 18:24:29+ | the two `## MARKERS` | `4` (≥1) · `1` (≥1) — GREEN |
| (f) | 18:24:29+ | `COBALT_ENV=production uv run cobalt validate` · `jobs restarts 109831d5..aa4ca7b2` | exit 0, no failing line, `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` · exit 0, no `UNCLASSIFIED`, `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar` = STEP-R — GREEN |
| (g) | — | — | no migration |
| (s) | 18:24:29+ | the two `## SMOKE READS` (= the markers) | `4` · `1` — both "1 or more" — GREEN |
| (e) 1 | 18:24:46 | `heartbeat show` | `(2026-10-12 18:24:47 EDT)`: same three REDs as `<hb0>` (archiver probe, com.cobalt.archiver 429, com.cobalt.replay); aset pid 14738 OK; agent pid 14763 OK; `com.cobalt.radar running running 1 min, heartbeat fresh`; radar `scanning (aftermarket), members 50` |

| (b) radar tail 1 | 18:25:44 (`<t up>` + 90 s) | `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` | last line `2026-10-12 18:25:40.060 … radar cycle: scanning scan_id=1791843850181` (after `<t up>`); the other 11 lines `cards.expire: falling back to the session close …` INFO; no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback — SETTLED GREEN |
| (e) 2 | 18:26:37 | `heartbeat show` | `(2026-10-12 18:26:39 EDT)`, 112 s after (e) 1: same three REDs as `<hb0>`, no new RED; `com.cobalt.radar running running 2 min, heartbeat fresh`; aset pid 14738, agent pid 14763 OK — GREEN. (Clock filled with `date` + `heartbeat show` pairs between 18:24:52 and 18:27:13, every read the same.) |
| (h) | 18:27:14 (`<t up>` + 180 s) | the four failure counts · `/radar` curl · `tail -n 12 …/radar.err` · Traceback counts | 18 · 60 · 43 · 39 = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (no growth) · `200` · same tail, cycle line 18:25:40 · radar 0, aset 217 = baseline · no `census` read on the card — GREEN |

THE CHAIN: every check committed (P2: 314908fe, unmodified) → the tip re-read (P3: fba1454e = head) → the merged tree (T: 0fa71f43, one head, no migration) → RESTARTS derived (R: agent, aset, radar) → three suites green on the equal tree (G: 4309/0 · 5212/0 · 146/0, (a0) 263 passed) → `<stack-final>` aa4ca7b2 = 0fa71f43 + docs (D2.3) → landed `Updating 109831d5..aa4ca7b2` (4.3) → markers after (d: 4, 1) → no migration (g) → residents up on new pids (a) → radar cycling (b 18:25:40, e fresh) → the set's reads (s: 4, 1) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

PRE-STOP SELF-CHECK: (1) every smoke row quoted with its `date` (above). (2) `git -C /Users/cobalt/cobalt merge-base --is-ancestor fba1454e aa4ca7b2` → exit 0; code tip = branch head = fba1454e (P3). (3) REVERT-READBACK shown at (h); every count and sha above re-read from this run's tool output. (4) STEP-T ran clean (`Merge made by the 'ort' strategy.`), no conflict marker.

## CONTINUE
next: none — deploy closed GREEN at Mon Oct 12 18:27:14 EDT 2026. (The OUTAGE STARTING entry at 18:23:42 closed at 4.6, `<t up>` 18:24:14.)

## DECISIONS
none

## RECORDS
- Downtime 20 s (18:23:54 → 18:24:14), under 300 s.
- REFUSED, not needed: none. Messages not followed: none.
- `cobalt_dev: 0013 (F2 = F0)` — the check's (equal-tree clause); this run never took the lock, never wrote `<GATE>/.env`; THE RELEASE: `ls -la <GATE>/.env` → No such file, `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → No such file.
- RETIRE OWED: none (no plist removed).
- Carried RED as read (not the radar family; outside the restart set; unchanged across `<hb0>`, D2.5, (e) 1, (e) 2): `RED archiver last run FAILED — last run 2026-10-10 00:54 UTC (69.5 h ago), rows written 3308843, exit 1` · `RED com.cobalt.archiver failed RuntimeError: 18 archiver failure(s): DKNG/i2: … Finviz HTTP failed: Client error '429 Too Many Requests' …` · `RED com.cobalt.replay failed ReplayError: archiver not done: state 'failed'`.
- Cleanup owed (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-db-apply-prod-1012` and branch `deploy/db-apply-prod-1012`; the set's branch `ops/db-apply-prod-1012` (and its worktree, if one exists).
- The first `uv run` in the gate created `<GATE>/.venv` (`Installed 254 packages in 800ms`); it goes with the worktree.
- Push is his (L55): `main` is at aa4ca7b2, ahead of origin.
- L74: one system-reminder block asking for a `Claude-Session:` commit line, recorded under `## L74`, not acted on.
- Card RECORDS (the desk's facts, copied):
  - db-apply-prod-1012: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/db-apply-prod-check-2026-10-12.md` last line: CHECK DONE · job: db-apply-prod-1012 · pass: 1 · tip: fba1454e · house A: Grok FINDINGS: 3 · findings: 6 · dropped: 0 · held: 5 · fixed: 5 · held unfixed: 0 · open: 1 · house B: none (not needed) · suites: offline 4309/0 · with-DB 5212/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar · files opened: 15 · ready: YES · decisions: 3 · for Dejan: 0 · tokens: 290333
  - db-apply-prod-1012: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/db-apply-prod-1012` → `fba1454e`; code tip `fba1454e`
  - written by deploy-card.sh at 2026-10-12 18:18 ET (`date`); trial merge of the heads onto main in order: clean

DEPLOYED deploy-2026-10-12-db-apply-prod aa4ca7b2 | set: none | migrations: none | gate: offline 4309/0 · with-DB 5212/0 · live-note 146/0 | RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar | smoke: GREEN | decisions: 0 · for Dejan: 0 · tokens: 210896
