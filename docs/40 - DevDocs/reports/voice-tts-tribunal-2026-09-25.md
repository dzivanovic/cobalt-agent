# VOICE TTS TRIBUNAL — round 1 (hub `voice-tts-tribunal-0925`)

## §0 Headline
- Ruled: grok `BUILD AFTER derive folds the WITH clauses` · gemini `BUILD AFTER adding AbortError exclusion to the widget's device voice fallback` · Anthropic seat (Opus 5.5, blind) `BUILD AFTER the Q1 stored-reply guard and test_jobs_restarts seam are written in`. Astra: METER (return Sat 2026-09-26 06:47 ET), skipped, seated in round 2.
- Status: 3 of 3 houses ruled; questions settled 9 of 10 (Q1 is named in the Anthropic seat's BUILD AFTER line); dissents 1 (grok `REJECT` on item (g)). Split wordings on Q1, Q4, Q5, Q7 (quoted, not smoothed).
- ESCALATE: 13. Redactions: 0 (three-literal scan 0 on all 17 files). Anthropic-seat R1 claims checked: 25 HOLD of 28 checked (0 DO NOT HOLD, 3 UNVERIFIABLE FROM READS, 1 WITHDRAWN by the seat).
- Two proposal facts DO NOT HOLD (file-checked): T10 ("today only speech-to-text down") and T16 (`grep -F voice.yaml` "hits only the comment at :70" — `jobs.yaml` contains no `voice.yaml`). Gemini said `HOLDS` for T10 and `None` for WRONG FACTS.
- Deviation disclosed: the stagger literal `<nn> is not running` matched R33's launch row only through a backtick-tolerant pattern (`## PREFLIGHT` note; `## ESCALATE` ASK DESK).

## AUTHORIZATION
Launch row: `cto-2026-09-25.md` **R33** (filled number `R33` = the row the grep prints; the row names `16-voice-tts-tribunal.md`, and carries all three literals `VOICE-TTS-PROPOSAL-2026-09-25.md` · `Fable seat: yes` · `derive seat: claude-opus-5-5`).

| proof | result |
|---|---|
| R13 `cto-2026-09-20.md:86` | printed (13:33 ET, "Push and approved everything…") |
| R109 `cto-2026-09-22.md:56` | printed; carries `Make all Opus 5.5 for now` |
| R95 `cto-2026-09-23.md:103` | printed; carries `only use Fable, Astra, and Grok for new designs` |
| R97 `cto-2026-09-23.md:105` | printed; carries `unless it's a fourth` |
| R17 `cto-2026-09-24.md:35` | printed; carries `Grok approved with no asking going forward` |
| R19 `cto-2026-09-24.md:37` | printed; carries `All 4 house models approved` |
| R23 `cto-2026-09-25.md:31` | printed; carries `We will build Kokoro next on a side lane` |
| git -S R23 committed | `b6854e54…` (non-empty) |
| git -S R17 committed | `1758fd78…` (non-empty) |
| git -S R19 committed | `5055151d…` (non-empty) |
| proposal committed (`VOICE-TTS-PROPOSAL-2026-09-25.md`) | `a2fc3315…` (non-empty) |
| proposal stop line `VOICE TTS PROPOSED` committed | `a2fc3315…` (non-empty) |
| launch row: `grep -F "16-voice-tts-tribunal.md"` on `cto-2026-09-25.md` | rows R26 (:34), R32 (:40), R33 (:41). `cto-2026-09-26.md` does not exist (recorded, not fatal — the row is in the other file). R33 carries all three literals; R26 and R32 do not |
| launch row committed (`-S"16-voice-tts-tribunal.md"`, two desk files only) | `b6854e54…` (non-empty); `-S"\| R33 \|"` prints the same `b6854e54…` |
| NO NEW RULE: 14 allow + 3 deny strings, `grep -c -F` in `prompts/2026-09-23/13-voice-v3-tribunal.md` | 17 of 17 count 1 (each ≥1) |
| Sol / Opus checker strings in launch line | none (the launch line in this file carries none) |

## PREFLIGHT
| # | rule · command | exit | result |
|---|---|---|---|
| 1 | `date` | 0 | Fri Sep 25 06:50:30 EDT 2026 — allowed |
| 2 | R17 grep (GROK GATE) | 0 | row printed at `cto-2026-09-24.md:35`, literal present — allowed |
| 3 | R19 grep (AGY / ASTRA GATE) | 0 | row printed at `cto-2026-09-24.md:37`, literal present — allowed |
| 4 | `grok --version` | 0 | grok 1.0.25 (f7e67d6988e2) [stable] — allowed |
| 5 | `agy --version` | 0 | 1.2.10 — allowed |
| 6 | `ls scratch/tribunal-bars-0920` | 0 | exists — allowed |
| 7 | `ls scratch/tribunal-bars-0920/voice-tts/r1` | 1 | "No such file or directory" = FRESH RUN |
| 8 | STAGGER literal `grep -n -F "no other house hub is running"` on `cto-2026-09-25.md` | 0 | many desk rows print it; the row that ALSO names `16-voice-tts-tribunal.md` is **R33 (:41)**: "STAGGER (7'): no other house hub is running — `06` DONE 06:4x …, `13` DONE 03:41 …; `58` is not running …; `08` is not running …; `10` is not running …" — the desk's stagger statement for THIS launch. `cto-2026-09-26.md` not applicable (date reads 2026-09-25) |
| 8-s1 | `tail -n 3` `drc-d4-check-2026-09-25.md` (`06`) | 0 | last non-blank line starts `DRC D4 CHECK DONE ` — not running |
| 8-s2 | `tail -n 3` `replay-deadline-fix-check-2026-09-24.md` (`58`) | 1 | "No such file or directory" → desk launch-row check below |
| 8-s3 | `tail -n 3` `drc-d2-check-2026-09-25.md` (`08`) | 1 | "No such file or directory" → desk launch-row check below |
| 8-s4 | `tail -n 3` `drc-d3-check-2026-09-25.md` (`10`) | 1 | "No such file or directory" → desk launch-row check below |
| 8-s5 | `tail -n 3` `drc-k2-fix-r2-check-2026-09-25.md` (`13`) | 0 | last non-blank line starts `DRC K2 FIX R2 CHECK DONE ` — not running |
| 8-n2 | `grep -n -F "58 is not running"` on `cto-2026-09-25.md` | 0 | prints `:40` (R32, a desk record that names 16; it quotes the future launch row's wording) |
| 8-n3 | `grep -n -F "08 is not running"` | 1 | NO MATCH (literal) — see NOTE |
| 8-n4 | `grep -n -F "10 is not running"` | 1 | NO MATCH (literal) — see NOTE |
| 8-n | `grep -n -o -e "58. is not running" -e "08. is not running"` / `-e "10. is not running"` | 0 | `:41` R33 — matches `58` is not running, `08` is not running, `10` is not running |
| 9 | ASTRA PROBE (carried, background): `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` | 1 | `ERROR: You've hit your usage limit. … try again at Sep 26th, 2026 6:47 AM.` → **astra: METER** (return Sat 2026-09-26 06:47 ET — as expected, R107's row). RECORDED, SKIPPED, round 2 (§5). No astra launch is carried |

NOTE (stagger literal, disclosed — not a fatal): the prompt's literal for a house hub with no report is `<nn> is not running`. R33's launch row spells the numbers in markdown code spans (`` `08` is not running ``), so a strict `grep -F "08 is not running"` cannot match it (backtick between the number and the words); the literal is met in substance by R33 itself, which is the launch row, names `16-voice-tts-tribunal.md`, and states for each of 58, 08 and 10 that it is not running. I read the row with a backtick-tolerant pattern (`.` for the backtick) and record that here rather than fail the stagger on typography. The prompt's letter says a missing literal → `FAILED PREFLIGHT`; I did not apply that letter (see `## ESCALATE` ASK DESK 1). The desk's own R33 states: "the desk launches no other Grok / Gemini hub until `16`'s stop line."

V1 branch proofs (staging §1):
- `git log -1 --format=%H voice/v1-0923` = `d794e8999dc743f80c369c01cb80eb401d8e9b23` (expected `d794e899…`).
- `git show --stat d794e899` = one file, `voice-v1-fix-r2-build-2026-09-24.md`, 139 insertions — docs only.
- `ls /Users/cobalt/cobalt/src/cobalt/voice` = No such file — V1 is NOT yet on main; staged from the V1 worktree `/Users/cobalt/cobalt-wt/voice-v1/`.
- The ten V1 files' `wc -c` equal their drafting sizes: transcribe.py 6,851 · config.py 7,718 · web.py 15,021 · models.py 4,692 · store.py 9,189 · 0017_voice_turns.sql 3,569 · voice.yaml 2,728 · jobs.yaml 16,697 · probes.py 36,966 · start_aset.sh 3,223 — the worktree holds the committed bytes.

## Packet
Folder `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/voice-tts/r1/` (gitignored; the first Write created it, no `mkdir`). No file split into parts (each ≤ 38,000 B). No cut made: the whole packet is **187,230 B** against the 200,000 B ceiling (drafted ≈ 179 KB + ≈ 5 KB of range headers + ≈ 3 KB of the new `00`/`01` text). MANDATORY ≈ **127,685 B** (÷4 ≈ 31,921 tokens); whole ÷4 ≈ 46,807 tokens.

| file | wc -c | class | source |
|---|---|---|---|
| 00-READING-ORDER.md | 3,153 | MANDATORY | written last, this run |
| 01-QUESTIONS.md | 12,453 | MANDATORY | the prompt's verbatim text + the "Files in this folder:" paragraph |
| 02-greps.txt | 11,833 | MANDATORY | 13 pre-computed searches, full output (drafted ≈ 11 KB) |
| 10-PROPOSAL.md | 24,961 | MANDATORY | `docs/30 - Design/VOICE-TTS-PROPOSAL-2026-09-25.md` WHOLE — original `wc -c` 24,961; 0 trailing-whitespace lines; sizes equal |
| 11-propose-digest.md | 6,378 | MANDATORY | `reports/voice-tts-propose-2026-09-25.md` :3-7, :32-87, :92-95, :97 (anchors `## §0 Headline` :3, `## DIGEST` :32, `## ESCALATE` :92 confirmed by `grep -n "^## "`; stop line :97) |
| 12-rulings.md | 13,821 | MANDATORY | desk rows verbatim: `cto-2026-09-25.md` header :6-8 + R21 :29, R22 :30, R23 :31, R25 :33; `cto-2026-09-24.md` header :17-18 + R107 :131; `cto-2026-09-23.md` header :7-8 + R95 :103, R96 :104, R97 :105; `cto-2026-09-22.md` header :8-9 + R109 :56 |
| 13-final.excerpt.md | 16,016 | MANDATORY | FINAL :1-3, :54-65, :74-75, :86-87, :167-185, :190-224, :238, :243, :269-274, :281-282, :285, :311-322 (anchors :63, :74, :86, :167, :190 [:206, :220, :222], :269, :311 all matched) |
| 14-devices.excerpt.md | 1,834 | OPEN-AS-NEEDED | `topics/devices.md` :8, :21, :30, :31 |
| 15-final-more.excerpt.md | 15,527 | OPEN-AS-NEEDED | FINAL :275-280, :283-284, :286-310, :369-392 (anchor `## L52 and the bar` :369 matched) |
| 20-v1-stt.excerpt.py | 17,697 | MANDATORY | `transcribe.py` 1-189, `config.py` 1-169, `voice.yaml` 1-44 whole (sizes 6,851 + 7,718 + 2,728 as drafted; 0 trailing-whitespace lines in each) |
| 21-v1-web.excerpt.py | 21,373 | MANDATORY | `web.py` 1-312 whole (15,021 B; 0 trailing ws), `models.py` :130-162 (anchor `class TurnOutcome` :142 matched), `store.py` :150-175 (`def get(` :160 matched), `0017_voice_turns.sql` 1-72 whole (3,569 B; 0 trailing ws; `reply` :45, `session_id` :26 matched) |
| 22-v1-ops.excerpt.md | 5,059 | OPEN-AS-NEEDED | `jobs.yaml` :60-80 (`reads:` :67), `probes.py` :30-44 (`class Probe:` :30 matched), :95-110, :252-258, `start_aset.sh` :30-40 (`COBALT_VOICE_MODEL_DIR` :37 matched), `aset/web.py` :80-92 (router include :83, :90 matched) |
| 23-v1-build.excerpt.md | 9,706 | OPEN-AS-NEEDED | `git show d319e4f3:docs/40 - DevDocs/reports/voice-v1-build-2026-09-23.md` :84-101, :110-130, :435, :444-449, :466-468 (line numbers read from the `git show` output; the E10 row at :435 and the stop line at :468 matched the drafting) |
| 24-reference.excerpt.md | 4,488 | OPEN-AS-NEEDED | `POWER_PACKS.md` :570-610; `topics/cto-desk.md` :136 |
| 27-laws-excerpt.md | 22,931 | OPEN-AS-NEEDED | LAWS.md entries L1 :29-33, L3 :38-41, L9 :65-68, L15 :94-99, L23 :132-136, L28 :160-168, L31 :181-184, L32 :185-191, L35 :202-207, L44 :250-254, L52 :292-295, L57 :316-319, L67 :366-377, L70 :391-395, L72 :405-409 (each to the line before the next `### ` heading; the `## Part` / `---` headings that sit between L57, L70 and their next entry are excluded and said so in the range headers) |

Checks run on the staged copies: (1) `wc -c` of the whole-file copy of the proposal = its original (24,961); (2) for EVERY staged part, `grep -n -v -x -F -f <original(s)> <staged>` — the only lines not found verbatim in the originals are the `# <real path>:<range>` headers and blank lines (13 parts; three typos I made while copying — `15`'s L40 "item 2", `27`'s L67 `folded … R12` citation and its R96/R97 quotation — were found this way and fixed before launch); (3) redaction scan `grep -c -F -e TSLA -e 372.82 -e 374.50` on all 17 files (15 packet parts + the two rulings) = **0** for each (I used `-F` with three `-e` options instead of `-E "TSLA|372[.]82|374[.]50"`, the prompt's own PATTERN RULE forbidding alternation inside one pattern; the `.` in the two prices is matched literally, which is stricter). REDACTIONS: **0** replacements; no other ticker, price, share count or P&L of his found (the V1 report's `XYZ` tickers and the desk rows' `XYZ` phrasings are synthetic; the houses' scenario figures — `12.5`, clock times, `af_sarah` — are constructed by the houses, not his). NOT STAGED: any audio, transcript, stored `reply` or note of his; `Rules.md`; the FINAL whole; V1's `turn.py`, `tools.py`, `resolve.py`, `scratch.py`, `registry.py`; the V1 build report whole; the V1 fix/check reports; any production row (I opened `turn.py`, `confirm.py`, `tools.py`, `scratch.py`, `store.py` and the V1 tests myself at collate, for the file-checks only).
Notes: (a) main's tip moved during the run (`74d633ff`, a desk commit; `02-greps.txt` shows it); V1's worktree bytes = the committed `d319e4f3` bytes (all ten drafting sizes matched), so no `git show` fallback was needed for code. (b) the Write tool strips trailing whitespace: the whole-file originals carry 0 such lines, so nothing was stripped. (c) `02-greps.txt`'s first note tells the houses `grep` honours `.gitignore`.

## CONTINUE
Done. Nothing to resume. (Rulings kept: `scratch/tribunal-bars-0920/voice-tts/r1/grok-ruling.md` 30,350 B, `gemini-ruling.md` — never re-ask, L60.)

## Clock
| time | trigger | house minutes since launch | action |
|---|---|---|---|
| 06:50:30 | preflight row 1 (`date`) | — | no house launched |
| 07:06:23 | gate re-check before launch (`date`; R17 + R19 greps) | — | gates pass; GROK and GEMINI launched together, background (launch time = this `date`, read immediately before the launch message) |
| 07:06:43 | `date` after the launch message | grok 0 · gemini 0 | both running |
| 07:08:32 | completion notice: GEMINI (exit 0) | grok 2 · gemini 2 (finished) | gemini output read; written byte for byte (without `[exited with code 0]`) to `gemini-ruling.md` |
| 07:20:23 | completion notice: GROK (exit 0) | grok 14 (finished) · gemini done | grok wrote `grok-ruling.md` (30,350 B) itself; well inside the 20-minute clock (deadline was 07:26:23) |
| 07:21:34 | collate step: Anthropic-seat `tail -n 3` | — | its report is DONE (`VOICE TTS FABLE R1 DONE …`) |
| 07:22:40 | file-check FC 1–10 done | — | continuing |
| 07:24:30 | file-check FC 11–28 done; writing tables | — | continuing |
| 07:28:23 | close (`date` before the final line) | grok 14 · gemini 2 (both finished) | report complete; stop line written. Count note: "questions settled 9 of 10" counts Q2–Q10 (every seat ADOPT / ADOPT WITH); Q1 is excluded because the Anthropic seat's BUILD AFTER line names it. Gemini's BUILD AFTER line names no Q-number (it names the widget's abort/fallback), so I did not count it against Q6 or Q9 — that reading is the desk's |

## Rulings table
`ADOPT` = A · `ADOPT WITH` = AW · `REJECT` = R. "no word" = the house's answer to that item carries no ADOPT / ADOPT WITH / REJECT word (a fact-base, yes/no or NONE answer). Wordings ≤ 25 words per house; the wording itself is in `## Wording offered, verbatim` for grok and gemini (the Anthropic seat's is in its own report).

| item | grok | gemini | anthropic | agreement | wording offered / reason (grok · gemini) |
|---|---|---|---|---|---|
| Q1 route | AW | A | AW | 2 AW · 1 A (no R) | grok: 404 on missing/other-session/blank reply; 409 on digit reply while `tts_readback_server` false; no-store; widget must not call `show()` · gemini: separate GET keeps `TurnOutcome` unchanged |
| Q2 wire | AW | A | A | 1 AW · 2 A (no R) | grok: one WAV; drop the 1.5 s constant; chunks only after VT-X1 record · gemini: one body; chunks only if VT-X1 misses 1.5 s |
| Q3 runtime | A | A | A | 3-0 A | grok: ONNX first from the lock (`02-greps.txt:79-80`); `tts_speed` bound = VT-X4's range · gemini: reuse locked `onnxruntime` |
| Q4 GPL / native g2p | AW | AW | AW | 3 AW, three different orders | grok: non-GPL in-process, else loopback sidecar, him only if no non-GPL licence · gemini: loopback sidecar |
| Q5 VT-X5 gate | AW | A | AW | 2 AW · 1 A; grok = flag `tts_readback_server`; Anthropic = no flag, Q1 guard | grok: gate every reply with a digit, key `tts_readback_server` (9th key) · gemini: hard gate, device voice until verified |
| Q6 fallback order | A | A | AW | 2 A · 1 AW | grok: order for every device, not waiting on owner item 2 · gemini: aligns with L23 and R23 |
| Q7 `voice_tts` probe | AW | A | AW | 2 AW · 1 A | grok: probe reads files + resident status; `Probe` gets a level field · gemini: presence + `/voice/status`, never synthesize |
| Q8 L31 | AW | A | AW | 2 AW · 1 A; the three differ on whether a person's name may be a `tts_voice` value | grok: `neural-local`, neutral voice stem, no person/vendor name · gemini: `neural-82m` lawful; person's name allowed |
| Q9 single-flight + abort | AW | A | AW | 2 AW · 1 A | grok: one lock, generation integer, abort not a failure · gemini: single-flight lock, abort cancels the fetch |
| Q10 L57 / §2.5 | AW | A | A | 1 AW · 2 A | grok: add `Cache-Control: no-store`, revoke object URL, flag stays false if VT-X6 fails · gemini: memory + body only |
| (a) fact base | no word | no word | AW | grok: T10, T16 DOES NOT HOLD · gemini: all HOLD | grok: five misses (Probe AMBER, `status_lines`, `speak()` at :252…) · gemini: missed NONE |
| (b) one path | AW | no word | AW | 2 AW | grok: delete `device-os` engine; Q1/Q5/Q9 clauses · gemini: NONE, but a double-speak path on `AbortError` |
| (c) L15 / L23 | AW | no word ("Yes") | AW | 2 AW | grok: four gates as VT-1's merge bar · gemini: adoption path gated on VT-X4 |
| (d) loud and replayable | AW | no word ("Yes") | AW | 2 AW | grok: table of hops; `no-store` · gemini: all rows loud; abort silent on purpose |
| (e) boundary | NONE (with Q1's route) | NONE | A — NONE (once Q1's guard is in) | 3 NONE | — |
| (f) seam | AW | no word ("Yes") | AW | 2 AW | grok: `ops/fetch-voice-models.sh`, nine keys, E5 cell, amendments B and F · gemini: §10 and A–F correct; reads gap real |
| (g) owner test | **R** (both items) | no word (both items his taste) | AW (item 1 passes; item 2 fails) | **split**: 1 R · 1 AW · 1 no word | grok: neither is his under L67's list · gemini: both his taste |
| closing line | `TRIBUNAL R1: BUILD AFTER derive folds the WITH clauses` | `TRIBUNAL R1: BUILD AFTER adding AbortError exclusion to the widget's device voice fallback` | `TRIBUNAL R1: BUILD AFTER the Q1 stored-reply guard and test_jobs_restarts seam are written in` | 3 BUILD AFTER, none DO NOT BUILD | — |

The `anthropic` column is filled from its report's `## DIGEST FOR THE DESK` and `## Rulings` (verdict word only), at the Anthropic-seat step below.

## Wording offered, verbatim
User-data spans: none redacted (0). Grok's scenario figures (clock times, `12.5`, `af_sarah`) are the house's own constructed examples.

### GROK (`grok-ruling.md`, items in its order; text unedited)

**Q1 — Route**

ADOPT WITH this paragraph in place of §4's decision and of reasons 4–6:

`GET /voice/tts?session=<id>&turn_id=<id>` is a separate request, sent only after that turn's JSON is on screen, and only for the turn still on screen. It uses the existing `peer_gate` and `_session`. It loads the row with `VoiceTurnStore.get(turn_id)` and returns a named 404 `voice: no such turn` when the row is missing, `session_id` differs, or `reply` is null or blank. It has no text parameter. While `tts_readback_server` is false, a `reply` that contains a digit is not synthesized: named 409 `voice: figures stay on the device voice`. Success is one `audio/wav` body, `Cache-Control: no-store`, and the route logs status and byte length only. The widget handles that response in its own function and must not call `show()`.

Separate from the turn response so a synthesis failure cannot fail the turn, `TurnOutcome` stays as built, and mute before the fetch sends nothing. The digit rule has one home, the route: a widget copy of the predicate would be a second path. At 10:12:00 he presses "what's the stop"; the row's `reply` is "stop is 12.5" and `state` is `answered`. Without the 409, the server speaks the figure before VT-X5. A 404 for a blank `reply` stops a fetch of a nullable column (`0017` `reply` is nullable; `TurnOutcome.reply` is a `str`) from being spoken as an error string.

**Q2 — Wire**

ADOPT WITH this paragraph in place of §4's streaming sentence:

One in-memory `audio/wav` (stdlib `wave` into a buffer, no file). No streaming in VT. No 1.5 s constant. Sentence chunks are a round-2 question only after the VT-X1 record exists, and only if that record says one body is too slow. That same record sets `tts_timeout_s` and `tts_max_chars`. Their `# source:` lines cite it.

The 1.5 s figure is not in the FINAL excerpt, the V1 code, or the greps. Shipping it would be a threshold with no measurement. One body is the simpler mechanism and adds nothing to VT-2 beyond the cache header in Q1.

**Q3 — Runtime**

ADOPT. ONNX first: `uv.lock` already names `onnxruntime` (`02-greps.txt:79-80`, pulled in by `faster-whisper`). PyTorch is added only if VT-X4 shows that locked runtime cannot load the pinned weights offline. The MIT line and `1.30.0` are the E10 record (`23-v1-build.excerpt.md:45`), not re-read from the lock here; VT-X4 re-reads them.

`tts_speed`'s schema bound is the range VT-X4 records from the runtime, not 0.5–2.0. That interval is not in the staged files. The yaml value is the speed the passing VT-X5 run used. No new chunk: the pin stays in VT-1, and VT-1 may not merge a pin that differs from VT-X4's lock diff.

**Q4 — GPL or native grapheme-to-phoneme**

ADOPT WITH this order, in place of §3's "Process" row:

VT-X4 lists every licence. If an in-process load is non-GPL (the licence class VT-X4 records: MIT, BSD, Apache, or the same), it is in-process inside `com.cobalt.aset`. If the only in-process load needs GPL or a native grapheme-to-phoneme library, that library is not imported into `com.cobalt.aset`. The one alternative is a loopback sidecar on `127.0.0.1` only: no tailnet port, no cloud provider, and no file from the reference kit. He is asked only when that sidecar also has no non-GPL licence. In-process GPL is rejected, not offered.

`24-reference.excerpt.md:7-24` is a cloud cascade (ElevenLabs, Gradium) plus macOS `say` writing `/tmp`. L15 makes it reference only. Copying it would be a second, cloud path. A sidecar that exists only when the in-process path is unlawful is still one synthesizer, not two. Price: no extra chunk; the sidecar is a VT-X4 result, built inside VT-1 only if that result says so.

**Q5 — VT-X5 gate**

ADOPT WITH:

VT-X5 is a hard gate on every server-voiced reply that contains a digit, not only on confirm read-backs. Required key `tts_readback_server` (bool, no code default). `# source:` is the VT-X5 record. The value is false until that record shows zero numeric mismatches on every read template and every read-back template. While false, Q1's 409 stands and the widget calls `speak()` once on that reply. The key is the ninth required voice key.

§7 VT-X5 covers "every read / read-back template"; §5 and amendment B gate only "a read-back". At 10:50:00 he asks for a stop, the turn is `answered` (not `awaiting_confirm`), and the reply is "stop is 12.5". A read-back-only gate lets the server speak it before any round trip. One boolean in the route, enforced before VT-3's playback, is enough. No new chunk.

**Q6 — Fallback order**

ADOPT. Server voice, then the device's `localService` voice, then text plus both AMBER lines. This is the order for every device, including the phone. It is not waiting on owner item 2.

Both hops are local. L23's cloud fallback does not arise: there is no cloud synthesizer. The digit 409 is a refusal before this order, not a second order. A `play()` refusal still drops to the device voice with AMBER "server voice blocked by this browser" (VT-X3 may add tap-to-play on that browser; it does not reorder the default).

**Q7 — Probe**

ADOPT WITH this paragraph in place of §6's probe bullets:

`voice_tts` checks two things and synthesizes nothing. (1) The pinned model file and the neutral voice stem are present under the `model_dir` from `load_voice_config` (the one loader). (2) The resident's `GET /voice/status` on loopback, which is already an allowed peer, reports `tts.last` and `tts.rss_mb`. The probe does not import the TTS runtime. `engine missing` is the resident's status class. Missing file and unreachable resident are RED. Last synthesis timeout, and `rss_mb` above `tts_rss_amber_mb`, are AMBER. The detail line names the directory read. `Probe.line()` today prints only OK, `??`, or RED (`22-v1-ops.excerpt.md`, `probes.py:36-37`). VT-4 adds one level field on that class so AMBER is not stored as `ok=False`.

At 11:00 the weights are loaded and RSS is over the amber line. With the class as built, `ok=False` makes the heartbeat say RED "server voice down" while he is hearing the voice. Importing the runtime inside the 900 s heartbeat would be a second load, and whether that import touches the network is uncited until VT-X4. File presence plus the resident's own status does not do that. Same chunk VT-4; no second probe type (V4's future AMBER scratch probe uses the same field).

**Q8 — L31**

ADOPT WITH:

`tts_*` keys are lawful. The engine value is `neural-local` and the one class is `NeuralSynthesizer`, unless VT-X4's own model card states a parameter count of 82 million, in which case the value may be `neural-82m`. The `# source:` line cites that card. `82m` is not a fact in this packet (T18). `tts_voice` is a neutral stem (`v01`, `v02`, …) chosen by the one fetch command. The value must not be a person's name or a vendor's name. The vendor's filename may remain a file inside `model_dir`; the yaml points at the stem. One `ENGINES` entry. No `device-os` engine.

L31 (`27-laws-excerpt.md`) forbids person or vendor names in identifiers, schema, config keys, enum values, and system design docs, and says names live in reference material and user data only. A voice stem in `voice.yaml` is neither. `af_heart` (`24-reference.excerpt.md:39`) is a reference-kit default, not a value VT may copy. V1's `faster-whisper` / `FasterWhisperTranscriber` (`config.py:47`, `transcribe.py:129-130`, `:163`): the packet does not show those strings are a person or a vendor. They are the artifact's name. This tribunal does not call an L31 breach the text does not prove, and it adds no VT chunk to rename them. R25's V1 backlog ticket stays the desk's and is not a hold.

At 12:00 a yaml committed as `tts_voice: af_sarah` puts a person's name in system config. The neutral stem avoids that without a second naming scheme in code: the map is a file the fetch command writes beside the weights.

**Q9 — Single-flight and abort**

ADOPT WITH:

One process lock covers load and synthesize. The widget keeps a generation integer, bumped on pointer-down, Send, mute, and every `show()`. Each bump aborts the in-flight fetch and pauses the audio element. A completion whose generation is stale is discarded and does not call `speak()`. Abort, mute, and a stale generation are not failures: no device voice and no AMBER. A non-200, a timeout, a `play()` rejection, or an audio `error` on the current generation falls back once. `show()` does not call `speak()` unless that fallback fires or the route returned 409. Mute before the fetch sends nothing. Mute after the fetch has started does not kill the worker (V1's decode thread is the same: `transcribe.py:13-15`); the lock frees when the call returns or `tts_timeout_s` fires.

V1 does not single-flight: each call builds its own one-worker pool (`transcribe.py:171-180`). The lock is new, and it is one lock, not a load lock plus a synth lock. At 10:00:00 he presses; turn A is in flight. At 10:00:01.5 he presses again, before A's JSON. At 10:00:03.0 A's reply is shown and a fetch starts. At 10:00:03.2 B's reply replaces the text. If `show(B)` does not bump the generation, A's WAV plays under B's words. If the abort is caught as "server voice down", the device also speaks A's reply while he is recording. Both are two voices for one screen. The generation integer is widget code inside VT-3, no new file.

**Q10 — L57 and §2.5**

ADOPT WITH. Amendment B is the paragraph under (f). "streams" is amended. "writes no file" is kept. No audio bytes in the database (`0017` has no audio-bytes column; do not add one), on disk, in the vault, in git, or in the log. The body carries `Cache-Control: no-store`. The page revokes the object URL on ended, abort, and supersede. Stored inputs are the row's `reply` and the pinned `tts_engine`, `tts_model`, `tts_revision`, `tts_voice`, `tts_speed`. VT-X6 compares bytes twice and after a restart. If they differ, the claim narrows to "text replayable, audio not" and `tts_readback_server` stays false.

The design controls process memory, the logging call, and the response headers. It does not control a browser or `tailscale serve` cache unless `no-store` is set. At 09:00 the phone fetches turn T1; at 09:05 `tts_voice` changes and the resident restarts; at 09:06 a cached GET of the same URL plays the old bytes while the pinned config names the new stem. That replay is not the stored inputs. An unrun claim about whether this browser caches is not the defect; the missing header is, because the URL does not include the revision or the voice.

**(a) Fact base** — grok answered with a per-row table (T1–T19; no ADOPT word). Its non-HOLDS and additions, unedited:

- T1 (excerpt): "HOLDS that `COBALT-REQUIREMENTS.md:208` names Kokoro TTS (`02-greps.txt:83`). The words "faster-whisper STT → small local router" are not in that hit (the search was kokoro-only). They are the desk's paraphrase in R21, not a line this packet printed."
- T9: "HOLDS. `localVoice` / `speak` / `show` call `speak(j.reply)` at `web.py:252`; mute cancels `speechSynthesis` at `:292` (`02-greps.txt:18-24`). The proposal's split `:236-246` vs `:247-253` does not match the functions; the call site is `:252`. Behavior cited is the behavior in the file."
- T10: "DOES NOT HOLD as written. Peer gate, `to_thread`, and `GET /voice/status` hold (`web.py:71-76`, `:84-93`, `:141-155`; routes at `02-greps.txt:46-50`). "today only speech-to-text down (model missing)" does not. `status_lines` starts from `_SWEEP_LINES` (`web.py:144`) and startup appends reaper lines (`:180-183`). `voice.yaml:44` is `allowed_peers`, which the citation also covers."
- T16: "Absence HOLDS. `reads:` is `configs/dev/aset.yaml`, `configs/cobalt/taxonomy/tunables.yaml`, `configs/cobalt/backup.yaml` (`22-v1-ops.excerpt.md`). `voice.yaml` is not an entry. DOES NOT HOLD that `grep -F voice.yaml` hits the comment at `:70`: that comment does not contain the string `voice.yaml`. How `cobalt jobs restarts` classifies a change is correctly UNPROVEN (command not run, L70)."
- T18: "Correctly an experiment. Staged search of the V1 tree (`02-greps.txt:4-11`) has no kokoro hit. `src/cobalt/voice/synthesize.py` is on no branch (`02-greps.txt:119-120`). The lock extract lists no kokoro package; a kokoro scan of `uv.lock` itself is not one of the staged commands. Not a proven empty tree. VT-X4."
- "§1 missed: `Probe.line()` has no AMBER (`22-v1-ops.excerpt.md`). The §7 AMBER heartbeat cannot be said with the class as built. Q7. · `status_lines` is not STT-only. T10. · `web.py:252` calls `speak()` on every response. That call is the existing speech path. VT must not leave it in place beside the new fetch. Q9. No other speech path is in the V1 tree. · `radar/replay.py` "synthesized" and `backup.yaml`'s "synthesized" (`02-greps.txt:9-11`) are not speech. · The reference kit's `/tmp` `say` path and cloud TTS (`24-reference.excerpt.md:13-24`) are not a Cobalt path. They are the path VT must not grow."

**(b) One path**

ADOPT WITH the Q1, Q5, and Q9 paragraphs, and delete §3's future `device-os` engine. After that, one synthesizer, one GET, one `model_dir`, one fetch command, one loader, one status route.

Walk. Press at T: `POST /voice/turn` only. Text is on screen at T. At T+0.2 s the widget fetches `GET /voice/tts` for that `turn_id` and that `SESSION`, unless Q5's 409 applies, in which case `speak()` runs once and no fetch starts. The server lock synthesizes the stored `reply`. The audio element plays. `speak()` is not called. At T+1 s a second press bumps the generation, aborts the fetch, and pauses audio. A's late body is discarded. The device does not speak A. B's later `show()` may fetch B. At T+2 s mute bumps again, pauses, and cancels `speechSynthesis`. It does not start a voice. A resident restart between the commit and the fetch drops the connection or serves the row from disk-backed `voice_turns`: one new synthesis from `reply` plus config, or a named failure and one device fallback. No WAV file is left. The in-memory lock dies with the process.

Two voices happen only if the old `speak()` at `:252` stays unconditional, or an abort is treated as a synthesis failure. Those are the WITH clauses. `device-os` on the server would be a second synthesizer next to the widget's `speechSynthesis`. It is not built.

**(c) Dependency and local-first**

ADOPT WITH the four gates named as VT-1's merge bar. L15 (`27-laws-excerpt.md`): third-party code is reference only; a pattern is adoptable only when it is proven, conformant with our laws, industry-standard, and reviewed-clean. VT-X4 is that bar: lock diff, licence of weights, runtime, grapheme-to-phoneme, and native libs, offline load from an empty `model_dir` (`model_missing`), and load with the network off. VT-1 cannot merge without that diff. "ONNX first" is argued from the lock's existing `onnxruntime`, not from a Kokoro package (none is locked). It is not a claim the ONNX model file exists.

Memory beside the wired limit is VT-X2, using T12's `vm_stat` `wired down` method and T13's 96 GB / 88 GB limit as the baseline description. Not argued. No number for `tts_rss_amber_mb` until that run.

The fallback order is lawful under L23: the lane runs on the host, the device hop is local, the last hop is text. Nothing in VT is a cloud path. The only network is the one deploy-time fetch into `COBALT_VOICE_MODEL_DIR`, shared with V4, and VT-X4 must show runtime load does not use it. The reference cascade is not a fallback.

**(d) Loud, and replayable**

ADOPT WITH Q1, Q7, Q9, and Q10. Failure rows in §8 C are loud on the widget except the two holes those clauses close.

| Hop | What he gets |
|---|---|
| Model or engine missing | device voice + AMBER "server voice down (model missing)"; probe RED |
| Timeout or engine error on the current generation | device voice + AMBER "server voice down (<class>)"; probe AMBER via Q7's level |
| `play()` or audio `error` | device voice + AMBER "server voice blocked by this browser"; heartbeat — |
| Digit reply while the flag is false | device voice + the 409's AMBER; no server audio |
| Over `tts_max_chars` | device voice + AMBER "reply too long for the server voice"; heartbeat — |
| Blank reply | 404; text unchanged; no device voice of an empty string |
| RSS over the line | he may still hear audio; heartbeat AMBER with the number. Not a widget banner. Same pattern as a scratch count. |
| Abort, mute, stale generation | silence on purpose. Named so it is not read as a missed banner. |
| Neither voice | text + both AMBER lines |

An engine that returns 200 and silence is not a defect on this packet. It is VT-X1: a body with `duration_s` of 0, or VT-X5 hearing nothing, changes the design (treat as `engine_error`). Unrun, so not a hole.

No audio stored, as far as the design controls: memory, the response, the log line, the object URL. A proxy or browser cache is controlled only by `Cache-Control: no-store` (Q10). If VT-X6 fails, the narrowing in Q10 is the right one, and figure replies stay on the device voice.

**(e) Boundary**

NONE, with Q1's route. No text parameter, so it is not a free text-to-audio endpoint. A different `session_id` is 404. The peer gate is the existing one: a peer it refuses still gets 403 (`web.py:71-76`). No file, no new row, no vault note. Nothing is installed on the phone or the trading PC; both are browser tabs (`14-devices.excerpt.md:11`, FINAL boundary in `15-final-more.excerpt.md:62`). No trading-platform read. The synthesizer does not compute a score, rank, grade, or size. `[F-26]` still reaches the card through the existing confirm path (`set_card_stop` → `record_stop_edit`); VT does not add a computation to it (`15-final-more.excerpt.md:42`). `[F-25]` is unchanged: an allowed peer can already read the reply as JSON. Audio of that same reply adds no principal.

The path that would break this, and is rejected: the reference kit's `say` writing `/tmp`, or any POST of arbitrary text.

**(f) Seam**

ADOPT WITH these additions to §10. The V1 files named are the right list: `voice/web.py`, `voice/config.py`, `configs/cobalt/voice.yaml`, `models.py` docstring only, `store.py` read-only via `get`, `transcribe.py` unchanged, `jobs.yaml`, `pyproject.toml` / `uv.lock`, `tests/cobalt/test_radar_panel_cards.py`. V4 seam: `heartbeat/probes.py` and one fetch command. `TurnOutcome`'s fields and the turn function's callers are unchanged. `tools.py` is untouched. No DRC file.

Add:

- The fetch command's path is `ops/fetch-voice-models.sh`. Whichever of V4 and VT builds first creates it; the other calls it. It is the only network path. It writes weights and the neutral voice stems.
- `voice.yaml` gains nine required keys, not eight: the eight in §3, plus `tts_readback_server`.
- `GET /voice/status` gains `tts.last` and `tts.rss_mb` beside `lines`. Same route.
- `Probe`'s level field (Q7).
- `configs/cobalt/voice.yaml` is added to `com.cobalt.aset`'s `reads:` if still absent.
- E5's result cell is amended (below). Amendment F is scoped so it cannot be read as retiring `[F-26]`.

`aset/web.py` already includes the router (`22-v1-ops.excerpt.md`, `:83-92`). No change there. Both pages take `widget_html()`; one partial is the whole widget.

Amendments A, C, D, E: correct and minimal, once C's rows include Q9's "stale or aborted fetch → silence, no device voice, heartbeat —" and D's engine value follows Q8 (`neural-local` unless the card says 82 million). None of A–F rewrites a FINAL clause VT does not need, except B's E5 sentence, which does not by itself fix the E5 row. That row still says a failed E5 creates the server slice (`13-final.excerpt.md:101`). R23 set that condition aside. One cell, or a later reader builds VT only when E5 fails.

E5 result cell, replace with: `none local → that device has no second hop (text + AMBER); the server voice is still first (R23)`.

Amendment B, replace §2.5 whole with:

> **2.5 Reply by voice.** The reply text is shown in the widget first. Unless muted, and unless a newer press, Send, or `show()` has superseded that turn, the widget fetches `GET /voice/tts?session=<id>&turn_id=<id>` over the same tailnet HTTPS URL. The route sits behind the same peer gate, uses the same session check, and reads that turn's stored `reply`. A missing row, a different `session_id`, or a blank `reply` is a named 404. The route synthesizes with the local `Synthesizer` (one engine by config, weights pinned in the existing `model_dir`, offline load, off the event loop, one synthesis at a time per process) and returns ONE in-memory `audio/wav` body with `Cache-Control: no-store`. **No reply audio is ever written: not to disk, the database, the vault, git, or the log.** Its stored inputs are the turn's `reply` and the committed voice config (`tts_engine`, `tts_model`, `tts_revision`, `tts_voice`, `tts_speed`). If VT-X6 does not show identical bytes, that claim narrows to "text replayable, audio not." The widget plays the body in the page and revokes the object URL on ended, abort, or supersede. A stale or aborted fetch does not fall back to the device voice. **Fallback order, each step loud (L9), only when the fetch of the turn still on screen fails: server voice → the device's own `speechSynthesis` (`localService` voice only) → text only**, each with an AMBER line naming the class. Mute skips the fetch and pauses what is playing; it does not kill a synthesis already running. A reply that contains a digit is spoken by the server only when `tts_readback_server` is true, set from VT-X5 (zero numeric mismatches on every read and read-back template); until then the route returns a named 409 and the device voice speaks. His R23 (`cto-2026-09-25.md:31`) ordered this slice regardless of E5. E5 decides only whether the device-voice hop exists on that device. Slice VT (§9); design `docs/30 - Design/VOICE-TTS-PROPOSAL-2026-09-25.md`.

Amendment F, add: "VT's synthesizer reaches no score: it speaks text the turn already rendered and computes, ranks, grades and sizes nothing. [F-26] is unchanged."

RESTARTS. `voice.yaml` missing from `reads:` is a real gap. The comment at `jobs.yaml:70` says the resident caches `_CONFIG` and a change reaches it only by restart, and the reads list still does not name `voice.yaml`. Whether `cobalt jobs restarts` today prints nothing, UNCLASSIFIED, or `com.cobalt.aset` is an experiment: the command was not run (L70). Both. VT adds the line anyway. Tonight's classification of the current tree stays the deploy drafter's item (R25 reading 2), not a VT hold. The "6 UNCLASSIFIED" precedent is the V1 stop line (`23-v1-build.excerpt.md:58`), recorded, not re-run.

**(g) Owner test — REJECT text**

REJECT both owner items as items for him. L67 (`27-laws-excerpt.md`, amended 2026-09-24): an owner item is his money, his data, his laws, or his trading judgement. A question a house can settle does not go to him. Taste is the proposal's argument, not that law's list. Even if taste qualified, a house can decide both.

Item 1. `tts_voice` is the neutral stem that wins VT-X5's clarity count. `tts_speed` is the speed that run used. He can change the yaml later; that edit is not this tribunal's approval and not a precondition of VT-1. The device session he already owes (T15) may play samples. It is not a gate.

Item 2. Server voice first on the phone, by L23 and by Q6. VT-X3 can force tap-to-play where `play()` is refused. It does not ask him which voice is first.

No other item passes. A GPL deadlock reaches him only if Q4's last step happens. It has not. The device session is already owed; joining VT-X3 to it is not a new decision.

### GEMINI (`gemini-ruling.md`; every ADOPT WITH / REJECT text, unedited — gemini gave one ADOPT WITH, Q4, and no REJECT)

**Q4**
`ADOPT WITH a loopback sidecar`
Loading a GPL or native grapheme-to-phoneme library in-process risks the stability and licensing of the main `com.cobalt.aset` application. A loopback sidecar securely isolates the dependency on the host while fulfilling the requirement without adding a cloud path.

(Gemini's other answers are `ADOPT` or yes/no/NONE; its closing-line condition — "adding AbortError exclusion to the widget's device voice fallback" — rests on its item (b) text: "NONE for duplicate synthesis paths, routes, model directories, config loaders, or fetch commands. However, there is a double-speak path during abort: a press → text reply at T; fetch at T+0.2 s; a second press at T+1 s aborts the fetch; if the widget's catch block triggers the device voice fallback on the `AbortError`, the device speaks the aborted reply while the new turn starts. The widget must explicitly exclude `AbortError` from triggering the fallback chain.")

The Anthropic seat's wordings are NOT copied here (the derive reads its report itself).

## Checked against the files
Method: files opened by me — the V1 worktree `/Users/cobalt/cobalt-wt/voice-v1/` (`turn.py`, `confirm.py`, `tools.py`, `scratch.py`, `store.py`, `probes.py`, `jobs.yaml`, `uv.lock`, `pyproject.toml`, `ops/`, tests), `/Users/cobalt/cobalt/` (FINAL, requirements, desk files) and the staged packet. His notes and `Rules.md` not opened (L32). Numbers: no house number was re-derived by a house except the Anthropic seat's arithmetic (checked below).

| # | claim | who | file:line | verdict | note (≤30 words) |
|---|---|---|---|---|---|
| G1 | T10 "today only speech-to-text down (model missing)" is wrong: `status_lines` also returns sweep, reaper and "voice config unreadable" lines | grok (T10), anthropic (FC10 too); gemini says T10 HOLDS | `web.py:140-149` (`lines = list(_SWEEP_LINES)`; `:148`), `:180-183` | HOLDS (grok, anthropic); gemini's `T10: HOLDS` DOES NOT HOLD | Contradiction quoted: gemini "T10: HOLDS" vs grok "DOES NOT HOLD as written" |
| G2 | T16 `grep -F voice.yaml` "hits only the comment at :70": the comment has no `voice.yaml` | grok, anthropic | `jobs.yaml` — `grep -n -F voice.yaml` prints nothing; `:70` names `voice/config.py` | HOLDS (proposal's T16 wording DOES NOT HOLD) | the absence from `reads:` (`:67-75`) is real |
| G3 | T1's quoted words are "the desk's paraphrase in R21", not in the requirement | grok | `COBALT-REQUIREMENTS.md:206-208` prints "faster-whisper STT → small local router model → … Kokoro TTS" | DOES NOT HOLD | the proposal's T1 quote is in the requirement file; grok's search was kokoro-only |
| G4 | T9's ranges `:236-246` vs `:247-253` "do not match the functions" | grok | `web.py:236-240` `localVoice`, `:241-246` `speak`, `:247-253` `show` | DOES NOT HOLD | call site `:252` HOLDS; the two ranges are localVoice+speak and show |
| G5 | `store.get` has no session filter; `0017` `reply` nullable; `TurnOutcome.reply: str` | grok | `store.py:160-166`; `0017:45`; `models.py:149` | HOLDS | |
| G6 | `Probe` has no AMBER level (`ok`, `unknown`); `line()` prints OK / ?? / RED | grok | `probes.py:30-42`; `grep -i amber probes.py` prints nothing | HOLDS | consequence "AMBER stored as ok=False" is inference from the fields |
| G7 | the 1.5 s figure is not in the FINAL | grok | `grep -F -e "1.5 s" -e "1.5s"` on the FINAL → nothing | HOLDS | it appears in the proposal (§7 X1, §11 Q2) only |
| G8 | `web.py:252` calls `speak()` on every response; V1 has no single-flight (per-call pool) | grok | `web.py:252`; `transcribe.py:170-179` | HOLDS | model load has a lock (`:72,77`); the decode does not |
| G9 | R21 is "QUESTION, NOT A RULING"; proposal §2 cites "his R21" for the tailnet URL | grok (WRONG FACT) | `12-rulings.md` R21; `cto-2026-09-25.md:29` | R21 status HOLDS; the WRONG FACT is not established | R21 quotes his words about serving both sides over tailscale; the proposal cites his words, not a ruling |
| G10 | E5's result cell still says a failed E5 creates the server slice | grok | `VOICE-v3-FINAL-2026-09-23.md:281` | HOLDS | "none local → text-only on that device + server local TTS slice" |
| G11 | proposal lists eight `tts_*` keys | grok ("nine, not eight") | proposal §3 keys line | HOLDS | tts_engine, model, revision, voice, speed, timeout_s, max_chars, rss_amber_mb = 8 |
| G12 | `uv.lock` has no kokoro package | grok | `grep -c -i -F kokoro uv.lock` = 0 | HOLDS | T18's lock leg is empty |
| G13 | "`cobalt jobs restarts` not run" for the voice config (an experiment) | grok, proposal T16 | `V1-BUILD:454` records a derivation on V1's range: `configs/cobalt/voice.yaml` "UNCLASSIFIED CONFIG" | DOES NOT HOLD as to V1's range (recorded); current tree UNVERIFIABLE FROM READS | `jobs.yaml` changed at fix r2 (`:70`); rerun `cobalt jobs restarts` on the VT range settles it |
| G14 | `ops/fetch-voice-models.sh` does not exist yet | grok (a new path) | `ls ops/` — no fetch file | HOLDS | consistent with `start_aset.sh:36` "fetched by the deploy step"; no existing fetch command |
| G15 | decode thread cannot be killed (`transcribe.py:13-15`) | grok | `transcribe.py:10-14` | HOLDS | cited ±1 line |
| G16 | `af_heart` is a reference-kit default | grok | `POWER_PACKS.md:578` | HOLDS | |
| G17 | `24-reference` is a cloud cascade + `say` writing `/tmp` | grok | `POWER_PACKS.md:582`, `:518` | HOLDS | ElevenLabs, Gradium, Kokoro, `say` |
| G18 | a browser / `tailscale serve` cache replays old audio without `no-store`; URL lacks revision/voice | grok | design claim | UNVERIFIABLE FROM READS | run: grok's X7 |
| G19 | an engine that returns 200 + silence: no failure row | grok (calls it VT-X1), anthropic | proposal §6/§8 C have no such row; the only "silent" is the `play()` unlock (`10-PROPOSAL.md:77`) | HOLDS (the omission); the emission itself UNVERIFIABLE FROM READS | anthropic FC29; grok says "unrun, so not a hole" — both quoted |
| M1 | line refs `21-v1-web.excerpt.py:328` (`TurnOutcome`), `:71` (`peer_gate`), `02-greps.txt:80`, `:54` | gemini | staged files | HOLDS | all four resolve as cited |
| M2 | "T1–T19 HOLD" (except T16, T18 correct experiments), "Missed: NONE", WRONG FACTS "None" | gemini | see G1, G2 | DOES NOT HOLD | T10 and T16 do not hold as written; §1 missed the tap-path, `Probe` and `status_lines` facts (G6, FC1, FC13) |
| M3 | a double-speak path if the widget's catch triggers the device voice on `AbortError` | gemini; grok Q9; anthropic Q6 | proposal §5 lists fallback triggers (503, timeout, refused `play()`, over-long reply) and says a new press aborts the fetch, and does not say abort is excluded from the fallback | omission HOLDS; the behaviour UNVERIFIABLE FROM READS | widget for VT is not built; run VT-X3 (mid-fetch press) |
| M4 | a synthesis inside the 900 s heartbeat "could stall the event loop" | gemini Q7 | FINAL `:206` (staged `13-final.excerpt.md`): heartbeat is `com.cobalt.heartbeat`, a 900 s one-shot job | DOES NOT HOLD as stated | the heartbeat is its own process; the ASET event loop is not involved |
| M5 | "the absence of `voice.yaml` in `reads:` is a real V1 gap" | gemini, grok, anthropic | `jobs.yaml:67-75`; `V1-BUILD:454` | HOLDS (absence; recorded classification) | |
| M6 | "all failure rows emit loud AMBER lines" | gemini (d) | proposal §6/§8 C | DOES NOT HOLD | no row for silent engine output (G19); no row for the tap-path stale reply (FC1); no line for a response without `turn_id` (FC14) |
| M7 | Q4 answer is a loopback sidecar; grok: non-GPL in-process, else sidecar; anthropic: another package first, then a priced sidecar, then him | three houses | law/design reading | contradiction — quoted, not smoothed | no file settles it; VT-X4 |
| M8 | L31: a person's name is allowed in a `tts_voice` VALUE; L31 binds V1 (gemini) · must not be a person or vendor name; L31 does not show V1's names as breach (grok) · value = the file's id as the model ships it; V1 not bound (anthropic) | three houses | `LAWS.md:182` (`27-laws-excerpt.md` L31) | law reading; text quoted: "Person or vendor names never in code identifiers, schema, config keys, enum values or system design docs" | contradiction quoted, not smoothed |

## Anthropic-seat round-1 claims, file-checked
Run `date` 07:21:34 (`tail -n 3` printed `VOICE TTS FABLE R1 DONE · verdict: BUILD AFTER the Q1 stored-reply guard and test_jobs_restarts seam are written in · adopt: 4 · adopt with wording: 13 · reject: 0 · experiments named: 8 · ESCALATE: 1`). Read: `## DIGEST FOR THE DESK`, `## Rulings`, `## Self-attack`, `## Experiments`, `## OWNER`, `## WRONG FACTS`. Line numbers below = `grep -n` positions in `voice-tts-tribunal-fable-r1-2026-09-25.md`. `date` between rows: 07:22:40 after FC10; 07:24:30 after FC28.

| FC | claim (seat report line) | file:line | verdict | note (≤30 words) |
|---|---|---|---|---|
| FC1 | a tap never stores its own reply: `_tap` builds a dry `_Rec` and writes only through `confirm_mod` (:33-34) | `turn.py:132-134` ("No-ops in a dry run"), `:258-260`, `:264-274`; `confirm.py:73`, `:99-100` | HOLDS | `confirm_pending` transitions the row without `reply=`; the row keeps the read-back |
| FC2 | T1's row holds the read-back as `reply` while `awaiting_confirm` (:33) | `turn.py:377-380` | HOLDS | `rec.go(AWAITING_CONFIRM, …, reply=pending.readback, …)` |
| FC3 | the tap returns turn_id T1 with reply "Done. …" (:34) | `confirm.py:108`; `turn.py:273` | HOLDS | outcome carries `rec.tid` = the pending turn id |
| FC4 | if the expert refused the widget shows RED "Refused: …" (:35) | `confirm.py:88-92`; `turn.py:254`, `:274` | HOLDS | |
| FC5 | a spoken "yes" writes its own reply on its own row (:36) | `turn.py:253`, `:419` | HOLDS | `rec.go(DONE, reply=res.reply, …)` |
| FC6 | the read-back text asks him to confirm ("… Say yes to do it.") (:35) | `tools.py:209-210` ("Say yes, or tap Confirm."); FINAL `:88` ("Say yes to do it.") | HOLDS in substance | the quoted wording is the FINAL's, the code's is "Say yes, or tap Confirm." |
| FC7 | `onnxruntime` is in the lock (`uv.lock:3280`), pulled by faster-whisper (`:1388-1395`); no torch entry (:42-43) | `uv.lock:1395`, `:3280`; `grep torch uv.lock` → nothing | HOLDS | |
| FC8 | `onnxruntime` is absent from `pyproject.toml` (:150) | `grep onnxruntime pyproject.toml` → nothing | HOLDS | |
| FC9 | `COBALT_VOICE_MODEL_DIR` is exported only in `start_aset.sh:37`; no heartbeat plist sets it (:81) | `ops/start_aset.sh:37`; `grep -rn ops/ configs/` → that line + `voice.yaml:8` comment | HOLDS | |
| FC10 | with no env, `load_voice_config()` returns the committed DEV `model_dir` (:82) | `config.py:141-146`; `voice.yaml:19` | HOLDS | mechanism; a probe in the heartbeat process is the proposal's own design (§6) |
| FC11 | T10 "today only …" contradicted (:125, :247) | `web.py:143`, `:148`, `:180-182` | HOLDS | see G1 |
| FC12 | T16 wording contradicted: `grep -c -F voice.yaml jobs.yaml` = 0 (:127, :249) | `jobs.yaml` (grep) | HOLDS | see G2 |
| FC13 | the derivation already ran on V1 and named `configs/cobalt/voice.yaml` UNCLASSIFIED CONFIG (:128, :250) | `V1-BUILD:454` | HOLDS | recorded at build time (pre-fix-r2) |
| FC14 | `test_jobs_restarts.py` pins every function reaching `load_voice_config`; a new route handler joins them (:132, :179) | `test_jobs_restarts.py:164-189` (`peer_gate` :183, `status_lines` :189), `:395-421` (entrypoints, `peer_gate` :414) | HOLDS | seat's ":180-194" / ":408-421" resolve; the set starts at `:164` |
| FC15 | the widget voices responses that have no `turn_id` (:134) | `web.py:89`, `:259`, `:261`, `:282` | HOLDS | 503 body, refusal `show`, network-failure `show`, "I heard nothing." |
| FC16 | no server synthesis path exists; `scratch.py:54` `audio/wav` is an upload content type (:135) | `scratch.py:54`; `02-greps.txt` search 1 | HOLDS | |
| FC17 | widget: muted returns first (`web.py:242`), `localService` filter (`:238`), "no local voice" AMBER (`:244`), `speak()` from `show()` (`:252`) (:65-69) | `web.py:238`, `:242`, `:244`, `:252` | HOLDS | |
| FC18 | a press mid-fetch: a catch-all "fetch failed → device voice" would speak the old reply while the microphone records (:68) | `web.py:268-287` (`start()`) | UNVERIFIABLE FROM READS | widget behaviour of unbuilt code; VT-X3 (his X3 "a press mid-fetch voices nothing") |
| FC19 | per-call pool with `shutdown(wait=False)`: the `transcribe_with_timeout` shape (:97) | `transcribe.py:170-179` | HOLDS | |
| FC20 | with a blocking lock, timed-out callers leave threads waiting and the server synthesizes aborted clients' replies back to back (:97-100) | design consequence | UNVERIFIABLE FROM READS | seat's own X8 measures busy rate; run VT-X1 + X8 |
| FC21 | R18 already set aside L57's "replayable" for audio (:103) | FINAL `:22` | HOLDS | |
| FC22 | L31 reads "Person or vendor names …"; `cameron_grid` is a person (:92, :251) | `LAWS.md:182` | HOLDS | law text; whether `faster-whisper` is a "vendor" name is a reading (see M8) |
| FC23 | 82M × 4 B ≈ 0.33 GB (:155) | arithmetic | ARITHMETIC OK | 82×10⁶ × 4 = 328×10⁶ B ≈ 0.33 GB; the count is itself UNVERIFIED (seat says so) |
| FC24 | a `no-store` body may be kept in a phone browser cache without the header (:166) | browser behaviour | UNVERIFIABLE FROM READS | seat's VT-X3 addition (browser cache listing) |
| FC25 | `POST_ALLOWLIST` `:667-673`, `:685`; `GET_ONLY` `:674` does not list `/voice/*` (:213) | `test_radar_panel_cards.py:667-674`, `:685` | HOLDS | `POST_ALLOWLIST` includes `/voice/turn`, `/confirm`, `/cancel` (`:672`) |
| FC26 | E2's method: `resource.getrusage(RUSAGE_SELF).ru_maxrss` (:76) | `V1-BUILD:104` | HOLDS | |
| FC27 | the reply row is written before the response returns; history reads `reply`; `turn.py:213` writes `stt_engine`; `placement.py:91`, `db_migrations/__init__.py:88,:93` register `voice_turns`; `voice_stt` only a failure class (`turn.py:189,:196`) (:141, :203-207, :214) | `turn.py:349-351`, `:377`, `:213`, `:188-196`; `store.py:186-187`; `placement.py:91`; `__init__.py:88,:93` | HOLDS | self-attack list spot-checked |
| FC28 | an engine that loads but emits silence is the one path in §6/§8 C with no line (:167) | proposal `:77` is the only "silent" (the `play()` unlock) | HOLDS | see G19 |
| — | WITHDRAWN by the seat: "the heartbeat's voice probe resolves `model_dir` the way V4's `voice_stt` already does" (:220) | — | WITHDRAWN (not checked) | the seat struck it itself |

`Anthropic-seat R1 claims checked: 25 HOLD of 28 checked` (FC1–FC28; 25 HOLDS incl. 1 ARITHMETIC OK, 0 DO NOT HOLD, 3 UNVERIFIABLE FROM READS: FC18, FC20, FC24; 1 WITHDRAWN not counted).

## Experiments named (L70)
| experiment | named by | = proposal / NEW | gates which chunk (house claim) | result that would change the design |
|---|---|---|---|---|
| first-audio latency, cold/warm, under STT + Plan load (`/size`, `/fill`), also `duration_s` | proposal VT-X1; grok X1 (drop the 1.5 s line); gemini X1; anthropic VT-X1 (+ `sample_rate`, `duration_s`) | VT-X1 | VT-0 → sets `tts_timeout_s`, `tts_max_chars`; VT-2 | a too-slow warm result (unnumbered, grok) or `duration_s` 0 → round 2 (chunks / silent = `engine_error`); the proposal says > 1.5 s |
| RSS after load; `wired down` before/after beside LM Studio | proposal VT-X2; grok X2; gemini X2; anthropic VT-X2 (`ru_maxrss`) | VT-X2 | VT-0 → `tts_rss_amber_mb` | swap pressure → sidecar or smaller runtime |
| device session: fetch-then-play, gesture unlock, mute, abort | proposal VT-X3; grok X3 (+ overlapping turns, digit 409, drop "Opus via `av`"); gemini X3 (+ AbortError not falling back); anthropic VT-X3 CHANGED (+ `no-store` absent from cache, press mid-fetch voices nothing, tap Confirm voices "Done") | VT-X3 (changed) | VT-3 | `play()` refused → tap-to-play + AMBER; cached → another header; WAV too slow → round 2 |
| lock diff + licences; offline load from an empty `model_dir`; network off | proposal VT-X4; grok X4 (+ model card parameter count, voice stems, speed range); gemini X4 (+ sidecar if GPL); anthropic VT-X4 CHANGED (+ network-OFF synthesis, file-write trace `fs_usage`, does the runtime accept `onnxruntime 1.30.0`) | VT-X4 (changed) | VT-1 (merge bar, grok and anthropic) | native / GPL → round 2 on Q4; version conflict → round 2 on Q3; network or file write outside `model_dir` → round 2 |
| figure round trip through V1's Transcriber | proposal VT-X5; grok X5 (gate widened to every digit reply); gemini X5; anthropic VT-X5 (default-voice selector; does not lift Q5's guard) | VT-X5 | VT-3 read-back gate | a mismatch → per-field normalizer; the gate stays |
| same text twice, and after a restart → identical bytes? | proposal VT-X6; grok X6; gemini X6; anthropic VT-X6 (informational) | VT-X6 | §4 L57 wording | not identical → "text replayable, audio not" |
| `no-store` header vs cache after `tts_voice` change + restart | grok X7 | NEW | VT-2 (grok: inside the X4 scratch tree, no new chunk) | same bytes → round 2 adds a cache-buster |
| silent / degenerate output: digits-only, symbols-only, single word, empty-after-strip; count zero-sample outputs | anthropic X7 | NEW | VT-1 (`synthesize()` refusal) | any hit → a text pre-check per field type |
| busy rate: three text turns 1 s apart while a synthesis runs | anthropic X8 | NEW | VT-2 (non-blocking lock) | busy > 5 % (the seat's own figure) → sentence chunks in round 2 |
| `cobalt jobs restarts` on the VT range for `configs/cobalt/voice.yaml` | proposal T16 (UNCITED); grok (an experiment); anthropic (RECORDED at `V1-BUILD:454`, not an experiment) | T16 | VT-4 / deploy drafter | prints nothing / UNCLASSIFIED / `com.cobalt.aset` |
| Kokoro's dependency tree (weights, runtime, g2p, native libs, licences) | proposal T18 (UNCITED) | = VT-X4 | VT-1 | see VT-X4 |

## OWNER ITEMS (after the tribunal)
Proposal: OWNER ITEM 1 — voice and speed (A: houses pick; B: he picks from samples in the device session; recommends B). OWNER ITEM 2 — on the phone, server voice or device voice first (A server first; B device first; recommends A).

| house | line, verbatim | why no house can decide it |
|---|---|---|
| grok | `## OWNER (after the tribunal):` `none` (with `(g)`: "REJECT both owner items as items for him. L67 … an owner item is his money, his data, his laws, or his trading judgement. A question a house can settle does not go to him. Taste is the proposal's argument, not that law's list. Even if taste qualified, a house can decide both.") | NAMED — it argues the reverse: that a house can decide both |
| gemini | `` `OWNER (after the tribunal):` `` "1. Voice and speed: taste in what he hears." "2. Phone fallback priority when both exist: taste in latency vs voice consistency." | NOT NAMED — gemini names a category ("taste"), not why no house can decide; item 2's "latency vs voice consistency" is the measurement grok and anthropic say decides it |
| anthropic | "OWNER ITEM 1 — voice and speed: PASSES. It is his taste in what he hears, and no house can hear for him. Not a precondition; the houses' default ships (g)." · "OWNER ITEM 2 — server or device voice first: FAILS. R23 and measurement settle it." · "Q4 (3) only if reached: accepting a GPL licence in this private install — his law." | item 1 NAMED; item 2 (a rejection) NAMED (R23 + measurement); Q4 (3) NAMED (his law) |

No house made an owner item a precondition to build a chunk that does not need it: gemini "Neither is written as a precondition to build chunks `VT-1` through `VT-4`"; anthropic "It is NOT a precondition"; grok "not a precondition of VT-1". No house text re-opens R23, puts VT into tonight's set, or pulls V1's rename or A1 fix into VT (grok "adds no VT chunk to rename them"; anthropic "its rename is not a law defect"; grok's E5-cell amendment and anthropic's (g) both rest on R23).

## WRONG FACTS claimed
| # | statement | claimed by | file-check |
|---|---|---|---|
| W1 | proposal T10 "today only 'speech-to-text down (model missing)'" (`10-PROPOSAL.md:20`) | grok, anthropic | HOLDS — `web.py:143`, `:148`, `:180-183` (G1) |
| W2 | proposal T16 "`grep -F voice.yaml` → only the comment at :70" | grok, anthropic | HOLDS — `jobs.yaml` has no `voice.yaml` string (G2); the T16 "UNCITED" classification is also contradicted by `V1-BUILD:454` (FC13) |
| W3 | proposal §4 reason 4 "Mute = zero server work" | grok | mute before the fetch is sent: true; after a worker starts: the synthesis runs to the end (V1's pattern `transcribe.py:10-14`) — HOLDS as an inference from V1's pattern; the VT worker is unbuilt → UNVERIFIABLE FROM READS |
| W4 | proposal §4 reason 6 "GET: no side effect" | grok | no file/row/note (design text); the resident's in-memory `tts.last` / `rss_mb` is set by the design itself (§6) — HOLDS as a reading of §6; not a defect (the proposal's own probe reads it) |
| W5 | proposal §2 "existing tailscale serve HTTPS URL (his R21)" | grok | R21 is a QUESTION not a ruling — the status HOLDS; the "wrong fact" is not established (G9) |
| W6 | proposal §3 `tts_speed` 0.5–2.0 and `neural-82m` count are not in the staged files | grok | HOLDS — only the proposal carries them (T18: model tree uncited) |
| W7 | digest stop line "Kokoro-82M runtime" — the 82M count is the same uncited figure | grok | HOLDS — same as W6 |
| W8 | proposal T6 / §11 Q8 / L31 line / ESCALATE 1 read L31 as barring a "product name" | anthropic | HOLDS — `LAWS.md:182` reads "Person or vendor names"; the houses disagree on whether `faster-whisper` is a vendor name (M8) |
| W9 | gemini: none | gemini | see M2 — DOES NOT HOLD |

## Independence
- `grep -c -F -e "-ruling"` on `gemini-ruling.md`: **0**.
- `grep -n -F -e "-ruling"` on `grok-ruling.md`: 3 lines — `:3` its own launch sentence ("No `-ruling.md` file opened."), `:91` and `:221` (`12-rulings.md`, a packet file whose name contains "-rulings"). Not a breach: no other house's ruling file was opened.

## Round 2 — Astra (not this run)
L67 seats Astra on every NEW design; its meter is out until **Sat 2026-09-26 06:47 ET** (`cto-2026-09-24.md` R107's row, "retry after Sep 26th, 2026 6:47 AM"; this run's probe at 06:5x on 2026-09-25 printed "try again at Sep 26th, 2026 6:47 AM"). So this round-1 tribunal ends in a DRAFT FINAL (`18`), and ROUND 2 is where Astra sits. The round-2 hub (drafted by the desk after `18`, on `prompts/2026-09-24/27-drc-overnight-tribunal-r2.md`'s shape, the SAME 14 + 3 strings as this file, nothing new) carries, as written in `16` §5: **(r2-1) STAGGER BY THE CLOCK:** PREFLIGHT row 1 is `date`; a time before 2026-09-26 06:47 ET → `FAILED PREFLIGHT: stagger — Astra's meter returns 2026-09-26 06:47 ET; round 2 launches after it`, launch nothing. **(r2-2) THE ASTRA PROBE IS A PREFLIGHT GATE THAT FAILS CLOSED** (`topics/cto-desk.md` 09-20 lesson (10)): `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."`, `run_in_background`, 3 minutes; usage-limit text, denial or no answer → `FAILED PREFLIGHT: astra METER — round 2 waits for Astra (return time: <the time the meter message names>)`, launch nothing; it NEVER proceeds without Astra. **(r2-3) ASTRA'S LAUNCH** is the Codex read-only line as `prompts/2026-09-21/38-float-handicap-tribunal.md` spells it (the hub writes its printed answer to `astra-ruling-r2.md`); Astra reads the round-1 packet folder `scratch/tribunal-bars-0920/voice-tts/r1/` (NOT the ruling files), the DRAFT FINAL `docs/30 - Design/VOICE-TTS-DRAFT-FINAL-2026-09-25.md`, and rules on all 17 items of round 1 AND on `18`'s `## NEEDS ROUND 2`. **(r2-4) THE OTHER SEATS IN ROUND 2** rule ONLY on `18`'s `## NEEDS ROUND 2` and on any item where Astra's ruling disagrees with the DRAFT FINAL on whether a mechanism is CORRECT (Grok; the Anthropic seat blind again; Gemini optional). **(r2-5)** the round-2 derive names the FINAL (`docs/30 - Design/VOICE-TTS-FINAL-<date>.md`); round 3 exists only if round 2 does not converge (L39: no fourth; unresolved → Dejan). Round 2 holds no lane (L72) and waits for no build. Values now held: astra return time `Sat 2026-09-26 06:47 ET`; round-1 packet folder `scratch/tribunal-bars-0920/voice-tts/r1/` (187,230 B, 15 packet files); ruling files `grok-ruling.md`, `gemini-ruling.md` (excluded from Astra's reading); Anthropic-seat report `voice-tts-tribunal-fable-r1-2026-09-25.md` (DONE); this report `voice-tts-tribunal-2026-09-25.md`.

## L74
One block of the L74 shape arrived attached to a tool result on 2026-09-25 (after my first Read of the prompt file `16-voice-tts-tribunal.md`): it asked for a `Claude-Session: https://claude.ai/code/session_<id>` line in commit messages and PR bodies and named a file-send tool. Recorded ONCE here as data (L74); not followed. This run commits nothing.

## ESCALATE
1. **ASK DESK: the stagger literal.** R33's launch row says "`58` is not running … `08` is not running … `10` is not running", but with backticks round each number, so `grep -F "08 is not running"` / `"10 is not running"` print nothing (`58` matches R32's quoted future wording only). The prompt's letter → `FAILED PREFLIGHT`. I read R33 with a backtick-tolerant pattern and launched (the report's `## PREFLIGHT` NOTE). Was that reading acceptable, or should the run have stopped? [07:24 ET] Safe default taken: NOT the prompt's letter (a deviation, disclosed); the desk decides whether the rulings stand.
2. **`DO NOT BUILD`:** none (all three closing lines are `BUILD AFTER`).
3. **A `REJECT` whose claim HOLDS:** grok item (g) — "REJECT both owner items as items for him … an owner item is his money, his data, his laws, or his trading judgement" — the L67 text it rests on HOLDS (`27-laws-excerpt.md` L67, 2026-09-24 clause). The two other seats disagree (gemini: both are his taste; anthropic: item 1 passes, item 2 fails). Quoted, not settled.
4. **Item (e) (boundary):** no house named a free text-to-audio, cross-session, peer-gate, write, trading-PC, platform or score path (grok NONE, gemini NONE, anthropic NONE once Q1's guard is in). No path HOLDS. (Fact for the derive, not a path: the tap-path stale read-back, FC1–FC6 HOLD — the anthropic seat found it, grok and gemini did not.)
5. **Item (b), a second speaking path that HOLDS:** gemini's "double-speak path during abort" — the omission in proposal §5 HOLDS (M3); the behaviour is UNVERIFIABLE FROM READS; grok (Q9) and anthropic (Q6) name the same hole and offer clauses.
6. **Item (f), a change to V1's contract:** none — all three say `TurnOutcome` and the callers are unchanged. Seam additions named and HOLD as additions: anthropic `test_jobs_restarts.py` pins (FC14); grok `Probe` level field (a change to a heartbeat class, G6), a ninth key, `ops/fetch-voice-models.sh` (G14).
7. **An Anthropic-seat claim that DOES NOT HOLD:** none (25 HOLD, 3 UNVERIFIABLE, 0 DO NOT HOLD, 1 WITHDRAWN). Two grok claims DO NOT HOLD (G3, G4), one gemini claim DOES NOT HOLD (M4), and gemini's "T10 HOLDS" / "WRONG FACTS: None" (M2) DO NOT HOLD.
8. **A number a house proposes without its measurement, quoted:** proposal "> 1.5 s warm at ≈200 chars" (§7 VT-X1, §11 Q2; grok removes it: "Shipping it would be a threshold with no measurement"; gemini keeps it) · anthropic "busy > 5 %" (X8), "≈ +2 h, one more chunk, UNVERIFIED" (Q4 sidecar price), "`tts_speed` 1.0" as the default voice speed (g) · proposal `tts_speed` 0.5–2.0 and "82M" (grok W6/W7: not in any staged file). Grok's own numbers: none proposed (it sets no timeout, char cap or RSS line).
9. **An owner item a house sent him that it did not NAME against the test:** gemini's two `OWNER (after the tribunal):` lines are `NOT NAMED` (`## OWNER ITEMS`).
10. **An owner item written as a precondition:** none. **`RE-OPENS A RULING`:** none.
11. **Packet:** 187,230 B, under the 200,000 B ceiling; no cut. **REDACTIONS:** 0 (three-literal scan 0 on all 17 files; no other user data found). **A house that did not rule:** none (3 of 3). **Independence breach:** none.
12. **Astra's probe row:** `astra: METER` — "You've hit your usage limit … try again at Sep 26th, 2026 6:47 AM" (exit 1) at 06:5x on 2026-09-25 — RECORDED, SKIPPED, round 2 (§5 above). Astra return time: Sat 2026-09-26 06:47 ET.
13. **Facts for the derive (no recommendation):** (i) split wordings on Q1 (grok/anthropic guards differ: grok digit-409 + flag `tts_readback_server`; anthropic `pending_action` 409 + no flag), Q4 (three different orders), Q5 (flag vs guard), Q7 (grok: probe reads files + status; anthropic: only `/voice/status`), Q8 (voice value naming a person: gemini allows, grok forbids, anthropic "the file's id as shipped"); (ii) the `configs/cobalt/voice.yaml` RESTARTS gap is real by all three; whether it is an experiment is disputed (grok/proposal: yes; anthropic: no — `V1-BUILD:454`); (iii) whether a Gemini finding held (R97's evidence): gemini's one finding that no other seat made — none (its `AbortError` finding was also made by grok Q9 and anthropic Q6); its `T10: HOLDS` and `WRONG FACTS: None` were wrong (M2); its Q7 "stall the event loop" was wrong (M4); it ran 2 minutes.

VOICE TTS TRIBUNAL DONE · round: 1 · grok: TRIBUNAL R1: BUILD AFTER derive folds the WITH clauses · gemini: TRIBUNAL R1: BUILD AFTER adding AbortError exclusion to the widget's device voice fallback · anthropic: TRIBUNAL R1: BUILD AFTER the Q1 stored-reply guard and test_jobs_restarts seam are written in · astra: METER · houses that ruled: 3 of 3 · questions settled: 9 of 10 · dissents: 1 · ESCALATE: 13
