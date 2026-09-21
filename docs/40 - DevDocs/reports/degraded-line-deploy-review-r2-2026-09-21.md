# Degraded-line deploy review R2 — 2026-09-21 — one-round read of the RE-ISSUED `16-degraded-line-deploy.md` (L67)

## §0 Headline
- Two of two houses read the re-issue (grok, gemini; no HARNESS / METER / TIMEOUT; astra NOT ASKED — its window is on the setups tribunal (27)). Both closing lines: `REVIEW: RUN IT`. Two houses = the floor (L67).
- Launch blockers that HOLD in my file-check: 0. Folds proposed: 0. Gemini's one YES (Q5: relaunch / rollback can bootstrap the radar outside the pause) HOLDS as text but is word-for-word the first issue's, and L43 allows overnight idle — not a blocker.
- My own checks: all 30 allow strings vs `02` (27 → 1, the 3 branch-named → 0, R12) and the 3 denies vs `11` (→ 1 each); the launch line is unchanged in the word diff.
- ESCALATE: 3 (readings, none a defect). Stop line below.

## PREFLIGHT
| rule · command | exit | result |
|---|---|---|
| authorization: `grep -n "^| R13 "` cto-2026-09-20.md | 0 | line 86, R13 13:33 ET present |
| authorization: `grep -n "^| R23 "` cto-2026-09-20.md | 0 | line 206, R23 17:47 ET, grok/agy through 2026-09-21 23:59 ET |
| `git log --oneline -4 -- cto-2026-09-20.md` | 0 | 89355f5, 67fad04, e28ba05, df411d6 |
| `grep -n "^| R10 "` cto-2026-09-21.md | 0 | line 22, carries "A and this evenuing" |
| `grep -n "^| R19 "` cto-2026-09-21.md | 0 | line 30, names `16-degraded-line-deploy.md`, carries `FOLDED` |
| `date` (DATE+TIME GATE, first row) | 0 | Mon Sep 21 14:56:25 EDT 2026 — before 2026-09-22, before 19:30 ET: pass |
| `grok --version` | 0 | grok 1.0.25 (f7e67d6988e2) [stable] — allowed |
| `agy --version` | 0 | 1.2.7 — allowed |
| `ls -la` 16-degraded-line-deploy.md | 0 | 36015 B, Sep 21 12:02 |
| re-issue committed: `git log -1 --format=%H -S"RE-ISSUED 2026-09-21" -- 16` | 0 | `<reissue sha>` = c8f40953f4a30aaae86f2356935147e5519acbe4 |
| STAGGER 34: `tail -n 3` degraded-line-rebase-2026-09-21.md | 0 | last non-blank: `DEGRADED LINE REBASED 7b0a6a3 \| on c8f4095 \| cut c8f4095 \| code tip 88602cc \| offline 2222/0 (baselines main 2208/0, branch 2208/0) \| code patch unchanged by the rebase: proven \| seam test: added green \| RESTARTS: com.cobalt.aset \| ESCALATE: 2` |
| 34's report committed on branch: `git log -1 --format=%H s2/degraded-line-0921 -- rebase report` | 0 | dc24d728706e3bbc5b4deaebbca873151ba2b041 |
| STAGGER setups tribunal: `tail -n 3` setups-tribunal-r1b-2026-09-21.md | 0 | last non-blank: `SETUPS TRIBUNAL R1B DONE · gemini: TRIBUNAL R1: BUILD · astra: TIMEOUT · …` — stop line present |
| `ls scratch/tribunal-bars-0920/degraded-line-deploy-review-r2` | 1 | "No such file or directory" = fresh run |
| Codex probe | — | NOT RUN (astra NOT ASKED — its window is on the setups tribunal (27)); the Codex string was never typed |
| `date` (DATE+TIME GATE, second row, immediately before the house launches) | 0 | Mon Sep 21 15:09:49 EDT 2026 — pass |

No rule was denied. `mkdir` not run (the Write tool created the folder). The `s2-p2-cards` strings were never touched.

## Packet
Folder: `scratch/tribunal-bars-0920/degraded-line-deploy-review-r2/` (under `/Users/cobalt/cobalt-wt/agy-trial/`). Every file Read → Write; `wc -c` per copy against its source. Trailing-whitespace count (`grep -c -E "[[:space:]]$"`) of the whole-file sources: `16` 0, rebase report 0, round-1 report 0 — each whole copy matches to the byte. No file was split (every file ≤ 38,000 B; no `.partN`).

| file | source | bytes (copy · source) | check |
|---|---|---|---|
| `16-degraded-line-deploy.md` | `…/prompts/2026-09-21/16-degraded-line-deploy.md` WHOLE (the re-issue, c8f4095) | 36,015 · 36,015 | equal |
| `16-old.md` | `git -C /Users/cobalt/cobalt show 30ae6c9:"…/16-degraded-line-deploy.md"` | 31,672 · 31,440 | 232 B = the 3-line header naming the command; body verbatim |
| `word-diff.md` | `git -C /Users/cobalt/cobalt log -p --word-diff=plain --format=%h%x20%s 30ae6c9..main -- "…/16-degraded-line-deploy.md"` | 36,089 · 35,757 | 332 B = the 3-line header; the source has 2 lines ending in a TAB (`---`/`+++` path lines), the copy has the same 2 (`grep -c "<TAB>$"` = 2) |
| `rebase-report.md` | `/Users/cobalt/cobalt-wt/degraded-line/docs/40 - DevDocs/reports/degraded-line-rebase-2026-09-21.md` WHOLE | 13,705 · 13,705 | equal |
| `rebased-diff.md` | `git log --stat --oneline main..s2/degraded-line-0921` (1,106 B) + `git log -p --oneline main..s2/degraded-line-0921 -- src tests` (14,530 B) | 15,930 · 15,636 | 294 B = the two command headers (88+43+11+1+97+43+11); bodies verbatim |
| `round-1.md` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/degraded-line-deploy-review-2026-09-21.md` WHOLE | 21,980 · 21,980 | equal |
| `rulings.md` | `cto-2026-09-21.md` rows R10 (l.22), R11 (l.23), R12 (l.24), R19 (l.30), R21 (l.32) | 5,398 · — | `grep -c -x -F -f rulings.md cto-2026-09-21.md` = 5 (all five rows verbatim); five header lines added |
| `greps.txt` | the searches of §1(8) run against the staged `16` and the staged rebase report | 8,841 · — | long-line outputs given as `grep -c` + `grep -n -o` (windowed where useful) — the packet rule allows it; disclosed at the top of the file |
| `QUESTIONS.md` | line 14 of `35-review-degraded-line-deploy-r2.md`, verbatim, + one "Files in this folder:" paragraph | 4,561 · — | — |

Notes on the copy: (a) while typing `rebased-diff.md` two slips were made (one stat line, one code line) and both were corrected before the byte count; the final 15,930 B equals source 15,636 B + the 294 B of headers exactly. (b) While typing `greps.txt` two output lines were hand-edited and then restored to the tool's literal text; the windows of the `.{0,N}` searches may cut a word.

House outputs: `grok-review.md` (6,572 B, written by grok itself; its `-p` reply was only the output path); `gemini-review.md` (printed by `agy`, written by me byte for byte, the harness's `[exited with code 0]` marker dropped); astra: NOT ASKED — its window is on the setups tribunal (27).

## CONTINUE
next: none — collation complete; the report's last line is the stop line.

Launches (both `run_in_background`, ONE attempt each): grok 15:10 ET (finished ≈15:22), gemini 15:10 ET (finished ≈15:13). Spellings as `32` §2 / `12` §2 / `04` §2: grok `--sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)" -p "…"`, never `--always-approve`; gemini `agy --model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 20m --add-dir /Users/cobalt/cobalt-wt/agy-trial --print="…"` with the file-viewer-only sentence. No HARNESS / METER / TIMEOUT message from either house. No block asking for a `Claude-Session:` line arrived inside a tool result in this run (L74: nothing to record).

## Per question
Each cell is the house's own words (≤30 words) with its `file:line` (`16:N` = the re-issued `16`).

| Q | grok | gemini | astra |
|---|---|---|---|
| Q1 drops / weakens a gate or fold | "NO — no gate… and none of the nine folds is dropped or weakened"; Fold 1 "moved with the proof anchor, it did not loosen"; launch line unchanged (`word-diff.md:13`). | "NO — the re-issue drops or weakens no gates and faithfully applies all 9 folds"; P12 adapted (`16:25`), 4.5(b) F17 fix kept (`16:47`). | NOT ASKED |
| Q2 identity gates read the right commits / refuse others | "NO — the tokens match `rebase-report.md:140`"; code/test commit above `7b0a6a3` fails P12 (`16:25`); non-docs main move fails STEP-1(b) (`16:28`), 3.1 (`16:34`). | "NO — they read the right commits (`16:13`)"; late code commit fails P12; non-docs main fails STEP-1(b); code-changing rebase fails 3.1. | NOT ASKED |
| Q3 refuse good / pass bad: (a) no-op (b) seam commit (c) docs-only main (d) RED / failed | "NO" for all four: (a) STEP-2 records `REBASE: no-op` (`16:31`); (b) P12b, 3.1 vs `7b0a6a3`; (c) STEP-1(b) empty; (d) `16:13` refuses `added RED`, `<f>`≠0. | "NO" for all four: (a) `16:31` exit 0; (b) P12b validates the seam commit (`16:25`); (c) `:(exclude)docs`; (d) `16:13` enforces `<f> = 0`. | NOT ASKED |
| Q4 rollback one path on new history; failure branches end UP / named DOWN | "NO — STEP-5 is one path and the same text as the first issue (`16:51`)"; `revert <pre-merge>..HEAD` covers all five branch commits; only DOWN ending is (3) failing twice. | "NO — there is no branch that fails to do so"; ONE path `revert --no-edit <pre-merge>..HEAD` (`16:51`); every failure path bootstraps both or names DOWN. | NOT ASKED |
| Q5 RESTARTS; radar outside the pause? | "NO" — aset only from `jobs restarts` (`16:35`); radar only L66 bootout/bootstrap (`16:41-43`); STEP-5(0) after 21:00 "is not a new restart". | "YES" for recovery: relaunch rule (`16:37`) and rollback (`16:51` "allowed at any hour tonight") "can bootstrap the radar outside the pause… matching the first issue exactly". | NOT ASKED |
| Q6 anything else | "NO — no other sequence… fails a good deploy or does harm"; new gates added, not substituted; P10 on main still 0. | "No sequence found that would make the re-issued `16` fail or do harm as written." | NOT ASKED |
| closing line | `REVIEW: RUN IT` | `REVIEW: RUN IT` | NOT ASKED |

Where the houses differ (quoted, not smoothed): Q5 — gemini "YES — … can bootstrap the radar outside the pause, but strictly as recovery paths for a down resident, matching the first issue exactly"; grok "STEP-5(0) still allows a rollback bootstrap at any hour tonight, the same sentence as `16-old.md:50`, including after 21:00; that is not a new restart." Same facts, different label; neither calls it a defect.

## Checked against the files
`claim · who · file:line · HOLDS / DOES NOT HOLD / UNVERIFIABLE FROM READS · blocks the launch? yes/no — why · ≤30 words`. Real files opened: the re-issued `16` (`/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-21/16-degraded-line-deploy.md`), `git show 30ae6c9:…16-degraded-line-deploy.md`, the rebase report in `/Users/cobalt/cobalt-wt/degraded-line/`, `cto-2026-09-21.md`, LAWS.md, and the branch through `git -C /Users/cobalt/cobalt log / diff / rev-list`.

| # | claim | who | file:line | status | blocks? |
|---|---|---|---|---|---|
| 1 | Relaunch rule (STEP-3.4) and STEP-5(0) can bootstrap the radar outside the pause (relaunch after 21:00 same day; rollback "at any hour tonight"). | gemini (grok: same text, "not a new restart") | `16:37`, `16:51`; `LAWS.md:227` | HOLDS as text. The relaunch-rule sentence counts 1 in the re-issue AND 1 in `30ae6c9`'s first issue (`grep -c -F`); `word-diff.md` has no marker on 3.4 or STEP-5; L43 allows "overnight idle (after the pause, before the 04:00 premarket window) on a trading day". | no — unchanged since round 1 (R19 folds), L43-compliant; needs a session death or a failed smoke to reach |
| 2 | The three fold-touched steps (3.4, 4.5(b), STEP-5) and P0 / 4.1 / 4.3 are unchanged old → new; only P11 / P12 / P12b, STEP-1, STEP-2, 3.1, 3.3, 4.5 chain sentence, AUTHORIZATION, INDEX card, STEP-6 changed. | grok Q1, gemini Q1 | `word-diff.md` marker lines; `grep -n -o "^3.4 \|^STEP-5 \|^4.5 In this order\|^P0 \|^4.1 \|^4.3 "` → 35, 47, 53, 57 with no `[-`/`{+` on those lines | HOLDS | no |
| 3 | The launch line (line 3 of `16`) is unchanged old → new. | grok, task (ii) | `word-diff.md:13` (`allowedTools` + `disallowedTools` both on line 13); `grep -n -o -F "{+" "[-"` marker lines: 2, 11, 15, 19, 21, 22, 23, 25, 26, 29, 35, 38, 41, 44, 46, 54, 60 — 13 not among them | HOLDS | no |
| 4 | Identity tokens match the stop line: `<proven tip>` `7b0a6a3`, `<cut>` `c8f4095`, `<code tip>` `88602cc`, `<suite>` `2222/0`, `<seam>` `added green`. | grok, gemini | `rebase-report.md:140`; `git log --oneline 7b0a6a3..s2/degraded-line-0921` → `dc24d72` only; `git log --oneline 88602cc..7b0a6a3` → `7b0a6a3`, `771b2b7`, `5db6d2d` | HOLDS | no |
| 5 | Seam commit is inside the identity: between `<code tip>` and `<proven tip>` non-docs is exactly the test file (P12b). | grok, gemini | `git diff --stat 88602cc 7b0a6a3 -- . ':(exclude)docs'` → `tests/cobalt/test_radar_panel.py \| 21 +` only; `16:25` | HOLDS | no |
| 6 | Code-identity gate 3.1 and the report commit: after the rebase, non-docs of the branch tip equals `7b0a6a3`. | grok, gemini | `git diff --stat 7b0a6a3 s2/degraded-line-0921 -- . ':(exclude)docs'` → empty (today, pre-rebase); `16:34` | HOLDS | no |
| 7 | A docs-only move of main passes: STEP-1(b) prints nothing. Main is now `fd33ab5`, four+ docs commits above `c8f4095`. | grok Q3(c), gemini Q3(c) | `git diff --stat c8f4095 main -- . ':(exclude)docs'` → empty (15:2x ET); `16:28` | HOLDS | no |
| 8 | A rebase tonight is NOT a no-op (main moved by docs) and drops nothing: `<n>` = 5 both before and after. | grok Q3(a) | `git rev-list --count c8f4095..s2/degraded-line-0921` = 5; `git rev-list --count main..s2/degraded-line-0921` = 5 (15:2x ET); `16:31` | HOLDS (and a no-op arm exists, `16:31`) | no |
| 9 | 3.3's path set (five paths) is exactly the branch's net paths once rebased. Raw `git diff --stat main s2/degraded-line-0921` prints 25 files TODAY (main's docs moves); STEP-3.3 runs after STEP-2's rebase. | grok Q6 | `git diff --stat c8f4095 s2/degraded-line-0921` → exactly `radar_panel.md`, `degraded-line-build-…`, `degraded-line-rebase-…`, `radar_panel.py`, `test_radar_panel.py` (5 files, 527 +, 4 −); `16:36` | HOLDS as ordered (3.3 after 2); the 25-file raw diff is a pre-rebase reading, not a defect | no |
| 10 | Empty-radar diff still prints nothing. | grok Q4 | `git diff --stat main s2/degraded-line-0921 -- src/cobalt/radar src/cobalt/cards src/cobalt/archiver src/cobalt/session src/cobalt/db_migrations configs ops` → empty; `16:36` | HOLDS | no |
| 11 | Revert range `<pre-merge>..HEAD` holds the branch's five commits and nothing pre-merge. | grok Q4, gemini Q4 | `main..s2/degraded-line-0921` = 5 commits (`dc24d72`, `7b0a6a3`, `771b2b7`, `5db6d2d`, `88602cc` as printed in `rebased-diff.md`); `16:51` | HOLDS | no |
| 12 | A `seam test: added RED` or a non-zero failed count is refused before STEP-0; the real stop line satisfies the gate (`2222/0`, `added green`, `RESTARTS: com.cobalt.aset |`). | grok Q3(d), gemini Q3(d) | `16:13`; `rebase-report.md:140`; greps.txt search 11 | HOLDS | no |
| 13 | P10: production's tree carries no `id="degraded-line"` today (marker count 0). | grok Q6 | `grep -c -F "id=\"degraded-line\"" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` → 0; `16:25` | HOLDS | no |
| 14 | Round-1 rulings still stand: R19 names `16-degraded-line-deploy.md` and `FOLDED` (kept as its own AUTHORIZATION grep); the re-issue's own row `R__` is unfilled in the file. | grok Q6 | `cto-2026-09-21.md:30`; `16:11`; `grep -n -o "R__"` → line 11 ×4, line 16 ×1 | HOLDS; `R__` placeholders are by design filled by the desk before launch (`16:11`) | no — the desk's fill (see ESCALATE 1) |
| 15 | With the gemini answer: "no shell command" — the run finished with a printed answer, exit 0, no denial. | gemini | `b8q055ryk` output | HOLDS (no HARNESS) | no |

My own checks, whatever the houses said:

(i) Allow strings of the re-issued `16` launch line, each `grep -c -F -e '"<string>"' "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-19/02-deploy-stack-3.md"` (quotes included):
- Count **1** for all 27 non-branch strings: `git -C /Users/cobalt/cobalt add *` · `commit *` · `reset --soft HEAD~1` · `tag *` · `revert --no-edit *` · `revert --abort` · `git -C * status*` · `log*` · `diff*` · `rev-parse*` · `rev-list*` · `show*` · `COBALT_ENV=production uv run cobalt jobs *` · `… heartbeat show*` · `launchctl bootout gui/501/com.cobalt.aset` · `…radar` · `bootstrap … ops/com.cobalt.aset.plist` · `bootstrap … LaunchAgents/com.cobalt.radar.plist` · `kickstart -k …aset` · `…radar` · `launchctl print gui/501/*` · `curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/*` · `grep *` · `tail *` · `ls *` · `wc *` · `date*`.
- Count **0** (expected, the three BRANCH-NAMED strings, approved by his R12, `cto-2026-09-21.md:24`): `merge --ff-only s2/degraded-line-0921` · `cobalt-wt/degraded-line rebase main` · `cobalt-wt/degraded-line rebase --abort`.
- Denies `"AskUserQuestion"`, `"EnterWorktree"`, `"Bash(git push*)"` each `grep -c -F -e` against `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-21/11-panel-order-deploy.md` → **1**.

(ii) `word-diff.md` shows no change inside the launch line (line 1 of `16-old.md` = line 3 of the re-issue): the line holding `allowedTools` / `disallowedTools` is `word-diff.md:13`, and no `[-` / `{+` is printed on line 13 (row 3 above; the `[-` / `{+` on line 2 are my own header text).

UNVERIFIABLE FROM READS, carried: the live merge, the outage duration, the two `launchctl` cycles, the STEP-1 / 3.1 / 3.3 / P12 / P12b outputs at 20:02 (`git -C /Users/cobalt/cobalt diff --stat <cut> main -- . ':(exclude)docs'` etc. — run by `16` itself), whether the desk's `R__` fill and its own commits keep `main` still until the ff-merge.

## Folds proposed
None. No HOLDS finding needs a text change to `16`: the only claim that something can happen (row 1) is identical to the first issue's folded text and L43-compliant, and no launch blocker holds.

## ESCALATE
1. `16` still carries five `R__` placeholders (line 11 ×4, line 16 ×1); it is unrunnable until the desk fills the same number into each and commits that row (`16:11` refuses otherwise). A reading for the desk, not a defect of the prompt.
2. UNVERIFIABLE FROM READS, carried (see the closing paragraph of `## Checked against the files`): the 20:02 run's own gate outputs and the live merge.
3. Both `34`'s own ESCALATE lines (no browser ran; with-DB suite NOT RUN) ride along as READINGS, as `16` STEP-6 already instructs.

DEGRADED LINE DEPLOY REVIEW R2 DONE · grok: REVIEW: RUN IT · gemini: REVIEW: RUN IT · houses that read it: 2 of 2 · launch blockers that HOLD: 0 · folds proposed: 0 · ESCALATE: 3
