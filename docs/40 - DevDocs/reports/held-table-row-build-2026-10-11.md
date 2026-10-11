# held-table-row-1011 — build report (2026-10-11)

## §0 Headline
- T1 built: the held-id read in THE RULE takes a `## RUNS` table row whose first cell is a valid id and whose last cell holds `**HELD**`; the bullet form is kept as written.
- One text, byte for byte, in `deploy-card.sh`, `desk-launch.sh` and `deploy-step0.sh` (`test_h1_the_rule_is_one_text_in_the_three_scripts` green).
- Six new tests (seven cases), red on `2f877800` for the card's reasons, green at `0188faa1`; three mutations each turn them red.
- Suites at `0188faa1`: offline 4199/0, `tests/ops` 3132/0, live-note 146/0; DB: none; RESTARTS: none.

## L74
- One system reminder in this session named a `Claude-Session:` attribution line. Recorded once as data; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/361-held-table-row-card.md"` (12:27 ET), output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/361-held-table-row-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-11/361-held-table-row-card.md" · 0 · 40e077ef3e0d9fabee4be33eb7dbcc8a6128c833
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-11/361-held-table-row-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1069 row · grep -n "^| R1069 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 24:| R1069 | 10:37 ET | HIS RULING · APPROVED (via the brain, L79; words R1069): OpenAI available, tribunal seats approved, no stops, no design round; deploy 324, install SHADOW-HUB, Grok, Sonnet, Terra arms in parallel (only the lock serializes). | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1069 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1069 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 2322ed1e5044b6ec734e2cd0d225252408f87dbd
RULING 2026-10-11 R1069 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
rule · command · exit · output
- mechanical rows · `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` · 0 · whole:
```
clock · date · 0 · Sun Oct 11 12:27:12 EDT 2026
status · git status --short --branch · 0 · ## ops/held-table-row-1011
head · git log --oneline -1 · 0 · 2f877800 docs(desk): §5 drafter 360 live (49e83894)
diff · git diff --stat 2f877800 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/held-table-row-1011 · 0 · 2f877800 docs(desk): §5 drafter 360 live (49e83894)
env here · ls /Users/cobalt/cobalt-wt/held-table-row-1011/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
- base · `git show --stat 2f877800` · 0 · `2f877800 docs(desk): §5 drafter 360 live (49e83894)` · `docs/40 - DevDocs/reports/cto-2026-10-11.md | 10 +++++-----` · `1 file changed, 5 insertions(+), 5 deletions(-)`
- parsers · `grep -n -F "HELD, NOT FIXED" ops/desk/deploy-card.sh ops/desk/desk-launch.sh ops/desk/deploy-step0.sh` · 0 · `deploy-card.sh:141` (comment), `:160` (awk), `:174`, `:205` (refusals); `desk-launch.sh:1022` (comment), `:1041` (awk), `:1055`, `:1086`; `deploy-step0.sh:145` (comment), `:164` (awk), `:178`, `:209`
- callers · `grep -n -F "held_rule " <the three>` · 0 · `deploy-card.sh:392: held_rule "$job" "$creport" "$last" "$fixtip" "$head" "$frep" || refuse "$held_why"` · `desk-launch.sh:1281: held_rule "deploy $sbranch" "$crep" "$clast" "$ctip" "$shead" "$frep" || refuse "$held_why"` · `deploy-step0.sh:582: held_rule "$branch" "$report" "$last" "$ctip" "$head" "$frep" || why=$held_why` (plus the comment lines `:139`, `:1020`, `:143`)
- end markers · `grep -n -F "# ---- end of THE RULE" <the three>` · 0 · `deploy-card.sh:321`, `desk-launch.sh:1202`, `deploy-step0.sh:325`
- pin · `grep -n -F "test_h1_the_rule_is_one_text_in_the_three_scripts" tests/ops/test_deploy_card.py` · 0 · `797:def test_h1_the_rule_is_one_text_in_the_three_scripts():`
- fixtures (Read tool) · `test_deploy_card.py:608` `HELD_RUN`, `:618` `held_round`; `test_deploy_step0.py:692` `HELD_RUN`, `:704` `held_round`; `test_desk_launch_prechecks.py:700` `HELD_RUN`, `:711` `held_round`, all at the lines the card cites.
- sizes · `wc -l` · 0 · `491 ops/desk/deploy-card.sh` · `1684 ops/desk/desk-launch.sh` · `732 ops/desk/deploy-step0.sh` · `892 tests/ops/test_deploy_card.py` · `834 tests/ops/test_deploy_step0.py` · `1294 tests/ops/test_desk_launch_prechecks.py`
- READ report · `tail -n 3 ".../reports/install-shadow-hub-check-2026-10-11.md"` · 0 · last line `CHECK DONE · job: install-shadow-hub-1011 · pass: 1 · tip: f6d698ab · … · held: 1 · fixed: 0 · held unfixed: 1 · open: 1 · … · ready: NO · decisions: 3 · for Dejan: 1 · tokens: 193760`; its `## RUNS` `:181-191` read with the Read tool: header `:182`, separator `:183`, O1 `:184` verdict `**HELD** — red for its stated reason: …`, O2-O7 `:185-190` and G1 `:191` verdicts start `NOT HELD`.
- restarts · `uv run cobalt jobs restarts 2f877800..HEAD` · 0 · `path	change	rule	restart` / `RESTARTS: none`
- card records, copied: drafter read at `2f877800`; parsers `deploy-card.sh:160`, `desk-launch.sh:1041`, `deploy-step0.sh:164` (re-read above, hold); refusal text `deploy-card.sh:174` (re-read, holds); fixture shape `:182`, `:184`, `:185-190` (re-read, holds; `:191` G1 also `NOT HELD`); pin `test_deploy_card.py:787-803` and end markers (re-read, hold); RESTARTS none (re-read: `RESTARTS: none`); no preflight by the drafter (R1069, R1084).
- DB: none card: no lock probe, no with-DB string used.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `2f877800` → `4199 passed, 800 skipped, 1 xfailed, 36 warnings in 635.84s (0:10:35)`.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.73s`; the skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (it does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Tests written (no `src/` or `ops/` edit): `held_round` in each of the three test files gains `runs_text: str | None = None` (when given, it is the `## RUNS` text; every existing caller passes none and keeps today's behaviour).
- `tests/ops/test_deploy_card.py`: `TABLE_HEAD`, `TABLE_HELD`, `TABLE_NOT_HELD`; `test_t1_a_bullet_row_is_still_counted`, `test_t1_a_table_row_marked_held_is_counted`, `test_t1_a_table_row_marked_not_held_is_ignored[one held and one not held | not held only]`, `test_t1_a_mixed_report_counts_both_forms`.
- `tests/ops/test_deploy_step0.py`: `test_t1_p2_reads_a_table_row_marked_held`.
- `tests/ops/test_desk_launch_prechecks.py`: `test_t1_the_launch_reads_a_table_row_marked_held`.

`uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line <the three files> -k "test_t1_"` on `2f877800` → `5 failed, 2 passed, 289 deselected, 15 warnings in 4.21s`. Every red's first line:
- `test_t1_a_table_row_marked_held_is_counted` → `AssertionError: REFUSED: alpha: the check …/alpha-check-2026-01-02.md lists 0 HELD, NOT FIXED row(s) under ## RUNS (none), its last line says 'held unfixed: 1'` (the card's reason)
- `test_t1_a_table_row_marked_not_held_is_ignored[one held and one not held]` → `… lists 0 HELD, NOT FIXED row(s) under ## RUNS (none), its last line says 'held unfixed: 1'` (the card's reason)
- `test_t1_a_mixed_report_counts_both_forms` → `… lists 1 HELD, NOT FIXED row(s) under ## RUNS (O1), its last line says 'held unfixed: 2'` (the card's reason)
- `test_t1_p2_reads_a_table_row_marked_held` → `FAILED STEP-0: P2 check 1 — …/alpha-check-2026-01-02.md — ops/alpha: the check … lists 0 HELD, NOT FIXED row(s) under ## RUNS (none), its last line says 'held unfixed: 1'` (the card's reason)
- `test_t1_the_launch_reads_a_table_row_marked_held` → `REFUSED: deploy ops/x-job: the check …/x-job-check-2026-01-02.md lists 0 HELD, NOT FIXED row(s) under ## RUNS (none), its last line says 'held unfixed: 1'` (the card's reason)
- GREEN on BASE, as the card says: `test_t1_a_bullet_row_is_still_counted`, `test_t1_a_table_row_marked_not_held_is_ignored[not held only]` (the `lists 0 … (none)` refusal).

Commit `9b335b87 wip(held-table-row-1011): red`.

## E3 THE ROWS
T1, in the three scripts alike (`git diff --stat` after the fix: `deploy-card.sh | 7 +++++--`, `deploy-step0.sh | 7 +++++--`, `desk-launch.sh | 7 +++++--`):
- header comment: the clause `each a line `- <id> · … HELD, NOT FIXED …`` now reads `… or a table row `| <id> | … | <verdict> |` whose last cell holds `**HELD**` (the id trimmed, [A-Za-z0-9._-]+)`.
- the awk keeps its bullet branch as written and adds, under the same `on` switch: `on && /^[|]/ {n = split($0, c, "|"); id = c[2]; v = c[n]; if (n > 2 && v ~ /^[ \t]*$/) v = c[n - 1]` / `sub(/^[ \t]+/, "", id); sub(/[ \t]+$/, "", id); if (id ~ /^[A-Za-z0-9._-]+$/ && index(v, "**HELD**")) print id}`. The last cell is `c[n]`, or `c[n-1]` when `c[n]` is blank (the text after a closing `|`). `/^[|]/` and two `sub` calls rather than `\|` or `gsub` alternation, with no `gensub` and no `match(…, arr)` (X4).
- At tip, `grep -n -F "index(v, " <the three>` → `deploy-card.sh:163`, `desk-launch.sh:1044`, `deploy-step0.sh:167`, the same line.

After the row: `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_deploy_card.py tests/ops/test_deploy_step0.py tests/ops/test_desk_launch_prechecks.py` → `296 passed, 15 warnings in 128.81s (0:02:08)`.

THE MUTATIONS (Edit tool, never committed):
- M1, undo the fix: `index(v, "**HELD**")` → `index(v, "**HELD-MUTANT**")` in all three (the pin stays equal) → `-k "test_t1_ or test_h1_the_rule"` over the three files: `5 failed, 3 passed, 288 deselected` — FAILED `test_t1_a_table_row_marked_held_is_counted`, `test_t1_a_table_row_marked_not_held_is_ignored[one held and one not held]`, `test_t1_a_mixed_report_counts_both_forms`, `test_t1_p2_reads_a_table_row_marked_held`, `test_t1_the_launch_reads_a_table_row_marked_held`; first failing line (mixed): `AssertionError: REFUSED: alpha: the check … lists 1 HELD, NOT FIXED row(s) under ## RUNS (O1), its last line says 'held unfixed: 2'`.
- M2, break the negative control: `index(v, "HELD")` in all three (so `NOT HELD` counts) → `test_deploy_card.py -k "test_t1_ or test_h1_the_rule"`: `3 failed, 3 passed, 81 deselected` — FAILED `…not_held_is_ignored[one held and one not held]` (`lists 2 HELD, NOT FIXED row(s) under ## RUNS (O1 O2), its last line says 'held unfixed: 1'`), `…[not held only]` (`lists 2 … (O1 O2)` where `lists 0 … (none)` was asserted), `test_t1_a_mixed_report_counts_both_forms` (`lists 3 … (O1 O2 O3), … 'held unfixed: 2'`).
- M3, break the bullet branch in `deploy-card.sh` only: `index($0, "HELD, NOT FIXED-MUTANT")` → `3 failed, 3 passed, 81 deselected` — FAILED `test_h1_the_rule_is_one_text_in_the_three_scripts`, `test_t1_a_bullet_row_is_still_counted`, `test_t1_a_mixed_report_counts_both_forms`.
- Each undone with the Edit tool; `git diff --stat` → the three scripts at `7 +++++--` each (the fix); `grep -rn -F "MUTANT" ops/desk` → nothing.

DevDocs: no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/` (Glob `docs/40 - DevDocs/cobalt/**/*desk*` → none; the precedent 317 wrote none). See `## RECORDS`.

Commit `0188faa1 fix(held-table-row-1011): the held-id read takes a table row whose last cell holds **HELD** (T1, L3, L72)`.

## RESTARTS
`uv run cobalt jobs restarts 2f877800..HEAD` at `0188faa1`, whole:
```
path	change	rule	restart
docs/40 - DevDocs/reports/held-table-row-build-2026-10-11.md	A	DOCS	-
ops/desk/deploy-card.sh	M	operator script; no Cobalt reader	-
ops/desk/deploy-step0.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_deploy_card.py	M	test/documentation; no resident	-
tests/ops/test_deploy_step0.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_prechecks.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row.

## W THE THREE SUITES
`<tip>` = `0188faa1`.
- (a0) `git diff --name-only --no-renames 2f877800` → `ops/desk/deploy-card.sh`, `ops/desk/deploy-step0.sh`, `ops/desk/desk-launch.sh`, `tests/ops/test_deploy_card.py`, `tests/ops/test_deploy_step0.py`, `tests/ops/test_desk_launch_prechecks.py`. Every path starts with `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 6 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh held-table-row-1011 offline` → `offline 4199/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/held-table-row-1011-offline-20261011-124401.log` (its `:879` `4199 passed, 800 skipped, 1 xfailed, 36 warnings in 641.99s (0:10:41)`). This build adds no test under `tests/cobalt` or `tests/taxonomy`; its six tests sit in `tests/ops` (below).
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3132 passed, 1 xfailed, 15 warnings in 594.83s (0:09:54)`, the six T1 tests (seven cases) among them.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh held-table-row-1011 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/held-table-row-1011-livenote-20261011-125459.log`; its one skip (`:56`) names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`.
- with-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/held-table-row-1011/.env` → `No such file or directory` (12:55 ET).

## PRE-STOP SELF-CHECK
(1) Every added test shown red: `test_t1_a_table_row_marked_held_is_counted`, `…not_held_is_ignored[one held and one not held]`, `test_t1_a_mixed_report_counts_both_forms`, `test_t1_p2_reads_a_table_row_marked_held` and `test_t1_the_launch_reads_a_table_row_marked_held` were red at E2 and red under M1; `…[not held only]` red under M2; `test_t1_a_bullet_row_is_still_counted` red under M3 (all quoted in E2 / E3). No test stayed green under its mutation; none was rewritten.
(2) Every entry path pinned: the three `held_rule` callers at tip (`deploy-card.sh:395`, `desk-launch.sh:1284`, `deploy-step0.sh:585`, `grep -n -F "held_rule "` re-run) are each pinned by a T1 table test: `test_t1_a_table_row_marked_held_is_counted` (deploy-card), `test_t1_the_launch_reads_a_table_row_marked_held` (desk-launch), `test_t1_p2_reads_a_table_row_marked_held` (deploy-step0); the one-text pin keeps every other table-form case equal across the three. Bullet only, table only, both forms, NOT HELD rows, header and separator rows: pinned in `test_deploy_card.py`.
(3) Re-read at tip: `grep -n -F "index(v, "`, `grep -n -F "held_rule "`, `grep -n -F "def test_t1_"` (`test_deploy_card.py:818`, `:827`, `:847`, `:862`; `test_deploy_step0.py:769`; `test_desk_launch_prechecks.py:766`), `git log --oneline 2f877800..HEAD`, the gate logs' summary lines (`grep -n -F`).

## FOR THE CHECK
- `2f877800..0188faa1`: `9b335b87 wip(held-table-row-1011): red` · `0188faa1 fix(held-table-row-1011): the held-id read takes a table row whose last cell holds **HELD** (T1, L3, L72)`.
- T1 reds, mutation runs and greens: E2 and E3 above.
- Caller greps: PREFLIGHT (at base) and SELF-CHECK (2) (at tip; the lines move by +3 from the added awk lines).
- RUN rows: none on this card.
- Suites: offline `offline 4199/0` (gate offline, log above); `tests/ops` `3132 passed, 1 xfailed`; live-note `live-note 146/0` (gate livenote, log above); with-DB: not run (DB: none).
- `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock taken / released: not run (DB: none).
- RESTARTS table: above. Records copied at PREFLIGHT: above.
- For X2: by the card's THE READ, a verdict cell holding `**HELD**` anywhere counts, so `NOT HELD — … **HELD** …` counts; `**NOT HELD**` does not (no `**` right before `HELD`); a leading-space `  | O1 | … |` does not start with `|` and is ignored; a row under `## OPEN` or `## DECISIONS` is outside the `on` switch.

## CONTINUE
next: none (BUILT)

## DECISIONS
none

## RECORDS
- REFUSED, not needed: `grep -rn -F "HELD" ops --include=*.sh -c` — `(eval):1: no matches found: --include=*.sh` (zsh glob; the three-file greps cover the parsers).
- DevDocs: no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/`; no dated line written (precedent 317 wrote none, and the card's files list no page).
- `tests/ops` ran outside the gate as (a0) says; the offline gate covers `tests/cobalt` and `tests/taxonomy` (`offline 4199/0`, the same count as E0).
- The card's records, as re-read at PREFLIGHT: all hold.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: held-table-row-1011 · tip: 0188faa1 | on 2f877800 | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 142972
