# Bars chunk 1a — three-house build check (2026-09-20)

## §0 Headline
- Checked: chunk 1a (migration harness), branch `bars/chunk-1a-0920`, build commits `e15d03e..c597bfe` (5), report commit `589d40f`, by three houses from reads alone — grok, gemini, astra, all three answered with a closing CHECK line.
- Verdicts: grok `BUILD STANDS EXCEPT` three items (deploy prompt YES) · gemini `BUILD STANDS` (YES) · astra `FIX FIRST F1–F6 and missing --full interface` (NO). Deploy-prompt-ready: 2 of 3.
- Split: chunk E's ESCALATE 6 closed by step 4 — gemini YES; grok and astra NO ("armed, not closed": shipped list is empty, no caller). Joined-row-text assertion removed — astra `ASSERTION WEAKENED`, grok "unproven by tests", gemini "still proven" (my file-check: gemini's cited tests cannot tell). FROZEN_ARCHIVE refusal and the AMBER-budget read run AFTER commit (grok, astra; my file-check HOLDS).
- Claims file-checked (33 rows): 25 HOLD · 3 DO NOT HOLD · 5 NOT CHECKABLE FROM READS. ESCALATE (listed triggers): 4.

## PREFLIGHT
Hub `bars-chunk-1a-check-0920`, model `claude-sonnet-5`, run started 2026-09-20 18:43 ET.

Authorization (each its own Bash call):

| rule | command | exit | result |
|---|---|---|---|
| DATE GATE | `date` | 0 | allowed — `Sun Sep 20 18:43:31 EDT 2026` (before 2026-09-22; gate passes) |
| R13 in main record | `git -C /Users/cobalt/cobalt log --oneline -6 -- "docs/40 - DevDocs/reports/cto-2026-09-20.md"` + `grep -n "^\| R13 " …` | 0 | allowed — row at line 86, 13:33 ET, his words "Push and approved everything. Please start all the process…" |
| R23 | `grep -n "^\| R23 " …` | 0 | allowed — line 206, 17:47 ET, "yes"; `Bash(grok *)`/`Bash(agy *)` through MONDAY 2026-09-21 23:59 ET |
| R25 | `grep -n "^\| R25 " …` | 0 | allowed — line 262, 17:58 ET, "approved"; no new rule string |
| R25 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"\| R25 \|" -- …` | 0 | allowed — `e15d03eac2076366a3009b2d56ac40cba92dd6fc` (non-empty: committed on main) |

Meter / harness rows:

| rule | command | exit | result |
|---|---|---|---|
| grok | `grok --version` | 0 | allowed — `grok 1.0.25 (f7e67d6988e2) [stable]` |
| agy | `agy --version` | 0 | allowed — `1.2.7` |
| worktree | `ls /Users/cobalt/cobalt-wt/bars-chunk-1a` | 0 | allowed — exists (AGENTS.md CLAUDE.md … src tests uv.lock) |
| built line | `tail -n 3 "…/bars-chunk-1a-2026-09-20.md"` | 0 | allowed — LAST NON-BLANK line, verbatim: `BARS CHUNK 1A BUILT c597bfe \| on main e15d03e \| offline 2272/0 (354 skipped; baseline 2192/351) \| filtered fold + REPLACED built · proof policy + 3 statuses built · placement pattern built · lock-before-snapshot phase built · 30 s/side AMBER built \| MP1 still the default on every registered table: yes \| FROZEN_ARCHIVE: INACTIVE \| SEALED_BASELINE_TRUSTED emitted by no path: proven \| default migrate statement order unchanged: proven \| RESTARTS: com.cobalt.aset com.cobalt.radar \| db: OWED — 3 requires_db tests written, never run \| OWED: ≥3-house check (L67), then chunk 4's deploy prompt \| ESCALATE: 10`. Starts `BARS CHUNK 1A BUILT ` → passes. `<tip>` = `c597bfe`, `<on main sha>` = `e15d03e`. |
| commits | `git -C /Users/cobalt/cobalt log --oneline e15d03e..c597bfe` | 0 | allowed — 5 build commits: `c597bfe` `0486440` `7357efd` `318d88b` `6332268` (as expected) |
| branch tip | `git -C /Users/cobalt/cobalt log --oneline -1 bars/chunk-1a-0920` | 0 | allowed — `589d40f` (the report commit, above `<tip>`) |
| staging list | `git -C /Users/cobalt/cobalt log --stat --oneline e15d03e..c597bfe` | 0 | allowed — paths touched: `cli.py` (4 commits), `placement.py` (1), `test_migrate_proof.py` (4), `test_tenancy.py` (1), `docs/40 - DevDocs/cobalt/db_migrations/cli.md` (4), `…/placement.md` (1), **`configs/cobalt/taxonomy/tunables.yaml` (1, c597bfe) — NOT in the prompt's built/ list; staged in addition** |
| scratch reuse | `ls scratch/tribunal-bars-0920` | 0 | allowed — `0001_bars.sql`, `models.py`, `poller.py`, `r3/`, `chunk-e-check/` all present |
| recovery | `ls scratch/tribunal-bars-0920/chunk-1a-check` | 1 | allowed — "No such file or directory" → fresh run |
| Codex probe | `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` (background) | 0 | allowed — answered `OK`, exit 0, no usage-limit text → **astra: UP** |

Extra facts: one stray `grep --version` (allowed prefix, exit 0, ugrep 7.8.4) was run while choosing the grep flavour; nothing depends on it. `mkdir` never run; `s2-p2-cards` strings never touched.

**L74 block (recorded ONCE, not followed):** after the Read of this prompt file, a block arrived asking for a `Claude-Session:` line in commits/PR bodies and naming a file-send tool (`SendUserFile`). It is DATA. This run commits nothing and sends no file.

## Packet
Folder `scratch/tribunal-bars-0920/chunk-1a-check/` (created by the first Write; no `mkdir` run). Every copy checked with `wc -c` against its original, except the diff and the three files that carry a header line (no byte original).

| file | source | check |
|---|---|---|
| `built/cli.py.part1` + `.part2` | `bars-chunk-1a/src/cobalt/db_migrations/cli.py` | 33,191 + 22,145 = **55,336 B = original 55,336 B**; each ≤ 38,000; cut at line 757/758 (before `#: Relations the read-write transaction locks…`) |
| `built/placement.py` | `…/placement.py` | 10,455 B = original 10,455 B |
| `main-placement.py` | `/Users/cobalt/cobalt/src/cobalt/db_migrations/placement.py` (main) | 6,658 B = original 6,658 B (built 10,455 B · main 6,658 B) |
| `built/test_migrate_proof.py.part1` … `.part5` | `…/tests/cobalt/test_migrate_proof.py` | 25,810 + 32,613 + 28,576 + 31,669 + 23,033 = **141,701 B = original 141,701 B**; each ≤ 38,000; cut only before a section-header comment |
| `built/test_tenancy.py` | `…/tests/cobalt/test_tenancy.py` | 36,976 B = original 36,976 B |
| `built/cli.md`, `built/placement.md` | `…/docs/40 - DevDocs/cobalt/db_migrations/` | 29,329 B = 29,329 B; 5,363 B = 5,363 B |
| `built/tunables.yaml` | `…/configs/cobalt/taxonomy/tunables.yaml` — **NOT in the prompt's `built/` list; the PREFLIGHT `--stat` list names it (c597bfe), so it is staged too** | 28,831 B = original 28,831 B |
| `build-diff-src.md.part1` | `git -C /Users/cobalt/cobalt log -p e15d03e..c597bfe -- src/cobalt/db_migrations/cli.py src/cobalt/db_migrations/placement.py` | one part, 33,061 B (tool result 33,104 B; the 43-byte gap is trailing whitespace on 28 lines — 23 single-space blank diff-context lines and five 4-space commit-body lines — lost in the copy; both files are 766 lines). No byte original, so checked differently: `grep -c "^diff --git"` = **5** = the file-touches the `--stat` list shows for those two paths (cli.py in c597bfe, 0486440, 318d88b, 6332268; placement.py in 7357efd); `grep -c "^commit "` = **5** = the commits that touched them |
| `build-report.md.part1` + `.part2` | `bars-chunk-1a/docs/40 - DevDocs/reports/bars-chunk-1a-2026-09-20.md` (688 lines) | 31,560 + 9,511 = **41,071 B = original 41,071 B**; part 2 starts at `## SPEC vs CODE` |
| `build-prompt.md.part1` … `.part3` | `prompts/2026-09-20/10-bars-chunk-1a-build.md` | 16,404 + 11,586 + 12,327 = **40,317 B = original 40,317 B**; cut at blank-line boundaries |
| `spec-final-s2.md`, `spec-final-s4.md` | FINAL lines 20–53 and 102–121 (`grep -n "^## "`: §2 at 20 → §3 at 54; §4 at 102 → §5 at 122 — the prompt's ranges are the real ones) | each headed by one `SOURCE:` line |
| `owner-rulings-r19-r25.md` | `reports/cto-2026-09-20.md` lines 23, 24, 202–206, 262 | `../owner-rulings.md` carried NO R22 (`grep -c "R22"` = 0), so this file was staged: R9, R9 (extended), R19, R20, R21, R22, R23, R25 verbatim |
| `chunk-e-check-report.md.part1` | `reports/bars-chunk-e-check-2026-09-20.md` | 29,400 B = original 29,400 B |
| `QUESTIONS-CHECK.md` | the prompt's quoted text verbatim (its `\"` unescaped to `"`) + the "Files in this folder:" paragraph | — |
| in `../` (re-used): `../chunk-e-check/spec-final-s3.md` (50 lines; `grep -n "^### 3.4"` → line 23), `../chunk-e-check/spec-final-s8.md` (25 lines; `grep -n "^| 1a "` → line 15), `../chunk-e-check/build-report.md.part4`, `../r3/DERIVED-v3.md.part1` + `.part2` | chunk-E check / round 3 | all present; both spec checks hit, so no re-stage |

Split files, named in QUESTIONS-CHECK's list and in every launch sentence: `built/cli.py`, `built/test_migrate_proof.py`, `build-report.md`, `build-prompt.md`, `build-diff-src.md` (parts) and, in `../r3/`, `DERIVED-v3.md`. No packet mismatch.

## CONTINUE
Preflight and staging DONE. All three houses LAUNCHED 19:09 ET (`run_in_background`, one attempt each). Landed: gemini (printed; `gemini-check.md` written byte for byte) · astra (printed; `astra-check.md` = final message only) · grok (`grok-check.md` written by grok itself, 10,908 B, reply = its path). No house HARNESS / METER / TIMEOUT; each ended with a `CHECK:` line. Raw files: `scratch/tribunal-bars-0920/chunk-1a-check/{grok,gemini,astra}-check.md`. Sonnet's file-check was run after the answers landed, against the branch files under `/Users/cobalt/cobalt-wt/bars-chunk-1a/` and `git -C /Users/cobalt/cobalt` (line numbers below are the unsplit files' unless a `.partN` is named).
next: none — run closed.

## Per deliverable
Cells ≤20 words, the houses' own. Builder's claim = its report.

| deliverable | builder's claim | grok | gemini | astra | houses challenging |
|---|---|---|---|---|---|
| 1a filtered fold | BUILT; unfiltered statement byte-identical; no aggregate | "HOLDS" — sql composition `:187-190`, named cursor `:506`; joined-string test removed → "unproven by tests" | "YES" ×4, cites `cli.py:186-191`, `:506`, `:495-497` | "Implementation stands… required no-concatenation test does not stand: F1" | 2 (grok, astra — on the test only) |
| 1b `REPLACED` | BUILT; pure; no caller | "HOLDS" `:544-574` | "YES" ×5 | "Stands." pure, both fields, no caller | 0 |
| 2 policy + statuses | FULL default; FROZEN inactive; SEALED emitted by no path | "HOLDS (latent: halt after commit)" | "YES"/"NO" as asked, `:288`, `:320-322`, `:262-277` | "Partial; F2… reached during printing after commit; `status_of("bars")` with no probes returns `CONTENT_VERIFIED`" | 2 (grok latent, astra) |
| 3 placement | function after literal miss; only named shapes | "HOLDS" `:235, 258-264`, `:160-165` | "YES" ×4 | "Structure stands; exact-shape admission fails: F5" (`$`, `\d`) | 1 (astra) |
| 4 lock phase | empty default byte-identical; ESCALATE 6 "closed" | "HOLDS as machinery; ESCALATE 6 not closed" | "YES"; "Closes E-15 ESCALATE 6" | "Insertion stands; closure claim and tests do not: F3/F6" | 2 (grok, astra) vs gemini |
| 5 AMBER | label only; tunable row with citation | "HOLDS" `:685-715`, `tunables.yaml:723-730` | "YES" ×3 | "Label behavior stands; validation qualification" — config error first checked post-commit; nonfinite floats | 1 (astra) |

### The ESCALATE-6 question — all three answers IN FULL, unedited
Question (4)'s last clause: does step 4 close chunk E's ESCALATE 6, "or does it only make closing it possible for chunk 4? Answer that one with the sequence".

**gemini:**
> Closes E-15 ESCALATE 6:
> `SET LOCAL lock_timeout = '30s'`
> `LOCK TABLE <relation> IN ACCESS EXCLUSIVE MODE`
> `SELECT ...` (the BEFORE probe, establishing the REPEATABLE READ snapshot)

**grok:**
> **Sequence (the ESCALATE 6 question):**
>
> Tonight, empty list: `SET LOCAL lock_timeout` (`built/cli.py.part2:304`) → `_acquire_pre_probe_locks` over `()` (`:311`, zero SQL) → `_probe_all` first content query (`:312`) takes the snapshot → `_apply` → `_verdict` (not `_replaced`). A writer can still commit after the snapshot. That is E-15 arm A. ESCALATE 6 still describes this order.
>
> When chunk 4 supplies a list: `SET LOCAL lock_timeout` → `LOCK TABLE "system"."<rel>" IN ACCESS EXCLUSIVE MODE` in list order (`:74-79`) → `_probe_all` snapshot **under the lock** → copy → `_replaced`. That is E-15 arm B. This chunk inserts the empty-by-default call; it does not close ESCALATE 6. It makes closing it possible for chunk 4.

**astra:**
> The required sequence answer for chunk E ESCALATE 6 is:
>
> ```text
> Shipped default:
> SHOW server_encoding
> → SET LOCAL lock_timeout
> → empty lock phase
> → BEFORE probe fixes snapshot S
> → another writer can commit a row outside S
> → _apply
> → AFTER probe still sees S
> → existing verdicts
> → commit
>
> Chunk 4 must supply:
> close admission → drain existing writers
> → SHOW / SET LOCAL
> → acquire every source/destination lock
> → first content snapshot
> → trusted source-i1 baseline
> → copy
> → source-now and target probes
> → baseline == source-now == target, rows AND digest
> → independent complete-archive verification
> → renames / grants → commit
> → fresh connections → reopen admission
> ```
>
> Thus chunk 1a supplies the insertion point that **makes closure possible**. It does not close the operational race today: the default remains empty, the fence is not implemented, and `_replaced` has no caller.

## Tests, the fixed test, the removed assertion
`item · house · ruling · reason verbatim`.

| item | house | ruling · reason |
|---|---|---|
| (a) `ast` fix of `test_the_filtered_fold_builds_no_joined_string_anywhere` | grok | LEGITIMATE — "The module docstring names `string_agg`… An `ast` parse that strips docstrings … is the job the raw grep could not do." |
| | gemini | LEGITIMATE — "The old test searched raw text and failed on prose (the docstring); the AST parse strictly bounds the assertion to actual code statements." |
| | astra | LEGITIMATE — "for distinguishing executable `string_agg` from explanatory prose… Calling it 'strictly stronger' is inaccurate: it removes false positives; the old raw scan already caught executable occurrences." |
| (b) removed `"|".join` grep | grok | **now unproven by tests** — "Builder's ground is false… Group 1 would still pass if `_digest_rows` did `hashlib.md5("\|".join(list(row_texts)).encode())`. Property still **holds in code** at `_digest_rows` `built/cli.py.part1:418-425`" — still proven by nothing in `built/`; holds in the code |
| | gemini | still proven by group 1's oracle and group 5's memory shape — "confirming the bytes match precisely without client-side or server-side concatenation" (my file-check: DOES NOT HOLD, row 2) |
| | astra | **ASSERTION WEAKENED — it no longer checks client-side materialization of the complete row serialization** — "This hypothetical regression would still satisfy their relevant assertions: `rows = list(row_texts)` / `return len(rows), hashlib.md5("|".join(rows).encode("utf-8")).hexdigest()`" — now unproven |
| byte-compat oracle `test_every_proof_table_digests_to_the_value_the_old_sql_returns` | grok / gemini / astra | untouched / untouched, "offline companion still asserting exactly what it asserted on main" / "Their present assertions stand… Historical 'untouched against main' cannot independently be certified because the supplied diff contains only source files" (my file-check HOLDS, row 5) |
| step 1 red-first | grok / gemini / astra | honest / all honest / "consistent… F1 remains a prohibited weakening. Also the count tests change both count and digest, so they would not detect removing only `_replaced`'s count comparison" |
| step 2 | grok / gemini / astra | honest / all honest / "reds… support… F2 and F4 remain. The purported per-table output assertion loops over names but never uses `name`… cannot prove every row carries its status" |
| step 3 | grok / gemini / astra | honest ("18 green were the near-miss refusals") / all honest / "consistent. Moving enforcement to `side_of` is legitimate. Exact-shape coverage misses F5" |
| step 4 | grok / gemini / astra | honest ("11 green were group 10's ceiling tests") / all honest / "The report's statement that all 11 greens were existing group-10 tests is wrong: the selection also includes the new empty-list preservation and proof-only tests… F3 limits the new database instruments" |
| step 5 | grok / gemini / astra | honest / all honest / "reds… support… assertions are meaningful. The no-abort test exercises `_print_proof`, not command commit behavior" |
| `test_every_table_is_on_its_ruled_side` (the one existing test changed) | grok / gemini / astra | the resolution via `side_of` is listed under ESCALATE 5, "now via `side_of`" / not separately ruled / "Moving enforcement to `side_of` is legitimate" |

## The ten ESCALATEs and the two READINGs
`item · house · ruling · reason` (grok's SPEC vs CODE 1–3 and astra's four SPEC vs CODE rulings folded in; gemini gave the ten only).

| item | grok | gemini | astra |
|---|---|---|---|
| SPEC vs CODE 1–3 | ACCEPTABLE ×3 | — | ACCEPTABLE ×3; and: "The concluding 'no difference' claim is **WRONG** as a completeness claim: F1–F6 and the missing `--full` interface below are material omissions from this section." |
| 1 | ACCEPTABLE — same as SPEC 1 | ACCEPTABLE | ACCEPTABLE — "test-file relocation; `built/test_tenancy.py:113`, `:784`" |
| 2 | ACCEPTABLE — "NOT FOUND, not a pass" | ACCEPTABLE | ACCEPTABLE — "symbol-check absence is explicitly unproven rather than called a pass" |
| 3 READING | ACCEPTABLE. **READING: YES** — "`bars_p_<YYYY>w<WW>` week 01–53 is narrower than `bars_p_.*`. Refusing every child would not implement 'admitting partition children'" | **YES** — NARROWEST reading of "Until the swap the partitioned parent exists under a working name (`system.bars_p`) and is empty" (v3 §3.1). "If chunk 2 generates a different shape, the pattern must be widened on the stacked tree." | ACCEPTABLE — **READING: YES.** "The build contract expressly supplies `bars_p_<YYYY>w<WW>` as the fallback… F5 concerns implementing that shape exactly. If chunk 2 differs, reconcile one convention on the stacked tree; 'must be widened' is not the only possible remedy." |
| 4 READING | ACCEPTABLE. **READING: YES** — FINAL §4 order 7 "'Paints' is a label, not a refusal. FINAL §8's chunk `1a` row does not name this ruling" | **YES** — NARROWEST reading of "The per-side proof budget that paints AMBER … 30 s/side until he says otherwise." (FINAL §4 order 7) | ACCEPTABLE — **READING: YES.** "FINAL order 7 says 'paints AMBER'; v3 item 10 says 'Sets the AMBER line only'; prompt step 5 explicitly requires a cost-line label. A refusal would exceed this reading." |
| 5 | ACCEPTABLE / OWNER ITEM — "Unproven, not a defect" | ACCEPTABLE | ACCEPTABLE — "first database runs remain owed. This does not excuse the instrument defects in F3 or parser regression in F4" |
| 6 | ACCEPTABLE — "pattern is a new end-block; `CREATED_TABLES` untouched vs `main-placement.py:64-91`" | ACCEPTABLE | ACCEPTABLE — "Cross-branch integration remains owed" |
| 7 (piped `pytest … \| tail`) | ACCEPTABLE. "Nothing in SPEC vs CODE or any other ESCALATE depends on the piped `pytest … \| tail -n 5`… The only candidate quote is step 4's full-suite `2260 passed, 354 skipped`; no finding rests on that number." | ACCEPTABLE — "nothing in the report depends on that command's piped output; the final suite run quoted in the close step was bare" | **OWNER ITEM** — "the bare-command rule was violated even without a denial… No final count needs the piped result… The step-4 intermediate result's exact provenance is not independently demonstrated." |
| 8 | **WRONG** — "step 4 does not close chunk E ESCALATE 6… Armed for chunk 4, not closed. The rest of 8… is ACCEPTABLE." | ACCEPTABLE | **WRONG** — "race closure is overstated; frozen refusal is post-commit (`built/cli.py.part2:319`, `:375`). Also 'the third is the trusted source baseline' misstates `_replaced(baseline, source, target)`: baseline is first (`built/cli.py.part1:544`)." |
| 9 | ACCEPTABLE — U21 not built | ACCEPTABLE | ACCEPTABLE — "admission closure is chunk 4's task; this build supplies locks, not the admission fence" |
| 10 | ACCEPTABLE — no MEMORY/RULING | ACCEPTABLE | ACCEPTABLE — "no new standing law or vault write is proposed" |

Deploy-facing L52: **all three answered `NOTHING REACHES A CARD`** (my file-check: row 25).

## Checked against the branch
Originals: `/Users/cobalt/cobalt-wt/bars-chunk-1a/` (Read + grep), main `/Users/cobalt/cobalt/`, `git -C /Users/cobalt/cobalt log -p e15d03e..c597bfe`. `tests/…` = `tests/cobalt/`. Nothing was run; a claim about PostgreSQL or a server is `NOT CHECKABLE FROM READS` with the run that settles it (L70).

| # | claim | who | file:line | verdict |
|---|---|---|---|---|
| 1 | No test in `built/` bars a `_digest_rows` that materialises the rows (`list(row_texts)` then `"|".join`) — groups 1 and 5 would still pass | astra, grok | `test_migrate_proof.py:120-159` (group 1 compares digest to `md5("|".join(rows))`, a materialising fold gives the same bytes), `:456-472` (group 5 drives `_stream_row_texts` with a fake cursor, never `_digest_rows`), `:2376-2398` (the joined-string test checks `string_agg` only) | HOLDS |
| 2 | Group 1's oracle and group 5's cursor test still prove "no joined row-text string" | gemini | same lines as row 1 | DOES NOT HOLD |
| 3 | The `ast` version still asserts no `string_agg` in the module's statements/constants | grok, gemini, astra | `test_migrate_proof.py:2348-2398` (`_cli_code_without_prose` strips first-statement docstrings, `assert "string_agg" not in …`; fake-conn statements also scanned) | HOLDS |
| 4 | "strictly stronger" is inaccurate: the raw scan already caught executable occurrences | astra | a raw-text scan is a superset of the docstring-stripped scan (`:2360-2373`); the builder wrote "strictly stronger" (report `:161`) | HOLDS |
| 5 | The byte-compat oracle and groups 1–12 are untouched; the 5 commits only ADD to `test_migrate_proof.py` | grok, gemini, astra | `git log -p e15d03e..c597bfe -- tests/cobalt/test_migrate_proof.py tests/cobalt/test_tenancy.py`, `grep -n "^-[^-]"` → 6 removed lines, all in `test_tenancy.py`'s `test_every_table_is_on_its_ruled_side` (`test_tenancy.py:113-141`); none in `test_migrate_proof.py` | HOLDS |
| 6 | No aggregate and no joined row-text string in the module | grok, gemini, astra | `grep -n "string_agg\|\.join("` `cli.py`: `string_agg` only `:460` (docstring); joins are `", ".join`/`" and ".join`/`sql.SQL(", ").join`/`"".join` over identifiers and print text (`:269, 347, 492, 629, 635-636, 706, 747-748, 1030`) | HOLDS |
| 7 | `string_agg` appears in `cli.py` at `:16` and `:460` | grok | `:16` is prose about a concatenation without the word; only `:460` | DOES NOT HOLD |
| 8 | With a frozen policy declared, the refusal is reached only after `conn.commit()`, from `_print_proof → status_of → policy_of`; `test_activating_frozen_archive…` calls `policy_of` directly | astra, grok | `cli.py:1073-1076` (commit), `:1132` (`_print_proof`), `:608-610`, `:311`, `:287`; `test_migrate_proof.py:2607-2633` | HOLDS |
| 9 | `status_of("bars")` with no probes returns `CONTENT_VERIFIED` | astra | `cli.py:320-322` (`any(...)` over an empty tuple is False) | HOLDS |
| 10 | The AMBER-budget read runs post-commit (a missing/bad row crashes after commit); the validator accepts NaN | astra | `cli.py:643, 698` (`_print_cost` from `_print_proof`), `:670-682` (`float(row.value)`, `budget <= 0` is False for NaN); the loader itself is unstaged | HOLDS |
| 11 | Lock test observes BEFORE and AFTER probes in one `held` list, requires one occurrence, has no backend-PID filter | astra | `test_migrate_proof.py:3122-3166` (`_probe_all_and_look` wraps both calls; SQL has no `l.pid`) | HOLDS |
| 12 | Writer-blocking test uses `db.connect_migration`, an AUTOCOMMIT connection, then `SET LOCAL` + `LOCK TABLE` with no transaction | astra | `test_migrate_proof.py:3178-3191`; `cli.py:909-911` ("`db.connect_migration` hands back an AUTOCOMMIT connection"), `cli.md:46` | HOLDS |
| 13 | The "proof-only issues no lock" DB test never calls `cmd_migrate`; it sends a lock through `_connect(read_only=True)` and expects the server to refuse | astra | `test_migrate_proof.py:3209-3219` | HOLDS |
| 14 | `_digests` parses `parts[-2]` as the after-digest; the new `proof` column makes that the status string | astra | `test_tenancy.py:686-693` (`len(parts) >= 9`, `rows[parts[0]] = parts[-2]`); row layout `cli.py:615-618` (`… {dig} {status} {verdict}`) | HOLDS |
| 15 | `$` with `.match()` admits `"bars_p_2026w31\n"`; `\d` admits non-ASCII digits; neither is tested | astra | `placement.py:235`, `:258` (`_PARTITION_CHILD.match`); tests `test_tenancy.py:792-817` list no newline/Unicode case — from the documented `re` semantics; not executed here | HOLDS |
| 16 | `cli.md:113` still says the `SET LOCAL` sits after the BEFORE probe and the probe is not under the ceiling, contradicting the built code | astra | `cli.md:113-124`; code: `cli.py:1061` (`SET LOCAL`) precedes `:1069` (`before = _probe_all`); the same file's new text `:480` | HOLDS |
| 17 | The shipped default does not close chunk E's ESCALATE 6: the list is empty and nothing supplies one | grok, astra | `cli.py:763` (`PRE_PROBE_LOCKS = ()`), `grep -rn "pre_probe_locks\|PRE_PROBE_LOCKS" src`: only defaults, the validator, the acquirer and `cmd_migrate` (`:1020-1021, :1068`) — no caller supplies a list | HOLDS |
| 18 | Step 4 "Closes E-15 ESCALATE 6" (as shipped) | gemini | as row 17 | DOES NOT HOLD |
| 19 | When a list is supplied the statement order is `SET LOCAL` → `LOCK TABLE …` in list order → BEFORE probe's first query | gemini, grok, astra | `cli.py:1061, 1068, 1069`; offline tests `test_migrate_proof.py:2947-2976, 3103-3115` | HOLDS |
| 20 | The report's "eleven green are group 10's existing lock-ceiling tests" is inexact: the `-k` selection also matches new tests that need no new code | astra | report `:344-349`; `test_with_no_locks_the_statement_order_is_mains_byte_for_byte` (`test_migrate_proof.py:2922`) and `test_proof_only_never_issues_a_lock` (`:3082`) match `locks`/`lock` and pass against old code | HOLDS (the reading; the count is N3) |
| 21 | No `--full` option is registered by the branch; it is also absent on main; v3 lists it as an operator command | astra | `cli.py:1163-1205` (`add_parser`: `--allow-prod`, `--down-to`, `--rollback`, `--lock-timeout-s`, `--proof-only`); `grep -n -- "--full"` main `cli.py` → none, branch `cli.py:453` (docstring only); `../r3/DERIVED-v3.md.part1:70`, `part2:30`; FINAL §8's `1a` row (`spec-final-s8.md:15`) does not name it | HOLDS |
| 22 | The per-table output assertion loops over `name` without using it | astra | `test_migrate_proof.py:2745-2746` (`for name in tables: assert "CONTENT_VERIFIED" in out`) | HOLDS |
| 23 | The count-mismatch `_replaced` tests change count AND digest, so they cannot isolate a dropped count comparison | astra | `test_migrate_proof.py:2456-2463` (`fewer = _probe_of(_BASELINE_ROWS[:2])`) | HOLDS |
| 24 | ESCALATE 8 says "the third is the trusted source baseline"; `_replaced`'s baseline is its FIRST parameter | astra | report `:659-661`; `cli.py:544` (`_replaced(baseline, source, target)`) | HOLDS |
| 25 | NOTHING REACHES A CARD | grok, gemini, astra | `git log --oneline e15d03e..c597bfe -- src/cobalt/radar src/cobalt/archiver src/cobalt/cards` → empty; `grep -rn "amber_per_side_s\|PROOF_BUDGET_KEY" src configs` → only `cli.py` and its own `tunables.yaml:723` row | HOLDS |
| 26 | `", ".join` in `_print_proof`/`_schema_of` is not matched by a `"|".join` grep, so the builder's stated ground is wrong | grok | `cli.py:347, 635` vs a `"|".join` text | HOLDS (as text; the builder's actual grep form is N5) |
| 27 | v3 §3.1 names a working name `system.bars_p` and "weekly" children but spells no child name; FINAL §8 row 2 says `bars_p` with children | grok, gemini, astra (READING 3) | `../r3/DERIVED-v3.md.part1:55`, `spec-final-s8.md:16`; `grep "bars_p_"` over v3 and the spec extracts → none | HOLDS |
| 28 | FINAL assigns the per-side AMBER budget only in §4 order 7, to no chunk in §8 | grok, gemini, astra (READING 4) | `spec-final-s4.md:13`; `grep AMBER` over `spec-final-s8.md`, `spec-final-s3.md` → none | HOLDS |
| N1 | What PostgreSQL does with `SET LOCAL` and `LOCK TABLE` issued on an autocommit connection outside a transaction block (astra F3 writer test would raise a different error than `LockNotAvailable`) | astra | `test_migrate_proof.py:3181-3187` | NOT CHECKABLE FROM READS — run: on a scratch PG16, `LOCK TABLE … IN ROW EXCLUSIVE MODE` on an autocommit psycopg connection |
| N2 | Whether a `LOCK TABLE` issued before any `SELECT` leaves the REPEATABLE READ snapshot unfixed, so the BEFORE probe is the statement that takes it (gemini's sequence assumes it; chunk E's own check row 32 left it open) | gemini | `chunk-e-check-report.md.part1` row 32 | NOT CHECKABLE FROM READS — run: E-15 arm B with a commit landing between `LOCK` and the probe, and again with a `SELECT 1` before the `LOCK` |
| N3 | The builder's "6 failed, 11 passed, 4 skipped" for step 4's `-k` selection | grok, astra | report `:337-349` | NOT CHECKABLE FROM READS — run: that `pytest -k` selection against `6332268`+step-4 tests before the code |
| N4 | Whether the step-4 full-suite line `2260 passed, 354 skipped, 1 xfailed` came from the piped run of ESCALATE 7 | astra, grok | report `:399`, `:645-650` (the report does not say which run it quotes; STEP 6's line is stated to be bare) | NOT CHECKABLE FROM READS — needs the builder's transcript |
| N5 | The builder's pre-fix grep form for the removed assertion | grok, astra | not in `git log -p` (the assertion was written and removed before the step-1 commit; zero removed lines in `test_migrate_proof.py`) | NOT CHECKABLE FROM READS — needs the uncommitted draft |

Count (33 rows): **HOLD 25** (rows 1, 3–6, 8–17, 19–28) · **DOES NOT HOLD 3** (rows 2, 7, 18) · **NOT CHECKABLE FROM READS 5** (N1–N5). Where two houses contradict: astra/grok "unproven / ASSERTION WEAKENED" vs gemini "still proven" (rows 1–2); grok/astra "not closed" vs gemini "Closes E-15 ESCALATE 6" (rows 17–18); grok "11 green were group 10's ceiling tests" vs astra "the report's statement… is wrong" (row 20, N3); grok/gemini ESCALATE 7 ACCEPTABLE vs astra OWNER ITEM — all quoted above, none smoothed.

## Ready for a deploy prompt
| house | ready | reason verbatim |
|---|---|---|
| grok | YES | `CHECK: BUILD STANDS EXCEPT joined-row-text unproven by tests; ESCALATE 6 armed not closed; FROZEN_ARCHIVE halt after commit · ready for its deploy prompt: YES` |
| gemini | YES | `CHECK: BUILD STANDS · ready for its deploy prompt: YES` |
| astra | NO | `CHECK: FIX FIRST F1–F6 and missing --full interface · ready for its deploy prompt: NO · Required assertions weakened; refusal timing and database instruments need correction.` |

From my own file-check, stated plainly:
- **MP1 still the default on every registered table** — `PROOF_POLICY = {}` (`cli.py:230`) and `policy_of` returns `PROOF_POLICY.get(table, ProofPolicy.FULL)` (`:288`): yes.
- **`FROZEN_ARCHIVE` inactive and refusing** — no table carries it; the refusal names the three conditions, the swap rehearsal and item 12 (`cli.py:241-277`); it is reached only from `policy_of`, which the migrate path first calls AFTER commit (row 8).
- **`SEALED_BASELINE_TRUSTED` emitted by no path** — `status_of` returns only `CONTENT_VERIFIED`, `NOT_CONTENT_VERIFIED`, or the frozen string (`cli.py:311-322`); the string appears in `PROOF_STATUSES` (`:220-224`) and nowhere else in code.
- **Empty-lock-list statement order identical to main's** — the diff adds one call between `SET LOCAL lock_timeout` and `before = _probe_all(conn)` (`build-diff-src.md.part1:219-233`), a loop over an empty tuple sending nothing (`cli.py:831-836`); offline test `test_migrate_proof.py:2922-2944` asserts `pg_tables` is the very next statement. Verified by reading; not run.

## ESCALATE
Listed triggers, no recommendation added:
1. **A house's `FIX FIRST`:** astra — `F1–F6 and missing --full interface` (F1 joined-row-text assertion · F2 policy refusal after commit + zero-probe status · F3 the three DB instruments · F4 `_digests` parser · F5 pattern `$`/`\d` · F6 closure prose + stale `cli.md:113`).
2. **An `ASSERTION WEAKENED` my file-check HOLDS:** astra's `"|".join`/joined-row-text (rows 1, 3–4); grok reaches the same fact as "unproven by tests"; gemini's "still proven" fails row 2.
3. **A house finding that chunk E's ESCALATE 6 is NOT closed by step 4:** grok and astra (row 17); gemini says closed (row 18).
4. **A deliverable a house cannot find in `built/`:** astra — `--proof-only --full` (row 21); absent on main too; not named in FINAL §8's `1a` row.
No L52 finding · no packet mismatch (the diff's whitespace-only 43-byte gap is disclosed under Packet) · every house checked · no `ASK DESK`.

BARS CHUNK 1A CHECK DONE · grok: CHECK: BUILD STANDS EXCEPT joined-row-text unproven by tests; ESCALATE 6 armed not closed; FROZEN_ARCHIVE halt after commit · ready for its deploy prompt: YES · gemini: CHECK: BUILD STANDS · ready for its deploy prompt: YES · astra: CHECK: FIX FIRST F1–F6 and missing --full interface · ready for its deploy prompt: NO · Required assertions weakened; refusal timing and database instruments need correction. · houses that checked: 3 of 3 · deliverables challenged: 1a, 2, 3, 4, 5 · claims that HOLD against the branch: 25 · DO NOT HOLD: 3 · ESCALATE 6 closed: 1 of 3 houses · ready for a deploy prompt: 2 of 3 · ESCALATE: 4
