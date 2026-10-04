JOB: drc-k3
LADDER: S3-P3 · F14
BRANCH: drc/k3-surfaces-1004
WORKTREE: drc-k3-1004
BASE: 979ec797
TIP:
REPORT: /Users/cobalt/cobalt-wt/drc-k3-1004/docs/40 - DevDocs/reports/drc-k3-build-2026-10-04.md
CHECK REPORT:
HOUSE B:
TREE STATE: unchanged
RULINGS: 2026-10-03 R219

## ROWS

WHY: re-cut of `prompts/2026-09-29/30-drc-k3-build.md` (drafted on `drc/d1-trading-log` at `985cca3b`, never launched, held for the fixed-file flow 09-30 R63) onto `main`. D1–D3, K1, K2 are live since deploy `2026-09-30-1` (migrations `0016`, `0018`–`0020` on `main`); `drc/d1-trading-log` is one docs commit above `main`, so the K3 seam with `s3/exits-c4` in `aset/web.py` is gone (S3 is on `main` too). Each row's full text is that prompt's row of the same id (`## THE BEHAVIOURS`, lines 22–30): the builder reads it, re-greps every `file:line` it cites at BASE, and quotes what `grep -n` prints. No migration: every kind K3 writes exists.

| row | what | red first | files |
|---|---|---|---|
| X | the four v3 experiments before any `src/` edit (v3 `## First-gate experiments`): X11 (`:327`, re-run K2's `test_drc_k2_experiments.py` X11 tests), X13 (`:334`, after a green X7 re-run; the older `unit_after` put back on disk in a `tmp_path` vault), X14 (`:335`, on a `tmp_path` copy of `tests/fixtures/drc/template_shape.md`), X15 (`:336`, the unit bytes under their heading and his text byte-identical, on the same `tmp_path` copy) | RUN — asserts nothing; each result quoted; a design-changing result is a `DECISION X<n>` (X14's named consequence stops K3-2 only) | `tests/cobalt/test_drc_k3_experiments.py` |
| K3-1 | the `drc-trades/open_positions` unit from ONE stored list `build_day.derived["open_positions"]` computed once in `plan_note` (`30` K3-1) | a test asserting the header, one line per position and the three loud states, red on BASE (`units.OPEN_POSITIONS` absent) | `src/cobalt/drc/build.py`, `src/cobalt/drc/units.py`, tests |
| K3-2 | `open overnight: <n>` in the summary from the SAME list (`30` K3-2); not built if X14 is design-changing | red: the summary lacks the line | `src/cobalt/drc/units.py`, `src/cobalt/drc/build.py`, tests |
| K3-3 | the A31 section `drc-open-items/open_positions` after `drc-trades` (`30` K3-3) | red: the section is absent; D3's E3 test stays green unopened | `src/cobalt/drc/units.py`, `src/cobalt/drc/build.py`, tests |
| K3-4 | the stale renderings: a restated resolve, `book_stale`, the `[F-03]` note half (`note_stale` key); the ONE read-only store method `superseded_stated_ids` (`30` K3-4) | red per state | `src/cobalt/drc/build.py`, `src/cobalt/drc/units.py`, `src/cobalt/drc/store.py` (that method only), `src/cobalt/drc/imports.py` (`day_view` only), tests |
| K3-5 | the `/drc` hand-off: only `_morning`'s `book is None` line changes; the after-drop line in `day_view` (`30` K3-5) | red: the old CLI-only text | `src/cobalt/drc/imports.py`, `src/cobalt/aset/drc_page.py`, tests |
| K3-6 | the state-your-book form: `imports.state_book`, `[I was flat]` one tap, a listed book preview → confirm with `expected_sha256`; `cli._rebuilds`' body MOVED to `imports.statement_rebuilds` (`30` K3-6) | red: no `state_book`; every CLI state-book test green unchanged | `src/cobalt/drc/imports.py`, `src/cobalt/drc/cli.py` (`_rebuilds`' body moved only), `src/cobalt/aset/web.py`, `src/cobalt/aset/drc_page.py`, tests |
| K3-7 | RESOLVE `closed outside the export`, offered only for `seed_for(day)` trade ids, preview → confirm (`30` K3-7) | red: no `resolve`; an id outside the seed refused, nothing written | `src/cobalt/drc/imports.py`, `src/cobalt/aset/web.py`, `src/cobalt/aset/drc_page.py`, tests |
| K3-8 | the notes after a statement: `build.rebuild_notes(dates)` factored out of `run_drc_build`'s loop, two callers (`30` K3-8) | red: no `rebuild_notes`; `run_drc_build`'s tests unchanged | `src/cobalt/drc/build.py`, `src/cobalt/drc/imports.py`, tests |
| K3-9 | the routes `POST /drc/state-book`, `POST /drc/resolve` inside D2's `/drc` block, `drc_no_trade`'s shape (`30` K3-9; `30`'s `:1517`–`:1610` were read at `985cca3b` — on `main` the block opens at `web.py:2067`, `drc_no_trade` `:2138`, `drc_scan` `:2152`) | red: 404 on both | `src/cobalt/aset/web.py`, tests |
| DOC | one paragraph dated the day the build runs, `<date> — DRC K3`, in each DevDocs page of a `drc/` module K3 edits (`build.md`, `units.md`, `imports.md`, `store.md`, `cli.md`) | — | `docs/40 - DevDocs/cobalt/drc/` |

## NOT IN THIS JOB
- The voice caller (K4); every other A31 item and the reconcile writes (D5, card `03`); a migration (a need → `FAILED: <step> — migration needed`, next free number `0023`).
- Any writer of `src/cobalt/drc/store.py` (`record_stated_book`, `seed_for`, `record_day`, `rebuild`, `effect_day`, `_repair`, `_commit`); `pairing.py`, `models.py`, `trading_log.py`, `stats_log.py`, `detect.py`, `playbooks.py`, `template.py`; `src/cobalt/cli.py`; `src/cobalt/settings/*`; a smoke row.
- Opening by Edit or Write `tests/cobalt/test_drc_d3_fix_r1.py`, `tests/cobalt/test_drc_build.py`, `tests/fixtures/drc/template_shape.md` (they hold U+00A0; read and import only).
- A test write to the dev vault or his vault (BUILD-HUB: both read only); the dev-vault proof is the desk's step after the check.

## READ
- `prompts/2026-09-29/30-drc-k3-build.md` `## THE SEAMS YOU BUILD ON` and `## THE BEHAVIOURS` (rows K3-1 to K3-9 in full); `reports/drc-k3-build-draft-2026-09-29.md` `## DECISIONS`, `## ESCALATE`.
- `docs/30 - Design/DRC-OVERNIGHT-POSITION-v3-2026-09-24.md` §2a–§2c, §5, §6 row K3, `[F-03]`, `[F-06]`, `[F-11]`, `[F-16]`, X11, X13–X15.
- The `## FOR K3` sections: `reports/drc-d3-fix-r2-build-2026-09-29.md` (on `drc/d1-trading-log`: `git show 985cca3b:<path>`), `drc-d2-fix-r2-build-2026-09-28.md`, `drc-k2-fix-r2-build-2026-09-25.md`.

## CHECK ASKS
- X1 Is every unit figure a key of `build_day.derived` with its inputs (L57), from ONE list (L3)?
- X2 Does the form or RESOLVE write anything except through `record_stated_book` with `via="drc_page"`?
- X3 Is `cli._rebuilds`' logic byte-identical after the move, and is every CLI state-book test unchanged?

## RECORDS
- Judge, 10-04: the drafter's ESCALATE 2 (preview → confirm with `expected_sha256` for a listed book and a RESOLVE; `[I was flat]` one tap) and 3 (A31 placement after `drc-trades`) KEEP as written in `30`. ESCALATE 5 (`last execution not stored`) stays a `## DECISIONS` item if met.
- Judge, 10-04: X13 and X15 run in `tmp_path` vaults (BUILD-HUB: the dev vault is read only). The dev-vault proof of the whole build (v3 X15's dev-vault half; the 09-29 drafter's item 10) is the desk's step after the check, before the deploy.
- TREE STATE `unchanged` holds while every new with-DB test uses `tests/cobalt/test_drc_store.py`'s `migrated` fixture (DRC migrations inside the suite's rollback; DRC's with-DB tests run in pass 1 at `0013`). A test that needs a real forward → `## DECISIONS`, not a hub edit.
- HOUSE B at the check: `mandatory — vault notes` (K3 writes his DRC note's units).
- RESTARTS: derived (`drc/*`, `aset/web.py`, `aset/drc_page.py` → `com.cobalt.aset` expected; quote `cobalt jobs restarts`).
- Seams with the other two cards of 10-04 (desk R233, one deploy): the chain is `01` this card (on `main`) → `03` D5 (on this card's CHECKED tip; it edits `build.py`, `units.py` and the A31 section after this card) → `02` F15 P2 (on D5's BUILT tip; it shares no file with this card). TIP order 01, 03, 02.
