# SETUPS FIX R3 — 2026-09-22

## §0 Headline
(in progress — resume of `e79c815` under R79)

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
(below)

## CONTINUE
next: F3 COMMIT, then F4 (draft in the job tmp dir) (T drafted in the job tmp dir; the base roles pin captured: `F3 roles on the committed day: 160 observations sha=0922dadc29013941a7a2512e038ba9310e4fb791bc3a5e53bdd17a4bf5dd6323`)

(run in progress — row 2 of 6, next under ## CONTINUE)
