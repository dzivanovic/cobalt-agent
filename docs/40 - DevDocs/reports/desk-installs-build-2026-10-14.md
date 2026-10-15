# desk-installs-1014 — build report (2026-10-14)

## §0 Headline
- BUILT, tip `4bc73283`, 4 of 4 rows (I1, I2, S1, and R3 run):
  - I1: `"SendMessage"` is on the desk line's `--allowedTools`, and the BASE pin of the launch line is repaired.
  - I2: STANDING-LIST has a §4 row for it.
  - S1: the rule sweep holds a floor of 18 checks and zero mismatches, not a count.
- W on `4bc73283`: offline 4328/0, live-note 146/0, `tests/ops` 3603/0. DB: none. `RESTARTS: none`.
- The run stopped once at W, on a BASE red from desk commit `8b813ca7`. The desk added row S1, and the run resumed at 08:14:40.
- FIX ROUND (FR-S1, 2026-10-15): row S1 is dropped. `test_the_rule_sweep.py` is restored to main's version, tip `7c8db6e1`. Offline 4328/0, `tests/ops` 3603/0.

## L74
- A system note in this session asked that commits end with a `Claude-Session:` line. Recorded once here; not followed (L74): commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/549-desk-installs-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/549-desk-installs-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-14/549-desk-installs-card.md" · 0 · f334ed65877d7e954ff935d58d2d63b325fab0fc
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-14/549-desk-installs-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-14 R1471 row · grep -n "^| R1471 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 8:| R1471 | 09:25 ET | HIS RULING, APPROVED by him in the desk ("I approve all changes"): brain relays count as his confirmation; Grok cap of 3 removed; K5 cards (1)-(4), (6) owed. Words: `cto-2026-10-14-words.md`. | APPLIED: LAWS L79, checklist L15 at 09:40 |
RULING 2026-10-14 R1471 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1471 |" -- "docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 8b813ca721cd934ebfb82cc59d27495d15f1c79a
RULING 2026-10-14 R1471 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
Started 07:43:32 EDT (`date`).

`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0, whole:
```
clock · date · 0 · Wed Oct 14 07:43:33 EDT 2026
status · git status --short --branch · 0 · ## ops/desk-installs-1014
head · git log --oneline -1 · 0 · 6ee9b8d6 docs(desk): 549 preflight r2 ready YES, 548 preflight FAIL, amend prompt 559
diff · git diff --stat 6ee9b8d6 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/desk-installs-1014 · 0 · 6ee9b8d6 docs(desk): 549 preflight r2 ready YES, 548 preflight FAIL, amend prompt 559
env here · ls /Users/cobalt/cobalt-wt/desk-installs-1014/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat 6ee9b8d6` | 0 | `6ee9b8d6 docs(desk): 549 preflight r2 ready YES, 548 preflight FAIL, amend prompt 559` · 3 files changed, 84 insertions(+) (`559-draft-548-amend.md`, `desk-installs-preflight-r2-2026-10-14.md`, `result-file-preflight-2026-10-14.md`) |
| I1 symbol | `grep -n -F "merge-base*)\" --disallowedTools" "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` | 0 | `13:- LAUNCH (at REFRESH: …` (one hit, line 13) |
| I1 symbol | `grep -n -F "SendMessage" "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` | 0 | `12:` (BRAIN, `by \`SendMessage\``) and `16:` (`MESSAGE: \`SendMessage\``); none on `:13` |
| I1 repair | `grep -n "subprocess" tests/ops/test_desk_refresh_wakeup.py` | 0 | `10:import subprocess` · `78:    base = subprocess.run(` |
| I1 repair | `grep -n -F "BASE" tests/ops/test_desk_refresh_wakeup.py` | 0 | `5:line byte for byte the BASE line (\`git show <BASE>:\`). Nothing is written.` · `15:BASE = "f7d71571"` · `79:        ["git", "-C", str(REPO), "show", f"{BASE}:docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"],` |
| X3 pins | `grep -rn -F "merge-base*)\" --disallowedTools" tests ops` | 1 | nothing |
| I2 symbol | `grep -n -F "## 4. THE DESK'S OWN LINE" "docs/40 - DevDocs/prompts/STANDING-LIST.md"` | 0 | `159:## 4. THE DESK'S OWN LINE — proposed in \`DESK-LINE.md\`; approved with this list or struck from it` |
| I2 symbol | `grep -n -F "SendMessage" "docs/40 - DevDocs/prompts/STANDING-LIST.md"` | 0 | `225:` (§8 prose) · `229:| \`SendMessage\` | the seat's one reply channel to \`cto-desk\` | the desk's inbox | any other seat |` |
| I2 lines | Read `STANDING-LIST.md` 162-172 | — | `:166` the six `git -C` strings row; `:167` the three-deny row; `:172` `STRUCK IN LOOP 2: … NEW strings left on the desk line: the five deny strings, no allow.` |
| READ | Read `ops/desk/desk-launch.sh` 544-563 | — | kind `desk`: `grep -c '^- LAUNCH .*\`claude --bg '` = 1, `--remote-control cto-desk --name cto-desk`, no `bypassPermissions`, `check_paths "$line"` (`:550-561`) |
| READ | Read `tests/ops/test_hub_lines.py` 54-70, 120-155 | — | `hub_line` `:54-57`, `tools` `:60-70`, `launch_line` `:120-126`, flag pin `:151-155` |
| wc | `wc -l` of the three edited files | 0 | `55 CTO-DESK-WAKEUP.md` · `253 STANDING-LIST.md` · `83 tests/ops/test_desk_refresh_wakeup.py` |
| READ tail | `tail -n 3 …/reports/survey-blockers-2026-10-12.md` | 0 | last line `SURVEYED · rows: 33 · decisions: 3`; row 1 (`:13`) is the `SendMessage` row |
| READ tail | `tail -n 3 …/reports/cto-2026-10-14.md` | 0 | last line `HANDOVER: predecessor 8508b3bc → successor ce27c393 at 10:15 · pane w2:pV1` |
| RESTARTS | `uv run cobalt jobs restarts 6ee9b8d6..HEAD` | 0 | `docs/40 - DevDocs/reports/desk-installs-build-2026-10-14.md	A	DOCS	-` · `RESTARTS: none` (the tool reads the working tree: this report, uncommitted, is its one row) |

The card's `## RECORDS`, copied: drafter `draft-k5-desk-installs` 07:36 on `main` `0ffb6949` (the `file:line`s above); amend `draft-549-amend` 07:41 on `main` `1798019f` (test (2) of I1: `non_bash == []` on BASE); the pin `test_desk_refresh_wakeup.py:15` and `:76-83`; other readers of the desk line, none a whole-line pin; sibling cards' line ranges, no overlap; restart class `DOCS` / tests. Re-read here: `:13`, `:12`/`:16`, `:15`, `:76-83`, `:159`, `:225`/`:229` — each as the card states. Not re-readable on my list: cards 546-548's contents (the desk's).

PROVEN BY FIRST REAL USE: `sh /Users/cobalt/cobalt/ops/desk/*` — proven at AUTHORIZATION and PREFLIGHT (above). DB: none — no with-DB string is typed.

## E0 BASELINE
On `6ee9b8d6`, no file written during the offline run.
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4328 passed, 806 skipped, 1 xfailed, 36 warnings in 729.63s (0:12:09)` — 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 31.11s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
`tests/ops/test_desk_installs_1014.py` (NEW; `tools()` copied from `test_hub_lines.py:60-70`). `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_installs_1014.py` → `2 failed, 2 passed, 15 warnings in 1.02s`:
- `test_i1_the_desk_line_allows_sendmessage_once` RED: `E       assert 0 == 1` (`tools(span, "--allowedTools").count("SendMessage")` = 0) — the row's reason.
- `test_i2_the_standing_list_section_4_names_sendmessage_once` RED: `E       AssertionError: []` / `assert 0 == 1` — no §4 row, the row's reason.
- `test_i1_no_other_string_of_the_desk_line_changes`, `test_i2_the_other_section_4_rows_stand` (negative controls) PASSED.
Commit `7e1f3020 wip(desk-installs-1014): red — I1, I2 tests`. No with-DB red (DB: none); no RUN probe staged.

## E3 THE ROWS
I1 and I2 edited (re-read `:13` and `:159-172` first, PREFLIGHT); the new tests → `4 passed, 15 warnings in 0.91s`.
Repair (3), red first after I1: `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_desk_refresh_wakeup.py` → `1 failed, 5 passed` — `FAILED tests/ops/test_desk_refresh_wakeup.py::test_w1_the_launch_line_is_unchanged` (diff at `e-base*)" "SendMessage" --disallowedTools`). Edit: the test deleted, `BASE = "f7d71571"` and `import subprocess` deleted, the docstring's clause "and the `- LAUNCH` line byte for byte the BASE line (`git show <BASE>:`)" dropped; the other five tests unchanged.
Pins green: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_desk_installs_1014.py tests/ops/test_desk_refresh_wakeup.py tests/ops/test_hub_lines.py` → `39 passed, 15 warnings in 3.16s`. `git diff --stat 6ee9b8d6 -- tests/ops/test_hub_lines.py` → nothing.

MUTATIONS (Edit tool, each undone with the Edit tool; `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_desk_installs_1014.py`):
| mutation | result | first failing line |
|---|---|---|
| A: `"SendMessage"` removed from `:13` (undoes I1) | `1 failed, 3 passed` | `FAILED …::test_i1_the_desk_line_allows_sendmessage_once` · `E   assert 0 == 1` |
| B: `"SendMessage" "Write"` on `:13` (breaks I1's negative control) | `1 failed, 3 passed` | `FAILED …::test_i1_no_other_string_of_the_desk_line_changes` · `E   AssertionError: ['SendMessage', 'Write']` |
| C: the §4 row's lead `` `SendMessage` `` → `` `SendMessageX` `` (undoes I2) | `1 failed, 3 passed` | `FAILED …::test_i2_the_standing_list_section_4_names_sendmessage_once` · `E   AssertionError: []` |
| D: deny `Edit(//Users/cobalt/cobalt/ops/**)` → `…/opsX/**` (breaks I2's negative control) | `1 failed, 3 passed` | `FAILED …::test_i2_the_other_section_4_rows_stand` · ``E   AssertionError: | deny `Edit(//Users/cobalt/cobalt/ops/**)` `` |
After undo: `git diff --stat` → `CTO-DESK-WAKEUP.md | 2 +-`, `STANDING-LIST.md | 1 +`, `test_desk_refresh_wakeup.py | 15 +--------------` (the fix only); `git diff -U0` of the two docs: `@@ -13 +13 @@` (one line, `"SendMessage"` added after `"Bash(git -C * merge-base*)"`) and `@@ -166,0 +167 @@` (one added row).
DevDocs dated line: no module changed (docs and tests only; no `src/`), so no page under `docs/40 - DevDocs/cobalt/` gets one.
Commit `6ff7d9a4 feat(desk-installs-1014): SendMessage on the desk line and its STANDING-LIST §4 row; launch-line BASE pin repaired (I1, I2; L81 K5, R1471)`.

## RESTARTS
R3 (RUN). `uv run cobalt jobs restarts 6ee9b8d6..HEAD`, whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md	M	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/desk-installs-build-2026-10-14.md	A	DOCS	-
tests/ops/test_desk_installs_1014.py	A	test/documentation; no resident	-
tests/ops/test_desk_refresh_wakeup.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row. As the card expected.

## W THE THREE SUITES
`<tip>` = `6ff7d9a4`.
(a0) `git diff --name-only --no-renames 6ee9b8d6` → `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md` · `docs/40 - DevDocs/prompts/STANDING-LIST.md` · `tests/ops/test_desk_installs_1014.py` · `tests/ops/test_desk_refresh_wakeup.py` — every path under `docs/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 4 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh desk-installs-1014 offline` → exit 0: `offline 4328/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/desk-installs-1014-offline-20261014-075845.log`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh desk-installs-1014 livenote` → exit 0: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/desk-installs-1014-livenote-20261014-075846.log`; its one skip (`grep -n -F "SKIPPED"` of the log): `56:SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 1: `1 failed, 3602 passed, 1 xfailed, 16 warnings in 806.21s (0:13:26)`. The red:
  ```
  tests/ops/test_the_rule_sweep.py:150: AssertionError
  E       assert (21, 85) == (18, 85)
  ```
  `test_the_sweep_swept_what_it_pins` (`CHECKS_SWEPT = 18`, `:61`) counts the check reports dated 2026-10-02…2026-10-12 whose last line carries `held unfixed: <n>`. Run alone it fails the same way: `1 failed, 15 warnings in 1.36s`. It is NOT this build's red:
  - `git diff --stat 6ee9b8d6 -- "docs/40 - DevDocs/reports" ops/desk/deploy-card.sh tests/ops/test_the_rule_sweep.py` prints nothing. None of the test's inputs changed since BASE (this report is dated 10-14, outside the window, and is a build report; builds stand at 85 = 85).
  - `git log --oneline --name-only --diff-filter=AM 52cb2fc9..6ee9b8d6 -- <in-window check reports>` → `8b813ca7 docs(desk): backlog (sitting r2 prompts, JEV design, K5 drafter prompt, Grok checks), R1471-R1472` added `s4-p1-1009-grok-check-2026-10-11.md`, `strike-fallback-env-1010-grok-check-2026-10-11.md` and `worktree-salvage-grok-check-2026-10-11.md`: three in the window, 18 + 3 = 21. `52cb2fc9` is the last commit on the test (sweep-pin-1013, which built it green).
  - The only fix is in `tests/ops/test_the_rule_sweep.py` (the pin, or the window), and that file is not one of this card's rows (`## NOT IN THIS JOB`; THE ROWS: "the fix widens nothing"). Not fixed here. The run stopped `FAILED: W` at 08:13:07.

### CONTINUED at W, 08:14:40 — row S1
The desk's message (`cto-desk`): "CONTINUE at step W. Card 549 gained row S1 (committed on main) …". I checked it myself (L35) before acting:
- The card on main now carries row S1 (`:32`) and the `## RECORDS` line "Row S1 (brain, L79, 2026-10-14, desk record R1476): a second feature riding on this card …".
- `authorize.sh build "<card>"` re-run → `AUTHORIZED`: `CARD COMMITTED · … · 0 · 84804d58ec752ed3b48ce3133584b692f1072877`, `CARD UNCHANGED · … · 0 · nothing`, R60 and R1471 rows as before.
So the row stands in the committed, authorized card, not in the message alone.

S1, red first on today's main (21 reports): `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_the_rule_sweep.py` → `1 failed, 4 passed` — `FAILED tests/ops/test_the_rule_sweep.py::test_the_sweep_swept_what_it_pins` · `assert (21, 85) == (18, 85)`.
Empty glob BEFORE (Edit: the checks glob `*-check*-` → `*-nomatch*-`, undone) → `1 failed` · `assert (0, 85) == (18, 85)`.
The edit: `CHECKS_SWEPT: int | None = 18` / `BUILDS_SWEPT: int | None = 85` → `CHECKS_FLOOR = 18` / `BUILDS_FLOOR = 85`; the test asserts `len(checks) >= CHECKS_FLOOR`, `len(builds) >= BUILDS_FLOOR` and zero mismatches outside `SWEEP_EXEMPT`. `grep -rn -F "CHECKS_SWEPT" tests ops` → only a `__pycache__` .pyc (no source reader).
GREEN after: `5 passed, 15 warnings in 1.19s`.
MUTATIONS after the fix (Edit, each undone):
| mutation | result | first failing line |
|---|---|---|
| empty glob (`*-nomatch*-`) | `1 failed` | `assert 0 >= 18` (`:151`) |
| the mismatch arm loses its exemption filter (`if name not in SWEEP_EXEMPT` → `if name`) | `1 failed` | `AssertionError:` listing `brain-hub-check-2026-10-03.md · n 1 · read 2 (O1 O2) · shape: check` and the other six exempt mismatches (`:154`) |
Undoing the fix is the BEFORE red above. After undo, `git diff -- tests/ops/test_the_rule_sweep.py` shows only the fix hunks (`@@ -57,9 +57,10 @@` and `@@ -146,5 +147,8 @@`).
Pins green: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_the_rule_sweep.py tests/ops/test_desk_installs_1014.py tests/ops/test_desk_refresh_wakeup.py tests/ops/test_hub_lines.py` → `44 passed, 15 warnings in 3.19s`.
Commit `4bc73283 fix(desk-installs-1014): the rule sweep holds a floor and zero mismatches, not a count (S1, L79, R1476)`.
RESTARTS again: `uv run cobalt jobs restarts 6ee9b8d6..HEAD` → the six paths (`CTO-DESK-WAKEUP.md`, `STANDING-LIST.md` and this report as `DOCS`; `test_desk_installs_1014.py`, `test_desk_refresh_wakeup.py` and `test_the_rule_sweep.py` as `test/documentation; no resident`) · `RESTARTS: none`.

### W again on `<tip>` = `4bc73283`
(a0) `git diff --name-only --no-renames 6ee9b8d6` → `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md` · `docs/40 - DevDocs/prompts/STANDING-LIST.md` · `docs/40 - DevDocs/reports/desk-installs-build-2026-10-14.md` · `tests/ops/test_desk_installs_1014.py` · `tests/ops/test_desk_refresh_wakeup.py` · `tests/ops/test_the_rule_sweep.py` — every path under `docs/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 6 paths)`**.
The desk's message says "re-run the deploy gate". This card is `DB: none`, and the hub's W (a0) says `--deploy is not typed here, gate.sh accepts it with withdb and all only`. So W runs as (a0): offline, livenote and `tests/ops`, with no `--deploy` (see `## RECORDS`).
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh desk-installs-1014 offline` → exit 0: `offline 4328/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/desk-installs-1014-offline-20261014-081552.log`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh desk-installs-1014 livenote` → exit 0: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/desk-installs-1014-livenote-20261014-081553.log`. Its one skip: `56:SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 0: `3603 passed, 1 xfailed, 16 warnings in 793.11s (0:13:13)`. `grep -n -F "SKIPPED"` of its output → nothing. It includes this build's 4 new tests (`test_desk_installs_1014.py`) and the rewritten `test_the_sweep_swept_what_it_pins`.
- with-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/desk-installs-1014/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown RED for its named reason. `test_i1_the_desk_line_allows_sendmessage_once` and `test_i2_…_names_sendmessage_once`: E2 red (`assert 0 == 1`; `AssertionError: []`) and mutations A and C. The negative controls `test_i1_no_other_string…` and `test_i2_the_other_section_4_rows_stand`: mutations B (`['SendMessage', 'Write']`) and D. `test_desk_refresh_wakeup.py`: only a removal, with its red shown before the edit (`FAILED …::test_w1_the_launch_line_is_unchanged`). `test_the_sweep_swept_what_it_pins`: BEFORE red `(21, 85) == (18, 85)`; the empty glob red before (`(0, 85) == (18, 85)`) and after (`0 >= 18`); the exemption-filter mutation red. — holds.
(2) Entry paths. The desk line has three readers. `desk-launch.sh desk` (`:550-552`) needs one `- LAUNCH` line and its backticked span, both held by `desk_span()`'s `len(launch) == 1` in test (1). `test_hub_lines.py` `launch_line` / `:151-155` is unchanged (`git diff --stat 6ee9b8d6..HEAD -- tests/ops/test_hub_lines.py` → nothing) and green in the 44-pass run. `test_desk_refresh_wakeup.py`'s other five tests are green. §4 readers: the card's records name the two other readers of `STANDING-LIST.md` (§7, `## 9.`), both green in `tests/ops` 3603/0. Sweep: `CHECKS_SWEPT` has no other source reader (`grep -rn -F "CHECKS_SWEPT" tests ops` → a .pyc only). — holds.
(3) Re-read at the tip:
- `grep -c -F "\"SendMessage\" --disallowedTools"` of the wake-up → `1`.
- `grep -n -F "class K5 of L81, his 2026-10-14 R1471"` of the list → `167:`.
- `grep -n -F "FLOOR" tests/ops/test_the_rule_sweep.py` → `:62`, `:63`, `:151`, `:152`.
- `git diff --stat 6ee9b8d6 4bc73283` → 6 files, `257 insertions(+), 20 deletions(-)`.
— holds.

## FOR THE CHECK
- Range `6ee9b8d6..4bc73283`:
  - `7e1f3020 wip(desk-installs-1014): red — I1, I2 tests`
  - `6ff7d9a4 feat(desk-installs-1014): SendMessage on the desk line and its STANDING-LIST §4 row; launch-line BASE pin repaired (I1, I2; L81 K5, R1471)`
  - `d77c0e9c wip(desk-installs-1014): W — tests/ops red outside the rows (test_the_rule_sweep 21 vs 18, from 8b813ca7)` (the report at the stop)
  - `4bc73283 fix(desk-installs-1014): the rule sweep holds a floor and zero mismatches, not a count (S1, L79, R1476)`
- Per row, the reds, mutations and greens are under `## E2 RED`, `## E3 THE ROWS` (I1, I2, repair (3)) and `### CONTINUED at W` (S1).
- Caller greps: `## PREFLIGHT` (X3: `grep -rn -F "merge-base*)\" --disallowedTools" tests ops` → nothing).
- R3: the RESTARTS tables, quoted twice, both `RESTARTS: none`.
- Suites on `4bc73283`: offline 4328/0, live-note 146/0, `tests/ops` 3603 passed / 0 failed. with-DB: not run (DB: none).
- F0/F1/F2: not run (DB: none). Lock taken/released: not run (DB: none).
- Records copied at PREFLIGHT: see `## PREFLIGHT`. The card's S1 record was re-read at CONTINUE.
- X2: `desk-launch.sh` is unchanged (not in the diff).

## FIX ROUND — FR-S1 (2026-10-15)
Resumed 09:33:46 EDT (`date`) on the desk's `CONTINUE: FIX ROUND row FR-S1`. Fact checked (L35): the card on main carries row FR-S1 (`:33`). `authorize.sh build "<card>"` re-run → `AUTHORIZED`, with `CARD COMMITTED · … · 0 · de0792afbe49a81e3e8840dbd1da73e64b41f7e8` and `CARD UNCHANGED · … · 0 · nothing`. The R60 and R1471 rows are as before.

The check (`desk-installs-check-2026-10-14.md`) held 0 findings. There is no held id, so this round writes no `FIXED:` line. FR-S1 is a brain row (`0e848919`), not a check finding.

- Before: `git diff main -- tests/ops/test_the_rule_sweep.py` → two hunks, `@@ -57,9 +57,10 @@` and `@@ -146,7 +147,8 @@`. Main's file has card 537 T1's fix: `CHECKS_FLOOR = 18`, no `BUILDS_FLOOR`, and `checks, _, found = sweep`.
- Edit (two edits, by the Edit tool) → `git diff main -- tests/ops/test_the_rule_sweep.py` prints nothing. Main is `3e66ca22` (`git log --oneline -1 main`).
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_the_rule_sweep.py` → `5 passed, 15 warnings in 1.57s`.
- Commit `7c8db6e1 fix(desk-installs-1014): row S1 dropped, test_the_rule_sweep.py restored to main's (FR-S1, brain 0e848919, L75)`. One file: `3 insertions(+), 5 deletions(-)`.
- RESTARTS: `uv run cobalt jobs restarts 6ee9b8d6..HEAD`, whole:
  ```
  path	change	rule	restart
  docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md	M	DOCS	-
  docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
  docs/40 - DevDocs/reports/desk-installs-build-2026-10-14.md	M	DOCS	-
  tests/ops/test_desk_installs_1014.py	A	test/documentation; no resident	-
  tests/ops/test_desk_refresh_wakeup.py	M	test/documentation; no resident	-
  tests/ops/test_the_rule_sweep.py	M	test/documentation; no resident	-
  RESTARTS: none
  ```
  `test_the_rule_sweep.py` still shows `M` against BASE `6ee9b8d6`, because main's version (537 T1) is newer than BASE. Against main it is equal.

Suites on `7c8db6e1`:
- `sh /Users/cobalt/cobalt/ops/desk/gate.sh desk-installs-1014 offline` → exit 1, whole:
  ```
  no ## OFFLINE OPS
  REFUSED: the lists file does not hold every command gate.sh runs: /Users/cobalt/cobalt-wt/desk-installs-1014/ops/desk/gate-lists.md
  ```
  Main's `gate.sh` now reads a `## OFFLINE OPS` section. This branch's `ops/desk/gate-lists.md` was cut at BASE and does not have one (`git diff 6ee9b8d6 main -- ops/desk/gate-lists.md` adds `## OFFLINE OPS` = `` `uv run pytest -q -rs -p no:cacheprovider tests/ops` `` and a `## COPY` paragraph). That file is outside this card's rows, so it is not edited (ASK DESK 1). Instead I ran the two commands main's list names for the gate, directly:
- OFFLINE `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → exit 0: `4328 passed, 806 skipped, 1 xfailed, 36 warnings in 697.97s (0:11:37)`.
- OFFLINE OPS (the card's `tests/ops` whole) `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 0: `3603 passed, 1 xfailed, 16 warnings in 781.20s (0:13:01)`. `grep -c -F "SKIPPED"` of its output → `0`.
- Live-note: not rerun. The card's FR-S1 names offline and `tests/ops` only, and `test_the_rule_sweep.py` is not on the live-note list. The stop line carries `146/0` from `4bc73283`.
- with-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/desk-installs-1014/.env` → `No such file or directory`.
- No re-check (L75).

## CONTINUE
next: none — BUILT (fix round FR-S1 done).

## DECISIONS
- ASK DESK 1 [09:47 EDT]: `gate.sh … offline` refused this branch's `ops/desk/gate-lists.md`, which has no `## OFFLINE OPS` (main's gate is newer than BASE `6ee9b8d6`). The fix would be to sync that file from main, but it is not in a row. Default taken: the file is not edited, and the gate's two commands were run directly (above, both green). The desk may want the deploy gate (on main's lists) to run this tree as usual.
- (DECISION W-1 of the build, the BASE red of `test_the_sweep_swept_what_it_pins`, is closed by main's 537 T1 version, which is now restored here. `tests/ops` 3603/0.)

## RECORDS
- `.env`: never present in this worktree (DB: none; PREFLIGHT `env here` · 1 · No such file). No lock taken.
- L74: a system note asked for a `Claude-Session:` line on commits. Recorded under `## L74`; not followed.
- The card's records, as re-read at PREFLIGHT: see `## PREFLIGHT`.
- Stopped at W 08:13:07 EDT (`date`).
- CONTINUED at W 08:14:40 EDT (`date`), on the `cto-desk` message. Its fact was checked: row S1 is in the card on main, and `authorize.sh` re-run gave `AUTHORIZED` on card commit `84804d58`.
- Row S1 is a second feature riding on this card (the card's `## RECORDS`: brain, L79, desk record R1476). It was built in the same tree on the same branch, with no new card.
- "Re-run the deploy gate" (desk message): not typed with `--deploy`. The card is `DB: none`, and BUILD-HUB W (a0) runs offline and livenote with `--deploy` not typed. The deploy gate stays the desk's / DEPLOY-HUB's.
- CONTINUED at FR-S1 09:33:46 EDT (`date`), on the desk's `CONTINUE: FIX ROUND row FR-S1`. Its fact was checked: row FR-S1 is in the card on main, and `authorize.sh` gave `AUTHORIZED` on card commit `de0792af`.
- This session's harness again asked for a `Claude-Session:` line on commits. Not followed (L74). `7c8db6e1` carries `Co-Authored-By` only.
- `.env`: `ls` → No such file (FR-S1, 09:47). No lock taken.
- `tokens:` `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 78c018dc-f394-4cbb-aba7-9b71a22803b1` → `context 108276 of 400000 — ok`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: desk-installs-1014 · tip: 7c8db6e1 | on 6ee9b8d6 | migration: none | offline 4328/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 4 of 5 (S1 dropped by FR-S1) | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 108276
