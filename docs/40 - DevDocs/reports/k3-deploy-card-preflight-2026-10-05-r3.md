# K3 deploy card 51 — preflight r3 (2026-10-05)

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `git log -1 --format=%h -- <fix report>` / `git diff --stat -- <fix report>` | `be249b1b` / empty | OK |
| 1b | fix report last non-blank line | `BUILT · job: drc-k3 · tip: 0ebdf95e \| on 979ec797 \| …` (starts `BUILT ·`, carries `tip: 0ebdf95e`) | OK |
| 1c | check report `log -1` / `diff --stat` / last line | `a1c846ff` / empty / `CHECK DONE · … tip: 3e40359a · … held unfixed: 0 · … ready: YES · …` | OK |
| 1d | `merge-base --is-ancestor 3e40359a 0ebdf95e` | exit 0, no output | OK |
| 2 | branch report (`44e8de82`) last line vs fix report last line | identical text: `BUILT · job: drc-k3 · tip: 0ebdf95e \| on 979ec797 \| migration: none \| offline 3869/0 \| with-DB 4730/0 \| live-note 146/0 \| … decisions: 9 · for Dejan: 0 · tokens: 167460`; fix report's other claims (suites, `requires_db`, `statements` fixture, head adds the build report only) match the branch report headline and `diff --stat` | OK (compared by eye; no pipe allowed) |
| 3a | `rev-parse --short=8 drc/k3-surfaces-1004` | `44e8de82` = TIP | OK |
| 3b | `diff --stat 0ebdf95e..44e8de82 -- . ":(exclude)docs"` | empty (whole diff: build report only, 1 file) | OK |
| 4 | `grep -n R412 cto-2026-10-05.md`; log/diff on file | row R412: `HIS RULING … APPROVED`; file `be249b1b`, diff empty. RULINGS `2026-10-05 R412` | OK |
| 5a | `grep -c` on main: store.py `def superseded_stated_ids` / build.py `CALENDAR_INPUT` / test_drc_k3.py | `0` / `0` / `No such file or directory` (before matches card; `requires_db` grep on absent file: warning, no file) | OK |
| 5b | `git grep -c` at `0ebdf95e`: same strings + `requires_db` | `1` / `2` / `3` (`def test_` → 54) | OK |
| 5c | `diff --stat main...0ebdf95e` | 20 files: 7 src (aset/drc_page, aset/web, drc/build, imports, store, units, cli), 7 tests, 5 DevDocs drc pages, build report; matches SHIPS row; RESTARTS `com.cobalt.aset com.cobalt.radar` as stated | OK |
| 6a | header of seven-column table, main `CARD.md` line 44 and `deploy-card.sh` line 207 | `\| # \| branch \| code tip \| branch head \| check report \| its stop line must carry \| fix report \|` — card 51 uses the same seven | OK |
| 6b | S3 card 02 `MIGRATIONS` / `SET` | `none` / `s3`; card 51 `none` / `s3` | OK |
| 7a | `grep -c -F "«FILL"` card 51 | `0` | OK |
| 7b | `grep -n -i seam` card 51 | only the filename `test_drc_web_seam.py`; no claim the seam does not appear | OK |
| 7c | card `log -1` / `diff --stat` | `be249b1b` / empty | OK |

Notes (not fails): card 51 SHIPS prose says "20 files, plus the build report"; the 20 already include the build report. Card 02's own row is still six columns (old tip `3e40359a`); card 51 supersedes it.

## ISSUES
none

PREFLIGHT DONE · card: k3-deploy-51 · checks: 15 · fails: 0 · ready: YES
