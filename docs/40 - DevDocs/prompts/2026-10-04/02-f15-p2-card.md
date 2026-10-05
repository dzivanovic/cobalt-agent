JOB: f15-p2
LADDER: S3-P3 · F15
BRANCH: f15/p2-replay-1004
WORKTREE: f15-p2-1004
BASE: 3c1f75b8
TIP: 437c7299
REPORT: /Users/cobalt/cobalt-wt/f15-p2-1004/docs/40 - DevDocs/reports/f15-p2-build-2026-10-04.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/f15-p2-check-2026-10-05.md
HOUSE B: as needed
TREE STATE: row T
RULINGS: 2026-10-03 R219

## ROWS

WHY: F15 P2 of `docs/30 - Design/F15-PREDICTION-RECORDS-FINAL-2026-09-29.md` (`## CHUNKS` row P2, `:484`). P1 is live (migration `0022`, `cards/predictions.py` `PredictionRecord` and `write_record` on `main`); its X12 ran green (`reports/f15-p1-build-2026-09-30.md` DECISION X12), so the `transition_id` rule stands; X6, the fifth experiment that gates P2 (FINAL `:434`), ran green on P1's records — (a) and (c) in the build's H2 tests, (b) in its check (`reports/f15-p1-check-2026-09-30.md` O1) — and P2-1's ROW and decision-grade tests are its replay half. S3 C1–C4 are on `main` (`cards/legs.py:677` `realized_r`, `legs_current_v`), so the design's "P2 builds on a tree carrying `s3/exits-c4`" holds on `main`. Pure reads: no write, no migration. With-DB job: takes the lock.

| row | what | red first | files |
|---|---|---|---|
| X | P2's first-gate experiments (FINAL `## First-gate experiments`): X7 (`:435`, the NUMERIC(8,6) `conviction` read back after `scoring.conviction()`), X10 (`:438`, a record's `output` after the JSONB round trip vs `published_numbers(...)`), X11 (`:439`, a real-shape card that EXPIRES untriggered, then the nightly replay on `cobalt_dev`: is a `missed` row written?) | RUN — asserts nothing; each result quoted under `## DECISIONS` as `DECISION X<n>`. X7 different reprs → the replay compare is on `Decimal` (already the design's); X10 a difference → MATCH uses a canonical compare; X11 no row → design-changing (FINAL `:439`: "the status label goes to round 2"): `DECISION X11` names it, and P2-3 is still built with `awaiting nightly replay` as written | `tests/experiments/f15_p2/` |
| P2-1 | `cobalt cards replay <card_id> [--json]`: per record by `seq`, MATCH / DIFF / NOT REPLAYABLE per FINAL §5 (`[F-08]` as amended by `[F-33]`, `[F-35]`; `replay_receipt` against the RECORDED scorer, `ReplayError` caught, the `formula_sha256` NOTE); the decision grade per R2-1 (c) B (the last record by `seq` whose `transition_id` < the id of the card's first `card_transitions` row with `from_state = 'WATCH'`; none while WATCH; derived, never stored); the ROW line against the last record by `seq`; exit 0 / 1 / 2 as §5; a manual card and a pre-F15 card (the audit-export line, `--run` = `system.radar_score.run_id` of its `radar_score_id`) exit 2 | the CHUNKS pass list, one test each: MATCH on create → tap → refresh → fill → exit → CLOSED; a tampered `output` → DIFF, exit 1; another version → NOT REPLAYABLE, exit 2; pre-F15 → exit 2 with the line; no receipt → NOT REPLAYABLE; manual → exit 2; arm-then-disarm picks the record before the ARM; ROW against the last record by `seq` (a card row whose numbers no record stores → `ROW: holds numbers no record stores`, exit 1); no decision grade while WATCH | `src/cobalt/cards/predictions.py`, `src/cobalt/cards/cli.py`, tests |
| P2-2 | `--json`: the ONE object of `[F-44]` (R2-5 (5)), numbers as `published_numbers` strings, compare on `Decimal` | red: the object's keys and a DIFF record's `diff` list | `src/cobalt/cards/predictions.py`, `src/cobalt/cards/cli.py`, tests |
| P2-3 | `predictions.corpus(since) -> list[CorpusRow]` and `cobalt cards corpus [--since YYYY-MM-DD] [--json]` per FINAL §6 `[F-09]` and the ONE read (`:337`–`:342`): one row per card — decision record, final record, record count; state; `realized_r` called, never restated (L3), with its provisional flag; the current `missed` row (`is_current`, `kind = 'card'`: `cf_r`, `mfe_r`, `excluded_by`); the `picks` row; `outcome_status` ∈ open / provisional / final / awaiting nightly replay; n per status printed first; no EV, no aggregate; `replay`'s OUTCOME line calls `corpus` for its one card | red: a CLOSED card with an estimated leg → provisional; an EXPIRED card with no missed row → `awaiting nightly replay`, never `missed: none`; the n-per-status line printed before the first row | `src/cobalt/cards/predictions.py`, `src/cobalt/cards/cli.py`, tests |
| T | the tree state: every with-DB test of this build that needs `0021` / `0022` gets its `--deselect` appended at the END of the PASS 1 list and its id appended at the END of the PASS 2 list in `ops/desk/gate-lists.md` (the ONE home, BUILD-HUB `## W`; the hub files hold no id list), AFTER D5's ids as they read at BASE, EXACTLY as (c) and (c3) executed (precedent: P1's `tests/cobalt/test_f15_p1_records_db.py` in pass 2) | `git diff <BASE> -- ops/desk/gate-lists.md` shows only this build's `--deselect` ids at the end of PASS 1 and the same ids at the end of PASS 2, after D5's; `git diff <BASE> -- "docs/40 - DevDocs/prompts"` shows nothing | `ops/desk/gate-lists.md` (PASS 1 and PASS 2 lists, as BUILD-HUB `## W` says; the hub files hold no id list) |
| DOC | a paragraph dated the day the build runs, `<date> — F15 P2`, in the DevDocs pages of `cards/predictions.py` and `cards/cli.py` | — | `docs/40 - DevDocs/cobalt/cards/` |

## NOT IN THIS JOB
- Any write: no record, receipt, `missed` or `legs` row; no migration; no change to `write_record`, `create_radar_card`, `refresh_radar_card`, `tap_dot`, `write_receipt`, `EVALUATOR_VERSION`.
- Re-grading with today's formula (FINAL §5: a what-if, Open point 2); a card chip or a DRC cell (§7); backfill; S8.
- A second realized-R or estimated-leg rule (L3); a re-decision of R2-1 (c) (his, R145).

## READ
- FINAL §3 (the record), §5 (replay, the RULED block, `[F-25]`, `[F-44]`), §6 (`[F-09]`, the ONE read), `## First-gate experiments` X7, X10, X11, `## SEAM`, `## CHUNKS` row P2.
- `reports/f15-p1-build-2026-09-30.md` `## E2 RED` (X12 lines), `## DECISIONS` 6, `## RECORDS`; `reports/f15-p1-check-2026-09-30.md` §0.
- Code at BASE: `src/cobalt/cards/predictions.py`; `src/cobalt/cards/cli.py` (the `cards` family); `src/cobalt/radar/evaluate.py` (`ReplayError`, `published_numbers`, `replay_receipt`); `src/cobalt/cards/store.py` (`receipt_for_run`); `src/cobalt/cards/legs.py` (`realized_r`); `tests/cobalt/test_radar_cards_db.py` (the real-shape `world` fixture).

## CHECK ASKS
- X1 Does any path of `replay` or `corpus` write, or read current settings or market data?
- X2 Is the decision grade derived only from `transition_id` and `card_transitions` (never from `at` or `card_state`)?
- X3 Is `realized_r` called and its provisional flag used as returned, with no arithmetic restated?

## RECORDS
- STACKED (desk R233): BASE is `03` D5's BUILT tip (a stacked card starts at its base's BUILT line). The chain is `01` K3 → `03` D5 → `02` this card, ONE deploy, TIP order 01, 03, 02. This card shares no source file with `01` or `03`; row T writes its ids into the pass-1 / pass-2 lines AS THEY READ AT BASE (D5's ids already in), so the hub-line edits never meet in a merge. BASE carries K3's and D5's diffs: the check reads `<BASE>..<TIP>` only.
- HOUSE B at the check: `as needed` (reads only; no vault note, no sizing).
- RESTARTS: derived (`cards/*.py`; quote `cobalt jobs restarts`).
