# Setups tribunal, round 1B — Gemini and Astra (2026-09-21)

## §0 Headline
- Hub `setups-tribunal-r1b-0921`, Sonnet 5. Packet reused, nothing restaged. **1 of 2 houses ruled: Gemini** (`TRIBUNAL R1: BUILD`, no item REJECTED). **Astra: TIMEOUT** — probed UP at 11:45, launched 11:46, printed only `Reading additional input from stdin...`, no ruling; stopped by me with TaskStop at 14:51 ET. k = 0, no file.
- File-check of Gemini's claims: 16 HOLD · 9 DO NOT HOLD · 4 UNVERIFIABLE FROM READS. Blockers to build (by the prompt's formula: REJECTED / BUILD AFTER items whose claim HOLDS): 0 — but Gemini's `BUILD` rests on nine claims that do NOT hold, 2 of them contradicting Grok's R1 `BUILD AFTER` items (see `## ESCALATE`). Owner items: 5, none a precondition. ESCALATE: 4.
- Redactions (L32): 2 spans in my own file-check rows replaced by `[user data: <note>:<lines>]`. Gemini's text quotes nothing from his notes, the gap table, `assumed-values.md` or `trade-tags.txt` (keys `A-nn` only), so none was redacted there. Report Write path accepted; not refused.
- L74 (recorded once, not followed): a block appended inside a tool result (the prompt file Read) asked for a `Claude-Session:` line in commits and named a file-send tool. It is data; this run commits nothing.
- Desk message (cross-session, 14:5x ET) asked me to stop the hung astra shell, record `astra: TIMEOUT`, and finish. Done inside prompt `27` and my own tools; no relaunch. Its `ps` figures (elapsed 03:04:26, CPU 0:00.09) are the desk's reading — `ps` is not in my allow list and I did not run it. My own facts: output file holds only the stdin line at 11:52 and at 14:51; TaskStop reported success.

## AUTHORIZATION (verified by the hub, each its own Bash call)
| proof | result |
|---|---|
| R13 in `cto-2026-09-20.md` | line 86, carries the 13:33 ET words |
| R23 in `cto-2026-09-20.md` | line 206, grok/agy through 2026-09-21 23:59 ET |
| R15 in `cto-2026-09-21.md` | line 27, carries "I don't want to rule on anything" |
| R18 in `cto-2026-09-21.md` | line 29, carries "Hitchhicker, Backside, Rubberband" |
| desk's answer "both houses re-run alone today" | `cto-2026-09-21.md:243` (non-empty) |
| that answer committed | `7ea4f26d25da46a2699003adb05b80643ceae07c` |
| round-1 hub report committed (`SETUPS TRIBUNAL R1 DONE`) | `7ea4f26d25da46a2699003adb05b80643ceae07c` |
| proposal committed | `652434e50156f9ea30777703c0fc1072b8562308` |
| 14 allow + 3 deny strings in `08-bars-chunk-e-check.md` | 17 of 17 count 1 (no new rule) |

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| DATE GATE + TIME GATE (row 1) | `date` | 0 | allowed — `Mon Sep 21 11:44:41 EDT 2026` (before 2026-09-22; at/after 11:15; before 23:20) |
| `Bash(agy *)` | `agy --version` | 0 | allowed — `1.2.7` |
| `Bash(ls *)` | `ls scratch/tribunal-bars-0920` | 0 | allowed — folder exists |
| `Bash(tail *)` | `tail -n 3 …/setups-tribunal-2026-09-21.md` | 0 | allowed — last non-blank line starts `SETUPS TRIBUNAL R1 DONE ` |
| `Bash(ls *)` | `ls -l scratch/tribunal-bars-0920/setups-tribunal/r1` | 0 | allowed — every file the prompt lists present at its stated byte size; `grok-ruling.md` 23148 present; no `gemini-ruling.md`, `astra-ruling.md`, `astra-ruling.partial.md` in `r1/` |
| CODEX PROBE (gate for astra only) | `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` | 0 | allowed — replied `OK`, exit 0, no usage-limit text → **astra: UP** (its output also began `Reading additional input from stdin...`, then completed) |
| DATE GATE (row 2, before the launches) | `date` | 0 | allowed — `Mon Sep 21 11:45:51 EDT 2026` |

## Packet
`ls -l scratch/tribunal-bars-0920/setups-tribunal/r1`: **every file the prompt lists is present at exactly its stated size, 0 missing, 0 changed**; reused, nothing restaged, no packet file edited. Count note: the prompt's own list holds 43 named files (the prompt and round 1 call it 44); the listing shows 44 entries because `grok-ruling.md` (not a packet file, forbidden to both houses by their launch sentences) sits beside them. No size mismatch, so no FAILED PREFLIGHT.

## CONTINUE
LAUNCHED 11:46 ET, both `run_in_background`, one attempt each, 20-minute timeout, no rule added, spellings word for word from `04-bars-chunk-1a-check-r3.md` §2 with this prompt's sentences.
- GEMINI: completed exit 0 within ~3 minutes, printed a full ruling ending `TRIBUNAL R1: BUILD`; written to `r1/gemini-ruling.md` (6,360 B, minus the harness's trailing `[exited with code 0]`). The file-viewer-only sentence held: no `command` denial this time.
- ASTRA: `astra: TIMEOUT`. Background output = the single line `Reading additional input from stdin...` at 11:52 and unchanged at 14:51:11 ET. No reads, no ITEM message, no usage-limit text, no exit. I did not enforce the 20-minute timeout at 12:06: after launching I went idle awaiting the completion notification and read the clock only when the desk's message woke me at ~14:51 — a slip in my own conduct, disclosed; the cost was the two staggered runs behind this one. Stopped with TaskStop at 14:51 (success reported). k = 0 → no `astra-ruling.md`, no `astra-ruling.partial.md`.
- UNPROVEN (L70): why astra hung. What the transcript shows differed from round 1's astra run: nothing observable to me — the same `codex exec … -s read-only "<long prompt>"` shape, `run_in_background`, launched in one message beside Gemini. The desk's reading (codex waited for stdin EOF in a background shell) is unproven: the 11:45 probe printed the same stdin line and then answered `OK` and exited 0, so the line alone is not the hang signature. Settling run: relaunch with stdin closed (`< /dev/null`) is not in the approved rule list — a desk/Dejan decision — and compare.
- UNPROVEN (L70): whether `codex exec` prints intermediate messages as it goes. Not settled: it printed nothing in 3 hours, so no ITEM message could have been captured either way.
next: none — the report is complete; the desk commits it (I commit nothing).

## Rulings table
Grok's column is COPIED from `reports/setups-tribunal-2026-09-21.md` `## Rulings table`, not re-checked. Astra: `—` on every row (TIMEOUT, k = 0). "Agreement" counts houses that ruled the item: 2 of 3 (Gemini, Grok).

| item | gemini | astra | grok (R1, copied) | agreement | wording offered / reason (≤25 words per house) |
|---|---|---|---|---|---|
| O1 direction from anatomy `A-01` | ADOPT | — | ADOPT WITH | split (ADOPT vs ADOPT WITH), 2 of 3 ruled | G: relation is setup context; all 7 oppose the Extension. Grok: scope `against ext.direction` to rubberband's C1; never the four with-trend defs. |
| O2 mirrored frame | ADOPT | — | ADOPT WITH | split, 2 of 3 | G: negation preserves distances, no side branching; 2× cost "measured (X5)". Grok: replace the property test with `negate_prices(eval_as_long(mirror(bars))) == eval_as_short(bars)`. |
| O3 `unclassified` token | ADOPT | — | ADOPT | 2-0 ADOPT, 2 of 3 | G: honest, no migration, tap stays authoritative. Grok: `setup_ref` already `str`; `SetupRef` enum must not gain it. |
| O4 score suppressed on assumed formation | ADOPT | — | ADOPT WITH | split, 2 of 3 | G: implements L52(a); cards stay visible by tie policy. Grok: persist `assumed_formation` on the row; `refresh_card` must not overwrite it. |
| O5 one vault note + hole-fill | ADOPT | — | ADOPT WITH | split, 2 of 3 | G: hole-fill only on null engine rows. Grok: new L28 command; hole-fill only if engine null AND source assumed AND same scope AND same key. |
| O6 premarket seed beside Extension ATR | ADOPT | — | ADOPT WITH | split, 2 of 3 | G: keep `atr_run` RTH, seed `atr_working`. Grok: seeded ATR gets a NEW name (`atr_seeded`); keep `atr_working`; `ev.ema9` stays RTH until version bump. |
| O7 opening-drive termination `A-07` | ADOPT WITH | — | ADOPT | split, 2 of 3 | G: replacement wording below (micro-Range from extreme within bounded retrace ⇒ consolidation). Grok: proposed rule is the only forming one; taxonomy amendment is OWNER after cards. |
| O8 9-EMA catalyst `A-13` | ADOPT | — | ADOPT | 2-0 ADOPT, 2 of 3 | G: tap gate violates R17; admission as proxy, marked ASSUMED. Grok: no catalyst collector; mark on atom, chip on card, dot stays YOURS. |
| (a) direction | ADOPT | — | not safe for all seven | conflict, 2 of 3 | G: `against ext.direction` correctly models all 7. Grok: right for rubberband; backside/FL need the frame; four with-trend defs are not against-Extension. |
| (b) mirrored frame | ADOPT | — | ten non-equivalences named | conflict, 2 of 3 | G: "No equivalence flaws exist in the staged logic"; adds X6. Grok: stop buffer+nudge, upper third, `gt=0` spec, tie label…; stated property test not enough. |
| (c) L52 (a)–(d) | ADOPT (all four) | — | ADOPT WITH / ADOPT / ADOPT WITH / ADOPT | split on (a),(c) | G: all L52 requirements met. Grok: (a) recorder must wrap every cfg read; (c) name seams as artifacts in their chunk. (b),(d) agree. |
| (d) assumed visibility | ADOPT | — | paths (1)(2)(5) not covered as written | conflict, 2 of 3 | G: interpreter `cfg` recorder covers all paths. Grok: A-01 not a cfg key; cfg reads outside interpreter; `refresh_card` recomputes suppression. |
| (e) store | ADOPT (desk-written note) | — | build the L28 command | conflict, 2 of 3 | G: desk-written note, 0 cost to C2, "obeys L65 strictly". Grok: R15 is not an L65 write instruction; L28 command, +S on C2; hole-fill same key+scope only. |
| (f) acceptance | ADOPT | — | gates 1–4 catch; gate 5 does not | largely agree, 2 of 3 | G: gates 1 and 4 catch; green-while-empty = builder-chosen day, skipped live-note test. Grok adds gate-5 gap, zero tagged rubberband/backside, unevaluable defs. |
| (g) warm-up | ADOPT | — | no number moves if names differ | split, 2 of 3 | G: two distinct quantities, no shift. Grok: `ev.ema9` moves if seeded; "two quantities" true only with two names. |
| (h) chunks / experiments / latency | ADOPT | — | split C3; X6, X8 added | split, 2 of 3 | G: order clean, C3 large but required; `100T` scan arithmetic. Grok: split C3a/C3b; 7×2×50 = 700 vs ~50 today; add X6, X8. |
| (i) not checkable | ADOPT (adds X6) | — | X1–X6, X8 (X7 "settled") | overlap on X6, 2 of 3 | G: X1–X5 plus X6 (negative-price `Bar`). Grok: X1–X6, X8; X7 called settled. |
| closing line | `TRIBUNAL R1: BUILD` | — | `TRIBUNAL R1: BUILD AFTER scoped A-01, atr name, hole-fill, assumed persist` | conflict (BUILD vs BUILD AFTER) | — |

## Wording offered, verbatim
Only one `ADOPT WITH` replacement wording came from Gemini and no `REJECT` was issued by either new house. Astra: nothing printed. `[PARTIAL]` items: none.

### Gemini — O7 ADOPT WITH (verbatim)
> When a micro-Range instantiates from the drive's extreme within a bounded retrace, the termination is consolidation.

Gemini's reasoning beside it, verbatim: "A literal taxonomy reading ("first opposing bar ends a leg") makes `terminated_by == consolidation` impossible, breaking Hitchhiker. The replacement interpretation correctly identifies sideways ranges following a drive."

### Gemini — every other item: ADOPT, no replacement wording
Reasoning text is in `r1/gemini-ruling.md` (6,360 B, full text kept whole); the reasoning lines the file-check rows below quote are copied word for word in their `claim` cells.

## Checked against the files
Real files opened by the hub: `/Users/cobalt/cobalt/src/cobalt/radar/evaluate.py`, `…/anatomy/structure.py`, `…/anatomy/extension.py`, `…/cards/radar.py`, `…/cards/scoring.py`, `…/taxonomy/loader.py`, `…/archiver/models.py`, `configs/cobalt/taxonomy/tunables.yaml`, `tests/cobalt/test_radar_evaluate.py`, `docs/30 - Design/TAXONOMY-DRAFT-v0_7.md` and the proposal on main; the notes under `/Users/cobalt/Vault/Think/1 - Trading/4 - Strategies/`; `cto-2026-09-21.md`. Line numbers are the ORIGINAL files'. Only Gemini made claims (astra: none). "= R1 row n" points at the round-1 report's `## Checked against the files`.

| # | claim (Gemini) | file:line | verdict | note (≤30 words) |
|---|---|---|---|---|
| 1 | O1/(a): `valid_setups[].relation` describes the setup's HTF context, not intraday direction; `evaluate.py:635-647` conflates them | `evaluate.py:635-645`; `TAXONOMY-DRAFT-v0_7.md:136-137` | HOLDS | Gate maps all-countertrend / all-with_trend / mixed to sides; schema puts `relation` on the setup entry, direction separate. = R1 row 1 |
| 2 | O1/(a)/OWNER: "All 7 setups are pullbacks where the entry opposes the immediate Extension"; `trade_direction = against ext.direction` "correctly models all 7 setups" | `PROPOSAL:25,33`; evidence `[user data: 9 EMA Scalp.md:45; VWAP Continuation.md:40; Hitchhiker.md:33-47]` | DOES NOT HOLD | The four with-trend defs bind the trade side with the drive, not against it; `ext.direction` is set from close vs open (`extension.py:96-103`). Proposal itself scopes the rule (:33) and says three defs resolve against (:25). = R1 rows 5, 6 |
| 3 | O2/(b): negation preserves absolute distances, True Range; `upper_third` evaluates as the lower third of the original | `TAXONOMY-DRAFT-v0_7.md:89`; `PROPOSAL:55` | HOLDS | \|(-a)-(-b)\| = \|a-b\|; high↔low swap keeps high−low. ARITHMETIC OK (by reading, not run). = R1 row 9 |
| 4 | (b): "No equivalence flaws exist in the staged logic"; "I analyzed … stop logic (`structure.py`)" | `structure.py:96-116`; `PROPOSAL:57`; `cards/radar.py:86,88` | DOES NOT HOLD | Stop 10.02, buffer 0.02: raw 10.00 on the ten-cent grid → 10.01; mirrored −10.02 → raw −10.04, off-grid (−1004 not divisible by 10 under either remainder sign) → −10.04; −10.01 ≠ −10.04. ARITHMETIC OK. `gt=0` on trigger/stop also exists. = R1 rows 8a, 8b, 10 |
| 5 | (b)/(i) X6: does a negative-price `Bar` raise? ("If it throws a validation error (`ge=0`)…") | `archiver/models.py:41-45,47` | UNVERIFIABLE FROM READS | OHLC are bare `Decimal`; only `volume` carries `ge=0`; only `ts` has a validator (no `model_validator`). DB-level CHECK unread. Run: insert a negative-price `Bar` on `cobalt_dev`. = R1 row 14 |
| 6 | O6/(g): "keeping `atr_run` strictly RTH … introducing `atr_working` for the warm series" | `evaluate.py:568`; `PROPOSAL:143,270` | DOES NOT HOLD | `atr_working` is already today's seam observation of the Extension's RTH ATR; `atr_run` appears nowhere in `src/` (search: only the proposal). = R1 row 20 |
| 7a | (g): Rubberband's `atrs_from_open` does not shift | `evaluate.py:437-445`; `PROPOSAL:143` | HOLDS | Factor inputs read `ext.atr`, which the proposal leaves on the RTH run. |
| 7b | (g): "existing numbers … do not shift" (blanket) | `evaluate.py:560-564,794`; `PROPOSAL:141` | UNVERIFIABLE FROM READS | `ev.ema9` = `ema(run, …)` feeds FILLED-card health; proposal seeds EMA9 from premarket without saying whether `:562` changes. Run: C3 build + replay of a FILLED card. = R1 row 22 |
| 8 | O4/(d): "`assumed_formation` suppression accurately covers all paths" | `evaluate.py:777-780,800`; `cards/scoring.py:247-251,264-267` | DOES NOT HOLD | `refresh_card` recomputes `score_suppressed` from dots only; `assumed_formation` exists nowhere in `src/`; proposal states no persistence across refresh. = R1 row 17 |
| 9 | (d): "By intercepting the interpreter's `cfg` callable, … every consulted assumed key is recorded" | `evaluate.py:419-422,528,601-602,653,656`; `extension.py:55-63` | DOES NOT HOLD | Trigger `bars_cleared` and stop buffer go through `_cfg_value`; Extension params through `from_tunables` — none through the interpreter's `cfg`. = R1 row 26 |
| 10 | (c): "`Formation`, `TriggerOutcome`, and the `assumed_keys` view are explicit, schema-validated seams" | `evaluate.py:661`; search of `src/` for `TriggerOutcome`, `StopOutcome`, `assumed_keys`, `assumed_formation` = 0 hits; `PROPOSAL:230` | DOES NOT HOLD | `Formation` exists; the other three are proposed names, each "pinned … in the chunk that adds it". Not artifacts today (L52(c) asks for a specified artifact). |
| 11 | (c)/(d): `audit-export` and `replay_receipt` exist for audit | `radar/cli.py:49`; `radar/audit_export.py:1-4`; `evaluate.py:1043` | HOLDS | Both present. Neither reads `EVALUATOR_VERSION` per R1 row 24 (not re-opened here). |
| 12 | (c)(b): `card_score` remains the sole ranker | `cards/scoring.py:264-267`; `evaluate.py:134-138` | HOLDS | Score is `None` when suppressed; WATCH orders by `card_score`. = R1 (c)(b) |
| 13 | O4: suppressed-score cards "remain visible in the list by relying on the WATCH tie policy" | `evaluate.py:134-138` | HOLDS | `WATCH by card_score desc nulls last, pool_position …` |
| 14 | O5/(e): hole-fill "targets only `value: null` engine rows" | `PROPOSAL:175`; `loader.py:126-128`; `tunables.yaml:73-80` | HOLDS | Wording matches proposal; but neither states a scope condition, and `resolve_cfg` returns by key only, so Grok's scope-widening claim also HOLDS. = R1 row 18 |
| 15 | (e): if the engine gains a value the collision is loud | `loader.py:95-111` | HOLDS | Collisions raise `TaxonomyConfigError`; Gemini's "shadows" wording is inverted — the merge refuses shadowing (:95-99). |
| 16 | (e): on owner edit the source becomes `ruling` and clears the chip | `PROPOSAL:165` | HOLDS | Design text as stated; not implemented (proposal only). |
| 17a | (e): desk-written note "adds 0 cost to C2" | `PROPOSAL:177` | HOLDS | Proposal: no new write path; the fallback command "would add about an S". |
| 17b | (e): desk-written note "obeys L65 strictly" | `LAWS.md:335`; `PROPOSAL:177` | DOES NOT HOLD | L65: "Never a value he has not ruled"; the proposal itself calls assumed values unruled by definition. Whether R15 (`cto-2026-09-21.md:27`) overrides is his (L73), not checked. = R1 row 19 |
| 18 | O7: the literal reading makes `terminated_by == consolidation` "impossible" | `TAXONOMY-DRAFT-v0_7.md:94`; `PROPOSAL:271` | UNVERIFIABLE FROM READS | Text says pullback (≥1 opposing bar) or consolidation; proposal says "almost never", Gemini "impossible". Run: evaluate hitchhiker on stored drive-then-range days under both readings. = R1 rows 32a, 32b |
| 19 | O8: R17 quoted as "see the cards before I rule" | `cto-2026-09-21.md:28` | HOLDS | R17 carries "I need to see the cards before I rule on anything"; Gemini's span is an exact substring. |
| 20 | O8: 9-EMA "requires a catalyst or setup"; radar admission as proxy, marked ASSUMED | `[user data: 9 EMA Scalp.md:44]`; `PROPOSAL:151-153` | HOLDS | Reading matches the proposal's citation of the note. Gemini does not note A-13 is constant True on admitted members (R1 row 33). |
| 21 | (f): gates 1 and 4 would have caught the Rubberband defect | `PROPOSAL:183-188` | HOLDS | Gate 1 only on the real mixed shape; gate 4 on a day that forms. Counterfactual by reading of the proposal's own gates. = R1 (f) |
| 22 | (f): live-note test skipped when its env var is unset | `tests/cobalt/test_radar_evaluate.py:686-688,691,714` | HOLDS | `requires_vault` skipif; assertion is only "not stuck at not_evaluable". = R1 row 27 |
| 23a | (h): arithmetic "if evaluation takes T, scan takes 100T" | `tunables.yaml:467-474`; `PROPOSAL:234` | ARITHMETIC OK for one def (2 frames × 50 = 100) / WRONG AT the evaluations-per-scan step | The proposal evaluates seven defs: 7×2×50 = 700 (R1 row 31a). T is undefined; `radar.scan_interval` = 100 s. |
| 23b | (h): whether a doubled evaluation misses a scan | `tunables.yaml:467-474` | UNVERIFIABLE FROM READS | Gemini marks it UNVERIFIED itself. Run X5: time the evaluation on `cobalt_dev` against 100 s. |
| 24 | O2: "The 2× CPU cost is measured (X5)" | `PROPOSAL:57,234` | DOES NOT HOLD | X5 is a to-run experiment; nothing in the packet is a measurement. |
| 25a | WRONG FACTS "None found" | `evaluate.py:568`; `PROPOSAL:143,265` | DOES NOT HOLD | R1's WRONG FACT 2 (`atr_working` collision) re-verified in row 6; WRONG FACT 3 (same-side reading beyond rubberband, `PROPOSAL:265`) sits against row 2. WRONG FACT 1 = R1 row 29, not re-opened here. |
| 25b | WRONG FACTS support: `valid_setups` schema, consumed set holding premarket bars, `tunables.yaml` null rows match | `TAXONOMY-DRAFT-v0_7.md:136`; `evaluate.py:498-500`; `tunables.yaml:73-80` | HOLDS | Consumed = every closed i1 bar of the trade date; null `range.wick_ratio_max` row exists. |
| 26 | O3: `unclassified` needs no migration; the `setup_relation` tap remains | `cards/radar.py:84`; `evaluate_cli.py:35` | HOLDS | `setup_ref` is `str`; tap grade for `setup_relation` in the CLI. = R1 row 16 |

Counts: HOLDS = 16 (rows 1, 3, 7a, 11, 12, 13, 14, 15, 16, 17a, 19, 20, 21, 22, 25b, 26) · DOES NOT HOLD = 9 (2, 4, 6, 8, 9, 10, 17b, 24, 25a) · UNVERIFIABLE FROM READS = 4 (5, 7b, 18, 23b) · ARITHMETIC (rows 3, 4, 23a) OK/OK/OK-with-WRONG-STEP.

### Where Gemini and Grok's R1 ruling contradict (both quoted, nothing smoothed)
| topic | Gemini | Grok (R1) | file-check |
|---|---|---|---|
| all seven vs against the Extension | "All 7 setups are pullbacks where the entry opposes the immediate Extension." | "It is **not** true that `trade_direction = against ext.direction` is safe for every one of the seven." | row 2: Gemini's DOES NOT HOLD; Grok's (a) table = R1 rows 5–6 |
| mirror flaws | "No equivalence flaws exist in the staged logic." | "`detector(mirror(bars)) == mirror(detector(bars))` is **not** enough: it false-fails (1)(2) and does not mention (3)." | row 4: Gemini's DOES NOT HOLD |
| ATR names | "keeping `atr_run` strictly RTH … introducing `atr_working` for the warm series" | "Proposal name `atr_working` for the seeded ATR collides with today's Extension ATR observation." | row 6: Grok's HOLDS |
| suppression coverage | "The `assumed_formation` suppression accurately covers all paths" | "`assumed_formation` as specified does **not** cover (1)(2)(5) without the O4/O1 C1 wording." | rows 8, 9: Gemini's DOES NOT HOLD |
| store | "I would build the desk-written vault note … obeys L65 strictly." | "R15 is **not** a L65 write instruction. Build the L28 Cobalt-owned unit (O5)." | row 17b: a ruling, not decided here; "strictly" DOES NOT HOLD |
| WRONG FACTS | "None found." | three listed | rows 6, 25a |

## Experiments named (L70)
| experiment | named by | gates (house's claim) | result that would change the design |
|---|---|---|---|
| X1 premarket-seed viability | proposal, grok (R1) | C3 / C5 | Low share ⇒ earliest windows stay empty; report the rate. |
| X2 does `cobalt_dev` hold i1 for tagged trade days | proposal, grok (R1) | C1 fixture choice | None held ⇒ C1 fixture is a checker-confirmed pool day. |
| X3 C1 `--replay` over the last 10 sessions | proposal, grok (R1) | C1 deploy | Zero rubberband formations allowed (proof ESCALATE 2), not a defect. |
| X4 mirror equivalence on stored days | proposal, grok (R1: on its replacement property) | C2 | A fail that is only the old property test is not a defect. |
| X5 scan latency, doubled evaluation × pool | proposal, grok (R1: 700 evaluations), gemini (restates X1–X5; "measured" wording is wrong, row 24) | C2 | p95 over 100 s ⇒ sequential frames / smaller pool, never a silent miss. |
| X6 negative-price `Bar` | grok (R1), **gemini** (same experiment; adds "if `ge=0`, the frame needs a shadow model") | C2 Frame | A raise ⇒ Frame wraps `WorkingBar` only; row 5: only `volume` carries `ge=0`, DB CHECK unread. |
| X7 replay version mismatch | grok (R1, called settled) | C1 gate 5 | R1 hub check stands (`replay/formations.py:81,145`). |
| X8 form a card on an assumed key, flip its source, assert suppression persists | grok (R1) | C2 | Card gains a score ⇒ persist suppression (row 8). |
| (hub, unrun) A-07 literal reading effect; `Decimal % 10` on negative cents | R1 hub | — | Gemini's "impossible" (row 18) is the claim that this run would settle. |
Gemini named no experiment beyond X6. Astra: none.

## OWNER ITEMS (after cards)
Gemini's `OWNER (after cards):` list, verbatim (nothing needed redacting — keys only):
- Confirm A-07 micro-Range consolidation termination reading.
- Confirm A-01 orientation rule (all 7 setups trade against immediate Extension).
- Confirm radar in-play admission satisfies 9-EMA catalyst requirement (A-13).
- Confirm premarket seeding for early-window indicators (A-05).
- Confirm tie policy sorting for WATCH cards with suppressed scores.

Astra: none. No item is written as a precondition to build; nothing conflicts with R15 / R17. Note: the second item carries the claim in row 2 (DOES NOT HOLD) inside its parenthesis.

## WRONG FACTS claimed
| # | Gemini's claim | hub file-check |
|---|---|---|
| — | "None found. The proposal's claims regarding `valid_setups` schema, consumed sets holding premarket bars, and `tunables.yaml` null rows strictly match the staged files." | The three named points HOLD (row 25b). "None found" DOES NOT HOLD: `atr_working` is taken today (row 6, `evaluate.py:568`) and the proposal's same-side reading (`PROPOSAL:265`) is not true for the four with-trend defs (row 2). |
Astra: none.

## Independence
- `grep -c -F -e "grok-ruling" …/r1/gemini-ruling.md` = **0**.
- Astra: no ruling file exists (`astra-ruling.md`, `astra-ruling.partial.md` absent — `ls` exit 1). `grep -c -F -e "grok-ruling"` on astra's background output = **0** (it held one line and lists no opened file).
- No `READ ANOTHER RULING` finding. (Gemini's transcript was not searched: the prompt names the ruling files and astra's output only.)

## ESCALATE
1. **ASK DESK: astra did not rule R1B (`TIMEOUT` — only `Reading additional input from stdin...`, unchanged from 11:52 to 14:51 ET, stopped by TaskStop) — astra has now had its one attempt on this packet; take the derive with the seats that ruled, or bring him the question?** [14:53 ET] Safe default taken: no retry by me. **ASTRA IS REQUIRED — the derive (25) refuses; the desk brings him the two-house question.** Astra's cause of hang is UNPROVEN (`## CONTINUE`); a retry that closes stdin needs a rule outside the approved list (desk/Dejan's call). L67: a house that produced no ruling has not used a round.
2. **Gemini's `BUILD` (no item REJECTED) rests on claims that DO NOT HOLD: rows 2, 4, 6, 8, 9, 10, 17b, 24, 25a.** Most consequential: the "all seven against the Extension" reading (row 2) contradicts Grok's R1 `BUILD AFTER` and the four with-trend defs' definitions — a wrong-side card risk if applied beyond the proposal's own scoping. It is not a `DO NOT BUILD`, so it is not counted as a blocker by the closing-line formula (0); it is listed because Gemini's ADOPTs on (a), (b), (c), (d) cannot be taken as agreement with the proposal on these points.
3. **A number reaching a card unmarked that HOLDS (L52 (a)):** assumed-value reads outside the recorder — `_cfg_value` at `evaluate.py:653,656`, `ExtensionParams.from_tunables` at `:528` — and a `refresh_card` that recomputes the suppression from dots (`:777-800`). Gemini says the design covers all paths (rows 8, 9): DOES NOT HOLD. Grok's R1 ESCALATE 3 (A-01) remains open. Two houses now disagree with the proposal's recorder; the proposal's own text (`PROPOSAL:161`) puts the recorder on the interpreter `cfg` only.
4. **Conflict between houses on the store (L65 vs R15):** Gemini builds the desk-written note ("obeys L65 strictly"), Grok builds the L28 command; `LAWS.md:335` and `PROPOSAL:177` read against Gemini's "strictly" (row 17b). Which house's reading applies is his or the desk's under L73; not decided here.
No `DO NOT BUILD`, no `REJECT`, no second ranking authority claimed, no owner item written as a precondition, no packet mismatch, no independence breach.

SETUPS TRIBUNAL R1B DONE · gemini: TRIBUNAL R1: BUILD · astra: TIMEOUT · houses that ruled: 1 of 2 · round 1 total: 2 of 3 + Fable · claims that HOLD: 16 · blockers to build: 0 · owner items: 5 · ESCALATE: 4
