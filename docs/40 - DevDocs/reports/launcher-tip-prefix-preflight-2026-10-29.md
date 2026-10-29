# Launcher-tip-prefix card 1085 — preflight (read-only)

Subject: `prompts/2026-10-29/1085-launcher-tip-prefix-card.md`. Main tip read: `46cbbb7c` (`git -C /Users/cobalt/cobalt rev-parse --short=8 main`; the card's records say `c29d13e9`, two docs commits earlier). `git diff --stat main -- ops/desk tests/ops` prints nothing, so the working tree equals main there.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | Read card against `CARD.md` build header | JOB, LADDER, BRANCH, WORKTREE, BASE (FILL), TIP (empty), REPORT, CHECK REPORT (empty), HOUSE B (empty), DB none, BAND HIGH (card dated 2026-10-29), RULINGS present. `## ROWS`, `## NOT IN THIS JOB`, `## READ`, `## DEPLOY PROOF` (marker lines with `· before`/`· after` plus a smoke read), `## RECORDS` present; headings are bare lines in the right order | OK |
| 2 | Read THE RULE and rows T1/A1/A2 | Rule = literal `… tip: <TIP>`, then end, a space, or `[0-9a-f]` up to the next space/end. Refused: other 8-hex prefix (T1 b), `z` and `9z` tails (T1 c), shorter tip (T1 d), other job and `x-jobber` (unchanged cases). The POSIX `sh` shape (`${last#…}`, `${rest%% *}`, `case *[!0-9a-f]*`) needs the starts-with guard, which the card states. Nothing looser | OK |
| 3 | Flipping tests, `git grep` and Read of the test files | `test_desk_launch_prechecks.py:342` is `"BUILT · job: x-job · tip: TIP9 | on x"`: it flips, and the card gives `TIPz`. `:411` `("tip9", False)` and `:420` are as cited, and `("tipz", False)` is named. `test_preflight.py:462` is the `{tip}9` row with `True`, and the card names the new expectation. Names, `:331-359`, `:391`, `:408-430`, `:103`, `:141`, `:443` and `:53` (`OTHER_TIP`) all true | OK |
| 4 | Red-green in the card | (a) 9-hex line refused on BASE (`assert 1 == 0`) and admitted after; (b) `OTHER_TIP`, (c) `z`/`9z` and (d) `[:7]` GREEN on both sides. SHADOW `tip9` is red then green; `tipz` is green on both sides. A2 `test_1085_a2_…` is red with last line `FAILED PREFLIGHT: report`; the `{tip}z` row is green on both sides. Test names carry `1085`, so the `-k` filters and DEPLOY PROOF counts fit | OK |
| 5 | `git -C … grep -n -F "BUILT · job" main -- ops/desk/desk-launch.sh ops/desk/preflight.sh` | `desk-launch.sh:2133` (BUILT arm) and `:2134` (SHADOW arm); `preflight.sh:273` (BUILT glob with `self-check:`) and `:285` (SHADOW arm). All four as cited | OK |
| 6 | `git grep -n -F "not built" main -- ops/desk/desk-launch.sh` | `:2130` (no build report), `:2135` (shadow arm with `[ -n "$shadow" ] \|\| refuse`), `:2136` (`*) refuse`). As cited | OK |
| 7 | `git grep -n -F "hex8 TIP" main -- ops/desk/desk-launch.sh` | `:2091` (`hex8 TIP "$tip"`) and `:2209`. As cited | OK |
| 8 | `git grep -n -F "tip: " main -- ops/desk/desk-launch.sh` | `:1523-1524` and `:1810` are `"BUILT ·"*"tip: $x"*` globs, as the card says; no other site compares a stop-line tip to the card TIP | OK |
| 9 | `git grep -n -F "short=8" main -- ops/desk/desk-launch.sh` | The deploy `.result` read shortens with `--short=8` at `:1774` (and the fix-report read at `:1805`). The card cites `:1773`; the claim is true, the line is off by one | OK (NOTE 1) |
| 10 | `git grep -n -F "BUILT ·" main -- ops/desk/deploy-step0.sh ops/desk/deploy-card.sh` | `deploy-card.sh:264` and `deploy-step0.sh:783` are fix-report globs (also `deploy-step0.sh:275`, `deploy-card.sh:536-539`); not the build stop-line compare. As cited | OK |
| 11 | `ls -l /Users/cobalt/.claude/ops/desk-launch.sh /Users/cobalt/.claude/ops/preflight.sh` | Both are symlinks into `/Users/cobalt/cobalt/ops/desk/`. The edited files are the tracked `ops/desk/` sources; `desk-launch.sh:1093-1119` `install-ops` links by name (`install-ops: <n> linked, <r> replaced, <m> kept`), so the card's `0 linked` is the right shape | OK |
| 12 | BUILD line (`BUILD-HUB.md:14`) against every builder command in the card | Builder commands are `uv run pytest -q -p no:cacheprovider --color=no …` (`uv run pytest *`), plus Read, Edit and `git add/commit`. `install-ops`, the `grep -c -F` proofs and the smoke read are the desk's or deploy's, not the builder's. `grep -n -E "git mv\|git rm\|rm \|revert\|cherry\|mv "` on the card hits only A2's `\|` text. None of the forbidden verbs | OK |
| 13 | RESTARTS and migration | `grep -n -F "ops/desk" configs/cobalt/jobs.yaml` prints nothing, and the card has `RESTARTS: none`, `MIGRATIONS: none`, `DB: none`. This matches an ops script (L42, card 580): `install-ops` after DEPLOYED. The builder's `jobs restarts` table is the proof. All files sit under `ops/` and `tests/ops/`, so (a0) holds | OK |
| 14 | K5 allow-line and guard widening | The card edits two stop-line compares and tests only. It touches no allow string, no `--allowedTools`, no hook and no `bare-guard.py`. Admitted tails are hex-only | OK |
| 15 | One seam, dependencies | The only job is the 9-hex tip compare in two tracked files. Neither 1082 nor 1081 is named as an input in the card; `:273` tightening is fenced to `## DECISIONS`. No dependency | OK |

## OPEN FILLS
- `BASE` is `«FILL: 8-hex main commit the branch is cut from»`. The desk fills it with a main commit at or after `46cbbb7c`.
- `TIP`, `CHECK REPORT` and `HOUSE B` are empty, as for a build card (they are set before the check).
- The card has no `RULINGS` `«FILL»`; `2026-10-29 R2571` is set.

## ISSUES
- NOTE 1: the card cites the deploy `.result` `--short=8` read at `desk-launch.sh:1773`; on main `46cbbb7c` it is `:1774`. The claim is true and nothing changes there.
- NOTE 2: the card's RECORDS say HEAD `c29d13e9`; main is now `46cbbb7c` (docs commits only, `ops/desk` and `tests/ops` unchanged). Every cited `file:line` still holds.
- NOTE 3: the A1 comment `card 1085` on two arms plus the deploy-proof counts (≥1, ≥1, ≥4, ≥1) are consistent with the rows: four new `test_1085_t1_*` names (a, b, c, d) in the prechecks file and one `test_1085_a2_*` in the preflight file.
- Blocks the launch: nothing but the desk's `BASE` fill.

PREFLIGHT DONE · cards: 1085 · checks: 15 · fails: 0 · ready: YES
