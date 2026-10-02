# ops-glob — check, pass 1 (2026-10-02)

## §0 Headline
- G1 holds at `9fa18f14`. The new test is red when the fix is undone (I re-ran it: `1 failed, 18 passed`, `'UNCLASSIFIED' == 'operator scr...Cobalt reader'`). It is green at the tip: `43 passed`.
- X1: nothing outside the folder names a file in `ops/desk/`. X2: no path outside the folder matches the prefix (six-path test green).
- One open item, O3, which was already there before this build: `changes()` drops the old side of a rename. A rename of a read file into `ops/desk/` now derives no restart and no escalate; on the base it escalated. It is REJECTED as out of the row's clauses and goes under `## DECISIONS` as a follow-up.
- House A: none (overruled 2026-10-02 R47). No commit of mine, so the suites stand as built. `ready: YES`.

## L74
- The session's attribution reminder asked for a `Claude-Session:` line in commits. Recorded here as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`date` → `Fri Oct  2 10:00:48 EDT 2026`
- INSTALLED: `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` → exit 1, no output.
- CARD placeholder: `grep -n -E "«FIL[L]" ".../2026-10-02/15-ops-glob-card.md"` → exit 1, no output.
- CARD committed: `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-02/15-ops-glob-card.md"` → `2f286234f9edc62ef05aa41e526ed6dea88b9b3d`; `git -C … diff --stat -- <card>` → no output.
- RULINGS R47: `grep -n "^| R47 " ".../reports/cto-2026-10-02.md"` → line 54, carries `HIS RULING` and `HIS RULING · APPROVED`; `git -C … log -1 --format=%H -S"| R47 |" -- …cto-2026-10-02.md` → `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a`.
- HOUSE A overrule (same row R47, "no outside house"): proved by the R47 lines above.
- STANDING LIST R60: `grep -n "^| R60 " ".../reports/cto-2026-09-30.md"` → line 46, `**HIS RULING**` … `APPROVED`; `git -C … log -1 --format=%H -S"| R60 |" -- …cto-2026-09-30.md` → `962e9d1705b62a61821f62f4d7bf5d8131656e2a`.
- House gates R17 / R19 (cto-2026-09-24.md): line 35 and line 37, one row each; `-S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c`.

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Fri Oct  2 10:00:48 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/ops-glob-1002` |
| tip | `git log --oneline -1` | 0 | `24001f82 docs(ops-glob): build report — 9fa18f14` |
| docs-only above tip | `git log --stat --format=%h 9fa18f14..HEAD` | 0 | `24001f82` · `.../reports/ops-glob-build-2026-10-02.md \| 197 +++` · `1 file changed, 197 insertions(+)` — docs only |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: ops-glob · tip: 9fa18f14 \| on a0188b69 \| migration: none \| offline 3784/0 \| with-DB 4554/0 \| live-note 146/0 \| cobalt_dev: 0013 \| .env: removed \| RESTARTS: com.cobalt.radar \| rows: 1 of 1 \| self-check: 3 of 3 \| decisions: 0 · for Dejan: 0` |
| range | `git log --oneline a0188b69..9fa18f14` | 0 | `9fa18f14 fix(ops-glob): every path under ops/desk/ is an operator script, by rule (G1, L42, L3)` · `9e03e04c wip(ops-glob): red — every path under ops/desk/ is an operator script (G1)` |
| range stat | `git log --stat --format=%h a0188b69..9fa18f14` | 0 | 9fa18f14: `docs/40 - DevDocs/cobalt/jobs/restarts.md \| 4 ++++`, `src/cobalt/jobs/restarts.py \| 4 +++-`; 9e03e04c: `tests/cobalt/test_jobs_restarts.py \| 20 ++++` |
| lock (own) | `ls <WT>/.env` | 1 | `No such file or directory` |
| lock (all) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| scratch | `ls <S>` | 1 | `No such file or directory` — fresh |
| house | — | — | house A: none (overruled 2026-10-02 R47); no house gate, no probe run (NO OUTSIDE HOUSE line) |

Path union (for `## Scope`): `src/cobalt/jobs/restarts.py`, `tests/cobalt/test_jobs_restarts.py`, `docs/40 - DevDocs/cobalt/jobs/restarts.md` — all three in G1's `files`.

## Files copied
none — house A: none (overruled 2026-10-02 R47); `## 1` not run.

## OWN FINDINGS
Read: the card; the diff `a0188b69..9fa18f14` (`git diff a0188b69 9fa18f14`); `src/cobalt/jobs/restarts.py` whole at the tip; `tests/cobalt/test_jobs_restarts.py` lines 1–150; the build report's `## E0`–`## RECORDS` and last line; `cobalt.md` `## What Cobalt is` and `## Build rules` down; `BUILD-HUB.md` `## THE LOCK` to `## CLOSE`.

FINDING O1
ROW: X1
CLAIM: A plist, a `reads:` entry of `configs/cobalt/jobs.yaml` or a `src/` module other than `src/cobalt/jobs/restarts.py:38` names a file under `ops/desk/`, so the folder is not safe to match whole.
RUN: COMMAND — `grep -rn -F "desk/" ops configs/cobalt/jobs.yaml src --include=*.py --include=*.plist --include=*.yaml` (on my list as three plain calls: `grep -rn -F "ops/desk" <WT>/configs/cobalt/jobs.yaml`, `grep -rn -F "ops/desk" <WT>/src`, `grep -rln -F "desk/" <WT>/ops`)
EXPECT: a hit other than `restarts.py:38` and its `.pyc`.

FINDING O2
ROW: X2
CLAIM: A path not under the folder matches the prefix test at `src/cobalt/jobs/restarts.py:226` (the folder name bare, a sibling file, a case variant, the folder nested under another root).
RUN: TEST — `tests/cobalt/test_jobs_restarts.py`:
```python
def test_check_o2_no_path_outside_ops_desk_matches_the_prefix(monkeypatch):
    outside = ("ops/desk", "ops/desk.sh", "ops/desktop.sh", "Ops/desk/x.sh", "ops/Desk/x.sh", "lib/ops/desk/x.sh")
    monkeypatch.setattr(restarts, "changes", lambda _range: [Change(p, "A") for p in outside])
    by_path = {row.path: row for row in classify("HEAD...HEAD")}
    for path in outside:
        assert by_path[path].rule != "operator script; no Cobalt reader", path
        assert by_path[path].escalate is True, path
```
EXPECT: an assertion fails naming one of the six paths.

FINDING O3
ROW: G1 (entry path: a rename)
CLAIM: `changes()` keeps only the last tab field of a `git diff --name-status` line (`src/cobalt/jobs/restarts.py:79`), so a rename of a resident-read file into the folder (`R100\tops/start_aset.sh\tops/desk/start_aset.sh`) yields only the new path; G1 now classifies it `operator script; no Cobalt reader`, no restart and no escalate, where on `BASE` the same range escalated (`UNCLASSIFIED`).
RUN: TEST — `tests/cobalt/test_jobs_restarts.py`:
```python
def test_check_o3_a_rename_out_of_a_read_path_into_ops_desk_still_restarts_or_escalates(monkeypatch):
    def fake_git(*args):
        if args[:2] == ("diff", "--name-status") and len(args) == 3:
            return "R100\tops/start_aset.sh\tops/desk/start_aset.sh\n"
        return ""
    monkeypatch.setattr(restarts, "_git", fake_git)
    rows = classify("BASE..TIP")
    assert any(row.escalate or "com.cobalt.aset" in row.restarts for row in rows), rows
```
EXPECT: `AssertionError` with the one row `Classification(path='ops/desk/start_aset.sh', change='R', rule='operator script; no Cobalt reader', restarts=(), escalate=False)`.

FINDING O4
ROW: SCOPE
CLAIM: The range touches a path inside the fence (`OPS_TOOLS`'s entries, a script under `ops/`, `configs/cobalt/jobs.yaml`) or another classification rule.
RUN: COMMAND — `git log --oneline a0188b69..9fa18f14 -- ops configs/cobalt/jobs.yaml`, and `git diff a0188b69 9fa18f14 -- src` (only the two `+` lines at `:37-38` and `:226`).
EXPECT: a commit listed by the first; a changed line in `src` other than the constant, its comment and the `:226` test.

FINDING O5
ROW: G1 (test strength)
CLAIM: `test_every_path_under_ops_desk_is_an_operator_script` (`tests/cobalt/test_jobs_restarts.py:111`) stays green when the fix is undone or the slash is dropped.
RUN: COMMAND — the builder's two mutations are quoted in its report (`## E3`, MUTATION 1 and 2: `1 failed, 2 passed` each). I re-run the test at the tip (`uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_jobs_restarts.py`) and re-run MUTATION 1 myself with the Edit tool.
EXPECT: the test passes under MUTATION 1.

## Findings
none — no house.

## Dropped
none.

## RUNS
| id · source | run | output | verdict |
|---|---|---|---|
| O1 · own | `grep -rn -F "ops/desk" <WT>/configs/cobalt/jobs.yaml` · `grep -rn -F "ops/desk" <WT>/src` · `grep -rln -F "desk/" <WT>/ops` | jobs.yaml: no output · src: `src/cobalt/jobs/restarts.py:38:OPS_DESK_PREFIX = "ops/desk/"` and `Binary file …/__pycache__/restarts.cpython-314.pyc matches` · ops: no output (no plist and no script under `ops/` contains `desk/`) | NOT HELD. X1 answered: no plist, no `reads:` entry and no other `src/` module names a file under `ops/desk/`. |
| O2 · own | test added to `tests/cobalt/test_jobs_restarts.py`; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_jobs_restarts.py::test_check_o2_no_path_outside_ops_desk_matches_the_prefix` | `1 passed in 0.51s` | NOT HELD: removed again with Edit. X2 answered: `ops/desk`, `ops/desk.sh`, `ops/desktop.sh`, `Ops/desk/x.sh`, `ops/Desk/x.sh` and `lib/ops/desk/x.sh` each escalate and none gets the operator rule. |
| O3 · own | test added to `tests/cobalt/test_jobs_restarts.py`; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_jobs_restarts.py::test_check_o3_a_rename_out_of_a_read_path_into_ops_desk_still_restarts_or_escalates` | `1 failed in 0.51s`; `E       AssertionError: [Classification(path='ops/desk/start_aset.sh', change='R', rule='operator script; no Cobalt reader', restarts=(), escalate=False)]` at `tests/cobalt/test_jobs_restarts.py:147` | REJECTED — G1: "Every path under `ops/desk/` is an operator script", so the new path's class is the row's. The lost old path comes from `changes()` (`restarts.py:79`, `path = parts[-1]`), which is not in the row. Fixing it would change every rename's classification, and the fence excludes "Any other classification rule of `classify`". Red for its stated reason. The test is removed from the tree (it is not committed red) and kept verbatim under `## OWN FINDINGS`. OPEN. |
| O4 · own | `git log --oneline a0188b69..9fa18f14 -- ops configs/cobalt/jobs.yaml` · `git diff a0188b69 9fa18f14 -- src` | first: no output · second: only `+#: Safe to match whole: …`, `+OPS_DESK_PREFIX = "ops/desk/"`, and `-        if not rule and path in OPS_TOOLS:` / `+        if not rule and (path in OPS_TOOLS or path.startswith(OPS_DESK_PREFIX)):` | NOT HELD: nothing inside the fence, no other rule touched, `OPS_TOOLS` unchanged, rule text and `()` unchanged. |
| O5 · own | MUTATION 1 by Edit (`(path in OPS_TOOLS)` at `restarts.py:226`); `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_jobs_restarts.py` | `1 failed, 18 passed in 11.54s`; first failing line `E           AssertionError: assert 'UNCLASSIFIED' == 'operator scr...Cobalt reader'` at `tests/cobalt/test_jobs_restarts.py:123`. Undone by Edit. Then `git status --short --branch` → `## ops/ops-glob-1002`, and `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_jobs_restarts.py tests/cobalt/test_jobs_reads.py` → `43 passed in 13.53s` | NOT HELD: the test is red when the fix is undone. |

No HELD finding, so there is no `wip(ops-glob): check red` commit.

## FIXES
none — no finding held.

## Suites
`suites: as built (no commit)`. From the build report (`## W THE THREE SUITES`): offline `3784 passed, 673 skipped, 1 xfailed, 25 warnings in 597.48s (0:09:57)`; with-DB pass 1 `4383 passed, 7 skipped, 65 deselected, 3 xfailed, 31 warnings in 703.57s (0:11:43)` and pass 2 `171 passed, 1 deselected, 5 warnings in 219.31s (0:03:39)` (`<d>` = 4554); live-note `146 passed, 1 skipped, 15 warnings in 27.98s`. `cobalt_dev: 0013 — F2 = F0`. `.env: removed, proven gone (W)` at 08:42. RESTARTS line (build report `## RESTARTS`): `RESTARTS: com.cobalt.radar`.
I took no lock: `ls /Users/cobalt/cobalt-wt/ops-glob-1002/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`.

## Scope
Path union `a0188b69..9fa18f14`: `src/cobalt/jobs/restarts.py`, `tests/cobalt/test_jobs_restarts.py`, `docs/40 - DevDocs/cobalt/jobs/restarts.md`. All three are in G1's `files`. I made no commits.

## Checked against the branch
(i) `git log --oneline 9fa18f14..HEAD -- . ":(exclude)docs"` → no output (no commit of mine); `<tip now>` = `9fa18f14`.
(ii) `git log --stat --format=%h 9fa18f14..HEAD` (PREFLIGHT) → `24001f82`, only `docs/40 - DevDocs/reports/ops-glob-build-2026-10-02.md`. No non-docs path.
(iii) `git log --oneline a0188b69..HEAD -- ops configs/cobalt/jobs.yaml` → no output. `OPS_TOOLS` is unchanged (`git diff a0188b69 9fa18f14 -- src`, O4).
(iv) no HELD finding.
(v) `ls <WT>/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; `git status --short --branch` → `## ops/ops-glob-1002`.
(vi) `git log --stat --format=%h a0188b69..HEAD -- src/cobalt/db_migrations tests/cobalt` → `9e03e04c`, `tests/cobalt/test_jobs_restarts.py | 20 +++`. No migration and no new with-DB test file. TREE STATE: unchanged holds.
(vii) No card `## RECORDS` line names an `ls`, a `grep` or a `git -C /Users/cobalt/cobalt log` command. Nothing to run.
(viii) L32: this report holds constructed paths only (`ops/desk/any-new-tool.sh`, `ops/desk/start_aset.sh` as a test value); no ticker, price or date of his.

Counting: findings 5 (own 5, house 0) · dropped 0 · held 0 · fixed 0 · held unfixed 0 · open 1 (O3).

## OPEN
- O3 · own · REJECTED. `changes()` (`src/cobalt/jobs/restarts.py:79`) keeps only the last tab field of a `--name-status` line. A rename's old path is never classified. With G1, a rename of a resident-read file into `ops/desk/` derives no restart and no escalate; on `BASE` the same line escalated `UNCLASSIFIED`. The same gap was already there before this build for a rename into `docs/` or any other no-restart class. Run and output: `## RUNS` O3. To settle it: a card row that makes `changes()` also emit the old path of an `R`/`C` line (as a `D`), with the O3 test as its red. If a real plist still names the old path, the plist edit itself already derives the restart (`plist in diff`). That is why I take the gap as narrow.

## CONTINUE
next: none — CHECK DONE.

## DECISIONS
- O3 (open, outside the card's rows; `house B: none available` under the R47 overrule). Rename handling in `changes()` drops the old path, so a resident-read file renamed into `ops/desk/` derives no restart. Default taken: nothing fixed here; it goes to the follow-up list as a separate card row (`changes()` emits the old path of `R`/`C`, red = the O3 test under `## OWN FINDINGS`). It does not block this branch.

## RECORDS
- No house: HOUSE A none (overruled 2026-10-02 R47); `## 1` and `## 3` not run; no house gate run at PREFLIGHT and no probe. The R17/R19 greps under AUTHORIZATION ran anyway.
- No dropped finding. No `REFUSED` or `CONTINUED` line. No lock take.
- L74: one reminder asking for a `Claude-Session:` line, recorded under `## L74`, not acted on.
- The O2 and O3 tests were added to `tests/cobalt/test_jobs_restarts.py` and removed again with Edit. MUTATION 1 was applied to `src/cobalt/jobs/restarts.py:226` and undone. Afterwards `git status --short --branch` → `## ops/ops-glob-1002` (clean).
- Line numbers: the card's `restarts.py` line 224 (the rule) is `:226` at the tip, +2 from the constant and its comment.
- files opened: 7 — `CHECK-HUB.md`, the card `15-ops-glob-card.md`, `src/cobalt/jobs/restarts.py`, `tests/cobalt/test_jobs_restarts.py`, the build report `ops-glob-build-2026-10-02.md`, `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down), `BUILD-HUB.md` (`## THE LOCK` to `## CLOSE`).
- Check of `ops-glob`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: ops-glob · pass: 1 · tip: 9fa18f14 · house A: none (overruled 2026-10-02 R47) · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 7 · ready: YES · decisions: 1 · for Dejan: 0
