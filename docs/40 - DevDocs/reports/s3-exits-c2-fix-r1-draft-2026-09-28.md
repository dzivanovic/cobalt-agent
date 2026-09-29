# S3 exits C2 fix r1 — drafter report (2026-09-28)

Seat `s3-exits-c2-fix-r1-draft-0928` (Opus 5.5, auto), desk row R160 (`cto-2026-09-28.md:169`). Start `date` → `Mon Sep 28 21:21:54 EDT 2026`. `<r1>` = `reports/s3-exits-c2-check-2026-09-28.md`; `<b>` = the C2 build report on `s3/exits-c2`. Branch tip read 21:22: `0d591041` over `77cf18fd` (as expected).

## §0 Headline
- 3 FIX, all traced: CLOSED only by the zero-running leg (v3 §2), one fill-cache writer (L3), a pre-C1 card closed by its exits still reads its position (C2-3 / C2-7 / O21 A).
- 2 RUNS for the UNPROVEN: R1 the three suites re-executed and quoted, R2 three test-file reads.
- 16 NOT REAL (6 weak-assertion or path facts, the L31 prose word, 10 FOR THE CLASSIFIER confirmations); 0 OUT OF SCOPE; 0 OWNER ITEM.
- Written: `prompts/2026-09-28/54-s3-exits-c2-fix-r1-build.md` and `55-s3-exits-c2-fix-r1-check.md` (Opus · Sol · Grok); no new rule string.
- ESCALATE 2: C2 lands with C3, never alone, after F1; L74.

## L74
Recorded once: a system-reminder block arrived appended to the first tool result (the read of this prompt file), asking for a `Claude-Session:` line in commits and PR bodies and naming a file-send tool. Not followed; I commit nothing and sent no file.

## Classification
Every class is taken from the hub's file-check column (`<r1>` `## Checked against the branch`) or, where the hub walked nothing, from `<r1>`'s own "not visible to this read" line (L35 / L70).

| # | finding (short) | source line | class | traces to | FIX shape or reason |
|---|---|---|---|---|---|
| 1 | FILLED → CLOSED is writable at running above 0 with no leg, through the sheet's `/card/{id}/move` and `cobalt cards move --to CLOSED` (Opus (4)) | `<r1>:106`, `:107`, `:137`; Per question `:77` | FIX → **F1** | v3 §2 transition table (`S3-EXITS-v3-2026-09-22.md:90`): FILLED → CLOSED = "the zero-running leg", evidence `{leg_id}`, one transaction; `22` C2-2; C1-4's FILLED refusal on the same two paths is the shape (`20`, `test_fill_c1_offline.py:265`, `:285`) | Route body and `cmd_move` refuse `to = CLOSED` before any store call, loud; red = offline stub tests whose `transition` must not be reached. The guard stays at the two call sites. A guard in `transition()` is OUT OF SCOPE, as C1 fix r1 ruled it (`s3-exits-c1-fix-r1-draft-2026-09-28.md:28`). Grok's reading (`cli.py:89` "pre-existing generic") is not a counter-finding: C2 did not widen the path, but the design names one CLOSE trigger. |
| 2 | `_rewrite_fill_cache` is a second UPDATE of the fill cache; `aset/store.py:361-362` still says "written only by `mark_filled`" (Opus (6); builder ESCALATE 4) | `<r1>:108`, `:138`; `:79` | FIX → **F2** | L3; v3 Q4 `[F-04]` (`S3-EXITS-v3-2026-09-22.md:319`) "No other path writes them"; R67 N (the correction rewrites the cache in its own transaction — kept, never reopened, L77); `22` C2-3 | `AsetStore._update_fill_cache(..., at_fill=True)` stays the ONE UPDATE; `at_fill=False` omits `filled_at` / `drift_warning_pct`; `legs._rewrite_fill_cache` keeps its recompute and writes through it; docstring names both callers. Red: offline scan, `actual_fill = %s` in `src/cobalt` → exactly one (two at `77cf18fd`). With-DB guard test after a FILLED stop edit (not red by design). |
| 3 | On a card filled before C1 (no entry leg), the ✓ confirm (a correction) and `cobalt cards legs` are refused `no_position` once the card is CLOSED (Opus (1) edge) | `<r1>:109`, `:139`; `:74` | FIX → **F3** | `22` C2-3 (a correction needs a FILLED **or CLOSED** card), C2-7 (`cards legs` shows legs, running, basis), O21 A (pre-C1 basis); `<b>` `## SEAM FOR C3` (✓ confirm of an `estimated` flat = a correction) | `running_shares`: CLOSED + no entry leg + at least one current exit leg → the O21 A basis; nothing else changes. Red: with-DB, pre-C1 card, flat `estimated` → CLOSED, ✓ confirm → `LegRefused no_position` at `77cf18fd`. |
| 4 | Over-entry test asserts the refusal only, not "nothing written" (Opus (a)(1), Grok (a)(1)) | `<r1>:110`; `:85` | NOT REAL | `22` C2-3 requires the refusal; the refusal raises before `_insert_leg` (Opus Q(3), `<r1>:76`; `legs.py:557-561`) | A test fact, not a defect against any row; nothing is tightened (L75 widens nothing). |
| 5 | Held-count-on-CLOSED test asserts the refusal only (Opus (a)(2)) | `<r1>:111`; `:85` | NOT REAL | `22` C2-4; refusal raised before any INSERT (`<r1>:76`) | Same as 4. |
| 6 | Reset-refusal and `market_reset` tests assert no `card_stop_edits` count (Opus (a)(3)) | `<r1>:85` (no hub row) | UNPROVEN | L70; the hub walked no row for it | RUN **R2** read: `grep -n -F "card_stop_edits" tests/cobalt/test_legs_c2_db.py`, quoted. |
| 7 | No test of the plan-at-fill cache branch (Opus (a)(4)) | `<r1>:85`, `:115` ("not visible to this read") | UNPROVEN | L35 / L70 | RUN **R2** read: `grep -n -F "stop_in_force" tests/cobalt/test_legs_c2_db.py`, quoted. F2's with-DB test covers the branch either way. |
| 8 | No test of a pre-C1 closing-exit correction (Opus (a)(5)) | `<r1>:85`, `:115` | UNPROVEN | L35 / L70 | RUN **R2** read: `grep -rn -F "no_position" tests/cobalt`, quoted. F3's red test covers it either way. |
| 9 | Holding-0 test does not assert `evidence["leg_id"]` (Grok (a)(2)) | `<r1>:112`; `:85` | NOT REAL | `22` C2-4 "`held = 0` → CLOSED as C2-3"; one close path `_close_if_zero` (`legs.py:228-238`) whose evidence is asserted at `test_legs_c2_db.py:261` | A test fact; the evidence is written by the one function already proven. |
| 10 | `cobalt cards legs` test asserts the `realized R: ` prefix, not the figure (Grok (a)(3)) | `<r1>:113`; `:85` | NOT REAL | `22` C2-7 (read-only render); C2-5's figure proven in `test_realized_r.py:25-72` (`<r1>:80`) | A test fact, not a defect. |
| 11 | Paths to a size: the entry-price correction writes `recomputed_shares`; the WATCH stop edit writes `shares` (Opus (b), Grok (b)) | `<r1>:114`; `:86` | NOT REAL | R67 N / `22` C2-3 (the cache is ruled); WATCH edit is pre-C2 behaviour (`store.py:813-823`); hub: no score, rank, grade or planned `shares` on FILLED | No L52 path. |
| 12 | The suite counts were reported, not re-executed (Opus Q(10) "re-run needed to confirm"; hub "Not checkable from reads") | `<r1>:83`, `:115` | UNPROVEN | L70 | RUN **R1**: `54` W executes offline, with-DB (two passes) and live-note; summaries quoted whole. |
| 13 | The word "Fable" in `legs.py:5` docstring and `cards/legs.md:4` (Q(11)) | `<r1>:84`, `:99` | NOT REAL | L31 binds identifiers, schema, config keys, enum values; both seats: NOTHING WIDENED, prose only | A provenance word in prose, not an identifier. |
| 14 | FC1 `running_shares` the only running read, under the lock, basis rule | `<r1>:125` | NOT REAL | Q(1) HOLDS | A confirmation; its pre-C1 CLOSED edge is row 3. |
| 15 | FC2 one connection, one commit; X7; X21 before-fix | `<r1>:126` | NOT REAL | Q(2) HOLDS | A confirmation. |
| 16 | FC3 the nine refusals loud, nothing written | `<r1>:127` | NOT REAL | Q(3) HOLDS | A confirmation. |
| 17 | FC4 C2's writers close through `transition()` in the same transaction | `<r1>:128` | NOT REAL | Q(4) HOLDS | A confirmation; the "nowhere else" half is row 1. |
| 18 | FC5 the held count | `<r1>:129` | NOT REAL | Q(5) HOLDS | A confirmation. |
| 19 | FC6 corrections append-only; cache rewrite in the same transaction | `<r1>:130` | NOT REAL | Q(6) HOLDS | A confirmation; the L3 half is row 2. |
| 20 | FC7 `realized_r.1` | `<r1>:131` | NOT REAL | Q(7) HOLDS | A confirmation. |
| 21 | FC8 the FILLED stop edit | `<r1>:132` | NOT REAL | Q(8) HOLDS | A confirmation. |
| 22 | FC9 X-OPEN carry | `<r1>:133` | NOT REAL | Q(9) HOLDS | A confirmation. |
| 23 | FC10 NOTHING WIDENED; no name in an identifier | `<r1>:134` | NOT REAL | Q(11) HOLDS; hub checks (i)–(iv) `<r1>:118-121` | A confirmation. |

Totals: FIX 3 · NOT REAL 16 · UNPROVEN 4 (→ 2 RUNS) · OUT OF SCOPE 0 · OWNER ITEM 0.

## RECORDS
- `<r1>` ESCALATE 4 — Astra METER at 20:12 (back 8:58 PM): no round spent (L67). The fix check `55` seats Sol in its place (K22, R151); Astra is not relaunched.
- `<r1>` ESCALATE 5 — the builder's asks 2–4: ALREADY ANSWERED by the desk (TAKEN). Ask 4 is reopened only by HOLD row 2 → F2.
- `<r1>` ESCALATE 6 — the round-1 standing line; round 2 is `55`.
- Desk question (ii) "store": `55` asks for every `.transition(` caller in `src` that can reach CLOSED. At `77cf18fd` they are `legs.py:236` (`_close_if_zero`), `cli.py:89` and `web.py:1251`. The other `.transition(` callers go to FILLED, EXPIRED or PASSED (`store.py:535`, `:549`, `:1193`, `expire.py:203`, `web.py:1338`). F1 closes the two call sites.
- `54` / `55` carry the `R__` row placeholder and `«FILL AT LAUNCH: …»` values; `55`'s `<packet ceiling>` is the desk's (K17).
- RULE STRINGS checked (before `date` 21:29:45): `54` line 5 equals `22` line 6 once the path and name are masked (`diff` empty); `comm -3` of the quoted tokens prints only the two `Read '…'` paths. `55` line 1 against `23` line 1 prints only the two `codex exec` strings (Astra / Sol). The Sol string has `grep -c -F` = 1 in `51` line 1 and in `43` line 1.

## OWNER ITEMS
NONE.

## FOR DEJAN
New rule strings: NONE.

## ESCALATE
1. ASK DESK: after F1, no route or CLI writes CLOSED until C3's panel calls `record_exit`. A C2 deployed alone would leave him no way to close a FILLED card. Safe default taken: F1 as classified; the desk lands C2 only in the stack with C3, never alone. [21:29 ET, from date]
2. L74: recorded once under `## L74`.

## CONTINUE
next: none. The desk verifies (L35), commits `54`, `55` and this report, writes `54`'s launch row (`<base>`, `no with-DB run in flight`) and launches it only while `ls ~/cobalt-wt/*/.env` has no match and no with-DB run is in flight (L76).

S3 EXITS C2 FIX R1 DRAFTED · FIX: 3 · NOT REAL: 16 · UNPROVEN: 4 · OUT OF SCOPE: 0 · OWNER ITEM: 0 · prompts: 2 · new rule strings: 0 · ESCALATE: 2
