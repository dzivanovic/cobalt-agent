# Preflight round 2 — card 607 `deploy-freeze-fr1` (port of 546), 2026-10-15

Read only. main HEAD at the read: `6e883218`. Card: `prompts/2026-10-15/607-deploy-freeze-fr1-card.md`, last commit `4419e75d`. 546 BASE `de0792af`, 546 last commit `b544abfb`.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff HEAD -- <card>`; `git log --oneline -2 -- <card>` | diff empty; last commit `4419e75d` | OK |
| 2 | header keys vs CARD.md (build): JOB, LADDER, BRANCH, WORKTREE, BASE, TIP, REPORT, CHECK REPORT, HOUSE B, DB, RULINGS | all present; `grep -c "«FILL"` = 0; the only empty values are `BASE:` and `TIP:` (the desk's). `CLASS`, `INSTALL`, `RESTARTS` are extra keys, as on card 546 | OK |
| 3 | FR-P1 range: `git merge-base --is-ancestor b544abfb HEAD` | exit 0 (ancestor); FR-P1 now names `de0792af..b544abfb` and says the change against the merge-base is empty | OK (issue 1 fixed) |
| 4 | PROOF per file: `git diff --stat de0792af HEAD -- <the four>`; `git ls-files` of the two new files; `git diff --stat de0792af b544abfb` | stat empty (main has not touched any of the four); the two new files are not in HEAD; branch stat: `deploy-shipped.sh` +103, `test_deploy_freeze_1014.py` +342, `pre-commit` +52/-, hub 4 lines, plus two `deploy-freeze-build-2026-10-14` reports. FR-P1 names all four with the same counts and says the two reports are not ported | OK (issue 2 fixed) |
| 5 | O1: `git show b544abfb:ops/desk/pre-commit` and `…:tests/ops/test_deploy_freeze_1014.py` | `git diff --cached --name-only --no-renames` with comment "check O1"; `test_f1_a_staged_rename_of_a_shipped_path_is_refused` present. FR-P1 O1 names both | OK (issue 3 fixed) |
| 6 | D1 prose vs `git show b544abfb:ops/desk/deploy-shipped.sh` | card: `git grep -l -e "^JOB: <JOB>$" main -- "docs/40 - DevDocs/prompts"` + `BASE: main`; the script's grep line is the same; REFUSED / exit 1 / read only / `GIT_OPTIONAL_LOCKS=0` / `LC_ALL=C` all match | OK (note 4 fixed) |
| 7 | `pre-commit` anchors, `git show HEAD:ops/desk/pre-commit` | `:1-2` begin, `:3-4` toplevel/branch, `:5-7` filter, `:8-22` live read (`:17-18` name print, `:20-21` NONE), `:23-28` NONE + UNREADABLE note, `:29-34` `*)` arm (`exit 1` `:33`), `:35-37` esac/fi/fi, `:38` end marker, `:39-52` row gate. Card F1 says `:39-52`, `:38` end marker; the b544abfb diff touches only `:3-4` and `:29-34` | OK (note 1 fixed) |
| 8 | hub anchors, `grep -n` on `DEPLOY-HUB.md` | `:11` `claude --bg ` (once), `:15` `THE DESK WHILE YOU RUN`, `:114` `- MAIN:` holding `main moved outside docs`, `:129` `- D2.0 COMMIT`, `:130` D2.1, `:132` D2.3, `:140` `4.3 ` holding `foreign commit on main` and `--ff-only`. Each once. Card H1 OLD/NEW text equals the b544abfb diff of `:15` and `:129` | OK |
| 9 | `desk-commit.sh`, `desk-launch.sh`, `restarts.py`, `test_desk_row.py` anchors | `desk-commit.sh:8-10` `COBALT_REPO_ROOT` (card `:10`, `:2-8` usage); `desk-launch.sh:2277` reminder, `:2039` prodwrite refusal, `:502-522` close refusal, `:541` reminder (card cites all four); `restarts.py:38`, `:225-228`, `:230-232`, `:245-246`; `test_desk_row.py:21` `GIT_ENV`, `:42` `git()`, `:51-66` fixture, `:225-226` hook write | OK |
| 10 | `deploy-card.sh` anchors: `grep -n` and `sed -n 36,40p` | `COBALT_REPO_ROOT` is at `:39`, `COBALT_WT_ROOT` at `:40` (`:38` is a blank line, `:34` the comment). Card D1 says `deploy-card.sh:38-39` and card RECORDS (drafter record, line 74) the same. `:618` `JOB: $name`, `:622` `BASE: main`: OK | FAIL (ISSUE 1) |
| 11 | DEPLOY PROOF counts: `git grep -c -F "deploy-shipped.sh" b544abfb -- <hub> <hook>`; card line form vs 546/537 | hub 2 lines, hook 1; the `ls` line matches; the three marker lines have the form `· before` `· after` as card 546/537 (HEAD) | OK |
| 12 | deploy smoke read names this job's JOB | `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --job deploy-freeze-fr1` = header `JOB: deploy-freeze-fr1`; build card's `BASE:` is 8 hex, so only the deploy card (`BASE: main`, `deploy-card.sh:618,622`) counts | OK (note 3 fixed) |
| 13 | allow line: new commands vs `BUILD-HUB.md:12` and `DEPLOY-HUB.md:11` | `uv run pytest`, `uv run cobalt jobs restarts` are on the build line; `sh /Users/cobalt/cobalt/ops/desk/*` is CLASS (a) (`STANDING-LIST.md:31`, `:36`) and holds `deploy-shipped.sh` in the hub and the smoke read. No new string, no `ASK DESK` needed | OK |
| 14 | X3 on the ported test file (`git show b544abfb:tests/ops/…`) | reads the hub by `startswith` prefix and `in`/`count` of phrases; every commit hash comes from a tmp repo; no whole fixed-file line, no real-repo commit, no BASE hash | OK |
| 15 | RESTARTS: card rows' paths | `ops/desk/`, `docs/`, `tests/` only; `RESTARTS: none` holds | OK |
| 16 | blockers: `ls /Users/cobalt/cobalt-wt`, `rev-parse refs/heads/ops/deploy-freeze-fr1`, report path | no worktree `deploy-freeze-fr1` nor `deploy-deploy-freeze-fr1`; branch absent (exit 1); this report did not exist before this run. The live session list was not read | OK |

## ISSUES

1. FAIL (check 10) — wrong anchor: `deploy-card.sh:38-39` in row D1 (and in `## RECORDS`, line 74) is `:39-40` on HEAD (`REPO=` `:39`, `WT=` `:40`; `:38` is blank). Does not block the build (the script's own read is `COBALT_REPO_ROOT`); one-digit fix in D1: `deploy-card.sh:39-40`.
2. NOTE — F1 (iii) still reads `git diff --cached --name-only` "as `:5`" with no `--no-renames`; the `## FIX ROUND` O1 line overrides it (byte-equal port), so a builder who reads both ports the right line.
3. NOTE — `CLASS`, `INSTALL`, `RESTARTS` header keys and the `## FIX ROUND` section are not in CARD.md's tables (same on card 546).
4. NOTE — desk work before launch: fill `BASE` (main HEAD at launch; it has moved since, now `6e883218`); `TIP` stays empty for the build; the deploy must be named `deploy-freeze-fr1` for the smoke read to find its card. Nothing in the card blocks the build or the deploy.

PREFLIGHT DONE · card: deploy-freeze-fr1 · checks: 16 · fails: 1 · ready: NO
