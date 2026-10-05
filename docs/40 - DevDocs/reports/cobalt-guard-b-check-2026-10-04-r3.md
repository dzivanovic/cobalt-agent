# cobalt-guard-b — check, pass 1 (r3) — 2026-10-04

## §0 Headline
- Pass 1 (r3) of `cobalt-guard-b`, no outside house (overruled 2026-10-02 R47). I wrote 4 findings; 2 held and both are fixed at `47ec01c5`.
- O1: an unquoted brace word (`sort {-o,out} f`, `uniq {f,out}`, `sort -{n..p} f`, `sort /x/wt/job/.{d..f}nv`) got past B1, B2 and B4. O2: `sort $'-o' out f` got past B2 and B4.
- Suites on `47ec01c5`: offline 3782/0 · live-note 146/0 · `tests/ops` 1348 passed · RESTARTS none · `.env` absent.
- 1 decision for the desk, not for Dejan: the `$'…'` fix sits in the one word reader that every rule uses.

## L74
One block arrived in a system reminder at session start asking commits to end with a `Claude-Session:` line. Recorded as DATA; acted on none. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-04/06-cobalt-guard-b-card.md"` · exit 0 · output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-04/06-cobalt-guard-b-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-04/06-cobalt-guard-b-card.md" · 0 · c77349dd4d978f290ef7907bb734a80c811d04c3
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-04/06-cobalt-guard-b-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-02 R47 row · grep -n "^| R47 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-02.md" · 0 · 54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, no meter wait, built and deployed in a day; card `20` (`deploy-outage.sh`) keeps a Grok check ([words](cto-2026-10-02-words.md#r38-r48)). | HIS RULING · APPROVED |
RULING 2026-10-02 R47 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R47 |" -- "docs/40 - DevDocs/reports/cto-2026-10-02.md" · 0 · 4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a
RULING 2026-10-02 R47 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-02.md" · 0 · the row as grepped
RULING 2026-10-03 R33 row · grep -n "^| R33 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · 39:| R33 | 11:08 ET | HIS RULING (via brain): read-only pipes allowed (each segment `grep`, `sed -n`, `cut`, `sort`, `uniq`, `head`, `tail`, `wc`, `awk`; no redirect, `&&`, `;`); amends 10-01 R45 part 1; card `10` Sunday ([words](cto-2026-10-03-words.md#r33)). | HIS RULING · APPROVED |
RULING 2026-10-03 R33 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R33 |" -- "docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · a09f08622ac8522adce99096f5af18faaed9e2ca
RULING 2026-10-03 R33 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · the row as grepped
RULING 2026-10-03 R283 row · grep -n "^| R283 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · 289:| R283 | 10-04 19:55 ET | HIS RULING (via brain): drop `awk` for good; amends 10-03 R33; no line carries `Bash(awk *)`; after guard-b ships only `cut`, `sort`, `uniq` strings; guard G1 drops awk (B11) ([words](cto-2026-10-04-words.md#r283)). | HIS RULING · APPROVED — pending fold |
RULING 2026-10-03 R283 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R283 |" -- "docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · c41fdd35ed9c1d407a4432c3656074f33029d4dd
RULING 2026-10-03 R283 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · the row as grepped
HOUSE A overruled 2026-10-02 R47 row · grep -n "^| R47 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-02.md" · 0 · 54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, no meter wait, built and deployed in a day; card `20` (`deploy-outage.sh`) keeps a Grok check ([words](cto-2026-10-02-words.md#r38-r48)). | HIS RULING · APPROVED |
HOUSE A overruled 2026-10-02 R47 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R47 |" -- "docs/40 - DevDocs/reports/cto-2026-10-02.md" · 0 · 4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a
HOUSE A overruled 2026-10-02 R47 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-02.md" · 0 · the row as grepped
AUTHORIZED
```

House gates: not run — the card header carries `HOUSE A: none — overruled 2026-10-02 R47`, so PREFLIGHT runs no house gate and no probe (CHECK-HUB "NO OUTSIDE HOUSE").

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:

```
clock · date · 0 · Sun Oct  4 20:20:53 EDT 2026
status · git status --short --branch · 0 · ## ops/cobalt-guard-b-1004
head · git log --oneline -1; git log --stat --format=%h 3ecdd3dc..HEAD · 0 · (5 lines)
    bc0e88f3 docs(cobalt-guard-b): build report — 3ecdd3dc
    bc0e88f3
    
     .../reports/cobalt-guard-b-build-2026-10-04.md     | 68 +++++++++++++++++++---
     1 file changed, 61 insertions(+), 7 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/cobalt-guard-b-1004/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/cobalt-guard-b-1004/docs/40 - DevDocs/reports/cobalt-guard-b-build-2026-10-04.md" · 0 · BUILT · job: cobalt-guard-b · tip: 3ecdd3dc | on 979ec797 | migration: none | offline 3782/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 9 of 9 | self-check: 3 of 3 | decisions: 4 · for Dejan: 0
range · git log --oneline 979ec797..3ecdd3dc · 0 · (14 lines)
    3ecdd3dc fix(cobalt-guard-b): an awk pipe segment is not a read-only filter (B11, L1 L72 L77)
    4edae759 wip(cobalt-guard-b): red — B11 tests on c74edcd3
    6a06a3ee docs(cobalt-guard-b): build report — c74edcd3
    c74edcd3 fix(cobalt-guard-b): awk file-reading constructs are G3; a wrapped command is judged as itself (B9 B10, L1 L72)
    67039e11 wip(cobalt-guard-b): red — B9 B10 tests on 8e68decd
    776d0a13 docs(cobalt-guard-b): build report — 8e68decd
    8e68decd fix(cobalt-guard-b): --co is compress-program; G3 reads option values (B7 B8, L1 L72)
    1218375f wip(cobalt-guard-b): red — B7 B8 tests on 1f2c19a9
    1f2c19a9 fix(cobalt-guard-b): a lone sort uniq awk by path or behind NAME= meets B4 (check O1)
    f5815a0e wip(cobalt-guard-b): check red — O1
    a9fe5090 docs(cobalt-guard-b): build report — 3c451126
    3c451126 fix(cobalt-guard-b): pin the house-probe ending on a lone sort (B4, K25 2)
    87576deb fix(cobalt-guard-b): read-only filters stay read-only; sort cut uniq awk read no .env (B1-B4, L1 L3 L72)
    82c5c7a2 wip(cobalt-guard-b): red — B1–B4 tests on BASE
PREFLIGHT OK
```

- THE RANGE typed: `git log --stat --format=%h 979ec797..3ecdd3dc` · exit 0 · path union: `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py`, `docs/40 - DevDocs/reports/cobalt-guard-b-build-2026-10-04.md`.
- DB: none: `git diff --name-only --no-renames 979ec797..3ecdd3dc` · exit 0 · whole:
  ```
  docs/40 - DevDocs/reports/cobalt-guard-b-build-2026-10-04.md
  ops/desk/bare-guard.py
  tests/ops/test_bare_guard.py
  ```
  every path under `ops/`, `tests/ops/` or `docs/`.
- `ls <S>` · exit 0 · `opus-1.md` (708 bytes, 19:26, from an earlier round of this job; this launch carries no `CONTINUE:`, the r3 report did not exist (`ls` exit 1, "No such file or directory"); not opened — earlier checks of this branch are not on the read list; overwritten at `## 8`).
- house A: none (overruled 2026-10-02 R47) · house B, if needed: none available (no probe run).

## Files copied
none — no house (overruled 2026-10-02 R47).

## OWN FINDINGS
Written from my read of the card, the diff `979ec797..3ecdd3dc`, `ops/desk/bare-guard.py` and `tests/ops/test_bare_guard.py` at the tip, the build report's `## RESTARTS`, `## W`, `## FOR THE CHECK` and last line, and `areas/cobalt.md` (the two sections). Nothing was run before this section was written.

FINDING O1
ROW: B2, B4 (sort/uniq, lone and in a pipe)
CLAIM: `sort_writes` and `uniq_writes` (`ops/desk/bare-guard.py:483`, `:499`) read each word as `shlex` returns it, but the shell brace-expands an unquoted `{a,b}` word first; `sort {-o,out} f` runs as `sort -o out f` and `uniq {f,out}` as `uniq f out`. The guard already reads braces for G3 (`braces`, `:675`), but not for B2/B4. So a write passes in a lone command and in a pipe segment.
RUN: TEST — `tests/ops/test_bare_guard.py`:
```python
@pytest.mark.parametrize(
    "command,found",
    [
        ("sort {-o,out} f", SORT_FOUND),
        ("grep X f | sort {-o,out}", SORT_FOUND),
        ("uniq {f,out}", UNIQ_FOUND),
        ("grep X f | uniq {-,out}", UNIQ_FOUND),
    ],
)
def test_check_b_r3_o1_a_brace_word_that_expands_to_a_write_is_denied(roots, command, found):
    assert_resend(run(command, make_seat(roots, "build")), found)
```
EXPECT: each id fails `assert 0 == 2` in `assert_resend`.

FINDING O2
ROW: B2, B4 (sort, lone and in a pipe)
CLAIM: the scanner reads `$'…'` ANSI-C quotes (`bare-guard.py:164`), but `words` (`:211`) uses `shlex.split`, which turns `$'-o'` into `$-o`; bash runs it as `-o`. `sort_writes` (`:494`) tests `a.startswith("-")`, so `sort $'-o' out f` and `grep X f | sort $'\x2do' out` are allowed and write `out`.
RUN: TEST — `tests/ops/test_bare_guard.py`:
```python
@pytest.mark.parametrize("command", ["sort $'-o' out f", "grep X f | sort $'\\x2do' out"])
def test_check_b_r3_o2_an_ansi_c_quoted_sort_output_is_denied(roots, command):
    assert_resend(run(command, make_seat(roots, "build")), SORT_FOUND)
```
EXPECT: each id fails `assert 0 == 2`.

FINDING O3
ROW: B1, B8 (sort reads no `.env`)
CLAIM: B8 tests the value of `--files0-from` with `is_env` (`env_words`, `bare-guard.py:693`); the value `-` means "the file names come from standard input", which the guard cannot read. A pipe of read-only filters can build the name `/x/wt/job/.env` on its input (`grep -o` with `[.]env`, which `is_env` does not match, `head -c`, `sort -z`), and `sort --files0-from=-` then prints that file whole. G1 and G3 both allow it.
RUN: TEST — `tests/ops/test_bare_guard.py`:
```python
def test_check_b_r3_o3_sort_with_file_names_from_its_input_is_denied(roots):
    target = roots.tmp / "target"
    target.write_text("B=2\nA=1\n")
    shown = subprocess.run(
        ["sort", "--files0-from=-"], input=str(target).encode() + b"\0", capture_output=True, timeout=60
    )
    assert shown.stdout == b"A=1\nB=2\n"  # sort prints the file its input names
    command = "grep -o -m1 '/x/wt/job/[.]env' f | head -c 14 | sort -z | sort --files0-from=-"
    assert_denied(run(command, make_seat(roots, "build")), G3_ROUTE)
```
EXPECT: the subprocess line passes; the guard line fails `assert 0 == 2` in `assert_denied`.

FINDING O4
ROW: SCOPE (suite lines)
CLAIM: the build report `## W` (fourth pass) quotes the offline gate log line 828 as `3782 passed, 755 skipped, 1 xfailed, 36 warnings in 597.55s (0:09:57)`.
RUN: COMMAND — `grep -n -F "3782 passed" /Users/cobalt/cobalt-wt/.gate-logs/cobalt-guard-b-1004-offline-20261004-200937.log`
EXPECT: if the claim is false, no line, or a line number other than 828.

## Findings
none — no house.

## Dropped
none.

## RUNS
Run with `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_bare_guard.py -k check_b_r3` (the three tests as written above) → `7 failed, 529 deselected, 15 warnings in 1.33s`.

| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `-k check_b_r3`, 4 ids | each `E assert 0 == 2` at `tests/ops/test_bare_guard.py:996` (`assert_resend`), `returncode=0, stderr=''` | HELD |
| O1 (extended) | Opus | after the first run I added the brace *sequence* form of O1 before the red commit, as two tests: `sort -{n..p} f`, `uniq {1..2}` (B2/B4) and `sort /x/wt/job/.{d..f}nv` (B1); `-k "check_b_r3 and sequence"` → `3 failed, 535 deselected` | the two writes: `E assert 0 == 2` at `:996`; the `.env` id: `E AssertionError: (0, '')` at `:268` (`assert_denied`) | HELD |
| O2 | Opus | `-k check_b_r3`, 2 ids | each `E assert 0 == 2` at `:996`, `returncode=0, stderr=''` | HELD |
| O3 | Opus | `-k check_b_r3` | `E AssertionError: assert b'' == b'A=1\nB=2\n'` at `:1247`: on this machine `sort --files0-from=-` printed nothing, so the claim's first step (that sort prints the file its input names) did not hold | NOT HELD — red for another reason; the test was removed with the Edit tool |
| O4 | Opus | `grep -n -F "3782 passed" /Users/cobalt/cobalt-wt/.gate-logs/cobalt-guard-b-1004-offline-20261004-200937.log` | `828:…3782 passed…, …755 skipped…, …1 xfailed…, …36 warnings… in 597.55s (0:09:57)` (colour codes left out) | NOT HELD — the report's line is the log's line 828 |

Red commit: `54d955d2 wip(cobalt-guard-b): check red — r3 O1 O2` (`tests/ops/test_bare_guard.py`, 38 insertions).

## FIXES
| id | fix | file | after |
|---|---|---|---|
| O1 | `braces` (`ops/desk/bare-guard.py`) now also expands `{a..b[..step]}` letter and number sequences (at most 256 items); `filter_problem` brace-expands each word before `sort_writes`, `uniq_writes` and `awk_file` (empty alternatives dropped, as bash drops them). G11's `awk_writes` still reads the raw words. | `ops/desk/bare-guard.py` | `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_bare_guard.py` → `538 passed, 15 warnings in 16.64s` |
| O2 | `words` decodes each `$'…'` outside quotes into the single-quoted text bash makes of it (`unquote_ansi_c`, `ansi_c`: `\a \b \e \E \f \n \r \t \v \\ \' \" \?`, octal, `\x`, `\u`, `\U`, `\c`) before `shlex`. This is one word reader for every rule (L3), so G3, G4 and G7 now read `$'…'` as the shell does too. It can only add denies: a word that matched before still matches. | `ops/desk/bare-guard.py` | same run |
| controls | `test_check_b_r3_a_brace_or_ansi_c_read_stays_allowed`: `sort {a,b}`, `sort -{n,u} f`, `sort $'-u' f`, `grep X f \| uniq $'-c'`, `uniq {f,}` | `tests/ops/test_bare_guard.py` | `543 passed, 15 warnings in 17.05s` |

Fix commit: `47ec01c5 fix(cobalt-guard-b): words read as the shell runs them — $'…' decoded, braces and sequences expanded for B2-B4 (check r3 O1 O2)`. DevDocs line: none. `ops/desk/bare-guard.py` has no page under `docs/40 - DevDocs/cobalt/` (Glob `docs/40 - DevDocs/cobalt/**/*guard*` → only `modelaccess/guard.md`, `redact/guard.md`, `session/guard.md`, which are other modules), and the card fences every other file.

## Suites
On `<tip now>` = `47ec01c5`. RESTARTS first, `uv run cobalt jobs restarts 979ec797..HEAD` → exit 0, whole:
```
path	change	rule	restart
docs/40 - DevDocs/reports/cobalt-guard-b-build-2026-10-04.md	A	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```
W for a "DB: none" card ((a0), (a), (e)):
- (a0) `git diff --name-only --no-renames 979ec797` → `docs/40 - DevDocs/reports/cobalt-guard-b-build-2026-10-04.md` · `ops/desk/bare-guard.py` · `tests/ops/test_bare_guard.py`. Every path is under `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 3 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh cobalt-guard-b-1004 offline` → exit 0, verdict `offline 3782/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/cobalt-guard-b-1004-offline-20261004-202831.log`. Log line 828: `3782 passed, 755 skipped, 1 xfailed, 36 warnings in 579.54s (0:09:39)`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh cobalt-guard-b-1004 livenote` → exit 0, verdict `live-note 146/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/cobalt-guard-b-1004-livenote-20261004-202832.log`. Line 57: `146 passed, 1 skipped, 15 warnings in 28.41s`. Its only skip is line 56, `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, and no skip names `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 0, `1348 passed, 1 xfailed, 15 warnings in 342.43s (0:05:42)`. The check's tests are in this run: the 5 functions at `tests/ops/test_bare_guard.py:1232`, `:1244`, `:1248`, `:1254`, `:1261`.
- With-DB: not run (DB: none). `.env`: `ls /Users/cobalt/cobalt-wt/cobalt-guard-b-1004/.env` → `No such file or directory` (20:38 ET).

## Scope
PREFLIGHT path union: `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py`, `docs/40 - DevDocs/reports/cobalt-guard-b-build-2026-10-04.md`. My commits: `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py`. Both files are in every row's `files`. Nothing else was written in the worktree.

## Checked against the branch
- (i) `git log --oneline 3ecdd3dc..HEAD -- . ":(exclude)docs"` → `47ec01c5 fix(cobalt-guard-b): words read as the shell runs them — $'…' decoded, braces and sequences expanded for B2-B4 (check r3 O1 O2)` · `54d955d2 wip(cobalt-guard-b): check red — r3 O1 O2`. `<tip now>` = `47ec01c5`.
- (ii) `git log --stat --format=%h 3ecdd3dc..HEAD` → `47ec01c5`: `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py`; `54d955d2`: `tests/ops/test_bare_guard.py`; `bc0e88f3`: the build report (docs). Every non-docs path is a row's file. No WIDENED line.
- (iii) The fence names no path but the two files. Its hub texts and launch lines: `git log --oneline 979ec797..HEAD -- "docs/40 - DevDocs/prompts"` → empty.
- (iv) `grep -n -F "def test_check_b_r3_" tests/ops/test_bare_guard.py` → `1232:` (O1 words) · `1244:` (O1 sequences) · `1248:` (O1 sequence `.env`) · `1254:` (O2) · `1261:` (the controls, added in the fix commit). The red commit `54d955d2` sits below the fix commit `47ec01c5` in (i).
- (v) `ls /Users/cobalt/cobalt-wt/cobalt-guard-b-1004/.env` → `No such file or directory`; `git status --short --branch` → `## ops/cobalt-guard-b-1004` alone.
- (vi) `git log --stat --format=%h 979ec797..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no migration and no with-DB test, so no gate-list line is owed (`git log --oneline 979ec797..HEAD -- ops/desk/gate-lists.md` → empty).
- (vii) No card `## RECORDS` line names an `ls`, a `grep` or a `git -C /Users/cobalt/cobalt log` command. Nothing to re-run.
- (viii) L32: this report holds constructed test values only (`/x/wt/job/.env`, `out`, `f`, `A=1`, `B=2`).

COUNTING: findings 4 (O1–O4; no house) · dropped 0 · held 2 (O1, O2) · fixed 2 · held unfixed 0 · open 0.

## OPEN
none.

## CONTINUE
next: none (pass 1 done; house B not needed).

## DECISIONS
1. ASK DESK [20:38 ET]: O2's fix decodes `$'…'` in `words`, which every Bash rule reads. That includes G3, G4 and G7, which the fence says "stand as built at `a2e19ceb`". The fence forbids a new rule. This change adds no rule: it makes the one word reader (L3) read a word the way the shell runs it, as the scanner's own header already says it does. It can only add denies, since a word that matched before still matches. Two examples: `cat $'.env'` and `git $'push'` are now denied, and before the fix they were allowed. Safe default taken: the change is kept, because the other choice is a second word reader for B2–B4 alone, and that leaves the G3 hole open. Not for Dejan. If the desk reads it as widening, reverting the `words` line in `47ec01c5` leaves O1 fixed and puts O2 back as HELD, NOT FIXED.

## RECORDS
- No house: the card header reads `HOUSE A: none — overruled 2026-10-02 R47`. PREFLIGHT ran no house gate and no probe. `## 1` and `## 3` were not run.
- Dropped findings: none. No house produced or failed to produce a list (none was launched).
- `<S>` held an `opus-1.md` (708 bytes, 19:26) from an earlier round of this job. Opening it would mean reading an earlier check of this branch, which the read list forbids, and the Write tool cannot overwrite a file it has not read. So my sections went to `<S>/opus-1-r3.md`, which points to this report. House B is not needed, so no pass 2 reads it.
- A carried read, not held: O3's chain (a pipe of read-only filters builds a `.env` path on `sort --files0-from=-`'s input). It did not hold on this machine's `sort`, which printed nothing for `--files0-from=-`. A GNU sort may read names from stdin. Should GNU coreutils ever sit first on the PATH, re-running O3's test (its text is under `## OWN FINDINGS`) settles it.
- REFUSED, not needed: none. CONTINUED: none. Extra lock takes: none (DB: none).
- L74: one system reminder at session start asked for a `Claude-Session:` line in commits. It was not acted on, and `54d955d2` and `47ec01c5` carry `Co-Authored-By` only.
- Files opened: 7 — `CHECK-HUB.md`; the card; `ops/desk/bare-guard.py`; `tests/ops/test_bare_guard.py`; the build report (its `## RESTARTS`, `## W`, `## PRE-STOP SELF-CHECK`, `## FOR THE CHECK`, `## DECISIONS`, `## RECORDS` and last line); `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); `BUILD-HUB.md` (`## W`, and its heading list). Read by `grep` or `tail` only: the three gate logs named above and the background task outputs.
- Check of `cobalt-guard-b`, pass 1: no outside house (overruled 2026-10-02 R47) and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: cobalt-guard-b · pass: 1 · tip: 47ec01c5 · house A: none (overruled 2026-10-02 R47) · findings: 4 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3782/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 7 · ready: YES · decisions: 1 · for Dejan: 0
