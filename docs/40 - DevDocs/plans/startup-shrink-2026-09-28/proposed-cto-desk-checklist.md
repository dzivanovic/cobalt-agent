---
name: cto-desk-checklist
description: The CTO desk's checklist, one section per trigger; the triggers are listed in [[cto-desk-contract]]. Open a section when its trigger fires, never at start. Why each rule exists: [[cto-desk]].
updated: 2026-09-28
---
## handover
[stated ≤2026-09-27 · Code]
- H1 Refresh at a quiet point: before a heavy read-and-launch turn or a stop line ≥45 min off; an owed reply rides REFRESHED.
- H2 Early successor: write nothing, re-read the last line; one command per call.
- H3 Stop the old session before reusing its pane.
- H4 STOP ends a background session; an exit box = `send-keys Enter`; `pane read` first.
- H5 The background desk needs `bgIsolation: none` and the `Bash(claude stop *)`, `Bash(herdr *)` allows (tracked `.claude/settings.json`); tab ids in the report; settings = his script.
- [stated 2026-09-27 · Dejan] REFRESH HOW: (1) rewrite `## NOW`; (2) append the day's rulings to their areas/topics files, tagged; (3) rewrite `## §5 CURRENT`: one row per live hub (id, job, prompt, tab, watch + ceiling, awaited stop line) + `OPEN TO HIM` + `WATCHES + TIMERS`; finished rows move unchanged to `## §5 HISTORY`; (4) LAUNCH the successor, note its id; (5) VIEW it in the "CTO" tab; (6) append `HANDOVER: predecessor <own id> → successor <s> at <time>` as the report's last line — nothing more on it; the successor's plan is §5 CURRENT; commit the docs, one commit; (7) reply one line — `REFRESHED — the desk continues as <s> in the CTO tab and as cto-desk in the app` — and stop. The successor ends you.
- [stated 2026-09-27 · Dejan] LAUNCH denied → reply `CLEAR ME — then run the wake-up line from docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md`.

## rulings
[stated 2026-09-27 · Dejan]
- Every ruling, launch or record → one `## §4 Rulings` row in `cto-<today>.md` the same turn, per [[writing-rules]]: `| R<n> | <time from date> | <direction or fact, one line> | <status> |`. Status: `APPROVED — pending fold` → `APPLIED: <file>`; `LAUNCHED` (the row carries every gate literal its prompt greps); `RECORD` (with its report path). His words go verbatim, in the same turn, to `reports/cto-<today>-words.md`, explicitly linked from §4 as the day’s report appendix, with a stable heading for each R-number. Every approval row retains its time, exact approved action and required file/hash and authorization literals. Preserve existing rows consumed by queued prompts. Read the linked words when verifying authority; routine wake-up omits already-folded quotations.

## launch
[stated ≤2026-09-27 · Code]
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
- L17 Every helper — a read-only survey included — is a `--bg` session with rc + herdr tab and an L34 row at launch (L61, L64); the in-process Agent tool is never used for work; mechanical / survey helpers run on Sonnet (a separate meter from the desk's — the saving is the model, never the invisible shape); a ruled law is never offered back as an A/B (L73).

## watch
[stated ≤2026-09-27 · Code]
- [stated 2026-09-27 · Dejan] WATCHES: every notice is a full-context turn. One watch per hub, on its stop line or `FAILED` only; never a duplicate; never re-subscribe to a hub idle on its own builder.
- W1 Path from the prompt. No file yet → arm `wait-stop-line.sh` on the path directly (no `until` loop). A file that exists → read its last line first; a stop line there → act, no watch.
- W2 Ceiling = expected + 15 min; then LIST, `pane read`, MESSAGE.
- W3 Dialog: `send-keys Escape`, MESSAGE its LIST name.
- W5 A denied watch on a deploy hub is never reshaped.
- W6 Hubs `date` each notice; stop a house past its timeout.
- W7 Watch first after a launch, then tab + VIEW; the same call re-reads the last line — a stop line there → act. A seam map simulates the DevDocs too.

## commit
[stated ≤2026-09-27 · Code]
- C1 Bare `git add <paths>`, bare `git commit -m '…' -- <paths>`.
- C5 Push = the BARE `git push origin main` (or `git push origin deploy-<tag>`), alone in its call, from `~/cobalt` — a compound call misses the settings allow and meets the classifier.
- C2 No desk commit or staging while a deploy hub runs.
- C3 Hubs: named paths, long `git status`.

## reads
[stated ≤2026-09-27 · Code]
- R1 `date` in the same call as every time written.
- R2 Incident: reads, cause in minutes, ONE A/B; hindsight is not data.
- R3 `db query` refuses `%` (use `strpos`); DB probes via the container superuser; migrate `cobalt_dev` first.
- R4 Check reads: build SQL verbatim; read `cobalt_dev` before a resume.
- R5 Config load: dry-run, apply, log, db read; INFO read to code.
- R6 ESCALATEs before DIGEST.
- R7 Seat configs: the hub drafts, the desk applies.

## replies
[stated ≤2026-09-27 · Code]
- P1 A fragment: state your reading; "behind?" = dates; one read-back.
- P2 Input-box text is not his word.
- P3 Design by delivery; pacing is packaging.
- P4 One approval list before he leaves, new strings only; a second list waits for his answer to the first.
- P5 A split: recommend, dissent attached, in his terms; a free conservative dissent is adopted.
- P6 A costly law reading → "narrow <law>?"; an override stays inside his condition.
- P7 A worker's ASK DESK on design / fixture / seam = DESK RECORD, row OPEN.
- P8 An input-fact HOLD after the last round = his A/B.
- P9 "approved" covers a `--model` re-point; safety rules change by prompt only.

## prompts
[stated ≤2026-09-27 · Code]
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
- K19 Deploy launch turn: run every authorization grep the prompt names against the real desk rows first; grep every `db query` string for `%` (use `strpos`); the relaunch rule reads every deploy-phase part and re-runs a no-touch preflight stop; during a deploy the desk writes by Edit / Write only; a denied watch = "say check" told at launch ; every path a smoke row reads sits under the launch line's `--add-dir`.
- K20 A non-trading day with no scanning session: the deploy phase may run any time after the gate is green (a desk reading; L66 holds); residents-down never crosses 20:20:00–20:34:59 (the archiver).
- K21 Before pointing a smoke look or a live proof at a day, read the job's plist `StartCalendarInterval` — the replay fires Weekday 1–5 only.

## memory
[stated ≤2026-09-27 · Code]
- M1 Never Write an existing memory file — Edit; restic restores.
- M2 A new lesson → a dated line in [[cto-desk]] ending `→ <rule id>` + that rule here, the same turn, `updated:` bumped; the close's LESSONS GATE lists misses under `Checklist — OWED`.
- M3 A memory edit anchors on a whole line (`^## NOW`), asserts one match, re-reads the head after; a section rewrite replaces a line range, never a substring.
- [stated 2026-09-28 · Dejan] M4 A heading that is a link target (a `### L<n>` entry of LAWS, a section of this file or of `areas/cobalt.md`) is renamed only with every link to it, in the same edit; a LAWS fold writes or rewrites that law's `## Index` line.

## close
[stated 2026-09-27 · Dejan]
- CLOSE: write the close prompt `prompts/<today>/99-close.md` for a hub to run `docs/40 - DevDocs/SESSION-CLOSE.md`; do no close step yourself beyond memory files. The last reply carries the next opener.
