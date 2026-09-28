# SETUPS DEPLOY R2 DRAFT — 2026-09-24 (`09-draft`: re-issue of `05` as the stacked set + its house read)

## §0 Headline
- Branches: 2 — `setups/seven-0921` + `replay/mover-partial-0924`. `08`'s last line, read first (`tail -n 3`, 07:04 ET): `MOVER BARS FIX CHECK DONE · round: 1 · opus: CHECK MOVER BARS: FIX STANDS · ready for a deploy prompt: YES · grok: CHECK MOVER BARS: FIX STANDS · ready for a deploy prompt: YES · sol: NOT SEATED (METER — retry after Sep 26th, 2026 6:47 AM) · gemini: NOT SEATED (R96/R97) · defects that HOLD: 0 · ESCALATE: 9`.
- Written: `prompts/2026-09-24/09-setups-deploy-r2.md` (110,220 B; `05` + 8 folds + R118 + `07` carries, `66`'s gate-branch shape) and `prompts/2026-09-24/10-review-setups-deploy-r2.md` (`06`'s shape; its 9 allow strings, 3 denies, `--add-dir` triplet = `06`'s, `cmp` identical).
- Rows: 4 (R119 ×2 + R82 ×2; `dist.k.vwap` held, R118). Known red: none. New rule strings: 0 (51 allows, all in `66`'s pool; `comm` left side empty).
- Shape change to note: the desk re-cuts the gate ON THE MOVER TIP, not on `main`. That avoids one new string. ESCALATE 1 asks the desk to confirm. A `05` defect that `06` did not catch is fixed: the `rules.yaml` exclusion, ESCALATE 2.
- ESCALATE: 7.

## FOLDS
Each row: `06` `## Folds proposed` n → where it landed in `09` (line numbers in `09-setups-deploy-r2.md`).
| # | before (`05`) | after (`09`) | `09` line |
|---|---|---|---|
| 1 | 4.1: `On either FAILED, nothing is down and nothing merged: go to STEP-7.` | `On the BETWEEN FAILED write the stop line and do NOT commit the report (main must stay <pre-merge> for RELAUNCH (iv)); on too late, go to STEP-7.` Carried into THE WINDOW (BETWEEN bullet), REPORT (commit points), YOU CAN ALWAYS STOP and STEP-7 5 | 303; 42; 111; 70; 435 |
| 2 | RELAUNCH (i): `then 4.7 onward.` · 6.4: `Anything else → R119: NOT WRITTEN — dry run <what>` | (i): `then 4.7 onward, unless (vi)'s condition also holds: then (vi) applies first.` · 6.4: `no change because the four rows are already there = WRITTEN (relaunch, (vi)); anything else → NOT WRITTEN`. Plus one sentence in 6.5, `On a relaunch whose 6.4 read "already there", 6.5 is still run once: an idempotent no-change apply` (ESCALATE 5) | 292; 403; 404 |
| 3 | THE WINDOW: `MERGE CLOCK before **20:22 ET**` (PAUSE) | `MERGE CLOCK = **20:28 ET minus P14-M's proof cost in seconds, never later than 20:22 ET**` (recorded as `<pause merge clock>` at P14-M; 4.1 uses it) | 40; 212; 301 |
| 4 | P-HIS: `-S"DONE TRADING"` | `-S"DONE TRADING <hh:mm>"`, `<hh:mm>` = the time the grep matched, typed literally; the reason is given (`06` row 6) | 135 |
| 5 | 2.3 (a): `cp /Users/cobalt/cobalt/.env …` | `ONLY after 2.2's <task-notification> has arrived and its tail -n 3 is read and green: cp …` | 247 |
| 6 | STEP-5 (2): `HEAD is <ship>.` | `HEAD is <stack-final>, the 3.1 merge; otherwise NO revert: end FAILED: STEP-5 (2) — HEAD is <HEAD>, not <stack-final>; no revert made … aset: DOWN — radar: DOWN`, residents left DOWN and named. Added to the "ONLY endings with a resident DOWN" list | 346; 358 |
| 7 | STEP-5 (4): `Re-run 4.7 (a), (b), (c), (e) and (g)` | `Re-run 4.7 (a), (b), (c), (e), (f) and (g)` (with (f)'s range stated) | 355 |
| 8 | 6.7: no radar-cycle requirement | `FIRST date, then tail -n 12 …/radar.err → a radar cycle: line stamped AFTER <t write>` (three tails at most, as 4.7 (b), with 4.7 (b)'s PAUSE provision applied the same way). `<t write>` = `date` after 6.5 | 406; 404 |
`06`'s ESCALATE 1 is answered by the desk (the launch shell has neither `COBALT_ALLOW_DEV_ENTRY` nor `COBALT_VAULT_PATH`, `printenv | grep -c` = 0). It is carried into 6.3 as text, with one added guard: the diff paths must lie under `~/dev-vault-cobalt` (line 402). Fold 1 is the desk's answer to `06` ESCALATE 2 ("TAKEN").

## R118
His R118 (`cto-2026-09-23.md` line 126): the deploy holds `dist.k.vwap` and STEP-6 writes FOUR rows. There is no known red, and R107 is superseded. Every change, `05` line → `09` line:
| `05` line | `05` text (R107 / five) | `09` |
|---|---|---|
| 11 | title `HIS FIVE ASSUMED ROWS (R119 ×3 + R82 ×2)` | 11: `HIS FOUR ASSUMED ROWS (R119 ×2 + R82 ×2; dist.k.vwap HELD, R118)` |
| 27 | `his five rows … (STEP-6.8, R107: EXPECTED RED on vwap-continuation)` | 28: `his FOUR rows … (STEP-6.8, R118: EXPECTED GREEN)` |
| 54 | AUTHORIZATION **R107** grep (`ALL THREE R119 rows`, `EXPECTED RED`) | 56: **R118** grep (`Let's go with B`, `HOLDS`, `FOUR rows`) + `-S"| R118 |"` |
| 56 | R3 "the STEP-6 vault write" | 59: kept, plus `(R3 named FIVE rows; the FOUR written here are a subset of them — R118.)` |
| 99 | report title `his five assumed rows` | 104: `his four assumed rows` |
| 101 | sections list `## R119 → ## KNOWN RED → ## ESCALATE` | 106: `## KNOWN RED` removed |
| 153 | P5 `R119 vwap:` field `(expected False — the R107 KNOWN RED, predicted)` | 158: `(expected False — why R118 holds dist.k.vwap out)` |
| 200 | P14 THE STRATEGY-NOTE ORDER read (`ls` of `4 - Strategies`, `<last note>`) | removed. It served only R107's one-failure argument; `rows.md` in `10` still stages the `ls` |
| 334 | `## STEP-6 — HIS FIVE ROWS … (R107)` | 359: `## STEP-6 — HIS FOUR ROWS … (R118: expected GREEN)` |
| 336 | HIS RULINGS: R107 paragraph (`ALL THREE R119 rows … RED on vwap-continuation`) | 361: R107 paragraph replaced by R118 paragraph (his words, four keys named, no `dist.k.vwap` row, pin stays, GREEN, R107 superseded) |
| 338 | 6.1 BEFORE parser: `the five keys read hole` | 363: `the four keys read hole, dist.k.vwap reads hole and leg.min_size_atr reads hole` |
| 339–383 | 6.2 rows file with the `dist.k.vwap` block (5 rows); cites `:393-418` | 365–400: 4 rows, `dist.k.vwap` block deleted; cites `:393-409` |
| 386 | 6.4 `EXACTLY the five rows` | 403: `EXACTLY the four rows` |
| 388 | 6.6 `the five keys … values 0.05, 0.05, 0.5, 1, 0.1` | 405: `the four keys … 0.05, 0.05, 1, 0.1; dist.k.vwap reads hole` |
| 390 | 6.8 heading `his R107` | 407: `his R118: EXPECTED GREEN` |
| 394 | 6.8 EXPECTED: one failure `assert forms` on `'vwap-continuation'`, `1 failed, 130 passed`, three AWAITING lines | 411: `0 failed`, `0 errors`, FOUR AWAITING lines (the second-chance pin lifts, the vwap-continuation pin holds) |
| 395 | WHY ONE FAILURE PROVES … (note-order argument) | removed |
| 396 | RECORD `R119 live-note: RED (expected, R107)` under `## KNOWN RED` | 412: `R119 live-note: GREEN — <summary>` |
| 397 | ANY OTHER RED … UNEXPECTED GREEN … | 413: ANY RED → STEP-5 with (2c); "There is NO known red on this run (R118 supersedes R107)" |
| 398 | 6.9 `5 rows (R119 ×3 + R82 ×2)` | 414: `4 rows (R119 ×2 + R82 ×2; dist.k.vwap held, R118)` |
| 404 | STEP-7 3 `## KNOWN RED` paragraph | removed; STEP-7 3 (`## ESCALATE`) gains `dist.k.vwap held for his VWAP Continuation sitting (R118)` (420) |
| 410 | stop line `R119: <WRITTEN 5 rows…> · R119 live-note: <RED (expected, R107)|NOT RUN|UNEXPECTED GREEN>` | 425: `R119: <WRITTEN 4 rows|NOT WRITTEN> · R119 live-note: <GREEN|NOT RUN>` |
Kept on purpose: 2.3 (d)'s `EXACTLY these five AWAITING lines` (254). That is the pre-STEP-6 pin set, not a row count, and both pins hold before STEP-6. `grep -c "five" 09` = 1, and it is that line. The only `R107` strings left in `09` say it is superseded (56, 361, 413).

## MOVER CARRIES
| `07` ESC | carry | how it landed in `09` |
|---|---|---|
| 5 RESTARTS | aset + radar by static import reach of `cobalt.replay.*` | L66 SHAPE paragraph names both and cites `07` `## RESTARTS` (≈34). 2.5's prediction gains `07`'s four replay rows plus `s2.yaml → -` (258–266). The gate stops on any other resident, any `UNCLASSIFIED` row or a non-zero exit (unchanged). 4.7 (f) re-derives on the landed classifier. The report's last line carries `restarts: com.cobalt.aset com.cobalt.radar` |
| 1 first S2 smoke on a post-deploy night | a pre-deploy job row lacks `archive_partial_by_side`: K9.8 / K9.11 FAIL, K9.9 / K9.12 ERROR | `05` ran no `cobalt smoke s2`, so `68`'s line 270 rule is copied and amended in STEP-4.7 as `NOT RUN HERE: cobalt smoke s2 …` (338). Its S2 verdict is read tonight after the 21:10 replay by the desk, never on a pre-deploy row. It is carried to `## ESCALATE` (338, 420) and the stop line (`S2 smoke: owed after 21:10`, 425). `cobalt smoke s2` is also named in the SEAT's NO-list (1). New markers show the mover landed without running the smoke: `archive_partial_by_side` 0 → ≥1 and `id: K17` 1 → 0 (P14 209, 4.7 (d) 334; drafter's read: main 0 / branch 3; main `s2.yaml` has `id: K17`, the branch drops it at line 507) |
| 2 the shared test file | `tests/cobalt/test_replay_runner.py`: setups 418 / 472, mover appends at the end (`@@ -894,3 +894,110 @@`); `cards/stale-score-0922` not shipping | WHAT SHIPS names the seam and its hunks (19). 1.3 makes ONE named merge: exit 0 with `Auto-merging tests/cobalt/test_replay_runner.py` + `Merge made by the 'ort' strategy.`; a `CONFLICT` or non-zero exit → `merge --abort`, `status`, `FAILED: 1.3 — conflict …` naming the paths (227–229). Then `status --short` clean, `git diff --check <mover tip> HEAD -- tests/cobalt/test_replay_runner.py` empty (231), that file's diff = exactly setups' two pairs, and both sides' identity diffs empty (230–235). The parents are proved to be the two branches, and the stack totals `81 files changed` (74 + 8 − 1) (236–237). STEP-2 proves the seam (L68). stale-score is out of scope (L68 SCOPE), named in ESCALATE (420). Drafter's reads: the two branches' non-docs paths intersect ONLY in that file, and all paths including docs intersect only there too (`comm -12` of both name lists) |

## RULE STRINGS
`comm -23 <09's sorted allow+deny "Bash(…)" strings> <66's line 6 sorted>` (the part only in `09`) → **empty**. `comm -13` (only in `66`) → exactly the three dropped strings: `"Bash(git -C /Users/cobalt/cobalt-wt/s2-smoke-fix rebase --abort)"`, `"Bash(git -C /Users/cobalt/cobalt-wt/s2-smoke-fix rebase main)"`, `"Bash(git -C /Users/cobalt/cobalt-wt/stacked-0923 merge --no-edit s2/smoke-fix-0922)"`. Counts: `66` 55 `Bash(` strings (54 allows + the push deny), `09` 52 (51 + the same deny). `09` = `05`'s 50 + `stacked-0923 merge --no-edit main` (in `66`, dropped by `05`, approved in 09-23 R52 "the three `stacked-0923` `merge --no-edit`"). The denies and `--add-dir` pair are byte-identical to `66`'s. The mover worktree needs NO string: it is only read (`git -C * status*`, `ls *`, `tail *`), and the gate is cut on its tip by the desk. `10`: `--allowedTools … --add-dir /Users/cobalt/cobalt-wt` tail `cmp` against `06` line 11 → IDENTICAL. **New rule strings: 0.**

## FOR DEJAN
ONE list:
1. `Bash(grok *)` through 2026-09-24 23:59 ET, for `prompts/2026-09-24/10-review-setups-deploy-r2.md` (the house read of `09`, Opus 5.5 + Grok, his R95). The desk writes his word as `10`'s `R__G` row, which must name `10-review-setups-deploy-r2.md`, carry `Bash(grok *)` and `2026-09-24`, and quote his word.
Not asked, with the reason for each:
- The rows need no new approval. The four rows are a SUBSET of the five his R3 approved (R118).
- `09`'s launch line needs no new approval. Its 51 strings = R3's 50 + one string of 09-23 R52 (0 new). His R12 / R13 say a ruling is never re-asked. If the desk wants his word on this exact combination anyway, it is one line in this list (ESCALATE 3).
- The window is unchanged: R83 (DAY < 19:55 / PAUSE 20:00–20:20), on his `DONE TRADING <hh:mm>` word.
Nothing makes `09` NOT LAUNCHABLE.

## ESCALATE
1. ASK DESK: THE GATE CUT. `09`'s bare command (1) is `git -C /Users/cobalt/cobalt-wt/stacked-0923 checkout -B deploy/stacked-0923 replay/mover-partial-0924`, on the mover tip, NOT on `main`.
   - Why: `66`'s pool has no `stacked-0923 merge --no-edit replay/mover-partial-0924` string. Cutting on `main` would need that new string, and `09` would be NOT LAUNCHABLE until his word.
   - Cut on the mover tip, the hub's one sibling merge (`merge --no-edit setups/seven-0921`, approved) makes a real two-parent merge. This is the state `66`'s own first merge reached by fast-forward.
   - Everything downstream holds: main merged INTO the gate, parent 2 = production, one `-m 2` revert. P12 fails the run if the gate is not at the mover tip (a cut on `main`, or `4e4577c3`). 1.3 fails a fast-forward.
   - Safe default: the mover-tip cut, 0 new strings. The alternative: cut on `main` plus the one new string, brought to him. [2026-09-24 07:1x ET]
2. A `05` DEFECT THAT `06` DID NOT CATCH, FIXED IN `09`: `main` moved non-docs after `05` was drafted.
   - `c212645f` `chore(generated): nightly rewrite 2026-09-23` committed `configs/cobalt/rules.yaml`. `git diff --stat 797fdd2f main -- . ':(exclude)docs'` printed 11 files, not `05`'s 10.
   - `05` 1.2's identity diff excluded only the 10 smoke paths. After the rebase it would have printed `rules.yaml` and FAILED a good deploy at 1.2.
   - `09` excludes `rules.yaml` at 1.2 (222) and pins main's 11 paths at P11 (187). Any further non-docs commit on `main` before launch → `FAILED PREFLIGHT` naming it. The desk's own nightly-rewrite commit is the likely cause, so hold it until the stop line (DESK LINE).
3. ASK DESK: the launch-line approval is AUTHORIZATION = R3 (0924) + R52 (0923), both his rows, both committed, checked by grep and `-S`. No new approval was asked (R12 / R13). Safe default: it stands. Otherwise add `09`'s line to his ONE list.
4. `10`'s packet: `09` 110 KB (four parts) + `05` 94 KB + `66` 82 KB + `06`'s report + this report. That is ≈330 KB of sources, close to `06`'s 286 KB, and on it Grok used 16½ of its 20 minutes. `68` / `68-outcome` are dropped from the packet to compensate. A Grok TIMEOUT fails `10` (L67 floor), and the desk re-issues with a smaller packet.
5. Additions beyond the eight folds, each the smallest text, named so `10` can check them:
   - 6.5 re-runs once on a relaunch after 6.4 reads "already there". `<t write>` is recorded for fold 8.
   - STEP-5 (2)'s "other revert error" branch is adapted to ONE `-m 2` revert: HEAD still `<stack-final>` → NEW code kept (`66`'s label); otherwise → partial, residents DOWN, named.
   - RELAUNCH (ii) is adapted to one revert commit.
   - 6.3 guards that its diff paths lie under `~/dev-vault-cobalt` (`06` ESC 1).
   - P14 reads `com.cobalt.replay`'s state with R113's context.
6. `05`'s 4.7 (b) PAUSE idle clause is kept verbatim. `06` row 2 found that the radar logs `radar cycle: paused_market_reset` in the pause, so the clause is conservative, not wrong. Fold 8's 6.7 radar-cycle rule applies the same provision.
7. The mover build's other ESCALATE rows are carried as READINGS into `09` STEP-7 3: ESC 3 (three test pins amended beyond T1–T7, answered by the desk R11 and read by `08`) and ESC 4 (cosmetic ×2). Its check `08` has ESCALATE 9, not re-read here.

SETUPS DEPLOY R2 DRAFTED · branches: 2 · folds: 8 · rows: 4 · known red: none · new rule strings: 0 · window: DONE TRADING · restarts: com.cobalt.aset com.cobalt.radar · ESCALATE: 7
