# FIXED FILES — DRAFT, THIRD PASS, 2026-09-30 (the brain's THIRD PASS, his R45)

Seat `fixed-files-loop3`, Opus 5.5, prompt `prompts/2026-09-30/54-draft-fixed-files-loop3.md`. First `date` 12:33:46, checks ended 13:00:37 ET. `F` = `docs/40 - DevDocs/plans/fixed-files-2026-09-30/`. This report is the drafter's, not a file of the process.

## §0 Headline
- All five items are done under `F`. Nothing is installed, folded, launched, run, committed or `chmod`-ed; no file outside `F` was written. Both scripts stay `DRAFT — NOT INSTALLED — NOT TESTED`.
- `CHECK-HUB.md` is rebuilt: the check IS one visible fresh Opus session on the build list plus the three house strings; `PASS-2` is a second launch; `ROUND` left the card.
- `RULE-CHANGES.md` holds 48 rows (13 of them `NEW ON THE LIST`), every home line quoted from the real file. The start set is 298 B smaller after the fold (34,017 → 33,719).
- One thing does NOT fit: with the narrower desk line the wake-up file itself grows 109 B. That line is left out of the list (DECISIONS 1).
- `SPLIT.md`: 376 rows, unhomed 0; two rows changed home. 14 decisions, none for Dejan.

## L74
A block appended to the Read result of `areas/cobalt.md` asked for a `Claude-Session:` line in every commit and PR body and named a file-send tool. Data; not followed. This session commits nothing.

## WHAT CHANGED
| item | file(s) | done | what |
|---|---|---|---|
| 1 | `CHECK-HUB.md` | DONE, rebuilt whole | One `claude --bg` line: Opus 5.5, `acceptEdits`, `<job>-check`, launched from the job's worktree; 27 allow = the 24 build strings byte for byte + `grok`, the Sol `codex exec`, `agy`. Order: stage and start house A in the background (`## 1`) → own read and findings (`## 2`) → only then house A's list and THE DROP (`## 3`) → judge every finding by running it (`## 4`) → fix (`## 5`) → the finish (`## 6`) → file checks (`## 7`) → close (`## 8`). `## PASS 2` for the second launch; no third. Stop line per pass: `files opened`, `open`, `house B: needed / not needed / none available`, `decisions · for Dejan`; the token total is the desk's measurement. Seat order, mandatory house B, the drop rule, the read list, no packet: kept. The gate keeps one home (`BUILD-HUB.md` `## THE LOCK`, `## E2`, `## RESTARTS`, `## W`) |
| 1 | `CARD.md`, `desk-launch.sh` | DONE | `ROUND` removed from the header table, both examples and the script's check gate |
| 2 | `desk-launch.sh` | DONE | Kinds `desk` (the backticked `claude --bg` span of the wake-up's `- LAUNCH` line, from `/Users/cobalt/cobalt`) and `prompt "<file>"` (the prompt's own line and cwd; refuses `acceptEdits` and the six write strings); `check <card> PASS-2`; a `CONTINUE` step on build and check. Shared helpers `committed`, `check_paths`, `run_launch` |
| 2 | `DESK-LINE.md` | DONE | The row on the desk's launch strings is now two rows: `desk-launch.sh desk` and `desk-launch.sh prompt`; the desk's `claude --bg` stays out |
| 3 | `BUILD-HUB.md`, `CHECK-HUB.md` | DONE | CONTINUE, DO NOT RESTART (a)–(c) in UNATTENDED RULES; RECOVERY is the new-session case only; the header, the LAWS line, PREFLIGHT and YOU CAN ALWAYS STOP no longer say a denial ends the run |
| 3 | `DEPLOY-HUB.md` | DONE | (d): a deploy never continues by message; outside the outage a refused command the hub added itself is a record; inside it the strict rule stays; the one resume is `STEP-D0` |
| 3 | `DESK-LINE.md` §4 | DONE | Keep a FAILED worker; measure with `desk-context.sh <id>` before `CONTINUE`; above 250,000 tokens a new worker; the message names a step and states a fact |
| 4 | `RULE-CHANGES.md` | DONE, new | 48 rows: LAWS 12, `UNATTENDED-LAUNCH.md` 8, checklist 15, contract 3, start files and writing rules 5, wake-up 5; NOT CHANGED; FOLD ORDER; START-SET. F1–F7 left `DESK-LINE.md` §3, which is now a pointer table |
| 4 | `DEPLOY-HUB.md`, `CARD.md`, `SPLIT.md` | DONE | The ended override: P1 (iv) and the LAWS line admit only his per-case override for one deploy (L73); the card's `RULINGS` wording; `45:1f` dropped |
| 5 | `CARD.md` | DONE | Lines 88, 94, 131, 134 and line 50; also X5 (it asked a house for `NO`) and the two L75 mentions |
| 5 | `STANDING-LIST.md` §2 | DONE | Rewritten for the one line; the head says what is new (DECISIONS 3) |
| 5 | `SPLIT.md` | DONE | 27 rows re-homed or re-worded (`L3`); counts recounted |
| — | `pre-commit-deploy-guard.sh` | NOT CHANGED | No change required it |
Also, to reach check (c): the sentence "there is no ESCALATE section" is reworded in the three hub files.

## CHECKS
(a) `ls F` (12:58) → `BUILD-HUB.md CARD.md CHECK-HUB.md DEPLOY-HUB.md desk-launch.sh DESK-LINE.md pre-commit-deploy-guard.sh RULE-CHANGES.md SPLIT.md STANDING-LIST.md`; this report makes eleven. Nothing else.

(b) Written by me: the eight changed files of the nine, `RULE-CHANGES.md`, this report. `git -C /Users/cobalt/cobalt status --short` (13:00) prints the same lines as at the session's start: nothing outside `F` is new or modified by this run.

(c) `grep -c -F "ESCALATE"` → `BUILD-HUB.md:0`, `CARD.md:0`, `CHECK-HUB.md:0`, `DEPLOY-HUB.md:0`.

(d) In `CHECK-HUB.md`: `grep -c -F "Sonnet hub"` → `0`; `grep -c -F "claude -p"` → `0`; `grep -c -F -e "--output-format"` → `0`. `grep -c "^claude --bg "` → `1` in each hub file.

(e) Every allow string of the build and check lines, `grep -c -F`, one pattern per call, over `37`, `38`, `12` (2026-09-29) and `45`, `47`, `50` (2026-09-30):

| string or run | `37` | `38` | `12` | `45` | `47` | `50` | on the line of |
|---|---|---|---|---|---|---|---|
| `"Bash(uv run pytest *)"` | 1 | 0 | 0 | 1 | 1 | 0 | build, check, deploy |
| `"Bash(uv run cobalt jobs restarts *)"` | 1 | 0 | 0 | 0 | 0 | 0 | build, check |
| run: `git add *` … `git show*` (six) | 1 | 0 | 0 | 0 | 1 | 0 | build, check |
| `"Bash(git -C /Users/cobalt/cobalt log*)"` | 1 | 1 | 1 | 0 | 1 | 1 | build, check |
| `"Bash(git -C * diff*)"` | 0 | 0 | 0 | 1 | 0 | 0 | build, check, deploy |
| `"Bash(cd *)"` | 1 | 0 | 0 | 1 | 1 | 0 | build, check, deploy |
| run: `ls *` `grep *` `tail *` `wc *` `date*` | 1 | 1 | 1 | 0 | 1 | 1 | build, check |
| `"Bash(COBALT_ENV=dev uv run pytest *)"` | 1 | 0 | 0 | 1 | 0 | 0 | build, check, deploy |
| PATTERN `"Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/` | 1 | 0 | 0 | 1 | 0 | 0 | build, check, deploy |
| PATTERN `"Bash(rm /Users/cobalt/cobalt-wt/` | 1 | 0 | 0 | 1 | 0 | 0 | build, check, deploy |
| `"Bash(COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest *)"` | 1 | 0 | 0 | 1 | 0 | 0 | build, check, deploy |
| run: the four `COBALT_ENV=dev uv run cobalt db …` | 1 | 0 | 0 | 1 | 0 | 0 | build, check, deploy |
| `"Bash(grok *)"` | 0 | 1 | 1 | 0 | 0 | 1 | check |
| `"Bash(codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only *)"` | 0 | 1 | 0 | 0 | 0 | 0 | check |
| `"Bash(agy *)"` | 0 | 0 | 1 | 0 | 0 | 0 | check |
| the three deny strings, as one run | 1 | 1 | 1 | 1 | 1 | 1 | all three |

None unmatched; none NEW. THE DEPLOY LINE was not edited in this pass. I did not grep its 50 strings one by one: one call, `grep -n -F "claude --bg"` on `45`, printed that prompt's whole launch line, and I read `DEPLOY-HUB.md`'s line against it string by string — the same 50 allow strings in the same order, with `<branch>`, `<worktree>`, `<tip merges>` and `<prod migrate strings>` standing where `45` has its values. The fixed line adds `--name` and `--add-dir /Users/cobalt/cobalt` (loop 1).

(f) Absolute paths inside allow strings against each file's `--add-dir` set, read from the three lines:

| file | path in a listed string | under |
|---|---|---|
| BUILD, CHECK | `/Users/cobalt/cobalt` (`git -C … log`; the `.env` source) | `/Users/cobalt/cobalt` |
| BUILD, CHECK | `/Users/cobalt/cobalt-wt/<worktree>/.env` | `/Users/cobalt/cobalt-wt` |
| BUILD, CHECK | `/Users/cobalt/Vault/Think` | `/Users/cobalt/Vault` |
| CHECK | the three house strings hold no absolute path | — |
| DEPLOY | `/Users/cobalt/cobalt` (git, `ops/com.cobalt.aset.plist`, `cobalt.sh`), `/Users/cobalt/cobalt-wt/<worktree>`, `/Users/cobalt/Vault/Think`, `/Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` | its four roots |
| DEPLOY | `/dev/null` (curl's `-o`) | NONE — a device, as in loops 1 and 2 |
Inside the check's house spellings (typed by the session, not allow strings): Grok's `Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/…)` and Gemini's `--add-dir /Users/cobalt/cobalt-wt/agy-trial` sit under `/Users/cobalt/cobalt-wt`.

(g) `RULE-CHANGES.md`: `grep -c "^### "` → `50` = 48 rows + the two `### L67` heading lines quoted inside row 1. `grep -c -F "NEW ON THE LIST"` → `14` = 13 rows + the legend. Every TODAY block was copied from a Read of the home file made in this session (LAWS by line ranges `:1-100`, `:161-168`, `:200-252`, `:296-380`; the other six files whole); line numbers are those reads'. The brain's line numbers had not drifted. START-SET, measured (`wc -c`; `grep -b -n` for the point where the start read ends; `grep -b -n -A2 -F "~~~start"` for each text):

| start file | `wc -c` | start part before | change | after |
|---|---|---|---|---|
| `CLAUDE.md` | 126 | 126 | +119 | 245 |
| `areas/cobalt.md` (to `## Build rules`) | 8,099 | 5,150 | −114 | 5,036 |
| `LAWS.md` (to `## Reading`) | 61,011 | 9,396 | −92 | 9,304 |
| `cto-desk-contract.md` | 6,003 | 6,003 | −26 | 5,977 |
| `CTO-DESK-WAKEUP.md` | 10,146 | 10,146 | −176 | 9,970 |
| `cto-desk-checklist.md` (`## handover`) | 14,343 | 3,196 | −9 | 3,187 |
| THE SET | | 34,017 | −298 | 33,719 |
The set is smaller. `CLAUDE.md` grows and its cut is row 40 (−124 in `cobalt.md`). The after figures are arithmetic on measured texts, not a `wc -c` of folded files.

(h) `SPLIT.md`, `grep -c -F "| <HOME> |"`, one call each: CARD `80` · CHECK `37` · DROPPED `33` · BUILD `77` · DEPLOY `137` · LIST + LAUNCH-SH + GUARD + BLANK `12` (one call, four `-e`) · UNHOMED `0`. Sum 376. Unhomed 0.

(i) `wc -c`, before (12:36) and after (12:59):

| file | before | after |
|---|---|---|
| `BUILD-HUB.md` | 28,182 | 29,987 |
| `CHECK-HUB.md` | 35,526 | 37,944 |
| `CARD.md` | 12,434 | 12,299 |
| `DEPLOY-HUB.md` | 50,972 | 52,222 |
| `desk-launch.sh` | 15,107 | 23,816 |
| `pre-commit-deploy-guard.sh` | 5,297 | 5,297 |
| `STANDING-LIST.md` | 21,664 | 21,660 |
| `DESK-LINE.md` | 18,792 | 13,818 |
| `SPLIT.md` | 50,322 | 52,972 |
| `RULE-CHANGES.md` | — | 58,621 |
| total (without this report) | 238,296 | 308,636 |
A check worker reads `CHECK-HUB.md` 37,944 B + four sections of `BUILD-HUB.md` + its card; the file did not get smaller with the hub gone, because the judging and fixing steps moved into it.

## NEW STRINGS
In the three hub files: NONE as allow strings (check (e)). On the desk line (`DESK-LINE.md` §2, `STANDING-LIST.md` §4): the 3 deny strings of loop 2, unchanged — `Edit(src/**)`, `Edit(configs/**)`, `Edit(//Users/cobalt/cobalt-wt/**)`; this pass added none.
Not new strings, and his to see before the one approval:
1. NEW COMBINATION: the three house strings on the check's `acceptEdits` write-path line. Every proven run of them was on an auto-mode hub that wrote no code.
2. GONE: `Bash(claude -p --model claude-opus-5-5 *)` (and loop 2's NEW USE of it), `--output-format json`, and `Bash(git -C /Users/cobalt/cobalt show*)` are on no fixed file's line.
3. STILL PROPOSED: the removal of `Bash(claude --bg *)` from `settings.local.json` line 9. The script now carries every launch, so nothing is left without a string.

## UNTESTED — for the desk's scratch test; none of it is resolved here
Loop 2's list, less its items 7, 8 and 10 (the `claude -p` write seat, `--output-format json`, the hub's `cd` around a background seat), which the rebuilt check removes:
1. `desk-launch.sh`: never run. More to test than in loop 2: the two new kinds; the `sed` that lifts a backticked `claude --bg` span out of the wake-up and out of a one-off prompt, and the `cd` span; the `PASS-2.` and `CONTINUE:` prefixes; the read of a check report's last line; the fill of a card path with spaces; the `eval`; the exit status.
2. `pre-commit-deploy-guard.sh`: never run.
3. Whether a deny on `Edit(<glob>)` also stops the Write tool on that glob.
4. Whether the desk can still Write a NEW card under `docs/40 - DevDocs/` once the bare `Write` is gone.
5. Whether a git hook run from a Claude session finds `claude` and `python3` on its PATH.
6. Whether `claude --bg` started from inside `sh desk-launch.sh` registers, names and attaches as a desk-typed launch does; whether `Bash(sh /Users/cobalt/.claude/ops/*)` matches a command whose path argument holds spaces.
7. `agy` on a code check: the spelling is proven on design tribunals only.
Added by this pass:
8. Under `acceptEdits`: whether `grok …`, `agy …` and the Sol `codex exec … < /dev/null` spelling match their allow strings with no dialog.
9. Under `acceptEdits`: whether a command on no allow string is REFUSED with no dialog. CONTINUE, DO NOT RESTART (a) rests on it (the brain's recommendation 4 asked for this test).
10. The check's `cd` to `agy-trial`, a house started there in the background, `cd` back: whether the house keeps `agy-trial` as its cwd and the session's later calls run in the worktree.
11. A background house with `timeout` 2700000: whether the session is re-invoked at the house's end and at the 45-minute stop, after it ended its turn to wait.
12. Whether a `CONTINUE: <step>. <fact>` message from `cto-desk` reaches a worker idle on its `FAILED:` line and resumes it, and whether the worker sees the sender's name.
13. `desk-context.sh <id>` on a worker's id (it is known on the desk's own).
14. The check's Write of its report into the main tree (`/Users/cobalt/cobalt/docs/…`) from a session whose cwd is a worktree.

## DECISIONS
None is marked FOR DEJAN: none is scope, a date, money, a carried held defect or a schema rollback.
1. THE NARROWER DESK LINE DOES NOT FIT THE START-SET RULE. With rows 44–48 the wake-up shrinks 176 B; the line adds 285 B; the wake-up would end 109 B larger than today (the set still 13 B smaller). Default taken: the line is NOT a row of `RULE-CHANGES.md`; `DESK-LINE.md` §2b says it waits for a further cut of the wake-up of more than 109 B.
2. CONTINUE (a) RESTS ON AN UNPROVEN FACT: that an unlisted command under `acceptEdits` is refused, not held on a dialog. Default: the rule is written as ruled; a dialog is case (c) — nobody presses it, a new worker takes over. UNTESTED 9.
3. THE HOUSE STRINGS ON A WRITE-PATH LINE are a new combination, and the Sol spelling carries a redirect. Default: written as the spec orders ("the build list plus the house strings"), named at the head of `STANDING-LIST.md`. UNTESTED 8.
4. A THIRD VALUE ON THE STOP LINE: `house B: none available`, beyond the spec's `needed|not needed`. It is the case "house B needed, the card not mandatory, no second house up". Default: the open items are listed under `## DECISIONS` of the check report and the line may be `ready: YES`; the judgment seat may order PASS-2 when a meter is back.
5. BOTH PASSES CARRY THE NAME `<job>-check`, as the spec says. Default: PASS-2 launches only after the pass-1 session is stopped and removed; the script does not check that.
6. ONE PLACE WHERE A TURN ENDS: the check waits for its house by ending its turn (no sleep string exists). Default: written as the one exception to "never end a turn between steps". UNTESTED 11.
7. THE CHECK LEAVES ITS WORKTREE TO START A HOUSE: Grok's and Gemini's proven spellings read inside `agy-trial`, so the session `cd`s there for that one call and back. Default: kept the proven spellings; a guard call (`git status --short --branch`) follows the return. UNTESTED 10.
8. ROW 1 (L67), MY WORDING BEYOND THE BRAIN'S: the heading is renamed (it said "three checkers for every build"; the only link is the Index line); a one-off deploy, rebase or re-land prompt outside the fixed file is still read by one other house; that read is by "one house other than its author that is up, in the seat order"; the sentence dating the old schedule (2026-09-23 18:10) and the "new build" desk reading go to history. Default: the narrowest text I could write that removes the contradiction.
9. ROWS BEYOND THE BRAIN'S LIST: 13 rows are `NEW ON THE LIST` (10, 11, 12, 15, 17, 19, 23, 24, 34, 35, 41, 43, 46). Inside listed rows, from the agreed recommendations: row 22 adds "stays `pending fold` until it is in LAWS or NOW" and "what he was answering" (recommendation 6); row 36 removes the contract line instead of rewording it; row 9 drops L61's list of command names (the standing list is their home); row 48 drops the wake-up's pointer to `UNATTENDED-LAUNCH.md` (checklist L2 keeps it). Default: written; each is the brain's to read.
10. CHECKLIST RULES ABOUT ROUNDS LEFT AS THEY ARE: K2, K3, K7, K11, K16 and L10's "the prior round ran". They may still bind design tribunals. Default: not struck, not reworded.
11. `STANDING-LIST.md` HAS NO INSTALL PATH. The rows name it without one. Default: the desk sets it at install, beside the hub files.
12. `DEPLOY-HUB.md` PROVES NOTHING ABOUT ITS OWN OTHER-HOUSE READ (row 1's deployment floor). Default: no step added; the read is the desk's row at install and at each change.
13. `desk-launch.sh prompt` REFUSES MORE THAN THE SPEC'S SIX STRINGS: also `Bash(git *)`, the `git -C <path> add|commit|merge` spellings, a line with no `--permission-mode`, without the two dialog denies, or without `--remote-control` and `--name`. Default: kept — a refusal is the safe side; a drafter line like this session's own passes.
14. `L75` LEFT THE BUILD FILE AND THE CARD (it binds design tribunals only after row 3); "build only the card's rows" stays as the fixed file's own rule. `CARD.md` changed in two places beyond the four lines named: line 50 and the example's X5.

## RECORDS
- START READ OF THIS SESSION: `CLAUDE.md` sent me to `## Start here`; the prompt said to read its sources and nothing else at start. Read: `## NOW`, `INDEX.md`, LAWS lines 1–100 (a source). Not read: preferences, profile.
- DEPARTURES FROM MY LAUNCH LINE, none refused: two `cd` calls (into `prompts/` for check (e), and back); one `git -C /Users/cobalt/cobalt status --short`; `grep -r` twice; two `grep` calls with several `-e` patterns. No file was written by Bash; no script was run.
- One Edit of `RULE-CHANGES.md` and one of `CHECK-HUB.md` appended more than 15 KB; the first Write of each was under it.
- ROWS OF `DESK-LINE.md` §3 point at `RULE-CHANGES.md` rows 4, 9, 14, 22, 37, 39, 40, 42, 45, 47.
- The wake-up's `:29` ("do not open INDEX") against `cobalt.md:8` stays as the brain listed it: no row touches it.
- `## NOW` still says checks seat "Opus 5.5 + Grok" and names K24 as it reads today: a snapshot, the desk's to rewrite.
- METER: 12:33 → 13:01, inside the 75 minutes.

## CONTINUE
next: the brain reads the ten files against `## THIRD PASS`; the desk runs the scratch test (`## UNTESTED`); he approves `STANDING-LIST.md` once; `RULE-CHANGES.md` is put in front of him and folded by the desk — rows 1–4, 39 and 40 before the first launch on a fixed file; then the install, then the next build on a card.

FIXED FILES LOOP 3 DRAFTED · folder: docs/40 - DevDocs/plans/fixed-files-2026-09-30/ · files: 10 · rule rows: 48 · new strings: 3 · decisions: 14 · for Dejan: 0
