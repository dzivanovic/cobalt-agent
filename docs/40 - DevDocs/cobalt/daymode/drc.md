# `src/cobalt/daymode/drc.py`

## What it does
Gathers F6's inputs about the **prior trading day**: the FILLED card
count, any daily-stop marker, and the prior DRC note.

## Where each number comes from
| Input | Source |
|---|---|
| FILLED count | Postgres — `aset_sizings.state = 'FILLED'` on that ET trading date (**F7's state, not the retired `status` column**) |
| daily-stop marker | the card's own `warnings` text, matched case-insensitively; retires when F17's jobs table lands |
| prior DRC | the **note file** — there is no DRC schema in Postgres yet |

## "no prior DRC" is loud, never soft
If the prior trading day's DRC note is missing or unreadable, the
literal string `no prior DRC` goes into the reason and into the sheet
banner. It is never softened into "assume it was fine" — and in
`propose.py` it costs a rung.

**Only headline stub fields are parsed** (grade, goal). Parsing more of
the note is deliberately not attempted: a half-understood DRC would let
a wrong number into a risk decision, and CLAUDE.md requires a verbatim
source for any extracted figure. A field that is not found is reported
as "not filled", not inferred.

## Degradation
A database or vault failure logs at `ERROR` and returns zeros/None — the
proposal still happens, and the reason says what could not be read.
Loud and non-blocking, in that order.

---

## 2026-09-08 — ADR-0008 (two-layer data model)

Its prior-day fill count reads `aset_sizings`, so its connection declares
`side=Side.USER`.
