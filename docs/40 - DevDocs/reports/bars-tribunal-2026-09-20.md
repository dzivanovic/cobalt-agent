# Bars-lifecycle tribunal, round 1 — 2026-09-20 (hub `bars-tribunal-0920`)

## §0 Headline
- 3 of 3 houses ruled, all `BUILD WITH MY AMENDMENTS`; no point is 3-0 ACCEPT; T4, T5, T7, T9 are 3-0 AMEND; T1, T2, T3, T6, T8 are split. All three name the same missing step — a catch-up copy between the chunk-3 copy and the chunk-4 swap — and all three name chunk 4 as the most dangerous. Files: `scratch/tribunal-bars-0920/{grok,gemini,astra}-ruling.md`.
- §2.7's "15.7 s until ≈2,000 tickers/day": 3 of 3 houses say it does not hold; their arithmetic checks (≈2,010 is the 30 s/side point, 60 s both; 15.7 s both sides holds to ≈526 tickers/day at 507.3 rows/ticker/day; Grok also: 1,062 tickers at 960 rows/ticker/day). Astra rules daily partitions; Gemini and Grok keep weekly.
- Two houses' claims about today's code are FALSE (both Gemini: poller "crash", `heartbeat/probes.py:273` "reads i5"); 11 claims NOT CHECKABLE FROM READS, each with its experiment. R9 RISK raised: 0 (Grok wrote `R9 RISK: none …`).
- Card reach (L52 note): no house says the design touches scoring, ranking or card value; Grok (T2, T6) argues it reaches the card's INPUT — a missing partition leaving stale minutes on cards, a derived i2 that differs from the trader's chart — recorded under `## Checked against the files`.
- ESCALATE: 0 (no FAILED, no HARNESS/METER/TIMEOUT; the Fable seat's ruling and the derived FINAL are the desk's next step).

## PREFLIGHT
Authorization verified from the committed record (`git -C /Users/cobalt/cobalt log`): `cto-2026-09-20.md` log shows `8ea21a6`, `2079acc`, `dd7e9a7`, `a6cc75c`, `4f52276`, `9067d2a`; rows `R9` and `R9 (extended)` present (lines 23–24); `cto-2026-09-18.md` log shows `8f2597a`, `243aa65`, `0158028`, …; rows `R9`, `R15`, `R17`, `R18`, `R21` present (lines 22, 28, 30, 31, 34); `cto-2026-09-19.md` rows `R1`, `R8` (pointer; full row line 194), `R10`, `R15` present. Record matches the prompt.

| rule | command | exit | result |
|---|---|---|---|
| `Bash(grok *)` | `grok --version` | 0 | allowed — `grok 1.0.25 (f7e67d6988e2) [stable]` |
| `Bash(agy *)` | `agy --version` | 0 | allowed — `1.2.7` |
| `Bash(date*)` | `date` | 0 | allowed — `Sun Sep 20 13:34:07 EDT 2026` |
| Codex read-only rule | `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` (background) | 0 | allowed — answered `OK`, no usage-limit text, 2,277 tokens → **astra: UP** |
| `Bash(mkdir -p scratch/tribunal-bars-0920)` | `mkdir -p scratch/tribunal-bars-0920` | 0 | allowed (recovery `ls` first: folder absent → fresh run) |

L74: no tool result carried an instruction block during this run. (Recorded once.)

## Packet
Folder `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/` (Read → Write, byte counts checked with `wc -c` against the originals):

| file | source | bytes / lines | check |
|---|---|---|---|
| `BRIEF.md.part1` + `BRIEF.md.part2` (**staged in two ordered parts — the Write tool would not take 69 KB in one call**; every launch line says "read them in order as one file") | `docs/30 - Design/bars-lifecycle-brief-2026-09-20.md` | 51,880 + 17,617 = **69,497** / 452 + 153 = **605** | equals the original 69,497 / 605 — MATCH |
| `desk-notes.md` | `prompts/2026-09-20/04-packet/desk-notes.md` | 3,607 / 21 | MATCH |
| `owner-rulings.md` | rows R9, R9 (extended) of `cto-2026-09-20.md` §4; R15, R17 of `cto-2026-09-18.md` §4; the FULL R8 row of `cto-2026-09-19.md` (line 194, under §14) | 7,086 / 15 | rows copied from `grep` output, verbatim |
| `poller.py`, `replay.py`, `anatomy-bars.py`, `aggregate.py`, `models.py`, `archiver-store.py`, `clock.py`, `0001_bars.sql` | `src/cobalt/radar/poller.py`, `radar/replay.py`, `radar/anatomy/bars.py`, `archiver/aggregate.py`, `archiver/models.py`, `archiver/store.py`, `session/clock.py`, `archiver/migrations/0001_bars.sql` | 4,981 / 5,931 / 5,559 / 1,568 / 1,658 / 14,076 / 12,394 / 1,347 | each MATCHES its original |
| `radar-store.excerpt.py` | `src/cobalt/radar/store.py` lines 290–380 (header line names path and range) | 4,202 / 92 | excerpt |
| `migrate-proof.excerpt.py` | `src/cobalt/db_migrations/cli.py` lines 250–440 (header names path and range) | 7,601 / 192 | excerpt |
| `readers-grep.txt` | the two `grep` commands of the prompt, full output under each command line; says `grep` honours `.gitignore`. The `'i1'` search returned **2** lines, the first search **10** | 1,856 / 18 | as run |
| `lists-archive-fields.md` | `Radar Lists.md`: each `archive:` key, list items, tier name only (no ticker lists, L32) | 1,052 / 32 | as run |
| `finviz-windows.md` | `tribunal-archiver-r3-0919/finviz-windows.md` | 5,303 / 83 | MATCH |
| `archiver-dissents.md` | `TRIBUNAL-R3.md` section `## Dissents for the owner, verbatim` (line 318 to end of file, which includes that file's own last `TRIBUNAL ROUND 3 DONE …` line) | 2,869 / 25 | section as it stands |
| `QUESTIONS.md` | the prompt's QUESTIONS.md block, verbatim | 5,109 / 1 | verbatim |

Launch (all three together ~13:43 ET, `run_in_background`, one attempt each, spellings of `01-review-harness.md` §2.1–2.3 with this folder and output names; Astra/Gemini prompts say "ruling" where the harness says "findings"; the "BRIEF.md is split into ordered parts" sentence added): Grok task `bavsf8kr6` (`--sandbox cobalt-job`, `--allow Write(…/tribunal-bars-0920/**)`, wrote `grok-ruling.md` itself); Gemini task `bnii0y231` (hub wrote `gemini-ruling.md`); Astra task `bdtz0au2v` (`-s read-only`; hub wrote `astra-ruling.md`).

House rows, as they landed:
- **gemini** — 13:45 ET (~2 min), exit 0. Printed answer written byte for byte (the tool's `[exited with code 0]` marker is not part of it). Closing line: `RULING: BUILD WITH MY AMENDMENTS T1, T4, T5, T7, T8, T9`.
- **astra** — 13:46 ET (~3 min), exit 0, 66,052 tokens, no usage-limit text. The Codex transcript echoes every file it read; its final answer (printed twice, identical) written byte for byte. Closing line: `RULING: BUILD WITH MY AMENDMENTS T1 T2 T3 T4 T5 T6 T7 T8 T9`.
- **grok** — 13:52 ET (~9 min), exit 0; wrote `grok-ruling.md` and replied with its path. Closing line: `RULING: BUILD WITH MY AMENDMENTS T2 T3 T4 T5 T6 T7 T9`. Its transcript says it first read "the required memory files" (outside the packet folder; L44 entitles that); nothing in its ruling rests on a fact not in the packet or in the laws the brief names.

## Rulings table
`A` = ACCEPT, `M` = AMEND, `R` = REJECT.

| point | grok | gemini | astra | agreement | the amendment(s) in ≤25 words each |
|---|---|---|---|---|---|
| **T1** partitioning | A (P3 weekly) | M | M | split 1 A / 2 M | Gemini: P3 wording — proof scales linearly with ticker count; keep weekly. Astra: use DAILY ET-midnight bounds; partition width bounds rows per partition, not total proof work. |
| **T2** no partition at 04:00 | M | A | M | split 1 A / 2 M (all keep F2, no DEFAULT) | Grok: "no partition" aborts the poll cycle; horizon probe Fri 20:30 and at radar start; create-ahead at deploy/boot. Astra: verify contiguous coverage; ensure-partitions op plus range reconciliation. |
| **T3** migration proof | M | A | M | split 1 A / 2 M | Grok: MP1 until P3; MP4 only with `(relfilenode, n_tup_ins/upd/del)` guard, `--full` stays. Astra: MP1 default; MP2 only with a sealing protocol; MP4 needs owner authorization. |
| **T4** how the rows leave | M | M | M | **3-0 AMEND** | All keep D4 and add a catch-up copy before the swap (Gemini: final `INSERT` in the lock; Grok: `ts > copy_watermark`/anti-join; Astra: change capture incl. updates, drain, verified delta). |
| **T5** readers/writers | M | M | M | **3-0 AMEND** | Gemini: add `heartbeat/probes.py:273` to §2.6a. Grok: "zero runtime readers" false until chunk 0; refuse `interval != i1`. Astra: not established; `CHECK(interval = 'i1')`. |
| **T6** derived i2 vs vendor | M | A | M | split 1 A / 2 M | Grok: run `aggregate.py` on the 52 keys; compare one bar with DAS. Astra: describe as measured overlap agreement, keep exception evidence, reconcile with the chart. |
| **T7** i1 as single source | M | M | M | **3-0 AMEND** | Gemini: timezone-aware DST bounds. Grok: gap probe skips the open minute; test 2026-11-01 and 2027-03-14. Astra: four-state gap classifier; both DST fixtures; early-close tests. |
| **T8** growth | A (G1) | M | M | split 1 A / 2 M | Gemini: print rolling 5-day distinct active tickers; act near 1,500. Astra: scenarios not findings; print projected end-of-period proof seconds across all writable partitions. |
| **T9** build order | M | M | M | **3-0 AMEND**; most dangerous chunk: **4 (the swap), 3 of 3** | Gemini: move chunk 7 earlier; catch-up in chunk 4. Grok: coverage/gap/disk gates before chunk 3. Astra: verify readers and writers, rehearse copy/cutover/rollback before any swap. |
| **MISSING** | present | present | present | catch-up copy before swap: 3 of 3 | Grok: 8 items. Gemini: 1 item. Astra: 8 items (partition lifecycle, adversarial proof tests, cold-file metadata, coverage evidence …). |
| **RULING line** | BUILD WITH MY AMENDMENTS T2 T3 T4 T5 T6 T7 T9 | BUILD WITH MY AMENDMENTS T1, T4, T5, T7, T8, T9 | BUILD WITH MY AMENDMENTS T1 T2 T3 T4 T5 T6 T7 T8 T9 | 3 of 3 "BUILD WITH MY AMENDMENTS" | — |

§2.7 arithmetic row (the brief's claim: a weekly partition holds the open-partition proof at 15.7 s until ≈2,000 tickers/day):

| house | verdict | its steps (arithmetic checked under `## Checked against the files`) |
|---|---|---|
| grok | **BREAKS AT 1,062 tickers/day** (960 rows/ticker/day); the 2,010 algebra holds only as the 30 s/side point | 1,332,705 ÷ 170,000 × 2 = 15.678 s (holds today); 30 s/side → 5,100,000 rows → 1,020,000/day → ÷ 507.3 ≈ 2,010; ÷ 960 = 1,062 |
| gemini | **BREAKS AT 2,000 tickers/day** | 2,000 tickers → 5.07 M rows/week → 59.7 s both sides |
| astra | **BREAKS AT 2,000 tickers/day** | 2,000 × 507.3 × 5 = 5,073,000 rows → 59.682 s; 15.7 s both sides holds to ≈ 526 tickers/day |

## Amendments and rejections, verbatim
Each house's own replacement text, unedited, in point order. Full rulings including every objection and scenario: `scratch/tribunal-bars-0920/grok-ruling.md`, `gemini-ruling.md`, `astra-ruling.md`. No house REJECTED a point.

### grok
R9 RISK (verbatim): `R9 RISK: none on the live card path (poller/store/replay are i1 already). Residual is T6's three bars, not a reason to keep stored i2.`

T1 — ACCEPT P3 (no replacement): "Weekly RANGE(`ts`), ET-aligned, width revisable forward. Bounds must be `timestamptz` at `America/New_York`, never a numeric offset (T7)."

T2 — AMEND F2. Objection: "the 04:00 poller does not fail loud. `poller.py:106-115` catches `BaseException`, marks the ticker `error`, and `continue`s. Monday 2026-10-12 04:00 ET, week-N partition missing, NVDA insert raises `no partition of relation "bars" found`, every subsequent ticker fails the same way, `stopped_at` is the last name, cards render Friday's last minute as live."
Replacement: "F2 plus (1) treat "no partition of relation" as a cycle-abort (raise like `StageDropped`), not a per-ticker continue; (2) horizon probe at Friday 20:30 `market_reset` and at radar start, so Monday 04:00 never discovers the gap; (3) create-ahead is also a deploy/boot step, not only a cron."

T3 — AMEND MP4/MP2/MP1. Scenario: "migration 0012 `ALTER`s `radar_score_run` and a `DO` block runs `UPDATE bars SET volume = 0 WHERE ticker = 'NVDA'`; 960 NVDA minutes go to 0; MP4 prints OK; he sizes off zero volume."
Replacement: "MP1 until P3 lands; MP2 once partitioned; MP4 only if the unnamed-table guard is equality of `(relfilenode, n_tup_ins, n_tup_upd, n_tup_del)` before/after — never `reltuples` — and `--proof-only --full` stays. A DML-counter move forces a content digest of that table in the same run."

T4 — AMEND D4. Objection (2): "Chunk 3 copy and chunk 4 swap are separate. Friday 21:00 copy of 5,281,313 i1 rows; Monday 04:00–20:00 poller writes ~266 k i1 rows to **old** `bars`; Tuesday swap; Tuesday 04:00 NVDA cards missing Monday's minutes."
Replacement: "D4 plus a catch-up under L66 immediately before rename (`interval='i1'` anti-join on PK, or `ts > copy_watermark`); swap refused while `pg_stat_activity` shows any non-migration writer on `bars`; disk free ≥ 1.2 GiB is a hard gate; `bars_legacy` is not dropped by this migration."

T5 — AMEND. Replacement: "chunk 0 first; keep the `Interval` enum (aggregate labels derived bars); after D4, `upsert_bars_on` / `insert_new_bars` refuse `interval != i1` fail-loud (CHECK on the new parent is the DDL form). Do not delete enum members."

T6 — AMEND. Replacement: "still derive i2 from i1 (R9). Before D4, run `aggregate.py` (not the SQL fold) against the 52 keys and print all five fields. `working_bars` already flags incomplete buckets; a complete bucket that still disagrees with vendor i2 must be listed, not averaged away. Do not claim the derived bar is the one he trades until one of those three prints is compared to DAS."

T7 — AMEND. Replacement: "gap probe as above (chunk 8 before D4); partition bounds via `America/New_York` with tests on 2026-11-01 **and** 2027-03-14; half-day test against the clock now, live re-verify 2026-11-27; add `premarket_only` / `after_hours_only`; D4 waits if the 584→337 drop is loss rather than archive lag."

T8 — ACCEPT G1 (no replacement). Its print list: "Deploy must print: `bars_open_partition_rows`, `bars_proof_s` both sides, `bars_rows_per_day` (last 5 td mean), `bars_distinct_tickers_today`, `bars_future_partitions`. Act when open-week rows approach ~3.4 M (20 s/side at 170 k), not when someone counts tickers."

T9 — AMEND. Replacement order: "0 lists `[i1]` → coverage+gap+vendor-window remeasure+disk → (MP4 only if he rules the T3 guard) → chunk 2 horizon/DST/no DEFAULT → chunk 3 online i1 copy → L66 catch-up → chunk 4 swap, `bars_legacy` kept → chunk 5 MP2 → retention later. Chunk 7 derivation helpers parallel from today."

### gemini
T1 — "Exact replacement wording for P3 benefit: "open partition ≈ 1,332,705 rows today → bounded proof 15.7 s both. Proof scales linearly with ticker count; width revisable per period without touching history.""

T4 — "Exact replacement wording for D4: "D4 — fold the deletion into the partition copy, but require a final catch-up `INSERT` inside the swap's ACCESS EXCLUSIVE lock to prevent intraday poller data loss.""

T5 — "Exact replacement wording for the missing site in §2.6a: "`heartbeat/probes.py:273` | vendor window limit | assumes 21 days for `i5` | **YES** — will fail to warn before i1's 14-day window closes.""

T7 — "Exact replacement wording for the DST row in §2.6h: "DST transition | Yes | The next is 2026-11-01. ET-aligned partition bounds must be written using timezone-aware datetimes (e.g., `America/New_York`), allowing Postgres to natively calculate the 169-hour week.""

T8 — "Exact replacement wording for G1 warning sign: "The rolling 5-day average of distinct active tickers archived per day, printed at deploy. When this metric approaches 1,500, trigger the partition width reduction.""

T9 — "Exact replacement wording for Chunk 4: "4 | The swap — final catch-up `INSERT` of uncopied rows inside an ACCESS EXCLUSIVE lock, then two renames. Sub-second. `bars_legacy` kept until he says drop.""

### astra
T1: "Use native RANGE(ts) with daily, half-open bounds generated from consecutive America/New_York calendar midnights. Future widths remain revisable. Partition width bounds rows per partition, not total proof work: every writable or invalidated partition must be read. Treat throughput as a provisional model and benchmark the complete proof, including catalog and ledger checks. Do not claim constant cost as daily coverage grows. Weekly remains a possible later width if measured costs support it; the arithmetic does not establish that daily construction doubles the build."

T2: "Keep F2: pre-create a configured horizon without DEFAULT. Verify contiguous timestamp coverage, including the current period, rather than counting children. Classify missing-partition failures separately, expose affected tickers and ranges, and provide an idempotent ensure-partitions operation followed by explicit reconciliation of failed ranges. Test restart, missed maintenance, concurrent creation, old backfills, future timestamps, and transactional batch failure. Do not describe DEFAULT as silent data loss: it preserves rows but requires monitoring and evacuation."

T3: "Retain MP1 as the default pending the owner’s scope ruling. Implement MP2 only with an explicit sealing protocol: drain writers, enforce closure across parent and direct-child access, separate routine roles from ownership and privileged maintenance, and atomically record the content digest, exact count, partition bounds, schema and generation. Late writes and repairs invalidate the seal and require controlled reopening and resealing. Digest every writable or invalidated partition. Validate partition membership and effective access on every proof. Version the partition-manifest proof separately; preserve the original full proof for historical comparison. Report CONTENT_VERIFIED, SEALED_BASELINE_TRUSTED and NOT_CONTENT_VERIFIED distinctly. MP4 requires explicit owner authorization and must never print “content UNCHANGED on every table” for skipped content."

T4: "Keep D4 as the migration method, but distinguish exclusion from the new table from physical deletion of legacy data. Establish transactional change capture before taking the copy snapshot; capture updates as well as inserts, and deletes if any writer permits them. Copy i1 in resumable batches, replay captured changes in order, then stop and drain all writers, apply the final delta, and verify source-to-target equality at a common fence. Acquire cutover locks with bounded waits; abort safely if unavailable. Swap atomically, restore grants and dependencies, recycle connections, and verify the production write path. Keep legacy data until owner-authorized disposal. After writes resume, rollback requires reverse reconciliation; two renames alone are insufficient. Size headroom for legacy, target, indexes, WAL, temporary files, retained changes and continuing ingestion."

T5: "State that the staged evidence supports i1-only live radar reads, not zero non-i1 runtime consumers. Change enabled archive lists to [i1], explicitly activate the new configuration, and verify effective targets. Constrain every storage writer and repair command to i1 and add a database CHECK(interval = 'i1') on the replacement table. Preserve wider Interval members for derived outputs. Specify default-backfill precedence, handle historical progress rows, and update smoke and documentation before relying on the new behavior. The fetch-list edit alone is not completion of the future-write prohibition."

T6: "Derive stored-interval replacements exclusively from i1 as ruled, but describe vendor equivalence as measured overlap agreement with unresolved exceptions. Preserve the exception evidence before disposal and reconcile it against the trader’s actual chart. All trading-facing derivation must use the closure and completeness checks around the shared aggregate function, with explicit session selection and source provenance. Do not claim universal exact reproduction, correctness from a wider range, or reconstructibility before each ticker’s available i1 history."

T7: "Use SessionClock for every session label and both endpoints of a derived bucket. Replace the binary gap classifier with observed, confirmed-no-trade, ingestion-failure and unknown states supported by acquisition evidence; absence of an i1 row alone remains unknown. Track expected ticker coverage, fetch outcomes, returned ranges, persistence outcomes and catch-up completion. Keep incomplete working bars visibly flagged and unavailable to detectors. Test 2026-11-27 and 2026-12-24 early closes; both DST transitions, using 2026-03-08 and 2026-11-01 fixtures; all session endpoints; holidays; missing calendar years; and equivalent aware timestamps expressed in different zones. Reverify half-day behavior live."

T8: "Treat flat, expanding and saturating active coverage as scenarios, not findings established by five days. Distinguish membership arrivals, actively fetched tickers, archived tickers, onboarding timestamps and earliest bar timestamps. Recommend no ticker ceiling, subject to the owner’s decision, and daily partitions under T1. Every deploy must print actual proof seconds and projected end-of-period proof seconds across all writable partitions, with rows scanned, forecast rows and measured throughput. Also report coverage deficits, seal backlog, partition horizon and disk exhaustion forecast. Capacity decisions must include cold files and WAL; retention bounds hot history only."

T9: "First complete reader/writer and default-path verification, prepare i1 enforcement, and activate the authorized fetch-list change without deleting data. Next build derivation/session tests, coverage instrumentation, partition maintenance and the revised sealing/proof protocol. Rehearse transactional copying, final reconciliation, cutover, restart and rollback at production scale before any production swap. Keep the full proof unless the owner rules otherwise. Perform owner-authorized retention only after export durability and restoration have been demonstrated. Update documentation and smoke alongside each behavior change. No deletion occurs before the owner’s post-tribunal ruling."

## Advice on the owner's six rulings
Each house's one-line recommendation and harm, verbatim; the hub adds none.

| item | grok | gemini | astra |
|---|---|---|---|
| 1. i1 retention period | "**Retention:** 90 calendar days hot. 30 days: lost bars — he cannot replay last month's NVDA day after a rule change, vendor i1 is ~14 calendar days (finviz-windows.md, MSFT 2026-08-13 04:00 → 08-27, last measured 2026-08-27, not re-verified). 365/forever: a slower night and a deploy outage that grows to 852 s unpartitioned at 12 months." Also: "Retention is the irreversible one. Re-measure the vendor window before he picks a number (`UNVERIFIED — export_oldest on NVDA i1 today`)." | "Recommendation: 365 calendar days. Harm: A shorter window destroys your ability to re-run counterfactuals over a full seasonal cycle; a longer window guarantees a slower night and a red dashboard from proof timeouts." | "Recommend preserving recoverable i1 history indefinitely for now; an undersized period loses old bars and makes historical counterfactuals impossible. **UNVERIFIED — remeasure the reported approximately 14-calendar-day vendor window, last measured 2026-08-27.**" |
| 2. DETACH to cold file or DROP | "**DETACH to cold file, never DROP.** DROP: those bars are gone when he wants them; vendor will not re-serve i1. DETACH costs disk (`UNVERIFIED — df`) and half a chunk; wrong choice the other way is only a slower night." | "Recommendation: DETACH to a cold file. Harm: DROP means permanently lost bars since Finviz never re-serves past 14 days, making the retention limit completely irreversible." | "Recommend verified cold export with tested restoration and a separate durable copy; an unreadable file beside a failed database disk means permanently lost bars." |
| 3. Ceiling on the stored ticker set | "**No ceiling on the stored set (G1).** A cap: the name he actually traded is the one not stored — lost bars, 14-day window already closed, a red dashboard when replay has no series." | "Recommendation: No ceiling (G1). Harm: Capping the active list means a ticker you later want to study will have no history stored, permanently blocking analysis (lost bars)." | "Recommend none; the wrong ceiling omits the name he later wants to study, while insufficient capacity planning causes slower nights." |
| 4. Repair seam A / B / D | "**D for closed partitions, A unchanged for the open week, do not build B.** B: a bug in the poller write path is a red dashboard and a dead radar at 04:00. A-only on last month's repair: Astra's overwrite, wrong prices on a reviewed correction. D-without-A: same overwrite on this week's bars." | "Recommendation: D for closed periods, A for the open period. Harm: B introduces live-radar outage risk at 04:00; A alone risks wrong prices when a reviewed correction is blindly overwritten by a stale poller thread." | "Recommend B with transactional exclusion and generation validation; A remains his current ruling, while D alone neither protects open-period prices nor preserves reader availability." |
| 5. May the proof narrow its scope | "**Narrow the proof only with the T3 DML-counter guard; `--full` stays.** Bare MP4: wrong prices pass the deploy. Refusal: every deploy keeps a 106.8 s outage that grows." | "Recommendation: Yes (MP4). Harm: Rejecting it guarantees every unrelated deploy incurs a 106s outage, increasing the risk of a deploy outage in seconds without proportional benefit." | "Recommend no MP4 authorization as written; shortening a deploy by trusting catalog metadata can leave wrong prices undetected." |
| 6. May a permanent derived rollup exist | "**No permanent rollup.** It fails his own test (not dissectable into i1/i2). Yes: wrong prices on a year-old number, not replayable (L57). No: last-year questions go to cold files — slower research, not a red dashboard." | "Recommendation: No. Harm: Creating a second derivation path risks silently wrong prices if the logic ever drifts, fundamentally violating your i1-only mandate." | "Recommend no exception now; it cannot replace dissectable i1 history, and stale derivation definitions can preserve wrong prices." |

## Carried dissents
Statuses and sequences verbatim (D1 = Gemini on the repair seam; D2 = Astra on the repair seam; D3 = Astra, mixed prices after a vendor restatement).

| dissent | grok | gemini | astra |
|---|---|---|---|
| D1 | "**STILL OPEN** on the open week, **ANSWERED** for closed periods if D lands. Sequence: last poll cycle looks idle, one Finviz fetch is still in flight, quiet window opens, `restate --apply` commits NVDA 04:00 close B, stuck fetch returns A, `upsert_bars` DO UPDATE writes A over B (`poller.py:64` hook is optional; `archiver-store.py:29-33` lock is not taken by the poller). D puts last month's rows off `bars`; it does not cover this week's child." | "STILL OPEN. Option A does not prevent a delayed poller thread from overwriting a repair after the quiet window ends (Astra's sequence 03:59:50), and the brief's Option D only covers closed partitions, leaving the open period exposed to overwritten corrections." | "STILL OPEN. A poller fetch holds old NVDA data; repair commits corrected data; the delayed fetch then upserts the old values. The optional hook in `poller.py:103` supplies no demonstrated generation exclusion. Detaching a closed partition does not settle a response that commits after reattachment, or an open-period repair." |
| D2 | "**STILL OPEN** on the same in-flight hole; the 03:59:50 start-time example is the sequence A was built to refuse (repair <10 min before 04:00). `quiet.py` is not staged — `UNVERIFIED — that the 10-minute bound actually fires`. A start-time check still lets a fetch started at 03:50 land at 04:00:20 after B is committed." | "STILL OPEN. The live poller still takes no archive lock, so a repair transaction executed before scanning opens can still be silently corrupted by an in-flight poller write." | "STILL OPEN. An admitted repair overruns its anticipated quiet window; scanning begins and fetches old data; repair commits; the poller writes afterward. The brief's 03:59:50 example should be refused by A's stated opening margin, but an earlier admitted repair that overruns preserves the objection. A time margin is not enforced exclusion." |
| D3 | "**MADE WORSE**, and the brief is right. Sequence: NVDA restates 2026-09-18 10:00 i1 close 141.20 → 141.00; append leaves 141.20; poller overlap DO UPDATE writes 141.00 on the last ~5 minutes; older minutes stay 141.20; card at 10:05 mixes; no i5/i30 twin to see the jump; red dashboard does not stop the mix. Cheapest honest mitigation: L9 degrade that ticker on a `restated` incident; only A quiet `restate --apply` may correct stored bars; poller overlap may DO UPDATE only `ts >=` that day's `premarket_open`. Do not invent an i5 cross-check. Do not build full B for this." | "MADE WORSE. By dropping i5/i30, we lose the wider-interval cross-checks. Since the archiver moves to append mode, it cannot heal past restatements. Cheapest mitigation: run a nightly `restate --apply` strictly over the active ticker list for the past 14 days." | "**MADE WORSE in observability, with the original correctness defect still open.** A vendor restates NVDA history; append refuses divergent history; the unchanged poller writes adjusted recent minutes beside older unadjusted prices. Removing other intervals removes possible comparison evidence, although those exports were never independent truth. The cheapest honest mitigation is a per-ticker integrity state, retained divergence evidence and suppression of affected price-derived outputs until reconciliation. Preventing continued mixed writes additionally requires a write guard; a red dashboard alone does not repair prices." |

Also carried (Astra, verbatim): "The separately staged Grok half-day freshness objection is also not answered by finer bar granularity: a shorter session can still trip an export-freshness rule comparing against a previous full session. Its current status requires the unstaged archiver guard implementation."

## Checked against the files
Files = staged copies (identical to main, byte counts above) or the real files on main; `part1:N` / `part2:N` = `BRIEF.md.part1` / `part2` line N (same numbering as the brief). No database query was run.

| # | claim | who | file:line | verdict |
|---|---|---|---|---|
| 1 | The poller catches the per-ticker upsert exception, records an `error` failure and `continue`s; only `StageDropped` is re-raised | Grok, Astra | `poller.py:104–115` | TRUE |
| 2 | A missing partition makes the poller "crash" | Gemini T2 | `poller.py:104–115` | **FALSE** — the exception is caught (:106) and the loop continues; the bar is not written that cycle (TRUE) |
| 3 | A bar not written this cycle is (or is not) refetched next cycle — "lose the minute" / "creating the partition later does not recover missed bars" | Gemini, Astra | `poller.py:96–102` (threshold = watermark − `overlap_bars`; `overlap_bars` is config, not staged) | NOT CHECKABLE FROM READS — experiment: read the production `overlap_bars` value and replay a missed minute on `cobalt_dev` with the partition created afterwards |
| 4 | A future-dated export is filtered at `poller.py:100`; older timestamps pass when there is no watermark | Astra | `poller.py:98–102` | TRUE |
| 5 | The 04:00 bar is not closed at 04:00:30 (`bar.ts + 1 min <= now`) | Grok | `poller.py:99–101` | TRUE |
| 6 | The `before_commit` hook is optional; the poller takes no archive lock; nothing validates a repair generation | Grok, Gemini, Astra | `poller.py:64, 96–105`; `archiver-store.py:28–34` | TRUE |
| 7 | `upsert_bars_on` is `DO UPDATE`; `insert_new_bars` is `DO NOTHING` | Grok | `archiver-store.py:158–170, 264–269` | TRUE |
| 8 | Nothing forces `interval = 'i1'`: `0001_bars.sql` has no CHECK, the enum has five members, the poller hardcodes `Interval.I1` | Grok, Astra | `0001_bars.sql:18–28`; `models.py:22–26`; `poller.py:88` | TRUE |
| 9 | `bars_in_range` reads whatever interval it is given; tier_a fetches `[i1,i2,i5,i15,i30]`, tier_b `[i1,i5,i30]` | Grok | `archiver-store.py:283–346`; `lists-archive-fields.md` | TRUE (callers not staged) |
| 10 | `readers-grep.txt` hits are the enum, comments and a `SequenceMatcher` false positive; the search excludes tests, docs and the vault | Grok, Astra | `readers-grep.txt:1–3`; `models.py:23–26`; `vaultwrite/merge.py:87–95` | TRUE |
| 11 | `heartbeat/probes.py:273` "reads i5 conceptually", "assumes 21 days for i5", "will fail to warn" | Gemini T5 | `heartbeat/probes.py:261–304` (docstring); `grep -n "21"` hits only :273 and :473 | **FALSE** as to behaviour — the words "i5 ≈ 21 days" sit in the docstring of `archiver_freshness`; the code reads no bars and holds no 21-day constant. TRUE that the text exists at :273 |
| 12 | The brief gives two different defaults for `backfill-missing` (i1 vs the `backfill_default` list) | Gemini, Astra | `part1:318` vs `part1:360`. Code: `archiver/cli.py:336–341` `_intervals_for` = given interval, else `archive_progress` rows, else `[I1]`; the Lists `backfill_default` block is read by `runner.py:451` and `radar/sources.py:70–79`. The brief's §2.6a table names `runner.py:354`, not `:451` | TRUE (brief contradicts itself; the CLI path is `cli.py:341`, the Lists path is `runner.py:451`) |
| 13 | `restate` / `backfill-missing` accept any `Interval` member as an explicit argument | Astra | `archiver/cli.py:467, 479` | TRUE |
| 14 | `aggregate()` emits whatever rows it is given; `working_bars` is the wrapper that flags missing minutes; the brief says "The derivation layer already refuses to fabricate a partial bar" | Astra | `aggregate.py:14–45`; `anatomy-bars.py:3–17, 87–130`; `part1:245` | TRUE |
| 15 | Deleting enum members breaks `aggregate()` (`Interval(f"i{minutes}")`) | Grok, Astra | `aggregate.py:17–20` | TRUE |
| 16 | `aggregate.py` floors on an ET-converted value; the brief's SQL floors on UTC epoch; "false on a DST day" | Grok | `aggregate.py:11, 23–28`; `part1:185` | NOT CHECKABLE FROM READS (forms differ — TRUE; results differ — no example given; both use minute-of-hour after whole-hour ET offsets). Experiment: run `aggregate()` and the SQL fold over i1 rows of a spring-forward and the 2026-11-01 week on `cobalt_dev` and compare |
| 17 | `_probe_all` content-digests every table in MOVED+SEEDED+CREATED; `_verdict` compares only the before/after it is handed | Grok, Astra | `migrate-proof.excerpt.py:96–98, 105–122`; `db_migrations/cli.py:83, 345, 386` | TRUE |
| 18 | "The harness already knows every table each registered migration names" | Astra disputes | brief `part1:288`; `db_migrations/placement.py:26, 44, 64, 152, 164` (table→side dicts, `side_of`, `tables_on`); no migration→tables mapping in `cli.py` or `placement.py` | NOT CHECKABLE FROM READS — experiment: grep the rest of `src/cobalt/db_migrations/` and the migration registry for a migration→tables mapping |
| 19 | On an early-close day AFTERMARKET is [13:00, 17:00), MARKET_RESET [20:00, 21:00), so 17:00–20:00 is OVERNIGHT; 2026-11-27 and 2026-12-24 are the early closes | Grok, Astra | `clock.py:196–218, 222–228`; `tunables.yaml:266–315`; `nyse-2026.yaml:59–63` | TRUE |
| 20 | 04:00 is inside premarket (start inclusive); 20:00 is market_reset, not a bar | Grok | `clock.py:222–228`; `tunables.yaml:239–293` | TRUE |
| 21 | `rth_only` is the only session selector; premarket / after-hours siblings do not exist | Grok | `anatomy-bars.py:133–139` | TRUE |
| 22 | The §2.7 first-seen-by-week query uses `min(ts)` of `bars`, not an ingestion time; the membership query uses `min(trade_date)` | Astra | `part2:7` (bars query, `min(ts) AS t0`); the membership query with `min(trade_date)` is in part 1's last lines | TRUE |
| 23 | The daily-partition row says "252 partitions/year, 730 at 2 years" for a calendar-day partition | Astra | `part1:157` | TRUE (the brief is internally inconsistent: 252 trading days vs 730 = 2 × 365) |
| 24 | In EDT, 16:00–20:00 ET = 20:00–24:00 UTC (ends at midnight); in EST it is 21:00–01:00 UTC (crosses); the brief says "20:00–00:00 UTC, so a UTC-midnight bound splits a session" | Astra | `part1:148` | ARITHMETIC OK (offsets −4/−5); the brief's sentence is TRUE for EST only |
| 25 | The brief has no catch-up / delta step between the chunk-3 copy and the chunk-4 swap (chunk 3 says "verified row-for-row against `bars_legacy`"; chunk 4 "two renames") | Gemini, Astra, Grok | `part2:90–91` (§3 table); `grep -i "catch-up\|delta"` over both parts: no hit | TRUE |
| 26 | The brief's table row "500 (today) \| 1.33 M \| 15.7 s"; 1,332,705 = 5 × 266,541 ≈ 525 names at 507.3, not 500 | Grok | `part2:54` | TRUE (line exists); ARITHMETIC OK: 500 × 507.3 × 5 = 1,268,250 → 14.92 s both |
| 27 | Brief line references: `part1:22` ("stays 15.7 s at 10 M rows or at 100 M"), `:24` (§2.7 claim), `:318`, `:323`, `:360`, `part2:57` (12.68 M rows → 149 s) | Gemini | as listed | TRUE (lines exist as quoted; whether §0 item 8 (table rows) contradicts the part2:57 row (open-week rows) is the house's reading) |
| 28 | `radar-store.excerpt.py:45` and `replay.py:136` filter `interval = 'i1'`; `poller.py:88` fetches `Interval.I1` | Grok | as listed | TRUE |
| 29 | `quiet.py` is not in the packet | Grok | `scratch/tribunal-bars-0920/` listing | TRUE |
| 30 | i1 window ≈14 calendar days: MSFT 2026-08-13 04:00 → 2026-08-27 06:04 | Grok | `finviz-windows.md:12` | NOT CHECKABLE FROM READS for today's window (the 2026-08-27 record itself is TRUE) — experiment: `uv run cobalt archiver restate NVDA i1` preview (prints `export_oldest`) |
| 31 | tier_b's i2 writes already stopped on 2026-09-03 with nothing breaking | Grok | brief `part1:359` (data) | NOT CHECKABLE FROM READS — experiment: `SELECT interval, max(ts) FROM system.bars WHERE ticker IN (tier_b list) GROUP BY 1` |
| 32 | `pg_class.reltuples` is not updated until VACUUM; `n_tup_ins/upd/del` are usable as a before/after guard | Grok | — | NOT CHECKABLE FROM READS — experiment on `cobalt_dev`: delete rows, read `reltuples` and `pg_stat_user_tables` before and after, and after a restart |
| 33 | REVOKE on a child does not stop an INSERT routed through the parent; a compressed export is not directly attachable; a long reader delays ACCESS EXCLUSIVE; whether a mixed batch rolls back entirely | Astra, Grok | — | NOT CHECKABLE FROM READS — experiments on `cobalt_dev`: child REVOKE + parent INSERT; `ATTACH PARTITION` of a restored file; a held read lock during two renames; a mixed-batch insert |
| 34 | The vendor's i2 low is lower than the derived low for DRAM 04:02, DRAM 04:04, QTUM 04:00 on 2026-09-03; which bar the trader's 2-minute chart shows | Gemini, Grok, Astra | brief `part1:334` (data) | NOT CHECKABLE FROM READS — experiment: stage the three keys' i1 rows and vendor i2 rows and compare with the trader's chart (DAS) |
| 35 | i1 distinct tickers per day 584→337 vs membership 536→462 is unexplained (archive lag vs loss) | Grok | brief `part1:405` (data) | NOT CHECKABLE FROM READS — experiment: per-day distinct-ticker counts against `radar_membership` and the archiver's night log |
| 36 | Disk: ≈820 MiB extra; peak filesystem use during copy + WAL | Grok, Astra | — | NOT CHECKABLE FROM READS for peak use (the 820 MiB arithmetic is OK, see the table below) — experiment: `df -h` on the postgres volume, then a production-scale rehearsal on `cobalt_dev` |
| 37 | A missing partition leaves cards showing Friday's last minute as live | Grok T2 | card bar reads: `radar-store.excerpt.py:36–48` (`i1_bars` reads `bars`) | NOT CHECKABLE FROM READS — the card path does read i1 from `bars` (TRUE); the staleness outcome needs a rehearsal with a missing partition on `cobalt_dev`. **This is the card-input reach noted in §0; no house shows the design reaching scoring, ranking or card value** |

Arithmetic the houses re-derived (copied, arithmetic only):

| house | step | result | check |
|---|---|---|---|
| Grok | 3,465,033 ÷ 13 = 266,541; 296,286 ÷ 584 = 507.337; 5 × 266,541 = 1,332,705; ÷ 170,000 × 2 = 15.678 | as printed | ARITHMETIC OK (exact 507.339 and 15.679; last-digit rounding) |
| Grok | 8,834,532 ÷ 53.29 = 165,782; ÷ 47.05 = 187,768 | as printed | ARITHMETIC OK (187,769.0 exact, one unit off) |
| Grok | 30 s/side → 5,100,000 rows; ÷ 5 = 1,020,000/day; ÷ 507.3 ≈ 2,010; ÷ 960 = 1,062; 21 × 266,541 = 5,597,361 → 32.9 s | as printed | ARITHMETIC OK (2,010.6; 1,062.5; 32.93) |
| Grok | 500 × 507.3 × 5 = 1,268,250 → 14.9 s; 5,281,313 + 266,541 × 252 = 72.45 M → 852 s | as printed | ARITHMETIC OK (14.92 s; 72,449,645; 852.35 s) |
| Gemini | 2,000 tickers → 5.07 M rows/week → 59.7 s; the week of 2026-11-01 is 169 hours | as printed | ARITHMETIC OK (5,073,000 rows; 59.68 s; 7 × 24 + 1 = 169) |
| Astra | 266,541; 507.339; 1,332,705; 7.839 s/side; 15.679 s | as printed | ARITHMETIC OK |
| Astra | 2,000 × 507.3 × 5 = 5,073,000; × 2 ÷ 170,000 = 59.682 s; 15.7 × 170,000 ÷ (2 × 5 × 507.3) ≈ 526; 2,665,410 ÷ 188,000 = 14.18, ÷ 166,000 = 16.06; daily 3.136 s and 11.936 s | as printed | ARITHMETIC OK |
| Astra | 1,780,528 + 1,025,864 + 161,044 + 585,783 = 3,553,219; 8,834,532 − 3,553,219 = 5,281,313; ≈ 820 MiB; 1,371.5 + 820 = 2,191.5 | as printed | ARITHMETIC OK |
| Astra | 1,780,528 + 835,818 + 131,950 + 69,550 = 2,817,846; − 52 = 2,817,794 = 99.9981546 %; i2 alone 99.9970795 % | as printed | ARITHMETIC OK |
| Astra | (72 + 47 + 94 + 111) ÷ 4 = 81; 860 − 584 = 276; 5,281,313 + 266,541 × 252 = 72,449,645; × 2 ÷ 170,000 = 852.35 s | as printed | ARITHMETIC OK |
| Astra/Grok | session densities 120.4 ÷ 330 = 36.48 %; 312.9 ÷ 390 = 80.23 %; 74 ÷ 240 = 30.83 % | as printed | ARITHMETIC OK |
| brief (Grok/Astra dispute) | §2.7 table: 1,500 tickers → 3.80 M rows/week → 44.8 s both sides | `part2:55` | ARITHMETIC OK (1,500 × 507.3 × 5 × 2 ÷ 170,000 = 44.76 s) — the brief's own table gives 44.8 s at 1,500 tickers, not 15.7 s |

BARS TRIBUNAL ROUND 1 DONE · grok: RULING: BUILD WITH MY AMENDMENTS T2 T3 T4 T5 T6 T7 T9 · gemini: RULING: BUILD WITH MY AMENDMENTS T1, T4, T5, T7, T8, T9 · astra: RULING: BUILD WITH MY AMENDMENTS T1 T2 T3 T4 T5 T6 T7 T8 T9 · houses that ruled: 3 of 3 · points 3-0 ACCEPT: none · points with an AMEND or REJECT: T1, T2, T3, T4, T5, T6, T7, T8, T9 · §2.7 arithmetic: holds 0 / breaks 3 / unverified 0 · R9 RISK raised: 0 · false claims about the code: 2 · NOT CHECKABLE: 11
