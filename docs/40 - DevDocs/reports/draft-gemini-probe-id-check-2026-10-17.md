# draft-gemini-probe-id-check — 2026-10-17

## §0 Headline
Card 677 written: `prompts/2026-10-16/677-gemini-probe-id-check-card.md`, a check of `ops/gemini-probe-id-1017` (tip `744128d7`, base `f2140694`), shape of card 666.
Rows S0, G1 (RUN, RED on `5bce12c9`, four mutations, control), G2 (leftover old-id list), P1 (both desk records), D1, R3, G3 (deploy gate). Every tip `file:line` proved on the worktree copy; none run.
Two desk records quoted whole in `## RECORDS`.

## DECISIONS
1. ASK DESK: the prompt says BASE and TIP "stay the desk's"; I wrote `BASE: f2140694` and `TIP: 744128d7` (the prompt's own values) so the card has no `«FILL`. Default: kept; the desk may overwrite [Sat Oct 17 08:55 EDT].
2. ASK DESK: `gate.sh gemini-probe-id-1017 offline --deploy-gate` (row G3) and the `log:` path are the desk's allow line, not mine [Sat Oct 17 08:55 EDT]. Default: as card 666 row G1.
3. ASK DESK: `git grep` on the branch is not on my allow line; I proved the old-id occurrences by `grep` on the worktree copy (clean, at the head `9f281a6a`) [Sat Oct 17 08:55 EDT]. Default: the check re-runs it on the tip.

## RECORDS
- Drafted Sat Oct 17 08:55 EDT 2026; `main` HEAD `03da61af`. Reads only: `git show`/`log`/`diff`/`rev-parse`, `grep` and `Read`.
- `git log --oneline -5 ops/gemini-probe-id-1017`: `9f281a6a`, `744128d7`, `5bce12c9`, `f2140694`, `5b933294`. `git diff --stat f2140694 744128d7`: 4 files, 19 insertions, 5 deletions. `git diff --stat 744128d7 9f281a6a -- . ":(exclude)docs"`: nothing.
- Tip lines (worktree `grep -n -F`): `house-probe.sh:24`, `:104`; `CHECK-HUB.md:95`; `STANDING-LIST.md:13`; `test_house_probe.py:253`, `:284`, `:289`, `:292`, `:294`.
- Old id left on the tip: `SHADOW-HUB.md:88`, `test_desk_launch_shadow.py:216-217` (card 671), `test_house_probe.py:294` (the pin's negative string). `desk-launch.sh:398` is the glob `gemini-*`: no old id.
- The two desk records (`agy models` 08:03:45; worktree probe `gemini: UP` 08:52) are copied whole into the card's `## RECORDS`.
- Build report read: stop line, `## DECISIONS` (3), `## RECORDS`.

DRAFTED · decisions: 3
