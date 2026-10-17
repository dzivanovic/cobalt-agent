# draft-band-routing-fr2-check — report (2026-10-17)

## §0 Headline
- Card written: `prompts/2026-10-16/666-band-routing-fr2-check-card.md`, a CHECK of `ops/band-routing-1015` at code tip `fda2300b` (head `4fc9b9da`), BASE `f2ca3e1a`, shape of card 638.
- Rows S0, FR-6, FR-7, FR-8 (each a RUN with RED on the old code, `45b9d8c7`, and its control), E1 (FR-1 to FR-5 and B1-B6 short re-run), D1, R3, T1, G1 (`offline --deploy-gate`).
- Reads only; no test run, no mutation, no launch. 3 decisions for the desk.

## DECISIONS
- ASK DESK: the prompt's build report path `band-routing-build-fr2-2026-10-16.md` is absent; I used `band-routing-build-fr6-2026-10-16.md`, the report commit `4fc9b9da` adds (`REPORT:` header). Default: this path. [07:40 EDT]
- ASK DESK: the card's RED-before-the-fix rule restores old text from `git show 45b9d8c7:<file>`. The prompt says "the code tip's parent"; `45b9d8c7` changes the tests only, so its code equals `7bf43c2b`, and the new tests exist there. Default: `45b9d8c7`. [07:40 EDT]
- ASK DESK: house B. The card keeps `HOUSE B: as needed` and states that a Gemini-only candidate is N/A (id `gemini-3.1-pro-high` rejected, K5 card pending). The gate `log:` path is also owed to the desk (as card 638, ASK DESK 2). Default: the card as written. [07:40 EDT]

## RECORDS
- Date `Sat Oct 17 07:40:29 EDT 2026`; `main` HEAD `d8bdf960`. Branch log: `4fc9b9da`, `fda2300b`, `45b9d8c7`, `ac172ab9`. Worktree clean. `git diff --stat fda2300b 4fc9b9da -- . ":(exclude)docs"` printed nothing.
- Tip lines proved with `git grep` on `ops/band-routing-1015`: `desk-launch.sh:393`, `:991`, `:992`, `:994`, `:999`, `:2356`; `desk-watch.sh:65`, `:74`, `:110`, `:153`; `SHADOW-HUB.md:28`; test names and lines `:403`-`:639`; no `xfail` hit. The FR-1 arm is now at `:999` (the builder's report still says `:997`).
- Sources read: card 638, `CARD.md`, the fix-round-2 build report, card 583 rows FR-6 to FR-8 and `## RECORDS`, the tail of `band-routing-check-fr1-r2-2026-10-16.md`. Card 641 is DEPLOYED (`b57cbf8e`), the binding precondition.

DRAFTED · decisions: 3
