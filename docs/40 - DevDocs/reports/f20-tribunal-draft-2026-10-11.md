# F20 tribunal drafter · 2026-10-11

## §0 Headline
- Three prompts written in `prompts/2026-10-11/`: hub `326a-f20-tribunal.md`, blind Opus seat `326b-f20-tribunal-opus-seat.md`, Opus derive `326c-f20-tribunal-derive.md`. Each is a minimal edit of `237` / `238` / `239`.
- Packet: the F20 proposal and its report, the SDK spike, the rulings, the F20 code the proposal cites, and the laws it touches. The question set is D1–D16 plus (a)–(g), 23 items.
- Seats follow R920 and R921: Grok and the blind Opus seat, Gemini only when the launch row says `gemini: sits`. Astra is recorded `NOT SEATED`, and the Codex string is dropped from the hub's launch line.
- The stagger gate is the current one from `258` (`grok runs: <n> of 3`, `openai seat: …`, `gemini: …`).
- Every allow and deny string was checked against its precedent. Three decisions are open.

## DECISIONS
- ASK DESK: the F4 floor was "the proposer plus two outside houses". Without Astra that cannot hold with Grok alone. I set the floor to Grok up and ruling, plus the blind Opus seat, as R921 seats it. Gemini adds a house and never replaces Grok. `FAILED PREFLIGHT: floor` fires if Grok is not up. Default: as written. [06:22 ET]
- ASK DESK: the task says the design is named by the `REPORT` line of `232`. That line names `f20-design-2026-10-10.md`, which is the drafter's report. The design is on the `OUTPUT` line, `f20-design-proposal-2026-10-10.md`. I staged both: the proposal as `10-`, the report as `11-`. The launch row must carry `f20-design-proposal-2026-10-10.md`. Default: as written. [06:22 ET]
- ASK DESK: the task says the derive states a remaining split as ONE line for Dejan, never before. I replaced the precedent's `NEEDS ROUND 2` and `DRAFT FINAL` path with that one line (`FINAL — ONE SPLIT FOR DEJAN`). The derive drafts no round-2 hub. L39 and L67 allow up to three rounds, so the desk can still ask for one. Default: as written. [06:22 ET]

## RECORDS
- Reads:
  - Prompts: `326-draft-f20-tribunal.md:1-6`; `232-draft-f20-design.md:1-8` (only its `REPORT` and `OUTPUT` lines were needed); `237-f4-tribunal.md:1-66`; `238-f4-tribunal-opus-seat.md:1-27`; `239-f4-tribunal-derive.md:1-37`; `262-draft-f4-tribunal-r2-stagger.md:1-10`; `258-f4-tribunal-r2.md:1` and `:9` (the current stagger paragraph).
  - Reports: `f20-design-proposal-2026-10-10.md:1-96` (13,421 B); `f20-design-2026-10-10.md:1-33` (4,151 B).
  - Desk rows: R920, R921 (`cto-2026-10-10.md:92`, `:91`); R858 (`:154`); R865 (`:147`); R1012, R1014 (`cto-2026-10-11.md:10`, `:8`); LAWS headings L26, L29, L35, L79 and the L-numbers cited.
- Launch rows: the desk has none yet for `326a` (`grep -n -F "f20-tribunal" cto-2026-10-11.md` printed nothing). The hub's gate refuses without it.
- Commit proofs:
  - `git log -1 -- reports/f20-design-proposal-2026-10-10.md` → `962ffba2a7f09bd76fd022e885fb2d98442e4a14`.
  - `git log -1 -S"F20 DESIGN DRAFTED" -- reports/f20-design-2026-10-10.md` → the same hash.
- Sizes (`wc -c`):
  - Proposal 13,421 B; drafter's report 4,151 B.
  - Cited source files, whole files only: `voice/registry.py` 3,924 · `voice.yaml` 2,227 · `0001_cobalt_jobs.sql` 3,793 · `jobs/wrapper.py` 8,047 · `killswitch.py` 4,491 · `jobs.yaml` 20,349 · `mattermost.py` 6,740 · `notify.yaml` 1,483 · `redact/guard.py` 8,273 · `modelaccess/guard.py` 1,800 · `modelaccess.yaml` 2,190 · `pyproject.toml` 2,708 · `generated.yaml` 2,130 B.
  - Large files, ranges only: `aset/web.py` 106,628 · `heartbeat/probes.py` 36,966 · `tunables.yaml` 36,489 B.
  - Spike 5,698 · Lane C source 9,809 · kashef memo 5,518 B.
  - Packet bound in the hub: MANDATORY ≈ 100 KB, whole ≈ 135 KB, ceiling 200,000 B, with a cut order. This is a bound from file sizes, not a measurement; the hub measures.
- Written prompts: `326a` 65,850 B, `326b` 20,609 B, `326c` 24,834 B.
- Allow and deny strings, checked with `grep -o -F -f <patterns> <file> --max-count=1`; every string printed in the precedent and in the new file:
  - `326a` against `237`: all 13 allow strings and 3 denies. These are `237`'s fourteen minus the Codex string.
  - `326b` against `238`: 7 allow and 3 denies.
  - `326c` against `239`: 7 allow and 3 denies.
  - Each string was checked as its own `-F` pattern, with the quotes, and printed once. This used one `grep -o -F -f` call per file rather than the `grep -c -F` per-string form, so each string's count is "printed ≥1", not an individual number.
- `FABLE ROW: R109` and `DERIVE ROW: R109` are whole lines that appear once in `326b` and `326c`.
- Not done: no code run, no launch, no git write. I did not check the F20 source line ranges the packet cites; the hub verifies each anchor with `grep -n`.

F20 TRIBUNAL DRAFTED · prompts: 3 · decisions: 3
