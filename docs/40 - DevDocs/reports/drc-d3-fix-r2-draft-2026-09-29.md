# DRC D3 fix r2 — classification and the fix r2 build + check prompts (2026-09-29)

Seat `drc-d3-fix-r2-draft-0929` · Opus 5.5 · prompt `prompts/2026-09-29/20-draft-drc-d3-fix-r2.md` · authorization `cto-2026-09-29.md:104` (R96 LAUNCH ROW) · started 15:29 ET, closed 15:45 ET (`date`).

## §0 Headline
- `09`'s 3 `## FOR THE CLASSIFIER` items, its ESCALATE 1–12, the three seats' CHECK lines and its other file-check rows are classified from the hub's file-check column (L75): FIX 2 · NOT REAL 5 · UNPROVEN 3 · OUT OF SCOPE 0 · OWNER ITEM 0.
- The desk's reading holds: (a) F-7 → FIX F-7r2, (b) `--dry-run --no-trades` → FIX F-1r2. Each goes red first on `15c23748`.
- Written: `prompts/2026-09-29/21-drc-d3-fix-r2-build.md` (base `15c23748`, branch tip `7d064f2d`; F-1r2, F-7r2, RUN-4, RUN-5) and `prompts/2026-09-29/22-drc-d3-fix-r2-check.md` (round 3 of ≤3, THE LAST; Opus 5.5 · Sol · Grok).
- `21`'s line = `08`'s line without the R80 byte-write string, which is `09-28/10`'s line with only the path and name changed. `22`'s line = `09`'s line with only the path and name changed. New rule strings: 0. ESCALATE: 10.

## L74
A system-reminder block arrived inside this session's first tool result (the Read of `20`). It asked for a `Claude-Session:` trailer on commits and named `SendUserFile`. Recorded once here and not followed: this seat commits nothing and sends no file.

## Classification
`#` · finding (short) · source line · class · traces to · FIX shape or reason. Source lines: `C2` = `reports/drc-d3-fix-r1-check-2026-09-29.md`; `OC` / `SC` / `GC` = `…/agy-trial/scratch/tribunal-bars-0920/drc-check/d3-fix-r1/{opus,sol,grok}-check.md`; `B1` = the fix r1 build report. Code read at `15c23748` (`git show`).

| # | finding (short) | source line | class | traces to | FIX shape or reason |
|---|---|---|---|---|---|
| 1 | F-7: the control's rebuild fails the helper through its first line, the OLD rows assertion; the note half `:173` is never the raiser (opus, sol, grok) | C2:117, :139; OC:13; SC:9, :49; GC:11, :53 | **FIX F-7r2 (a)(b)** | `09-29/08` THE FIX ROWS (`08:12`) "its NEGATIVE CONTROL shows the old assertion passing where the new one FAILS"; `09-28/10` E3 `[F-19]`; L35 | Walked: `test_drc_d3_fix_r1_db.py:139`–`:142` rebuild, then `pytest.raises`. `_snapshot_holds` `test_drc_build_db.py:168` is `_build_rows == before` (the old `:155`@a8c622ca). **Red first on `15c23748`:** the strict contract (the old rows assertion PASSES on the input, then the helper raises with a message that starts `  - card: `) run on r1's own rebuild input. It fails at the old-assertion step, which is the HOLD as a run. **Fix:** the input becomes "no rebuild, the helper asked for a stop the note does not carry". r1's rebuild leg is kept after it. The helper is unchanged. |
| 2 | F-7: the pin still cannot fail on its defect; nothing between the dict change and the helper reads the card (opus, grok) | C2:118, :140; OC:13; GC:53 | **FIX F-7r2 (c)** | L35 "a test that cannot fail on its defect is not proof"; `[F-19]` | Walked: `test_drc_build_db.py:154`–`:155`. The snapshot is a JSON copy (`build.py:288`–`:292` `_card_snapshot`). **Fix:** between `:154` and `:155`, the pin plans D through the build's own read (`plan_note`, which writes nothing, L10). It asserts the plan's AAA `card:` line carries `$48.0`, so the change is real where the build reads the card, and then that the stored rows and note still carry `$49.9`. It can now fail if a read with the changed card moves the snapshot. Green on `15c23748` (a pin). C2's item 4 counts items 1–2 as one defect, so they are one FIX row. |
| 3 | F-1: `--dry-run --no-trades` reaches `imports.no_trade` before the dry-run guard and writes a statement (sol; grok NOT CHECKABLE) | C2:119, :141; SC:3, :48; GC:62 | **FIX F-1r2** | `09-28/10` D3-4 (`10-drc-d3-build.md:58`) "`--dry-run` writes nothing"; L10; L1 | Walked at `15c23748`: `cli.py:268` `if args.no_trades:` sits before `:279` `if args.dry_run:`. `:269` → `imports.py:655` `no_trade` → `:672` `record_stated_book` (and the rebuild `:683`). The flags are independent (`:252`, `:254`). **Fix:** `cmd_build` first refuses the pair with one named line (`DRY_RUN_NO_TRADES`) and `SystemExit(2)`. `imports.no_trade`, `state-book` and each flag alone are unchanged (L3: the no-trade preview stays `state-book`'s dry run). **Red:** the parser is built in-process and `no_trade` / `record_stated_book` are spied; this gives `AssertionError: imports.no_trade called on a dry run` on `15c23748`. **Pin:** the build command's `store_true` flags are exactly `{dry_run, no_trades}`, so "every combination the CLI accepts" is two cases, each tested. |
| 4 | F-5's build half asserts `unmapped playbooks: 2` without tying it to the bad note (opus, grok) | C2:120; OC:59; GC:54, :65 | **UNPROVEN → RUN-5** | L70; hub: NOT CHECKABLE FROM READS | Nobody ran which names make the count. RUN-5 rebuilds F-5's construction and states `<n>`, the constructed names, and whether the bad note's name is among them. |
| 5 | The 21:10 process and the build's resident resolve the same vault root string (opus) | C2:121; OC:64 | **UNPROVEN** (a deploy record, no RUN) | L70; hub: NOT CHECKABLE FROM READS — "needs the environment of both production jobs" | This lane never reads a production job's environment, so no build RUN can settle it. It is carried as a record into `21`'s `## FOR THE DEPLOY` (K10.2's note equality at the deploy). |
| 6 | `test_drc_d3_fix_r1.py:197`–`:199` and `test_drc_build.py:309` hold a literal U+00A0, not the escape F-6 named (opus) | C2:122; OC:65 | **NOT REAL** | hub fact C2:122: `test_drc_build.py` literal count 1, and `:197` holds the character | The rule protects the U+00A0 byte from being normalised to U+0020. The hub's `grep -P` shows the byte is present, and the tests that use it are green against the fixture's U+00A0 (B1:102, :120). A normalised copy would fail loud, not pass. Consequence carried into `21`: those two files and the fixture are NEVER opened by Edit / Write (this seat counted 3 in `test_drc_d3_fix_r1.py`), so F-1r2's tests go in a NEW file. |
| 7 | Whether `risk_parameters_line` (opus), or `plan_note` before `build.py:536` (grok), writes anything on the dry-run path | C2:123; OC:66; GC:63 | **UNPROVEN → RUN-4** | L70; hub: NOT CHECKABLE FROM READS | Nobody ran it. RUN-4 does a dry run with the real `risk_parameters_line`, wrapping every open-for-write, rename, replace and mkdir, and states the count and the paths. |
| 8 | The seam cites `build.py:324`, `:689`, `:697`–`:713`, `units.py:125`, `store.py:1436`, `checks.py:461` were not in any slice (opus, grok) | C2:124; OC:54; GC:64 | **NOT REAL** | hub: the build report's own greps print those lines (B1:105) | Grok says "Not a defect". The cause is the packet. `22`'s `code-at-tip` now slices each of them. |
| 9 | The F-2 test's `ts` stamp is set by an `UPDATE` of the writer's own row (the builder's open ASK DESK, B1 ESCALATE 2) | C2:153 (ESC 9) | **NOT REAL** (no finding) | all three houses: F-2 CLOSED (C2:54) | No house claims a defect. It is the desk's open ASK and is carried, not built. |
| 10 | Two deviations inside named files: E3's `Take all` literal (B1 ESC 3) and `units.py`'s docstring (B1 ESC 4) | OC:10, :32 | **NOT REAL** | all three houses: `KEPT` and `NOTHING WIDENED` (C2:77–:86) | Both were escalated by the builder and read by the checkers, and no house objects. |
| 11 | L52 path | SC:51; OC:61; GC:56–:58 | **NOT REAL** | all three: NO PATH | `build.py:621` prints the stored grade and computes none. |

Folded, not counted separately: C2's ESCALATE 1–3 (the three CHECK lines) are rows 1–3. Opus's "F-7 control fails on old rows check; note half unproven" is row 1. Sol's "dry-run no-trades still writes; F-7 control also fails old assertion" is rows 3 and 1. Grok's "F-7 control fails where the old row assertion also fails" is row 1. Opus ESCALATE 1 (OC:69, the builder's claim "the helpers raise where the old assertions would pass") is row 1. Grok's `--no-trades` NOT CHECKABLE (C2:147) is settled by row 3's HOLD. The round-1 classes of `reports/drc-d3-fix-r1-draft-2026-09-29.md` stand unchanged: C2's file-check column brings no new evidence against any of them.

## RECORDS
`09`'s `## ESCALATE`, beyond the rows above, each a RECORD (no defect of its own):
1. ESC 4: the count `defects that HOLD: 2` treats items 1–2 as one defect (F-7) and item 3 as the other. That matches FIX 2 here.
2. ESC 5: the packet measured 258,048 B with no cut. The deviations are the L32 redaction and U+0020 in copies. No checker wrote a stray file. `22` states the K17 formula and this measured size.
3. ESC 6: L74 was recorded by the hub.
4. ESC 7: RUN-1 rendered, RUN-2 equal, RUN-3 4 of 4. These are results, not defects (L70).
5. ESC 8: O-1 was answered A (R66 / R80). F-6's U+00A0 half is built (7 at the tip, 0 at the base). This round writes no fixture byte, so `21` drops the R80 string.
6. ESC 9: all three seats were SEATED. The builder's ASK DESK is row 9.
7. ESC 10, the build's `## FOR THE DEPLOY`, is carried whole into `21`'s `## FOR THE DEPLOY`:
   - RESTARTS for both ranges.
   - The two UNCLASSIFIED config rows (`configs/cobalt/prefill.yaml` M, `configs/cobalt/templates/drc.md.j2` D) stay UNCLASSIFIED (L42) and are never guessed.
   - `.clinerules` is OWED (R74).
   - `0019` / `0020` at migrate.
   - The `com.cobalt.prefill-drc` bootout and plist.
   - His daily-stop value.
   - The E7 ops read of D2.
   - The dev-vault diff proof, which also answers round 1's OUT OF SCOPE row 16.
   - Added as a record: row 5's vault-root read.
8. ESC 11–12, the standing lines: `22` re-states them for round 3, and a HOLD there goes to Dejan (L39).

## OWNER ITEMS
- **This round holds none.** Both FIX shapes are design questions the houses settle in round 3. Nothing touches his money, data, laws or trading judgement. O-1 (round 1) was his and is answered.

## FOR DEJAN
- New strings: NONE. `21` = `08`'s line less one string (R80's byte-write, unused this round) = `09-28/10`'s line with path and name changed. `22` = `09`'s line with path and name changed. `comm` over the tokens shows 0 other differences.

## ESCALATE
1. **F-7r2 is an ASSERTION row, so its "red first on `15c23748`" is the HOLD as a run.** The code (the helper) is right. The red is the strict negative-control contract run on r1's own rebuild input, and it fails at the step "the old rows assertion passes". The fix is the input change. `22` question (i) asks for exactly this.
2. **F-1r2's shape is a refusal (exit 2), not a dry-run preview of the no-trade path.** Reasons: L3 (the one preview is `state-book --no-trade DAY`, already a dry run by default); L1 (loud, non-zero); it widens nothing. Round 3's houses judge it.
3. **`22` deviates from `09`'s shape in these places:**
   - `## FOR THE CLASSIFIER` becomes `## FOR DEJAN`. Round 3 has no classifier (L39).
   - `round-1.md` becomes `round-2.md`.
   - `nbsp-proof.md` now proves that the three U+00A0 files were never opened.
   - `code-at-tip` adds the seam lines that round 2 left unsliced (row 8).
   - `rules.md` carries D3-4, E3's `[F-19]` line and `08`'s assertion-row doctrine.
   The launch line is byte for byte.
4. **The never-opened rule** (row 6): `test_drc_d3_fix_r1.py` (3 U+00A0 bytes, counted by this seat), `test_drc_build.py` (1, the hub) and the fixture (7). `21` PREFLIGHT counts them, F4 re-counts them, and `22` `nbsp-proof.md` proves them untouched.
5. **A reading, not a finding:** r1's control shows that a rebuild with a changed card re-snapshots the card, by design, because a rebuild re-reads it. No house claims that `[F-19]` should survive a re-pair. It is not classified and not built. It is named here once so the desk can see it.
6. **Launch-time values:**
   - `21` carries `R__` and one `«FILL AT LAUNCH»` (the desk's tip read).
   - `22` carries `R__` and `«FILL AT LAUNCH»` for the built line, tip, reds, report commit, range, path union and ceiling.
   - Each file's gate allows the token only on line 1 and on the gate's own line.
7. **`22`'s ceiling is left to the desk** (K17: the formula is the measured staged packet; the precedent is `09`'s 258,048 B under 400,000 B, R86).
8. **`21`'s DESK LINE:** the desk launches `21` only while `ls ~/cobalt-wt/*/.env` has no match and no with-DB run is in flight (L76).
9. **Seat names:** `drc-d3-fix-r2-build` / `drc-d3-fix-r2-check`, with no `-0929` suffix, as `08` / `09` had.
10. **L74:** recorded under `## L74`.

## CONTINUE
next: none — the run is over. The desk commits the three files: this report, `prompts/2026-09-29/21-drc-d3-fix-r2-build.md` (52,899 B) and `prompts/2026-09-29/22-drc-d3-fix-r2-check.md` (46,658 B).

DRC D3 FIX R2 DRAFTED · FIX: 2 · NOT REAL: 5 · UNPROVEN: 3 · OUT OF SCOPE: 0 · OWNER ITEM: 0 · prompts: 2 · new rule strings: 0 · ESCALATE: 10
