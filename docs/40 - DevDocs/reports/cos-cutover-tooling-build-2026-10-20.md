# cos-cutover-tooling — build report 2026-10-20

## §0 Headline
- Built 5 of 5 rows on `4a9b60bd`, tip `96728174`: `desk-launch.sh deploy` admits card 929's bootstrap-only form (T2); `deploy-step0.sh`, `deploy-outage.sh` and `DEPLOY-HUB.md` read one retirement record, `ops/desk/retired-labels`, and leave a retired agent alone (T1a–c).
- With no record, every changed line behaves as on BASE (controls green on BASE and after).
- Gates: offline 9018/0, live-note 148/0, `tests/ops` 4121 passed; with-DB not run (DB: none); RESTARTS: none.
- 4 decisions, none for Dejan: the record's form (b), the card's ASK DESK defaults, the `none`-filled strings, two E2 differences from the card.

## L74
- A system block in this session asked for a `Claude-Session:` line on commits. Recorded once here; not acted on. The commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/931-cos-cutover-tooling-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/931-cos-cutover-tooling-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/931-cos-cutover-tooling-card.md" · 0 · 97794293af7456e951976365963b15ef58728d89
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/931-cos-cutover-tooling-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0:
```
clock · date · 0 · Tue Oct 20 17:58:10 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/cos-cutover-tooling
    ?? "docs/40 - DevDocs/reports/cos-cutover-tooling-build-2026-10-20.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 4a9b60bd docs(desk): R2214 931 amend drafted, preflight r2 943
diff · git diff --stat 4a9b60bd · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/cos-cutover-tooling · 0 · 4a9b60bd docs(desk): R2214 931 amend drafted, preflight r2 943
env here · ls /Users/cobalt/cobalt-wt/cos-cutover-tooling/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
- `git show --stat 4a9b60bd` · 0 · `docs(desk): R2214 931 amend drafted, preflight r2 943`, 4 files changed, 35 insertions(+), 6 deletions(-) (the card, 943 preflight r2, cto-2026-10-20.md, the amend draft).
- THE CARD'S SYMBOLS (each `grep -n`, quoted):
  - `grep -n -F "RESIDENTS" ops/desk/deploy-step0.sh` · 0 · `73:RESIDENTS="com.cobalt.aset com.cobalt.radar com.cobalt.agent com.cobalt.cos"`, `875:for label in $RESIDENTS; do`
  - `grep -n -F "com.cobalt.aset|com.cobalt.radar|com.cobalt.agent|com.cobalt.cos)" ops/desk/deploy-outage.sh` · 0 · `90:        com.cobalt.aset|com.cobalt.radar|com.cobalt.agent|com.cobalt.cos) ;;`
  - `grep -n -F "cobalt.sh status is not ONLINE" ops/desk/deploy-outage.sh` · 0 · `436:    fail com.cobalt.agent "cobalt.sh status is not ONLINE: $(first "$out")"`
  - `grep -n -F "section SHIPS" ops/desk/desk-launch.sh` · 0 · `2161:    section SHIPS`
  - `grep -rn -F "ships_checked" ops/desk` · 0 · `ops/desk/desk-launch.sh:1705:ships_checked() {`, `ops/desk/desk-launch.sh:2206:        ships_checked` (one caller)
  - Grep tool `worktree add -b $branch $WT/$wt main` in desk-launch.sh · `2670:    [ -n "$step" ] || add="git -C $REPO worktree add -b $branch $WT/$wt main"` (the Bash form printed nothing: the `$` expanded in its double quotes; re-run with the Grep tool)
  - `grep -n -F "OPS_DESK_PREFIX" src/cobalt/jobs/restarts.py` · 0 · `38:OPS_DESK_PREFIX = "ops/desk/"`, `230:        if not rule and (path in OPS_TOOLS or path.startswith(OPS_DESK_PREFIX)):`
  - `grep -rn -F "deploy-outage.sh" src` · 1 · nothing (no Cobalt reader)
  - Read tool: `deploy-step0.sh:41-42` (P8 census comment), `:874-886` (census loop); `deploy-outage.sh:88-97`, `:118-151`, `:429-437`; `desk-launch.sh:1286-1352`, `:1374-1392`, `:1703-1839`, `:1845-1920`, `:2159-2210`, `:2613-2673`; `DEPLOY-HUB.md:53`, `:65`, `:89`, `:93`, `:123`, `:140`, `:144`, `:146`, `:150`, `:155`, `:160`, `:169` — each where the card names it.
- `wc -l` · `desk-launch.sh` 2782 · `deploy-step0.sh` 908 · `deploy-outage.sh` 443 · `DEPLOY-HUB.md` 188 · `tests/ops/test_deploy_step0.py` 1044 · `tests/ops/test_deploy_outage.py` 608 (equal to the card's RECORDS counts).
- `## READ` report: `tail -n 3 "docs/40 - DevDocs/reports/cos-bootstrap-decisions-2026-10-20.md"` → last line `` `RECORDS: cos bootstrap 929 — no listener overlap (F-14 kept, run.py:44-57); … — brain 9b07db5a 2026-10-20` ``.
- Card 929 at `main`: `git show "main:docs/40 - DevDocs/prompts/2026-10-20/929-deploy-cos-bootstrap-card.md"` · 0 · read whole (its header keys `JOB LADDER BRANCH: none WORKTREE: none BASE: main TIP: none REPORT RULINGS TAG MIGRATIONS: none SET TICKERS: none WAITS`, sections `## LAUNCHD` (one `add` line), `## GATE RESULTS` (14 lines, one label), `## NOT IN THIS JOB`, `## MARKERS`, `## SMOKE READS`, `## CHECK ASKS`, `## RECORDS`).
- `uv run cobalt jobs restarts 4a9b60bd..HEAD` · 0 · one row, the untracked report (`DOCS`, `-`); `RESTARTS: none`. Nothing else in the range.
- The card's `## RECORDS`, copied, each re-read where the list can: drafter 930 at 17:43 EDT, BASE read at `main` `bd7bc0c9` (the card's BASE key is `4a9b60bd`, the launch's); line counts 2782 / 908 / 443 / 188 (re-read, equal); `deploy-step0.sh:73` `RESIDENTS` (re-read, equal); `deploy-outage.sh:90-91`, `:429-437` (re-read: `:90`, `:436`); `DEPLOY-HUB.md:65`, `:123`, `:93`, `:150`, `:169` (re-read with the Read tool, equal); `configs/cobalt/jobs.yaml:127-163` agent row, `:157-158` reads (not re-read: not in this job's files); `desk-launch.sh` order on 929's form (re-read: E2's red shows `incomplete card: no '## SHIPS' section`); `deploy-step-c.sh:37-41`, `:170-196` (not re-read, not changed); installed copies are links (not re-read); RESTARTS homes `restarts.py:38`, `:230` (re-read); BAND HIGH; ORDER.
- No lock probe (`DB: none`).

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `4897 passed, 878 skipped, 4 xfailed, 36 warnings in 765.76s (0:12:45)` — 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.79s`; the one skip `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (names no `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Tests written (no `src/` or script edit): `tests/ops/test_desk_launch_bootstrap_only.py` (new), `tests/ops/test_hub_agent_retired_1020.py` (new), `tests/ops/test_deploy_step0.py` (+3), `tests/ops/test_deploy_outage.py` (+5).
`uv run pytest -q -p no:cacheprovider --color=no --tb=no tests/ops/test_desk_launch_bootstrap_only.py tests/ops/test_hub_agent_retired_1020.py tests/ops/test_deploy_step0.py tests/ops/test_deploy_outage.py` on BASE's scripts and hub → `39 failed, 121 passed, 15 warnings in 104.07s`. The reds, each its row's reason (first lines from the `--tb=line` run):
- T2 `test_t2_the_929_form_is_admitted` → `AssertionError: REFUSED: incomplete card: no '## SHIPS' section`.
- T2 `test_t2_every_partial_form_is_refused` (13 cases) → each `assert 'REFUSED: deploy: bootstrap-only card: ' in "REFUSED: incomplete card: no '## SHIPS' section\n"`, and for `a ## SHIPS section` `… in "REFUSED: incomplete card: TIP 'none' is not 8 hex characters\n"`. BASE refuses them too (exit 1, nothing on stdout) by another message; the test asserts the form's message, so it is RED on BASE by that alone (the docstring says so; the card expected these green on BASE with a weaker assertion).
- T2 `test_t2_every_other_refusal_still_fires`: RED on BASE behind the SHIPS refusal for `a STEP-D0 resume`, `a TAG with a slash`, `a held lock dir`, `no ## MARKERS`, `the agent as the label`, `the deploy report present` (e.g. `assert ('REFUSED: ' in "REFUSED: incomplete card: no '## SHIPS' section\n" and 'the cobalt_dev lock is held' in …)`). GREEN on BASE: `a FILL token`, `the card edited after its commit`, `RULINGS x` — these three are read before the `deploy)` arm (`:1286`, `:1351`, `:1328-1332`) and fire on BASE as after (the card expected all of them red through SHIPS; the docstring states which are not).
- T1c `test_hub_agent_retired_1020.py`: 7 place cases, D1, the eight-line count, P8's read, the GATE minus, STEP-5 (3), the two scripts' record — each `assert 'com.cobalt.agent recorded retired' in …` or the like; count `0`.
- T1a `test_t1_a_retired_agent_is_recorded_retired_with_no_print` → the row `P8 census com.cobalt.agent · launchctl print gui/501/com.cobalt.agent · 0 · pid 4103 · state running (recorded)`; `test_t1_dry_run_names_no_print_of_a_retired_agent` → `assert 'WOULD RUN: launchctl print gui/501/com.cobalt.agent' not in [...]`.
- T1b `test_t1_a_retired_agent_offline_passes_the_final_read` → `FAILED OUTAGE: com.cobalt.agent — cobalt.sh status is not ONLINE:   Cobalt is OFFLINE. · residents: up: com.cobalt.aset · down: none`; `…_in_the_set_is_refused_before_anything_goes_down` → the outage ran (`com.cobalt.agent · pid before 503 · pid after 901`, `OUTAGE DONE 0s`); `…_online_fails_the_final_read` → `OUTAGE DONE 0s`, exit 0; `…_whose_status_is_neither_fails_the_final_read` → `FAILED OUTAGE: com.cobalt.agent — cobalt.sh status is not ONLINE: cobalt.sh: no such pid file …`.
- CONTROLS green on BASE (`-rp` run): `test_t2_a_normal_card_still_cuts_its_gate`, `test_c_the_gate_within_span_is_the_four_labels`, `test_c_d1_still_reads_cos`, `test_c_no_allow_string_changed`, `test_k2_census_lists_cos_after_the_agent`, `test_k2_dry_run_names_the_cos_census`, `test_k2_a_cos_not_loaded_is_recorded_and_fails_nothing`, `test_k2_the_three_residents_rows_are_unchanged`, `test_t1_a_record_without_the_agent_line_changes_nothing`, `test_a_label_outside_the_residents_is_refused_before_anything_goes_down` (4 cases), `test_the_agent_goes_down_by_cobalt_sh_and_up_by_kickstart`, `test_g1_an_agent_offline_at_the_final_status_is_kickstarted_by_the_trap`, `test_k1_*` (5), `test_t1_dry_run_with_a_retired_agent_still_reads_the_status`.
- Commit `11b8b6f9 wip(cos-cutover-tooling): red`.

## E3 THE ROWS
THE RECORD (T1, `## DECISIONS` 1): `ops/desk/retired-labels` (candidate (b)), one label per line; absent today. Each script has ONE reader of it (`deploy-step0.sh` `agent_retired()`, `deploy-outage.sh` one `grep -q -x -F com.cobalt.agent "$REPO/ops/desk/retired-labels"`); the hub reads it with `grep -c -x -F "com.cobalt.agent" /Users/cobalt/cobalt/ops/desk/retired-labels` (the `Bash(grep *)` string of `DEPLOY-HUB.md:11`). No file of this card writes it; tests write it under their tmp repo.
- T2 `ops/desk/desk-launch.sh` `deploy)` arm: the form is read first when any of TIP / BRANCH / WORKTREE is `none`; the whole form or `REFUSED: deploy: bootstrap-only card: <what>`; on the form `section SHIPS`, the `TIP` loop (`hex8` / `commit_exists` / `$merges`), the gate-worktree check and `ships_checked` are skipped, and the deploy `add=` stays empty. Tests: `uv run pytest -q -p no:cacheprovider --color=no --tb=short tests/ops/test_desk_launch_bootstrap_only.py tests/ops/test_desk_launch_launchd.py tests/ops/test_desk_launch_prechecks.py` → `228 passed, 15 warnings in 94.46s`.
- T1a `ops/desk/deploy-step0.sh`: the record and `agent_retired()` beside `RESIDENTS`; the census row of a retired agent is `P8 census com.cobalt.agent · grep -x -F com.cobalt.agent <repo>/ops/desk/retired-labels · 0 · retired (recorded)`, no print, none in the dry run; the header names it. `uv run pytest -q -p no:cacheprovider --color=no --tb=short tests/ops/test_deploy_step0.py` → `82 passed, 15 warnings in 63.29s`.
- T1b `ops/desk/deploy-outage.sh`: the record read before the label loop; the agent in the set with the record → `REFUSED: com.cobalt.agent is retired; a retired label is never restarted; nothing is down` (no call); the final read: OFFLINE passes, ONLINE → `retired but ONLINE: …`, anything else → `retired, and cobalt.sh status is neither OFFLINE nor ONLINE: …`; without the record the `elif` is today's block; the header and the dry-run comment name it. `uv run pytest -q -p no:cacheprovider --color=no --tb=short tests/ops/test_deploy_outage.py` → `38 passed, 15 warnings in 31.57s`.
- T1c `DEPLOY-HUB.md`: one clause each at P8, D1, the STEP-R GATE, smoke (a), STEP-5 (3), THE ONE RESUME (e), smoke (f), the RED list. `uv run pytest -q -p no:cacheprovider --color=no --tb=short tests/ops/test_hub_agent_retired_1020.py tests/ops/test_hub_deferred_1018.py tests/ops/test_hub_cos_restart_1019.py` → `25 passed, 15 warnings in 0.93s`. Then `uv run pytest -q -p no:cacheprovider --color=no --tb=short tests/ops` → `4121 passed, 1 xfailed, 16 warnings in 912.61s (0:15:12)`.
- DEPLOY PROOF counts at the fix: `grep -c -F "card 931 T2" ops/desk/desk-launch.sh` → `1`; `grep -c -F "is retired; a retired label is never restarted" ops/desk/deploy-outage.sh` → `1`; `grep -c -F "retired (recorded)" ops/desk/deploy-step0.sh` → `1`; `grep -c -F "com.cobalt.agent recorded retired" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` → `8`.
- THE MUTATIONS (each made and undone with the Edit tool):
  - T2 (1) `[ -n "$bonly" ] || section SHIPS` → `section SHIPS`: `7 failed, 17 passed` — `test_t2_the_929_form_is_admitted` (`AssertionError: REFUSED: incomplete card: no '## SHIPS' section`) and six of `test_t2_every_other_refusal_still_fires`.
  - T2 (2) `bo()` → `bo() { :; }` (the form check off): `13 failed, 11 passed` — every case of `test_t2_every_partial_form_is_refused`.
  - T2 (3) the deploy `add=` skip removed: `test_t2_the_929_form_is_admitted` → `AssertionError: git -C <tmp>/repo worktree add -b none <tmp>/wt/none main` (`1 failed, 23 deselected`).
  - T1a `if [ "$label" = com.cobalt.agent ] && agent_retired; then` → `if false; then`: `2 failed, 1 passed` — the row `… · pid 4103 · state running (recorded)`; `'WOULD RUN: launchctl print gui/501/com.cobalt.agent' not in […]`. Control break, `grep -q -x -F com.cobalt.agent` → `grep -q .`: `test_t1_a_record_without_the_agent_line_changes_nothing` red (`1 failed, 6 passed`, the agent row absent).
  - T1b `|| agent_retired=1` → `|| agent_retired=""`: `4 failed, 1 passed` — the four T1b tests (`cobalt.sh status is not ONLINE:   Cobalt is OFFLINE.`, the outage ran, `OUTAGE DONE 0s`, the BASE message).
  - T1c the STEP-5 (3) clause removed: `3 failed, 13 passed` — `[STEP-5 (3)]`, `assert 7 == 8`, `test_t1c_step5_never_kickstarts_a_retired_agent`.
  - `git diff --stat` after the undo: the four row files only (75+, 20−), the fix as built; then the four files → `160 passed, 15 warnings in 103.13s`.
- DevDocs: no page under `docs/40 - DevDocs/cobalt/` covers an `ops/desk/` script (Grep for the three script names there: only `jobs/restarts.md`, a list entry); none written (`## RECORDS`).
- Commit `96728174 feat(cos-cutover-tooling): bootstrap-only deploy launch, retired agent record read (T2, T1a, T1b, T1c; L1, L3, L42)`.

## RESTARTS
`uv run cobalt jobs restarts 4a9b60bd..HEAD` (row R5, RUN) →
```
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/cos-cutover-tooling-build-2026-10-20.md	A	DOCS	-
ops/desk/deploy-outage.sh	M	operator script; no Cobalt reader	-
ops/desk/deploy-step0.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_deploy_outage.py	M	test/documentation; no resident	-
tests/ops/test_deploy_step0.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_bootstrap_only.py	A	test/documentation; no resident	-
tests/ops/test_hub_agent_retired_1020.py	A	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row; candidate (b) puts no config in the range.

## W THE THREE SUITES
- (a0) `git diff --name-only --no-renames 4a9b60bd` → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `ops/desk/deploy-outage.sh`, `ops/desk/deploy-step0.sh`, `ops/desk/desk-launch.sh`, `tests/ops/test_deploy_outage.py`, `tests/ops/test_deploy_step0.py`, `tests/ops/test_desk_launch_bootstrap_only.py`, `tests/ops/test_hub_agent_retired_1020.py` — every path under `ops/`, `tests/ops/` or `docs/`.
- **cobalt_dev: not taken (DB: none — 8 paths)**
- `<tip>` = `96728174`.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh cos-cutover-tooling offline` (background) → exit 0:
  ```
  tests/ops: run (docs/40 - DevDocs/prompts/DEPLOY-HUB.md)
  offline 9018/0
  log: /Users/cobalt/cobalt-wt/.gate-logs/cos-cutover-tooling-offline-20261020-184543.log
  ```
  In the log: `956:4897 passed, 878 skipped, 4 xfailed, 36 warnings in 756.14s (0:12:36)` and `1031:4121 passed, 1 xfailed, 16 warnings in 904.43s (0:15:04)` (tests/ops, holding the four files' new tests); `grep -n -F " failed"` → nothing. → `<p>` = 9018.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh cos-cutover-tooling livenote` (background) → exit 0:
  ```
  live-note 148/0
  log: /Users/cobalt/cobalt-wt/.gate-logs/cos-cutover-tooling-livenote-20261020-191341.log
  ```
  `grep -n -F "SKIPPED" <log>` → `56:SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (no skip naming `COBALT_LIVE_VAULT_ROOT`). → `<l>` = 148.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `4121 passed, 1 xfailed, 16 warnings in 899.91s (0:14:59)`.
- with-DB: not run (DB: none). No (b)–(d), no (f).

## PRE-STOP SELF-CHECK
(1) Every added test shown RED for its named reason: E2's 39 reds (quoted under `## E2 RED`) and E3's mutation reds — T2 (1) 7, T2 (2) 13 (the partial forms), T2 (3) 1; T1a 2 and its control's break 1; T1b 4; T1c 3. The tests that stay green on BASE are controls named as such (E2 list), plus three `test_t2_every_other_refusal_still_fires` cases read before the deploy arm (`## DECISIONS` 4). T2 (1) left those three green: they sit outside the arm and pin refusals this build did not move. None of the row tests stayed green under its mutation.
(2) Entry paths: `ships_checked` has one caller (`desk-launch.sh:2233`, PREFLIGHT grep), skipped only on the form; the normal path is pinned by `test_t2_a_normal_card_still_cuts_its_gate` and `tests/ops/test_desk_launch_launchd.py` / `test_desk_launch_prechecks.py` (228 passed). Neither script has a `src` caller (`grep -rn -F "deploy-outage.sh" src` → nothing); `deploy-outage.sh` calls `deploy-step0.sh --window` only, unchanged. Flag combinations: run and `--dry-run` of both scripts with the record present and absent (T1a/T1b tests and the K1/K2 controls); the agent in and out of the set; OFFLINE, ONLINE and neither at the final read; the record holding another label; a STEP-D0 resume on the form.
(3) Re-read at the tip: `grep -n -F "bonly" ops/desk/desk-launch.sh` → `2166`, `2186`, `2188`, `2199`, `2230`, `2233`, `2697`; `grep -n -F "retired" ops/desk/deploy-step0.sh` → `76`, `77`, `78`, `884`, `885`; `grep -n -F "retired" ops/desk/deploy-outage.sh` → `5`, `6`, `12`, `17`, `31`, `43`, `92`, `93`, `96`, `97`, `441`, `442`, `443`, `446`; `git diff --stat 4a9b60bd 96728174` → 8 files, 582 insertions, 20 deletions; the four DEPLOY PROOF counts (E3).

## FOR THE CHECK
- `4a9b60bd..96728174`: `11b8b6f9 wip(cos-cutover-tooling): red` · `96728174 feat(cos-cutover-tooling): bootstrap-only deploy launch, retired agent record read (T2, T1a, T1b, T1c; L1, L3, L42)`.
- Per row, reds / mutations / greens: `## E2 RED`, `## E3 THE ROWS`.
- Caller greps: `## PREFLIGHT`.
- RUN row R5, WHOLE: `## RESTARTS`.
- Suites: offline `9018/0` (executed `gate.sh cos-cutover-tooling offline`, log above); with-DB `not run (DB: none)`; live-note `148/0` (`gate.sh cos-cutover-tooling livenote`); `tests/ops` 4121 passed.
- `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock taken / released: not run (DB: none).
- X5, for the check: on the admitted form the line fills `<worktree>` and `<branch>` with `none`: `"Bash(git -C /Users/cobalt/cobalt merge --ff-only none)"`, `"Bash(git -C /Users/cobalt/cobalt-wt/none merge --no-edit main)"`, `"Bash(git -C /Users/cobalt/cobalt-wt/none merge --abort)"`, `"Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/none/.env)"`, `"Bash(rm /Users/cobalt/cobalt-wt/none/.env)"`; `<tip merges>` fills empty (two spaces). Quoted from mutation T2 (3)'s printed line. No string is added beyond the label's `bootout` / `bootstrap`.

## CONTINUE
next: none (closed)

## DECISIONS
1. THE RECORD's form: candidate (b), `ops/desk/retired-labels`, tracked, one label per line. Why: a plain line is read by `grep -x -F` in `sh` and by the hub's `Bash(grep *)` without parsing; the retirement is a desk commit on `main`, so it is in git history and no deploy merge or data cleanup can drop it; `ops/desk/` has no Cobalt reader (`restarts.py:38`, `:230`), so writing it restarts nothing. (a) is gitignored JSON that `sh` would have to parse; (c) puts a config read by the watchdog, `cobalt validate` and `jobs restarts` into the change. Safe default taken: (b). The retirement desk job writes the file; this card does not.
2. ASK DESK 1 — (c)–(h) of T1c: in (the card's default). ASK DESK 3 — a retired agent ONLINE at the final read fails (`retired but ONLINE: …`), as does a status that is neither: in (the card's default).
3. ASK DESK 4 / X5 — the `none`-filled strings above stand as the launcher fills them; no allow string changed (R60). Default: stand.
4. E2 against the card's expectations: the partial-form tests assert the form's own message, so they are RED on BASE (the card expected green with a weaker assertion); three other-refusal cases (`a FILL token`, `the card edited after its commit`, `RULINGS x`) are GREEN on BASE, because those refusals sit before the `deploy)` arm. Default: kept as written, docstrings say so.

## RECORDS
- Started 17:58:03 EDT, closed 19:29:36 EDT (`date`).
- REFUSED, not needed: `git -C /Users/cobalt/cobalt show "main:docs/40 - DevDocs/prompts/2026-10-20/929-deploy-cos-bootstrap-card.md"` — Permission to use Bash has been denied because Claude Code is running in don't ask mode. (Read instead with the listed `git show main:…` from this worktree.)
- The L74 line: see `## L74`.
- No DevDocs page under `docs/40 - DevDocs/cobalt/` covers an `ops/desk/` script; none written.
- No lock taken (DB: none); `.env` never present (`ls /Users/cobalt/cobalt-wt/cos-cutover-tooling/.env` → No such file, PREFLIGHT and CLOSE).
- Context at close: `context 288545 of 400000 — ok` (`desk-context.sh b51515e0`), above the desk's 250,000 line.
- The card's `## RECORDS`, as re-read at PREFLIGHT: `## PREFLIGHT`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: cos-cutover-tooling · tip: 96728174 | on 4a9b60bd | migration: none | offline 9018/0 | with-DB 0/0 | live-note 148/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 5 of 5 | self-check: 3 of 3 | decisions: 4 · for Dejan: 0 · tokens: 288545
