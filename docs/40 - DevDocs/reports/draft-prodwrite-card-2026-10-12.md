# draft-prodwrite-card — 2026-10-12

## §0 Headline
- Card written: `prompts/2026-10-12/392-prodwrite-seat-card.md`, `CLASS: K3, K5`, `INSTALL: none`, 8 rows (W1 hub + STANDING-LIST + CARD.md section, W2 launcher kind, W3 guard G2/G5/G7, W4 authorize, W5 watch/done, W6 prompt-kind production refusal, W7 deny pins, W8 RESTARTS RUN).
- Guard finding: a seat on a new `PRODWRITE-HUB.md` run from `/Users/cobalt/cobalt` is kind `None` today, and G2 skips kind `None` (`bare-guard.py:779-790`, `:1074`): it would pass every production command. W3 makes it kind `prodwrite`, passing only the card's one command, `backup run`, `backup status` and the R686 read.
- Launcher finding: the prompt kind's F5 exception (`desk-launch.sh:571-589`) lets a ruled prompt line carry a `COBALT_ENV=production` write string; W6 closes it.
- The desk's own production rules for the check to compare: L51 (1) `COBALT_ENV=production` pre-approved on a deploy's production command; L62 PRODUCTION READS (G2 passes the one `db query` read for every seat, R686); L81 K3/K5 (`COBALT_ENV=production*` deny and G2 stay on every other line).

## DECISIONS
- ASK DESK: a raw SQL statement has no Cobalt tool in production (`db query` is `BEGIN READ ONLY`, `src/cobalt/db_query.py:163`); allow statements? [06:20 ET] Default taken: no. The card's write is an existing `cobalt` verb; a statement needs a Cobalt write verb, built on its own card first.
- ASK DESK: the backup step — always `cobalt backup run` (restic snapshot with the `cobalt_brain` dump), or the inverse alone? [06:20 ET] Default taken: always `backup run`, refused if missing; the `inverse` cell (or `none`) is written under `## ROLLBACK` before the write and is never run by the seat.
- ASK DESK: must the `WRITE RULING` row name this job, or is any HIS RULING · APPROVED row enough (R1138 itself)? [06:20 ET] Default taken: any row `ruling_row` proves; the card row names the write (K3: "named by a card row or a ruling of his").
- ASK DESK: the stop line carries no `tokens:` field (L71) because the prompt fixes its shape exactly. [06:20 ET] Default taken: the prompt's exact shape; tokens recorded under `## RECORDS`.
- ASK DESK: the prompt says `Bash(COBALT_ENV=production*)` stays in the deny list of every other kind, but today it is on the build, check, devfix and shadow lines only; deploy and close allow named production strings, and desk, brain and prompt lines are held by G2 alone. Add the deny to those lines? [06:20 ET] Default taken: no line change (the desk's own R686 reads would break); W7 pins every line's production strings as they stand today, and W3 Q5 shows G2 denies the seat's command for every other kind.
- ASK DESK: the seat's count verify uses the wildcard `Bash(COBALT_ENV=production uv run cobalt db query *)` (read-only by the tool and by `prod_read`), since an exact SQL string cannot sit inside the eval'd line's quotes. [06:20 ET] Default taken: the wildcard read string, as the deploy line already carries it.
- ASK DESK: a prodwrite never resumes, and a write is never re-run (a re-run could apply it twice). [06:20 ET] Default taken: the launcher refuses a resume step; a stopped write is a new card after the desk reads the backup line.

## RECORDS
- `main` HEAD `6468fb5e` (`git rev-parse --short=8 HEAD`, 06:20 ET); every `file:line` below read at that HEAD.
- `hands-off-answer-2026-10-12.md` read whole: K3 row `:22`, K5 `:24`, card C3 `:32`. R1138 = `cto-2026-10-12.md:12`, HIS RULING · APPROVED, added in `5d6ce588`; `git diff --stat HEAD` on both files prints nothing.
- LAWS read: L29 `:204-208`, L37 `:236-238`, L41 `:249-250`, L51 `:285-286`, L62 `:320-324`, L63 `:326-328`, L81 `:403-406`.
- `CARD.md` whole; `BUILD-HUB.md` whole; `DEPLOY-HUB.md` whole (`:11` the line, `:13` the token fill, `:131` D2.4 `backup run`); card 386 whole (RUN row L3 the RESTARTS precedent).
- `desk-launch.sh` (1687 lines): `:16-46` desk lines, `:104-163` refusals, `:245-247` `watch_line`, `:253-269` `ruling_row`, `:316` usage, `:571-600` F5, `:720-730` brain's live-session read, `:883-898` kind → fixed file, `:914-993` card gates, `:1302-1304` `ship_cell`, `:1310-1365` build/shadow arm (`:1360-1362` the character rule), `:1423-1464` deploy (`:1447` production strings), `:1465-1516` devfix, `:1606-1687` line fill, mode check, dir.
- `bare-guard.py` (1376 lines): `:65` G2 route, `:90-98` HUBS/WORKERS, `:147` PROD, `:741-763` `read_card`, `:766-798` `seat`, `:965-1006` `prod_read`, `:1060-1103` `bash_rules` (G2 `:1074`), `:1225-1268` `g5`.
- `authorize.sh:1-60`; `desk-watch.sh:30-69`; `desk-done.sh:22-27`; `stop-guard.py:1-30`, `:150-175`, `:380-414` (worker cwd only).
- `src/cobalt/backup/cli.py:24-77` (`run`, `status`, `restore`; `:62` the database line); `src/cobalt/backup/restic.py:55-84` (`describe`); `src/cobalt/db_query.py:145-215`; `src/cobalt/jobs/restarts.py:38`, `:225-246`.
- Tests read: `test_hub_lines.py:1-100`; `test_bare_guard.py:186-275`, `:380-420`; `test_desk_launch_prechecks.py:73-230`, F5 tests `:981-1036`; `test_desk_launch_brain.py` stub `:106-108`.
- Production-string Grep over `prompts/*.md` (06:20 ET): deny `Bash(COBALT_ENV=production*)` on BUILD, CHECK, DEVFIX, SHADOW lines; `CLOSE-HUB.md:10` allows `validate*` and `heartbeat show*`; BRAIN, OPS-HAND, SPIKE, CTO-DESK-WAKEUP hold none.
- `~/.claude/settings.json:22` hook = `python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py` (repo path); `.claude/settings.json:30` desk allow `Bash(sh /Users/cobalt/.claude/ops/*)`: `INSTALL: none`.
- REFUSED, not needed: two Bash `grep`s holding the production word were denied by G2 (this seat is kind brain); the same reads were made with the Grep tool.
- No commit, no launch, no production or database command (L36). The card and this report are the desk's to commit.

DRAFTED · decisions: 7
</content>
</invoke>
