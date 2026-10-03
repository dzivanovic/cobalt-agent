JOB: worker-watch
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R47
BRANCH: ops/worker-watch-1003
WORKTREE: worker-watch-1003
BASE: «FILL: the 8-hex head of main after set 1 (01 + 01b) is DEPLOYED»
TIP:
REPORT: /Users/cobalt/cobalt-wt/worker-watch-1003/docs/40 - DevDocs/reports/worker-watch-build-2026-10-03.md
CHECK REPORT:
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B:
TREE STATE: unchanged
DB: none
RULINGS: 2026-10-02 R47, 2026-10-02 R157, 2026-10-03 R24

## ROWS

WHY: the desk's watch waits for a changed stop line and nothing else, so a worker that goes idle without one (it asked in text, it stopped after a denied call, it finished a turn mid-step) leaves both sides waiting; a Sonnet desk waited hours this way (09-28 … 10-01), and this morning's `01b` hour was the same shape under Opus. His word: the biggest issue we have; install as soon as possible. Three guardrails, each a fact, each zero tokens until it fires. The two hooks are settings hooks (a command on JSON stdin; exit 2 blocks, stderr goes to the model): no mod, no new flag. They live in `ops/desk/`, run as `python3 <path>`, and enter `.claude/settings.json` by HIS ONE INSTALL (the same install as `bare-guard.py`'s entry: three entries, one paste). Tests in `tests/ops/` with stub inputs; no test touches a real session, `cobalt_dev`, a house or the network. `export LC_ALL=C` first in every shell script; `python3` scripts set `LC_ALL=C` in their environment for any subprocess.

| row | what | red first | files |
|---|---|---|---|
| S1 | `ops/desk/stop-guard.py`, a `Stop` hook. Reads the hook JSON from stdin (`cwd`, `transcript_path`, `stop_hook_active`). It acts ONLY when `cwd` is under `/Users/cobalt/cobalt-wt/` (a worker; the desk and the brain run in `/Users/cobalt/cobalt`) and exits 0 otherwise. It finds the worker's report: the one file matching `<cwd>/docs/40 - DevDocs/reports/*-build-*.md` or `*-check-*.md` newest by mtime, or the `REPORT` / `CHECK REPORT` of a card path named in the transcript's first user message when that is simpler and provable — say which under `## RECORDS`. If the report's last non-blank line begins with one of `BUILT ·`, `CHECK DONE ·`, `DEPLOYED ·`, `REBUILT ·`, `FAILED`, `FAILED PREFLIGHT`, `ASK DESK:` or `(run in progress)` → exit 0. Otherwise, when `stop_hook_active` is false → exit 2 with ONE stderr sentence: `NOT A REFUSAL. Your report's last line is not a stop line. Write the step's stop line, or FAILED: <step> — <what> — <reason>, or ASK DESK: <one question>, then stop.` When `stop_hook_active` is true → exit 0 (the turn ends; no loop). Never writes a file | `tests/ops/test_stop_guard.py`: stdin JSON built per case with a tmp worktree and report: a `BUILT ·` last line → exit 0; a prose last line, `stop_hook_active` false → exit 2 and the sentence; the same with `stop_hook_active` true → exit 0; `cwd` = `/Users/cobalt/cobalt` → exit 0 without reading any report; no report file → exit 2 with the sentence (a worker with no report has not started its fixed file). RED on `BASE`: no such file | `ops/desk/stop-guard.py`, `tests/ops/test_stop_guard.py` |
| N1 | `ops/desk/idle-wake.py`, a `Notification` hook. Reads the hook JSON; acts only when the notification is the idle kind (the session waiting for input; the JSON's `message` or type field says so — read the hook reference in `~/.claude` docs or the harness's help, and say which field under `## RECORDS`) and `cwd` is under `/Users/cobalt/cobalt-wt/`. It appends ONE line to `/Users/cobalt/cobalt-wt/.job-state/WAKE` (creating the dir if absent): `<time from the system clock, ET> <worktree name> IDLE <the report's last non-blank line, or "no report">`. Exit 0 always; never blocks | `tests/ops/test_idle_wake.py`: an idle notification for a tmp worktree with a report → one WAKE line with the worktree name and the last line; a non-idle notification → no line; `cwd` under the repo → no line; a second idle → a second line (append, never overwrite). RED on `BASE`: no such file | `ops/desk/idle-wake.py`, `tests/ops/test_idle_wake.py` |
| W1 | The shell watch exits on idle. `ops/desk/wait-stop-line.sh` and `ops/desk/desk-watch.sh` (card `18`): while waiting, every poll also reads `desk-list.sh` (beside the script) for the watched session's state and `/Users/cobalt/cobalt-wt/.job-state/WAKE` for a line naming the worktree; a session shown idle for two consecutive polls with the stop line unchanged, or a WAKE line → the watch exits 3 and prints `IDLE: <session> — <the WAKE line or "no WAKE line">` and the report's last five non-blank lines. The desk's LIST and CONTINUE then follow as today. A session not in the listing (gone) → exit 3 with `GONE: <session>` | `tests/ops/test_desk_watch.py` (the card `18` test file) gains: a stub `desk-list.sh` answering `idle` twice → exit 3 and the `IDLE:` line with the five lines; a WAKE line for the worktree → exit 3 at once; `busy` with a changed stop line → exit 0 as today. RED on `BASE`: the watch waits past the stub's idle answers until its timeout | `ops/desk/wait-stop-line.sh`, `ops/desk/desk-watch.sh`, `tests/ops/test_desk_watch.py`, `tests/ops/test_wait_stop_line.py` if it exists |
| I1 | HIS INSTALL TEXT, in `## RECORDS` of the build report and in the header of `stop-guard.py`: the `hooks` value for `/Users/cobalt/cobalt/.claude/settings.json`, with THREE entries — `PreToolUse` matcher `Bash` → `python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py`; `Stop` → `python3 /Users/cobalt/cobalt/ops/desk/stop-guard.py`; `Notification` → `python3 /Users/cobalt/cobalt/ops/desk/idle-wake.py` — as one JSON object he pastes once, valid JSON, proved by `python3 -c "import json,sys; json.load(open(sys.argv[1]))" <a tmp file holding it>` in the build. RUN — asserts nothing: quote the object | — | `ops/desk/stop-guard.py` (header only) |

## NOT IN THIS JOB
- Any edit of `.claude/settings.json`: his install, after set 2 is DEPLOYED (the scripts must be on `main` at the paths the entries name).
- A mod; a `--plugin-dir`; any launch-line change; any hub file.
- The runner (`job-run.sh`, card `06`) — it reads the same WAKE file; this card writes it.
- Any hook on the desk or brain seat: both are exempt by `cwd`.

## READ
- Claude Code hooks: the hook input JSON fields (`cwd`, `transcript_path`, `stop_hook_active`, the Notification message), the exit-2 block rule and the `stop_hook_active` loop guard — from `ops/desk/bare-guard.py` at `BASE` (how it reads stdin and exits 2) and the harness's hooks documentation as reachable read-only; what you could not verify goes under `## DECISIONS`, not into the code.
- `ops/desk/desk-watch.sh`, `wait-stop-line.sh`, `desk-list.sh`, `desk-context.sh` at `BASE`; `tests/ops/test_desk_watch.py`.
- `reports/harness-mods-review-2026-10-03.md` `## OPERATIONS A HOOK CAN TAKE` rows 20–23 (the ledger and the route; NOT built here — this card is the stall only).
- `BUILD-HUB.md` `## STOP LINE`, `## UNATTENDED RULES` (b): the lines S1 accepts are exactly the stop shapes and the `FAILED` / `ASK DESK` lines those sections define.

## CHECK ASKS
- X1 Can the Stop hook loop (block forever) or block the desk or the brain? Build the JSON cases and run the script.
- X2 Can a worker end a turn with a report whose last line is prose, with S1 installed, by any path (no report yet; a report in another folder; a stop line followed by a blank and prose)?
- X3 Does W1's idle read misfire on a worker that is busy inside a long background run (pass 1, 2–12 minutes with no transcript change)? The listing's state, not the stop line, must decide.
- X4 Is every line S1 accepts a line the hubs define, and is any hub stop shape missing from its list (`DEVFIX-HUB.md`'s `REBUILT`, the deploy's `FAILED: … · rollback:`)?

## RECORDS
- `DB: none`: every file is under `ops/` or `tests/ops/`; no lock.
- His words, brain session 10-03 (the desk's clock, about 10:1x ET): "As far as your hooks, yes, I want them installed as soon as possible because this is one of the biggest issues that we're having. The things are waiting for each other and both sides are waiting and not knowing what's going on."
- Mods and hooks are Anthropic process tuning: no outside house (his 10-03 word, desk row 2026-10-03 R12).
- Base: `main` after set 1; ships in set 2 with `03`, `02`, `06`. His install follows set 2's DEPLOYED line.
