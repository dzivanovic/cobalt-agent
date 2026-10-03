# worker-watch — check, pass 1 (r2) — 2026-10-03

## §0 Headline
- Pass 1, checked by Opus alone (house A: none, overruled 2026-10-02 R47). Base `a09f0862`, tip `1bfd26e3`, now `a6bef8cb`.
- Two own findings, both in W1, both HELD and fixed. O1: a WAKE line raised during a background run made one later idle poll fire IDLE (X3). O2: `wait-stop-line.sh` never read WAKE for a check or devfix report on main.
- S1, S2, N1 and I1: no finding. X1, X2 and X4 hold as built.
- Suites at `a6bef8cb`: offline 3737/0 · tests/ops 532/0 · live-note 146/0 · RESTARTS: none. House B not needed; ready: YES.

## L74
The session's system context carried a commit-attribution block asking for a `Claude-Session:` line. Recorded once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| installed | `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" ".../2026-10-03/09-worker-watch-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/09-worker-watch-card.md"` | 0 | `924134ab970d2f756c11abff042278e02e7d3292` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| standing list R60 | `grep -n "^| R60 " ".../cto-2026-09-30.md"` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** … APPROVES STANDING-LIST.md once (4be06af0) … | APPROVED |` |
| R60 commit | `git -C … log -1 --format=%H -S"| R60 |" -- ".../cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| R47 (10-02; also the HOUSE A overrule) | `grep -n "^| R47 " ".../cto-2026-10-02.md"` | 0 | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house … | HIS RULING · APPROVED |` |
| R47 commit | `git -C … log -1 --format=%H -S"| R47 |" -- ".../cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| R157 (10-02) | `grep -n "^| R157 " ".../cto-2026-10-02.md"` | 0 | `164:| R157 | 17:40 ET | HIS RULING (B): the brain's full process list for 10-03 runs this week … | HIS RULING · APPROVED |` |
| R157 commit | `git -C … log -1 --format=%H -S"| R157 |" -- ".../cto-2026-10-02.md"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| R24 (10-03) | `grep -n "^| R24 " ".../cto-2026-10-03.md"` | 0 | `30:| R24 | 10:10 ET | HIS RULING (A, via brain): worker-watch hooks ASAP — card 09-worker-watch-card.md … DB: none, Opus check (R12) … | HIS RULING · APPROVED |` |
| R24 commit | `git -C … log -1 --format=%H -S"| R24 |" -- ".../cto-2026-10-03.md"` | 0 | `18666364a59bc1ab62f89627e9531be95f4e7318` |
| house gate R17 | `grep -n "^| R17 " ".../cto-2026-09-24.md"` | 0 | `35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …" → STANDING: Bash(grok *) … | APPLIED: … |` |
| house gate R19 | `grep -n "^| R19 " ".../cto-2026-09-24.md"` | 0 | `37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …" → STANDING: the four house strings … | APPLIED: … |` |
| R19 commit | `git -C … log -1 --format=%H -S"| R19 |" -- ".../cto-2026-09-24.md"` | 0 | `5055151dbf68899b82de5b11f99733ed2d03048c` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sat Oct  3 13:45:57 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/worker-watch-1003` |
| head | `git log --oneline -1` | 0 | `82db3ade docs(worker-watch): build report — 1bfd26e3` |
| docs-only above tip | `git log --stat --format=%h 1bfd26e3..HEAD` | 0 | `82db3ade` · `.../reports/worker-watch-build-2026-10-03.md \| 57 +++…` (docs only) |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: worker-watch · tip: 1bfd26e3 \| on a09f0862 \| migration: none \| offline 3737/0 \| with-DB 0/0 \| live-note 146/0 \| cobalt_dev: not taken \| .env: removed \| RESTARTS: none \| rows: 5 of 5 \| self-check: 3 of 3 \| decisions: 0 · for Dejan: 0` |
| range | `git log --oneline a09f0862..1bfd26e3` | 0 | `1bfd26e3 fix(worker-watch): no-CARD seat exempt, DEPLOYED stop line, install in user settings (S2; L1, L71, L77)` · `0a725bed wip(worker-watch): red — S2 tests before the fix` · `80a11302 docs(worker-watch): build report — 264e58f7` · `264e58f7 feat(worker-watch): Stop hook, idle hook, watch idle exit (S1, N1, W1, I1; L1, L3, L28, L71)` · `a6e8d571 wip(worker-watch): red — S1, N1, W1 tests before the scripts` (5 commits) |
| range paths | `git log --stat --format=%h a09f0862..1bfd26e3` | 0 | 1bfd26e3: `ops/desk/stop-guard.py`; 0a725bed: `tests/ops/test_stop_guard.py`; 80a11302: build report; 264e58f7: `ops/desk/desk-watch.sh`, `ops/desk/idle-wake.py`, `ops/desk/stop-guard.py`, `ops/desk/wait-stop-line.sh`, `tests/ops/test_desk_watch.py`, `tests/ops/test_stop_guard.py`; a6e8d571: `tests/ops/test_desk_watch.py`, `tests/ops/test_idle_wake.py`, `tests/ops/test_stop_guard.py` |
| DB: none — .env | `ls <WT>/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/worker-watch-1003/.env: No such file or directory` |
| other .env | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| DB: none — paths | `git diff --name-only --no-renames a09f0862..1bfd26e3` | 0 | `docs/40 - DevDocs/reports/worker-watch-build-2026-10-03.md` · `ops/desk/desk-watch.sh` · `ops/desk/idle-wake.py` · `ops/desk/stop-guard.py` · `ops/desk/wait-stop-line.sh` · `tests/ops/test_desk_watch.py` · `tests/ops/test_idle_wake.py` · `tests/ops/test_stop_guard.py` — all under ops/, tests/ops/, docs/ |
| scratch | `ls <S>` | 0 | `opus-1.md` (12:37, from the earlier check of this job; NOT opened — an earlier check of this branch is outside WHAT YOU READ). No CONTINUE in the launch: not a RECOVERY. |
| house | — | — | house A: none (overruled 2026-10-02 R47). No house gate run, no probe. HOUSE B: as needed. |

## Files copied
None — house A: none (overruled 2026-10-02 R47); `## 1` not run.

## OWN FINDINGS
Read before any run: the card, the diff `a09f0862..1bfd26e3` (ops, tests), `ops/desk/stop-guard.py`, `idle-wake.py`, `wait-stop-line.sh`, `desk-watch.sh`, `tests/ops/test_stop_guard.py`, `tests/ops/test_desk_watch.py`, the build report's `## RESTARTS`, `## W`, `## FOR THE CHECK` and last line, BUILD-HUB `## THE LOCK` / `## E2` / `## RESTARTS` / `## W` (plus `## UNATTENDED RULES`, `## RECOVERY` and `## STOP LINE` for the card's `## READ`), the stop-line sections of DEVFIX-HUB and DEPLOY-HUB, and cobalt.md's two sections.

FINDING O1
ROW: W1 (X3)
CLAIM: `desk-watch.sh:66` and `wait-stop-line.sh:68` fix the WAKE window (`skip`) once, at the watch's start. A WAKE line written while the listing shows the session `working` (a background run; `wait-stop-line.sh:55` does not fire beside busy) stays in the window. The next single poll that reads the session idle (not working) then fires `IDLE` at once. Without that stale line the watch needs two idle polls (`:56`). So one transient idle reading after a long background run ends the watch: the X3 misfire.
RUN: TEST — `tests/ops/test_desk_watch.py`
```python
def test_w1_a_wake_line_raised_while_working_is_spent_by_the_busy_poll(card, tmp_path):
    """X3 (check O1): a WAKE line beside `working` is a background wait; one idle poll after it
    is not two."""
    card, build, check, env = card
    build.write_text(SEVEN)
    answers(tmp_path, "x-job-build idle working", "x-job-build idle done",
            "x-job-build busy working", "x-job-build busy working")

    def wake():
        time.sleep(0.3)
        append_wake(tmp_path, WAKE_LINE)

    writer = threading.Thread(target=wake)
    writer.start()
    done = watch("build", str(card), "4", env=env)
    writer.join()
    assert done.returncode == 2, done.stdout
    assert done.stdout.startswith("STILL RUNNING after 4s")
```
EXPECT: on the tip, `assert 3 == 2` with stdout `IDLE: x-job-build — 2026-01-02T10:00:00-05:00 x-job IDLE …` (poll 2, one idle poll).

FINDING O2
ROW: W1
CLAIM: `wait-stop-line.sh:66` takes the worktree from the REPORT path only. A check's `CHECK REPORT` and a devfix `REPORT` live under `/Users/cobalt/cobalt/docs/…`, not under a worktree, so `wt` stays `-` and `:47` never reads WAKE. The card's "or a WAKE line → the watch exits 3" is not built for `wait-stop-line.sh` on a check or a devfix, and the script has no way to be told the worktree.
RUN: TEST — `tests/ops/test_desk_watch.py`
```python
def test_w1_wait_stop_line_reads_wake_for_a_report_outside_the_worktrees(tmp_path):
    """Check O2: a check or devfix report lives on main; the worktree is the fifth argument."""
    stage(tmp_path)
    script = tmp_path / "ops" / "wait-stop-line.sh"
    bin_ = tmp_path / "bin"
    bin_.mkdir()
    (bin_ / "sleep").write_text("#!/bin/sh\n/bin/sleep 1\n")
    (bin_ / "sleep").chmod(0o755)
    env = dict(os.environ, PATH=f"{bin_}:{os.environ['PATH']}")
    report = tmp_path / "main" / "docs" / "x-job-check.md"
    report.parent.mkdir(parents=True)
    report.write_text(SEVEN)
    answers(tmp_path, "x-job-check idle blocked")

    def wake():
        time.sleep(0.3)
        append_wake(tmp_path, WAKE_LINE)

    writer = threading.Thread(target=wake)
    writer.start()
    r = subprocess.run(
        ["sh", str(script), str(report), "^(CHECK DONE|FAILED)", "200", "x-job-check", "x-job"],
        env=env, capture_output=True, text=True, timeout=60)
    writer.join()
    assert r.returncode == 3, r.stdout + r.stderr
    assert r.stdout.splitlines() == [f"IDLE: x-job-check — {WAKE_LINE}", *LAST_FIVE]
```
EXPECT: on the tip, the first stdout line is `IDLE: x-job-check — no WAKE line` (two idle polls), not the WAKE line.

THE CHECK ASKS, as read (no finding where none is written):
- X1: the loop guard returns first (`stop-guard.py:119`); the desk and brain cwd returns at `:122`; a worktree seat with no `CARD:` returns at `:128`. Pinned by `test_the_same_prose_with_stop_hook_active_ends_the_turn`, `test_the_desk_and_the_brain_cwd_is_exempt_and_reads_no_report`, `test_s2_…`. Run at `## 4` with the suites.
- X2: a prose last line ends a turn only through the loop guard's second Stop (the card's design) or through a line the card's list accepts, `(run in progress` and `FAILED…` (card S1). A stop line followed by a blank and prose blocks (`:106` keeps the last non-blank line). No finding.
- X3: O1.
- X4: every accepted shape is a hub line: BUILD-HUB:114/116, CHECK-HUB:129–131, DEVFIX-HUB:56–57 (`REBUILT ·`, `FAILED: … · .env`), DEPLOY-HUB:185 (`DEPLOYED <TAG>`, after S2), `FAILED: … · rollback:` under `FAILED`, `(run in progress` (BUILD-HUB:36, CHECK-HUB:57). `RESUMED:` is a running line, not a stop line (BUILD-HUB:32): blocked, as the card lists. No finding.

## Findings
None — house A: none (overruled 2026-10-02 R47).

## Dropped
None.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_watch.py::test_w1_a_wake_line_raised_while_working_is_spent_by_the_busy_poll` (tip `1bfd26e3` + the test) | `1 failed, 15 warnings in 3.13s` · `AssertionError: IDLE: x-job-build — 2026-01-02T10:00:00-05:00 x-job IDLE (run in progress — next step under ## CONTINUE)` … `assert 3 == 2` | HELD — one idle poll after a WAKE line raised during `working` fired IDLE |
| O2 | Opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_watch.py::test_w1_wait_stop_line_reads_wake_for_a_report_outside_the_worktrees` | `1 failed, 15 warnings in 2.19s` · `At index 0 diff: 'IDLE: x-job-check — no WAKE line' != 'IDLE: x-job-check — 2026-01-02T10:00:00-05:00 x-job IDLE (run in progress — next step under ## CONTINUE)'` | HELD — WAKE never read for a report outside the worktrees |

Both tests committed red before any fix: `e296a7cc wip(worker-watch): check red — O1, O2`. Neither test's form was repaired.

## FIXES
| id | fix | files | after | commit |
|---|---|---|---|---|
| O1 | After a poll that reads the session `busy`, the WAKE window moves to the file's current end, so a line raised during a background run is spent. A fresh WAKE line beside a non-busy listing still fires at once (DECISION 2 of the build, KEEP by R69, unchanged). | `ops/desk/desk-watch.sh` (`:83`), `ops/desk/wait-stop-line.sh` (`:86`) | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_watch.py tests/ops/test_stop_guard.py tests/ops/test_idle_wake.py` → `75 passed, 15 warnings in 73.46s (0:01:13)` | `a6bef8cb` |
| O2 | `wait-stop-line.sh` takes an optional fifth argument `[worktree]`; without it the worktree comes from the report path as before. | `ops/desk/wait-stop-line.sh` (`:2`, `:12–20`, `:68–69`) | the same run | `a6bef8cb` |

DevDocs line: no page under `docs/40 - DevDocs/cobalt/` covers the desk scripts (`Grep "wait-stop-line|desk-watch"` there → only the path list in `jobs/restarts.md:42`), and the build wrote none. None written; the header comments of both scripts carry the change.

## Suites
On `<tip now>` = `a6bef8cb`, a DB: none card (BUILD-HUB W (a0), (a), (e) and `tests/ops`):
- RESTARTS: `uv run cobalt jobs restarts a09f0862..HEAD` → `docs/40 - DevDocs/reports/worker-watch-build-2026-10-03.md A DOCS -` · `ops/desk/desk-watch.sh M operator script; no Cobalt reader -` · `ops/desk/idle-wake.py A operator script; no Cobalt reader -` · `ops/desk/stop-guard.py A operator script; no Cobalt reader -` · `ops/desk/wait-stop-line.sh M operator script; no Cobalt reader -` · `tests/ops/test_desk_watch.py M test/documentation; no resident -` · `tests/ops/test_idle_wake.py A test/documentation; no resident -` · `tests/ops/test_stop_guard.py A test/documentation; no resident -` · `RESTARTS: none`. No UNCLASSIFIED row.
- (a0) `git diff --name-only --no-renames a09f0862` → the same eight paths, every one under `docs/`, `ops/` or `tests/ops/` → **`cobalt_dev: not taken (DB: none — 8 paths)`**.
- (a) Offline: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3737 passed, 745 skipped, 1 xfailed, 36 warnings in 638.20s (0:10:38)`, exit 0 → `<p>` = 3737. No test added under `tests/cobalt` or `tests/taxonomy`.
- ops: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` (background) → `532 passed, 1 xfailed, 15 warnings in 260.10s (0:04:20)`, exit 0. That is the build's 530 plus this check's two tests, O1 and O2.
- (e) Live-note: `ls /Users/cobalt/cobalt-wt/worker-watch-1003/.env` → `No such file or directory`, then `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.61s`. The skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, which does not name `COBALT_LIVE_VAULT_ROOT` → `<l>` = 146.
- with-DB: not run (DB: none). `cobalt_dev`: not taken. `.env`: never present (`ls …/.env` → `No such file or directory` at PREFLIGHT, before (e), and at the close, 14:02).

## Scope
PREFLIGHT's union (`a09f0862..1bfd26e3`): the build report, `ops/desk/desk-watch.sh`, `ops/desk/idle-wake.py`, `ops/desk/stop-guard.py`, `ops/desk/wait-stop-line.sh`, `tests/ops/test_desk_watch.py`, `tests/ops/test_idle_wake.py`, `tests/ops/test_stop_guard.py` — every one in a row's `files` (S1, N1, W1, I1, S2) or the build report. My commits: `tests/ops/test_desk_watch.py` (W1's test file), `ops/desk/desk-watch.sh`, `ops/desk/wait-stop-line.sh` (W1's files). Nothing else.

## Checked against the branch
- (i) `git log --oneline 1bfd26e3..HEAD -- . ":(exclude)docs"` → `a6bef8cb fix(worker-watch): a WAKE line raised while busy is spent; wait-stop-line takes the worktree (check O1, O2)` · `e296a7cc wip(worker-watch): check red — O1, O2`. `<tip now>` = `a6bef8cb`.
- (ii) `git log --stat --format=%h 1bfd26e3..HEAD` → `a6bef8cb`: `ops/desk/desk-watch.sh`, `ops/desk/wait-stop-line.sh`; `e296a7cc`: `tests/ops/test_desk_watch.py`; `82db3ade`: the build report (docs). Every non-docs path is in W1's `files`. No WIDENED.
- (iii) fence: `git log --oneline a09f0862..HEAD -- .claude/settings.json ops/desk/job-run.sh` → empty; `git log --oneline a09f0862..HEAD -- "docs/40 - DevDocs/prompts"` → empty (no hub file); `git log --oneline a09f0862..HEAD -- ops/desk/desk-launch.sh ops/desk/bare-guard.py` → empty (no launch-line change, no mod).
- (iv) `grep -n -F "def test_w1_a_wake_line_raised_while_working_is_spent_by_the_busy_poll" tests/ops/test_desk_watch.py` → `329:…`; `grep -n -F "def test_w1_wait_stop_line_reads_wake_for_a_report_outside_the_worktrees" tests/ops/test_desk_watch.py` → `496:…`. `e296a7cc` (red) sits below `a6bef8cb` (fix) in (i).
- (v) see `## Suites` (the `.env` lines) and the close.
- (vi) TREE STATE unchanged: `git log --stat --format=%h a09f0862..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty.
- (vii) the card's `## RECORDS` name no `ls`, `grep` or `git -C /Users/cobalt/cobalt log` command: nothing to run.
- (viii) L32: this report holds no ticker, price or date of his; the test values are constructed (`x-job`, `2026-01-02T10:00:00-05:00`).

## OPEN
none (open: 0).

## CONTINUE
next: none — CHECK DONE (pass 1 at `a6bef8cb`)

## DECISIONS
none

## RECORDS
- house A: none (overruled 2026-10-02 R47; card header `HOUSE A: none — overruled 2026-10-02 R47`). No house launched, nothing staged, no house gate or probe run. `## 1` and `## 3` were not run.
- Dropped findings: none. A house that produced nothing: none (no house).
- REFUSED, not needed: `grep -n -F "[ \"$out\" != busy ]" ops/desk/desk-watch.sh ops/desk/wait-stop-line.sh` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." It was my error: a `$` in a double-quoted argument, against UNATTENDED RULES. Done with the Grep tool.
- REFUSED, not needed: `grep -n -F "wt=${5:--}" ops/desk/wait-stop-line.sh` — the same message, the same cause. Done with the Grep tool.
- `<S>` held `opus-1.md` (12:37), from the earlier check of this job. It was not opened (an earlier check is outside WHAT YOU READ) and not overwritten. This pass's sections are at `<S>/opus-1-r2.md`. House B is not needed, so no house reads it.
- No DevDocs line: no page under `docs/40 - DevDocs/cobalt/` covers the desk scripts (see `## FIXES`).
- Not verified here: whether a real `claude --bg` transcript's first non-`isMeta` user entry is the hub launch message. `stop-guard.py:65–83` and S2 (a) depend on it. If it is not, the hook exits 0 for every worker (silent), not 2. Proving it needs a real session transcript, which is outside this check's read list. His install's first real worker Stop shows it, as the judge ruled for the idle field (card `## RECORDS`, R69).
- No lock taken (DB: none). No `CONTINUE` message arrived.
- L74: the session's system context asked for a `Claude-Session:` commit line. Not acted on; both commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.
- files opened: 22. CHECK-HUB.md; the card; BUILD-HUB.md; cto-2026-09-30.md, cto-2026-10-02.md, cto-2026-10-03.md, cto-2026-09-24.md (grep rows); the build report; `ops/desk/stop-guard.py`, `idle-wake.py`, `wait-stop-line.sh`, `desk-watch.sh`; areas/cobalt.md (the two sections); `tests/ops/test_stop_guard.py`, `tests/ops/test_desk_watch.py`; DEVFIX-HUB.md, DEPLOY-HUB.md, CARD.md, CLOSE-HUB.md (grep and the stop-line or launch lines); `docs/40 - DevDocs/cobalt/jobs/restarts.md` (grep); the two suite output files. Also tried, absent: `ops/desk/desk-list.sh` (not in this tree; it arrives with card `03`).
- Check of `worker-watch`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: worker-watch · pass: 1 · tip: a6bef8cb · house A: none (overruled 2026-10-02 R47) · findings: 2 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3737/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 22 · ready: YES · decisions: 0 · for Dejan: 0
