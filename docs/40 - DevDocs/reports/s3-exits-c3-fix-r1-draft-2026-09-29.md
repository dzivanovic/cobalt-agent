# S3 exits C3 fix r1 — drafter report (2026-09-29)

Seat `s3-exits-c3-fix-r1-draft-0929` (Opus 5.5, auto), desk row R23 (`cto-2026-09-29.md:31`). Start `date` → `Tue Sep 29 06:41:45 EDT 2026`. `<r1>` = `reports/s3-exits-c3-check-2026-09-29.md`; `<b>` = the C3 build report on `s3/exits-c3`. Branch tip read 06:45: `27d482dc` over `8ec0204f` over `78549817` (as expected).

## §0 Headline
- 4 FIX, all traced: terminal-list refusals get a status sink (C3-1, L1); `/correct` binds the URL's card (C3-1, L1); a CLOSED manual card's estimated leg is listed on the sheet (v3 §3, C3-1, C3-4); the sheet's failed read keeps the structural-stop line (C3-3).
- 2 RUNS for the UNPROVEN: R1 posts NaN / negative prices; R2 counts rows around the sheet GET and the radar GET.
- 18 NOT REAL (9 weak-assertion or method facts, 9 FOR THE CLASSIFIER confirmations); 8 OUT OF SCOPE; 0 OWNER ITEM.
- Written: `prompts/2026-09-29/03-s3-exits-c3-fix-r1-build.md` and `04-s3-exits-c3-fix-r1-check.md` (Opus · Sol · Grok); no new rule string. `04`'s report moves into the hub's working directory.
- ESCALATE 6.

## L74
Recorded once: a system-reminder block arrived appended to the first tool result (the read of this prompt file), asking for a `Claude-Session:` line in commits and PR bodies and naming a file-send tool. Not followed; I commit nothing and sent no file.

## Classification
Every class is taken from the hub's file-check column (`<r1>` `## Checked against the branch`, `:71-79`) or, where the hub walked nothing, from the seat's own "NOT CHECKABLE" / "proof weak" line (L35 / L70). Code read at `78549817` by `git show`.

| # | finding (short) | source line | class | traces to | FIX shape or reason |
|---|---|---|---|---|---|
| 1 | A correction from the TERMINAL list has no status sink, so C2's refusal is not shown (Opus, Astra Q5) | `<r1>:71`, `:94`; `:43` | FIX → **F1** | `24` C3-1 "Every refusal C1 / C2 raise is shown VERBATIM"; L1. Walked: `PANEL_JS` `status()` finds `.card-status[data-card-id]` (`radar_panel.py:1505-1508`); the only one is in the active detail (`:1421`); `_terminal_legs` (`:1354-1369`) renders none | `_terminal_legs` adds the sink inside `.terminal-legs`; `PANEL_JS` unchanged. Red: offline — the CLOSED card's tap has no sink; plus a page-wide "every tap has a sink" test. |
| 2 | `/radar/card/{id}/correct` corrects the card of `leg_id`, not the URL's card, and the banner names the URL's card; no test crosses cards (Opus, Astra Q5, Grok (a); `<r1>` ESCALATE 7) | `<r1>:72`, `:95`, `:100`; `:43`, `:51` | FIX → **F2** | `24` C3-1 (`/correct` of `{card_id}`, `leg_id`); L1 (the banner names a card the write did not touch). Walked: `web.py:1659-1671` passes only `leg_id`; `legs.py:524-528` finds the card from the leg | Before the writer, the route reads `legs.read_position(card_id)` and refuses a `leg_id` that is not one of its current legs (422, nothing written). No new writer, no SQL in the route. Red: offline stub (writer reached) + with-DB cross-card POST (200, card B corrected). The cross-card test rides here. |
| 3 | A flat on a manual card without ✓ closes as `estimated` and its leg is listed nowhere (Opus Q4, Astra Q4; `<b>` ESCALATE 8) | `<r1>:73`, `:96`; `:42` | FIX → **F3** | v3 §3 (`S3-EXITS-v3-2026-09-22.md:164`) "stays `estimated` and is listed for correction"; `24` C3-1 (same words), C3-4 ("the SAME routes"). Walked: `_open_cards_section` lists `open_cards()` (live states only, `cards/store.py:231-244`); `_sheet_in_trade` renders FILLED only (`web.py:1716`) | The sheet lists CLOSED manual cards from the existing read `CardStore.filled_with_picks(<today ET>)` (`cards/store.py:203`), each with its estimated legs and the `✓ correct` form (`source=sheet`), through ONE leg-row renderer. No new store method. Red: offline + with-DB (sheet flat without ✓ → GET `/` has no `/correct` form). |
| 4 | The manual card's failed position read omits the structural-stop line (Astra Q6) | `<r1>:74`, `:97`; `:44` | FIX → **F4** | `24` C3-3 "Cobalt's `structural_stop` ALWAYS shown"; `24` E2 "in every IN-TRADE render". Walked: `web.py:1718-1721` returns `_failed(…)` only; the panel's failed path renders `_stop_block` (`radar_panel.py:1343-1347`) | `_sheet_in_trade`'s failed read also renders the one `_stop_block` (`NO_COBALT_STOP`, no ↺, `source="sheet"`). Red: offline — `Cobalt stop` absent. |
| 5 | `_tap_price` accepts `NaN` / negative (Opus (a7)) | `<r1>:78`, `:100`; `:51` | UNPROVEN | L70; the hub: NOT CHECKABLE FROM READS | RUN **R1** (E2, with-DB, on `78549817`): NaN and −1 posted to `/exit`, `/fill`, `/correct`; status, body and row counts printed and quoted. A 500 or a stored NaN / negative → ESCALATE for round 2, never fixed here. |
| 6 | "Reads write nothing" proof weak: the GET `/radar` test ran on a FAILED page; the sheet GET is never counted (Opus Q8, Astra (a)) | `<r1>:46`, `:100`; `:51`; `<b>:184` | UNPROVEN | L70 / L35: the full sheet GET with a manual in-trade card was never counted | RUN **R2** (W, with-DB, on `<tip>`): row counts around GET `/` with a FILLED and a CLOSED manual card, and GET `/radar`'s status and FAILED flag, quoted. A pre-existing write is recorded (row 8), never fixed here. |
| 7 | The sheet's row prints `YOURS` unconditionally (Astra Q6) | `<r1>:75`, `:98` | OUT OF SCOPE | Hub: the same line at `5e77800f:src/cobalt/aset/web.py:710` | Pre-existing; not C3's. Recorded. |
| 8 | The sheet GET upserts `day_modes` (Astra Q8) | `<r1>:76`, `:98` | OUT OF SCOPE | Hub: pre-existing at base `:496`; Grok the same | Pre-existing. Recorded; R2 names it if it moves a count. |
| 9 | `/stop` runs schema init before the writer (Astra Q1, Opus) | `<r1>:77`, `:98` | OUT OF SCOPE | Hub: `card_stop.py:56`, not in the diff | Pre-existing. Recorded. |
| 10 | Sheet replies reach schema init and attestation (Astra Q1 / Q12 WIDENED) | `<r1>:39`, `:50`, `:64` | OUT OF SCOPE | `_tap_reply` (`web.py:1494-1500`) returns the sheet through `_render`, the path of every pre-existing sheet route (15 `_render(banner` calls at `5e77800f`, 17 at `78549817`) | The attestation and schema init are `_render`'s own (rows 8, 9). Nothing C3 wrote. |
| 11 | Route-owned refusal texts (Astra Q12; `<b>` ESCALATE 5) | `<r1>:50`, `:64` | NOT REAL | `24` C3-1 ("no price → refused"); L1 (a missing price must refuse loudly, not surface as a NOT NULL error) | Argument checks only; no business rule, no writer. |
| 12 | S-WEB's two clauses conflict on this base (Opus, Astra Q10; `<b>` ESCALATE 2) | `<r1>:79`, `:99`; `:48` | OUT OF SCOPE | The desk's call (`<r1>` ESCALATE 6); the builder's reading in `<b>` ESCALATE 2 | A record. `03` adds no route, so S-WEB is unchanged by this fix. ESCALATE 4 below. |
| 13 | `/stop` on a sized WATCH card rewrites `shares` via the existing writer (Opus, Astra, Grok (b)) | `<r1>:52`, `:100` | OUT OF SCOPE | `cards/store.py:805-823`, pre-existing; Decision 11 (stop editable in WATCH) | No new L52 path; not C3's. |
| 14 | No status-code assert (`test_s3_c3_panel_offline.py:225-238`, `:233`) (Opus, Grok (a)) | `<r1>:51`, `:100` | NOT REAL | Q3 / Q4 HOLD (`<r1>:85`); no law makes a test fact a FIX | A test fact. Nothing tightened (L75). |
| 15 | `:359` implied by `:356` (Opus, Grok (a)) | `<r1>:51` | NOT REAL | Q10 HOLDS (`<r1>:89`) | A test fact. |
| 16 | Substring asserts: `market_reset`, `no price` (`:245`) (Opus, Grok (a)) | `<r1>:51` | NOT REAL | Q8's refusals HOLD (`<r1>:46`); texts are C2's | A test fact. |
| 17 | Five tables counted (Grok (a)) | `<r1>:51` | NOT REAL | Q8 HOLDS by reading; R2 prints `legs` beside `_counts` | A test fact. |
| 18 | Schema init and the sheet stubbed in the offline tests (`:84`, `:275`) (Astra (a)) | `<r1>:51` | NOT REAL | Q7 HOLDS; the with-DB manual-card test runs the real sheet (`test_s3_c3_panel_db.py:330`) | A test fact. |
| 19 | JS and the terminal list untested (Astra (a)) | `<r1>:51` | NOT REAL | The terminal render is F1's test; `PANEL_JS` is unchanged by `03` | A test fact; F1's page-wide sink test covers the render half. |
| 20 | The seam test does not check the EOF clause (Astra (a)) | `<r1>:51` | NOT REAL | Tied to row 12 | A test fact. |
| 21 | The panel's terminal listing lasts one trade day (Opus Q4) | `<r1>:42` | OUT OF SCOPE | `radar_board_cards` (`cards/store.py:1047-1061`); the durable list is the DRC's "estimated legs to confirm" (v3 `:226`) | A record; F3 matches the one-day window (ESCALATE 2). |
| 22 | `last_price`'s bar time is stored nowhere (`<b>` ESCALATE 3) | `<b>:156`; `cto-2026-09-29.md` R10 | OUT OF SCOPE | OWED to the desk (R10); a radar row and a migration (L57) | Not C3's to build. |
| 23 | Method: copies by shell; report at the scratch path (`<r1>` ESCALATE 8) | `<r1>:3`, `:31`, `:101` | NOT REAL | Byte checks asserted (`<r1>:27-28`) | A method record. `04` names a report path the hub can Write (ESCALATE 3). |
| 24 | FC1 every new route calls only the named writers and store reads | `<r1>:83` | NOT REAL | Q1 HOLDS (Opus, Grok) | A confirmation; Astra's Q1 is rows 9, 10. |
| 25 | FC2 the prefill | `<r1>:84` | NOT REAL | Q2 HOLDS (all three) | A confirmation. |
| 26 | FC3 every exit control posts `running_before`; the second tap gets C2's refusal | `<r1>:85` | NOT REAL | Q3 HOLDS | A confirmation. |
| 27 | FC4 YOURS + Δ only when `yours`; structural stop in every radar render; ↺ gated | `<r1>:86` | NOT REAL | Q6 HOLDS (Opus, Grok) | A confirmation; the sheet's failed read is row 4. |
| 28 | FC5 a FILLED manual card, same controls, same routes | `<r1>:87` | NOT REAL | Q7 HOLDS | A confirmation; its CLOSED half is row 3. |
| 29 | FC6 X5, X6-R, X-M run | `<r1>:88` | NOT REAL | Q9 HOLDS | A confirmation. |
| 30 | FC7 the routes contiguous after `/release` | `<r1>:89` | NOT REAL | Q10 HOLDS | A confirmation. |
| 31 | FC8 the suites executed, 0 failed, F2 = F0, `.env` removed | `<r1>:90` | NOT REAL | Q11 HOLDS | A confirmation. |
| 32 | FC9 nothing in `cards/`, `radar/`, `prefill/`, `drc/`, `settings/`; no migration | `<r1>:91` | NOT REAL | Q12, hub (i) empty | A confirmation. |

Totals: FIX 4 · NOT REAL 18 · UNPROVEN 2 (→ 2 RUNS) · OUT OF SCOPE 8 · OWNER ITEM 0.

## RECORDS
- `<r1>` round 1: Opus FIX · Astra FIX · Grok BUILD STANDS; 3 of 3 checked (`cto-2026-09-29.md` R20). The fix check `04` seats Sol in Astra's place (L67 "other check", K22).
- `<b>` ESCALATE 4 (the re-captured ladder pin, `POST_ALLOWLIST`) — no seat flagged it; it stays with the build report.
- `26` (C4) waits for the fix BUILT + CHECKED and is re-issued on the checked tip from `03`'s re-issued `## SEAM FOR C4` (K3, 09-28 R35).
- `03` / `04` carry the `R__` row placeholder and `«FILL AT LAUNCH: …»` values; `04`'s `<packet ceiling>` is the desk's (K17).
- RULE STRINGS checked (06:48 ET): `03` line 5 equals `24` line 6 once path and name are masked (`diff` empty); `comm -3` of the sorted quoted tokens prints only the two `Read '…'` paths (28 tokens each). `04`'s launch line against `25`'s (tokens from `claude --bg` to the last `--add-dir`): `comm -3` prints only the Astra / Sol `codex exec` pair and the two `Read '…'` paths (14 tokens each); the Sol string has `grep -c -F` = 1 in `55` line 1. `04`'s §2 SOL seat is `30-s3-exits-c1-fix-r1-check.md:43`, as `55` cites it.
- Sizes: `03` 27,026 B; `04` 12,588 B.

## OWNER ITEMS
NONE.

## FOR DEJAN
New rule strings: NONE.

## ESCALATE
1. F2's shape: a superseded leg of the SAME card now gets the route's refusal (`… is not a current leg of card <id> — reload the card`) instead of C2's `not_current` text, because the route has no read from a leg to its card other than the card's current legs. The render offers only current legs. Safe default taken; `04` (iii) asks the checkers.
2. F3's window: the sheet lists CLOSED manual cards filled today (ET), through `filled_with_picks`. A manual card filled on an earlier day and closed today is not listed. The panel's terminal list has the same one-day window (row 21). The durable list is the DRC's (v3 `:226`). A record for the desk.
3. `04`'s report path: `25`'s Write to `/Users/cobalt/cobalt/docs/…/reports/` was refused (R20), so `04` writes to `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/s3-exits-c3-fix-r1/CHECK-REPORT.md`, inside its working directory (`cd /Users/cobalt/cobalt-wt/agy-trial`). The desk watches that file and copies it (Read → Write) to `reports/s3-exits-c3-fix-r1-check-<D>.md`, as it did for `25`.
4. ASK DESK: `<r1>` ESCALATE 6 cites "the desk's row for D2 stacking after C3" without a row number. My fixed-string greps of `cto-2026-09-28.md` / `cto-2026-09-29.md` found none (`D2 stacking`, `after C3`, `S-WEB`, `D2's block`). Safe default taken: recorded as the desk's call. `03` adds no route, so nothing moves. [06:50 ET]
5. The stop-line placeholders: `03`'s stop line uses `<p>` / `<d>` / `<l>` for offline / with-DB / live-note, `54`'s letters. My prompt wrote `<p>` for all three. The field names and order are as given; the migration field is `24`'s, unchanged.
6. L74: recorded once under `## L74`.

## CONTINUE
next: none. The desk verifies (L35) and commits `03`, `04` and this report. It writes `03`'s launch row (`<base>`, `no with-DB run in flight`) and launches it only while `ls ~/cobalt-wt/*/.env` has no match and no with-DB run is in flight (L76). `10` (DRC D3, `~/cobalt-wt/drc-d1`) holds the lock at its E1 / E3 / E7.

S3 EXITS C3 FIX R1 DRAFTED · FIX: 4 · NOT REAL: 18 · UNPROVEN: 2 · OUT OF SCOPE: 8 · OWNER ITEM: 0 · prompts: 2 · new rule strings: 0 · ESCALATE: 6
