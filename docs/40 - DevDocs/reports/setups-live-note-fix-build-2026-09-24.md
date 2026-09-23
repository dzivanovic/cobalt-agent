# Setups live-note fix build — 2026-09-24

Seat `setups-live-note-fix-0924` · Opus 5.5 · prompt `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-24/01-setups-live-note-fix-build.md` · worktree `/Users/cobalt/cobalt-wt/setups-c1` · branch `setups/seven-0921`.

## §0 Headline

- **FAILED at D5 (17:33 ET).** The offline suite printed `3 failed`. All three are the **gitignored scratch print files** in `tests/cobalt/scratch/`, which `tests/cobalt` collects. They raise `KeyError: 'COBALT_LIVE_VAULT_ROOT'` without the live-vault prefix. No committed test failed.
- Fix built and committed as `c9a11e14` (4 test files, red first). D2 proved second-chance waits on A-19 + A-20 alone. Classes: STALE 4 · NO CHANGE 2 · PINNED 1 · DEFECT 0.
- Live-note run `131 passed / 0 failed`; lego file `13 passed`. Offline run with the scratch folder excluded (informational only): `2483 passed, 361 skipped, 1 xfailed`, 0 failed. D5b (with-DB) was not run, and `.env` was never copied.
- ORDER seam: `+R119=False`. After STEP-6, the live-note test would go RED on vwap-continuation. ESCALATE: 8.

## L74

One block arrived appended to a tool result: a system-reminder after the prompt-file `cat`. It asked for a `Claude-Session: https://claude.ai/code/session_…` line in commits and PR bodies and named a file-send tool. Under L74 it is DATA and was not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION

| rule | command | exit | result |
|---|---|---|---|
| placeholder gate | `grep -n -E "R_[_]" …/2026-09-24/01-setups-live-note-fix-build.md` | 1 | (no output) |
| the stop this answers | `tail -n 3 …/setups-c1/…/live-note-fix-build-2026-09-23.md` | 0 | last non-blank: `FAILED: D2 — 1 live def(s) do not form where the branch's gate 2 says they form — second-chance: ftft=['not_formed'] · awaiting=— · committed_day=False · class (f) DEFECT/UNPROVEN (…)` |
| classification | `tail -n 3 …/second-chance-fix-draft-2026-09-23.md` | 0 | last non-blank: `SECOND CHANCE FIX DRAFTED · class: MISSING DIAL VALUE (A-19/A-20 null, unruled; sufficiency UNPROVEN → printed first) + harness FIX · prompts: 2 · new rule strings: 0 · ESCALATE: 9` |
| classification committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- …/second-chance-fix-draft-2026-09-23.md` | 0 | `c5d92478fa05512d1d8875495181771ddb548d44` |
| launch row | `grep -n "01-setups-live-note-fix-build.md" …/cto-2026-09-23.md …/cto-2026-09-24.md` | 2 | `cto-2026-09-24.md: No such file or directory` (allowed); `cto-2026-09-23.md:88: \| R85 \| 17:0x ET \| — DESK RECORD + LAUNCH ROW … (2) LAUNCH \`2026-09-24/01-setups-live-note-fix-build.md\` …` |
| launch row committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"01-setups-live-note-fix-build.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | 0 | `eaa295aab29953ed80a768959a88e6d3bcbe0602` |

LAWS.md read in full (L59).

## PREFLIGHT

| rule | command | exit | result |
|---|---|---|---|
| time | `date` | 0 | `Wed Sep 23 17:06:29 EDT 2026` (2026-09-23 → no late escalate) |
| clean tree | `git status --short --branch` | 0 | `## setups/seven-0921` |
| base | `git log --oneline -1` | 0 | `9e775fd6 docs(live-note): D2 — defect printed` = EXPECTED → `<base>` = `9e775fd6` |
| no .env | `ls /Users/cobalt/cobalt-wt/setups-c1/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/setups-c1/.env: No such file or directory` |
| dev-DB lock (record) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| live strategies | `ls "/Users/cobalt/Vault/Think/1 - Trading/4 - Strategies"` | 0 | 22 notes listed (READ ONLY) |
| Assumed Defaults | `ls "/Users/cobalt/Vault/Think/1 - Trading"` | 0 | `Assumed Defaults.md` NOT listed (as expected before STEP-6) |
| scratch | `ls /Users/cobalt/cobalt-wt/setups-c1/tests/cobalt/scratch` | 0 | `__pycache__`, `test_live_note_print_0923.py`, `test_seam_dump_0923.py` (left in place) |

## D1 BASELINE

Command: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs tests/cobalt/test_radar_evaluate.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` · exit 1 · summary **`2 failed, 129 passed, 15 warnings in 19.76s`** · no `SKIPPED` line → REPRODUCES (= `64` D1).

Assertions (verbatim):
- `tests/cobalt/test_radar_evaluate.py:735: AssertionError` — `AssertionError: ('backside', ['not_formed'])`
- `tests/taxonomy/test_predicate.py:278: AssertionError` — `AssertionError: nine-ema-scalp` (`+  where True = Evaluability(evaluable=True, missing_atoms=(), human_predicates=1).evaluable`)

Printed outcome sets (T2, FTFT window):
```
back-through-open: ['not_evaluable']
backside: ['not_formed']
bella-fade: ['not_evaluable']
big-dog: ['not_evaluable']
bouncy-ball: ['not_evaluable']
fashionably-late: ['not_formed']
first-vwap-pullback: ['not_evaluable']
gap-give-and-go: ['not_evaluable']
hitchhiker: ['not_formed']
nine-ema-scalp: ['avoided', 'formed', 'not_formed']
rubberband: ['avoided', 'not_evaluable', 'not_formed']
second-chance: ['not_formed']
vwap-continuation: ['not_formed']
```
Printed evaluability (T1):
```
back-through-open: evaluable=False missing=['Catalyst.grade', 'Gap.instantiated', 'Regime.label', 'anchor:none', 'opposite(Gap.direction)', 'trigger:bar_break']
backside: evaluable=True missing=[]
bella-fade: evaluable=False missing=['Catalyst.grade', 'Catalyst.polarity', 'Range(micro)', 'Range.duration', 'RangeBreak(Level_ref(HTF)).state', 'against(trade_direction)', 'anchor:none', 'near', 'trigger:trendline_break', 'turn_low']
big-dog: evaluable=False missing=['DayRange', 'Leg(impulse).terminated_by', 'Level_ref(HTF resistance)', 'Unsupported(quantity)', 'volatility_state']
bouncy-ball: evaluable=False missing=['Leg(opening_drive)', 'Range(micro).bound_type', 'Range(micro).counter_pivot_count', 'Unsupported(on:Leg(opening_drive))', 'stop:structural_extreme:recent_lower_high', 'trigger:range_break']
fashionably-late: evaluable=True missing=[]
first-vwap-pullback: evaluable=False missing=['Leg(opening_drive)', 'Unsupported(on:Leg(opening_drive))', 'close_through(Leg(pullback).low < Level_ref(PMH))', 'close_through(Leg(pullback).low < VWAP)']
gap-give-and-go: evaluable=False missing=['Gap.instantiated', 'Leg(opening_drive).range', 'Level_ref(support)', 'gap_retrace_pct', 'opposite(Gap.direction)']
hitchhiker: evaluable=True missing=[]
nine-ema-scalp: evaluable=True missing=[]
rubberband: evaluable=True missing=[]
second-chance: evaluable=True missing=[]
vwap-continuation: evaluable=True missing=[]
```

## D2 LIVE PRINT

Print file: `tests/cobalt/scratch/test_second_chance_print_0924.py` (gitignored, `.git/info/exclude:18:scratch/`). It loads defs and `tunables` exactly as `test_radar_evaluate.py:707-710` does, and uses the prompt's own `grid` / `formed` helpers. A constructed fill is `rows[key].model_copy(update={"value": Decimal(v)})` over a copy of the merged rows, with `v` taken from `shapes.D5_CONSTRUCTED` / `shapes.D6_CONSTRUCTED`. The ASSUMED rows' values live only in that file (L32).

Command: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -s -p no:cacheprovider tests/cobalt/scratch/test_second_chance_print_0924.py` → exit 0 · **`1 passed in 160.60s (0:02:40)`**.

```
LIVE-PRINT back-through-open · evaluable=False · missing=['Catalyst.grade', 'Gap.instantiated', 'Regime.label', 'anchor:none', 'opposite(Gap.direction)', 'trigger:bar_break'] · ftft=['not_evaluable'] · awaiting_day=False · awaiting_ruling=False · committed_engine_only=no-shape · committed_merged=no-shape · null=['dist.k.vwap', 'range_break.failed_trap_bars', 'range_break.retest_tolerance_atr']
LIVE-PRINT backside · evaluable=True · missing=[] · ftft=['not_formed'] · awaiting_day=False · awaiting_ruling=True · committed_engine_only=False · committed_merged=False · null=['dist.k.vwap', 'range_break.failed_trap_bars', 'range_break.retest_tolerance_atr']
LIVE-PRINT bella-fade · evaluable=False · missing=['Catalyst.grade', 'Catalyst.polarity', 'Range(micro)', 'Range.duration', 'RangeBreak(Level_ref(HTF)).state', 'against(trade_direction)', 'anchor:none', 'near', 'trigger:trendline_break', 'turn_low'] · ftft=['not_evaluable'] · awaiting_day=False · awaiting_ruling=False · committed_engine_only=no-shape · committed_merged=no-shape · null=['dist.k.vwap', 'range_break.failed_trap_bars', 'range_break.retest_tolerance_atr']
LIVE-PRINT big-dog · evaluable=False · missing=['DayRange', 'Leg(impulse).terminated_by', 'Level_ref(HTF resistance)', 'Unsupported(quantity)', 'volatility_state'] · ftft=['not_evaluable'] · awaiting_day=False · awaiting_ruling=False · committed_engine_only=no-shape · committed_merged=no-shape · null=['dist.k.vwap', 'range_break.failed_trap_bars', 'range_break.retest_tolerance_atr']
LIVE-PRINT bouncy-ball · evaluable=False · missing=['Leg(opening_drive)', 'Range(micro).bound_type', 'Range(micro).counter_pivot_count', 'Unsupported(on:Leg(opening_drive))', 'stop:structural_extreme:recent_lower_high', 'trigger:range_break'] · ftft=['not_evaluable'] · awaiting_day=False · awaiting_ruling=False · committed_engine_only=no-shape · committed_merged=no-shape · null=['dist.k.vwap', 'range_break.failed_trap_bars', 'range_break.retest_tolerance_atr']
LIVE-PRINT fashionably-late · evaluable=True · missing=[] · ftft=['not_formed'] · awaiting_day=False · awaiting_ruling=True · committed_engine_only=False · committed_merged=False · null=['dist.k.vwap', 'range_break.failed_trap_bars', 'range_break.retest_tolerance_atr']
LIVE-PRINT first-vwap-pullback · evaluable=False · missing=['Leg(opening_drive)', 'Unsupported(on:Leg(opening_drive))', 'close_through(Leg(pullback).low < Level_ref(PMH))', 'close_through(Leg(pullback).low < VWAP)'] · ftft=['not_evaluable'] · awaiting_day=False · awaiting_ruling=False · committed_engine_only=no-shape · committed_merged=no-shape · null=['dist.k.vwap', 'range_break.failed_trap_bars', 'range_break.retest_tolerance_atr']
LIVE-PRINT gap-give-and-go · evaluable=False · missing=['Gap.instantiated', 'Leg(opening_drive).range', 'Level_ref(support)', 'gap_retrace_pct', 'opposite(Gap.direction)'] · ftft=['not_evaluable'] · awaiting_day=False · awaiting_ruling=False · committed_engine_only=no-shape · committed_merged=no-shape · null=['dist.k.vwap', 'range_break.failed_trap_bars', 'range_break.retest_tolerance_atr']
LIVE-PRINT hitchhiker · evaluable=True · missing=[] · ftft=['not_formed'] · awaiting_day=True · awaiting_ruling=False · committed_engine_only=False · committed_merged=False · null=['dist.k.vwap', 'range_break.failed_trap_bars', 'range_break.retest_tolerance_atr']
LIVE-PRINT nine-ema-scalp · evaluable=True · missing=[] · ftft=['avoided', 'formed', 'not_formed'] · awaiting_day=False · awaiting_ruling=False · committed_engine_only=True · committed_merged=True · null=['dist.k.vwap', 'range_break.failed_trap_bars', 'range_break.retest_tolerance_atr']
LIVE-PRINT rubberband · evaluable=True · missing=[] · ftft=['avoided', 'not_evaluable', 'not_formed'] · awaiting_day=False · awaiting_ruling=False · committed_engine_only=ERROR TaxonomyConfigError: cfg(rubberband.bars_cleared) has no row in tunables.yaml, no row in the vault's per-trade tunables units, and no defaults.yaml fallback · committed_merged=False · null=['dist.k.vwap', 'range_break.failed_trap_bars', 'range_break.retest_tolerance_atr']
LIVE-PRINT second-chance · evaluable=True · missing=[] · ftft=['not_formed'] · awaiting_day=False · awaiting_ruling=False · committed_engine_only=False · committed_merged=False · null=['dist.k.vwap', 'range_break.failed_trap_bars', 'range_break.retest_tolerance_atr']
LIVE-PRINT vwap-continuation · evaluable=True · missing=[] · ftft=['not_formed'] · awaiting_day=False · awaiting_ruling=False · committed_engine_only=False · committed_merged=False · null=['dist.k.vwap', 'range_break.failed_trap_bars', 'range_break.retest_tolerance_atr']
LADDER second-chance · merged=False · +A19+A20=True · +D6=True
LADDER vwap-continuation · merged=False · +A16=True · +D5=True
ASSUMED vwap-continuation · +R119=False
ASSUMED second-chance · +companion=True
HARNESS rubberband · engine_only=ERROR TaxonomyConfigError: cfg(rubberband.bars_cleared) has no row in tunables.yaml, no row in the vault's per-trade tunables units, and no defaults.yaml fallback · merged=False
```

`git status --short --branch` → `## setups/seven-0921` + `?? "docs/40 - DevDocs/reports/setups-live-note-fix-build-2026-09-24.md"`. The `??` line is this report, which CLOSE commits. The scratch file does not print, so it is ignored (the same reading as `64` D2).

## D2 CLASSES

Rules (a)–(f) applied in order, and only those rules.

| slug | ftft | awaiting | committed_merged | null | ladder | class | rule |
|---|---|---|---|---|---|---|---|
| backside | `['not_formed']` | ruling | False | all 3 | — | STALE — AWAITING_A_RULING not honoured | (b) |
| fashionably-late | `['not_formed']` | ruling | False | all 3 | — | STALE — AWAITING_A_RULING not honoured | (b) |
| hitchhiker | `['not_formed']` | day | False | all 3 | — | ALREADY PINNED | (a) |
| nine-ema-scalp | `['avoided', 'formed', 'not_formed']` | — | True | all 3 | — | NO CHANGE | (c) |
| rubberband | `['avoided', 'not_evaluable', 'not_formed']` | — | False | all 3 | — | NO CHANGE | (c): `avoided` is in ftft |
| second-chance | `['not_formed']` | — | False | contains both `range_break.*` | `+A19+A20=True` | STALE — awaiting its engine fill (A-19, A-20) — MISSING DIAL VALUE | (e2) |
| vwap-continuation | `['not_formed']` | — | False | contains `dist.k.vwap` | `+D5=True` | STALE — awaiting its engine fill (dist.k.vwap) | (e) |

Not evaluable (T2 asserts `not_evaluable` everywhere, unchanged): back-through-open, bella-fade, big-dog, bouncy-ball, first-vwap-pullback, gap-give-and-go.

Counts: STALE 4 · NO CHANGE 2 · PINNED 1 · DEFECT 0.

Informational rows (never class inputs):
- `ASSUMED vwap-continuation · +R119=False`: after the deploy's STEP-6 writes R119's three rows, the live-note test drops vwap-continuation's pin (its hole is no longer null) and asserts it forms. That run would be **RED**. This is the deploy's ORDER seam → ESCALATE.
- `ASSUMED second-chance · +companion=True`: if he rules A-19 / A-20 at the companion's values, second-chance forms on its committed day, and the pin-lift assertion would be green.
- `LADDER vwap-continuation · +A16=True` with `+D5=True`: at the constructed value, vwap-continuation waits on A-16 alone. No escalate is triggered, because that rule fires only on `+A16=False`.

GATES:
- DEFECT rows: 0 → pass.
- second-chance `+A19+A20=True`: the UNPROVEN read is now **PROVEN**. A-19 + A-20 alone are what it waits on. Pass.
- `HARNESS rubberband · merged=False`: not an ERROR, so the gate passes. His merged rows evaluate rubberband; the ERROR is only on the engine-only path. The grid does not form rubberband on the old FTFT/BGFI day (its HTF avoid applies, as the lego docstring says). The committed-day check's CUT_DAY_CHECKS path covers rubberband's cut day.
- T1: the live `evaluable=True` set is {backside, fashionably-late, hitchhiker, nine-ema-scalp, rubberband, second-chance, vwap-continuation}. That EQUALS the seven setups, so the gate holds.

## D3 THE EDITS

FIX rows built: F1 (T1 STALE) · F2 (T2 AWAITING_A_RULING, plus the committed-day check on his merged rows, i.e. the harness seam) · F3 (engine-fill pin with its (e) vwap-continuation and (e2) second-chance keys, and a gate-2 GREEN-as-pin). D2 printed both an (e) and an (e2) row, so both keys were built.

| edit | file | block |
|---|---|---|
| E1 | `tests/taxonomy/test_predicate.py` | T1 tail = `64` D3's T1 block |
| E2 | `tests/cobalt/setups_shapes.py` | `every_scan(…, *, tunables=None)` + one private `_grid` helper; the uncached path when `tunables` is given |
| E2 | `tests/cobalt/test_setups_lego.py` | `_forms_on_a_committed_day(key, shape, ld, tunables=None)` → `every_scan(…, tunables=tunables)`; `CUT_DAY_CHECKS` unchanged |
| E2 | `tests/cobalt/test_radar_evaluate.py` | imports; the AWAITING block replaced with the prompt's block |
| E3 | `tests/cobalt/test_setups_lego.py` | `AWAITING_AN_ENGINE_FILL` below `AWAITING_A_RULING`; `test_second_chance_without_its_engine_fill_forms_on_no_committed_scan` below the vwap pin |
| E3 | `tests/cobalt/test_radar_evaluate.py` | import gains `AWAITING_AN_ENGINE_FILL`; the `holes` pin block between `forms = …` and `assert forms`; one docstring clause |

**RED-FIRST RUN (after E1+E2, before E3):** `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs tests/cobalt/test_radar_evaluate.py tests/taxonomy/test_predicate.py` → exit 1 · **`1 failed, 108 passed, 15 warnings in 21.51s`**. The failure is at `tests/cobalt/test_radar_evaluate.py:742: AssertionError`, the new `assert forms`: `AssertionError: ('second-chance', ['not_formed'])`, which is the D2 (e2) slug. T1 passed. Printed: `AWAITING A RULING: backside`, `AWAITING A RULING: fashionably-late`, `AWAITING A DAY: hitchhiker`. That is the engine-fill red, as EXPECTED.

Proof: `git diff --stat` →
```
 tests/cobalt/setups_shapes.py       | 16 ++++++++++++----
 tests/cobalt/test_radar_evaluate.py | 29 ++++++++++++++++++++++++-----
 tests/cobalt/test_setups_lego.py    | 35 +++++++++++++++++++++++++++++++++--
 tests/taxonomy/test_predicate.py    | 15 ++++++++++-----
 4 files changed, 79 insertions(+), 16 deletions(-)
```
EXACTLY the four files. `git diff`, whole:
```diff
diff --git a/tests/cobalt/setups_shapes.py b/tests/cobalt/setups_shapes.py
index b858b567..c1ffd061 100644
--- a/tests/cobalt/setups_shapes.py
+++ b/tests/cobalt/setups_shapes.py
@@ -191,14 +191,22 @@ def evaluate(ld: sup.LoadedDef, ticker: str, at: datetime, *, tunables=None):
 _SCANS: dict[tuple[str, str], list] = {}
 
 
-def every_scan(ld: sup.LoadedDef, ticker: str) -> list:
+def _grid(ld: sup.LoadedDef, ticker: str, tunables=None) -> list:
+    return [(DAY_START + timedelta(minutes=m),
+             evaluate(ld, ticker, DAY_START + timedelta(minutes=m), tunables=tunables))
+            for m in range(0, 391, 2)]
+
+
+def every_scan(ld: sup.LoadedDef, ticker: str, *, tunables=None) -> list:
     """One evaluation per two-minute scan across the whole RTH fixture day
     (computed once per (def slug, md5, ticker) — two notes with the same YAML
-    body share an md5, the slug being frontmatter)."""
+    body share an md5, the slug being frontmatter). `tunables` given (a live
+    def's merged rows): evaluated with them, never cached."""
+    if tunables is not None:
+        return _grid(ld, ticker, tunables)
     key = (ld.slug, ld.md5, ticker)
     if key not in _SCANS:
-        _SCANS[key] = [(DAY_START + timedelta(minutes=m), evaluate(ld, ticker, DAY_START + timedelta(minutes=m)))
-                       for m in range(0, 391, 2)]
+        _SCANS[key] = _grid(ld, ticker)
     return _SCANS[key]
 
 
diff --git a/tests/cobalt/test_radar_evaluate.py b/tests/cobalt/test_radar_evaluate.py
index 21113a0e..914caabb 100644
--- a/tests/cobalt/test_radar_evaluate.py
+++ b/tests/cobalt/test_radar_evaluate.py
@@ -699,10 +699,14 @@ def test_live_defined_notes_evaluate_on_the_fixture_bars_and_only_the_evaluable_
     `formed` in its outcome set unless its own avoid is `avoided` on those
     scans or it is pinned in `AWAITING_A_DAY` (printed). A def the registry
     does NOT call evaluable is `not_evaluable` on every scan. The deploy runs
-    this with `COBALT_LIVE_VAULT_ROOT` set; a SKIP there is RED."""
+    this with `COBALT_LIVE_VAULT_ROOT` set; a SKIP there is RED, pinned in
+    AWAITING_A_DAY, AWAITING_A_RULING or AWAITING_AN_ENGINE_FILL while its hole
+    is null (printed), or proven on its committed day through gate 2's check
+    with his merged rows (FINAL §9 gate 3, "on its fixture day")."""
     from cobalt.radar.anatomy.registry import evaluability
     from cobalt.taxonomy.vault_loader import load_vault_trade_defs
-    from test_setups_lego import AWAITING_A_DAY
+    from test_setups_lego import AWAITING_A_DAY, AWAITING_A_RULING, AWAITING_AN_ENGINE_FILL, _forms_on_a_committed_day
+    import setups_shapes as shapes
 
     loaded = load_vault_trade_defs(vault_root=Path(os.environ[LIVE_VAULT_ENV]))
     defs = [sup.LoadedDef(slug=d.slug, md5=d.md5, definition=d.definition) for d in loaded.defs]
@@ -728,11 +732,26 @@ def test_live_defined_notes_evaluate_on_the_fixture_bars_and_only_the_evaluable_
             assert outcomes == {"not_evaluable"}, ld.slug
             continue
         assert "Setup(relation)" not in missing.get(ld.slug, set()), ld.slug
-        if ld.slug in AWAITING_A_DAY:
+        if ld.slug in AWAITING_A_DAY or ld.slug in AWAITING_A_RULING:
             with capsys.disabled():
-                print(f"AWAITING A DAY: {ld.slug}")
+                print(f"AWAITING A {'DAY' if ld.slug in AWAITING_A_DAY else 'RULING'}: {ld.slug}")
             continue
-        assert "formed" in outcomes or "avoided" in outcomes, (ld.slug, sorted(outcomes))
+        if "formed" in outcomes or "avoided" in outcomes:
+            continue
+        # FINAL §9 gate 3: formed "on its fixture day" — gate 2's committed-day
+        # check (test_setups_lego), run on HIS live def with HIS merged rows.
+        assert ld.slug in shapes.SHAPES, (ld.slug, sorted(outcomes))
+        forms = _forms_on_a_committed_day(ld.slug, shapes.SHAPES[ld.slug], ld, tunables)
+        holes = [key for key in AWAITING_AN_ENGINE_FILL.get(ld.slug, ())
+                 if tunables.get(key) is None or tunables[key].value is None]
+        if holes:
+            # Pinned like gate 2's `<slug>_without_its_engine_fill` tests: the
+            # hole's row is not in his vault yet; the day it is, this asserts forms.
+            with capsys.disabled():
+                print(f"AWAITING ITS ENGINE FILL: {ld.slug} ({', '.join(holes)} null)")
+            assert not forms, (ld.slug, holes)
+            continue
+        assert forms, (ld.slug, sorted(outcomes))
 
 
 def sup_member(bars, at):
diff --git a/tests/cobalt/test_setups_lego.py b/tests/cobalt/test_setups_lego.py
index 30668dec..16af9a33 100644
--- a/tests/cobalt/test_setups_lego.py
+++ b/tests/cobalt/test_setups_lego.py
@@ -55,6 +55,22 @@ AWAITING_A_DAY: frozenset[str] = frozenset({"hitchhiker"})
 #:   writes the assumed rows.
 AWAITING_A_RULING: frozenset[str] = frozenset({"backside", "fashionably-late"})
 
+#: Evaluable setups that form on NO committed scan while an ENGINE hole their
+#: atoms read is null in committed config (FINAL §8: an engine hole is filled
+#: only by a ruled or assumed row, never here), keyed by setup slug:
+#: - vwap-continuation: `dist.k.vwap` (`A-16`), R119's row, written by the
+#:   setups deploy; pinned by
+#:   `test_vwap_continuation_without_its_engine_fill_forms_on_no_committed_scan`.
+#: - second-chance: `range_break.failed_trap_bars` (`A-19`) and
+#:   `range_break.retest_tolerance_atr` (`A-20`) — `range_break_params` refuses
+#:   on either null, so `RangeBreak(level)` never reaches `accepted`; no value
+#:   is ruled yet (owner item, 2026-09-23); pinned by
+#:   `test_second_chance_without_its_engine_fill_forms_on_no_committed_scan`.
+AWAITING_AN_ENGINE_FILL: dict[str, tuple[str, ...]] = {
+    "vwap-continuation": ("dist.k.vwap",),
+    "second-chance": ("range_break.failed_trap_bars", "range_break.retest_tolerance_atr"),
+}
+
 
 @pytest.fixture(scope="module")
 def corpus(tmp_path_factory):
@@ -79,8 +95,9 @@ def _rubberband_forms_on_its_cut_day(ld) -> bool:
 CUT_DAY_CHECKS = {"rubberband": _rubberband_forms_on_its_cut_day}
 
 
-def _forms_on_a_committed_day(key, shape, ld) -> bool:
-    if any(ev.evaluation == "formed" for ticker in shape.tickers for _, ev in shapes.every_scan(ld, ticker)):
+def _forms_on_a_committed_day(key, shape, ld, tunables=None) -> bool:
+    if any(ev.evaluation == "formed" for ticker in shape.tickers
+           for _, ev in shapes.every_scan(ld, ticker, tunables=tunables)):
         return True
     check = CUT_DAY_CHECKS.get(key)
     return bool(check and check(ld))
@@ -110,6 +127,20 @@ def test_vwap_continuation_without_its_engine_fill_forms_on_no_committed_scan(tm
     assert not _forms_on_a_committed_day("vwap-continuation", shape, ld)
 
 
+def test_second_chance_without_its_engine_fill_forms_on_no_committed_scan(tmp_path):
+    """GREEN-as-pin (09-24 fix round): the break-retest-turn shape on the
+    COMMITTED engine rows only (no `engine=` fill, so A-19 / A-20 stay null)
+    forms on no scan. A hole filled in committed config, or a RangeBreak that
+    accepts without them, turns this red; with its D6 fills the same shape
+    forms (gate 2 above)."""
+    shape = shapes.SHAPES["second-chance"]
+    ld = shapes.load_note(tmp_path, "example-fix-break-retest-committed-rows", shape.mapping())
+    for key in AWAITING_AN_ENGINE_FILL["second-chance"]:
+        assert sup.engine_tunables()[key].value is None, key
+    assert evaluability(ld.definition).evaluable, evaluability(ld.definition).missing_atoms
+    assert not _forms_on_a_committed_day("second-chance", shape, ld)
+
+
 def test_every_unlocked_setup_shape_is_evaluable(corpus):
     """FINAL §9 point (4) / [F-16] (4): the corpus shape of every setup the
     build claims to unlock is `evaluable`, or the missing atom is named."""
diff --git a/tests/taxonomy/test_predicate.py b/tests/taxonomy/test_predicate.py
index cd5c728e..78a9bcf8 100644
--- a/tests/taxonomy/test_predicate.py
+++ b/tests/taxonomy/test_predicate.py
@@ -270,9 +270,14 @@ def test_all_live_defined_notes_parse_and_report_missing_atoms(capsys):
     with capsys.disabled():
         for slug, result in sorted(report.items()):
             print(f"{slug}: evaluable={result.evaluable} missing={list(result.missing_atoms)}")
-    rubberband = report.pop("rubberband")
-    assert rubberband.evaluable, rubberband.missing_atoms
-    # R2: Rubberband is the only def evaluable end-to-end in S2; every
-    # other def names exactly what it is missing, never a fake card.
+    # Setups ladder change (09-21 R44; setups FINAL §9 point (4)): the seven
+    # setups are evaluable end-to-end at defaults — the S2 "rubberband only"
+    # rule (R2) is superseded. Every other def still names exactly what it is
+    # missing, never a fake card. Same seven as test_setups_lego.SETUP_SLUGS.
+    setups = {"rubberband", "hitchhiker", "backside", "second-chance", "fashionably-late",
+              "nine-ema-scalp", "vwap-continuation"}
+    evaluable = {slug for slug, result in report.items() if result.evaluable}
+    assert evaluable == setups, (sorted(evaluable - setups), sorted(setups - evaluable))
     for slug, result in report.items():
-        assert not result.evaluable and result.missing_atoms, slug
+        if slug not in setups:
+            assert not result.evaluable and result.missing_atoms, slug
```

Commit: `c9a11e14 fix(live-note): live-note tests to the setups ladder world; engine-fill pin for vwap-continuation and second-chance; committed-day check on his merged rows (L75, 09-24)` → `<tip>` = `c9a11e14`.

## D4 LIVE-NOTE

On `<tip>` = `c9a11e14`.

Command: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs tests/cobalt/test_radar_evaluate.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → exit 0 · **`131 passed, 15 warnings in 26.93s`** → `<lp>` = 131, `<lf>` = 0. No `SKIPPED` line.

Printed AWAITING lines. These are exactly the D2 (a), (b), (e) and (e2) slugs:
```
AWAITING A RULING: backside
AWAITING A RULING: fashionably-late
AWAITING A DAY: hitchhiker
AWAITING ITS ENGINE FILL: second-chance (range_break.failed_trap_bars, range_break.retest_tolerance_atr null)
AWAITING ITS ENGINE FILL: vwap-continuation (dist.k.vwap null)
```

The pins are not a loophole. Command: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q tests/cobalt/test_setups_lego.py` → exit 0 · **`13 passed in 136.61s (0:02:16)`**, 0 failed. Three tests are in that pass:
- the new `test_second_chance_without_its_engine_fill_forms_on_no_committed_scan`
- the vwap pin
- `test_registry_evaluable_implies_forms_or_awaits_a_day`, which still forms second-chance's corpus shape with its D6 fills

## D5 SUITE

On `<tip>` = `c9a11e14`.

| step | command | exit | result |
|---|---|---|---|
| no .env | `ls /Users/cobalt/cobalt-wt/setups-c1/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/setups-c1/.env: No such file or directory` |
| GATE | `uv run pytest -q tests/cobalt tests/taxonomy` | 1 | **`3 failed, 2484 passed, 361 skipped, 1 xfailed, 15 warnings in 503.19s (0:08:23)`** |

Failures (verbatim):
```
FAILED tests/cobalt/scratch/test_live_note_print_0923.py::test_live_note_print - KeyError: 'COBALT_LIVE_VAULT_ROOT'
FAILED tests/cobalt/scratch/test_live_note_print_0923.py::test_live_note_info_committed_day_with_his_rows - KeyError: 'COBALT_LIVE_VAULT_ROOT'
FAILED tests/cobalt/scratch/test_second_chance_print_0924.py::test_second_chance_print - KeyError: 'COBALT_LIVE_VAULT_ROOT'
```
Each one fails at its first line, `load_vault_trade_defs(vault_root=Path(os.environ["COBALT_LIVE_VAULT_ROOT"]))` (`test_live_note_print_0923.py:28`, and the same line in the others). The suite runs without the live-vault prefix, so the variable is unset. All three files are gitignored scratch files (`.git/info/exclude:18:scratch/`), not part of `<tip>`. Two are `64`'s; one is this run's D2 print, written where the prompt placed it. **GATE: `0 failed` NOT met → FAILED: D5.**

INFORMATIONAL, not the gate. The same command with the scratch folder excluded, on the committed tree only: `uv run pytest -q tests/cobalt tests/taxonomy --ignore=tests/cobalt/scratch` → exit 0 · **`2483 passed, 361 skipped, 1 xfailed, 15 warnings in 504.42s (0:08:24)`**. 2487 tests ran in the gate run and 2483 here. The difference of 4 is the four scratch tests: the three failures plus `test_seam_dump_0923.py`'s one passing test.

## D5b WITH-DB

NOT RUN (D5 gate). `.env` was never copied, so nothing is on disk: `.env: never present` (D5 `ls` above).

## RESTARTS

NOT RUN (D5 stop). `<base>..<tip>` changes 4 test paths only (D3 `git diff --stat`).

## CONTINUE

next: D5, on the desk's ruling (ESCALATE 1). The code commit `c9a11e14` is on the branch and this report is wip-committed. A relaunch with `CONTINUE: D5` resumes at D5's `ls` + suite. It needs one of these first:
- the desk has removed the scratch files, or
- the desk rules the scratch exclusion.

After that come D5b, RESTARTS and CLOSE.

## ESCALATE

1. **D5 red = the scratch print files, not the branch. The desk decides the resume.** `tests/cobalt/scratch/` sits inside `tests/cobalt`, so the gate command collects every gitignored scratch print. Those prints read `os.environ["COBALT_LIVE_VAULT_ROOT"]` and error without it. D5b's `COBALT_ENV=dev uv run pytest -q tests/cobalt tests/taxonomy` would collect the same files and fail the same way. Two options:
   - (a) The desk removes `tests/cobalt/scratch/test_live_note_print_0923.py` and `test_second_chance_print_0924.py`. This seat has no `rm` string for them, and that cleanup is already owed. `02`'s hub reads them first, or reads their output quoted here and in `64`'s report. Then relaunch with `CONTINUE: D5`.
   - (b) The desk rules that D5 / D5b run with `--ignore=tests/cobalt/scratch`. This command is already inside the `uv run pytest *` / `COBALT_ENV=dev uv run pytest *` strings.

   The deploy's gate in `~/cobalt` never sees these files, because they exist only in this worktree. The informational committed-tree run above is green: 2483 / 0.
2. **THE ORDER SEAM, now with its boolean: `ASSUMED vwap-continuation · +R119=False`.** The deploy's live-note proof (its 2.3 (d)) runs BEFORE STEP-6, so both engine-fill pins hold there. After STEP-6 writes R119's rows, `dist.k.vwap` is no longer null, so vwap-continuation leaves its pin. The next live-note run then asserts it forms, and at R119's values it does NOT, so that run goes **RED**. The desk must know before the deploy. For contrast, `+A16=True` at the constructed value shows the pin is correct and the gap lies between R119's value and the constructed one. Deploy delta row 19's post-STEP-6 run would catch it.
3. **second-chance stays pinned until HE rules A-19 / A-20.** `ASSUMED second-chance · +companion=True`: at the companion's values it forms on its committed day, so the pin lift would be green. The owner item is carried from the drafter (FOR DEJAN 1).
4. **The UNPROVEN read is now PROVEN:** `LADDER second-chance · merged=False · +A19+A20=True · +D6=True`. A-19 + A-20 alone are what second-chance waits on.
5. **HARNESS note (informational):** `HARNESS rubberband · engine_only=ERROR TaxonomyConfigError … · merged=False`. With his merged rows, rubberband evaluates (no ERROR) but does not form on the old FTFT/BGFI grid; the HTF avoid applies there. T2 never reaches the committed-day check for rubberband, because `avoided` is in its FTFT outcomes. If it ever did, `CUT_DAY_CHECKS` covers its cut day.
6. **R81 (GATE EARLY)** is recorded once: the desk's direction, applied by the drafter to this file. This run got as far as the offline leg; the with-DB leg is owed.
7. **Scratch files on disk** (gitignored), left for `02`'s hub, with cleanup owed by the desk (see 1):
   - `tests/cobalt/scratch/test_live_note_print_0923.py`
   - `tests/cobalt/scratch/test_second_chance_print_0924.py` (holds the ASSUMED values; L32 keeps them out of every committed file)
   - `tests/cobalt/scratch/test_seam_dump_0923.py`
8. L74 is recorded once above. The expectations moved on file evidence only: D2 gave 4 rows STALE and 0 DEFECT, and the red first was the engine-fill red at E2. The check is `02` (L67, three houses), and its packet must carry this report's executed output of all three suites (R81 (4)). The with-DB suite is still owed here. The deploy's L68 gate re-proves them on the tree that ships.

FAILED: D5 — offline suite red — 3 failed, 2484 passed: all three are the gitignored scratch prints in tests/cobalt/scratch/ (KeyError: 'COBALT_LIVE_VAULT_ROOT'); committed tree with --ignore=tests/cobalt/scratch: 2483 passed / 0 failed (informational) · fix c9a11e14 built, live-note 131/0 · D5b not run · desk: remove scratch or rule the ignore, relaunch CONTINUE: D5
