# Card 01 drc-k3 — preflight 2026-10-04

§0: 8 checks, 1 FAIL. Check 7: the card ends with no K25 PRE-STOP SELF-CHECK (`grep -n -E "K25|PRE-STOP"` on the card → no output). Everything else holds. Ready: NO until the desk adds it.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C … merge-base --is-ancestor 979ec797 main` · `git -C … log --oneline -1 979ec797` | exit 0, no output · `979ec797 Merge branch 'main' into deploy/set3b-1004` | OK |
| 2 | `git -C … rev-parse --verify drc/k3-surfaces-1004` · `ls /Users/cobalt/cobalt-wt/` | `fatal: Needed a single revision` (branch absent) · the listing has no `drc-k3-1004` (nearest: `drc-d1`) | OK |
| 3 | `git show 979ec797:<path>` for every `files` path, plus every cite | See 3a–3c below | OK |
| 4 | RESTARTS class vs the `files` paths | Card `## RECORDS`: `RESTARTS: derived (drc/*, aset/web.py, aset/drc_page.py → com.cobalt.aset expected; quote cobalt jobs restarts)`. Every `src/` path in the rows is under `drc/*`, `aset/web.py` or `aset/drc_page.py`. Tests and DevDocs paths are not named, and carry no restart class. | OK (see NOTES 2) |
| 5 | design cites in `DRC-OVERNIGHT-POSITION-v3-2026-09-24.md` | `:327` X11 "A resolve with no exit price on a carried trade: CLOSED, `legs = []`, realized `not computed…`" · `:334` X13 "After a green X7, put an older `unit_after` of `drc-trades/open_positions` back on disk" · `:335` X14 "On a copy of his note shape (no `drc-summary`, no `open_positions` section), upsert unit…" · `:336` X15 "Dev vault: unit bytes under their heading, his text byte-identical (v2 E3 shape)." Each says what the rows say. | OK |
| 6 | RULINGS greps | See 6a–6c below | OK (NOTE 1) |
| 7 | each row has a red-first test; the card ends with a K25 PRE-STOP SELF-CHECK | Rows K3-1 to K3-9 each carry a `red first` cell. The card's last section is `## RECORDS` (line 47). `grep -n -E "K25\|PRE-STOP"` → no output. | **FAIL** |
| 8 | `grep -c -F "«FILL" <card>` | `0` | OK |

3a. Paths that exist at BASE (`git ls-tree`, `git show`): `src/cobalt/drc/{build,units,store,imports,cli}.py`, `src/cobalt/aset/{web,drc_page}.py`, `tests/cobalt/test_drc_k2_experiments.py`, `test_drc_d3_fix_r1.py`, `test_drc_build.py`, `test_drc_store.py`, `tests/fixtures/drc/template_shape.md`, and the DevDocs pages `docs/40 - DevDocs/cobalt/drc/{build,units,imports,store,cli}.md`. `git diff --stat 979ec797 main` over `src/cobalt/drc`, `aset/web.py` and `aset/drc_page.py` is empty, so BASE equals main for them. New files: `tests/cobalt/test_drc_k3_experiments.py` (absent at BASE; the row lists it as the file to create).

3b. Cites and names at BASE:
- `build.py:324` `def plan_note(day: date, *, deps: BuildDeps, event, check: bool = True)`.
- `build.py:697` `def run_drc_build(event, *, deps…)`.
- `store.py` has `record_day:281`, `rebuild:329`, `effect_day:385`, `_repair:704`, `_commit:850`, `seed_for:1038`, `record_stated_book:1340`.
- `imports.py` has `_morning:739` with `if book is None:` at `:751`, `day_view:789`, `no_trade_event:691`.
- `cli.py` has `_rebuilds` (`def _rebuilds(store, req: StateBookRequest) -> bool`) and `cmd_state_book`.
- `web.py:2067` `# DRC D2-4: the \`/drc\` import page`, `:2138` `async def drc_no_trade(date: str = Form(...))`, `:2152` `async def drc_scan(date: str = Form(...))`.
- `test_drc_k2_experiments.py` has X11 at `:556` and X7 at `:198`.

3c. Names the card says are absent are absent: `OPEN_POSITIONS` in `units.py` (its `__all__` has no such name), `state_book` and `statement_rebuilds` in `imports.py` (`grep -c` → 0), `rebuild_notes` in `build.py`, `superseded_stated_ids` in `store.py`.

6a. R51 (`cto-2026-09-24.md:69`): status cell `APPROVED — design ruling; carried into v3 FINAL by the K-build drafter`. `HIS RULING`: no. The row text reads "R2-1 RULED "A"… His word, desk chat 12:55 ET". `APPROVED`: yes.

6b. R52 (`cto-2026-09-24.md:70`): status cell `APPROVED — design ruling; carried into v3 FINAL by the K-build drafter`. `HIS RULING`: no. The row text reads "His word, desk chat 12:57 ET". `APPROVED`: yes.

6c. R219 (`cto-2026-10-03.md:225`): status cell `HIS RULING · APPROVED`. Both present.

## ISSUES
- FAIL check 7: the card ends with no K25 PRE-STOP SELF-CHECK. Its last section is `## RECORDS` (line 47).

## NOTES
1. R51 and R52 read `APPROVED — design ruling` and carry no `HIS RULING` tag. Reported as a NOTE, not a FAIL, as ordered.
2. The card's RESTARTS line names only the `src/` classes. The tests and DevDocs paths have no class listed. I read that as no restart.
3. Rows X and DOC have no red-first test: X reads "RUN — asserts nothing", DOC reads "—". I took both as intended by design.
4. The card's own cites are all checked. The rows' full text lives in `prompts/2026-09-29/30-drc-k3-build.md` `## THE BEHAVIOURS`, and its inner `file:line` cites (at `985cca3b`) were not re-checked here. The card tells the builder to re-grep them at BASE.
5. This session's tool results said nothing that asked for an action beyond the prompt.

PREFLIGHT DONE · card: 01 · checks: 8 · fails: 1 · ready: NO
