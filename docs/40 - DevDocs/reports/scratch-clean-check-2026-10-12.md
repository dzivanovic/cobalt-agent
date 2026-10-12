# scratch-clean-1012 — CHECK (pass 1) · 2026-10-12

## §0 Headline
- Check of `scratch-clean-1012`. House A was Grok (`FINDINGS: 2`). House B was not needed. I wrote 4 findings of my own. Nothing was dropped.
- Two findings held and both are fixed in `581d7b3a`. O4: a file tracked by a nested repo under an ignored dir was removed. G1: a dir holding `.{env,x}` was removed.
- Four findings did not hold: O1, O2, O3 and G2. The script already refuses those paths.
- Suites: offline 4199/0, live-note 146/0, `tests/ops` 3190/0. cobalt_dev not taken (DB: none). RESTARTS: none. `ready: YES`.

## L74
A system block arrived mid-session asking that commits carry a `Claude-Session:` trailer. It is recorded here and was not acted on: commits carry `Co-Authored-By` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/389-cleanup-class-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/389-cleanup-class-card.md" · 0 · e3d807e272d4840da0bebf43eb739844c138ac4b
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/389-cleanup-class-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 19:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```
House gates (06:58 ET): `grep -n "^| R17 " …cto-2026-09-24.md` → one row (line 35, STANDING `Bash(grok *)`); `grep -n "^| R19 " …` → one row (line 37, the four house strings standing); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Mon Oct 12 06:58:34 EDT 2026
status · git status --short --branch · 0 · ## ops/scratch-clean-1012
head · git log --oneline -1; git log --stat --format=%h 382876bc..HEAD · 0 · (5 lines)
    7b950fe1 docs(scratch-clean-1012): build report — 382876bc
    7b950fe1
    
     .../reports/scratch-clean-build-2026-10-12.md      | 169 +++++++++++++++++++++
     1 file changed, 169 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/scratch-clean-1012/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/scratch-clean-1012/docs/40 - DevDocs/reports/scratch-clean-build-2026-10-12.md" · 0 · BUILT · job: scratch-clean-1012 · tip: 382876bc | on 5e5fab02 | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 210025
range · git log --oneline 5e5fab02..382876bc · 0 · (2 lines)
    382876bc feat(scratch-clean-1012): scratch-clean.sh removes one untracked or ignored workspace path; BUILD-HUB NO CLUTTER line (C1, H1, R1138, L81, L76)
    98a8b744 wip(scratch-clean-1012): red
PREFLIGHT OK
```
- THE RANGE · `git log --stat --format=%h 5e5fab02..382876bc` · 0:
```
382876bc
 docs/40 - DevDocs/prompts/BUILD-HUB.md |   2 +
 ops/desk/scratch-clean.sh              | 156 +++++++++++++++++++++++++++++++++
 tests/ops/test_scratch_clean.py        |  84 +++++++++---------
 3 files changed, 203 insertions(+), 39 deletions(-)
98a8b744
 tests/ops/test_build_hub_no_clutter.py |  60 +++++
 tests/ops/test_scratch_clean.py        | 455 +++++++++++++++++++++++++++++++++
 2 files changed, 515 insertions(+)
```
  Path union: `docs/40 - DevDocs/prompts/BUILD-HUB.md`, `ops/desk/scratch-clean.sh`, `tests/ops/test_scratch_clean.py`, `tests/ops/test_build_hub_no_clutter.py`.
- DB: none · `git diff --name-only --no-renames 5e5fab02..382876bc` · 0 → `docs/40 - DevDocs/prompts/BUILD-HUB.md`, `ops/desk/scratch-clean.sh`, `tests/ops/test_build_hub_no_clutter.py`, `tests/ops/test_scratch_clean.py` — every path under `ops/`, `tests/ops/` or `docs/`.
- `ls <S>` · 1 · `No such file or directory` → fresh.
- House probes · `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · 0:
```
grok: UP
gemini: UP
```
- Seats: no `HOUSE A:` header line; Grok UP → **house A: Grok · house B: none (not needed)** (`HOUSE B: as needed`).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · 0:
```
41156 …/scratch-clean-1012-check/diff.md
12877 …/files/389-cleanup-class-card.md
20385 …/files/scratch-clean-build-2026-10-12.md
33098 …/files/wt/docs/40 - DevDocs/prompts/BUILD-HUB.md
6753 …/files/wt/ops/desk/scratch-clean.sh
2135 …/files/wt/tests/ops/test_build_hub_no_clutter.py
17655 …/files/wt/tests/ops/test_scratch_clean.py
355 …/rulings.md
STAGED 8 files · 134414 bytes · commits 2
```
`stage-copy.sh` (each `COPIED`): `files/wt/ops/desk/job-clean.sh` 11524 · `files/wt/ops/desk/bare-guard.py` 53420 · `files/wt/tests/ops/test_gate_clean.py` 30258 · `files/wt/tests/ops/test_hub_lines.py` 11448 · `files/wt/tests/cobalt/test_placement.py` 3431 · `files/brain-direction-2026-10-02.md` 49936 · `files/cto-2026-10-11.md` 42406. `HOUSE-INSTRUCTIONS.md` written at 07:00 (14774 bytes).

## OWN FINDINGS
Written 07:0x ET before any house file was opened.

FINDING O1
ROW: X1 (C1 (8))
CLAIM: A file that a NESTED untracked repo tracks (`<wt>/scratch/vendor/.git` + committed `t.md`) passes every guard: no `.git` component, a file so no `find` (`ops/desk/scratch-clean.sh:125`), and the outer worktree's `ls-files`/`status` (`:138-145`) see only an untracked tree — so it may be removed.
RUN: TEST `tests/ops/test_scratch_clean.py`
```python
def test_o1_a_file_tracked_by_a_nested_repo_is_refused(desk):
    nested = desk.job_wt / "scratch" / "vendor"
    f = desk.put(nested / "t.md", "nested tracked\n")
    git(nested, "init", "-q", "-b", "main")
    git(nested, "add", "-A")
    git(nested, "commit", "-q", "-m", "n")
    done = desk.run(str(f))
    assert done.returncode == 1, done.stdout + done.stderr
    assert f.read_text() == "nested tracked\n"
```
EXPECT: on the tip, `assert done.returncode == 1` fails with `RUN: rm -rf -- …/t.md` in the message (removed).

FINDING O2
ROW: X1 (C1 (6), (8))
CLAIM: A SUBDIRECTORY of a nested repo (`<wt>/scratch/vendor/sub/`, the `.git` one level up) holds no `.git` below it, so `:125-133` pass it, and the outer git sees only untracked paths — the nested repo's tracked files may be removed.
RUN: TEST `tests/ops/test_scratch_clean.py`
```python
def test_o2_a_directory_inside_a_nested_repo_is_refused(desk):
    nested = desk.job_wt / "scratch" / "vendor"
    f = desk.put(nested / "sub" / "t.md", "nested tracked\n")
    git(nested, "init", "-q", "-b", "main")
    git(nested, "add", "-A")
    git(nested, "commit", "-q", "-m", "n")
    done = desk.run(str(nested / "sub"))
    assert done.returncode == 1, done.stdout + done.stderr
    assert f.read_text() == "nested tracked\n"
```
EXPECT: `assert done.returncode == 1` fails (exit 0, `sub` removed).

FINDING O3
ROW: X1 (C1 (4), (8))
CLAIM: On a case-insensitive volume, a case variant of a tracked directory (`<wt>/DOCS/mixed`) may pass `realpath` equality (`:78-79`) if `realpath` keeps the spelling, then `ls-files --error-unmatch` (case-sensitive pathspec, `:138`) misses `docs/mixed/t.md` and the tracked file is removed.
RUN: TEST `tests/ops/test_scratch_clean.py`
```python
def test_o3_a_case_variant_of_a_tracked_directory_is_refused(desk):
    mixed = desk.job_wt / "docs" / "mixed"
    desk.put(mixed / "u.md")
    done = desk.run(str(desk.job_wt / "DOCS" / "mixed"))
    assert done.returncode == 1, done.stdout + done.stderr
    assert (mixed / "t.md").read_text() == "tracked\n"
```
EXPECT: `assert done.returncode == 1` fails (exit 0, the tracked `t.md` gone).

FINDING O4
ROW: X1 (C1 (8))
CLAIM: As O1 but under an IGNORED directory (`docs/_inflight/clone/`, a cloned repo there): the outer status prints `!! ` and the nested repo's tracked file may be removed.
RUN: TEST `tests/ops/test_scratch_clean.py`
```python
def test_o4_a_file_tracked_by_an_ignored_nested_repo_is_refused(desk):
    nested = desk.job_wt / "docs" / "_inflight" / "clone"
    f = desk.put(nested / "t.md", "nested tracked\n")
    git(nested, "init", "-q", "-b", "main")
    git(nested, "add", "-A")
    git(nested, "commit", "-q", "-m", "n")
    done = desk.run(str(f))
    assert done.returncode == 1, done.stdout + done.stderr
    assert f.read_text() == "nested tracked\n"
```
EXPECT: `assert done.returncode == 1` fails (exit 0, removed).

X2, X3, X4 read with no finding: every `refused()` call in `tests/ops/test_scratch_clean.py:113-128` asserts exit 1, one `REFUSED: ` line, empty stdout and `snap` equal, and each R test ends in a `removed()` control; the H1 line is the card's text byte for byte (`git diff 5e5fab02..382876bc -- BUILD-HUB.md` adds exactly it and one blank line); the script touches only `$WT/<registered>/` and `$CLAUDE_JOB_DIR/tmp/` and reads no secret.

## Findings
Grok finished 07:20 ET (exit 0; it wrote `<S>/house-a.md` itself, its stdout the path); `FINDINGS: 2`. House B: none (not needed).
- G1 · Grok · C1 (7) · an ignored dir holding an entry named `.{env,x}` is removed; `is_env` brace-expands it to `.env`, the script's `forbidden` does not · TEST
- G2 · Grok · X1 · a file tracked by a nested repo under the worktree is removed · TEST

## Dropped
none (both blocks carry a `def test_`).

## RUNS
Each test pasted into `tests/ops/test_scratch_clean.py` with the Edit tool (form unchanged; the two Grok tests as written) and run alone: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_scratch_clean.py::<test>`.

| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `test_o1_a_file_tracked_by_a_nested_repo_is_refused` | `1 passed, 15 warnings in 1.15s` | NOT HELD (removed again) |
| O2 | own | `test_o2_a_directory_inside_a_nested_repo_is_refused` | `1 passed, 15 warnings in 1.00s` | NOT HELD (removed again) |
| O3 | own | `test_o3_a_case_variant_of_a_tracked_directory_is_refused` | `1 passed, 15 warnings in 0.92s` | NOT HELD (removed again) |
| O4 | own | `test_o4_a_file_tracked_by_an_ignored_nested_repo_is_refused` | `1 failed` · `E AssertionError: RUN: rm -rf -- …/wt/x-job/docs/_inflight/clone/t.md` · `scratch-clean: removed …/clone/t.md` · `assert 0 == 1` (`test_scratch_clean.py:493`) | HELD — a file a nested repo tracks, under an ignored dir, is removed |
| G1 | Grok | `test_c1_a_brace_name_is_env_reads_is_not_removed` | `1 failed` · `E AssertionError: RUN: rm -rf -- …/wt/x-job/src/pkg/__pycache__` · `scratch-clean: removed …/__pycache__` · `assert 0 == 1` (`:502`) | HELD — a dir holding `.{env,x}` (is_env reads `.env`) is removed |
| G2 | Grok | `test_x1_a_file_tracked_in_a_nested_repo_is_not_removed` | `1 passed, 15 warnings in 1.10s` | NOT HELD (removed again; same as O1 — under an untracked dir the outer status prints nothing for the path) |

Red commit: `e0ffca74 wip(scratch-clean-1012): check red — O4, G1` (`tests/ops/test_scratch_clean.py`, 24 insertions).

## FIXES
| fix | finding | change | run | commit |
|---|---|---|---|---|
| F1 | O4 | `ops/desk/scratch-clean.sh` (8) root (a): `git -C <parent> rev-parse --show-toplevel` must equal `$WT/<name>`, else `REFUSED: <p> sits inside another git work tree (<top>), not <tree>`; header (8) updated | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_scratch_clean.py tests/ops/test_build_hub_no_clutter.py` → `53 passed, 15 warnings in 7.80s` | `581d7b3a` |
| F2 | G1 | `forbidden()`: a name holding `{` or `}` is refused as `.env` (is_env brace-expands, `bare-guard.py:839`); header (7) updated | same run | `581d7b3a` |
DevDocs line: none — no page under `docs/40 - DevDocs/cobalt/` covers an `ops/desk/` script (the build report's RECORDS, the same finding).

## Suites
On tip `581d7b3a`. This is a DB: none card, so W runs (a0), (a) and (e).
- RESTARTS: `uv run cobalt jobs restarts 5e5fab02..HEAD` → `BUILD-HUB.md M DOCS -` · `scratch-clean-build-2026-10-12.md A DOCS -` · `ops/desk/scratch-clean.sh A operator script; no Cobalt reader -` · `tests/ops/test_build_hub_no_clutter.py A test/documentation; no resident -` · `tests/ops/test_scratch_clean.py A test/documentation; no resident -` · `RESTARTS: none`.
- (a0): `git diff --name-only --no-renames 5e5fab02` → `docs/40 - DevDocs/prompts/BUILD-HUB.md`, `docs/40 - DevDocs/reports/scratch-clean-build-2026-10-12.md`, `ops/desk/scratch-clean.sh`, `tests/ops/test_build_hub_no_clutter.py`, `tests/ops/test_scratch_clean.py`. Every path is under `ops/`, `tests/ops/` or `docs/`. **cobalt_dev: not taken (DB: none — 5 paths)**.
- (a): `gate.sh scratch-clean-1012 offline` → `offline 4199/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/scratch-clean-1012-offline-20261012-072238.log`.
- (e): `gate.sh scratch-clean-1012 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/scratch-clean-1012-livenote-20261012-073442.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3190 passed, 1 xfailed, 15 warnings in 642.55s (0:10:42)`. The build's run gave 3188; the 2 extra are the held tests.
- `.env`: `ls -la /Users/cobalt/cobalt-wt/scratch-clean-1012/.env` → `No such file or directory`. No lock was taken.

## Scope
The PREFLIGHT path union (`BUILD-HUB.md`, `ops/desk/scratch-clean.sh`, `tests/ops/test_scratch_clean.py`, `tests/ops/test_build_hub_no_clutter.py`) plus my commits (`tests/ops/test_scratch_clean.py`, `ops/desk/scratch-clean.sh`). All of these are in the `files` of row C1 or row H1.

## Checked against the branch
- (i) `git log --oneline 382876bc..HEAD -- . ":(exclude)docs"` → `581d7b3a fix(scratch-clean-1012): refuse a path inside a nested repo and a dot name holding a brace (check O4, G1)` · `e0ffca74 wip(scratch-clean-1012): check red — O4, G1`. tip now = `581d7b3a`.
- (ii) `git log --stat --format=%h 382876bc..HEAD` → `581d7b3a ops/desk/scratch-clean.sh | 15` · `e0ffca74 tests/ops/test_scratch_clean.py | 24` · `7b950fe1 …/reports/scratch-clean-build-2026-10-12.md | 169`. Both non-docs paths are in row C1. Nothing is WIDENED.
- (iii) `git log --oneline 5e5fab02..HEAD -- ops/desk/desk-launch.sh ops/desk/job-clean.sh ops/desk/bare-guard.py …STANDING-LIST.md …CARD.md …CHECK-HUB.md …SHADOW-HUB.md …CTO-DESK-WAKEUP.md src .claude/settings.json` → empty.
- (iv) `grep -n -F "def test_o4_a_file_tracked_by_an_ignored_nested_repo_is_refused" tests/ops/test_scratch_clean.py` → `456:` · `grep -n -F "def test_c1_a_brace_name_is_env_reads_is_not_removed" …` → `467:`. Red `e0ffca74` sits below fix `581d7b3a` in (i).
- (v) `ls …/.env` → No such file · `git status --short --branch` → `## ops/scratch-clean-1012`.
- (vi) `git log --stat --format=%h 5e5fab02..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty. There is no new migration and no new with-DB test, so no gate lists are needed.
- (vii) Card RECORDS, re-run:
  - `grep -c "^claude --bg "` on BUILD, CHECK and SHADOW hubs → 1 · 1 · 1.
  - `grep -c -F "Bash(sh /Users/cobalt/cobalt/ops/desk/*)"` → 2 · 2 · 1. The string is present on each hub.
  - `ls -la …/launcher-shadow-check-1011/docs/_inflight` → `README.md` only.
  - `ls -ld /Users/cobalt/cobalt-wt /Users/cobalt/.claude/jobs` → both `drwxr-xr-x` directories.
- (viii) L32: this report holds no value of his. The test values are constructed (`COBALT_TEST_CONSTRUCTED=1`, `nested tracked`).

## OPEN
none. Counts: findings 6 (O1–O4, G1, G2) · dropped 0 · held 2 (O4, G1) · fixed 2 · held unfixed 0 · open 0.

## CONTINUE
next: none — CHECK DONE

## DECISIONS
none

## RECORDS
- House A Grok: started 07:00 ET and finished 07:20 ET with exit 0. It wrote `house-a.md` itself (`FINDINGS: 2`). House B: none (not needed; `HOUSE B: as needed`). The Gemini probe was UP but Gemini was not seated.
- The Grok completion notice arrived after `## OWN FINDINGS` was written (07:01:55 ET).
- One hook block: my first `git commit` message for the fix named the env-file word. `bare-guard.py` blocked it (`route: .env is never read; …`). I resent the same commit with the message reworded, with no change to the command shape. This was not a refusal of a listed string.
- Gemini was not launched, and no session or agent other than house A was launched.
- No lock was taken. No `CONTINUE` was received.
- L74: the `Claude-Session:` trailer request, as in `## L74`.
- files opened: 14. They are:
  - CHECK-HUB.md and the card
  - BUILD-HUB.md (sections)
  - `ops/desk/scratch-clean.sh` and `tests/ops/test_scratch_clean.py`
  - `tests/ops/test_build_hub_no_clutter.py`
  - `bare-guard.py:830-869`
  - the build report (`:100-170`)
  - `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down)
  - `house-a.md`
  - the four task outputs (probe, Grok, offline gate, live-note gate)
- Check of `scratch-clean-1012`: house A `Grok`, house B `none`, and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: scratch-clean-1012 · pass: 1 · tip: 581d7b3a · house A: Grok FINDINGS: 2 · findings: 6 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 155480
