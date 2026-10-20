## §0 Headline
Card 731 amended in place for the preflight's 3 fails and 1 note; nothing committed.
FAIL 15: the two `uv run pytest` lines are gone from `## DEPLOY PROOF`; markers for 0715 (already there), 0745, 0815, 0845 in `grep -c -F … · before `0` · after `1`` form.
FAIL 16: header, RECORDS RESTARTS line and PORT (7) read `com.cobalt.aset com.cobalt.cos com.cobalt.radar`.
FAIL 17: PORT (3), (4), DONE WHEN now use `git show 3c96ad2e:<file>` and the Grep tool; no other non-admitted builder command found. NOTE: CHECK ASKS marked SUPERSEDED by PORT (fr2).

## DECISIONS
1. ASK DESK: the `-0715` marker line already existed, so I added three new lines, not four; the four plists are all covered. Default: keep as is. [06:41]
2. ASK DESK: the text `git grep` stays in K0 (not run, "K0 is re-proved by PORT (0)"), PORT1 and FIX2 (NOT REBUILT context rows) and in dated RECORDS; I did not rewrite history. Default: leave. [06:41]
3. ASK DESK: CHECK ASKS :82 (Genesis "lower number 0026") is stale too but was not named; left. Default: leave. [06:41]

## RECORDS
- Tue Oct 20 06:41 EDT 2026 (`date`). Read: prompt 905; card 731 whole; `reports/f5-port2-preflight-2026-10-20.md` `## ISSUES` and rows 15-17; `reports/f5-checkpoints-fr1-check-2026-10-20.md` (grep of `RESTARTS`, `O2`: `:6,92,113,120,174,186`); `ops/desk/deploy-smoke.sh` `:1-180` (`shape()` and the marker/smoke row forms); `prompts/BUILD-HUB.md:14` (BUILD allow list).
- Admitted per `BUILD-HUB.md:14`: `git diff`, `git show`, `git log`, `ls`, `uv run pytest`, `uv run cobalt jobs restarts`, Read/Grep/Glob, Edit in the worktree, `sh ops/desk/*`. PORT's other commands (`git -C /Users/cobalt/cobalt diff --name-only`, `git diff -M`, `git diff --stat`, `git log --merges`, `ls`) all fit.
- Not run: `git show HEAD:<file>` proofs were not needed (no new file:line was added); not traced: none.

DRAFTED · decisions: 3
