# deploy price-floor-1008 · SET: none · MIGRATIONS: 0023

## §0 Headline
- Card 150, price floor (R692), one branch `ops/price-floor-1008` at `e34ad12c`, migration 0023. In progress.

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

## CONTINUE
- next: STEP-D2

(run in progress — next step under ## CONTINUE)
