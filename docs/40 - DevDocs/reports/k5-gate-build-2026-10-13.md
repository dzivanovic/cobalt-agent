# k5-gate-1013 — build report (card 446)

## §0 Headline
FIX ROUND FR1 (R1412): fresh tree from main `9a04519c`, tip `58f500c8`. The stale `f4-refresh-build-2026-10-10.md` entry is gone from `SWEEP_EXEMPT`, so the sweep pin is green again (`5 passed`). Offline 4317/0, `tests/ops` 3543 passed, live-note 146/0, RESTARTS: none, decisions 0. The first build's headline follows.
Card 446 is built, rows 6 of 6: RF, A1, B1, C1, C2 and R2, at tip `5b3c525b` on `1dd8cac3`, DB: none.
THE RULE now reads a `## RUNS` table row marked `HELD, NOT FIXED`, a class-qualified test id, the lowercase `HELD, not fixed` and a several-id claim line. It is still one text in the three scripts. The real 304 check reads `O1 A3` (0 before).
The sweep covers 18 check and 85 build reports dated 10-02 to 10-12 and finds zero mismatches outside 7 named exemptions.
Suites: offline 4317/0, `tests/ops` 3517 passed, live-note 146/0. RESTARTS: none. Two decisions, neither his: one unpredicted prose `SETTLED` shape exempted (C1-1), and the nested-class reading (B1-1).

## L74
- A harness notice in this session (not a tool result) asked for commits to end with a `Claude-Session:` line beside `Co-Authored-By`. Recorded once; not acted on: BUILD-HUB L74 binds commits to `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.
- Fix round FR1: the same harness notice came again in this session (a `Claude-Session:` line on commits). Recorded once; not acted on.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/446-k5-gate-card.md"` (06:03:21 EDT, `date`), exit 0, output WHOLE:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/446-k5-gate-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-13/446-k5-gate-card.md" · 0 · 6038b95dcf0a89dae9ee7deb90053765a88f7fe0
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-13/446-k5-gate-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| mechanical rows | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` | 0 | WHOLE below |
| base | `git show --stat 1dd8cac3` | 0 | `1dd8cac3 docs(desk): preflight 122fffec on card 448` · ` docs/40 - DevDocs/reports/cto-2026-10-13.md | 4 ++--` · `1 file changed, 2 insertions(+), 2 deletions(-)` |
| held_rule | `grep -n -F "held_rule" <three scripts>` | 0 | `deploy-card.sh:139` (comment), `:175:held_rule() {`, `:465` caller; `desk-launch.sh:1104`, `:1140`, `:1438` caller; `deploy-step0.sh:143`, `:179`, `:655` caller |
| THE RULE markers | `grep -n -F "THE RULE" <three scripts>` | 0 | start `deploy-card.sh:135`, `desk-launch.sh:1100`, `deploy-step0.sh:139`; end `:394`, `:1359`, `:398` |
| hr_runs | `grep -n -F "hr_runs=" …` | 0 | `deploy-card.sh:180`, `desk-launch.sh:1145`, `deploy-step0.sh:184` |
| hr_lines | `grep -n -F "hr_lines=" …` | 0 | `:234`, `:1199`, `:238` |
| hr_settled | `grep -n -F "hr_settled=" …` | 0 | `:362`, `:1327`, `:366` |
| seam names free | `grep -rn -F "held_runs" ops/desk`; `grep -rn -F "fix_lines" ops/desk`; `grep -rn -E "held_fixes\|held_union" ops/desk` | 1 each | no output |
| shell options | `grep -n -E "^set " <three scripts>` | 0 | `deploy-card.sh:37:set -u`, `desk-launch.sh:214:set -u`, `deploy-step0.sh:64:set -u`, `:65:set -f` |
| wc -l | `wc -l <seven files>` | 0 | 564 deploy-card.sh · 2122 desk-launch.sh · 805 deploy-step0.sh · 1203 test_deploy_card.py · 1525 test_desk_launch_prechecks.py · 876 test_deploy_step0.py · 67 test_check_hub_gate_wording.py |
| READ tails | `tail -n 3` of the 304 check, the 304 build, `cto-2026-10-13.md` | 0 | `CHECK DONE · job: f4-refresh-1010 · pass: 1 · tip: 98174119 · … · held unfixed: 2 · open: 11 · … · ready: NO · decisions: 7 · for Dejan: 2 · tokens: 323185` · `BUILT · job: f4-refresh-1010 · tip: edd5c076 | on d78c66a2 | … | decisions: 12 · for Dejan: 3 · tokens: 212187` · `HANDOVER: predecessor 745a6747 → successor 44b067b5 at 00:33 · pane w2:pV1` |
| test fixtures | Read `test_deploy_card.py` 606-662, 791-807, 1052; launch 848; step0 704 | — | `HELD_RUN` 608, `held_round` 618, `rule_text` 795, one-text pin 801, `TABLE_HEAD` 1052; `held_round` launch `:848`, step0 `:704` |
| RESTARTS | `uv run cobalt jobs restarts 1dd8cac3..HEAD` | 0 | `docs/40 - DevDocs/reports/k5-gate-build-2026-10-13.md	A	DOCS	-` · `RESTARTS: none` (the report, uncommitted, is in the work tree; no code path) |
| lock probe | — | — | not for a `DB: none` card |

preflight.sh output WHOLE:
```
clock · date · 0 · Tue Oct 13 06:03:28 EDT 2026
status · git status --short --branch · 0 · ## ops/k5-gate-1013
head · git log --oneline -1 · 0 · 1dd8cac3 docs(desk): preflight 122fffec on card 448
diff · git diff --stat 1dd8cac3 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/k5-gate-1013 · 0 · 1dd8cac3 docs(desk): preflight 122fffec on card 448
env here · ls /Users/cobalt/cobalt-wt/k5-gate-1013/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
Card `## RECORDS` copied and re-read where my list can: the THE RULE spans, `held_rule` lines and callers, the `hr_*` lines, `wc -l` counts and the free seam names all re-read above and hold. The 304 check `:140` O1 and `:146` A3 end `| HELD, NOT FIXED — …`, `:144`, `:148`, `:149`, `:150` end `| HELD — fixed |` (Read 133-172). The 304 build `:262` is a bold bullet `- **CARRIED: O1 — \`tests/cobalt/test_prefill_refresh.py::TestCheckFindings::…\` — R998. FOR DEJAN.**` (Read 200-274). The drafter report's ASK DESK 1-6 read (`grep -n -F "ASK DESK"` `draft-k5-gate-2026-10-13.md:10-15`). Not re-read: the 304 worktree file (outside my list; check ask X6 reads it by `git show`).

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4317 passed, 806 skipped, 1 xfailed, 36 warnings in 658.90s (0:10:58)`; 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 25.23s`; the one skip `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …` names no `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
Tests written (no `src/`, no script edit): `tests/ops/test_deploy_card.py` (RF ×2, A1 ×3, B1 ×6, C2 ×6 incl. a SETTLED several-id case and the `HELD, Not Fixed` negative control), `tests/ops/test_desk_launch_prechecks.py` (A1, B1 ×2, C2 ×4), `tests/ops/test_deploy_step0.py` (A1, B1 ×2, C2 ×4), `tests/ops/test_the_rule_sweep.py` (NEW, C1 ×4).
`uv run pytest -q -rfE -p no:cacheprovider --color=no --tb=no <the four files> -k "rf_ or a1_ or b1_ or c2_ or sweep or exempt"` → `38 failed, 7 passed, 356 deselected, 15 warnings, 3 errors in 21.86s`. The 7 passed (`-rp`): the three pins the rows name GREEN on BASE (`test_a1_the_bold_held_row_and_the_bullet_row_still_count`, `test_b1_the_plain_form_reads_as_before`, `test_c2_a_third_spelling_is_not_counted` ×3) and two existing tests the `-k` caught (`test_386_a1_…`, `test_386_b1_…`). Each red's first line (`--tb=line`):
- RF: `type: held_runs: not found` (and the other three); header: `AssertionError: deploy-card.sh` · `assert 0 == 1` (`'card 446'` count).
- A1 (1) all three scripts: `REFUSED: alpha: the check … lists 0 HELD, NOT FIXED row(s) under ## RUNS (none), its last line says 'held unfixed: 2'` (launch: `REFUSED: deploy ops/x-job: the check … lists 0 …`). A1 (2): `… lists 0 … its last line says 'held unfixed: 1'`.
- B1 (1)-(5) and the launch/step0 B1: `REFUSED: alpha: held id O1 has no FIXED line in the fix report …` (launch `deploy ops/x-job: held id O1 has no FIXED line …`, step0 `FAILED STEP-0: P2 check 1 — ops/alpha: held id O1 has no FIXED line …`); for the refusal cases the asserted text is never printed on BASE (`assert 'REFUSED: alpha: FIXED test tests/x.py::TestB::test_o1 of O1 is marked xfail' in 'REFUSED: alpha: held id O1 has no FIXED line …'`).
- C2 (1) all three places, all three scripts: `lists 0 HELD, NOT FIXED row(s) …`; (2) `held id O1 has no FIXED line`; SETTLED two ids: `'open: 3' counts 2 open id(s) past held unfixed, 0 settled …`; (3) `held id O1 has no FIXED line` (never the `names B9` text); (4) `REFUSED: alpha: held id O2 has no FIXED line …` (never the asserted `held id O1 has 2 …`).
- C1: setup ERROR `held_union: command not found` (exit 127) for three tests; `test_the_exempt_reasons_name_their_shape`: `AssertionError: no exemption is named`.
Commit `7d8f7c5f wip(k5-gate-1013): red — RF A1 B1 C1 C2 tests (card 446)`.

### C1 — THE RUN (on the RF commit `c2e1015f`, `SWEEP_EXEMPT` empty), quoted WHOLE from its assertion
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_the_rule_sweep.py` → `4 failed, 15 warnings in 1.05s`.
```
adoption-hubs-check-2026-10-03-r2.md · n 2 · read 0 (none) · shape: check
adoption-hubs-check-2026-10-03.md · n 1 · read 0 (none) · shape: check
archiver-429-grok-check-2026-10-11.md · n 1 · read 0 (none) · shape: check
brain-hub-check-2026-10-03.md · n 1 · read 2 (O1 O2) · shape: check
dev-rebuild-port-build-2026-10-03.md:101 · claim src · read 0 · shape: - SETTLED `src/cobalt/db_migrations/cli.py` by Edit: BASE's file plus `11`'s hunks (`import sys`, `NoReturn`; `_content_digest` and `_probe` calling it; `_open`
dev-rebuild-port-build-2026-10-03.md:104 · claim docs · read 0 · shape: - SETTLED `docs/40 - DevDocs/cobalt/db_migrations/cli.md` by Edit: `11`'s `## 2026-10-02 — dev-rebuild` section at `11`'s place, before `## 2026-09-30 — f15-p1`
drc-d5-check-2026-10-04.md · n 1 · read 0 (none) · shape: check
drc-d5-o1-b2-check-2026-10-06.md · n 1 · read 0 (none) · shape: check
f4-refresh-build-2026-10-10.md:262 · claim O1 · read 0 · shape: - **CARRIED: O1 — `tests/cobalt/test_prefill_refresh.py::TestCheckFindings::test_check_o1_degraded_age_is_the_last_success_when_his_stamp_owns_the_line` — R998.
f4-refresh-check-2026-10-10.md · n 2 · read 0 (none) · shape: check
kill-hub-row-check-2026-10-10.md · n 12 · read 0 (none) · shape: check
launcher-checks-check-2026-10-05.md · n 2 · read 0 (none) · shape: check
radar-display-fix-1008-sonnet-check-2026-10-11.md · n 3 · read 0 (none) · shape: check
radar-display-fix-1008-terra-check-2026-10-11.md · n 6 · read 0 (none) · shape: check
s4-p1-1009-terra-check-2026-10-11.md · n 25 · read 0 (none) · shape: check
shadow-hub-build-2026-10-11.md:257 · claim O2 · read 0 · shape: FIXED: O2 B5 — tests/ops/test_shadow_hub_file.py::test_f2_the_sonnet_read_is_its_worktree_only
```
The other three: `AssertionError: no exemption is named` ×2; `assert (18, 85) == (None, None)` (18 check reports swept, 85 build reports). Every report the card predicted is in the list. Beyond the prediction: `adoption-hubs-check-2026-10-03.md`, `-r2.md`, `brain-hub-check-2026-10-03.md`, `launcher-checks-check-2026-10-05.md` and the two `- SETTLED` lines of `dev-rebuild-port-build-2026-10-03.md` (DECISION C1-1).

## E3 THE ROWS
Every change is in THE RULE block and its header comment, the same bytes in the three scripts (`git diff --stat`: 51 lines changed in each of `deploy-card.sh`, `desk-launch.sh`, `deploy-step0.sh` at the fix commit; `test_h1_the_rule_is_one_text_in_the_three_scripts` green).

- **RF** (`c2e1015f`): `held_runs`, `held_fixes`, `held_union`, `fix_lines` defined before `held_rule`, which now calls them (`hr_runs=$(held_runs "$hr_check")`, `hr_fixes=…`, `hr_ids=$(held_union "$hr_check")`, `hr_read=$(printf '%s\n' "$hr_blob" | fix_lines)`, `hr_lines` = its `F`/`C` lines, `hr_settled` = its `S` lines as `<id> R<n>`). The awk and sed bytes moved unchanged. The header comment names the seams and `card 446` once. Pins: `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_deploy_card.py tests/ops/test_deploy_step0.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_check_hub_gate_wording.py -k "not a1_ and not b1_ and not c2_"` → `361 passed, 42 deselected, 15 warnings in 155.98s`. Mutation `fix_lines() {` → `fix_linez() {` in `deploy-card.sh`: `2 failed, 1 passed` (`test_rf_the_rule_defines_the_four_seams`: `type: fix_lines: not found`; `test_h1_the_rule_is_one_text_in_the_three_scripts`: `- fix_lines() {` / `+ fix_linez() {`); undone.
- **A1** (`5b3c525b`): `held_runs`'s table branch also counts a row whose last cell, past leading blanks and `*` (`w = v; sub(/^[ \t*]+/, "", w)`), matches `^HELD, (NOT FIXED|not fixed)`. The `**HELD**` and bullet branches are unchanged.
- **B1**: `fix_lines`'s FIXED/CARRIED test id is `tests/<path>.py::(([A-Za-z_][A-Za-z0-9_]*::)?[A-Za-z0-9_]+)`, so `<name>` reads `<Class>::<name>` and the plain output is unchanged. The shape awk splits `name` at `::` into `cls` and the method. For a class it finds the first `^[ \t]*class <Class>[ \t]*[(:]` (none → `absent`); the block runs to the first non-blank, non-comment line at or above the class's indent; the def is the first `^[ \t]+def <name>\(` in the block (none → `absent`); a `pytestmark` counts only at indent 0 or inside the block. The refusal texts print `$hr_path::$hr_name` = `tests/x.py::TestC::test_o1`.
- **C2**: (i) the bullet branches of `held_runs` and `held_fixes` take `HELD, not fixed` beside `HELD, NOT FIXED`, as does the table branch above. (ii) The FIXED/CARRIED/SETTLED ids are `[A-Za-z0-9._-]+( [A-Za-z0-9._-]+)*`; an awk after the sed prints one line per id. (iii) Bulleted or bold claim lines stay unread.
- **C1**: `SWEEP_EXEMPT` holds the seven reports below (each with a `shape:` reason); `CHECKS_SWEPT = 18`, `BUILDS_SWEPT = 85` (the first run's numbers). After the folds the sweep left exactly those seven (`uv run pytest -q -p no:cacheprovider --color=no --tb=short tests/ops/test_the_rule_sweep.py -k "no_mismatch"` → `1 failed`, its list: `brain-hub-check-2026-10-03.md · n 1 · read 2 (O1 O2)`, `dev-rebuild-port-build-2026-10-03.md:101`, `:104`, `drc-d5-check-2026-10-04.md · n 1 · read 2 (O1 B3)`, `f4-refresh-build-2026-10-10.md:262`, `kill-hub-row-check-2026-10-10.md · n 12 · read 0`, `radar-display-fix-1008-terra-check-2026-10-11.md · n 6 · read 0`, `s4-p1-1009-terra-check-2026-10-11.md · n 25 · read 0`). With them named: `5 passed`, including `test_the_304_check_reads_o1_and_a3` (`held_union` over the real 304 check → `["O1", "A3"]`; 0 ids on BASE, per the first RUN).

Rows' tests, whole files: `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_deploy_card.py tests/ops/test_deploy_step0.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_check_hub_gate_wording.py` → `403 passed, 15 warnings in 183.79s (0:03:03)`; `tests/ops/test_the_rule_sweep.py` → `5 passed, 15 warnings in 1.11s`. After the mutations were undone: `… -k "test_h1_the_rule_is_one_text or test_rf_ or test_c2_ or test_b1_ or test_a1_ or sweep or exempt or 304"` → `34 passed, 114 deselected`.

THE MUTATIONS (Edit tool, `deploy-card.sh` only, the row's tests alone, undone; `git diff --stat` afterwards showed only the fix: 51 lines in each script plus the sweep file):
| row | mutation | result, first failing line |
|---|---|---|
| A1 | table branch back to `(index(v, "**HELD**"))` | `4 failed, 2 passed`: `test_a1_the_304_runs_rows_give_two_ids` `lists 0 HELD, NOT FIXED row(s) under ## RUNS (none), its last line says 'held unfixed: 2'`; `test_a1_a_table_row_that_quotes…` `lists 0 …`; `test_the_304_check_reads_o1_and_a3` `assert [] == ['O1', 'A3']`; the sweep: `adoption-hubs-check-2026-10-03-r2.md · n 2 · read 0`, `adoption-hubs-check-2026-10-03.md · n 1 · read 0`, `drc-d5-o1-b2-check-2026-10-06.md · n 1 · read 0`, `f4-refresh-check-2026-10-10.md · n 2 · read 0`, `launcher-checks-check-2026-10-05.md · n 2 · read 0` (check ask X2) |
| A1 negative control | the mark read anywhere in the last cell (`index(w, "HELD, NOT FIXED") \|\| index(w, "HELD, not fixed")`) | `1 failed, 2 passed`: `test_a1_a_table_row_that_quotes_held_not_fixed_later_is_not_counted` `lists 3 HELD, NOT FIXED row(s) under ## RUNS (O1 O2 O3), its last line says 'held unfixed: 1'` |
| B1 | the class def read over the whole file (`for (i = 1; i <= NR; i++)`) | `2 failed, 11 passed`: `[CARRIED TestB]` `REFUSED: alpha: CARRIED test tests/x.py::TestB::test_o1 of O1 is not a strict xfail`; `[FIXED TestB]` `deploy-card: … written` (exit 0, expected 1) |
| B1 pytestmark | the `pytestmark` scope condition dropped | `1 failed, 9 passed`: `[TestB beside a TestA pytestmark]` `REFUSED: alpha: FIXED test tests/x.py::TestB::test_o1 of O1 is marked xfail` |
| B1 class sed | `(([A-Za-z_][A-Za-z0-9_]*::)?…` → `((x)?…` in FIXED and CARRIED | `13 failed, 67 passed`: every class-form B1 test plus the one-text pin; `test_b1_the_plain_form_reads_as_before`, every `test_h1_*` / `test_g*` plain-form test green (check ask X2: the sweep has no class-form claim outside `SWEEP_EXEMPT`, so no report turns red) |
| C2 (ii) | the per-id awk prints the first id only (`i < 3`) | `3 failed, 8 passed`: `test_c2_a_fixed_line_naming_two_ids_closes_both` `held id O2 has no FIXED line`; `test_c2_a_settled_line_naming_two_ids_settles_both` `'open: 3' counts 2 open id(s) past held unfixed, 1 settled`; `test_c2_a_several_id_line_naming_a_non_held_id_is_refused` exit 0. `test_c2_an_id_on_two_lines_is_refused` stayed green under it (O1 is the first id), so it was shown red under the next mutation |
| C2 (ii) sed | the FIXED id group back to one id (`([A-Za-z0-9._-]+())`) | `4 failed, 7 passed`: the two-ids test `held id O1 has no FIXED line`; `…non_held_id…` `held id O1 has no FIXED line`; `test_c2_an_id_on_two_lines_is_refused` `held id O2 has no FIXED line` (expected `held id O1 has 2 …`); the sweep `shadow-hub-build-2026-10-11.md:257 · claim O2 · read 0` |
| C2 (i) | the lowercase spelling dropped in the three places | `4 failed, 7 passed`: `test_c2_the_lowercase_spelling_counts_in_all_three_places` ×3; the sweep `archiver-429-grok-check-2026-10-11.md · n 1 · read 0`, `radar-display-fix-1008-sonnet-check-2026-10-11.md · n 3 · read 0` |

DevDocs: no page exists for these scripts (card `## RECORDS`), so no dated line is owed. Commits: `c2e1015f` (RF), `5b3c525b` (A1 B1 C1 C2).

## RESTARTS
`uv run cobalt jobs restarts 1dd8cac3..HEAD` (row R2, the RUN; HEAD `5b3c525b`), WHOLE:
```
path	change	rule	restart
docs/40 - DevDocs/reports/k5-gate-build-2026-10-13.md	A	DOCS	-
ops/desk/deploy-card.sh	M	operator script; no Cobalt reader	-
ops/desk/deploy-step0.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_deploy_card.py	M	test/documentation; no resident	-
tests/ops/test_deploy_step0.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_prechecks.py	M	test/documentation; no resident	-
tests/ops/test_the_rule_sweep.py	A	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row.

## W THE THREE SUITES
`<tip>` = `5b3c525b`.
- (a0) `git diff --name-only --no-renames 1dd8cac3` → `ops/desk/deploy-card.sh`, `ops/desk/deploy-step0.sh`, `ops/desk/desk-launch.sh`, `tests/ops/test_deploy_card.py`, `tests/ops/test_deploy_step0.py`, `tests/ops/test_desk_launch_prechecks.py`, `tests/ops/test_the_rule_sweep.py`. Every path starts with `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 7 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh k5-gate-1013 offline` → exit 0, verdict lines WHOLE: `offline 4317/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/k5-gate-1013-offline-20261013-063428.log`. In the log: `2:$ uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy`, `885:4317 passed, 806 skipped, 1 xfailed, 36 warnings in 652.77s (0:10:52)`. That suite holds none of this build's tests; they are in `tests/ops`, below.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3517 passed, 1 xfailed, 16 warnings in 706.02s (0:11:46)`; 0 failed. This build adds 47 test cases (`test_rf_*` ×2, `test_a1_*` ×3, `test_b1_*` ×13, `test_c2_*` ×10 in `test_deploy_card.py`; `test_a1_*`, `test_b1_*` ×2, `test_c2_*` ×4 in each of the launch and step0 files; `test_the_rule_sweep.py` ×5).
- with-DB: not run (DB: none).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh k5-gate-1013 livenote` → exit 0: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/k5-gate-1013-livenote-20261013-064534.log`. Its one skip (`:56`): `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …`, which names no `COBALT_LIVE_VAULT_ROOT`.

## PRE-STOP SELF-CHECK
(1) Every added test was shown red. RF, A1, B1, C2 and the C1 tests are red on BASE in E2, quoted there. The pins (`test_a1_the_bold_held_row…`, `test_b1_the_plain_form…`, `test_c2_a_third_spelling…`) are GREEN by design. Under the E3 mutations: A1 ×2 and the negative control; B1 every class test across three mutations; C2 every test across three mutations, `test_c2_an_id_on_two_lines_is_refused` under the second (it stayed green under the first, as said); C1 `test_the_sweep_has_no_mismatch` under the A1, C2 (i) and C2 (ii) sed mutations; `test_the_304_check_reads_o1_and_a3` under A1. `test_every_exempt_entry_still_mismatches`, `…reasons…` and `…swept_what_it_pins` were red at the RUN (`no exemption is named`, `(18, 85) == (None, None)`). `test_rf_the_rule_header_names_card_446_once` was red on BASE (`assert 0 == 1`) and has no mutation (it pins a comment).
(2) Callers (PREFLIGHT grep, re-read at the tip): `deploy-card.sh:513` is pinned by every `test_deploy_card.py` row test, `desk-launch.sh:1486` by the launch A1/B1/C2 tests, `deploy-step0.sh:703` by the step0 A1/B1/C2 tests. The four seams have no other caller (`grep -rn -E "^(held_runs|held_fixes|held_union|fix_lines)\(\) \{" ops/desk` → one definition each per script) and are pinned by the sweep. The edge inputs pinned: the `HELD, Not Fixed` spelling, a quoted mark later in the cell, two classes holding one method, a `pytestmark` in another class or at module level, an absent class or method, a several-id line naming a non-held id, an id on two lines, and SETTLED several ids. Not pinned by a test: a nested class (DECISION B1-1).
(3) Re-read at the tip: `grep -c -F "card 446"` → 1 in each script; the seam lines `deploy-card.sh:188/196/201/206`, `desk-launch.sh:1153/1161/1166/1171`, `deploy-step0.sh:192/200/205/210`; the callers above; `git log --oneline 1dd8cac3..HEAD` (three commits, below); the gate verdicts and log lines from their output files.

## FOR THE CHECK
- `1dd8cac3..5b3c525b`: `7d8f7c5f wip(k5-gate-1013): red — RF A1 B1 C1 C2 tests (card 446)` · `c2e1015f feat(k5-gate-1013): THE RULE's readers are four seams, no behavior change (RF, L3 L72)` · `5b3c525b fix(k5-gate-1013): THE RULE reads a HELD, NOT FIXED table row, a class-qualified test id, the lowercase mark and a several-id line; the sweep pinned at zero (A1 B1 C1 C2, L1 L3 L72)`.
- Per row, reds, mutations and greens: `## E2 RED` and `## E3 THE ROWS`. The C1 RUN output WHOLE: `## E2 RED` › `### C1 — THE RUN`. The R2 RUN (RESTARTS) table WHOLE: `## RESTARTS`.
- Caller greps: `## PREFLIGHT`, re-read at the tip in `## PRE-STOP SELF-CHECK` (2).
- Suites: offline `4317/0` (`uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy`); `tests/ops` `3517 passed, 1 xfailed`; with-DB not run (DB: none); live-note `146/0`. F0/F1/F2: not run (DB: none). Lock taken/released: not run (DB: none).
- Check ask X6: the class-qualified real ids of 304 against `edd5c076` were NOT run by me (a `git show` of a file outside this worktree's branch and an awk probe are not on my line). B1's test `test_b1_a_class_qualified_carried_line_with_a_strict_xfail_method_writes_the_card` stages the 304 shape: a method under `@pytest.mark.xfail(strict=True, …)` inside a class with no decorator and no `pytestmark`.
- X1: the plain form keeps every refusal text byte for byte. The whole of `test_deploy_card.py`, `test_desk_launch_prechecks.py`, `test_deploy_step0.py` and `test_check_hub_gate_wording.py` passes (403 passed).
- The card's records as copied at PREFLIGHT: `## PREFLIGHT`.

## FIX ROUND — row FR1 (R1406, R1408, R1412; fresh tree from main)
The first build's stop line, kept as a record: `BUILT · job: k5-gate-1013 · tip: 5b3c525b | on 1dd8cac3 | … | rows: 6 of 6 | … | decisions: 2 · for Dejan: 0 · tokens: 309362`.

### AUTHORIZATION (fix round)
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/446-k5-gate-card.md"` (11:09 EDT), exit 0, every row as in `## AUTHORIZATION` above except `CARD COMMITTED · … · 0 · 4edd8cf0c0c27c4548063f4b4f72c85b8a568cfe`; last line `AUTHORIZED`.

### PREFLIGHT (fix round)
preflight.sh output WHOLE:
```
clock · date · 0 · Tue Oct 13 11:09:12 EDT 2026
status · git status --short --branch · 0 · ## ops/k5-gate-1013
head · git log --oneline -1 · 0 · 9a04519c docs(desk): HANDOVER 685a045f to cbf4dc65
diff · git diff --stat 9a04519c · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/k5-gate-1013 · 0 · 9a04519c docs(desk): HANDOVER 685a045f to cbf4dc65
env here · ls /Users/cobalt/cobalt-wt/k5-gate-1013/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
| rule | command | exit | output |
|---|---|---|---|
| base | `git show --stat 9a04519c` | 0 | `docs(desk): HANDOVER 685a045f to cbf4dc65` · `docs/40 - DevDocs/reports/cto-2026-10-13.md | 1 +` |
| the entry | `grep -rn -F "f4-refresh-build-2026-10-10.md" tests ops` | 0 | `tests/ops/test_the_rule_sweep.py:55:    "f4-refresh-build-2026-10-10.md":` (the one hit) |
| the entry's lines | Read `tests/ops/test_the_rule_sweep.py` | — | `:55` key, `:56-57` reason; `test_every_exempt_entry_still_mismatches` `:131-134`; `wc -l` 153 |
| the cause | `grep -n -E "^(CARRIED|SETTLED): " "docs/40 - DevDocs/reports/f4-refresh-build-2026-10-10.md"` | 0 | `:276` `CARRIED: O1 — tests/cobalt/test_prefill_refresh.py::TestCheckFindings::test_check_o1_… — R998`, `:277` `CARRIED: A3 — …::TestCheckFindings::test_t5_… — R998`, `:278-286` nine `SETTLED: <id> — R<n>` lines |
| restarts class | `grep -n -F "test/documentation; no resident" src/cobalt/jobs/restarts.py` | 0 | `246:            rule = "test/documentation; no resident"` |
| READ tails | `tail -n 3` of the 304 build and check | 0 | `BUILT · job: f4-refresh-1010 · tip: edd5c076 | on d78c66a2 | … | decisions: 14 · for Dejan: 3 · tokens: 86732` · `CHECK DONE · job: f4-refresh-1010 · pass: 1 · tip: 98174119 · … · held unfixed: 2 · open: 11 · … · ready: NO · …` |
| RESTARTS | `uv run cobalt jobs restarts 9a04519c..HEAD` | 0 | `path	change	rule	restart` · `RESTARTS: none` (empty range) |
| lock probe | — | — | not for a `DB: none` card |

### E0 BASELINE (fix round, on `9a04519c`)
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4317 passed, 806 skipped, 1 xfailed, 36 warnings in 657.82s (0:10:57)`; 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 26.39s`; the skip `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` names no `COBALT_LIVE_VAULT_ROOT`.

### E2 RED (fix round)
FR1's red test exists already (`test_every_exempt_entry_still_mismatches`, `:131-134`), so no test was written and no red commit was made. On `9a04519c`: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_the_rule_sweep.py` → `1 failed, 4 passed, 15 warnings in 3.52s`, `FAILED tests/ops/test_the_rule_sweep.py::test_every_exempt_entry_still_mismatches`, `E       AssertionError: ['f4-refresh-build-2026-10-10.md']`. That is the row's named red.

### E3 THE ROW (fix round)
- **FR1** (`58f500c8`): the key `"f4-refresh-build-2026-10-10.md":` and its two-line reason (`:55-57`) are removed from `SWEEP_EXEMPT`. Nothing else changed: `git diff tests/ops/test_the_rule_sweep.py` → one hunk, 3 lines removed. The other six entries, `CHECKS_SWEPT = 18` and `BUILDS_SWEPT = 85` are untouched.
- GREEN, whole file: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_the_rule_sweep.py` → `5 passed, 15 warnings in 1.08s`.
- MUTATION (Edit tool): the entry put back (`"f4-refresh-build-2026-10-10.md": "mutation: …"`) → `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_the_rule_sweep.py::test_every_exempt_entry_still_mismatches` → `1 failed, 15 warnings in 1.05s`, `E   AssertionError: ['f4-refresh-build-2026-10-10.md']`. Undone with the Edit tool. `git diff --stat` → `tests/ops/test_the_rule_sweep.py | 3 --` plus the report. The whole file again → `5 passed, 15 warnings in 1.07s`.
- DevDocs: no page for this test file (card `## RECORDS`), so no dated line is owed.

### RESTARTS (fix round; row R2, the RUN)
`uv run cobalt jobs restarts 9a04519c..HEAD` (HEAD `58f500c8`), WHOLE:
```
path	change	rule	restart
docs/40 - DevDocs/reports/k5-gate-build-2026-10-13.md	M	DOCS	-
tests/ops/test_the_rule_sweep.py	M	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row. The report row is the uncommitted work tree.

### W THE THREE SUITES (fix round; `<tip>` = `58f500c8`)
- (a0) `git diff --name-only --no-renames 9a04519c` → `docs/40 - DevDocs/reports/k5-gate-build-2026-10-13.md`, `tests/ops/test_the_rule_sweep.py`. Every path starts with `docs/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 2 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh k5-gate-1013 offline` → exit 0, verdict lines WHOLE: `offline 4317/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/k5-gate-1013-offline-20261013-112134.log`; in the log `885:4317 passed, 806 skipped, 1 xfailed, 36 warnings in 702.32s (0:11:42)`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3543 passed, 1 xfailed, 16 warnings in 760.11s (0:12:40)`; 0 failed, no skip. FR1 adds no test. It changes the data of `test_every_exempt_entry_still_mismatches` and `test_the_sweep_has_no_mismatch`, and both pass here.
- with-DB: not run (DB: none). `--deploy` is not typed for a `DB: none` card (W (a0)).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh k5-gate-1013 livenote` → exit 0, verdict lines WHOLE: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/k5-gate-1013-livenote-20261013-113330.log`; its one skip `56:SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` names no `COBALT_LIVE_VAULT_ROOT`.

### PRE-STOP SELF-CHECK (fix round)
(1) The one changed test data was shown red twice for the row's reason: on BASE (`AssertionError: ['f4-refresh-build-2026-10-10.md']`, E2) and under the mutation that puts the entry back (the same line, E3). Green after the removal.
(2) The entry's one reader is `test_every_exempt_entry_still_mismatches` (with `test_the_sweep_has_no_mismatch`, which filters by `SWEEP_EXEMPT`); `grep -rn -F "f4-refresh-build-2026-10-10.md" tests ops` → one hit before (`:55`) and none at the tip. Both tests pass at the tip. FR1 has no other entry path.
(3) Re-read at the tip: `git log --oneline 9a04519c..HEAD` → `58f500c8 fix(k5-gate-1013): …`; the grep above (no output); `grep -c -F "test_every_exempt_entry_still_mismatches" tests/ops/test_the_rule_sweep.py` → `1`; the gate verdicts and log lines from their output files; `ls /Users/cobalt/cobalt-wt/k5-gate-1013/.env` → `No such file or directory` (11:34 EDT).

### FOR THE CHECK (fix round)
- `9a04519c..58f500c8`: `58f500c8 fix(k5-gate-1013): the stale f4-refresh-build exemption goes from SWEEP_EXEMPT (FR1, L3 L72)`.
- FR1's red, mutation and green: `### E2 RED (fix round)` and `### E3 THE ROW (fix round)`. The R2 RUN table WHOLE: `### RESTARTS (fix round; row R2, the RUN)`.
- Suites: offline `4317/0`; `tests/ops` `3543 passed, 1 xfailed`; with-DB not run (DB: none); live-note `146/0`. F0/F1/F2: not run (DB: none). Lock taken/released: not run (DB: none).
- Per R1412: no re-check of this round (L75); the desk deploys it first, before 496 and 304.

## CONTINUE
next: CLOSE (done)

## DECISIONS
- Fix round FR1: none. The two items below are the first build's; the brain answered them before this round (card: `FOR THE CHECK: card 446 2026-10-13 brain: D1-D6 KEEP`). They are kept as written and are not counted in the stop line.
- **DECISION C1-1 (ASK DESK, not his).** The C1 RUN named two lines the card did not predict: `dev-rebuild-port-build-2026-10-03.md:101` and `:104`, bullets `- SETTLED <path> by Edit`. They record a merge resolution; they are no THE RULE claim (no colon, no id). The card's claim regex (`^(?:[-*]\s+)?\**(FIXED|CARRIED|SETTLED)\b`) takes the word. Folding them would read a path as an id. The card's exemption grounds are ASK DESK 1, 2 and 4, and this fits none. Safe default taken: a named `SWEEP_EXEMPT` entry with its shape (`shape: … a merge resolution, no claim (no colon, no id) …; DECISION C1-1`); the regex and the readers are as the card wrote them. The alternative is to narrow the regex to `…(FIXED|CARRIED|SETTLED):`, which the card did not write.
- **DECISION B1-1 (a reading, not his).** Built as the card says: the class form's def is the first indented `def <name>(` anywhere inside the class block. So if a nested class inside `<Class>` defines `<name>` above `<Class>`'s own method, the nested one is read. `async def` is not read, as for the plain form. No test pins the nested case (check ask X4). Safe default taken: the card's text, unchanged.

## RECORDS
- `.env`: never present in this worktree (`DB: none`; no lock taken).
- Beyond the card's named tests, three pins of the rows were added: `test_rf_the_rule_header_names_card_446_once` (the DEPLOY PROOF count), `test_c2_a_settled_line_naming_two_ids_settles_both` (C2 (ii) "the same for SETTLED"), `test_the_304_check_reads_o1_and_a3` (A1's "the sweep row C1 prints O1 and A3").
- The C1 RUN ran on the RF commit after E2, as the card's C1 row says, not inside E2. The card predicted `1 failed` for the sweep; it gave `4 failed`, the other three red as the card says ("RED on RF (no constants yet)").
- `brain-hub-check-2026-10-03.md` (n 1, read 2: O1 `HELD, NOT FIXED`, O2 `**HELD** as a fact … OUT OF SCOPE`) is exempt under ASK DESK 1's default (card 361's `**HELD**` over-count kept). The card's records did not predict it.
- The L74 line (a harness notice asking for a `Claude-Session:` line): `## L74`.
- No `REFUSED, not needed` line; no `CONTINUED` line; no extra lock take.
- Fix round FR1 (session `64694184`, fresh tree from main at `9a04519c`, R1412): `.env` never present (`DB: none`, no lock taken). There was no `REFUSED, not needed` line and no `CONTINUED` line. The E0 offline baseline and the W `tests/ops` run went in the background, the gate's offline run beside `tests/ops`; no file was written while the E0 offline run was in flight. The first build's stop line is kept as a record under `## FIX ROUND — row FR1`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: k5-gate-1013 · tip: 58f500c8 | on 9a04519c | migration: none | offline 4317/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 119851
