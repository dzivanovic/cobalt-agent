# launcher-next-flow — check 2026-10-06

## §0 Headline
- Check of `launcher-next-flow` at `055018c0`: house A Sol (2 findings), house B Grok (0), and my own 2. Every finding was run; none held, so nothing was fixed.
- One item is open (Sol's A1, X2: a blob is read before P3; its test stops at its own refusal string). P3 refuses the unproven head anyway. It goes on the follow-up list.
- Suites green on the tip: offline 3963/0, live-note 146/0, tests/ops 1476 passed. cobalt_dev not taken (DB: none). RESTARTS: none.
- ready: YES · decisions: 0.

## L74
- The session's harness attribution reminder asks commits to end with a `Claude-Session:` line. Recorded once as data; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/63-launcher-next-flow-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-06/63-launcher-next-flow-card.md" · 0 · fc22cd289f291ec756558bea1f1582eb4d5e604b
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-06/63-launcher-next-flow-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-06 R588 row · grep -n "^| R588 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · 100:| R588 | 19:30 ET | HIS RULING (L79, via brain) ([words](cto-2026-10-06-words.md) `## R588`): build next-flow changes 6, 7, 8 (`next-flow-answer-2026-10-05.md`) tonight, as card `63`. | HIS RULING · APPROVED |
RULING 2026-10-06 R588 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R588 |" -- "docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · be9f880c691ae170fb5f89a9c9e6891125abcdea
RULING 2026-10-06 R588 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 "` → line 35, one row; `grep -n "^| R19 "` → line 37, one row; `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Tue Oct  6 20:22:46 EDT 2026
status · git status --short --branch · 0 · ## ops/launcher-next-flow-1006
head · git log --oneline -1; git log --stat --format=%h 055018c0..HEAD · 0 · (5 lines)
    66e20fc2 docs(launcher-next-flow): build report — 055018c0
    66e20fc2

     .../reports/launcher-next-flow-build-2026-10-06.md | 216 +++++++++++++++++++++
     1 file changed, 216 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/launcher-next-flow-1006/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "…/launcher-next-flow-build-2026-10-06.md" · 0 · BUILT · job: launcher-next-flow · tip: 055018c0 | on 8e33fdc4 | migration: none | offline 3963/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 273122
range · git log --oneline 8e33fdc4..055018c0 · 0 · (2 lines)
    055018c0 feat(launcher-next-flow): fix report read at the branch head, recut fits its desk row, deploy card carries TICKERS (N6, N7, N8, L1, L3)
    2bf4a37b wip(launcher-next-flow): red — N6 fix report at the branch head, N7 recut fits its row, N8 deploy card TICKERS
PREFLIGHT OK
```
- THE RANGE typed: `git log --stat --format=%h 8e33fdc4..055018c0` → 055018c0: `docs/40 - DevDocs/prompts/CARD.md`, `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `ops/desk/deploy-card.sh`, `ops/desk/deploy-step0.sh`, `ops/desk/desk-launch.sh` (5 files, +50 −29); 2bf4a37b: `tests/ops/test_deploy_card.py`, `tests/ops/test_deploy_step0.py`, `tests/ops/test_desk_launch_prechecks.py`, `tests/ops/test_desk_launch_recut.py` (4 files, +219 −43).
- DB: none: `git diff --name-only --no-renames 8e33fdc4..055018c0` → the nine paths above, every one under `ops/`, `tests/ops/` or `docs/`.
- `ls <S>` → `No such file or directory` (fresh).
- House probes (`sh /Users/cobalt/cobalt/ops/desk/house-probe.sh`, exit 0), three lines whole:
  - `sol: UP`
  - `grok: UP`
  - `gemini: OUT — CRITICAL INSTRUCTION 1: You may have access to a variety of tools at your disposal. Some tools may be for a specific task such as 'view_file' (for viewing contents of a file). Others may be very broadly applicable such as the ability to run a command on a terminal. Always prioritize using the most specific tool you can for the task at hand. Here are some rules: (a) NEVER run cat inside a bash command to create a new file or append to an existing file. (b) ALWAYS use grep_search instead of running grep inside a bash command unless absolutely needed. (c) DO NOT use ls for listing, cat for viewing, grep for finding, sed for replacing.` (HARNESS)
- house A: Sol · house B: Grok. HOUSE B: as needed.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` (exit 0) output whole (`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/launcher-next-flow-check`):
```
31455 <S>/diff.md
12669 <S>/files/63-launcher-next-flow-card.md
33136 <S>/files/launcher-next-flow-build-2026-10-06.md
14786 <S>/files/wt/docs/40 - DevDocs/prompts/CARD.md
57061 <S>/files/wt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md
11872 <S>/files/wt/ops/desk/deploy-card.sh
23278 <S>/files/wt/ops/desk/deploy-step0.sh
64841 <S>/files/wt/ops/desk/desk-launch.sh
18773 <S>/files/wt/tests/ops/test_deploy_card.py
31332 <S>/files/wt/tests/ops/test_deploy_step0.py
53573 <S>/files/wt/tests/ops/test_desk_launch_prechecks.py
15703 <S>/files/wt/tests/ops/test_desk_launch_recut.py
302 <S>/rulings.md
STAGED 13 files · 368781 bytes · commits 2
```
`stage-copy.sh`, one call each: `COPIED 3408 <S>/files/next-flow-answer-2026-10-05.md` · `COPIED 16550 <S>/files/deploy-deploy-drc-d5-o1-b2-1006.md` · `COPIED 21445 <S>/files/21-launcher-checks-card.md` · `COPIED 2562 <S>/files/wt/ops/desk/desk-row.sh`.
`grep -c "^commit " <S>/diff.md` → `2` (= PREFLIGHT's count). `<S>/HOUSE-INSTRUCTIONS.md` written (15120 bytes).
Houses started 20:24 EDT (`date` 20:24:34; both gates re-run: R17 line 35, R19 line 37): house A Sol (task b0tiiv8dw), house B Grok (task b29d8cgnc), `run_in_background`, timeout 2700000. After `cd <WT>`: `git status --short --branch` → `## ops/launcher-next-flow-1006`.

## OWN FINDINGS
Read: the card, the diff `8e33fdc4..055018c0` (`diff.md` source), at the tip `ops/desk/desk-launch.sh:788-870,1052-1140`, `ops/desk/deploy-step0.sh:110-134,320-420`, `ops/desk/deploy-card.sh:1-95`, `ops/desk/desk-row.sh` whole, `ops/desk/gate.sh:92-105`, the four test files' changed parts and fixtures, the build report's `## RESTARTS`, `## W`, `## FOR THE CHECK` and last line. X1 read at the tip with the Grep tool (`frep|fix report|fixed_ok` over both scripts): hits `deploy-step0.sh:338,385,389,391,398,400,403` and `desk-launch.sh:806,840,842,843,844,848,856,1040` — every read of the fix report is `git -C "$REPO" show "<head>:<rel>"` (`desk-launch.sh:848`, `deploy-step0.sh:391`); none reads a file on `main` (`:1040` is the devfix report). I found no defect in the three rows' code. The two findings below pin the two CHECK ASK clauses the build report itself says no test pins (`## FOR THE CHECK` X3, X4); each is a claim that the code is WRONG there, so a green run is `NOT HELD`.

FINDING O1
ROW: X3 (N7)
CLAIM: A failed line with a second ` — ` and an earlier ` · rollback:` inside the middle is cut wrongly by `ops/desk/desk-launch.sh:1111-1116` (the tail must start at the LAST ` · rollback:`, the head end at the FIRST ` — `), or the row it writes fails desk-row.sh's 300.
RUN: TEST — `tests/ops/test_desk_launch_recut.py`
```python
def test_o1_check_a_middle_rollback_and_a_second_dash_are_cut_right(desk):
    line = ("FAILED: gate — G (c) — x · rollback: maybe — " + LONG_MIDDLE
            + " · rollback: not used")
    desk.write_report(line)
    done = desk.recut()
    assert done.returncode == 0, done.stdout + done.stderr
    rows = [ln for ln in desk.today.read_text().splitlines() if "RECUT x-deploy attempt 2" in ln]
    assert len(rows) == 1, rows
    row = rows[0]
    assert desk_row_size(row) <= 300, (desk_row_size(row), row)
    text = row.split(" ET | ", 1)[1].removesuffix(" | RECORD |")
    assert text.startswith("RECUT x-deploy attempt 2 — FAILED: gate — G (c) — x · rollback: maybe — "), row
    assert text.endswith("… · rollback: not used"), row
    assert text.count(" · rollback:") == 2, row
    assert len("| R0000 | 00:00 ET | %s | RECORD |" % text) == 300, row
```
EXPECT: on the tip, if the claim is true, one of the assertions fails (exit 1, a tail cut at the first ` · rollback:`, or a row over 300).

FINDING O2
ROW: X4 (N8)
CLAIM: A deploy card that carries the new `TICKERS:` header line (written by `ops/desk/deploy-card.sh:210`) is refused by `ops/desk/desk-launch.sh` deploy, which N8 leaves unchanged.
RUN: TEST — `tests/ops/test_desk_launch_prechecks.py`
```python
@pytest.mark.parametrize("tickers", ["ZZPB,TEST", "none"])
def test_o2_check_a_deploy_card_with_a_tickers_line_launches(desk, tickers):
    desk.write_deploy()
    text = desk.deploy.read_text().replace("SET: x-job\n", f"SET: x-job\nTICKERS: {tickers}\n")
    desk.deploy.write_text(text)
    assert f"\nTICKERS: {tickers}\n" in desk.deploy.read_text()
    desk.ship()
    done = desk.launch("deploy", str(desk.deploy))
    assert done.returncode == 0, done.stderr
    assert (desk.wt / "x-gate").is_dir()
```
EXPECT: on the tip, if the claim is true, `assert done.returncode == 0` fails with a `REFUSED:` in stderr.

## Findings
House A Sol finished 20:30 EDT (`date` 20:30:24; exit 0). I wrote its final message, the last of its two printed lists, to `<S>/house-a.md` (2435 bytes, ends `FINDINGS: 2`). House B Grok finished 20:41 EDT (`date` 20:41:57; exit 0). Grok wrote `<S>/house-b.md` itself: 12 bytes, `FINDINGS: 0`. `ls -la <S>` at 20:41 shows both files.
| id | house | row | claim | run |
|---|---|---|---|---|
| O1 | Opus | X3 / N7 | A line with a second ` — ` and an earlier ` · rollback:` in the middle is cut wrongly, or the row it writes is over 300 | TEST |
| O2 | Opus | X4 / N8 | A deploy card with a `TICKERS:` line is refused by the unchanged `desk-launch.sh deploy` | TEST |
| A1 | Sol | X2 | The launcher reads the fix-report blob at the row's head (`desk-launch.sh:848`) before P3 proves that head (`:859`) | TEST |
| A2 | Sol | SCOPE | N6 says `test_f1_a_fix_report_outside_the_reports_folder_still_refuses` "stays as it is", but the build changed its setup | COMMAND |

## Dropped
none. Every block has a `RUN:` line followed by a `def test_` or a `git diff` command. Grok wrote no block.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_launch_recut.py::test_o1_check_a_middle_rollback_and_a_second_dash_are_cut_right` | `1 passed, 15 warnings in 1.59s` | NOT HELD: the cut keeps the head through the first ` — ` and the tail from the last ` · rollback:`, and the row is exactly 300 characters. Test removed. |
| O2 | Opus | `uv run pytest … tests/ops/test_desk_launch_prechecks.py::test_o2_check_a_deploy_card_with_a_tickers_line_launches` | `2 passed, 15 warnings in 1.75s` | NOT HELD: a card with `TICKERS: ZZPB,TEST` or `TICKERS: none` launches. Test removed. |
| A1 | Sol | `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=short tests/ops/test_desk_launch_prechecks.py::test_x2_the_fix_report_head_is_proven_before_its_blob_is_read` | `1 failed` at `tests/ops/test_desk_launch_prechecks.py:681` in `refused(…)`: `assert 'REFUSED: deploy ops/x-job: the branch head 60ec684a, the row says 253171e8 — the head moved: 60ec684a' in 'WARNING: desk size unread — guard skipped\nREFUSED: deploy ops/x-job: the branch head is 60ec684a, the row says 253171e8 — the head moved: 60ec684a\n'` | UNSETTLED: the test stops at its own expected refusal text, which lacks the script's word `is`, so its ordering assertion never runs. Fixing that string would change an assertion, which a check may not do. The same run shows the unproven head is refused by P3 (`the branch head is …, the row says …`), so a blob read there cannot launch anything. Test removed. |
| A2 | Sol | `git diff HEAD~2 HEAD -- tests/ops/test_desk_launch_prechecks.py` | (no output) | NOT HELD: red for another reason. `HEAD~2..HEAD` is `2bf4a37b..66e20fc2`, which leaves out the red commit that holds the test change. The change itself is disclosed and explained in the build report's `## DECISIONS` (DECISION N6-1). |
No HELD test, so there is no `wip(launcher-next-flow): check red` commit. After the removals, `git status --short --branch` → `## ops/launcher-next-flow-1006` (clean).

## FIXES
none (nothing held).

## Suites
I made no commit, so W ran on the build's `TIP` `055018c0` (HEAD `66e20fc2` adds only the build report). For a DB: none card that is (a0), (a) and (e).
- RESTARTS: `uv run cobalt jobs restarts 8e33fdc4..HEAD` → 10 rows (3 DOCS, 3 `operator script; no Cobalt reader`, 4 `test/documentation; no resident`), last line `RESTARTS: none`.
- (a0) `git diff --name-only --no-renames 8e33fdc4` → `docs/40 - DevDocs/prompts/CARD.md`, `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `docs/40 - DevDocs/reports/launcher-next-flow-build-2026-10-06.md`, `ops/desk/deploy-card.sh`, `ops/desk/deploy-step0.sh`, `ops/desk/desk-launch.sh`, `tests/ops/test_deploy_card.py`, `tests/ops/test_deploy_step0.py`, `tests/ops/test_desk_launch_prechecks.py`, `tests/ops/test_desk_launch_recut.py`. Every path is under `ops/`, `tests/ops/` or `docs/`, so **`cobalt_dev: not taken (DB: none — 10 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh launcher-next-flow-1006 offline` → exit 0, `offline 3963/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/launcher-next-flow-1006-offline-20261006-204304.log`. Log line 862: `3963 passed, 787 skipped, 1 xfailed, 36 warnings in 604.16s (0:10:04)`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh launcher-next-flow-1006 livenote` → exit 0, `live-note 146/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/launcher-next-flow-1006-livenote-20261006-205321.log`. Its one SKIPPED line is log line 56: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. It does not name `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `1476 passed, 1 xfailed, 15 warnings in 375.15s (0:06:15)`.
- with-DB: not run (DB: none). `.env`: `ls <WT>/.env` → `No such file or directory`, before and after W. No lock was taken.

## Scope
PREFLIGHT's path union is the nine paths of `8e33fdc4..055018c0`. Each sits in a row's `files`: N6 covers `desk-launch.sh`, `deploy-step0.sh`, `test_desk_launch_prechecks.py` and `test_deploy_step0.py`; N7 covers `desk-launch.sh` and `test_desk_launch_recut.py`; N8 covers `deploy-card.sh`, `test_deploy_card.py`, `CARD.md` (the new row after `SET` and the word on the short-form line only, per the diff) and `DEPLOY-HUB.md` (the one phrase on `:101` only, per the diff). I added no commits.

## Checked against the branch
- (i) `git log --oneline 055018c0..HEAD -- . ":(exclude)docs"` → empty. I made no commit, so `<tip now>` = `055018c0`.
- (ii) `git log --stat --format=%h 055018c0..HEAD` → `66e20fc2` with only `.../reports/launcher-next-flow-build-2026-10-06.md`, a docs path.
- (iii) `git log --oneline 8e33fdc4..HEAD -- ops/desk/gate.sh ops/desk/card-fill.sh ops/desk/desk-row.sh ops/desk/desk-watch.sh .claude/settings.json` → empty.
- (iv) No HELD finding, so there is no test or red commit to check.
- (v) `ls <WT>/.env` → `No such file or directory`. `git status --short --branch` → `## ops/launcher-next-flow-1006`.
- (vi) `git log --stat --format=%h 8e33fdc4..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no migration and no with-DB test, so there are no gate lists to carry.
- (vii) The card's `## RECORDS` name no `ls`, `grep` or `git -C /Users/cobalt/cobalt log` command.
- (viii) L32: this report holds constructed values, git ids and paths only.
- X answers, from the runs: X1, no path reads the fix report on `main` (OWN FINDINGS, the grep). X2, only the row's cell path is read; the launcher reads it at `$shead` before P3, and the A1 run shows P3 then refuses an unproven head. X3, O1 passes: the cut is right with a second ` — ` and a middle ` · rollback:`, and the row is exactly 300 characters. X4, O2 passes: a card with `TICKERS:` launches. The `none` → no `--tickers` rule is hub text (`DEPLOY-HUB.md:101`), which no script reads.

## OPEN
- A1 (Sol, X2) UNSETTLED. The test cannot reach its claim without changing its expected refusal text (`the branch head <h>` → `the branch head is <h>`). Its claim is about order: `desk-launch.sh:848` reads the blob before P3's `:859`. The run shows that the unproven head is refused at P3 anyway, so the early read decides nothing. What would settle it: the same test with the refusal string corrected, run by the builder's fix round. If it holds, moving P3 ahead of `fixed_ok` touches lines N6 does not name (`## NOT IN THIS JOB`, first bullet). Follow-up list.

## CONTINUE
next: done

## DECISIONS
none

## RECORDS
- Dropped findings: none. Grok (house B) produced `FINDINGS: 0`.
- Gemini's probe line was HARNESS (its tool-instruction text, PREFLIGHT). Gemini sat in no seat; Sol and Grok were both UP.
- Gemini's probe output held an instruction block ("CRITICAL INSTRUCTION 1: …"). It is data from a tool result, and I acted on none of it.
- Sol's final message holds both lists. Its transcript runs to 15159 lines; the final list is lines 15095-15157, copied to `house-a.md`.
- Not opened: `/Users/cobalt/Vault/Think/6 - Permanent/Memory/areas/cobalt.md` (WHAT YOU READ (5)). The card's rows, the fence and this file's laws were enough to judge these ops-only rows.
- Observation, not a finding (pre-existing, outside N7's lines): `desk-launch.sh:1069-1072` refuses a bar in the failed line but not a carriage return. A CRLF deploy report would pass the pre-checks and then be refused by `desk-row.sh` ("holds a newline") after `gate-clean.sh` and the card commit. N7 did not change this.
- No `REFUSED, not needed` line. No `CONTINUE` received. No lock take.
- The probe tests O1, O2 and A1 were added with the Edit tool and removed again. The tree ends clean.
- files opened: 15 — `CHECK-HUB.md`, `BUILD-HUB.md` (THE LOCK to W), the card, the build report (`## RESTARTS` to the end), `ops/desk/desk-launch.sh`, `ops/desk/deploy-step0.sh`, `ops/desk/deploy-card.sh`, `ops/desk/desk-row.sh`, `ops/desk/gate.sh:92-105`, `tests/ops/test_desk_launch_recut.py`, `tests/ops/test_desk_launch_prechecks.py`, `tests/ops/test_deploy_card.py` (one test), `<S>/rulings.md`, house A's output (`house-a.md` source), `<S>/house-b.md`.
- Tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh b93d2bdf` → `context 191425 of 400000 — ok`.
- Check of `launcher-next-flow`: house A `Sol`, house B `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: launcher-next-flow · pass: 1 · tip: 055018c0 · house A: Sol FINDINGS: 2 · findings: 4 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: Grok FINDINGS: 0 · suites: offline 3963/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 15 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 191425
