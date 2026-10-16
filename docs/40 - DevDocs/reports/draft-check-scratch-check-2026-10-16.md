# draft-check-scratch-check — report (prompt 647)

## §0 Headline
- Wrote card 648: `prompts/2026-10-16/648-check-scratch-check-card.md`, a K5 CHECK of `ops/check-scratch-1016` (BASE `b84cca9a`, TIP `85eade55`, head `0605334f`).
- Rows: S0, CS-1 (RED on BASE's lines plus the no-prior-card-copy control), CS-2 (refusals plus five mutations), SC1 (the clear touches only `<JOB>-check`), H1, X4, R2, G1 (deploy gate).
- Reads only. No test, mutation or launch was run. Every `file:line` was proved on the worktree, which equals the tip for `ops` and `tests`.
- 2 decisions for the desk.

## DECISIONS
- ASK DESK: the build report says `clearable` has one caller at `:128`. On the tip it is `:130` (BASE's number). I wrote `:130` and told the checker to name the difference. Default: keep `:130`. [12:59]
- ASK DESK: `CARD.md` on `main` has no `BAND` row yet, so I copied `BAND: MID` from build card 641 as the prompt says. Default: keep the field. It does no harm until band-routing-1015 deploys. [12:59]

## RECORDS
- Card path: `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/648-check-scratch-check-card.md`. Its `## RECORDS` holds the full line proofs.
- Shape copied from 633 and 638. The header fields are the prompt's. G1 uses the form of 633 row G1.
- `date` Fri Oct 16 12:59:20 EDT 2026. `main` HEAD `a5466508`.
- Branch name: `git -C /Users/cobalt/cobalt-wt/check-scratch-1016 branch --show-current` → `ops/check-scratch-1016`. Worktree status clean. `git diff --stat 85eade55 ops/check-scratch-1016 -- ops tests` printed nothing.
- Tip lines proved by Read of the worktree's `stage-set.sh`: `:8`, `:50-54`, `:92-124`, `:108-114`, `:130`, `:151`, `:157-158`. Tests by Grep: `:344-440`.
- Piped `git show … | cat -n` was refused by the bare-guard, so I read the worktree copy instead. It is equal to the tip, shown by the empty diff.
- The L74 block (attribution reminder) was not acted on.

DRAFTED · decisions: 2
