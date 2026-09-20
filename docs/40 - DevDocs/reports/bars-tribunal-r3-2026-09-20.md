# BARS TRIBUNAL ROUND 3 — 2026-09-20 (hub `bars-tribunal-r3-0920`, Sonnet 5)

## 0. Headline
- **3 of 3 houses ruled, the last round.** grok `BUILD WITH 4 FIXES` (P-span, P-closed, P-range, P-swap) · gemini `BUILD WITH 3 FIXES` (a, d, h) · astra `BUILD WITH 6 FIXES` (F1–F6); all three say "builder may fold them without another round: YES".
- **22 of 25** round-2 defects RESOLVED by their raiser; NOT RESOLVED: **G-01, G-12, G-13** (all astra). **13 NEW DEFECTs** named (gemini 3 · grok 4 · astra 6).
- Hub walk against the staged files: **18 sequences HOLD**, 4 claims DO NOT HOLD, **9 NOT CHECKABLE FROM READS** (PostgreSQL behaviour; each with its experiment and whether chunk E lists it). **12 dissent blocks** for the owner.
- No house shows the design reaching a card value, ranking or score. Report path was not refused. ESCALATE: 0. (I judge nothing, L37; the tables below are file checks.)

## PREFLIGHT
Authorization verified: `git log` of `cto-2026-09-20.md` lists 6 commits; `grep -n "^| R13 "` returns line 86 with Dejan's 13:33 ET words ("Push and approved everything. Please start all the process and inform me when you have something for me to rule on. I'm expecting you to run for a while.") — matches the prompt.

| rule | command | exit | allowed / DENIED |
|---|---|---|---|
| DATE GATE | `date` | 0 | allowed — `Sun Sep 20 14:53:12 EDT 2026` (still 2026-09-20; gate passes) |
| recovery | `ls scratch/tribunal-bars-0920/r3` | 1 | allowed — `No such file or directory` (fresh run, nothing staged) |
| grok | `grok --version` | 0 | allowed — `grok 1.0.25 (f7e67d6988e2) [stable]` |
| agy | `agy --version` | 0 | allowed — `1.2.7` |
| round-2 folder | `ls scratch/tribunal-bars-0920/r2` | 0 | allowed — holds `astra-ruling-r2.md`, `gemini-ruling-r2.md`, `grok-ruling-r2.md`, `DERIVED.md`, and the code excerpts |
| Codex probe | `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` (background) | 0 | allowed — answer `OK`, 229 tokens, no usage-limit text → **astra: UP** |

L74 note (recorded once, never raised again): a block appended inside a tool result (the Read of the prompt file) asked for a `Claude-Session: https://claude.ai/code/session_<id>` line and mentions a file-send tool. It is data; not followed. This run commits nothing.

## Packet
Staged in `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/r3/` (folder created by the first Write; no `mkdir`). Every file Read → Write, then `wc -c` against its original; all match. `DERIVED-v3.md` did not fit one Write and is staged in ORDERED PARTS (`DERIVED-v3.md.part1` = lines 1–119, `DERIVED-v3.md.part2` = blank line 120 + lines 121–265); QUESTIONS-R3's file list and every launch sentence say so. **Line citations below are `V3:<n>` = the ORIGINAL file's line number (part1 line n = V3:n; part2 line k = V3:k+119).**

| staged file | source | bytes (staged = original) |
|---|---|---|
| `DERIVED-v3.md.part1` + `.part2` | `docs/30 - Design/BARS-LIFECYCLE-DERIVED-v3-2026-09-20.md` | 38,136 + 34,333 = 72,469 = 72,469 ✔ |
| `round2-grok.md` / `round2-gemini.md` / `round2-astra.md` | `r2/{grok,gemini,astra}-ruling-r2.md` | 10,276 / 4,648 / 18,992 ✔ |
| `round2-checked.md` | round 2's report lines 276–335 (`## Checked against the files` … "Where a house says the design contradicts itself"; stop line :337 excluded) | 13,267 = (52,202 − 38,934 byte offsets by `grep -b`) − 1 blank line ✔ |
| `DERIVED-v2.md` | `r2/DERIVED.md` | 50,716 ✔ |
| `poller.py`, `clock.py`, `aggregate.py`, `anatomy-bars.py`, `migrate-proof.excerpt.py`, `owner-rulings.md`, `finviz-windows.md` | `r2/` | 4,981 / 12,394 / 1,568 / 5,559 / 7,601 / 7,086 / 5,303 ✔ |
| `ev-runner`, `ev-reconcile`, `ev-archiver-cli`, `ev-migrate-rollback`, `ev-db`, `ev-schemas`, `ev-placement`, `ev-watermark` (`.excerpt.py` / `.sql`) | `r2/` | 1,818 / 1,105 / 2,370 / 2,244 / 1,473 / 1,336 / 2,085 / 1,173 ✔ (four were first written 1 byte long — an extra trailing blank line — and trimmed to match before any launch) |
| `0001_bars.sql` | round 1's folder | 1,347 ✔ |
| `ev-store-upsert.excerpt.py` (NEW) | `/Users/cobalt/cobalt/src/cobalt/archiver/store.py` 104–172, headed by path and range | 2,638 = 102-byte header + 2,536 bytes (`grep -b` offsets 4165 → 6701 of the real file) ✔ |
| `QUESTIONS-R3.md` | the prompt's block, verbatim, + one appended "Files in this folder:" paragraph | (new) |

The brief is not re-staged; round 1's copy sits at `../BRIEF.md.part1`, `../BRIEF.md.part2`.

## Launch
15:07 ET, Sun 2026-09-20 — three independent background launches, one attempt each, none pointed at another's round-3 ruling. No HARNESS, METER or TIMEOUT.

| house | launched | landed | result |
|---|---|---|---|
| grok | 15:07 | ≈15:15 — wrote `r3/grok-ruling-r3.md` itself (reply was that path) | `RULING R3: BUILD v3 WITH 4 FIXES P-span P-closed P-range P-swap — builder may fold them without another round: YES` |
| gemini | 15:07 | ≈15:10, exit 0 — `r3/gemini-ruling-r3.md` written byte for byte | `RULING R3: BUILD v3 WITH 3 FIXES (a, d, h) — builder may fold them without another round: YES` |
| astra | 15:07 | ≈15:12, exit 0 — `r3/astra-ruling-r3.md` = the final message only (the transcript's echoed copy after `tokens used`) | `RULING R3: BUILD v3 WITH 6 FIXES F1 F2 F3 F4 F5 F6 — builder may fold them without another round: YES` |

Raw rulings: `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/r3/{grok,gemini,astra}-ruling-r3.md`.

## Round-2 defects re-run
`raiser's verdict` is the raiser's own word under v3. `walk` = the hub's walk through the staged code and v3's wording: SURVIVES (v3's wording stands against the raiser's sequence) / STILL FAILS / NOT CHECKABLE FROM READS. Gemini and grok each answered only their own rows; astra answered hers and gave a one-line view on G-06, G-11, G-19.

| id | raiser | raiser's verdict | walk | ≤30 words |
|---|---|---|---|---|
| G-01 | astra | **NOT RESOLVED** | STILL FAILS | V3:62 step (4) reports any post-rollback write error as `no_partition`; `upsert_bars([])` returns before connecting (`ev-store-upsert` :118–119) so a zero-row cycle never re-reads bounds. |
| G-02 | grok | RESOLVED | SURVIVES | Covered rows written, uncovered named (V3:62, step 3); the sequence he raised is met. The same path is what grok's P-closed and astra's F2 attack (see below). |
| G-03 | gemini | RESOLVED | SURVIVES | Gemini accepts the bounds read; v3 still carries it as N3 (V3:181). Gemini lists no N3 dissent. |
| G-04 | grok | RESOLVED | NOT CHECKABLE FROM READS | Candidate guards gated on E-3/6/7/9 (V3:28); PostgreSQL behaviour, each already an experiment. |
| G-05 | gemini | RESOLVED | NOT CHECKABLE FROM READS | Moved to E-3 (V3:190); replica-role behaviour. |
| G-06 | gemini | RESOLVED ("reason right") | SURVIVES | Whole dirty partitions are digested: `_probe` reads a whole relation (`migrate-proof.excerpt.py:59-98`); round 2 already marked 31.36 s arithmetic OK, premise not. |
| G-07 | astra | RESOLVED | NOT CHECKABLE FROM READS | Replica-role / no-op-function sequences moved to E-3 / E-8; MP1 default V3:70. |
| G-08 | astra | RESOLVED | NOT CHECKABLE FROM READS | `SHARE ROW EXCLUSIVE` seal lock (V3:77); the race is E-10. Astra: wait "not established" as one digest. |
| G-09 | astra | RESOLVED | SURVIVES | Conditional examples, first-contact writes included (V3:82, 232); arithmetic OK (below). |
| G-10 | grok | RESOLVED | SURVIVES | No online copy exists, so `upsert` of 10-05 (`ev-runner.excerpt.py:15–29`) cannot rewrite a copied row. Non-resident writers: see astra F1. |
| G-11 | gemini | RESOLVED ("reason right") | SURVIVES | A failed `ts < T0` equality stopped v2's swap (round-2 check #11); v3 removes T0 and copies everything inside. |
| G-12 | astra | **NOT RESOLVED** | NOT CHECKABLE FROM READS | Code order confirmed (`before = _probe_all` precedes `_apply`, `ev-migrate-rollback.excerpt.py:31-32`); whether a post-snapshot commit is invisible to the copy is PG snapshot semantics. |
| G-13 | astra | **NOT RESOLVED** | STILL FAILS | V3:93 step 6 says "residents down" and lists no lock, admission closure or activity check; step 3 (V3:90) has an activity query only for the swap. |
| G-14 | grok | RESOLVED | SURVIVES | IMCC 09-15…09-27 lies below `oldest_returned_ts` → `unknown` (V3:114, 116). Grok's own formula has two new holes: overlap and empty export (P-range). |
| G-15 | grok | RESOLVED | SURVIVES | Minutes below `oldest_returned_ts` are `unknown`; whether the vendor carries pre-IPO minutes is U17 (vendor fact, NOT CHECKABLE). |
| G-16 | gemini | RESOLVED | SURVIVES | No ledger; `unknown` for un-retained coverage (V3:116). |
| G-17 | astra | RESOLVED | SURVIVES | NVDA 09-04 is below the returned range → `unknown`. Astra's F3 separately attacks the `ingestion_failure` wording. |
| G-18 | astra | RESOLVED (withdrawn; "verifier's reason is right") | SURVIVES | Round-2 check #24: the label names exactly the response it describes. |
| G-19 | gemini | RESOLVED ("reason right") | SURVIVES | Empty parent until commit (V3:55); 106.8 + 62.1 = 168.9 (arithmetic OK, round 2 G2). Empty-parent probe cost = E-13, NOT CHECKABLE. |
| G-20 | astra | RESOLVED | SURVIVES | Switch ships OFF, flipped with the Lists edit (V3:100). |
| G-21 | astra | RESOLVED | SURVIVES | `5-dev` row precedes R (V3:138, 140). |
| G-22 | astra | RESOLVED | SURVIVES | "If the scale rehearsal is not authorized … remain blocked" (V3:88, 127); the struck v2 sentence is absent. |
| G-23 | astra | RESOLVED | SURVIVES | Chunk 4 wait-list (V3:141) names gates, R, item 11; astra's F5 attacks chunk 6's list, not chunk 4's. |
| G-24 | grok | RESOLVED | SURVIVES | The 2.67 M / 31 s delta line is absent from v3's §7 (V3:223–244). |
| G-25 | astra | RESOLVED | SURVIVES | V3:106 quotes astra's paragraph verbatim; no "missed print" assertion remains. |

Tally: RESOLVED by raiser **22 of 25** (gemini 6/6 · grok 6/6 · astra 10/13). NOT RESOLVED: G-01, G-12, G-13.

### Attacks (a)–(h), by house
| attack | gemini | grok | astra |
|---|---|---|---|
| (a) swap, one transaction | BROKEN BY gemini — a cron `restate` queued behind the ACCESS EXCLUSIVE lock resumes after the rename and inserts into `bars_legacy`. | BROKEN BY grok — P-span: children cover only ≥26 weeks ahead; live i1 starts 2026-07-30 → one source row has no partition → whole swap rolls back (also: `lock_timeout` ≠ run-time cap; REPLACED not bound to the fold; grants). | BROKEN BY astra — F1: the before-probe snapshot precedes the lock; a non-resident commit between them is omitted from copy and digest; F6: no run-time deadline. |
| (b) post-restart rollback | HELD | HELD ("no wrong-row sequence if the lock is the same fence as the swap; say so") | BROKEN BY astra — F1 rollback: a non-resident correction after the equality check reopens on the old price; step 6 names no lock or admission fence. |
| (c) poller bounds | HELD | BROKEN BY grok — P-closed: Monday 04:00:30 `closed` is all prior-week; only `now`'s period is tested; also `newest`/`stale` computed from unwritten rows | BROKEN BY astra — F2: mid-cycle detach with zero submitted rows never re-reads bounds; a non-routing write error is labelled `no_partition`. |
| (d) gap states | BROKEN BY gemini — empty export leaves `oldest_returned_ts` undefined; `max(...)` raises. | BROKEN BY grok — P-range: overlap window (`threshold` … watermark) falls below the range start → `unknown`; empty export; ticker not polled / `stopped_at` wording. | BROKEN BY astra — F3: a generic `PollFailure` / `stopped_at` / incomplete cycle becomes minute-level `ingestion_failure`; null-watermark `max`. |
| (e) proof | HELD | BROKEN BY grok — chunk 4's wait-list names item 11, not item 12, yet FROZEN_ARCHIVE narrows the proof at the swap. (Seal lock, F-A, text-scan: HELD.) | BROKEN BY astra — F4: E-5 keyword fallback and F-B leave the substitute undemonstrated; F-B's exposure "until the bracket ends" understates it. |
| (f) chunk E | HELD | BROKEN BY grok — E-6's fallback "a generation that DETACH breaks" names no writer (hand-wave). No bypass without an experiment. | BROKEN BY astra — assessment of E-3…E-14 (rows below); three routes with no experiment. |
| (g) build order | HELD | BROKEN BY grok — P-swap: item 12 (FROZEN_ARCHIVE) is a proof narrowing reachable at chunk 4 without being a wait-condition. 0b switch: HELD if default OFF. | BROKEN BY astra — F5: chunk 6's wait-list lacks E/R; MP4 path has no E/R dependency. |
| (h) arithmetic | BROKEN BY gemini — the "≈3.1 min / 5.6 min" conversions omit the ≈42 s deploy overhead the same §7 row names. | HELD on arithmetic; flags "illustration dressed as measurement": copy rates, filtered-digest rate, +20 d, 820 MiB. | BROKEN BY astra — F6: end-to-end 3.8–6.5 min now, 6.3–11.6 min at +20 td once the 42.2 s is added; all multiplications correct. |

### Chunk E rows disputed
| E | house | class | ≤30 words |
|---|---|---|---|
| E-3 | astra | incomplete fallback | "counters alone" is acceptable only after a complete counter protocol passes its own tests; otherwise F-A. |
| E-4 | astra | incomplete | Also demonstrate the statement-level TRUNCATE trigger under replica role; `relfilenode` change forces a content proof, it is not equality. |
| E-5 | astra | incomplete fallback | "treat COPY as a bypass keyword" is a text-scan; V3:81 says a text scan cannot authorize; needs F-A if no demonstrated guard remains. |
| E-6 | grok, astra | incomplete fallback | "membership must carry a generation that DETACH breaks" has no specified writer; grok: bind DETACH to `cobalt bars close` with generation+1, or F-A. |
| E-7 | grok, astra | incomplete fallback | Not a pre-commit guard ⇒ F-A, not F-B (grok); test the exact comparison algorithm and baseline selection (astra). |
| E-8 | astra | same as E-7 | Transaction-local DML evidence must still force comparison with trusted content. |
| E-9 | astra | wrong expectation | "Every reset/restart breaks equality" is not universal: clean restarts can preserve statistics; test colliding histories. |
| E-10 | astra | wrong expectation | Writer wait is workload-dependent, not one child's digest; residents-down fallback must include non-resident writers and F1's snapshot order. |
| E-12 | astra | incomplete | `INSERT…SELECT` is one statement, `executemany` is many inside a transaction — verify the context manager rolls back earlier executions. (E-12 already lists both cases.) |
| E-13 | astra | wrong expectation | ≈0 s is not guaranteed; 30 children still cost catalog and planning time. |
| E-14 | astra | incomplete | Too broad: test old connections, idle transactions, prepared statements, queued writers separately; add F1's snapshot race. |

Bypass routes with NO experiment — gemini: none stated · grok: none (residual `UPDATE SET close = close` vs `n_tup_upd` named "not worth an E") · astra: the pre-probe snapshot race; a queued non-resident writer across the rename; a bypass combined with a counter reset/collision before commit.

## Not resolved and new defects, verbatim
Unedited from the raw rulings in `r3/`. Hub notes appear only in `## Checked against the files`.

### astra — NOT RESOLVED rows (fold table, verbatim)
| G-01 | **NOT RESOLVED** | Reading bounds solves the original mixed-batch ambiguity, in either row order. However, §3.2’s exception branch labels every remaining write exception `no_partition`, even when refreshed bounds cover every submitted timestamp. Its once-per-cycle inventory also permits a current partition to disappear without another write exposing it. Concrete sequences and replacement: F2. |
| G-12 | **NOT RESOLVED** | Copying all timestamps removes T0’s age assumption. However, “every writer is down” is implemented as residents down plus a point-in-time activity check. The staged harness establishes its repeatable-read snapshot before `_apply`; a nonresident writer can commit after that snapshot and before the exclusive lock. Both copy and comparison can omit its acknowledged row. F1 supplies the sequence and replacement. |
| G-13 | **NOT RESOLVED** | Full upsert correctly carries an old-timestamp correction, and stopping on legacy-only keys avoids silently resurrecting deleted data. But “residents down” still does not enforce the quoted requirement to drain every writer during rollback. A concurrent acknowledged correction can miss reconciliation. F1 covers both directions. |

### astra — NEW DEFECTs F1–F6 (verbatim)
**F1 — NEW DEFECT: the swap and rollback lack an enforced admission fence**

Concrete cutover sequence:

1. On September 26, the migration’s activity check finds no competing session.
2. Its before-probe establishes the repeatable-read snapshot described in `ev-migrate-rollback.excerpt.py`.
3. A separate archiver process opens a connection and commits one NVDA i1 row for September 25 19:59. The staged store permits this through its independently opened connection and `ON CONFLICT DO UPDATE`.
4. The migration acquires `ACCESS EXCLUSIVE` after that writer commits.
5. Its repeatable-read copy and source digest use the earlier snapshot. Both omit the new row; counts and digests agree.
6. Cutover commits. The acknowledged row remains in legacy and is absent from the live parent.

An existing-row correction has the same visibility problem for a read-only source copy. The lock excludes later writes while held; it does not refresh an already established snapshot.

There is also no specified admission rule for an operator, cron or second desk arriving during cutover. An already waiting operation must not be allowed to resume against the retired relation after commit.

Concrete rollback sequence: after cutover, a nonresident process corrects NVDA September 1 from 141.20 to 141.00 after reverse reconciliation’s snapshot or equality check. Without locks and admission closure covering both relations through commit, the reverse rename can reopen service on 141.20 despite acknowledging 141.00.

**Exact replacement wording:**

> Before either cutover or reverse reconciliation, close database admission to every non-migration writer, including operator commands, scheduled jobs and other desks; drain existing sessions and transactions. An activity query is diagnostic, not the fence. Keep admission closed through commit and connection replacement. Acquire locks on every source and destination relation before establishing the content snapshot. Because the existing harness probes before applying migrations under REPEATABLE READ, the swap requires a pre-probe locking phase or a dedicated transaction whose first content snapshot follows successful lock acquisition.
>
> Preserve a trusted source baseline under that fence. Before cutover commit, verify that source i1 has not changed from that baseline and that the complete target i1 count and OHLCV digest equal it. Preserve and verify the complete legacy archive independently. Reverse reconciliation uses the same fence and locks: full i1 upsert, explicit legacy-only-key check, equality, renames, commit, fresh connections, then reopen admission. A nonempty legacy-only-key result aborts without committing reconciliation or renames; resolving deletion or retention differences requires a separate authorized procedure.

This preserves the one-transaction design. It does not require live change capture.

A source row without a destination partition should abort the transaction. A crash at row nine million should leave no committed partial copy, but recovery, WAL consumption and cleanup time must be measured. A waiting lock should time out; running copy work is a separate timeout problem, addressed in F6.

`REPLACED` catches a price changed only in the target. Source-versus-target equality alone does **not** catch the same wrong price written into both. The trusted source baseline above closes that distinction.

**F2 — NEW DEFECT: coverage refresh and failure classification are incomplete**

Two concrete sequences:

- At Monday September 21 04:00:30, the initial bounds read finds the current week. Another operation detaches it. NVDA returns only already stored Friday data; filtering produces zero submitted rows. `upsert_bars([])` returns before opening a connection, as the staged store explicitly shows. No routing exception occurs, so §3.2 never refreshes bounds or marks missing current coverage RED.
- At 04:01, NVDA submits one closed current-week row. All bounds exist, but its write fails for a non-routing reason. Under §3.2 step 4, refreshed current coverage is present, so the ticker is reported as `no_partition` despite having no uncovered timestamps. This hides the actual persistence failure and supplies a nonexistent reconciliation range.

**Exact replacement wording:**

> On an unpartitioned parent, execute the existing poller path unchanged. On a partitioned parent, validate current coverage before fetching and refresh it before publishing cycle health, including cycles with zero submitted rows. Serialize partition maintenance with polling or use a tested coverage-generation protocol so a topology change invalidates the cycle’s cached inventory.
>
> After a write failure, preserve StageDropped propagation, roll back, and refresh bounds. Unreadable bounds produce coverage_unknown and abort; missing current coverage aborts RED. Classify no_partition only when submitted timestamps are actually uncovered, recording all uncovered ranges. If all submitted timestamps remain covered, retain the existing generic error classification. Record the entire rolled-back submitted batch as unpersisted work, separately from the uncovered subset.
>
> For a successfully persisted covered subset, compute freshness from persisted rows and the prior watermark. Preserve its historical no_partition failure and recovery ranges; do not clear them through the generic error-success branch.

At 04:00:30, checking coverage independently of `closed` is correct: Monday’s open minute need not be submitted to establish that Monday has nowhere to store bars.

Historical-only holes should remain local to the affected ticker. I do not adopt N3’s always-abort rule.

**F3 — NEW DEFECT: generic failure records become unsupported minute-level evidence**

The verbatim principle in §3.7 is sound. Its implementation paragraph contradicts it.

Concrete sequence: NVDA first appears September 21. September 4 10:17 is absent and outside every retained response. Today’s fetch fails, creating `PollFailure("NVDA", "error", now)`. The proposed classifier labels September 4 10:17 `ingestion_failure` merely because NVDA carries a failure. That failure provides no evidence about September 4.

Likewise, a stopped cycle can label historical absences for an entirely unattempted ticker as ingestion failures. In the staged code, `stopped_at` is assigned on errors and polling then **continues**; it is not a reliable description of a budget cutoff or of which members were attempted. A carried `stale` record is not a failed acquisition range either.

**Exact replacement wording:**

> PollResult records cycle identity, attempted tickers, response coverage, successful persistence coverage, and any evidenced failed ranges. A generic PollFailure, stale record, stopped_at value or incomplete cycle is not minute-level coverage evidence.
>
> For each absent closed minute, use no_print_as_fetched only when a retained successful response covers it and omits it; use ingestion_failure only when retained acquisition or persistence evidence covers that minute. Otherwise retain unknown. Distinguish returned-but-unpersisted rows from rows omitted by the response.
>
> On first contact, use oldest_returned_ts without applying max to a null watermark. An empty response supplies no inferred range. The successful range must remain within the returned closed-time extent; overlap below the conservative watermark boundary may remain unknown. Cards rendered between cycles use explicitly identified retained evidence or unknown, never an implied current-cycle success. Persist the classification and supporting evidence with the card inputs.

No new table is logically necessary. Existing card-input persistence can hold this evidence if its schema is extended appropriately. The staged files do not show that persistence implementation, so “no new table” is a design option, not a demonstrated integration fact.

**F4 — NEW DEFECT: experimental fallbacks can weaken the proof without demonstrating the substitute**

Two concrete paths remain:

1. E-5’s unexpected result says to treat `COPY` as a bypass keyword. A migration can invoke dynamically constructed SQL or a stored function whose body performs the copy. V3 itself acknowledges that text scanning cannot authorize a narrowed proof. Keyword fallback therefore does not close the hypothetical failed-trigger path.
2. Under F-B, a migration changes a SEALED NVDA September 1 close to zero. The post-deploy bracket detects it and finishes. No restoration procedure is specified. The price does not automatically become correct when the bracket ends, so “wrong until the bracket ends” understates the exposure.

**Exact replacement wording:**

> A failed or inconclusive experiment disables every proof optimization that depends on that behavior. The automatic fallback is F-A: full live-table content proof before and after the migration, with CHANGED rejected before commit. A proposed alternative guard must itself be specified and demonstrated before activation; keywords, unnamed membership generations and untested counter combinations are not substitutes.
>
> Any partition selected for post-migration digestion must have a trusted pre-migration comparison value. A newly discovered invalidation cannot be handled by computing only a post-change digest. Seal publication must take its lock before establishing the content snapshot used for publication.
>
> F-B requires explicit owner acceptance of post-commit detection. State that wrong SEALED content may remain until repair or recovery completes, not merely until detection finishes. Define the preflight baseline, post-deploy comparison, failure alert, affected-reader handling and recovery procedure before offering F-B for activation. Text scanning may only widen the proof.

MP1’s default is sufficient to keep development proceeding while these experiments remain unresolved. Passing fourteen examples alone is not proof that arbitrary privileged code cannot bypass the protocol.

**F5 — NEW DEFECT: the activation graph does not enforce all its headline gates**

Concrete dependency sequence: the owner rules retention items 1–2; the restore drill passes; chunk 6’s listed dependencies are satisfied while E/R have not passed. Its row permits the first DETACH despite §0’s claim that no detach is reachable before both gates.

There is also an exceptional MP4 authorization path in §3.3 without an explicit E/R activation dependency.

**Exact replacement wording:**

> Production renames, DETACH operations and proof narrowing require the relevant mechanism experiments to PASS and the relevant production-scale rehearsal to PASS; “reported” is insufficient. Chunk 6 explicitly depends on those gates, the owner’s retention rulings and the restore drill. FROZEN_ARCHIVE activation requires the swap rehearsal and item 12 authorization. MP4 has no activation path in this build; any later proposal requires its own demonstrated protocol and owner ruling.
>
> Chunk 0 plus 0b activation is an explicit exception to the E/R sequencing: after the required shadow night and the owner’s timing decision, the effective lists and every non-i1 refusal activate together. While OFF, all associated store and CLI refusal branches preserve existing behavior.

Stopping non-i1 writes before the swap rehearsal is intentional and consistent with the owner’s instruction. It should be stated as that exception, rather than hidden behind a universal gate claim.

`bars_legacy` can be outside the in-outage proof only after item 12 is approved. It still contains the preserved non-i1 archive. Reverse upserting live i1 does not repair damage to those rows.

**F6 — NEW DEFECT: outage illustrations omit deployment work and do not bound running work**

A concrete operational sequence is a ten-million-row copy that acquires its lock promptly, then slows sharply under WAL or disk pressure. `lock_timeout` does not stop that running statement. The design’s “any timeout rolls back” does not provide a deadline for leaving the outage.

The arithmetic also separates approximately 42 seconds of ordinary deployment work from numbers labeled “the swap’s outage.”

**Exact replacement wording:**

> Report end-to-end resident outage, including admission closure, lock acquisition, all proof passes, copy, commit, connection replacement and verified restart. Set and rehearse finite statement deadlines plus an overall deployment deadline and cancellation/recovery procedure; lock_timeout bounds lock waits only. Reserve time for abort, crash recovery and restart before the next scanning session. Disk failure and rollback can leave WAL, cleanup work or recovery delay even when production rows remain transactionally unchanged.
>
> The current arithmetic illustrates copy-and-proof time, not the complete outage. Add the reported approximately 42.2 seconds of other deployment work, then replace all illustrations with R’s measured end-to-end result. A seal’s approximately 7.8-second digest is likewise an estimate, not a maximum writer wait.

### gemini — NEW DEFECTs (a), (d), (h) (verbatim)
(a) `NEW DEFECT`: A cron job (`cobalt archiver restate`) connecting after the `pg_stat_activity` check blocks on the `ACCESS EXCLUSIVE` lock, binding to the `bars` OID. The migration copies the data, renames `bars` to `bars_legacy`, and commits. The cron's lock wait resolves, and it inserts its i1 row directly into `bars_legacy`, silently losing the row from the live table.
(d) `NEW DEFECT`: A fetch that returns an empty export (e.g., zero volume today) leaves `oldest_returned_ts` undefined or None. The calculation `max(watermark_before_fetch, oldest_returned_ts)` will raise a Python `TypeError` or `ValueError`, crashing the poll cycle. The covered range for an empty success must use the requested bounds, not the returned row content.
(h) `NEW DEFECT`: The swap outage minutes in §7 mathematically exclude the 42-second deploy overhead from the final minute conversions. For today's size, 187.8 s is 3.1 min, but the total outage is 187.8 + 42 = 229.8 s (3.8 min). The 3.1 min and 5.6 min figures are illustrations dressed as measurements that silently understate the true deploy outage.

(gemini gave no separate "exact replacement wording" for (a) or (h); (d)'s replacement is its last sentence.)

### grok — NEW DEFECTs P-span, P-swap, P-closed, P-range (verbatim, from `## NEW DEFECT (v3 inventions only)`)
**P-span — lost swap, not lost bars.** Chunk 2 creates "≥26 weeks **ahead**"; the heartbeat is `[now − (vendor window + 2 days), now + horizon]` (~16 d back). Live i1 starts **2026-07-30**. Sequence: swap window 2026-10-24 weekend; `bars_p` children cover 2026-10-05…+26 w; `INSERT INTO bars_p SELECT … WHERE interval='i1'` hits NVDA 2026-07-30 04:00; no child; E-12: whole transaction rolls back. Production intact, deploy failed, he sits in the pause for nothing. R would catch it if R copies all i1; the **text** does not require the children R needs.

Replacement: before chunk 4, children cover `[min(ts) of source i1, now + horizon]`, contiguous, no `DEFAULT`. Heartbeat after swap goes RED for any hole in the still-attached span, not only the vendor window.

**TOCTOU / lock never comes / 5–10 M rows / crash at 9 M / lock_timeout vs runtime.** `pg_stat_activity` then `LOCK` is fail-fast only. A `cobalt archiver restate` or second desk that starts after the check either finishes (its rows are in the copy) or holds a lock (`SET LOCAL lock_timeout` already exists, `ev-migrate-rollback.excerpt.py:30`) and the swap aborts — production unchanged. **A lock that never comes is only possible if `lock_timeout` is 0 or unset; the harness today does set it.** `lock_timeout` does **not** cap `INSERT…SELECT` runtime. Crash at row 9 M: uncommitted → source intact (R). Disk-full / WAL of one 5–10 M-row transaction is U4; §7's 820 MiB is **table bytes only** — sizing the gate from 820 MiB under-buys WAL/temp.

**Renames / old connections.** E-14 fallback is right: restart every resident on fresh connections before the new name is trusted. A leftover prepared statement would still see the old OID (`bars_legacy`). L66 + ACCESS EXCLUSIVE make this fail-safe if **every** session is gone; an operator connection not in the resident list is the residual.

**Grants.** "parent + open child" is not enough. Replay/card read older weeks (`U18`: replay ~14 d). PG16 does not inherit GRANTs onto partitions. A `cobalt_app` SELECT through the parent on a child with no GRANT is a missing-history read, not a wrong price.

**REPLACED vs a different i1 price.** MP1 hashes `to_jsonb(t)` of every column, PK-ordered (`migrate-proof.excerpt.py:3-8, 77-87`). If REPLACED is that fold over `bars WHERE interval='i1'` vs `bars_p`, a close of 141.20 vs 141.00 cannot pass. If it is keys+counts only, it can. The invariant sentence is the right rule; it is not yet bound to the fold.

**Outage illustration (§7).** Honest that copy rate is U5 and the minutes are illustration. Not honest if read as a measurement: 52.0 s i1-filter digest assumes the unfiltered 170 k rows/s (no index serves `interval`-then-PK); 25 k/100 k copy rates are assumed; +20 d ignores non-i1 growth until chunk 0; WAL/temp and `statement_timeout` are absent. Desk item 11 must wait on R, not on 3.1–5.8 min.

**P-closed — Monday 04:00:30.** `closed` drops the still-open minute (`:99-101`). At Mon 2026-10-12 04:00:30, `now` is week W1 (10-12), `closed` is entirely W0 (Fri 10-09 19:59 and overlap). Step (1) only tests the period containing `now`. Sequence: W1 exists, W0 detached or never created; cycle does **not** abort; every ticker's `closed` is uncovered; per-ticker `no_partition`; loop continues ~500 times; radar health not RED. Cards at 04:05 cannot persist Friday overlap. Heartbeat may already be RED; the poller still treats it as historical-only.

Replacement: abort RED if **any period that this cycle's `closed` would write** is missing (period of `now` **and** of `max(closed.ts)` when `closed` is non-empty), not only `now`.

**Stale bounds inside a cycle / detach between read and write.** Operator DETACH of 2026-09-28 at 09:31 during a scan: XYZ first-sight still submits that week; `executemany` raises; **that ticker's current-week rows roll back**; re-read: current covered → per-ticker `no_partition`; others continue. Next cycle retries (watermark still None). One cycle late, not 500 names, not Friday-as-live. Quiet-window DETACH (chunk 6) makes this operator error. Not a fifth fix; test it as already listed.

**`stale` / `error` at `:113-124`.** Uncovered historical must **not** take the `except` path (`:112-115` sets `error` + `stopped_at`). Do not compute `newest` (`:117-120`) from unwritten `closed` minutes — use persisted `watermark` / written ts. Empty covered at Monday 04:00 must not look like a successful ticker with Friday `newest`. `no_partition` is its own class; do not also plant `error`.

**P-range.** My own formula, taken verbatim, starts at `watermark_before_fetch` and **excludes the overlap window**. Sequence: watermark 10:00, `overlap_bars=3`, threshold 09:57; fetch omits 09:58; `closed` includes 09:57 and 09:59 (`bar.ts > threshold`); range `[max(10:00, oldest), newest] = [10:00, …]`; 09:58 is absent and below the range → `unknown` even though this response covered it. Replacement: covered = `[threshold if watermark else oldest_returned_ts, newest_after_fetch]` clipped to the successful response; first contact still starts at `oldest_returned_ts`.

**Empty export.** Fetch `[]`, watermark None, `oldest_returned_ts` undefined. Sequence: NEWCO, Finviz returns no rows. If newest is forced to `now`, the whole vendor window becomes `no_print`. Replacement: empty successful export → **no covered range**, absences `unknown`.

**Ticker not polled / card between cycles / `stopped_at`.** Not polled this cycle → `unknown` (not no-print). Between cycles, last stored card-input range only. Wording "absent and this ticker carries a PollFailure **or the cycle did not complete** → `ingestion_failure`" would paint tickers 1–199 as ingestion_failure because ticker 200 hit the budget. Replacement: `ingestion_failure` only for a ticker with a covering `PollFailure`, or a ticker at/after `stopped_at`; successfully polled tickers keep their range.

**(grok §(e), proof)** … **Exception:** `FROZEN_ARCHIVE` on `bars_legacy` is a proof narrowing at chunk 4, and chunk 4's wait-list names item 11, not item 12. Desk says NO while it waits. The table must match the prose.

**(grok §(e), F-B)** … **F-B** names the exposure (wrong SEALED price from commit until the post-deploy bracket) but does not say whether that bracket runs **before** residents restart. I refuse F-B (same harm as bare 5b).

**(grok §(f), E-6)** … **hand-wave**: "generation that DETACH breaks" has no writer. Bind DETACH to `cobalt bars close` in one txn with `generation+1`, or F-A.

**(grok §(g))** … First proof narrowing is 5-prod **or** item 12 at chunk 4 — the latter is the leak (P-swap). … Residual: a tampered **non-i1** row in the archive rides back into `bars` on step-6 rollback; card paths do not read it after chunk 0. HIS (item 12); NO until he says YES.

## Advice on the owner's rulings — changes since round 2
`round 2` = the house's own R2 line (`round2-<house>.md`); `round 3` = its R3 line, verbatim.

| item | house | round 2 | round 3 | the harm |
|---|---|---|---|---|
| 4 | gemini | UNCHANGED (round 1 column in DERIVED §4: "D closed / A open") | "Add B (strict per-target lock); A only = reviewed corrections are overwritten in a seconds-wide race, leaving wrong prices on your cards." | wrong prices on cards (seconds-wide overwrite race) |
| 1 | grok | "**CHANGED — 365 days hot** (keep everything hot until the restore drill, then 365). Under §3.3 the in-outage proof no longer grows with retention; 90 days is now lost bars he cannot replay, vendor closed, EV stuck at insufficient data. Price of 365 is disk (~10.2 GiB/yr) and an evening bracket (~426 s at 12 months, residents up), not a 04:00 outage." | "**CHANGED (harm, not the number):** keep everything hot until the restore drill, then 365. Under **MP1** that is ≈14 min deploy outage at 12 months (+15.7 s per further hot week), not only disk and an evening bracket. Still cheaper than lost bars the vendor will not re-serve. Nothing detaches until you say." | a deploy outage of ≈14 min at 12 months under MP1 vs lost bars |
| 5 | grok | "**CHANGED** — YES to 5b only with in-outage DML-counter equality on sealed (`ENABLE ALWAYS` trigger); 5a only with both guards; `--full` stays. Bare 5b as written: wrong prices pass the deploy and sit under cards until evening." | "**UNCHANGED in substance** — MP1 until E; YES to 5b only if E-3/6/7/8/9 pass **and** in-outage counter equality + `ENABLE ALWAYS`; skip 5a. If E cannot exclude a bypass: **F-A** (keep MP1), never F-B. F-B is a wrong old price under cards from commit until the bracket ends." | wrong old price under cards (F-B) |
| 11 | gemini | (new item) | "11. (A) Copy everything with the system down; (B) puts a capture trigger on the live write path, where a bug means a dead radar at 04:00." | minutes of outage vs a dead radar at 04:00 |
| 11 | grok | (new item) | "11. **A, on a weekend. Do not build B unless R cannot fit the window you name.** A is minutes of outage (R measures; 3–11 min is a guess) when nobody trades. B buys a shorter cutover with a capture trigger on the live poller for every day the copy runs — the same write path R8 already protected. A bug there is a dead radar at 04:00, paid to save minutes on a Saturday. If R comes back longer than the window you name, *then* ask B; do not install B first." | minutes of outage on a Saturday vs a dead radar at 04:00 |
| 11 | astra | (new item) | "11. **NEW ADVICE — choose A, with F1 and F6, in a measured weekend window.** Accept several minutes of planned outage to avoid adding change capture to the live poller. The corrected illustrations are roughly **3.8–6.5 minutes now**, or **6.3–11.6 minutes at +20 trading days**, before additional unmeasured work. Choose B only if the rehearsal cannot fit your approved window; B needs its own design and rehearsal." | 3.8–6.5 min now / 6.3–11.6 min at +20 td vs live-path capture |
| 12 | gemini | (new item) | "12. YES; a silent change to the archive cannot reach a card, and proving it in-outage adds 106.8 s of deploy outage for a table nothing reads." | 106.8 s per deploy |
| 12 | grok | (new item) | "12. **YES — prove `bars_legacy` off the outage, labeled `NOT_CONTENT_VERIFIED (frozen archive)`, never `UNCHANGED`.** Nothing reads it, so a silent change cannot price a card; step-6 rollback overwrites its i1 from live. NO costs ~107 s on **every** later deploy until you drop it. Do **not** default this on in chunk 4; until you say YES, MP1 still covers it." | ~107 s per deploy vs an unproven archive |
| 12 | astra | (new item) | "12. **NEW ADVICE — conditional YES to off-outage archive proof.** It can save roughly the reported **107 seconds per deploy**. Require an enforced frozen relation, retained trusted digest, recoverable backup, explicit off-outage comparisons and verification before using it for rollback. The exposure includes preserved non-i1 history; a delayed alert cannot reconstruct damaged rows. Until these conditions and your ruling exist, keep archive MP1." | ~107 s per deploy vs damaged non-i1 history that a late alert cannot rebuild |

`UNCHANGED` counts (items 1–10 minus the rows above): **gemini 9** (items 1, 2, 3, 5, 6, 7, 8, 9, 10) · **grok 8** (items 2, 3, 4, 6, 7, 8, 9, 10; item 1 CHANGED, item 5 "unchanged in substance", quoted above) · **astra 10** (items 1–10, all "UNCHANGED" against her round-2 lines). Gemini's items 7–10 lines are bare `UNCHANGED`; gemini's round-2 §4b lines (K = 50, 30 s) are not restated in round 3.

## Dissents for the owner, verbatim
### gemini
DISSENT FOR THE OWNER:
D1: A repair seam lacking a strict per-target lock allows delayed poller threads to overwrite your reviewed corrections with bad data in a seconds-wide race. If this happens, wrong prices return to your cards. It is highly likely to happen during latency spikes. Fixing this now costs a simple generation lock; fixing it later means chasing phantom data regressions in production.

D3: After a vendor restatement, the unchanged poller will continue mixing old and adjusted prices. A red dashboard alone does not stop these mixed, wrong prices from reaching your cards. This is guaranteed to happen on every restatement. Fixing it now by suppressing price-derived outputs on degraded tickers costs little; fixing it later means trading on false signals.

(gemini lists no D2, N2 or N3 block.)

### grok
**D1 — delayed poller overwrites a reviewed repair (open week).** What: you correct NVDA's 10:17 bar at 20:40; a poller fetch that started at 19:58 lands after and `DO UPDATE`s the old print back (`poller.py:64` hook optional, `:103-105` no generation). Closed weeks: only if you add D. How likely: any repair that overlaps an in-flight fetch — seconds-wide, not theoretical. Cost now: D on closed children (already in the candidate ledger). Cost later: one bad print under a card you already reviewed, found when you replay.

**D2 — a quiet-window margin is not exclusion.** What: repair starts 03:50, scanning opens 04:00, in-flight write commits 04:00:20 onto the corrected row. Same overwrite as D1. How likely: every pre-open repair that is not finished and committed before the first poll acquires. Cost now: finish repairs inside the pause or take D. Cost later: same mixed print, plus a false sense that "≥5 min after last poll" closed it.

**D3 — restatement mixes old and new prices on the card.** What: vendor restates a morning; append writes new minutes; old minutes stay; the card still mixes both. This design does not fix it (red dashboard does not reconcile). How likely: every restated name until you rule a degraded/suppressed state. Cost now: L9-degrade that ticker (reaches the card face — your word). Cost later: size off a mixed tape.

**N2 — Astra wants B (per-target lock on the poller).** I still refuse B. What: a bug on the 04:00 write path is a dead radar, not a slower night. How likely: first non-trivial lock/generation bug in a scan loop. Cost now: nothing — A+D holds. Cost later if you take B: you debug the poller during premarket instead of during a pause.

**N3 — always-abort on any missing partition.** **NONE.** Always-abort is the sequence I already refused: one new mover's 14-day export overlapping one missing historical week halts ~500 names and leaves Friday on the cards (`poller.py:96-102`). v3's bounds read meets the need without dissecting `e`.

**P-span / P-closed / P-range / P-swap** are fixes, not dissents: they fold into v3 without a new architecture.

### astra
- **G-12/G-13 — write fencing:** A separately launched job can acknowledge a bar or correction that the swap or rollback omits. The overlap is probably uncommon, but no staged evidence measures it. Fix admission and snapshot ordering now; after cutover, finding stranded corrections requires reconciliation and another outage. F1 is required.

- **G-01 — coverage handling:** A disappearing current partition can escape a cycle with no submitted rows; unrelated write errors can be mislabeled as missing partitions. Both become deterministic under the described events, though their production frequency is unknown. F2 is a contained change now; later diagnosis starts from misleading failure records.

- **D1 — delayed poller write:** A response fetched before a repair can later overwrite the reviewed price. I judge the race uncommon under quiet-window discipline, but possible and unmeasured. Transactional exclusion now costs a separately reviewed live-path change; afterward it costs identifying and repairing the overwritten bars.

- **D2 — quiet-window margin:** Starting a repair before scanning opens does not itself stop it overlapping a later writer. Likelihood depends on delays and repair duration, neither measured here. Enforced exclusion costs design and testing now; after an incident, it also costs an outage and price reconciliation.

- **D3 — mixed adjusted prices:** Old and adjusted prices can coexist despite a red dashboard. This is a credible restatement failure, not a quantified daily probability. An integrity state and authorized suppression require separate card-facing work now; later, affected outputs and stored history also need review.

- **N2 — recommendation B:** I still recommend transaction-level repair exclusion and generation validation, subject to your current A ruling. It introduces live-path implementation risk but directly addresses D1/D2. Building it later remains possible; accepting A meanwhile accepts those correction-overwrite risks.

N3 is not my dissent. Historical-only holes should not stop healthy current polling for the entire universe.

Counts: gemini 2 blocks · grok 4 blocks + N3 `NONE` · astra 6 blocks = **12 dissent blocks**.

## Checked against the files
Files = the staged copies in `r3/` (byte-matched to originals) or real files on main. `poller:N` = `poller.py:N`; `V3:N` as defined under `## Packet`; `mig:N` = `ev-migrate-rollback.excerpt.py:N`; `store:N` = `ev-store-upsert.excerpt.py` (real `store.py` line = N + 102). PostgreSQL behaviour, psycopg internals and row counts cannot be settled from reads: `NOT CHECKABLE FROM READS`, with the experiment and whether chunk E already lists it (L70 — never restated as a defect). No database query was run.

| # | claim | who | file:line | verdict |
|---|---|---|---|---|
| 1 | With `watermark` None (first contact, `poller:97`) or an empty export, a range built as `max(watermark_before_fetch, oldest_returned_ts)` has no defined operand; V3:115 gives no rule for either case; in Python `max(None, datetime)` raises `TypeError` | gemini (d), astra F3, grok | `poller:96-102`; V3:115 | HOLDS — text gap; the crash needs a naive implementation, but the text prescribes none |
| 2 | §7 names "the rest of a deploy ≈ 42 s" in the swap row but the ≈3.1–5.8 min / 5.6–10.9 min headline figures exclude it | gemini (h), astra F6 | V3:236 (row), V3:92 (step 5 "≈ 3.1–5.8 min") | HOLDS — 187.8 + 42 = 229.8 s = 3.83 min (ARITHMETIC OK); astra's 230.0 s uses 42.2 |
| 3 | v3 says children are created ≥26 weeks ahead; no line requires them to reach back to the oldest source i1 row; live i1 starts 2026-07-30 | grok P-span | V3:58; `owner-rulings.md` (R9: "i1 and i2 both run 2026-07-30 → 2026-09-18"); V3:90 ("rows route to the pre-created children") | HOLDS — text gap; R (V3:140) copies "the whole swap transaction" and would hit it, but R's own children are not specified either |
| 4 | Monday 04:00:30: `closed` excludes the still-open minute, so it ends in the prior week; step (1) tests only the period containing `now` | grok P-closed | `poller:98-102`; V3:62 step (1) and (3) | HOLDS — with W1 present, W0 absent, no abort; every ticker's overlap rows are "uncovered" → per-ticker `no_partition`, as V3:62 (3) is written |
| 5 | `closed` includes `bar.ts > threshold` where `threshold = watermark − overlap_bars`; v3's range starts at `max(watermark_before_fetch, oldest_returned_ts)` | grok P-range | `poller:97-102`; V3:114, 115 | HOLDS — minutes in (threshold, watermark) that the response covered lie below the range start → `unknown` (conservative, not a false label). Sub-step "`closed` includes 09:57" DOES NOT HOLD: `bar.ts > threshold` excludes 09:57 (`poller:101`) |
| 6 | Chunk 4's waits-for names item 11, not item 12; step 7 makes FROZEN_ARCHIVE "a narrowing … HIS (§4 item 12)"; item 12 says "NO while it waits (MP1 covers it)" | grok P-swap, astra F5 | V3:141 vs V3:94 and V3:172 | HOLDS — three lines quoted: V3:141 "§3.4 step 1's gates, all of them; R passed; his §4 item 11; L66 / L43 / L68; the stated outage"; V3:94 "This IS a narrowing of what the outage proves, so it is HIS (§4 item 12)" |
| 7 | `stopped_at` is set in the `except` branches and the loop `continue`s; nothing in `poll()` breaks on a budget | astra F3, grok | `poller:94-95, 114-115` | HOLDS — `stopped_at` = the last errored ticker, not a cut-off point. Grok's replacement "a ticker at/after `stopped_at`" rests on the opposite reading and DOES NOT HOLD against these lines |
| 8 | v3's classifier: "absent and this ticker carries a `PollFailure` or the cycle did not complete → `ingestion_failure`" | astra F3, grok | V3:115; `poller:93, 113` (`PollFailure` = ticker, reason, onset only) | HOLDS — the record carries no minute range, so a September-4 minute is tagged by a today failure |
| 9 | `upsert_bars([])` returns 0 before `_connect()` | astra F2 | `store:16–17` (`if not bars: return 0` precedes `with self._connect()` at `store:18`) | HOLDS |
| 10 | Step (4): after a raised write, bounds are re-read; missing current → abort; "otherwise that ticker fails with `no_partition`" | astra F2 | V3:62 | HOLDS — no test that the submitted timestamps were actually uncovered |
| 11 | Step (1) reads bounds once per cycle, before the first fetch; a detach later in the cycle is seen only if a write raises | astra F2, grok | V3:62 | HOLDS as text; grok's detach-between-read-and-write: the `executemany` raises, that ticker rolls back, one cycle late — consistent with `poller:104-115` |
| 12 | `newest`, `stale`, and the `error` pop are computed from `closed` after a successful `upsert_bars`; v3 names no rule for them when uncovered rows are removed | grok (c) | `poller:116-124`; no `` `stale` `` in V3 (grep count 0/0) | HOLDS — text gap |
| 13 | The harness runs `before = _probe_all(conn)` then `_apply` inside one transaction opened by `_connect(read_only=False)`; the code comment names REPEATABLE READ | astra F1/G-12 | `mig:22-33`, `mig:40-42` | HOLDS (order). Whether a commit landing after that first read is invisible to a later `INSERT … SELECT` in the same transaction is PG snapshot semantics — NOT CHECKABLE FROM READS; experiment: two sessions, RR transaction reads one table, other session commits a row, first session takes ACCESS EXCLUSIVE, copies, reads count. E-14 lists a blocked READER, not this; astra herself says no experiment covers it |
| 14 | v3 does not fix the order of a before-probe and the LOCK: step 3 lists LOCK → INSERT → REPLACED with no before-probe; §7 sums "before-probe 52.0 s + legacy-i1 digest 52.0 s + new digest 31.1 s" | astra F1, grok (contradicting claims, below) | V3:90 vs V3:236 | HOLDS as an internal inconsistency — both lines quoted. Astra's failing sequence needs the probe first; grok's "rows are in the copy" needs the lock first |
| 15 | A non-resident writer that queues behind ACCESS EXCLUSIVE resumes after the rename and writes into `bars_legacy` | gemini (a) | V3:90 (activity check "refuse to start while `pg_stat_activity` shows any non-migration session on `bars`") | NOT CHECKABLE FROM READS — experiment: writer session waits on the lock, rename commits, writer resumes; which table does it hit (also with a prepared statement). E-14 (V3:200) has a blocked reader and "old connections see the new table"; a queued writer is not listed |
| 16 | v3 step 6 (rollback) names no lock, admission closure or activity check; step 3 (swap) names an activity query | astra F1 rollback, gemini | V3:93 vs V3:90 | HOLDS — text gap; whether a non-resident writer exists in the rollback window is an operational fact |
| 17 | No `statement_timeout` or admission fence in v3; `lock_timeout` covers lock waits (harness comment) | astra F6, grok | grep of `DERIVED-v3.md.part1/2` for `statement_timeout`, `admission`: 0/0; `mig:24-30` | HOLDS — text gap; that `lock_timeout` does not bound a running statement is PG behaviour (documented) — NOT CHECKABLE FROM READS, experiment: `SET lock_timeout='1s'` then a long `INSERT…SELECT` |
| 18 | §0 says nothing that renames, detaches or narrows a proof is reachable before E and R have PASSED; §3.9's E row says "before it has reported"; chunk 6's waits-for is items 1–2 rulings only; the closing paragraph gates the first DETACH on "his rulings + the restore drill" | astra F5 | V3:9; V3:131 ("has reported"); V3:143; V3:145 | HOLDS — DERIVED against itself: V3:9 "Nothing that renames, detaches or narrows a proof is reachable before E and the rehearsal R have passed" vs V3:145 "The first DETACH is chunk 6 (gated on his rulings + the restore drill)" |
| 19 | §3.3 keeps an MP4 path ("unless he rules §4 item 5a YES, and then only with both guards as in v2") but §3.9 has no chunk 1b row | astra F5 | V3:83; V3:128–144 (no 1b row; v2's had one, `DERIVED-v2.md` §3.9) | HOLDS — an MP4 path with no wait-condition row |
| 20 | E-5's fallback is "treat `COPY` as a bypass keyword (forces `--full`)"; v3 says a `DO` block with dynamic SQL evades a text scan | astra F4 | V3:191; V3:81 | HOLDS — text: a keyword scan is a widening rule (V3:81) and E-5's fallback relies on it |
| 21 | F-B: "a wrong SEALED price sits in the table from the commit until the post-deploy bracket ends"; no restoration procedure is written | astra F4 | V3:80 | HOLDS — no recovery step in V3:80 |
| 22 | F-B "does not say whether that bracket runs before residents restart" | grok (e) | V3:80 | DOES NOT HOLD — V3:80: "the full SEALED digest run OFF the outage immediately before the drain and immediately after the restart" |
| 23 | "§7's 820 MiB is table bytes only — sizing the gate from 820 MiB under-buys WAL/temp" | grok (a) | V3:238 ("both before WAL/temp"); V3:88 (gate = max(1.2 GiB, 1.5 × R's measured peak incl. WAL/temp)) | DOES NOT HOLD — v3 says "before WAL/temp" and sizes the gate from R's measured peak, not from 820 MiB |
| 24 | "PG16 does not inherit GRANTs onto partitions … a `cobalt_app` SELECT through the parent on a child with no GRANT is a missing-history read" | grok (a) | V3:90 ("grants re-applied and asserted on parent + open child") | NOT CHECKABLE FROM READS — experiment: as a role with SELECT on the parent only, select through the parent rows that live in a child with no GRANT. E-14 (V3:200) lists "grants" in the miniature swap; this exact case is not listed |
| 25 | "A leftover prepared statement would still see the old OID" | grok (a) | V3:200 (E-14 expected "after commit old connections see the new table") | NOT CHECKABLE FROM READS — experiment: prepared statement on a session opened before the rename, executed after; E-14 states the opposite expectation for old connections |
| 26 | REPLACED is "PK-ordered digest of `bars WHERE interval = 'i1'` equals the digest of `bars_p`, AND exact counts equal" — v3 does not name the row fold | grok (a) | V3:90; `migrate-proof.excerpt.py:75-87` (`_probe` folds `to_jsonb(t)` minus excluded columns, PK-ordered, no filter argument) | HOLDS as a reading — v3 says "digest" and reuses MP1's word; `_probe` takes no `WHERE`, so a filtered variant must be written; the fold's columns are not bound in the text |
| 27 | E-12: "one `executemany` and one `INSERT … SELECT` where ONE row has no partition → whole statement and transaction roll back"; astra: verify the store's context manager rolls back earlier executions | astra (E-12) | V3:198; `store:55–68` (`executemany`), `_connect` not staged | NOT CHECKABLE FROM READS — `_connect` (store.py ≤103) is not in the packet; experiment: `executemany` of 5 rows, the 4th unroutable, read back the table. E-12 lists both cases |
| 28 | E-9 / E-10 / E-13 expectations ("restart breaks equality"; "writer waits ≈ one child's digest"; "seconds ≈ 0") are not universal | astra | V3:195, 196, 199 | NOT CHECKABLE FROM READS — PG behaviour; each is its own experiment E-9 (restart, reset, crash), E-10 (two sessions), E-13 (30 children) |
| 29 | "Stopping non-i1 writes before the swap rehearsal is intentional"; 0b's switch defaults OFF and flips with the Lists edit | astra F5, grok (g) | V3:100, V3:145 | HOLDS — grok and astra agree; the switch is inert while OFF is a listed test (V3:148) |
| 30 | Grok and astra differ on a writer that commits after the activity check: grok — "finishes (its rows are in the copy) or … the swap aborts"; astra — its row is omitted from copy and digest | grok (a) vs astra F1 | rows 13–14 | Contradiction recorded, not decided: it turns on whether the LOCK or a snapshot comes first (V3:90 vs V3:236) and on RR snapshot semantics — row 13's experiment settles it |
| 31 | The step-6 rollback: a post-swap correction to an OLD timestamp is carried by the full upsert; a key only in legacy i1 stops it; a key only in new is inserted into legacy; legacy's non-i1 rows are untouched | grok (b), astra | V3:93; `store:55–68` (`DO UPDATE` of all five fields) | HOLDS — the code and the text agree; astra: "The i1-qualified anti-join does not confuse legacy's non-i1 rows" |
| 32 | U19's grep did not cover `ops/`, `dev_utils/` or the old tree | grok (b) | V3:220 | HOLDS — quoted from v3 itself |

Cross-check of v3's arithmetic where houses redid it: `ARITHMETIC OK` for every line below, hub steps in parentheses.
| line | steps | check |
|---|---|---|
| swap today, copy/proof subtotal | 8,834,532 ÷ 170,000 = 51.968 (×2 = 103.94); 5,281,313 ÷ 170,000 = 31.066; sum 135.002 | ARITHMETIC OK |
| + copy at 100,000 / 25,000 rows/s | 5,281,313 ÷ 100,000 = 52.813 → 187.815; ÷ 25,000 = 211.253 → 346.255 | ARITHMETIC OK |
| end-to-end at today's size | 149 − 106.8 = 42.2; 187.815 + 42.2 = 230.015 s (3.83 min); 346.255 + 42.2 = 388.455 s (6.47 min) | ARITHMETIC OK (astra); gemini 187.8 + 42 = 229.8 s (3.83 min) OK |
| +20 trading days | i1 5,281,313 + 5,330,820 = 10,612,133; legacy 8,834,532 + 5,330,820 = 14,165,352; 2 × 83.326 + 62.424 = 229.075 s; + 106.121 = 335.196; + 424.485 = 653.560; + 42.2 → 377.396 / 695.760 s (6.29 / 11.60 min) | ARITHMETIC OK |
| MP1 after the swap; + one hot week; 12 months | 5,281,313 × 2 ÷ 170,000 = 62.133; 1,332,705 × 2 ÷ 170,000 = 15.679; (5,281,313 + 266,541 × 252) = 72,449,645; × 2 ÷ 170,000 = 852.349 | ARITHMETIC OK |
| conditional scan examples | td × 266,541 × 2 ÷ 170,000 = 15.679 / 21.950 / 31.358 / 34.494 / 47.037 (td = 5, 7, 10, 11, 15) | ARITHMETIC OK (round 2 A1–A2 repeated) |
| AMBER; seal hold | 0.6 × 30 × 170,000 = 3,060,000; 1,332,705 ÷ 170,000 = 7.839 | ARITHMETIC OK |
| frozen-archive cost band | 8,834,532 × 2 = 17,669,064; ÷ 187,769 = 94.10; ÷ 165,782 = 106.58; ÷ 170,000 = 103.94 (grok's 103.9) | ARITHMETIC OK — 106.8 s is the measured figure (V3:230), not derived |
| disk | 1,438,171,136 ÷ 8,834,532 = 162.79 B/row; × 5,281,313 ÷ 1,048,576 = 819.9 MiB; × 10,612,133 ÷ 1,048,576 = 1,647.5 MiB | ARITHMETIC OK |
| 168.9 s | 106.8 + 62.1 | ARITHMETIC OK |

### Where a house says the design contradicts itself
- astra F5 — V3:9 "Nothing that renames, detaches or narrows a proof is reachable before E and the rehearsal R have passed" · V3:131 "nothing below that renames, detaches or narrows a proof may be scheduled before it has reported" · V3:143 (chunk 6) `first DETACH | **his rulings** §4 items 1–2 — until then nothing is detached` · V3:145 "The first DETACH is chunk 6 (gated on his rulings + the restore drill)."
- astra F1 / grok — V3:90 "in ONE harness transaction under `lock_timeout`: `LOCK TABLE bars IN ACCESS EXCLUSIVE MODE` → `INSERT INTO bars_p SELECT … FROM bars WHERE interval = 'i1'` … → the harness's NEW verdict **`REPLACED`**" (no before-probe) · V3:236 "before-probe 52.0 s + legacy-i1 digest 52.0 s + new digest 31.1 s = 135.0 s".
- grok P-swap — V3:141 (chunk 4 waits-for lists item 11, not 12) · V3:94 "This IS a narrowing of what the outage proves, so it is HIS (§4 item 12)" · V3:172 "**Desk: YES.** NO while it waits (MP1 covers it)."
- No house shows the design reaching a scoring, ranking or card-value path (L52 bar not triggered); grok's and astra's poller/gap sequences concern which label a minute carries and card freshness.

### Sequence ledger (the counts in the last line)
- **HOLD — 18:** gemini (d), (h) · grok P-span, P-closed, P-range, P-swap (item 12), empty export, `stopped_at`/ticker wording · astra F1-rollback, F2-1, F2-2, F3, F4-1 (E-5 fallback), F4-2 (F-B recovery), F5-1 (chunk 6 / §0), F5-2 (MP4), F6-1 (no run-time deadline), F6-2 (42.2 s).
- **DO NOT HOLD — 4 claims:** grok "F-B does not say whether the bracket runs before restart" (row 22) · grok "820 MiB under-buys WAL/temp" (row 23) · grok's step "`closed` includes 09:57" (row 5) · grok's replacement premise "at/after `stopped_at`" (row 7).
- **NOT CHECKABLE FROM READS — 9:** gemini (a) queued writer across the rename (row 15) · astra F1 cutover snapshot (row 13) · grok grants (row 24) · grok prepared statement / old OID (row 25) · astra E-12 rollback in the store's context manager (row 27) · astra E-9, E-10, E-13 expectations (row 28 — three) · `lock_timeout` vs a running statement (row 17). Chunk E lists none of gemini (a), grok's grants, grok's prepared-statement case or astra's snapshot race as such (E-14 is the nearest).

BARS TRIBUNAL ROUND 3 DONE · grok: RULING R3: BUILD v3 WITH 4 FIXES P-span P-closed P-range P-swap — builder may fold them without another round: YES · gemini: RULING R3: BUILD v3 WITH 3 FIXES (a, d, h) — builder may fold them without another round: YES · astra: RULING R3: BUILD v3 WITH 6 FIXES F1 F2 F3 F4 F5 F6 — builder may fold them without another round: YES · houses that ruled: 3 of 3 · r2 defects RESOLVED by their raiser: 22 of 25 · NOT RESOLVED: G-01, G-12, G-13 · new defects: 13 · sequences that HOLD against the code: 18 · dissents for the owner: 12 · NOT CHECKABLE: 9
