# deploy s4-p2-1009 — set: none — migrations: 0024

## §0 Headline
- S4-P2 (card 73, F9 delivery) deploys alone with migration 0024 (`"user".strike_alerts`). Hub `DEPLOY-HUB.md`, card `2026-10-09/213-deploy-s4-p2-card.md`.

## L74
- A harness system reminder at session start asked that commits end with a `Claude-Session: https://claude.ai/code/session_01SQaRij9FaUMahppwTvmXWh` line. Recorded as data. Not acted on: under L74, commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/213-deploy-s4-p2-card.md"`, exit 0, output in full:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/213-deploy-s4-p2-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/213-deploy-s4-p2-card.md" · 0 · 3eca9ef6c4e4ccce1fcc6465e8c1290345fbb985
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/213-deploy-s4-p2-card.md" · 0 · nothing
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
| first launch | `ls -la ".../reports/deploy-s4-p2-1009.md"` | 1 | No such file or directory |
| P0 | `authorize.sh deploy <card>` | 0 | `AUTHORIZED` (above) |
| P1 | `date` | 0 | `Sat Oct 10 02:38:58 EDT 2026` (L43: any hour) |
| P2 | `tail -n 3 ".../s4-p2-check-2026-10-10.md"` | 0 | `CHECK DONE · job: s4-p2-1009 · pass: 1 · tip: 44cd4e98 · … · held unfixed: 0 · … · suites: offline 4166/0 · with-DB 5063/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 17 · ready: YES · decisions: 3 · for Dejan: 0 · tokens: 238152`. Has `held unfixed: 0` and `ready: YES`; `tip: 44cd4e98` = the code tip |
| P2 | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/s4-p2-check-2026-10-10.md"` | 0 | `83e32258e7f3bd50a0072c04c686d09b6c9c2961` |
| P2 | `git -C /Users/cobalt/cobalt diff --stat -- "<check>"` | 0 | (nothing) |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 44cd4e98` | 0 | `44cd4e98` |
| P3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/s4-p2-1009` | 0 | `44cd4e98` (= TIP) |
| P3 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 44cd4e98 ops/s4-p2-1009` | 0 | — |
| P3 | `git -C /Users/cobalt/cobalt diff --stat 44cd4e98 ops/s4-p2-1009 -- . ':(exclude)docs'` | 0 | (nothing) |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env`: no lock holder |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/s4-p2-1009` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `3eca9ef6` = `<m0>` |
| P5 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 3eca9ef6 main` | 0 | — |
| P5 | `git -C /Users/cobalt/cobalt log --oneline main..deploy/s4-p2-1009` | 0 | (empty) |
| P6 | `grep -c -F "0024_strike_alerts" /Users/cobalt/cobalt/src/cobalt/db_migrations/__init__.py` | 1 | `0` = before |
| P7 | `git -C /Users/cobalt/cobalt diff --stat main 44cd4e98 -- src/cobalt/db_migrations` | 0 | `0024_strike_alerts.rollback.sql` 5+, `0024_strike_alerts.sql` 32+, `__init__.py` 6+, `placement.py` 3+ (code) |
| P7 | `git -C /Users/cobalt/cobalt diff main 44cd4e98 -- src/cobalt/db_migrations/__init__.py` | 0 | FORWARD gains `MIGRATIONS_DIR / "0024_strike_alerts.sql",` at its end. REVERSE gains `MIGRATIONS_DIR / "0024_strike_alerts.rollback.sql",` at its start. Every other changed line is docstring. Only the card's 0024 |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · `state = running` · `pid = 51224` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` · `state = running` · `pid = 51235` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit 44cd4e98` → `Merge made by the 'ort' strategy.` (48 files changed, 2183 insertions(+), 101 deletions(-)).
- `git -C <GATE> rev-parse --short=8 HEAD` → `d4415262` = `<m1>`.
- `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 3eca9ef6..deploy/s4-p2-1009` → `d4415262 Merge commit '44cd4e98' into deploy/s4-p2-1009` (one line, one head).
- `git -C /Users/cobalt/cobalt merge-base --is-ancestor 44cd4e98 deploy/s4-p2-1009` → exit 0.
- `git -C /Users/cobalt/cobalt diff --stat 3eca9ef6 deploy/s4-p2-1009 -- src/cobalt/db_migrations` → `0024_strike_alerts.rollback.sql` 5+, `0024_strike_alerts.sql` 32+, `__init__.py` 6+, `placement.py` 3+ (code). The migration paths are exactly 0024 and its registry.
- `git -C /Users/cobalt/cobalt diff 3eca9ef6 deploy/s4-p2-1009 -- src/cobalt/db_migrations/__init__.py` → the same hunks as P7: FORWARD gains `0024_strike_alerts.sql` and REVERSE gains `0024_strike_alerts.rollback.sql`.
- `grep -n -F 'MIGRATIONS_DIR / "' <GATE>/src/cobalt/db_migrations/__init__.py` → FORWARD ends `168:    MIGRATIONS_DIR / "0024_strike_alerts.sql",` and REVERSE begins `173:    MIGRATIONS_DIR / "0024_strike_alerts.rollback.sql",`.
- STEP-C: `git -C /Users/cobalt/cobalt diff --stat 3eca9ef6 deploy/s4-p2-1009 -- configs ops` → in full:
```
 configs/cobalt/jobs.yaml   | 18 +++++++++++-------
 configs/cobalt/strike.yaml | 15 +++++++++++++++
 ops/desk/gate-lists.md     |  4 ++--
 3 files changed, 28 insertions(+), 9 deletions(-)
```
  No plist was added, modified or removed, so no `RETIRE OWED`.

## RESTARTS
`cd <GATE>` · `ls -la <GATE>/.env` → `No such file or directory` · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0. The `uv` lines: `Creating virtual environment at: .venv` · `Built cobalt-agent @ file:///Users/cobalt/cobalt-wt/deploy-s4-p2-1009` · `Installed 253 packages in 786ms`. The table, in full:
```
path	change	rule	restart
configs/cobalt/jobs.yaml	M	registry; register, no restart	-
configs/cobalt/strike.yaml	A	resident reads	com.cobalt.aset
docs/40 - DevDocs/cobalt/aset/__main__.md	M	DOCS	-
docs/40 - DevDocs/cobalt/aset/strike.md	A	DOCS	-
docs/40 - DevDocs/cobalt/aset/web.md	M	DOCS	-
docs/40 - DevDocs/cobalt/db_migrations/__init__.md	M	DOCS	-
docs/40 - DevDocs/cobalt/db_migrations/placement.md	M	DOCS	-
docs/40 - DevDocs/cobalt/strike/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/strike/delivery_config.md	A	DOCS	-
docs/40 - DevDocs/cobalt/strike/week.md	A	DOCS	-
docs/40 - DevDocs/reports/s4-p2-build-2026-10-09.md	A	DOCS	-
ops/desk/gate-lists.md	M	operator script; no Cobalt reader	-
src/cobalt/aset/__main__.py	M	static import reach	com.cobalt.aset
src/cobalt/aset/strike.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/aset/web.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/db_migrations/0024_strike_alerts.rollback.sql	A	non-Python src asset	-
src/cobalt/db_migrations/0024_strike_alerts.sql	A	non-Python src asset	-
src/cobalt/db_migrations/__init__.py	M	static import reach	com.cobalt.radar
src/cobalt/db_migrations/placement.py	M	static import reach	com.cobalt.radar
src/cobalt/strike/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/strike/delivery_config.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/strike/week.py	A	static import reach	com.cobalt.radar
tests/cobalt/test_archiver_migrations.py	M	test/documentation; no resident	-
tests/cobalt/test_assumed_store.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_d2_fix_r1_db.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_d3_experiments.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_k1_store.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_store.py	M	test/documentation; no resident	-
tests/cobalt/test_f15_p1_records_offline.py	M	test/documentation; no resident	-
tests/cobalt/test_jobs_reads.py	M	test/documentation; no resident	-
tests/cobalt/test_jobs_restarts.py	M	test/documentation; no resident	-
tests/cobalt/test_legs_migration.py	M	test/documentation; no resident	-
tests/cobalt/test_p4_migrations.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_handicap_store.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_migration.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_price_floor_db.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_score_migration.py	M	test/documentation; no resident	-
tests/cobalt/test_seam_drc_s3_registry.py	M	test/documentation; no resident	-
tests/cobalt/test_stale_score_db.py	M	test/documentation; no resident	-
tests/cobalt/test_strike_ack_db.py	A	test/documentation; no resident	-
tests/cobalt/test_strike_config.py	M	test/documentation; no resident	-
tests/cobalt/test_strike_fallback.py	A	test/documentation; no resident	-
tests/cobalt/test_strike_stream.py	A	test/documentation; no resident	-
tests/cobalt/test_strike_stream_db.py	A	test/documentation; no resident	-
tests/cobalt/test_strike_week.py	A	test/documentation; no resident	-
tests/cobalt/test_tenancy.py	M	test/documentation; no resident	-
tests/cobalt/test_voice_store.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
GATE: exit 0 with no `UNCLASSIFIED` row, and the set falls within the three allowed labels. `<restart set>` = `com.cobalt.aset com.cobalt.radar`. That equals the check's stop line. A migration with a non-empty set passes L66.

## L68 GATE
- EQUAL-TREE CLAUSE: `git -C /Users/cobalt/cobalt diff --stat 44cd4e98 d4415262 -- . ":(exclude)docs"` → `src/cobalt/archiver/collector.py`, `report.py`, `runner.py` and three archiver tests (6 files, 484+/10−): this is main's archiver-429, which landed after the check's tip. The clause does not hold, so the gate runs whole.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `263 passed, 163 skipped in 16.64s`. 0 failed, and every skip is a with-DB skip (`Postgres env settings not available` / `requires_db`).
- Deselects: none. The build report `s4-p2-build-2026-10-09.md:161` says: "The gate call carried no `--deselect`: the two new with-DB files are in `gate-lists.md` PASS 1 / PASS 2 (W1)". `TICKERS: none`, so `--tickers` is omitted. With migration 0024 the call carries `--migration`.
- THE GATE: `ls -la <GATE>/.env` → No such file · `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-s4-p2-1009 all --deploy --migration` → exit 0. Verdict lines in full:
```
offline 4188/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
forward, back, forward, back — F = F0 twice
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5085/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-s4-p2-1009-all-20261010-024102.log
```
- (a) OFFLINE → `offline 4188/0`. Log line 879: `4188 passed, 800 skipped, 1 xfailed, 36 warnings in 637.29s (0:10:37)`.
- (b) lock taken (`lock: waited 0 min`), `LEVEL 0013`, proof-only with no `CHANGED` (log 942: `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`).
- (c) PASS 1 at 0013, whole. Log 1107: `4880 passed, 7 skipped, 99 deselected, 3 xfailed, 43 warnings in 781.60s (0:13:01)` → `<d1>` = 4880. All seven SKIPPED lines are in the allowed set: `test_cards_picks.py:388` and `:401`, `test_radar_evaluate.py:695`, the `test_replay_line.py` skip whose reason names `COBALT_TEST_LIVE_DRC`, `test_s3_c4_experiments.py:95` (the decorator line of `test_x14_live_his_template_strips_to_the_committed_fixture`, read at `<GATE>/tests/cobalt/test_s3_c4_experiments.py:95-96`), `test_catalyst.py:365` and `test_predicate.py:262`.
- (c2) FORWARD. Log 1109: `dev forward: APPLIED 03:05:06`. The log shows `-- applying 0024_strike_alerts.sql` last (log 1135). Every content proof reads `content UNCHANGED on every table`, and `grep -n -F "CHANGED" <log>` finds no `CHANGED` verdict.
- (c3) PASS 2. Log 1961: `205 passed, 1 deselected, 5 warnings in 229.37s (0:03:49)` → `<d2>` = 205. `with-DB 5085/0` = 4880 + 205.
- (c4) forward and rollback again: `forward, back, forward, back — F = F0 twice`. Log 2218: `F (c4): 664 35 272c95bbb12241e3611e4b36326ccf87`.
- (f) `cobalt_dev: 0013 — F2 = F0`.
- THE RELEASE: log 2221–2226: `sh /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh deploy-s4-p2-1009` → `lock released` · `.env: removed`. The log carries no clock time for the release. The gate's completion notice and the `date` read after it give `Sat Oct 10 03:10:37 EDT 2026`. Verified afterwards: `ls -la <GATE>/.env` → No such file. `grep -c -x -F "deploy-s4-p2-1009" /Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` → `No such file or directory`, so no lock is held.
- (e) LIVE-NOTE → `live-note 146/0`. Log 2291: `146 passed, 1 skipped, 15 warnings in 25.00s`. No skip names `COBALT_LIVE_VAULT_ROOT` in the live-note leg.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on d4415262

## Deploy table
### STEP-D0
| rule | command | exit | result |
|---|---|---|---|
| MAIN | `git -C /Users/cobalt/cobalt status --short --branch` | 0 | first line `## main...origin/main [ahead 74]` |
| MAIN | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | Nothing is staged. The ` M` lines are `.claude/settings.json` and six files under `docs/40 - DevDocs/reports/`. The `??` lines are under `docs/40 - DevDocs/`, plus `.claude/settings.json.bak` (see DECISIONS). No dirty `src/`, `tests/`, `ops/` or `configs/` path |
| MAIN | `git -C /Users/cobalt/cobalt diff --stat 3eca9ef6 main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | (nothing) |
| PROBE | `tag scratch-allow-probe-s4-p2-1009` / `tag -d …` | 0 / 0 | `Deleted tag 'scratch-allow-probe-s4-p2-1009' (was 3eca9ef6)` |
| PROBE | `commit --allow-empty -m "scratch: allowlist probe (reverted next line)"` | 0 | `[main e824da71] scratch: allowlist probe (reverted next line)` |
| PROBE | `reset --soft HEAD~1` → `log --oneline -1` | 0 / 0 | `3eca9ef6 docs(desk): S4-P2 card 213 written, check done (R825)`: HEAD is back |
| TAGS | `rev-parse --verify --quiet refs/tags/deploy-2026-10-10-s4-p2` | 1 | free |
| TAGS | `rev-parse --verify --quiet refs/tags/pre-s4-p2-1009` | 1 | free |

### STEP-D1 (baseline, read-only)
- `date` → `Sat Oct 10 03:11:09 EDT 2026`.
- `<hb0>` = `COBALT_ENV=production uv run cobalt heartbeat show` → `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-10 03:11:10 EDT)`. The aset, sheet and radar probes are all OK: `OK   sheet HTTP               http://127.0.0.1:5010/ -> 200` · `OK   sheet daymode            day mode reduced · stage 1 (system rule, pre-09:00) · half sheet — cards are accepted` · `OK   radar                    idle (overnight)` · `OK   com.cobalt.aset              running   loaded, pid 51224 [launchd probe]` · `OK   com.cobalt.agent             running   pid 22243 alive (from /Users/cobalt/cobalt/logs/cobalt.pid) [pidfile probe]` · `OK   com.cobalt.radar             running   running 94 min, heartbeat fresh`. The REDs are named here and do not stop the run:
  - `RED  archiver                 last run FAILED — last run 2026-10-10 00:54 UTC (6.3 h ago), rows written 3308843, exit 1`
  - `RED  com.cobalt.archiver          failed    RuntimeError: 18 archiver failure(s): DKNG/i2: Fetch failed for DKNG/i2: Finviz HTTP failed: Client error '429 Too Many Requests' for url 'https://elite.finviz.com/export/stock?t=DKNG&p=i2&auth=[REDACTED:url_query_secret]'`
  - `RED  com.cobalt.replay            failed    ReplayError: archiver not done: state 'failed'` (followed by a traceback in the probe text)
  - `AMB  com.cobalt.herdr             unmanaged AMBER launchd unmanaged — loaded, not running (last exit 0) [launchd probe]; runs outside launchd by declared interim (`launchd_unmanaged` in configs/cobalt/jobs.yaml)`
  No radar RED of the carried family appears.
- `<val0>` = `COBALT_ENV=production uv run cobalt validate` → exit 0 and `13 trade_def(s) validated OK from the vault.`, with no `docs/_inflight/` line. `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` · `registry <-> ops/: 15 label(s), exact match.` · `reads: 12 config path(s) re-read at runtime by 3 resident(s); every path exists, every one-shot empty.` Last line: `Placement (docs/PLACEMENT.md): tree clean.`
- `COBALT_ENV=production uv run cobalt backup status` → `newest snapshot: 1.6 h old`.
- `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 51224` = `<aset pid>`. `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 51235` = `<radar pid>`. `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` `ps -p 22243` → `22243 ??         0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 /Users/cobalt/cobalt/logs/radar.err` → eight `radar cycle: idle:overnight scan_id=None` lines, 02:59:14.613 to `2026-10-10 03:10:54.769 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None`, with no traceback.
- LOG BASELINES: `<a0>` Started server process = 57 · `<ta0>` aset Traceback = 2 · `<tr0>` radar Traceback = 0 · `<tc0>` TaxonomyConfigError = 0 · `<rp0>` radar panel FAILED = 18 · `<rpr0>` radar pool refresh FAILED = 60 · `<re0>` radar S5 evaluate FAILED = 43 · `<lc0>` lifecycle card read failed = 39.
- `curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/radar` → `200`.
- MARKER `grep -c -F "0024_strike_alerts" /Users/cobalt/cobalt/src/cobalt/db_migrations/__init__.py` → `0` (before).
- `<RB>` BEFORE → `m0024` / `0` = the card's BEFORE. The card marks no SMOKE READS line `census`.
- D1-M `COBALT_ENV=production uv run cobalt db migrate --allow-prod --proof-only` → exit 0. It probed 36 tables on cobalt_brain, with no `CHANGED`. Its lines: `Proof cost: total 219.8 s — and a migration pays it TWICE (before and after), inside the outage.` · `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.` · `SLOTS ok · highest user.aset_sizings 60 of 1600` · `code: 3eca9ef6 (DIRTY: 27 path(s)) · /Users/cobalt/cobalt` · `FINGERPRINT cols 893 · rels 44 · views_md5 126f2d6983fa59f9d0eaaff7da7dd29c` · `TABLES 0022`. Four info lines follow the `NOTHING WAS APPLIED` line, the same shape as the gate log's proof-only. `TABLES 0022` names the newest table-creating migration; 0023 adds a column and a CHECK and creates no table. The gate's `TABLES 0011` at level 0013 reads the same way.

## CONTINUE
next: STEP-D2

(run in progress — next step under ## CONTINUE)
