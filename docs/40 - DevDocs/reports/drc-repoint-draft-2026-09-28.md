# DRC re-point draft — 2026-09-28 (drc-repoint-draft-0928)

## §0
- Re-pointed `08`–`11` in place to the checked merge from `42`'s `## FOR 08`: tip `e64b1dac`, code `7cdc5774`.
- Pins carried: 12 of 12 (every `file:line` of the source, one `grep -n -F` each, hit printed).
- Model ids: `09`, `11` → `claude-sonnet-5-5`; launch lines otherwise byte-identical; new rule strings: 0.
- ESCALATE: 6 (rollback-proof runner, probe numbers, D3 `0020` renumber, git-proved anchors, `.clinerules` caveat, tools used).
- Launched nothing; committed nothing; wrote the four files and this report.

## FACTS
Authorization (18:22 ET, `date`): `git -C /Users/cobalt/cobalt log --oneline -3 -- "docs/40 - DevDocs/reports/cto-2026-09-28.md"` → `c59eb3cc`, `89502f8e`, `c023f8f9`; `grep -n -F "| R128 |"` on that file → row 137 names `48-draft-drc-repoint.md`. R124 → row 133 (`grep -n "^| R124 "`).
- Tip: `git -C /Users/cobalt/cobalt log --oneline -3 drc/d1-trading-log` → `e64b1dac` (r4 report) · `84827649` (r3 report) · `509f19f5` (r2 report). The desk read `e64b1dac` at 18:21; same at 18:23.
- Code: `git -C /Users/cobalt/cobalt log --oneline 7cdc5774..drc/d1-trading-log -- src tests configs` → empty (0 lines). The three commits above `7cdc5774` touch only the merge-fix reports (`log --stat`).
- `7cdc5774` = `fix(drc-merge): fix r2 — 0018 rollback a no-op on absent drc_rows; 0015 registry pin re-stated`, parent `0e75e46d`, over `4fc270c7` (fix r1).
- Merge: `git -C /Users/cobalt/cobalt log -1 --format='%h %p %s' 5bb1f4b5` → parents `10163d51` `daf36e01`.
- Main tip: `git -C /Users/cobalt/cobalt log --oneline -3 main` → `0c25848a` (was `68862854` at r4 launch; 18 commits since, `68862854..main -- src tests configs` = 0 lines).
- Main since the merge: `git -C /Users/cobalt/cobalt log --oneline daf36e01..main -- src tests configs ops pyproject.toml` → 0 lines (docs-only).
- Ahead: `git -C /Users/cobalt/cobalt log --oneline main..drc/d1-trading-log` → 73 lines. Behind: `git -C /Users/cobalt/cobalt log --oneline drc/d1-trading-log..main` → 89 lines. The source's 72 / 71 were read at `84827649` against `68862854`.
- Migrations (source, `__init__.py:106–145`): `0018` last; `FORWARD` `0018` at `:124`, `REVERSE` `:129` (`grep -n "0018_drc_stated_books"` on the worktree → `:62`, `:66`, `:72`, `:124`, `:129`). `0019` = `08`'s `drc_events`, `0020` = D3, `0021` = S3 exits C1 (off main).
- Counts (source): `<p>` 3547 offline · `<d>` 4066 with-DB (4057 + 9) · `<l>` 146 live-note · `<F0>` = `<F2>` = `<F3>` = 664 · 35 · `272c95bbb12241e3611e4b36326ccf87` · `<F1>` (at `0018`) = 796 · 40 · `5727e9dfb418376cc48722a3601ca7c3`.
- With-DB deselect set (source; `reports/drc-merge-fix-r2-build-2026-09-28.md:211`): eight arguments, nine tests. Lines, each proved by `grep -n -F "def <name>"` on the worktree: `test_tenancy.py` `:701`, `:714`, `:263` · `test_migrate_proof.py` `:306` · `test_voice_store.py` `:215`, `:232`, `:257` · `test_voice_confirm.py` `:218` · `test_voice_lifecycle.py` `:137`.
- Anchors (source, `7cdc5774`), each proved by `git -C /Users/cobalt/cobalt show 7cdc5774:<path>` + `grep -n -F`: `placement.py:100` · `aset/web.py:1152` (`/attest`), `:1557` (`/drc`), `:1512` (`radar_card_release`) · `cli.py:512` · `replay/line.py:60` · `taxonomy/vault_loader.py:91`.
- RESTARTS (source, `10163d51..84827649`): `com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar`; widened to every resident by the UNCLASSIFIED `.clinerules` row; OWED to the DRC deploy (R74).
- DRC files unchanged by the merge: `git -C /Users/cobalt/cobalt log --oneline 6777c463..7cdc5774 -- src/cobalt/drc src/cobalt/aset/drc_page.py` → empty; every `drc/*.py` line cite in the four files holds.

## CHANGES
Line numbers are the new files'. Bytes: `08` 81773 → 90087 (pin list +13 lines, contract, F8 set) · `09` 56714 → 58547 · `10` 66561 → 69846 · `11` 47589 → 48890. `R__` count: 1 per file, in the AUTHORIZATION block (`08:54`, `09:23`, `10:65`, `11:17`).

| file · line | what | why |
|---|---|---|
| 08 · 1 | header `RE-POINTED …` after `MODEL:`; `git diff 6777c463` → `7cdc5774`; probe `short by FIVE` → `SIX` | item 8; 1 |
| 08 · 5 | BASE `7cdc5774`, tip `e64b1dac`, merge, 73 ahead / 89 behind, main `0c25848a` | item 1 |
| 08 · 19 | rollback contract + proof shape added to the `0019` rollback bullet | item 3 |
| 08 · 28, 129–131 | `git diff` / `--stat` bases `6777c463` → `7cdc5774`; merge-fix reports named in the range | item 1 |
| 08 · 44 | `web.py` range end `:1606` → `:1610` (file length at `7cdc5774`) | item 1 |
| 08 · 53 | R124 authorization bullet | item 6 |
| 08 · 73 | F0 tip rows: `e64b1dac` / `84827649`; `git diff --stat 7cdc5774 e64b1dac`; `<base>` = `7cdc5774` | item 1 |
| 08 · 79 | `placement.py` `(95, 97)` → `(98, 100)`; the `-rln` name-grep → `ls` of the eleven pin files | items 1, 2 |
| 08 · 80 | `restarts 7cdc5774..HEAD`, docs-only expectation names the three reports | item 1 |
| 08 · 83–85 | F1 baseline `e64b1dac`; `2588` → `3547`; `142` → `146`; with-DB baseline `4066` | item 1 |
| 08 · 107–120 | THE REGISTRY PINS = the source's complete list (12 pin lines, two WITH-DB, NOT PINS) | item 2 |
| 08 · 156 | F8 `<DS>` = eight arguments, nine tests, by name with lines | item 1 |
| 08 · 158–159 | deselect count 9; `<dp>` = 4066 + new; probe `28 == 34`, short by 6 (`voice_turns` added) | items 1; ESCALATE 2 |
| 08 · 162 | RESTARTS caveat carried | item 5 |
| 08 · 197 | stop line `on 7cdc5774` | item 1 |
| 09 · 1 | tag `Sonnet 5.5 (claude-sonnet-5-5)`; header; launch `--model claude-sonnet-5-5`; LAW STEP gains merge + fix r1–r4 + `43`; base `7cdc5774`; range `7cdc5774..<tip>` | items 4, 8, 1 |
| 09 · 3, 13, 125 | title, `short by SIX`, standing line: base `7cdc5774` | item 1 |
| 09 · 22 | R124 authorization bullet | item 6 |
| 09 · 58, 60–61 | `\| on 7cdc5774`; range shape with the three merge-fix report commits; stat path union: pin files per the source, the three reports replace the D2 report | items 1, 2 |
| 09 · 75–76, 79, 118 | `log -p` / `git diff` / `log --oneline` bases `7cdc5774` | item 1 |
| 09 · 81, 100, 115 | nine deselect ids, eight arguments; probe `SIX` incl. `voice_turns` | items 1; ESCALATE 2 |
| 10 · 1 | header; `## FOR 09` sentence: `0019` → `0020` and the probe re-pointed here, SETTLED token and seam symbols stay the desk's; L76 list gains `0019`, `0020` | items 8, 1 |
| 10 · 15, 29 | `writer.py:673` / `cli.py:196` at `7cdc5774`; `src/cobalt/cli.py:511` → `:512` | item 1 |
| 10 · 37, 44, 51, 102, 127, 130 | D3 migration `0019` → `0020` (kinds, D3-M row, L76, X-K test name and reversal, diff quote, commit message) | item 1 |
| 10 · 40–44, 51, 57, 89 | anchors: `runner.py` `:443` → `:483`; `pyproject.toml` `:67` → `:68`; `jobs.yaml` `:181-186` → `:199-204`, `:310` → `:328`; `s2.yaml` `:436-438` → `:545-547`, `:383-398` → `:492-507`; `line.py` `:59` → `:60`; `placement.py` `:95` → `:98`; `__init__.py` `:100`, `:105` → `:124`, `:129`; preflight greps to match | item 1; ESCALATE 4 |
| 10 · 44 | rollback contract for `0020` (guard on `drc_rows`, proof shape) | item 3 |
| 10 · 65 | R124 authorization bullet | item 6 |
| 10 · 142, 144–145 | E7 `<DS>` eight arguments, nine tests, count 9; probe `28 == 34`, short by 6; record and `UNPROVEN` names `0020` | items 1; ESCALATE 2 |
| 10 · 150 | RESTARTS caveat carried | item 5 |
| 10 · 155, 160, 163 | K3 next free after `0020`; deploy items `0019` and `0020`; stop line `migration 0020`, `0020: rolled back`, `0020: UNPROVEN` | item 1 |
| 11 · 1 | tag `Sonnet 5.5 (claude-sonnet-5-5)`; header; launch `--model claude-sonnet-5-5`; `0019` → `0020` | items 4, 8 |
| 11 · 3, 7, 50, 55, 58, 76, 128, 135–136 | D3 migration `0019` → `0020`; `0020: UNPROVEN` | item 1 |
| 11 · 16 | R124 authorization bullet | item 6 |
| 11 · 79, 109, 122 | nine deselect ids, eight arguments; probe `28 == 34`, short by 6 | items 1; ESCALATE 2 |

Carried, not stale: `08:165–167` cite `6777c463` for the D2 build report's own lines; `09:82` labels the superseded D2 report `6777c463`; `08:5` and `09:1` name `10163d51` as the merge parent and D2 report commit.

## PIN PROOF
Each: `grep -n -F "<token>" 08-drc-d2-fix-r1-build.md`; a hit line printed (exit 0; the exit code itself was not printed).
1. `tests/cobalt/test_assumed_store.py:245–256` → `08:108`
2. `tests/cobalt/test_drc_k1_store.py:116` → `08:109`
3. `tests/cobalt/test_drc_store.py:65–66` → `08:110`
4. `tests/cobalt/test_voice_store.py:57` → `08:111`
5. `tests/cobalt/test_radar_handicap_store.py:84–87` → `08:112`
6. `tests/cobalt/test_stale_score_db.py:159–162` → `08:113`
7. `tests/cobalt/test_p4_migrations.py:101–112` → `08:114`
8. `tests/cobalt/test_radar_migration.py:33–45` → `08:115`
9. `tests/cobalt/test_radar_score_migration.py:103–114` → `08:116`
10. `tests/cobalt/test_tenancy.py:513–526` → `08:117`
11. `tests/cobalt/test_archiver_migrations.py:84–95` → `08:118`
12. `tests/cobalt/test_archiver_migrations.py:54` → `08:119`

Pins carried: 12 of 12.

## RULE PROOF
Method: launch line = the text from `claude --bg` to the closing `--add-dir /Users/cobalt/cobalt-wt` of line 1; morning version = `git -C /Users/cobalt/cobalt show HEAD:<path>`; compared token by token (77 tokens each).

| file | result |
|---|---|
| 08 | identical |
| 09 | one differing token: `claude-sonnet-5` → `claude-sonnet-5-5` |
| 10 | identical |
| 11 | one differing token: `claude-sonnet-5` → `claude-sonnet-5-5` |

The `MODEL:` tag of `09` and `11` moved with it (`Sonnet 5 (claude-sonnet-5)` → `Sonnet 5.5 (claude-sonnet-5-5)`); `08` and `10` stay `claude-opus-5-5`.

NEW strings: none.

## ESCALATE
1. ASK DESK: who runs the repeated `--down-to 0013` proof (`F3 = F2 = F0`) for `0019`, and for `0020` in `10`? `08` and `10` carry no `cobalt db` string and take no new one. Reading A: the builder proves the contract through pytest only (S-1 test 12). Reading B: the desk runs the proof at the L68 gate. Default: both prompts state the source's contract and proof shape; the runner is left to the desk. [18:34 ET]
2. ASK DESK: the source states no absence-probe number for the merged tree. `08` (c2), `10` E7 (c2), `11` carry `assert 28 == 34`, short by 6 — derived: 33 tables probed at `0018` (`reports/drc-merge-fix-r2-build-2026-09-28.md:83`; the test asserts `len(recorder.cursor_names) == len(PROOF_TABLES)`, `test_migrate_proof.py:316`) plus `0019`'s `drc_events`; `10` adds no table. Reading B: carry the pre-merge shape (`28 == 33` short by 5 in `08`, `28 == 32` short by 4 in `10`) — stale by `voice_turns`. Default: derived, named as derived in the prompts. [18:34 ET]
3. ASK DESK: `10` and `11` renumbered D3's migration `0019` → `0020`, from the source's migration list. The seam document's `## FOR 09` leaves that renumbering to the desk at launch. Reading B: leave it for launch. Not touched: the SETTLED token, the seam symbols, `10:37`'s first-check text. Default: renumbered. [18:34 ET]
4. ASK DESK: anchors beyond the source's ANCHORS list were re-pointed on git proof (CHANGES `10 · 40–44 …`; `08 · 44`, `08 · 79`; test lines of the deselect ids). Reading B: only the source's anchors move; the rest surface as `LINE MOVED` at preflight. Default: git-proved anchors re-pointed, each cited above. [18:34 ET]
5. Carried, never resolved: the RESTARTS line widened by the UNCLASSIFIED `.clinerules` row, OWED to the DRC deploy (R74) — in `08` and `10` `## RESTARTS`.
6. Tools: read-only `python3` (regex and `difflib` over the four files and `git show HEAD:`), `sed -n`, `awk`, `for` loops and one job-tmp write (`$CLAUDE_JOB_DIR/tmp/pintokens.json`) went beyond the seven precedented strings. No repo write except the Edit / Write tools on the four files and this report.

## CONTINUE
None. The desk verifies the four files (L35) and launches `08`.

DRC CHAIN REPOINTED · files: 4 · tip: e64b1dac · code: 7cdc5774 · pins carried: 12 of 12 · new rule strings: 0 · ESCALATE: 6
