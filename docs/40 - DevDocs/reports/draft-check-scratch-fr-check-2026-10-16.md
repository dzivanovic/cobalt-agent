# draft-check-scratch-fr-check — prompt 661

## §0 Headline
- Card 662 written: `prompts/2026-10-16/662-check-scratch-fr-check-card.md`, a CHECK of FR-1 and FR-2 on tip `dd4d968d` (BASE `b84cca9a`), header in the shape of 648, rows S0, GD, FR-1, FR-2, SC1, LIVE, H1, X4, R2, G1.
- One blocker for the live proof: the first check's report `check-scratch-check-2026-10-16.md` is untracked, so the staging would refuse at `stage-set.sh:144`. Commit it before the launch (ASK DESK 1).
- Every `file:line` read on the tip's code (head `a7fe4110` adds docs only). No test run, no mutation tried.

## DECISIONS
1. ASK DESK: commit `reports/check-scratch-check-2026-10-16.md` (and its `.result`) to `main` before launching check 662. `git ls-tree main` and `git log main` print nothing for it; `git status` shows `??`. The prior check card in the live folder is `648`, whose `CHECK REPORT` is that file; `clearable()` refuses a prior report not on `main` (`:144`), so row LIVE would fail for a reason that is not FR-1's. [14:36 EDT] Default taken: the card says so in `## RECORDS` and asks the checker to quote any refusal as a finding; nothing committed here.
2. ASK DESK: the G1 log path (`gate.sh … --deploy-gate` prints a `log:` path), as in card 648 row G1. [14:36 EDT] Default taken: the checker quotes the path as printed, no further command.

## RECORDS
- Drafter `draft-check-scratch-fr-check`, 2026-10-16 14:36 EDT (`date`), `main` HEAD `47e4bfc4`. Read: `prompts/CARD.md`, cards 648 and 638, the build report whole, `ops/desk/stage-set.sh` whole and `tests/ops/test_stage_set.py` `:70-100`, `:440-536` at the worktree (equal to the tip: `git diff --stat dd4d968d a7fe4110 -- ops tests` printed nothing), card 641 `## CONTINUE FIX ROUND`, rows, `## NOT IN THIS JOB`, `## CHECK ASKS`, the first check's `## OPEN`, `reports/cto-2026-10-16.md` R1706-R1723.
- Branch found by `git -C /Users/cobalt/cobalt-wt/check-scratch-1016 branch --show-current` → `ops/check-scratch-1016`.
- Live folder `ls`: `633-`, `638-`, `641-`, `648-…-card.md`, a band-routing report, the build report, `wt`. By header: `648` is the one check card of this JOB; the staged `648` blob `8b5a1281…` equals `main`'s.
- `grep` for `«FILL` in card 662: none.
- Drafter's sum, not a quote: FR-1's previous-tip run is `2 failed, 30 passed` (the builder's `29 passed` predates FR-2's test).
- The prompt's `:115` is `:137` on the tip (FR-1 added 22 lines above it); the card names `:137`.

DRAFTED · decisions: 2
