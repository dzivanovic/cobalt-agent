# Excerpt of deploy-2026-09-19.md — the ACTUAL dry-run/apply output for the dark-row card-settings load (the only precedent for what this loader prints), plus the hash-verification and post-write smoke pattern 02 used

## P11 — hash verification pattern (lines 36-42)
**P11 — the three approved hashes, re-verified at 08:16 ET:**

| file | sha256 | equals approval row |
|---|---|---|
| `…/ops-2026-09-18/scratch/daymode-settings-0918/daymode.yaml` | `daa7bb720f19b60a438f3366aa7327188842d69f5fe0da343fa6bbbe7b3d5ebb` | YES |
| `…/ops-2026-09-18/scratch/daymode-settings-0918/aset.yaml` | `8eca6945087170312a11709a4c5833a9d36d298798343ea1af39265a6eb99d58` | YES |
| `…/cobalt/data/backups/pre-s2-p2-2026-09-17/p2-dark-settings.yaml` | `945e42f86997559267b2e7c20783f2d023b9135ae4bb437ca25a4999ca7cd3ca` | YES |

## Deploy table 3.6-3.8 summary row (lines 103-107)
| 3.4 forward dry run | **GATE PASSED** — `DRY RUN — 1 setting(s) would change. Nothing written.`; six keys `=`, the only `~` is `daymode.stepdowns` (db side 6 rows, file side the same 6 + `trade_count_over_band`) |
| 3.5 migration | **GREEN, exit 0** — the proof table below |
| 3.6 over-band apply | `date` 08:21:11 ET (outside 19:40–21:00) → **applied** |
| 3.7 dark row | `date` 08:21:15 ET → dry run then **applied** |
| 3.8 validate | **exit 0**, `Step-downs:` now carries `trade_count_over_band=down(1)` — **7 row(s)** |

## 3.6 and 3.7 — the actual apply output text, verbatim (lines 144-149)
**3.6 — the over-band row, applied 08:21:11 ET.** `applied: {'aset.sheet_modes': 'unchanged', 'aset.enabled_grades': 'unchanged', 'daymode.reduced_sheet': 'unchanged', 'daymode.reduced_enabled_grades': 'unchanged', 'daymode.enabled_modes': 'unchanged', 'daymode.hotkey_file_template': 'unchanged', 'daymode.stepdowns': 'updated'}` then `from_db() == from_yaml() — field-by-field diff EMPTY.`
**L28 trace:** approved by Dejan via the desk — `cto-2026-09-19.md` row **R7** (07:49 ET) · command `COBALT_ENV=production uv run cobalt settings load --from /Users/cobalt/cobalt-wt/ops-2026-09-18/scratch/daymode-settings-0918 --apply` · `daymode.yaml` sha256 `daa7bb72…3d5ebb`, `aset.yaml` sha256 `8eca6945…b99d58` · applied 2026-09-19 08:21:11 ET.

**3.7 — the dark row, applied 08:21:15 ET.** Dry run: `+ radar.cards_enabled`, db `(absent)` → file `false`, `DRY RUN — 1 card setting(s) would change. Nothing written.` — **ONE add, ZERO deletions**, no existing `card.*` row listed. Apply: `applied: {'radar.cards_enabled': 'created'}; deleted: []` and `round trip: CardSettings.from_rows(db) == reviewed file — EQUAL.` Independent read back: `db query --side user --prod "SELECT key, value FROM trader_settings WHERE key = 'radar.cards_enabled'"` → **one row, `radar.cards_enabled  False`**.
**L28 trace:** approved by Dejan via the desk — `cto-2026-09-19.md` row **R7** (07:49 ET) · command `COBALT_ENV=production uv run cobalt settings load --card /Users/cobalt/cobalt/data/backups/pre-s2-p2-2026-09-17/p2-dark-settings.yaml --sha256 945e42f8…ca7cd3ca --apply` · applied 2026-09-19 08:21:15 ET.


## Smoke table — post-write verification pattern (lines 159-171)
## Smoke

| check | result |
|---|---|
| `curl … :5010/` | **200** |
| `curl … :5010/radar` | **200** |
| `heartbeat show` (08:21:57) | **`HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red`** — **NO new RED, and no RED at all**. `com.cobalt.aset running pid 72854`; `com.cobalt.radar running 0 min, heartbeat fresh`; `radar idle (overnight)`; `sheet daymode … cards are accepted`; herdr AMBER by declared interim, unchanged |
| `validate` | exit **0** — `Step-downs: … trade_count_band_placeholder=floor; trade_count_over_band=down(1) — 7 row(s), every computable signal ruled.` Band min 2 / max 6 unchanged; `60 engine tunable(s)`; `Card states: 8 states, 11 legal edges`; `Placement: tree clean` |
| `radar.err` | radar started **08:21:42** on the new code (`cobalt.radar.runner:resident:459` — the old line was `:347`), vault unlocked, Finviz token resolved, first cycle `radar cycle: idle:overnight scan_id=None`. **No traceback, no `CardSettingsError`, no `trade_def_slug`, no `radar_pool_failed_stage_check`** |
| `aset.log` / `aset.err` | server restarted (`Started server process [72861]`, `Uvicorn running on http://0.0.0.0:5010`), `GET /` 200, `GET /radar` 200, `GET /api/health` 200. **No traceback, no degraded day-mode banner** |
| `radar_pool` spaced reads | **NOT APPLICABLE — no scanning session is open.** Saturday 08:2x ET is overnight idle; `radar.err` reads `idle:overnight` every 100 s, which is the correct shape outside a session (`runner.py` gates the cycle on PREMARKET/RTH/AFTERMARKET). No `last_scan_at` can advance today |
| `ops/cto-desk.sh` | `-rwxr-xr-x  1 cobalt  staff  17510 Sep 19 08:19` — present on main and **executable** |
| beats | `grep -c "ENTERED RED" logs/heartbeat.log` → **93 — unchanged from the 3.1 baseline**: the outage raised no RED entry and sent no DM |

## P2 DARK proof pattern (lines 173-179) — the shape of a post-write round-trip read
**P2 DARK proof (5.2)**

| check | result |
|---|---|
| `radar evaluate --replay 2026-09-18` | ran on the new code, **`writes: none`**. `replay 2026-09-18: scans=235 formations=0 path_b_only=52 counts={'input_stale': 1286, 'not_evaluable': 5454, 'not_formed': 5010}`. 12 defs printed `not evaluable: missing atoms […]`, and 52 rubberband path-B-only lines (`not evaluable in S2 (catalyst unknown, R4)`) — **formations=0, so no card was formed and nothing was written** |
| radar-origin card rows | provenance column taken from `0007_radar_cards.sql`'s `aset_sizings_radar_provenance` CHECK: it keys on **`origin`** (`CHECK (origin <> 'radar' OR …)`). `db query --side user --prod "SELECT count(*) FROM aset_sizings WHERE origin = 'radar'"` → **0** |
| `radar_score_run` | `db query --side system --prod "SELECT count(*) FROM radar_score_run"` → **0**, no error — the table exists (0006 applied). **Rows appear only in a scanning session; today is overnight idle, so 0 is the expected case** |
