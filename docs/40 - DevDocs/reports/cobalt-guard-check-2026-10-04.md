# cobalt-guard — check, pass 1 (2026-10-04)

## §0 Headline
- Check of `cobalt-guard`, pass 1. The tip moved from `21b9e21f` to `a2e19ceb`. No outside house took part (house A: none, overruled 2026-10-02 R47).
- 6 own findings. 4 held and were fixed: O1, a false deny of every deploy's `DEPLOYED` stop line; O2, `.env` reached by a glob, a brace or another case; O3, a whole-tree `git add` by another spelling; O6, a fixed file written in another case.
- 2 are open, rejected by the card's letter: O4, `sort -o` and `uniq <in> <out>` in a "read-only" pipe; O5, `.env` read by `sort`, `cut`, `uniq` or `awk`. O5 is FOR DEJAN, because those are the four strings waiting for his approval.
- Suites on `a2e19ceb`: offline 3739/0, `tests/ops` 968/0, live-note 146/0. DB: none. RESTARTS: none.

## L74
- At the start: an attribution block in the session context asked for a `Claude-Session:` URL line on commits. DATA (L74): recorded once, not acted on; `64380944` and `a2e19ceb` carry the `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` line only.

## AUTHORIZATION
Started 15:35:53 EDT (`date`).
- INSTALLED: `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` → exit 1, no output.
- CARD: `grep -n -E "«FIL[L]" ".../prompts/2026-10-03/10-cobalt-guard-card.md"` → exit 1, no output · `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/10-cobalt-guard-card.md"` → `b70e462e574dab7725b4fcc31a577d79eb3f7ba9` · `git -C /Users/cobalt/cobalt diff --stat -- <card>` → no output.
- STANDING LIST 2026-09-30 R60: `cto-2026-09-30.md:46` `| R60 | 15:15 ET | **HIS RULING** … | APPROVED |` · `-S"| R60 |"` → `962e9d1705b62a61821f62f4d7bf5d8131656e2a`.
- 2026-10-02 R47 (also the `HOUSE A: none — overruled` row): `cto-2026-10-02.md:54` `… | HIS RULING · APPROVED |` · `-S` → `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a`.
- 2026-10-03 R32: `cto-2026-10-03.md:38` `… | HIS RULING · APPROVED |` · `-S` → `a09f08622ac8522adce99096f5af18faaed9e2ca`.
- 2026-10-03 R33: `cto-2026-10-03.md:39` `… | HIS RULING · APPROVED |` · `-S` → `a09f08622ac8522adce99096f5af18faaed9e2ca`.
- 2026-10-03 R12: `cto-2026-10-03.md:18` `… | HIS RULING · APPROVED — pending fold |` · `-S` → `c32c93cb8ef290caddaaa6c767e0a970d8149a02`.
- House gates R17/R19: not run — house A: none (overruled 2026-10-02 R47), per `## THE FLOW` "NO OUTSIDE HOUSE".

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sun Oct  4 15:35:53 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/cobalt-guard-1004` |
| tip | `git log --oneline -1` | 0 | `13a75577 docs(cobalt-guard): build report — 21b9e21f` |
| docs-only above tip | `git log --stat --format=%h 21b9e21f..HEAD` | 0 | `13a75577` · `.../reports/cobalt-guard-build-2026-10-04.md | 133 +++…` (docs only) |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: cobalt-guard · tip: 21b9e21f \| on a8d8a848 \| migration: none \| offline 3739/0 \| with-DB 0/0 \| live-note 146/0 \| cobalt_dev: not taken \| .env: removed \| RESTARTS: none \| rows: 11 of 11 \| self-check: 3 of 3 \| decisions: 1 · for Dejan: 0` |
| range | `git log --oneline a8d8a848..21b9e21f` | 0 | `21b9e21f feat(…G9–G11…)` · `11adaf00 wip(cobalt-guard): red — G9–G11 tests…` · `b31120b4 docs(…) build report — 28276443` · `28276443 feat(…G1–G8…)` · `78561316 wip(cobalt-guard): red — G1–G8 tests on the old guard` (5 commits) |
| range stat | `git log --stat --format=%h a8d8a848..21b9e21f` | 0 | 21b9e21f `ops/desk/bare-guard.py` 50 · 11adaf00 `tests/ops/test_bare_guard.py` 146 · b31120b4 build report 220 · 28276443 `ops/desk/bare-guard.py` 607, `tests/ops/test_bare_guard.py` 8 · 78561316 `tests/ops/test_bare_guard.py` 648 |
| lock (DB: none) | `ls <WT>/.env` | 1 | `ls: …/cobalt-guard-1004/.env: No such file or directory` |
| DB: none diff | `git diff --name-only --no-renames a8d8a848..21b9e21f` | 0 | `docs/40 - DevDocs/reports/cobalt-guard-build-2026-10-04.md` · `ops/desk/bare-guard.py` · `tests/ops/test_bare_guard.py` — all under `ops/`, `tests/ops/`, `docs/` |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| houses | — | — | house A: none (overruled 2026-10-02 R47); no gate, no probe |

Path union for `## Scope`: `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py`, `docs/40 - DevDocs/reports/cobalt-guard-build-2026-10-04.md`.

## Files copied
none — house A: none; `## 1` not run.

## OWN FINDINGS
Written before any run; no house list exists (house A: none). Tests go in `tests/ops/test_bare_guard.py` and use its own fixtures and helpers (`roots`, `make_seat`, `run`, `call`, `write`, `report`, `assert_denied`, `assert_allowed`, the route constants).

FINDING O1
ROW: G6 (X1, X3)
CLAIM: `ops/desk/bare-guard.py:593` denies any stop line while `<cwd>/.env` exists, but the deploy seat's cwd is `/Users/cobalt/cobalt` (`ops/desk/desk-launch.sh:46`; `DEPLOY-HUB.md:42`, `:116` "`ls -la /Users/cobalt/cobalt/.env` (listed = cwd back)"), whose `.env` is the lock's permanent source (`ls -la /Users/cobalt/cobalt/.env` → `-rw-------  1 cobalt  staff  2186 Sep  9 16:58 /Users/cobalt/cobalt/.env`). Every `DEPLOYED` stop line (`DEPLOY-HUB.md:185`) is denied, and the route ("release the lock") cannot clear it. The same holds for a build or check whose cwd is the repo (X2).
RUN: TEST
```python
def test_check_guard_o1_the_repos_own_env_does_not_make_a_seat_dirty(roots):
    # the deploy seat sits in the repo (desk-launch.sh:46); the repo's .env is the lock's source
    seat = make_seat(roots, "deploy")
    (roots.repo / ".env").write_text("CONSTRUCTED=1\n")
    assert_allowed(write(report(roots), seat, "# r\nDEPLOYED · job: x\n"))
    # its gate worktree's copy still makes it dirty
    (roots.wt / JOB_WT).mkdir(parents=True, exist_ok=True)
    (roots.wt / JOB_WT / ".env").write_text("CONSTRUCTED=1\n")
    assert_denied(write(report(roots), seat, "# r\nDEPLOYED · job: x\n"), G6_ROUTE)
```
EXPECT: on the tip, the first `assert_allowed` fails: `AssertionError: route: release the lock (W (f)), then the stop line`.

FINDING O2
ROW: G3 (X1)
CLAIM: `ops/desk/bare-guard.py:524-525` matches `.env` only as the literal last path word, so a word the shell expands to `.env` (`.en?`, `.env*`, `{.env,x}`) or that names it on this case-insensitive filesystem (`.ENV`; `ls -la ".../prompts/check-hub.md"` lists `CHECK-HUB.md`'s 40359 bytes) passes `cat`/`head`/the Read tool.
RUN: TEST
```python
@pytest.mark.parametrize(
    "command",
    ["cat /x/wt/job/.en?", "cat /x/wt/job/.env*", "cat /x/wt/job/{.env,x}", "head -1 /x/wt/job/.ENV"],
)
def test_check_guard_o2_a_word_that_names_env_after_expansion_is_denied(roots, command):
    assert_denied(run(command, make_seat(roots, "build")), G3_ROUTE)


def test_check_guard_o2_the_read_tool_on_env_in_another_case_is_denied(roots):
    assert_denied(call("Read", {"file_path": "/x/wt/job/.ENV"}, make_seat(roots, "build")), G3_ROUTE)


@pytest.mark.parametrize("command", ["cat /x/wt/job/.env.*", "grep -n X *", "cat /x/wt/job/{.env.example,x}"])
def test_check_guard_o2_a_pattern_that_cannot_name_env_stays_allowed(roots, command):
    assert_allowed(run(command, make_seat(roots, "build")))
```
EXPECT: on the tip, each id of the first test and the Read test fails `assert 0 == 2`; the control passes.

FINDING O3
ROW: G4 (X1)
CLAIM: `ops/desk/bare-guard.py:554-555` denies `add` only for the words `.`, `--all` and a short flag holding `A`, so the same whole-tree add by another spelling — `./`, `:/` (the top of the tree), `--no-ignore-removal` (git's alias of `--all`) — passes from a worker.
RUN: TEST
```python
@pytest.mark.parametrize(
    "command", ["git add ./", "git add -- ./", "git add :/", "git add --no-ignore-removal"]
)
def test_check_guard_o3_a_whole_tree_add_by_another_spelling_is_denied(roots, command):
    assert_denied(run(command, make_seat(roots, "build")), G4_ROUTE)
```
EXPECT: on the tip, each id fails `assert 0 == 2`.

FINDING O4
ROW: G1 (X1)
CLAIM: `ops/desk/bare-guard.py:395-403` checks options only for `sed` and `awk`; `sort -o`/`--output=` writes a file, `sort --compress-program=` runs a program, and `uniq`'s second operand is an output file, so a "read-only pipe" can write.
RUN: TEST
```python
@pytest.mark.parametrize(
    "command",
    [
        "grep X f | sort -o out",
        "grep X f | sort --output=out",
        "grep X f | sort --compress-program=sh",
        "grep X f | uniq - out",
    ],
)
def test_check_guard_o4_a_filter_that_writes_or_runs_is_denied(roots, command):
    done = run(command, make_seat(roots, "build"))
    assert done.returncode == 2, done.stderr
```
EXPECT: on the tip, each id fails `assert 0 == 2`.

FINDING O5
ROW: G3 (X1; card `## RECORDS` the four read strings)
CLAIM: `ops/desk/bare-guard.py:73` lists `cat grep sed head tail less` as `.env` readers; `sort`, `cut`, `uniq`, `awk` — the four strings the card's `## RECORDS` puts up for his approval — print the file and pass.
RUN: TEST
```python
@pytest.mark.parametrize(
    "command",
    [
        "sort /x/wt/job/.env",
        "cut -c1- /x/wt/job/.env",
        "uniq /x/wt/job/.env",
        "awk 1 /x/wt/job/.env",
        "grep -n X f | sort /x/wt/job/.env",
    ],
)
def test_check_guard_o5_the_four_new_read_verbs_on_env_are_denied(roots, command):
    assert_denied(run(command, make_seat(roots, "build")), G3_ROUTE)
```
EXPECT: on the tip, each id fails `assert 0 == 2`.

FINDING O6
ROW: G5 (X1)
CLAIM: `ops/desk/bare-guard.py:607-610` compares the fixed-file name and folder case-sensitively; on this case-insensitive filesystem `prompts/build-hub.md` is `BUILD-HUB.md`, so the desk (no fence but the fixed files) or a build in its worktree writes a fixed file by another case.
RUN: TEST
```python
@pytest.mark.parametrize("kind", ["desk", "build"])
def test_check_guard_o6_a_fixed_file_in_another_case_is_denied(roots, kind):
    seat = make_seat(roots, kind)
    base = roots.repo if kind == "desk" else roots.wt / JOB_WT
    assert_denied(write(base / "docs" / "40 - DevDocs" / "prompts" / "build-hub.md", seat), G5_FIXED)
    assert_denied(write(base / "docs" / "40 - devdocs" / "PROMPTS" / "BUILD-HUB.md", seat), G5_FIXED)
    assert_denied(write(base / "x" / "laws.md", seat), G5_FIXED)
```
EXPECT: on the tip, the first `assert_denied` fails `assert 0 == 2` for both kinds.

X3 (walked, facts): BUILD-HUB and CHECK-HUB steps type no production string, no denied git verb (every commit carries `--`), no launcher but CHECK-HUB's three house strings (G9). DEVFIX-HUB names `COBALT_ENV=production` and git verbs only in its "never typed" lists (lines 3, 12, 14), and writes only its report. DEPLOY-HUB types no launcher (`grep` for a backticked `claude|codex|grok|agy ` → 0), its production strings and merges are deploy-allowed (G2, G4 exempt deploy), its `.env` calls are `ls -la` (lines 42–116) — and its stop line is O1.

## Findings
none — no house.

## Dropped
none.

## RUNS
Each test pasted into `tests/ops/test_bare_guard.py` as written above (no form repair) and run alone on the tip `21b9e21f` (`uv run pytest -q -rs -p no:cacheprovider --color=no [--tb=line] <file>::<test>` or `-k check_guard_o<n>`).

| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `::test_check_guard_o1_the_repos_own_env_does_not_make_a_seat_dirty` | `1 failed … in 0.97s`; first failing line `E       AssertionError: route: release the lock (W (f)), then the stop line` / `assert 2 == 0` at `assert_allowed(write(report(roots), seat, "# r\nDEPLOYED · job: x\n"))` | HELD |
| O2 | own | `-k check_guard_o2` | `5 failed, 3 passed, 444 deselected … in 1.03s`; each red `AssertionError: (0, '')` / `assert 0 == 2` (the four command ids and the Read `.ENV` test); the three controls passed | HELD |
| O3 | own | `-k check_guard_o3` | `4 failed, 448 deselected … in 0.91s`; each `AssertionError: (0, '')` / `assert 0 == 2` | HELD |
| O4 | own | `-k check_guard_o4` | `4 failed, 448 deselected … in 1.07s`; each `assert 0 == 2` at `test_bare_guard.py:974` | REJECTED — card G1: "allowed when … EVERY segment's first word is one of `grep sed cut sort uniq head tail wc awk` with `sed` only as `sed -n` and no `-i`, `w`, `e` flags"; the row limits options for `sed` only (and G11 for `awk`), so `sort -o` is allowed by its letter. Test removed again. OPEN |
| O5 | own | `-k check_guard_o5` | `5 failed, 447 deselected … in 1.07s`; each `AssertionError: (0, '')` / `assert 0 == 2` | REJECTED — card G3: "`cat`, `grep`, `sed`, `head`, `tail`, `less`, `Read` of a path ending `/.env` → deny"; the verb list is closed. Test removed again. OPEN |
| O6 | own | `-k check_guard_o6` | `2 failed, 450 deselected … in 0.98s`; each `AssertionError: (0, '')` / `assert 0 == 2` at the first `assert_denied` (`prompts/build-hub.md`) | HELD |

Red commit: `64380944 wip(cobalt-guard): check red — O1 O2 O3 O6` (`tests/ops/test_bare_guard.py`, 47 insertions).

## FIXES
| fix | ids | where | after |
|---|---|---|---|
| `g6`: the `<cwd>/.env` probe skips the repo root (`s["cwd"] != REPO_ROOT`); the seat's worktree `.env` and the lock owner still make it dirty | O1 | `ops/desk/bare-guard.py` `g6` | O1 green; its second half (gate worktree `.env` → deny) holds |
| `is_env`: brace alternatives (`braces`), then `fnmatch` of the lower-cased basename against `.env`, a leading dot matched only by a literal dot (so `grep -n X *` and `.env.*` stay allowed) | O2 | `is_env`, new `braces`, `import fnmatch` | O2 green, controls green |
| `git_problem` `add`: also `:/`, `--no-ignore-removal`, and any word whose `normpath` is `.` | O3 | `git_problem` | O3 green |
| `is_fixed`: `LAWS.md` and the `prompts/` folder compared lower-cased | O6 | `is_fixed` | O6 green |

`uv run pytest -q -p no:cacheprovider --color=no --tb=short -rfE tests/ops/test_bare_guard.py` → `443 passed, 15 warnings in 13.95s` (428 at the tip + 15 new ids). Commit: `a2e19ceb fix(cobalt-guard): repo .env not dirt, .env by expansion or case, whole-tree add spellings, fixed file in any case (check O1 O2 O3 O6)`. DevDocs line: no page for `ops/desk/` exists under `docs/40 - DevDocs/cobalt/` (the build's `## RECORDS`); none made (`## RECORDS`).

## Suites
On `<tip now>` = `a2e19ceb`. The card is DB: none, so W was run as (a0), (a), `tests/ops` and (e).
- RESTARTS: `uv run cobalt jobs restarts a8d8a848..HEAD` → `docs/40 - DevDocs/reports/cobalt-guard-build-2026-10-04.md A DOCS -` · `ops/desk/bare-guard.py M operator script; no Cobalt reader -` · `tests/ops/test_bare_guard.py M test/documentation; no resident -` · `RESTARTS: none`.
- (a0) `git diff --name-only --no-renames a8d8a848` → `docs/40 - DevDocs/reports/cobalt-guard-build-2026-10-04.md` · `ops/desk/bare-guard.py` · `tests/ops/test_bare_guard.py`. Every path is under `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 3 paths)`**
- (a) `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3739 passed, 745 skipped, 1 xfailed, 36 warnings in 583.89s (0:09:43)`. `grep -c -F "FAILED"` over the output → `0`. This check adds no test there.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` (background) → `968 passed, 1 xfailed, 15 warnings in 256.01s (0:04:16)`. That is 953 at the build tip plus the 15 ids added here.
- (e) `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.50s`. The skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, which does not name `COBALT_LIVE_VAULT_ROOT`.
- `.env`: `ls /Users/cobalt/cobalt-wt/cobalt-guard-1004/.env` → `No such file or directory` (15:53:48 EDT). It was never present.

## Scope
PREFLIGHT's union (`ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py`, the build report) plus my two commits (`ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py`): every non-docs path is a G1–G11 `files` path. Nothing under `## NOT IN THIS JOB`.

## Checked against the branch
- (i) `git log --oneline 21b9e21f..HEAD -- . ":(exclude)docs"` → `a2e19ceb fix(cobalt-guard): …(check O1 O2 O3 O6)` · `64380944 wip(cobalt-guard): check red — O1 O2 O3 O6`; `<tip now>` = `a2e19ceb`.
- (ii) `git log --stat --format=%h 21b9e21f..HEAD` → `a2e19ceb` `ops/desk/bare-guard.py | 33` · `64380944` `tests/ops/test_bare_guard.py | 47` · `13a75577` the build report (docs). Both non-docs paths are in the rows' `files`.
- (iii) NOT IN THIS JOB (hub text): `git log --oneline a8d8a848..HEAD -- "docs/40 - DevDocs/prompts"` → empty.
- (iv) `grep -n -F "def test_check_guard_o" tests/ops/test_bare_guard.py` → `928:` o1 · `943:` o2 expansion · `947:` o2 Read · `952:` o2 control · `959:` o3 · `964:` o6; `64380944` (red) sits below `a2e19ceb` (fix) in (i).
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/cobalt-guard-1004`.
- (vi) TREE STATE unchanged: `git log --stat --format=%h a8d8a848..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty.
- (vii) the card's `## RECORDS` name no `ls`, `grep` or `git -C` command.
- (viii) L32: this report holds constructed values only (`/x/wt/job/.env`, `CONSTRUCTED=1`, `model-x`).

## OPEN
- O4 · own · REJECTED — G1's letter. `grep X f | sort -o out`, `… | sort --output=out`, `… | sort --compress-program=sh`, `… | uniq - out` pass the hook (`4 failed … assert 0 == 2` on the tip, and on `a2e19ceb` unchanged): a "read-only pipe" that writes a file or runs a program. Settles by: a card row (as G11 did for `awk`) denying `sort -o`/`--output`/`--compress-program` and a second `uniq` operand in a pipe segment; the test above is its red.
- O5 · own · REJECTED — G3's letter. `sort`, `cut`, `uniq`, `awk` on `/x/wt/job/.env` pass the hook (`5 failed … assert 0 == 2`), and these are the four read strings the card's `## RECORDS` puts up for his approval. Settles by: a card row adding them to G3's readers (`ENV_READERS`) before those strings go on any line; the test above is its red.

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
1. **O4 — a read-only pipe can still write through `sort -o` or `uniq <in> <out>`, or run a program through `sort --compress-program`.** OPEN (REJECTED by G1's letter). No house B is available (house A: none, R47), so it ships to the follow-up list unless the judge orders a row. Safe default taken: built to the card's letter, nothing changed. Needed: a card row like G11.
2. **O5 — `.env` read by the four new read verbs. FOR DEJAN.** G3 names `cat grep sed head tail less`; `sort`, `cut`, `uniq`, `awk` print the file and pass. Those four are the strings waiting for his one approval (card `## RECORDS`). Safe default taken: nothing changed; the recommended order is a G3 row adding the four verbs before he approves the four strings, since secrets are never printed (cobalt.md, absolute boundaries).
3. **O1 — a reading for the judge to confirm.** G6 says "while `<cwd>/.env` exists". The deploy seat's cwd is `/Users/cobalt/cobalt`, whose `.env` always exists, so every `DEPLOYED` line was denied with a route that cannot clear it. I held it as a false deny (X1) and fixed it: the repo's own `.env` no longer counts; the seat's worktree `.env` and the lock owner still do. Safe default taken: fixed (`a2e19ceb`). If the letter is to stand, revert the one condition in `g6` and DEPLOY-HUB's stop line needs another route.

## RECORDS
- REFUSED, not needed: grep -n -o -E "(ls|ls -la|cat|cp|rm|test -f|grep)[^`]*\.env" "<DEPLOY-HUB.md>" — Permission to use Bash has been denied because Claude Code is running in don't ask mode. (a backtick in the pattern; read with the Grep tool instead)
- The build's DECISION 1 (`awk -f <file>` stays allowed) is the build's, carried in its report; not counted again here.
- No DevDocs page exists for `ops/desk/` under `docs/40 - DevDocs/cobalt/` (the build's record); none made for the fix.
- No lock taken (DB: none).
- Remaining after O2, for the file: a `$VAR`/`${…}` inside a path word (`cat /x/.${NOPE}env`) is not expanded by the hook; `grep -r` of a folder holding `.env` is not a G3 read by its letter.
- House A: none (overruled 2026-10-02 R47). No house was staged or launched; `<S>` holds only `opus-1.md`.
- Counts: findings 6 (own) · dropped 0 · held 4 (O1 O2 O3 O6) · fixed 4 · held unfixed 0 · open 2 (O4 O5). House B is needed by the count but none is available under the overrule; the open items are in `## DECISIONS`.
- files opened: 14. Read: `CHECK-HUB.md`, the card, `BUILD-HUB.md` (lines 28–99), the build report, `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py`, `areas/cobalt.md` (the two sections), `cto-2026-10-03.md` (REFUSALS), `harness-mods-review-2026-10-03.md` (`## OPERATIONS A HOOK CAN TAKE`), `ops/desk/desk-launch.sh` (lines 40–57), `DEPLOY-HUB.md` (grep and lines 42, 116), `DEVFIX-HUB.md` (lines 1–16). Grep only: `cto-2026-09-30.md`, `cto-2026-10-02.md`.
- Check of `cobalt-guard`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: cobalt-guard · pass: 1 · tip: a2e19ceb · house A: none (overruled 2026-10-02 R47) · findings: 6 · dropped: 0 · held: 4 · fixed: 4 · held unfixed: 0 · open: 2 · house B: none available · suites: offline 3739/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken (DB: none) · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 3 · for Dejan: 1
