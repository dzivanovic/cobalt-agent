MODEL: Opus 5.5 (`claude-opus-5-5`, 09-22 R109). A test-only fix on the merge commit, a `cobalt_dev` forward migrate and its rollback to `0013` (L29's list: Opus floor, never auto mode). PERMISSION MODE, quoted from the line below: `--permission-mode acceptEdits` (write path, L62; `acceptEdits` + the full allowlist is the interim write-path practice — an unlisted Bash command raises a dialog under it, so run ONLY exact listed prefixes; a dialog is a FAILED run, L63) · SEAT: DRC merge fix r1 builder `drc-merge-fix-r1-build`, launched by the CTO desk in the background · SESSION: fresh; a relaunch uses the SAME line with ONE `CONTINUE: <step>` prefix line (L19, L60) · never `bypassPermissions`; push DENIED on the line · METER: Anthropic MEDIUM (rows ≈ 10 min; offline ≈ 10 min; with-DB two passes ≈ 15 min; live-note ≈ 1 min; ≈ 40–50 min in all) · nobody sits at this terminal: the report file is your channel; `ASK DESK: <question> [<time from date>]` under `## ESCALATE`, take the safe default, continue; NEVER END A TURN BETWEEN STEPS · grep patterns: plain fixed strings, one per call (`grep -n -F`), no backtick, no `\|`, no `$` in a double-quoted argument — or the Read tool.

THE DESK'S BARE COMMANDS, from the desk's shell, only while (i) the launch row and this file are committed on main, (ii) THE LOCK is free: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found` and no with-DB run in flight (the launch row carries the literal `no with-DB run in flight`), (iii) the drc-d1 tree is quiet: `git -C /Users/cobalt/cobalt-wt/drc-d1 status --short --branch` → `## drc/d1-trading-log` alone, and `git -C /Users/cobalt/cobalt log -1 --format=%h drc/d1-trading-log` → `338a2439` (`15`'s wip report commit over `5bb1f4b5`; read at launch by the desk: read by the desk 12:28 ET: drc-d1 tip `338a2439`, main at launch `6a8c21e1`):
(1) `cd /Users/cobalt/cobalt-wt/drc-d1` (its own call; the worktree EXISTS; it is NOT re-cut), then
(2) `claude --bg "Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-28/17-drc-merge-fix-r1-build.md' and follow it exactly." --model claude-opus-5-5 --permission-mode acceptEdits --remote-control drc-merge-fix-r1-build --name drc-merge-fix-r1-build --allowedTools "Bash(git add *)" "Bash(git commit *)" "Bash(git -C * status*)" "Bash(git -C * log*)" "Bash(git -C * diff*)" "Bash(git -C * rev-parse*)" "Bash(git -C * rev-list*)" "Bash(git -C * merge-base*)" "Bash(git -C * show*)" "Bash(cd *)" "Bash(uv run pytest *)" "Bash(COBALT_ENV=dev uv run pytest *)" "Bash(COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest *)" "Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/drc-d1/.env)" "Bash(rm /Users/cobalt/cobalt-wt/drc-d1/.env)" "Bash(COBALT_ENV=dev uv run cobalt db migrate)" "Bash(COBALT_ENV=dev uv run cobalt db migrate --proof-only)" "Bash(COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013)" "Bash(COBALT_ENV=dev uv run cobalt db query *)" "Bash(uv run cobalt jobs restarts *)" "Bash(ls *)" "Bash(grep *)" "Bash(tail *)" "Bash(wc *)" "Bash(date*)" --disallowedTools "AskUserQuestion" "EnterWorktree" "Bash(git push*)" --add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt --add-dir /Users/cobalt/cobalt-wt`

RULE STRINGS: 25 allow, 3 deny = `prompts/2026-09-28/15-drc-merge-main-build.md` line 5 byte for byte, minus `Bash(git merge --no-ff --no-edit main)` and `Bash(git merge --abort)` (no merge happens); the other tokens that differ are this file's path and `drc-merge-fix-r1-build` in `--remote-control` and `--name`. `comm` of the two files' quoted Bash tokens: 26 common (25 allow + `Bash(git push*)`), 2 in `15` only (the merge pair), 0 in this file only. NEW strings: NONE. Never typed: `git merge`, `git rebase`, `git reset`, `git checkout`, `git restore`, `git stash`, `git push`, `psql`, `COBALT_ENV=production`.

# DRC MERGE FIX R1 BUILD 2026-09-28 — THE 7 REGISTRY POSITION PINS OF `15`'s O RE-STATED TO THE MERGED NUMERIC ORDER, THE ARCHIVER DOCSTRING PARAGRAPH DROPPED, THE THREE SUITES ON THE FIX TIP UNDER L76

LADDER: `S3-P3 · F14` (DRC stack, branch `drc/d1-trading-log`, worktree `/Users/cobalt/cobalt-wt/drc-d1`). LAW STEP: `15` made the merge commit `5bb1f4b5` (main `daf36e01` into `10163d51`) and stopped `FAILED: O — offline red on 5bb1f4b5` (7 failed, 3540 passed); `cto-2026-09-28.md` R38 (5) / R46 rule a fix round (L75); the drafter's classification `reports/drc-merge-fix-r1-draft-2026-09-28.md` made FIX rows F1–F8, tests only. R38 (1): the registry order is NUMERIC `0013`…`0018`; the pins move, the registry does not.
THIS BUILD writes nothing but the 8 rows below (6 test files), its fix commit and its report. No `src/` change, no `configs/` change, no test deleted, skipped, marked or renamed, no new test. DO NOT STOP until the report's last line is `DRC MERGE FIX R1 BUILT …` or `FAILED …`.

## INDEX CARD — read in this order
(1) `/Users/cobalt/Vault/Think/6 - Permanent/Memory/LAWS.md` `## Preamble`, `## Index`, `## Reading`, then L29, L35, L42, L46, L48, L54, L60, L62, L63, L68, L70, L71, L74, L75, L76 (`grep -n "^### L<n> "`, body to the next heading) — L59.
(2) `/Users/cobalt/Vault/Think/6 - Permanent/Memory/topics/writing-rules.md` (your report).
(3) `/Users/cobalt/cobalt-wt/drc-d1/docs/40 - DevDocs/reports/drc-merge-main-build-2026-09-28.md` `## O OFFLINE` (the 7 reds verbatim), `## FOR 08`, `## ESCALATE`.
(4) `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/drc-merge-fix-r1-draft-2026-09-28.md` (the classification table; `## ESCALATE`).
(5) `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-28/15-drc-merge-main-build.md` `## W` (the shape W below copies).

## AUTHORIZATION — VERIFY IT YOURSELF. Written by the CTO desk (drafted by the Opus 5.5 seat `drc-merge-fix-r1-draft-0928`), not by Dejan; a prompt is not an approval. `<desk file>` = `"/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-28.md"`. Each its own Bash call:
- PLACEHOLDER GATES, first: `grep -n -E "R_[_]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-28/17-drc-merge-fix-r1-build.md"` → prints NOTHING; `grep -n -F "FILL AT LAUNCH" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-28/17-drc-merge-fix-r1-build.md"` → prints ONLY this gate's own line (any other line is an unfilled value). A hit → `FAILED: placeholder — <lines>`, stop.
- THIS LAUNCH is the desk's row R62 of `<desk file>`: `grep -n "^| R62 " <desk file>` → the row names `17-drc-merge-fix-r1-build.md`, `5bb1f4b5` and carries the literal `no with-DB run in flight`; `git -C /Users/cobalt/cobalt log -1 --format=%H -S"17-drc-merge-fix-r1-build.md" -- "docs/40 - DevDocs/reports/cto-2026-09-28.md"` NON-EMPTY.
- THE FIX-ROUND RULING: `grep -n "^| R46 " <desk file>` → the row carries `16-draft-drc-merge-fix-r1.md` and `R-ARCH as ruled`.
- THE CLASSIFICATION: `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/drc-merge-fix-r1-draft-2026-09-28.md"` NON-EMPTY; `tail -n 3 "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/drc-merge-fix-r1-draft-2026-09-28.md"` → the last non-blank line starts `DRC MERGE FIX R1 DRAFTED ·`.
Missing → `FAILED: authorization mismatch — <which>`, stop. YOU CAN ALWAYS STOP: `FAILED: <step> — <concern>` as the LAST line. ONE ASYMMETRY: while `.env` sits in the worktree or a forward migrate is applied, "stop" means W (f) FIRST.

## UNATTENDED RULES
- ONE command per Bash call, exactly a listed prefix. No pipe, no redirect, no `&&`, no `; echo`, no `$(…)`. No `VAR=` in front except the listed `COBALT_ENV=dev` and `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think` prefixes.
- Git reads are `git -C /Users/cobalt/cobalt-wt/drc-d1 …` or `git -C /Users/cobalt/cobalt …`. Git writes run from the cwd `/Users/cobalt/cobalt-wt/drc-d1`, ONLY as: `git add "<explicit path>"` (never `-A`, `.`, `-u`, a directory) · `git commit -m "…" -m "…"` (never bare: an editor is a dialog). `cd /Users/cobalt/cobalt-wt/drc-d1` is its own call before the first git write.
- Files change through the Edit tool ONLY on the 6 test files of `## THE ROWS`, and only the OLD block each row quotes. The Write tool writes ONLY your report. Nothing under `/Users/cobalt/Vault`; nothing outside this worktree.
- Long runs `run_in_background`, read whole. The migrate and the rollback in the FOREGROUND with `timeout` 600000. No sleep or wait command.
- Before every `pytest`, `COBALT_ENV=dev …` or `jobs restarts` call the preceding call is `ls -la /Users/cobalt/cobalt-wt/drc-d1/.env`: LISTED inside W (b)–(e), "No such file" everywhere else. Never print, `cat` or `grep` it.
- MID-RUN DENIAL or a dialog = the run FAILED (L62): W (f) if the lock is held, then `FAILED: <step> — <command> — <reason verbatim>`, stop. Never a retry in another spelling.
- Every output this file says to quote goes into a fenced block exactly as printed (L48).
- After the first `uv run`, `git -C /Users/cobalt/cobalt-wt/drc-d1 status --short --branch` → `## drc/d1-trading-log` plus this report's `??` line (and, before the fix commit, the 6 row files as ` M`) only. A modified `uv.lock` or any other change → `FAILED: <step> — uv run changed <path>` (the desk restores it; this build holds no restore string).

## RECOVERY (L60)
A relaunch (`CONTINUE: <step>`) runs first: `git -C /Users/cobalt/cobalt-wt/drc-d1 status` (LONG form), `git -C /Users/cobalt/cobalt-wt/drc-d1 log --oneline -3`, `ls -la /Users/cobalt/cobalt-wt/drc-d1/.env`, then reads `## CONTINUE`.
- `.env` PRESENT → W (f) FIRST, recorded, then resume.
- The row files modified and NOT committed → re-read each row's NEW block in the file (Read tool); each matches → resume at T; any mismatch → `FAILED: RECOVERY — <path> holds an edit that is not its row` (never a revert: this build holds no restore string).
- The fix commit present (`HEAD` subject `test(drc-merge): fix r1 …`) → resume at the step `## CONTINUE` names.
- The report stays UNTRACKED until CLOSE. On a FAILED stop: `git add "docs/40 - DevDocs/reports/drc-merge-fix-r1-build-2026-09-28.md"` then `git commit -m "wip(drc-merge-fix-r1): <step> — <reason>" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" -- "docs/40 - DevDocs/reports/drc-merge-fix-r1-build-2026-09-28.md"`.
THE LAST LINE WHILE YOU RUN (L71): exactly `(run in progress — next step under ## CONTINUE)`; `next: <step>` lives inside `## CONTINUE` only; no other line STARTS with `DRC MERGE FIX R1 BUILT`, `FAILED` or `CONTINUE`.

## REPORT (L48)
`/Users/cobalt/cobalt-wt/drc-d1/docs/40 - DevDocs/reports/drc-merge-fix-r1-build-2026-09-28.md`, Write tool, committed at CLOSE. Sections: `## §0 Headline` (≤5 lines) → `## L74` → `## AUTHORIZATION` → `## PREFLIGHT` → `## R0 RED` → `## THE ROWS` → `## T TARGETED` → `## FIX COMMIT` → `## O OFFLINE` → `## W WITH-DB` → `## RESTARTS` → `## FOR 08` → `## FOR THE CHECK` → `## CONTINUE` → `## ESCALATE` → last line. Every clock time from `date` in that turn. The FIRST Write (after PREFLIGHT's status read) creates it with `## CONTINUE` = `next: R0` and the pinned last line.

## PREFLIGHT — each its own call, one row each (rule · command · exit · output verbatim)
- `date` → 2026-09-28 or later; record the ET time.
- `git -C /Users/cobalt/cobalt-wt/drc-d1 status --short --branch` → EXACTLY `## drc/d1-trading-log`. Anything else → `FAILED PREFLIGHT: drc-d1 tree not quiet — <lines>`.
- `git -C /Users/cobalt/cobalt-wt/drc-d1 log --oneline -2` → `338a2439 wip(drc-merge): O — offline red on 5bb1f4b5 (7 registry position pins outside the conflict set)` over `5bb1f4b5 Merge branch 'main' into drc/d1-trading-log` (the drafter's read, 11:02 ET; a later `15` report commit directly over `5bb1f4b5` is the same state, recorded). `git -C /Users/cobalt/cobalt-wt/drc-d1 log --oneline 5bb1f4b5..HEAD -- src tests configs` → EMPTY. `git -C /Users/cobalt/cobalt-wt/drc-d1 log -1 --format=%p 5bb1f4b5` → `10163d51 daf36e01`. Anything else → `FAILED: preflight — tip moved — <lines>`.
- `git -C /Users/cobalt/cobalt log -1 --format=%h main` → record as `<main at launch>`.
- THE LOCK, read for the record: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; `ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` → "No such file".
- Write the report. `## CONTINUE`: `next: R0`.

## R0 — THE 7 REDS REPRODUCED on the preflight tip (offline, before any edit)
`ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` → "No such file". `uv run pytest -q -p no:cacheprovider tests/cobalt/test_assumed_store.py tests/cobalt/test_drc_k1_store.py tests/cobalt/test_drc_store.py tests/cobalt/test_radar_handicap_store.py tests/cobalt/test_voice_store.py tests/cobalt/test_archiver_migrations.py` (`run_in_background`) → quote the summary WHOLE and every `FAILED` line. EXPECTED `7 failed` — exactly the 7 test ids of `15`'s stop line. A different set → `FAILED: R0 — the reds are not 15's seven — <lines>` (the classification is for those seven only). Then the status rule. `## CONTINUE`: `next: ROWS`.

## THE ROWS — 8 FIX rows, tests only (the classification's F1–F8; line numbers at `5bb1f4b5`)
THE MERGED ORDER (R38 (1); `src/cobalt/db_migrations/__init__.py` at `5bb1f4b5`): FORWARD tail `…0011, 0013, 0014, 0015, 0016, 0017, 0018` → `FORWARD[-6]` = `0013` … `FORWARD[-1]` = `0018`; REVERSE head `0018, 0017, 0016, 0015, 0014, 0013, 0011, …` → `REVERSE[0]` = `0018` … `REVERSE[5]` = `0013`. `_rollback_paths("<n>")` = every REVERSE entry numbered above `<n>`, in REVERSE order.
Per row: Read the file; the OLD block must be at the stated lines VERBATIM (moved → the lines you read, recorded as `LINE MOVED`; text differs → `FAILED: ROWS — <path> old block differs — <what you read>`); Edit OLD → NEW exactly (indentation 4 spaces as shown); record `path:line · old · new` in the report.

**F1 — `tests/cobalt/test_assumed_store.py:244–252`, `test_0013_is_registered_forward_and_reverse`.** Intent: 0013 registered, 0014 directly after it, every tail slot pinned to its number. Reason: 0016 and 0018 interleave numerically, so each slot moves; the whole tail stays pinned. OLD:
```
    # 0014 (the float handicap H1) now follows it; 0013 stays directly before.
    assert FORWARD[-4].name == "0013_tunables_slug_nullable.sql"
    assert FORWARD[-3].name == "0014_radar_handicap.sql"
    assert REVERSE[3].name == "0013_tunables_slug_nullable.rollback.sql"
    assert REVERSE[2].name == "0014_radar_handicap.rollback.sql"
    assert FORWARD[-2].name == "0015_shadow_agreement_stale.sql"  # the stale-score build (R40)
    assert REVERSE[1].name == "0015_shadow_agreement_stale.rollback.sql"
    assert FORWARD[-1].name == "0017_voice_turns.sql"
    assert REVERSE[0].name == "0017_voice_turns.rollback.sql"
```
NEW:
```
    # 0014 (the float handicap H1) now follows it; 0013 stays directly before.
    assert FORWARD[-6].name == "0013_tunables_slug_nullable.sql"
    assert FORWARD[-5].name == "0014_radar_handicap.sql"
    assert REVERSE[5].name == "0013_tunables_slug_nullable.rollback.sql"
    assert REVERSE[4].name == "0014_radar_handicap.rollback.sql"
    assert FORWARD[-4].name == "0015_shadow_agreement_stale.sql"  # the stale-score build (R40)
    assert REVERSE[3].name == "0015_shadow_agreement_stale.rollback.sql"
    assert FORWARD[-3].name == "0016_drc.sql"  # DRC D1
    assert REVERSE[2].name == "0016_drc.rollback.sql"
    assert FORWARD[-2].name == "0017_voice_turns.sql"
    assert REVERSE[1].name == "0017_voice_turns.rollback.sql"
    assert FORWARD[-1].name == "0018_drc_stated_books.sql"  # DRC K1
    assert REVERSE[0].name == "0018_drc_stated_books.rollback.sql"
```

**F2 — `tests/cobalt/test_drc_k1_store.py:116–117`, `test_the_pair_exists_and_is_registered_after_0016`.** Intent: 0018 is after 0016 and last; its rollback reverses first, 0016's after it. Reason: voice V1's 0017 sits between them. OLD:
```
    assert names[-2:] == ["0016_drc.sql", "0018_drc_stated_books.sql"]
    assert REVERSE[0] == ROLLBACK and REVERSE[1].name == "0016_drc.rollback.sql"
```
NEW:
```
    assert names[-3:] == ["0016_drc.sql", "0017_voice_turns.sql", "0018_drc_stated_books.sql"]
    assert REVERSE[0] == ROLLBACK and [p.name for p in REVERSE[1:3]] == [
        "0017_voice_turns.rollback.sql", "0016_drc.rollback.sql"]
```

**F3 — `tests/cobalt/test_drc_k1_store.py:121`, `test_down_to_0016_selects_only_the_k1_rollback`.** Intent: the bound 0016 selects every rollback above it, newest first, never 0016's own. Reason: 0017 is above 0016, so `--down-to 0016` reverses it too (selection by number, `_rollback_paths`). OLD:
```
    assert [p.name for p in _rollback_paths("0016")] == ["0018_drc_stated_books.rollback.sql"]
```
NEW:
```
    # every rollback newer than 0016, newest first — voice V1's 0017 sits between (numeric order)
    assert [p.name for p in _rollback_paths("0016")] == [
        "0018_drc_stated_books.rollback.sql", "0017_voice_turns.rollback.sql"]
```

**F4 — `tests/cobalt/test_drc_store.py:65–66`, `test_the_pair_exists_and_is_registered_last`.** Intent: 0016's pair sits at its numeric slot with every newer slot pinned. Reason: 0017 and 0018 follow 0016. OLD:
```
    assert FORWARD[-2] == SQL and FORWARD[-1].name == "0018_drc_stated_books.sql"
    assert REVERSE[1] == ROLLBACK and REVERSE[0].name == "0018_drc_stated_books.rollback.sql"
```
NEW:
```
    assert FORWARD[-3] == SQL and [p.name for p in FORWARD[-2:]] == [
        "0017_voice_turns.sql", "0018_drc_stated_books.sql"]
    assert REVERSE[2] == ROLLBACK and [p.name for p in REVERSE[:2]] == [
        "0018_drc_stated_books.rollback.sql", "0017_voice_turns.rollback.sql"]
```

**F5 — `tests/cobalt/test_drc_store.py:140–143`, `test_down_to_0011_on_this_tree_selects_only_this_rollback`.** Intent: the bound 0011 selects every rollback above it, newest first, 0011 excluded. Reason: the merged tree carries main's 0013, 0014, 0015 and 0017 above 0011. OLD:
```
    assert [p.name for p in _rollback_paths("0011")] == [
        "0018_drc_stated_books.rollback.sql",
        "0016_drc.rollback.sql",
    ]
```
NEW:
```
    assert [p.name for p in _rollback_paths("0011")] == [
        "0018_drc_stated_books.rollback.sql",
        "0017_voice_turns.rollback.sql",
        "0016_drc.rollback.sql",
        "0015_shadow_agreement_stale.rollback.sql",
        "0014_radar_handicap.rollback.sql",
        "0013_tunables_slug_nullable.rollback.sql",
    ]
```

**F6 — `tests/cobalt/test_radar_handicap_store.py:84–86`, `test_down_to_0013_selects_only_this_rollback`.** Intent (its own comment, `:83`, kept): every rollback newer than 0013, newest first, 0014 the oldest. Reason: the branch's 0016 and 0018 are above 0013. OLD:
```
    assert [p.name for p in _rollback_paths("0013")] == [
        "0017_voice_turns.rollback.sql", "0015_shadow_agreement_stale.rollback.sql",
        "0014_radar_handicap.rollback.sql"]
```
NEW:
```
    assert [p.name for p in _rollback_paths("0013")] == [
        "0018_drc_stated_books.rollback.sql", "0017_voice_turns.rollback.sql",
        "0016_drc.rollback.sql", "0015_shadow_agreement_stale.rollback.sql",
        "0014_radar_handicap.rollback.sql"]
```

**F7 — `tests/cobalt/test_voice_store.py:57–58`, `test_both_files_exist_and_are_registered_last_and_first`.** Intent: 0017's pair at its numeric slot; the bound 0015 selects every rollback above it, newest first. Reason: 0018 follows 0017 and 0016 is above 0015. OLD:
```
    assert FORWARD[-1] == SQL and REVERSE[0] == ROLLBACK
    assert [p.name for p in _rollback_paths("0015")] == ["0017_voice_turns.rollback.sql"]
```
NEW:
```
    assert FORWARD[-2] == SQL and REVERSE[1] == ROLLBACK
    assert [p.name for p in _rollback_paths("0015")] == [
        "0018_drc_stated_books.rollback.sql", "0017_voice_turns.rollback.sql",
        "0016_drc.rollback.sql"]
```

**F8 — `tests/cobalt/test_archiver_migrations.py:160–167`, the docstring of `test_the_registry_is_an_explicit_contiguous_list_and_reverse_mirrors_it`.** R-ARCH as ruled (`15` `## BOTH-SIDES`; R46 answer to `15` ASK DESK 3): the branch's registry-pin paragraph is dropped; the docstring ends as main's. Not a red. OLD:
```
    never by position.

    DRC D1 (`drc/d1-trading-log`) adds 0016 on a `main` base. 0012–0015
    are the SIBLINGS', absent from this tree: 0012 `bars/chunk-2-0920`
    (`0012_bars_partitioned_parent`, unmerged), 0013 `setups/seven-0921`
    (`0013_tunables_slug_nullable`), 0014 handicap H1
    (`0014_radar_handicap`, reserved), 0015 stale score (reserved,
    conditional). The combined pin is written at the L68 gate."""
```
NEW:
```
    never by position."""
```
Proof after F8: `git -C /Users/cobalt/cobalt show daf36e01:tests/cobalt/test_archiver_migrations.py` → the same docstring ends `never by position."""` (quote its line).

NOT BUILT (the classification's UNPROVEN rows U1 / U2, L70): `tests/cobalt/test_stale_score_db.py:156–162` and `tests/cobalt/test_radar_handicap_store.py:170–194` are with-DB tests the offline run skipped; nobody has run them on the merged tree. Never edited here. A red on either in W (c1) is a RESULT: quote it whole, then W (f), then `FAILED: W (c1) — with-DB pass 1 red — <tests + assertions verbatim>` (the desk rules the next round from it).
`## CONTINUE`: `next: T`.

## T — TARGETED (offline), then the fix commit
- `git -C /Users/cobalt/cobalt-wt/drc-d1 diff --stat` → quote; EXACTLY the 6 row files. `git -C /Users/cobalt/cobalt-wt/drc-d1 diff` → quote WHOLE (the check reads it against the rows).
- `ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` → "No such file". The R0 command again (`run_in_background`) → EXPECTED `0 failed`, `0 errors`; quote the summary WHOLE. A red → `FAILED: T — <tests + assertions verbatim>` (never a second edit beyond its row: a row that cannot hold its intent is the desk's).
- `cd /Users/cobalt/cobalt-wt/drc-d1`. `git add "<path>"` for each of the 6 row files, one call each. `git commit -m "test(drc-merge): fix r1 — registry pins re-stated to the merged numeric order" -m "R38 (1) / R46: 7 single-side position pins on the migration registry moved to 0013…0018 numeric order (5 files); the branch's registry-pin docstring paragraph dropped (R-ARCH). Tests only (drc-merge-fix-r1-draft-2026-09-28.md F1–F8)." -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"`. `date`.
- PROOF: `git -C /Users/cobalt/cobalt-wt/drc-d1 log -1 --format=%h%x20%p` → `<fix tip>`, parent `338a2439` (or the preflight tip). `git -C /Users/cobalt/cobalt-wt/drc-d1 show --stat --format=%h <fix tip>` → quote; the paths are EXACTLY the 6 files under `tests/cobalt/`. Any other path → `FAILED: T — the fix commit is not tests only — <paths>`.
`## CONTINUE`: `next: O`.

## O — OFFLINE on `<fix tip>`
`ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` → "No such file". `uv run pytest -q -p no:cacheprovider tests/cobalt tests/taxonomy` (`run_in_background`) → GATE `0 failed`, `0 errors`; quote the summary WHOLE → `<p>`. EXPECTED `3547 passed` (`15`'s O: 7 failed + 3540 passed = 3547 ran; the 7 now pass) and `15`'s `525 skipped, 1 xfailed`; a different passed or skipped count is named against 3547 / 525, not a stop. Then the status rule. A red → name each test, quote each assertion, `FAILED: O — offline red on <fix tip> — <tests>` (never an edit; the desk rules). `## CONTINUE`: `next: W`.

## W — WITH-DB on `cobalt_dev` UNDER L76, then the live-note leg — `15`'s W exactly. Order (a) → (b) → (c1) → (c2) → (d) → (e) → (f).
`<FP>` typed EXACTLY: `COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`.
- (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; a listed file → you do NOT hold the lock: `FAILED: W — cobalt_dev lock held — <path>` (relaunched `CONTINUE: W`). `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/drc-d1/.env` (by name, never read or printed, L4 / L41); `ls -la /Users/cobalt/cobalt-wt/*/.env` → EXACTLY one line, ours. Record `L76 lock taken <time>`.
- (b) `<FP>` → `<F0>`. `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → quote; EXPECTED `cobalt_dev` at `0013`. Any other level or a `CHANGED` → (f) step 3, then `FAILED: W — cobalt_dev not at 0013 before the build — <line>`.
- (c1) PASS 1 at `0013`: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped` (`run_in_background`; copy the executed command WHOLE into the report). GATE `0 failed`, `0 errors`, `9 deselected` → `<d1>`; quote every `SKIPPED` line. A red → (f) step 3, then `FAILED: W (c1) — with-DB pass 1 red — <tests + assertions verbatim>`. `DeadlockDetected` is a red: name it, never re-run it here. (U1 / U2 of `## THE ROWS` run here for the first time on the merged tree.)
- (c2) FORWARD: `COBALT_ENV=dev uv run cobalt db migrate` (FOREGROUND, `timeout` 600000) → quote. EXPECT `0014`, `0015`, `0016`, `0017`, `0018` applied in that order, every pre-existing table `OK`, no `CHANGED`; created: `drc_imports`, `drc_fills`, `drc_rows`, `drc_stated_books`, `voice_turns`. Record **`dev forward: APPLIED <time>`** the moment it returns — from here every ending runs (f). `<FP>` → `<F1>`. Anything else → (f), then `FAILED: W (c2) — forward migrate — <output verbatim>`.
- (d) PASS 2 at `0018`: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_tenancy.py::TestMigrationRoundTrip tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped` (`run_in_background`; copy the executed command WHOLE). GATE `0 failed`, `0 errors`, `9 passed` → `<d2>`. A red → (f), then `FAILED: W (d) — with-DB pass 2 red — <tests + assertions verbatim>`. `<d>` = `<d1>` + `<d2>`.
- (e) LIVE-NOTE (read-only on his notes): `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → GATE `0 failed`, no skip naming `COBALT_LIVE_VAULT_ROOT` (the `COBALT_TEST_LIVE_DRC` skip is known) → `<l>`. A red → (f), then `FAILED: W (e) — live-note <red|skipped> — <lines>`.
- (f) ALWAYS from the moment (c2) returned, on green or red:
  1. `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (FOREGROUND, `timeout` 600000) → quote: `0018`, `0017`, `0016`, `0015`, `0014` reversed newest first, nothing at or below `0013`.
  2. `<FP>` → `<F2>` MUST equal `<F0>` field for field → **`cobalt_dev: 0013 — F2 = F0 (<cols> · <rels> · <views_md5>)`**. Unequal → never retried: `ESCALATE 0: cobalt_dev NOT back at 0013 — F0 <…> F2 <…>; the desk repairs before any with-DB launch`, still step 3, and the run ends `FAILED: W (f) — cobalt_dev not restored`.
  3. `rm /Users/cobalt/cobalt-wt/drc-d1/.env`; `ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` → "No such file"; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`. Record **`.env: removed, proven gone (L76 lock released <time>)`**.
  A stop line written while `.env` is on disk, or while `dev forward: APPLIED` has no `F2 = F0` line after it, is itself a failure. A failure before (c2) runs step 3 only.
`## CONTINUE`: `next: RESTARTS`.

## RESTARTS (L42)
`ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` → "No such file". `uv run cobalt jobs restarts 10163d51..<fix tip>` (explicit shas) → quote the table WHOLE and its exit code. `RESTARTS:` in the stop line = the table's last line after `RESTARTS: `, never trimmed. An `UNCLASSIFIED` row → `ESCALATE: UNCLASSIFIED <path>` (the DRC deploy's L42 item), not a stop. `## CONTINUE`: `next: CLOSE`.

## `## FOR 08` — write it WHOLE, re-issued (the desk re-points `08`–`11` from it; it supersedes `15`'s partial `## FOR 08`)
- `<fix tip>` and its parent; `5bb1f4b5` (the merge commit) with its two parents `10163d51` `daf36e01`; `<main at launch>`; the branch is `<n>` commits ahead of main (`git -C /Users/cobalt/cobalt rev-list --count main..drc/d1-trading-log`) and `<m>` behind (`git -C /Users/cobalt/cobalt rev-list --count drc/d1-trading-log..main`; main moved docs-only since `daf36e01` → `git -C /Users/cobalt/cobalt diff --stat daf36e01 main -- . ':(exclude)docs'` quoted; non-empty → `ESCALATE: main moved with code since the merge — <paths>`).
- FORWARD and REVERSE as merged, quoted from `git -C /Users/cobalt/cobalt-wt/drc-d1 show HEAD:src/cobalt/db_migrations/__init__.py`, with the line numbers of the `0018` FORWARD and REVERSE entries (`grep -n -F "0018_drc_stated_books" "/Users/cobalt/cobalt-wt/drc-d1/src/cobalt/db_migrations/__init__.py"`). Next free: `0019` (`08`'s `drc_events`), `0020` (D3), `0021` (S3 exits C1, off main).
- The anchors `08`–`11` cite, each `grep -n -F` on the fix tip's tree: `"drc_stated_books": Side.USER` (placement.py) · `@app.post("/attest"` and `@app.get("/drc"` and `def radar_card_release` (web.py) · `drc_cli.add_parser` (cli.py) · `MIN_N_FOR_AVERAGE` · `STRATEGIES_DIR` (vault_loader.py).
- The counts on the fix tip: `15`'s `<p0>` (2588 on `10163d51`) → `<p>` offline; `<d1>` + `<d2>` = `<d>` with-DB; `<l>` live-note; `<F0>` / `<F1>` / `<F2>`.
- THE WITH-DB DESELECT SET: on the merged tree the voice tests need `0017` applied, so `08`'s three `--deselect` arguments (four tests) no longer describe a green pass at `0013`; the set W (c1) ran with (eight arguments, nine tests) is the merged tree's.
- THE REGISTRY PINS `08` MUST RE-STATE when it adds `0019`: every `FORWARD[-n]` / `REVERSE[n]` / `names[-n:]` / `_rollback_paths` list of `test_assumed_store.py`, `test_drc_k1_store.py`, `test_drc_store.py`, `test_radar_handicap_store.py`, `test_voice_store.py`, `test_stale_score_db.py` and the five R-PINS / R-ARCH files (`grep -n -F "0018_drc_stated_books" "/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/<file>"`, one call per file, the hits listed).
- RESTARTS as derived.
- `CLAUDE.md` in the worktree is main's stub (R33 (4)).

## `## FOR THE CHECK`
R0's summary and FAILED lines; T's `git diff --stat` and `git diff` WHOLE; the fix commit's `show --stat`; F8's main-docstring proof line; the three suites' summaries; W's two executed commands; `<F0>` / `<F1>` / `<F2>`; the lock times; the RESTARTS table; every `LINE MOVED`; the statement `no path edited outside the 6 row files; no row edited beyond its OLD block`.

## CLOSE
- `## ESCALATE`: every `ASK DESK`, every `ESCALATE` line, the L74 line if a block arrived.
- `## §0 Headline` (≤5 lines): `<fix tip>` on `5bb1f4b5`; 8 rows, tests only; the three results; `cobalt_dev: 0013`; RESTARTS.
- Write the stop line. Then `git add "docs/40 - DevDocs/reports/drc-merge-fix-r1-build-2026-09-28.md"` and `git commit -m "docs(drc-merge): DRC merge fix r1 build report — <fix tip>" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" -- "docs/40 - DevDocs/reports/drc-merge-fix-r1-build-2026-09-28.md"`. Then quote in your final chat message: `git -C /Users/cobalt/cobalt-wt/drc-d1 status --short --branch` → `## drc/d1-trading-log`; `git -C /Users/cobalt/cobalt-wt/drc-d1 log --oneline -3` → the report commit over `<fix tip>` over `338a2439`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`.
- STOP LINE (L71), the LAST NON-BLANK line, exactly:
`DRC MERGE FIX R1 BUILT <fix tip> | on 5bb1f4b5 | tests only: <n> files | offline <p>/0 | with-DB <d>/0 | live-note <l>/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: <as derived> | FIX: <n> | ESCALATE: <n>`
  — `<n> files` from the fix commit's `show --stat` (EXPECTED 6); `<p>`, `<d>`, `<l>` passed counts; `/0` failed; `FIX: <n>` rows built (EXPECTED 8) — or `FAILED: <step> — <reason>` / `FAILED PREFLIGHT: <rule>`.
  While you run, the last line is `(run in progress — next step under ## CONTINUE)`.
