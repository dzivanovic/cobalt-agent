# Card 549 `desk-installs-1014` — preflight (2026-10-14, seat `desk-installs-preflight`)

Read on `git show HEAD:<file>` (HEAD `6b5ceded`; the card's `0ffb6949` anchors still hold). Nothing run but reads.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git log --oneline -2 -- <card>`; `git diff HEAD --stat -- <card>` | commit `79e286cc`; diff empty | OK |
| 2 | header vs `CARD.md` | JOB, LADDER, BRANCH, WORKTREE, REPORT, CHECK REPORT, HOUSE B, DB, RULINGS present; BASE and TIP empty (desk's); CLASS, INSTALL, RESTARTS as in 537, 546, 550; no `«FILL`. `<BASE>` appears only inside commands (`:32`, `:34`, `:53`) | OK |
| 3 | `grep -n -E "^- LAUNCH\|SendMessage" HEAD:CTO-DESK-WAKEUP.md` | the one `- LAUNCH` line is `:13`; `SendMessage` at `:12`, `:16`, none in `--allowedTools`; OLD text `"Bash(git -C * merge-base*)" --disallowedTools "AskUserQuestion"` occurs once | OK |
| 4 | counts in `:13` | 12 allow strings, 7 deny strings, two `--add-dir`, `--permission-mode auto`, `--remote-control cto-desk --name cto-desk` | OK |
| 5 | `STANDING-LIST.md` anchors | `:159` heading; `:166` six `git -C` strings; `:167`, `:168`, `:169` deny rows; `:172` "NEW strings left … the five deny strings, no allow"; `:14` "Section 4 … five deny strings **NEW**"; `SendMessage` only at `:225`, `:229` (§8); `:229` is `\| \`SendMessage\` \| the seat's one reply channel`, so the DEPLOY PROOF grep `\| \`SendMessage\` \| **NEW**` is 0 before, 1 after | OK |
| 6 | `test_desk_refresh_wakeup.py` anchors | `import subprocess` `:10` and `subprocess.run` `:78` only; `BASE = "f7d71571"` `:15`; the pin is `:76-83`; 5 other tests; docstring `:1-6` (card says `:1-9`) and `:5` states "the `- LAUNCH` line byte for byte the BASE line" | OK (NOTE 2) |
| 7 | `test_hub_lines.py` anchors | `HUBS` `:29`; `hub_line` `:54`; `tools` `:60-70`; `launch_line` `:120`; desk-flag pin `:151-155` | OK |
| 8 | `desk-launch.sh` kind `desk` | `:544-563` as the card says; checks only `cto-desk` name, no `bypassPermissions`, `check_paths`; no non-Bash allow is read; `SendMessage` at `:866`, `:914` (ops-hand) | OK |
| 9 | `grep -rn -F 'merge-base*)" --disallowedTools' tests ops` | no output; the only whole-line pin of the desk line is `test_desk_refresh_wakeup.py:76-83` (via `git show f7d71571:`), which the card repairs | OK |
| 10 | no test pins a whole file, a whole fixed-file line equal to a commit, or a BASE literal | new tests I1(1), I1(2), I2(1), I2(2) find lines by content; none reads `git show` or a BASE hash; the one BASE literal (`f7d71571`) is deleted. Other readers of the line (`test_hub_lines.py:116,124,151-155`, `test_bare_guard.py:258,557,1156`, `test_stop_guard.py:302`) hold no whole line | OK |
| 11 | each row's red names its failing reason on BASE | I1(1): count 0 on BASE ✓. I2(1): §4 count 0 ✓. I1(3): repair, red after I1 ✓. **I1(2): labelled "GREEN on BASE", but its assertion `[non-Bash allow] == ["SendMessage"]` is `[]` on BASE, so it is RED on BASE** | **FAIL** (ISSUE 1) |
| 12 | allow strings the card adds vs survey row 1 (`survey-blockers-2026-10-12.md:13`) and R411, R412 | the card adds `"SendMessage"` only; survey row 1 proposes `"SendMessage"` byte for byte; siblings stay ASK DESK. L81 K5 (`LAWS.md:405`): no secret access, no K3 seat | OK |
| 13 | RESTARTS class home (K10) | `docs/` → `DOCS` (`restarts.py:225-228`), `tests/` → "test/documentation; no resident" (`:245-246`); the card's files are two docs files and two test files; `RESTARTS: none` | OK |
| 14 | overlap with 521, 523, 537, 546, 550 (547, 548 absent from `prompts/2026-10-14/`, `ls` 531-551) | 521: 0 hits on `CTO-DESK-WAKEUP`, `STANDING-LIST`, the two test files; 523: one mention of `CTO-DESK-WAKEUP.md` as text of a retired card, no edit; 537: `STANDING-LIST.md` §3 (`:109-157`) and `test_hub_lines.py`; 546: `DEPLOY-HUB.md:15`, `:129`; 550: 0 hits | OK (NOTE 3) |
| 15 | deploy blockers | see ISSUES | NOTE |

## ISSUES

1. FAIL — I1 test (2) `test_i1_no_other_string_of_the_desk_line_changes`: the card calls it "negative control, GREEN on `BASE` and after", but `[s for s in allow if not s.startswith("Bash(")] == ["SendMessage"]` is false on BASE (no non-Bash string there). A builder cannot make it both green on BASE and meet the card. Fix: `set(non_bash) <= {"SendMessage"}` (or `== []` for everything but `SendMessage`), leaving test (1) to carry the count of `SendMessage`.
2. NOTE — the card says the docstring is `:1-9`; it is `:1-6` (`:4-5` name the `- LAUNCH` line). The builder edits by content; no change needed.
3. NOTE — 537 deploys first and inserts rows in `STANDING-LIST.md` §3, so `:159-172` and `:14` shift by its added lines on the BASE this build starts from; the card finds the row by content ("after the six `git -C` strings") and tells the builder to re-read, so no change needed. `STANDING-LIST.md:172` and `:14` stay unedited (the drafter's ASK DESK default).
4. NOTE — what blocks this card's deploy: one deploy hub at a time and no desk commit on `main` while a deploy hub runs. 537's build `91b68031` runs and 537 deploys first; the 523 fix-round deploy, 521's deploy (it needs 537's smoke string) and 546 (deploy freeze) queue on the same rule. No file conflict with them. A merge-time overlap exists with none; 547 and 548 do not exist yet.
5. NOTE — the running desk keeps its old launch line until its next REFRESH, so `SendMessage` is not proven by the deploy itself (the card's DEPLOY PROOF says so).

PREFLIGHT DONE · card: desk-installs-1014 · checks: 15 · fails: 1 · ready: NO
