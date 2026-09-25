# `src/cobalt/voice/models.py`

## What it does
The typed data of a voice turn.

- `Plan` (FINAL §2.4): `kind` ∈ answer / act / clarify / unsupported /
  refuse, `tool`, `args` (each a `Span` — a verbatim substring of the
  transcript — or a `CandidateRef` — an id from a closed list), `say`.
  `extra="forbid"` everywhere: an extra field is a parse failure.
- `PromptInputs`: the WHOLE whitelist the prompt builder may read
  (transcript, this session's history, the clock, the card candidates).
- `CardCandidate`: one open card as the model sees it — an id and a
  code-rendered label.
- `PendingAction`: an act waiting for his confirmation — card, from → to,
  card state, the read-back, `diff_sha256`, `target_sha256`, expiry
  (FINAL §2.6, [F-09]).
- `TurnState` + `EDGES`: the FINAL §7 state machine
  (received → transcribing → planned → answered | awaiting_confirm →
  executing → done | failed | cancelled | expired | unsupported).
- `TurnOutcome` / `DegradedLine`: what the widget and the CLI show.
