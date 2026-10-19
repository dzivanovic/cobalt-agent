# Preflight — card 790 `f16-close-fr2` (prompt 860), 2026-10-19

Read-only. Card `prompts/2026-10-18/790-f16-close-card.md`, committed at `3cfb077d`. main HEAD at the run: `3cfb077d`.

## CHECKS

| # | command · output | OK/FAIL |
|---|---|---|
| 1 | `git merge-base --is-ancestor cb4e42ce main` → rc 0. `git log --oneline cb4e42ce..main` → 2 commits (`3cfb077d` card 790 re-head, `72a26b15` 717 amend/prompt 859). `git diff --name-only cb4e42ce main` → 8 files, all under `docs/40 - DevDocs/` (card 790, prompts 855/859/860, cto-2026-10-19, desk-wakeup-log, draft-717, draft-f16-port2). None under `src/`, `configs/` or `cobalt/cli.md`. BASE is 2 docs-only commits behind HEAD; the card says the desk refreshes BASE at launch. | OK (NOTE 1) |
| 2 | `grep -c "«FILL"` on the card → `0` | OK |
| 3 | Header: `JOB: f16-close-fr2`, `BRANCH: ops/f16-close-fr2`, `WORKTREE: f16-close-fr2`, `REPORT: …/f16-close-fr2-build-2026-10-19.md`, `CHECK REPORT: …/f16-close-fr2-check-2026-10-19.md`. `grep -o f16-close-fr1` → lines 27, 29, 31, 57 only: old SEAM row, PORT2 context text, PORT2 row (source branch), PORT2 SCOPE (earlier check). All context. `TIP:` empty (set by the build). | OK |
| 4 | `git diff --name-only 6452f70e c5eafaf1` → `cobalt/cli.md`, `cobalt/taxonomy/loader.md`, `src/cobalt/cli.py`, `src/cobalt/taxonomy/loader.py`, `tests/cobalt/test_f16_close_1018.py` = the row's 5 files, none a report. `git diff --stat 6452f70e main -- <file>`: `taxonomy/loader.py` empty, `test_f16_close_1018.py` empty, `taxonomy/loader.md` empty (3 untouched, claim true); `src/cobalt/cli.py` → `+2`; `cobalt/cli.md` → `+3` (2 touched, claim true). One PROOF line per file is named in the row's (A) list (3 files) and (B) hunks (2 files). All 5 re-proved (≤15). | OK |
| 4b | `git diff 6452f70e main -- src/cobalt/cli.py` → hunk `@@ -87,6 +87,7` adds `from cobalt.genesis import cli as genesis_cli  # noqa: E402`; hunk `@@ -553,6 +554,7` adds `genesis_cli.add_parser(sub)` after `hitl_cli.add_parser(sub)`. `git diff 6452f70e c5eafaf1 -- src/cobalt/cli.py` → one hunk `@@ -335,6 +335,26` (the 20-line F16 block). Matches the row's (1), (2), (3) hunk headers exactly. | OK |
| 5 | `git show main:"…/cobalt/cli.md"` ends with `## 2026-10-19 — f21-genesis-1013` and its line, no F16 section. `git show 57e2278c:"…/cobalt/cli.md"` is the same text plus a blank line, `## 2026-10-19 — f16-close-1018`, and the line `` `cobalt validate` builds the F23 playbook config and the F4 daily-refresh config and prints one line for each; a bad file fails loud.`` The card's three lines equal that tail, character for character. `git diff 6452f70e main --stat` on the file → `+3` (Genesis), consistent. | OK |
| 6 | Card line 29 (PORT2 JOB) says rows V1, V2, C1, FIX1, first SEAM, PORT and second SEAM "are context, NOT rebuilt"; line 33 `ORDER: launch build at PORT2 … Rows V1, V2, C1, FIX1, SEAM, PORT and the second SEAM above are the content of the port, NOT rebuilt`. The old PORT row (line 26) says "BASE = main HEAD at launch (header: 6452f70e)" but is fenced as context by lines 29 and 33. | OK (NOTE 2) |
| 7 | `## CHECK ASKS` holds P5 (`git merge-base main <tip>` → `<hash>` = `git rev-parse main` → `<hash>` proof line) and P6 (the two FIX1 tests by name, no `pptx_loaded` skip, unloads `pptx`, `cobalt.playbook.deck`, `cobalt.playbook.data`). | OK |
| 8a | `grep -n "def _cmd_validate"` cli.py → `141`. The card's context rows cite `:137`. Row PORT2 cites the cli.py lines by content (`main :337`, `:339`). | OK (context cite stale) |
| 8b | `grep -n` cli.py: `CROSS-CHECK 1` → `339`; `their plists are not bootstrapped` → `337`; `if disabled:` → `332`. PORT2 row says `:337` and `:339`. | OK |
| 8c | `def load_tunables` in loader.py → `76`; `return TunableRegistry(**raw)` → `85`. Card `:76-85`. | OK |
| 8d | `consumers: list[str] = Field(default_factory=list)` in tunables.py → `103`. Card `:103`. | OK |
| 8e | `load_tunables` import in cli.py → `150` (and `:250`). RECORDS cites `cli.py:146`. | FAIL (stale, context, NOTE 3) |
| 8f | `prefill.refresh_window` in tunables.yaml → `1148`; `prefill.refresh_interval_min` → `1160`. Scope text cites `:1084`, `:1096`. | FAIL (stale, context, NOTE 3) |
| 8g | `grep -c "^  - key:"` tunables.yaml → `100`; `grep -c "^    consumers:"` → `100`. Card says `94` and `94` (RECORDS), and "all 94" in the C1 control and in live ask X6. | FAIL (NOTE 4) |
| 8h | `src/cobalt/classify/route.py` `MIN_N = 30` → `80`. Card `:80`. | OK |
| 8i | `ops/desk/checkin-timer.sh` `PING_MAX_AGE_MIN=30` → `54`. Card `:54`. | OK |
| 8j | `def test_walk_slide_counts` in `tests/cobalt/test_playbook_offline.py` → `264`. Card FIX1 cites `:264`. | OK |
| 8k | `daily_refresh:` in `configs/cobalt/prefill.yaml` → `24`. Card `:24-26` for the block. | OK |
| 8l | `def load_playbook_config` playbook/config.py → `43`; `class PlaybookConfigError` → `22`; `def load_daily_refresh_config` prefill/config.py → `198` (card `:198-203`); `class PrefillConfigError` → `33`. | OK |
| 9 | Header carries `HOUSE B: as needed` and `RULINGS: 2026-10-18 R1841`, both unchanged by `git diff cb4e42ce 3cfb077d` (only JOB, BRANCH, WORKTREE, BASE, TIP, REPORT, CHECK REPORT changed). The header has no `RESTARTS:` or `CLASS:` line, before or after; RESTARTS is in `## RECORDS` ("class home of BOTH `src/cobalt/cli.py` and `src/cobalt/taxonomy/loader.py`") and the deploy card takes it from the build's `cobalt jobs restarts`. | OK (NOTE 5) |
| 10 | `git log -1 --oneline -- <card>` → `3cfb077d docs(desk): card 790 re-headed f16-close-fr2 (drafted), preflight prompt 860`. `git diff HEAD --stat -- <card>` → empty. The card is committed and clean. | OK |

## ISSUES
- FAIL 8g / NOTE 4: live ask X6 says "every one of the 94 real rows still loads"; `tunables.yaml` has `100` rows and `100` consumers lines on main. A check seat would chase a count that is not there. Fix: `94` → `100` in X6 (and in the C1 control and RECORDS if wanted); the C1 and RECORDS texts are context. This is the one thing to correct before the launch.
- FAIL 8e/8f / NOTE 3: stale `file:line` cites in context (`tunables.yaml:1084/:1096` now `:1148/:1160`; `cli.py:146` now `:150`). The card says to re-find by content; not a blocker.
- NOTE 1: BASE `cb4e42ce` is 2 docs-only commits behind main (`3cfb077d`), and the desk's commit of this report moves it again. P5 needs `git merge-base main <tip>` = main HEAD at the check, so the desk sets BASE to main HEAD at the launch (the card says it does) and cuts the worktree from it.
- NOTE 2: old PORT row still reads "BASE = main HEAD at launch (header: 6452f70e)". Fenced as context by lines 29 and 33, and the ORDER launches at `PORT2`. A builder reading carefully will not run it.
- NOTE 5: no `RESTARTS:` or `CLASS:` header in the card; unchanged from before this re-head.

Blocks the launch: the X6 count `94` (one-word edit).

PREFLIGHT DONE · card: f16-close-fr2 · checks: 23 · fails: 3 · ready: NO
