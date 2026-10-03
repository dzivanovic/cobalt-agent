# BRAIN — Claude Code hooks and mods against our process (review, 2026-10-03, about 07:0x ET)

His question: Anthropic shipped "mods" and has had hooks for a while; would they help, and are we over-engineering instead of using the vendor's means? Read-only; nothing written outside this file. Source for the mod facts: the `plugin-authoring` skill text of this build (2.1.287), loaded in the brain session; its long reference and the 14,000-line API file were NOT read (context budget): a design card must read them before anything is built.

## §0 Headline
1. We already use hooks: `bare-guard.py` is a PreToolUse hook. What hooks and mods add is the ability to enforce a rule AT THE TOOL BOUNDARY, deterministically, with no model turn and nothing on the read path. That is exactly what THE STANDARD 12 wants ("rules live in scripts, not on the read path") — a hook is the stronger home for the refusal half of it.
2. Partly over-engineered, yes: the fixed files carry typed procedures and long per-kind allow lists that re-implement, in prose and permission strings, what a `tool.call` hook does in one function. The step scripts (`gate.sh`, `authorize.sh`, …), the cards, the fresh-seat check, the three suites and the lock are NOT over-engineering: they are the process, and a hook cannot replace a test run or a judgment.
3. Order: finish this weekend's cards as ruled and measure; then one read-only design card on the harness; then a phase-1 card that moves the REFUSALS into a hook module and leaves everything else in place. Phase 1 removes text from the fixed files and strings from the lines; it adds no process.
4. Risk: mods are new in this build; a mod runs inside the seat's process (a bug there is a blocked seat, reported only as a dim transcript line or in the debug log); a mod dies with its session, so the runner and the close timer stay shell and launchd. The mod API is large; the design card reads it, the brain does not guess at it.

## What the harness offers (from the skill text)
| vendor means | what it does | our thing it could replace or carry |
|---|---|---|
| settings `hooks` (PreToolUse etc., a shell command on JSON stdin, exit 2 blocks) | a rule per tool call, no model turn | `bare-guard.py` (in use); every "never typed" sentence of the fixed files; the production-string deny; the `.env` never-read rule |
| mod `on('tool.call', {tool}, hook)` → `{ deny }` or `next({...e, rewritten})` | the same, typed, in-process, with state and the session's facts | the per-kind allow lists shrink to the engine's own permission plus one policy module keyed by the seat's kind |
| mod `prompt.compose` (system-prompt sections) | adds or replaces a system-prompt section per session | the `--append-system-prompt` flag of card `02` A4 (the bare-command sentence) |
| mod `session.start` + `$.process` / `$.fs` | run a script at start, read files | AUTHORIZATION and PREFLIGHT could run once at start and be shown to the worker as a table — but L35 ("every claim is tool output") must say whether a hook's output counts; a law question for the close, not a card |
| mod `ui.open` pane, `AbovePrompt` band, `$.ui.status`, `$.ui.toast` | a live view in the desk's terminal | the desk's watch turns (`desk-watch.sh`, `wait-stop-line.sh`): a pane listing each hub's last line, the lock holder, the level — zero tokens per look |
| mod `$.clock` | timers inside the session | NOT the close timer (dies with the session; launchd stays) |
| mod `$.command.register` | a slash command answered by the mod | `/radar`-style reads for the desk; the `MEASURE` request as a command instead of a message |
| mod `$.tool`, `$.agent` | a tool the model calls; spawning subagents | not for us now: our seats are launched by `desk-launch.sh` on purpose (R72, one launcher, one line) |

## What is over-engineered, named
- The "never typed" lists and ONE-command-per-call prose in `BUILD-HUB.md` line 14 and 29, `CHECK-HUB.md` line 32 and 50: a hook does this in one place for every seat. After phase 1 those sentences become one line: "the guard refuses it".
- The per-kind allow strings for the dev `db` verbs, the `.env` `cp`/`rm` pair, the pytest prefixes: the engine's allow list stays as the outer wall, but a kind-aware hook can be the inner one, so the lines stop growing per verb (his class ruling, direction row 2, already points this way).
- The TREE STATE row and its proofs: already going (card `02`).
- NOT over-engineered: cards, the fresh Opus check, the three suites, the lock, the scripts, the judge seat, the words file and the rulings. Those exist because models err in judgment, not in typing; hooks fix typing.

## What hooks cannot do
- Run a test, prove a tree equal, judge a finding, decide a seam. They stop a wrong call; they do not make a right one.
- Survive the session: a runner, a timer, a close must live outside the seat.
- Replace the launcher: a mod loads into a session the launcher started.

## Proposed order (after the measure, his word first)
1. DESIGN CARD (read-only, one Opus reader): reads `plugin-authoring/reference.md`, the API file's `tool.call`, `prompt.compose`, `session.start`, `ui.render` declarations, our four fixed files and `STANDING-LIST.md`; produces the hook policy table: rule · today's home (sentence or string) · hook event · deny or rewrite · test. Names what L35 and L29 say about hook output.
2. PHASE 1 CARD `cobalt-guard`: one mod (or plain settings hooks if mods prove unstable) with the refusals: compound commands (the present `bare-guard.py`), any `COBALT_ENV=production` from a build / check / devfix seat, any read of a `.env`, a `git add -A` / `.` / bare `commit`, a report stop line written while `.env` is on disk or a migration above `0013` is applied (reads the lock dir), a Write outside the seat's fence. Tested with `claude plugin test`. The fixed files lose the matching sentences; the lines lose nothing yet.
3. PHASE 2 CARD, desk visibility: the jobs pane and status line for the desk seat; the MEASURE as a command. Measured by desk turns per job before and after.
4. His installs: the mod loads by `--plugin-dir` on the launch lines (a flag, not a permission string; the design card says whether it is a new class).

## THE MODS TO LOOK INTO, best first (his ask, 07:1x ET)
| # | mod | event / noun | offloads | tokens saved |
|---|---|---|---|---|
| 1 | `cobalt-guard` | `tool.call` deny / rewrite | every "never typed" rule, the production deny for build seats, `.env` reads, bare commits, a stop line while the lock is held or a migration is applied | the refusal turns and the re-reads of those sentences in every seat |
| 2 | `cobalt-seat` | `prompt.compose`, `session.start` | the system-prompt sentence (replaces the `--append-system-prompt` flag); the kind's standing rules as a section instead of fixed-file prose; `authorize.sh` / `preflight.sh` run at start and shown as a table (pending L35's word on hook output) | 6–8 AUTHORIZATION and 15–25 PREFLIGHT turns per seat |
| 3 | `desk-board` | `ui.open` pane, `AbovePrompt` band, `$.ui.status`, `$.fs`, `$.clock` | the desk's watch: each hub's last line, the lock holder and holder time, the dev level, the lock queue, the meter | most of `desk-watch.sh` and the ~7 desk calls per stage |
| 4 | `desk-commands` | `$.command.register` + `command.run` | `/measure`, `/row <text>` (desk-row + commit), `/done <job>`, `/launch <kind> <card>` calling the scripts | the typed desk calls and their permission round-trips |
| 5 | `stop-line-check` | `tool.call` on Write / Edit of a report | the stop-line shape and the pinned last line checked at write time; a `«FILL` token in a card refused at write, not at launch | a relaunch per malformed card or report |
| 6 | `judge-inbox` | `$.fs` watch + `$.ui.toast` | the brain sees a new `## DECISIONS` section the moment a report stops with `decisions: ≥1`, without a desk message | one desk message per judge request |
Not a mod: the runner (`job-run.sh`) and the close timer (launchd) — they must outlive a session.

## OPERATIONS A HOOK CAN TAKE (his ask, 07:2x ET; his four items are 1, 2, 3 and 20–23)
Rule: a hook takes an operation when its answer is a FACT or a CLOSED LIST, never a judgment. Event names are the mod's; the same is possible with settings hooks where the row says so. "Deny" sends the reason back to the model as a message, not a refusal (the NOT A REFUSAL line); "rewrite" changes the call before it runs.

| # | operation | event | deny / rewrite / show | replaces today |
|---|---|---|---|---|
| 1 | THE SEAT READS ITS OWN SIZE: a timer runs `desk-context.sh <id> <line>` and shows the number in the status line; at the seat's line (desk 250,000, brain 500,000) a toast and a line into the report's `## RECORDS` | `$.clock`, `$.process`, `$.ui.status` | show | the MEASURE message to the desk and its reply |
| 2 | THE STANDING MODEL PER SEAT: a `claude --bg … --model <x>` launch is rewritten to the standing model of that kind from one table (desk Opus 5.5, brain Fable 5.1, Grok `grok-4.7`, R34 / R131 / 10-03 R3); a `grok` call without `-m` gets it | `tool.call` Bash, rewrite | rewrite | the model and `-m` words on every launch line and in the hub text |
| 3 | COMPOUND OR UNAPPROVED COMMAND: `&&`, `;`, `\|`, redirect, newline, `$(…)` outside quotes → deny with the resend line (today's `bare-guard.py`); a prefix outside the seat's kind table → deny naming the class it would need | `tool.call` Bash, deny | deny | `bare-guard.py`; the "never typed" lists; part of the per-kind allow strings |
| 4 | PRODUCTION FROM A NON-DEPLOY SEAT: `COBALT_ENV=production`, `--prod`, `cobalt_brain` in any call from build / check / devfix / brain → deny | `tool.call`, deny | deny | the `--disallowedTools` deny string and its prose |
| 5 | `.env` NEVER READ: `cat`, `grep`, `sed`, `Read` of any path ending `/.env` → deny | `tool.call` Bash + Read, deny | deny | L4 / L41 sentences |
| 6 | GIT SHAPE: `git add -A` / `.`; a bare `git commit`; a commit without the explicit `-- <paths>`; `git push` from a worker; `git merge` / `rebase` / `reset` / `checkout` / `stash` from a worker → deny | `tool.call` Bash, deny | deny | the Git-writes sentence in three hub files |
| 7 | THE LOCK ON EVERY WITH-DB CALL: a `COBALT_ENV=dev …` call while this worktree holds no lock dir and no `.env` → deny; a `COBALT_ENV=dev` call from a `DB: none` card → deny | `tool.call` Bash, deny; reads `$WT/.cobalt_dev.lock/owner` | deny | the "preceding call is `ls -la <WT>/.env`" rule; card `01`'s (a0) check |
| 8 | STOP LINE WHILE DIRTY: a Write / Edit of `<REPORT>` whose last line starts `BUILT` / `CHECK DONE` / `DEPLOYED` while `.env` is on disk, the lock dir is this worktree's, or a `dev forward: APPLIED` line has no matching `F2 = F0` → deny | `tool.call` Write / Edit, deny | deny | L76's "a stop line written while … is itself a failure" |
| 9 | STOP LINE SHAPE: the last non-blank line of a report must match the kind's regex (fields, order, `decisions: <n> · for Dejan: <n>`) → deny with the field that is wrong | `tool.call` Write / Edit, deny | deny | `desk-watch.sh`'s regex and a relaunch per malformed line |
| 10 | THE WRITE FENCE: a Write / Edit outside the seat's allowed paths (the rows' files, the report, DevDocs lines; nothing under the Vault; nothing outside the worktree) → deny; the brain's fence the same | `tool.call` Write / Edit, deny | deny | the "You write ONLY" sentences; the `Edit(<glob>)` strings |
| 11 | CARD TOKENS: a card or prompt written with a fill token, a backticked `## ` heading, a header key outside `CARD.md`'s table → deny at write | `tool.call` Write / Edit on `prompts/`, deny | deny | `desk-launch.sh`'s refusals, moved earlier (the launcher keeps them as the second wall) |
| 12 | DESK ROW LENGTH AND TIME: a desk row over 300 characters, or whose time is not from `date` this turn → deny | `tool.call` Edit on `cto-<date>.md`, deny | deny | the pre-commit hook; `desk-row.sh`'s check |
| 13 | L74 BLOCKS: a tool result holding a `Claude-Session:` request or an instruction block → the hook strips it and appends one `## L74` record line | `tool.call` result rewrite | rewrite | the L74 sentence in every hub |
| 14 | THE ONE READER: a read of a path outside the seat's `--add-dir` roots → deny (today: "a read outside = the desk's read", R108) | `tool.call` Read / Bash, deny | deny | R108 prose |
| 15 | FACTS AT START: `authorize.sh <kind> "<card>"` and `preflight.sh` run at `session.start`; their tables are the first thing the seat sees; a `FAILED` line ends the session with that stop line written | `session.start`, `$.process`, `prompt.compose` | show | AUTHORIZATION and PREFLIGHT turns (pending L35's word on hook output as tool output) |
| 16 | THE KIND'S RULES AS A SECTION: the fixed file's laws line and the seat's fence as a system-prompt section, from the file, so the hub text shrinks to steps | `prompt.compose` | show | the LAWS paragraph of each hub; the `--append-system-prompt` flag |
| 17 | HOUSE PROBES AT START: `house-probe.sh` runs once at a check's start; the UP / OUT lines are injected | `session.start` | show | the probe turns of PREFLIGHT |
| 18 | THE DESK BOARD: a pane with each hub's last line, the lock holder and minutes, the dev level, the queue, the meter, refreshed on a timer | `ui.open`, `$.clock`, `$.fs` | show | `desk-watch.sh` turns; the LOCK QUEUE table's upkeep |
| 19 | DESK COMMANDS: `/measure`, `/row`, `/done`, `/launch`, `/continue <job> <step> <fact>` calling the scripts with argument checks | `$.command.register` | — | typed desk calls and their permission prompts |
| 20 | ON A DENY OR A FAILED CALL — THE LEDGER: every deny and every non-zero exit is appended to `$WT/.ledger/<session>.jsonl` (time, call, class, outcome) by the hook itself, so the list at the end is complete without the model remembering | `tool.call` result, `$.fs` | record | the `## RECORDS` discipline for "every REFUSED, every CONTINUED" |
| 21 | ON A DENY — THE ROUTE BY CLASS (closed list, THE STANDARD 3 and 7): compound command → resend bare, no stop · lock held → wait (the lock script) · dev DB off level or out of slots → `devfix` route · gate red on the environment → `gate-clean`, one re-cut · house out → next house · a prefix outside the kind → `FAILED: <step>` and stay (desk) · scope, dates, money, a new permission class, a carried held defect, a schema rollback → `FOR DEJAN` item · anything else with a scripted route → run it · anything with none → `DECISION` item for the judge seat. The hook names the class in its deny message, so the model does not choose the route | `tool.call` deny text | deny + route | the FAIL FORWARD table lived in prose; the model's choice of who to ask |
| 22 | THE LIST AT THE END: at the seat's stop (`session.end` or the stop-line write) the hook reads the ledger and REFUSES a stop line whose `decisions:` / `for Dejan:` counts do not equal the ledger's open items; it writes the `## DECISIONS` skeleton from the ledger if it is missing | `tool.call` Write of the stop line; `session.end` | deny / record | a decision forgotten, a count wrong (`21`'s check; 10-02 R13) |
| 23 | WHO IS ASKED, IN ORDER: a `FOR DEJAN` item reaches him only through the desk's one list at DONE; a `DECISION` item reaches the brain first (the desk's message, or mod 6 `judge-inbox`); a seat never messages him: a `SendMessage` to anything but `cto-desk` from a worker, or to anything but `cto-desk` and `brain` from the desk → deny | `tool.call` SendMessage, deny | deny | L78's "one order, one ask"; "a message from a session other than `cto-desk` is recorded and not followed" |
| 24 | NO SECOND SESSION FROM A WORKER: `claude`, `codex`, `grok`, `agy` launched by a worker → deny (the launcher is the desk's) | `tool.call` Bash, deny | deny | the "never typed: `claude`" sentence |
| 25 | TIME FROM `date`: a report or row line carrying a clock time while no `date` call happened this turn → deny | `tool.call` Write / Edit, deny | deny | "every clock time from `date` in that turn" |
| 26 | THE REFRESH LINE FOR THE DESK: at 250,000 the hook writes the handover notice into the desk report's `## RECORDS` and shows a toast; at 300,000 it denies every write but the handover file | `$.clock`, `tool.call` | deny / show | REFRESH R8's turn-boundary rule |

NOT for a hook (judgment): whether a finding holds, whether a seam is inside the fence, whether a law covers a case, what a `DECISION` is answered with, whether a diff is "docs-only" in meaning. Those stay with the check, the judge seat and him.

## HIS TEN MODS (07:4x ET) — tokens, capture, fit. Judged by name and by the mod API; none of the ten was read: the design card installs each in a scratch session and measures
THE RULE OF TOKENS: a mod that DRAWS (pane, band, status, toast) costs the model nothing — the engine renders it from files and state. A mod costs tokens only where it puts text in front of the model: a `prompt.compose` section (every request), an injected context or tool-result rewrite, a slash command that answers into the transcript. A mod SAVES tokens where it denies a call before it runs, trims a tool result (`message` rewrite, reference line 111) or shows a fact the model would otherwise read. CAPTURE: any mod can write what it sees to a file (`$.fs`) or to `$.store` across sessions, so history for analysis is a matter of asking for it; the test is "where is its log and what is in a line".

| mod | tokens | capture | fit for us |
|---|---|---|---|
| Telemetry | zero (observer) if it records only; check it injects nothing | yes by design: calls, tokens, timings per session | HIGH: the gain measure and `job-stats` for free, every day |
| Flight Recorder (live view of every call) | zero if drawn from the transcript | yes if it writes its stream | HIGH for his eyes and the desk's watch; replaces tab-hopping |
| Auto Handoff | costs at the threshold: a model-written handover (one long turn); may save a stuck seat | the handover file | BIG IF: it must call `desk-launch.sh` (R72), respect "brain stopped only on his word" (R76), take the kind's line (desk 250,000, brain 500,000) and write in our handover shape (card `07` B1). Trial on the brain seat first, beside a hand-written handover, and compare |
| Model Router | zero if a table; tokens and RISK if it classifies tasks with a model call | its decisions must be logged | ONLY as the standing table (op 14): a router that picks models by its own judgment crosses R34 / R71 / R73 (model-by-complexity parked) |
| Output Tray | zero (collects files the seat wrote) | built in | medium: the desk's reports and cards in one place |
| Changes Receipt | zero if computed from `git diff`; tokens if the model writes the summary | the receipt file | medium: could feed `card-fill.sh` and `## FOR THE CHECK`; must be the git kind |
| Blast Radius | zero if drawn from the diff; tokens if injected | — | medium for the desk's `DB: none` and RESTARTS reading; a visual check, never the proof (the build's `git diff --name-only` stays the proof) |
| DomainLoader | SAVES if it replaces broad reads with a domain's set; COSTS if it injects a summary every request | — | low for seats: ours already read a fixed small set (READ AT START); maybe for the design and tribunal prompts |
| Repo Heatmap | zero (visual) | — | his eyes; no process value |
| Session Bookmark | zero (state) | — | his eyes; no process value |

REMOVING MODS PER SESSION (reference line 68): a mod loads only where the launch names it, `claude --plugin-dir <folder>` once per mod, or the folders in `CLAUDE_CODE_PLUGIN_DIRS` (the `env` block of `~/.claude/settings.json`, never a project's). A session launched without the flag has none; the dev-mods folder loads only after the session's own "enable hot reloading" answer. So each kind's launch line carries its own mod set (Telemetry on every seat; the visual ones on the desk and the brain; nothing on a Grok or Gemini run), and a `--plugin-dir` is a launch-line flag the design card classifies (a permission class or not: his).

## RULED, brain session 10-03 about 07:5x ET — his words verbatim
"also model picker will need to wait for two tasks, we need to do as you said model-by-complexity tribunal and also JEV typesave ai picker and then shadow run for JEV with antroic seat so we improve JEV until 80% and then let it be the decision maker. For auto handoff of brain - if you want to test there first, I already allow brain to decide if it needs it's own restart, so this can be tested there. For others if they are high value but no burn, we need to find time to install them"
- MODEL ROUTER: waits for (1) the model-by-complexity tribunal (parked ≥1 week, R73) and (2) the JEV type-safe AI picker; then a shadow run of JEV beside an Anthropic seat until JEV agrees at 80%; then JEV is the decision maker. Until then the model per seat is the standing table (op 14) and nothing routes.
- AUTO HANDOFF: tested on the brain seat first; the brain already decides its own restart (his standing allowance; his 10-03 line of 500,000). The trial compares the mod's handover with the brain's hand-written one on the same session.
- HIGH VALUE, NO BURN (Telemetry, Flight Recorder with the house recorder row, Output Tray): find the time to install them — an install card after the weekend's measure, behind the design card; no model-side text in any of them.
- Rows for the desk: three `HIS RULING · APPROVED` rows (router gate; auto-handoff trial on the brain; install the no-burn mods), words to the words file.

## DECISIONS
1. FOR DEJAN — timing: after the weekend's measure, as he said. Recommendation: the design card Monday beside the ladder; phase 1 the same week if the design holds.
2. FOR DEJAN — scope of phase 1: refusals only; no pane, no runner, no timer in the mod.
3. Mine, his veto — the shell runner and launchd timer stay as built regardless of mods.

## RECORDS
- Not read: `plugin-authoring/reference.md`, the API types file. Every "could" above is from the skill's summary table and must be verified by the design card.
- R71 (no new vendors) is not touched: this is the vendor we already run on.
