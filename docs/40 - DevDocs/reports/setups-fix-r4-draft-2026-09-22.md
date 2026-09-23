# SETUPS FIX ROUND 4 — drafter report (`71`, Opus 5.5, seat `setups-fix-r4-draft-0922`, 2026-09-22 21:03–21:1x ET, times from `date`)

## §0 Headline
- Classified every finding of `setups-check-r2r3-2026-09-22.md` (L75): **FIX 5 · NOT REAL 8 · UNPROVEN 3 · OUT OF SCOPE 2 · OWNER ITEM 3** (Q1, Q2, and a new Q3: the word-only proposal grades).
- Wrote `72-setups-fix-r4.md` (Opus 5.5, `auto`, OFFLINE, `setups-c1`, base `8da261a`; stop line `… | with-DB: OWED (68) | …`) and `73-review-devdb-repair.md` (Sonnet 5 hub, Grok + Gemini read `68`, date gate R30).
- `72` = `33`'s line byte for byte **plus ONE appended string**: `12`'s cutter string (R23). That is a NEW USE of a precedented string, and it needs his word. `73` = `25`'s line byte for byte, no new string.
- Drafter find, not a check finding and not built: the precedent cutter `_cut_p2_fixtures.py` has the same date-only shift, with a September real day re-dated onto a January synthetic day. The committed-day pins may also be an hour off. ESCALATE 2.
- ESCALATE: 9.

## CLASSIFICATION
Ids: `H<n>` = a row of the check's `## Checked against the branch` table, in table order. `P<n>` = another claim in the check (proposal table, assertions table). `Q<n>` = `## FOR DEJAN`. `E<n>` = the check's `## ESCALATE` item. `## FOR THE CLASSIFIER` items 1–6 map to H1, H2, H3, H4, H6 and H7 (noted per row). ESCALATE 1–7 restate the rows mapped here and are not counted twice.

| id | finding (≤2 lines) | backing file-check row (hub's own) | CLASS | fix / reason | `72` row |
|---|---|---|---|---|---|
| H1 · FTC 1 · E1 · E2 | [CUT] C1: `_shift_datetime_str` moves only the calendar date and keeps the UTC clock. An EDT real day re-dated onto an EST synthetic day lands 1 h early in NY local time | `cut-diff.md:334-341`, live `tests/fixtures/radar/_cut_setups_fixtures.py` (`:47-53`, drafter read) — **HOLDS** | **FIX** | re-date on the New York wall clock (zoneinfo); re-cut from `12`'s saved raw inputs and argv; re-copy the five pins from printed output (`13` re-derives them) | **F4** |
| H2 · FTC 2 · E3 | [CUT] the real day is a literal in `test_setups_fixture_cut.py`'s docstring | `tests/cobalt/test_setups_fixture_cut.py:3` — **HOLDS** | **FIX** | remove the real day from the docstring; add a pin that every ISO date in the test and cutter is a synthetic day | **F3** |
| H3 · FTC 3 · E4 | [CUT] C3: the pinned cut formation does not correspond to the stored day's line. The stated reason is real but incomplete (the hour shift is a second cause) | `cut-report.md` FIND vs `## PIN`, `cut-diff.md:163-174` — **HOLDS** | **FIX** | after F4, a `## C3` table in NY local time with one verdict. Cause (1) removed by F4; cause (2), the definition difference, is named UNPROVEN beyond the reading | **F5** |
| H4 · FTC 4 · E5 | [R3] F6(a): `_per_trade_accepted` treats any `VaultTaxonomyError` as "not reachable" and never asserts why | `fix-diff-r3.part1.md:44`, live `test_setups_fix_r3.py:405-406` (drafter read) — **HOLDS** | **FIX** | match the engine-key refusal's own message; re-raise anything else; a malformed probe note must raise (RED on base) | **F1** |
| H5 | how-to and r3 report attribute the per-trade refusal to `merge_tunables`, while the probe's refusal comes from `load_vault_trade_defs` | `adding-a-setup-at-tip.md:18`, `r3-report.md:108` vs `fix-diff-r3.part1.md:30,44` — **NOT CHECKABLE FROM READS** | **UNPROVEN** (L70) | not built. F1 RECORDS the raise site only; the doc is not edited | — (recorded in F1) |
| H6 · FTC 5 · E6 · P0 | [R3] `leg.min_size_atr` (A-24) SHOULD BE NULL: no source addresses pullback size | r3 report ESCALATE (i) concedes it; R48/R49 rule — **HOLDS**, unanimous | **FIX** | the gitignored proposal row `A-24` → null. Committed config is already `value: null` | **F2** |
| H7 · FTC 6 · E7 | [R2] `tests/cobalt/test_radar_anatomy.py` touched outside [R2]'s CLOSE list | PREFLIGHT `--stat` of `90c9f56` / `c62e593` — **HOLDS**, "known, accepted deviation" | NOT REAL (as a defect) | disclosed by r2 (ESC vii), accepted by the desk's R113 (b). No content defect was raised, and reverting it would undo r2 F2's A1 | — |
| H8 | [R3] `test_setups_lego.py` (comment) and `leg_roles.py` touched outside `rows.md`'s fix column | `70` §1 item (25) boundary list — **DOES NOT HOLD** | NOT REAL | both files are on the round's authorized list | — |
| P1 | proposal grades `flat_threshold.ema9` (A-09), `flat_threshold.vwap` (A-10), `dist.k.vwap` (A-16): Grok says SHOULD BE NULL (no source number); Gemini and Opus say GRADE STANDS | the check's `## Proposal keys` — a 1-vs-2 split on reading R48/R49, not file-checked as a HOLD | **OWNER ITEM** (Q3) | whether a word-only source can carry an assumed value is his rule. No vote (L39) | — |
| P2 | Opus (a): `_tunables_digests`' unit overwrite is a weaker assertion | `## Assertions and boundary` R3 opus: "covered by `test_f5`" | NOT REAL | the checker's own cell says it is covered | — |
| P3 | Opus (c): an L52 path through second-chance with an assumed A-24 row | `## Assertions and boundary` R3 opus — **NOT CHECKABLE** | **UNPROVEN** (L70) | the run it names was never made. It is moot while A-24 is null (F2) | — |
| P4 | the CUT commit `65c08a0`'s own message carries the real day | the check's (viii), H2 note: "also present in commit `65c08a0`'s message" | OUT OF SCOPE | history is never rewritten. Named in `72` ESCALATE (iii) | — |
| Q1 | [R2] stop resolvers declare no `tunable_keys`, so a stop reading an undeclared engine key could sit outside a def's closure. Latent: no live def is affected | check `## FOR DEJAN` Q1 (all three agree) | **OWNER ITEM** | → `## FOR DEJAN` | — |
| Q2 | [R3] a note row for an engine key is refused, and an Assumed-Defaults row tunes every setup reading that key. Opus adds: `per_trade(<loaded def>)` rows exist, but whether one fills a global hole is `merge_tunables`' predicate (NOT CHECKABLE) | check `## FOR DEJAN` Q2 | **OWNER ITEM** (its NOT CHECKABLE half is UNPROVEN, not counted twice) | → `## FOR DEJAN` | — |
| E8 | standing coverage line (range, round 2 of 3) | — (a record) | NOT REAL | no finding | — |
| E9 | `13` (the blind re-derivation of the five cut pins) is owed, and should wait for the cutter's hour-shift fix | check ESCALATE 9 | OUT OF SCOPE (next law step) | `13` runs AFTER `72` (see (A)3 below) | — |
| E10 | every with-DB claim of the three reports is UNPROVEN until `68` lands | check ESCALATE 10 | **UNPROVEN** (L70) | `72` is offline. Its stop line carries `with-DB: OWED (68)`, and `## WITH-DB OWED` names the set | — |
| E11 | the `Claude-Session:` trailer in `65c08a0`'s message | check ESCALATE 11 | NOT REAL | L74: data, recorded once by the check | — |
| E12 · E13 · E14 | no proposal/report mismatch · no packet mismatch · no ASK DESK | check ESCALATE 12–14 | NOT REAL | no finding | — |

**Counts** (one per row, first class): FIX **5** (H1, H2, H3, H4, H6) · NOT REAL **8** (H7, H8, P2, E8, E11, E12, E13, E14) · UNPROVEN **3** (H5, P3, E10) · OUT OF SCOPE **2** (P4, E9) · OWNER ITEM **3** (Q1, Q2, P1 → Q3). Each FIX row is backed by a hub row that HOLDS. The fix widens nothing: no `src/`, no `configs/`, no committed-day pin, and `_cut_p2_fixtures.py` stays untouched.

## DIGEST FOR THE DESK
- **Launch order:**
  - `72` now, in the build lane. It holds NO dev-DB lane (offline, no `.env`), so it runs beside `68`.
  - `73` in the house lane, once `59`, `63` and the r4 check are clear.
  - `68` after `73`'s stop line + the folds + his ONE approval.
  - The r4 check (check round 3 of 3) after `72`'s stop line. `13` after `72`. The with-DB re-run after `68`.
- **`72` needs, before launch:**
  - the launch row `R__` carrying `NEW USE` + his quoted "approve" for `Bash(uv run python tests/fixtures/radar/_cut_setups_fixtures.py *)` (R23's string, `12`'s worktree);
  - the check report (staged `A`, uncommitted now) and THIS report, both committed (its AUTHORIZATION greps both with `-S`).
- **`72` rows:**
  - F1 probe asserts why (test only).
  - F2 A-24 → null (gitignored file only).
  - F3 real-day docstring + an ISO-date allowlist pin.
  - F4 cutter keeps the NY wall clock. Commit 1 is the code and its test; commit 2 is the re-cut and five pins re-copied.
  - F5 `## C3` correspondence (+1 printed field).
  - Expected: `src` / `configs` diffs EMPTY, `RESTARTS: none`.
- **`72` risks:**
  - `12`'s raw inputs sit in the harness tmp dir, and a reboot deletes them. `72` then FAILs F4 and names the re-point (ESCALATE 3).
  - The corrected cut may form nothing. The IF-NOTHING rule applies: FAILED, the re-cut is left uncommitted, and the desk rules.
- **`73`:**
  - Packet: `68` whole · `env.py`, `devdb.py` whole · `db_query.py:98-178` · `test_tenancy.py:659-711` · drafter READING + ESCALATE (a)–(f) · R110 / R112 / R30 · 12 greps.
  - Q1–Q5 as `71` names them, plus the UNUSED / WIDER strings.
  - Stop line `DEVDB REPAIR REVIEWED · grok: … · gemini: … · blockers: <n> · string changes: <n> · ESCALATE: <n>`.
  - The launch row must carry `59 is not running` · `63 is not running` · `r4 check is not running` (or those reports' stop lines).
- **(A)3, the NEXT CHECK is round 3 of 3, THE LAST (L67 / L39).** It is `70`'s shape re-pointed to r4's range `8da261a..<r4 tip>`. Not drafted here. Re-point lines in `70`:
  - `:1` seat / remote-control (`setups-check-r4-0922`), the LAW STEP text, the range, and the prompt path in the launch line (strings otherwise byte for byte).
  - `:3` title and scope ([R4] F1–F5 only).
  - `:9` the fix-path calls → `72-setups-fix-r4.md`.
  - `:10` R112 → the desk's r4 decision row.
  - `:11` R113 → a new launch row.
  - `:18` the built line → ONE line, `SETUPS FIX R4 BUILT … | on 8da261a |`.
  - `:19`–`:21` chain, range list and branch tip.
  - `:22`–`:25` the boundary → `72`'s CLOSE list.
  - `:30` / `:39` recovery folder → `setups-check/r4/`.
  - `:32` stagger → add `73`.
  - `:37` the report path and stop prefix.
  - `:43`–`:52` the packet: r4 diff; the re-cut bars excerpted, never whole; r4 report `## F1`–`## F5`, `## C3`, `## PINS MOVED`.
  - `:61` RED-on-base base → `8da261a`.
  - `:81` per-FIX rows → [R4] F1–F5.
  - `:88`–`:92` protected paths → `src`, `configs` and the four pin files EMPTY.
  - `:108` standing line → "THIRD house check, round 3 of 3, the last".
  - A HOLDS there goes to `## FOR DEJAN` (no fifth round).
- **`13` runs AFTER `72`'s re-cut** (check ESCALATE 9). Re-point in `13`:
  - its base (the r4 tip);
  - the five constants' line numbers in `test_setups_fixture_cut.py`;
  - the fixture files (re-cut; same paths);
  - never the check's packet folder.

## RULE PROOF
Each check was one `grep -c -F -e "<span>"` call. The span runs from `--model` to the last `--add-dir`, quotes included.

| check | file | count |
|---|---|---|
| `33`'s span, rc `setups-fix-r3-0922`, 19 allow + 3 deny + triplet | `33-setups-fix-r3.md` | 1 |
| the same span with rc `setups-fix-r4-0922` and ONE string appended after the `rm .env` string: `"Bash(uv run python tests/fixtures/radar/_cut_setups_fixtures.py *)"` | `72-setups-fix-r4.md` | 1 |
| that appended string | `12-setups-fixture-cut.md` | 2 (approved R23, `cto-2026-09-22.md:125`) |
| `25`'s span, rc `stacked-deploy-review-r2-0922`, 9 allow + 3 deny + triplet | `25-review-stacked-deploy-r2.md` | 1 |
| the same span with rc `devdb-repair-review-0922` | `73-review-devdb-repair.md` | 1 |

- `73` vs `25`: the only differences are the prompt path and the remote-control name, as expected.
- `72` vs `33`: the prompt path, the remote-control name, and ONE appended precedented string. This is not the expected set; see ESCALATE 1.
- The cwd in each launch is its parent's (`setups-c1`; `agy-trial`), and the mode is its parent's (`auto`; `auto`).

## NEW strings:
None never-approved. ONE NEW USE: `"Bash(uv run python tests/fixtures/radar/_cut_setups_fixtures.py *)"` in `72`, the same string in the same worktree that R23 approved for `12`. It needs his word on `72`'s launch row, and `72`'s AUTHORIZATION refuses without it.

## FOR DEJAN
(Owner items, one per message, quoted from the check; A/B are the drafter's framing, no recommendation.)
- **Q1 — stop resolvers and `tunable_keys`.**
  - Check, quoted: "All three checkers agree: `closure_keys` unions the trigger resolver's declared reads (this round's own fix) but stop resolvers still declare none, so a stop that reads an undeclared engine key (Opus names `pivot.n`, read by `recent_higher_low`/`range_base` stops) could in principle sit outside a def's closure. All three note the eight corpus defs already name the matching atoms, so no live def is affected today — the gap is latent, not active."
  - **A:** leave it; it is a backlog item for when a new definition needs it.
  - **B:** stop resolvers declare their keys too; that is a small build with its own check, after this deploy.
- **Q2 — per-setup tuning of an engine dial.**
  - Check, quoted: "All three checkers confirm the report's own finding: a note row for an engine key is refused, and an `Assumed Defaults` row tunes every setup that reads that key (`global`/`per_indicator` scope), not one setup alone. Only a def's own `cfg(<trade_key>.…)` keys are per-setup (today: hitchhiker's duration band). If "tune the setups so the noise subsides" (R61) is meant per-setup, the only lever today is writing the number into each def's own text."
  - **A:** an engine dial stays one number for every setup that reads it; per-setup tuning = the number written into that setup's own note.
  - **B:** a per-setup scope for engine dials, as a design item that goes to a tribunal.
- **Q3 — the three word-only proposal values (NEW owner item).**
  - Check, quoted: "Grok's reading treats "no source number" (a word only, no figure) as disqualifying for all four; Gemini and Opus read R48/R49's "sheet-derived assumed value" rule as satisfied by a word-only passage for A-09/A-10/A-16, and draw the SHOULD BE NULL line only at A-24".
  - **A:** the desk writes the three proposed values into your `Assumed Defaults` as ASSUMED, LOW confidence, then you tune them live.
  - **B:** all three stay null until you set them; fashionably-late and vwap-continuation then do not form at defaults.
  - (Info, no ruling: A-24, the minimum-size rule, goes null by the unanimous finding. The rule is off until you set a number, as R49's "we tune in live" allows.)

## ESCALATE
1. **`72` is not byte-for-byte `33`.**
   - C1's fix needs the fixture re-cut, and only `12`'s cutter string runs it. That string is not in `33`'s line.
   - `ASK DESK: bring the NEW USE of R23's cutter string to him with 72's launch? [21:13]`.
   - Safe default, if he declines: the desk re-issues `72` without the string. F4 then builds only commit 1 (the cutter code + its test). The re-cut + pins + F5 move to a `12` re-point (its R23 strings), and the check reads both.
2. **DRAFTER FIND, not a check finding, not built (L75).**
   - `tests/fixtures/radar/_cut_p2_fixtures.py:37-53` re-dates a SEPTEMBER real anchor (EDT) onto the January synthetic day with the same date-only `_shift_datetime_str`.
   - The committed P2 day may carry the same one-hour NY-local offset. That day is the source of the 17 committed-day `DEF_WRITTEN_*` pins (`17` re-derived them blind, on the same bars).
   - UNPROVEN as a defect (L70): a code read. Nobody has shown the bars against the session clock.
   - `ASK DESK: have the r4 check read it as an extra question, or run a separate item? [21:13]`. Safe default: the r4 check does not ask it, and the desk carries it on the plate.
3. **`12`'s raw inputs are ephemeral.** The two raw files sit in the harness tmp dir, and a reboot deletes them. The daily CSV is in the production cache. `72` PREFLIGHT checks the byte counts. Absent → F4 FAILED, and the raw reads are re-done through `12`'s production strings (R23). Launch `72` before any host restart.
4. **L45 / L32 residue outside the check's rows, drafter read, not built.**
   - `12`'s committed report (`a09c6da`, on the branch) names the real day and ticker in several places.
   - The CUT commit message does too (P4, OUT OF SCOPE).
   - Redacting the report (L45 companion: "redact the report") is the desk's call.
5. **`73`'s packet is wider than `71` listed.** Added: `db_query.py:98-178` (Q1: `68`'s Q rule relies on it), the drafter's READING 1–9 (Q2 / Q4: its dump-vs-recreate and head claims), rows R110 / R112 / R30, and a `docker-compose.yml` container grep. Each is strikable by a re-issue. The house timeout is 20 min (vs `25`'s 15) for the larger packet; that is not a rule string.
6. **`73`'s stagger (s3):** the r4 check has no prompt number yet, so the gate is the launch-row literal `r4 check is not running` alone. The desk writes it, or holds `73`.
7. **`72` F4's IF-NOTHING rule** leaves the re-cut fixtures uncommitted on FAILED. `72` has no `git checkout` / `restore` string, so the desk restores them. A re-point of `12` for a new day, or `rubberband` back into `AWAITING_A_DAY`, is the desk's / his call.
8. **With-DB is OWED for rounds 2–4** (`68` first). `72`'s `## WITH-DB OWED` names the set (`33`'s CLOSE set + the r3 and r4 modules) and the seat the desk names.
9. `MEMORY:` fix-round drafters check whether a fixture cutter's re-dating crosses a DST boundary. Twice now, the date-only shift carried a UTC clock string across EDT → EST (`12`'s cutter, and by code read the P2 precedent). `[stated 2026-09-22 · setups-fix-r4-draft]`

## CONTINUE
next: none. `72`, `73` and this report are written. The desk commits all three plus the check report, fills `R__` in `72` / `73`, and brings the NEW USE to him.

SETUPS FIX R4 DRAFTED · FIX: 5 · NOT REAL: 8 · UNPROVEN: 3 · OUT OF SCOPE: 2 · OWNER ITEM: 3 · prompts: 2 · new rule strings: 1 · ESCALATE: 9
