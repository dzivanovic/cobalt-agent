# stop-guard-g7-1009 — build report 2026-10-09

## §0 Headline
- G7 built on `b8047e79`: the desk's stop is blocked by a `§5 CURRENT` QUEUE row, by a `waiting on Dejan` item without `R<n>`, and by a desk item settled only by the brain's id.
- 3 reds shown on BASE, 5 mutations red, 82/82 in the file; offline 4036/0, tests/ops 2088 passed, live-note 146/0; DB: none.
- One decision: two G7a edges untested by the card's limit.

## L74
- 11:48 ET: a system reminder asked for a `Claude-Session:` line on commits. Recorded as data; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/164-stop-guard-g7-card.md"` (11:48 ET), exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/164-stop-guard-g7-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/164-stop-guard-g7-card.md" · 0 · 9db1211c094f7b7e5cba3c1bdbe89fcc6ff17300
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/164-stop-guard-g7-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
rule · command · exit · output
- mechanical · `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` · 0 ·
```
clock · date · 0 · Fri Oct  9 11:49:00 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/stop-guard-g7-1009
    ?? "docs/40 - DevDocs/reports/stop-guard-g7-build-2026-10-09.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 1458693d docs(desk): drafts 152 and 154, preflight and drafter prompts, brain answers, desk 10-09 report
diff · git diff --stat 1458693d · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/stop-guard-g7-1009 · 0 · 1458693d docs(desk): drafts 152 and 154, preflight and drafter prompts, brain answers, desk 10-09 report
env here · ls /Users/cobalt/cobalt-wt/stop-guard-g7-1009/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
- base · `git show --stat 1458693d` · 0 · `commit 1458693dbde5371259a29c5d502d74e3878fee3b` · `docs(desk): drafts 152 and 154, preflight and drafter prompts, brain answers, desk 10-09 report` · `17 files changed, 548 insertions(+), 1 deletion(-)` (all under `docs/40 - DevDocs/`).
- symbols (each `grep -n -F`, exit 0):
  - `def unsettled` ops/desk/stop-guard.py → `269:def unsettled(items):`
  - `def owed_block` → `198:def owed_block(report):`
  - `marker == WAITING` → `274:        if marker == WAITING:`
  - `cto-desk` → `25:# <id> 8+ chars of [0-9a-f-], not named cto-desk) and PGREP below (a line containing <path>).` · `289:                if any(i.startswith(sid) and name != "cto-desk" for i, name in seen["list"]):`
  - callers `unsettled(` → `269:def unsettled(items):` · `313:            what = unsettled(items)` (one caller, `desk`)
  - `def owed` tests/ops/test_stop_guard.py → `306:    def owed(self, *block: str, heading: str = "## §5 CURRENT") -> None:`
  - `waiting on Dejan` tests → `409` `OWED: fold R1 | waiting on Dejan` · `456` `OWED: a | waiting on Dejan", "OWED: b` · `564` `OWED: w | waiting on Dejan", "OWED: a", "OWED: b` · `586` (two-bars, fails open at parse) · `587` (none-beside-an-item, fails open at parse) · `675` (fails open at parse)
  - `--name brain` prompts/BRAIN-HUB.md → `8:claude --bg … --remote-control brain --name brain …`
  - Read tool: stop-guard.py `:20-26` header, `:89-96` constants, `:198-241` owed_block, `:244-292` listed/watched/unsettled, `:295-330` desk — as the card gives them. tests `:262-334`, `:400-460`, `:464-486`, `:562-566`, `:672-682` — as the card gives them.
- `wc -l ops/desk/stop-guard.py tests/ops/test_stop_guard.py` → `371` · `702`.
- `tail -n 3 desk-idle-answer-2026-10-09.md` → last line `- The card 134 check: \`aa94b309\` is closed. The new brain judges the 134 draft's DECISIONS when the desk sends them.` Its `## CARD ROW` (line 18) G7 (a)(b)(c) matches the card's rows.
- `uv run cobalt jobs restarts 1458693d..HEAD` · 0 ·
```
path	change	rule	restart
docs/40 - DevDocs/reports/stop-guard-g7-build-2026-10-09.md	A	DOCS	-
RESTARTS: none
```
- RECORDS re-read:
  - BASE `1458693d…`: `git show --stat` above → `1458693dbde5371259a29c5d502d74e3878fee3b`.
  - `desk-list.sh` prints `id · name · cwd · status · state`: `ops/desk/desk-list.sh:3` `# one line each: id · name · cwd · status · state.`, `:16` `print(a['id'], a.get('name','?'), …, sep=' · ')`. `listed()` at `stop-guard.py:254-255` keeps `(f[0], f[1])`.
  - three QUEUE rows: this worktree's (BASE) `reports/cto-2026-10-09.md:35-37` each start `| QUEUE`. The main checkout's copy no longer holds them (`grep -n -F "QUEUE"` → only `17:| R724 …`): the desk has since turned them over; the code does not depend on it.
  - RESTARTS classes: `grep -c -F "ops/desk" configs/cobalt/jobs.yaml` → `0`.
  - WHERE IT RUNS: `stop-guard.py:47` `{"hooks": [{"type": "command", "command": "python3 /Users/cobalt/cobalt/ops/desk/stop-guard.py"}]}`.
  - ORDER (after https-only deploys): the desk's fact; not re-readable from this list.
- DB: none — no lock probe; no with-DB string is used in this build.

## E0 BASELINE
- offline `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `1458693d` → `4036 passed, 790 skipped, 1 xfailed, 36 warnings in 677.68s (0:11:17)` (exit 0; 0 failed, 0 errors; its last SKIPPED line `tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof`, the offline run's expected skip).
- live-note `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 31.36s`; the skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
T0 (fixture `rows=`, `:456` and `:564` gain `(asked R1)`) and five new tests, no `src/` or `ops/` edit. Against BASE's `ops/desk/stop-guard.py`: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stop_guard.py` → `3 failed, 79 passed, 15 warnings in 24.49s`. Each red fails for its row's reason (BASE lets the stop through, exit 0):
- (a) `test_g7a_a_queue_row_in_current_blocks` → `E       AssertionError: assert (0, '', '') == (2, '', 'start it: x card\n')`
- (b) `test_g7b_waiting_on_him_without_a_row_blocks` → `E       AssertionError: assert (0, '', '') == (2, '', 'star...: build 72\n')`
- (c) `test_g7c_the_brains_id_on_a_desk_item_blocks` → `E       AssertionError: assert (0, '', '') == (2, '', 'star...https card\n')`
- controls `test_g7b_waiting_on_him_with_a_row_lets_the_turn_end`, `test_g7c_the_brains_id_on_a_brain_item_lets_the_turn_end`: passed on BASE (among the 79). T0's touched tests `test_g2_the_block_before_a_blank_line_and_the_table_is_read_as_the_block`, `test_g4_the_first_unsettled_item_is_named`: passed on BASE.
- commit `3acc92f8 wip(stop-guard-g7-1009): red — G7 a/b/c reds, two controls, T0 fixture`.

## E3 THE ROWS
Rows in order, `ops/desk/stop-guard.py` only (plus T0 in the test file at E2).
- G7a: `report_lines(report)` is the one read (the read and its two fail-open lines, unchanged, moved out of `owed_block`, which now takes the lines); `queued(lines)` returns the first `|` row under `## §5 CURRENT`, before the next `## ` line, whose first cell starts `QUEUE` → its third cell, stripped (fewer than three cells → the row, stripped); `desk` calls it only when `unsettled` returns None. A missing block keeps the `start it: the OWED block …` message. After G7a: `2 failed, 80 passed` (the two unbuilt rows G7b, G7c).
- G7b: `ASKED = re.compile(r"\bR\d+\b")`; a `waiting on Dejan` item without it → `unsettled` returns `ask him: <what>`; `desk` prints `start it: %s` unchanged.
- G7c: `BRAIN = "brain"`; a matching row settles when its name is neither `cto-desk` nor `brain`, or is `brain` and `"brain" in what`.
- Header `:20-29` and `unsettled`'s docstring name the rules (card 164 G7; his 2026-10-09 R724).
- After all rows: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_stop_guard.py` → `82 passed, 15 warnings in 24.53s`.
- MUTATIONS (Edit tool, each undone; `--tb=line`, `-k` the row's tests):
  - M1 G7a undone (`what = queued(lines)` → `what = None`), `-k g7a` → `1 failed, 81 deselected`: `tests/ops/test_stop_guard.py:716: AssertionError: assert (0, '', '') == (2, '', 'start it: x card\n')`
  - M2 G7b undone (waiting → bare `continue`), `-k g7b` → `1 failed, 1 passed, 80 deselected`: `tests/ops/test_stop_guard.py:723: AssertionError: assert (0, '', '') == (2, '', 'star...: build 72\n')`
  - M3 G7b control (`ASKED = re.compile(r"(?!x)x")`, matches nothing), `-k g7b` → `1 failed, 1 passed, 80 deselected`: `tests/ops/test_stop_guard.py:730: AssertionError: assert (2, '', 'star...sked R722)\n') == (0, '', '')`
  - M4 G7c undone (`and name != "cto-desk"`), `-k "g7c or test_g3_a_live_session_id_lets_the_turn_end or test_g3_the_desks_own_row_is_not_live"` → `1 failed, 3 passed, 78 deselected`: `tests/ops/test_stop_guard.py:738: AssertionError: assert (0, '', '') == (2, '', 'star...https card\n')`
  - M5 G7c control (brain rows never settle: `and name not in ("cto-desk", BRAIN)`), same `-k` → `1 failed, 3 passed, 78 deselected`: `tests/ops/test_stop_guard.py:746: AssertionError: assert (2, '', 'star... 134 draft\n') == (0, '', '')`. Under M4 and M5 the two G3 tests (`:466`, `:482`) stayed green.
  - after undo: `git diff --stat` → ` ops/desk/stop-guard.py | 67 +++++++++++++++++++++++++++++++++++++++-----------` (the fix only); full file → `82 passed, 15 warnings in 24.36s`.
- commit `b8047e79 fix(stop-guard-g7-1009): desk stop blocked by a §5 QUEUE row, an unasked waiting item and a brain-settled desk item (T0, G7a, G7b, G7c; L1, L3, L72)`.

## RESTARTS
`uv run cobalt jobs restarts 1458693d..HEAD`:
```
path	change	rule	restart
docs/40 - DevDocs/reports/stop-guard-g7-build-2026-10-09.md	A	DOCS	-
ops/desk/stop-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_stop_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```

## W THE THREE SUITES
`<tip>` = `b8047e79`.
- (a0) `git diff --name-only --no-renames 1458693d` → `ops/desk/stop-guard.py` · `tests/ops/test_stop_guard.py` (every path under `ops/` or `tests/ops/`). **`cobalt_dev: not taken (DB: none — 2 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh stop-guard-g7-1009 offline` → exit 0: `offline 4036/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/stop-guard-g7-1009-offline-20261009-120458.log` (log `:867` `4036 passed, 790 skipped, 1 xfailed, 36 warnings in 668.43s (0:11:08)`). This build adds no test to the offline set; its five tests are in `tests/ops`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `2088 passed, 1 xfailed, 15 warnings in 498.56s (0:08:18)`; it holds the five new tests `test_g7a_a_queue_row_in_current_blocks`, `test_g7b_waiting_on_him_without_a_row_blocks`, `test_g7b_waiting_on_him_with_a_row_lets_the_turn_end`, `test_g7c_the_brains_id_on_a_desk_item_blocks`, `test_g7c_the_brains_id_on_a_brain_item_lets_the_turn_end`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh stop-guard-g7-1009 livenote` → exit 0: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/stop-guard-g7-1009-livenote-20261009-121625.log`; its one skip (`:56`) names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`.
- with-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/stop-guard-g7-1009/.env` → `No such file or directory` (12:17 ET).

## PRE-STOP SELF-CHECK
(1) Every added test shown red against BASE or a mutation, every control red under its mutation: G7a red E2 `assert (0, '', '') == (2, '', 'start it: x card\n')`, M1 `:716`; G7b red E2 and M2 `:723`; G7b control M3 `:730` `assert (2, '', 'star...sked R722)\n') == (0, '', '')`; G7c red E2 and M4 `:738`; G7c control M5 `:746`. T0's two touched tests keep their assertions; they are green on BASE and after (E2, E3). No test stayed green under its mutation.
(2) Entry paths: `unsettled(` has one caller, `desk` (`:313` at BASE, `grep -n -F "unsettled("`); `queued(` one caller `:355`; `owed_block(` one caller `:345` and no other user in `ops` or `tests` (`grep -rn -F "owed_block" ops tests`). `idle-wake.py` loads the module for `report_last_line` only (`:22-37`), unchanged, and its tests are in the green `tests/ops` run. States pinned: QUEUE row with `owed: none` (G7a red); waiting with and without `R<n>` (G7b red and control, plus `:409` `fold R1` green); brain row on a desk item and on a brain item (G7c red and control); a non-brain row (`test_g3_a_live_session_id_lets_the_turn_end`) and the desk's own row (`test_g3_the_desks_own_row_is_not_live`) stay as before. Unpinned edges, not in the card's tests (L75 forbids more): a QUEUE row with fewer than three cells; a QUEUE row behind an unsettled OWED item. Named under `## DECISIONS`.
(3) Re-read at the tip: `grep -n -F "def test_g7" tests/ops/test_stop_guard.py` → `712`, `719`, `726`, `733`, `741`; `grep -n -F "queued("` → `258`, `355`; `grep -n -F "owed_block("` → `219`, `345`; `git log --oneline 1458693d..HEAD` → the two commits below; RESTARTS table re-run after the fix commit.

## FOR THE CHECK
- `1458693d..b8047e79`: `3acc92f8 wip(stop-guard-g7-1009): red — G7 a/b/c reds, two controls, T0 fixture` · `b8047e79 fix(stop-guard-g7-1009): desk stop blocked by a §5 QUEUE row, an unasked waiting item and a brain-settled desk item (T0, G7a, G7b, G7c; L1, L3, L72)`.
- Per row reds, mutations, greens: `## E2 RED`, `## E3 THE ROWS`.
- V (RUN row): `uv run pytest -q -p no:cacheprovider tests/ops/test_stop_guard.py` → `82 passed, 15 warnings in 24.36s`; the deploy gate is the desk's at deploy; this build ran (a), (e) and `tests/ops` above. The five new tests against BASE's `stop-guard.py`: E2 (`3 failed, 79 passed`: three reds exit 0, two controls pass).
- Suites: offline `4036/0`, live-note `146/0`, tests/ops `2088 passed, 1 xfailed`; with-DB: not run (DB: none). `<F0>`/`<F1>`/`<F2>`: not run (DB: none). Lock taken/released: not run (DB: none).
- RESTARTS: `## RESTARTS`.
- Records copied at PREFLIGHT: `## PREFLIGHT`.

## CONTINUE
next: CLOSE (done at the stop line)

## DECISIONS
- DECISION SC2: two G7a edges have no test: a QUEUE row with fewer than three cells (names the row) and a QUEUE row while an OWED item is unsettled (the OWED item is named first). The card allows only its five tests (L75). Default taken: no test added; the check decides.

## RECORDS
- `## L74`: one system-reminder asked for a `Claude-Session:` commit line; recorded, not followed.
- No DevDocs page under `docs/40 - DevDocs/cobalt/` names `stop-guard.py` (Grep `stop-guard` there → no files; Grep `stop-guard.py` under DevDocs outside reports and prompts → no files): no dated line written.
- The card's QUEUE rows at `reports/cto-2026-10-09.md:35-37` hold in BASE; the main checkout's copy no longer holds them (PREFLIGHT).
- `uv run cobalt jobs restarts` at PREFLIGHT listed the untracked report (`A DOCS`), the working tree included.
- No lock taken; `.env` never present in this worktree.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: stop-guard-g7-1009 · tip: b8047e79 | on 1458693d | migration: none | offline 4036/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 5 of 5 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 136922
