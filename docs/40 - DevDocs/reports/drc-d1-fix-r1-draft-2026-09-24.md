# DRC D1 FIX R1 — DRAFT (classify `54`'s 14 HOLDs, L75; write `14` build + `15` check)

Drafter `drc-d1-fix-r1-draft-0924`, Opus 5.5, 2026-09-24 07:38–07:50 ET (from `date`).

## §0 Headline
- Classified all 17 rows of `54`'s `## Checked against the branch` (14 HOLD) and its 12 ESCALATEs from the hub's own file-check column. Result: **FIX 13 · NOT REAL 2 · UNPROVEN 3 · OUT OF SCOPE 3 · OWNER ITEM 1**.
- Wrote `prompts/2026-09-24/14-drc-d1-fix-r1-build.md` (Opus 5.5, `acceptEdits`, base `7ed5e5ee`, red first, all three suites under L76, stop line as ordered). Wrote `prompts/2026-09-24/15-drc-d1-fix-r1-check.md` (round 2 of ≤3; Opus 5.5 + Grok, Sol from Sep 26th, 2026 6:47 AM; the grok gate is `09-24 R17`).
- New rule strings: **2** (the `drc-d1` `.env` pair, for `14`). `15` = `04`'s line byte for byte (diff-proved).
- ESCALATE: 5.

## Classification — `54` `## Checked against the branch` (L75; every FIX backed by a row that HOLDS)
| `54` row | claim (short) | `54` result | CLASS | fix row in `14` · trace |
|---|---|---|---|---|
| 1 | carried SHORT, no seed: first `B` opens a phantom long (`pairing.py:186-189`) | HOLDS | **FIX** (+ residue → OWNER ITEM O1) | F2 + F3. v2 `:81` / `:94` `[F-10]`: "a carried symbol with no prior row FAILs … never assumed flat". After any recorded day, the seed chain covers it: `check_contiguity` plus F3's not-computed FAIL (row 2). The reachable phantom is closed by F3. A seeded short is pinned (F2). The FIRST import alone cannot tell a cover from an open, because E1's cover code is `B` and so is an open (fixture README; `pairing.py:6`). That residue is his (O1). |
| 2 | `seed_for` seeds flat after a pairing-not-computed day (`store.py:192-201`, `:225-246`) | HOLDS | **FIX** | F3. v2 `:94` "never assumed flat"; L1. `seed_for` FAILS naming the prior day. |
| 3 | trading log: a non-UTF-8 byte on a data line is named `line 1` (`trading_log.py:188-190`) | HOLDS | **FIX** | F4. `53` D1-2 "every row validates … or the WHOLE file is failed"; `54` Q "naming the line". |
| 4 | the same in the stats log (`stats_log.py:292-294`) | HOLDS | **FIX** | F4 (`53` D1-4: "the same fail-loud … rules as D1-2"). |
| 5 | an empty `Open Date` cell reads "empty: Open Date, Open Time" (`pairing.py:275-279`) | HOLDS | **FIX** | F5. The reason names a cell that is not empty, so the shown fact is false (L1, L35). The fix is honest joint wording, and the model is not widened. |
| 6 | the real E1 date is committed (`README.md:4`, `test_drc_detect.py:318,324`, `trading_log.py:9`, the build report) | HOLDS | **FIX** | F1. L32; the L45 companion "dates … stripped"; L45 09-13 R5 "redact the report". The drafter also found his two file names (they carry the date) in the build report. F1 strips them too. |
| 7 | `pytest.raises(Exception)` on the system-role read (`test_drc_store.py:427`) | HOLDS | **FIX** (test-only) | F6. The query is schema-qualified and the exception is `InsufficientPrivilege`. A missing relation can no longer pass. |
| 8 | both-kinds file in a set: the set status is not asserted (`test_drc_detect.py:304-312`) | HOLDS | **FIX** (test-only) | F7: asserts `53` D1-2a's set rule (`pass`, the failed file listed). A different status is ESCALATEd, never fitted. |
| 9 | the partial reason is checked by `startswith` only (`test_drc_store.py:347`) | HOLDS | **FIX** (test-only) | F8b: the exact reason names `Account`, taken from the constant. |
| 10 | the undecodable-file test asserts no line (`test_drc_trading_log.py:166-168`) | HOLDS | **FIX** (test-only) | F4a: the red for row 3. |
| 11 | the carried-symbol test covers the long only (`test_drc_pairing.py:239-241`) | HOLDS | **FIX** (test-only) | F2: two carried-short tests. |
| 12 | `_bytes` docstring vs `QUOTE_MINIMAL` (`test_drc_stats_log.py:36,39`) | NOT CHECKABLE FROM READS | **UNPROVEN** (L70) | none. It needs a one-row `csv.writer` run, and no assertion depends on it. |
| 13 | edits outside the rows' named files: `test_p4_migrations.py`, `test_radar_migration.py`, `test_radar_score_migration.py`, `test_tenancy.py` | HOLDS | **OUT OF SCOPE** | none. Each hunk is required by `0016`'s place in `FORWARD` / `REVERSE`, and reverting one turns the suite red. The report states each one (D1-5 C, ESCALATE 2). The desk re-pins at the L68 gate. |
| 14 | `open_position` rows' `inputs` hold only `trading_log_import_id` (L57) | HOLDS | **FIX** | F8: the open position's inputs = its trade row's inputs (L57). |
| 15 | `drc_imports.degraded` stores the flag without the extra names | HOLDS | **FIX** | F9. `53` D1-2 "sets `degraded: trading_log_shape` naming it"; L9. `degraded` is `TEXT` with no CHECK (`0016_drc.sql:33`), so no migration change is needed. |
| 16 | "3 exit times" (report) vs "3 exit fills at 2 Times" (README / fixture) | NOT CHECKABLE FROM READS | **UNPROVEN** (L70) | none. It needs the real E1 file, and the fixture matches the README. |
| 17 | L52 NO PATH | no path found | **NOT REAL** | none. |

**The 14 HOLD rows:** 13 FIX (rows 1–11, 14, 15) and 1 OUT OF SCOPE (row 13).

## Classification — `54` `## ESCALATE` (12)
| # | item | CLASS |
|---|---|---|
| 1 | L32 real E1 date committed | FIX (= row 6, F1) |
| 2 | opus `CHECK D1: FIX` | FIX (= rows 1–6, 14, 15 — covered) |
| 3 | D1-3 carried short | FIX (= rows 1, 11) + OWNER ITEM O1 (residue) |
| 4 | D1-5 flat seed | FIX (= row 2) |
| 5 | D1-2 / D1-4 decode line, empty-cell reason | FIX (= rows 3, 4, 5) |
| 6 | the five weak assertions | FIX (= rows 7–11) |
| 7 | outside-the-rows hunks | OUT OF SCOPE (= row 13) |
| 8 | the minor storage notes | FIX (= rows 14, 15) |
| 9 | checker contradictions (D1-3, the L32 date) | **NOT REAL**. The hub's file-check settled both: rows 1 and 6 HOLD. |
| 10 | sol did not check (METER) | **OUT OF SCOPE**: a seat record. `15` records the return (Sep 26th, 2026 6:47 AM) and seats Sol from then. |
| 11 | R105 scope record | **OUT OF SCOPE**: a record, nothing to build. For `14`, the `.env` pair is on his ONE list (`## FOR DEJAN`). |
| 12 | NOT CHECKABLE carried (rows 12, 16; HEADER PROOF, the `4 of 4` zone proof, the with-DB counts) | **UNPROVEN** (L70). `14`'s D7 re-runs with-DB on the fixed tree, and D5 adds the live-note leg the D1 build never ran (it predates L68 GATE EARLY). |

**Totals (distinct items):** FIX 13 (rows) · NOT REAL 2 (row 17, ESC 9) · UNPROVEN 3 (rows 12, 16, ESC 12's builder claims) · OUT OF SCOPE 3 (row 13, ESC 10, ESC 11) · OWNER ITEM 1 (O1, row 1's residue).

## `14` — what it builds (FIX rows only, red first)
- **Base:** `7ed5e5ee` (branch tip: the D1 report commit over code `f6798406`). The launch line is `03`'s byte for byte, except the path, the `cd`, the rc `drc-d1-fix-r1-build-0924`, the mode `acceptEdits` (the desk's order) and the `.env` pair re-pathed (diff-proved: only the two `.env` strings differ in the allow list).
- **Red offline (D2):** EXPECTED 3 failed (F4a, F4b, F5). **Red with-DB (D3, first lock take):** EXPECTED 3 failed (F3, F8, F9). F2, F6, F7, F8b and F1's test rename are GREEN-as-pin, and `14` says so.
- **Edits (D4):** 15 paths = four `src/cobalt/drc/` files, five `test_drc_*` files, the fixtures README, the D1 build report (redaction), and four DevDocs. No migration, no `configs/`.
- **Gate (L68 / L76):** live-note (D5; four `requires_vault` files, baseline at D1), offline (D6), with-DB (D7, second lock take; the D1 build's three `cobalt_dev` deselects with their reasons), and a `0016` ABSENCE PROBE (the named-cursor test expected short by exactly 3). `.env` is removed and proven gone after each take.
- **Stop:** `DRC D1 FIX R1 BUILT <tip> | on <base> | red <hash> | offline <p>/<f> | with-DB <p>/<f> | live-note <p>/<f> | .env: removed | 0016: rolled back | FIX: 13 | ESCALATE: <n>`.
- **DESK LINE:** the desk launches `14` only while no `~/cobalt-wt/*/.env` exists and the 09-24 deploy (`09-setups-deploy-r2.md`) is not between its gate cut and its stop line.

## `15` — the check
Round 2 of ≤3.
- **Seats:** Opus 5.5 + Grok. Sol is METER until **Sep 26th, 2026 6:47 AM**; at or after that time `15` probes it and seats it. The check fails closed below TWO. No Gemini, no Astra.
- **Grok gate:** `grep -n "^| R17 " …/cto-2026-09-24.md`, plus R19 for the Opus / Sol strings. Never a dated row.
- **Packet:** the red + fix diff, the DevDocs diff, the code at tip, the build proofs, the executed output of all three suites (`suites.md`, L68), `54`'s rows and this classification, and v2 `:81/:88/:94/:191`. The build report's redaction diff is replaced by counts. The hub runs a DATE SWEEP itself (counts only).
- **Launch line:** `04`'s byte for byte (diff-proved IDENTICAL).
- **Placeholders:** both prompts carry `R__` twice (the gate text and the launch row), for the desk.

## OWNER ITEMS
O1 — First import only: DAS writes a short cover as `B`, the same code as a new buy, and the first day you import has no earlier day to check against — if you ever held a SHORT overnight into that first imported day, Cobalt would read the morning cover as a new long. Choose: (A) the first import is taken as flat (as built; you said you leave nothing open overnight), or (B) the first import FAILS until you state its overnight positions.

## FOR DEJAN
New rule strings for `14` (his ONE list; the same two strings were approved under 09-22 R105 for `48`–`57` only):
- `Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/drc-d1/.env)`
- `Bash(rm /Users/cobalt/cobalt-wt/drc-d1/.env)`

`14`'s AUTHORIZATION requires a committed `cto-2026-09-24.md` row of his, naming `14-drc-d1-fix-r1-build.md` and carrying his words, that approves these two strings. `15` needs no new string.

## ESCALATE
1. **L32 beyond this branch's fix (the desk's):** `14` strips the E1 date and his two file names from every file the D1 branch adds. The date stays in two places `14` does not touch. (a) The branch's EARLIER commits (`04b05cd4..7ed5e5ee`): a merge carries them into `main`'s history, and whether history is rewritten before the merge is the desk's call. (b) Files already on `main`: v2, `53`, `54`'s report (its stop-line quote of the D1 build line) and desk reports.
2. **Permission mode:** the desk ordered `acceptEdits` for `14`; `03` used `auto`. Under `acceptEdits` an unlisted Bash command raises a DIALOG (L63 state note), where `auto` would pass it to the classifier. `14` therefore binds the builder to exact listed prefixes and treats a dialog as FAILED. The mode is the desk's to confirm at launch (L62 R80: stated on the line).
3. **L76 stagger:** `14` takes the `cobalt_dev` lock TWICE (D3 red, D7 gate). The desk must not launch it inside the 09-24 deploy's gate window. If it is running when that window opens, the deploy's with-DB gate waits for its stop line (L76: the gate takes the lock alone).
4. **`0016` absence proof is indirect:** no `psql` is on `14`'s line, so D7 (d) proves `0016` absent by the named-cursor test's expected shortfall of 3 (the D1 build read `assert 28 == 31`). A different shape gives `0016: UNPROVEN` in the stop line, and the desk checks `cobalt_dev` before the next with-DB run.
5. **Live-note leg is new for D1:** the D1 build predates L68 GATE EARLY and never ran it. `14`'s D1 baselines it on `7ed5e5ee` first, so a base red is recorded, not blamed on the fix.

DRC D1 FIX R1 DRAFTED · FIX: 13 · NOT REAL: 2 · UNPROVEN: 3 · OUT OF SCOPE: 3 · OWNER ITEM: 1 · prompts: 2 · new rule strings: 2 · ESCALATE: 5
