# `src/cobalt/daymode/match.py`

## What it does
The F6 match check: refuses card creation while the attested `.htk`
disagrees with the day mode in force, and refuses a key outside the
rung's grade ladder.

## What slice 2 actually shipped — and why this is an attestation
The ".htk-match check" appears in the ledger's slice-2 scope line
("day-mode line + .htk-match check"). **What landed is one static
string**, `src/cobalt/prefill/daily.py`'s `SHEET_MODE_LINE`:

```
Sheet mode: [ ] FULL [ ] HALF — .htk loaded: [ ] full [ ] half
```

Two pairs of markdown checkboxes in the daily note. It reads nothing,
compares nothing, persists nothing and refuses nothing; the trader ticks
a box and no code ever looks at it. There is **no other `.htk`
reference anywhere in `src/`** — so there was no DAS-state read to keep.

Nor could there be. The trading PC has **not** joined the tailnet
(S1-P1's line 0: `cobalt`, `dejans-s25`, `fedora` — no Windows peer),
and CLAUDE.md's first absolute boundary forbids touching DAS Trader Pro
at all. So Cobalt cannot know which hotkey file is loaded, and the
honest design is not to pretend: **he states it, and Cobalt holds him
to it.**

`day_modes.attested_sheet` is his word and `attested_at` is when he gave
it. The attestation is a weaker guarantee than a read, is labelled as
one everywhere it surfaces ("attested, not read"), and is strictly
stronger than a checkbox nobody reads.

## The refusals
```
sheet FULL loaded, day mode REDUCED — reload reduced_day.htk or overrule
```
- **Nothing attested is also a refusal.** "No attestation" is not the
  same as "it matches": an unstated hotkey file is exactly the state in
  which a full-size key gets pressed on a reduced-size day.
- `half.htk` and `reduced_day.htk` are **different attestations**:
  `reduced_day.htk` is the reduced rung (half-sized keys *and* the
  B-only restriction); `half.htk` is the plain half rung. Attesting the
  wrong one of the two is still a mismatch.
- `assert_grade_allowed` refuses a key outside the rung — an A key on
  the reduced rung is not a smaller A, it is a key he has decided not to
  press today. Refused with the reason on screen, never silently resized.

Both refusals run in `POST /size` **before any write**, and both are
logged: a refusal nobody can count is a rule nobody can review at the DRC.
