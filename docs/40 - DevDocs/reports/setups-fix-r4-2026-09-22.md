# SETUPS FIX R4 — 2026-09-22 (`72`, Opus 5.5, hub `setups-fix-r4-0922`, started 21:17:57 EDT from `date`)

## §0 Headline
(pending)

## L74
Recorded once: a system-reminder appended after this session's first tool result asked for a `Claude-Session: https://claude.ai/code/session_…` line in commit messages and PR bodies and named a file-send tool (`SendUserFile`). Data under L74 — not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (the branch's own precedent, `git show --stat 8da261a`).

## AUTHORIZATION
| check | command | result |
|---|---|---|
| check committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"SETUPS CHECK R2R3 DONE" -- ".../setups-check-r2r3-2026-09-22.md"` | `dbfe49f95dde048b791af53af58fa382c3ebb072` |
| classification committed | `… -S"SETUPS FIX R4 DRAFTED" -- ".../setups-fix-r4-draft-2026-09-22.md"` | `688bc1f0772862d53674bbf7ca0f7734ce584861` |
| R32 | `grep -n "^| R32 " cto-2026-09-22.md` | `:119` carries `claude-opus-5-5` |
| R41 | `grep -n "^| R41 " cto-2026-09-21.md` | `:52` quotes both `.env` strings and `"Approved"` |
| R23 | `grep -n "^| R23 " cto-2026-09-22.md` | `:128` carries `Bash(uv run python tests/fixtures/radar/_cut_setups_fixtures.py *)` and `"approved"` |
| launch row + NEW USE | `grep -n "72-setups-fix-r4.md" cto-2026-09-22.md cto-2026-09-23.md` | `cto-2026-09-22.md:35: | R118 | 21:16 ET | NEW USE for \`72-setups-fix-r4.md\`, his words: "Approved" …`; `cto-2026-09-23.md`: `No such file or directory` (recorded, not fatal) |
| launch row committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"72-setups-fix-r4.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | `1823e02128ab90e99732b367f9c9980cc0772f3d` |
| rule strings | `grep -c -F -e "<rule>" 33-setups-fix-r3.md`, one call per string, quotes included: 19 allow, 3 deny, the `--add-dir` triplet | every one `1`, except `"Bash(rm /Users/cobalt/cobalt-wt/setups-c1/.env)"` → `2`; all ≥1 — PASS |
| cutter string | `grep -c -F -e "\"Bash(uv run python tests/fixtures/radar/_cut_setups_fixtures.py *)\"" 12-setups-fixture-cut.md` | `1` — PASS |

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| date | `date` | 0 | `Tue Sep 22 21:17:57 EDT 2026` |
| BASE TIP filled | title line | — | `8da261a` (7-hex) — PASS |
| r3 stopped on its tip | `tail -n 3 ".../setups-fix-r3-2026-09-22.md"` | 0 | `SETUPS FIX R3 BUILT be44eb4 \| on 65c08a0 \| offline 2453/0 \| with-DB 569/3 \| …` — PASS |
| clean | `git status --porcelain` | 0 | (no output) — PASS |
| branch | `git status` | 0 | `On branch setups/seven-0921` / `nothing to commit, working tree clean` — PASS |
| tip | `git log --oneline -1` | 0 | `8da261a fix(setups): round 3 — report` — PASS (first launch) |
| 8da261a docs-only | `git show --stat 8da261a` | 0 | `.../reports/setups-fix-r3-2026-09-22.md \| 187 ++++…` / `1 file changed, 183 insertions(+), 4 deletions(-)` — PASS |
| `.env` | `ls -la /Users/cobalt/cobalt-wt/setups-c1/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/setups-c1/.env: No such file or directory` — PASS |
| same worktree | `ls -la ".../setups-fix-r4-2026-09-22.md"` | 1 | `No such file or directory` — PASS (first launch) |
| 12's raw bars | `ls -la …/tasks/bj70z1v0d.output` | 0 | `-rw-r--r--  1 cobalt  wheel  155216 Sep 22 15:34 …` — 155216 = 12's count — PASS |
| 12's raw membership | `ls -la …/tasks/bn9p3qf72.output` | 0 | `-rw-r--r--  1 cobalt  wheel  234 Sep 22 15:34 …` — 234 = 12's count — PASS |
| 12's daily CSV | `ls -la <production daily-cache CSV, 12 § CUT 3.1>` | 0 | `-rw-r--r--  1 cobalt  staff  95128 …` — 95128 = 12's count — PASS |
| proposal file | `ls …/docs/_inflight/setups-assumed-values-r3-2026-09-22.md` | 0 | present — PASS |
| restarts | `uv run cobalt jobs restarts 8da261a..HEAD` | 0 | `path	change	rule	restart` / `RESTARTS: none` (empty range) |

## BASELINE
- **OFFLINE** `uv run pytest -q tests/cobalt tests/taxonomy -p no:cacheprovider` (background, on the untouched `8da261a`; no file edited while it ran — the report file was created BEFORE launch): `2453 passed, 361 skipped, 1 xfailed, 15 warnings in 483.26s (0:08:03)` → **2453/0** = r3's CLOSE line, as expected.
- NO WITH-DB BASELINE (`cobalt_dev` broken, `68` owed).

## F1
The dials probe asserts WHY a note row was refused.

### T
RED-on-`8da261a`, two new tests in `tests/cobalt/test_setups_fix_r4.py` (`uv run pytest -q -p no:cacheprovider tests/cobalt/test_setups_fix_r4.py -k f1` → `1 failed, 1 passed in 0.19s`):
- `test_f1_a_malformed_probe_note_fails_the_probe_loudly` (RED): a `tunables:<slug>` unit whose extra row carries only `key` + `value` (no unit, scope, …) → must raise `VaultTaxonomyError` matching `invalid tunables rows`. Failing line VERBATIM: `E       Failed: DID NOT RAISE <class 'cobalt.taxonomy.vault_loader.VaultTaxonomyError'>` (`tests/cobalt/test_setups_fix_r4.py:33`).
- `test_f1_the_engine_key_refusal_still_reads_not_reachable` (GREEN guard): r3's `## DIALS` row `| rubberband | stop.buffer | assumed / engine only (global) |` → `_per_trade_accepted(...) is False`.

### C
`tests/cobalt/test_setups_fix_r3.py` `_per_trade_accepted` only (+ `import re` and one module constant under it): `except VaultTaxonomyError as e:` returns `False` only when `str(e)` matches `_ENGINE_KEY_REFUSAL`, else `raise`. The pattern is the fixed words of the refusal's raise site (no value):
- raise site `src/cobalt/taxonomy/loader.py:114` in **`merge_tunables`**: `raise TaxonomyConfigError(f"user tunable row(s) {collisions} shadow engine keys in " f"{TUNABLES_PATH.name}. A per-trade row in a strategy note may only " "ADD keys (scope per_trade(...)), never redefine an engine key — " …)`;
- re-raised as `VaultTaxonomyError` at `src/cobalt/taxonomy/vault_loader.py:601` in `_resolve_every_cfg` (`raise VaultTaxonomyError(f"{', '.join(notes)}: {e}") from e`), called from `load_vault_trade_defs` (`vault_loader.py:517`).
- pattern: `r"user tunable row\(s\) .* shadow engine keys in .*A per-trade row in a strategy note may only\s+ADD keys"` (`re.S`).
After C: `-k f1` → `2 passed in 0.17s`.

### A1
None. r3's F6 tests: `uv run pytest -q -s -p no:cacheprovider tests/cobalt/test_setups_fix_r3.py -k f6` → `2 passed, 17 deselected in 26.67s`; the `DIALS` lines re-printed and compared row for row with r3's `## DIALS` table: **IDENTICAL** — 79 rows, same order, same `reachable` cell (78 `assumed / engine only (<scope>)`, 1 `per_trade` = `hitchhiker | example_drive_then_range.range_duration_band`); no probe raised, so every r3 "not reachable" was the engine-key refusal. F6 (b)'s three lines re-printed unchanged (`formed_scans=71`, `4.8500` / `4.8500` / `4.6220`).

### SUITE
OFFLINE → `2455 passed, 361 skipped, 1 xfailed, 15 warnings in 485.05s (0:08:05)` → **2455/0** = 2453 + 2 new F1 tests.

### COMMIT
`2817896 fix(setups): round 4 — F1 the dials probe refuses only on the engine-key refusal, any other error fails loudly` — `git show --stat HEAD`: `.../reports/setups-fix-r4-2026-09-22.md | 101 +++…` · `tests/cobalt/test_setups_fix_r3.py | 17 +++-` · `tests/cobalt/test_setups_fix_r4.py | 42 +++…` · `3 files changed, 158 insertions(+), 2 deletions(-)`.

## F2
`A-24` → null in the gitignored proposal.

### C
Read the file; ONE Edit, on the `A-24` row's PROPOSED-value cell only (every other cell of the row, and rows `A-09`, `A-10`, `A-16`, untouched). Committed config untouched (`leg.min_size_atr` already `value: null`).
- Read back (`grep -n "A-24" docs/_inflight/setups-assumed-values-r3-2026-09-22.md`, row 10), the changed cell only, no value: `` `null` — `status: null` — reason: `no passage speaks to pullback size (check r2r3, unanimous)` (fix r4 F2) ``.
- `git status --porcelain` → (no output): no line for `docs/_inflight/…` — the file stays untracked and ignored. No commit (nothing tracked changed).
- NOT edited (row-only rule): the file's line 12 paragraph explaining the old A-24 value and its closing tally line `proposal: 4 proposed, 0 null` — now stale; ESCALATE (ii).

## F3
No real-day literal in the cut's committed test.

### T
RED-on-`8da261a`, in `tests/cobalt/test_setups_fix_r4.py`: `test_f3_every_iso_date_in_the_cut_is_a_synthetic_day`, parametrised over `test_setups_fixture_cut.py` and `_cut_setups_fixtures.py` (2 cases): every `\d{4}-\d{2}-\d{2}` literal ∈ `{2026-01-06, 2026-01-07, 2026-01-08}`. The message COUNTS outsiders and never prints them (L32). `-k f3` → `1 failed, 1 passed, 2 deselected in 0.11s`; failing lines VERBATIM: `E       AssertionError: test_setups_fixture_cut.py: 1 ISO date literal(s) outside the synthetic allowlist` / `E       assert 1 == 0` (`tests/cobalt/test_setups_fix_r4.py:66`). The cutter case was already GREEN.

### C
`tests/cobalt/test_setups_fixture_cut.py` module docstring only: `real day <real day>,` → `the real stored day (see` / `` the fixture-cut report of prompt `12`, `## FIND — rubberband`), `` — the synthetic day stays. **Deviation from the row's wording, named (ESCALATE (iii-a)):** the row's text `(see \`setups-fixture-cut-2026-09-22.md\`)` itself carries an ISO date (`2026-09-22`, the report's filename) — it would keep this row's own pin RED and fail the CLOSE `grep -rn "2026-09-" …` self-check. Safe default taken: the pin and the self-check win; the report is named by its prompt and section instead. For the same reason this module's own docstring names the check and drafter reports by prompt number, not by dated filename. After C: `-k f3` → `2 passed, 2 deselected in 0.07s`; `grep -rn "2026-09-" tests/cobalt/test_setups_fix_r4.py tests/cobalt/test_setups_fixture_cut.py` → (no output).

### A1
None.

### SUITE
OFFLINE → `2457 passed, 361 skipped, 1 xfailed, 15 warnings in 487.30s (0:08:07)` → **2457/0** = 2455 + 2 new F3 cases.

### COMMIT
(below)

## F4
(pending)

## F5
(pending)

## C3
(pending)

## PINS MOVED
(pending)

## CLOSE
(pending)

## WITH-DB OWED
(pending)

## NOTE FOR THE DESK
(pending)

## ESCALATE
(pending)

## CONTINUE
next: F3 (F1 committed `2817896`; F2 done, gitignored, no commit)

(run in progress — row 0 of 5, next under ## CONTINUE)
