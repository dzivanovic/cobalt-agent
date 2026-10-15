# close-automation preflight — 2026-10-15 09:44 ET

Card `prompts/2026-10-15/580-close-automation-card.md`, read on `main` HEAD `924bc5b1`. Read-only; no test was run (every RED stays UNPROVEN until the builder quotes it).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt log --oneline -2 -- <card>` and `git diff HEAD --stat -- <card>` | `924bc5b1 docs(card): 580 …`; diff empty | OK |
| 2 | header vs `CARD.md` (build): JOB, LADDER, BRANCH, WORKTREE, BASE, TIP, REPORT, CHECK REPORT, HOUSE B, DB, RULINGS present; `grep -c "«"` of the card | all present; `0`; the only empty values are BASE and TIP (the desk's). `LADDER` has no `<date> R<n>` tail (NOTE 6) | OK |
| 3 | `RULINGS: 2026-10-15 R1536` vs `desk-launch.sh:295-322` (`ruling_row`), row at `cto-2026-10-15.md:22` | row reads `DESK RECORD, brain (L79) … RECORDED`, not `HIS RULING` + `APPROVED`: the build launch is REFUSED (`:317`) | FAIL |
| 4 | `desk-watch.sh` anchors (`:3`, `:15`, `:50-54`, `:64`, `:67-71`, `:79-83`, `:90`, `:94-95`) | all as quoted; `git diff HEAD --stat -- ops/desk tests/ops src/cobalt/jobs/restarts.py ops/cto-desk.sh` empty | OK |
| 5 | `desk-launch.sh` anchors (`:100-110`, `:266-285`, `:588`, `:921-947`, `:2291-2294`, `:2296`) | all as quoted; `install-ops` last line `:947`; block slot `:2294`→`:2296` exists; `COBALT_REPO_ROOT` read at `:217` | OK |
| 6 | `stop-guard.py` anchors (`:111`, `:125`, `:315-326`, `:340-370`, `:373-418`, `:391-398`) and `wait-stop-line.sh:43-45` | all as quoted | OK |
| 7 | `ops/cto-desk.sh:325-362` as the source of the pane JSON keys | the lines show `tab_id`, `pane_id`, `label`; `terminal_title_stripped` and `herdr tab close` are not there (NOTE 2) | OK |
| 8 | tests anchors: `test_desk_watch.py:26-75`, `test_stop_guard.py:313-369` and `:568`, `test_install_ops.py:29-62`, `test_desk_launch_prechecks.py` stub | as quoted | OK |
| 9 | `DEPLOY-HUB.md:135`, `reports/deploy-desk-refresh-1013.md:207`, `cto-desk-checklist.md:60`, `LAWS.md` L79 `:397`, L81 `:406`, `restarts.py:38`, `:225-228`, `:232`, `:246` | all as quoted; the DEPLOYED line is `DEPLOYED <TAG> <head8> \| set: …` | OK |
| 10 | each row's red names its failing reason on BASE | C1 `FileNotFoundError` (no `job-close.sh`), C2 one-line stdout, C3 exit 0 vs 2, C4 missing link: each named | OK |
| 11 | pins: whole file, whole fixed-file line, BASE or hash literal, `git show` | the card forbids all four; the fixtures are `aaaa0001`, `b43daef9`; the control reads `desk-list.sh` by content; no whole-line pin | OK |
| 12 | allow line: `git show HEAD:.claude/settings.json` for `Bash(sh /Users/cobalt/.claude/ops/*)`, `Bash(claude stop *)`, `Bash(claude rm *)`, `Bash(herdr *)` | all four at HEAD; the card adds no command and no string | OK |
| 13 | K10: every row's files vs `restarts.py` | `ops/desk/` → "operator script; no Cobalt reader", `tests/` → "test/documentation; no resident": `RESTARTS: none` holds | OK |
| 14 | overlap with 546 (`DEPLOY-HUB.md:15`, `:129`, `deploy-shipped.sh`), 549 (`CTO-DESK-WAKEUP.md:13`, `STANDING-LIST.md` §4, `test_desk_refresh_wakeup.py`), 550 (`CARD.md`, `test_card_template_1014.py`), 577 (`grep` of the three scripts) | no shared file or line range; 549 and 550 hold `desk-launch.sh` as "not changed" | OK |
| 15 | overlap with `2026-10-15/582-draft-k5-band-routing.md` (the band card's drafter prompt) | it names `desk-launch.sh:2233` (the `<model>` fill) and this card's `:2294-2296`, and asks the drafter to prove no overlap; the band card is not written: UNPROVEN (NOTE 7) | OK |
| 16 | what blocks the card's own build or deploy | the ruling row (check 3); BASE and TIP to fill; nothing else found (DB none, no lock, no allow string) | FAIL (check 3) |

## ISSUES

1. FAIL (blocks the build launch): `RULINGS: 2026-10-15 R1536` cites a `DESK RECORD … RECORDED` row. `ruling_row` (`desk-launch.sh:316-317`) refuses any row that is not `HIS RULING` + `APPROVED`, so `desk-launch.sh build` refuses the card. Fix: cite a row of his that covers the K5 class (siblings 546, 549 and 550 cite `2026-10-14 R1471`, `cto-2026-10-14.md:13`, HIS RULING + APPROVED, "K5 cards (1)-(4), (6) owed") or have the desk record his word first. The desk chooses (ASK DESK 1); R1536 can stay in `## WHY`.
2. NOTE: the card never mentions `ops/desk/desk-done.sh` (card 17 A5, tested in `tests/ops/test_desk_done.py`). It already does `claude stop`, `claude rm` and `herdr tab close` from a stop line and refuses `brain*` and `cto-desk`; the tab id is passed by the desk. C1 `job-close.sh` is a second closer: the difference is the tab found by title, the three-way proof and the `cto-desk` and exact `brain` test (desk-done refuses any `brain*` name). Desk to decide whether C1 reuses or replaces `desk-done.sh`; if both stay, say so under `## NOT IN THIS JOB`.
3. NOTE: C1's source for `terminal_title_stripped` and `herdr tab close <tab_id>` is not at `ops/cto-desk.sh:325-362`; the only repo hit is `desk-done.sh:71` and `test_desk_done.py`. The drafter's one live `herdr pane list` read is the only proof of the key.
4. NOTE: C2 (c), `job-close.sh` not beside the script: the card puts the stderr-only line but not when it is tested. If the 120 s close-wait runs first, every existing build or check stop-line test of `test_desk_watch.py` (no `job-close.sh` staged, a worktree that does not exist) waits `DESK_WATCH_CLOSE_WAIT`, and `test_a_report_already_at_its_stop_line_returns_at_once` (`< 5 s`, `:101`) goes red. The builder must test for `job-close.sh` before the poll.
5. NOTE: C3 says `finished_open` reuses "the cached read of `unsettled()`'s `seen["list"]`", but `seen` is local to `unsettled()` (`stop-guard.py:344`); a single read per stop needs `unsettled()` to hand it back or a second `desk-list.sh` run, and the row says nothing else of the file changes. Also a `ListUnreadable` raised from `finished_open` needs the same `UNREADABLE` path as `:393-394`.
6. NOTE: `LADDER: OFF-LADDER — reports/cto-2026-10-15.md` has no `<date> R<n>` tail (the `CARD.md` shape `OFF-LADDER — <report> <date> R<n>`); siblings were not compared. Not read by `desk-launch.sh` as far as `grep` shows.
7. NOTE: C2's launcher block (every kind of the common tail) also closes an idle replaced `deploy-hub-<job>` session (a STEP-D0 relaunch), while C2 (d) says a deploy hub is "closed by the desk". Say which wins. Also unspecified: the block's behaviour when `claude agents --json` is unreadable (fail open or `REFUSED`); other launcher tests with a stub `claude` that prints nothing for `agents` may be hit (the prechecks stub answers `[]`). The `tests/ops` whole run in ORDER would catch it, not name it. And 582's overlap with `:2294-2296` is still to be proved by that card's drafter.

PREFLIGHT DONE · card: close-automation-1015 · checks: 16 · fails: 2 · ready: NO
