# draft-k5-close-automation — 2026-10-15

## §0 Headline
- Card 580 written: `prompts/2026-10-15/580-close-automation-card.md`, class K5, rows C1 job-close.sh, C2 desk-watch auto-close and launcher replaced-session close, C3 stop-guard FINISHED block, C4 install-ops after DEPLOYED.
- One NEW test file, `tests/ops/test_close_automation_1015.py`; every row red first with controls; no existing test edited.
- No new allow string or command (R411, R412 not triggered); no overlap with 546, 549, 550; BAND card overlap UNPROVEN.
- 10 ASK DESK items, each with a default; nothing was run but reads.

## DECISIONS
- ASK DESK 1: `RULINGS: 2026-10-15 R1536`, but R1536 is a DESK RECORD (brain, L79), not a HIS RULING row; `authorize.sh` may refuse it. Default: keep R1536 (the only row naming the ask); the desk swaps in his own row if one exists. [09:39 ET]
- ASK DESK 2: the tab of a session is found by the herdr pane whose `terminal_title_stripped` equals the session name (worker panes carry no `agent_session`; read once on `herdr pane list`); two panes of one name give KEPT. Default: as written in C1. [09:39 ET]
- ASK DESK 3: the worker's last turn is still ending at its stop line, so C2 polls clean (tree, report, idle) for `DESK_WATCH_CLOSE_WAIT` seconds before KEPT. Default: 120 s. [09:39 ET]
- ASK DESK 4: C2 auto-closes `build`, `check`, `devfix`, `shadow` only; `deploy`, `prodwrite`, `close` print `KEPT <session>: closed by the desk` (W8 closes a deploy hub but its tree and report differ; no ruling names a script step). Default: as written. [09:39 ET]
- ASK DESK 5: a check's report sits on main and is the desk's to commit, so a check is KEPT `report not committed` until the desk commits and runs `job-close.sh` by hand. Default: as written. [09:39 ET]
- ASK DESK 6: the header of `desk-watch.sh` says `Read-only` (`:3`) and `Writes nothing.` (`:15`); C2 and C4 make both false. Default: the row rewrites those two sentences. [09:39 ET]
- ASK DESK 7: C3's source is a new record file `/Users/cobalt/cobalt-wt/.job-state/FINISHED` that C2 appends to at each clean stop line; the OWED text names no source. Default: as written (a stale line is harmless, the guard also needs a LIST row). [09:39 ET]
- ASK DESK 8: wording and exit codes not in a ruling: `CLOSED`/`KEPT` exit 0 and a bad id `REFUSED:` exit 1 (C1); `install-ops FAILED: <first line>` when install-ops exits non-zero (C4). Default: as written. [09:39 ET]
- ASK DESK 9: the launcher's replaced-session block refuses (`REFUSED: a session named <name> is still busy or kept`) when the old row is busy or `job-close.sh` prints KEPT, instead of closing a live worker; never runs under `DESK_LAUNCH_DRY=1`. Default: as written. [09:39 ET]
- ASK DESK 10: the BAND and routing card (undrafted) edits `desk-launch.sh` (the `<model>` fill, `:2233`) 60 lines above this card's one block (`:2294-2296`); overlap UNPROVEN. Default: the desk compares the two cards before launching both builds. [09:39 ET]

## RECORDS
- 2026-10-15 09:39 ET (`date`), `main` HEAD `bcdef9f0` (`git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD`). `git -C /Users/cobalt/cobalt diff HEAD --stat` over `desk-watch.sh`, `stop-guard.py`, `desk-launch.sh`, `desk-list.sh`, `wait-stop-line.sh`, `bare-guard.py`, `test_desk_watch.py`, `test_stop_guard.py`, `test_install_ops.py`, `restarts.py` printed nothing: each `file:line` read is HEAD's. `git -C /Users/cobalt/cobalt show HEAD:ops/desk/desk-watch.sh` read whole.
- Read: `CARD.md`, cards 549 and 550, `cto-2026-10-15.md` (OWED, LESSONS, R1536, R1542), checklist W8 (`cto-desk-checklist.md:60`), `desk-watch.sh`, `stop-guard.py`, `desk-launch.sh` (`:100-110`, `:263-285`, `:496-522`, `:921-947`, `:2214-2304`), `wait-stop-line.sh:43-45`, `desk-list.sh`, `ops/cto-desk.sh:325-362`, `DEPLOY-HUB.md:135`, `reports/deploy-desk-refresh-1013.md:207` (the DEPLOYED line), `restarts.py:38`, `:225-228`, `:232`, `:246`, the pins under `tests/ops/` (`test_desk_watch.py:26-100`, `test_stop_guard.py:300-378`, `test_install_ops.py:20-62`), `.claude/settings.json` at HEAD (the grants `claude stop`, `claude rm`, `herdr *`, `sh /Users/cobalt/.claude/ops/*`).
- `herdr pane list` ran once, read only: worker panes carry `terminal_title_stripped` = the session name and a `tab_id`.
- Overlap: 546 (`DEPLOY-HUB.md:15`, `:129`, `deploy-shipped.sh`), 549 (`CTO-DESK-WAKEUP.md:13`, `STANDING-LIST.md` §4), 550 (`CARD.md`): none edits `desk-watch.sh`, `stop-guard.py`, `desk-launch.sh` or the new test file.
- No test, no production command, no git write, no launch.

DRAFTED · decisions: 10
