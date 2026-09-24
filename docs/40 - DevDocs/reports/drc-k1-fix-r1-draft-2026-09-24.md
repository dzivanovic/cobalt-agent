# DRC K1 FIX ROUND 1 — CLASSIFICATION (L75) + THE FIX BUILD `48` AND ITS CHECK `49`

Drafter `drc-k1-fix-r1-draft-0924`, Opus 5.5, started Thu Sep 24 17:26:23 EDT 2026 (from `date`). Prompt `prompts/2026-09-24/47-draft-drc-k1-fix-r1.md`; authorization `cto-2026-09-24.md:89` `| R76 |` names it. Branch read: `drc/d1-trading-log` = `a50e5515` above `9a0fc900` (`git -C /Users/cobalt/cobalt log --oneline -2 drc/d1-trading-log`).

## §0 Headline
- Classified all 26 rows (3 HOLDs · `40`'s 14 ESCALATEs · `39`'s 9): **FIX 3** (H1 `opened_on`, H2 derived `reason`, H3 seam (2)) · **UNPROVEN 1** → RUN-1 · **OUT OF SCOPE 4** · **NOT REAL 15** · **OWNER ITEM 1** (H1's residue). Counts are over DISTINCT findings; 7 rows restate another row and are marked `= #n`.
- Wrote `prompts/2026-09-24/48-drc-k1-fix-r1-build.md` (red first, RUN-1, three suites under L76; stop `DRC K1 FIX R1 BUILT … | FIX: 3 | RUNS: 1 …`) and `49-drc-k1-fix-r1-check.md` (round 2; Opus + Grok, Sol from Sep 26th 6:47 AM; packet lists the four deselected ids). Both carry `R__`.
- New rule strings: 0 (`48` = `14`'s line, `49` = `15`'s, byte-checked with `grep -c -F`: 1 hit in each precedent and each new file).
- `## FOR K2`: the seam MOVES (H1, H2, H3). ESCALATE: 4.

## L74
- One block arrived as a system-reminder beside the Read of `47` (a `Claude-Session:` commit line and a file-send tool). Recorded once; not followed. This seat commits nothing and sends no file.

## Classification
Sources: `C` = `reports/drc-k1-check-2026-09-24.md` (`40`); `B` = `/Users/cobalt/cobalt-wt/drc-d1/docs/40 - DevDocs/reports/drc-k1-build-2026-09-24.md` (`39`); v3 = `docs/30 - Design/DRC-OVERNIGHT-POSITION-v3-2026-09-24.md`. Code at `9a0fc900` (worktree tip `a50e5515`, docs only above it).

| # | claim (short) | source line | class | traces to | FIX shape or reason |
|---|---|---|---|---|---|
| H1 | a stated position's `opened_on` = the stated day — false for a swing opened before D, and kept by every carry | C:149 (row 1), C:172; code `pairing.py:122`, `:216`, `:298` | **FIX** | L1; v3 `:134` (an `opening` position is `{symbol, direction, shares, avg_cost|null}` — v3 names NO open day); B:251 pin 2 | `OpenPosition.opened_on` → `Optional[date]` (`models.py:133`); `stated_open_positions` → `None`; `_Book.seeded` so `:298` keeps a seeded book's `None` and a new book keeps `day`. Two assertions reversed, named: `test_drc_k1.py:132`, `test_drc_k1_store.py:420`. Red offline + with-DB. Residue → OWNER ITEM 1 |
| H2 | derived `reason` stores `chain broken at <P>` when P IS recorded (the chain is not broken) — permanent in an append-only table | C:150 (row 2), C:173; code `store.py:485-489`; append-only `0018_drc_stated_books.sql:49-51` | **FIX** | L1; v3 §2c `:108` (a stated opening exists for "the first import ever … or a chain the page cannot close"); v3 `:139` (the reasons); R51 ("REBUILDS the later days from the earlier day's close" — the close wins) | `_reason` refuses an `opening` for D while `prior_trading_day(D)` has a `day` row (`ValueError`, nothing written); `record_stated_book` (`:543`) and `preview_stated_book` (`:507`) both refuse; CLI unchanged (`drc/cli.py:142` catches `ValueError`). `test_seed_iv_…` (`test_drc_k1_store.py:394-399`) SETUP reordered to R51's order, assertion byte for byte. Red with-DB |
| H3 | seam (2) silent on whether the route records the unpaired day `record_day(pairing, ids, None)` | C:151 (row 3), C:174; B:227-228; code `store.py:212-217` | **FIX** (seam statement) | v3 §4 row 1 `:212` ("stores files; pairing not computed"), X2 (a) `:313` (the `day` row's `not_computed`); L72 | `## SEAM FOR D2` (2) amended: the route RECORDS it (a `day` row, no `seed`, no `book_close`) and the next day FAILS `pairing not computed` until stated; one with-DB GREEN-as-pin test. Written whole in `48`, superseding `39`'s |
| C-E1 | = H1 | C:177 | = H1 | — | dup, not counted |
| C-E2 | = H2 | C:178 | = H2 | — | dup, not counted |
| C-E3 | = H3 | C:179 | = H3 | — | dup, not counted |
| C-E4 | two current `resolve` rows for one `trade_id` on different days both accepted | C:180, C:153 (row 5); `store.py:547-549` | **OUT OF SCOPE → K2** | v3 `[F-01]` `:126` / §4 `:226` — "FAIL naming both ids" is in the column "What the import does": a READER's failure, not a write refusal; K1's reader already FAILs on ANY stored resolve (`store.py:379-389`); `[F-06]` (K2) replaces that raise | carried in `## FOR K2`; Opus: "This belongs to K2." |
| C-E5 | `record_day` accepts a caller-built `SeedBook(stated, stated_book_id=<absent id>)` | C:181, C:154 (row 6); `store.py:212-217` | **NOT REAL** | Opus: "not a defect"; the hub did not count it; seam (3) names `seed_for` as the book's source; no production caller exists (B:253) | a guard would be a new behaviour no HOLD backs (L75: nothing widens). `48`'s seam (3) restates "`book` is the `SeedBook` `seed_for` returned" (text only) |
| C-E6 | X5 `design-changing`: Opus "yes, by the letter", Grok + build "no" | C:182, C:104-106; B:77, B:91 | **NOT REAL** | v3 X5 `:316`: result "the CHECK unchanged → a new numbered file, never the fold (`[F-02]`'s "Otherwise")" — that result occurred (`CheckViolation`), and its consequence IS the design as built (`0018`, `39` C6) | by the column's letter the result ran; it changes nothing built. Recorded: `design-changing: 0` in `39`'s stop line is the builder's reading; the letter reads 1-with-no-change |
| C-E7 | `match_stats` compares `entry_time` with `==`; a stated trade's stats row goes unmatched; no test runs a stated seed with a stats log | C:183, C:155 (row 7); `pairing.py:366-369` | **UNPROVEN** (L70) | Opus `NOT CHECKABLE FROM READS`; the hub walked it, no run | RUN-1 in `48` D5: stated seed + closing file + one-row stats log → no exception, stats row `unmatched`, reason quoted; red → strict `xfail`, reported, not fixed |
| C-E8 | Grok `DESELECTS OPEN` (the fourth deselected id not in the packet) | C:184, C:152 (row 4) | **NOT REAL** (DOES NOT HOLD) | the hub walked `test_tenancy.py:697`, `:710`, `:263`, `test_migrate_proof.py:306` = 4 | PACKET RULE in `49` §1 (6): the four ids listed by name, each `grep -n`-confirmed; `48` D8 writes them into its report |
| C-E9 | = B-E7 (the DRAFTER PINS line) | C:185 | = B-E7a–e | — | dup, not counted |
| C-E10 | = B-E8 (`book_sha256` binds positions, not day / kind) | C:186 | = B-E8 | — | dup, not counted |
| C-E11 | Astra METER — the K1 NEW BUILD's Astra read | C:187 | **OUT OF SCOPE** (the desk's seat) | L67 (a new build: Fable · Astra · Grok); L62 R19 ("use it after it's back") | a fix round is never Astra-seated (L67); the desk seats Astra's read of K1 from Sep 26th, 2026 6:47 AM. `48` / `49` carry the line |
| C-E12 | L74 block recorded | C:188 | **NOT REAL** | L74 | recorded once, not followed |
| C-E13 | standing line: HOLD → fix round | C:189 | **NOT REAL** (state) | L75, L39 | this round is that branch |
| C-E14 | standing line: the deploy's L68 gate re-proves the stack | C:190 | **OUT OF SCOPE** (the deploy's) | L68 | carried into `49`'s standing line |
| B-E1 | R22 scope read as the drc-d1 pair (desk reading) | B:245 | **NOT REAL** | desk R61, R65 (1) | `48` records the same reading, not a stop |
| B-E2 | a backtick grep raised a dialog, cancelled by the desk | B:246 | **NOT REAL** (process) | L63; 09-24 evening lesson (1) | `48` / `49` carry "grep patterns carry no backtick, no `\|`, no alternation" |
| B-E3 | `drc_stated_books` in a `models.py` docstring, edited back by `--amend` | B:247 | **NOT REAL** | L40; both checkers `NOTHING WIDENED` (C:110-111); re-grep clean (C:158) | resolved in `9a0fc900` |
| B-E4 | one test edit outside S5's line list (`test_radar_score_migration.py:122`) | B:248 | **NOT REAL** | Opus "None is a loosened comparison"; Grok "signature consequences" (C:94) | the same hunk kind as `:104` |
| B-E5 | C3 refusal names the CURRENT ids (the new row has none yet) — builder reading | B:249 | **NOT REAL** | v3 `[F-01]`; C3 `MEETS THE ROW` from both (C:88) | as built |
| B-E6 | stored-resolve FAIL bounded `day <= D` — builder reading | B:250 | **OUT OF SCOPE → K2** | v3 `[F-06]` `:190` (K2 replaces the raise) | carried in `## FOR K2` |
| B-E7a | pin: stated `trade_id` `<symbol>-<direction>-stated-<day>` | B:251; C:139 | **NOT REAL** (kept as built, recorded) | both `SOUND` | the day in the id is a label, not an open-day claim (stable across restatements of that day) |
| B-E7b | pin: `opened_on` = the stated day | B:251; C:140 | = H1 (**FIX**) | — | dup, not counted |
| B-E7c | pin: the X4 hash encoding | B:251; C:141 | **NOT REAL** (kept as built) | both `SOUND`; X4 green (B:90) | — |
| B-E7d | pin: the derived `reason` | B:251; C:142 | = H2 (**FIX**) | — | dup, not counted |
| B-E7e | pin: `seed_for` case (iv) FAILS until K2 | B:251; C:143 | **NOT REAL** (kept as built) | both `SOUND`; R51's rebuild is K2's (v3 §6 K2 `:248`) | H2 narrows how (iv) is reached (R51's order only); `## FOR K2` |
| B-E8 | `book_sha256` hashes positions only — `--apply --sha256` binds positions, not day / kind | B:252; C:186 | **NOT REAL** (recorded) | v3 `:135` defines the hash over `positions`; R52 (the printout beside the hash in his approval message); Opus "not a finding" | changing the hash is a v3 change, not a K1 fix; the desk keeps the printed row beside the hash |
| B-E9 | K1 has no production caller until D2; the check is `40` | B:253 | **NOT REAL** (record) | v3 `[F-10]` `:256` | — |
| O1 | H1's residue: what open day a stated swing carries | C:149; v3 `:134` | **OWNER ITEM** | L67 owner-items clause: his data — only he knows the day he opened a swing; adding the field is his friction call (L30) | NOT built; until he rules, `None` = not stated (L1). `## OWNER ITEMS` |

Distinct totals: FIX 3 · UNPROVEN 1 · OUT OF SCOPE 4 (C-E4, C-E11, C-E14, B-E6) · NOT REAL 15 (C-E5, C-E6, C-E8, C-E12, C-E13, B-E1–B-E5, B-E7a, B-E7c, B-E7e, B-E8 (= C-E10), B-E9) · OWNER ITEM 1 = 24; dups 7 (C-E1–3, C-E9, C-E10, B-E7b, B-E7d).

## FOR K2
**Does the seam move: YES** — three clauses of `39`'s `## FOR K2` / `## SEAM FOR D2`, written whole in `48` (its report's `## SEAM FOR D2` supersedes `39`'s):
- **H1:** `OpenPosition.opened_on` becomes `Optional[date]` — `None` for a stated position and every carry of it (`models.py:133`, `pairing.py:122`, `:298`). K2's R51 comparison of a stated book with a recorded close must not compare `opened_on`.
- **H2:** `record_stated_book` refuses an `opening` for D while D's prior trading day is recorded (`store.py:477-489`). `seed_for` case (iv) (`store.py:360-367`) is then reached ONLY in R51's order (D stated first, P recorded after) — exactly what K2's rebuild replaces. Seam (4) gains that sentence.
- **H3:** seam (2): the route RECORDS the unpaired day (`day` row with `not_computed.pairing`, no `seed`, no `book_close`). K2's forward re-pair and empty-day record meet such rows.
- Also carried to K2 (OUT OF SCOPE here): `40` ESCALATE 4 (two current resolves across days → K2's `[F-06]` reader FAILs naming both) and `39` ESCALATE 6 (the `day <= D` bound).
- Desk's call (L72): K2's DRAFTER can run beside `48` if it cites THIS section and `48`'s `## SEAM FOR D2` / `## FOR K2` text (the seam is settled in documents both cite); K2's BUILD launches on `48`'s tip, after `49`.

## OWNER ITEMS
- When you state an opening book that holds a swing you opened on an earlier day, do you want to give that swing's open day too (optional), or is "opened: not stated" enough?

## FOR DEJAN
- New strings: NONE. `48` = `14`'s line (the drc-d1 `.env` pair is your R22, carried by `14` / `39`); `49` = `15`'s line (standing strings R17 / R19).

## ESCALATE
1. H2 is a behaviour change on the write path (a refusal), not a text change: the only two `reason` values v3 names for an `opening` are both false when P is recorded, and v3 §2c / R51 give a statement no role then. If the desk reads R51 as wanting that statement STORED as history even when made after P, H2 needs a v3 `reason` value instead — a design question for the houses (L67), not built here.
2. H1 leaves K3's unit field "`opened_on` · trading days held" (v3 `:76`, §5 `:236` "opened <date> · day <k>") with no date for a stated swing; `48` seam (7) says "opened: not stated". K3's drafter reads it; `day <k>` for such a swing is K3's to state.
3. `48` D4's REORDER RULE lets the builder touch `test_drc_k1_experiments.py` only to move a statement before its prior day's record; a test whose assertion depends on the refused order FAILS the build rather than being edited. I found one such setup (`test_drc_k1_store.py:394-399`, named); others, if any, surface only at D4's proof.
4. `48`'s DESK LINE: at drafting `42` stale-score holds the `cobalt_dev` lock and `43` H1 is queued; `48` waits its turn (L76).

DRC K1 FIX R1 DRAFTED · FIX: 3 · NOT REAL: 15 · UNPROVEN: 1 · OUT OF SCOPE: 4 · OWNER ITEM: 1 · prompts: 2 · new rule strings: 0 · ESCALATE: 4
