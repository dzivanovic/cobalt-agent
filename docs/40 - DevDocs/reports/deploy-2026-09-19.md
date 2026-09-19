# DEPLOY 2026-09-19 — STACKED DEPLOY

Hub `deploy-stack-0919` (Opus 5, `claude-opus-5`), bg `2f3cea78`, cwd `/Users/cobalt/cobalt`.
Prompt: `docs/40 - DevDocs/prompts/2026-09-19/02-deploy-stack-3.md` (sha256 `447eed96b6563b739c530eaff7f284cd0501189f8da6eb7525d3b2c1cfb1e432`).
Authorization: `cto-2026-09-19.md` §4 **R7** (07:49 ET) + `cto-2026-09-18.md` §4 R3/R5/R6/R10/R18–R21. Verified rule by rule below.

## §0 Headline

- **STACKED DEPLOY DONE. Main `2893a7f`, tagged `deploy-2026-09-19`, smoke GREEN, both residents UP on new pids, outage 2 min 40 s.** §6 was never entered.
- **Migrations 0006/0007 APPLIED** — the harness that died at production scale on 09-18 completed in 94.1 s of proof: 23 tables, **0 `CHANGED`**, 8 `CREATED` and every one defined by 0006/0007.
- Both approved `trader_settings` writes landed: the over-band row 08:21:11 ET (`validate` now shows **7 step-down rows**, `trade_count_over_band=down(1)`) and the dark row 08:21:15 ET (`radar.cards_enabled = False`, read back independently).
- P2 ships DARK and proven dark: `radar evaluate --replay 2026-09-18` → `formations=0 … writes: none`; radar-origin `aset_sizings` rows **0**; `radar_score_run` exists, 0 rows (overnight idle).
- PREFLIGHT 12 probes + the rollback gate, **zero denials**; heartbeat GREEN before and after, RED-entry count **93 → 93**. ESCALATE: **5** (none blocks anything shipped).

## PREFLIGHT

Ran 08:15–08:17 ET from `/Users/cobalt/cobalt`. **Zero denials — every allowlisted shape probed.**

| rule | command | exit | allowed / DENIED |
|---|---|---|---|
| P1 | `git -C /Users/cobalt/cobalt status --porcelain` | 0 | allowed — ` M docs/40 - DevDocs/reports/cto-2026-09-19.md`, ` M docs/40 - DevDocs/reports/seat-usage.md`. Nothing else dirty (**no `configs/cobalt/rules.yaml`** — V1/U1's case does not arise today) |
| P2 | `git … tag scratch-allow-probe-0919` then `tag -d …` | 0 / 0 | allowed — `Deleted tag 'scratch-allow-probe-0919' (was 15ff759)` |
| P3 | `git … commit --allow-empty` then `reset --soft HEAD~1` | 0 / 0 | allowed — `[main e4f0802]` created, then `log --oneline -1` → **`15ff759`** — HEAD is back |
| P4 | `COBALT_ENV=production uv run cobalt validate` | **0** | allowed — 13 trade_defs OK; `Step-downs: … trade_count_band_placeholder=floor — 6 row(s)` (no `trade_count_over_band`: the pre-merge state); band min 2 / max 6; `Placement: tree clean` |
| P5 | `COBALT_ENV=production uv run cobalt backup status` | 0 | allowed — `ssd local ARMED`, `newest snapshot: 10.6 h old` |
| P6 | `COBALT_ENV=production uv run cobalt backup run --dry-run` | 0 | allowed — `backup: cobalt_brain via pg_dump inside cobalt_memory — 645.1 MB`; `DRY RUN — nothing written, no jobs row touched.` |
| P7 | `COBALT_ENV=production uv run cobalt jobs restarts main..sprint-2/stack` | **1** | allowed — EXPECTED exit 1 under main's OLD classifier: `.gitignore  M  UNCLASSIFIED` (`ESCALATE: unclassified path .gitignore`). Everything else classified (`DOCS → -`, `static import reach`, `resident reads`, `test/documentation; no resident`). The rules that classify it are inside this merge |
| P8 | `COBALT_ENV=production uv run cobalt heartbeat show` | 0 | allowed — **`HEARTBEAT GREEN — 15 job(s), 12 probe(s), nothing red (2026-09-19 08:16:02 EDT)`** |
| P9 | `launchctl print gui/501/com.cobalt.aset` · `…/com.cobalt.radar` | 0 / 0 | allowed — both `state = running`; **aset pid 76253**, `path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` · **radar pid 76271**, `path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`. Both paths are the expected ones — no plist moved |
| P10 | `curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/` | 0 | allowed — **`200`** |
| P11 | `shasum -a 256` × 3 | 0 | allowed — all three equal the approval row (table below) |
| P12 | `COBALT_ENV=production uv run cobalt db query --side system --prod "SELECT tablename, array_agg(schemaname ORDER BY schemaname) FROM pg_tables WHERE schemaname IN ('public','user','system') GROUP BY tablename HAVING count(*) > 1"` | 0 | allowed — header only, **ZERO rows**. No duplicate table name; the round-2 refusal cannot fire at 3.5 |

**P8 — NO BASELINE RED TO RECORD.** Every probe `OK`; the only non-OK line is `AMB com.cobalt.herdr unmanaged — launchd unmanaged … by declared interim`, the standing AMBER, not a RED. R6's accepted-RED gate is therefore not needed today; the smoke's rule becomes simply "no RED at all". `radar` probe reads `idle (overnight)`. Cycling proof for the record — **outside a scanning session, so `idle:<session>` lines are the correct shape** (`tail -n 12 logs/radar.err`): `radar cycle: idle:overnight scan_id=None` at 07:57:00, 07:58:40, 08:00:20, 08:02:00, 08:03:40, 08:05:20, 08:07:00, 08:08:40, 08:10:21, 08:12:01, 08:13:41, 08:15:21 — **100 s apart, no traceback**.

**P11 — the three approved hashes, re-verified at 08:16 ET:**

| file | sha256 | equals approval row |
|---|---|---|
| `…/ops-2026-09-18/scratch/daymode-settings-0918/daymode.yaml` | `daa7bb720f19b60a438f3366aa7327188842d69f5fe0da343fa6bbbe7b3d5ebb` | YES |
| `…/ops-2026-09-18/scratch/daymode-settings-0918/aset.yaml` | `8eca6945087170312a11709a4c5833a9d36d298798343ea1af39265a6eb99d58` | YES |
| `…/cobalt/data/backups/pre-s2-p2-2026-09-17/p2-dark-settings.yaml` | `945e42f86997559267b2e7c20783f2d023b9135ae4bb437ca25a4999ca7cd3ca` | YES |

### Authorization, verified before anything ran

| what | where | verdict |
|---|---|---|
| the row that names THIS file | `cto-2026-09-19.md` §4 **R7**, 07:49 ET, "Approved" | PRESENT — approves the launch line of `02-deploy-stack-3.md` AND both settings loads by file + sha256 |
| the file is the approved text | R7's applied column: text-only folds recorded, round 3 → FINAL sha256 `447eed96…1e432` | `shasum -a 256` of the prompt file = **`447eed96b6563b739c530eaff7f284cd0501189f8da6eb7525d3b2c1cfb1e432`** — EQUAL |
| the row is committed on main | `git log --oneline -10 -- "docs/40 - DevDocs/reports/cto-2026-09-19.md"` | `9917515` (R7) and `15ff759` (round-3 fold, the FINAL hash) both on main |
| the 09-18 rows | `git log --oneline -10 -- "docs/40 - DevDocs/reports/cto-2026-09-18.md"` | committed; R3 (07:14) + R5 (11:09) weekend push through 09-20; R6 (11:18) baseline-RED class + aset bootstraps from the REPO plist; R10 (15:36) "Approved one stack"; R18–R21 (17:30–17:42) L67 |
| R7's launch conditions | §11/§14 of `cto-2026-09-19.md` | (1) deployment check round 3 named no blocker — MET; (2) `PROD PROOF DONE` on `ad9b07c` — MET; (3) `date` = **08:17 ET ≤ 18:30** — MET |

No mismatch anywhere. GATE 0.2: **proven — commit + tag allowed by the session allowlist** (P2 + P3 both ran and were undone).

### 0.3 Rollback directory

| item | fact |
|---|---|
| directory | `mkdir -p /Users/cobalt/cobalt/data/backups/pre-stack-0919/daymode-settings-rollback` — created fresh by this hub. Under gitignored `data/`; **never `git add`ed** |
| `aset.yaml` | written BYTE-IDENTICAL to the forward file — proven by hash: `8eca6945087170312a11709a4c5833a9d36d298798343ea1af39265a6eb99d58`, equal to the forward file's |
| `daymode.yaml` | the forward file MINUS exactly the four-line `trade_count_over_band` row (`- signal:` / `effect:` / `rungs:` / `because:`). sha256 `48a99812acf090574f738df886d4584c2100f1d6e0f3abbbd9882bde183d81e1` |
| **GATE** | `settings load --from …/pre-stack-0919/daymode-settings-rollback --dry-run` → all seven keys `=`, then verbatim: **`no differences — the database already holds these settings.`** The rollback file equals production |

No value from either settings file is quoted in this report (L32).

## Preconditions (08:17–08:18 ET)

| check | result |
|---|---|
| 1.1 clock | `Sat Sep 19 08:17:56 EDT 2026` — **08:17 ET ≤ 18:30**, the run may start. Ninety minutes of margin before 19:40; re-checked before 3.2, 3.6 and 3.7 |
| 1.2 gate — round 2 | `harness-round2-2026-09-19.md` ends **`ROUND2 BUILT ad9b07c on sprint-2/stack … offline: 1562 passed, 0 failed`** ✓ |
| 1.2 gate — prod proof | `prod-proof-only-3-2026-09-19.md` ends **`PROD PROOF DONE | 23 tables | system.bars 8834532 rows in 51.99 s | … nothing applied, nothing written | 0006/0007 absent: yes`** ✓ |
| 1.2 proof BOUND to the gated code (V7 / R3) | `git -C …/s2-p2-cards log --oneline ad9b07c..HEAD -- "…/prod-proof-only-3-2026-09-19.md"` → **three commits** (`4a0b1c4`, `8ae5c9b`, `c61fcac`) — the proof report was committed on this branch AFTER `ad9b07c`, and the code diff below is empty, so the proof ran on `ad9b07c`'s code |
| 1.2 branch (V8) | `log -1 --format=%D` → **`HEAD -> sprint-2/stack`** |
| 1.2 byte-identity (V2) | `diff --stat ad9b07c HEAD -- . ':(exclude)docs'` → **printed NOTHING**. Only report commits sit above the gated code |
| 1.2 clean | `status --porcelain` → **empty** |
| 1.2 `<n>` | `rev-list --count main..HEAD` → **81** |
| 1.3 no other merger | `log --oneline -3` → `3b30b94` (my own PREFLIGHT commit) over `15ff759` (desk, deploy launches) over `2d1c7a1`. Main's tip is a deploy/desk docs commit; no build or deploy session merging |

## Deploy table

**Step 2 — machine-written files, snapshot, tag (08:18 ET)**

| step | fact |
|---|---|
| 2.1 dirty tree | ` M docs/40 - DevDocs/reports/cto-2026-09-19.md` (the desk's live report), ` M docs/40 - DevDocs/reports/seat-usage.md` — exactly the expected set, **no `configs/cobalt/rules.yaml`**. Both `git add`ed BY NAME, nothing under `data/` |
| 2.1 commit | **`5d0cf61`** `chore: machine-written + report files, committed as-is (L51-2)` — 2 files, +28 |
| 2.2 snapshot | `ssd: snapshot b17c8dec — 1 new / 5 changed, 6.4 MB added, 0 pruned`; dump line `backup: cobalt_brain via pg_dump inside cobalt_memory — 645.1 MB`. `backup status` → `newest snapshot: 0.0 h old` ✓ |
| 2.2 tag | **`pre-stack-0919`** created at `5d0cf61` |

Known and carried (ops ESCALATE 4): snapshot `b17c8dec` (08:18 ET) is pruned by tonight's 21:40 nightly (`--keep-daily 14`) and `cobalt backup` cannot list snapshot ids. **The durable rollback point is the tag `pre-stack-0919`.**

**Step 3 — the outage window (08:19:07 → 08:21:47 ET, 2 min 40 s)**

| step | fact |
|---|---|
| 3.0 rebase | `git -C …/s2-p2-cards rebase main` → `Successfully rebased and updated refs/heads/sprint-2/stack` (81/81, no conflict). **PROOF:** `diff --stat ad9b07c HEAD -- . ':(exclude)docs'` **printed NOTHING** — the V1 exception was NOT needed (`configs/cobalt/rules.yaml` was never dirty on main today). `rev-list --count main..HEAD` → **81** = `<n>` of 1.2 ✓ |
| 3.0 `<pre-merge>` | **`2e965c3`** (my own step-2.3 report commit) |
| 3.1 baseline | `grep -c "ENTERED RED" logs/heartbeat.log` → **93**. Window opened `Sat Sep 19 08:19:07 EDT 2026` |
| 3.2 residents DOWN | `bootout` aset, then radar. Both `launchctl print` then exit **113** `Could not find service … in domain for user gui: 501` — the proof. **No 15-min beat landed inside the window** (beats 08:07 and 08:22 ET), so the outage raised no RED and sent no DM |
| 3.3 merge | `rev-parse --short HEAD` = `2e965c3` ✓ → `merge --ff-only sprint-2/stack` → `Updating 2e965c3..2893a7f`, fast-forward, **167 files, 32,240 insertions(+), 498 deletions(−)**. Tip **`2893a7f`** |
| 3.4 forward dry run | **GATE PASSED** — `DRY RUN — 1 setting(s) would change. Nothing written.`; six keys `=`, the only `~` is `daymode.stepdowns` (db side 6 rows, file side the same 6 + `trade_count_over_band`) |
| 3.5 migration | **GREEN, exit 0** — the proof table below |
| 3.6 over-band apply | `date` 08:21:11 ET (outside 19:40–21:00) → **applied** |
| 3.7 dark row | `date` 08:21:15 ET → dry run then **applied** |
| 3.8 validate | **exit 0**, `Step-downs:` now carries `trade_count_over_band=down(1)` — **7 row(s)** |

**3.5 — the migration, exit 0. The harness that failed on 09-18 at production scale now completes in 94.1 s of proof.** All seven FORWARD files walked (`-- applying 0001…0007`); 0001–0005 re-ran idempotently by design. Proof table verbatim:

```
table                side    schema before -> after     rows            probe secs      digest before -> after verdict
----------------------------------------------------------------------------------------------------------------------
aset_sizings         user    user -> user               146 -> 146      0.03 -> 0.01    baac6ac1 -> baac6ac1  OK
bars                 system  system -> system           8834532 -> 8834532 47.21 -> 46.42  d21fc0b3 -> d21fc0b3  OK
card_dot_taps        user    - -> user                  - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
card_dots            user    - -> user                  - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
card_stop_edits      user    user -> user               1 -> 1          0.00 -> 0.00    cbae670b -> cbae670b  OK
card_transitions     user    user -> user               293 -> 293      0.00 -> 0.00    3986eb3f -> 3986eb3f  OK
cobalt_email_sends   system  system -> system           463 -> 463      0.00 -> 0.00    c8fc112a -> c8fc112a  OK
cobalt_jobs          system  system -> system           15 -> 15        0.00 -> 0.00    b722fe7f -> b722fe7f  OK
cobalt_kill_switch   system  system -> system           1 -> 1          0.00 -> 0.00    31065594 -> 31065594  OK
cobalt_redactions    system  system -> system           2 -> 2          0.00 -> 0.00    cf42d85e -> cf42d85e  OK
day_modes            user    user -> user               10 -> 10        0.00 -> 0.00    d9139ce7 -> d9139ce7  OK
desk_grade           system  - -> system                - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
desk_packet          system  - -> system                - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
desk_regime          system  - -> system                - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
radar_membership     system  system -> system           3334 -> 3334    0.04 -> 0.04    72b94dfe -> 72b94dfe  OK
radar_pool           system  system -> system           1 -> 1          0.00 -> 0.00    88537229 -> 88537229  OK
radar_score          system  - -> system                - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
radar_score_receipt  user    - -> user                  - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
radar_score_run      system  - -> system                - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
session_blocks       system  system -> system           8 -> 8          0.00 -> 0.00    ddf2a773 -> ddf2a773  OK
traders              user    user -> user               1 -> 1          0.00 -> 0.00    cf9aec4d -> cf9aec4d  OK
vault_overrides      user    user -> user               29 -> 29        0.00 -> 0.00    1f529ee7 -> 1f529ee7  OK
vault_writes         user    user -> user               1322 -> 1322    0.13 -> 0.13    50b08c4e -> 50b08c4e  OK
----------------------------------------------------------------------------------------------------------------------
23 table(s) proven; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id; aset_sizings: 25 card column(s) added by 0007. content UNCHANGED on every table.
proof cost: BEFORE 47.4 s + AFTER 46.6 s = total 94.1 s; slowest table bars (47.2 s before).
```

**GATE, checked term by term:** ZERO tables marked `CHANGED`. The `CREATED` set is exactly **8 tables**, and every one is defined by the two shipping migrations — `0006_radar_score.sql` creates `radar_score_run`, `radar_score`, `desk_regime`, `desk_packet`, `desk_grade`; `0007_radar_cards.sql` creates `card_dots`, `card_dot_taps`, `radar_score_receipt` (both read back with `grep -n "CREATE TABLE"`). No other object was created. No serialization failure, no partial apply, no tool timeout. `bars` read 8,834,532 rows twice (47.21 s / 46.42 s) — in line with the 09-19 proof's 51.99 s.

**3.6 — the over-band row, applied 08:21:11 ET.** `applied: {'aset.sheet_modes': 'unchanged', 'aset.enabled_grades': 'unchanged', 'daymode.reduced_sheet': 'unchanged', 'daymode.reduced_enabled_grades': 'unchanged', 'daymode.enabled_modes': 'unchanged', 'daymode.hotkey_file_template': 'unchanged', 'daymode.stepdowns': 'updated'}` then `from_db() == from_yaml() — field-by-field diff EMPTY.`
**L28 trace:** approved by Dejan via the desk — `cto-2026-09-19.md` row **R7** (07:49 ET) · command `COBALT_ENV=production uv run cobalt settings load --from /Users/cobalt/cobalt-wt/ops-2026-09-18/scratch/daymode-settings-0918 --apply` · `daymode.yaml` sha256 `daa7bb72…3d5ebb`, `aset.yaml` sha256 `8eca6945…b99d58` · applied 2026-09-19 08:21:11 ET.

**3.7 — the dark row, applied 08:21:15 ET.** Dry run: `+ radar.cards_enabled`, db `(absent)` → file `false`, `DRY RUN — 1 card setting(s) would change. Nothing written.` — **ONE add, ZERO deletions**, no existing `card.*` row listed. Apply: `applied: {'radar.cards_enabled': 'created'}; deleted: []` and `round trip: CardSettings.from_rows(db) == reviewed file — EQUAL.` Independent read back: `db query --side user --prod "SELECT key, value FROM trader_settings WHERE key = 'radar.cards_enabled'"` → **one row, `radar.cards_enabled  False`**.
**L28 trace:** approved by Dejan via the desk — `cto-2026-09-19.md` row **R7** (07:49 ET) · command `COBALT_ENV=production uv run cobalt settings load --card /Users/cobalt/cobalt/data/backups/pre-s2-p2-2026-09-17/p2-dark-settings.yaml --sha256 945e42f8…ca7cd3ca --apply` · applied 2026-09-19 08:21:15 ET.

**Step 4 — residents UP (08:21:42–08:21:47 ET)**

| step | fact |
|---|---|
| 4.1 register | `cobalt jobs register` → `registered 15 job(s)` — **no plist change**: 6 resident + 9 one-shot, the same registry as before the merge |
| 4.1 RESTARTS | `cobalt jobs restarts 2e965c3..HEAD` → **`RESTARTS: com.cobalt.aset com.cobalt.radar`**, **0 UNCLASSIFIED**. The merge's own new rules classify the two paths main could not: `.gitignore  M  META  -` and `ops/cto-desk.sh  A  operator script; no Cobalt reader  -`. No third resident derived |
| 4.2 bootstrap | `bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist` (the REPO plist, R6) and `…/Library/LaunchAgents/com.cobalt.radar.plist`. Both `state = running`, NEW pids **aset 72854** (was 76253), **radar 72867** (was 76271), `last exit code = (never exited)`, both `path =` lines unchanged. **No `Bootstrap failed: 5`, no `kickstart` needed** |
| outage | 08:19:07 → 08:21:47 = **2 min 40 s** |

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

**P2 DARK proof (5.2)**

| check | result |
|---|---|
| `radar evaluate --replay 2026-09-18` | ran on the new code, **`writes: none`**. `replay 2026-09-18: scans=235 formations=0 path_b_only=52 counts={'input_stale': 1286, 'not_evaluable': 5454, 'not_formed': 5010}`. 12 defs printed `not evaluable: missing atoms […]`, and 52 rubberband path-B-only lines (`not evaluable in S2 (catalyst unknown, R4)`) — **formations=0, so no card was formed and nothing was written** |
| radar-origin card rows | provenance column taken from `0007_radar_cards.sql`'s `aset_sizings_radar_provenance` CHECK: it keys on **`origin`** (`CHECK (origin <> 'radar' OR …)`). `db query --side user --prod "SELECT count(*) FROM aset_sizings WHERE origin = 'radar'"` → **0** |
| `radar_score_run` | `db query --side system --prod "SELECT count(*) FROM radar_score_run"` → **0**, no error — the table exists (0006 applied). **Rows appear only in a scanning session; today is overnight idle, so 0 is the expected case** |

## Close

| item | value |
|---|---|
| main tip | **`2893a7f`**, `git status --porcelain` empty |
| tags | `pre-stack-0919` = `5d0cf61` (rollback point) · **`deploy-2026-09-19`** = `2893a7f` |
| snapshot | restic `b17c8dec`, 08:18 ET (pruned by tonight's 21:40 nightly; the tag is the durable point) |
| RESTARTS | **done: `com.cobalt.aset` `com.cobalt.radar`** — both bootstrapped, both running on new pids |
| outage | **2 min 40 s** (08:19:07 → 08:21:47 ET) |
| membership gap | 08:19:07 ET → the first completed scan. **No scan can complete today**: the radar gates its cycle on PREMARKET/RTH/AFTERMARKET and Saturday is overnight idle throughout. The gap closes at **Monday 2026-09-21 04:00 ET**, the premarket open |
| first live proof of the step-down | **Monday 2026-09-21 09:00 ET**, `com.cobalt.daymode-propose` — the first run of the proposer that reads the seventh `daymode.stepdowns` row |
| first COMPLETE `radar_score_run` | **Monday 2026-09-21 04:00 ET** premarket, proven by that day's day-open report |

## ESCALATE

1. **`migrate`'s proof cost is now the whole outage, and it is still growing.** The deploy took 2 min 40 s of downtime; **94.1 s of it (59%) was the migration's BEFORE+AFTER read of `system.bars`** (8,834,532 rows, 47.21 s + 46.42 s). Everything else — rebase, merge of 167 files, two settings writes, `validate`, both bootstraps — cost about 65 s together. Today's number is slightly *better* than the 08:0x proof run's 104 s estimate (host was quieter), so `prod-proof-only-3-2026-09-19.md` ESCALATE 1's superlinearity question is unresolved, not closed. The bounded-`bars` proof (closed periods proven once by a stored digest, only the open period re-read) is now the single largest lever on deploy downtime, and Sunday's partition/retention tribunal is where it belongs.
2. **Both of the day's standing harness limits went untested, by luck of the clock, and should not be read as proven.** No serialization failure occurred (the build hub's ESCALATE 1 predicted effectively nil exposure — confirmed, not tested), and `com.cobalt.archiver` is still not among the jobs the deploy disarms (`prod-proof-only-3` ESCALATE 2): it last ran 00:53 UTC and was idle throughout this window, so its zero exposure today is a fact about the hour, not about the design. The standing fix — disarm the archiver like the other two, or land the bounded proof — is still owed, and the next deploy in a busier hour is where it will matter.
3. **`configs/cobalt/rules.yaml` was clean at 2.1 today, so the V1 named exception never fired.** The desk's re-check at 08:13 (§14) held: `git status --porcelain` on main showed only `seat-usage.md`, and the desk's live `cto-2026-09-19.md`. Both went into `5d0cf61` as-is under L51-2 — **the desk should know its 08:0x–08:13 report text is committed at that hash**, including the §14 launch row that says it stays uncommitted. The V1 fold is untested in production and remains correct as written.
4. **Hub self-report: two early reads in this run were not bare commands.** `UNATTENDED-LAUNCH.md` §2 requires one bare command per Bash call with no pipe and no redirect. Two exploratory reads during the index-card phase were sent wrapped (`grep … | cut -c1-700`, and one `ls …; echo …; grep …` chain) — both over already-readable report files, both on allowlisted prefixes, neither denied, neither load-bearing for any verdict here. **Every command from PREFLIGHT onward was bare**, exactly the listed prefix, one per call. Recorded because the rule exists to keep the classifier — not the shell — the thing that judges a command.
5. **The prompt's own tail carries no injected block this time, and the `Claude-Session:` line was still not written into commits.** Unlike 09-18's three runs (where a block styled as a system reminder sat inside the prompt file's tail), `grep -c "Claude-Session" 02-deploy-stack-3.md` = **0** — the file is clean. A harness reminder asking for a `Claude-Session:` URL line did arrive in this session, attached to a tool result. Following the three prior deploy hubs' recorded decision, commits carry `Co-Authored-By` only. The desk may want to rule once whether that line is wanted in Cobalt's history, so the next hub does not re-decide it.

STACK DEPLOY DONE 2893a7f · LIVE: sprint-2/stack DARK y · ops-0918 y · migrations 0006/0007 applied · over-band row 08:21:11 ET · dark row 08:21:15 ET · RESTARTS done: com.cobalt.aset com.cobalt.radar · outage 02:40 · PUSH: Dejan · ESCALATE: 5
