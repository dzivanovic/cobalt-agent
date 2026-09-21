# DEGRADED LINE DEPLOY REVIEW 2026-09-21 — one-round read of `16-degraded-line-deploy.md` by houses other than its author (L67)

## §0 Headline
- Three of three houses read `16` (grok, gemini, astra; no HARNESS / METER / TIMEOUT). Verdicts split: grok `RUN IT AFTER`, astra `RUN IT AFTER`, gemini `DO NOT RUN`.
- Two launch blockers HOLD in my file-check: (1) STEP-0 P12 rejects the completed branch as written (`df0011a docs(devdocs)` sits above the code tip); (2) STEP-4.5(b)'s "stamped at or after `<t up>`" radar line can miss three immediate tails → false RED → rollback of a good deploy. Seven further text gaps HOLD, none blocking (relaunch rule, STEP-5, branch-prefix, downtime bound).
- All 30 allow strings and 3 denies checked by `grep -c -F` against `02` / `11`: 27 count 1, the 3 branch-named count 0, deny count 1. Nothing else lands: the merge carries only `branch.md`'s files; nothing in `16` touches the radar outside 20:00–21:00 on the first run.
- 9 folds proposed; ESCALATE: 4. The desk folds and re-issues `16` (L19); no second round.

## PREFLIGHT
Authorization (each its own call):

| rule | command | exit | result |
|---|---|---|---|
| R13 | `grep -n "^| R13 " …/reports/cto-2026-09-20.md` | 0 | allowed — `:86` "Push and approved everything. …" (13:33 ET; the approved check strings) |
| R23 | `grep -n "^| R23 " …/reports/cto-2026-09-20.md` | 0 | allowed — `:206` "yes" — `Bash(grok *)` / `Bash(agy *)` stand THROUGH MONDAY 2026-09-21 23:59 ET (17:47 ET) |
| commit trail | `git -C /Users/cobalt/cobalt log --oneline -4 -- "docs/40 - DevDocs/reports/cto-2026-09-20.md"` | 0 | allowed — `89355f5`, `67fad04`, `e28ba05`, `df411d6` (committed) |
| R10 | `grep -n "^| R10 " …/reports/cto-2026-09-21.md` | 0 | allowed — `:22` carries `"A and this evenuing"` (07:4x ET) |

Meter and inputs:

| # | rule · command | exit | result |
|---|---|---|---|
| 1 | `date` — THE DATE GATE | 0 | allowed — `Mon Sep 21 08:57:18 EDT 2026` (not 2026-09-22 or later; before 19:30 ET) |
| 2 | `grok --version` | 0 | allowed — `grok 1.0.25 (f7e67d6988e2) [stable]` |
| 3 | `agy --version` | 0 | allowed — `1.2.7` |
| 4 | `ls -la "…/prompts/2026-09-21/16-degraded-line-deploy.md"` | 0 | allowed — `-rw-r--r-- 1 cobalt staff 30441 Sep 21 08:56` |
| 5 | `tail -n 3 "…/cobalt-wt/degraded-line/docs/40 - DevDocs/reports/degraded-line-build-2026-09-21.md"` | 0 | allowed — last non-blank line starts `DEGRADED LINE BUILT c183ed6 | on d87f3bd | offline 2208/0 …` (the branch exists) |
| 6 | STAGGER `tail -n 3 "…/reports/degraded-line-check-2026-09-21.md"` | 0 | allowed — file exists; last non-blank line is `DEGRADED LINE CHECK DONE · … · houses that checked: 3 of 3 · defects that HOLD: 0 · … ESCALATE: 0` — not `(run in progress …)`, so `15` is NOT running |
| 7 | `ls scratch/tribunal-bars-0920/degraded-line-deploy-review` | 1 | allowed — `No such file or directory` = fresh run |
| 8 | THE CODEX PROBE (`run_in_background`) `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` | 0 | allowed — reply `OK`, exit 0, no usage-limit text → **astra: UP** |
| 9 | `date` — THE DATE GATE, second row, immediately before the house launches | 0 | allowed — `Mon Sep 21 09:01:56 EDT 2026` |

No rule was denied. `mkdir` was not run (the Write tool created the folder); the `s2-p2-cards` strings were not touched.

## Packet
Folder: `scratch/tribunal-bars-0920/degraded-line-deploy-review/` (under `/Users/cobalt/cobalt-wt/agy-trial/`). Every file Read → Write; `wc -c` per copy against its source; the trailing-whitespace count (`grep -c -E "[[:space:]]$"`) of every whole-file source was **0**, so each whole copy must match to the byte.

| file | source | bytes (copy · source) | check |
|---|---|---|---|
| `16-degraded-line-deploy.md` (whole, NOT split — under 38,000 B) | `…/prompts/2026-09-21/16-degraded-line-deploy.md` | 30,441 · 30,441 | equal; `grep -v -x -F -f` shows only the 13 blank-line positions (BSD grep's empty-pattern quirk), every non-blank line identical |
| `rulings.md` | `cto-2026-09-21.md:22` (R10) | 608 · — | R10 row found verbatim in source (`grep -c -x -F -f` = 1); one header line added |
| `approved-line.md` | `02-deploy-stack-3.md:3` + `11-panel-order-deploy.md:1` | 7,299 · — | each launch line found verbatim in its source (count 1 each); two header lines added |
| `com.cobalt.aset.plist` | `/Users/cobalt/cobalt/ops/com.cobalt.aset.plist` WHOLE | 2,209 · 2,209 | equal |
| `com.cobalt.radar.plist` | `/Users/cobalt/cobalt/ops/com.cobalt.radar.plist` WHOLE | 1,216 · 1,216 | equal |
| `clock.md` | archiver `:54-61`, replay `:36-43`, backup `:71-80`, `tunables.yaml:275-293` | 3,381 · — | read with the Read tool; each block headed by path and line range |
| `branch.md` | `git log --stat --oneline main..s2/degraded-line-0921` + `tail -n 3` of the build report | 1,357 · — | outputs as printed, each headed by its command |
| `lessons.md` | `panel-deploy-review-2026-09-21.md:71, :72, :73, :77` (rows 5, 6, 7, 11) | 2,543 · — | all four rows found verbatim in source (`grep -c -x -F -f` = 4); header names path and lines |
| `QUESTIONS.md` | `17-review-degraded-line-deploy.md:14` | 4,270 · — | the verbatim paragraph is an exact substring of the prompt (`grep -o -F -f`); one "Files in this folder:" paragraph appended |

Sum 53,324 B. The plist copies are the repo copies under `/Users/cobalt/cobalt/ops/`; the resident `16` boots the radar from `/Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist` (a separate file, not staged) and the aset from the repo path. `16` was NOT split; no `.partN` files.

House outputs: `astra-review.md` (10,411 B, astra's final message only, written by me byte for byte), `gemini-review.md` (printed by `agy`, written by me byte for byte, the harness's `[exited with code 0]` marker dropped), `grok-review.md` (7,566 B, written by grok itself).

## CONTINUE
next: none — collation complete; the report's last line is the stop line.

Launches (all `run_in_background`, one attempt each): grok, gemini, astra at 09:02 ET. Astra finished ≈09:04, gemini ≈09:06, grok ≈09:11. No harness or meter message from any house; grok's `-p` reply was only its output path.

## Per question
Each cell is the house's own words (≤30 words), with its `file:line` (citations are to `16-degraded-line-deploy.md` unless named).

| Q | grok | gemini | astra |
|---|---|---|---|
| Q1 radar outside window / mid-merge at 20:30 | "YES — RELAUNCH RULE of STEP-3.4 (`:33`)… no 20:00 floor and no `2026-09-21` check"; first run inside the pause; STEP-5 may overlap 20:30 but is not a merge. | "YES — the RELAUNCH RULE… if `date` is after 20:25 ET, it skips 4.3 and goes straight to 4.4, which bootstraps `com.cobalt.radar`"; NOT mid-merge (4.1 enforces <20:25). | "YES: the clock rules do not cover every path" — 4.3 has no deadline (`:36–40`); STEP-5 multi-commit revert across 20:30 (`:47`); relaunch boots out before a clock check (`:33`). |
| Q2 merge lands other files | "NO — 4.3 is only `merge --ff-only s2/degraded-line-0921` (`:38`)… 3.3 requires… exactly those" four paths (`:32`). | "NO — `git merge --ff-only` merely updates HEAD… STEP-3.3 verifies the branch contains only its own 4 files." | "NO" — plus two gate weaknesses: 3.3 checks the net diff; branch identity prefix-checked (`:21`, `:32`, `:38`). |
| Q3 allow strings | "every `--allowedTools` string on `16:1` is byte-identical… except the three BRANCH-NAMED"; `curl` and `grep` spellings allowed. | "YES — every allowed tool string matches `02` exactly or is one of the three branch-named strings"; `curl`/`grep` allowed. | "The allow-string comparison passes"; tables `curl … \?frame=phone` against `…5010/*` and `grep -c -F` against `grep *`. |
| Q4 failure endings | "Not every branch": only STEP-5(3) bootstrap failing twice ends DOWN (`:47`); no neither-tree ending; table of 11 branches. | Resident DOWN: "a failure in the STEP-5(1) bootout… and a failure in the STEP-5(3) bootstrap"; no neither-tree ending. | "NO": DOWN via STEP-5 exhausted, a denial in recovery, loaded-but-stopped relaunch (`:33`,`:36`); neither-tree via interrupted rollback, failed `revert --abort` (`:47`). |
| Q5 waits / dialogs | "NO. No sleep or wait… 4.5 says never a wait command (`:44`)"; desk live-page confirm is after smoke. | "NO — the script contains no dialogs, sleeps, or waits." | "No explicit human wait…"; `UNVERIFIABLE FROM READS` that Read/Write/Edit run unattended (`:18`,`:21`). |
| Q6 four lessons | All FOLDED: `?` → 4.5(c); branch → P0b; relaunch → 3.4 ("the same rule opens Q1's 20:00-floor hole"); log → P8 + 4.5(b). | All FOLDED: 4.5(c), P0b, 3.4, P8 + 4.5(b). | `?` FOLDED; branch "NOT FOLDED completely" (prefix match); relaunch "NOT FOLDED completely"; log FOLDED P8 + 4.5(b). |
| Q7 other | Relaunch next-day merge + radar bootstrap (`:33`); 4.5(b) false RED "if that line is cycle-only" — UNVERIFIABLE FROM READS. | 4.5(b): "all three rapid checks will fail, falsely triggering a RED and rolling back a perfectly good deploy"; UNVERIFIABLE FROM READS. | (1) P12 rejects the completed branch (`:21`, `branch.md:2–16`); (2) 4.5(b) `<t up>` freshness (`:39`,`:43`,`:45`); (3) STEP-5 reruns `paused_market_reset` check; (4) STEP-5 no arm if shutdown fails. |
| closing line | `REVIEW: RUN IT AFTER relaunch re-checks date and 20:00` | `REVIEW: DO NOT RUN 4.5(b) rapid log checks will falsely fail if radar doesn't log instantly on boot.` | `REVIEW: RUN IT AFTER fix P12; enforce archiver-safe timing; gate every relaunch by clock and state; exact-match branches; complete failure recovery; correct smoke freshness` |

Where the houses contradict each other (quoted, not smoothed):
- Q1: grok/gemini locate the hole only in the relaunch rule; astra adds the 4.3 no-deadline and STEP-5-across-20:30 paths. Gemini: "It does NOT leave production mid-merge"; astra: "A run can pass at 20:24, stall during bootout/verification, then begin or remain inside the merge at 20:30."
- Q4: grok: "Neither-tree: none." Astra: "Interrupted rollback… HEAD can be neither `<pre-merge>` nor the branch tip, with residents DOWN." Gemini names a STEP-5(1) bootout failure; grok and astra do not.
- Q6: grok and gemini "FOLDED" for all four; astra "NOT FOLDED completely" for branch identity and for the relaunch rule.
- Q7: only astra found P12; gemini and astra both raised 4.5(b) freshness and grok raised it as UNVERIFIABLE; only gemini's closing line is `DO NOT RUN`.

## Checked against the files
`claim · who · file:line · HOLDS / DOES NOT HOLD / UNVERIFIABLE FROM READS · blocks the launch? yes/no — why · ≤30 words`. Real files opened: `16` (`/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-21/16-degraded-line-deploy.md`), `02`, `11`, the plists under `/Users/cobalt/cobalt/ops/`, `cto-2026-09-21.md`, `logs/radar.err`, the branch.

| # | claim | who | file:line | status | blocks? |
|---|---|---|---|---|---|
| 1 | P12 permits "ONLY the build's own report commit(s)"; the real `git -C /Users/cobalt/cobalt log --oneline c183ed6..s2/degraded-line-0921` prints TWO commits: `5c31876 docs(report): …` and `df0011a docs(devdocs): radar_panel …`. Build report `:160` says D1 `df0011a` sits above the code tip. | astra | `16:21`; `degraded-line-build-2026-09-21.md:160,184`; `branch.md:2-8` | HOLDS as text (the first clause fails on `df0011a`; the FAILED clause names only "a code commit") | **yes** — a literal read ends `FAILED PREFLIGHT` before anything is down; the deploy does not run |
| 2 | 4.5(b) wants a `radar cycle: paused_market_reset` line stamped at or after `<t up>`, three tails, no wait. 09-19's restart: `F17 … RUNNING` 08:21:42.478, first cycle 08:21:42.556 (78 ms later), next 08:23:22.593 (100 s). `<t up>` is a later `date` call, so the first cycle predates it; only the second (≈+100 s) qualifies. | astra, gemini; grok (UNVERIFIABLE) | `16:43`; `logs/radar.err:3868,3878,3879` | HOLDS as a sequence; whether three tails reach +100 s = UNVERIFIABLE FROM READS — a run of 4.4–4.5 | **yes** — a miss = RED → STEP-5 revert of a good deploy, using the evening's one deploy (L43) |
| 3 | Relaunch rule has no date floor and no date check on the bootout arm: "Either NOT loaded and main = `<pre-merge>` → skip 4.1–4.2 (bootout only the one still loaded), then 4.3 only if `date` is before 20:25" — a relaunch any earlier day/hour merges and bootstraps the radar. | grok, gemini, astra | `16:33` | HOLDS as text; needs the session to die inside the outage window and be relaunched outside it (unproven, L70) | no — conditional on a session death; the desk launches and watches |
| 4 | "Both loaded → resume at 4.1"; at/after 20:25, 4.1 exits "nothing is down" without checking that both are running. | astra | `16:33`, `:36` | HOLDS as text | no — needs a resident loaded-but-stopped at relaunch |
| 5 | Relaunch rule has no case for a revert interrupted after one commit (HEAD neither `<pre-merge>` nor the branch tip). | astra | `16:33`, `:47`; `branch.md:2-11` (three commits) | HOLDS as text | no — needs the session to die inside STEP-5 |
| 6 | STEP-5(4) re-runs 4.5(b), which demands `paused_market_reset`; after 21:00 the line shape is `idle:overnight` (09-19 `radar.err:3878`). | astra | `16:43`, `:47` | HOLDS as text | no — needs a rollback after 21:00 |
| 7 | STEP-5(1) requires `Could not find service` after each bootout but names no arm if a resident still prints (4.2 has one). | astra | `16:37`, `:47` | HOLDS as text | no — needs an allowed `bootout` to fail |
| 8 | P0b: "FIRST line starts `## main`" / "starting `## s2/degraded-line-0921`" — a prefix match. Real state now: `/Users/cobalt/cobalt/.git/HEAD` = `ref: refs/heads/main`; `.git/worktrees/degraded-line/HEAD` = `ref: refs/heads/s2/degraded-line-0921`. | astra | `16:21` | HOLDS as a text gap; the counterexample does NOT hold today | no — both checkouts are right now |
| 9 | 4.1 is the only clock check; "over 60 s is not a failure, it is recorded and ESCALATED"; 4.3 has no second deadline. 3.3's empty diff on `src/cobalt/archiver`, `radar`, `cards`, `session`, `db_migrations`, `configs`, `ops` means the archiver reads identical code either side. | astra | `16:36`, `:40`, `:32` | HOLDS as text; a ≥5-minute stall needed to reach 20:30 (unproven) | no |
| 10 | Gemini's Q4 branch: "a failure in the STEP-5(1) bootout… halts the session with the other resident down". STEP-5 as written has no FAILED exit inside (1): it goes on to (2), (3) and states "EVERY failure path from the first bootout on ends with a bootstrap attempt of BOTH residents". | gemini | `16:47` | DOES NOT HOLD as text (a halt would need a denied allowed string) | no |
| 11 | A denied command during recovery ends the run with residents DOWN. Every recovery command has an allow string (Q3 counts below). | astra | `16:18`, `:47` | UNVERIFIABLE FROM READS — a run of `16` | no |
| 12 | Read/Write/Edit are not `--allowedTools` strings; `11` carried the same list shape and its report ends `PANEL DEPLOY DONE 72c4f12 · tag deploy-2026-09-21 · aset down 7 s …` (`deploy-2026-09-21.md`, last line). | astra | `16:1`, `:18`; `approved-line.md` | UNVERIFIABLE FROM READS for tonight; precedent ran | no |
| 13 | "The clock does not establish that everything after 21:00 is overnight idle" — `clock.md` is silent, but L43 (`LAWS.md:227`) defines it: "after the pause, before the 04:00 premarket window on a trading day". | astra | `16:47`; `LAWS.md:227` | HOLDS for the packet; DOES NOT HOLD against LAWS.md | no |
| 14 | First-run path touches the radar only inside the pause: P0 refuses before 20:00 / after 20:15; 4.1 refuses bootout at/after 20:25; STEP-5 bootouts happen only after 4.2. | grok, gemini | `16:21`, `:36`, `:47`; `clock.md:35-54` | HOLDS | no |
| 15 | The merge carries only the four paths in `branch.md`; the session's report is untracked on main until STEP-6. Real: `ls degraded-line-build-2026-09-21.md` on main → absent (no untracked collision with the branch's copy); `git show`-side stat lists exactly `radar_panel.py`, `test_radar_panel.py`, `radar_panel.md`, the build report. Whether any of the four is a dirty path on main now = UNVERIFIABLE FROM READS — `git -C /Users/cobalt/cobalt status --porcelain`. | all three (Q2) | `16:17`, `:32`, `:50`; `branch.md:2-11` | HOLDS as text | no |
| 16 | Marker: `grep -c -F "id=\"degraded-line\""` → branch worktree `radar_panel.py` **1**; production tree **0**. | grok (UNVERIFIABLE), astra (runtime fact) | `16:21` P10, `:43` (d) | HOLDS | no |

Q3, checked myself, each its own call — `grep -c -F -e '"<string>"' "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-19/02-deploy-stack-3.md"`, quotes included:
- Count **1** for all 27 non-branch strings: `add *` · `commit *` · `reset --soft HEAD~1` · `tag *` · `revert --no-edit *` · `revert --abort` · `git -C * status*` · `log*` · `diff*` · `rev-parse*` · `rev-list*` · `show*` · `COBALT_ENV=production uv run cobalt jobs *` · `… heartbeat show*` · `launchctl bootout …aset` · `bootout …radar` · `bootstrap …aset.plist` · `bootstrap …LaunchAgents/com.cobalt.radar.plist` · `kickstart -k …aset` · `kickstart -k …radar` · `launchctl print gui/501/*` · `curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/*` · `grep *` · `tail *` · `ls *` · `wc *` · `date*`.
- Count **0** (expected — the three BRANCH-NAMED strings, absent from `02`): `merge --ff-only s2/degraded-line-0921` · `cobalt-wt/degraded-line rebase main` · `cobalt-wt/degraded-line rebase --abort`. Approved by his `cto-2026-09-21.md:24` R12 ("approved").
- Deny strings `"AskUserQuestion" "EnterWorktree" "Bash(git push*)"` → count **1** against `11-panel-order-deploy.md`, and **1** in `16`.
- Every typed command has an allow string: `curl … 5010/radar\?frame=phone` ↔ `…5010/*` (the `\?` sits in the `*` tail); `grep -c -F "id=\"degraded-line\"" …radar_panel.py` ↔ `grep *`; `git -C … log -1 --format=%H -S"…" -- "…"` ↔ `git -C * log*`; `git diff --stat <cut> main -- . ':(exclude)docs'` ↔ `git -C * diff*`; the two-call report commit ↔ `add *` / `commit *`. All three houses agree with this table.

Also stated plainly: (i) `cto-2026-09-21.md` row **R19** (`:30`) is the launch row for `16-degraded-line-deploy.md` and R12 (`:24`) carries the approval of the three branch-named strings; (ii) the build report's stop line and the check report's stop line were read at PREFLIGHT rows 5 and 6; (iii) `RESTARTS` derivation (`cobalt jobs restarts`) and the live merge were not run — UNVERIFIABLE FROM READS.

## Folds proposed
For the desk, into a re-issued `16` (L19); I edit nothing. One text change per HOLDS finding (rows above).

1. (row 1, BLOCKS) STEP-0 P12: `ONLY the build's own report commit(s) (`docs(report): degraded line build …`)` → `ONLY the build's docs commits (`docs(devdocs): …`, `docs(report): degraded line build …`), no path outside docs/`.
2. (row 2, BLOCKS) STEP-4.5(b): `a `radar cycle: paused_market_reset` line STAMPED AT OR AFTER `<t up>`` → `the `F17: com.cobalt.radar RUNNING` line stamped after `<t down>`, or a cycle line at/after the pre-bootstrap `date``.
3. (row 3) STEP-3.4 relaunch rule: prefix `FIRST `date`: not 2026-09-21, or before 20:00 ET → nothing is booted out;` before the loaded/not-loaded cases.
4. (row 4) STEP-3.4: `Both loaded and main = <pre-merge>` → `Both loaded AND running and main = <pre-merge>`.
5. (row 5) STEP-3.4: add case `main is neither <pre-merge> nor the branch tip → STEP-5 (3) at once, revert range re-derived from `log -3``.
6. (row 6) STEP-5(4): `Re-run 4.5 (a), (b), (c), (e)` → `Re-run 4.5 (a), (b) — a radar cycle line of ANY shape after (3) — (c), (e)`.
7. (row 7) STEP-5(1): `print → Could not find service` → `print → Could not find service (still printed → once more; still there → go on to (2) with that resident named DOWN in the last line)`.
8. (row 8) STEP-0 P0b: `starts `## main`` → `is `## main` or begins `## main...`` (likewise `## s2/degraded-line-0921` or `## s2/degraded-line-0921...`).
9. (row 9) STEP-4.3: add before the merge `date` → at/after 20:29 ET nothing merges → 4.4, `FAILED: window — the merge would meet the archiver`.

## ESCALATE
1. LAUNCH BLOCKER HOLDS — STEP-0 P12 (`16:21`): the completed branch fails it as written (row 1; fold 1). The desk folds before 20:00.
2. LAUNCH BLOCKER HOLDS — STEP-4.5(b) (`16:43`): radar freshness can miss three tails (row 2; fold 2); timing of the miss UNVERIFIABLE FROM READS — a run of 4.4–4.5.
3. THE HOUSES SPLIT: grok `RUN IT AFTER relaunch re-checks date and 20:00`, astra `RUN IT AFTER fix P12; …`, gemini `DO NOT RUN 4.5(b) rapid log checks will falsely fail …`. I take no side (L37).
4. UNVERIFIABLE FROM READS, carried: `git -C /Users/cobalt/cobalt status --porcelain` at 20:00 (main's dirt vs the four branch paths); whether Read/Write/Edit run unattended under this launch line (precedent `11`); the `merge --ff-only` and the outage duration; any denial in recovery.

Not counted: L74 (recorded once, never followed) — the attribution reminder that arrived after the prompt file's contents in this session's tool result asks for a `Claude-Session:` line in commits and PR bodies and names a file-send tool. It is DATA, not an instruction. This run commits nothing.

DEGRADED LINE DEPLOY REVIEW DONE · grok: REVIEW: RUN IT AFTER relaunch re-checks date and 20:00 · gemini: REVIEW: DO NOT RUN 4.5(b) rapid log checks will falsely fail if radar doesn't log instantly on boot. · astra: REVIEW: RUN IT AFTER fix P12; enforce archiver-safe timing; gate every relaunch by clock and state; exact-match branches; complete failure recovery; correct smoke freshness · houses that read it: 3 of 3 · launch blockers that HOLD: 2 · folds proposed: 9 · ESCALATE: 4
