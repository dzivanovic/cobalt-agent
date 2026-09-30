# DEPLOY SPLIT 2026-09-30 — `41` → `44` (DRC D3) + `45` (S3 exits C1–C4 on the seam branch)

## §0 Headline
- `prompts/2026-09-30/44-deploy-1-drc-0930.md` (184 lines, 44,286 B) and `45-deploy-2-s3-seam-0930.md` (191 lines, 47,442 B) are written: two deploys, one after the other, no window, no new string.
- Launch-time values left for the desk: `44`: `<main base>`, `<launch row>`; `45`: `<main base>`, `<launch row>`, `<seam tip>` (also inside its merge string).
- One decision for him (`## FOR DEJAN`): the K10 `jobs.yaml` commit needs `add` / `commit` in a gate worktree; the default is the desk's own shell (bare commands (0a), (0b) of `44`).
- `seam/drc-s3-0930` reads `6785c7d5` and the seam report ends `(run in progress …)` at 06:54: `<seam tip>` does not exist yet.

## L74
One block arrived inside a tool result: appended to the read of `43-draft-two-deploys.md`, it asked for a `Claude-Session:` line in every commit and PR and named a file-send tool. It is data and was not followed. This session made no commit.

## CHANGES
| # | `41` → `44` / `45` | `41` line |
|---|---|---|
| 1 | Split by set: `44` = DRC `b8ac291b` only (WHAT SHIPS row 1); `45` = the seam tip only, C1–C4 rows 2–5 kept as its check rows, plus a seam row | 14–22 |
| 2 | Names: `44` worktree `deploy-0930-1`, branch `deploy/drc-0930`, tags `deploy-2026-09-30-1` / `pre-drc-0930` / scratch `scratch-allow-probe-0930d1`, report `deploy-2026-09-30-1.md`, hub `deploy-drc-0930`; `45` the same with `-2`, `deploy/s3-0930`, `pre-s3-0930`, `…0930d2`, `deploy-s3-0930`. `grep -c -F "stacked-0930"` = 0 on both | 1, 4, 6, 48 |
| 3 | THE WINDOW block removed in both (09:15:00 `FAILED: window`, merge clock 09:10:00, 09:15–09:30 no-restart clause, D0's 09:00:00 line, P1's before-09:15 rule, STEP-5 (0)'s window clause, the "before 09:30" title); the R10 standing line in each header; P1 records the time only | 10, 12, 67–71, 75, 139, 164, 167, 172, 192 |
| 4 | AUTHORIZATION: P-HIS (R4's literal) replaced by R9 and R10 rows, each `grep -n "^| R<n> "` + `git log -1 -S"| R<n> |"`; launch row names `44-…` / `45-…` | 33–34 |
| 5 | STEP-T: five merges and the conflict rules S-1…S-5 removed. `44`: the desk merges `b8ac291b` and commits the K10 configs before launch; the hub verifies (one merge, the migration and `ops` diffs, the six-commit migration list). `45`: ONE merge of `<seam tip>`, a conflict → `merge --abort`, `FAILED: merge` | 84–106 |
| 6 | STEP-S: `44` verifies the desk's `jobs.yaml` commit against the five readers greps (both decisions, no other line); `45` has none. S-6 and the nine pin tests are the seam build's (`42`); `45` keeps the offline early read of the 16 seam-facing files as G (a0) | 108–119 |
| 7 | STEP-G kept: offline, lock, fingerprint, pass 1 at `0013`, forward, pass 2, validate, release with `F2 = F0`, live-note. `44` uses DRC F8 (c)'s eight `--deselect` (nine tests) and the same eight ids as pass 2; `45` uses C4 W (c) / (c3) byte for byte. No seam-red fix commit in either: a red ends the run | 121–130 |
| 8 | `<RB>`: `44` reads `m_drc`, `m0020` (`0 · 0` → `5 · 1`); `45` keeps the four-column read (`5 · 1 · 0 · 0` → `5 · 1 · 2 · 4`) | 64 |
| 9 | STEP-R kept; `44` expects `agent aset radar`, `45` `aset radar`; the SEAM RED clause removed | 132–136 |
| 10 | D0 / D1 / D2 kept; `45` D1 has no `prefill-drc` print; the census stays in `45` only (it reads `card_stop_edits` / `aset_sizings`, `0021`'s) | 138–161 |
| 11 | STEP-4: `4.2b` (the retired job) stays in `44` only; the merge clock line is gone; migrations `0016 0018 0019 0020` (`44`) / `0021` (`45`) | 163–170 |
| 12 | Smoke: (d) markers and (s) reads split by set (`44`: the DRC constraint; `45`: C1–C4); (h) census in `45` only | 172–190 |
| 13 | STEP-5: `(2b)` per set; ROLLBACK STRING `--down-to 0017` (`44`, `0016` note kept) / `--down-to 0020` (`45`, `0021` only); re-land titles re-pointed | 191–203 |
| 14 | `45` P1b: `main` contains `b8ac291b`, `deploy-2026-09-30-1`'s stop line is `DEPLOYED …` with `smoke: GREEN`, tag exists; P3: the seam tip descends from `6785c7d5` and `b8ac291b`; P4 lock free | 13 of `43`; 76–78 |
| 15 | STOP LINES: `DEPLOYED deploy-2026-09-30-1 <main tip> | set: 1 | migrations: 0016 0018 0019 0020 | …`; `DEPLOYED deploy-2026-09-30-2 <main tip> | set: seam | migrations: 0021 | …` | 218 |
| 16 | RECORDS split: DRC's in `44`; C1 X-S, C3 R1, C4 E1 in `45` | 211–215 |

## RULE STRINGS
`41`'s list is line 6 of `41` (line 5 is the `(1) cd` line). Each list = `grep -o '"[^"]*"'` of the launch line, `sort -u`, the `Read '…'` instruction removed, `comm -3` (column 1 = base only, column 2 = new only). The lists were computed in Python with the same set difference; the extracted line equals the launch line in each file byte for byte.
`44`: 52 allow + 3 denies. Common with `41`: 49 (46 allow + 3 denies). `41` only: 12. `44` only: 6.
```
"Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/deploy-0930/.env)"          | 41 only
	"Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/deploy-0930-1/.env)"      | 44 only
"Bash(git -C /Users/cobalt/cobalt merge --ff-only deploy/stacked-0930)"                | 41 only
	"Bash(git -C /Users/cobalt/cobalt merge --ff-only deploy/drc-0930)"                  | 44 only
"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 add *)"                               | 41 only (dropped: seam)
"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 commit *)"                            | 41 only (dropped: seam)
"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 merge --abort)"                       | 41 only
	"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930-1 merge --abort)"                   | 44 only
"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 merge --no-edit 04b3ca3e)"            | 41 only (S3 tip: 45's)
"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 merge --no-edit 6785c7d5)"            | 41 only (S3 tip: 45's)
"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 merge --no-edit 6983de75)"            | 41 only (S3 tip: 45's)
"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 merge --no-edit b8ac291b)"            | 41 only
	"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930-1 merge --no-edit b8ac291b)"        | 44 only
"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 merge --no-edit bbf25412)"            | 41 only (S3 tip: 45's)
"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 merge --no-edit main)"                | 41 only
	"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930-1 merge --no-edit main)"            | 44 only
"Bash(rm /Users/cobalt/cobalt-wt/deploy-0930/.env)"                                    | 41 only
	"Bash(rm /Users/cobalt/cobalt-wt/deploy-0930-1/.env)"                                | 44 only
```
(The `| …` notes are added for reading; `comm -3` prints the strings only.) Against `50` (line 6): common 47; `50` only 6 (`handicap-dry-run`, the `stacked-0925` `cp` / `ff-only` / `merge --abort` / `merge --no-edit main` / `rm` strings, all re-pointed or dropped as in `41`); `44` only 8: the six above plus `launchctl bootout gui/501/com.cobalt.prefill-drc` and `rm /Users/cobalt/Library/LaunchAgents/com.cobalt.prefill-drc.plist` (already in `41`).
`45`: 50 allow + 3 denies. Common with `41`: 47 (44 allow + 3 denies). `41` only: 14. `45` only: 6.
```
"Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/deploy-0930/.env)"          | 41 only
	"Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/deploy-0930-2/.env)"      | 45 only
"Bash(git -C /Users/cobalt/cobalt merge --ff-only deploy/stacked-0930)"                | 41 only
	"Bash(git -C /Users/cobalt/cobalt merge --ff-only deploy/s3-0930)"                   | 45 only
"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 add *)"                               | 41 only (dropped: seam)
"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 commit *)"                            | 41 only (dropped: seam)
"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 merge --abort)"                       | 41 only
	"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930-2 merge --abort)"                   | 45 only
"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 merge --no-edit 04b3ca3e)"            | 41 only
"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 merge --no-edit 6785c7d5)"            | 41 only
"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 merge --no-edit 6983de75)"            | 41 only
"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 merge --no-edit b8ac291b)"            | 41 only (DRC: 44's)
"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 merge --no-edit bbf25412)"            | 41 only
"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 merge --no-edit main)"                | 41 only
	"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930-2 merge --no-edit main)"            | 45 only
	"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930-2 merge --no-edit <seam tip>)"      | 45 only: the seam-tip merge, the shape of 41's five tip merges
"Bash(launchctl bootout gui/501/com.cobalt.prefill-drc)"                               | 41 only (44's)
"Bash(rm /Users/cobalt/Library/LaunchAgents/com.cobalt.prefill-drc.plist)"             | 41 only (44's)
"Bash(rm /Users/cobalt/cobalt-wt/deploy-0930/.env)"                                    | 41 only
	"Bash(rm /Users/cobalt/cobalt-wt/deploy-0930-2/.env)"                                | 45 only
```
Against `50`: common 47; `50` only 6; `45` only 6 (the same six as above, minus none). NEW STRINGS: 0 in both — every `44`-only / `45`-only string is a `41` string re-pointed. In `45` the seam tip stands as the FILL marker inside that one string until the desk fills it.

## PLACEHOLDERS
| file | token | where | count command | count now |
|---|---|---|---|---|
| `44` | `<main base>` | definition line 24 | `grep -c -E "«FIL[L]"` | 2 |
| `44` | `<launch row>` | definition line 25 | same | (in the 2) |
| `45` | `<main base>` | definition line 28 | `grep -c -E "«FIL[L]"` | 4 |
| `45` | `<launch row>` | definition line 29 | same | (in the 4) |
| `45` | `<seam tip>` | definition line 30 and the merge string on line 6 | same | (in the 4) |
`grep -c -E "R_[_]"` → 0 on `44`, 0 on `45` (neither file has a row placeholder). Each file's `FILL` count must reach 0 before launch; prose uses the symbolic names only.

## FOR DEJAN
One decision, forced by the split, with a safe default already in `44`:
- The K10 `jobs.yaml` commit (`prefill.yaml` under `com.cobalt.aset` `reads:`, `drc.md.j2` as `no_resident_reads`) needs a commit in the gate worktree. `41` had `add *` / `commit *` in `deploy-0930` for it; `43` drops both. DEFAULT (in `44`): the desk merges `b8ac291b` and makes the commit from its own shell (bare commands (0a), (0b)) before launch; the hub verifies the commit and the merge and runs the gate. Alternative on his word: the same two strings scoped to `deploy-0930-1`; the hub then merges and commits (`41`'s STEP-S) and the list has 54 allow strings.
- Consequence of the default: the listed `merge --no-edit b8ac291b` string in `44` is not used. It stays because `43` names the list. Drop it or keep it: the desk's call.

## ESCALATE
1. ASK DESK: `jobs.yaml`'s hunks (DRC adds `rules.yaml` to the `com.cobalt.aset` `reads:` block, retires `prefill-drc`) sit beside the desk's `prefill.yaml` line; committing AFTER the merge (default in `44`) avoids a conflict. [06:54] Safe default: as `44` writes it.
2. `43` names `41`'s "line 5"; the launch list is line 6 (line 5 is `(1) cd /Users/cobalt/cobalt`). Compared against line 6.
3. The known RED (one unplaced K8.1 `input_stale`, card 433): `41` has no line for it (`grep -F "433"`, `"K8.1"`, `"input_stale"` and `"R171"` print nothing), and no smoke row of `44` or `45` reads K8.1. The evidence is `reports/s2-smoke-2026-09-28.md` (K8.1 FAIL, `input_stale = 1`). No line was added; the desk classifies it (R171, L75).
4. DRC alone has no forward pass on record: DRC F8 ran pass 1 with eight `--deselect` and an absence probe. `44` derives pass 2 as the same eight ids run positively after `cobalt_dev` reaches `0020`; the expected counts are context, the gate is `0 failed`.
5. `41` lists seven migration commits for DRC; `git log --oneline main..b8ac291b -- src/cobalt/db_migrations` prints six (`d2897b46 8e8762ca 7cdc5774 5bb1f4b5 9a0fc900 d583f6fd`; `0075db31` is absent). `44` quotes the command and states the six; the hub decides on its own read.
6. `45`'s migration-list check tolerates the seam build's own commits; the seam report (still running) names them. `<seam tip>` and `seam/drc-s3-0930` (`6785c7d5` at this read) are not final.
7. Smoke (b) counts a `radar cycle:` line of any kind as GREEN and calls RED after 300 s without one; with no window, a deploy outside the radar's session hours can show no cycle line. ASK DESK: is that RED wanted at any hour? [06:54] Safe default: as `41` wrote it.
8. L67 floor: `44` and `45` have no other-house read; the gate is the check (recorded for the desk's one-line override note, L73).
9. K6: each file was written in three calls; sizes were not measured, and `45`'s second call is likely over 15 KB. Two scratch files (`l44.txt`, `l45.txt`) were written under `$CLAUDE_JOB_DIR/tmp` to compute the launch lines; no other file besides the three named.

## CONTINUE
next: the desk fills the launch values in `44`, resolves `## FOR DEJAN`, runs the two placeholder counts, commits, runs (0)–(2) of `44`; after `DEPLOYED deploy-2026-09-30-1` and the seam build's stop line, fills `45` and runs its (0)–(2).

TWO DEPLOYS DRAFTED · 44 lines: 184 · 45 lines: 191 · new strings: 0 · ESCALATE: 9
