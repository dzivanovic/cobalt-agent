# rename-follow-up — check, pass 1 (2026-10-03)

## §0 Headline
- Pass 1 of `rename-follow-up` at `393f3ad5`. No outside house, by his overrule (2026-10-02 R47). I checked it alone.
- 5 own findings, 0 held. Undoing the fix turns both row tests red, plus my X1 test (`3 failed, 19 passed`). With the fix restored: `21 passed`.
- X1: a rename across two read classes derives both restarts (`1 passed`). X2: `changes()` has one caller, and `restarts.py` never asks git for `--name-only` or porcelain output.
- No commit by me: the build's suite lines stand. Nothing is open, so house B is not needed. ready: YES.

## L74
- One harness system reminder (not a tool result) asked for a `Claude-Session:` trailer on commits. I made no commit, and CHECK-HUB says commits carry `Co-Authored-By` only. Recorded once, not acted on.

## AUTHORIZATION
- installed: `grep -n -E "«INSTAL[L]" CHECK-HUB.md` → no output (exit 1).
- card: `grep -n -E "«FIL[L]" <card>` → no output; `git -C /Users/cobalt/cobalt log -1 --format=%H -- <card>` → `05355f3a9a331c76c1788f0476f2bfac8f701931`; `git -C … diff --stat -- <card>` → no output.
- standing list 2026-09-30 R60: `grep -n "^| R60 " cto-2026-09-30.md` → `46:| R60 | 15:15 ET | **HIS RULING** … APPROVES STANDING-LIST.md once (4be06af0) … | APPROVED |`; `log -S"| R60 |"` → `962e9d1705b62a61821f62f4d7bf5d8131656e2a`.
- RULINGS 2026-10-02 R47: `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house … | HIS RULING · APPROVED |`; `log -S"| R47 |"` → `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a`. Also proves the card's `HOUSE A: none — overruled 2026-10-02 R47`.
- RULINGS 2026-10-02 R157: `164:| R157 | 17:40 ET | HIS RULING (B): the brain's full process list for 10-03 runs this week … | HIS RULING · APPROVED |`; `log -S"| R157 |"` → `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2`.
- house gates: not run (HOUSE A: none — overruled 2026-10-02 R47).

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sat Oct  3 12:08:32 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/rename-follow-up-1003` |
| tip | `git log --oneline -1` | 0 | `8c32a8d1 docs(rename-follow-up): build report — 393f3ad5` |
| docs-only above tip | `git log --stat --format=%h 393f3ad5..HEAD` | 0 | `8c32a8d1` · `.../reports/rename-follow-up-build-2026-10-03.md | 140 +++` (docs only) |
| built | `tail -n 3 <REPORT>` | 0 | `BUILT · job: rename-follow-up · tip: 393f3ad5 \| on a09f0862 \| migration: none \| offline 3739/0 \| with-DB 846/0 \| live-note 146/0 \| cobalt_dev: 0013 \| .env: removed \| RESTARTS: com.cobalt.radar \| rows: 1 of 1 \| self-check: 3 of 3 \| decisions: 2 · for Dejan: 0` |
| range | `git log --oneline a09f0862..393f3ad5` | 0 | `393f3ad5 fix(rename-follow-up): changes() emits the old path of a rename/copy as a delete (O3, L42)` · `3506e45a wip(rename-follow-up): red — O3 rename old path absent from changes()` |
| range stat | `git log --stat --format=%h a09f0862..393f3ad5` | 0 | 393f3ad5: `docs/40 - DevDocs/cobalt/jobs/restarts.md | 4`, `src/cobalt/jobs/restarts.py | 4`; 3506e45a: `tests/cobalt/test_jobs_restarts.py | 35` |
| lock (own) | `ls <WT>/.env` | 1 | `No such file or directory` |
| lock (all) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| houses | — | — | house A: none (overruled 2026-10-02 R47) · no probe, no house gate |

Path union: `src/cobalt/jobs/restarts.py`, `tests/cobalt/test_jobs_restarts.py`, `docs/40 - DevDocs/cobalt/jobs/restarts.md`.

## Files copied
none (no house).

## OWN FINDINGS
Written before any run (house A: none, overruled 2026-10-02 R47, so this is the only list).

FINDING O1
ROW: X1
CLAIM: A rename whose old and new paths sit in different classes may not derive both restarts; `classify()` handles each `Change` on its own (`src/cobalt/jobs/restarts.py:194`), and the old path now arrives as `D` (`:79-82`), but no test pins the case where both sides have a resident reader.
RUN: TEST — `tests/cobalt/test_jobs_restarts.py`:
```python
def test_check_x1_a_rename_across_two_read_classes_derives_both_restarts(monkeypatch):
    def fake_git(*args):
        if args[:2] == ("diff", "--name-status") and len(args) == 3:
            return "R100\tconfigs/cobalt/rules.yaml\tconfigs/cobalt/radar.yaml\n"
        return ""
    monkeypatch.setattr(restarts, "_git", fake_git)
    by_path = {row.path: row for row in classify("BASE..TIP")}
    assert by_path["configs/cobalt/rules.yaml"].change == "D"
    assert by_path["configs/cobalt/rules.yaml"].restarts == ("com.cobalt.aset",)
    assert "com.cobalt.radar" in by_path["configs/cobalt/radar.yaml"].restarts
    assert not any(row.escalate for row in by_path.values())
```
EXPECT: if the claim is true, an `AssertionError` (or `KeyError` on the old path); if false, `1 passed`.

FINDING O2
ROW: X2
CLAIM: a caller might feed `changes()`/`collect()` a `--name-only` or porcelain shape; `collect()` is called at `src/cobalt/jobs/restarts.py:86`, `:88`, `:89`, and `changes()` at `:194`.
RUN: COMMAND — `grep -rn -F "changes(" src` (then `grep -n -F "name-only" src/cobalt/jobs/restarts.py` and `grep -n -F "porcelain" src/cobalt/jobs/restarts.py`).
EXPECT: if the claim is true, a caller other than `restarts.py:194`, or a `--name-only`/porcelain call in `restarts.py`.

FINDING O3
ROW: O3
CLAIM: the two row tests (`tests/cobalt/test_jobs_restarts.py:144`, `:154`) may stay green when the fix at `src/cobalt/jobs/restarts.py:79-82` is undone.
RUN: COMMAND — with the four lines `:79-82` removed by Edit: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_jobs_restarts.py`; then restore.
EXPECT: if the claim is true, `21 passed`; if false, `2 failed, 19 passed`.

FINDING O4
ROW: SCOPE
CLAIM: the build may touch the fence (`configs/cobalt/jobs.yaml`, or a classification rule in `restarts.py`) beyond the four lines of `collect()`.
RUN: COMMAND — `git log --oneline a09f0862..393f3ad5 -- configs/cobalt/jobs.yaml` (and `git diff a09f0862 393f3ad5 -- src`).
EXPECT: if the claim is true, a commit line, or a `src` hunk outside `changes()`.

FINDING O5
ROW: SCOPE (6)
CLAIM: `cobalt.jobs.restarts` may be reached from a score, rank, grade or size path.
RUN: COMMAND — `grep -rn -F "jobs.restarts" src` (and `grep -rn -F "from .restarts" src`).
EXPECT: if the claim is true, an importer outside `cobalt.jobs`/the CLI.

## Findings
none (no house).

## Dropped
none.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | test added at the tip; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_jobs_restarts.py::test_check_x1_a_rename_across_two_read_classes_derives_both_restarts` | `1 passed in 0.56s`. With the fix undone (O3 run), it fails: `E       KeyError: 'configs/cobalt/rules.yaml'` at `tests/cobalt/test_jobs_restarts.py:186` | NOT HELD. X1 answered: both restarts are derived. Test removed again with Edit |
| O2 | own | `grep -rn -F "changes(" src` · `grep -n -F "name-only" src/cobalt/jobs/restarts.py` · `grep -n -F "porcelain" src/cobalt/jobs/restarts.py` | `src/cobalt/jobs/restarts.py:69:def changes(…)`, `src/cobalt/jobs/restarts.py:194:    for item in changes(git_range):`, `radar/evaluate.py:1324`/`:1907` (`formation_changes`, an unrelated function) · no output · no output | NOT HELD. X2 answered: the one caller is `classify()`, and `collect()` gets only `--name-status` output |
| O3 | own | `:79-82` removed by Edit; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_jobs_restarts.py` | `3 failed, 19 passed in 13.75s`: `:151` `AssertionError: [Classification(path='ops/desk/start_aset.sh', change='R', rule='operator script; no Cobalt reader', restarts=(), escalate=False)]`; `:168` `At index 1 diff: Change(path='docs/new.md', change='A') != Change(path='configs/cobalt/radar.yaml', change='D')`; `:186` the O1 `KeyError`. Restored by Edit (O1 test removed); `git status --short --branch` → `## ops/rename-follow-up-1003`; re-run → `21 passed in 13.31s` | NOT HELD: both row tests go red when the fix is undone |
| O4 | own | `git log --oneline a09f0862..393f3ad5 -- configs/cobalt/jobs.yaml` · `git diff a09f0862 393f3ad5 -- src` | no output · one hunk `@@ -76,6 +76,10 @@ def changes(…)`: the four `+` lines of the R/C branch only | NOT HELD |
| O5 | own | `grep -rn -F "jobs.restarts" src` · `grep -rn -F "from .restarts" src` · `grep -rn -F "import restarts" src` | no output · no output · `src/cobalt/jobs/cli.py:29:from . import restarts` | NOT HELD: the only importer is the `cobalt jobs` CLI, so the change reaches no score, rank, grade or size |

No HELD finding, so there is no `wip(rename-follow-up): check red` commit.

## FIXES
none (no finding held).

## Suites
suites: as built (no commit). From the build report `## W THE THREE SUITES`:
- offline `3739 passed, 745 skipped, 1 xfailed, 36 warnings in 638.02s (0:10:38)`
- with-DB pass 1 `673 passed, 7 skipped, 3803 deselected, 2 xfailed, 12 warnings in 121.76s`, pass 2 `173 passed, 1 deselected, 5 warnings in 231.03s` (846 in all)
- live-note `146 passed, 1 skipped, 15 warnings in 28.17s`
- `cobalt_dev: 0013 — F2 = F0`; `.env: removed, proven gone (W)`
- RESTARTS (build `## RESTARTS`): `RESTARTS: com.cobalt.radar`

I took no lock. `ls <WT>/.env` → `No such file or directory` at PREFLIGHT and again at step 7.

## Scope
PREFLIGHT path union: `src/cobalt/jobs/restarts.py`, `tests/cobalt/test_jobs_restarts.py` (both in row O3's `files`), and `docs/40 - DevDocs/cobalt/jobs/restarts.md` (the DevDocs line). I made no commit. The working tree is unchanged after my runs.

## Checked against the branch
- (i) `git log --oneline 393f3ad5..HEAD -- . ":(exclude)docs"` → no output (no commit of mine); `<tip now>` = `393f3ad5`.
- (ii) `git log --stat --format=%h 393f3ad5..HEAD` → `8c32a8d1` · `.../reports/rename-follow-up-build-2026-10-03.md | 140` (docs only).
- (iii) fence: `git log --oneline a09f0862..HEAD -- configs/cobalt/jobs.yaml` → no output. The second fenced item (classification rules in `restarts.py`) is covered by O4: one hunk, inside `changes()`.
- (iv) no HELD finding.
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/rename-follow-up-1003`.
- (vi) `git log --stat --format=%h a09f0862..HEAD -- src/cobalt/db_migrations tests/cobalt` → `3506e45a` · `tests/cobalt/test_jobs_restarts.py | 35` only: no new migration and no new with-DB test file, so TREE STATE: unchanged is carried.
- (vii) no card `## RECORDS` line names an `ls`, `grep` or `git -C` command.
- (viii) L32: this report holds only paths, test names, commit ids and test counts.

## OPEN
none (open: 0).

## CONTINUE
next: done

## DECISIONS
none

## RECORDS
- No house: card `HOUSE A: none — overruled 2026-10-02 R47`. Its row is proved under `## AUTHORIZATION`. `## 1` and `## 3` were not run, and nothing was staged under `<S>`.
- `opus-1.md` was not written: house B is not needed, and `<S>` was never made.
- Dropped findings: none. REFUSED lines: none. CONTINUED lines: none. Lock takes: none.
- A copy source is emitted as `D` because the card's row says so (`C<nn>\told\tnew` → DELETE of the old path), even though git keeps that file. No rule in `classify()` reads `D`, so the derivation is the same. This is not a finding.
- BUILD-HUB `## THE LOCK`, `## E2`, `## RESTARTS` and `## W` were not opened: I made no commit, took no lock and ran no with-DB step, so none of them was acted on.
- files opened: 7. They are `CHECK-HUB.md`, the card, `src/cobalt/jobs/restarts.py`, `tests/cobalt/test_jobs_restarts.py`, the build report (`rename-follow-up-build-2026-10-03.md`), `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down), and `reports/ops-glob-check-2026-10-02.md` (O3, by Grep).
- Check of `rename-follow-up`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: rename-follow-up · pass: 1 · tip: 393f3ad5 · house A: none (overruled 2026-10-02 R47) · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 7 · ready: YES · decisions: 0 · for Dejan: 0
