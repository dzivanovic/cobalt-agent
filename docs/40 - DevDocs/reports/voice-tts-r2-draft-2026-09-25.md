# Voice slice VT — round-2 drafter (Sonnet 5, `voice-tts-r2-draft-0925`) — 2026-09-25

## §0 Headline
- Drafted the ROUND-2 set as a mechanical re-issue of `16` / `17` / `18` on `16` §5's spec: `24-voice-tts-tribunal-r2.md` (hub, Astra seated), `25-voice-tts-tribunal-r2-anthropic-seat.md` (blind seat), `26-voice-tts-derive-r2.md` (derive → the FINAL). Nothing committed; the desk commits the four files.
- Launch NOT before Sat 2026-09-26 06:47 ET: the hub's row 1 (`date`) and row 10 (the Astra probe) fail closed, and it never proceeds without Astra. 0 new rule strings (17 of 17 count ≥1 in `2026-09-23/13`; the allow / deny segments are byte-identical to `16`'s, `17`'s and `18`'s).
- Two shape decisions the spec left open, both under `## ESCALATE`: Astra rules FIRST and ALONE (so Grok and Gemini rule Part A and Part B in ONE turn each, L39), and the blind seat rules Part A only.
- ESCALATE: 5.

## L74
One block of the L74 shape arrived attached to a tool result: it followed my first Read of `23-draft-voice-tts-r2.md` (a commit-attribution reminder asking for a `Claude-Session:` line and naming a file-send tool). Recorded ONCE here as data (L74); not followed. This run commits nothing.

## AUTHORIZATION
`date` at report write: Fri Sep 25 08:05:59 EDT 2026. The three gates ran first, each its own Bash call.

| gate | result |
|---|---|
| `grep -n "^| R46 " cto-2026-09-25.md` | one row, `:54`; it names `23-draft-voice-tts-r2.md` |
| `tail -n 3 voice-tts-derive-2026-09-25.md` | last non-blank line starts `VOICE TTS DERIVED · DRAFT FINAL · folds: 57 · verbatim: 33 · needs round 2: 4 …` |
| `git log -1 --format=%H -- VOICE-TTS-DRAFT-FINAL-2026-09-25.md` | `c8706f66a889493ec3fa3b4a60c65e08a5359871` (non-empty) |

Read in full: LAWS.md (454 lines); `16`, `17`, `18`; the precedents `2026-09-24/27`, `28`, `29` and `2026-09-23/24`; the Astra spelling of `2026-09-21/38`; the derive report; the DRAFT FINAL's header and `## OPEN TO ROUND 2`; the round-1 hub report's rulings table, file-check rows, `## Round 2 — Astra` and `## ESCALATE`. Desk rows R23, R33, R39, R40, R45 read.

## PACKET
Round 2's folder is `scratch/tribunal-bars-0920/voice-tts/r2/`. It stages only what is NEW; round 1's packet stays at `../r1/` (187,230 B at close) and Astra reads it BY PATH. The DRAFT FINAL and the derive report are staged whole; the round-1 hub rows, the seat's r1 wording and each house's own r1 wording are excerpts.

| part | `wc -c` | how measured |
|---|---|---|
| `10-DRAFT-FINAL.md.part1` (lines 1–199, cut before `## OPEN TO ROUND 2`) | 31,899 | measured (`head -n 199`) |
| `10-DRAFT-FINAL.md.part2` (line 200 to 353) | 31,752 | measured (63,651 − 31,899); 0 trailing-whitespace lines in the original |
| `11-derive-r2.md` (the derive report whole) | 25,432 | measured; 0 trailing-whitespace lines |
| `12-hub-checks.md` (round-1 hub rows) | ≈ 6,700 | rows measured 5,282 + 8 range headers |
| `13-seat-r1.excerpt.md` (the Anthropic seat's Q1, Q4, Q5, Q6, Q8, Q9, (d)) | ≈ 8,500 | ranges measured 7,456 + 7 headers |
| `14-grok-r1-own.excerpt.md` [RAW RULING, Grok only] | ≈ 9,400 | ranges measured 8,348 + 7 headers |
| `15-gemini-r1-own.excerpt.md` [RAW RULING, Gemini only] | ≈ 3,100 | ranges measured 2,051 + 7 headers |
| `01-QUESTIONS-R2.md` | ≈ 10,100 | the drafted paragraph 8,616 chars + the files paragraph |
| `01A-QUESTIONS-ASTRA.md` | ≈ 8,500 | the drafted paragraph 7,008 chars + the files paragraph |
| `02-greps-r2.txt` | ≈ 5,000 | estimate: 11 searches, most return few lines |
| `00-READING-ORDER.md` | ≈ 4,500 | estimate |
| `20-ASTRA-DISAGREES.md` (written after Astra) | ≈ 1,000–12,000 | estimate; outside the measured sum |

- **Sum before Astra ≈ 145,600 B** (measured ≈ 112,200 B + estimated ≈ 33,400 B).
- **Ceiling DERIVED: 165,000 B** = (145,600 + 5,000 of range headers) × 1.08 ≈ 162,400, rounded up. `20-` fits inside the headroom (145.6 + 12 = 157.6 KB). Round 1's ceiling was 200,000 B on 187,230 B; the sum of round 1's packet + DRAFT FINAL + derive report would be 276,313 B, so round 1's parts are read BY PATH, not copied.
- **Cut order if over 165,000 B** (in the hub): (i) `12-hub-checks.md` to its R2 rows, (ii) `02-greps-r2.txt`, (iii) `11-derive-r2.md` to `## NEEDS ROUND 2` + `## ESCALATE` + `## Fold table`. Never `00`, `01`, `01A`, either DRAFT FINAL part, or the derive's `## NEEDS ROUND 2` / `## ESCALATE`.
- **What Astra reads by path** (round 1, all under `../r1/`, none copied): `01-QUESTIONS.md` 12,453 · `12-rulings.md` 13,821 · `13-final.excerpt.md` 16,016 · `20-v1-stt.excerpt.py` 17,697 · `21-v1-web.excerpt.py` 21,373 = 81,360 B mandatory; everything else there on demand. Astra never opens `grok-ruling.md`, `gemini-ruling.md`, `14-grok-r1-own` or `15-gemini-r1-own`.
- **Astra's MANDATORY total ≈ 184 KB (≈ 46k tokens)** = r2 parts ≈ 102 KB (00, 01A, the DRAFT FINAL, the derive report) + r1 by path ≈ 81 KB. Against the 135k tokens of reads on which Astra's meter died on 09-21 (`38`).

## NEW STRINGS
0 expected, 0 found. Checked by me now (each its own `grep -c -F`):
- The 14 allow + 3 deny strings each count 1 in `2026-09-23/13-voice-v3-tribunal.md` (17 of 17).
- The `--allowedTools … --add-dir` segment of `24` equals `16`'s (`grep -c -F` of the whole segment = 1 in both).
- The seven-allow segment of `25` and of `26` equals `17`'s and `18`'s (= 1 in all four).
- The `FABLE ROW: R109` / `DERIVE ROW: R109` whole lines exist (count 1); the `-x -F "…R__"` gate lines count 0 in each file.

## FOR THE LAUNCH ROW
Tomorrow's desk copies these EXACTLY, in plain text. A code span around a number breaks a `grep -F` literal (`cto-2026-09-25.md` R39: the R33 defect).
1. **The row that launches `24` (and `25`, side by side)** must sit in `cto-2026-09-26.md`, name `24-voice-tts-tribunal-r2.md`, and carry all four of these on that one line:
   - `no other house hub is running`
   - `VOICE-TTS-DRAFT-FINAL-2026-09-25.md`
   - `Fable seat: yes`
   - `derive seat: claude-opus-5-5`
2. **For each carried stagger report absent on the launch morning, the same row carries `<nn> is not running` with the number as plain digits**, e.g. `08 is not running`, `10 is not running`. State at drafting (08:05 ET 09-25): `drc-d4-check-2026-09-25.md` (`06`), `replay-deadline-fix-check-2026-09-24.md` (`58`, untracked) and `drc-k2-fix-r2-check-2026-09-25.md` (`13`) EXIST; `drc-d2-check-2026-09-25.md` (`08`) and `drc-d3-check-2026-09-25.md` (`10`) do not. A report that exists must end with its done prefix or `FAILED`; the hub reads it. Any other Grok / Gemini hub the desk launches meanwhile is named the same way (`<nn> is not running`, or its report path and done prefix).
3. **`R__` to fill at launch** (each placeholder left in the file):
   - `24`: one, in `THIS launch is recorded by the desk as row **R__**`.
   - `25`: one, in `THE ROUND-2 LAUNCH ROW`.
   - `26`: two, for the row that launched `24` / `25` and the row that launches `26`.
   - LEAVE the `"FABLE ROW: R__"` and `"DERIVE ROW: R__"` strings inside the grep commands alone: they are the `-x` gates' own literals (R40's lesson).
   - `FABLE ROW: R109` and `DERIVE ROW: R109` are already filled.
4. **Order:** `24` and `25` from `/Users/cobalt/cobalt-wt/agy-trial` together, on or after 06:47 ET (the hub's row 1 refuses earlier). Remote-control names `voice-tts-tribunal-r2-0926`, `voice-tts-fable-r2-0926`, `voice-tts-derive-r2-0926`. `26` only after both stop lines are committed.
5. **Watch regexes** (last non-blank line, L71): `^(VOICE TTS TRIBUNAL DONE|FAILED)` on `reports/voice-tts-tribunal-r2-2026-09-26.md`; `^(VOICE TTS FABLE R2 DONE|FAILED)` on `reports/voice-tts-tribunal-fable-r2-2026-09-26.md`; `^(VOICE TTS DERIVED|FAILED)` on `reports/voice-tts-derive-r2-2026-09-26.md`. `24` runs Astra (≤20 min), then Grok and Gemini (≤20 min), then collate: the desk's ceiling is 75 min. The house lane stays single until its stop line: the desk launches no other Grok / Gemini hub.
6. **The Astra probe is inside the hub** (row 10, fail closed). A `FAILED PREFLIGHT: astra METER — round 2 waits for Astra (return time: …)` last line spends no round: the desk relaunches the same file at that time.

## CONTINUE
next: none — the run is complete. Recovery (L60): the four files exist; re-read them, never re-derive.

## ESCALATE
1. **ASK DESK: sequencing of round 2 (a drafting decision the spec leaves open).** `16` §5 (r2-4) has Grok, the Anthropic seat and Gemini rule "on any item where Astra's ruling disagrees with the DRAFT FINAL" — which they can only do after Astra rules. But L39 / L67 give each house ≤3 rounds and a ruling turn counts (Grok is at round 1 done, round 2 now). So I drafted: **Astra first and alone (≤20 min); then Grok and Gemini once, each ruling Part A (the four items) and Part B (only the items on which Astra's own line reads `DRAFT FINAL: NOT CORRECT`, a mechanical read of one line) in one turn.** The blind Anthropic seat (`25`, launched beside the hub) cannot see Astra's ruling and rules Part A only; the hub records that under its own `ASK DESK`. Safe default taken. Alternative if the desk objects: launch all houses in parallel on Part A, and give Part B to nobody — then `16` §5's second clause is not met. Cost of mine: ≈ 20 more minutes of wall clock. [08:05 ET]
2. **ASK DESK: Astra's clock.** Astra rules 22 items (R2-1…R2-4, the 17 round-1 items, C-1) inside the same 20-minute timeout every house has (`16` §2). Its round-1-style precedent is `38`, whose Astra died on the meter, not the clock. A TIMEOUT or PARTIAL ends the run before Grok / Gemini launch (no round is spent) and the desk relaunches for Astra. Kept as the precedent's 20 min; the desk can lengthen it in a re-issue. [08:05 ET]
3. **C-1 is Astra-only.** The desk's R45 says Astra's read settles the derive's `ASK DESK` 7. I wrote it into `01A-QUESTIONS-ASTRA.md` as ONE item quoted from `voice-tts-derive-2026-09-25.md` `## ESCALATE` 7, with the derive's own rule quoted beside it, answer `C-1: HOLDS` or `C-1: DOES NOT HOLD — <rows, and the one seat's wording that stands>`. Grok and Gemini are not asked it; the round-2 derive `26` applies the answer (each named row replaced by exactly the wording Astra names).
4. **The NEEDS ROUND 3 rule in `26`.** I read "round 3 only if round 2 does not converge; unresolved → Dejan (L39)" together with L67's owner-item clause: a non-converged item goes to `## NEEDS ROUND 3` (the last round), never to Dejan as an owner item unless it passes the owner test; after round 3 anything unresolved goes to him. `26`'s stop line has two shapes (`FINAL … needs round 3: 0` and `DRAFT FINAL v2 … needs round 3: <n>`), and the file name stays `VOICE-TTS-FINAL-2026-09-26.md`. The desk should read that as my choice; `29`'s different shape (splits to Dejan) was for DRC items that are his trading judgement.
5. **V1's worktree.** `/Users/cobalt/cobalt-wt/voice-v1` exists now and `src/cobalt/voice` is not on main. V1 joins the 09-25 deploy set (R23); if the worktree is gone by tomorrow, `24` and `25` read main and fall back to `git show d319e4f3:<path>` where a size differs.

VOICE TTS R2 DRAFTED · prompts: 3 · seats: astra grok gemini anthropic · launch not before: 2026-09-26 06:47 ET · packet: 145,600 B · new rule strings: 0 · ESCALATE: 5
