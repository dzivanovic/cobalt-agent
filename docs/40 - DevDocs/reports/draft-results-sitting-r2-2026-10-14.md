# Draft results sitting round 2 (Grok row) — 2026-10-14

## §0 Headline
- Drafted hub `prompts/2026-10-14/532-results-sitting-r2.md` (25,933 B) and blind seat `533-results-sitting-r2-opus-seat.md` (8,500 B). There are five cells: C1 378 and C2 365 (LOW), C3 368 and C4 379 (MID), C5 371 (HIGH).
- Grok rules on all five cells, but each one is its own vendor's, so all five rulings are recorded apart. The counted pair on every cell is Astra and the Opus seat, and both are needed (the floor).
- The per-band lines use 427's lookup, with n stated (2/2/1) and "insufficient data" on each line. The X1 decline is stated and not scored. The hub writes no routing table; the desk writes it afterwards.
- Packet: 13 parts, each ≤ 38,000 B (the largest is `18-baseline` at ≈ 28 KB). The total is ≈ 140 KB, a bound from file sizes; the ceiling is 200,000 B, with a cut order.
- Blocker: the 365, 379 and 371 Grok check reports are not committed yet, so the hub refuses until the desk commits them.

## DECISIONS
- ASK DESK: the Grok checks for 365, 379 and 371 are uncommitted (`git log -1` is empty for each), while 378 is at `ed8587ab` and 368 at `18fbb7d5`. The hub refuses inputs that are not committed. [06:45 EDT] Default: the desk commits the three reports before the launch row.
- ASK DESK: the launch row needs the new literal `grok read: ruled R1315`. It replaces 427's `grok read: open`, which made 427 refuse once his ruling had landed. `Fable seat: yes`, `grok runs: <n> of 3` and `openai seat: …` stay as in 427. [06:45 EDT] Default: the desk writes all four literals.
- ASK DESK: R1315 lists 378, 368, 371 and 379 as scored but does not name 365. 365 was rebuilt after R1315, and R1319 ("check … 365 … scored", "n=2/2/1") counts it. [06:45 EDT] Default: 365 is graded as C2 under R1315 and R1319.
- ASK DESK: no committed baseline exists for archiver-429 (C1) or worktree-salvage (C4). SHADOW-HUB :76 gives 1/2/2 only for the three bake-off cards, and both originals' `CHECK DONE` lines print `held:` without the opus-own split. [06:45 EDT] Default: each counted house derives the original's opus-own count with its steps; the hub file-checks it, and if the two houses differ, that goes to ESCALATE.
- ASK DESK: the results table's Grok row (`complexity-shadow-results-2026-10-11.md` :17) predates R1315 and the 10-13 rebuilds: it still shows 365, 371 and 379 INCOMPLETE and 378, 368 UNSCORED. [06:45 EDT] Default: stage the table as it is, with a header line saying the check reports govern C1–C5; no refill before the sitting, and UNKNOWN cells stay UNKNOWN.
- ASK DESK: L8 renders "insufficient data" for any n<30, which covers n=2 as well as the n=1 your card named. [06:45 EDT] Default: every band line reads "insufficient data (n=<n> per band)", per L8.
- ASK DESK: Grok counts on no cell. If Grok is not up, should the sitting run without its separate ruling? If Astra is not up, should it run with every cell ONE HOUSE? [06:45 EDT] Default: in either case launch nothing and the desk waits (427's floor rule).

## RECORDS
Proven from the files:
- Launch commands are copied, not invented. 532's `--allowedTools`/`--disallowedTools`/`--add-dir` segment matches 427's line (`grep -c -F` = 1 on each file). 533's matches 428's (= 1 on each). The house spellings come from 427 `## 2`: `grok -m grok-4.7 --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)" -p "<sentence>"` and `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "<sentence>" < /dev/null`. 427 ran both on 10-12 (`results-sitting-2026-10-12.md` Clock :71). The desk lines are `sh /Users/cobalt/.claude/ops/desk-launch.sh prompt "<532|533 path>"`.
- The following are reused from 427 by reference ("as 427"): the rules, the packet reading order (`00`), the stagger rule (R908, `grok runs`/`openai seat`), the REDACTION pointer (`73` §1 through 427/270), the excerpt ranges, the astra capture, the collate lookup, Independence and L74.
- The derive step is the same as in 427: none. The per-band lines are filled by lookup, and an OPEN cell goes to him as an A/B.
- Packet parts (bytes measured over the excerpt ranges, header lines excluded):
  - 10 table: 8,442
  - 11 stage answer: 4,505
  - 12 SHADOW-HUB :37-38, :72-103: ≈ 3.8 KB (427 measured 3,792)
  - 13 LOW: 378 8,781 + 365 4,102 + 2 stop lines ≈ 14.5 KB
  - 14 MID: 368 4,689 + 379 3,747 + stops ≈ 9.8 KB
  - 15 HIGH: 371 8,045 + stop ≈ 8.7 KB
  - 18 baseline: round-1 three 17,401 + archiver original 5,327 + worktree original 3,931 + stops ≈ 28 KB
  - 19 rulings: ≈ 4 KB
  - 20 round-1 excerpt: ≈ 4 KB
  - 27 laws: ≈ 13.5 KB (427: 13,531)
  - 00/01/02: ≈ 33 KB (427's 02 was 28,307)
- Stop line of counts: `RESULTS SITTING R2 DONE · grok: … (apart: C1 C2 C3 C4 C5) · astra: … · opus: … · cells closed: <n> of 5 · open · one house · claims that HOLD · owner items · ESCALATE`. Seat: `RESULTS SITTING R2 OPUS DONE · <SITTING> · apart: none · withdrawn · ESCALATE`.
- Input facts:
  - Grok check stop lines, opus-own held: 378 1, 365 2, 368 0 (house 1, grok-own 1), 379 3, 371 4 (house 2, grok-own 2).
  - Original baseline: 365/368/371 1/2/2 (stage answer §3). The archiver original has `held: 5` (:258) and the worktree original `held: 4` (:213), neither split.
  - Build stop lines: 371 `passes: 3 · suites at first run: red`. Its build §0 :5 says one red test, green after one re-pass. The other four are `green`.
- Where 532/533 differ from 427/428, and why:
  - The cells are the five Grok builds, not Sonnet and Terra: round 2 grades the Grok row (R1319, R1350, R1468).
  - Grok is recorded apart on all five cells, and the counted pair is Astra plus the Opus seat everywhere: every cell is Grok's own vendor's (stage answer §3).
  - The floor drops Grok and is now Astra plus the Opus seat; the Opus seat's grades all count, so it has no apart cells.
  - Authorization adds R1315, R1319, R1350, R1452 and R1468. The launch row literal is `grok read: ruled R1315`, where 427 refused on `ruled`, because his word is in.
  - NO NEW RULE is proven against 427 and 428, the lines that ran, not against 270 and 271.
  - Two baselines are derived by the houses (C1, C4), because SHADOW-HUB gives none for those cards.
  - The per-band lines print two cards per band side by side and are never merged, so no new merge rule is invented. n is stated per band (2/2/1).
  - The hub writes no routing table; the desk writes it from the confirmed grades (card 531).
  - X1 is stated and never scored (R1451, R1452).
  - Part `20-round1` stages round 1's closed cells as context, for the same cards' Sonnet and Terra arms.
  - The folder is `results-sitting/r2/`; the reports are `results-sitting-r2-2026-10-14.md` and `results-sitting-r2-opus-2026-10-14.md`.
- Files read:
  - `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/531-draft-results-sitting-r2.md`
  - `/Users/cobalt/Vault/Think/6 - Permanent/Memory/areas/cobalt.md`; `/Users/cobalt/Vault/Think/6 - Permanent/Memory/topics/writing-rules.md`; `LAWS.md` L8 (`grep -A4`)
  - `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/427-results-sitting-tribunal.md`, `428-results-sitting-opus-seat.md` (whole)
  - `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/draft-results-sitting-2026-10-12.md`, `results-sitting-2026-10-12.md` (whole)
  - `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/complexity-shadow-results-2026-10-11.md`, `bakeoff-results-stage-answer-2026-10-11.md` (whole)
  - `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md` :30-109
  - The five Grok checks `reports/*-grok-check-2026-10-11.md`: headings, `## §0`, last line
  - Originals `reports/archiver-429-check-2026-10-10.md` and `reports/worktree-salvage-check-2026-10-07.md`: headings, §0, `## Findings`, CHECK DONE
  - Grok build stop lines under `/Users/cobalt/cobalt-wt/<job>/docs/40 - DevDocs/reports/`, and the `s4-p1-1009-grok` build report's headings and red lines
  - Card headers `prompts/2026-10-11/378-…`, `379-…` (TIP, SHADOW OF)
  - Rows R1274 (`cto-2026-10-12.md`); R1315, R1317, R1319, R1350, R1436–R1439, R1451, R1452, R1458, R1459, OWED :173, :199 (`cto-2026-10-13.md`); R1467, R1468, OWED :17 (`cto-2026-10-14.md`)
  - `git log -1` of the five Grok checks, two originals, rows R1315/R1319/R1350/R1452 and both round-1 reports.

DRAFTED · decisions: 7
