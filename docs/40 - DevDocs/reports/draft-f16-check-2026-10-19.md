# draft-f16-check — report

## §0 Headline
Wrote the check card `prompts/2026-10-19/817-f16-close-check-card.md` for `s5/f16-close-1018` (rows S0, V1, V2, C1, X3, X4, X5, R2, G1).
Proven: BASE `40e646ed` is the merge-base with `main`; tip `f44c4b52`; head `be0810ce` adds only the build report and its `.result`.
The build's three `ASK DESK` items are carried as check ask X6. Nothing run, nothing committed.
Two header values are the drafter's guess: `CLASS` and `RESTARTS` (below).

## DECISIONS
1. ASK DESK: `CLASS` is not in `CARD.md` or in build card 790; I wrote `K2` (the src-and-restart cards `731-f5-card.md` and `730-f20-card.md` carry K2; the K5 cards are ops-script cards) [07:06 EDT]. Default taken: `CLASS: K2`, `INSTALL: none`. Change it if the desk classes this one otherwise.
2. ASK DESK: the card carries `RESTARTS: com.cobalt.aset com.cobalt.radar` (the build's committed-range line); card 790 named `com.cobalt.radar` only. The check re-derives it at row R2 [07:06 EDT]. Default taken: the build's line, since the tool answers (L42).
3. ASK DESK: card 790 `## RECORDS` names `e7ef198a` as `main` at drafting; the branch's BASE is `40e646ed` (the prompt's value, and the merge-base). Not a conflict for the check; named in the card's `## RECORDS` [07:06 EDT]. Default taken: `40e646ed`.

## RECORDS
- Started and ended 2026-10-19 07:06 EDT (`date`); `main` HEAD `597f8b89`.
- Proofs, each by command: `git -C /Users/cobalt/cobalt merge-base s5/f16-close-1018 main` → `40e646edf7264b21191b2b63f5fbbb2dede793c7`; `git -C /Users/cobalt/cobalt log --oneline 40e646ed..s5/f16-close-1018` → `be0810ce`, `f44c4b52`, `81efedf3`; `git -C /Users/cobalt/cobalt diff --stat f44c4b52 s5/f16-close-1018 -- . ":(exclude)docs"` → nothing; `git -C /Users/cobalt/cobalt diff --name-only --no-renames f44c4b52 s5/f16-close-1018` → the build report and its `.result`; `git -C /Users/cobalt/cobalt diff --name-only --no-renames 40e646ed f44c4b52` → five files (two DevDocs pages, `cli.py`, `loader.py`, the new test file).
- Files read: `CARD.md`, `CHECK-HUB.md`, `648-check-scratch-check-card.md`, `790-f16-close-card.md`, the build report. The prompt's `rev-parse` of a bare tip (`f44c4b52`) was not run alone after a first call without `--short` failed; the proofs above stand without it.
- Block-in-result instructions (L74): none.

DRAFTED · decisions: 3
