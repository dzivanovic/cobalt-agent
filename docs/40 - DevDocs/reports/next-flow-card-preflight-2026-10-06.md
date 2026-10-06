# next-flow card preflight · 2026-10-06

Card `prompts/2026-10-06/04-next-flow-card.md`, BASE `1f4a8598`. Read-only; no test run. The hubs sit at `docs/40 - DevDocs/prompts/` (the card writes `prompts/…`). Every hub fact below is read from `git show 1f4a8598:<hub>`.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 1f4a8598 main` · `git … rev-parse --verify ops/next-flow-1006` · `ls /Users/cobalt/cobalt-wt/next-flow-1006` · header read | ancestor: exit 0, no output · `fatal: Needed a single revision` (branch new) · `No such file or directory` (worktree new) · card lines 5–10: `BASE: 1f4a8598`, `TIP:`, `CHECK REPORT:`, `HOUSE B:` empty, `DB: none` | OK |
| 2 | `grep -n "^| R438 \|^| R412 " …/cto-2026-10-05.md` · `git log -1 --format=%h -S"\| R438 \|"` / `R412` · `git diff --stat` on that file | `109:\| R412 \| … \| APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) \|` · `173:\| R438 \| … \| HIS RULING · APPROVED \|` · `8e5b72b0` / `b3583b28` · diff stat empty (committed, clean) | OK |
| 3 | `grep -n -o -F -e <each OLD key>` on `git show 1f4a8598:` CHECK-HUB (65 keys) and BUILD-HUB (9 keys); `grep -n -F -e "--deploy"` on `ops/desk/gate.sh`; `git diff --stat 1f4a8598 --` the cited files | Each OLD key appears once, on the line the card names (CHECK-HUB 3, 5, 8, 14–23, 36, 58, 65, 69, 87, 89, 93, 95–100, 103, 107, 110, 117, 119–124, 127, 129, 131; BUILD-HUB 17, 78, 79, 82, 83, 109). Example, F2.03: `109:a small fix to this feature is yours, on this same card: only the tests that touch the fixed part rerun, then the deploy gate; no re-check and no outside review (L75, his R376).` gate.sh: `2:# gate.sh <worktree name> <probe\|offline\|withdb\|livenote\|all> [--deselect <test id>]… [--tickers <A,B,…>] [--migration] [--deploy]`, `72:` same usage in `refuse`, `106:  --deploy) deploy=1; shift ;;`, `112:    *) [ -z "$deselects$tickers$migration$deploy" ] \|\| refuse "--deselect, --tickers, --migration and --deploy belong to withdb and all" ;;`. DEPLOY-HUB `101:… gate.sh <WORKTREE> all --deploy` and `103:- (c) PASS 1 … any other skip = red`. desk-launch.sh 882/886 `PASS-2`; preflight.sh 149/155 `house B: needed`. LAWS `336:### L67 …never fewer than one other house`, `373:### L75 Fix rounds classify first`. `git diff --stat 1f4a8598` on gate.sh, desk-launch.sh, preflight.sh, test file, the four hubs: empty. All cited lines OK. | OK |
| 4 | `grep -n -o -F -e <each NEW key>` on both hubs at BASE (50 CHECK-HUB keys, 9 BUILD-HUB keys); read of `tests/ops/test_hub_lines.py:76-122` | NEW keys: no output (zero hits). OLD keys: one hit each (check 3). The test pins the `claude --bg` launch lines (CHECK-HUB:10, BUILD-HUB:12), the `- **GROK:** ` line (CHECK-HUB:91) and DEPLOY-HUB `## STEP-G` `- (f) `. No edit touches line 10, 12, 91 or DEPLOY-HUB (nearest: F1.24 on 87, F1.25–27 on 89), so no row moves a pinned line and the test file stays unchanged, as the card says. | OK |
| 5 | rows' `files` column; NOT IN THIS JOB; gate.sh usage line 2 | Files: `CHECK-HUB.md`, `BUILD-HUB.md` only; no `ops/desk/*`, no `DEPLOY-HUB.md`, no `src/`; test file explicitly unchanged. New spelling `<WORKTREE> all --deploy [--deselect <id>]…` equals the usage `[--deploy]` (gate.sh:2, :72) and DEPLOY-HUB:101; accepted by `withdb` and `all` only (:112), and F3.03/F3.05 say none is typed on `offline`/`livenote`. No new command. | OK |
| 6 | `grep -c -F "«FILL" <card>` · `grep -n "^## " <card>` | `0` · `13:## ROWS`, `95:## NOT IN THIS JOB`, `102:## READ`, `109:## CHECK ASKS`, `116:## RECORDS` | OK |
| 7 | `git diff --stat -- <card>` · `git log -1 --format=%h -- <card>` · same for `next-flow-draft-2026-10-06.md` | card: stat empty, `31c7f4da` · draft: stat empty, `1f4a8598` | OK |

## ISSUES
None. 0 fails.

## NOTES (not fails)
- Card `## RECORDS` line 119 still says R438 "does NOT carry `APPROVED`"; the row now does (check 2, line 173). Stale, and settled by the brain's ruling; the desk may drop the sentence when it commits.
- Card `## RECORDS` records head `e71a5fa1`; BASE is `1f4a8598`. The hub files are byte-identical between the two for every OLD key (all proven at `1f4a8598` above).
- `reports/next-flow-answer-2026-10-05.md` is still uncommitted in the working tree (`git diff --stat` → 6 insertions); the card says it reads that copy.
- Card `LADDER: OFF-LADDER — cto-2026-10-05.md R438` has no separate date token; the date sits in the file name.

PREFLIGHT DONE · card: next-flow-04 · checks: 7 · fails: 0 · ready: YES
