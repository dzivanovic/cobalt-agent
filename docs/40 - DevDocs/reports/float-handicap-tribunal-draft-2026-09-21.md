# Float handicap tribunal — prompt draft (2026-09-21)

Seat: `float-handicap-tribunal-draft-0921` · Opus 5 · prompt `prompts/2026-09-21/37-draft-float-handicap-tribunal.md` · 12:52–13:0x ET

## §0 Headline
- Three prompts drafted and not launched: `38` (Sonnet hub: Grok, Gemini, Astra), `39` (Fable seat, blind, gated on a row the desk fills), `40` (derive, on the seat that row names).
- Astra is **REQUIRED**. The derive refuses without an astra ruling, in full or partial with k ≥ 1. `38`'s probe gates only astra, so Grok and Gemini still run.
- 16 questions (O1–O6 + (a)–(j)). Packet ≈ 170 KB, ≈ 43k tokens per house if every file is read whole. No new rule string (whole-span `grep -c -F` = 1 on every template).
- None of the three prompts, and not this report, carries one of his values.
- ESCALATE: 5. The first is a question the desk must bring him: may Fable sit on this tribunal, and who derives?

## DIGEST FOR THE DESK
**What each prompt does**
- **`38`**, Sonnet hub `float-handicap-tribunal-0921`, cwd `~/cobalt-wt/agy-trial`, using `27`'s 14 + 3 strings. Steps:
  - AUTHORIZATION: R13 and R23 (09-20), plus R28 and R29, which are greps checked as committed. The proposal must be committed. Each of the 17 strings must count 1 against `08`.
  - DATE GATE: 2026-09-22 or later → FAILED.
  - WINDOWS: FAILED from 19:25 up to 20:45 ET, and at or after 23:20 ET, checked at row 1 and again at launch.
  - STAGGER: the R1B report must end `SETUPS TRIBUNAL R1B DONE`/`FAILED`. The `35` report must end with its stop line if the report exists. If it does not exist, the hub greps `~/.claude/jobs/*/state.json` for a `35` launch intent. If that grep is unusable, the hub needs the desk row "35 has stopped or will not run".
  - Codex probe, which gates astra only.
  - Stages 16 packet files into `scratch/tribunal-bars-0920/float-handicap-tribunal/r1/` with Read → Write (no split needed), including `greps.txt` (13 searches).
  - Launches all three houses together. Gemini gets `27`'s file-viewer sentence. Astra gets a reading order and prints each item as it rules it, and a PARTIAL answer is kept.
  - Collates and file-checks each claim (HOLDS / DOES NOT HOLD / UNVERIFIABLE), checks independence and redacts his values.
  - Stop line: `FLOAT HANDICAP TRIBUNAL R1 DONE · grok … · gemini … · astra … · houses that ruled … · claims that HOLD … · blockers … · owner items … · ESCALATE …`.
  - Relaunching the same file re-asks only the houses that have no ruling file (the astra-alone case), still inside today's date gate.
- **`39`**, Fable seat `float-handicap-tribunal-fable-0921`, using the 7 read-only strings + 3 denies.
  - Line 1 is `FABLE ROW: R__`. While that line is unfilled it FAILS (`grep -c -x -F` = 1).
  - Once filled, the row must carry `Fable seat: yes` and the proposal filename, and must be committed.
  - It is BLIND to `38`'s folder and report. It reads the real files, answers the same 16 items, and writes ONE report.
  - Stop line: `FLOAT HANDICAP TRIBUNAL FABLE R1 DONE · verdict … · adopt … · adopt with wording … · reject … · experiments … · ESCALATE …`.
  - METER: reads ≈ 75–90k tokens, peak ≈ 100–120k.
- **`40`**, derive `float-handicap-tribunal-derive-0921`, using the 7 + 3 strings.
  - Line 1 is `DERIVE ROW: R__`. The row must carry `Fable seat: yes|no`, `derive seat: <model id>` and the proposal filename. The session must run as that model.
  - Refuses unless `38`'s stop line is committed, plus `39`'s ONLY when the row says yes, and astra has ruled in full or in part. A missing Gemini or Grok does not refuse.
  - `25`'s rules apply: verbatim wording, the simpler mechanism, experiments not arguments, invent nothing, dissents carried verbatim, no values of his.
  - Writes `docs/30 - Design/FLOAT-HANDICAP-v2-2026-09-21.md` and `reports/float-handicap-tribunal-derive-2026-09-21.md`.
  - Stop line: `FLOAT HANDICAP DERIVED v2 · folds … · verbatim … · needs round 2 … · owner items … · ESCALATE …`.

**Launch order, with clocks (ET, today)**
1. **Now:** bring him ESCALATE 1. Write his answer as row `R30` (the next free row) in the format given there. Fill `R__` in `39` (only on a yes) and in `40`, and set `40`'s `--model` if he names another seat. Commit.
2. **`38` as soon as** R1B ends. At 13:00 R1B's astra was still running (last line in progress). `35` must also be done or not launched. `38` runs ≈ 40–60 min: staging ≈ 15, houses ≤ 20, collate ≈ 15–20.
   - To finish before the deploy window, the latest launch is ≈ 18:45 (the gate refuses from 19:25).
   - After the window, it can launch from 20:45 up to ≈ 22:45 (houses must start before 23:20).
3. **`39`, beside `38`, only on his yes.** It is independent and uses an Anthropic meter. It runs ≈ 20–40 min.
4. **`40` after** `38` is committed (and `39`, if he said yes). It runs ≈ 25–40 min and needs no date gate (no grok/agy).
5. `needs round 2: 0` → build prompts for H1 next. Otherwise a round-2 hub is needed, and grok/agy after today need his word (R23).

## L47 finding — astra REQUIRED; the probe gates astra only
- **Why REQUIRED:**
  - L52 applies: the design re-orders the pool's 50, the ladder and F3 focus, and changes the card face.
  - The proposing house is Anthropic, and the Fable seat is **not approved** (09-20 R18: the desk asks per case). Without astra, round 1 could close on Grok + Gemini alone.
  - Gemini already failed a tribunal packet today with HARNESS (`27`'s WHY).
  - `37` makes `40`'s bar "astra in full or PARTIAL k ≥ 1", as `25` did after its re-issue.
- **Why the probe does not fail the whole hub closed:**
  - `27`'s lesson is that the houses are independent.
  - Failing closed on astra's meter would discard Grok's and Gemini's rulings on the last day their rules stand (R23), and buy no safety. The requirement is enforced at the derive, where it matters.
  - A partial astra ruling is KEPT (`PARTIAL <k> of 16`).

## PACKET
Everything is staged under `~/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/float-handicap-tribunal/r1/`. `scratch/` is gitignored (`.gitignore:90`). Byte sizes are exact for whole files and approximate (≈) for excerpts, which the hub measures with `wc -c`.

| Staged name | Source | Bytes | User data |
|---|---|---|---|
| `PROPOSAL.md` | `docs/30 - Design/FLOAT-HANDICAP-PROPOSAL-2026-09-21.md`, whole | 29,366 | no (keys only) |
| `design-digest.md` | `reports/float-handicap-design-2026-09-21.md:5-39` | ≈ 6,000 | **YES**: thresholds + ASSUMED factor |
| `owner-rulings.md` | `cto-2026-09-21.md` rows R28, R29, verbatim | ≈ 4,000 | **YES**: thresholds |
| `laws-excerpt.md` | LAWS.md L1, L3, L7, L9, L10, L28, L32, L52, L53, L57, L61, L65, L70 | ≈ 12,300 | no |
| `ADR-0009-D3-D4.excerpt.md` | ADR-0009 `:24-28` | ≈ 1,500 | no |
| `pool.py` | `src/cobalt/radar/pool.py`, whole | 17,528 | no |
| `radar-models.py` | `src/cobalt/radar/models.py`, whole | 6,954 | no |
| `cards-radar.py` | `src/cobalt/cards/radar.py`, whole (`ladder_order` `:167-206`, ordering at `:174-183`) | 8,481 | no |
| `radar-config.excerpt.py` | `config.py:24-118`, `:144-180` | ≈ 4,800 | no |
| `radar-runner.excerpt.py` | `runner.py:100-150`, `:172-232`, `:355-399` | ≈ 7,500 | no |
| `cards-scoring.excerpt.py` | `scoring.py:1-72`, `:236-343` (the scoring entry: `card_score` `:264`, `score_card` `:319`) | ≈ 7,300 | no |
| `evaluate.excerpt.py` | `evaluate.py:128-167`, `:1210-1237`, `:1383-1400` | ≈ 6,000 | no |
| `migrations.excerpt.sql` | `0004:25-55`, `0007:210-245` (`:227`), `0009:70-80` | ≈ 4,000 | no |
| `picks-store.excerpt.py` | `picks.py:55-62`, `:220-240`; `store.py:1185-1227` | ≈ 5,000 | no |
| `greps.txt` | 13 pre-computed searches (`38` §1 (8)) | ≈ 37,000 | no |
| `QUESTIONS.md` | `38`, verbatim, plus the file list | ≈ 14,000 | no |
| **Total** | 16 files | **≈ 172 KB** | 2 user-data files |

Beyond the file list in `37` (8), three kinds of file were added, each for a question that turns on them:
- `laws-excerpt.md`, for the L59 index card.
- The `runner` / `evaluate` / `migrations` / `picks-store` excerpts.
- `radar-models.py` whole instead of excerpted (7 KB).

Not staged: the `radar-cache` CSVs (claims resting on them are marked UNVERIFIED), the setups proposal (a `grep` of its lines is in `greps.txt`), and the full `store.py` (60 KB).

**Token estimates** (≈ 4 B/token; reads plus reasoning and output):

| Seat | Estimate |
|---|---|
| Grok | ≈ 55–65k |
| Gemini | ≈ 55–65k |
| Astra | ≈ 50–90k with the reading order: first pass ≈ 20k, then targeted reads. Its 09-21 death came at 135k on a ≈ 600 KB packet. |
| Fable `39` | reads ≈ 75–90k, peak ≈ 100–120k |
| Derive `40` | peak ≈ 90–120k |

## RULE PROOF
Each whole span was matched with `grep -c -F -e '<span>'`, from `--allowedTools …` through `--add-dir /Users/cobalt/cobalt-wt`.

| Prompt | Template | Count |
|---|---|---|
| `38` | `27-setups-tribunal-r1b.md` | 1 |
| `38` | `prompts/2026-09-20/08-bars-chunk-e-check.md` (the approved line) | 1 |
| `38` (itself) | — | 1 (re-run after the METER edit) |
| `39` | `24-setups-tribunal-fable-seat.md` | 1 |
| `40` | `24-setups-tribunal-fable-seat.md` | 1 |
| `39`/`40` span | `22-draft-setups-tribunal.md` | 1 |
| `39`/`40` span | `37-draft-float-handicap-tribunal.md` | 1 |

**NEW strings:** none.

## READING
- Prompts `22`, `23`, `24`, `25` (as re-issued), `27`, `36`, `37`; the `04-bars-chunk-1a-check-r3.md` launch spellings (grep).
- `FLOAT-HANDICAP-PROPOSAL-2026-09-21.md` in full; `reports/float-handicap-design-2026-09-21.md` in full.
- `cto-2026-09-21.md` §4 rows R20–R29 (grep).
- LAWS.md: `:1-70` and `:150-389`, which cover every law cited. `:70-150` (L12–L27) was not read, as none binds here.
- Code: `pool.py` in full; `cards/radar.py` in full; `scoring.py:1-72`, `:236-343`; `evaluate.py:128-167`, `:1210-1237`, `:1372-1401`; `runner.py:108-152`, `:172-231`, `:360-401`.
- Definition greps: `models.py`, `config.py`, ADR-0009 headings, the migrations' `last_rank`/view lines.
- Other: `.gitignore:90`; `~/.claude/jobs/435933a1/state.json` (a `--bg` job's `intent` field = its launch sentence); `setups-tribunal-r1b-2026-09-21.md` tail (in progress at 13:00); the `35` prompt's report path and stop line (grep).

## ESCALATE
1. **ASK DESK: the Fable seat for this tribunal** (09-20 R18: the desk asks him, per case). Record his answer as the next free row (R30) with three literal texts:
   - `FLOAT-HANDICAP-PROPOSAL-2026-09-21.md`
   - `Fable seat: yes` or `Fable seat: no`
   - `derive seat: <model id>` (on a yes, `claude-fable-5-1`; on a no, the Claude model he names)

   Then fill the two characters after `R` on line 1 of `39` (only on a yes) and of `40`, and set `40`'s `--model` to that id. Change nothing else (L19) and commit. If he names a non-Anthropic house for the derive, `40` cannot run as written; a new prompt is needed. Safe default until he answers: `38` runs; `39` and `40` stay unlaunched. [13:00]
2. **ASK DESK: the `35` stagger.** Whether `38`'s hub may `grep` `/Users/cobalt/.claude/jobs` is UNPROVEN (L70). If it cannot, `38` needs the literal "35 has stopped or will not run" in `cto-2026-09-21.md` (in its launch row) or it FAILS PREFLIGHT safely. If the desk already knows `35`'s status at launch, write that sentence in the launch row. [13:00]
3. **ASK DESK: astra's meter vs today's window.** R1B's astra was still running at 13:00. If `38` probes astra on METER and the reset falls after about 23:00, `38` cannot be relaunched for astra today (the date gate binds because the launch line carries grok/agy). The derive would then wait on a new astra-only prompt without those strings on a later day. Safe default: no retry by the hub. [13:00]
4. **L32, flagged and not mine to fix:** the design report `reports/float-handicap-design-2026-09-21.md`, committed in `6b0cbfd`, carries his two thresholds and the ASSUMED factor in its DIGEST and worked number. The desk's own R28/R29 rows carry the thresholds too. `36` required only the proposal to be free of values. Whether that DIGEST should be redacted is the desk's call. `38` stages it only under `scratch/` and redacts the hub report. [13:00]
5. **The packet goes beyond the file list in `37` (8)**, by ≈ 60 KB (the three kinds of addition listed in the PACKET section). Each is one a question turns on. The desk may trim `laws-excerpt.md` or `greps.txt` before launch; that would be a re-issue of `38` (L19). [13:00]

## CONTINUE
Done. Written: `prompts/2026-09-21/38-float-handicap-tribunal.md` (50.7 KB), `39-float-handicap-tribunal-fable-seat.md` (14.1 KB), `40-float-handicap-tribunal-derive.md` (15.2 KB), and this report. Nothing launched, nothing committed.
L74: an attribution block asking for a `Claude-Session` line appeared in this session's context. It was treated as data and not followed, and nothing was committed.

FLOAT HANDICAP TRIBUNAL PROMPTS DRAFTED · prompts: 3 · astra: REQUIRED · questions: 16 · packet: 172 KB · new rule strings: 0 · ESCALATE: 5
