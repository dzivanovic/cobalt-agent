# Card 549 `desk-installs-1014` — preflight round 2 (2026-10-14, seat `desk-installs-preflight`)

Read on `git show HEAD:<file>` / `git grep … HEAD` (HEAD `af2fc379`; the card's `0ffb6949` anchors still hold, only docs commits since). Nothing run but reads.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff HEAD --stat -- <card>`; `git log --oneline -3 -- <card>` | diff empty; last commit `af2fc379` (= HEAD), before it `79e286cc` | OK |
| 2 | I1 test (2) re-check (round-1 FAIL) | now `set(non_bash) <= {"SendMessage"}`: `non_bash` is `[]` on BASE (12 `Bash(` strings only, `git grep` of `:13`), so `set() <= {"SendMessage"}` is true on BASE and after; test (1) alone carries the `SendMessage` count (0 on BASE = red). The other assertions (12 strings once each, `AskUserQuestion` and `EnterWorktree` in deny, `--permission-mode auto`, `--remote-control cto-desk --name cto-desk` once, no `COBALT_ENV`/`.env`/`cobalt_key`) all hold on BASE | OK |
| 3 | header vs `CARD.md` | JOB, LADDER, BRANCH, WORKTREE, REPORT, CHECK REPORT, HOUSE B, DB, RULINGS present; BASE and TIP empty (desk's); CLASS, INSTALL, RESTARTS as in 546, 550; no `«FILL`; `<BASE>` only inside commands | OK |
| 4 | `git grep` `CTO-DESK-WAKEUP.md` | the one `- LAUNCH` line is `:13`; `SendMessage` at `:12`, `:16`, none in `--allowedTools`; `merge-base*)" --disallowedTools` once; 12 allow, 7 deny (`AskUserQuestion`, `EnterWorktree`, 5 `Edit(`), two `--add-dir` | OK |
| 5 | `git grep` `STANDING-LIST.md` | `:159` heading `## 4.`; `:164` `git add`/`commit`, `:165` `git log`…, `:166` six `git -C`, `:167`, `:168`, `:169` deny rows; `:172` "NEW strings left … five deny strings, no allow"; `:14` "Section 4 … five deny strings **NEW**"; `SendMessage` only `:225`, `:229` (§8). Each I2 (2) prefix occurs once in §4 | OK |
| 6 | `test_desk_refresh_wakeup.py` | `import subprocess` `:10` (used only at the last test), `BASE = "f7d71571"` `:15`, the pin `:76-83`, five other tests; docstring `:1-6`, `:4-5` state the launch line "byte for byte the BASE line" | OK (NOTE 2) |
| 7 | `test_hub_lines.py` | `HUBS` `:29`, `hub_line` `:54`, `tools` `:60-70`, `launch_line` `:120`, desk flag pin `:151-155` (once, not a whole line) | OK |
| 8 | `desk-launch.sh` kind `desk` | per round 1, `:544-563`: checks `cto-desk` name, no `bypassPermissions`, `check_paths`; reads no non-Bash allow; not edited by the card | OK |
| 9 | `git grep -F 'merge-base*)" --disallowedTools' HEAD -- tests ops` | no hit; the only whole-line pin of the desk line is `test_desk_refresh_wakeup.py:76-83` (via `git show f7d71571:`), which I1 (3) repairs | OK |
| 10 | no whole-file pin, no whole-line-equals-commit pin, no BASE literal | new tests I1 (1), (2), I2 (1), (2) find lines by content; none runs `git show` or reads a BASE hash; the one BASE literal (`f7d71571`) is deleted by I1 (3); I2 (2) asserts line prefixes only | OK |
| 11 | each row's red names its failing reason on BASE | I1 (1): `count("SendMessage")` is 0, not 1; I1 (3): red after I1 (whole-line equality fails); I2 (1): §4 count 0, not 1; I1 (2) and I2 (2) are labelled GREEN on BASE and are | OK |
| 12 | strings added vs survey row 1 (`survey-blockers-2026-10-12.md:13`), R411, R412 | the card adds `"SendMessage"` only, byte for byte as the survey proposes; siblings stay ASK DESK | OK |
| 13 | K5 scope (`LAWS.md:405`) | one allow string, no Bash, reads no secret, widens no K3 seat | OK |
| 14 | RESTARTS class home (K10) | `docs/` → `DOCS` (`restarts.py:225-228`), `tests/` → "test/documentation; no resident" (`:245-246`); files are two docs files and two test files; `RESTARTS: none` | OK |
| 15 | overlap with 521, 523, 537, 546, 547, 548, 550 (`grep` of each card for `CTO-DESK-WAKEUP`, `STANDING-LIST`, the two test files) | 521, 523, 548, 550: no hit (550 edits `CARD.md` only); 537: `STANDING-LIST.md:109`, `:139-140`, `test_hub_lines.py` (not §4, not `:13`); 546: `DEPLOY-HUB.md:15`, `:129`; 547: text only, no edit of those files | OK |
| 16 | `grep -rl "OWN LINE" tests ops` | no reader of §4 by heading that a new row could break | OK |
| 17 | deploy blockers | see ISSUES 3 | NOTE |

## ISSUES

1. NOTE — round 1's one FAIL (I1 test (2) red on BASE) is fixed: the assertion is `set(non_bash) <= {"SendMessage"}`, green on BASE and after.
2. NOTE — the card says the `test_desk_refresh_wakeup.py` docstring is `:1-9`; it is `:1-6` (`:4-5` name the launch line). The card edits it by content; no change needed.
3. NOTE — what blocks this card's deploy: one deploy hub at a time, no desk commit on `main` while one runs. 537 deploys first (its build `91b68031`), then the 523 fix-round, 521 (needs 537's smoke string) and 546 queue on the same rule. 537 inserts a row in `STANDING-LIST.md` §3, shifting `:159-172` and `:14` on this build's BASE; the card finds the row by content and re-reads before the edit, so no change needed. No file conflict with any card.
4. NOTE — the running desk keeps its old launch line until its next REFRESH, so `SendMessage` is not proven by the deploy itself (the card's DEPLOY PROOF says so).

PREFLIGHT DONE · card: desk-installs-1014 · checks: 17 · fails: 0 · ready: YES
