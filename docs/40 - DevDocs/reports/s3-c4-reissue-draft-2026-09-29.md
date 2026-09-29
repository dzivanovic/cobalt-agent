# S3 C4 RE-ISSUE DRAFT — 2026-09-29

## §0 Headline
- `26` and `27` re-issued whole, in place, on C3 fix r1's code `78e9df82`, from its build report's `## SEAM FOR C4` (copied into `26` byte-identical: 20 of 20 lines, 70 of 70 tokens).
- 09-28 R35 (3) written in: Cobalt fills his keys only while blank, never overwrites. 10 lines changed; each unsettled point takes the narrower write and is under `## ESCALATE`.
- Carried findings: (a) R1 NaN exit stored / −1 correction 500 → FIX → new row `C4-06`; (b) Grok's (iii) → NOT REAL.
- Launch lines differ from 09-28 only by `<base>` (`26`) and `claude-sonnet-5-5` (`27`). New rule strings: 0. ESCALATE 7. Written 09:10 ET (`date`).

## L74
Recorded once (L74): this session's context carries a `Claude-Session: https://claude.ai/code/session_…` commit / PR attribution line and names a file-send tool. No commit was made and no file was sent.

## AUTHORIZATION
`date` → `Tue Sep 29 09:03:26 EDT 2026`. `git -C /Users/cobalt/cobalt log --oneline -3 -- ".../cto-2026-09-29.md"` → `221d484b docs(desk): 09-29 R43–R44 — … 06 C4 re-issue drafter prompt + launch row` first. `| R35 |` → `cto-2026-09-28.md:44`, carries `Approved as recomended` and `O5 / O6 = A`. `| R37 |` → `cto-2026-09-29.md:45`, carries `ready for C4: YES`. `| R44 |` → `cto-2026-09-29.md:52`, names `06-draft-s3-exits-c4-reissue.md`. PASS.

## FACTS
| fact | command | result |
|---|---|---|
| base = C3 fix r1 code | `git -C /Users/cobalt/cobalt log --oneline -4 s3/exits-c3` | `6983de75` docs · `78e9df82 fix(s3-c3): fix r1 — F3's with-DB test and R2 read the sheet's day from the suite clock` · `6114304e fix(s3-c3): fix r1 — …` · `4d3553de wip(s3-c3-fix-r1): red` |
| the code stands | `git -C /Users/cobalt/cobalt log --oneline 78e9df82..s3/exits-c3 -- src tests configs` | EMPTY (exit 0) |
| C1 + C2 + C3 commits below the base | `git -C /Users/cobalt/cobalt log --oneline main..78e9df82` | 24: `78e9df82` · `6114304e` · `4d3553de` · `27d482dc` · `8ec0204f` · `78549817` · `5ecb0898` · `ac5bad7e` · `5e77800f` · `d727a7bc` · `0d591041` · `77cf18fd` · `8c4f116f` · `80e0c8a2` · `bbf25412` · `944f632e` · `9b25eced` · `3ceb3b11` · `da9246f0` · `d9240ae4` · `5164f867` · `eb642f05` · `c57634f8` · `0da7e2e8` |
| main's tip | `git -C /Users/cobalt/cobalt log --oneline -1 main` | `1ca81e99 docs(desk): 09-29 R44 — C4 re-issue drafter db90110f running, tab w2:tD2` |
| migrations | `git -C /Users/cobalt/cobalt show 78e9df82:src/cobalt/db_migrations/` | `0021_legs` last; source: `migration none (0021 rolled back)`; `26` gives C4 none. Agree. `trade_note_path` at `0021_legs.sql:112`; `legs.price CHECK (price > 0)` at `:46` |
| counts | source `## W THE THREE SUITES` | offline `3297 passed, 462 skipped, 1 xfailed` · with-DB pass 1 `3688 passed, 6 skipped, 65 deselected, 1 xfailed` + pass 2 `87 passed` = 3775 · live-note `146 passed, 1 skipped` (`COBALT_TEST_LIVE_DRC`) |
| deselect set | source (c) | fourteen `--deselect` arguments (65 deselected); pass 2 = its (c3) ids; forward creates `legs` and `voice_turns` |
| anchors | source `## SEAM FOR C4`; spot-read `git show 78e9df82:src/cobalt/aset/web.py` / `radar_panel.py` / `cards/legs.py` | every anchor true at the tip (`_card_tap :1512`, `mark_filled :1564`, `record_exit :1620`, `record_correction :1676`, `_tap_reply :1500`, `_sheet_closed_estimated :1745`, `render_stop_block :1232`, `read_in_trade :802`, `LegView :336`, `read_position legs.py:713`). Outside the source: `/size`'s `upsert_trade_note` `web.py:1042`; `_tap_price` `web.py:1465` |
| RESTARTS | source `## RESTARTS` | `uv run cobalt jobs restarts 27d482dc..78e9df82` → `RESTARTS: com.cobalt.aset com.cobalt.radar`; no `UNCLASSIFIED` |
| C3 fix r1 check | last line of `reports/s3-exits-c3-fix-r1-check-2026-09-29.md` | `… houses that checked: 2 of 3 · defects that HOLD: 0 · ready for C4: YES · ESCALATE: 8` |

## Classification
| # | finding | source line | class | reason |
|---|---|---|---|---|
| (a) | R1: `/exit` `price=NaN` → 200, a leg stored with price `NaN`; `/correct` `price=-1` → 500, nothing written | build `## ESCALATE` 1–2 (`s3-exits-c3-fix-r1-build-2026-09-29.md:242-243`), R1 output `:83`, `:89`, `:91`; check `## Checked against the branch` rows `:98-99` (HOLDS), `## ESCALATE` 2–3 | FIX → `C4-06` | Both ran and were read (not L70): `_tap_price` (`web.py:1465-1472`) accepts `Decimal('NaN')`, which passes `CHECK (price > 0)`; −1 fails that CHECK uncaught → 500, a refusal that never reaches the page (L1). C4 writes these prices into his note (C4-3 units, R35 exit keys). |
| (b) | Grok (iii): any leg absent from the URL card's current legs, a superseded leg of the same card included, gets the route's sentence, not C2's `not_current` text | check `## ESCALATE` 1, `## Checked against the branch` row `:92` (HOLDS as a fact) | NOT REAL | The fact holds, but it is the refusal `03` row F2 specifies (`03:25`); it is loud, 422, nothing written (L1). The drafter and builder recorded it; no rule is broken. |
Totals: FIX 1 · NOT REAL 1 · UNPROVEN 0 · OUT OF SCOPE 0 · OWNER ITEM 0.

## CHANGES
| file | line | what | why |
|---|---|---|---|
| `26` | 1 | RE-ISSUED header after the `MODEL:` tag | item 9 |
| `26` | 4 | worktree command `<base>` → `78e9df82` | item 8 |
| `26` | 14–18 | LAUNCH-TIME VALUES → BUILT VALUES: `<base>` = `<c3 tip>` = `78e9df82` with their proofs, the 24 commits, the migrations, EXPECTED counts, the base RESTARTS | item 1, 6 |
| `26` | 22 | new O5 / O6 line: RULED, his words quoted, the keys and their one source each, BLANK, times format, a filled value then his | R35 (3) |
| `26` | 23 | O5 / O6 removed from the unruled owner defaults | R35 (3) |
| `26` | 27 | seams sourced from C3 fix r1's report (path of record) | item 2 |
| `26` | 29–49 | new `### SEAM FOR C4`, the source's section whole | item 2 |
| `26` | 54 | C4-1: "his seven keys created blank, never written" → filled only while blank, never overwritten. The "seven" also disagreed with the six v3 §7 names | R35 (3) |
| `26` | 55 | C4-2: fill routes anchored (`web.py:1067` / `:1131`; `:1556` / `:1567`) | item 2 |
| `26` | 56 | C4-3: note seams anchored (`:1624`, `:1649`, `:1680`); a CLOSED commit fills his blank exit keys | item 2; R35 (3) |
| `26` | 58 | C4-5: DevDocs name C4-06 | item 4 |
| `26` | 59 | new row `C4-06 — carried from C3 fix r1 (R37)` | item 4 |
| `26` | 61 | NOT IN C4: "filling his keys (O5 / O6)" removed; `profit_loss` / `RVOL` and C3's block beyond C4-06 added | R35 (3); item 4 |
| `26` | 64 | L28 card line adds clause 2a | R35 (3) |
| `26` | 65 | INDEX CARD (3) / (4): C3 fix r1's seam; `web.py:1042`, `_tap_price :1465` | items 1, 2 |
| `26` | 69–70 | AUTHORIZATION: R35 and R37 greps added; C3's last check report named; `R__` untouched | item 7 |
| `26` | 75 | W on this base: the source's 14-argument pass 1, its pass 2 ids, `voice_turns` created (was `48`'s eight `--deselect`, `legs` only) | item 1 |
| `26` | 83 | E0 EXPECTED counts | item 1 |
| `26` | 93 | E2: R35 (3) reds (entry_time, trade_def, exit keys, absent key, earlier fill untouched) and C4-06's two reds | R35 (3); item 4 |
| `26` | 95 | E3 names C4-06 | item 4 |
| `26` | 98 | CLOSE ESCALATE names R35 (3)'s defaults as built | R35 (3) |
| `27` | 1 | header; `MODEL:` → Sonnet 5.5 (`claude-sonnet-5-5`, R118); launch `--model claude-sonnet-5` → `claude-sonnet-5-5` | items 5, 9 |
| `27` | 5–6 | `<base>` → `78e9df82`; `<tip>` / `<report>` stay FILL AT LAUNCH | item 1 |
| `27` | 11 | R35 / R37 greps; Grok's copies add C3 fix r1's build report; §3 (iv) → his keys behind the blank test; new (iv-b) `_tap_price` one; `R__` untouched | items 2, 4, 7; R35 (3) |
| `27` | 15 | THE CHUNK: his keys filled only while blank, his ruling quoted; C4-06 named | R35 (3); item 4 |
| `27` | 20 | Q(4) re-written to R35 (3) | R35 (3) |
| `27` | 28 | new Q(12) for C4-06 | item 4 |
Seats: `27` already seats Opus 5.5 (Fable seat) · Astra · Grok, which is L67's `CHECKER SEATS BY KIND OF WORK` for a NEW build. No change. Carried unchanged: rows C4-4, E1, the stop lines, `26`'s RULE STRINGS text. R35 (3) lines: `26` 22, 54, 56, 61, 64, 93, 98; `27` 11, 15, 20 = 10.
Sizes (`wc -c`): `26` 16,768 → 27,656; `27` 8,337 → 10,256. The growth is the seam block copied whole (item 2), R35 (3), C4-06 and the built values. `R__` count: 1 in each, both in the AUTHORIZATION block (`26:71`, `27:11`).

## SEAM PROOF
Seam block: `diff` of source lines 190–209 against `26` lines 30–49 → IDENTICAL (20 of 20 lines). One `grep -q -F` per token in `26`, one shell loop (`date` 09:09), each exit 0: `src/cobalt/aset/web.py:1512` · `_card_tap` · `radar_card_fill` · `web.py:1556` · `AsetStore().mark_filled` · `:1564` · `web.py:1567` · `radar_card_exit` · `web.py:1593` · `legs.record_exit` · `:1620` · `web.py:1624` · `radar_card_held` · `web.py:1640` · `legs.record_held` · `web.py:1649` · `radar_card_correct` · `web.py:1658` · `legs.record_correction` · `:1676` · `web.py:1680` · `web.py:1670-1674` · `legs.read_position(card_id)` · `_TapInputRefused` · `web.py:1067` · `store.mark_filled` · `:1123` · `:1131` · `:1152` · `save_fill_update` · `_sheet_closed_estimated` · `web.py:1745` · `_open_cards_section` · `:746` · `_sheet_in_trade` · `web.py:1720` · `:755` · `_tap_reply` · `web.py:1500` · `FILLED — trade note NOT written` · `leg saved, note unit NOT written` · `_terminal_legs` · `radar_panel.py:1363` · `:1378` · `:1430` · `web.py:1736` · `render_stop_block` · `radar_panel.py:1232` · `web.py:1537` · `:1582` · `:1689` · `:1702` · `radar_panel.py:1437` · `test_the_notes_line_keeps_its_text` · `radar_cards_v` · `0007_radar_cards.sql:233` · `test_x_m_` · `aset/migrations/0001_aset_sizings.sql:20` · `radar/evaluate.py:1051` · `last_price_at: null` · `price_asof = NULL` · `cto-2026-09-29.md` R10 · `legs_current_v` · `cards/legs.py:713` · `radar_panel.read_in_trade` · `radar_panel.py:802` · `LegView` · `:336` · `ExitResult(…)` · `CorrectionResult(…)`. Result: `tokens 70 of 70`, no `MISS`.

## RULE PROOF
- `26` launch line (`claude --bg …` to the last `--add-dir`) vs `git -C /Users/cobalt/cobalt show HEAD:<path>`: identical (Python compare `True`). Worktree command: equal after `<base>` → `78e9df82` (`True`).
- `27` launch line vs HEAD: differs only by `claude-sonnet-5` → `claude-sonnet-5-5` (compare `True` after that one swap).

NEW strings: none.

## ESCALATE
1. ASK DESK (R35 (3), BLANK): reading A, taken as the narrower write: blank = the key is present with an empty value; an absent key is never added. Reading B: an absent key counts as blank and is added. [09:10 ET, from date]
2. ASK DESK (R35 (3), `exit_price`): reading A, taken as the narrower write: filled only when the card CLOSED through exactly ONE current exit leg that is `confirmed`. Reading B: the share-weighted price of all current exit legs, estimated legs included. A filled value is never refreshed, so an estimated price would stay. [09:10 ET]
3. ASK DESK (R35 (3), `profit_loss`): the unit is unruled. Reading A, taken as the narrower write: left blank. Reading B: dollars, Σ shares × (exit − entry) by direction. Reading C: realized R (C2's `RealizedR`). [09:10 ET]
4. ASK DESK (R35 (3), times): taken: `entry_time` / `exit_time` in ET in the `date` key's format `%Y-%m-%d %H:%M`. Reading B: the shape his existing notes use (e.g. `HH:MM`). [09:10 ET]
5. ASK DESK (R35 (3), Cobalt's own fill): reading A, taken as the narrower write: a key Cobalt filled is then his and is never rewritten, even after a leg correction. Reading B: Cobalt refreshes its own earlier value while he has not edited it (unit-style human-wins). [09:10 ET]
6. ASK DESK (C4-06's path): `_tap_price` (`web.py:1465`) is a C3 helper. `26`'s rows edited route bodies only, so this is a FIX on a path `26` did not touch. Option 1, taken as the safe default: a row in `26` (`C4-06`). Option 2: a C3 fix r2. Its one guard in the one parser (L3) also covers a negative `/exit` and `/fill` price. R1 left those unproven (the −1 exit hit `stale`). The reds cover only the two proven cases. [09:10 ET]
7. L74: recorded once under `## L74`.

## CONTINUE
next: none. The desk verifies (L35) and commits `26`, `27` and this report. It writes `26`'s launch row (`R__` filled, `78e9df82`, `no with-DB run in flight`, his R35 (1) approval word for the two `.env` strings) and launches it only while `ls -la /Users/cobalt/cobalt-wt/*/.env` has no match and no with-DB run is in flight (L76).

S3 C4 REISSUED · files: 2 · base: 78e9df82 · seam lines carried: 20 of 20 · R35 (3) lines: 10 · classified: 2 (FIX 1 · NOT REAL 1 · UNPROVEN 0 · OUT OF SCOPE 0 · OWNER ITEM 0) · rows added: 1 · new rule strings: 0 · ESCALATE: 7
