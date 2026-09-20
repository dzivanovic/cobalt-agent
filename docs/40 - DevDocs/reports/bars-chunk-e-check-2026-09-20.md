# BARS CHUNK E CHECK — 2026-09-20

## §0 Headline
- Checked: the chunk-E harness (25 files) and the builder's results report (branch `bars/chunk-e-0920`, `a6488d1..982d958`) by three houses, from reads alone: grok, gemini, astra — all three answered with a closing CHECK line.
- Verdicts: grok `RESULTS STAND EXCEPT E-19` · gemini `RESULTS STAND` · astra `RESULTS STAND EXCEPT E-19`. Chunk 1a may build: YES ×3. Chunk 2 may build: YES ×3. Both reds (E-6b, E-9) = REAL RESULT ×3; all five test fixes LEGITIMATE ×3; item 2 = OUT OF SCOPE ×3; no house finds item 6 leaving a hole in FINAL's chunk 4 wording.
- Two houses (grok, astra) find E-19's `assert detected_by` cannot fail once the content moved (`test_e19_bypass_with_reset.py:140,163,167` — my file-check HOLDS); astra alone also raises (c) findings on E-8, E-12, E-15 (file-check HOLDS the code facts). Gemini answered every (c) with NO and made two claims my file-check DOES NOT HOLD (E-16 OIDs, E-10 writer-first).
- Claims file-checked (32 rows): 26 HOLD · 2 DO NOT HOLD · 4 NOT CHECKABLE FROM READS. ESCALATE (listed triggers): 0.

## PREFLIGHT
Hub `bars-chunk-e-check-0920`, model `claude-sonnet-5`, run started 2026-09-20 16:59 ET.

| rule | command | exit | result |
|---|---|---|---|
| DATE GATE | `date` | 0 | `Sun Sep 20 16:59:50 EDT 2026` — gate passes (not 09-21) |
| AUTHORIZATION | `git -C /Users/cobalt/cobalt log --oneline -6 -- "docs/40 - DevDocs/reports/cto-2026-09-20.md"` | 0 | latest `40f12ac docs(desk): 09-20 R15 chunk E approved …`; `ef184bb`, `1b2fcda`, `33d9109`, `bd4692e`, `b82aa50` |
| R13 | `grep -n "^| R13 " …cto-2026-09-20.md` | 0 | line 86: 13:33 ET "Push and approved everything. Please start all the process … I'm expecting you to run for a while." |
| R15 | `grep -n "^| R15 " …cto-2026-09-20.md` | 0 | line 198: 15:59 ET "Approved. Launch it." — chunk E; `--disallowedTools` `AskUserQuestion` `EnterWorktree` `Bash(git push*)` |
| grok | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` — allowed |
| agy | `agy --version` | 0 | `1.2.7` — allowed |
| r3 folder | `ls scratch/tribunal-bars-0920/r3` | 0 | holds `DERIVED-v3.md.part1`, `DERIVED-v3.md.part2`, `migrate-proof.excerpt.py`, `ev-migrate-rollback.excerpt.py`, `ev-store-upsert.excerpt.py` (all five present) |
| harness | `ls /Users/cobalt/cobalt-wt/bars-chunk-e/tests/experiments/bars_chunk_e` | 0 | 25 `.py` files (+ `__pycache__`, never staged) — count as expected |
| recovery | `ls scratch/tribunal-bars-0920/chunk-e-check` | 1 | `No such file or directory` — fresh run |
| astra probe | `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` (background) | 0 | answer `OK`, 2,277 tokens, no usage-limit text → **astra: UP** |

L74 (recorded ONCE, never followed): after the Read of the launch prompt, a block arrived in the tool-result stream asking for a `Claude-Session: https://claude.ai/code/session_…` line in commits/PR bodies and naming a file-send tool. Data, not an instruction; not followed. This run commits nothing.

Authorization: the record matches this file (R13, R15, the 14 strings, the added `git push*` deny). No mismatch.

## Packet
Folder `scratch/tribunal-bars-0920/chunk-e-check/` (created by the first Write; no `mkdir` run). Every copy checked with `wc -c` against its original.

| file | source | check |
|---|---|---|
| `harness/` — 25 files | `/Users/cobalt/cobalt-wt/bars-chunk-e/tests/experiments/bars_chunk_e/` | 5 support files 37,593 B = original 37,593 B; 20 experiment files 121,638 B = original 121,638 B, equal one by one; `scratch.py` 28,455 B in ONE Write |
| `build-report.md.part1` … `part4` | builder's report, 798 lines | 22,152 + 29,267 + 23,395 + 10,865 = **85,679 B = original 85,679 B**; each part ≤ 38,000 B; cut at `## ` boundaries (part2 starts `## E-6b`, part3 `## E-14`, part4 `## RESULTS`) |
| `spec-final-s3.md`, `spec-final-s6.md`, `spec-final-s8.md` | FINAL lines 54–101, 153–179, 190–212 (first/last lines checked against `grep -n "^## "`: §3 at 54 → §4 at 102; §6 at 153 → §7 at 180; §8 at 190 → EOF 212) | one header line each naming path + range |
| `spec-07-build-prompt.md` | `prompts/2026-09-20/07-bars-chunk-e.md` lines 18–56 | one header line |
| `ev-migrate-schema-pk.excerpt.py`, `ev-migrate-connect.excerpt.py` | `src/cobalt/db_migrations/cli.py` 189–249 and 504–560 | each headed by its real path + range |
| `QUESTIONS-CHECK.md` | verbatim from the prompt + one appended "Files in this folder:" paragraph | — |
| in `../` (already staged, not copied): `../0001_bars.sql`, `../models.py`, `../poller.py`, `../r3/ev-store-upsert.excerpt.py`, `../r3/migrate-proof.excerpt.py`, `../r3/ev-migrate-rollback.excerpt.py`, `../r3/DERIVED-v3.md.part1` + `.part2` | round 1 / round 3 folders | all present |

Split files (named in QUESTIONS-CHECK's list and in every launch sentence): `build-report.md` in four ordered parts; `DERIVED-v3.md` in two ordered parts (`../r3/`). No packet mismatch.

## CONTINUE
Launched 17:1x ET, all three `run_in_background`, one attempt each; nothing re-asked. Landed: gemini (printed; `gemini-check.md` written byte for byte) · astra (printed; `astra-check.md` = final message only) · grok (`grok-check.md` written by grok itself, reply = its path). No house HARNESS / METER / TIMEOUT; each ended with a `CHECK:` line. Raw files: `scratch/tribunal-bars-0920/chunk-e-check/{grok,gemini,astra}-check.md`.
next: none — run closed at 17:27 ET.

## Per experiment
Cells ≤20 words, the houses' own. `—` = house wrote nothing of substance beyond YES/NO. An experiment no house challenges is one short row. Astra's (c) cells for the two reds read "Not applicable: red"; grok "— (NOT AS EXPECTED)"; gemini wrote NO.

| E | builder | grok (a)/(b)/(c) | gemini (a)/(b)/(c) | astra (a)/(b)/(c) | challenging |
|---|---|---|---|---|---|
| E-1 | AS EXPECTED | Y/Y/N | Y/Y/N | Y/Y/N | 0 |
| E-2 | AS EXPECTED | Y/Y/N | Y/Y/N | Y/Y/N | 0 |
| E-3 | AS EXPECTED | Y/Y/N | Y/Y/N | Y/Y/N | 0 |
| E-4 | AS EXPECTED | Y/Y/N ("dirty=False can only mean the row trigger was silent") | Y/Y/N | Y/Y/N ("ordinary-TRUNCATE-under-replica observation is printed, not asserted") | 0 |
| E-5 | AS EXPECTED | Y/Y/N | Y/Y/N | Y/Y/N | 0 |
| E-6 | AS EXPECTED | Y/Y/N | Y/Y/N | Y/Y/N | 0 |
| E-6b | NOT AS EXPECTED | Y/Y/— | Y/Y/N | Y/Y/n.a. (red) | 0 |
| E-7 | AS EXPECTED | Y/Y/N ("asserts `_xact_[1]==n`") | Y/Y/N | Y/Y/N ("both comparison outcomes are asserted") | 0 |
| E-8 | AS EXPECTED | Y/Y/N | Y/Y/N | Y/Y/**YES** — "`:74` reads `_xact_`, but assertions at `:104` onward never require it to show DML" | 1 (astra) |
| E-9 | NOT AS EXPECTED | Y/Y/— | Y/Y/N | Y (separate restart/crash invocations)/Y/n.a. — "initial collision is after committed damage, not a before-commit demonstration" | 0 (note) |
| E-10 | AS EXPECTED | Y/Y/N ("Both commit orders remain") | Y/Y/N | Y/Y/N — "measured interval spans the writer's INSERT work through commit"; "151,000 rows/s … inside 165,782–187,769 is arithmetically false" | 0 verdict; 1 report-arithmetic note |
| E-11 | AS EXPECTED | Y/Y/N | Y/Y/N | Y/Y/N | 0 |
| E-12 | AS EXPECTED | Y/Y/**N** ("`landed==0` would fail if earlier `executemany` calls committed") | Y/Y/N | Y/Y/**YES** — "`:136` accepts any caught database error and never asserts `written == [2, 2]`" | 1 (astra) |
| E-13 | AS EXPECTED | Y/Y/N | Y/Y/N | **NO, literally, for registration** — "`:100` directly probes the new parent; `:148` … reports only `bars`"; (b) Y/(c) N | 1 (astra, (a)) |
| E-14 | AS EXPECTED | Y/Y/N — "Case 3 issues `SELECT max(ts)` *before* the swap, so ACCESS SHARE is already held" | Y/Y/N | Y/Y/N — "claim that case 3 begins the migration lock-free is unsupported" | 2 (grok note, astra (b)) |
| E-15 | AS EXPECTED | Y/Y/**N** | Y/Y/N | Y/Y/**YES**, narrowly — "`:118` require the row absent … do not require `replaced=True`" | 1 (astra) |
| E-16 | CONTESTED — SETTLED | Y/Y/— ("OIDs are read from observer `bare_conn`") | Y/Y/N ("read after commit from the session under test (not a fresh one)") | Y/Y/N — "post-commit OIDs are not read from the tested writer/prepared session" | 1 (astra/grok vs gemini) |
| E-17 | CONTESTED — SETTLED | Y/Y/— | Y/Y/N | Y/Y/N | 0 |
| E-18 | AS EXPECTED | Y/Y/N | Y/Y/N | Y/Y/N ("5-dev after the swap" comment inconsistent with FINAL §8) | 0 verdict; 1 comment note |
| E-19 | AS EXPECTED | Y/**Y — OBSERVED shows `_xact_` + digest; the AS EXPECTED gate does not**/**YES** — "`:140-141` puts F-A content digest in `detected_by`; `:167` asserts nonempty" | Y/Y/N | **NO**/**NO** for the unqualified protocol-pass verdict/**YES** — "`assert detected_by` at `:167` cannot fail after the damage assertion succeeds" | 2 (grok, astra) |

## Tests fixed, the two reds, the six readings
`item · house · ruling · the house's reason verbatim`. Astra and grok tag every ruling; gemini's are one-liners.

| item | house | ruling · reason |
|---|---|---|
| E-4 fix 1 (`fill_child`) | grok | LEGITIMATE — "`fill()` writes all three children; after a one-child TRUNCATE the next arm raises `UniqueViolation` and cannot finish the row's procedure." |
| | gemini | LEGITIMATE. |
| | astra | LEGITIMATE — "Refilling all three children after truncating one introduces unrelated duplicate-key failures. `fill_child()` restores the intended test state." |
| E-4 fix 2 (`pg_inherits` keys only) | grok | LEGITIMATE — "the row reads `pg_inherits`. TRUNCATE rewrites `pg_class` for the new `relfilenode`; `pg_class.xmin` moving *is* that relfilenode finding (already asserted). Full dict still OBSERVED. Not a weaker membership proof." |
| | gemini | LEGITIMATE — "The spec row asked for `pg_inherits` membership unchanged; `pg_class.xmin` moving is a side-effect of TRUNCATE and dropping it from the assertion prevents a false negative." |
| | astra | LEGITIMATE — "The row requires reading `pg_inherits`, not invariant `pg_class.xmin`. `test_e04_truncate.py:35` retains inheritance parent, sequence, inheritance xmin and partition status; `:128` compares them. The changed class xmin remains reported." |
| E-8 fix | grok | LEGITIMATE — "a second indented copy made the hash differ for a reason the row is not about. One body, bootstrap and restore." |
| | gemini | LEGITIMATE. |
| | astra | LEGITIMATE — "Restoring a differently formatted body does not restore the original body hash. Using `scratch.TRIGGER_FN_SQL` preserves the hash-equality assertion." |
| E-10 fix (`after_lock`) | grok | LEGITIMATE — "releasing the writer after the digest measured 0.024 s and did not wait through a digest. … **Both commit orders still run:** A/M writer arrives on the held lock and waits through digest; B writer commits first (`writer_first=True`; `after_lock` returns without waiting). Lock-free C still uses `after_digest` for the G-08 window." |
| | gemini | LEGITIMATE — "Releasing the writer the instant the lock is held exercises BOTH commit orders because the writer blocks on the lock in the locked case, and the sealer blocks on the writer's lock in the writer-first case." |
| | astra | LEGITIMATE — "It creates the intended arrival during the lock hold. Writer-first remains a separate branch at `test_e10_seal_race.py:151`; cases B/D still execute it. Lock-free case C retains release after digestion." |
| E-18 fix | grok | LEGITIMATE — "a `string_agg` fold cannot perform count+digest at 8,208,000 rows. Streamed fold is the production proof; assertion (rows, digest) unchanged." |
| | gemini | LEGITIMATE. |
| | astra | LEGITIMATE — "It enables the required large-source count-and-digest measurement without concatenating the table into one value. Source equality assertions remain at `test_e18_deadlines.py:235`." |
| E-19 two reporting fixes | grok | "Current file matches the description … Pre-fix text **NOT CHECKABLE FROM READS**. The live assertion is still `:167` `assert detected_by`." (no LEGITIMATE/WEAKENED tag) |
| | gemini | LEGITIMATE (both). |
| | astra | LEGITIMATE (both) — "E-19's false-green assertion is a separate defect; these two reporting fixes did not introduce or justify it." |
| E-6b (red) | grok | REAL RESULT — F-A = the row's "the candidate is dropped; F-A". |
| | gemini | REAL RESULT — F-A "exactly the one the spec's own row names". |
| | astra | REAL RESULT — "The selected fallback is exactly the row's 'the candidate is dropped; F-A.'" |
| E-9 (red) | grok | REAL RESULT — F-A = "counters dropped ⇒ F-A". |
| | gemini | REAL RESULT. |
| | astra | REAL RESULT — plus "E-9's damage and second reset occur through an autocommit connection. Its initial collision is **after committed damage**, not a before-commit demonstration." |
| reading 1 | grok / gemini / astra | narrowest **YES / YES / YES** |
| reading 3 | grok / gemini / astra | narrowest **YES / YES / YES**; all three: cumulative-as-worded passes E-7's and E-19's bypass; the `_xact_` view catches both |
| reading 4 | grok / gemini / astra | narrowest **YES / YES / YES** |
| item 5 | grok | "**Not confirmed by an OBS line.** E-18 never executes `string_agg`; `_source` calls `cli._probe` … `swapmini.py:72-79` *comments* the 1 GB `ProgramLimitExceeded` at 8,208,000 rows and still uses `string_agg` at scratch scale. … the 1 GB failure itself is a builder claim, not a pasted OBS." |
| | gemini | "Confirmed by `test_e18_deadlines.py` and `swapmini.py`. `REPLACED` cannot be a `string_agg` aggregate due to the 1 GB string buffer limit." |
| | astra | "confirmed in scope, with an evidence limit. … 'Cannot be an aggregate' is too broad; the demonstrated problem is materializing the complete serialization in one string. **NOT CHECKABLE FROM READS** — independently reproducing the precise 8,208,000-row string-buffer failure would require restoring and running the former aggregate expression." |

**Item 6 — IN FULL, every house, unedited**

- **grok:** "**6. E-15 ARM A `REPLACED=True` on lost content.** `test_e15_snapshot_race.py` **does** reproduce the current harness order: RR (`ev-migrate-connect.excerpt.py:552`) + before-probe then apply (`ev-migrate-rollback.excerpt.py:689-690`). ARM A: late row `in_new==0`, `in_legacy==1`, `REPLACED True`, all in-txn digests 28,800 / `5c4e050…`. ARM B: migration queued (`AccessExclusiveLock`, `granted=false`), late row PRESENT, `REPLACED True`. Lock-first **closes** it. FINAL already **requires** lock-first / dedicated-transaction: §3.4 *"Acquire locks on every source and destination relation before establishing the content snapshot"* and *"the swap requires a pre-probe locking phase or a dedicated transaction whose first content snapshot follows successful lock acquisition"* (`spec-final-s3.md`); chunk 1a is *"the lock-before-snapshot phase (F1)"* (`spec-final-s8.md`). FINAL does not leave the hole open; the current harness does, until 1a is built to those words."
- **gemini:** "ESCALATE 6: `test_e15_snapshot_race.py` really reproduces production's current order (RR precedes the lock). Lock-first is shown to close it. FINAL's chunk 4 as worded already REQUIRES the lock-first/dedicated-transaction shape ("Acquire locks on every source and destination relation before establishing the content snapshot")."
- **astra:** "6. **Snapshot race: confirmed; FINAL already closes it explicitly.** `swapmini.py:51` probes before locking in arm A. E-15 sets REPEATABLE READ and releases the writer after that probe. This reproduces the material production order in the supplied migration excerpts. The row remains in legacy, is missing from the target, and all in-transaction comparisons agree on stale content. Arm B observes the migration queued behind the writer, then takes its first content snapshot after acquiring the locks. The row appears in source and target. FINAL §3.4 explicitly requires locks before the content snapshot and a pre-probe locking phase or dedicated transaction; §8 assigns that work to chunk 1a. **The design text does not leave this hole open.** Implementing the swap inside the unchanged probe-first transaction would violate it. `SET LOCAL lock_timeout` precedes the lock in the miniature, so "LOCK is the first statement" should read "LOCK precedes the first content snapshot.""

**Item 2 — IN FULL, every house, unedited**

- **grok:** "**2. `pg_inherits.xmin` / `pg_class.xmin` as a membership generation.** **OUT OF SCOPE WITHOUT A NEW TRIBUNAL.** No house designed it; the tribunal is closed. (xmin also moves for wraparound, VACUUM FREEZE, and unrelated `pg_class` rewrites — not evaluated here.)"
- **gemini:** "ESCALATE 2: OUT OF SCOPE WITHOUT A NEW TRIBUNAL."
- **astra:** "2. **Catalog xmin: OUT OF SCOPE WITHOUT A NEW TRIBUNAL.** The observations establish that these catalog tuple versions moved in the tested histories. They do not establish a durable membership-generation protocol."

**Fifth (special attention), the houses' one-sentence answers**

| point | grok | gemini | astra |
|---|---|---|---|
| E-10 wait | "1.904 s … 1.819 s … Linear to a full i1 week (1,332,705 rows) … ≈ **8.8 s** on this host's ~151 k rows/s; production's band is ~7.1–8.0 s" | "1.904 s at 288,001 rows and scales workload-dependently … an estimate of the digest duration and not a constant" | "measured interval spans the writer's INSERT work through commit … includes lock waiting … ≈ **8.8 s** from A and **8.4 s** from M … illustrations, not bounds" |
| E-18 | "`_source` is `cli._probe` (count **and** digest) before any arm and after both cancels; `:235-236` assert equality … `lock_timeout` does not bound run time" | "source is intact … by exact row count and content digest equality … `lock_timeout` does not bound the overall statement run time" | "**Yes, SOURCE integrity is checked by both exact count and digest** … cancellation during this copy, not the complete deployment deadline across fencing, proofs and restart" |
| E-16 OIDs | "read from observer `bare_conn` … not from the queued-writer or prepared-statement session" | "read after commit from the session under test (not a fresh one)" | "**No, post-commit OIDs are not read from the tested writer/prepared session.** They are read through `bare_conn` at `:99` and `:143`" |
| E-17 | "`has_table_privilege(role, child, SELECT)` is False on all three and asserted … no PUBLIC `=…`" | "role is really granted SELECT on the parent ONLY (with no inherited or PUBLIC grant on the child)" | "**Yes, the role effectively lacks child SELECT, including inherited or PUBLIC access.**" |
| E-13 | "`_probe(parent)` … is the cost of one probe-set entry … Descent is demonstrated … `_probe_all` here only sees unpartitioned `bars`" | "measures exactly what chunk 1a needs to prove that empty partitions add negligible overhead" | "**Yes, the direct parent probe measures the incremental content-proof operation chunk 1a needs** … does not measure placement validation or prove registry integration … 'cold' is unsupported by cache controls" |

**Where two houses contradict each other on the same test — both quoted, neither smoothed**
- E-16 OIDs: gemini "The OIDs are read after commit from the session under test (not a fresh one)" · astra "No, post-commit OIDs are not read from the tested writer/prepared session. They are read through `bare_conn`" · grok "read from observer `bare_conn`".
- E-10 writer-first: gemini "the sealer blocks on the writer's lock in the writer-first case" · grok "B writer commits first (`writer_first=True`; `after_lock` returns without waiting)".
- E-8 (c): astra "YES — … assertions at `:104` onward never require it to show DML" · grok and gemini "NO".
- E-12 (c): astra "YES — `:136` accepts any caught database error and never asserts `written == [2, 2]`" · grok "NO — `landed==0` would fail if earlier `executemany` calls committed" · gemini "NO".
- E-15 (c): astra "YES, narrowly — … do not require `replaced=True`" · grok and gemini "NO".
- E-19 (c): grok and astra "YES" · gemini "NO".
- Item 5: gemini "Confirmed by `test_e18_deadlines.py` and `swapmini.py`" · grok "Not confirmed by an OBS line" · astra "NOT CHECKABLE FROM READS".

## Checked against the harness
Originals opened: `/Users/cobalt/cobalt-wt/bars-chunk-e/tests/experiments/bars_chunk_e/` (bytes equal to the packet copies, see Packet), `/Users/cobalt/cobalt/src/cobalt/db_migrations/cli.py`, the staged FINAL extracts, the builder's report parts. Test paths abbreviated to `test_eNN`.

| # | claim | who | file:line | verdict |
|---|---|---|---|---|
| 1 | E-8 reads `_xact_` but never asserts on it | astra | `test_e08:74` read; asserts `:104-112` (n, fn hashes, tdh, dirty_during, cum_after, digest) — none on `xact` | HOLDS |
| 2 | E-12 accepts any caught DB error; `written` never asserted | astra | `test_e12:136-143` (`case_b is not None`, `after_b==before`, `landed==0`); `written` only observed `:124` | HOLDS |
| 3 | E-13 probes the new parent directly; `_probe_all` sees only `bars` | astra, grok | `test_e13:100`, `:148`; builder OBS `_probe_all tables … ['bars']` (report part2 E-13) | HOLDS |
| 4 | E-14 case 3's blocker takes ACCESS SHARE before the migration starts (identical to case 2, not "holding NO lock while the swap starts") | astra, grok | `test_e14:135-141` (`SELECT max(ts)` inside `hold`), `:75-83` (`hold` runs, then `mig` is created); OBS case 3 `blocker_locks [('AccessShareLock', True)]` | HOLDS |
| 5 | E-15 arm A asserts only the row absent from target/present in legacy; `replaced` and digests are observed, not asserted | astra | `test_e15:118-124` | HOLDS |
| 6 | E-19 `assert detected_by` cannot fail once `:163` passes (`:140-141` appends the content digest) | astra, grok | `test_e19:140-141`, `:163`, `:167` | HOLDS |
| 7 | E-16 post-commit OIDs read from `bare_conn`, not the writer / prepared session | astra, grok | `test_e16:99`, `:143` (`_oids(bare_conn)`) | HOLDS |
| 8 | E-16 OIDs read from "the session under test (not a fresh one)" | gemini | `test_e16:99`, `:143` — `bare_conn` is a separate autocommit fixture connection | DOES NOT HOLD |
| 9 | E-10 writer-first: "the sealer blocks on the writer's lock" | gemini | `test_e10:151-157` — writer thread is joined (committed) BEFORE the seal thread starts; nothing to block on | DOES NOT HOLD |
| 10 | E-10 both commit orders still run after the `after_lock` fix | grok, astra (gemini: conclusion) | `test_e10:151-164` (`writer_first` branch), cases B/D `:215-221` | HOLDS |
| 11 | E-10 measured interval = INSERT through commit incl. lock wait | astra | `test_e10:139-144` (`t0` before `_writer`, `t1` after `commit`) | HOLDS |
| 12 | Report's "≈151,000 rows/s, inside production's 165,782–187,769 band" is false; M digests 288,009 not 288,001 | astra | report part2 E-10: 288,001/1.904 = 151,261 < 165,782; `rows_digested` M = 288009 (OBS `MEASURED WAITS`) | HOLDS |
| 13 | Linear extrapolation to 1,332,705 rows ≈ 8.8 s (A) / 8.4 s (M) | astra, grok | 1,332,705/288,001×1.904 = 8.81; /288,009×1.819 = 8.42 — ARITHMETIC OK | HOLDS |
| 14 | E-18's "triggers arrive with chunk 5-dev, after the swap" is inconsistent with FINAL §8 | astra | `test_e18` docstring `:19-23`; `spec-final-s8.md`: 5-dev row precedes S/R/4, 5-prod is the after-swap row | HOLDS |
| 15 | E-9 damage and second reset run on an autocommit connection, so the collision is post-commit | astra | `test_e09:103` (`conn` fixture = `scratch.connect()` autocommit, `conftest.py:47-56`), `:120-131` | HOLDS |
| 16 | `swapmini.py` uses `string_agg` (statements at `:80`, `:95`, `:103`); E-18 does not execute `string_agg` (`_source` → `cli._probe`) | astra, grok | `swapmini:80-104`, `:72-79` (comment); `test_e18:56-71` | HOLDS |
| 17 | The 1 GB `ProgramLimitExceeded` at 8,208,000 rows appears only as a comment / report text, not an OBS or executable arm | grok, astra | `swapmini:72-79`; report part4 "TESTS FIXED" row E-18 | HOLDS |
| 18 | "Confirmed by `test_e18…` and `swapmini.py`" that `string_agg` fails at 1 GB | gemini | neither file runs it — see #17; the failure itself is a PostgreSQL behaviour | NOT CHECKABLE FROM READS — re-run: the removed `string_agg(...)` fold over 8,208,000 rows of a scratch PG16 table |
| 19 | E-15 arm A reproduces production's order: `SET LOCAL` → before-probe (snapshot) → writer commits → LOCK | astra, grok, gemini | `swapmini:47-55` (`lock_first=False`), `test_e15:90-96`; `cli.py:552` (RR), `:688-691` (`SET LOCAL lock_timeout`, `before = _probe_all`, `_apply`, `after`) | HOLDS |
| 20 | FINAL §3.4 / §8 already require lock-before-snapshot / dedicated transaction | all three | `spec-final-s3.md` step 3 ("Acquire locks on every source and destination relation before establishing the content snapshot … a pre-probe locking phase or a dedicated transaction"); `spec-final-s8.md` chunk 1a "the lock-before-snapshot phase (F1)" | HOLDS |
| 21 | "LOCK is the first statement" is loose: `SET LOCAL lock_timeout` precedes it | astra | `swapmini:47` vs `:57`; `test_e15:137` observe text | HOLDS |
| 22 | E-17: children carry no PUBLIC / role grant; `has_table_privilege` false asserted | all three | `test_e17:108-109`; OBS relacl children `{postgres=arwdDxt/postgres,cobalt_system=arwd/postgres}` (report part3 E-17) | HOLDS |
| 23 | E-18: source count AND digest compared after both cancels | all three | `test_e18:56-71` (`digest_of` → rows+digest), `:235-236` | HOLDS |
| 24 | E-4 fix 2 retains `pg_inherits` keys and compares them | grok, astra | `test_e04:35`, `:42-43`, `:128-130` | HOLDS |
| 25 | E-12: `T0080` is not in the fill, so `landed==0` would fail if earlier executemany calls committed | grok | `test_e12:52-53` (`T0080`); `scratch.fill` tickers `T0001…` (`scratch:411`) | HOLDS |
| 26 | E-13's "cold" label has no cache control | astra | `test_e13:99-102` (three plain runs) | HOLDS |
| 27 | E-7 asserts `_xact_[1]==n`, cumulative equal, combined not equal | grok | `test_e07:108`, `:111`, `:115`, `:118` | HOLDS |
| 28 | E-19: `xact_shows_dml` True and survives the reset; cumulative equal to seal after reset | grok, astra, gemini | `test_e19:57-74`, `:118-123`; OBS E-19 (report part3) `xact_counters (0, 4800, 0)` before and after | HOLDS |
| 29 | E-9 tuple compare `:57` and assertion `:94` reject a colliding pass | astra | `test_e09:57-76`, `:94-100` | HOLDS |
| 30 | xmin also moves for wraparound / VACUUM FREEZE / unrelated `pg_class` rewrites | grok | PostgreSQL behaviour, no file states it | NOT CHECKABLE FROM READS — re-run: on the scratch PG16, `VACUUM FREEZE`, `ALTER TABLE … SET (fillfactor)`, `COMMENT ON`, a GRANT on a child, each followed by a read of that child's `pg_class.xmin` / `pg_inherits.xmin` |
| 31 | Grok: E-19 pre-fix text | grok | the packet holds final code, not the historical diffs | NOT CHECKABLE FROM READS — re-run: `git diff` of the two E-19 fixes on `bars/chunk-e-0920` (not opened; that worktree is outside this run's allowlist) |
| 32 | REPEATABLE READ takes its snapshot at the first query, not at `SET LOCAL` / `LOCK TABLE` (implicit in arm B's "first content snapshot follows the lock") | grok, astra | PostgreSQL behaviour; only E-15's two observed arms bear on it | NOT CHECKABLE FROM READS — re-run: E-15 arm B with the writer's commit landing between `SET LOCAL` and `LOCK`, and again with a `SELECT 1` before the `LOCK` |

Count (32 rows): **HOLD 26** (rows 1–7, 10–17, 19–29) · **DOES NOT HOLD 2** (rows 8, 9) · **NOT CHECKABLE FROM READS 4** (rows 18, 30, 31, 32).

## Chunks 1a and 2
| house | chunk 1a may build | chunk 2 may build | reason if NO |
|---|---|---|---|
| grok | YES | YES | — |
| gemini | YES | YES | — |
| astra | YES | YES | — |

Closing CHECK lines, verbatim: grok `CHECK: RESULTS STAND EXCEPT E-19 · chunk 1a may build: YES · chunk 2 may build: YES` · gemini `CHECK: RESULTS STAND · chunk 1a may build: YES · chunk 2 may build: YES` · astra `CHECK: RESULTS STAND EXCEPT E-19 · chunk 1a may build: YES · chunk 2 may build: YES`. Gate rows (E-12, E-13, E-15, E-17): no house says DO NOT RELY ON any of them.

## ESCALATE
Listed triggers:
- a house's `DO NOT RELY ON` for E-12, E-13, E-15, E-17: none.
- an ASSERTION WEAKENED that my file-check HOLDS: none (no house ruled any fix ASSERTION WEAKENED).
- a house finding that item 6 leaves a hole in FINAL's chunk 4 wording: none (all three: FINAL already requires lock-first).
- a packet mismatch: none.
- a house that did not check: none (3 of 3, each with a CHECK line).
- `ASK DESK`: none.

ESCALATE: 0. (Facts for the desk, not triggers: two houses' CHECK lines except E-19; astra's (c) findings on E-8, E-12, E-15 are code facts my file-check HOLDS — rows 1, 2, 5 above; the builder report's "151,000 rows/s inside the 165,782–187,769 band" and its case-3 "holding NO lock at all when the deploy began" fail my file-check — rows 12, 4.)

BARS CHUNK E CHECK DONE · grok: CHECK: RESULTS STAND EXCEPT E-19 · chunk 1a may build: YES · chunk 2 may build: YES · gemini: CHECK: RESULTS STAND · chunk 1a may build: YES · chunk 2 may build: YES · astra: CHECK: RESULTS STAND EXCEPT E-19 · chunk 1a may build: YES · chunk 2 may build: YES · houses that checked: 3 of 3 · results challenged: E-19 · claims that HOLD against the harness: 26 · DO NOT HOLD: 2 · chunk 1a may build: 3 of 3 · chunk 2 may build: 3 of 3 · ESCALATE: 0
