# R2R3 check drafted (70), 2026-09-22

## §0 Headline
- Wrote `prompts/2026-09-22/70-setups-check-r2r3.md`, unlaunched. It re-issues `67` widened to `60ddac4..be44eb4` in three tagged sub-ranges: [R2] `60ddac4..826d284`, [CUT] `74eefd8..65c08a0`, [R3] `65c08a0..be44eb4`. It has 22 answer blocks.
- The launch line is byte-identical to `67`'s apart from the path and `setups-check-r2r3-0922`. No new rule strings.
- The packet is ≈215 KB, over the desk's 150 KB target, because the three diffs alone are ≈120 KB. ESCALATE (a).
- ESCALATE: 7, including 3 ASK DESK. Seat `r3-check-widen-0922`, 20:06–20:1x ET (`date`). Everything was read-only, and I wrote only these two files.

## DIGEST FOR THE DESK
- **Round count:** this is the SECOND house check (round 1 = `66`). `16` and `67` are not counted (L67 P-c). If a defect HOLDS, ONE more fix round is lawful. Its drafter classifies first (L75), and its check is round 3, the last.
- **Questions:**
  - FIRST covers 15 tagged rows: [R2] F1–F5 + P1 (16's "look hardest"), [CUT] C1–C3, and [R3] F1–F6 (67's text).
  - C1 asks whether the fixture is real-shape (L45). C2 asks whether any value of his entered (R24). C3 asks whether the cut reproduces the stored day's formations.
  - SECOND is the proposal keys + grades. THIRD is Q1 (r2 ESC (viii)) and Q2 (r3 ESC (v)).
  - FOURTH is the not-fixed rows. FIFTH is (a), (b), (c) per tag.
- **Boundary:** the union of `15`'s CLOSE, `12`'s STEP-6 list and `33`'s CLOSE, plus r3 ESC (ix)/(x). The protected-path checks are split per round, because r3 legitimately touches `configs` / `cards` / `taxonomy` and the cut legitimately touches `tests/fixtures`.
- **Packet (estimates):**

  | files | size |
  |---|---|
  | `fix-diff-r2` | 41.6 KB |
  | `cut-diff` (bars JSON excluded) | ≈17 KB |
  | `cut-bars-excerpt` (first 40 / last 20 lines of the committed blob + `grep -c` counts) | ≈2 KB |
  | `fix-diff-r3` | 61.5 KB |
  | ADDING-A-SETUP at the tip | 9.4 KB |
  | report sections (r2 ESC; cut FIND/CUT/PIN/ESC; r3 PROPOSAL/DIALS/ESC) | ≈40 KB |
  | `classify`, `rows`, `QUESTIONS`, `proposal-keys` | ≈45 KB |

  That is ≈54k tokens per house. The hub ceiling is 230,000 B.
- **Gates added** (all three verified read-only just now):
  - R23 must carry `12-setups-fixture-cut.md`.
  - The `14-…` and `12-…` desk calls must be committed. `12`'s is `d86b973`.
  - R112 must carry `60ddac4..be44eb4`. R112 is committed (`e91c39a`).
- **The launch row is `R__`.** The gate greps `^| R__ ` so that R112 (which already names `70-…`) can never satisfy it. The row must name `70-setups-check-r2r3.md`, plus `59 is not running` / `63 is not running` if their reports are absent.
- **A fact I read (L35), not a verdict:** the stored-day replay printed `BTTC rubberband FORMED short trigger 0.6690 stop 0.87 (formation bar 10:24 ET)` (cut report `:57`). The pin on the cut is long, formed bar `15:34 UTC`, trigger `0.8400`. The cut report's ESC (i) gives the reason: the replay evaluates the production-synced def, and the pin evaluates the neutral shape. C3 asks the houses about this.

## RULE PROOF
Each check was one `grep -c -F -e "<span>"` call.

| check | file | count |
|---|---|---|
| `67`'s span `--model claude-sonnet-5 … --remote-control setups-check-r3-0922 --allowedTools …15… --disallowedTools …3… --add-dir …3…` | `67-setups-check-r3.md` | 1 |
| the SAME span with only `setups-check-r3-0922` → `setups-check-r2r3-0922` | `70-setups-check-r2r3.md` | 1 |
| `` `cd /Users/cobalt/cobalt-wt/agy-trial` then `claude --bg "Read '…/70-setups-check-r2r3.md' and follow it exactly." --model claude-sonnet-5 … setups-check-r2r3-0922`` | `70` | 1 |

The only differences between the two launch lines are the prompt path and the remote-control name, as expected. The date gate (R30), OFFLINE ONLY, L32 staging and the four seats are carried unchanged.

## NEW strings:
none (0).

## ESCALATE
(a) **The packet is over the 150 KB target.**
- The three diffs alone are ≈120 KB, measured by tool output: r2 41.6 KB, r3 61.5 KB, and the cut ≈17 KB without the 191 KB bars file.
- The minimum that keeps every question answerable is ≈215 KB.
- Dropping `classify.md`, `## DIALS`, the report sections and the how-to would reach ≈150 KB. But then FOURTH, F6, Q1, Q2 and the doc rows become NOT CHECKABLE.
- `ASK DESK: accept ≈215 KB (ceiling 230,000 B), or trim to ≈150 KB and lose FOURTH/F6/Q1/Q2/doc rows? [20:16]`. Safe default as drafted: ≈215 KB.

(b) **The r2 fix touched `tests/cobalt/test_radar_anatomy.py`, which is outside `15`'s CLOSE list.**
- The r2 report names it in its ESC (vii) (two A1 re-points).
- The desk's union rule does not include it, so the hub's check (i) will record it as outside the boundary, with (vii) quoted.
- `ASK DESK: allow it the way r3 ESC (ix)/(x) files are allowed? [20:16]`. Safe default: not added.

(c) **HOLD 1's closure has never been checked by a house.**
- This was `16`'s SECOND question: `17`'s comparison of the committed-day pins. The desk's question set leaves it out.
- `ASK DESK: add 16's HOLD 1 question? [20:16]`. Safe default: not asked, recorded as a standing line.

(d) **The real day and ticker appear in committed files.**
- The CUT commit message and the `test_setups_fixture_cut.py` docstring name the real day `2026-09-21`, and the commit message also names the ticker.
- `12`'s leak proof covered only `tests/fixtures/radar/`.
- `70` adds hub check (viii). It records the line and does not judge it. C1 asks the houses.

(e) **`70`'s packet carries the five new cut pins.** `13` (their blind re-derivation) has not run. `70` adds a standing line: `13`'s seat must never be pointed at this folder, and `13` is owed before the deploy prompt.

(f) **Drafter deviations beyond the listed changes.** The desk accepts or strikes each one:
- the launch-row gate is keyed on `| R__ |`;
- three gates were added (R23, the committed `14`/`12` calls, R112);
- the packet is cut by section rather than whole reports; round-1 verdicts, `17`'s comparison and the DevDoc diffs were dropped; a bars excerpt was added;
- the CLOSED standard now reads RED-on-base from the diff's `-` lines, because the `### T` sections are not staged;
- `## FOR THE CLASSIFIER` (L75) is split from `## FOR DEJAN` (Q1, Q2 only);
- the check line is `CHECK R2R3: … FIX AGAIN` (`16`'s shape);
- the [CUT] base for file-reads is `74eefd8`.

(g) **Stagger.** `59` and `63` do not name `70`. The desk holds them while `70` runs, as R111 did for `67`.

## CONTINUE
next: none. `70` and this report are written. The desk rules on (a)–(c), fills `R__`, commits, and launches.

R2R3 CHECK DRAFTED · range: 60ddac4..be44eb4 · questions: 22 · packet: 215 KB · new rule strings: 0 · ESCALATE: 7
