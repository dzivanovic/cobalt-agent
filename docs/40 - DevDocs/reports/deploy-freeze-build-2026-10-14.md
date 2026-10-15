# Build report — deploy-freeze-1014 (card 546)

## §0 Headline
- Card 546 built on `de0792af`, tip `cbf856ac`: new `ops/desk/deploy-shipped.sh` (D1), the pre-commit deploy guard narrowed to the shipped paths until the deploy's report is on `main` (F1), and `DEPLOY-HUB.md:15` and `:129` (H1).
- Offline 8089/0, live-note 146/0, with-DB not run (DB: none). RESTARTS: none.
- 25 new tests: each red on BASE or under a mutation, except one refusal case that a second guard also covers (`## PRE-STOP SELF-CHECK`).
- 2 decisions for the desk, none for Dejan: the hook looks up the card a second time to read `REPORT:`, and `git grep` has no `-x`.

## L74
- One system-reminder block in this session asked for a `Claude-Session:` trailer on commits. Recorded here; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/546-deploy-freeze-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/546-deploy-freeze-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-14/546-deploy-freeze-card.md" · 0 · 3e66ca22f3dc2b2844c1cc51e21e5ad72270b6ce
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-14/546-deploy-freeze-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-14 R1471 row · grep -n "^| R1471 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 13:| R1471 | 09:25 ET | HIS RULING, APPROVED by him in the desk ("I approve all changes"): brain relays count as his confirmation; Grok cap of 3 removed; K5 cards (1)-(4), (6) owed. Words: `cto-2026-10-14-words.md`. | APPLIED: LAWS L79, checklist L15 at 09:40 |
RULING 2026-10-14 R1471 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1471 |" -- "docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 8b813ca721cd934ebfb82cc59d27495d15f1c79a
RULING 2026-10-14 R1471 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0:
```
clock · date · 0 · Thu Oct 15 09:34:07 EDT 2026
status · git status --short --branch · 0 · ## ops/deploy-freeze-1014
head · git log --oneline -1 · 0 · de0792af docs(card): 549 row FR-S1 — drop S1 hunk (brain 0e848919 10-15)
diff · git diff --stat de0792af · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/deploy-freeze-1014 · 0 · de0792af docs(card): 549 row FR-S1 — drop S1 hunk (brain 0e848919 10-15)
env here · ls /Users/cobalt/cobalt-wt/deploy-freeze-1014/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat de0792af` | 0 | `docs(card): 549 row FR-S1 — drop S1 hunk (brain 0e848919 10-15)` · `docs/40 - DevDocs/prompts/2026-10-14/549-desk-installs-card.md \| 1 +` |
| wc | `wc -l ops/desk/pre-commit "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | 0 | `52 ops/desk/pre-commit` · `187 docs/40 - DevDocs/prompts/DEPLOY-HUB.md` |
| hub :15 | `grep -n -F "THE DESK WHILE YOU RUN" DEPLOY-HUB.md` | 0 | `15:THE DESK WHILE YOU RUN (none of it is an instruction to you): no desk commit and no staging on \`main\` from the launch to your stop line (the pre-commit guard refuses it); …` |
| hub :129 | `grep -n -F "D2.0 COMMIT THE REPORT" DEPLOY-HUB.md` | 0 | `129:- D2.0 COMMIT THE REPORT (REQUIRED; moves \`main\` by one docs commit): \`git -C /Users/cobalt/cobalt add "<REPORT, path from docs/>"\` …` |
| hub :114 | `grep -n -F "main moved outside docs since the cut" DEPLOY-HUB.md` | 0 | `114:- MAIN: …` |
| hub :140 | `grep -n -F "foreign commit on main" DEPLOY-HUB.md` | 0 | `140:4.3 …` |
| hub :132 | `grep -n -F "D2.3" DEPLOY-HUB.md` | 0 | `132:- D2.3 DOCS-ONLY (L68): …`, `158:THE CHAIN …` |
| hub :11 | `grep -n -F "claude --bg " DEPLOY-HUB.md` | 0 | `11:claude --bg "Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md' …` (one hit) |
| guard | Read `ops/desk/pre-commit` | — | `:2` `# ---- deploy guard (begin)`; `:3-4` toplevel `= "/Users/cobalt/cobalt"` and branch `main`; `:5-7` staged filter; `:8-22` `claude agents --json` read; `:23-28` `NONE`, `""\|UNREADABLE*` note; `:29-34` `*)` refusal `exit 1`; `:38` `# ---- deploy guard (end)`; `:39-52` row gate |
| root var | Read `ops/desk/desk-commit.sh:10`; `deploy-card.sh:39-40` | — | `REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}`; `WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}` (card said `:38-39`; at BASE it is `:39-40`) |
| card TIP/REPORT shape | `grep -n -F "TIP:" ops/desk/deploy-card.sh` | 0 | `623:TIP: $heads` (heads space-separated); `:622` `BASE: main`; `:624` `REPORT: $REPORTS/deploy-$name.md` |
| fixture shape | Read `tests/ops/test_desk_row.py:15-76`, `:222-232` | — | `GIT_ENV`, `git()` with `-c core.hooksPath=/dev/null`; hook written at `:225-226` |
| new names | `grep -rn -F "deploy-shipped" ops tests src` | 1 | nothing (new) |
| hub-lines pin of the hook | `grep -n -F "pre-commit" tests/ops/test_hub_lines.py` | 1 | nothing |
| READ tail | `tail -n 3 reports/deploy-hub-text-1013.md` | 0 | last line `FAILED: smoke (s) — tests/ops/test_hub_text_1013.py::test_h1_the_launch_line_and_every_other_line_stand red on the landed tree (BASE ce548f10 pinned; main's launch line moved since) · rollback: used — …` |
| READ row 21 | `grep -n -F "\| 21 " reports/survey-blockers-2026-10-12.md` | 0 | `33:\| 21 \| \`ops/desk/pre-commit:17-33\` … \| KEEP: \`main\` must not move between D2.0 and 4.3 …` |
| READ R1472 | `grep -n -F "\| R1472 " reports/cto-2026-10-14.md` | 0 | `12:\| R1472 \| 10:05 ET \| DESK RECORD, brain: … fix round pins only 523's own lines (no whole-line pin, no BASE hash) …` |
| RESTARTS empty | `uv run cobalt jobs restarts de0792af..HEAD` | 0 | `path	change	rule	restart` / `RESTARTS: none` |
| DB | card `DB: none` | — | no lock probe, no with-DB step |

Card `## RECORDS` copied (re-read where listed): the drafter read on `main` `0ffb6949` / amend on `97abf074`; every `file:line` above re-read at BASE `de0792af` and equal, except `deploy-card.sh:38-39` → `:39-40` at BASE (one line off; same text). The `.git/hooks/pre-commit` symlink and `core.hooksPath` unset are the desk's reads (not re-read: no listed command reads them).

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4328 passed, 806 skipped, 1 xfailed, 36 warnings in 714.70s (0:11:54)` (exit 0; 0 failed, 0 errors).
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 31.12s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
`uv run pytest -q -rfE -p no:cacheprovider --color=no --tb=line tests/ops/test_deploy_freeze_1014.py` on BASE → `16 failed, 5 passed, 15 warnings in 4.24s`. Each red's first line:
- D1 (1) `test_d1_lists_the_heads_paths_and_the_hub_file`, (2) `test_d1_moved_prints_a_shipped_path_that_changed_on_main`, (3) `test_d1_moved_is_empty_when_only_an_unshipped_path_moved`: `AssertionError: sh: /Users/cobalt/cobalt-wt/deploy-freeze-1014/ops/desk/deploy-shipped.sh: No such file or directory` / `assert 127 == 0`. (3) is the card's negative control "GREEN once D1 is in"; on BASE it is red for the missing script, as (1)-(2).
- D1 (4) `test_d1_refuses_no_card_two_cards_and_a_bad_head[unknown job|two cards|bad head|no TIP line|card outside prompts|bad rev]`: `AssertionError: (127, 'sh: …/deploy-shipped.sh: No such file or directory` / `assert 127 == 1`. The last three cases are the card's other `REFUSED:` rules (missing `TIP:`, a card outside `prompts/`) and a `--moved` rev that does not resolve.
- F1 (5) `test_f1_a_shipped_path_is_refused_while_the_report_is_uncommitted`: `assert 0 == 1` (guard skipped in the tmp repo).
- F1 (7) `test_f1_every_path_is_refused_once_the_report_is_committed_on_main`: `assert 0 == 1`.
- F1 (8) `test_f1_an_unreadable_session_list_commits_with_the_note`: `assert 'could not read the session list' in ''`.
- F1 (9) `test_f1_a_card_that_cannot_be_found_refuses_all_paths[no card|two live hubs]`: `assert 0 == 1` (the second case is the card's "two or more live `deploy-hub-` sessions → (i)").
- H1 (11): `AssertionError: assert 'of a path this set ships' in 'THE DESK WHILE YOU RUN …'`; H1 (12): `assert 0 == 1` on `line.count("deploy-shipped.sh --moved <m0>")`.
- GREEN on BASE as the card says: (6) `test_f1_an_unshipped_path_commits_while_the_report_is_uncommitted` (docstring states it), (8) `test_f1_the_report_path_alone_commits`, `test_f1_no_live_hub_commits_anything`, (10) `test_f1_the_hook_is_one_deploy_guard_and_one_row_gate`, (13) `test_h1_the_other_freeze_lines_stand`.
- Commit `d7943e3e wip(deploy-freeze-1014): red — D1 F1 H1 tests`. No RUN row in E2 (R5 runs at RESTARTS).

## E3 THE ROWS
Re-read before the edits: `ops/desk/pre-commit` whole (Read), `DEPLOY-HUB.md:15` and `:129` (grep, `## PREFLIGHT`).

**D1** `ops/desk/deploy-shipped.sh` (NEW). First run: `error: unknown switch \`x'` from `git grep` (it has no `-x`). The card's `git grep -l -x -F "JOB: <JOB>"` became `git grep -l -e "^JOB: <JOB>$"`, with `<JOB>` refused outside `[A-Za-z0-9_-]` (DECISION 1). Then `uv run pytest … -k test_d1` → `9 passed, 12 deselected`.
Tests added beyond the card's list: `test_d1_a_build_card_of_the_same_job_is_not_the_deploy_card` (check ask X4), plus the refusal cases `short head`, `no TIP line`, `card outside prompts` and `bad rev`. The `two cards` case was rewritten: its first form named the head `00000000`, which the diff's own failure already refused, so it stayed green under M-D1c. Now the second card names the same valid head.
- M-D1a (the hub path dropped from the list) → `1 failed, 8 passed`: `test_d1_lists_the_heads_paths_and_the_hub_file` — `assert ['docs/a.md'] == ['docs/40 - D..., 'docs/a.md']`.
- M-D1b (`--moved` prints every shipped path) → `2 failed, 7 passed`: `test_d1_moved_prints_a_shipped_path_that_changed_on_main` — `assert ['docs/40 - D..., 'docs/a.md'] == ['docs/a.md']`; negative control `test_d1_moved_is_empty_when_only_an_unshipped_path_moved` — `assert 'docs/40 - De...\ndocs/a.md\n' == ''`.
- M-D1c (the one-card rule and the resolve check removed; the hex check made silent) → `1 failed, 10 passed`: `[two cards]` — `AssertionError: (0, '')` / `assert 0 == 1`. `[bad head]` (`zzzzzzzz`) stayed green: `git diff main...zzzzzzzz` fails, and that refuses too (self-check 1).
- M-D1d (the `BASE: main` filter and the 8-length check removed) → `2 failed, 9 passed`: `test_d1_a_build_card_of_the_same_job_is_not_the_deploy_card` — `REFUSED: 2 deploy cards on main with JOB: x and BASE: main`; `[short head]` — `AssertionError: (0, '')`.
- Each undone with Edit; the file was re-read whole at the fix (Read `:36-104`).

**F1** `ops/desk/pre-commit`: `:3` root → `${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}`; the `*)` arm decides (i) / (ii) / (iii) as the card says. The today's-refusal lines are kept word for word inside its `else`. Run → `71 passed`, 2 failed (H1 only, not built yet). The card's REPORT fail-closed rules had no test, so `test_f1_a_card_report_that_cannot_be_read_refuses_all_paths[no REPORT|REPORT outside docs]` was added. `[two live hubs]` was added to test (9).
- M-F1a (`guard_mode=shipped` never set: today's freeze-all) → `2 failed, 7 passed`: (5) `assert ('ships' in 'pre-commit: a deploy hub is live — no desk commit on main until its stop line:…')`; (6) `assert 1 == 0`.
- M-F1b (arm (ii) dropped: `&& true`) → `1 failed, 8 passed`: (7) `assert 0 == 1`.
- M-F1c (an unreadable REPORT → shipped mode) → `2 failed, 9 passed`: `[no REPORT]`, `[REPORT outside docs]` `assert 0 == 1`.
- M-F1d (a refused `deploy-shipped.sh` → shipped mode) → `2 failed, 9 passed`: (9) `[no card]`, `[two live hubs]` `assert 0 == 1`.
- The `:3` change undone is BASE itself: E2's reds for (5), (7), (9), the unreadable note.

**H1** `DEPLOY-HUB.md:15` and `:129`, new text exactly as the card gives it. `git diff` of the hub: two hunks, at `@@ -12,7 +12,7 @@` (line 15) and `@@ -126,7 +126,7 @@` (line 129), nothing else.
- M-H1 (both lines back to BASE words, and the negative control broken: `foreign commit on main` → `foreign commit`) → `3 failed`: (11) `assert 'of a path this set ships' in 'THE DESK WHILE YOU RUN …'`; (12) `assert 0 == 1` on `count('deploy-shipped.sh --moved <m0>')`; (13) `assert 0 == 1` on `count('foreign commit on main')`.

At the fix: `git diff --stat` → `DEPLOY-HUB.md | 4 +--`, `ops/desk/pre-commit | 50 ++++…`, `tests/ops/test_deploy_freeze_1014.py | 36 ++…` (the added tests), then `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_deploy_freeze_1014.py tests/ops/test_hub_lines.py tests/ops/test_desk_row.py` → `77 passed, 15 warnings in 10.20s`. Commit `c93c9022 feat(deploy-freeze-1014): a deploy freezes only the paths it ships, re-verified at D2.0 (D1 F1 H1, R1471, L1 L3 L72)`.

Second fix (found after the first W, by the card's DEPLOY PROOF): `grep -c -F "deploy-shipped.sh" ops/desk/pre-commit` → `2` (a comment named it), but the card expects `after 1`. The comment was reworded, and now `grep -c` → `1`. The card's pins → `77 passed, 15 warnings in 10.90s`. Commit `cbf856ac fix(deploy-freeze-1014): the hook names deploy-shipped.sh once, as DEPLOY PROOF counts (F1)`. RESTARTS and W were run again (`## RECORDS`).

DevDocs: `docs/40 - DevDocs/cobalt/` holds no page for an `ops/desk/` script (`ls` in `## PREFLIGHT` scope; `Grep pre-commit|desk-commit.sh` outside reports/prompts hits only `plans/fixed-files-2026-09-30/*` and two archiver pages), so no dated line was written (`## RECORDS`).

## RESTARTS
R5 (RUN). `uv run cobalt jobs restarts de0792af..HEAD` on tip `cbf856ac`:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/deploy-freeze-build-2026-10-14.md	A	DOCS	-
ops/desk/deploy-shipped.sh	A	operator script; no Cobalt reader	-
ops/desk/pre-commit	M	operator script; no Cobalt reader	-
tests/ops/test_deploy_freeze_1014.py	A	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row. The same table on `c93c9022`.

## W THE THREE SUITES
`<tip>` = `cbf856ac`. (a0) `git diff --name-only --no-renames de0792af` → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `ops/desk/deploy-shipped.sh`, `ops/desk/pre-commit`, `tests/ops/test_deploy_freeze_1014.py`: every path is under `docs/`, `ops/` or `tests/ops/`. **cobalt_dev: not taken (DB: none — 4 paths)**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-freeze-1014 offline` → exit 0:
  `tests/ops: run (docs/40 - DevDocs/prompts/DEPLOY-HUB.md)` · `offline 8089/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-freeze-1014-offline-20261015-102118.log`. The first run on `c93c9022` was the same: `offline 8089/0`, log `…-offline-20261015-095422.log` (`grep -n -F "passed"` → `885:4328 passed, 806 skipped, 1 xfailed …`, `955:3761 passed, 1 xfailed …`).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-freeze-1014 livenote` → exit 0: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-freeze-1014-livenote-20261015-102119.log` (first run `…-livenote-20261015-095423.log`, `146/0`).
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` on `c93c9022` → `3761 passed, 1 xfailed, 16 warnings in 855.95s (0:14:15)`. On `cbf856ac` the tests/ops run is the one inside the offline gate (its `tests/ops: run` line; a one-line comment change).
- The new tests at the tip: `uv run pytest -q -rA … tests/ops/test_deploy_freeze_1014.py` → `25 passed`, each `PASSED` id is quoted in `## FOR THE CHECK`.
- with-DB: not run (DB: none). `.env`: never present (`## PREFLIGHT`; no lock taken).

## PRE-STOP SELF-CHECK
(1) Each test was shown red. D1 (1)-(4): E2's `127` reds, then M-D1a–d. F1 (5), (7), (9), the unreadable note: E2 reds, then M-F1a, M-F1b, M-F1d. (6) M-F1a. The REPORT fail-closed test: M-F1c. H1 (11)-(13): E2 and M-H1. The controls (8) and (10) are green by design: (8) the report path alone and no live hub; (10) the markers. GAP: `[bad head]` (`zzzzzzzz`) stays refused if the hex and resolve checks are removed, because `git diff main...zzzzzzzz` fails and refuses too. Its red on E2 was the missing script only. Not rewritten: either check is enough to refuse it.
(2) Every entry path is pinned. Callers of `deploy-shipped.sh` (`grep -rn -F "deploy-shipped" ops src`): `ops/desk/pre-commit:37` is the one code caller, pinned by the F1 tests through the real hook copy. The hub's D2.0 line is pinned by (12). Forms: `--job` (1)-(4), the card path (1) and `[card outside prompts]`, `--moved` with `--job` (2), (3), `[bad rev]`. Guard states: no hub, unreadable, one hub, two hubs, no card, REPORT missing or outside docs, report committed. `--moved` with a card path is not run by a test; it shares its code with `--moved --job` (DECISIONS none: same branch after the card is read).
(3) Every count was re-read at the tip: `grep -c -F "deploy-shipped.sh"` → hub `2`, hook `1` (after `cbf856ac`); `git log --oneline de0792af..HEAD`; the hub `git diff`; the RESTARTS table re-run at the tip; the gate lines read from their output files.
self-check: 3 of 3, with the gap in (1) stated above (backed by M-D1c's output).

## FOR THE CHECK
- `de0792af..cbf856ac`: `d7943e3e wip(deploy-freeze-1014): red — D1 F1 H1 tests` · `c93c9022 feat(deploy-freeze-1014): a deploy freezes only the paths it ships, re-verified at D2.0 (D1 F1 H1, R1471, L1 L3 L72)` · `cbf856ac fix(deploy-freeze-1014): the hook names deploy-shipped.sh once, as DEPLOY PROOF counts (F1)`.
- The reds, mutations and greens per row: `## E2 RED`, `## E3 THE ROWS`.
- The new test ids, all PASSED at the tip (`-rA`): `test_d1_lists_the_heads_paths_and_the_hub_file`, `test_d1_moved_prints_a_shipped_path_that_changed_on_main`, `test_d1_moved_is_empty_when_only_an_unshipped_path_moved`, `test_d1_a_build_card_of_the_same_job_is_not_the_deploy_card`, `test_d1_refuses_no_card_two_cards_and_a_bad_head[unknown job|two cards|bad head|short head|no TIP line|card outside prompts|bad rev]`, `test_f1_a_shipped_path_is_refused_while_the_report_is_uncommitted`, `test_f1_an_unshipped_path_commits_while_the_report_is_uncommitted`, `test_f1_every_path_is_refused_once_the_report_is_committed_on_main`, `test_f1_the_report_path_alone_commits`, `test_f1_no_live_hub_commits_anything`, `test_f1_an_unreadable_session_list_commits_with_the_note`, `test_f1_a_card_that_cannot_be_found_refuses_all_paths[no card|two live hubs]`, `test_f1_a_card_report_that_cannot_be_read_refuses_all_paths[no REPORT|REPORT outside docs]`, `test_f1_the_hook_is_one_deploy_guard_and_one_row_gate`, `test_h1_the_desk_line_names_the_shipped_paths_and_the_full_freeze_after_d20`, `test_h1_d20_reverifies_the_shipped_paths_before_the_report_commit`, `test_h1_the_other_freeze_lines_stand` → `25 passed`.
- Caller grep: `ops/desk/pre-commit:37` (the call); the hub D2.0 line (H1). X2: the shipped paths are derived only in `deploy-shipped.sh`. But the hook's arm (ii) runs a second, narrower `git grep` to find the card's `REPORT:` line (DECISION 2).
- X3: the test file reads no commit literal and no `<BASE>` hash: `grep -n -F "de0792af"` and `grep -n -F "* 8"` over it print nothing. Heads come from the tmp repo by `rev-parse`, and the hub lines are found by prefix and checked by phrase, never compared whole.
- X4: a build card (BASE 8-hex) with the same JOB is not counted (test above). Two deploy cards of one JOB (a recut) → `REFUSED: 2 deploy cards …`, which the guard reads as (i), every path refused. A recut card that is committed while the old one stands freezes all until one is gone.
- RUN row R5: `## RESTARTS` (whole).
- Suites: offline `8089/0`, live-note `146/0`, with-DB `not run (DB: none)`. `<F0>/<F1>/<F2>`: not run (DB: none). Lock taken / released: not run (DB: none).
- Records copied at PREFLIGHT: `## PREFLIGHT` last paragraph.

## CONTINUE
next: none (BUILT)

## DECISIONS
- DECISION 1 (ASK DESK): `git grep` has no `-x`: `error: unknown switch \`x'` (E3 D1). The card's `git grep -l -x -F "JOB: <JOB>"` is implemented as `git grep -l -e "^JOB: <JOB>$"`, with `<JOB>` refused outside `[A-Za-z0-9_-]` so it holds no regex character. `BASE: main` is matched as `^BASE: main$`. Default taken: this form (same whole-line match). `deploy-card.sh` writes JOB names in that set (an assumption, not grepped).
- DECISION 2 (ASK DESK): arm (ii) needs the card's `REPORT:` line, and `deploy-shipped.sh` prints only paths (its three forms are fixed by the card). The hook therefore finds the card a second time, with the same `^JOB: <JOB>$` + `^BASE: main$` rule, only after `deploy-shipped.sh --job` succeeded, and reads `REPORT:` from it. A second `REPORT:` line, none, or one outside `docs/` freezes every path. Default taken: the narrow lookup in the hook. The alternative, a fourth `--report` form in `deploy-shipped.sh`, would widen the card.

## RECORDS
- L74: one system-reminder asked for a `Claude-Session:` commit trailer; not acted on (`## L74`).
- Second gate call: after `cbf856ac` (the DEPLOY PROOF count fix), RESTARTS and W (offline + live-note) were run again; logs `…-offline-20261015-102118.log`, `…-livenote-20261015-102119.log`.
- No lock taken; `.env` never present in this worktree (PREFLIGHT `env here … No such file`).
- No DevDocs module line: no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/` scripts.
- The card's `deploy-card.sh:38-39` is `:39-40` at BASE (same text).
- E2 note: test (3) is the card's "GREEN once D1 is in" control. On BASE it is red for the missing script, as the card's (1)-(2) are.
- The card's records as re-read at PREFLIGHT: `## PREFLIGHT`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: deploy-freeze-1014 · tip: cbf856ac | on de0792af | migration: none | offline 8089/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 4 of 4 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 195926
