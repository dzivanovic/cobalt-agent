# launcher-f5 deploy card 57 — preflight (read-only, 2026-10-05)

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `git -C /Users/cobalt/cobalt rev-parse --verify fb2d95a2^{commit}` | `fb2d95a2f3612a469eee1582bb72f8fe0eb291f8` | OK |
| 1b | `git -C /Users/cobalt/cobalt rev-parse ops/launcher-fixround-1005` | `fb2d95a2f3612a469eee1582bb72f8fe0eb291f8` (the card's TIP is the head) | OK |
| 1c | `git -C /Users/cobalt/cobalt log --oneline 8d79d7c9..ops/launcher-fixround-1005 -- tests ops configs src` | empty | OK |
| 1d | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 8d79d7c9 ops/launcher-fixround-1005` | exit 0 | OK |
| 1e | `git -C /Users/cobalt/cobalt merge-base --is-ancestor a545a4d8 8d79d7c9` | exit 0 | OK |
| 1f | `tail -n 2 reports/launcher-checks-check-2026-10-05-r2.md` | `CHECK DONE · job: launcher-checks · pass: 1 · tip: a545a4d8 · … · held unfixed: 0 · open: 0 · … · ready: YES · …` | OK |
| 1g | `git diff --stat -- <check report>` · `git log -1 --format=%h -- <check report>` | empty · `6bf0b815` (committed, clean) | OK |
| 2a | `tail -n 5 reports/launcher-f5-fixround-2026-10-05.md` | last non-blank line `BUILT · job: launcher-checks · tip: 8d79d7c9 \| on 5fb0ddf5 \| migration: none \| offline 3786/0 \| with-DB 857/0 \| live-note 146/0 \| cobalt_dev: 0013 \| .env: removed \| RESTARTS: none \| rows: 1 of 1 \| self-check: 3 of 3 \| decisions: 2 · for Dejan: 0 · tokens: 179659` | OK |
| 2b | `git show ops/launcher-fixround-1005:"docs/40 - DevDocs/reports/launcher-fixround-build-2026-10-05.md"` (tail, via the saved output) | last line is the same `BUILT · … tip: 8d79d7c9 … tokens: 179659` line, identical to 2a on reading | OK |
| 2c | `git diff --stat -- <fix report>` · `git log -1 --format=%h -- <fix report>` | empty · `44c22cfa` (committed on main, unmodified) | OK |
| 2d | `grep -n -A12 "fixed_ok" ops/desk/desk-launch.sh` | rule: `"$REPORTS"/*.md) ;; *) return 1` (the cell must be an absolute path under the reports dir); then file exists, committed, clean, `ltip` ancestor of `ctip`, last non-blank line `"BUILT ·"*"tip: $ctip"*`. The card's cell `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-f5-fixround-2026-10-05.md` meets it | OK |
| 3a | `git rev-parse --verify deploy/deploy-launcher-f5-1005` | `fatal: Needed a single revision` (new) | OK |
| 3b | `git rev-parse --verify deploy-2026-10-05-launcher-f5` | `fatal: Needed a single revision` (new) | OK |
| 3c | `ls /Users/cobalt/cobalt-wt/deploy-launcher-f5-1005` | `No such file or directory` (new) | OK |
| 3d | `ls "…/reports/deploy-deploy-launcher-f5-1005.md"` | `No such file or directory` (new) | OK |
| 4 | `grep -n "^| R412 " reports/cto-2026-10-05.md` · `grep -c "^| R412 .*HIS RULING.*APPROVED"` · `git log -1 --format=%h -- reports/cto-2026-10-05.md` · `git diff --stat` on it | `109:\| R412 \| 10-05 13:16 ET \| HIS RULING: drop pre-merge (d2) … \| APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) \|` · `1` · `81da0121` · empty. R412 is the only R-number on the card's RULINGS line | OK |
| 5a | `grep -c -F "ruling_items() {" ops/desk/desk-launch.sh` (main) · after on `8d79d7c9` | `0` · `1` (card: before 0, after 1) | OK |
| 5b | `grep -c -F "tool_list() {" …` | `0` · `1` (card: 0 / 1) | OK |
| 5c | `grep -c -F "card 21 F5: a string in --disallowedTools is never a write string" …` | `0` · `1` (card: 0 / 1) | OK |
| 5d | `grep -c -F "def test_f5_the_survey_prompt_launches_on_its_rulings_row" tests/ops/test_desk_launch_prechecks.py` | `0` · `1` (card: 0 / 1) | OK |
| 5e | `git diff --stat main...8d79d7c9` | `ops/desk/desk-launch.sh \| 139`, `tests/ops/test_desk_launch_prechecks.py \| 109`; 2 files | OK |
| 5f | `git diff --stat main...fb2d95a2` | the same two files plus `docs/40 - DevDocs/reports/launcher-fixround-build-2026-10-05.md \| 71`; 3 files = the SHIPS note. Classes: operator script (no Cobalt reader), test, DOCS; no `src/` path; RESTARTS none | OK |
| 6 | `grep -n "^| # | branch" prompts/CARD.md` · `grep -n "fix report\|SHIPS" ops/desk/deploy-card.sh` | CARD.md:44 and deploy-card.sh:207 both `\| # \| branch \| code tip \| branch head \| check report \| its stop line must carry \| fix report \|`; the card's row has the same 7 columns | OK |
| 7 | `grep -c -F "«FILL" <card>` · `grep -n "^## " prompts/2026-10-05/47-deploy-launcher-fixround-card.md` | `0`; sections SHIPS, MARKERS, SMOKE READS, RECORDS match the sibling's and CARD.md's deploy shape (`MIGRATIONS: none`, so no READ-BACK). The sibling's SHIPS has 6 columns (old shape, no `fix report`); the card follows CARD.md | OK |
| 8 | `git diff --stat -- <card>` · `git log -1 --format=%h -- <card>` | empty · `44c22cfa` (card committed, clean); the fix report is in 2c | OK |

## ISSUES

None.

PREFLIGHT DONE · card: launcher-f5-deploy-57 · checks: 8 · fails: 0 · ready: YES
