# recut-archive preflight round 2 2026-10-12 — card 434 `recut-archive-1012`

Read-only. Reads at `main` HEAD `aeab258f`; BASE `0990393f` (`git diff 0990393f HEAD --stat` over `ops src tests configs pyproject.toml`, `DEPLOY-HUB.md`, `CARD.md`, `deploy-aset-orphan-1010.md`, `.claude/settings.json`: empty).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff --stat -- <card>`; `git log --oneline -- <card>` | diff empty; commits `aeab258f` (amend), `6a97a036` (round-1 card) | OK |
| 2 | `grep -n -E "FILL\|^BASE:\|^TIP:\|^RESTARTS:" <card>` | no `FILL`; `BASE: 0990393f`; `TIP:` empty by design (build); `RESTARTS: none` | OK |
| 3 | card header; R1138 row | `CLASS: K5`; `RULINGS: 2026-10-12 R1138`; R1138 row `HIS RULING · APPROVED` | OK |
| 4 | `grep -c -F` of the brain's row (from "recut first archives them" to "refused both before and after.") in the card and in `433-draft-recut-archive.md` | 1 in each; `git diff 6a97a036 HEAD` shows the quote unchanged | OK |
| 5 | `git diff 6a97a036 HEAD -- <card>` | changed: A1 row (`$bt` `:1874`, `$br` `:1875`, test (a) wording, (g) in RA3, RA6 slice, RA2 (ii) order, RA7, "SEVEN tests"), `## READ` cto anchors, two `## RECORDS` bullets. Nothing else moved (`NOT IN THIS JOB`, `CHECK ASKS`, R2, `## READ` code anchors, line counts) | OK |
| 6 | round-1 checks 1-16 re-run: anchors of `desk-launch.sh`, `gate-clean.sh`, `job-clean.sh`, tests, DEPLOY-HUB, 256 report, `restarts.py`, settings line 29; `wc -l` of the seven files | no file changed since BASE; `wc -l` 2023 / 109 / 212 / 338 / 745 / 181 / 248 = the card's; the refusal `tag pre-$job exists: the deploy got that far` still `gate-clean.sh:89-90`, `.env` `:99`, lock `:100-101`; `gate-clean.sh` call `desk-launch.sh:1919` | OK |
| 7 | `grep -n -E "^recut\)\|^    ;;\|^ +bt=\|^ +br=\|^ +bw=\|gate-clean.sh" desk-launch.sh` | `recut)` `:1847`; `bw=` `:1873`, `bt=` `:1874`, `br=` `:1875`; the comment naming `gate-clean.sh` `:1917`, the call `:1919`; the arm's own `    ;;` `:1935` (`^    ;;` does not match `:1853`, `:1861`: those are indented deeper). Card `$bt` `:1874`, `$br` `:1875`, `:1917`, `:1935` right | OK |
| 8 | `git grep -n` on `HEAD:reports/cto-2026-10-12.md` for R1277-R1279, R1138, OWED deploy queue | R1279 `:10`, R1278 `:11`, R1277 `:12`, R1138 `:149`, OWED deploy queue `:156`. Card: `:9-11`, `:148`, `:155` (twice: `## READ` bullet 1, the last bullet, and `## RECORDS` AMEND). All three are one line short: right at `75c39896`, moved by the R1281-R1282 row `aeab258f` added | FAIL |
| 9 | count of tests named; each failing reason on BASE | seven: RA1-RA7, "SEVEN tests, RA1-RA7". BASE fires `gate-clean.sh:89` before `:92`, `:99`, `:100`, so RA1 exit 1 `REFUSED: tag pre-x-deploy exists`, RA2-RA3, RA7 stderr lacks `— not archived:`, RA4 the refusal is gate-clean's, RA5 refused at the pre tag, RA6 `tag "$at"` absent. Each reason stated | OK |
| 10 | RA7 (archive test (g)) and RA3 (g) (lock directory) | RA7: `date` stubbed on `PATH` printing `20261012-1930`, (i) archive tag present, (ii) archive branch present, stderr `— not archived: ` plus the name, nothing changed, RED on BASE stated. RA3 (g): `$WT/.cobalt_dev.lock/owner` = `x-gate`, `gate-clean.sh:100-101` (f is `.env` `:99`), "Both sides and RED on `BASE` as RA2" | OK |
| 11 | test (a) pinned wording; RA2 asserts | miss text starts `DEPLOYED`: `DEPLOYED: tag <name> exists` (tag case, RA2 (i)), `DEPLOYED: <report file> holds a DEPLOYED line` (report case, RA2 (ii)); RA2 After: stderr holds `… — not archived: ` and `DEPLOYED` | OK |
| 12 | RA6 slice | `recut)` `:1847` col 0 to the first line exactly four spaces + `;;` (`:1935`); nested `;;` `:1853`, `:1861` do not end it; comment lines (first non-blank `#`, e.g. `:1917`) dropped before the count; `tag -d` once, after `tag "$at"`; no `branch -D`/`-d`, `worktree remove`, `gate-clean.sh` call but step 1's | OK |
| 13 | RA2 (ii) order | `stale_256` run FIRST, then the by-hand recut (`:255-263` moves the gate, renames the branch), "so `stale_256` cannot run after it" | OK |
| 14 | `## RECORDS` for RESTARTS classes | bullet "RESTARTS classes behind `none`": `desk-launch.sh` "operator script; no Cobalt reader" (`:38`, `:230-233`), the test file "test/documentation; no resident" (`:246`), reports `DOCS` (`:225-228`); no `src/`, no resident, no restart (`src/` unchanged since BASE) | OK |

## ISSUES
- FAIL #8: fix the cto-report anchors to R1277-R1279 `:10-12`, R1138 `:149`, OWED `:156` in `## READ` bullet 1, the last `## READ` bullet and the `## RECORDS` AMEND bullet (HEAD `aeab258f`). The file grows a row every round, so cite the row ids (R1277-R1279, R1138, "OWED: deploy queue") and drop the line numbers, or re-read at the commit just before the build starts.
- NOTE: the card's BASE `0990393f` is still right for build (no `ops/ src/ tests/ configs/` change since), so the amend moves no BASE.
- NOTE: `main` carries uncommitted modified files (`.claude/settings.json`, `configs/cobalt/rules.yaml`, six docs reports, among them `cto-2026-10-08.md`) and a working-tree edit of `cto-2026-10-12.md` (one row, the desk's live OWED line); the desk settles them before the card's deploy hub starts.
- NOTE: carried from round 1: a branch named `archive` or `archive/deploy` (directory/file clash) passes `show-ref` and fails at `branch -m` after the tree is gone; the card words the `REFUSED: recut: the archive stopped at …` result, no ref is lost.

PREFLIGHT DONE · card: recut-archive-1012 · checks: 14 · fails: 1 · ready: NO
