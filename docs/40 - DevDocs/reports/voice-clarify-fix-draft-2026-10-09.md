# Voice clarify-and-confirm fix · draft · 2026-10-09

## §0 Headline
- Card `prompts/2026-10-09/193-voice-clarify-fix-card.md` written: rows A (doubled sentence), B (Confirm/Cancel CSS), C1 (measurement: candidates and history on a plan clarify), C2 (plan_shape, the brain's row text verbatim), D (restarts run).
- Two `«FILL»` gate the launch: `BASE`, and the PLAN_SHAPE ROWS production read (the desk's, R686) that row C2 is built from.
- Every `file:line` proven at `e4586978`; `main` `b7d37cdc` has no code change past it.

## CHANGES
- New: `docs/40 - DevDocs/prompts/2026-10-09/193-voice-clarify-fix-card.md`.
- New: this report.

## DECISIONS
1. `DB` key left out, not `none`: the rows touch `src/` and `tests/cobalt/`, and `CARD.md` allows `none` only for `ops/`, `tests/ops/`, `docs/`. Every new test is offline.
2. Row A follows the brain: a `say` that contains the template is dropped whole, so an echoed lead-in ("I can hear you…") is dropped with it.
3. Row C cause, from the code: the planner is offered only non-terminal cards (`turn.py:287`, `:290` → `tools.py:164` → `cards/store.py:231`–`:244`), and no voice tool reads a closed or expired card (`configs/cobalt/agents/voice.yaml`). "closed nn card" and "NN short from today" name a card that is probably not offered, so clarify is the plan's only legal kind; the row does not record whether NN was offered. The code cannot settle it, so C1 is a measurement row: a plan clarify records the candidate ids and history count it was given.
4. Row C2 is the desk's brain direction (L79), pasted verbatim, with plan_shape taken off NOT IN THIS JOB. Three additions, after the verbatim text: (a) the production read is the desk's before launch, a `«FILL»` in RECORDS; the builder runs no production command; (b) the brain's query says `created_at` and `"user".voice_turns`; the table has `updated_at` and `--side user` selects the schema, so RECORDS gives the working form, plus the `plan` column; (c) `build_messages` already prints each tool's `[kind]` and `Args:` (`agent.py:92`), so "the system message states the tool's kind and args" is green on BASE. The red is the sentence the fix adds for the rule the stored shape broke.
5. NOT IN THIS JOB carries the speaker-to-microphone echo (22:44:54), the `unsupported` turn (22:49:27), a closed-card read tool, the clarify template's wording and the stt model.
6. Card 156 merge: row B adds one line after `web.py:203`. Card 156 edits `:268`–`:287`, `:300` and `:306`–`:308`. Whichever deploys first, the other bases on its merge (L72).

## RECORDS
- `git -C /Users/cobalt/cobalt show e4586978:` read whole: `src/cobalt/voice/turn.py`, `tools.py`, `agent.py`, `resolve.py`, `models.py`, `registry.py`; `configs/cobalt/agents/voice.yaml`; `tests/cobalt/test_voice_turn.py`, `test_voice_web.py`; `tests/fixtures/voice/plan-replies.constructed.yaml`; `src/cobalt/cards/store.py` `:225`–`:264`. 2026-10-09 18:30–18:54 EDT.
- `git -C /Users/cobalt/cobalt grep -n … e4586978 --` proved: `turn.py:52`, `:284`, `:287`, `:290`, `:291`, `:306`, `:322`, `:328`, `:329`, `:346`, `:380`; `tools.py:114`, `:121`, `:122`, `:159`, `:164`, `:166`; `agent.py:85`, `:88`, `:92`, `:93`, `:98`, `:105`–`:107`, `:109`, `:115`, `:118`, `:134`, `:137`, `:141`, `:143`, `:149`; `resolve.py:37`, `:44`, `:45`; `store.py:179`–`:189`; `cards/store.py:231`; `web.py:198`, `:199`, `:203`, `:212`, `:214`, `:216`, `:217`, `:229`, `:247`, `:249`, `:250`, `:297`, `:298`, `:300`, `:306`; `test_voice_tools.py:120`–`:123`; `jobs.yaml:82`–`:85`; `restarts.py:220`, `:225`, `:228`, `:246`; `voice.yaml:40` (`history_turns: 4`).
- `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `b7d37cdc`; `git -C /Users/cobalt/cobalt diff --stat e4586978 HEAD -- src tests configs` → empty (18:54 EDT).
- Inputs: `reports/voice-clarify-confirm-answer-2026-10-09.md`, `reports/voice-turns-query-2026-10-09.md` (rows copied into the card), `prompts/2026-10-09/156-https-only-card.md`, `prompts/CARD.md`, the desk's message (brain direction for row C, L79, 2026-10-09).

VOICE FIX CARD DRAFTED · decisions: 6
