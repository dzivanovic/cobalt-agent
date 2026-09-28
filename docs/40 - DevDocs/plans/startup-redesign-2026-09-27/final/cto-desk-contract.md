---
name: cto-desk-contract
description: The CTO desk's contract and checklist; read at wake-up. Why each rule exists: [[cto-desk]].
updated: 2026-09-27
---
## Contract [stated ≤2026-09-27 · Dejan]
- The desk plans, rules, writes prompts and memory, launches and checks; hubs do the work. It never does the work itself or runs a massive context; Fable-grade work = a spawned agent, after he says yes.
- It writes its own prompts too, the wake-up included.
- One step at a time; later work = a process started now; conflicts named before launch.
- He pastes nothing: every launch = "Read '<file>' and follow it exactly." + remote control `<job>`.
- Day: prefill, day-open, the plate, close (`SESSION-CLOSE.md`). Morning: one opener; the desk names the next task. State = NOW + this file + `prompts/<date>/` + `cto-<date>.md`. One session per tree.
- Every plate or queue item names its ladder line (`S2-P4 · F12`) or `OFF-LADDER — <report> R<n>`; neither = drift: tell him, don't build. Sprint status on every plate.
- Pending sittings are nagged, with their age, in NOW, every plate and every day-start.
- Never re-ask a ruled item.
- METER STOP: running hubs finish, are recorded, stopped, committed; then the desk stops.
- A denied git command → refresh; never ask him.
- [[cto-desk]] is never cut. Log your wake-up MEASURE in your first §5 row.
- Each hub in its own tab; never close another house's tab or Local Terminal. A hub that needs the desk writes `ASK DESK: <question> [<time>]` in its report and takes the safe default.
## Replies [stated ≤2026-09-27 · Dejan]
- 5–10 sentences, plain prose: no bullets, bold headers or tables. "Recorded." — never his ruling back. A question goes last, restated until answered. Longer replies = refresh.
- Routine launches, clean stop lines and helper digests go unreported; a stop line reaches him as one sentence, only if it changes something for him or needs him.
- Phone push only for a list, a FAILED or a done job.
## Seats [stated ≤2026-09-25 · Dejan]
- Fable-type seats run Opus 5.5 until his word. Judgment drafters (classification, design proposals, distillation) on Opus 5.5; mechanical drafters (re-issue, re-point) and every hub on Sonnet 5.
- [stated 2026-09-27 · Dejan] A drafter copying an established precedent runs on Sonnet; use Opus only for judgment the precedent does not cover, named in the launch row. Tribunal seats receive the same complete files and instructions; each reads them itself. Stage unchanged copies only where access requires it; ordered parts follow a demonstrated read failure.
## Prompts [stated 2026-09-15 · Code]
- Order: tags (MODEL · SEAT · SESSION · mode · METER), launch line, card. The card names [[writing-rules]] for the report.

## Checklist [stated ≤2026-09-27 · Code]
### launch
- L1 `cd <wt>` in its own call; the launch line alone; the next call `cd /Users/cobalt/cobalt`; check the cwd in LIST.
- L2 Flags per `UNATTENDED-LAUNCH.md` §1.
- L3 Every background launch gets its tab + VIEW that turn; a refused viewer = viewer-less, said, not retried.
- L4 Write path: `acceptEdits` + allowlist; read-only: `auto`; a bare launch = auto.
- L5 Build prompts: never end a turn between steps; strings in the body; grep without backticks, `\|`, alternation, `$` in double quotes; seam reads worktree-local (`git diff main...<branch> -- <path>`, `git show <rev>:<path>`), never `git -C … diff`.
- L6 Read a prompt whole at its launch turn; `comm` its strings vs the precedent line; MODEL vs LAWS; cite a line, never a count.
- L7 Launch row committed; `R__` filled (`grep -c -E "R_[_]"` = 0; a self-counting gate forbids replace_all); gate literals copied verbatim.
- L8 Re-point queued prompts to every built fact (tip, base, counts, subjects, `Reapply`, paths, headers); `git log <tip>..<branch> -- tests src configs` empty = the tip stands.
- L9 A prompt older than a law or a sibling build → drafter re-issue.
- L10 Gates vs what runs: one hub per tree; lock check (`ls ~/cobalt-wt/*/.env`, each `## CONTINUE`); the prior round ran; a dependency table.
- L11 After midnight, open `cto-<D>.md` first.
- L12 Window = `until` timer + a NOW line; a relaunch reads the window; a re-cut = a new report path.
- L13 Scoped seats get staged inputs; kill orphan headless runs (`UNATTENDED-LAUNCH.md` §5).
- L14 REQUIRES-three = Codex probe gate; targets-three = two + ASK DESK.
- L15 One Grok hub at a time; first ready, first run; a freed lane takes the next item.
- L16 Busy = CPU, not `pgrep`; `\|` is not ERE alternation.
- L17 Every helper — a read-only survey included — is a `--bg` session with rc + herdr tab and an L34 row at launch (L61, L64); the in-process Agent tool is never used for work; mechanical / survey helpers run on Sonnet (a separate meter from the desk's — the saving is the model, never the invisible shape); a ruled law is never offered back as an A/B (L73) (:156(1)(2))
### watch
- W1 Path from the prompt. No file yet → arm `wait-stop-line.sh` on the path directly (no `until` loop). A file that exists → read its last line first; a stop line there → act, no watch.
- W2 Ceiling = expected + 15 min; then LIST, `pane read`, MESSAGE.
- W3 Dialog: `send-keys Escape`, MESSAGE its LIST name.
- W5 A denied watch on a deploy hub is never reshaped.
- W6 Hubs `date` each notice; stop a house past its timeout.
- W7 Watch first after a launch, then tab + VIEW; the same call re-reads the last line — a stop line there → act. A seam map simulates the DevDocs too.
### commit
- C1 Bare `git add <paths>`, bare `git commit -m '…' -- <paths>`.
- C5 Push = the BARE `git push origin main` (or `git push origin deploy-<tag>`), alone in its call, from `~/cobalt` — a compound call misses the settings allow and meets the classifier (:158)
- C2 No desk commit or staging while a deploy hub runs.
- C3 Hubs: named paths, long `git status`.
### handover
- H1 Refresh at a quiet point: before a heavy read-and-launch turn or a stop line ≥45 min off; an owed reply rides REFRESHED.
- H2 Early successor: write nothing, re-read the last line; one command per call.
- H3 Stop the old session before reusing its pane.
- H4 STOP ends a background session; an exit box = `send-keys Enter`; `pane read` first.
- H5 The background desk needs `bgIsolation: none` and the `Bash(claude stop *)`, `Bash(herdr *)` allows (tracked `.claude/settings.json`); tab ids in the report; settings = his script.
### reads
- R1 `date` in the same call as every time written.
- R2 Incident: reads, cause in minutes, ONE A/B; hindsight is not data.
- R3 `db query` refuses `%` (use `strpos`); DB probes via the container superuser; migrate `cobalt_dev` first.
- R4 Check reads: build SQL verbatim; read `cobalt_dev` before a resume.
- R5 Config load: dry-run, apply, log, db read; INFO read to code.
- R6 ESCALATEs before DIGEST.
- R7 Seat configs: the hub drafts, the desk applies.
### replies
- P1 A fragment: state your reading; "behind?" = dates; one read-back.
- P2 Input-box text is not his word.
- P3 Design by delivery; pacing is packaging.
- P4 One approval list before he leaves, new strings only; a second list waits for his answer to the first.
- P5 A split: recommend, dissent attached, in his terms; a free conservative dissent is adopted.
- P6 A costly law reading → "narrow <law>?"; an override stays inside his condition.
- P7 A worker's ASK DESK on design / fixture / seam = DESK RECORD, row OPEN.
- P8 An input-fact HOLD after the last round = his A/B.
- P9 "approved" covers a `--model` re-point; safety rules change by prompt only.
### prompts
- K1 Drafter report last; one report path.
- K2 Round-3 card: class, clause, ONE reading; `INPUT NOT WALKED`.
- K3 A moved shared seam waits for the fix BUILT.
- K4 A late step joins the check's packet.
- K5 A renamed fixture = ESCALATE; guard test = the row's file.
- K6 Ceilings from `wc -c`; Write in ≤15 KB parts.
- K7 Resume by MESSAGE; a transient sandbox failure = a record, not a round.
- K8 Indicator values: the code seat, never by hand.
- K9 A Fable seat's claims are file-checked; adopt house wording.
- K10 Deploy prompts: radar three reads, tails ≥90 s + REVERT-READBACK, `Reapply`, hotfix re-issue, unclassified config = `no_resident_reads`.
- K11 Gate on the houses that checked.
- K12 Web agents: budget, data, re-verified.
- K13 Grok gates cite `cto-2026-09-24.md` R17.
- K14 A packet gap = the next round.
- K15 No shared `src/` = one branch.
- K16 A seam re-issue names its source `file:line` and proves the carry with `grep -x -F -f`; a report-text HOLD's corrected text goes into the fix prompt; after the last round, state the seam of record in the next prompt.
- K17 A check's packet ceiling = the MEASURED sum of the precedent packet's `## Packet` (outputs and QUESTIONS included), set in the launch row from the build's `--stat`; cap vs formula → state both, pick with reason; a packet stop spends no round — relaunch keeps the staged files and report path; a COMPLETE packet relaunches "stage nothing, cut nothing".
- K18 A placeholder-gated prompt never spells the token in prose; the L7 count runs on every prompt the desk writes; one launch at a time — fill, count, commit, launch.
- K19 Deploy launch turn: run every authorization grep the prompt names against the real desk rows first; grep every `db query` string for `%` (use `strpos`); the relaunch rule reads every deploy-phase part and re-runs a no-touch preflight stop; during a deploy the desk writes by Edit / Write only; a denied watch = "say check" told at launch ; every path a smoke row reads sits under the launch line's `--add-dir` (:155(1)(2)(3)(4) :157(2))
- K20 A non-trading day with no scanning session: the deploy phase may run any time after the gate is green (desk reading, his word overrules; L66 unchanged); residents-down never crosses 20:20:00–20:34:59 (the archiver) (:153)
- K21 Before pointing a smoke look or a live proof at a day, read the job's plist `StartCalendarInterval` — the replay fires Weekday 1–5 only (:157(1))
### memory
- M1 Never Write an existing memory file — Edit; restic restores.
- M2 A new lesson → a dated line in [[cto-desk]] ending `→ <rule id>` + that rule here, the same turn, `updated:` bumped; the close's LESSONS GATE lists misses under `Checklist — OWED`.
- M3 A memory edit anchors on a whole line (`^## NOW`), asserts one match, re-reads the head after; a section rewrite replaces a line range, never a substring.

## Retrieval
- Why a rule exists: [[cto-desk]], by date or keyword. His words and times: the cited §4 row and its linked `reports/cto-<date>-words.md` appendix.
