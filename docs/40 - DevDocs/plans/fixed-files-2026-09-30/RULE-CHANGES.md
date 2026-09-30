# RULE-CHANGES — every rule the new process contradicts, with its new text (DRAFT 2026-09-30, fourth pass · NOTHING HERE IS FOLDED)

FOR DEJAN TO SEE. His ruling `cto-2026-09-30.md` R45: he agrees with all the brain's recommendations; every rule that contradicts the new process is changed to match it; he is not asked rule by rule. This is the list: one row per rule. The desk folds it (L58: replaced LAWS wording moves to `LAWS-HISTORY.md`, replaced memory lines to `_retired/<file>.md`); a drafter folded nothing. Only a row the brain finds saying more or less than what was ruled comes back to him.

HOW TO READ A ROW: the rule · HOME `file:line` (read from the real file on 2026-09-30) · CARRIES = the section of `reports/brain-desk-review-2026-09-30.md` it rests on · TODAY = the text as it stands, verbatim · NEW = the exact text to fold. Where TODAY quotes part of a line, the rest of that line stays byte for byte. `NEW ON THE LIST` = a rule in conflict that the brain's list did not name. A block fenced `start-old` / `start-new` sits in a file the desk reads at start; its bytes are counted in `## START-SET` at the end.

Paths: `M` = `/Users/cobalt/Vault/Think/6 - Permanent/Memory` · `P` = `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts` · LAWS = `M/LAWS.md` · CHECKLIST = `M/topics/cto-desk-checklist.md` · CONTRACT = `M/topics/cto-desk-contract.md` · UL = `P/UNATTENDED-LAUNCH.md` · WAKE = `P/CTO-DESK-WAKEUP.md`. Section names: READ OF THE SCRATCH TEST, RULED — THE NIGHTLY CLOSE, READ OF THE THIRD PASS (fourth pass); THIRD PASS, RULED CHECK FLOW, READ OF THE DRAFT, RULED WORKER ENDINGS, READ OF LOOP 2, RULED PROCESS, RECOMMENDATIONS, RULED — the 9:30 override ends.

## LAWS

### 1 · L67 — build checks: the flow, the seat order, Gemini; the deployment floor
HOME: `LAWS:334` (heading), `:335`, `:338`, `:340`, Index `:77` · CARRIES: RULED CHECK FLOW; THIRD PASS items 1 and 4; READ OF LOOP 2 gap 3.
TODAY `:334`:
~~~text
### L67 Four-house tribunal for every design; three checkers for every build; never fewer than one other house
~~~
NEW `:334` (the heading is a link target: the Index line changes in the same edit, checklist M4; `grep -r -l -F "LAWS#L67"` over `M` finds no other link):
~~~text
### L67 Four-house tribunal for every design; the check flow for every build; never fewer than one other house
~~~
TODAY Index `:77`:
~~~start-old
- [[LAWS#L67 Four-house tribunal for every design; three checkers for every build; never fewer than one other house]] — tribunals, checker seats, the round cap; owner items are only his.
~~~
NEW Index `:77`:
~~~start-new
- [[LAWS#L67 Four-house tribunal for every design; the check flow for every build; never fewer than one other house]] — tribunals, the build check flow; owner items are only his.
~~~
TODAY `:335`, from its third sentence to its end:
~~~text
Every DEVELOPMENT (build) is checked by at least THREE members of the tribunal. The exception is an EMERGENCY design or development while more than one house is unavailable; then fewer checkers are allowed. The FLOOR holds at all times: any design, development or DEPLOYMENT is checked by at least ONE house other than its author, and by more than one additional house when the meters allow (L47: the meter is a precondition, checked before asking). This includes the CTO desk's own deploy, rebase and re-land prompts.
~~~
NEW `:335`, the same span, followed by one new paragraph:
~~~text
Every DEVELOPMENT (build) is checked by the BUILD CHECK FLOW below. The exception is an EMERGENCY design while more than one house is unavailable; then fewer houses are allowed. The FLOOR holds at all times: any design or development is checked by at least ONE house other than its author, a design by more than one additional house when the meters allow (L47: the meter is a precondition, checked before asking). A DEPLOYMENT's floor is: the build check of every branch it carries, plus ONE read of the fixed deploy file `DEPLOY-HUB.md` by a house other than its author, at its install and at each change of it; no read per deploy. A one-off deploy, rebase or re-land prompt of the CTO desk's, outside the fixed file, is read by one other house before it runs.
BUILD CHECK FLOW (the procedure is `docs/40 - DevDocs/prompts/CHECK-HUB.md`). The check IS one fresh Opus session, never the builder. It starts HOUSE A, one house outside Anthropic, which reads the card, the diff and the files; a house cannot run a command, so a house finding is a test it wrote or an exact command, and a claim with nothing runnable is dropped. While house A runs, the Opus session reads the same set and writes its own findings; only then does it read house A's. It judges every finding by running it and fixes what holds. It is done when every held finding's test passes, the three suites are green (L68) and each new test was shown red first. Nothing open → the check is done. Something open — a finding it could not settle, or one it rejects although its test runs red for the stated reason — → a SECOND fresh Opus session starts HOUSE B, a different house, which reads the diff with the fixes and both findings lists and adds its own; that session judges and fixes the same way. No further house and no third pass: what no test can catch ships and goes on the follow-up list. MANDATORY HOUSE B: a build that writes his vault notes or changes sizing runs the second pass even when nothing is open. SEAT ORDER, by the meter probe at launch: OpenAI up → house A = OpenAI, house B = Grok; OpenAI out → A = Grok, B = Gemini; OpenAI and Grok both out → A = Gemini and no house B, and a mandatory-B build then waits for a meter unless he overrules it per case. Gemini never sits ahead of a house that is up. A build check has no rounds (L39) and no classifier (L75), no packet and no byte ceiling.
~~~
TODAY `:338`, its first sentence:
~~~text
ROUNDS AND THE METER FLOOR: each tribunal house gets at most THREE rounds, for as long as the houses have meter; when meters run out the tribunal may shrink, but never below TWO houses: the proposer and one other.
~~~
NEW `:338`, that sentence:
~~~text
ROUNDS AND THE METER FLOOR (design tribunals only; a build check has no rounds): each tribunal house gets at most THREE rounds, for as long as the houses have meter; when meters run out the tribunal may shrink, but never below TWO houses: the proposer and one other.
~~~
TODAY `:340`, whole:
~~~text
CHECKER SEATS BY KIND OF WORK: DESIGNS and NEW BUILDS — a proposal, a tribunal that rules on a design, a derive, and the check of a new build — seat Fable (Anthropic) · Astra (OpenAI) · Grok. EVERY OTHER CHECK — a fix round, a code check of a finished build, a deploy-prompt read — seats Opus (Anthropic) · Sol (OpenAI, `gpt-5.6-sol`) · Grok; when the OpenAI meter is short, Opus + Grok. NEVER one house: every code check has an Anthropic seat and at least one other house. Gemini is an optional FOURTH seat on a NEW design tribunal only, when its meter is free; it reads no code check and no deploy read, and each derive states whether a Gemini finding held. Sol and Astra draw on the same Codex allowance — the probe stays a preflight. This checker-seat schedule applies to prompts drafted from 2026-09-23 18:10 ET; prompts drafted earlier run as written. The reduced seats for code checks and deploy reads apply only while the work follows L68's GATE EARLY clause. Desk readings, not his words: a "new build" is the first check of a new feature's build, everything after it is "other"; the Anthropic seat named "Fable" runs as Opus 5.5 until his word.
~~~
NEW `:340`, whole:
~~~text
SEATS BY KIND OF WORK: DESIGNS — a proposal, a tribunal that rules on a design, a derive — seat Fable (Anthropic) · Astra (OpenAI) · Grok; Gemini is an optional FOURTH seat on a NEW design tribunal, when its meter is free, and each derive states whether a Gemini finding held. A BUILD CHECK seats the BUILD CHECK FLOW above: the fresh Opus session, house A, and house B when needed; the OpenAI house there is Sol (`gpt-5.6-sol`), and Gemini sits by the seat order. NEVER one house: every build check has the Anthropic session and at least one other house. The read of `DEPLOY-HUB.md`, and of a one-off deploy, rebase or re-land prompt, is by one house other than its author that is up, in the seat order. Sol and Astra draw on the same Codex allowance — the probe stays a preflight. The build check flow applies only while the work follows L68's GATE EARLY clause. Desk reading, not his words: the Anthropic seat named "Fable" runs as Opus 5.5 until his word.
~~~

### 2 · L39 — the round cap binds councils and design tribunals only
HOME: `LAWS:240` · CARRIES: THIRD PASS item 4 ("rounds and the classifier bind design tribunals only; a build check has neither").
TODAY `:240`, its last sentence:
~~~text
A law file is never voted: an unresolved disagreement is an OPEN item for him.
~~~
NEW `:240`, that sentence and one more:
~~~text
A law file is never voted: an unresolved disagreement is an OPEN item for him. This cap binds councils and design tribunals; a build check has no turns or rounds — it is the flow of L67, one pass or two.
~~~

### 3 · L75 — the classifier binds design tribunals only
HOME: `LAWS:371`, Index `:85` · CARRIES: THIRD PASS item 4; READ OF LOOP 2 gap 3.
TODAY `:371`, whole:
~~~text
A fix round's drafter classifies every check finding — FIX, NOT REAL, UNPROVEN (L70), OUT OF SCOPE or OWNER ITEM — from the check hub's own file-check rows, before anything is built. Only FIX rows are built, each backed by a row that HOLDS; the fix widens nothing; every OWNER ITEM reaches him verbatim.
~~~
NEW `:371`, whole:
~~~text
DESIGN TRIBUNALS ONLY. Before a design is re-drafted after a tribunal round, the drafter classifies every finding of that round — FIX, NOT REAL, UNPROVEN (L70), OUT OF SCOPE or OWNER ITEM — from the tribunal hub's own file-check rows. Only FIX rows are taken, each backed by a row that HOLDS; the fix widens nothing; every OWNER ITEM reaches him verbatim. A BUILD CHECK has no classifier and no fix round: its fresh Opus session judges each finding by running it and fixes what holds (L67). A held finding it cannot fix inside the card's rows is built by a new card, each row backed by the check's run that HELD; that build widens nothing.
~~~
TODAY Index `:85`:
~~~start-old
- [[LAWS#L75 Fix rounds classify first]] — every finding is classified before a fix is built.
~~~
NEW Index `:85`:
~~~start-new
- [[LAWS#L75 Fix rounds classify first]] — design tribunals only: findings classified before a fix.
~~~

### 4 · L59 and the Preamble's last sentence — who reads what at start
HOME: `LAWS:308`, Index `:69`, Preamble `:6` · CARRIES: READ OF THE DRAFT, RULED on gap 9; THIRD PASS item 4.
TODAY `:308`, its first sentence:
~~~text
Every seat — the desk, architect, hub, builder and reviewer — reads this file's `## Preamble` and `## Index` at start, and the whole entry of every law its index card names or its task touches before it acts on that law; a seat unsure whether a law applies opens its entry.
~~~
NEW `:308`, in its place (the rest of `:308`, from "Read-and-judge seats", stays):
~~~text
The CTO desk, and a seat Dejan talks to, read this file's `## Preamble` and `## Index` at start. A worker — hub, builder, checker, drafter, a seat of a tribunal — reads neither: it reads its fixed file or prompt, its card, and `areas/cobalt.md` from `## What Cobalt is` and from `## Build rules` down; not `## NOW`, INDEX's `## start`, preferences or profile. The laws that bind a worker are the one-line list in its fixed file or prompt. Every seat reads the whole entry of a law before it acts on that law; a seat unsure whether a law applies opens its entry.
~~~
TODAY Index `:69`:
~~~start-old
- [[LAWS#L59 Worker law-reading]] — every seat reads the Preamble and this Index at start, and an entry before it acts on that law.
~~~
NEW Index `:69`:
~~~start-new
- [[LAWS#L59 Worker law-reading]] — the desk reads this Index at start; a worker, its card; an entry before acting on its law.
~~~
TODAY Preamble `:6`, its last sentence:
~~~start-old
Every house starts at its startup file → `areas/cobalt.md` → INDEX → this file's `## Preamble` and `## Index`; an entry is read when a task touches its law (L59).
~~~
NEW Preamble `:6`, that sentence:
~~~start-new
The desk starts at its wake-up file, a worker at its fixed file or prompt; an entry is read before its law is acted on (L59).
~~~

### 5 · L62 — one standing list; CONTINUE, DO NOT RESTART for builds and checks
HOME: `LAWS:317`, Index `:72` · CARRIES: RULED PROCESS item 6; READ OF LOOP 2 gap 7 (a)–(d); THIRD PASS items 2, 3 and 4.
TODAY `:317`, whole:
~~~text
Every session the desk starts gets all its permissions before it starts: a per-session allowlist, shown to him once as an approval list. No mid-run questions: a mid-run question or denial means the run FAILED and is rerun with corrected information, never patched from inside. The report file is the always-open stop channel; `FAILED: <step> — <reason>` is always a correct ending. Standard: `docs/40 - DevDocs/prompts/UNATTENDED-LAUNCH.md`.
~~~
NEW `:317`, whole:
~~~text
Every session the desk starts gets all its permissions before it starts, and every launch runs through `desk-launch.sh`. A build, a check and a deploy run on the launch line of their fixed file; those lists are ONE STANDING LIST (`STANDING-LIST.md`), approved by him once and cited in each fixed file's title; a string not on it is new and is asked for by itself. A one-off prompt (a drafter, a tribunal and its seats, a brain tab, a close hub) carries a per-session allowlist, shown to him once unless its strings are standing; it is never a write path. No mid-run questions. CONTINUE, DO NOT RESTART, for builds and checks: a command the worker added on its own that is refused is recorded and the worker goes on with its listed commands; a worker that stops on something outside itself — a held lock, stray rows, a missing fact — writes its `FAILED:` line and stays alive, the desk does not stop or remove it, and once the cause is fixed the desk sends `CONTINUE: <step>` plus the fact and the same worker resumes. That message names a step and states a fact; it never widens the job or grants anything. A NEW worker takes over at the report's `## CONTINUE` step only when the launch line itself must change, the session died, the judgment seat finds the worker misread the job, or the worker's context measures above the desk's line (250,000 tokens; his to move). A DEPLOY never continues by message: its one resume is `STEP-D0`, and inside the outage a refusal sends it to its rollback step. For a one-off prompt a mid-run question or denial still means the run FAILED and is rerun with corrected information. The report file is the always-open stop channel; `FAILED: <step> — <reason>` is always a correct ending. Standard: `docs/40 - DevDocs/prompts/UNATTENDED-LAUNCH.md` and the three fixed files.
~~~
TODAY Index `:72`:
~~~start-old
- [[LAWS#L62 Unattended launch]] — every permission before start; a mid-run question = FAILED; standing strings.
~~~
NEW Index `:72`:
~~~start-new
- [[LAWS#L62 Unattended launch]] — one standing list before start; continue, do not restart.
~~~

### 6 · L68 — "every check packet carries them"
HOME: `LAWS:347` · CARRIES: RECOMMENDATIONS 9 (packet ceilings go, his 2026-09-27 R42); RULED CHECK FLOW (no packet, no byte ceiling).
TODAY `:347`, inside its first sentence:
~~~text
without all three it is not BUILT, and every check packet carries them.
~~~
NEW `:347`, those words:
~~~text
without all three it is not BUILT, and the check reads them in the build report itself (no packet, L67); a check that commits runs the three again on its own tip.
~~~

### 7 · L19 — a fixed file plus its card is the whole prompt
HOME: `LAWS:165`–`:166`, Index `:29` · CARRIES: RECOMMENDATIONS 9; RULED PROCESS items 1–3; THIRD PASS item 4.
TODAY `:165`–`:166`:
~~~text
Every Code prompt delivered complete in one block, always; changes = full re-issue. Model tag on every prompt.
A CONTINUE relaunch is a full re-issue when the prompt file is unchanged and the only addition is ONE `CONTINUE:` prefix line naming the resume point (L47, L60). Any change to the file itself is a full re-issue of the file.
~~~
NEW `:165`–`:166`:
~~~text
Every Code prompt is complete in itself, always: for a build, a check or a deploy the whole prompt is its fixed file (`BUILD-HUB.md`, `CHECK-HUB.md`, `DEPLOY-HUB.md`) plus the job's card; a one-off prompt is one complete file. No prompt points at another prompt's blocks or binds them "with substitutions". Changes = full re-issue. Model tag on every prompt and every fixed file.
A CONTINUE relaunch is a full re-issue when the file is unchanged and the only addition is ONE `CONTINUE:` prefix line naming the resume point (L47, L60); a check's `PASS-2.` prefix is the same. Any change to the file itself is a full re-issue of the file.
~~~
TODAY Index `:29`:
~~~start-old
- [[LAWS#L19 Whole prompt]] — every prompt complete in one block with its model tag; a change = full re-issue.
~~~
NEW Index `:29`:
~~~start-new
- [[LAWS#L19 Whole prompt]] — a fixed file plus its card is the whole prompt; a change = full re-issue.
~~~

### 8 · L43 — the other-house read of a deploy prompt
HOME: `LAWS:252` · CARRIES: THIRD PASS item 4 (L61 / L43; the deployment floor under L67).
TODAY `:252`, inside its first sentence:
~~~text
the gate proven earlier that day, the deploy prompt read by houses other than its author, L66's shape.
~~~
NEW `:252`, those words:
~~~text
the gate proven by the fixed deploy file's own run before the merge (L68), that file read by one house other than its author at its install and at each change of it (L67), L66's shape.
~~~
NOTE: the window text of L43 and of L66 is NOT changed; both bind again (see NOT CHANGED at the end).

### 9 · L61 — who starts a deploy; its list
HOME: `LAWS:314`, Index `:71` · CARRIES: RULED PROCESS item 7 (deploys leave his four; a deploy launches itself; he is asked only for a carried held defect and a schema rollback); READ OF THE DRAFT gap 4; THIRD PASS items 2 and 4.
TODAY `:314`, whole:
~~~text
The desk starts every hub itself as an independent background session with remote control, attachable in herdr, never dependent on the desk process. His hands remain for push (L55), rulings, and grants the classifier withholds. An unattended production deploy runs under a per-session allowlist naming exactly its commands (commit, merge --ff-only, rebase, tag, kickstart, validate, migrate --allow-prod when a migration ships, pg_dump); push is never in it; never `bypassPermissions`; the hub proves the gate at launch with a reverted tag and an empty commit before scheduling. Interim approval: L7.
~~~
NEW `:314`, whole:
~~~text
The desk starts every hub itself, through `desk-launch.sh`, as an independent background session with remote control, attachable in herdr, never dependent on the desk process. His hands remain for every push but the close's nightly push of `main` (L55), rulings, and grants the classifier withholds. WHO STARTS A DEPLOY: the desk, without asking him, when every check of the set closed with nothing held (`held unfixed: 0`, `ready: YES`); the fixed deploy file proves the integrated gate green before the merge (L68), inside the window (L43, L66). He is asked for two things only: a CARRIED HELD DEFECT, which ships only on a row of his, and a SCHEMA ROLLBACK, which is never part of a deploy run. An unattended production deploy runs under the allow list of `DEPLOY-HUB.md`, approved once in the standing list (L62) and naming exactly its commands; push is never in it; never `bypassPermissions`; the hub proves the list with a reverted tag and an empty commit before the outage. Interim approval: L7.
~~~
TODAY Index `:71`:
~~~start-old
- [[LAWS#L61 Desk launches, deploy permissions]] — the desk starts every hub in the background; deploy allowlists.
~~~
NEW Index `:71`:
~~~start-new
- [[LAWS#L61 Desk launches, deploy permissions]] — every launch by the script; who starts a deploy.
~~~

### 10 · L60 — the recovery rule · NEW ON THE LIST
HOME: `LAWS:311` · CARRIES: READ OF LOOP 2 gap 7 (b), (c).
TODAY `:311`, its last sentence:
~~~text
Every build prompt carries a recovery rule: partial work is wip-committed and the chunk relaunched with a CONTINUE prefix, never discarded.
~~~
NEW `:311`, that sentence:
~~~text
Every build and check carries a recovery rule: partial work is wip-committed and CONTINUED — by the desk's `CONTINUE` message to the same session, or by a new session with a CONTINUE prefix in the cases L62 names — never discarded.
~~~

### 11 · L42 — an unclassified path · NEW ON THE LIST
HOME: `LAWS:249` · CARRIES: RECOMMENDATIONS 3 (rule C: an UNCLASSIFIED path is fixed in the build that adds it); THIRD PASS (K10).
TODAY `:249`, inside its first sentence:
~~~text
unclassified → ESCALATE, never dropped.
~~~
NEW `:249`, those words:
~~~text
unclassified → classified in the build that adds the path, before its stop line, with `cobalt jobs restarts` clean and its suite green; never dropped, never owed to a deploy.
~~~

### 12 · L64 — where the desk's launch rule lives · NEW ON THE LIST
HOME: `LAWS:326` · CARRIES: READ OF LOOP 2 gap 2; THIRD PASS item 2 (the desk's `claude --bg` stays out; the script carries every launch).
TODAY `:326`, inside its last sentence:
~~~text
the desk relaunches only from `~/cobalt` (the `Bash(claude --bg *)` rule lives there);
~~~
NEW `:326`, those words:
~~~text
the desk relaunches only through `desk-launch.sh desk`, which runs the wake-up's launch line from `~/cobalt` (the desk holds no `claude --bg` rule of its own);
~~~

## `UNATTENDED-LAUNCH.md` (UL)

### 13 · UL §1 — the per-session approval list → the standing list and the script
HOME: `UL:3`–`:8` · CARRIES: RULED PROCESS items 4 and 6; THIRD PASS items 2 and 4.
TODAY `:4`–`:8`:
~~~text
1. Read the prompt end to end. List every command shape beyond plain reading, editing inside the session's own worktree, or `uv run pytest`: production reads, credential-file copies, vault-token fetches, dev DB migrations and rollbacks, other houses' CLIs (`claude -p`, `agy`, `grok`, `codex`), git history operations, anything outside the worktree. Known denial classes: `[Production Reads]`, `[Production Deploy]` (also cobalt_dev rollbacks), `[Credential Materialization]`, `[Credential Exploration]`, `[Git Destructive]`, `[Create Unsafe Agents]`, `[Self-Modification]`, `[Auto-Mode Bypass]`.
2. APPROVAL LIST: one row per rule — the exact `Bash(<prefix> *)`, what it is for, what it can touch, what it never touches. Add the NEVER block: push, `bypassPermissions`, `--allow-prod` outside a deploy prompt, production vault writes, `launchctl`, another seat's config file.
3. Show him the list once, in the desk chat, before anything starts; his approval is a §4 row. A list already approved for the same job shape is reused from the prompt's launch line, never brought again.
4. Launch line (the SEAT PROFILE's LAUNCH): `claude --bg "Read '<prompt file>' and follow it exactly." --model <m> --remote-control <job> --allowedTools "<rule>" … --disallowedTools "AskUserQuestion" "EnterWorktree" "Bash(git push*)" --add-dir …`. Per session; never `bypassPermissions`; never push.
5. After launch: VIEW it in a job-named herdr tab; record id, pid, tab and the approved list in the desk report's §5 sessions table.
~~~
NEW `:4`–`:8`:
~~~text
1. A BUILD, A CHECK AND A DEPLOY launch on a fixed file and a card: `sh /Users/cobalt/.claude/ops/desk-launch.sh <build|check|deploy> "<card>"` (a check's second pass adds `PASS-2`; a deploy resume adds `STEP-D0`); THE NIGHTLY CLOSE on its fixed file and a date: `… desk-launch.sh close <YYYY-MM-DD>`. Each runs under `--permission-mode dontAsk`: a call on no allow string is refused with no dialog. Their allow lists are the STANDING LIST (`STANDING-LIST.md`), approved by him once: no list is brought per job, and a string not on it is new and is asked for by itself. The script refuses an incomplete or uncommitted card, a worktree outside the approved pattern, a with-DB launch while the lock is held, and a listed path outside `--add-dir`.
2. A ONE-OFF PROMPT (a drafter, a tribunal and its seats, a brain tab) launches by `sh /Users/cobalt/.claude/ops/desk-launch.sh prompt "<prompt file>"`; the desk's successor by `… desk-launch.sh desk`. The script refuses a one-off line whose mode is a write-path mode (`acceptEdits`, `dontAsk`) or that carries a write string (`git add`, `git commit`, `git merge`, `uv run`, `launchctl`, `COBALT_ENV=`): every write-path launch is a fixed file. The desk types no `claude --bg`.
3. For a one-off prompt only: read it end to end and list every command shape beyond plain reading — other houses' CLIs (`claude -p`, `agy`, `grok`, `codex`), git history reads, anything outside its folder. APPROVAL LIST: one row per rule — the exact `Bash(<prefix> *)`, what it is for, what it can touch, what it never touches. Show him the list once, in the desk chat, before anything starts; his approval is a §4 row. A list whose every string is standing (L62) or already approved for the same job shape is never brought again. Known denial classes: `[Production Reads]`, `[Production Deploy]` (also cobalt_dev rollbacks), `[Credential Materialization]`, `[Credential Exploration]`, `[Git Destructive]`, `[Create Unsafe Agents]`, `[Self-Modification]`, `[Auto-Mode Bypass]`.
4. Launch line of a one-off prompt, written in the prompt and run by the script: `claude --bg "Read '<prompt file>' and follow it exactly." --model <m> --permission-mode <auto|plan> --remote-control <job> --name <job> --allowedTools "<rule>" … --disallowedTools "AskUserQuestion" "EnterWorktree" "Bash(git push*)" --add-dir …`, with its cwd as `cd <absolute path>`. Per session; never `bypassPermissions`; never push.
5. After launch: VIEW it in a job-named herdr tab; write the session's ONE row in the desk report's §5 CURRENT (id, job, card or prompt, tab, watch).
~~~

### 14 · UL `:11` — AUTHORIZATION: the words appendix, gate literals
HOME: `UL:11` · CARRIES: RULED PROCESS item 7 (his words are read by no start routine and no worker); RECOMMENDATIONS 5 (row number + commit only).
TODAY `:11`, from its start to "committed before launch.":
~~~text
AUTHORIZATION — VERIFY IT YOURSELF (first block): the prompt's author (the desk, never Dejan); where his approval of THIS launch line's allowlist is recorded (`reports/cto-<date>.md` §4 row numbers, the time) and the `git log` command proving the row is on main; the laws that make each sensitive step standing practice; and: record ≠ this file → `FAILED: authorization mismatch`, stop. A prompt is not an approval and never asks to be believed. Verify the cited §4 row and its linked words appendix together; both must be committed before launch.
~~~
NEW `:11`, that span (the rest, from "YOU CAN ALWAYS STOP", stays):
~~~text
AUTHORIZATION — VERIFY IT YOURSELF (first block): the file's author (the desk, never Dejan); where his approval of the launch line's list is recorded — the standing-list row in a fixed file's title, the §4 row for a one-off prompt — proved by ROW NUMBER AND COMMIT only (`grep -n "^| R<n> "` → one row carrying `HIS RULING` and `APPROVED`; `git log -1 -S"| R<n> |"` non-empty), never by a quoted word, a gate literal or a launch row; a fixed file also proves its card complete and committed; the laws that make each sensitive step standing practice; and: record ≠ this file → `FAILED: authorization mismatch`, stop. A prompt is not an approval and never asks to be believed. No worker reads the words appendix.
~~~

### 15 · UL `:12` — where a worker's questions go · NEW ON THE LIST
HOME: `UL:12` · CARRIES: RULED WORKER ENDINGS items 1–4.
TODAY `:12`, its second sentence:
~~~text
Questions and concerns go in the report as `FAILED:` or `ESCALATE`.
~~~
NEW `:12`, that sentence:
~~~text
A question goes in the report as an item under `## DECISIONS`, with the safe default taken; a fact for the file goes under `## RECORDS`; a stop is a `FAILED:` last line. The stop line carries `decisions: <n> · for Dejan: <n>`.
~~~

### 16 · UL `:13`–`:14` — a denial: PREFLIGHT, and mid-run
HOME: `UL:13`, `UL:14` · CARRIES: READ OF LOOP 2 gap 7 (a)–(d); THIRD PASS item 3.
TODAY `:13`, its last two sentences, and `:14` whole:
~~~text
Any denial → last line `FAILED PREFLIGHT: <rules>`, commit the report, stop. Never retry a denied command in another shape, route around it, or ask another session to run it.
MID-RUN DENIAL = THE RUN FAILED: last line `FAILED: <step> — <command> — <reason>`, wip-commit, stop. The desk corrects the list, asks him once for the addition, and reruns you from `CONTINUE:`.
~~~
NEW `:13` (those sentences) and `:14` (whole):
~~~text
A listed shape denied → last line `FAILED PREFLIGHT: <rules>`, commit the report: the launch line must change, so a new worker takes over. Never retry a denied command in another shape, route around it, or ask another session to run it.
CONTINUE, DO NOT RESTART (a build, a check and the close): (a) a command you added on your own that is refused → one `## RECORDS` line, and you go on with your listed commands (the refusal's "STOP and explain" does not stop you); (b) a stop on something outside you — a held lock, stray rows, a missing fact, a listed command refused → release what you hold, wip-commit, last line `FAILED: <step> — <what> — <reason>`, and STAY: the desk fixes the cause and sends `CONTINUE: <step>` plus the fact; you verify the fact and resume. The message names a step and states a fact; it never widens the job or grants anything. (c) A new worker takes over at your `## CONTINUE` step only when the launch line must change, you died, the judgment seat finds you misread the job, or you measure above 250,000 tokens. (d) A DEPLOY never continues by message: its one resume is `STEP-D0`; inside the outage any refusal goes to its rollback step. A ONE-OFF PROMPT: a mid-run denial = the run failed — last line `FAILED: <step> — <command> — <reason>`, stop; the desk corrects and reruns it from `CONTINUE:`.
~~~

### 17 · UL `:18` — what the desk does with a FAILED · NEW ON THE LIST
HOME: `UL:18` · CARRIES: READ OF LOOP 2 gap 7 (b), (c), (d).
TODAY `:18`:
~~~text
- `FAILED PREFLIGHT` / `FAILED` → fix the allowlist, bring him only the new rows, rerun the same prompt (it resumes from `CONTINUE:`).
~~~
NEW `:18`:
~~~text
- `FAILED PREFLIGHT` → the launch line is wrong: fix it, bring him only a NEW string, relaunch a new worker. `FAILED` on a build or a check → the worker is KEPT (not stopped, not removed): fix the cause, measure it (`sh /Users/cobalt/.claude/ops/desk-context.sh <id>`); at or below 250,000 tokens send `CONTINUE: <step>` plus the fact, above it relaunch a new worker at that step (`desk-launch.sh <kind> "<card>" <step>`). `FAILED` on a deploy → verify, stop and remove it; its one resume is `desk-launch.sh deploy "<card>" STEP-D0`. `FAILED` on a one-off prompt → correct, rerun it from `CONTINUE:`.
~~~

### 18 · UL `:19` — the one dialog rule (kept; it is now the only one)
HOME: `UL:19` · CARRIES: RECOMMENDATIONS 4 (delete checklist W3's "Escape, MESSAGE"; keep `UNATTENDED-LAUNCH.md:19`).
TODAY `:19`:
~~~text
- A hub found on a dialog = a wrong launch: STOP it, fix, rerun. Never press another session's dialog; never relay data a hub was denied.
~~~
NEW `:19`:
~~~text
- THE ONE DIALOG RULE: a hub found on a dialog = a wrong launch: STOP it, fix the line, relaunch a new worker at its `## CONTINUE` step. Never press another session's dialog, never send a key into its pane; never relay data a hub was denied (a `CONTINUE` message states a fact the hub can read itself). A deploy hub past its first bootout is not stopped while it moves; hung there, it is stopped and resumed at once with `STEP-D0`.
~~~

### 19 · UL `:22` — the close: stop lines, decisions · NEW ON THE LIST
HOME: `UL:22` · CARRIES: RULED WORKER ENDINGS items 5 and 6; READ OF LOOP 2 gap 7 (b).
TODAY `:22`:
~~~text
When the last line is the stop line: verify the artifact (L35: worktree clean, commits present, suite line), record it, STOP the session if still listed, close its tab, fold `MEMORY:` / `RULING:` lines, bring him the ESCALATE items per [[preferences]].
~~~
NEW `:22`:
~~~text
When the last line is a DONE stop line (`BUILT`, `CHECK DONE`, `DEPLOYED`, a one-off prompt's own): verify the artifact (L35: worktree clean, commits present, suite line), record it, STOP and remove the session, close its tab, fold `MEMORY:` / `RULING:` lines. `decisions: 0` → launch the next step. `decisions: ≥1` → hand the report path to the Opus judgment seat (`brain`, or a hub the desk launches): it reads `## DECISIONS` only — for a DEPLOY report both `## DECISIONS` and `## RECORDS`, whatever the count — and answers each; record the answers; a `FOR DEJAN` item reaches him as one short question, per [[preferences]]. A build or check that ended `FAILED` is not closed: §3.
~~~

### 20 · UL `:29` — a string first used for real
HOME: `UL:29` · CARRIES: RECOMMENDATIONS 1 (rule E: nothing is first used inside the outage; every absolute path on the allow list sits under `--add-dir`).
TODAY `:29`, its second sentence:
~~~text
The desk names every probe in the prompt; a rule with no harmless variant is probed by its first real use.
~~~
NEW `:29`, that sentence:
~~~text
Every probe is named in the prompt or fixed file; a rule with no harmless variant is probed by its first real use, and the file says what a denial there leaves behind. In a deploy no string is used for the first time inside the outage that could be used before it (the few with no harmless variant are named in `DEPLOY-HUB.md` P8), and every absolute path on a launch line sits under its `--add-dir` set (the script refuses a line where one does not).
~~~

## The checklist (CHECKLIST)

### 21 · REFRESH HOW (3) — §5 CURRENT
HOME: `CHECKLIST:17`, step (3) · CARRIES: RULED WORKER ENDINGS item 7; RECOMMENDATIONS 7.
TODAY `:17`, step (3):
~~~start-old
(3) rewrite `## §5 CURRENT`: one row per live hub (id, job, prompt, tab, watch + ceiling, awaited stop line) + `OPEN TO HIM` + `WATCHES + TIMERS`; finished rows move unchanged to `## §5 HISTORY`;
~~~
NEW `:17`, step (3):
~~~start-new
(3) rewrite `## §5 CURRENT`: one row per live session (id, job, card or prompt, tab, watch + ceiling, awaited stop line) + `OPEN TO HIM`; finished rows move unchanged to `## §5 HISTORY`;
~~~
Step (4), "LAUNCH the successor", stands: LAUNCH is the wake-up's verb, and row 44 makes it the script.

### 22 · `## rulings` — gate literals, the words read, the per-event record
HOME: `CHECKLIST:22` · CARRIES: RECOMMENDATIONS 5, 6 and 7; RULED PROCESS item 7; RULED WORKER ENDINGS item 7.
TODAY `:22`, whole:
~~~text
- Every ruling, launch or record → one `## §4 Rulings` row in `cto-<today>.md` the same turn, per [[writing-rules]]: `| R<n> | <time from date> | <direction or fact, one line> | <status> |`. Status: `APPROVED — pending fold` → `APPLIED: <file>`; `LAUNCHED` (the row carries every gate literal its prompt greps); `RECORD` (with its report path). His words go verbatim, in the same turn, to `reports/cto-<today>-words.md`, explicitly linked from §4 as the day’s report appendix, with a stable heading for each R-number. Every approval row retains its time, exact approved action and required file/hash and authorization literals. Preserve existing rows consumed by queued prompts. Read the linked words when verifying authority; routine wake-up omits already-folded quotations.
~~~
NEW `:22`, whole:
~~~text
- Every ruling, launch or record → one `## §4 Rulings` row in `cto-<today>.md` the same turn, per [[writing-rules]]: `| R<n> | <time from date> | <direction or fact, one line> | <status> |`. Status: `APPROVED — pending fold` → `APPLIED: <file>` (a standing ruling stays `pending fold` until it is in LAWS or NOW); `LAUNCHED` (the job, its card or prompt, the session id; no gate literal — a hub proves his approval by row number and commit, K23, and its card by its commit); `RECORD` (with its report path). PER EVENT: ONE row and ONE commit per launch; §5 CURRENT holds one row per live session, overwritten in place, with no TABS row and no WATCHES row. His words go verbatim, in the same turn, to `reports/cto-<today>-words.md`, explicitly linked from §4 as the day’s report appendix, with a stable heading for each R-number that says what he was answering. Every approval row retains its time, exact approved action and required file/hash. Preserve existing rows consumed by queued prompts. The row alone carries the direction: no start routine and no worker reads the words file.
~~~

### 23 · `## rulings` R2 — what a row carries · NEW ON THE LIST
HOME: `CHECKLIST:23` · CARRIES: RECOMMENDATIONS 5; READ OF THE DRAFT gap 5 (RULED: the launch-row field and its gate are dropped).
TODAY `:23`, inside its first sentence:
~~~text
the literals a prompt greps (ids, file names, hashes, gate literals) and a link to the report or words heading that holds the detail.
~~~
NEW `:23`, those words:
~~~text
the ids a reader needs (session id, file names, hashes) and a link to the report or words heading that holds the detail; no prompt greps a row for a literal.
~~~

### 24 · `## launch` L1 — how a launch is typed · NEW ON THE LIST
HOME: `CHECKLIST:28` · CARRIES: READ OF THE DRAFT gap 2; READ OF LOOP 2 gap 2; THIRD PASS item 2.
TODAY `:28`:
~~~text
- L1 `cd <wt>` in its own call; the launch line alone; the next call `cd /Users/cobalt/cobalt`; check the cwd in LIST.
~~~
NEW `:28`:
~~~text
- L1 Every launch is ONE bare command: `sh /Users/cobalt/.claude/ops/desk-launch.sh <build|check|deploy> "<card>" [PASS-2] [<step>]`, `… desk-launch.sh desk`, or `… desk-launch.sh prompt "<prompt file>"`. Never a typed `cd`, `git worktree add` or `claude --bg`; check the cwd in LIST.
~~~

### 25 · `## launch` L6–L9 — what the desk reads and fills at launch
HOME: `CHECKLIST:33`–`:36` · CARRIES: RULED PROCESS items 3 and 4; RECOMMENDATIONS 5 and 9; READ OF THE DRAFT gap 6.
TODAY `:33`–`:36`:
~~~text
- L6 [stated 2026-09-29 · Code, R165] At launch read only what the desk acts on: the MODEL line and the launch line (`sed -n` their lines), the fill and gate lines (`grep -n`); never the whole prompt — the drafter's `comm` and its `new rule strings:` count stand; cite a line, never a count.
- L7 Launch row committed; `R__` filled (`grep -c -E "R_[_]"` = 0; a self-counting gate forbids replace_all); gate literals copied verbatim.
- L8 Re-point queued prompts to every built fact (tip, base, counts, subjects, `Reapply`, paths, headers); `git log <tip>..<branch> -- tests src configs` empty = the tip stands.
- L9 A prompt older than a law or a sibling build → drafter re-issue.
~~~
NEW `:33`–`:36`:
~~~text
- L6 [stated 2026-09-30 · Dejan, R45] A launch on a fixed file reads nothing of that file: fill the card; the script refuses what is wrong. A one-off prompt: read only its MODEL line and its launch line, never the whole prompt.
- L7 The card is committed on `main` with no `«FILL` token before the launch (the script refuses both). The launch row is the desk's record (L34) and carries no gate literal.
- L8 A built fact goes into the CARD (`TIP`, `CHECK REPORT`, `HOUSE B`; a deploy's `TIP` and `## SHIPS`), never into a prompt's text; `git log <tip>..<branch> -- tests src configs` empty = the tip stands.
- L9 A one-off prompt older than a law → drafter re-issue. A fixed file's procedure changes by a drafter re-issue that the judgment seat reads; its allow list changes only with his approval; its tree-state lines by a build row; `DEPLOY-HUB.md` is read by one other house at each change (L67).
~~~
FOURTH PASS: L9 AS AMENDED BY THE JUDGMENT SEAT (`reports/brain-desk-review-2026-09-30.md` `## READ OF THE THIRD PASS`, "ONE ROW AMENDED"): the third pass's "A fixed file changes only by a build row … or with his approval of a changed list" left no way to correct a fixed file's procedure.

### 26 · `## watch` W3 — the dialog
HOME: `CHECKLIST:51` · CARRIES: RECOMMENDATIONS 4; THIRD PASS item 4.
TODAY `:51`:
~~~text
- W3 Dialog: `send-keys Escape`, MESSAGE its LIST name.
~~~
NEW `:51`:
~~~text
- W3 Dialog: `UNATTENDED-LAUNCH.md` §3 — STOP the hub, fix the line, relaunch a new worker; never a key into its pane.
~~~

### 27 · `## watch` W8 — a FAILED worker is kept, not removed
HOME: `CHECKLIST:55` · CARRIES: READ OF LOOP 2 gap 7 (b); THIRD PASS item 4.
TODAY `:55`, from "stop line verified" to its end:
~~~text
stop line verified (L35) → STOP + rm the hub, then bare `herdr tab close <tab>`, the same turn. Never left "closable" for later.
~~~
NEW `:55`, those words:
~~~text
a DONE stop line verified (L35) → STOP + rm the hub, then bare `herdr tab close <tab>`, the same turn. Never left "closable" for later. A build or check whose last line is `FAILED` is not done: it is KEPT — not stopped, not removed, its tab open — until the desk has sent it `CONTINUE` or relaunched a new worker in its place (L62). A `FAILED` deploy is stopped and removed; it resumes only at `STEP-D0`.
~~~

### 28 · `## commit` C2 — the guard
HOME: `CHECKLIST:61` · CARRIES: RULED PROCESS item 5; RECOMMENDATIONS 3.
TODAY `:61`:
~~~text
- C2 No desk commit or staging while a deploy hub runs.
~~~
NEW `:61`:
~~~text
- C2 No desk commit or staging on `main` while a deploy hub is live: the pre-commit guard refuses it (it lets through only the hub's own `reports/deploy-<name>.md`). Write by Edit / Write; commit once the hub is stopped and removed. The desk never commits into a gate or seam tree.
~~~

### 29 · `## prompts` K6 — ceilings
HOME: `CHECKLIST:93` · CARRIES: RECOMMENDATIONS 9 ("Packet ceilings (K6, K17) go, as he ruled on 09-27").
TODAY `:93`:
~~~text
- K6 Ceilings from `wc -c`; Write in ≤15 KB parts.
~~~
NEW `:93`:
~~~text
- K6 No packet and no byte ceiling (his 2026-09-27 R42); a new file is written in ≤15 KB parts.
~~~

### 30 · `## prompts` K10 — deploy prompts; the unclassified path
HOME: `CHECKLIST:97` · CARRIES: RECOMMENDATIONS 3 (K10 "today sends the classification to the deploy"); RULED PROCESS item 9.
TODAY `:97`:
~~~text
- K10 Deploy prompts: radar three reads, tails ≥90 s + REVERT-READBACK, `Reapply`, hotfix re-issue, unclassified config = `no_resident_reads`.
~~~
NEW `:97`:
~~~text
- K10 A deploy is a card on `DEPLOY-HUB.md`, which carries the radar three reads, the spaced tails, REVERT-READBACK and `Reapply`. An unclassified path is classified in the BUILD that adds it, with `cobalt jobs restarts` clean at its stop line (L42); never at the deploy, never by the desk.
~~~

### 31 · `## prompts` K17 — the packet ceiling
HOME: `CHECKLIST:104` · CARRIES: RECOMMENDATIONS 9; HIS DIRECTIONS row 09-27 R42 ("K17 still prescribes one").
TODAY `:104`:
~~~text
- K17 A check's packet ceiling = the MEASURED sum of the precedent packet's `## Packet` (outputs and QUESTIONS included), set in the launch row from the build's `--stat`; cap vs formula → state both, pick with reason; a packet stop spends no round — relaunch keeps the staged files and report path; a COMPLETE packet relaunches "stage nothing, cut nothing".
~~~
NEW `:104`:
~~~text
- K17 — struck (his 2026-09-27 R42): a check has no packet and no ceiling; the check session and each house read the files themselves (`CHECK-HUB.md` `## 1`).
~~~

### 32 · `## prompts` K19 — the deploy launch turn
HOME: `CHECKLIST:106` · CARRIES: RECOMMENDATIONS 1, 2 and 5; READ OF THE DRAFT gap 7.
TODAY `:106`:
~~~text
- K19 Deploy launch turn: run every authorization grep the prompt names against the real desk rows first; grep every `db query` string for `%` (use `strpos`); the relaunch rule reads every deploy-phase part and re-runs a no-touch preflight stop; during a deploy the desk writes by Edit / Write only; a denied watch = "say check" told at launch ; every path a smoke row reads sits under the launch line's `--add-dir`.
~~~
NEW `:106`:
~~~text
- K19 Deploy launch turn: `desk-launch.sh deploy "<card>"` — it refuses an incomplete or uncommitted card, a `%` in a `db query` string (use `strpos`) and a listed path outside `--add-dir`; every path a smoke row of the card reads sits under that set. The one relaunch is `… deploy "<card>" STEP-D0`. During a deploy the desk writes by Edit / Write only; it never stops a deploy hub past its first bootout while it moves; a hub hung there is stopped and resumed at once with `STEP-D0`; a denied watch = "say check" told at launch.
~~~

### 33 · `## prompts` K22 — a fix round's seats
HOME: `CHECKLIST:109` · CARRIES: RULED CHECK FLOW (SEAT ORDER); THIRD PASS item 4.
TODAY `:109`:
~~~text
- [stated 2026-09-28 · Code] K22 A fix-round draft names its check's seats from L67 `CHECKER SEATS BY KIND OF WORK` (a fix round = Opus · Sol · Grok), never from the round-1 check it copies.
~~~
NEW `:109`:
~~~text
- [stated 2026-09-30 · Dejan] K22 — struck: a build check's seats are the flow and the seat order of `CHECK-HUB.md` (L67); no draft names them.
~~~

### 34 · `## prompts` K4, K14 — the check's packet · NEW ON THE LIST
HOME: `CHECKLIST:91`, `:101` · CARRIES: RECOMMENDATIONS 9; RULED CHECK FLOW (no packet; no rounds).
TODAY `:91` and `:101`:
~~~text
- K4 A late step joins the check's packet.
- K14 A packet gap = the next round.
~~~
NEW `:91` and `:101`:
~~~text
- K4 — struck (no packet, his 2026-09-27 R42).
- K14 — struck (no packet, no rounds in a build check: L67).
~~~

### 35 · the word ESCALATE in K24, R6 and K5 · NEW ON THE LIST
HOME: `CHECKLIST:111`, `:71`, `:92` · CARRIES: RULED WORKER ENDINGS items 1–5; RULED CHECK FLOW step 1 and the brain's CORRECTION (READ OF THE DRAFT gap 1).
TODAY `:111`, `:71`, `:92`:
~~~text
- [stated 2026-09-29 · Dejan] K24 A check counts a finding only with a failing test or command the checker ran (L70); the rest go under ESCALATE unclassified (R129).
- R6 ESCALATEs before DIGEST.
- K5 A renamed fixture = ESCALATE; guard test = the row's file.
~~~
NEW `:111`, `:71`, `:92`:
~~~text
- [stated 2026-09-29 · Dejan] K24 A check counts a finding only when its fresh Opus session ran the finding's test or command and it held (L70); a claim with nothing runnable is dropped and listed (R129).
- R6 `## DECISIONS` before DIGEST: `decisions: 0` → verify and launch the next step; one or more → the judgment seat.
- K5 A renamed fixture = a `## DECISIONS` item; guard test = the row's file.
~~~

## The contract (CONTRACT)

### 36 · a denied git command
HOME: `CONTRACT:16` · CARRIES: STARTUP, Contradictory (`:16` against `:17` and `:20`); READ OF LOOP 2 gap 7; THIRD PASS item 4.
TODAY `:16`:
~~~start-old
- A denied git command → refresh; never ask him.
~~~
NEW `:16`: the line is REMOVED (it moves to `_retired/cto-desk-contract.md`). `:17` already says what the desk does with a refused command — one more try by another reasonable approach — and `:20` forbids a refresh below 220,000 tokens. Counted below as 0 bytes after.

### 37 · his four → three
HOME: `CONTRACT:21` · CARRIES: RULED PROCESS item 7 ("deploys leave his four").
TODAY `:21`, its first sentence:
~~~start-old
He rules only scope, dates, deploys and money.
~~~
NEW `:21`, that sentence (the tag before it takes the fold's date; who starts a deploy, and the two things he is still asked, have their one home in L61):
~~~start-new
He rules only scope, dates and money.
~~~

### 38 · seats — where they name check hubs
HOME: `CONTRACT:29` (`:30` and `:31` stand as written) · CARRIES: THIRD PASS item 1 (the check is a fresh Opus; no Sonnet hub).
TODAY `:29`, its last clause:
~~~start-old
mechanical drafters (re-issue, re-point) and every hub on Sonnet.
~~~
NEW `:29`, that clause:
~~~start-new
mechanical drafters (re-issue, re-point) and tribunal hubs on Sonnet; a fixed file names its model.
~~~

## The start files and the writing rules

### 39 · `CLAUDE.md` — what a worker reads
HOME: `/Users/cobalt/cobalt/CLAUDE.md:3` · CARRIES: READ OF THE DRAFT, RULED on gap 9; RECOMMENDATIONS 8.
TODAY `:3`:
~~~start-old
Read `/Users/cobalt/Vault/Think/6 - Permanent/Memory/areas/cobalt.md` and follow its `## Start here`.
~~~
NEW `:3` (it grows; its larger cut is row 40, the same fact leaving its second home):
~~~start-new
Read `/Users/cobalt/Vault/Think/6 - Permanent/Memory/areas/cobalt.md`: a worker on a card or a prompt, only `## What Cobalt is` and from `## Build rules` down; the CTO desk and a seat Dejan talks to, its `## Start here`.
~~~

### 40 · `areas/cobalt.md` `## Start here`
HOME: `M/areas/cobalt.md:8`–`:9` · CARRIES: READ OF THE DRAFT, RULED on gap 9.
`:8` STANDS as written: with row 39, only the desk and a seat he talks to reach `## Start here`, and `:8` is theirs.
TODAY `:9`:
~~~start-old
- The sections from `## Build rules` down are the rules for building Cobalt. Every house but the CTO desk reads them now; the desk opens them when its task plans, drafts, builds, reviews or documents Cobalt code, config or docs.
~~~
NEW `:9`:
~~~start-new
- The desk opens `## Build rules` down when its task plans, drafts, builds, reviews or documents Cobalt.
~~~

### 41 · `areas/cobalt.md` `## Working rules` — the report shape · NEW ON THE LIST
HOME: `M/areas/cobalt.md:39` · CARRIES: RULED WORKER ENDINGS items 1–4.
TODAY `:39`:
~~~start-old
- Report: §0 ≤5 lines → tables → ESCALATE; facts only.
~~~
NEW `:39`:
~~~start-new
- Report: §0 ≤5 lines → tables → DECISIONS, RECORDS; facts only.
~~~

### 42 · `writing-rules.md` — the words read
HOME: `M/topics/writing-rules.md:10` · CARRIES: RULED PROCESS item 7; RECOMMENDATIONS 6.
TODAY `:10`, its last sentence:
~~~text
Store his words in the day’s linked words appendix; read them when verifying a ruling.
~~~
NEW `:10`, that sentence:
~~~text
Store his words in the day’s linked words appendix, each block saying what he was answering; no start routine and no worker reads them — the row carries the direction.
~~~

### 43 · `writing-rules.md` — the report sections the desk reads · NEW ON THE LIST
HOME: `M/topics/writing-rules.md:22` · CARRIES: RULED WORKER ENDINGS items 1–4.
TODAY `:22`, its opening words:
~~~text
A report section the desk reads (§0, `## CONTINUE`, `## ESCALATE`, the stop line)
~~~
NEW `:22`, those words:
~~~text
A report section the desk reads (§0, `## CONTINUE`, `## DECISIONS`, the stop line)
~~~

## The wake-up (WAKE)

### 44 · the desk's own launch
HOME: `WAKE:13` · CARRIES: READ OF LOOP 2 gap 2; THIRD PASS item 2 (`desk` runs the wake-up's own launch line).
TODAY `:13`, its opening words (the backticked `claude --bg …` span after them stays byte for byte: the script reads it from here):
~~~start-old
- LAUNCH (by the predecessor at REFRESH; by Dejan only when no desk is alive): `cd ~/cobalt`, then
~~~
NEW `:13`, those words:
~~~start-new
- LAUNCH (at REFRESH: `sh /Users/cobalt/.claude/ops/desk-launch.sh desk` runs this line; by Dejan only when no desk is alive): `cd ~/cobalt`, then
~~~
NOT IN THIS ROW: the narrower allow and deny strings of `DESK-LINE.md` §2. They are a change of the desk's list, approved or struck with `STANDING-LIST.md` §4, not a rule this process contradicts; they would add 285 bytes to this line (`DESK-LINE.md` §2b) and are counted on their own line in `## START-SET`.

### 45 · RECONCILE — the words file is read by no start routine
HOME: `WAKE:33` · CARRIES: RULED PROCESS item 7; RECOMMENDATIONS 6.
TODAY `:33`, three places:
~~~start-old
then read only those rows and their `## R<n>` blocks in that day's `-words.md`.
~~~
~~~start-old
A row you cannot verify from the row plus its R<n> block → OPEN, not applied.
~~~
~~~start-old
a wording you cannot settle from his words goes in marked "desk reading".
~~~
NEW `:33`, the same three places:
~~~start-new
then read only those rows.
~~~
~~~start-new
A row without its direction → OPEN, not applied.
~~~
~~~start-new
a wording the row does not settle goes in marked "desk reading".
~~~

### 46 · SESSIONS and ACT — the ending sections, dialogs, a relaunch · NEW ON THE LIST
HOME: `WAKE:34`, `WAKE:36` · CARRIES: RULED WORKER ENDINGS; RECOMMENDATIONS 4; READ OF LOOP 2 gap 7.
TODAY `:34`, one clause, and `:36` whole:
~~~start-old
its last `## ESCALATE` block only when that `§0` counts one.
~~~
~~~start-old
8. ACT on step 6's notes: answer each `ASK DESK` by MESSAGE; clear dialogs (CHECKLIST `## watch` W3); relaunch a hub in the previous desk report but absent from LIST `--all` on its own launch line (its `CONTINUE:` line); WAIT on every busy hub you wait for; write the session table (id, job, state, waits for) in §5.
~~~
NEW `:34`, that clause, and `:36` whole:
~~~start-new
its `## DECISIONS` only when its stop line counts one.
~~~
~~~start-new
8. ACT on step 6's notes: answer each `ASK DESK` by MESSAGE; a hub on a dialog, or in the previous desk report but absent from LIST `--all` → CHECKLIST W3 and L1; WAIT on every busy hub you wait for; write each live session's row in §5.
~~~

### 47 · EVERY TURN — his four → three
HOME: `WAKE:40` · CARRIES: RULED PROCESS item 7.
TODAY `:40`, one clause:
~~~start-old
He rules only scope, dates, deploys and money;
~~~
NEW `:40`, that clause:
~~~start-new
He rules only scope, dates and money;
~~~

### 48 · ON TRIGGER — a launch
HOME: `WAKE:45` · CARRIES: RULED PROCESS items 4 and 6; RULED CHECK FLOW, START-SET RULE.
TODAY `:45`:
~~~start-old
- A launch → CHECKLIST `## launch` and `## watch`, then `D/prompts/UNATTENDED-LAUNCH.md`.
~~~
NEW `:45` (the standard is opened from CHECKLIST L2, for a one-off prompt; a fixed-file launch needs neither the standard nor a list):
~~~start-new
- A launch → CHECKLIST `## launch` and `## watch`.
~~~

## THE NIGHTLY CLOSE (fourth pass; RULED — THE NIGHTLY CLOSE, his "Yes, I want all this", brain tab, 09-30, point 4: every law and rule that stops points 1–3 changes to match, as a set, under his same word)

### 49 · L55 — the standing nightly push
HOME: `LAWS:294`, Index `:65` · CARRIES: RULED — THE NIGHTLY CLOSE points 3 and 4.
TODAY `:294`, whole:
~~~text
Auto mode per session, never blanket; never `bypassPermissions` on the host; the classifier is a safety gate, not an approval (L37). Code installs and proves every scheduled job it ships. The desk pushes `main` and deploy tags only on his typed or spoken "push" in the desk chat — the HITL approval for that one push: it names the range and tags first, verifies after (`git rev-list --count origin/main..main` = 0; `git ls-remote` for the tag) and logs both in the desk report. Never a force push, never another branch, never a hub or builder; push is in no launch allowlist. The desk's push allow lives only in `~/cobalt/.claude/settings.local.json` (force / delete / mirror / all / tags denied there); every hub launch line carries `--disallowedTools "Bash(git push*)"`.
~~~
NEW `:294`, whole:
~~~text
Auto mode per session, never blanket; never `bypassPermissions` on the host; the classifier is a safety gate, not an approval (L37). Code installs and proves every scheduled job it ships. THE STANDING NIGHTLY PUSH: the close (`CLOSE-HUB.md`), after its one commit, pushes `main` — `git push origin main`, never forced, never another branch, never a tag — and verifies it (`git status --short --branch` shows no `[ahead`); its line allows that one spelling and denies force / delete / mirror / all / tags. Every other push — `main` in the day, a deploy tag — is the desk's, only on his typed or spoken "push" in the desk chat — the HITL approval for that one push: it names the range and tags first, verifies after (`git rev-list --count origin/main..main` = 0; `git ls-remote` for the tag) and logs both in the desk report. Never a force push, never another branch, never a build, check or deploy hub; push is in no other launch allowlist. The desk's push allow lives only in `~/cobalt/.claude/settings.local.json` (force / delete / mirror / all / tags denied there); every build, check and deploy launch line carries `--disallowedTools "Bash(git push*)"`.
~~~
TODAY Index `:65`:
~~~start-old
- [[LAWS#L55 Push, no bypass, proven jobs]] — push only on his word; never `bypassPermissions`.
~~~
NEW Index `:65`:
~~~start-new
- [[LAWS#L55 Push, no bypass, proven jobs]] — push on his word, or the nightly close; never `bypassPermissions`.
~~~

### 50 · L58 — the close's part; who rewrites NOW
HOME: `LAWS:303` (two sentences), `LAWS:304` (whole), Index `:68` · CARRIES: RULED — THE NIGHTLY CLOSE points 2 and 4 ("`## NOW` rewritten whole from live evidence, at most 1,500 characters (L58)" is a step the close KEEPS; "rule changes are applied at the ruling").
TODAY `:303`, two sentences:
~~~text
This file changes only from the close prompt's list of that day's approved rulings, each carrying his words, the time and the exact fold text, applied by the desk.
A hub never writes the memory folder or this file.
~~~
NEW `:303`, those two sentences:
~~~text
This file changes only from his approved rulings, each carrying its row, the time and the exact fold text, applied by the desk at the ruling; the nightly close lists any still `APPROVED — pending fold`.
A hub never writes the memory folder or this file, but the close rewrites `## NOW` of `areas/cobalt.md`.
~~~
TODAY `:304`, whole:
~~~text
AT A SESSION CLOSE the close hub PROPOSES and MEASURES — the ledger appendix, the `Laws fold — PROPOSED, NOT APPLIED` list, the ladder status, the always-loaded measurement — and the desk APPLIES: LAWS.md, LAWS-HISTORY.md, `## NOW`, areas/topics. `SESSION-CLOSE.md` names the runner of every step. On a night the desk is down, the close report lists the desk's steps as OWED and the next wake-up's reconcile applies them.
~~~
NEW `:304`, whole:
~~~text
AT THE NIGHTLY CLOSE the close hub (`CLOSE-HUB.md`, launched by the desk after the 21:00 ET pause, when no deploy hub is live) writes the ledger appendix and the sprint status block, rewrites `## NOW` whole from live evidence (its one memory write), cuts the day's §4 rows to the row rule with the full text archived, lists every ruling still `APPROVED — pending fold` and every lesson no fixed file or checklist rule carries, measures the always-loaded block, commits once and pushes `main` (L55). The desk APPLIES what it lists: LAWS.md, LAWS-HISTORY.md, the checklist, areas/topics. A missed night is closed by the morning desk's first launch, before the plate.
~~~
TODAY Index `:68`:
~~~start-old
- [[LAWS#L58 Memory write path]] — only the desk writes memory and this file, from his approved rulings; NOW is a snapshot.
~~~
NEW Index `:68`:
~~~start-new
- [[LAWS#L58 Memory write path]] — the desk writes memory and this file at the ruling; the close rewrites NOW.
~~~

### 51 · LAWS `## Fold at session close` — the close lists, the desk applies at the ruling · NEW ON THE LIST
HOME: `LAWS:380` (the section under the heading at `:379`; the heading and its Index line `:88` stand — a link target, checklist M4) · CARRIES: RULED — THE NIGHTLY CLOSE point 2 ("the laws fold lists only a ruling still `APPROVED — pending fold` (rule changes are applied at the ruling)").
TODAY `:380`, its first three sentences and its last:
~~~text
Trigger: every session close, including a close with no new law — a no-change close records that outcome. The close hub's inputs: the live ledger's newly dated rulings, this file's `## Index` and the entries its candidates touch, LAWS-HISTORY.md's lines for those entries, Memory INDEX + the always-loaded cap's profile/preferences companions, and Dejan's session rulings with dated provenance. The close hub's work: separate standing-law changes from product decisions/status, and write each candidate under `Laws fold — PROPOSED, NOT APPLIED` in its close report with his words, the time and the exact fold text; it writes nothing under `6 - Permanent/Memory/` (L58).
Procedure: `docs/40 - DevDocs/SESSION-CLOSE.md`.
~~~
NEW `:380`, those sentences:
~~~text
Trigger: a ruling of his that changes a law; the desk applies it at the ruling (L58). The nightly close lists, from the day's desk report, every ruling still `APPROVED — pending fold` — row, time, row text verbatim — and judges or proposes nothing; a close with none records `none pending`. It writes nothing under `6 - Permanent/Memory/` but `## NOW` (L58).
Procedure: `docs/40 - DevDocs/prompts/CLOSE-HUB.md`.
~~~
The desk's work, the refusal list and "Uncertain classification stays OPEN for Dejan" stand byte for byte.

### 52 · CONTRACT `:11` — the day's close
HOME: `CONTRACT:11` · CARRIES: RULED — THE NIGHTLY CLOSE points 1, 2 and 4 ("contract `:11`").
TODAY `:11`, those words:
~~~start-old
close (`SESSION-CLOSE.md`)
~~~
NEW `:11`, those words (the rest of the line stands):
~~~start-new
close (`CLOSE-HUB.md`; missed: before the plate)
~~~

### 53 · CHECKLIST `## close` — the desk launches the close; it writes no close prompt
HOME: `CHECKLIST:123` (under `## close`, `:121`; its tag `:122` takes the fold's date) · CARRIES: RULED — THE NIGHTLY CLOSE points 1, 2, 3 and 4 ("checklist `## close` `:123`").
TODAY `:123`:
~~~text
- CLOSE: write the close prompt `prompts/<today>/99-close.md` for a hub to run `docs/40 - DevDocs/SESSION-CLOSE.md`; do no close step yourself beyond memory files. The last reply carries the next opener.
~~~
NEW `:123`:
~~~text
- CLOSE: each evening after the 21:00 ET pause, when no deploy hub is live, `sh /Users/cobalt/.claude/ops/desk-launch.sh close <today>` — never asked of him, no close prompt written. A missed night: `… close <that date>` is the morning desk's first act, before the plate. No desk commit on `main` until its stop line `^(CLOSE PUSHED|FAILED)`; the close pushes `main` itself (L55). Apply what it lists (pending folds, OWED lessons) at once. The last reply carries the next opener.
~~~

### 54 · `SESSION-CLOSE.md` — the table is replaced by the fixed file
HOME: `/Users/cobalt/cobalt/docs/40 - DevDocs/SESSION-CLOSE.md` (15 lines, 3,544 B `wc -c`; not under `prompts/`, as the prompt of this pass names it) · CARRIES: RULED — THE NIGHTLY CLOSE point 2 ("One fixed file, `CLOSE-HUB.md`, replaces `SESSION-CLOSE.md`'s table").
TODAY `:3` (lines 5–15 are the step table: steps 1, 2, 2a, 4a, 3, 4, 5, 6, 7):
~~~text
A session is closed only by this routine. The close hub runs it from `~/cobalt` on `main`; every step leaves its evidence in the file it names. The hub PROPOSES and MEASURES; the desk APPLIES (L58). Memory rules: INDEX `rules:` and [[writing-rules]].
~~~
NEW: the whole file becomes these three lines (the table moves to git history; its steps are `CLOSE-HUB.md` 1–8: 1 ledger, 2 laws fold reduced, 2a lessons reduced, 4a status, 3 NOW (now the close's), 5 measure, 6 commit kept; 4 areas/topics dropped — applied at the ruling; 7 push on his word → the nightly push; the §4 row cut added):
~~~text
# SESSION-CLOSE — replaced
The nightly close is `docs/40 - DevDocs/prompts/CLOSE-HUB.md`, launched by `desk-launch.sh close <date>` (L55, L58 as amended <fold date> R<n>).
The old step table is in git history.
~~~

## NOT CHANGED — for the record
- THE 9:30 OVERRIDE ENDED (RULED — the 9:30 override ends; `cto-2026-09-30.md` R44). L66's pause and L43's window bind every deploy again; their window text is not touched. L73 is NOT amended: "A standing or blanket permission to skip steps does not exist" stands, and his 09-30 R10 met its own end condition. No deploy card cites R10. `DEPLOY-HUB.md` P1 admits the pause, the overnight idle, a non-trading day, or his PER-CASE override for that one deploy (L73), never a standing one.
- L58 for THIS list: it already lets the desk write LAWS "at the ruling when possible", from his approved rulings; this list is that ruling's exact fold text. (The close's part of L58 changes: row 50.)
- L64 (FOURTH PASS, "L64 if its text needs it"): no text needs a change. It names the desk's refresh and relaunch, not the close; row 12 already moves its launch rule to `desk-launch.sh desk`.
- L29, L36, L37, L63, L70, L76: the fixed files comply as written (the build, the check and the deploy are Opus on `dontAsk` — a permission gate the 09-30 scratch test proved stops file AND command writes with no dialog (item 9, probe D) — never auto mode on a write path; a worker launches only the one house its file names; no model approves; no dialog; a finding counts only when run; one lock).
- `INDEX.md:11` ("A read-and-judge seat reads only its card's law excerpts (L59)") stands. `## NOW` of `areas/cobalt.md` is a snapshot the desk rewrites (L58), not a rule: its lines on K24, R128 and the fixed-file process are rewritten at the next refresh.
- CHECKLIST K23 and K25 stand and are carried by the fixed files.

## FOLD ORDER (FOURTH PASS, DONE means)
The brain reads this file; the desk has run the scratch test (09-30, done); he approves `STANDING-LIST.md` once; this list is put in front of him; then the desk FOLDS FIRST — rows 1–12 and 49–51 into LAWS (replaced wording to `LAWS-HISTORY.md`; each Index line in the same edit), rows 13–20 into `UNATTENDED-LAUNCH.md`, 21–35 and 53 into the checklist, 36–38 and 52 into the contract, 39–43, 44–48, and 54 (`SESSION-CLOSE.md`) — then INSTALLS the fixed files and the script, then launches the next build on a card. Rows 1–4, 39 and 40 must be in before the first launch on a fixed file: until then `CLAUDE.md` sends every worker to `## Start here` and L67 names three checkers.

## START-SET — the files the desk reads at start are SMALLER after the fold
Measured 2026-09-30. BEFORE: `wc -c` of each file, and `grep -b -n` of the heading where the start read ends. Each text: `grep -b -n -A2 -F "~~~start"` on this file — the bytes of a text are the offset of its closing fence minus the offset of the text, minus 1. AFTER = before − old + new. A row that grows a start file names the larger cut that pays for it.

| row | start file | old B | new B | change | the larger cut, when it grows |
|---|---|---|---|---|---|
| 1 | LAWS Index `:77` | 188 | 180 | −8 | |
| 3 | LAWS Index `:85` | 95 | 101 | +6 | row 4, same file (−48) |
| 4 | LAWS Index `:69` | 133 | 128 | −5 | |
| 4 | LAWS Preamble `:6` | 168 | 125 | −43 | |
| 5 | LAWS Index `:72` | 114 | 94 | −20 | |
| 7 | LAWS Index `:29` | 112 | 105 | −7 | |
| 9 | LAWS Index `:71` | 116 | 101 | −15 | |
| 21 | CHECKLIST `## handover` `:17` | 197 | 188 | −9 | |
| 36 | CONTRACT `:16` | 50 + its newline | 0 | −51 | |
| 37 | CONTRACT `:21` | 46 | 37 | −9 | |
| 38 | CONTRACT `:29` | 65 | 99 | +34 | row 36, same file (−51) |
| 39 | `CLAUDE.md:3` | 101 | 220 | +119 | row 40 (−124): the same fact leaves `cobalt.md:9` |
| 40 | `cobalt.md:9` | 228 | 104 | −124 | |
| 41 | `cobalt.md:39` | 61 | 71 | +10 | row 40, same file |
| 44 | WAKE `:13` | 98 | 146 | +48 | rows 45–48, same file (−224) |
| 45 | WAKE `:33` | 79 + 79 + 73 | 26 + 50 + 64 | −91 | |
| 46 | WAKE `:34`, `:36` | 61 + 317 | 54 + 239 | −85 | |
| 47 | WAKE `:40` | 46 | 37 | −9 | |
| 48 | WAKE `:45` | 91 | 52 | −39 | |
| 49 | LAWS Index `:65` | 97 | 114 | +17 | row 50, same file (−13), and rows 1–9 (−92) |
| 50 | LAWS Index `:68` | 125 | 112 | −13 | |
| 52 | CONTRACT `:11` | 26 | 48 | +22 | rows 36–37, same file (−60) |

| start file | what the desk reads of it | `wc -c` of the file | start part BEFORE | change | start part AFTER |
|---|---|---|---|---|---|
| `/Users/cobalt/cobalt/CLAUDE.md` | whole (the harness loads it) | 126 | 126 | +119 | 245 |
| `M/areas/cobalt.md` | top to `## Build rules` | 8,287 (fourth pass, 14:5x ET; 8,099 at the third pass: the desk's `## NOW` grew) | 5,338 (`grep -b -n "^## Build rules"`; 5,150 at the third pass) | −114 | 5,224 (file: 8,173) |
| `M/LAWS.md` | top to `## Reading` | 61,011 | 9,396 | −88 (third pass −92; rows 49–50 +4) | 9,308 |
| `M/topics/cto-desk-contract.md` | whole | 6,003 | 6,003 | −4 (third pass −26; row 52 +22) | 5,999 |
| `P/CTO-DESK-WAKEUP.md` | whole | 10,146 | 10,146 | −176 | 9,970 |
| `M/topics/cto-desk-checklist.md` | `## handover`, at every handover | 14,343 | 3,196 | −9 | 3,187 |
| THE SET | | | 34,205 | −272 | 33,933 |

THE TOTAL (fourth pass, re-measured): 34,205 B before, 33,933 B after: 272 B SMALLER (the third pass: 298 B on its 34,017 B; the close's three start lines add 26; `cobalt.md`'s `## NOW` grew 188 B between the passes, which no row touches — NOW is rewritten whole at every close and refresh, ≤1,500 characters, L58). The other five start files measure today exactly as at the third pass (`wc -c`: 126, 61,011, 6,003, 10,146, 14,343; `## Reading` at byte 9,396). Five of the six start parts shrink; `CLAUDE.md` alone grows (+119) and is paid for by row 40. Rows 51, 53, 54 touch no start part (LAWS below `## Reading`, the checklist's `## close`, `SESSION-CLOSE.md`); row 49's and row 50's LAWS entries (`:294`, `:303`–`:304`) sit below `## Reading` too.
WITH THE NARROWER DESK LINE, if he approves `STANDING-LIST.md` §4: FOURTH PASS +357 B on `WAKE:13` (the line with the two denies of scratch item 4, `DESK-LINE.md` §2b) → the wake-up 10,327 B, the set 34,290 B: 85 B LARGER than today (34,205), and the WAKE-UP FILE ITSELF 181 B LARGER (10,146 → 10,327). The brain's answer to the third pass's DECISION 1 — the line goes in with a cut of dated cites in the wake-up (`CTO-DESK-WAKEUP.md:12`, `:21`, `:26`), measured at install — now needs a cut of at least 181 B to leave the wake-up smaller (the set then 96 B smaller). So the narrower line is still NOT a row of this list: it waits for that cut, measured at install. (Third pass: +285 B, the wake-up 109 B larger, the set 13 B smaller.)
NOT IN THE SET (read on a trigger, never at start): the LAWS entries below `## Reading` (rows 1–12 make several longer: L67, L62, L61, L19, L75), `UNATTENDED-LAUNCH.md` (5,601 B today; rows 13–20 make it longer), the checklist below `## handover`, `writing-rules.md` (2,748 B). `M/preferences.md` and `M/profile.md` are in the start set and no row touches them.



## ADDED BY THE DESK AFTER THE DRAFT — his ruling R56 (`reports/cto-2026-09-30.md` R56; words `cto-2026-09-30-words.md` `## R56`, 09-30)

NOT FROM THE BRAIN'S REPORT. His words: no limit on refreshes per day (the twice-a-day rule came from option A on 09-29 18:34, bundled with the scope rule; he never asked for it); never below 220,000; at or above 250,000 the first quiet moment; above 400,000 the next turn boundary even on a busy day; never mid-ruling or with a reply owed; one ruling per question, never two rulings behind one letter of an A/B. Until folded, his message governs. Byte deltas are measured at the fold (each row removes more than it adds except row 57).

### 55 · CONTRACT `:20` REFRESH line (the contract)
TODAY: `- [stated 2026-09-29 · Dejan] REFRESH: at most twice a day (R127); never below 220,000 tokens (R68); at or above 250,000, the first quiet moment while one of the day's two remains (desk reading) (checklist H1a).`
NEW: `- [stated 2026-09-30 · Dejan] REFRESH (R56): no daily limit; never below 220,000 tokens (R68); at or above 250,000, the first quiet moment; above 400,000, the next turn boundary even on a busy day; never mid-ruling or with a reply owed (checklist H1a).`

### 56 · CHECKLIST `:9` H1a and WAKE-UP `:40` LIMITS, and `cobalt.md:15`
TODAY (H1a): `H1a REFRESH LIMITS: at most twice a day (R127); never below 220,000 tokens (MEASURE, R68), whatever H1, a task change or an hour's quiet says; at or above 250,000, the first quiet moment while one of the day's two remains. A heavy read under 220,000 is read, not refreshed around. Count the day's refreshes from its `HANDOVER:` lines; on 09-29 only those after R127 (18:34).`
NEW (H1a): `H1a REFRESH LIMITS (R56, replaces R127's twice a day): no daily limit; never below 220,000 tokens (MEASURE, R68), whatever H1, a task change or an hour's quiet says; at or above 250,000, the first quiet moment; above 400,000, at the next turn boundary even on a busy day; never mid-ruling or with a reply owed. A heavy read under 220,000 is read, not refreshed around.`
TODAY (WAKE-UP `:40`, the LIMITS sentence): `LIMITS (his 09-29 R68, R127): at most twice a day; never below 220,000 tokens by MEASURE, whatever else triggers it; at or above 250,000, at the first quiet moment while one of the day's two remains.`
NEW: `LIMITS (his R68, R56): no daily limit; never below 220,000 tokens by MEASURE, whatever else triggers it; at or above 250,000, at the first quiet moment; above 400,000, at the next turn boundary even on a busy day.` The sentence `He rules only scope, dates, deploys and money; …(R127)` after it stays.
TODAY (`cobalt.md:15`): `- REFRESH ≤2 a day (R127), never below 220,000 tokens (R68); 09-30: 2 used (06:14, 14:2x).`
NEW: `- REFRESH (R56): no daily limit; never below 220,000 tokens; ≥250,000 first quiet moment; >400,000 next turn boundary.`

### 57 · PREFERENCES `:10` — one ruling per question
TODAY: `- [stated 2026-09-13 · chat] Up to ten rulings per message, each A/B + a recommendation.`
NEW: `- [stated 2026-09-13 · chat; 2026-09-30 · Dejan R56] Up to ten rulings per message, each its own A/B + a recommendation; one ruling per question — never two rulings behind one letter of an A/B.`
Also the CONTRACT `## Replies` A/B line (`:27`, "Before an A/B reaches him…") gains: `Each A/B holds ONE ruling (R56).`

### 58 · CHECKLIST H1 `:8` and the handover count
No text change beyond row 56: H1 ("Refresh at a quiet point…") stays; the per-day count of `HANDOVER:` lines is no longer kept (removed with H1a's last sentence).


### 59 · THE OPS SCRIPTS AND THE HOOK ARE TRACKED (desk, from the brain's DF-2; NOT A TEXT ROW)
HOME: `DESK-LINE.md` §2a and `STANDING-LIST.md` §4. At the fold: the desk creates `/Users/cobalt/cobalt/ops/desk/` with the four scripts (copies of the fixed `desk-launch.sh`, `desk-context.sh` and the two `wait-*` scripts) and the hook, makes the two symlinks (`/Users/cobalt/.claude/ops/<name>`, `.git/hooks/pre-commit`), commits, all before the desk line narrows. Replaces DRAFT4 DECISION 15's "his hand edit". No law text changes.
