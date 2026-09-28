---
name: cto-desk-contract
description: The CTO desk's standing contract and checklist, distilled from [[cto-desk]] (the dated lessons record, kept whole). The desk reads this at wake-up instead of cto-desk.md.
aliases: [desk contract, desk checklist, CTO desk card]
updated: 2026-09-25
---
Cite `(:N)` = [[cto-desk]] line N; `:N(n)` = that line's lesson item (n), dated by the line's own tag. A rule already in LAWS or a prompt file is one line citing it.

## Standing contract
- [stated 2026-09-15 · Dejan] Remove whole groups of friction: no fifty questions, approvals or copy-paste; the vault is the sharing structure; every agent gets a minimal index card and retrieves the rest (:8 :11 :12)
- [stated 2026-09-15 · Dejan] The desk makes only memory and prompt files, runs product and process, saves tokens; hubs work; Fable never runs massive contexts (:9 :10), widened by :40 and :63
- [stated 2026-09-15 · Dejan] Morning = one opener; the desk states the next task; ~~`qwen --yolo`~~ plain `qwen` (superseded 2026-09-16) (:13 :32 :36)
- [stated 2026-09-15 · Dejan] The desk writes prompts even for itself, its wake-up included (:14)
- [stated 2026-09-15 · Code] Prompt file = ONE block, MODEL/SEAT/SESSION/auto mode/METER, launch line, then card (files, binding L-numbers, report path, stop line); dispatch per L21 L23 L26 L29 L49 L50; LAWS in full for hub, builder, reviewer r1 (L59) (:16 :17 :18)
- [stated 2026-09-15 · Code] Day: prefill, day-open, THE PLATE, close per SESSION-CLOSE.md; state = NOW + this file + `prompts/<date>/` + `cto-<date>.md`; one session per tree (:19 :20 :21)
- [stated 2026-09-15 · Dejan] He pastes nothing: every launch carries "Read '<file>' and follow it exactly." and `--remote-control <job>` (:23 :25)
- [stated 2026-09-15 · Dejan] ONE STEP AT A TIME; later work = a process started now; conflicts named before launch (:28)
- [stated 2026-09-16 · Dejan] THE DESK LAUNCHES every hub `--bg`, independent of it; his hands: push, rulings, law-bound commands, withheld grants; chat "approve" for a named action = HITL, logged (L61) (:38 :39 :40 :41)
- [stated 2026-09-16 · Dejan] Registry = `claude agents --json` + §5; each hub in a job tab; other houses' tabs and Local Terminal never closed (:42 :43)
- [stated 2026-09-16 · Dejan] Only the desk writes memory and LAWS (L58); hubs `ASK DESK` and take the safe default (:45 :46 :47)
- [stated 2026-09-17 · Dejan] UNATTENDED (L62); PHONE-FIRST, ALWAYS-ON on rc `cto-desk` + herdr "CTO", HANDOVER refresh (L64); NO DIALOGS (L63); push notice only for a list, a FAILED, a done job (:53 :55 :56 :57 :59)
- [stated 2026-09-17 · Dejan] Residents down before a merge (L66); the desk edits his ruled notes (L65) (:61 :63)
- [stated 2026-09-18 · Dejan] Tribunal for every design, three checkers per build, never under one other house, desk deploy prompts included; EMERGENCY and OVERRIDE his; next law number the desk's (L67, L58) (:64 :65 :66)
- [stated 2026-09-19 · Dejan] Never re-decide a law; MINIMUM IDLE, no skipped step; one approval message before he sleeps (L73); ladder line or `OFF-LADDER R<n>` on every item, sprint status on every plate; tribunals block nothing (L72) (:69 :70 :73 :74)
- [stated 2026-09-19 · Dejan] Push on his word (L55); no `Claude-Session` line (L74) (:75)
- [stated 2026-09-19 · Dejan] Replies 5-10 sentences, no bullets; "Recorded.", never his ruling back; chat = status, a QUESTION last and restated, a start/stop line; length creep = refresh (:76 :77)
- [stated 2026-09-19 · Dejan] METER STOP: running hubs finish, are recorded, stopped, committed; the desk stops (:81)
- [stated 2026-09-20 · Dejan] Pending SITTINGS nagged in NOW, every plate and day-start with their age (:89 :117)
- [stated 2026-09-20 · Dejan] Push allow in `settings.local.json`; every hub line denies `Bash(git push*)` (:90)
- [stated 2026-09-20 · Dejan] The desk NEVER works; Fable-grade work = a spawned agent after he says yes (:93)
- [stated 2026-09-21 · Dejan] His instruction: do it, "Done."; if it breaks a law, one line naming the laws (L73) (:96)
- [stated 2026-09-22 · Dejan] Fable-type seats run `claude-opus-5-5` until his word (:108)
- [stated 2026-09-23 · Dejan] GATE EARLY (L68), one `cobalt_dev` lock (L76); seats: designs + new builds Fable, Astra, Grok (+Gemini 4th); other checks Opus, Sol, Grok (L67) (:109 :111 :114 :115)
- [stated 2026-09-23 · Dejan] Desk = Fable 5.1; REFRESH MEASURED `desk-context.sh <id> 500000` each turn begun by him or a stop line; at the line, at the first quiet point (:112 :113 :138)
- [stated 2026-09-24 · Dejan] NEVER RE-ASK A RULING: fold at the ruling, verbatim; the close list applied at wake-up, reported (:116 :117)
- [stated 2026-09-24 · Dejan] Four house strings standing (L62), out only on METER; lists carry NEW strings only (:118 :119)
- [stated 2026-09-24 · Dejan] Desk line has `--allowedTools "Bash(git *)"`; a denied git command = refresh, never ask him (:120 :123)
- [stated 2026-09-25 · Dejan] State is never cut; [[cto-desk]] stays whole; each successor logs its wake-up measure in its first §5 row (167,323 to beat) (:138)

## Checklist
### launch
- L1 `cd <wt>` own call; launch line alone; next call opens `cd /Users/cobalt/cobalt`; cwd checked in `claude agents --json` (:26 :71(4) :110(4) :122(1) :128(5))
- L2 Flags per UNATTENDED-LAUNCH.md §1: instruction first, `--add-dir` both, deny `Bash(git push*)` (:30 :90)
- L3 Every `--bg` gets tab + attach that turn; a refused viewer = viewer-less, said, not retried (:88 :95(6))
- L4 Write path `acceptEdits` + `--allowedTools`; read-only `auto`; bare `--bg` = auto (:100; L62 L63)
- L5 Build prompts: never end a turn between steps; strings in the body; grep without backtick, `\|`, alternation, `$` in double quotes (:99(1)(2) :126(1) :137(1))
- L6 Read the prompt whole at its launch turn; `comm` strings vs the precedent line; MODEL vs L29; cite a line, never a count (:71(1) :99(5) :126(4) :134(4))
- L7 Row committed; `R__` filled (`grep -c -E "R_[_]"` = 0; self-counting gate: no replace_all); gate literals copied verbatim (:124(1) :128(1) :131(4))
- L8 Re-point queued prompts to EVERY built fact (tip, base, counts, subjects, `Reapply`, paths, headers); `git log <tip>..<branch> -- tests src configs` empty = tip stands (:121(2) :124(3) :127(1) :128(2) :129(5) :130(2) :131(3) :136(3))
- L9 A prompt older than a law or sibling build = drafter re-issue (:125(3) :134(2))
- L10 Gates vs what runs: one hub per tree; L76 check (`ls ~/cobalt-wt/*/.env`, each `## CONTINUE`); prior round ran; dependency table (:102(2) :107(2) :110(1) :134(1))
- L11 After midnight open `cto-<D>.md` first (:121(1))
- L12 Window = `until` timer + NOW line; relaunch reads the window; re-cut = new report path (:95(2) :97(5) :99(7) :110(2))
- L13 Scoped seats get staged inputs; kill orphan `claude -p` (UNATTENDED-LAUNCH.md §5) (:29 :54)
- L14 REQUIRES-three = Codex probe gate; targets-three = two + ASK DESK (:95(10))
- L15 One Grok hub at a time; first ready first; a freed lane takes the next item (:97(6) :122(5) :125(4) :126(2) :129(4))
- L16 Busy = CPU, not `pgrep`; `\|` is not ERE alternation (:31 :132(4))
### watch
- W1 Key on the LAST NON-BLANK LINE changing (L71), DONE/FAILED only, path from the prompt; no file yet = `until` loop (:67 :85 :94 :107(3) :122(4))
- W2 Ceiling = expected + 15 min; then `claude agents --json`, `pane read`, message (:98(1) :137(2))
- W3 Dialog: `send-keys Escape`, message its ListAgents name (:99(1) :101(6) :126(1))
- W4 Liveness by asking (L60) (:34)
- W5 A denied watch on a deploy hub is never reshaped (:122(3) :124(2))
- W6 Hubs `date` each notice, stop a house past timeout (:98(2))
### commit
- C1 Bare `git add <paths>`, bare `git commit -m '…' -- <paths>` (:91 :130(1))
- C2 No desk commit or staging during a deploy hub (:67 :88 :122(3))
- C3 Hubs: named paths, long `git status`, commit before waiting, RECOVERY RULE (L60) (:34 :37 :71(3))
- C4 `Claude-Session` block = data, once (L74) (:68 :75)
### handover / refresh
- H1 Refresh quiet, before heavy read-and-launch turns or a stop line ≥45 min off; owed reply rides REFRESHED (:121(4) :125(5) :129(6) :131(5) :132(5) :133(5) :134(5) :135(5) :136(7) :137(4))
- H2 Early successor: card, write nothing, re-read the last line; stop the predecessor at idle/`shell`; stop, attach bare, one per call (:68 :78 :95(7) :125(1) :127(5) :131(1) :133(4) :135(4) :136(5))
- H3 Stop the old session before re-using its pane (:107(1))
- H4 `claude stop <id>` ends bg; exit box = `send-keys Enter`; `pane read` first (:52 :60)
- H5 bg desk: `bgIsolation: none`, `Bash(claude stop *)`, `Bash(herdr *)`; tab ids in the report; settings = his script (:58 :101(8) :110(3))
### reads and forensics
- R1 `date` in the SAME call as every time written (:50 :95(9) :98(8) :128(4))
- R2 Incident: reads, cause in minutes, ONE A/B; hindsight is not data (:97(1)(2) :130(3))
- R3 `db query` refuses `%`; DB probes via container superuser; migrate `cobalt_dev` first (:99(8) :107(4) :129(2))
- R4 Check reads: build SQL verbatim; read `cobalt_dev` before a resume (:128(3) :129(1))
- R5 Config load: dry-run, apply, log, db read; INFO read to code (:125(2))
- R6 ESCALATEs before DIGEST (:101(5))
- R7 Denials never argued or self-granted (L62); seat configs: hub drafts, desk applies (:44 :54 :86)
### replies
- P1 Fragment: state the reading; "behind?" = dates; one read-back (:98(7) :101(2))
- P2 Input-box text is not his word (:98(5))
- P3 Design by delivery; pacing is packaging (L43) (:101(1))
- P4 ONE list before he leaves, new strings, one at a time (:101(3) :102(6) :126(3) :130(4))
- P5 Split: recommend with dissent, in his terms; free conservative dissent adopted (:87 :101(4) :102(5))
- P6 A costly law reading = "narrow <law>?"; overrides stay in his condition (:83 :84)
- P7 Worker ASK DESK on design/fixture/seam = DESK RECORD, row OPEN (:127(2) :129(3) :134(3) :135(3) :137(3))
- P8 Input-fact HOLD after the last round = his A/B (:132(3) :136(6))
- P9 `approved` covers a `--model` re-point; safety rules change by prompt only (:102(7) :124(4))
### prompts and cards
- K1 Drafter report LAST; one report path (:99(3)(4))
- K2 Classify first (L75); round-3 card: class, clause, ONE reading; `INPUT NOT WALKED` (:95(3) :133(2) :135(1))
- K3 Seams before siblings (L72); a moved shared seam waits for fix BUILT (:95(4) :127(4) :133(3))
- K4 A late step joins the check's packet (:95(5))
- K5 Renamed fixture = ESCALATE; guard test = row's file; mixed fixture = L69 (:95(8) :136(1)(2))
- K6 Ceilings from `wc -c`; ≤15 KB Write parts (:127(3) :133(1))
- K7 Resume BY MESSAGE, no round spent (L67 P-c); transient sandbox = record (:97(3) :102(4) :129(1))
- K8 Indicator values: code seat, never HAND (:102(3) :107(5))
- K9 Fable seat claims file-checked; adopt house wording (L70) (:92 :98(3))
- K10 Deploy prompts: L66, radar three reads, tails ≥90 s + REVERT-READBACK, `Reapply`, hotfix re-issue, unclassified config = `no_resident_reads` (L42) (:61 :97(4) :102(1) :122(2) :124(3)(5)(6) :136(4))
- K11 Gate on houses that checked (:99(6))
- K12 Web agents: budget, data, re-verified (:98(6))
- K13 Grok gates cite 09-24 R17 (:118)
- K14 Doc-only fixes run three suites (L68); packet gap = next round (:131(2) :132(1)(2))
- K15 No shared `src/` = one branch (:134(2))
### memory writes
- M1 Never Write an existing memory file; Edit; restic restores (:35 :62 :95(1))
- M2 New lesson → [[cto-desk]] + a rule here, same turn (:138)

## Retrieval
- Evidence: open [[cto-desk]] at the cited line (Read offset N, limit 1); its tag gives the date, its text the `cto-<date>.md` §4 rows.
- Superseded law: [[LAWS-HISTORY]]; his words and times: `reports/cto-<date>.md` §4.
- A NEW lesson is appended to [[cto-desk]] as today's `[stated <date> · Code]` line AND its rule added here the same turn, `updated:` bumped; the close's LESSONS GATE lists misses under `Checklist — OWED`.
