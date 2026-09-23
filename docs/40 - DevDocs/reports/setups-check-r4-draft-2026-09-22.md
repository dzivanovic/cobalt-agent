# SETUPS CHECK R4 — drafter report (`78`, Opus 5.5, seat `setups-check-r4-draft-0922`, 2026-09-22 22:15–22:23 ET, times from `date`)

## §0 Headline
- Wrote `79-setups-check-r4.md`: check round 3 of 3, THE LAST, over `8da261a..f5aaeb4` ([R4] F1–F5 + four questions from r4's own ESCALATE). Any defect that HOLDS goes to `## FOR DEJAN` as the override question (L39). Offline only; `70`'s launch line byte for byte.
- Re-issued `13-setups-blind-values.md` in place, pointed at the r4 tip: new `R__` row, R30 date gate, a stagger against `63` / `79`, and the real day written `<real day>`. Launch line unchanged; it is never pointed at `setups-check/**`.
- NEW strings: none. ESCALATE: 6 (one `ASK DESK`: `13` is a hand seat, not code-capable).

## DIGEST FOR THE DESK
- **Launch order: `63` → `13` → `79`, one at a time, never side by side.**
  - Both use Gemini (`agy`) in the house lane (one Grok / Gemini hub at a time), and each prompt's STAGGER refuses while the other runs.
  - `13` goes first. The blind seat should answer before any house has read the five new pins in a check packet. Whether `agy` keeps anything between headless runs is NOT KNOWN.
- **`13`'s house lane use:** ONE `agy --sandbox` call (Gemini, lawful under R30 through 2026-09-23 23:59 ET). On a HARNESS or METER line it falls back once to Opus 5.5 `claude -p`, which is Anthropic and uses no house lane (recorded as "blind but same-house").
  - `17`'s precedent: `agy` headless auto-denied a command, and the Opus fallback returned 17 of 17 fields UNDERIVABLE. `13` is therefore a HAND seat, not code-capable (ESCALATE 1).
- **`79`:** three houses (Grok · Gemini · Opus 5.5). Sol is METER until 09-26 06:47, probed and skipped. Packet ≈ 95 KB ≈ 24k tokens per house, ceiling 150,000 B.
- **Launch rows the desk writes** (`R__` in both files; each row must also carry the stagger literals below if the other report is absent):
  - `13`: names `13-setups-blind-values.md` + `f5aaeb4`, plus `63 is not running` / `79 is not running`.
  - `79`: names `79-setups-check-r4.md`, plus `63 is not running` / `13 is not running`.
- **Gates `79` greps (all committed now):** R118, R125, the r2r3 check, the r4 classification, R30, R32.
- **Window:** R30 for both runs, through 2026-09-23 23:59 ET (S2 stops 09-23). `63` runs first (R125: "The r4 check waits for `63`'s stop line").
- **After both runs:** the with-DB set after `68` (`77` is re-issuing it), then the deploy prompt carrying R119's three Assumed-Defaults rows.

## RULE PROOF
Each span below runs from `--model` to the last `--add-dir`, quotes included, one `grep -c -F -e` call each.

| check | file | count |
|---|---|---|
| `70`'s span, rc `setups-check-r2r3-0922`, 15 allow + 3 deny + triplet | `70-setups-check-r2r3.md` | 1 |
| the same span with rc `setups-check-r4-0922` | `79-setups-check-r4.md` | 1 |
| `cd …/agy-trial` + `claude --bg "Read '…/79-setups-check-r4.md' …" --model claude-sonnet-5` | `79` | 1 |
| `13`'s span, rc `setups-blind-values-0922`, 9 allow + 3 deny + triplet, BEFORE the re-issue (= `HEAD`; `git status` clean for it, last commit `b8a72b5`) | `13` (HEAD) | 1 |
| the same span AFTER the re-issue | `13` (new) | 1 |
| `cd …/agy-trial` + `claude --bg "Read '…/13-setups-blind-values.md' …" --model claude-sonnet-5` | `13` (new) | 1 |
| L32 self-check: the ticker, the real day, the new pin values and `setups-check/r4/` | `13` (new) | 0 |

- **`79` vs `70`:** only the prompt path and the remote-control name differ. Mode `auto`, cwd `agy-trial`, as in `70`.
- **`13` vs `HEAD`:** the launch line is byte-identical. What changed in the prose:
  - the launch row: R24 → `R__`, and the gate now requires `f5aaeb4`;
  - the Gemini date gate: R39 (expired 09-22 23:59) → R30;
  - PREFLIGHT gains the r4 tip + the proof that the fixture is the tip's, and the stagger against `63` / `79`;
  - it reads the r4 report's last line and `## NOTE FOR THE DESK` only;
  - `setups-check/**` is added to the NEVER list;
  - the stale constant line numbers are not used;
  - the `_ANCHOR` constant is read over its continuation lines;
  - the anchor is compared on object, direction and bar timestamp;
  - the real day is written `<real day>`.

## NEW strings:
None.

## L74
Recorded once: a system-reminder appended after this session's first tool result asked for a `Claude-Session:` commit line and named a file-send tool. It is data and was not followed (this seat commits nothing).

## ESCALATE
1. **`13` is a HAND seat, not code-capable.**
   - As written, both of its houses read only. Gemini `agy` headless auto-denies commands (`17`: `jetski: no output produced — a tool required the "command" permission …`). The Opus fallback is limited to Read / Grep / Glob.
   - `17`'s precedent is UNDERIVABLE 17/17. R24 itself named "the code seat `23`'s shape" as the fallback.
   - `23`'s Grok run rule was approved "today, under R39" (09-22 only), and its Sol fallback is available from Sat 09-26. A code-capable re-point of `23` needs his word extending the Grok run rule.
   - `ASK DESK: launch 13 as a hand seat (expect UNDERIVABLE), or bring 23's Grok run-rule extension to him? [22:23]` — safe default: `13` as re-issued.
2. **`13` first issue, an L32 leak, fixed in the re-issue.** Its PREFLIGHT row quoted the cut report's last line "verbatim". That line carries `days: rubberband=<real day>`, so the committed report would have carried the real day. The re-issue writes `<real day>`. This is a drafter change beyond the re-point.
3. **`79` drafter choices, each strikable by a re-issue; none is a rule string.**
   - Packet shape: the BEFORE and AFTER bars excerpts, the cutter and the cut test whole, and the raise-site excerpts for F1 / Q1.
   - Ceiling 150,000 B (was 230,000 in `70`).
   - The end-line word `DEFECT REMAINS` replaces `FIX AGAIN`, because no fix round follows.
   - His R119 row is NOT staged, because it quotes proposal values.
4. **Questions (4):** Q1–Q4 come from r4's ESCALATE (i), (ii), (iii-a) and (iv-b), each touching a FIX row. r4 (v) is asked inside F5. (vi) `_cut_p2_fixtures.py` touches no FIX row, so it is NOT asked (the safe default of `71`'s ESC 2 is kept) and is a standing line for the desk's plate.
5. **With-DB OWED for rounds 2–4.** `68` has not landed (R125: FAILED Q3; `77` is re-issuing it). `79` is offline, and its standing line names the owed set.
6. The r4 fix report's `## C3` and `## §0` quote the stored day's ticker and the new pin values. `79` stages `## C3` for F5 (this is a check packet). `13` never opens those sections before its house answers.

## CONTINUE
next: none. `79`, `13` (re-issued) and this report are written. The desk commits all three, fills `R__` in `79` and `13`, and launches `13` then `79` after `63`'s stop line.

SETUPS CHECK R4 DRAFTED · range: 8da261a..f5aaeb4 · questions: 4 · 13 re-issued: yes · new rule strings: 0 · ESCALATE: 6
