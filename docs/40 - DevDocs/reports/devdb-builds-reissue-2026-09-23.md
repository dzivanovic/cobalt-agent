# DEV-DB BUILDS RE-ISSUE — 2026-09-23 (`45`, seat `devdb-builds-reissue-0923`, Opus 5.5)

## §0 Headline
- Four prompts written, none launched: `46` (stale score build, re-issues `31`), `47` (H1 build, re-issues `27`), `50` (check of `46`, re-issues `32`), `51` (check of `47`, re-issues `28`). `50` and `51` follow `06`'s shape.
- **46 is ready.** Its base is the setups tip once `39` adds the seam pin; the desk copies that sha from `39`'s stop line. It can't use `b007ce2e` or main: `b007ce2e` fails the ladder pin test on its own, and v2 §6 needs setups underneath.
- **47 waits for tonight's deploy.** H1 is cut from main after `41` ends `STACKED DEPLOY DONE …`, so `0014` sits directly on `0013`.
- Hub rule strings: 0 new (both `.env` pairs were already approved: R64 and R30). One new approval for him: the grok/agy extension for `50`/`51`.
- ESCALATE: 11.

## MIGRATION SEAM (L72 P-b) — the decision, settled before drafting
| number | owner | lands | status |
|---|---|---|---|
| `0013_tunables_slug_nullable` | `setups/seven-0921` | tonight, `41` (`--allow-prod`) | on the setups branch; not yet on main |
| `0014_radar_handicap` | H1 (`47`) | H1's own deploy | reserved |
| `0015_shadow_agreement_stale` | stale score (`46`), **only if X30 = (A)** | stale score's deploy | reserved; unused if (B) |
| `0016` | DRC D1 (`52` → `53`) | its deploy | reserved (for `52`'s drafter to cite) |

**Decision for H1: gate the LAUNCH on tonight's deploy stop line, then cut from main.** Main will then carry `0013`, and `0014` numbers straight after it.
- **Why it starts as soon as the alternative.** H1 can't start before `46` stops anyway: R58 says "one after the other", stale score first, one dev-DB lane. `46` takes ≈4–7 h from ~14:00, plus a lane stop while `41` runs its with-DB gate, so it should stop around 19:00–22:00. `41` has to restart by 19:55 (R5). So in the expected case, the deploy stops before the dev-DB lane frees, and the gate costs no idle time. The only case where it costs time is if `46` finishes before `41` is done.
- **Why not the alternative (build on the setups tip `b007ce2e` or the gate branch).** (1) `b007ce2e` fails the pin test on its own, so H1's BASELINE would stop red. (2) The gate branch `deploy/stacked-0923` gets re-cut by the desk before `41` runs (`41` DELTA row 2: `checkout -B … main`). (3) `41` STEP-1.1 rebases `setups/seven-0921` onto main again (`41` carries `git -C …/setups-c1 rebase main`), so every setups sha goes stale tonight. (4) H1 is off-ladder and doesn't depend on setups; stacking it would add a fake dependency for L68 at H1's deploy.
- **What it means for L68 at H1's deploy:** H1 is a plain branch off main. Its only sibling is `cards/stale-score-0922`. They share `db_migrations/__init__.py` (only if `0015` exists), `radar_panel.py` (only if X22 finds a scorer) and `tests/experiments/`. The stacked gate of whichever deploy carries both proves the seam.
- **Runner check:** `src/cobalt/db_migrations/cli.py` `_apply` re-runs every registered `FORWARD` file each time (idempotent; there is no version table). An unused `0015` breaks nothing. `_rollback_paths` compares numbers, so gaps are fine there too.

**Stale-score base (not main now, as `45` asked).** v2 §6 and derive ESC 5 say "C is built on a tree that already carries `setups/seven-0921`". Main won't carry setups until tonight. So `46` stacks on `b007ce2e` + `39`'s pin. `46`'s PREFLIGHT proves the base contains the pin and no code above `b007ce2e`.

## NEW STRINGS — his ONE approval list
1. `Bash(grok *) and Bash(agy *) through 2026-09-25 for 50 and 51` — the literal `50`/`51`'s DATE + EXTENSION GATE greps. R30 covers only through 2026-09-23, and R105 covers the DRC checks `53`–`57` only. Same sandboxed, headless, read-only use as R30.

Hub rule strings: **0 new.** `46` = `31`'s line byte for byte, and its `.env` pair is his **R64** ("Approved all", 09-22 15:08). `47` = `27`'s line byte for byte, and its `.env` pair is his **R30** ("Approved", 09-22 13:0x). `50` = `32`'s line and `51` = `28`'s line, both equal to `06`'s. I checked every string by `grep -c -F`: 23/23 each for `46` and `47`, and 18/18 each for `50` and `51` (the 13 + 3 are in `08`; the Sol and Opus strings are in `32`/`28`).

Desk commands (the desk's own; not hub strings):
- `git -C /Users/cobalt/cobalt worktree add -b cards/stale-score-0922 /Users/cobalt/cobalt-wt/stale-score <39's tip>`
- `git -C /Users/cobalt/cobalt-wt/handicap-h1 merge --ff-only main` (after `41` DONE; the worktree exists at `be4c79b5`, clean, with no commits of its own)
- a Write of `/Users/cobalt/cobalt-wt/DEVDB-HOLD`, and `rm /Users/cobalt/cobalt-wt/DEVDB-HOLD`

## 46 DELTA FROM 31
| where | change | why |
|---|---|---|
| line 1 | re-issue sentence; seat/remote `stale-score-0923`; prompt path `46`; `.env` pair stands on R64, not NEW | L19 |
| line 1 / title / PREFLIGHT | `__TIP__` → `__BASE__` = `39`'s BUILT tip; the `worktree add` string names it | seam pin; `b007ce2e` is red on its own |
| new rule | **LANE GATE** before every `cp` of `.env`: `ls -la /Users/cobalt/cobalt-wt/*/.env` has no match AND `ls /Users/cobalt/cobalt-wt/DEVDB-HOLD` finds nothing. A failure is a LANE STOP (wip, breadcrumb, pinned line), not a FAILURE. Uses only existing `ls *` | R58 one lane; `41`'s with-DB gate and DRC D1 share `cobalt_dev` |
| WHAT IS RULED | migration number settled as `0015` (was "next free") | L72 P-b |
| AUTHORIZATION | adds 09-23 R58 `"yes start both"` + committed check; launch row greps `46-…` in 09-23/24; R64's word `"Approved all"` accepted; the rest of the line greps `31` | `31`'s list lacked `"Approved all"`, the words R64 actually has, so `31`'s own gate would have failed |
| PREFLIGHT | `b007ce2e..<base>` has commits and no `src`/`configs` change; a setups re-sha by `41` is recorded, not fatal | L68 / L54 |
| STEP-2 / CLOSE | `test_radar_panel_cards.py` diff stays empty (the seam pin is never re-pointed) | R44 |
| CLOSE L68 / FOR THE DEPLOY | adds `radar/handicap-h1-0922` + DRC D1's branch; rebase-then-ff after `41`'s re-sha | L54 |
| report | `stale-score-build-2026-09-23.md`; new `## LANE`; `## FOR 32` → `## FOR 50` | — |

## 47 DELTA FROM 27
| where | change | why |
|---|---|---|
| line 1 | re-issue sentence; seat/remote `handicap-h1-0923`; path `47`; `.env` pair on R30, not NEW; **LAUNCH GATE** = `41` DONE + `46` stopped | the seam decision; R58 order |
| line 1 | the worktree is fast-forwarded (`merge --ff-only main`) instead of `worktree add` (it already exists) | the 09-22 worktree was never used |
| WHAT IS RULED | `0014` settled; a `0014` already on main → FAILED | L72 P-b |
| INDEX 4 | re-locate every `d2d82e7` cite by symbol (`evaluate.py`, `cli.py` and `__init__.py` changed tonight) → `27 cite → main line` table | line drift |
| AUTHORIZATION | adds 09-23 R58, R32; launch row `47-…`; the rest of the line greps `27`; the LAUNCH GATE is proved by `tail` of `deploy-2026-09-23-r2.md` and of `46`'s report | — |
| PREFLIGHT | `0013` in `ls` and in `FORWARD`/`REVERSE`; not still at `be4c79b5`; setups code on main; `ls tests/experiments` | seam proof |
| new | LANE GATE (as in 46); `main` means the recorded `<main tip>` sha | main moves with desk commits |
| STEP-5 | `0014` placed after `0013` in `FORWARD`, before it in `REVERSE`; "take next free" removed | L72 P-b |
| CLOSE | `test_radar_panel_cards.py` empty diff; L68 list adds `cards/stale-score-0922`, `s2/smoke-fix-0922`, DRC D1 | — |
| report | `handicap-h1-build-2026-09-23.md`; `## LANE`; `## FOR 51` | — |

## 50 DELTA FROM 32 (and 51 DELTA FROM 28)
| where | change | why |
|---|---|---|
| line 1 | path `50`/`51`, remote `…-check-0923`; build prompt `46`/`47`; round 1 of ≤3 | L19, L39 |
| DATE GATE | 09-23 → R30; 09-24/25 → only his row with `Bash(grok *) and Bash(agy *) through 2026-09-25 for 50 and 51`; R105 named as DRC-only | the new approval |
| AUTHORIZATION | adds 09-23 R58, and a desk row quoting `STALE SCORE BUILT` / `HANDICAP H1 BUILT` (L35); the rest greps `32`/`28` + `08` | `06`'s shape |
| PREFLIGHT | `06`'s BUILT-line shape (fields, branch-moved-above-tip check, boundary list); `50`: base carries the pin; `51`: `<main tip>` carries `0013`; the stagger is `06`'s (s4) launch-row literal instead of `<STAGGER REPORT>` | `06`'s shape |
| report | `…-check-2026-09-23.md`; adds `## L74` and `## FOR THE CLASSIFIER` (L75); the stop line gains `round: 1` | `06`'s shape |
| questions | `50` Q7/Q10 and `51` Q7/Q12 add `0015`/`0014` registration and the ladder pin; check rows (x) grep `__init__.py` | seam |

## ESCALATE
1. **`46` depends on `39`.** If `39` ends `FAILED` (the ladder diff is a real defect), `46` has no green base and doesn't launch. The next step is the setups fix round.
2. **Setups gets re-sha'd tonight.** `41` STEP-1.1 rebases `setups/seven-0921` onto main again, so `46`'s base becomes pre-rebase shas. The code is patch-identical, and `46`'s deploy rebases before its ff (L54). This is written into `46` FOR THE DEPLOY and `50` ESCALATE.
3. **`cobalt_dev` collision risk with `41`.** `41`'s with-DB gate (the `stacked-0923` `.env`) checks only its own `.env`, not other worktrees'. Before launching `41`, the desk must Write `/Users/cobalt/cobalt-wt/DEVDB-HOLD`. It launches `41` only once `ls -la /Users/cobalt/cobalt-wt/*/.env` shows nothing (`46`'s gate only runs before each `cp`, so a with-DB suite already in progress, ≈8 min, finishes first). It removes the hold after `41` stops. This is new desk practice and has no law weight.
4. **`31` would have failed its own AUTHORIZATION.** R64's row says `"Approved all"`, and `31` accepted only `"approved"`/`"Approved"`/`"All approved"`. `46` and `47` now accept `"Approved all"` as well; nothing else is widened.
5. **If `41` fails or doesn't land tonight, `47` stays gated.** The next lawful step is the desk's call: re-issue `47` on the re-sha'd setups tip (stacked, the alternative above), or wait for the next deploy. ASK DESK: which one, if `41` fails? [13:34]
6. **H1 worktree:** `/Users/cobalt/cobalt-wt/handicap-h1` (`radar/handicap-h1-0922` @ `be4c79b5`, 146 commits behind main, clean). The desk runs `merge --ff-only main`. If the desk prefers a fresh branch name, that's a new `worktree add` at the same path; the `.env` pair only works at that path.
7. **DRC D1 (`52`, R59) is a third dev-DB user.** Its drafter should cite `0016` from the table above and use the same LANE GATE and `DEVDB-HOLD` marker. The desk points `52` at this report.
8. **Owed before `50` launches:** the desk's production reads X9 / X25 (`50` §1a; unchanged from `32`).
9. **House lane:** `50` and `51` are both house hubs, so one at a time; the DRC checks `53`–`57` and the JEV checks share the lane. Each launch row needs the literal `no other house hub is running` on a line that names the file.
10. **Superseded, never launched:** `2026-09-22/27`, `28`, `31` and `32`. The desk marks them superseded by `47`, `51`, `46` and `50` in its launch rows.
11. **Clock vs rows:** `date` read 13:19–13:34 EDT during this run, while the desk rows R58/R59 say 13:2x/13:3x. That's recorded only; every time in this report comes from `date` (L48).

DEVDB BUILDS REISSUED · 46: ready · 47: gated on deploy · new rule strings: 1 · ESCALATE: 11
