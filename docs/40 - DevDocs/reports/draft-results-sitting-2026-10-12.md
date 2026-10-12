# Draft results sitting — 2026-10-12

## §0 Headline
- Drafted hub `prompts/2026-10-12/427-results-sitting.md` (30,377 B) and blind seat `428-results-sitting-opus-seat.md` (9,211 B). One round; houses Grok, Astra and the blind Opus seat; no derive seat.
- Six cells (Sonnet and Terra × LOW/MID/HIGH). Each cell has two counted houses: Grok + Astra on Sonnet, Grok + the Opus seat on Terra. Self-vendor rulings are recorded apart. Grok's 378 and 368 are not cells (UNSCORED), and UNKNOWN cells stay UNKNOWN.
- The per-band lines (SHADOW-HUB :90-93) come from a fixed lookup: both counted houses agree → CLOSED → CAN BUILD / WITH A REVIEW / NOT YET; otherwise OPEN, which goes to him as an A/B. Every line carries "insufficient data (n=1 per band)" and states it is not a routing rule.
- The packet has 13 parts, each ≤ 38,000 B (the largest is 16-checks-HIGH-terra, ≈ 26 KB). Derived bound ≈ 136 KB: an upper bound from file sizes, not a measurement. Ceiling 200,000 B, with a cut order.
- Differences from 270 are listed under RECORDS.

## DECISIONS
- ASK DESK: launch 427 + 428 now, or after card 417 as R1253 says? The sitting uses no DB and no lock, so the only shared resources are the OpenAI seat and the Grok count. [15:49 ET] Default: after card 417, per R1253.
- ASK DESK: I wrote no derive seat (no 272 equivalent). The hub fills the per-band lines by lookup, and an OPEN cell goes to him as an A/B, so there is no round 2. If you want a derive seat, a file 429 is owed. [15:49 ET] Default: no derive.
- ASK DESK: the hub is Sonnet 5.5, as in 270, and this sitting grades Sonnet. The hub only counts and looks up; it gives no verdict (L37). Keep Sonnet, or put the hub on Opus 5.5 (one token in the launch line)? [15:49 ET] Default: keep Sonnet, as 270.
- ASK DESK: the launch row needs two new desk literals, `Fable seat: yes` (271's spelling, kept) and `grok read: open`. The second one makes the hub refuse if his grok-read word lands before launch, because 427 would then need re-issuing with the Grok cells. [15:49 ET] Default: the desk writes both literals in the launch row.
- ASK DESK: if Astra is out of meter, C1–C3 would rest on Grok alone. The hub stops `FAILED PREFLIGHT: astra not up` instead of running with one house. [15:49 ET] Default: launch nothing, the desk waits for the meter's return time.

## RECORDS
Proven from the files:
- Launch commands, copied without change. Grok: `grok -m grok-4.7 --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)" -p "<sentence>"`. This spelling is identical in 270 :34 and in the newest hubs that ran Grok (335/336/337/338, 2026-10-11, all `DONE`). Astra: `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "<sentence>" < /dev/null`. The newest hub that ran Astra is 270 (`model-tribunal-2026-10-10.md` stop line `astra: TRIBUNAL R1: ADOPT AFTER …`). 278 and 335–338 have `astra: NOT SEATED`.
- 427's allow line is 270's 14 strings minus `Bash(agy *)` (13 strings), with the 3 denies unchanged; nothing added. I proved the astra and mkdir strings in 270 (`grep -c -F` = 1). The hub re-proves all 16 at AUTHORIZATION. 428's line is 271's 7 strings and 3 denies, unchanged.
- The redaction paragraph points at `prompts/2026-09-21/73-s3-exits-tribunal.md` §1 (REDACTION at :14), through 270 §1. It is not copied (L32).
- Packet parts and sizes (bytes ÷ lines from `wc -c`/`wc -l`, ranges from `grep -n "^## "`): 10 table 8,442 · 11 stage answer 4,505 · 12 SHADOW-HUB :37-38 + :72-103 ≈ 5 KB · 13 LOW (366, 367) ≈ 12.5 KB · 14 MID (369, 370) ≈ 11.7 KB · 15 HIGH Sonnet (372) ≈ 10.5 KB · 16 HIGH Terra (373, plus RUNS through Suites) ≈ 26 KB · 17 Grok unscored ≈ 3 KB · 18 originals baseline ≈ 19 KB · 19 rulings ≈ 3 KB · 27 laws ≈ 18 KB · 00/01/02 ≈ 15 KB.
- Stop line of counts: `RESULTS SITTING DONE · grok · astra (apart: C4 C5 C6) · opus (apart: C1 C2 C3) · cells closed: <n> of 6 · open · one house · claims that HOLD · owner items · ESCALATE`.
- Where the drafts differ from 270, and why:
  - One round and no derive: the brain §3 asks for one round and its output is the per-band lines.
  - Cells instead of 18 items, and the `SITTING:` closing line: the grades are the question.
  - No Gemini or `agy`: R921, and Gemini is N/A in the table.
  - Self-vendor rulings recorded apart for each cell (brain §3), instead of Grok-only S1/S5/S6/S9.
  - The floor is two counted houses per cell, instead of two outside houses.
  - Excerpts are bounded by headings instead of fixed line ranges.
  - Report path `results-sitting-2026-10-12.md`, folder `results-sitting/r1/`.
- Files read:
  - `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/426-draft-results-sitting.md`
  - `/Users/cobalt/Vault/Think/6 - Permanent/Memory/areas/cobalt.md` (What Cobalt is; Build rules on)
  - `/Users/cobalt/Vault/Think/6 - Permanent/Memory/topics/writing-rules.md`
  - `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/bakeoff-results-stage-answer-2026-10-11.md` (whole)
  - `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/complexity-shadow-results-2026-10-11.md` (whole)
  - `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/270-model-tribunal.md` (whole)
  - `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/271-model-tribunal-opus-seat.md` (whole)
  - `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/272-model-tribunal-derive.md` (line starts)
  - `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/258-f4-tribunal-r2.md` :9, :44-52
  - `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/338-f23-tribunal.md` :1
  - `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md` :1-104
  - `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-21/73-s3-exits-tribunal.md` (REDACTION grep)
  - Stop lines: `reports/model-tribunal-2026-10-10.md`, `f4-tribunal-r3-2026-10-10.md`, `f5-`/`f20-`/`f21-`/`f23-tribunal-2026-10-11.md`
  - Headings and `CHECK DONE` lines, `wc -c`, `wc -l` of the 8 shadow checks and the 3 originals (`/Users/cobalt/cobalt/docs/40 - DevDocs/reports/`)
  - Rows R908, R919–R921 (`cto-2026-10-10.md`); R1008, R1012, R1014, R1019, R1069, R1127 (`cto-2026-10-11.md`); R1250–R1255 and OWED (`cto-2026-10-12.md`)
  - LAWS.md headings (`/Users/cobalt/Vault/Think/6 - Permanent/Memory/LAWS.md`)

DRAFTED · decisions: 5
