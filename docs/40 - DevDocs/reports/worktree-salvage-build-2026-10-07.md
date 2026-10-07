# worktree-salvage — build report 2026-10-07

## §0 Headline
- `job-clean.sh salvage <worktree-name>` is built (W1-W7) at tip `df4cd805` on `c4e52f4e`. It inspects the tree, refuses before any change, saves the work to a `wip/` branch, then removes the tree. It is never forced. The card mode is unchanged.
- Suites: offline 3963/0, live-note 146/0, `tests/ops` 1508 passed; `test_gate_clean.py` 32 → 64 passed. DB: none. RESTARTS: none.
- 4 decisions, none for Dejan. Item 4: a stray untracked `…build-2026-10-07.md.tail` file is left for the desk to delete.

## L74
- 06:57 EDT: a system reminder asked commits to end with a `Claude-Session:` line. Recorded here as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-07/83-worktree-salvage-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-07/83-worktree-salvage-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-07/83-worktree-salvage-card.md" · 0 · d42329ed8bc41ac4f65f787b51701c60ab5890c9
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-07/83-worktree-salvage-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-07 R613 row · grep -n "^| R613 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · 8:| R613 | 06:37 ET | HIS RULING (words: `cto-2026-10-07-words.md` R613): worktree cleanup is the desk's. Inspect, report, remove; real unsaved work becomes a side job first, nothing waits on him; the desk gets the remove command. | APPROVED — pending fold |
RULING 2026-10-07 R613 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R613 |" -- "docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · 02c6b37b7a4e33033071e35d977620deb0f93068
RULING 2026-10-07 R613 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0, output whole:
```
clock · date · 0 · Wed Oct  7 06:57:31 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/worktree-salvage-1007
    ?? "docs/40 - DevDocs/reports/worktree-salvage-build-2026-10-07.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · c4e52f4e docs(desk): salvage preflight r2 08370621 in section 5
diff · git diff --stat c4e52f4e · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/worktree-salvage-1007 · 0 · c4e52f4e docs(desk): salvage preflight r2 08370621 in section 5
env here · ls /Users/cobalt/cobalt-wt/worktree-salvage-1007/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
`git show --stat c4e52f4e` · 0 · `docs(desk): salvage preflight r2 08370621 in section 5` — `docs/40 - DevDocs/reports/cto-2026-10-07.md | 2 +-`, 1 file changed, 1 insertion(+), 1 deletion(-).

| rule | command | exit | output |
|---|---|---|---|
| symbol `:24` | `grep -n -F "usage: job-clean.sh" ops/desk/job-clean.sh` | 0 | `24:[ "$#" -eq 1 ] \|\| refuse "usage: job-clean.sh \"<job card>\""` |
| symbol `:55` | `grep -n -F "merge-base --is-ancestor" ops/desk/job-clean.sh` | 0 | `7:` (header), `55:git -C "$REPO" merge-base --is-ancestor "refs/heads/$branch" main \|\| refuse …` |
| symbol `:13` | `grep -n -F "LC_ALL=C" ops/desk/job-clean.sh` | 0 | `13:export LC_ALL=C` |
| symbol `:44` | `grep -n -F "agy-trial" ops/desk/job-clean.sh` | 0 | `5:` (header), `44:[ "$wt" != "agy-trial" ] \|\| refuse …` |
| symbol `:62-63` | `grep -n -F "branch -d" ops/desk/job-clean.sh` | 0 | `9:` (header), `62:printf 'RUN: git -C %s branch -d %s\n' …`, `63:git -C "$REPO" branch -d "$branch" \|\| …` |
| `restarts.py:230-232` | `grep -n -F "operator script; no Cobalt reader" src/cobalt/jobs/restarts.py` | 0 | `232:` |
| `restarts.py:245-246` | `grep -n -F "test/documentation; no resident" src/cobalt/jobs/restarts.py` | 0 | `246:` |
| `restarts.py:38` | `grep -n -F "ops/desk/" src/cobalt/jobs/restarts.py` | 0 | `38:OPS_DESK_PREFIX = "ops/desk/"` |
| `STANDING-LIST.md:36` | `grep -n -F "Bash(sh /Users/cobalt/cobalt/ops/desk/*)" …STANDING-LIST.md` | 0 | `36:`, `49:`, `79:`, `135:`, `203:` |
| file sizes | `wc -l ops/desk/job-clean.sh tests/ops/test_gate_clean.py` | 0 | `64`, `315` |
| READ tail | `tail -n 3 …/cto-2026-10-07-words.md` | 0 | last line: `Earlier in the turn: "worktree are mine if they are broken not mine if they are normal. …"` |
| READ tail | `tail -n 3 …/cto-2026-10-07.md` | 0 | last line: `## §5 HISTORY` |
| checklist `:59` | Read `Memory/topics/cto-desk-checklist.md:59` | — | holds the R613 clause ending "until it ships the desk reports a broken tree and removes nothing." |
| restarts | `uv run cobalt jobs restarts c4e52f4e..HEAD` | 0 | one row, the untracked report `A DOCS -`; `RESTARTS: none` |
| test count before | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_gate_clean.py` | 0 | `32 passed, 15 warnings in 7.89s` |

The job-clean.sh section (`:248-315`) is 7 test functions / 12 collected; `job-clean.sh` read whole (64 lines); `test_gate_clean.py` read whole.

Card `## RECORDS` copied: (1) citations proven at main `2ac0e604` by the drafter; (2) the job-clean.sh tests live in `tests/ops/test_gate_clean.py:248-315` — re-read: true; (3) `.git/hooks/pre-commit` two parts — not re-read (outside this worktree's list; the test `git()` helper runs with `core.hooksPath=/dev/null`).

DB: none — no lock probe, no `<FP>`.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `c4e52f4e` → exit 0: `3963 passed, 787 skipped, 1 xfailed, 36 warnings in 636.69s (0:10:36)` — 0 failed, 0 errors (the two `COBALT_LIVE_VAULT_ROOT not set` skips belong to this offline run; the live-note run below covers them).
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → exit 0: `146 passed, 1 skipped, 15 warnings in 28.12s`; the one skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, so no skip names `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
Tests added to `tests/ops/test_gate_clean.py`, new section `# ---- job-clean.sh salvage ----` after the old `:315`; no `src/` or script edit. Commit `98e9e87d wip(worktree-salvage): red — job-clean.sh salvage tests W1-W7`.
`uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_gate_clean.py` on BASE → `19 failed, 45 passed, 15 warnings in 9.28s` (45 = the 32 old + 13 negative controls). Every red's first line names BASE's `:24` refusal, which is each row's named reason:
- W1 `test_salvage_usage_names_the_salvage_form` → `AssertionError: REFUSED: usage: job-clean.sh "<job card>"` (BASE prints the old usage only).
- W1/X3 `test_salvage_a_prefix_of_a_registered_worktree_is_refused` → `assert 'is not a registered worktree of' in 'REFUSED: usage: job-clean.sh "<job card>"\n'`.
- W2/W4/W5 `…clean_merged…`, `…clean_unmerged…`, `…dirty_unmerged…`, `…dirty_merged…`, `…detached_unmerged…`, `…detached_merged_clean…` (6) → `assert 1 == 0` with stderr `REFUSED: usage: job-clean.sh "<job card>"` (exit 1 at `:24`, the tree stands).
- W3 `…env…after_the_report`, `…locked…[None]`, `…locked…[held by a test]`, `…git_operation…[rebase-merge|rebase-apply|MERGE_HEAD|CHERRY_PICK_HEAD|REVERT_HEAD|BISECT_LOG]`, `…existing_wip_branch…`, `…wip_name_git_refuses…` (11) → `assert False` from `''.startswith('INSPECT: worktree …')` (stdout empty, `:24`).
Negative controls GREEN on BASE: `test_salvage_a_name_outside_the_pattern_is_refused` ×6 (`../x-job`, `/abs/x-job`, `a/b`, `.hidden`, `agy-trial`, `""`), `…symlinked_name…`, `…directory_git_does_not_know…`, `…accented_name…utf8…`, `…tree_on_main…`, `…clean_unmerged…negative_control` (W5), `…env…negative_control` (W3), `test_job_clean_is_never_forced` (W7).
W6 on BASE: `grep -c -F "job-clean.sh salvage <worktree-name>" ops/desk/job-clean.sh` → `0`.
No RUN row; no with-DB red (DB: none).

## E3 THE ROWS
Built in card order W1-W7 in `ops/desk/job-clean.sh` (64 → 200 lines, `wc -l` at the tip); commit `df4cd805 feat(worktree-salvage): job-clean.sh salvage mode — inspect, save to a wip branch, remove, never forced (W1-W7, L1, L3, L76)`.
- W1: dispatch before the card mode (two args with `$1 = salvage` → `salvage "$2"`; one arg → card mode; else the two-form usage). The name check is one function `plain_worktree`, used by both modes (card mode's old `:41-47` replaced by `plain_worktree "$wt"`, same messages). The stanza is matched with `$0 == p` (whole line); `branch refs/heads/<b>`, `detached`, `^locked( |$)` read from it; `main` refused; all before stdout.
- W2: the INSPECT lines in the card's order. W3: `.env`, `locked`, the six `--git-path` markers, then (only when a wip branch is due) `check-ref-format --branch` and an existing branch — all after the report, before any change. W4: `switch -q -c <wip>`, then `add -A` and `commit -q` only when status is non-empty; `SALVAGED:` lines as the card gives. W5: `worktree remove` (no flag), `branch -d` only when merged into main (its git output sent to stderr so stdout stays the protocol), `kept:` lines, the last line.
- W6: header lines 2-25 carry the second usage line, the report, refusals, wip branch, `SALVAGED:`, the last line, "ignored files are not saved", "Never forced". `grep -c -F "job-clean.sh salvage <worktree-name>" ops/desk/job-clean.sh` → `0` on BASE, `2` after.
- W7: `test_job_clean_is_never_forced`.
- DevDocs line: no page under `docs/40 - DevDocs/cobalt/` names `job-clean` (Grep → no files), and the card fences every file but the two (`## NOT IN THIS JOB`); no line written (DECISIONS item 2).
Test rewritten after its first mutation stayed green: `_salvage_refused_after_report` now also asserts `"RUN:" not in done.stdout`, and the existing-wip and bad-wip-name tests assert their own refusal reason. Without that, removing the explicit wip-branch checks left the tests green, because git's own `switch -c` also refuses.
Greens: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_gate_clean.py` → `64 passed, 15 warnings in 11.12s` (32 before → 64 after; the 12 old job-clean.sh tests and 20 gate-clean.sh tests unchanged and green).

MUTATIONS (each made with Edit, the row's tests run alone, then undone with Edit; `git diff --stat` after the last undo → `ops/desk/job-clean.sh | 154 +++…`, `tests/ops/test_gate_clean.py | 7 +-` against the red commit, i.e. the fix only):
| row | mutation | result, first failing line |
|---|---|---|
| W1 | usage text back to BASE's | `1 failed` — `AssertionError: REFUSED: usage: job-clean.sh "<job card>"` |
| W1/X3 | stanza match `index($0, p) == 1` (prefix) | `1 failed` — `assert 'is not a registered worktree of' in 'fatal: not a git repository … REFUSED: …/wt/x-jo has no HEAD commit\n'`. (A first try, `index(p, $0) == 1`, was the wrong direction and stayed green; replaced by the real prefix bug.) |
| W1 | main refusal disabled | `1 failed` — `assert 0 == 1` with stdout `… deleted main; kept none` |
| W1 NC | `refuse` exits 0 | `9 failed` — the 6 names, symlink, loose directory, accented name |
| W2 | commit lines suppressed | `1 failed` — `At index 4 diff: 'INSPECT: status: 0 lines' != 'INSPECT:   aa3db6ca job'` |
| W2 | `locked:` prints `$merged` | `1 failed` — `At index 6 diff: 'INSPECT: locked: yes' != 'INSPECT: locked: no'` |
| W3 + NC | `.env` refusal disabled | `2 failed` (NC and full) — `assert 0 == 1` (tree salvaged and removed) |
| W3 | locked refusal disabled | `2 failed` — `assert 'RUN:' not in …` |
| W3 | `^locked$` (bare line only) | `1 failed` — `…locked…[held by a test]` |
| W3 | git-operation refusal disabled | `6 failed` — one per marker |
| W3 | both wip-name refusals disabled | `2 failed` — `assert 'RUN:' not in …` |
| W4 | `add -A` → `add -u` | `1 failed` — `contains modified or untracked files, use --force to delete it` / `REFUSED: worktree remove failed; every branch is kept` → `assert 1 == 0` |
| W4 | wip only when dirty (detached ignored) | `1 failed` — `…detached_unmerged…`: `assert 0 == 1` (`len([])`) |
| W4 | wip for any detached HEAD (merge ignored) | `1 failed` — `…detached_merged_clean…`: `assert not True` |
| W5 + NC | unmerged branch dropped with `update-ref -d` | `2 failed` — `assert False` where `has_branch(…, 'ops/x-job')` |
| W5 | wip branch dropped after `kept:` | `3 failed` — dirty unmerged, dirty merged, detached unmerged: `assert 0 == 1` (`len([])`) |
| W7 | a `# mutation: --force` comment | `1 failed` — `assert ['--force'] == []` |

## RESTARTS
`uv run cobalt jobs restarts c4e52f4e..HEAD` → table whole:
```
path	change	rule	restart
docs/40 - DevDocs/reports/worktree-salvage-build-2026-10-07.md	A	DOCS	-
ops/desk/job-clean.sh	M	operator script; no Cobalt reader	-
tests/ops/test_gate_clean.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row.

## W THE THREE SUITES
`<tip>` = `df4cd805`. Card `DB: none`.
- (a0) `git diff --name-only --no-renames c4e52f4e` → whole: `ops/desk/job-clean.sh`, `tests/ops/test_gate_clean.py` — every path under `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 2 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh worktree-salvage-1007 offline` → exit 0, verdict whole: `offline 3963/0`; `log: /Users/cobalt/cobalt-wt/.gate-logs/worktree-salvage-1007-offline-20261007-071543.log`. The 32 tests this build adds are all in `tests/ops/test_gate_clean.py`, which this suite does not hold, so they run in the third suite.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh worktree-salvage-1007 livenote` → exit 0, verdict whole: `live-note 146/0`; `log: /Users/cobalt/cobalt-wt/.gate-logs/worktree-salvage-1007-livenote-20261007-071544.log`. `grep -n -F "SKIPPED" <log>` → `56: SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`; no skip names `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `1508 passed, 1 xfailed, 15 warnings in 396.40s (0:06:36)`.
- The card's deploy gate, row proof: `tests/ops/test_gate_clean.py` → `64 passed, 15 warnings in 11.12s` (32 before, 64 after); `tests/ops` → `0 failed` (above).
- (b)-(d), (f): not run (DB: none). `.env`: never present (PREFLIGHT `env here` → No such file).

## PRE-STOP SELF-CHECK
(1) Every added test was shown red. 32 tests were added: 19 are red at E2 against BASE. The 13 negative controls are red under their mutations (W1 NC 9 by `refuse` exit 0, W3 NC by the `.env` refusal, W5 NC by `update-ref -d`, W7 by the `--force` comment). Every row's full tests are red under the E3 mutations in the table. One test stayed green under its first mutation and was rewritten (the `RUN:` assertion, E3). — 3 of 3 items backed.
(2) Every entry path is pinned:
- Callers: `grep -n -F "plain_worktree"` → `:52` (salvage) and `:183` (card mode). The card mode is pinned by the 12 old tests (green), the salvage mode by the new ones.
- Argument shapes: 3 args, 0 args, 2 args with `salvage`, 1 arg (old tests).
- Tree states: clean merged, clean unmerged, dirty unmerged, dirty merged, detached unmerged, detached merged clean, `.env`, locked with and without a reason, six markers, pre-made wip branch, invalid wip name, `main`, prefix name, unknown directory, symlink, six bad names, accented name.
- Not pinned by a test: `worktree remove` failing for a reason other than a lock, `branch -d` failing after the removal, and a failed `switch`/`add`/`commit`. No constructed state produces them in the temp repo without a hook or a force form. They are named under `## DECISIONS` item 3.
(3) Re-read at the tip:
- `wc -l` → `200 ops/desk/job-clean.sh`, `679 tests/ops/test_gate_clean.py`.
- `grep -n -F "refuse \"usage"` → `166:`.
- `grep -n -F "plain_worktree"` → `39:`, `40:`, `52:`, `183:`.
- `grep -n -F "printf 'job-clean: %s and %s removed"` → `200:`.
- `grep -c -F "job-clean.sh salvage <worktree-name>"` → `2`.
- `git log --oneline c4e52f4e..HEAD` → `df4cd805`, `98e9e87d`.
- The restarts table was re-run after `df4cd805`.

## FOR THE CHECK
- Range `c4e52f4e..df4cd805`: `98e9e87d wip(worktree-salvage): red — job-clean.sh salvage tests W1-W7`; `df4cd805 feat(worktree-salvage): job-clean.sh salvage mode — inspect, save to a wip branch, remove, never forced (W1-W7, L1, L3, L76)`.
- Per row: E2 reds and NC greens under `## E2 RED`; mutations under `## E3 THE ROWS`; greens `64 passed` (file) and `1508 passed, 1 xfailed` (`tests/ops`).
- Caller greps: `plain_worktree` `:52`, `:183`; card mode `:166-200`, its messages unchanged (`git diff -U0`: card-mode hunks are the usage line and `:41-47` → `plain_worktree "$wt"`, the function holding the same four refusals with `$1` for `$wt`).
- X1: a dirty tree is committed before `worktree remove`. A failed add/commit refuses before the removal. `worktree remove` with no flag refuses a tree that still holds untracked or modified files (the `add -u` mutation proved it: `contains modified or untracked files`). `branch -d` runs only after `merge-base --is-ancestor refs/heads/<b> main`. A detached unmerged HEAD gets a wip branch at its commit.
- X3: the stanza line is matched whole (`$0 == p`). The prefix mutation is red. A trailing slash in `COBALT_WT_ROOT` gives `…//name`, which matches no stanza and is refused.
- X4: every W3 refusal is before the first `RUN:` line, and every W3 test asserts `"RUN:" not in stdout`, unchanged status and an unchanged HEAD.
- X5: `test_job_clean_is_never_forced` green; its mutation is red.
- RUN rows: none. With-DB: not run (DB: none). `<F0>`/`<F1>`/`<F2>`: not run (DB: none). Lock taken/released: not run (DB: none).
- RESTARTS table: under `## RESTARTS` (`RESTARTS: none`).
- Card records copied at PREFLIGHT: under `## PREFLIGHT`.

## CONTINUE
next: CLOSE (done at the report commit)

## DECISIONS
1. The text of the `switch` failure. The card gives `REFUSED: salvage stopped at <step>; nothing removed; the tree is on <wip>`, but after a failed `switch -c` the tree is not on `<wip>`. Default taken: the same text names where the tree really is (`<b>` or `(detached at <8 hex>)`). The add and commit failures name `<wip>` as the card says.
2. The DevDocs dated line. BUILD-HUB E3 asks for one line per changed module in its page under `docs/40 - DevDocs/cobalt/`. No page names `job-clean` (Grep → no files), and the card's `## NOT IN THIS JOB` fences every other file. Default taken: no line written. The desk decides whether an ops-script page is owed.
3. Failure paths with no test:
   - Not specified by the card: a `branch -d` failure after the tree is removed. Default taken: the card mode's form, `job-clean salvage: removed <path>; branch -d <b> FAILED; kept <wip or none>`, exit 1.
   - Not pinned by a test: a failed `switch`/`add`/`commit`, and a `worktree remove` failure other than a lock. No state built without a hook or a force form reaches them.
   Default taken: the safe exits shown, nothing removed before a failed salvage.
4. Cleanup owed. A stray untracked file, `docs/40 - DevDocs/reports/worktree-salvage-build-2026-10-07.md.tail` (one line, `x`), was written by mistake with the Write tool at 07:26 EDT. `rm` of any path but `.env` is not on this build's list, so it is not committed and stays in the tree. Default taken: left for the desk to delete. Because of it, the CLOSE `git status` shows one `??` line.

## RECORDS
- L74: a system reminder at 06:57 EDT asked for a `Claude-Session:` line in commits; recorded under `## L74`, not acted on.
- The live-note suite was run at E0 while the offline suite ran in the background (both read only); no file was written during the offline run.
- The card's records as re-read at PREFLIGHT: (2) re-read true; (1) and (3) not re-read, as stated there.
- Extra tests beyond the card's list, each pinning a path of a row: the prefix name (X3), a tree on `main` (W1), a detached clean merged HEAD (W4), a wip name git refuses (W3), and the bare and reasoned `locked` lines (W1).
- Lock: none taken (DB: none). No extra lock take.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: worktree-salvage · tip: df4cd805 | on c4e52f4e | migration: none | offline 3963/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 7 of 7 | self-check: 3 of 3 | decisions: 4 · for Dejan: 0 · tokens: 206624
