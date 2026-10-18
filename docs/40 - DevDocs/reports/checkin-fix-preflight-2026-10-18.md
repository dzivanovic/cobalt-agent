# Preflight — card 751 `checkin-install-1018`, row F1 (fix round) — 2026-10-18

Read-only. Branch tip proved against `git show ops/checkin-install-1018:<file>`; line numbers read with `grep -n` / Read on the worktree `cobalt-wt/checkin-install-1018`, whose `.git/worktrees/.../HEAD` is `ref: refs/heads/ops/checkin-install-1018` and whose content matched the `git show` text read first.

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt rev-parse ops/checkin-install-1018` | `3108359fc80e6b61acf9575b5118b49759283faa` = the row's `3108359f` | OK |
| 2 | `git show <tip>:ops/desk/checkin-timer.sh`; `grep -n` on the worktree | step 4 comment `:111`, `ping_id=""` `:112`, loop `:113-123`, `break` `:120`, `if` / DEFERRED / `finish 0` `:124-127`, step 5 comment `:129`. Row's `:111-127`, `:113-123`, `:120`, `:124-127` all hold | OK |
| 3 | `grep -n` `#   4. a live row` in `checkin-timer.sh` | header step 4 is at `:24`, not `:23` (the row says "The header text of step 4 (`:23`)") | FAIL |
| 4 | `grep -n -E "^REPO=\|^WT=\|^DESK_LIST=\|^LAUNCH=\|^PING="` | `REPO` `:45`, `WT` `:46`, `DESK_LIST` `:47`, `LAUNCH` `:48`, `PING` `:49`. The row says `:44-48` (and "the three at `:46`"); the three overridables are `:45-47` | FAIL |
| 5 | `git show <tip>:ops/desk/desk-done.sh`; `grep -n` | `:3` usage line `desk-done.sh <session id> --replaced [<tab>]`; `:16-17` the `--replaced` text; refuses `brain*` and `cto-desk` only (`checkin-ping` closes); last stdout line `CLOSED <id>` or `KEPT <id>: …` | OK |
| 6 | `grep -n startedAt ops/cto-desk.sh` | `:189` fields `cwd, id, kind, name, sessionId, startedAt, state`; `:226-229` the `_age_key` comment "epoch MILLISECONDS (1789728845765) in CLI 2.1.276" and `str(started).isdigit()` | OK |
| 7 | Read `desk-launch.sh` at `:2380-2397`, `:745-750` | `:749` `run_launch` of kind `prompt`, no replacement; `:2385` busy test `!($2 == "idle" && $3 != "working")`; `:2388` `desk-done.sh "$rid" --replaced`; `:2393-2395` `KEPT*` or non-zero rc → `refuse` | OK |
| 8 | `grep -n "^def test_\|^@pytest"` on the test file | `test_t1_a_live_ping_defers` `:183` (ends `:190`, `:191` blank); O1 mark `:193`, def `:194` (ends `:202`); A1 mark `:205`, def `:206` (ends `:227`). Row's `:183-191`, `:193-203`, `:205-227` hold, each including the trailing blank | OK |
| 9 | the row's age rule, read whole | judged by `startedAt` epoch ms (`now − startedAt > 30 min`), never by `state`; cites R117 for why | OK |
| 10 | the row's step (4) | every `checkin-ping` row older than 30 min is closed whatever its state (no `break`); a younger row defers `DEFERRED: ping live — <id>` naming that row, even when a stale one was closed; failed close / `KEPT` → `REFUSED: close of stale ping <id> failed` (one notify, exit 1, no launch) | OK |
| 11 | RED on the tip | `checkin-timer.sh:112-127` never reads `state` and defers on the first `checkin-ping` row, so `idle · working` + `startedAt` six hours back prints `DEFERRED` and makes no call: red at `DEFERRED` not in stdout, named in the row | OK |
| 12 | controls | `test_f1_a_five_minute_old_ping_still_defers` (id in stdout, no calls, no notify) and `test_f1_no_ping_row_launches_directly` (`[prompt <PING>]`, no `done`) both hold on the tip (defer on any row; launch on none), so green before and after. `test_t1_a_live_ping_defers` gets a `startedAt` five minutes back | OK |
| 13 | the two strict xfails | O1 `test_x3_a_finished_ping_row_does_not_defer_the_next_fire` SETTLED, mark removed; A1 `test_x3_a_finished_ping_is_not_left_as_a_named_session` same name, body restated at the timer (`<id> --replaced` before `prompt <PING>`, once each), mark removed. Both are settled, none carried. The ruling is cited as "L79 (a)", not an `R<n>` (see ISSUES 1) | OK |
| 14 | row's files vs the card | `ops/desk/checkin-timer.sh` and `tests/ops/test_checkin_install_1018.py` only, both in the card; no fixed file; `desk-launch.sh`, plist and ping prompt untouched; the two new env names (`COBALT_AGENTS_CMD`, `COBALT_DESK_DONE`) are test-only; no `--allowedTools` / `--add-dir` / launch-line string added (R411, R412 not re-read in this seat: the row adds no command to any launch line) | OK |
| 15 | `git -C /Users/cobalt/cobalt log -1 --format=%h -- <card>` and `git diff --stat HEAD -- <card>` | `4b685aeb`; diff empty | OK |
| 16 | what blocks the card's own deploy | see ISSUES 5 | OK |

## ISSUES
1. NOTE — O1/A1 are SETTLED "by L79 (a)". The brain's ruling now has its own row, `reports/cto-2026-10-18.md:16` **R1895** (brain L79 on 751 D1, option (a)); the drafter's decision 1 asked for it. Default: cite `R1895` in the two xfail-removal commit lines and the build report; the row text can stay.
2. FAIL (cite, cosmetic) — header step 4 is `checkin-timer.sh:24`, not `:23`. The builder re-reads by content (BUILD-HUB E3), so the edit lands right.
3. FAIL (cite, cosmetic) — the three overridables are `checkin-timer.sh:45-47` (`REPO`..`PING` `:45-49`), not `:44-48` / `:46`.
4. NOTE — the row says "reads `claude agents --json` once" with no temp file. `ops/cto-desk.sh:119-122` records that CLI 2.1.276 writes NOTHING into a pipe, and the registry goes "through a temp file, always". (`desk-done.sh` itself pipes it, so it may differ there.) If the timer pipes it, every ping has UNKNOWN age and is closed, never deferred: the 5-minute control passes in tests (the stub prints to a pipe fine) but a young ping is closed in real use. Harmless (a ping is one turn), and no permanent defer, but the builder should write to a file like `cto-desk.sh`. The desk can add "to a temp file" to the row.
5. NOTE — two young `checkin-ping` rows: the row says "that row's id" and does not say which. Pick the first young row in list order and pin it in the test. Not a blocker.
6. NOTE — deploy blockers for the card, not for this row: (a) the fix round, then step `W` gates and the scoped check, none done yet; (b) D2 of the check: `SHADOW-INSTRUCTIONS.md` is untracked and UNCLASSIFIED in `cobalt jobs restarts`, so `RESTARTS:` lists six residents until that file is gone, committed range is `none`; (c) `desk-launch.sh install-ops`, then his three install lines for the plist (until then CONTRACT:29's timeout stands); (d) `main` carries unrelated uncommitted edits (`.claude/settings.json`, several reports), not examined here.

PREFLIGHT DONE · card: checkin-install-1018 · checks: 16 · fails: 2 · ready: YES
