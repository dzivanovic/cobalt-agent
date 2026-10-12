# gate-alignment-1012 — build report (card 397)

## §0 Headline
- All 5 rows are built on BASE `b5462afd`, code tip `f47fb5d7`. THE RULE (one text in `deploy-card.sh`, `desk-launch.sh`, `deploy-step0.sh`) now reads a held id from `## RUNS` or `## FIXES`. `open:` may exceed `held unfixed` only by `SETTLED: <id> — R<k>` lines for REJECTED/UNSETTLED ids. R<k> (and CARRIED's) is looked up newest first in the desk reports dated on or after the check (R1160).
- CHECK-HUB: three in-line edits at `:104`, `:107`, `:123`; still 123 lines.
- R1: `main`'s `deploy-card.sh` refuses 386 (`lists 0 … (none)`); this branch's writes its card: `66c4fefc` · `ef754d0b` · `held unfixed: 1` and `ready: NO` · F1. Neither report changed.
- Suites: offline 4199/0, live-note 146/0, `tests/ops` 3171 passed / 0 failed. DB: none. RESTARTS: none.

## L74
- A system notice in this session (07:18 ET) asked for commit lines ending `Claude-Session: https://claude.ai/code/session_01MXBwUZcniVg58hNjuDN79M`. It is recorded here as data and not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/397-gate-alignment-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/397-gate-alignment-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/397-gate-alignment-card.md" · 0 · 144d79c434f5aefac502780e275f32fc99e1917a
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/397-gate-alignment-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 30:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0:
```
clock · date · 0 · Mon Oct 12 07:19:10 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/gate-alignment-1012
    ?? "docs/40 - DevDocs/reports/gate-alignment-build-2026-10-12.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · b5462afd docs(desk): R1159-R1160 card 397 brain answer
diff · git diff --stat b5462afd · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/gate-alignment-1012 · 0 · b5462afd docs(desk): R1159-R1160 card 397 brain answer
env here · ls /Users/cobalt/cobalt-wt/gate-alignment-1012/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
- `git show --stat b5462afd` → `docs(desk): R1159-R1160 card 397 brain answer`, `docs/40 - DevDocs/reports/cto-2026-10-12.md | 8 +++++---`.
- Symbols (BASE):
  - `grep -rn -F "held_rule " ops/desk` → `desk-launch.sh:1020` (comment), `desk-launch.sh:1284: held_rule "deploy $sbranch" "$crep" "$clast" "$ctip" "$shead" "$frep" || refuse "$held_why"`, `deploy-step0.sh:143` (comment), `deploy-step0.sh:585: held_rule "$branch" "$report" "$last" "$ctip" "$head" "$frep" || why=$held_why`, `deploy-card.sh:139` (comment), `deploy-card.sh:395: held_rule "$job" "$creport" "$last" "$fixtip" "$head" "$frep" || refuse "$held_why"`.
  - `grep -n -F "THE RULE"` → block markers `deploy-card.sh:135`/`:324`, `desk-launch.sh:1016`/`:1205`, `deploy-step0.sh:139`/`:328`, as the card gives.
  - THE RULE's id read `deploy-card.sh:160-163` (`awk '/^## /{on = ($0 == "## RUNS"); next}` … `index($0, "HELD, NOT FIXED")` … `index(v, "**HELD**")`), its `open: $hr_n` test `:172-175`, its count refusal `:176-179`, the CARRIED lookup `:228-229`, `:306-317` — read whole with the Read tool.
  - `grep -n -F "twice under"` → `deploy-card.sh:181`, `deploy-step0.sh:185`, `desk-launch.sh:1062`; no test pins this text.
  - `grep -n -F "SETTLED: "` over the three scripts and CHECK-HUB → nothing.
  - `grep -n -F "assert len(lines) == 123" tests/ops/test_house_probe.py` → `193`.
  - Test fixtures read: `test_deploy_card.py` `held_round` `:618`, `runs_text` `:621`, check text `:649`, `DESK_ROW` `:613`, the refusal params `:708-749`, `test_h1_the_rule_is_one_text_in_the_three_scripts` `:800`; `test_desk_launch_prechecks.py` `held_round` `:711`, `runs_text` `:714`, `:744`; `test_deploy_step0.py` `held_round` `:704`, `runs_text` `:707`, `:746`.
  - CHECK-HUB `:104` holds ``HELD` — red, or the output shown, for the finding's stated reason``; `:107` holds `is `HELD, NOT FIXED — <file>``; `:123` starts `` `ready: YES` only when``.
  - `tests/ops/test_check_hub_shadow.py` (the `lines()`/`head_lines()` shape the card names) is NOT on BASE: it is card 386's file, read with `git show ops/launcher-shadow-check-1011:tests/ops/test_check_hub_shadow.py` (`lines()` reads the file; `head_lines()` runs `git show HEAD:<hub>`). The new test file copies that shape (`## RECORDS`).
- `wc -l` (BASE): deploy-card.sh 494 · desk-launch.sh 1687 · deploy-step0.sh 735 · test_deploy_card.py 962 · test_desk_launch_prechecks.py 1307 · test_deploy_step0.py 846 · CHECK-HUB.md 123 · test_house_probe.py 280 (as the card's record).
- `## READ` reports: the 386 check report's last line (`:230`) `CHECK DONE · job: launcher-shadow-check-1011 · pass: 1 · tip: a8c18242 · … · held unfixed: 1 · open: 1 · … · ready: NO · decisions: 3 · for Dejan: 0 · tokens: 236094`; `:223` reads `open: 5`; `:168` G3 ends `· **HELD**.`; `:173` `- G3: **HELD, NOT FIXED — …**`. The F1 report at `ops/launcher-shadow-check-1011` ends `FIXED: G3 — tests/ops/test_check_hub_shadow.py::test_build_report_case_count_matches_collection`, blank, `BUILT · job: launcher-shadow-check-1011 · tip: 66c4fefc | … | decisions: 3 · for Dejan: 0 · tokens: 115749`.
- cto rows: `R1149`, `R1154`, `R1157` (DESK RECORD, DIRECTION), `R1159` (RECORD), `R1160` (DESK RECORD, the brain row in G2) — each grepped at `docs/40 - DevDocs/reports/cto-2026-10-12.md`.
- Card records re-read: 386's lines `:168`, `:173`, `:223`, `:230` as above; F1's last two non-blank lines as above; `wc -l` as above; `grep -c "SETTLED: "` → nothing. Not re-read: card 386's hunks and the `86b9daa5` commit history (no need: the files read match the record).
- `uv run cobalt jobs restarts b5462afd..HEAD` → `docs/40 - DevDocs/reports/gate-alignment-build-2026-10-12.md A DOCS -` (the untracked report), `RESTARTS: none`.
- DB: none: no lock probe.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, exit 0) → `4199 passed, 800 skipped, 1 xfailed, 36 warnings in 725.05s (0:12:05)`; 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 31.10s`; the one skip `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (not `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Tests only, no `ops/` or `src/` edit. `held_round` in `test_deploy_card.py` gained one optional `last=` (the check's last line, card 386 test (2)); nothing else of the fixtures changed.
`uv run pytest -q -rA -p no:cacheprovider --color=no --tb=no -k "g1 or g2 or h3" <the four files>` on BASE → `29 failed, 23 passed, 279 deselected`. The 23 passes are the two-sided controls below plus 18 of `test_deploy_step0.py`'s card-317 `test_h3_…` tests, which `-k h3` also matched (existing, unchanged). The reds' first lines, from the `--tb=line` run (each path shortened to `…`):
- G1 `test_deploy_card.py`: `…_closed_by_its_fixed_line_writes_the_card` (`:824`), `…_386_check_lines_and_its_f1_line_write_the_card` (`:842`), `…_with_no_fixed_line_is_refused`, `…_naming_an_absent_test_is_refused`, `…_twice_under_fixes_is_refused[n 1]` → `REFUSED: alpha: the check …/alpha-check-2026-01-02.md lists 0 HELD, NOT FIXED row(s) under ## RUNS (none), its last line says 'held unfixed: 1'`; `[n 2]` → the same with `'held unfixed: 2'`.
- G1 `test_desk_launch_prechecks.py` (3) → `REFUSED: deploy ops/x-job: the check …/x-job-check-2026-01-02.md lists 0 HELD, NOT FIXED row(s) under ## RUNS (none), its last line says 'held unfixed: 1'`.
- G1 `test_deploy_step0.py` (3) → `FAILED STEP-0: P2 check 1 — …/alpha-check-2026-01-02.md — ops/alpha: the check … lists 0 HELD, NOT FIXED row(s) under ## RUNS (none), its last line says 'held unfixed: 1'`.
- G2 `test_deploy_card.py`: `…_settled_by_a_desk_record_are_not_counted_open` (`:911`), `…_unsettled_table_row…` (`:922`), `…_without_a_settled_line_is_refused`, `…_no_desk_record_is_refused`, `…_naming_a_held_id_is_refused`, `…_missing_one_proof_is_refused[two lines for one id]`, `[a NOT HELD id]`, `[an id the check does not list]`, `[fewer settled than m - n]`, `…_settled_row_recorded_the_next_day_is_accepted` (`:994`), `…_outside_the_days…[SETTLED, the day before]`, `[SETTLED, in no desk report]` → `REFUSED: alpha: the check's last line says 'held unfixed: 1' (held ids: O1) but not 'open: 1': CHECK DONE · … · open: <3|2|4> · ready: NO · …`.
- G2 `[a settled line with open equal to n]` → `deploy-card: …/03-deploy-x-set-card.md written (2 job(s), TIP …)` (`:503`): BASE does not read SETTLED lines.
- R1160 `…_carried_row_recorded_the_next_day_is_accepted` (`:1004`) → `REFUSED: alpha: CARRIED O1 names R7, which is no DESK RECORD row of …/cto-2026-01-02.md`. `[CARRIED, newest first]` → `deploy-card: … written (2 job(s), …)` (`:503`): BASE reads only the check's day, where R7 is a DESK RECORD.
- H3 `test_check_hub_gate_wording.py:49` `test_h3_runs_and_fixes_name_held_not_fixed` → `assert 0 == 1`; `:59` `test_h3_the_ready_line_names_what_the_gates_read` → `assert 0 == 1`.
- Two-sided controls, green on BASE: `test_g1_an_id_held_in_both_sections_counts_once`, `test_g2_open_below_held_unfixed_keeps_todays_text`, `test_g2_a_row_outside_the_days_on_or_after_the_check_is_refused[CARRIED, the day before]`, `[CARRIED, a words file]`, `[CARRIED, in no desk report]`, `test_h3_no_line_is_added`.
- Not two-sided as the card words them: G1 (3), (4), (5) and G2 (2), (3), (4) are exit 1 on both sides, but each asserts the AFTER refusal text, so on BASE they are red for the id-count or `open:` refusal (quoted above). That is the row's reason: BASE never reaches the FIXED, SETTLED or row check. No test was rewritten.
- RUN R1, before (BASE scripts on both paths): the probe staged outside the worktree at `/Users/cobalt/.claude/jobs/05456e9f/tmp/r1probe/run_397_r1.py`, run as `uv run pytest -q -rP -p no:cacheprovider --color=no /Users/cobalt/.claude/jobs/05456e9f/tmp/r1probe/run_397_r1.py` → `1 passed in 0.22s`, captured WHOLE:
```
== /Users/cobalt/cobalt/ops/desk/deploy-card.sh · exit 1
-- stdout
-- stderr
REFUSED: launcher-shadow-check-1011: the check /Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-shadow-check-check-2026-10-11.md lists 0 HELD, NOT FIXED row(s) under ## RUNS (none), its last line says 'held unfixed: 1'
== /Users/cobalt/cobalt-wt/gate-alignment-1012/ops/desk/deploy-card.sh · exit 1
-- stdout
-- stderr
REFUSED: launcher-shadow-check-1011: the check /Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-shadow-check-check-2026-10-11.md lists 0 HELD, NOT FIXED row(s) under ## RUNS (none), its last line says 'held unfixed: 1'
== git -C /Users/cobalt/cobalt status --short -- <check report> <F1 report> · exit 0
(nothing)
```

## E3 THE ROWS
Commits: `f3dc5e33 fix(gate-alignment-1012): THE RULE reads a held id from RUNS or FIXES, settles open by desk record, CHECK-HUB says so (G1, G2, H3; L1, L3, L72)`, then `f47fb5d7 fix(gate-alignment-1012): THE RULE names card 397 once, in its header, pinned (G1; L1, L72)`. The first commit's SETTLED code comment also read `(card 397)`, so `grep -c -F "card 397"` gave `2` per script against the card's `1`. The second commit changes that comment to `(R1157 (2))` and adds `test_g1_the_rule_header_names_card_397_once`.
- G1 (THE RULE block and its header comment only, the same bytes in the three scripts): `hr_runs` is today's `## RUNS` read, unchanged. `hr_fixes` reads `## FIXES` lines `- <id>: … HELD, NOT FIXED …` from column 0. `hr_ids` is the RUNS ids, then the FIXES ids RUNS does not name. Each section's duplicate is refused (`twice under ## RUNS`, today's text, and a new `twice under ## FIXES`). The count refusal reads `under ## RUNS` when `## FIXES` adds no id (today's text, byte for byte) and `under ## RUNS and ## FIXES` otherwise. The header comment states the new read, and `card 397` appears once.
- G2: `hr_m` is the line's `open: <m>`. A missing value or `m < n` is refused with today's text (`… but not 'open: <n>'`). `hr_open` holds the `## RUNS` bullets whose last ` · ` field (leading `*` and blanks cut) starts `REJECTED` or `UNSETTLED`, and the table rows whose last cell does. Each `SETTLED: <id> — R<k>` line, from column 0, is refused when the id is held, is not in `hr_open`, has two lines, or its R<k> is no DESK RECORD row. The distinct count must equal m − n. BRAIN ROW (R1160): `held_row` reads the `cto-YYYY-MM-DD.md` files at HEAD dated on or after the check's date (`ls-tree`; the `-words` files excluded), newest first, and stops at the first file holding `| R<k> |`. CARRIED uses the same lookup. Its refusal text names `cto-<check date>.md`, as today (pinned at `test_deploy_card.py` `row absent` / `row without DESK RECORD`).
- H3: `CHECK-HUB.md` `:104` (a), `:107` (b), `:123` (c), each inside its line; (c) carries the brain row's `found by this rule` in place of `of the check's day` (R1160). `wc -l` → `123`; `:113-114` untouched (`git diff` hunks at `:104`, `:107`, `:123` only, `6 +-`).
- Greens after the rows: `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_deploy_card.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_deploy_step0.py tests/ops/test_check_hub_gate_wording.py tests/ops/test_house_probe.py` → `357 passed, 15 warnings in 183.22s` at `f3dc5e33`, again `357 passed … in 190.31s` after the mutations, and `358 passed, 15 warnings in 187.36s (0:03:07)` at `f47fb5d7`. `test_h1_the_rule_is_one_text_in_the_three_scripts` and the `:726-742` / `:767` pins stand unchanged and green; `test_house_probe.py:193` (123) is green.
- MUTATIONS (Edit tool, each undone; `git diff --stat` after the last one → only the fix: `CHECK-HUB.md 6 +-`, each script `101 +++…--`; `grep -c -F "MUTATED"` → `0` in each):
  - G1 `## FIXES` read off (`"## FIXES-MUTATED"`) in `deploy-card.sh`: `6 failed, 1 passed`. All six G1 tests (`…writes_the_card`, `…386…`, `…no_fixed_line…`, `…absent_test…`, `…twice…[n 1]`, `[n 2]`) fail on `REFUSED: alpha: the check … lists 0 HELD, NOT FIXED row(s) under ## RUNS (none), its last line says 'held unfixed: 1'`. The control `…held_in_both_sections_counts_once` stays green: RUNS names the id.
  - The same in `desk-launch.sh` and `deploy-step0.sh`: `6 failed` (the three `test_desk_launch_prechecks.py` G1 tests and the three `test_deploy_step0.py` G1 cases).
  - G2 `m >= n` → `m == n` (`-ne`): `12 failed, 7 passed`. Every test needing `open:` past `held unfixed` fails, and the `open: 0` control stays green.
  - G2 m − n count off (`if false`): `3 failed` — `…without_a_settled_line…`, `[a settled line with open equal to n]`, `[fewer settled than m - n]`.
  - G2 held-id and REJECTED/UNSETTLED guards off: `3 failed` — `…naming_a_held_id…`, `[a NOT HELD id]`, `[an id the check does not list]`.
  - G2 duplicate guard off: `1 failed` — `[two lines for one id]`.
  - G2 SETTLED row check off: `3 failed` — `…no_desk_record…`, `[SETTLED, the day before]`, `[SETTLED, in no desk report]`.
  - R1160 lookup on the check's day only (`'$0 == d'`): `3 failed` — `…settled_row_recorded_the_next_day…`, `…carried_row_recorded_the_next_day…`, `[CARRIED, newest first]`.
  - R1160 date floor off (`'1'`): `2 failed` — `[CARRIED, the day before]`, `[SETTLED, the day before]`.
  - R1160 name filter loosened (`…[0-9]{2}.*[.]md$`): `1 failed` — `[CARRIED, a words file]`.
  - R1160 oldest first (`sort`): `1 failed` — `[CARRIED, newest first]`.
  - H3 (a) cut back to `on this row` and (c) back to `of the check's day`: `2 failed` — `:49 assert 0 == 1` (a), `:61 assert 0 == 1` (c). One line added to CHECK-HUB: `1 failed` — `test_h3_no_line_is_added` `assert 124 == 123`.
  - The header pin: `(card 397)` put back in `deploy-card.sh`'s SETTLED comment → `1 failed` — `test_g1_the_rule_header_names_card_397_once` `AssertionError: deploy-card.sh` / `assert 2 == 1`.
- RUN R1, after (`f3dc5e33`; again at `f47fb5d7`, the same output except the out file's name, `probe-386-worktree-075503.md`), WHOLE:
```
== /Users/cobalt/cobalt/ops/desk/deploy-card.sh · exit 1
-- stdout
-- stderr
REFUSED: launcher-shadow-check-1011: the check /Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-shadow-check-check-2026-10-11.md lists 0 HELD, NOT FIXED row(s) under ## RUNS (none), its last line says 'held unfixed: 1'
== /Users/cobalt/cobalt-wt/gate-alignment-1012/ops/desk/deploy-card.sh · exit 0
-- stdout
deploy-card: /Users/cobalt/.claude/jobs/05456e9f/tmp/r1probe/probe-386-worktree-074443.md written (1 job(s), TIP ef754d0b)
-- stderr
-- the SHIPS row(s) of /Users/cobalt/.claude/jobs/05456e9f/tmp/r1probe/probe-386-worktree-074443.md
| 1 | `ops/launcher-shadow-check-1011` | `66c4fefc` | `ef754d0b` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-shadow-check-check-2026-10-11.md` | `held unfixed: 1` and `ready: NO` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-shadow-check-build-2026-10-11.md` |
== git -C /Users/cobalt/cobalt status --short -- <check report> <F1 report> · exit 0
(nothing)
1 passed in 0.41s
```
  This is the card's expected result: `main` refuses with `lists 0 … (none)`; this worktree writes the card, and its SHIPS row reads `66c4fefc` · `ef754d0b` · `held unfixed: 1` and `ready: NO` · the F1 report. The check report and the F1 report are unchanged.
- DEPLOY PROOF figures in this worktree: `grep -c -F "card 397"` → `1` in each of the three scripts; `grep -c -F "SETTLED: <id> — R<n>" CHECK-HUB.md` → `1`.
- DevDocs: no page under `docs/40 - DevDocs/cobalt/` covers these scripts (Grep `deploy-card.sh|desk-launch.sh|deploy-step0.sh|CHECK-HUB` there → only `cobalt/jobs/restarts.md`, the classifier's page). No line was added (card 386's precedent).

## RESTARTS
`uv run cobalt jobs restarts b5462afd..HEAD` at `f47fb5d7` (row R2):
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CHECK-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/gate-alignment-build-2026-10-12.md	A	DOCS	-
ops/desk/deploy-card.sh	M	operator script; no Cobalt reader	-
ops/desk/deploy-step0.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_check_hub_gate_wording.py	A	test/documentation; no resident	-
tests/ops/test_deploy_card.py	M	test/documentation; no resident	-
tests/ops/test_deploy_step0.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_prechecks.py	M	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row, as row R2 expects. The report row appears because the report is untracked while the table runs.

## W THE THREE SUITES
`<tip>` = `f47fb5d7`.
- (a0) `git diff --name-only --no-renames b5462afd` → `docs/40 - DevDocs/prompts/CHECK-HUB.md`, `ops/desk/deploy-card.sh`, `ops/desk/deploy-step0.sh`, `ops/desk/desk-launch.sh`, `tests/ops/test_check_hub_gate_wording.py`, `tests/ops/test_deploy_card.py`, `tests/ops/test_deploy_step0.py`, `tests/ops/test_desk_launch_prechecks.py`. Every path is under `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 8 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh gate-alignment-1012 offline` (exit 0) → **`offline 4199/0`**, `log: /Users/cobalt/cobalt-wt/.gate-logs/gate-alignment-1012-offline-20261012-075457.log`. This build adds no test under `tests/cobalt` or `tests/taxonomy`; its tests are in `tests/ops`, below.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh gate-alignment-1012 livenote` (exit 0) → **`live-note 146/0`**, `log: /Users/cobalt/cobalt-wt/.gate-logs/gate-alignment-1012-livenote-20261012-075458.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` (exit 0) → **`3171 passed, 1 xfailed, 15 warnings in 654.89s (0:10:54)`**; `grep -c -F "SKIPPED"` over its output → `0`. The tests this build adds or changes: `test_deploy_card.py` G1 (7 test ids: 6 plus the header pin), G2 (19 ids, R1160 included); `test_desk_launch_prechecks.py` G1 (3); `test_deploy_step0.py` G1 (3); `test_check_hub_gate_wording.py` (3).
- (b)–(d), (f): not run (DB: none). `ls /Users/cobalt/cobalt-wt/gate-alignment-1012/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every added test was shown red: at E2 against BASE (29 reds, first lines quoted), or under an E3 mutation (each quoted). The six BASE-green controls go red under their mutation: `…held_in_both_sections_counts_once` is pinned by the RUNS read, which this build leaves as is (named, not rewritten); `…open_below_held_unfixed_keeps_todays_text` is today's text, held under every mutation because it is the `m < n` branch, unchanged (named); `[CARRIED, the day before]` (date floor off), `[CARRIED, a words file]` (name filter), `[CARRIED, in no desk report]` (always refused: no file holds R7, so no mutation of the lookup turns it; named, as card R1160 asks "refused both before and after"), and `test_h3_no_line_is_added` (one line added → `assert 124 == 123`). The header pin `test_g1_the_rule_header_names_card_397_once` was written in E3, after `f3dc5e33` showed a count of `2`. Its red is the E3 mutation quoted (`assert 2 == 1`); on BASE it is red too (`0`).
(2) Callers, re-read at the tip (`grep -n -F "held_rule "`):
  - `deploy-card.sh:464` → G1 (`test_deploy_card.py`, 7 ids) and G2 (19 ids)
  - `desk-launch.sh:1353` (kind `deploy`) → G1 `test_desk_launch_prechecks.py` (3)
  - `deploy-step0.sh:654` (P2) → G1 `test_deploy_step0.py` (3)
  The G2 and R1160 behaviour of the two other callers is pinned through `test_h1_the_rule_is_one_text_in_the_three_scripts` (byte-identical block, green), as the card places G2's tests in `test_deploy_card.py` only. The clean path (`held unfixed: 0`) is fenced and unread; unchanged.
(3) Re-read at the tip: `git log --oneline b5462afd..HEAD` (three commits, below); `grep -c -F "card 397"` → `1` ×3; `grep -c -F "SETTLED: <id> — R<n>" CHECK-HUB.md` → `1`; `wc -l CHECK-HUB.md` → `123`; `grep -n -F "held_rule "` → the lines in (2); the RESTARTS table at `f47fb5d7`; R1 rerun at `f47fb5d7`.

## FOR THE CHECK
- Range `b5462afd..f47fb5d7`:
  - `edcedd7b wip(gate-alignment-1012): red`
  - `f3dc5e33 fix(gate-alignment-1012): THE RULE reads a held id from RUNS or FIXES, settles open by desk record, CHECK-HUB says so (G1, G2, H3; L1, L3, L72)`
  - `f47fb5d7 fix(gate-alignment-1012): THE RULE names card 397 once, in its header, pinned (G1; L1, L72)`
- Per row, the reds, mutation runs and greens: `## E2 RED` and `## E3 THE ROWS`. The caller greps: self-check (2). The RUN rows WHOLE: R1 in E2 (before) and E3 (after); R2 in `## RESTARTS`.
- Suites: `## W`. With-DB: not run (DB: none). F0 / F1 / F2: not run (DB: none). Lock taken / released: not run (DB: none).
- The card's records as re-read: `## PREFLIGHT`.
- For X1: a `**HELD**` RUNS bullet with no FIXES row counts nothing; that is today's read, and it is the case the CHECK-HUB (a)/(b) wording closes. A FIXES bullet counts only when it starts `- <id>: ` at column 0 and holds `HELD, NOT FIXED` anywhere in the line, so prose carrying that phrase on such a bullet counts. `NOT HELD` and table rows are as today.
- For X2: a `SETTLED` line naming a held id is refused (`…settles O1, which is a held id…`); one naming an id whose last ` · ` field (or last table cell) does not start `REJECTED`/`UNSETTLED` is refused; fewer or more distinct ids than m − n are refused; a SETTLED line never enters the FIXED/CARRIED count (the `hr_lines` grammar takes only `FIXED:`/`CARRIED:`).
- For X3: `test_h1_the_rule_is_one_text_in_the_three_scripts` green; the three `git diff` stats are `101 +++…--` each; the `:726-742` and `:767` pins green unchanged.
- For X4: `wc -l` 123; hunks at `:104`, `:107`, `:123` only.

## CONTINUE
next: CLOSE (done)

## DECISIONS
none

## RECORDS
- `tests/ops/test_check_hub_shadow.py`, the shape `## READ` and row H3 name, is not on BASE. It is card 386's file on `ops/launcher-shadow-check-1011`, read with `git show`. The new `test_check_hub_gate_wording.py` copies its `lines()` / `head_lines()` shape and imports nothing from it.
- Interpretations held to the card's words, each pinned by a test: a FIXES duplicate with n = 1 is refused at the id count (`lists 2 … under ## RUNS and ## FIXES (O1 O1)`), and with n = 2 by `twice under ## FIXES`; the order of today's refusals is unchanged. The SETTLED and CARRIED refusals name `cto-<check date>.md`, today's text (pinned for CARRIED), although the lookup now reads every desk report on or after that date. A "verdict" is the bullet's last ` · ` field or the row's last cell, after leading `*`/blanks are cut, and it must start `REJECTED` or `UNSETTLED`.
- RUN rows: R1 and R2 each showed exactly what the card expects, so neither carries a `DECISION <row>` line. The precedent is card 386's build report, whose RUN rows (L3) are quoted in E2/E3/RESTARTS, none under DECISIONS.
- R1's probe and its out files live under `/Users/cobalt/.claude/jobs/05456e9f/tmp/r1probe/` (outside the worktree, as the row asks): `run_397_r1.py`, `probe-386-worktree-074443.md`, `probe-386-worktree-075503.md`. They are cleaned with the job. Nothing was written in `/Users/cobalt/cobalt`.
- Extra work at E3: a second fix commit (`f47fb5d7`) before W, for the `card 397` count. One W run in all; no extra gate call.
- `.venv/` was created by the first `uv run` (gitignored).
- Tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 05456e9f` → `context 285193 of 400000 — ok` at 08:06 ET. That is above the desk's 250,000 line (UNATTENDED RULES (c)); the run is finished.
- The card's records, as re-read at PREFLIGHT, are above.
- The L74 line: see `## L74`. No commit carries a `Claude-Session:` line.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: gate-alignment-1012 · tip: f47fb5d7 | on b5462afd | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 5 of 5 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 285193
