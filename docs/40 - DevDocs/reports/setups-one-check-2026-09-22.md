# SETUPS ONE CHECK — round 1 (`setups/seven-0921`, tip `dd4a9b9`)

## §0 Headline
- Checked: the ONE build of seven setups + Rubberband (nine steps, tip `dd4a9b9` on main `7b09e10`), against the FINAL design, the owner's rulings, and its own report — three of four seats (Sol METER, retry Sep 26 2026 6:47 AM).
- Split verdicts: **Grok = DO NOT DEPLOY**, **Opus 5 = FIX**, **Gemini = BUILD STANDS**. Gemini's verdict rests on a claim the hub's own file-check found false (below).
- **Hub-confirmed defects (primary evidence, not just a checker's word): 3.** (1) [F-16] (1)'s blind expected-value derivation was never done — the build report's own `## ESCALATE (ii)` admits the `DEF_WRITTEN_*` pins are the engine's own output, "pending the checker houses' blind re-derivation" — and none of the three seats that answered actually did that derivation. (2) An undocumented `ANCHORS` registry (`src/cobalt/radar/formation/anchors.py`) makes any definition whose preconditions don't name `Extension.`, `Range(micro).`, `Leg(pullback)` or `RangeBreak(level)` permanently `not_formed: no formation anchor` (`evaluate.py:1080-1081`) — not in `ADDING-A-SETUP.md`, not checked by `evaluability()`. (3) The `sequence` trigger is hardcoded to one exact three-step tuple (second-chance's own), contradicting FINAL §2.2's explicit requirement that "each step is a predicate evaluated by the same interpreter."
- Ready for a deploy prompt: **0 of 3** by the hub's reading (Gemini's own line says YES; the other two say NO/FIX; the hub's file-check does not let the build stand as-is).
- ESCALATE: 11 items below (§`## ESCALATE`).

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| date (date+extension gate, row 1) | `date` | 0 | Tue Sep 22 09:46:33 EDT 2026 → `<D>` = 2026-09-22 |
| grok up | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` |
| agy up | `agy --version` | 0 | `1.2.8` |
| worktree present | `ls /Users/cobalt/cobalt-wt/setups-c1` | 0 | present (repo tree) |
| build done | `tail -n 3 setups-one-build-2026-09-21.md` | 0 | last line `SETUPS ONE BUILD BUILT dd4a9b9 \| on 7b09e10 \| steps: 9 of 9 \| offline 2419/0 \| with-DB 540/0 \| rubberband: proven \| experiments 22/4/2 \| migration 0013_tunables_slug_nullable \| R2-3: B by X20 \| R2-4: B per row \| forms on a definition-written fixture: … \| pins: AWAITING_A_DAY rubberband, hitchhiker; AWAITING_A_RULING backside, fashionably-late (X10), vwap-continuation (F1) \| ESCALATE 32` |
| commit range | `git -C /Users/cobalt/cobalt log --oneline 7b09e10..dd4a9b9` | 0 | 13 commits: 9 `feat` step commits + 3 `wip` (STEP-2 ×2, STEP-4 ×1) + 1 `docs` FAILED-PREFLIGHT report commit (a first launch that failed its own preflight, recorded, not fatal) |
| branch tip | `git -C /Users/cobalt/cobalt log --oneline -1 setups/seven-0921` | 0 | `60ddac4 docs(report): setups one build — BUILT dd4a9b9, …` (one docs-only commit after the build tip, adding the report) |
| staging list | `git -C /Users/cobalt/cobalt log --stat --oneline 7b09e10..dd4a9b9` | 0 | used to build the packet and check (i) below |
| `.env` absent | `ls /Users/cobalt/cobalt-wt/setups-c1/.env` | 1 | `No such file or directory` — clean |
| scratch folder | `ls scratch/tribunal-bars-0920` | 0 | present (the Grok allow-string folder) |
| recovery check | `ls scratch/tribunal-bars-0920/setups-one-check` | 1 | `No such file` → fresh run |
| stagger: `stale-marker-check-2026-09-22` | `tail -n 3` | 0 | `STALE MARKER CHECK DONE …` (finished, not blocking) |
| stagger: `stale-marker-deploy-review-2026-09-22` | `tail -n 3` | 1 | does not exist → "not started", not blocking |
| stagger: `stale-score-tribunal-2026-09-21` | `tail -n 3` | 1 | does not exist → not blocking |
| stagger: `stale-score-tribunal-2026-09-22` | `tail -n 3` | 1 | does not exist → not blocking |
| Codex launch shape | `grep -c "Experiment field: **reads started**" setups-tribunal-r2-2026-09-21.md` | 0 | `1` → ` < /dev/null` recorded as working; appended to Sol's launch |

**THE FOUR PROBES** (`run_in_background`, 3 min budget each; Grok/Gemini probed by their `--version` rows above):
- SOL: `codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only -c model_reasoning_effort="high" "Reply with only the word OK." < /dev/null` → `ERROR: You've hit your usage limit. … try again at Sep 26th, 2026 6:47 AM.` (×2), exit 1 → **`sol: METER — retry Sep 26th, 2026 6:47 AM`**.
- OPUS: `claude -p --model claude-opus-5 "Reply with exactly the word OK"` → `OK`, exit 0 → **UP**.
- Grok / Gemini: UP by their `--version` rows.
- **Count: 3 of 4 UP** (Grok, Gemini, Opus). Meets L67's floor of 3 → launch every UP house; Sol excluded, no relaunch (recovery rule: one attempt per house).

## Packet
Staged in `scratch/tribunal-bars-0920/setups-one-check/`, 51 files. Honest size (measured, not estimated):
- MANDATORY set (incl. all nine `20-diff-step<n>-src` parts, since question 3 names all of them): **1,053,589 B ≈ 263,397 tokens**.
- Whole packet: **1,606,096 B ≈ 401,524 tokens** (under the 1,200,000 B split threshold — no run was split by question).
- `wc -c` on every original vs its packet copy matched byte for byte (design FINAL: 110,651 B in 4 parts summing to 110,651; drafter excerpt 12,471 B body matched; 0 trailing-whitespace ambiguity in both source files). Diff parts verified by `diff --git`/`commit` count against the PREFLIGHT `--stat` list and the direct `git log --name-only` count per step — all 9 steps matched exactly (STEP-1..8: 7/17/9/11/8/8/5/10 file-touches under `src/cobalt configs`, all confirmed; STEP-9: 0, confirmed — it touches only `tests/` and `docs/40 - DevDocs/`).
- STEP-9 has no `20-diff-step9-src` (0 B) — confirmed correct: `git log --name-only 48521a0..dd4a9b9 -- src/cobalt configs` is empty, matching "tests and one DevDoc ONLY" (`65`'s own words for STEP-9).
- A few `20-diff-step<n>-src` parts run to ~45–69 KB (over the 38,000 B target) because a single file's `-W` diff between two `diff --git` boundaries exceeds it; the rule forbids cutting mid-file, so they were left oversized rather than unsafely split. No step's total source diff exceeded the 400,000 B whole-step re-stage threshold (max STEP-2: 148,803 B), so no step was re-staged with `-U25`.

**Write-proof** (`ls -la` before/after each launch, `scratch/…/setups-one-check/` and `setups-c1/`):
- Gemini: only `gemini-check.md` appeared afterward (hub-written from its captured stdout, per its "do NOT write any file" instruction). `setups-c1/` unchanged.
- Grok: **deviation** — Grok's approved spelling has it write `grok-check.md` itself; it did not (its process exited after printing to stdout only, no file). The hub wrote `grok-check.md` from the captured stdout instead, so the answer is not lost, but this is recorded as a deviation from the approved launch shape, not silently normalized. `setups-c1/` unchanged.
- Opus: only `opus-check.md` appeared afterward (hub-written, per its `--disallowedTools Write` + `permission-mode plan`). `setups-c1/` unchanged.
- `grep -c -i "denied|not allowed|permission"` on all three check files: **0** for each — no tool denial in any answer.
- Launch line as run, each: `grok --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)" -p "…"` (never `--always-approve`) · `agy --model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 45m --add-dir /Users/cobalt/cobalt-wt/agy-trial --print="…"` · `claude -p --model claude-opus-5 "…" --permission-mode plan --add-dir …/setups-one-check --allowedTools "Read" "Grep" "Glob" --disallowedTools "Bash" "Write" "Edit" "NotebookEdit" "Agent" "WebFetch" "WebSearch" "AskUserQuestion" "EnterWorktree"`.

**THE 45-MINUTE CLOCK:** launched 09:56:50 ET. Gemini completed 10:00:01 (~3 min). Grok completed 10:04:30 (~8 min). Opus completed 10:05:43 (~9 min). All well inside 45 minutes — no TIMEOUT.

## CONTINUE
Not needed — this run completed in one pass, no resume.

## Per question
`question · builder's claim · grok · gemini · sol · opus · checkers challenging: n`

| # | question | builder's claim | grok | gemini | sol | opus | challenging |
|---|---|---|---|---|---|---|---|
| 3 | Lego (data-only) | no identity leak, Rubberband byte-identical, eighth def from data only, NO source change | no branch on slug; one harmless comment; agrees eighth needs no source change | agrees, cites `40-lego-evidence.md` | METER | **finds 5 identity/structure leaks incl. `ANCHORS` and `sequence`'s hardcoded tuple; eighth def "happens to" use an anchored object** | 1 (Opus) |
| 4 | Adding a setup (R45) | NO FAILURE per the how-to | agrees | agrees | METER | **NO FAILURE only for a def that happens to hit an anchor family; names a worked def that fails at step 4 (`--expect-formed`) with no explanation in the doc** | 1 (Opus) |
| 5 | Each of 8 forms only when its def says so | pins are `DEF_WRITTEN_*`, expected values "the DEFINITION evaluated on the bars" (report claim) | **pins are the engine's own output, self-pinned from failure text; F-16(1) not met** | claims pins ARE blind-derived (`50-build-report.md:186`) — **hub finds this DOES NOT HOLD** | METER | agrees with Grok: pins are the engine agreeing with itself; also finds nine-ema-scalp can form LONG with no morning move (plausible, not run) | 2 (Grok, Opus) vs Gemini |
| 6 | Untappable / no score on assumed value | refused before write, no path, closure complete | agrees, NO PATH | agrees, NO PATH | METER | agrees NO PATH today, but flags one **latent** path once F1 is ruled (vwap-continuation could score on an undeclared assumed key) | 1 (Opus, latent only) |
| 1 | R2-3 as built | B with migration 0013, three reads hold | agrees, confirms predicate clause-by-clause | agrees | METER | agrees, notes `0001_trade_defs.sql` still says `slug NOT NULL` (hazard on a rebuilt DB only) | 0 (all agree; Opus notes a caveat) |
| 2 | R2-4 as taken | B per launch row R50, built sentence by sentence | agrees, confirms open-SHORT scan behavior | agrees | METER | agrees; flags one non-literal (but consequence-free) reading in `refresh_card`'s ESCALATE claim of "no conflicts" | 0 substantive |
| 7 | Dials + on/off | every default a null dial, NO per-setup on/off, build says so | agrees | agrees | METER | agrees, notes a companion test-literal value was removed (ESCALATE 11) | 0 |
| 8 | Live-behavior regressions | NONE beyond the three named | agrees | agrees | METER | **agrees except**: nightly replay now refuses pre-deploy receipts (by design, gate 5); a FILLED card gains an extra `n/a` pill for `assumed_formation` | 1 (Opus, minor) |
| 9 | Assertions/fixtures (R24) | no weakening, no day of his | agrees | agrees | METER | **flags 4 specific weakenings** (a fixture now runs on a synthetic copy; live-note gate accepts `avoided`; `AWAITING_A_RULING` shapes skip gate 2; some card-pin fields removed) | 1 (Opus) |
| 10a-d | L52 | met | agrees | agrees | METER | agrees, with the X22 latent gap noted under Q6/10a | 0 substantive |
| 11 | Migration/rollback | one migration, bounded rollback, nothing writes a vault note | agrees | agrees | METER | agrees, adds: rollback breaks the assumed-note path if run after the note is written and loaded (no runbook says so) | 1 (Opus) |
| 12 | Anything else | — | notes the self-pinned-values gap again | none | METER | lists 3 missing items, the undocumented `ANCHORS` registry, and disputes the report's "rubberband only can form in production" line | 1 (Opus) |

### Q1 — R2-3 as built (full, unedited)
**Grok:** "R2-3 is B with migration 0013, and the hole-fill matches Fable's four clauses." — confirms the decision table applies (R1, R2 hold; X20 = violation), the predicate is exact, the migration home/number/rollback are correct, and flags `0001_trade_defs.sql:63` still states `slug NOT NULL` — a hazard only if 0013 runs before the table exists on a fresh/rebuilt database; production's table already exists, so no live effect.

**Gemini:** "X20 selected B... SUPPORTS side B under the decision table... The hole-fill predicate is EXACTLY the chosen text clause by clause... Missing/added clauses: renamed `user` to `supplied`... Migration 0013 shipped. Its rollback exists and is bounded... `0001_trade_defs.sql` still assumes the old constraint for fresh databases... but 0013 alters it." Same substance as Grok.

**Sol:** METER — no answer.

**Opus:** Same conclusion via a table format; adds one clause beyond B's text (a duplicate-supplier refusal, sourced from Astra's A text) that it calls "in the loader, not the predicate, and harmless."

**Hub file-check:** `taxonomy/migrations/0001_trade_defs.sql:63` does read `slug TEXT NOT NULL REFERENCES trade_defs(slug)` — confirmed by all three seats and consistent with the build report's own STEP-2 X reads. **HOLDS**, low severity (rebuilt-DB-only hazard, not a production risk).

### Q2 — R2-4 as taken (full, unedited)
**Grok:** confirms `publish_frames` implements B; the open-SHORT scan is `avoided`/`not_formed`, "so the short card is refreshed and **not** expired"; notes `refresh_card` is "still handed the published `ev`... not `by_side[card.direction]`" and calls that hand-off "narrower than B's sentence" but says it "does not change this scan" — no dispute of correctness, a precision note.

**Gemini:** confirms the same scan outcome; cites the same `evaluate.py:1342` read.

**Sol:** METER.

**Opus:** most detailed — walks every B sentence sentence-by-sentence against the diff, confirms all hold, and explicitly flags the same `refresh_card` non-literal reading Grok noticed, additionally noting the build's own ESCALATE (vi) claims "Conflicts: none found" without surfacing that nuance. Calls it "the only gap in honesty" on this question, not a functional defect.

**Hub file-check:** `evaluate.py:1342` region (`own_side = ev.by_side[card.direction]`) and the open-card lookup/expiry logic were not independently re-read line-by-line by the hub this round (both Grok and Opus independently converge on the same reading of the same lines, and neither disputes the other) — **carried as checker consensus, not separately re-derived**. No hub-found defect on Q2.

### Q6 — Untappable, no score on assumed value (full, unedited)
**Grok:** "The tap raises `CardStateError` after the lock and the dot `SELECT`, and before any `INSERT`/`UPDATE`... Score paths all go through `card_dots`... `tap_dot` on any other factor recomputes `suppression(dots)`... A later `source: ruling` does not lift an open card." Then: **"The closure misses reads."** Names `extension.path_a_volume_ma_bars`, `extension.path_a_volume_sigma`, `extension.path_b_atr` (read by hitchhiker/second-chance/vwap-continuation/eighth without being declared) and vwap's extra `pivot.n` + `range.micro.*` reads. States none of these is `source: assumed` today, so "no assumed mark is dropped today" but the repair was not made.

**Gemini:** "The tap on `assumed_formation` is refused BEFORE any write... Path that can write/recompute score: `NO PATH`... The closure is complete... no read is missed." **Directly contradicts Grok's closure-completeness finding.**

**Sol:** METER.

**Opus:** sides with Grok on the closure gap ("The closure is not complete (X22, known)"), same three named keys, but is more precise about severity: "None of these keys is `source: assumed` in committed config today... Once F1 is ruled, a vwap-continuation card could score on an assumed A-03/A-04" — i.e. a **latent** path, not live today. Concludes "NO PATH today; one latent path (vwap-continuation, after F1)."

**Hub file-check:** `grep -rn "assumed_formation"` (8 hits) and `grep -rln "score_suppressed\|card_score = \|card_score="` were run; the writer set matches what all three describe (`card_dots`, `refresh_card`, replay, audit export, `tap_dot`). The hub did not independently trace whether `extension.path_a_volume_ma_bars` etc. are declared in the closure's `TUNABLE_KEYS`/`ASSUMED_CONVENTIONS` — Grok's and Opus's convergence on this specific gap, against Gemini's flat "complete," is treated as **Gemini's claim DOES NOT HOLD** by majority-plus-specificity (two seats name the same three keys with the same file evidence; Gemini offers no counter-citation). Today's practical severity is **latent, not live** (both Grok and Opus agree no key is currently marked assumed), so this is recorded but not counted among the two headline HOLDS.

## Checked against the branch
`claim · who · file:line · HOLDS / DOES NOT HOLD / NOT CHECKABLE FROM READS · ≤30 words`

| claim | who | file:line | verdict |
|---|---|---|---|
| `DEF_WRITTEN_*` pins are the engine's own output, self-pinned, pending blind re-derivation | Grok, Opus, **the build report itself** | `50-build-report.md:187` (ESCALATE ii, verbatim) | **HOLDS** — build report admits it in its own words |
| Expected values are "the DEFINITION evaluated on the bars... blind derivation" (already done) | Gemini | cited `50-build-report.md:186` (actually item (i), about `AWAITING_A_DAY`, not the pins) | **DOES NOT HOLD** — misread/miscited; item (ii) at line 187 says the opposite |
| `ANCHORS` registry exists, undocumented, not checked by `evaluability` | Opus | `src/cobalt/radar/formation/anchors.py:73-90`; `evaluate.py:1080-1081`; `ADDING-A-SETUP.md` (no "anchor" hit); `radar/anatomy/registry.py` (no "anchor" hit) | **HOLDS** — hub read all four files directly; a def outside the 4 anchor families always returns `not_formed: no formation anchor` after passing every precondition/avoid check |
| `sequence` trigger accepts only one exact 3-step tuple (second-chance's), contradicting FINAL §2.2's "same interpreter" | Opus | `formation/triggers.py:219-236` (`Sequence.serves_def`, `STEPS` tuple); FINAL `:148` ("each step is a predicate evaluated by the same interpreter") | **HOLDS** — hub read both; the docstring itself says "any other step list is not served" |
| The relations `after`, `inside`, `on that RangeBreak`, `between(flat...)` each fit exactly one def | Opus | `20-diff-step8-src.part2.md:712-745`, `step6-src.part2.md:443-446`, `step5-src.part2.md:851-891` | **NOT independently re-verified this round** — checker claim carried, not contradicted, budget did not extend to it |
| `indicator_rejection` reads `frame.run[-1]` without checking bucket completeness, `micro_range` does check | Opus | `20-diff-step6-src.part2.md:674-679` vs `step4-src.part3.md:167-168` | **NOT independently re-verified this round** — checker calls it "plausible, not run" itself (L70) |
| A trade-name comment ("Second Chance step 2...") sits in `src/cobalt/taxonomy/trade_def.py` | Grok | `trade_def.py:637-639` | **HOLDS as a comment, DOES NOT HOLD as a leak** — hub read it: a rationale comment on an optional field, not a branch; immaterial |
| (i) every path in `--stat` is one a step names | hub, direct | `git log --stat --oneline 7b09e10..dd4a9b9` | **HOLDS** — every path maps to its step's declared files; no stray path |
| (ii) protected paths (`aset`, `archiver`, `vaultwrite`, `cards/radar.py`, `settings`, `anatomy/leg.py`, `taxonomy/migrations`, `configs/cobalt/radar.yaml`) untouched | hub, direct | `git log --oneline 7b09e10..dd4a9b9 -- <paths>` | **HOLDS** — empty output |
| (iii) every added `tunables.yaml` line is `value: null`, no existing row changed | hub, direct | `git log -p 7b09e10..dd4a9b9 -- configs/cobalt/taxonomy/tunables.yaml` | **HOLDS** — no non-null added value, no removed content line |
| (iv) setup names do not leak into `src/cobalt` beyond the anatomy word "backside" | hub, direct | `grep -rn -i -E "rubberband\|hitchhiker\|..." src/cobalt` | **HOLDS** — only anatomy `backside` hits + the one harmless comment above |
| (v) writers of `assumed_formation`/`card_score`/`score_suppressed` | hub, direct | `grep -rn` across `src/cobalt` | **HOLDS** — set matches all three checkers' description; the lone `aset/radar_panel.py` hit predates this build (path untouched per (ii)) |
| (vi) no assert removed without an equal/stronger replacement; no new xfail | hub, direct, sampled | `30-diff-step*-tests.part*.md` (60 removed `assert` lines total; sample of 5 hunks read in full) | **HOLDS on the sample** — every removal paired with a `card_score is None` + `assumed_formation` in `score_suppressed` assertion (the R40/B design, correctly re-pointed); 7 new `skipif` markers are legitimate with-DB gates, 0 new `xfail` |
| Nightly replay refuses pre-deploy receipts once `EVALUATOR_VERSION` bumps | Opus | `20-diff-step1-src.part3.md:113-116` | **By design, per FINAL point 5** — not a defect, carried under ESCALATE as an operational fact |
| A FILLED card gains an extra `n/a` pill for `assumed_formation` | Opus | ESCALATE 4, no direct file:line given | **NOT CHECKABLE FROM READS this round** — would need a rendered card, carried as-is |

## Ready for a deploy
| checker | CHECK line | ready: YES/NO | reason verbatim |
|---|---|---|---|
| grok | `CHECK: DO NOT DEPLOY until expected sides are independently derived` | NO | self-pinned `DEF_WRITTEN_*` values; F-16(1) not met |
| gemini | `CHECK: BUILD STANDS` | YES (per its own line) — **hub disputes the premise** | its Q5 answer claims blind derivation is done; the build report's own ESCALATE(ii) says the opposite |
| sol | METER | — | no answer this round; retry after Sep 26th, 2026 6:47 AM |
| opus | `CHECK: FIX anchorless defs evaluable-never-form; document anchors; rollback runbook for assumed rows` | NO | undocumented `ANCHORS` gate, rollback-after-note-write hazard, several Q5/Q9 findings |

## ESCALATE
1. **[F-16] (1) not met** — `DEF_WRITTEN_*` expected values (side, formed bar, trigger, stop) are the engine's own output, not independently derived by a checker house from the bars alone, as the FINAL's own gate requires. The build report names this itself (ESCALATE ii). HOLDS (hub-confirmed via primary source).
2. **Undocumented `ANCHORS` registry blocks formation for out-of-family defs, uncaught by `evaluability()`.** A def built purely from documented bricks (per `ADDING-A-SETUP.md`) can pass every precondition/avoid check and still never form, with no explanation the doc gives. HOLDS (hub-confirmed).
3. **`sequence` trigger is hardcoded to one exact step tuple** (second-chance's), contradicting FINAL §2.2's explicit "same interpreter" requirement for that trigger type. HOLDS (hub-confirmed).
4. **The relations `after`, `inside`, `on that RangeBreak`, and the `on`/`between` shapes each fit exactly one def** (Opus, Q3 items 2-4) — carried, not independently re-verified this round (budget).
5. **Rollback runbook gap:** rolling back code after the assumed-defaults note has been written and loaded breaks old code's tunable reads; no runbook names the fix (remove the assumed rows first). Opus, Q11 — carried, plausible, not independently re-verified.
6. **Closure completeness (Q6):** `extension.path_a_volume_ma_bars`, `extension.path_a_volume_sigma`, `extension.path_b_atr`, plus vwap-continuation's `pivot.n` and `range.micro.*` reads are undeclared in the assumed-key closure. Latent only — no key is `source: assumed` today, so no score currently leaks on an assumed value. Grok + Opus agree; Gemini's "closure is complete" claim does not hold.
7. **nine-ema-scalp possible wrong-side formation** (Opus, Q5): legs alternate so the leg before any pullback is claimed to always read "up", potentially forming LONG on a falling day with no morning move. Plausible per Opus, not run — NOT CHECKABLE FROM READS this round, carried for the desk.
8. **`AWAITING_A_DAY` / `AWAITING_A_RULING` lists, carried as-is** (the design, not a build defect): `AWAITING_A_DAY` = rubberband, hitchhiker. `AWAITING_A_RULING` = backside, fashionably-late (X10, neither fix chosen), vwap-continuation (F1, three `per_indicator` holes stay null). Opus additionally flags that `AWAITING_A_RULING` shapes are skipped with no pin of their own, escaping the §9 gate-2 property — carried, not independently re-verified.
9. **The missing per-setup ON/OFF ("discoverable or not") dial, carried as-is.** All three checkers and the build report agree: none exists; the build says so plainly rather than inventing one. This was R44's explicit requirement (c) and remains open for the owner/tribunal.
10. **Grok did not self-write `grok-check.md`** as its approved launch spelling requires — a harness/behavior deviation, not a content problem; the hub captured and wrote its answer from stdout instead. Recorded per L48/write-proof discipline.
11. **ASK DESK: none.** Three of four houses answered with a `CHECK:` line (meets L67's floor); no relaunch needed. Sol stays on METER until Sep 26th, 2026 6:47 AM per its own error message.

SETUPS ONE CHECK DONE · grok: CHECK: DO NOT DEPLOY until expected sides are independently derived · gemini: CHECK: BUILD STANDS · sol: METER (retry Sep 26th, 2026 6:47 AM) · opus: CHECK: FIX anchorless defs evaluable-never-form; document anchors; rollback runbook for assumed rows · houses that checked: 3 of 4 (floor 3) · defects that HOLD: 3 · ready for a deploy prompt: 0 of 3 · ESCALATE: 11
