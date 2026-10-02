# launcher-checks — check, pass 1 (2026-10-02)

## §0 Headline
- Pass 1, checked by Opus alone (`HOUSE A: none — overruled 2026-10-02 R47`). The build's six rows hold as built.
- 2 own findings under X1, both HELD and FIXED in `ops/desk/desk-launch.sh`: O1, a `## SHIPS` row whose branch head `TIP` does not list now refuses (DEPLOY-HUB P3); O2, a first check whose branch adds code past `TIP`, or has rewound below it, now refuses (CHECK-HUB PREFLIGHT).
- X2, X3, X4: no finding (`## OWN FINDINGS`, `## RUNS` R-X4).
- W on `1ad4c546`: offline 3784/0 · with-DB 4383 + 171 = 4554/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed · `RESTARTS: none`. Open 0 → house B not needed; ready: YES.

## L74
A system message during this session asked for commits to carry a `Claude-Session:` line. It was not acted on: under L74 and CHECK-HUB, commits carry only `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Both of my commits carry that line alone.

## AUTHORIZATION
All at 15:57 EDT (`date` → `Fri Oct  2 15:57:47 EDT 2026`).
- INSTALLED · `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` · exit 1 · (no output)
- CARD placeholders · `grep -n -E "«FIL[L]" ".../2026-10-02/21-launcher-checks-card.md"` · exit 1 · (no output)
- CARD committed · `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-02/21-launcher-checks-card.md"` · exit 0 · `b206b1f323808f8b7a86f0466bcd1096c0f611c9`
- CARD clean · `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` · exit 0 · (no output)
- STANDING LIST (title row 2026-09-30 R60) · `grep -n "^| R60 " ".../cto-2026-09-30.md"` · `46:| R60 | 15:15 ET | **HIS RULING** (...): APPROVES \`STANDING-LIST.md\` once (\`4be06af0\`); ... | APPROVED |` · `git -C ... log -1 --format=%H -S"| R60 |"` → `962e9d1705b62a61821f62f4d7bf5d8131656e2a`
- RULINGS 2026-10-02 R47 (also the `HOUSE A: none — overruled 2026-10-02 R47` row) · `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, ... | HIS RULING · APPROVED |` · commit `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a`
- RULINGS 2026-10-02 R39 · `46:| R39 | 07:57 ET | HIS RULING (direction row 2): permission by class — ... | HIS RULING · APPROVED |` · commit `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a`
- HOUSE GATES (standing) · `grep -n "^| R17 "` → line 35, one row · `grep -n "^| R19 "` → line 37, one row · `-S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c`. Not used: house A none (overruled 2026-10-02 R47).

## PREFLIGHT
- date · `Fri Oct  2 15:57:47 EDT 2026`
- branch · `git status --short --branch` · 0 · `## ops/launcher-checks-1002`
- tip · `git log --oneline -1` · 0 · `7be1c888 docs(launcher-checks): build report — 039ccab9`; `git log --stat --format=%h 039ccab9..HEAD` · 0 · `7be1c888` and `832d86e3`, each only `.../reports/launcher-checks-build-2026-10-02.md` (docs only)
- built · `tail -n 3 "<REPORT>"` · 0 · last line `BUILT · job: launcher-checks · tip: 039ccab9 | on 63649058 | migration: none | offline 3784/0 | with-DB 4554/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 6 of 6 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0`
- range · `git log --oneline 63649058..039ccab9` · 0 · 6 commits: `039ccab9` fix (L3, L5, R41), `6c4d4737` wip red (L3, L4), `b3ec073c` docs, `4f60f644` wip W (b) lock held, `a2dd9400` feat (L1–L6), `b4d38eda` wip red (L1–L4)
- path union · `git log --stat --format=%h 63649058..039ccab9` · `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_prechecks.py`, `tests/ops/test_devdb_lock.py`, `tests/ops/test_desk_size_guard.py`, `tests/ops/test_desk_launch_devfix.py`, `docs/40 - DevDocs/prompts/STANDING-LIST.md`, `docs/40 - DevDocs/reports/launcher-checks-build-2026-10-02.md`
- lock · `ls <WT>/.env` · 1 · `No such file or directory` · `ls -la /Users/cobalt/cobalt-wt/*/.env` · 1 · `no matches found: /Users/cobalt/cobalt-wt/*/.env`
- scratch · `ls <S>` · 1 · `No such file or directory` (fresh)
- house · `house A: none (overruled 2026-10-02 R47)`; no house gate and no probe run in PREFLIGHT; HOUSE B: as needed.

## Files copied
none — house A none (overruled 2026-10-02 R47); `## 1` and `## 3` not run.

## OWN FINDINGS
Read before any run: the diff `63649058..039ccab9` (`ops/desk/desk-launch.sh` whole at the tip; the four `tests/ops/` files; `STANDING-LIST.md`), `DEPLOY-HUB.md` P2 (line 60) and P3 (line 61), `CARD.md` `## SHIPS`, `BUILD-HUB.md` `## STOP LINE`, the build report's `## RESTARTS`, `## W`, `## FOR THE CHECK` and last line.

FINDING O1
ROW: L3 (X1)
CLAIM: `ships_checked` (`ops/desk/desk-launch.sh:590`–`:593`) proves every TIP head is some row's branch head, but not the converse; DEPLOY-HUB P3 (`DEPLOY-HUB.md:61`) wants each row's branch head to be "the same value `TIP` lists", so a card with a clean `## SHIPS` row whose head is missing from `TIP` launches a deploy whose P3 is sure to fail.
RUN: TEST — `tests/ops/test_desk_launch_prechecks.py`:
```python
def test_x1_a_ships_row_whose_head_tip_does_not_list_refuses(desk):
    """DEPLOY-HUB.md P3: each row's branch head is 'the same value TIP lists' (check O1)."""
    git(desk.repo, "branch", "ops/y-job", desk.tip)
    other = desk.reports / "y-job-check.md"
    other.write_text(f"# y-job check\n\n{check_line(desk.tip)}\n\n")
    desk.deploy.write_text(desk.deploy.read_text().replace(
        "|\n\n## MARKERS",
        f"|\n| 2 | `ops/y-job` | `{desk.tip}` | `{desk.tip}` | `{other}` | `held unfixed: 0` and `ready: YES` |\n\n## MARKERS"))
    desk.ship()
    refused(desk, desk.launch("deploy", str(desk.deploy)),
            f"deploy ops/y-job: the branch head {desk.tip} is no head TIP lists")
    assert not desk.gate_left()
```
EXPECT: on `039ccab9` it fails at `assert done.returncode == 1` (`0 == 1`): the deploy launches.

FINDING O2
ROW: L2 (X1)
CLAIM: the check block (`ops/desk/desk-launch.sh:702`–`:719`) proves the BUILT line but not the worktree's head; CHECK-HUB PREFLIGHT (`CHECK-HUB.md:63`) fails a first pass-1 check whose branch has a non-docs commit past `TIP` (`FAILED PREFLIGHT: the tip is not the code tip`), and the launcher starts that worker.
RUN: TEST — `tests/ops/test_desk_launch_prechecks.py`:
```python
def test_x1_a_check_whose_branch_adds_code_past_its_tip_refuses(desk):
    """CHECK-HUB.md PREFLIGHT: HEAD is TIP or a docs-only commit above it (check O2)."""
    (desk.job_wt / "src" / "y.py").write_text("Y = 1\n")
    desk.commit_job("src past the tip")
    refused(desk, desk.launch("check", str(desk.card)), "the tip is not the code tip")
```
EXPECT: on `039ccab9` it fails at `assert done.returncode == 1` (`0 == 1`): the check launches.

CHECK ASKS read, no finding written: X2 — the controls for `RULINGS: none`, an old-shape line, `STEP-D0` (with and without a row) and `PASS-2` stand in the test file (`:318`, `:465`, `:494`, `:502`, `:360`); a carried held defect is expressed in the row's own literals, which L3 tests as the row says. X3 — `refused()` plus `gate_left()` after every L3 refusal (`:442`–`:449`, `:480`, `:491`); `ships_checked` runs at `:758`, before `add` is set (`:859`). X4 — run under `## RUNS` (R-X4).

## Findings
none — no house.

## Dropped
none.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_launch_prechecks.py::test_x1_a_ships_row_whose_head_tip_does_not_list_refuses` on `039ccab9` | `1 failed, 15 warnings in 1.41s`; first failing line `E       AssertionError: HEAD is now at c3054c1 check report` … `assert 0 == 1` in `refused()` (`:222`); stderr shows `worktree add -b deploy/x-deploy …` and `RUN: claude --bg …` | HELD |
| O2 | own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_launch_prechecks.py::test_x1_a_check_whose_branch_adds_code_past_its_tip_refuses` on `039ccab9` | `1 failed, 15 warnings in 1.26s`; `assert 0 == 1` in `refused()` (`:222`); stdout `WATCH: sh …/desk-watch.sh check "…/01-x-job-card.md"`, stderr `RUN: claude --bg "Read '…/CHECK-HUB.md' …` | HELD |
| R-X4 | own (X4) | `git diff 63649058 039ccab9 -- tests/ops/test_devdb_lock.py tests/ops/test_desk_launch_devfix.py tests/ops/test_desk_size_guard.py` | 3 files; every `+`/`-` line is a fixture line (a `cto-2026-01-02.md` write, the BUILT line, the `## SHIPS` row and its check report, `TIP: {tip}` → `TIP: {head}` on the deploy card in `test_devdb_lock.py:231`); no `assert` line among them | no finding (X4: no assertion changed) |

Red commit: `59709a8d wip(launcher-checks): check red — O1, O2`.

## FIXES
| id | file | change | proof |
|---|---|---|---|
| O1 | `ops/desk/desk-launch.sh` (`ships_checked`) | each `## SHIPS` row's branch head must be one of the `TIP` heads, else `REFUSED: deploy <branch>: the branch head <h> is no head TIP lists — add it to TIP, or drop its ## SHIPS row` (DEPLOY-HUB P3) | below |
| O2 | `ops/desk/desk-launch.sh` (check block) | on a first pass-1 launch (no step, no `PASS-2`): `TIP` must be an ancestor of the worktree's HEAD, and `git log --name-only TIP..HEAD -- . ':(exclude)docs'` empty, else `REFUSED: the tip is not the code tip — …` (CHECK-HUB PREFLIGHT); a resume and a `PASS-2` are not re-read (they sit on the check's own commits) | below |

Added with the fix, in `tests/ops/test_desk_launch_prechecks.py`: `test_x1_a_check_whose_tip_is_not_on_the_branch_head_refuses` (O2's ancestor clause) and the control `test_x1_a_check_resume_or_pass_2_on_its_own_code_commits_launches[E3|PASS-2]`. The header's refusal list names both. No DevDocs page exists for `ops/desk/desk-launch.sh` under `docs/40 - DevDocs/cobalt/` (Grep `desk-launch` there → `jobs/restarts.md` only), as the build found; none invented.
MUTATIONS (Edit, then undone): the O2 block's `if` → `if false; then` and O1's `case " $tip "` → `case " $shead "`; `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_desk_launch_prechecks.py -k x1_` → `3 failed, 2 passed, 50 deselected, 15 warnings in 2.97s` (O2, the rewound branch and O1 red with `assert 0 == 1`; the two controls green). Undone; `git diff --stat` → `ops/desk/desk-launch.sh | 20`, `tests/ops/test_desk_launch_prechecks.py | 18` (the fix, no mutation left).
After the fix: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `170 passed, 1 xfailed, 15 warnings in 106.24s (0:01:46)`; `… tests/ops/test_desk_launch_prechecks.py` → `55 passed, 15 warnings in 23.18s`.
Commit: `1ad4c546 fix(launcher-checks): a SHIPS row whose head TIP does not list, and a first check whose branch adds code past TIP or rewound below it, are refused (check O1, O2)`.

## Suites
RESTARTS first, `uv run cobalt jobs restarts 63649058..HEAD` (HEAD `1ad4c546`):
```
path	change	rule	restart
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/launcher-checks-build-2026-10-02.md	A	DOCS	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_desk_launch_devfix.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_prechecks.py	A	test/documentation; no resident	-
tests/ops/test_desk_size_guard.py	M	test/documentation; no resident	-
tests/ops/test_devdb_lock.py	M	test/documentation; no resident	-
RESTARTS: none
```
W on `<tip>` = `1ad4c546`:
- (a) OFFLINE `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → exit 0, `3784 passed, 673 skipped, 1 xfailed, 25 warnings in 596.40s (0:09:56)` → `<p>` = 3784. This check adds no test in these folders (its 5 new tests are in `tests/ops/`: `170 passed, 1 xfailed`, `## FIXES`).
- (b) THE LOCK: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/launcher-checks-1002/.env`; `ls -la …/*/.env` → one line, `-rw-------  1 cobalt  staff  2186 Oct  2 16:07 /Users/cobalt/cobalt-wt/launcher-checks-1002/.env`. Taken `Fri Oct  2 16:07:33 EDT 2026`. `<FP>` (typed as `BUILD-HUB.md` `## THE LOCK` gives it) → `<F0>`: `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`. `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `36 table(s) probed on cobalt_dev`. The `drc_*`, `legs`, `prediction_records` and `voice_turns` tables show `-` (not there), so `cobalt_dev` is at `0013`. No `CHANGED`. `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.` `code: 1ad4c546 (clean)`.
- (c) PASS 1: the pass-1 command byte for byte, no deselect added (no with-DB test in this check), run in the background → exit 0, `4383 passed, 7 skipped, 65 deselected, 3 xfailed, 31 warnings in 714.57s (0:11:54)` → `<d1>` = 4383. SKIPPED: `test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev` · `test_cards_picks.py:401: real S2-P2 0007 applied: …` · `test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — …` · `test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set` · `test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — …` · `taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — …` · `taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — …` (7, the build's same seven). No deadlock this time.
- (c2) FORWARD `COBALT_ENV=dev uv run cobalt db migrate` (foreground) → `0001` … `0011`, `0013` … `0022` applied in order; the eight tables `CREATED`; `content UNCHANGED on every table.`; no `CHANGED`; `code: 1ad4c546 (clean)`. **`dev forward: APPLIED Fri Oct  2 16:20:25 EDT 2026`**. `<F1>`: `893 · 44 · 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) PASS 2: the pass-2 command byte for byte (nothing added) → exit 0, `171 passed, 1 deselected, 5 warnings in 219.28s (0:03:39)`. No SKIPPED, FAILED or ERROR test line: the `| ERROR |` lines are the app's own log output of refusal tests. `<d2>` = 171; `<d>` = 4554.
- (c3r) no with-DB test of this check writes a ticker; `aset_sizings 1 -> 1`, `0824685c -> 0824685c` in both migrate tables.
- (e) LIVE-NOTE (`.env` absent, before the take) → `146 passed, 1 skipped, 15 warnings in 27.23s`. The skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, which does not name `COBALT_LIVE_VAULT_ROOT` → `<l>` = 146.
- (f) ROLLBACK `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) → `0022` … `0014` reversed newest first, the eight tables `DROPPED`, `content UNCHANGED on every table.` `<F2>`: `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` = `<F0>` field for field → **`cobalt_dev: 0013 — F2 = F0`**. The lock's (d): `rm /Users/cobalt/cobalt-wt/launcher-checks-1002/.env` → exit 0; `ls …/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`. Released `Fri Oct  2 16:24:56 EDT 2026`. `.env: removed, proven gone (W)`.

## Scope
PREFLIGHT path union: `ops/desk/desk-launch.sh` and `tests/ops/test_desk_launch_prechecks.py` (L1–L4), `tests/ops/test_devdb_lock.py`, `tests/ops/test_desk_launch_devfix.py` and `tests/ops/test_desk_size_guard.py` (L5), `docs/40 - DevDocs/prompts/STANDING-LIST.md` (L6), and the build report. My commits add `ops/desk/desk-launch.sh` and `tests/ops/test_desk_launch_prechecks.py`, both in rows L1–L4's `files`. L6's section is at `STANDING-LIST.md:31`, after `## NEVER` (`:16`) and before the `.env` pattern section (`:40`).

## Checked against the branch
- (i) `git log --oneline 039ccab9..HEAD -- . ":(exclude)docs"` → `1ad4c546 fix(launcher-checks): … (check O1, O2)` · `59709a8d wip(launcher-checks): check red — O1, O2`; `<tip now>` = `1ad4c546`.
- (ii) `git log --stat --format=%h 039ccab9..HEAD` → `1ad4c546`: `ops/desk/desk-launch.sh | 20`, `tests/ops/test_desk_launch_prechecks.py | 18`; `59709a8d`: `tests/ops/test_desk_launch_prechecks.py | 23`; `7be1c888`, `832d86e3`: the build report only. Both non-docs paths are in rows L1–L4's `files`. No `WIDENED`.
- (iii) the fence: `git log --oneline 63649058..HEAD -- .claude/settings.json` → empty; `… -- BUILD-HUB.md CHECK-HUB.md DEPLOY-HUB.md DEVFIX-HUB.md CARD.md` (under `docs/40 - DevDocs/prompts/`) → empty; `… -- ops/desk/desk-watch.sh ops/desk/desk-context.sh` → empty. The devfix and install-ops blocks, the desk-size guard and the lock tests' assertions: untouched by `1ad4c546` (its diff is the check block, `ships_checked` and the header list).
- (iv) `grep -n -F "def test_x1_a_ships_row_whose_head_tip_does_not_list_refuses" tests/ops/test_desk_launch_prechecks.py` → `519:`; `grep -n -F "def test_x1_a_check_whose_branch_adds_code_past_its_tip_refuses" …` → `368:`; their red commit `59709a8d` sits below the fix `1ad4c546` in (i).
- (vi) TREE STATE `unchanged`: `git log --stat --format=%h 63649058..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty.
- (vii) no line of the card's `## RECORDS` names an `ls`, a `grep` or a `git -C /Users/cobalt/cobalt log` command. The RESTARTS record matches the table under `## Suites`.
- (viii) L32: this report holds constructed values and repo hashes only.

## OPEN
none. Counts: findings 2 (O1, O2; no house) · dropped 0 · held 2 · fixed 2 · held unfixed 0 · open 0.

## CONTINUE
next: none — closed (8).

## DECISIONS
none.

## RECORDS
- Dropped findings: none (no house list).
- No house produced nothing, because none was seated: `house A: none (overruled 2026-10-02 R47)`. `## 1` and `## 3` were not run, `<S>` was not staged, and no house process was started.
- No `REFUSED, not needed` line; no `CONTINUED` line; one lock take (W), no extra.
- L74: one line, under `## L74`.
- The card's `## READ` item `deploy-2026-10-01-1.md` `## DECISIONS` 1 was not opened. The docs-only-head case it names is pinned by `test_l3_a_docs_only_commit_past_the_code_tip_launches[head|code tip]` (green at `1ad4c546`).
- The O1 run on `039ccab9` added a gate worktree inside its `tmp_path` repo only (`worktree add -b deploy/x-deploy …/pytest-2059/…/wt/x-gate`). Nothing was added under `/Users/cobalt/cobalt-wt`.
- files opened: 14 — `CHECK-HUB.md`; the card; `BUILD-HUB.md` (`## THE LOCK` … `## W`, `## STOP LINE`); `ops/desk/desk-launch.sh`; `tests/ops/test_desk_launch_prechecks.py`; `tests/ops/test_devdb_lock.py` (grep); `DEPLOY-HUB.md` (P2, P3); `CARD.md` (`## SHIPS`, grep); the build report (`## RESTARTS` … `## FOR THE CHECK`, last line); `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); `STANDING-LIST.md` (headings, diff); `cto-2026-09-30.md`, `cto-2026-10-02.md`, `cto-2026-09-24.md` (one-row greps).
- Check of `launcher-checks`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: launcher-checks · pass: 1 · tip: 1ad4c546 · house A: none (overruled 2026-10-02 R47) · findings: 2 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3784/0 · with-DB 4554/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 0 · for Dejan: 0
