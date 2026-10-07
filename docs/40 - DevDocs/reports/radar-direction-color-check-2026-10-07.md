# radar-direction-color — CHECK 2026-10-07

## §0 Headline
Check of `radar-direction-color` on `6370ea6a`: houses Sol (2) and Grok (1), own read 0. One held (A1: an unhashable direction raised `TypeError` in `_direction_mark`), fixed at `541adf0c`.
Two rejected and open (A2, B1: row C's control also drops the IN-TRADE 1R/2R head, which the card names as direction-dependent by design).
Gate green: offline 3975/0 · with-DB 4859/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed. ready: YES.

## L74
The session's system context carried an attribution block asking commits to end with a `Claude-Session:` line (2026-10-07, at launch). Recorded as data; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-07/89-radar-direction-color-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-07/89-radar-direction-color-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-07/89-radar-direction-color-card.md" · 0 · 091eb75a4fec6b85d3eb8ad9cdbb470e994eb747
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-07/89-radar-direction-color-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-07 R625 row · grep -n "^| R625 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · 19:| R625 | 10:15 ET | HIS RULING (words: `cto-2026-10-07-words.md` R625): a radar card's header row and title are green for long, red for short; a short fix or a rework, the drafter sizes it. LAUNCHING a drafter, prompt `88`. | HIS RULING · APPROVED |
RULING 2026-10-07 R625 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R625 |" -- "docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · 33a49ab6048bcc5ae6f489310beb5e99978eadfd
RULING 2026-10-07 R625 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 "` → row 35 (STANDING `Bash(grok *)`); `grep -n "^| R19 "` → row 37 (four house strings pre-approved); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0:
```
clock · date · 0 · Wed Oct  7 11:48:16 EDT 2026
status · git status --short --branch · 0 · ## ops/radar-direction-color-1007
head · git log --oneline -1; git log --stat --format=%h 6370ea6a..HEAD · 0 · (5 lines)
    6a3bc41a docs(radar-direction-color): build report — 6370ea6a
    6a3bc41a
    
     .../radar-direction-color-build-2026-10-07.md      | 183 +++++++++++++++++++++
     1 file changed, 183 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/radar-direction-color-1007/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "…/radar-direction-color-build-2026-10-07.md" · 0 · BUILT · job: radar-direction-color · tip: 6370ea6a | on d2b53d6d | migration: none | offline 3973/0 | with-DB 4857/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 4 of 4 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 165689
range · git log --oneline d2b53d6d..6370ea6a · 0 · (2 lines)
    6370ea6a fix(radar-direction-color): strip and title carry the direction class, arrow and tint (A, B, C; L1, L3, L45)
    194ffbed wip(radar-direction-color): red
PREFLIGHT OK
```
THE RANGE, `git log --stat --format=%h d2b53d6d..6370ea6a`:
```
6370ea6a
 docs/40 - DevDocs/cobalt/aset/radar_panel.md |  3 +++
 src/cobalt/aset/radar_panel.py               | 24 ++++++++++++++++++++----
 tests/cobalt/test_radar_panel_cards.py       |  7 +++++--
194ffbed
 tests/cobalt/test_radar_panel_cards.py | 175 +++++++++++++++++++++++++++++++++
```
Path union: `docs/40 - DevDocs/cobalt/aset/radar_panel.md`, `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_radar_panel_cards.py`. Card has no `DB: none` key.
`ls <S>` → `No such file or directory` (fresh).
HOUSE PROBES: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh` · exit 0:
```
sol: UP
grok: UP
gemini: UP
```
Seat order → house A: Sol (`gpt-5.6-sol`) · house B: Grok (`grok-4.7`). HOUSE B: as needed.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"`:
```
22346 …/radar-direction-color-check/diff.md
11434 …/radar-direction-color-check/files/89-radar-direction-color-card.md
23264 …/radar-direction-color-check/files/radar-direction-color-build-2026-10-07.md
19553 …/radar-direction-color-check/files/wt/docs/40 - DevDocs/cobalt/aset/radar_panel.md
82911 …/radar-direction-color-check/files/wt/src/cobalt/aset/radar_panel.py
48302 …/radar-direction-color-check/files/wt/tests/cobalt/test_radar_panel_cards.py
341 …/radar-direction-color-check/rulings.md
STAGED 7 files · 208151 bytes · commits 2
```
`stage-copy.sh …/src/cobalt/aset/web.py <S>/files/wt/src/cobalt/aset/web.py` → `COPIED 104855 …/files/wt/src/cobalt/aset/web.py`.
`<S>/HOUSE-INSTRUCTIONS.md` written (13417 bytes). Houses started 11:49:34 EDT: Sol (`b2fcqshuk`), Grok (`b3xynwfmr`); `cd` back, `git status --short --branch` → `## ops/radar-direction-color-1007`.

## OWN FINDINGS
Written 11:51 EDT, before either house list was opened. Read: the card, rulings (R625), `git diff d2b53d6d..6370ea6a` (src, tests, docs), `radar_panel.py:1381`–`:1516` at tip, `mirrorStale` (`:1575`), the build report's `## RESTARTS`, `## W`, `## PRE-STOP SELF-CHECK`, `## FOR THE CHECK`, `## DECISIONS`, last line; `areas/cobalt.md` from `## What Cobalt is` and `## Build rules` down.
What I checked and found built as the rows say (no defect to run):
- A: `_DIRECTION_MARK` / `_direction_mark` (`radar_panel.py:1381`–`:1391`) read by `_card_detail` (`:1433`, `:1436`–`:1437`) and `render_ladder` (`:1479`, `:1482`–`:1483`); the arrow sits in the third span, `<b>` unchanged; terminal rows (`:1494`–`:1499`) unchanged; the class word now comes from the map, not the raw value.
- B: `:1513` is the one new line, between the body line and the first `@media`; no existing line changed (diff shows `+` only for that line).
- C: only the LADDER pin line changed (`tests/cobalt/test_radar_panel_cards.py:397`), POOL and API pins unchanged; comment line added at `:395`.
- X3: `mirrorStale` reads `item.querySelector('.strip b')` → `b.firstChild.nodeValue` (`:1575`); the `<b>` still opens with the ticker. `.strip span:nth-child(4)` still matches only the 4th child span; the new arrow span is child 1 of the 3rd span.
- X2: the two hex values in `:1513` (`#0f2a1c`, `#3a1119`) occur in `.dot.filled.colour-2` / `.colour-0` on `:1512`; no `dir-unknown` or `.direction.unknown` rule.
- Scope: the range touches `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_radar_panel_cards.py`, the module's docs page; nothing in the fence.
- Noted, not a defect: row C's body comparison also drops the IN-TRADE head's `next exits` 1R/2R values (a fourth removal beyond the card's three); the builder disclosed it as ASK DESK 1 and asserts it happens once per FILLED card.
OWN FINDINGS: 0

## Findings
Sol finished 11:53:22 EDT (exit 0; final message written by me to `<S>/house-a.md`, `FINDINGS: 2`). Grok finished 12:00:30 EDT (exit 0; wrote `<S>/house-b.md` itself, `FINDINGS: 1`). Every block has a `RUN:` line followed by a `def test_`; none dropped.
| id | house | row | claim | run |
|---|---|---|---|---|
| A1 | Sol | A | `_DIRECTION_MARK.get(card.direction, …)` (`radar_panel.py:1389`) raises for an unhashable direction instead of rendering the unknown mark | TEST |
| A2 | Sol | C | the body-control helper (`test_radar_panel_cards.py:794`) also drops the IN-TRADE `next exits` values, beyond row C's three fields | TEST |
| B1 | Grok | C | with only row C's three drops, the FILLED card's long/short blocks differ at the IN-TRADE `next exits` head (`radar_panel.py:1350`) | TEST |

## Dropped
none

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| A1 | Sol | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_panel_cards.py::test_radar_any_other_direction_is_marked_never_guessed` | `2 failed in 0.84s`; first: `E       TypeError: cannot use 'list' as a dict key (unhashable type: 'list')` at `src/cobalt/aset/radar_panel.py:1389` | HELD |
| A2 | Sol | `…::test_radar_direction_body_control_drops_only_the_three_named_fields` | `1 failed in 0.61s`; `E       assert 'next exits <value> / <value></div>' in '<div class="expanded" data-state="IN-TRADE">…'` | REJECTED — row C: "the `LEVELS` 1R/2R fields, which differ by the sign (`:908`)". The `next exits` head (`radar_panel.py:1350`–`:1351`) prints the same `card.target_1r` / `card.target_2r`, so it differs by direction by the design row C names; the builder disclosed the fourth drop (build report ASK DESK 1). Test removed. OPEN |
| B1 | Grok | `…::test_three_named_drops_leave_the_filled_in_trade_head_different` | `1 failed in 0.67s`; `E               AssertionError: 4` … `- t exits <value> / <value></div><` / `+ t exits <value> / <value></div><` | REJECTED — same row C line as A2; the only difference is the 1R/2R targets in the IN-TRADE head. Test removed. OPEN |
Held test committed red: `789ac7d0 wip(radar-direction-color): check red — A1`.

## FIXES
| id | fix | test | commit |
|---|---|---|---|
| A1 | `_direction_mark` (`radar_panel.py:1387`–`:1392`) looks up the map only when `isinstance(card.direction, str)`; any other value → `_DIRECTION_UNKNOWN` / word `unknown`. Doc line added under `## 2026-10-07 — radar-direction-color` in `docs/40 - DevDocs/cobalt/aset/radar_panel.md` | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_panel_cards.py tests/cobalt/test_radar_panel.py` → `146 passed, 2 skipped in 2.10s` (skips: `test_radar_panel_cards.py:202: reaches cobalt_dev (lock-relief G1)`, `test_radar_panel.py:1496: requires_db`); the ladder pin unchanged and green | `541adf0c fix(radar-direction-color): any non-str direction renders unknown, never raises (check A1)` |

## Suites
RESTARTS (before the gate), `uv run cobalt jobs restarts d2b53d6d..HEAD`:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-direction-color-build-2026-10-07.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
`sh /Users/cobalt/cobalt/ops/desk/gate.sh radar-direction-color-1007 all --deploy` on `541adf0c` · exit 0 (no `--deselect`, `--tickers` or `--migration`: no with-DB test or migration added). Verdict lines, whole:
```
offline 3975/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4859/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/radar-direction-color-1007-all-20261007-120141.log
```
offline 3975 = the build's 3973 + the 2 cases of A1. `grep -n -F "OUTSIDE" <log>` → nothing. `ls <WT>/.env` → `No such file or directory` (12:29 EDT).

## Scope
Range union (PREFLIGHT) plus my commits: `src/cobalt/aset/radar_panel.py` (rows A, B), `tests/cobalt/test_radar_panel_cards.py` (rows A–C), `docs/40 - DevDocs/cobalt/aset/radar_panel.md` (doc line), the build report (docs). Nothing outside the rows' files.

## Checked against the branch
- (i) `git log --oneline 6370ea6a..HEAD -- . ":(exclude)docs"` → `541adf0c fix(radar-direction-color): any non-str direction renders unknown, never raises (check A1)` · `789ac7d0 wip(radar-direction-color): check red — A1`. tip now `541adf0c`.
- (ii) `git log --stat --format=%h 6370ea6a..HEAD` → `541adf0c`: `docs/40 - DevDocs/cobalt/aset/radar_panel.md`, `src/cobalt/aset/radar_panel.py`; `789ac7d0`: `tests/cobalt/test_radar_panel_cards.py`; `6a3bc41a`: the build report. All in rows' files, tests or docs.
- (iii) `git log --oneline d2b53d6d..HEAD -- src/cobalt/aset/web.py` → empty. The diff touches no other `src/` or test file ((ii) and PREFLIGHT range).
- (iv) `grep -n -F "def test_radar_any_other_direction_is_marked_never_guessed" tests/cobalt/test_radar_panel_cards.py` → `839:` one line; `789ac7d0` (red) sits below `541adf0c` (fix) in (i).
- (v) `ls <WT>/.env` → No such file; `git status --short --branch` → `## ops/radar-direction-color-1007`.
- (vi) `git log --stat --format=%h d2b53d6d..HEAD -- src/cobalt/db_migrations tests/cobalt` → only `tests/cobalt/test_radar_panel_cards.py` (offline tests); no migration, no with-DB test above `0013`: gate lists not needed.
- (vii) card record `git -C /Users/cobalt/cobalt diff --stat HEAD -- src tests configs/cobalt/jobs.yaml` → nothing (as recorded). The `rev-parse` record is not on my list; not run. The RESTARTS record matches the table above.
- (viii) L32: values from failing test output are written `<value>`; no real ticker, price or date of his.

## OPEN
- A2 (Sol), B1 (Grok) — REJECTED, FOLLOW-UP: row C's body comparison also strips the IN-TRADE head's `next exits {target_1r} / {target_2r}` (`radar_panel.py:1350`–`:1351`), a fourth removal beyond the card's three. Their tests run red for the stated reason; the values are the same sign-derived 1R/2R targets row C names as differing by design (`:908`). What would settle it: the card owner accepts the fourth drop (build report ASK DESK 1), or the helper is narrowed to remove only the card's exact `target_1r` / `target_2r` string from that head.

## CONTINUE
next: none — CHECK DONE

## DECISIONS
none

## RECORDS
- L74: the attribution block asking for a `Claude-Session:` line (see `## L74`); not acted on.
- Houses: Sol `FINDINGS: 2` (11:53:22), Grok `FINDINGS: 1` (12:00:30); none produced nothing. No dropped finding.
- No `REFUSED, not needed` line; no `CONTINUED` line; no by-hand lock take (one take, inside `gate.sh`).
- files opened: 13 — `CHECK-HUB.md`, the card, `BUILD-HUB.md` (THE LOCK → W), `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down), `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_radar_panel_cards.py`, the build report, `docs/40 - DevDocs/cobalt/aset/radar_panel.md`, the probe output, Sol's output, Grok's output, `<S>/house-b.md`, the gate output.
- Check of `radar-direction-color`: house A `Sol`, house B `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: radar-direction-color · pass: 1 · tip: 541adf0c · house A: Sol FINDINGS: 2 · findings: 3 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 2 · house B: Grok FINDINGS: 1 · suites: offline 3975/0 · with-DB 4859/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 13 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 148149
