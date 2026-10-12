# Bake-off results stage — brain answer 2026-10-11

On desk R1126 (all shadow builds reported). It applies `model-bakeoff-redo-answer-2026-10-11.md` (c) and THE TRIBUNAL REDO, and SHADOW-HUB `## RESULTS TABLE`. Brain: the successor of `3d24c7e5`, on handover 349.

## §0 Headline
- No grade exists yet. A grade is counted on the shadow CHECK's held findings against the original's (redo (c), `[F-04]`), so every built shadow is checked first.
- Order: (1) shadow checks → (2) the desk fills the results table → (3) the results sitting (Grok, the blind Anthropic seat, Astra) → (4) the routing table goes to him. Routing takes effect only on his word (L29).
- Grok's two built cards are checked too, but are printed UNSCORED until he rules on "grok read".

## 1. SHADOW CHECKS (the existing CHECK-HUB flow, one fresh Opus check seat per build; houses as CHECK-HUB names them)
| card | model | band | tip | note for the check |
|---|---|---|---|---|
| 366 | Sonnet | LOW | `813036e8` | — |
| 369 | Sonnet | MID | `c289f478` | — |
| 372 | Sonnet | HIGH | `51fe6947` | first run red; 4 passes |
| 367 | Terra | LOW | `d02370df` | X1 PASS on the decoy (read reach recorded under his "terra read") |
| 370 | Terra | MID | `e544d94f` | — |
| 373 | Terra | HIGH | `9e3a133b` | with-DB 4959/1. The check says first whose red it is: the model's own code after 2 re-passes = BELOW (redo (c)); the lock, the DB level or `.env` = INCOMPLETE and one rerun on a clean harness (SHADOW-HUB :38) |
| 378 | Grok | LOW | `3e60d5f6` | UNSCORED until his Grok word; Grok's own findings counted apart (`[F-03]`) |
| 368 | Grok | MID | `ff0f2e0f` | the same |
- Concurrency: the `cobalt_dev` lock serializes the with-DB gates (L76). Grok houses are capped at 3 at once (R908). Sol may sit in checks (R1009) but is not needed: Opus plus Grok, with Gemini only if Grok fails (R920/R921).
- X12 and X9 (OWED at the first shadow check) ride the first of these checks.
- No PASS-2 and no fix round on a shadow. A shadow is scored, never repaired (SHADOW-HUB :37, :59; FINAL §2.2 step 6).

## 2. RESULTS TABLE
The desk copies SHADOW-HUB `## RESULTS TABLE` into `reports/complexity-shadow-results-2026-10-11.md` and fills it from the stop lines and the checks: builder tokens and wall time per build, and "insufficient data (n=1 per band)" in every cell (L8). Rows:
- Sonnet: LOW 366, MID 369, HIGH 372.
- Terra: LOW 367, MID 370, HIGH 373, with the harness line: `reads not confined to the worktree; accepted by his word ("terra read")`.
- Grok: LOW 378, MID 368 printed UNSCORED (`harness: reads not confined, X1 FAILED 365`); HIGH 371 INCOMPLETE (stopped); 365 and 379 INCOMPLETE.
- Opus and Sol: NOT MEASURED, his word R1019. Gemini: N/A, as the hub row says.
- Grok's role trials (drafter, preflight, judge): not run. They stay with the Grok arm, held for his word.

## 3. THE RESULTS SITTING (one round, after the table is filled)
- Houses: Grok, the blind Anthropic seat, and Astra (R1069 approves the meter use). It is one OpenAI seat; nothing else uses OpenAI at the same time (R908).
- Input: the filled table plus each check report's `## §0` and held findings. The originals' Opus-own held findings are the baseline (1 / 2 / 2).
- Each house's ruling on its own vendor's models is recorded apart and counts on no cell: Grok on Grok, Astra on Terra, the Anthropic seat on Sonnet.
- Output: the per-band lines of SHADOW-HUB :90-93, each reading CAN BUILD / WITH A REVIEW / NOT YET, as an indication for his word, not a routing rule.

## 4. TO DEJAN
The routing table, with his two open words beside it: Grok read (accept, or a sandbox fix and a re-run), and L27.

## FLAG
X1 365 showed that Grok's `cobalt-job` sandbox does not confine reads. If the Grok house in CHECK-HUB and the tribunals runs under that same profile, the same gap applies there. The desk reads `ops/grok-sandbox.toml` and the house's launch line and states in one line whether they are the same. This goes to him with the Grok question. The checks above are not held for it: the Grok house has run under that harness all along, and his "grok read" answer covers it.

## FOR THE CHECK
`bake-off results stage 2026-10-11 brain: shadow checks first on 366 369 372 367 370 373 (scored) and 378 368 (unscored); 373's with-DB red classified by its check (own = BELOW, harness = INCOMPLETE + one rerun); table per SHADOW-HUB; results sitting Grok + blind Anthropic + Astra, self-vendor apart; routing to his word; Grok house sandbox flag to him`
