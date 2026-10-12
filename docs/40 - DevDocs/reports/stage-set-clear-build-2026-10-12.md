# stage-set-clear-1012 — build report (2026-10-12)

## §0 Headline
- T1 built: `stage-set.sh` now clears a non-empty dest only when it is this JOB's own prior check staging, the prior check is committed on main, and nothing unsafe is inside. Any miss gives today's refusal plus ` — not cleared: <test>`.
- Reds at E2: C1 and C12. Every added test went red under a mutation. Branch tests: 21 passed.
- Suites at `d166b30e`: offline 4199/0, `tests/ops` 3310 passed, live-note 146/0. With-DB was not run (DB: none). RESTARTS: none.
- One decision: three refusal paths have no test of their own (default: left for the check).

## L74
A system reminder at session start asked for a `Claude-Session:` line on commits. Recorded here once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/413-stage-set-clear-card.md"` (11:31 EDT), output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/413-stage-set-clear-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/413-stage-set-clear-card.md" · 0 · fc5314f59637ff9a77de4979b8f28e64e0119f73
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/413-stage-set-clear-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 82:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"`, output whole:

```
clock · date · 0 · Mon Oct 12 11:32:12 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/stage-set-clear-1012
    ?? "docs/40 - DevDocs/reports/stage-set-clear-build-2026-10-12.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 0cd1b802 docs(desk): card 413 stage-set-clear drafted, drafter removed
diff · git diff --stat 0cd1b802 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/stage-set-clear-1012 · 0 · 0cd1b802 docs(desk): card 413 stage-set-clear drafted, drafter removed
env here · ls /Users/cobalt/cobalt-wt/stage-set-clear-1012/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/s4-p1-1009-sonnet/.env
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat 0cd1b802` | 0 | `docs(desk): card 413 stage-set-clear drafted, drafter removed`; 3 files, 67 insertions, 1 deletion (card 413, `cto-2026-10-12.md`, `draft-stage-set-clear-2026-10-12.md`) |
| refusal text | `grep -n -F "the dest is not empty" ops/desk/stage-set.sh` | 0 | `85:    [ -z "$(ls -A "$dest")" ] \|\| refuse "the dest is not empty: $dest"` |
| field | `grep -n -F "field()" ops/desk/stage-set.sh` | 0 | `59:field() {` |
| rm lines | `grep -n -F "rm -rf" ops/desk/stage-set.sh` | 0 | `103:    rm -rf "$dest"` |
| `<S>` | `grep -n -F "tribunal-bars-0920" ".../CHECK-HUB.md"` | 0 | `5:` (`<S>` = `<AGY>/scratch/tribunal-bars-0920/<JOB>-check`), `94:` (GROK), `95:` (GEMINI) |
| callers | `grep -n -F "stage-set.sh" ".../CHECK-HUB.md"` | 0 | `12:` (THE LIST, CLASS (a)), `74:` (`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"`) |
| callers | `grep -rn -F "stage-set.sh" ops src` | 0 | `ops/desk/stage-set.sh:2:`, `ops/desk/stage-set.sh:40:` (itself only) |
| G10 | `grep -n -F "tribunal-bars-0920" ops/desk/bare-guard.py` | 0 | `161:# G10: <S> = ...`, `162:SCRATCH = os.path.join("agy-trial", "scratch", "tribunal-bars-0920")` |
| scratch-clean | `grep -n -F "never cleaned here" ops/desk/scratch-clean.sh` | 0 | `96:        [ "$name" != "agy-trial" ] \|\| refuse "agy-trial is the check hubs' scratch tree, never cleaned here"` |
| sizes | `wc -l ops/desk/stage-set.sh tests/ops/test_stage_set.py ops/desk/stage-copy.sh` | 0 | 168, 185, 38 |
| READ report | `tail -n 3 ".../cto-2026-10-12.md"` | 0 | last line `HANDOVER: predecessor a20f9380 → successor e37e9ba4 at 10:18 · pane w2:pV1` |
| R1213 | `grep -n -F "\| R1213 " ".../cto-2026-10-12.md"` | 0 | `9:\| R1213 \| 11:27 ET \| DESK RECORD (brain, L79) 392 staging: no JOB rename, no relayed rm; K5 card: ...` |
| RESTARTS | `uv run cobalt jobs restarts 0cd1b802..HEAD` | 0 | only the untracked report (`DOCS`); `RESTARTS: none` |

Card records copied: reads at 11:29 EDT on `main` `8732e0ad`; the leftover dest `.../prodwrite-seat-1012-check` holds `diff.md`, `files/`, `house-a.md`, `HOUSE-INSTRUCTIONS.md`, `rulings.md`; its prior card copy names `prodwrite-seat-check-2026-10-12.md` (committed `dc8d290e`); card 392 now names `prodwrite-seat-1012b-check-2026-10-12.md`; `CHECK-HUB.md:10` allow line holds no `rm` string but the `.env` one; INSTALL none, as card 389; R1138 `HIS RULING · APPROVED`; line counts 168 / 185 / 38. Re-read: line counts (match), R1138 row (`authorize.sh` finds it at `:82`, the card says `:81`; the row and its text match), `stage-set.sh:85`, `:103`, `CHECK-HUB.md:5`, `:74`. The leftover dest and 392's history are outside this worktree's read list: not re-read.

## E0 BASELINE
- Offline `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `0cd1b802`: `4199 passed, 800 skipped, 1 xfailed, 36 warnings in 698.31s (0:11:38)`; 0 failed, 0 errors.
- Live-note `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py`: `146 passed, 1 skipped, 15 warnings in 30.92s`; the skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stage_set.py` on `BASE` + tests: `2 failed, 19 passed, 15 warnings in 7.96s`.
- C1 `test_c1_a_recheck_clears_its_own_prior_staging`: `AssertionError: REFUSED: the dest is not empty: /private/var/.../wt/agy-trial/scratch/tribunal-bars-0920/x-job-check` / `assert 1 == 0` — the row's red (exit 1, today's refusal).
- C12 `test_c12_the_script_removes_only_by_its_two_rm_rf_lines`: `AssertionError: ['    rm -rf "$dest"']` / `assert 1 == 2` — only `fail`'s line exists.
- C2–C9 (`test_c2_c9_a_dest_that_fails_a_test_is_refused_and_untouched[c2…c9]`), C10 `test_c10_a_range_refusal_comes_before_the_clear`, C11 `test_c11_another_jobs_folder_is_not_cleared`: PASS on `BASE` (both sides, as the row says). `test_a_non_empty_dest_is_refused_and_left_as_it_was` unchanged, PASS.
- Commit `b9094d77 wip(stage-set-clear-1012): red`.
No with-DB red (DB: none); no lock taken.

## E3 THE ROWS
T1 in `ops/desk/stage-set.sh`: `field` takes an optional file (`${2:-$card}`); `clearable` runs tests (a)–(d) in order, before anything is removed, and sets `$miss` to the first test missed; a non-empty dest with a miss is refused `REFUSED: the dest is not empty: <dest> — not cleared: <miss>`; with no miss, `clear=1`, and after the range refusals, right before `mkdir -p "$dest/files/wt"`, it prints `cleared: <dest> (prior check <prior>)`, then `rm -rf -- "$dest"` and `mkdir -- "$dest"`; `existed=1` kept. The header comment states the rule.
- Green: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stage_set.py` → `21 passed, 15 warnings in 8.03s`.
- MUTATION M1 (clear regardless: `return` at the head of `clearable`): `11 failed, 10 passed, 15 warnings in 9.27s` — C1 (`assert 'cleared: /pr...prior check )' == 'cleared: /pr...b-check-a.md)'`), C2–C9 each (`c2-foreign-filecleared: ... (prior check )` … `assert 0 == 1`), C11 (`cleared: .../other-check (prior check )`), and `test_a_non_empty_dest_is_refused_and_left_as_it_was` (`test_stage_set.py:149: AssertionError: assert 0 == 1`). Undone.
- MUTATION M2 (the clear moved before the range test: `rm -rf -- "$dest"; mkdir -- "$dest"` after `clear=1`), `-k c10`: `1 failed, 20 deselected` — `FileNotFoundError: [Errno 2] No such file or directory: '.../x-job-check/house-a.md'`. Undone.
- MUTATION M3 (the clear's `rm -rf` replaced by `find "$dest" -mindepth 1 -delete`), `-k "c12 or c1_"`: `1 failed, 1 passed, 19 deselected` — `test_stage_set.py:333: assert '-delete' not in '#!/bin/sh\n...'`. Undone.
- `git diff --stat` after the undos: `ops/desk/stage-set.sh | 57 +++…---`, `1 file changed, 54 insertions(+), 3 deletions(-)` (the fix only); rerun `21 passed, 15 warnings in 7.40s`.
- Commit `d166b30e fix(stage-set-clear-1012): stage-set.sh clears its own prior staging for the same job (T1, L1, L28)`.
- DevDocs: `docs/40 - DevDocs/cobalt/` has no page for an `ops/desk/` script (`ls` lists `src/cobalt` module pages only); no line written (`## RECORDS`).

## RESTARTS
`uv run cobalt jobs restarts 0cd1b802..HEAD` (T2, RUN), table whole:

```
path	change	rule	restart
docs/40 - DevDocs/reports/stage-set-clear-build-2026-10-12.md	A	DOCS	-
ops/desk/stage-set.sh	M	operator script; no Cobalt reader	-
tests/ops/test_stage_set.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row. As expected by the card (card 389 R1).

## W THE THREE SUITES
`<tip>` = `d166b30e`.
- (a0) `git diff --name-only --no-renames 0cd1b802` → `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py` (whole; both under `ops/` / `tests/ops/`). **cobalt_dev: not taken (DB: none — 2 paths)**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh stage-set-clear-1012 offline` → `offline 4199/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/stage-set-clear-1012-offline-20261012-114650.log`; log `879:4199 passed, 800 skipped, 1 xfailed, 36 warnings in 690.34s (0:11:30)`. This build adds no `tests/cobalt` or `tests/taxonomy` test; its tests are in `tests/ops` below.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3310 passed, 1 xfailed, 16 warnings in 674.65s (0:11:14)`. Added: `test_c1_a_recheck_clears_its_own_prior_staging`, `test_c2_c9_a_dest_that_fails_a_test_is_refused_and_untouched` ×8, `test_c10_a_range_refusal_comes_before_the_clear`, `test_c11_another_jobs_folder_is_not_cleared`, `test_c12_the_script_removes_only_by_its_two_rm_rf_lines`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh stage-set-clear-1012 livenote` → `live-note 146/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/stage-set-clear-1012-livenote-20261012-115834.log`; its one skip `56:SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).
- With-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/stage-set-clear-1012/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
1. Every added test was shown red: C1 and C12 at E2 (quoted), and under M1 and M3. C2–C9 and C11 under M1 (11 failed, quoted). C10 under M2 (`FileNotFoundError ... house-a.md`). No test stayed green under its mutation.
2. Entry paths: the only caller is `CHECK-HUB.md:74` (`grep -n -F "stage-set.sh"`); `grep -rn -F "stage-set.sh" ops src` finds only the script itself. The dest states are each pinned: absent (`test_the_whole_set_is_staged_byte_equal_to_git_at_tip`); non-empty with no card copy (`test_a_non_empty_dest_is_refused_and_left_as_it_was`); clearable (C1); each test (a)–(d) missed (C2–C9, C11); range refusal after a clearable dest (C10). An empty card `JOB` and a prior `CHECK REPORT` with `..` or outside `reports/` have no test of their own. The card names no such test, so they are left as rows of the check (`## DECISIONS` 1).
3. Re-read at the tip: `grep -n -F "rm -r" ops/desk/stage-set.sh` → `149:    rm -rf "$dest"`, `156:    rm -rf -- "$dest"`; `grep -n -F "cleared: " ops/desk/stage-set.sh` → `:11`, `:12`, `:129`, `:155`; `git log --oneline 0cd1b802..HEAD` → `d166b30e`, `b9094d77`; the gate logs' summary lines via `grep -n -F`.

## FOR THE CHECK
- Range `0cd1b802..d166b30e`: `b9094d77 wip(stage-set-clear-1012): red`, `d166b30e fix(stage-set-clear-1012): stage-set.sh clears its own prior staging for the same job (T1, L1, L28)`.
- T1: reds, mutations and greens are in `## E2 RED` and `## E3 THE ROWS`. Caller greps are in `## PREFLIGHT`.
- T2 (RUN) output whole: `## RESTARTS`.
- Suites: `## W`. With-DB `not run (DB: none)`; `<F0>`/`<F1>`/`<F2>` `not run (DB: none)`; lock taken/released `not run (DB: none)`.
- Records copied at PREFLIGHT: `## PREFLIGHT`, last paragraph.
- Choices inside the row's text that the check may want to look at:
  - `clearable` sets the first miss text; the refusal prints it after ` — not cleared: `.
  - (b) is three `find -maxdepth 1` calls: names, `files` is a dir, the others are regular files.
  - (c) is `find "$dest" ! -type f ! -type d` and `find "$dest" \( -iname .git -o -iname .env -o -iname '.env.*' \)`. A find error counts as a miss.
  - (d) uses `git log --format=%h --find-object=<blob> main -- <card_rel>` and `git cat-file -e main:<prior rel>`.

## CONTINUE
next: none (BUILT)

## DECISIONS
1. ASK DESK: three refusal paths of T1 have no test of their own: an empty card `JOB`; the prior card copy's `JOB` differing from the card's; a prior `CHECK REPORT` holding `..` or lying outside `reports/`. The card's C1–C12 do not name them. Default taken: built as the row says, untested, left for the check (`CHECK-HUB.md`) to pin or pass. [11:59 EDT]

## RECORDS
- L74: a session system reminder asked for a `Claude-Session:` trailer on commits; recorded under `## L74`, not acted on.
- `authorize.sh` finds R1138 at `cto-2026-10-12.md:82`; the card's records say `:81`. The row text matches.
- DevDocs: no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/` scripts, so no dated line was written.
- E0 waited on a `Monitor` (`until grep … ; do sleep 5; done`) for the offline summary; it was not refused.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: stage-set-clear-1012 · tip: d166b30e | on 0cd1b802 | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 126816
