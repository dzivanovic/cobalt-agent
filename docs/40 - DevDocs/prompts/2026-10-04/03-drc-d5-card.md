JOB: drc-d5
LADDER: S3-P3 · F14
BRANCH: drc/d5-reconcile-1004
WORKTREE: drc-d5-1004
BASE: 3e40359a
TIP:
REPORT: /Users/cobalt/cobalt-wt/drc-d5-1004/docs/40 - DevDocs/reports/drc-d5-build-2026-10-04.md
CHECK REPORT:
HOUSE B:
TREE STATE: row T
RULINGS: 2026-10-03 R219

## ROWS

WHY: D5 of `docs/30 - Design/DRC-AUTOMATION-v2-2026-09-22.md` (§9 row D5, `:179`): the reconcile step WRITES to `legs`. Today the reconcile unit renders `legs: not built` / `adjustment pending (legs writer not built)` (`src/cobalt/drc/units.py:193`, in `reconcile(day_row)` `:189`) and the trade block prints `realized not computed (D5)` (`src/cobalt/drc/build.py:627`). C2's writer is on `main` and already carries S-C1 / S-C2 (`src/cobalt/cards/legs.py` docstring: `source = 'trading_log'` with a required `source_import_id`, appended, CLOSED check only at 0, `LegRefused` by stable `code`), so D5 adds no migration. R90 settled v2's open R2-1: a refusal on a CLOSED card the export shows open builds the DRC, keeps the position OPEN in the DRC book as the export shows it, carries `unresolved: card <id>` until he resolves it, and gives him a RESOLVE on `/drc`.

| row | what | red first | files |
|---|---|---|---|
| X | v2 X11 (`:203`) under R90: on `cobalt_dev`, a CLOSED card whose export exits total LESS than Cobalt's → C2's writer refuses; the build stores the unresolved item, renders it, and the DRC is built | RUN — asserts nothing; quoted; a red (the build fails, or the refusal is forced) → `DECISION X11`, D5-3 not built | `tests/cobalt/test_drc_d5_experiments_db.py` |
| D5-1 | THE DIFF (v2 `:80` steps 1–3): per matched card (`build.py` `matched`, the §4 match) against that card's current legs (`legs_current_v`): per leg seq shares, price, time; DAS exits with no Cobalt leg; Cobalt legs with no DAS execution; held after each leg. Stored ONCE as a key of the matched trade's `build_trade.derived` (and its inputs: the `drc_imports` row id, the leg ids read) (L57); rendered by `units.reconcile` from the stored keys only (it takes the day row alone today, `units.py:189`); his taps and held-count statements listed as history (v2 `:140`) | red: the unit still prints `legs: not built` for a card with legs and a differing export | `src/cobalt/drc/reconcile.py` (new), `src/cobalt/drc/build.py`, `src/cobalt/drc/units.py`, tests |
| D5-2 | THE WRITES (v2 `:80` steps 4–6, S-C2): through `cards.legs` ONLY (L3, L40): a correction per mismatched leg (`record_correction`), a new exit leg per DAS exit Cobalt never recorded (`record_exit`; its time per `## RECORDS` D5-b) — each with `source = 'trading_log'` and `source_import_id` = the `drc_imports` row id; a card with no legs: `## RECORDS` D5-a; a Cobalt leg with no DAS execution: `## RECORDS` D5-c; his taps and held statements stay as rows; after it, running shares = the DAS position; the unit re-renders `adjusted to DAS: <k> rows (<ids>)`. The writes run on the event day's build only (`## RECORDS` D5-d), never inside `plan_note`: `cobalt drc build --dry-run` calls `plan_note` alone (`drc/cli.py:288`–`:292`) and writes nothing (v2 `[F-09]`, `:79`) | red: with-DB, a card with ½ off tapped at a price the export disagrees with → after the build, a correction row naming the import and the running count equal to the export's; negative control: the same day `--dry-run` → no `legs` row added | `src/cobalt/drc/reconcile.py`, `src/cobalt/drc/build.py`, `src/cobalt/drc/units.py`, tests |
| D5-3 | THE REFUSAL (R90): a `LegRefused` is never forced and never fails the build: stored as an unresolved item (card id, leg ids, the export rows, the refusal text and `code` verbatim) on the day's `build_day.derived`; rendered `unresolved: card <id> — <refusal>` in the reconcile unit AND in K3's A31 section `drc-open-items/open_positions`; carried on every later DRC until resolved; the DRC book keeps the position OPEN as the export shows it (no CLOSED→open card edge: O20). RESOLVED when a later reconcile of that card succeeds, or when a current `drc_stated_books` `resolve` row names that trade (K3-7's RESOLVE, offered on `/drc` beside the line — ONE resolve path, L3) | red: the X11 shape → the line in both units, the DRC built, and the line still there on the next day's build; gone after a resolve row for that trade | `src/cobalt/drc/reconcile.py`, `src/cobalt/drc/build.py`, `src/cobalt/drc/units.py`, `src/cobalt/drc/imports.py` (`day_view` offer only), `src/cobalt/aset/drc_page.py`, tests |
| D5-4 | REALIZED R (`[F-19]`, v2 B25 / C2): the trade block's `realized not computed (D5)` becomes `legs.realized_r` over the post-reconcile current legs, stored with `fn_version = realized_r.1` and its inputs; provisional while any leg is estimated, as `realized_r` returns it (never restated, L3); `not computed — <reason>` when the trade has no matched card, the card has no legs, or the reconcile was refused | red: the line still reads `not computed (D5)` for a reconciled card | `src/cobalt/drc/build.py`, `src/cobalt/drc/units.py`, tests |
| T | the tree state: every with-DB test of this build that needs `0021` (the `legs` writer opens its own connection, so it needs a real forward) gets a `--deselect` in the pass-1 commands and its id in the pass-2 commands, in `BUILD-HUB.md` (c), (c3) and `DEPLOY-HUB.md` STEP-G, exactly as executed (precedent: `tests/cobalt/test_legs_c2_db.py`) | `git diff <BASE> -- <both hub files>` shows only these ids added | `docs/40 - DevDocs/prompts/BUILD-HUB.md`, `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` |
| DOC | a paragraph dated the day the build runs, `<date> — DRC D5`, in the DevDocs pages of each `drc/` module D5 edits, and a new `reconcile.md` | — | `docs/40 - DevDocs/cobalt/drc/` |

## NOT IN THIS JOB
- A second leg writer, any `INSERT` / `UPDATE` on `legs` outside `cards.legs` (L3, L40); a change to `cards/legs.py`; a CLOSED→open card edge (O20, a trading-logic change); a migration (a need → `FAILED: <step> — migration needed`, next free number `0023`).
- A second RESOLVE (D5-3 offers K3-7's); any other A31 item; the daily-note C13 line; `daily.md.j2`; a smoke row.
- Opening by Edit or Write `tests/cobalt/test_drc_d3_fix_r1.py`, `tests/cobalt/test_drc_build.py`, `tests/fixtures/drc/template_shape.md` (U+00A0).

## READ
- v2 `:80` (the reconcile step), `:96` (S-C1 / S-C2, `[F-11]`), `:117` (`[F-19]`), §9 row D5 and the Order paragraph (`:179`–`:181`), X11 (`:203`), `## OPEN — ROUND 2` (`:235`–`:247`) with his settlement `reports/cto-2026-09-22.md` R90.
- `src/cobalt/cards/legs.py` whole (docstring, `_check_source`, `insert_entry_leg`, `record_exit`, `record_correction`, `running_shares`, `realized_r`, `read_position`); `src/cobalt/drc/build.py` (`matched`, `day_derived`, `plan_note`, `:627`); `src/cobalt/drc/units.py` (`reconcile`, K3's `open_positions` / A31 units); K3's build report `## FOR THE CHECK` on its branch.
- `tests/cobalt/test_legs_c2_db.py` (the real-forward legs fixture shape).

## CHECK ASKS
- X1 Does any path write `legs` except through `cards.legs` with `source = 'trading_log'` and the import id?
- X2 Is a refusal ever forced, or does it ever fail the build?
- X3 Is the unresolved line carried on the next day's build and cleared only by a successful reconcile or a current resolve row for that trade?

## RECORDS
- Judge, 10-04: R90's "RESOLVE action for that line (his choice recorded on the trade, versioned)" is read as K3-7's RESOLVE `closed outside the export` on that trade (a `drc_stated_books` row, versioned by `supersedes`): one resolve path (L3). The other choice R90 names, "leave it opened", is the default and needs no action. On his veto list at DONE.
- STACKED (desk R233, his "S3 deploys Monday night"; 03c precedent: ONE parent, a checked tip, no merge). The chain is `01` K3 (on `main`) → `03` D5 (on K3's CHECKED tip: D5 edits K3's `build.py`, `units.py` and A31 section, so it needs K3's check fixes) → `02` F15 P2 (on D5's BUILT tip: P2 shares no source file with either, and its row T then writes its pass-1 / pass-2 ids on top of D5's, so the two hub-line edits never meet in a merge). The deploy TIP order is 01, 03, 02. A fix commit from D5's check touches D5's files only, so P2's head still merges clean; a D5 check fix to the hub lines → the desk names it before the deploy.
- The re-read drafter's four ASK DESK items, 2026-10-04 (`reports/s3-reread-draft-2026-10-04.md` `## DECISIONS`); each default below binds until the desk answers:
  - D5-a — a card with no legs (filled before C1): v2 `:80` gives it an entry leg from DAS "through the same writer", but `insert_entry_leg` (`cards/legs.py:246`) writes `source_import_id = NULL` (`:274`) and `0021_legs.sql:63` refuses `source = 'trading_log'` without one. Default: no entry leg is written; the exit diff and writes run on the pre-C1 basis `running_shares` reads (`legs.py:323`–`:328`); the unit shows `entry leg: not written — the entry writer carries no import id`.
  - D5-b — a new exit leg's time: `record_exit` stamps `at = now` (`legs.py:431`), and `now` also drives the `market_reset` gate (`:409`). Default: `now` is the build's clock, never the export's time; the export time is then set by one `record_correction(leg, at=<export time>, source='trading_log', source_import_id=…)`.
  - D5-c — a Cobalt leg with no DAS execution: no writer removes a leg (`record_correction` refuses `shares <= 0`, code `shares`, `legs.py:519`–`:520`). Default: no write is tried; it is stored and rendered as a D5-3 unresolved item, reason `no writer removes a leg`.
  - D5-d — which builds write: a carried trade's DAS rows for one day hold only that day's executions while the card's legs span every day, and `run_drc_build` rebuilds every re-paired date (`build.py:704`). Default: writes run only on the event day's build (`check=True`) and only for a trade with no `inputs.carried_from`; a carried trade and a re-paired date get the diff stored and rendered, `adjustment not written — <carried trade | re-paired date>`.
- DOC row date: the paragraph carries the date the build runs.
- HOUSE B at the check: `mandatory — vault notes` (the DRC note's units).
- RESTARTS: derived (`drc/*`, `aset/*` → `com.cobalt.aset` per v2 `[F-27]`; quote `cobalt jobs restarts`).
