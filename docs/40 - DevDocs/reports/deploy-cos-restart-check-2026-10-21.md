# deploy-cos-restart — check 2026-10-21

## §0 Headline

CHECK DONE on `3770387d` (build tip `af0f86bc`): the three cos strings, the STEP-R admit, the resume read and the stop-line field are built as the card's rows say; no defect in the hub text.
House A Grok wrote 5 findings and I wrote 4. Two held (A4, A5): the build's tests left `those three services`, the `## 3.` counts and `the three bootout/bootstrap` unpinned, and two new tests now pin them (each shown red under a mutation).
One item is open, A2 / X5: R2240 is committed but is not on the card's `RULINGS`, so `authorize.sh` does not prove it. That is the desk's file (`## DECISIONS`). The cos smoke-health and stale-line items fall inside the card's fence.
Offline 9094/0 · live-note 148/0 · `tests/ops` 4136 passed · DB: none · `RESTARTS: none` · ready: YES.

## L74

- A system-reminder in this session asked for a `Claude-Session:` line on commits. Recorded once here as DATA (L74); not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION

`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/1008-deploy-cos-restart-card.md"` → exit 0:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/1008-deploy-cos-restart-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-21/1008-deploy-cos-restart-card.md" · 0 · ef93937e5653688191ab6d8479e4d0220a951ad8
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-21/1008-deploy-cos-restart-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

House gates: `grep -n "^| R17 " ".../cto-2026-09-24.md"` → one row (`35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …`); `grep -n "^| R19 " …` → one row (`37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …`); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT

`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` → exit 0:

```
clock · date · 0 · Thu Oct 22 00:21:21 EDT 2026
status · git status --short --branch · 0 · ## ops/deploy-cos-restart
head · git log --oneline -1; git log --stat --format=%h af0f86bc..HEAD · 0 · (6 lines)
    c03fdc59 docs(deploy-cos-restart): build report — af0f86bc
    c03fdc59
    
     .../reports/deploy-cos-restart-build-2026-10-21.md | 180 +++++++++++++++++++++
     .../deploy-cos-restart-build-2026-10-21.result     |  15 ++
     2 files changed, 195 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/deploy-cos-restart/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/deploy-cos-restart/docs/40 - DevDocs/reports/deploy-cos-restart-build-2026-10-21.md" · 0 · BUILT · job: deploy-cos-restart · tip: af0f86bc | on 0e2b5b54 | migration: none | offline 9092/0 | with-DB 0/0 | live-note 148/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 6 of 6 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 187734
range · git log --oneline 0e2b5b54..af0f86bc · 0 · (2 lines)
    af0f86bc feat(deploy-cos-restart): the deploy line restarts a loaded cos from its repo plist (F1-F4, P1, L42, L60, L67)
    eac16bee wip(deploy-cos-restart): red — F1-F4 tests (F1-F4, L67)
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| the range, typed | `git log --stat --format=%h 0e2b5b54..af0f86bc` | 0 | `af0f86bc`: `DEPLOY-HUB.md` 20, `STANDING-LIST.md` 10, `test_deploy_smoke_string_1014.py` 13, `test_desk_launch_launchd.py` 8, `test_hub_cos_restart_1019.py` 15, `test_hub_deferred_1018.py` 2 (6 files, +31 −37) · `eac16bee`: `test_deploy_cos_restart_1021.py` 141, `test_desk_launch_launchd.py` 9 (2 files, +150) |
| DB: none paths | `git diff --name-only --no-renames 0e2b5b54..af0f86bc` | 0 | `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `docs/40 - DevDocs/prompts/STANDING-LIST.md` · `tests/ops/test_deploy_cos_restart_1021.py` · `tests/ops/test_deploy_smoke_string_1014.py` · `tests/ops/test_desk_launch_launchd.py` · `tests/ops/test_hub_cos_restart_1019.py` · `tests/ops/test_hub_deferred_1018.py` — every path under `docs/` or `tests/ops/` |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| house probes | `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` | 0 | `grok: UP` · `gemini: UP` |
| seats | SEAT ORDER, no header line | — | house A: Grok · house B: none (not needed) — card `HOUSE B: as needed` |
| self-check | build report last line | — | `self-check: 3 of 3` |

## Files copied

`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → exit 0:

```
32 <S>/STAGED-CARD
13419 <S>/diff.md
27612 <S>/files/1008-deploy-cos-restart-card.md
22663 <S>/files/deploy-cos-restart-build-2026-10-21.md
70647 <S>/files/wt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md
47869 <S>/files/wt/docs/40 - DevDocs/prompts/STANDING-LIST.md
5681 <S>/files/wt/tests/ops/test_deploy_cos_restart_1021.py
4601 <S>/files/wt/tests/ops/test_deploy_smoke_string_1014.py
10551 <S>/files/wt/tests/ops/test_desk_launch_launchd.py
2861 <S>/files/wt/tests/ops/test_hub_cos_restart_1019.py
4107 <S>/files/wt/tests/ops/test_hub_deferred_1018.py
386 <S>/rulings.md
STAGED 12 files · 210429 bytes · commits 2
```

`stage-copy.sh`, each → `COPIED <bytes> <dest>`: `files/deploy-x15-hitl-probe-port.md` 11609 · `files/869-hub-cos-restart-card.md` 21134 · `files/wt/ops/desk/desk-launch.sh` 157078 · `files/wt/tests/ops/test_hub_agent_retired_1020.py` 4166 · `files/wt/ops/desk/deploy-outage.sh` 16612 · `files/wt/ops/desk/deploy-step0.sh` 46839 · `files/wt/ops/com.cobalt.cos.plist` 1335. `<S>/HOUSE-INSTRUCTIONS.md` written (28174 bytes, `ls -la <S>`).

## OWN FINDINGS

Written 00:3x EDT before any house file was opened. Read: the card, `git diff --word-diff 0e2b5b54..af0f86bc -- "docs/40 - DevDocs/prompts"`, the test diff, `tests/ops/test_deploy_cos_restart_1021.py`, `tests/ops/test_deploy_smoke_string_1014.py:25-112`, `DEPLOY-HUB.md:5-13, 65, 90-97, 120-174` at the tip, `STANDING-LIST.md:105-162`, `ops/com.cobalt.cos.plist`, Grep of `ops/desk` for `com.cobalt.cos` and for stop-line field parsers.

FINDING O1
ROW: F1 (c) / X1
CLAIM: No test pins the `## 3.` heading counts (`STANDING-LIST.md:109`, `60 allow … (57 without a migration`) against the hub line `DEPLOY-HUB.md:11` (`Grep` of `tests` for `allow with one head` → no match); the +3 may not equal the line's real count.
RUN: TEST — `tests/ops/test_deploy_cos_restart_1021.py`
```python
def test_o1_the_section_3_heading_counts_the_line():
    import re
    line = one("claude --bg ")
    for token in (" <tip merges>", " <prod migrate strings>", " <launchd strings>"):
        line = line.replace(token, "", 1)
    literal = tools(line, "--allowedTools")
    (head,) = [ln for ln in lines(LIST) if ln.startswith("## 3. ")]
    m = re.search(r"— (\d+) allow with one head and a migration \((\d+) without a migration", head)
    assert m, head
    assert int(m.group(1)) == len(literal) + 1 + 3, (m.group(1), len(literal))
    assert int(m.group(2)) == len(literal) + 1, (m.group(2), len(literal))
```
EXPECT: if the heading is off, `AssertionError: ('60', <n>)`.

FINDING O2
ROW: F2 (a)
CLAIM: The admit's two conditions (`state = running`, the `path = ` line EXACTLY the repo plist) at `DEPLOY-HUB.md:94` are pinned by no test: `test_f2_a_loaded_running_cos_is_admitted_at_step_r` (`tests/ops/test_deploy_cos_restart_1021.py:94-105`) asserts `keeps it in \`<restart set>\`` and `COS_PLIST`, and `COS_PLIST` already stands on BASE's line; dropping `state = running` keeps every row test green.
RUN: TEST — `tests/ops/test_deploy_cos_restart_1021.py`
```python
def test_o2_the_admit_pins_running_and_the_exact_path():
    line = one(NOT_LOADED)
    assert ("Exit 0 → `state = running` and its `path = ` line EXACTLY "
            "`/Users/cobalt/cobalt/ops/com.cobalt.cos.plist` keeps it in `<restart set>`") in line
    assert "loaded and not running, or loaded from another path → `cd /Users/cobalt/cobalt`" in line
```
EXPECT: on the tip, if the hub text lacks the conditions, the first assertion fails.

FINDING O3
ROW: X3
CLAIM: No smoke step reads cos beyond (a)'s `launchctl print` (`DEPLOY-HUB.md:150`); `ops/com.cobalt.cos.plist:27-31` `KeepAlive` / `SuccessfulExit` `false` restarts a crashing cos, so one print can read `state = running` between crashes; no `logs/cos.err` count is taken.
RUN: COMMAND — `grep -c -F "cos.err" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: `0`.

FINDING O4
ROW: X6
CLAIM: `DEPLOY-HUB.md:95` still says `P8 and D1 print \`com.cobalt.aset\` and \`com.cobalt.radar\` by name` while D1 (`:123`) prints cos by name when it is in `<restart set>`; P8 (`:65`) proves the loaded path of aset and radar only (cos's is proven at STEP-R `:94`).
RUN: COMMAND — `grep -n -F "P8 and D1 print" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: one line, `95:`.

CHECK ASK answers with no finding (each read above, re-run at `## 4`):
- X2: 4.2 `:140` names cos in its `for each of` list; 4.6 `:144` bootstraps it from `/Users/cobalt/cobalt/ops/com.cobalt.cos.plist`; STEP-5 (1) `:163` acts on "each launchd resident of `<restart set>`", (3) `:169` bootstraps "each resident booted out" with 4.6's retry; smoke (a) `:150` reads a NEW pid for a label in the set against D1's `<cos pid>` (`:123`). A cos `not loaded — skipped` leaves `<restart set>` at `:94`, and every call above takes its label from `<restart set>` (`:95`).
- X4: `ops/desk/deploy-outage.sh:119` `com.cobalt.cos) printf '%s' "$REPO/ops/com.cobalt.cos.plist"`, `:100` admits cos; `deploy-step0.sh:74` lists it. Same path as S2.
- X5: `grep -n "^| R2240 " ".../cto-2026-10-20.md"` → `43:| R2240 | 20:57 ET | HIS RULING · APPROVED (via brain): the three R60 launchctl restart strings for a loaded com.cobalt.cos …`; `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R2240 |" -- …` → `f70be7320ae0b8be99317efecf7122b508c95f72`. Committed; not on the card's `RULINGS`, so `authorize.sh` did not prove it: `## DECISIONS`.
- X6: Grep of `ops/` for a stop-line field parser (`aset: <`, `— radar`, `· radar`) → none; no script reads the new `— cos:` field.

## Findings

House A Grok finished 00:35:39 EDT (`date`); `<S>/house-a.md` 5831 bytes, written by Grok; its stdout ends with that path. `FINDINGS: 5`. House B: none (not needed). Each `RUN:` line is followed by one `grep` command line: none dropped.

| id | house | row | claim (≤30 words) | form |
|---|---|---|---|---|
| A1 | Grok | X3 | no smoke step reads cos health beyond `launchctl print`; `KeepAlive` brings a crash loop back to running; no `logs/cos.err` read; a cos RED in `<hb0>` is not new | COMMAND |
| A2 | Grok | X5 | R2240 is committed `HIS RULING · APPROVED` but the card's `RULINGS` holds R1863 only, so `authorize.sh` does not prove it | COMMAND |
| A3 | Grok | X6 | THE ONE RESUME's (e) runs before (b)'s `## RESTARTS` read; `:95`, `:120`, `:135`, `:124`, `:151` still name aset/radar only | COMMAND |
| A4 | Grok | F1 | no test pins `those three services` (`STANDING-LIST.md:146-148`) or the `:109` counts | COMMAND |
| A5 | Grok | F2 | no test pins `the three \`bootout\`` / `the three \`bootstrap\`` on `DEPLOY-HUB.md:78`; only `kickstart -k` is asserted | COMMAND |

## Dropped

none

## RUNS

Form repair (one, said here): the houses' `grep -n -E` commands with alternations and several files were run as one `grep -n -F` per pattern (UNATTENDED RULES), and the three patterns that hold a backtick through the Grep tool (the bare-guard hook refuses a backtick in a Bash call). No assertion changed.

| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_deploy_cos_restart_1021.py::test_o1_the_section_3_heading_counts_the_line …::test_o2_…` | `2 passed, 15 warnings in 0.97s` | NOT HELD — the heading `60 … (57` equals the line's count (literal strings + 1 head + 3 migrate); test removed |
| O2 | Opus | same call | `2 passed` | NOT HELD — the admit text holds both conditions; test removed |
| O3 | Opus | `grep -c -F "cos.err" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | `0` | OUT OF SCOPE — `## NOT IN THIS JOB`: "A cos log read or a cos heartbeat expectation in smoke: CHECK ASK X3 asks it; a needed line is its own card." |
| O4 | Opus | `grep -n -F "P8 and D1 print" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | `95:- THE SET DRIVES THE REST: … P8 and D1 print \`com.cobalt.aset\` and \`com.cobalt.radar\` by name; …` | OUT OF SCOPE — `## NOT IN THIS JOB`: "Any line of `DEPLOY-HUB.md` but `:3`, `:11`, `:23`, `:53`, `:78`, `:94`, `:140`, `:144`, `:150`, `:171`" (`:95` stands) |
| A1 | Grok | `grep -n -F "SuccessfulExit" ops/com.cobalt.cos.plist` · `grep -n -F "probe_mod.cos" src/cobalt/heartbeat/runner.py` · `grep -n -F "logs/cos.err" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md" ops/com.cobalt.cos.plist` | `29:        <key>SuccessfulExit</key>` · `150:        probe_mod.cos(ts),` · `ops/com.cobalt.cos.plist:35:    <string>/Users/cobalt/cobalt/logs/cos.err</string>` (no `DEPLOY-HUB.md` line) | OUT OF SCOPE — the same fence line as O3 |
| A2 | Grok | `grep -n -F "RULINGS:" "<card>"` · `grep -n "^| R2240 " ".../cto-2026-10-20.md"` | `15:RULINGS: 2026-10-18 R1863` · `43:| R2240 | 20:57 ET | HIS RULING · APPROVED (via brain): the three R60 launchctl restart strings for a loaded com.cobalt.cos …` | UNSETTLED — the output shows the claim, but its fix is the card's `RULINGS` line, a desk file outside the rows and this branch; no test of this branch can settle it: `## DECISIONS` |
| A3 | Grok | `grep -n -F "(e) FIRST"` · `"P8 and D1 print"` · `"no new RED on the aset or radar"` (DEPLOY-HUB.md) · Grep `aset / sheet probe` (count 1) · `grep -n -F "recut: the failed deploy names" ops/desk/desk-launch.sh` | `53:` holds `(e) FIRST` and, inside (e), `` `…/com.cobalt.cos` → `state = running` when the report's `## RESTARTS` puts `com.cobalt.cos` in `<restart set>` `` · `95:` · `135:- D2.5 … no new RED on the aset or radar probe` · `2493:        *"rollback: used"*) refuse "recut: the failed deploy names 'rollback: used' …` | NOT HELD for the resume — (e)'s own clause directs the `## RESTARTS` read for its cos print, so a resume that follows `:53` reads it; the output does not show a cos left down. OUT OF SCOPE for `:95`, `:120`, `:124`, `:135`, `:151` (the `DEPLOY-HUB.md` line fence) |
| A4 | Grok | `grep -rn -F "those three services" tests` · `grep -rn -F "60 allow with one head" tests` | no output (both) | HELD — no test pins F1 (b)'s `those three services` or (c)'s counts; mutation proof below |
| A5 | Grok | Grep `the three \`(bootout\|bootstrap\|kickstart -k)\`` over `tests` | `tests/ops/test_deploy_cos_restart_1021.py:118:    assert "the three \`kickstart -k\`" in row` (only) | HELD — F2 (f)'s `the three \`bootout\`` / `the three \`bootstrap\`` unpinned; mutation proof below |

RED FIRST for A4, A5 (the held runs were commands, so the new tests are shown red against a mutation of the hub text, each made with Edit and undone with Edit):
- M-A: `STANDING-LIST.md:146` `those three services` → `those two services`, and `DEPLOY-HUB.md:78` `the three \`bootout\`` → `the two \`bootout\``: `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_deploy_cos_restart_1021.py` → `........FF` · `2 failed, 8 passed` — `test_a4_…`: `AssertionError: | \`Bash(launchctl bootout gui/501/com.cobalt.aset)\` · … | those two services | any other label |`; `test_a5_…`: `AssertionError: bootout` · `assert 'the three \`bootout\`' in '| NO HARMLESS VARIANT …'`. The builder's 8 tests stayed GREEN under this mutation (A4, A5's claim, shown).
- M-B: `STANDING-LIST.md:109` `60 … (57` → `57 … (54` (BASE's): the same file plus `tests/ops/test_deploy_smoke_string_1014.py` → `1 failed, 13 passed` — `test_a4_…`: `assert (57, 54) == (60, 57)`. No other test failed.
- Both undone; `git diff --stat` → `tests/ops/test_deploy_cos_restart_1021.py | 26 +` only.

## FIXES

- A4, A5: fixed in `tests/ops/test_deploy_cos_restart_1021.py` (a row's file): NEW `::test_a4_the_standing_list_rows_say_three_and_the_heading_counts_the_line` (each S1-S3 row says `those three services`; the `## 3.` heading's two numbers = the line's literal allow strings + 1 head + 3 migrate, and + 1 head) and NEW `::test_a5_the_harmless_variant_row_names_three_of_each` (`the three` and never `the two` for `bootout`, `bootstrap`, `kickstart -k`). Green at the tip: `2 passed, 15 warnings in 0.78s`; the card's suite `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_deploy_cos_restart_1021.py tests/ops/test_hub_cos_restart_1019.py tests/ops/test_hub_deferred_1018.py tests/ops/test_desk_launch_launchd.py tests/ops/test_deploy_smoke_string_1014.py tests/ops/test_hub_agent_retired_1020.py tests/ops/test_hub_lines.py` → `91 passed, 15 warnings in 13.75s`. Commit `3770387d fix(deploy-cos-restart): pin the three-services rows, the ## 3. counts and the three bootout/bootstrap (check A4, A5)`. No `src/` module changed: no DevDocs module page to date (as the build).

## Suites

On `3770387d` (DB: none card: RESTARTS, then W (a0), (a) with `--deploy-gate`, (e)):
- RESTARTS: `uv run cobalt jobs restarts 0e2b5b54..HEAD` → exit 0, 9 rows: `DEPLOY-HUB.md`, `STANDING-LIST.md`, the build report and its `.result` `DOCS -`; the five `tests/ops` files `test/documentation; no resident -`; last line `RESTARTS: none`. No UNCLASSIFIED row.
- (a0) `git diff --name-only --no-renames 0e2b5b54` → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `docs/40 - DevDocs/prompts/STANDING-LIST.md` · `docs/40 - DevDocs/reports/deploy-cos-restart-build-2026-10-21.md` · `docs/40 - DevDocs/reports/deploy-cos-restart-build-2026-10-21.result` · `tests/ops/test_deploy_cos_restart_1021.py` · `tests/ops/test_deploy_smoke_string_1014.py` · `tests/ops/test_desk_launch_launchd.py` · `tests/ops/test_hub_cos_restart_1019.py` · `tests/ops/test_hub_deferred_1018.py` — every path under `docs/` or `tests/ops/`: **`cobalt_dev: not taken (DB: none — 9 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-cos-restart offline --deploy-gate` → exit 0: `tests/ops: run (deploy gate)` · `offline 9094/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-cos-restart-offline-20261022-003853.log`; in the log `957:4958 passed, 878 skipped, 4 xfailed, 36 warnings in 720.59s (0:12:00)`, `1032:4136 passed, 1 xfailed, 16 warnings in 902.44s (0:15:02)`. The 2 tests this check adds: `test_a4_…`, `test_a5_…` (4134 → 4136).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-cos-restart livenote` → exit 0: `live-note 148/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-cos-restart-livenote-20261022-010632.log`; its one skip `56:SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (none names `COBALT_LIVE_VAULT_ROOT`).
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `4136 passed, 1 xfailed, 16 warnings in 909.85s (0:15:09)`.
- with-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/deploy-cos-restart/.env` → `No such file or directory`.

## Scope

PREFLIGHT's path union (`0e2b5b54..af0f86bc`): `DEPLOY-HUB.md` (F1-F4), `STANDING-LIST.md` (F1), `tests/ops/test_deploy_cos_restart_1021.py` (F1-F4), `tests/ops/test_desk_launch_launchd.py` (F1, P1), `tests/ops/test_hub_cos_restart_1019.py`, `tests/ops/test_hub_deferred_1018.py`, `tests/ops/test_deploy_smoke_string_1014.py` (P1) — each in a row's `files`. My commit `3770387d`: `tests/ops/test_deploy_cos_restart_1021.py` only (F1, F2 `files`). No path reaches a score, rank, grade or size: the change is hub text and `tests/ops` only.

## Checked against the branch

- (i) `git log --oneline af0f86bc..HEAD -- . ":(exclude)docs"` → `3770387d fix(deploy-cos-restart): pin the three-services rows, the ## 3. counts and the three bootout/bootstrap (check A4, A5)` = `<tip now>`.
- (ii) `git log --stat --format=%h af0f86bc..HEAD` → `3770387d` `tests/ops/test_deploy_cos_restart_1021.py | 26 +`; `c03fdc59` the build report and `.result` (docs). No other path.
- (iii) `git log --oneline 0e2b5b54..HEAD -- ops/desk/desk-launch.sh ops/desk/deploy-step-c.sh ops/desk/deploy-step0.sh ops/desk/deploy-outage.sh ops/desk/orphan-clean.sh ops/desk/deploy-card.sh ops/desk/deploy-smoke.sh src/cobalt/jobs/restarts.py configs/cobalt/jobs.yaml ops/com.cobalt.cos.plist "docs/40 - DevDocs/prompts/CARD.md"` → EMPTY. The `DEPLOY-HUB.md` line fence: the build's word-diff touches `:3 :11 :23 :53 :78 :94 :140 :144 :150 :171` only; my mutations were undone (`git diff --stat` → the test file only before the commit).
- (iv) `grep -n -F "def test_a4_the_standing_list_rows_say_three_and_the_heading_counts_the_line" tests/ops/test_deploy_cos_restart_1021.py` → `146:` · `grep -n -F "def test_a5_the_harmless_variant_row_names_three_of_each" …` → `163:`. No `wip(deploy-cos-restart): check red` commit: A4 and A5 held by COMMAND output (no test existed to commit red); the new tests were shown red against undone mutations (M-A, M-B under `## RUNS`) and committed once with the fix.
- (v) `ls /Users/cobalt/cobalt-wt/deploy-cos-restart/.env` → `No such file or directory`; `git status --short --branch` → `## ops/deploy-cos-restart`.
- (vi) `git log --stat --format=%h 0e2b5b54..HEAD -- src/cobalt/db_migrations tests/cobalt` → EMPTY: no gate list owed.
- (vii) card `## RECORDS` `ls /Users/cobalt/cobalt/ops/com.cobalt.cos.plist` → `/Users/cobalt/cobalt/ops/com.cobalt.cos.plist` (listed). The R2240 row re-read: `43:| R2240 | 20:57 ET | HIS RULING · APPROVED (via brain): …` (as recorded).
- (viii) L32: this report holds no ticker, price or date of his; the values quoted are file paths, labels and counts.

## OPEN

- A2 (X5) UNSETTLED: R2240 is not on the card's `RULINGS` line. Settled by a DESK RECORD row (`SETTLED: A2 — R<n>`) that either adds `2026-10-20 R2240` to the card's `RULINGS` for the deploy's `authorize.sh`, or records that R60's standing list plus the committed R2240 row is the proof.
- OUT OF SCOPE (never open): O3 / A1 (no cos health read in smoke beyond (a); `KeepAlive` can hide a crash loop from one print; a cos RED already in `<hb0>` is not new — the card's own fence line, "a needed line is its own card"); O4 / the line part of A3 (`DEPLOY-HUB.md:95` `P8 and D1 print` aset and radar by name; `:120`, `:135` stop only on aset / radar probe REDs; `:124`, `:151` read no `logs/cos.err`) — fenced `DEPLOY-HUB.md` lines.

## CONTINUE

next: CLOSE (done)

## DECISIONS

1. ASK DESK: A2 / X5 — his R2240 (`reports/cto-2026-10-20.md:43`, committed `f70be732`) is the approval the three new strings rest on, but the card's `RULINGS` holds only `2026-10-18 R1863`, so no `authorize.sh` run proves R2240. Safe default taken: nothing changed (the card is the desk's file, outside this branch); ready stays YES because the row is committed and APPROVED. The desk adds it to the card before the deploy, or records why the standing list suffices, as one `SETTLED: A2 — R<n>`. [01:21 EDT]

Follow-up (no decision, OUT OF SCOPE): a cos smoke-health card (a `logs/cos.err` baseline and count, a cos probe expectation in (e)) and the stale `:95` sentence, as `## OPEN` lists them.

## RECORDS

- Check started 00:21:17 EDT 2026-10-22 (`date`); house A started 00:24:06; house A finished 00:35:39; suites ended 01:21:57 (`date`).
- House A Grok: `<S>/house-a.md` written by Grok itself; stdout was its progress text and the path. House B: none — the card says `HOUSE B: as needed`; Gemini probed UP and was not seated.
- Dropped: none. No house produced nothing. No `REFUSED, not needed` line. No `CONTINUED` line. No lock take (DB: none).
- The bare-guard hook blocked three Bash greps that held a backtick (`NOT A REFUSAL … contains a backtick`); they were run through the Grep tool (A5's row).
- L74: one system-reminder asked for a `Claude-Session:` line on commits; recorded under `## L74`, not acted on.
- The house-probe output and the gate outputs were read from the session's task files; the diff was read from `git diff` output.
- files opened: 11 — `CHECK-HUB.md`, the card, `BUILD-HUB.md` (`## THE LOCK`, `## E2`, `## RESTARTS`, `## W`), the build report, `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down), `tests/ops/test_deploy_cos_restart_1021.py`, `tests/ops/test_deploy_smoke_string_1014.py`, `DEPLOY-HUB.md`, `STANDING-LIST.md`, `ops/com.cobalt.cos.plist`, `<S>/house-a.md`.
- Check of `deploy-cos-restart`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: deploy-cos-restart · pass: 1 · tip: 3770387d · house A: Grok FINDINGS: 5 · findings: 9 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 1 · house B: none (not needed) · suites: offline 9094/0 · with-DB 0/0 · live-note 148/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 11 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 216150
