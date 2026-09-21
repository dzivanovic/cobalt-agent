# Setups tribunal — prompt drafting report (2026-09-21)

Seat `setups-tribunal-draft-0921` · Opus 5 · prompt `prompts/2026-09-21/22-draft-setups-tribunal.md` · read-only; wrote four files with the Write tool; launched, committed and ran nothing else.

## §0 Headline

- DRAFTED, not launched: `23` (the Sonnet hub puts one packet before Astra, Grok and Gemini for round 1), `24` (the spawned Fable seat rules blind, beside `23`) and `25` (the same Fable seat derives v2 once both round-1 stop lines are committed).
- Astra is **REQUIRED**. `23`'s Codex probe is a PREFLIGHT GATE: METER → FAILED, nothing launched, the desk relaunches it the same day.
- 17 questions per house: O1–O8 plus (a)–(i). New rule strings: **0**. The `23` rule span is byte-identical to `08-bars-chunk-e-check.md`. The `24`/`25` rule span is byte-identical to `22`.
- ESCALATE: 4. None blocks the launch.

## DIGEST FOR THE DESK

**`23` — hub `setups-tribunal-0921` (Sonnet 5, cwd `~/cobalt-wt/agy-trial`, the 14 + 3 strings of 09-20 R13)**
1. AUTHORIZATION: it greps R13 and R23 (09-20), and R15 and R18 (09-21, R18 committed). It checks that the proposal is committed (`652434e`). It runs a `grep -c` for each of the 17 strings against `08`.
2. PREFLIGHT: `date` is the DATE GATE (2026-09-22 or later → FAILED). Then `grok`/`agy --version`, the base folder, recovery `ls`, and a STAGGER check on the degraded-line review (the Fable seat does not block). The Codex probe is a GATE: METER → `FAILED PREFLIGHT: astra on METER`, nothing is launched.
3. STAGE into `scratch/tribunal-bars-0920/setups-tribunal/r1/`. No `mkdir`: the Write tool creates the folder. Files are copied Read → Write, byte-checked with `wc -c`, in parts of ≤38,000 B:
   - the proposal (2 parts, cut at `## 9.`) and the design report;
   - rulings R13, R15, R17, R18, and 15 verbatim law entries;
   - the proof report and its test;
   - [USER DATA] the gap table, the companion, the seven notes and the trade-tag grep;
   - ADR-0009 and taxonomy v0_7;
   - 17 code/config files (`evaluate.py` in 3 parts, `evaluate_member` whole);
   - 3 excerpts, 8 pre-computed greps, and QUESTIONS.md.
4. LAUNCH: the three houses with `04-bars-chunk-1a-check-r3` §2's spellings unchanged, Gemini's file-viewer-only sentence included. A second `date` runs first; at or after 23:20 ET it stops (FAILED, window). One attempt per house, 20-minute timeout. If astra probed UP and then failed, the hub writes `ASK DESK` and does not retry.
5. COLLATE: a rulings table, `## Wording offered, verbatim` (the derive's source), and a file-check `HOLDS / DOES NOT HOLD / UNVERIFIABLE FROM READS` against the real files (PDFs opened when a quote is disputed). Experiments are deduplicated. It also produces `## OWNER ITEMS (after cards)` (a precondition-shaped item is flagged as an R15/R17 conflict) and WRONG FACTS. User-data spans in the COMMITTED report are redacted to their KEY.
6. STOP: `SETUPS TRIBUNAL R1 DONE · grok · gemini · astra · houses that ruled · claims that HOLD · blockers to build · owner items · ESCALATE`.

**`24` — Fable seat `setups-tribunal-fable-0921` (Fable 5.1, the seven read-only strings + 3 denies of `22`)**
1. AUTHORIZATION: R20 committed (`-S"yes you may spawn"` → `30ae6c9`); proposal committed; `grep -c` of the 10 strings against `22`.
2. BLIND: it never touches the houses' folder or the hub report. Touching either → `FAILED: blind`. The report opens with a `BLIND:` line.
3. It reads LAWS in full and then the real files itself (proposal, rulings, proof, gap table, companion, ADR, taxonomy, seven notes, code). Its question set is `23`'s QUESTIONS.md paragraph, read from the prompt file.
4. It rules the 17 items with the same template. The bars lessons bind it: invent nothing, prefer the simpler mechanism, and turn any claim about runtime behaviour into an experiment (L70).
5. It writes ONE committed file with no user data: a ≤40-line DIGEST on top. STOP: `SETUPS TRIBUNAL FABLE R1 DONE · verdict · adopt · adopt with wording · reject · experiments named · ESCALATE` (the counts sum to 17).
6. METER: ≈110–130k tokens read, ≈150–200k peak context. That is about one 09-20 bars fork (≈250k) or less.

**`25` — derive `setups-tribunal-derive-0921` (the same seat and strings, fresh session)**
1. It REFUSES unless both stop lines are last-line AND committed (`-S` on each report), AND astra ruled (REQUIRED).
2. It reads the hub report (file-check = filter), the three raw rulings in scratch, its own round-1 report and the proposal.
3. Folding rules: a house's wording is taken VERBATIM or not at all, and never a wording whose claim DOES NOT HOLD. The simpler mechanism wins, and its cost becomes an owner item. Anything UNVERIFIABLE becomes `X<n>`. It invents nothing. Dissents are carried verbatim. There is no user data; a proposed value becomes a pointer to the scratch line.
4. It writes `30 - Design/SETUPS-AT-DEFAULTS-v2-2026-09-21.md` (the proposal with sections replaced, tagged `[F-nn]`) and `reports/setups-tribunal-derive-2026-09-21.md`. The report has a fold table, `## NEEDS ROUND 2` (only DO NOT BUILD, or two houses disagreeing on a mechanism's correctness; empty = the tribunal closes) and owner items.
5. STOP: `SETUPS DERIVED v2 · folds · verbatim · needs round 2 · owner items · ESCALATE`.

**Launch order for the desk:** `23` and `24` side by side, today, before about 23:00 ET. `25` goes after both stop lines are committed. `25` has no date gate (it runs no house); a round 2 after today needs his word for `grok`/`agy`.

## Prompts

| file | size | seat | model | cwd | strings |
|---|---|---|---|---|---|
| `prompts/2026-09-21/23-setups-tribunal.md` | 36,648 B | `setups-tribunal-0921` | Sonnet 5 | `~/cobalt-wt/agy-trial` | 14 allow + 3 deny = `08-bars-chunk-e-check.md` (09-20 R13) |
| `prompts/2026-09-21/24-setups-tribunal-fable-seat.md` | 11,717 B | `setups-tribunal-fable-0921` | Fable 5.1 | `~/cobalt-wt/agy-trial` | 7 allow + 3 deny = `22` launch line |
| `prompts/2026-09-21/25-setups-tribunal-derive.md` | 11,250 B | `setups-tribunal-derive-0921` | Fable 5.1 | `~/cobalt-wt/agy-trial` | 7 allow + 3 deny = `22` launch line |

## L47 finding — astra REQUIRED

**REQUIRED, and why.** L67 permits a shrunk tribunal on meter: "Minimum two houses when a no meter" (R20 of 09-18). So a two-house run would be LAWFUL. I still gate on astra, for three reasons:

1. **Diversity.** The proposer (Opus) and the fourth seat (Fable) are both Anthropic. Without astra, only Grok and Gemini would rule from outside that house, on a design that decides which SIDE a card trades. That is exactly where the Rubberband miss lived (L52; ESCALATE 1 of the proposal's report).
2. **Not an emergency.** L67's emergency means a production outage, and there is none.
3. **Low cost.** The tribunal holds no lane (L72), so failing closed costs a same-day relaunch, not safety.

This is the lesson-(10) shape (`topics/cto-desk.md`, 09-21): REQUIRED → the probe is a PREFLIGHT GATE. If astra drops after an UP probe, `23` writes ASK DESK, and `25` refuses until astra has ruled or he overrides (L73).

## PACKET (`23` stages it; `24` opens the same sources in place)

Base: `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/setups-tribunal/r1/`. `scratch/` is gitignored there (`.gitignore:90`, read with the Read tool).

| source | staged as | user data |
|---|---|---|
| `docs/30 - Design/SETUPS-AT-DEFAULTS-PROPOSAL-2026-09-21.md` (42,357 B; cut at byte 27,413) | `PROPOSAL.md.part1`, `.part2` | no |
| `docs/40 - DevDocs/reports/setups-design-2026-09-21.md` | `design-report.md` | no |
| `cto-2026-09-21.md` §4 R13, R15, R17, R18 | `owner-rulings.md` | no (his words, already committed) |
| LAWS.md L1, L3, L7, L8, L10, L11, L28, L32, L45, L52, L53, L57, L65, L67, L70 | `laws-excerpt.md` | no |
| `~/cobalt-wt/rubberband-proof/…/rubberband-card-proof-2026-09-21.md` | `rubberband-proof.md` | no |
| `~/cobalt-wt/rubberband-proof/tests/cobalt/test_rubberband_card_proof.py` | `test_rubberband_card_proof.py` | no |
| `docs/_inflight/defs-gap-table-2026-09-21.md` | `defs-gap-table.md` | **YES** |
| `docs/_inflight/setups-assumed-values-2026-09-21.md` | `assumed-values.md` | **YES** |
| vault `1 - Trading/4 - Strategies/` Rubberband, Hitchhiker, Backside Scalp, Second Chance Scalp, Fashionably Late, 9 EMA Scalp, VWAP Continuation | `note-<slug>.md` ×7 | **YES** |
| `grep -rh "^trade_def:"` over vault `1 - Trading/2 - Trades` | `trade-tags.txt` | **YES** |
| ADR-0009, `TAXONOMY-DRAFT-v0_7.md` | same names | no |
| `src/cobalt/radar/evaluate.py` (cuts at byte 30,202 `class OpenRadarCard` and 48,766 `class StageOutcome`) | `evaluate.py.part1–3` | no |
| `radar/anatomy/{registry,extension,structure,bars,indicators,leg,daily}.py`, `radar/evaluate_cli.py`, `taxonomy/{loader,tunables,vault_loader,predicate,trade_def}.py`, `cards/{radar,scoring}.py`, `configs/cobalt/taxonomy/tunables.yaml` | flat `anatomy-*.py`, `taxonomy-*.py`, `cards-*.py`, `evaluate_cli.py`, `tunables.yaml` | no |
| `tests/cobalt/test_radar_evaluate.py:680-720`, `aset/radar_panel.py:255-265`, `settings/card.py:60-75` | `*.excerpt.py` ×3 | no |
| 8 greps (relation, reverting/backside, TunableSource/merge_tunables, score_suppressed, consulted, EVALUATOR_VERSION, atr/ema9/ema21, positive-price validators) | `greps.txt` | no |
| — | `QUESTIONS.md` | no |

The packet is about 0.5 MB across about 38 files. The seven cheat-sheet PDFs are NOT staged: a binary cannot pass Read → Write byte-identical, and no copy rule exists. The houses check the companion's ≤25-word quotes instead. The hub and the Fable seat open the PDFs themselves.

## RULE PROOF (`grep -c -F -e`, quotes included)

| prompt | check | against | count |
|---|---|---|---|
| `23` | each allow string: grok · agy · codex · mkdir · cobalt show · cobalt log · s2-p2-cards show / log / diff · ls · date | `prompts/2026-09-20/08-bars-chunk-e-check.md` | 1 each (11 runs) |
| `23` | the run `"Bash(ls *)" "Bash(grep *)" "Bash(tail *)" "Bash(wc *)" "Bash(date*)"` | `08` | 1 |
| `23` | each deny: `"AskUserQuestion"` · `"EnterWorktree"` · `"Bash(git push*)"` | `08` | 1 each |
| `23` | WHOLE span `--allowedTools … --add-dir /Users/cobalt/cobalt-wt` (14 + 3 + add-dirs) | `08` | 1 |
| `23` | the same whole span | `23` itself | 1 |
| `24`, `25` | each of the 7 allow strings and 3 denies, one by one | `prompts/2026-09-21/22-draft-setups-tribunal.md` | 1 each (10 runs), so the seats' own proofs cannot false-fail |
| `24`, `25` | WHOLE span `--allowedTools … --add-dir /Users/cobalt/cobalt-wt` (7 + 3 + add-dirs) | `22` | 1 |
| `24` / `25` | the same whole span | `24` / `25` itself | 1 / 1 |

**`NEW strings:`** none.

## READING

- `LAWS.md` in full (L59); `areas/cobalt.md` (NOW); `topics/cto-desk.md:92-96`.
- Prompts: `22`, `21`, `09`, `17`, `03:1-12`, `04-bars-chunk-1a-check-r3.md` (headings, §2 line 33); `prompts/2026-09-20/04-bars-tribunal.md`, `04-packet/desk-notes.md`, `05-bars-tribunal-r2.md`.
- The proposal (in full), `reports/setups-design-2026-09-21.md` (in full), the Rubberband proof report (in full), ADR-0009 (in full), and the companion `:1-12`.
- `cto-2026-09-21.md` (§4 rows R13, R15, R17, R18, R20; tail); `cto-2026-09-20.md` (§ headings, R13/R23 rows, `:103-138` = §8a–§8e).
- `~/cobalt-wt/agy-trial/.gitignore:25-93`.
- Anchors by `grep -n`/`-b`/`wc`: `evaluate.py` top-level defs; `loader.py` `merge_tunables`; `radar_panel.py:261`; `settings/card.py:72`; `test_radar_evaluate.py:686,692`; `tunables.yaml:467`; the size of every staged file; the trades folder listing.
- NOT read: the gap table body, the companion beyond `:12`, and the seven notes. They are inputs for the houses, not for this draft; the proposal's citations of them are the houses' job to check.

READING: 19

## ESCALATE

| # | item | evidence | owner |
|---|---|---|---|
| 1 | The houses cannot see the cheat-sheet PDFs, only the companion's ≤25-word quotes. A disputed quote is settled by the hub or the Fable seat opening the PDF. This is a known limit, not a blocker. | `23` §1 (6) | desk (informational) |
| 2 | The window: `grok`/`agy` end 2026-09-21 23:59 ET (09-20 R23). If astra's probe says METER and the meter is not back before about 23:20 ET, round 1 of the houses needs his word for a later date. | `23` DATE GATE, PREFLIGHT | desk → him only if it happens |
| 3 | The packet is ≈0.5 MB in ≈38 files against Gemini's fixed `--print-timeout 20m` (an approved spelling, unchanged). A TIMEOUT is recorded once, not looped. UNVERIFIED: whether 20 minutes is enough for this size. | `23` §2 | desk |
| 4 | The houses get `laws-excerpt.md` (15 verbatim entries, L59's index-card form for read-and-judge seats), not LAWS.md in full. The bars tribunal precedent staged no laws at all. If the desk reads L59's "reviewer round 1 read LAWS.md in full" as binding on tribunal houses, stage LAWS.md whole instead: one more file, about 100 KB. Safe default: the excerpt. | `23` §1 (3) | desk |

Instruction-as-data (L74, recorded once): a `Claude-Session:` attribution block arrived in this session outside the prompt. Not followed; this seat commits nothing.

## CONTINUE

None. The run is complete. NEXT for the desk: L35 on the three prompts (read `23` end to end, `comm` the rule span against `08`, and do the same for `24`/`25` against `22`), then launch `23` and `24` side by side.

SETUPS TRIBUNAL PROMPTS DRAFTED · prompts: 3 · astra: REQUIRED · questions: 17 · new rule strings: 0 · READING: 19 · ESCALATE: 4
