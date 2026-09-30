# Fixed-files scratch test — 2026-09-30

Sandbox `~/cobalt-wt/scratch-fixed-0930/`, nothing installed (R49, R50). Desk probes ran 14:08–14:30 ET; hub `f9cd8480` (Opus 5.5, `acceptEdits`) stop line: `SCRATCH TEST HUB DONE · items run: 9 of 9 · pass: 9 · fail: 0 · defects: 3`. Hub and probe sessions stopped and removed; hub tab closed.

## Summary — the 14 items

| # | item | owner | result |
|---|---|---|---|
| 1 | `desk-launch.sh`: every kind, refusals | hub | PASS — D1 (a CONTINUE relaunch is refused while its own `.env` is left), D2 (`CARD.md` example refused) |
| 2 | `pre-commit-deploy-guard.sh` | hub | PASS — D3 (fail-open is silent when `python3` is missing) |
| 3 | deny `Edit(glob)` also stops Write | desk | PASS |
| 4 | desk can Write a new card without a bare `Write` | desk | PASS — only a deny forbids; paths off the three deny globs (`.git/hooks`, `.claude/`) need their own deny |
| 5 | git hook PATH from a Claude session | hub | PASS — real `claude` and `python3` both found |
| 6a | `claude --bg` from inside `sh` | desk | PASS |
| 6b | allow string vs spaced paths | hub | PASS — spaced argument matches; a quoted spaced script path raises a dialog (never install an ops script under a spaced path) |
| 7 | `agy` on a code check | hub | PASS |
| 8 | house spellings under `acceptEdits` | hub | PASS — all ran with no dialog; Sol = METER until 10-04 14:06 |
| 9 | `acceptEdits` refuses an off-list command | desk | FAIL for `acceptEdits` (opens a dialog); PASS for `dontAsk`. CONTINUE rule (a) holds only under `dontAsk` |
| 10 | `cd` to `agy-trial`, background house, `cd` back | hub | PASS |
| 11 | worker ends its turn on purpose (`idle`) | hub | NOT WRITTEN — the hub counted 9 of 9 but `HUB-RESULTS.md` has no item 11 section (8 sections); needs the hub's answer or a re-run |
| 12 | CONTINUE message resumes an idle worker, sender visible | desk | PASS |
| 13 | `desk-context.sh` on a worker's id | desk | FAIL — line 8 reads only `~/cobalt` transcripts (his ops script; one-line fix in the file below) |
| 14 | report Write from a worktree session | hub | PASS — in-dir no dialog; outside every `--add-dir` = dialog |

Defects for the draft: D1, D2, D3 (hub), item 9 (launch-line mode), item 13 (script).

---

# PART 1 — DESK-PROBES.md (verbatim)

# SCRATCH TEST — desk-run items (3, 4, 6a, 9, 12, 13), 2026-09-30 ≈14:08–14:30 ET

Sandbox: `/Users/cobalt/cobalt-wt/scratch-fixed-0930/`. Nothing installed; every probe session was a scratch session in a sandbox folder (folder trust accepted once per scratch folder in a throwaway herdr tab); all four probe sessions stopped and removed after. Method: the desk launched each probe with the flags the drafted files propose, the probe wrote its result into the chat, the desk read it in a herdr attach tab.

## ITEM 3 — does a deny on `Edit(<glob>)` also stop the Write tool on that glob?
RESULT: PASS (yes, it does).
Probe A (`probe-a`, cwd `deskmock`, Sonnet 5.5, `--permission-mode auto`, allow = the DESK-LINE proposed git strings, deny = `AskUserQuestion`, `EnterWorktree`, `Edit(src/**)`, `Edit(configs/**)`, `Edit(//Users/cobalt/cobalt-wt/scratch-fixed-0930/deskmock/scratch-wt/**)`, no bare `Edit` or `Write`). Verbatim results:
- A1 Write NEW `src/probe-a1.txt` → `<tool_use_error>File is in a directory that is denied by your permission settings.</tool_use_error>`
- A2 Edit EXISTING `src/existing.txt` → the same refusal.
- A3 Write NEW `configs/probe-a3.txt` → the same refusal.
- A4 Write NEW `scratch-wt/probe-a4.txt` (the absolute-path deny glob) → the same refusal.
So a deny on the `Edit(...)` rule covers the Write tool on the same glob, for a relative glob (`src/**`, `configs/**`) and for the `//`-absolute glob. The refusal is a tool error, no dialog.

## ITEM 4 — can the desk still Write a NEW card under `docs/40 - DevDocs/` once the bare `Write` is gone?
RESULT: PASS (yes), with one thing the files should say plainly.
- A5 Write NEW `docs/40 - DevDocs/cards/new-card.md` → `File created successfully at …/deskmock/docs/40 - DevDocs/cards/new-card.md`. The scratch project's `.claude/settings.json` had `Edit(docs/40 - DevDocs/**)` (the real tracked settings line 23) and no bare `Write`.
- A6 (the control) Write NEW `notes/other.txt`, a path on neither an allow nor a deny → `File created successfully …/notes/other.txt`. In `auto` mode the absence of a bare `Write` does NOT stop writes to paths outside the deny globs: ONLY a deny stops a write. DESK-LINE.md §2 already says "an allow list pre-approves and does not forbid (L37): only a deny does"; this probe confirms it with a run. The three deny globs are therefore the whole write guard of the proposed desk line; any path the desk must not write that is not on those three globs (for example `.git/hooks`, `.claude/`) needs its own deny.

## ITEM 6a — does `claude --bg` started from inside `sh` register, name and attach as a desk-typed launch does?
RESULT: PASS.
`sh -c 'cd /Users/cobalt/cobalt-wt/scratch-fixed-0930/probes/noop && claude --bg "Reply with only the word DONE." --name scratch-launch-test --remote-control scratch-launch-test --permission-mode dontAsk --model claude-sonnet-5-5'` → `backgrounded · b8c3fc0c · scratch-launch-test`, exit 0. `desk-list.sh` then printed `b8c3fc0c · scratch-launch-test · ~/cobalt-wt/scratch-fixed-0930/probes/noop · idle · done` (the cwd of the subshell's `cd`, the name, the state reached done); `claude agents --json --all` row: `{'id': 'b8c3fc0c', 'name': 'scratch-launch-test', 'cwd': '…/probes/noop', 'status': 'idle', 'state': 'done'}`; `claude attach b8c3fc0c` in a herdr pane opened the session (pane title `scratch-launch-test`; `pgrep` showed the attach process). A launch from inside a `sh` subshell is the same launch as a typed one.
Second half ("does `Bash(sh /Users/cobalt/.claude/ops/*)` match a command whose path ARGUMENT holds spaces"): PASS for the real allow, by today's record — the desk (auto mode, that allow from tracked `settings.json` line 29) ran `sh /Users/cobalt/.claude/ops/wait-stop-line.sh "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/<file>.md" '<regex>' <seconds>` more than thirty times on 2026-09-30 with no dialog and no refusal. The hub's item 6b tests the scratch equivalent and a script path that itself holds a space (the real path has none).

## ITEM 9 — under `acceptEdits`, is a command on no allow string REFUSED with no dialog? (CONTINUE, DO NOT RESTART (a) rests on it)
RESULT: FAIL for `acceptEdits` (it opens a DIALOG and the session stops until someone answers); PASS for `dontAsk`.
- Observed three times today under `acceptEdits`, each time the session went `waiting · blocked` in LIST until the desk pressed Escape, and then sat `idle` until a message told it to continue: (1) the scratch test hub's first compound inspection command (`find … ; grep … ; git … ; ls …`) ≈14:08, dialog text: "This command changes directory before running a version-control command … Approve only if you trust it"; (2) probe C's first attempt, a `git worktree add …` the worker chose on its own after a Write error; (3) earlier today (deploy 1 attempts 5 and 7): an `ls` outside `--add-dir`, a `rm` outside `--add-dir`, and a `git ls-files` not on the list. So a worker that adds a command on its own does NOT get a refusal under `acceptEdits`.
- Probe B (`probe-b`, cwd `probes/dontask`, `--permission-mode dontAsk`, allow `Bash(git log*)` and `Read`): B1 `ls /etc` (on no allow string) → REFUSED, no dialog; the tool message, verbatim: "Permission to use Bash has been denied because Claude Code is running in don't ask mode. IMPORTANT: You may attempt to accomplish this action using other tools that might naturally be used to accomplish this goal, e.g. using head instead of cat. But you should not attempt to work around this denial in malicious ways, e.g. do not use your ability to run tests to execute non-test actions. You should only try to work around this restriction in reasonable ways that do not attempt to bypass the intent behind this denial. If you believe this capability is essential to complete the user's request, STOP and explain to the user what you were trying to do and why you need this permission. Let the user decide how to proceed." B2 `git log -1` (allowed) ran (exit 128, no commits in the scratch repo: the allow let it through). The probe reported: "Permission dialog: none ever appeared."
CONSEQUENCE FOR THE FILES: rule (a) of CONTINUE, DO NOT RESTART ("a command the worker added on its own is refused → it records that and goes on") is TRUE only under `--permission-mode dontAsk`, NOT under the `acceptEdits` the hub files' launch lines carry. UNPROVEN, and not tested here: whether a build under `dontAsk` can still Edit and Write files in its worktree (it would need an explicit `Edit` / `Write` allow, as `acceptEdits` gives them implicitly). And the refusal message itself tells the worker "STOP and explain to the user": a worker may stop on it instead of going on, so (a) also needs the hub text to say what to do on that message.

## ITEM 12 — does a `CONTINUE: <step>. <fact>` message from `cto-desk` reach a worker idle on its `FAILED:` line and resume it; does the worker see the sender's name?
RESULT: PASS.
Probe C (`probe-c`, second launch; the first launch failed on the rig, see OBSERVATIONS) wrote `worker-report.md` = `STEP-1 done` + `FAILED: test-wait — a held lock (simulated)` and ended its turn (LIST: `idle · blocked`). The desk sent `CONTINUE: step 3. The simulated lock is free.` by SendMessage (tool reply: "queued there"). Within 8 seconds the file read, verbatim: `STEP-1 done` / `RESUMED: CONTINUE: step 3. The simulated lock is free. | sender: cto-desk` / `WORKER DONE`, LIST `idle · done`. The worker resumed in the same session and saw the sender as `cto-desk`. So the continue rule's mechanism works: a message to an idle worker resumes it, names its sender, and the worker acts on the text.

## ITEM 13 — `desk-context.sh <id>` on a WORKER's id
RESULT: FAIL (a defect in the script).
`sh /Users/cobalt/.claude/ops/desk-context.sh <id> 250000` printed `context 597589 of 250000 — REFRESH` for the desk (`3adfd15c`), `context 700249 of 250000 — REFRESH` for the brain (`e079c3f6`, cwd `~/cobalt`), and `no transcript for <id>` (exit 2) for every worker whose cwd is not `~/cobalt`: `f9cd8480` (scratch test hub, cwd `…/scratch-fixed-0930/wt`), `e82d2f49`, `09060d06`, `6009ed1c`. Cause: `/Users/cobalt/.claude/ops/desk-context.sh` line 8 reads `/Users/cobalt/.claude/projects/-Users-cobalt-cobalt/"$id"*.jsonl` only; a worker's transcript lives under `~/.claude/projects/<its own cwd, path-encoded>/` (there are such folders, e.g. `-Users-cobalt-cobalt-wt-agy-trial`). THE ONE-LINE FIX (not applied; the script is outside the plans folder and outside this test): `ls -t /Users/cobalt/.claude/projects/*/"$id"*.jsonl 2>/dev/null | head -1`. The continue rule's "the desk measures the worker (`desk-context.sh <id>`) before it sends CONTINUE" cannot work until that line is fixed; every hub worker runs from a worktree. (The desk's own size is 597,589 tokens: the REFRESH threshold is 250,000; the desk is due to hand over.)

## OBSERVATIONS (not items; the desk saw them while running the rig)
1. LIST states, measured: a finished worker = `idle · done`; a worker idle on a `FAILED:` line, waiting for a message = `idle · blocked`; a worker stopped on a permission dialog = `waiting · blocked`; a worker whose first call failed on the API (`529`) = `idle · blocked`. A watch that fires on `blocked` alone cannot tell a dialog from a worker that is correctly waiting for CONTINUE; the desk reads the pane.
2. Folder trust: `claude --bg` in a directory that has never been trusted refuses to start: `Workspace not trusted. Run `claude` in <dir> once and accept the trust prompt, then retry.` Real worktrees of `~/cobalt` (`~/cobalt-wt/<branch>`) launched all day without it (the trust of the repo covers its worktrees); a scratch folder that is its own repo needs one interactive accept each. `desk-launch.sh` runs in worktrees of `~/cobalt`, so it is not affected, but a card whose worktree is not one of them would stop there.
3. `worktree.bgIsolation`: a background session in a folder whose `.claude/settings.json` lacks `"worktree": {"bgIsolation": "none"}` tries to create its own git worktree (probe C's first launch: `Write(worker-report.md)` → `Error writing file`, then `git worktree add -b probe-c-worker .claude/worktrees/probe-c` → a dialog). The real repo's tracked settings carry it (and so do its worktrees); any scratch or new project needs it.
4. A stray prompt text (`Read PROBE-C.md and follow it exactly`) appeared in probe B's input box when the desk attached; the desk did not type it and did not submit it. Unexplained; noted.


---

# PART 2 — HUB-RESULTS.md (verbatim)

# SCRATCH TEST HUB — RESULTS (2026-09-30)

Seat: scratch-test-hub · Opus 5.5 · acceptEdits · cwd /Users/cobalt/cobalt-wt/scratch-fixed-0930/wt

## ITEM 1 — desk-launch.sh
RESULT: PASS (every kind launches, every promised refusal I ran fires) — with 2 DEFECTS in the draft (D1, D2 below)

EDITS TO THE COPY `scripts/desk-launch.sh` (the only ones):
- `:75` `REPO=/Users/cobalt/cobalt` → `REPO=/Users/cobalt/cobalt-wt/scratch-fixed-0930/main` (ordered).
- `:76` `WT=/Users/cobalt/cobalt-wt` → `WT=/Users/cobalt/cobalt-wt/scratch-fixed-0930` (NOT in the order; needed so the build's and deploy's `git worktree add` land inside the sandbox and not in `/Users/cobalt/cobalt-wt/<name>`; it also makes `wt` a "`$WT/<one name>`" worktree the check card can name).
- `/Users/cobalt/.claude/ops` → `/Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts` everywhere (ordered): lines 9, 10, 13–18, 21, 22 — comments only; the script's code never names that path.
- Side effect of the WT edit, not a defect: the hub lines hard-code `/Users/cobalt/cobalt-wt/<worktree>` while the script builds the tip-merge string from `$WT`, so in the sandbox the deploy line shows `…/cobalt-wt/scratch-fixed-0930/sgate merge --no-edit 87e024f4` beside `…/cobalt-wt/sgate merge --no-edit main`. With the real `WT` the two agree.

SANDBOX FIXTURES (all under the sandbox): hub files copied into `main/docs/40 - DevDocs/prompts/` and committed (`scripts/setup-hubs.sh`); build report committed in `wt` (TIP `87e024f4`, BASE `86d60082`); cards with a SPACE in the file name, in a dir with spaces: `…/prompts/2026-09-30/01 sbuild-card.md` (build), `02 scheck-card.md` (check, WORKTREE `wt`), `03 sdeploy-card.md` (deploy), plus refusal cards 20–28 (`scripts/gen-badcards.sh`); one-off prompts 10–19 (`scripts/gen-prompts.sh`). Runner: `scripts/run.sh` = `sh desk-launch.sh "$@" 2>&1; echo EXIT=$?`.

COMMANDS (each one Bash call; `<P>` = `/Users/cobalt/cobalt-wt/scratch-fixed-0930/main/docs/40 - DevDocs/prompts`):
- DRY: `env DESK_LAUNCH_DRY=1 sh /Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts/run.sh <kind> "<P>/2026-09-30/<nn> …-card.md" [PASS-2] [<step>]`
- STUB: `env PATH=/Users/cobalt/cobalt-wt/scratch-fixed-0930/bin:/usr/bin:/bin sh /Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts/run.sh …` (run.sh prints `claude=/Users/cobalt/cobalt-wt/scratch-fixed-0930/bin/claude` on these runs; on DRY runs `claude=/opt/homebrew/bin/claude`, never invoked).

EVERY KIND — DRY then STUB, exit status:
| kind | DRY | STUB |
|---|---|---|
| `build 01` | EXIT=0; printed `git -C …/main worktree add -b scratch/sbuild …/scratch-fixed-0930/sbuild 86d60082`, `cd …/sbuild`, the BUILD line | EXIT=0; `Preparing worktree (new branch 'scratch/sbuild')`, stub cwd `…/sbuild` |
| `check 02` | EXIT=0; `cd …/wt` + CHECK line | EXIT=0; stub cwd `…/wt` |
| `check 02 PASS-2` | before a report: `REFUSED: PASS-2 needs pass 1's report: …/reports/scheck-check-2026-09-30.md` EXIT=1 | with a pass-1 line `… house B: needed …`: EXIT=0 |
| `check 02 "STEP-3 rerun"` | EXIT=0 | EXIT=0 |
| `check 02 PASS-2 STEP-4` | — | EXIT=0 |
| `deploy 03` | EXIT=0; `git -C …/main worktree add -b scratch/gate …/sgate main`, `cd …/main`, DEPLOY line | EXIT=0; `Preparing worktree (new branch 'scratch/gate')`, stub cwd `…/main` |
| `deploy 03 STEP-D0` | before the gate exists: `REFUSED: a resume needs the gate worktree …/sgate` EXIT=1 | after: EXIT=0, no worktree add |
| `desk` | EXIT=0; `cd …/main` + the wake-up's line | EXIT=0; stub cwd `…/main` |
| `prompt 10-own-line.md` (a line of its own + a `cd` line) | EXIT=0; `cd …/wt` | EXIT=0 |
| `prompt 11-span.md` (backticked `cd` span + backticked `claude --bg` span on one line) | EXIT=0; `cd …/wt` | EXIT=0 |

THE sed LIFTS: the wake-up's `- LAUNCH` line (`cd ~/cobalt`, then `` `claude --bg …` ``) gave exactly: `claude --bg "Read 'docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md' and follow it exactly." --model claude-sonnet-5-5 --permission-mode auto --remote-control cto-desk --name cto-desk --allowedTools "Bash(git *)" "Edit" "Write" "Bash(python3 *)" --disallowedTools "AskUserQuestion" "EnterWorktree" --add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt-wt --no-chrome --strict-mcp-config`. The prompt span and own-line forms both gave the whole line; the `cd` span gave `/Users/cobalt/cobalt-wt/scratch-fixed-0930/wt` in both forms.

THE FINAL MESSAGES THE STUB RECEIVED (`results/stub-claude.log`, `grep -n -o "args: --bg .* --model [a-z0-9-]*"`), verbatim:
```
1:args: --bg Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md' and follow it exactly. CARD: '/Users/cobalt/cobalt-wt/scratch-fixed-0930/main/docs/40 - DevDocs/prompts/2026-09-30/01 sbuild-card.md' --model claude-opus-5-5
3:args: --bg CONTINUE: STEP-3 rerun. Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md' and follow it exactly. CARD: '…/02 scheck-card.md' --model claude-opus-5-5
5:args: --bg CONTINUE: STEP-D0. Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md' and follow it exactly. CARD: '…/03 sdeploy-card.md' --model claude-opus-5-5
6:args: --bg Read 'docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md' and follow it exactly. --model claude-sonnet-5-5
9:args: --bg PASS-2. Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md' and follow it exactly. CARD: '…/02 scheck-card.md' --model claude-opus-5-5
10:args: --bg PASS-2. CONTINUE: STEP-4. Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md' and follow it exactly. CARD: '…/02 scheck-card.md' --model claude-opus-5-5
```
Stub cwds, in order: sbuild, wt, wt, main, main, main, wt, wt, wt, wt.

THE eval (the stub logs `$*`, which hides argument boundaries, so a probe `claude` in `probes/argc/` printed `$#` and each argument; runner `scripts/argc.sh`): `check 02 PASS-2 "STEP-4 two words"` → `ARGC=48`, `ARG1=[--bg]`, `ARG2=[PASS-2. CONTINUE: STEP-4 two words. Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md' and follow it exactly. CARD: '/Users/cobalt/cobalt-wt/scratch-fixed-0930/main/docs/40 - DevDocs/prompts/2026-09-30/02 scheck-card.md']`, `ARG3=[--model]`, `LAST=[/Users/cobalt/cobalt-wt]`, `EXIT=0`. `deploy 03 STEP-D0` → `ARGC=70`, ARG2 the whole message, `LAST=[/Users/cobalt/Library/LaunchAgents]`. The message with the spaced card path is ONE argument.
EXIT STATUS OF THE LAUNCH: probe `claude` exiting 7 (`scripts/argc7.sh desk`) → `EXIT=7`: the script passes the launch's status on.

THE READ OF A CHECK REPORT'S LAST LINE: pass-1 line `CHECK DONE · job: scheck · pass: 1 · … · house B: needed · …` → PASS-2 launched (above). The same line with `house B: not needed` → `REFUSED: PASS-2 launches only on a pass-1 stop line that says 'house B: needed'; the report ends: CHECK DONE · job: scheck · pass: 1 · tip: 87e024f4 · house A: grok FINDINGS: 0 · … · house B: not needed · … · for Dejan: 0`, EXIT=1. First check with the report present → `REFUSED: the check report already exists: a second pass is PASS-2, a new worker names its CONTINUE step`, EXIT=1.

REFUSALS (all DRY; each EXIT=1, message on stderr, nothing run):
- fixed file with its `«INSTALL` token (as drafted): `REFUSED: the fixed file still carries its «INSTALL token (his approval row is not filled): …/prompts/BUILD-HUB.md`. (Sandbox copies then had the token replaced with `2026-09-30 R0 (scratch)` — `scripts/untoken.sh` — and committed.)
- fixed file changed since its commit: `REFUSED: the fixed file differs from its commit: …/BUILD-HUB.md`
- kind not a fixed file (`review 01…`): `REFUSED: kind 'review' is none of build, check, deploy, desk, prompt`
- incomplete card, «FILL: `7:BASE: «FILL: the base commit»` then `REFUSED: incomplete card: the «FILL tokens listed above still stand`
- incomplete card, empty key: `REFUSED: incomplete card: 'BRANCH' is empty`
- incomplete card, missing section: `REFUSED: incomplete card: no '## ROWS' section`
- card not committed: `REFUSED: the card is not committed on main: …/27 uncommitted-card.md`
- worktree `../outside`: `REFUSED: worktree '../outside' is outside the approved pattern /Users/cobalt/cobalt-wt/scratch-fixed-0930/<one directory name>`; worktree `cobalt-wt/sbad`: the same message; worktree `agy-trial`: `REFUSED: worktree 'agy-trial' is the check hubs' scratch tree, never a job's`
- with-DB launch while a `.env` lock exists (`sgate/.env`): build, check (at a step) and deploy STEP-D0 each → `REFUSED: with-DB launch refused: the cobalt_dev lock is held (/Users/cobalt/cobalt-wt/scratch-fixed-0930/sgate/.env) (L76)`
- deploy relaunch without STEP-D0 while the gate exists: `REFUSED: the gate worktree …/sgate already exists: a relaunch is 'desk-launch.sh deploy <card> STEP-D0'`
- deploy resume `STEP-3`: `REFUSED: a deploy resumes at STEP-D0 only, never 'STEP-3'`
- deploy card with `db query … like '%a%'`: `REFUSED: a db query string in the card contains '%' (the tool refuses it; use strpos)`
- `build 01 PASS-2`: `REFUSED: PASS-2 is an option of kind check only`
- prompt `--permission-mode acceptEdits`: `REFUSED: permission mode acceptEdits: a write-path launch is a fixed file (build, check, deploy)`
- prompt `"Bash(git add *)"`: `REFUSED: write string 'git add' on a prompt line: a write-path launch is a fixed file`; `git commit`, `git merge`, `uv run` (`"Bash(uv run pytest *)"`), `launchctl` (`"Bash(launchctl print *)"`), `COBALT_ENV=` (`"Bash(COBALT_ENV=dev ls *)"`): the same message with each string named
- prompt `"Bash(git -C …/main commit *)"`: `REFUSED: a git -C write string on a prompt line: a write-path launch is a fixed file`
- a card as a prompt: `REFUSED: a card is launched by its kind (build, check, deploy), never as a prompt`; `CHECK-HUB.md` as a prompt: `REFUSED: a fixed file is launched by its kind, never as a prompt`
- NOT RUN: `desk` with a wake-up line not naming cto-desk; the `check_paths` refusal (a path under no `--add-dir`); a `worktree add` failure. Not in the order's list; left for lack of need.

DEFECT D1 — A CONTINUE WORKER CAN NEVER BE LAUNCHED WHILE ITS OWN `.env` IS LEFT. `BUILD-HUB.md:36` and `CHECK-HUB.md:56` say a NEW session at a `CONTINUE: <step>` runs `ls -la …/<WORKTREE>/.env` first and, "`.env` present → W (f) FIRST". The script refuses to launch that session. Input (`.env` in the job's own worktree, ignored as the real `.gitignore` does; `scripts/lock.sh own`): `build 01 STEP-5` → `REFUSED: with-DB launch refused: the cobalt_dev lock is held (/Users/cobalt/cobalt-wt/scratch-fixed-0930/sbuild/.env) (L76)` EXIT=1; `check 02 STEP-5` → `REFUSED: /Users/cobalt/cobalt-wt/scratch-fixed-0930/wt/.env exists: the build did not release the lock (L76)` EXIT=1. Cause: `desk-launch.sh:355` (build `lock_free`), `:388` and `:393` (check), `:432` (deploy; STEP-D0 with the gate's own `.env` is refused the same way) — `lock_free` (`:329–333`) and `:388` do not except the job's own worktree when a resume step is given. The case is the one the recovery exists for (the session died mid with-DB suite).

DEFECT D2 — CARD.md's OWN EXAMPLE IS REFUSED. `CARD.md:82` (and :89, :94, :98, :119, :126) print the body headings as `` `## ROWS` `` (backticked). A card made by copying example 1 as printed (`23 example1-card.md`, built by `sed` from CARD.md) → `REFUSED: incomplete card: no '## ROWS' section` EXIT=1: `desk-launch.sh:276` greps `^## ROWS`. The script is on the safe side; the example misleads a drafter.

## ITEM 2 — pre-commit-deploy-guard.sh
RESULT: PASS (refuses and lets through as written; fails open) — with 1 DEFECT (D3: one fail-open path is silent)

EDIT TO THE COPY `scripts/pre-commit-deploy-guard.sh`: `:54` `= "/Users/cobalt/cobalt" ]` → `= "/Users/cobalt/cobalt-wt/scratch-fixed-0930/main" ]` (the only one; needed so the sandbox main counts as the main tree).
THE HOOK `main/.git/hooks/pre-commit` (`scripts/assemble-hook.sh`): line 1 `#!/bin/sh`, then the whole guard copy (hook lines 2–86; `deploy guard (begin)` at 54, `(end)` at 86), then my scratch row gate (`scripts/rowgate-hook.sh` lines 2–5), a pipeline that is the hook's LAST command: `git -c core.quotePath=false diff --cached --name-only --diff-filter=ACM | grep '^docs/40 - DevDocs/reports/cto-[^/]*\.md$' | while … awk 'length($0) > 300' … exit 1`.
HOW EACH COMMIT WAS MADE: `env PATH=/Users/cobalt/cobalt-wt/scratch-fixed-0930/bin:/usr/bin:/bin sh /Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts/commit-case.sh <list> <commit>`. The wrapper writes `agents.json` (`live` = rows `deploy-hub-old` pid null, `deploy-hub-sdep` pid 4242, `sbuild-build` pid 77; `none` = the same without the live deploy row), stages, runs `git -C <repo> commit`, prints `EXIT=`. It is a wrapper because of item 5: a plain `git -C … commit` from this session would put the REAL `claude` on the hook's PATH.

| list | commit | output (verbatim) | exit |
|---|---|---|---|
| live | desk file on main (`plans/desk-note.md`) | `pre-commit: a deploy hub is live — no desk commit on main until its stop line:` / `a1b2c3 deploy-hub-sdep` / `Write by Edit / Write only; commit after DEPLOYED or FAILED, once the hub is stopped and removed.` | 1 |
| live | deploy report only (`reports/deploy-sdep-2026-09-30.md`) | `[main 6f0b658] scratch: item 2 live deploy` | 0 |
| live | nothing staged (`--allow-empty`) | `[main 6185ccf] scratch: item 2 live empty` | 0 |
| live | in the `wt` worktree (`wt-note.md`, branch scratch/wt) | `[scratch/wt f8c431b] scratch: item 2 live wt` | 0 |
| none | desk file on main | `[main 103167f] scratch: item 2 none desk` | 0 |
| none | `reports/cto-2026-09-30.md` with a 327-char line (`| R1 | ` + 320 × `x`) | `row gate: docs/40 - DevDocs/reports/cto-2026-09-30.md has a line over 300 characters` (the guard fell through; the row gate still refused) | 1 |
| none | the same file, a short line | `[main a3e2655] scratch: item 2 none rowgate-ok` | 0 |
| `agents.json` not JSON (`Error: not json at all`) | desk file | `pre-commit: deploy guard could not read the session list (claude agents --json); NOT enforced for this commit.` then `[main ff46f77] …` — FAILS OPEN, loud | 0 |
| `agents.json` chmod 000, live row inside | desk file | `[main 543ccd1] …`, no warning — the STUB's `cat … 2>/dev/null \|\| echo "[]"` answered `[]`; a stub artifact, not the guard | 0 |
| live row; NO `claude` on the hook's PATH (`PATH=/usr/bin:/bin`) | desk file | `pre-commit: deploy guard could not read the session list (claude agents --json); NOT enforced for this commit.` then `[main e75b859] …` — fails open, loud | 0 |
| live row; `claude` (stub) present, NO `python3` on the hook's PATH | desk file | `[main c46dce7] scratch: item 2 nopython desk` — NO warning (the `date`/`mkdir`/`chmod: command not found` lines around it are my wrapper under its narrowed PATH) | 0 |

DEFECT D3 — ONE FAIL-OPEN PATH IS SILENT. Header `:42–43` promises: list unreadable → "the guard WARNS on stderr and lets the commit through — it fails open, loud". With `python3` missing (or crashing before it prints), `python3 … 2>/dev/null` prints nothing, `guard_live` is empty, and the `""` arm (`:71`) lets the commit through with no word, while a deploy hub is live. Cause: `pre-commit-deploy-guard.sh:59–69` (python's failure is folded into the "no live row" answer). Fix: end the pipeline with `|| echo UNREADABLE` and have the Python print `NONE` when no row matches, so `""` never means "no hub". Item 5 shows `python3` IS on a hook's PATH from a Claude session, so the risk is small.

## ITEM 5 — a git hook's PATH from a Claude session
RESULT: PASS (question answered: both found; `claude` is the REAL one)
Hook (`scripts/hook-path-probe.sh`, installed by `sh /Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts/install-hook.sh hook-path-probe.sh` as the sandbox `main/.git/hooks/pre-commit`) writes `command -v claude`, `command -v python3`, `$PATH` to `results/hook-path.txt`.
Trigger, from this session: `git -C /Users/cobalt/cobalt-wt/scratch-fixed-0930/main commit --allow-empty -m "scratch: item 5 hook PATH probe"` → `[main ad1a7ad] scratch: item 5 hook PATH probe`.
`results/hook-path.txt`, verbatim:
```
claude: /opt/homebrew/bin/claude
python3: /opt/homebrew/bin/python3
PATH=/opt/homebrew/opt/git/libexec/git-core:/opt/homebrew/bin:/opt/homebrew/sbin:/Users/cobalt/.orbstack/bin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin:/Users/cobalt/.local/bin:/Users/cobalt/.lmstudio/bin:/Users/cobalt/.lmstudio/bin
```
`command -v claude` printed `/opt/homebrew/bin/claude`: the REAL path, not the stub (`/Users/cobalt/cobalt-wt/scratch-fixed-0930/bin/claude`). The hook inherits the session's own PATH, with git's `git-core` put first. So the installed guard WOULD run the real `claude agents --json` from a desk commit, as it is meant to.

## ITEM 6b — `Bash(sh /Users/cobalt/cobalt-wt/scratch-fixed-0930/*)` against paths with spaces
RESULT: PASS (question answered). A spaced ARGUMENT matches with no dialog. A spaced SCRIPT PATH, quoted, does NOT match: it opens a dialog (the one blocked sub-case).
- A spaced argument with an unspaced script path: `sh /Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts/bgjob.sh 0 "/Users/cobalt/cobalt-wt/scratch-fixed-0930/cards dir/a b.md"` → ran with NO dialog, `(Bash completed with no output)`. Also every item-1 call, e.g. `env DESK_LAUNCH_DRY=1 sh /Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts/run.sh build "/Users/cobalt/cobalt-wt/scratch-fixed-0930/main/docs/40 - DevDocs/prompts/2026-09-30/01 sbuild-card.md"` (a quoted `…/40 - DevDocs/…` argument, the real case's shape) ran with no dialog, about 40 times. So the real `Bash(sh /Users/cobalt/.claude/ops/*)` should match `sh /Users/cobalt/.claude/ops/desk-launch.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/…"`, since that script path has no space.
- The script path WITH a space, QUOTED: `sh "/Users/cobalt/cobalt-wt/scratch-fixed-0930/ops dir/echo-args.sh" "/Users/cobalt/cobalt-wt/scratch-fixed-0930/cards dir/a b.md"` → an approval DIALOG. My tool result: "The user doesn't want to proceed with this tool use. The tool use was rejected". `cto-desk` then messaged: the call "raised an approval dialog; I cancelled it with Escape … dialog raised, not allowed by the string". The allow string does NOT match a quoted script path (the command starts `sh "/Users…`, not `sh /Users…`).
- The PLAIN (unquoted) spaced script path: NOT RUN. The rule: "a call that blocks is … never retried in another shape", and the desk said: "Do not retry the spaced-path call." Unquoted, `sh` would open `/Users/cobalt/cobalt-wt/scratch-fixed-0930/ops` (no such file), so it would fail anyway.
- Consequence for the install: never install an ops script under a path with a space; the real `/Users/cobalt/.claude/ops/` has none.

## ITEM 7 — `agy` on a CODE check
RESULT: PASS
Setup: `sample.py` copied by the Write tool to `/Users/cobalt/cobalt-wt/agy-trial/scratch/fixed-files-test-0930/sample.py` (functions `add`, `neg`).
Run: `cd /Users/cobalt/cobalt-wt/agy-trial` (its own call), then, `run_in_background`:
`agy --model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 20m --add-dir /Users/cobalt/cobalt-wt/agy-trial --print="You are GEMINI, checking code. The folder is scratch/fixed-files-test-0930/ (absolute path /Users/cobalt/cobalt-wt/agy-trial/scratch/fixed-files-test-0930/). Read sample.py in that folder with your file viewer only. Run NO shell command. Do NOT write any file. List ONLY the names of the functions defined in sample.py, one per line, then end with exactly the line FINDINGS: 0"`
Notice: `Background command "Gemini house code check via agy in background" completed (exit code 0)`. Output file, verbatim:
```
add
neg
FINDINGS: 0

[exited with code 0]
```
Exit code 0; names `add` and `neg`; no error; no dialog. The harness's trailing `[exited with code 0]` is there, as `CHECK-HUB.md:93` says it is.

## ITEM 8 — the house spellings under `acceptEdits`
RESULT: PASS — all three RAN with NO dialog (Sol's answer was a METER, not a dialog)
Each ran from cwd `/Users/cobalt/cobalt-wt/agy-trial`, in the foreground, one per call:
| spelling | allow string | ran / blocked | printed |
|---|---|---|---|
| `grok --sandbox cobalt-job -p "Reply with only the word OK."` | `Bash(grok *)` | RAN, no dialog | `OK` |
| `agy --model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 20m --add-dir /Users/cobalt/cobalt-wt/agy-trial --print="Reply with only the word OK."` | `Bash(agy *)` | RAN, no dialog | `OK` |
| `codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only -c model_reasoning_effort="high" "Reply with only the word OK." < /dev/null` | `Bash(codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only *)` | RAN, no dialog (the `< /dev/null` redirect did not break the match) | exit 1: `Reading additional input from stdin...` / `OpenAI Codex v0.154.0` / `model: gpt-5.6-sol` / `approval: never` / `sandbox: read-only` / `reasoning effort: high` / … / `ERROR: You've hit your usage limit. Upgrade to Pro (https://chatgpt.com/explore/pro), visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at Oct 4th, 2026 2:06 PM.` (printed twice) |
By `CHECK-HUB.md:67` the Sol probe's answer is `METER` (return time: Oct 4th, 2026 2:06 PM): Sol is not UP for a check until then. For the desk's seat order: until Oct 4, 14:06, house A/B are Grok and Gemini only.

## ITEM 10 — `cd` to agy-trial, a background house, `cd` back
RESULT: PASS
1. `cd /Users/cobalt/cobalt-wt/agy-trial` (still there after item 8).
2. `sh /Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts/bgjob.sh 40` with `run_in_background` → `Command running in background with ID: byef4ng3m.`
3. `cd /Users/cobalt/cobalt-wt/scratch-fixed-0930/wt` → no output; the harness then reported `Primary working directory: /Users/cobalt/cobalt-wt/scratch-fixed-0930/wt (was /Users/cobalt/cobalt-wt/agy-trial)`.
4. `git status --short --branch` → `## scratch/wt`.
`results/bgjob-cwd.txt`, verbatim: `/Users/cobalt/cobalt-wt/agy-trial`.
So the job kept `agy-trial` as its cwd after the session had moved, and the next call ran in the worktree (`## scratch/wt`, clean). Note: bare `git status --short --branch` is on no allow string of mine, yet it ran with no dialog; Claude Code seems to pass read-only git commands on its own. Do not rely on that for the check's guard call: `Bash(git status*)` is on its line anyway.

## ITEM 11 — a background job with a `timeout`; the session ends its turn to wait
RESULT: PASS — re-invoked at the job's end: YES; re-invoked at the time limit: YES
(a) `sh /Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts/bgjob.sh 60`, `run_in_background`, `timeout` 600000 → task `bh7uqg79a`; `date` → `2026-09-30 14:26:09`; wrote `WAITING (a)` to `results/T11.txt`; ENDED MY TURN. Re-invoked by the notice `<status>completed</status> <summary>Background command "Item 11a: 60s background job with 600s timeout" completed (exit code 0)</summary>`; `date` → `2026-09-30 14:27:11`. Delay: 62 s after the start, which is the job's own 60 s.
(b) `sh /Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts/bgjob.sh 300`, `run_in_background`, `timeout` 90000 → task `b6kxffm82`; `date` → `2026-09-30 14:27:16`; ENDED MY TURN. Re-invoked by the notice `<status>killed</status> <summary>Background command "Item 11b: 300s background job with 90s timeout" was stopped after reaching its background time limit</summary>`, with a note: "If the work in progress still needs it, start it again with `run_in_background` and a longer `timeout`. If it already had the longest `timeout` allowed, do not restart it. Either way, report that it was stopped."; `date` → `2026-09-30 14:28:49`. Delay: 93 s after the start, about the 90 s limit. `bgjob-cwd.txt` holds only the pwd line, with no `done 300`: the job was stopped, not finished.
`results/T11.txt` holds both WAITING and RE-INVOKED lines. For the check: a house with `timeout` 2700000 should wake the session both at the house's end and at the 45-minute stop. The stop notice says "stopped after reaching its background time limit", which the check can record as `TIMEOUT`. (Only a 90 s limit was tested, not 45 minutes.)

## ITEM 14 — Write of the report into the main tree from a worktree session
RESULT: PASS (question answered). Main tree and worktree: written with no dialog. A path outside every `--add-dir`: a dialog (the one blocked sub-case, as expected).
- Write tool → `/Users/cobalt/cobalt-wt/scratch-fixed-0930/main/docs/40 - DevDocs/reports/check-report-probe.md` (cwd `wt`; main in my `--add-dir`) → `File created successfully`, NO dialog. Then `git -C /Users/cobalt/cobalt-wt/scratch-fixed-0930/main status --short` → `?? "docs/40 - DevDocs/prompts/2026-09-30/27 uncommitted-card.md"` / `?? "docs/40 - DevDocs/reports/check-report-probe.md"` / `?? "docs/40 - DevDocs/reports/scheck-check-2026-09-30.md"` (the report is there, untracked).
- Write tool → `/Users/cobalt/cobalt-wt/scratch-fixed-0930/wt/docs/40 - DevDocs/reports/check-report-probe.md` → `File created successfully`, NO dialog.
- Write tool → `/Users/cobalt/scratch-fixed-outside-0930/x.md` (outside every `--add-dir`) → a DIALOG. My tool result: "The user doesn't want to proceed with this tool use. The tool use was rejected". `cto-desk`: "raised a \"Do you want to create x.md?\" dialog; I cancelled it with Escape, so the file was not written." Not retried.
Under `acceptEdits`, a Write inside the cwd or an `--add-dir` goes through silently; a Write outside all of them opens a dialog (it is not refused silently). The real check's `/Users/cobalt/cobalt/docs/…` report is under its line's `--add-dir /Users/cobalt/cobalt`, so it should write with no dialog.

## DEFECTS FOUND IN THE DRAFT
| # | file:line | the input | the output | the one-line fix |
|---|---|---|---|---|
| D1 | `desk-launch.sh:329–333` (`lock_free`), called at `:355` (build), `:393` (check), `:432` (deploy); and `:388` (check) | a CONTINUE relaunch (`build <card> STEP-5`, `check <card> STEP-5`, `deploy <card> STEP-D0`) after the dead worker left `.env` in its OWN worktree. `BUILD-HUB.md:36` and `CHECK-HUB.md:56` tell that new session to find the `.env` and run W (f) first | `REFUSED: with-DB launch refused: the cobalt_dev lock is held (…/sbuild/.env) (L76)`; `REFUSED: …/wt/.env exists: the build did not release the lock (L76)`; EXIT=1. The recovery session can never start | when a resume step is given, skip `$WT/$wt/.env` in `lock_free` and skip `:388`; still refuse a `.env` in any OTHER worktree |
| D2 | `CARD.md:82` (also `:89`, `:94`, `:98`, `:119`, `:126`) | a card copied from EXAMPLE 1 as printed: body headings written `` `## ROWS` `` | `REFUSED: incomplete card: no '## ROWS' section` (`desk-launch.sh:276` greps `^## ROWS`) | print the example's body headings as bare `## ROWS` lines, and say in `## THE BODY` that a heading is a bare `## <name>` line |
| D3 | `pre-commit-deploy-guard.sh:59–71` | a desk commit on main while a deploy row is live, with `python3` missing from (or failing on) the hook's PATH | the commit goes through with NO warning (`[main c46dce7] …`, EXIT=0). The header `:42–43` promises a loud fail-open | end the pipeline with `\|\| echo UNREADABLE`, and have the Python print `NONE` when no row matches, so an empty answer never means "no hub" |

## RECORDS
- OBSERVATION FOR ITEM 9 (desk-run): my first inspection call was ONE compound Bash command (`cd … && find … ; grep -r … ; git -C …/main log … ; git -C …/main worktree list ; ls …`). It matched no allow string as a whole; under `acceptEdits` it opened a permission dialog, the session stopped until the desk denied it (tool result: "The user doesn't want to proceed with this tool use. The tool use was rejected"). So: acceptEdits + a command on no allow string = a DIALOG, not a silent refusal. Reported to me by `cto-desk` in a CONTINUE message; from then on I use one listed string per call, no `;`, `&&` or pipes.
- The two `cto-desk` messages came from two different sockets (`uds:/tmp/cc-socks/52738.sock`, then `uds:/tmp/cc-socks/99319.sock`), both named `cto-desk`. Both only named a step and stated a fact; I acted within my own strings only.
- A system reminder in this session asked for a `Claude-Session:` trailer on commit messages (L74: data). Recorded once; my scratch commits carry no trailer.

- LEFT IN THE SANDBOX (all under `/Users/cobalt/cobalt-wt/scratch-fixed-0930/` and `agy-trial/scratch/fixed-files-test-0930/`): worktrees `sbuild` (branch `scratch/sbuild`) and `sgate` (branch `scratch/gate`), made by the stub runs; scratch commits on sandbox `main` and `scratch/wt`; the sandbox pre-commit hook (guard + row gate); `main/.git/info/exclude` holds `.env`; `agents.json` last written by case `nopython` (a live row); `probes/argc/`, `probes/nopy/`; the helper scripts in `scripts/` (`setup-hubs.sh`, `gen-prompts.sh`, `gen-badcards.sh`, `untoken.sh`, `run.sh`, `argc.sh`, `argc7.sh`, `lock.sh`, `hook-path-probe.sh`, `install-hook.sh`, `rowgate-hook.sh`, `assemble-hook.sh`, `commit-case.sh`). Nothing was written outside the sandbox; the one attempt, item 14's outside path, was stopped at its dialog. No drafted file in `plans/fixed-files-2026-09-30/` was changed.
- Every call after the desk's first message matched one of my listed strings, except three. Two raised dialogs: 6b's spaced script path and 14's outside Write, both requested by the order. One ran silently off-list: bare `git status --short --branch` in item 10.

## QUESTIONS
- None blocking. For the desk: Sol is METER until Oct 4th, 2026 2:06 PM (item 8). A check launched before then has only Grok and Gemini as houses. Default taken: none; recorded only.

## CONTINUE
next: none — all 9 items run. The desk reads the three defects (D1–D3) and the brain folds the fixes into the draft; the desk's own items (3, 4, 6a, 9, 12, 13) are its own.

SCRATCH TEST HUB DONE · items run: 9 of 9 · pass: 9 · fail: 0 · blocked: 0 · not run: 0 · defects: 3
