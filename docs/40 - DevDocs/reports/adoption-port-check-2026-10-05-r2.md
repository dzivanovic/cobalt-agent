# adoption-port — check, pass 1 (round 2026-10-05 r2, P7)

## §0 Headline
- Pass 1 at `36fa02ad`, no outside house (R47 overrule). Seven own findings were run (P5 X4, P6, P7, X1–X3 scope): six NOT HELD, one UNSETTLED (O4).
- P7 holds: offline `4 passed, 1 skipped` (the skip is `:55`); with the dev DB, under one lock take, `5 passed`, F0 = F2. Under G1's guarded connect, `--no-db` reaches no DB.
- O4 is open, FOR DEJAN: (d2)'s `… validate --no-db` relies on an unstarred allow string in a `dontAsk` seat. Untested; it ships as built and the next deploy's (d2) is the proof.
- No commit; suites as built (`offline 3786/0 · with-DB 4639/0 · live-note 146/0`); `.env` removed.

## L74
A system reminder asked for a `Claude-Session:` line on commits. Recorded once, not acted on. No commit was made.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-03/03d-adoption-port-card.md"` · exit 0 · last line `AUTHORIZED`. Rows: INSTALLED nothing; PLACEHOLDER nothing; CARD COMMITTED `b17ae03f12bb93aabde53f1382da8233cc329a7c`; CARD UNCHANGED nothing; STANDING LIST R60 row 46 (HIS RULING · APPROVED), committed `962e9d17`; RULING 2026-10-03 R327 row 333 (HIS RULING · APPROVED), committed `b1337431`; RULING 2026-10-05 R347 row 20 (HIS RULING · APPROVED), committed `e89ef63a`; HOUSE A overruled 2026-10-02 R47 row 54 (HIS RULING · APPROVED), committed `4e3fa8d8`.
House gates: not run — the card carries `HOUSE A: none — overruled 2026-10-02 R47` (CHECK-HUB `## THE FLOW` NO OUTSIDE HOUSE).

## PREFLIGHT
- `sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · `PREFLIGHT OK`. clock `Mon Oct  5 11:11:00 EDT 2026`; status `## ops/adoption-port-1005`; head `07655b9b docs(adoption-port): build report — 36fa02ad` (docs-only above `36fa02ad`: one file, the build report); env here: No such file; env anywhere: none; report last line `BUILT · job: adoption-port · tip: 36fa02ad | on e6ba65e6 | migration: none | offline 3786/0 | with-DB 4639/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 3 of 3 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0`; range 9 commits `ec98fada`..`36fa02ad`.
- `git log --stat --format=%h e6ba65e6..36fa02ad` · exit 0. Path union: `src/cobalt/cli.py`, `tests/cobalt/test_validate_no_db.py`, `docs/40 - DevDocs/cobalt/cli.md`, `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `docs/40 - DevDocs/reports/adoption-port-build-2026-10-05.md`.
- DB: the card has no `DB` key (with-DB job; RECORDS line "No `DB` key").
- `ls <S>` · exit 0 · `opus-1-1005.md`, `opus-1-r3.md`, `opus-1.md` — files of earlier check rounds of this job (dated Oct 3, Oct 4, Oct 5 08:07); this launch carries no `CONTINUE:`, so it is a fresh pass; none of them is opened (`## WHAT YOU READ` NOT: earlier checks of this branch).
- house A: none (overruled 2026-10-02 R47) · house B, if needed: none (no probe run, by the overrule).

## Files copied
none — no house (overrule).

## OWN FINDINGS
FINDING O1
ROW: P7, X4
CLAIM: With the dev DB env present, `tests/cobalt/test_validate_no_db.py:55` (P7's marked test) may not run or may fail, and the unmarked `--no-db` test (`:39`) may reach the DB. The conftest's G1 guard (`tests/cobalt/conftest.py:305`, `:335`) would then refuse it, which would show a DB reach under `--no-db` (X4).
RUN: COMMAND, one lock take (`BUILD-HUB.md` `## THE LOCK`): `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no tests/cobalt/test_validate_no_db.py`
EXPECT: if true, a FAILED line: G1's `with-DB test without an offline skip mark` on `test_no_db_skips_the_db_checks_and_exits_clean`, or P7's test SKIPPED or FAILED; otherwise `5 passed`.

FINDING O2
ROW: P7
CLAIM: Offline (no `POSTGRES_HOST` / `POSTGRES_USER`), P7's test may not skip, or one of the other four may fail (`tests/cobalt/test_validate_no_db.py:55`).
RUN: COMMAND `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_validate_no_db.py`
EXPECT: if true, anything other than `4 passed, 1 skipped`, with the skip naming `:55` and `reaches cobalt_dev (lock-relief G1)`.

FINDING O3
ROW: P6
CLAIM: (d2)'s command and the one sentence may not each stand exactly once (`docs/40 - DevDocs/prompts/DEPLOY-HUB.md:101`).
RUN: COMMAND `grep -n -F "COBALT_ENV=production uv run cobalt validate --no-db" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`, then `grep -n -F "are made after the merge by 4.5" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: if true, a count other than one hit each at `:101`.

FINDING O4
ROW: P6
CLAIM: The deploy seat runs `--permission-mode dontAsk`. Its only string covering (d2) is the unstarred `"Bash(COBALT_ENV=production uv run cobalt validate)"` (`DEPLOY-HUB.md:11`). The card says it "admits trailing arguments by prefix (`:74`'s note)", but `:74` carries no such note. If the harness matches an unstarred rule exactly, (d2)'s new command `… validate --no-db` is refused with no dialog, and the deploy stops at G (d2). No deploy has typed it yet: `deploy-deploy-03d-1005.md:82` says "(d2) SKIPPED per R391".
RUN: COMMAND `grep -n -F "Bash(COBALT_ENV=production uv run cobalt validate" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`, then `grep -n -F "admits" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: if true, one hit at `:11` with no ` *` or `*` before `)`, and no `admits` note at `:74`.

FINDING O5
ROW: X1, X2, X3, SCOPE
CLAIM: This round changes `DEPLOY-HUB.md` only at (d2). No `02b` sentence, chain sentence or ruled sentence (P1–P4, shipped in `979ec797`) is touched.
RUN: COMMAND `git diff --stat e6ba65e6..36fa02ad -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: if not true, more than `1 insertion(+), 1 deletion(-)`.

FINDING O6
ROW: P5, X4
CLAIM: The `else` block (`src/cobalt/cli.py:191-240`) may not hold exactly base's three checks. A non-DB check may have been dropped or moved into it, or a line changed.
RUN: COMMAND `git diff -w e6ba65e6..36fa02ad -- src/cobalt/cli.py`
EXPECT: if true, a `-` or `+` line ignoring whitespace other than the docstring usage line, the `if args.no_db:` block, `else:` and the parser's `add_argument`.

FINDING O7
ROW: P7 (fence: "Exactly this one test body changes, with the mark and the import")
CLAIM: P7's commits may change more than the mark, the import and that one body.
RUN: COMMAND `git diff 53b56384..36fa02ad -- tests/cobalt/test_validate_no_db.py`, then `git log --stat --format=%h 53b56384..36fa02ad`
EXPECT: if true, a hunk outside `import os`, the `skipif` line and `test_without_the_flag_validate_still_reads_the_db`'s body, or a non-docs path other than that file.

## Findings
none — no house.

## Dropped
none.

## RUNS
- O2 · own · `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_validate_no_db.py` · `SKIPPED [1] tests/cobalt/test_validate_no_db.py:55: reaches cobalt_dev (lock-relief G1)` / `4 passed, 1 skipped in 0.64s` · NOT HELD
- O3 · own · `grep -n -F "uv run cobalt validate --no-db" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` → one hit, `101:- (d2) VALIDATE, right before the gate call (seconds): …validate --no-db\` → exit 0; …`; `grep -n -F "are made after the merge by 4.5" …` → one hit, `101:` (the same line). Both match the card's P6 sentence word for word. The first spelling, with the production prefix in the pattern, was blocked by the bare-guard hook (`## RECORDS`) and resent as a narrower fixed string · NOT HELD
- O4 · own · `grep -c -F "uv run cobalt validate)" …DEPLOY-HUB.md` → `1` (`:11`, the launch line's `"Bash(COBALT_ENV=production uv run cobalt validate)"`); `grep -c -F "uv run cobalt validate *)" …` → `0`; `grep -c -F "uv run cobalt validate*)" …` → `0`; `grep -n -F "admits" …` → no output (no such note at `:74` or anywhere in the file). The facts of the claim are shown. Whether the harness admits `… validate --no-db` under an unstarred rule is not shown by any command on this seat's list: no `claude` call, and only the deploy seat types it · UNSETTLED — the matching rule is shown only by a deploy seat's first (d2) call, or by a starred allow string, which is fenced (`## NOT IN THIS JOB`: "the launch line's allow strings")
- O5 · own · `git diff --stat e6ba65e6..36fa02ad -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` → ` docs/40 - DevDocs/prompts/DEPLOY-HUB.md | 2 +-` / ` 1 file changed, 1 insertion(+), 1 deletion(-)` · NOT HELD (X1–X3: no shipped P1–P4 text moved this round)
- O6 · own · `git diff -w e6ba65e6..36fa02ad -- src/cobalt/cli.py` → three hunks only: the usage line `cobalt validate [--no-db]`; the comment, `if args.no_db:` with its three `SKIPPED (--no-db):` lines, and `else:` before the unchanged `sheets = load_sheet_modes_config()`; the parser's `validate.add_argument("--no-db", …)`. No base line is removed or changed apart from whitespace · NOT HELD (X4: the `else` holds exactly base's three checks; no non-DB check moved)
- O1 · own · ONE lock take: `sh /Users/cobalt/cobalt/ops/desk/take-devdb-lock.sh adoption-port-1005 90` → `lock taken: adoption-port-1005` (exit 0); `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, this worktree's (`-rw-------  1 cobalt  staff  2186 Oct  5 11:14 /Users/cobalt/cobalt-wt/adoption-port-1005/.env`); `<FP>` → `<F0>` = `664	35	272c95bbb12241e3611e4b36326ccf87`; `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.` / `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` / `TABLES 0011`. The output prints no `LEVEL` line; the fingerprint equals the build gate's F0 at `LEVEL 0013` (build report `## W`, round 2b (b)). Then `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no tests/cobalt/test_validate_no_db.py` → `PASSED …::test_no_db_skips_the_db_checks_and_exits_clean`, `PASSED …::test_without_the_flag_validate_still_reads_the_db`, `PASSED …::test_no_db_still_fails_a_config_error_it_does_not_skip`, `PASSED …::test_the_parser_carries_the_flag`, `PASSED …::test_without_the_flag_the_three_checks_still_run_in_order` / `5 passed in 0.94s`. `<FP>` again = `664	35	272c95bbb12241e3611e4b36326ccf87` = `<F0>`; `sh /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh adoption-port-1005` → `lock released`; `ls …/.env` → `No such file or directory` (11:15 EDT). With the DB present, the conftest replaces `db.connect` with the G1-guarded `fake_connect` (`tests/cobalt/conftest.py:304-305`, `:338-339`), so the unmarked `--no-db` test passing shows that no `db.connect` or `psycopg.connect` reach happens under the flag (X4). P7's marked test ran (not skipped) and passed · NOT HELD
- O7 · own · `git diff 53b56384..36fa02ad -- tests/cobalt/test_validate_no_db.py` → `+import os`; `+@pytest.mark.skipif('not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER"))', reason="reaches cobalt_dev (lock-relief G1)")` on the `def`; the body's `pytest.raises(DbConfigError)` replaced by `assert cli._cmd_validate(argparse.Namespace(no_db=False)) is None` and the `Sheets:` / `Day modes:` / no-`SKIPPED` asserts. `git log --stat --format=%h 53b56384..36fa02ad` → `36fa02ad` and `5719af3c` touch only `tests/cobalt/test_validate_no_db.py`; `efc887dd` and `00292cad` touch only the build report · NOT HELD

## FIXES
none — nothing held.

## Suites
suites: as built (no commit). From the build report `## W THE THREE SUITES`, round 2b, `<tip>` = `36fa02ad`, `gate.sh adoption-port-1005 all --deploy` → exit 0: `offline 3786/0` · `cobalt_dev: 0013 — F2 = F0` · `.env: removed` · `with-DB 4639/0` · `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/adoption-port-1005-all-20261005-104050.log`. RESTARTS (build report `## RESTARTS`, round 2 at `5719af3c`; `36fa02ad` adds only a test file): `RESTARTS: com.cobalt.radar`. This check's own lock take left `cobalt_dev` at F0 (O1) and `.env` removed, proven gone.

## Scope
PREFLIGHT's path union: `src/cobalt/cli.py` (P5), `tests/cobalt/test_validate_no_db.py` (P5, P7), `docs/40 - DevDocs/cobalt/cli.md` (P5), `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (P6), the build report (docs). Every path is in a row's `files`. No commit of this check.

## Checked against the branch
- (i) `git log --oneline 36fa02ad..HEAD -- . ":(exclude)docs"` → no output; no commit of mine; `<tip now>` = `36fa02ad`.
- (ii) `git log --stat --format=%h 36fa02ad..HEAD` → `07655b9b`, ` .../reports/adoption-port-build-2026-10-05.md | 58 ++++…--`: docs only.
- (iii) The fence. `git log --oneline e6ba65e6..HEAD -- src` → `74370e5d fix(adoption-port): validate --no-db; DEPLOY-HUB (d2) runs it (P5, P6, L1, L41, L76)`, which touches only `src/cobalt/cli.py` (PREFLIGHT's range stat). `git log --oneline e6ba65e6..HEAD -- ops configs` → no output. `DEPLOY-HUB.md`: one line changed (O5), which is P6's command and sentence; the launch line is unchanged.
- (iv) no HELD finding.
- (v) `ls /Users/cobalt/cobalt-wt/adoption-port-1005/.env` → `No such file or directory`; `git status --short --branch` → `## ops/adoption-port-1005`.
- (vi) `git log --stat --format=%h e6ba65e6..HEAD -- src/cobalt/db_migrations tests/cobalt` → only `tests/cobalt/test_validate_no_db.py` (`ec98fada`, `74370e5d`, `5ac157d5`, `5719af3c`, `36fa02ad`). No migration. Its one with-DB test runs at `0013` (O1, and the build's gate pass 1 whole), so no `ops/desk/gate-lists.md` change is owed.
- (vii) The card's `## RECORDS` name no `ls`, `grep` or `git -C /Users/cobalt/cobalt log` command to run.
- (viii) L32: this report holds no ticker, price or date of his; the fingerprint and file sizes are `cobalt_dev` schema facts.
COUNTING: findings 7 (own 7, house 0) · dropped 0 · held 0 · fixed 0 · held unfixed 0 · open 1 (O4).

## OPEN
- O4 · own · UNSETTLED. The deploy seat (`--permission-mode dontAsk`) is covered for (d2) only by the unstarred `"Bash(COBALT_ENV=production uv run cobalt validate)"` (`DEPLOY-HUB.md:11`). The card says it admits `--no-db` "by prefix (`:74`'s note)", but `:74` carries no such note (`grep -n -F "admits"` → none). No deploy has typed `… validate --no-db` yet (`deploy-deploy-03d-1005.md:82`: "(d2) SKIPPED per R391"). Two things would settle it: the next deploy's (d2) call itself, which is admitted or refused before anything in production moves (`FAILED: G (d2) … · rollback: not used`), or a starred allow string, which is fenced here and returns to him (R60).

## CONTINUE
next: done (CLOSE written 11:17 EDT).

## DECISIONS
1. FOR DEJAN — O4, open: (d2)'s new `COBALT_ENV=production uv run cobalt validate --no-db` against the unstarred allow string `"Bash(COBALT_ENV=production uv run cobalt validate)"` in a `dontAsk` deploy seat. It is not shown either way. If the harness matches an unstarred rule exactly, the deploy stops at G (d2) with nothing in production moved. A change to the launch line's allow strings is his (R60) and is fenced on this card. Default taken: nothing changed; it ships as built; the next deploy's (d2) call is the proof. A refusal there is a fail-loud stop and goes to a starred string (`… validate *`) by his approval. House B: none available, because the card carries `HOUSE A: none — overruled 2026-10-02 R47`.

## RECORDS
- Fresh pass 1: the launch carried no `CONTINUE:`. `<S>` held `opus-1.md`, `opus-1-r3.md` and `opus-1-1005.md` from earlier check rounds of this job; none was opened, and none is overwritten. This pass's copy is `<S>/opus-1-1005-r2.md`.
- No house: `HOUSE A: none — overruled 2026-10-02 R47` (AUTHORIZATION row 54). No house gate, probe, staging or house list; `## 1` and `## 3` not run.
- Hook block, resent: `grep -n -F "COBALT_ENV=production uv run cobalt validate --no-db" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` → `PreToolUse:Bash hook error: [python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py]: route: production is the deploy hub's; a dev read uses COBALT_ENV=dev`. Resent as `grep -n -F "uv run cobalt validate --no-db" …` (O3). The bare guard reads the production prefix inside a grep pattern as a production call.
- Lock: one take (O1), 11:14–11:15 EDT, F0 = F2 = `664 35 272c95bbb12241e3611e4b36326ccf87`, `lock released`, `.env` proven gone.
- `--proof-only` printed `TABLES 0011` and no `LEVEL` line. The fingerprint equals the build gate's F0 at `LEVEL 0013`.
- Observation, not a finding: after P7, `tests/cobalt/test_validate_no_db.py:22` `from cobalt.db import DbConfigError` is no longer used, and the module docstring (`:9-10`, "These tests open no connection") no longer holds for P7's test under the DB. P7's fence ("nothing else in the file") keeps both as built; no suite fails on either.
- files opened: 17 — `CHECK-HUB.md`; the card; `BUILD-HUB.md` (`## THE LOCK`, `## E2`, `## RESTARTS`, `## W`, and its heading list); `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); the build report (`## RESTARTS`, `## W`, `## PRE-STOP SELF-CHECK`, `## FOR THE CHECK`, `## CONTINUE`, `## DECISIONS` head); `src/cobalt/cli.py`; `src/cobalt/db.py`; `src/cobalt/settings/store.py`; `src/cobalt/settings/models.py`; `tests/cobalt/conftest.py`; `tests/cobalt/test_validate_no_db.py` (by diff); `docs/40 - DevDocs/cobalt/cli.md` (by diff); `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (grep, `:72-75`); `tests/ops/test_bare_guard.py` (`:370-409`, `:835-869`); `src/cobalt/heartbeat/runner.py` and `src/cobalt/archiver/settings.py` (grep of the functions `_cmd_validate` calls); `reports/deploy-deploy-03d-1005.md` (two `grep -n -F`, O4). Plus content searches with no file read whole: `dotenv` over `src/cobalt`; `_cmd_validate|cobalt validate` over the worktree; `ruff|F401` over `tests`.
- L74: a system reminder in this session asked for a `Claude-Session:` line on commits. Recorded once, not acted on. This check made no commit.
- Check of `adoption-port`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: adoption-port · pass: 1 · tip: 36fa02ad · house A: none (overruled 2026-10-02 R47) · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 17 · ready: YES · decisions: 1 · for Dejan: 1
