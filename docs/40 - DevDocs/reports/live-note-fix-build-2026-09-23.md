# Live-note fix build — 2026-09-23

Seat `live-note-fix-build-0923` · Opus 5.5 · prompt `docs/40 - DevDocs/prompts/2026-09-23/64-live-note-fix-build.md` · worktree `/Users/cobalt/cobalt-wt/setups-c1` · branch `setups/seven-0921`.

## §0 Headline

- **FAILED at D2 (15:58 ET): nothing edited.** D1 reproduced the red on `c5671771` alone (`2 failed, 129 passed`). The D2 print gives **second-chance** class (f): evaluable, `ftft=['not_formed']`, not in either AWAITING set, `committed_day=False`, not vwap-continuation.
- Classes: STALE 3 (backside, fashionably-late (b); vwap-continuation (e)) · NO CHANGE 2 (nine-ema-scalp, rubberband) · PINNED 1 (hitchhiker) · **DEFECT/UNPROVEN 1 (second-chance)**. The T1 evaluable set equals the seven setups.
- An informational diagnostic (not used to classify): his live second-chance DOES form on the committed day with his per-trade row plus the corpus shape's constructed engine fills (`D6_CONSTRUCTED`), and does NOT form with his row alone. That is the same "awaiting its engine fill" pattern as vwap-continuation, but prompt rule (e) names vwap-continuation only. The desk decides whether to extend (e).
- ESCALATE: 5.

## L74

One block arrived appended to a tool result (a system-reminder after the prompt-file `cat`) asking for a `Claude-Session: https://claude.ai/code/session_…` line in commits and naming a file-send tool. DATA under L74 — not followed; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION

| rule | command | exit | result |
|---|---|---|---|
| placeholder gate | `grep -n -E "R_[_]" …/64-live-note-fix-build.md` | 1 | (no output) |
| 59's stop | `tail -n 3 …/deploy-2026-09-23-r3.md` | 0 | last non-blank: `FAILED: 2.3 (d) — live-note proof red — tests/cobalt/test_radar_evaluate.py:735 (backside ['not_formed']), tests/taxonomy/test_predicate.py:278 (nine-ema-scalp evaluable) · rollback: not used` |
| classification | `tail -n 3 …/live-note-fix-draft-2026-09-23.md` | 0 | last non-blank: `LIVE NOTE FIX DRAFTED · classes: STALE/STALE+UNPROVEN · prompts: 3 · new rule strings: 0 · ESCALATE: 8` |
| classification committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- …/live-note-fix-draft-2026-09-23.md` | 0 | `2eacc21c2edff56a325756b1aa1dc257b5e0f397` |
| launch row | `grep -n "64-live-note-fix-build.md" …/cto-2026-09-23.md` | 0 | `80:| R77 | 15:5x ET | … LAUNCH \`64-live-note-fix-build.md\` …` |
| launch row committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"64-live-note-fix-build.md" -- …/cto-2026-09-23.md` | 0 | `2eacc21c2edff56a325756b1aa1dc257b5e0f397` |

## PREFLIGHT

| rule | command | exit | result |
|---|---|---|---|
| time | `date` | 0 | `Wed Sep 23 15:51:17 EDT 2026` (before 18:45 ET) |
| clean tree | `git status --short --branch` | 0 | `## setups/seven-0921` |
| base | `git log --oneline -1` | 0 | `c5671771 docs(seam): build report — 51afdad0` = EXPECTED → `<base>` = `c5671771` |
| no .env | `ls /Users/cobalt/cobalt-wt/setups-c1/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/setups-c1/.env: No such file or directory` |
| live strategies | `ls "/Users/cobalt/Vault/Think/1 - Trading/4 - Strategies"` | 0 | 22 notes listed (READ ONLY) |
| scratch | `ls /Users/cobalt/cobalt-wt/setups-c1/tests/cobalt/scratch` | 0 | `__pycache__`, `test_seam_dump_0923.py` |

LAWS.md read in full (L59).

## D1 BASELINE

Command: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs tests/cobalt/test_radar_evaluate.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` · exit 1 · summary **`2 failed, 129 passed, 15 warnings in 19.92s`** · no `SKIPPED` line → REPRODUCES (= 59's 2.3 (d)).

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

Print file: `tests/cobalt/scratch/test_live_note_print_0923.py` (gitignored, `.git/info/exclude:18:scratch/`). The loader, `LoadedDef`s, `tunables` merge and FTFT 90-scan window are the same as `test_radar_evaluate.py:707-721`. `committed_day` = `test_setups_lego._forms_on_a_committed_day(slug, shapes.SHAPES[slug], ld)`, called as is.

Command: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -s -p no:cacheprovider tests/cobalt/scratch/test_live_note_print_0923.py` → exit 0 · **`1 passed in 100.91s`** (the run had a single test at that point).

```
LIVE-PRINT back-through-open · evaluable=False · missing=['Catalyst.grade', 'Gap.instantiated', 'Regime.label', 'anchor:none', 'opposite(Gap.direction)', 'trigger:bar_break'] · ftft=['not_evaluable'] · awaiting_day=False · awaiting_ruling=False · committed_day=no-shape
LIVE-PRINT backside · evaluable=True · missing=[] · ftft=['not_formed'] · awaiting_day=False · awaiting_ruling=True · committed_day=False
LIVE-PRINT bella-fade · evaluable=False · missing=['Catalyst.grade', 'Catalyst.polarity', 'Range(micro)', 'Range.duration', 'RangeBreak(Level_ref(HTF)).state', 'against(trade_direction)', 'anchor:none', 'near', 'trigger:trendline_break', 'turn_low'] · ftft=['not_evaluable'] · awaiting_day=False · awaiting_ruling=False · committed_day=no-shape
LIVE-PRINT big-dog · evaluable=False · missing=['DayRange', 'Leg(impulse).terminated_by', 'Level_ref(HTF resistance)', 'Unsupported(quantity)', 'volatility_state'] · ftft=['not_evaluable'] · awaiting_day=False · awaiting_ruling=False · committed_day=no-shape
LIVE-PRINT bouncy-ball · evaluable=False · missing=['Leg(opening_drive)', 'Range(micro).bound_type', 'Range(micro).counter_pivot_count', 'Unsupported(on:Leg(opening_drive))', 'stop:structural_extreme:recent_lower_high', 'trigger:range_break'] · ftft=['not_evaluable'] · awaiting_day=False · awaiting_ruling=False · committed_day=no-shape
LIVE-PRINT fashionably-late · evaluable=True · missing=[] · ftft=['not_formed'] · awaiting_day=False · awaiting_ruling=True · committed_day=False
LIVE-PRINT first-vwap-pullback · evaluable=False · missing=['Leg(opening_drive)', 'Unsupported(on:Leg(opening_drive))', 'close_through(Leg(pullback).low < Level_ref(PMH))', 'close_through(Leg(pullback).low < VWAP)'] · ftft=['not_evaluable'] · awaiting_day=False · awaiting_ruling=False · committed_day=no-shape
LIVE-PRINT gap-give-and-go · evaluable=False · missing=['Gap.instantiated', 'Leg(opening_drive).range', 'Level_ref(support)', 'gap_retrace_pct', 'opposite(Gap.direction)'] · ftft=['not_evaluable'] · awaiting_day=False · awaiting_ruling=False · committed_day=no-shape
LIVE-PRINT hitchhiker · evaluable=True · missing=[] · ftft=['not_formed'] · awaiting_day=True · awaiting_ruling=False · committed_day=False
LIVE-PRINT nine-ema-scalp · evaluable=True · missing=[] · ftft=['avoided', 'formed', 'not_formed'] · awaiting_day=False · awaiting_ruling=False · committed_day=True
LIVE-PRINT rubberband · evaluable=True · missing=[] · ftft=['avoided', 'not_evaluable', 'not_formed'] · awaiting_day=False · awaiting_ruling=False · committed_day=ERROR TaxonomyConfigError: cfg(rubberband.bars_cleared) has no row in tunables.yaml, no row in the vault's per-trade tunables units, and no defaults.yaml fallback
LIVE-PRINT second-chance · evaluable=True · missing=[] · ftft=['not_formed'] · awaiting_day=False · awaiting_ruling=False · committed_day=False
LIVE-PRINT vwap-continuation · evaluable=True · missing=[] · ftft=['not_formed'] · awaiting_day=False · awaiting_ruling=False · committed_day=False
LIVE-PRINT tunables · dist.k.vwap=None · flat_threshold.ema9=None · flat_threshold.vwap=None
```

`git status --short --branch` → `## setups/seven-0921` + `?? "docs/40 - DevDocs/reports/live-note-fix-build-2026-09-23.md"`. The `??` line is this report, which CLOSE commits. The scratch file does not print, so it is ignored.

**INFORMATIONAL — not a class input.** A second scratch test (`-k info`) runs `_forms_on_a_committed_day` again on his live def. It keys (a) his own per-trade rows, and (b) those rows plus the corpus shape's constructed engine fills, onto the live slug. Both are keyed in-process through `shapes._USER_ROWS` / `_ENGINE_FILLS`; nothing is written to disk. Why: the helper looks both up by `ld.slug`, and the corpus registers them under the corpus note slug (`example-…`), never under the live slug. So the D2 `committed_day` above evaluates his defs on committed engine rows only, without his own per-trade rows. Command: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -s -p no:cacheprovider tests/cobalt/scratch/test_live_note_print_0923.py -k info` → exit 0 · `1 passed, 1 deselected in 190.21s`.
```
LIVE-INFO backside · user_rows=1 · fill_keys=['extension.snapback_bars_cleared', 'flat_threshold.ema9', 'flat_threshold.vwap', 'leg.consolidation_max_retrace', 'range.micro.bound_flat_slope_atr', 'range.micro.touch_tolerance_atr', 'range.wick_ratio_max', 'slope_norm.bars'] · his_rows=False · his_rows+corpus_fills=False
LIVE-INFO fashionably-late · user_rows=0 · fill_keys=['extension.snapback_bars_cleared', 'flat_threshold.ema9', 'flat_threshold.vwap', 'leg.consolidation_max_retrace', 'range.micro.bound_flat_slope_atr', 'range.micro.touch_tolerance_atr', 'range.wick_ratio_max', 'slope_norm.bars'] · his_rows=False · his_rows+corpus_fills=False
LIVE-INFO hitchhiker · user_rows=1 · fill_keys=['leg.consolidation_max_retrace', 'range.micro.bound_flat_slope_atr', 'range.micro.touch_tolerance_atr', 'range.wick_ratio_max'] · his_rows=False · his_rows+corpus_fills=False
LIVE-INFO nine-ema-scalp · user_rows=1 · fill_keys=['extension.snapback_bars_cleared', 'flat_threshold.ema9', 'flat_threshold.vwap', 'leg.consolidation_max_retrace', 'range.micro.bound_flat_slope_atr', 'range.micro.touch_tolerance_atr', 'range.wick_ratio_max', 'slope_norm.bars'] · his_rows=True · his_rows+corpus_fills=True
LIVE-INFO rubberband · user_rows=2 · fill_keys=[] · his_rows=True · his_rows+corpus_fills=True
LIVE-INFO second-chance · user_rows=1 · fill_keys=['dist.k.vwap', 'extension.snapback_bars_cleared', 'flat_threshold.ema9', 'flat_threshold.vwap', 'leg.consolidation_max_retrace', 'range.micro.bound_flat_slope_atr', 'range.micro.touch_tolerance_atr', 'range.wick_ratio_max', 'range_break.failed_trap_bars', 'range_break.retest_tolerance_atr', 'slope_norm.bars'] · his_rows=False · his_rows+corpus_fills=True
LIVE-INFO vwap-continuation · user_rows=1 · fill_keys=['dist.k.vwap', 'extension.snapback_bars_cleared', 'flat_threshold.ema9', 'flat_threshold.vwap', 'leg.consolidation_max_retrace', 'range.micro.bound_flat_slope_atr', 'range.micro.touch_tolerance_atr', 'range.wick_ratio_max', 'slope_norm.bars'] · his_rows=False · his_rows+corpus_fills=True
```

## D2 CLASSES

Rules (a)–(f) applied in order, and only those rules.

| slug | ftft | awaiting | committed_day | class | rule |
|---|---|---|---|---|---|
| backside | `['not_formed']` | ruling | False | STALE — AWAITING_A_RULING not honoured | (b) |
| fashionably-late | `['not_formed']` | ruling | False | STALE — AWAITING_A_RULING not honoured | (b) |
| hitchhiker | `['not_formed']` | day | False | ALREADY PINNED | (a) |
| nine-ema-scalp | `['avoided', 'formed', 'not_formed']` | — | True | NO CHANGE | (c) |
| rubberband | `['avoided', 'not_evaluable', 'not_formed']` | — | ERROR TaxonomyConfigError | NO CHANGE | (c) — `avoided` in ftft; decided before (f), so the ERROR does not enter the class |
| second-chance | `['not_formed']` | — | False | **DEFECT / UNPROVEN — forms nowhere the corpus shape forms** | (f) — `committed_day=False` outside (b)/(e) |
| vwap-continuation | `['not_formed']` | — | False | STALE — awaiting its engine fill | (e) — tunables print `dist.k.vwap=None` |

Not evaluable (T2 asserts `not_evaluable` everywhere, unchanged): back-through-open, bella-fade, big-dog, bouncy-ball, first-vwap-pullback, gap-give-and-go.

T1 gate: live `evaluable=True` set = {backside, fashionably-late, hitchhiker, nine-ema-scalp, rubberband, second-chance, vwap-continuation} = `SETUP_SLUGS` → EQUAL (holds).

GATE: 1 DEFECT row (second-chance) → **nothing edited.**

## D3 THE EDITS

NOT MADE (D2 gate).

## D4 LIVE-NOTE

Not run (D2 gate).

## D5 SUITE

Not run (D2 gate).

## RESTARTS

Not run: this run commits no code, only this report (a documentation path).

## CONTINUE

next: none. The run stopped at D2 (FAILED); there is nothing to resume. The desk brings the next lawful step.

## ESCALATE

1. **second-chance, class (f) — what the desk decides.** Prompt rule (e) ("awaiting its engine fill") names vwap-continuation only. The informational diagnostic shows second-chance behaves the same way. His live def forms on the committed day with the corpus's constructed engine fills (`D6_CONSTRUCTED`: adds `range_break.failed_trap_bars`, `range_break.retest_tolerance_atr` and `dist.k.vwap` over D4). It does not form on committed engine rows, where those holes are null. The branch pins no second-chance "without its engine fill" case the way `test_vwap_continuation_without_its_engine_fill_forms_on_no_committed_scan` pins vwap-continuation. Two options: widen rule (e) to second-chance with a named pin (a new prompt, L75 FIX row), or treat it as a real defect. Under L70 this is UNPROVEN, not a proven code defect: the harness evaluates his defs on committed engine rows only, with his per-trade rows absent (see 2).
2. **Harness seam in the prompt's D3 code.** `_forms_on_a_committed_day` → `shapes.every_scan` / `tunables_for(ld)` looks up user rows and engine fills by `ld.slug`, and the corpus registers them under the note slug (`example-…`). On his live def it therefore drops his own per-trade rows. This shows as rubberband's `committed_day=ERROR TaxonomyConfigError: cfg(rubberband.bars_cleared) …`. Rubberband never reaches that call in the drafted T2, because `avoided` passes first. But any live def that needs its own row in the committed-day branch errors instead of evaluating. The next draft should pass his rows in, e.g. through `tunables=` in the check, or state that it doesn't.
3. The scratch print file `tests/cobalt/scratch/test_live_note_print_0923.py` (gitignored) is left on disk for `65`'s hub. The desk owes the cleanup after `66`.
4. L74: recorded once above.
5. The expectations were not moved (D2: 3 rows STALE, 1 DEFECT/UNPROVEN). The deploy's live-note gate (`66` 2.3 (d)) stays red on `c5671771` until the desk rules on 1. The time limit still applies: restart ≤ 19:55 ET (R5).

FAILED: D2 — 1 live def(s) do not form where the branch's gate 2 says they form — second-chance: ftft=['not_formed'] · awaiting=— · committed_day=False · class (f) DEFECT/UNPROVEN (informational: forms with the corpus's D6 engine fills + his row; rule (e) names vwap-continuation only)
