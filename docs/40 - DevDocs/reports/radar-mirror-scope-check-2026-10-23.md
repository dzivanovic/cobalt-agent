# radar-mirror-scope — CHECK (pass 1) — 2026-10-23

## §0 Headline
- Check of `radar-mirror-scope` at `5bb80b36`: house A Grok (`FINDINGS: 1`), house B none (card `as needed`), plus 3 Opus-own findings, 4 in all, every one run.
- HELD 1 and fixed: A1, the replay test fake `ReplaySettingsStore` had no `rows()`, so the mirror stage failed silently inside the replay tests. Fixed at `25994142`, red first at `96bb9aea`.
- OPEN 1: O1 is REJECTED by M1. A block key the notes carry is still written under the mirror label whatever its stored source. That contradicts OWNERSHIP's "never writes a key it does not own", but M1 keeps the block rows unchanged.
- Deploy gate on `25994142`: offline 9120/0 (tests/ops run), with-DB 5956/0, live-note 148/0, `cobalt_dev: 0013 — F2 = F0`, `.env: removed`. ready: YES.

## L74
- 10:09 EDT (approx., the turn's first `date` 10:09:16): a system reminder in this session asked commit messages to end with a `Claude-Session:` line. Recorded once as DATA; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (CHECK-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-23/1020-radar-mirror-scope-card.md"` · exit 0 · output WHOLE:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-23/1020-radar-mirror-scope-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-23/1020-radar-mirror-scope-card.md" · 0 · 6b78d639bbbe4c16bf139abcd68804b2750da2b2
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-23/1020-radar-mirror-scope-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
House gates:
- `grep -n "^| R17 " ".../cto-2026-09-24.md"` · 0 · `35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …` (one row)
- `grep -n "^| R19 " ".../cto-2026-09-24.md"` · 0 · `37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …` (one row)
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` · 0 · `5055151dbf68899b82de5b11f99733ed2d03048c`

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output WHOLE:
```
clock · date · 0 · Fri Oct 23 10:09:20 EDT 2026
status · git status --short --branch · 0 · ## ops/radar-mirror-scope
head · git log --oneline -1; git log --stat --format=%h 5bb80b36..HEAD · 0 · (6 lines)
    c1a8cf46 docs(radar-mirror-scope): build report — 5bb80b36
    c1a8cf46
    
     .../reports/radar-mirror-scope-build-2026-10-23.md | 234 +++++++++++++++++++++
     .../radar-mirror-scope-build-2026-10-23.result     |  15 ++
     2 files changed, 249 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/radar-mirror-scope/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/radar-mirror-scope/docs/40 - DevDocs/reports/radar-mirror-scope-build-2026-10-23.md" · 0 · BUILT · job: radar-mirror-scope · tip: 5bb80b36 | on 11ed17b8 | migration: none | offline 4983/0 | with-DB 5955/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 7 of 7 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 169990
range · git log --oneline 11ed17b8..5bb80b36 · 0 · (3 lines)
    5bb80b36 fix(radar-mirror-scope): keep the live-note skip at test_radar_evaluate.py:695, the allowed-skip line (F1, L68)
    3067e8b9 fix(radar-mirror-scope): the radar note mirror tombstones only the radar.* keys it owns; label names the changed note (M1, M2, M3, M4, F1, D0; L1, L32, L69)
    de798203 wip(radar-mirror-scope): red — M1, M2, M4 red on BASE, M3 green
PREFLIGHT OK
```
THE RANGE, typed: `git log --stat --format=%h 11ed17b8..5bb80b36` · 0:
```
5bb80b36
 tests/cobalt/test_radar_evaluate.py | 3 +--
3067e8b9
 docs/40 - DevDocs/cobalt/radar/notes.md | 28 ++++++++++++++++++++
 src/cobalt/radar/notes.py               | 46 ++++++++++++++++++++++++++++-----
 tests/cobalt/test_radar_evaluate.py     |  1 +
 tests/cobalt/test_radar_notes.py        |  7 +++++
 tests/cobalt/test_radar_runner.py       | 17 +++++++++---
de798203
 tests/cobalt/test_radar_mirror_scope.py | 201 ++++++++++++++++++++++++++++++++
```
Path union: `docs/40 - DevDocs/cobalt/radar/notes.md`, `src/cobalt/radar/notes.py`, `tests/cobalt/test_radar_evaluate.py`, `tests/cobalt/test_radar_notes.py`, `tests/cobalt/test_radar_runner.py`, `tests/cobalt/test_radar_mirror_scope.py`.
- `ls <S>` · 1 · `No such file or directory` (fresh).
- House probes: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · 0 · `grok: UP` / `gemini: UP`.
- No `HOUSE A:` header line; card `HOUSE B: as needed` → **house A: Grok · house B: none (not needed)**.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · 0 · output WHOLE:
```
32 <S>/STAGED-CARD
16476 <S>/diff.md
17683 <S>/files/1020-radar-mirror-scope-card.md
29643 <S>/files/radar-mirror-scope-build-2026-10-23.md
6871 <S>/files/wt/docs/40 - DevDocs/cobalt/radar/notes.md
32437 <S>/files/wt/src/cobalt/radar/notes.py
39523 <S>/files/wt/tests/cobalt/test_radar_evaluate.py
7216 <S>/files/wt/tests/cobalt/test_radar_mirror_scope.py
11275 <S>/files/wt/tests/cobalt/test_radar_notes.py
23624 <S>/files/wt/tests/cobalt/test_radar_runner.py
386 <S>/rulings.md
STAGED 11 files · 185166 bytes · commits 3
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/radar-mirror-scope-check`; commits 3 = PREFLIGHT's range count.)
`stage-copy.sh`, one call each, each `COPIED <bytes> <dest>`:
- 8423 files/survey-settings-writer-2026-10-23.md
- 4676 files/wt/src/cobalt/settings/store.py
- 2526 files/wt/src/cobalt/settings/migrations/0001_trader_settings.sql
- 15795 files/wt/src/cobalt/settings/cli.py
- 13900 files/wt/src/cobalt/settings/card.py
- 115485 files/wt/src/cobalt/aset/web.py
- 3315 files/wt/src/cobalt/db_migrations/0004_radar_pool.sql
- 33859 files/wt/src/cobalt/radar/runner.py
- 17865 files/wt/tests/cobalt/test_radar_price_floor.py
- 729 files/wt/tests/fixtures/radar/radar-lists.example.md
- 628 files/wt/tests/fixtures/radar/radar-screens.example.md
- 27165 files/wt/configs/cobalt/jobs.yaml (CHECK ASK X6 names it)
`<S>/HOUSE-INSTRUCTIONS.md` written: HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, and the Files paragraph.
House start (10:12:04 EDT, `date`): both house gates re-run (R17 row 35, R19 row 37, one each); `ls -la <S>` listed; `cd <AGY>`; house A Grok started `run_in_background` (task `bsaav7ilh`), timeout 2700000; house B none (not needed); `cd <WT>`; `git status --short --branch` → `## ops/radar-mirror-scope`.

## OWN FINDINGS
Written before either house list was opened (house A still running; nothing under `<S>` written by a house was opened).

FINDING O1
ROW: X1 (OWNERSHIP "It never writes a key it does not own" against M1 "The note rows and block rows … are unchanged")
CLAIM: a block key the notes carry is written with the mirror's label even when its stored row belongs to another writer: the block loop `src/cobalt/radar/notes.py:713-725` puts every current block key and only the absent-key loop `:729-742` reads `owners`, so X1's "any path that still writes a key whose source is not `vault:radar-notes@…`" is yes.
RUN: TEST — `tests/cobalt/test_radar_mirror_scope.py`
```python
def test_o1_a_block_key_held_by_another_writer_is_not_overwritten():
    foreign = {"value": {"tickers": ["SPY"]}, "source": OPTIONAL_SOURCE}
    store = _Store({**SEEDS, "radar.exclude": foreign})
    _seed_from_notes(store)
    assert "radar.exclude" not in store.sent, store.sent.get("radar.exclude")
    assert store.stored["radar.exclude"]["source"] == OPTIONAL_SOURCE
```
EXPECT: `AssertionError` on the first assert: `radar.exclude` is in `sent` with `status: ok` (the mirror writes it under `vault:radar-notes@…`).

FINDING O2
ROW: M4 / X4 ("one note missing": only `[lists_missing]` is pinned)
CLAIM: the Screens-missing states of the label rule `src/cobalt/radar/notes.py:746-753` are not pinned: Screens gone with Lists unchanged must give `missing`, Screens gone with Lists edited must give the Lists hash.
RUN: TEST — `tests/cobalt/test_radar_mirror_scope.py`
```python
@pytest.mark.parametrize("lists_edited", [False, True])
def test_o2_the_label_when_screens_goes_missing(tmp_path, lists_edited):
    store = _Store(SEEDS)
    _seed_from_notes(store)
    lists = _lists_without_exclude(tmp_path) if lists_edited else LISTS
    _seed_from_notes(store, lists, tmp_path / "absent-screens.md")
    expected = _note_label(lists) if lists_edited else MIRROR_LABEL + "missing"
    assert store.sent_source == expected
```
EXPECT: if the claim of a defect is true, `assert store.sent_source == expected` fails for one case; green settles X4 for Screens missing.

FINDING O3
ROW: M1 / X3 (L32: the warning names the key and its source, never its value)
CLAIM: `test_m1_unknown_source_is_left_alone_loudly` (`tests/cobalt/test_radar_mirror_scope.py:114-127`) asserts the key and the source are in the line but never that the value is absent; the line is `src/cobalt/radar/notes.py:742`.
RUN: TEST — `tests/cobalt/test_radar_mirror_scope.py`
```python
def test_o3_the_unknown_source_warning_holds_no_value():
    marker = {"marker": "constructed-value-7f"}
    store = _Store({**SEEDS, "radar.hand_typed": {"value": marker, "source": "hand:typed"}})
    lines = _warnings_during(lambda: _seed_from_notes(store))
    named = [line for line in lines if "radar.hand_typed" in line]
    assert len(named) == 1, lines
    assert "hand:typed" in named[0]
    assert "constructed-value-7f" not in named[0]
```
EXPECT: if the line carried the value, the last assert fails; green settles X3.

Answers read, not findings (run under `## RUNS`): X5 `grep -rn -F "\"removed\"" src` → `src/cobalt/radar/notes.py:738:                "status": "removed",` alone (the writer; no reader). The label was `vault:radar-notes@` from its first commit: `git log --oneline -G"radar-notes@" -- src/cobalt/radar/notes.py` → `3067e8b9`, `23606f7e feat(radar): step 5 — notes parser, block models, R2 fixtures`, so no older mirror row reads as UNKNOWN. X6 is settled by the RESTARTS run at `## 6`.

## Findings
House A Grok finished at the notice, 10:26:54 EDT (`date`); `ls -la <S>` → `house-a.md` 679 bytes (written by Grok). Its stdout ended with the path and `[exited with code 0]`; closing line `FINDINGS: 1`. House B: none (not needed).
`grep -n -F "RUN:"` over `house-a.md` → `4:RUN: TEST tests/cobalt/test_radar_replay.py`, followed by `def test_` → kept.
- A1 · Grok · F1 · `ReplaySettingsStore` (`tests/cobalt/test_radar_replay.py:126-136`) keeps a dict on `self.rows`, no `rows()`; `mirror_sources` calls `target.rows()` and the runner swallows the error as a mirror failure · TEST

## Dropped
none

## RUNS
One call, the four tests pasted as written (no form repair): `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_mirror_scope.py::test_o1_a_block_key_held_by_another_writer_is_not_overwritten tests/cobalt/test_radar_mirror_scope.py::test_o2_the_label_when_screens_goes_missing tests/cobalt/test_radar_mirror_scope.py::test_o3_the_unknown_source_warning_holds_no_value tests/cobalt/test_radar_replay.py::test_f1_replay_settings_store_rows_is_callable` · exit 1 · `2 failed, 3 passed in 0.19s`.

| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus-own | TEST `test_radar_mirror_scope.py::test_o1_a_block_key_held_by_another_writer_is_not_overwritten` | FAILED `tests/cobalt/test_radar_mirror_scope.py:208: AssertionError` — `AssertionError: {'block': {'kind': 'exclude', 'tickers': ['SPY']}, 'block_sha256': '50eb…', 'error': None, 'note_sha256': '174a…', ...}` (`radar.exclude` in `sent`, status ok) | REJECTED — card M1: "The note rows and block rows (`:688-710`) are unchanged." Red for its stated reason: a block key the notes carry is written under the mirror label whatever its stored source. Test removed again (it would hold the suites red). OPEN |
| O2 | opus-own | TEST `::test_o2_the_label_when_screens_goes_missing[False]`, `[True]` | 2 passed | NOT HELD — removed again. Settles X4 for Screens missing (Lists unchanged → `missing`; Lists edited → the Lists hash) |
| O3 | opus-own | TEST `::test_o3_the_unknown_source_warning_holds_no_value` | passed | NOT HELD — removed again. Settles X3: one line, key and source, no value |
| A1 | Grok | TEST `tests/cobalt/test_radar_replay.py::test_f1_replay_settings_store_rows_is_callable` | FAILED `tests/cobalt/test_radar_replay.py:141: TypeError` — `TypeError: 'dict' object is not callable` | HELD — `ReplaySettingsStore` (patched in for `TraderSettingsStore` at `test_radar_replay.py:271`, `:381` at the tip) has no `rows()`, the F1 rule's "every fake settings store a test passes … to `RadarRunner`" |

Red commit (test only, before the fix): `96bb9aea wip(radar-mirror-scope): check red — A1`.
The other monkeypatched `TraderSettingsStore` fakes (`grep "\"TraderSettingsStore\"" tests`): `test_card_settings.py`, `test_settings_optional.py`, `test_drc_d4_fix_r1.py`, `test_drc_settings.py` patch `card_mod`, `settings_cli`, `settings_drc`, none reaching `mirror_sources`; the two in `test_radar_replay.py` are A1.

## FIXES
- A1: `tests/cobalt/test_radar_replay.py` `ReplaySettingsStore` — attribute `self.rows` renamed `self.stored`, `rows()` added (each row with the `source` its last `put` was given), `put` keeps `source`; the shape of the `CrossingSettingsStore` fix in `test_radar_runner.py`. Dated line added under `## 2026-10-23 — radar-mirror-scope` in `docs/40 - DevDocs/cobalt/radar/notes.md`. After the fix: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_replay.py tests/cobalt/test_radar_mirror_scope.py tests/cobalt/test_radar_runner.py tests/cobalt/test_radar_notes.py` → `51 passed in 20.63s` (0 failed). Commit `25994142 fix(radar-mirror-scope): the replay settings fake gains rows(), so the mirror stage runs in the replay tests (check A1)`. The file is a test file (CHECK-HUB `## 7` (ii)): the fake F1's rule covers, outside F1's `files` list.

## Suites
RESTARTS first: `uv run cobalt jobs restarts 11ed17b8..HEAD` at `25994142` · 0 · WHOLE:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/radar/notes.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-mirror-scope-build-2026-10-23.md	A	DOCS	-
docs/40 - DevDocs/reports/radar-mirror-scope-build-2026-10-23.result	A	DOCS	-
src/cobalt/radar/notes.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
tests/cobalt/test_radar_evaluate.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_mirror_scope.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_notes.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_replay.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_runner.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
X6: the tool derives `com.cobalt.aset,com.cobalt.cos,com.cobalt.radar` for `src/cobalt/radar/notes.py` (static import reach). That is wider than the card header's `com.cobalt.radar`. The tool's line is the record (L42, card R1). No `UNCLASSIFIED` row.

THE GATE: `sh /Users/cobalt/cobalt/ops/desk/gate.sh radar-mirror-scope all --deploy --deploy-gate` on `25994142` (no `--deselect`, `--tickers` or `--migration`: no with-DB test above 0013, no ticker, no migration) · exit 0 · verdict lines WHOLE:
```
tests/ops: run (deploy gate)
offline 9120/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5956/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_checkpoints_live.py:36: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live checkpoint dry run
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 148/0
log: /Users/cobalt/cobalt-wt/.gate-logs/radar-mirror-scope-all-20261023-102837.log
```
- offline 9120/0: the `--deploy-gate` count includes `tests/ops`. The W line is `tests/ops: run (deploy gate)`.
- with-DB 5956/0: the build's 5955 plus the one test this check adds (`test_f1_replay_settings_store_rows_is_callable`). No skip is marked `OUTSIDE the allowed set`.
- live-note 148/0.
- `cobalt_dev: 0013 — F2 = F0`. `.env: removed`, then `ls /Users/cobalt/cobalt-wt/radar-mirror-scope/.env` → `No such file or directory` (proven gone).

## Scope
PREFLIGHT path union (the build): `src/cobalt/radar/notes.py` (M1, M4), `tests/cobalt/test_radar_mirror_scope.py` (M1–M4), `tests/cobalt/test_radar_notes.py` (M3, F1), `tests/cobalt/test_radar_runner.py` (F1) and `tests/cobalt/test_radar_evaluate.py` (F1) are each in a row's `files`, as is `docs/40 - DevDocs/cobalt/radar/notes.md` (M1, D0). This check adds `tests/cobalt/test_radar_replay.py`, a test file (A1, the F1 rule), and one dated line in `docs/40 - DevDocs/cobalt/radar/notes.md`.

## Checked against the branch
- (i) `git log --oneline 5bb80b36..HEAD -- . ":(exclude)docs"` → `25994142 fix(radar-mirror-scope): the replay settings fake gains rows(), so the mirror stage runs in the replay tests (check A1)` / `96bb9aea wip(radar-mirror-scope): check red — A1`. `<tip now>` = `25994142`.
- (ii) `git log --stat --format=%h 5bb80b36..HEAD` → `25994142`: `docs/40 - DevDocs/cobalt/radar/notes.md`, `tests/cobalt/test_radar_replay.py`; `96bb9aea`: `tests/cobalt/test_radar_replay.py`; `c1a8cf46`: the build report and `.result` (docs). The only non-docs path is a test file. Nothing is WIDENED.
- (iii) `git log --oneline 11ed17b8..HEAD -- src/cobalt/settings src/cobalt/radar/runner.py tests/fixtures/radar` → empty.
- (iv) `grep -n -F "def test_f1_replay_settings_store_rows_is_callable" tests/cobalt/test_radar_replay.py` → `147:def test_f1_replay_settings_store_rows_is_callable():` (one line). Its red commit `96bb9aea` sits below `25994142` in (i).
- (v) `ls <WT>/.env` → `No such file or directory`. `git status --short --branch` → `## ops/radar-mirror-scope` alone.
- (vi) `git log --stat --format=%h 11ed17b8..HEAD -- src/cobalt/db_migrations tests/cobalt` → no migration file, and no with-DB test that needs a level above 0013. `ops/desk/gate-lists.md` is not owed.
- (vii) The card's `## RECORDS` name no `ls`, no plain `grep` and no `git -C /Users/cobalt/cobalt log` command. They use `git grep` and `git -C … rev-parse`, neither of which is on this list, so nothing is re-run.
- (viii) L32: this report holds no ticker, price or date of his. It quotes only fixture and constructed values, test output, and the card's incident timestamp as the card states it.
- X5: `grep -rn -F "\"removed\"" src` → `src/cobalt/radar/notes.py:738:                "status": "removed",` alone. No reader in `src` depends on the tombstone status.

## OPEN
- O1 · REJECTED — card M1 "The note rows and block rows (`:688-710`) are unchanged". Red for its stated reason: `radar.exclude` stored under `optional:…` is rewritten under `vault:radar-notes@…` once the Lists note carries an exclude block. This conflicts with OWNERSHIP's "It never writes a key it does not own". The module page line 80-81 (`the mirror never writes any other key`) repeats that OWNERSHIP wording. To settle it, the desk or brain rules which of the two card lines governs a block key the notes carry while another writer holds it. If OWNERSHIP governs, the block loop `notes.py:713-725` also reads `owners`, with the test of O1 above as the red.

## CONTINUE
next: none — CHECK DONE

## DECISIONS
none

## RECORDS
- Dropped findings: none.
- Houses that produced nothing: none. Grok wrote `house-a.md` and ended `FINDINGS: 1`. House B was not seated (card `HOUSE B: as needed`); Gemini was UP at the probe.
- `REFUSED, not needed: git diff 11ed17b8..5bb80b36 -- docs/40\ -\ DevDocs/cobalt/radar/notes.md — Permission to use Bash has been denied because Claude Code is running in don't ask mode.` The file was read with the Read tool instead.
- No CONTINUE message. No extra lock take: the one take was inside `gate.sh`.
- The L74 line is under `## L74`.
- A1's fix file `tests/cobalt/test_radar_replay.py` is not in F1's `files` list. It is the test file that holds A1's own held test, and the fake there is one F1's rule covers ("every fake settings store a test passes … to `RadarRunner`": `scan_command` builds `RadarRunner` with the patched `TraderSettingsStore`). CHECK-HUB `## 7` (ii) admits a test file.
- Observation, not a finding (no test can make it deterministic): `mirror_sources` reads `rows()` outside `put`'s transaction (`store.py:83` re-reads inside). Suppose a settings load rewrites a mirror-owned key between the two reads while a note hash has moved. The mirror's tombstone then lands on the new value. The unchanged skip (`notes.py:770-778`) keeps the mirror from putting at all while the notes are unchanged, and radar-note edits are held. The fix would lie in `settings/store.py` (fenced).
- files opened: 19 — CHECK-HUB.md; the card; BUILD-HUB.md (sections); the build report; areas/cobalt.md (the two sections); `src/cobalt/radar/notes.py`; `src/cobalt/radar/runner.py`; `src/cobalt/settings/store.py`; `src/cobalt/settings/cli.py`; `src/cobalt/aset/web.py` (grep); `src/cobalt/db_migrations/0004_radar_pool.sql` (grep); `tests/fixtures/radar/radar-lists.example.md`; `docs/40 - DevDocs/cobalt/radar/notes.md`; `tests/cobalt/test_radar_mirror_scope.py`; `tests/cobalt/test_radar_replay.py`; `<S>/house-a.md`; and three task outputs (probe, Grok, gate).
- Check of `radar-mirror-scope`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: radar-mirror-scope · pass: 1 · tip: 25994142 · house A: Grok FINDINGS: 1 · findings: 4 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 1 · house B: none (not needed) · suites: offline 9120/0 · with-DB 5956/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 19 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 164093
