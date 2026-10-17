# draft-gemini-builder-row-check — 2026-10-17

## §0 Headline
Wrote the check card `prompts/2026-10-16/687-gemini-builder-row-check-card.md` for `ops/gemini-builder-row-1017`: BASE `7f415a4f`, TIP `7b986738`, head `7b22e411` (adds only the report; `git diff --stat 7b986738 7b22e411 -- . ":(exclude)docs"` printed nothing).
Rows S0, L1, G2, H1, X2, R1, M1 (583 merge shape), R3, G3; BAND HIGH, HOUSE A grok, HOUSE B as needed.
Reads only; nothing run, committed or launched. 2 decisions for the desk.

## DECISIONS
- ASK DESK: row M1 and the x1-canary `ls -la` in row X2 use `git merge-base`, `git diff -U0` and `ls -la /Users/cobalt/cobalt-wt/x1-canary`; I could not tell whether the check seat's allow line carries them. Default: M1 falls back to `git diff --stat` only; X2 reads the decoys from the build report's `## PREFLIGHT`. [09:25]
- ASK DESK: card 583's branch has moved (head `4b62c2fa`, FR-9) since card 671's AMENDED 2 overlap record; the card tells the check to re-run the stat, not trust the numbers. If 583 changes again before the check launches, the M1 figures in the card's `## RECORDS` are stale by design. Default: leave as written. [09:25]

## RECORDS
- Drafted Sat Oct 17 09:21–09:25 EDT 2026; `main` HEAD `00edfacb`. Read: prompt 686, cards 677 and 671, CARD.md, the build report, `reports/cto-2026-10-17.md` R1752 (line 25).
- `git log --oneline ops/gemini-builder-row-1017 -5`: `7b22e411`, `7b986738`, `14a17ab7`, `7f415a4f`, `3f037e70`. `git diff --stat 7f415a4f 7b986738`: 6 files, 169 insertions, 18 deletions. `git diff --stat 7f415a4f main -- ops tests SHADOW-HUB.md` printed nothing.
- Tip lines were read on the worktree copy with Grep (the worktree's `ops`/`tests` equal the tip: `git diff --stat 7b986738 -- ops tests` printed nothing), because `git show … | grep` is refused by the one-bare-command hook (not a failure). The card tells the check to re-prove each on `git show`.
- Card 583 overlap vs merge-base `f2ca3e1a` (09:20): `SHADOW-HUB.md | 15`, `bare-guard.py | 5`, `desk-launch.sh | 80`, 3 files, 90 insertions, 10 deletions.
- The card carries the sentence telling the checker to quote any refusal as a finding (WHY paragraph). The build's DECISION R1 (four grep lines) is row R1 and ask X6.
- Card 670 files are fenced in `## NOT IN THIS JOB`. Commit nothing; no launch.

DRAFTED · decisions: 2
