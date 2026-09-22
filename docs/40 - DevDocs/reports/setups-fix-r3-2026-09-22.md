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
(below)

## CONTINUE
next: F1 COMMIT, then F2 (T already drafted and RED-run: `1 failed, 4 passed` — the accept test RED with `VaultTaxonomyError … has scope 'per_indicator(ema9)'`)

(run in progress — row 0 of 6, next under ## CONTINUE)
