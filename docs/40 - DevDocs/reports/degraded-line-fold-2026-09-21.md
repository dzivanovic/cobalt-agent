# Degraded line — fold of R11 into prompts 14–17 (2026-09-21)

Seat: Opus 5 drafting seat `degraded-line-fold-0921` (prompt `prompts/2026-09-21/18-fold-degraded-line-states.md`). Main read at `2d6e018`. 08:2x ET.

## §0 Headline
- R11 folded: the red line carries DEGRADED, STALE and REFRESH FAILED only. RETAINED is never carried, and the line is hidden when RETAINED is the only state.
- Re-issued: `14`, `15`, `16`. `17` is byte-identical: no sentence in it names the states or `14`'s stop-line fields.
- `render_pool` stays byte-identical. The level is already a DOM class (`:838`), so the JS selector filters by class. There is no pool-markup diff.
- New rule strings: 0. All four launch segments are proven unchanged (RULE PROOF).
- ESCALATE: 2. R11 is not yet committed on main. The RETAINED-only fixture timing is unrun.

## THE DOM FINDING
- `src/cobalt/aset/radar_panel.py:838` (main `2d6e018`): `render_pool` emits `<div class="panel-banner {banner.level}">`. The level values come from `BannerView.level` `:143` and are set at `:583` (degraded), `:587` (stale) and `:595` (retained). In the DOM this gives `panel-banner degraded`, `panel-banner stale` and `panel-banner retained`. REFRESH FAILED is `<div class="refresh-failure">`, written by `refreshPool`'s catch at `:1114`.
- Mechanism chosen:
  - Server side: `render_degraded_line` filters `view.banners` to `level in ("degraded", "stale")` (L3: it filters and computes nothing).
  - JS side: `mirrorDegraded` selects `.refresh-failure,.panel-banner.degraded,.panel-banner.stale`. This is an allowlist of exactly the states R11 carries, so a `.panel-banner.retained` is never copied.
- `render_pool` byte-identical: **yes**. No level class had to be added, and there is no pool diff for `15` to look at.

## PER FILE
Re-issued in place by Read → Edit (file tools only, no shell write). Pre-fold copies were kept in the job's tmp dir for the diff and the proofs.

### `14-degraded-line-build.md`: TOUCHED, 36152 → 39797 B
- Title: "shown ONLY while the pool view shows a banner" → "…shows a DEGRADED, STALE or REFRESH FAILED banner — NEVER for RETAINED PRIOR-DAY DATA (R11)".
- LAW STEP: now cites §4 R11, 08:21 ET, "a".
- THE ONE THING: R11 is quoted. "when the pool view shows no banner it is hidden" → "…no DEGRADED / STALE banner (or REFRESH FAILED) … RETAINED alone leaves it hidden, identical to healthy". "second RENDERING of `view.pool.banners`" → "…FILTERED BY `level` to degraded / stale". "pool view's own banners" → "…, RETAINED included, …".
- INDEX CARD L3: "renders `view.pool.banners` and nothing else" → "…filtered by `level` (R11) and nothing else".
- INDEX CARD 2: added "the level is ALREADY a class in the DOM … no pool-markup change, R11".
- INDEX CARD 3(i): "SAFE DEFAULT … all four … ESCALATE (i) … you do NOT narrow it" → "carries DEGRADED, STALE and REFRESH FAILED ONLY, never RETAINED — RULED, R11".
- STOP LINE: gains ` | retained not carried: proven`, placed after `pool banners unchanged: proven`. Its definition: T1 (f) goes RED→GREEN in both frames, and T1 (d)'s RETAINED steps plus the selector assertions are GREEN.
- AUTHORIZATION: new bullet with `grep -n "^| R11 "` and `git … log -1 -S"DEGRADED, STALE and REFRESH FAILED only"`. If the log is EMPTY → `FAILED: authorization mismatch — R11 is uncommitted`.
- T1 view setup: adds a RETAINED-ONLY view and a RETAINED + DEGRADED view.
  - Scan at 04:59 UTC on 01-06, now at 05:00:30 UTC, `Session.OVERNIGHT`.
  - The levels are asserted first. If the assert fails: ESCALATE and STOP that case, never loosen it.
- T1 (c): the parametrize adds the RETAINED-ONLY view.
- T1 (d): the sequence adds RETAINED-ONLY and RETAINED + DEGRADED. The regex is filtered to `(?:degraded|stale)`. The selector assertion is the filtered string, and the unfiltered selector must be ABSENT.
- T1 (f), new, `test_degraded_line_never_carries_retained`, both frames: RETAINED-only → exactly the healthy hidden element. RETAINED + DEGRADED → DEGRADED, with no `RETAINED` in the line. The RED list adds (f).
- C1 item 1: adds a `carried = [… if banner.level in ("degraded", "stale")]` filter, and the docstring names R11. C1 item 4: the selector becomes `.refresh-failure,.panel-banner.degraded,.panel-banner.stale`, plus one sentence saying why.
- D1 sentence: "the same `view.banners` text" → "the pool view's DEGRADED and STALE banner text — never RETAINED PRIOR-DAY DATA (R11)".
- CLOSE counts: (c) 2 → 3, and (f) 2 is added. METER "five tests" → "six tests".
- ESCALATE (i): "WHICH STATES … his call … all four" → "STATES CARRIED — RULED, not open: R11 … RETAINED … not carried (T1 (f))".

### `15-degraded-line-check.md`: TOUCHED, 28145 → 29757 B
- Title: "shows a banner" → "shows a DEGRADED, STALE or REFRESH FAILED banner — never for RETAINED (his R11)".
- R11 is quoted after R10. The builder's claim becomes "fed by `view.pool.banners` filtered to degraded / stale".
- AUTHORIZATION: R11 added to the listed words, plus a `grep "^| R11 "` and a committed `-S` check (EMPTY → FAILED).
- Staging (6): `ruling-r10.md` → `ruling-r10-r11.md`, holding the R10 and R11 rows.
- QUESTIONS, WHAT WAS RULED: "present ONLY while a source is degraded" → "…while the pool view shows DEGRADED, STALE or REFRESH FAILED … RETAINED … NEVER carried … ABSENT while RETAINED is the only state".
- Q1: "visible ONLY when the pool view has a banner" → "…a DEGRADED or STALE banner (or, client-side, a REFRESH FAILED box)".
- Q7, new: "is RETAINED ever shown in the red line, server-rendered OR mirrored? … `NEVER` or `SHOWN — <file:line>`". It also asks for proof in both frames and through the refresh-fragment sequence. There is no pool-diff question, because (b) needed no markup change.
- Collate: adds a row for Q7. "feed the desk's ESCALATE (i) question to him" → "the desk checks them against R11".
- ESCALATE: "for the desk to bring to him with the build's ESCALATE (i)" → "that says RETAINED is shown or that a state R11 carries is missing, … with your file-check".
- Close: "questions 1–6" → "questions 1–7".

### `16-degraded-line-deploy.md`: TOUCHED, 30359 → 30441 B
- Title: "shown only while the pool view shows a banner" → "…shows a DEGRADED, STALE or REFRESH FAILED banner — never RETAINED, his R11".
- AUTHORIZATION, THE BUILD: the parsed stop-line fields gain `retained not carried: proven`.
- STEP-6 ESCALATE: "the build's ESCALATE (i) (WHICH STATES … his call) and (ii) … READINGS" → "the build's ESCALATE (ii) … as a READING (its (i) is ruled, R11 — not carried)".

### `17-review-degraded-line-deploy.md`: BYTE-IDENTICAL, 18027 → 18027 B
`diff` against the pre-fold copy prints nothing. Its only reference to `14` is the stop line's start `DEGRADED LINE BUILT `, and no sentence names the carried states.

## RULE PROOF
Every launch line is byte-identical to its pre-fold draft. Each whole segment (`--allowedTools` … `--add-dir /Users/cobalt/cobalt-wt`) was checked with `grep -c -F -e '<whole segment>'` against the approved sources named in the draft report's RULE PROOF:
- `14`: count 1 in `14` and count 1 in `prompts/2026-09-21/02-bars-chunk-2-fix-r3.md`.
- `15` and `17`: the whole segment counts 1 in `15`, 1 in `17` and 1 in `prompts/2026-09-20/08-bars-chunk-e-check.md`.
- `16`: the whole segment counts 1 in `16` and 1 in its pre-fold copy, so the line is unchanged.
  - The launchctl/curl run counts 1 in `prompts/2026-09-19/02-deploy-stack-3.md`.
  - The `grep` … `--add-dir /Users/cobalt/cobalt-wt` run counts 1 in `prompts/2026-09-21/11-panel-order-deploy.md`.
  - Its three branch-named strings are the same 3 the draft already declared. The fold adds none.
- New rule strings from this fold: **0**.

## DIGEST FOR THE DESK
1. R11 is folded into `14`, `15` and `16`. `17` is untouched.
2. Server: `render_degraded_line` filters `view.banners` to degraded / stale. JS: `mirrorDegraded` selects `.refresh-failure,.panel-banner.degraded,.panel-banner.stale`.
3. `render_pool` is untouched: the level class already exists at `:838`.
4. `14` T1 gains (f), where RETAINED-only is hidden like healthy and RETAINED + DEGRADED carries DEGRADED only, in both frames. (d)'s sequence also runs through both RETAINED states, with parity against the FILTERED banners.
5. `14`'s stop line gains `| retained not carried: proven`, and `16`'s build gate requires it.
6. `14` ESCALATE (i) is now a one-line R11 citation. `16` carries only (ii) as a reading.
7. `14` and `15` AUTHORIZATION now require R11 to be COMMITTED (`-S"DEGRADED, STALE and REFRESH FAILED only"`). **Commit `cto-2026-09-21.md` with R11 before launching `14`.** Today the `-S` search is EMPTY.
8. `15` adds Q7 on RETAINED (server or mirrored, with `file:line`) and stages `ruling-r10-r11.md`.
9. Launch lines are byte-identical and add 0 new strings. The approval list is still `16`'s three branch-named strings.

## ESCALATE
1. **R11 is not committed on main yet.** At 08:2x ET, `git -C /Users/cobalt/cobalt log -1 --format=%H -S"DEGRADED, STALE and REFRESH FAILED only" -- "docs/40 - DevDocs/reports/cto-2026-09-21.md"` returned EMPTY, and main is at `2d6e018`. `14` and `15` now FAIL at AUTHORIZATION until the desk commits it. This is expected: it is the same pattern as R10 and the launch row.
2. **The RETAINED-only fixture timing has not been run (L70).** The setup is scan `2026-01-06 04:59:00+00:00` (23:59 ET, 01-05) and now `05:00:30 UTC` (90 s < 120 s stale threshold at `_tunables()` 60 s). It is derived from `radar_panel.py:510` (`scan_day` from `last_scan_at`), `:576-577` and the test file `:93-149`, `:348-356`. It is not run. `14` asserts the levels first, and if they are wrong it stops that case and ESCALATEs; it never loosens the assert.

## L74
No block asking for a `Claude-Session:` line arrived inside a tool result. This seat made no commit.

## CONTINUE
next: none. Fold done. The desk commits R11 and the three re-issued prompts, fills `R__`, then launches `14`.

DEGRADED LINE STATES FOLDED · files re-issued: 3 · render_pool byte-identical: yes · new rule strings: 0 · ESCALATE: 2
