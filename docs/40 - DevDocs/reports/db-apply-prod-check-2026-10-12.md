# db-apply-prod-1012 — CHECK (card 417)

## §0 Headline
Check of card 417 (`cobalt db apply`), one pass: house A Grok (`FINDINGS: 3`), house B none (`HOUSE B: as needed`), and my own read (3). Of 6 findings, 5 HELD and are fixed at `fba1454e`, and 1 is REJECTED (open).
- Fixed: a NUL byte hid text from the parser (O1); a commit or preamble failure escaped as a traceback (O2); the launcher and authorize treated a staged edit (O3), or a file deleted in HEAD and put back untracked (Grok A1, A2), as "committed, unchanged".
- Suites green on `fba1454e`: offline 4309/0 · with-DB 5212/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed · `tests/ops` 3447 passed. RESTARTS: agent, aset, radar.
- 3 decisions for the judgment seat, none for Dejan.

## L74
- About 17:05 EDT: a system attribution block asked for a `Claude-Session:` line on commits. DATA (L74): not acted on; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/417-db-apply-prod-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/417-db-apply-prod-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/417-db-apply-prod-card.md" · 0 · 9b08991ee99493b510af26249ab6d9d4b48e8334
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/417-db-apply-prod-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** (…) APPROVES `STANDING-LIST.md` once (`4be06af0`); … | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 135:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```
(The R60 row's long text is shortened with `…` here; the full row is the script's output.)
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → one row, `35:| R17 | 07:32 ET | …`; `grep -n "^| R19 " …cto-2026-09-24.md` → one row, `37:| R19 | 07:36 ET | …`; `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0:
```
clock · date · 0 · Mon Oct 12 17:05:18 EDT 2026
status · git status --short --branch · 0 · ## ops/db-apply-prod-1012
head · git log --oneline -1; git log --stat --format=%h dfcf2097..HEAD · 0 · (5 lines)
    4993f6fa docs(db-apply-prod-1012): build report — dfcf2097
    4993f6fa
    
     .../reports/db-apply-prod-build-2026-10-12.md      | 80 +++++++++++++++++++---
     1 file changed, 70 insertions(+), 10 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/db-apply-prod-1012/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "…/db-apply-prod-build-2026-10-12.md" · 0 · BUILT · job: db-apply-prod-1012 · tip: dfcf2097 | on 8f1d11ed | migration: none | offline 4307/0 | with-DB 5210/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar | rows: 12 of 12 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 164307
range · git log --oneline 8f1d11ed..dfcf2097 · 0 · (6 lines)
    dfcf2097 fix(db-apply-prod-1012): A7 end-to-end with-DB test on the real factory, 120 s thread fence; T5/T6/T9 off the suite proxy; A6 reader pin (A6, A7; L42, L45)
    2de9afa9 wip(db-apply-prod-1012): W — A6 pin green, A7 test written; with-DB run hung, handed to a new session
    2e0e7c82 wip(db-apply-prod-1012): W — offline red on the backup.yaml reader pin, outside the rows
    81452495 feat(db-apply-prod-1012): cobalt db apply — parse-tree allowlist, hashed file, backup bound, one transaction; launch and authorize re-prove the file (A1-A5, K1-K4; L1, L3, L4, L28, L45)
    870f94ca wip(db-apply-prod-1012): E3 — pglast 6.16 does not install on the CPython 3.14 venv
    df558cb7 wip(db-apply-prod-1012): red — db apply tests A1-A5, K1-K4 (card 417)
PREFLIGHT OK
```
- The range, typed, `git log --stat --format=%h 8f1d11ed..dfcf2097` · 0: six commits. Path union: `.gitignore`, `docs/40 - DevDocs/cobalt/cli.md`, `docs/40 - DevDocs/cobalt/db_apply.md`, `docs/40 - DevDocs/cobalt/db_migrations/cli.md`, `docs/40 - DevDocs/prompts/CARD.md`, `docs/40 - DevDocs/prompts/PRODWRITE-HUB.md`, `docs/40 - DevDocs/reports/db-apply-prod-build-2026-10-12.md`, `ops/desk/authorize.sh`, `ops/desk/desk-launch.sh`, `pyproject.toml`, `src/cobalt/cli.py`, `src/cobalt/db_apply.py`, `src/cobalt/db_migrations/cli.py`, `tests/cobalt/test_db_apply.py`, `tests/cobalt/test_db_apply_db.py`, `tests/cobalt/test_jobs_restarts.py`, `tests/ops/test_authorize.py`, `tests/ops/test_desk_launch_prodwrite.py`, `tests/ops/test_gitignore_apply_sql.py`, `tests/ops/test_prodwrite_hub.py`, `uv.lock`.
- Not a "DB: none" card (the header has no `DB:` key).
- `ls <S>` · 1 · `No such file or directory` → fresh.
- House probe `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · 0:
```
grok: UP
gemini: UP
```
- Seats: no `HOUSE A:` header line → house A: Grok · house B: none (not needed) (`HOUSE B: as needed`).
- Build self-check: `3 of 3`.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · 0, whole:
```
95406 <S>/diff.md
54384 <S>/files/417-db-apply-prod-card.md
50354 <S>/files/db-apply-prod-build-2026-10-12.md
4600 <S>/files/wt/.gitignore
5599 <S>/files/wt/docs/40 - DevDocs/cobalt/cli.md
2024 <S>/files/wt/docs/40 - DevDocs/cobalt/db_apply.md
24714 <S>/files/wt/docs/40 - DevDocs/cobalt/db_migrations/cli.md
16740 <S>/files/wt/docs/40 - DevDocs/prompts/CARD.md
13017 <S>/files/wt/docs/40 - DevDocs/prompts/PRODWRITE-HUB.md
35384 <S>/files/wt/docs/40 - DevDocs/reports/db-apply-prod-build-2026-10-12.md
13550 <S>/files/wt/ops/desk/authorize.sh
111659 <S>/files/wt/ops/desk/desk-launch.sh
2731 <S>/files/wt/pyproject.toml
25775 <S>/files/wt/src/cobalt/cli.py
12424 <S>/files/wt/src/cobalt/db_apply.py
51541 <S>/files/wt/src/cobalt/db_migrations/cli.py
22041 <S>/files/wt/tests/cobalt/test_db_apply.py
5985 <S>/files/wt/tests/cobalt/test_db_apply_db.py
29832 <S>/files/wt/tests/cobalt/test_jobs_restarts.py
21058 <S>/files/wt/tests/ops/test_authorize.py
19326 <S>/files/wt/tests/ops/test_desk_launch_prodwrite.py
1288 <S>/files/wt/tests/ops/test_gitignore_apply_sql.py
7640 <S>/files/wt/tests/ops/test_prodwrite_hub.py
1060695 <S>/files/wt/uv.lock
356 <S>/rulings.md
STAGED 25 files · 1688123 bytes · commits 4
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/db-apply-prod-1012-check`.) `commits 4` against PREFLIGHT's 6: the diff is `-- . ":(exclude)docs"`, and `git log --oneline 8f1d11ed..dfcf2097 -- . ":(exclude)docs"` prints exactly 4 (`dfcf2097`, `2de9afa9`, `81452495`, `df558cb7`); the two others (`870f94ca`, `2e0e7c82`) touch only the build report. Taken as complete (`## DECISIONS` ASK DESK 1).
`stage-copy.sh`, one call each, every one `COPIED`:
```
COPIED 2467 <S>/files/prodwrite-card-decisions-2026-10-12.md
COPIED 2014 <S>/files/db-apply-prod-decisions-2026-10-12.md
COPIED 12423 <S>/files/PRODWRITE-HUB.md   (main's; the branch's is under files/wt/)
COPIED 7878 <S>/files/wt/src/cobalt/db_query.py
COPIED 2809 <S>/files/wt/docker-compose.yml
COPIED 14043 <S>/files/wt/src/cobalt/db.py
COPIED 3825 <S>/files/wt/src/cobalt/env.py
COPIED 3014 <S>/files/wt/src/cobalt/backup/cli.py
COPIED 11490 <S>/files/wt/src/cobalt/backup/restic.py
COPIED 1486 <S>/files/wt/tests/cobalt/test_db_query.py
COPIED 10789 <S>/files/wt/tests/cobalt/test_dev_rebuild_db.py
COPIED 9957 <S>/files/wt/tests/cobalt/test_backup.py
COPIED 20349 <S>/files/wt/configs/cobalt/jobs.yaml
COPIED 12098 <S>/files/wt/src/cobalt/jobs/restarts.py
COPIED 6282 <S>/files/wt/venv-psycopg/_preparing.py
COPIED 22768 <S>/files/wt/venv-psycopg/_cursor_base.py
COPIED 15734 <S>/files/wt/venv-psycopg/_queries.py
COPIED 18834 <S>/files/wt/venv-pglast/parser.pyx
```
`<S>/HOUSE-INSTRUCTIONS.md` (55714 bytes): the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS` (with its `FOR THE CHECK` line) and `## RECORDS` whole, and the Files paragraph.
House A Grok started 17:11 EDT (`run_in_background`, task `b22gnad3i`, timeout 2700000), from `<AGY>`; back in `<WT>`, `git status --short --branch` → `## ops/db-apply-prod-1012`. House B: none (not needed).

## OWN FINDINGS
Written between 17:11 and 17:31 EDT, before any house list was opened; nothing run.

FINDING O1
ROW: A1 (X1)
CLAIM: `parse` hands the text to `pg_parser.parse_sql_json` (`src/cobalt/db_apply.py:83`), a C string, so a NUL byte (valid UTF-8, passes A2 `:196`) may end the text the parser reads; the last statement's piece is `raw[loc:]` to the end (`:111`), so `check_file` can return a piece holding text the tree never covered — "the text that runs is the text that was checked" (A1) fails, or a non-`ApplyRefused` error escapes `command` (`:284` catches `ApplyRefused` only) as a traceback instead of `REFUSED … — nothing opened`.
RUN: TEST `tests/cobalt/test_db_apply.py`
```python
def test_check_o1_a_nul_byte_never_hides_text_from_the_check():
    with pytest.raises(ApplyRefused):
        check_file("UPDATE t SET a = 1\x00; DROP TABLE t")
```
EXPECT: `Failed: DID NOT RAISE <class 'cobalt.db_apply.ApplyRefused'>` (the piece is returned), or another exception class than `ApplyRefused`.

FINDING O2
ROW: A4 (X2, X4)
CLAIM: `apply_statements` catches only a statement's exception (`src/cobalt/db_apply.py:252-257`); an exception from `conn.commit()` (`:260`, e.g. a deferred constraint) or from the preamble (`:237-244`) escapes as a raw traceback, so the run prints no `FAILED … — ROLLED BACK` line and does not return 1, against A4's "Nothing is printed but those lines".
RUN: TEST `tests/cobalt/test_db_apply.py`
```python
def test_check_o2_a_commit_that_fails_ends_in_a_failed_line_and_exit_1(capsys):
    class CommitFails(FakeConn):
        def commit(self):
            self.events.append(("commit",))
            raise RuntimeError("constructed deferred failure")

    conn = CommitFails()
    assert run(conn) == 1
    out = capsys.readouterr()
    assert "ROLLED BACK" in out.out + out.err
    assert ("rollback",) in conn.events
```
EXPECT: `RuntimeError: constructed deferred failure` raised out of `run(conn)`.

FINDING O3
ROW: K1 (X3)
CLAIM: the launcher's "unchanged" test is `git -C "$REPO" diff --quiet -- "$pw_rel"` (`ops/desk/desk-launch.sh:1773`), which compares the working file with the INDEX, not with the commit; a file committed as A, then edited to B and `git add`-ed (staged, never committed), passes, so a card whose block and `--sha256` are B launches a file that is not the committed one. `authorize.sh` uses the same index compare (`git diff --stat`, `ops/desk/authorize.sh:292`).
RUN: TEST `tests/ops/test_desk_launch_prodwrite.py`
```python
def test_check_o3_a_staged_uncommitted_change_of_the_file_is_refused(desk):
    changed = APPLY_SQL + 'UPDATE "user".x_settings SET v = 9;\n'
    apply_card(desk, blocks=(changed,), sha=hashlib.sha256(changed.encode()).hexdigest())
    (desk.prompts / APPLY_FILE).write_text(changed)
    git(desk.repo, "add", "-A")
    refused(desk, desk.run("prodwrite", str(desk.card), dry=False),
            "db apply: the file changed since its commit: docs/40 - DevDocs/prompts/" + APPLY_FILE)
```
EXPECT: `assert 0 == 1` (it launches).

Read and found nothing runnable to hand over: X5 (`uv.lock` gains `pglast` 7.20, its own entry with no `dependencies` line, a `cp314-cp314-macosx_11_0_arm64` wheel; `git diff 8f1d11ed..dfcf2097 -- uv.lock`); X4 beyond O2 (`db.py:193-199` composes the DSN inside `_open` and nothing in `db_apply.py` prints it); A5 wiring (`db_migrations/cli.py:1131`, `:1134`; `cli.py:18`); K4 (`.gitignore:93-95`).

## Findings
House A Grok finished 17:31 EDT (task exit 0; it wrote `<S>/house-a.md` itself, 2880 bytes, last line `FINDINGS: 3`). House B: none (not needed). `grep -n -F "RUN:" <S>/house-a.md` → `4:RUN: TEST — tests/ops/test_desk_launch_prodwrite.py`, `22:RUN: TEST — tests/ops/test_authorize.py`, `41:RUN: COMMAND`: each followed by a `def test_` or one `grep` line, so none is dropped.
- A1 · Grok · K1 · a path deleted in HEAD and written back untracked passes the launcher's "committed" (`git log -1` non-empty) and "unchanged" (`git diff --quiet`) tests (`desk-launch.sh:1771-1773`) · TEST
- A2 · Grok · K2 · the same deleted-then-untracked file passes authorize's `SQL FILE committed` / `SQL FILE unchanged` rows (`authorize.sh:286-295`) and ends `AUTHORIZED` · TEST
- A3 · Grok · A7 · the with-DB test carries no `@pytest.mark.timeout(120)` (`test_db_apply_db.py:103-105`) · COMMAND

## Dropped
none

## RUNS
Each test put in its named file by Edit and run alone (`uv run pytest -q -rs -p no:cacheprovider --color=no <file>::<test>`); no test's form was repaired.
- O1 · own · `tests/cobalt/test_db_apply.py::test_check_o1_a_nul_byte_never_hides_text_from_the_check` · `1 failed in 0.09s`; `E       Failed: DID NOT RAISE <class 'cobalt.db_apply.ApplyRefused'>` (`tests/cobalt/test_db_apply.py:567`) · HELD
- O2 · own · `tests/cobalt/test_db_apply.py::test_check_o2_a_commit_that_fails_ends_in_a_failed_line_and_exit_1` · `1 failed in 0.08s`; `E       RuntimeError: constructed deferred failure` raised from `src/cobalt/db_apply.py:260: in apply_statements` `conn.commit()`; captured stdout `STATEMENT 1/3` … `ROWS 3: 3` and no `FAILED` line · HELD
- O3 · own · `tests/ops/test_desk_launch_prodwrite.py::test_check_o3_a_staged_uncommitted_change_of_the_file_is_refused` · `1 failed, 15 warnings in 1.37s`; `E       assert 0 == 1` — it launches, the line carrying `"Bash(COBALT_ENV=production uv run cobalt db apply --side user --prod --sha256 0f4b8d56… 2026-01-02/1-x-apply.sql)"` for the staged, uncommitted bytes · HELD
- A1 · Grok · `tests/ops/test_desk_launch_prodwrite.py::test_k1_a_file_deleted_in_head_and_restored_untracked_is_refused` · `1 failed, 15 warnings in 1.26s`; `E       assert 0 == 1` — it launches with `"Bash(COBALT_ENV=production uv run cobalt db apply … --sha256 aef873b4… 2026-01-02/1-x-apply.sql)"` · HELD
- A2 · Grok · `tests/ops/test_authorize.py::test_k2_a_file_deleted_in_head_and_restored_untracked_is_not_authorized` · `1 failed, 15 warnings in 1.03s`; `E       assert 0 == 1`; stdout rows `SQL FILE committed · … · 0 · 3a54e282…`, `SQL FILE unchanged · … · 0 · nothing`, `SQL SHA256 · … · 0`, `SQL CARD BLOCK · … · 0 · the card's ## SQL block is the file byte for byte`, last line `AUTHORIZED` · HELD
- A3 · Grok · `grep -n "pytest.mark.timeout" tests/cobalt/test_db_apply_db.py` · no output · REJECTED — the card's A7 cell: "`pytest-timeout` is no dependency … and none is added: the 120 s fence below is carried by the test file with no `signal` and no new dependency, `command` run in a daemon `threading.Thread` joined for 120 s", and `## NOT IN THIS JOB` "A second dependency"; the build's DECISION 2 (a mark without the plugin does nothing) was answered KEEP by the desk (`## RECORDS`). The thread fence is present (`test_db_apply_db.py:34`, `:132-135`). OPEN.
Red commit: `git commit … -- tests/cobalt/test_db_apply.py tests/ops/test_desk_launch_prodwrite.py tests/ops/test_authorize.py` → `[ops/db-apply-prod-1012 09d44101] wip(db-apply-prod-1012): check red — O1 O2 O3 A1 A2` · `3 files changed, 54 insertions(+)`.

## FIXES
One commit, `fba1454e` `fix(db-apply-prod-1012): NUL refused, commit/preamble failures end in one FAILED line, apply file proved against HEAD at launch and authorize (check O1 O2 O3 A1 A2)` · `4 files changed, 36 insertions(+), 8 deletions(-)`. Every changed file is in a row's `files` (A1/A4 `src/cobalt/db_apply.py`; K1 `ops/desk/desk-launch.sh`, inside the prodwrite arm; K2 `ops/desk/authorize.sh`) plus the module's DevDocs page.
- O1 (A1): `parse` refuses a text holding `"\x00"` as `does not parse: the text holds a NUL byte`, before the parser. It is a precondition on the input, not a word rule in the classifier: Postgres's query text cannot carry a NUL either.
- O2 (A4): the preamble (`SET LOCAL` ×2, `SHOW server_version_num`, `SELECT current_user`) runs inside its own `try` → `FAILED before statement 1: <class>: <message> — ROLLED BACK`, return 1; `conn.commit()` in a `try` → `FAILED at commit: <class>: <message> — ROLLED BACK`, return 1. T7's order is unchanged; `current_user` is now read before the major is judged, and no statement is sent on either refusal.
- O3, A1 (K1): `desk-launch.sh` adds `git -C "$REPO" cat-file -e "HEAD:$pw_rel"` (committed means in HEAD) → `db apply: the file is not committed: <rel>`, and compares with `git -C "$REPO" diff --quiet HEAD -- "$pw_rel"` (against HEAD, so a staged edit is a change) → `db apply: the file changed since its commit: <rel>`. The card's K1 (b) names `git diff --quiet -- <rel>` and calls it "(committed, unchanged)"; the index compare does not prove that, and the fix keeps the card's two refusal texts.
- A2, O3 (K2): `authorize.sh` `SQL FILE committed` also fails when `git cat-file -e "HEAD:<rel>"` fails (`(not in HEAD)` appended); `SQL FILE unchanged` runs `git diff --stat HEAD -- <rel>`. The four row names are unchanged.
- After the fix: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_db_apply.py tests/ops/test_desk_launch_prodwrite.py tests/ops/test_authorize.py` → `199 passed, 15 warnings in 15.99s` (`0 failed`).
- DevDocs: `docs/40 - DevDocs/cobalt/db_apply.md` gains `## 2026-10-12 — check of db-apply-prod-1012 (O1, O2)`. The two desk scripts have no page under `docs/40 - DevDocs/cobalt/`.

## Suites
RESTARTS first, `uv run cobalt jobs restarts 8f1d11ed..HEAD` · 0: the build's table plus no new row class (`ops/desk/authorize.sh`, `ops/desk/desk-launch.sh` → `operator script; no Cobalt reader`; `src/cobalt/db_apply.py` → `static import reach` `com.cobalt.radar`; the three test files → `test/documentation; no resident`; `pyproject.toml`, `uv.lock` → `resident reads` `com.cobalt.agent,com.cobalt.aset,com.cobalt.radar`), no `UNCLASSIFIED`, last line **`RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar`** (R1's expectation).
`sh /Users/cobalt/cobalt/ops/desk/gate.sh db-apply-prod-1012 all --deploy` (background, about 17:34–18:03 EDT) · exit 0. No `--deselect`, `--tickers` or `--migration` (no migration; the with-DB tests write no ticker). Verdict lines, whole:
```
offline 4309/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5212/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/db-apply-prod-1012-all-20261012-173438.log
```
- Log: `code: fba1454e (clean)` (`:950`, `:1188`, `:2030`, `:2085`); offline `:885` `4309 passed, 806 skipped, 1 xfailed, 36 warnings in 630.52s` (the build's 4307 plus O1 and O2); pass 1 `:1115` `5007 passed, 7 skipped, 99 deselected, 3 xfailed, 43 warnings in 772.82s`; pass 2 `:1969` `205 passed, 1 deselected, 5 warnings in 228.17s` (5007 + 205 = 5212); live-note `:2160` `146 passed, 1 skipped, 15 warnings in 25.66s`. No skip is marked `OUTSIDE the allowed set`.
- `cobalt_dev`: `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:902`) = `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:2037`) → `cobalt_dev: 0013 — F2 = F0`.
- `.env`: the gate's `.env: removed`; `ls /Users/cobalt/cobalt-wt/db-apply-prod-1012/.env` → `No such file or directory`.
- The gate's suites are `tests/cobalt tests/taxonomy` (log `:2`, `:958`); `tests/ops` is outside them, and this check changed two desk scripts, so: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` (background) · exit 0 → `3447 passed, 1 xfailed, 16 warnings in 656.23s (0:10:56)`.
- Every held finding's test passes (gate offline for O1, O2; `tests/ops` for O3, A1, A2), each was shown red first (`## RUNS`), and the three suites are green.

## Scope
PREFLIGHT's path union (21 paths, `## PREFLIGHT`) plus my two commits: `09d44101` `tests/cobalt/test_db_apply.py`, `tests/ops/test_authorize.py`, `tests/ops/test_desk_launch_prodwrite.py` (test files); `fba1454e` `src/cobalt/db_apply.py` (A1, A4 files), `ops/desk/desk-launch.sh` (K1, its prodwrite arm), `ops/desk/authorize.sh` (K2), `docs/40 - DevDocs/cobalt/db_apply.md` (the DevDocs line). No path outside a row's `files`, a test file or `docs/`.

## Checked against the branch
- (i) `git log --oneline dfcf2097..HEAD -- . ":(exclude)docs"` → `fba1454e fix(db-apply-prod-1012): NUL refused, …` and `09d44101 wip(db-apply-prod-1012): check red — O1 O2 O3 A1 A2`; `<tip now>` = `fba1454e`.
- (ii) `git log --stat --format=%h dfcf2097..HEAD` → `fba1454e`: `docs/40 - DevDocs/cobalt/db_apply.md`, `ops/desk/authorize.sh`, `ops/desk/desk-launch.sh`, `src/cobalt/db_apply.py`; `09d44101`: the three test files; `4993f6fa`: the build report. Every non-docs path is in a row's `files` or is a test file. No WIDENED.
- (iii) `git log --oneline 8f1d11ed..HEAD -- ops/desk/bare-guard.py "docs/40 - DevDocs/prompts/STANDING-LIST.md" configs/cobalt/taxonomy/tunables.yaml .claude/settings.json src/cobalt/db_query.py` → empty. `git diff 8f1d11ed..HEAD -- "docs/40 - DevDocs/prompts/PRODWRITE-HUB.md"` → one hunk at `@@ -23,10 +23,10 @@` (steps (0) and (1)): the launch line `:10` and the NEVER line `:16` are untouched.
- (iv) `grep -n -F "def <name>"`, one line each: `tests/cobalt/test_db_apply.py:566` (O1), `:571` (O2); `tests/ops/test_desk_launch_prodwrite.py:429` (O3), `:438` (A1); `tests/ops/test_authorize.py:448` (A2). In (i), `09d44101` (red) sits below `fba1454e` (fix).
- (v) at CLOSE.
- (vi) `git log --stat --format=%h 8f1d11ed..HEAD -- src/cobalt/db_migrations tests/cobalt` → no new migration file; the one new with-DB file `tests/cobalt/test_db_apply_db.py` runs at `0013` (the build's pass 1 ran it, no `--deselect`). `ops/desk/gate-lists.md` is not needed: no GATE LISTS NOT CARRIED.
- (vii) card RECORDS re-run: `ls -l /Users/cobalt/.claude/ops/desk-launch.sh` → `… /Users/cobalt/.claude/ops/desk-launch.sh -> /Users/cobalt/cobalt/ops/desk/desk-launch.sh` (INSTALL: none holds); `grep -n backup.yaml configs/cobalt/jobs.yaml` → `75:      - "configs/cobalt/backup.yaml"` (`:75` only); `grep -n -F "cobalt db " src/cobalt/cli.py` → `17:    cobalt db migrate [--allow-prod] [--rollback]`, `18:    cobalt db apply --side {user,system} [--prod] --sha256 <hex> <date>/<nn>-<name>-apply.sql`; `grep -n -F "updated_at = now()" src/cobalt/jobs/store.py src/cobalt/drc/store.py` → `jobs/store.py:120`, `:135`, `drc/store.py:501` among its lines (the record's three hold); `grep -n -F "image:" docker-compose.yml` → `4:    image: pgvector/pgvector:pg16`.
- (viii) L32: this report holds no ticker, price or date of his; every statement, table and hash in it is constructed or a repo identifier.

## OPEN
- A3 (Grok, A7) · REJECTED — the card's A7 cell says `pytest-timeout` is no dependency and none is added, and the 120 s fence is the daemon thread (`test_db_apply_db.py:34`, `:132-135`); the desk kept the build's DECISION 2 ("D2 D3 KEEP"). What would settle it: the fix round's `SETTLED: A3 — R<n>`, or a card line that drops `@pytest.mark.timeout(120)` from A7's text.

## CONTINUE
next: none. The check is closed at `fba1454e`. The desk commits this report, verifies the artifact and launches the next step.

## DECISIONS
- ASK DESK 1 (17:07 EDT, not for Dejan): `stage-set.sh` printed `commits 4`, and PREFLIGHT's range holds 6. The staged diff is `-- . ":(exclude)docs"`, and `git log --oneline 8f1d11ed..dfcf2097 -- . ":(exclude)docs"` prints exactly 4; the other two (`870f94ca`, `2e0e7c82`) touch only the build report, which the house got whole under `files/`. The hub's rule reads `<k>` = PREFLIGHT's count. Safe default taken: the diff was treated as complete for its pathspec and the check went on. Should `stage-set.sh`'s count, or the hub's rule, name the docs-excluded count?
- ASK DESK 2 (17:50 EDT, not for Dejan): the fix for O3, A1 and A2 goes past K1 (b)'s literal command. The card names `git -C "$REPO" diff --quiet -- <rel>` and calls it "(committed, unchanged)". The fix keeps `git log -1` and both refusal texts, adds `git cat-file -e HEAD:<rel>`, and compares against `HEAD` (`diff --quiet HEAD`, and `diff --stat HEAD` in authorize). Default taken: fixed to the row's stated rule, inside the rows' files (`desk-launch.sh` prodwrite arm, `authorize.sh`). If the literal command was meant, the fix round reverts those lines and O3, A1, A2 become held-unfixed.
- ASK DESK 3 (17:50 EDT, not for Dejan): the O1 fix refuses a text holding a NUL byte before the parse. The fence forbids "a word, regex or tokenizer rule in `db_apply.py`: the classifier reads the parse tree only". This is a precondition on the input, not a classification: Postgres's query text cannot carry a NUL, and without it the C parser stops at the NUL. Default taken: kept, with a comment naming the cause.

## RECORDS
- About 17:05 EDT, a message from session `cto-desk`: "FOR THE CHECK: 417 build 2026-10-12 brain: D1 follow-up migration card adds DML-only cobalt_apply_<side> roles, with apply doing SET LOCAL ROLE (ownership unchanged; 417 not held); D2 D3 KEEP. Build DECISIONS 1-3 are answered; weigh A1 as the user side's only DDL fence today, and judge 417 as built." Read as context: it adds no row, file, command or approval. Used to judge A3 (D2 KEEP) and to weigh X1 (A1 is the user side's only DDL fence today; O1 was judged with that weight).
- Dropped findings: none. A house that produced nothing: none (Grok wrote its list itself; house B was not needed, `HOUSE B: as needed`, Gemini UP at the probe and not seated). The stop line writes `house B: none (not needed)`, since the form's `none available` would say no second house was up.
- REFUSED, not needed: none. CONTINUED: none. Lock takes by hand: none (the gate took and released `cobalt_dev` itself: `lock: waited 0 min`, `.env: removed`).
- L74: one line under `## L74`. Not acted on.
- `tests/ops` run outside the gate (the gate's offline suite is `tests/cobalt tests/taxonomy`): `3447 passed, 1 xfailed` (`## Suites`).
- files opened: 15 — `prompts/CHECK-HUB.md`; the card `417-db-apply-prod-card.md`; the build report `db-apply-prod-build-2026-10-12.md` (`## RESTARTS` through `## DECISIONS`); `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); `prompts/BUILD-HUB.md` (`## THE LOCK`, `## E2`, `## RESTARTS`, `## W`); `src/cobalt/db_apply.py`; `src/cobalt/db.py` (`:155-269`); `ops/desk/desk-launch.sh` (`:1768-1775`); `ops/desk/authorize.sh` (`:284-297`); `tests/cobalt/test_db_apply.py`; `tests/cobalt/test_db_apply_db.py`; `tests/ops/test_desk_launch_prodwrite.py`; `tests/ops/test_authorize.py` (`:39-95`, `:320-456`); `docs/40 - DevDocs/cobalt/db_apply.md`; `<S>/house-a.md`. Plus the range diffs by `git diff` (ops, config, CLI wiring, `uv.lock`, the hub).
- Check of `db-apply-prod-1012`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: db-apply-prod-1012 · pass: 1 · tip: fba1454e · house A: Grok FINDINGS: 3 · findings: 6 · dropped: 0 · held: 5 · fixed: 5 · held unfixed: 0 · open: 1 · house B: none (not needed) · suites: offline 4309/0 · with-DB 5212/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar · files opened: 15 · ready: YES · decisions: 3 · for Dejan: 0 · tokens: 290333
