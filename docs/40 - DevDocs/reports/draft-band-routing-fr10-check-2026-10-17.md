# draft-band-routing-fr10-check (prompt 702) — 2026-10-17

## §0 Headline
- Card `prompts/2026-10-17/703-band-routing-fr10-check-card.md` written on the shape of card 692: rows S0, FR-10, E1, M1, D1, R3, G1; CHECK ASKS X1-X7; DEPLOY PROOF gains the `shadow|routed|check)` marker.
- Branch head `2880eb0e` adds only the report and its `.result` past the BUILT tip `05654335`; BASE `f2ca3e1a` (`git merge-base`). Nothing committed, nothing run but reads.
- 2 decisions.

## DECISIONS
1. ASK DESK: the card asks the checker to re-prove every `file:line` by `git show ops/band-routing-1015:<file>`, but `bare-guard.py` refused my `git show … | grep` (one bare command per call), so I proved the lines on the worktree copy (docs-only difference to the tip). Is a bare `git show` of a whole file acceptable to the checker, or should the card name `Read` of the worktree copy? [14:35 EDT] Default: the card as written (checker uses `git show` bare, then the worktree copy).
2. ASK DESK: row G1 (`gate.sh … offline --deploy-gate`) and the `uv run pytest` / `uv run cobalt jobs restarts` commands are beyond my allow line; they are copied from card 692 and not tried. Confirm the check seat's allow line carries them. [14:35 EDT] Default: as card 692 (G1 stays; if refused, the checker quotes the refusal as a finding).

## RECORDS
- `git -C /Users/cobalt/cobalt log --oneline ops/band-routing-1015 -5` → `2880eb0e`, `05654335`, `630542a7`, `061f6d6f`, `3f399b60`. `git diff --name-only 05654335 2880eb0e` → the fr10 report and its `.result` only. `git merge-base ops/band-routing-1015 main` → `f2ca3e1a…`.
- Build report found in the worktree only; stop line `BUILT · … tip: 05654335 … offline 8442/0 … decisions: 0 · for Dejan: 0`; `## DECISIONS` none.
- Merge-shape stats and BASEs of 671 (`7f415a4f`) and 670 (`f2140694`) read with `git diff --stat`, as in the card's RECORDS.
- Not proved by me: `check-scratch-fr1` DEPLOYED (taken from the prompt); no test run, no mutation tried.
- `date` → Sat Oct 17 14:35:15 EDT 2026; `main` HEAD `1027bfb4`.

DRAFTED · decisions: 2
