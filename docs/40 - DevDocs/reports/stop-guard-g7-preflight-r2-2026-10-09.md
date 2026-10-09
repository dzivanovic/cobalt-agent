# Stop-guard G7 card 164: preflight r2 · 2026-10-09
Read-only. Card `prompts/2026-10-09/164-stop-guard-g7-card.md`, main HEAD `eef792cf`. Every check re-run, none carried over.

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `desk-launch.sh:901-904` build REPORT rule vs card `REPORT:` | rule: `$WT/$wt/docs/40 - DevDocs/reports/*.md`; card: `/Users/cobalt/cobalt-wt/stop-guard-g7-1009/docs/40 - DevDocs/reports/stop-guard-g7-build-2026-10-09.md` (`WT=/Users/cobalt/cobalt-wt`, `:168`; wt `stop-guard-g7-1009`) → matches | OK |
| 2 | `need JOB LADDER BRANCH WORKTREE BASE REPORT RULINGS` (`:722`) | all seven non-empty (JOB `stop-guard-g7-1009`, LADDER `OFF-LADDER — …R724`, BRANCH `ops/stop-guard-g7-1009`, WORKTREE `stop-guard-g7-1009`, BASE `1458693d`, REPORT, RULINGS) | OK |
| 3 | JOB `[a-z0-9-]` (`:733`), BRANCH plain (`:736`), WORKTREE one name, not `agy-trial` (`:754-757`) | pass | OK |
| 4 | card path `$PROMPTS/*-card.md`, chars `[A-Za-z0-9 ._/-]`, no `..` (`:687-694`) | `…/prompts/2026-10-09/164-stop-guard-g7-card.md` passes | OK |
| 5 | no `«FILL`, `## ROWS` present (`:696`, `:897`), TAG empty (`:896`), `TIP:`/`CHECK REPORT:`/`HOUSE B:` empty, `DB: none` | pass | OK |
| 6 | `git -C … rev-parse 1458693d` · `merge-base --is-ancestor 1458693d HEAD` | `1458693dbde5371259a29c5d502d74e3878fee3b`; ancestor, exit 0 (a real main commit, `hex8` ok) | OK |
| 7 | worktree/branch (`:905-911`): `ls /Users/cobalt/cobalt-wt` · `git show-ref --verify refs/heads/ops/stop-guard-g7-1009` | no `stop-guard-g7-1009` dir; `not a valid ref` → launcher creates both | OK |
| 8 | RULINGS format (`:738`) | `2026-10-08 R685` | OK |
| 9 | `ops/authorize.sh` (named by the prompt) | the file does not exist (`ls ops`); the rule is `ruling_row` in `desk-launch.sh:245-272`, read instead (NOTE 1) | OK |
| 10 | `grep -n "^| R685 " reports/cto-2026-10-08.md` | one line, `:38`: `… HIS RULING (words R685, standing) … \| APPROVED · HIS RULING · APPLIED …`; `HIS RULING` before `APPROVED` on one line; `n=1` (`:263`); matches `:266` | OK |
| 11 | `git log -1 --format=%H -S"\| R685 \|" -- reports/cto-2026-10-08.md` | `e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c` | OK |
| 12 | `git show HEAD:…/cto-2026-10-08.md` (the `:270` exact-line test) | row at HEAD is the same line as the working tree's; the file's only working-tree change is one deleted OWED line, not R685 | OK |
| 13 | `git log -1 --format=%H -- <card>` · `git status --short -- <card>` · `git diff HEAD --stat -- <card>` | `9db1211c094f7b7e5cba3c1bdbe89fcc6ff17300`; status empty; diff empty (committed, unchanged) | OK |
| 14 | `git show 9db1211c -- <card>` | one hunk, `@@ -4,7 +4,7 @@`: one `-` and one `+` line, `REPORT: /Users/cobalt/cobalt/docs/…` → `REPORT: /Users/cobalt/cobalt-wt/stop-guard-g7-1009/docs/…`; no other line changed | OK |
| 15 | `git diff --stat 1458693d HEAD -- ops/desk tests/ops/test_stop_guard.py` and `git diff HEAD --stat -- ops/desk tests/ops/test_stop_guard.py` | both empty: every `file:line` is BASE's and HEAD's | OK |
| 16 | `stop-guard.py` cites, read at HEAD: header `:20-26` (OWED block, `waiting on Dejan`); constants `:89-96`; `owed_block` `:198-241`; `listed` `:244-255` (`rows`/`return` at `:254-255`); `unsettled` `:269-292` (docstring `:270`; `if marker == WAITING: continue` `:274-275`; `# the desk cannot name itself` `:288`, `any(i.startswith(sid) and name != "cto-desk" …)` `:289`); `desk` `:295`, `:310` missing-block line, `:313-317`; `worker` `:353`; count and give-up `:295-330`; INSTALL Stop entry `:47` | all match | OK |
| 17 | `test_stop_guard.py` cites: `Desk.owed` `:306` (`*block, heading=`, no `rows`); `:456`; `:564`; `:409` `fold R1`; `:675`; `:464`; `:480`; `ROW :267`; `lister :315`; `grep -n "waiting on Dejan"` | `:409 :456 :564 :586 :587 :675` only, each as the card says (`:586-587` raise at parse, `:675` fails open); `:456` and `:564` carry no `R<n>`, so T0 touches every test (b) would turn red; no test reads a QUEUE row or a `brain` lister row (`grep -n "QUEUE\|brain"`: only cwd tests `:109`, `:372`) | OK |
| 18 | `grep -n -- "--name" prompts/BRAIN-HUB.md` | `8: … --remote-control brain --name brain …` | OK |
| 19 | `desk-list.sh:3`, `:16` | `:3` `id · name · cwd · status · state`; `:16` `print(a['id'], a.get('name','?'), …, sep=' · ')` | OK |
| 20 | scope vs brief `## CARD ROW` (G7 a, b, c) | (a) QUEUE row → `start it: <prompt cell>`; (b) no `R<digits>` → `start it: ask him: <what>`; (c) `brain` id settles only a `brain` item. Reds: `\| QUEUE \| — \| x card` + `owed: none`; `OWED: build 72 \| waiting on Dejan`; `OWED: launch https card \| live: <brain id>` + a `brain` row. Controls: `OWED: Finviz rate D2 (asked R722) \| waiting on Dejan`; `OWED: brain checks card 134 draft \| live: <brain id>`. All present with exit 0 on BASE / 2 after; `## NOT IN THIS JOB` fences the rest; T0's two edited tests are needed by (b) | OK |
| 21 | check line: `grep -n "A desk stop is blocked"` in card and in prompt `163` | card `:37` X1 = prompt `163:5` text, identical. The brief `desk-idle-answer-2026-10-09.md` itself holds no such line (NOTE 2) | OK |
| 22 | K25, each red on BASE by reading `stop-guard.py` | (a) `owed: none` → `owed_block` `[]` → `unsettled([])` None → exit 0, the table never read; (b) `marker == WAITING` settles → 0; (c) `f20cc306-0000 · brain` matches `startswith("f20cc306")`, `SESSION_ID` fullmatch, name not `cto-desk` → settled → 0. After: (a) 3rd cell of `\| QUEUE \| — \| x card \| — \| x \|` is `x card`; (b) `ask him: build 72` printed by `"start it: %s"` (`:317`); (c) `"brain" not in "launch https card"` → unsettled. Controls: `\bR\d+\b` matches `R722`; `"brain" in "brain checks card 134 draft"`; both exit 0 on BASE (waiting settles; any non-`cto-desk` row settles). Both mutations turn their control red. `:464` (`b43daef9 · x-job-build`) and `:480` (`cto-desk`) unchanged | OK |
| 23 | offline: `Desk` fixture (tmp_path, fake `desk-list.sh`, `python3` subprocess); G7a/b read no list, no `pgrep` | no network, no DB, no production command | OK |
| 24 | new commands (R411, R412) | card runs `uv run pytest -q -p no:cacheprovider tests/ops/test_stop_guard.py`, the deploy gate, `uv run cobalt jobs restarts <BASE>..HEAD`: all existing | OK |
| 25 | RESTARTS: `grep -c -F "ops/desk" configs/cobalt/jobs.yaml` | `0`; `## RECORDS` gives one class per path: `stop-guard.py` operator script, `test_stop_guard.py` test, report DOCS | OK |
| 26 | `## RECORDS` QUEUE cite: `grep -n QUEUE reports/cto-2026-10-09.md` | only `:17` (the R724 row's "no QUEUE rows"); the three table QUEUE rows the card cites at `:35-37` are gone (NOTE 3) | NOTE |

## ISSUES
- NOTE 1: the prompt names `ops/authorize.sh` lines 84-122; no such file exists. The ruling rule is `ruling_row`, `desk-launch.sh:245-272`; checks 8-12 apply it.
- NOTE 2: the check line is verbatim from prompt `163`, not from the brief; the card holds it in `## CHECK ASKS` X1 (CARD.md has no `## CHECK`).
- NOTE 3: `## RECORDS` says today's report holds three `QUEUE` rows (`cto-2026-10-09.md:35-37`) that will block after the deploy. They are gone: the desk has already turned them into OWED lines (R724). A stale record, not code; the build is unaffected. Fix or drop the line when the card is next touched.
- NOTE 4: main is `eef792cf`, not BASE `1458693d`; nothing under `ops/desk`, `tests/ops/test_stop_guard.py` or `desk-list.sh` moved, so the cites hold. ORDER: if the https-only build (card 156) merges first, re-run `git diff --stat 1458693d main -- ops/desk tests/ops/test_stop_guard.py` before the launch.
- The previous FAIL (check 0a, `REPORT:` a main path) is fixed by `9db1211c`, which changed only that line (check 14). No FAIL remains.

PREFLIGHT DONE · card: stop-guard-g7-1009 · checks: 26 · fails: 0 · ready: YES
