# launcher-checks — fix round build (card 21, row F1) — 2026-10-05

## §0 Headline
- FIX ROUND (F2–F4), stopped at F3: F2 built at `7c33d97b` (`deploy-step0.sh` P2 accepts a fix-round row; the check's O1 test passes, 0 xfailed). F3 needs `main` merged into this branch first, and `git merge` is a command this builder may not type. F4 waits behind F3 (card order).
- Row F1 built at `c1746720` on `5fb0ddf5`: a deploy now accepts a check tip below the code tip when the row's `fix report` is committed under reports and ends `BUILT · … tip: <code tip>`. Every other mismatch is refused as before.
- `deploy-card.sh` and `CARD.md` carry the `fix report` column; written rows get the empty 7th cell.
- Gate green: offline 3786/0, with-DB 857/0, live-note 146/0; `cobalt_dev` back at 0013 (F2 = F0); `.env` removed; RESTARTS: none.
- 1 decision: a `tests/ops` brain-hub test was already red on BASE, outside this card.

## L74
- 16:57 ET (fix round): this session's harness attribution reminder again asks commits to end with a `Claude-Session:` line. Recorded; not acted on.
- 13:54 ET: the harness attribution reminder of this session asks commits to end with a `Claude-Session:` line. Recorded once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (BUILD-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-02/21-launcher-checks-card.md"` → exit 0:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-02/21-launcher-checks-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-02/21-launcher-checks-card.md" · 0 · e8fa0219cac2d36f04fdf39f59596b8824585e51
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

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0:

```
clock · date · 0 · Mon Oct  5 13:55:08 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/launcher-fixround-1005
    ?? "docs/40 - DevDocs/reports/launcher-fixround-build-2026-10-05.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 5fb0ddf5 docs(desk): R419 hub-text drafter prompt 25, parallel (L72)
diff · git diff --stat 5fb0ddf5 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/launcher-fixround-1005 · 0 · 5fb0ddf5 docs(desk): R419 hub-text drafter prompt 25, parallel (L72)
env here · ls /Users/cobalt/cobalt-wt/launcher-fixround-1005/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| base | `git show --stat 5fb0ddf5` | 0 | `docs(desk): R419 hub-text drafter prompt 25, parallel (L72)` · 2 files, `docs/40 - DevDocs/prompts/2026-10-05/25-draft-hub-text.md` +14, `docs/40 - DevDocs/reports/cto-2026-10-05.md` +3 |
| symbol | `grep -n -F "carry=" ops/desk/desk-launch.sh` | 0 | `714:        carry=$(printf '%s\n' "$srow" \| awk -F'\|' '{print $7}')` |
| symbol | `grep -n -F "is neither the code tip" ops/desk/desk-launch.sh` | 0 | `748: … \|\| refuse "deploy $sbranch: the check's tip '$ltip' is neither the code tip $ctip nor the branch head $shead — the check is not clean: $clast"` |
| symbol | `grep -n -F "ship_cell" ops/desk/desk-launch.sh` | 0 | `710 sbranch`, `711 ctip`, `712 shead`, `713 crep`, `762` comment, `763:ship_cell() {` |
| symbol | `grep -n -F "REPORTS=" ops/desk/desk-launch.sh` | 0 | `161:REPORTS="$REPO/docs/40 - DevDocs/reports"` |
| symbol | `grep -n -F "its stop line must carry" ops/desk/deploy-card.sh` | 0 | `207:\| # \| branch \| code tip \| branch head \| check report \| its stop line must carry \|` |
| symbol | `grep -n -F "ships=" ops/desk/deploy-card.sh` | 0 | `94:ships=""` · `141:    ships="$ships\| $n \| … \| \`held unfixed: 0\` and \`ready: YES\` \|$nl"` |
| symbol | `grep -n -F "its stop line must carry" "docs/40 - DevDocs/prompts/CARD.md"` | 0 | `44:\| # \| branch \| code tip \| branch head \| check report \| its stop line must carry \|` |
| symbol | `grep -n -F "def break_other_tip" tests/ops/test_desk_launch_prechecks.py` | 0 | `430:def break_other_tip(desk):` (and `Desk` :73, `built_line` :141, `write_build_report` :145, `ship` :185, Read tool) |
| callers | `grep -rn -F "deploy-card.sh" tests/ops` | 0 | `tests/ops/test_deploy_card.py:1`, `:19 SCRIPT = REPO / "ops" / "desk" / "deploy-card.sh"`; its SHIPS asserts are substrings of a row (`:179`–`:186`) |
| wc | `wc -l` | 0 | `1086 ops/desk/desk-launch.sh` · `218 ops/desk/deploy-card.sh` · `675 tests/ops/test_desk_launch_prechecks.py` · `138 docs/40 - DevDocs/prompts/CARD.md` |
| READ tail | `tail -n 3 ".../reports/deploy-2026-10-01-1.md"` | 0 | `FAILED: gate — G (c) — tests/cobalt/test_radar_score_migration.py::test_card_checks_index_and_receipt_immutability_on_cobalt_dev (TooManyColumns: cobalt_dev "user".aset_sizings 1581/1600 column slots) · rollback: not used · decisions: 2 · for Dejan: 0` |
| RESTARTS | `uv run cobalt jobs restarts 5fb0ddf5..HEAD` | 0 | `docs/40 - DevDocs/reports/launcher-fixround-build-2026-10-05.md A DOCS -` · `RESTARTS: none` (only this untracked report; no code path) |
| bare-guard | `grep -n -F "carry=$(printf" …` | — | blocked by the bare-command hook (`$(`), resent as `grep -n -F "carry="`; not a refusal |

Card records copied (re-read where the list can): RESTARTS homes — `ops/desk/desk-launch.sh` → `ops/desk/` rule, `tests/ops/*` → test/documentation, `docs/…` → DOCS (confirmed by the table above for `docs/`); the three refused launches of 10-01; classes his 2026-10-02 R39; outside house set aside (R47, confirmed in AUTHORIZATION); judge answers 2026-10-02 R41 (L3 refusals present: `test_l3_a_deploy_card_whose_ships_table_has_no_row_refuses`, `test_l3_a_tip_head_that_is_the_head_of_no_ships_row_refuses`); the `DeadlockDetected` known flake (applies only if W meets it).

Header: no `DB: none` key — W runs `gate.sh … all` (with the lock).

## E0 BASELINE
On `5fb0ddf5`, no edit:
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3786 passed, 756 skipped, 1 xfailed, 36 warnings in 651.40s (0:10:51)`, exit 0.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 30.74s`; the one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (names no `COBALT_LIVE_VAULT_ROOT`).
- Extra, for the row's file set: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` on BASE → `1 failed, 1347 passed, 1 xfailed, 15 warnings in 362.93s`; the red is `tests/ops/test_desk_launch_brain.py::test_the_trees_brain_hub_line_is_printed_with_its_handover_filled` — `assert INSTALL in text  # the title token stands until his approval row` → `AssertionError: assert '«INSTALL' in '# BRAIN-HUB — the standing brain seat (installed 2026-10-05 on his 2026-10-02 R54 …'`. Outside this card's rows (`git log --oneline -3 -- tests/ops/test_desk_launch_brain.py "docs/40 - DevDocs/prompts/BRAIN-HUB.md"` → `4a19b075 docs(desk): R357 wake-up ecc18b72; R358 BRAIN-HUB installed on R54 …`); not fixed here (DECISIONS 1).

## E2 RED
Tests only, in `tests/ops/test_desk_launch_prechecks.py`: `Desk.write_deploy` gains `fix=` (None: today's six columns; a string: the `fix report` column with that cell); new `fix_round`, `neither`, `ships_lines` helpers and five tests (F1 block, before L4). No with-DB red (the row is shell and docs): no lock take at E2.

`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_launch_prechecks.py -k f1` on BASE code → `3 failed, 7 passed, 68 deselected, 15 warnings in 5.84s`. Reds:
- `test_f1_a_fix_round_past_the_checked_tip_launches` → `REFUSED: deploy ops/x-job: the check's tip '97d54377' is neither the code tip 4272bd57 nor the branch head 4272bd57 — the check is not clean: CHECK DONE · … tip: 97d54377 …` (the row's named reason).
- `test_f1_deploy_card_writes_the_fix_report_column_and_its_empty_cell` → `AssertionError: | # | branch | code tip | branch head | check report | its stop line must carry |` (`header.endswith("| fix report |")`).
- `test_f1_card_md_ships_header_has_the_fix_report_column_and_a_matching_separator` → same header assertion on `CARD.md`.
Green on BASE, as the card says: the five negative controls `test_f1_a_fix_round_missing_one_proof_still_refuses[(a) empty cell | (b) BUILT for the checked tip | (b) FAILED line naming the code tip | (c) report uncommitted | (d) checked tip not an ancestor]` (each refused for `neither the code tip`) and `test_f1_a_card_of_todays_shape_passes_as_today[code tip | head]` (six columns and the empty-cell seven columns).
Commit `7681e81f wip(launcher-checks): red — F1 fix-round tip launches; fix report column in deploy-card.sh and CARD.md`.

## E3 THE ROWS
Row F1 only (L1–L6 shipped, not rebuilt). Lines re-read before the edit (`desk-launch.sh` :714, :746-748; `deploy-card.sh` :141, :207-208; `CARD.md` :44-45).
- `ops/desk/desk-launch.sh`: after :714 `frep=$(ship_cell "$srow" 8)`; at :746-748 a `fixed_ok` test ORed after today's two equalities: `frep` non-empty, under `"$REPORTS"/*.md`, a file, committed and unmodified (the :733-736 commands), `git -C "$REPO" merge-base --is-ancestor "$ltip" "$ctip"`, last non-blank line `"BUILT ·"*"tip: $ctip"*`. Else today's refuse, unchanged. :749-757 unchanged.
- `ops/desk/deploy-card.sh`: header :207 gains `fix report |`, separator :208 a 7th `---|`, row :141 an empty 7th cell (`… \`ready: YES\` | |`).
- `docs/40 - DevDocs/prompts/CARD.md` :44-45 only: header gains `fix report`, separator a 7th cell.
- Row tests after the fix: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_launch_prechecks.py tests/ops/test_deploy_card.py` → `105 passed, 15 warnings in 40.81s`. With the launcher files beside them (`… tests/ops/test_devdb_lock.py tests/ops/test_desk_launch_devfix.py tests/ops/test_desk_size_guard.py` added) → `214 passed, 1 xfailed, 15 warnings in 127.82s`.
- DevDocs page: none exists for `ops/desk/desk-launch.sh` or `deploy-card.sh` under `docs/40 - DevDocs/cobalt/` (`grep -rln -F "desk-launch" "docs/40 - DevDocs/cobalt"` → only `jobs/restarts.md`); none invented, as the 10-02 build (`launcher-checks-build-2026-10-02.md:169`).

THE MUTATIONS (Edit tool, each undone, F1 tests run alone with `-k f1` or the named test):

| # | mutation | result (summary · first failing line) |
|---|---|---|
| M1 | `\|\| fixed_ok` removed (the fix undone) | `1 failed, 9 passed` · `test_f1_a_fix_round_past_the_checked_tip_launches` — `REFUSED: … the check's tip '1c592be6' is neither the code tip a92f423d nor the branch head a92f423d` |
| M2 | `fixed_ok` returns 0 first | `5 failed, 5 passed` · all five `test_f1_a_fix_round_missing_one_proof_still_refuses[…]` |
| M3 | last-line case `"BUILT ·"*"tip: $ctip"*` → `*` | `2 failed, 8 passed` · `[(b) BUILT for the checked tip]`, `[(b) FAILED line naming the code tip]` |
| M4 | the committed-and-unmodified test → `true` | `1 failed, 9 passed` · `[(c) report uncommitted]` |
| M5 | the `merge-base --is-ancestor` test → `true` | `1 failed, 9 passed` · `[(d) checked tip not an ancestor]` |
| M6 | today's equalities removed (only `fixed_ok`) | `2 failed, 8 passed` · `test_f1_a_card_of_todays_shape_passes_as_today[code tip]`, `[head]` |
| M7 | `deploy-card.sh` header and separator reverted | `1 failed, 77 deselected` · `AssertionError: \| # \| branch \| … \| its stop line must carry \|` (`endswith('\| fix report \|')`) |
| M8 | `deploy-card.sh` :141 empty cell removed | `1 failed, 77 deselected` · `assert (True and False)` — the row `.endswith('\| \|')` |
| M9 | `CARD.md` separator left at six cells | `1 failed, 77 deselected` · `assert 8 == 7` (header vs separator pipes) |

`git diff --stat` after the undo → `CARD.md 4 ++--`, `deploy-card.sh 6 +++---`, `desk-launch.sh 22 +++++++++++++++++++++-` (the fix only). No test stayed green under its mutation; none rewritten.
Commit `c1746720 fix(launcher-checks): a deploy accepts a check tip below the code tip when the SHIPS row's fix report is committed and BUILT on the code tip; deploy-card.sh and CARD.md carry the fix report column (F1, R376, L75)`.

### FIX ROUND (rows F2–F4), resumed at E3 16:57 ET on the desk's `CONTINUE: E3`
Verified first (L35): `git status --short --branch` → `## ops/launcher-fixround-1005` plus this report; `git log --oneline -6` → `7e7803d5` (the check's F1 fix) on `553f8c7b` (the check's O1 strict xfail) on `36b98d61` (this report) on `c1746720`; `ls -la …/.env` → `No such file or directory`. `sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "<card>"` re-run, since the card gained rows F2–F4 → `AUTHORIZED`, exit 0; `CARD COMMITTED … b2a903d5c2a5dc145836b56c194a55874db75a8e`, `CARD UNCHANGED … nothing`; R60, R412, R47 rows as at the first AUTHORIZATION.
`git -C /Users/cobalt/cobalt diff --stat 5fb0ddf5 main -- "docs/40 - DevDocs/prompts/CARD.md" ops/desk/deploy-step0.sh tests/ops/test_deploy_step0.py` → nothing (those three files are the same on `main` as on BASE). `git -C /Users/cobalt/cobalt diff --stat 7e7803d5 main -- … "docs/40 - DevDocs/prompts/DEPLOY-HUB.md" …` → `DEPLOY-HUB.md | 16 +++++++---------` (card 26, deployed): on `main`, line 57 (`**P1 DATE**`) has changed; line 58 (`**P2 EVERY CHECK, COMMITTED**`) is the same on `main` and here.

**Row F2** (`ops/desk/deploy-step0.sh`, `tests/ops/test_deploy_step0.py`).
- RED (tests only, no script edit): the strict-xfail mark removed from `test_o1_a_fix_round_row_the_launcher_accepts_passes_p2`, assertion unchanged. Added `fix_round(desk, …)`, `test_f2_a_fix_round_row_passes_p2_and_step0` and `test_f2_a_fix_round_missing_one_proof_still_fails_p2[(a) fix report cell empty | (b) fix report BUILT for the checked tip | (c) checked tip not an ancestor]`. `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_deploy_step0.py -k "o1 or f2 or not_the_row_s_code_tip"` on the unchanged script → `2 failed, 4 passed, 36 deselected`; both reds end `FAILED STEP-0: P2 check 1 — …/alpha-check.md — its tip db231e71 is not the row's code tip dc7d9471` (the row's reason). Green there, as the card says: the three negative controls and `test_a_check_report_whose_tip_is_not_the_row_s_code_tip_fails`. Commit `4e8296fc wip(launcher-checks): red — F2 fix-round row passes STEP-0 P2 (O1 xfail mark removed; negative controls a-c)`.
- FIX: after `lits=` (:337) `frep=` reads column 8; inside the P2 tip test (after :384), when the tip is not the code tip and `frep` is non-empty, `why` is cleared only if the fix report's last non-blank line matches `"BUILT ·"*"tip: $ctip"*` and `git -C "$REPO" merge-base --is-ancestor "$t" "$ctip"` holds. Otherwise today's refusal, with the reason added. The literals stay the check report's. A row with no fix report takes today's path.
- One test rewritten: my own last assertion of `test_f2_a_fix_round_row_passes_p2_and_step0` split the P2 row on ` · `, which the check line itself contains. It failed on the fixed script with `STEP-0 OK` printed. Rewritten to `" · 0 · CHECK DONE " in p2[0]`.
- GREEN: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_deploy_step0.py` → `42 passed, 15 warnings in 23.97s` (0 xfailed). With the F1 files: `… tests/ops/test_deploy_step0.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_deploy_card.py` → `149 passed, 15 warnings in 63.45s`.
- MUTATIONS (Edit tool, each undone):

| # | mutation | result (summary · first failing line) |
|---|---|---|
| M10 | `why=""` on the accepting path → `:` (the fix undone) | `2 failed, 4 passed` · `test_o1_a_fix_round_row_the_launcher_accepts_passes_p2`, `test_f2_a_fix_round_row_passes_p2_and_step0` — `FAILED STEP-0: P2 check 1 — … its tip 7f7e1cf0 is not the row's code tip 4a756527` |
| M11 | the `merge-base --is-ancestor` test → `true` | `1 failed, 5 passed` · `[(c) checked tip not an ancestor]` |
| M12 | the `"BUILT ·"*"tip: $ctip"*` pattern → `*` | `1 failed, 5 passed` · `[(b) fix report BUILT for the checked tip]` |
| M13a | only the `[ -n "$frep" ]` guard removed | `42 passed`. The guard is redundant: an empty cell has no file, so `flast` is empty and the BUILT test refuses it anyway. Not a test gap. |
| M13 | an empty cell read as a fix round (`[ -n "$frep" ] \|\| flast="BUILT · tip: $ctip"`) | `1 failed, 41 passed` · `[(a) fix report cell empty]` |

`git diff 4e8296fc -- ops/desk/deploy-step0.sh` after the undo → the fix only (+16 lines at :338 and :385-399). DevDocs page: `Grep "deploy-step0"` under `docs/40 - DevDocs/cobalt` → none; none invented.
Commit `7c33d97b fix(launcher-checks): STEP-0 P2 accepts a fix-round row: the check tip an ancestor of the code tip and the fix report BUILT on it; check O1 test passes (F2, R376, L75)`.

**Row F3** — STOPPED before any edit. The card: "BEFORE writing this row the builder merges `main` into its branch, then re-reads line 58". `git merge` is on BUILD-HUB's never-typed list (`## THE LIST`: "Never typed: … `git merge` …") and matches no allow string of the launch line. I did not type it. BASE read for the RUN row: Grep (count, fixed text ``the check's `tip:` is an ancestor of the code tip``) over `docs/40 - DevDocs/prompts` → `0` (both `DEPLOY-HUB.md` and `CARD.md`); `DEPLOY-HUB.md:58` is the `**P2 EVERY CHECK, COMMITTED**` line.
**Row F4** — not started (card order, behind F3). BASE read: `grep -n -F "The last column is" CARD.md` (Grep tool) → `47:The code tip is the \`tip:\` of the check's stop line (a fresh Opus pass may have moved it past the build's). The last column is \`held unfixed: 0\` and \`ready: YES\` for a check run on \`CHECK-HUB.md\`; a report of the old shape keeps its own literals.`

## RESTARTS
`uv run cobalt jobs restarts 5fb0ddf5..HEAD` →
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CARD.md	M	DOCS	-
docs/40 - DevDocs/reports/launcher-fixround-build-2026-10-05.md	A	DOCS	-
ops/desk/deploy-card.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_desk_launch_prechecks.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row.

## W THE THREE SUITES
`<tip>` = `c1746720`. The card has no `DB: none` key: `sh /Users/cobalt/cobalt/ops/desk/gate.sh launcher-fixround-1005 all` (no `--deselect`: this build adds no with-DB test; no `--tickers`: none written; no `--migration`) → exit 0. Verdict lines, whole:

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
log: /Users/cobalt/cobalt-wt/.gate-logs/launcher-fixround-1005-all-20261005-141405.log
```

- (a) offline: log :829 `3786 passed, 756 skipped, 1 xfailed, 36 warnings in 628.65s` → `offline 3786/0`. This build adds no test under `tests/cobalt` or `tests/taxonomy`; its five tests are in `tests/ops` (run below).
- (b) `lock taken: launcher-fixround-1005` (log :835), `lock: waited 0 min`; `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (:846); `LEVEL 0013`.
- (c) PASS 1, executed (log :900): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --db-only --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py` → :969 `684 passed, 7 skipped, 3850 deselected, 2 xfailed, 12 warnings in 123.32s` → `<d1>` = 684. Skips quoted in the verdict block above (none marked `OUTSIDE the allowed set`).
- (c2) `dev forward: APPLIED 14:26:57` (:971); `F1: 893 44 126f2d6983fa59f9d0eaaff7da7dd29c` (:1046).
- (c3) PASS 2 → :1528 `173 passed, 1 deselected, 5 warnings in 222.13s` → `<d2>` = 173; `<d>` = 684 + 173 = 857 = `with-DB 857/0`. No with-DB test of this build to find in the `-rA` lines.
- (c3r) `stray rows: not read (no --tickers given)` — this build writes no ticker.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (:1593) = F0 field for field → `cobalt_dev: 0013 — F2 = F0` (:1644); `lock released` (:1646); `.env: removed`; `ls /Users/cobalt/cobalt-wt/launcher-fixround-1005/.env` → `No such file or directory`.
- (e) live-note, `.env` absent → :1715 `146 passed, 1 skipped, 15 warnings in 26.29s` → `live-note 146/0`; the skip is `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`.
- `tests/ops` at the tip (the row's suite; the gate does not run it): `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `1 failed, 1357 passed, 1 xfailed, 15 warnings in 349.83s`. The one red is the BASE red of E0, `test_the_trees_brain_hub_line_is_printed_with_its_handover_filled` (DECISIONS 1); BASE had `1347 passed`, +10 = this build's ten test ids (1 + 5 + 2 + 1 + 1).

## PRE-STOP SELF-CHECK
(1) Every added or changed test shown RED for its named reason against a mutation or negative control — YES: `test_f1_a_fix_round_past_the_checked_tip_launches` red at E2 on BASE and under M1; the five `test_f1_a_fix_round_missing_one_proof_still_refuses[…]` red under M2, and (b)×2 under M3, (c) under M4, (d) under M5; `test_f1_a_card_of_todays_shape_passes_as_today[…]` ×2 red under M6; `test_f1_deploy_card_writes_…` red at E2 and under M7, M8; `test_f1_card_md_…` red at E2 and under M9 (E3 table). The changed fixture `write_deploy(fix=None)` keeps today's text: the 78 older ids of the file stay green (`105 passed` with `test_deploy_card.py`). None stayed green; none rewritten.
(2) Every entry path pinned — YES: `grep -n -F "ships_checked" ops/desk/desk-launch.sh` → `699:ships_checked() {`, `906: ships_checked` (the deploy kind, its one caller), pinned by the F1 launch tests; the `STEP-D0` resume skips it (existing `test_l3_a_step_d0_resume_is_not_re_checked`); both card shapes (six columns, seven with an empty cell) pinned by `test_f1_a_card_of_todays_shape_passes_as_today`; `deploy-card.sh`'s callers (`grep -rn -F "deploy-card.sh" tests/ops` → `test_deploy_card.py`) green with the extra cell, and pinned by `test_f1_deploy_card_writes_…`. A card with several SHIPS rows runs the same per-row test (`while … read -r srow`); no separate multi-row fix-round test.
(3) Every `file:line`, count and quote re-read at the tip — YES: `grep -n -F "frep" ops/desk/desk-launch.sh` (→ :715, :751-761), `grep -n -F "fix report |" ops/desk/deploy-card.sh "docs/40 - DevDocs/prompts/CARD.md"` (→ `deploy-card.sh:207`, `CARD.md:44`), `grep -n -F "def test_f1_" tests/ops/test_desk_launch_prechecks.py` (→ :580, :592, :609, :630, :645), `git diff --stat 5fb0ddf5 c1746720` (4 files, +135 −10), the gate log greps above.

## FOR THE CHECK
- Range `5fb0ddf5..c1746720`: `7681e81f wip(launcher-checks): red — F1 fix-round tip launches; fix report column in deploy-card.sh and CARD.md` · `c1746720 fix(launcher-checks): a deploy accepts a check tip below the code tip when the SHIPS row's fix report is committed and BUILT on the code tip; deploy-card.sh and CARD.md carry the fix report column (F1, R376, L75)`.
- Row F1: reds at `## E2 RED`, mutations M1–M9 at `## E3 THE ROWS`, greens `105 passed` and `214 passed, 1 xfailed` (E3), `tests/ops` at the tip `1357 passed` + the BASE red.
- Caller greps: `## PRE-STOP SELF-CHECK` (2); PREFLIGHT table.
- RUN rows: none in this round (L5, L6 shipped).
- Suites: offline `3786 passed, 756 skipped, 1 xfailed`; with-DB pass 1 `684 passed, 7 skipped, 3850 deselected, 2 xfailed` (command at W (c)), pass 2 `173 passed, 1 deselected`; live-note `146 passed, 1 skipped`.
- One lock take (the gate's): `F0 664 35 272c95bbb12241e3611e4b36326ccf87` · `F1 893 44 126f2d6983fa59f9d0eaaff7da7dd29c` · `F2 664 35 272c95bbb12241e3611e4b36326ccf87`. Taken in the gate started 14:14 (log name `…-20261005-141405.log`, `waited 0 min`), forward applied 14:26:57, `lock released` (log :1646) before the gate's exit; the log prints no clock on the take or release lines.
- RESTARTS table: `## RESTARTS` (`RESTARTS: none`).
- Records copied at PREFLIGHT: `## PREFLIGHT` last paragraph.
- Seam as the card states it (L72): the `fix report` must sit under `$REPORTS` (the main repo's reports folder) and be committed there, as the check report; a fix report committed only on the job branch is refused.

## CONTINUE
next: E3 row F3, once `main` is merged into `ops/launcher-fixround-1005` (by the desk; this builder may not type `git merge`). Then re-read `DEPLOY-HUB.md:58`, then F3, F4, RESTARTS, W (the gate, for tip ≥ `7c33d97b`), PRE-STOP SELF-CHECK, CLOSE. F2 is built and committed (`7c33d97b`).

## DECISIONS
1. `tests/ops/test_desk_launch_brain.py::test_the_trees_brain_hub_line_is_printed_with_its_handover_filled` is red on BASE `5fb0ddf5` and at the tip (`assert INSTALL in text` — BRAIN-HUB.md now carries `installed 2026-10-05 …`, commit `4a19b075 … R358 BRAIN-HUB installed on R54 …`). It lies outside this card's rows and files; the gate's suites do not run `tests/ops`, but a deploy gate that runs `tests/ops` would meet it. Safe default taken: not touched; the desk routes it (a card for that test, or the deploy gate's reading).
2. FIX ROUND, row F3 BLOCKS. The card orders "merges `main` into its branch" before line 58 is written. `git merge` is never typed by a builder (BUILD-HUB `## THE LIST`) and matches no allow string. `main` changed `DEPLOY-HUB.md:57` (card 26, P1); line 58 is still the same text on both. If line 58 is edited without the merge, the deploy gate's merge of this branch would meet `main`'s line-57 change in the next line, and git conflicts on changes that touch. Safe default taken: stopped before F3, nothing typed, F4 not started (card order). Needed: the desk merges `main` into `ops/launcher-fixround-1005` (or rules otherwise), then sends `CONTINUE: E3`.

## RECORDS
- L74: the harness attribution reminder asked for a `Claude-Session:` line on commits; recorded once under `## L74`, not acted on.
- `REFUSED`, not needed: none. Bare-guard block once at PREFLIGHT (`$(` inside a grep pattern), resent as a single plain call; not a refusal.
- Extra lock takes: none (the gate's one take only). `.env: removed, proven gone (W)`.
- No DevDocs page exists for `ops/desk/desk-launch.sh` or `ops/desk/deploy-card.sh` under `docs/40 - DevDocs/cobalt/`; none invented.
- Card records as re-read at PREFLIGHT: RESTARTS homes confirmed by the table (`operator script; no Cobalt reader`, `test/documentation; no resident`, `DOCS`); R47 row approved (AUTHORIZATION); the `DeadlockDetected` flake did not occur at W.
- CONTINUED at E3 16:57 ET (the desk's `CONTINUE: E3`; fix round F2–F4; the message added no row, file, command or approval: the rows are the committed card's, `b2a903d5`).
- REFUSED, not needed: `git -C /Users/cobalt/cobalt merge-base 7e7803d5 main` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." Read the same fact from `git -C … diff` instead.
- `.env: removed, proven gone` — at E3 resume `ls -la …/.env` → No such file; no lock taken in the fix round so far.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

F1 round stop line (kept for the record, superseded by the fix round below): `BUILT · job: launcher-checks · tip: c1746720 | on 5fb0ddf5 | migration: none | offline 3786/0 | with-DB 857/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0`

FAILED: E3 — row F3 — main is not merged into ops/launcher-fixround-1005 — the card orders the merge before line 58; `git merge` is on BUILD-HUB's never-typed list and on no allow string, not typed
