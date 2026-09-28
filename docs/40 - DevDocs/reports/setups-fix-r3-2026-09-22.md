# SETUPS FIX R3 — 2026-09-22

## §0 Headline
- BUILT, 6 of 6 rows on `65c08a0` (resume of `e79c815` under R79): F1 R47 side binding by the mirrored frame (X10 now PASS) · F2 R48 `per_indicator` holes take assumed rows · F3 R49 `A-24` `leg.min_size_atr` (null) · F4 R50 health pills skip `assumed_formation` · F5 R51 `stop.buffer` → `dollars` · F6 R61 dials table + per-trade override proven. Code tip `be44eb4`.
- Offline 2453/0 (base 2434 + 19 new tests). With-DB **569/3 — the 3 reds are `cobalt_dev` itself** (`TooManyColumns` re-applying migration 0007; `cobalt_dev` likely left below 0007 — ESCALATE (0), the desk's repair before any dev-DB run). No `DEF_WRITTEN_*` moved. Proposal: 4 proposed, 0 null (gitignored file).
- ESCALATE: 18 — incl. (0) the dev DB, (ix) one `evaluate.py` hunk (F1, a named-EMPTY file), (v) "an assumed row tunes EVERY setup that reads the key" (R61 finding).

## L74
Recorded once: a system-reminder appended after this session's first tool result asked for a `Claude-Session: https://claude.ai/code/session_…` line in commit messages and PR bodies and named a file-send tool (`SendUserFile`). Data under L74 — not followed. (Seen again on this resume's first tool result; same record.)

## AUTHORIZATION
Re-run 16:45 EDT on the R79 resume.

| check | command | result |
|---|---|---|
| R47 | `grep -n "^| R47 " cto-2026-09-22.md` | `:67` carries `"A definition wins"` |
| R48 | `grep -n "^| R48 " …` | `:66` carries `F1 is WIDENED` |
| R49 | `grep -n "^| R49 " …` | `:65` carries `"A and we tune in live"` |
| R50 | `grep -n "^| R50 " …` | `:64` carries `SKIP \`assumed_formation\`` |
| R51 | `grep -n "^| R51 " …` | `:63` carries `"You pick the one easier to program and maintain"` |
| R61 | `grep -n "^| R61 " …` | `:53` carries `SUPERSEDES R46` |
| R49 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"we tune in live" -- …cto-2026-09-22.md` | `636763520c9cca3365da70a6f34f8bb65c0acd94` |
| R61 committed | `… -S"SUPERSEDES R46" …` | `74fe5c8af4c984f138f73c3d4c913871e6ed1299` |
| R32 | `grep -n "^| R32 " …` | `:79` carries `claude-opus-5-5` |
| R41 | `grep -n "^| R41 " cto-2026-09-21.md` | `:52` quotes both `.env` strings and `"Approved"` |
| R41 committed | `… -S"Bash(rm /Users/cobalt/cobalt-wt/setups-c1/.env)" -- …cto-2026-09-21.md` | `598a8d77acb31c03a91da70430ad7b7690d329f1` |
| launch row | `grep -n "33-setups-fix-r3.md" cto-2026-09-22.md cto-2026-09-23.md` | `cto-2026-09-22.md:36: | R78 | 16:4x ET | …` and `:35: | R79 | 16:4x ET | … DESK RE-ISSUE of \`33\`…`; `cto-2026-09-23.md`: `No such file or directory` (recorded, not fatal) |
| launch row committed | `… -S"33-setups-fix-r3.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | `9c58e794dc8f24cd90d3e429bda435d7fed5ac73` |
| rule strings | `grep -c -F -e "<the whole span: 19 allow strings, --disallowedTools, 3 deny strings, 3 --add-dir>" 15-setups-fix.md` — the entire contiguous span as ONE fixed string (stronger than 25 separate greps: every string present, in order, byte for byte) | `1` (first run: 25 separate greps, each ≥1) |

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| date | `date` | 0 | `Tue Sep 22 16:45:28 EDT 2026` |
| BASE TIP filled | title line | — | `65c08a0` (7-hex) |
| 12 stopped on that tip | `tail -n 3 ".../setups-fixture-cut-2026-09-22.md"` | 0 | `SETUPS FIXTURE CUT BUILT 65c08a0 \| on 74eefd8 \| … \| ESCALATE: 7` — PASS |
| clean | `git status --porcelain` (via long form) | 0 | `nothing to commit, working tree clean` — PASS |
| branch | `git status` | 0 | `On branch setups/seven-0921` — PASS |
| tip (resume) | `git log --oneline 65c08a0..HEAD` | 0 | `e79c815 wip(setups-fix-r3): F0 partial …` / `a09c6da docs(report): setups fixture cut …` — PASS (R79: `a09c6da` = base; `e79c815` = this hub's own wip; resume) |
| a09c6da docs-only | `git show --stat a09c6da` | 0 | `.../reports/setups-fixture-cut-2026-09-22.md \| 194 +++…` / `1 file changed, 194 insertions(+)` — PASS |
| `.env` | `ls -la /Users/cobalt/cobalt-wt/setups-c1/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/setups-c1/.env: No such file or directory` — PASS |
| stagger | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — PASS |
| same worktree | report file | — | present = this hub's own resume (R79) |
| companion | `ls …/setups-assumed-values-2026-09-21.md` | 0 | present |
| references | `ls "/Users/cobalt/cobalt/docs/90 - References"` | 0 | cited: `back$ide_cheat_sheet.pdf`, `the_fashionably_late_scalp_cheat_sheet.pdf`, `VWAP Continuation.pdf`, `9 EMA.pdf`, `hitchhiker_scalp_cheat_sheet.pdf`, `the_second_chance_scalp_cheat_sheet.pdf` (as rows need them) |
| `_inflight` | `ls /Users/cobalt/cobalt-wt/setups-c1/docs/_inflight` | 0 | `README.md` (first run) — the folder exists; the Write lands in it |
| restarts | `uv run cobalt jobs restarts 65c08a0..HEAD` | 0 | `…setups-fix-r3-2026-09-22.md	A	DOCS	-` / `…setups-fixture-cut-2026-09-22.md	A	DOCS	-` / `RESTARTS: none` |

## BASELINE
- **OFFLINE** `uv run pytest -q tests/cobalt tests/taxonomy -p no:cacheprovider` (background, started 16:46 on the base tree): `1 failed, 2433 passed, 361 skipped, 1 xfailed, 15 warnings in 457.95s (0:07:37)`. The one failure: `tests/cobalt/test_setups_nine_ema.py::test_x26_an_assumed_argument_on_the_atom_is_a_validation_error_and_detail_passes_none - IndexError: list index out of range` — the test reads `inspect.getsource(evaluate.evaluate_member)` at run time, and I began F1's edit of `evaluate.py` while the suite was still running (a process slip, named under ESCALATE), so the source lines no longer matched the loaded function. Re-run alone on the edited tree: `1 passed, 13 deselected in 0.07s`. **Base count used for comparison: 2434 passed / 0 failed, 361 skipped, 1 xfailed.**
- **WITH-DB**, run on the F1-edited tree (NOT the pristine base — the slip above; named under ESCALATE): `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/setups-c1/.env` → the BASELINE command + `tests/cobalt/test_setups_fix_r2.py` (as r2's CLOSE ran it; `12`'s added test file `test_setups_fixture_cut.py` holds no DB test — `grep` finds no DB marker; not added) → `1 failed, 552 passed, 1 skipped in 1853.62s (0:30:53)`. The one failure: `test_setups_d4.py` X10 pin, `AssertionError: assert 'PASS' == 'FAIL'` — the module was collected before its A1 re-point (F1, by design). The skip: `SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof` (by design). The stored-session X7/X18 experiment is in this set and PASSED with F1 in place (`both_sides == 0` for every shape). → `rm /Users/cobalt/cobalt-wt/setups-c1/.env` → `ls -la …/.env` → `ls: /Users/cobalt/cobalt-wt/setups-c1/.env: No such file or directory`. **Comparison count: 553 / 0** (r2's line `553 passed, 1 skipped`, same set).

## F1
R47 — `backside` / `fashionably-late` bind side through the mirrored frame (Grok's fix).

### T
RED-on-`65c08a0`. X10 FIRST on the base code (`uv run pytest -q -s -p no:cacheprovider tests/cobalt/test_setups_d4.py -k "x10"`): `X10: FAIL evaluation=not_evaluable direction=None long=not_evaluable/Extension path B only — catalyst unknown in S2 (R4) short=not_formed/None` · `2 passed, 21 deselected in 0.19s` (NOT AS EXPECTED on the base, as the build recorded).
New in `tests/cobalt/test_setups_fix_r3.py` (4): backside past the open forms LONG · the mirrored construction forms SHORT · fashionably-late past the open forms LONG (its `A-09`/`A-10` holes = the corpus's constructed fills `D4_CONSTRUCTED`, L69) · `binds_side_by_frame` is True for exactly the two defs (rubberband + the four with-trend shapes False). Run on the base code: `4 failed in 0.32s` — the RED lines:
- `AssertionError: ('not_evaluable', 'Extension path B only — catalyst unknown in S2 (R4)', …)` (backside, and fashionably-late)
- `AssertionError: ('not_formed', None, {'long': SideOutcome(evaluation='not_f...` (mirrored)
- `ImportError: cannot import name 'binds_side_by_frame' from 'cobalt.radar.anatomy.frame'`

### C
| file | change |
|---|---|
| `src/cobalt/radar/anatomy/extension.py` | `detect_extension(..., *, direction=None)`: None = today (run's sign); a given direction reads that Extension whatever the run's sign, path B only for a distance moved that way |
| `src/cobalt/radar/anatomy/frame.py` | `PAST_CULMINATION`, `BOUND_EXTENSION_DIRECTION = "down"`, `binds_side_by_frame(td)`; `build_frame(..., bind_side=False)`; `Frame.observed` (the detector's own Extension) |
| `src/cobalt/radar/evaluate.py` | 3 hunks: `_build_frames(..., bind_side=False)` passes it through; `evaluate_member` passes `binds_side_by_frame(td)` and reads the seam/factor observations from `frames["long"].observed` — **ESCALATE: a file the CLOSE list names EMPTY, and `31`'s stacked file (L68)** |

After C: `uv run pytest -q -s --color=no -p no:cacheprovider tests/cobalt/test_setups_fix_r3.py` → `F1 backside past the open: evaluation=formed direction=long long=formed/None short=not_formed/None` · `F1 backside mirrored: evaluation=formed direction=short` · `F1 fashionably-late past the open: evaluation=formed direction=long long=formed/None short=not_formed/None` · `4 passed in 0.46s`.
GREEN guards after C (`… test_setups_x5.py test_rubberband_forms.py test_setups_d4.py test_setups_lego.py test_setups_registries.py`): `1 failed, 92 passed, 6 skipped in 272.34s` — the one failure is the X10 pin (A1 below): `AssertionError: assert 'PASS' == 'FAIL'`. X10 after C: `X10: PASS evaluation=formed direction=long long=formed/None short=not_formed/None`. X5: `X5 offline: defs=9 frames=2 members=50 runs_s=[5.44, 5.37, 5.4] p95~max=5.44s budget=100.0s` (budget 100 s). `test_rubberband_forms.py` all green, unchanged in text. X7 re-run: `X7 backside: scans=392 formed=0 both_sides=0` · `X7 fashionably-late: scans=392 formed=0 both_sides=0`.
Stated plainly: X5's number and the rubberband pins were NOT quoted BEFORE C on this run (I edited before running the guards); the before-evidence is the offline BASELINE (both files green on the base tree) and r2's last X5 line, `X5 offline: defs=9 frames=2 members=50 runs_s=[5.15, 5.09, 5.1] p95~max=5.15s budget=100.0s`.

### A1
| test | old | new | row |
|---|---|---|---|
| `test_setups_d4.py::test_x10_…` (`X10_RESULT`) | `"FAIL"` | `"PASS"` (same assertion `result == X10_RESULT`) | F1 by design |
| `test_setups_lego.py` `AWAITING_A_RULING` | backside, fashionably-late (X10) | UNCHANGED set; comment re-pointed to the run's own printed outcome: neither forms on any committed scan (X7 lines above) — they STAY, announced (reason now: lifecycle holes `A-08`/`A-11` null at committed config; fashionably-late also its `per_indicator` holes) | F1 |
No `DEF_WRITTEN_*` moved; no assertion removed or loosened; no skip / xfail. `test_setups_d4.py` is outside the CLOSE path list → ESCALATE.

### D
Appended one paragraph each: `radar/anatomy/extension.md`, `radar/anatomy/frame.md`, `radar/evaluate.md`.

### SUITE
`uv run pytest -q tests/cobalt tests/taxonomy -p no:cacheprovider --color=no` → `2438 passed, 361 skipped, 1 xfailed, 15 warnings in 470.94s (0:07:50)` → **2438/0** = 2434 + the 4 new F1 tests; skipped unchanged. With-DB not re-run per row: `test_setups_d4.py` / `test_setups_lego.py` hold no DB-backed test (`grep -c -e "requires_db" -e "cobalt_dev" -e "POSTGRES" -e "dev_db"` → `0` each), and the with-DB BASELINE above already ran on the F1 source.

### COMMIT
`c4f5fd7 fix(setups): round 3 — F1 backside / fashionably-late bind side through the mirrored frame (R47)` — `git show --stat HEAD`: 10 files, `254 insertions(+), 53 deletions(-)`: the three DevDocs, this report, `extension.py`, `frame.py`, `evaluate.py`, `test_setups_d4.py`, `test_setups_fix_r3.py` (new), `test_setups_lego.py`.

## F2
R48 — the assumed-rows reader accepts a `per_indicator` HOLE.

### T
RED-on-`65c08a0` (vault_loader unchanged since the base). New (5 tests: 1 + a 3-case parametrised refusal + 1): a `tmp_path` vault's `Assumed Defaults.md` carries a `per_indicator(ema9)` row for `flat_threshold.ema9` (this file's literal = the build's constructed fill, not a companion value — L69) → loaded, merged over the null engine row, and the fashionably-late card formed on it (F1's constructed series) carries `assumed_formation` naming the key; three refusal cases (non-hole key, mismatched `<ind>`, no engine row); `source: sheet` refused. Run before C: `1 failed, 4 passed, 4 deselected in 0.16s`; RED line: `cobalt.taxonomy.vault_loader.VaultTaxonomyError: 1 - Trading/Assumed Defaults.md (tunables:assumed): tunable 'flat_threshold.ema9' has scope 'per_indicator(ema9)'. The reader accepts \`global\` or \`per_trade(<a def loaded in this pass>)\` only (a per_indicator hole is not fillable here as the design words it).` (The refusal pins were already green — refused by the old blanket rule; after C they are refused by the new named reasons.)

### C
`src/cobalt/taxonomy/vault_loader.py` only (`load_assumed_tunables` + its docstring, "F1: not widened" → R48's). `loader.py` untouched (the merge's same-scope hole-fill already serves it); the closure untouched (`flat_threshold.ema9` / `.vwap` / `dist.k.vwap` are `cfg()` tokens of the defs, already in it). `configs/` not touched. After C: `F2: assumed_keys=('anatomy.orientation.extension', 'flat_threshold.ema9', 'frame.warmup_source', 'vwap.anchor')`; refusals now read e.g. `tunable 'flat_threshold.ema9' has scope 'per_indicator(vwap)', but its engine row's scope is 'per_indicator(ema9)'. A per_indicator row fills ONLY an engine hole (\`value: null\`) of that same per_indicator scope (R48).`

### A1
| test | old | new | row |
|---|---|---|---|
| `test_assumed_store.py::test_the_reader_refuses_a_row_outside_its_contract[row0-per_indicator]` | a `per_indicator(ema9)` row for `flat_threshold.ema9` is refused (`match="per_indicator"`) | a `per_indicator(vwap)` row for `flat_threshold.ema9` is refused (`match="per_indicator"`, same strength) — the old case is now ACCEPTED by design and pinned in `test_setups_fix_r3.py` | F2 |
Red before the re-point: `Failed: DID NOT RAISE <class 'cobalt.taxonomy.vault_loader.VaultTaxonomyError'>`. After: `67 passed, 3 skipped` over `test_assumed_store.py test_setups_d1.py test_setups_vwap_cont.py test_setups_fix_r3.py`. `test_assumed_store.py` is outside the CLOSE path list → ESCALATE.

### PROPOSAL
Written ONCE to `docs/_inflight/setups-assumed-values-r3-2026-09-22.md`; `git status --porcelain` after the Write listed no line for it (ignored). Details under `## PROPOSAL`.

### D
`taxonomy/vault_loader.md` + one paragraph; `ADDING-A-SETUP.md` § Where its dials go: the assumed-default line now says a `per_indicator(<ind>)` hole takes an assumed row of that same scope (R48).

### SUITE
OFFLINE → `2443 passed, 361 skipped, 1 xfailed, 15 warnings in 470.10s (0:07:50)` → **2443/0** = 2438 + 5 new F2 tests. `test_assumed_store.py` is a with-DB file (it holds `requires_db` tests), so the row ran it inside the `.env` pair: `cp …` → `COBALT_ENV=dev uv run pytest -q -p no:cacheprovider -rs --color=no tests/cobalt/test_assumed_store.py tests/cobalt/test_setups_fix_r3.py` → `31 passed in 1.87s` → `rm …/.env` → `ls -la …/.env` → `ls: /Users/cobalt/cobalt-wt/setups-c1/.env: No such file or directory`.

### COMMIT
`3194038 fix(setups): round 3 — F2 the assumed-rows reader accepts a per_indicator hole (R48)` — `git show --stat HEAD`: 6 files, `147 insertions(+), 12 deletions(-)`: `ADDING-A-SETUP.md`, `taxonomy/vault_loader.md`, this report, `vault_loader.py`, `test_assumed_store.py`, `test_setups_fix_r3.py`.

## F3
R49 — the minimum-size rule for `impulse` / `pullback` legs, `A-24` = `leg.min_size_atr`, `value: null`.

Key number: `grep -c "A-24"` on the companion → `0`, on the FINAL → `0` → `A-24` is the next free. Key name: `grep -rn "min_size"` over `configs src tests` and the FINAL → no output (no collision).

### T
RED-on-`65c08a0` for the change (4), GREEN-as-pin for the null guard (1). New (5): a small last pullback is not a `pullback`, the large earlier one is (with this file's literal minimum between them, L69) · an impulse below the minimum is not an `impulse` (`before` / `before_role` None — `Leg(opening_drive OR impulse)` no longer holds) · on the nine-ema definition-written day the key null forms and a minimum above its pullback removes the pullback atom and the formation · the whole-day null pin (every role, both frames, FTFT and BGFI, every 10 min — 160 observations; the sha was computed on the pre-F3 code, `leg_roles.py` byte-identical to the base, and copied from that run's failure: `F3 roles on the committed day: 160 observations sha=0922dadc29013941a7a2512e038ba9310e4fb791bc3a5e53bdd17a4bf5dd6323`) · the key is a null engine row in the closure of exactly the defs naming the roles, and `assumed_closure` carries it when assumed. Run before C: `4 failed, 1 passed, 9 deselected in 0.88s`; RED lines: `TypeError: pullback_roles() got an unexpected keyword argument 'min_size'` (×2) · `KeyError: 'leg.min_size_atr'` (×2).

### C
| file | change |
|---|---|
| `configs/cobalt/taxonomy/tunables.yaml` | ONE row: `leg.min_size_atr`, `value: null`, unit `atr`, scope `global`, `dynamic: true`, `status: proposed`, `source: dwv` (as the other null engine rows) |
| `src/cobalt/radar/anatomy/leg_roles.py` | `MIN_SIZE_KEY`, `ROLE_TUNABLE_KEYS`, `min_size(rows)`; `pullback_roles(..., *, min_size=None, atr=None)`; `PullbackRoles.unavailable` |
| `src/cobalt/radar/anatomy/frame.py` | the `pullback_roles` object passes the key's value and the seeded ATR; a role atom reads `unavailable` when the roles are |
| `src/cobalt/radar/formation/atoms.py` (the closure) | the five role atoms declare `ROLE_TUNABLE_KEYS`; `_ROLE_REASONS` + `insufficient_seed` |
`leg.py` (`legs()`) untouched: `git diff configs src/cobalt/radar/anatomy/leg.py` shows only the config row. After C: `F3 nine-ema day, leg.min_size_atr=None: pullback atom=symbol/down evaluation=formed` · `F3 nine-ema day, leg.min_size_atr=1.5: pullback atom=null/None evaluation=not_formed` · `F3 roles on the committed day: 160 observations sha=0922dadc29013941a7a2512e038ba9310e4fb791bc3a5e53bdd17a4bf5dd6323` (unchanged) · `F3 defs naming Leg(impulse) / Leg(pullback): ['nine-ema-scalp', 'vwap-continuation']` · `5 passed`. (The printed `1.5` is this test file's own constructed literal, not a proposal.)

### A1
The first full offline run after C: `5 failed, 2443 passed, 361 skipped, 1 xfailed` — all five are the card-digest pins, which map `tunables_sha256` back to the start digest by EXCLUDING each row committed config gained (the build's standing A1 shape): `test_setups_registries.py::test_lego_ii_every_card_spec_is_byte_identical_through_the_registries[countertrend|mixed]`, `test_setups_d1.py::test_f11_the_dots_and_card_score_do_not_move[countertrend|mixed]`, `test_rubberband_forms.py::test_t6_a_def_that_formed_before_changes_only_in_the_finals_named_ways` (it imports `test_setups_registries._tunables_digests`), e.g. `AssertionError: assert 'b5f387c348f8...8503ab86dcd58' == '7a0e5796e33e...1f8811573450a'`.
| test | old | new | row |
|---|---|---|---|
| `test_setups_registries.py` `STEP3_KEYS` | the 17 rows the build + r2 added | + `leg.min_size_atr` (same exclusion, same strength; every pinned sha UNCHANGED in text) | F3 |
| `test_setups_d1.py` `ADDED_KEYS` | the same 17 | + `leg.min_size_atr` | F3 |
`test_rubberband_forms.py` unchanged in text (it reads the registries helper). No `DEF_WRITTEN_*` moved. After: `85 passed, 6 skipped in 194.47s` over those three files; with-DB (both are with-DB files): `cp …` → `COBALT_ENV=dev uv run pytest -q -p no:cacheprovider -rs --color=no tests/cobalt/test_rubberband_forms.py tests/cobalt/test_setups_d1.py tests/cobalt/test_setups_registries.py tests/cobalt/test_setups_fix_r3.py tests/cobalt/test_radar_cards_db.py tests/cobalt/test_radar_evaluate.py` → `144 passed, 1 skipped in 205.79s (0:03:25)` (the by-design live-note skip) → `rm` → `ls: /Users/cobalt/cobalt-wt/setups-c1/.env: No such file or directory`. `test_setups_registries.py` / `test_setups_d1.py` are outside the CLOSE path list → ESCALATE.

### PROPOSAL
`A-24`'s proposal is in the gitignored file (written with F2's; see `## PROPOSAL`).

### D
`radar/anatomy/leg_roles.md`, `radar/anatomy/frame.md`, `radar/formation/atoms.md` + one paragraph each; `ADDING-A-SETUP.md` § Where its dials go + one line naming the key and that it is his to tune (L53).

### SUITE
OFFLINE → `2448 passed, 361 skipped, 1 xfailed, 15 warnings in 472.11s (0:07:52)` → **2448/0** = 2443 + 5 new F3 tests. With-DB for the touched with-DB files: above (A1).

### COMMIT
`b737c25 fix(setups): round 3 — F3 minimum-size rule for impulse / pullback legs, A-24 leg.min_size_atr null (R49)` — `git show --stat HEAD`: 12 files, `243 insertions(+), 18 deletions(-)`: `tunables.yaml`, `ADDING-A-SETUP.md`, `frame.md`, `leg_roles.md`, `atoms.md`, this report, `frame.py`, `leg_roles.py`, `atoms.py`, `test_setups_d1.py`, `test_setups_fix_r3.py`, `test_setups_registries.py`.

## F4
R50 — a FILLED card's health pills skip `assumed_formation`.

### T
RED-on-`65c08a0`. New (2): `dot_pills` over two graded dots + the `assumed_formation` dot → exactly the two graded pills, no "assumed_formation has no graded value" note; `card_health` → the dot class is the graded dot only, and `assumed_keys_of(dots)` still reads the dot (it stays on the card). Run before C: `2 failed, 14 deselected in 0.08s`; printed `F4 pills: [('factor_a', 'ok'), ('factor_b', 'ok'), ('assumed_formation', 'n/a')]`; RED lines: `AssertionError: assert ['factor_a', ...ed_formation'] == ['factor_a', 'factor_b']` · `AssertionError: assert ['factor_a', ...ed_formation'] == ['factor_a']`.

### C
`src/cobalt/cards/health.py` only: `dot_pills` skips `dot.factor == ASSUMED_FORMATION` (one comment naming R50). After C: `F4 pills: [('factor_a', 'ok'), ('factor_b', 'ok')]`. Guards (the build's tests, untouched): `… test_setups_fix_r3.py test_card_health.py test_radar_panel_cards.py test_setups_d1.py -k "f4 or health or pill or filled"` → `29 passed, 60 deselected in 49.87s` (`X14: filled-card refreshes=138 non-health numbers moved=False health moved=True`).

### A1
None.

### D
`cards/health.md` + one paragraph.

### SUITE
OFFLINE → `2450 passed, 361 skipped, 1 xfailed, 15 warnings in 472.73s (0:07:52)` → **2450/0** = 2448 + 2 new F4 tests. No with-DB file touched.

### COMMIT
`e7a2090 fix(setups): round 3 — F4 a FILLED card's health pills skip assumed_formation (R50)` — `git show --stat HEAD`: 4 files, `80 insertions(+), 2 deletions(-)`: `cards/health.md`, this report, `health.py`, `test_setups_fix_r3.py`.

## F5
R51 — `stop.buffer`'s unit label `cents` → `dollars`; value unchanged; no behaviour change.

### T
RED-on-`65c08a0`. New (1): the loaded `stop.buffer` row's unit is `TunableUnit.DOLLARS` and its value equals the committed file's (read from the YAML, never typed — L69). Run before C: `1 failed, 16 deselected in 0.13s`; RED line: `AttributeError: type object 'TunableUnit' has no attribute 'DOLLARS'`.
THE ARITHMETIC PROOF (no new pin): `grep -n "raw = extreme + away \* buffer" src/cobalt/radar/anatomy/structure.py` → before C `104:    raw = extreme + away * buffer`, after C `104:    raw = extreme + away * buffer`; `git diff 65c08a0 -- src/cobalt/radar/anatomy/structure.py src/cobalt/radar/formation/stops.py` → no output. The existing stop pins, unchanged in text, GREEN after C (`-rA`): `PASSED tests/cobalt/test_setups_registries.py::test_x4_the_ten_cent_grid_and_the_stop_sweep_on_negated_extremes` · `nine-ema-scalp on the committed day: formed_scans=1 first=('long', '2026-01-06T15:36:00+00:00', '4.7930', '4.64')` · `vwap-continuation on the committed day: formed_scans=2 ticker=BGFI first=('long', '2026-01-06T20:04:00+00:00', '24.8120', '24.75')` · `second-chance on the committed day: formed_scans=55 ticker=FTFT first=('long', '2026-01-06T16:22:00+00:00', '5.3000', '5.21')` · the three definition-written path tests + hitchhiker's → `8 passed, 81 deselected in 42.63s`; `test_rubberband_forms.py` whole green (its `DEF_WRITTEN_*` stop prices) in the A1 run below.

### C
`src/cobalt/taxonomy/tunables.py`: `TunableUnit.DOLLARS = "dollars"` with one comment naming R51. `configs/cobalt/taxonomy/tunables.yaml`: the one `unit:` line of `stop.buffer`. The def-side `buffer: {type: fixed, cents: …}` spec key is NOT renamed (L45 — ESCALATE (iii)).

### A1
First full offline run after C: `5 failed, 2446 passed, 361 skipped, 1 xfailed` — the same five card-digest pins as F3 (the relabel moves `tunables_sha256` by construction).
| test | old | new | row |
|---|---|---|---|
| `test_setups_registries.py` `_tunables_digests` | the start digest = committed rows minus the added keys | … and `stop.buffer`'s `unit` mapped back to `cents` (the label only; every pinned sha UNCHANGED in text) | F5 |
| `test_setups_d1.py` `_tunables_digests` | same | same mapping | F5 |
After: `102 passed, 6 skipped in 198.16s` over `test_rubberband_forms.py test_setups_d1.py test_setups_registries.py test_setups_fix_r3.py`; with-DB: `cp …` → `COBALT_ENV=dev uv run pytest -q -p no:cacheprovider -rs --color=no tests/cobalt/test_rubberband_forms.py tests/cobalt/test_setups_d1.py tests/cobalt/test_setups_registries.py tests/cobalt/test_setups_fix_r3.py tests/cobalt/test_radar_cards_db.py tests/cobalt/test_radar_evaluate.py tests/cobalt/test_taxonomy_store.py` → `162 passed, 1 skipped in 209.64s (0:03:29)` (the by-design live-note skip) → `rm` → `ls: /Users/cobalt/cobalt-wt/setups-c1/.env: No such file or directory`.

### D
`taxonomy/tunables.md` + one paragraph. ROLLBACK NOTE: `ADDING-A-SETUP.md` § Rolling back after the assumed note + one line — the code rollback and the `unit: dollars` line revert TOGETHER; `src/cobalt/taxonomy/store.py` stores only the vault's user rows (`INSERT INTO tunables (key, row, slug, loaded_at)` over `result.user_tunables`), and `stop.buffer` is an engine row, so the DB holds no copy to re-sync.

### SUITE
OFFLINE → `2451 passed, 361 skipped, 1 xfailed, 15 warnings in 476.25s (0:07:56)` → **2451/0** = 2450 + 1 new F5 test.

### COMMIT
`953e22b fix(setups): round 3 — F5 stop.buffer unit label cents to dollars, value unchanged (R51)` — `git show --stat HEAD`: 8 files, `68 insertions(+), 5 deletions(-)`: `tunables.yaml`, `ADDING-A-SETUP.md`, `taxonomy/tunables.md`, this report, `tunables.py`, `test_setups_d1.py`, `test_setups_fix_r3.py`, `test_setups_registries.py`.

## F6
R61 — the dials per setup, and one per-trade override proven to reach the evaluator. No source change.

### T
Both GREEN-as-pin (no code change is this row's). (a) a report generator: per setup of `SHAPES` (the seven) + `example-lego-eighth`, every key of `closure_keys(def)` ∪ the note's own rows, and per key whether a `tunables:<slug>` row for it is ACCEPTED by `load_vault_trade_defs` (a probe note written into a `tmp_path` vault per key) — KEYS ONLY. Printed table → `## DIALS` verbatim. It would turn red if a per-trade row began to shadow an engine key, or a setup gained a per-trade dial unannounced. `UNPROVEN` keys: none. (b) the reversal shape (`rubberband-without-htf-avoid`) with its trigger's `bars_cleared` written as `cfg(<trade_key>.bars_cleared)` and a `tunables:<slug>` row — at the value the neutral shape writes as a literal, and overridden by this file's literal — over every 2-minute scan of the committed FTFT day, VERBATIM:
- `F6 (b) literal note: formed_scans=71 first=[('2026-01-06T16:24:00+00:00', 'short', '4.8500', 2)]`
- `F6 (b) per-trade dial at 2: formed_scans=71 first=[('2026-01-06T16:24:00+00:00', 'short', '4.8500', 2)]`
- `F6 (b) per-trade dial overridden to 5: formed_scans=71 first=[('2026-01-06T16:24:00+00:00', 'short', '4.6220', 5)]`
The override REACHES the evaluator (trigger price and `bars_cleared` change; the same scans form). Also run once on the F1 tree before F2–F5 (same lines). `2 passed, 17 deselected in 26.42s`. It would turn red if the per-trade path stopped reaching the trigger. No `ASK DESK` needed.

### C
None (tests and the doc only).

### A1
None.

### D
`ADDING-A-SETUP.md` § Where its dials go + one paragraph: tuning is the noise tool (R61), per_trade in the note's unit (only the note's own `cfg(<trade_key>.…)` keys — a note row for an engine key is refused), engine keys through `Assumed Defaults` rows, changed by the desk on his word (L65), loaded by `cobalt taxonomy load`. (`wc -l` → 104, under the Lego (v) cap of 120.)

### SUITE
OFFLINE → `2453 passed, 361 skipped, 1 xfailed, 15 warnings in 503.62s (0:08:23)` → **2453/0** = 2451 + 2 new F6 tests.

### COMMIT
`be44eb4 fix(setups): round 3 — F6 the dials per setup and a per-trade override proven to reach the evaluator (R61)` — `git show --stat HEAD`: 3 files, `130 insertions(+), 1 deletion(-)`: `ADDING-A-SETUP.md`, this report, `test_setups_fix_r3.py`.

## PROPOSAL
File: `docs/_inflight/setups-assumed-values-r3-2026-09-22.md` (gitignored; `git status --porcelain` never listed it). Every cited passage was re-read on its PDF page with the Read tool and found word for word. No value, no quote here (L32).

| key | companion row | PDF, page | status |
|---|---|---|---|
| `flat_threshold.ema9` (`per_indicator(ema9)`) | A-09 | `the_fashionably_late_scalp_cheat_sheet.pdf` p.2 | proposed (NO SOURCE NUMBER, LOW — as the companion) |
| `flat_threshold.vwap` (`per_indicator(vwap)`) | A-10 | `the_fashionably_late_scalp_cheat_sheet.pdf` p.1 | proposed (NO SOURCE NUMBER, LOW) |
| `dist.k.vwap` (`per_indicator(vwap)`) | A-16 | `VWAP Continuation.pdf` p.1 | proposed (NO SOURCE NUMBER, LOW) |
| `leg.min_size_atr` (`global`) | A-24 (new) | `VWAP Continuation.pdf` p.1 · `9 EMA.pdf` p.1 | proposed (NO SOURCE NUMBER, LOW; the passages speak to the with-trend move only — ESCALATE) |

proposal: 4 proposed, 0 null

## DIALS
F6 (a)'s printed table, VERBATIM (`DIALS setup | key | reachable`; KEYS only). `per_trade` = a `tunables:<slug>` row for it is accepted for that def; `assumed / engine only (<scope>)` = the loader refuses a note row for it (an engine key), so it is reached only through an `Assumed Defaults` row (a hole) or the engine row. Read once after F3 (so `leg.min_size_atr` appears).

| setup | key | reachable |
|---|---|---|
| rubberband | anatomy.orientation.extension | assumed / engine only (global) |
| rubberband | extension.backside_hh_min | assumed / engine only (global) |
| rubberband | extension.backside_hl_min | assumed / engine only (global) |
| rubberband | extension.path_a_volume_ma_bars | assumed / engine only (global) |
| rubberband | extension.path_a_volume_sigma | assumed / engine only (global) |
| rubberband | extension.path_b_atr | assumed / engine only (global) |
| rubberband | extension.snapback_bars_cleared | assumed / engine only (global) |
| rubberband | range.wick_ratio_max | assumed / engine only (global) |
| rubberband | slope_norm.bars | assumed / engine only (global) |
| rubberband | stop.buffer | assumed / engine only (global) |
| hitchhiker | dayrange.session | assumed / engine only (global) |
| hitchhiker | example_drive_then_range.range_duration_band | per_trade |
| hitchhiker | frame.warmup_source | assumed / engine only (global) |
| hitchhiker | leg.consolidation_max_retrace | assumed / engine only (global) |
| hitchhiker | range.micro.bound_flat_slope_atr | assumed / engine only (global) |
| hitchhiker | range.micro.touch_tolerance_atr | assumed / engine only (global) |
| hitchhiker | range.micro.touches_per_side | assumed / engine only (global) |
| hitchhiker | range.wick_ratio_max | assumed / engine only (global) |
| hitchhiker | stop.buffer | assumed / engine only (global) |
| backside | anatomy.orientation.extension | assumed / engine only (global) |
| backside | extension.backside_hh_min | assumed / engine only (global) |
| backside | extension.backside_hl_min | assumed / engine only (global) |
| backside | extension.path_a_volume_ma_bars | assumed / engine only (global) |
| backside | extension.path_a_volume_sigma | assumed / engine only (global) |
| backside | extension.path_b_atr | assumed / engine only (global) |
| backside | extension.snapback_bars_cleared | assumed / engine only (global) |
| backside | frame.warmup_source | assumed / engine only (global) |
| backside | range.micro.bound_flat_slope_atr | assumed / engine only (global) |
| backside | range.micro.touch_tolerance_atr | assumed / engine only (global) |
| backside | range.micro.touches_per_side | assumed / engine only (global) |
| backside | slope_norm.bars | assumed / engine only (global) |
| backside | stop.buffer | assumed / engine only (global) |
| fashionably-late | anatomy.orientation.extension | assumed / engine only (global) |
| fashionably-late | extension.backside_hh_min | assumed / engine only (global) |
| fashionably-late | extension.backside_hl_min | assumed / engine only (global) |
| fashionably-late | extension.path_a_volume_ma_bars | assumed / engine only (global) |
| fashionably-late | extension.path_a_volume_sigma | assumed / engine only (global) |
| fashionably-late | extension.path_b_atr | assumed / engine only (global) |
| fashionably-late | extension.snapback_bars_cleared | assumed / engine only (global) |
| fashionably-late | flat_threshold.ema9 | assumed / engine only (per_indicator(ema9)) |
| fashionably-late | flat_threshold.vwap | assumed / engine only (per_indicator(vwap)) |
| fashionably-late | frame.warmup_source | assumed / engine only (global) |
| fashionably-late | slope_norm.bars | assumed / engine only (global) |
| fashionably-late | vwap.anchor | assumed / engine only (global) |
| nine-ema-scalp | catalyst_ref.resolver | assumed / engine only (global) |
| nine-ema-scalp | extension.on_leg.form | assumed / engine only (global) |
| nine-ema-scalp | extension.path_a_volume_ma_bars | assumed / engine only (global) |
| nine-ema-scalp | extension.path_a_volume_sigma | assumed / engine only (global) |
| nine-ema-scalp | extension.path_b_atr | assumed / engine only (global) |
| nine-ema-scalp | frame.warmup_source | assumed / engine only (global) |
| nine-ema-scalp | leg.min_size_atr | assumed / engine only (global) |
| nine-ema-scalp | leg.pre_test | assumed / engine only (global) |
| nine-ema-scalp | stop.buffer | assumed / engine only (global) |
| vwap-continuation | dist.k.vwap | assumed / engine only (per_indicator(vwap)) |
| vwap-continuation | frame.warmup_source | assumed / engine only (global) |
| vwap-continuation | leg.min_size_atr | assumed / engine only (global) |
| vwap-continuation | level.rejected.rule | assumed / engine only (global) |
| vwap-continuation | levels.set | assumed / engine only (global) |
| vwap-continuation | pivot.n | assumed / engine only (global) |
| vwap-continuation | range.micro.bound_flat_slope_atr | assumed / engine only (global) |
| vwap-continuation | range.micro.touch_tolerance_atr | assumed / engine only (global) |
| vwap-continuation | range.micro.touches_per_side | assumed / engine only (global) |
| vwap-continuation | stop.buffer | assumed / engine only (global) |
| vwap-continuation | trendline.min_pivots | assumed / engine only (global) |
| second-chance | event.stop_hit.source | assumed / engine only (global) |
| second-chance | extension.on_leg.form | assumed / engine only (global) |
| second-chance | frame.warmup_source | assumed / engine only (global) |
| second-chance | leg.pre_test | assumed / engine only (global) |
| second-chance | levels.set | assumed / engine only (global) |
| second-chance | range_break.failed_trap_bars | assumed / engine only (global) |
| second-chance | range_break.retest_tolerance_atr | assumed / engine only (global) |
| second-chance | range_prior.rule | assumed / engine only (global) |
| second-chance | stop.buffer | assumed / engine only (global) |
| second-chance | turn_candle.rule | assumed / engine only (global) |
| example-lego-eighth | frame.warmup_source | assumed / engine only (global) |
| example-lego-eighth | range.micro.bound_flat_slope_atr | assumed / engine only (global) |
| example-lego-eighth | range.micro.touch_tolerance_atr | assumed / engine only (global) |
| example-lego-eighth | range.micro.touches_per_side | assumed / engine only (global) |
| example-lego-eighth | stop.buffer | assumed / engine only (global) |

UNPROVEN: none. Not in the table by construction: (1) the literal numbers written in a def's own text (e.g. a trigger's `bars_cleared`, a stop's `fraction`) — tuned by editing the note, or turned into a per-trade dial by writing `cfg(<trade_key>.<field>)` there (F6 (b) proves that path); (2) the three `extension.path_*` keys every def reads through the stage's seam observations but only an Extension-anchored def DECLARES (X22's standing finding, `test_setups_lego.ALWAYS_READ_UNDECLARED`). `stop.buffer` has a per-trade override convention in its own docstring (`<trade_id>.stop.buffer`) — as a separately NAMED key, not a row for `stop.buffer` itself.

## CLOSE
- **OFFLINE** `uv run pytest -q tests/cobalt tests/taxonomy -p no:cacheprovider --color=no` on `be44eb4` → `2453 passed, 361 skipped, 1 xfailed, 15 warnings in 500.73s (0:08:20)` → **2453/0**. Counted: base 2434 + 19 new tests in `test_setups_fix_r3.py` (F1 4 · F2 5, of which one parametrised function = 3 cases · F3 5 · F4 2 · F5 1 · F6 2); skipped unchanged at 361 (the new module holds no with-DB test).
- **WITH-DB** `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/setups-c1/.env` → the BASELINE command + `tests/cobalt/test_setups_fix_r3.py` (`--color=no`) → **`3 failed, 569 passed, 1 skipped in 1905.69s (0:31:45)`** → `rm /Users/cobalt/cobalt-wt/setups-c1/.env` → `ls -la …/.env` → `ls: /Users/cobalt/cobalt-wt/setups-c1/.env: No such file or directory`. The skip: `SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof` (by design). **The three reds are the `cobalt_dev` DATABASE, not this round's code** — ESCALATE (0):
  - `tests/cobalt/test_radar_score_migration.py::test_card_checks_index_and_receipt_immutability_on_cobalt_dev` — `psycopg.errors.TooManyColumns: tables can have at most 1600 columns` at `_apply(conn, [SYSTEM_SQL, USER_SQL])` (`:498`), re-applying `0007_radar_cards.sql`;
  - `tests/cobalt/test_tenancy.py::TestMigrationRoundTrip::test_twice_is_idempotent_and_the_rollback_round_trips` and `::test_the_proof_table_names_every_ruled_table` — `cobalt db migrate` subprocess: `-- applying 0007_radar_cards.sql` / `FAILED: TooManyColumns: tables can have at most 1600 columns`.
  - Why not this round: `git diff 65c08a0 -- src/cobalt/db_migrations` → no output; `0007_radar_cards.sql` ADDs 25 columns to `"user".aset_sizings` (`ADD COLUMN IF NOT EXISTS` ×25, `:32-56`) and its rollback DROPs them (`:40-64`); PostgreSQL keeps a dropped column counted toward the 1600-attribute limit until the table is rewritten, and `TestMigrationRoundTrip` COMMITS a full rollback + re-migrate on `cobalt_dev` every with-DB run (its docstring: "`db migrate` commits"). The same three tests PASSED in this session's with-DB BASELINE ~2 h earlier (`1 failed, 552 passed` — the one red being the X10 pin). Every other with-DB test of the set, including all of this round's, passed.
- `git diff --stat 65c08a0` → 26 files, `1138 insertions(+), 56 deletions(-)`: `configs/cobalt/taxonomy/tunables.yaml`; DevDocs `cards/health.md`, `radar/ADDING-A-SETUP.md`, `radar/anatomy/extension.md`, `frame.md`, `leg_roles.md`, `radar/evaluate.md`, `radar/formation/atoms.md`, `taxonomy/tunables.md`, `taxonomy/vault_loader.md`; reports `setups-fix-r3-2026-09-22.md`, `setups-fixture-cut-2026-09-22.md` (`12`'s `a09c6da`, part of the base per R79); `src/cobalt/cards/health.py`, `radar/anatomy/extension.py`, `frame.py`, `leg_roles.py`, `radar/evaluate.py`, `radar/formation/atoms.py`, `taxonomy/tunables.py`, `taxonomy/vault_loader.py`; tests `test_assumed_store.py`, `test_setups_d1.py`, `test_setups_d4.py`, `test_setups_fix_r3.py`, `test_setups_lego.py`, `test_setups_registries.py`. Paths outside the prompt's list → ESCALATE (ix), (x).
- EMPTY checks, each its own call: `git diff 65c08a0 -- src/cobalt/db_migrations` → no output · `git diff 65c08a0 -- src/cobalt/radar/anatomy/structure.py src/cobalt/radar/formation/stops.py` → no output · `git diff 65c08a0 -- tests/fixtures` → no output · `git diff --stat 65c08a0 -- src/cobalt/cards/store.py src/cobalt/cards/scoring.py src/cobalt/radar/evaluate.py` → `src/cobalt/radar/evaluate.py | 16 ++++++++++------` / `1 file changed, 10 insertions(+), 6 deletions(-)` (NOT empty — ESCALATE (ix)); `store.py` / `scoring.py` untouched · `git diff 65c08a0 -- tests/cobalt/test_rubberband_forms.py tests/cobalt/test_setups_nine_ema.py tests/cobalt/test_setups_vwap_cont.py tests/cobalt/test_setups_second_chance.py` → no output.
- `git diff 65c08a0 -- configs` → exactly two hunks: `-    unit: cents` / `+    unit: dollars` (the `stop.buffer` row, value `0.02` unchanged), and the new `leg.min_size_atr` row (`value: null`, `unit: atr`, `scope: global`, `dynamic: true`, `status: proposed`, `source: dwv`, one consumer line, two comment lines).
- **L32 self-check:** `git status --porcelain` never listed `docs/_inflight/…` (ignored; never staged). Each proposal value grepped (`grep -rn -F "<value>" tests/cobalt/test_setups_fix_r3.py configs/cobalt/taxonomy/tunables.yaml "docs/40 - DevDocs/cobalt/radar/ADDING-A-SETUP.md"`, one call each, value withheld here): proposal value 1 (A-09 / A-10's): 2 hits — `test_setups_fix_r3.py:204`, `:207`, my own constructed leg-width comments (unrelated) · proposal value 2 (A-16's): 1 hit — `tunables.yaml:176`, the pre-existing ruled row `gap_retrace_pct_max` (unchanged since the base; unrelated) · proposal value 3 (A-24's): 2 hits — `test_setups_fix_r3.py:205`, `:208`, substrings of my own constructed leg prices (unrelated). No fix needed.
- `uv run cobalt jobs restarts 65c08a0..HEAD` → VERBATIM:
```
path	change	rule	restart
configs/cobalt/taxonomy/tunables.yaml	M	resident reads	com.cobalt.aset,com.cobalt.radar
docs/40 - DevDocs/cobalt/cards/health.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/ADDING-A-SETUP.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/anatomy/extension.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/anatomy/frame.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/anatomy/leg_roles.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/evaluate.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/formation/atoms.md	M	DOCS	-
docs/40 - DevDocs/cobalt/taxonomy/tunables.md	M	DOCS	-
docs/40 - DevDocs/cobalt/taxonomy/vault_loader.md	M	DOCS	-
docs/40 - DevDocs/reports/setups-fix-r3-2026-09-22.md	A	DOCS	-
docs/40 - DevDocs/reports/setups-fixture-cut-2026-09-22.md	A	DOCS	-
src/cobalt/cards/health.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/anatomy/extension.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/anatomy/frame.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/anatomy/leg_roles.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/evaluate.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/formation/atoms.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/taxonomy/tunables.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/taxonomy/vault_loader.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_assumed_store.py	M	test/documentation; no resident	-
tests/cobalt/test_setups_d1.py	M	test/documentation; no resident	-
tests/cobalt/test_setups_d4.py	M	test/documentation; no resident	-
tests/cobalt/test_setups_fix_r3.py	A	test/documentation; no resident	-
tests/cobalt/test_setups_lego.py	M	test/documentation; no resident	-
tests/cobalt/test_setups_registries.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
(taken before the report's last edits; the report commit adds only a DOCS path). No `UNCLASSIFIED`.
- `git log --oneline 65c08a0..HEAD` (before the report commit): `be44eb4` F6 · `953e22b` F5 · `e7a2090` F4 · `b737c25` F3 · `3194038` F2 · `c4f5fd7` F1 · `e79c815` (this hub's first-run wip, docs only) · `a09c6da` (`12`'s report, docs only — base per R79).
- **L68:**

| branch | shared path | commits |
|---|---|---|
| `cards/stale-score-0922` | — | not cut (`fatal: ambiguous argument 'cards/stale-score-0922': unknown revision`) |
| `radar/handicap-h1-0922` | none | (no output) |
| `bars/chunk-2-0920` | `configs/cobalt/taxonomy/tunables.yaml` | `c941d30`, `c798a0a` |
| `bars/chunk-1a-0920` | `configs/cobalt/taxonomy/tunables.yaml` | `c597bfe` |
| `bars/chunk-e-0920` | none | (no output) |

## NOTE FOR THE DESK
"`prompts/2026-09-22/16-setups-check-r2.md` checks round 2 on `60ddac4..<r2 tip>` and reads `setups-fix-r2-2026-09-22.md`'s last line; it must be RE-POINTED (L19, a full re-issue) to check round 2 AND round 3 together or round 3 alone — its PREFLIGHT `tail` path and `| on 60ddac4 |` gate, its `60ddac4..<tip>` ranges, its boundary path list (`15`'s CLOSE list → this round's), its packet (3) fix report, and its FIX-row question set (F1–F5 + P1 → this round's F1–F6, plus the r2 ESCALATE (viii) stop-resolver question and the proposal file `docs/_inflight/setups-assumed-values-r3-2026-09-22.md` for R48's 'read by the check') — the desk's call. `31`'s TIP is filled from THIS round's report commit if the stale-score build stacks after it. Pins this round moved (F1 only): none → re-derived blind by `23` (committed day) / `13` (cut days)."

Round 3's code tip: `be44eb4` (the report commit sits above it). Base: `65c08a0` (with `12`'s docs-only `a09c6da` and this hub's first-run wip `e79c815` above it, R79). Note for `16`: the range `65c08a0..be44eb4` also lists `a09c6da` and `e79c815` — both docs-only.

## ESCALATE
(0) **`cobalt_dev` is broken for the whole dev-DB lane — FIRST, the desk's action.** The CLOSE with-DB run's three reds are `TooManyColumns: tables can have at most 1600 columns` on re-applying `0007_radar_cards.sql` (details under `## CLOSE`). `"user".aset_sizings` in `cobalt_dev` has accumulated dropped columns from committed 0007 rollback / re-apply round trips (`TestMigrationRoundTrip`, every with-DB run of every hub). Worse: that test's sequence is `--rollback --down-to 0001` then `migrate`, and the `migrate` failed at 0007 — so `cobalt_dev` is most likely LEFT BELOW 0007 now (0001–0006 re-applied, 0007 + later absent). INFERRED from the test's own code and output, NOT read directly (L70: `cobalt db` is not mine to run). Any hub's with-DB run on `cobalt_dev` will fail until it is repaired: a table rewrite of `"user".aset_sizings` (e.g. `VACUUM FULL` or a dump / restore of `cobalt_dev`), then `cobalt db migrate` on `cobalt_dev`, then this round's with-DB set again. Not production: no prod DB was touched. The same three tests passed ~2 h earlier in this session.
(i) **The proposal** (`docs/_inflight/setups-assumed-values-r3-2026-09-22.md`, gitignored): `flat_threshold.ema9` (A-09) proposed · `flat_threshold.vwap` (A-10) proposed · `dist.k.vwap` (A-16) proposed · `leg.min_size_atr` (A-24) proposed. Null: none. All four are NO SOURCE NUMBER, LOW (a word only). A-24's passages speak only to the with-trend move ("strong"); NO passage in the two sheets of the defs naming the roles speaks to how big a PULLBACK must be — the check / desk may prefer to leave A-24 null until he tunes it live (R49).
(ii) The desk writes the proposed rows into his `1 - Trading/Assumed Defaults.md` ONLY after the check reads them (R48, L65, FINAL §8). Until then committed config keeps all four null and nothing changes in production.
(iii) F5: the rollback line (`ADDING-A-SETUP.md` § Rolling back — code and the `unit: dollars` line revert together; the DB holds no copy of the engine row). The def-side `buffer: {type: fixed, cents: …}` spec key (`StopBuffer.cents`, `predicate.UNITS`) is LEFT as his notes' shape (L45); `TunableUnit.CENTS` stays for it. The spec key now names a unit the value is not in — a naming residue for him, not a behaviour.
(iv) A1 re-points (none moved a `DEF_WRITTEN_*`; no blind seat owed): F1 `test_setups_d4.py` `X10_RESULT` `"FAIL"` → `"PASS"`; F1 `test_setups_lego.py` `AWAITING_A_RULING` comment only (set unchanged); F2 `test_assumed_store.py` refusal case `per_indicator(ema9)` → `per_indicator(vwap)`; F3 `test_setups_registries.py` `STEP3_KEYS` / `test_setups_d1.py` `ADDED_KEYS` + `leg.min_size_atr`; F5 the same two `_tunables_digests` map `stop.buffer`'s unit back to `cents` for the start digest. Every pinned sha unchanged in text.
(v) F6: `## DIALS` above; (b) the per-trade override REACHES the evaluator (the trigger moves, same 71 formed scans). UNPROVEN keys: none. **FINDING for R61 (not a defect, no code): per-setup tuning of an ENGINE dial is not possible today.** A note row for an engine key is refused (`merge_tunables`: a note only ADDS keys), and an `Assumed Defaults` row is global (or per_indicator) — it tunes EVERY setup that reads the key (e.g. `stop.buffer`, `frame.warmup_source`, `range.micro.*` sit in 4–8 setups' tables). Only the def's own `cfg(<trade_key>.…)` keys are per-setup; today the corpus has one (hitchhiker's duration band). If "tune the setups so the noise subsides" means per setup, the lever is to write the number into the def as its own `cfg(<trade_key>.…)` (F6 (b)'s path) — the desk's / his call.
(vi) The r2 ESCALATE (viii) stop-resolver question (stop resolvers not given `tunable_keys`) — carried for `16`, NOT built (not his ruling).
(vii) `ASK DESK`: none raised; no safe default taken beyond the rows as written.
(viii) `MEMORY:` / `RULING:` lines: none.
(ix) **`src/cobalt/radar/evaluate.py` changed (F1)** — a file the CLOSE list names EMPTY and `31`'s stacked file (L68). Three hunks: `_build_frames(..., bind_side=False)` passes the flag through; `evaluate_member` passes `binds_side_by_frame(td)` and reads the seam / factor observations from `frames["long"].observed`. Why needed: `build_frame` has no def, and the side binding is per def (Grok's fix binds only the two defs whose text names a state past the culmination; Rubberband must keep the detector's direction, FINAL fact 3). For every other def `observed is extension`, so no published row changes (the full offline + with-DB suites and every card-digest pin agree).
(x) **Test files changed outside the CLOSE path list**, each an A1 of its row: `tests/cobalt/test_setups_d4.py` (F1), `tests/cobalt/test_assumed_store.py` (F2), `tests/cobalt/test_setups_registries.py` and `tests/cobalt/test_setups_d1.py` (F3, F5). Also `src/cobalt/radar/anatomy/extension.py` / `frame.py` (F1's side-binding files) and `src/cobalt/radar/formation/atoms.py` (F3's closure) — named by the rows, listed here for the boundary check.
(xi) **F1's reading, named for the checkers:** a def binds side through the frame when a precondition compares the unqualified `Extension.state` to a state past the culmination (`reverting` / `backside`, taken from the atom's own domain, so no setup word in source — Lego (i) green). For such a def BOTH frames read the DOWN Extension in frame coordinates (`detect_extension(..., direction="down")`; path B then counts only a distance moved down). The formation's `leg_count` / anchor come from that bound Extension; the seam observations stay the detector's own. The stored-session X7 (in the with-DB set) shows `both_sides == 0` for every shape with F1 in place. X10: PASS.
(xii) **backside and fashionably-late STAY in `AWAITING_A_RULING`, announced** (F1's A1 rule): X10 is closed, but neither forms on any committed scan (`X7 backside: scans=392 formed=0 both_sides=0`, `X7 fashionably-late: scans=392 formed=0 both_sides=0`), and at committed config their lifecycle holes (`A-08`, `A-11`) and fashionably-late's `per_indicator` holes are null. Their blocker is now holes + a day, not a ruling — moving them to `AWAITING_A_DAY` (and a fixture-cut day for them) is the desk's call.
(xiii) **Process slips, stated plainly (L35):** (a) I began F1's source edits while the offline BASELINE was still running; one test that reads `inspect.getsource(evaluate.evaluate_member)` failed on the line drift (`IndexError`), passing alone afterwards — the baseline is recorded as 2434/0 with that reasoning; (b) the with-DB BASELINE therefore ran on the F1-edited tree, not the pristine base (`1 failed, 552 passed, 1 skipped` — the one red was the X10 pin collected before its re-point); (c) X5's number and the rubberband pins were not quoted BEFORE F1's C on this run (the before-evidence is the offline baseline and r2's X5 line); (d) while waiting on the long suites I re-ran `test_setups_lego.py` / `test_setups_d4.py` (and, before F3 / F6, `test_setups_fix_r3.py -k probe` / `-k f6`) as timers — all green each time; some of those runs overlapped a with-DB run while `.env` was in the worktree, which is harmless only because none of those modules holds a DB-backed test (`grep -c -e "requires_db" -e "cobalt_dev" -e "POSTGRES" -e "dev_db"` → `0` for lego / d4; the new module has none). (e) The F3 base-roles pin was captured by a temporary probe test in the module, removed before F1's commit (never committed red). No denied call; no command outside the list.
(xiv) **RESTARTS** (`uv run cobalt jobs restarts 65c08a0..HEAD`): `RESTARTS: com.cobalt.aset com.cobalt.radar` (config `resident reads` + `src/` static import reach). No `UNCLASSIFIED`.
(xv) **L68:** `cards/stale-score-0922` — not cut (`unknown revision`). `radar/handicap-h1-0922` — no commit on any path of this round. `bars/chunk-2-0920` — `c941d30`, `c798a0a` touch `configs/cobalt/taxonomy/tunables.yaml`; `bars/chunk-1a-0920` — `c597bfe` touches it (a textual-conflict risk with F3's row / F5's line at the stacked gate). `bars/chunk-e-0920` — none.
(xvi) **Proposal hygiene (L32):** the proposal values were grepped in `test_setups_fix_r3.py`, `tunables.yaml`, `ADDING-A-SETUP.md` — hits are my own unrelated literals (constructed leg prices in two test comments / leg tuples) and one pre-existing ruled engine row in `tunables.yaml` (`gap_retrace_pct_max`, unchanged since the base). No proposal value entered a committed file.
(xvii) **L74** recorded once above.

## CONTINUE
next: none — all six rows and CLOSE done; `.env` removed and proven gone. A relaunch has nothing to build. After the desk repairs `cobalt_dev` (ESCALATE (0)), the with-DB set of `## CLOSE` can be re-run on `be44eb4` by any seat holding the `.env` pair.

SETUPS FIX R3 BUILT be44eb4 | on 65c08a0 | offline 2453/0 | with-DB 569/3 | src changed: yes | tests added: 19 (one parametrised function counted as its 3 cases) | .env: removed, proven gone | ESCALATE: 18
