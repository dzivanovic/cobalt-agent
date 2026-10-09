# voice_turns, last 11 rows, read from production 2026-10-09 18:50 ET (his R686, read-only)

Command (one bare call, exit 0): `COBALT_ENV=production uv run cobalt db query --prod --side user "select updated_at, state, input_kind, transcript, reply, resolution from voice_turns order by updated_at desc limit 20"` (the brain's query said `"user".voice_turns` and `created_at`; the table has `updated_at`, and `--side user` selects the schema). Printed 11 rows (the table holds 11). Times are UTC.

| updated_at (UTC) | state | kind | transcript | reply | resolution |
|---|---|---|---|---|---|
| 22:49:40 | failed | audio | What can you do? What can I ask you? | Cobalt can't think right now (plan_shape). | |
| 22:49:27 | unsupported | audio | Can you tell me about the expired NN short card? | I can't do that yet. | refusal: unsupported |
| 22:49:13 | failed | audio | (empty) | I heard nothing. | |
| 22:48:46 | done | text | NN short from today | I can hear you. What would you like to do? I need a little more: which card, and what value? I need a little more: which card, and what value? | clarify: plan |
| 22:47:41 | done | audio | I need a little work to know which card and what value. | same doubled clarify reply | clarify: plan |
| 22:47:17 | done | text | closed nn card | same doubled clarify reply | clarify: plan |
| 22:47:17 | failed | audio | (empty) | That clip is too long (41 s; the limit is 30 s). Say it again, shorter. | |
| 22:46:39 | done | audio | We're going home, wait! | same doubled clarify reply | clarify: plan |
| 22:44:54 | done | audio | Can you hear me? Can you hear me? I can hear you. What would you like to do? I need all that. | same doubled clarify reply | clarify: plan |
| 22:44:45 | done | audio | Can you hear me? Can you hear what I'm talking about? Can you hear me? | I can hear you. What would you like to do? I need a little more: which card, and what value? (single) | clarify: plan |
| 22:41:52 | failed | audio | (empty) | I heard nothing. | |

DESK READING (facts only, for the card's row C): (1) the transcripts are clear, and two are typed text ("closed nn card", "NN short from today"), so the speech-to-text step is not the cause; every one clarifies with `clarify: plan`, so the planner fails to bind a card from clear input. (2) The reply doubles from the second turn on (the first turn at 22:44:45 is single): the planner echoes its own earlier clarify sentence into `say` from the history. (3) The 22:44:54 transcript contains the spoken reply ("I can hear you. What would you like to do?"): the speaker output reached the microphone. (4) Two other turns failed differently: `plan_shape` ("Cobalt can't think right now") and `unsupported`.
