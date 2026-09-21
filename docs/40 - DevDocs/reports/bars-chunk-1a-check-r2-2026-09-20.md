# BARS CHUNK 1A CHECK R2 — 2026-09-21 (hub `bars-chunk-1a-check-r2-0920`)

## §0 Headline
Round 2 of at most 3 on chunk 1a, the FIX only (`589d40f..1404f23`, 13 commits): 2 of 3 houses checked (grok `FIX STANDS` · YES; astra `FIX STANDS EXCEPT X9/X14 naming-contract reconciliation` · NO; gemini HARNESS, not retried).
FIX rows CLOSED by every checking house with no holding NOT CLOSED: 12 of 13 — X9 is open (astra NOT CLOSED vs grok CLOSED, over X14 replacing the `w<WW>` child-name shape); new defects 0; nothing reaches a card.
X14 (commit `1404f23`) is outside the classify table's FIX rows; the desk's launch row R48 exists on main. Packet exact to the byte except trailing whitespace stripped by the Write tool (115 bytes, fix diff only).
ESCALATE: 5 (X9 · X14 outside the rows · gemini HARNESS + ASK DESK · ASK DESK whitespace · ASK DESK X14 question set).

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| DATE GATE | `date` | 0 | allowed — `Mon Sep 21 00:15:08 EDT 2026` (2026-09-21, not 09-22 or later → gate passes) |
| authorization | `git -C /Users/cobalt/cobalt log --oneline -6 -- "docs/40 - DevDocs/reports/cto-2026-09-20.md"` | 0 | allowed — top: `90e47bb docs(desk): 09-20 desk 892750de awake …` |
| authorization | `grep -n "^| R13 " …cto-2026-09-20.md` | 0 | allowed — line 86, R13 13:33 ET "Push and approved everything…" |
| authorization | `grep -n "^| R23 " …` | 0 | allowed — line 206, R23 17:47 ET "yes" (grok/agy through 2026-09-21 23:59 ET) |
| authorization | `grep -n "^| R25 " …` | 0 | allowed — line 262, R25 17:58 ET "approved" |
| authorization | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"\| R25 \|" -- …` | 0 | allowed — `e15d03eac2076366a3009b2d56ac40cba92dd6fc` (non-empty) |
| authorization | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"a FIX ROUND is the next lawful step" -- …` | 0 | allowed — `da522a08ceeb4d74eb63f488627b6f48daf21a22` (non-empty) |
| METER | `grok --version` | 0 | allowed — `grok 1.0.25 (f7e67d6988e2) [stable]` |
| METER | `agy --version` | 0 | allowed — `1.2.7` |
| worktree | `ls /Users/cobalt/cobalt-wt/bars-chunk-1a` | 0 | allowed — present (src, tests, docs, configs …) |
| fix built | `tail -n 3 "/Users/cobalt/cobalt-wt/bars-chunk-1a/docs/40 - DevDocs/reports/bars-chunk-1a-2026-09-20.md"` | 0 | allowed — LAST NON-BLANK line: `BARS CHUNK 1A FIX BUILT 1404f23 \| on 589d40f \| offline 2295/0 (355 skipped; fix round 1 2291/0) \| fixed: X14 \| not fixed (listed): 13 \| default migrate statement order unchanged: proven \| card/scoring paths untouched: empty diff \| db: OWED — 0 requires_db tests written, never run \| ESCALATE: 6` → `<fix tip>` = `1404f23`, `<round-1 tip>` = `589d40f` (both taken from that line) |
| fix commits | `git -C /Users/cobalt/cobalt log --oneline 589d40f..1404f23` | 0 | allowed — **13 commits**: 1404f23 X14 · 8dddf2b report(fix round 1) · 793f452 X11 · 81dae9c X10 · beab8c7 X9 · 5114af9 X8 · c8893c7 X7 · e493c95 X6 · 4778c31 X5 · 19e0228 X4 · e292817 X3 · a4f9a07 X2 · de70755 X1 |
| branch tip | `git -C /Users/cobalt/cobalt log --oneline -1 bars/chunk-1a-0920` | 0 | allowed — `6961ee0 docs(report): bars chunk 1a fix round 1b — the child-name seam` (the fix-report commit above `<fix tip>`) |
| boundary / staging list | `git -C /Users/cobalt/cobalt log --stat --oneline 589d40f..1404f23` | 0 | allowed — paths touched: `docs/40 - DevDocs/cobalt/db_migrations/placement.md`, `docs/40 - DevDocs/cobalt/db_migrations/cli.md`, `src/cobalt/db_migrations/placement.py`, `src/cobalt/db_migrations/cli.py`, `tests/cobalt/test_migrate_proof.py`, `tests/cobalt/test_tenancy.py`, `docs/40 - DevDocs/reports/bars-chunk-1a-2026-09-20.md`. **24 file-touches** across the 13 commits. |
| round-1 folder | `ls scratch/tribunal-bars-0920/chunk-1a-check` | 0 | allowed — holds `grok-check.md`, `gemini-check.md`, `astra-check.md` (+ round 1's staged copies) |
| recovery | `ls scratch/tribunal-bars-0920/chunk-1a-check-r2` | 1 | allowed — "No such file or directory" → **fresh run** |
| CODEX PROBE | `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` (background) | 0 | allowed — answer `OK`, exit 0, no usage-limit text → **astra: UP** |

Note: the branch under check carries X1–X13 AND the later X14 step (`1404f23`, "fix round 1b") in the one range `589d40f..1404f23`, as the fix report's own closing line says. `classify.md` (staged below) is the list of what was to be fixed.

## Packet
Folder `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/chunk-1a-check-r2/` (no `mkdir`; the first Write created it). Every file staged Read → Write; each checked with `wc -c` (and `wc -l`) against its original.

**One deviation from "byte-identical", disclosed and unavoidable:** the Write tool STRIPS TRAILING WHITESPACE from every line (probed: a 4-line test file with trailing space/tab came back 7 bytes, not 10; the probe file `wstest.tmp` stays in the folder, listed in QUESTIONS-R2 as "ignore"). Consequence: every file whose original has no trailing whitespace matches its original to the byte; the fix diff (whose blank context lines are `" "` and whose `---`/`+++` header lines end in a tab) differs by exactly the whitespace bytes. Round 1's hub hit the same thing (its check report: "the diff's whitespace-only 43-byte gap"). `ASK DESK` is under `## ESCALATE`; safe default taken: continue, disclosed, and the houses are told in QUESTIONS-R2's closing note.

| staged file | original | original bytes | staged bytes | check |
|---|---|---|---|---|
| `fix-diff.md.part1` … `part5` | `git -C /Users/cobalt/cobalt log -p 589d40f..1404f23` (persisted tool result, 1,754 lines) | 107,195 | 14,866 + 49,325 + 20,192 + 17,282 + 5,415 = 107,080 | 13 `^commit ` (= the 13 commits of `log --oneline`) · 24 `^diff --git` (= the 24 file-touches of `--stat`) · line counts per part sum to 1,754 · the 115-byte gap = the counted trailing-whitespace bytes (per part: 19 + 7 + 44 + 38 + 7). `part2` is 49,325 B (> 38,000): it is ONE commit (`8dddf2b`, the fix's report, one file, one hunk) and the rule cuts only at a `commit`/`diff --git` line; it is staged whole rather than cut inside a hunk. |
| `classify.md` | `reports/bars-1a-fix-draft-2026-09-20.md` lines 11–47 (`## CLASSIFY`) | 9,910 | 10,052 − 142 (one-line header) = 9,910 | exact |
| `round1-verdicts.md` | `reports/bars-chunk-1a-check-2026-09-20.md` lines 165–204 and 219–225 (`## Checked against the branch`, `## ESCALATE`; the report's closing stop line 227 is not copied and its blank line 226 is not either) | 10,098 + 954 | header + 10,098 + 954 | exact (both sections byte-counted against `grep -b` offsets) |
| `fix-report.md.part1` … `part3` | worktree `docs/40 - DevDocs/reports/bars-chunk-1a-2026-09-20.md`, `# FIX ROUND 1` (line 690) to end (line 1478); it carries fix round 1 AND `# FIX ROUND 1b` (X14) | 76,479 | 36,723 + 35,759 + 3,997 = 76,479 | exact (original has 0 trailing-whitespace lines) |
| `fix-prompt.md.part1`, `part2` | `prompts/2026-09-20/20-bars-chunk-1a-fix.md` WHOLE | 39,957 | 34,730 + 5,227 = 39,957 | exact |
| `fixed/cli.py.part1`, `part2` | worktree `src/cobalt/db_migrations/cli.py` | 57,332 | 34,609 + 22,723 = 57,332 | exact |
| `fixed/placement.py` | worktree `src/cobalt/db_migrations/placement.py` | 11,711 | 11,711 | exact |
| `fixed/test_migrate_proof.py.part1` … `part5` | worktree `tests/cobalt/test_migrate_proof.py` | 158,599 | 34,171 + 34,033 + 37,530 + 34,552 + 18,313 = 158,599 | exact (cut only between test functions) |
| `fixed/test_tenancy.py.part1`, `part2` | worktree `tests/cobalt/test_tenancy.py` | 41,973 | 31,800 + 10,173 = 41,973 | exact |
| `fixed/cli.md` | worktree `docs/40 - DevDocs/cobalt/db_migrations/cli.md` | 29,832 | 29,832 | exact |
| `fixed/placement.md` | worktree `docs/40 - DevDocs/cobalt/db_migrations/placement.md` | 6,139 | 6,139 | exact |
| `QUESTIONS-R2.md` | the prompt's QUESTIONS-R2.md text (quotes removed, the JSON-style `\"` shown as `"`) + the appended "Files in this folder:" paragraph and a closing note on the whitespace | — | 8,230 | — |

The sources under `fixed/` and the whole 1a report were checked for trailing whitespace first: `grep -c -E "[[:space:]]$"` = 0 on all six `fixed/` originals and on the report. The prompt's `--stat` list names the six `fixed/` paths plus the 1a report (staged as item 5); nothing else was touched by the fix.

Not staged, by the prompt's own list: the build prompt, the spec, v3, his rulings and chunk E's reports (named in QUESTIONS-R2 as round 1's copies, for reference only: `../chunk-1a-check/build-prompt.md.part1…3`, `../chunk-e-check/spec-final-s3.md`, `spec-final-s8.md`, `../chunk-1a-check/owner-rulings-r19-r25.md`). Also not staged: `prompts/2026-09-20/25-bars-chunk-1a-fix-1b.md`, the prompt of fix round 1b (X14) — the prompt's staging list names only prompt 20; the fixer's own 1b account is in `fix-report.md`.

**One fact the packet cannot hide, and the file list says so:** the range `589d40f..1404f23` carries fix round 1 (X1–X13, `classify.md`'s FIX rows) AND fix round 1b (X14, commit `1404f23`, the child-name pattern); `classify.md` has no X14 row and QUESTIONS-R2's FIRST asks about X1…X13. The file list in QUESTIONS-R2 names where X14 lives (`fix-report.md` `# FIX ROUND 1b`, the first commit of `fix-diff.md`). `ASK DESK` under `## ESCALATE`.

## CONTINUE
Houses launched (`run_in_background`, one attempt each) after staging finished, before 00:51 ET on Mon 2026-09-21:
- **gemini: HARNESS** — the whole output, verbatim: `jetski: no output produced — a tool required the "command" permission that headless mode cannot prompt for, so it was auto-denied. Add an allow-rule under permissions.allow in settings.json (e.g. command(<target>)). Alternatively, re-run with --dangerously-skip-permissions to auto-approve all tools.` `[exited with code 0]`. No answer file. One attempt is the rule, so it is not retried; `--dangerously-skip-permissions` is not used (never more access).
- grok: answered (`grok-check-r2.md`, written by grok itself; last line `CHECK R2: FIX STANDS · ready for its deploy prompt: YES`).
- astra: answered (`astra-check-r2.md`, the hub wrote its final printed message byte for byte; last line `CHECK R2: FIX STANDS EXCEPT X9/X14 naming-contract reconciliation · ready for its deploy prompt: NO · …`).
Nothing left to do: the run is finished and the last line below is the stop line. The desk reads this report (L67: a round-3 fix is the desk's call and the LAST; no fourth round).

## Per FIX row
Houses: grok `CHECK R2: FIX STANDS` (writes `grok-check-r2.md` itself) · gemini HARNESS (no answer) · astra `CHECK R2: FIX STANDS EXCEPT X9/X14 naming-contract reconciliation` (`astra-check-r2.md`, the hub wrote its final printed message byte for byte). Line references in the houses' cells are to the STAGED parts; I verified the ones I relied on against the originals (see `## Checked against the branch`).

| row | what it fixes (classify.md) | grok | gemini | astra | CLOSED: n of 2 |
|---|---|---|---|---|---|
| X1 | restore the joined-row-text assertion | CLOSED | HARNESS | CLOSED | 2 of 2 |
| X2 | `_replaced` count difference alone | CLOSED | HARNESS | CLOSED | 2 of 2 |
| X3 | per-row proof status asserted | CLOSED | HARNESS | CLOSED | 2 of 2 |
| X4 | FROZEN_ARCHIVE refused before connect | CLOSED | HARNESS | CLOSED | 2 of 2 |
| X5 | AMBER budget read before connect | CLOSED | HARNESS | CLOSED | 2 of 2 |
| X6 | non-finite budget refused | CLOSED | HARNESS | CLOSED | 2 of 2 |
| X7 | `status_of` with no probes refused | CLOSED | HARNESS | CLOSED | 2 of 2 |
| X8 | round-trip digest parser reads the digest | CLOSED | HARNESS | CLOSED | 2 of 2 |
| X9 | partition-child pattern complete ASCII match | CLOSED — "At X9 (`beab8c7`) the pattern became `…\Z` — complete ASCII, narrower, shape unchanged … X14 then replaced the shape (not a `$`/`\d` widening)" | HARNESS | **NOT CLOSED — against its unchanged-shape requirement.** "`fixed/placement.py:255` and `:281` admit `bars_p_20261026`; `bars_p_2026w31` now raises … the final language is not a subset of round 1's `bars_p_<YYYY>w<WW>`. Commit `beab8c7` satisfied X9; X14 subsequently replaced that convention." | 1 of 2 |
| X10 | lock-ownership instrument: BEFORE boundary, migrate pid | CLOSED (instrument; NOT RUN, L70) | HARNESS | CLOSED as an instrument; execution owed | 2 of 2 |
| X11 | `--proof-only` observed sending no lock | CLOSED (instrument; NOT RUN, L70) | HARNESS | CLOSED as an instrument; execution owed | 2 of 2 |
| X12 | correction: `_replaced` baseline is the FIRST parameter | CLOSED | HARNESS | CLOSED | 2 of 2 |
| X13 | correction: "strictly stronger", "eleven green" | CLOSED | HARNESS | CLOSED | 2 of 2 |

Also answered (both houses, same words in substance): X4/X5/X7 add no statement between `_connect` and `conn.commit()` on the default path (grok `X4/X5/X7 order` row; astra: "no changed statement lies between `_connect` and `conn.commit()`"); neither X10 nor X11 sends a statement on the migrate connection before its first probe. No NEW DEFECT INTRODUCED from either house. grok NOT CHECKABLE: whether `conn.info.backend_pid` sends a statement (fixer cites installed psycopg source, not staged). astra NOT CHECKABLE: database outcomes, E-15 interleavings, the generator's own code, the integrated stacked-tree result.

## Per not-fixed row
| row | class | grok | gemini | astra |
|---|---|---|---|---|
| NR1 | NOT REAL | AGREE | HARNESS | AGREE |
| NR2 | NOT REAL | AGREE | HARNESS | AGREE |
| NR3 | NOT REAL | AGREE | HARNESS | AGREE |
| U1 | UNPROVEN | AGREE | HARNESS | AGREE |
| U2 | UNPROVEN | AGREE | HARNESS | AGREE |
| U3 | UNPROVEN | AGREE | HARNESS | AGREE |
| U4 | UNPROVEN | AGREE | HARNESS | AGREE |
| U5 | UNPROVEN | AGREE | HARNESS | AGREE |
| U6 | UNPROVEN | AGREE | HARNESS | AGREE |
| S1 | OUT OF SCOPE | AGREE | HARNESS | AGREE |
| S2 | OUT OF SCOPE | AGREE | HARNESS | AGREE |
| O1 | OWNER ITEM | AGREE — "what he would be ruling: whether an empty default lock list **closes** chunk E ESCALATE 6, or only **arms** it for chunk 4" | HARNESS | AGREE — "Resolving the prompt's conflicting closure language belongs to the owner. The later report claims R45 settled it as armed now, closure in chunk 4; that ruling itself is not supplied." |
| O2 | OWNER ITEM | AGREE — "whether one piped `pytest … \| tail -n 5` outside the bare-shape rule is an owner item or acceptable. Nothing in this fix counts on it." | HARNESS | AGREE — "Disposition of the bare-command deviation remains the owner's process decision." |

No house DISAGREES on any class; no OWNER-ITEM disagreement to quote.

## Assertions and boundary
- **grok (a) weaker assertions:** "NONE. No `assert` removed. X6 parametrize extended. X3/X10 keep the old assert and add. X8 replaces a wrong helper, not an assertion. X14 re-points the same `KeyError` / `side_of is SYSTEM` / ordered `LOCK TABLE` compares to the generator's name; old `w<WW>` admitted names are now near-misses (tighter). No test newly skipped or xfailed."
- **grok (b) outside the FIX rows:** "X14, commit `1404f23` (not a CLASSIFY row; authorized fix round 1b)" — hunks: `placement.py` (import, READING comment, `_PARTITION_CHILD` → `(?P<date>[0-9]{8})`, week guard → `strptime`), `placement.md` READING paragraph, `test_tenancy.py` (admitted names → `bars_p_20261026`/`20240101`/`20251229`; near-miss list 15 → 19 rows), `test_migrate_proof.py` (`test_a_registered_relation_admitted_by_the_pattern_is_accepted` fixture `bars_p_2026w31` → `bars_p_20261026`). "Report commit `8dddf2b` is X12/X13 + CLOSE, in scope."
- **grok L52:** NOTHING REACHES A CARD.
- **astra (a):** "NONE weakened by X1–X13 … X14 changes the asserted naming contract: former acceptance cases become rejection cases and near-miss fixtures are repointed. Under the documented calendar-date convention, these retain their corresponding test strength; they do not preserve X9's expressly unchanged convention."
- **astra (b):** "X14, commit `1404f23`, is outside X1–X13" — hunks `fix-diff.md.part1:13, :52, :60, :112, :130, :159, :205, :256, :265` (the same set); "No additional out-of-row code hunk was identified. All changed paths remain within the supplied allowed path set."
- **astra L52:** NOTHING REACHES A CARD.
- **gemini:** no answer (HARNESS).

## Checked against the branch
Originals: the worktree `/Users/cobalt/cobalt-wt/bars-chunk-1a/` (Read/grep) and `git -C /Users/cobalt/cobalt`; `<round-1 tip>` `589d40f`, `<fix tip>` `1404f23`. Nothing was run.

| # | claim | who | file:line | verdict |
|---|---|---|---|---|
| 1 | X1's added assertion is an AST check for a `.join` whose receiver is the constant `'\|'`/`b'\|'`, plus a recorder that fails any `md5` update that is neither `b"\|"` nor one row text, and a pull/fold order check; the regression `rows = list(row_texts)` / `md5("\|".join(rows)…)` trips both | grok, astra | `tests/cobalt/test_migrate_proof.py:2404-2417` (AST), `:2420-2483` (recorder; constructor data is judged as an update, `:2437-2442`; pull-then-fold order `:2475-2483`); `_digest_rows` `cli.py:407-437` streams. The mutation puts the joined bytes into one `md5(...)` constructor call → not `b"\|"`, not in `row_bytes` → red; `'\|'.join` is the flagged node | HOLDS (by reading; not run) |
| 2 | the two `string_agg` assertions of the X1 test are kept and the docstring sentence "not attempted here" was replaced | grok, astra | `test_migrate_proof.py:2393-2402` kept; `:2383-2389` new docstring (diff `de70755`, 5 removed lines all docstring) | HOLDS |
| 3 | X2: equal digests `"d"`, counts 3 vs 2, `_replaced` False vs target and vs source; `_replaced` still compares `rows` and `digest` | grok, astra | `test_migrate_proof.py:2551-2574`; `cli.py:583-586` | HOLDS |
| 4 | X3: per-table row selected by first token, four `->`, proof column read after the fourth `->`, old `assert "CONTENT_VERIFIED" in out` kept | grok, astra | `test_migrate_proof.py:2924-2934` | HOLDS |
| 5 | X4: `_assert_frozen_archive_inactive()` is called in `cmd_migrate` before every `_connect` on every branch; `policy_of` keeps its call; the test covers forward/rollback/`--proof-only` and asserts `_connect` never called, no statements, `committed == 0` | grok, astra | `cli.py:1064` (call) < `:1083` (`--proof-only` `_connect`) < `:1099` (read-write `_connect`); `:288` (`policy_of` call); `test_migrate_proof.py:2747-2795` | HOLDS |
| 6 | X5: budget read once at `:1097`, after the `--proof-only` early `return` (`:1092`) and before `_connect` (`:1099`); passed on as `budget_s`; `_print_cost` keeps a keyword default | grok, astra | `cli.py:1092`, `:1097`, `:1099`, `:1178-1180`, `:713-718`, `:735`; tests `test_migrate_proof.py:3620-3683` | HOLDS |
| 7 | X6: `math.isfinite` refusal naming the key precedes `<= 0`; parametrize keeps `0,-1,"thirty",None` and adds nan/inf/-inf | grok, astra | `cli.py:697-704`; `test_migrate_proof.py:3686-3689` | HOLDS |
| 8 | X7: `if not probes:` is `status_of`'s first statement, before `policy_of`; test covers `bars` and an unruled table | grok, astra | `cli.py:317-322` (`policy_of` at `:323`); `test_migrate_proof.py:2803-2811` | HOLDS |
| 9 | X8: `_digests` reads the token after the fourth `->`; two offline tests render the real `_print_proof` | grok, astra | `tests/cobalt/test_tenancy.py:686-704`, `:918-973` | HOLDS |
| 10 | X10: observes the FIRST `_probe_all` call only, `l.pid = migrate_pid` from `conn.info.backend_pid`, two relations each asserted, original `assert "AccessExclusiveLock" in held` kept, observer on a second connection | grok, astra | `test_migrate_proof.py:3339-3392` | HOLDS as reading |
| 11 | X10/X11: `conn.info.backend_pid` sends no statement on the migrate connection | grok (NOT CHECKABLE), astra | fixer cites installed psycopg source (`fix-report.md`), not staged | NOT CHECKABLE FROM READS — run/read: `psycopg/_connection_info.py` and `pq_ctypes.py` `backend_pid`, or a recording connection around `conn.info.backend_pid` |
| 12 | X11: `cmd_migrate(proof_only=True, pre_probe_locks=("cobalt_jobs",))` through a `_RecordingConn` over the real connection; asserts no `LOCK TABLE`, no `lock_timeout`; second-session pid check before and after; the wrapper starts after `_connect`, so `SHOW server_encoding` is unrecorded (disclosed) | grok, astra | `test_migrate_proof.py:3448-3521`; `_RecordingConn` `:263-283` records `execute` and named-cursor `execute` | HOLDS |
| 13 | X12/X13 are appended corrections in the report; the pre-existing report is not edited | grok, astra | `git log -p 589d40f..bars/chunk-1a-0920 -- <report>`: 0 removed lines (persisted output, `grep -c "^-[^-]"` = 0) | HOLDS |
| 14 | `_replaced`'s baseline is its FIRST parameter | grok, astra | `cli.py:556` | HOLDS |
| 15 | NR2: `string_agg` occurs in `cli.py` only in a docstring | grok | `grep -n string_agg cli.py` → `:472` only | HOLDS |
| 16 | NR3/O1: `PRE_PROBE_LOCKS = ()`, acquire sends nothing by default | grok | `cli.py:800`, `:1114` | HOLDS |
| 17 | S1: no `--full` in `add_parser`; S2: `cli.md:120` still says the BEFORE probe is not under the ceiling | grok | `cli.py:1211-1253` (no `--full`); `cli.md:119-121` | HOLDS |
| 18 | X9: the pattern at the fix tip is `^bars_p_(?P<date>[0-9]{8})\Z` plus `strptime`, replacing round 1's `w<WW>` shape; `bars_p_2026w31` now raises; the language is not a subset of round 1's | astra (grok agrees on the replacement) | `placement.py:255`, `:281-287`; `fix-diff.md.part1:107-108` (old regex line removed, new added); the tests re-pointed `test_tenancy.py:826-850` | HOLDS (as a fact; whether it is a defect is the desk's — see ESCALATE) |
| 19 | at `beab8c7` (X9) the pattern was `…(?P<year>[0-9]{4})w(?P<week>[0-9]{2})\Z`, complete and ASCII, same shape | grok | `git show beab8c7` hunk in `fix-diff.md.part3` (`placement.py` line `:232-238`) | HOLDS |
| 20 | X14's authority: the desk's seam call and the launch row R48 are committed on main; the fix prompt's X9 text ("shape … is NOT changed") is round-1's and the 1b prompt (`25-bars-chunk-1a-fix-1b.md`) is not staged | astra, grok | `cto-2026-09-20.md:463` (row R48, "ONE step X14, the child-name seam"); `git -C /Users/cobalt/cobalt log -1 -S"the GENERATOR's Monday-date shape stands"` → `407091266786727a04f188baa81feebedf4c305d` (non-empty); `prompts/2026-09-20/25-bars-chunk-1a-fix-1b.md` present | HOLDS (record exists; its wording is the desk's) |
| 21 | astra's out-of-row hunk list for X14 (`fix-diff.md.part1:13,52,60,112,130,159,205,256,265`) | astra | those are the hunk headers of `1404f23` in part1 | HOLDS |
| 22 | after X14, Unicode digits still refuse only by `strptime` and not by the regex, i.e. a second mechanism (`strptime` rejects non-ASCII digits) | grok | `placement.py:255` uses `[0-9]` — the regex itself refuses non-ASCII; whether CPython's `strptime` rejects them is a runtime fact | NOT CHECKABLE FROM READS — run: `datetime.strptime("２０２６1026", "%Y%m%d")` (incidental to the verdict: `[0-9]` refuses them first) |
| 23 | a `$` pattern would admit `bars_p_20261026\n` (so `\Z` is proven by the newline row) | grok | re semantics: `$` before a trailing newline; the captured group excludes it, so `strptime` would succeed; the test row `test_tenancy.py:848` | HOLDS by re semantics; not executed |
| 24 | NOTHING REACHES A CARD | grok, astra | `git -C /Users/cobalt/cobalt log --oneline 589d40f..1404f23 -- src/cobalt/cards src/cobalt/radar src/cobalt/archiver configs` → empty | HOLDS |

Count: 24 claims — HOLD 22 (rows 1–10, 12–21, 23, 24 counted as HOLDS/HOLDS as reading/fact) · NOT CHECKABLE FROM READS 2 (rows 11, 22) · DO NOT HOLD 0.

**The four facts the fix promised, stated plainly:**
(i) `git -C /Users/cobalt/cobalt log --stat 589d40f..bars/chunk-1a-0920` names exactly `src/cobalt/db_migrations/cli.py`, `src/cobalt/db_migrations/placement.py`, `tests/cobalt/test_migrate_proof.py`, `tests/cobalt/test_tenancy.py`, `docs/40 - DevDocs/cobalt/db_migrations/cli.md`, `docs/40 - DevDocs/cobalt/db_migrations/placement.md`, and `docs/40 - DevDocs/reports/bars-chunk-1a-2026-09-20.md` — no other path. **HOLDS.**
(ii) `git -C /Users/cobalt/cobalt log --oneline 589d40f..1404f23 -- src/cobalt/cards src/cobalt/radar src/cobalt/archiver configs` is EMPTY. **HOLDS.**
(iii) `git -C /Users/cobalt/cobalt log -p 589d40f..bars/chunk-1a-0920 -- "docs/40 - DevDocs/reports/bars-chunk-1a-2026-09-20.md"` (two commits, `8dddf2b` +487 and `6961ee0` +303, `--stat` "insertions(+)" only): removed lines that are not the `---` header = **0**. Nothing above the `# FIX ROUND 1` heading changed. **HOLDS.**
(iv) Removed lines (`^-[^-]`) in the diff of the two test files, listed from the persisted diff: none is deleted outright as an `assert` — the two `assert` lines removed are `test_tenancy.py`'s `assert "bars_p_2026w31" not in placement.PLACEMENT, (` and `assert "bars_p_2026w31" not in system`, each replaced in the same hunk by the same assertion at `bars_p_20261026` (X14); the other removed lines are docstring/comment text, the parametrize header extended by X6, the pid-less query block of X10 (moved into a per-relation loop with `AND l.pid = %s` added, its `assert "AccessExclusiveLock" in held` kept), `parts[-2]` in X8's helper, and old near-miss/admitted `w<WW>` names re-pointed by X14. **No `assert` is removed without an equal replacement.**

## Ready for a deploy prompt
| house | ready | reason verbatim |
|---|---|---|
| grok | YES | `CHECK R2: FIX STANDS · ready for its deploy prompt: YES` |
| gemini | — | HARNESS: no answer |
| astra | NO | "Reconcile the changed naming contract with this check before deployment." (`CHECK R2: FIX STANDS EXCEPT X9/X14 naming-contract reconciliation · ready for its deploy prompt: NO`) |

## ESCALATE
No recommendation added.
1. **A NOT CLOSED my file-check HOLDS (as a fact) — X9, astra vs grok.** astra: NOT CLOSED, "the final language is not a subset of round 1's `bars_p_<YYYY>w<WW>`"; grok: CLOSED, "X14 then replaced the shape (not a `$`/`\d` widening)". Both quoted in `## Per FIX row`; nothing smoothed. The file-check confirms the pattern at the tip is `bars_p_<YYYYMMDD>` (check row 18) and that the fix prompt's X9 text said the shape was not to change (round 1's). The desk's record for X14 exists (row R48, seam call `407091266786727a…`).
2. **A hunk outside the FIX rows my file-check HOLDS — X14, commit `1404f23`** (`placement.py`, `placement.md`, `test_tenancy.py`, `test_migrate_proof.py`), named by both houses; `classify.md` has no X14 row and the prompt's QUESTIONS-R2 FIRST asks X1…X13 only.
3. **A house that did not check — gemini: HARNESS.** Verbatim: `jetski: no output produced — a tool required the "command" permission that headless mode cannot prompt for, so it was auto-denied. Add an allow-rule under permissions.allow in settings.json (e.g. command(<target>)). Alternatively, re-run with --dangerously-skip-permissions to auto-approve all tools.` One attempt per house is the rule. **ASK DESK: gemini was on HARNESS for round 2 — a second attempt for gemini alone (the same launch line fired a permission-denied read in this run; round 1's same spelling worked), or two houses for this round? [01:04 ET]** Safe default taken: two houses (L67's floor of one house other than the author is met); no retry by me.
4. **ASK DESK (packet): the staging tool strips trailing whitespace, so a byte-identical packet is impossible for the fix diff (115 bytes over 5 parts; every other staged file is exact to the byte) — accept this, or should a whitespace-preserving copy path be given the hub? [01:04 ET]** Safe default taken: continued, disclosed in `## Packet` and in QUESTIONS-R2's closing note. Also: `fix-diff.md.part2` is 49,325 B (> the 38,000 B part limit) because it is one commit with one file and one hunk and the cut rule allows only `commit`/`diff --git` lines.
5. **ASK DESK (packet): the prompt's QUESTIONS-R2 asks X1…X13; the branch range also carries X14 (fix round 1b), which `classify.md` does not list. I named its location in the file list rather than stay silent; both answering houses then reported it as outside the rows. Should the round-2 question set be extended to X14 before round 3? [01:04 ET]** Safe default taken: file list only, no change to the question text; prompt 25 (the 1b prompt) not staged.

Not escalated, recorded: no `FIX AGAIN` from any house; no class DISAGREE; no L52 finding; no weaker assertion my file-check HOLDS; no NEW DEFECT.

BARS CHUNK 1A CHECK R2 DONE · grok: CHECK R2: FIX STANDS · ready for its deploy prompt: YES · gemini: HARNESS · astra: CHECK R2: FIX STANDS EXCEPT X9/X14 naming-contract reconciliation · ready for its deploy prompt: NO · houses that checked: 2 of 3 · FIX rows CLOSED: 12 of 13 · new defects: 0 · ready for a deploy prompt: 1 of 2 · ESCALATE: 5
