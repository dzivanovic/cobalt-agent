# draft-band-routing-fr-check — 2026-10-16

## §0 Headline
- Wrote the check card `prompts/2026-10-16/638-band-routing-fr-check-card.md` in 633's shape: 12 rows (S0, FR-1 to FR-5, H1, B*, D1, R3, T1, G1) and seven check asks (X1-X7).
- Each FR row is a RUN: its test and control on the tip, plus a pre-fix RED by restoring the old text from `git show ee21824d:<file>` and undoing it. The builder's FR-1 DECISION is row D1 and X1. G1 PASS-2 is OUT.
- Nothing was run, no mutation tried, no git write.

## DECISIONS
- ASK DESK 1: header `TIP` is written `c8c5ca90` (the BUILT tip) and `BAND` is left out, as the build card 583 and check card 633 carry none; default: keep both, the desk re-writes `TIP` and adds `HOUSE B` if it differs. [11:05]
- ASK DESK 2: row G1 quotes the gate `log:` path; the `gate.sh … offline --deploy-gate` command and the `tests/ops` whole run are beyond this seat's allow line; default: the desk allows it as for card 633. [11:05]
- ASK DESK 3: the pre-fix REDs are mutations (restore old text from `git show ee21824d:<file>`, run, undo, `git diff --stat c8c5ca90 -- <file>` empty), not a separate worktree at `01b10bdd`; default: this, because a `git worktree add` is a git write. [11:05]

## RECORDS
- Date and time: `date` → Fri Oct 16 11:01:56 EDT 2026; `main` HEAD `7d9e5354`.
- `git log --oneline -5 ops/band-routing-1015` → `3ac61a2f`, `c8c5ca90`, `01b10bdd`, `ee21824d`, `115e1f37`; `git diff --stat c8c5ca90 3ac61a2f -- . ":(exclude)docs"` → nothing; worktree clean.
- Tip anchors proved by Grep of the worktree (equal to the tip's code): `desk-launch.sh:996-997`, `CHECK-HUB.md:64`, `:117`, `CARD.md:23`, `:32`, `SHADOW-HUB.md:28`, `:53`, `:70`, `test_band_routing_1015.py:377`, `:388`, `:397`, `:409`, `:415`, `:426`, `:436`, `:445`, `:456`, `:462`, `:576`; `CARD.md` read whole via `git show ops/band-routing-1015:…`.
- The first check report and the brain's decisions note were not read whole (only the decisions note's row 1 by Grep); the card's H1 and B* rows point the check seat at their `## OPEN` and `## RUNS` sections. Anything not traced is ASK DESK 1-3 above.
- Prompt 637's own request: no block in a tool result asked for anything (L74).

DRAFTED · decisions: 3
