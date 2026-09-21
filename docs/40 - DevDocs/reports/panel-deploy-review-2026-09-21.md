# PANEL DEPLOY REVIEW 2026-09-21 — one-round read of `11-panel-order-deploy.md` (hub `panel-deploy-review-0921`)

## §0 Headline
3 of 3 houses read `11` (grok, gemini, astra all answered; runs 07:15–07:25 ET). All three: no radar touch (Q1), only the branch's own files land (Q2), every allow string in `02` or branch-named (Q3, my `grep -c` = 1 for all 24 others).
Verdicts: grok `RUN IT AFTER fill launch row R__` · gemini `RUN IT` · astra `RUN IT AFTER` six folds. Launch blockers that HOLD in my file-check: 3 — `R__` unfilled (`11:10`, `:13`), the panel-order check report has NO commit on main (`11:12` demands one), and 4.5(c)'s unquoted `…/radar?frame=phone` aborts under this host's zsh (hub-found, my run).
Folds proposed: 4 (2 launch-blocking). ESCALATE: 4. Report is uncommitted — the desk commits it.

## PREFLIGHT
Rule · command · exit · allowed/DENIED

| # | rule | command | exit | result |
|---|---|---|---|---|
| A1 | authorization R13 | `grep -n "^| R13 " "…/reports/cto-2026-09-20.md"` | 0 | allowed · `86:| R13 | 13:33 ET | "Push and approved everything. …"` (approved check strings) |
| A2 | authorization R23 | `grep -n "^| R23 " …` | 0 | allowed · `206:| R23 | 17:47 ET | "yes" …` → `Bash(grok *)` / `Bash(agy *)` THROUGH 2026-09-21 23:59 ET |
| A3 | committed | `git -C /Users/cobalt/cobalt log --oneline -4 -- "docs/40 - DevDocs/reports/cto-2026-09-20.md"` | 0 | allowed · `89355f5`, `67fad04`, `e28ba05`, `df411d6` |
| A4 | authorization R5 | `grep -n "^| R5 " "…/reports/cto-2026-09-21.md"` | 0 | allowed · `16:| R5 | 06:38 ET | OVERRIDE …` carries `it needs to be done by 9:30` |
| 1 | DATE GATE | `date` | 0 | allowed · `Mon Sep 21 07:11:45 EDT 2026` → passes (2026-09-21, before 09:10) |
| 1b | DATE GATE, before launch | `date` | 0 | allowed · `Mon Sep 21 07:15:30 EDT 2026` → passes |
| 2 | METER | `grok --version` | 0 | allowed · `grok 1.0.25 (f7e67d6988e2) [stable]` |
| 3 | METER | `agy --version` | 0 | allowed · `1.2.7` |
| 4 | prompt exists | `ls -la "…/prompts/2026-09-21/11-panel-order-deploy.md"` | 0 | allowed · `25374 Sep 21 06:46` |
| 5 | STAGGER | `tail -n 3 "…/reports/bars-chunk-2-check-r3-2026-09-21.md"` | 0 | allowed · file exists; LAST NON-BLANK line starts `BARS CHUNK 2 CHECK R3 DONE …` → not running |
| 6 | STAGGER | `tail -n 3 "…/reports/panel-order-check-2026-09-21.md"` | 0 | allowed · file exists; LAST NON-BLANK line starts `PANEL ORDER CHECK DONE …` → not running |
| 7 | RECOVERY | `ls scratch/tribunal-bars-0920/panel-deploy-review` | 1 | allowed · `No such file or directory` → fresh run |
| 8 | CODEX PROBE | `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` (background) | 0 | allowed · answer `OK`, no usage-limit text → **astra: UP** |
| 9 | launch | grok (`--sandbox cobalt-job --allow "Write(…/scratch/tribunal-bars-0920/**)" -p …`), gemini (`agy --model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 20m --add-dir … --print="…"` + file-viewer-only sentence), astra (Codex read-only line) — all background, one attempt each | 0 / 0 / 0 | allowed · none DENIED, no HARNESS / METER / TIMEOUT |

Disclosures, none a stop: (i) this session's tool surface was not launched with the 14-string line; every Bash call stayed inside those prefixes except that two fact-check calls were written with an option/regex the shell rejected (`--include=*.py`, a backtick regex) and re-run corrected, and one early verification call used a `| grep -c ""` pipe (read-only, changed nothing); (ii) I ran one harmless `ls http://127.0.0.1:5010/radar?frame=phone` to test shell globbing (no network); (iii) astra ran `cat` / `nl -ba` in its own read-only sandbox (reads only, inside the packet folder); (iv) L74: no tool result in this run carried a `Claude-Session:` / file-send block.

## Packet
Folder `scratch/tribunal-bars-0920/panel-deploy-review/` (Write tool created it; no `mkdir`). Read → Write, no parts (every file < 38,000 B). Every house received the same six files (L44).

| file | source | source B | copy B | check |
|---|---|---|---|---|
| `11-panel-order-deploy.md` | `prompts/2026-09-21/11-panel-order-deploy.md` whole | 25,374 | 25,374 | sizes equal; 0 trailing-whitespace lines in source |
| `rulings.md` | `cto-2026-09-21.md` rows R3 (:14), R5 (:16) | — | 3,020 | `grep -n -x -F -f` copy against source matched exactly 2 lines (both rows byte-identical) |
| `approved-line.md` | `02-deploy-stack-3.md:3` | — | 3,966 | `grep -c -x -F -f` copy against source = 1 (byte-identical); the copy's header is line 1, the launch line is line 2 |
| `com.cobalt.aset.plist` | `/Users/cobalt/cobalt/ops/com.cobalt.aset.plist` | 2,209 | 2,209 | sizes equal; 0 trailing-whitespace lines |
| `branch.md` | `git log --stat --oneline main..s2/panel-order-0921` + `tail -n 3` of the build report | — | 1,226 | re-ran the log today; same three commits `b5914d0`, `5dc5819`, `291ce7b` |
| `QUESTIONS.md` | verbatim from `12` + the "Files in this folder" paragraph | — | 3,161 | — |

Outputs: `astra-review.md` (6,691 B, the final message only, byte for byte), `gemini-review.md` (681 B, byte for byte), `grok-review.md` (10,507 B, written by grok itself).

## CONTINUE
next: none — collation finished; the closing line below is the stop line.

## Per question
Cells are the house's own words, ≤30 words. Line cites: astra cites `11:<n>` by `nl -ba` numbering (matches the file); grok's `11` cites run one line low (it writes `:21` for the STEP-0 row, which is line 22) and `approved-line.md:1` for the launch line (line 2 of the copy); gemini gave no `file:line`.

| Q | grok | gemini | astra |
|---|---|---|---|
| Q1 radar touch | NO — launch line has no radar bootout/bootstrap/kickstart; radar only under read-only `print`; P6, P7, 4.5(f) read-only (`11:1`) | NO — the launch line only allows bootout, bootstrap and kickstart for aset, omitting any string to modify radar | NO direct radar lifecycle command (`11:1`, `:22`, `:44`, `:48`); indirect via `start_aset.sh`: UNVERIFIABLE FROM READS — `cat ops/start_aset.sh` |
| Q2 stray land | NO — `--ff-only` of one named ref, gated to the five paths; P1 dirt, other branches, session report not in the diff (`11:33`, `:17`) | NO — `--ff-only`; 3.3 pins five files; main's dirt stays uncommitted; report untracked until STEP-6 | Intended path excludes dirt and report, BUT no step verifies `/Users/cobalt/cobalt` is on `main` (or the panel-order worktree on its branch); wrong checkout would land main's docs commits (`11:25`, `:28`, `:33`, `:39`) |
| Q3 strings | YES — all byte-identical to `approved-line` or the three branch-named; step commands all covered; Write/Edit not Bash | YES; other string NONE; unmatched command NONE | YES — same three replacements; other strings none; every step command has a matching rule (`11:1`, `:32`, `:19`) |
| Q4 failure ends | No — one ending leaves aset DOWN: STEP-5(3) bootstrap failing twice; neither tree: none scripted (`11:47`) | YES; ends with aset DOWN: STEP-5(3) bootstrap failing twice; neither tree NONE | NO — DOWN possible at: P4 pre-red aset, 4.2 loaded-not-running, STEP-5(3) run-then-fail, denial after bootout / during rollback; revert-abort partial state (`11:38–48`) |
| Q5 waits | NO — unattended; `(d)-(f)` pace retries instead of a sleep; no wait/dialog/sleep; `date` ET UNVERIFIABLE | NO — unattended; every typed command covered by the allowlist | No explicit wait/dialog/sleep; recovery after a terminal denial depends on further commands (`11:19`, `:48`) |
| Q6 else | (1) `R__` blank; (2) STEP-4 CONTINUE freeze → death after bootout leaves aset DOWN, rerun ambiguity; (3) curl RED → STEP-5; (5) dirty `rules.yaml`; (6) Write not in list | NONE | (1) `R__` stops the file as supplied; (2) rerun after bootout resumes STEP-4 and may exit falsely at 4.1; (3) `tail -n 30` logs can miss / mis-pick lines |
| REVIEW | `RUN IT AFTER fill launch row R__` | `RUN IT` | `RUN IT AFTER fill launch row; verify both checkout identities; reconcile reruns; resolve terminal-denial recovery; verify rollback and service states; scope logs to this start` |

Contradiction, quoted both: Q4 — gemini `Q4 — YES; ends with aset DOWN: STEP-5 (3) bootstrap failing twice` vs grok `No. One written ending leaves aset DOWN` and astra `NO, aset UP is not guaranteed on every failure exit`. Q6 — gemini `Q6 — NONE` vs grok and astra, who both name `R__` blank (`11:10`).

## Checked against the files
`claim · who · file:line · HOLDS / DOES NOT HOLD / UNVERIFIABLE FROM READS · blocks the launch? yes/no — why · ≤30 words`

| # | claim | who | file:line | status | blocks? |
|---|---|---|---|---|---|
| 1 | No step touches `com.cobalt.radar`. `grep -n -o -E "launchctl (bootout\|bootstrap\|kickstart)…"` over real `11`: hits at lines 1, 38, 40, 48 — every one `com.cobalt.aset`. `grep -rn -l -E "launchctl\|kickstart\|bootout" src/cobalt/aset` → no files. `start_aset.sh:69` is `exec uv run python -m cobalt.aset` | all three; astra's start-script question | `11:1,38,40,48`; `ops/start_aset.sh:69` | HOLDS | no — settles astra's UNVERIFIABLE |
| 2 | Allow strings: `grep -c -F -e '"<string>"' 02-deploy-stack-3.md` = **1** for each of the 24 non-branch strings (add, commit, reset --soft HEAD~1, tag, revert --no-edit, revert --abort, status, log, diff, rev-parse, rev-list, show, jobs, heartbeat show, bootout aset, bootstrap aset, kickstart aset, print, curl 5010, grep, tail, ls, wc, date). The five-string run merge/revert/revert --abort/rebase main/rebase --abort is present in real `11` (count 1); `02` carries `merge --ff-only sprint-2/stack` (count 1) | all three (Q3) | `11:1`; `02:3` | HOLDS | no |
| 3 | `R__` is still in the file: `grep -n -F "R__"` → line 10 and line 13. Line 10 also tells the session to FAIL on an unfilled row and to find a row in `cto-2026-09-21.md` naming `11-panel-order-deploy.md`; `grep -n -E "^\| R[0-9]+ .*(11-panel-order-deploy\|12-review-panel)"` → no row yet | grok, astra (gemini said NONE) | `11:10`, `:13` | HOLDS | yes — the desk fills both places and adds the row before launch (11:10's own rule) |
| 4 | The panel-order check report has NO commit on main: `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/panel-order-check-2026-09-21.md"` → empty (07:26 ET; re-run twice). `11:12` requires NON-EMPTY, else `FAILED: not checked`. The file exists and its last line is `PANEL ORDER CHECK DONE … houses that checked: 3 of 3 … defects that HOLD: 0` | hub-found, no house raised it | `11:12` | HOLDS | yes — a desk commit of that report before launch clears it (desk action, not a text change) |
| 5 | 4.5(c) types `…/radar?frame=phone` unquoted. Test on this host, `ls http://127.0.0.1:5010/radar?frame=phone` → `(eval):1: no matches found: …` (exit 1) before any command runs. Precedent smoke rows (`deploy-p4-2026-09-19.md:45-46`, `deploy-d3-2026-09-19.md:47-48`, `deploy-2026-09-19.md:30`) curl only `/` and `/radar`, no query string. `11:46`: a curl not `200` after three attempts = RED → STEP-5 revert of a good deploy. Grok listed `5010/*` matching `?frame=phone` as unverifiable and raised the no-sleep curl RED; nobody found the glob | hub-found; grok Q6(3) adjacent | `11:44`, `:46` | HOLDS on this host's tool shell (zsh); the deploy session's own shell = UNVERIFIABLE FROM READS — `echo $SHELL` there | yes — as written the third curl aborts and reads RED, so a good deploy could roll back |
| 6 | No step verifies which branch is checked out: `grep -n -E "abbrev-ref\|show-current\|symbolic-ref\|branch --"` over `11` → no hits. Today: `/Users/cobalt/cobalt/.git/HEAD` = `ref: refs/heads/main`; `.git/worktrees/panel-order/HEAD` = `ref: refs/heads/s2/panel-order-0921` | astra Q2 | `11:22`, `:28`, `:39` | HOLDS as a text gap; the counterexample does NOT hold today; at run time UNVERIFIABLE FROM READS — `git -C /Users/cobalt/cobalt status --short --branch` | no — both checkouts are right now; the 4.3 `<pre-merge>` compare catches a mismatch after the fact |
| 7 | Rerun ambiguity: 3.4 sets `next: STEP-4` and says "NO report prose from here until STEP-4 ends"; a relaunch after a bootout re-runs 4.1 (window → "nothing is down") and 4.2 | astra Q6, grok Q6(2) | `11:34`, `:37`, `:38`, `:39` | HOLDS as text; needs the session to die inside the outage window (unproven, L70) | no — one concrete but conditional sequence; the desk watches the report and the launch |
| 8 | STEP-5(3) failing twice is the one written aset-DOWN ending, and `11` says so | grok, gemini, astra | `11:48` | HOLDS (documented, not hidden) | no |
| 9 | Astra's further DOWN routes: P4 red aset leaves state as found; 4.2 "still printed" ≠ running; a denial after bootout ends the run. Each is a prompt-text reading; every typed command matches an allow string (row 2), so a denial would come from outside the list — not settled by reads | astra Q4, Q5 | `11:19`, `:22`, `:38`, `:48` | 4.2/P4 text HOLDS; denial routes UNVERIFIABLE FROM READS — `a run of 11 itself` | no |
| 10 | Revert partial state: `11:48` calls `revert --abort` and assumes it works; the branch's three commits touch disjoint paths (`branch.md:2-12`: the report; the two DevDocs; `radar_panel.py` + its test) so a mid-range conflict is not expected | astra Q4, grok Q4 | `11:48`; `branch.md:2-12` | disjoint paths HOLDS; abort behaviour UNVERIFIABLE FROM READS — `git revert --abort` after a mid-sequence conflict | no |
| 11 | Log-tail check (b): `tail -n 30 aset.err` today shows THREE older `Started server process` lines ([72861], [80635], [19000]) and 2026-09-18 `ERROR` lines but no `Traceback` line; a stale start line would satisfy "fresh" with no pid tie; `aset.log` tail is all access lines. `.err` holds uvicorn's start lines | astra Q6 | `11:44` | HOLDS as a weakness; no traceback in today's tail | no — weak evidence, not a failure sequence |
| 12 | `date` prints ET on the host | grok Q5 | — | HOLDS — `Mon Sep 21 07:26:02 EDT 2026` | no |
| 13 | A dirty `configs/cobalt/rules.yaml` does not enter the merge: 3.3 requires the branch to carry exactly five paths and none of them is a P1 dirty path; STEP-1(b) today: `git log --stat --oneline 2c8f3d5..main -- . ':(exclude)docs'` → empty (main moved docs-only since the cut) | grok Q6(5); Q2 all | `11:22`, `:25`, `:33` | path claim HOLDS; the merge itself UNVERIFIABLE FROM READS — `git merge --ff-only s2/panel-order-0921` | no |
| 14 | Smoke (d) pattern `render_ladder(view.ladder)}{render_pool(view.pool)` → exactly 1 hit on the branch (`radar_panel.py:1126`), 0 hits on production's tree now | (none — hub check of 11:44) | `11:44` | HOLDS | no |
| 15 | Write/Edit and Read are not `--allowedTools` strings; if the harness treats the list as exclusive STEP-0's Write is denied before bootout; same shape as `02:3` | grok Q3, Q6(6) | `11:1`, `:19` | UNVERIFIABLE FROM READS — a run of the session's first Write; precedent `02` used the same list shape | no — fail-safe (before bootout) |

Also stated plainly, as `04`-style facts: (i) `11`'s launch line in the packet equals the source in size (25,374 B); (ii) the five branch paths in `3.3` match `branch.md:2-12` (report, two DevDocs, `radar_panel.py`, its test); (iii) `RESTARTS` derivation (`cobalt jobs restarts`) was not run — UNVERIFIABLE FROM READS.

## Folds proposed
For the desk to fold into a re-issued `11` (L19); I edit nothing.

1. STEP-launch row (lines 10 and 13): `R__` → the desk's real row number in both places (and the row in `cto-2026-09-21.md` must name `11-panel-order-deploy.md`, committed). — launch-blocking (row 3)
2. STEP-4.5(c): `…/radar?frame=phone` → `…/radar\?frame=phone` (backslash before the `?`, the string still starts with the approved prefix). — launch-blocking (row 5)
3. STEP-0 P1: add `git -C /Users/cobalt/cobalt rev-parse --abbrev-ref HEAD` → `main`, else `FAILED PREFLIGHT: production is not on main`. — optional (row 6, astra)
4. STEP-4 rerun: at `## CONTINUE` `next: STEP-4` add "on a relaunch print aset first; booted out → 4.3/4.4, merged → 4.4 only". — optional (row 7, both grok and astra)

Not a text change to `11`, so not counted above — desk action: commit `panel-order-check-2026-09-21.md` before the launch (row 4).

## ESCALATE
1. **Desk action before launch:** the panel-order check report is untracked on main, and `11:12` FAILs the run on an empty `git log -1 -- <that file>` (row 4). Commit it first, and do not commit anything after the launch (`11:19` desk-hold rule).
2. **`R__`** in `11:10`, `:13` is unfilled and no row names `11` yet (row 3).
3. **Smoke curl glob** (row 5): as written, 4.5(c)'s `?frame=phone` aborts in a zsh tool shell and reads RED → STEP-5 would revert a good deploy. Fold 2 fixes it.
4. **Non-blocking HOLDS gaps** for the desk to take or leave: no branch-identity gate, rerun after a mid-outage death, stale-line log check (rows 6, 7, 11).

Not escalated: no `ASK DESK`; no packet mismatch; every house answered; no house on METER / HARNESS / TIMEOUT. Time at close: before 09:15 ET (the deploy's hard clock).

PANEL DEPLOY REVIEW DONE · grok: REVIEW: RUN IT AFTER fill launch row R__ · gemini: REVIEW: RUN IT · astra: REVIEW: RUN IT AFTER fill launch row; verify both checkout identities; reconcile reruns; resolve terminal-denial recovery; verify rollback and service states; scope logs to this start · houses that read it: 3 of 3 · launch blockers that HOLD: 3 · folds proposed: 4 · ESCALATE: 4
