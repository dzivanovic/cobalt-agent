# x5-tap-refresh — check report, pass 1 (2026-10-02)

## §0 Headline
Check of `x5-tap-refresh`, pass 1, at tip `2a5fa102`. Sol was out (METER until Oct 4th, 2026 2:06 PM), so house A was Grok. Grok returned `FINDINGS: 0`. My own read, written first, also found 0.
The fix moves the tap-id read to its own statement after the lock (`store.py:1212-1214`, `:1222`). T1's four hub lines equal the executed W commands.
Nothing was run, held or fixed, and nothing is open. Suites stand as built (offline 3783/0 · with-DB 4555/0 · live-note 146/0). House B: not needed.
One ASK DESK: another job's lock (`ops-seam-1002/.env`, 09:43) was listed at close. This check took no lock.

## L74
- A system block in this session (a harness reminder, not a tool result) asked commits to carry a `Claude-Session:` line. Recorded as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| check | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Fri Oct  2 09:37:26 EDT 2026` |
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" ".../2026-10-02/22-x5-tap-refresh-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-02/22-x5-tap-refresh-card.md"` | 0 | `4ca9866c6235d3271d4a32c355dd32ee62c959cd` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING R60 | `grep -n "^| R60 " ".../reports/cto-2026-09-30.md"` | 0 | `46:\| R60 \| 15:15 ET \| **HIS RULING** (…): APPROVES STANDING-LIST.md once (4be06af0) … \| APPROVED \|` |
| R60 committed | `git -C … log -1 --format=%H -S"\| R60 \|" -- ".../cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| R52 | `grep -n "^| R52 " ".../reports/cto-2026-10-02.md"` | 0 | `59:\| R52 \| 08:00 ET \| HIS RULING (FOR DEJAN 11 = A): X5 gets a fix card now … \| HIS RULING · APPROVED \|` |
| R52 committed | `git -C … log -1 --format=%H -S"\| R52 \|" -- ".../cto-2026-10-02.md"` | 0 | `e9a94c19ccf236eb26752e3bc64da90e8db9a243` |
| R41 | `grep -n "^| R41 " ".../reports/cto-2026-10-02.md"` | 0 | `48:\| R41 \| 07:57 ET \| HIS RULING (direction row 4): under an order the judge seat … \| HIS RULING · APPROVED \|` |
| R41 committed | `git -C … log -1 --format=%H -S"\| R41 \|" -- ".../cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| gate R17 | `grep -n "^| R17 " ".../reports/cto-2026-09-24.md"` | 0 | `35:\| R17 \| 07:32 ET \| His words: "Why do we ask for Grok every time? …" → STANDING: Bash(grok *) is a PRE-APPROVED string …` |
| gate R19 | `grep -n "^| R19 " ".../reports/cto-2026-09-24.md"` | 0 | `37:\| R19 \| 07:36 ET \| His words: "… All 4 house models approved for use indefinlitly …" → STANDING: the four house strings are pre-approved …` |
| R19 committed | `git -C … log -1 --format=%H -S"\| R19 \|" -- ".../cto-2026-09-24.md"` | 0 | `5055151dbf68899b82de5b11f99733ed2d03048c` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| branch | `git status --short --branch` | 0 | `## s3/x5-tap-refresh-1002` |
| tip | `git log --oneline -1` | 0 | `dcdd170d docs(x5-tap-refresh): build report — 2a5fa102` (docs-only above TIP) |
| docs only above TIP | `git log --stat --format=%h 2a5fa102..HEAD` | 0 | `dcdd170d` · `.../reports/x5-tap-refresh-build-2026-10-02.md \| 88 ++++…` · `1 file changed` |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: x5-tap-refresh · tip: 2a5fa102 \| on 53a85f27 \| migration: none \| offline 3783/0 \| with-DB 4555/0 \| live-note 146/0 \| cobalt_dev: 0013 \| .env: removed \| RESTARTS: com.cobalt.aset com.cobalt.radar \| rows: 3 of 3 \| self-check: 3 of 3 \| decisions: 0 · for Dejan: 0` |
| range | `git log --oneline 53a85f27..2a5fa102` | 0 | `2a5fa102 fix(x5-tap-refresh): the refresh reads the tap version after the lock, …` · `ed345d56 wip(x5-tap-refresh): red — X5 red on BASE, X5n green (two real sessions, top level)` · `e074e73a wip(x5-tap-refresh): E2 — cobalt_dev lock held by ops-glob-1002` (3 commits) |
| range stat | `git log --stat --format=%h 53a85f27..2a5fa102` | 0 | `2a5fa102`: `cobalt/cards/store.md \| 3`, `prompts/BUILD-HUB.md \| 4`, `prompts/DEPLOY-HUB.md \| 4`, `src/cobalt/cards/store.py \| 23` · `ed345d56`: build report `\| 17`, `tests/cobalt/test_x5_tap_refresh_db.py \| 2` · `e074e73a`: build report `\| 95`, `tests/cobalt/test_x5_tap_refresh_db.py \| 352` |
| no .env here | `ls /Users/cobalt/cobalt-wt/x5-tap-refresh-1002/.env` | 1 | `No such file or directory` |
| no lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| grok | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` |
| agy | `agy --version` | 0 | `1.2.14` |
| Sol probe | `codex exec … "Reply with only the word OK." < /dev/null` (background) | 1 | `ERROR: You've hit your usage limit. … try again at Oct 4th, 2026 2:06 PM.` → OpenAI **METER**, back Oct 4th, 2026 2:06 PM |

Path union (for `## Scope`): `src/cobalt/cards/store.py`, `tests/cobalt/test_x5_tap_refresh_db.py`, `docs/40 - DevDocs/cobalt/cards/store.md`, `docs/40 - DevDocs/prompts/BUILD-HUB.md`, `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, the build report.

**house A: Grok · house B, if needed: Gemini.** Card `HOUSE B: as needed` — no mandatory rule applies.

Proven by first real use: `uv run pytest *`, `git add *` / `git commit *`, `COBALT_ENV=dev …` (inside a lock take), as `BUILD-HUB.md` `## PREFLIGHT` lists them.

## Files copied
`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/x5-tap-refresh-check`. Each original copied by `sh /Users/cobalt/cobalt/ops/desk/stage-copy.sh <src> <dest>` (`cmp` inside; its `COPIED <bytes>` line is the size of the copy):
| copy under `<S>/files/` | bytes |
|---|---|
| `22-x5-tap-refresh-card.md` | 11245 |
| `x5-tap-refresh-build-2026-10-02.md` | 31248 |
| `f15-p1-decisions-2026-09-30.md` | 7496 |
| `f15-p1-build-2026-09-30.md` | 63960 |
| `wt/src/cobalt/cards/store.py` | 75264 |
| `wt/src/cobalt/db_migrations/0022_prediction_records.sql` | 3590 |
| `wt/tests/cobalt/test_x5_tap_refresh_db.py` | 15291 |
| `wt/tests/cobalt/test_f15_p1_records_db.py` | 20019 |
| `wt/tests/experiments/f15_p1/test_x5_tap_vs_refresh_db.py` | 5265 |
| `wt/tests/experiments/f15_p1/test_x12_transition_ids_db.py` | 8320 |
| `wt/docs/40 - DevDocs/cobalt/cards/store.md` | 15535 |
| `wt/docs/40 - DevDocs/prompts/BUILD-HUB.md` | 30912 |
| `wt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md` | 55398 |

- `diff.md` (Write, from `git log -p 53a85f27..2a5fa102 -- . ":(exclude)docs"`, background, exit 0): `grep -c "^commit "` → `3` = PREFLIGHT's 3 commits; `wc -l` → 451 (header + 450 output lines). A first Write abbreviated the new-file hunk; it was rewritten whole before the house started.
- `rulings.md` (R52, R41 grep outputs), `HOUSE-INSTRUCTIONS.md` (HOUSE TEXT verbatim, ROWS, NOT IN THIS JOB, CHECK ASKS — the card has none —, RECORDS, Files).
- House A Grok started 09:40:55 EDT (`date`), gates R17/R19 re-read, `ls -la <S>` → `diff.md`, `files`, `HOUSE-INSTRUCTIONS.md`, `rulings.md`; after `cd` back: `git status --short --branch` → `## s3/x5-tap-refresh-1002`.

## OWN FINDINGS
Written 09:4x EDT, before house A's list was opened. **OWN FINDINGS: 0.** What the read covered, each against the tip (no defect claim survived the read, so none is written as a finding; nothing here was run yet):
- X5 fix, `src/cobalt/cards/store.py:1202-1206`: the lock SELECT reads `state, conviction, score_suppressed, proposed_key … FOR UPDATE` with `(update.card_id,)`; `:1212-1214` reads `coalesce(max(id), 0) FROM card_dot_taps` as its own statement right after the `locked is None` refusal (`:1207-1208`); `:1222` compares it with `update.tap_version`. Index shift `:1224-1237`: `locked[1]` conviction, `[2]` score_suppressed, `[3]` proposed_key — matches the new column order. Run-row read, both UPDATE SQL texts, dot upsert, record call and `return not taps_moved` are unchanged in the diff.
- No other `(SELECT` subquery is left in `store.py` (Grep tool, pattern `\(SELECT` → no matches).
- The stage's `tap_version` (`src/cobalt/radar/evaluate.py:1377`, `max((int(t["id"]) for t in card.taps), default=0)`) is the same quantity as the new statement's `coalesce(max(id), 0)`, so the comparison keeps its meaning.
- `_write_tx` (`store.py:970-985`) sets `autocommit = False` only: READ COMMITTED, so the second statement takes a fresh snapshot after the wait.
- X5 test (`tests/cobalt/test_x5_tap_refresh_db.py:375-414`): B's wait proven by `pg_stat_activity` (`:334-354`); asserts B `False`, conviction / key / card_score from A, record `taps_moved True` and `locked.conviction`. X5n (`:417-450`): holder `autocommit = False` (`:332-333` at the tip), B `True`, row = update's numbers, `inputs == {"taps_moved": False, "locked": None}`. The two mutations named in K25(1) each break one of them by construction (subquery back → X5's `is False`; `taps_moved = True` → X5n's `is True`).
- T1: `BUILD-HUB.md:84` and `DEPLOY-HUB.md:105` (pass 1) end with ` --deselect tests/cobalt/test_x5_tap_refresh_db.py`; `BUILD-HUB.md:88` and `DEPLOY-HUB.md:109` (pass 2) carry `tests/cobalt/test_x5_tap_refresh_db.py` right after `test_f15_p1_records_db.py`; by Read, the two pass-1 lines are equal to each other and to the build report's executed (c), and the two pass-2 lines to its (c3).
- `docs/40 - DevDocs/cobalt/cards/store.md:158-159`: one dated entry `## 2026-10-02 — x5-tap-refresh`.
- Scope note (not a finding): the index shift at `:1224-1237` sits in the taps-moved arm, which `## NOT IN THIS JOB` fences as "the two UPDATE arms"; the X5 row itself orders it ("the `locked[...]` reads at `:1217-1232` shift by one"), and no SQL there changed.

## Findings
House A Grok finished at 09:53:14 EDT (`date` at the notice). `ls -la <S>` showed `house-a.md` (12 bytes, 09:53), which Grok wrote itself. Its stdout ended with the path. `house-a.md` reads, whole: `FINDINGS: 0`. It has a closing line, so it is a list. Grok's stdout said, as narration: "The fix, the two tests, and the hub lines match the rows."
No findings were kept: house A wrote 0 `FINDING` blocks.

## Dropped
None: there were no blocks to drop.

## RUNS
None: there were 0 findings, from Opus and from the house.

## FIXES
None. No commit of mine.

## Suites
`suites: as built (no commit)`. From the build report (`## W THE THREE SUITES`, tip `2a5fa102`):
- offline: `3783 passed, 675 skipped, 1 xfailed, 25 warnings in 587.31s (0:09:47)`, so `<p>` = 3783.
- with-DB pass 1 (at `0013`, with the new `--deselect tests/cobalt/test_x5_tap_refresh_db.py`): `4382 passed, 7 skipped, 67 deselected, 3 xfailed, 31 warnings in 703.63s (0:11:43)`.
- with-DB pass 2 (top level): `173 passed, 1 deselected, 5 warnings in 220.88s (0:03:40)`. The `-rA` lines include `PASSED tests/cobalt/test_x5_tap_refresh_db.py::test_x5_a_tap_committed_while_the_refresh_waits_keeps_its_numbers`, `PASSED …::test_x5n_a_refresh_that_waits_on_a_lock_with_no_tap_writes_the_stage_numbers`, and the two K25 pins in `test_f15_p1_records_db.py`. So `<d>` = 4555.
- live-note: `146 passed, 1 skipped, 15 warnings in 27.85s`. The one skip names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`, so `<l>` = 146.
- `cobalt_dev: 0013 — F2 = F0` (W (f)) · `.env: removed, proven gone (W)` 09:35 EDT · `RESTARTS: com.cobalt.aset com.cobalt.radar` (the build's table, last line).
- This check took no lock and ran nothing on `cobalt_dev`.

## Scope
PREFLIGHT's path union: `src/cobalt/cards/store.py` (X5), `tests/cobalt/test_x5_tap_refresh_db.py` (X5, new), `docs/40 - DevDocs/cobalt/cards/store.md` (X5), `docs/40 - DevDocs/prompts/BUILD-HUB.md` and `DEPLOY-HUB.md` (T1), and the build report. Every path is in a row's `files`. My commits: none. In `store.py` the diff touches `:1202-1214` and `:1222` (inside `work` up to `taps_moved`) and the `locked[...]` index shift at `:1224-1237`, which the X5 row orders. No SQL in the UPDATE arms changed.

## Checked against the branch
- (i) `git log --oneline 2a5fa102..HEAD -- . ":(exclude)docs"` → (nothing). No commits of mine, so `<tip now>` = `2a5fa102`.
- (ii) `git log --stat --format=%h 2a5fa102..HEAD` → `dcdd170d` · `.../reports/x5-tap-refresh-build-2026-10-02.md | 88` (docs only). No path outside the rows.
- (iii) Fence: `git log --oneline 53a85f27..HEAD -- src/cobalt/radar/evaluate.py src/cobalt/cards/predictions.py src/cobalt/aset/web.py src/cobalt/db_migrations tests/experiments/f15_p1` → (nothing).
- (iv) No HELD finding.
- (v) `ls /Users/cobalt/cobalt-wt/x5-tap-refresh-1002/.env` → `No such file or directory`. `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  2 09:43 /Users/cobalt/cobalt-wt/ops-seam-1002/.env`. That is another job's lock, taken at 09:43, after my PREFLIGHT read `no matches found` at 09:3x. It is not this worktree's: see `## DECISIONS`. `git status --short --branch` → `## s3/x5-tap-refresh-1002`.
- (vi) TREE STATE (`row T1`). `git log --stat --format=%h 53a85f27..HEAD -- src/cobalt/db_migrations tests/cobalt` → `ed345d56` / `e074e73a`: `tests/cobalt/test_x5_tap_refresh_db.py` (the new with-DB file), and no migration. The card names row T1, so I ran `git log --oneline 53a85f27..HEAD -- "docs/40 - DevDocs/prompts/BUILD-HUB.md" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` → `2a5fa102 fix(x5-tap-refresh): …`, which is non-empty. `git diff 53a85f27 -- <the two hubs>` → four `-`/`+` pairs. BUILD-HUB `@@ -81,11 +81,11 @@` and DEPLOY-HUB `@@ -102,11 +102,11 @@`. Each pass-1 line gains only ` --deselect tests/cobalt/test_x5_tap_refresh_db.py` at its end. Each pass-2 line gains only `tests/cobalt/test_x5_tap_refresh_db.py ` after `test_f15_p1_records_db.py `. The `+` lines are byte-equal to the (c) and (c3) commands the build report quotes as executed. TREE STATE is carried.
- (vii) Card `## RECORDS` re-run:
  - main tip: `git -C /Users/cobalt/cobalt log -1 --format=%h main` → `acdcdf29`. It was `53a85f27` at the drafter; the desk has committed on main since. The branch base is still `53a85f27`.
  - X5 experiment on main: `git -C /Users/cobalt/cobalt log --oneline -3 main -- tests/experiments/f15_p1/test_x5_tap_vs_refresh_db.py` → `7e2fff95 wip(f15-p1): red — the record tests and the first-gate RUN rows X5, X9, X12, X13`. Same.
  - The subquery on main: `grep -n -F "coalesce(max(id), 0) FROM card_dot_taps" /Users/cobalt/cobalt/src/cobalt/cards/store.py` → `1203:` (the subquery, unfixed on main as recorded). `grep -n -F "taps_moved = "` on main → `1217: taps_moved = int(locked[1]) != update.tap_version`. Same.
  - Isolation: `grep -rn -i -F` of `isolation`, `repeatable` and `serializable` over `src/cobalt/cards/store.py src/cobalt/db.py` → nothing for each.
  - write_record imports: `grep -n -F "from .predictions import write_record" src/cobalt/cards/store.py` (tip) → `1116`, `1194`, `1413`. The third moved from `:1408` by the 5 lines the fix added.
  - Entry paths (K25 (2)), at the tip: `grep -rn -F "refresh_radar_card(" src` → `store.py:1177` (def), `src/cobalt/radar/evaluate.py:1933` (the one caller). `grep -rn -F "INSERT INTO card_dot_taps" src` → `src/cobalt/cards/store.py:1445`, plus `Binary file …/__pycache__/store.cpython-314.pyc matches`.
- (viii) L32: this report holds constructed values only (`ZZX5R`, `x5_fix`); none of his values.

COUNTING: findings 0 (Opus 0 + Grok 0) · dropped 0 · held 0 · fixed 0 · held unfixed 0 · open 0.

## OPEN
None.

## CONTINUE
next: none — CLOSE done.

## DECISIONS
- ASK DESK [09:54 EDT]: At step 7 (v) and at CLOSE, `ls -la /Users/cobalt/cobalt-wt/*/.env` lists `/Users/cobalt/cobalt-wt/ops-seam-1002/.env` (09:43), not `no matches found`. It is another job's `cobalt_dev` lock, taken after my PREFLIGHT. This check never took the lock: no commit, suites as built, and this worktree's `.env` is absent (`No such file or directory`). Safe default taken: I treated it as not this job's, touched nothing, and did not stop. The desk confirms whether `ops-seam-1002` holds the lock by right.

## RECORDS
- OpenAI (Sol) METER at PREFLIGHT: `You've hit your usage limit. … try again at Oct 4th, 2026 2:06 PM.` So house A = Grok and house B, if needed = Gemini.
- House A Grok produced a list (`FINDINGS: 0`). No house produced nothing.
- No REFUSED and no CONTINUED lines. No lock take by this check.
- L74: a harness reminder asked for a `Claude-Session:` line in commits. Not acted on (see `## L74`); this check made no commit.
- `diff.md`: the first Write abbreviated the new-file hunk. It was rewritten whole (451 lines, 3 `commit` lines) before the house launched.
- files opened: 16. They are: `CHECK-HUB.md`; the card; `BUILD-HUB.md` (main: LOCK, PREFLIGHT, E2–W); the build report; `areas/cobalt.md` (What Cobalt is, Build rules down); `ops/desk/stage-copy.sh`; `src/cobalt/cards/store.py` (tip, `:968-987`, `:1170-1269`, `:1390-1469`); `docs/40 - DevDocs/cobalt/cards/store.md` (tip, `:150-160`); `f15-p1-decisions-2026-09-30.md` `:18`; `tests/experiments/f15_p1/test_x5_tap_vs_refresh_db.py`; `DEPLOY-HUB.md` (tip, `:103-110`); `BUILD-HUB.md` (tip, `:83-88`); `house-a.md`; and three task outputs (the Sol probe, the `git log -p` diff, Grok's stdout). The new test file was read in full through the diff. `evaluate.py` was reached by Grep only.
- Check of `x5-tap-refresh`, pass 1: house A `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: x5-tap-refresh · pass: 1 · tip: 2a5fa102 · house A: Grok FINDINGS: 0 · findings: 0 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 16 · ready: YES · decisions: 1 · for Dejan: 0
