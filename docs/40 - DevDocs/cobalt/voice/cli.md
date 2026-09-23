# `src/cobalt/voice/cli.py`

## What it does
`cobalt voice turn` — the turn function's third caller (FINAL [F-01], §8):

    cobalt voice turn --text "<text>"  [--dry-run] [--session S]
    cobalt voice turn --audio <file>   [--dry-run] [--session S]
    cobalt voice turn --confirm <turn_id> [--session S]

It prints the turn id, state, what was heard, the reply, any RED / AMBER
lines and, for `--dry-run`, the Plan, the resolution and the exact change
(nothing written). Exit 1 when the turn failed, 2 on a refusal.

## Rules
- `--confirm` is REFUSED under `COBALT_ENV=production`: a production act
  is confirmed only by the widget — his tap or his own next turn. No
  house confirms a production act (L37, FINAL [F-02]).
- `--audio` accepts webm / ogg / m4a / wav, and takes the scratch-dir lock
  for its turn; while a server holds it the command refuses by name.
- Any house runs this in DEV with synthetic audio or text (L44, [F-02]).
