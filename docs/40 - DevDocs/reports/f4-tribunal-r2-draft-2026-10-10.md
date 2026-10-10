# F4 round-2 tribunal prompts — drafter `f4-tribunal-r2-draft` (Sonnet 5.5), 2026-10-10

## §0 Headline
- Wrote the three round-2 prompts: `258` hub, `259` blind Opus seat, `260` derive. Shape is round 1's, narrowed to `R2-1`…`R2-7`.
- New rule strings: none. All 17 hub strings and the 10 seat and derive strings occur once each in the new files, identical to round 1's.
- 6 decisions, each at its default; none waits for him. Nothing was committed or launched.

## CHANGES
All three files are new, under `docs/40 - DevDocs/prompts/2026-10-10/`.
- `258-f4-tribunal-r2.md` (63,496 B):
  - Same launch line as 237 except the prompt path and remote-control name (`f4-tribunal-r2-1010`).
  - Authorization greps are re-pointed: R876 and R903 added, round 1 shown done and committed, and the three round-2 prompts shown committed.
  - The stop line is `F4 TRIBUNAL R2 DONE`, the packet folder is `.../f4-tribunal/r2/`, and the report is `reports/f4-tribunal-r2-2026-10-10.md`.
  - The packet is the DRAFT FINAL whole, the derive's `## NEEDS ROUND 2` and `## FOR DEJAN`, and the round-1 hub rows for the seven items by `F`/`FC` number.
  - It also carries the Opus seat's round-1 rulings on the seven items, the Charter, and pre-cut code excerpts at `d0a5fbb8`.
  - `01-QUESTIONS.md` asks only R2-1…R2-7. Each has A and B quoted verbatim from the derive report, plus its question. The R2-4 REJECT text comes whole from the FINAL's `## Dissents, verbatim`.
  - Verdict words are `ADOPT A · ADOPT B · ADOPT WITH · REJECT`. Unrunnable facts become `X<n>`. Closing line: `TRIBUNAL R2: …`.
  - The houses are barred from the round-1 folder. Astra prints `ITEM R2-n` as it rules, and its partial count is `k of 7`.
  - Collate step: rulings table, verbatim wordings, file-check, then the Opus seat's FCs numbered from `FC27`.
- `259-f4-tribunal-r2-opus-seat.md`:
  - Blind to the r1 and r2 scratch folders and to the hub's r2 report. It reads committed round-1 reports only.
  - Its own round-1 wording on three of the seven positions is stated as a conflict of interest. No SELF lines (no seat is assigned).
  - Report: `reports/f4-tribunal-r2-opus-2026-10-10.md`. Stop line: `F4 TRIBUNAL R2 OPUS DONE · … · adopt A · adopt B · adopt with wording · reject · ESCALATE`, summing to 7.
- `260-f4-tribunal-r2-derive.md`:
  - Refuses unless the round-2 stop lines and the round-1 chain are committed, a `ROUND 2 OWED` marker is still present, and the floor is met.
  - An item closes only on a verbatim A, B or ADOPT WITH. It stays OPEN on a disagreement about correctness, a REJECT whose claim holds, or an unfilled gap. It never settles by vote (L37).
  - It rewrites `docs/30 - Design/F4-FINAL-2026-10-10.md` in place. Round-2 tags continue from `[F-26]`. The header reads `FINAL` or `FINAL WITH OPEN ITEMS (<ids>)`.
  - `## FOR DEJAN` carries one A/B per open item, in his terms and with no recommendation, then one approval.
  - Stop line: `F4 DERIVED R2 · …`.

## DECISIONS
Each is taken at its default. None is a rule string.
1. **Session and remote-control names are new** (`f4-tribunal-r2-1010`, `f4-tribunal-r2-opus-1010`, `f4-tribunal-r2-derive-1010`). Round 1 changed the same two things versus its parent prompts. Default: carried. Need for his word (R411): only if the deployed guard admits a seat or derive file by a name shape other than `…-tribunal-r2-opus-seat.md` / `…-tribunal-r2-derive.md`. The desk can check this before launch.
2. **The derive overwrites `F4-FINAL-2026-10-10.md` in place**, as 257 says. The DRAFT FINAL stays in git history. Default: carried. If the guard allows only new-file writes for the derive, the desk would need his word on a `-R2` file name.
3. **`## FOR DEJAN` carries an A/B for open items**, as 257 asks. L67 as amended says a design question a house can settle is not an owner item. The derive therefore keeps `## OWNER ITEMS` at `none` unless the owner test passes, and names the A/B as L39's carried split, with a third round as the alternative. Default: carried. This is not a string. It is a law tension for the desk.
4. **The round-2 packet adds one writer range** (`writer.py:588-669`, `create_if_absent` and `_seed_baselines`). Round 1 cut it and two houses flagged the gap (F25). It also adds `jobs/wrapper.py:125-199`, `daymode/note.py:238-256`, `aset/daily_note.py` and `radar/notes.py:270-395`, the files the seven items cite. Whole packet ≤ ≈ 230 KB at the derived bound, so the cut order (laws, consumers, experiments table, `daily.py` to ranges) probably applies; the hub measures. Default: carried.
5. **L8 is staged this round** (round 1 left it out, F12), along with L9 for the C7 question. Default: carried.
6. **A and B per item follow the derive's quotes.** R2-1 has four positions (Grok, Astra, Gemini's disk-built rule, the seat's baseline-built plus lock). The houses reach the seat's through `ADOPT WITH`. R2-7's B is the folded C8 text, because the derive names no house wording for stubs. Default: carried.

Strings needing his word (R411): none.

## RECORDS
**RULE PROOF.** Each carried rule string occurs once on the launch line of its round-1 prompt:
- Against `237` (hub): each of the 14 allow and 3 deny strings printed `grep -c -F` = 1 (17 calls).
- Against `238` (seat) and `239` (derive): each of the 7 allow and 3 deny strings printed once under `grep -o -F` (10 lines each).
- Against `258`: the same `grep -o -F` over all 17 strings printed 17 lines, one per string, in the same order.
- Against `259` and `260`: the same over the 10 strings printed 10 lines each, one per string.
- `grep -c -x -F "FABLE ROW: R__"` on `259` = 0, and `grep -c -x -F "DERIVE ROW: R__"` on `260` = 0. Both rows are filled (R109).
- NEW strings: none.

**Launch-row facts the prompts rely on** (read from `cto-2026-10-10.md`):
- R849, R860, R876 (carries `237-f4-tribunal.md`) and R903 (`7 items need round 2`) exist.
- R903 names the drafter `257`, prompts 258–260.

**File sizes.** Measured with `wc -c`:
- `258` 63,496 B (its line 1 was not touched by the later packet-ceiling edit, so the rule proof stands); `259` 20,448 B; `260` 26,805 B.
- Whole-file sizes I read at drafting (the hub measures the staged copies):
  - FINAL 48,835 (needs 2 parts)
  - round-1 hub report 54,580, of which only the named rows are staged
  - Opus r1 report 31,545, of which only the named blocks
  - derive report 18,900, of which two sections.
- The packet sum is derived, not measured: ≈ 195 KB MANDATORY and ≈ 230 KB whole. That bound is above the 200,000 B ceiling, so `258` carries a cut order, and a packet still over the ceiling is staged and listed under ESCALATE.

F4 R2 PROMPTS DRAFTED · prompts: 3 · new rule strings: 0 · decisions: 6
