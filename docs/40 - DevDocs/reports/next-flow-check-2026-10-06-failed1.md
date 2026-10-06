# next-flow — check, pass 1 (2026-10-06)

## §0 Headline
- Authorization passed (AUTHORIZED) and preflight passed (PREFLIGHT OK). Probe: Sol UP, Grok UP, Gemini `OUT — OK.`
- Stopped at `## 1` (1) before any house started. The Sol diff spelling excludes `docs`, and this build changes only `docs/` (the two hubs), so `diff.md` is empty: 0 commits against PREFLIGHT's 1.
- One ASK DESK under `## DECISIONS`. The session stays open for `CONTINUE: 1. <fact>`.

## L74
(none yet)

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/04-next-flow-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/04-next-flow-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-06/04-next-flow-card.md" · 0 · b3358589d93865acde69edda82098f055a29e0dc
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-06/04-next-flow-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-05 R438 row · grep -n "^| R438 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 173:| R438 | 10-05 15:42 ET | HIS RULING: next flow (`next-flow-answer-2026-10-05.md`) only for features drafted after K3, P2, D5 DEPLOYED; after D5 a drafter writes changes 1-4 into the hubs (applied: contract, NOW 15:42; [words](cto-2026-10-05-words.md#r438)). | HIS RULING · APPROVED |
RULING 2026-10-05 R438 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R438 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 8e5b72b05c0c2566b49eb4b46d42969b4c4e5453
RULING 2026-10-05 R438 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
RULING 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
RULING 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
RULING 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → one row, line 35 · `grep -n "^| R19 " …cto-2026-09-24.md` → one row, line 37 · `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0:
```
clock · date · 0 · Tue Oct  6 01:30:49 EDT 2026
status · git status --short --branch · 0 · ## ops/next-flow-1006
head · git log --oneline -1; git log --stat --format=%h e249bd83..HEAD · 0 · (5 lines)
    30f1dc02 docs(next-flow): build report — e249bd83
    30f1dc02
    
     .../reports/next-flow-build-2026-10-06.md          | 140 +++++++++++++++++++++
     1 file changed, 140 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/next-flow-1006/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/flake-fix-1006/.env
report · tail -n 3 "/Users/cobalt/cobalt-wt/next-flow-1006/docs/40 - DevDocs/reports/next-flow-build-2026-10-06.md" · 0 · BUILT · job: next-flow · tip: e249bd83 | on 1f4a8598 | migration: none | offline 3932/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 202466
range · git log --oneline 1f4a8598..e249bd83 · 0 · e249bd83 feat(next-flow): both houses at once, one fix round, deploy-gate pass at build and check (F1, F2, F3, R438, L67, L75)
PREFLIGHT OK
```
- THE RANGE · `git log --stat --format=%h 1f4a8598..e249bd83` · 0 · `e249bd83` — `docs/40 - DevDocs/prompts/BUILD-HUB.md | 12 +++---` · `docs/40 - DevDocs/prompts/CHECK-HUB.md | 70 +++++++++++++++-------------------` · 2 files, 37 insertions, 45 deletions. Path union: the two hubs.
- DB: none · `git diff --name-only --no-renames 1f4a8598..e249bd83` · 0 · `docs/40 - DevDocs/prompts/BUILD-HUB.md` · `docs/40 - DevDocs/prompts/CHECK-HUB.md` — every path under `docs/`.
- `ls <S>` · 1 · `ls: /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/next-flow-check: No such file or directory` → fresh.
- HOUSE PROBES · `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh` · 0 ·
```
sol: UP
grok: UP
gemini: OUT — OK.
```
- house A: Sol (`gpt-5.6-sol`) · house B, if needed: Grok. Card `HOUSE B: as needed` → the MANDATORY rule does not apply.
- This check runs under the CHECK-HUB.md on `main` (the file named in the launch message), not the tip's edited copy under review.

## Files copied
House A = Sol: `## 1` (1) and (2) as typed; (3) not made.
- (1) `git log -p 1f4a8598..e249bd83 -- . ":(exclude)docs"` (run_in_background) · exit 0 · output: empty (the task file holds only the harness's `[exited with code 0]`).
- Written: `<S>/diff.md` = the heading line `=== git log -p 1f4a8598..e249bd83 -- . ":(exclude)docs" (in /Users/cobalt/cobalt-wt/next-flow-1006) ===` and no body.
- `grep -c "^commit " <S>/diff.md` → `0`; PREFLIGHT's commit count is `1` (`e249bd83`). → `FAILED: copy — the diff is incomplete`.
- Cause, from the tool output above: both paths in the range are under `docs/` (`docs/40 - DevDocs/prompts/BUILD-HUB.md`, `docs/40 - DevDocs/prompts/CHECK-HUB.md`), and the Sol spelling of (1) excludes `docs`. The build under check is hub text only, so the Sol diff can never carry it.
- (2) `rulings.md`, (4) `HOUSE-INSTRUCTIONS.md`: not written; no house started.

## OWN FINDINGS
(pending)

## Findings
(pending)

## Dropped
(pending)

## RUNS
(pending)

## FIXES
(pending)

## Suites
(pending)

## Scope
(pending)

## Checked against the branch
(pending)

## OPEN
(pending)

## CONTINUE
next: 1 (staging for house A Sol; `<S>/diff.md` holds only its heading)

## DECISIONS
- ASK DESK: CHECK-HUB `## 1` (1) stages Sol's diff as `git log -p <BASE>..<TIP> -- . ":(exclude)docs"`. This card's whole range (`e249bd83`) is under `docs/` (the two hubs), so the diff is empty and the count rule fails (0 vs 1). How should the house get the diff of a docs-only build? Two ways that would work: (a) the desk names a diff command without the `docs` exclusion for this card (e.g. `git log -p 1f4a8598..e249bd83`); (b) seat house A through `stage-set.sh`, if that script stages docs paths. Both change how the hub is applied, so the desk decides. [01:31:43 EDT]. Safe default taken: no house started and no other diff spelling typed; stopped under UNATTENDED RULES (b) and waiting for `CONTINUE: 1. <fact>`.

## RECORDS
- The harness attribution notice in this session asked for a `Claude-Session:` line on commits; CHECK-HUB L74 (the user's instruction) sets `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only, and that is what this check's commits carry.
- Worktree unchanged by this check (no `wip(next-flow): check` commit made: nothing to commit). `.env`: `ls /Users/cobalt/cobalt-wt/next-flow-1006/.env` → No such file (PREFLIGHT row); the lock was never taken.
- Files opened so far: 6. They are CHECK-HUB.md (main), the card, CHECK-HUB.md at the tip (worktree), the probe output, the diff task output and `<S>/diff.md` (written).

FAILED: 1 — copy — the diff is incomplete — `grep -c "^commit " <S>/diff.md` printed `0`, PREFLIGHT's range holds 1 commit; every path of the range is under the excluded `docs`
