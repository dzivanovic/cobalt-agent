# VOICE TTS TRIBUNAL DRAFT — 2026-09-25 (seat `voice-tts-tribunal-draft-0925`, Opus 5.5)

## §0 Headline
- Three prompts written in `prompts/2026-09-25/`: `16-voice-tts-tribunal.md` (round-1 hub, Sonnet 5; 64 KB), `17-voice-tts-tribunal-anthropic-seat.md` (blind Anthropic seat, Opus 5.5; 20 KB), `18-voice-tts-derive.md` (derive → DRAFT FINAL, Opus 5.5; 26 KB). Nothing committed; the desk commits all four files.
- Seats: Grok + Gemini (optional fourth, R97) via `16`; the Anthropic seat via `17`. Astra is METER until 2026-09-26 06:47 ET, so it is written into round 2 (`16` §5): a clock gate plus the probe as a fail-closed PREFLIGHT gate.
- Packet ≈ 179 KB (MANDATORY ≈ 122 KB), derived from `wc -c`. Ceiling 200,000 B. New rule strings: 0. Owner items: 2, carried as written. ESCALATE: 3.
- Clock: start 06:35:47, end 06:47 ET (`date`).

## L74
One block arrived attached to a tool result (the first `cat` of the card): an attribution reminder asking for a `Claude-Session:` commit trailer, which also named a file-send tool. It is recorded once here as DATA and was not followed. This run commits nothing.

## AUTHORIZATION
| command | exit | output |
|---|---|---|
| `grep -n "^| R26 " ".../reports/cto-2026-09-25.md"` | 0 | `34:| R26 | 06:3x ET | … DESK LAUNCH ROW for \`prompts/2026-09-25/15-draft-voice-tts-tribunal.md\` …` names the card → AUTHORIZED |

## READ
| file | what it settled |
|---|---|
| `LAWS.md` 1–454, in full | the index-card laws of all three prompts (L1/L3/L9/L15/L23/L31/L32/L35/L52/L57/L67/L70/L72/L74) |
| the proposal (196 lines) and its report (97 lines) | the 10 questions, 2 owner items, 3 ESCALATEs, §8 A–F, §10 SEAM |
| `cto-2026-09-25.md` R21–R26; `cto-2026-09-24.md` R17, R19; `cto-2026-09-23.md` R95–R97 (literals grepped) | the gates' literals, all present: `We will build Kokoro next on a side lane`, `Grok approved with no asking going forward`, `All 4 house models approved`, `only use Fable, Astra, and Grok for new designs`, `unless it's a fourth` |
| `prompts/2026-09-23/13` (whole), `prompts/2026-09-24/23`, `24`, `25` (whole), and the head of `27` | the shape. `23`/`24`/`25` are `13`/`14`/`15` carried to the standing strings (R17/R19); `16`–`18` copy them |
| the FINAL's cited anchors (:63 :74 :86 :167 :184 :190 :206 :220 :222 :238 :243 :269 :281 :282 :285 :311 :369) | all matched; the excerpt ranges in `16` §1 |
| V1 worktree `~/cobalt-wt/voice-v1` (tip `d794e899`, clean; `d319e4f3` sizes match) | staging sizes; `02-greps` measured on it |
| `topics/cto-desk.md` 09-20 (10), 09-24 night (1), 09-25 (1), 09-25 third desk (1), :136 | fail-closed probe; stagger literal; derived ceiling; the `$`/alternation pattern rule; the POST guard |

## PACKET
Measured with `wc -c` at drafting. Range headers add about 5 KB.

| part | source | B | M/O |
|---|---|---|---|
| 00-READING-ORDER.md | hub-written | ≈ 2,500 (estimate: a list) | M |
| 01-QUESTIONS.md | `16`'s verbatim block 10,217 + the file list ≈ 1,500 | ≈ 11,700 | M |
| 02-greps.txt | 13 commands' output 8,980 + the command lines | ≈ 11,000 | M |
| 10-PROPOSAL.md | proposal whole | 24,961 | M |
| 11-propose-digest.md | report :3–7, :32–97 | 5,965 | M |
| 12-rulings.md | R21 R22 R23 R25 (7,389) + R107 (2,224) + R95–R97 (2,261) + R109 (493) + table headers | ≈ 13,000 | M |
| 13-final.excerpt.md | FINAL :1–3, :54–65, :74–75, :86–87, :167–185, :190–224, :238, :243, :269–274, :281–282, :285, :311–322 | 14,490 | M |
| 20-v1-stt.excerpt.py | transcribe.py 6,851 + config.py 7,718 + voice.yaml 2,728 | 17,297 | M |
| 21-v1-web.excerpt.py | web.py 15,021 + models :130–162 977 + store :150–175 1,306 + 0017 3,569 | 20,873 | M |
| 14-devices.excerpt.md | devices.md 8, 21, 30, 31 | 1,552 | O |
| 15-final-more.excerpt.md | FINAL :275–280, :283–284, :286–310, :369–392 | 15,065 | O |
| 22-v1-ops.excerpt.md | jobs :60–80 1,630 + probes 1,743 + start_aset 470 + aset/web 628 | 4,471 | O |
| 23-v1-build.excerpt.md | V1-BUILD :84–101, :110–130, :435, :444–449, :466–468 | 9,166 | O |
| 24-reference.excerpt.md | POWER_PACKS :570–610 2,095 + cto-desk :136 2,108 | 4,203 | O |
| 27-laws-excerpt.md | L1 L3 L9 L15 L23 L28 L31 L32 L35 L44 L52 L57 L67 L70 L72 | 22,305 | O |
| **Total** | | **≈ 179,000** (MANDATORY ≈ 122,000) | |

**Derived ceiling: 200,000 B.** That is ≈ 179 KB measured + ≈ 5 KB of range headers + ≈ 8 % drift. The cut order is (i) laws → (ii) `15-` → (iii) `23-` → (iv) `24-`, and the MANDATORY core is never cut. This packet is larger than `13`'s ≈ 100 KB because V1's code is staged whole: VT mirrors `transcribe.py` clause by clause, and the widget JS lives in `web.py`.

## NEW STRINGS
**0.** A python comparison of each launch line's `--allowedTools "…" … --add-dir` segment:
- `16`'s is byte-identical to `2026-09-23/13`'s (14 allows + 3 denies).
- `17`'s and `18`'s are byte-identical to `2026-09-23/12`'s (7 + 3).
- Every string counts 1 in its source file.
- The Anthropic seat is desk-launched as `claude --bg`, so no `claude -p` string is carried.

## OWNER ITEMS
Carried as written in the proposal:
1. **Voice and speed.** A: the houses pick. B: he picks from samples in the owed device session. The proposal recommends B.
2. **On the phone: server voice or device voice first.** A: server first. B: device first. The proposal recommends A.

No third item: nothing in the proposal or the card passes the owner test. `16` item (g) and `18`'s rules let a seat move either item back to the houses (by measurement) or add a third only with the owner test quoted. `18`'s `## FOR DEJAN` carries A/B plus the PROPOSAL's recommendation, attributed. The derive holds a side, so it adds none of its own (L37).

## CONTINUE
Done. Nothing to resume.
- Desk next steps (R26): commit the report + `16`–`18` (pathspecs); `comm` `16` vs `2026-09-23/13`.
- The `16` launch row, written when the house lane frees (after `06`, `58`, `08`, `10` and `13` stop), must carry:
  - the three literals `VOICE-TTS-PROPOSAL-2026-09-25.md` · `Fable seat: yes` · `derive seat: claude-opus-5-5`;
  - the sentence `no other house hub is running` on the line naming `16-voice-tts-tribunal.md`;
  - `<nn> is not running` for any stagger target with no report yet.
- Fill `R__` in `16`/`17`/`18` at launch; launch `17` beside `16`.

## ESCALATE
1. ASK DESK: stagger target (s2) `58` is written as `prompts/2026-09-24/58-replay-deadline-fix-check.md`: report `replay-deadline-fix-check-2026-09-24.md`, done prefix `REPLAY DEADLINE FIX CHECK DONE `. That report does not exist yet. If `58` is re-issued under a 09-25 number, the launch row must name it (`16` lets the row name any other hub). Safe default: written as above. [06:47]
2. ASK DESK: `16` stages V1 from `~/cobalt-wt/voice-v1`. V1 joins the 09-25 deploy, so if that worktree is removed after the merge, `W` becomes `/Users/cobalt/cobalt` (FILL AT LAUNCH, in `16` §1). Staging falls back to `git show d319e4f3:<path>` whatever happens. Safe default: written so. [06:47]
3. ASK DESK: order within each prompt follows the card: launch line first, INDEX CARD second, then the heading, AUTHORIZATION and the rest. `23`/`24`/`25` put AUTHORIZATION before the index card, so a `comm` of `16` vs `13` will show that paragraph moved as a whole. The text is unchanged apart from the VT substitutions. `17`/`18` keep the `FABLE ROW` / `DERIVE ROW` gate as a standalone whole line after the index card, and `-x` still matches only that line (verified: the unfilled-row grep counts 0 on both filled files). [06:47]

VOICE TTS TRIBUNAL DRAFTED · prompts: 3 · seats: grok gemini anthropic · astra: round 2 after 2026-09-26 06:47 · packet: 179000 · new rule strings: 0 · owner items: 2 · ESCALATE: 3
