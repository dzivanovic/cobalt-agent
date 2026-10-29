# sheet-check-warns — build report 2026-10-29 (routed card, BAND MID, builder grok-4.7, gate seat sheet-check-warns-gate)

## §0 Headline
- The sheet check warns, never refuses (R2563): `sheet_warning` replaces `assert_sheet_matches`; `/size` and the radar key tap write the card and carry the warning; the grade check and an unresolved mode still refuse.
- Built by grok-4.7 in two passes (T, S), no re-pass; suites at first run green: offline 5039/0, with-DB 6011/0, live-note 148/0; `cobalt_dev` 0013, F2 = F0.
- RESTARTS (committed range): com.cobalt.aset com.cobalt.cos com.cobalt.radar.
- Two decisions: the untracked `SHADOW-INSTRUCTIONS.md` in the HEAD RESTARTS table; T1 (b), (c) never shown red, no mutations (self-check 2 of 3).

## L74
none

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh shadow "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-29/1082-sheet-check-warns-card.md"`:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-29/1082-sheet-check-warns-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-29/1082-sheet-check-warns-card.md" · 0 · 597c9a7533bba03b4e65ea8bf7119f45b7263476
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-29/1082-sheet-check-warns-card.md" · 0 · nothing
STANDING LIST 2026-10-11 R1069 row · grep -n "^| R1069 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 74:| R1069 | 10:37 ET | HIS RULING · APPROVED (via the brain, L79; words R1069): OpenAI available, tribunal seats approved, no stops, no design round; deploy 324, install SHADOW-HUB, Grok, Sonnet, Terra arms in parallel (only the lock serializes). | APPLIED: cobalt.md NOW 11:17 |
STANDING LIST 2026-10-11 R1069 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1069 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 2322ed1e5044b6ec734e2cd0d225252408f87dbd
STANDING LIST 2026-10-11 R1069 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
RULING 2026-10-29 R2563 row · grep -n "^| R2563 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-29.md" · 0 · 13:| R2563 | 11:05 ET | HIS RULING · APPROVED ("enable everything I need to use. I want all enabled"): all day modes enabled; desk reading: sheet check warns, never refuses (A). Drafter prompt 1080 → cards 1081, 1082. | APPROVED — pending fold |
RULING 2026-10-29 R2563 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R2563 |" -- "docs/40 - DevDocs/reports/cto-2026-10-29.md" · 0 · 868d51c0f73ee71ddee4b9c91c1ea85ce0a3c808
RULING 2026-10-29 R2563 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-29.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh shadow "<card>"`:
```
clock · date · 0 · Thu Oct 29 17:51:19 EDT 2026
status · git status --short --branch · 0 · ## ops/sheet-check-warns
head · git log --oneline -1 · 0 · 78a6ab4ac docs(desk): R2558 day-open 10-27 GREEN
diff · git diff --stat 78a6ab4a · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/sheet-check-warns · 0 · 78a6ab4ac docs(desk): R2558 day-open 10-27 GREEN
env here · ls /Users/cobalt/cobalt-wt/sheet-check-warns/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
- Routed card: no `SHADOW OF:` (SHADOW-HUB `:28`, `:57`); BAND MID → builder `grok-4.7` (SHADOW-HUB `## BUILDERS`, band row MID). No original build, so no admitted exceptions.
- `git show --stat 78a6ab4a` → `docs(desk): R2558 day-open 10-27 GREEN`, 2 files under `docs/40 - DevDocs/reports/`.
- `uv run cobalt jobs restarts 78a6ab4a..HEAD` → `path	change	rule	restart` / `RESTARTS: none` (empty range).
- Symbols (Grep `assert_sheet_matches|sheet_warning` over `src`, `tests`): `src/cobalt/daymode/match.py:80` def, `:146` `__all__`; `src/cobalt/daymode/__init__.py:27`, `:62`; `src/cobalt/aset/web.py:57` import, `:536` docstring, `:609` banner, `:968` comment, `:1033` `/size`, `:1771` radar key; `tests/cobalt/test_daymode.py:33,401,413,418,422,424,428,525`; `tests/cobalt/test_sheet_daymode_probe.py:128`. `sheet_warning`: no hit. Every `file:line` of the card re-read with Read: `match.py:71-146`, `config.py:189-239`, `web.py:530-640`, `:960-1100`, `:1740-1801`, `test_daymode.py:385-530`, `test_aset_web.py:40-101`, `:405-464`, `test_radar_card_routes.py:55-124`, `test_sheet_daymode_probe.py:118-135` — each as the card states.
- `wc -l`: `match.py` 146 · `daymode/__init__.py` 69 · `aset/web.py` 2457 · `test_daymode.py` 885 · `test_aset_web.py` 939 · `test_radar_card_routes.py` 151 · `test_sheet_daymode_probe.py` 202.
- Card `## RECORDS` re-read: `grep -c -F "assert_sheet_matches(" /Users/cobalt/cobalt/src/cobalt/aset/web.py` → `3`; `grep -c -F "def assert_sheet_matches(" …/match.py` → `1`; `grep -c -F "def sheet_warning(" …/match.py` → `0` (the DEPLOY PROOF "before" values). DevDocs pages exist: `docs/40 - DevDocs/cobalt/daymode/match.md`, `docs/40 - DevDocs/cobalt/aset/web.md`.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `5038 passed, 878 skipped, 4 xfailed, 36 warnings in 801.97s (0:13:21)`; 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 26.06s`; the skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## PASSES
| pass | env check | command as run | wall | tokens | diff stat | commit |
|---|---|---|---|---|---|---|
| T | `ls -la /Users/cobalt/cobalt-wt/sheet-check-warns/.env` → `ls: /Users/cobalt/cobalt-wt/sheet-check-warns/.env: No such file or directory` | `grok -m grok-4.7 --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/sheet-check-warns/**)" -p "You are GROK (xAI), building a card. Read SHADOW-INSTRUCTIONS.md in this folder whole first and follow it exactly. Pass T: tests only under tests/. Write only the rows' files. Run no command. Reply with the list of files you wrote."` | 18:06:54 → 18:11:57 EDT (5 min) | UNKNOWN (L70: grok prints none) | `tests/cobalt/test_aset_web.py 26 +++++++++++---------` · `tests/cobalt/test_daymode.py 41 ++++++++++++++++----------------` · `tests/cobalt/test_radar_card_routes.py 19 ++++++++++++---` · `tests/cobalt/test_sheet_daymode_probe.py 4 ++--` · `4 files changed, 54 insertions(+), 36 deletions(-)` | `662c31fc7 wip(sheet-check-warns): red` |
| S | `ls -la /Users/cobalt/cobalt-wt/sheet-check-warns/.env` → `ls: /Users/cobalt/cobalt-wt/sheet-check-warns/.env: No such file or directory` | `grok -m grok-4.7 --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/sheet-check-warns/**)" -p "You are GROK (xAI), building a card. Read SHADOW-INSTRUCTIONS.md in this folder whole first and follow it exactly. Pass S: the rows. Write only the rows' files. Run no command. Reply with the list of files you wrote."` | 18:12:28 → 18:16:26 EDT (4 min) | UNKNOWN (L70) | `docs/40 - DevDocs/cobalt/aset/web.md 7 +++` · `docs/40 - DevDocs/cobalt/daymode/match.md 3 ++` · `src/cobalt/aset/web.py 74 +++++++++++++++++++------------` · `src/cobalt/daymode/__init__.py 7 +--` · `src/cobalt/daymode/match.py 58 ++++++++++++------------` · `5 files changed, 88 insertions(+), 61 deletions(-)` | `011075704 feat(sheet-check-warns): rows` |

Grok's reply (whole): `I'll read SHADOW-INSTRUCTIONS.md first and follow it exactly.Pass S is the source rows only. I'll re-read the cited lines, then write just those files.The sheet check becomes a warning on the two card paths and the banner. I'll write only those source and DevDocs files.- src/cobalt/daymode/match.py - src/cobalt/daymode/__init__.py - src/cobalt/aset/web.py - docs/40 - DevDocs/cobalt/daymode/match.md - docs/40 - DevDocs/cobalt/aset/web.md [exited with code 0]`

SCOPE: every path of both passes is a row's file; no `SCOPE` record.

Grok's reply (whole): `I'll read the card instructions in this folder first and follow them exactly.Pass T is tests only. I'll read the card's cited sources and the four test files before writing any row.The sheet check stays a warning in the tests: `sheet_warning` is what they call, and the card paths assert the warning instead of a refusal. I’ll edit only those four test files.- tests/cobalt/test_daymode.py - tests/cobalt/test_aset_web.py - tests/cobalt/test_radar_card_routes.py - tests/cobalt/test_sheet_daymode_probe.py [exited with code 0]`

## E2 RED
- T1's RUN on BASE's `src/`: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_daymode.py tests/cobalt/test_radar_card_routes.py` → exit 2, `1 error in 0.48s`: `E   ImportError: cannot import name 'sheet_warning' from 'cobalt.daymode.match'` (T1 (a), as named; collection stops, so (d) is read in the next run).
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_card_routes.py tests/cobalt/test_aset_web.py tests/cobalt/test_sheet_daymode_probe.py` → `3 failed, 39 passed, 29 skipped in 5.83s`:
  - `test_a_plus_key_tap_on_the_half_day_records_a_plus_sizes_at_a_70_with_notice` → `E       KeyError: 'sheet_warning'` (T1 (d) `:83-92`, the new `is None` assertion)
  - `test_the_hotkey_file_mismatch_warns` → `E       assert 409 == 200` (T1 (d), as named)
  - `test_nothing_attested_warns` (radar) → `E       assert 409 == 200` (T1 (d) new test, as named)
  - every skip: `reaches cobalt_dev (lock-relief G1)` in `test_aset_web.py`, among them `:433`, `:445` (T1 (c)).
- T1 (b) `test_daymode.py::TestDayModeStore::test_a_card_warns_while_the_attested_sheet_disagrees` and T1 (c) `test_aset_web.py::TestMatchCheckAtTheSheet::test_full_sheet_attested_on_a_reduced_day_warns`, `::test_nothing_attested_warns`: with-DB, no lock take at E2 → red UNPROVEN (L70), `## DECISIONS`.
- `test_sheet_daymode_probe.py`: docstring only (`:127-129`), green.

## E3 THE ROWS
Pass S (row in `## PASSES`) wrote M1, W1, W2, W3, D1; the seat edited no `src/` or `tests/` file (SHADOW-HUB RULES OF THE SEAT), so BUILD-HUB E3's mutations were not made (`## DECISIONS` 2).
- The touched files' offline run (card ORDER): `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_daymode.py tests/cobalt/test_radar_card_routes.py tests/cobalt/test_aset_web.py tests/cobalt/test_sheet_daymode_probe.py` → `122 passed, 40 skipped in 6.13s`; every skip `Postgres env settings not available` (`test_daymode.py`) or `reaches cobalt_dev (lock-relief G1)` (`test_aset_web.py`).
- Grep `assert_sheet_matches` over `src/**/*.py`, `tests/**/*.py` → no match. Grep `sheet_warning\(` over `src` → `src/cobalt/daymode/match.py:84:def sheet_warning(`, `src/cobalt/aset/web.py:609` (banner), `:1031` (`/size`), `:1781` (radar key).

## RESTARTS
- `uv run cobalt jobs restarts 78a6ab4a..HEAD` → exit 1, `FAILED: RestartError: one or more changed paths were unclassified`; table: `SHADOW-INSTRUCTIONS.md	A	UNCLASSIFIED	com.cobalt.agent,com.cobalt.aset,com.cobalt.cos,com.cobalt.herdr,com.cobalt.mainframe,com.cobalt.obsidian,com.cobalt.radar` / `ESCALATE: unclassified path SHADOW-INSTRUCTIONS.md`, plus the report (`DOCS`) and the committed paths below; last line `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.cos com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar`. The UNCLASSIFIED path is the untracked, never-committed harness file (`## DECISIONS` 1).
- `uv run cobalt jobs restarts 78a6ab4a..011075704` (the committed tip), WHOLE:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/web.md	M	DOCS	-
docs/40 - DevDocs/cobalt/daymode/match.md	M	DOCS	-
src/cobalt/aset/web.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/daymode/__init__.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/daymode/match.py	M	static import reach	-
tests/cobalt/test_aset_web.py	M	test/documentation; no resident	-
tests/cobalt/test_daymode.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_card_routes.py	M	test/documentation; no resident	-
tests/cobalt/test_sheet_daymode_probe.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```

## W THE THREE SUITES
`sh /Users/cobalt/cobalt/ops/desk/gate.sh sheet-check-warns all --deploy` on `<tip>` = `011075704` (no `--tickers`: no test of this build writes a ticker row; no `--deselect`, no `--migration`) → exit 0, the verdict lines WHOLE:
```
tests/ops: skipped (no ops paths)
offline 5039/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 6011/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/sheet-check-warns-all-20261029-181717.log
```
No skip is marked `OUTSIDE the allowed set`. From the log (`grep -n`): `:958` offline `5039 passed, 878 skipped, 4 xfailed, 36 warnings in 780.17s (0:13:00)`; `:965` `lock taken: sheet-check-warns`; `:976` `F0: 664 35 272c95bbb12241e3611e4b36326ccf87`; `:1032` `pass 1: whole (deploy)`; `:1204` pass 1 `5767 passed, 9 skipped, 138 deselected, 7 xfailed, 43 warnings in 953.72s (0:15:53)`; `:1290` `F1: 954 47 126f2d6983fa59f9d0eaaff7da7dd29c`; `:2186` pass 2 `244 passed, 1 deselected, 5 warnings in 245.98s (0:04:05)`; `:2260` `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (= F0); `:2316` `lock released`; `:2387` live-note `148 passed, 1 skipped, 15 warnings in 26.58s`. `ls /Users/cobalt/cobalt-wt/sheet-check-warns/.env` → `No such file or directory`. `.env: removed, proven gone (W)`.
The executed pass 1 command (log `:1034`) is the gate's PASS 1 with `--deploy`; it runs `tests/cobalt tests/taxonomy` with the standing `--deselect` list of `ops/desk/gate-lists.md`; none of this build's tests is deselected, so T1 (b) `test_daymode.py::TestDayModeStore::test_a_card_warns_while_the_attested_sheet_disagrees` and T1 (c) `test_aset_web.py::TestMatchCheckAtTheSheet::test_full_sheet_attested_on_a_reduced_day_warns`, `::test_nothing_attested_warns` ran green in pass 1 (`-q`: no per-id line; 0 failed).

DEPLOY PROOF markers, read on this tree (`/Users/cobalt/cobalt-wt/sheet-check-warns/src/…`; the card's paths are the deploy's): `def sheet_warning(` in `match.py` → `1`; `def assert_sheet_matches(` in `match.py` → `0`; `assert_sheet_matches(` in `aset/web.py` → `0` — each the card's "after".

## PRE-STOP SELF-CHECK
(1) RED for its named reason: T1 (a) every `test_daymode.py` test → collection `ImportError: cannot import name 'sheet_warning'` on BASE `src/` (E2); T1 (d) `test_the_hotkey_file_mismatch_warns`, radar `test_nothing_attested_warns` → `assert 409 == 200`, `:83-92` → `KeyError: 'sheet_warning'` (E2). T1 (b), (c) are with-DB and were not run red on BASE (no E2 lock take); the seat edits no `src/`, so no E3 mutation stands in → GAP, `## DECISIONS` 2.
(2) Entry paths: the three callers at tip (Grep `sheet_warning\(` over `src`): `web.py:609` banner — the banner test files unchanged and green (offline 5039/0, pass 1); `web.py:1031` `/size` — T1 (c), green in pass 1; `web.py:1781` radar key — T1 (d), green offline. `match.py` direct — T1 (a), (b). Grade refusal kept: `test_daymode.py::TestGradeRestriction::test_a_plus_is_refused_on_the_reduced_rung` and `test_aset_web.py::TestMatchCheckAtTheSheet::test_a_key_outside_the_rung_is_refused` unchanged, green (offline, pass 1).
(3) Re-read at tip: Grep `assert_sheet_matches` (no match), Grep `sheet_warning\(` (four hits above), the three DEPLOY PROOF greps, `git log --oneline 78a6ab4a..HEAD`, the RESTARTS table at `011075704`, the gate log greps above.
→ `self-check: 2 of 3`.

## FOR THE CHECK
- `78a6ab4a..011075704`: `662c31fc7 wip(sheet-check-warns): red` (pass T: the four test files) · `011075704 feat(sheet-check-warns): rows` (pass S: `match.py`, `daymode/__init__.py`, `aset/web.py`, the two DevDocs pages). Both written by grok-4.7; the seat wrote only `SHADOW-INSTRUCTIONS.md` (untracked) and this report.
- Per row: T1 reds in `## E2 RED`; M1, W1, W2, W3 green in `## E3 THE ROWS` (`122 passed, 40 skipped`) and in W; D1 adds `## 2026-10-29 — sheet-check-warns` to both pages; R1 in `## RESTARTS`. No mutation runs (`## DECISIONS` 2).
- Seat's reading of the diff, for the check to weigh, not findings of the seat: (i) `/size` places `sheet_line` before each post-check banner, including the `Persistence FAILED` one (W1's five returns); (ii) a `ConfigError` from `sheet_for_hotkey_file` (an off-list file) still refuses `/size` through the existing `except (… ConfigError …)` and answers 503 on the key tap, as on BASE; (iii) `match.py`'s DevDocs page keeps its older "The refusals" section above the new dated section.
- Three suites: offline 5039/0 · with-DB 6011/0 (5767 + 244) · live-note 148/0; F0 = F2 = `664 35 272c95bbb12241e3611e4b36326ccf87`, F1 `954 47 126f2d6983fa59f9d0eaaff7da7dd29c`; lock taken `:965`, released `:2316` of the log.
- Card records as re-read at PREFLIGHT: `## PREFLIGHT` last bullet.

## CONTINUE
next: none (stop line written)

## DECISIONS
1. ASK DESK [18:17]: `uv run cobalt jobs restarts 78a6ab4a..HEAD` names the untracked, never-committed harness file `SHADOW-INSTRUCTIONS.md` UNCLASSIFIED (exit 1). Safe default taken: not classified (it is never committed; X9 unsettled), as `cos-outage-1018-build-2026-10-18.md` and `agy-read-1018-build-2026-10-18.md` did; the stop line carries the committed range `78a6ab4a..011075704`: `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar` (= the card's header).
2. T1 (b), (c) red UNPROVEN (L70, as the card's T1 allows): the with-DB tests were not run on BASE (no E2 lock take), and the gate seat edits no `src/`, so no E3 mutation was made for any row. They are green at tip (pass 1, 0 failed). Default: `self-check: 2 of 3`; the check may run the mutation (undo W1's `sheet_warning` in `/size`, expect (c) red).

## RECORDS
- `SHADOW-INSTRUCTIONS.md` at the worktree root is the one untracked file (SHADOW-HUB step 4), never committed.
- Routed card (BAND MID, no `SHADOW OF`): stop line `BUILT ·` (SHADOW-HUB `:28`, `:74`). Builder grok-4.7, two passes (T, S), no S2; builder tokens UNKNOWN (L70); builder wall 9 min (5 + 4).
- One lock take (the gate's, W). No extra take.
- `.env: removed, proven gone (W)`.
- The card's `## RECORDS` as re-read: `## PREFLIGHT`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: sheet-check-warns · tip: 011075704 | on 78a6ab4a | migration: none | offline 5039/0 | with-DB 6011/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 7 of 7 | self-check: 2 of 3 | decisions: 2 · for Dejan: 0 · tokens: 183601
