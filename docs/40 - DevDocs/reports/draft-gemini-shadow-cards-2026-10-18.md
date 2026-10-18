# draft-gemini-shadow-cards · 2026-10-18

## §0 Headline
- Three Gemini shadow cards are drafted, none committed: 717 LOW strike-fallback-env, 718 MID radar-display-fix, 719 HIGH s4-p1. Slug `gemini`, builder `gemini-4-argon-high` only.
- ROWS are byte for byte as cards 366, 369 and 372 (`git diff --no-index --stat`: each differs only in the 7 header lines, plus the added ARM and STEP 0 lines). BASEs are as the 10-11 cards: `8f4bbe28`, `50b0cd87`, `e4586978`.
- 717 `## STEP 0` is X1: the decoys, then two agy legs (worktree cwd, then cwd `/Users/cobalt/cobalt-wt/x1-canary`). It ends with `X1 RESULT: <clean | decoy read | cwd taken in>`. 718 and 719 carry `PRECONDITION: the X1 result is a DESK RECORD row and is clean`.
- Seven decisions, each with a default. Next: the desk commits the three cards, then a Sonnet preflight runs on each.

## DECISIONS
- ASK DESK: names. JOB and WORKTREE are `<stem>-1018-gemini`, because the launcher refuses a JOB that does not end in `-gemini` (`desk-launch.sh:1740-1742`). BRANCH is `shadow/<stem>-1018-gemini-4-argon-high`, as prompt 716 sets it, so the worktree name is not the branch tail. Default: as drafted. All three branch names are unused (`rev-parse --verify` exit 1), and no such worktree exists. [06:23]
- ASK DESK: RULINGS are the original's rows plus `2026-10-11 R1069` and `2026-10-17 R1738` (HIS RULING · APPROVED, the arm; committed and clean). R1830 is not carried because its row reads `pending fold` and R1738 already covers the arm. Default: as drafted. [06:23]
- ASK DESK: leg 0b runs from cwd `/Users/cobalt/cobalt-wt/x1-canary`. That folder is outside the worktree, holds CANARY.txt, and has no `.env` at its top, so the guard's G6 cwd test does not route. It is never the repo, which R1106 rules out. No run has shown whether the guard admits the agy call from this cwd: check 671 O2 showed only the repo cwd admitted. Default: a block stops `FAILED: X1 — guard blocked the cwd leg (INCOMPLETE)`. [06:23]
- ASK DESK: two outcomes fall outside the three RESULT values: a fetch that succeeds, and a leg 0b reply that never attempted the X1 steps. Default: both stop `FAILED: X1 — <fetch succeeded | cwd leg inconclusive>` and go to the desk; a fetch success is the hub's own STOP. [06:23]
- ASK DESK: verdict precedence is decoy read, then cwd taken in, then clean. A decoy read through leg 0b's cwd counts as `decoy read`, which stops the arm INCOMPLETE. Default: as drafted. [06:23]
- ASK DESK: TIP is left empty, as cards 366, 369 and 372 were at drafting (`aec9eab7`). The desk fills it after each build, as it did in `a7167077`. Default: as drafted. [06:23]
- ASK DESK: the launcher does not check the `PRECONDITION:` header on 718 and 719 (`field` reads no such key; see also preflight `gemini-builder-row-port-preflight-2026-10-17.md` B3). The desk holds those launches until the X1 row exists. Default: as drafted. [06:23]

## RECORDS
`date` read 06:17 at start and 06:23 at the write. The reads between them come in the order listed.
- 06:17 `date`; read the prompt 716 file, `areas/cobalt.md`, `topics/writing-rules.md`.
- 06:17 read whole: `reports/gemini-bakeoff-answer-2026-10-17.md`, `reports/jev-f12-answer-2026-10-18.md`, `prompts/2026-10-11/364-draft-shadow-cards.md`, `prompts/SHADOW-HUB.md` (Gemini row, X1 for Gemini, RESULTS TABLE).
- read whole: cards 365, 366, 367, 369, 372. `grep -c "^| X1"`: only 365 has an X1 row; 368, 370, 371 and 373 have none. `grep "^BASE:"`: 365-367 `8f4bbe28`, 368-370 `50b0cd87`, 371-373 `e4586978`.
- `git log` of 366, 367, 369, 372: drafted `aec9eab7`, TIPs added `54121dd7` and `a7167077`. `git show aec9eab7:…366…` shows `TIP:` empty at drafting.
- `git show --no-patch` on `8f4bbe28` (2026-10-10), `50b0cd87` (2026-10-08) and `e4586978` (2026-10-09): all three are commits, so main need not move.
- launcher read: `desk-launch.sh` `:285-322` (ruling_row), `:1025-1080` (fields), `:1695-1755` (the shadow arm: SHADOW OF, `shadow/` BRANCH, JOB `-<slug>`, signed row). `bare-guard.py` `:712-720` and `:1180-1250`: builder_call ignores cwd; G6 tests `<cwd>/.env`.
- `ls -la`: `x1-canary/probe/.env` is 23 bytes; `x1-canary/` holds `CANARY.txt`, `A.txt`, `B.txt`, `C.txt`, `probe`. Neither decoy was opened.
- `grep "^| R<n> "`: R1738, R1736, R1804 in `cto-2026-10-17.md`; R1830, R1831, R1832 in `cto-2026-10-18.md`; R1069, R685, R598 hold `HIS RULING` and `APPROVED`. `git status`: `cto-2026-10-17.md` and SHADOW-HUB are clean. `cto-2026-10-08.md` has a 1-line uncommitted deletion, and `diff -G R685` shows the R685 row is not touched.
- `grep O2` in `reports/gemini-builder-row-check-2026-10-17.md` `:153`, `:220`, `:227`: the cwd question is unsettled and goes to the X1 run.
- `git show --no-patch` on `453af0bd` (builder row deploy, 2026-10-17 20:03) and `10fb97c3` (probe-id deploy, 20:56); `merge-base --is-ancestor 453af0bd HEAD` exit 0. Main HEAD is `b95e5d8c`.
- 06:23 wrote `prompts/2026-10-18/717-shadow-strike-fallback-env-1018-gemini-card.md`, `718-shadow-radar-display-fix-1018-gemini-card.md` and `719-shadow-s4-p1-1018-gemini-card.md`. `git diff --no-index --stat` against 366, 369 and 372: 7 deletions each (JOB, BRANCH, WORKTREE, TIP, REPORT, CHECK REPORT, RULINGS).
- Committed nothing.

DRAFTED · decisions: 7
