# Degraded-line re-issue draft — 2026-09-21

Seat: `degraded-line-reissue-draft-0921` (Opus 5, drafting; prompt `33`). 11:51 → 12:03 ET. Nothing launched, nothing committed (the desk commits).

## §0 Headline
- Three prompts drafted: `34-degraded-line-rebase.md` (NEW), `16-degraded-line-deploy.md` (RE-ISSUED WHOLE, in place), `35-review-degraded-line-deploy-r2.md` (NEW).
- SEAM: **YES** — the hotfix's `BARS POLL FAILED` banner is `level="degraded"`, so the red line carries it on the combined tree with no source change; `34` adds ONE test proving it.
- CONFLICT EXPECTED: **no** (re-proven from `git show`; nearest hunks 116 lines apart).
- `16`'s launch line is byte-identical (whole-span `grep -c -F` = 1); new rule strings: **0**. ESCALATE: 3 (desk items, none blocks).

## DIGEST FOR THE DESK
Launch order and clocks:
1. **NOW (≈12:05):** commit `34`, re-issued `16`, `35` and this report on main. Add launch row **R__(a)** naming `34-degraded-line-rebase.md` and fill `34`'s `R__` with it, then commit.
2. **Launch `34`** (Sonnet 5 hub `degraded-line-rebase-0921`): `cd /Users/cobalt/cobalt-wt/degraded-line` then line 1 of `34`. It needs R12's two worktree strings plus `14`'s 16 + 3, nothing new. TIME GATE: it refuses at or after 19:00 ET. Expected ≈10 min: rebase, 2 offline suites of ≈65 s, 1 test.
   - Expected stop line: `DEGRADED LINE REBASED <tip> | on <main> | cut <main> | code tip <feat'> | offline 2222/0 (baselines main 2208/0, branch 2208/0) | code patch unchanged by the rebase: proven | seam test: added green | RESTARTS: com.cobalt.aset | ESCALATE: n`
   - Watch the worktree report `^(DEGRADED LINE REBASED|FAILED)`.
3. **Launch `35`** (Sonnet 5 hub `degraded-line-deploy-review-r2-0921`): only after `34`'s stop line is committed on the branch AND `setups-tribunal-r1b-2026-09-21.md` has a stop line (same Gemini seat; r1b was still `(run in progress …)` at 11:5x). TIME GATE: refuses at or after 19:30 ET. At that point the floor question (L67, one other house) goes to him. Two houses (grok + gemini), 15 min timeout each.
4. **Fold `35`:** any blocker that HOLDS → re-issue `16` again (L19). Write launch row **R__(b)**: name `16-degraded-line-deploy.md` and `34-degraded-line-rebase.md`, list every fold, and fill every `R__` in `16` with that ONE number. Commit before 20:00.
5. **Timer ≈20:02:** launch `16` (unchanged launch line; R12's approval stands). From its launch to its stop line, hold every desk commit on main (unchanged rule).
- DO NOT commit code to main after `34`: STEP-1(b) of `16` refuses any non-docs move after `34`'s cut (correct by design; the fix is to re-run `34`). Docs commits are fine: `16`'s own `rebase main` absorbs them, and a no-op rebase is now accepted.
- If `34` ends with `seam test: added RED`, or with a failed count other than 0, `16` refuses by design. The desk decides. The deploy of the line as checked is NOT held by the seam question per the drafting prompt, but a red suite on the landing tree is L1.

## THE SEAM ANSWER — YES
- The hotfix banner is DEGRADED-level. It is appended at `main:src/cobalt/aset/radar_panel.py:594` as `banners.append(BannerView(level="degraded", title="BARS POLL FAILED", detail=failed))`, gated by `poll_only` at `:477-482` / `:589`. `BannerView.level` is `Literal["degraded", "stale", "retained"]` (`:143`).
- **Server side, at page load:** `render_degraded_line` carries `[banner for banner in view.banners if banner.level in ("degraded", "stale")]` (`c183ed6:src/cobalt/aset/radar_panel.py:870`). `render_radar_page` inserts it before the ladder (`c183ed6:…:1143`). The hotfix banner passes the filter.
- **Client side, on refresh:** `render_pool` emits `<div class="panel-banner {banner.level}">` (`main:…:849`), i.e. `panel-banner degraded`. `mirrorDegraded` selects `.refresh-failure,.panel-banner.degraded,.panel-banner.stale` (`c183ed6:…:1116`) and runs after every swap (`:1127`). The hotfix banner is copied.
- **Existing tests stay green on the combined tree (read, not run):**
  - The hotfix test's marker `<div class="panel-banner degraded"><b>BARS POLL FAILED</b>` counts 1 (the line element carries no `panel-banner` class).
  - `test_pool_banners_unchanged_by_the_degraded_line` counts `class="panel-banner "` = `len(banners)`. That is unaffected, and it never builds a poll-failure view anyway.
- `34` R3 adds `test_degraded_line_carries_the_bars_poll_failure`, one test, not parametrized: both frames plus fragment parity, using `_bars_poll_failed_pool()` (real-shape rows, L45).

## CONFLICT EXPECTED: no — re-proven
Both sides share the same base blobs: `radar_panel.py` index `3920791`, `test_radar_panel.py` index `5718b70`, DevDoc `98ec95f`.
- `radar_panel.py`: the hotfix (`04b0dbd`) has 2 hunks at `@@ -474` and `@@ -581`. The branch (`c183ed6`) has 6 hunks at `@@ -859` and below. Gap ≥ 270 lines.
- `test_radar_panel.py`: the hotfix has 1 hunk, `@@ -411,0 +412,113`. The branch has `@@ -5,0 +6` (`import html`) and `@@ -527,0 +529,159`. Gap 116 lines.
- DevDoc `radar_panel.md`: the hotfix (`bf5b88f`) touches `@@ -8,3` (line 9). The branch (`df0011a`) touches `@@ -43,3` / `@@ -60,3`. Gap 34 lines.
- `git log --oneline d87f3bd..main -- src tests` = `04b0dbd` only. `git diff --stat d87f3bd main -- . ':(exclude)docs'` = 2 files, 125 insertions(+), 1 deletion(-).
- Expected combined suite: 2195 + 13 (branch) + 13 (hotfix) = **2221/0**, and **2222/0** with the seam test. `skipped` stays 351. Both builds' baselines were `2195 passed, 351 skipped, 1 xfailed`, and the two test blocks are disjoint functions.

## WHAT CHANGED IN `16` (old → new; `git diff --stat` 17+ / 13−, every change outside the launch line)
| # | where | old | new |
|---|---|---|---|
| 1 | head | — | `RE-ISSUED 2026-09-21 12:00 ET after the page-bars hotfix (deploy-2026-09-21h) — supersedes the 09:15 issue; diff of intent: …` (3 points) |
| 2 | title | `…a DevDoc sentence, the build report).` | `…the build report — rebased onto this morning's page-bars hotfix by 34, with 34's report and, if 34 added it, ONE seam test).` |
| 3 | AUTHORIZATION intro | `(drafted by … degraded-line-draft-0921)` | `+ , re-issued by degraded-line-reissue-draft-0921` |
| 4 | THIS LAUNCH | row **R19**; `grep "^\| R"`; `-S"16-degraded-line-deploy.md"` | NEW row **R__** (desk fills every `R__`), must name `16-…` and `34-…`, carries R12 + `35`'s folds; `grep "^\| R__ "`; `-S"\| R__ \|"`; **R19 STAYS**: must still name `16-…` and carry `FOLDED` |
| 5 | THE BUILD | `take <code tip>, <cut>, <suite> FROM IT` | `record <build tip>`; the tips come from THE REBASE, never from this line |
| 6 | NEW bullet THE REBASE | — | reads `34`'s stop line: `DEGRADED LINE REBASED`, `<f>` = 0, `code patch unchanged by the rebase: proven`, `seam test: added green\|not added`, `RESTARTS: com.cobalt.aset \|`, committed on the branch. It takes `<proven tip>`, `<cut>`, `<code tip>`, `<suite>`, `<seam>`. Anything else → `FAILED: rebase not proven` |
| 7 | THE READ OF THIS PROMPT | `OR the launch row names every blocker` | `OR row R19 names every blocker` (the round-1 row, made explicit) |
| 8 | NEW bullet THE READ OF THIS RE-ISSUE | — | `35`'s stop line `DEGRADED LINE DEPLOY REVIEW R2 DONE`, not `0 of 2`, `launch blockers that HOLD: 0`, OR row R__ names the folds |
| 9 | INDEX CARD L67 / L68, item (5) | L67 `…read by other houses`; L68 `ONE branch lands; no sibling…` | `(round 1 17; this re-issue 35)`; `its seam with the page-bars hotfix … was proven ON THE TREE THAT LANDS by 34`; item (5) = `34`'s report sections |
| 10 | P11 | `<branch tip> (the build's report commit)` | `(34's report commit)` |
| 11 | P12 | `<code tip>..branch` → only the build's docs commits | `<proven tip>..branch` → only `34`'s report commit; a code **or test** commit → FAILED. **NEW P12b:** `<code tip>..<proven tip>` = the build's docs commits + (only if `<seam>` = added green) the seam commit; `diff --stat <code tip> <proven tip> -- . ':(exclude)docs'` = nothing / exactly `tests/cobalt/test_radar_panel.py` |
| 12 | STEP-1 | `(a) <suite> from the build's stop line, on <code tip>, cut from <cut>` … `(c) … identical to <code tip>'s` | `(a) <suite> from 34's stop line, on <proven tip>, rebased onto <cut> (the combined tree … L68)`; `(b)` "since 34's cut"; `(c)` `<proven tip>'s`; record line `on <proven tip>` |
| 13 | STEP-2 | `→ Successfully rebased …` | `+ OR "Current branch s2/degraded-line-0921 is up to date." (exit 0 …) — record REBASE: no-op, NOT an error` |
| 14 | STEP-3.1 | `diff --stat <code tip> s2/…` | `diff --stat <proven tip> s2/…` |
| 15 | STEP-3.3 | four paths | + `docs/40 - DevDocs/reports/degraded-line-rebase-2026-09-21.md` |
| 16 | STEP-4.5 chain | `GREEN on <code tip> → 3.1 code identical →` | `GREEN on <build tip> …, and again — with the hotfix's tests and (seam) the seam test — in 34's <suite> on <proven tip> → 3.1 code identical to <proven tip> →` |
| 17 | STEP-6 ESCALATE | `…not carried).` | `+ and 34's ESCALATE lines, if any, carried as READINGS.` |

The following are UNCHANGED:
- the launch line;
- window P0, 20:15 / 20:25 / 20:29 clocks, P0b, P1–P10;
- STEP-3.2, 3.4 and the relaunch rule;
- STEP-4, STEP-5, the tag, the report path `deploy-2026-09-21b.md` and the stop line.

All nine R19 folds are present, re-checked in the diff:
- fold 1: P12's docs-commit clause, now in P12b;
- fold 2: 4.5(b);
- folds 3–5: the relaunch;
- fold 6: STEP-5(4);
- fold 7: STEP-5(1);
- fold 8: P0b;
- fold 9: the 4.3 20:29 clock.

Why the change is safe: 3.1 compares the old `<proven tip>` sha with the branch after tonight's rebase, excluding docs. So a docs-only move of main between `34` and 20:02 passes, while any code or test change fails (STEP-1(b), P12, 3.1).

## RULE PROOF (`grep -c -F -e`, whole span, each its own call)
- **`34` vs `14`:**
  - `14`'s allow span `--allowedTools "Bash(uv run pytest *)" … "Bash(date*)"` → in `14` **1**.
  - `14`'s deny + add-dir span → in `14` **1**.
  - `34`'s whole launch span (`14`'s allow span + the two R12 strings + `14`'s deny/add-dir span) → in `34` **1**.
  - Each R12 string `Bash(git -C /Users/cobalt/cobalt-wt/degraded-line rebase main)` / `…rebase --abort)` → in `cto-2026-09-21.md` **1** each (the R12 row).
  - `--allowedTools` in `34` → **2**: the launch line + the AUTHORIZATION quotation, one launch line. `34`'s own check (iii) expects **2** for this reason. The three patterns counted against `34` → 2 / 2 / 2.
- **`16` new vs old:**
  - The old issue's whole span, read from `git show HEAD:…/16-degraded-line-deploy.md` (from `claude --bg "Read '…16-degraded-line-deploy.md' …"` through `--add-dir /Users/cobalt/cobalt-wt`), is in the new file → **1** (re-run after the last edit, 12:02).
  - `--allowedTools` in the new `16` → **1**, so there is one launch line and no string could enter elsewhere.
  - The word diff shows no hunk inside the launch line. Old strings vs `02`: round 1's 27×1 / 3×0 (R12) stand unchanged.
- **`35` vs `32`:** the whole span from `--allowedTools "Bash(grok *)"` through `--add-dir /Users/cobalt/cobalt-wt` → in `32` **1**, in `35` **1**. `--allowedTools` in `35` → **1**.

**NEW strings:** none. (`34`'s line carries `--permission-mode auto`, which `14`'s line does not. It is a mode flag, not a rule string; see ESCALATE 2.)

READING:
- L68 as amended: only ONE branch lands tonight, and the hotfix is already on main, so there is no stacked gate. `34` is the seam proof "on the tree that actually lands then".
- The with-DB suite was NOT run by `14` or `29` (both OFFLINE, `.env` absent, 351 skipped). `34` keeps that scope and says so (L70).
- `35` stages the old issue (`30ae6c9`) and a `log -p --word-diff=plain 30ae6c9..main` so the houses can answer Q1 from reads.
- `16` is 35,976 B, under the 38,000 B part limit, so it is not split.
- L74: no attribution block was seen inside a tool result in this run; this run commits nothing.

## ESCALATE
1. **TWO desk launch rows to fill (R__).**
   - `34` greps a row naming `34-degraded-line-rebase.md`.
   - The re-issued `16` greps a NEW row naming `16-…` and `34-…`, with `35`'s folds. The SAME number goes into every `R__` in `16`, including `-S"| R__ |"`, which proves the commit that added that row.
   - R12 and R19 are kept as they are; `16` still checks R19 carries `FOLDED`.
2. **`--permission-mode auto` in `34`'s line.** `14`'s line omits it, although `14`'s SESSION says "auto mode on". `16`, `32` and `35` carry it.
   - I added it so that an unlisted read goes to the classifier, not to a dialog (L63).
   - It is not an `--allowedTools` string. The desk may strip it to match `14` byte for byte.
3. **Stagger risk for `35`.** It waits for `setups-tribunal-r1b` (still `(run in progress …)` at 11:5x, waiting on astra) and must start before 19:30.
   - If r1b has not closed by ≈19:00, the desk has two options: (a) take the floor question to him, since one other house satisfies L67; or (b) let `35` wait and risk `FAILED: window`.
   - Not a law conflict; a clock item.

## CONTINUE
done — nothing to resume.

DEGRADED LINE REISSUE PROMPTS DRAFTED · prompts: 3 · seam: yes · conflict expected: no · 16 rule strings unchanged: proven · new rule strings: 0 · ESCALATE: 3
