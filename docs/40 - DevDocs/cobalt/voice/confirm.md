# `src/cobalt/voice/confirm.py`

## What it does
Decides and carries out what happens to a pending act — by CODE, never by
the model (FINAL [F-08], L37).

- `classify(transcript, agent)` → `confirm` / `cancel` / `other`, by
  EQUALITY of the whole normalized transcript with the registry's words
  (`yes`, `no`). Normalization: NFKC, casefold, strip whitespace, strip
  leading / trailing `. , ! ?` (the engine writes "Yes."). "yes please",
  "yeah", a request with "yes" in it — all `other`.
- `confirm_pending(store, row, now, execute)`: expired → `expired`,
  nothing done. Otherwise ONE single-flight `awaiting_confirm → executing`;
  losing that race → `no_pending`. Then `tools.execute_stop` (re-read,
  re-hash, `set_card_stop`): success → `done` with the expert's write
  (`card_stop_edits`, row id) on the row; `TargetChanged` → `failed:
  target_changed` and the new read-back returned for re-confirmation;
  an expert refusal (entry guard, `market_reset`, state) → `failed:
  expert_refused`, spoken; anything else → `failed: execute_error`.
  If the final `executing → done` step finds the row already reaped (fix
  r1, [F-15]), the outcome is `failed` — never "Done." — its reply says
  the stop WAS written and names the edit id, and an error line names the
  turn; nothing is retried.
- `cancel_pending(store, row, now, reason)`: `awaiting_confirm → cancelled`
  (a `no`, a Cancel tap, or any other transcript — nothing executed).

## X-X13
A tap on Confirm and a transcript `no` in flight together: exactly one
wins; the stop changes at most once; the row is never both `done` and
`cancelled` (in memory ×50, and with-DB through two real connections).
