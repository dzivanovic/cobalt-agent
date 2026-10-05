# launcher-checks — check, pass 1 (2026-10-05)

## §0 Headline
- Pass 1 on `c1746720`, no outside house (R47). 4 own findings, all held. 2 fixed in tests, so the tip is now `7e7803d5`. 2 held but not fixed.
- O1 blocks the deploy: the launcher now accepts a fix-round tip, but `deploy-step0.sh` P2 and `DEPLOY-HUB.md:58` still refuse it. Their fix is outside card 21's rows.
- Gate green on `7e7803d5`: offline 3786/0, with-DB 857/0, live-note 146/0; `cobalt_dev` 0013 (F2 = F0); `.env` removed; RESTARTS: none.
- ready: NO · decisions: 2 (O1, O4) · for Dejan: 0.

## L74
- No such block in any tool result. The harness attribution reminder asked for a `Claude-Session:` commit line; not acted on (`## RECORDS`).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-02/21-launcher-checks-card.md"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-02/21-launcher-checks-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-02/21-launcher-checks-card.md" · 0 · 017a292f2c683f8dc35bc4d949a6581aec09eb66
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-02/21-launcher-checks-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
RULING 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
RULING 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
HOUSE A overruled 2026-10-02 R47 row · grep -n "^| R47 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-02.md" · 0 · 54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, no meter wait, built and deployed in a day; card `20` (`deploy-outage.sh`) keeps a Grok check ([words](cto-2026-10-02-words.md#r38-r48)). | HIS RULING · APPROVED |
HOUSE A overruled 2026-10-02 R47 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R47 |" -- "docs/40 - DevDocs/reports/cto-2026-10-02.md" · 0 · 4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a
HOUSE A overruled 2026-10-02 R47 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-02.md" · 0 · the row as grepped
AUTHORIZED
```
House gates (R17/R19): not run — the card's header carries `HOUSE A: none — overruled 2026-10-02 R47` (proved above); CHECK-HUB: "PREFLIGHT runs no house gate and no probe".

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Mon Oct  5 15:13:09 EDT 2026
status · git status --short --branch · 0 · ## ops/launcher-fixround-1005
head · git log --oneline -1; git log --stat --format=%h c1746720..HEAD · 0 · (5 lines)
    36b98d61 docs(launcher-checks): build report — c1746720
    36b98d61
    
     .../reports/launcher-fixround-build-2026-10-05.md  | 187 +++++++++++++++++++++
     1 file changed, 187 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/launcher-fixround-1005/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/launcher-fixround-1005/docs/40 - DevDocs/reports/launcher-fixround-build-2026-10-05.md" · 0 · BUILT · job: launcher-checks · tip: c1746720 | on 5fb0ddf5 | migration: none | offline 3786/0 | with-DB 857/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0
range · git log --oneline 5fb0ddf5..c1746720 · 0 · (2 lines)
    c1746720 fix(launcher-checks): a deploy accepts a check tip below the code tip when the SHIPS row's fix report is committed and BUILT on the code tip; deploy-card.sh and CARD.md carry the fix report column (F1, R376, L75)
    7681e81f wip(launcher-checks): red — F1 fix-round tip launches; fix report column in deploy-card.sh and CARD.md
PREFLIGHT OK
```
THE RANGE, typed: `git log --stat --format=%h 5fb0ddf5..c1746720` · exit 0:
```
c1746720
 docs/40 - DevDocs/prompts/CARD.md |  4 ++--
 ops/desk/deploy-card.sh           |  6 +++---
 ops/desk/desk-launch.sh           | 22 +++++++++++++++++++++-
 3 files changed, 26 insertions(+), 6 deletions(-)
7681e81f
 tests/ops/test_desk_launch_prechecks.py | 113 ++++++++++++++++++++++++++++++--
 1 file changed, 109 insertions(+), 4 deletions(-)
```
Path union: `docs/40 - DevDocs/prompts/CARD.md`, `ops/desk/deploy-card.sh`, `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_prechecks.py`.
DB line: the card carries no `DB: none` line; that row is not run.
`ls <S>` · exit 1 · `ls: /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/launcher-checks-check: No such file or directory` → fresh.
House probes: not run — `house A: none (overruled 2026-10-02 R47)`. HOUSE B: as needed.

## Files copied
none — no outside house (overruled 2026-10-02 R47); `## 1` and `## 3` are not run.

## OWN FINDINGS
Written before any run (house A: none, overruled 2026-10-02 R47 — `## 2` is the read).

FINDING O1
ROW: F1 · X1 · X2
CLAIM: After F1 the launcher starts a deploy whose `## SHIPS` row carries a fix round (check `tip:` an ancestor of the code tip, `ops/desk/desk-launch.sh:767`), but the deploy worker's own STEP-0 P2 still demands the check's `tip:` equal the row's code tip — `ops/desk/deploy-step0.sh:378-383` (`why="its tip $t is not the row's code tip $ctip"`) and `DEPLOY-HUB.md:58` ("its `tip:` equals the row's code tip"; also "every literal the row's last column names", and the last column is now `fix report`) — so the launched worker is sure to fail its PREFLIGHT on the moved tip (X1).
RUN: TEST — `tests/ops/test_deploy_step0.py`:
```python
def test_o1_a_fix_round_row_the_launcher_accepts_passes_p2(desk):
    # the check ran on alpha's code tip; a small fix then moved the code tip past it (R376, L75)
    checked = desk.tip["alpha"]
    git(desk.repo, "checkout", "-q", "ops/alpha")
    (desk.repo / "src" / "alpha.py").write_text("alpha = 2\n")
    git(desk.repo, "add", "-A")
    git(desk.repo, "commit", "-q", "-m", "alpha small fix")
    fixed = git(desk.repo, "rev-parse", "--short=8", "HEAD")
    git(desk.repo, "checkout", "-q", "main")
    fix_report = desk.reports / "alpha-fix-build.md"
    fix_report.write_text(f"# alpha fix round\n\nBUILT · job: alpha · tip: {fixed} | rows: 1 of 1\n")
    desk.tip["alpha"], desk.head["alpha"] = fixed, fixed
    text = desk.card_text()
    text = text.replace("its stop line must carry |\n|---|---|---|---|---|---|\n",
                        "its stop line must carry | fix report |\n|---|---|---|---|---|---|---|\n")
    text = text.replace(f"`{fixed}` | `{desk.check['alpha']}` | `held unfixed: 0` and `ready: YES` |\n",
                        f"`{fixed}` | `{desk.check['alpha']}` | `held unfixed: 0` and `ready: YES` | `{fix_report}` |\n")
    desk.card.write_text(text)
    desk.check["alpha"].write_text(f"# check alpha\n\n{check_line(checked)}\n")
    desk.commit("fix round")
    done = desk.run()
    p2 = [ln for ln in done.stdout.splitlines() if ln.startswith("P2 check 1 ")]
    assert p2 and "is not the row's code tip" not in p2[0], done.stdout
```
EXPECT: on the tip the assertion fails: the `P2 check 1` row reads `… its tip <checked> is not the row's code tip <fixed>`.

FINDING O2
ROW: F1
CLAIM: The "unmodified" half of the fix report's committed-and-unmodified test (`ops/desk/desk-launch.sh:758-759`, `git diff --quiet` / `git diff --cached --quiet`) is pinned by no test: the five negative controls cover an uncommitted report only (`tests/ops/test_desk_launch_prechecks.py`, `(c) report uncommitted`), and the build's M4 removed the whole test at once.
RUN: TEST (to pass on the tip, and run red with those two lines removed) — `tests/ops/test_desk_launch_prechecks.py`:
```python
def test_f1_a_fix_report_edited_after_its_commit_still_refuses(desk):
    checked, fixed = fix_round(desk)
    report = desk.reports / "x-job-fix-build.md"
    report.write_text(report.read_text() + "an edit after the commit\n" + desk.built_line(fixed) + "\n")
    refused(desk, desk.launch("deploy", str(desk.deploy)), neither(checked, fixed))
    assert not desk.gate_left()
```
EXPECT: green on the tip; with `desk-launch.sh:758-759` cut to `[ -n "$(git … log …)" ] || return 1`, the F1 tests at the tip stay `0 failed` (the clause unpinned) and this test turns red (`assert 0 == 1`).

FINDING O3
ROW: F1
CLAIM: The card's clause "matches `"$REPORTS"/*.md`" (`ops/desk/desk-launch.sh:752-755`) is pinned by no test: every F1 test puts the fix report under `desk.reports`.
RUN: TEST (to pass on the tip, and run red with the `case` removed) — `tests/ops/test_desk_launch_prechecks.py`:
```python
def test_f1_a_fix_report_outside_the_reports_folder_still_refuses(desk):
    checked, fixed = fix_round(desk)
    stray = desk.prompts / "x-job-fix-build.md"
    stray.write_text((desk.reports / "x-job-fix-build.md").read_text())
    desk.write_deploy(code_tip=fixed, head=fixed, fix=str(stray))
    desk.commit("fix report outside reports")
    refused(desk, desk.launch("deploy", str(desk.deploy)), neither(checked, fixed))
    assert not desk.gate_left()
```
EXPECT: green on the tip; with `desk-launch.sh:752-755` removed the F1 tests stay `0 failed` and this test turns red (the deploy launches).

FINDING O4
ROW: F1 · X5
CLAIM: `docs/40 - DevDocs/prompts/CARD.md:47`, the sentence under the changed header, now reads false for a fix-round row: "The code tip is the `tip:` of the check's stop line … The last column is `held unfixed: 0` and `ready: YES`" — the last column is `fix report`, and a fix round's code tip is past the check's `tip:`.
RUN: COMMAND — `grep -n -F "The last column is" "docs/40 - DevDocs/prompts/CARD.md"`
EXPECT: `47:The code tip is the \`tip:\` of the check's stop line … The last column is \`held unfixed: 0\` and \`ready: YES\` …`

CHECK ASKS, answered by run under `## RUNS`: X1 → O1; X2 → `test_f1_a_card_of_todays_shape_passes_as_today` and O1; X3 → the negative controls' `gate_left()` asserts; X4 → `git diff --stat` of the three older files; X5 → the F1 header tests, the `CARD.md` diff, O4.

## Findings
none — house A: none (overruled 2026-10-02 R47).

## Dropped
none.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_deploy_step0.py::test_o1_a_fix_round_row_the_launcher_accepts_passes_p2` | `1 failed, 15 warnings in 1.72s` · `assert "is not the row's code tip" not in 'FAILED STEP...tip 05391efe'` — the script's last line `FAILED STEP-0: P2 check 1 — …/alpha-check.md — its tip e53ba006 is not the row's code tip 05391efe` | HELD, NOT FIXED — `ops/desk/deploy-step0.sh` (no row's file) and `DEPLOY-HUB.md:58` (fenced: "Any hub file") |
| O2 | own | `desk-launch.sh:758-759` cut (Edit, undone after), `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_desk_launch_prechecks.py -k f1` | `1 failed, 11 passed, 68 deselected` · the one red is the new `test_f1_a_fix_report_edited_after_its_commit_still_refuses` (`assert 0 == 1`, the deploy launched: `RUN: git … worktree add -b deploy/x-deploy …`); the build's ten F1 ids stay green | HELD (the clause is pinned by no build test) |
| O3 | own | `desk-launch.sh:752-755` (the `"$REPORTS"/*.md` case) cut (Edit, undone after), the same command | `1 failed, 11 passed, 68 deselected` · the one red is the new `test_f1_a_fix_report_outside_the_reports_folder_still_refuses` (`assert 0 == 1`, the deploy launched); the build's ten F1 ids stay green | HELD (the clause is pinned by no build test) |
| O4 | own | `grep -n -F "The last column is" "docs/40 - DevDocs/prompts/CARD.md"` | `47:The code tip is the \`tip:\` of the check's stop line (a fresh Opus pass may have moved it past the build's). The last column is \`held unfixed: 0\` and \`ready: YES\` for a check run on \`CHECK-HUB.md\`; a report of the old shape keeps its own literals.` | HELD, NOT FIXED — `CARD.md` beyond lines 44-45 (fenced) |
| X1 | ask | O1 | a fix-round deploy launches (`test_f1_a_fix_round_past_the_checked_tip_launches` green) and its STEP-0 P2 is sure to fail (O1) | answered by O1 |
| X2 | ask | `test_f1_a_card_of_todays_shape_passes_as_today[code tip|head]`, inside the run of `## FIXES` | green: six columns and the empty seventh cell both launch | no finding |
| X3 | ask | the negative controls' `assert not desk.gate_left()` (five build ids + O2, O3) | green on the tip: no gate worktree, no `deploy/x-deploy` branch after a refusal | no finding |
| X4 | ask | `git diff --stat 5fb0ddf5..c1746720 -- tests/ops/test_devdb_lock.py tests/ops/test_desk_launch_devfix.py tests/ops/test_desk_size_guard.py` | (empty) | no finding |
| X5 | ask | `git diff 5fb0ddf5..c1746720 --stat -- "docs/40 - DevDocs/prompts/CARD.md" ops/desk/deploy-card.sh` | `CARD.md \| 4 ++--` · `deploy-card.sh \| 6 +++---` · `2 files changed, 5 insertions(+), 5 deletions(-)`; the content diff (read at `## 2`) touches `CARD.md:44-45` and `deploy-card.sh:141,207,208` only | no finding beyond O4 |

Form repair, said: O1's test as first written read the reason from the `P2 check 1 ` row and ran GREEN (`1 passed`), because the script prints the reason on its last line, not on the row (the row's output, `-rP`: `P2 check 1 · … · 0 · CHECK DONE · … tip: c13fc11c …`; last line `FAILED STEP-0: P2 check 1 — … — its tip c13fc11c is not the row's code tip 32807a58`). Repaired once to read `last_line(done)` (the file's own helper); the asserted fact is unchanged. O1 is committed with `@pytest.mark.xfail(strict=True, …)` and its assertion unchanged, so the held defect stays visible and the mark fails the day P2 accepts a fix round.
`git diff --stat` after the O2/O3 mutations were undone → `tests/ops/test_deploy_step0.py | 24`, `tests/ops/test_desk_launch_prechecks.py | 18` only (no script change left).

## FIXES
| id | file | fix | proof | commit |
|---|---|---|---|---|
| O2, O3 | `tests/ops/test_desk_launch_prechecks.py` | two negative controls beside the build's five: a fix report edited after its commit, and one committed outside `$REPORTS`, each still refused with `neither the code tip`, no gate left | red under each mutation (`## RUNS`); `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_deploy_step0.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_deploy_card.py` → `144 passed, 1 xfailed, 15 warnings in 59.51s` (the xfail is O1) | `7e7803d5 fix(launcher-checks): F1 negative controls pin the fix report's unmodified and reports-folder clauses (check O2, O3)` |
| O1 | — | not fixed (outside the rows) | held test committed, strict xfail | `553f8c7b wip(launcher-checks): check red — O1 (…)` |

No DevDocs line: only tests changed, and no page exists for `ops/desk/desk-launch.sh` under `docs/40 - DevDocs/cobalt/` (build report `## E3`).

## Suites
RESTARTS first: `uv run cobalt jobs restarts 5fb0ddf5..HEAD` →
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CARD.md	M	DOCS	-
docs/40 - DevDocs/reports/launcher-fixround-build-2026-10-05.md	A	DOCS	-
ops/desk/deploy-card.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_deploy_step0.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_prechecks.py	M	test/documentation; no resident	-
RESTARTS: none
```
W on `7e7803d5`: `sh /Users/cobalt/cobalt/ops/desk/gate.sh launcher-fixround-1005 all` (no `--deselect`, `--tickers` or `--migration`: no with-DB test, ticker or migration added) · exit 0 · verdict lines whole:
```
offline 3786/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 857/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/launcher-fixround-1005-all-20261005-151858.log
```
`ls /Users/cobalt/cobalt-wt/launcher-fixround-1005/.env` → `No such file or directory`.
The rows' suite (the gate does not run it): `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `1 failed, 1359 passed, 2 xfailed, 15 warnings in 349.67s (0:05:49)`. The one red is the build's BASE red, `tests/ops/test_desk_launch_brain.py::test_the_trees_brain_hub_line_is_printed_with_its_handover_filled` (`AssertionError: assert '«INSTALL' in '# BRAIN-HUB — the standing brain seat (installed 2026-10-05 …`), the build's DECISIONS 1, outside this card. Against the build's tip run (`1357 passed, 1 xfailed`): +2 passed (O2, O3), +1 xfailed (O1).
New tests shown red first: O1 red on the tip (`## RUNS`); O2 and O3 red under their mutations (`## RUNS`).

## Scope
PREFLIGHT path union: `docs/40 - DevDocs/prompts/CARD.md` (row F1, lines 44-45), `ops/desk/deploy-card.sh` (F1), `ops/desk/desk-launch.sh` (F1), `tests/ops/test_desk_launch_prechecks.py` (F1). My commits: `tests/ops/test_desk_launch_prechecks.py` (F1's test file), `tests/ops/test_deploy_step0.py` (a test for held finding O1). No other path.

## Checked against the branch
(i) `git log --oneline c1746720..HEAD -- . ":(exclude)docs"` →
```
7e7803d5 fix(launcher-checks): F1 negative controls pin the fix report's unmodified and reports-folder clauses (check O2, O3)
553f8c7b wip(launcher-checks): check red — O1 (deploy-step0.sh P2 refuses the fix-round tip the launcher accepts; strict xfail, held, not fixed: outside card 21's rows)
```
`<tip now>` = `7e7803d5`.
(ii) `git log --stat --format=%h c1746720..HEAD` → `7e7803d5 tests/ops/test_desk_launch_prechecks.py | 18` · `553f8c7b tests/ops/test_deploy_step0.py | 26` · `36b98d61 …/reports/launcher-fixround-build-2026-10-05.md | 187` — test files and a docs report only; no WIDENED.
(iii) `git log --oneline 5fb0ddf5..HEAD -- <the four hubs> ops/desk/desk-watch.sh .claude/settings.json tests/ops/test_devdb_lock.py tests/ops/test_desk_launch_devfix.py tests/ops/test_desk_size_guard.py` → empty.
(iv) `grep -n -F "def test_o1_a_fix_round_row_the_launcher_accepts_passes_p2" tests/ops/test_deploy_step0.py` → `548:…`; `grep -n -F "def test_f1_a_fix_report_" tests/ops/test_desk_launch_prechecks.py` → `608:def test_f1_a_fix_report_edited_after_its_commit_still_refuses(desk):` · `616:def test_f1_a_fix_report_outside_the_reports_folder_still_refuses(desk):`. O1's `wip` commit `553f8c7b` sits below `7e7803d5`; O2 and O3 have no separate `wip` red commit: their tests are green on the tip by design (they pin a clause the code already holds) and were shown red under the mutation (`## RUNS`).
(v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/launcher-fixround-1005`.
(vi) `git log --stat --format=%h 5fb0ddf5..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no gate-list change owed.
(vii) The card's `## RECORDS` name no `ls`, `grep` or `git -C … log` command to run.
(viii) L32: this report holds constructed values and commit ids only.

## OPEN
| id | verdict | what would settle it |
|---|---|---|
| O1 | HELD, NOT FIXED — `ops/desk/deploy-step0.sh:378-383` and `DEPLOY-HUB.md:58` | a card row that teaches STEP-0 P2 (script and hub text) the fix-round acceptance F1 gave the launcher; `tests/ops/test_deploy_step0.py::test_o1_a_fix_round_row_the_launcher_accepts_passes_p2` then passes and its strict xfail mark must be removed |
| O4 | HELD, NOT FIXED — `CARD.md:47` (fenced) | a row that rewrites `CARD.md:47` for the seventh column and the fix-round code tip |

## CONTINUE
next: done (stop line)

## DECISIONS
1. **O1 — HELD, NOT FIXED (blocks the deploy F1 exists for).** The launcher now launches a fix-round deploy (`desk-launch.sh:767`), but the deploy's own STEP-0 refuses it: `deploy-step0.sh` P2 → `FAILED STEP-0: P2 check 1 — …/alpha-check.md — its tip e53ba006 is not the row's code tip 05391efe` (`## RUNS` O1), and `DEPLOY-HUB.md:58` says the same in text ("its `tip:` equals the row's code tip"; and it reads literals from "the row's last column", which is now `fix report`). So the 03d deploy (R405) still fails, one step later, inside a launched worker (CHECK ASK X1). The fix lies in `ops/desk/deploy-step0.sh` (no row of card 21) and `DEPLOY-HUB.md` (fenced). Safe default taken: not fixed; the test is committed with a strict xfail. Needs: a card row for both (the R419 hub-text prompt may cover the hub text; the script is separate).
2. **O4 — HELD, NOT FIXED.** `CARD.md:47` still says "The last column is `held unfixed: 0` and `ready: YES`" and that the code tip is the check's `tip:`; both are false for a row with a fix round. Fenced (CARD.md beyond lines 44-45). Safe default: not touched; same follow-up card as 1.
House B: `none available` (house A none, overruled 2026-10-02 R47); the two open items are listed here instead.

## RECORDS
- Dropped findings: none (no house).
- House: none produced nothing — house A none by his overrule 2026-10-02 R47; no probe run.
- `REFUSED, not needed`: none. `CONTINUED`: none. Extra lock takes: none (the gate's one take).
- L74: none in a tool result. The session's own attribution reminder asked for a `Claude-Session:` line on commits; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.
- The O1 test is a held finding's test in `tests/ops/test_deploy_step0.py`, a file outside F1's `files` (allowed: "tests for held findings"). I committed it with `xfail(strict=True)` and did not leave it plain red, so `tests/ops` gets no new red for a defect this card cannot fix. The assertion is unchanged.
- Reads beyond the list, for X1: `ops/desk/deploy-step0.sh` (lines 1-100, 300-402) and `tests/ops/test_deploy_step0.py` (its fixture and lines 78-262).
- `<S>/opus-1.md` is written, but shortened: the O1 test is named, not pasted, and the RUNS rows are condensed. The full sections are in this report, which a pass 2 reads anyway.
- files opened: 15 — `CHECK-HUB.md`, the card, `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_prechecks.py`, `ops/desk/deploy-card.sh` (diff), `docs/40 - DevDocs/prompts/CARD.md` (diff, grep), the build report, `BUILD-HUB.md` (THE LOCK, E2, RESTARTS, W), `areas/cobalt.md` (the two sections), `DEPLOY-HUB.md` (P2, P3), `ops/desk/deploy-step0.sh`, `tests/ops/test_deploy_step0.py`, the gate output, the `tests/ops` output, this report.
- Check of `launcher-checks`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: launcher-checks · pass: 1 · tip: 7e7803d5 · house A: none (overruled 2026-10-02 R47) · findings: 4 · dropped: 0 · held: 4 · fixed: 2 · held unfixed: 2 · open: 2 · house B: none available · suites: offline 3786/0 · with-DB 857/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 15 · ready: NO · decisions: 2 · for Dejan: 0
