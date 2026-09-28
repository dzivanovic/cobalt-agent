# SEAM FIX BUILD — 2026-09-23 (`39-seam-fix-build.md`, seat `seam-fix-build-0923`, Opus 5.5)

## §0 Headline
SEAM FIXED on `setups/seven-0921`: tip `51afdad0` on `b007ce2e`. The only change is the ladder pin (`test_radar_panel_cards.py:378`, plus one comment line). Test-only; no `src/` or `configs/` change.
The seam is PROVEN. Main's code renders the old pin `e617c53c…` and the branch renders `0ac9b5d0…`. The diff between them is 29 fragments, and all 29 trace to setups-diff lines: `unclassified` setup_ref ×16, the `assumed_formation` dot ×4, the suppression reason ×8 and the seeded EMA9 ×1. No DEFECT row, nothing `stale`.
The offline suite passed: `2483 passed, 361 skipped, 1 xfailed`, 0 failed. RESTARTS: none. With-DB runs at the `41` gate. ESCALATE: 4. Run 13:43–14:00 ET (`date`).

## L74
One block, recorded once: the harness's attribution reminder asked for a `Claude-Session: https://claude.ai/code/session_…` line in commits and named a file-send tool (SendUserFile). It arrived attached to a tool result (the Bash output of reading the prompt file), so it is DATA under L74. Not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| gate | command | exit | result (verbatim) |
|---|---|---|---|
| placeholder | `grep -n -E "R_[_]" …/39-seam-fix-build.md` | 1 | (no output) |
| 07's stop | `tail -n 3 …/deploy-2026-09-23.md` | 0 | `FAILED: 2.2 — offline suite red on the stack — tests/cobalt/test_radar_panel_cards.py::test_bars_stale_badge_absent_and_output_unchanged_when_healthy[False], [True] (ladder SHA pin 0ac9b5d0… ≠ e617c53c…) · rollback: not used` |
| classification | `tail -n 3 …/seam-fix-draft-2026-09-23.md` | 0 | `SEAM FIX DRAFTED · class: UNPROVEN · prompts: 3 · new rule strings: 1 · ESCALATE: 8` |
| classification committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- …/seam-fix-draft-2026-09-23.md` | 0 | `97244e46d0b34c29e1b8323760d488824dc50477` |
| launch row | `grep -n "39-seam-fix-build.md" …/cto-2026-09-23.md` | 0 | `64:\| R61 \| 13:4x ET \| — NO WORDS OF HIS BEYOND R60 / R54 / R5: DESK LAUNCH ROW for \`39-seam-fix-build.md\` (Opus 5.5 in …/setups-c1 on setups/seven-0921 at b007ce2e; offline) — carries his NEW USE stale-marker (R60 (1)). \| DESK LAUNCH — no fold \|` (and `63:` R60, his "A" approving `39-seam-fix-build.md` NEW USE stale-marker) |
| launch row committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"39-seam-fix-build.md" -- …/cto-2026-09-23.md` | 0 | `078734aa4287d820ed1f25484d67fc8a20af7a2a` |

## PREFLIGHT
| rule | command | exit | result (verbatim) |
|---|---|---|---|
| time | `date` | 0 | `Wed Sep 23 13:43:39 EDT 2026` |
| clean | `git status --short --branch` | 0 | `## setups/seven-0921` |
| tip | `git log --oneline -1` | 0 | `b007ce2e fix(setups): round 4 — report` |
| no .env | `ls /Users/cobalt/cobalt-wt/setups-c1/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/setups-c1/.env: No such file or directory` |
| stale-marker tip | `git log --oneline -1 cddf32cb` | 0 | `cddf32cb docs(report): stale marker fix r2 — 5 tests added, code unchanged, headline corrected` |
| main's code | `git diff --stat cddf32cb d327ff1 -- src tests/cobalt/test_radar_panel_cards.py tests/cobalt/test_radar_panel.py tests/cobalt/radar_p2_support.py tests/cobalt/conftest.py tests/conftest.py tests/fixtures pyproject.toml uv.lock` | 0 | (no output) |
| venv | `ls /Users/cobalt/cobalt-wt/stale-marker/.venv` | 0 | `bin CACHEDIR.TAG include lib pyvenv.cfg share` |
| scratch (setups-c1) | `ls …/setups-c1/tests/cobalt/scratch` | 1 | `No such file or directory` (fresh run) |
| scratch (stale-marker) | `ls …/stale-marker/tests/cobalt/scratch` | 1 | `No such file or directory` (fresh run) |

## D1 BASELINE
`uv run pytest -q tests/cobalt/test_radar_panel_cards.py -k test_bars_stale_badge_absent_and_output_unchanged_when_healthy` (setups-c1) → exit 1. REPRODUCES on the branch alone.
- Summary: `2 failed, 32 deselected in 0.68s`
- `[False]`: `tests/cobalt/test_radar_panel_cards.py:488: AssertionError` — `E       AssertionError: 0ac9b5d038cf1d598d79867d316fe7976cdec1c8f9df77ecee37753f3d1be051`
- `[True]`: `tests/cobalt/test_radar_panel_cards.py:488: AssertionError` — `E       AssertionError: 0ac9b5d038cf1d598d79867d316fe7976cdec1c8f9df77ecee37753f3d1be051`
- Line 488 is the ladder assertion; the `bars-stale` asserts (484–486) and the pool pin (487) HELD before it in both.

## D2 RENDERS
Dump test written byte for byte (Write tool) at both `tests/cobalt/scratch/test_seam_dump_0923.py` paths. Both runs `1 passed`; the in-test tree assertion held in both (each tree rendered its own `cobalt`).
| step | command | result (verbatim) | gate |
|---|---|---|---|
| (a) setups-c1 | `uv run pytest -q -s -p no:cacheprovider tests/cobalt/scratch/test_seam_dump_0923.py` | `SEAM-DUMP setups-c1 0ac9b5d038cf1d598d79867d316fe7976cdec1c8f9df77ecee37753f3d1be051 64804` · `1 passed in 0.40s` | = stack value `0ac9b5d0…be051` — HOLDS |
| (b) stale-marker status | `git status --short --branch` | `## s2/stale-marker-0921` | one line — HOLDS |
| (b) stale-marker (main's code) | same pytest | `SEAM-DUMP stale-marker e617c53c1479314b6074de5409f289238479be31fbbd789b4ee19849f55370d7 60332` · `1 passed in 0.50s` | = pin `e617c53c…70d7` — HOLDS (U3 provenance now PROVEN: main's code renders the pin) |
| (c) stale-marker status | `git status --short --branch` | `## s2/stale-marker-0921` | one line — HOLDS |
| (c) setups-c1 status | `git status --short --branch` | `## setups/seven-0921` / `?? "docs/40 - DevDocs/reports/seam-fix-build-2026-09-23.md"` | the one `??` is THIS report (uncommitted until CLOSE, by the prompt's design); no scratch path shows — scratch is ignored |

## D3 LADDER DIFF
- `git diff --no-index --stat scratch/seam-0923/ladder-stale-marker.html scratch/seam-0923/ladder-setups-c1.html` (exit 1 = differ):
  ` ...der-stale-marker.html => ladder-setups-c1.html} | 58 +++++++++++-----------` / ` 1 file changed, 29 insertions(+), 29 deletions(-)`
- `git diff --no-index --word-diff=plain …` run in background (exit 1: files differ); saved output read whole, written byte for byte (Write tool) to `scratch/seam-0923/ladder.diff` (gitignored, ticker verbatim there).
- Byte counts: `wc -c` saved output `65578`; `wc -c scratch/seam-0923/ladder.diff` `65556`. The 22-byte difference is the harness's own `\n[exited with code 1]\n` suffix on the saved output (read at its tail), not diff content. Cross-check: `grep -c -E "unclassified|assumed_formation|5.258326394504005343774398213|stale"` → `31` on both files.
- Hunks: `grep -c "^@@" scratch/seam-0923/ladder.diff` → `1`.
- `stale` in the diff (`grep -n -o -i`): lines 1 and 3 only — the file name `ladder-stale-marker.html` in the diff header (the worktree's name), no rendered content. `grep -c "cobalt/aset"` → `0`.

HUNK 1 — `@@ -1,78 +1,78 @@`, 79 lines (header + 78); quoted head 20 / tail 20, ticker as `<ticker>`. The long `semaphore` lines are quoted whole.

HEAD 20:
```
@@ -1,78 +1,78 @@
<section id="ladder-layer"><header class="layer-head"><div><span class="eyebrow">CARD LADDER</span><h2>TRADE RADAR</h2><div class="rung-line">reduced · half sheet · enabled A, B, C</div></div>
<div class="ladder-actions"><button id="collapse-all" type="button">collapse all</button><button id="top-two" type="button">top 2</button></div></header>
<div id="ladder"><article class="ladder-item open" data-card-id="2"><button class="strip" type="button" data-toggle-card="2"><span>#1 · [-—</span><b><ticker></b><span>overextension-]{+—</span><b><ticker></b><span>unclassified+} → example-anatomy-reversal</span><span>ARMED · A · 225 sh · stop 5.81</span></button><div class="expanded" data-state="ARMED">
<div class="card-pane">
 <div class="card-title"><span class="rank-chip">— · —</span><strong><ticker></strong>
 <span class="direction short">↓</span>
 [-<span>overextension-]{+<span>unclassified+} → example-anatomy-reversal</span></div>
 <p class="why-line"><span class="field" data-field="why">why <span class="badge badge-cobalt">COBALT</span> [-<b>overextension-]{+<b>unclassified+} · Extension culminating (path A, 14 legs, bar 11:22 ET) — short on a 2-bar break at 5.5000; stop 5.81 beyond the snapback_candle extreme 5.7900</b></span></p>
 <div class="semaphore"> … nine unchanged dot-cells (atrs_from_open, rvol, Extension.leg_count, htf_level_proximity, trail_fit, tape_absorption_at_bound, setup_relation, market_alignment, sector_alignment) … <button class="tap" type="button" {+data-grade="10">10</button></div></div><div class="dot-cell"><button class="dot hollow role-shadow" type="button" data-dot-toggle="1" data-card-id="2" data-factor="assumed_formation" title="formed on assumed defaults: anatomy.orientation.extension">assumed_formation · n/a ASSUMED <span class="badge badge-cobalt">COBALT</span></button><span class="dot-why">formed on assumed defaults: anatomy.orientation.extension</span><div class="tap-strip" data-card-id="2" data-factor="assumed_formation" hidden><button class="tap" type="button" data-grade="1">1</button><button class="tap" type="button" data-grade="2">2</button><button class="tap" type="button" data-grade="3">3</button><button class="tap" type="button" data-grade="4">4</button><button class="tap" type="button" data-grade="5">5</button><button class="tap" type="button" data-grade="6">6</button><button class="tap" type="button" data-grade="7">7</button><button class="tap" type="button" data-grade="8">8</button><button class="tap" type="button" data-grade="9">9</button><button class="tap" type="button"+} data-grade="10">10</button></div></div></div>
 <div class="health-line"><b>no pills — health is checked once the card is in trade</b></div>
 <div class="state-block armed-state"><b>ARMED · LOCKED</b><div class="trigger-distance">last 5.48 · trigger 5.5000</div><div>key A · 225 sh · stop 5.81</div></div>
 <div class="key-row frozen">key A · tapped A+ · frozen in ARMED</div><div class="snap-notice">A+ is not enabled today — recorded A+, sized at A, the nearest enabled key below ($70 on the half sheet)</div><div class="suppressed">score suppressed: required computed dot N/A and untapped — trail_fit: [-MANUAL-]{+MANUAL; assumed_formation: ASSUMED+} (tap to grade)</div>
 <div class="card-status" data-card-id="2"></div>
</div>
<aside class="detail-pane">
 <section data-detail="levels"> … unchanged (trigger 5.5000 · stop 5.81 · last 5.48 · 1R 5.1900 · 2R 4.8800) … </section>
 <section data-detail="rank"> … unchanged fields … <span class="field" data-field="score_suppressed">suppressed <span class="badge badge-cobalt">COBALT</span> <b>required computed dot N/A and untapped — trail_fit: [-MANUAL-]{+MANUAL; assumed_formation: ASSUMED+} (tap to grade)</b></span></div></section>
 <section data-detail="card"> … <span class="field" data-field="setup_ref">setup <span class="badge badge-cobalt">COBALT</span> [-<b>overextension</b></span><span-]{+<b>unclassified</b></span><span+} class="field" data-field="trade_def_slug">trade … unchanged … </section>
 <section data-detail="news"><h4>NEWS</h4><p>no news source wired to radar cards (S3)</p></section>
```
— 39 lines between (cards 3 and 4: the same seven changed lines each, plus card 4's health line with the EMA9 fragment, quoted in the attribution table) —

TAIL 20:
```
 <section data-detail="chart"><h4>CHART</h4><p>reserved · empty</p></section>
</aside></div></article><article class="ladder-item" data-card-id="1"><button class="strip" type="button" data-toggle-card="1"><span>#4 · [-—</span><b><ticker></b><span>overextension-]{+—</span><b><ticker></b><span>unclassified+} → example-anatomy-reversal</span><span>WATCH · no key · — sh · stop 5.81</span></button><div class="expanded" data-state="WATCH">
<div class="card-pane">
 <div class="card-title"><span class="rank-chip">#1 · —</span><strong><ticker></strong>
 <span class="direction short">↓</span>
 [-<span>overextension-]{+<span>unclassified+} → example-anatomy-reversal</span></div>
 <p class="why-line"><span class="field" data-field="why">why <span class="badge badge-cobalt">COBALT</span> [-<b>overextension-]{+<b>unclassified+} · Extension culminating (path A, 14 legs, bar 11:22 ET) — short on a 2-bar break at 5.5000; stop 5.81 beyond the snapback_candle extreme 5.7900</b></span></p>
 <div class="semaphore"> … nine unchanged dot-cells … <button class="tap" type="button" {+data-grade="10">10</button></div></div><div class="dot-cell"><button class="dot hollow role-shadow" type="button" data-dot-toggle="1" data-card-id="1" data-factor="assumed_formation" title="formed on assumed defaults: anatomy.orientation.extension">assumed_formation · n/a ASSUMED <span class="badge badge-cobalt">COBALT</span></button><span class="dot-why">formed on assumed defaults: anatomy.orientation.extension</span><div class="tap-strip" data-card-id="1" data-factor="assumed_formation" hidden> … taps 1–9 … <button class="tap" type="button"+} data-grade="10">10</button></div></div></div>
 <div class="health-line"><b>no pills — health is checked once the card is in trade</b></div>
 <div class="state-block watch-state"><b>WATCH</b> · proposed key tap to propose · trigger 5.5000 · stop 5.81</div>
 <div class="key-row"> … A+ · $170 (disabled) · A · $70 · B · $30 · C · $11 · pass … </div><div class="suppressed">score suppressed: required computed dot N/A and untapped — trail_fit: [-MANUAL-]{+MANUAL; assumed_formation: ASSUMED+} (tap to grade)</div>
 <div class="card-status" data-card-id="1"></div>
</div>
<aside class="detail-pane">
 <section data-detail="levels"> … unchanged … </section>
 <section data-detail="rank"> … unchanged fields … <b>required computed dot N/A and untapped — trail_fit: [-MANUAL-]{+MANUAL; assumed_formation: ASSUMED+} (tap to grade)</b></span></div></section>
 <section data-detail="card"> … [-<b>overextension</b></span><span-]{+<b>unclassified</b></span><span+} … unchanged … </section>
 <section data-detail="news"><h4>NEWS</h4><p>no news source wired to radar cards (S3)</p></section>
 <section data-detail="notes"><h4>NOTES</h4><p>no notes source wired to radar cards (S3)</p></section>
 <section data-detail="chart"><h4>CHART</h4><p>reserved · empty</p></section>
```
DEVIATION, said (not hidden): unchanged runs INSIDE a quoted line are elided with ` … ` — a `semaphore` line is ≈12 KB of unchanged tap buttons; every changed `[-…-]` / `{+…+}` fragment in the quoted lines is verbatim (ticker → `<ticker>`). The verbatim hunk is `scratch/seam-0923/ladder.diff`, 65556 bytes, for `40`'s hub.

## D3 ATTRIBUTION
29 changed fragments (= the `--stat`'s 29 changed lines, one fragment each: 7 per card × 4 cards + 1), in 7 shapes. Every cause read at `b007ce2e` (the clean worktree tip) by `grep -n` / Read on the file, and in `git diff d327ff1 b007ce2e -- src/cobalt/radar/evaluate.py src/cobalt/cards/…`.

| # | fragment (ticker as `<ticker>`) | × | class | cause file:line at b007ce2e | ruling |
|---|---|---|---|---|---|
| 1 | strip `[-—</span><b><ticker></b><span>overextension-]{+—</span><b><ticker></b><span>unclassified+}` | 4 | INTENDED — evaluator | `src/cobalt/radar/evaluate.py:1111` `extension_direction=real_direction, trade_direction=side, setup_ref=UNCLASSIFIED_SETUP,`; `:164` `UNCLASSIFIED_SETUP = "unclassified"`; replaces the removed `-    setup_ref = next(vs.setup_ref.value for vs in td.valid_setups if vs.relation == wanted)` | FINAL §1 `A-01` (docstring `:41-42`: "No setup is detected: the card's `setup_ref` is the token `UNCLASSIFIED_SETUP`.") |
| 2 | card-title `[-<span>overextension-]{+<span>unclassified+}` | 4 | INTENDED — evaluator | same `evaluate.py:1111` / `:164` | same |
| 3 | why-line `[-<b>overextension-]{+<b>unclassified+}` (rest of the why sentence byte-identical) | 4 | INTENDED — evaluator | `evaluate.py:1139` `f"{formation.setup_ref} · Extension culminating (path A, {formation.leg_count} legs, "` (card_why's Extension sentence, unchanged text; the value is `:1111`'s) | same; `card_why` docstring "The Extension formation keeps its sentence byte for byte" — it did |
| 4 | setup_ref field `[-<b>overextension</b></span><span-]{+<b>unclassified</b></span><span+}` | 4 | INTENDED — evaluator | same `evaluate.py:1111` / `:164` | same |
| 5 | dot cell `{+… data-factor="assumed_formation" title="formed on assumed defaults: anatomy.orientation.extension">assumed_formation · n/a ASSUMED …+}` | 4 | INTENDED — assumed_formation | `src/cobalt/radar/evaluate.py:1156` `def card_dots(`; `:1176` `dots.append(Dot(`; `:1177` `factor=ASSUMED_FORMATION, position=len(ld.definition.quality_factors), source="cobalt-degraded",`; `:1179` `engine_why=f"formed on assumed defaults: {', '.join(keys)}",`; keys from `:1114` `assumed_keys=assumed_closure(td, tunables)` | R2-2 = B |
| 6 | suppression `[-MANUAL-]{+MANUAL; assumed_formation: ASSUMED+}` (div.suppressed ×4 + score_suppressed field ×4; ` (tap to grade)` KEPT — the blockers are mixed MANUAL + ASSUMED) | 8 | INTENDED — suppression | `src/cobalt/cards/scoring.py:256` `blockers = [d for d in dots if d.computed and d.na_reason and d.trader_grade is None]`; `:259` `reason = "required computed dot N/A and untapped — " + "; ".join(f"{d.factor}: {d.na_reason}" for d in blockers)`; `:261` `return reason if all(d.na_reason == "ASSUMED" for d in blockers) else reason + " (tap to grade)"`; `:75` adds `"ASSUMED"` to `NaReason` | R2-2 = B (scoring docstring: the assumed_formation dot "suppresses the score for the card's life") |
| 7 | EMA9 health pill title `[-5.258327362044217306501313365-]{+5.258326394504005343774398213+}` (card 4, IN-TRADE only — the one card with health pills) | 1 | INTENDED — evaluator | `src/cobalt/radar/evaluate.py:980` `ema9 = frames["long"].number("EMA9")`, replacing the removed `-        ema9 = ema(run, defaults.ma.fast).value if run else None` (RTH-only); the atom: `src/cobalt/radar/anatomy/frame.py:564` `**{name: ema_atom(period) for name, period in EMA_PERIODS.items()},` → `:279` `return lambda: _num(ema_back(period, 0)[-1], "insufficient_seed")` → `:257` `chosen = seeded(ema, pre, run, period)` (premarket-seeded EMA, `indicators.seeded`) | [F-10] / FINAL §5 `A-05` (`evaluate.py` comment `:977-979`: "EMA9 has ONE definition — seeded, falling back to RTH-only — and `ema9` (the FILLED card's health input) takes it") |

DEFECT rows: **0**. No fragment carries `bars-stale`, `STALE`, `data-bars-stale` or `stale` in any spelling (the only `stale` hits are the diff header's file name); no cause is under `src/cobalt/aset/` (the renderer's markup around every fragment is byte-identical; only the values it is fed changed). The fixture feeding this test is unchanged by the setups branch: `tests/cobalt/radar_p2_support.py` `fixture_bars` keeps the default `"bars-rubberband.real-shape.json"` (the diff only adds a `filename` parameter).

GATE: every row INTENDED → D4.

## D4 THE PIN
MOVED. Two Edit-tool edits to `tests/cobalt/test_radar_panel_cards.py`, nothing else. New value copied from the printed `SEAM-DUMP setups-c1 0ac9b5d038cf1d598d79867d316fe7976cdec1c8f9df77ecee37753f3d1be051 64804` line (D2 (a)).
- `git diff --stat` → ` tests/cobalt/test_radar_panel_cards.py | 3 ++-` / ` 1 file changed, 2 insertions(+), 1 deletion(-)` — EXACTLY the one file, 1 changed + 1 added line.
- `git diff`, whole:
```
diff --git a/tests/cobalt/test_radar_panel_cards.py b/tests/cobalt/test_radar_panel_cards.py
index 531e5f0d..45b0ff3d 100644
--- a/tests/cobalt/test_radar_panel_cards.py
+++ b/tests/cobalt/test_radar_panel_cards.py
@@ -373,8 +373,9 @@ def test_card_panel_escapes_why_and_notices(evaluated):
 # ---------------------------------------------------------------------
 
 # GOLDEN PINS captured on main's code (`5b208a0`), GREEN there — from then on a GUARD.
+# LADDER pin re-captured 2026-09-23 on setups/seven-0921 (b007ce2e): the setups ladder change adds the assumed_formation dot (R2-2 = B); healthy bars still add nothing (seam-fix-build-2026-09-23.md D3).
 PIN_HEALTHY_POOL_SHA256 = "f2e79add6bc4d4286b381154b071b04ec9e7887467ffd15b0f499e9d62181552"
-PIN_HEALTHY_LADDER_SHA256 = "e617c53c1479314b6074de5409f289238479be31fbbd789b4ee19849f55370d7"
+PIN_HEALTHY_LADDER_SHA256 = "0ac9b5d038cf1d598d79867d316fe7976cdec1c8f9df77ecee37753f3d1be051"
 PIN_HEALTHY_API_SHA256 = "450b3415c2346c8b13b53932c5175f56ee6af78877ca9fc8086ca824601c5462"
 
 # Tonight's `mirrorDegraded` line, byte for byte as main has it (`radar_panel.py:1127`).
```
- Test intent kept: no `assert` removed, no parametrize narrowed, no skip/mark; pool and API pins untouched.
- `uv run pytest -q tests/cobalt/test_radar_panel_cards.py` → `34 passed in 1.29s` (0 failed).
- Commit: `[setups/seven-0921 51afdad0] fix(seam): re-pin the healthy-ladder SHA to the setups ladder change (L68 seam, 09-23)` · ` 1 file changed, 2 insertions(+), 1 deletion(-)`. `git log --oneline -1` → `51afdad0 fix(seam): re-pin the healthy-ladder SHA to the setups ladder change (L68 seam, 09-23)` → `<tip>` = `51afdad0`.

## D5 SUITE
- `ls /Users/cobalt/cobalt-wt/setups-c1/.env` → exit 1, `No such file or directory`.
- `uv run pytest -q tests/cobalt tests/taxonomy` (background, on `51afdad0`) → exit 0: **`2483 passed, 361 skipped, 1 xfailed, 15 warnings in 541.89s (0:09:01)`**. That is 2483 passed and 0 failed, with 0 errors. GATE HOLDS.
- For context only: `07`'s stack ran `2 failed, 2492 passed`, and that stack also carried the smoke-fix branch's tests. setups r4 alone ran `2464/0` before the rebase.
- UNVERIFIED reading, not a claim: the gitignored dump `tests/cobalt/scratch/test_seam_dump_0923.py` sits under `tests/cobalt`, so this run probably collected it (+1 passed). It rewrites `scratch/seam-0923/ladder-setups-c1.html` with the same render. `-q` without `-s` does not print its line, so this read does not confirm it.
- WITH-DB was not run here (offline round; the pin test is DB-free). It runs at `41`'s L68 gate on the stack.

## RESTARTS
`uv run cobalt jobs restarts b007ce2e..51afdad0` → as EXPECTED:
```
path	change	rule	restart
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
RESTARTS: none
```

## CONTINUE
next: none. The run is complete (CLOSE). A relaunch finds the pin commit `51afdad0` and this report committed on top of it, so there is nothing to resume.

## ESCALATE
1. **NEW USE, as named on the launch row (R61 / R60 (1)):** `cd *` and `uv run pytest *` ran ONE scratch test inside `/Users/cobalt/cobalt-wt/stale-marker` (`s2/stale-marker-0921`). `git status --short --branch` showed exactly `## s2/stale-marker-0921` both before and after, so no tracked file changed.
2. **Scratch left on disk for `40`'s hub, all gitignored; the desk cleans up after `41`:**
   - `/Users/cobalt/cobalt-wt/setups-c1/tests/cobalt/scratch/test_seam_dump_0923.py`
   - `/Users/cobalt/cobalt-wt/stale-marker/tests/cobalt/scratch/test_seam_dump_0923.py`
   - `/Users/cobalt/cobalt-wt/setups-c1/scratch/seam-0923/`: `ladder-setups-c1.html`, `ladder-stale-marker.html` and `ladder.diff`

   The setups-c1 dump sits under `tests/cobalt`, so any offline suite run in this worktree probably collects it (see D5) until it is removed. The desk should remove it before `41` re-cuts the gate, or the stack's pass count carries +1.
3. **The prescribed pin comment is narrower than the diff.** The D4 comment line was written verbatim as prescribed and names only the `assumed_formation` dot. D3 proves three more INTENDED causes that also moved the ladder bytes:
   - `setup_ref` `unclassified` (`evaluate.py:1111`, `A-01`)
   - the suppression reason (`scoring.py:259`)
   - the seeded EMA9 (`evaluate.py:980`, [F-10])

   The comment points to this report's D3, which lists all four. The drafter's pre-read named only the dot and the suppression change, so the `unclassified` and EMA9 fragments are new facts for `40`'s checkers to verify.
4. **The pin moved on file evidence only (D3: 29 fragments, all INTENDED).** The check is `40` (L67, three houses); the with-DB proof is `41`'s L68 gate.

SEAM FIX BUILT 51afdad0 | on b007ce2e | offline 2483/0 | with-DB: at the 41 gate | diff: 29 fragments INTENDED, 0 DEFECT | pin: 0ac9b5d038cf | tests changed: 1 | ESCALATE: 4
