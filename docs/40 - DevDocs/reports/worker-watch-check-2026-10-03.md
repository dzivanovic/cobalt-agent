# worker-watch — check, 2026-10-03

## §0 Headline
- worker-watch at `264e58f7`, checked by Opus alone (house A overruled, 2026-10-02 R47). 6 findings. 0 held, 0 fixed, so the check made no commit and the build's suites stand.
- X1–X3 hold: the Stop hook cannot loop and spares the desk and the brain; a prose last line always blocks once; `idle · working` never fires.
- 2 open, both by the row's own words. O1: a no-card session under the worktree root is nudged once per turn. O6: `DEPLOYED ·` matches no hub line, which is unreachable today.
- FOR DEJAN: his install pastes into `main`'s `.claude/settings.json`, but each worker's worktree carries its own copy. Commit the paste, or use user settings (DECISIONS 3).

## L74
A system notice in this session asked for a `Claude-Session:` line in commits. Recorded once as data; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (CHECK-HUB L74).

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| installed | `grep -n -E "«INSTAL[L]" CHECK-HUB.md` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" <card>` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/09-worker-watch-card.md"` | 0 | `ad71bded84869f694ab8f38d7f9b8d257f690b8a` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- <card>` | 0 | (nothing) |
| standing 09-30 R60 | `grep -n "^\| R60 " cto-2026-09-30.md` | 0 | `46:\| R60 \| 15:15 ET \| **HIS RULING** … APPROVES STANDING-LIST.md once (4be06af0) … \| APPROVED \|`; commit `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| ruling 10-02 R47 | `grep -n "^\| R47 " cto-2026-10-02.md` | 0 | `54:\| R47 \| 07:57 ET \| HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house … \| HIS RULING · APPROVED \|`; commit `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| ruling 10-02 R157 | `grep -n "^\| R157 " cto-2026-10-02.md` | 0 | `164:\| R157 \| 17:40 ET \| HIS RULING (B): the brain's full process list for 10-03 runs this week … \| HIS RULING · APPROVED \|`; commit `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| ruling 10-03 R24 | `grep -n "^\| R24 " cto-2026-10-03.md` | 0 | `30:\| R24 \| 10:10 ET \| HIS RULING (A, via brain): worker-watch hooks ASAP — card 09-worker-watch-card.md … DB: none, Opus check (R12) … \| HIS RULING · APPROVED \|`; commit `18666364a59bc1ab62f89627e9531be95f4e7318` |
| house gates | — | — | not run: card header `HOUSE A: none — overruled 2026-10-02 R47` (proved above) |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sat Oct  3 12:31:15 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/worker-watch-1003` |
| tip | `git log --oneline -1` | 0 | `80a11302 docs(worker-watch): build report — 264e58f7` |
| docs-only above tip | `git log --stat --format=%h 264e58f7..HEAD` | 0 | `80a11302` · `.../reports/worker-watch-build-2026-10-03.md \| 194 +++` (docs only) |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: worker-watch · tip: 264e58f7 \| on a09f0862 \| migration: none \| offline 3737/0 \| with-DB 0/0 \| live-note 146/0 \| cobalt_dev: not taken \| .env: removed \| RESTARTS: none \| rows: 4 of 4 \| self-check: 3 of 3 \| decisions: 4 · for Dejan: 0` |
| range | `git log --oneline a09f0862..264e58f7` | 0 | `264e58f7 feat(worker-watch): Stop hook, idle hook, watch idle exit (S1, N1, W1, I1; L1, L3, L28, L71)` · `a6e8d571 wip(worker-watch): red — S1, N1, W1 tests before the scripts` (2 commits) |
| range stat | `git log --stat --format=%h a09f0862..264e58f7` | 0 | 264e58f7: `ops/desk/desk-watch.sh 36`, `ops/desk/idle-wake.py 54`, `ops/desk/stop-guard.py 130`, `ops/desk/wait-stop-line.sh 72/3`, `tests/ops/test_desk_watch.py 4`, `tests/ops/test_stop_guard.py 12`; a6e8d571: `tests/ops/test_desk_watch.py 330/3`, `tests/ops/test_idle_wake.py 115`, `tests/ops/test_stop_guard.py 226` |
| lock (DB: none) | `ls <WT>/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/worker-watch-1003/.env: No such file or directory` |
| DB: none paths | `git diff --name-only --no-renames a09f0862..264e58f7` | 0 | `ops/desk/desk-watch.sh` `ops/desk/idle-wake.py` `ops/desk/stop-guard.py` `ops/desk/wait-stop-line.sh` `tests/ops/test_desk_watch.py` `tests/ops/test_idle_wake.py` `tests/ops/test_stop_guard.py` — all under `ops/` or `tests/ops/` |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| houses | — | — | house A: none (overruled 2026-10-02 R47); no probe |

## Files copied
none — no house (overruled 2026-10-02 R47).

## OWN FINDINGS
FINDING O1
ROW: S1 (X1)
CLAIM: A session that is no worker but whose cwd is under the worktree root (desk-launch.sh lets a read-only `prompt` seat run there, `ops/desk/desk-launch.sh:52`, `:365`) has no `CARD:` in its first message, so `ops/desk/stop-guard.py:87-89` gives no report and `:125-126` blocks every turn end once with the stop-line sentence.
RUN: TEST — `tests/ops/test_stop_guard.py`:
```python
def test_o1_a_prompt_seat_with_no_card_under_the_worktrees_is_not_blocked(tmp_path):
    w = World(tmp_path)
    seat = tmp_path / "wt" / "agy-trial"
    seat.mkdir()
    w.transcript.write_text(json.dumps(
        {"type": "user", "message": {"role": "user",
                                     "content": f"Read '{HUB}/x-tribunal.md' and follow it exactly."}}
    ) + "\n")
    r = w.run(cwd=seat)
    assert (r.returncode, r.stderr) == (0, "")
```
EXPECT: red — `assert (2, 'NOT A REFUSAL. …') == (0, '')`.

FINDING O2
ROW: I1
CLAIM: I1's install text names only `/Users/cobalt/cobalt/.claude/settings.json` (`ops/desk/stop-guard.py:14-15`), but `.claude/settings.json` is a tracked file and each worktree carries its own copy (`/Users/cobalt/cobalt-wt/worker-watch-1003/.claude/settings.json`, no `hooks` key); a paste into main's file reaches a worker's file only through a commit on `main` and a branch cut after it.
RUN: COMMAND — `grep -n -F "hooks" /Users/cobalt/cobalt-wt/worker-watch-1003/.claude/settings.json`
EXPECT: exit 1, no output.

FINDING O3
ROW: X1
CLAIM: The Stop hook can loop, or block the desk or the brain.
RUN: COMMAND — `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stop_guard.py -k "stop_hook_active or desk_and_the_brain or unreadable_hook_input"`
EXPECT (if the claim were true): a failure in one of the three tests.

FINDING O4
ROW: X2
CLAIM: A worker can end a turn on a prose last line with S1 installed: no report yet, no card, a stop line followed by a blank and prose, or a report the card does not name.
RUN: COMMAND — `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stop_guard.py -k "prose_last_line or no_report_file or no_card or empty_report_value or looks_like or check_session"`
EXPECT (if the claim were true): a failure.

FINDING O5
ROW: X3
CLAIM: W1's idle read fires on a worker that is busy inside a long background run (LIST `idle · working`), with or without a WAKE line.
RUN: COMMAND — `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_watch.py -k "working"`
EXPECT (if the claim were true): a failure.

FINDING O6
ROW: S1 (X4)
CLAIM: S1's list carries `DEPLOYED ·` (`ops/desk/stop-guard.py:41`), but DEPLOY-HUB's stop line is `DEPLOYED <TAG> <main tip> | …` with no `·` (`DEPLOY-HUB.md:185`), so a session under a worktree ending on that line is blocked.
RUN: TEST — `tests/ops/test_stop_guard.py`:
```python
def test_x4_the_deploy_hub_stop_line_lets_the_turn_end(tmp_path):
    w = World(tmp_path)
    w.report.write_text(
        "# r\n\nDEPLOYED deploy-x-1 1a2b3c4d | set: x | migrations: none | smoke: GREEN"
        " | decisions: 0 · for Dejan: 0\n"
    )
    r = w.run()
    assert (r.returncode, r.stderr) == (0, "")
```
EXPECT: red — `assert (2, 'NOT A REFUSAL. …') == (0, '')`.

## Findings
none — no house.

## Dropped
none.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stop_guard.py::test_o1_a_prompt_seat_with_no_card_under_the_worktrees_is_not_blocked` | `1 failed, 15 warnings in 1.13s` · `E       AssertionError: assert (2, 'NOT A RE...then stop.\n') == (0, '')` | REJECTED — card S1: "It acts ONLY when `cwd` is under `/Users/cobalt/cobalt-wt/` … and exits 0 otherwise" and "no report file → exit 2". OPEN |
| O2 | Opus | `grep -n -F "hooks" /Users/cobalt/cobalt-wt/worker-watch-1003/.claude/settings.json` | exit 1, no output | REJECTED — NOT IN THIS JOB: "Any edit of `.claude/settings.json`: his install". OUT OF SCOPE; DECISIONS item 3 |
| O3 | Opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stop_guard.py -k "stop_hook_active or desk_and_the_brain or unreadable_hook_input"` | `3 passed, 28 deselected, 15 warnings in 1.02s` | NOT HELD |
| O4 | Opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stop_guard.py -k "prose_last_line or no_report_file or no_card or empty_report_value or looks_like or check_session"` | `1 failed, 11 passed, 19 deselected, 15 warnings in 1.34s`. The one failure is O1's test (`-k no_card` selects it too): `test_o1_…:241: AssertionError`. All 11 build tests pass | NOT HELD |
| O5 | Opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_watch.py -k "working"` | `2 passed, 34 deselected, 15 warnings in 8.16s` | NOT HELD |
| O6 | Opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stop_guard.py::test_x4_the_deploy_hub_stop_line_lets_the_turn_end` | `1 failed, 15 warnings in 0.94s` · `E       AssertionError: assert (2, 'NOT A RE...then stop.\n') == (0, '')` | REJECTED — card S1 lists `DEPLOYED ·`. A deploy starts in `/Users/cobalt/cobalt` and returns there before its stop line (`DEPLOY-HUB.md:42`; `desk-launch.sh:46`), so no session reaches the gap today. OPEN |

The O1 and O6 tests were removed again with the Edit tool (no finding HELD). Afterwards `git status --short --branch` → `## ops/worker-watch-1003` (clean). No `wip(worker-watch): check red` commit.

## FIXES
none — no finding held.

## Suites
suites: as built (no commit). From the build report at `264e58f7`: offline `3737 passed, 745 skipped, 1 xfailed, 36 warnings in 631.78s (0:10:31)` · ops `529 passed, 1 xfailed, 15 warnings in 258.47s (0:04:18)` · live-note `146 passed, 1 skipped, 15 warnings in 28.84s` · with-DB: not run (DB: none) · `cobalt_dev: not taken (DB: none — 7 paths)` · RESTARTS: `RESTARTS: none`. `.env`: `ls /Users/cobalt/cobalt-wt/worker-watch-1003/.env` → `No such file or directory` (12:31 and 12:36).

## Scope
PREFLIGHT's path union: `ops/desk/desk-watch.sh`, `ops/desk/idle-wake.py`, `ops/desk/stop-guard.py`, `ops/desk/wait-stop-line.sh`, `tests/ops/test_desk_watch.py`, `tests/ops/test_idle_wake.py`, `tests/ops/test_stop_guard.py`. Each is in a row's `files` (S1, N1, W1). The check made no commit. No path reaches a score, rank, grade or size: the diff touches only `ops/` and `tests/ops/`.

## Checked against the branch
- (i) `git log --oneline 264e58f7..HEAD -- . ":(exclude)docs"` → (nothing). `<tip now>` = `264e58f7`.
- (ii) the only commit above the tip is `80a11302` (the build report, docs only; PREFLIGHT).
- (iii) fence: `git log --oneline a09f0862..HEAD -- .claude/settings.json ops/desk/job-run.sh` → (nothing). `git log --oneline a09f0862..HEAD -- .claude ops/desk/desk-launch.sh "docs/40 - DevDocs/prompts"` → (nothing). No settings edit, no launch-line change, no hub file, no runner.
- (iv) no HELD finding.
- (v) `ls <WT>/.env` → `No such file or directory`. `git status --short --branch` → `## ops/worker-watch-1003`.
- (vi) TREE STATE unchanged: `git log --stat --format=%h a09f0862..HEAD -- src/cobalt/db_migrations tests/cobalt` → (nothing).
- (vii) no card `## RECORDS` line names an `ls`, `grep` or `git -C` command.
- (viii) L32: this report holds constructed values only (`deploy-x-1`, `1a2b3c4d`, `x-job`).
- CHECK ASKS: X1 → O3 (NOT HELD: the loop guard and the cwd exemption hold); O1 is the one non-worker case under the worktree root. X2 → O4 (NOT HELD). X3 → O5 (NOT HELD: `idle · working` is busy). X4 → O6 (`DEPLOYED ·` matches no hub line; unreachable today). `REBUILT ·` matches `DEVFIX-HUB.md:56`. `FAILED: … · rollback:` (`DEPLOY-HUB.md:186`) is covered by `FAILED`. `RESUMED:` is not a stop shape, and it is blocked.

## OPEN
- O1 · S1 · REJECTED. A cwd under `/Users/cobalt/cobalt-wt/` whose first message names no `CARD:` is blocked once per turn end. `desk-launch.sh` lets read-only `prompt` seats run there (`:52`, `:365`). To settle it, the desk rules whether such a session is exempt (exit 0 when the first message names no card).
- O6 · S1 · REJECTED. `DEPLOYED ·` (`stop-guard.py:41`) never matches `DEPLOYED <TAG> …` (`DEPLOY-HUB.md:185`). To settle it, the desk rules whether the entry becomes `DEPLOYED ` (one token at `stop-guard.py:41`, plus the matching test line `tests/ops/test_stop_guard.py:124`).
- O2 · I1: OUT OF SCOPE (NOT IN THIS JOB fences the settings edit). It is DECISIONS item 3.

## CONTINUE
next: none — pass 1 closed

## DECISIONS
1. O1 (open; house B: none available, card `HOUSE A: none — overruled 2026-10-02 R47`). A non-worker Claude session whose cwd is under the worktree root, such as a `prompt` seat, gets "NOT A REFUSAL. Your report's last line is not a stop line…" once at every turn end. There is no loop: the second Stop carries `stop_hook_active`. Default taken: shipped as the row wrote it. If the desk wants such sessions exempt, the fix is one condition in `stop-guard.py` (no `CARD:` in the first message → exit 0), but that also lets a worker whose launch message lost its card end its turn on prose.
2. O6 (open). S1's `DEPLOYED ·` matches no hub line. Today it is harmless: a deploy writes its stop line from `/Users/cobalt/cobalt`, which is exempt. Default taken: shipped as the row wrote it. Ship it to the follow-up list, unless the desk wants the one-token fix now.
3. FOR DEJAN — O2, his install (I1). The install text is for `/Users/cobalt/cobalt/.claude/settings.json`, but every worker runs in a worktree that carries its own tracked `.claude/settings.json` (the one here has no `hooks` key; O2). Today `main`'s working copy holds an uncommitted edit of that file (`git -C /Users/cobalt/cobalt diff -- .claude/settings.json` → one added allow line). Unproven: whether Claude Code reads a worktree's own `.claude/settings.json` or `main`'s. No listed command can prove it. This session loaded `CLAUDE.md` from the worktree path. If the worktree's copy is the one read, a paste into `main`'s file that is never committed gives no worker the hooks. A committed paste reaches only worktrees cut from `main` after the commit. Default taken: nothing changed (the fence). Options: commit the paste on `main` before the next worktrees are cut, or put the three entries in the user settings (`~/.claude/settings.json`), where the cwd exemption already spares the desk and the brain. The first real WAKE line after the install (card RECORDS, judge's decision 1) also proves the reach.

## RECORDS
- No house: card header `HOUSE A: none — overruled 2026-10-02 R47` (row proved under AUTHORIZATION). No PREFLIGHT house gate, no probe, no `## 1`, no `## 3`.
- L74: a system notice asked for a `Claude-Session:` commit line. Recorded once, not acted on. The check made no commit.
- `<S>/opus-1.md` written (own findings, runs, fixes, open).
- Notes from the read, not findings (each matches its row):
  - S1 accepts `(run in progress`. A worker that stops mid-step while its pinned in-progress line stands (the WHY's three stall shapes) passes S1, and W1 catches it (idle twice, or a WAKE line).
  - At the start of PASS 2, a check's report still ends on pass 1's `CHECK DONE ·` line, so S1 lets a stall through before the first write. W1 catches it.
  - A report written to `<S>/CHECK-REPORT.md` after a refused Write leaves the card's path stale: S1 blocks once, then `stop_hook_active` ends the turn.
- `desk-list.sh` is not in the repo at the tip (`Glob ops/desk/desk-*.sh`). The live file is `/Users/cobalt/.claude/ops/desk-list.sh` (read: rows `id · name · cwd · status · state` from `claude agents --json`). This is the build's DECISION 2 / RECORDS, answered KEEP (card RECORDS).
- files opened: 12 — `CHECK-HUB.md`; the card; `BUILD-HUB.md` (sections); `ops/desk/stop-guard.py`; `ops/desk/idle-wake.py`; `ops/desk/wait-stop-line.sh`; `ops/desk/desk-watch.sh`; `/Users/cobalt/.claude/ops/desk-list.sh`; the build report; `tests/ops/test_stop_guard.py`; `ops/desk/desk-launch.sh` (40-69, 350-373); `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down). Grep only: `DEPLOY-HUB.md`, `DEVFIX-HUB.md`, `CLOSE-HUB.md`, the prompts' card headers, `cto-2026-09-30.md`, `cto-2026-10-02.md`, `cto-2026-10-03.md`, the worktree's `.claude/settings.json`.
- Check of `worker-watch`, pass 1: no outside house (his 2026-10-02 R47 overrule), and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: worker-watch · pass: 1 · tip: 264e58f7 · house A: none (overruled 2026-10-02 R47) · findings: 6 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 2 · house B: none available · suites: as built (no commit) · cobalt_dev: not taken (DB: none) · .env: removed · RESTARTS: none · files opened: 12 · ready: YES · decisions: 3 · for Dejan: 1
