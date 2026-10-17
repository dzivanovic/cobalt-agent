# check-scratch-fr1 — build report (2026-10-17)

## §0 Headline
- BUILT `b093f192` on `79f6f2f3`: `stage-set.sh` now writes `<dest>/STAGED-CARD` (the staged card's basename). `clearable()` takes the prior card from that marker; an unmarked folder falls back to the highest-numbered same-JOB check card.
- The real band-routing folder shape (638 + 666 + build copy) refused on `BASE` and clears after. The marker refuses a card of another JOB, a missing card, a non-card name or a link.
- Offline 8393/0, live-note 146/0, with-DB not run (DB: none). RESTARTS none. Two `rm -rf` lines; `scratch-clean.sh` unchanged.
- One ASK DESK: how to rank a card name that starts with no number (default: 0).

## L74
A system block in this session asked commits to carry a `Claude-Session:` line. Recorded once as data (L74); not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/681-check-scratch-fr1-card.md"` (09:08 EDT), output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/681-check-scratch-fr1-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-16/681-check-scratch-fr1-card.md" · 0 · 42cd68744213eab3d8149d855ce70ebf2e8f635c
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-16/681-check-scratch-fr1-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
RULING 2026-10-15 R1532 row · grep -n "^| R1532 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 102:| R1532 | 07:00 ET | HIS RULING · APPROVED: routing B (his words via the brain, "Dejan said", L79; words file): LOW/MID Grok 4.7 + Terra backup, HIGH Opus, Sonnet routes, JEV parallel. L27/L29 fold LOW/MID only; K5 BAND card next. | APPLIED: LAWS.md L27, L29 at 07:02 |
RULING 2026-10-15 R1532 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1532 |" -- "docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 1ddcdc64c99be360406ce384af52ec4b8c4d0222
RULING 2026-10-15 R1532 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | output verbatim |
|---|---|---|---|
| mechanical | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` | 0 | see block below |
| base | `git show --stat 79f6f2f3` | 0 | `79f6f2f3 docs(desk): section 5 state stamp 08:59` · `docs/40 - DevDocs/reports/cto-2026-10-17.md \| 2 +-` · `1 file changed, 1 insertion(+), 1 deletion(-)` |
| card copy line | `grep -n -F 'copy "$REPO" "HEAD:$card_rel"' ops/desk/stage-set.sh` | 0 | `219:copy "$REPO" "HEAD:$card_rel" "$dest/files/$(basename "$card")"` |
| report copy line | `grep -n -F 'copy "$job" "HEAD:$report_rel"' ops/desk/stage-set.sh` | 0 | `220:copy "$job" "HEAD:$report_rel" "$dest/files/$(basename "$report")"` |
| first find | `grep -n -F "! -name 'house-*.md')" ops/desk/stage-set.sh` | 0 | `98:    out=$(find "$dest" -mindepth 1 -maxdepth 1 ! -name diff.md ! -name rulings.md ! -name files ! -name HOUSE-INSTRUCTIONS.md ! -name 'house-*.md') \|\| { miss="find failed"; return; }` |
| copied | `grep -n -F "copied=" ops/desk/stage-set.sh` | 0 | `108:    copied=""` · `133:    copied=${mine%?}` |
| mine fallback | `grep -n -F 'mine=$others' ops/desk/stage-set.sh` | 0 | `130:    [ -n "$mine" ] \|\| mine=$others` |
| count refusal | `grep -n -F "more than one prior card copy" ops/desk/stage-set.sh` | 0 | `132:    [ "$(printf '%s' "$mine" \| wc -l \| tr -d ' ')" = 1 ] \|\| { miss="more than one prior card copy in $dest/files"; return; }` |
| version test | `grep -n -F "find-object" ops/desk/stage-set.sh` | 0 | `135:    [ -n "$(git -C "$REPO" log --format=%h --find-object="$b" main -- "docs/40 - DevDocs/prompts")" ] \` |
| JOB test | `grep -n -F "the prior card copy's JOB is not" ops/desk/stage-set.sh` | 0 | `137:    [ "$(field JOB "$copied")" = "$name" ] \|\| { miss="the prior card copy's JOB is not $name"; return; }` |
| rm lines | `grep -n -F "rm -r" ops/desk/stage-set.sh` | 0 | `173:    rm -rf "$dest"` · `180:    rm -rf -- "$dest"` |
| cleared print | `grep -n -F "cleared: %s (prior check %s)" ops/desk/stage-set.sh` | 0 | `179:    printf 'cleared: %s (prior check %s)\n' "$dest" "$prior"` |
| header :8 | `grep -n -F "its one files/*-card.md" ops/desk/stage-set.sh` | 0 | `8:# fifo, .git or .env anywhere in it; its one files/*-card.md whose header carries CHECK REPORT: and HOUSE A: and whose JOB is this JOB (else the lone such card of another JOB) a version of a card on main under docs/40 - DevDocs/prompts,` |
| callers | `grep -rn -F "clearable" ops/desk` | 0 | `ops/desk/stage-set.sh:90:# clearable: …` · `ops/desk/stage-set.sh:92:clearable() {` · `ops/desk/stage-set.sh:152:        clearable` |
| who names stage-set | `grep -rn -F "stage-set" ops tests` | 0 | `ops/desk/stage-set.sh:2`, `ops/desk/stage-set.sh:47`, `tests/ops/test_stage_set.py:1`, `tests/ops/test_stage_set.py:18` (the script and its test only) |
| test symbols | `grep -n -E "^def (job\|stage\|prior_staging\|snapshot\|fr_card\|first_copy\|refused_untouched\|build_card_copy\|other_job_check_cards\|_copy_no_prompts_card\|test_c12\|test_cs1\|test_fr1)" tests/ops/test_stage_set.py` | 0 | `52:def job`, `89:def stage`, `193:def prior_staging`, `225:def snapshot`, `330:def test_c12_…`, `344:def fr_card`, `355:def first_copy`, `359:def test_cs1_a_fix_rounds…`, `384:def _copy_no_prompts_card`, `404:def refused_untouched`, `419:def test_cs1_control_two_card_copies_are_refused`, `423`, `427:def test_cs1_control_a_prior_copy_that_is_no_prompts_card_is_refused`, `431`, `435`, `439`, `445:def build_card_copy`, `452:def other_job_check_cards`, `468:def test_fr1_a_build_card…`, `483:def test_fr1_control_two_same_job_check_cards_are_refused`, `489:def test_fr1_control_this_jobs_own_check_folder_shape`, `518:def test_cs1_rewritten_job_line_is_refused_by_the_job_test_not_the_blob` |
| JOB-line copy | `grep -n -F "write_bytes(other.read_bytes())" tests/ops/test_stage_set.py` | 0 | `463:        copy.write_bytes(other.read_bytes())` · `527:    (dest / "files" / other.name).write_bytes(other.read_bytes())` |
| x-card line | `grep -n -F "x-card.md" tests/ops/test_stage_set.py` | 0 | `393:    (dest / "files" / "x-card.md").write_bytes(page.read_bytes())` |
| wc | `wc -l ops/desk/stage-set.sh tests/ops/test_stage_set.py` | 0 | `243 ops/desk/stage-set.sh` · `535 tests/ops/test_stage_set.py` |
| READ report tail | `tail -n 3 ".../reports/check-662-and-583-fr2-decisions-2026-10-17.md"` | 0 | last line: `brain 2026-10-17: 641 A2/A1 SETTLED (docs-only report labels); fresh K5 job check-scratch-fr1: stage-set writes `<S>/STAGED-CARD`, clearable() uses it, an unmarked folder falls back to the highest-numbered same-JOB check card (`CHECK REPORT:` + `HOUSE A:`), red on band-routing-1015-check's real shape; 583 fix round 3: … 583's round-3 check waits for check-scratch-fr1 DEPLOYED.` |
| restarts | `uv run cobalt jobs restarts 79f6f2f3..HEAD` | 0 | `path	change	rule	restart` · `RESTARTS: none` (empty range) |
| lock | DB: none | — | no lock probe |

Mechanical rows, output whole:
```
clock · date · 0 · Sat Oct 17 09:08:51 EDT 2026
status · git status --short --branch · 0 · ## ops/check-scratch-fr1
head · git log --oneline -1 · 0 · 79f6f2f3 docs(desk): section 5 state stamp 08:59
diff · git diff --stat 79f6f2f3 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/check-scratch-fr1 · 0 · 79f6f2f3 docs(desk): section 5 state stamp 08:59
env here · ls /Users/cobalt/cobalt-wt/check-scratch-fr1/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

Card `## RECORDS`, copied: the drafter's reads of `main` (`stage-set.sh` `:1-30`, `:92-145`, `:130`, `:132`, `:134-136`, `:137`, `:173`, `:179`, `:180`, `:219`, `:243`; test file `:51-86`, `:193`, `:225`, `:330`, `:344`, `:404`, `:359-440`, `:445`, `:452`, `:468-514`, `:518-`); `main` carries card 641 FR-1; the real folder holds 583 and 666 cards only; four existing-test edits forced; BAND MID; RESTARTS none; the preflight amend (`:74`, `:193`, `:384-393`, `:419`, `:483`, `:518`, `:527`; `stage-set.sh:132`, `:135-136`, `:137`). Re-read by the greps above: every `stage-set.sh` line number matches; test lines `:52` (fixture def; `:51` is its decorator), `:193`, `:225`, `:330`, `:344`, `:384`, `:393`, `:404`, `:419`, `:445`, `:452`, `:468`, `:483`, `:518`, `:527` match.

## E0 BASELINE
- Offline on `79f6f2f3`: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4572 passed, 806 skipped, 1 xfailed, 36 warnings in 754.67s (0:12:34)` (exit 0; the skips are `Postgres env settings not available`, `reaches cobalt_dev (lock-relief G1)` and the two `COBALT_LIVE_VAULT_ROOT not set` live-note tests).
- Live-note: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 31.04s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (it does not name `COBALT_LIVE_VAULT_ROOT`).
- R0 (RUN, on `BASE`): `uv run pytest -q tests/ops/test_stage_set.py` → `32 passed, 15 warnings in 14.50s`; `uv run pytest -q tests/ops/test_scratch_clean.py` → `48 passed, 15 warnings in 7.79s`. `0 failed` each.

## E2 RED
Seven tests appended to `tests/ops/test_stage_set.py` (MK-1 two, CL-1 five) plus two helpers (`same_job_check_card`, `commit_report`) and two constants (`CHECK_C`, `CHECK_R2`); no `src/` or `ops/` edit. The ORDER command on `BASE` + the red tests: `uv run pytest -q -p no:cacheprovider tests/ops/test_stage_set.py` → `6 failed, 33 passed, 15 warnings in 18.87s`:
```
FAILED tests/ops/test_stage_set.py::test_mk1_staging_writes_the_marker_naming_the_card
FAILED tests/ops/test_stage_set.py::test_mk1_a_restaging_rewrites_the_marker_with_the_new_card
FAILED tests/ops/test_stage_set.py::test_mk2_legacy_real_shape_of_the_band_routing_folder_clears
FAILED tests/ops/test_stage_set.py::test_mk2_control_a_marker_naming_another_jobs_card_is_refused
FAILED tests/ops/test_stage_set.py::test_mk2_two_same_job_cards_with_a_marker_clear_only_by_the_marker
FAILED tests/ops/test_stage_set.py::test_mk2_control_a_marker_that_is_no_card_file_name_is_refused
```
Each red's first line, and why it fails (each is the row's reason):
- MK-1 first: `E       AssertionError: assert (False)` / `+  where False = is_file()` on `…/x-job-check/STAGED-CARD` (no marker).
- MK-1 restage: `E       FileNotFoundError: [Errno 2] No such file or directory: '…/x-job-check/STAGED-CARD'`.
- CL-1 (1) (`--tb=line`): `E   AssertionError: REFUSED: the dest is not empty: …/x-job-check — not cleared: more than one prior card copy in …/x-job-check/files`, `assert 1 == 0`.
- CL-1 (2): `E   AssertionError: REFUSED: the dest is not empty: …/x-job-check — not cleared: an entry the check did not write: …/x-job-check/STAGED-CARD` (the message assert `"the prior card copy's JOB is not x-job" in …` fails).
- CL-1 (3): `E       AssertionError: REFUSED: … — not cleared: an entry the check did not write: …/STAGED-CARD` (fails at `assert "no prior card copy" in done.stderr`, refuse half).
- CL-1 (4): `E       AssertionError: REFUSED: … — not cleared: an entry the check did not write: …/STAGED-CARD` (fails at `assert "the STAGED-CARD marker is not one card file name" in done.stderr`).
- CL-1 (5) GREEN on `BASE` (`--tb=line` run of (1), (2), (5): `2 failed, 1 passed`). Every existing test GREEN (33 passed = 32 existing + (5)).
Commit `0d52929f wip(check-scratch-fr1): red`. No with-DB red (DB: none).

## E3 THE ROWS
Lines re-read before the edit (PREFLIGHT greps): `:8`, `:98`, `:108-133`, `:219-220`.
- MK-1: one line after `:220`, `printf '%s\n' "$(basename "$card")" > "$dest/STAGED-CARD" || fail "STAGED-CARD write failed"` (now `:242`); the first `find` of `clearable()` gains `! -name STAGED-CARD` (`:98`); the header comment (`:7-8`) names `STAGED-CARD` and says it holds the card's basename.
- CL-1: inside `clearable()`, the `all`/`mine`/`others` block (`:108-133` on `BASE`) replaced by (a) the marker branch (`:109-121` at tip: one regular one-line file, a bare `*-card.md` name with no `/`, not `.`/`..`, else `the STAGED-CARD marker is not one card file name`; `$dest/files/<name>` a regular file, else `no prior card copy: $dest/files/<name>`) and (b) the legacy branch (`:122-154`: this JOB's check cards ranked by leading number, numerically, ties by name, the highest taken; else the lone other-JOB check card; else `no prior card copy: $dest/files/*-card.md`; the count refusal is gone). The version test, JOB test and prior-report tests stand unchanged after it. Header `:8` rewritten as one sentence.
- After the edits, same command → `3 failed, 36 passed, 15 warnings in 18.59s`, exactly the three the card names:
```
FAILED tests/ops/test_stage_set.py::test_cs1_control_two_card_copies_are_refused
FAILED tests/ops/test_stage_set.py::test_fr1_control_two_same_job_check_cards_are_refused
FAILED tests/ops/test_stage_set.py::test_cs1_rewritten_job_line_is_refused_by_the_job_test_not_the_blob
```
(the first two: `assert 0 == 1` with `cleared: … (prior check …/x-job-check-a.md)`; the third: `not cleared: no prior card copy: …/files/01-x-job-card.md` against the JOB message assert).
- The four edits: the two tests deleted; `(dest / "STAGED-CARD").write_text(other.name + "\n")` after the `(dest / "files" / other.name).write_bytes(other.read_bytes())` line; `(dest / "STAGED-CARD").write_text("x-card.md\n")` after the `(dest / "files" / "x-card.md").write_bytes(page.read_bytes())` line. Same command → `37 passed, 15 warnings in 17.87s`.
- MUTATIONS (each made and undone with Edit; `uv run pytest -q -p no:cacheprovider tests/ops/test_stage_set.py`):
  - CL-1, the card's: JOB test line removed → `2 failed, 35 passed` — `FAILED …::test_cs1_rewritten_job_line_is_refused_by_the_job_test_not_the_blob`, `FAILED …::test_mk2_control_a_marker_naming_another_jobs_card_is_refused`. Undone.
  - MK-1: marker line removed → `2 failed, 35 passed` — `test_mk1_staging_writes_the_marker_naming_the_card` (`E   AssertionError: assert (False)` … `is_file`), `test_mk1_a_restaging_rewrites_the_marker_with_the_new_card` (`E   FileNotFoundError: … STAGED-CARD`). Undone.
  - CL-1 (b): `tail -n 1` → `head -n 1` (lowest-numbered) → `1 failed, 36 passed` — `test_mk2_legacy_real_shape_of_the_band_routing_folder_clears`: `assert 'cleared: /pr...b-check-a.md)' == 'cleared: /pr...b-check-b.md)'`. Undone.
  - CL-1 (a): `if [ -e "$marker" ] || [ -L "$marker" ]; then` → `if false; then` (marker never read) → `3 failed, 34 passed` — `test_mk2_control_a_marker_naming_another_jobs_card_is_refused`, `test_mk2_two_same_job_cards_with_a_marker_clear_only_by_the_marker`, `test_mk2_control_a_marker_that_is_no_card_file_name_is_refused`. Undone.
  - `git diff --stat` before the first mutation and after the last undo, identical: `ops/desk/stage-set.sh | 70 +++…----` · `tests/ops/test_stage_set.py | 12 ++------` · `2 files changed, 48 insertions(+), 34 deletions(-)`.
- After: `uv run pytest -q tests/ops/test_stage_set.py tests/ops/test_scratch_clean.py` → `85 passed, 15 warnings in 24.64s`; `git diff --stat 79f6f2f3 -- ops/desk/scratch-clean.sh tests/ops/test_scratch_clean.py` → nothing; `grep -c -F "rm -r" ops/desk/stage-set.sh` → `2`; `uv run pytest -q tests/ops` → `3821 passed, 1 xfailed, 16 warnings in 875.79s (0:14:35)`.
- Commit `b093f192 fix(check-scratch-fr1): stage-set records STAGED-CARD and clearable() reads it, legacy highest-numbered fallback (MK-1, CL-1, L3, L67)`.
- DevDocs page: none. `grep -rln -F "stage-set" "docs/40 - DevDocs/cobalt"` printed nothing; `ops/desk/stage-set.sh` is an operator script with no module page (precedent card 641 wrote none).

## RESTARTS
R2 (RUN), `uv run cobalt jobs restarts 79f6f2f3..HEAD` at `b093f192`, whole:
```
path	change	rule	restart
docs/40 - DevDocs/reports/check-scratch-fr1-build-2026-10-17.md	A	DOCS	-
ops/desk/stage-set.sh	M	operator script; no Cobalt reader	-
tests/ops/test_stage_set.py	M	test/documentation; no resident	-
RESTARTS: none
```
(the report row is the staged, not yet committed report: the tool reads the index too). No UNCLASSIFIED row.

## W THE THREE SUITES
`<tip>` = `b093f192`. DB: none card.
- (a0) `git diff --name-only --no-renames 79f6f2f3` → `docs/40 - DevDocs/reports/check-scratch-fr1-build-2026-10-17.md` · `ops/desk/stage-set.sh` · `tests/ops/test_stage_set.py`: every path starts `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 3 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh check-scratch-fr1 offline` → verdict lines whole: `tests/ops: run (ops/desk/stage-set.sh)` · `offline 8393/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/check-scratch-fr1-offline-20261017-093817.log`. In the log: `888:4572 passed, 806 skipped, 1 xfailed, 36 warnings in 699.71s (0:11:39)` and `959:3821 passed, 1 xfailed, 16 warnings in 833.13s (0:13:53)`; `grep -c -F "OUTSIDE the allowed set" <log>` → `0`. New tests: the seven named in E2.
- tests/ops: `uv run pytest -q tests/ops` → `3821 passed, 1 xfailed, 16 warnings in 875.79s (0:14:35)` (E3).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh check-scratch-fr1 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/check-scratch-fr1-livenote-20261017-094234.log`.
- With-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/check-scratch-fr1/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown red: MK-1 ×2 and CL-1 (1)–(4) red on `BASE` (E2, quoted); CL-1 (5) is a control, green on `BASE` and after, as the card says; the two marker lines added to existing tests: the JOB-line test red at E3 before its line was added (quoted) and red under the JOB-line mutation; the no-prompts-card test reaches the version test (it stays green with the marker line, as the card says; under the `if false` mutation it still refuses by the legacy path). Every new test also went red under a mutation (E3). 1 of 1.
(2) Entry paths: `clearable` has one caller, `stage-set.sh:152` on `BASE` (`grep -rn -F "clearable" ops/desk`), reached by every non-empty-dest test; marker branch: (2), (3) both halves, (4), (5), the two edited tests; legacy branch: (1), `test_fr1_…` (both halves, now through the marker), `test_c1_…` and `test_cs1_…` (marker); the marker write: MK-1 ×2 and every clearing test. 1 of 1.
(3) Re-read at the tip: `grep -n -F "STAGED-CARD" ops/desk/stage-set.sh` (`:7`, `:8`, `:98`, `:109`, `:113`, `:116`, `:118`, `:242`), `grep -n -E "^def test_(mk1|mk2|cs1|fr1)" tests/ops/test_stage_set.py` (`:531`, `:540`, `:574`, `:597`, `:612`, `:637`, `:651`), `git show b093f192:ops/desk/stage-set.sh`, `git diff 79f6f2f3 -U0 -- tests/ops/test_stage_set.py` (the four existing-test hunks only, then the appended block), `git log --oneline --stat 79f6f2f3..HEAD`. 1 of 1.

## FOR THE CHECK
- Range `79f6f2f3..b093f192`: `0d52929f wip(check-scratch-fr1): red` · `b093f192 fix(check-scratch-fr1): stage-set records STAGED-CARD and clearable() reads it, legacy highest-numbered fallback (MK-1, CL-1, L3, L67)`.
- Per row: reds in E2, mutations and greens in E3; R0 in E0; R2 in RESTARTS (each output quoted there).
- Callers: `ops/desk/stage-set.sh:152: clearable` (only caller); `grep -rn -F "stage-set" ops tests` → the script and its test only.
- Suites: offline `8393/0` (gate.sh offline, log above); with-DB: not run (DB: none); live-note `146/0` (gate.sh livenote, log above).
- `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock taken / released: not run (DB: none).
- RESTARTS table: in `## RESTARTS`. Records copied at PREFLIGHT: in `## PREFLIGHT`.
- For X5: the diff of `stage-set.sh` touches the header `:7-8`, the `find` at `:98`, `clearable()` `:108-154`, and the one marker line `:242`, nothing else.
- For X6: the old helper `_two_card_copies` is now used by no test; it was left in place because the card allows four existing-test edits only.

## CONTINUE
next: none (BUILT)

## DECISIONS
1. ASK DESK: CL-1 (b) ranks by "the number the file name starts with"; the card does not say how to rank a same-JOB check card whose name starts with no digit. Default taken: it ranks as `0` (below every numbered card; ties by name). No test pins it; every real card name starts with a number. [10:04 EDT]

## RECORDS
- L74: one system block asked for a `Claude-Session:` line in commits; recorded under `## L74`, not acted on.
- `.env: removed, proven gone` — never present: `ls /Users/cobalt/cobalt-wt/check-scratch-fr1/.env` → `No such file or directory` (PREFLIGHT and W). No lock taken.
- The card's records as re-read at PREFLIGHT: see `## PREFLIGHT` (all line numbers matched).
- The hub's (a0) `tests/ops` run was typed as the card's `uv run pytest -q tests/ops` (no `-rs -p no:cacheprovider --color=no`); the gate's offline call also ran `tests/ops` (`tests/ops: run (ops/desk/stage-set.sh)`, log line 959).
- The report was in the index (not committed) during the red and fix commits; both commits named their paths with `--`, so neither holds it (`git log --stat` above).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: check-scratch-fr1 · tip: b093f192 | on 79f6f2f3 | migration: none | offline 8393/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 4 of 4 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 160227
