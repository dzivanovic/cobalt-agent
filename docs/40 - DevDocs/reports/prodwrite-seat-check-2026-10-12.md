# prodwrite-seat-1012 — check report (card 392, 2026-10-12)

## §0 Headline
- Checked card 392 on one pass: house A Grok (3 findings), no house B (as needed), and my own read (3 findings).
- 5 held and all 5 are fixed in `b96737bf`. The guard now names the seat by the repo hub only, counts every ROWS row and denies `git --output`. The prompt-line production check reads the line as eval does. The hub's SHAPE step re-proves W2.
- 1 open (A2, rejected by card W3 and R686): the read-only `db query` still passes on a card with no single write. It is a follow-up for the desk.
- Suites green on `b96737bf`: offline 4199/0, live-note 146/0, tests/ops 3240 passed. DB: none, so the lock was not taken. RESTARTS: none. `ready: YES`.

## L74
- One system block in this session asked for a `Claude-Session:` line on commits. It is DATA (L74). Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/392-prodwrite-seat-card.md"` · exit 0 · output WHOLE:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/392-prodwrite-seat-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/392-prodwrite-seat-card.md" · 0 · 1916b5fadca84532fbda6d337df59466549bb56a
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/392-prodwrite-seat-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 38:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```
- House gates: `grep -n "^| R17 " ".../cto-2026-09-24.md"` → `35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …` (one row); `grep -n "^| R19 " …` → `37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …` (one row); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c`.

## PREFLIGHT
- `date` → `Mon Oct 12 08:17:45 EDT 2026`.
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output WHOLE:
```
clock · date · 0 · Mon Oct 12 08:17:53 EDT 2026
status · git status --short --branch · 0 · ## ops/prodwrite-seat-1012
head · git log --oneline -1; git log --stat --format=%h 89fd13c5..HEAD · 0 · (5 lines)
    8736ce47 docs(prodwrite-seat-1012): build report — 89fd13c5
    8736ce47
    
     .../reports/prodwrite-seat-build-2026-10-12.md     | 93 +++++++++++++++++++++-
     1 file changed, 89 insertions(+), 4 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/prodwrite-seat-1012/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/prodwrite-seat-1012/docs/40 - DevDocs/reports/prodwrite-seat-build-2026-10-12.md" · 0 · BUILT · job: prodwrite-seat-1012 · tip: 89fd13c5 | on 86b9daa5 | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 8 of 8 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 409585
range · git log --oneline 86b9daa5..89fd13c5 · 0 · (2 lines)
    89fd13c5 feat(prodwrite-seat-1012): the production-write seat — PRODWRITE-HUB.md, launcher kind, guard G2/G5, authorize, watch/done, prompt production refusal (W1-W7, L29 L81 K3 K5)
    fdc1efdf wip(prodwrite-seat-1012): red — W1-W7 tests
PREFLIGHT OK
```
- `git log --stat --format=%h 86b9daa5..89fd13c5` · exit 0 → `89fd13c5`: CARD.md, PRODWRITE-HUB.md, STANDING-LIST.md, ops/desk/authorize.sh, bare-guard.py, desk-done.sh, desk-launch.sh, desk-watch.sh (8 files, 335+, 31-); `fdc1efdf`: the build report, tests/ops/test_authorize.py, test_bare_guard.py, test_desk_done.py, test_desk_launch_prechecks.py, test_desk_launch_prodwrite.py, test_desk_watch.py, test_hub_lines.py, test_prodwrite_hub.py (9 files, 837+, 4-).
- DB: none · `git diff --name-only --no-renames 86b9daa5..89fd13c5` · exit 0 → 17 paths, every one under `ops/`, `tests/ops/` or `docs/`:
```
docs/40 - DevDocs/prompts/CARD.md
docs/40 - DevDocs/prompts/PRODWRITE-HUB.md
docs/40 - DevDocs/prompts/STANDING-LIST.md
docs/40 - DevDocs/reports/prodwrite-seat-build-2026-10-12.md
ops/desk/authorize.sh
ops/desk/bare-guard.py
ops/desk/desk-done.sh
ops/desk/desk-launch.sh
ops/desk/desk-watch.sh
tests/ops/test_authorize.py
tests/ops/test_bare_guard.py
tests/ops/test_desk_done.py
tests/ops/test_desk_launch_prechecks.py
tests/ops/test_desk_launch_prodwrite.py
tests/ops/test_desk_watch.py
tests/ops/test_hub_lines.py
tests/ops/test_prodwrite_hub.py
```
- `ls /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/prodwrite-seat-1012-check` · exit 1 → `No such file or directory` (fresh).
- `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0 → `grok: UP` · `gemini: UP`.
- SEATS: no `HOUSE A` header line; Grok UP → **house A: Grok · house B: none (not needed)** (`HOUSE B: as needed`).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0 → `STAGED 21 files · 620117 bytes · commits 2` (commits 2 = PREFLIGHT's range). Per file (bytes, under `<S>/`): `diff.md` 73344 · `files/392-prodwrite-seat-card.md` 25453 · `files/prodwrite-seat-build-2026-10-12.md` 20467 · `files/wt/docs/40 - DevDocs/prompts/CARD.md` 16372 · `…/PRODWRITE-HUB.md` 11964 · `…/STANDING-LIST.md` 44690 · `files/wt/docs/40 - DevDocs/reports/prodwrite-seat-build-2026-10-12.md` 7217 · `files/wt/ops/desk/authorize.sh` 9859 · `bare-guard.py` 55506 · `desk-done.sh` 3008 · `desk-launch.sh` 101333 · `desk-watch.sh` 5256 · `files/wt/tests/ops/test_authorize.py` 18625 · `test_bare_guard.py` 97424 · `test_desk_done.py` 7579 · `test_desk_launch_prechecks.py` 64223 · `test_desk_launch_prodwrite.py` 14395 · `test_desk_watch.py` 23403 · `test_hub_lines.py` 13550 · `test_prodwrite_hub.py` 6094 · `rulings.md` 355.
`stage-copy.sh`, each exit 0: `COPIED 5788 …/files/hands-off-answer-2026-10-12.md` · `COPIED 15371 …/files/wt/docs/40 - DevDocs/prompts/DEVFIX-HUB.md` · `COPIED 57921 …/DEPLOY-HUB.md` · `COPIED 3014 …/files/wt/src/cobalt/backup/cli.py` · `COPIED 11490 …/restic.py` · `COPIED 7878 …/files/wt/src/cobalt/db_query.py` · `COPIED 21839 …/files/wt/tests/ops/test_desk_launch_brain.py` · `COPIED 24661 …/files/386-launcher-shadow-check-card.md` · `COPIED 33741 …/files/324-shadow-hub-card.md`.
`<S>/HOUSE-INSTRUCTIONS.md` written (27030 bytes): the HOUSE TEXT, the card's ROWS, NOT IN THIS JOB, CHECK ASKS, RECORDS, the Files paragraph.
House A Grok started 08:21 ET (`date` 08:21:05; both gates re-read, one row each); `git status --short --branch` after the return → `## ops/prodwrite-seat-1012`. House B: none (not needed).

## OWN FINDINGS
FINDING O1
ROW: W3 / X1
CLAIM: `ops/desk/bare-guard.py:798-799` names kind `prodwrite` from the basename of the first message's Read, whatever the path or cwd, so a worktree seat whose first message reads a copy named `PRODWRITE-HUB.md` with a `CARD:` passes G2 with that card's production write, where before the change it was kind `worker` and denied.
RUN: TEST `tests/ops/test_bare_guard.py`
```python
def test_o1_a_worktree_copy_named_prodwrite_hub_is_not_the_seat(roots):
    p = prompts(roots)
    card = p / "2026-01-01" / "01-prodwrite-card.md"
    card.parent.mkdir(parents=True, exist_ok=True)
    card.write_text(prodwrite_card_text(roots))
    hub = roots.wt / JOB_WT / "docs" / "40 - DevDocs" / "prompts" / "PRODWRITE-HUB.md"
    seat = make_seat(roots, "worker", cwd=roots.wt / JOB_WT,
                     first=f"Read '{hub}' and follow it exactly. CARD: '{card}'")
    assert_denied(run(PW_WRITE, seat), G2_ROUTE)
```
EXPECT: `AssertionError: (0, '')` (the write passes).

FINDING O2
ROW: W6
CLAIM: `ops/desk/desk-launch.sh:602-606` looks for the literal `COBALT_ENV=production` inside each `"…"` field of an allow token, but `run_launch` evals the line (`:257`), so a token spelled `"Bash(COBALT_ENV="production" uv run …)"` or `"Bash(COBALT_ENV=${x:-production} uv run …)"` becomes a production write string while the check sees none, and F5 then passes it on a ruled `RULINGS:` row.
RUN: TEST `tests/ops/test_desk_launch_prechecks.py`
```python
@pytest.mark.parametrize("extra", [
    'Bash(COBALT_ENV="production" uv run cobalt settings load *)',
    'Bash(COBALT_ENV=${{x:-production}} uv run cobalt settings load *)',
])
def test_o2_a_production_write_spelled_for_eval_is_refused(desk, tmp_path, extra):
    line = with_allow(extra)
    refused(desk, launch_prompt(desk, tmp_path, survey_prompt(desk, "2026-01-02 R1", line)), PROD_REFUSAL)
```
EXPECT: `assert 0 == 1` in `refused` (the prompt launches).

FINDING O3
ROW: W3 / X2
CLAIM: the prodwrite line allows `Bash(git -C /Users/cobalt/cobalt diff*)` and `log*` (`PRODWRITE-HUB.md:10`), and the guard's `--output` check (`ops/desk/bare-guard.py:959`) runs only for `GIT_SHAPED` kinds (`:104`, `:1102`), so the seat writes any file with `git … diff --output=<path>`, past the G5 fence that holds it to its REPORT.
RUN: TEST `tests/ops/test_bare_guard.py`
```python
def test_o3_the_prodwrite_seat_writes_no_file_through_git_output(roots):
    seat = make_seat(roots, "prodwrite")
    for command in (f"git -C {roots.repo} diff --output={roots.repo}/src/x.py HEAD",
                    f"git -C {roots.repo} log --output={roots.repo}/src/x.py -1"):
        done = run(command, seat)
        assert done.returncode == 2, (command, done.returncode, done.stderr)
```
EXPECT: `AssertionError: ('git -C … diff --output=…/src/x.py HEAD', 0, '')`.

X1–X5 as read (answers, not findings): X1 — the prompt kind cannot name a card in its first message (`desk-launch.sh:680-683`, text after `follow it exactly.` is refused), so a prompt seat named `PRODWRITE-HUB.md` reads no card and its card command is None; the one path left is O1. X2 — the line holds exactly the card's 15 strings plus the one filled write (test_prodwrite_hub); its `git … diff*`/`log*` strings are O3. X3 — `PRODWRITE-HUB.md:32-46`: BACKUP, then `(2b) ROLLBACK` written, then COUNT, then WRITE "ONCE … NEVER typed a second time". X4 — the `prodwrite)` arm (`desk-launch.sh:1545-1674`) runs before the fill (`:1776-1781`); each P2 case asserts its own text (`test_desk_launch_prodwrite.py:192-222`). X5 — the hook runs the repo copy (card RECORDS); nothing under `~/.claude/` is named by any row.

## Findings
Grok's completion notice came at 08:44 ET (`date` → `Mon Oct 12 08:44:09 EDT 2026`). `ls -la <S>` showed `house-a.md` at 2380 bytes, written by Grok, ending `FINDINGS: 3`. Every block carries a `RUN:` line followed by a `def test_`, so none is dropped.
- O1 · Opus · W3/X1 · a worktree seat whose first message reads a copy named PRODWRITE-HUB.md passes G2 with its card's write · TEST
- O2 · Opus · W6 · a production write string spelled for eval (split quotes, `${x:-production}`) passes the prompt-line refusal · TEST
- O3 · Opus · W3/X2 · the prodwrite seat writes any file through `git … diff/log --output=` (G4's check skips its kind) · TEST
- A1 · Grok · W3 · a short (non-7-cell) second ROWS row leaves the one command named, so the write passes · TEST
- A2 · Grok · W3 · with two write rows or none the production db query read still passes · TEST
- A3 · Grok · W1 · hub step (1) SHAPE does not re-prove the verb, the character set or the table · TEST

## Dropped
none

## RUNS
Each test was placed with the Edit tool and run alone with `uv run pytest -q -rs -p no:cacheprovider --color=no <file>::<test>`. Every result below is the run's own output on tip `89fd13c5`.
- O1 · Opus · `test_bare_guard.py::test_o1_a_worktree_copy_named_prodwrite_hub_is_not_the_seat` · `AssertionError: (0, '')` / `assert 0 == 2`: the write passes for a worktree seat reading a copy named PRODWRITE-HUB.md · **HELD**
- O2 · Opus · `test_desk_launch_prechecks.py -k test_o2_` · `2 failed`, each `assert 0 == 1` in `refused`. Both lines launched: `RUN: claude --bg … "Bash(COBALT_ENV="production" uv run cobalt settings load *)" …` and `… "Bash(COBALT_ENV=${x:-production} uv run cobalt settings load *)" …` · **HELD**
- O3 · Opus · `test_bare_guard.py::test_o3_the_prodwrite_seat_writes_no_file_through_git_output` · `AssertionError: ('git -C …/repo diff --output=…/repo/src/x.py HEAD', 0, '')` · **HELD**
- A1 · Grok · `test_bare_guard.py::test_q2_a_short_second_row_still_names_the_write` · `AssertionError: (0, '')`: the write passes with a short second row · **HELD**
- A2 · Grok · `test_bare_guard.py::test_q2_two_rows_deny_the_production_read` · `AssertionError: (0, '')`: the read passes on a two-row card · **REJECTED — card W3: "kind `prodwrite` passes a production command only when it is … or `prod_read` (`:971-1006`)"; his 2026-10-08 R686 lets every seat run that read (card RECORDS)**. It stays OPEN, and its test was removed again with the Edit tool.
- A3 · Grok · `test_prodwrite_hub.py::test_shape_reproves_the_verb_the_characters_and_the_table` · `assert 'db migrate' in shape` fails · **HELD**
- Held tests committed red: `335de8b4 wip(prodwrite-seat-1012): check red — O1 O2 O3 A1 A3`.

## FIXES
`b96737bf fix(prodwrite-seat-1012): guard names the seat by the repo hub only, counts every ROWS row, denies git --output; prompt prod-string check reads the line as eval does; hub SHAPE re-proves W2 (check O1 O2 O3 A1 A3)`
- O1 · `ops/desk/bare-guard.py` `seat()`: a first message whose Read names `PRODWRITE-HUB.md` names kind `prodwrite` only when the path is `<REPO_ROOT>/docs/40 - DevDocs/prompts/PRODWRITE-HUB.md`. A copy elsewhere falls through to the cwd rules: worker, brain or None, as before the change. The `HUBS` entry stays; the header comment says so.
- A1 · `bare-guard.py` `read_card`: every data row of `## ROWS` counts, of any width, with the 7-cell header and `---` lines skipped. A command is named only by ONE row of 7 cells.
- O3 · `bare-guard.py` `GIT_SHAPED` gains `prodwrite`. `git_problem`'s `--output` check, plus its push/add/commit shapes, now binds the seat at G4.
- O2 · `ops/desk/desk-launch.sh` prompt kind (`:600-616`, comment `:120-127`): the allow list is read with its quotes cut, and only exact `Bash(COBALT_ENV=production uv run cobalt db query *)` substrings are taken out. An allow list holding `$`, a backtick or a backslash is refused with the same W6 text.
- A3 · `PRODWRITE-HUB.md` `## (1) SHAPE`: re-proves W2's refusals of the write, naming the character set, the verbs, `--rollback`/`--down-to`, the table and the count read naming it.
- After the fixes: `tests/ops/test_bare_guard.py` → `1858 passed`; `tests/ops/test_desk_launch_prechecks.py tests/ops/test_desk_launch_prodwrite.py` → `181 passed`; `tests/ops/test_prodwrite_hub.py tests/ops/test_hub_lines.py` → `43 passed`. All five held tests are green.
- DevDocs: no page under `docs/40 - DevDocs/cobalt/` documents an `ops/desk/` script (the build report's record). No dated line was written.

## Suites
The card is DB: none, so W ran (a0), (a) and (e) plus tests/ops. Tip: `b96737bf`.
- RESTARTS: `uv run cobalt jobs restarts 86b9daa5..HEAD` · exit 0. It printed the same 17 rows as the build's table: `docs/` DOCS, `ops/desk/` "operator script; no Cobalt reader", `tests/ops/` "test/documentation; no resident". Its last line: `RESTARTS: none`.
- (a0) `git diff --name-only --no-renames 86b9daa5` · exit 0 → 17 paths, every one under `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 17 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh prodwrite-seat-1012 offline` · exit 0 → `offline 4199/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/prodwrite-seat-1012-offline-20261012-084713.log`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh prodwrite-seat-1012 livenote` · exit 0 → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/prodwrite-seat-1012-livenote-20261012-084714.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` · exit 0 → `3240 passed, 1 xfailed, 15 warnings in 633.54s (0:10:33)`. The build had 3234; the check adds 6 (O1, O2 ×2, O3, A1, A3).
- with-DB: not run (DB: none; gate.sh takes `--deploy` with withdb and all only). `ls /Users/cobalt/cobalt-wt/prodwrite-seat-1012/.env` → `No such file or directory`.

## Scope
PREFLIGHT's path union is the 17 paths above. My commits touch `tests/ops/test_bare_guard.py`, `tests/ops/test_desk_launch_prechecks.py` and `tests/ops/test_prodwrite_hub.py` (all test files of rows W3, W6, W1). They also touch `ops/desk/bare-guard.py` (W3), `ops/desk/desk-launch.sh` (W6's `:113-125`/`:571-589` block only) and `docs/40 - DevDocs/prompts/PRODWRITE-HUB.md` (W1). Every path is in some row's `files`.

## Checked against the branch
- (i) `git log --oneline 89fd13c5..HEAD -- . ":(exclude)docs"` → `b96737bf fix(prodwrite-seat-1012): …` and `335de8b4 wip(prodwrite-seat-1012): check red — O1 O2 O3 A1 A3`. Tip now: `b96737bf`.
- (ii) `git log --stat --format=%h 89fd13c5..HEAD` → `b96737bf`: PRODWRITE-HUB.md, ops/desk/bare-guard.py, ops/desk/desk-launch.sh; `335de8b4`: the three test files; `8736ce47`: the build report (docs). No path falls outside the rows' files.
- (iii) `git log --oneline 86b9daa5..HEAD -- <the fenced scripts, src, the ten other hubs, .claude>` → empty.
- (iv) `grep -n -F "def <test>"`, one line each: `test_bare_guard.py:513` O1, `:524` O3, `:532` A1; `test_desk_launch_prechecks.py:1063` O2; `test_prodwrite_hub.py:160` A3. `335de8b4` sits below `b96737bf` in (i).
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/prodwrite-seat-1012`.
- (vi) `git log --stat --format=%h 86b9daa5..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no migration and no with-DB test, so no gate-lists change is owed.
- (vii) Card RECORDS: R1138 sits at `cto-2026-10-12.md:38` per authorize.sh at 08:17 ET (the card says `:12`; the build read `:25`; the file has grown). It is committed in `5d6ce588`, HIS RULING · APPROVED. The other records name Grep counts, not runnable commands.
- (viii) L32: this report holds constructed values only.

## OPEN
- A2 (Grok) · REJECTED — card W3 passes `prod_read` for the seat, and his R686 lets every seat run that read. On a card with two write rows or none, the read-only `db query` still passes. That matches the builder's DECISION 2 (safe default). To settle it, the desk decides whether card W3's Q2 ("every production command") means the read too. If so, the guard's `prodwrite` branch drops `prod_read` when `named` is empty, and the test returns as written under `## RUNS`. FOLLOW-UP.

## CONTINUE
next: CLOSE (done)

## DECISIONS
none

## RECORDS
- L74: one system block in this session asked for a `Claude-Session:` line on commits. It was recorded under `## L74` and not followed.
- Dropped findings: none. Houses that produced nothing: none (Grok wrote `house-a.md`, `FINDINGS: 3`). House B: none (not needed; `HOUSE B: as needed`).
- REFUSED, not needed: `git show 89fd13c5:docs/40\ -\ DevDocs/prompts/PRODWRITE-HUB.md` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." I read the file with the Read tool instead.
- No lock take (DB: none). No CONTINUE received.
- A comment-only edit to `desk-launch.sh` (`:120-127`) came after the 181-pass launcher run and before the fix commit. The tests/ops run (3240 passed) covers the committed file.
- files opened: 15 — CHECK-HUB.md; the card; BUILD-HUB.md (`## THE LOCK` → `## W`); the build report; areas/cobalt.md (`## What Cobalt is`, `## Build rules` down); PRODWRITE-HUB.md; ops/desk/bare-guard.py; ops/desk/desk-launch.sh; tests/ops/test_bare_guard.py; tests/ops/test_desk_launch_prodwrite.py; tests/ops/test_desk_launch_prechecks.py; tests/ops/test_prodwrite_hub.py; src/cobalt/backup/cli.py; src/cobalt/backup/restic.py; house-a.md. The diffs of authorize.sh, desk-watch.sh and desk-done.sh were read through `git diff`.
- Check of `prodwrite-seat-1012`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: prodwrite-seat-1012 · pass: 1 · tip: b96737bf · house A: Grok FINDINGS: 3 · findings: 6 · dropped: 0 · held: 5 · fixed: 5 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 15 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 244290
