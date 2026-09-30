# E1 inline — answers to the build's decisions (2026-09-30)

## §0 Headline
All 3 items answered with the safe option. None of them is for Dejan: none is about scope, a date or money.
1: the with-DB passes wait for the check or STEP-G, when the lock is free. 2: A1 needs no fix. 3: in the unclear cases the comment goes with the old value, as built.

## ANSWERS
DECISION 1 — Do not run the with-DB passes in this build: the check, or the deploy's STEP-G, runs `test_prefill_trade_note.py` and `test_s3_c4_trade_note_db.py` once the lock is free — the card says this job is offline, with "no database, no migration, no lock (L76)" and running beside F15 P1, which held the lock at 17:31 (card `62-e1-inline-card.md:32`; build report DECISIONS item 1). Not for Dejan: this is about test order, not scope, a date or money.
DECISION 2 — A1 is closed as a record and needs no fix: `_render_value` always returns one line for today's values, and a ` #` inside quotes is kept as part of the value — the function is one f-string per branch (`trade_note.py:113-118`, branch `s3/e1-inline-0930`); `inline_comment` scans quoted values up to their closing quote before it looks for a ` #` (`:347-361`); and the `"5.2000 # not a comment"` assertion passed. Not for Dejan.
DECISION 3 — Keep the behaviour as built: for (a) a rendered value of several lines, (b) a quoted value that does not close on its line and (c) a flow `[`/`{` value, the comment is not guessed and goes with the old value — the card says "do NOT guess: keep the current behaviour" (card `62-e1-inline-card.md:18`), and the code does this at `trade_note.py:345-346` (flow), `:358-359` (unclosed quote) and `:378` (several lines). The docstring at `:304-307` states this rule. Case (a) cannot happen with today's values (see item 2). Not for Dejan.

E1 DECISIONS ANSWERED · answered: 3 of 3 · for Dejan: 0
