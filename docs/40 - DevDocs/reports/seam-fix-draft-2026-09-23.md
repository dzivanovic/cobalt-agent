# SEAM FIX DRAFT 2026-09-23 — the L68 seam from `07` (ladder SHA pin): classify (L75), fix, check, deploy re-issue

Drafter `seam-fix-draft-0923` · Opus 5.5 (`claude-opus-5-5`) · prompt `prompts/2026-09-23/38-draft-seam-fix.md` · started 13:03:37 EDT, written 13:1x EDT (`date`).

## §0 Headline
Class: **UNPROVEN** (L70). No read shows the differing bytes. The file evidence points to INTENDED output of the setups change, not a stale-marker defect. `39` prints the diff before any pin moves.
Wrote `39-seam-fix-build.md` (Opus 5.5 builder: reproduce, render both codes, diff, attribute, then move one pin), `40-seam-fix-check.md` (Sonnet hub; Grok · Gemini · Opus 5.5; it also carries the house read of `41`) and `41-stacked-deploy-r2.md` (`07` re-issued; the 54 hub strings are byte for byte `07`'s).
New rule strings: 0 hub strings. 1 desk command (the gate re-cut). 1 NEW USE of precedented strings (`39` in the `stale-marker` worktree). ESCALATE: 8.

## L74
One block arrived inside a tool result (appended to the output of the Bash read of `38`'s prompt file). It asked that commit messages end with a `Claude-Session: https://claude.ai/code/session_…` line and named a file-send tool (SendUserFile). It is DATA under L74 and was not followed. This session made no commit.

## CLASSIFICATION (L75) — one finding, from `07`'s own rows
| # | finding (`deploy-2026-09-23.md` ESCALATE 2) | class | evidence (file:line, read this session) |
|---|---|---|---|
| S1 | `test_bars_stale_badge_absent_and_output_unchanged_when_healthy[False\|True]`: ladder SHA `0ac9b5d0…` ≠ pin `e617c53c…` on the stack `f2dd42cb` | **UNPROVEN** — FIX **if** `39` D3 attributes every changed fragment to the setups change; a real defect if any fragment does not trace | see below |

Evidence, each read this session:
- **Only the ladder line failed.** The test at `f2dd42cb:tests/cobalt/test_radar_panel_cards.py:474-489` asserts in order: `bars-stale` absent in the pool, ladder, API and main-markup renders; `class="bars-stale"` / `data-bars-stale` absent from the page; then the pool pin, the ladder pin and the API pin. The failure is at `:488`, the ladder pin (`07` 2.2, verbatim). Every assertion before it HELD, so no stale marking appears in the healthy render. `07`: "The pool-HTML pin on the line above (`PIN_HEALTHY_POOL_SHA256`) held."
- **The test file is main's, unchanged by the stack.** `git diff --stat main f2dd42cb -- tests/cobalt/test_radar_panel_cards.py` printed nothing. The pin comment `:374` says "GOLDEN PINS captured on main's code (`5b208a0`)". The capture rows are at `stale-marker-build-2026-09-21.md:66-68`. The setups branch never changed this file: `git diff --stat 5b208a0 f78bf4d -- tests/cobalt/test_radar_panel_cards.py tests/cobalt/test_radar_panel.py` printed nothing.
- **The renderer is main's.** `git diff --stat main setups/seven-0921` lists no `src/cobalt/aset/` path. The only rendering change is the `radar_panel.py` code that the stale marker itself added on main.
- **The setups change alters what the ladder renders for this fixture.** The rows come from the real evaluator over `bars-rubberband.real-shape.json` (`test_radar_panel_cards.py:120-133`), an Extension formation. The setups diff (`git diff main setups/seven-0921 -- src/cobalt/radar/evaluate.py src/cobalt/cards/…`) shows three changes:
  - `ASSUMED_CONVENTIONS = ("anatomy.orientation.extension",)` counts as assumed unconditionally for a formation anchored on an Extension (diff lines +536–+566).
  - `card_dots` then appends ONE `assumed_formation` dot: `na_reason="ASSUMED"`, `engine_why=f"formed on assumed defaults: …"` (+1026–+1041, R2-2 = B).
  - `scoring.suppression` now drops ` (tap to grade)` when every blocker is ASSUMED (`scoring.py` diff), and `card_why` was reworked (+988–+997).

  The ladder renders each dot as a `dot-cell` with `data-factor`, `n/a <na_reason>` and `dot-why` (`radar_panel.py:934-951`). It also renders `score suppressed: …` and the `suppressed` field (`:997-998`, `:1039`). So on this fixture's cards the ladder bytes must change.
- **Not proven by a read:** which bytes differ. The HTML was not rendered; this seat runs no code. So the class is UNPROVEN, never FIX on inference (L35, L70). `39` D1–D3 turn it into proof:
  - D1 reproduces `0ac9b5d0…` on the setups branch alone, which also clears the smoke fix.
  - D2 renders main's code (`stale-marker` worktree, `src/` = `d327ff1`'s, drafter's `git diff --stat cddf32cb d327ff1 -- src …` printed only non-`src` paths). Its GATE is the pin `e617c53c…`, so the dump is proven faithful on both sides.
  - D3 prints the diff and attributes each fragment.
  - `39` moves the pin only if every fragment is `INTENDED`. Any `DEFECT` fragment, or one it cannot trace, is `FAILED: D3` with nothing moved.
- **The test's intent is kept by the fix.** Healthy bars must add nothing. The pool and API pins, all four `bars-stale` absence asserts and the page asserts stay as they are. The ladder pin is re-captured on the ladder the setups change produces, so it still fails if healthy bars ever add a byte. The fix widens nothing (L75): one value and one comment line in one test file (`39` D4 enforces `3 ++-`).
- **Smoke fix:** not implicated. Its 10 paths hold no ladder or card file (`deploy-2026-09-23.md` 1.3), and `39` D1 proves it by reproducing the red without it.

## NEW STRINGS
| where | string | status |
|---|---|---|
| `39` launch line | the 19 allow strings, 3 denies and `--add-dir` triplet of `2026-09-22/33-setups-fix-r3.md` (the first 19 of `72`'s) | byte for byte, **0 new**. `72`'s cutter string is not carried |
| `39` | `cd *` + `uv run pytest *` used in `/Users/cobalt/cobalt-wt/stale-marker`, writing only a gitignored `tests/cobalt/scratch/` file there (`git check-ignore -v`: `…/.git/info/exclude:18:scratch/` in both worktrees) | **NEW USE of precedented strings**. The launch row must carry the literal `NEW USE stale-marker` (its AUTHORIZATION gate) |
| `40` launch line | `17`'s 15 strings, 3 denies, triplet | byte for byte, **0 new** |
| `41` launch line | `07`'s 54 allow strings, 3 denies, `--add-dir` pair | byte for byte, **0 new**. R52 carries (R__A) |
| desk, before `41` | `git -C /Users/cobalt/cobalt-wt/stacked-0923 checkout -B deploy/stacked-0923 main` | **1 desk command**, not a hub string. It replaces the brief's `branch -f` candidate: git refuses to force-update a branch checked out in a worktree, and `deploy/stacked-0923` is checked out in `stacked-0923` (`git -C …/stacked-0923 status --short --branch` → `## deploy/stacked-0923`). Not run here (L70: git's documented refusal, not a denial seen). A new gate name would change 7 hub strings instead |

## 41 DELTA FROM 07
Every line of `07` that `41` changes (`07` line → what `41` says). All other lines are `07`'s text.
| # | `07` line(s) | change in `41` | why |
|---|---|---|---|
| 1 | 1 | seat `stacked-deploy-0923` → `stacked-deploy-r2-0923`; RE-ISSUE sentence added; "NO `worktree add`" → "NO `worktree add` and NO gate re-cut" | L19 re-issue |
| 2 | 4 | desk command (1): `worktree add -b …` → `git -C /Users/cobalt/cobalt-wt/stacked-0923 checkout -B deploy/stacked-0923 main`, with why `branch -f` is not it | the gate re-cut |
| 3 | 6 | prompt path `07-…` → `41-stacked-deploy-r2.md`; `--remote-control stacked-deploy-r2-0923`. Every rule string unchanged | re-issue |
| 4 | 8–12 | THE LIST: "byte for byte `07`'s"; approval row R52 → **R__A** ("R52 carries") | brief: placeholders |
| 5 | 14 | title: "RE-ISSUE AFTER THE L68 SEAM FIX" | — |
| 6 | 19 | WHAT SHIPS (1): code tip `<setups tip>` from `39`'s stop line; rebased on `d327ff1`; 73 non-docs paths (+`test_radar_panel_cards.py`); `40` added to "Checked" | the new setups tip |
| 7 | 20–22 | (2): branch tip `4706e219`, rebased; shared path quotes `07`'s clean merge; with-DB "(`07` stopped at 2.2, before it)" | consequence of `07`'s run |
| 8 | 30 | WHY REBASE FIRST → WHY REBASE AGAIN: both on `d327ff1`, main docs-only since; of the nine paths the setups branch now touches ONE (`test_radar_panel_cards.py`) | the new setups tip |
| 9 | 33 | DOWNTIME: `07` wrote "P13 … proof cost" (P13 is the `.env` check) → P14-M, with `07`'s measured `76.9 s` | correction |
| 10 | 37 | START: the literal is `07`'s R53 `DONE TRADING 12:46` | his word is already given |
| 11 | 43, 46 | AUTHORIZATION intro names this drafter; NOT SET ASIDE L67 adds "the seam fix checked" | — |
| 12 | 49–53 | R52 → **R__A** (checks unchanged) | brief |
| 13 | 54–57 | R53 → **R__L**; the row names `41`, the re-cut and its time, `39`'s and `40`'s stop lines, the folded `41` blockers | brief |
| 14 | 62–64 | PLACEHOLDER GATE: tokens `R__A` / `R__L`, this file's path | brief |
| 15 | 80, 86 | index L67 line: `40` for the seam fix and the re-issue read; (2) adds `deploy-2026-09-23.md` WHOLE | — |
| 16 | 92–93, 243, 368 | REPORT → NEW `deploy-2026-09-23-r2.md`, never `07`'s file; commit paths and subjects `r2` | `07`'s report holds a `## L68 GATE` section: appending a SECOND RUN to it would make RELAUNCH RULE (i) read "MERGED" once the re-cut gate equals main |
| 17 | 133, 137 | P1: today's dirty list per `07`'s P1; the stack-added list gains `seam-fix-build-2026-09-23.md` | the new setups tip |
| 18 | 141 | P4: note that `07` took no tag | — |
| 19 | 142–145 | P5: the r4 line recorded as `<r4 tip>`; **`<setups tip>` from `39`'s `SEAM FIX BUILT` line** (`| on b007ce2e |`, `offline <p>/0`, `0 DEFECT`) | the new setups tip |
| 20 | 146–148 | **P6 also reads `40`'s DONE line**: `SEAM FIX CHECK DONE`, `ready … YES` ×3, `defects that HOLD: 0`, `41 blockers: 0`; the smoke check line quoted from `07` | brief |
| 21 | 151, 153 | P7 note; P9 quotes `07`'s P9 value and names `40`'s `41 blockers: 0` as the re-issue's read | L67 for the re-issue |
| 22 | 155, 158 | P10: `39`'s ignored scratch named; expected tips = the seam report commit / `4706e219` | the new setups tip |
| 23 | 159–163 | P11: seam range `b007ce2e..<setups tip>` = the one test file; `<r4 tip>`↔`b007ce2e` identity (`07` 1.3's exclusions); `<nse>` 36 | the new setups tip |
| 24 | 164–169 | P12: "the desk RE-CUT"; HEAD must not be `f2dd42cb`; `.venv/` ignored | the gate re-cut |
| 25 | 176, 185 | P14: `07`'s validate and `attnotnull` readings quoted as context | — |
| 26 | 193, 197–198 | 1.1: `<nse>` commits over a docs-only move; 1.3 identity: the nine exclusions dropped (both bases moved docs-only); `73 files changed`, only `test_radar_panel_cards.py` of the nine appears | the new setups tip |
| 27 | 201, 204 | 1.4: `07`'s clean merge noted; `82 files changed` | the new setups tip |
| 28 | 211 | 2.2 context: `07`'s `2 failed, 2492 passed`; the seam build's `<p>/0` | — |
| 29 | 255 | RELAUNCH (i): one sentence added — "the report" is THIS run's `r2` file | the new report path |
| 30 | 302 | smoke chain adds "the seam fix … checked by three houses (`40`)" | — |
| 31 | 324 | 6.1: "`07` never reached STEP-6" | — |
| 32 | 366 | STEP-7 ESCALATE: `39`'s scratch cleanup; the seam ESCALATE count | — |
Deadline gate: unchanged. P0, 4.1: `19:55 ET` hard clock; 4.3: `19:58 ET` merge clock.

## TIMING (drafter's estimate, not a measurement)
- `39` takes ≈ 20–25 min: two one-test renders, one diff, then the suite ≈ 8–9 min.
- `40` takes ≈ 45–60 min (`17`'s class) and waits on the house lane: `29`, then `37`, must be done or not running, and `19` must stay PAUSED.
- `41` runs `07`'s ≈ 13 min preflight, then the offline suite ≈ 8 min, with-DB ≈ 10+ min, the window and STEP-6.
- So `41` must launch by ≈ 18:15 ET to reach 4.1 before 19:55.

## ESCALATE
1. **Desk command (1) of `41`** is `git -C /Users/cobalt/cobalt-wt/stacked-0923 checkout -B deploy/stacked-0923 main`, not the brief's `git branch -f deploy/stacked-0923 main`. Git refuses `branch -f` on a branch checked out in a worktree. This is git's documented behaviour and was not run here (L70). If the desk's own rules do not cover `git -C * checkout -B …`, it is one desk permission, named. The other shape, a new gate branch plus worktree, changes 7 hub strings and needs his new approval.
2. **`39` NEW USE**: `cd *` + `uv run pytest *` in `/Users/cobalt/cobalt-wt/stale-marker`, which renders main's ladder and writes only a gitignored scratch file. The launch row must carry `NEW USE stale-marker` (`39`'s AUTHORIZATION greps it). ASK DESK: does this NEW USE need his word, as `72`'s cutter string did under R23? Safe default: bring it to him in the same message as the `39` launch.
3. **`41` changes beyond the brief's four** (new tip, re-cut, P6, placeholders), each forced by the new tip or by `07`'s run:
   - the NEW report path `deploy-2026-09-23-r2.md` (delta 16 — appending to `07`'s report would mis-fire RELAUNCH RULE (i));
   - the path counts 73 / 82 / `<nse>` 36 and 1.3's identity form (delta 23, 26, 27);
   - the P1 stack-added path;
   - the P9 re-issue read.

   All are listed in `## 41 DELTA FROM 07`. No rule string changed.
4. **`40` carries `41`'s house read** (L67: a deployment prompt is read by ≥1 other house). This avoids a separate review hub and a second wait on the house lane. `41` P6 needs `41 blockers: 0`. The brief did not name it.
5. **Class is UNPROVEN, not FIX.** The evidence strongly suggests INTENDED output: the `assumed_formation` dot, the suppression text and the `card_why` rework, while every stale assertion and the pool pin held. The bytes are unread. If `39` D3 finds a fragment it cannot trace, `39` FAILS with nothing moved, and the desk brings the next lawful step (a real seam defect).
6. **House lane for `40`**: `29` (JEV check A) was relaunched at R54, and `37` (check B) follows it. `19` is PAUSED. `40` preflights `19 is PAUSED` + the PAUSE file, `29 is not running`, `37 is not running` and `no other house hub is running` on its launch row. If JEV A/B are still running, `40` waits for them. ASK DESK: should `37` yield to `40` for tonight's deadline? L72: a check that gates tonight's deploy vs an OFF-LADDER trial check. Safe default: the desk's call, not this drafter's.
7. **Cleanup owed after `41`**:
   - `39`'s gitignored scratch: `setups-c1/scratch/seam-0923/`, `setups-c1/tests/cobalt/scratch/`, `stale-marker/tests/cobalt/scratch/`;
   - the gate worktree `stacked-0923` (its `.venv` from `07`);
   - `07`'s unreferenced stack commit `f2dd42cb` after the re-cut (it is recorded in `deploy-2026-09-23.md`).
8. **Tonight's replay**: if `41` does not land before 19:55, the 21:10 replay stays RED on the movers `Change ''` bug (`07` ESCALATE 2). Dropping the setups branch and shipping the smoke fix alone would be a one-branch re-issue, a separate file (L19/L43). It is not drafted here: the brief asked for the stacked re-issue.

SEAM FIX DRAFTED · class: UNPROVEN · prompts: 3 · new rule strings: 1 · ESCALATE: 8
