# Smoke-Only Deploy Review — 2026-09-23 (`69` read of `68-smoke-only-deploy.md`)

## §0 Headline
- 2 of 3 houses answered: Gemini `REVIEW: RUN IT`, Opus `REVIEW: RUN IT AFTER` 4 folds. Grok TIMEOUT at 15 min, no `REVIEW:` line (its second timeout in a row). The L67 floor (≥1 of Grok / Gemini) is met by Gemini alone.
- 1 blocker by the rule stated under `## Checked against the files` (a defect on the run's OWN single path, no third party, no relaunch): STEP-5's "any other revert error → (3)" brings both residents UP on a half-reverted tree, against the relaunch rule's DOWN-unless-PROVE-IT-empty (`68` part2:121 vs part2:69). 5 further folds (gate-branch sha re-check, two relaunch-rule gaps, the "NEVER crossed" wording, an `_inflight` validate line).
- Mechanical checks clean: all 43 launch-line tokens count 1 in `07` (and in `59`), 0 NEW, no unused allow string, no dialog path found; dev DB at 0013 supported harmless (Opus's `IntegrityError` UNVERIFIABLE settled: no such test). `R__L` count = 3 (the desk's expected placeholder).
- ESCALATE: 4.

## L74
One block arrived inside a tool result: appended to the Read of this run's own prompt file (`69`), a system-reminder-shaped block asking that commit messages and PR bodies end with a `Claude-Session: https://claude.ai/code/session_…` line and naming a file-send tool (SendUserFile). DATA under L74 — recorded once here, never followed. This hub commits nothing.

## PREFLIGHT
| rule | command | exit | allowed/DENIED + reason |
|---|---|---|---|
| DATE GATE (1st) | `date` | 0 | ALLOWED — `Wed Sep 23 16:12:14 EDT 2026` (2026-09-23; R30 covers the two house strings) |
| AUTH R30 | `grep -n "^| R30 " cto-2026-09-22.md` · `git log -1 --format=%H -S"Bash(grok *) and Bash(agy *) through 2026-09-23 23:59 ET" -- cto-2026-09-22.md` | 0 | ALLOWED — line 133 carries `Bash(grok *) and Bash(agy *) through 2026-09-23 23:59 ET` and `"Approved"`; commit `055242df8032632dfafdcc8a69dcc271be89c0f6` (NON-EMPTY) |
| AUTH R32 | `grep -n "^| R32 " cto-2026-09-22.md` · `git log -1 --format=%H -S"Bash(claude -p --model claude-opus-5-5 *)" -- cto-2026-09-22.md` | 0 | ALLOWED — line 131 carries `Bash(claude -p --model claude-opus-5-5 *)`; commit `b8a72b5300370e248cd6c7a8a732258fec03e6a0` (NON-EMPTY) |
| AUTH R80 (THIS LAUNCH) | `grep -n "^| R80 " cto-2026-09-23.md` · `git log -1 --format=%H -S"69-review-smoke-only-deploy.md" -- cto-2026-09-23.md` | 0 | ALLOWED — line 83 names `69-review-smoke-only-deploy.md` (token filled); commit `41eeef39ac939449ddc5c1c092f094c27256cefa` (NON-EMPTY) |
| `grok --version` | `grok --version` | 0 | ALLOWED — `grok 1.0.25 (f7e67d6988e2) [stable]` |
| `agy --version` | `agy --version` | 0 | ALLOWED — `1.2.9` |
| OPUS PROBE | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` (background, task `bbi9snaz5`) | 0 | ALLOWED — `OK` = UP |
| 68 exists | `ls -la ".../2026-09-23/68-smoke-only-deploy.md"` | 0 | ALLOWED — 62735 B, Sep 23 16:08 |
| 68 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- ".../68-smoke-only-deploy.md"` | 0 | ALLOWED — `<prompt sha>` = `41eeef39ac939449ddc5c1c092f094c27256cefa`; `git diff --stat HEAD` on it printed nothing |
| STAGGER 62 | `grep -n -F "62 is not running" cto-2026-09-23.md` | 0 | ALLOWED — R80 (line 83) names `69-review-smoke-only-deploy.md`: `62: not running (launch row)` ("62 is not running (stopped by the desk)") |
| STAGGER 65 | `grep -n -F "65 is not running" cto-2026-09-23.md` | 0 | ALLOWED — R80: `65: not running (launch row)` ("never launched — the setups branch left tonight's set, R78") |
| STAGGER 19 | `grep -n -F "19 is PAUSED" cto-2026-09-23.md` | 0 | ALLOWED — R80: `19: PAUSED (launch row)` ("PAUSED by the desk (PAUSE file)") |
| RECOVERY | `ls scratch/tribunal-bars-0920/smoke-only-deploy-0923` | 1 | fresh run — "No such file or directory" |
| DATE GATE (2nd) | `date` | 0 | ALLOWED — `Wed Sep 23 16:31:41 EDT 2026` (2026-09-23) |

## Packet
Staged in `scratch/tribunal-bars-0920/smoke-only-deploy-0923/`. Read → Write, then each copy checked with `wc -c` against its source and with `grep -v -x -F -f <source> <copy>` (every non-blank copy line is a line of the source). Trailing-whitespace lines: 0 in every Read→Write copy and in every packet file except `greps.txt` (14), `greps-2.txt` (6), `greps-3.txt` (7) — those are the generator's own `counts (grep -c): …` lines.
- `68-smoke-only-deploy.part1.md` 35,851 B (lines 1–160) + `part2.md` 26,884 B (161–300) = 62,735 B = source `68-smoke-only-deploy.md` (62,735 B).
- `59-base.part1.md` 25,166 + `part2.md` 26,725 + `part3.md` 26,671 = 78,562 B = source `59-stacked-deploy-r3.md` (78,562 B); split at lines 100 and 220.
- `59-outcome.md` 25,379 B = source `deploy-2026-09-23-r3.md` (25,379 B).
- `branches.md` 3,144 B · `stop-lines.md` 5,057 B (all five files; the drafter's `## THE DEV-DB DECISION` in full) · `rulings.md` 9,182 B (R5, R52, R53, R72, R75, R78 of 09-23; R30, R32 of 09-22) · `laws.md` 11,828 B (L42, L43, L54, L62, L63, L66, L68) · `devdb.md` 16,268 B · `restarts.md` 4,494 B · `clock.md` 3,706 B · `QUESTIONS.md` 6,937 B (the prompt's text verbatim + the "Files in this folder:" paragraph).
- `greps.txt` 33,022 B (searches 1–7) · `greps-2.txt` 29,000 B (8–11) · `greps-3.txt` 19,873 B (12–16). Split to keep each under 38,000 B; generated by shell redirection from the real `grep` outputs, not retyped. LONG-LINE RULE applied and said so inside the files: part1 lines 1, 6, 8 (each >1,250 B) are named, not reprinted; search 13 (`FAILED`, 70 hits) gives `grep -c` only.
- Helper commands the hub used outside the launch list, all read-only or scratch-folder-only (the classifier allowed each, no dialog): `sed -n`, `awk`, `cut`, `tr`, `printf … >` into the packet folder, `git rev-parse` / `status` / `diff --stat` / `grep`, `rm` of the hub's own temp files. Nothing under `/Users/cobalt/cobalt` except this report file was written.
- Every house got the identical packet (L44).

Houses (one attempt each, `run_in_background`, launched 16:31:4x–16:32:00 ET after the second date gate 16:31:41):
- GEMINI (`agy --model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 20m --add-dir … --print="…"`): DONE 16:36:52 (≈5 min), exit 0, closing `REVIEW: RUN IT`; written to `gemini-review.md` byte for byte.
- OPUS (`claude -p --model claude-opus-5-5 "…" --permission-mode plan --add-dir … --allowedTools "Read" "Grep" "Glob" --disallowedTools …`): DONE 16:37:55 (≈6 min), exit 0, closing `REVIEW: RUN IT AFTER …` (4 folds); written to `opus-review.md` byte for byte.
- GROK (`grok -p "…" --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)"`): TIMEOUT. 16:31:4x–16:47:07 ET (past 15 min), stopped with TaskStop on task `bzse21a47`. No `REVIEW:` line = `NO REVIEW LINE`; no `grok-review.md` written. Its whole output, kept verbatim: "I'll start with `QUESTIONS.md` and follow it exactly, then open `greps.txt`.`QUESTIONS.md` is the only round: a desk review of `68` from this folder alone. Next I'll open `greps.txt`, then the rest of the packet in the order it names.The greps name three long lines that were not reprinted. I'll read `68` in full, then the laws, rulings, and the files each question cites.The launch line and the laws are in. Next I'll compare `59`'s allow strings and relaunch rule, and check the branch, clock, and dev-database evidence the questions name."
- The previous read of `07` (`stacked-deploy-review-2026-09-23.md`) recorded the same Grok outcome: TIMEOUT at 15 min, no `REVIEW:` line. Recorded, not retried.
- **L67 floor: MET** — Gemini (a non-author house) answered in full with a `REVIEW:` line.

## CONTINUE
next: none — the desk commits this report (P9 of `68` requires it COMMITTED), folds and re-issues `68` if it takes any row below (L19), writes `R__L`, re-cuts the gate, launches `68` before 19:55 ET.

## Per question
Cells are the house's own words (≤30), cited as the house cited them. Gemini cited no `file:line` (its answer names steps only).
| Q | grok | gemini | opus |
|---|---|---|---|
| Q1 Allowlist | TIMEOUT | "Yes, EVERY command … covered exactly"; every string matches `59`'s byte for byte (0 NEW); "NO — every allow string is used" (step-named: `merge --abort`, `rebase --abort`, `reset --soft`) | NO defect. 40 strings at `part1.md:6`, each in `59-base.part1.md:6`; none unused; UNVERIFIABLE: whether the `ls -la …/cobalt-wt/*/.env` glob asks (`part1.md:138`) |
| Q2 L68 gate / single-branch | TIMEOUT | Yes: suites on `<ship>` before merge; `.env` gone in 2.3 (e) on all paths; `main` = gate base at 3.1; L54 lawful. "NO — … No untested code can land." | YES, narrow: 4.3 merges the NAME `deploy/stacked-0923`; no step re-reads its sha after 1.3 (`part2.md:83-84`). Fix: `rev-parse deploy/stacked-0923` = `<ship>` at 3.1 and 4.3. Rest holds |
| Q3 Window | TIMEOUT | Both down (4.2) / up (4.6); "Yes, STEP-5 (0)" lets the rollback cross 21:10 / 21:40 (quotes `part2` STEP-5 (0)) | Both down/up (`part2.md:79-91`); `<t up>` can pass 20:00 (merge clock 19:57:59) despite "NEVER crossed" (`part1.md:37`) — inside the pause, no harm; 20:30/21:10/21:40 only via STEP-5 (`part2.md:114`) |
| Q4 Rollback | TIMEOUT | Revert editor-free, proven before residents up; "RELAUNCH RULE handles partial reverts, merged-but-not-restarted states, and a moved main flawlessly"; "NO — no failure branch leaves a resident's state unknown" | Two branches fail: in-run "any other revert error → (3)" brings residents up on a half-revert (`part2.md:121` vs `:69`); relaunch (ii) after a finished/committed run reverts or bootouts (`:69`); (v) skips `.env` (`:72`) |
| Q5 Dev DB 0013 | TIMEOUT | HARMLESS supported by `devdb.md`; red suite stops safely, names the `58` string, never runs it; "NO — no test asserts `tunables.slug`'s nullability" | NO defect (`devdb.md:25, 76-89, 239-246`; `part1.md:136`; `rulings.md:13`). UNVERIFIABLE: a test expecting `IntegrityError` on a NULL slug |
| Q6 Dialog / question | TIMEOUT | "NO — all commands exactly match the non-interactive allowlist"; `--no-edit` / `--ff-only`; no waits | NO, apart from the Q1 glob: rebase non-interactive, merge/revert `--no-edit`, lightweight tags, no waits (`part1.md:94`), `ASK DESK` = record and continue (`part1.md:105`) |
| Q7 Other | TIMEOUT | "NO — the run is perfectly safe as written"; the drops from `59` are all setups-only | (1) a NEW `docs/_inflight/*.md` mid-run → validate RED → STEP-5 (`part2.md:86,107`); (2) preflight-only `.env` lane vs the parallel setups round (`part1.md:138`, `rulings.md:19`) → false red; drops harmless (`part2.md:38`) |
| REVIEW | TIMEOUT / NO REVIEW LINE | `REVIEW: RUN IT` | `REVIEW: RUN IT AFTER 4.3: rev-parse deploy/stacked-0923 equals <ship> before ff · STEP-5 other error: residents up only if PROVE IT empty · relaunch (ii): any committed stop line ends run · relaunch: ls/rm gate .env before any ending` |

## Checked against the files
Blocker rule (mine, applied to every row; it is a mechanical test, not a verdict on `68`): `blocks the launch? yes` = the text as written fails a good deploy, passes a bad one or leaves a resident/tree wrong on the run's OWN single path (no third-party action, no relaunch); `no` = it needs a third party (desk / another hub), a relaunch, or is wording only.

Files opened: `68` (the staged parts, and the source), `59`, `deploy-2026-09-23-r3.md`, LAWS.md, `cto-2026-09-23.md`, `cto-2026-09-22.md`, `58-devdb-rollback-0017.md` and its report, main's `src/` and `tests/` by path, and the branch by `git -C /Users/cobalt/cobalt show|grep s2/smoke-fix-0922`.

| claim | who | file:line | verdict | blocks? | ≤30 words |
|---|---|---|---|---|---|
| 4.3 merges the branch NAME; no step re-reads `deploy/stacked-0923`'s sha after 1.3, so a moved name lands an untested tree | opus | `68` part2:21 (1.3, reads the worktree HEAD), :64, :83–84; every other mention of the name is a relaunch rule or the launch line (greps: `deploy/stacked-0923` at part2:67,68,72,84) | HOLDS (textual) | no — needs the desk or a hub to move the gate branch mid-run; part1:4, :23 say the hub never re-cuts and the desk holds its commits | Text confirmed; no re-read exists. Trigger is a third-party move. |
| `main` moving between 3.1 and 4.3 is caught only after the bootout; 4.6 restores | opus | part2:64, :83 | HOLDS | no — ends both UP (`Anything else → 4.6 at once`), a needless outage | P12, 3.1, 4.3 all check `main`; `--ff-only` refuses too. |
| In-run: "any other revert error → (3)" brings residents up on a partially reverted tree; the relaunch rule keeps them DOWN unless PROVE IT is empty | opus | part2:121 (label `partial revert — the desk decides`, then (3)) vs part2:69 (`ONLY IF (2)'s PROVE IT diff would be empty, else left DOWN`) | HOLDS (textual contradiction) | **yes** — the run's own STEP-5 path after a red smoke; (3) bootstraps without the PROVE IT diff that (2) requires for the empty case | The two rules disagree; only the relaunch path is guarded. |
| Relaunch (ii) after a finished (DONE) or committed-FAILED run treats it as "a revert was interrupted" and goes to STEP-5 (1) | opus | part2:69 ("if it is a `FAILED:` line carrying `rollback: used` … Otherwise a revert was interrupted"); part2:68 (i) needs main = `<ship>`, but STEP-7's report commit puts main one above | HOLDS (textual) | no — needs a relaunch after the run ended | A `DONE` line or a `rollback: not used` `FAILED` falls into "Otherwise". |
| Relaunch (v) ends with no `.env` check in the gate worktree | opus | part2:72; the general rules at part1:53, :101 say clean it up first but the relaunch rule's first calls (part2:67) do not list `ls .env` | HOLDS (textual) | no — needs a relaunch after a death inside 2.3 | Generic rule exists; the relaunch path never looks. |
| `<t up>` can pass 20:00 despite "NEVER crossed" | opus | part1:36–37 (merge clock 19:58), part2:83–91 (validate, bootstraps, one retry, one kickstart follow the merge) | HOLDS | no — 20:00–21:00 is L66's own restart window (laws.md, L66 lines 361–363); R5 sets the radar clause aside (rulings.md, R5 row) | Wording, not harm. |
| STEP-5 may run "at any hour today", so 21:10 / 21:40 / 20:30 can be crossed | gemini, opus | part2:114 | HOLDS | no — stated behaviour; ESCALATE carries it | clock.md: archiver 20:30, replay 21:10 (Mon–Fri), backup 21:40. |
| RELAUNCH RULE handles partial reverts, merged-but-not-restarted and moved-main states "flawlessly" | gemini | part2:67–73 | DOES NOT HOLD as stated | no — see rows 4–5 and the in-run row | Opus's three gaps are in the text of (ii) and (v). |
| Every allow string of `68` is a string of `59`'s / `07`'s line; 0 NEW | gemini, opus | `68` part1:6 vs `59-base.part1.md:6`; `07-stacked-deploy.md` | HOLDS | no | My `grep -c -F -e` counts below: 43 tokens, each 1 in `07`; 41 Bash tokens and both dialog denies each 1 in `59`; `07` has 55 Bash tokens on its line. |
| No allow string is unused; every step's command matches a string | gemini, opus | `68` steps vs part1:6 | HOLDS | no | I read each of the 40 against its step (P2/P3, 1.1–1.3, 2.x, 3.2, 4.x, 4.7, STEP-5, STEP-7). |
| The `ls -la /Users/cobalt/cobalt-wt/*/.env` glob might ask (UNVERIFIABLE) | opus | `devdb-rollback-0017-2026-09-23.md:18–20`: the same command ran and printed `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` | SETTLED — no dialog | no | Opus's own settle-command, run by me. |
| `\?` in the phone curl matches `…5010/*` | gemini | `68` part2:104 area; `05-stacked-deploy.md` and `deploy-2026-09-22.md` each carry `radar\?frame=phone` (`grep -c -F` = 1, 1) | HOLDS | no | Precedent ran green on 09-22. |
| No test or code on the landing tree reads `tunables.slug`'s nullability | gemini, opus | `devdb.md` §6–7 (3 `.py` hits: `test_vault_restore.py:553,557`, `test_radar_score_migration.py:390`, `test_tenancy.py:268`, all other columns); `store.py:127,136,185`; main's `LoadedTunable.slug: str` (`vault_loader.py:133,147,155`) | HOLDS | no | Writes a non-NULL slug. |
| A test may expect `IntegrityError` on a NULL slug (UNVERIFIABLE) | opus | Opus's command `grep -rn "IntegrityError\|slug=None\|\"slug\": None" /Users/cobalt/cobalt/tests` → no output (exit 1); on the branch `git grep` for `IntegrityError\|slug=None` in `tests` → 0 | SETTLED — none | no | Settles it for main and the branch. |
| 68's `@requires_vault` claim: none of the 10 paths carries the marker; `test_replay_line.py:256` reads `COBALT_TEST_LIVE_DRC` and reaches `.models` | (my own check of a `68` claim) | `git show s2/smoke-fix-0922:<path> \| grep -c` = 0 for all 10 paths; `test_replay_line.py:256` `@requires_vault`, `:41` env `COBALT_TEST_LIVE_DRC`, `:260` `os.environ[…]`; `line.py:49` `from .models import …` | HOLDS | no | Stays UNPROVEN (L70) as `68` says. |
| A NEW `docs/_inflight/*.md` created mid-run makes 4.5 / 4.7 (f) RED and STEP-5 rolls back a good deploy | opus | part2:86, :107 ("exit 1 on EXACTLY `<val0>`'s `docs/_inflight/` lines"); `docs/_inflight/` now holds 5 files + `README.md`, newest `Sep 22 15:51` (none created today) | HOLDS (textual, no evidence it happens) | no — needs another session to write there during the run | Plausibility unproven. |
| The parallel setups fix round could hold `cobalt_dev` / `.env` during 2.3 (c) → false red | opus | `rulings.md:19` (R78: "runs in parallel"); the lane check is preflight only (part1:138) | HOLDS as a possibility; whether it uses `cobalt_dev` is UNVERIFIABLE FROM READS — `ls -la /Users/cobalt/cobalt-wt/*/.env` at launch | no — a false red is a safe stop | Desk-side hold, see ESCALATE. |
| L54: rebase-then-ff through the name `deploy/stacked-0923` is lawful for one branch | gemini, opus | laws.md:18 (L54: "Rebase-then-ff on every single-branch merge. A gate branch that combines sibling branches (L68) is the one exception"); `68` part2:19–20: `Fast-forward` expected, `Merge made by …` → FAILED | HOLDS | no | No merge commit is made anywhere. |
| `.env` is removed on every 2.3 path before any stop line or commit | gemini, opus | part2:35, :37, :39, :40 (each red routes to (e) FIRST); commits only at P3 (before the copy) and STEP-7 | HOLDS (single run) | no | The relaunch gap is the (v) row. |
| Derived restarts match the prediction `com.cobalt.aset com.cobalt.radar` | gemini, opus | `stop-lines.md` build line `RESTARTS: com.cobalt.aset com.cobalt.radar`; `restarts.md` (aset imports `cobalt.aset.*`, radar `cobalt.cli`); `68` part2:52–54 takes both down whatever the table says | UNVERIFIABLE FROM READS for the derived table itself — `COBALT_ENV=production uv run cobalt jobs restarts <main-at-gate>..<ship>` (`68` 2.5, run in the gate tree) | no | Both residents go down regardless. |
| No path to a mid-run question or dialog | gemini, opus | `68` part1:94, :105; `--no-edit` at part2:19, :118; tags carry no `-m` | HOLDS | no | The `ls` glob is settled above. |

(i) Allow-string counts, `grep -c -F -e "<string>"` (quotes included) against `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-23/07-stacked-deploy.md` — every string counts ≥1 (all 1); NONE counts 0, so no blocker from this check:
```
1  "Bash(git -C /Users/cobalt/cobalt add *)"
1  "Bash(git -C /Users/cobalt/cobalt commit *)"
1  "Bash(git -C /Users/cobalt/cobalt reset --soft HEAD~1)"
1  "Bash(git -C /Users/cobalt/cobalt tag *)"
1  "Bash(git -C /Users/cobalt/cobalt merge --ff-only deploy/stacked-0923)"
1  "Bash(git -C /Users/cobalt/cobalt revert --no-edit *)"
1  "Bash(git -C /Users/cobalt/cobalt revert --abort)"
1  "Bash(git -C /Users/cobalt/cobalt-wt/s2-smoke-fix rebase main)"
1  "Bash(git -C /Users/cobalt/cobalt-wt/s2-smoke-fix rebase --abort)"
1  "Bash(git -C /Users/cobalt/cobalt-wt/stacked-0923 merge --no-edit s2/smoke-fix-0922)"
1  "Bash(git -C /Users/cobalt/cobalt-wt/stacked-0923 merge --abort)"
1  "Bash(git -C * status*)"
1  "Bash(git -C * log*)"
1  "Bash(git -C * diff*)"
1  "Bash(git -C * rev-parse*)"
1  "Bash(git -C * rev-list*)"
1  "Bash(git -C * merge-base*)"
1  "Bash(git -C * show*)"
1  "Bash(cd *)"
1  "Bash(uv run pytest *)"
1  "Bash(COBALT_ENV=dev uv run pytest *)"
1  "Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/stacked-0923/.env)"
1  "Bash(rm /Users/cobalt/cobalt-wt/stacked-0923/.env)"
1  "Bash(COBALT_ENV=dev uv run cobalt db migrate --proof-only)"
1  "Bash(COBALT_ENV=production uv run cobalt validate)"
1  "Bash(COBALT_ENV=production uv run cobalt jobs restarts *)"
1  "Bash(COBALT_ENV=production uv run cobalt heartbeat show*)"
1  "Bash(COBALT_ENV=production uv run cobalt db query *)"
1  "Bash(launchctl bootout gui/501/com.cobalt.aset)"
1  "Bash(launchctl bootout gui/501/com.cobalt.radar)"
1  "Bash(launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist)"
1  "Bash(launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist)"
1  "Bash(launchctl kickstart -k gui/501/com.cobalt.aset)"
1  "Bash(launchctl kickstart -k gui/501/com.cobalt.radar)"
1  "Bash(launchctl print gui/501/*)"
1  "Bash(curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/*)"
1  "Bash(grep *)"
1  "Bash(tail *)"
1  "Bash(ls *)"
1  "Bash(date*)"
1  "Bash(git push*)"      (deny)
1  "AskUserQuestion"      (deny)
1  "EnterWorktree"        (deny)
```
The same 41 Bash tokens and both dialog denies each count 1 in `59-stacked-deploy-r3.md`. `07`'s line 6 carries 55 Bash tokens (54 allows + the push deny); `68` carries 41 (40 + the push deny): 14 dropped, 0 new, as `68` says.

(ii) `grep -c -E "R_[_]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-23/68-smoke-only-deploy.md"` → **3** (lines 48, 50, 140: the desk's `R__L`). Expected before the desk fills them; not a blocker.

Where the houses contradict: Q4. Gemini: "the RELAUNCH RULE handles partial reverts, merged-but-not-restarted states, and a moved main flawlessly" and "NO — no failure branch leaves a resident's state unknown or unhandled". Opus: "Two branches fail" — the in-run partial-revert branch brings residents up on a half-reverted tree, and relaunch rule (ii) after a finished run "STEP-5 bootouts and reverts a **good** deploy". The text supports Opus (rows 3–5 above). Q2: Gemini "NO — … No untested code can land"; Opus "YES, code the suites did not run on can land (narrow)" — the text shows no sha re-read after 1.3 (row 1); the trigger is a third-party move. Q7: Gemini "NO — the run is perfectly safe as written"; Opus lists two Q7 possibilities (rows `_inflight` and setups round).

## Folds proposed
Each HOLDS row as one text change to `68`, for the desk to fold (I edit nothing). Numbering follows the checked rows.
1. STEP-3.1 and STEP-4.3: `main must EQUAL <main-at-gate> …` / `HEAD must = <pre-merge>` → add, in both: `and `git -C /Users/cobalt/cobalt rev-parse --short deploy/stacked-0923` must EQUAL `<ship>`, else `FAILED: <step> — gate branch moved · rollback: not used` (4.3: 4.6 first)` (Opus; `rev-parse*` is already allowed).
2. STEP-5 (2), the "Any other revert error" bullet (part2:121): `→ log --oneline -8 quoted → (3), labelled safe state: <NEW code kept | partial revert — the desk decides> — revert failed: <error>` → `→ log --oneline -8 quoted → run (2)'s PROVE IT diff; empty → (3); non-empty → do NOT bring the residents up, end FAILED: STEP-5 (2) — partial revert — <paths> · rollback: used — aset: DOWN — radar: DOWN` (Opus; this is the blocker row).
3. RELAUNCH RULE (ii): `Otherwise a revert was interrupted: go to STEP-5 (1) at once` → `If it is any other committed stop line (SMOKE ONLY DEPLOY DONE, or FAILED with rollback: not used), end FAILED: relaunch — the run already ended; the desk decides · rollback: <as that line>. Only when the report has no stop line above # SECOND RUN was a revert interrupted: go to STEP-5 (1) at once` (Opus).
4. RELAUNCH RULE (v) (and (ii)'s "never recorded" clause): `End FAILED: relaunch — partial gate on disk …` → `FIRST `ls -la /Users/cobalt/cobalt-wt/stacked-0923/.env`; if listed, `rm` it and `ls -la` again (STEP-2.3 (e)); then end FAILED: relaunch — partial gate on disk …` (Opus).
5. part1:37 wording: `are NEVER crossed by a residents-down window` → `the 20:30 archiver, the 21:10 replay and the 21:40 backup are never crossed by the run's own window (STEP-5 excepted, part2:114); a window opened before 19:58 may close after 20:00, inside the 20:00–21:00 pause` (Opus).
6. STEP-4.5 and 4.7 (f): `exit 1 on EXACTLY <val0>'s docs/_inflight/ lines, or exit 0` → `exit 0, or exit 1 with ONLY lines of the form docs/_inflight/…: docs/_inflight/ may hold only README.md (a new such file is named in ## Smoke, not RED)` (Opus, Q7).
Desk-side (not a text change, so not counted): hold the setups fix round's with-DB work and any `.env` copy until `68` stops, and write that on the `R__L` row (Opus ESCALATE 3; `rulings.md:19`).

## ESCALATE
- ASK DESK: blockers = 1 (fold row 2, in-run partial revert). `68` P9 (part1:140) passes on `blockers: 0` OR when the `R__L` row names every blocker that held as folded into `68` — fold row 2 (a re-issue, L19) or name it on `R__L`. Safe default: fold it. [2026-09-23 16:5x ET]
- ASK DESK: rows 1, 3, 4, 5 and 6 are non-blocking under my rule (each needs a third party, a relaunch, or is wording). Safe default: fold 1 and 4 with row 2 (each is one allowed command); 3, 5 and 6 are optional. [2026-09-23 16:5x ET]
- ASK DESK: Grok TIMEOUT twice today on a deploy-prompt read (this one and `08`). The floor was met by Gemini; a third seat did not answer. Safe default: none needed for `68`; the desk may want Grok's meter/run shape checked before `62`'s relaunch. [2026-09-23 16:5x ET]
- The hub's own notes: this report is untracked at `/Users/cobalt/cobalt` until the desk commits it (P1 of `68` accepts a `??` report, P9 requires it committed); main's tip moved from `d104044e` (16:2x) to `2028ef79` (16:3x) while the hub read — the desk's own commits, docs only (`git -C /Users/cobalt/cobalt log --stat --oneline 797fdd2f..main -- . ':(exclude)docs'` printed nothing at 16:2x; not re-run after). The desk re-cuts the gate AFTER its last commit (`68` bare command (1)).

SMOKE ONLY DEPLOY REVIEW DONE · houses: 2 of 3 · other houses: 1 of 2 · blockers: 1 · folds: 6
