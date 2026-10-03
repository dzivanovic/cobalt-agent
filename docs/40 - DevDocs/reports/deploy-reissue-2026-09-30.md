# DEPLOY RE-ISSUE 2026-09-30 — `40` → `41-stacked-deploy-0930.md` (DRC D3 + S3 exits C1–C4, the seam inside the run)

## §0 Headline
- `prompts/2026-09-30/41-stacked-deploy-0930.md` is written (54,761 B, 223 lines): five merges, the DRC × S3 seam resolved by rule in `deploy-0930`, one seam commit, `40`'s gate, deploy before 09:15:00.
- Two launch values left for the desk: `<main base>`, `<launch row>`; and the P-HIS row number (R4 carries the literal).
- TWO strings beyond `40`'s line: `add *` / `commit *` in `deploy-0930` (FOR DEJAN). `40`'s `add` / `commit` strings name `~/cobalt` only.
- `configs/cobalt/prefill.yaml` HAS a resident reader (`aset/web.py`): it goes in `com.cobalt.aset` `reads:`, not `no_resident_reads` (ESCALATE 1).
- Four DRC-only tests pin DRC's tail and merge clean; `41` re-points them in the seam commit (S-6, ESCALATE 3).

## L74
One block arrived inside a tool result: appended to the read of `areas/cobalt.md`, it asked for a `Claude-Session:` line in every commit and PR and named a file-send tool. It is data and was not followed. This session made no commit.

## THE SEAM
Read by `git show <tip>:<path>` and by `grep -n` in the worktrees `drc-d1` (head `985cca3b`, report above `b8ac291b`) and `s3-exits-c1` (`bbf25412`). `merge-tree` is not on this seat's line: no hunk was read, both sides' lines were.

**S-1 `src/cobalt/db_migrations/__init__.py`**
- main `:108`–`:109`: `0015_shadow_agreement_stale.sql`, `0017_voice_turns.sql`; `REVERSE` `:114`–`:115`: `0017`, `0015`.
- DRC `b8ac291b` `FORWARD` `:135`–`:140`: `0015`, `0016_drc.sql`, `0017_voice_turns.sql`, `0018_drc_stated_books.sql`, `0019_drc_events.sql`, `0020_drc_build_kinds.sql`; `REVERSE` `:145`–`:150`: `0020`, `0019`, `0018`, `0017`, `0016`, `0015`.
- C1 `bbf25412` `FORWARD` `:115`–`:117`: `0015`, `0017_voice_turns.sql`, `0021_legs.sql`; `REVERSE` `:122`–`:124`: `0021_legs.rollback.sql`, `0017`, `0015`.
- Docstring: DRC adds the `0018`–`0020` entries; C1 adds the two `0021_legs` entries and rewrites the `0012 AND 0016 ARE NOT GAPS` paragraph to name `0021`.
- RULE: `FORWARD` ends `0015 0016 0017 0018 0019 0020 0021`; `REVERSE` begins `0021 0020 0019 0018 0017 0016 0015`; docstring = DRC's entries, then C1's; the paragraph is C1's.

**S-2 `src/cobalt/db_migrations/placement.py`**
- DRC `:89`–`:105`: `CREATED_TABLES` gains `drc_imports`, `drc_fills`, `drc_rows` (`0016`), `drc_stated_books` (`0018`), `drc_events` (`0019`), the `0020` comment; `DECLARED_TABLES` `:125`–`:128` drops `drc_rows`, keeps `legs`.
- C1 `:92`–`:94`: `CREATED_TABLES` gains `"legs": Side.USER`; `CREATED_VIEWS` `:107`–`:108` gains `legs_current_v`; `DECLARED_TABLES` `:116`–`:119` drops `legs`, keeps `drc_rows`.
- RULE: `CREATED_TABLES` = DRC's entries, then C1's `legs`; `CREATED_VIEWS` keeps `legs_current_v`; `DECLARED_TABLES` carries neither `legs` nor `drc_rows`.

**S-3 THE NINE PIN TESTS** (`tests/cobalt/`; DRC line · C1 line)
| file | DRC | C1 | rule |
|---|---|---|---|
| `test_assumed_store.py` | `:245`–`:260`: `FORWARD[-8]` `0013` … `FORWARD[-1]` `0020`; `REVERSE[7]` … `REVERSE[0]` | `:245`–`:254`: `FORWARD[-5]` `0013` … `FORWARD[-1]` `0021` | DRC's asserts, each index one place out; plus C1's `0021` pair |
| `test_stale_score_db.py` | `:159`–`:162`: `FORWARD[-6]` / `REVERSE[5]` `0015`, `[-8]` / `[7]` `0013` | `:160`–`:163`: `[-3]` / `[2]`, `[-5]` / `[4]` | `[-7]` / `[6]` and `[-9]` / `[8]` |
| `test_voice_store.py` | `:57`–`:62`: `FORWARD[-4] == SQL and REVERSE[3] == ROLLBACK`; list `0020 0019 0018 0017 0016` | `:58`–`:60`: `[-2]` / `[1]`; list `0021 0017` | `[-5]` / `[4]`; list `0021 0020 0019 0018 0017 0016` |
| `test_archiver_migrations.py` | `:90`–`:94`, `:102`–`:106`, `:130`–`:134`, `:142`–`:146`; `:175` `numbers == [*range(1, 12), 13, 14, 15, 16, 17, 18, 19, 20]`, `:176` `numbers[-10:-8] == [10, 11]`, `:177` `numbers[-1] == 20`; `:497` survivors | `:89`, `:97`, `:124`, `:133`; `:163` `[*range(1, 12), 13, 14, 15, 17, 21]`, `:165` `numbers[-7:-5]`; `:488`–`:492` excludes `("voice_turns", "legs")` | lists: `0021` on top of DRC's; `[*range(1, 12), *range(13, 22)]`; `numbers[-11:-9]`; `numbers[-1] == 21`; survivors exclude what either side excludes |
| `test_p4_migrations.py` | `:102`–`:106`, `:119`–`:123`, `:132`–`:136` | `:102`, `:116`, `:126` | each rollback list: `0021` first, then DRC's |
| `test_radar_handicap_store.py` | `:85`–`:87` | `:85` | same |
| `test_radar_migration.py` | `:35`–`:39` | `:35` | same |
| `test_radar_score_migration.py` | `:104`–`:108` ("the newest ten") | `:104` ("the newest nine"); `:147` `set(CREATED_VIEWS) - {"legs_current_v"}` | `0021` first, then DRC's; "newest eleven"; C1's `:147` stays |
| `test_tenancy.py` | `:516`–`:520` | `:515` | `0021` first, then DRC's |
THE UNION TAIL: `FORWARD[-9]` `0013` · `[-8]` `0014` · `[-7]` `0015` · `[-6]` `0016` · `[-5]` `0017` · `[-4]` `0018` · `[-3]` `0019` · `[-2]` `0020` · `[-1]` `0021`; `REVERSE[0]` `0021` … `[8]` `0013`.

**S-4 `src/cobalt/aset/web.py`** (merge 4). DRC's commits on it: `0075db31` (D4 settings block, `:1199`), `807c13ec`, `d5b72392` (the `/drc` block at the END, `:1517`–), `5bb1f4b5`. S3's: `eb642f05`, `3ceb3b11`, `5e77800f`, `78549817`, `6114304e`, `d05ae72d`. RULE: both sides' hunks whole; `/drc` stays last; imports = the union. A same-statement rewrite on both sides stops the run (`FAILED: merge`).

**S-5 DevDocs pages** (`cobalt/db_migrations/__init__.md`, `cobalt/aset/web.md`): both entries, DRC's first.

**S-6 FOUR DRC-ONLY PIN TESTS — no conflict, wrong on the union** (`grep -n` at `drc-d1`):
- `test_drc_d3_experiments.py:49` `FORWARD[-1].name == "0020_drc_build_kinds.sql"`; `:79`–`:83` `FORWARD[-1]` / `[-2]`, `REVERSE[0]` / `[1]`, `_rollback_paths("0019") == ["0020_drc_build_kinds.rollback.sql"]`; `:84`, `:86` `.read_text()` of `FORWARD[-1]` / `REVERSE[0]`.
- `test_drc_d2_fix_r1_db.py:164`–`:165` `FORWARD[-2] == SQL and FORWARD[-3].name == …`, `REVERSE[1]` / `[2]`; `:180`–`:181` `_rollback_paths("0018")` = `0020`, `0019`.
- `test_drc_store.py:65`–`:67` `FORWARD[-5] == SQL`, `FORWARD[-4:-2]`, `REVERSE[4]`, `REVERSE[2:4]`; `:142`–`:143` `_rollback_paths("0011")` begins `0020`.
- `test_drc_k1_store.py:117` `REVERSE[2] == ROLLBACK`, `REVERSE[3:5]`; `:124`–`:125` `_rollback_paths("0016")` = `0020`, `0019`, `0018`.
- RULE: each `FORWARD` end-index one further out, each `REVERSE` index +1, each ASSERTED rollback list gains `0021_legs.rollback.sql` first. `test_legs_migration.py:29` (S3) stays true.

**THE TWO CONFIGS (K10)** — `grep -rn` under `drc-d1/src`:
- `prefill.yaml`: `prefill/config.py:29` `PREFILL_CONFIG_PATH`, `:157` the load; callers of `load_prefill_paths(`: `aset/web.py:1034` (C4: `:1041`), `drc/template.py:38` / `:70`, `daymode/drc.py:95`, `replay/line.py:211`, `smoke/checks.py:129`, `taxonomy/trade_note_migration.py:59`. `aset/web.py` is `com.cobalt.aset`'s module (`jobs.yaml` `imports: [cobalt.aset.__main__, cobalt.aset.web]`) → `reads:` of `com.cobalt.aset`. The schema refuses a resident-read path in `no_resident_reads` (`jobs/config.py:393`–`:397`).
- `templates/drc.md.j2` (D): two hits, both prose — `prefill/drc.py:6` (docstring, "deleted"), `daymode/drc.py:121` (comment). `no_resident_reads` needs ≥1 registered one-shot label (`jobs/config.py:371`, `:398`–`:402`); its reader `com.cobalt.prefill-drc` leaves the registry in this set. `41` names `com.cobalt.prefill-daily` (`prefill/daily.py:238`, the one `FileSystemLoader(TEMPLATES_DIR)`) and says so in `because:`.
- `restarts.py:201`–`:208` reads both lists; `:251`–`:252` is the UNCLASSIFIED CONFIG row they end.

## CHANGES
| # | `40` → `41` | source |
|---|---|---|
| 1 | Names: `deploy-0930`, `deploy/stacked-0930`, `deploy-2026-09-30`, `pre-stacked-0930`, `scratch-allow-probe-0930s`, report `deploy-2026-09-30.md`; `grep -n "0929"` on `41` prints nothing | `01` item 1 |
| 2 | `<c4 tip>` = `6785c7d5`; `<c4 check stop>` filled verbatim (`tail -n 2` of the check report; `defects that HOLD: 1`); P2 accepts row 5 by equality | `01` item 2; R1, R3 |
| 3 | STEP-T resolves conflicts by rules S-1 … S-5, quotes each hunk, concludes the merge with `add` + `commit --no-edit`; an unruled path or a same-statement rewrite → `merge --abort`, `FAILED: merge` | `01` (a) |
| 4 | New STEP-S: the two configs classified from `grep -rn` hits; S-6; ONE commit `seam(deploy-0930): DRC x S3 registry union, configs classified`; an offline early read of the 16 seam-facing test files | `01` (b), (c) |
| 5 | The gate runs on `<seam>`; a seam red → one fix commit inside the seam files, gate again; any other red → `FAILED: gate` | `01` (d) |
| 6 | THE WINDOW: first bootout before 09:15:00; merge clock 09:10:00; D0 line 09:00:00; no bootout / `kickstart -k` of a running resident 09:15–09:30; `40`'s 23:37 and archiver guards out; the nightly-snapshot wait out | `01` header, item 3; R4 |
| 7 | STEP-R: no UNCLASSIFIED row expected; the two rows read `resident reads` / `no resident reads` | `01` (d) |
| 8 | AUTHORIZATION: `cto-2026-09-30.md`; P-HIS = the row's time, `HIS RULING`, the literal; `40`'s three extra substrings dropped | `01` item 5 |
| 9 | Launch line: 58 allow (56 + 2 seam strings), 3 denies; Edit allowed only on the seam files in `deploy-0930` | `01` item 4 |
| 10 | Smoke (b): any `radar cycle:` line counts (pre-market session); 4.6 kickstarts the agent unconditionally (4.2 stops it) | R4 hour |
| 11 | Migration list per tip quoted at STEP-T: DRC `d583f6fd 9a0fc900 0075db31 5bb1f4b5 7cdc5774 8e8762ca d2897b46`; each S3 tip `eb642f05` | `git log --oneline main..<tip> -- src/cobalt/db_migrations`, 06:1x |
| 12 | RECORDS gains C4 E1; STEP-7 ESCALATE carries the seam for a later other-house read | R3, R4 |

## RULE STRINGS
`sed -n '6p'` of `50` vs line 6 of `41`, `grep -o '"[^"]*"'`, the `Read '…'` instruction removed, `sort`, `comm -3` (column 1 = `50` only, column 2 = `41` only):
```
"Bash(COBALT_ENV=production COBALT_VAULT_PATH=/Users/cobalt/Vault/Think uv run cobalt radar handicap-dry-run --day 2026-09-27)"
	"Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/deploy-0930/.env)"
"Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/stacked-0925/.env)"
"Bash(git -C /Users/cobalt/cobalt merge --ff-only deploy/stacked-0925)"
	"Bash(git -C /Users/cobalt/cobalt merge --ff-only deploy/stacked-0930)"
	"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 add *)"
	"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 commit *)"
	"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 merge --abort)"
	"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 merge --no-edit 04b3ca3e)"
	"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 merge --no-edit 6785c7d5)"
	"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 merge --no-edit 6983de75)"
	"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 merge --no-edit b8ac291b)"
	"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 merge --no-edit bbf25412)"
	"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 merge --no-edit main)"
"Bash(git -C /Users/cobalt/cobalt-wt/stacked-0925 merge --abort)"
"Bash(git -C /Users/cobalt/cobalt-wt/stacked-0925 merge --no-edit main)"
	"Bash(launchctl bootout gui/501/com.cobalt.prefill-drc)"
	"Bash(rm /Users/cobalt/cobalt-wt/deploy-0930/.env)"
"Bash(rm /Users/cobalt/cobalt-wt/stacked-0925/.env)"
	"Bash(rm /Users/cobalt/Library/LaunchAgents/com.cobalt.prefill-drc.plist)"
```
Common: 47 (44 allow + the 3 denies). `50`: 50 allow; `41`: 58 allow. `41` only: 14. 12 are `40`'s twelve re-pointed to `0930` with C4's tip filled (approved as one list: `cto-2026-09-30.md` R4, 06:09 ET).

## FOR DEJAN
Two strings beyond R4's list, both forced by the seam:
- `Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 add *)` — stages a resolved conflict and the seam files.
- `Bash(git -C /Users/cobalt/cobalt-wt/deploy-0930 commit *)` — concludes a resolved merge and makes the seam commit. Both act only in the gate worktree; `main` moves only by `merge --ff-only`.

## ESCALATE
1. `prefill.yaml` is a RESIDENT read, against `01`'s default: `aset/web.py:1034` calls `load_prefill_paths()` at the fill. `41` writes it under `com.cobalt.aset` `reads:`. The restart set does not widen (aset is already in it).
2. `drc.md.j2` has no reader left and the schema wants a one-shot label. ASK DESK [06:22]: is `readers: [com.cobalt.prefill-daily]` with the stated `because:` the classification you want? Safe default: as `41` writes it.
3. S-6: four DRC-only tests merge clean and fail on the union. `41` edits them in the seam commit. Other clean-merging tests that apply `_rollback_paths("0015")` and then assert state (`test_drc_d3_experiments.py:68`, `test_drc_d2_fix_r1_db.py:121`, `:226`) now also reverse `0021` first: UNPROVEN (L70) until the gate runs them; a red there is a seam red with one fix.
4. No conflict hunk was read (`merge-tree` off this seat's line). S-4 (`web.py`) rests on the commit lists, not on lines. `41`'s rule 6 stops the run on a same-statement rewrite.
5. THE 09:15–09:30 CLAUSE. `01` says a resident is never restarted inside it. `41` reads it as: no bootout and no `kickstart -k` of a running resident; a resident already DOWN is brought up at once; a smoke red inside the span ends FAILED with the new code live and no rollback. ASK DESK [06:22]: is that his meaning? Safe default: as written.
6. THE CLOCK. `41` adds a 09:00:00 line at STEP-D0 and a 09:10:00 merge clock. Gate cost on record: DRC's one with-DB pass 681.92 s (`drc-d3-fix-r2-build-2026-09-29.md` F8 (c)); C4 ran two passes. A launch after about 07:30 risks `FAILED: window`.
7. L67 floor: `41` and the seam have no other-house read; the gate is the seam's check (R4). Recorded for the desk's one-line override note (L73).
8. P-HIS: R4 (`cto-2026-09-30.md:12`) carries the literal. It names neither the five migrations nor the two seam strings.
9. K6: `41` was written in four calls of about 17, 18, 17 and 2 KB, over the 15 KB part size.
10. Carried from `40`'s draft, unchanged in `41`: ESCALATE 8 (schema rollback shape, `0016` below `0017`), 9 (`validate` vs the retired job), 10 (the named-cursor count in pass 2 is information).
11. `41` drops `40`'s STEP-T quote of the `jobs.yaml` diff against `<main base>`; STEP-S quotes the seam's own `jobs.yaml` diff instead.

## CONTINUE
next: the desk fills `<main base>`, `<launch row>` and the P-HIS row number in `41`, rules on the two strings (FOR DEJAN) and ESCALATE 2 / 5, runs the two placeholder counts, commits, then bare commands (0)–(2).

STACKED DEPLOY 0930 RE-ISSUED · set: 5 · migrations: 5 · seam files: 19 · strings vs 50: 14 · ESCALATE: 11
