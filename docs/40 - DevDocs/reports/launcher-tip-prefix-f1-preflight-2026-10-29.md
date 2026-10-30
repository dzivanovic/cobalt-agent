# launcher-tip-prefix F1 — PREFLIGHT 2026-10-29

Read-only. Branch `ops/launcher-tip-prefix` at `5babf712` (`git -C /Users/cobalt/cobalt rev-parse --short=8 ops/launcher-tip-prefix` → `5babf712`). Nothing was run but reads; no test was executed.

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt diff 57dce28b… HEAD -U0 -- <card>` | only additions at card `:28-30`: the `F1` row after `A2`, a blank line, the "F1 RUNS AFTER A2…" paragraph. Four columns (row · what · red first · files), as T1/A1/A2. `git status --short -- <card>` empty (committed) | OK |
| 2a | `git grep -n -E "tip: \|8 hex" ops/launcher-tip-prefix -- ops/desk/card-fill.sh` | `:5` `# "BUILT · job: <the card's JOB> · tip: <8 hex>" …`; `:71` BUILT `re.match(r"BUILT · … tip: ([0-9a-f]{8})(?=\s\|$)", last)`; `:74` SHADOW BUILT, same regex | OK |
| 2b | `git show ops/launcher-tip-prefix:tests/ops/test_card_fill.py`, `git grep -n` | `:105-117` parametrize + `def test_a_report_not_ending_in_a_full_built_line…` (`:117`); `:127` O1 test; `:164` `test_386_e1_…`; `:177-189` e2 parametrize, the `1a2b3c4d5` row at `:187`. On `main` the same row is at `:179` (`git grep -n … main`) | OK |
| 2c | the row's other claims, read in `card-fill.sh` | `tip = m.group(2)` is the only use of the tip; `[0-9a-f]*` adds no capture group, so group 2 stays the first 8. O1 stderr text matches the check's `## RUNS` O1 | OK |
| 3 | regex `([0-9a-f]{8})[0-9a-f]*(?=\s\|$)` traced against the cases | 8 hex + `9` + space: admitted, `TIP:` = first 8. `<tip>z`, `<tip>9z`: the lookahead fails at every backtrack, refused. 7 hex: refused. `1A2B3C4D`: refused (no `IGNORECASE`). Job match is `m.group(1) != job`, untouched. Both arms (`:71`, `:74`) named. Not looser than the ruling (8 hex, optional hex, whitespace or end) | OK |
| 4a | red-first named | O1 test red already (`check` `## RUNS` O1, `assert 1 == 0`); new `test_1085_f1_a_nine_hex_shadow_line_fills_the_eight_hex_tip` red by name, same failure; the flipped pin: `1a2b3c4d5` leaves the refused list, `1a2b3c4dz` takes its place, and the new fill test carries the new expectation (`"TIP: 1a2b3c4d" in …`) | OK |
| 4b | run command `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_card_fill.py -k "1085 or test_386_e or full_built_line"` | `-k` selects the O1 test, the new f1 test, e1/e2/e3 and the `…full_built_line…` test. `grep -n "uv run pytest" BUILD-HUB.md` BUILD line `:14` allows `Bash(uv run pytest *)`; `Edit(//Users/cobalt/cobalt-wt/**)`, `git add *`, `git commit *` are on it too | OK |
| 4c | banned commands | the row and its paragraph name `uv run python -c`, `bash -n`, `git mv`, `git rm`, `rm`, `mv` only as "no"; no `revert`, `cherry-pick` | OK |
| 5 | files column and RESTARTS | `ops/desk/card-fill.sh`, `tests/ops/test_card_fill.py` only; no guard or allow line; `git grep -c card-fill` on the branch in `desk-launch.sh`, `preflight.sh` → none. Header `RESTARTS: none` stays; the check's `## Suites` RESTARTS row classes `ops/desk/*.sh` as no reader | OK |
| 6 | closing proof | `FIXED: O1 — tests/ops/test_card_fill.py::test_1085_check_o1_a_nine_hex_built_line_fills_the_eight_hex_tip` named, same text as the check's `## OPEN` | OK |
| 7a | default: no DEPLOY PROOF marker for `card-fill.sh` | sound enough to launch on. `ls -l /Users/cobalt/.claude/ops/card-fill.sh` → symlink to `/Users/cobalt/cobalt/ops/desk/card-fill.sh`, so `install-ops` has nothing to link and the four existing markers stand. See NOTE N2 | OK |
| 7b | default: no `ORDER:` line | sound: `grep -n "ORDER:"` finds none on the card or in `CARD.md` as a required header; table order puts F1 last and the paragraph says it runs after A2 | OK |
| 8 | desk-owned headers | the card diff above touches no header line; `BASE: 4f1c991f`, `TIP: 2edcf295`, `CHECK REPORT: …launcher-tip-prefix-check-2026-10-29.md`, `HOUSE B: as needed`, `RULINGS: 2026-10-12 R1138` as before | OK |

## ISSUES
- NOTE N1: the row says the `1a2b3c4dz` e2 row and the two new `…full_built_line…` rows are "GREEN on that tip" as boundary controls. Those rows do not exist at `5babf712`; the builder adds them, then they are green before and after the code edit. The builder should quote them from the red run (written first, green at once), not look for them on the tip.
- NOTE N2: no marker means the deploy does not machine-check that `card-fill.sh` landed. One line (`grep -c -F "card 1085" /Users/cobalt/cobalt/ops/desk/card-fill.sh` · before `0` · after at least `1`) is cheap, and the row already requires the comments. The desk may add it; not a blocker.
- NOTE N3: the drafter's `:179`-on-`main` claim is true (`main:tests/ops/test_card_fill.py:179`); the check report's own `:179` refers to `main`, F1's `:187` to the branch. Both are right.
- Blocks the launch: nothing.

PREFLIGHT DONE · cards: 1085-F1 · checks: 12 · fails: 0 · ready: YES
