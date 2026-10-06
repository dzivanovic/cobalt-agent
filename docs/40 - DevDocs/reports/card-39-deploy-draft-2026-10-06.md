# Card 39 deploy card — draft report, 2026-10-06

## §0 Headline
- The card is written: `prompts/2026-10-06/45-deploy-card-39-card.md`, one row, code tip `edd4d584`, branch head `38e0d47e`, no `«FILL` token (count 0).
- The launcher accepts the row: the SHIPS cell carries `held unfixed: 1` and `ready: NO`, and the fix-round path (`fixed_ok`) passes. No new command.
- `TIP` is `38e0d47e`, not `edd4d584` as the prompt said: the launcher needs the branch head in `TIP`. 2 decisions.

## CARD
- JOB `deploy-drc-d5-o1-b2-1006` · LADDER `OFF-LADDER — cto-2026-10-03.md R326` · BRANCH `deploy/deploy-drc-d5-o1-b2-1006` · WORKTREE `deploy-drc-d5-o1-b2-1006` · BASE `main` · TIP `38e0d47e`
- REPORT `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-drc-d5-o1-b2-1006.md` · TAG `deploy-2026-10-06-drc-d5-o1-b2` · MIGRATIONS `none` · SET `none`
- RULINGS `2026-10-03 R326, 2026-10-05 R412, 2026-10-05 R474`
- SHIPS: card 39, `ops/drc-d5-o1-b2-1006`, code tip `edd4d584`, head `38e0d47e`, check `drc-d5-o1-b2-check-2026-10-06.md`, literals `held unfixed: 1` and `ready: NO`, fix report `drc-d5-o1-b2-build-2026-10-06.md`. 13 files, 5 `src/cobalt/drc/` files → `com.cobalt.aset,com.cobalt.radar`.
- Markers (before → after): `_open_items` store.py 0→3 · `then refused` reconcile.py 0→1 · `kept = derived_day` build.py 0→1 · `def _items(rows` imports.py 0→1.
- Absent today: both `rev-parse --verify` (branch, tag) fail; `ls` fails for the worktree and the report.

## DECISIONS
1. ASK DESK: the prompt's header said `TIP: edd4d584`, but `desk-launch.sh:813-815` refuses a row whose branch head is not in `TIP` ("the branch head … is no head TIP lists"), and the branch head is `38e0d47e` (`38e0d47e` = the build report commit, docs only after `edd4d584`). I wrote `TIP: 38e0d47e` and SHIPS head `38e0d47e`, code tip `edd4d584`. Default: keep as written. [now]
2. ASK DESK: R545 is `DESK RECORD`, not a ruling row, and R390 is a law (L68), so neither is in `RULINGS` (the D5 draft dropped non-rulings the same way); R326, R412 and R474 are all committed and approved. LADDER follows the flake-fix-2 card (`OFF-LADDER — … R326`); the job card's own ladder text is `S3 — card 03`. Default: keep as written. [now]

## RECORDS
- Launcher read, `ops/desk/desk-launch.sh:790-872` at main: `ships_checked` takes the backticked literals of the SHIPS cell (col 7) and matches each against the check's last line by `*"$lit"|*"$lit "*` (`:830-837`). The check's last line carries `held unfixed: 1 ·` and `ready: NO ·`, so both pass. `ltip` = `9be877dc` is neither `ctip` nor `shead`, so `fixed_ok` (`:841-857`) runs: fix report (col 8) under `$REPORTS`, committed (`e2461938`) and unmodified, `9be877dc` an ancestor of `edd4d584` (`merge-base --is-ancestor` exit 0), last line `BUILT · … tip: edd4d584` (matches `"BUILT ·"*"tip: $ctip"*`). P3 (`:861-868`): head `38e0d47e` = `rev-parse --short=8`, `edd4d584` its ancestor, `diff --stat edd4d584 38e0d47e -- . ":(exclude)docs"` empty. D5's precedent (`d5-deploy-draft-2026-10-05.md` RECORDS) read the same way.
- Check report committed `9b8786ae`; fix report committed `e2461938`; `git status` shows neither modified.
- Branch log `-7`: `38e0d47e` (build report), `edd4d584` (O2 fix), `9be877dc` (check O1 fix), `9adba8ae`, `5084c6da`, `74f5674c`, `72868d84`. Worktree `/Users/cobalt/cobalt-wt/drc-d5-o1-b2-1006` clean at `38e0d47e`.
- Counts: before on main `grep -c -F` all 0 (4 strings); after on the worktree 3, 1, 1, 1. `store.py` after-count also read from `git show edd4d584:src/cobalt/drc/store.py` (3). The other three read in the worktree (one bare command per call; no pipe), whose `src/` equals `edd4d584`.
- Rulings on main: R326 `cto-2026-10-03.md:332` `HIS RULING · APPROVED`; R412 `cto-2026-10-05.md:109` `APPROVED (in cto-desk-contract.md …)`; R474 `:140` `HIS RULING · APPROVED`; R545 `cto-2026-10-06.md:23` `DESK RECORD`; R390 `:67`; R479 `:135` `DESK RECORD`.
- RESTARTS classes from the fix report `## RESTARTS` (`:15-34`): five `src/cobalt/drc/*` files `static import reach`, two tests, six DOCS, no `UNCLASSIFIED`.
- Carried: check `## OPEN` A1 / B1, the D5-3 question, written as a follow-up for him in the card.
- The card and this report are not committed (the desk commits).

CARD 39 DEPLOY CARD DRAFTED · decisions: 2
