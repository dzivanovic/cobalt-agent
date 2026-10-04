# Card 06 cobalt-guard-b — preflight (read-only)

CARD: `prompts/2026-10-04/06-cobalt-guard-b-card.md`. Run 2026-10-04, read-only, no git write.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 979ec797 main` | exit 0, no output | OK |
| 1b | `git -C /Users/cobalt/cobalt log --oneline -1 979ec797` | `979ec797 Merge branch 'main' into deploy/set3b-1004` (set 3b) | OK |
| 1c | `git -C /Users/cobalt/cobalt merge-base --is-ancestor a2e19ceb 979ec797` | exit 0, no output | OK |
| 2a | `git -C /Users/cobalt/cobalt rev-parse --verify ops/cobalt-guard-b-1004` | `fatal: Needed a single revision` (exit 128): branch absent | OK |
| 2b | `ls /Users/cobalt/cobalt-wt/` | 100+ entries incl. `cobalt-guard-1004`; no `cobalt-guard-b-1004` | OK |
| 3a | `git show 979ec797:ops/desk/bare-guard.py` | exists (whole file read) | OK |
| 3b | `git show 979ec797:tests/ops/test_bare_guard.py --stat` | exists (blob printed, 35.8KB); `git diff --stat 979ec797 HEAD` on both files is empty, so the line numbers below hold at BASE | OK |
| 3c | `grep -n` in `bare-guard.py` | `44:BLOCK = (` · `73:READ_FILTERS = ("grep", "sed", "cut", "sort", "uniq", "head", "tail", "wc", "awk")` · `74:ENV_READERS = ("cat", "grep", "sed", "head", "tail", "less")` · `372:def awk_writes(args):` · `389:def pipe_problems(command, cuts):` · `543:def g3_bash(segs):` · `303:def sed_problem(args):` · `330:` and `355:` `return "`sed -f`, a script the guard cannot read"` | OK (every card line number matches) |
| 3d | `grep -n` in `test_bare_guard.py` | `144:G3_ROUTE = (` · `223:def make_seat(` · `250:def call(` · `263:def run(command…` · `267:def assert_denied(done, route)` · `272:def assert_allowed(done)` · `356:def test_g11_an_awk_segment_that_can_write_is_denied` · `377:def test_g11_any_other_awk_segment_stays_allowed` · `432:def test_g3_a_read_of_env_is_denied_from_every_seat` | OK |
| 4 | card `## RECORDS` (K10, L7a) | `ops/desk/bare-guard.py` → `M operator script; no Cobalt reader -`; `tests/ops/test_bare_guard.py` → `M test/documentation; no resident -`; build report → `A DOCS -`; expected `RESTARTS: none`. Same three rows in the check report `## Suites` line 188 | OK |
| 5a | check report O4 (`## OWN FINDINGS` l.99, `## RUNS` l.170, `## OPEN` l.209) | "`sort -o`/`--output=` writes a file, `sort --compress-program=` runs a program" · REJECTED … OPEN | OK |
| 5b | check report O5 (l.119, l.171, l.210) | "`sort`, `cut`, `uniq`, `awk` … print the file and pass"; test `test_check_guard_o5_the_four_new_read_verbs_on_env_are_denied`, the 5 ids as in B1 | OK |
| 5c | check report `## DECISIONS` (l.215) 1 and 2 | "O4 — a read-only pipe can still write through `sort -o` or `uniq <in> <out>`" · "O5 — `.env` read by the four new read verbs. FOR DEJAN." | OK |
| 5d | build report `## DECISIONS` 1 (in `reports/`, l.290) | "`awk -f <file>` runs a program G11 cannot read." | OK |
| 5e | `grep -n "^\| R241 \|R247 \|R248 \|R254 "` in `cto-2026-10-03.md` | l.247 R241: "its decision 1 (`awk -f` passes G11) goes to a drafter" · l.253 R247: "1 for him (O5: `.env` past G3 by the four read verbs)" · l.254 R248: "O4, O5, `awk -f` → card `cobalt-guard-b` B1–B3" · l.260 R254: "guard-b D1 CHANGE (B2 by form), D2 CHANGE (B4 lone commands" | OK |
| 6a | `grep -n "^\| R47 "` in `cto-2026-10-02.md` | l.54, status cell `HIS RULING · APPROVED` | OK |
| 6b | `grep -n "^\| R33 "` in `cto-2026-10-03.md` | l.39, status cell `HIS RULING · APPROVED` | OK |
| 7 | each row's red-first | B1 5 ids, red `assert 0 == 2`, mutation named · B2 red ids and controls named · B3 named test and control, red/green stated, mutation named · B4 red commands and controls named. No K25 section needed (BUILD-HUB, R263) | OK |
| 8 | `grep -c -F "«FILL"` on the card | `0` | OK |

## ISSUES

None.

## NOTES

- Check 2 also holds for the card's header: `WORKTREE: cobalt-guard-b-1004` is not in `cobalt-wt`.
- Card B1 says `ENV_READERS` is line 74 and `READ_FILTERS` line 73. Both hold at BASE. `READ_FILTERS` already lists `cut sort uniq awk`; only `ENV_READERS` lacks them.
- B3 cites `bare-guard.py:372` for `awk_writes`, and it is there. `awk_writes` skips the `-f` value, which is the stated gap.
- The check report cites `bare-guard.py:73` (O5) and `:395-403` (O4) as of its tip. Those are earlier line numbers, not the card's. The card's own numbers are right at BASE.
- I read the test file at BASE through the working tree, since it is unchanged from BASE. The `git show` call confirmed the blob exists.

PREFLIGHT DONE · card: 06 · checks: 8 · fails: 0 · ready: YES
