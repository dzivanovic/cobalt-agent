JOB: deploy-launcher-f5-1005
LADDER: OFF-LADDER — workflow set, cto-2026-10-05.md 2026-10-05 R387
BRANCH: deploy/deploy-launcher-f5-1005
WORKTREE: deploy-launcher-f5-1005
BASE: main
TIP: fb2d95a2
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-launcher-f5-1005.md
RULINGS: 2026-10-05 R412
TAG: deploy-2026-10-05-launcher-f5
MIGRATIONS: none
SET: workflow2

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/launcher-fixround-1005` | `8d79d7c9` | `fb2d95a2` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-checks-check-2026-10-05-r2.md` | `held unfixed: 0` and `ready: YES` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-f5-fixround-2026-10-05.md` |

Files it ships (`git -C /Users/cobalt/cobalt diff --stat main...ops/launcher-fixround-1005`, 3 files), each with its RESTARTS class: `ops/desk/desk-launch.sh` (operator script; no Cobalt reader); `tests/ops/test_desk_launch_prechecks.py` (test/documentation; no resident); the builder's report `docs/40 - DevDocs/reports/launcher-fixround-build-2026-10-05.md` (DOCS). RESTARTS: none. No `src/` path is in the diff. Only the first two are F5's; the report is the builder's own, extended by the F5 section. The head is a report-only commit above the code tip: `git -C /Users/cobalt/cobalt log --oneline 8d79d7c9..ops/launcher-fixround-1005 -- tests ops configs src` prints nothing, and `rev-parse` gives `fb2d95a2f3612a469eee1582bb72f8fe0eb291f8` for the branch. The check's tip `a545a4d8` is an ancestor of the code tip `8d79d7c9` (`merge-base --is-ancestor`, exit 0).

## MARKERS
- `grep -c -F "ruling_items() {" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · before `0` · after `1`
- `grep -c -F "tool_list() {" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · before `0` · after `1`
- `grep -c -F "card 21 F5: a string in --disallowedTools is never a write string" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · before `0` · after `1`
- `grep -c -F "def test_f5_the_survey_prompt_launches_on_its_rulings_row" /Users/cobalt/cobalt/tests/ops/test_desk_launch_prechecks.py` · before `0` · after `1`

## SMOKE READS
- `ruling_items` helper (F5) · `grep -c -F "ruling_items() {" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · exit 0, a count of 1 or more
- `tool_list` helper (F5) · `grep -c -F "tool_list() {" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · exit 0, a count of 1 or more
- prompt-kind F5 comment (deny list never a write string) · `grep -c -F "card 21 F5: a string in --disallowedTools is never a write string" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · exit 0, a count of 1 or more
- F5 test · `grep -c -F "def test_f5_the_survey_prompt_launches_on_its_rulings_row" /Users/cobalt/cobalt/tests/ops/test_desk_launch_prechecks.py` · exit 0, a count of 1 or more

## RECORDS
- launcher-f5: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-checks-check-2026-10-05-r2.md` last line: CHECK DONE · job: launcher-checks · pass: 1 · tip: a545a4d8 · house A: none (overruled 2026-10-02 R47) · findings: 5 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3786/0 · with-DB 857/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 11 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 152813
- launcher-f5: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/launcher-fixround-1005` → `fb2d95a2`; code tip `8d79d7c9` (F5, row committed `6fce2ccb`; BASE `5fb0ddf5`). The F1-F4 part of the branch is already on main (deploy `21a06ce3`); the ship is F5's two code files and the builder's report.
- fix report: `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-f5-fixround-2026-10-05.md`, a pointer record whose last non-blank line is the branch report's `BUILT · … tip: 8d79d7c9` stop line. It must be committed on main and unmodified before the launch.
- G (d2): per the sibling cards' RECORDS wording on its state at deploy time; no Grok read (R412).
- The builder's DECISIONS item 1: `tests/ops/test_desk_launch_brain.py::test_the_trees_brain_hub_line_is_printed_with_its_handover_filled` is red on the old BASE `5fb0ddf5` only. The brain ruled 10-05: ignore; already fixed on main by `c4e12797`, 66 passed; the deploy merges main. A record, not a defect.
