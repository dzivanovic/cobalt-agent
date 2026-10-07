# worktree-salvage draft — 2026-10-07

## §0 Headline
- Card `prompts/2026-10-07/83-worktree-salvage-card.md` drafted: `job-clean.sh salvage <worktree-name>`, rows W1-W7, files `ops/desk/job-clean.sh` and `tests/ops/test_gate_clean.py` only, `DB: none`, RESTARTS none expected.
- Card mode unchanged and pinned by the eight existing tests; no force form anywhere (W7 grep test).
- One fill token: `BASE` (main HEAD at launch). Main HEAD at draft: `2ac0e604`.
- Six named choices below, each with its default written into the card; none needs a new command.

## CARD
- Path: `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-07/83-worktree-salvage-card.md` (uncommitted; the desk commits it).
- W1 call and name checks (shared with card mode `:41-47`, plus registered stanza); W2 INSPECT report on stdout; W3 refusals after the report (`.env`, locked, six in-progress markers, wip branch taken); W4 wip branch `wip/<tree>-salvage-<YYYYMMDD>` + `SALVAGED:` line; W5 `worktree remove` (no flag), `branch -d` only if merged, `kept:` lines, fixed last line; W6 header; W7 no-force test.
- Test file is `tests/ops/test_gate_clean.py` (its `job-clean.sh` section `:248-315`); temp repos via the existing `Desk` fixture.

## DECISIONS
1. ASK DESK: a clean tree not merged into main prints `SALVAGED: <its branch> 0 files <m> commits ahead`, so every tree with work off main reaches the desk. Default YES (in card W4). Alternative: `SALVAGED:` only when a wip branch is made; the `kept:` line alone reports it. [06:52]
2. ASK DESK: the salvage commit runs the repo's hooks (`.git/hooks/pre-commit`: deploy guard acts on main only `:3-4`; desk row gate `:41-52`); a failed commit refuses with nothing removed. Default HOOKS RUN (card W4). Alternative: `commit --no-verify`, never blocked. [06:52]
3. ASK DESK: a detached HEAD not merged into main gets a wip branch at that HEAD (clean or dirty). Default YES (card W4). Alternative: REFUSE detached trees. [06:52]
4. ASK DESK: in-progress markers are six: `rebase-merge`, `rebase-apply`, `MERGE_HEAD`, `CHERRY_PICK_HEAD`, `REVERT_HEAD`, `BISECT_LOG`. Default SIX (card W3). Alternative: the three his order names (rebase, merge, cherry-pick). [06:52]
5. ASK DESK: a wip branch name already taken (second salvage of one tree on one day) refuses. Default REFUSE (card W3). Alternative: suffix `-2`, `-3`. [06:52]
6. ASK DESK: a registered tree whose directory is gone (prunable) is refused at the directory check (`job-clean.sh:47`) and reported; `git worktree prune` stays out of this card. Default REFUSE (card NOT IN THIS JOB). Alternative: a `prune` row in this card. [06:52]

## RECORDS
- `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `2ac0e604` (06:46 EDT).
- Read `ops/desk/job-clean.sh` whole, 64 lines: usage `:24`, field `:29-31`, pattern `:41-43`, agy-trial `:44`, symlink `:46`, dir `:47`, registered `:48-52`, merged `:55`, clean `:56`, `.env` `:57`, remove `:60-63`, last line `:64`, roots `:11`, `LC_ALL=C` `:13`.
- Read `tests/ops/test_gate_clean.py:1-115`, `:245-316`: `Desk` `:45-110`, `job_wt` `wt/x-job` on `ops/x-job` `:63-67`, `.gitignore` = `.env` `:57`, job-clean section `:248-315` (8 tests incl. parametrized pattern `:290`).
- `ls tests/ops`: the job-clean tests sit only in `test_gate_clean.py` (Grep `job-clean` over `tests/`).
- Read `prompts/CARD.md` whole: header keys `:11-29`, `DB: none` rule `:22`, body order `:31-62`.
- Read `prompts/2026-10-06/66-desk-stop-guard-card.md` whole (card shape precedent).
- `prompts/CTO-DESK-WAKEUP.md:13` LAUNCH: desk runs `--permission-mode auto`; its allow strings are git only.
- `prompts/STANDING-LIST.md:36`: CLASS (a) `Bash(sh /Users/cobalt/cobalt/ops/desk/*)` covers any `ops/desk/` script that reached main through build, check, deploy; `prompts/BUILD-HUB.md:12`, `:14` carry it.
- `Memory/topics/cto-desk-checklist.md:59` W8 R613 clause: wip branch `wip/<tree>-salvage-<date>`, side card per real work, "until it ships the desk reports a broken tree and removes nothing"; `:133` R190.
- `reports/cto-2026-10-07-words.md:3-5` `## R613`; `reports/cto-2026-10-07.md:8` R613, `:11` R615.
- `ops/desk/stop-guard.py:1-40` header style.
- `src/cobalt/jobs/restarts.py:38` `OPS_DESK_PREFIX`, `:230-232` operator script, `:245-246` tests.
- `.git/hooks/pre-commit` read whole (53 lines): deploy guard `:2-38`, row gate `:39-52`.
- Card `«FILL` count: `grep -c` → `1` (06:52 EDT).

WORKTREE SALVAGE CARD DRAFTED · decisions: 6
