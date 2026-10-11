## §0 Headline
- Drafted the F5 tribunal triple in `prompts/2026-10-11/`: `325a-f5-tribunal.md` (hub, 65,209 B), `325b-f5-tribunal-opus-seat.md` (21,648 B), `325c-f5-tribunal-derive.md` (27,022 B), each a minimal edit of `237` / `238` / `239` with `258`'s stagger gate.
- Seats: Grok plus the blind Opus seat; Gemini only on the desk row's reason (R921); Astra `NOT SEATED (R920)`, no `codex` string anywhere in a launch line.
- Packet: F5 proposal, seam doc, F4-FINAL `## SEAM` and `## CHUNKS`, the Charter and ladder lines, code ranges at `d0a5fbb8`, 24 laws; question set re-pointed to 19 items (D1–D12, S1, a–f).
- Every allow and deny string counts ≥1 in its precedent (36 of 36). Nothing is run, committed or launched.

## DECISIONS
- ASK DESK: the floor. R860's "proposer plus two outside houses" cannot be met by Grok alone once R920 removes Astra and R921 makes Gemini conditional. Default written into the hub and derive: floor = Grok ruled AND the Opus seat's stop line present; Gemini counts when it sat; Grok not up or not ruled → `FAILED` floor. [2026-10-11, desk]
- ASK DESK: packet scope. The task says "F5 design and the LAWS it touches"; I also staged F4-FINAL's header, `## SEAM`, `## CHUNKS` (part 15) because it contradicts the proposal on module home and config home (`prefill/checkpoints.py` and a `checkpoints:` block against a `checkpoint/` package and `checkpoints.yaml`; item S1 asks it), plus code excerpts as in 237. Default: kept. Drop part 15 and the code parts if you want the packet to be design plus laws only. [2026-10-11, desk]
- ASK DESK: the question set is new text, not an edit. 237's 21 items are F4's; I wrote D1–D12 from the proposal's `## 5`, one seam item S1 and (a)–(f) re-aimed at F5 (number guard, write walk, L1/L9/L22–L25/L52/L53/L57, chunks, restarts). Default: kept; it needs your read before launch. [2026-10-11, desk]
- ASK DESK: Gemini's launch literal. The hub reads `gemini: sits` with a reason (money, sizing, vault note, load-bearing split) or `gemini: not seated`. F5 has a money-adjacent value (`checkpoint.grace_min`, the Finviz request count) but I decided nothing. Default: `gemini: not seated` unless the desk row says otherwise. [2026-10-11, desk]
- The prompts keep the precedents' background text; writing-rules.md says a prompt is tags, launch line, card, steps. Default: kept, because the task said minimal edit of the precedents.

## RECORDS
Reads:
- `prompts/2026-10-11/325-draft-f5-tribunal.md:1-6` (the task).
- `prompts/2026-10-10/224-draft-f5-design.md:6` REPORT line, then `reports/f5-design-2026-10-10.md:1-54` whole; `reports/f5-design-proposal-2026-10-10.md:1-134` whole (15,465 B).
- `prompts/2026-10-10/237-f4-tribunal.md:1-66` whole, `238-f4-tribunal-opus-seat.md:1-27`, `239-f4-tribunal-derive.md:1-37`, `262-draft-f4-tribunal-r2-stagger.md:1-10`, `258-f4-tribunal-r2.md:1-13` (current stagger gate, `:9`).
- `reports/f4-f5-seam-2026-10-10.md:1-52` (4,503 B); `docs/30 - Design/F4-FINAL-2026-10-10.md:226-295` and the heading list (`## SEAM` at :226, `## CHUNKS` at :293).
- Desk rows by grep: `cto-2026-10-10.md:81` R931, `:91` R921, `:92` R920, `:104` R908; `cto-2026-10-11.md:11` R1012, `:9` R1014. The literals I put in the hub's greps (`tribunals Grok+Opus seat`, `only the model tribunal uses OpenAI`, `several Grok sessions may run at the same time`, `S5 tribunals F5 F20 F21 F23 run NOW`) are from those lines. R849, R860, R109, R95, R97, R17, R19 literals are copied from 237 / 238 and not re-read.
- `topics/writing-rules.md:1-27`; LAWS.md heading index (`### L1` … `### L80`) by grep.

Counts proved (`grep -c -F`, each its own call, each printed 1):
- Hub: 13 allow strings (grok, agy, mkdir, cobalt show, cobalt log, three `s2-p2-cards` strings, ls, grep, tail, wc, date) and 3 denies against `258-f4-tribunal-r2.md` (16 of 16). The `codex exec` string is dropped.
- Opus seat: 7 allow and 3 denies against `238` (10 of 10). Derive: 7 and 3 against `239` (10 of 10).
- Leftover `astra`, `codex`, `f4-tribunal` hits in the new files (13 matches by grep) are the intended ones: the precedent paths, `astra: NOT SEATED (R920)`, and the refusal on a `codex exec` string.

Sizes: hub 65,209 B, Opus seat 21,648 B, derive 27,022 B (`wc -c`). Packet size is the hub's to measure; the hub states a derived bound (mandatory ≤ ≈110 KB, whole ≤ ≈150 KB, ceiling 200,000 B), derived from the F4 packet's file sizes, not measured. I recorded sizes only for the three reports I measured; the code files carry no drafting size.

Not checked: that the code line numbers in the packet's excerpt list (from the F5 report's RECORDS) still hold at `d0a5fbb8`; the hub checks each anchor with `grep -n`. No desk launch row for `325a` exists yet; the hub verifies it.

F5 TRIBUNAL DRAFTED · prompts: 3 · decisions: 4
