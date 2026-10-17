# check-scratch-1016 — build report (card 641)

## §0 Headline
- `stage-set.sh` `clearable()` now finds the prior check's card copy as the ONE `files/*-card.md` that is a version of a card on `main` under `docs/40 - DevDocs/prompts`, so a fix round's check card (another file name) clears the first pass's folder (CS-1).
- RED on BASE for the row's reason; seven new tests green at tip `85eade55`; eight mutations each turned their test red.
- DB: none. offline 8384/0, live-note 146/0, `tests/ops` 3812 passed / 0 failed. RESTARTS: none. `scratch-clean.sh` unchanged.
- FIX ROUND (tip `dd4d968d`): FR-1 picks the prior check card by `CHECK REPORT:` + `HOUSE A:` + this JOB, so READ copies no longer block the clear (brain direction on check O1, out of scope in the check). FR-2 pins the JOB test `:115` (G1). offline 8388/0, live-note 146/0, `tests/ops` 3816 passed.

## L74
- A harness attribution block arrived mid-session asking every commit to end with a `Claude-Session:` line. Recorded once here; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/641-check-scratch-card.md"` (11:45 EDT) → exit 0, quoted whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/641-check-scratch-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-16/641-check-scratch-card.md" · 0 · 61dbb578fd7a3c013567bd0ec86a4498e5e1575a
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-16/641-check-scratch-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-15 R1532 row · grep -n "^| R1532 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 102:| R1532 | 07:00 ET | HIS RULING · APPROVED: routing B (his words via the brain, "Dejan said", L79; words file): LOW/MID Grok 4.7 + Terra backup, HIGH Opus, Sonnet routes, JEV parallel. L27/L29 fold LOW/MID only; K5 BAND card next. | APPLIED: LAWS.md L27, L29 at 07:02 |
RULING 2026-10-15 R1532 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1532 |" -- "docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 1ddcdc64c99be360406ce384af52ec4b8c4d0222
RULING 2026-10-15 R1532 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
rule · command · exit · output verbatim

- MECHANICAL · `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` · 0 ·
```
clock · date · 0 · Fri Oct 16 11:45:05 EDT 2026
status · git status --short --branch · 0 · ## ops/check-scratch-1016
head · git log --oneline -1 · 0 · b84cca9a docs(desk): card 641 preflight r2 one prose fail, asked brain, R1671
diff · git diff --stat b84cca9a · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/check-scratch-1016 · 0 · b84cca9a docs(desk): card 641 preflight r2 one prose fail, asked brain, R1671
env here · ls /Users/cobalt/cobalt-wt/check-scratch-1016/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
- BASE · `git show --stat b84cca9a` · 0 · `b84cca9a docs(desk): card 641 preflight r2 one prose fail, asked brain, R1671` — 2 files changed, 22 insertions(+), 2 deletions(-) (`.../check-scratch-card-preflight-r2-2026-10-16.md`, `docs/40 - DevDocs/reports/cto-2026-10-16.md`).
- SYMBOL · `grep -n -F "clearable" ops/desk/stage-set.sh` · 0 · `90:# clearable: every test of card 413 T1, …` · `92:clearable() {` · `128:        clearable` (the one caller: the dest gate, `:124-131`)
- SYMBOL · `grep -n -F "no prior card copy" ops/desk/stage-set.sh` · 0 · `109:    [ -f "$copied" ] || { miss="no prior card copy: $copied"; return; }`
- SYMBOL · `grep -n -F "find-object" ops/desk/stage-set.sh` · 0 · `111:    [ -n "$(git -C "$REPO" log --format=%h --find-object="$b" main -- "$card_rel")" ] \`
- SYMBOL · `grep -n -F "its files/<card name>" ops/desk/stage-set.sh` · 0 · `8:# fifo, .git or .env anywhere in it; its files/<card name> a version of the card committed on main,`
- SYMBOL · `grep -n -F "rm -rf" ops/desk/stage-set.sh` · 0 · `149:    rm -rf "$dest"` · `156:    rm -rf -- "$dest"`
- SYMBOL · `grep -n -F "def job" tests/ops/test_stage_set.py` · 0 · `52:def job(tmp_path):`
- SYMBOL · `grep -n -F "def prior_staging" tests/ops/test_stage_set.py` · 0 · `193:def prior_staging(job, *, dest=None, report="main", change=True):`
- SYMBOL · `grep -n -F "def snapshot" tests/ops/test_stage_set.py` · 0 · `225:def snapshot(root: Path) -> dict:`
- SYMBOL · `grep -n -F "test_r6_agy_trial_is_refused_though_registered" tests/ops/test_scratch_clean.py` · 0 · `315:def test_r6_agy_trial_is_refused_though_registered(desk):`
- SYMBOL · `grep -n -F "agy-trial" ops/desk/scratch-clean.sh` · 0 · `12:#       (a) $WT/<name>/… with <name> a plain directory name, never agy-trial, …` · `96:        [ "$name" != "agy-trial" ] || refuse "agy-trial is the check hubs' scratch tree, never cleaned here"`
- SYMBOL · `grep -n -F "operator script; no Cobalt reader" src/cobalt/jobs/restarts.py` · 0 · `232:                Classification(path, item.change, "operator script; no Cobalt reader", ())`
- WC · `wc -l ops/desk/stage-set.sh tests/ops/test_stage_set.py` · 0 · `219 ops/desk/stage-set.sh` · `336 tests/ops/test_stage_set.py`
- READ TAIL · `tail -n 6 ".../reports/band-routing-check-fr1-2026-10-16.md"` · 0 · last line: `FAILED: 1 — copy — REFUSED: the dest is not empty: /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/band-routing-1015-check — not cleared: no prior card copy: /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/band-routing-1015-check/files/638-band-routing-fr-check-card.md`
- RESTARTS · `uv run cobalt jobs restarts b84cca9a..HEAD` · 0 · `path	change	rule	restart` / `RESTARTS: none` (empty range)
- DB: none card: no lock probe; no with-DB string is used in this build.
- Card `## RECORDS` copied: (1) drafter `draft-check-scratch` (prompt 640), 2026-10-16 11:40 EDT, reads only, every RED UNPROVEN until quoted (L70); re-read: the `file:line`s it names (`:8`, `:108-112`, `:113`, `:114-121`, `:124-131`, `:149`, `:156`) match the greps above on BASE. (2) The cause: the refusal at `:109` because `copied` is named after the current card — re-read: line 108 `copied="$dest/files/$(basename "$card")"` and line 109 above. (3) `BAND: MID`, `RESTARTS: none` (re-read: `:232` above; the empty-range table above), `RULINGS: 2026-10-15 R1532` (re-read by authorize.sh).

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, on `b84cca9a`) → exit 0: `4572 passed, 806 skipped, 1 xfailed, 36 warnings in 690.21s (0:11:30)`. 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → exit 0: `146 passed, 1 skipped, 15 warnings in 28.75s`. The one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. It names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
Seven tests appended to `tests/ops/test_stage_set.py` (no existing test edited): `test_cs1_a_fix_rounds_check_clears_the_first_passes_folder` and six controls, each its own function: `test_cs1_control_two_card_copies_are_refused`, `test_cs1_control_a_prior_copy_of_another_job_is_refused`, `test_cs1_control_a_prior_copy_that_is_no_prompts_card_is_refused`, `test_cs1_control_the_second_pass_with_the_same_check_report_is_refused`, `test_cs1_control_a_foreign_file_blocks_the_clear`, `test_cs1_control_no_prior_card_copy_is_refused`. Helpers: `fr_card` (the second committed card `02-x-job-fr-card.md`, same fields, `CHECK REPORT` = `CHECK_B` or `CHECK_A`), `first_copy`, `refused_untouched`. Every control stages the SECOND card. The first pass is `prior_staging(job, change=False)`: the first card keeps `CHECK_A`, as a first pass's card does.

`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stage_set.py` on BASE's script → exit 1: `1 failed, 27 passed, 15 warnings in 10.02s`. The one red, its first line:
```
E       AssertionError: REFUSED: the dest is not empty: …/wt/agy-trial/scratch/tribunal-bars-0920/x-job-check — not cleared: no prior card copy: …/wt/agy-trial/scratch/tribunal-bars-0920/x-job-check/files/02-x-job-fr-card.md
```
at `assert done.returncode == 0` (`tests/ops/test_stage_set.py:364`). That is the row's named reason. All six controls PASSED on BASE.
Commit `3f0fd60e wip(check-scratch-1016): red`.

## E3 THE ROWS
### CS-1
Re-read by content before the edit (`grep -n -F` in PREFLIGHT): `:108` `copied="$dest/files/$(basename "$card")"`, `:109` the `no prior card copy` line, `:111` the `--find-object … -- "$card_rel"` line, `:8` the header sentence.
The edit, inside `clearable()`:
```
-    copied="$dest/files/$(basename "$card")"
-    [ -f "$copied" ] || { miss="no prior card copy: $copied"; return; }
+    copied=""
+    [ ! -d "$dest/files" ] || copied=$(find "$dest/files" -mindepth 1 -maxdepth 1 -type f -name '*-card.md') || { miss="find failed"; return; }
+    [ -n "$copied" ] || { miss="no prior card copy: $dest/files/*-card.md"; return; }
+    [ "$(printf '%s\n' "$copied" | wc -l | tr -d ' ')" = 1 ] || { miss="more than one prior card copy in $dest/files"; return; }
     b=$(git -C "$REPO" hash-object --no-filters "$copied") || …
-    [ -n "$(git -C "$REPO" log --format=%h --find-object="$b" main -- "$card_rel")" ] \
-        || { miss="the prior card copy is no version of the card on main"; return; }
+    [ -n "$(git -C "$REPO" log --format=%h --find-object="$b" main -- "docs/40 - DevDocs/prompts")" ] \
+        || { miss="the prior card copy is no version of a card on main under docs/40 - DevDocs/prompts"; return; }
```
Header `:8` now reads: `# fifo, .git or .env anywhere in it; its one files/*-card.md a version of a card on main under docs/40 - DevDocs/prompts,`. The JOB test, the four prior-report tests, the gate, both `rm -rf` lines and the output lines are unchanged in text.

First green run after the edit: `2 failed, 26 passed`. Two causes, both fixed before the commit:
- (i) The existing `test_a_non_empty_dest_is_refused_and_left_as_it_was` failed because the dest has no `files/`, so `find` printed `find: …` to stderr ahead of `REFUSED:`. Fix: the `[ ! -d "$dest/files" ] ||` guard (inside `clearable()`). An absent `files/` now reads as "no prior card copy".
- (ii) `test_cs1_control_a_prior_copy_that_is_no_prompts_card_is_refused` was REWRITTEN. As first written, `docs/page.md` held the card copy's exact bytes. That is the same blob as the committed prompts card, so the clear was right and the control was wrong. Now `docs/page.md` holds the card text plus one line (`a page, not a card`): a card-shaped blob on `main` outside the prompts folder. The JOB and later tests would pass it, so only the prompts-path test refuses it (see M3).

After the fix: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stage_set.py` → `28 passed, 15 warnings in 10.47s`. `uv run pytest -q -p no:cacheprovider --color=no tests/ops` → `3812 passed, 1 xfailed, 16 warnings in 837.43s (0:13:57)`.

THE MUTATIONS (Edit tool; each undone with the Edit tool). Runs are `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_stage_set.py`, or `-k cs1 --tb=no` for M5–M8:
| # | mutation | summary | failing test, first line |
|---|---|---|---|
| M1 | the BASE lines of `:108-112` back (undoes the fix) | `1 failed, 27 passed` | `test_cs1_a_fix_rounds_…`: `AssertionError: REFUSED: the dest is not empty: … — not cleared: no prior card copy: …/files/02-x-job-fr-card.md`. All six controls GREEN on BASE's lines, the rewritten one included |
| M2 | count guard replaced by `copied=$(printf '%s\n' "$copied" \| sed -n 1p)` | `1 failed, 27 passed` | `test_cs1_control_two_card_copies_are_refused`: `AssertionError: cleared: …/x-job-check (prior check …/x-job-check-a.md)` |
| M3 | `-- "docs/40 - DevDocs/prompts"` dropped (whole history) | `1 failed, 27 passed` | `test_cs1_control_a_prior_copy_that_is_no_prompts_card_is_refused`: `AssertionError: cleared: …` |
| M4 | the `[ ! -d "$dest/files" ] \|\|` guard dropped | `1 failed, 27 passed` | `test_a_non_empty_dest_is_refused_and_left_as_it_was`: `AssertionError: assert False … 'find: …/x-job-check — not cleared: find failed'` |
| M5 | version test and JOB test removed | `2 failed, 5 passed, 21 deselected` | `test_cs1_control_a_prior_copy_of_another_job_is_refused`, `test_cs1_control_a_prior_copy_that_is_no_prompts_card_is_refused`: `AssertionError: cleared: …` |
| M6 | the "this check's own" test removed | `1 failed, 6 passed, 21 deselected` | `test_cs1_control_the_second_pass_with_the_same_check_report_is_refused` |
| M7 | the "an entry the check did not write" test removed | `1 failed, 6 passed, 21 deselected` | `test_cs1_control_a_foreign_file_blocks_the_clear` |
| M8 | `[ -n "$copied" ] \|\| return` (no miss) | `1 failed, 6 passed, 21 deselected` | `test_cs1_control_no_prior_card_copy_is_refused` |

The M7 restore first dropped a newline (an Edit slip). That made the first M8 run `7 failed` with the script broken, so that run is void. The newline was put back, `git diff` showed only the M8 change, and M8 was run again: the row above. After M8 was undone: `git diff --stat` → empty, and `tests/ops/test_stage_set.py` → `28 passed, 15 warnings in 10.18s`.
No module page for `ops/desk/stage-set.sh` exists under `docs/40 - DevDocs/cobalt/` (Grep `stage-set` there: no files), so none was written (`## RECORDS`).
Commit `85eade55 fix(check-scratch-1016): stage-set clears a fix round's check by the one prior card copy (CS-1, L1, L3)`.

### R2 (RUN — asserts nothing)
- `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_stage_set.py tests/ops/test_scratch_clean.py` → `76 passed, 15 warnings in 17.21s`
- `git diff --stat b84cca9a..HEAD -- ops/desk/scratch-clean.sh` → (nothing printed)
- `uv run cobalt jobs restarts b84cca9a..HEAD` → the table under `## RESTARTS`; `RESTARTS: none`.
Nothing it shows is a DECISION.

## RESTARTS
`uv run cobalt jobs restarts b84cca9a..HEAD` (tip `85eade55`), quoted whole:
```
path	change	rule	restart
docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.md	A	DOCS	-
ops/desk/stage-set.sh	M	operator script; no Cobalt reader	-
tests/ops/test_stage_set.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row.

## W THE THREE SUITES
`<tip>` = `85eade55`.
- (a0) `git diff --name-only --no-renames b84cca9a` → `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py`. Every path starts with `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 2 paths)`**
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh check-scratch-1016 offline` → exit 0:
```
tests/ops: run (ops/desk/stage-set.sh)
offline 8384/0
log: /Users/cobalt/cobalt-wt/.gate-logs/check-scratch-1016-offline-20261016-121457.log
```
  Tests this build adds: the seven `test_cs1_…` above.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh check-scratch-1016 livenote` → exit 0:
```
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/check-scratch-1016-livenote-20261016-121458.log
```
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 0: `3812 passed, 1 xfailed, 16 warnings in 840.27s (0:14:00)`.
- with-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/check-scratch-1016/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown RED for its named reason against a mutation or a negative control. `test_cs1_a_fix_rounds_…`: E2 red and M1. Two-copies: M2. Another-job: M5 refuses it by the version test first, so M5 does not pin the JOB test `:115`; the JOB test is pinned by `test_cs1_rewritten_job_line_is_refused_by_the_job_test_not_the_blob` (fix round FR-2: `:115` removed alone → this test red, `1 failed, 31 passed`, `AssertionError: cleared: …`). No-prompts: M3, M5. Same-check-report: M6. Foreign-file: M7. No-copy: M8. One test that stayed wrong (the no-prompts control as first written) was rewritten: E3 (ii).
(2) Every entry path is pinned. `clearable` has one caller, `:128` (grep in PREFLIGHT), reached only with a non-empty dest. Paths through it: the fix round clears (main test). None, two or a non-prompts copy (three controls). Another JOB (control). Own report (control). Foreign entry (control). Absent `files/` (existing `test_a_non_empty_dest_…`, M4). The existing re-check of the same card name still clears (`test_c1_…`), and `test_c2_c9_…` ×8, `test_c10_…`, `test_c11_…` and `test_c12_…` are green at tip.
(3) Re-read at the tip: `git show 85eade55:ops/desk/stage-set.sh` (whole); `grep -n -F "rm -r" ops/desk/stage-set.sh` → `151:    rm -rf "$dest"` and `158:    rm -rf -- "$dest"` (two lines, their text unchanged, moved +2 by the edit); `grep -n -F "def test_cs1_" tests/ops/test_stage_set.py` → `:359`, `:419`, `:423`, `:427`, `:431`, `:435`, `:439`; `grep -c -F "more than one prior card copy" ops/desk/stage-set.sh` → `1`; `git log --oneline b84cca9a..HEAD` → the two commits below.

## FOR THE CHECK
- Range `b84cca9a..85eade55`: `3f0fd60e wip(check-scratch-1016): red`, `85eade55 fix(check-scratch-1016): stage-set clears a fix round's check by the one prior card copy (CS-1, L1, L3)`. The report commit is above the tip.
- CS-1 reds, mutations and greens: `## E2 RED` and `## E3 THE ROWS`. R2's output in full: `## E3` `### R2`.
- Caller grep: `grep -n -F "clearable" ops/desk/stage-set.sh` → `:90` (comment), `:92` (definition), `:128` (the one call).
- Suites: offline `offline 8384/0` (`gate.sh check-scratch-1016 offline`), live-note `live-note 146/0` (`gate.sh check-scratch-1016 livenote`), `tests/ops` `3812 passed, 1 xfailed`; with-DB: not run (DB: none).
- `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock taken / released: not run (DB: none).
- RESTARTS table: `## RESTARTS`.
- For X3: the `rm -rf` lines moved from `:149`/`:156` to `:151`/`:158` (two lines added above them inside `clearable()`); their text is unchanged; `test_c12_…` green.
- The card's `## RECORDS`, as re-read at PREFLIGHT, are copied in `## PREFLIGHT`.

## FIX ROUND (FR-1, FR-2) — 2026-10-16
Launched `CONTINUE: FIX ROUND row FR-1` as a new session (RECOVERY). `git status --short --branch` → `## ops/check-scratch-1016`; `git log --oneline -3` → `0605334f`, `85eade55`, `3f0fd60e`; `ls -la …/check-scratch-1016/.env` → `No such file or directory`; `date` → `Fri Oct 16 14:03:56 EDT 2026`.

- BUILT: FR-1 — brain direction (R1706) on check O1; O1 was out of scope in the check, not HELD — tests/ops/test_stage_set.py::test_fr1_a_build_card_read_copy_does_not_block_the_clear
FIXED: G1 — tests/ops/test_stage_set.py::test_cs1_rewritten_job_line_is_refused_by_the_job_test_not_the_blob

### AUTHORIZATION (fix round)
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "<card>"` → exit 0. Rows as in `## AUTHORIZATION` above, except `CARD COMMITTED · … · 0 · 1edaae19cdd7dddce9fd28564b1dafd6df21003e`. Last line `AUTHORIZED`.

### PREFLIGHT (fix round)
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 1, quoted whole:
```
clock · date · 0 · Fri Oct 16 14:04:09 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/check-scratch-1016
     M "docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.md"
head · git log --oneline -1 · 0 · 0605334f docs(check-scratch-1016): build report — 85eade55
diff · git diff --stat b84cca9a · 0 · (5 lines)
     .../reports/check-scratch-build-2026-10-16.md      | 180 +++++++++++++++++++++
     .../reports/check-scratch-build-2026-10-16.result  |  15 ++
     ops/desk/stage-set.sh                              |  12 +-
     tests/ops/test_stage_set.py                        | 104 ++++++++++++
     4 files changed, 306 insertions(+), 5 deletions(-)
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/check-scratch-1016 · 0 · 0605334f docs(check-scratch-1016): build report — 85eade55
env here · ls /Users/cobalt/cobalt-wt/check-scratch-1016/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
FAILED PREFLIGHT: status
```
The one `M` line is this report's `RESUMED:` last line, the write RECOVERY makes first; `git status --short --branch` before that write printed `## ops/check-scratch-1016` alone. The head and the diff against BASE are the first build's, as a fix round on a built branch has them. See `## DECISIONS` 1.

### FR-1 — red on the tip `0605334f` (code `85eade55`)
The fixture line `HOUSE A: grok` added (the one existing line edited, `tests/ops/test_stage_set.py:78`), the three FR-1 tests appended. `uv run pytest -q -p no:cacheprovider --color=no -rA --tb=line tests/ops/test_stage_set.py` → exit 1, `2 failed, 29 passed, 15 warnings in 11.74s`. The two reds, first lines:
```
E   AssertionError: REFUSED: the dest is not empty: …/test_fr1_a_build_card_read_cop0/wt/agy-trial/scratch/tribunal-bars-0920/x-job-check — not cleared: more than one prior card copy in …/x-job-check/files
/Users/cobalt/cobalt-wt/check-scratch-1016/tests/ops/test_stage_set.py:476: AssertionError: …
E   AssertionError: REFUSED: the dest is not empty: …/test_fr1_control_this_jobs_own0/wt/agy-trial/scratch/tribunal-bars-0920/x-job-check — not cleared: more than one prior card copy in …/x-job-check/files
/Users/cobalt/cobalt-wt/check-scratch-1016/tests/ops/test_stage_set.py:508: AssertionError: …
```
Both at `assert done.returncode == 0`; the second at its clear half (`:508`), its refuse half having passed. GREEN in the same run (THE GUARD: the fixture line in, before the `clearable()` edit): `test_c1_a_recheck_clears_its_own_prior_staging`, `test_c2_c9_…` ×8 (c2-foreign-file, c3-prior-report-untracked, c4-prior-report-off-main, c5-symlink, c6-dot-env, c7-dot-git, c8-card-copy-edited, c9-prior-is-this-check), `test_c10_a_range_refusal_comes_before_the_clear`, `test_c11_another_jobs_folder_is_not_cleared`, `test_c12_the_script_removes_only_by_its_two_rm_rf_lines`, `test_cs1_a_fix_rounds_check_clears_the_first_passes_folder`, the six `test_cs1_control_…`, and `test_fr1_control_two_same_job_check_cards_are_refused`. Commit `a370ecce wip(check-scratch-1016): FR-1 red`.

### FR-1 — the edit
Inside `clearable()` only (`ops/desk/stage-set.sh:108-133` at the tip): each `*-card.md` of `$dest/files` is read up to its first blank line; one with both `^CHECK REPORT:` and `^HOUSE A:` there is a check card; its `field JOB` equal to this JOB puts it in `mine`, else in `others`. `mine` empty → `others` (THE FALLBACK). None → `no prior card copy: $dest/files/*-card.md`; two or more → `more than one prior card copy in $dest/files`; one → `copied`. The version test (`:134-136`) and the JOB test (`:137`) follow unchanged. Header `:8` amended (one sentence). `git diff 85eade55 -- ops/desk/stage-set.sh` → the header line and the `clearable()` hunk only, `26 insertions(+), 4 deletions(-)`.
After the edit: the same command → `32 passed, 15 warnings in 12.19s` (FR-2's test appended by then; before it, `31 passed, 15 warnings in 11.96s`). Every test named under THE GUARD above is PASSED again in the `-rA` lines.

FR-1 mutations (Edit, undone by Edit; `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_stage_set.py`):
| # | mutation | summary | red |
|---|---|---|---|
| F1 | the `^HOUSE A:` filter line removed | `2 failed, 29 passed` | `test_fr1_a_build_card_read_copy_…` (`:476`) and `test_fr1_control_this_jobs_own_check_folder_shape` (`:508`), both `more than one prior card copy` |
| F2 | the JOB split → `if true; then` (every check card in `mine`) | `1 failed, 30 passed` | `test_fr1_control_this_jobs_own_check_folder_shape` (`:508`), `more than one prior card copy` |
| F3 | THE FALLBACK line `[ -n "$mine" ] \|\| mine=$others` removed | `1 failed, 31 passed` | `test_cs1_rewritten_job_line_…` (`:533`): `assert "the prior card copy's JOB is not x-job" in 'REFUSED: … no prior card copy: …/files/*-card.md'` |
After the undo: `git diff --stat 85eade55 -- ops/desk/stage-set.sh` → `1 file changed, 26 insertions(+), 4 deletions(-)` (the FR-1 edit only).

### FR-2
`test_cs1_rewritten_job_line_is_refused_by_the_job_test_not_the_blob` appended: a `y-job` card (header `CHECK REPORT:` `CHECK_A`, `HOUSE A: grok`) committed under `prompts/2026-01-02/` of the tmp repo, copied as the SOLE `*-card.md` (the first copy unlinked), the second card staged. Green with the JOB line in place: `32 passed, 15 warnings in 12.36s`.
MUTATION (after FR-1, as the row asks): the line `[ "$(field JOB "$copied")" = "$name" ] || { miss="the prior card copy's JOB is not $name"; return; }` removed alone by Edit → `1 failed, 31 passed, 15 warnings in 12.35s`:
```
FAILED tests/ops/test_stage_set.py::test_cs1_rewritten_job_line_is_refused_by_the_job_test_not_the_blob
E   AssertionError: cleared: …/test_cs1_rewritten_job_line_is0/wt/agy-trial/scratch/tribunal-bars-0920/x-job-check (prior check …/repo/docs/40 - DevDocs/reports/x-job-check-a.md)
/Users/cobalt/cobalt-wt/check-scratch-1016/tests/ops/test_stage_set.py:531: AssertionError: cleared: …
```
Undone by Edit; `git diff --stat 85eade55 -- ops/desk/stage-set.sh` → `ops/desk/stage-set.sh | 30 ++++++++++++++++++++++++++----` (the FR-1 edit only). CONTROL: `test_cs1_control_a_prior_copy_of_another_job_is_refused` PASSED with the line in place, unedited. The M5 clause of `## PRE-STOP SELF-CHECK` (1) corrected to name this test.
Commit `dd4d968d fix(check-scratch-1016): stage-set picks the prior check card by CHECK REPORT and HOUSE A and this JOB; the JOB test pinned (FR-1, FR-2, L1, L3)`.

### Fences and RUNs at the tip `dd4d968d`
- `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_stage_set.py tests/ops/test_scratch_clean.py` → `80 passed, 15 warnings in 17.96s`.
- `git diff --stat 85eade55 -- ops/desk/scratch-clean.sh tests/ops/test_scratch_clean.py` → (nothing printed).
- `grep -c -F "rm -r" ops/desk/stage-set.sh` → `2` (`:173` `rm -rf "$dest"`, `:180` `rm -rf -- "$dest"`).
- `git diff 85eade55 -U0 -- tests/ops/test_stage_set.py` → one existing line changed (`@@ -78 +78 @@`, the fixture line), the rest appended after `:440`; no assertion edited.
- `uv run cobalt jobs restarts 85eade55..HEAD`, quoted whole:
```
path	change	rule	restart
docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.md	M	DOCS	-
docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.result	A	DOCS	-
ops/desk/stage-set.sh	M	operator script; no Cobalt reader	-
tests/ops/test_stage_set.py	M	test/documentation; no resident	-
RESTARTS: none
```
- (a0) `git diff --name-only --no-renames b84cca9a` → `docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.md`, `docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.result`, `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py`. Every path starts with `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 4 paths)`**

### W (fix round) on `<tip>` = `dd4d968d`
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh check-scratch-1016 offline` → exit 0:
```
tests/ops: run (ops/desk/stage-set.sh)
offline 8388/0
log: /Users/cobalt/cobalt-wt/.gate-logs/check-scratch-1016-offline-20261016-140859.log
```
  Tests this round adds: `test_fr1_a_build_card_read_copy_does_not_block_the_clear`, `test_fr1_control_two_same_job_check_cards_are_refused`, `test_fr1_control_this_jobs_own_check_folder_shape`, `test_cs1_rewritten_job_line_is_refused_by_the_job_test_not_the_blob` (8384 + 4 = 8388).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh check-scratch-1016 livenote` → exit 0:
```
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/check-scratch-1016-livenote-20261016-140900.log
```
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 0: `3816 passed, 1 xfailed, 16 warnings in 835.71s (0:13:55)`.
- with-DB: not run (DB: none); `--deploy` not typed (W (a0): gate.sh accepts it with withdb and all only). `<F0>`/`<F1>`/`<F2>`, lock times: not run (DB: none). `ls /Users/cobalt/cobalt-wt/check-scratch-1016/.env` → `No such file or directory` (14:34 EDT).

### PRE-STOP SELF-CHECK (fix round)
(1) FR-1: `test_fr1_a_…` and `test_fr1_control_this_jobs_own_…` red on the tip run (`:476`, `:508`, `more than one prior card copy`), and under F1 / F2. `test_fr1_control_two_same_job_…` is a control green on both sides, as the row names it. FR-2: `test_cs1_rewritten_job_line_…` red under the `:115` mutation (`:531`, `AssertionError: cleared: …`) and under F3 (`:533`); the M5 clause is corrected.
(2) `clearable` has one caller, `grep -n -F "clearable" ops/desk/stage-set.sh` → the comment, the definition and the one call in the dest gate. Paths through the new selection: one this-JOB check card among a READ build copy (`test_fr1_a_…`); with other-JOB check cards (`…own_check_folder_shape`, clear half); two of this JOB (`…two_same_job…`, `test_cs1_control_two_card_copies…`); none of this JOB and two others (`…own_check_folder_shape`, refuse half); none of this JOB and one other (FR-2's test; `test_cs1_control_a_prior_copy_of_another_job…`); none at all (`test_cs1_control_no_prior_card_copy…`, `test_a_non_empty_dest_…`); a no-prompts card (`test_cs1_control_a_prior_copy_that_is_no_prompts_card…`); an edited copy (c8).
(3) Re-read at the tip: `grep -n -F "prior card copy" ops/desk/stage-set.sh` → `:131`, `:132`, `:136`, `:137`; `grep -n -F "rm -rf" ops/desk/stage-set.sh` → `:173`, `:180`; `grep -n -F "def test_fr1_" tests/ops/test_stage_set.py` → `:468`, `:483`, `:489`; `grep -n -F "def test_cs1_rewritten" tests/ops/test_stage_set.py` → `:518`; `git log --oneline 85eade55..HEAD` → `dd4d968d`, `a370ecce`, `0605334f`.

### FOR THE CHECK (fix round)
- Range `85eade55..dd4d968d`: `a370ecce wip(check-scratch-1016): FR-1 red`, `dd4d968d fix(check-scratch-1016): stage-set picks the prior check card by CHECK REPORT and HOUSE A and this JOB; the JOB test pinned (FR-1, FR-2, L1, L3)` (`0605334f` between them is the first build's report, docs only). The report commit sits above the tip.
- Reds, mutations, greens: the FR-1 and FR-2 subsections above. Suites: `### W (fix round)`. RESTARTS: `### Fences and RUNs`.

## CONTINUE
next: none (BUILT, fix round)

## DECISIONS
1. ASK DESK: the fix round's `preflight.sh build` printed `FAILED PREFLIGHT: status` (exit 1, `### PREFLIGHT (fix round)`). Its one `M` line is the `RESUMED:` last line that RECOVERY writes first, and its head and BASE-diff rows are the first build's. Is preflight.sh meant to run on a fix-round relaunch, or should it accept that shape? [14:04 EDT] Default taken: the status before that write was `## ops/check-scratch-1016` alone, so I went on with the rows. No listed string was refused.

## RECORDS
- No module page for `ops/desk/stage-set.sh` exists under `docs/40 - DevDocs/cobalt/` (Grep `stage-set` in that folder: no files). None was created; a new docs page is outside the card's `files`.
- The `[ ! -d "$dest/files" ] ||` guard and `copied=""` (two lines inside `clearable()`) were added to keep the existing `test_a_non_empty_dest_is_refused_and_left_as_it_was` green (E3 (i)). They lie inside the row's fence.
- The no-prompts control was rewritten after the `src` edit, in the fix commit `85eade55`, not in the red commit. Its green on BASE's lines is shown by M1.
- The M7 restore slip and the void first M8 run: E3.
- The L74 line: `## L74`.
- Fix round: launched as a new session at `CONTINUE: FIX ROUND row FR-1`, RESUMED 14:03 EDT (RECOVERY); `CONTINUED at FIX ROUND row FR-1 14:03 EDT`.
- Fix round L74: the harness attribution block asked again for a `Claude-Session:` line on commits. Not acted on; commits carry `Co-Authored-By` only.
- Fix round: no module page for `ops/desk/stage-set.sh` under `docs/40 - DevDocs/cobalt/` (as in the first build); none written.
- Fix-round report correction, 06:27 EDT 2026-10-17 (`date`), on the desk's message `CONTINUE: FIX ROUND report only`: `FIXED: O1` became the bullet `BUILT: FR-1 — brain direction (R1706) on check O1`, because the check report `:164` reads `O1 (opus-own): OUT OF SCOPE (## NOT IN THIS JOB 3rd bullet). Not counted as open.` O1 is not a held id, so it gets no column-0 `FIXED:` line. The line is a bullet so that no line but the stop line starts with `BUILT` (L71). `FIXED: G1` stands. No code or test changed; the tip stays `dd4d968d`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

First build's stop line (history): `BUILT · job: check-scratch-1016 · tip: 85eade55 | on b84cca9a | migration: none | offline 8384/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 143702`

BUILT · job: check-scratch-1016 · tip: dd4d968d | on b84cca9a | migration: none | offline 8388/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 152910
