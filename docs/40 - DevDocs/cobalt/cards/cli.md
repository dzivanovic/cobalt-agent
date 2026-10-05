# `src/cobalt/cards/cli.py`

## What it does
`cobalt cards` — the state machine's command surface, mounted by
`cobalt.cli`.

| Command | Purpose |
|---|---|
| `state <id>` | the card's current state |
| `history <id>` | every transition, oldest first, with evidence |
| `legs <id>` | READ ONLY (S3 C2-7): the current legs, `running: <n> (basis: <legs\|recomputed_shares\|shares>)`, `realized R: <value\|reason> <provisional\|final> [realized_r.1]`, `stop owner: <yours\|cobalt>`; a card with no position exits with the refusal text |
| `move <id> --to STATE [--actor] [--reason]` | one transition through the gates |
| `backfill [--dry-run]` | give every state-less card a state + genesis row |
| `expire [--at ISO] [--dry-run]` | what `com.cobalt.cards-expire` runs at 16:05 ET |
| `edges` | print the edge table (the source of the DevDoc page) |
| `trail-fit-draft [--out]` | write the R5 `trail_fit → source: human` review DRAFT; no note touched, no apply exists (`trail_fit_draft.py`) |
| `shadow-report [--since YYYY-MM-DD]` | per-factor shadow agreement vs `card.shadow_promotion_bar`; read-only (`shadow_report.py`) |

## Notes
- `--at` exists for the same reason `session now --at` does: the tests
  freeze the clock rather than sleeping until 16:05. It refuses a naive
  datetime — sessions are ET, storage is UTC (ADR-0007).
- `backfill` applies migration 0007's `NOT NULL` only **after** the
  backfill commits — the same two-step the F1 `session` backfill uses.
- `edges` is what `docs/40 - DevDocs/cobalt/cards/models.md` renders, so
  the wiki cannot disagree with what the store enforces.
- The two S2-P2 commands (`trail-fit-draft`, `shadow-report`) import their
  modules lazily, so `cobalt cards state` does not load the taxonomy or the
  settings reader. `picks` is the exception: `cli.py` imports it at the top,
  which costs only `cobalt.radar.models` and the session clock.

---

## 2026-09-17 — S2-P4: `cobalt cards picks` and the fill result

`cobalt cards picks [--date YYYY-MM-DD] [--cutoff ISO8601]` prints pick vs
pool rank/value and card-score rank for every FILLED transition on the ET
day (default: today ET). It exits 1 when any counted transition has no pick
row (MISSING). `--cutoff` must carry a timezone offset. Gaps before it
print `MISSING (before cutoff)` and do not count: this is smoke check K6's
comparison window, so historical gaps stay visible without failing it. An
empty day prints `no FILLED transitions on <date>` and exits 0. Rendering
lives in `picks.render_picks_report`.

`cobalt cards move <id> FILLED` now reads `FillResult.transition_ids`. If
the fill committed but the pick did not, it prints `PICK NOT RECORDED …` to
stderr and exits 1, so a script cannot mistake the gap for a clean fill.

## 2026-09-29 — S3 exits C4: `cobalt cards trade-note <card_id>` (C4-4)

The retry for a trade note that was not written at the fill (L1: a banner,
`trade_note_path` NULL, and this command). It applies to a FILLED or CLOSED
card and runs `prefill.trade_note.write_card_note(card_id, retry=True)`:
- the session gate;
- the SAME `upsert_trade_note` as the fill (create, or update an existing
  note — `create_if_absent` alone is not the retry);
- one `upsert_unit` per current leg seq;
- sets `trade_note_path`.

It prints `card <id>: trade note <action>: <path>`, one `  leg-<seq>: <action>`
line per unit, then `trade_note_path: <relative path>`. `market_reset` →
`REFUSED card <id>: <the gate's message> Nothing written.` (exit non-zero;
nothing touched). Any other failure → `FAILED card <id>: trade note NOT
written: <reason> — trade_note_path NULL` (exit non-zero). That includes a
card not FILLED / CLOSED and a path another card holds.

## 2026-10-04 — F15 P2: `cobalt cards replay <id> [--json]`, `cobalt cards corpus [--since YYYY-MM-DD] [--json]`

Two read-only commands (FINAL §5, §6), no schema call, nothing written:
- `replay` prints the header (`card <id> <ticker> <direction> · <origin> ·
  <state> · scorer card_grade <versions> · <n> records`), one line per record
  (`#k kind HH:MM:SS ET  MATCH | DIFF <field> recorded … → replayed … |
  NOT REPLAYABLE — <reason>`, the decision grade marked `← decision grade
  (last record before <state>)`, or `decision grade: none — the card is
  still WATCH`), the formula NOTE when the source changed, `ROW: matches
  record #k` or `ROW: holds numbers no record stores (…)`, `OUTCOME: …` (the
  corpus row) and the count line. Exit 0 / 1 / 2 as §5; a card that does not
  exist prints `REFUSED card <id>: no card <id>` and exits 2. `--json` prints
  `ReplayReport.as_json()` (the `[F-44]` object) with the same exit.
- `corpus` prints `corpus: n=<N> · open … · provisional … · final … ·
  awaiting nightly replay …` first, then one line per card; `--json` prints
  `{"counts": …, "rows": […]}`.
