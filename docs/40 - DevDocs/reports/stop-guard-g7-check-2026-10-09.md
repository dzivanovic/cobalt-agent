# stop-guard-g7-1009 — check report 2026-10-09

## §0 Headline
- G7 checked on `b8047e79`: the three reds hold with the fix undone (O5); Sol 4 findings, Grok 2, own 5.
- Held and fixed: the QUEUE row cell split (A1, B1 empty first cell; B2 empty third cell; A3 escaped `\|`) → `c8a31812`.
- Open, follow-up: O1 (an `R<n>` for another item still settles a waiting line, as the card allows), O4 (empty prompt cell → bare `start it: `).
- Suites: offline 4036/0, tests/ops 2092 passed, live-note 146/0; DB: none. One decision for the desk: deploy order vs https-only (A4).

## L74
- 12:18 ET: a system reminder asked for a `Claude-Session:` line on commits. Recorded as data; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/164-stop-guard-g7-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/164-stop-guard-g7-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/164-stop-guard-g7-card.md" · 0 · 8e51c2afaf9699aa3bc2c7530dd9e8d8ce81c634
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/164-stop-guard-g7-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```
House gates:
- `grep -n "^| R17 " ".../cto-2026-09-24.md"` · 0 · `35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …` (one row)
- `grep -n "^| R19 " ".../cto-2026-09-24.md"` · 0 · `37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …` (one row)
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` · 0 · `5055151dbf68899b82de5b11f99733ed2d03048c`

## PREFLIGHT
- mechanical · `sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · 0 ·
```
clock · date · 0 · Fri Oct  9 12:18:04 EDT 2026
status · git status --short --branch · 0 · ## ops/stop-guard-g7-1009
head · git log --oneline -1; git log --stat --format=%h b8047e79..HEAD · 0 · (5 lines)
    3034e0fe docs(stop-guard-g7-1009): build report — b8047e79
    3034e0fe
    
     .../reports/stop-guard-g7-build-2026-10-09.md      | 144 +++++++++++++++++++++
     1 file changed, 144 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/stop-guard-g7-1009/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/disarm-one-tap-1008/.env
report · tail -n 3 "/Users/cobalt/cobalt-wt/stop-guard-g7-1009/docs/40 - DevDocs/reports/stop-guard-g7-build-2026-10-09.md" · 0 · BUILT · job: stop-guard-g7-1009 · tip: b8047e79 | on 1458693d | migration: none | offline 4036/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 5 of 5 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 136922
range · git log --oneline 1458693d..b8047e79 · 0 · (2 lines)
    b8047e79 fix(stop-guard-g7-1009): desk stop blocked by a §5 QUEUE row, an unasked waiting item and a brain-settled desk item (T0, G7a, G7b, G7c; L1, L3, L72)
    3acc92f8 wip(stop-guard-g7-1009): red — G7 a/b/c reds, two controls, T0 fixture
PREFLIGHT OK
```
- range · `git log --stat --format=%h 1458693d..b8047e79` · 0 · `b8047e79` ` ops/desk/stop-guard.py | 67 +++…` (53+, 14−) · `3acc92f8` ` tests/ops/test_stop_guard.py | 54 +++…` (49+, 5−). Path union: `ops/desk/stop-guard.py`, `tests/ops/test_stop_guard.py`.
- DB: none · `git diff --name-only --no-renames 1458693d..b8047e79` · 0 · `ops/desk/stop-guard.py` · `tests/ops/test_stop_guard.py` (both under `ops/` / `tests/ops/`).
- `ls <S>` · 1 · `No such file or directory` (fresh).
- house probes · `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh` · 0 ·
```
sol: UP
grok: UP
gemini: OUT — OK.
```
- seats: house A: Sol (`gpt-5.6-sol`) · house B: Grok (`grok-4.7`). HOUSE B: as needed.
- the other sibling `.env` (`disarm-one-tap-1008`) is another job's lock; this card is DB: none and takes no lock.

## Files copied
- `sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · 0 ·
```
11077 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/stop-guard-g7-1009-check/diff.md
7154 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/stop-guard-g7-1009-check/files/164-stop-guard-g7-card.md
17710 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/stop-guard-g7-1009-check/files/stop-guard-g7-build-2026-10-09.md
17164 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/stop-guard-g7-1009-check/files/wt/ops/desk/stop-guard.py
26781 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/stop-guard-g7-1009-check/files/wt/tests/ops/test_stop_guard.py
384 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/stop-guard-g7-1009-check/rulings.md
STAGED 6 files · 80270 bytes · commits 2
```
- `grep -c "^commit " <S>/diff.md` → `2` (= PREFLIGHT's commit count).
- `stage-copy.sh` (each exit 0): `COPIED 3808 <S>/files/desk-idle-answer-2026-10-09.md` · `COPIED 14350 <S>/files/66-desk-stop-guard-card.md` · `COPIED 7665 <S>/files/BRAIN-HUB.md` · `COPIED 868 <S>/files/wt/ops/desk/desk-list.sh`.
- `<S>/HOUSE-INSTRUCTIONS.md`: the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS` whole, the Files paragraph.
- 12:19 ET: house A Sol (`codex exec … gpt-5.6-sol …`, task `bpsjdnhfb`) and house B Grok (`grok -m grok-4.7 …`, task `bgdkmmntc`) started, `run_in_background`, timeout 2700000; `cd` back; `git status --short --branch` → `## ops/stop-guard-g7-1009`.

## OWN FINDINGS
Written before either house list was opened.

FINDING O1
ROW: G7b (X1)
CLAIM: The incident's own line (desk-idle-answer-2026-10-09.md:7: a `waiting on Dejan` line carrying a desk item and a row cited for another item) still settles, because `ops/desk/stop-guard.py:305` accepts any `R<digits>` anywhere in `<what>`.
RUN: TEST — tests/ops/test_stop_guard.py
```python
def test_check_o1_a_row_cited_for_another_item_does_not_settle_a_waiting_line(tmp_path):
    d = Desk(tmp_path)
    d.owed("OWED: S4 builds 72 / 73; guard cards D2 then D1 now unblocked (R707) | waiting on Dejan")
    r = d.run()
    assert r.returncode == 2, r
```
EXPECT: `AssertionError` — exit 0 on the tip (the `(R707)` settles the line).

FINDING O2
ROW: G7a (build DECISION SC2, first edge)
CLAIM: A QUEUE row with fewer than three cells names the row, stripped (`ops/desk/stop-guard.py:269`); no test pins it.
RUN: TEST — tests/ops/test_stop_guard.py
```python
def test_check_o2_a_short_queue_row_is_named_whole(tmp_path):
    d = Desk(tmp_path)
    d.owed("owed: none", rows=("| QUEUE | x card |",))
    r = d.run()
    assert (r.returncode, r.stdout, r.stderr) == (2, "", "start it: | QUEUE | x card |\n")
```
EXPECT: green if built as the row says; red names the defect.

FINDING O3
ROW: G7a (build DECISION SC2, second edge)
CLAIM: The QUEUE row is read only after every OWED item is settled (`ops/desk/stop-guard.py:354-355`): an unsettled OWED item is named first; no test pins it.
RUN: TEST — tests/ops/test_stop_guard.py
```python
def test_check_o3_an_unsettled_item_is_named_before_a_queue_row(tmp_path):
    d = Desk(tmp_path)
    d.owed("OWED: b", rows=("| QUEUE | — | x card | — | x |",))
    r = d.run()
    assert (r.returncode, r.stdout, r.stderr) == (2, "", "start it: b\n")
```
EXPECT: green if built as the row says; red names the defect.

FINDING O4
ROW: G7a
CLAIM: A QUEUE row whose third cell is empty (`| QUEUE | x | |`) yields the bare line `start it: ` with no work named (`ops/desk/stop-guard.py:267-269`: `strip("|")` then a third cell `""`).
RUN: TEST — tests/ops/test_stop_guard.py
```python
def test_check_o4_a_queue_row_with_an_empty_prompt_cell_names_something(tmp_path):
    d = Desk(tmp_path)
    d.owed("owed: none", rows=("| QUEUE | x | |",))
    r = d.run()
    assert r.returncode == 2 and r.stderr != "start it: \n", r
```
EXPECT: `AssertionError` — stderr `start it: \n` on the tip.

FINDING O5
ROW: X1 (G7a, G7b, G7c)
CLAIM: With the three G7 hunks of `ops/desk/stop-guard.py` undone (`:305-307` → `continue`, `:323` → `name != "cto-desk"`, `:354-355` removed) the three reds fail for their row's reason (exit 0) and the two controls pass — the build's E2/M1-M5 claims, re-run here (L70).
RUN: COMMAND `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_stop_guard.py -k g7` under that mutation (Edit tool, undone after).
EXPECT: `3 failed, 2 passed`, each failure `assert (0, '', '') == (2, …)`.

## Findings
- 12:23 ET Sol done (exit 0); its final message written to `<S>/house-a.md` (`FINDINGS: 4`). 12:35 ET Grok done (exit 0); `<S>/house-b.md` (`FINDINGS: 2`). `ls -la <S>` → `house-a.md` 2546 · `house-b.md` 1193.

id · house · row · claim · run
- A1 · Sol · G7a · `strip("|")` (`stop-guard.py:267`) peels an empty first cell, so `|| QUEUE | …` (QUEUE in cell 2) blocks · TEST
- A2 · Sol · V · the build report (`:125`) leaves the deploy gate to the desk, not run and quoted by the build · COMMAND
- A3 · Sol · G7a · an escaped `\|` inside the prompt cell truncates the `start it:` text · TEST
- A4 · Sol · SCOPE · the desk launched G7 while https-only (card ORDER record) was still waiting on machine steps · COMMAND
- B1 · Grok · G7a · same as A1: `|| QUEUE | …` is read as a QUEUE row · TEST
- B2 · Grok · G7a · `| QUEUE | — ||` (empty third cell) is counted as two cells and names the whole row, not the empty third cell · TEST

## Dropped
none — every block carries a test function or an allowed command.

## RUNS
Each test run alone: `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_stop_guard.py::<test>` on `b8047e79`'s code. Form repairs: none (each test pasted as written; the houses' and mine).
id · source · run · output · verdict
- O1 · own · TEST `test_check_o1_a_row_cited_for_another_item_does_not_settle_a_waiting_line` · `1 failed` · `test_stop_guard.py:753: AssertionError: CompletedProcess(… returncode=0, stdout='', stderr='')` / `assert 0 == 2` · REJECTED — card G7b: "A `waiting on Dejan` item is settled only when its `<what>` holds `R<digits>`": the line holds `R707`, so the card says it settles. Test removed; OPEN.
- O2 · own · TEST `test_check_o2_a_short_queue_row_is_named_whole` · `1 passed` · NOT HELD (green: a QUEUE row with fewer than three cells names the row; settles the build's DECISION SC2 first edge). Test removed.
- O3 · own · TEST `test_check_o3_an_unsettled_item_is_named_before_a_queue_row` · `1 passed` · NOT HELD (green: the unsettled OWED item is named before the QUEUE row; settles SC2 second edge). Test removed.
- O4 · own · TEST `test_check_o4_a_queue_row_with_an_empty_prompt_cell_names_something` · `1 failed` · `assert (2 == 2 and 'start it: \n' != 'start it: \n')` · REJECTED — card G7a: "`start it: <its third cell, stripped>`": an empty third cell gives an empty name, as the row says (B2 holds the same reading). Test removed; OPEN.
- O5 · own · COMMAND, under a mutation (Edit tool: `:305-307` → `continue`, `:323` → `and name != "cto-desk"`, `:354-355` removed) `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_stop_guard.py -k "test_g7a_a_queue or test_g7b_waiting or test_g7c_the_brains or test_g2_the_block_before or test_g4_the_first_unsettled"` · `3 failed, 4 passed, 83 deselected`: `:716 assert (0, '', '') == (2, '', 'start it: x card\n')` · `:723 assert (0, '', '') == (2, '', 'star...: build 72\n')` · `:738 assert (0, '', '') == (2, '', 'star...https card\n')`; the two controls and T0's two tests passed. Undone; `git diff --stat -- ops/desk/stop-guard.py` → nothing · NOT HELD (no defect: the three reds are red for their row's reason with the fix undone; the build's E2/M1-M4 claims stand, L70).
- A1 · Sol · TEST `test_g7a_queue_in_the_second_cell_does_not_block` · `1 failed` · `:781: AssertionError: assert (2, '', 'start it: x card\n') == (0, '', '')` · HELD (card G7a: "whose first cell, stripped, starts with `QUEUE`"; `strip("|")` at `:267` peels the empty first cell).
- A2 · Sol · COMMAND `grep -n -F "the deploy gate is the desk's at deploy" "<build report>"` · `125:- V (RUN row): … the deploy gate is the desk's at deploy; this build ran (a), (e) and \`tests/ops\` above. …` · NOT HELD — the line is there, but for a "DB: none" card the gate is `BUILD-HUB.md` W (a0), (a), (e) ("--deploy is not typed here, gate.sh accepts it with withdb and all only", `BUILD-HUB.md:78`), and the build report's `## W` quotes all three plus `tests/ops`. This check runs the same at `## 6`.
- A3 · Sol · TEST `test_g7a_an_escaped_pipe_stays_in_the_prompt_cell` · `1 failed` · `:788: AssertionError: assert (2, '', 'start it: x \\\n') == (2, '', 'star...x \\| card\n')` · HELD (card G7a names the third cell, `prompt · tab`; a Markdown `\|` is inside that cell and the split at `:267` cut it).
- A4 · Sol · COMMAND `grep -n -E "Launched G7 build|https-only card 156 needs" "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-09.md"` · `31:| R732 | 11:48 ET | G7 preflight r2 READY YES … Launched G7 build \`1979c01a\` (card \`164\`) …` · `38:OWED: https-only card 156 needs his M0/M2/M3 machine steps before launch (asked R727); … | waiting on Dejan` · OUT OF SCOPE — the output shows it (lines 31/38, not 30/37), but ORDER is a card `## RECORDS` line (a desk fact on launch order), not a row; nothing in the rows' files to fix. Under `## DECISIONS` for the desk (deploy order).
- B1 · Grok · TEST `test_g7a_an_empty_first_cell_is_not_a_queue_row` · `1 failed` · `:795: AssertionError: assert (2, '', 'start it: x card\n') == (0, '', '')` · HELD (same cause as A1).
- B2 · Grok · TEST `test_g7a_an_empty_third_cell_is_the_prompt_cell` · `1 failed` · `:802: AssertionError: assert (2, '', 'star...EUE | — ||\n') == (2, '', 'start it: \n')` · HELD (card G7a: the third cell; `| QUEUE | — ||` has three cells and `strip("|")` ate the empty third).
- HELD tests committed before the fix: `6f0d1cab wip(stop-guard-g7-1009): check red — A1, A3, B1, B2` (`1 file changed, 28 insertions(+)`).

## FIXES
- A1, A3, B1, B2 · `ops/desk/stop-guard.py`: `CELL = re.compile(r"(?<!\\)\|")`; `queued` splits the stripped row on unescaped pipes, drops the text before the first edge pipe and one empty cell after the last, then reads the first cell / third cell as before. `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_stop_guard.py` → `86 passed, 15 warnings in 24.26s`. Commit `c8a31812 fix(stop-guard-g7-1009): QUEUE row cells read between the edge pipes, an escaped pipe kept in its cell (check A1, A3, B1, B2)`. DevDocs line: none — no page under `docs/40 - DevDocs/cobalt/` names `stop-guard` (the build's RECORDS); none written.

## Suites
On `c8a31812` (DB: none: RESTARTS, then W (a0), (a), (e) and `tests/ops`, `BUILD-HUB.md:78`).
- RESTARTS · `uv run cobalt jobs restarts 1458693d..HEAD` · 0 ·
```
path	change	rule	restart
docs/40 - DevDocs/reports/stop-guard-g7-build-2026-10-09.md	A	DOCS	-
ops/desk/stop-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_stop_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```
- (a0) `git diff --name-only --no-renames 1458693d` → `docs/40 - DevDocs/reports/stop-guard-g7-build-2026-10-09.md` · `ops/desk/stop-guard.py` · `tests/ops/test_stop_guard.py` — every path under `docs/`, `ops/`, `tests/ops/`. **`cobalt_dev: not taken (DB: none — 3 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh stop-guard-g7-1009 offline` · exit 0 · `offline 4036/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/stop-guard-g7-1009-offline-20261009-123738.log` (log `:867` `4036 passed, 790 skipped, 1 xfailed, 36 warnings in 666.66s (0:11:06)`).
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` · exit 0 · `2092 passed, 1 xfailed, 15 warnings in 499.11s (0:08:19)` (the build's 2088 + the check's 4).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh stop-guard-g7-1009 livenote` · exit 0 · `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/stop-guard-g7-1009-livenote-20261009-124903.log`; its one skip `:56 SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).
- with-DB: not run (DB: none). `.env`: `ls /Users/cobalt/cobalt-wt/stop-guard-g7-1009/.env` → `No such file or directory` (12:49 ET); never present.

## Scope
PREFLIGHT path union: `ops/desk/stop-guard.py`, `tests/ops/test_stop_guard.py` (+ the build report under `docs/`). The check's commits: `6f0d1cab` → `tests/ops/test_stop_guard.py`; `c8a31812` → `ops/desk/stop-guard.py`. Both are in rows G7a's `files`. Nothing else.

## Checked against the branch
- (i) `git log --oneline b8047e79..HEAD -- . ":(exclude)docs"` → `c8a31812 fix(stop-guard-g7-1009): QUEUE row cells read between the edge pipes, an escaped pipe kept in its cell (check A1, A3, B1, B2)` · `6f0d1cab wip(stop-guard-g7-1009): check red — A1, A3, B1, B2`. `<tip now>` = `c8a31812`.
- (ii) `git log --stat --format=%h b8047e79..HEAD` → `c8a31812` `ops/desk/stop-guard.py | 9 +++++++--` · `6f0d1cab` `tests/ops/test_stop_guard.py | 28 ++++…` · `3034e0fe` `.../reports/stop-guard-g7-build-2026-10-09.md | 144 +++…`. Every non-docs path is in a row's `files`.
- (iii) fence: `git log --oneline 1458693d..HEAD -- ops/desk/desk-list.sh src configs` → empty. No hub, `settings.json` or other `ops/desk` script in (ii).
- (iv) `grep -n -F "def <test>" tests/ops/test_stop_guard.py` → A1 `749:def test_g7a_queue_in_the_second_cell_does_not_block(tmp_path):` · A3 `756:def test_g7a_an_escaped_pipe_stays_in_the_prompt_cell(tmp_path):` · B1 `763:def test_g7a_an_empty_first_cell_is_not_a_queue_row(tmp_path):` · B2 `770:def test_g7a_an_empty_third_cell_is_the_prompt_cell(tmp_path):`; `6f0d1cab` (red) sits below `c8a31812` (fix) in (i).
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/stop-guard-g7-1009`.
- (vi) `git log --stat --format=%h 1458693d..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no migration, no with-DB test; gate lists not touched.
- (vii) RECORDS re-run: `git -C /Users/cobalt/cobalt diff --stat main -- ops/desk/stop-guard.py tests/ops/test_stop_guard.py ops/desk/desk-list.sh` → nothing; `git -C /Users/cobalt/cobalt log --oneline 1458693d..main -- <same three>` → nothing (main has not moved these files; main now `90012742 docs(desk): top-50 check launched`); `grep -c -F "ops/desk" configs/cobalt/jobs.yaml` → `0`; `grep -n -F -e "--name brain" ".../prompts/BRAIN-HUB.md"` → `8:claude --bg … --remote-control brain --name brain …`.
- (viii) L32: this report holds no ticker, price or date of his; test values are constructed.

## OPEN
- O1 · REJECTED — card G7b. A `waiting on Dejan` line settles on any `R<digits>` in `<what>`, so a line that cites a row for a different item (the incident's own shape, `desk-idle-answer-2026-10-09.md:7`, `(R707)`) still settles. Would settle it: a row that ties the R<n> to the `(asked R<n>)` form (e.g. `\(asked R\d+\)`), or the desk's RULE NOW 3 alone. FOLLOW-UP.
- O4 · REJECTED — card G7a. A QUEUE row whose prompt cell is empty blocks with the bare line `start it: ` (B2 pins this as the card's reading). Would settle it: a row naming the whole row when the third cell is empty. FOLLOW-UP.

## CONTINUE
next: CLOSE (done at the stop line)

## DECISIONS
- A4 (Sol, OUT OF SCOPE for this check): the card's ORDER record says this card builds after https-only (`156`) deploys; `cto-2026-10-09.md:31` shows the G7 build launched at 11:48 ET while `:38` still holds https-only `waiting on Dejan` (asked R727). Nothing in the rows' files to fix. Default taken: none — the deploy order is the desk's; this check only reports that G7 is ready ahead of https-only.

## RECORDS
- Dropped findings: none.
- Every house produced a list: Sol `FINDINGS: 4` (12:23 ET), Grok `FINDINGS: 2` (12:35 ET). Gemini probed `OUT — OK.` and was not seated.
- The build's DECISION SC2 (two G7a edges untested) settled by run: O2 and O3 green on the tip; their tests removed (NOT HELD).
- A1 and B1 are the same test body; both kept (one per finding, for (iv)).
- REFUSED, not needed: none. CONTINUED: none. Lock takes: none (DB: none). L74: one line (above).
- Another job's `.env` at PREFLIGHT: `/Users/cobalt/cobalt-wt/disarm-one-tap-1008/.env` (its lock; not this card's).
- Fixed-string grep with a leading `--` needs `-e`: `grep -n -F "--name brain" …` → `grep: unrecognized option` (exit 2); re-run as `grep -n -F -e "--name brain" …`.
- files opened: 14 — `CHECK-HUB.md`; the card `164-stop-guard-g7-card.md`; `BUILD-HUB.md` (`## THE LOCK` … `## W`); `ops/desk/stop-guard.py`; `tests/ops/test_stop_guard.py`; the build report; `desk-idle-answer-2026-10-09.md`; `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); the house probe output; Sol's output (→ `house-a.md`); `house-b.md`; the offline gate output; the `tests/ops` output; the livenote gate output.
- Check of `stop-guard-g7-1009`: house A `Sol`, house B `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: stop-guard-g7-1009 · pass: 1 · tip: c8a31812 · house A: Sol FINDINGS: 4 · findings: 11 · dropped: 0 · held: 4 · fixed: 4 · held unfixed: 0 · open: 2 · house B: Grok FINDINGS: 2 · suites: offline 4036/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 160632
