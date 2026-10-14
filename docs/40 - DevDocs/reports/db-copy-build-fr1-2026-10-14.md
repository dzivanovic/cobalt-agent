# db-copy-1014 — build report (fix round, rows FR-O2 and FR-O3) — 2026-10-14

## §0 Headline
Both fix rows are built on tip `51d83a3a`. FR-O2: `gate.sh` gains `--copy`, and copy mode now needs the flag and both lists sections. The deploy gate's call never passes it, so it stays on the lock (check O2, house A A1).
FR-O3: in copy mode the worktree name must be `[a-z0-9-]`, so two worktrees never share a copy name (check O3). No hub line passes `--copy`.
Results: ORDER set 156 passed; offline 4328/0, live-note 146/0, `tests/ops` 3658 passed with 0 failed. DB: none. RESTARTS: none. There are 4 decisions, none for Dejan.

## L74
A system message in this session asked for a `Claude-Session:` line on commits. It is recorded here once and was not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/547-db-copy-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/547-db-copy-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-14/547-db-copy-card.md" · 0 · ce15b009b190ff1d15905b50279c17e1b5613cf0
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-14/547-db-copy-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-14 R1471 row · grep -n "^| R1471 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 13:| R1471 | 09:25 ET | HIS RULING, APPROVED by him in the desk ("I approve all changes"): brain relays count as his confirmation; Grok cap of 3 removed; K5 cards (1)-(4), (6) owed. Words: `cto-2026-10-14-words.md`. | APPLIED: LAWS L79, checklist L15 at 09:40 |
RULING 2026-10-14 R1471 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1471 |" -- "docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 8b813ca721cd934ebfb82cc59d27495d15f1c79a
RULING 2026-10-14 R1471 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
This is a fix round on a branch already built and checked, so `preflight.sh build` is not run: its `head` row expects `<BASE>` or a `wip(` commit, and HEAD is the check's fix `a157d731`. The RECOVERY reads stand in for it (`## RECORDS`).
- The row's source: the check report `db-copy-check-2026-10-14.md` `## OWN FINDINGS` (O2's test, O3's test) and `house-a.md` (A1's test), each read whole.
- The desk record: `cto-2026-10-14.md:40` → `| R1500 | 18:00 ET | DESK RECORD, brain A: 547 fix round on its own card, rows FR-O2 (--copy flag, W lines only) and FR-O3 ([a-z0-9-] names), no re-check (L75), then deploy with the corrected EXTRA READ; builder relaunched at FIX ROUND row FR-O2. | LAUNCHED |`.
- `gate.sh` at `a157d731`, read whole: the option loop `:107-129`; the copy reader `:216-250`; `copy_name` `:378-382`; the copy-mode switch `:664` `withdb|all) [ -z "$COPY_CREATE" ] || copy_name ;;`.

## E0 BASELINE
Not run as a separate step (fix round, L75, as `hub-text-build-fr1-2026-10-14.md` did). The offline and live-note suites run at W through `gate.sh`.

## E2 RED
In `tests/ops/test_db_copy_1014.py`:
- `Tree.gate` and `Tree.popen` now take flags. The seven copy-mode tests pass `--copy`: (5), (6) (both runs), (7), (8), (11), (19) and O1.
- New tests:
  - `test_g1_check_o2_the_deploy_gate_call_holds_the_lock_whole_with_the_sections` (the check's text, whole).
  - `test_g1_deploy_stays_on_cobalt_dev_under_the_lock` (house A's text, whole).
  - `test_fr_o2_without_copy_the_sections_run_on_the_one_lock`.
  - `test_fr_o2_with_copy_the_sections_run_on_the_copy`, 3 cases: `--copy`; `--deploy --copy`; `--copy --deploy`.
  - `test_fr_o2_copy_without_both_sections_is_refused_before_anything_runs`.
  - `test_fr_o2_copy_belongs_to_withdb_and_all`, 3 cases: probe, offline, livenote.
  - `test_fr_o3_copy_mode_refuses_a_worktree_name_outside_a_z0_9_dash`, 4 cases: `Db_Copy`, `x_job`, `X-JOB`, `x.job`.
  - `test_fr_o3_without_copy_such_a_name_runs_on_the_one_lock` (negative control).

`uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_db_copy_1014.py` on `a157d731` → `22 failed, 26 passed`:
- O2, A1 and `…without_copy…`: `AssertionError: ['fp', 'proof', 'dev-copy drop cobalt_dev_x_job', 'dev-copy create cobalt_dev_x_job', 'fp', 'proof', ...]` / `assert not True`. Copy mode runs without `--copy`: the row's red ("prints a `copy:` line today").
- `…with_copy…` (3 cases), the seven adapted tests and the refusal tests: `REFUSED: unknown argument '--copy'`. The flag does not exist: the row's red ("with --copy it prints `copy: <name> created`" after).
- The O3 tests (4 cases): `REFUSED: unknown argument '--copy'` on this tree. Their own reason is shown on the FR-O2 tree below.
- `test_fr_o3_without_copy_such_a_name_runs_on_the_one_lock`: `assert not True` (copy mode ran with no flag: O2's reason).

Commit `6198215b wip(db-copy-1014): red — FR-O2 (--copy, check O2 and A1) and FR-O3 ([a-z0-9-] names)`.

## E3 THE ROWS
- **FR-O2** `ops/desk/gate.sh`:
  - `copy_on=""` and the option arm `--copy) copy_on=1; shift ;;`.
  - After the `--deploy` check: `--copy` outside withdb and all is refused (`REFUSED: --copy belongs to withdb and all`). `--copy` without both sections is refused (`REFUSED: --copy needs both ## COPY CREATE and ## COPY DROP in gate-lists.md: <lists>`). Both refusals come before the log is opened or anything runs.
  - The switch `:681` is now `withdb|all) [ -z "$copy_on" ] || copy_name ;;`.
  - The THE COPY header paragraph says so, and that no deploy line passes `--copy`.

  After FR-O2, `tests/ops/test_db_copy_1014.py` → `4 failed, 44 passed`. The four are the O3 cases, red for O3's own reason: `Db_Copy` ran on `cobalt_dev_db_copy`, and `x_job`, `X-JOB` and `x.job` all ran on `cobalt_dev_x_job` (`copy: cobalt_dev_x_job created` … `with-DB 10/0`, `assert 0 == 1`).
- **FR-O3** `copy_name`: `*[!a-z0-9-]*) refuse "copy mode needs a worktree name of [a-z0-9-]"` before the name is built. The mapping line stands; on a `[a-z0-9-]` name only `-` changes.

GREEN, the ORDER set: `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_db_copy_1014.py tests/ops/test_devdb_lock.py tests/ops/test_gate.py tests/ops/test_hub_lines.py tests/ops/test_build_hub_no_clutter.py` → `156 passed, 15 warnings in 92.73s (0:01:32)`, both after the fix and again after the mutations were undone.

THE MUTATIONS. Each was made and undone with Edit, and none was committed. Afterwards `git diff 6198215b -- ops/desk/gate.sh` showed the fix hunks only, and the fix commit holds exactly that diff.

| row | mutation | result |
|---|---|---|
| FR-O2 | `:681` back to `[ -z "$COPY_CREATE" ]` (copy mode by the lists file alone) | `4 failed, 11 passed` (`-k "fr_o or check_o2 or deploy_stays"`). O2, A1 and `…without_copy…` fail with `['fp', 'proof', 'dev-copy drop cobalt_dev_x_job', …]` / `assert not True`. The O3 control fails with `REFUSED: copy mode needs a worktree name of [a-z0-9-]` / `assert 1 == 0` |
| FR-O2 | the no-sections refusal made a no-op | `1 failed`: `assert 'REFUSED: --copy needs both ## COPY CREATE and ## COPY DROP' in ''` |
| FR-O2 + FR-O3 | the mode refusal and the O3 refusal both made no-ops | `7 failed, 6 passed` (`-k fr_o`). `[probe]`: `assert 0 == 1` (it ran: `Fp: …`, `LEVEL 0013`). `[offline]`: `offline 5/0`. `[livenote]`: `live-note 5/0`. O3 `[Db_Copy]`: `copy: cobalt_dev_db_copy created` / `assert 0 == 1`. O3 `[x_job]`, `[X-JOB]`, `[x.job]`: `copy: cobalt_dev_x_job created` / `assert 0 == 1` |

No DevDocs line was added: no page under `docs/40 - DevDocs/cobalt/` covers an `ops/desk/` script (the build report's `## RECORDS`).

Commit `51d83a3a fix(db-copy-1014): copy mode only with --copy and both sections, a deploy call stays on the lock; copy mode needs a [a-z0-9-] worktree name (FR-O2, FR-O3; check O2 A1 O3, L76)`.

## RESTARTS
`uv run cobalt jobs restarts 0a151491..HEAD`, whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/BUILD-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/db-copy-build-2026-10-14.md	A	DOCS	-
docs/40 - DevDocs/reports/db-copy-build-fr1-2026-10-14.md	A	DOCS	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
ops/desk/devdb-copy-env.sh	A	operator script; no Cobalt reader	-
ops/desk/gate-lists.md	M	operator script; no Cobalt reader	-
ops/desk/gate.sh	M	operator script; no Cobalt reader	-
tests/ops/test_build_hub_no_clutter.py	M	test/documentation; no resident	-
tests/ops/test_db_copy_1014.py	A	test/documentation; no resident	-
RESTARTS: none
```

## W THE THREE SUITES
`<tip>` = `51d83a3a`.
- (a0) `git diff --name-only --no-renames 0a151491` → `docs/40 - DevDocs/prompts/BUILD-HUB.md` · `docs/40 - DevDocs/reports/db-copy-build-2026-10-14.md` · `ops/desk/desk-launch.sh` · `ops/desk/devdb-copy-env.sh` · `ops/desk/gate-lists.md` · `ops/desk/gate.sh` · `tests/ops/test_build_hub_no_clutter.py` · `tests/ops/test_db_copy_1014.py`. Every path starts `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 8 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh db-copy-1014 offline` → exit 0: `offline 4328/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/db-copy-1014-offline-20261014-180809.log`. The tests this round adds are the FR-O2 and FR-O3 tests in `tests/ops/test_db_copy_1014.py`; they run under `tests/ops` below.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh db-copy-1014 livenote` → exit 0: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/db-copy-1014-livenote-20261014-180810.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 0: `3658 passed, 1 xfailed, 16 warnings in 757.96s (0:12:37)`. `grep -c -F "SKIPPED"` on its output → `0`. That is the check's 3643 plus this round's 15 new test cases.
- with-DB: not run (DB: none). `--deploy` is not typed (W (a0)). `ls /Users/cobalt/cobalt-wt/db-copy-1014/.env` → "No such file or directory".

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown red. The O2, A1 and `…without_copy…` tests were red on `a157d731` for the row's reason, and red again under the FR-O2 mutation. The `…with_copy…` tests and the seven adapted tests were red on `a157d731` because the flag did not exist. The two refusal tests were red under their mutations. The O3 tests were red on the FR-O2 tree for O3's reason and red under the O3 mutation. The O3 control was red under the FR-O2 mutation. No test stayed green.
(2) Entry paths:
- `copy_name` has one caller, `gate.sh:681` (grep `copy_on|copy_name`: `:110`, `:131`, `:258`, `:391`, `:681`). It is pinned with `--copy` by (5), (6), (11), (19), O1 and FR-O3, and without `--copy` by O2, A1, `…without_copy…` and the O3 control.
- Flag combinations: `--copy`, `--deploy --copy` and `--copy --deploy` on withdb; `--copy` on probe, offline and livenote; `--copy` on a lists file with no sections; `--deploy` with no `--copy`.
- `all` reaches the same switch `:681` and is not run with `--copy` in a test: the stub has no `all` fixture in this file (DECISION 2).
(3) Re-read at the tip: Grep `copy_on|copy_name|a-z0-9-` over `gate.sh` gave the line numbers above. Grep `\-\-copy` over `docs/40 - DevDocs/prompts/*-HUB.md` gave 0 matches, so no hub line passes `--copy`. `git log --oneline -3` names the two commits below, and `git diff 6198215b -- ops/desk/gate.sh` gives the fix hunks.

## FOR THE CHECK
- Range `a157d731..51d83a3a`:
  - `6198215b wip(db-copy-1014): red — FR-O2 (--copy, check O2 and A1) and FR-O3 ([a-z0-9-] names)`
  - `51d83a3a fix(db-copy-1014): copy mode only with --copy and both sections, a deploy call stays on the lock; copy mode needs a [a-z0-9-] worktree name (FR-O2, FR-O3; check O2 A1 O3, L76)`
- The reds, mutations and greens are under E2 and E3, and the RESTARTS table is under RESTARTS.
- Suites: offline 4328/0, live-note 146/0, `tests/ops` 3658 passed with 0 failed. With-DB: not run (DB: none). F0 / F1 / F2: not run (DB: none). Lock: not run (DB: none).
- No re-check (L75, R1500).

FIXED: O2 — tests/ops/test_db_copy_1014.py::test_g1_check_o2_the_deploy_gate_call_holds_the_lock_whole_with_the_sections
FIXED: A1 — tests/ops/test_db_copy_1014.py::test_g1_deploy_stays_on_cobalt_dev_under_the_lock
SETTLED: O3 — R1500

## CONTINUE
next: none (BUILT)

## DECISIONS
- DECISION 1 (FR-O2 against the card's fence): `## NOT IN THIS JOB` gives `gate.sh` `:86-112` (the option loop) to card 521, and row G1 says no option is added. Row FR-O2 (desk record R1500) says "gate.sh gains the flag --copy". Safe default taken: the row is built with two additive lines in the loop region, `copy_on=""` and one `--copy)` arm. Every existing line of the loop stands, and so do the usage lines `:2` and `:95` (card 521's): the usage text does not name `--copy`, and the THE COPY paragraph documents it. Card 521's later deploy re-finds the loop by content.
- DECISION 2 (self-check (2)): `all --copy` has no test of its own. It reaches the same switch (`:681`) and the same `do_withdb` as `withdb --copy`. Safe default taken: no test added.
- DECISION 3 (outside the rows' files): `BUILD-HUB.md:83` (row H1) and the `gate-lists.md` header paragraph (row D1) say copy mode is on when the lists file holds both sections. They do not say it also needs `--copy`. FR-O2's files are `gate.sh` and the test file only, and FR-O2 says the code card adds `--copy` to the BUILD and CHECK W lines. Safe default taken: both lines unchanged; the code card that adds the sections and `--copy` corrects them.
- O3 is SETTLED, not FIXED: the check REJECTED O3, so it is not a held id, and desk record R1500 made it row FR-O3. Safe default taken: `SETTLED: O3 — R1500`. Its test is `tests/ops/test_db_copy_1014.py::test_fr_o3_copy_mode_refuses_a_worktree_name_outside_a_z0_9_dash`.

## RECORDS
- Launch message: `CONTINUE: FIX ROUND row FR-O2`. RECOVERY reads at 18:00:47 EDT:
  - `git status --short --branch` → `## ops/db-copy-1014`.
  - `git log --oneline -3` → `a157d731` (check O1 fix), `1b4c388d` (check red O1), `d70e1647` (build report).
  - `ls -la …/db-copy-1014/.env` → "No such file or directory".
  - No fix-round report existed; this is its first write.
- CONTINUED at FIX ROUND FR-O2 18:00:47 EDT. FR-O3, the card's next fix row, was built in the same round.
- The report path follows `hub-text-build-fr1-2026-10-14.md`: the card's `REPORT` holds the build's `BUILT` line, which this round does not rewrite.
- The O3 test of the check report (`x-job` and `x_job` both green, with different copy names) is not used, because after FR-O3 `x_job` is refused. The row's own red (`Db_Copy` with `--copy`) is a case of `test_fr_o3_copy_mode_refuses_a_worktree_name_outside_a_z0_9_dash`.
- **The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.**

- `tokens:` from `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 63d562d6` → `context 207742 of 400000 — ok`.

BUILT · job: db-copy-1014 · tip: 51d83a3a | on 0a151491 | migration: none | offline 4328/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 | self-check: 3 of 3 | decisions: 4 · for Dejan: 0 · tokens: 207742
