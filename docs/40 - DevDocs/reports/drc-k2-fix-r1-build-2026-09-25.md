# DRC K2 FIX R1 BUILD — 2026-09-25

Seat `drc-k2-fix-r1-build-0925` · prompt `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-25/02-drc-k2-fix-r1-build.md` · branch `drc/d1-trading-log` · base `09ce3742` · start `Fri Sep 25 01:42:38 EDT 2026` (`<D>` = `2026-09-25`).

## §0 Headline
- All 5 FIX rows are built (F-1 resolve key across days + `effect_day`; F-2 `book_stale` mark; F-3 one no-trade seed; F-4 stats re-matched; F-5 one partial rule). `drc.pairing/4`. The red commits are `d2abba17` / `11e9af9a`; the fix is `a51988c9` + `d684f80b`; the tip is `4626a1f2`.
- RUN-1 is GREEN (a plain pin).
- All three gate suites passed on the tip. Offline: 2467/0. With-DB: 2915/0 (4 deselected). Live-note: 142/0.
- `.env` is removed and proven gone. `0016`/`0018` are proven absent from `cobalt_dev` (the probe is short by 4).
- ESCALATE: 9 (0 ASK DESK). This build found and corrected one defect of its own in F-1 (a variable shadow, ESCALATE 5).

## L74
A `<system-reminder>` block arrived INSIDE the Read tool result of the prompt file (after line 122) asking that commits end with a `Claude-Session: https://claude.ai/code/…` line and naming a file-send tool (`SendUserFile`). Recorded as DATA per L74; not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| rule | command | exit | result |
|---|---|---|---|
| placeholder gate | `grep -n -E "R_[_]" …/02-drc-k2-fix-r1-build.md` | 1 | (no output) |
| 52's stop | `tail -n 3 …/drc-k2-check-2026-09-24.md` | 0 | last non-blank: `DRC K2 CHECK DONE · round: 1 · … · defects that HOLD: 9 · ready for K3: NO · ESCALATE: 11` |
| 52 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- …/drc-k2-check-2026-09-24.md` | 0 | `eaa9c49b56a4f1dc8d5a18831680b45f5b33c011` |
| classification | `tail -n 3 …/drc-k2-fix-r1-draft-2026-09-25.md` | 0 | last non-blank: `DRC K2 FIX R1 DRAFTED · FIX: 8 · NOT REAL: 11 · UNPROVEN: 1 · OUT OF SCOPE: 6 · OWNER ITEM: 0 · prompts: 2 · new rule strings: 0 · ESCALATE: 3` |
| classification committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- …/drc-k2-fix-r1-draft-2026-09-25.md` | 0 | `1f76d9d9c68494856d4db82769a2ccbef59615c7` |
| .env strings his | `grep -n -F "Bash(rm /Users/cobalt/cobalt-wt/drc-d1/.env)" …/cto-2026-09-24.md` | 0 | `:39` R21 (desk record) and `:40` `\| R22 \| 07:56 ET \| His words: "approved. A for now. …` |
| R22 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"approved. A for now" -- …/cto-2026-09-24.md` | 0 | `813a4dfa27ace0faede64584d45932169345db9e` |
| launch row | `grep -n "02-drc-k2-fix-r1-build.md" …/cto-2026-09-25.md` | 0 | `:14` R6 (not counted) and `:15` `\| R7 \| 01:42 ET \| … DESK LAUNCH ROW for 02-drc-k2-fix-r1-build.md …` |
| launch row committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"02-drc-k2-fix-r1-build.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | 0 | `1f76d9d9c68494856d4db82769a2ccbef59615c7` |

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| date | `date` | 0 | `Fri Sep 25 01:42:38 EDT 2026` |
| clean | `git status --short --branch` | 0 | `## drc/d1-trading-log` |
| tip | `git log --oneline -2` | 0 | `214c4b39 docs(k2): DRC K2 build report — 09ce3742` / `09ce3742 feat(drc): K2 — no-trade carry, …` |
| code unmoved | `git diff --stat 09ce3742 214c4b39 -- . ':(exclude)docs'` | 0 | (empty) |
| no .env | `ls /Users/cobalt/cobalt-wt/drc-d1/.env` | 1 | `No such file or directory` |
| lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| strategies | `ls ".../1 - Trading/4 - Strategies"` | 0 | 22 notes listed |
| requires_vault | `grep -rln "requires_vault" tests` | 0 | `tests/cobalt/test_radar_evaluate.py`, `tests/cobalt/radar_p2_support.py`, `tests/cobalt/test_replay_line.py`, `tests/taxonomy/test_catalyst.py`, `tests/taxonomy/test_predicate.py` (the expected set) |
| kept_match | `grep -n "kept_match" src/cobalt/drc/store.py` | 0 | `484`, `489`, `490`, `520`, `525` |
| partial | `grep -n "if outcome is Outcome.PARTIAL else" …store.py` | 0 | `459` |
| stop | `grep -n "stop = None if _Close.computed(pairing) else _stopped(pairing.day)" …store.py` | 0 | `556` |
| not_computed | `grep -n "derived->'not_computed' ? 'pairing'" …store.py` | 0 | `852` |
| resolve filter | `grep -n "(%s::text IS NULL OR positions->0->>'trade_id' = %s)" …store.py` | 0 | `1019` |
| no_trade_id | `grep -n "no_trade_id = self._no_trade_id(conn, pairing.day)" …store.py` | 0 | `312` |
| absent | `grep -n "absent = [c for …]" …trading_log.py` | 1 | no hit (regex bracket); re-run `grep -n -F` → `170` |
| partial flag | `grep -n "PARTIAL — missing:" …models.py` | 0 | `236`, `262` (expected `263`: LINE MOVED) |
| FN_VERSION | `grep -n "FN_VERSION = " …pairing.py` | 0 | `87: FN_VERSION = "drc.pairing/3"` |
| _rebuilds | `grep -n "def _rebuilds" …cli.py` | 0 | `127` |
| FN pins | `grep -rn "drc.pairing/3" tests/cobalt` | 0 | `test_drc_k2.py:75`, `test_drc_store.py:403`, `test_drc_k1.py:66`, `test_drc_k1_store.py:497` |

## F1 BASELINE
- Offline `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (exit 0): `2463 passed, 449 skipped, 1 xfailed, 15 warnings in 68.97s` → `<bp>` = 2463, `<bf>` = 0 (as `51`'s S8).
- Live-note `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` (exit 0): `142 passed, 1 skipped, 15 warnings in 9.81s` → `<blp>` = 142, `<blf>` = 0. The one SKIPPED: `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (the known one); no SKIPPED line names `COBALT_LIVE_VAULT_ROOT`.

## F2 RED (offline)
- New `tests/cobalt/test_drc_k2_fix_r1.py` (4 tests, F-5); named reversal 1: `tests/cobalt/test_drc_k2.py:72-75` `test_the_pairing_version_is_3` → `test_the_pairing_version_is_4` (`drc.pairing/4`, docstring names K2 fix r1 and the four stored shapes).
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_drc_k2_fix_r1.py tests/cobalt/test_drc_k2.py` (exit 1): `5 failed, 19 passed in 0.09s`. Failures, exactly the named rows:
  - `test_missing_of_a_parsed_import_is_empty` — `ImportError: cannot import name 'missing_of' from 'cobalt.drc.models'`
  - `test_missing_of_inverts_the_partial_flag` — same `ImportError`
  - `test_missing_of_refuses_an_unreadable_partial_reason` — same `ImportError`
  - `test_pairing_not_computed_is_the_first_records_text` — `ImportError: cannot import name 'pairing_not_computed' from 'cobalt.drc.trading_log'`
  - `test_the_pairing_version_is_4` — `AssertionError: assert 'drc.pairing/3' == 'drc.pairing/4'`
- Commit `<red>` = `d2abba17 wip(k2-fix-r1): DRC K2 fix r1 red tests, offline — one partial-import rule, drc.pairing/4 (L75)`.

## F3 RED (with-DB)
- New `tests/cobalt/test_drc_k2_fix_r1_store.py` (8 tests: F-1 ×3, F-2 ×2, F-3, F-4, F-5), harness by import; `D4 = date(2001, 1, 5)` defined in the file.
- LOCK (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found` · (b) `cp …/.env …/drc-d1/.env` → exit 0; `ls -la …/*/.env` → exactly one line `-rw------- … /Users/cobalt/cobalt-wt/drc-d1/.env`.
- (c) run 1 `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_drc_k2_fix_r1_store.py tests/cobalt/test_drc_k2_store.py tests/cobalt/test_drc_k2_experiments.py` (exit 1): `8 failed, 36 passed in 2.51s`. Seven reds were the named reasons; ONE named test, `test_every_later_day_of_a_stopped_chain…`, was red on MY setup (`assert _stated_rows(migrated) == books` — `books` read before `_stopped_chain` states D_NEXT), not on `book_stale`. The test was corrected (the L7 check moved inside `_stopped_chain`, around D's record only; no assertion of the row loosened) and re-run in the SAME lock take (lock re-read: one line, this worktree's).
- (c) run 2, same command (exit 1): `8 failed, 36 passed in 2.64s`; no SKIPPED line (not skipped). The eight, one-line reasons:
  - `test_a_second_current_resolve_for_one_trade_on_another_day_is_refused` — `Failed: DID NOT RAISE <class 'ValueError'>`
  - `test_a_resolve_restated_on_another_day_supersedes_and_rebuilds_from_the_earlier_day` — `ValueError: 2001-01-04 resolve for DDD-long-2001-01-02T10:00:00-05:00: supersedes #3 names no single current row — current: none; nothing written`
  - `test_the_cli_restatement_rebuilds_from_the_superseded_rows_day` — `assert (0 == 0 and 'on --apply: rebuild 2001-01-03 and every later recorded day' in 'cobalt drc state-book — DRY RUN …')` (the base prints the restatement's own day)
  - `test_every_later_day_of_a_stopped_chain_carries_the_stale_mark_and_fails_its_successor` — `KeyError: 'book_stale'`
  - `test_the_stale_mark_leaves_when_the_root_is_stated_and_rebuilt` — `KeyError: 'book_stale'`
  - `test_a_no_trade_day_recorded_by_record_day_stores_the_no_trade_carry` — `AssertionError: assert ('carried' == 'no_trade_carry'`
  - `test_an_unpaired_day_with_a_stats_log_is_re_matched_when_it_is_paired` — `At index 0 diff: ('unmatched — no trades were paired', None) != ('matched', 'DDD-long-2001-01-02T10:00:00-05:00')` (the kept `pairing did not run` match)
  - `test_a_partial_file_missing_only_a_non_pairing_column_stays_paired_through_a_re_pair` — `At index 0 diff: ('day', 'day', '{"import_ids": {"trading_log": 2}}', '{"not_computed": {"pairing": "[...]` (D_NEXT un-paired by the re-pair)
- GREEN-as-pin: `test_drc_k2_experiments.py:397` `test_x9_pass_c_a_not_computed_match_is_kept` passed (among the 36).
- (d) `rm …/drc-d1/.env` → exit 0; `ls …/drc-d1/.env` → `No such file or directory`. **.env: removed, proven gone (F3).**
- Commit `11e9af9a wip(k2-fix-r1): DRC K2 fix r1 red tests, with-DB — resolve key across days, the stale mark, one no-trade seed, stats re-matched, one partial rule (L75)` (01:48 ET).

## F4 THE EDITS
Src (each quoted whole by `git diff 09ce3742 -- src` below):
Line numbers below are from `grep -n` on the committed tree (resolve branch `store.py:1097`, `INSERT` `:1126`, `effect_day` `:371`, `_no_trade_seed` `:552`, its callers `:319` / `:542`, `missing_of` calls `:472` / `:530`, stats-import guard `:521`, `stale_mark` `:623`, `root, stop` `:636`, `for d in stale:` `:651`, stale refusal `:937`; `models.py` `:38`, `:239`, `:265`, `:269`; `trading_log.py` `:73`, `:181`; `cli.py` `:139`, `:151`, `:161`, `:181`; `pairing.py:90`).
- **F-1** `store.py` `record_stated_book` (`:1097-1113`): for `resolve` the current set is every current resolve naming the trade id, any day; `opening` / `no_trade` keep `(day, kind)`; refusals name `#<id> (<day>)`; the `supersedes` rule, the table lock, `_reason` and the one `INSERT` unchanged. NEW `DrcStore.effect_day` (`:371-386`). `cli.py` `_rebuilds` (`:129-142`) and `cmd_state_book` (`:151`, `:161`, `:181`) use `effect_day`. `_with_resolves` unchanged.
- **F-2** `store.py` `_commit` (`:611-623`, `:636`, `:651-656`): each `not_repaired` day's own `day` row gets `derived.book_stale = {root, reason}` by one `UPDATE … derived || %s` in the same transaction (`drc_rows` has no append-only trigger; only `0018_drc_stated_books.sql:51`'s table does). `_carried` (`:927-940`) refuses a marked prior. The mark leaves only when a re-pair rewrites the day whole through `_rows`; no code clears it otherwise.
- **F-3** `store.py` NEW static `_no_trade_seed` (`:552-574`); `_repair` calls it (`:543`), `record_day` calls it (`:318-319`).
- **F-4** `store.py` `_repair` (`:511-540`): `kept_match` and the `model_copy` removed; the stats input rebuilt from the stored rows with the stats import's own outcome and `missing_of(...)`, always passed to `build_day`; no stats import named → `PairingError`. `Unmatched` import dropped (unused).
- **F-5** `models.py` `PARTIAL_PREFIX` (`:38`), both `partial_flag` (`:239`, `:265`), NEW `missing_of` (`:269-279`), exported. `trading_log.py` NEW `pairing_not_computed` (`:73-80`), called by the parser (`:181`), exported. `store.py` `_repair` (`:470-488`): the partial rule through `missing_of` + `pairing_not_computed`; an unreadable reason → `PairingError`.
- **FN_VERSION** `pairing.py:90` → `"drc.pairing/4"`.

Named test edits:
- Reversals 2–4 (FN pins): `test_drc_k1.py:68`, `test_drc_k1_store.py:499`, `test_drc_store.py:405` → `drc.pairing/4` (each docstring gains one K2 fix r1 sentence; the two without a docstring gained one).
- Reversal 5 (F-5): `test_drc_k2_experiments.py:462` → `== f"not computed — missing: Price"`; docstring's last clause → `= the first record's text (K2 fix r1 F-5; v3 :181, FR14)` + one sentence. The `reason` read above it was REMOVED (it had no other use).
- Reversals 6–7 (F-2): `test_drc_k2_experiments.py:548-549` and `test_drc_k2_store.py:197-198` → `_without_stale(_snapshot(…D_NEXT)) == before` AND `book_stale == {"root": "2001-01-02", "reason": _NOT_COMPUTED_PRIOR}`; docstring sentence added. A test helper `_without_stale` was added to `test_drc_k2_experiments.py:133` for these two and the new store file (moved there from the F3 file, which now imports it).
- The ONE SETUP CHANGE (F-1; NOT an assertion change): `test_drc_k2_store.py:325-331` — `second` is a direct insert through the store's proxy (the pre-lane test's shape), copying `first`'s row with `day = D3`, `RETURNING` the stated columns into `_stated(...)`; `first`, `both` and every `pytest.raises` line are byte for byte. Docstring sentence added as named.
- THE REORDER RULE: no other with-DB test needed the setup change (proven at F5's with-DB run below).

DevDocs: `docs/40 - DevDocs/cobalt/drc/{store,models,trading_log,cli,pairing}.md`, one dated `K2 fix r1` paragraph each.

Proofs:
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_drc_k2_fix_r1.py tests/cobalt/test_drc_k2.py tests/cobalt/test_drc_k2_experiments.py tests/cobalt/test_drc_k1.py tests/cobalt/test_drc_k1_experiments.py tests/cobalt/test_drc_k1_fix_r1_runs.py tests/cobalt/test_drc_pairing.py tests/cobalt/test_drc_store.py tests/cobalt/test_drc_stats_log.py tests/cobalt/test_drc_trading_log.py` (exit 0): `165 passed, 36 skipped in 0.30s` — **0 failed**; every file existed.
- `git diff --stat 09ce3742` (exit 0): exactly the five src files, the two new test files, the six named test files, the five DevDocs and `docs/40 - DevDocs/reports/drc-k2-build-2026-09-24.md` (`214c4b39`'s): `19 files changed, 899 insertions(+), 79 deletions(-)`. No other path.
- `git diff 09ce3742 -- src/cobalt/db_migrations configs src/cobalt/cli.py src/cobalt/drc/stats_log.py src/cobalt/drc/detect.py src/cobalt/aset src/cobalt/prefill src/cobalt/replay src/cobalt/vaultwrite` → empty. `grep -n "INSERT INTO drc_stated_books" src/cobalt/drc/store.py` → one hit `1126` (inside `record_stated_book`). `grep -n "INSERT INTO" src/cobalt/drc/cli.py`, `"UPDATE "`, `"DELETE FROM"` → empty each. `grep -rn "VaultWriter" src/cobalt/drc` → empty. `grep -n "kept_match" src/cobalt/drc/store.py` → empty.
- After the proofs, one whitespace-only edit: a second blank line after `pairing_not_computed` (`trading_log.py:81`, PEP 8); F7 runs on it.
- Commit `<fix>` = `a51988c9 fix(drc): K2 fix r1 — resolve key across days, the stale mark on a stopped chain, one no-trade seed, stats re-matched, one partial rule; drc.pairing/4 (L75, 09-25)`, plus its correction `d684f80b` (F5, ESCALATE 5: F-1's query result shadowed the validated positions; renamed `found`).

`git diff 09ce3742 -- src` (whole, as run before the blank-line edit; the committed tree adds only that blank line):
- `cli.py`: docstring sentence; `_rebuilds` → `day = store.effect_day(req.day, req.supersedes)` then `has_current_import(day, …)` / `has_chain_through(day)`; `cmd_state_book` → `effect = store.effect_day(req.day, req.supersedes)`, prints `rebuild {effect.isoformat()}`, calls `store.rebuild(effect)`.
- `models.py`: `PARTIAL_PREFIX = "PARTIAL — missing: "`; both `partial_flag` → `f"{PARTIAL_PREFIX}{', '.join(self.missing)}"`; `missing_of` (returns `[]` unless partial; `ValueError` if the reason lacks the prefix; else the names split on `", "`); `__all__` + `PARTIAL_PREFIX`, `missing_of`.
- `pairing.py`: the version comment's `/4` sentence; `FN_VERSION = "drc.pairing/4"`.
- `store.py`: import `missing_of` (drops `Unmatched`); `record_day` → `seed = self._no_trade_seed(seed, no_trade_id)`; `effect_day`; `_repair` partial rule via `missing_of` + `trading_log.pairing_not_computed`; the stats block rebuilt from the stats import's `name, parse_status, reason`; `kept_match` + `model_copy` removed; `seed = self._no_trade_seed(self._seed(conn, day, overlay), no_trade_id if imp is None else None)`; `_no_trade_seed`; `_commit` docstring + `stale` / `stale_mark` / `root` + the `UPDATE drc_rows SET derived = derived || %s … kind = 'day'` loop; `_carried` stale check + its `PairingError`; `record_stated_book` resolve-by-trade-id query + `#<id> (<day>)`.
- `trading_log.py`: `Iterable` import; `pairing_not_computed`; the parser calls it; `__all__` + `pairing_not_computed`.
(The full unified diff is the tool output of that call in this session; the checker re-derives it with `git diff 09ce3742 a51988c9 -- src`.)

## F5 THE RUN
- New `tests/cobalt/test_drc_k2_fix_r1_runs.py`, one test `test_run_1_a_no_trade_day_with_a_stated_opening_beside_a_recorded_prior` (RUN-1; build ESCALATE 9, `drc-k2-build-2026-09-24.md:255`). Setup reading (ESCALATE 6): D_NEXT is recorded (`rebuild(D_NEXT) == [D_NEXT]`, a no-trade day from his statement) BEFORE D, so D's forward re-pair reaches it — `_commit` re-pairs only days that have a `day` row.
- LOCK (a) `ls -la …/*/.env` → `(eval):1: no matches found` · (b) `cp` exit 0; `ls -la …/*/.env` → one line, `…/drc-d1/.env` (01:53).
- (c) run 1 `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_drc_k2_fix_r1_runs.py` (exit 0): `1 passed in 0.21s` — on `a51988c9`.
- (c) the F4 REORDER-RULE check, in the same take: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_drc_k2_fix_r1_store.py tests/cobalt/test_drc_k2_store.py tests/cobalt/test_drc_k2_experiments.py tests/cobalt/test_drc_k1_store.py tests/cobalt/test_drc_k1_experiments.py tests/cobalt/test_drc_store.py` (exit 1): `22 failed, 110 passed in 6.70s`. Cause, one: my F-1 edit named its query result `rows`, shadowing the validated positions `rows` that the `INSERT` writes — every statement stored `[]` (e.g. `psycopg.errors.CheckViolation: new row for relation "drc_stated_books" violates check constraint "drc_stated_books_check"` / `Failing row contains (3, 1, 2001-01-03, resolve, [], …)`). Not a test's assertion: a defect in my F-1 code. Corrected (`found`, `store.py:1101-1113`), nothing else changed.
- (c) re-run of that check (exit 0): `132 passed in 5.76s` — no red, no skip; the reorder rule needed no further setup change.
- (c) RUN-1 re-run on the corrected code (exit 0): `1 passed in 0.18s`. (Run 1's pass was on the shadowed code, where the opening was stored `[]`; the corrected run is the result.)
- RUN-1 RESULT (green, a plain pin): on D_NEXT, no exception; `seed.inputs` keys exactly `{source, from_day, from_book_sha256, stated_book_id}` with `source == "carried"`, `stated_book_id == op.id`, `from_day == "2001-01-02"`; `seed.derived` keys exactly `{count, trade_ids, stated_differs}` with `trade_ids == [<DDD trade id>]` and `stated_differs` non-empty, holding the `DDD` trade id; `day.inputs.no_trade_id == nt.id`; `stated_difference(D_NEXT)` starts `stated book for 2001-01-03 differed from 2001-01-02's close:`; the `record_day` path stores a `seed` row equal to the re-pair's; `drc_stated_books` gains only D's own opening across D's record, nothing across `record_day`.
- (d) `rm …/drc-d1/.env` exit 0; `ls …/drc-d1/.env` → `No such file or directory`. **.env: removed, proven gone (F5).**
- Commits: `d684f80b fix(drc): K2 fix r1 F-1 — the resolve-key query no longer shadows the validated positions in record_stated_book (L75, 09-25)`; `<tip>` = `4626a1f2 test(drc): K2 fix r1 RUNS — a no-trade day with a stated opening beside a recorded prior (L70)` (01:54 ET).

## F6 LIVE-NOTE
- On `4626a1f2`, F1's command byte for byte (exit 0): `142 passed, 1 skipped, 15 warnings in 9.78s` → `<lp>` = 142, `<lf>` = 0; 0 errors. The one SKIPPED: `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (the known one, as F1); no SKIPPED line names `COBALT_LIVE_VAULT_ROOT`. Identical to F1.

## F7 OFFLINE
- `ls /Users/cobalt/cobalt-wt/drc-d1/.env` → `No such file or directory`.
- On `4626a1f2`, F1's command byte for byte (exit 0): `2467 passed, 458 skipped, 1 xfailed, 15 warnings in 68.14s (0:01:08)` → `<p>` = 2467, `<f>` = 0; 0 errors.
- Counted from the tool results: `<p>` = `<bp>` 2463 + F2's 4 new offline tests (`test_drc_k2_fix_r1.py`; the renamed version test is not new) = 2467 ✓. Skipped = F1's 449 + F3's 8 + F5's 1 new with-DB tests = 458 ✓.

## F8 WITH-DB
- Deselects (`51`'s three, selecting four tests), each confirmed by `grep -n`: `test_tenancy.py::TestMigrationRoundTrip::test_twice_is_idempotent_and_the_rollback_round_trips` (`:697`), `test_tenancy.py::TestMigrationRoundTrip::test_the_proof_table_names_every_ruled_table` (`:710`), `test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default` (`:263`), `test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches` (`:306`). Classes at `test_tenancy.py:239` (`TestTenantGuc`) and `:688` (`TestMigrationRoundTrip`).
- LOCK (a) `ls -la …/*/.env` → `(eval):1: no matches found` · (b) `cp` exit 0; `ls -la …/*/.env` → one line, `…/drc-d1/.env` (01:56).
- (c) `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches` on `4626a1f2` (exit 0): `2915 passed, 6 skipped, 4 deselected, 1 xfailed, 15 warnings in 148.56s (0:02:28)` → `<dp>` = 2915, `<df>` = 0; 0 errors; deselected 4 as expected.
- Counted: `51`'s 2902 + F2's 4 + F3's 8 + F5's 1 = 2915 ✓.
- The six SKIPPED lines (none names Postgres): `test_cards_picks.py:383`, `:396` (S2-P2 dev-DB state), `test_radar_evaluate.py:691`, `test_catalyst.py:365`, `test_predicate.py:262` (`COBALT_LIVE_VAULT_ROOT not set` — the live-note leg is F6), `test_replay_line.py:256` (`COBALT_TEST_LIVE_DRC`). So `test_drc_store.py`, `test_drc_k1_store.py`, `test_drc_k1_experiments.py`, `test_drc_k2_store.py`, `test_drc_k2_experiments.py`, `test_drc_k2_fix_r1_store.py` and `test_drc_k2_fix_r1_runs.py` were NOT skipped.
- (c2) ABSENCE PROBE `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches` (exit 1): `1 failed in 5.64s`, `assert 28 == 32` at `test_migrate_proof.py:316`; the 28 named cursors listed contain NO `drc_imports`, `drc_fills`, `drc_rows` or `drc_stated_books` — SHORT BY EXACTLY 4, the known shape (`51`'s S9 (c2)). **0016 + 0018: rolled back — applied only inside the suite's transaction; absent on cobalt_dev (probe short by 4).**
- (d) `rm …/drc-d1/.env` exit 0; `ls …/drc-d1/.env` → `No such file or directory` (01:59). **.env: removed, proven gone (F8).**

## RESTARTS
`uv run cobalt jobs restarts 09ce3742..4626a1f2` (exit 0):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/drc/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/models.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/pairing.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/store.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/trading_log.md	M	DOCS	-
docs/40 - DevDocs/reports/drc-k2-build-2026-09-24.md	A	DOCS	-
src/cobalt/drc/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/drc/models.py	M	static import reach	com.cobalt.radar
src/cobalt/drc/pairing.py	M	static import reach	com.cobalt.radar
src/cobalt/drc/store.py	M	static import reach	com.cobalt.radar
src/cobalt/drc/trading_log.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_drc_k1.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_k1_store.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_k2.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_k2_experiments.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_k2_fix_r1.py	A	test/documentation; no resident	-
tests/cobalt/test_drc_k2_fix_r1_runs.py	A	test/documentation; no resident	-
tests/cobalt/test_drc_k2_fix_r1_store.py	A	test/documentation; no resident	-
tests/cobalt/test_drc_k2_store.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_store.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
As expected: the five `src/cobalt/drc/*` paths derive `com.cobalt.radar`; tests and docs derive nothing; 0 UNCLASSIFIED.

## SEAM FOR D2
This section supersedes `51`'s (L72). Signatures read from the tree at `4626a1f2`: `store.py:764` `DrcStore.seed_for(self, day: date) -> Optional[SeedBook]` · `store.py:281` `DrcStore.record_day(self, pairing: DayPairing, import_ids: dict[Kind, int], seed: Optional[SeedBook]) -> int` · `store.py:329` `DrcStore.rebuild(self, day: date) -> list[date]` · `store.py:351` `DrcStore.stated_difference(self, day: date) -> Optional[str]` · `store.py:1066` `DrcStore.record_stated_book(self, day, kind, positions, *, via, turn_id=None, readback_sha256=None, supersedes=None, expected_sha256=None, now=None) -> StatedBook` · `store.py:1044` `DrcStore.preview_stated_book(self, day, kind, positions, *, via, turn_id=None, readback_sha256=None, supersedes=None) -> StatedBook` · `store.py:371` `DrcStore.effect_day(self, day: date, supersedes: Optional[int]) -> date` · `pairing.py:483` `build_day(trading, stats=None, seed=None, resolves=())` · `pairing.py:286` `pair_day(...)` · `models.py:391` `SeedBook` · `models.py:139` `OpenPosition.opened_on: Optional[date]` · `models.py:269` `missing_of(outcome: Outcome, reason: str) -> list[str]` · `cli.py:190` `add_parser(sub) -> None`.

"`[F-17]` CONTRACT, as built by K1 at `9a0fc900`, amended by K1 fix r1 at `40cf173e`, by K2 at `09ce3742` and by K2 fix r1 at `4626a1f2`:
(1) Before pairing an import for day D, the route calls `DrcStore().seed_for(D)` → `Optional[SeedBook]` (`store.py:764`). It RAISES `PairingError` on a broken chain, an uncomputed prior, a STALE prior (a day left unrepaired behind a not-computed root: `<P> is stale — <root> was re-recorded with pairing not computed …`, `store.py:937`), a pre-lane prior (`rebuild <P>`), a hash mismatch, two current opening books, two current resolves for one trade id (naming both ids — a guard: the writer no longer stores a second one, `store.py:1097`), a resolve naming a trade no book held, and a resolve dated before D still held (`rebuild <R>`). Each is a loud FAILED on the page, never caught into a flat book. A stated opening beside a recorded prior is not a raise: the close wins (R51) and the book carries `stated_book_id` + `stated_differs`. [K2; K2 fix r1 F-2]
(2) `None` means no book is stated. The route calls `build_day(trading, stats, seed=None)` → `not computed — opening book not stated`, and RECORDS that day: `record_day(pairing, import_ids, None)` — one `day` row carrying `not_computed.pairing`, NO `seed`, NO `book_close`. It shows `state your opening book for <D>` (K3's form; until K3, the `cobalt drc state-book` CLI, R52). After he states it, `DrcStore().rebuild(D)` pairs D from the statement, re-pairs every later recorded day, and re-matches each re-paired day's stored stats rows (F-4, `store.py:511-540`). [H3, fix r1; K2; K2 fix r1 F-4]
(3) Otherwise `build_day(trading, stats, seed=book.positions, resolves=book.resolves)`, then `DrcStore().record_day(pairing, import_ids, book)` — `seed` is REQUIRED for a computed day, and `book` is the `SeedBook` `seed_for` returned. When a LATER day is already recorded, `record_day` re-pairs every later recorded day in the SAME transaction (`[F-03]`, R51): a later day that fails → `PairingError` naming it and NOTHING in `drc_rows` is written (the file stays stored, `[F-25]`); a chain stopped at a not-computed day → recorded, the later days named in the `day` row's `derived.not_repaired`, AND each later day's OWN `day` row carries `derived.book_stale = {root, reason}` (`store.py:623`, `:651`) until a re-pair reaches it; `seed_for` of the day after any stale day FAILS naming the root. The re-paired days are the `day` row's `derived.repaired`. [K2; K2 fix r1 F-2]
(4) Every statement from any caller goes through `DrcStore().record_stated_book(day, kind, positions, via=…, now=…)` (refused inside `market_reset`, `[F-01]`; an `opening` refused for D while D's prior trading day is recorded, H2). One current row per KEY: `opening` / `no_trade` — the day; `resolve` — the trade id, ON ANY DAY (`store.py:1097`); a restatement names the current row it replaces with `supersedes`, a resolve's on another day included. A statement's EFFECT is `DrcStore().rebuild(DrcStore().effect_day(day, supersedes))` (`store.py:371`) — the earlier of its day and the superseded row's day: a `no_trade` statement for D (the empty-day record, `[F-05]`), a `resolve` for a recorded day (`[F-06]`), an `opening` for a day recorded unpaired. The page calls it after the statement; the CLI does (`cobalt drc state-book … --apply`, AMENDED C7; `cli.py:151`, `:181`). The page passes `via="drc_page"`; the widget (K4) passes `via="voice_widget"` with `turn_id` + `readback_sha256`. [K2; K2 fix r1 F-1]
(5) `pair_day` is the FIFO engine and holds no book policy: a route never calls it directly.
(6) D3's `cobalt drc build` joins K1's `drc` parser group in `src/cobalt/drc/cli.py` (`cli.py:190`) — never a second `drc` group (L3).
(7) A stated position's `opened_on` is `None` (not stated); a page renders it `opened: not stated`, never a date. [H1, fix r1]
(8) For each day the page shows, `DrcStore().stated_difference(day)` (`store.py:351`) → the R51 line `stated book for <N> differed from <P>'s close: <trade_ids>`, or `None`. It is a read of stored rows; nothing is computed on the page. [K2]
(9) `DrcStore().rebuild(P)` is also the `rebuild <P>` remedy of a pre-lane day (v3 §4 row 4), and of a stale chain's root once its book is stated. [K2; K2 fix r1 F-2]"

## FOR K3
`51`'s `## FOR K3` stands, amended by:
- A day whose `day` row carries `derived.book_stale` (`{root, reason}`, written at `store.py:651`) is a day whose stored book is unknown: K3 renders its unit STALE naming the root (`<root> has pairing not computed — its open positions are unknown`), never as a continuing book; its date leaves the stale state only when a re-pair rewrites it (it is then in the root's `derived.repaired`, which K3 already re-upserts). [F-2]
- A resolve restated on another day: the rebuild runs from `effect_day` (`store.py:371`, the earlier day); `derived.repaired` of that day lists every date K3 re-upserts. [F-1]
- A re-paired day's `stats_row` rows are re-matched (F-4, `store.py:511-540`): K3 renders `stats_row.derived.match` as stored, never a cached match.
- `FN_VERSION` is `drc.pairing/4` (`pairing.py:90`).
- RUN-1 (GREEN, `test_drc_k2_fix_r1_runs.py`): a no-trade day with a stated opening beside a recorded prior stores `seed.inputs.source: carried` with `stated_book_id` (the statement link) and a non-empty `seed.derived.stated_differs`, and its `day` row names `no_trade_id`; `stated_difference` returns the R51 line. K3 renders such a day as carried-with-difference, not as `no_trade_carry`.

## CONTINUE
done — all steps complete; the report is committed at CLOSE.

## ESCALATE
1. R22 scope: read as the drc-d1 pair for this worktree (desk reading, R61 / R65 (1)).
2. LINE MOVED: `grep -n "PARTIAL — missing:" src/cobalt/drc/models.py` — expected 263, read 262.
3. PREFLIGHT grep: the prompt's `grep -n "absent = [c for c in PAIRING_INPUTS if c in detection.missing]"` carries `[` without `-F` and printed nothing (regex bracket); re-run with `grep -n -F` → `trading_log.py:170`. Not a stop.
4. F3: the first with-DB red run showed ONE named test (`test_every_later_day_of_a_stopped_chain…`) red on my own setup (a `_stated_rows` read placed before the chain's statement), not on `book_stale`. Corrected in the test (the L7 check moved inside `_stopped_chain` around D's record; nothing loosened) and re-run in the same lock take: red on `KeyError: 'book_stale'`. Both runs are quoted under F3.
5. F4/F5: my F-1 edit shadowed `record_stated_book`'s validated `rows` with its query result, so every statement stored `[]` positions; F4's offline proof could not see it (with-DB only). F5's with-DB REORDER-RULE check caught it (`22 failed, 110 passed`), corrected in `d684f80b` (a rename, `found`), re-proven `132 passed`. `<fix>` is therefore TWO commits: `a51988c9` + `d684f80b`. The checker reads `git diff 09ce3742 d684f80b -- src` for the fix.
6. F5 RUN-1 SETUP READING: the prompt's order (state the opening and the no-trade DRC for D_NEXT, then record D) never re-pairs D_NEXT, because `_commit` re-pairs only later days that have a `day` row. The run therefore records D_NEXT first (`rebuild(D_NEXT) == [D_NEXT]`, a no-trade day from his stated book) and then D — R51's order as `test_drc_k2_store.py` `_r51_setup` shapes it. RUN-1 is GREEN on `4626a1f2`.
7. F5 ran one EXTRA with-DB command inside its own lock take (the F4 reorder-rule check over the six DRC with-DB files), beyond the prompt's one RUN command: the reorder rule needs a with-DB run after the edits, and none is named before F8. Same lock, same four moves.
8. F4 `_repair` (F-4) now RAISES `PairingError` when stored `stats_row` rows exist but the `day` row names no stats import (the prompt's text); before, such a day re-paired silently without the id. No test reaches it; no row the store writes can produce it (`record_day` stores stats rows only from a pairing that ran with a stats input — a caller passing stats without its import id could). Named for `03`.
9. **"The FIX rows moved on file evidence only (`52` `## Checked against the branch` rows 1–7 HOLD; rows 8–9 NOT REAL — the contract text is AMENDED C7, no code). The red: F2 offline on `d2abba17`, F3 with-DB on its successor, green on `a51988c9` + `d684f80b`. The seams move (F-1: seam (1), (4); F-2: seam (1), (3), (9); `## FOR K3`) — the desk decides whether K3's drafter waits for `03` (L72). The check is `03` (round 2 of ≤3; Opus 5.5 + Grok, with Sol from Sep 26th, 2026 6:47 AM), and its packet carries this report's executed output of all three suites and RUN-1 (L68). Astra's read of the K2 NEW BUILD is owed from its meter return (`52` ESCALATE 7, the desk's seat). X12 stays the desk's hub-run read. The deploy's L68 gate re-proves the three suites on the tree that ships."**

DRC K2 FIX R1 BUILT 4626a1f2 | on 09ce3742 | red d2abba17 | offline 2467/0 | with-DB 2915/0 | live-note 142/0 | .env: removed | 0018: rolled back | FIX: 5 | RUNS: 1 | ESCALATE: 9
