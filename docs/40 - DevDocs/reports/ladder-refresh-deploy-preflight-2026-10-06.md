# card 54 deploy card — preflight (2026-10-06)

Card `prompts/2026-10-06/60-deploy-ladder-refresh-card.md`; read-only; every command run by this seat. `git` = `git -C /Users/cobalt/cobalt`; `R` = `docs/40 - DevDocs/reports`.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git rev-parse --verify ed19060f^{commit}` | `ed19060f6914f95e1e38bd3b840aa2015b6e9fd3` | OK |
| 2 | `git rev-parse ops/radar-ladder-refresh-1006` (card TIP = branch head) | `ed19060f6914f95e1e38bd3b840aa2015b6e9fd3` = card TIP `ed19060f` | OK |
| 3 | `git log --oneline -7 ops/radar-ladder-refresh-1006` | `ed19060f`, `1e7fe5f2`, `94ef37fe`, `d2330003`, `7ba8880e`, `8c554d77`, `f4c4b33a` (matches the card's RECORDS) | OK |
| 4 | `git merge-base --is-ancestor ed19060f ops/radar-ladder-refresh-1006` | exit 0, no output | OK |
| 5 | `git diff --stat ed19060f..ops/radar-ladder-refresh-1006` | empty (head = code tip, nothing between, so nothing in `src`, `tests`, `configs`, `ops`) | OK |
| 6 | `git diff --stat main...ops/radar-ladder-refresh-1006` | 4 files, 483 insertions, 2 deletions: `docs/…/cobalt/aset/radar_panel.md`, `R/radar-ladder-refresh-build-2026-10-06.md`, `src/cobalt/aset/radar_panel.py`, `tests/cobalt/test_radar_panel.py` = the card's four shipped files, no `ops/`, no migration | OK |
| 7 | `grep -c -F "tickLadder" src/cobalt/aset/radar_panel.py` (main, BEFORE) | `0` (card before `0`) | OK |
| 8 | `grep -c -F "window.setInterval(tickLadder,interval)" …radar_panel.py` (main, BEFORE) | `0` (card before `0`) | OK |
| 9 | `grep -c -F "window.setInterval(refreshPool,interval)" …radar_panel.py` (main, BEFORE) | `1` (card before `1`) | OK |
| 10 | `git show ed19060f:src/cobalt/aset/radar_panel.py` then `grep -c -F "tickLadder"` (AFTER) | `2` (card after `2`) | OK |
| 11 | same, `grep -c -F "window.setInterval(tickLadder,interval)"` (AFTER) | `1` (card after `1`) | OK |
| 12 | same, `grep -c -F "window.setInterval(refreshPool,interval)"` (AFTER) | `1` (card after `1`, unchanged) | OK |
| 13 | SMOKE READS = the three marker greps above (ladder tick function ≥1, ladder timer ≥1, pool timer ≥1) | on `ed19060f`: 2, 1, 1, all ≥1; the draft's one DECISION (live proof left out) kept, not failed | OK |
| 14 | `git rev-parse --verify deploy/deploy-radar-ladder-refresh-1006` (BRANCH absent) | `fatal: Needed a single revision` (exit 128) | OK |
| 15 | `ls /Users/cobalt/cobalt-wt/deploy-radar-ladder-refresh-1006` (WORKTREE absent) | `No such file or directory` | OK |
| 16 | `git rev-parse --verify deploy-2026-10-06-radar-ladder-refresh` (TAG absent) | `fatal: Needed a single revision` (exit 128) | OK |
| 17 | `ls R/deploy-deploy-radar-ladder-refresh-1006.md` (REPORT absent) | `No such file or directory` | OK |
| 18 | `grep -n "^| R556 " R/cto-2026-10-06.md` | `\| R556 \| 14:20 ET \| HIS RULING (…): fix the empty radar screen if the brain says GO … \| HIS RULING · APPROVED \|` | OK |
| 19 | R556 committed: `git log -1 --format=%h -- R/cto-2026-10-06.md` and `git diff --stat -- <same>` | `6511d978`; diff empty | OK |
| 20 | `grep -c -F "«FILL" <card>` | `0` | OK |
| 21 | card committed and clean: `git log -1 --format=%h -- <card>` and `git diff --stat -- <card>` | `bb9c010c`; diff empty | OK |
| 22 | check report committed and clean: `git log -1 --format=%h -- R/radar-ladder-refresh-check-2026-10-06.md` | `02b15e1f` (not in `git status` as modified) | OK |
| 23 | `tail -n 3 R/radar-ladder-refresh-check-2026-10-06.md` last non-blank line | `CHECK DONE · job: radar-ladder-refresh · pass: 1 · tip: ed19060f · … · held: 11 · fixed: 11 · held unfixed: 0 · open: 0 · … · RESTARTS: com.cobalt.aset com.cobalt.radar · … · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 181164` | OK |
| 24 | build report last line (worktree `radar-ladder-refresh-1006`) | `BUILT · job: radar-ladder-refresh · tip: d2330003 \| on 8c554d77 \| migration: none \| … \| RESTARTS: com.cobalt.aset com.cobalt.radar \| …` (build tip `d2330003`, as the card says) | OK |
| 25 | RESTARTS class home for every shipped path (`src/cobalt/jobs/restarts.py:216-220`, `:225-229`, `:245-246`) | `src/cobalt/aset/radar_panel.py` → `static import reach` (`:220`); `docs/…/radar_panel.md` and the build report → `DOCS` (`:225-228`); `tests/cobalt/test_radar_panel.py` → `test/documentation; no resident` (`:245-246`). None falls to `UNCLASSIFIED` (`:260-261`). Matches the card's four-row, no-`UNCLASSIFIED` claim and `RESTARTS: com.cobalt.aset com.cobalt.radar`. `uv run` is outside this seat's tools, so the rows are read from the code, not re-run | OK |
| 26 | launcher `ops/desk/desk-launch.sh:790-872` (`ships_checked`), `:830`–`:834`: `*"$lit"\|*"$lit "*) ;;` for each backticked literal of the SHIPS cell | stop line carries `held unfixed: 0 ·` and `ready: YES ·`, each followed by a space mid-line → both literals pass | OK |
| 27 | launcher `:838` and `:858`: `ltip` from `sed 's/.* tip: \([0-9a-f]*\).*/\1/'`; `[ "$ltip" = "$ctip" ] \|\| [ "$ltip" = "$shead" ]` | the line's one `tip: ed19060f` → `ltip=ed19060f` = code tip = branch head → passes with no fix report needed (`frep` empty) | OK |
| 28 | launcher `:795-798`, `:813-816`, `:861-868`: TIP head is the row's head; head = `rev-parse --short=8 <branch>`; code tip ancestor of head; `diff --stat <ctip> <head> -- . ':(exclude)docs'` empty | TIP `ed19060f` = row head `ed19060f`; `rev-parse` shows `ed19060f`; ancestor exit 0; non-docs diff empty (check 5) → passes | OK |
| 29 | build report copy absent from main: `ls R/radar-ladder-refresh-build-2026-10-06.md` and `git log --oneline -3 main -- <it>` | `No such file or directory`; log empty. Absent, so the deploy merge adds it with no add/add | OK |

## ISSUES

None.

PREFLIGHT DONE · card: deploy-card-54-60 · checks: 29 · fails: 0 · ready: YES
