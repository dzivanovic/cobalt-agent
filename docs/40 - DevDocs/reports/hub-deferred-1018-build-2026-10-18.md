# hub-deferred-1018 — build report (2026-10-18)

## §0 Headline
- Card 787, rows D1 and D2, built on `170e90ca`; tip `79b8ac8e`. DB: none.
- `DEPLOY-HUB.md` changed on its five card lines only (`:5`, `:89`, `:93`, `:94`, `:154`). STEP-R now admits the `RESTARTS:` set minus `<deferred set>`, so card 730's set passes. A label outside the three that is not deferred is still refused.
- New `tests/ops/test_hub_deferred_1018.py`: 3 failed, 2 passed on BASE (the card's figure); 5 passed at the tip. Every test went red under its mutation.
- offline 8608/0 · with-DB not run (DB: none) · live-note 147/0 · RESTARTS: none.

## L74
- A system reminder in this session asked commits to carry a `Claude-Session:` line. Recorded once here; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (BUILD-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/787-hub-deferred-card.md"` (exit 0), output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/787-hub-deferred-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/787-hub-deferred-card.md" · 0 · 5566b713bb85cc35fd8682ee6e8ac918c58ea2ac
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/787-hub-deferred-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 62:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` (exit 0), output whole:
```
clock · date · 0 · Sun Oct 18 16:39:22 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/hub-deferred-1018
    ?? "docs/40 - DevDocs/reports/hub-deferred-1018-build-2026-10-18.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 170e90ca docs(prompt): 786 drafter for hub-deferred-1018 card
diff · git diff --stat 170e90ca · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/hub-deferred-1018 · 0 · 170e90ca docs(prompt): 786 drafter for hub-deferred-1018 card
env here · ls /Users/cobalt/cobalt-wt/hub-deferred-1018/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat 170e90ca` | 0 | `docs(prompt): 786 drafter for hub-deferred-1018 card` · `docs/40 - DevDocs/prompts/2026-10-18/786-draft-hub-deferred.md \| 7 +++++++` · 1 file changed, 7 insertions(+) |
| symbol D1(c) | Grep `` `RESTARTS:` set within `com.cobalt.agent com.cobalt.aset com.cobalt.radar` `` in the hub | 0 | `93` |
| symbol D2(a) | `grep -n -F "Never copy an expectation from an earlier deploy."` hub | 0 | `94:- THE SET DRIVES THE REST: …` |
| symbol D2(b) | Grep `` `RESTARTS:` = STEP-R's `<restart set>` `` in the hub | 0 | `154` |
| symbols D1(a), D1(b) | `grep -n -F "deferred"` hub | 0 | lines `5`, `13`, `89` (`:5` holds `a \`deferred\` label is not in it; none → empty)`; `:89` holds `is \`<launchd set>\`, with its mode, named beside \`<restart set>\``) |
| `<deferred set>` on BASE | `grep -n -F "<deferred set>"` hub | 1 | nothing |
| launchctl call sites | Grep `launchctl (bootout\|bootstrap\|kickstart\|print)` -o in the hub | 0 | lines 11, 13, 53, 65, 77, 122, 125, 139, 143, 144, 149, 162, 163, 165, 168 |
| CARD.md `## LAUNCHD` | `grep -n -F "## LAUNCHD"` CARD.md | 0 | `69:` (the `add\|change\|deferred` line), `150:` |
| card 730 | `grep -n -F "deferred"` 730 card · Read lines 13-14 · Grep `D8` | 0 | `13: RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.cos com.cobalt.radar` · `14:BOOTSTRAP: deferred com.cobalt.cos` · `94:- D8 — DEPENDENCY: … RESTARTS holds \`com.cobalt.cos\`; \`DEPLOY-HUB.md:93\` … refuse any other label.` |
| deploy-step-c.sh | Read `:24-32`, `:280-290` | — | `:285-286` `if [ "$lmode" = deferred ]; then printf 'ADMITTED: %s · add · deferred\n'` |
| hub readers (callers) | Grep `DEPLOY-HUB.md` in `tests/` | 0 | test_authorize, test_bare_guard, test_hub_text_1013, test_desk_launch_recut, test_deploy_step0, test_gate, test_devdb_lock, test_deploy_smoke_string_1014, test_deploy_card, test_stop_guard, test_deploy_freeze_1014, test_desk_launch_prechecks, test_desk_launch_launchd, test_pass1_db_only, test_hub_lines, test_deploy_step_c, test_desk_size_guard, test_db_copy_1014 |
| wc | `wc -l "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | 0 | `187` (188 lines with the last one unterminated, as the card's Read counts) |
| new file | `ls tests/ops/test_hub_deferred_1018.py` | 1 | No such file or directory |
| RESTARTS empty range | `uv run cobalt jobs restarts 170e90ca..HEAD` | 0 | only the untracked report row (`DOCS`, `-`); `RESTARTS: none` |
| tail of `## READ` reports | — | — | `## READ` names no report |
| lock probe | — | — | none (DB: none) |

Card `## RECORDS`, copied: drafter `draft-hub-deferred` (prompt 786), 16:33 EDT, BASE `170e90ca` (re-read: preflight `head` row) · the hub read whole at BASE; `deferred` on `:5`, `:13`, `:89` only (re-read: grep above) · hub path `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (re-read) · no test pinned the five lines; `test_deploy_step_c.py:298-301` asserts the MODEL line holds `<launchd set>` and STEP-C names `deploy-step-c.sh` once (re-read: Read `:297-301`) · BAND HIGH · RESTARTS K10: `docs/` and `tests/ops/` reach no resident (re-read: the RESTARTS table) · ORDER: this card deploys before card 730.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4646 passed, 841 skipped, 4 xfailed, 36 warnings in 747.71s (0:12:27)`.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 30.90s`; the one skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. No skip names `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_hub_deferred_1018.py` on BASE's hub → `3 failed, 2 passed, 15 warnings in 0.88s` (`F.FF.`), which is the card's `3 failed, 2 passed`:
- `test_d1_card_730s_set_is_admitted`: `E       AssertionError: assert False is True` (admits returns False: no `minus` clause).
- `test_d2_the_deferred_set_is_named_where_it_is_made_and_read`: `E       AssertionError: assert 0 == 1` (the first assert: count 0).
- `test_d2_no_launchctl_call_names_the_deferred_set`: `E       assert 0 == 5` (0 lines).
- CONTROLs green on BASE: `test_d1_a_label_outside_the_three_not_deferred_is_refused` and `test_d2_the_three_residents_strings_stand` passed.
No with-DB red (DB: none). Commit `dbe3f841 wip(hub-deferred-1018): red — D1, D2 hub-text tests (3 red, 2 controls green on BASE)`.

## E3 THE ROWS
- D1: (a) `:5` adds the `<deferred set>` name; (b) `:89` adds `; each \`ADMITTED:\` label marked \`· deferred\` is \`<deferred set>\``; (c) `:93` adds `, minus every label of \`<deferred set>\` (a label the card ships \`deferred\` merges unloaded: nothing restarts it),` and `; write \`<deferred set>\` under \`## RESTARTS\` beside it`. The three names, `(one, two, all three, or none)` and the `Anything else (…)` sentence are unchanged (`git diff` below). After D1: `-k d1` → `2 passed, 3 deselected`.
- D2: (a) `:94` appends the card's sentence verbatim; (b) `:154` reads `` `RESTARTS:` minus `<deferred set>` (as `## RESTARTS` records it) = STEP-R's `<restart set>` ``. After D2: the file → `5 passed, 15 warnings in 0.80s`.
- `git diff 170e90ca -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`: three hunks, five `-`/`+` line pairs, at `:5`, `:89`, `:93`, `:94`, `:154`; `git diff --stat` → `10 +++++-----`, `5 insertions(+), 5 deletions(-)`.
- `uv run pytest -q -p no:cacheprovider --color=no tests/ops` → `3962 passed, 1 xfailed, 16 warnings in 910.21s (0:15:10)`.
- DEPLOY PROOF figures in the worktree: `grep -c -F "<deferred set>"` → `5`; `grep -c -F "minus every label of"` → `1`.
- THE MUTATIONS (Edit tool, each undone with the Edit tool):
  - M1, D1 fix undone (the `minus …` clause removed from `:93`): `-k d1` → `1 failed, 1 passed, 3 deselected`; `FAILED …::test_d1_card_730s_set_is_admitted` · `E   AssertionError: assert False is True`.
  - M2, D1 control broken (`com.cobalt.herdr` → `com.cobalt.hrdr` in `Anything else`): `-k d1` → `1 failed, 1 passed, 3 deselected`; `FAILED …::test_d1_a_label_outside_the_three_not_deferred_is_refused` · `assert 'Anything else (an \`UNCLASSIFIED\` row, \`com.cobalt.herdr\` …' in "- GATE: exit 0, …"`.
  - M3, D2 fix undone (the `:154` clause removed): `-k d2` → `2 failed, 1 passed, 2 deselected`; `E   assert '\`RESTARTS:\` minus \`<deferred set>\`' in "- (f) …"` and `E   assert 4 == 5`.
  - M4, D2 guard (`<deferred set>` put into 4.6L's `for each label of`): `-k no_launchctl` → `1 failed, 4 deselected`; `E   AssertionError: 4.6L THE LAUNCHD SET, … for each label of \`<deferred set>\` …`.
  - M5, CONTROL 2 broken (MODEL line `the labels of \`<launchd set>\`` → `<deferred set>`): `-k strings_stand` → `1 failed, 4 deselected`; `E   AssertionError: assert 'the labels of \`<launchd set>\`' in 'MODEL: …'`.
  - After all undos: `git diff --stat` → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md | 10 +++++-----` (the fix); the row tests plus `test_hub_text_1013.py`, `test_hub_lines.py`, `test_deploy_step_c.py`, `test_deploy_freeze_1014.py`, `test_desk_launch_launchd.py` → `121 passed, 15 warnings in 25.94s`.
- DevDocs line: no `.py` module changed, so no module page under `docs/40 - DevDocs/cobalt/` (Grep for `DEPLOY-HUB` there: `cli.md` only, which is a module page). See `## RECORDS`.
- Commit `79b8ac8e fix(hub-deferred-1018): STEP-R admits the restart set minus the deferred set; no launchctl call names it (D1, D2, L1, L42, L79)`.

## RESTARTS
`uv run cobalt jobs restarts 170e90ca..HEAD`, whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/hub-deferred-1018-build-2026-10-18.md	A	DOCS	-
tests/ops/test_hub_deferred_1018.py	A	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row.

## W THE THREE SUITES
`<tip>` = `79b8ac8e`.
- (a0) `git diff --name-only --no-renames 170e90ca` → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `tests/ops/test_hub_deferred_1018.py`. Every path starts with `docs/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 2 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh hub-deferred-1018 offline` (exit 0):
  ```
  tests/ops: run (docs/40 - DevDocs/prompts/DEPLOY-HUB.md)
  offline 8608/0
  log: /Users/cobalt/cobalt-wt/.gate-logs/hub-deferred-1018-offline-20261018-171106.log
  ```
  The build adds five tests, all in `tests/ops/test_hub_deferred_1018.py`: `test_d1_card_730s_set_is_admitted`, `test_d1_a_label_outside_the_three_not_deferred_is_refused`, `test_d2_the_deferred_set_is_named_where_it_is_made_and_read`, `test_d2_no_launchctl_call_names_the_deferred_set`, `test_d2_the_three_residents_strings_stand`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh hub-deferred-1018 livenote` (exit 0):
  ```
  live-note 147/0
  log: /Users/cobalt/cobalt-wt/.gate-logs/hub-deferred-1018-livenote-20261018-171107.log
  ```
  `grep -n -F "SKIPPED" <log>` → `56:SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. No skip names `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3962 passed, 1 xfailed, 16 warnings in 947.75s (0:15:47)`.
- (b)–(d), (f): not run (DB: none). `ls /Users/cobalt/cobalt-wt/hub-deferred-1018/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
1. Every added test was shown red for its named reason. On BASE: `test_d1_card_730s_set_is_admitted` (`assert False is True`), `test_d2_the_deferred_set_is_named_where_it_is_made_and_read` (`assert 0 == 1`), `test_d2_no_launchctl_call_names_the_deferred_set` (`assert 0 == 5`). Under mutation: M1, M3, M4. The two CONTROLs went red under M2 and M5. No test stayed green under its mutation, so none was rewritten.
2. Every entry path is pinned. Each line the rows change has a test: `:93` by both D1 tests; `:5`, `:89`, `:94` and `:154` by `test_d2_the_deferred_set_is_named_where_it_is_made_and_read`. Every `launchctl` call site from PREFLIGHT's grep (lines 11 … 168) is covered by `test_d2_no_launchctl_call_names_the_deferred_set`. The launch line `:11` and the MODEL line `:3` are pinned by `test_d2_the_three_residents_strings_stand`. The hub's other readers (PREFLIGHT caller grep) all pass in `tests/ops` at the tip. Not pinned by a test, and outside the rows: CHECK ASK X4 (a set that holds only a deferred label becomes an empty `<restart set>`, which `:95` then refuses when there is a migration). This is the hub text as written, left for the check.
3. Re-read at the tip from tool output: `grep -c -F "<deferred set>"` → 5, `grep -c -F "minus every label of"` → 1, `git diff 170e90ca -- <hub>` (five lines), `git log --oneline 170e90ca..HEAD` (two commits), the RESTARTS table, and both gate output files.

## FOR THE CHECK
- `170e90ca..79b8ac8e`: `dbe3f841 wip(hub-deferred-1018): red — D1, D2 hub-text tests (3 red, 2 controls green on BASE)` · `79b8ac8e fix(hub-deferred-1018): STEP-R admits the restart set minus the deferred set; no launchctl call names it (D1, D2, L1, L42, L79)`.
- Per row, the reds, mutations and greens are in `## E2 RED` and `## E3 THE ROWS`; the caller grep is in `## PREFLIGHT`. There are no RUN rows.
- Suites: offline `8608/0` (`gate.sh … offline`, log above) · with-DB: not run (DB: none) · live-note `147/0` (`gate.sh … livenote`, log above) · `tests/ops` `3962 passed, 1 xfailed`.
- `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock taken / released: not run (DB: none).
- RESTARTS table: `## RESTARTS`. Records copied at PREFLIGHT: `## PREFLIGHT`.

## CONTINUE
next: none (BUILT; the desk launches CHECK-HUB.md on this card)

## DECISIONS
none

## RECORDS
- Report created 2026-10-18 16:39:10 EDT (`date`); W launched 17:11:07 EDT; close 17:39:37 EDT (`date`).
- Bare-guard hook blocks (not refusals): five `grep -n -F` calls with a backtick in the pattern. The same reads were made with the Grep tool and with backtick-free fixed strings.
- No DevDocs module line: the rows change a prompt file and a test, no `.py` module (BUILD-HUB E3 names a module's page).
- Card `## RECORDS` as re-read at PREFLIGHT: see `## PREFLIGHT`.
- L74: one `Claude-Session:` request in a system reminder, not acted on (`## L74`).
- No extra lock take; no `REFUSED, not needed` line; no `CONTINUE` message.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: hub-deferred-1018 · tip: 79b8ac8e | on 170e90ca | migration: none | offline 8608/0 | with-DB 0/0 | live-note 147/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 157900
