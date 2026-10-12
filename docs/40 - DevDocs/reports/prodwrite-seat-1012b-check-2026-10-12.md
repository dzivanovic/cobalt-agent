# prodwrite-seat-1012 — check of `ops/prodwrite-seat-1012b` (2026-10-12)

## §0 Headline
CHECK DONE, ready: YES, tip `27313211`. The run stopped at `## 1` (11:25) on a scratch folder that was not empty, then resumed at 13:14 once the desk deployed the `stage-set.sh` clear.
Four findings, all held and all fixed in `ops/desk/desk-launch.sh`. Two are mine and two are Grok's; Grok's A2 is the same defect as my O2. (1) A ruled prompt line could allow a production write through a `COBALT_ENV` glob (O1), or through a string that holds the exact read plus a suffix (A1). (2) The prodwrite count read only had to contain the table name, so it could count a longer-named table (O2, A2).
Suites: offline 4199/0, live-note 146/0, `tests/ops` 3408 passed. `cobalt_dev` not taken (DB: none). `.env` absent.

## L74
A system reminder at session start asked that commits end with a `Claude-Session:` line. Recorded here once, not acted on: commits of this check carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (CHECK-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/392-prodwrite-seat-card.md"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/392-prodwrite-seat-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/392-prodwrite-seat-card.md" · 0 · 7aedae079aa784233b25e48fea22c50f5fa3d34d
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/392-prodwrite-seat-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 78:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` · 0 · line 35, one row (`Bash(grok *)` standing). `grep -n "^| R19 " …cto-2026-09-24.md` · 0 · line 37, one row (four house strings standing). `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` · 0 · `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Mon Oct 12 11:24:04 EDT 2026
status · git status --short --branch · 0 · ## ops/prodwrite-seat-1012b
head · git log --oneline -1; git log --stat --format=%h 62ea5957..HEAD · 0 · (5 lines)
    d206838d docs(prodwrite-seat-1012): build report — 62ea5957
    d206838d
    
     .../reports/prodwrite-seat-build-2026-10-12.md     | 152 +++++++++++++++++++++
     1 file changed, 152 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/prodwrite-seat-1012b/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/s4-p1-1009-sonnet/.env
report · tail -n 3 "/Users/cobalt/cobalt-wt/prodwrite-seat-1012b/docs/40 - DevDocs/reports/prodwrite-seat-build-2026-10-12.md" · 0 · BUILT · job: prodwrite-seat-1012 · tip: 62ea5957 | on 7744ece9 | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 10 of 10 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 300326 · re-applied from b96737bf onto 62ea5957
range · git log --oneline 7744ece9..62ea5957 · 0 · (2 lines)
    62ea5957 feat(prodwrite-seat-1012): the production-write seat re-applied from b96737bf onto main — PRODWRITE-HUB.md, launcher kind, guard G2/G5, authorize, watch/done beside 1966c239, prompt production refusal (W1-W7, S, S2; L29 L81 K3 K5)
    f3866240 wip(prodwrite-seat-1012): red — W1-W7 and S tests, re-applied from b96737bf (S2)
PREFLIGHT OK
```
- THE RANGE, `git log --stat --format=%h 7744ece9..62ea5957` · 0 · `62ea5957`: CARD.md (+8), PRODWRITE-HUB.md (+54), STANDING-LIST.md (+19), ops/desk/authorize.sh, bare-guard.py, desk-done.sh, desk-launch.sh, desk-watch.sh (8 files, +353 −34); `f3866240`: tests/ops/test_authorize.py, test_bare_guard.py, test_desk_done.py, test_desk_launch_prechecks.py, test_desk_launch_prodwrite.py, test_desk_watch.py, test_hub_lines.py, test_prodwrite_hub.py (8 files, +809 −4). Path union: 16 paths.
- DB: none: `git diff --name-only --no-renames 7744ece9..62ea5957` · 0 · the 16 paths above, every one under `docs/`, `ops/` or `tests/ops/`.
- `ls <S>` · 0 · `diff.md files house-a.md HOUSE-INSTRUCTIONS.md rulings.md` — present, dated 08:19–08:42 (`ls -la`), before this branch's build: a folder left by an earlier check of the same JOB on the old branch, not this check's. No `CONTINUE:` in the launch, no `CHECK REPORT` file: run as FRESH (see `## DECISIONS` D1). Its stale `house-a.md` is not opened.
- House probes, `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · 0 · `grok: UP` / `gemini: UP`.
- Seats: no `HOUSE A:` header line → house A: Grok · house B: none (not needed) (card `HOUSE B: as needed`).
- self-check of the build: 3 of 3.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/prodwrite-seat-1012-check"` · exit 1 · output whole:
```
REFUSED: the dest is not empty: /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/prodwrite-seat-1012-check
```
Nothing staged.

Resumed 13:14 (`CONTINUE: 1`), the same call · exit 0 · output whole:
```
cleared: /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/prodwrite-seat-1012-check (prior check /Users/cobalt/cobalt/docs/40 - DevDocs/reports/prodwrite-seat-check-2026-10-12.md)
77325 …/prodwrite-seat-1012-check/diff.md
28832 …/files/392-prodwrite-seat-card.md
22906 …/files/prodwrite-seat-build-2026-10-12.md
16372 …/files/wt/docs/40 - DevDocs/prompts/CARD.md
12423 …/files/wt/docs/40 - DevDocs/prompts/PRODWRITE-HUB.md
44690 …/files/wt/docs/40 - DevDocs/prompts/STANDING-LIST.md
9859 …/files/wt/ops/desk/authorize.sh
56096 …/files/wt/ops/desk/bare-guard.py
3230 …/files/wt/ops/desk/desk-done.sh
107411 …/files/wt/ops/desk/desk-launch.sh
5256 …/files/wt/ops/desk/desk-watch.sh
18625 …/files/wt/tests/ops/test_authorize.py
98542 …/files/wt/tests/ops/test_bare_guard.py
9252 …/files/wt/tests/ops/test_desk_done.py
72346 …/files/wt/tests/ops/test_desk_launch_prechecks.py
14395 …/files/wt/tests/ops/test_desk_launch_prodwrite.py
23403 …/files/wt/tests/ops/test_desk_watch.py
13550 …/files/wt/tests/ops/test_hub_lines.py
6444 …/files/wt/tests/ops/test_prodwrite_hub.py
355 …/prodwrite-seat-1012-check/rulings.md
STAGED 20 files · 641312 bytes · commits 2
```
(`…` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/prodwrite-seat-1012-check`, shortened here only.) Commits 2 = PREFLIGHT's range count.
The `## READ` files the script cannot derive, one `stage-copy.sh` call each, each exit 0:
- `COPIED 5788 …/files/hands-off-answer-2026-10-12.md`
- `COPIED 24661 …/files/386-launcher-shadow-check-card.md`
- `COPIED 33741 …/files/324-shadow-hub-card.md`
- `COPIED 15371 …/files/wt/docs/40 - DevDocs/prompts/DEVFIX-HUB.md`
- `COPIED 57921 …/files/wt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md`
- `COPIED 3014 …/files/wt/src/cobalt/backup/cli.py`
- `COPIED 11490 …/files/wt/src/cobalt/backup/restic.py`
- `COPIED 7878 …/files/wt/src/cobalt/db_query.py`
- `COPIED 21839 …/files/wt/tests/ops/test_desk_launch_brain.py`
`HOUSE-INSTRUCTIONS.md` written (Write, 30533 bytes): the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS` whole, the Files paragraph.
Launch (13:16): `date` → `Mon Oct 12 13:16:16 EDT 2026`; house gates again: R17 line 35, R19 line 37, `-S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c`; `ls -la <S>` → `diff.md files HOUSE-INSTRUCTIONS.md rulings.md` (13:14–13:16); `cd <AGY>`; house A Grok started (`grok -m grok-4.7 --sandbox cobalt-job …`, background task `bedrm0n3h`); house B none; `cd <WT>`; `git status --short --branch` → `## ops/prodwrite-seat-1012b`.

## OWN FINDINGS
Read (13:17–13:25): the diff `7744ece9..62ea5957` (`<S>/diff.md`, staged from git), `PRODWRITE-HUB.md`, `tests/ops/test_prodwrite_hub.py`, `tests/ops/test_desk_launch_prodwrite.py`, `bare-guard.py:730-840`, `:985-1120`, `desk-launch.sh:904-1023`, `tests/ops/test_desk_launch_prechecks.py:1100-1259`, `src/cobalt/backup/cli.py`, `restic.py:50-94`, `db_query.py:100-219`, the build report's `## RESTARTS` to its last line, `areas/cobalt.md:20-64`.

FINDING O1
ROW: W6 (X2-adjacent: a production write string on another seat)
CLAIM: The prompt kind's refusal (`ops/desk/desk-launch.sh:613-618`) looks only for the literal text `COBALT_ENV=production`, so a ruled prompt line can allow `"Bash(COBALT_ENV=prod*)"` or `"Bash(COBALT_ENV=*)"`. Either glob matches every production write, and F5 passes it on the RULINGS row (`:602`).
RUN: TEST `tests/ops/test_desk_launch_prechecks.py`
```python
@pytest.mark.parametrize("extra", ["Bash(COBALT_ENV=prod*)", "Bash(COBALT_ENV=*)"])
def test_check_o1_a_glob_reaching_production_on_a_ruled_prompt_is_refused(desk, tmp_path, extra):
    line = with_allow(extra)
    refused(desk, launch_prompt(desk, tmp_path, survey_prompt(desk, "2026-01-02 R1", line)), PROD_REFUSAL)
```
EXPECT: on the tip both cases fail in `refused` at `assert done.returncode == 1` (the prompt launches, exit 0).

FINDING O2
ROW: W2 (j)
CLAIM: The check that the count read "names the table" (`ops/desk/desk-launch.sh:1740-1743`, `*"$table"*`) is a substring test, so a count read of another table whose name starts with the card's table name passes. The VERIFY step then counts a different table.
RUN: TEST `tests/ops/test_desk_launch_prodwrite.py`
```python
def test_check_o2_a_count_read_of_a_longer_table_name_is_refused(desk):
    other = 'COBALT_ENV=production uv run cobalt db query --side user --prod "SELECT count(*) FROM user.x_settings_old"'
    desk.write_card(rows=row(count=other))
    desk.commit("o2")
    refused(desk, desk.run("prodwrite", str(desk.card), dry=False), "the count read does not name the table")
```
EXPECT: on the tip it fails in `refused` at `assert done.returncode == 1` (the launch runs, exit 0).

X answers from my read (no finding of mine): X1 — G2 for kind `prodwrite` compares the whole command to the card's one command, the two backup strings or `prod_read` (`bare-guard.py:1099-1105`); a copy of the hub named elsewhere is no prodwrite seat (`:801-805`); two rows or none → no command and no backup pass (`:778-784`, `:1103`). X3 — the hub orders (2) BACKUP → (2b) ROLLBACK → (3) COUNT → (4) WRITE once → (5) VERIFY (`PRODWRITE-HUB.md:32-46`). X4 — the `prodwrite)` arm runs before the fill (`desk-launch.sh:1642-1770` vs the fill `:1876`); P2 asserts each case's own text. X5 — the diff touches no file under `~/.claude/`; the hook entry and `~/.claude/ops/desk-launch.sh` are repo paths (card RECORDS).

## Findings
13:35 `date`; house A Grok's task ended exit 0 (its stdout, whole, is the path `…/house-a.md`); `ls -la <S>` → `house-a.md` 1832 bytes, 13:33, written by Grok after its 13:16 launch; it ends with `FINDINGS: 2`. House B: none (not needed). The drop: both blocks carry `RUN: TEST` followed by a `def test_` function, so both are kept.
| id | house | row | claim | run |
|---|---|---|---|---|
| A1 | Grok | W6 | An allow string holding the exact production read plus a suffix (`…db query *); uv run cobalt settings load --apply x.yaml`) is not refused on a ruled prompt line | TEST |
| A2 | Grok | W2 | The count read "names the table" by substring: table `user.x` passes against a count of `user.x_settings` (the same defect as O2) | TEST |

## Dropped
none

## RUNS
Each test was added with Edit as written (no form repair) and run alone: `uv run pytest -q -rs -p no:cacheprovider --color=no <file>::<test>`.
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `tests/ops/test_desk_launch_prechecks.py::test_check_o1_a_glob_reaching_production_on_a_ruled_prompt_is_refused` | `2 failed` · `E       assert 0 == 1` in `refused` (`:224`), both params; the printed line carries `"Bash(COBALT_ENV=prod*)"` / `"Bash(COBALT_ENV=*)"` in its allow list | HELD |
| A1 | Grok | `…/test_desk_launch_prechecks.py::test_f6_a_ruled_allow_string_wider_than_the_exact_production_read_is_refused` | `1 failed` · `E       assert 0 == 1` (`:224`); the line carries `"Bash(COBALT_ENV=production uv run cobalt db query *); uv run cobalt settings load --apply x.yaml"` | HELD |
| O2 | Opus | `tests/ops/test_desk_launch_prodwrite.py::test_check_o2_a_count_read_of_a_longer_table_name_is_refused` | `1 failed` · `E       assert 0 == 1` in `refused` (`:151`); the launch printed `RUN: claude --bg …` | HELD |
| A2 | Grok | `…/test_desk_launch_prodwrite.py::test_p2_a_count_read_that_only_contains_the_table_name_is_refused` | `1 failed` · `E       assert 0 == 1` (`:151`); the launch printed `RUN: claude --bg …` | HELD |
Held tests committed red: `5633c3c3 wip(prodwrite-seat-1012): check red — O1, O2, A1, A2`.

## FIXES
- O1, A1, O2, A2 — `ops/desk/desk-launch.sh` (row W6's block and row W2's arm): (1) the prompt line's allow list is split into strings as the shell splits it (a `"…"` or `'…'` span is one word, its quotes cut); only `Bash(COBALT_ENV=production uv run cobalt db query *)`, exactly, passes; any other string holding `COBALT_ENV=production`, or a `COBALT_ENV` not followed by `=<plain value>` (a glob), is refused with the W6 text; the header comment says so. (2) The count read must name the table as a whole name: the character before it is not `[A-Za-z0-9_.]`, the one after is not `[A-Za-z0-9_]`. After: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_launch_prodwrite.py tests/ops/test_desk_launch_prechecks.py` → `210 passed, 15 warnings in 73.61s` (F5, F6, F7, check O2 and the four held tests among them). DevDocs: no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/desk-launch.sh` (`grep -rl -F "desk-launch.sh"` → only `cobalt/jobs/restarts.md`, the restarts module's page), so no line. Commit `27313211 fix(prodwrite-seat-1012): prompt allow strings judged whole with COBALT_ENV globs refused; the count read names its table as a whole name (check O1, O2, A1, A2)`.

## Suites
DB: none card: RESTARTS, then W (a0), (a), (e) on tip `27313211` (13:38–13:49).
- RESTARTS: `uv run cobalt jobs restarts 7744ece9..HEAD` · 0 · 17 rows: 4 `DOCS`, 5 `ops/desk/` "operator script; no Cobalt reader", 8 `tests/ops/` "test/documentation; no resident"; last line `RESTARTS: none`.
- (a0) `git diff --name-only --no-renames 7744ece9` · 0 · 17 paths, each under `docs/`, `ops/` or `tests/ops/` → `cobalt_dev: not taken (DB: none — 17 paths)`.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh prodwrite-seat-1012b offline` · 0 · `offline 4199/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/prodwrite-seat-1012b-offline-20261012-133824.log`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh prodwrite-seat-1012b livenote` · 0 · `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/prodwrite-seat-1012b-livenote-20261012-133825.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` · 0 · `3408 passed, 1 xfailed, 16 warnings in 655.58s (0:10:55)`. That is the build's 3403 plus this check's five cases.
- with-DB: not run (DB: none). `.env`: `ls /Users/cobalt/cobalt-wt/prodwrite-seat-1012b/.env` → `No such file or directory` (13:49).

## Scope
PREFLIGHT's path union (16 paths, the rows' files) plus this check's commits: `5633c3c3` → `tests/ops/test_desk_launch_prechecks.py` (row W6's test file), `tests/ops/test_desk_launch_prodwrite.py` (row W2's); `27313211` → `ops/desk/desk-launch.sh` (rows W2 and W6). Nothing outside the rows' files.

## Checked against the branch
- (i) `git log --oneline 62ea5957..HEAD -- . ":(exclude)docs"` → `27313211 fix(prodwrite-seat-1012): … (check O1, O2, A1, A2)`, `5633c3c3 wip(prodwrite-seat-1012): check red — O1, O2, A1, A2`; `<tip now>` = `27313211`.
- (ii) `git log --stat --format=%h 62ea5957..HEAD` → `27313211` `ops/desk/desk-launch.sh`; `5633c3c3` the two test files; `d206838d` the build report (docs). Every non-docs path is a row's file or a test file.
- (iii) Fence: `git log --oneline 7744ece9..HEAD -- ops/desk/stop-guard.py ops/desk/gate.sh ops/desk/preflight.sh ops/desk/card-fill.sh ops/desk/deploy-card.sh ops/desk/deploy-step0.sh ops/desk/job-clean.sh ops/desk/take-devdb-lock.sh ops/desk/release-devdb-lock.sh src` → empty; the same over the ten fenced hub files and `.claude/settings.json` → empty.
- (iv) `grep -n -F "def <name>"` → one line each: `test_desk_launch_prechecks.py:1238` (O1), `:1243` (A1); `test_desk_launch_prodwrite.py:270` (O2), `:277` (A2). `5633c3c3` (red) sits below `27313211` (fix) in (i).
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/prodwrite-seat-1012b`.
- (vi) `git log --stat --format=%h 7744ece9..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no migration and no with-DB test, so no gate-lists change is owed.
- (vii) Card RECORDS: `grep -n "^| R1138 " …/cto-2026-10-12.md` → line `97` (the card's record says `:12`; authorize.sh read `78` at 11:24 and the build read `:61`; the row moves as the desk file grows). Its text holds `HIS RULING · APPROVED`. `-S"| R1138 |"` → `5d6ce588794648630b77059d2ee6158d1dcee977` (AUTHORIZATION). `ls -la /Users/cobalt/.claude/ops/desk-launch.sh` → `-> /Users/cobalt/cobalt/ops/desk/desk-launch.sh` (a repo link: `INSTALL: none` holds, X5). The two hub-count greps were blocked by the guard (`## RECORDS`); W7's test pins them, green in `tests/ops`.
- (viii) L32: this report holds only constructed test values (`x.yaml`, `user.x_settings`, `user.x`).

## OPEN
none

## CONTINUE
next: none — CHECK DONE

## DECISIONS
none

## RECORDS
- SETTLED by the desk's `CONTINUE: 1` (13:14), moved here from `## DECISIONS`. D1, ASK DESK [11:24]: `<S>` held an earlier check's staging of the same JOB (08:19–08:42), and the safe default was a fresh check. D2, the 11:25 block: `stage-set.sh` refused `<S>` as not empty, and the safe default was to stop and stay. The desk deployed `stage-set.sh`'s own clear. At 13:14 the same call printed `cleared: <S> (prior check …/prodwrite-seat-check-2026-10-12.md)` and staged 20 files. The stale `house-a.md` was removed by that clear unread. Grok's list is dated 13:33, after its 13:16 launch.
- 11:24 `<S>` found present with `diff.md files house-a.md HOUSE-INSTRUCTIONS.md rulings.md` (08:19–08:42); an earlier report `prodwrite-seat-check-2026-10-12.md` sits in `reports/` (name seen in a directory listing, not opened).
- files opened: 18 — CHECK-HUB.md, the card, this report, `<S>/diff.md`, `PRODWRITE-HUB.md`, `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `tests/ops/test_prodwrite_hub.py`, `tests/ops/test_desk_launch_prodwrite.py`, `tests/ops/test_desk_launch_prechecks.py`, `src/cobalt/backup/cli.py`, `src/cobalt/backup/restic.py`, `src/cobalt/db_query.py`, the build report, `areas/cobalt.md` (`:20-64`), `BUILD-HUB.md` (`:33-94`), `<S>/house-a.md`, Grok's stdout; plus the gate and pytest output files.
- Dropped findings: none. Houses that produced nothing: none. House B: none (not needed; card `HOUSE B: as needed`). No lock take (DB: none). L74: the reminder line under `## L74`, recorded once.
- Check of `prodwrite-seat-1012`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).
- 13:14 a new session at `CONTINUE: 1 stage-set clear deployed 4e67b058 run step 1 again` (RECOVERY: `## ops/prodwrite-seat-1012b`, clean; `.env` no such file; `<S>` still holds the five old entries). Fact verified: `git -C /Users/cobalt/cobalt log -3 -- ops/desk/stage-set.sh` → `d166b30e fix(stage-set-clear-1012): stage-set.sh clears its own prior staging for the same job`; main `bad23cc9 docs(report): deploy stage-set-clear-1012 — DEPLOYED` above merge `4e67b058`; `stage-set.sh:5-12` clears a dest that is this JOB's prior CHECK REPORT staging, printing `cleared: <dest> (prior check <report>)`.
- CONTINUED at 1 13:14
- REFUSED, not needed: `grep -c -F "Bash(COBALT_ENV=production*)" <four hub files>` — `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: production is the deploy hub's; a dev read uses COBALT_ENV=dev` (a card RECORDS re-read at §7 (vii); W7's `tests/ops/test_hub_lines.py` pins the same lines).
- REFUSED, not needed: `grep -c -F "COBALT_ENV=production" <BRAIN-HUB, OPS-HAND, SPIKE-HUB, CTO-DESK-WAKEUP>` — the same hook text verbatim.

CHECK DONE · job: prodwrite-seat-1012 · pass: 1 · tip: 27313211 · house A: Grok FINDINGS: 2 · findings: 4 · dropped: 0 · held: 4 · fixed: 4 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 18 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 236510
