## §0 Headline
S3 C3 house check, round 1: 3 of 3 seats checked (Opus, Astra: FIX · Grok: BUILD STANDS). 4 file-verified defects HOLD (terminal correction refusal has no sink; `/correct` never binds leg to card; CLOSED manual card's estimated leg is never listed; manual failed-read render omits the structural-stop line). `ready for C4: NO`. ESCALATE: 8.
The `reports/` Write was refused (background-isolation guard); this is the same report at `scratch/tribunal-bars-0920/s3-exits-c3/CHECK-REPORT.md`. No `/reports/` copy exists.
Desk note (09-29 06:2x): copied to this path by the CTO desk `b50d5fd5` from the hub's scratch file `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/s3-exits-c3/CHECK-REPORT.md` (Read → Write); the hub's text below is unchanged.

## L74
No L74 line arrived.

## PREFLIGHT
| step | result |
|---|---|
| `date` | Tue Sep 29 05:46:07 EDT 2026 |
| placeholder gates (`R_` + `_`, `FILL AT LAUNCH`) | both nothing |
| R17 / R19 rows, `git log -S"All 4 house models approved"` | both carry the strings; `5055151dbf68899b82de5b11f99733ed2d03048c` |
| R95 (cto-09-23), R109 (cto-09-22 "Make all Opus") | one row each, present |
| R175 (cto-09-28) | present: C2 fix r1 CHECKED, `24` stacks on `5e77800f` |
| launch row R11 (cto-09-29 :19) | names `25-s3-exits-c3-check.md`, carries `<build stop>` and `no other house hub is running`; `git log -S` → `b1ade60e4d9668093b98d8709321a517f846b496` |
| `grok --version` | `grok 1.0.25 (f7e67d6988e2) [stable]` |
| `tail -n 3 <report>` | last non-blank line = `<build stop>`, starts `S3 EXITS C3 BUILT ` |
| `git log --oneline 5e77800f..78549817` | `78549817 feat(s3): C3 — the panel…` · `5ecb0898 wip(s3-c3): red` · `ac5bad7e wip(s3-c3): E1 experiments` (3 commits) |
| `git log --stat` path union | `docs/40 - DevDocs/cobalt/aset/{radar_panel,web}.md`, `src/cobalt/aset/{radar_panel,web}.py`, `tests/cobalt/{test_radar_panel_cards,test_s3_c3_panel_db,test_s3_c3_panel_offline,test_s3_c3_experiments}.py` |
| `ls …/s3-exits-c3/.env` | No such file or directory |
| `ls scratch/tribunal-bars-0920/s3-exits-c3` | absent (fresh) |
| probes | OPUS `OK` (UP) · ASTRA `OK` (UP); Grok not probed (per file) |

## Files copied
Diff: 4 parts (`diff.part1..4.md`), each headed per the file; `grep -c "^commit "` over the parts = 1+0+1+1 = 3 = PREFLIGHT's 3 commits. Part bytes 25785 / 31797 / 18793 / 30415 = 106390 (diff) + 400 (four header lines).
`files/` copies byte-identical (concatenated parts asserted equal to the original in the copy step): report 45611 (2 parts) · `20` 31610 · `22` 19994 · `24` 28101 · C2 fix r1 report 37477 · v3 78960 (3) · LAWS.md 61011 (2) · `radar_panel.py` 79157 (3) · `web.py` 80851 (3) · `test_radar_panel_cards.py` 38337 (2) · `test_s3_c3_panel_db.py` 18580 · `test_s3_c3_panel_offline.py` 25135 · `test_s3_c3_experiments.py` 4758. `rulings.md` = the two grep outputs. `CHECK-INSTRUCTIONS.md` = the QUESTIONS verbatim + a Files paragraph.

## CONTINUE
Done. Method note (ESCALATE 2): the copies and diff parts were cut by shell (`head` / `tail` / a splitter) into the existing scratch folder, not by Read → Write; the byte check is the assert above.

## Clock
Seats launched 05:48 ET. Opus complete by 05:52:25. Astra complete by 05:55:38. Grok complete by 06:07:56 (its first write seen 05:55). All inside 45 minutes; no TIMEOUT, METER or HARNESS. Written-nothing proof: `ls -la S` before the launch showed only the copies; after, only `grok-check.md` (Grok's own file) plus the two files I wrote from stdout.

## Per question (cells ≤30 words, seat's words)
| Q | opus | astra | grok |
|---|---|---|---|
| 1 | HOLDS — only the named writers plus reads; no SQL (`web.py:1530-1704`) | DOES NOT HOLD — `/stop` and sheet replies reach schema init and attestation persistence (`web.py:1682`, `card_stop.py:57`, `web.py:496`) | HOLDS — `transition`, `mark_filled`, `record_exit/held/correction`, `record_stop_edit` only (`web.py:1539-1701`) |
| 2 | HOLDS — `card.last`, NULL empty, never `entry` (`radar_panel.py:1188`); bar time null (X6-R) | HOLDS — prefill `last_price`; bar time null, disclosed (`web.py:1479`) | HOLDS — `last_poll`/`estimated` vs `typed`/`confirmed` (`web.py:1479`); no-price refused `store.py:252` |
| 3 | HOLDS — `running_before` posted; second ½ gets C2's text (`legs.py:423-425`) | HOLDS — `radar_panel.py:1304`, `legs.py:423` | HOLDS — `radar_panel.py:1298-1310`, `legs.py:424` |
| 4 | HOLDS with a listing gap — CLOSED manual card's estimated leg never listed; radar listing lasts one day | DOES NOT HOLD for manual cards — flat without ✓ closes, disappears from the sheet (`web.py:744`, `:1716`) | HOLDS — untouched flat `estimated`; ✓ `confirmed`, closed in `record_exit`'s transaction (`web.py:1609`, `legs.py:438`) |
| 5 | DOES NOT HOLD — terminal ✓ correct has no status sink (`radar_panel.py:1368`, `:1505`); `/correct` never checks leg∈card (`web.py:1659`) | DOES NOT HOLD — same two defects (`radar_panel.py:1354`, `:1505`; `web.py:1659`) | HOLDS — writers reached, refusals unrewritten (`web.py:1643`, `:1663`, `:1524`) |
| 6 | HOLDS — `YOURS`/Δ only if `owner == "yours"` (`radar_panel.py:1239`); structural stop always; ↺ gated | DOES NOT HOLD — sheet's old row prints `YOURS` unconditionally (`web.py:710`); manual failed-read shows no structural stop (`web.py:1721`) | HOLDS — `radar_panel.py:1239-1268`, `:1396`, `store.py:753` |
| 7 | HOLDS — `_sheet_in_trade` same routes (`web.py:1707-1725`) | HOLDS for FILLED manual cards (`web.py:1722`); see Q4 | HOLDS — `web.py:1716`, `:1722` |
| 8 | HOLDS by reading; proof weak (radar GET rendered FAILED page; sheet GET not counted) | DOES NOT HOLD — sheet GET can upsert `day_modes` (`web.py:496`, `daymode/store.py:153`) | HOLDS — position read rolled back (`legs.py:713`); `day_modes` upsert pre-existing (`web.py:496`) |
| 9 | HOLDS — X5 EXPIRED; X6-R none; X-M → sheet | HOLDS (X5 exercises session-close fallback) | HOLDS — report :60-62; `expire.py` not in diff |
| 10 | HOLDS, but the two S-WEB clauses conflict on this base (ESCALATE 2 of the build) | DOES NOT HOLD literally — same conflict; also `_open_cards_section` changed | HOLDS — block after `/release` `:1433`→`:1530`; also file end |
| 11 | HOLDS from the report | HOLDS as reported evidence | HOLDS — 3292/0 · 3679/0 + 83/0 · 146/0 · F2=F0 |
| 12 | NOTHING WIDENED | WIDENED — sheet replies reach schema init / attestation; route-owned refusal texts | NOTHING WIDENED |
| (a) | GET `/radar` test ran on a FAILED page; JS string-matched only; no cross-card `/correct` test; status codes unchecked (`test_s3_c3_panel_offline.py:225-238`); `:359` implied by `:356`; substring `market_reset` asserts; `_tap_price` accepts `NaN`/negative (plausible) | schema init/sheet stubbed in tests (`test_s3_c3_panel_offline.py:84`, `:275`); GET coverage omits sheet; JS/terminal untested; seam test not the EOF clause | `no price` substring (`:245`); `:233` no status; `:359` implied; five tables counted; no cross-card `leg_id` test |
| (b) | `/fill`→`mark_filled` recompute; `/stop` on a sized WATCH card rewrites `shares` (`cards/store.py:805-823`), pre-existing writer | A size path exists: fill/entry correction cache (`legs.py:474`, `store.py:372`); WATCH `/stop` (`cards/store.py:814`) | No new score path; `/fill`, `/stop`→`recompute_for_stop` existing (`cards/store.py:782`, `:812`) |
Final lines — opus: `CHECK S3 C3: FIX (5) TERMINAL-LIST REFUSAL SINK, (5) /correct LEG-CARD BINDING, (a7) _tap_price NaN/negative · ready for C4: NO · terminal corrections drop refusals; /correct writes another card's leg` · astra: `CHECK S3 C3: FIX Q1/Q4/Q5/Q6/Q8; resolve Q10/Q12 · ready for C4: NO · Unintended writes and inaccessible corrections leave this build unready today.` · grok: `CHECK S3 C3: BUILD STANDS · ready for C4: YES`.

## Suites (from the builder's report, facts)
- offline: `3292 passed, 458 skipped, 1 xfailed, 20 warnings in 549.08s`, exit 0, 0 failed, 0 errors (:91).
- with-DB, first W: pass 1 `1 failed, 3678 passed` (a stray card the builder left on `cobalt_dev`; desk removed it, cto-09-29 R1/R2); resumed W: pass 1 at `0013` `3679 passed, 6 skipped, 65 deselected, 1 xfailed` (:178); pass 2 at `0021` `83 passed` (:184); total 3762/0.
- deselected: the report's (c) command names them (`test_tenancy.py::TestMigrationRoundTrip`, `::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default`, `test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches`, …); 65 in count.
- F0 = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`; F1 = `773 · 38 · 126f2d6983fa59f9d0eaaff7da7dd29c`; F2 = F0 (:186, :139).
- live-note `146 passed, 1 skipped, 15 warnings in 25.40s` (:187).
- `.env`: taken 05:27:33, removed and proven gone (`ls` → No such file, `no matches found`), lock released 05:43:08 (:138, :192); my own preflight `ls` → No such file.

## Scope
- opus: NOTHING WIDENED · astra: WIDENED — sheet replies reach schema init and attestation persistence; route-owned refusal texts · grok: NOTHING WIDENED.
- My path union (PREFLIGHT): only `src/cobalt/aset/{radar_panel,web}.py`, four test files and two DevDocs md files. My (i) `git log --oneline 5e77800f..78549817 -- src/cobalt/cards src/cobalt/radar src/cobalt/prefill src/cobalt/drc src/cobalt/settings src/cobalt/db_migrations` → EMPTY.

## Checked against the branch
claim · who · file:line · result · note
| claim | who | file:line | result | note |
|---|---|---|---|---|
| terminal ✓ correct has no status sink | opus, astra | `radar_panel.py:1354-1369`, `:1421`, `:1505-1507` | HOLDS | the only `.card-status[data-card-id]` is in the active detail (`:1421`); `.terminal-legs` carries the id on a div of another class |
| `/correct` never binds leg to the card in the URL | opus, astra, grok (a) | `web.py:1651-1673`; `legs.py:524-528` | HOLDS | `card_id` is used only in the message; the writer finds the card from `leg_id` |
| CLOSED manual card's estimated leg is not listed | opus, astra | `web.py:744`, `:1716`; report :168 | HOLDS | builder disclosed it (ESCALATE 8); sheet lists live states, `_sheet_in_trade` is FILLED+MANUAL only |
| manual failed position read shows no structural-stop line | astra | `web.py:1719-1721` | HOLDS | returns `_failed(...)` only; other in-trade renders carry `NULL — no Cobalt stop` |
| sheet's row prints `YOURS` unconditionally | astra | `web.py:710`; base `5e77800f:src/cobalt/aset/web.py:710` | DOES NOT HOLD as a C3 defect | the same line exists unchanged at the base |
| sheet GET upserts `day_modes` | astra | `web.py:496`; base :496 | DOES NOT HOLD as a C3 defect | pre-existing at the base; Grok says the same |
| `/stop` runs schema init before the writer | astra, opus | `card_stop.py:56`; base :56 | DOES NOT HOLD as a C3 defect | `card_stop.py` not in the diff |
| `_tap_price` accepts `NaN`/negative | opus | `web.py:1459-1466`; no price check in `legs.py` | NOT CHECKABLE FROM READS | `Decimal('NaN')` parses; whether a negative gives a 500 needs the DB CHECK to be run |
| S-WEB two clauses conflict on this base | astra, opus | `web.py:1433`, `:1530`; base last route `:1432` | HOLDS | `/release` was the last route at `5e77800f` (base `@app.` list); the block is after it and also at the end |
Also stated by me: (ii) `@app.` list at the tip — `/release` :1433, new routes :1530 `/triggered`, :1549 `/fill`, :1575 `/pass`, :1586 `/exit`, :1633 `/held`, :1651 `/correct`, :1675 `/stop`, :1688 `/stop/reset`; base list identical to the tip's up to `/release` (line numbers +1), so nothing after `/attest` moved, nothing after the pre-existing last route (which is `/release`) except the new block → HOLDS · (iii) `grep -rn -F "INSERT INTO" src/cobalt/aset` → one hit, `aset/store.py:129` (`aset_sizings`, pre-existing); none in `web.py` / `radar_panel.py` → HOLDS · (iv) L32: no ticker beyond constructed ones, no real date or value of his in this report.

## FOR THE CLASSIFIER
1. "Every new route calls only the named writers and store reads — no SQL, no running-count" · opus, grok · Q1 · `web.py:1530-1704` · HOLDS
2. "Prefill is `last_price`, NULL → empty, untouched `last_poll`/`estimated`, edited `typed`/`confirmed`, no-price refused" · opus, astra, grok · Q2 · `radar_panel.py:1215`, `web.py:1479`, `store.py:252` · HOLDS
3. "Every exit control posts the rendered `running_before`; the second tap gets C2's refusal verbatim" · opus, astra, grok · Q3 · `radar_panel.py:1304`, `legs.py:423-425` · HOLDS
4. "YOURS + delta only when `stop_owner` is `yours` (new stop block); structural stop in every radar in-trade render; ↺ gated; no stop edit in ARMED / TRIGGERED" · opus, grok · Q6 · `radar_panel.py:1239-1268`, `:1396` · HOLDS
5. "A FILLED manual card has the same controls through the same routes" · all three · Q7 · `web.py:1707-1725` · HOLDS
6. "X5 EXPIRED, X6-R `none`, X-M → sheet, all run" · all three · Q9 · report :60-62 · HOLDS
7. "The new routes are contiguous after `/release`" · all three · Q10 · `web.py:1433`→`:1530` · HOLDS
8. "Suites executed, 0 failed, F2 = F0, `.env` removed" · all three · Q11 · report :91, :178, :184, :186, :187, :192 · HOLDS
9. "Nothing in `cards/`, `radar/`, `prefill/`, `drc/`, `settings/`; no migration" · opus, grok · Q12 · (i) empty · HOLDS

## ESCALATE
1. **FIX (opus, astra) — HOLDS, my check:** a correction from the TERMINAL list has no status sink, so C2's refusal (stale, `market_reset`, …) is not shown. `radar_panel.py:1354-1369` / `:1505`.
2. **FIX (opus, astra, grok's note) — HOLDS:** `/radar/card/{id}/correct` corrects the card of `leg_id`, not the card in the URL, and the banner names the URL's card. `web.py:1651-1673`.
3. **FIX (opus, astra) — HOLDS (builder-disclosed, ESCALATE 8):** a flat on a manual card without ✓ closes as `estimated` and its leg is listed nowhere. `web.py:744`, `:1716`.
4. **FIX (astra) — HOLDS, narrow:** the manual card's failed position read omits the structural-stop line. `web.py:1719-1721`.
5. **Not C3's, my check (astra Q1/Q6/Q8):** sheet `YOURS`, `attest_sheet` on GET and `ensure_schema` on `/stop` are pre-existing at `5e77800f`; recorded, not counted.
6. **OPEN, desk's call (opus Q10, astra Q10, build ESCALATE 2):** S-WEB's "directly after `/release`" and "nothing after the file's last pre-existing route" conflict on this base; the desk's row for D2 stacking after C3 stands.
7. **Weak assertions (all three, OWED):** GET `/radar` test ran on a FAILED page and the sheet GET is never counted; no cross-card `/correct` test; no status-code assert on `test_s3_c3_panel_offline.py:225-238`; `_tap_price` `NaN`/negative untested (NOT CHECKABLE FROM READS). Size path (b): `/stop` on a sized WATCH card rewrites `shares` via the existing writer (`cards/store.py:805-823`), reached by a direct POST; not new in C3.
8. **Method deviation (mine):** copies and diff parts were made by shell (byte-verified by `wc -c` and a concatenation assert), not by Read → Write; and the report is at the scratch path because the `reports/` Write was refused.
Standing line: **Round 1 of ≤3 (L39) of S3 C3: Opus 5.5 (Fable seat, R109) · Astra · Grok (L67, R95). A HOLD → a fix round classified first (L75). `ready for C4: YES` → `26-s3-exits-c4-build.md` stacks on `<tip>`.**

S3 EXITS C3 CHECK DONE · round: 1 · opus: CHECK S3 C3: FIX (5) TERMINAL-LIST REFUSAL SINK, (5) /correct LEG-CARD BINDING, (a7) _tap_price NaN/negative · ready for C4: NO · terminal corrections drop refusals; /correct writes another card's leg · astra: CHECK S3 C3: FIX Q1/Q4/Q5/Q6/Q8; resolve Q10/Q12 · ready for C4: NO · Unintended writes and inaccessible corrections leave this build unready today. · grok: CHECK S3 C3: BUILD STANDS · ready for C4: YES · houses that checked: 3 of 3 · defects that HOLD: 4 · ready for C4: NO · ESCALATE: 8
