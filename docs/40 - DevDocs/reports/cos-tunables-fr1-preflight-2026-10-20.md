# cos-tunables FR1 preflight — 2026-10-20

Card 933 row FR1, read only. `TIP:` of the card is `17f45d80`. The checked branch head is `ace7a92a` (`git rev-parse --short=8 ops/cos-tunables`). Main is `6e714f28`, ahead of the card's commit by desk commits only. Nothing was run but reads.

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `grep -n "^BAND" 933-cos-tunables-card.md` (card read whole) | line 12 `BAND: HIGH`; row FR1 at line 27 | OK |
| 2 | `git rev-parse --short=8 ops/cos-tunables` | `ace7a92a` (= the card's "tip `ace7a92a`") | OK |
| 3 | `git grep -n` probes.py at `ops/cos-tunables` | `COS_LABEL` :126; `cos` :135; `bootstrap_owed()` call :146; `hitl` :171; call :181; `_cos_enabled` :129. The card's `:144-147` and `:179-182` hold both calls and both OWED returns. | OK |
| 4 | `git grep -n` runner.py | `:127` "Never raises on a red."; `probe_mod.cos(ts)` :150; `probe_mod.hitl(ts)` :151 | OK |
| 5 | `git grep -n` watchdog.py | `BOOTSTRAP_OWED_PATH` :55; `BootstrapOwedError` :59; `bootstrap_owed` :63; raises at :79 and :81 (not JSON; not an object keyed by label) | OK |
| 6 | `git grep -n "def test_"` test_cos_probes.py | `test_an_unreadable_owed_file_raises_through_both_probes` :117 (body :117-127, two `pytest.raises(BootstrapOwedError)`); `test_the_runner_path_reads_the_real_row_then_the_owed_file` :130 | OK |
| 7 | `git diff --stat ace7a92a ops/cos-tunables -- tests/cobalt/test_sheet_daymode_probe.py`; `git show --stat 17f45d80` | diff empty (the tip is `ace7a92a`, so byte equality is trivially true); `17f45d80` = `tests/cobalt/test_sheet_daymode_probe.py \| 4 ++++`; the file at `ace7a92a` holds the cos/hitl stub with the owed-file comment | OK |
| 8 | FR-2 is inside P1's files | FR1 `files`: `probes.py` (`:144-147`, `:179-182` only), `test_cos_probes.py`, the admitted `test_sheet_daymode_probe.py`, `probes.md`. `runner.py` is not edited, and its `:127` docstring stands. | OK |
| 9 | FR-2 names the replaced test, red first, both cases, the other probes | Names `test_an_unreadable_owed_file_raises_through_both_probes`. Red first as `wip(cos-tunables): fr1 red`. Covers an unreadable and a malformed file (one `tmp_path` file each). Asserts the `database` probe stays in the beat. The model is check FINDING O1 (`reports/cos-tunables-check-2026-10-20.md:88-114`), which uses `_cos_enabled` (exists, :129) and the faked `sweep`. | OK |
| 10 | Commands the card gives the builder vs `BUILD-HUB.md:14` and `:16` | Everything is on the list: `uv run pytest *`, `git add/commit/show/diff/log`, `ls`, `grep`, `sh /Users/cobalt/cobalt/ops/desk/*` (`gate.sh`), `uv run cobalt jobs restarts *`. `probes.md` and the tests go through `Edit(//Users/cobalt/cobalt-wt/**)`. No `git mv`, `git rm`, `rm`, `cat` or `mkdir` in FR1. | OK |
| 11 | Dated DevDocs line (BUILD-HUB E3) | `## 2026-10-20 — cos-tunables fr1` into `probes.md` after the check section (`:151`). `:148` is the cos-tunables section and `:149` holds "`BootstrapOwedError` is not caught". | OK |
| 12 | RECORDS line carries the brain's text | Card line 69: `cos-tunables 933 fr1 — FR-1 admits tests/cobalt/test_sheet_daymode_probe.py (…); FR-2 an unreadable bootstrap-owed.json makes the cos/hitl probe red with the error, never a raise in take_beat; BAND HIGH fix round — brain 9b07db5a 2026-10-20`. The prompt's `…` is an elision, and the card holds the whole text. | OK |
| 13 | RULINGS and R2227 | The header has `RULINGS: 2026-10-18 R1863`. `git grep -F R1863 HEAD cto-2026-10-18.md:90` → "HIS RULING · APPROVED". `git grep -F R2227 HEAD cto-2026-10-20.md` → 2 hits, committed (the row is at :21). | OK |
| 14 | Stale "raises" text can mislead? | See ISSUES 2. FR1 says it supersedes, and the code (`probes.py`) holds no "raises" docstring for cos/hitl. | OK (NOTE) |
| 15 | `desk-launch.sh build` for BAND HIGH, no `git mv/rm/delete` | `desk-launch.sh:1944` HIGH → "Opus 5.5 (BUILD-HUB.md line)". FR1 has none of the three; `grep -F "git mv"` in the launcher → none. The `<resume step>` `FR1` passes the launcher's character check (`:2631`). | OK (NOTE) |
| 16 | Check after FR1 runs as JOB `cos-tunables-fr1` | The card's `## CHECK ASKS` FR1 line (card :52) names it, scoped to FR1 and the suites. | OK |
| 17 | Card committed, empty diff | `git diff --stat HEAD -- 933-cos-tunables-card.md` → empty. Last card commit `51c9e1a4` (R2228 `ccc4a461` is the desk's later commit). | OK |

## ISSUES
1. NOTE (blocks the launch until the desk acts, not a card defect): the worktree `/Users/cobalt/cobalt-wt/cos-tunables` holds an untracked `SHADOW-INSTRUCTIONS.md` (22,792 bytes, 18:34). `git status --short --branch` there gives `## ops/cos-tunables` plus `?? SHADOW-INSTRUCTIONS.md`. The launcher's build path refuses an unclean worktree (`desk-launch.sh:1993`); only the check path excuses this file (`:2146`). Remove it first with `sh /Users/cobalt/cobalt/ops/desk/scratch-clean.sh "<path>"`. I did not touch it.
2. NOTE: the card's P1 text ("An unreadable owed file raises …"), the card's `## DECISIONS`/`## RECORDS` "raises" wording, the old test at `test_cos_probes.py:117` and `probes.md:149` all still say "raises" or "not caught". They could mislead a builder who reads P1 alone. FR1 says in so many words that it SUPERSEDES P1's line and that those texts stay as context, and it names the test it replaces and the doc line it supersedes. A builder who reads the card whole gets it right. No card edit is needed. This is the drafter's decisions 1 and 2, defaults taken, and I agree with both.
3. NOTE: the launch form. The card's `desk-launch.sh build 933 FR1` is shorthand. The script's usage is `desk-launch.sh build "<absolute card path>" [<resume step>]` (`:1240`). The command is `sh /Users/cobalt/.claude/ops/desk-launch.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md" FR1`. A step makes the line start `CONTINUE: FR1.` (`:2634`) and calls `lock_free` (`:1998`). It reuses the worktree without a re-cut (`:2670`). BUILD-HUB has no `FR1` step name, but `STOP LINE` (`:113`) gives the fix round to the same card, and the precedent (prompt 900, FIX1) uses the same form.
4. NOTE: FR-1's byte-equality proof is trivial at the tip: the tip is `ace7a92a`, so `git show ace7a92a:<file>` equals the tip's file by construction. The card says the builder re-runs it on its own tip, which gives it content.
5. NOTE: the existing test at `:130` (`test_the_runner_path_reads_the_real_row_then_the_owed_file`) monkeypatches `bootstrap_owed` and stays green. It does not conflict with FR-2.

Nothing in the card blocks the build. Item 1 blocks the launch until the desk clears the file.

PREFLIGHT DONE · card: cos-tunables-fr1 · checks: 17 · fails: 0 · ready: YES
