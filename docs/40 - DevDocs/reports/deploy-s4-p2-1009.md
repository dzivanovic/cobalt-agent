# deploy s4-p2-1009 — set: none — migrations: 0024

## §0 Headline
- DEPLOYED: S4-P2 (card 73, F9 delivery) landed alone with migration 0024 (`"user".strike_alerts`), fast-forwarding `79977081` → `975345f3`. Tagged `deploy-2026-10-10-s4-p2`; the rollback tag is `pre-s4-p2-1009`.
- The gate was green on `d4415262`: offline 4188/0 · with-DB 5085/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0`.
- Outage 03:16:55 → 03:24:28 EDT (453 s, mostly the migration's 431 s of proofs). aset and radar were restarted. Smoke is GREEN on every row.
- FOR DEJAN (DECISIONS 2): on the new aset, the strike fallback thread's first pass logged `DbConfigError: Missing Postgres settings for the APP credential`. Whether later passes succeed is unproven, so the phone-fallback DM is unproven until his B5 proof or a build reads it.
- Hub `DEPLOY-HUB.md`, card `2026-10-09/213-deploy-s4-p2-card.md`.

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

### STEP-D2
- D2.0 `git -C /Users/cobalt/cobalt add "docs/40 - DevDocs/reports/deploy-s4-p2-1009.md"` · `commit -m "docs(report): deploy s4-p2-1009 — gate green on d4415262" …` → `[main 79977081] docs(report): deploy s4-p2-1009 — gate green on d4415262`. `show --stat HEAD` → that one file (197+). `rev-parse --short=8 main` → `79977081` = `<pre-merge>`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (only `docs/40 - DevDocs/reports/deploy-s4-p2-1009.md`).
- D2.2 `git -C <GATE> rev-parse --short=8 HEAD` → `975345f3` = `<stack-final>`. `rev-parse --short=8 deploy/s4-p2-1009^2` → `79977081` = `<pre-merge>`; the branch head is `975345f3`. `merge-base --is-ancestor d4415262 deploy/s4-p2-1009` → exit 0.
- D2.3 `git -C /Users/cobalt/cobalt diff --stat d4415262 deploy/s4-p2-1009 -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → (nothing): DOCS-ONLY.
- D2.4 `backup status` → `newest snapshot: 1.7 h old`. `backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 6694.4 MB` · `ssd: snapshot 3c4a4548 — 0 new / 2 changed, 16.5 MB added, 1 pruned` · `F17: com.cobalt.backup DONE`. `backup status` → `newest snapshot: 0.0 h old`. Snapshot id: `3c4a4548`.
- D2.5 `date` → `Sat Oct 10 03:16:39 EDT 2026`. `heartbeat show` → `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-10 03:16:39 EDT)`, 329 s after D1's 03:11:10. The REDs are the same three as `<hb0>` (archiver probe, `com.cobalt.archiver`, `com.cobalt.replay`). The aset, sheet and radar probes are OK: `com.cobalt.aset running loaded, pid 51224`, `com.cobalt.radar running running 99 min, heartbeat fresh`. No new RED.
- D2.6 `date` → `Sat Oct 10 03:16:43 EDT 2026`. `git -C /Users/cobalt/cobalt tag pre-s4-p2-1009` → `rev-parse --short=8 pre-s4-p2-1009` = `79977081`.

### STEP-4 (the outage)
- 4.1 `date` → `Sat Oct 10 03:16:55 EDT 2026` = `<t down>`.
- 4.2 `launchctl bootout gui/501/com.cobalt.aset` → exit 0. `launchctl print gui/501/com.cobalt.aset` → exit 113, `Could not find service "com.cobalt.aset" in domain for user gui: 501`. `launchctl bootout gui/501/com.cobalt.radar` → exit 0. `launchctl print gui/501/com.cobalt.radar` → exit 113, `Could not find service "com.cobalt.radar" in domain for user gui: 501`. The agent is not in the set.
- 4.3 `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `79977081` = `<pre-merge>`. `git -C /Users/cobalt/cobalt merge --ff-only deploy/s4-p2-1009` → `Updating 79977081..975345f3` / `Fast-forward` (48 files changed, 2183 insertions(+), 101 deletions(-)).
- 4.4 `COBALT_ENV=production uv run cobalt db migrate --allow-prod` → `FORWARD on cobalt_brain`, applied in order through `-- applying 0024_strike_alerts.sql`. There were no `uv` sync lines. The proof table has 36 rows `OK` and one `strike_alerts        user    - -> user                  - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED`. Its summary reads `37 table(s) proven; … content UNCHANGED on every table.` · `proof cost: BEFORE 215.8 s + AFTER 215.6 s = total 431.4 s; slowest table radar_score (101.9 s before).` · `SLOTS ok · highest user.aset_sizings 60 of 1600` · `code: 975345f3 (DIRTY: 27 path(s)) · /Users/cobalt/cobalt`. There is no `CHANGED`. The table proof lists the one created table, which matches the card. The index `strike_alerts_seam_at` is not a row of the per-table proof. `<RB>` → `m0024` / `1` = the card's AFTER. `migrations applied: all`.
- 4.5 `COBALT_ENV=production uv run cobalt validate` → exit 0 and `13 trade_def(s) validated OK from the vault.`, with no failing line. `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` and `registry <-> ops/: 15 label(s), exact match.` match `<jobs0>`. `reads:` is now `14 config path(s) re-read at runtime by 3 resident(s)` (was 12): it gains `configs/cobalt/strike.yaml -> com.cobalt.aset` (this set) and `configs/cobalt/notify.yaml -> com.cobalt.aset`.
- 4.6 `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` → exit 0. `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` → exit 0. `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 85816` (≠ 51224). `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 85833` (≠ 51235). `date` → `Sat Oct 10 03:24:28 EDT 2026` = `<t up>`. Downtime 453 s (over 300 s: RECORDS).

### STEP-7 — the deploy row
| item | value |
|---|---|
| landed | `<pre-merge>` `79977081` → `<stack-final>` `975345f3` (fast-forward) |
| tags | `pre-s4-p2-1009` = `79977081` · `deploy-2026-10-10-s4-p2` = `975345f3` (set after the green smoke) |
| outage | `<t down>` 03:16:55 → `<t up>` 03:24:28 EDT = 453 s |
| uv sync | none in production; the gate tree's first `uv run` built its own `.venv` (`Installed 253 packages in 786ms`) |
| proof cost | D1-M `219.8 s`; 4.4 `BEFORE 215.8 s + AFTER 215.6 s = total 431.4 s` |
| migrations applied | all (0024) |
| `<RB>` | before `0` · after `1` |
| snapshot | `3c4a4548` (ssd, D2.4) |
| RESTARTS done | com.cobalt.aset com.cobalt.radar |

THE ROLLBACK STRING (the desk's; never this session's):
1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 975345f3`, with com.cobalt.aset and com.cobalt.radar down first and up after. The card's MIGRATIONS line says the old code runs on 0024: the table is additive, and the old code never reads or writes it.
2. SCHEMA: only as a separate desk job on HIS word, after the code revert: `COBALT_ENV=production uv run cobalt db migrate --allow-prod --rollback --down-to 0023`. It drops `"user".strike_alerts` and every strike alert record. The seam rows in `"user".card_transitions` stay.
3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>`. Git titles it `Reapply "Merge branch 'main' into deploy/s4-p2-1009"`.

## Smoke
- FIRST CALLS after `<t up>`: `<rp_up>` 18 · `<rpr_up>` 60 · `<re_up>` 43 · `<lc_up>` 39 (equal to D1's 18 / 60 / 43 / 39).
- (a) `Sat Oct 10 03:24:47 EDT 2026` · `launchctl print gui/501/com.cobalt.aset` → `state = running`, `pid = 85816` (new, ≠ 51224). `launchctl print gui/501/com.cobalt.radar` → `state = running`, `pid = 85833` (new, ≠ 51235). `/Users/cobalt/cobalt/cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` (the agent is outside the set and keeps the same pid). GREEN.
- (b) `Sat Oct 10 03:24:50 EDT 2026` · `grep -c "Started server process" /Users/cobalt/cobalt/logs/aset.err` → `58` (> 57, ≤ 59). `tail -n 30 /Users/cobalt/cobalt/logs/aset.err` → the last start is `INFO:     Started server process [85822]` · `INFO:     Waiting for application startup.` · `2026-10-10 03:24:25.378 | INFO     | cobalt.voice.web:voice_startup:183 - voice: scratch dir /Users/cobalt/.cobalt/voice-scratch locked by this process; start sweep deleted 0 file(s), 0 failed` · `INFO:     Application startup complete.` · `INFO:     Uvicorn running on http://0.0.0.0:5010 (Press CTRL+C to quit)`. The counts equal the baseline: aset Traceback `2`, radar Traceback `0`, TaxonomyConfigError `0`. The listed checks are GREEN. ALSO IN THAT TAIL, a new line just before the start (see DECISIONS 2): `2026-10-10 03:24:25.092 | ERROR    | cobalt.aset.strike:run:544 - strike fallback: pass failed — the thread goes on: DbConfigError: Missing Postgres settings for the APP credential: POSTGRES_HOST, COBALT_DB_USER, COBALT_DB_PASSWORD. That credential is composed from COBALT_DB_USER and COBALT_DB_PASSWORD (plus POSTGRES_HOST/POSTGRES_PORT, shared). Fail-loud: no default credentials, and NO FALLBACK to the other pair — running the application as the bootstrap superuser because a line is missing from .env is the failure this split exists to prevent.` `grep -c -F "strike fallback: pass failed" /Users/cobalt/cobalt/logs/aset.err` → `1`. `grep -n -F "strike" /Users/cobalt/cobalt/logs/aset.log` → `19047:  strike fallback: tail thread started (DM after strike.yaml dm_after_s)`.
- (c) `Sat Oct 10 03:25:17 EDT 2026` · `curl … http://127.0.0.1:5010/` → `200` · `…/radar` → `200` · `…/radar\?frame=phone` → `200`. Each passed on the first attempt. GREEN.
- (d) `Sat Oct 10 03:25:20 EDT 2026` · `grep -c -F "0024_strike_alerts" /Users/cobalt/cobalt/src/cobalt/db_migrations/__init__.py` → `4` = after. GREEN.
- (g) `Sat Oct 10 03:25:20 EDT 2026` · `<RB>` → `m0024` / `1` = AFTER. GREEN.
- (s) `Sat Oct 10 03:25:20 EDT 2026` · the strike migration registered: `grep -c -F "0024_strike_alerts" /Users/cobalt/cobalt/src/cobalt/db_migrations/__init__.py` → exit 0, `4` (green is 1 or more). GREEN.
- (e) read 1, `heartbeat show` at `2026-10-10 03:25:23 EDT` → `HEARTBEAT RED — 2 job(s) and 1 probe(s)`. The REDs are the same three as `<hb0>` (archiver probe, `com.cobalt.archiver` 429, `com.cobalt.replay`). `OK   com.cobalt.aset              running   loaded, pid 85816 [launchd probe]` · `OK   com.cobalt.radar             running   running 1 min, heartbeat fresh` · `OK   sheet HTTP               http://127.0.0.1:5010/ -> 200` · `OK   radar                    idle (overnight)`. Nothing new. A filler read at `03:25:36 EDT` is the same.
- (b) radar tails (`<t up>` 03:24:28). Tail 1 at `Sat Oct 10 03:26:01 EDT 2026` (+93 s): `tail -n 12 /Users/cobalt/cobalt/logs/radar.err` ends `2026-10-10 03:24:26.770 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None`, which is stamped before `<t up>` and so not counted. The other lines are vault unlock and finviz token lines, with no traceback. Tail 2 at `Sat Oct 10 03:27:30 EDT 2026` (+182 s) ends `2026-10-10 03:26:06.800 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None`. That is a cycle line after `<t up>` with no `radar S5 evaluate FAILED`, no `lifecycle card read failed` and no traceback, so (b) settles GREEN.
- (e) read 2 at `Sat Oct 10 03:27:13 EDT 2026`: `heartbeat show` → `HEARTBEAT RED — 2 job(s) and 1 probe(s)  (2026-10-10 03:27:14 EDT)`, 111 s after read 1 (03:25:23). The REDs are the same three as `<hb0>`. `OK   com.cobalt.radar             running   running 3 min, heartbeat fresh` · `OK   com.cobalt.aset              running   loaded, pid 85816 [launchd probe]`. Nothing new. GREEN.
- (b) tail 3 at `Sat Oct 10 03:29:30 EDT 2026` (+302 s) shows cycle lines at `03:26:06.800`, `03:27:46.829` and `2026-10-10 03:29:26.856 | INFO     | cobalt.radar.runner:resident:638 - radar cycle: idle:overnight scan_id=None`, with no failure line and no traceback. The radar cycles every ~100 s, as at D1. GREEN. At the same time `grep -c "Traceback" /Users/cobalt/cobalt/logs/aset.err` → `2` (baseline) and `grep -c -F "strike fallback: pass failed" …/aset.err` → `1`.
- (h) REVERT-READBACK at `Sat Oct 10 03:27:34 EDT 2026` (+186 s, after (b) settled): `radar panel FAILED` 18 · `radar pool refresh FAILED` 60 · `radar S5 evaluate FAILED` 43 · `lifecycle card read failed` 39. These equal `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (18 / 60 / 43 / 39), so no count grew. `curl … /radar` → `200`. No census reads on the card. GREEN. `grep -c -F "strike fallback: pass failed" /Users/cobalt/cobalt/logs/aset.err` → `1`, unchanged; the thread logs once per distinct message, so this proves nothing about later passes (DECISIONS 2).
- (f) `Sat Oct 10 03:25:28 EDT 2026` · `COBALT_ENV=production uv run cobalt jobs restarts 79977081..975345f3` → exit 0, the same 48 rows as STEP-R with no `UNCLASSIFIED`, and `RESTARTS: com.cobalt.aset com.cobalt.radar` = `<restart set>`. `COBALT_ENV=production uv run cobalt validate` → exit 0 and `13 trade_def(s) validated OK from the vault.`, the same as 4.5. GREEN.

THE CHAIN: every check committed (P2: `s4-p2-check-2026-10-10.md` at `83e32258`, `held unfixed: 0`, `ready: YES`) → the tips re-read (P3: `44cd4e98` = code tip = head) → the merged tree (T: `<m1>` = `d4415262`, one merge, migration paths exactly 0024) → RESTARTS derived (R: `com.cobalt.aset com.cobalt.radar`) → three suites green on `<m1>` (G: offline 4188/0 · with-DB 5085/0 · live-note 146/0, `cobalt_dev: 0013 — F2 = F0`) → `<stack-final>` `975345f3` = `<m1>` + docs (D2.3 empty) → the landed code (4.3 `Updating 79977081..975345f3` Fast-forward) → markers (d: `4`) → the migration read back (g: `1`) → residents up after the merge (a: new pids 85816 / 85833) → radar cycling (b: 03:26:06.800 cycle; e: two reads, nothing new) → the set's reads (s: `4`) → no new failure (h: 18 / 60 / 43 / 39 flat). The card surface (`/strike`, ARM, a live alert) is not readable here. The desk confirms it with him (L70); it is his proof B5.

PRE-STOP SELF-CHECK (K25):
1. Every smoke row is quoted verbatim with its `date`: (a) 03:24:47, (b) 03:24:50 plus the tails at 03:26:01, 03:27:30 and 03:29:30, (c) 03:25:17, (d)/(g)/(s) 03:25:20, (e) 03:25:23 and 03:27:13, (f) 03:25:28, (h) 03:27:34.
2. Every code tip and head was re-read in P3: `44cd4e98` = `44cd4e98`. `git -C /Users/cobalt/cobalt merge-base --is-ancestor 44cd4e98 975345f3` → exit 0, so it is an ancestor of `<stack-final>`.
3. REVERT-READBACK is shown under (h): 18 / 60 / 43 / 39 = the `_up` counts. Every count, sha and `file:line` here was re-read from this run's tool output. `git -C /Users/cobalt/cobalt rev-parse --short=8 deploy-2026-10-10-s4-p2` → `975345f3`.
4. No conflict marker: STEP-T ran clean (`Merge made by the 'ort' strategy.`), as did D2.1. `git -C /Users/cobalt/cobalt status --short --branch` → `## main...origin/main [ahead 83]`, with no `UU`/`AA` line.
THE RELEASE: the gate released the lock at its end (`.env: removed`). Re-read before the stop: `ls -la <GATE>/.env` → `No such file or directory`. This session holds no lock.

## CONTINUE
next: none — DEPLOYED. Earlier entries: OUTAGE ENDED Sat Oct 10 03:24:28 EDT 2026 (residents up, smoke next) · OUTAGE STARTING Sat Oct 10 03:16:43 EDT 2026.

## DECISIONS
1. `.claude/settings.json.bak` (`??`, untracked, at the repo root) was in D0's porcelain. It is on neither the hub's ACCEPTED list nor its REFUSED list (the REFUSED list names dirty `src/`, `tests/`, `ops/`, `configs/` paths). The session-start git status already showed it. Safe default taken: not a stop; it is untracked and never reaches the landed tree (D2.3 empty). ASK DESK: should this path go on the D0 accepted list, or be removed? [Sat Oct 10 03:13 EDT 2026]
2. THE STRIKE FALLBACK'S FIRST PASS FAILED ON THE NEW CODE. `aset.err` `2026-10-10 03:24:25.092 | ERROR    | cobalt.aset.strike:run:544 - strike fallback: pass failed — the thread goes on: DbConfigError: Missing Postgres settings for the APP credential: POSTGRES_HOST, COBALT_DB_USER, COBALT_DB_PASSWORD. …`. `src/cobalt/aset/__main__.py:50-57` starts the thread before `uvicorn.run(...)`. `src/cobalt/aset/strike.py:535-546` logs a failure once per distinct message, so a flat count (1 at 03:24:50, 1 at 03:27:34) does not prove the later passes succeed. If they keep failing, the phone fallback DM never sends. That is unproven (L70), not known and not a defect claim. It is on no RED line of 4.7. The residents, sheet, radar and every listed smoke read are GREEN. Safe default taken: no rollback, deploy closes green. The read that would prove it: an armed strike crossing `dm_after_s` unacknowledged → a `"user".strike_alerts` row with its DM result. That is his B5 proof (open `/strike` on the trading PC, press ARM, see one live alert). ASK DESK, FOR DEJAN: before B5 is relied on for the phone fallback, have a build read whether the fallback thread's DB credential resolves after the server's startup, and fix the order if it does not. [Sat Oct 10 03:28 EDT 2026]

## RECORDS
- DOWNTIME: `<t down>` 03:16:55 → `<t up>` 03:24:28 EDT = 453 s, over 300 s. The migration's proof cost was `BEFORE 215.8 s + AFTER 215.6 s = total 431.4 s` of that, as D1-M forecast (`219.8 s`, paid twice).
- `cobalt_dev: 0013 (F2 = F0)`: the gate's `cobalt_dev: 0013 — F2 = F0` · `forward, back, forward, back — F = F0 twice` · `.env: removed` · `lock released`.
- RETIRE OWED: none (no plist removed).
- THE CARRIED RED, as read: no radar RED of the carried family at D1, D2.5 or smoke. The three standing REDs were archiver and replay, outside the aset, sheet and radar probes. They are unchanged from `<hb0>` to the last read: `RED  archiver                 last run FAILED — last run 2026-10-10 00:54 UTC …`, `RED  com.cobalt.archiver          failed    RuntimeError: 18 archiver failure(s): DKNG/i2: … '429 Too Many Requests' …`, `RED  com.cobalt.replay            failed    ReplayError: archiver not done: state 'failed'`.
- `validate` `reads:` grew 12 → 14 after the merge, adding `configs/cobalt/strike.yaml -> com.cobalt.aset` and `configs/cobalt/notify.yaml -> com.cobalt.aset`. `notify.yaml` is not in this set's diff. Its new reader comes from the strike code's import reach (`start_fallback_thread` imports `cobalt.notify.mattermost`). aset was restarted in this deploy, so no reader is left stale. Information only.
- A command I typed on my own and did not need: `COBALT_ENV=production uv run cobalt heartbeat show radar` → exit 2 `cobalt: error: unrecognized arguments: radar` (the CLI's usage error, not a permission refusal). It was a clock filler; I went on with the listed `heartbeat show`.
- CLEANUP OWED (L46): the gate worktree `/Users/cobalt/cobalt-wt/deploy-s4-p2-1009` and its branch `deploy/s4-p2-1009`; the set's branch `ops/s4-p2-1009` and its worktree, if one exists. The desk owns this cleanup.
- Push is his (L55): `main` is ahead of `origin/main`.
- The card's `## RECORDS`, copied:
  - s4-p2-1009: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/s4-p2-check-2026-10-10.md` last line: CHECK DONE · job: s4-p2-1009 · pass: 1 · tip: 44cd4e98 · house A: Sol FINDINGS: 4 · findings: 9 · dropped: 0 · held: 4 · fixed: 4 · held unfixed: 0 · open: 5 · house B: Grok FINDINGS: 3 · suites: offline 4166/0 · with-DB 5063/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 17 · ready: YES · decisions: 3 · for Dejan: 0 · tokens: 238152
  - s4-p2-1009: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/s4-p2-1009` → `44cd4e98`; code tip `44cd4e98`
  - written by deploy-card.sh at 2026-10-10 02:38 ET (`date`); trial merge of the heads onto main in order: clean
- L74: one harness reminder asked for a `Claude-Session:` commit line. It is recorded under `## L74` and was not acted on.

DEPLOYED deploy-2026-10-10-s4-p2 975345f3 | set: none | migrations: 0024 | gate: offline 4188/0 · with-DB 5085/0 · live-note 146/0 | RESTARTS: com.cobalt.aset com.cobalt.radar | smoke: GREEN | decisions: 2 · for Dejan: 1 · tokens: 249737
