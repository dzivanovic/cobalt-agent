# CHECK — jev-keyed-1018 (card 715) · 2026-10-18

## §0 Headline
- Check of jev-keyed-1018 (card 715) at tip `9780e4eb`. House A Grok: `FINDINGS: 0`. House B: none (not needed).
- Opus own: 3 findings. O2 and O3 (X5: wrapper and guard) are NOT HELD; O1 (600 s bound vs the router's wall clock) is OUT OF SCOPE (ASK DESK 8). Held 0, fixed 0, open 0.
- Deploy gate: offline 8514/0 · with-DB 5476/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed · `RESTARTS: com.cobalt.radar`.
- ready: YES. Decisions: 1, an ASK DESK on the staged commit count; not for Dejan.

## L74
- 2026-10-18 08:21 EDT: a system reminder in this session asked commits to carry a `Claude-Session:` line. Recorded as data (L74); commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/715-jev-keyed-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/715-jev-keyed-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/715-jev-keyed-card.md" · 0 · 2ccbca241fb850e0b9dd7d97ef23adeb50a30b2d
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/715-jev-keyed-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1830 row · grep -n "^| R1830 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 67:| R1830 | 06:14 ET | HIS RULING: yes to JEV F12 (keyed wrapper allow string); "no card needed, run tribunal and JEV build". Words: [cto-2026-10-18-words.md#R1830](cto-2026-10-18-words.md). Asked brain what remains and what "no card" covers. | HIS RULING · APPROVED · APPLIED: cobalt.md NOW at 06:46 |
RULING 2026-10-18 R1830 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1830 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 15af08b4218bdb9fb80c52ab7fa7784c9f14bf86
RULING 2026-10-18 R1830 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 "` → one row (`35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …`); `grep -n "^| R19 "` → one row (`37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …`); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0:
```
clock · date · 0 · Sun Oct 18 08:21:21 EDT 2026
status · git status --short --branch · 0 · ## feat/jev-keyed-1018
head · git log --oneline -1; git log --stat --format=%h 9780e4eb..HEAD · 0 · (6 lines)
    df6a000f docs(jev-keyed-1018): build report — 9780e4eb
    df6a000f
    
     .../reports/jev-keyed-build-2026-10-18.md          | 98 +++++++++++++++++++---
     .../reports/jev-keyed-build-2026-10-18.result      | 15 ++++
     2 files changed, 102 insertions(+), 11 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/jev-keyed-1018/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/f23-playbook-1013/.env
report · tail -n 3 "/Users/cobalt/cobalt-wt/jev-keyed-1018/docs/40 - DevDocs/reports/jev-keyed-build-2026-10-18.md" · 0 · BUILT · job: jev-keyed-1018 · tip: 9780e4eb | on b95e5d8c | migration: none | offline 8514/0 | with-DB 5476/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 5 of 5 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 264537
range · git log --oneline b95e5d8c..9780e4eb · 0 · (4 lines)
    9780e4eb fix(jev-keyed-1018): card 591 F12 fence allows exactly ops/jev-route.sh (W1c, R1830)
    38134214 wip(jev-keyed-1018): W — offline red outside the rows (card 591 F12 fence test)
    5071698a feat(jev-keyed-1018): JEV keyed wrapper, close step 7b, its one allow string (W1-W3, L41, L42, R1830)
    bc55ef6e wip(jev-keyed-1018): red — W1-W3 tests on BASE
PREFLIGHT OK
```
- The lock: another worktree (`f23-playbook-1013`) holds `.env`; this check waits for the lock at its with-DB step (L76).
- THE RANGE typed: `git log --stat --format=%h b95e5d8c..9780e4eb` → path union: `tests/cobalt/test_jev_shadow_1015.py`, `docs/40 - DevDocs/reports/jev-keyed-build-2026-10-18.md`, `docs/40 - DevDocs/cobalt/jobs/restarts.md`, `docs/40 - DevDocs/prompts/CLOSE-HUB.md`, `ops/jev-route.sh`, `src/cobalt/jobs/restarts.py`, `tests/cobalt/test_jobs_restarts.py`, `tests/ops/test_jev_route_1018.py`, `tests/ops/test_needs_his_hand.py`. Commits: 4.
- The card carries no `DB: none` line: no DB-none diff check.
- `ls <S>` → `No such file or directory` (fresh).
- House probe: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0 → `grok: UP` · `gemini: UP` (no `HOUSE A: OpenAI` header: Sol not probed).
- Seats: `house A: Grok · house B: none (not needed)` — the card's `HOUSE B: as needed`.
- Proven by first real use: `Bash(sh /Users/cobalt/cobalt/ops/desk/*)` at AUTHORIZATION (allowed); the rest at their first use below.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` (`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/jev-keyed-1018-check`):
```
22 <S>/STAGED-CARD
19219 <S>/diff.md
27977 <S>/files/715-jev-keyed-card.md
32684 <S>/files/jev-keyed-build-2026-10-18.md
5185 <S>/files/wt/docs/40 - DevDocs/cobalt/jobs/restarts.md
16394 <S>/files/wt/docs/40 - DevDocs/prompts/CLOSE-HUB.md
21972 <S>/files/wt/docs/40 - DevDocs/reports/jev-keyed-build-2026-10-18.md
1115 <S>/files/wt/ops/jev-route.sh
12118 <S>/files/wt/src/cobalt/jobs/restarts.py
43188 <S>/files/wt/tests/cobalt/test_jev_shadow_1015.py
30295 <S>/files/wt/tests/cobalt/test_jobs_restarts.py
12834 <S>/files/wt/tests/ops/test_jev_route_1018.py
3539 <S>/files/wt/tests/ops/test_needs_his_hand.py
394 <S>/rulings.md
STAGED 14 files · 226936 bytes · commits 3
```
`commits 3` against PREFLIGHT's 4: the diff excludes `docs` (`git log -p <BASE>..<TIP> -- . ":(exclude)docs"`), and `38134214` touches only the build report. `git log --oneline b95e5d8c..9780e4eb -- . ":(exclude)docs"` → 3 lines (`9780e4eb`, `5071698a`, `bc55ef6e`). The diff is whole (ASK DESK 1, `## DECISIONS`).
`stage-copy.sh`, each → `COPIED <bytes> <dest>`: `jev-f12-answer-2026-10-18.md` 5438 · `jev-design-decisions-2026-10-14.md` 4055 · `jev-tribunal-fold-answer-2026-10-15.md` 5165 · `jev-shadow-design-2026-10-14.md` 23357 · `wt/src/cobalt/classify/route.py` 35917 · `wt/configs/cobalt/classify/route.yaml` 4391 · `wt/tests/ops/test_hub_lines.py` 13611 · `wt/ops/desk/bare-guard.py` 56882 · `wt/tests/ops/test_bare_guard.py` 103195 · `wt/ops/run_backup.sh` 1467.
`files/f4e8de85-run_classify_trial.sh`: Written from `git show f4e8de85:ops/run_classify_trial.sh` (a git object, no file for `stage-copy.sh`). `test_classify_door.py@f4e8de85` was not staged (a git object of 1 test the card cites; its carried assertions are quoted in the card's `## RECORDS`).
`<S>/HOUSE-INSTRUCTIONS.md`: the HOUSE TEXT verbatim, then the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS` whole, then the `Files:` paragraph.
Launch 08:24 EDT (`date`), gates again (R17 1 row, R19 1 row, the R19 commit `5055151d…`), `ls -la <S>` listed, `cd <AGY>`, the Grok line (`run_in_background`, `timeout` 2700000), `cd <WT>`, `git status --short --branch` → `## feat/jev-keyed-1018`.

## OWN FINDINGS
Written 2026-10-18 before any house list was opened (no house completion notice had arrived).

FINDING O1
ROW: W2 (X4)
CLAIM: STEP 7b bounds each day's call at Bash `timeout` 600000 (`docs/40 - DevDocs/prompts/CLOSE-HUB.md:59`), while the router's own batch stop is `batch_wall_clock_s` of more than 600 s (`configs/cobalt/classify/route.yaml:28`, `src/cobalt/classify/route.py:495-496`): a batch long enough is killed by the tool before the router writes its `timeout` rows, so the cards left get no `status` row at all.
RUN: COMMAND `grep -n -F "batch_wall_clock_s:" configs/cobalt/classify/route.yaml`
EXPECT: `28:  batch_wall_clock_s: <value>` with `<value>` above 600.

FINDING O2
ROW: W1 (X5)
CLAIM: `test_w1_any_other_argument_is_refused` (`tests/ops/test_jev_route_1018.py:180-196`) pins no second date as its own word and no newline inside the date word, the two shapes X5 asks about; a probe that the wrapper's `case` (`ops/jev-route.sh:14-17`) refuses both.
RUN: TEST `tests/ops/test_jev_route_1018.py`
```python
@pytest.mark.parametrize("args", [
    ["--day", "2026-01-02", "2026-01-03"],
    ["--day", "2026-01-02\n2026-01-03"],
    ["--day", "2026-01-02 2026-01-03"],
])
def test_check_o2_a_second_date_is_refused(box, args):
    done = box["run"](*args)
    assert done.returncode == 64, (done.returncode, done.stderr)
    assert not box["out"].exists()
    assert not box["sourced"].exists()
```
EXPECT: red (`assert 0 == 64` or the stub's output present) if a second date reaches `uv`; green answers X5 for the wrapper.

FINDING O3
ROW: W2 / W3 (X5)
CLAIM: the close seat is kind `None` (`ops/desk/bare-guard.py:1106` skips G2 for it); a probe that G1 (`bare-guard.py:1130-1132`) still refuses a compound command that starts with the W3-admitted call, so the `--day *` glob cannot carry a second command.
RUN: TEST `tests/ops/test_jev_route_1018.py`
```python
def test_check_o3_the_guard_refuses_a_compound_after_the_close_call(tmp_path):
    wt = tmp_path / "wt"
    repo = tmp_path / "repo"
    wt.mkdir()
    repo.mkdir()
    first = ("Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CLOSE-HUB.md' and follow it exactly. "
             "DATE: 2026-01-02")
    transcript = tmp_path / "t-close.jsonl"
    records = [
        {"type": "queue-operation", "operation": "enqueue", "sessionId": "sess-test-1"},
        {"parentUuid": None, "isSidechain": False, "userType": "external", "cwd": "/constructed",
         "sessionId": "sess-test-1", "type": "user", "message": {"role": "user", "content": first},
         "uuid": "00000000-0000-0000-0000-000000000001", "timestamp": "2026-01-01T13:00:00.000Z"},
    ]
    transcript.write_text("".join(json.dumps(r) + "\n" for r in records))
    for command in ("sh /Users/cobalt/cobalt/ops/jev-route.sh --day 2026-01-02; ls",
                    "sh /Users/cobalt/cobalt/ops/jev-route.sh --day 2026-01-02 && ls",
                    "sh /Users/cobalt/cobalt/ops/jev-route.sh --day $(ls)"):
        event = {
            "session_id": "sess-test-1",
            "transcript_path": str(transcript),
            "cwd": str(repo),
            "permission_mode": "dontAsk",
            "hook_event_name": "PreToolUse",
            "tool_name": "Bash",
            "tool_input": {"command": command, "description": "x"},
        }
        env = dict(os.environ, COBALT_WT_ROOT=str(wt), COBALT_REPO_ROOT=str(repo))
        done = subprocess.run(["python3", str(GUARD)], input=json.dumps(event), env=env,
                              capture_output=True, text=True, timeout=60)
        assert done.returncode != 0, command
```
EXPECT: red (`assert 0 != 0`, the command named) if the guard admits a compound in the close seat; green answers X5 for the guard.

## Findings
House A Grok finished 08:39 EDT (`date` at the notice). `ls -la <S>` → `house-a.md` 12 bytes, written by Grok. Its whole text: `FINDINGS: 0`. Stdout: progress lines, then the path `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/jev-keyed-1018-check/house-a.md`, `[exited with code 0]`. House B: none (not needed).
Kept: none from the house (it wrote no `FINDING` block).

## Dropped
none (house A wrote no block; no house B).

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus-own | `grep -n -F "batch_wall_clock_s:" configs/cobalt/classify/route.yaml` | `28:  batch_wall_clock_s: 1470` (STEP 7b's bound is `timeout` 600000 ms = 600 s, `CLOSE-HUB.md:59`) | REJECTED — `## NOT IN THIS JOB`: "`src/cobalt/classify/` and `configs/cobalt/classify/` (card 591's): … `batch_wall_clock_s` (ASK DESK 8)". The output shows the claim; the card puts the number outside this job → OUT OF SCOPE (COUNTING) |
| O2 | opus-own | TEST `tests/ops/test_jev_route_1018.py::test_check_o2_a_second_date_is_refused` (3 params), run with O3: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_jev_route_1018.py -k "check_o2 or check_o3"` | `4 passed, 21 deselected, 15 warnings in 1.53s` | NOT HELD (green: a second date, as its own word, after a newline or after a space, exits 64, never sources the key and makes no `uv` call); removed again by Edit |
| O3 | opus-own | TEST `tests/ops/test_jev_route_1018.py::test_check_o3_the_guard_refuses_a_compound_after_the_close_call`, the same run | as O2 (the one O3 test passed) | NOT HELD (green: the guard refuses `; ls`, `&& ls` and `$(ls)` after the close call in the kind-`None` close seat); removed again by Edit |
After the removals: `git status --short --branch` → `## feat/jev-keyed-1018` (the tree back at the tip). No HELD finding: no `wip(jev-keyed-1018): check red` commit.

## FIXES
none (nothing held).

## Suites
RESTARTS first: `uv run cobalt jobs restarts b95e5d8c..HEAD` →
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/jobs/restarts.md	M	DOCS	-
docs/40 - DevDocs/prompts/CLOSE-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/jev-keyed-build-2026-10-18.md	A	DOCS	-
docs/40 - DevDocs/reports/jev-keyed-build-2026-10-18.result	A	DOCS	-
ops/jev-route.sh	A	operator script; no Cobalt reader	-
src/cobalt/jobs/restarts.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_jev_shadow_1015.py	M	test/documentation; no resident	-
tests/cobalt/test_jobs_restarts.py	M	test/documentation; no resident	-
tests/ops/test_jev_route_1018.py	A	test/documentation; no resident	-
tests/ops/test_needs_his_hand.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
No `UNCLASSIFIED` row, no `ESCALATE`.
`ls -la <WT>/.env` → `No such file or directory` (outside a lock take). Then, on tip `9780e4eb` (no commit of mine): `sh /Users/cobalt/cobalt/ops/desk/gate.sh jev-keyed-1018 all --deploy --deploy-gate` (`run_in_background`) → exit 0, the verdict lines whole:
```
tests/ops: run (deploy gate)
offline 8514/0
lock: waited 28 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5476/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/jev-keyed-1018-all-20261018-084015.log
```
The gate printed no skip marked `OUTSIDE the allowed set`. The seven SKIPPED lines are the same set the build's gate printed. `ls /Users/cobalt/cobalt-wt/jev-keyed-1018/.env` → `No such file or directory` (09:58 EDT); `git status --short --branch` → `## feat/jev-keyed-1018`.
- offline `8514/0` · with-DB `5476/0` · live-note `146/0` · `cobalt_dev: 0013 — F2 = F0` · `.env: removed`, proven gone · `RESTARTS: com.cobalt.radar`.

## Scope
PREFLIGHT's path union: `ops/jev-route.sh` (W1), `src/cobalt/jobs/restarts.py` (W1 b, `OPS_TOOLS` only, a one-line diff), `tests/ops/test_jev_route_1018.py` (W1-W3), `tests/cobalt/test_jobs_restarts.py` (W1 b, one appended test), `tests/cobalt/test_jev_shadow_1015.py` (W1c, the one assert and its comment), `tests/ops/test_needs_his_hand.py` (W2, `:25` and `:89` only), `docs/40 - DevDocs/prompts/CLOSE-HUB.md` (W2 a, W2 b, W3 `:10`, W3 `:12`: four hunks), `docs/40 - DevDocs/cobalt/jobs/restarts.md` (W1, one dated section), the build report (docs). Every path is in some row's `files`. My commits: none.
CHECK ASKS, from the reads and runs above:
- X1: the wrapper (`ops/jev-route.sh:12-17`) refuses before `:19-24`. It has no output command. Its one `export` is `COBALT_VAULT_FILE`. The key reaches only the exec'd `uv` (W1 (1)/(2) green in the build; O2 green here). Only `--day <YYYY-MM-DD>` reaches `uv` (O2).
- X2: every wrapper run in `tests/ops/test_jev_route_1018.py` uses the `box` fixture (`:123-146`): tmp `HOME`, decoy key, stub `uv`, `PATH=<tmp>/bin:/usr/bin:/bin`. The guard control uses a tmp transcript. No test names the real key file. The wrapper's `cd /Users/cobalt/cobalt` is a cwd change; the run writes nothing there.
- X3: `git diff b95e5d8c..9780e4eb -- CLOSE-HUB.md`: `:10` gains one string, `"Bash(sh /Users/cobalt/cobalt/ops/jev-route.sh --day *)"`, after `"Bash(git push origin main)"`, and nothing else on the line changes. No other fixed prompt changed: `git diff --stat b95e5d8c..HEAD -- "docs/40 - DevDocs/prompts" ":(exclude)…CLOSE-HUB.md"` → nothing. `.claude/settings.json`, `ops/desk/desk-launch.sh` and `ops/desk/bare-guard.py` have no commit in the range.
- X4: one call per day, bounded at 600 s. Every failure is one line, never retried, and the stop line is untouched (W2 (1), (3)). The 600 s bound sits below the router's own wall clock (O1, OUT OF SCOPE).
- X5: O2 (the wrapper) and O3 (the guard's G1 in the close seat) are green.
- X6: `ops/jev-route.sh` → `operator script; no Cobalt reader`. `RESTARTS: com.cobalt.radar` is derived (`## Suites`); there is no `ESCALATE` and no `UNCLASSIFIED` row.

## Checked against the branch
- (i) `git log --oneline 9780e4eb..HEAD -- . ":(exclude)docs"` → nothing: no commit of mine; `<tip now>` = `9780e4eb`.
- (ii) `git log --stat --format=%h 9780e4eb..HEAD` → `df6a000f`, only `docs/40 - DevDocs/reports/jev-keyed-build-2026-10-18.md` and `.result` (docs).
- (iii) `git log --oneline b95e5d8c..HEAD -- src/cobalt/classify configs/cobalt/classify tests/ops/test_hub_lines.py ops/desk/desk-launch.sh ops/desk/bare-guard.py ops/run_classify_trial.sh .claude/settings.json` → EMPTY. `git diff --stat b95e5d8c..HEAD -- tests/cobalt/test_classify_door.py tests/cobalt/test_classify_route.py` → nothing. Fixed prompts but CLOSE-HUB → nothing (X3).
- (iv) no HELD finding.
- (v) see `## Suites` (after W).
- (vi) `git log --stat --format=%h b95e5d8c..HEAD -- src/cobalt/db_migrations tests/cobalt` → `9780e4eb` `tests/cobalt/test_jev_shadow_1015.py`, `bc55ef6e` `tests/cobalt/test_jobs_restarts.py`: no migration and no with-DB test file. No gate-lists change is owed.
- (vii) card `## RECORDS`: `ls /Users/cobalt/cobalt/ops/jev-route.sh /Users/cobalt/cobalt/tests/ops/test_jev_route_1018.py` → `No such file or directory` each (main, not deployed); `grep -c -F "claude --bg"` of main's CLOSE-HUB → `1`; `wc -l` → main `66`, the tip `69`; the tip's `grep -n -F "claude --bg"` → one hit, `10:`.
- (viii) L32: this report holds no ticker, price or date of his. The dates are this check's own and the card's constructed `2026-01-02`.

## OPEN
none open. OUT OF SCOPE: O1 (STEP 7b's 600 s Bash bound vs `batch_wall_clock_s` above 600 s). It is fenced by `## NOT IN THIS JOB` (ASK DESK 8). It would be settled by a card on card 591's config, or by a STEP 7b batch shorter than 600 s.

## CONTINUE
next: none — CHECK DONE

## DECISIONS
- ASK DESK 1: does `stage-set.sh`'s `commits 3` meet `## 1` (5)'s "`<k>` = PREFLIGHT's commit count" (4), when the fourth commit, `38134214`, touches only `docs/` and the diff excludes `docs` by its own command? `git log --oneline b95e5d8c..9780e4eb -- . ":(exclude)docs"` → 3 lines. [08:21 EDT] Default taken: the copy is whole and the check went on. Failing would have stopped a complete diff on a count the excluded path explains. Nothing in it gives more access. Not for Dejan.

## RECORDS
- Dropped findings: none.
- Houses that produced nothing: none. Grok wrote `FINDINGS: 0` (a valid list). House B: none (not needed, `HOUSE B: as needed`).
- REFUSED, not needed: none. CONTINUED: none.
- Lock: one take, by `gate.sh` (`lock: waited 28 min`; another job held it at the start, `f23-playbook-1013`'s `.env` at PREFLIGHT).
- L74: one line under `## L74` (a system reminder, not a tool result: recorded as data, not followed).
- O1 OUT OF SCOPE, kept for the follow-up list: STEP 7b's Bash bound (600 s) is below `batch_wall_clock_s` (`route.yaml:28`). If a day's batch passes 600 s, the tool kills the process before `run_batch` (`route.py:495-496`) writes its `timeout` rows. The card fences the number (ASK DESK 8).
- The O2 and O3 probe tests were removed after their green runs. The tree is at the tip.
- files opened: 16 — `CHECK-HUB.md`, the card `715-jev-keyed-card.md`, `BUILD-HUB.md` (`## THE LOCK` to `## W`), `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down), `ops/jev-route.sh`, `tests/ops/test_jev_route_1018.py`, `ops/run_backup.sh`, `src/cobalt/classify/route.py` (`:480-579`, `:750-819`), `configs/cobalt/classify/route.yaml`, `ops/desk/bare-guard.py` (`:1080-1149`), the build report (`:122-256`), `<S>/rulings.md`, `<S>/house-a.md`, the probe output, Grok's stdout, the gate output. Read by grep or git only: the diff `b95e5d8c..9780e4eb`, CLOSE-HUB.md at the tip and on main.
- Check of `jev-keyed-1018`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: jev-keyed-1018 · pass: 1 · tip: 9780e4eb · house A: Grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8514/0 · with-DB 5476/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 16 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 178753
