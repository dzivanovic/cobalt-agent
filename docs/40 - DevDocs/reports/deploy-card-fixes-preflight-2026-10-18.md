# Preflight — card 721 `deploy-card-fixes-1018` (read-only, 2026-10-18)

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt diff HEAD --stat -- <721 card>` · `git log --oneline -2 -- <721 card>` | diff empty; last commit `75dcdb5f docs(desk): R1839 cards 721 and 723 and preflight prompts` | OK |
| 2 | header vs `CARD.md` (build column) | JOB, LADDER, BRANCH, WORKTREE, BASE `279c99ce`, TIP empty, REPORT (absolute, in the worktree), CHECK REPORT empty, HOUSE B `as needed` (the launcher's form, cto-2026-10-15 LESSONS), DB `none` (both files under `ops/`, `tests/ops/`), BAND `LOW`, RULINGS `2026-10-18 R1833` all present; extra keys CLASS, INSTALL, RESTARTS. Only TIP is open (the desk's). `git diff 279c99ce HEAD --stat -- ops/desk/deploy-card.sh tests/ops/test_deploy_card.py` empty, so BASE equals HEAD for both files | OK |
| 3 | `grep -c "«FILL"` on the card; row ids read | `0`; one row, D1; no D2 | OK |
| 4 | `git show HEAD:ops/desk/deploy-card.sh`, anchors by content | `:457` JOB, `:520-521` ctip/head, `:541-542` fix-round `ctip=$fixtip`, `:550` head ancestor refusal, `:551-552` docs-only refusal, `:566-576` DEPLOY PROOF, `:585-608` trial merge, `:616-641` card text: all match. Header REFUSED list is `:8-11` (card says `:9-12`; the clause `the code tip is not an ancestor of the head;` is `:10`, inside the range). The new line lands after `:552`, so it reads `ctip` after the `:542` reassignment (X1) | OK |
| 5 | `git show HEAD:tests/ops/test_deploy_card.py`, anchors | `Desk` is `:47-130` (`run` at `:113`), alpha branch `:73-86`, SMOKE READS test `:210-222`, DEPLOY PROOF placeholders `:190-192`. Card says `:192-219`: slightly off, same tests. `restarts.py` `:38`, `:232`, `tests/` rule `:245-246`: match | OK (NOTE 2) |
| 6 | the red test recipe against `Desk` | `git merge --ff-only ops/alpha` CANNOT work: `Desk` commits "checks and cards" on `main` (`:100-101`) after `ops/alpha` branched, so `ops/alpha` is not a descendant of `main`. The merge must be `git merge --no-edit ops/alpha` (a merge commit); the tip is then an ancestor of main and the test holds. The card's wording (and RECORDS last line) says fast-forward | FAIL (NOTE 1) |
| 7 | red reason on BASE; control | BASE script never reads main: exit 0 and the card is written, so `returncode == 1` fails. Control (main's `rev-parse --short=8 main` in stderr) fails on BASE by the same test. The card's parenthesis "`assert 1 == 0` reversed" is muddled, the intended reason is clear. The existing two-job tests (control 2) cover a tip not on main | OK |
| 8 | `grep -n -i "d1"` over the test file (for `-k d1`) | no hit: `-k d1` selects only the new test | OK |
| 9 | tests pin no whole file / BASE literal | the new test asserts job name, tip, `already an ancestor of main`, main's short hash read at run time, `desk.out` absent; no hash literal, no whole-line pin | OK |
| 10 | launch-line command strings | the card holds no launch line, allow string or `--add-dir`; its `uv run pytest` sits in DEPLOY PROOF only (R411, R412) | OK |
| 11 | RESTARTS (K10) | `ops/desk/` → "operator script; no Cobalt reader" (`restarts.py:38`, `:232`); `tests/` → `:245-246` "test/documentation; no resident"; `RESTARTS: none` is consistent | OK |
| 12 | `grep -c -F "already an ancestor of main" /Users/cobalt/cobalt/ops/desk/deploy-card.sh` | `0` on main now; the card's `after 2` = header clause line + refusal line, as stated. Differs before/after | OK (NOTE 3) |
| 13 | `## DEPLOY PROOF` form | present; one marker line (`· before `0` · after `2``), one smoke line (no `· before `/`· after `), so `deploy-card.sh:567-575` yields a marker and a smoke read, no `«FILL` | OK (NOTE 4) |
| 14 | what blocks the card's own deploy | see ISSUES (B1-B3) | NOTE |

## ISSUES

- FAIL 1 (check 6): the red test's setup says `git merge --ff-only ops/alpha`; on the `Desk` fixture that exits non-zero (`main` is ahead of `ops/alpha`). Use `git merge --no-edit ops/alpha` (identity comes from `GIT_ENV`). Fix the row text and the last RECORDS line before the build, or the builder adapts it silently.
- NOTE 2: test anchors `:192-219` should read `:210-222`; header anchor `:9-12` should read `:8-11`. Harmless; the card says to re-read by content.
- NOTE 3: the header clause is appended to `:10`, which will push the line past the file's ~100-column style; if the builder wraps it mid-phrase, `already an ancestor of main` splits across two lines and the marker reads `1`, not `2`. Tell the builder to keep the phrase on one line.
- NOTE 4: the smoke read is `uv run pytest …`; `DEPLOY-HUB.md` smoke (s) says "no test runs in production" and "a test the gate ran is quoted from the gate". The hub should quote the gate's run; the line is allowed by its allowlist, so not a refusal.
- B1: the card cannot launch a check or deploy until the desk fills TIP, CHECK REPORT (and the build exists); worktree `deploy-card-fixes-1018` and branch `ops/deploy-card-fixes-1018` do not exist yet (the builder creates them).
- B2: the deploy gate demands `0 failed`; `test_llm.py`'s 9 BASE reds (cto-2026-10-15 R1598, HANDOVER PLAN (3)) are a separate defect card, outside this job. If still red on main the deploy's gate stops on them unless carried or fixed first.
- B3: no desk commit on main while a deploy hub runs; the working tree on main holds uncommitted docs edits (`git status`), and `.claude/settings.json.bak` is his. After the DEPLOYED, run `sh desk-launch.sh install-ops` (the set touches `ops/desk`).

PREFLIGHT DONE · card: deploy-card-fixes-1018 · checks: 14 · fails: 1 · ready: NO
