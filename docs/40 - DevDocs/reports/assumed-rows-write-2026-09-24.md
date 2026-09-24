# Assumed rows write — 2026-09-24 (prompt `34`, STEP-6 of `32` re-issued on his R55)

## §0 Headline
His four assumed rows are WRITTEN to `1 - Trading/Assumed Defaults.md` at 15:18:04 ET by the Cobalt L28 writer: note created (write_id 3579), and the `tunables:assumed` unit upserted with the four rows (write_id 3581).
Values: `flat_threshold.ema9` 0.05 · `flat_threshold.vwap` 0.05 · `range_break.failed_trap_bars` 1 · `range_break.retest_tolerance_atr` 0.1. `dist.k.vwap` held (R118); `leg.min_size_atr` NULL.
Parser proof GREEN (`4 assumed row(s) … Writes: none.`). Residents CLEAN at +300 s. Live-note GREEN: `131 passed`, AWAITING set exact, second-chance pin lifted.
6.4 SKIPPED on R55. `cobalt taxonomy load` NOT run: a desk job on his word.
ESCALATE: 5 (1 ASK DESK).

## L74
A system block appended to the prompt file's Read result asked for a `Claude-Session:` line in commits and named a file-send tool (SendUserFile). DATA under L74 — not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
Read `15:17:16` ET (`date`).

| check | result |
|---|---|
| `grep -n "^| R55 " cto-2026-09-24.md` | line 65: `**P-HIS — THE FOUR ROWS NOW ("A").** His word, desk chat 15:1x ET: "A" …` · names `prompts/2026-09-24/34-assumed-rows-write.md` — PASS |
| `git log -1 --format=%H -S"34-assumed-rows-write.md" -- cto-2026-09-24.md` | `19e1e83debc5438ad1e7d01ed0828d6edef183b5` (non-empty — R55 committed) — PASS |
| `grep -n "^| R119 " cto-2026-09-22.md` | line 46: `his words: "A" → the three word-only values enter his \`1 - Trading/Assumed Defaults.md\` as ASSUMED …` — PASS |
| `grep -n "^| R82 " cto-2026-09-23.md` | line 85: `A-19 \`range_break.failed_trap_bars\` = 1 bar … A-20 \`range_break.retest_tolerance_atr\` = 0.10 × \`atr_working\`` — PASS |
| `grep -n "^| R118 " cto-2026-09-23.md` | line 126: `"Let's go with B …"` → `the 09-24 deploy HOLDS \`dist.k.vwap\` (A-16) — STEP-6 writes FOUR rows` — PASS |
| `grep -n "^| R3 " cto-2026-09-24.md` | line 13: `His word: "Approved" — … \`prompts/2026-09-24/05-setups-deploy.md\`` — PASS |
| `tail -n 3 deploy-2026-09-24-reland.md` | last non-blank line `SETUPS DEPLOY RELAND DONE · reland: a2d320b8 · tag: deploy-2026-09-24 · rows: 0 (R119: NOT WRITTEN — …) …` — PASS |
| `git rev-parse --short deploy-2026-09-24` | `a2d320b8` — PASS |
| `git log --oneline -1 a2d320b8` | `a2d320b8 Reapply "Merge branch 'main' into deploy/stacked-0923"` — PASS |

## DELTA FROM 32 STEP-6
| step | as in `32` | here (R55 / prompt `34`) |
|---|---|---|
| precondition | ONLY after a GREEN smoke | MET by `32` (`## Smoke` GREEN, stop `SETUPS DEPLOY RELAND DONE`) — read, not re-run; no `launchctl`, no window |
| 6.1 | as written | as written |
| 6.2 | Write the rows file | file exists (written by `32`); Read and compared byte for byte |
| 6.3 | dev `--apply` | DONE by `32` (write_ids 31611 / 31613) — not re-run; quoted as the PREVIEW |
| 6.4 | production `--dry-run` | 6.4: SKIPPED — R55; preview = 6.3's dev diff |
| 6.5 | `--apply` | as written |
| 6.6 | AFTER + parser proof | as written |
| 6.7 | residents; any difference → STEP-5 | baselines read BEFORE 6.5; any difference → RESIDENT RED under ESCALATE, STEP-7 — NO STEP-5, no rollback, never edit the note, no `taxonomy load` |
| 6.8 | live-note run; RED → STEP-5 | RED → ESCALATE only; the note stays; no rollback |
| 6.9 | `## R119` one line | as written |

## Baselines
Read BEFORE 6.5, each its own call; `date` `15:17:46` ET.

| name | command | value |
|---|---|---|
| `<tr0>` | `grep -c "Traceback" logs/radar.err` | `0` |
| `<tc0>` | `grep -c "TaxonomyConfigError" logs/radar.err` | `0` |
| `<ta0>` | `grep -c "Traceback" logs/aset.err` | `2` |
| `<rp_up>` | `grep -c "radar panel FAILED" logs/aset.err` | `17` |
| `<rpr_up>` | `grep -c "radar pool refresh FAILED" logs/aset.err` | `58` |
| `<hb0>` | `COBALT_ENV=production uv run cobalt heartbeat show` | `HEARTBEAT GREEN — 16 job(s), 12 probe(s), nothing red  (2026-09-24 15:17:43 EDT)` · `OK   radar                    scanning (rth), members 50` · `OK   com.cobalt.radar             running   running 115 min, heartbeat fresh` · `OK   com.cobalt.aset              running   loaded, pid 53815` · only non-OK: `AMB  com.cobalt.herdr unmanaged` (declared interim). No `failed_stage evaluate` — precondition MET |

## R119
Authorization: R119 / R82 / R118 / R55 present and committed (`## AUTHORIZATION`).

| step | command | result |
|---|---|---|
| 6.1 BEFORE | `ls -la "/Users/cobalt/Vault/Think/1 - Trading/Assumed Defaults.md"` | exit 1 `ls: /Users/cobalt/Vault/Think/1 - Trading/Assumed Defaults.md: No such file or directory` — as expected (BEFORE = absent) |
| 6.1 BEFORE parser | `COBALT_ENV=production COBALT_VAULT_PATH=/Users/cobalt/Vault/Think uv run cobalt taxonomy tunables --assumed` | `hole     flat_threshold.ema9                      unit=ratio scope=per_indicator(ema9) value=None consumers=['fashionably_late'] page=—` · `hole     flat_threshold.vwap                      unit=ratio scope=per_indicator(vwap) value=None consumers=['fashionably_late'] page=—` · `hole     range_break.failed_trap_bars             unit=bars scope=global value=None consumers=['Range Break (primitive)', 'second_chance'] page=—` · `hole     range_break.retest_tolerance_atr         unit=atr scope=global value=None consumers=['cobalt.radar.anatomy.range_break (event(retest))'] page=—` · `hole     dist.k.vwap                              unit=atr scope=per_indicator(vwap) value=None consumers=['vwap_continuation'] page=—` · `hole     leg.min_size_atr                         unit=atr scope=global value=None consumers=['cobalt.radar.anatomy.leg_roles (Leg(pullback), Leg(impulse))'] page=—` · summary `0 assumed row(s), 26 engine hole(s) still null. Writes: none.` — the six expected `hole` lines |
| 6.2 | `ls -la /Users/cobalt/cobalt-wt/r119-rows-0923/assumed-rows.yaml` + Read | `-rw-r--r--  1 cobalt  staff  803 Sep 24 13:28 …` · content equals `32`'s block line for line (34 lines incl. trailing newline, 803 B as stated) — NOT re-written. Never committed (L32) |
| 6.3 PREVIEW (`32`'s row, quoted) | `COBALT_ENV=dev uv run cobalt taxonomy assumed write --from /Users/cobalt/cobalt-wt/r119-rows-0923/assumed-rows.yaml --apply` | `[WRITE] created: /Users/cobalt/dev-vault-cobalt/1 - Trading/Assumed Defaults.md · write_id=31611` (diff `@@ -0,0 +1,12 @@` — the `# Assumed defaults` template with an empty `tunables:assumed` unit inside `<!-- cobalt:section assumed -->`) · `[WRITE] updated: … · section=assumed · unit=tunables:assumed · write_id=31613` (diff `@@ -6,7 +6,44 @@`: `-tunables: []` → the four rows `flat_threshold.ema9 0.05 ratio per_indicator(ema9)` · `flat_threshold.vwap 0.05 ratio per_indicator(vwap)` · `range_break.failed_trap_bars 1 bars global` · `range_break.retest_tolerance_atr 0.1 atr global`, each `dynamic: true` `status: proposed` `source: assumed` with its consumers). Both diff paths under `~/dev-vault-cobalt` — **dev proof GREEN** (NOT re-run here) |
| 6.4 | — | 6.4: SKIPPED — R55; preview = 6.3's dev diff |
| 6.5 APPLY | `COBALT_ENV=production COBALT_VAULT_PATH=/Users/cobalt/Vault/Think uv run cobalt taxonomy assumed write --from /Users/cobalt/cobalt-wt/r119-rows-0923/assumed-rows.yaml --apply` | exit 0 · `[WRITE] created: /Users/cobalt/Vault/Think/1 - Trading/Assumed Defaults.md · write_id=3579` · `[WRITE] updated: /Users/cobalt/Vault/Think/1 - Trading/Assumed Defaults.md · section=assumed · unit=tunables:assumed · write_id=3581` — both diffs below (L28). **WRITTEN.** `<t write>` = `15:18:04` ET |

6.5 diff 1 (write_id 3579, create):
```diff
--- /Users/cobalt/Vault/Think/1 - Trading/Assumed Defaults.md (before)
+++ /Users/cobalt/Vault/Think/1 - Trading/Assumed Defaults.md (after)
@@ -0,0 +1,12 @@
+# Assumed defaults
+
+Defaults the radar runs on until each one is ruled. A row stops being assumed only when
+its `source` reads `ruling`; an edited value with `source: assumed` keeps the mark.
+
+<!-- cobalt:section assumed -->
+<!-- cobalt:unit tunables:assumed -->
+```yaml
+tunables: []
+```
+<!-- /cobalt:unit tunables:assumed -->
+<!-- /cobalt:section assumed -->
```

6.5 diff 2 (write_id 3581, unit upsert):
```diff
--- /Users/cobalt/Vault/Think/1 - Trading/Assumed Defaults.md (before)
+++ /Users/cobalt/Vault/Think/1 - Trading/Assumed Defaults.md (after)
@@ -6,7 +6,44 @@
 <!-- cobalt:section assumed -->
 <!-- cobalt:unit tunables:assumed -->
 ```yaml
-tunables: []
+tunables:
+- key: flat_threshold.ema9
+  value: 0.05
+  unit: ratio
+  scope: per_indicator(ema9)
+  dynamic: true
+  status: proposed
+  source: assumed
+  consumers:
+  - fashionably_late
+- key: flat_threshold.vwap
+  value: 0.05
+  unit: ratio
+  scope: per_indicator(vwap)
+  dynamic: true
+  status: proposed
+  source: assumed
+  consumers:
+  - fashionably_late
+- key: range_break.failed_trap_bars
+  value: 1
+  unit: bars
+  scope: global
+  dynamic: true
+  status: proposed
+  source: assumed
+  consumers:
+  - Range Break (primitive)
+  - second_chance
+- key: range_break.retest_tolerance_atr
+  value: 0.1
+  unit: atr
+  scope: global
+  dynamic: true
+  status: proposed
+  source: assumed
+  consumers:
+  - cobalt.radar.anatomy.range_break (event(retest))
 ```
 <!-- /cobalt:unit tunables:assumed -->
 <!-- /cobalt:section assumed -->
```

6.6 AFTER — `/Users/cobalt/Vault/Think/1 - Trading/Assumed Defaults.md`, Read WHOLE (49 lines):
````markdown
# Assumed defaults

Defaults the radar runs on until each one is ruled. A row stops being assumed only when
its `source` reads `ruling`; an edited value with `source: assumed` keeps the mark.

<!-- cobalt:section assumed -->
<!-- cobalt:unit tunables:assumed -->
```yaml
tunables:
- key: flat_threshold.ema9
  value: 0.05
  unit: ratio
  scope: per_indicator(ema9)
  dynamic: true
  status: proposed
  source: assumed
  consumers:
  - fashionably_late
- key: flat_threshold.vwap
  value: 0.05
  unit: ratio
  scope: per_indicator(vwap)
  dynamic: true
  status: proposed
  source: assumed
  consumers:
  - fashionably_late
- key: range_break.failed_trap_bars
  value: 1
  unit: bars
  scope: global
  dynamic: true
  status: proposed
  source: assumed
  consumers:
  - Range Break (primitive)
  - second_chance
- key: range_break.retest_tolerance_atr
  value: 0.1
  unit: atr
  scope: global
  dynamic: true
  status: proposed
  source: assumed
  consumers:
  - cobalt.radar.anatomy.range_break (event(retest))
```
<!-- /cobalt:unit tunables:assumed -->
<!-- /cobalt:section assumed -->
````

| step | command | result |
|---|---|---|
| 6.6 PARSER PROOF (L65) | `COBALT_ENV=production COBALT_VAULT_PATH=/Users/cobalt/Vault/Think uv run cobalt taxonomy tunables --assumed` | `assumed  flat_threshold.ema9                      unit=ratio scope=per_indicator(ema9) value=0.05 consumers=['fashionably_late'] page=—` · `assumed  flat_threshold.vwap                      unit=ratio scope=per_indicator(vwap) value=0.05 consumers=['fashionably_late'] page=—` · `assumed  range_break.failed_trap_bars             unit=bars scope=global value=1 consumers=['Range Break (primitive)', 'second_chance'] page=—` · `assumed  range_break.retest_tolerance_atr         unit=atr scope=global value=0.1 consumers=['cobalt.radar.anatomy.range_break (event(retest))'] page=—` · `hole     dist.k.vwap                              unit=atr scope=per_indicator(vwap) value=None consumers=['vwap_continuation'] page=—` · `hole     leg.min_size_atr                         unit=atr scope=global value=None consumers=['cobalt.radar.anatomy.leg_roles (Leg(pullback), Leg(impulse))'] page=—` · summary `4 assumed row(s), 22 engine hole(s) still null. Writes: none.` — **PARSER PROOF GREEN** |

6.7 RESIDENTS (`<t write>` 15:18:04):

| row | `date` | command | result |
|---|---|---|---|
| counts | `15:18:29` | `grep -c "Traceback" logs/radar.err` / `grep -c "TaxonomyConfigError" logs/radar.err` / `grep -c "Traceback" logs/aset.err` / `grep -c "radar panel FAILED" logs/aset.err` / `grep -c "radar pool refresh FAILED" logs/aset.err` | `0` = `<tr0>` / `0` = `<tc0>` / `2` = `<ta0>` / `17` = `<rp_up>` / `58` = `<rpr_up>` — EQUAL |
| curl | `15:18:29` | `curl … /radar` | `200` |
| heartbeat | `15:18:34` | `heartbeat show` | `HEARTBEAT RED — 1 probe(s)  (2026-09-24 15:18:34 EDT)` · only RED `RED  radar                    failed_stage bars: poll failures: 1` · `OK   com.cobalt.radar             running   running 116 min, heartbeat fresh` · no `failed_stage evaluate` — the carried bars kind (differs from `<hb0>` GREEN; watched below) |
| heartbeat | `15:18:44` | `heartbeat show` | same: `RED  radar  failed_stage bars: poll failures: 1` |
| filler | `15:18:54` … `15:19:30` (≈every 3 s, 11 reads) | `heartbeat show` | each `HEARTBEAT RED — 1 probe(s)` · only `RED  radar  failed_stage bars: poll failures: 1` · `com.cobalt.radar running 116–117 min, heartbeat fresh` |
| tail 1 | `15:19:34` (`<t write>` + 90 s) | `tail -n 12 logs/radar.err` | cycles every ≈185 s from `14:44:07` to **`2026-09-24 15:18:05.678 \| INFO     \| cobalt.radar.runner:resident:459 - radar cycle: scanning scan_id=1790277399978`** — a cycle stamped after `<t write>`; no error, no traceback, no `TaxonomyConfigError` in the tail → radar-cycle bullet GREEN |
| filler | `15:19:47` … `15:20:53` (≈every 3 s, 23 reads) | `heartbeat show` | each `HEARTBEAT RED — 1 probe(s)` · only `RED  radar  failed_stage bars: poll failures: 1` · radar `running … heartbeat fresh` · never `failed_stage evaluate` |
| heartbeat | `15:20:58` · `15:21:00` | `heartbeat show` | **`HEARTBEAT GREEN — 16 job(s), 12 probe(s), nothing red  (2026-09-24 15:20:58 EDT)`** · `OK   radar                    scanning (rth), members 50` — the bars finding CLEARED; same as `<hb0>` again |
| tail 2 | `15:21:04` (`<t write>` + 180 s) | `tail -n 12 logs/radar.err` | unchanged: last line `15:18:05.678 … radar cycle: scanning scan_id=1790277399978` (cadence ≈185 s; next due ≈15:21:11); no error lines |
| filler | `15:21:12` … `15:23:02` (≈every 3 s, 37 reads) | `heartbeat show` | each `HEARTBEAT GREEN — 16 job(s), 12 probe(s), nothing red` · `OK   radar  scanning (rth), members 50` |
| counts | `15:22:12` | the five `grep -c` rows | `0` / `0` / `2` / `17` / `58` — EQUAL to `<tr0>` / `<tc0>` / `<ta0>` / `<rp_up>` / `<rpr_up>` |
| curl | `15:22:12` | `curl … /radar` | `200` |
| tail 3 | `15:23:04` (`<t write>` + 300 s) | `tail -n 12 logs/radar.err` | new last line **`2026-09-24 15:21:11.419 \| INFO     \| cobalt.radar.runner:resident:459 - radar cycle: scanning scan_id=1790277585709`** — a second full cycle after `<t write>`; no error lines |

6.7 VERDICT: **residents CLEAN** — counts equal at 15:18:29 and 15:22:12, `/radar` 200 both times, two radar cycles after `<t write>` (15:18:05, 15:21:11) with no error line, and the heartbeat ended at the same kind as `<hb0>` (GREEN from 15:20:58 through 15:23:02). Between 15:18:34 and 15:20:53 the heartbeat read `RED  radar  failed_stage bars: poll failures: 1`. That is the carried bars kind this prompt accepts for `<hb0>` itself (the reland saw the same kind at 13:23 and it cleared at 13:27). There was never a `failed_stage evaluate`, and it cleared by itself. Recorded under ESCALATE 5, not treated as a resident RED.

6.8 LIVE-NOTE RUN (on `a0ba0098`, gate worktree, no `.env`; reads his vault, writes nothing):

| step | command | result |
|---|---|---|
| cwd | `cd /Users/cobalt/cobalt-wt/stacked-0923` | ok |
| gate HEAD | `git -C /Users/cobalt/cobalt-wt/stacked-0923 rev-parse --short HEAD` | `a0ba0098` — EQUAL |
| gate status | `git -C /Users/cobalt/cobalt-wt/stacked-0923 status --short --branch` | exactly `## deploy/stacked-0923` |
| gate `.env` | `ls -la /Users/cobalt/cobalt-wt/stacked-0923/.env` | exit 1 `No such file or directory` |
| run | `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs tests/cobalt/test_radar_evaluate.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` (foreground) | **`131 passed, 15 warnings in 23.90s`**: 0 failed, 0 errors, no `SKIPPED` line (none names `COBALT_LIVE_VAULT_ROOT`). The 15 warnings are all litellm `asyncio.iscoroutinefunction` DeprecationWarnings. AWAITING lines, exactly: `AWAITING A RULING: backside` · `AWAITING A RULING: fashionably-late` · `AWAITING A DAY: hitchhiker` · `AWAITING ITS ENGINE FILL: vwap-continuation (dist.k.vwap null)`. The second-chance pin LIFTED (`second-chance: ['avoided', 'formed', 'not_formed']`, `evaluable=True missing=[]`); the vwap-continuation pin HOLDS |
| back | `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` | listed (`-rw-------  1 cobalt  staff  2186 Sep  9 16:58`) — cwd back; `date` `15:23:50` |

R119 live-note: GREEN — `131 passed, 15 warnings in 23.90s` · AWAITING: `backside` (ruling) · `fashionably-late` (ruling) · `hitchhiker` (day) · `vwap-continuation (dist.k.vwap null)` (engine fill)

R119: WRITTEN — note created, 4 rows (R119 ×2 + R82 ×2; dist.k.vwap held, R118), parser proof green — radar load OWED (cobalt taxonomy load, desk job)

## ESCALATE
1. **Radar load OWED, a desk job on his word.** The four rows are in his note (write_ids 3579 / 3581) but not in the radar's DB copy. `cobalt taxonomy load` was NOT run (by rule). Until it runs, production keeps reading the engine holes. `ASK DESK: run cobalt taxonomy load now that the note holds the four rows (his word)? [15:23]`. Safe default taken: not run.
2. **Rollback order now binds.** Once the load runs, `ADDING-A-SETUP.md` § "Rolling back after the assumed note" applies. The order is: empty the `tunables:assumed` unit and re-run `taxonomy load` first, then revert the code, then revert migration 0013. Any rollback of `a2d320b8` must follow that order. That is on top of the `card_dots` ASSUMED-row order in `deploy-2026-09-24-reland.md` ESCALATE 6.
3. `dist.k.vwap` (A-16) stays HELD for his VWAP Continuation sitting (R118; `cto-2026-09-24.md` R13 / R14). vwap-continuation stays pinned (`AWAITING ITS ENGINE FILL`, confirmed by 6.8). `leg.min_size_atr` (A-24) stays NULL (R119, unanimous).
4. **Dry-run defect → BACKLOG.** `taxonomy assumed write --dry-run` REFUSES on an absent note (`upsert_unit never creates a note — call create_if_absent() with a template first (L28.1)`, reland 6.4). `--apply` creates the note and then upserts. The dry run must preview the create as well. This run skipped 6.4 on R55 only. The defect is not fixed.
5. Heartbeat transient, not RED: from 15:18:34 to 15:20:53 the heartbeat read `RED  radar  failed_stage bars: poll failures: 1`. That is the carried bars kind, the same kind the reland saw at 13:23–13:27. It cleared at 15:20:58, and the heartbeat stayed GREEN through 15:23:02. It never read `failed_stage evaluate`, all counts stayed equal, and radar cycles kept logging with no error line. This run did not tie it to the note: the radar reads the DB copy, and `taxonomy load` did not run. The desk may judge otherwise.

Artifacts left as they were (cleanup still owed per reland ESCALATE 10): the rows file `/Users/cobalt/cobalt-wt/r119-rows-0923/assumed-rows.yaml` (user data, never committed) and the gate worktree `stacked-0923` (untouched, HEAD `a0ba0098`, no `.env`).

## CONTINUE
next: none — run ended (STEP-7). A relaunch reads 6.5 WRITTEN (write_ids 3579 / 3581) and 6.6 reached → nothing to re-run; the desk decides.

(history) next: 6.8 live-note run (6.7 residents CLEAN 15:23:04; 6.6 parser GREEN; 6.5 WRITTEN 15:18:04, write_ids 3579 / 3581)

ASSUMED ROWS WRITTEN · rows: 4 · write_ids: 3579/3581 · parser: GREEN · residents: CLEAN · live-note: 131 passed, 0 failed · ESCALATE: 5
