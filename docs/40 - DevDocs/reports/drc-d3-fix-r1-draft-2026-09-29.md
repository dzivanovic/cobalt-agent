# DRC D3 fix r1 — classification and the fix r1 build + check prompts (2026-09-29)

Seat `drc-d3-fix-r1-draft-0929` · Opus 5.5 · prompt `prompts/2026-09-29/07-draft-drc-d3-fix-r1.md` · authorization `cto-2026-09-29.md:61` (R53 LAUNCH ROW) · started 09:49 ET, closed 10:0x ET (`date`).

## §0 Headline
- `09-28/11`'s 10 HOLDs, its ESCALATE 1–9, both seats' CHECK lines and its other file-check rows are classified from the hub's file-check column (L75): FIX 8 · NOT REAL 5 · UNPROVEN 2 · OUT OF SCOPE 1 · OWNER ITEM 1.
- Written: `prompts/2026-09-29/08-drc-d3-fix-r1-build.md` (F-1 … F-8, RUN-1 … RUN-3, base `a8c622ca`, branch tip `7dd031fb`) and `prompts/2026-09-29/09-drc-d3-fix-r1-check.md` (round 2 of ≤3; Opus 5.5 · Sol · Grok).
- Both launch lines `comm`-clean against `10` / `11` (only the path and the name differ). New rule strings: 0.
- O-1 (his): the fixture's seven U+00A0 bytes cannot be written on `10`'s line. `08` builds the name half only.
- ESCALATE: 6.

## L74
A system-reminder block arrived inside this session's first tool result (the Read of `07`). It asked for a `Claude-Session:` trailer on commits and named `SendUserFile`. Recorded once here and not followed: this seat commits nothing and sends no file.

## Classification
`#` · finding (short) · source line · class · traces to · FIX shape or reason. Source lines: `R1` = `reports/drc-d3-check-2026-09-25.md`, `OC` = `…/drc-check/d3-0925/opus-check.md`, `GC` = `…/grok-check.md`. Code read at `a8c622ca` (`git show`).

| # | finding (short) | source line | class | traces to | FIX shape or reason |
|---|---|---|---|---|---|
| 1 | D3-4: `--dry-run` writes the generated rules file (opus, grok) | R1:134, :102; OC:20; GC:16 | **FIX F-1** | `10` D3-4 row (`10-drc-d3-build.md:58`): "`--dry-run` writes nothing"; L10 | Walked: `drc/cli.py:277` → `build.py:556` `deps.rules_block()` → `build.py:160` `rules_checkbox_block` → `prefill/drc.py:82` `regenerate_rules_config()` → `prefill/rules_gen.py:156`–`:158` writes. Fix: the dry-run branch in `drc/cli.py` plans with `dataclasses.replace(deps, rules_block=<one named line>)`. The real build is unchanged (F41). Red: the regenerator spied, `rules_block` not stubbed. |
| 2 | D3-6: K10.2 FAILs a miss line written after midnight (opus, grok) | R1:135, :103; OC:22; GC:18 | **FIX F-2** | `10` D3-6 row (`:60`): "PASS when `done` and both present" | Walked: `s2.yaml:524`–`:526` counts any note's writes by `ts` ET date. The build stamps at clock time (`build.py:161` `now=None`), so a next-morning write FAILs. The same predicate also PASSes D on another note's write. Fix: count `vault_writes.note` = the event row's `note_path` (both `str(path)`: `vaultwrite/writer.py:537`, `:657`; `0019_drc_events.sql:32`), with no `ts` predicate. `08` PREFLIGHT proves the two writers compose the path identically (`replay/line.py:212`, `drc/template.py:71`). Red: two with-DB cases. |
| 3 | D3-2: the stop line skips `_Stats.text` under a partial stats file (opus) | R1:136, :104; OC:16 | **FIX F-3** | `10` D3-2 row (`:54`), "a value fed by a column a `partial` file lacks → `not computed — missing`"; 09-23 R17 (5); L1 | Walked: `build.py:632`–`:633` reads `stats.row` directly. `_Stats.text` (`:304`–`:311`) returns `not computed — missing` for an unmatched row. Grok's MEETS cites `:634` "stop from the stats row only" and does not walk the partial case (GC:12, :24). Fix: `stop: ` + `stats.text("stop")`. Pins keep `not given` / as-is (R17 (4)). |
| 4 | D3-2: `drc-risk/facts` sits under `### PnL on the day:`, not above his risk paragraph (opus; builder ESCALATE 9a) | R1:137, :105; OC:16 | **FIX F-4** | `10` D3-2 row (`:54`) "`drc-risk/facts` above his risk paragraph"; v2 §13 A9 (`DRC-AUTOMATION-v2-2026-09-22.md:273`) "facts above his paragraph", ruled with §13 (R69–R72); R40 item 9(a) leaves "above" to this classifier | Walked: `units.py:50`, `:92`; `build.py:545`. His `### How I managed risk:` is fixture `:45` and `### PnL on the day:` is `:49`. `find_section` refuses a duplicate section, and `pnl` must stay under the PnL heading (R102 O16), so one section cannot satisfy both. Fix: `facts` gets its own section `drc-risk-facts`, placed under `### How I managed risk:`. `drc-risk` keeps `pnl` and `risk_parameters` where built. E3's heading map is re-pointed with the code. |
| 5 | D3-2b: a non-UTF-8 strategy note fails the build (opus, low) | R1:138, :106; OC:18 | **FIX F-5** | `10` D3-2b row (`:56`): "NEITHER a build failure"; "An unreadable strategies folder → the build does NOT fail" | Walked: `playbooks.py:95` raises `UnicodeDecodeError` (a `ValueError`), and `:97` catches only `SlugError, FrontmatterError, OSError`. Grok's MEETS (GC:14) lists the except tuple without the error type. Fix: the tuple gains `UnicodeDecodeError`. |
| 6a | D3-1: the fixture's first heading carries his name (opus; builder ESCALATE 5) | R1:139, :107; OC:15 | **FIX F-6** | L45 "personal attribution … stripped"; L31; R40 item 5 | Read: `template_shape.md:5` carries his name (1 hit; not reproduced here). Fix: that one line becomes `# Example Trader DRC` plus its trailing character. Leak grep reported without text. |
| 6b | D3-1: U+0020 at the seven heading positions where his template has U+00A0 (opus; desk item R40 5) | R1:139, :107; OC:15; GC:11 | **OWNER ITEM O-1** | L45; R40 item 5 ("FIX if the committed fixture differs"); L62 (a grant is his) | Read: the fixture has `grep -c -P "\xc2\xa0"` = 0. His template carries U+00A0 at `:5`, `:49`, `:128`, `:134`, `:156`, `:173`, `:175` (35 lines in all; the rest are prose that the fixture replaces). The fixture differs, so the defect holds. `10`'s line has no string that writes the byte. Write / Edit normalise U+00A0 to U+0020 (build report `:108`; re-proven by this seat on its own report: `grep -c -P "\x{00A0}"` → 0). Only a grant of his, or his waiver, moves it. |
| 7 | Scope WIDENED: `replay/models.py`, `prefill/config.py`, D2 harness / registry-pin test lines, `test_drc_settings.py` (opus) | R1:140, :108; OC:44–48 | **NOT REAL** | R40 item 8 (the two paths accepted as the rows' smallest seats); R40 item 6 (the D2 harness lines accepted); build ESCALATE 7 (registry pins shift by one, as every migration's do); D4's `## FOR D3` names the build as the readers' caller | Every widening was escalated by the builder and accepted by the desk's R40. No unaccepted path remains. Grok: NOTHING WIDENED (GC:39). |
| 8 | E3 / E6 / E8 / E11: the E1 table's post-code cells are empty (grok; opus notes the same) | R1:141, :109; GC:30–33; OC:36–39 | **NOT REAL** (+ RUN-3) | build report `:150` names the four tests; `:223` offline and `:228` with-DB, 0 failed, the files not skipped | This is a report-form gap: the tests are green inside the gate counts. RUN-3 quotes the four PASSED lines by node id so round 2 holds them. |
| 9 | Weak: the with-DB card-snapshot test cannot fail (opus) | R1:142, :110; OC:70 | **FIX F-7** | `10` E3 list (`:137`): "`drc_rows` inputs snapshot survives a later `aset_sizings` update (`[F-19]`)"; L35 | Walked: `test_drc_build_db.py:154`–`:155` mutates a dict and re-reads stored rows. Fix: a pin + negative control (the `58` 0d shape). The helper asserts the rows AND the note's card line. The control re-builds with the changed card and shows the helper failing. |
| 10 | Weak: the re-pair test asserts only `is_file()` (opus) | R1:143, :111; OC:71 | **FIX F-8** | `10` E3 list (`:137`): "D3-2r re-builds the later day's `build_*` rows and note"; L35 | Walked: `test_drc_build_db.py:202`. Fix: a pin + negative control. The summary unit's text must differ from before and equal `units.summary(<re-paired build_day>)`. The control shows the helper failing on the unrewritten text. |
| 11 | `cli.py:280` names `PairingError`; import unproven (opus, NOT CHECKABLE) | R1:113; OC:90 | **NOT REAL** | hub: DOES NOT HOLD | `drc/cli.py:45` `from .models import PairingError, StatedBook` (read at `a8c622ca`). |
| 12 | `build.py:609` `units.money(gross_pnl)` with no None guard, on a day ending with an open position (opus) | R1:114; OC:91 | **UNPROVEN → RUN-1** | L70; hub: NOT CHECKABLE FROM READS | `units.money` is `Decimal(str(value))` (`units.py:100`–`:102`), so `None` would raise. Whether the stored open trade's `gross_pnl` is `None` is a pairing fact (`pairing.py:184` `book.realized`) that no one ran. RUN-1 builds D1's carry-day fixture offline and states the result. |
| 13 | The replay CLI stores `line_inputs` in `last_result` (opus) | R1:115; OC:93 | **UNPROVEN → RUN-2** | L70; hub: NOT CHECKABLE FROM READS | Read: `replay/cli.py:116` `job.result = result.job_result()` and `models.py:507`–`:508` `model_dump(mode="json")` carry the field. Nobody ran the re-render after JSON (Decimals, times). RUN-2 re-renders E6's blob after the JSON round trip and states equal or not. |
| 14 | Weak: the offline card-snapshot twin (opus, `test_drc_build.py:573`) | R1:110; OC:70 | **NOT REAL** | hub: DOES NOT HOLD for the twin (`test_drc_build.py:584`–`:585` can fail if the store held a reference) | — |
| 15 | L52 path | R1:116; OC:77; GC:60 | **NOT REAL** | both seats: NO PATH | `build.py:621` prints the stored grade on a `card:` line and computes none. |
| 16 | The build against his real template (opus, NOT CHECKABLE) | OC:92 | **OUT OF SCOPE** | L28 "writers off until proven on the dev vault with a diff"; build ESCALATE 14; `11` ESCALATE 8 | The desk's hub-run dev-vault proof after the check, carried in `08`'s `## FOR THE DEPLOY`. |

Folded, not counted separately: OC:73 ("no test covers the D3-2 stop case or the D3-6 next-day write") is closed by F-3's and F-2's reds. The seats' CHECK line items are all covered above: Opus D3-2 (3, 4), D3-4 (1), D3-6 (2), D3-1 (6a, 6b), D3-2b (5); Grok D3-4 (1), D3-6 (2).

## RECORDS
`09-28/11` `## ESCALATE` 1–9, each classed RECORD (no defect of its own):
1. Opus's line (`BUILD STANDS EXCEPT D3-2, D3-4, D3-6, D3-1, D3-2b · ready for K3: YES`) is covered by rows 1–6 above. Its `ready: YES` beside five HOLDs is Opus's field. The hub rule (`11` §4: YES only with 0 HOLDs) decides.
2. Grok's line (`BUILD STANDS EXCEPT D3-4, D3-6 · ready for K3: NO`) is covered by rows 1–2.
3. Items 1–10 are restated in rows 1–10.
4. Contradictions (D3-1, D3-2, D3-2b, the E-cells, scope, ready) were settled from the file-check column, never by vote (rows 3, 5, 6a/6b, 7, 8).
5. Packet cuts (rules.part01 −7,953 B, part06 −4,330 B, part10 −8,244 B; prior-attempt staging deviations): a record. `09` states the K17 formula and round 1's 678,318 B (R50).
6. L74 recorded by the hub; no ASK DESK; no checker wrote a stray file.
7. Astra: the fix check seats Opus 5.5 · Sol · Grok (L67 `CHECKER SEATS BY KIND OF WORK`, a fix round; K22), with no Astra seat. D3's NEW BUILD Astra read stays the desk's (R51).
8. Deploy items, carried whole into `08`'s `## FOR THE DEPLOY` and its RESTARTS:
   - RESTARTS: every resident.
   - `0019` / `0020` at migrate.
   - The `com.cobalt.prefill-drc` bootout and plist removal.
   - His daily-stop value.
   - The two config rows (`configs/cobalt/prefill.yaml` M, `configs/cobalt/templates/drc.md.j2` D) stay UNCLASSIFIED (L42), never guessed.
   - The dev-vault diff proof (build report `:266`, item 14).
   - The E7 ops read of D2.
9. Standing line: re-stated for round 2 in `08`'s CLOSE and `09`'s `## ESCALATE`.

## OWNER ITEMS
**O-1 — the fixture's seven U+00A0 bytes (L45; R40 item 5).** `tests/fixtures/drc/template_shape.md` carries U+0020 at `:5`, `:49`, `:128`, `:134`, `:156`, `:173`, `:175`, where his template carries U+00A0. The Write / Edit tools cannot write the byte, and `10`'s line (which `08` copies byte for byte) has no string that can.
- **A** — grant ONE exact byte-write string for the fix build, drafted by the desk and limited to that fixture's seven positions (for example a `perl -CSD -i -pe` with `\x{00A0}` escapes addressed by line number). The desk then re-issues `08` whole (L19) before launch, and F-6 builds both halves.
- **B** — accept U+0020 at those seven positions as the committed fixture. The U+00A0 match stays proven by `test_the_placements_match_his_no_break_spaces` (` ` escapes in the test source), and L45 is set aside for those seven bytes by his word.
- **Recommendation: A.** L45 binds, and the placements' regexes are exactly where U+00A0 matters. A byte-true fixture makes a future regex change fail a test before it reaches his notes.

## FOR DEJAN
- New strings: NONE. `08` = `10`'s line and `09` = `11`'s line, each except path + name (`comm` over the tokens: 0 other differences).
- O-1 above (A/B).

## ESCALATE
1. **The desk's reading on D3-1 / D3-2 / D3-2b (one house, UNPROVEN → RUN) is not taken for rows 3, 5 and 6a. They are classed FIX.** Reason: the hub's file-check HOLDS with `file:line` on both sides of the diff. Each mechanism is fixed by the code (a direct read; an except tuple; a committed line) and needs no runtime state. `08` makes the red the run: a CODE row not red on `a8c622ca` for its named reason is NOT built and is recorded (`08` THE FIX ROWS). This spends no extra round (L70 is met before any fix). The one-house claims that need runtime state are rows 12–13, classed UNPROVEN → RUN-1 / RUN-2.
2. **O-1 blocks nothing:** `08` builds F-6's name half. If he answers A, `08` is re-issued whole (L19) BEFORE launch; `08`'s DESK LINE (3) says so.
3. **Seat names:** `08` / `09` use `drc-d3-fix-r1-build` / `drc-d3-fix-r1-check` as `07` wrote them, with no `-0929` suffix. The launch row may add one; that is an L19 re-issue of the line.
4. **F-2's query keys on path equality.** `08` PREFLIGHT proves that the 21:10 writer and the build compose the note path identically before any edit. If they differ, the result is `FAILED: PREFLIGHT`, never a normalising transform.
5. **Not classified (not in `11`'s lists):** the build's ESCALATE 10 (v2 X12's second half vs the `card: not matched` render) and 11 (the 21:10 blob lives one night in the one-row-per-label job table). Both stay the desk's.
6. **The `09` ceiling is left to the desk as `«FILL AT LAUNCH»`** (K17 formula = the measured staged packet; round-1 precedent 678,318 B, R50).

## CONTINUE
next: none — the run is over. The desk commits the three files: this report, `prompts/2026-09-29/08-drc-d3-fix-r1-build.md` (57,092 B) and `prompts/2026-09-29/09-drc-d3-fix-r1-check.md` (46,312 B).

DRC D3 FIX R1 DRAFTED · FIX: 8 · NOT REAL: 5 · UNPROVEN: 2 · OUT OF SCOPE: 1 · OWNER ITEM: 1 · prompts: 2 · new rule strings: 0 · ESCALATE: 6
