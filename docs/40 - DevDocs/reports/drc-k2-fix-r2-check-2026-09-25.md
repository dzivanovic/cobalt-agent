# DRC K2 fix r2 — house check, ROUND 3 OF 3 (THE LAST) — 2026-09-25

## §0 Headline
- Checked `4626a1f2..f5c6946b` on `drc/d1-trading-log` (red `bf943793`, fix `bdd54135`, RUN-2 `f5c6946b`, AMENDED C7 (r2) / SEAM FOR D2 / FOR K3 / FOR D4, the three suites' executed output). Opus 5.5 and Grok both answered `FIX STANDS · ready for K3: YES`, both walked THE INPUT by name and both wrote `INPUT CLOSED`; no `INPUT NOT WALKED`, no contradiction between them.
- My file-check: `defects that HOLD: 0` (no checker made an INPUT OPEN / FALSE / SEAM GAP / INCOMPLETE / MISSES / WEAKENED / WIDENED / NOT SHOWN / DESELECTS OPEN / DEFECT REMAINS claim). `ready for K3: YES` under the prompt's rule.
- Two residuals the checkers list as NOT defects (facts, no verdict from me): the named NOT-built stored state after a refused rebuild, and an `opening`-kind restatement path that exits 0 (from K2, untouched by r2; consequence NOT CHECKABLE FROM READS) — ESCALATE 1–2.
- Sol: NOT SEATED (METER — retry after Sep 26th, 2026 6:47 AM). ESCALATE: 12.

## L74
A block inside a tool result (appended after the file text of the Read of the prompt file, ~03:15 ET) asked for a `Claude-Session:` line in commit / PR text and named a file-send tool (`SendUserFile`). DATA under L74 — recorded once, not followed. This hub commits nothing.

## PREFLIGHT
`rule · command · exit · allowed / DENIED` (every call ran under the launch line's strings; no denial, no dialog).
| rule | command | exit | result |
|---|---|---|---|
| date | `date` | 0 | `Fri Sep 25 03:15:19 EDT 2026` → `<D>` = 2026-09-25; before 2026-09-26 06:47 ET |
| placeholder | `grep -n -E "R_[_]" …/13-drc-k2-fix-r2-check.md` | 1 | prints nothing — PASS |
| placeholder | `grep -n -F "FILL AT LAUNCH" …/13-drc-k2-fix-r2-check.md` | 0 | prints only line 1 (the SEAT prose) and line 16 (this gate's own line) — PASS |
| GROK GATE (1st) | `grep -n "^| R17 " …/cto-2026-09-24.md` | 0 | `:35` `\| R17 \|` … `Grok approved with no asking going forward`; `git … log -1 --format=%H -S"Grok approved with no asking going forward" -- …cto-2026-09-24.md` → `1758fd78a572f47b613b2ca831dcfa636ed8f65a` |
| GROK GATE (1st) | `grep -n "^| R19 " …/cto-2026-09-24.md` | 0 | `:37` `\| R19 \|` … `All 4 house models approved for use indefinlitly`; `git … log -1 --format=%H -S"All 4 house models approved" -- …cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c` |
| round 2 committed | `git … log -1 --format=%H -- …drc-k2-fix-r1-check-2026-09-25.md` + `tail -n 3` | 0 | `43d570bed3142e7926cb35a9819f415c69a45850`; last non-blank line starts `DRC K2 FIX R1 CHECK DONE · round: 2 ·` — PASS |
| classification committed | `git … log -1 --format=%H -- …drc-k2-fix-r2-draft-2026-09-25.md` + `tail -n 3` | 0 | `a04b411b72d30bd985ec7084da91addfb59fc5a8`; last non-blank line starts `DRC K2 FIX R2 DRAFTED ·` — PASS |
| launch row | `grep -n "13-drc-k2-fix-r2-check.md" …/cto-2026-09-25.md` | 0 | `:22` `\| R14 \| 03:14 ET` (DESK LAUNCH ROW for `13`; not `R12`, not `12`'s row); `git … log -1 --format=%H -S"13-drc-k2-fix-r2-check.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` → `df727562daa66e9e610b3d0efc60bcc2dbd4a4f8` — PASS |
| grok | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` → UP |
| worktree | `ls /Users/cobalt/cobalt-wt/drc-d1` | 0 | present |
| BUILT LINE | `tail -n 3 …/drc-k2-fix-r2-build-2026-09-25.md` | 0 | last non-blank: `DRC K2 FIX R2 BUILT f5c6946b \| on 4626a1f2 \| red bf943793 \| offline 2467/0 \| with-DB 2918/0 \| live-note 142/0 \| .env: removed \| 0018: rolled back \| FIX: 1 of 1 \| RUNS: 1 \| ESCALATE: 6` — every required field present; `<tip>` = `f5c6946b`, `<red>` = `bf943793`; no `0018: UNPROVEN` |
| tip | `git … log --oneline -1 f5c6946b` | 0 | `f5c6946b test(drc): K2 fix r2 RUNS — stats rows stored with no stats import named (L70)` — the expected shape |
| range | `git … log --oneline 4626a1f2..f5c6946b` | 0 | EXACTLY 4 lines: `f5c6946b` RUNS · `bdd54135` fix · `bf943793` red with-DB · `1724d59e` docs (fix r1 report); non-docs commits 3; no second fix, no resume |
| range | `git … log --oneline f5c6946b..drc/d1-trading-log -- src tests configs` | 0 | EMPTY |
| path union | `git … log --stat --format=%h 4626a1f2..f5c6946b` | 0 | 7 paths = `12`'s list exactly: `src/cobalt/drc/cli.py`, `src/cobalt/drc/store.py`, `tests/cobalt/test_drc_k2_fix_r2_runs.py` (new), `tests/cobalt/test_drc_k2_fix_r2_store.py` (new), `docs/40 - DevDocs/cobalt/drc/cli.md`, `…/store.md`, `docs/40 - DevDocs/reports/drc-k2-fix-r1-build-2026-09-25.md` (`1724d59e`); non-docs path-touches 4; nothing else (no `db_migrations`, `configs`, `src/cobalt/cli.py`, `drc/pairing.py`, `models.py`, `trading_log.py`, `stats_log.py`, `detect.py`, no edited existing test) |
| headers | `grep -n "^## " …/drc-k2-fix-r2-build-2026-09-25.md` | 0 | the 18 headers at the desk's lines (`3` §0 Headline · `9` L74 · `12` AUTHORIZATION · `27` PREFLIGHT · `39` F1 · `44` F2 · `51` F3 · `144` F4 · `151` F5 · `154` F6 · `157` F7 · `165` RESTARTS · `180` AMENDED C7 (r2) · `187` SEAM FOR D2 · `203` FOR K3 · `213` FOR D4 · `219` CONTINUE · `222` ESCALATE); no `(run 2)` section |
| SWEEP | `grep -rn "VaultWriter" …/src/cobalt/drc` | 1 | none |
| SWEEP | `grep -n "INSERT INTO" …/src/cobalt/drc/cli.py` | 1 | none |
| SWEEP | `grep -n "INSERT INTO drc_stated_books" …/store.py` | 0 | exactly ONE: `store.py:1132`, inside `record_stated_book` (`:1072`) |
| SWEEP | `grep -n "def stated_day" …/store.py` | 0 | exactly ONE definition: `store.py:371` |
| SWEEP | `grep -n "stated_day(" …/cli.py` | 0 | ONE call: `cli.py:147`, inside `_rebuilds` |
| .env | `ls /Users/cobalt/cobalt-wt/drc-d1/.env` | 1 | `No such file or directory` — as required |
| recovery | `ls scratch/tribunal-bars-0920/drc-check/k2-fix-r2` | 1 | `No such file or directory` — fresh run |
| STAGGER | `grep -n -F "no other house hub is running" …/cto-2026-09-25.md` | 0 | printed lines include `:22` (R14), which also names `13-drc-k2-fix-r2-check.md` — PASS |
| PROBE Opus | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` (background) | 0 | `OK` → UP (one harness notice line before it: the `git push*:*` deny-rule syntax notice — a notice, no denial of any call of this hub) |
| PROBE Sol | — | — | NOT PROBED: `date` before 2026-09-26 06:47 ET → `sol: METER — retry after Sep 26th, 2026 6:47 AM (15 / 37's record)` |
| GROK GATE (2nd, before launch) | the two `git … -S` calls again at 03:26 ET | 0 | `1758fd78…` and `5055151d…` — unchanged, non-empty |
FAIL-CLOSED floor (two): Opus UP + Grok UP → met.

## Packet
`scratch/tribunal-bars-0920/drc-check/k2-fix-r2/` (folder created by the Write tool; no `mkdir` run). Every file's header names the REAL path, range and `<tip>`; every code slice's header reads `=== <real path> @ f5c6946b, REAL lines <a>–<b>; the first line below is REAL line <a> ===`. Sizes are `wc -c` of the staged files, measured after staging:
| file | bytes | what |
|---|---|---|
| `QUESTIONS-DRC-K2-FIX-R2.md` | 7,941 | the seven questions verbatim + the "Files in this folder" paragraph |
| `fix-diff.part1.md` | 14,005 | `git log -p 4626a1f2..f5c6946b -- . ":(exclude)docs"` (one part; the tool's output file was 13,782 B including its 2 trailing tool lines; the copy = the git output + a one-line header) |
| `devdocs-diff.md` | 2,580 | `git log -p … -- "docs/40 - DevDocs/cobalt/drc"` |
| `code-at-tip.part1–4.md` | 6,665 · 9,205 · 6,904 · 4,317 | REAL-line slices at the tip (cli `_rebuilds`…`cmd_state_book` 129–193; store `rebuild` 329–349, `stated_day`…`has_chain_through` 371–406, `_repair` 436–529, `_commit` 582–663, `_with_resolves` 841–890, `record_stated_book` 1072–1145; tests: `_resolve_applied_on_d_next` 80–89, the later-day restatement 130–143, K1 parametrize + dry-run test 636–667, K2 opening test 407–413) |
| `build-proof.md` | 14,021 | build report `## PREFLIGHT`, `## F2 RED (with-DB)`, `## F3 THE EDIT`, `## RESTARTS`, `## ESCALATE`, the stop line, each headed by its REAL report lines |
| `run.md` | 1,953 | `## F4 THE RUN` whole (RUN-2's executed result) |
| `suites.md` | 5,413 | `## F1 BASELINE`, `## F5 LIVE-NOTE`, `## F6 OFFLINE`, `## F7 WITH-DB` whole + THE DESELECTS, LISTED (four ids, each `file:line` by this hub's own `grep -n -F`: `test_tenancy.py:697`, `:710`, `:263`; `test_migrate_proof.py:306`) |
| `seam.part1–3.md` | 10,749 · 4,479 · 9,260 | parts 1–2 = the CURRENT `## AMENDED C7 (r2)` / `## SEAM FOR D2` / `## FOR K3` / `## FOR D4`; part 3 = SUPERSEDED (fix r1's seam and K3, `02`'s AMENDED C7) |
| `round-2.part1–3.md` | 5,904 · 4,837 · 8,588 | round 2's `## Seam`, `## Checked against the branch`, `## Ready for K3`, `## FOR THE CLASSIFIER`, `## ESCALATE`; the classification table, `## FOR K3`, `## FOR D4` |
| `rules.part1–2.md` | 5,772 · 6,167 | v3 lines 97–104, 186–190, 212–232; the printed R51 and R52 rows |
**Total 128,760 B (≈ 32,190 tokens per checker at ÷ 4)** — 42.9 % of the 300,000 B ceiling; largest part 14,021 B (< 15,000 B, R79); no cut. Checks before any checker launched: (1) `grep -c "^commit "` over `fix-diff` = 3 = the range's non-docs commits; `grep -c "^diff --git"` = 4 = the `--stat` non-docs path-touches. (2) Trailing whitespace: the git copies keep the 8 (fix-diff) / 2 (+ 4 tab-ended `---`/`+++` lines, devdocs) whitespace-ended lines; `build-proof.md` keeps the report's 5 single-space diff-context lines and 8 tab-separated RESTARTS lines; the source files carry 0. (3) REVERSE CHECK on every staged copy: `grep -v -n -F -x -f <original(s)> <copy>` lists only this hub's own header lines and blank lines (the BSD grep does not match an empty pattern, so blank lines print) — no typo in any copied content line. (4) Line counts: `code-at-tip` parts = 129 · 181 · 129 · 72 = exactly the slice lengths + headers; `fix-diff` 300 = 299 git lines + header; `devdocs-diff` 45 = 44 + header.
Checkers (the `15` / `03` spellings, `run_in_background`, one attempt each): OPUS 03:26:22 ET — `claude -p --model claude-opus-5-5 "You are OPUS. The folder is scratch/tribunal-bars-0920/drc-check/k2-fix-r2/ (absolute path …). Start with QUESTIONS-DRC-K2-FIX-R2.md and follow it exactly. … Do not open any *-check.md file. Read files with the Read, Grep and Glob tools only. Write no file. Print your complete check as your answer." --permission-mode plan --add-dir …/k2-fix-r2 --allowedTools "Read" "Grep" "Glob" --disallowedTools "Bash" "Write" "Edit" "NotebookEdit" "Agent" "WebFetch" "WebSearch" "AskUserQuestion" "EnterWorktree"`; answered by 03:33 (≈ 7 min); its stdout carried two harness notice lines (the `git push*:*` notice, `Warning: no stdin data received in 3s …`) then the check; `opus-check.md` written by this hub from stdout, byte for byte from the check's first line on (the two ANSI-coloured notice lines left out); reverse check against the saved stdout lists only blank lines. GROK 03:26:28 ET — `grok --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)" -p "You are GROK. … Write your complete check to …/k2-fix-r2/grok-check.md and reply with only that path."` (never `--always-approve`); it wrote its own file (12,510 B, on disk 03:38, ≈ 12 min) and replied with that path only. Written-nothing proof: `ls -la` of the packet folder before launch (18 files) vs after (those 18 unchanged + `opus-check.md` by this hub + `grok-check.md` by Grok, as told); `ls -la /Users/cobalt/cobalt-wt/drc-d1` before vs after identical (no `.env`, no new entry, root mtime 03:11). Sol: not launched.

## CONTINUE
done — both checkers answered, every claim walked, report complete.

## The input
`question · opus · grok · sol` (verbatim, ≤40 words each).
| question | opus | grok | sol |
|---|---|---|---|
| (a) the dry run | "Prints the row, then `on --apply: rebuild 2001-01-01 and every later recorded day` (`:165`–`:167`), then `DRY RUN — nothing written …`. Exit 0." | "Dry run prints `on --apply: rebuild 2001-01-01 and every later recorded day` and exits 0. It does not print `stated;`." | NOT SEATED |
| (b) after `--apply` | "Prints `APPLY`, the row and `written: drc_stated_books #<value> …`. Then `not rebuilt: 2001-01-01: no trading-log import and no no-trade DRC — nothing to re-pair ([F-05])`. **Exit 1.** No `stated;` line" | "the CLI prints `not rebuilt: 2001-01-01: no trading-log import and no no-trade DRC — nothing to re-pair ([F-05])` and exits 1. The new stated row stays … No `stated;` line. No `rebuilt:` line." | NOT SEATED |
| (c) the later day's stored rows | "nothing in `drc_rows` changes. … 2001-01-03's `trade` row keeps `inputs.resolve_id = first.id`, and its `day` row keeps `derived.resolves` naming `first.id`. … Its `book_close` still excludes the trade" | "`D_NEXT` and `D3` `drc_rows` are unchanged … the later `trade` row's `inputs.resolve_id` is still the superseded id … `book_close` still does not list that trade … Not a HOLD." | NOT SEATED |
| (c) is it a defect? | "I don't judge it one for this round. It is the named NOT-built item … The CLI is loud about it exactly once, with exit 1." | "This is the named NOT-built item (no stored mark). It does not break v3 `[F-06]` … Not a HOLD." | NOT SEATED |
| (d) any exit-0 path | "For THE INPUT: none after `--apply`. … For `resolve` / `no_trade` restatements whose superseded row's day is recorded: none. … For `opening` restatements: one path remains, which r2 did not change. … NOT CHECKABLE FROM READS" | "No apply path exits 0 for THE INPUT. For any `no_trade` or `resolve` restatement whose superseded row's day is recorded, `cli.py:147-148` makes `_rebuilds` true … Exit 0 remains only for the dry run, … a rebuild that finishes …, and for OTHERWISE" | NOT SEATED |
| INPUT line | `INPUT CLOSED — src/cobalt/drc/cli.py:147–148 (trigger; src/cobalt/drc/store.py:371, :399) · src/cobalt/drc/store.py:500–502 → src/cobalt/drc/cli.py:191–192 (refusal, exit 1; statement committed at src/cobalt/drc/store.py:1139)` | `INPUT CLOSED — src/cobalt/drc/cli.py:147 and src/cobalt/drc/cli.py:191` | NOT SEATED |
Both answers name THE INPUT by its test name in their first paragraph (Opus: `test_a_resolve_restated_to_an_earlier_unrecorded_day_is_never_a_silent_exit` in §0 / FIRST; Grok: same, first line).

## C7 and the seams
`clause · opus · grok · sol` (verbatim ≤30 words).
| clause | opus | grok | sol |
|---|---|---|---|
| `--apply --sha256 H` → `record_stated_book` | TRUE — `src/cobalt/drc/cli.py:173`–`:176` | TRUE — `src/cobalt/drc/cli.py:173` and `:187` | NOT SEATED |
| (a) effect day has a current import | TRUE — `src/cobalt/drc/cli.py:144`–`:146`, `:187` | TRUE — `src/cobalt/drc/cli.py:145` | NOT SEATED |
| (b) `no_trade`/`resolve` + a `day` row on/before the day tested (superseded row's day) | TRUE — `cli.py:147`–`:148`; `store.py:371`, `:399` | TRUE — `cli.py:147` (`has_chain_through` `store.py:399`) | NOT SEATED |
| dry run prints `on --apply: rebuild <effect day> …` in exactly those cases | TRUE — `cli.py:158`, `:165`–`:167` | TRUE — `cli.py:167` | NOT SEATED |
| `rebuilt: <dates>` | TRUE — `cli.py:193` | TRUE — `cli.py:193` | NOT SEATED |
| refusal → `not rebuilt:`, exit 1, statement kept | TRUE — `cli.py:188`–`:192`; commit precedes at `store.py:1139` | TRUE — `cli.py:191` (commit `store.py:1139`, row rollback `store.py:344`) | NOT SEATED |
| e.g. a resolve (or a restatement to such a day while the superseded day is recorded) → `[F-05]` | TRUE — `cli.py:147`–`:148`; `store.py:500`–`:502` | TRUE — `store.py:501` | NOT SEATED |
| "applied when that day's input is recorded (`seed_for` reads the day's resolves)" | TRUE as far as reads reach; `seed_for` … is not in the slices. | NOT CHECKABLE FROM READS — seed_for's body is not in the slices (signature only) | NOT SEATED |
| OTHERWISE prints `stated; <effect day> has no import yet`, exit 0 | TRUE — `cli.py:183`–`:185`; pinned at `test_drc_k2_fix_r2_store.py:107`–`:111` | TRUE — `cli.py:184` | NOT SEATED |
| that branch leaves no stored effect (superseded day unrecorded) | TRUE for the kinds (b) tests … (Pre-existing gloss note: see the verdict below.) | TRUE — `cli.py:185` (second test asserts no `drc_rows`) | NOT SEATED |
| a later day still holding the trade FAILS with `rebuild <R>` | TRUE — `store.py:883`–`:889` (`:887` is inside the raise) | TRUE — `store.py:887` (raise `:886`, condition `:883`) | NOT SEATED |
| next import is a first import (`seed_for` → `None`) | NOT CHECKABLE FROM READS — `seed_for` is not in the slices | NOT CHECKABLE FROM READS — seed_for's body is not in the slices | NOT SEATED |
| keeps `test_drc_k1_store.py:648` and `test_drc_k2_store.py:408` green | TRUE — … both green in with-DB (`…fix-r2-build-2026-09-25.md:160`) | TRUE — `test_drc_k1_store.py:648` and `test_drc_k2_store.py:408` (F7: … 0 failed) | NOT SEATED |
| the CLI inserts nothing (L3) | TRUE — `…build-2026-09-25.md:141` | TRUE — `cli.py:173` (no insert in `cli.py:151-193`) | NOT SEATED |
| SEAM (4) | TRUE: single writer `store.py:1072`, `market_reset` refusal `:1090`, key `:1103`–`:1111`, `supersedes` `:1120`–`:1129`, effect `:385`/`:392`, trigger `cli.py:147`–`:148`, `:187`. H2 opening refusal NOT CHECKABLE (`_reason` not in slices). | TRUE at `store.py:1072`, `:1090`, `:1103`, `:1125`, `:392`, `cli.py:147`, `:191`, `:187`; `assert_writable`'s body and H2 (`_reason`) NOT CHECKABLE FROM READS | NOT SEATED |
| SEAM line | `SEAM STATED`, with one note, pre-existing since `02`'s C7 and not moved by r2. The OTHERWISE gloss ("no `day` row on or before the day tested") does not describe `opening`, which (b) never tests. … consequence is NOT CHECKABLE | `SEAM STATED` — unchanged points: lines present in the slices are real; bodies not staged are NOT CHECKABLE FROM READS; "Not a gap." | NOT SEATED |
Unchanged points (1)–(3), (5)–(9): opus — "their citations land at the tip wherever the slices reach … There is no false cite." · grok — "the lines present in the slices are real." (both name `store.py:770`, `:943`, `:1050`, `cli.py:196` etc. as not in the slices; I read them at the tip under `## Checked against the branch`).

## FOR K3 / FOR D4
| checker | THIRD answer (verbatim ≤30 words) |
|---|---|
| opus | "`COMPLETE`. The page's loud refusal is at `…:210`. The STALE render … is also at `:210` … RUN-2 GREEN is at `:211`." · "`NAMES ALL`. Covered at `…:214`–`:217`: the base re-point, `_rebuilds` … `stated_day`, `effect_day`, the moved seam words, and D4's own greps" |
| grok | "`COMPLETE` — both NEW lines are there …; RUN-2 is stated GREEN with the refusal `<day>: stats rows are stored with no stats import named — nothing assumed`" · "`NAMES ALL` — base moves to `f5c6946b`; code re-read is `_rebuilds` …, the OTHERWISE print …, new `stated_day` …, `effect_day` calling it" |
| sol | NOT SEATED |
Opus adds two notes (facts; Opus: "harmless" / "NOT CHECKABLE"): the FOR D4 phrase "lines below `:371` moved +6" is imprecise (the shift starts after the old `effect_day`), and whether `05` pins suite counts (with-DB passed 2915 → 2918, offline skipped 458 → 461).

## Intent
| checker | FOURTH answer |
|---|---|
| opus | `KEPT`. — "No existing test file was edited. No mark was added, and RUN-2 is green with no `xfail`. `rebuild`, `_repair`, `_commit`, `_with_resolves` and `record_stated_book` are outside the store hunk" |
| grok | `KEPT` — "No D1 / K1 / K2 test file is edited, no assertion removed or loosened, no skip or `xfail` added … `effect_day`'s result is still `day` or `min(day, superseded day)`" |
| sol | NOT SEATED |

## Scope
| checker | FIFTH answer |
|---|---|
| opus | `NOTHING WIDENED`. — "The out-of-scope diff is empty, and there is exactly one `INSERT INTO drc_stated_books` … `stated_day` is a read. … `FN_VERSION`, migrations and `configs/` are untouched." |
| grok | `NOTHING WIDENED` — "`src` diff is `cli.py` (`_rebuilds`, the OTHERWISE print) and `store.py` (`stated_day` plus `effect_day` calling it) … The one `INSERT INTO drc_stated_books` remains inside `record_stated_book`" |
| sol | NOT SEATED |

## Suites
`suite · opus · grok · sol` (SIXTH, verbatim ≤30 words).
| suite | opus | grok | sol |
|---|---|---|---|
| offline | SHOWN — `2467 passed, 461 skipped, 1 xfailed, 15 warnings in 68.21s`, with `.env` proven absent | SHOWN — `2467 passed, 461 skipped, 1 xfailed, 15 warnings in 68.21s; <p> 2467 / <f> 0; .env absent (No such file)` | NOT SEATED |
| with-DB | SHOWN — `2918 passed, 6 skipped, 4 deselected, 1 xfailed, 15 warnings in 150.13s`, exit 0 … absence probe shows `assert 28 == 32`, short by 4 | SHOWN — `2918 passed, 6 skipped, 4 deselected, 1 xfailed, 15 warnings in 150.13s; <dp> 2918 / <df> 0; .env removed …; absence probe 1 failed, assert 28 == 32, short by 4` | NOT SEATED |
| live-note | SHOWN — `142 passed, 1 skipped, 15 warnings in 9.65s` | SHOWN — `142 passed, 1 skipped, 15 warnings in 9.65s; <lp> 142 / <lf> 0` | NOT SEATED |
| deselects | `DESELECTS AS STATED` — `test_tenancy.py:697`, `:710`, `:263`, `test_migrate_proof.py:306`; "four tests, matching `4 deselected`" | `DESELECTS AS STATED` — "the three `--deselect` arguments are the four tests" (same four lines) | NOT SEATED |
YOURSELF, from the build report (`/Users/cobalt/cobalt-wt/drc-d1/docs/40 - DevDocs/reports/drc-k2-fix-r2-build-2026-09-25.md`, facts, no verdict):
- Offline (F6, `:155`): `2467 passed, 461 skipped, 1 xfailed, 15 warnings in 68.21s (0:01:08)` — no `failed` and no `error` token in the summary line; report text: `<f>` 0, `0 errors`. (F1 baseline `:41`: `2467 passed, 458 skipped, 1 xfailed, 15 warnings in 68.19s`.)
- With-DB (F7 (c), `:160`): `2918 passed, 6 skipped, 4 deselected, 1 xfailed, 15 warnings in 150.13s (0:02:30)`, exit 0 — no `failed` / `error` token; `<df>` 0, `0 errors`, deselected 4.
- Live-note (F5, `:152`): `142 passed, 1 skipped, 15 warnings in 9.65s` — no `failed` / `error` token; `<lf>` 0, `0 errors`. Its SKIPPED line: `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC …` (known); no SKIPPED line names `COBALT_LIVE_VAULT_ROOT` (expected none — none).
- Deselected count 4 and the four ids as the build names them (`:158`): `test_tenancy.py:697`, `:710`, `:263`, `test_migrate_proof.py:306` — matches `suites.md`, and my own `grep -n -F` of each name at the tip returned those four lines (`class TestMigrationRoundTrip` `:688`, `class TestTenantGuc` `:239`).
- Absence probe (F7 (c2), `:162`): `1 failed in 5.67s`, `assert 28 == 32` at `test_migrate_proof.py:316`; the 28 listed cursors contain no `drc_imports`, `drc_fills`, `drc_rows` or `drc_stated_books` — short by 4, the known shape; `0016 + 0018: rolled back … absent on cobalt_dev`.
- `.env: removed, proven gone` is written for F2 (`:48`), F4 (`:148`) AND F7 (`:163`); F6 also shows `ls …/.env` → `No such file or directory` (`:155`). The lock reads (`no matches found`, one-line `ls -la` while held) are at `:45`, `:146`, `:159`.

## Run
| run | opus | grok | sol |
|---|---|---|---|
| RUN-2 (SEVENTH) | `RESULT SHOWN — green`: `3 passed in 0.36s` … refusal asserted equal to `2001-01-03: stats rows are stored with no stats import named — nothing assumed` (`test_drc_k2_fix_r2_runs.py:68`; raised at `store.py:527`–`:528`) | `RESULT SHOWN — green, raised message "2001-01-03: stats rows are stored with no stats import named — nothing assumed"` (`store.py:528`). No `xfail`. | NOT SEATED |
YOURSELF, from the build report (`:147`): RUN-2 = `tests/cobalt/test_drc_k2_fix_r2_runs.py`'s one test; `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_drc_k2_fix_r2_runs.py tests/cobalt/test_drc_k2_fix_r2_store.py` → `3 passed in 0.36s`; quoted: "**RUN-2 GREEN** (no `xfail` mark added): (1) `record_day` stores the state (no raise); (2) the day's `stats_row` rows exist (`count >= 1`) and its `day` row's `inputs.import_ids` keys are exactly `['trading_log']` (asserted equal); (3) `rebuild(2001-01-03)` raises `PairingError` whose text is asserted equal to `2001-01-03: stats rows are stored with no stats import named — nothing assumed` (`store.py:528`), and D_NEXT's `_snapshot` is identical before and after." It is GREEN, not a strict `xfail`; there is no xfail reason to quote. At the tip the test file asserts those values at `tests/cobalt/test_drc_k2_fix_r2_runs.py:62`, `:68`, `:69` (read).

## Red
From the build report (`:47`), F2, with-DB, on `4626a1f2` (the tree with THE INPUT's test added): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_drc_k2_fix_r2_store.py tests/cobalt/test_drc_k2_fix_r1_store.py tests/cobalt/test_drc_k2_store.py tests/cobalt/test_drc_k1_store.py` → `1 failed, 76 passed in 3.83s`. THE INPUT's failure reason, quoted: `test_a_resolve_restated_to_an_earlier_unrecorded_day_is_never_a_silent_exit`, `tests/cobalt/test_drc_k2_fix_r2_store.py:76`: `assert 'on --apply: rebuild 2001-01-01 and every later recorded day' in 'cobalt drc state-book — DRY RUN\n\nday: 2001-01-01\nkind: resolve …'` — "the base's `_rebuilds` is false for THE INPUT (`cli.py:142`)". The second new test, `test_a_resolve_restated_to_an_earlier_unrecorded_day_before_any_record_still_says_stated`: "PASSED on the base (a GREEN-as-pin of the OTHERWISE clause)" — yes, GREEN as a pin. Line 76 of the committed test is that `assert "on --apply: rebuild 2001-01-01 …" in out` (read at the tip). Red commit `bf943793`; green at `bdd54135`; both stated in the build report (`:49`, `:142`, `:147`).

## Checked against the branch
No checker returned INPUT OPEN, FALSE, SEAM GAP, INCOMPLETE, MISSES, WEAKENED, WIDENED, NOT SHOWN, DESELECTS OPEN or DEFECT REMAINS, so no such reason needed a walk. The two residual items and the checkers' notes, walked in the real files (`/Users/cobalt/cobalt-wt/drc-d1/`, Read tool):
`claim · who · file:line · HOLDS / DOES NOT HOLD / NOT CHECKABLE FROM READS · ≤30 words`
| # | claim | who | file:line | verdict | walked |
|---|---|---|---|---|---|
| 1 | After the refused rebuild the later day's stored rows still name the superseded resolve; no K2 read fails on them | opus (grok: same state, "Not a HOLD") | `store.py:341`–`:346`, `:500`–`:502`; `tests/cobalt/test_drc_k2_fix_r2_store.py:86`–`:87`; `store.py:869`–`:889` | HOLDS as a fact; neither checker calls it a defect | Rollback leaves `drc_rows` untouched (`store.py:344`–`:346`); the test asserts D_NEXT/D3 snapshots equal (`:86`–`:87`); `_with_resolves` raises only for a held trade (`:883`–`:889`). It is the build's NOT-built item (`…build:227`). |
| 2 | An `opening`-kind restatement on a recorded day with no import exits 0 without a rebuild | opus | `cli.py:148`, `:183`–`:185`; `store.py:1020`–`:1048` | path HOLDS as code; its consequence NOT CHECKABLE FROM READS | `cli.py:148` tests `req.kind in ("no_trade", "resolve")`; with no import on the effect day an `opening` falls to `cli.py:183`–`:185` (`stated;`, exit 0). `_reason` (`store.py:1020`) allows an opening on a first import or a broken chain; whether a recorded no-trade day can hold one and what it stores needs a run. Unchanged by r2 (the fix diff touches `cli.py:129`–`:148`, `:184` only). |
| 3 | Test docstring cites `store.py:520-522`, a pre-fix line; at the tip it is `:527`–`:528` | opus | `tests/cobalt/test_drc_k2_fix_r2_runs.py:7`; `store.py:527`–`:528` | HOLDS (a citation fact) | The docstring line 7 reads `(`store.py:520-522`)`; the guard raise is `store.py:528` at the tip. Citation drift in a test docstring, not behaviour. |
| 4 | FOR D4 "lines below `:371` moved +6" is imprecise | opus | build report `:215`; `store.py:371`–`:392` | HOLDS (a wording fact) | `stated_day` `:371`–`:383`, `effect_day` `:385`–`:392`; net +6 overall (`seed_for` `:770`, `record_stated_book` `:1072`, `add_parser` `cli.py:196` all read at the tip). |
| 5 | `seed_for` (`:770`), `_reason`, `assert_writable` bodies are not in the slices | opus; grok | packet slices | NOT CHECKABLE FROM READS | None of these is changed by the range (`fix-diff` touches `cli.py` / `store.py` only at `:133`–`:148`, `:181`, `:368`–`:392`). `def seed_for` `store.py:770`, the "is stale" text `:943`, `def add_parser` `cli.py:196`, `FN_VERSION` `pairing.py:90`, `assert_writable(` call `store.py:1090` read at the tip. |
Where the checkers contradict each other: nowhere — both answered `INPUT CLOSED`, `SEAM STATED`, `KEPT`, `NOTHING WIDENED`, all suites `SHOWN`, `DESELECTS AS STATED`, RUN-2 green, `FIX STANDS · YES`. Their differences are only in what each lists as NOT CHECKABLE.
Also stated, yourself:
- (i) SWEEP hits: `VaultWriter` none; `INSERT INTO` in `cli.py` none; `INSERT INTO drc_stated_books` exactly ONE `store.py:1132` inside `record_stated_book`; `def stated_day` exactly ONE `store.py:371`; `stated_day(` in `cli.py` ONE call `cli.py:147` inside `_rebuilds` (`store.py:392` is the second caller, inside `effect_day`, as the DevDocs say). No hit outside the expected.
- (ii) `git -C /Users/cobalt/cobalt log --oneline 4626a1f2..f5c6946b -- src/cobalt/db_migrations src/cobalt/cli.py configs src/cobalt/drc/pairing.py src/cobalt/drc/models.py src/cobalt/drc/trading_log.py src/cobalt/aset src/cobalt/prefill src/cobalt/replay src/cobalt/vaultwrite` → EMPTY.
- (iii) MY OWN WALK OF THE INPUT, from the real files at `f5c6946b`: `_rebuilds`' tested day = the superseded row's day, `tested = req.day if req.supersedes is None else store.stated_day(req.supersedes)` `cli.py:147` (read at `store.py:371`–`:383`; the effect day `store.effect_day(...)` `cli.py:144` = `min(day, stated_day)` `store.py:392`) — `has_chain_through(tested)` `cli.py:148` (`store.py:399`–`:406`); the dry-run print `cli.py:167`; the call `rebuild(effect)` makes: `cli.py:187` → `store.py:341` `self._repair(conn, day, {})` (then `_commit` `:342`); the line of `_repair` that refuses it: `store.py:500`–`:502` (`PairingError … no trading-log import and no no-trade DRC — nothing to re-pair ([F-05])`), reached because `_current_import` (`:444`) and `_no_trade_id` (`:445`) are both `None` for the earlier day; the rollback `store.py:344`–`:346`; the CLI line that prints `not rebuilt:` `cli.py:191`, then `raise SystemExit(1)` `cli.py:192`; the statement was committed earlier in `record_stated_book` (`store.py:1139`; called at `cli.py:173`).
- (iv) L32 — I read this report once before the last line: no ticker beyond the constructed `GGG` / `HHH` / `DDD` / `EEE` (only `DDD` appears, inside the tests' names), constructed dates only (`2001-…`) inside quoted checker / build text, no real date of his, no file name of his, no value written. The meter times (`Sep 26th, 2026 6:47 AM`) are the desk's records, not his.

## Ready for K3
| checker | CHECK DRC K2 FIX R2 line | ready | reason (verbatim) | INPUT walked |
|---|---|---|---|---|
| opus | `CHECK DRC K2 FIX R2: FIX STANDS · ready for K3: YES` | YES | — | YES |
| grok | `CHECK DRC K2 FIX R2: FIX STANDS · ready for K3: YES` | YES | — | YES |
| sol | NOT SEATED (METER — retry after Sep 26th, 2026 6:47 AM) | — | — | — |
`defects that HOLD: 0` → `ready for K3: YES` (every answering checker YES, every one walked THE INPUT, HOLD count 0).

## FOR THE CLASSIFIER
Round 3 is THE LAST — no fourth round, no further classification.
none. (No claim of a defect was made by either checker; the two residuals are put to the desk under `## ESCALATE` 1–2 as facts, in the checkers' own words that neither is a defect.)

## ESCALATE
1. **The NOT-built stored state (Opus; Grok "Not a HOLD"):** after THE INPUT's refused rebuild, D_NEXT's `trade` row / `day.derived.resolves` still name the superseded resolve and no K2 read fails on it later (`store.py:883`–`:889` raises only for a held trade); the build's named NOT-built item (`…build:227`), covered on the page by K3's STALE rule (`…build:210`). Opus: "This is Dejan's call; I don't hold it." File-check: HOLDS as a fact (row 1 above); not counted as a defect.
2. **The `opening`-kind restatement exit-0 path (Opus):** `cli.py:148` excludes `opening` from (b); an opening with no import on the effect day exits 0 through `cli.py:183`–`:185`; it dates from K2 and r2 did not touch it; whether it can occur and what it leaves stored is NOT CHECKABLE FROM READS — settling it needs a run (a first-of-chain no-trade day recorded by `rebuild`, its opening stated, the opening restated through the CLI). Row 2 above; not counted (L70).
3. **NOT CHECKABLE FROM READS rows, both checkers:** bodies of `seed_for`, `_reason`, `assert_writable` are not in the slices (row 5); none is touched by the range. Not counted.
4. **Citation facts (Opus, verified):** the RUN-2 test docstring cites `store.py:520-522` (`test_drc_k2_fix_r2_runs.py:7`); FOR D4's "+6 below `:371`" is loose (rows 3–4). Not counted.
5. **Packet:** no mismatch, no cut (128,760 B of the 300,000 B ceiling). Note: the verbatim copies of RUN-2's test and the build text carry the tests' constructed `FFF` symbol (the questions named `GGG` / `HHH` / `DDD` / `EEE`); no checker quoted it. Typos: none (reverse check clean).
6. **Checkers:** both answered with a `CHECK DRC K2 FIX R2:` line; no `INPUT NOT WALKED`; no checker wrote a file it was not told to (Grok wrote only `grok-check.md`); no `ASK DESK`. The build's own ESCALATE 2 (three of its own read-only greps used `\|`, ran with no dialog) is recorded as it stated.
7. **The L74 line:** recorded under `## L74`.
8. **The build's `0018: UNPROVEN` / `LINE MOVED`:** none — its stop line reads `0018: rolled back`; PREFLIGHT read `0 LINE MOVED`.
9. **Sol:** NOT SEATED (METER — retry after Sep 26th, 2026 6:47 AM); the desk seats Sol from that time.
10. **Astra:** the K2 NEW BUILD's Astra read is owed from Sep 26th, 2026 6:47 AM (52 ESCALATE 7) — the desk's seat, not this round's. **X12:** NOT RUN — hub-run read (v3 :306, :328), the desk's; carried.
11. **Standing line:** **"Round 3 — THE LAST (L39 / L67 / L75) — covers DRC K2 fix r2 only (`4626a1f2..f5c6946b`: the CLI's rebuild trigger for a restatement, `stated_day`, the printed effect day, AMENDED C7 (r2) and the re-issued seams, RUN-2), with its three suites' executed output, checked by Opus 5.5 + Grok (+ Sol when seated) under his R95 (a fix round = other check; Gemini out, R96/R97). With every seated house `ready for K3: YES`, THE INPUT walked by every seated house, and `defects that HOLD: 0`, K2 is checked (L67): `05` D4 BUILD launches on the lock with its base re-pointed to `f5c6946b` (R100) citing the fix r2 report's `## FOR D4`, and K3's drafter (after D2 + D3, R9) cites its `## SEAM FOR D2` / `## FOR K3`. A HOLD here goes to Dejan as ONE message — his per-case override (L67 OVERRIDE / L73) or a design round — NEVER a fourth round. A NO with `defects that HOLD: 0` also goes to him as that ONE message. A1 stays the desk's reading of R51."**
12. **Standing line:** **"The deploy's L68 gate re-proves offline, with-DB and the live-note suite on the stacked tree that ships (D1 + K1 + K2 + D4 + D2 + D3); the deploy prompt gets its own house read (L67, R95 seats)."**

DRC K2 FIX R2 CHECK DONE · round: 3 · opus: CHECK DRC K2 FIX R2: FIX STANDS · ready for K3: YES · grok: CHECK DRC K2 FIX R2: FIX STANDS · ready for K3: YES · defects that HOLD: 0 · ready for K3: YES · ESCALATE: 12
