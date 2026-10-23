# radar-mirror-scope — card 1020 preflight round 2 (prompt 1026)

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git log --oneline -- <card>`; `git diff --stat HEAD -- <card>` | `4c68cd4c` (R2398 amended) on top of round-1 `b9e59913`; diff against HEAD empty (card committed) | OK |
| 2 | `git diff b9e59913 4c68cd4c -- <card>` | exactly three hunks: (a) WHY `after the WBD edit` → `after the 10-21 edit`; (b) M1: constant text gains `(ONE line, assigned once; no other line of notes.py holds the text MIRROR_SOURCE_PREFIX = , the deploy proof counts it)` and the unknown-source test gains the "One line is PER `mirror_sources` call" sentence; (c) DEPLOY PROOF marker 1. No other line differs | OK |
| 3 | marker 1 vs `deploy-smoke.sh:122-131` | `grep -c -F "MIRROR_SOURCE_PREFIX = " /Users/cobalt/cobalt/src/cobalt/radar/notes.py`: opens with `grep -c -F "`, has a closing `" ` followed by a plain path; pattern `MIRROR_SOURCE_PREFIX = ` is non-empty, no `$`, backtick or backslash; `:129` plain_path gets the notes.py path. Maps as `grep` | OK |
| 4 | markers 2, 3, 4 vs `deploy-smoke.sh:118-129` | marker 2 pattern `def test_m2_a_lists_edit_..._byte_identical` has no quote, backslash, `$` or backtick, path plain; the two `ls` rows are plain paths. All map. No `curl`, URL or `db query` in the section | OK |
| 5 | before count on main: `grep -c -F "MIRROR_SOURCE_PREFIX = " src/cobalt/radar/notes.py` | `0` (and `grep -c -F "MIRROR_SOURCE_PREFIX"` → `0`), so `before 0` holds | OK |
| 6 | after count from the card's M1 text | M1 defines `MIRROR_SOURCE_PREFIX = "vault:radar-notes@"` once, on one line, and states no other line holds `MIRROR_SOURCE_PREFIX = `. Uses of the name (label `:749`, ownership test) read `MIRROR_SOURCE_PREFIX)` / `{MIRROR_SOURCE_PREFIX}` / `startswith(MIRROR_SOURCE_PREFIX`, none followed by ` = `. `FOREIGN_SOURCE_PREFIXES` does not contain the text. After = 1. The `notes.md` docs are a different file | OK |
| 7 | marker 2 before | test file does not exist on main (new file), same shape as round 1 NOTE 8; `after 1` once M2's `def` line is written | OK |
| 8 | `## RECORDS` line 1 vs prompt 1019 | `grep -c -F` of the whole sentence in `1019-draft-radar-mirror-scope.md` → 1; the card line is unchanged by the diff of check 2 | OK |
| 9 | ticker name elsewhere in the card: `grep -n -F "WBD" <card>` | one hit, line 65, the verbatim RECORDS line only. WHY now says "the 10-21 edit" | OK |
| 10 | round 1 header values | JOB, LADDER, BRANCH, WORKTREE, BASE `7487bb56`, TIP empty, BAND `HIGH`, RESTARTS `com.cobalt.radar`, MIGRATIONS `none`, RULINGS `2026-10-23 R2389` unchanged (not in the check-2 diff) | OK |
| 11 | OWNERSHIP, M2, M3, M4, F1 (fakes list), R1, D0, ORDER, NOT IN THIS JOB, READ, CHECK ASKS | unchanged (not in the check-2 diff); round 1 checks 3-22 and 26-30 therefore stand: file:line cites, `store.py` and migration cites, the six foreign labels, M2/M3/M4 testability, F1 completeness (`MirrorStore`, `Store`, `Settings`, `CrossingSettingsStore` with the `self.rows` shadow, `_Settings`), D0 target, K10 homes for all three file classes | OK |
| 12 | builder commands vs `BUILD-HUB.md:14`, `:16` | ORDER and R1 use the same commands as round 1 (`uv run pytest -q -p no:cacheprovider --color=no <6 files>`, `uv run cobalt jobs restarts <BASE>..HEAD`, `git add`/`git commit`, `grep`, `ls`); not touched by the amend | OK |
| 13 | M1's unknown-source test, as amended | the sink wraps each `mirror_sources` call alone and the assertion counts one warning per call; `hand_typed` is absent from the notes in both calls, so each call logs one line. Round 1 NOTE 6 is closed | OK |
| 14 | what blocks the card's own build | nothing found | OK |

## ISSUES
- NOTE 1: BASE `7487bb56` trails `main` by desk commits; not a fail, the desk resets it.
- NOTE 2: marker 2's `before 0` is a file that does not exist yet (`grep -c` prints no count, exit 2), the same shape as round 1.
- NOTE 3: the card's verbatim RECORDS line still names the ticker (line 65, required verbatim). L32 binds the builder's report and commits: say "the 10-21 edit".
- NOTE 4 (X6, carried from round 1): `com.cobalt.aset` reaches `cobalt.radar.notes` only through function-level imports (`drc/build.py:171`, constant `REPLAY_LABEL`); R1's table settles whether the header's RESTARTS needs it.
- NOTE 5 (carried from round 1): M4 pins only the Lists-only label case; the other cases fall to PRE-STOP SELF-CHECK 2.
- Blocks the card's own build: nothing.

PREFLIGHT DONE · card: radar-mirror-scope r2 · checks: 14 · fails: 0 · ready: YES
