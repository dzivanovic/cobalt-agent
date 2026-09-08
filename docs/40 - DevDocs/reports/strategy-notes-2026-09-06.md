# Strategy note set — vault hand-work, 2026-09-06

Opus 5 on the write path (L29 satisfied). Code freeze respected: nothing under
`src/`, `tests/`, `migrations/`, `configs/` was read anything but read-only, no
database connection was opened, nothing was committed. Writes landed in the live
vault only, resolved through `cobalt.vault.resolve_vault_path()`
(`COBALT_ENV=production`, `COBALT_VAULT_PATH=/Users/cobalt/Vault/Think`).
`com.cobalt.obsidian` confirmed running (PID 66104, exit 0) before the first
write and again immediately before the live run.

## Backup

    /tmp/strategies-backup-20260906-092125

Four files, copied with `cp -p` before any edit:
`Back Through Open.md`, `Backside Scalp.md`, `Second Chance Scalp.md`,
`Second Day Play.md`.

This backup is the ONLY rollback for this batch — see ESCALATE #15.

## Write scope actually touched

- `1 - Trading/4 - Strategies/` — 18 created, 4 amended in place = 22 notes.
- `5 - Templates/Strategy.md` — created.

Nothing else in the vault was written.

## The 22 slugs

Created (18):

| slug | file |
|---|---|
| hitchhiker | Hitchhiker.md |
| fashionably-late | Fashionably Late.md |
| rubberband | Rubberband.md |
| big-dog | Big Dog.md |
| off-sides | Off Sides.md |
| opening-range-break | Opening Range Break.md |
| premarket-high-break | Premarket High Break.md |
| three-thirty | The 3:30 Trade.md |
| vwap-continuation | VWAP Continuation.md |
| nine-ema-reclaim | 9 EMA Reclaim.md |
| nine-ema-scalp | 9 EMA Scalp.md |
| bella-fade | Bella Fade.md |
| first-move-down | First Move Down.md |
| first-move-up | First Move Up.md |
| first-vwap-pullback | First VWAP Pullback.md |
| spencer-scalp | Spencer Scalp.md |
| gap-give-and-go | Gap Give and Go.md |
| bouncy-ball | Bouncy Ball.md |

Amended in place (4): `second-chance` → Second Chance Scalp.md ·
`backside` → Backside Scalp.md · `back-through-open` → Back Through Open.md ·
`second-day-play` → Second Day Play.md.

**Duplicate check: clean.** The whole vault (424 notes) was indexed by filename
and searched for every display name. The only hits were the four known notes.
`6 - Permanent/Memory/areas/rubberband-training.md` (and its `_imports` copy) is
the Playbook-Trainer *program* note, not a Rubberband strategy note — checked and
ruled a non-collision, not a duplicate. No note for any of the 22 slugs existed
under any other name, so the STOP condition never fired.

## YAML → slug map

13 committed defs in `configs/cobalt/taxonomy/trade_defs/`, all matched, **zero
unmatched YAML**. The map is hand-made: file stem / `trade_def.id` is snake_case,
the vault slug is kebab-case, and the two are not mechanically inter-derivable
(see ESCALATE #2).

| YAML file | `trade_def.id` | `trade_def.name` | → slug |
|---|---|---|---|
| back_through_open.yaml | back_through_open | Back-Through Open | back-through-open |
| backside.yaml | backside | Back$ide Scalp | backside |
| bella_fade.yaml | bella_fade | Bella Fade | bella-fade |
| big_dog.yaml | big_dog | Big Dog Consolidation | big-dog |
| bouncy_ball.yaml | bouncy_ball | Bouncy Ball | bouncy-ball |
| ema9_scalp.yaml | ema9_scalp | 9 EMA Scalp | nine-ema-scalp |
| fashionably_late.yaml | fashionably_late | Fashionably Late Scalp | fashionably-late |
| first_vwap_pullback.yaml | first_vwap_pullback | First VWAP Pullback | first-vwap-pullback |
| gap_give_and_go.yaml | gap_give_and_go | Gap, Give and Go | gap-give-and-go |
| hitchhiker.yaml | hitchhiker | Hitchhiker Scalp | hitchhiker |
| rubberband.yaml | rubberband | Rubber Band Scalp | rubberband |
| second_chance.yaml | second_chance | Second Chance Scalp | second-chance |
| vwap_continuation.yaml | vwap_continuation | VWAP Continuation | vwap-continuation |

## Populated Definition units — 13, `status: defined`

back-through-open · backside · bella-fade · big-dog · bouncy-ball ·
fashionably-late · first-vwap-pullback · gap-give-and-go · hitchhiker ·
nine-ema-scalp · rubberband · second-chance · vwap-continuation

Each unit holds the committed YAML file **verbatim, comments included** (schema
v0.4 as committed), inside one ```` ```yaml ```` fence. No def was invented, no
field reworded.

**v0.3 migration: not applicable, and none exists.** All 13 files declare
`Schema: TAXONOMY-DRAFT-v0_7.md §10.1 (schema v0.4)` in their own headers and all
13 validate against the current model unchanged. A grep of
`src/cobalt/taxonomy/*.py` for any migration path found none — there is no
importable v0.3→v0.4 migration in the repo (only a stale docstring in
`taxonomy/__init__.py` still saying "v0.6 §10, schema v0.3"). Copied as-is, as
instructed; flagged as ESCALATE #5.

## Empty Definition units — 9, `status: draft`

first-move-down · first-move-up · nine-ema-reclaim · off-sides ·
opening-range-break · premarket-high-break · second-day-play · spencer-scalp ·
three-thirty

**Count confirmed: 9, and the set is exactly the one predicted in the task.**
22 slugs − 13 committed defs = 9. No def was invented for any of them.

## Verification

Run against the live vault after the write (`verify.py`, read-only):

    FILES: 22 (expected 22)
    POPULATED (status defined): 13
    EMPTY UNIT (status draft): 9
    FAILURES: 0

What was checked, per note:

1. **22 files, one per slug, no extras** — directory listing is exactly 22 `.md`,
   every `trade_def:` is one of the 22 canonical slugs, no slug seen twice, no
   slug missing, and each slug's file name matches its ruled display name.
2. **Frontmatter parses** — `python-frontmatter` `frontmatter.load()` on every
   note, plus a presence check for `trade_def`, `name`, `category`, `sides`,
   `working_timeframe`, `status`, `source`. (python-frontmatter is not a project
   dependency; it was supplied by an ephemeral `uv run --with` overlay, which
   does not touch `pyproject.toml` or `uv.lock` — see ESCALATE #14.)
3. **Every unit resolvable** — `markers.find_section(lines, "definition")` and
   `markers.find_section(lines, "stats")` both return a block, and
   `trade_def:<slug>` / `stats:<slug>` are both present in `block.units`. All 44
   units resolved.
4. **Every populated unit round-trips the v0.4 model** — the fenced body is
   `yaml.safe_load`-ed and passed to `TradeDef(**raw["trade_def"])`, the exact
   call `loader.load_trade_defs()` makes. Import-only; no code changed. 13/13
   constructed clean.
5. **status agrees with the unit** — `defined` iff the unit holds a def that
   validated; `draft` iff the unit body is empty. No mismatches.

The same script was run first against a sandbox copy of the four notes in the
scratchpad; the live write only happened after that dry run came back green.

## The four diffs

Three of the four are **additions only**. The fourth carries the one ruled
exception plus one newline-termination artifact, both shown below.

### The ruled line — `Second Chance Scalp.md`

```diff
-strategy: Second Day Play
+strategy: Second Chance Scalp
```

That is the only human-authored line changed anywhere in this batch.

### The one other non-addition — `Second Chance Scalp.md`, end of file

```diff
-- 1.9 to 1 Reward to Risk ratio
\ No newline at end of file
+- 1.9 to 1 Reward to Risk ratio
+
```

The file had no terminating newline. Appending required terminating the last
line. The line's **content is byte-identical**; only the missing `\n` was added.
No prose was altered. Called out rather than buried because it is technically a
`-` line in the diff.

Full unified diffs follow.

### `Back Through Open.md`

```diff
--- a/Back Through Open.md
+++ b/Back Through Open.md
@@ -1,4 +1,117 @@
 ---
 aliases:
 strategy: Back Through Open
+trade_def: back-through-open
+name: Back Through Open
+category:
+sides: [long, short]
+working_timeframe: 2m
+status: defined
+source: SMB cheat sheet
 ---
+
+## Why it works
+
+## Rules
+
+## My rulings
+
+## Definition
+<!-- cobalt:section definition -->
+<!-- cobalt:unit trade_def:back-through-open -->
+```yaml
+# Source: TRADE-DEFS-BATCH2-v0_1.md §B.5 (SMB Back-Through Open sheet).
+# Schema: TAXONOMY-DRAFT-v0_7.md §10.1 (schema v0.4) + §A amendments
+# (v0.7 extensions, TRADE-DEFS-BATCH2-v0_1.md §A).
+# NOTE: trigger.params.ref = "open" applies A.5 (Level.type gains `open`,
+# the RTH opening print) — encoded as a free-text Level_ref value, same
+# as every other trigger-params anchor; no schema change needed (see
+# ADR-0002).
+# v0.7 §10.1/§10.2: trail on: entry, conditions [prior_bar_break 1,
+# ma_close EMA9] — moved into the trade_def.trail slot; the exit leg
+# below carries no params (one-stop law).
+trade_def:
+  id: back_through_open
+  name: Back-Through Open
+  aliases: [BTO, "Back Through Open"]
+  family: [opening_drive, continuation]
+  class: move2move  # RULED
+  valid_setups:
+    - {setup_ref: gap_and_go, relation: with_trend}
+    - {setup_ref: gap_down_into_support, relation: countertrend}
+    - {setup_ref: gap_up_into_resistance, relation: countertrend}
+    - {setup_ref: day2_continuation, relation: with_trend}
+    - {setup_ref: range_break, relation: with_trend}
+  entry_mode: front_side
+  preconditions:
+    - expr: "InPlay.state == active"
+    - expr: "Gap.instantiated"  # "big gap up"
+    - expr: "Catalyst.grade >= 8"  # avoid entirely if the catalyst is not at least an 8+
+    - expr: "Leg(opening_drive).direction == opposite(Gap.direction)"  # the initial downtick
+  trigger:
+    type: bar_break
+    params: {ref: "Level_ref(open)"}
+    confirmation_policy: {type: intrabar}  # "aggressively when price crosses back through the opening price"
+  stop:
+    placement:
+      type: structural_extreme
+      ref: turn_low
+      buffer: {type: fixed, cents: {value: "cfg(back_through_open.stop.buffer)", dynamic: false}}  # sheet 0.01 -> RULED 0.02 (A.6, tunables.yaml sheet_value)
+      floor: config
+    evaluation: touch  # "LOD" = tracked low
+  stop_management:
+    - type: time_stop
+      duration_bars: {value: 2, dynamic: false}
+      condition: "no progress from entry"  # "should work right away — no chop or pause after entry"
+      "on": {name: entry}
+  trail:
+    conditions:
+      - {type: prior_bar_break, n: 1}
+      - {type: ma_close, ma: {value: EMA9, dynamic: false}}
+    mode: select
+    "on": {name: entry}
+  exit:
+    - fraction: 1.0
+      target_type: trail  # no params — trade_def.trail defines the conditions (one-stop law)
+      params: {}
+      evaluation: close_through
+      computable: cobalt  # "close below the 9 EMA or a two-bar break" -> 1-bar trail law
+  on_cic: {triggers: [1, 2, 3, 4], action: exit_all}   # advisory
+  max_attempts: {value: 1, dynamic: false, note: "sheet: we will only try this trade once"}
+  add_policy: {type: none}
+  avoid:
+    - expr: "Regime.label IN {range_bound, fading}"  # "does not work in a range-bound market or one fading moves"
+    - text: "chop or pause after entry (mechanised via time_stop)"
+  quality_factors:
+    - catalyst_grade
+    - cross_time_since_open  # <=5 min guide
+    - downtick_depth  # small = pos
+    - post_cross_momentum
+    - daily_chart_breakout
+    - market_momentum  # aggressive = pos
+    - rvol
+    - trail_fit  # v0.7 §14 c.1 — cobalt-computable, which trail capability the stock cleanly follows
+    - setup_relation
+    - market_alignment  # opposite trend = neg
+    - sector_alignment
+  preferred_windows: [open_drive]
+  preferred_windows_ref: "First 5 minutes of the trading day"
+  reference_stats: null
+```
+<!-- /cobalt:unit trade_def:back-through-open -->
+<!-- /cobalt:section definition -->
+
+## Instances
+```dataview
+TABLE date, side, result_r, grade FROM "1 - Trading/2 - Trades"
+WHERE trade_def = "back-through-open" SORT date DESC
+```
+
+## Stats
+<!-- cobalt:section stats -->
+<!-- cobalt:unit stats:back-through-open -->
+n: insufficient data (n<30)
+<!-- /cobalt:unit stats:back-through-open -->
+<!-- /cobalt:section stats -->
+
+## Notes & research
```

### `Backside Scalp.md`

```diff
--- a/Backside Scalp.md
+++ b/Backside Scalp.md
@@ -2,6 +2,13 @@
 aliases:
 strategy: Backside Scalp
 strikes: "1"
+trade_def: backside
+name: Backside Scalp
+category:
+sides: [long, short]
+working_timeframe: 2m
+status: defined
+source: SMB cheat sheet
 ---
 
 ![[Pasted image 20250829155631.png]]
@@ -64,3 +71,90 @@
 - 50 - 60% win rate
 - 1.4 to 1 Reward to Risk ratio
 
+
+## My rulings
+
+## Definition
+<!-- cobalt:section definition -->
+<!-- cobalt:unit trade_def:backside -->
+```yaml
+# Source: TRADE-DEFS-BATCH1-v0_1.md §B.4 (SMB Back$ide Scalp sheet).
+# Schema: TAXONOMY-DRAFT-v0_7.md §10.1 (schema v0.4).
+# No trail slot: single VWAP exit target, not a trail.
+trade_def:
+  id: backside
+  name: "Back$ide Scalp"
+  aliases: ["Backside Scalp"]
+  family: [reversion]
+  class: scalp
+  valid_setups:
+    - {setup_ref: gap_down_into_support, relation: countertrend}
+    - {setup_ref: gap_up_into_resistance, relation: countertrend}
+    - {setup_ref: day2_continuation, relation: with_trend}
+    - {setup_ref: overextension, relation: countertrend}
+    - {setup_ref: volatility_in_range, relation: countertrend}
+  tf_ceiling: 15
+  entry_mode: backside
+  preconditions:
+    - expr: "Extension.state == backside"  # >=1 HH + >=1 HL above rising 9 EMA
+    - expr: "Range(micro).instantiated AND Range(micro).low > EMA9 AND EMA9.slope > 0"
+  trigger:
+    type: range_break
+    params: {ref: "Range(micro).top"}
+    confirmation_policy: {type: intrabar}
+  stop:
+    placement:
+      type: structural_extreme
+      ref: recent_higher_low  # micro-Range base pivot
+      buffer: {type: fixed, cents: {value: "cfg(stop.buffer)", dynamic: false}}
+      floor: config
+    evaluation: touch
+  stop_management:
+    - type: time_stop
+      duration_bars: {value: 2, dynamic: false}
+      condition: "no progress from entry in trade direction"
+      "on": {name: entry}
+  exit:
+    - fraction: 1.0
+      target_type: vwap
+      evaluation: touch
+      computable: cobalt
+  on_cic: {triggers: [1, 2, 3, 4], action: exit_all}   # advisory
+  max_attempts: {value: 1, dynamic: false, note: fixed}
+  add_policy: {type: none}
+  avoid:
+    - expr: "RangeBreak(HTF).day_count == 1"  # never on a day-1 HTF breakout
+  quality_factors:
+    - extension_distance_from_vwap
+    - Extension.leg_count
+    - rvol
+    - Range.duration
+    - hh_hl_count
+    - pct_bars_above_ema9_since_low
+    - range_position_lod_to_vwap  # >0.5 good
+    - price_action_consistency
+    - catalyst_ambiguity  # sheet: increase
+    - setup_relation
+    - market_alignment
+    - sector_alignment
+  preferred_windows: [morning, midday]
+  preferred_windows_ref: "sheet: 10:00-13:30"
+  reference_stats: {win_rate: "50-60%", rr: 1.4}
+```
+<!-- /cobalt:unit trade_def:backside -->
+<!-- /cobalt:section definition -->
+
+## Instances
+```dataview
+TABLE date, side, result_r, grade FROM "1 - Trading/2 - Trades"
+WHERE trade_def = "backside" SORT date DESC
+```
+
+## Stats
+<!-- cobalt:section stats -->
+<!-- cobalt:unit stats:backside -->
+n: insufficient data (n<30)
+<!-- /cobalt:unit stats:backside -->
+<!-- /cobalt:section stats -->
+
+## Notes & research
```

### `Second Chance Scalp.md`

```diff
--- a/Second Chance Scalp.md
+++ b/Second Chance Scalp.md
@@ -1,6 +1,13 @@
 ---
-strategy: Second Day Play
+strategy: Second Chance Scalp
 strikes: "2"
+trade_def: second-chance
+name: Second Chance Scalp
+category:
+sides: [long, short]
+working_timeframe: 2m
+status: defined
+source: SMB cheat sheet
 ---
 ![[Pasted image 20250902101053.png]]
 
@@ -67,4 +74,113 @@
 ## Scalp Statistics
 
 - 50-55% win rate
-- 1.9 to 1 Reward to Risk ratio
\ No newline at end of file
+- 1.9 to 1 Reward to Risk ratio
+
+## My rulings
+
+## Definition
+<!-- cobalt:section definition -->
+<!-- cobalt:unit trade_def:second-chance -->
+```yaml
+# Source: TRADE-DEFS-BATCH1-v0_1.md §B.3 (SMB Second Chance Scalp sheet).
+# Schema: TAXONOMY-DRAFT-v0_7.md §10.1 (schema v0.4).
+# NOTE: step 2 (retest) carries no confirmation_policy in the source
+# sheet — trigger.steps[].confirmation_policy is optional in the schema
+# for exactly this reason, rather than inventing a default. CONFIRMED
+# 2026-09-02 (TRADE-DEFS-BATCH2-v0_1.md item 0).
+# v0.7 §14 c.1 RULED: one stop at a time — the trail IS the stop once
+# its on: event fires. Second Chance = hard stop -> trail selected on
+# exit_leg(1) -> leg 2 exits on it (§10.2). trail_ma_close is REMOVED
+# (duplicate spelling); trail_conditions here supersede the 00ff853
+# retrofit (single ma.slow condition) with the full v0.7 §10.2 set.
+trade_def:
+  id: second_chance
+  name: Second Chance Scalp
+  aliases: ["2nd Chance"]
+  family: [range_break]
+  class: scalp
+  valid_setups:
+    - {setup_ref: gap_and_go, relation: with_trend}
+    - {setup_ref: range_break, relation: with_trend}
+  tf_ceiling: 15
+  entry_mode: backside
+  preconditions:
+    - expr: "RangeBreak(level).state == accepted"
+    - expr: "event(retest) on that RangeBreak"
+  trigger:
+    type: sequence
+    steps:
+      - name: break
+        predicate: {expr: "price close_through Level_ref"}
+        confirmation_policy: {type: close_through}
+      - name: retest
+        predicate: {expr: "event(retest)"}
+      - name: turn
+        predicate: {expr: "close_above(prior_bar)"}
+        confirmation_policy: {type: close_through}
+  stop:
+    placement:
+      type: structural_extreme
+      ref: turn_candle
+      buffer: {type: fixed, cents: {value: "cfg(stop.buffer)", dynamic: false}}
+      floor: config
+    evaluation: touch
+  stop_management:
+    - type: fixed
+      "on": {name: entry}
+  trail:
+    conditions:
+      - {type: ma_close, ma: {value: "ma.fast", dynamic: false}}
+      - {type: ma_close, ma: {value: "ma.slow", dynamic: false, note: "config; 20 by price action"}}
+      - {type: prior_bar_break, n: 1}
+    mode: select
+    "on": {name: exit_leg, n: 1}
+  exit:
+    - fraction: 0.5
+      target_type: leg_end
+      params: {leg_index: break_leg}
+      evaluation: touch
+      computable: cobalt
+    - fraction: 0.5
+      target_type: trail  # no params — trade_def.trail defines the conditions (one-stop law)
+      params: {}
+      evaluation: close_through
+      computable: cobalt
+  on_cic: {triggers: [1, 2, 3, 4], action: exit_all}   # advisory
+  max_attempts: {value: 2, dynamic: false, note: "sheet: 2 strikes, never a 3rd"}
+  add_policy: {type: none}
+  avoid:
+    - expr: "RangeBreak.state == failed_trap after event(retest)"  # sheet: back inside, no recovery next candle (N=1)
+    - expr: "event(stop_hit) AND price inside Range(prior)"  # instance dead, no re-entry on break back up
+  quality_factors:
+    - level_significance
+    - break_leg_strength  # range + volume
+    - retest_volume  # low = good
+    - retest_depth
+    - break_leg_range_vs_range_height  # >1 = neg
+    - rvol
+    - trail_fit  # v0.7 §14 c.1 — cobalt-computable, which trail capability the stock cleanly follows
+    - setup_relation
+    - market_alignment
+    - sector_alignment
+  preferred_windows: [morning, midday, afternoon, close]
+  preferred_windows_ref: "sheet: 9:59-4:00"
+  reference_stats: {win_rate: "50-55%", rr: 1.9}
+```
+<!-- /cobalt:unit trade_def:second-chance -->
+<!-- /cobalt:section definition -->
+
+## Instances
+```dataview
+TABLE date, side, result_r, grade FROM "1 - Trading/2 - Trades"
+WHERE trade_def = "second-chance" SORT date DESC
+```
+
+## Stats
+<!-- cobalt:section stats -->
+<!-- cobalt:unit stats:second-chance -->
+n: insufficient data (n<30)
+<!-- /cobalt:unit stats:second-chance -->
+<!-- /cobalt:section stats -->
+
+## Notes & research
```

### `Second Day Play.md`

```diff
--- a/Second Day Play.md
+++ b/Second Day Play.md
@@ -1,6 +1,13 @@
 ---
 strategy: " Second Day Play"
 strikes: "1"
+trade_def: second-day-play
+name: Second Day Play
+category:
+sides: [long, short]
+working_timeframe: 2m
+status: draft
+source: SMB cheat sheet
 ---
 ![[Pasted image 20250902120547.png]]
 
@@ -80,3 +87,26 @@
 
 
 ![[Pasted image 20250902120547.png]]
+
+## My rulings
+
+## Definition
+<!-- cobalt:section definition -->
+<!-- cobalt:unit trade_def:second-day-play -->
+<!-- /cobalt:unit trade_def:second-day-play -->
+<!-- /cobalt:section definition -->
+
+## Instances
+```dataview
+TABLE date, side, result_r, grade FROM "1 - Trading/2 - Trades"
+WHERE trade_def = "second-day-play" SORT date DESC
+```
+
+## Stats
+<!-- cobalt:section stats -->
+<!-- cobalt:unit stats:second-day-play -->
+n: insufficient data (n<30)
+<!-- /cobalt:unit stats:second-day-play -->
+<!-- /cobalt:section stats -->
+
+## Notes & research
```

## Git status of the repo

    $ git status --short
     M "docs/00 - Project/MVP-CHARTER-v0_2.md"
     M "docs/00 - Project/PROJECT-LEDGER.md"
     M "docs/30 - Design/archiver-runs.md"
    ?? "docs/30 - Design/RESEARCH-2026-09-05-memory-and-capture.md"
    ?? "docs/30 - Design/TRADE-RADAR-CARD-MOCK-v0_1/"
    ?? docs/_archive/gemini-era-vault-side/
    ?? "docs/40 - DevDocs/reports/"          <- this report (new untracked dir, collapsed by git)

**Byte-for-byte identical to the session-start snapshot, plus this report file
and nothing else.** The six pre-existing entries were already dirty when the
session opened and were not touched. No `src/`, `tests/`, `migrations/` or
`configs/` path appears. Nothing was committed. `docs/40 - DevDocs/**` is
explicitly un-ignored (`.gitignore:21`), which is why the report is visible to
git at all.

---

# ESCALATE — input to the Tuesday prompt, not work for today

Everything below is something I would have had to change in code, schema or
config to do this job *properly*. None of it was done. Ordered by how much it
blocks the vault-note-is-truth ruling.

**1 — `category:` has no counterpart in schema v0.4.** The skeleton mandates a
`category:` frontmatter key "empty unless the YAML def carries it". No def
carries it, because the schema has no such field — §10.1 has `family[]`
(opening_drive / continuation / range_break / reversion / time_window) and
`class` (scalp / move2move / swing / options). All 22 notes therefore carry an
empty `category:` that nothing can ever fill. Ruling needed: drop the key, alias
it to `class`, alias it to `family[0]`, or add `category` to the schema.

**2 — Nothing owns the slug ↔ `trade_def.id` mapping. This is the big one.**
The vault key is kebab (`back-through-open`), the YAML key is snake
(`back_through_open`), and the two are *not* inter-derivable: `ema9_scalp` →
`nine-ema-scalp` and `second_chance` → `second-chance` cannot be produced by any
rule. I hand-built the 13-row map in this report; it exists nowhere in the
repo. Until a `slug` field lands on `TradeDef`, or a
`configs/cobalt/taxonomy/slugs.yaml` registry exists, or the YAML files are
renamed to the slug, **the loader can never join a vault note to its def** — the
shared key the ruling depends on is currently a table in a markdown report.

**3 — Two display names per trade, no rule for which wins.** The note says
`name: Backside Scalp`, the def says `name: Back$ide Scalp`. Also: Rubberband /
Rubber Band Scalp · Big Dog / Big Dog Consolidation · Gap Give and Go / Gap,
Give and Go · Hitchhiker / Hitchhiker Scalp · Fashionably Late / Fashionably
Late Scalp · Back Through Open / Back-Through Open. Seven of thirteen disagree.
Needs a ruling on which is canonical and whether the other folds into
`aliases[]`.

**4 — There is no loader path for "the def lives in a vault note".**
`load_trade_defs()` reads `configs/cobalt/taxonomy/trade_defs/*.yaml` and nothing
else. After today the same def exists in two places — the YAML file and the
vault unit — which is a one-path-rule violation waiting to be tripped by the
first edit to either copy. Making the vault the source requires a vault-backed
loader (read markers → parse fence → `TradeDef`), and that loader will *fail*
unless three cross-checks move with it: `cameron_grid.yaml` row equality,
`variables/<id>.yaml` ↔ `quality_factors` set equality, and `cfg()` token
resolution. A vault-authored def has none of those files.

**5 — No v0.3→v0.4 migration exists.** Asked for, looked for, not there. All 13
committed defs are already v0.4 so nothing needed migrating today, but if a v0.3
def ever surfaces it will fail loud in `TradeDef` with no migration to reach for.
`src/cobalt/taxonomy/__init__.py:1` still advertises "v0.6 §10, schema v0.3" —
stale docstring, worth a one-line fix when the freeze lifts.

**6 — `working_timeframe: 2m` is a hardcoded duplicate.** Written flat on all 22
per the skeleton. The schema allows a per-trade `working_timeframe` plus a
`tf_ceiling`, and nothing reconciles the frontmatter value against the def's.
Either derive it from the def or add a validator; as written it is a second
source of truth that will silently drift.

**7 — `status:` is unmodelled and hand-maintained.** `draft` / `defined` is not
an enum anywhere, and nothing recomputes it when a unit gains or loses a def. It
is a manually-kept restatement of "is the unit body empty". Should be derived,
not stored — or at minimum validated.

**8 — The stats unit body is free text.** `n: insufficient data (n<30)` is a
string, not a typed row. The sample-size law wants a real shape (`n: 0`,
`status: insufficient`, and the n itself once trades exist) plus the writer that
maintains it. Right now 22 notes carry an unparseable literal.

**9 — Every `## Instances` dataview will render empty, today and after S1.** The
query joins on `trade_def`. I checked all 64 notes in `1 - Trading/2 - Trades/`:
**zero carry a `trade_def:` key.** They carry `strategy:`, as free text, and it
is a mess — 28 blank, and the non-blank values include leading spaces
(`" VWAP Continuation"`, `"  Second Chance Scalp"`), spelling drift
(`Fashionable Late Scalp` vs the note's Fashionably Late; `Offside Scalp` vs Off
Sides; `Puppy Dog Consolidation` *and* `Big Dawg` vs Big Dog), and values that
are not strategies at all (`Breaking News`, `Bad Trade Outside of Playbook`).
Needs: a ruling on `strategy:` → `trade_def:`, a hand-checked backfill of 64
notes against the 22 slugs, and a trade-note template change. Until then the
Instances section is decorative.

**10 — Heading vocabulary in the four legacy notes does not match the skeleton.**
They use "Why the Backside Scalp works:", "The exact rules of entry", "The
Second Day Play dynamics:". I did **not** rename them — a heading is a line of
human prose and renaming it is a modification, not an addition, and it was not
the ruled exception. I treated those headings as satisfying `## Why it works` and
`## Rules` and did not append empty duplicates; `Back Through Open.md` had no
body at all and got the full skeleton. This costs nothing functionally (the
machine-read sections are the marked ones), but if `## Rules` ever has to be
machine-findable, a rename ruling is needed.

**11 — `## Scalp Statistics` and `## Stats` now sit in the same note.** Three
legacy notes carry an SMB-sourced `## Scalp Statistics` (win rate, R:R) and now
also carry Cobalt's `## Stats` marked section. Different things, confusingly
adjacent — and the SMB figures are *already* in the def as `reference_stats`, so
this is a third copy. Needs a rename or a fold.

**12 — `The 3:30 Trade.md` has a colon in its filename.** Legal on APFS through
POSIX and it reads back correctly (verified), but macOS Finder renders it as
`The 3/30 Trade` and Obsidian's own new-note dialog rejects `:`. Created as
ruled; flagging that the display name probably wants to change.

**13 — The template's slug rule cannot produce 3 of the 22 canonical slugs.**
The specified derivation (lowercase, spaces→hyphens, strip punctuation, spell out
a leading digit) gets 19/22 right. It misses `second-chance` (derives
`second-chance-scalp`), `backside` (`backside-scalp`), and `three-thirty`
(`the-3-30-trade`). The rule is lossy because the canonical slugs are shortened
by hand. The template emits the derived slug, a `# FIX` marker if it still starts
with a digit, and a comment telling the author to check the canonical list —
but this is a workaround for the missing registry in #2.

**14 — `python-frontmatter` is not a project dependency.** Verification used an
ephemeral `uv run --with python-frontmatter` overlay, which leaves
`pyproject.toml` and `uv.lock` untouched. If frontmatter parsing becomes part of
any Cobalt read path it has to be added properly.

**15 — This batch has no L28 write record.** Twenty-two live-vault writes went
through hand-work, not `src/cobalt/vaultwrite/`, so there is no `write_id`, no
`vault_writes` row, and `cobalt vault restore --write-id N` cannot roll this
back. The only rollback is `/tmp/strategies-backup-20260906-092125`, which is
not durable across a reboot. **Copy it somewhere real before Tuesday.** If
seeding strategy notes ever needs doing again, it belongs behind the writer.
