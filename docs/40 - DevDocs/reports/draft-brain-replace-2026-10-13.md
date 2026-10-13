# draft-brain-replace 2026-10-13

## §0 Headline
- Card `prompts/2026-10-13/462-brain-replace-card.md` written, uncommitted: K5, rows D1 (`desk-done.sh` kind `brain`), L1 (`desk-launch.sh brain` replaces an asked brain), R2 (restarts run).
- The guards sit at `desk-done.sh:62-64` and `desk-launch.sh:803-813`; R1331's `:57` and `:730` point elsewhere (`:57` is `case $?`, `:730` is kind `prompt`).
- The ask row is pinned: today's committed `cto-<ET date>.md`, a `| R<n> |` line holding `DESK RECORD` and `` brain `<id>` asked for its replacement ``.
- BASE is the only fill token. The desk commits the card and fills BASE.

## DECISIONS
- ASK DESK 1: the ask row's fixed phrase is `` brain `<id>` asked for its replacement `` inside a `DESK RECORD` row; the desk writes its record row in that shape before it calls either script. Default: this phrase. [06:56 ET]
- ASK DESK 2: only today's ET report counts (`cto-<D>.md` at the call), so an ask recorded yesterday must be recorded again today. Default: today only. [06:56 ET]
- ASK DESK 3: the report must be committed and unchanged (the launcher's `committed` test, `desk-launch.sh:233-237`). The desk runs `desk-commit.sh` on the row first. Default: committed. [06:56 ET]
- ASK DESK 4: `desk-launch.sh brain` stops the asked brain through `desk-done.sh … brain` beside it, so both scripts share one stop path. It runs no `claude stop` of its own and closes no tab; the brain's tab stays the desk's (`herdr tab close`). Default: through `desk-done.sh`, no tab. [06:56 ET]
- ASK DESK 5: under kind `brain`, `desk-done.sh` accepts only a session named exactly `brain` (the seat's name, `desk-launch.sh:785-786`); `brain-*` names stay refused under every kind. Default: exactly `brain`. [06:56 ET]

## RECORDS
- `main` HEAD `2f043f0b` at 06:45 ET (`git -C /Users/cobalt/cobalt rev-parse HEAD`). `git status --short ops tests` printed nothing. The last commit on the four files is `df775390`.
- CARD.md read whole. The format precedent is `458-desk-refresh-card.md`, read whole (header order, `INSTALL: none`, `RESTARTS: none`, `## DEPLOY PROOF`).
- `grep -n "survey row 19" reports/cto-2026-10-13.md` → row R1331 (DESK RECORD, DIRECTION).
- Guards, by `grep -n`/`sed -n`: `desk-done.sh` 71 lines, whole; `desk-launch.sh:150-156`, `:217-300`, `:690-860`, `:730`, `:745`, `:1112-1128`, `:1295-1350`; `desk-list.sh` whole (19 lines).
- Rulings: R76 at `cto-2026-09-30.md:67`; R131 at `cto-2026-10-02.md:138`; R188 and R191 at `cto-2026-10-03.md:194`, `:197`; R1138 at `cto-2026-10-12.md:173`; checklist W8 at `topics/cto-desk-checklist.md:60`.
- The 10-11 case: `cto-2026-10-11.md` R1102 (the ask, inside a LAUNCHED row) and R1104 (`3d24c7e5` stopped under R188/R191). No DESK RECORD row carries the ask, so the red tests build one in a fixture.
- Tests: `tests/ops/test_desk_done.py` lines 1-60 and 160-185, plus its test list; `tests/ops/test_desk_launch_brain.py` lines 20-192, plus its test list. Nothing was run.
- Install: `ls -la /Users/cobalt/.claude/ops` shows both scripts symlinked into `ops/desk/`. Restarts: `src/cobalt/jobs/restarts.py:222-247`.
- Commands used: only the allowed reads (`git -C … rev-parse/log/status`, `ls`, `grep`, `sed -n`, `wc`, `cat`, `head`, `date`). No new command class is needed, so there was no `ASK DESK` for one.
DRAFTED · decisions: 5
