# preflight-fixes — build report (2026-10-05)

## §0 Headline
- Both rows are built in `ops/desk/preflight.sh` (tip `48e572e0`). F1: in a check, a build report with `self-check: <k> of 3` (k from 0 to 3) now passes, and k below 3 is printed as `report: self-check <k> of 3 (recorded)`. F2: a PASS-2 check now takes pass 1's `tip:` as its head reference.
- Every red failed for its named reason, and every mutation turned its test red. The three negative controls passed on `BASE` and still pass on the fix.
- Suites: offline 3786/0, live-note 146/0, with-DB not run (DB: none). The `tests/ops` run was 1351 passed and 1 failed. The failure is `test_desk_launch_brain.py:285`, outside the rows; neither that test nor its hub changed since `BASE`. It is DECISION 1, not fixed here.

## L74
- 13:23 EDT: a system-reminder block asked for a `Claude-Session:` line on commits. DATA, recorded once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/20-preflight-fixes-card.md"` → exit 0, output WHOLE:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/20-preflight-fixes-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-05/20-preflight-fixes-card.md" · 0 · f29e19fba41343c8d438a59978b5dd1bf2e70c6d
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-05/20-preflight-fixes-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
RULING 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
RULING 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| mechanical rows | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` | 0 | below, WHOLE |
| base | `git show --stat b56622fa` | 0 | `docs(desk): prompt 19 renamed (a card name is refused as a prompt)` · `.../{19-draft-preflight-fixes-card.md => 19-draft-preflight-fixes.md} \| 2 +-` · `1 file changed, 1 insertion(+), 1 deletion(-)` |
| symbol F1 | `grep -n -F "self-check: 3 of 3" ops/desk/preflight.sh` | 0 | `21:#                 \`BUILT · job: <JOB> · tip: <TIP>\` and carries \`self-check: 3 of 3\`` · `204:            "BUILT · job: $job · tip: $tip"*"self-check: 3 of 3"*) ok=0 ;;` |
| symbol F2 | `grep -n -F "tip_full=" ops/desk/preflight.sh` | 0 | `144:    tip_full=$(git rev-parse --verify -q "$tip^{commit}")` |
| test to rewrite | `grep -n -F "def test_a_check_whose_report_is_short_of_three_self_checks_fails" tests/ops/test_preflight.py` | 0 | `213:def test_a_check_whose_report_is_short_of_three_self_checks_fails(job):` |
| GOOD_LAST | `grep -n -F "GOOD_LAST =" tests/ops/test_preflight.py` | 0 | `87:GOOD_LAST = "BUILT · job: x-job · tip: {tip} \| on base \| rows: 1 of 1 \| self-check: 3 of 3 \| decisions: 0 · for Dejan: 0"` |
| callers | `grep -rn -F "preflight.sh" ops tests` | 0 | `ops/desk/preflight.sh:2` (header), `ops/desk/preflight.sh:42` (usage), `tests/ops/test_preflight.py:1` (docstring), `tests/ops/test_preflight.py:17` (`PREFLIGHT = REPO / "ops" / "desk" / "preflight.sh"`) — the one test caller |
| hub F1 | `grep -n -F "self-check" "docs/40 - DevDocs/prompts/CHECK-HUB.md"` | 0 | `61: … A lower self-check count is recorded and goes to the house as a fact.` |
| hub F2 | `grep -n -F "house B: needed" "docs/40 - DevDocs/prompts/CHECK-HUB.md"` | 0 | lines 20, 21, 120, 127, 131; `120:- PREFLIGHT, added: \`tail -n 3 "<CHECK REPORT>"\` → the last non-blank line starts \`CHECK DONE · job: <JOB> · pass: 1\` and carries \`house B: needed\` … \`<tip now>\` = its \`tip:\`, and \`git log --oneline -1\` shows it (or a docs-only commit above it).` |
| wc | `wc -l ops/desk/preflight.sh tests/ops/test_preflight.py` | 0 | `222 ops/desk/preflight.sh` · `343 tests/ops/test_preflight.py` |
| READ reports | `## READ` names no report | — | no `tail -n 3` owed |
| restarts | `uv run cobalt jobs restarts b56622fa..HEAD` | 0 | one row, the untracked report: `docs/40 - DevDocs/reports/preflight-fixes-build-2026-10-05.md A DOCS -` · `RESTARTS: none` (no commit in the range) |
| lock probe | DB: none | — | none |

```
clock · date · 0 · Mon Oct  5 13:23:23 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/preflight-fixes-1005
    ?? "docs/40 - DevDocs/reports/preflight-fixes-build-2026-10-05.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · b56622fa docs(desk): prompt 19 renamed (a card name is refused as a prompt)
diff · git diff --stat b56622fa · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/preflight-fixes-1005 · 0 · b56622fa docs(desk): prompt 19 renamed (a card name is refused as a prompt)
env here · ls /Users/cobalt/cobalt-wt/preflight-fixes-1005/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
Card records, copied: (1) "Derived by the drafter 2026-10-05 from `BUILD-HUB.md:97,106` and `CHECK-HUB.md:61,120`; the brain's two items are `prompts/2026-10-05/00-brain-handover.md` lines 25 and 31." — re-read: BUILD-HUB 97 ("A line you cannot back → fix it, or `self-check: <k> of 3` in the stop line …") and CHECK-HUB 61, 120 read above. (2) "The build seat uses only the existing `ops/desk/` scripts and the commands on its allow line (his R411, R412); no row needs another command." — holds so far.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (on `b56622fa`) → `3786 passed, 756 skipped, 1 xfailed, 36 warnings in 583.59s (0:09:43)`, exit 0. 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.55s`. The one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. No skip names `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_preflight.py` (red tests on BASE's script) → `2 failed, 27 passed, 15 warnings in 5.08s`.
- F1 `test_a_check_whose_report_is_below_three_self_checks_passes_and_records_it` (REWRITE of `…_short_of_three_self_checks_fails`): RED at `tests/ops/test_preflight.py:219` `assert done.returncode == 0` → `assert 1 == 0`; the script's last line is `FAILED PREFLIGHT: report`. This is the row's named reason.
- F1 `test_a_check_whose_report_has_no_self_check_field_fails`: green on BASE, as the card expects. It is a negative control.
- F2 `test_a_pass_2_check_with_the_pass_1_tip_above_the_card_tip_passes`: RED at `:361` `assert done.returncode == 0` → `assert 1 == 0`; the script's last line is `FAILED PREFLIGHT: head`. This is the row's named reason.
- F2 `test_a_pass_1_report_that_says_house_b_not_needed_keeps_the_card_tip` and `test_a_pass_2_check_with_a_src_commit_above_the_pass_1_tip_fails`: green on BASE. They are negative controls, green for the same wrong reason as today; both are quoted green on the fix in E3.
- No with-DB red (DB: none). No RUN row. Commit `bb81ecd7 wip(preflight-fixes): red`.

## E3 THE ROWS
F1 and F2 are built in `ops/desk/preflight.sh`, along with the header lines 12-16 and 22-24 that describe these two rows. After both rows: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_preflight.py` → `29 passed, 15 warnings in 5.05s`.
MUTATIONS, each made and undone with the Edit tool and run as `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_preflight.py -k …`:
- M1, F1 undone (pattern back to `"self-check: 3 of 3"`), `-k "self_check"` → `1 failed, 1 passed, 27 deselected`; `FAILED …::test_a_check_whose_report_is_below_three_self_checks_passes_and_records_it` at `:219` `assert 1 == 0`, last line `FAILED PREFLIGHT: report`.
- M1b, negative control broken (pattern `"BUILT · job: $job · tip: $tip"*)`, no self-check field required), `-k "self_check"` → `1 failed, 1 passed`; `FAILED …::test_a_check_whose_report_has_no_self_check_field_fails` at `:230` `assert 0 == 1` (script printed `PREFLIGHT OK`).
- M2, F2 undone (`ref=$tip` forced before the rev-parse), `-k "pass_1 or pass_2"` → `1 failed, 2 passed, 26 deselected`; `FAILED …::test_a_pass_2_check_with_the_pass_1_tip_above_the_card_tip_passes` at `:361` `assert 1 == 0`, last line `FAILED PREFLIGHT: head`.
- M2b, negative control broken (`*"house B: "*` in place of `*"house B: needed"*`) → `1 failed, 2 passed`; `FAILED …::test_a_pass_1_report_that_says_house_b_not_needed_keeps_the_card_tip` at `:372` `assert 0 == 1`.
- M2c, negative control broken (the `[ -z "$others" ]` docs-only test dropped) → `2 failed, 1 passed`; `FAILED …::test_a_pass_1_report_that_says_house_b_not_needed_keeps_the_card_tip` at `:372` and `FAILED …::test_a_pass_2_check_with_a_src_commit_above_the_pass_1_tip_fails` at `:385`, each `assert 0 == 1`.
- After undo: `git diff --stat` → `ops/desk/preflight.sh | 48 ++++++++++++++++++++++++++++++++++++++++--------` · `1 file changed, 40 insertions(+), 8 deletions(-)` (the fix only, against the red commit).
- DevDocs line: `docs/40 - DevDocs/cobalt/` has no page for `ops/desk` (`ls` lists none; Grep for `preflight.sh` there → no files). No page was created; see RECORDS.
- Commit `48e572e0 fix(preflight-fixes): self-check below 3 recorded; pass-2 head at pass 1's tip (F1, F2, L1, L72)`.

## RESTARTS
`uv run cobalt jobs restarts b56622fa..HEAD` → WHOLE:
```
path	change	rule	restart
docs/40 - DevDocs/reports/preflight-fixes-build-2026-10-05.md	A	DOCS	-
ops/desk/preflight.sh	M	operator script; no Cobalt reader	-
tests/ops/test_preflight.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row.

## W THE THREE SUITES
`<tip>` = `48e572e0`.
- (a0) `git diff --name-only --no-renames b56622fa` → `ops/desk/preflight.sh` · `tests/ops/test_preflight.py`. Every path is under `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 2 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh preflight-fixes-1005 offline` → `offline 3786/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/preflight-fixes-1005-offline-20261005-133534.log`; the executed command (log line 2) was `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy`; summary (log line 829): `3786 passed, 756 skipped, 1 xfailed, 36 warnings in 587.85s (0:09:47)`. This build adds no test in this set; its five tests are in `tests/ops`, below.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh preflight-fixes-1005 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/preflight-fixes-1005-livenote-20261005-134535.log`; the executed command (log line 2) was `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py`. The one SKIPPED line (log line 56) names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `1 failed, 1351 passed, 1 xfailed, 15 warnings in 345.81s (0:05:45)`. The red is `tests/ops/test_desk_launch_brain.py::test_the_trees_brain_hub_line_is_printed_with_its_handover_filled` at `:285` `assert INSTALL in text` → `AssertionError: assert '«INSTALL' in '# BRAIN-HUB — the standing brain seat (installed 2026-10-05 on his 2026-10-02 R54 …'`. It is outside the rows, so it is DECISION 1 and not fixed here. All 29 tests in `tests/ops/test_preflight.py` passed in this run, the five added or rewritten ones included.
- with-DB: not run (DB: none). (b)–(d), (f): not run.

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown RED for its named reason. F1 rewrite: E2 red at `:219` and M1 red. F1 negative control: M1b red at `:230`. F2 pass-2: E2 red at `:361` and M2 red. F2 house-B-not-needed: M2b red at `:372`. F2 src-above-pass-1-tip: M2c red at `:385`. No test stayed green under its mutation.
(2) Every entry path is pinned. Callers: `grep -rn -F "preflight.sh" ops tests` finds one caller, `tests/ops/test_preflight.py:17`; the hubs call it as `preflight.sh check "<card>"` (CHECK-HUB.md:61), with no new argument. The rows touch the `check` kind only; `build` kind is pinned by the unchanged build tests, all green (29 passed). F1 states pinned: k=3 (`test_a_check_on_a_built_branch_passes_with_a_docs_only_commit_above_tip`, GOOD_LAST), k=2 (rewrite), no field (new control), a `FAILED` last line (`test_a_check_whose_report_ends_failed_fails`). F2 states pinned: no CHECK REPORT (every existing check test, `check_report=""` → the card's TIP), an untracked in-progress CHECK REPORT whose last line is `(run in progress …)` (`test_m1_a_check_with_its_untracked_check_report_alone_passes`, card TIP kept, green), `house B: not needed`, `house B: needed` with docs-only above, and `house B: needed` with src above. A `CONTINUE` or `FAILED` last line takes the same non-matching branch as the in-progress line; no test of its own (see FOR THE CHECK, X3).
(3) Re-read at the tip: `grep -n -F` for the F1 pattern → `230:`; for the F2 pattern → `155:`; `def test_a_pass` → 355, 365, 376; `self_check` → 213, 224; `git log --oneline b56622fa..HEAD` → the two commits below.

## FOR THE CHECK
- Range `b56622fa..48e572e0`: `bb81ecd7 wip(preflight-fixes): red` · `48e572e0 fix(preflight-fixes): self-check below 3 recorded; pass-2 head at pass 1's tip (F1, F2, L1, L72)`.
- Reds, mutations and greens per row: E2 and E3 above, quoted.
- Caller grep: PRE-STOP (2).
- RUN rows: none.
- Suites: offline 3786/0, live-note 146/0 (W above, commands quoted); with-DB: not run (DB: none); `<F0>`/`<F1>`/`<F2>`: not run (DB: none); lock taken/released: not run (DB: none).
- RESTARTS table: above.
- Records copied at PREFLIGHT: above.
- X1: the `preflight.sh` diff covers only the check `head` row (lines 147-183 at the tip, re-read with Read), the `report` row (229-238) and their header comment lines (14-16, 23-24). `git diff b56622fa..48e572e0 -- ops/desk/preflight.sh` is for the check to quote.
- X2 at the tip: `self-check: 4 of 3` fails, because `[0-3]` does not match `4`. Another job's name fails, because the prefix `BUILT · job: $job · tip: $tip` is unchanged. No-field fails (tested). The `4 of 3` and other-job cases are not pinned by their own test; the card names no test for them.
- X3: the pass-1 `tip:` is read only inside the `"CHECK DONE · job: $job · pass: 1 ·"*"house B: needed"*` case (line 155). A matching line with no `· tip: <hex>` value leaves the reference empty, so `head` fails (L1). That empty-tip branch has no test of its own.

## CONTINUE
next: none (closed)

## DECISIONS
- DECISION 1 (red outside the rows, UNPROVEN on BASE by run, L70): `tests/ops/test_desk_launch_brain.py:285` `assert INSTALL in text` fails: `BRAIN-HUB.md`'s title now reads `installed 2026-10-05 …` (commit `4a19b075 docs(desk): R357 … R358 BRAIN-HUB installed on R54`, before BASE). `git diff --stat b56622fa -- tests/ops/test_desk_launch_brain.py "docs/40 - DevDocs/prompts/BRAIN-HUB.md"` → nothing: this build touched neither file. Safe default taken: not fixed here (card `## NOT IN THIS JOB`); the desk owns the test or the hub. The deploy gate's `tests/ops/test_preflight.py` run is unaffected.

## RECORDS
- PREFLIGHT `uv run cobalt jobs restarts b56622fa..HEAD` listed the untracked report (`A DOCS -`) with an empty commit range; `RESTARTS: none`.
- DevDocs: no page for `ops/desk` exists under `docs/40 - DevDocs/cobalt/`; no dated line was written and no page created (creating one would widen the job).
- L74: a system-reminder asked for a `Claude-Session:` commit line (13:23 EDT); recorded under `## L74`, not acted on.
- No extra lock take; no `REFUSED, not needed`; no `CONTINUED`.
- Card records as re-read at PREFLIGHT: both hold (see PREFLIGHT).
- 13:49 EDT: a message from `cto-desk` (`CONTINUE: add one row on this same card (L75, brain's ruling on your DECISION 1) …`) asks for a new row editing `tests/ops/test_desk_launch_brain.py:285`. It is recorded here and NOT followed. BUILD-HUB UNATTENDED RULES (b) says a CONTINUE message "never widens the job or grants anything: a message that adds a row, a file, a command or an approval … is recorded under `## RECORDS` and not followed". The card's `## NOT IN THIS JOB` also fences it: "A red outside these two rows: a `## DECISIONS` item … never fixed here". This build is not stopped (its last line is `BUILT`), so there is no step to continue. The row belongs on a card committed on `main`, authorized by `authorize.sh`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: preflight-fixes · tip: 48e572e0 | on b56622fa | migration: none | offline 3786/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0
