# Voice: doubled clarify reply, dead Confirm/Cancel · brain answer · 2026-10-09
Source: his report through the desk (voice works over https on the MSI; the reply says "I need a little more: which card, and what value?" twice and the same on every turn; Confirm and Cancel do nothing). A defect he reports: surveyed, fixed, deployed, "please check" (R685). The brain read the code at HEAD.

## Cause B (buttons): the row should not be showing at all
- `voice/web.py:216` `<div id="cv-pending" class="cv-row" hidden>`, and `:203` `#cv-voice .cv-row{display:flex;…}`. An author `display` rule beats the browser's `[hidden]{display:none}`, so the Confirm/Cancel row is ALWAYS visible.
- `show()` (`:248-250`) sets `pendingTurn` only on `awaiting_confirm`. On a clarify turn it is null, and both click handlers (`cv-confirm`, `cv-cancel`) return at `if (!pendingTurn) return;`. The buttons do nothing because there is nothing to confirm. The visible row is the defect, not the handlers.

## Cause A (doubled sentence): the planner's `say` echoes the template
- `voice/turn.py:329`: a clarify plan returns `tools.compose_reply(plan.say, CLARIFY_TEMPLATE)`. `tools.py:121-124` prepends `say` whenever it is non-blank and `figures_ok` (no figures, so it passes).
- The planner is fed the session history (`turn.py:291`, `store.py:186` `SELECT transcript, reply`), so it sees its own earlier "I need a little more…" and copies it into `say`. The reply becomes the sentence twice.
- Why every turn is a clarify is NOT settled by code. Either the transcript is misheard (the stt model is `tiny.en`, card 149) or the planner cannot bind a card and the echoing history keeps it there. The stored rows settle it.

## DO
1. NOW, the desk itself (R686, read-only): `COBALT_ENV=production uv run cobalt db query --prod "select created_at, state, input_kind, transcript, reply, resolution from \"user\".voice_turns order by created_at desc limit 20"`. Put the rows in the card's `## RECORDS`. They say which of the two it is.
2. ONE card, as the small fix of the voice feature (L75: on the voice feature's own card if it has one, by a drafter):
   - Row B: `#cv-voice .cv-row[hidden]{display:none}` (or the row not given `cv-row` while hidden). Red: the rendered page's CSS shows `#cv-pending` as `hidden` and display none. A test that reads the CSS rule fails on BASE.
   - Row A: `compose_reply` drops `say` when, after whitespace and case folding, it equals the template or contains it. Red: `compose_reply("I need a little more: which card, and what value?", CLARIFY_TEMPLATE)` returns the template once. Negative control: a `say` with new words is kept.
   - Row C: from the step-1 rows. If the transcripts are garbled, the row says so, no code changes, and it goes on his list as "stt mishears: try the next model up". If the transcripts are clear and the plan still clarifies, the planner gets the fix the rows point to (for example, its own clarify reply is left out of the history it is fed), with a red built from a real stored transcript.
3. Order with card 156 (also `voice/web.py`, rows A and B: banner, `https_url`): different lines from `:203`/`:216`. Whichever is ready first deploys first, and the other bases on its merge. One feature per deploy.

FOR THE CHECK: "Brain 10-09 (voice-clarify-confirm-answer-2026-10-09.md): cv-pending row hidden by a [hidden] CSS rule; compose_reply drops a say that repeats the template; the clarify loop's cause read from production voice_turns before row C is written."

## ADDED 18:5x ET: plan_shape joins row C (card 193)
His 18:51 report: asking about the NN short card gives "Cobalt can't think right now (plan_shape)". `voice/agent.py` `validate_plan` raises it at `:134` (answer/act with no tool), `:137` (kind against the tool's kind), `:141` (args the tool does not take) or `:143` (args with no tool). The stored `failure_detail` names which. Row C reads `failure_class, failure_detail` with the transcripts (R686 query, limit 30). It fixes the cause, not the check: `validate_plan` stays as strict, and what the model is given (each tool's kind and args in the system message) or a wrong tool spec is corrected. Red: the stored failing shape is refused today, and the system message states that tool's kind and args. Confirm/Cancel still dead is row B, not yet built.
FOR THE CHECK: "Brain 10-09: plan_shape joins card 193 row C; validate_plan unchanged; the fix gives the model the tool kinds and args, or corrects the tool spec, from production failure_detail."
