# plist-step-c-1013 — check report (2026-10-13)

## §0 Headline
Check of card 496 at `01fb7297`. House A was Grok (`FINDINGS: 7`). There was no house B: Gemini was OUT on a harness error, and the card says `HOUSE B: as needed`. Together with my 3 findings that makes 10, and none was dropped.
6 held and all 6 are fixed (`6c3402af`, tests `402aaa1c`). STEP-C now refuses a plist that arrives by rename. It matches the files cell whole, and it clears an owed entry when an `add` or `change` admission loads that label. A refusal at 4.6L goes to STEP-5. The DF1 and BO1 tests are stronger.
4 were rejected by a card or hub line and stay open (O2, A4, A6, A7). The deploy gate is green: offline 4327/0, with-DB 5230/0, live-note 146/0, `cobalt_dev` 0013 with F2 = F0, `.env` removed. RESTARTS: `com.cobalt.radar`.

## L74
- One system notice in this session asked for a `Claude-Session:` line in commits. Recorded here once, not followed: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/496-plist-step-c-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/496-plist-step-c-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-13/496-plist-step-c-card.md" · 0 · a71e8a972a72a87ea55ad7c6974feed0b40fe7f7
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-13/496-plist-step-c-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-13 R1341 row · grep -n "^| R1341 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-13.md" · 0 · 71:| R1341 | 07:25 ET | HIS RULING · APPROVED: "Confirmed: R1323, R1324, R1330, R1340." Words: `cto-2026-10-13-words.md` R1341. Confirms the relays R1323, R1324, R1330, R1340. | APPLIED: LAWS, checklist, areas/cobalt.md at 07:27 |
RULING 2026-10-13 R1341 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1341 |" -- "docs/40 - DevDocs/reports/cto-2026-10-13.md" · 0 · b399c9516e518b4d5a2b60b47382c9840c4130e6
RULING 2026-10-13 R1341 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-13.md" · 0 · the row as grepped
AUTHORIZED
```
House gates (11:02 ET): `grep -n "^| R17 "` → one row (`:35`); `grep -n "^| R19 "` → one row (`:37`); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c`.

## PREFLIGHT
rule · command · exit · output
- MECHANICAL · `sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · 0 · whole:
```
clock · date · 0 · Tue Oct 13 11:02:51 EDT 2026
status · git status --short --branch · 0 · ## ops/plist-step-c-1013
head · git log --oneline -1; git log --stat --format=%h 01fb7297..HEAD · 0 · (9 lines)
    dfc2624f docs(plist-step-c-1013): build report — 01fb7297
    dfc2624f
    
     .../reports/plist-step-c-build-2026-10-13.md       | 61 ++++++++++++++++++----
     1 file changed, 52 insertions(+), 9 deletions(-)
    2b39ef9d
    
     .../reports/plist-step-c-build-2026-10-13.md       | 217 +++++++++++++++++++++
     1 file changed, 217 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/plist-step-c-1013/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/plist-step-c-1013/docs/40 - DevDocs/reports/plist-step-c-build-2026-10-13.md" · 0 · BUILT · job: plist-step-c-1013 · tip: 01fb7297 | on 5214e50b | migration: none | offline 4327/0 | with-DB 5230/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 9 of 10 | self-check: 2 of 3 | decisions: 8 · for Dejan: 1 · tokens: 382312
report: self-check 2 of 3 (recorded)
range · git log --oneline 5214e50b..01fb7297 · 0 · (2 lines)
    01fb7297 feat(plist-step-c-1013): STEP-C as one script admits card-named launchd one-shots; deferred bootstrap owed and read as OWED (C1 C2 B1 R1 L1 D1 DF1 BO1 OW1, L1 L3 L42)
    b4793b17 wip(plist-step-c-1013): red
PREFLIGHT OK
```
- Self-check 2 of 3 recorded; it goes to the house as a fact.
- THE RANGE · `git log --stat --format=%h 5214e50b..01fb7297` · 0 · `01fb7297`: `configs/cobalt/smoke/s2.yaml`, `docs/40 - DevDocs/cobalt/jobs/watchdog.md`, `docs/40 - DevDocs/cobalt/smoke/checks.md`, `docs/40 - DevDocs/prompts/CARD.md`, `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `ops/desk/deploy-step-c.sh` (316 +), `ops/desk/desk-launch.sh` (88 +), `src/cobalt/jobs/watchdog.py`, `src/cobalt/smoke/checks.py`, `tests/ops/test_deploy_step_c.py` — 10 files, 509 insertions, 20 deletions; `b4793b17`: `tests/cobalt/test_jobs.py`, `tests/cobalt/test_smoke.py`, `tests/ops/test_deploy_step_c.py`, `tests/ops/test_desk_launch_launchd.py` — 4 files, 767 insertions. Path union: these 14 paths.
- DB: none · the card carries no `DB:` key (removed at `2ff41ff1`, build report RECORDS) · the (a0) rule does not apply.
- `ls <S>` · 1 · `No such file or directory` (fresh).
- THE HOUSE PROBES · `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · 0 · whole:
```
grok: UP
gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings
```
- SEATS: house A: Grok · house B: none (not needed — card `HOUSE B: as needed`). Gemini OUT (HARNESS, line above).

## Files copied
`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/plist-step-c-1013-check`.
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → whole:
```
65835 <S>/diff.md
26312 <S>/files/496-plist-step-c-card.md
35891 <S>/files/plist-step-c-build-2026-10-13.md
27803 <S>/files/wt/configs/cobalt/smoke/s2.yaml
3402 <S>/files/wt/docs/40 - DevDocs/cobalt/jobs/watchdog.md
11012 <S>/files/wt/docs/40 - DevDocs/cobalt/smoke/checks.md
17888 <S>/files/wt/docs/40 - DevDocs/prompts/CARD.md
65007 <S>/files/wt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md
14938 <S>/files/wt/ops/desk/deploy-step-c.sh
127627 <S>/files/wt/ops/desk/desk-launch.sh
23604 <S>/files/wt/src/cobalt/jobs/watchdog.py
32603 <S>/files/wt/src/cobalt/smoke/checks.py
40633 <S>/files/wt/tests/cobalt/test_jobs.py
77859 <S>/files/wt/tests/cobalt/test_smoke.py
17408 <S>/files/wt/tests/ops/test_deploy_step_c.py
9115 <S>/files/wt/tests/ops/test_desk_launch_launchd.py
320 <S>/rulings.md
STAGED 17 files · 597257 bytes · commits 2
```
(`<S>` abbreviates the absolute path the script printed.) `commits 2` = PREFLIGHT's range count.
`stage-copy.sh`, one call each:
- `COPIED 34139 <S>/files/304-f4-refresh-card.md`
- `COPIED 14583 <S>/files/deploy-f4-refresh-1010.md`
- `COPIED 16230 <S>/files/survey-blockers-2026-10-12.md`
- `COPIED 45695 <S>/files/wt/docs/40 - DevDocs/prompts/STANDING-LIST.md`
- `COPIED 12098 <S>/files/wt/src/cobalt/jobs/restarts.py`
- `COPIED 13550 <S>/files/wt/tests/ops/test_hub_lines.py`
- `COPIED 45801 <S>/files/wt/tests/ops/test_deploy_step0.py`
- `COPIED 4024 <S>/files/wt/src/cobalt/smoke/cli.py`
- `COPIED 16833 <S>/files/wt/src/cobalt/smoke/models.py`
`<S>/HOUSE-INSTRUCTIONS.md` written (28839 bytes): the HOUSE TEXT verbatim, the self-check fact, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, the Files paragraph.
House A Grok started 11:05 ET (`date` 11:05:18; gates re-run: R17 `:35`, R19 `:37`, commit `5055151d…`), background task `btx3svnee`; `cd` back, `git status --short --branch` → `## ops/plist-step-c-1013`. No house B (not needed).

## OWN FINDINGS
Written 11:07 ET, before any house list was opened (`date` 11:07:50).

FINDING O1
ROW: C1 · X2
CLAIM: `ops/desk/deploy-step-c.sh:206` runs `git diff --name-status` without `--no-renames`, so a plist that arrives by rename (status `R<n>`, old path in column 2) is read by its OLD path at `:214-219`, and when that old path is not a `.plist` the loop `continue`s: an unnamed `ops/com.cobalt.<label>.plist` passes STEP-C with exit 0.
RUN: TEST — `tests/ops/test_deploy_step_c.py`
```python
def test_check_o1_a_plist_that_arrives_by_rename_is_refused_unnamed(repo):
    repo.write("ops/notes.txt", plist(LABEL))
    repo.commit("gate: a note")
    git(repo.repo, "checkout", "-q", "main")
    git(repo.repo, "merge", "-q", "--ff-only", repo.branch)
    repo.m0 = git(repo.repo, "rev-parse", "--short=8", "HEAD")
    git(repo.repo, "checkout", "-q", repo.branch)
    git(repo.repo, "mv", "ops/notes.txt", PLIST_PATH)
    repo.commit("gate: the note becomes a plist")
    done = repo.run("")
    assert done.returncode == 1, done.stdout + done.stderr
    assert last(done) == f"FAILED: C — {PLIST_PATH}: {FAILED_TAIL}"
```
EXPECT: `assert 0 == 1` (stdout `STEP-C: ADMITTED 0`).

FINDING O2
ROW: L1 · X1
CLAIM: `ops/desk/desk-launch.sh` `launchd_line` (`:1565-1576` at the tip) admits any 1–4 words of `[a-z0-9 -]` after `uv run`, so a card line `dry run: COBALT_ENV=production uv run pkill -f cobalt --dry-run` puts `"Bash(COBALT_ENV=production uv run pkill -f cobalt --dry-run)"` on the deploy line: a production string that is not a Cobalt dry run.
RUN: TEST — `tests/ops/test_desk_launch_launchd.py`
```python
def test_check_o2_a_dry_run_that_is_no_cobalt_command_is_refused(tmp_path):
    desk = Desk(tmp_path)
    desk.set_card(section(card_line(dry="COBALT_ENV=production uv run pkill -f cobalt --dry-run")))
    done = desk.launch()
    assert done.returncode != 0, done.stdout
    assert "REFUSED" in done.stderr, done.stderr
```
EXPECT: `assert 0 != 0` (the dry launch exits 0).

FINDING O3
ROW: DF1 · OW1
CLAIM: an owed entry outlives the deploy that loads the label: `ops/desk/deploy-step-c.sh:308-314` touches the owed file only when this run has a `deferred` line, so a step C that admits the same label `add` (a recut of a deferred deploy that failed before 4.6L, then deployed `add`) leaves the entry, and from then on an unloaded label reads `OWED`, not red, in K18 and the sweep (`src/cobalt/jobs/watchdog.py` OW1 branch).
RUN: TEST — `tests/ops/test_deploy_step_c.py`
```python
def test_check_o3_an_add_admission_leaves_no_owed_entry_for_its_label(repo):
    repo.add_plist()
    assert repo.run(launchd(line(mode="deferred", gate=GATE))).returncode == 0
    assert LABEL in json.loads(repo.owed.read_text())
    done = repo.run(launchd(line()))
    assert done.returncode == 0, done.stdout + done.stderr
    assert LABEL not in json.loads(repo.owed.read_text())
```
EXPECT: `AssertionError: assert 'com.cobalt.prefill-refresh' not in {...}`.

FINDINGS: 3

## Findings
House A Grok finished 11:22 ET (`date` 11:22:09); `ls -la <S>` → `house-a.md` 5719 bytes, last line `FINDINGS: 7`. Every block has a `RUN:` followed by a `def test_` or one command with an allowed beginning: none dropped. House ids are `A<n>`.
id · house · row · claim · form
- O1 · Opus · C1/X2 · `deploy-step-c.sh:206` diff without `--no-renames`: a plist arriving by rename is read by its old path and skipped · TEST
- O2 · Opus · L1/X1 · a dry run `uv run <any binary> …` (e.g. `pkill -f cobalt`) passes the shape and reaches the deploy line · TEST
- O3 · Opus · DF1/OW1 · an owed entry survives a later `add` admission of its label, so a later unload reads OWED, not red · TEST
- A1 · Grok · C1 · files-cell check `*"$path"*` (`:277`) admits a cell that only contains the path as a substring · TEST
- A2 · Grok · DF1 · (o) asserts only `startswith(ADMITTED: … · add)`; dropping `· deferred` stays green · COMMAND
- A3 · Grok · BO1 · (t) never reads the hub's `4.6L-BO`; it bootstraps by itself, so deleting the hub step stays green · COMMAND
- A4 · Grok · OW1 · the sweep catches `BootstrapOwedError` (`watchdog.py:439`) instead of raising; no test calls the path · TEST
- A5 · Grok · X3 · `DEPLOY-HUB.md:41` ends a refused listed call after 4.6 on `FAILED:` without STEP-5, while 4.6L (`:144`) boots out a `change` label: it would be left out · COMMAND
- A6 · Grok · D1 · `STANDING-LIST.md:157` still says installing a launchd job is not on the list · COMMAND
- A7 · Grok · SCOPE · `docs/…/cobalt/jobs/watchdog.md` and `smoke/checks.md` changed, outside every row's files · COMMAND

## Dropped
none.

## RUNS
id · source · run · output · verdict
- O1 · Opus · `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_deploy_step_c.py::test_check_o1_a_plist_that_arrives_by_rename_is_refused_unnamed` (with the four below, one call, 11:23) → `AssertionError: STEP-C: ADMITTED 0 … assert 0 == 1` (`returncode=0, stdout='STEP-C: ADMITTED 0\n'`) · HELD
- O3 · Opus · `…::test_check_o3_an_add_admission_leaves_no_owed_entry_for_its_label` → `assert 'com.cobalt.prefill-refresh' not in {'com.cobalt.prefill-refresh': {… 'gate': ['X7 render', 'X8', 'X9', 'X10 dry run', 'X15']}}` · HELD
- A1 · Grok · `…::test_c1_a_files_cell_that_only_contains_the_path_is_refused` → `AssertionError: ADMITTED: com.cobalt.prefill-refresh · add / STEP-C: ADMITTED 1 … assert 0 == 1` · HELD
- O2 · Opus · `tests/ops/test_desk_launch_launchd.py::test_check_o2_a_dry_run_that_is_no_cobalt_command_is_refused` → `assert 0 != 0`; the dry line holds `"Bash(COBALT_ENV=production uv run pkill -f cobalt --dry-run)"` · REJECTED — card row L1: "a dry run not exactly `COBALT_ENV=production uv run <1–4 words of [a-z0-9-]> --dry-run` or `none`" is the refusal the card sets; `pkill -f cobalt` is three such words. The test was removed with Edit. OPEN
- A4 · Grok · `tests/cobalt/test_jobs.py::test_ow1_not_json_is_refused_loud` → `Failed: DID NOT RAISE <class 'cobalt.jobs.watchdog.BootstrapOwedError'>` · REJECTED — card row OW1: "any other enabled, unloaded label stays red"; the sweep keeps the label red (`ok` false, `not loaded`) with the file named in its detail, and K18 turns the same error into ERROR (`checks.py:733`). The test was removed with Edit. OPEN
- A2 · Grok · `grep -n -F -e "· add · deferred" -e "ADMITTED: %s · %s" -e "ADMITTED: {LABEL} · add" ops/desk/deploy-step-c.sh tests/ops/test_deploy_step_c.py` → `ops/desk/deploy-step-c.sh:283: printf 'ADMITTED: %s · add · deferred\n'`, `:290: printf 'ADMITTED: %s · %s\n' … add … change`, `tests/ops/test_deploy_step_c.py:317: assert any(ln.startswith(f"ADMITTED: {LABEL} · add") …)`. Then run by mutation: `:283` → `printf 'ADMITTED: %s · add\n'` with Edit; `-k "df1_ or bo1_ or check_a2 or check_a3 or check_a5"` → `3 failed, 6 passed`: every df1/bo1 test PASSED, the new `test_check_a2_a_deferred_admission_is_marked_deferred` failed `assert 'ADMITTED: com.cobalt.prefill-refresh · add · deferred' in ['ADMITTED: com.cobalt.prefill-refresh · add', …]`; undone with Edit · HELD (an assertion too weak)
- A3 · Grok · `grep -n -F -e "4.6L-BO" -e "launchctl\", \"bootstrap\"" tests/ops/test_deploy_step_c.py` → only `389:    subprocess.run(["launchctl", "bootstrap", "gui/501", …`. Same mutation run, hub `4.6L-BO` → `4.6L-XX`: the bo1 tests PASSED; the new `test_check_a3_the_hub_names_the_bootstrap_only_step` failed `ValueError: not enough values to unpack (expected 1, got 0)`; undone · HELD
- A5 · Grok · `grep -n -F -e "after 4.6)" -e "A failure → STEP-5" -e "(2L) After (2)" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` → `41:` (OUTSIDE THE OUTAGE (before 4.1, after 4.6) … A LISTED command a step names that is refused = THE RUN FAILED … then the `FAILED:` line. INSIDE THE OUTAGE (4.1 to the end of 4.6) the strict rule stays: ANY refused call → STEP-5 first), `144:` (4.6L … outside the outage … A failure → STEP-5), `165:` (2L). The new pin `test_check_a5_a_refusal_at_4_6l_goes_to_step_5` red on the tip: `assert '4.6L' in "- A DEPLOY NEVER CONTINUES BY MESSAGE …"` · HELD
- A6 · Grok · `grep -n -F "NOT ON THIS LIST, by design: retiring or installing a launchd job" "docs/40 - DevDocs/prompts/STANDING-LIST.md"` → `157:` holds it · REJECTED — card row D1: "Edited only after the desk's answer to report `## DECISIONS` item 1" (build report DECISIONS 1, no answer in the build). OPEN
- A7 · Grok · `git diff --stat 5214e50b 01fb7297 -- "docs/40 - DevDocs/cobalt/jobs/watchdog.md" "docs/40 - DevDocs/cobalt/smoke/checks.md"` → `watchdog.md | 3 +++`, `checks.md | 3 +++`, `2 files changed, 6 insertions(+)` · REJECTED — `BUILD-HUB.md` `## E3`: "Each changed module gets ONE dated line in its page under `docs/40 - DevDocs/cobalt/`" (the build is required to write them). OPEN
- Held tests committed before any fix: `402aaa1c wip(plist-step-c-1013): check red — O1 O3 A1 A2 A3 A5` (`tests/ops/test_deploy_step_c.py`, 60 +). `git diff --stat` after the removals and the undo → only `tests/ops/test_deploy_step_c.py`.

## FIXES
- O1: `ops/desk/deploy-step-c.sh` STEP-C diff gains `--no-renames` (a renamed-in plist is an `A`, its old path a `D`). Commit `6c3402af`.
- O3: `ops/desk/deploy-step-c.sh`: an `add` or `change` admission drops that label's existing owed entry on exit 0 (no file is written when nothing changes). Commit `6c3402af`.
- A1: `ops/desk/deploy-step-c.sh`: the files cell is matched as whole backticked, comma-separated entries (`case " $(… | tr '`,' '  ') " in *" $path "*`). Commit `6c3402af`.
- A5: `DEPLOY-HUB.md:41`: "So does 4.6L from its first `bootout` or `bootstrap` …: → STEP-5 first, whose (1L) and (2L) leave each label `out` or `restored`." Commit `6c3402af`.
- A2, A3: the fix is the stronger test itself (`402aaa1c`), green on the tip, red under the mutation above.
- After the fix: `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_deploy_step_c.py tests/ops/test_desk_launch_launchd.py tests/ops/test_hub_lines.py tests/ops/test_deploy_step0.py` → `151 passed, 15 warnings in 75.01s`.
- DevDocs line: no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/deploy-step-c.sh` (`Grep "deploy-step-c|deploy-step0"` there → no files); none written (the build wrote none for it either).

## Suites
- RESTARTS: `uv run cobalt jobs restarts 5214e50b..HEAD` → exit 0, 14 rows. The same classes as the build's table, no `UNCLASSIFIED`, last line `RESTARTS: com.cobalt.radar`.
- `ls -la /Users/cobalt/cobalt-wt/plist-step-c-1013/.env` → No such file (before the gate).
- THE GATE at `6c3402af`: `sh /Users/cobalt/cobalt/ops/desk/gate.sh plist-step-c-1013 all --deploy` (no `--deselect`, no `--tickers`, no `--migration`) → exit 0. Verdict lines, whole:
```
offline 4327/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5230/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/plist-step-c-1013-all-20261013-112609.log
```
  Log: `:956` `pass 1: whole (deploy)`; `:1117` `dev forward: APPLIED 11:51:24`. Every SKIPPED line is in the build report's allowed set, and none is marked `OUTSIDE the allowed set`.
- After the gate: `ls /Users/cobalt/cobalt-wt/plist-step-c-1013/.env` → No such file.
- `tests/ops` (the gate's offline pass does not run it): `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops` → `1 failed, 3590 passed, 1 xfailed, 16 warnings in 773.86s`. The one red is `tests/ops/test_the_rule_sweep.py:134: AssertionError: ['f4-refresh-build-2026-10-10.md']`, the same red outside the rows that the build named (its DECISIONS 6); this check changed none of its inputs. 3590 = the build's 3584 + this check's 6 new tests.

## Scope
PREFLIGHT's path union (14 paths) plus my commits: `tests/ops/test_deploy_step_c.py` (a test file), `ops/desk/deploy-step-c.sh` (rows C1/DF1/BO1), and `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (rows C2/B1/R1/L1/DF1/BO1; my edit is `:41`, not the fenced `:32` and `:58`). Nothing outside the rows' files.
CHECK ASK (L67 house read): house A Grok read `DEPLOY-HUB.md` whole as changed, and its findings A3 and A5 cite `:89`, `:41`, `:144` and `:165`. It also read `STANDING-LIST.md` as it stands (A6 cites `:157`). `STANDING-LIST.md` is not changed by this build.

## Checked against the branch
- (i) `git log --oneline 01fb7297..HEAD -- . ":(exclude)docs"` → `6c3402af fix(plist-step-c-1013): STEP-C reads renames as adds, …` and `402aaa1c wip(plist-step-c-1013): check red — O1 O3 A1 A2 A3 A5`. `<tip now>` = `6c3402af`.
- (ii) `git log --stat --format=%h 01fb7297..HEAD` → `6c3402af`: `DEPLOY-HUB.md`, `ops/desk/deploy-step-c.sh`; `402aaa1c`: `tests/ops/test_deploy_step_c.py`; `dfc2624f`, `2b39ef9d`: the build report. Every non-docs path is in a row's files or is a test file.
- (iii) `git log --oneline 5214e50b..HEAD -- ops/desk/deploy-outage.sh ops/desk/deploy-step0.sh ops/desk/deploy-card.sh ops/desk/authorize.sh ops/desk/bare-guard.py src/cobalt/jobs/restarts.py .claude/settings.json` → empty. The same for card 304 and `ops/com.cobalt.prefill-refresh.plist` → empty. `git diff 5214e50b HEAD -U0 -- DEPLOY-HUB.md` hunks are at `:3`, `:5`, `:11`, `:13`, `:41`, `:79`, `:89`, `:125`, `:144-145`, `:156`, `:163`, `:165`, `:170`, `:174`, `:180`; none touches `:32` or `:58`.
- (iv) `grep -n -F "def <name>" tests/ops/test_deploy_step_c.py` → `:406` O1, `:420` O3, `:429` A1, `:444` A2, `:451` A3, `:457` A5. Each test is one line. `402aaa1c` (wip) sits below `6c3402af` (fix) in (i).
- (v) `ls <WT>/.env` → No such file; `git status --short --branch` → `## ops/plist-step-c-1013`.
- (vi) `git log --stat --format=%h 5214e50b..HEAD -- src/cobalt/db_migrations tests/cobalt` → only `b4793b17`, with `tests/cobalt/test_jobs.py` and `tests/cobalt/test_smoke.py` (offline tests). There is no migration and no with-DB test above `0013`, so no gate lists are needed.
- (vii) Card RECORDS checked: `grep -n -F "| R411 "` → `107:`, and `grep -n -F "| R412 "` → `109:`, both in `cto-2026-10-05.md` (as the record says). `ls /Users/cobalt/cobalt/data` → `archiver-shadow backups memory.json postgres radar-cache radar-pool-block.yaml restarts-s2-p1-stage1.err restarts-s2-p1-stage1.txt` (`backups` present, no `deploy`). `grep -rn -F "BOOTSTRAP OWED" /Users/cobalt/cobalt/ops` → empty on main.
- (viii) L32: this report holds only constructed values and the repo's own labels and paths.

## OPEN
- O2 · REJECTED — row L1's dry-run shape (`uv run <1–4 words of [a-z0-9-]> --dry-run`) admits any binary, e.g. `pkill -f cobalt`. Settled by: a desk ruling that the shape names `cobalt` (or a fixed command list) as its first word, then a fix-round test (the O2 test above).
- A4 · REJECTED — the sweep keeps an unreadable owed file red with a note instead of raising. Settled by: a desk ruling on whether L1 "refuse loud" means raising in the heartbeat's sweep. The current behaviour matches OW1's "stays red".
- A6 · REJECTED — `STANDING-LIST.md:157` is not edited, which row D1 makes wait for the desk's answer to build DECISIONS 1. Settled by: that answer, then the one-line edit.
- A7 · REJECTED — the DevDocs lines are BUILD-HUB E3's required entries. Settled by: nothing. It is listed only because it is a rejected item.

## CONTINUE
next: none (CHECK DONE).

## DECISIONS
1. FOR DEJAN — A6: `STANDING-LIST.md:157` still reads `NOT ON THIS LIST, by design: retiring or installing a launchd job`, while `desk-launch.sh` now generates `bootout` and `bootstrap` strings for card-named labels. Row D1 waits for the desk's answer to build DECISIONS 1, and the file is his one approval (R60). Safe default: not edited.
2. O2 (open, X1): a `## LAUNCHD` dry run may name any binary that `uv run` resolves. The card's shape allows it, so the shape needs a ruling, e.g. a first word of `cobalt`, `prefill` or a named list. Safe default: the card's shape stands; the desk reads each `dry run:` by eye at the deploy card.
3. A4 (open): an unreadable `bootstrap-owed.json` keeps the sweep red (`not loaded` with the file's error in the detail), and K18 reports ERROR. It does not raise in the sweep. Safe default: as built.
4. A7 (open): the DevDocs lines are required by BUILD-HUB E3. No action.
5. UNPROVEN (L70), outside the rows, not fixed: `tests/ops/test_the_rule_sweep.py::test_every_exempt_entry_still_mismatches` fails with `AssertionError: ['f4-refresh-build-2026-10-10.md']` (`:134`), as in build DECISIONS 6. Its inputs are unchanged by this check.

## RECORDS
- Dropped findings: none.
- House B: Gemini OUT at the probe (`error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings`). It was not needed (`HOUSE B: as needed`) and was not launched.
- Tests removed after a REJECTED verdict: O2 (`tests/ops/test_desk_launch_launchd.py`) and A4 (`tests/cobalt/test_jobs.py`); their text is quoted under `## OWN FINDINGS` and in `<S>/house-a.md`. `git diff --stat` afterwards showed only `tests/ops/test_deploy_step_c.py`.
- Run by mutation (A2, A3): `ops/desk/deploy-step-c.sh:283` and the hub's `4.6L-BO` were changed with Edit for one run and undone with Edit. `git diff --stat` afterwards showed only the test file.
- One lock take, by `gate.sh` (`lock: waited 0 min`; `.env: removed`). No lock was taken by hand.
- Not read: `areas/cobalt.md` (WHAT YOU READ (5)). The card, its rows and the fence carried the job, and no finding rests on it.
- `tests/ops` ran while the gate ran (offline only; no DB, no `.env`).
- files opened: 13 — CHECK-HUB.md; the card; the build report; BUILD-HUB.md (`## THE LOCK`, `## E2`–`## W`); `ops/desk/deploy-step-c.sh`; `tests/ops/test_deploy_step_c.py`; `tests/ops/test_desk_launch_launchd.py`; `tests/cobalt/test_jobs.py` (`:940-1013`); the saved diff of DEPLOY-HUB/CARD/s2.yaml; `<S>/house-a.md`; and three task outputs (house probe, Grok, gate). Diffs of `desk-launch.sh` and `src/` were read as tool output.
- Context at close: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh f35779d1-3636-4800-8aff-7263982c647b` → `context 255726 of 400000 — ok`.
- Check of `plist-step-c-1013`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: plist-step-c-1013 · pass: 1 · tip: 6c3402af · house A: Grok FINDINGS: 7 · findings: 10 · dropped: 0 · held: 6 · fixed: 6 · held unfixed: 0 · open: 4 · house B: none available · suites: offline 4327/0 · with-DB 5230/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 13 · ready: YES · decisions: 5 · for Dejan: 1 · tokens: 255726
