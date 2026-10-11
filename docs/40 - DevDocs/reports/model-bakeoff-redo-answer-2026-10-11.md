# Model bake-off redo · brain direction · 2026-10-11

His words: R1008 and R1009 (`reports/cto-2026-10-11-words.md:3-7`). He wants, per model, the complexity it can BUILD: Sol, Opus 5.5, Sonnet 5.5, Terra, Grok 4.7. Nothing below Sonnet or Terra. Gemini only if Gemini 4 has rolled out and can sit. FINAL `3c3c37f6` (Grok only) is set aside. Its harness, cards, bands and pass bar are reused below, because they were ruled once and still fit.

## PURPOSE (his clarification, 2026-10-11, brain session)
His words: "the point of the bake-off for the models is not to exclude models from the build, but to understand at what complexity of a item that needs to be built, we can do it with the other models that are not always Opus 5.5."
The output is therefore a ROUTING table and not a ranking. For each band (LOW, MID, HIGH) it lists every model that builds it AT LEVEL (and those CLOSE BELOW, with a review), so a card of that band can go to a model other than Opus 5.5. No model is "failed". A NOT YET cell only means "not this band, on this evidence". The routing itself takes effect only on his word on the result (L29).

His next words, same session: "Within that tribunal, I especially want to check Grok 4.7 because we have a much bigger meter on that one. And can be used in many, many other areas."
So Grok 4.7 gets the deepest arm:
- **Builds:** TWO cards per band instead of one (six builds). The three common cards plus one more checked card per band, chosen by the proposer from the round-1 sample: no migration, each in a different file area. That makes n=2 per band for Grok, still printed as "insufficient data".
- **Other areas:** Grok is also tried in the non-build roles a seat fills here. Each result is graded against the Opus or Sonnet seat that did the same job, never merged or launched:
  - DRAFTER: write one card from an existing FINAL, compared on its preflight result with the real drafter's card.
  - PREFLIGHT: read two already-preflighted cards, one of them with a planted mismatch. It must catch the plant (Astra's `[F-14]` rule).
  - JUDGE: answer one past build report's `## DECISIONS`, compared with the brain's recorded answers.
  These are write-free except for the drafter card, which goes to a scratch path, so they need no new command class beyond the Grok string the shadow launcher already carries.
- **Order:** the Grok arm runs first, ahead of the other models, on its larger meter.

His next words, same session: "we don't need to build anything with Opus or Sol. We already know that Opus and Sol are at the same level of build. We need to test Terra and Sonnet rather than making tests across the board. We can assume that Sol and Opus can build anything."
This SUPERSEDES the Opus and Sol arms below:
- Arms: Grok 4.7 (deepest, run first), Sonnet 5.5 and Terra. Gemini 4 only per (a). No Opus or Sol rebuilds.
- Opus 5.5 and Sol are recorded as "can build every band" by his word, not measured.
- Baseline: each card's ORIGINAL Opus build and its check (held findings, fix rounds, tokens). Caveat, printed once in the table: the originals ran their own commands, while the arms write only and an Opus gate seat runs the commands, so a small difference can be the harness and not the model.
- The OpenAI meter is now needed for the Terra arm only.

## §0 Headline
- Every model rebuilds the SAME three cards under the SAME harness, Opus 5.5 included, so the results compare models and not harnesses.
- "Can build band X" is read from the three grades already ruled (AT LEVEL / CLOSE BELOW / BELOW), printed per model and per band with "insufficient data".
- The OpenAI arms (Sol, Terra) need meter that he expects to be gone. They run when the meter allows, which is his word. The Anthropic and Grok arms run first.

## (a) MODEL IDS
- The desk proves each id before any card names it: `~/.codex/models_cache.json` for `gpt-5.6-sol` and Terra's exact id, the `grok` CLI for `grok-4.7`, the `claude` model list for `claude-opus-5-5` and `claude-sonnet-5-5`, and the Gemini seat's own model list for a Gemini 4 id.
- No id is guessed. An id that cannot be proven is recorded `N/A — id not found (<where read>)`, and that arm does not run.
- Gemini 4: the arm exists only if a Gemini 4 id is listed AND a one-word probe answers. Otherwise it is recorded N/A, which is his "unless" and not a question.

## (b) CARDS AND HARNESS
- **Cards:** the same three for every model, each from its own BASE: `strike-fallback-env` (LOW 2), `radar-display-fix` (MID 5) and `s4-p1` (HIGH 13), as in FINAL §2.1. There are no migration cards (`[F-02]`).
- **Harness, one for all models:** the model WRITES files only. A fresh Opus 5.5 gate seat runs every command (RED FIRST, the three suites, the with-DB gate under the L76 lock) and feeds failures back. The re-pass cap is 2 per card (S6). The gate seat never repairs code (S6). Harness reds are INCOMPLETE (`[F-31]`).
  - Why Opus rebuilds too: the originals were built by an Opus session that ran its own commands, a different harness. An Opus rebuild under this harness is the fair baseline. It also measures the checker's run-to-run spread (X8).
  - Why Sonnet does not run its own commands: L29 puts every DB write path on Opus or higher. The with-DB gate is a DB write path, so it stays the Opus gate seat's for every arm. Sonnet writing files on a branch that is never merged is the trial he ordered (R1008).
- **Branches:** `shadow/<job>-<model>`, never merged, never deployed.
- **Launcher, one card:** extend the SHADOW-HUB card to one launcher kind with a model switch, `desk-launch.sh shadow <card> --model <grok-4.7|gpt-5.6-sol|<terra id>|claude-sonnet-5-5|claude-opus-5-5>`. Each model's write-only CLI string has its write glob limited to its own shadow worktree:
  - `grok -m … --sandbox cobalt-job --allow "Write(<wt>/**)"`
  - `codex exec -m … -s workspace-write` (confined to the worktree)
  - `claude -p --model … --allowedTools "Read" "Edit(<wt>/**)" "Write(<wt>/**)"`
  These strings are NEW COMMAND CLASSES (R411). R1009 approved the waiting builds and deploys, not a new command line. So the card's launch line gets his ONE sign-off when it is built and checked, the BUILD-HUB pattern. I ask him for it then.
- **Check of each shadow build:** the existing CHECK-HUB flow, which is Grok-first once card 298 is deployed. The check of a Grok-built card counts Grok's own findings apart (`[F-03]`).

## (c) PASS BAR, per model and per band
- Grades, counted on the Opus check's held findings against the Opus original's (`[F-04]`, `[F-30]`):
  - AT LEVEL: no extra held finding.
  - CLOSE BELOW: exactly one extra.
  - BELOW: two or more extra, or a red from the model's own code after 2 re-passes.
  - INCOMPLETE: a harness red.
- **The answer he asked for, per model:**
  - CAN BUILD: the highest band graded AT LEVEL, with every band below it AT LEVEL or CLOSE BELOW.
  - CAN BUILD WITH A REVIEW: a band graded CLOSE BELOW.
  - NOT YET: a band graded BELOW.
- The table has one row per model, LOW/MID/HIGH across, plus tokens and wall time per build (the cost he weighs against Opus). Every cell is printed with "insufficient data (n=1 per band)" (L8). It is an indication for his word, not a routing rule.

## (d) BANDS
- Keep LOW 0–2 · MID 3–6 · HIGH ≥7 frozen, descriptive only (`[F-13]`, Astra's wording). No cut point moves on these results.

## THE TRIBUNAL REDO
- One round on the amended design (this file plus FINAL's reused sections). Every house is now also a subject, so each house's ruling on its own vendor's models is recorded apart and not counted on that item: Grok on Grok, Astra on Sol and Terra, the Anthropic seat on Opus and Sonnet.
- Houses: Grok plus the blind Anthropic seat, plus Astra only if the OpenAI meter allows (R1009 approves Sol seats the brain requires; Astra is a tribunal house, so it is used if the meter is there).
- Then the SHADOW-HUB card (extended), his one sign-off on its line, then the arms.

## ORDER OF ARMS
1. Opus 5.5 (the baseline), Grok 4.7 and Sonnet 5.5: no OpenAI meter. They run in parallel up to the Grok cap of 3 and one with-DB gate at a time (L76).
2. Sol, then Terra: each needs about three builds' worth of OpenAI meter. They run when the meter shows room. He expects it gone after the tribunal, so these two arms wait on the meter. The desk records the date the meter returns, not a question to him.
3. Gemini 4: only per (a).

FOR THE CHECK: model bake-off redo brain 10-11 — all five models rebuild the same three cards (LOW/MID/HIGH) under one write-only harness with an Opus gate seat (L29), Opus included as the same-harness baseline; ids proven before use; Gemini 4 only if listed and probed; grades AT LEVEL / CLOSE BELOW / BELOW / INCOMPLETE give CAN BUILD / WITH REVIEW / NOT YET per band, n=1 per band; bands frozen; SHADOW-HUB extended with a --model switch, new command line on his one sign-off; OpenAI arms run when the meter allows; each house's ruling on its own models recorded apart.
