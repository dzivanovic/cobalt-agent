# CHECK — disarm-one-tap-1008 (2026-10-09)

## §0 Headline
Check of `disarm-one-tap-1008` at `f70f3db8`: house A Sol (2 findings), house B Grok (0), Opus 5 own. 7 findings run: 0 held, 5 not held, 2 rejected by the card's own lines (open, follow-up).
No fix commit. Deploy gate green: offline 4045/0 · with-DB 4932/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed.
RESTARTS: `com.cobalt.aset com.cobalt.radar`. ready: YES · decisions: 0.

## L74
A system-reminder in this session asked for a `Claude-Session:` trailer line on commits. Recorded once as data; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` (12:26 EDT) → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" ".../CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" ".../134-disarm-one-tap-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- ".../134-disarm-one-tap-card.md" · 0 · 7728a319bbff46b010042a062d2b56421a57f0b0
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- ".../134-disarm-one-tap-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · ... · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ... | APPROVED |
STANDING LIST 2026-09-30 R60 committed · ... · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · ... · 0 · the row as grepped
RULING 2026-10-08 R689 row · ... · 0 · 42:| R689 | 11:47 ET | HIS RULING (words R689, standing): radar taps are one-tap, no typed text mid-session. DISARM reason chips (brain), card `134`, drafter prompt `133`. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW |
RULING 2026-10-08 R689 committed · ... · 0 · 1d5aa3f32f2abb231af963f7c0c11f55ab5022f4
RULING 2026-10-08 R689 at HEAD · ... · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 "` → line 35 (one row); `grep -n "^| R19 "` → line 37 (one row); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` → exit 0:
```
clock · date · 0 · Fri Oct  9 12:26:17 EDT 2026
status · git status --short --branch · 0 · ## ops/disarm-one-tap-1008
head · git log --oneline -1; git log --stat --format=%h f70f3db8..HEAD · 0 · (5 lines)
    81816e6d docs(disarm-one-tap-1008): build report — f70f3db8
    81816e6d
     .../reports/disarm-one-tap-build-2026-10-08.md     | 160 +++++++++++++++++++++
     1 file changed, 160 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/disarm-one-tap-1008/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/radar-top50-1009/.env
report · tail -n 3 ".../disarm-one-tap-build-2026-10-08.md" · 0 · BUILT · job: disarm-one-tap-1008 · tip: f70f3db8 | on 6f55636b | migration: none | offline 4045/0 | with-DB 4932/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 5 of 5 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 194339
range · git log --oneline 6f55636b..f70f3db8 · 0 · (2 lines)
    f70f3db8 feat(disarm-one-tap-1008): DISARM is one tap on a reason chip; the route refuses any value off the list (A, B, C, D; R689, L1, L3, L72)
    0d9d4f4a wip(disarm-one-tap-1008): red — DISARM chips route, render, tray seam and controls (A-D, R689)
PREFLIGHT OK
```
THE RANGE typed, `git log --stat --format=%h 6f55636b..f70f3db8`:
```
f70f3db8
 docs/40 - DevDocs/cobalt/aset/radar_panel.md |  3 +++
 docs/40 - DevDocs/cobalt/aset/web.md         |  3 +++
 src/cobalt/aset/radar_panel.py               | 27 +++++++++++++++++++++------
 src/cobalt/aset/web.py                       | 11 ++++++-----
 tests/cobalt/test_radar_panel_cards.py       |  2 +-
0d9d4f4a
 tests/cobalt/test_radar_panel_cards.py   | 87 +++++++++++++++++++++++++++++---
 tests/cobalt/test_s3_c3_panel_offline.py | 40 +++++++--------
```
Path union: `docs/40 - DevDocs/cobalt/aset/radar_panel.md`, `docs/40 - DevDocs/cobalt/aset/web.md`, `src/cobalt/aset/radar_panel.py`, `src/cobalt/aset/web.py`, `tests/cobalt/test_radar_panel_cards.py`, `tests/cobalt/test_s3_c3_panel_offline.py`.
The card carries no `DB:` key (its `## RECORDS` DB line): not a "DB: none" card.
`ls <S>` → `No such file or directory` (fresh).
House probe `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh` (background, exit 0):
```
sol: UP
grok: UP
gemini: UP
```
Seat order: house A: Sol (`gpt-5.6-sol`) · house B: Grok (`grok-4.7`). `HOUSE B: as needed` — mandatory rule does not apply; both seats are up.

## Files copied

## OWN FINDINGS
Written before either house's list was opened. Read: the card, `diff.md`, `src/cobalt/aset/radar_panel.py` `:1110`–`:1229`, `:1430`–`:1644`, `src/cobalt/aset/web.py` `_radar_form` `:1542`, `S3_TAP_SOURCES` / `_tap_reply` `:1670`–`:1726`, `_card_tap` `:1776`–`:1797`, `tests/cobalt/test_s3_c3_panel_offline.py` `:1`–`:130`, the build report's `## RESTARTS`, `## W`, `## PRE-STOP SELF-CHECK`, `## FOR THE CHECK`, last line.

FINDING O1
ROW: X2 / A
CLAIM: `web.py:2026` strips the posted reason before the list check, so a chip with spaces around it is accepted and the store gets the bare chip word; no test posts a padded chip (the build report says so itself, `## FOR THE CHECK` X2).
RUN: TEST — `tests/cobalt/test_s3_c3_panel_offline.py`
```python
def test_check_o1_a_padded_chip_reaches_the_store_as_the_bare_chip(gated):
    cards = gated("ARMED")
    response = client.post("/radar/card/1/disarm", data={"source": "panel", "reason": "  no volume  "})
    assert response.status_code == 200, response.text
    assert cards.reasons == ["no volume"]
```
EXPECT: green if the route stores the stripped chip (then NOT HELD: a coverage gap only); red `assert ['  no volume  '] == ['no volume']` if the unstripped value reached the store.

FINDING O2
ROW: X1
CLAIM: `PANEL_JS` (`radar_panel.py:1551` on) carries no `confirm(` that a chip tap could hit.
RUN: COMMAND — `grep -n -F "confirm(" src/cobalt/aset/radar_panel.py`
EXPECT: a line printed if a confirm dialog exists; no output (exit 1) otherwise.

FINDING O3
ROW: X1
CLAIM: `PANEL_JS` carries no `prompt(` (the free-text prompt `askReason` lives on the sheet in `web.py`, fenced).
RUN: COMMAND — `grep -n -F "prompt(" src/cobalt/aset/radar_panel.py`
EXPECT: a line printed if a prompt exists; no output (exit 1) otherwise.

FINDING O4
ROW: SCOPE / X3
CLAIM: the range touches no fenced file: nothing under `src/cobalt/cards/` and not `tests/cobalt/test_radar_panel.py` (the JS tests row C says stay as they are).
RUN: COMMAND — `git diff --stat 6f55636b f70f3db8 -- src/cobalt/cards tests/cobalt/test_radar_panel.py`
EXPECT: output lines if a fenced file changed; empty otherwise.

FINDING O5
ROW: A
CLAIM: a sheet-source post (`S3_TAP_SOURCES`, `web.py:1670`) with an off-list reason goes through the same `work` (`web.py:2023`–`:2033`) and is refused before the store; no test posts `source=sheet` to `/disarm`.
RUN: TEST — `tests/cobalt/test_s3_c3_panel_offline.py`
```python
def test_check_o5_a_sheet_source_off_list_reason_writes_nothing(gated, monkeypatch):
    cards = gated("ARMED")
    monkeypatch.setattr(web_module, "_render", lambda **kw: kw.get("banner", ""))
    response = client.post("/radar/card/1/disarm", data={"source": "sheet", "reason": "spread blew out"})
    assert response.status_code == 422, response.text
    assert "REFUSED: a DISARM reason is one of" in response.text
    assert cards.calls == []
```
EXPECT: green if the list check binds on the sheet source too (NOT HELD); red with a 200 or a call recorded if it does not.

## Findings
Both houses finished: Sol at 12:31:41 EDT (exit 0, final message `FINDINGS: 2`, written by me to `<S>/house-a.md` from its final message); Grok at 12:38:21 EDT (exit 0, wrote `<S>/house-b.md` = `FINDINGS: 0`; stdout: "The rows match the tip: the list check, the chip markup, the untouched script, and the controls are in place. No finding holds.").
THE DROP: both Sol blocks carry a `RUN:` line followed by a `def test_` or one `git diff` command line → both kept. Grok: no block.

| id | house | row | claim | run |
|---|---|---|---|---|
| O1 | Opus | X2/A | a padded chip is stripped and stored as the bare chip; no test posts one | TEST |
| O2 | Opus | X1 | no `confirm(` in `radar_panel.py` | COMMAND |
| O3 | Opus | X1 | no `prompt(` in `radar_panel.py` | COMMAND |
| O4 | Opus | SCOPE/X3 | the range touches nothing under `src/cobalt/cards` nor `test_radar_panel.py` | COMMAND |
| O5 | Opus | A | a `source=sheet` off-list post is refused 422 with nothing written | TEST |
| A1 | Sol | X2 | `" setup broke "` is stripped, reaches the store, answers 200 not 422 | TEST |
| A2 | Sol | SCOPE | the build added DevDocs page lines not in any row's `files` | COMMAND |

## Dropped
none

## RUNS
The three tests (O1, O5, A1) were pasted into `tests/cobalt/test_s3_c3_panel_offline.py` after `test_a_disarm_reason_off_the_list_is_refused`, unchanged, and run together: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_s3_c3_panel_offline.py::test_check_o1_a_padded_chip_reaches_the_store_as_the_bare_chip …::test_check_o5_a_sheet_source_off_list_reason_writes_nothing …::test_a_disarm_chip_with_spaces_around_it_is_refused` → `1 failed, 2 passed in 0.57s`; the failure: `AssertionError: {"status":"ok","card_id":1,"state":"WATCH","transition_id":77}` / `assert 200 == 422` (`test_s3_c3_panel_offline.py:305`). All three removed again with the Edit tool; `git status --short --branch` → `## ops/disarm-one-tap-1008` (clean).

| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | the test above | passed | NOT HELD — the padded chip is stored as `"no volume"`, the bare chip |
| O2 | Opus | `grep -n -F "confirm(" src/cobalt/aset/radar_panel.py` | no output (exit 1) | NOT HELD |
| O3 | Opus | `grep -n -F "prompt(" src/cobalt/aset/radar_panel.py` | no output (exit 1) | NOT HELD |
| O4 | Opus | `git diff --stat 6f55636b f70f3db8 -- src/cobalt/cards tests/cobalt/test_radar_panel.py` | empty | NOT HELD |
| O5 | Opus | the test above | passed | NOT HELD — a sheet-source off-list post is 422 with nothing written |
| A1 | Sol | the test above | `assert 200 == 422` | REJECTED — card row A: "`reason = form.get("reason", "").strip()`. If `reason not in DISARM_REASONS`, raise …": the strip comes before the list check by the row's own words, so `" setup broke "` is the chip `setup broke` and 200 is the specified answer (O1 shows the store gets the bare chip, never the padded text) |
| A2 | Sol | `git diff --name-only 6f55636b..HEAD -- 'docs/40 - DevDocs/cobalt/aset/radar_panel.md' 'docs/40 - DevDocs/cobalt/aset/web.md'` | `docs/40 - DevDocs/cobalt/aset/radar_panel.md` / `docs/40 - DevDocs/cobalt/aset/web.md` | REJECTED — `BUILD-HUB.md` `## E3`: "Each changed module gets ONE dated line in its page under `docs/40 - DevDocs/cobalt/`", and `CHECK-HUB.md` `## 7` (ii) holds only non-docs paths to the rows' `files`: the two lines are required by the hub, not outside scope |

held: 0 → no `wip(disarm-one-tap-1008): check red` commit.

## FIXES
none (held: 0).

## Suites
RESTARTS first, `uv run cobalt jobs restarts 6f55636b..HEAD` · 0:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/cobalt/aset/web.md	M	DOCS	-
docs/40 - DevDocs/reports/disarm-one-tap-build-2026-10-08.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/aset/web.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
tests/cobalt/test_s3_c3_panel_offline.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No UNCLASSIFIED row.
W on the tip `f70f3db8` (no commit of mine), ONE call: `sh /Users/cobalt/cobalt/ops/desk/gate.sh disarm-one-tap-1008 all --deploy` (background) · exit 0, done 13:08 EDT. No `--deselect` (no with-DB test in this range), no `--tickers`, no `--migration`. Verdict lines WHOLE:
```
offline 4045/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4932/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/disarm-one-tap-1008-all-20261009-123935.log
```
`grep -n -F "OUTSIDE" <log>` → nothing (no skip outside the allowed set). `grep -n -F "pass 1: whole (deploy)" <log>` → `937:pass 1: whole (deploy)`. The figures equal the build's own gate (offline 4045, with-DB 4932, live-note 146).
`.env`: `ls /Users/cobalt/cobalt-wt/disarm-one-tap-1008/.env` → `No such file or directory`.

## Scope
PREFLIGHT path union: `src/cobalt/aset/radar_panel.py`, `src/cobalt/aset/web.py` (rows A, B), `tests/cobalt/test_radar_panel_cards.py` (rows B, C, D), `tests/cobalt/test_s3_c3_panel_offline.py` (row A), and two DevDocs module pages (the hub's dated line). Commits of mine: none. Every non-docs path is in a row's `files`.

## Checked against the branch
- (i) `git log --oneline f70f3db8..HEAD -- . ":(exclude)docs"` → empty: no commit of mine; `<tip now>` = `f70f3db8`.
- (ii) `git log --stat --format=%h f70f3db8..HEAD` → `81816e6d` · `.../reports/disarm-one-tap-build-2026-10-08.md | 160 +++` only (docs).
- (iii) fenced paths: `git log --oneline 6f55636b..HEAD -- src/cobalt/cards` → empty; `… -- tests/cobalt/test_radar_panel.py` → empty; `… -- src/cobalt/db_migrations configs` → empty.
- (iv) no HELD finding: nothing to check.
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/disarm-one-tap-1008`.
- (vi) `git log --stat --format=%h 6f55636b..HEAD -- src/cobalt/db_migrations tests/cobalt` → only `tests/cobalt/test_radar_panel_cards.py` and `tests/cobalt/test_s3_c3_panel_offline.py` (offline files); no migration and no with-DB test file → no gate-list entry is owed.
- (vii) card RECORDS: `grep -rln -i disarm src` → among `.py` sources only `src/cobalt/cards/store.py`, `src/cobalt/cards/models.py`, `src/cobalt/aset/web.py`, `src/cobalt/aset/radar_panel.py` (the remaining hits are `__pycache__/*.pyc` binaries); no `src/cobalt/drc/*.py` and no `aset/drc_page.py` — matches the record. `ls /Users/cobalt/cobalt-wt` → `disarm-one-tap-1008` now exists (the record's "does not exist" was at drafting, before the build). The `grep … "<input name=\|…"` record is not re-run: its pattern carries `\|`, which this file's UNATTENDED RULES forbid.
- (viii) L32: this report holds no ticker, price or date of his; the values quoted are the card's chip words, hashes and constructed test strings.

## OPEN
- A1 (Sol, X2) REJECTED — `" setup broke "` answers 200 because row A strips before the list check. Settled by: a ruling that a padded value must be refused (then the strip moves after the check, or goes); until then the card's row stands. FOLLOW-UP.
- A2 (Sol, SCOPE) REJECTED — the DevDocs dated lines are required by `BUILD-HUB.md` `## E3`. Settled by: nothing to change; listed for the count. FOLLOW-UP.

## CONTINUE
next: done

## DECISIONS
none

## RECORDS
- House A Sol completion notice at 12:31:41 EDT (exit 0); left unread until house B finished at 12:38:21 EDT.
- Grok's `house-b.md` is the one line `FINDINGS: 0`; its stdout said "No finding holds."
- Dropped findings: none. Houses that produced nothing: none.
- REFUSED, not needed: none. CONTINUED: none. Extra lock takes: none (the gate's one take only, `lock: waited 0 min`).
- `areas/cobalt.md` (WHAT YOU READ (5)) was not opened in this session.
- files opened: 12 — `CHECK-HUB.md`; the card `134-disarm-one-tap-card.md`; `BUILD-HUB.md` (`## THE LOCK`, `## E2`–`## W`); `<S>/diff.md`; `src/cobalt/aset/radar_panel.py`; `src/cobalt/aset/web.py`; `tests/cobalt/test_s3_c3_panel_offline.py`; the build report `disarm-one-tap-build-2026-10-08.md`; `<S>/house-b.md`; Sol's output file; the house-probe output; the gate output.
- Check of `disarm-one-tap-1008`: house A `Sol`, house B `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: disarm-one-tap-1008 · pass: 1 · tip: f70f3db8 · house A: Sol FINDINGS: 2 · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 2 · house B: Grok FINDINGS: 0 · suites: offline 4045/0 · with-DB 4932/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 12 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 172187
