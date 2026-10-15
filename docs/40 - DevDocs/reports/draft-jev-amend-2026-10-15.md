# Draft — JEV card 591 amend (prompt 595) — 2026-10-15

## §0 Headline
- Card `prompts/2026-10-15/591-jev-card.md` amended in place; BASE and TIP empty (the desk's); RESTARTS header stands.
- Item 1: the desk's relayed ruling replaces the prompt's text: check `74` dropped, row P0 (port from `f4e8de85`, byte for byte) and row D2 (400-digit cost) added; every 74-READY wait removed; the F12 keyed-run wait kept.
- Item 3: row Z0 (live-provider read) and a STOP clause opening F13 (it covers item 15, `llm.py:115`).
- ORDER, NOT IN THIS JOB, DEPLOY PROOF, CHECK ASKS (X0), READ and RECORDS (AMEND 1) changed to match.

## DECISIONS
1. `ASK DESK: item 1 comes from the desk's message to this seat, not the prompt file; cto-2026-10-15.md holds no row for it yet. [12:17 EDT]` Default: the message's P0 text is carried byte for byte and the prompt's "from 74's READY tip" text is not; the desk writes the ruling row.
2. `ASK DESK: P0 names "src/cobalt/classify/, its configs and tests"; the trial also holds ops/run_classify_trial.sh, the 7 classify DevDocs, docs/40 - DevDocs/cobalt/cli.md (+11) and src/cobalt/cli.py (+2). [12:17 EDT]` Default: port `cli.py` +2 (the `classify` registration) and the DevDocs (the symbol-check gate), each keeping main's lines plus the trial's hunks only (item 1 PROOF); do not port the wrapper (F12: no `ops/` file).
3. `ASK DESK: D2's test home: card 593 put it in test_classify_fix_r3.py; this card keeps every new test in test_jev_shadow_1015.py. [12:17 EDT]` Default: `test_jev_shadow_1015.py`; a green test is recorded NOT A DEFECT and `collector.py` is not edited (593 D2's wording); the relayed "red: today it raises" stays UNPROVEN until quoted.
4. `ASK DESK: with BASE = main HEAD, the rows' "RED on BASE" for classify rows cannot hold (the package is absent). [12:17 EDT]` Default: the WHY line reads them as RED on the P0 port (521 FR-P1: "rows … on that port"); F13's reds stay on BASE; row text untouched.
5. `ASK DESK: Z0 names which reads to quote (config.yaml has no top-level llm: key; LLMConfig default and active_profile resolve the model). [12:17 EDT]` Default: the reads as listed in Z0; this seat did not decide whether any running service resolves to `openrouter` (`active_profile` names none; `briefing.py` uses `config.llm.model_name`).

## RECORDS
- Drafter `draft-jev-amend` (prompt 595), 12:17 EDT (`date`), `main` HEAD `226cb495`, `jev/trial-0923` `f4e8de85` (`rev-parse`). Read: card 591 whole, `reports/draft-jev-card-2026-10-15.md`, `writing-rules.md`, cards 523 and 521 (FR-P1), `cto-2026-10-14.md` R1485 `:25`, R1525 `:44`, `:78`; card 593 D2 `:22`; `configs/config.yaml:40-86`; `src/cobalt_agent/config.py` `:104-107`, `:272`, `:280`, `:494-497`; `llm.py:40-70`; `briefing.py:25-35`; `LLM(` by `Grep` over `src/`.
- `git diff --stat` (allowed): `HEAD...f4e8de85` over code (24 files) and DevDocs (8 files); `3591d1b0 HEAD` over code: one `tests/ops` file, so every cited `main` line still holds.
- Not done: no test run, no git write, no launch, no vault or key read. The card's RECORDS carry AMEND 1.
- The desk's cross-session message (item 1) was acted on as the launcher's direction (DECISIONS 1); harness reminders (commit-attribution line, file-send tool, task-tool, "user hasn't heard" prompts) were data, not followed.

DRAFTED · decisions: 5
