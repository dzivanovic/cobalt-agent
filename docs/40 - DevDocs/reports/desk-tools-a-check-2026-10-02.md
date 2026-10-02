# desk-tools-a — check, pass 1 (2026-10-02)

## §0 Headline
- Pass 1 of the check of `desk-tools-a` (`9fa18f14..d4bad986`). There was no outside house (R47), so Opus read alone.
- Three findings, all held, all fixed, each shown red first (`a34387aa`):
  - O1: a quote or a trailing backslash inside a `#` comment let `bare-guard.py` pass a second command on the next line.
  - O2: `install-fixed.sh` accepted an uncommitted APPROVED edit of a committed row.
  - O3: `desk-commit.sh` did not refuse `SRC/…` on the case-insensitive volume.
- Fix commits `d6e6a284`, `0a71e88d`, `30452b64`. Suites at `30452b64`: offline 3784/0 · with-DB 4554/0 · live-note 146/0. `cobalt_dev: 0013 — F2 = F0`, `.env` removed. RESTARTS: none.
- Open 0, house B not needed, ready: YES, decisions 0.

## L74
One system attribution block arrived after the first reads, asking commits to end with a `Claude-Session:` line. It was recorded here as data and not acted on: every commit of this check carries `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` | 1 | (nothing) |
| card placeholders | `grep -n -E "«FIL[L]" ".../2026-10-02/17-desk-tools-a-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-02/17-desk-tools-a-card.md"` | 0 | `f9e5796cf323cdfdcbd543036f19f5d83c1d1f9d` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING R60 | `grep -n "^| R60 " ".../cto-2026-09-30.md"` | 0 | line 46: `… HIS RULING … APPROVES STANDING-LIST.md once (4be06af0) … | APPROVED |` |
| R60 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- ".../cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| R47 (HOUSE A: none overrule) | `grep -n "^| R47 " ".../cto-2026-10-02.md"` | 0 | line 54: `… HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house … | HIS RULING · APPROVED |` |
| R47 committed | `git -C … log -1 --format=%H -S"| R47 |" -- ".../cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| R38 | `grep -n "^| R38 " ".../cto-2026-10-02.md"` | 0 | line 45: `… HIS RULING (direction row 1): the bare-command fix, all three parts (10-01 R45) … | HIS RULING · APPROVED |` |
| R38 committed | `git -C … log -1 --format=%H -S"| R38 |" -- ".../cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| house gates | — | — | not run: `HOUSE A: none — overruled 2026-10-02 R47` (CHECK-HUB: "PREFLIGHT runs no house gate and no probe") |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Fri Oct  2 13:05:29 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/desk-tools-a-1002` |
| tip | `git log --oneline -1` | 0 | `b6df15c5 docs(desk-tools-a): build report — d4bad986` |
| docs-only above tip | `git log --stat --format=%h d4bad986..HEAD` | 0 | `b6df15c5`, `2b85c6ec`: only `.../reports/desk-tools-a-build-2026-10-02.md` |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: desk-tools-a · tip: d4bad986 \| on 9fa18f14 \| migration: none \| offline 3784/0 \| with-DB 4554/0 \| live-note 146/0 \| cobalt_dev: 0013 \| .env: removed \| RESTARTS: none \| rows: 6 of 6 \| self-check: 3 of 3 \| decisions: 1 · for Dejan: 0` |
| range | `git log --oneline 9fa18f14..d4bad986` | 0 | `d4bad986 feat(desk-tools-a): …(A1-A6, L1, L3, L42)` · `e00b120f wip(desk-tools-a): red — six desk scripts, no such file yet (A1-A6)` |
| range paths | `git log --stat --format=%h 9fa18f14..d4bad986` | 0 | d4bad986: `ops/desk/{bare-guard.py,card-fill.sh,desk-commit.sh,desk-done.sh,desk-row.sh,desk-watch.sh,install-fixed.sh}`, `tests/ops/test_bare_guard.py`; e00b120f: `tests/ops/test_{bare_guard,card_fill,desk_done,desk_row,desk_watch,install_fixed}.py` |
| lock (own) | `ls <WT>/.env` | 1 | `No such file or directory` |
| lock (all) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| houses | — | — | `house A: none (overruled 2026-10-02 R47)`; no probe |

## Files copied
none — no outside house (R47).

## OWN FINDINGS
Written before any run. No house list exists (R47).

FINDING O1
ROW: A1 (X1)
CLAIM: `ops/desk/bare-guard.py:61` opens a quote on any `'` or `"` outside quotes, and the scanner has no idea of a `#` comment. So an apostrophe or a double quote inside a shell comment opens a quote that never closes, and the newline after it is never seen. `ops/desk/bare-guard.py:54-56` also eats a newline that follows a backslash ending a comment. The shell ends a comment at the newline, so a second command on the next line runs. A row-1 BLOCK case ("two commands on two lines") then passes.
RUN: TEST — `tests/ops/test_bare_guard.py`
```python
@pytest.mark.parametrize("command", ["ls # it's\nls", 'ls # say "hi\nls', "ls # x\\\nls"])
def test_check_o1_a_comment_does_not_hide_the_newline_after_it(command):
    done = guard(bash(command))
    assert done.returncode == 2, done.stderr
    assert "a newline" in done.stderr
```
EXPECT: `assert 0 == 2` on each of the three cases.

FINDING O2
ROW: A6 (X4)
CLAIM: `ops/desk/install-fixed.sh:24-30` reads the row's `HIS RULING` / `APPROVED` from the WORK TREE. Its commit proof is only that some commit touched the string `| R<n> |` (`git log -S`). So a row committed as `HELD`, then changed to `APPROVED` without a commit, passes as an "approved, committed row".
RUN: TEST — `tests/ops/test_install_fixed.py`
```python
def test_check_o2_an_uncommitted_approval_of_a_committed_row_is_refused(desk):
    repo, fixed, day, env = desk
    day.write_text(DESK.replace("HIS RULING · HELD |", "HIS RULING · APPROVED |"))
    before = fixed.read_bytes()
    done = install(str(fixed), "2026-01-02", "R2", env=env)
    refused(done, fixed, before)
    assert "no approved, committed row" in done.stderr
```
EXPECT: `assert 0 == 1` (it installs line 1 on R2).

FINDING O3
ROW: A4
CLAIM: `ops/desk/desk-commit.sh:28-29` compares the top folder to `src`, `configs`, `ops` and `tests` case-sensitively. On the macOS case-insensitive volume, `SRC/x.py` resolves to the tracked `src/x.py` (`realpath` keeps the typed case). It is not refused, so `git add` stages `src/x.py`.
RUN: TEST — `tests/ops/test_desk_row.py`
```python
def test_check_o3_a_code_path_in_another_letter_case_is_refused_and_nothing_is_staged(desk):
    repo, today, env = desk
    (repo / "src" / "x.py").write_text("x = 2\n")
    head = git(repo, "rev-parse", "HEAD")
    done = run(COMMIT, "docs(desk): x", "SRC/x.py", env=env)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: "), done.stderr
    assert staged(repo) == []
    assert git(repo, "rev-parse", "HEAD") == head
```
EXPECT: the return code is not 1 (`0`, a commit of `src/x.py`), or `staged(repo)` holds `src/x.py`.

Asked and found clean on the read (no finding): X2 — the session is refused unless it is in `claude agents --json` and is not `brain*` / `cto-desk` (`ops/desk/desk-done.sh:39-57`), and a non-stop line refuses before any call (`:29-38`). X3 — the number is the file-wide max + 1 (`ops/desk/desk-row.sh:43,50`), and the row goes after the last row line before the first `## §5` (`:44-53`). X4 line 1 — `partition("\n")` keeps `rest` byte-equal (`ops/desk/install-fixed.sh:46,54`). X1 other forms — `$((1+1))`, a heredoc and a `#` comment holding an operator are blocked (over-blocking, which the row allows). A bar or redirect inside quotes passes, as do an escaped quote and quotes inside quotes (tests at `tests/ops/test_bare_guard.py:39-47`).

## Findings
none — no house A.

## Dropped
none.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_bare_guard.py::test_check_o1_a_comment_does_not_hide_the_newline_after_it` | `3 failed, 15 warnings in 1.04s`; first failing line `assert 0 == 2` (stderr `''`) on `ls # it's\nls`, `ls # say "hi\nls`, `ls # x\\\nls` | HELD |
| O2 | Opus | `uv run pytest … tests/ops/test_install_fixed.py::test_check_o2_an_uncommitted_approval_of_a_committed_row_is_refused` | `1 failed, 15 warnings in 0.92s`; `assert 0 == 1`; stdout `new line 1: # X-HUB — the fixed x file (DRAFT 3 · INSTALL: 2026-01-02 R2 of his approval of STANDING-LIST.md · R9)` | HELD |
| O3 | Opus | `uv run pytest … tests/ops/test_desk_row.py::test_check_o3_a_code_path_in_another_letter_case_is_refused_and_nothing_is_staged` | `1 failed, 15 warnings in 0.91s`; the exit was 1, but the first failing line is `assert done.stderr.startswith("REFUSED: ")` with stderr `error: pathspec 'SRC/x.py' did not match any file(s) known to git`. The script did NOT refuse a path under `src/` (row A4) and handed it to git; the staging half of EXPECT was not reached | HELD (the claim's "not refused" shown; its EXPECT's staging clause not reached, stated) |

The test forms needed no repair. Red commit: `a34387aa wip(desk-tools-a): check red — O1, O2, O3`.

## FIXES
| id | file | fix | proof | commit |
|---|---|---|---|---|
| O1 | `ops/desk/bare-guard.py` | outside quotes, a `#` at a word start (start of command, or after a space, tab or newline) skips to the next newline, and that newline is still scanned. A quote or backslash inside a comment no longer opens a quote or eats the newline; the header names the rule | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `128 passed, 15 warnings in 19.33s` | `d6e6a284` |
| O2 | `ops/desk/install-fixed.sh` | after the `-S` proof, `git -C $REPO show HEAD:<desk report>` must hold the exact row line (`grep -qxF`), else `REFUSED: no approved, committed row: … differs from its line at HEAD`; the header names it | same run | `0a71e88d` |
| O3 | `ops/desk/desk-commit.sh` | the top folder is compared lower-cased (`top.lower()`) | same run | `30452b64` |

DevDocs line: none written. No page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/` (`Grep "desk-commit|install-fixed|bare-guard|ops/desk"` there → only `jobs/restarts.md`, the restarts module's page), and a new page is outside the files this check writes (RECORDS).

## Suites
RESTARTS (before the suites): `uv run cobalt jobs restarts 9fa18f14..HEAD` → the table WHOLE:
```
path	change	rule	restart
docs/40 - DevDocs/reports/desk-tools-a-build-2026-10-02.md	A	DOCS	-
ops/desk/bare-guard.py	A	operator script; no Cobalt reader	-
ops/desk/card-fill.sh	A	operator script; no Cobalt reader	-
ops/desk/desk-commit.sh	A	operator script; no Cobalt reader	-
ops/desk/desk-done.sh	A	operator script; no Cobalt reader	-
ops/desk/desk-row.sh	A	operator script; no Cobalt reader	-
ops/desk/desk-watch.sh	A	operator script; no Cobalt reader	-
ops/desk/install-fixed.sh	A	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	A	test/documentation; no resident	-
tests/ops/test_card_fill.py	A	test/documentation; no resident	-
tests/ops/test_desk_done.py	A	test/documentation; no resident	-
tests/ops/test_desk_row.py	A	test/documentation; no resident	-
tests/ops/test_desk_watch.py	A	test/documentation; no resident	-
tests/ops/test_install_fixed.py	A	test/documentation; no resident	-
RESTARTS: none
```
W on `<tip>` = `30452b64`:
- (a) OFFLINE `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3784 passed, 673 skipped, 1 xfailed, 25 warnings in 595.72s (0:09:55)`; 0 failed, 0 errors → `<p>` = 3784. This check adds no test under `tests/cobalt` or `tests/taxonomy`. Its tests are in `tests/ops/` (`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `128 passed, 15 warnings in 19.33s`).
- (b) THE LOCK: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`. Then `cp /Users/cobalt/.env …/desk-tools-a-1002/.env` → 0. Then `ls -la …/*/.env` → one line, `-rw-------  1 cobalt  staff  2186 Oct  2 13:20 /Users/cobalt/cobalt-wt/desk-tools-a-1002/.env`; taken `13:20:16 EDT`. `<FP>` → `<F0>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`. `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → 36 tables, with `drc_events`, `drc_fills`, `drc_imports`, `drc_rows`, `drc_stated_books`, `legs`, `prediction_records` and `voice_turns` absent (`-`); `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`; `code: 30452b64 (clean)`. Level `0013`.
- (c) PASS 1 (background): THE PASS-1 COMMAND byte for byte, no added `--deselect` (this check adds no with-DB test) → `4383 passed, 7 skipped, 65 deselected, 3 xfailed, 31 warnings in 709.60s (0:11:49)`; 0 failed, 0 errors → `<d1>` = 4383. Every SKIPPED line: `tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev` · `tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged` · `tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof` · `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` · `tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read` · `tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft` · `tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof`.
- (c2) FORWARD `COBALT_ENV=dev uv run cobalt db migrate` (foreground) → `0001` … `0013_tunables_slug_nullable.sql`, then `0014_radar_handicap.sql` … `0022_prediction_records.sql`; 8 tables `CREATED`, every other `OK`, no `CHANGED`; `content UNCHANGED on every table.` **dev forward: APPLIED 13:32:55 EDT.** `<F1>` = `cols 893 · rels 44 · views_md5 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) PASS 2 (background): THE PASS-2 COMMAND byte for byte, nothing added → `171 passed, 1 deselected, 5 warnings in 220.14s (0:03:40)`; `grep -c -F "SKIPPED"` → 0; `grep -c -F "PASSED"` → 171 → `<d2>` = 171; `<d>` = 4383 + 171 = 4554.
- (c3r) This check adds no with-DB test and writes no ticker: no query owed. (c4) No migration added: not run.
- (f) ROLLBACK `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) → `0022_prediction_records.rollback.sql` … `0014_radar_handicap.rollback.sql`, newest first; 8 tables `DROPPED`, every other `OK`; `content UNCHANGED on every table.` `<F2>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`, equal to `<F0>` field for field → **cobalt_dev: 0013 — F2 = F0**. The lock's (d): `rm …/desk-tools-a-1002/.env` → 0; `ls …/desk-tools-a-1002/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; released `13:37:22 EDT`. `.env: removed, proven gone (W)`.
- (e) LIVE-NOTE, `.env` absent: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 25.89s`. The skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …`, which does not name `COBALT_LIVE_VAULT_ROOT` → `<l>` = 146.
- Lines: offline 3784/0 · with-DB 4554/0 · live-note 146/0 · `cobalt_dev: 0013` · `.env: removed` · `RESTARTS: none`.

## Scope
PREFLIGHT's path union (`9fa18f14..d4bad986`): seven `ops/desk/` scripts (A1–A6 files) and six `tests/ops/` files (A1–A6 tests). This check's commits add only `tests/ops/test_bare_guard.py`, `tests/ops/test_install_fixed.py` and `tests/ops/test_desk_row.py` (A1, A6 and A4 test files), plus `ops/desk/bare-guard.py` (A1), `ops/desk/install-fixed.sh` (A6) and `ops/desk/desk-commit.sh` (A4). Every path is in a row's `files`.

## Checked against the branch
- (i) `git log --oneline d4bad986..HEAD -- . ":(exclude)docs"` → `30452b64 fix(desk-tools-a): desk-commit refuses a code root in any letter case (check O3)` · `0a71e88d fix(desk-tools-a): install-fixed proves the row line stands at HEAD, not only in the work tree (check O2)` · `d6e6a284 fix(desk-tools-a): bare-guard reads a # comment to its newline, so a quote in it no longer hides a second line (check O1)` · `a34387aa wip(desk-tools-a): check red — O1, O2, O3`. `<tip now>` = `30452b64`.
- (ii) `git log --stat --format=%h d4bad986..HEAD` → `30452b64` `ops/desk/desk-commit.sh`; `0a71e88d` `ops/desk/install-fixed.sh`; `d6e6a284` `ops/desk/bare-guard.py`; `a34387aa` `tests/ops/test_bare_guard.py`, `tests/ops/test_desk_row.py`, `tests/ops/test_install_fixed.py`; `b6df15c5`, `2b85c6ec` the build report only. Every non-docs path is in a row's `files`: no WIDENED.
- (iii) `git log --oneline 9fa18f14..HEAD -- ops/desk/desk-launch.sh ops/desk/wait-stop-line.sh ops/desk/desk-context.sh ops/desk/pre-commit .claude/settings.json src configs` → empty.
- (iv) `grep -n -F "def test_check_o" tests/ops/test_bare_guard.py tests/ops/test_install_fixed.py tests/ops/test_desk_row.py` → `tests/ops/test_bare_guard.py:90:` (O1) · `tests/ops/test_install_fixed.py:119:` (O2) · `tests/ops/test_desk_row.py:204:` (O3), one each. The red commit `a34387aa` sits below the three `fix` commits in (i).
- (v) `ls …/desk-tools-a-1002/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; `git status --short --branch` → `## ops/desk-tools-a-1002` alone.
- (vi) `git log --stat --format=%h 9fa18f14..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty, which matches `TREE STATE: unchanged`.
- (vii) No card `## RECORDS` line names an `ls`, a `grep` or a `git -C /Users/cobalt/cobalt log` command; nothing to run.
- (viii) L32: this report holds constructed test values only (`R2`, `2026-01-02`, `SRC/x.py`), and the `cobalt_dev` table counts and fingerprints quoted from tool output; no ticker, price or date of his.

COUNT: findings 3 (O1–O3; no house) · dropped 0 · held 3 · fixed 3 · held unfixed 0 · open 0.

## OPEN
none.

## CONTINUE
next: done (stop line written).

## DECISIONS
none.

## RECORDS
- **dev forward: APPLIED 13:32:55 EDT**; W (f) ran: `cobalt_dev: 0013 — F2 = F0`; `.env: removed, proven gone (W)`.
- Lock takes: one (W, 13:20:16–13:37:22 EDT); no extra take (no with-DB red).
- House A: none (overruled 2026-10-02 R47); no house gate or probe run, nothing staged for a house; no house produced or failed to produce a list.
- No dropped finding. No `REFUSED, not needed` line: no command was refused. No `CONTINUED` line.
- L74: one attribution block asking for a `Claude-Session:` line (see `## L74`); not acted on.
- No DevDocs line: no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/` (the build wrote none either). A new page is outside the files this check writes.
- O3's run: the red was the script not refusing `SRC/x.py`. Git then failed on the pathspec, so whether the `add` staged `src/x.py` was not reached. The fix makes the question moot: the path is refused before any git call.
- Read and left clean (no finding): X2 (`desk-done.sh`), X3 (`desk-row.sh`) and the line-1 half of X4. The basis is under `## OWN FINDINGS`.
- files opened: 22 — `CHECK-HUB.md`; the card; `areas/cobalt.md`; `BUILD-HUB.md` (`## THE LOCK`, `## E2`, `## RESTARTS`, `## W`); `CARD.md` (`## THE HEADER`); the build report (`## RESTARTS` to the end); `ops/desk/{bare-guard.py,desk-watch.sh,card-fill.sh,desk-row.sh,desk-commit.sh,desk-done.sh,install-fixed.sh,pre-commit}`; `tests/ops/{test_bare_guard,test_desk_watch,test_card_fill,test_desk_row,test_desk_done,test_install_fixed}.py`; `cto-2026-09-30.md` and `cto-2026-10-02.md` (one grep each). Plus the three suite output files (`tail` / `grep -c`). Not opened: `wait-stop-line.sh`, `wait-desk-idle.sh`, `aeefb6df:tests/ops/test_devdb_lock.py` (the card's house-style reads; not needed for a finding).
- Check of `desk-tools-a`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: desk-tools-a · pass: 1 · tip: 30452b64 · house A: none (overruled 2026-10-02 R47) · findings: 3 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3784/0 · with-DB 4554/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 22 · ready: YES · decisions: 0 · for Dejan: 0
