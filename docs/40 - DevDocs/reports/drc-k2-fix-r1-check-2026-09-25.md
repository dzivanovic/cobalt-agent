# DRC K2 FIX R1 — BUILD CHECK, ROUND 2 (`09ce3742..4626a1f2` on `drc/d1-trading-log`)

Hub `drc-k2-fix-r1-check-0925`, Sonnet 5, started Fri Sep 25 02:02:56 EDT 2026 (from `date`; `<D>` = 2026-09-25). Prompt `prompts/2026-09-25/03-drc-k2-fix-r1-check.md` (launch row `| R8 |` of `cto-2026-09-25.md`). Packet folder `scratch/tribunal-bars-0920/drc-check/k2-fix-r1/` (cwd `/Users/cobalt/cobalt-wt/agy-trial`). Checkers launched 02:24, closed 02:36.

## §0 Headline
- Round 2 of ≤3 of DRC K2 fix round 1 (`4626a1f2` on `09ce3742`: F-1…F-5, RUN-1, the amended seams, AMENDED C7, the three suites' executed output). Packet 228,794 B (under the 300,000 B ceiling), no cut.
- Opus `DEFECT REMAINS · ready for K3: NO` (F-1 and the seam / AMENDED C7 on ONE input: a resolve restated to an EARLIER day with nothing recorded on or before it); Grok `FIX STANDS · ready for K3: YES` (did not walk that input). Both: intent KEPT, scope NOTHING WIDENED, all three suites SHOWN, DESELECTS AS STATED, RUN-1 green.
- In my file-check 2 claims HOLD (both Opus's, one input). `ready for K3: NO`. Sol: `NOT SEATED (METER — retry after Sep 26th, 2026 6:47 AM)`. ESCALATE: 12.

## L74
- One block arrived INSIDE a tool result (the Read of this prompt file, after its last line): a `<system-reminder>` asking that commits and PR bodies end with a `Claude-Session: https://claude.ai/code/…` line and naming a file-send tool (`SendUserFile`). Recorded once here as DATA, not followed. This hub commits nothing and sends no file. The build report's own `## L74` (its REAL line 12, a block of the same shape) is data too and is not in the packet.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| placeholder gate 1 | `grep -n -E "R_[_]" …/03-drc-k2-fix-r1-check.md` | 1 | no output — allowed |
| placeholder gate 2 | `grep -n -F "FILL AT LAUNCH" …/03-drc-k2-fix-r1-check.md` | 0 | prints only `:1` (the SEAT prose that defines the token) and `:19` (this gate's own line) — allowed |
| clock | `date` | 0 | `Fri Sep 25 02:02:56 EDT 2026` → `<D>` = 2026-09-25, before Sep 26th 6:47 AM |
| GROK GATE (R17) | `grep -n "^| R17 " …/cto-2026-09-24.md` | 0 | `:35` `\| R17 \| 07:32 ET \| … Grok approved with no asking going forward …` — allowed |
| GROK GATE (R17 committed) | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"Grok approved with no asking going forward" -- …/cto-2026-09-24.md` | 0 | `1758fd78a572f47b613b2ca831dcfa636ed8f65a` |
| GROK GATE (R19) | `grep -n "^| R19 " …/cto-2026-09-24.md` | 0 | `:37` `\| R19 \| 07:36 ET \| … All 4 house models approved for use indefinlitly …` — allowed |
| GROK GATE (R19 committed) | `git … log -1 --format=%H -S"All 4 house models approved" -- …/cto-2026-09-24.md` | 0 | `5055151dbf68899b82de5b11f99733ed2d03048c` |
| GROK GATE, second row (before launch) | the four rows above re-run at 02:24:15 | 0 | same rows (`:35`, `:37`), same hashes |
| grok | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` → UP |
| worktree | `ls /Users/cobalt/cobalt-wt/drc-d1` | 0 | listed (`AGENTS.md`, `CLAUDE.md`, `configs`, `docs`, `src`, `tests`, `uv.lock` …) |
| round 1 committed | `git … log -1 --format=%H -- …/drc-k2-check-2026-09-24.md`; `tail -n 3` | 0 | `eaa9c49b56a4f1dc8d5a18831680b45f5b33c011`; last non-blank line starts `DRC K2 CHECK DONE · round: 1 · …` |
| classification committed | `git … log -1 --format=%H -- …/drc-k2-fix-r1-draft-2026-09-25.md`; `tail -n 3` | 0 | `1f76d9d9c68494856d4db82769a2ccbef59615c7`; last non-blank line starts `DRC K2 FIX R1 DRAFTED · FIX: 8 · NOT REAL: 11 · UNPROVEN: 1 · OUT OF SCOPE: 6 · OWNER ITEM: 0 · prompts: 2 · new rule strings: 0 · ESCALATE: 3` |
| THIS launch | `grep -n "03-drc-k2-fix-r1-check.md" …/cto-2026-09-25.md` | 0 | `:14` R6 (`01`'s launch row, not counted), `:15` R7 (`02`'s launch row, not counted), `:16` `\| R8 \| 02:01 ET \| … DESK LAUNCH ROW for prompts/2026-09-25/03-drc-k2-fix-r1-check.md …` (counts), `:37`, `:41` |
| R8 committed | `git … log -1 --format=%H -S"03-drc-k2-fix-r1-check.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | 0 | `16699b37e393479cea19411e07ab8ea25cf4462f` |
| THE BUILT LINE | `tail -n 3 "/Users/cobalt/cobalt-wt/drc-d1/docs/40 - DevDocs/reports/drc-k2-fix-r1-build-2026-09-25.md"` | 0 | last non-blank line: `DRC K2 FIX R1 BUILT 4626a1f2 \| on 09ce3742 \| red d2abba17 \| offline 2467/0 \| with-DB 2915/0 \| live-note 142/0 \| .env: removed \| 0018: rolled back \| FIX: 5 \| RUNS: 1 \| ESCALATE: 9` — carries every required token. `<tip>` = `4626a1f2`, `<red>` = `d2abba17`. Not `0018: UNPROVEN` |
| tip subject | `git … log --oneline -1 4626a1f2` | 0 | `4626a1f2 test(drc): K2 fix r1 RUNS — a no-trade day with a stated opening beside a recorded prior (L70)` |
| range | `git … log --oneline 09ce3742..4626a1f2` | 0 | SIX, oldest last: `4626a1f2` RUNS · `d684f80b fix(drc): K2 fix r1 F-1 — the resolve-key query no longer shadows the validated positions in record_stated_book …` · `a51988c9 fix(drc): K2 fix r1 — resolve key across days, the stale mark …; drc.pairing/4` · `11e9af9a wip(k2-fix-r1): … red tests, with-DB …` · `d2abba17 wip(k2-fix-r1): … red tests, offline …` · `214c4b39 docs(k2): DRC K2 build report — 09ce3742`. Non-docs commits: FIVE (`grep -c "^commit "` over the staged diff parts = 5). `d684f80b` is the build's own F-1 correction (its ESCALATE 5), the second fix commit |
| nothing above the tip in code | `git … log --oneline 4626a1f2..drc/d1-trading-log -- src tests configs` | 0 | EMPTY |
| path union | `git … log --stat --format=%h 09ce3742..4626a1f2` | 0 | exactly `02`'s F4 list: `src/cobalt/drc/{cli,models,pairing,store,trading_log}.py` (5) · `tests/cobalt/test_drc_k2_fix_r1.py`, `test_drc_k2_fix_r1_store.py`, `test_drc_k2_fix_r1_runs.py` (3 new) · `test_drc_k2.py`, `test_drc_k2_store.py`, `test_drc_k2_experiments.py`, `test_drc_k1.py`, `test_drc_k1_store.py`, `test_drc_store.py` (6 edited) · `docs/40 - DevDocs/cobalt/drc/{cli,models,pairing,store,trading_log}.md` (5) · `docs/40 - DevDocs/reports/drc-k2-build-2026-09-24.md` (1, `214c4b39`'s) = 20 paths; no `db_migrations/`, `configs/`, `src/cobalt/cli.py`, `stats_log.py`, `detect.py`, `aset/`, `prefill/`, `replay/`, `vaultwrite/` |
| build report headers | `grep -n "^## " …/drc-k2-fix-r1-build-2026-09-25.md` | 0 | 17 headers, exactly as the prompt lists them (`§0 Headline` :5 … `ESCALATE` :197); no `(run 2)` section |
| L28 / L3 / L40 SWEEP | `grep -rn "VaultWriter" …/src/cobalt/drc` · `grep -n "INSERT INTO" …/drc/cli.py` · `grep -n "INSERT INTO drc_stated_books" …/drc/store.py` · `grep -n "kept_match" …/drc/store.py` | 1, 1, 0, 1 | none · none · exactly ONE, `store.py:1126` (inside `record_stated_book`, real lines 1066–1139) · none |
| `.env` | `ls /Users/cobalt/cobalt-wt/drc-d1/.env` | 1 | `No such file or directory` (never read) |
| recovery | `ls scratch/tribunal-bars-0920/drc-check/k2-fix-r1` | 1 | `No such file or directory` → fresh run (the Write tool created the folder; no `mkdir`) |
| STAGGER | `grep -n -F "no other house hub is running" …/cto-2026-09-25.md` | 0 | prints `:10` (R2, `67`'s row), `:12` (R4), `:16` (R8) — `:16` also names `03-drc-k2-fix-r1-check.md` — satisfied |
| PROBE Opus | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` (background) | 0 | `OK` → UP. The saved output carried one harness notice line before it (`Permission deny rule (../../cobalt/.claude/settings.local.json): Bash(git push*:*) mixes * with the trailing :* prefix syntax …`) — a notice, no denial of any call of this hub |
| PROBE Grok | its `--version` row | — | UP |
| PROBE Sol | keyed on `date` (2026-09-25, before 2026-09-26 06:47 ET) | — | `sol: METER — retry after Sep 26th, 2026 6:47 AM (15 / 37's record)` — not probed, not launched |
| FAIL CLOSED (checkers) | Opus UP and Grok UP | — | two UP → both launched |

## Packet
Staged in `scratch/tribunal-bars-0920/drc-check/k2-fix-r1/` (no `mkdir`; the Write tool created the folder). Every file is one Read → Write copy below a header naming the REAL path / range and `<tip>` `4626a1f2`; every code slice's header reads `=== <real path> @ 4626a1f2, REAL lines <a>–<b>; the first line below is REAL line <a> ===`. Sources: the saved `git log -p` outputs (read from the tool-result files) and `/Users/cobalt/cobalt-wt/drc-d1/` at `<tip>`. Each part < 15,000 B (R79).

| file | bytes | what |
|---|---|---|
| `fix-diff.part1.md` | 12,262 | saved-output lines 1–265: commits `4626a1f2`, `d684f80b`, then `a51988c9`'s `cli.py`, `models.py`, `pairing.py` diffs |
| `fix-diff.part2.md` | 14,349 | lines 266–558: `a51988c9`'s `store.py` diff |
| `fix-diff.part3.md` | 12,619 | lines 559–837: `a51988c9`'s `trading_log.py` diff and the edited tests |
| `fix-diff.part4.md` | 14,036 | lines 838–1161: `11e9af9a` (with-DB red tests) |
| `fix-diff.part5.md` | 4,047 | lines 1162–1251: `d2abba17` (offline red tests) |
| `devdocs-diff.md` | 5,030 | `git log -p 09ce3742..4626a1f2 -- "docs/40 - DevDocs/cobalt/drc"` lines 1–87 |
| `code-at-tip.part1.md` | 13,934 | `store.py` REAL lines 281–575 (`record_day` … `_no_trade_seed`; `effect_day` :371–386 is inside it) |
| `code-at-tip.part2.md` | 13,078 | `store.py` REAL 576–763 (`_commit`, `_rows`) and 1066–1139 (`record_stated_book` whole) |
| `code-at-tip.part3.md` | 12,898 | `store.py` REAL 764–964 (`seed_for` … `_carried`) and `cli.py` REAL 129–187 (`_rebuilds`, `cmd_state_book`) |
| `code-at-tip.part4.md` | 6,068 | `models.py` REAL 36–38, 235–240, 262–279; `trading_log.py` REAL 68–80, 176–194; `pairing.py` REAL 83–90, 483–519 |
| `build-proof.part1.md` | 11,768 | build report REAL 55–115: `## F2 RED (offline)`, `## F3 RED (with-DB)`, `## F4 THE EDITS` |
| `build-proof.part2.md` | 5,313 | build report REAL 144–171 (`## RESTARTS`) and 197–208 (`## ESCALATE`, the stop line) |
| `run.md` | 3,256 | build report REAL 116–126 (`## F5 THE RUN`, RUN-1) |
| `suites.md` | 5,643 | build report REAL 51–54 (`## F1 BASELINE`), 127–143 (`## F6 LIVE-NOTE`, `## F7 OFFLINE`, `## F8 WITH-DB`), and the four deselected ids with REAL `file:line` (this hub's own `grep -n`) |
| `seam.md` | 13,075 | fix build report REAL 172–193 (`## SEAM FOR D2`, `## FOR K3`), then the K2 build report's REAL 209–239 under `SUPERSEDED BY THE ABOVE (K2 build, 09ce3742)` |
| `round-1.part1.md` | 11,530 | round 1's report REAL 136–185 (`## Seam` with the pins table, `## Checked against the branch`) |
| `round-1.part2.md` | 8,882 | round 1's report REAL 191–221 (`## FOR THE CLASSIFIER`, `## ESCALATE`) |
| `round-1.part3.md` | 14,536 | the classification report REAL 14–58 (`## Classification` table, `## FOR K3`) |
| `rules.part1.md` | 6,443 | v3 REAL 97–104 and 124–143 |
| `rules.part2.md` | 11,817 | v3 REAL 165–190 |
| `rules.part3.md` | 6,015 | v3 REAL 212–232; the printed rows of R51 (`cto-2026-09-24.md:69`) and R52 (`:70`) |
| `rules.part4.md` | 14,313 | `51`'s `## THE K2 CONTRACT` REAL 81–113; then `02`'s `## AMENDED C7` REAL 16–17 under `C7 AS AMENDED BY K2 FIX R1 (replaces C7 above)` |
| `QUESTIONS-DRC-K2-FIX-R1.md` | 7,882 | the questions verbatim + the "Files in this folder:" paragraph |
| **total** | **228,794** | measured `wc -c` of the 23 staged files (`ls -l`), summed by hand; ÷ 4 = **≈ 57,199 tokens per checker**; under the 300,000 B ceiling (71,206 B margin); no `rules.md` cut was needed |

Written after the checks: `opus-check.md` 8,294 B (by this hub from stdout, byte for byte), `grok-check.md` 8,058 B (by Grok, told to).

Staging checks (each from a tool result):
- **Diff parts:** `grep -c "^commit "` over the five parts = 3 + 0 + 0 + 1 + 1 = **5** = PREFLIGHT's non-docs commit count; `grep -c "^diff --git"` = 5 + 1 + 7 + 1 + 2 = **16** = the non-docs path-touches `--stat` shows (1 + 1 + 11 + 1 + 2). The saved output was 55,610 B; its last two lines (a blank and the harness's `[exited with code 0]`, 22 B) are not git output and are not copied. The five parts total 57,313 B; the five headers are 301 + 297 + 325 + 374 + 428 = 1,725 B (`grep -b`); 57,313 − 1,725 = 55,588 = 55,610 − 22 (exact), part by part 11,961 · 14,052 · 12,294 · 13,662 · 3,619. The saved output has 49 lines ending in a space or tab (15 + 3 + 24 + 1 + 6): the copies hold the same lines (`grep -c -E "[[:space:]]$"` per part).
- **Reverse line check, every file:** `grep -n -F -x -v -f <source> <copy>` lists only the copy's own header lines and blank lines (the empty-line quirk of `-x`). It caught two typos in `fix-diff.part3.md` (fixed); the byte counts caught one extra `+` line in `fix-diff.part4.md` and a missing trailing blank line in `fix-diff.part3.md` and `seam.md` (all fixed before launch).
- **Code parts:** the sources have 0 lines ending in a space. `code-at-tip.part1`: 13,934 − 236 (header) = 13,698 = 24,683 − 10,985 (`grep -b` offsets of `_commit` and `record_day`); `part2`: 9,216 + 3,579 + two headers; `part3`: `store.py` slice 9,944 + `cli.py` slice 2,574; `part4`: 117 lines = 104 content + 7 headers + 6 blanks.
- **Report excerpts:** `build-proof.part1` 11,768 − 263 = 11,505 = 17,376 − 5,871; `part2` 1,514 + 3,362 (the report's `## RESTARTS` and `## ESCALATE` byte spans); `run.md` 2,959; `suites.md` 741 + 3,400; `seam.md` 6,733 + 5,538; `round-1.part1` 2,319 + 8,833; `part2` 2,688 + 5,769; `part3` 13,319 + 839.
- **`rules.part*`:** v3 slices 3,472 + 2,492 + 11,522 + 3,173 = the byte spans between the cut lines; R51's and R52's printed rows are the source rows + the `69:` / `70:` prefix (1,135 + 3 and 1,275 + 3); `51`'s contract 11,755 = 47,899 − 36,144.
- **`QUESTIONS-DRC-K2-FIX-R1.md`:** the reverse check against the prompt file lists only the appended paragraph, the opening line (the prompt's `QUESTIONS-DRC-K2-FIX-R1.md (verbatim): "` prefix) and the closing line (the prompt's closing quote mark).
- **Deselect ids** (`03` §1 (6)): `grep -rn` of each name in `/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/` → `test_tenancy.py:697`, `:710`, `:263`, `test_migrate_proof.py:306`; classes `TestTenantGuc` `:239`, `TestMigrationRoundTrip` `:688`. No line moved.

Launches (both `run_in_background`, independent, one attempt per house, told "Do not open any *-check.md file"; Opus first):
- OPUS at 02:24:25 (bg `b7qdft044`), `claude -p --model claude-opus-5-5 "You are OPUS. The folder is scratch/tribunal-bars-0920/drc-check/k2-fix-r1/ (absolute path /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/drc-check/k2-fix-r1/). Start with QUESTIONS-DRC-K2-FIX-R1.md and follow it exactly. Files named <name>.part<k>.md are one file read in order. Cite real paths and real lines only, as each file's header names them. Do not open any *-check.md file. Read files with the Read, Grep and Glob tools only. Write no file. Print your complete check as your answer." --permission-mode plan --add-dir /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/drc-check/k2-fix-r1 --allowedTools "Read" "Grep" "Glob" --disallowedTools "Bash" "Write" "Edit" "NotebookEdit" "Agent" "WebFetch" "WebSearch" "AskUserQuestion" "EnterWorktree"`. Answered by 02:27:48 (≈ 3 min). Its stdout carried two harness notice lines (the `git push*:*` notice and `Warning: no stdin data received in 3s …`) then the check. `opus-check.md` written by this hub from stdout, byte for byte (the reverse check lists only blank lines).
- GROK at 02:24:31 (bg `bf6khgzgy`), `grok --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)" -p "You are GROK. … Do not open any *-check.md file. Write your complete check to /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/drc-check/k2-fix-r1/grok-check.md and reply with only that path."` (never `--always-approve`). Its stdout was progress text and the path; its own file was on disk at 02:36 (`ls -la`). Recorded as Grok wrote it (8,058 B, ≈ 12 min).
- Clock: 45-minute deadline ≈ 03:09; both inside it; no HARNESS / METER / TIMEOUT.
- Written-nothing proof: `ls -la` of the packet folder (23 files) and of `/Users/cobalt/cobalt-wt/drc-d1` before the Opus launch (02:24:15), after it (02:24:25) and after the Grok launch (02:24:31) were identical. After both finished the packet folder holds exactly the 23 staged files + `opus-check.md` (this hub's) + `grok-check.md` (told to Grok), and `drc-d1` is unchanged (same entries and mtimes, folder mtime 01:59, no `.env`).

## CONTINUE
done — packet staged, both checkers answered, every claim walked; report closed below.

## Rows
`row · opus · grok · sol` (FIRST, ≤30 words each, verbatim).

| row | opus | grok | sol |
|---|---|---|---|
| F-1 | "**NOT CLOSED — `src/cobalt/drc/cli.py:142`** (with `src/cobalt/drc/store.py:386`). Details below the table." | "F-1 — CLOSED … `src/cobalt/drc/store.py:1097` keys a `resolve` by trade id on any day (`:1126` is the only `INSERT`)." | NOT SEATED |
| F-2 | "**CLOSED.** Each day in `not_repaired` goes into `stale` (`store.py:622-623`). One `UPDATE … derived \|\| book_stale … kind = 'day'` writes the mark (`store.py:651-656`)" | "F-2 — CLOSED … `src/cobalt/drc/store.py:623` sets one `{root, reason}`; `:651` writes it with `UPDATE … derived \|\|` onto each stopped day's own `day` row only." | NOT SEATED |
| F-3 | "**CLOSED.** There is one helper, `_no_trade_seed` (`store.py:552-574`). `record_day` calls it at `store.py:319` and `_repair` at `store.py:542`" | "F-3 — CLOSED … `_no_trade_seed` (`src/cobalt/drc/store.py:551`) is the only relabel. `record_day` calls it at `:319`; `_repair` calls it at `:542`." | NOT SEATED |
| F-4 | "**CLOSED.** `kept_match` is gone. The stats input is rebuilt with the stats import's own `missing_of` and always passed to `build_day` (`store.py:511-540`)." | "F-4 — CLOSED … `kept_match` and the `model_copy` are gone (`src/cobalt/drc/store.py:511-540` rebuilds the stats log from the stored rows and that import's own `missing_of`)." | NOT SEATED |
| F-5 | "**CLOSED.** One rule, `pairing_not_computed` (`trading_log.py:73-80`), called by the parser (`trading_log.py:181`) and by `_repair` (`store.py:487`)." | "F-5 — CLOSED … `pairing_not_computed` (`src/cobalt/drc/trading_log.py:73`) is the only decision. The parser calls it at `:181`; `_repair` calls it at `src/cobalt/drc/store.py:487`" | NOT SEATED |

## Intent
| checker | SECOND answer (≤30 words) |
|---|---|
| opus | "KEPT. The only assertion changes are the named ones: the four `drc.pairing/4` pins … the F-5 assertion … the two F-2 snapshots … each now `_without_stale(...) == before` plus an exact `book_stale` equality" |
| grok | "INTENT — KEPT. Assertion edits are only the named ones: the four `drc.pairing/4` pins …, the F-5 text …, the two F-2 snapshots replaced by `_without_stale` plus a `book_stale` assert …, and the one F-1 setup insert" |
| sol | NOT SEATED |

## Scope
| checker | THIRD answer (≤30 words) |
|---|---|
| opus | "NOTHING WIDENED. The fix touches the 5 src files, 3 new and 6 named test files, 5 DevDocs, and the K2 report … The diff over `db_migrations`, `configs`, `vaultwrite`, `aset`, `prefill` and `replay` is empty" |
| grok | "SCOPE — NOTHING WIDENED. `git diff 09ce3742` as named: `src/cobalt/drc/{cli,models,pairing,store,trading_log}.py`, the named tests, five DevDocs, and the K2 build report. Empty for `src/cobalt/db_migrations`, `configs` …" |
| sol | NOT SEATED |

## Seam
| checker | SIXTH answer (≤40 words) |
|---|---|
| opus | "SEAM GAP. Seam (4) and AMENDED C7 (its OTHERWISE clause): C7 says that with no import and nothing recorded on or before the effect day, \"no later `book_close` exists to hold the trade id\". That is wrong for a restatement whose superseded …" |
| grok | "SEAM STATED. Amended points match the tip. (1) stale prior `src/cobalt/drc/store.py:937`; writer guard `:1097`; reader raise still `:835`. (2) re-match `:511-540`. (3) `book_stale` dict `:623`, write loop `:651`. (4) resolve key `:1097` …" |
| sol | NOT SEATED |

## Suites
| suite | opus | grok | sol |
|---|---|---|---|
| offline | "SHOWN: `2467 passed, 458 skipped, 1 xfailed, 15 warnings`, 0 failed. The `.env` absence is proven." | "SHOWN — `2467 passed, 458 skipped, 1 xfailed, 15 warnings` (`<f>` = 0); `.env` absent before the run." | NOT SEATED |
| with-DB | "SHOWN: `2915 passed, 6 skipped, 4 deselected, 1 xfailed, 15 warnings`, 0 failed. The `.env` removal is proven. The 0016/0018 absence probe gives `assert 28 == 32`, short by exactly the 4 `drc_*` tables." | "SHOWN — `2915 passed, 6 skipped, 4 deselected, 1 xfailed, 15 warnings` (`<df>` = 0); `.env` removed and proven gone; absence probe `assert 28 == 32` …, short by 4" | NOT SEATED |
| live-note | "SHOWN: `142 passed, 1 skipped, 15 warnings`, 0 failed. The one skip is the known `COBALT_TEST_LIVE_DRC`." | "SHOWN — `142 passed, 1 skipped, 15 warnings` (`<lf>` = 0) … The `.env` removal and the `0016` / `0018` probe are the with-DB lock proof, not this leg." | NOT SEATED |
| deselects | "DESELECTS AS STATED: `test_tenancy.py:697` and `:710` …; `:263`; `test_migrate_proof.py:306`. The summary shows `4 deselected`." | "DESELECTS AS STATED. Three `--deselect` arguments, `4 deselected`: `tests/cobalt/test_tenancy.py:697`, `:710` (class `:688`), `:263` (class `:239`), `tests/cobalt/test_migrate_proof.py:306`." | NOT SEATED |

Facts, from the build report itself (`/Users/cobalt/cobalt-wt/drc-d1/docs/40 - DevDocs/reports/drc-k2-fix-r1-build-2026-09-25.md`), no verdict:
- **Offline** (F7, `:132`): `2467 passed, 458 skipped, 1 xfailed, 15 warnings in 68.14s (0:01:08)` — `<f>` = 0, "0 errors". Counted: 2463 + 4 = 2467; skipped 449 + 8 + 1 = 458.
- **With-DB** (F8, `:138`): `2915 passed, 6 skipped, 4 deselected, 1 xfailed, 15 warnings in 148.56s (0:02:28)` — `<df>` = 0, "0 errors", "deselected 4 as expected".
- **Live-note** (F6, `:128`): `142 passed, 1 skipped, 15 warnings in 9.78s` — `<lf>` = 0, "0 errors". The one SKIPPED line: `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC … not set`; no SKIPPED line of the live-note leg names `COBALT_LIVE_VAULT_ROOT` (expected none). The with-DB leg's six SKIPPED lines (`:140`) include three that read `COBALT_LIVE_VAULT_ROOT not set` (`test_radar_evaluate.py:691`, `test_catalyst.py:365`, `test_predicate.py:262`) — the with-DB run does not set it; the live-note leg is F6.
- **Deselected count and ids** (`:136`): `4 deselected`; the four ids as the build report names them: `test_tenancy.py::TestMigrationRoundTrip::test_twice_is_idempotent_and_the_rollback_round_trips` (`:697`), `…::test_the_proof_table_names_every_ruled_table` (`:710`), `test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default` (`:263`), `test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches` (`:306`) — matching my own `grep -n` at the tip.
- **Absence probe** (`:141`): `1 failed in 5.64s`, `assert 28 == 32` at `test_migrate_proof.py:316`; "SHORT BY EXACTLY 4, the known shape"; "0016 + 0018: rolled back … absent on cobalt_dev (probe short by 4)".
- **`.env: removed, proven gone`** is written for F3 (`:79`), F5 (`:124`) and F8 (`:142`) — all three.

## Run
| run | opus | grok | sol |
|---|---|---|---|
| RUN-1 (FIFTH) | "RESULT SHOWN — green. The stored `seed.inputs` keys are exactly `{source, from_day, from_book_sha256, stated_book_id}`, with `source == \"carried\"`." | "RUN-1 — RESULT SHOWN. Green. Corrected re-run `1 passed` … Stored seed keys: `inputs` `{source, from_day, from_book_sha256, stated_book_id}` with `source` `carried`" | NOT SEATED |

From the build report (`:119`–`:123`): run 1 `1 passed in 0.21s` on `a51988c9`; after the shadow correction (`d684f80b`) the re-run `1 passed in 0.18s`; "RUN-1 RESULT (green, a plain pin): … `seed.inputs` keys exactly `{source, from_day, from_book_sha256, stated_book_id}` with `source == "carried"`, `stated_book_id == op.id`, `from_day == "2001-01-02"`; `seed.derived` keys exactly `{count, trade_ids, stated_differs}` …". It is GREEN, not a strict `xfail`; no `xfail` in `tests/cobalt/test_drc_k2_fix_r1_runs.py` (`grep -n "xfail"` empty).

## Reds
From the build report:
- **F2 (offline)** `:57`: `5 failed, 19 passed in 0.09s`. Reasons: `test_missing_of_a_parsed_import_is_empty`, `test_missing_of_inverts_the_partial_flag`, `test_missing_of_refuses_an_unreadable_partial_reason` — `ImportError: cannot import name 'missing_of' from 'cobalt.drc.models'`; `test_pairing_not_computed_is_the_first_records_text` — `ImportError: cannot import name 'pairing_not_computed' from 'cobalt.drc.trading_log'`; `test_the_pairing_version_is_4` — `AssertionError: assert 'drc.pairing/3' == 'drc.pairing/4'`. The build says "exactly the named rows": the four new F-5 tests plus the renamed version pin — yes, the rows it named.
- **F3 (with-DB)** `:68`–`:77`: run 1 `8 failed, 36 passed in 2.51s` (one named test red on the test's own setup, corrected in the same lock take — build ESCALATE 4); run 2 `8 failed, 36 passed in 2.64s`. The eight: `…second_current_resolve…refused` — `Failed: DID NOT RAISE <class 'ValueError'>`; `…resolve_restated_on_another_day…` — `ValueError: … supersedes #3 names no single current row — current: none; nothing written`; `…cli_restatement_rebuilds…` — the dry run printed the restatement's own day; `…every_later_day_of_a_stopped_chain…` and `…stale_mark_leaves…` — `KeyError: 'book_stale'`; `…no_trade_day_recorded_by_record_day…` — `assert ('carried' == 'no_trade_carry'`; `…unpaired_day_with_a_stats_log…` — the kept `unmatched — no trades were paired` pair; `…partial_file_missing_only_a_non_pairing_column…` — D_NEXT un-paired by the re-pair. These are the eight tests the build named (F-1 ×3, F-2 ×2, F-3, F-4, F-5).
- **GREEN-as-pin:** the build reports `test_drc_k2_experiments.py:397` `test_x9_pass_c_a_not_computed_match_is_kept` passed "among the 36" (`:78`) and the three suites are 0 failed. At the tip the test is at REAL `tests/cobalt/test_drc_k2_experiments.py:411` (`grep -n`); the build and the classification cite `:397`.

## Checked against the branch
`claim · who · file:line · verdict · ≤30 words`. Code under `/Users/cobalt/cobalt-wt/drc-d1/` (Read / grep), the build report, and the packet's diff.

| # | claim | who | file:line | verdict | walked |
|---|---|---|---|---|---|
| 1 | F-1 NOT CLOSED — a resolve restated to an EARLIER day, with no import and no `day` row on or before it, skips the rebuild; the CLI prints `stated; <day> has no import yet`, exit 0; the later day keeps the superseded resolve's rows | opus | `src/cobalt/drc/cli.py:142` (`has_chain_through(day)` on the effect day), `:177-178`; `src/cobalt/drc/store.py:386` (`min(day, row[0])`), `:393-400`, `:1097-1113`, `:1119-1123`, `:877-883` | HOLDS | Walked: `record_stated_book` accepts (`supersedes` = the single current row; `_reason` for a resolve is the constant, `:1019-1020`). `effect_day` = the earlier day; `has_chain_through` counts only `day <= effect` → false, no import → `_rebuilds` false (`cli.py:142`) → `cli.py:177-178` prints and returns, exit 0. No `rebuild` runs, so the later day's stored rows keep R1's effect; `_with_resolves` does not raise for a later day because the trade is no longer held (`store.py:877-883`). The only restatement tests move the resolve LATER (`test_drc_k2_fix_r1_store.py`, in `fix-diff.part4.md`) |
| 2 | SEAM GAP — seam (4) / AMENDED C7's OTHERWISE clause says nothing recorded on or before the effect day means "no later `book_close` exists to hold the trade id"; false for the input of #1 | opus | AMENDED C7 (`02:17`, in `rules.part4.md`), `seam.md` (4); `cli.py:142`, `:177-178`; `store.py:393-400` | HOLDS | Same input: the effect day is earlier than the superseded row's recorded day, so a later `book_close` (that day's) exists and was built with R1 applied; C7's text says none exists, and the CLI exits 0 |
| — | NOT CHECKABLE FROM READS — `cli.py:190`, `models.py:391` / `:139`, `store.py:1044`, `pairing.py:286` are not in the code-at-tip slices | opus; grok (the same five, "not amended points") | real files | DOES NOT HOLD as a gap — the lines exist | `grep -n` at the tip: `def add_parser` `cli.py:190`; `class SeedBook` `models.py:391`; `opened_on: Optional[date]` `models.py:139`; `def preview_stated_book` `store.py:1044`; `def pair_day` `pairing.py:286` — the seam's signatures land. A fact, not a defect claim |

Where the checkers contradict each other, both quoted and neither smoothed:
- **F-1.** opus: `NOT CLOSED — src/cobalt/drc/cli.py:142 (with src/cobalt/drc/store.py:386)` · grok: `F-1 — CLOSED … src/cobalt/drc/cli.py:151 prints that day; :181 calls rebuild on it … The restatement test rebuilds from the earlier day and asserts no stored trade / day.derived.resolves on either day still carries the superseded id`. Grok describes the restatement that moves a resolve LATER (the tested input); Opus walks a restatement to an EARLIER day with nothing recorded on or before it. Grok's F-1 text does not name that input.
- **Seam.** opus: `SEAM GAP` · grok: `SEAM STATED … has_chain_through src/cobalt/drc/store.py:393. _rebuilds src/cobalt/drc/cli.py:129-142 tests the effect day … otherwise stated; <day> has no import yet and return … That is AMENDED C7.` Grok describes what `cli.py` does; Opus walks the input on which AMENDED C7's stated reason fails.
- A citation note (facts, no claim): a checker citing `store.py:1138` for the `supersedes` rule (grok, F-1) — REAL `store.py:1119-1123` holds that rule (`:1138` is `conn.close()`). Opus's `test_drc_k2_experiments.py:450` / `:535` and `test_drc_k2_store.py:193` are the classification's base-tree numbers; the tip's REAL lines are `:462`, `:548`, `:197` (grok cites those) and the F-1 setup insert `test_drc_k2_store.py:326`. The four pin lines at the tip: `test_drc_k2.py:79`, `test_drc_k1.py:68` (the others' `FN_VERSION ==` matches are in `fix-diff.part3.md`).

Also stated, yourself:
- (i) SWEEP hits (PREFLIGHT): `VaultWriter` none; `INSERT INTO` in `cli.py` none; `INSERT INTO drc_stated_books` exactly ONE, `store.py:1126`, inside `record_stated_book`; `kept_match` none.
- (ii) `git -C /Users/cobalt/cobalt log --oneline 09ce3742..4626a1f2 -- src/cobalt/db_migrations src/cobalt/cli.py configs src/cobalt/aset src/cobalt/prefill src/cobalt/replay src/cobalt/vaultwrite` → EMPTY.
- (iii) `grep -rn "book_stale" …/src/cobalt/drc` → `store.py:592` (the `_commit` docstring), `:655` (the write, `Jsonb({"book_stale": stale_mark})`, in `_commit`), `:928` and `:929` (the read, in `_carried`), `pairing.py:87` (the version comment). No other hit.
- (iv) L32 — I read this report once before the last line: no ticker beyond the constructed `DDD` (and the constructed dates only inside quoted checker / build text), no real date of his, no file name of his and no value written.

## Ready for K3
| checker | CHECK line | ready | reason (verbatim) |
|---|---|---|---|
| opus | `CHECK DRC K2 FIX R1: DEFECT REMAINS · ready for K3: NO · earlier-day resolve restatement skips rebuild; superseded effect stays stored` | NO | earlier-day resolve restatement skips rebuild; superseded effect stays stored |
| grok | `CHECK DRC K2 FIX R1: FIX STANDS · ready for K3: YES` | YES | — |
| sol | NOT SEATED (METER — retry after Sep 26th, 2026 6:47 AM) | — | — |

## FOR THE CLASSIFIER
Round 2 of ≤3 — a HOLD goes to round 3, the last (L75). No class, no recommendation:
1. "F-1 NOT CLOSED — `src/cobalt/drc/cli.py:142` (with `src/cobalt/drc/store.py:386`). … a resolve restated to an earlier day, before anything is recorded, skips the rebuild. The CLI prints `stated; …`, exits 0, and the later day keeps the old resolve's effect in its stored rows." · opus · row F-1 · `cli.py:142`, `:177-178`; `store.py:386`, `:393-400`, `:877-883` · HOLDS
2. "SEAM GAP — Seam (4) and AMENDED C7 (its OTHERWISE clause): C7 says that with no import and nothing recorded on or before the effect day, \"no later `book_close` exists to hold the trade id\". That is wrong for a restatement whose superseded resolve's day is recorded" · opus · the seam / C7 · AMENDED C7 (`02:17`); `cli.py:142`, `:177-178`; `store.py:393-400` · HOLDS

## ESCALATE
1. **opus's `DEFECT REMAINS`, quoted in full with my file-check verdict beside it:** `CHECK DRC K2 FIX R1: DEFECT REMAINS · ready for K3: NO · earlier-day resolve restatement skips rebuild; superseded effect stays stored` — claims 1 and 2 of `## Checked against the branch` HOLD (items 1–2 under `## FOR THE CLASSIFIER`); one input.
2. **grok's `FIX STANDS`, quoted in full with my file-check verdict beside it:** `CHECK DRC K2 FIX R1: FIX STANDS · ready for K3: YES` — its F-1 and seam text describe the tested (later-day) restatement and what `cli.py` does; it does not name the input of claims 1–2 (both quoted above under `## Checked against the branch`, neither smoothed).
3. **Every item under `## FOR THE CLASSIFIER`, restated by number:** items 1–2 (both opus). `defects that HOLD: 2`.
4. **Packet:** no mismatch, no cut (228,794 B against the 300,000 B ceiling). Typos and missing trailing lines of my own copies were caught by the reverse check and byte counts and fixed before any checker launched (`## Packet`).
5. **A checker that did not check / wrote a file it was not told to / every `ASK DESK`:** none (both answered with a `CHECK DRC K2 FIX R1:` line; Grok wrote only `grok-check.md`, as told; Opus wrote nothing). No `ASK DESK`.
6. **The L74 line:** recorded under `## L74`.
7. **The build's LINE MOVED** (its ESCALATE 2): `grep -n "PARTIAL — missing:" src/cobalt/drc/models.py` expected 263, read 262. At the tip the GREEN-as-pin test is at REAL `test_drc_k2_experiments.py:411` (the build and the classification cite `:397`).
8. **The build's ESCALATE 8, named for `03`:** `_repair` (F-4) now RAISES `PairingError` when stored `stats_row` rows exist but the `day` row names no stats import (`store.py:521-522`); "No test reaches it". Opus: "disclosed (build ESCALATE 8)" as part of F-4's shape; Grok: not raised.
9. **Sol's line:** `NOT SEATED (METER — retry after Sep 26th, 2026 6:47 AM)`; the desk seats Sol from that time.
10. **Astra's line:** the K2 NEW BUILD's Astra read is owed from Sep 26th, 2026 6:47 AM (52 ESCALATE 7) — the desk's seat, not this round's. **X12:** NOT RUN — hub-run read (v3 :306, :328), the desk's; carried.
11. **Standing line:** **"Round 2 covers DRC K2 fix r1 only (`09ce3742..4626a1f2`), with RUN-1, the amended seams, AMENDED C7 and its three suites' executed output, checked by Opus 5.5 + Grok (+ Sol when seated) under his R95 (a fix round = other check; Gemini out, R96/R97). With every seated house `ready for K3: YES` and `defects that HOLD: 0`, K2 is checked (L67) and K3's drafter cites the fix report's `## SEAM FOR D2` / `## FOR K3`; a HOLD goes to round 3, the last (L39, L75); a NO with `defects that HOLD: 0` leaves round 3 or his per-case override (L67 OVERRIDE / L73). A1 stays the desk's reading of R51."**
12. **Standing line:** **"The deploy's L68 gate re-proves offline, with-DB and the live-note suite on the stacked tree that ships (D1 + K1 + K2 + D4 + D2 + D3); the deploy prompt gets its own house read (L67, R95 seats)."**

DRC K2 FIX R1 CHECK DONE · round: 2 · opus: CHECK DRC K2 FIX R1: DEFECT REMAINS · ready for K3: NO · earlier-day resolve restatement skips rebuild; superseded effect stays stored · grok: CHECK DRC K2 FIX R1: FIX STANDS · ready for K3: YES · defects that HOLD: 2 · ready for K3: NO · ESCALATE: 12
