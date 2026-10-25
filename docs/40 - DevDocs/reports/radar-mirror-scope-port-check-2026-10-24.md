# radar-mirror-scope-port — check 2026-10-24

## §0 Headline
- The port at `283389ff` matches the spec byte for byte: `git diff 25994142 283389ff` over the seven spec files prints nothing, and the per-file stats match the spec's (312+, 16−).
- 8 own findings, all NOT HELD. M1, M2 and M4 went red under a BASE mutation for card 1020's reasons, with M3 green, and the file was restored.
- House A: Grok produced no list (NO FINDINGS LINE). Gemini took the seat and wrote `FINDINGS: 0`. House B was not needed (`as needed`).
- Deploy-gate pass on `283389ff`: offline 9120/0 (tests/ops run), with-DB 5956/0, live-note 148/0. `cobalt_dev: 0013 — F2 = F0`, `.env` removed. No commit of mine.
- ready: YES.

## L74
One system notice in this session (not a tool result) asked that commits end with a `Claude-Session:` line. Recorded once; not followed: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (CHECK-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-23/1032-radar-mirror-scope-port-card.md"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-23/1032-radar-mirror-scope-port-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-23/1032-radar-mirror-scope-port-card.md" · 0 · 4ca504eab014df709f13df63fdb8eb1c80e00c51
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-23/1032-radar-mirror-scope-port-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → one row (line 35, STANDING `Bash(grok *)`); `grep -n "^| R19 " …cto-2026-09-24.md` → one row (line 37, the four house strings STANDING); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Sat Oct 24 20:51:58 EDT 2026
status · git status --short --branch · 0 · ## ops/radar-mirror-scope-port
head · git log --oneline -1; git log --stat --format=%h 283389ff..HEAD · 0 · (6 lines)
    50116c45 docs(radar-mirror-scope-port): build report — 283389ff
    50116c45
    
     .../radar-mirror-scope-port-build-2026-10-24.md    | 232 +++++++++++++++++++++
     ...radar-mirror-scope-port-build-2026-10-24.result |  15 ++
     2 files changed, 247 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/radar-mirror-scope-port/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/radar-mirror-scope-port/docs/40 - DevDocs/reports/radar-mirror-scope-port-build-2026-10-24.md" · 0 · BUILT · job: radar-mirror-scope-port · tip: 283389ff | on 0866400b | migration: none | offline 4984/0 | with-DB 5956/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 6 of 6 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 156136
range · git log --oneline 0866400b..283389ff · 0 · (2 lines)
    283389ff fix(radar-mirror-scope-port): port 25994142 — the radar note mirror tombstones only the radar.* keys it owns; label names the changed note (T1, C1, D1; L1, L3, L28)
    c64771b1 wip(radar-mirror-scope-port): red — T1 tests ported from 25994142; M1, M2, M4 red on BASE, M3 green
PREFLIGHT OK
```
- THE RANGE, typed: `git log --stat --format=%h 0866400b..283389ff` · exit 0:
```
283389ff
 docs/40 - DevDocs/cobalt/radar/notes.md | 32 +++++++++++++++++++++++
 src/cobalt/radar/notes.py               | 46 ++++++++++++++++++++++++++++-----
 2 files changed, 72 insertions(+), 6 deletions(-)
c64771b1
 tests/cobalt/test_radar_evaluate.py     |   4 +-
 tests/cobalt/test_radar_mirror_scope.py | 201 ++++++++++++++++++++++++++++++++
 tests/cobalt/test_radar_notes.py        |   7 ++
 tests/cobalt/test_radar_replay.py       |  21 +++-
 tests/cobalt/test_radar_runner.py       |  17 ++-
 5 files changed, 240 insertions(+), 10 deletions(-)
```
Path union (for `## Scope`): the seven spec files.
- Card is not "DB: none" (no such header key): the DB-none diff row does not apply.
- `ls /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/radar-mirror-scope-port-check` · exit 1 · `No such file or directory` → fresh.
- House probes: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0 · `grok: UP` / `gemini: UP`.
- Seats: no `HOUSE A:` header line → house A: Grok · house B: none (not needed) — the card's line is `HOUSE B: as needed`.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0 · output whole:
```
37 <S>/STAGED-CARD
16990 <S>/diff.md
16347 <S>/files/1032-radar-mirror-scope-port-card.md
26883 <S>/files/radar-mirror-scope-port-build-2026-10-24.md
7144 <S>/files/wt/docs/40 - DevDocs/cobalt/radar/notes.md
32437 <S>/files/wt/src/cobalt/radar/notes.py
39523 <S>/files/wt/tests/cobalt/test_radar_evaluate.py
7216 <S>/files/wt/tests/cobalt/test_radar_mirror_scope.py
11275 <S>/files/wt/tests/cobalt/test_radar_notes.py
19995 <S>/files/wt/tests/cobalt/test_radar_replay.py
23624 <S>/files/wt/tests/cobalt/test_radar_runner.py
386 <S>/rulings.md
STAGED 12 files · 201857 bytes · commits 2
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/radar-mirror-scope-port-check`; `commits 2` = PREFLIGHT's range count.)
`## READ` files, each `stage-copy.sh` → `COPIED`:
- `COPIED 17683 <S>/files/1020-radar-mirror-scope-card.md`
- `COPIED 25412 <S>/files/radar-mirror-scope-check-2026-10-23.md`
- The spec bytes (`git show 25994142:<path>`): the house cannot run git; `git -C /Users/cobalt/cobalt-wt/radar-mirror-scope diff --stat 25994142` → empty (that worktree's tracked files equal `25994142`), so its seven files were copied: `COPIED 32437 …/files/spec-25994142/src/cobalt/radar/notes.py`, `COPIED 7216 …/tests/cobalt/test_radar_mirror_scope.py`, `COPIED 11275 …/tests/cobalt/test_radar_notes.py`, `COPIED 23624 …/tests/cobalt/test_radar_runner.py`, `COPIED 39523 …/tests/cobalt/test_radar_evaluate.py`, `COPIED 19995 …/tests/cobalt/test_radar_replay.py`, `COPIED 7144 …/docs/40 - DevDocs/cobalt/radar/notes.md`. Each byte count equals the tip copy's.
- `<S>/HOUSE-INSTRUCTIONS.md`: the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS` whole, and the Files paragraph.
- Launch: `date` → `Sat Oct 24 20:54:02 EDT 2026`; house gates R17, R19 one row each again; `ls -la <S>` (diff.md, files/, HOUSE-INSTRUCTIONS.md, rulings.md, STAGED-CARD); `cd <AGY>`; house A Grok started (`run_in_background`, timeout 2700000); `cd <WT>`; `git status --short --branch` → `## ops/radar-mirror-scope-port`.

## OWN FINDINGS
Written before either house list was opened. Each is a question the card's CHECK ASKS put; a run that shows no defect is `NOT HELD`.

FINDING O1
ROW: E1 / X1 (a)
CLAIM: A spec file at the tip differs from `25994142` (`src/cobalt/radar/notes.py:28` and the six other spec paths, ported by Edit hunk by hunk).
RUN: COMMAND `git diff 25994142 283389ff -- src/cobalt/radar/notes.py tests/cobalt/test_radar_mirror_scope.py tests/cobalt/test_radar_notes.py tests/cobalt/test_radar_runner.py tests/cobalt/test_radar_evaluate.py tests/cobalt/test_radar_replay.py "docs/40 - DevDocs/cobalt/radar/notes.md"`
EXPECT: any diff line (P0 found nothing from main since BASE, so none is admitted).

FINDING O2
ROW: E1 / X1 (b)
CLAIM: The port's per-file stat over the seven paths is not equal to the spec's.
RUN: COMMAND `git diff --stat 0866400b 283389ff -- <the seven paths>` beside `git diff --stat 11ed17b8 25994142 -- <the seven paths>`
EXPECT: a file whose count differs (spec: notes.py 46, test_radar_mirror_scope.py 201, test_radar_notes.py 7, test_radar_runner.py 17, test_radar_evaluate.py 4, test_radar_replay.py 21, radar/notes.md 32).

FINDING O3
ROW: SCOPE / X1 (c)
CLAIM: The range touches a code path beyond `src/cobalt/radar/notes.py` and the five test files, or a docs path beyond the module page, the build report and its `.result`.
RUN: COMMAND `git diff --stat 0866400b 283389ff -- src tests configs ops`, and `git diff --stat 0866400b HEAD`
EXPECT: a path outside those named.

FINDING O4
ROW: X2 (suite)
CLAIM: Card 1020's offline suite with the A1 file is not `0 failed` on the tip.
RUN: COMMAND `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_radar_mirror_scope.py tests/cobalt/test_radar_notes.py tests/cobalt/test_radar_runner.py tests/cobalt/test_radar_evaluate.py tests/cobalt/test_radar_price_floor.py tests/cobalt/test_drc_d4_fix_r1.py tests/cobalt/test_radar_replay.py`
EXPECT: a `failed` count above 0.

FINDING O5
ROW: T1 / X2 (red on BASE)
CLAIM: With `src/cobalt/radar/notes.py` returned to BASE bytes (the C1 hunks of `283389ff` undone by Edit, a mutation restored after), M1, M2, M4 are not red for card 1020's reasons, or M3 is not green.
RUN: COMMAND `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_radar_mirror_scope.py` under that mutation, then `git diff --stat -- src` empty after the restore
EXPECT: M1, M2 or `test_m4_the_source_names_the_note_that_changed` passing, or M3 failing.

FINDING O6
ROW: R1 / X3
CLAIM: The re-derived RESTARTS line is not `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`.
RUN: COMMAND `uv run cobalt jobs restarts 0866400b..283389ff`
EXPECT: a different last line, or an `UNCLASSIFIED` row.

FINDING O7
ROW: X4
CLAIM: A `## DEPLOY PROOF` line of the card (`1032-radar-mirror-scope-port-card.md:55-58`) is in a shape `ops/desk/deploy-smoke.sh` does not map, or `DEPLOY-HUB.md:11` does not admit, or the section reads `http://127.0.0.1:5010/` or holds a `uv run` line.
RUN: COMMAND `grep -n -F "grep -c -F" /Users/cobalt/cobalt/ops/desk/deploy-smoke.sh`, `grep -n -F "ls " /Users/cobalt/cobalt/ops/desk/deploy-smoke.sh`, `grep -n -F "Bash(grep *)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`, `grep -n -F "Bash(ls *)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`, and the card's lines 54-58 read
EXPECT: a marker shape with no mapping line, or a `Bash(...)` string missing from line 11, or `127.0.0.1` / `uv run` inside the section.

FINDING O8
ROW: DEPLOY PROOF (markers)
CLAIM: A marker's `after` does not hold on the tip (`MIRROR_SOURCE_PREFIX = ` count `1`, the M2 def count `1`).
RUN: COMMAND `grep -c -F "MIRROR_SOURCE_PREFIX = " src/cobalt/radar/notes.py` and `grep -c -F "def test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical" tests/cobalt/test_radar_mirror_scope.py`
EXPECT: a count other than `1`.

## Findings
- Grok (house A, first sitting): completion notice at `date` → `Sat Oct 24 21:00:23 EDT 2026`, exit 0; `ls -la <S>` → no `house-a.md`. Its stdout, verbatim: `I'll read the house instructions in full first, then follow them exactly.The check is a read of the port against the spec and the builder's report. I'll inventory the copied files, then write each finding before I read on.The report is in. Next I'll read the port card's deploy-proof and row text before writing anything.` — no list, no `FINDINGS:` line → NO FINDINGS LINE, nothing produced. The next house UP that has not sat, Gemini, takes seat A, ONE attempt (`## 3`): house gates R17, R19 one row each again; `cd <AGY>`; Gemini started (`run_in_background`, timeout 2700000); `cd <WT>`; `git status --short --branch` → `## ops/radar-mirror-scope-port`.
- Gemini (house A, second sitting): completion notice at `date` → `Sat Oct 24 21:02:19 EDT 2026`, exit 0. Its printed answer, whole: `FINDINGS: 0` (then the harness's `[exited with code 0]`). Written byte for byte without that trailer to `<S>/house-a.md` (12 bytes; `ls -la <S>`).
- House B: not seated (card `HOUSE B: as needed`).
- No house finding to keep. Rows kept: none.

## Dropped
none. Gemini wrote no FINDING block, and Grok wrote no list.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus | `git diff 25994142 283389ff -- src/cobalt/radar/notes.py tests/cobalt/test_radar_mirror_scope.py tests/cobalt/test_radar_notes.py tests/cobalt/test_radar_runner.py tests/cobalt/test_radar_evaluate.py tests/cobalt/test_radar_replay.py "docs/40 - DevDocs/cobalt/radar/notes.md"` | (no output) | NOT HELD |
| O2 | opus | `git diff --stat 0866400b 283389ff -- <seven>` · `git diff --stat 11ed17b8 25994142 -- <seven>` | both, identically: `radar/notes.md 32 +++++` · `notes.py 46 +++++++-` · `test_radar_evaluate.py 4 +-` · `test_radar_mirror_scope.py 201` · `test_radar_notes.py 7 ++` · `test_radar_replay.py 21 +++-` · `test_radar_runner.py 17 ++-` · `7 files changed, 312 insertions(+), 16 deletions(-)` | NOT HELD |
| O3 | opus | `git diff --stat 0866400b 283389ff -- src tests configs ops` · `git diff --stat 0866400b HEAD` | first: `src/cobalt/radar/notes.py 46`, the five test files, `6 files changed, 280 insertions(+), 16 deletions(-)`; second: those six + `docs/40 - DevDocs/cobalt/radar/notes.md 32` + `radar-mirror-scope-port-build-2026-10-24.md 232` + `.result 15`, `9 files changed, 559 insertions(+), 16 deletions(-)` | NOT HELD |
| O4 | opus | `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_radar_mirror_scope.py tests/cobalt/test_radar_notes.py tests/cobalt/test_radar_runner.py tests/cobalt/test_radar_evaluate.py tests/cobalt/test_radar_price_floor.py tests/cobalt/test_drc_d4_fix_r1.py tests/cobalt/test_radar_replay.py` | `107 passed, 1 skipped in 29.20s` | NOT HELD |
| O5 | opus | mutation: by Edit, `_mirror_rows`'s loop back to BASE's `if key.startswith("radar.") and key not in current_keys:` tombstone with no owner test and no warning, and the label back to `parsed.screens.note_sha256 or parsed.lists.note_sha256 or "missing"`; `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/cobalt/test_radar_mirror_scope.py`; then restored by Edit | `5 failed, 4 passed in 0.17s`: FAILED `::test_m1_unknown_source_is_left_alone_loudly` (`:121` `assert 'radar.hand_typed' not in {…}` — the key sent as a `removed` row); FAILED `::test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical` (`:139` `('radar.cards_enabled', {'block': None, … })` in `sent`); FAILED `::test_m4_the_source_names_the_note_that_changed` (`:168`, the label carries the other note's hash12); FAILED `::test_m4_the_label_in_each_case[lists_only]`, `[lists_missing]` (`:201`); M3 and M4 `[first]`, `[screens_only]`, `[both]` passed. After the restore: `git diff --stat -- src` → (no output); `git status --short --branch` → `## ops/radar-mirror-scope-port` | NOT HELD (M1, M2, M4 red for card 1020's reasons, M3 green) |
| O6 | opus | `uv run cobalt jobs restarts 0866400b..283389ff` | the table (under `## Suites`), last line `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`; `src/cobalt/radar/notes.py` `static import reach`; no `UNCLASSIFIED` | NOT HELD |
| O7 | opus | `grep -n -F "grep -c" /Users/cobalt/cobalt/ops/desk/deploy-smoke.sh` · `grep -n -F "ls " …deploy-smoke.sh` · `grep -n -F "Bash(grep *)" …DEPLOY-HUB.md` · `grep -n -F "Bash(ls *)" …DEPLOY-HUB.md`; card `:54-58` read | smoke script `:11` `#   grep -c -F "<fixed string>" <path>`, `:122` `'grep -c -F "'*)`, `:189` runs `grep -c -F -e`; `:10` `#   ls <path> \| ls "<path>"`, `:118` `"ls "*)`, `:188` runs `ls`. `DEPLOY-HUB.md:11` holds both `"Bash(grep *)"` and `"Bash(ls *)"`. The section's four lines are two `grep -c -F` and two `ls`; none reads `127.0.0.1` or holds `uv run` | NOT HELD |
| O8 | opus | `grep -c -F "MIRROR_SOURCE_PREFIX = " src/cobalt/radar/notes.py` · `grep -c -F "def test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical" tests/cobalt/test_radar_mirror_scope.py` | `1` · `1` | NOT HELD |

No test was added, so there is no `wip(radar-mirror-scope-port): check red` commit.

## FIXES
none. No finding held.

## Suites
RESTARTS (`BUILD-HUB.md` `## RESTARTS`): `uv run cobalt jobs restarts 0866400b..283389ff`, table whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/radar/notes.md	M	DOCS	-
src/cobalt/radar/notes.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
tests/cobalt/test_radar_evaluate.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_mirror_scope.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_notes.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_replay.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_runner.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
No `UNCLASSIFIED` row. (The range runs to the code tip `283389ff`; above it sit only the build report and its `.result`, both DOCS.)

W, ONE call, on tip `283389ff` (no commit of mine): `sh /Users/cobalt/cobalt/ops/desk/gate.sh radar-mirror-scope-port all --deploy --deploy-gate`. No `--deselect`, because the range adds no with-DB test; no `--tickers`; no `--migration`. Exit 0. Verdict lines whole:
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
log: /Users/cobalt/cobalt-wt/.gate-logs/radar-mirror-scope-port-all-20261024-210338.log
```
- offline: log `:957` `4984 passed, 878 skipped, 4 xfailed, 36 warnings in 730.82s (0:12:10)` and `:1032` (tests/ops) `4136 passed, 1 xfailed, 16 warnings in 902.16s (0:15:02)`, so 4984 + 4136 = `offline 9120/0`.
- with-DB: `:1049` `F0: 664 35 272c95bbb12241e3611e4b36326ccf87`; pass 1 `:1277` `5712 passed, 9 skipped, 138 deselected, 7 xfailed, 43 warnings in 896.20s (0:14:56)`; pass 2 `:2260` `244 passed, 1 deselected, 5 warnings in 245.14s (0:04:05)`; 5712 + 244 = 5956. `:2334` `F2: 664 35 272c95bbb12241e3611e4b36326ccf87`, equal to F0.
- live-note: `:2461` `148 passed, 1 skipped, 15 warnings in 26.49s`. The skip names `COBALT_TEST_LIVE_DRC`.
- `grep -n -F "OUTSIDE the allowed set" <log>` → no output.
- `.env`: `ls /Users/cobalt/cobalt-wt/radar-mirror-scope-port/.env` → `No such file or directory`, so `.env: removed, proven gone (W)`.

## Scope
PREFLIGHT's path union: `src/cobalt/radar/notes.py`, `docs/40 - DevDocs/cobalt/radar/notes.md`, `tests/cobalt/test_radar_mirror_scope.py`, `tests/cobalt/test_radar_notes.py`, `tests/cobalt/test_radar_runner.py`, `tests/cobalt/test_radar_evaluate.py`, `tests/cobalt/test_radar_replay.py`. Each path is in the `files` of row T1, C1 or D1. Above the tip are the build report and its `.result`, which the card admits. I made no commit.

## Checked against the branch
- (i) `git log --oneline 283389ff..HEAD -- . ":(exclude)docs"` → no output. I made no commit, so `<tip now>` = `283389ff`.
- (ii) `git log --stat --format=%h 283389ff..HEAD` → `50116c45`, holding only `radar-mirror-scope-port-build-2026-10-24.md` (232) and `.result` (15). No non-docs path.
- (iii) Fence: `git log --oneline 0866400b..HEAD -- src/cobalt/settings src/cobalt/radar/runner.py tests/fixtures/radar` → no output. `git log --oneline 0866400b..HEAD -- src` → `283389ff` alone, and its stat holds only `src/cobalt/radar/notes.py` (PREFLIGHT range). No path matches the card's git-command fences: the range is two commits, ported by Edit/Write as its messages state.
- (iv) No finding held, so there is no test to check.
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/radar-mirror-scope-port` alone.
- (vi) `git log --stat --format=%h 0866400b..HEAD -- src/cobalt/db_migrations tests/cobalt` → `c64771b1` with the five offline test files only. No migration and no with-DB test file, so `gate-lists.md` needs no change.
- (vii) Card `## RECORDS` commands: `ls /Users/cobalt/cobalt-wt/` → the listing holds `radar-mirror-scope`, `radar-mirror-scope-port` (the port, now built) and `deploy-radar-mirror-scope`. `git -C /Users/cobalt/cobalt log --oneline -6` → `612ab2b2`, `9c493c24`, `1e6ea99e`, `4ca504ea`, `e297ff7b`, `8a52f030` (all `docs(desk)`; main has moved past the drafter's `148b03ef`, as the card's DECISIONS 7 says the desk resets). The other records name `git grep`, `git rev-parse`, `git ls-tree`, which are not on this list and were not re-run. The marker reads were re-run on the tip as O8.
- (viii) L32: this report holds no ticker, price or date of his. It quotes only constructed fixture keys, test output, F-fingerprints and commit ids.
- X1–X5: X1 → O1, O2, O3; X2 → O4, O5; X3 → O6; X4 → O7; X5 kept: no finding re-decides card 1020's rows. Card 1020's check O1 (REJECTED there) is not re-opened.

## OPEN
none

## CONTINUE
next: none — CHECK DONE

## DECISIONS
none

## RECORDS
- Dropped findings: none.
- Houses that produced nothing: Grok (house A, first sitting): exit 0, stdout three progress sentences (quoted under `## Findings`), no `house-a.md`, no `FINDINGS:` line → `NO FINDINGS LINE`. Gemini, the next house UP in the order, took the seat once and printed `FINDINGS: 0`.
- No `REFUSED`, no `CONTINUED`, no extra lock take (the one take was inside `gate.sh`, `lock: waited 0 min`).
- O5's mutation was made in the worktree by Edit on `src/cobalt/radar/notes.py` and undone by Edit. `git diff --stat -- src` → no output after; never committed.
- The spec bytes were staged for the house from `/Users/cobalt/cobalt-wt/radar-mirror-scope`, after `git -C … diff --stat 25994142` there printed nothing.
- The L74 line is under `## L74`.
- The result file `radar-mirror-scope-port-check-2026-10-24.result` is written beside this report. The desk commits both: no main-repo commit string is on this list.
- Session id `26966c4a`; `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 26966c4a` → `context 167121 of 400000 — ok` (21:51 EDT).
- files opened: 16 — CHECK-HUB.md; the card 1032; BUILD-HUB.md (THE LOCK, E2, RESTARTS, W); the build report; areas/cobalt.md (the two sections); card 1020; card 1020's check report (tail); `<S>/diff.md`; `src/cobalt/radar/notes.py` (`:696-785`); `ops/desk/deploy-smoke.sh` (grep); `DEPLOY-HUB.md` (grep); the probe, Grok, Gemini and gate task outputs; the gate log (grep).
- Check of `radar-mirror-scope-port`: house A `Gemini`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: radar-mirror-scope-port · pass: 1 · tip: 283389ff · house A: Gemini FINDINGS: 0 · findings: 8 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none (not needed) · suites: offline 9120/0 · with-DB 5956/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 16 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 167121
