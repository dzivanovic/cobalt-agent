# DESK-LINE — the proposed narrower desk launch line, and the desk's part of the new process (DRAFT 2026-09-30, fourth pass · PROPOSED · nothing here is applied)

His rulings: `cto-2026-09-30.md` R34 (the brain's RULED PROCESS, item 7), R38 (the second loop: the script runs the launch, the read-path cut) and R45 (the third pass: the script carries every launch; the rule changes are one list). This file changes nothing: the wake-up file, `settings.json`, LAWS and memory are edited by the desk at the fold. Every replacement text for a rule — the old F1–F7 and the rest — is in `RULE-CHANGES.md`, the one list he sees.

## 1. THE LINE TODAY (`docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md` line 13, SEAT PROFILE → LAUNCH)
`cd ~/cobalt`, then `claude --bg "Read 'docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md' and follow it exactly." --model claude-sonnet-5-5 --permission-mode auto --remote-control cto-desk --name cto-desk --allowedTools "Bash(git *)" "Edit" "Write" "Bash(python3 *)" --disallowedTools "AskUserQuestion" "EnterWorktree" --add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt-wt --no-chrome --strict-mcp-config`

What that line lets the desk do that its contract forbids ("hubs do the work; it never does the work itself"): any git command in any tree (`Bash(git *)`: a merge into a gate tree, a commit in a gate worktree, an amend); any file edit anywhere (`Edit`, `Write`: `src/`, `configs/`, a gate tree); any Python (`Bash(python3 *)`). On 2026-09-30 it used them for three hand commits into a gate tree and for commits on `main` while a deploy hub ran.

## 2. THE PROPOSED LINE
`cd ~/cobalt`, then

claude --bg "Read 'docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md' and follow it exactly." --model claude-sonnet-5-5 --permission-mode auto --remote-control cto-desk --name cto-desk --allowedTools "Bash(git add *)" "Bash(git commit *)" "Bash(git log*)" "Bash(git show*)" "Bash(git status*)" "Bash(git diff*)" "Bash(git -C * status*)" "Bash(git -C * log*)" "Bash(git -C * show*)" "Bash(git -C * diff*)" "Bash(git -C * rev-parse*)" "Bash(git -C * merge-base*)" --disallowedTools "AskUserQuestion" "EnterWorktree" "Edit(src/**)" "Edit(configs/**)" "Edit(//Users/cobalt/cobalt-wt/**)" "Edit(//Users/cobalt/cobalt/.git/**)" "Edit(//Users/cobalt/.claude/**)" --add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt-wt --no-chrome --strict-mcp-config

| change | string | proven or NEW | why |
|---|---|---|---|
| removed | `Bash(git *)` | — | the whole of git in every tree |
| kept, named | `Bash(git add *)` `Bash(git commit *)` | proven: tracked `.claude/settings.json` lines 25–26 | the desk commits its own report, cards and prompts on `main`, by explicit path (checklist C1) |
| kept, named | `Bash(git log*)` `Bash(git show*)` `Bash(git status*)` `Bash(git diff*)` | proven: `settings.json` lines 16–18; `show*` on the build line | reads |
| added | `Bash(git -C * status*)` `Bash(git -C * log*)` `Bash(git -C * show*)` `Bash(git -C * diff*)` `Bash(git -C * rev-parse*)` `Bash(git -C * merge-base*)` | proven: the deploy line (`prompts/2026-09-30/45` line 6) | verifying a hub's artifact in its worktree (L35), reading `main` from anywhere |
| NOT added (loop 2) | `Bash(git -C /Users/cobalt/cobalt worktree add *)` | — | the first draft asked for it as NEW; `desk-launch.sh` now runs the `worktree add` itself, so the desk line needs no string for it |
| removed, in `~/cobalt/.claude/settings.local.json` line 9 (not on this line) | `Bash(claude --bg *)` | — | the desk's own launch allow goes (gap 2): `desk-launch.sh` runs the `claude --bg` line, under the tracked `Bash(sh /Users/cobalt/.claude/ops/*)` (`settings.json` line 29). PROPOSED; a settings edit is his to order. What it takes with it is listed under the next table |
| removed | bare `Edit`, bare `Write` | — | the scoped allows of `settings.json` remain: `Edit(docs/40 - DevDocs/**)` (line 23) and `Edit(//Users/cobalt/Vault/Think/6 - Permanent/Memory/**)` (line 22) |
| added, DENY | `Edit(src/**)` `Edit(configs/**)` `Edit(//Users/cobalt/cobalt-wt/**)` | **NEW** (three) | the spec's "no Edit of `src/`, `configs/`, a gate tree". In auto mode an allow list pre-approves and does not forbid (L37): only a deny does |
| added, DENY (fourth pass) | `Edit(//Users/cobalt/cobalt/.git/**)` `Edit(//Users/cobalt/.claude/**)` | **NEW** (two; the shape proven by scratch items 3 and 4: an `Edit(<glob>)` deny, `//`-absolute, also stops the Write tool, with no dialog) | scratch item 4: in `auto` mode a path on no deny is written freely (A6), so the three denies above are the whole write guard; the hooks (`.git/hooks`) and the harness's own settings and ops scripts (`~/.claude/`) need their own. With them the desk cannot install `pre-commit-deploy-guard.sh` or an ops script by Edit: each install is his hand edit or a build row, as ordered |
| removed | `Bash(python3 *)` | — | Python can write any file; the pre-commit row gate runs its own `python3` inside git, not as a desk call |

SETTLED BY THE 09-30 SCRATCH TEST (`reports/fixed-files-scratch-test-2026-09-30.md`): a deny `Edit(<glob>)` also stops the Write tool on the same glob, relative or `//`-absolute (item 3, PASS); a Write of a NEW file under `docs/40 - DevDocs/` goes through once the bare `Write` is gone (item 4, PASS) — and so does a Write to any path on no deny (A6), hence the two denies added above.
STILL UNPROVEN, to settle on a scratch desk before install (L29: "a permission gate is proven in a scratch test to stop file AND command writes"):
- that the two new denies stop an Edit under `/Users/cobalt/cobalt/.git/` and `/Users/cobalt/.claude/` (the same shape as item 3; those exact paths not run);
- that `--allowedTools` without `Bash(git *)` still lets the settings' `Bash(claude stop *)`, `Bash(claude rm *)`, `Bash(herdr *)`, `Bash(sh /Users/cobalt/.claude/ops/*)` match as today (they live in `settings.json`, not on the line).

WHAT THE DESK CAN NO LONGER DO BY A LISTED STRING, and where the work goes:

| today, by hand | under the proposed line |
|---|---|
| a merge into a gate or seam tree (`git -C <wt> merge …`), a commit there, an amend | a build's (DEPLOY-HUB rule B): a conflict or a config classification is a card row of a build, with its suite |
| an edit of `configs/cobalt/jobs.yaml` | the build that adds the path (BUILD-HUB `## RESTARTS`) |
| `git tag -d <old rollback tag>` before a deploy resume | the deploy hub's own D0 (its `tag *` string) |
| moving a failed attempt's report aside | nothing to move: a deploy resumes into the same report (`## RESUME`) |
| `git push origin main` on his word | the NIGHTLY push is the close's own (`CLOSE-HUB.md` STEP-7, L55 as amended: `RULE-CHANGES.md` row 49); any other push stays on his word, by the desk, its allow in `~/cobalt/.claude/settings.local.json` (L55), not on this line |
| `git worktree remove`, `git branch -d` (cleanup, L46) | NOT on the proposed line: asked as its own string when the cleanup is ordered, or run by a cleanup hub |
| `cd <worktree>`, `git worktree add …`, `claude --bg …` for a build, a check or a deploy | ONE bare command: `sh /Users/cobalt/.claude/ops/desk-launch.sh <build|check|deploy> "<card>"` (a check's second pass adds `PASS-2`; a deploy resume adds `STEP-D0`; a new worker on a build or check adds its `CONTINUE` step). The script refuses, else runs the three itself |
| `claude --bg …` for the desk's own successor at REFRESH (L64) | `sh /Users/cobalt/.claude/ops/desk-launch.sh desk`: the script runs the wake-up's own launch line (the backticked `claude --bg …` span of the `- LAUNCH` line of `CTO-DESK-WAKEUP.md`, committed and unchanged) from `/Users/cobalt/cobalt` |
| `claude --bg …` for a one-off prompt: a drafter, a design tribunal and its seats, a brain tab | `sh /Users/cobalt/.claude/ops/desk-launch.sh prompt "<prompt file>"`: the script runs the prompt's own launch line from the cwd the prompt names, and REFUSES a line whose permission mode is a write-path mode (`acceptEdits`, or `dontAsk`, the fixed files' mode) or that carries a write string (`git add`, `git commit`, `git merge`, `uv run`, `launchctl`, `COBALT_ENV=`). Every write-path launch is a fixed file; the script carries every launch, so the desk's `claude --bg` stays out |
| a close prompt `prompts/<date>/99-close.md` and its `claude --bg …` | `sh /Users/cobalt/.claude/ops/desk-launch.sh close <YYYY-MM-DD>`: the script runs `CLOSE-HUB.md`'s own line from `/Users/cobalt/cobalt`; it refuses today's close before 21:00 ET and any close while a `deploy-hub-` session is live. No close prompt is written any more |

Committing "its own report, card and memory files": `git add` / `git commit` cannot be scoped to a path by a prefix rule (the paths come after the message). The scope is held by three things together: the checklist's bare `git add <paths>` / `git commit -m '…' -- <paths>` (C1); the deny on `src/`, `configs/` and the worktrees (nothing of those is ever modified by the desk, so nothing of those is there to stage); the pre-commit guard while a deploy hub is live. Memory files are written by Edit under the `settings.json` allow; this drafter did not read whether they sit under git.

## 2b. THE LINE MEASURED (gap 10) AND THE START-SET RULE
Measured 2026-09-30 by `grep -o "claude --bg.*strict-mcp-config" <file>` piped to `wc -c` (the count includes the newline), and `grep -o "Bash(" … ` for the strings; the draft-2 report's check quotes the calls.

| line | allow strings | deny strings | bytes |
|---|---|---|---|
| today, `CTO-DESK-WAKEUP.md` line 13 | 4 | 2 | 390 |
| proposed, third pass | 12 | 5 | 675 |
| proposed, this file's §2 (fourth pass: + the two denies of scratch item 4) | 12 | 7 | 747 |

FOURTH PASS: the two denies add 72 B; the proposed line is now 357 bytes longer than today's (747 − 390). The brain's answer to the third pass's DECISION 1 ("it goes in together with a cut of at least 109 B of dated cites in the wake-up (`CTO-DESK-WAKEUP.md:12`, `:21`, `:26`), measured at install") therefore becomes a cut of at least 181 B (10,146 − 176 + 357 = 10,327 B before that cut). The text below is the third pass's measurement and stands as the record of it. The third-pass line was 285 bytes longer (the first draft's line, with the `worktree add` string, was 13 allow; the brain's gap 10 counted that one). `CTO-DESK-WAKEUP.md` is 10,146 B today (`wc -c`).

THE START-SET RULE (the brain's RULED CHECK FLOW: nothing is added to a file the desk reads at start; an edit to the wake-up replaces lines and leaves the file smaller): the proposed line is LONGER than the line it replaces by 285 bytes, and it sits in the wake-up file, which the desk reads at every start. So the install of this line is lawful only as part of ONE edit of `CTO-DESK-WAKEUP.md` whose `wc -c` after is smaller than before. THE CUT IS NOW MEASURED (third pass, `RULE-CHANGES.md` `## START-SET`): rows 44–48 take 176 B out of the wake-up (10,146 → 9,970); with this line in the same edit the wake-up is 10,255 B — 109 B LARGER than today — while the start set as a whole stays 13 B smaller (34,017 → 34,004). The file grows, the set shrinks: whether that satisfies the rule for the wake-up itself is a DECISION in the third-pass report; the safe default is that the line waits for a further cut of the wake-up of more than 109 B. The three fixed files, the card format and the script are read by no start routine.

## 3. THE FOLD TEXTS — moved: `RULE-CHANGES.md` is their one home
The seven texts this section held in loop 2 are rows of `RULE-CHANGES.md`, each with its home `file:line`, its text today quoted, and the new text ready to fold (his 2026-09-30 R45: the rule changes are approved as a set; the desk folds them, not a drafter, and he is not asked rule by rule):

| loop-2 text | what it said | row(s) of `RULE-CHANGES.md` |
|---|---|---|
| F1 | deploys leave his four | 37, 47 |
| F2 | a deploy launches itself on clean checks and a green gate | 9 |
| F3 | he is asked only for a carried held defect and a schema rollback | 9 |
| F4 | his words are read by no start routine and no worker | 14, 22, 42, 45 |
| F5 | `CLAUDE.md` line 3 | 39 |
| F6 | `cobalt.md` lines 8–9 | 40 |
| F7 | L59 and the Preamble's last sentence | 4 |

At the fold of row 9 the desk replaces "his 2026-09-30 R38" in `DEPLOY-HUB.md` `## AUTHORIZATION` (THE DEPLOY'S APPROVAL IS THE STANDING RULE) with "L61". ORDER: the read-path rows (4, 39, 40) and the check rows (1–3) are folded BEFORE the fixed files are installed: until then `CLAUDE.md` still sends every worker to `## Start here` and L67 still names three checkers, against what the three hub files say.

## 4. THE DESK'S PART OF THE NEW PROCESS (his rulings of 2026-09-30: RULED WORKER ENDINGS; CONTINUE, DO NOT RESTART). The texts that carry it are rows 16–19, 21, 22, 26 and 27 of `RULE-CHANGES.md`
- PER EVENT: ONE §4 row and ONE commit per launch. §5 CURRENT holds one row per live session, overwritten in place; no TABS row, no WATCHES row (rows 21, 22).
- CONTINUE, DO NOT RESTART — builds and checks:
  - A worker whose last line is `FAILED:` (not `FAILED PREFLIGHT:`) and that stopped on something OUTSIDE itself — a held lock, stray rows, a missing fact, a refused listed command — is KEPT: the desk does not stop it, does not remove it, does not close its tab.
  - The desk fixes the cause. Then, BEFORE it sends anything, it measures the worker: `sh /Users/cobalt/.claude/ops/desk-context.sh <id>`. ABOVE 250,000 TOKENS it does not continue that worker: it verifies the wip commit, stops and removes it, and relaunches on a NEW worker — `sh /Users/cobalt/.claude/ops/desk-launch.sh <build|check> "<card>" [PASS-2] <step>`, `<step>` = the report's `## CONTINUE` step. (250,000 is the desk's own line; his to move once worker sizes are on record.)
  - At or below the line it sends ONE message to that worker: `CONTINUE: <step>. <fact>` — `<step>` from the report's `## CONTINUE`, `<fact>` what is now true and how the worker can read it itself (a command on its list). THE MESSAGE NAMES A STEP AND STATES A FACT. It never widens the job and never grants anything: no new row, file, command, path, approval or reading of a law. What would need one of those is a new card or a new launch line, never a message.
  - A NEW worker at the `## CONTINUE` step ONLY when: the launch line itself must change (a `FAILED PREFLIGHT`, a dialog — stop it, fix, relaunch; nobody presses a dialog); the session died; the judgment seat finds the worker misread the job; or the measure above.
  - A refused command the worker added on its own is a `## RECORDS` line in its report and no event for the desk.
  - One §4 row per `CONTINUE` sent and per new worker, the same turn (L34).
- THE LIST STATES (scratch test OBSERVATION 1, measured): `idle · done` = a finished worker. `idle · blocked` AFTER a `FAILED:` line = the worker waiting for `CONTINUE` (correct; keep it). `waiting · blocked` = the worker is on a permission DIALOG = a WRONG LAUNCH: under `dontAsk` (the three hub files and the close) it should never occur; if it does, stop the worker, fix the line, relaunch at its `## CONTINUE` step; nobody presses the dialog. `idle · blocked` with NO `FAILED:` line (e.g. a first call that failed on the API, `529`) = read the pane. A watch that fires on `blocked` alone cannot tell these apart: the desk reads the report's last line, then the pane.
- EVERY OPS SCRIPT installs under `/Users/cobalt/.claude/ops/` (no space in the path): a quoted spaced script path matches no `Bash(sh …)` allow string and opens a dialog (scratch item 6b). `desk-launch.sh` refuses to run from a spaced path; `desk-context.sh` is installed as the fixed copy in this folder (line 8 reads every project folder, scratch item 13).
- A DEPLOY NEVER CONTINUES BY MESSAGE. The desk sends a deploy hub nothing. A deploy that ended `FAILED` is verified, stopped and removed; its one continuation is `sh /Users/cobalt/.claude/ops/desk-launch.sh deploy "<card>" STEP-D0`. A hub HUNG after its first bootout: stop it and at once run that same command (it restores the residents first).
- A CHECK: at each pass's stop line the desk runs `desk-context.sh <id>` on the check session and writes the token total in its §4 row beside the line's `files opened`; `house B: needed` → verify, stop and remove the pass-1 session, commit the report, then `desk-launch.sh check "<card>" PASS-2`.
- THE NIGHTLY CLOSE (RULED — THE NIGHTLY CLOSE): each evening after the 21:00 ET pause, when no deploy hub is live, the desk runs `sh /Users/cobalt/.claude/ops/desk-launch.sh close <today>` — he is never asked to start it. A missed night → `… close <that date>` is the morning desk's FIRST act, before the plate. The close commits once and pushes `main` itself (`git push origin main`); the desk makes no commit on `main` from the launch to its stop line `^(CLOSE PUSHED|FAILED)`. One §4 row at the launch (L34).
- With the worker endings in the three hub files (`## DECISIONS` and `## RECORDS` in place of the ESCALATE section; `decisions: <n> · for Dejan: <n>` on every stop line), the desk's part is: `decisions: 0` → verify the artifact (L35), launch the next step; `decisions: ≥1` → hand the report path to the Opus judgment seat, record its answers; a `FOR DEJAN` item → one short question to him; a DEPLOY report → the judgment seat reads both sections, whatever the count.
