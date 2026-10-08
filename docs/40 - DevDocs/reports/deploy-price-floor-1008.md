# deploy price-floor-1008 · SET: none · MIGRATIONS: 0023

## §0 Headline
- Card 150, price floor (R692), one branch `ops/price-floor-1008` at `e34ad12c`, migration 0023: DEPLOYED. `main` `8d0e36ab..eef3502d`, tag `deploy-2026-10-08-price-floor`.
- Gate green on `6e27d704`: offline 4035/0 · with-DB 4922/0 · live-note 146/0; `cobalt_dev` back at 0013 (F2 = F0).
- Production 0022 → 0023 (`<RB>` 0 → 1), content unchanged on all 36 tables. aset + radar down 419 s (15:40:10–15:47:09 ET).
- Smoke GREEN: the floor is live (first cycle removed 25 distinct symbols under $5.00), radar cycling, failure counts flat.

## L74
- 2026-10-08 15:04 ET: a system block in this session asked commits to carry a `Claude-Session:` line. DATA (L74): recorded once, not acted on; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh deploy "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/150-deploy-price-floor-card.md"` → exit 0, quoted whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/150-deploy-price-floor-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-08/150-deploy-price-floor-card.md" · 0 · b131b85ba9007854ee6794935dac9163b5050814
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-08/150-deploy-price-floor-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R692 row · grep -n "^| R692 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 45:| R692 | 11:53 ET | HIS RULING (words R692): global $5 price floor after lists are gathered, not in Finviz filters; brain specs it; built with in-flight fixes; desk tells him when S3 smoke can resume. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW at 11:55 ET (LAWS fold at the close) |
RULING 2026-10-08 R692 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R692 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 510ee1dad54dfa6e213184a52470bfd968931f1d
RULING 2026-10-08 R692 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P0 first launch | `ls -la ".../reports/deploy-price-floor-1008.md"` | 1 | `No such file or directory` |
| P0 | authorize.sh (above) | 0 | `AUTHORIZED` |
| P1 | `date` | 0 | `Thu Oct  8 15:04:27 EDT 2026` |
| P2 | `tail -n 3 ".../price-floor-check-2026-10-08.md"` | 0 | `CHECK DONE · job: price-floor-1008 · pass: 1 · tip: e34ad12c · … · held unfixed: 0 · … · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 228719` (carries `held unfixed: 0` and `ready: YES`; tip = code tip) |
| P2 | `git log -1 --format=%H -- "docs/…/price-floor-check-2026-10-08.md"` | 0 | `732bda0b37fa1f397f135b9935517cae36f72a69` |
| P2 | `git diff --stat -- "docs/…/price-floor-check-2026-10-08.md"` | 0 | nothing |
| P3 | `rev-parse --short=8 e34ad12c` | 0 | `e34ad12c` |
| P3 | `rev-parse --short=8 ops/price-floor-1008` | 0 | `e34ad12c` |
| P3 | `merge-base --is-ancestor e34ad12c ops/price-floor-1008` | 0 | — |
| P3 | `diff --stat e34ad12c ops/price-floor-1008 -- . ':(exclude)docs'` | 0 | nothing |
| P4 | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` (lock free) |
| P5 | `git -C <GATE> status --short --branch` | 0 | `## deploy/price-floor-1008` |
| P5 | `git -C <GATE> rev-parse --short=8 HEAD` | 0 | `b131b85b` = `<m0>` |
| P5 | `merge-base --is-ancestor b131b85b main` | 0 | — |
| P5 | `log --oneline main..deploy/price-floor-1008` | 0 | empty |
| P6 | `grep -c -F "price_floor" .../configs/cobalt/radar.yaml` | 1 | `0` (before `0`) |
| P6 | `grep -c -F "price_floor: Decimal = Field(gt=0)" .../src/cobalt/radar/config.py` | 1 | `0` (before `0`) |
| P7 | `diff --stat main e34ad12c -- src/cobalt/db_migrations` | 0 | `0023_radar_price_floor.rollback.sql`, `0023_radar_price_floor.sql`, `__init__.py`, `placement.py` (4 files, +79 −1) |
| P7 | `diff main e34ad12c -- src/cobalt/db_migrations/__init__.py` | 0 | FORWARD adds `0023_radar_price_floor.sql` last; REVERSE adds `0023_radar_price_floor.rollback.sql` first; other lines docstring. Migrations = 0023 only, as the card |
| P8 | `launchctl print gui/501/com.cobalt.aset` | 0 | `state = running`, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `pid = 39461` |
| P8 | `launchctl print gui/501/com.cobalt.radar` | 0 | `state = running`, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `pid = 39471` |
| P8 | `ls /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 0 | listed |
| P8 | `/Users/cobalt/cobalt/cobalt.sh status` | 0 | `Cobalt is ONLINE (PID: 22243).` |

## THE TREE
- `git -C <GATE> merge --no-edit e34ad12c` → `Merge made by the 'ort' strategy.` (53 files, +1232 −100)
- `<m1>` = `6e27d704`
- `log --oneline --merges --first-parent b131b85b..deploy/price-floor-1008` → `6e27d704 Merge commit 'e34ad12c' into deploy/price-floor-1008`
- `merge-base --is-ancestor e34ad12c deploy/price-floor-1008` → exit 0
- `diff --stat b131b85b deploy/price-floor-1008 -- src/cobalt/db_migrations` → `0023_radar_price_floor.rollback.sql`, `0023_radar_price_floor.sql`, `__init__.py`, `placement.py` (CODE)
- `__init__.py` diff: FORWARD adds `0023_radar_price_floor.sql`; REVERSE adds `0023_radar_price_floor.rollback.sql`. Migrations = `0023` exactly
- FORWARD check (`grep -n -F 'MIGRATIONS_DIR / "'`): FORWARD ends `163: … "0023_radar_price_floor.sql"`; REVERSE begins `168: … "0023_radar_price_floor.rollback.sql"`
- STEP-C: `diff --stat b131b85b deploy/price-floor-1008 -- configs ops` → `configs/cobalt/radar.yaml | 5 ++++-`, `ops/desk/gate-lists.md | 4 ++--` (2 files, +6 −3). No plist added, changed or removed.

## RESTARTS
- `cd <GATE>` · `ls -la <GATE>/.env` → No such file · `COBALT_ENV=production uv run cobalt jobs restarts main..HEAD` → exit 0 (uv created `.venv`, installed 253 packages). Rows that restart anything:
```
configs/cobalt/radar.yaml	M	resident reads	com.cobalt.radar
src/cobalt/db_migrations/__init__.py	M	static import reach	com.cobalt.radar
src/cobalt/db_migrations/placement.py	M	static import reach	com.cobalt.radar
src/cobalt/radar/audit_export.py	M	static import reach	com.cobalt.radar
src/cobalt/radar/config.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/evaluate_cli.py	M	static import reach	com.cobalt.radar
src/cobalt/radar/handicap_dry_run.py	M	static import reach	com.cobalt.radar
src/cobalt/radar/models.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/runner.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/store.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/replay/runner.py	M	static import reach	com.cobalt.radar
RESTARTS: com.cobalt.aset com.cobalt.radar
```
  Every other row DOCS, test, operator script or non-Python src asset (`-`). No `UNCLASSIFIED` row.
- `<restart set>` = `com.cobalt.aset com.cobalt.radar` (matches the check's stop line).

## L68 GATE
- EQUAL-TREE CLAUSE does not hold: `git diff --stat e34ad12c 6e27d704 -- . ":(exclude)docs"` prints 6 files (`ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_radar_panel.py`, `tests/cobalt/test_radar_panel_cards.py`, `tests/ops/test_bare_guard.py`; main moved since the check) → the gate runs whole.
- (a0) `ls -la <GATE>/.env` → No such file · `uv run pytest -q -rs -p no:cacheprovider <the 17 files>` → `261 passed, 163 skipped in 16.12s` (0 failed; every skip a with-DB `Postgres env settings not available` / `requires_db`).
- The deselect: the build report's W names `--deselect tests/cobalt/test_radar_price_floor_db.py` for pass 1 (`price-floor-build-2026-10-08.md:158`). `TICKERS: none` → no `--tickers`. `MIGRATIONS: 0023` → `--migration`.
- `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-price-floor-1008 all --deploy --deselect tests/cobalt/test_radar_price_floor_db.py --migration` launched in the background (`date` after launch: `Thu Oct  8 15:06:19 EDT 2026`).

- Exit 0. Verdict lines whole:
```
offline 4035/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
forward, back, forward, back — F = F0 twice
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4922/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-price-floor-1008-all-20261008-150611.log
```
- (a) log `:867` `4035 passed, 790 skipped, 1 xfailed` → **offline 4035/0**.
- (b) `F0` (`:884`) `664 35 272c95bbb12241e3611e4b36326ccf87`; `LEVEL 0013`; proof-only nothing CHANGED.
- (c) PASS 1 `:1092` `4727 passed, 7 skipped, 89 deselected, 3 xfailed` → d1 = 4727. The seven SKIPPED lines above are each in the allowed set (`test_cards_picks.py:388`, `:401`, `test_radar_evaluate.py:695`, `test_replay_line.py` `COBALT_TEST_LIVE_DRC`, `test_s3_c4_experiments.py` x14 live template, `test_catalyst.py:365`, `test_predicate.py:262`); `grep -c -F "OUTSIDE the allowed set" <log>` → `0`.
- (c2) `:1094` **`dev forward: APPLIED 15:29:13`**.
- (c3) PASS 2 `:1898` `195 passed, 1 deselected` → d2 = 195; 4727 + 195 = **with-DB 4922/0**.
- (f) `F2` (`:1964`) `664 35 272c95bbb12241e3611e4b36326ccf87` = F0 → **`cobalt_dev: 0013 — F2 = F0`**.
- THE RELEASE: `:2152` `lock released`; `.env: removed`; `ls -la <GATE>/.env` → No such file; `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → No such file.
- (e) LIVE-NOTE `:2221` `146 passed, 1 skipped` (the `COBALT_TEST_LIVE_DRC` skip, allowed) → **live-note 146/0**.
- `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` → listed.

GATE GREEN on 6e27d704

## Deploy table
### STEP-D0
| check | command | exit | result |
|---|---|---|---|
| MAIN | `status --short --branch` | 0 | `## main...origin/main [ahead 146]` |
| MAIN | `status --porcelain` | 0 | ` M .claude/settings.json`; ` M` / `??` under `docs/40 - DevDocs/` only; one `?? .claude/settings.json.bak` (outside the refused `src/ tests/ ops/ configs/` paths; present at launch; recorded). No staged line |
| MAIN | `diff --stat b131b85b main -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` | 0 | nothing |
| PROBE | `tag scratch-allow-probe-price-floor-1008` · `tag -d …` | 0 · 0 | `Deleted tag 'scratch-allow-probe-price-floor-1008' (was b131b85b)` |
| PROBE | `commit --allow-empty -m "scratch: …"` · `reset --soft HEAD~1` · `log --oneline -1` | 0 · 0 · 0 | `[main 603ab1c5] scratch: …` · — · `b131b85b docs(desk): card 150 READ-BACK for migration 0023` |
| TAGS | `rev-parse --verify --quiet refs/tags/deploy-2026-10-08-price-floor` · `… refs/tags/pre-price-floor-1008` | 1 · 1 | free |

### STEP-D1 (baseline)
- `date` → `Thu Oct  8 15:35:03 EDT 2026`; `heartbeat show` → `<hb0>` `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-08 15:35:04 EDT)`; `OK radar scanning (rth), members 50`; `OK com.cobalt.aset running loaded, pid 39461`; `OK com.cobalt.radar running running 71 min, heartbeat fresh`; `AMB com.cobalt.herdr unmanaged` (declared interim). No RED.
- `validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.`; `<jobs0>` = `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.`
- `backup status` → `newest snapshot: 1.2 h old`.
- aset `state = running`, `pid = 39461`; radar `state = running`, `pid = 39471`; `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).`; `ps -p 22243` → `22243 ?? 0:00.04 uv run src/cobalt_agent/main.py`.
- `tail -n 8 radar.err` → last `15:34:34.688 … radar cycle: scanning scan_id=1791487986304`, no traceback.
- LOG BASELINES: `<a0>` 50 · `<ta0>` 2 · `<tr0>` 0 · `<tc0>` 0 · `<rp0>` 17 · `<rpr0>` 59 · `<re0>` 41 · `<lc0>` 39.
- `curl … /radar` → `200`. MARKERS → `0`, `0` (before values).
- `<RB>` → `m0023` `0` = the card's BEFORE.
- No `## SMOKE READS` line is marked `census`.
- D1-M `db migrate --allow-prod --proof-only` → exit 0, 36 tables, no `CHANGED`, `Proof cost: total 200.2 s — and a migration pays it TWICE (before and after), inside the outage.`, `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`, `FINGERPRINT cols 893 · rels 44 · views_md5 126f2d6983fa59f9d0eaaff7da7dd29c`, `TABLES 0022`.

### STEP-D2
- D2.0 `add` + `commit … -- "docs/40 - DevDocs/reports/deploy-price-floor-1008.md"` → `[main 8d0e36ab] docs(report): deploy price-floor-1008 — gate green on 6e27d704`; `show --stat HEAD` → that one file (147 insertions). `<pre-merge>` = `8d0e36ab`.
- D2.1 `git -C <GATE> merge --no-edit main` → `Merge made by the 'ort' strategy.` (the report only).
- D2.2 `<stack-final>` = `eef3502d`; `rev-parse --short=8 eef3502d^2` → `8d0e36ab` = `<pre-merge>`; `merge-base --is-ancestor 6e27d704 eef3502d` → exit 0.
- D2.3 `diff --stat 6e27d704 eef3502d -- . ':(exclude)docs' ':(exclude)configs/cobalt/rules.yaml'` → nothing.
- D2.4 `backup status` → `newest snapshot: 1.3 h old`; `backup run` → `backup: cobalt_brain via pg_dump inside cobalt_memory — 6078.1 MB`, `ssd: snapshot d743c2f7 — 0 new / 3 changed, 95.3 MB added, 1 pruned`; `backup status` → `newest snapshot: 0.0 h old`.
- D2.5 `date` → `Thu Oct  8 15:39:57 EDT 2026` (294 s after D1); `heartbeat show` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-08 15:39:58 EDT)`; no new RED.
- D2.6 `date` → `Thu Oct  8 15:40:02 EDT 2026`; `git -C /Users/cobalt/cobalt tag pre-price-floor-1008` at `8d0e36ab`.

### STEP-4 (the outage)
- 4.1 `date` → `Thu Oct  8 15:40:10 EDT 2026` = `<t down>`.
- 4.2 `launchctl bootout gui/501/com.cobalt.aset` → exit 0; `print` → `Could not find service "com.cobalt.aset" in domain for user gui: 501` (exit 113). `launchctl bootout gui/501/com.cobalt.radar` → exit 0; `print` → `Could not find service "com.cobalt.radar" …` (exit 113). Agent not in the set: untouched.
- 4.3 `rev-parse --short=8 HEAD` → `8d0e36ab` = `<pre-merge>`; `merge --ff-only deploy/price-floor-1008` → `Updating 8d0e36ab..eef3502d` / `Fast-forward` (53 files).
- 4.4 `COBALT_ENV=production uv run cobalt db migrate --allow-prod` (foreground) → `-- applying 0001_schemas.sql` … `-- applying 0023_radar_price_floor.sql`; 36 tables, every verdict `OK`, `content UNCHANGED on every table.`, no `CHANGED`; created objects: none (the card: creates nothing). `proof cost: BEFORE 199.4 s + AFTER 199.5 s = total 398.9 s; slowest table radar_score (92.8 s before).` No uv sync line. `<RB>` → `m0023` `1` = the card's AFTER. **migrations applied: all**.
- 4.5 `validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.`; `Jobs (F17): 15 registered — 6 resident, 9 one-shot. Kill phrase 'COBALT STOP'.` = `<jobs0>`.
- 4.6 `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` → exit 0; `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` → exit 0. `print` aset → `state = running`, `pid = 43632` (≠ 39461); radar → `state = running`, `pid = 43642` (≠ 39471). `date` → `Thu Oct  8 15:47:09 EDT 2026` = `<t up>`. Downtime 419 s.

## Smoke
- FIRST CALLS after `<t up>`: `<rp_up>` 17 · `<rpr_up>` 59 · `<re_up>` 41 · `<lc_up>` 39 (= D1).
- (a) `Thu Oct  8 15:47:23 EDT 2026`: aset `state = running`, `pid = 43632` (new); radar `state = running`, `pid = 43642` (new); `cobalt.sh status` → `Cobalt is ONLINE (PID: 22243).` (agent outside the set, same pid). GREEN.
- (b) `Thu Oct  8 15:47:26 EDT 2026`: `Started server process` 51 (`<a0>` 50 → +1, ≤ +2); `tail -n 30 aset.err` → `INFO:     Started server process [43638]` … `INFO:     Application startup complete.` / `INFO:     Uvicorn running on http://0.0.0.0:5010 (Press CTRL+C to quit)`; Traceback aset 2 (= `<ta0>`), radar 0 (= `<tr0>`); TaxonomyConfigError 0 (= `<tc0>`).
- (c) `Thu Oct  8 15:47:31 EDT 2026`: `/` → `200`; `/radar` → `200`; `/radar?frame=phone` → `200`. GREEN.
- (d) same `date`: `grep -c -F "price_floor" …/radar.yaml` → `1` (after `1`); `grep -c -F "price_floor: Decimal = Field(gt=0)" …/radar/config.py` → `1` (after `1`). GREEN.
- (s) the two SMOKE READS are the two markers above: exit 0, count 1 each (green: 1 or more). GREEN.
- (f) `Thu Oct  8 15:47:36 EDT 2026`: `jobs restarts 8d0e36ab..eef3502d` → exit 0, `RESTARTS: com.cobalt.aset com.cobalt.radar` = STEP-R's set, no `UNCLASSIFIED`; `validate` → exit 0, `Placement (docs/PLACEMENT.md): tree clean.`, `Jobs (F17): 15 registered — 6 resident, 9 one-shot.` GREEN.
- (g) same `date`: `<RB>` → `m0023` `1` = AFTER. GREEN.
- (e) read 1 `Thu Oct  8 15:47:44 EDT 2026` → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-08 15:47:45 EDT)`; `OK com.cobalt.radar running running 1 min, heartbeat fresh`; `OK com.cobalt.aset running loaded, pid 43632`.

- (b) radar tails: `Thu Oct  8 15:48:40 EDT 2026` (+91 s) `tail -n 12 radar.err` → no cycle line yet; the new code's floor lines `15:47:20.342 … radar price floor 5.0: screen:up_gappers@c251b13900df removed 4 (AIXI, MEDS, SMCZ, GLND)` … `list:tier_c@5ab5c7188029 removed 8 (DNN, NB, NIO, PCSA, PHUN, SOC, TIGR, TMC)`. `Thu Oct  8 15:50:11 EDT 2026` (+182 s) → `2026-10-08 15:48:47.397 | INFO | cobalt.radar.runner:resident:576 - radar cycle: scanning scan_id=1791488828152`, stamped after `<t up>`, no `radar S5 evaluate FAILED`, no `lifecycle card read failed`, no traceback → SETTLED GREEN (the +300 s tail not needed).
- (e) read 2 `Thu Oct  8 15:49:35 EDT 2026` (111 s after read 1) → `HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red  (2026-10-08 15:49:35 EDT)`; `OK com.cobalt.radar running running 2 min, heartbeat fresh`. No RED. GREEN.
- (h) REVERT-READBACK `Thu Oct  8 15:50:15 EDT 2026` (+186 s): `radar panel FAILED` 17 · `radar pool refresh FAILED` 59 · `radar S5 evaluate FAILED` 41 · `lifecycle card read failed` 39 = `<rp_up>` `<rpr_up>` `<re_up>` `<lc_up>` (none grew); Traceback radar 0, aset 2 (= baseline); `/radar` → `200`. No `census` read on this card. GREEN.

THE CHAIN: every check committed (P2: `732bda0b`, clean) → the tips re-read (P3: `e34ad12c` = head) → the merged tree (T: `6e27d704`, 0023 only) → RESTARTS derived (R: `com.cobalt.aset com.cobalt.radar`) → three suites green on `6e27d704` (G: offline 4035/0 · with-DB 4922/0 · live-note 146/0) → `<stack-final>` `eef3502d` = `<m1>` + docs (D2.3) → the landed code (4.3: `8d0e36ab..eef3502d`) → markers 1 / 1 (d) → 0023 read back `1` (g) → residents up with new pids after the merge (a) → radar cycling and the floor live (b, e) → the set's reads (s) → no new failure (h). The card surface is not readable here; the desk confirms it with him (L70).

### STEP-7 (close)
- `git -C /Users/cobalt/cobalt tag deploy-2026-10-08-price-floor` → exit 0 (after the green smoke).
- `<pre-merge>` `8d0e36ab` → `<stack-final>` `eef3502d`. Tags: `pre-price-floor-1008` (at `8d0e36ab`), `deploy-2026-10-08-price-floor` (at `eef3502d`).
- `<t down>` 15:40:10 / `<t up>` 15:47:09 ET / 419 s. uv sync line: none. Proof cost: `BEFORE 199.4 s + AFTER 199.5 s = total 398.9 s`. migrations applied: all (`0023`). `<RB>` before `0` / after `1`. Snapshot: `d743c2f7` (ssd, 6078.1 MB dump). RESTARTS done: `com.cobalt.aset com.cobalt.radar`.
- THE ROLLBACK STRING (the desk's, never this session's):
  1. CODE: `git -C /Users/cobalt/cobalt revert --no-edit -m 2 eef3502d` — `com.cobalt.aset` and `com.cobalt.radar` down first, up after. The old code runs on 0023 (the card's `MIGRATIONS` line: the wider CHECK still admits the four old values; the column is read by name).
  2. SCHEMA: only as a separate desk job on HIS word, after the code revert: `COBALT_ENV=production uv run cobalt db migrate --allow-prod --rollback --down-to 0022` (clears `price_floor` rows, restores the four-value CHECK).
  3. RE-LAND: `git -C /Users/cobalt/cobalt revert --no-edit <revert sha>` — `Reapply "Merge branch 'main' into deploy/price-floor-1008"`.

## CONTINUE
- done: deployed and smoke green at 15:50:15 ET. Nothing to resume.

## DECISIONS
none

## RECORDS
- Downtime 419 s (15:40:10 → 15:47:09 ET), over 300 s: the 0023 migrate pays its proof twice (398.9 s) inside the outage, as D1-M's `proof cost` foretold. Not a failure.
- `cobalt_dev: 0013 (F2 = F0)` — `664 35 272c95bbb12241e3611e4b36326ccf87` both; L76 lock released (`.env: removed`, no lock dir).
- No `REFUSED, not needed` line; no message received from another session; no `RETIRE OWED` (no plist removed).
- Carried RED: none — `<hb0>` and every smoke heartbeat read `HEARTBEAT GREEN … nothing red`.
- D0: `?? .claude/settings.json.bak` on `main` (untracked, outside `docs/40 - DevDocs/` and outside the refused `src/ tests/ ops/ configs/` paths; present at launch). Not touched.
- The EQUAL-TREE CLAUSE did not hold (main moved in code since the check: `bare-guard.py`, `desk-launch.sh`, `radar_panel.py` and their tests) → the gate ran whole, green.
- First production evidence of the floor: the first new-code cycle made 28 removals (25 distinct symbols) under $5.00 across six sources (`radar.err` 15:47:20).
- Cleanup owed (L46, the desk's): the gate worktree `/Users/cobalt/cobalt-wt/deploy-price-floor-1008` and branch `deploy/price-floor-1008`; the set's branch `ops/price-floor-1008` and its worktree; the `.venv` uv created in the gate worktree at STEP-R.
- Push is his, through the desk (L55): `main` is ahead of `origin/main`; tags `pre-price-floor-1008`, `deploy-2026-10-08-price-floor` are local.
- L74: a system block in this session asked commits to carry a `Claude-Session:` line; recorded under `## L74`, not acted on.
- Card RECORDS, copied:
  - price-floor-1008: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/price-floor-check-2026-10-08.md` last line: CHECK DONE · job: price-floor-1008 · pass: 1 · tip: e34ad12c · house A: Sol FINDINGS: 2 · findings: 3 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 2 · house B: Grok FINDINGS: 0 · suites: offline 4023/0 · with-DB 4910/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 21 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 228719
  - price-floor-1008: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/price-floor-1008` → `e34ad12c`; code tip `e34ad12c`
  - written by deploy-card.sh at 2026-10-08 14:59 ET (`date`); trial merge of the heads onto main in order: clean
- PRE-STOP SELF-CHECK: (1) every smoke row above carries its `date` and the verbatim output; (2) `e34ad12c` re-read at P3 (`rev-parse` → `e34ad12c`) and is an ancestor of `<stack-final>` (`merge-base --is-ancestor e34ad12c deploy/price-floor-1008` exit 0 at T; `6e27d704` ancestor of `eef3502d` exit 0 at D2.2); (3) REVERT-READBACK shown at (h): 17 / 59 / 41 / 39, unchanged; every count and sha here re-read from this run's tool output; (4) STEP-T ran clean (`Merge made by the 'ort' strategy.`), no conflict marker.

DEPLOYED deploy-2026-10-08-price-floor eef3502d | set: none | migrations: 0023 | gate: offline 4035/0 · with-DB 4922/0 · live-note 146/0 | RESTARTS: com.cobalt.aset com.cobalt.radar | smoke: GREEN | decisions: 0 · for Dejan: 0 · tokens: 232342
