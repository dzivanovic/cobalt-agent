# needs-his-hand-1012 — build report 2026-10-12

## §0 Headline
- Row N1 is built. `CLOSE-HUB.md` names `## NEEDS HIS HAND` once in its report shape, between `## DECISIONS` and `## RECORDS`, and gains one line after `:34`. `DAY-OPEN-QWEN.md` gains one line after `:28`. No launch line, allow string or deny string changed.
- New `tests/ops/test_needs_his_hand.py`: 8 cases from 5 tests. All 8 were red on base; 5 mutations each turned at least one red.
- Suites on tip `ad73d04a`: offline 4199/0, live-note 146/0, `tests/ops` 3143 passed. DB: none, so no lock was taken. RESTARTS: none.
- One decision, not his: the close chain keeps the file's backtick spelling (`` `## DECISIONS` → `## NEEDS HIS HAND` → `## RECORDS` ``).

## L74
A system block in this session asked for a `Claude-Session:` line on commits. Recorded once here as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/393-needs-his-hand-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/393-needs-his-hand-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/393-needs-his-hand-card.md" · 0 · 3944cfd1928150a204980010a90b945e0b67b074
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/393-needs-his-hand-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 13:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| mechanical rows | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` | 0 | see block below |
| base | `git show --stat 6468fb5e` | 0 | `6468fb5e docs(desk): rename drafter prompts 387 390 391, the launcher refuses a card-named prompt` — 3 files changed, 3 insertions(+), 3 deletions(-) (renames 387, 390, 391) |
| symbol | `grep -n -F "## REPORT (L48)" CLOSE-HUB.md` | 0 | `33:## REPORT (L48)` |
| symbol | `grep -n -F "## RECORDS" CLOSE-HUB.md` | 0 | hits 22, 29, 30, 34, 59; `34:` is the shape line, ending `… → ## CONTINUE → ## DECISIONS → ## RECORDS → the stop line. …` |
| symbol | `grep -n -F "Table: check \| verdict" DAY-OPEN-QWEN.md` | 0 | `28:Table: check \| verdict PASS/FAIL/KNOWN/ERROR \| one-line evidence. … Last line: NEXT: the desk reads this report and states the plate. Write the report, print the table, stop.` |
| symbol | Grep tool `day-open verdict` in DAY-OPEN-QWEN.md | — | `9:If exit 0: run COBALT_ENV=production uv run cobalt day-open … COBALT_ENV=production uv run cobalt day-open verdict "SEAT VERDICT: …" …` |
| symbol | `grep -n -F "def tools(" tests/ops/test_hub_lines.py` | 0 | `60:def tools(line: str, option: str) -> list[str]:` |
| callers | `grep -rn -F "CLOSE-HUB" tests ops` | 0 | `tests/ops/test_desk_size_guard.py:226`, `tests/ops/test_stop_guard.py:406`, `tests/ops/test_desk_launch_prechecks.py:46`, `:86`, `tests/ops/test_bare_guard.py:1365`, `ops/desk/desk-launch.sh:80`, `:445`, `:535` |
| callers | `grep -rn -F "DAY-OPEN-QWEN" tests ops` | 1 | nothing |
| not yet carried | `grep -rn -F "NEEDS HIS HAND" "docs/40 - DevDocs/prompts" tests ops` | 0 | only `prompts/2026-10-12/391-draft-needs-his-hand.md:3` and `:4` |
| wc -l | `wc -l CLOSE-HUB.md DAY-OPEN-QWEN.md tests/ops/test_hub_lines.py` | 0 | 65 · 29 · 241 |
| wc -c BEFORE | `wc -c CLOSE-HUB.md DAY-OPEN-QWEN.md` | 0 | 14948 · 3576 |
| READ tail | `tail -n 3 ".../reports/hands-off-answer-2026-10-12.md"` | 0 | last line: `hands off 2026-10-12 brain: standing: … Cards C1 cleanup, C2 survey, C3 production-write seat, C4 NEEDS HIS HAND, C5 sheet changes.` |
| RESTARTS | `uv run cobalt jobs restarts 6468fb5e..HEAD` | 0 | `path	change	rule	restart` / `RESTARTS: none` (empty range) |

```
clock · date · 0 · Mon Oct 12 06:18:14 EDT 2026
status · git status --short --branch · 0 · ## ops/needs-his-hand-1012
head · git log --oneline -1 · 0 · 6468fb5e docs(desk): rename drafter prompts 387 390 391, the launcher refuses a card-named prompt
diff · git diff --stat 6468fb5e · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/needs-his-hand-1012 · 0 · 6468fb5e docs(desk): rename drafter prompts 387 390 391, the launcher refuses a card-named prompt
env here · ls /Users/cobalt/cobalt-wt/needs-his-hand-1012/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

Card records, re-read:
- HEAD `6468fb5e`: preflight `head` row above. Same.
- Line counts 65 and 29: `wc -l` above. Same.
- Launch line `CLOSE-HUB.md:10`, 21 allow / 11 deny (`:12` "THE LIST: 21 allow, 11 deny"): read whole (Read tool). Same.
- Shape chain `:34`; `Table:` `:28`; `/no_think` `:29`: greps and Read above. Same.
- `NEEDS HIS HAND` in no prompt: grep above. Same.
- R1138 `HIS RULING · APPROVED`: the card cites `reports/cto-2026-10-12.md:12`; the grep finds the row at `:13`. The row's text is as the card says; only the line number differs.
- `tools` helper `test_hub_lines.py:60-70`, `hub_line` `:54-57`: Read above. Same.
- Other tests naming CLOSE-HUB: the five hits the card lists. Same.
- RESTARTS: `restarts.py:225`, `path.startswith("docs/")`; the card cites `:225-228`. Same.

DB: none. No lock probe was run.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `4199 passed, 800 skipped, 1 xfailed, 36 warnings in 675.04s (0:11:15)`. 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 30.05s`. The one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. It does not name `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_needs_his_hand.py` on base → `8 failed, 15 warnings in 0.88s`. First line of each red:
- `test_the_section_is_named_once_in_each_file[CLOSE-HUB.md]` / `[DAY-OPEN-QWEN.md]` → `AssertionError: assert 0 == 1` (`count('## NEEDS HIS HAND')`). The row's reason: count 0.
- `test_the_entry_shape_is_written_once_byte_for_byte[CLOSE-HUB.md]` / `[DAY-OPEN-QWEN.md]` → `AssertionError: assert 0 == 1` (`count('what was blocked · … · what it unblocks')`). The row's reason: count 0.
- `test_the_four_rules_stand_in_the_one_line[CLOSE-HUB.md]` / `[DAY-OPEN-QWEN.md]` → `AssertionError: CLOSE-HUB.md: 0 lines hold the entry shape` / `DAY-OPEN-QWEN.md: 0 lines hold the entry shape`. The row's reason: no line holds `SHAPE`.
- `test_the_section_sits_where_the_text_puts_it` → `AssertionError: assert '`## DECISIONS` → `## NEEDS HIS HAND` → `## RECORDS`' in '`<REPORT>`, shaped: …'`. The row's reason: the chain lacks the name.
- `test_nothing_else_changed` → `AssertionError: CLOSE-HUB.md` / `assert 65 == 66`. The row's reason: the line count. The test stops at its first assert, so its launch-line parts were not shown green on base. They are shown green at the tip, and M4 shows one of them turning red.

No with-DB red and no RUN row. Commit `cd13e4e8 wip(needs-his-hand-1012): red`.

## E3 THE ROWS
N1, the edits (`git diff 6468fb5e -- <the two prompts>`):
- `CLOSE-HUB.md:34`: the chain `… → `## DECISIONS` → `## RECORDS` → the stop line` became `… → `## DECISIONS` → `## NEEDS HIS HAND` → `## RECORDS` → the stop line`. Nothing else on the line changed.
- `CLOSE-HUB.md:35` (new): `The NEEDS-HIS-HAND section: `none` when nothing is owed; else one entry per item: what was blocked · by which rule or tool · why no seat could do it · the exact line he types · what it unblocks. Work around the blocked ITEM, never around a permission check. An item for his hand is raised by day only; at night it waits in this section and the rest runs.`
- `DAY-OPEN-QWEN.md:29` (new; `/no_think` is now `:30`): `Above that last line the report carries `## NEEDS HIS HAND` (on the S0 path too: append it to the file the command wrote): `none` when nothing is owed; else one entry per item: what was blocked · by which rule or tool · why no seat could do it · the exact line he types · what it unblocks. Work around the blocked ITEM, never around a permission check. An item for his hand is raised by day only; at night it waits in this section and the rest runs.`

Green: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_needs_his_hand.py tests/ops/test_hub_lines.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_bare_guard.py tests/ops/test_stop_guard.py tests/ops/test_desk_size_guard.py` → `2127 passed, 1 xfailed, 15 warnings in 147.66s (0:02:27)`.

Size (`wc -c`), before → after:
- `CLOSE-HUB.md`: 14948 → 15331, +383 bytes. That is the new line plus the 22 bytes of `` `## NEEDS HIS HAND` → `` in the chain.
- `DAY-OPEN-QWEN.md`: 3576 → 4030, +454 bytes. That is the new line.

Line counts (`wc -l`): 66 and 30.

THE MUTATIONS. Each was made with Edit, run with `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_needs_his_hand.py`, then undone with Edit:
- M1, the new CLOSE line removed → `4 failed, 4 passed`. First failure: `test_needs_his_hand.py:58: AssertionError: assert 0 == 1` (shape count, CLOSE-HUB). The others: `CLOSE-HUB.md: 0 lines hold the entry shape` (×2) and `assert 65 == 66`.
- M2, `` `## NEEDS HIS HAND` → `` removed from the chain → `2 failed, 6 passed`. Failures: `test_needs_his_hand.py:53: AssertionError: assert 0 == 1` (section count, CLOSE-HUB) and `:73` (the chain).
- M3, the new day-open line removed → `5 failed, 3 passed`. First failure: `test_needs_his_hand.py:53: AssertionError: assert 0 == 1` (section count, DAY-OPEN-QWEN). The last: `assert 29 == 30`.
- M4, the negative control: `"Bash(git push*--all*)"` removed from the launch line `CLOSE-HUB.md:10` → `1 failed, 7 passed`: `test_needs_his_hand.py:90: assert 10 == 11`.
- M5, `by day only` weakened to `by day` on the day-open line → `1 failed, 7 passed`: `test_needs_his_hand.py:66: AssertionError: DAY-OPEN-QWEN.md: 'by day only' missing from the shape line`.

After the undos, `git diff 6468fb5e -- <the two prompts>` shows only the three changed lines above, and `tests/ops/test_needs_his_hand.py` → `8 passed, 15 warnings in 0.82s`. No test stayed green under its mutation, so none was rewritten.

DevDocs: no module under `src/` changed, so no page under `docs/40 - DevDocs/cobalt/` gets a line. The card's `files` fence names only the two prompts and the test.

Commit `ad73d04a feat(needs-his-hand-1012): NEEDS HIS HAND section in the close and day-open prompts (N1, L81, L1, L28)`.

## RESTARTS
`uv run cobalt jobs restarts 6468fb5e..HEAD` → whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CLOSE-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md	M	DOCS	-
docs/40 - DevDocs/reports/needs-his-hand-build-2026-10-12.md	A	DOCS	-
tests/ops/test_needs_his_hand.py	A	test/documentation; no resident	-
RESTARTS: none
```
Nothing is UNCLASSIFIED.

## W THE THREE SUITES
Tip `ad73d04a`.
- (a0) `git diff --name-only --no-renames 6468fb5e` → `docs/40 - DevDocs/prompts/CLOSE-HUB.md`, `docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md`, `tests/ops/test_needs_his_hand.py`. Every path starts with `docs/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 3 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh needs-his-hand-1012 offline` → exit 0, `offline 4199/0`. Log: `/Users/cobalt/cobalt-wt/.gate-logs/needs-his-hand-1012-offline-20261012-063434.log` (`:879` `4199 passed, 800 skipped, 1 xfailed, 36 warnings in 694.34s (0:11:34)`). The offline suite (`tests/cobalt`, `tests/taxonomy`) holds no test this build adds. The added tests run under `tests/ops` below.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh needs-his-hand-1012 livenote` → exit 0, `live-note 146/0`. Log: `/Users/cobalt/cobalt-wt/.gate-logs/needs-his-hand-1012-livenote-20261012-064623.log` (`:57` `146 passed, 1 skipped, 15 warnings in 29.10s`). The one skip, `:56`: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. It does not name `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3143 passed, 1 xfailed, 15 warnings in 624.09s (0:10:24)`. This includes the 8 new cases of `tests/ops/test_needs_his_hand.py`.
- with-DB: not run (DB: none). (b)–(d) and (f) were not run.

## PRE-STOP SELF-CHECK
(1) Every added test was shown red for its named reason. All 8 cases were red on base (E2). Each fix part turned at least one red under a mutation: M1 the close line, M2 the chain, M3 the day-open line, M5 one rule. The launch-line pin turned red under M4. No test stayed green, so none was rewritten.
(2) Every entry path is pinned:
- The two prompts are read by the seats themselves. `grep -rn -F "DAY-OPEN-QWEN" tests ops` finds nothing.
- `grep -rn -F "CLOSE-HUB" tests ops` hits `ops/desk/desk-launch.sh:445`, which reads the one `claude --bg ` line. `test_nothing_else_changed` pins that line: count, 21/11, `dontAsk`, no `NEEDS` (M4 red).
- The test hits at `test_desk_size_guard.py:226`, `test_desk_launch_prechecks.py:46/:86`, `test_stop_guard.py:406` and `test_bare_guard.py:1365` use constructed files or the launch line. They are green at the tip (the 2127 run, then the 3143 run).
- The card's X4 asks the check whether any of them reads the shape chain or the `Table:` line.
(3) Re-read at the tip:
- `grep -n -F "NEEDS HIS HAND"` over the two prompts → `CLOSE-HUB.md:34` and `DAY-OPEN-QWEN.md:29`, one hit each.
- `wc -l` → 66 and 30.
- `git show ad73d04a:tests/ops/test_needs_his_hand.py` → the file as quoted.
- `git log --oneline 6468fb5e..HEAD` → `ad73d04a`, `cd13e4e8`.

## FOR THE CHECK
- Range `6468fb5e..ad73d04a`:
  - `cd13e4e8 wip(needs-his-hand-1012): red`
  - `ad73d04a feat(needs-his-hand-1012): NEEDS HIS HAND section in the close and day-open prompts (N1, L81, L1, L28)`
- N1: reds in `## E2 RED`, mutations M1–M5 in `## E3 THE ROWS`, greens (8 passed; 2127 passed; 3143 passed) quoted above.
- Caller greps: in `## PREFLIGHT`.
- RUN rows: none.
- Suites:
  - offline `4199/0` (`gate.sh … offline`)
  - live-note `146/0` (`gate.sh … livenote`)
  - `tests/ops` `3143 passed, 1 xfailed`
  - with-DB: not run (DB: none)
- F0 / F1 / F2: not run (DB: none). Lock taken / released: not run (DB: none).
- RESTARTS table: in `## RESTARTS`.
- Records copied at PREFLIGHT: in `## PREFLIGHT`.
- X1: `SHAPE` appears byte for byte, once in each file (tests 2 and 3).
- X2: the diff is the three lines in `## E3`. `CLOSE-HUB.md:10` is not in the diff.
- X3: each added sentence says "never around a permission check" and "raised by day only; at night it waits in this section".

## CONTINUE
next: CLOSE (done)

## DECISIONS
- ASK DESK: Should the close chain carry the new name in the file's backtick spelling? [06:57 ET] THE TEXT writes the chain `… → ## DECISIONS → ## NEEDS HIS HAND → ## RECORDS → the stop line` without inner backticks, but every name on `CLOSE-HUB.md:34` is backticked (`` `## DECISIONS` → `## RECORDS` ``). The safe default taken: insert `` `## NEEDS HIS HAND` → `` in that same spelling. This changes only the one insertion and no other byte of the line. Test 4 pins `` `## DECISIONS` → `## NEEDS HIS HAND` → `## RECORDS` ``. Not his.

## RECORDS
- REFUSED, not needed: grep -n -F "## DECISIONS` → `## RECORDS` → the stop line" CLOSE-HUB.md — "NOT A REFUSAL. Dejan's rule: one bare command per call, and this call contains a backtick." Resent without a backtick.
- REFUSED, not needed: grep -n -F "COBALT_ENV=production uv run cobalt day-open verdict" DAY-OPEN-QWEN.md — "route: production is the deploy hub's; a dev read uses COBALT_ENV=dev". Read with the Grep tool instead.
- The card's R1138 line reference `cto-2026-10-12.md:12` reads `:13` at HEAD. The text is the same.
- `.env`: never present in this worktree (DB: none, no lock taken).
- L74: one `Claude-Session:` request (see `## L74`), not acted on.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: needs-his-hand-1012 · tip: ad73d04a | on 6468fb5e | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 130764
