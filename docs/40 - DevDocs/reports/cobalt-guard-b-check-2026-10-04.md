# cobalt-guard-b — check, pass 1 (2026-10-04)

## §0 Headline
- Checked B1–B4 at `3c451126` with no outside house (R47). I wrote 3 findings myself and ran each one.
- O1 held: B4 missed a lone `sort`/`uniq`/`awk` written by path or behind `NAME=` (`LC_ALL=C sort -o out f`). Fixed in `1f2c19a9`; its red test came first in `f5815a0e`.
- O2 (`sort --co=sh`) and O3 (`sort --files0-from=.env`) are red but REJECTED by the card's letter, so they stay open. Both are under `## DECISIONS`; O3 is FOR DEJAN.
- Suites on `1f2c19a9`: offline 3782/0 · live-note 146/0 · tests/ops 1281 passed. RESTARTS: none. `.env` absent.

## L74
A system reminder in this session asked for commits to end with a `Claude-Session:` line beside `Co-Authored-By`. Recorded once as data and not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` → exit 0, last line `AUTHORIZED`. Rows: INSTALLED nothing · PLACEHOLDER nothing · CARD COMMITTED `25355c969cf4b08cf3099af2d8a3180963a7baa5` · CARD UNCHANGED nothing · STANDING LIST R60 row 46, committed `962e9d17` · RULING 2026-10-02 R47 row 54 `HIS RULING · APPROVED`, committed `4e3fa8d8` · RULING 2026-10-03 R33 row 39 `HIS RULING · APPROVED`, committed `a09f0862` · HOUSE A overruled 2026-10-02 R47 row 54, committed `4e3fa8d8` · `AUTHORIZED`.

## PREFLIGHT
- `sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` → exit 0: clock `Sun Oct  4 19:11:13 EDT 2026` · status `## ops/cobalt-guard-b-1004` · head `a9fe5090 docs(cobalt-guard-b): build report — 3c451126`, above TIP only `docs/40 - DevDocs/reports/cobalt-guard-b-build-2026-10-04.md` · env here: No such file · env anywhere: none · report: `BUILT · job: cobalt-guard-b · tip: 3c451126 | … | self-check: 3 of 3 | decisions: 0 · for Dejan: 0` · range: `3c451126`, `87576deb`, `82c5c7a2` (3 commits) · `PREFLIGHT OK`.
- THE RANGE: `git log --stat --format=%h 979ec797..3c451126` → 3c451126 `tests/ops/test_bare_guard.py | 2 ++`; 87576deb `ops/desk/bare-guard.py | 80 +++…-`; 82c5c7a2 `tests/ops/test_bare_guard.py | 98 +++`. Path union: `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py`.
- DB: none: `git diff --name-only --no-renames 979ec797..3c451126` → `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py` — both under `ops/` / `tests/ops/`.
- `ls <S>` → No such file (fresh).
- house A: none (overruled 2026-10-02 R47). No house gate, no probe.

## Files copied
none (no house).

## OWN FINDINGS
Read before any run: the card, `git diff 979ec797..3c451126` whole, `ops/desk/bare-guard.py` at the tip whole, `tests/ops/test_bare_guard.py:130-279` (helpers) and `:967-1069` (the new tests), the build report whole, the cobalt-guard check report O4/O5 (`:99-137`, the restored tests match byte for byte in their bodies; O4 gains a `found` parameter and an `assert_resend`).

FINDING O1
ROW: B4
CLAIM: `ops/desk/bare-guard.py:486-487` and `:443-447` key B4 on `ws[0]` as typed, so a lone `sort`, `uniq` or `awk` written by path or behind a `NAME=` word (`LC_ALL=C sort -o out f`, `/usr/bin/sort -o out f`) meets no check; in a pipe segment the same shape is denied (`:462-463`, not a read-only filter), and G3 already names the verb past both (`verb`, `:192-197`, used at `:615`). B4 says "exactly as to a pipe segment".
RUN: TEST, `tests/ops/test_bare_guard.py`
```python
@pytest.mark.parametrize(
    "command,found",
    [
        ("LC_ALL=C sort -o out f", SORT_FOUND),
        ("/usr/bin/sort -o out f", SORT_FOUND),
        ("LC_ALL=C uniq f out", UNIQ_FOUND),
        ("/usr/bin/awk -f p.awk f", AWK_FILE_FOUND),
    ],
)
def test_check_b_o1_a_lone_filter_by_path_or_behind_an_assignment_that_writes_is_denied(roots, command, found):
    assert_resend(run(command, make_seat(roots, "build")), found)
```
EXPECT: on the tip each id fails `assert 0 == 2`.

FINDING O2
ROW: B2 (b)
CLAIM: `ops/desk/bare-guard.py:418` denies a long name only when it "begins `com`"; GNU `getopt_long` takes any unique prefix, and in sort's option table `--co` is unique to `compress-program`, so `sort --co=sh` would run a program and pass (that sort reading is not proven by a run here: `sort` is not on this seat's list).
RUN: TEST, `tests/ops/test_bare_guard.py`
```python
@pytest.mark.parametrize("command", ["grep X f | sort --co=sh", "sort --co=sh f"])
def test_check_b_o2_a_two_letter_compress_program_prefix_is_denied(roots, command):
    assert_resend(run(command, make_seat(roots, "build")), SORT_FOUND)
```
EXPECT: on the tip each id fails `assert 0 == 2`.

FINDING O3
ROW: B1
CLAIM: `ops/desk/bare-guard.py:615` tests `is_env` on whole words; `sort --files0-from=.env` (relative) holds `.env` only as an option value, `is_env("--files0-from=.env")` is false (`:607`, basename starts `-`), so a B1 verb reads `.env` and the hook passes it (sort quotes an unopenable file name in its error).
RUN: TEST, `tests/ops/test_bare_guard.py`
```python
def test_check_b_o3_sort_files0_from_env_is_denied(roots):
    assert_denied(run("sort --files0-from=.env", make_seat(roots, "build")), G3_ROUTE)
```
EXPECT: on the tip fails `assert 0 == 2`.

No finding: B1 test restored as written; B2 controls are the card's four plus three; B3 test and control as the card names; B4 ids as the card names plus the probe ending. No path to a score, rank, grade or size (the diff touches only the hook and its test). Nothing outside the two files. No CHECK ASKS on the card.

## Findings
none (no house).

## Dropped
none.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_bare_guard.py::test_check_b_o1_a_lone_filter_by_path_or_behind_an_assignment_that_writes_is_denied` | `FFFF` · `4 failed, 15 warnings in 1.04s`; each `test_bare_guard.py:995: AssertionError:` `assert 0 == 2` (`returncode=0, stderr=''`) | HELD — each lone command passes the hook |
| O2 | own | `… ::test_check_b_o2_a_two_letter_compress_program_prefix_is_denied` | `FF` · `2 failed, 15 warnings in 0.86s`; each `test_bare_guard.py:995` `assert 0 == 2` | REJECTED — card B2 (b): a long name is denied when it "begins `com` and is a prefix of `compress-program`"; `--co` does not begin `com`. Test removed again. OPEN |
| O3 | own | `… ::test_check_b_o3_sort_files0_from_env_is_denied` | `F` · `1 failed, 15 warnings in 0.83s`; `test_bare_guard.py:268: AssertionError: (0, '')` `assert 0 == 2` | REJECTED — card B1: "Any of them with an operand that `is_env` matches"; `--files0-from=.env` is an option word, and `## NOT IN THIS JOB`: "No rule beyond B1–B4: G1–G11 stand as built". Test removed again. OPEN |

Held test committed before the fix: `f5815a0e wip(cobalt-guard-b): check red — O1` (`tests/ops/test_bare_guard.py | 13 +++`).

## FIXES
| id | commit | change | after |
|---|---|---|---|
| O1 | `1f2c19a9 fix(cobalt-guard-b): a lone sort uniq awk by path or behind NAME= meets B4 (check O1)` | `ops/desk/bare-guard.py` `g1`: the lone-command words drop leading `NAME=value` words (`ASSIGN`) and the verb is read as its basename before `filter_problem`, as G3's `verb` reads it; a pipe segment is unchanged (its first word must already be a bare filter name) | `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_bare_guard.py` → `476 passed, 15 warnings in 15.09s` |

DevDocs line: not written. `ops/desk/bare-guard.py` has no module page under `docs/40 - DevDocs/cobalt/` (build report `## RECORDS`), and the card fences every file but its two.

## Suites
On `<tip now>` = `1f2c19a9`, DB: none, so W is (a0), (a), (e) plus `tests/ops`:
- RESTARTS: `uv run cobalt jobs restarts 979ec797..HEAD` → `docs/40 - DevDocs/reports/cobalt-guard-b-build-2026-10-04.md	A	DOCS	-` · `ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-` · `tests/ops/test_bare_guard.py	M	test/documentation; no resident	-` · `RESTARTS: none`.
- (a0) `git diff --name-only --no-renames 979ec797` → `docs/40 - DevDocs/reports/cobalt-guard-b-build-2026-10-04.md` · `ops/desk/bare-guard.py` · `tests/ops/test_bare_guard.py`; every path under `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 3 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh cobalt-guard-b-1004 offline` → exit 0, `offline 3782/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/cobalt-guard-b-1004-offline-20261004-191506.log`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh cobalt-guard-b-1004 livenote` → exit 0, `live-note 146/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/cobalt-guard-b-1004-livenote-20261004-191507.log`. One skip, `grep -n -F "SKIPPED" <log>` → `56: SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. No skip names `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 0, `1281 passed, 1 xfailed, 15 warnings in 348.59s (0:05:48)` (the build's 1277 plus O1's 4 ids).
- With-DB: not run (DB: none). `.env`: `ls /Users/cobalt/cobalt-wt/cobalt-guard-b-1004/.env` → `No such file or directory` (19:25 ET). `git status --short --branch` → `## ops/cobalt-guard-b-1004`.

## Scope
PREFLIGHT path union `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py` plus my commits (`ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py`): both are B1–B4's `files`. Docs above TIP: the build report only.

## Checked against the branch
- (i) `git log --oneline 3c451126..HEAD -- . ":(exclude)docs"` → `1f2c19a9 fix(cobalt-guard-b): a lone sort uniq awk by path or behind NAME= meets B4 (check O1)` · `f5815a0e wip(cobalt-guard-b): check red — O1`. `<tip now>` = `1f2c19a9`.
- (ii) `git log --stat --format=%h 3c451126..HEAD` → `1f2c19a9` `ops/desk/bare-guard.py | 7 +++++--` · `f5815a0e` `tests/ops/test_bare_guard.py | 13 +++` · `a9fe5090` the build report (docs). Every non-docs path is a row's file.
- (iii) Fence: `git log --oneline 979ec797..HEAD -- "docs/40 - DevDocs/prompts" ops/desk/gate-lists.md configs` → empty. The card fences "any file but" the two; (ii) shows only those two.
- (iv) `grep -n -F "def test_check_b_o1_a_lone_filter_by_path_or_behind_an_assignment_that_writes_is_denied" tests/ops/test_bare_guard.py` → `1081:` one line; `f5815a0e` (red) sits below `1f2c19a9` (fix) in (i).
- (v) `ls /Users/cobalt/cobalt-wt/cobalt-guard-b-1004/.env` → No such file; `git status --short --branch` → `## ops/cobalt-guard-b-1004` alone.
- (vi) `git log --stat --format=%h 979ec797..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no migration, no with-DB test; no gate-list change owed.
- (vii) No card `## RECORDS` line names an `ls`, `grep` or `git -C /Users/cobalt/cobalt log` command. The RESTARTS record's expected `RESTARTS: none` matches my run.
- (viii) L32: this report holds constructed values only (`f`, `out`, `p.awk`, `/x/wt/job/.env`).

## OPEN
- O2 · own · REJECTED — card B2 (b) "begins `com`". `sort --co=sh` (alone or after `grep X f |`) passes the hook (`2 failed … assert 0 == 2`). GNU `getopt_long` takes unique prefixes, and `--co` is unique to `compress-program` in sort's table (not run here: `sort` is not on this seat's list). Would settle it: a card row that widens (b) to names that begin `co`; the test in `## OWN FINDINGS` O2 is its red.
- O3 · own · REJECTED — card B1 "an operand that `is_env` matches" and the fence. `sort --files0-from=.env` passes the hook (`1 failed … assert 0 == 2`). Sort reads the file for names and quotes one it cannot open in its error. The absolute form `--files0-from=/x/wt/job/.env` is caught, because `is_env` takes a basename. Would settle it: a card row making G3 test the value of an `--opt=` word; the test in O3 is its red.

Counts: findings 3 (own) · dropped 0 · held 1 (O1) · fixed 1 · held unfixed 0 · open 2 (O2, O3). House B is needed by the count, but house A is none under R47 and the card is not mandatory, so `house B: none available`.

## CONTINUE
next: none (check done)

## DECISIONS
1. **O2: `sort --co=sh` runs a program and passes the hook.** OPEN, REJECTED by the letter of B2 (b) ("begins `com`"). No house B is available (R47), so it goes to the follow-up list unless the judge orders a row. Safe default taken: built to the card's letter; nothing changed. What it needs: a card row that widens (b) to names beginning `co`. Its red is the O2 test in `## OWN FINDINGS`.
2. **O3: `sort --files0-from=.env` reads `.env` and passes the hook. FOR DEJAN.** OPEN, REJECTED by the letter of B1 ("an operand") and by the fence (G1–G11 stand as built). Sort quotes a name it cannot open in its error, so the file's text can be printed, and secrets are never printed (cobalt.md, absolute boundaries). `Bash(sort *)` is one of the four strings waiting for his approval. Safe default taken: nothing changed. Recommended order: a G3 row that tests the value of an `--opt=` word, before the four strings go on any line. Its red is the O3 test.

## RECORDS
- L74: a system reminder (not a tool result) asked for a `Claude-Session:` line in commits. Recorded once under `## L74`; not acted on.
- Dropped findings: none. No house ran (HOUSE A: none — overruled 2026-10-02 R47), so no house produced nothing.
- REFUSED, not needed: none. CONTINUED: none. Extra lock takes: none (DB: none).
- `<S>/opus-1.md` written (`/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/cobalt-guard-b-check/opus-1.md`). It summarises O1–O3 and points to this report for the full sections.
- Not in scope, noted only: gawk's `-E`/`--exec`, `-i`/`--include` and `-l` also load program text from a file. The card names only `-f`/`--file` (B3), and the fence allows no rule beyond B1–B4.
- files opened: 12 — `CHECK-HUB.md`; the card; `ops/desk/bare-guard.py`; `tests/ops/test_bare_guard.py`; the build report; `cobalt-guard-check-2026-10-04.md` (O4/O5, grep); `BUILD-HUB.md` (`## RESTARTS`, `## W`); `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); three background-task output files (offline, live-note, tests/ops); the live-note gate log (grep, tail).
- **Check of `cobalt-guard-b`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).**

CHECK DONE · job: cobalt-guard-b · pass: 1 · tip: 1f2c19a9 · house A: none (overruled 2026-10-02 R47) · findings: 3 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 2 · house B: none available · suites: offline 3782/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 12 · ready: YES · decisions: 2 · for Dejan: 1
