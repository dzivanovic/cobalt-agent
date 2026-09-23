# VOICE v3 round-2 draft — 2026-09-23

Seat `voice-v3-r2-draft-0923` · model `claude-opus-5-5` (R36 / R109) · prompt `prompts/2026-09-23/23-draft-voice-v3-r2.md`. First `date` 10:04 EDT; prompts written by 10:12 EDT; report written 10:12 EDT (times from `date`).

## §0 Headline
- Wrote three prompts for round 2 of the VOICE v3 tribunal, covering the derive's R2-1, R2-2 and R2-3 only: `24` (house hub: Grok + Gemini), `25` (Anthropic seat, blind), `26` (second derive → `VOICE-v3-FINAL-2026-09-23.md`).
- The three launch lines are byte-identical to `13` / `14` / `15`. Only the prompt path and the remote-control name differ. New rule strings: 0.
- `24` shares the house lane with the routing X5 hub (`19`, running at drafting). It launches only once `19` is PAUSED through the desk's `scratch/tribunal-bars-0920/routing-x5/PAUSE` file.
- ESCALATE: 6. Two items need the desk: whether R28 covers `24`, and the choice of round 3 over his A/B for a split.

## Prompts

| file | seat · model | launch line = | report · stop line |
|---|---|---|---|
| `prompts/2026-09-23/24-voice-v3-tribunal-r2.md` | hub `voice-v3-tribunal-r2-0923` · Sonnet 5; houses Grok + Gemini; Astra probe carried (09-22 R13) | `13`'s 14 allow + 3 deny, byte for byte | `reports/voice-v3-tribunal-r2-2026-09-23.md` · `VOICE V3 TRIBUNAL R2 DONE · grok: … · gemini: … · astra: … · houses that ruled: <n> of 3 · converged: <n> of 3 · ESCALATE: <n>` |
| `prompts/2026-09-23/25-voice-v3-tribunal-r2-fable-seat.md` | seat `voice-v3-tribunal-fable-r2-0923` · Opus 5.5 (FABLE ROW R109), blind | `14`'s 7 allow + 3 deny | `reports/voice-v3-tribunal-fable-r2-2026-09-23.md` · `VOICE V3 TRIBUNAL FABLE R2 DONE · R2-1: … · R2-2: … · R2-3: … · ESCALATE: <n>` |
| `prompts/2026-09-23/26-voice-v3-derive-r2.md` | derive `voice-v3-derive-r2-0923` · Opus 5.5 (DERIVE ROW R109) | `15`'s 7 allow + 3 deny | `reports/voice-v3-derive-r2-2026-09-23.md` (+ `docs/30 - Design/VOICE-v3-FINAL-2026-09-23.md` only at 3 of 3 converged) · `VOICE V3 FINAL DERIVED · converged: <n> of 3 · round 3: <n> · O1: <open\|ruled A\|ruled B\|ruled No> · FINAL: <written\|not written> · ESCALATE: <n>` |

How the byte identity was proven: each launch span, from `claude --bg` to the last `--add-dir`, was compared as a string against its parent's with the path and the remote-control name normalized. `24=13`, `25=14`, `26=15`. Each rule string also counts ≥1 in `prompts/2026-09-20/08-bars-chunk-e-check.md` (for `24`) and in `prompts/2026-09-21/22-draft-setups-tribunal.md` (for `25` / `26`).

## The packet and the items

| item | positions put to the houses (verbatim from the derive report / derived design) | sub-points |
|---|---|---|
| R2-1 scratch deleter | A: grok / gemini (derived §5 bullet, heartbeat sweep in V4) · B: Anthropic seat T8 (voice module sweeps at aset start + turn start; the probe COUNTS; cross-key refusal) | (a) the heartbeat process as a second deleter under L40 · (b) the cross-key refusal · (c) how long a leftover sits with no turn, and R18 (b) · (d) V4's probe and §9 row |
| R2-2 O1 mechanics | P: the proposal's fold mechanics (grok: "correct and minimal") · S: the seat's (span-bound sha, no retry, span changed, "remains his") — the SCOPE clause is excluded | (a) span vs diff · (b) note vs span, and the `_commit` guard · (c) "takes no retry" in the law · (d) "remains his" vs the baseline code · (e) law vs §2.6 · then `FOLD A:` / `FOLD B:` paste-ready texts for both scopes |
| R2-3 HITL-draft slice | A: a named slice builds it (slice, change, files, hours, RESTARTS, what a request gets before it ships) · B: §2.4 stands with no slice — the seat's "refuse until built" is excluded (RE-OPENS R18) | the L40 owner of APPLYING a trading-logic change |

Packet estimate: ≈ 74 KB measured over the staged ranges (derived design 29.8 KB · code 24.3 KB · seat R1 6.5 KB · grok R1 4.4 KB · derive NEEDS 4.1 KB · hub rows 3.4 KB · gemini R1 1.4 KB), plus `greps.txt` and QUESTIONS-R2 at ≈ 15–25 KB (a GUESS) → ≈ 85–100 KB. `24` states a drop order above 110 KB.

## Launch rows for the desk (fill `R__`)

| R__ | <time> ET | — NO WORDS OF HIS BEYOND R18 / R28 / 09-22 R13 / 09-22 R109: DESK RECORD + LAUNCH ROWS. (1) PAUSE written `scratch/tribunal-bars-0920/routing-x5/PAUSE` at <time>; `19` paused (its `## CONTINUE` shows `paused by the desk`). (2) LAUNCH `24-voice-v3-tribunal-r2.md` (Sonnet 5 hub `voice-v3-tribunal-r2-0923`, cwd `agy-trial`; Grok + Gemini; Astra probe carried, R13; line = `13`'s byte for byte; grok / agy per R28 through 2026-09-24 23:59 ET). Stagger literals for `24-voice-v3-tribunal-r2.md`: 20 is not running · 53 is not running · 54 is not running · 55 is not running · 56 is not running · 57 is not running · no other house hub is running. (3) LAUNCH `25-voice-v3-tribunal-r2-fable-seat.md` (Opus 5.5, FABLE ROW R109, the seven read strings; not a house hub). | DESK LAUNCH — no fold |

| R__ | <time> ET | — NO WORDS OF HIS BEYOND 09-22 R109: DESK RECORD + LAUNCH ROW. `24` STOPPED `VOICE V3 TRIBUNAL R2 DONE …` and `25` STOPPED `VOICE V3 TRIBUNAL FABLE R2 DONE …`, both committed. PAUSE deleted; `19` relaunched with one `CONTINUE:` line. LAUNCH `26-voice-v3-derive-r2.md` (Opus 5.5, DERIVE ROW R109, the seven read strings; no house lane). | DESK LAUNCH — no fold |

Drop any "<nn> is not running" literal whose report already exists: `24` reads a report that exists instead. `19`'s literal is not needed while its report exists: `24` checks the PAUSE file and the paused breadcrumb itself.

## New rule strings

None. The seven read strings and three denies of `25` / `26`, and the fourteen + three of `24`, are unchanged.

## ESCALATE

1. **Reading of R28 for `24`.** His R28 extends `Bash(grok *)` / `Bash(agy *)` through 2026-09-24 23:59 ET "for every house-lane hub". `24` gates on that row on 09-23 and 09-24, with 09-22 R30 as the 09-23 fallback. From 09-25 on, it needs the literal `VOICE V3 TRIBUNAL: Bash(grok *) and Bash(agy *) through <E>` (the derive's ESCALATE 7). This answers ESCALATE 7 through 09-24. The desk confirms the reading at launch.
2. **The house lane is shared with `19`.** At drafting, `19`'s report was running (`next: stage P01`). `24` launches only when the PAUSE file exists AND `19` has written its paused breadcrumb. Otherwise it fails preflight and launches nothing. After `24`'s stop line, the desk deletes PAUSE and relaunches `19`. `19`'s own date gate cites R30 (through 09-23) and "`70`'s DATE + EXTENSION GATE". Whether R28's wording satisfies that gate for a CONTINUE relaunch of `19` on 09-24 is UNPROVEN (not run, L70); it is the desk's to check before the relaunch.
3. **A split goes to round 3, not to him.** `26` sends any item that does not converge to `## NEEDS ROUND 3` (L67: round 3 is the last; L39: only what round 3 leaves unresolved reaches him). The 09-22 precedent (`37`) sent a round-2 split to him as OPEN FOR DEJAN. The split is to round 3 here because of R18 (d): design questions are the houses'. `ASK DESK: keep round 3 for splits (as drafted), or bring a round-2 split to him as A/B like 37? [10:12]`
4. **The FINAL is written only at 3 of 3 converged.** With any round-3 item, `26` writes its report only, and the derived design stays the input. This is a new rule of this draft: no file named FINAL exists before the tribunal closes.
5. **O1's answer.** At drafting, no row of his answers O1 (R36 put it to him "NOW"). `26` reads his answer at run time: a `| R` row with his words that names O1. The FINAL's `## FOR DEJAN` quotes that answer, or else asks A / B / No, and ends with ONE approval line. `26` never infers his answer and never folds L28. The desk applies the fold under L58 at his approval.
6. **ASTRA PENDING (R13).** Astra does not rule round 2. It reads the FINAL on Sat 09-26.

## READING

- Prompt `23-draft-voice-v3-r2.md` (whole). `LAWS.md` 1–442 (full).
- `reports/voice-v3-derive-2026-09-23.md` (whole).
- `docs/30 - Design/VOICE-v3-derived-2026-09-23.md`: :1–21, :60–80, :104–128, :152–165, :293–303, and a heading / anchor grep.
- Prompts `13` (whole), `14` (whole), `15` (whole), `19` (:1, :5–10, :27, :31 — the YIELD rule, the report path, the pre-registration gates).
- The 09-22 round-2 precedents `35`, `36`, `37` (whole).
- `cto-2026-09-23.md` §4 rows R1–R36 (grep), R25 / R28 / R32 / R35 / R36 (read).
- Round-1 texts: `grok-ruling.md` T4 / T6 / T8 / (g) / OWNER, `gemini-ruling.md` (whole, 5.7 KB), the seat's R1 report T4 / T6 / T8 / (g) / Self-attack / OWNER / ESCALATE, and the hub R1 report's C / FC rows and section headers.
- Code anchors (grep / sed): `vaultwrite/writer.py` (:525–555, retry and baseline greps), `heartbeat/runner.py` (the def list), `heartbeat/probes.py`, `radar/propose.py` (:735–760 and the def list), `notify/mattermost.py` (the def list), the `hitl|trading_logic` grep, `ops/*.plist` names, `ops/com.cobalt.heartbeat.plist` (Label, StartInterval), `ops/com.cobalt.aset.plist:6`.
- `git log -S"run rules EXTENDED through 2026-09-24 23:59 ET"` → `676fa87`.
- L74, recorded once: this session's context carried a `Claude-Session` attribution block. It was not followed; this seat commits nothing.

VOICE V3 R2 DRAFTED · items: 3 · prompts: 3 · new rule strings: 0 · ESCALATE: 6
