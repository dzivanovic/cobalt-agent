# S3 cards re-read against their designs — drafter `s3-reread-draft`, 2026-10-04

## §0 Headline
- I read all three S3 cards against their designs and against `main` at `0b89e1d2`. Every row traces to its design. I fixed 10 rows by Edit; no header value or `«FILL»` was touched.
- D5 has two design gaps the code cannot meet as written. A no-legs card cannot get a DAS entry leg (`insert_entry_leg` carries no import id, and `0021` refuses that). A Cobalt leg with no DAS execution has no removal writer. These are ASK DESK D5-a and D5-c, and their defaults sit in the card's `## RECORDS`.
- D5 also needed fences the design implies: no writes on a `--dry-run`, and none on a re-paired date or a carried trade (D5-b, D5-d).
- P2 now says X6 ran in P1, and its X11 "no row" result is design-changing per FINAL `:439`. K3 changed only in citations and dates.

## CARDS

### 01 — DRC K3 (`DRC-OVERNIGHT-POSITION-v3-2026-09-24.md`; source `prompts/2026-09-29/30-drc-k3-build.md`)
| row | design cite | verdict | fix made |
|---|---|---|---|
| X | v3 `:327` X11, `:334` X13, `:335` X14, `:336` X15; `30` `:86`–`:91` | holds; K2's X11 tests at `test_drc_k2_experiments.py:566`, `:593` and the X7 tests at `:203`, `:231` exist | — |
| K3-1 | v3 §2a `:73`–`:80`, §5 `:236`, `[F-11]` `:82`; `30` `:22` | holds; `units.OPEN_POSITIONS` is absent on `main` (red holds); `plan_note` `build.py:324`, `reconcile` add `:554` | — |
| K3-2 | v3 §5 `:237`, X14 `:335`; `30` `:23` | holds; `units.summary` `:125` | — |
| K3-3 | v3 §5 `:238`, `[F-11]` `:82`, v2 A31 `:295`; `30` `:24` | holds; `_after_section` `units.py:82`, `DAY_PLACEMENT` `:91` | — |
| K3-4 | v3 `[F-03]` `:167`, §4 `:224`–`:225`; `30` `:25` | holds; `_CURRENT` `store.py:108`; `superseded_stated_ids` absent; `build_date` `build.py:689` | — |
| K3-5 | v3 §5 `:239`–`:240`; `30` `:26` | holds; `_morning` `imports.py:739`, line `:753`; `day_view` `:789`; `drc_page.render` `:87`, STARTING BOOK `:112` | — |
| K3-6 | v3 §2c row A `:112`, §5 `:241`, `[F-14]` `:120`, `[F-16]` `:116`; `30` `:27` | holds; `_rebuilds` `cli.py:142`, `cmd_state_book` `:164`, `VIA` `:47`; `record_stated_book` `store.py:1340`, `preview_stated_book` `:1318` | — |
| K3-7 | v3 §2b `:101`–`:103`, `[F-06]` `:190`, §4 `:221`–`:222`; `30` `:28` | holds; `seed_for` `store.py:1038`, `effect_day` `:385`, `rebuild` `:329` | — |
| K3-8 | v3 `[F-03]` `:167`; `30` `:29` | holds; `run_drc_build` `build.py:697`, loop `:704` | — |
| K3-9 | v3 §6 K3 `:249` (D2's `/drc` route); `30` `:30` | the `/drc` block moved: `30` read `:1517`–`:1610` at `985cca3b`, but on `main` it opens at `web.py:2067`, with `drc_no_trade` at `:2138` and `drc_scan` at `:2152` | the current lines added to the row |
| DOC | `30` `:32` | the hard date `2026-10-04` could be wrong if the build runs Monday | dated by the day the build runs |
| RECORDS RESTARTS | v2 §9 D2 `:176` | K3-5/6/7 edit `aset/drc_page.py`, but the record named only `aset/web.py` | `aset/drc_page.py` added |
| TREE STATE `unchanged` | `CARD.md` (K10) | holds by the desk's standing reading: a new with-DB test at `0013` under `migrated` runs in pass 1 as written (`prompts/2026-10-03/00-brain-handover.md:16`) | — |

### 03 — DRC D5 (`DRC-AUTOMATION-v2-2026-09-22.md`)
| row | design cite | verdict | fix made |
|---|---|---|---|
| WHY | v2 `:179`, `:93`, `:96`; R90 `cto-2026-09-22.md:75` | `units.py:189` is `def reconcile`; the text sits at `:193`. `build.py:627` holds | cite → `:193`, in `reconcile(day_row)` `:189` |
| X | v2 X11 `:203`, R90 | holds | — |
| D5-1 | v2 `:80` (1)–(3), §6 `:140` | the build row is per trade (`build_trade`, ref = trade id), not per card. `units.reconcile` takes only the day row. §6 `:140` needs his taps and held counts listed as history, and the card left that out | the key is placed on the matched trade's `build_trade.derived`; the signature fact and the `:140` history listing added |
| D5-2 | v2 `:80` (4)–(6), `:96`, `[F-09]` `:79` | `insert_entry_leg` cannot carry `source_import_id` (`legs.py:274`; CHECK `0021_legs.sql:63`). `record_exit` stamps `at = now` (`:431`). No writer removes a leg (`:519`–`:520`). Dry-run calls `plan_note` only (`drc/cli.py:288`–`:292`). Re-paired dates rebuild through `build_date` (`build.py:704`) | the entry-leg clause moved to ASK DESK D5-a; D5-b/c/d pointers added; the event-day-only and never-in-`plan_note` fence added, with a dry-run negative control |
| D5-3 | R90; v2 `:235`–`:247`, A31 `:295`; `LegRefused.code` `legs.py:68`–`:75` | holds | — |
| D5-4 | v2 `[F-19]` `:117`, `:110`; `realized_r` `legs.py:677` | missed the case of a trade with no matched card | "no matched card" added to the `not computed` cases |
| T | `CARD.md` TREE STATE; BUILD-HUB W (c)/(c3); precedent `test_legs_c2_db.py` in both lines | holds | — |
| DOC | — | the hard date `2026-10-05` conflicted with its own record ("the date the build runs") | dated by the day the build runs |
| READ | v2 `## OPEN — ROUND 2` | the section starts at `:235`, not `:233` | `:235`–`:247` |

### 02 — F15 P2 (`F15-PREDICTION-RECORDS-FINAL-2026-09-29.md`)
| row | design cite | verdict | fix made |
|---|---|---|---|
| WHY | CHUNKS P2 `:484` (gated by X6, X7, X10, X11, X12) | the card named X12 (run in P1) but not X6. X6 (a)/(c) ran in P1's build (H2 tests) and (b) in its check (`f15-p1-check-2026-09-30.md:220`) | X6's P1 runs stated; P2-1's ROW and decision-grade tests named as its replay half |
| X | `:435` X7, `:438` X10, `:439` X11 | X11's default contradicted the design: "no row ever → … the status label goes to round 2" | a no-row result is design-changing → `DECISION X11`; P2-3 is still built as written |
| P2-1 | §5 `:266`–`:291`, RULED `:304`–`:309`, `[F-35]`; CHUNKS `:484` | the CHUNKS list includes "the ROW line against the last record by `seq`", but the red list had no ROW test and no WATCH case | added a ROW test (including `ROW: holds numbers no record stores` → exit 1) and a no-decision-grade-while-WATCH test |
| P2-2 | `[F-44]` `:325` | holds; `published_numbers` `evaluate.py:1604`, `ReplayError` `:1523`, `replay_receipt` `:1618` | — |
| P2-3 | §6 `[F-09]` `:329`–`:346`, ONE read `:337`–`:342`; CHUNKS "corpus n per status" | `CorpusRow` was missing the decision record, the final record, the record count and the `picks` row. The red list had no n-per-status test | the fields added; an n-per-status-first red added. `missed` columns exist (`0009_picks_missed.sql:68`–`:97`) |
| T | `CARD.md`; pass-2 already carries `test_f15_p1_records_db.py` | holds | — |
| DOC | — | the hard date | dated by the day the build runs |
| symbols | `predictions.py` (`PredictionRecord` `:143`, `write_record` `:177`), `store.py` (`receipt_for_run` `:1316`, `receipts_chain` `:1324`), `cards/cli.py` `add_parser` `:239`, `test_radar_cards_db.py` `world` `:45` | all present on `main` | — |

## DECISIONS
- ASK DESK: D5-a. v2 `:80` gives a no-legs card its entry leg from DAS "through the same writer". `insert_entry_leg` writes `source_import_id = NULL`, and `0021_legs.sql:63` refuses `source = 'trading_log'` without one; changing `cards/legs.py` is fenced. How should a pre-C1 card be reconciled? [15:37 EDT] Default taken, in the card's `## RECORDS`: no entry leg is written. Exits and corrections run on the `running_shares` pre-C1 basis, and the unit says the entry leg was not written.
- ASK DESK: D5-b. `record_exit` stamps the leg's `at` with `now`, and `now` also drives the `market_reset` gate. Passing the export's time as `now` would sidestep the gate. [15:37 EDT] Default taken: `now` is the build's clock, and one `record_correction(at=<export time>)` through the same writer follows.
- ASK DESK: D5-c. A Cobalt leg with no DAS execution has no writer that removes it (`record_correction` refuses `shares <= 0`). [15:37 EDT] Default taken: no write is tried. It is stored and rendered as a D5-3 unresolved item.
- ASK DESK: D5-d. A carried trade's day-file holds only that day's executions, while the card's legs span days. `run_drc_build` also rebuilds every re-paired date, and K3-8 adds a second caller. Which builds write `legs`? [15:37 EDT] Default taken: only the event day's `check=True` build, only for a trade with no `inputs.carried_from`. Otherwise the diff is stored and rendered `adjustment not written — <carried trade | re-paired date>`.

## RECORDS
- Inputs read: the three cards; `prompts/CARD.md`; `prompts/BUILD-HUB.md`; `areas/cobalt.md` from `## Build rules`; `topics/writing-rules.md`; v3 whole; v2 `:70`–`:303`; F15 FINAL `:266`–`:487`; `prompts/2026-09-29/30-drc-k3-build.md` `:10`–`:39`, `:84`–`:93`; `cto-2026-09-22.md` R67, R90; `f15-p1-build-2026-09-30.md` and `f15-p1-check-2026-09-30.md` (X6, X12 lines).
- Code read on `main` `0b89e1d2`: `drc/build.py` `:324`–`:713`; `drc/units.py` `:45`–`:199`; `drc/cli.py` `:265`–`:301`; `cards/legs.py` `:1`–`:50`, `:246`–`:744`; `0021_legs.sql` source/CHECK lines; and symbol greps of `drc/store.py`, `drc/imports.py`, `aset/web.py`, `aset/drc_page.py`, `cards/predictions.py`, `cards/store.py`, `cards/cli.py`, `radar/evaluate.py`, `0009_picks_missed.sql` and the test fixtures.
- `4693097d` (in K3's `BASE` fill) is not a commit in this repo (`git log` exit 128); it reads as the deploy session's id. It is left as written.
- `drc-d3-fix-r2-build-2026-09-29.md` exists only at `985cca3b` (`git show --stat`: 1 file); K3's READ says so.
- The card edits are uncommitted on `main` (`git diff --stat`: 3 files, +19 −14); this seat makes no git write (L36).
- PRE-STOP SELF-CHECK (K25): (1) every fix has its design or code line cited in `## CARDS`; (2) every symbol the cards name was grepped on `main` (above); (3) each card's headers and `## ` headings were re-read after the edits (`grep -n` of the 11 keys and the headings: unchanged; `«FILL»` lines intact).

S3 CARDS RE-READ · fixed: 10 rows · decisions: 4
