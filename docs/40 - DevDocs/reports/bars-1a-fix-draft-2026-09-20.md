# Bars chunk 1a — fix-round prompts drafted (2026-09-20)

## §0 Headline
- Drafted, NOT launched: `20-bars-chunk-1a-fix.md` (Opus 5 fix build, existing worktree, offline) and `21-bars-chunk-1a-check-r2.md` (Sonnet 5 round-2 check, reads ONLY the fix).
- Classified 26 round-1 findings: FIX 13 · NOT REAL 3 · UNPROVEN 6 · OUT OF SCOPE 2 · OWNER ITEM 2. Every FIX row is backed by a check-hub row that HOLDS.
- New rule strings: 0. Prompt 20's whole rule block matches prompt 10's line exactly, and prompt 21's matches 08's (one whole-block `grep -c -F`, count 1 in each file).
- ESCALATE 6: 2 OWNER ITEMs, 2 OUT OF SCOPE for the desk, 2 `ASK DESK` (prompt 20's launch row `R__`; how a meter stop shows up for the watcher).

Seat `bars-1a-fix-draft-0920`, Opus 5, 19:0x–19:33 ET. No database, docker, pytest or git write, and no launch. Three files were written with the Write tool.

## CLASSIFY
Hub row = the row in `reports/bars-chunk-1a-check-2026-09-20.md` `## Checked against the branch`. File:line = my own read of the branch at `589d40f` (`/Users/cobalt/cobalt-wt/bars-chunk-1a/`), unless it says `main`.

| id | finding | house(s) | hub verdict | my file:line read | class |
|---|---|---|---|---|---|
| X1 | The joined-row-text assertion was removed. No test catches a `_digest_rows` that materialises the rows (`list(row_texts)`, then `"|".join`). The builder gave `", ".join` as the ground, which is not a `"|".join` match. | astra F1 (ASSERTION WEAKENED), grok ("unproven by tests") | row 1 HOLDS · row 26 HOLDS | `tests/cobalt/test_migrate_proof.py:2376-2398` checks for `string_agg` only, and its docstring (`:2383-2387`) says a join check "is not attempted here". Prompt 10 step 1 asks that the test "builds no joined string". `cli.py:418-425` is correct today. | **FIX** |
| X2 | The `_replaced` count-mismatch tests change count AND digest together, so they cannot isolate a dropped `rows` comparison. | astra (step 1) | row 23 HOLDS | `test_migrate_proof.py:2456-2463` (`fewer = _probe_of(_BASELINE_ROWS[:2])`). Prompt 10 step 1 says "on **both** `rows` and `digest`". | **FIX** |
| X3 | The per-table status assertion loops over `name` without using it. | astra (step 2) | row 22 HOLDS | `test_migrate_proof.py:2745-2746` (`for name in tables: assert "CONTENT_VERIFIED" in out`) | **FIX** |
| X4 | The `FROZEN_ARCHIVE` refusal is reached only after `conn.commit()`, through `_print_proof → status_of → policy_of`. | grok (EXCEPT 3), astra F2 | row 8 HOLDS | `cli.py:1076` commit → `:1132` `_print_proof` → `:608` → `:311` → `:287`. The refusal's own text at `:276` says "this run will not start". The test at `:2607-2633` calls `policy_of` directly. | **FIX** |
| X5 | The AMBER-budget read runs after commit, so a missing or bad row crashes after the migration committed. | astra (5) | row 10 HOLDS | `cli.py:643` → `:698` `_proof_budget_per_side_s()`, after `:1076`. Prompt 10 step 5 says "validated on load, a bad value crashes naming the key". | **FIX** |
| X6 | The budget validator accepts NaN and ±inf. | astra (5) | row 10 HOLDS; the hub left the loader "unstaged" | `cli.py:670-682` (`budget <= 0` is False for NaN). I read the loader: `src/cobalt/taxonomy/tunables.py:89` has `value: Any`, so it rejects nothing. That settles astra's caveat. | **FIX** |
| X7 | `status_of(table)` with zero probes returns `CONTENT_VERIFIED`. | astra F2 | row 9 HOLDS | `cli.py:320-322` (`any(...)` over `()` is False). Prompt 10 step 2 says "a table the probe did not read ⇒ never `CONTENT_VERIFIED`". | **FIX** |
| X8 | After the `proof` column was added, `_digests` parses `parts[-2]`, which is now the status. The round-trip equality can pass on different digests. | astra F4 | row 14 HOLDS | `tests/cobalt/test_tenancy.py:686-693`. The row layout is `cli.py:615-618` `… {dig} {status} {verdict}`. Step 2 added the column and broke this consumer. | **FIX** |
| X9 | The pattern uses `$` with `.match()`, which admits a trailing `\n`, and `\d`, which admits non-ASCII digits. Neither case is tested. | astra F5 | row 15 HOLDS ("from the documented `re` semantics; not executed here") | `placement.py:235`, `:258`. Prompt 10 step 3 says "admits **only** those shapes". Prompt 20 runs the red-first test as the FIRST run of the claim; a case that is green before the fix becomes NOT REAL (measured) and gets no code change. | **FIX** |
| X10 | The lock-ownership DB test watches both probes through one `held` list, needs only one occurrence, and has no PID filter. A lock moved after BEFORE still passes. | astra F3a | row 11 HOLDS | `test_migrate_proof.py:3136-3166`. Prompt 10 step 4 says the lock is held "before the first probe row is read". The fix is test-only and `requires_db`; its red-first is NOT RUN (L70). | **FIX** |
| X11 | The "proof-only issues no lock" DB test never calls `cmd_migrate`. It sends a lock itself and checks that the server refuses. | astra F3c | row 13 HOLDS | `test_migrate_proof.py:3209-3219`. Prompt 10 step 4 says "the `--proof-only` READ ONLY path never issues a lock statement". The fix ADDS a test beside it and keeps the old one. `requires_db`. | **FIX** |
| X12 | Report ESCALATE 8 says "the third is the trusted source baseline". `_replaced`'s baseline is its FIRST parameter. | astra (ESCALATE 8) | row 24 HOLDS | report `:659-661`; `cli.py:544` | **FIX** (appended correction; no code) |
| X13 | Two report sentences are inexact: "strictly stronger" (the `ast` fix only removes false positives), and "the eleven green are group 10's existing tests" (new tests match the `-k` too). | astra | row 4 HOLDS · row 20 HOLDS (the reading) | report `:161`, `:344-349`; tests `:2922`, `:3082` | **FIX** (appended correction; no code) |
| NR1 | Group 1's oracle and group 5's cursor test "still prove" there is no joined row-text. | gemini | row 2 DOES NOT HOLD | Group 1 compares against `md5("|".join(rows))`, which a materialising fold also meets. Group 5 drives `_stream_row_texts`, not `_digest_rows`. | **NOT REAL** |
| NR2 | `string_agg` appears in `cli.py` at `:16` and `:460`. | grok | row 7 DOES NOT HOLD | Only `:460`, in a docstring. | **NOT REAL** |
| NR3 | Step 4 "Closes E-15 ESCALATE 6", as shipped. | gemini | row 18 DOES NOT HOLD | `cli.py:763` `PRE_PROBE_LOCKS = ()`; no caller supplies a list | **NOT REAL** |
| U1 | The writer-blocking DB test uses `db.connect_migration` (AUTOCOMMIT), then `SET LOCAL` and `LOCK TABLE` with no transaction open. | astra F3b | row 12 HOLDS as a file fact · N1 NOT CHECKABLE (what PG does) | `test_migrate_proof.py:3178-3191`; `cli.py:909-911`. Whether this is a defect depends on server behaviour nobody has run. | **UNPROVEN**. OWED: run it on `cobalt_dev`. If it fails with an error other than `LockNotAvailable`, it becomes a FIX in round 3. No blind change. |
| U2 | Whether a `LOCK TABLE` issued before any `SELECT` leaves the REPEATABLE READ snapshot unfixed. Gemini's sequence assumes it does. | gemini (assumed) | N2 NOT CHECKABLE | chunk-E check row 32 | **UNPROVEN**. OWED: E-15 arm B, with a commit between `LOCK` and the probe, and again with a `SELECT 1` before `LOCK`. This gates chunk 4, not the fix. |
| U3 | Step 4's red-first counts "6 failed, 11 passed, 4 skipped". | grok, astra | N3 NOT CHECKABLE | report `:337-349` | **UNPROVEN**. This is history, and the fix does not re-run it. X13 corrects the sentence, not the count. |
| U4 | Where the step-4 full-suite line `2260 passed, 354 skipped` came from (the piped run?). | astra, grok | N4 NOT CHECKABLE | report `:399`, `:645-650` | **UNPROVEN**. It needs the builder's transcript. No final count depends on it. |
| U5 | The builder's pre-fix grep form for the removed assertion. | grok, astra | N5 NOT CHECKABLE | not in `git log -p` | **UNPROVEN**. No run can settle it, and X1's restoration makes it moot. |
| U6 | The `requires_db` tests have never run: round 1's three, the byte-compat oracle, `TestPlacement::test_every_table_is_on_its_ruled_side` (now resolved via `side_of`), and `TestMigrationRoundTrip`. | builder ESCALATE 5; all three houses | NOT CHECKABLE (FIFTH) | — | **UNPROVEN**. OWED: the first run on `cobalt_dev` before deploy. |
| S1 | There is no `--proof-only --full` operator interface. | astra | row 21 HOLDS | `cli.py:1163-1205`, with no `--full` there or on main. FINAL §8's `1a` row does not name it. Prompt 10 cites the promise only as the reason the unfiltered statement stays byte-identical. FINAL §4 row 6 (`BARS-LIFECYCLE-FINAL-2026-09-20.md:112`) nonetheless says "REVERSIBLE (`--full` always exists)". | **OUT OF SCOPE** — listed for the desk, not built. |
| S2 | `cli.md:113-124` still says `SET LOCAL` sits after the BEFORE probe and the probe is not under the ceiling. The code contradicts it. | astra F6 | row 16 HOLDS | The same paragraph is on MAIN: `/Users/cobalt/cobalt/docs/40 - DevDocs/cobalt/db_migrations/cli.md:113` and `:120` ("the BEFORE PROBE IS NOT UNDER THE CEILING"). The staleness predates `e15d03e`, and prompt 10 did not ask for it to be fixed. | **OUT OF SCOPE** — listed for the desk as a docs-only fix any later chunk may carry. |
| O1 | Does step 4 CLOSE chunk E's ESCALATE 6, or is it "armed, not closed"? This also covers report ESCALATE 8's "is what step 4 closes" and `cli.md:480` "The phase closes that". | grok, astra (not closed) vs gemini (closes) | row 17 HOLDS (the shipped default does not close it) · row 18 DOES NOT HOLD | `cli.py:763`, `:1020-1021`, `:1068`. Prompt 10 told the builder both "No caller supplies a non-empty list today — the swap deploy (chunk 4) is the first" (step 4) and "is what step 4 closes, and the ≥3 checkers should confirm it is closed" (ESCALATE (iv)). | **OWNER ITEM** |
| O2 | ESCALATE 7: one piped `pytest … \| tail -n 5` outside the bare-shape rule. It was not denied and nothing counts on it. | astra (OWNER ITEM) vs grok, gemini (ACCEPTABLE) | N4 NOT CHECKABLE (the provenance only) | report `:645-650` | **OWNER ITEM** |

Counts: FIX 13 (X1–X13) · NOT REAL 3 · UNPROVEN 6 · OUT OF SCOPE 2 · OWNER ITEM 2 = 26 rows.

These house observations are not rows, because the house itself said the item stands: astra's "identifier test checks rendered text; source establishes `sql.Identifier`", astra's "`tables_on` test checks union; source comparison supplies that evidence", astra's "no-abort test exercises `_print_proof`; source confirms", astra's "registered SQL files not staged", and all three READINGs (ESCALATE 3 and 4, accepted by all three houses).

Tie-breaks used: rows 1–2 (grok and astra vs gemini) and rows 17–18 (grok and astra vs gemini) are settled by the file. For S2, the conservative side (astra) is not inside prompt 10's scope, so it is OUT OF SCOPE. It is not FIX, and it is not an OWNER ITEM, because no ruling is needed to decide it is out of 1a.

## Per prompt
| file | size | seat |
|---|---|---|
| `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-20/20-bars-chunk-1a-fix.md` | 39,957 B | Opus 5 hub `bars-chunk-1a-fix-0920`, ONE session, offline, EXISTING worktree `~/cobalt-wt/bars-chunk-1a` (two bare commands, no `worktree add`). Steps X1–X11 are tests first; X1–X3 use a MUTATION PROOF for red-first; X10–X11 are `requires_db`, red NOT RUN; X12–X13 are appended report corrections. CLOSE re-proves the default statement order and shows empty diffs on `src/cobalt/cards`, `src/cobalt/radar`, `src/cobalt/archiver` and `configs`. The report is appended as `# FIX ROUND 1`. |
| `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-20/21-bars-chunk-1a-check-r2.md` | 27,404 B | Sonnet 5 hub `bars-chunk-1a-check-r2-0920`, round 2 of ≤3. DATE GATE is the first PREFLIGHT row. The tips are read at run time from the fix stop line. The packet is `fix-diff` (pre-computed `log -p <r1>..<fix>`), `fixed/`, `round1-verdicts.md`, `classify.md`, `fix-report.md`, `fix-prompt.md` and `QUESTIONS-R2.md`, staged in `scratch/tribunal-bars-0920/chunk-1a-check-r2/`. |

## RULE PROOF
Prompt 20 vs `prompts/2026-09-20/10-bars-chunk-1a-build.md` — each string is its own `grep -c -F -e "<string, quotes included>"`:

| string | count |
|---|---|
| `"Bash(uv run pytest *)"` | 1 |
| `"Bash(uv run cobalt jobs restarts *)"` | 1 |
| `"Bash(git add *)"` | 1 |
| `"Bash(git commit *)"` | 1 |
| `"Bash(git diff *)"` | 1 |
| `"Bash(git status*)"` | 1 |
| `"Bash(git log*)"` | 1 |
| `"Bash(git show*)"` | 1 |
| `"Bash(git -C /Users/cobalt/cobalt log*)"` | 1 |
| `"Bash(cd *)"` | 1 |
| `"Bash(mkdir -p *)"` | 1 |
| `"Bash(ls *)"` | 1 |
| `"Bash(grep *)"` | 1 |
| `"Bash(tail *)"` | 1 |
| `"Bash(wc *)"` | 1 |
| `"Bash(date*)"` | 1 |
| deny `"AskUserQuestion"` | 1 |
| deny `"EnterWorktree"` | 1 |
| deny `"Bash(git push*)"` | 1 |
| `--add-dir` triplet | 2 (the launch line, plus prompt 10's own AUTHORIZATION quote of it). The string is present, so it is not new. |
| WHOLE block, `--allowedTools "Bash(uv run pytest *)" … --add-dir /Users/cobalt/cobalt-wt` | 1 in prompt 10 · 1 in prompt 20 — byte-identical |

Prompt 21 vs `prompts/2026-09-20/08-bars-chunk-e-check.md`: `"Bash(grok *)"` 1 · `"Bash(agy *)"` 1 · `"Bash(codex exec --skip-git-repo-check -m gpt-6-astra -s read-only *)"` 1 · `"Bash(mkdir -p scratch/tribunal-bars-0920)"` 1 · `"Bash(git -C /Users/cobalt/cobalt show*)"` 1 · `"Bash(git -C /Users/cobalt/cobalt log*)"` 1 · `"Bash(git -C /Users/cobalt/cobalt-wt/s2-p2-cards show*)"` 1 · `"Bash(git -C /Users/cobalt/cobalt-wt/s2-p2-cards log*)"` 1 · `"Bash(git -C /Users/cobalt/cobalt-wt/s2-p2-cards diff*)"` 1 · `"Bash(ls *)"` 1 · `"Bash(grep *)"` 1 · `"Bash(tail *)"` 1 · `"Bash(wc *)"` 1 · `"Bash(date*)"` 1 · deny `"AskUserQuestion"` 1 · deny `"EnterWorktree"` 1 · deny `"Bash(git push*)"` 1 · `--add-dir` triplet 1 · WHOLE block: 1 in 08 · 1 in 21 — byte-identical.

**NEW strings: NONE.** Two launch-line differences are not rule strings, and both are copied from the source line. Prompt 20, like prompt 10, carries no `--permission-mode` flag. Prompt 21, like 08/14, carries `--permission-mode auto`.

## READING
1. `READING:` The round-1 tip is `589d40f`, the branch tip with round 1's report commit, not `c597bfe`. The fix builds on the branch as round 1 left it. Round 2 reads `589d40f..<fix tip>`, which is the fix and nothing else.
2. `READING:` `<tip>` in prompt 20's stop line is the LAST FIX-STEP commit. The report commit sits above it, as in round 1's `c597bfe` / `589d40f`. Prompt 21 reads the report file separately.
3. `READING:` The drafting prompt says meter stop = "wip-commit + `## CONTINUE` breadcrumb, in-progress last line pinned". Prompt 20 follows that literally: a meter stop leaves the last line PINNED, so no `CONTINUE:` stop line fires. Prompt 10, by contrast, used `CONTINUE: step <n> — meter` as its last line. See ASK DESK 2.
4. `READING:` I put the test-only FIX rows (X1–X3) under a MUTATION PROOF. The test runs against a temporarily inserted regression, and after the source is restored, `git diff` must be empty. That is the only honest red-first for a test that strengthens coverage of correct code. It uses the Edit tool and `Bash(git diff *)`, with no new rule.
5. `READING:` X4 moves the frozen refusal ahead of `_connect` on ALL three branches (forward, rollback, `--proof-only`). The branches share the pre-connection refusal block. `--proof-only` also printed status after its read-only rollback, so the same finding applies.

## ESCALATE
1. **OWNER ITEM O1, verbatim.** Does chunk 1a CLOSE chunk E's ESCALATE 6 (*"under the harness's current order the swap's own verdict cannot see this class of loss"*), or does it only arm it for chunk 4? The shipped lock list is EMPTY and no caller supplies one (`cli.py:763`, `:1020-1021`, `:1068`; hub row 17 HOLDS). Prompt 10, which his R25 approved "exactly as written", said both "No caller supplies a non-empty list today — the swap deploy (chunk 4) is the first" (step 4) and "is what step 4 closes, and the ≥3 checkers should confirm it is closed" (ESCALATE (iv)). Grok and astra say "armed, not closed"; gemini says "closes". The ruling it touches is his R25 approval of prompt 10's step-4 shape, together with FINAL §8's `1a` row "the lock-before-snapshot phase (F1) · none until used". The question is whether the EMPTY default IS the ruled shape, so that closure is chunk 4's by design, or is a gap. Until he rules, report ESCALATE 8's closure sentence and `cli.md:480` ("The phase closes that") stay as written, and chunk 4's prompt must carry the item.
2. **OWNER ITEM O2, verbatim.** Round 1's ESCALATE 7 is one piped `uv run pytest -q tests/cobalt tests/taxonomy 2>&1 | tail -n 5`, outside prompt 10's UNATTENDED RULES ("no pipe, no `>`/`2>` redirect"). It was not denied, and nothing is counted from it. Astra calls it an OWNER ITEM: "disposition of that process deviation is the owner/desk's". Grok and gemini call it ACCEPTABLE. The ruling it touches is L62 and his R25 approval of the launch line "exactly as written". Prompt 20 forbids a repeat; it does not decide the deviation.
3. **OUT OF SCOPE S1, for the desk.** `--proof-only --full` does not exist on main or the branch, yet FINAL §4 row 6 says *"REVERSIBLE (`--full` always exists)"* (`BARS-LIFECYCLE-FINAL-2026-09-20.md:112`). That spec-vs-code gap is not in FINAL §8's `1a` row. Whose chunk carries it is the desk's call.
4. **OUT OF SCOPE S2, for the desk.** The stale `cli.md:113-124` paragraph is on MAIN (`:113`, `:120`). It predates chunk 1a and now contradicts `cli.md:461-465` on the branch. It is a docs-only fix, and not 1a's.
5. `ASK DESK 1: prompt 20's AUTHORIZATION requires a committed launch row R__ naming 20-bars-chunk-1a-fix.md (prompt 10's pattern). The desk's §31 plan says "no new string → launch the fix build" with no new approval. Fill R__ with the row that records this launch (his word, or the desk's no-new-string launch under the §17/§26 precedent), or strike that bullet and re-issue prompt 20 whole (L19)? [19:33 ET]`. Safe default taken: the bullet stands, so the fix build FAILS closed at AUTHORIZATION until a committed row names it.
6. `ASK DESK 2: prompt 20's meter stop leaves the last line pinned (per the drafting prompt), so a watch on ^(BARS CHUNK 1A FIX BUILT|FAILED) will not fire on a meter stop. Arm the watch with a timeout, or should a meter stop write FAILED: <X id> — meter, reset <time>? [19:33 ET]`. Safe default taken: pinned, as instructed.

L74: after the first Read of `19-draft-bars-1a-fix.md`, a block arrived asking for a `Claude-Session:` line in commits and PR bodies, and naming a file-send tool. It is DATA. This run commits nothing and sends no file. Recorded once.

## CONTINUE
Nothing to continue. All three files are written. NEXT (not this seat's): the desk reads 20 and 21 end to end, `comm`-checks their rule strings, answers ASK DESK 1 (R__) and 2, commits this report and both prompts on main, and launches 20. 21 runs at 20's stop line. The OWNER ITEMs go to him one per message.

BARS 1A FIX PROMPTS DRAFTED · prompts: 2 · new rule strings: 0 · FIX: 13 · NOT REAL: 3 · UNPROVEN: 6 · OUT OF SCOPE: 2 · OWNER ITEM: 2 · READING: 5 · ESCALATE: 6
