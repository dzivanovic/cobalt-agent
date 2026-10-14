# Check report — db-copy-1014 (card 547)

## §0 Headline
Check of db-copy-1014 (card 547) on `0e136e4f`. House A was Grok (`FINDINGS: 1`); house B was not needed, and Gemini was OUT. There were 4 findings, 3 of them held.
Fixed: O1. A signal while the copy's create runs no longer leaves the copy behind (`a157d731`, red first in `1b4c388d`).
Held, not fixed: O2 and A1, one defect. Once the code card adds the sections, the deploy gate's own `all --deploy` call runs in copy mode. The fix sits behind the fence → `## DECISIONS`.
O3 (two worktree names sharing one copy name) is REJECTED by card step 1 and stays open. Suites: offline 4328/0, live-note 146/0, `tests/ops` 3643/0; DB: none. ready: NO (held unfixed 2).

## L74
One system note in this session asked that commits end with a `Claude-Session:` line. It is recorded here once and was not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/547-db-copy-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/547-db-copy-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-14/547-db-copy-card.md" · 0 · c8eb1ea213623975e53a502c6c82dc3c1a974e4c
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-14/547-db-copy-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-14 R1471 row · grep -n "^| R1471 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 13:| R1471 | 09:25 ET | HIS RULING, APPROVED by him in the desk ("I approve all changes"): brain relays count as his confirmation; Grok cap of 3 removed; K5 cards (1)-(4), (6) owed. Words: `cto-2026-10-14-words.md`. | APPLIED: LAWS L79, checklist L15 at 09:40 |
RULING 2026-10-14 R1471 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1471 |" -- "docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 8b813ca721cd934ebfb82cc59d27495d15f1c79a
RULING 2026-10-14 R1471 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · the row as grepped
AUTHORIZED
```
House gates:
- `grep -n "^| R17 " ".../cto-2026-09-24.md"` → exit 0, one row (`35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …`).
- `grep -n "^| R19 " ".../cto-2026-09-24.md"` → exit 0, one row (`37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …`).
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c`.

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` → exit 0, output whole:
```
clock · date · 0 · Wed Oct 14 17:18:07 EDT 2026
status · git status --short --branch · 0 · ## ops/db-copy-1014
head · git log --oneline -1; git log --stat --format=%h 0e136e4f..HEAD · 0 · (5 lines)
    d70e1647 docs(db-copy-1014): build report — 0e136e4f
    d70e1647
    
     .../reports/db-copy-build-2026-10-14.md            | 206 +++++++++++++++++++++
     1 file changed, 206 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/db-copy-1014/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/db-copy-1014/docs/40 - DevDocs/reports/db-copy-build-2026-10-14.md" · 0 · BUILT · job: db-copy-1014 · tip: 0e136e4f | on 0a151491 | migration: none | offline 4328/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 6 of 6 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 219435
range · git log --oneline 0a151491..0e136e4f · 0 · (2 lines)
    0e136e4f feat(db-copy-1014): gate copy mode, devdb-copy-env.sh, launcher skips a marked copy, lists and hub lines (E1 G1 L1 D1 H1, L76 L81)
    8152c66e wip(db-copy-1014): red — card 547 tests (E1, G1, L1, D1, H1)
PREFLIGHT OK
```
| rule | command | exit | output |
|---|---|---|---|
| THE RANGE | `git log --stat --format=%h 0a151491..0e136e4f` | 0 | `0e136e4f`: `BUILD-HUB.md` 2 +-, `ops/desk/desk-launch.sh` 2 +, `ops/desk/devdb-copy-env.sh` 75 +, `ops/desk/gate-lists.md` 6 +, `ops/desk/gate.sh` 174 +/-, `tests/ops/test_build_hub_no_clutter.py` 5 + (6 files, 256 insertions, 8 deletions) · `8152c66e`: `tests/ops/test_db_copy_1014.py` 625 + |
| DB: none | `git diff --name-only --no-renames 0a151491..0e136e4f` | 0 | `docs/40 - DevDocs/prompts/BUILD-HUB.md` · `ops/desk/desk-launch.sh` · `ops/desk/devdb-copy-env.sh` · `ops/desk/gate-lists.md` · `ops/desk/gate.sh` · `tests/ops/test_build_hub_no_clutter.py` · `tests/ops/test_db_copy_1014.py` — every path under `ops/`, `tests/ops/` or `docs/` |
| scratch | `ls /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/db-copy-1014-check` | 1 | `No such file or directory` (fresh) |
| HOUSE PROBES | `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` | 0 | `grok: UP` · `gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` |
| SEATS | SEAT ORDER, no `HOUSE A` header line | — | house A: Grok · house B: none (not needed — `HOUSE B: as needed`) |

Path union for `## Scope`: the seven paths above.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → exit 0, output whole:
```
43566 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/db-copy-1014-check/diff.md
37219 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/db-copy-1014-check/files/547-db-copy-card.md
20445 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/db-copy-1014-check/files/db-copy-build-2026-10-14.md
34042 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/db-copy-1014-check/files/wt/docs/40 - DevDocs/prompts/BUILD-HUB.md
127909 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/db-copy-1014-check/files/wt/ops/desk/desk-launch.sh
3033 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/db-copy-1014-check/files/wt/ops/desk/devdb-copy-env.sh
7138 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/db-copy-1014-check/files/wt/ops/desk/gate-lists.md
26266 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/db-copy-1014-check/files/wt/ops/desk/gate.sh
3195 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/db-copy-1014-check/files/wt/tests/ops/test_build_hub_no_clutter.py
24965 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/db-copy-1014-check/files/wt/tests/ops/test_db_copy_1014.py
350 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/db-copy-1014-check/rulings.md
STAGED 11 files · 328128 bytes · commits 2
```
`<k>` = 2 = PREFLIGHT's commit count. Then `stage-copy.sh`, one call each:
- `COPIED 16230 …/files/survey-blockers-2026-10-12.md`
- `COPIED 31524 …/files/cto-2026-10-14.md`
- `COPIED 1439 …/files/cto-2026-10-14-words.md`
- `COPIED 27102 …/files/521-gate-tests-ops-card.md`
- `COPIED 19627 …/files/523-hub-text-card.md`
- `COPIED 16434 …/files/537-deploy-smoke-string-card.md`
- `COPIED 2572 …/files/wt/ops/desk/take-devdb-lock.sh`
- `COPIED 2561 …/files/wt/ops/desk/release-devdb-lock.sh`
- `COPIED 13188 …/files/wt/tests/ops/test_devdb_lock.py`
- `COPIED 33735 …/files/wt/tests/ops/test_gate.py`
- `COPIED 13611 …/files/wt/tests/ops/test_hub_lines.py`
- `COPIED 3825 …/files/wt/src/cobalt/env.py`
- `COPIED 7905 …/files/wt/src/cobalt/devdb.py`

Not copied: LAWS.md (the card carries the laws). `HOUSE-INSTRUCTIONS.md` = the HOUSE TEXT verbatim, plus the card's `## ROWS` (prose and table), `## NOT IN THIS JOB`, `## CHECK ASKS` and `## RECORDS` copied whole, plus the `Files:` paragraph. House A, Grok, was started at 17:21 (`date` → `Wed Oct 14 17:21:24 EDT 2026`): `grok -m grok-4.7 --sandbox cobalt-job --allow "Write(…/scratch/tribunal-bars-0920/**)" -p "…"`, as `## 1` (5) spells it, `run_in_background`, `timeout` 2700000. Before it: the gates R17 and R19 again (one row each), and `ls -la <S>`. After it: `cd <WT>` and `git status --short --branch` → `## ops/db-copy-1014`. No house B was started.

## OWN FINDINGS
Written at 17:24 (`date`), before any house list was opened.

FINDING O1
ROW: G1 (step 5, (g)); X2
CLAIM: `ops/desk/gate.sh:390-395` `copy_create` sets `made=1` only AFTER the create command returns. A TERM, INT or HUP that lands while `## COPY CREATE` runs is handled by sh after that command returns, before `made=1` (the traps `:506-508` exit straight away). So when the create itself succeeded, `cleanup` (`:491`) sees `made` empty and never drops the copy: the copy outlives the run.
RUN: TEST `tests/ops/test_db_copy_1014.py`
```python
def test_g1_check_o1_a_signal_while_the_create_runs_still_drops_the_copy(tree):
    """CHECK O1 (X2, G1 step 5): a TERM that lands while `## COPY CREATE` runs, the create itself
    done, must not leave the copy behind: the trap drops it before the lock release."""
    tree.worktree(NAME, copy_lists())
    pidfile = tree.tmp / "gate-pid"
    real = tree.bin / "uv-real"
    (tree.bin / "uv").rename(real)
    (tree.bin / "uv").write_text(
        "#!/bin/sh\n"
        f'"{real}" "$@"\n'
        "rc=$?\n"
        'case " $* " in *" dev-copy create "*)\n'
        f'    while [ ! -s "{pidfile}" ]; do :; done\n'
        f'    kill -TERM "$(cat "{pidfile}")" ;;\n'
        "esac\n"
        'exit "$rc"\n'
    )
    (tree.bin / "uv").chmod(0o755)
    first = tree.popen(NAME, tree.env("a"))
    pidfile.write_text(str(first.pid))
    out, err = first.communicate(timeout=300)
    assert first.returncode == 143, out + err
    kinds = [kind(c) for c in tree.calls("a")]
    assert kinds[-1] == f"dev-copy drop {COPY}", kinds
    assert kinds.count(f"dev-copy drop {COPY}") == 2, kinds
    assert_nothing_left(tree)
```
EXPECT: `assert 'dev-copy create cobalt_dev_x_job' == 'dev-copy drop cobalt_dev_x_job'` (the log ends at the create).

FINDING O2
ROW: G1 (COPY MODE step 6; the header paragraph `ops/desk/gate.sh:54-55`)
CLAIM: Step 6 and `ops/desk/gate.sh:54-55` say a deploy gate still holds the lock whole. But copy mode is chosen only by the lists file (`:216-250`, `:661-663`), and the deploy gate runs `gate.sh <WORKTREE> all --deploy` on the merged `main` lists file (`DEPLOY-HUB.md:99`, `:102`). So once the code card adds the two sections, the deploy gate runs on a copy with the lock given back.
RUN: TEST `tests/ops/test_db_copy_1014.py`
```python
def test_g1_check_o2_the_deploy_gate_call_holds_the_lock_whole_with_the_sections(tree):
    """CHECK O2 (G1 step 6): the deploy gate's own call, `all --deploy` on a lists file that holds
    both sections, still runs on cobalt_dev under the lock."""
    tree.worktree(NAME, copy_lists())
    env = tree.env("a")
    done = subprocess.run(
        ["sh", str(tree.desk / "gate.sh"), NAME, "withdb", "--deploy"], env=env,
        capture_output=True, text=True, timeout=300,
    )
    assert done.returncode == 0, done.stdout + done.stderr
    log = tree.calls("a")
    assert not any(dev_copy(c) for c in log), [kind(c) for c in log]
    assert all(c["lock"] for c in log), log
```
EXPECT: `AssertionError: ['fp', 'proof', 'dev-copy drop cobalt_dev_x_job', 'dev-copy create cobalt_dev_x_job', …]` (copy mode under `--deploy`).

FINDING O3
ROW: G1 (COPY MODE step 1: "two worktrees must never share a name"); X3
CLAIM: `ops/desk/gate.sh:380` maps the worktree name to `cobalt_dev_` + lower-case with `[^a-z0-9]` → `_`, so `x-job`, `x_job` and `X-JOB` (all valid at `:96-98`) share `cobalt_dev_x_job`. One worktree's step-2 leftover drop (`:391`) can then drop another worktree's live copy.
RUN: TEST `tests/ops/test_db_copy_1014.py`
```python
def test_g1_check_o3_two_worktrees_never_share_a_copy_name(tree):
    """CHECK O3 (G1 step 1): two worktrees must never share a copy name."""
    tree.worktree(NAME, copy_lists())
    tree.worktree("x_job", copy_lists())
    a = tree.gate(NAME, tree.env("a"))
    b = tree.gate("x_job", tree.env("b"))
    assert a.returncode == 0, a.stdout + a.stderr
    assert b.returncode == 0, b.stdout + b.stderr
    made_a = [k for k in map(kind, tree.calls("a")) if k.startswith("dev-copy create")]
    made_b = [k for k in map(kind, tree.calls("b")) if k.startswith("dev-copy create")]
    assert made_a != made_b, (made_a, made_b)
```
EXPECT: `AssertionError: (['dev-copy create cobalt_dev_x_job'], ['dev-copy create cobalt_dev_x_job'])`.

FINDINGS: 3 (own)

## Findings
House A, Grok, finished at 17:42 (`date` → `Wed Oct 14 17:42:28 EDT 2026`). It wrote `<S>/house-a.md` itself (1333 bytes) and replied with only that path. The list's last line is `FINDINGS: 1`. House B: none (not needed).

| id | house | row | claim (≤30 words) | run |
|---|---|---|---|---|
| A1 | Grok | G1 | Step 6 is not built for `--deploy`: with both sections, `withdb --deploy` creates the copy and gives back the lock before the suite; `gate.sh:55` says the opposite; no test calls `--deploy`. | TEST `test_g1_deploy_stays_on_cobalt_dev_under_the_lock` |
| O1 | Opus | G1, X2 | A signal while the create runs is handled before `made=1`, so the trap never drops a copy that was made. | TEST |
| O2 | Opus | G1 step 6 | The deploy gate's call (`all --deploy`, on `main`'s lists file) runs in copy mode once the sections exist. | TEST |
| O3 | Opus | G1 step 1, X3 | `x-job` and `x_job` map to one copy name, `cobalt_dev_x_job`. | TEST |

A1 and O2 are the same defect, found apart.

## Dropped
none. A1's block has a `RUN:` line followed by `def test_`.

## RUNS
Each test was put in `tests/ops/test_db_copy_1014.py` with the Edit tool and run alone: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_db_copy_1014.py::<test>`. No test's form needed a repair.

| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `::test_g1_check_o1_a_signal_while_the_create_runs_still_drops_the_copy` | `1 failed` · `AssertionError: ['fp', 'proof', 'dev-copy drop cobalt_dev_x_job', 'dev-copy create cobalt_dev_x_job']` / `assert 'dev-copy cre...alt_dev_x_job' == 'dev-copy dro...alt_dev_x_job'` (exit 143 held; the log ends at the create) | HELD |
| O2 | Opus | `::test_g1_check_o2_the_deploy_gate_call_holds_the_lock_whole_with_the_sections` | `1 failed` · `AssertionError: ['fp', 'proof', 'dev-copy drop cobalt_dev_x_job', 'dev-copy create cobalt_dev_x_job', 'fp', 'proof', ...]` / `assert not True` | HELD, NOT FIXED — `ops/desk/gate.sh` option loop `:86-112` (fenced, card 521) or a DEPLOY-HUB line (fenced): `gate.sh` has no signal that tells the deploy gate from a build. Both call `all --deploy` (his R438; `BUILD-HUB.md:81`, `DEPLOY-HUB.md:102`), and card G1 says no option is added. |
| O3 | Opus | `::test_g1_check_o3_two_worktrees_never_share_a_copy_name` | `1 failed` · `AssertionError: (['dev-copy create cobalt_dev_x_job'], ['dev-copy create cobalt_dev_x_job'])` | REJECTED — card COPY MODE step 1: "`cobalt_dev_` + the worktree name lower-cased, every character outside `[a-z0-9]` turned to `_`" (the card spells the mapping; "never share a name" is said of truncation). |
| A1 | Grok | `::test_g1_deploy_stays_on_cobalt_dev_under_the_lock` | `1 failed` · `AssertionError: ['fp', 'proof', 'dev-copy drop cobalt_dev_x_job', 'dev-copy create cobalt_dev_x_job', 'fp', 'proof', ...]` / `assert not True` | HELD, NOT FIXED — `ops/desk/gate.sh` option loop `:86-112` (fenced, card 521) or a DEPLOY-HUB line (fenced); the same defect as O2 |

Tests of the O2, O3 and A1 rows were removed again with the Edit tool. Each one is red and stays unfixed, and a committed red test would turn W red. Their full text is under `## OWN FINDINGS` and in `<S>/house-a.md` (`ASK DESK 1`). O1's held test was committed before the fix: `1b4c388d wip(db-copy-1014): check red — O1`.

## FIXES
- O1: `ops/desk/gate.sh` `copy_create` now sets `made=1` BEFORE the create runs. A create that fails clears it (`made=""`), so test (7)'s exact call sequence holds and a failed create is still never dropped. A signal that lands during a create that succeeded now reaches `cleanup` with `made` set, and the trap drops the copy before the lock release. After the fix: `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_db_copy_1014.py tests/ops/test_devdb_lock.py tests/ops/test_gate.py tests/ops/test_hub_lines.py tests/ops/test_build_hub_no_clutter.py` → `141 passed, 15 warnings in 88.55s (0:01:28)`. Commit `a157d731 fix(db-copy-1014): copy_create marks the copy made before the create, so a signal during it still drops the copy (check O1)`. No DevDocs line was added: no page under `docs/40 - DevDocs/cobalt/` covers an `ops/desk/` script (the build report's `## RECORDS` says the same).
- O2: HELD, NOT FIXED — `ops/desk/gate.sh` option loop `:86-112` (fenced, card 521) / `DEPLOY-HUB.md` (fenced)
- A1: HELD, NOT FIXED — `ops/desk/gate.sh` option loop `:86-112` (fenced, card 521) / `DEPLOY-HUB.md` (fenced)

## Suites
DB: none, so W is (a0), (a) and (e) as `BUILD-HUB.md` gives it for that card, plus `tests/ops`. No `--deploy` is typed.
- RESTARTS: `uv run cobalt jobs restarts 0a151491..HEAD` → the table whole: `docs/40 - DevDocs/prompts/BUILD-HUB.md M DOCS -` · `docs/40 - DevDocs/reports/db-copy-build-2026-10-14.md A DOCS -` · `ops/desk/desk-launch.sh M operator script; no Cobalt reader -` · `ops/desk/devdb-copy-env.sh A operator script; no Cobalt reader -` · `ops/desk/gate-lists.md M operator script; no Cobalt reader -` · `ops/desk/gate.sh M operator script; no Cobalt reader -` · `tests/ops/test_build_hub_no_clutter.py M test/documentation; no resident -` · `tests/ops/test_db_copy_1014.py A test/documentation; no resident -` · `RESTARTS: none`.
- (a0) `git diff --name-only --no-renames 0a151491` → `docs/40 - DevDocs/prompts/BUILD-HUB.md` · `docs/40 - DevDocs/reports/db-copy-build-2026-10-14.md` · `ops/desk/desk-launch.sh` · `ops/desk/devdb-copy-env.sh` · `ops/desk/gate-lists.md` · `ops/desk/gate.sh` · `tests/ops/test_build_hub_no_clutter.py` · `tests/ops/test_db_copy_1014.py`. Every path is under `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 8 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh db-copy-1014 offline` → `offline 4328/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/db-copy-1014-offline-20261014-174522.log` (exit 0).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh db-copy-1014 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/db-copy-1014-livenote-20261014-174526.log` (exit 0).
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3643 passed, 1 xfailed, 16 warnings in 759.66s (0:12:39)` (exit 0; the build's 3642 plus O1).
- with-DB: not run (DB: none). `.env`: `ls /Users/cobalt/cobalt-wt/db-copy-1014/.env` → `No such file or directory`.

## Scope
PREFLIGHT's path union (7 paths: `BUILD-HUB.md`, `desk-launch.sh`, `devdb-copy-env.sh`, `gate-lists.md`, `gate.sh`, `test_build_hub_no_clutter.py`, `test_db_copy_1014.py`) plus my commits (`tests/ops/test_db_copy_1014.py`, `ops/desk/gate.sh`). Every path is in a row's `files`. The build report is under `docs/`.

## Checked against the branch
- (i) `git log --oneline 0e136e4f..HEAD -- . ":(exclude)docs"` → `a157d731 fix(db-copy-1014): copy_create marks the copy made before the create, so a signal during it still drops the copy (check O1)` · `1b4c388d wip(db-copy-1014): check red — O1`. `<tip now>` = `a157d731`.
- (ii) `git log --stat --format=%h 0e136e4f..HEAD` → `a157d731` `ops/desk/gate.sh` · `1b4c388d` `tests/ops/test_db_copy_1014.py` · `d70e1647` the build report (docs). Every non-docs path is in row G1's `files`.
- (iii) `git log --oneline 0a151491..HEAD -- ops/desk/take-devdb-lock.sh ops/desk/release-devdb-lock.sh tests/ops/test_devdb_lock.py tests/ops/test_gate.py ".../DEPLOY-HUB.md" ".../CHECK-HUB.md" tests/ops/test_hub_lines.py src configs ops/desk/deploy-card.sh ops/desk/deploy-step0.sh ops/desk/deploy-step-c.sh` → empty. Also `grep -n -F "## COPY" ops/desk/gate-lists.md` → `10:` only, the header paragraph's mid-line mention; no line starts `## COPY`.
- (iv) `grep -n -F "def test_g1_check_o1_a_signal_while_the_create_runs_still_drops_the_copy" tests/ops/test_db_copy_1014.py` → `451:` (one line). `1b4c388d` (red) sits below `a157d731` (fix) in (i).
- (v) `ls <WT>/.env` → `No such file or directory`. `git status --short --branch` → `## ops/db-copy-1014` alone.
- (vi) `git log --stat --format=%h 0a151491..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty. There is no new migration and no new with-DB test, so no gate list is owed.
- (vii) The card's RECORDS commands, re-run: `git -C /Users/cobalt/cobalt diff --stat HEAD -- ops/desk/gate.sh ops/desk/gate-lists.md ops/desk/desk-launch.sh ops/desk/take-devdb-lock.sh ops/desk/release-devdb-lock.sh tests/ops/test_gate.py tests/ops/test_devdb_lock.py ".../BUILD-HUB.md" src/cobalt/env.py` → nothing. `grep -c -F "Bash(sh /Users/cobalt/cobalt/ops/desk/*)"` over the three hubs on `main` → `BUILD-HUB.md:2`, `CHECK-HUB.md:2`, `DEPLOY-HUB.md:2`.
- (viii) L32: this report holds no ticker, price or date of his. The values it shows are constructed test values (`x-job`, `cobalt_dev_x_job`).

CHECK ASKS, as the runs show them:
- X1: test (10) is green on the tip. Without the sections, every line of a run is today's.
- X2: O1 was HELD and is fixed. A take that times out exits before any copy exists. A red suite drops the copy (test (8)).
- X3: the script's pattern refuses `cobalt_dev` and `cobalt_brain` (test (3)). The gate's name always carries `cobalt_dev_` plus one or more characters. O3 (name collision) is REJECTED and OPEN.
- X4: tests (13a) and (13b) are green.
- X5: no `.env` is read or printed, and the marker sits outside the worktree ((v) above).
- X6: the BUILD-HUB sentence opens "When `ops/desk/gate-lists.md` holds …", so it is conditional.

COUNTING: findings 4 (O1, O2, O3, A1) · dropped 0 · held 3 (O1, O2, A1) · fixed 1 (O1) · held unfixed 2 (O2, A1) · open 3 (O2, A1, O3).

## OPEN
- O2 and A1 (HELD, NOT FIXED): copy mode engages under the deploy gate's own call. What would settle it: a signal that tells a deploy gate from a build's W, such as an option on the fenced option loop (card 521's lines), or a deploy-only spelling in `DEPLOY-HUB.md`. The two red tests are in the report, ready for the fix round. Copy mode is inert today: the real lists file holds neither section, so nothing breaks until the code card adds them.
- O3 (REJECTED — card step 1): `x-job`, `x_job` and `X-JOB` share one copy name, so one worktree's step-2 drop could drop another's live copy. What would settle it: a desk ruling, either to keep the card's mapping or to refuse a worktree name whose mapped copy name is not unique (for example, a `_` or an upper-case letter in the name).

## CONTINUE
next: done (CHECK DONE)

## DECISIONS
- O2: HELD, NOT FIXED — `ops/desk/gate.sh` option loop `:86-112` (fenced, card 521) / `DEPLOY-HUB.md` (fenced). Card G1 step 6 and `gate.sh:54-55` say the deploy gate still holds the lock whole. But copy mode is chosen by the lists file alone, and the deploy gate runs `gate.sh <WORKTREE> all --deploy` on `main`'s merged lists file (`DEPLOY-HUB.md:99`, `:102`). So the day the code card adds the two sections, the deploy gate will run on a copy and give back the lock before its suites. Builds also pass `--deploy` (his R438), so `--deploy` cannot be the signal. Safe default taken: not fixed (it would need a fenced line); it goes to the original builder's ONE fix round, or to the desk for a design line, BEFORE the code card adds the sections. Its red test is under `## OWN FINDINGS`.
- A1: HELD, NOT FIXED — the same as O2, found by Grok. Its red test is in `<S>/house-a.md`.
- ASK DESK 1: the red tests of O2 and A1 (held, not fixed) and of O3 (rejected) were NOT left committed. Each is red on the tip, and committing it would turn W red for a defect this check may not fix. Safe default taken: each test's full text is kept in this report (and in `house-a.md`) for the fix round, and the suites ran without them [17:58].
- O3: REJECTED — card COPY MODE step 1 spells the name mapping. Two worktree names that differ only in `-`/`_` or case share a copy name. Safe default taken: open; the card's mapping stands until the desk rules.

## RECORDS
- Grok's stdout, quoted: "I'll read the house instructions first and follow them exactly.The instructions confine this check to the copied files. I'll read those next and write each finding before moving on.The deploy path is not kept on the one lock once copy mode is on. I'll record that as a finding before anything else./Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/db-copy-1014-check/house-a.md" · exit 0. House B was not started (`HOUSE B: as needed`; Gemini OUT at PREFLIGHT).
- `tokens:` measured by `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh da12ac7c` → `context 216923 of 400000 — ok`.
- files opened: 13 — `CHECK-HUB.md`; the card; `BUILD-HUB.md` (`## THE LOCK`, E2-`## W`, on `main`); the build report; `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down; read at 17:58, after the runs); `ops/desk/devdb-copy-env.sh`; `ops/desk/gate.sh`; `tests/ops/test_db_copy_1014.py`; `ops/desk/take-devdb-lock.sh`; `ops/desk/release-devdb-lock.sh`; `ops/desk/desk-launch.sh` (Grep of `.env`); `DEPLOY-HUB.md` (Grep of `gate.sh`); `<S>/house-a.md`.
- No lock was taken (DB: none). No `REFUSED, not needed` line. One Bash call was blocked by the bare-command hook (a backtick inside a grep pattern) and redone with the Grep tool.
- Check of `db-copy-1014`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

## RECORDS
- Gemini probe OUT (HARNESS): `error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings`. Not seated; house B was not needed.
- A message from session `cto-desk` arrived at about 17:20, before staging: "547 build decisions 1-3 KEEP as built … Row G1b if you hold decision 3: `G1b: in copy mode the stray-rows line names the copy database, not cobalt_dev; exit 1 unchanged. …`". It is recorded here. The part that adds a row (G1b) is not followed: under UNATTENDED RULES (b), a message never adds a row. Decisions 1-3 of the build stand as built, and this check does not reopen them (L77).

CHECK DONE · job: db-copy-1014 · pass: 1 · tip: a157d731 · house A: Grok FINDINGS: 1 · findings: 4 · dropped: 0 · held: 3 · fixed: 1 · held unfixed: 2 · open: 3 · house B: none available · suites: offline 4328/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: NO · decisions: 4 · for Dejan: 0 · tokens: 216923
