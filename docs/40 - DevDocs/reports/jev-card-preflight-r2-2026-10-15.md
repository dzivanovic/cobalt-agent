# Card 591 `jev-shadow-1015` — preflight round 2 (2026-10-15)

Read-only; this is the one file written. Card commit `e11791ed`. `main` since `3591d1b0`: only `tests/ops/test_card_template_1014.py` moved (`git diff --stat 3591d1b0 HEAD -- src configs tests ops`), so every cited `main` line still holds. Trial tip `f4e8de85`.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff HEAD --stat -- <card>`; `git log --oneline -3 -- <card>` | diff empty; last commit `e11791ed` | OK |
| 2 | header vs `CARD.md` (`grep -n -E "^KEY:"`) | `JOB LADDER BRANCH WORKTREE REPORT RULINGS` and `RESTARTS` filled; `BASE`, `TIP`, `HOUSE B` empty (the desk's); `CHECK REPORT` already set (harmless); `RULINGS` holds R42, R1112, R1467, R1532, R1535, no R1580 | OK |
| 3 | `grep -n -o -E "«FILL…\|TBD\|TODO\|<[A-Z]…>"` | only `<BASE>` (`:42`, `:44`) and the format words `<YYYY-MM-DD>` (`:36`, `:38`); no `«FILL` | OK |
| 4 | `main` anchors (`config.yaml`: no `^llm:`, `openrouter` only `:38 :57 :59 :61 :63`, `active_profile:` `:78`); main unchanged since `3591d1b0` | hold | OK |
| 5 | trial-tip anchors (`git show f4e8de85:src/cobalt/classify/collector.py` read whole: `_is_number`, `_send`, `_classify`, `ClassifyError`, `ClassifyAuthError`, `OpenRouterClassifier`) | symbols and behaviour as the card names them; hand-counted drift is NOTE 5 | OK |
| 6 | P0 file list vs `git diff --name-only HEAD...f4e8de85 -- docs tests/fixtures` | 7 classify DevDocs + `cli.md`, 5 JSON fixtures + `_classify_fixtures.md` — all named in P0; the 5 trial reports are excluded ("the trial's reports") | OK (round 1 issue 2 fixed) |
| 7 | P0 PROOF: main's lines plus the trial's hunks only | `src/cobalt/cli.py` (`+2`) and `cli.md` (`+11`) keep main's lines; per-file `git diff f4e8de85 -- <file>` empty or hunks named by row; the one dropped hunk is `test_the_wrapper_is_secret_free_and_execs_the_cli`, quoted from the brain's ruling | OK (round 1 issue 1 fixed) |
| 8 | P0 suites can go green | the only ported test that read an unported file was the wrapper test (round 1 check 11); it is dropped by name and the order of the second GREEN command ends `0 failed`; the later wrapper card brings it back | OK |
| 9 | no `ops/` wrapper ported (F12) | P0 "Not ported: `ops/run_classify_trial.sh`"; F12 builds no `ops/` file; control `test_f12_no_route_wrapper_in_ops` | OK |
| 10 | row D2 test file | `test_d2_a_400_digit_cost_never_raises_overflow` in `tests/cobalt/test_jev_shadow_1015.py`; `_is_number` is `math.isfinite(x)` after the `int/float` check, so `10**400` raises `OverflowError` out of `_classify`; guard-only fix, only if red | OK |
| 11 | classify rows' red on the P0 port; F13's on BASE | WHY: D2, F2-F12, J1, J2 read RED on BASE+P0; F13's reds on BASE; ORDER quotes the test file on the P0 port; the test file imports `cobalt.classify.route` lazily, so F13's reds fail for their own reason | OK (NOTE 3) |
| 12 | Z0 and its STOP clause open F13 | Z0 is first in ORDER; F13 opens with the STOP clause (covers `llm.py:115`, (a), (b)); Z0 quotes `config.yaml`, `config.py:104-107 :272 :280`, `llm.py:46-70`, every `LLM(` per `RESTARTS` service; STOP line `FAILED: DECISION <text>` | OK (NOTE 4) |
| 13 | no 74-READY wait; F12 keyed-run wait stays | WHY: "check `74` is dropped (R1580) … the build waits for no other check"; F1 edits design `:48` to drop it; keyed runs wait for his yes on F12 (`:17`, `## NOT IN THIS JOB`) | OK (round 1 note 10 fixed) |
| 14 | each row's red test names its failing reason | every `RED on …` names the assertion or the error (no module, `OverflowError`, `0.0`, argparse exit 2, `spend cap` not raised, the key injected); Z0, R1, R2 are `—` RUN rows | OK |
| 15 | R1472: no test pins a whole file, a commit-equal fixed-file line or a BASE literal | THE TEST RULE in `:17`; tests build their own tmp repo; ORDER ends with `grep -n -E -e "git show" -e "[0-9a-f]{8}"` over the test file | OK |
| 16 | card commands vs the desk's allow line (R411, R412) | build commands are `uv run pytest`, `uv run cobalt jobs restarts`, `git diff`/`git show`, `ls`, `grep`; R1 carries `ASK DESK 18` (the dry run is the J1 test; the builder only `ls`es the card list); `ls /Users/cobalt/.cobalt/classify` is `ASK DESK 19` and left to the desk (round 1 issue 5 fixed) | OK |
| 17 | `## DEPLOY PROOF` lines 79-82 | `ls` and `grep -c -F` markers with fixed `before` / `after` values; line 81 `after` is the path itself (round 1 issue 11 fixed for the old line) | OK |
| 18 | `## DEPLOY PROOF` line 83 | `grep -c -E "^spend_ledger:" …/trial.yaml` — `CARD.md` allows `ls <absolute path>` or `grep -c -F "<fixed string>" <absolute path>` only (`-E` is not `-F`); its `before` cell also carries a parenthetical after the value | FAIL |
| 19 | deploy lines 84-86 | no `· before`/`· after` pair, so each is a smoke read, not a marker (`deploy-card.sh:572-573`); the `~/.cobalt` read is outside `/Users/cobalt/cobalt` and is a smoke read | OK |
| 20 | K10: each row's files hold its RESTARTS class home | `RESTARTS:` `com.cobalt.agent com.cobalt.radar` matches `jobs.yaml:159` (agent imports `cobalt_agent.main`) and `:203` (radar imports `cobalt.cli`); `configs/cobalt/classify/*.yaml` is `UNCLASSIFIED CONFIG`, so `configs/cobalt/jobs.yaml` is named in R2's files (the build fixes it there, BUILD-HUB `## RESTARTS`); P0, F2, J1 do not name it | OK (NOTE 6) |
| 21 | round 1 notes 3, 9, 10 re-checked | note 3(c) fixed (lazy import in `:17`); note 9 fixed (F2's fixture line runs after the load via `model_copy`; F13 test (3) sets `active_profile` in the tmp `config.yaml`); note 10 fixed (F1 edits design `:48`); note 3(a)/(b) stand (NOTE 3) | OK |

## ISSUES

1. FAIL 18 — DEPLOY PROOF line 83 (`grep -c -E "^spend_ledger:" … trial.yaml`): `CARD.md` allows only `ls` or `grep -c -F "<fixed string>"` for a marker, and the `before` cell carries trailing text (`(the trial package is not on `main`)`) after the value. Fix: `grep -c -F "spend_ledger:" /Users/cobalt/cobalt/configs/cobalt/classify/trial.yaml` · before `No such file or directory` · after `<n>` (the builder's value, quoted after F2), with the parenthetical moved to `## RECORDS`.
2. NOTE 3 — (a) the WHY's RED list omits F1 (its red is "no file", so it reads RED on the P0 port too); (b) the controls read "GREEN on `BASE` and after", but on BASE a classify control cannot import: it is GREEN on the P0 port only. Neither blocks the build.
3. NOTE 4 — Z0's stop line `FAILED: DECISION <text>` follows BUILD-HUB's `FAILED: <step> — <reason>` loosely (no step name and no ` — `); it starts `FAILED:`, which the watch reads. Naming it `FAILED: Z0 — DECISION <text>` would fit the shape.
4. NOTE 5 — hand-counted drift on the trial tip: the door test's ledger line reads `:348`, the card says `:346`; the probe report's `1.3188e-05` row is `:57`, the card says `:56`. The builder re-reads by content (E3); no edit needed.
5. NOTE 6 — R2's `jobs.yaml` entry is "only if `UNCLASSIFIED CONFIG`", which `restarts.py:258` makes certain for `trial.yaml` and `route.yaml`; R2's files hold `configs/cobalt/jobs.yaml` either way.
6. NOTE — LADDER cites `cto-2026-10-15.md` for R1467; RECORDS proves R1467 in `cto-2026-10-14.md:17`; RULINGS is correct. Cosmetic.
7. BLOCKS (build): nothing, but Z0 may STOP the build before F13 by design; `BASE`, `TIP`, `HOUSE B` are the desk's to fill. BLOCKS (deploy): issue 1 (the marker form), then the F12 keyed-run wait for his yes.

PREFLIGHT DONE · card: jev-shadow-1015 · checks: 21 · fails: 1 · ready: NO
