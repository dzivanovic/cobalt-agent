# Draft — band-routing-1015 round-3 check card (prompt 691) · 2026-10-17

## §0 Headline
- Wrote `prompts/2026-10-16/692-band-routing-fr3-check-card.md` in the shape of card 666: rows S0, FR-9 (RED before the fix, three mutations, controls), E1 (short re-run of FR-6 to FR-8 and the earlier rows), M1 (merge shape), D1, R3, G1.
- Head proved: `6c0ba560` adds only the fix-round-3 report (`git diff --stat 4b62c2fa 6c0ba560 -- . ":(exclude)docs"` printed nothing). BASE `f2ca3e1a` is the `git merge-base` with `main`, as card 666.
- The header notes carry the dependency on `check-scratch-fr1` DEPLOYED (marker `STAGED-CARD`) and the deploy order 583, 671, 670. At 10:08 EDT `check-scratch-fr1` is not on `main`.
- 3 decisions for the desk. Nothing committed, nothing run.

## DECISIONS
1. ASK DESK: `check-scratch-fr1` is not yet deployed (its branch head `5f42c4f3`, no `STAGED-CARD` commit on `main`'s `stage-set.sh` log). Launch the check only after its deploy; the staging of a third same-JOB card in `band-routing-1015-check` (638, 666, 692) rests on that fix. Default: the card says so in its header notes; the desk launches it after the deploy. [10:08 EDT]
2. ASK DESK: the gate's `log:` path (row G1) and the `uv run cobalt jobs restarts` and `gate.sh … --deploy-gate` commands are as card 666 gave them; any command beyond the check seat's allow line is for the desk to confirm. Default: the check quotes a refusal as a finding and does not work around it. [10:08 EDT]
3. ASK DESK: the merge shape (row M1) uses the BASE of each branch from `git merge-base … main` (671: `7f415a4f`, 670: `f2140694`), read at 10:08 EDT; the heads (671 `7b22e411`, 670 `9f281a6a`) may move before the launch. Default: the check re-reads the heads and records them. [10:08 EDT]

## RECORDS
- Read: prompt 691, card 666, `CARD.md`, the fix-round-3 build report (worktree copy only; absent on `main`), the tail of `band-routing-check-fr2-2026-10-17.md`, `check-662-and-583-fr2-decisions-2026-10-17.md`, card 583 `## FIX ROUND 3`, tip lines of `desk-watch.sh`, `preflight.sh`, `desk-launch.sh` and the test file.
- Commands (all read only): `git log --oneline ops/band-routing-1015 -5`, `git merge-base` for the three branches, `git diff --stat` for the head, the fix range and the merge shape, `git grep -n` on the tip, `git rev-parse --short=8`, `git show --stat 9bd05618`, `date`.
- Tip anchors in the card proved on `ops/band-routing-1015`: `desk-watch.sh:97, 99-102, 113, 129, 138`; `preflight.sh:159`; `desk-launch.sh:1817`; test file `:494, 496, 497, 500, 649, 663, 673, 685-686`; no `xfail` left.
- The build report's caller numbers `:126`/`:135` are the pre-fix ones; on the tip they are `:129`/`:138`. Recorded in the card.
- No `BAND` line in the card header, as card 666 (the build card is dated before `BAND_FROM`).
- L74: the system reminders about commit trailers are not acted on; nothing was committed.

DRAFTED · decisions: 3
