# DRC OVERNIGHT TRIBUNAL R1 — hub `drc-overnight-tribunal-0924` (Sonnet 5), 2026-09-24

## §0 Headline
- Ruled by **2 of 3 houses** (Grok, Gemini; Astra `METER — proceed on three`, back Sat 09-26 06:47 ET); closing lines: Grok `TRIBUNAL R1: BUILD AFTER Q1 Q2 Q3 Q4 Q6 paste wording is folded` · Gemini `TRIBUNAL R1: BUILD`. Nobody said DO NOT BUILD; no REJECT; every OWNER line `none`.
- 42 houses' claims HOLD, 1 UNVERIFIABLE FROM READS (a Postgres / migrator behaviour), 2 DO NOT HOLD (both Gemini's); 4 blockers to build (Grok's Q1, Q3, Q4, Q6, each with a HOLDING claim; its Q2 rests on an unrun claim = an experiment). **Anthropic-seat R1 claims checked: 23 HOLD of 26 checked** (3 UNVERIFIABLE FROM READS, 0 DO NOT HOLD).
- ESCALATE: 5 (packet 184,504 B > 140 KB after the whole cut order; the seat's Mon-after-Tue assumed-book gap HOLDS; Astra's probe row; redaction counts; one hub mishap). Redactions: 0 (packet), 0 (this report). SHAPE-ONLY drops: 0.
- The houses contradict one another on: Q2 (fold into `0016` or never), the assumed-book walk (b), the `day <k>` figure (stored vs rendered), WRONG FACTS (Gemini `none` vs Grok 4 / seat 4) — quoted, not smoothed, under `## Checked against the files`.

## AUTHORIZATION
Read 09:3x–09:4x ET, each its own Bash call; written from tool output only.

| # | check | result |
|---|---|---|
| 1 | `^\| R13 ` `cto-2026-09-20.md` | :86 present (13:33 ET, the rule list) |
| 2 | `^\| R109 ` `cto-2026-09-22.md` | :56 carries `Make all Opus 5.5 for now` |
| 3 | `^\| R67 ` `cto-2026-09-22.md` | :99 carries `continuing position` |
| 4 | `^\| R93 ` `cto-2026-09-22.md` | :72 carries `DRC every market trading day` |
| 5 | `^\| R96 ` `cto-2026-09-23.md` | :104 carries `optional fourth seat on design tribunals` |
| 6 | `^\| R19 ` `cto-2026-09-24.md` | :29 carries `All 4 house models approved` (the (5') GROK / AGY GATE) |
| 7 | `^\| R22 ` `cto-2026-09-24.md` | :32 carries `We need to design the lane` |
| 8 | `git log -1 -S"\| R22 \| "` desk file | `5c0a8d3fe271e6e5d79f0856288533a2acc3d74d` (committed on main) |
| 9 | `git log -1 -S"All 4 house models approved"` desk file | `5055151dbf68899b82de5b11f99733ed2d03048c` (committed) |
| 10 | `git log -1` the proposal | `9a4242427b051837c5428e4c198958b7328a8d83` (committed) |
| 11 | `git log -1 -S"OVERNIGHT LANE PROPOSED"` draft report | `9a4242427b051837c5428e4c198958b7328a8d83` (committed) |
| 12 | `grep -n "23-drc-overnight-tribunal.md"` desk files | `cto-2026-09-25.md` does not exist (recorded, not fatal); `cto-2026-09-24.md` :42 R32 and :45 R35 name it. R32 (`| R` row, "DESK LAUNCH") carries all three literals: `DRC-OVERNIGHT-POSITION-PROPOSAL-2026-09-24.md` · `Fable seat: yes` · `derive seat: claude-opus-5-5` |
| 13 | `git log -1 -S"23-drc-overnight-tribunal.md"` the two desk files | `a09d005c12db8a531d1263d79cb49017e0912843` (launch row committed) |
| 14 | NO NEW RULE: `grep -c -F -e '"<rule>"'` on `prompts/2026-09-20/08-bars-chunk-e-check.md`, 14 allow + 3 deny, quotes included | all 17 print `1` (≥1). `Bash(grok *)` and `Bash(agy *)` print 1 in this quoted spelling (the prompt records 2 for the unquoted line count) — ≥1 holds. No Sol / Opus checker string (`gpt-5.6-sol`, `claude -p --model claude-opus-5`) is in this prompt's launch line. |

Note: R35's launch-row text does not itself carry the three literals; R32's does (row 12). Both name `23`.
Authorization: MATCHES. Real user words present in the rows quoted; no `FAILED: authorization mismatch`.

## PREFLIGHT (METER, L47)
| # | rule | command | exit | result |
|---|---|---|---|---|
| 1 | date | `date` | 0 | Thu Sep 24 09:38:21 EDT 2026 — market hours; no deploy-window rule applies (this hub reads and writes scratch only) |
| 2 | (5') GROK / AGY GATE | R19 grep (above, row 6) | 0 | allowed — R19 row printed with `All 4 house models approved`; STANDING, no date |
| 3 | grok | `grok --version` | 0 | allowed — `grok 1.0.25 (f7e67d6988e2) [stable]` |
| 4 | agy | `agy --version` | 0 | allowed — `1.2.9` |
| 5 | base folder | `ls scratch/tribunal-bars-0920` | 0 | allowed — exists |
| 6 | RECOVERY | `ls scratch/tribunal-bars-0920/drc-overnight/r1` | 1 | `No such file or directory` = fresh run |
| 7 | (7') STAGGER s1 `15` | `tail -n 3` `drc-d1-fix-r1-check-2026-09-24.md` | 0 | last non-blank line starts `DRC D1 FIX R1 CHECK DONE ` — not running |
| 8 | s2 `16` | `tail -n 3` `voice-v1-check-a-2026-09-24.md` | 0 | last non-blank line starts `VOICE V1 CHECK DONE ` — not running |
| 9 | s3 `17` | `tail -n 3` `voice-v1-check-b-2026-09-24.md` | 1 | `No such file or directory`; launch row: `grep -n -F "17 is not running"` → R32 :42 and R35 :45, R35 names `23-drc-overnight-tribunal.md` → `17: no report — not running (launch row)` |
| 10 | s4 `18` | `…-c-2026-09-24.md` | 1 | no such file; `18 is not running` printed (R35 :45 names `23`) → not running (launch row) |
| 11 | s5 `19` | `…-d-2026-09-24.md` | 1 | no such file; `19 is not running` printed (R35 :45) → not running (launch row) |
| 12 | s6 `74` | `jev-check-final-2026-09-23.md` | 1 | no such file; `74 is not running` printed (R35 :45) → not running (launch row) |
| 13 | (3') CODEX PROBE (astra only) | `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` (background) | 1 | `ERROR: You've hit your usage limit. … try again at Sep 26th, 2026 6:47 AM.` → `astra: METER — proceed on three`. Return time recorded: **Sat Sep 26 06:47 AM** (L62 / R19: the desk seats Astra again from then). Not a refusal. |

D1 code proofs: `git log -1 --format=%H drc/d1-trading-log` = `38a709472d428f1fda77fac93c75d0f5b9a2c6d6` (expected `38a70947…` ✓); `git show --stat 38a70947` = 1 file, `drc-d1-fix-r1-build-2026-09-24.md`, docs only ✓. Worktree sizes match drafting: `pairing.py` 12,901 · `store.py` 10,568 · `models.py` 8,844 · `test_drc_pairing.py` 13,959 · `0016_drc.sql` 4,945 (the worktree holds the committed bytes as far as size shows). Proposal `wc -c` = 29,546 (matches).

## Packet
Folder `scratch/tribunal-bars-0920/drc-overnight/r1/` (staged by the Write tool, no `mkdir`). Built code = the D1 branch (`drc/d1-trading-log`, tip `38a70947` = code tip `d1342595` + one docs-only report commit; worktree sizes matched drafting, so the worktree files were staged). Anchors: every drafted anchor was at its drafted line (checked with `grep -n`); no boundary moved.

| file | bytes | note |
|---|---|---|
| `00-READING-ORDER.md` | 4,179 | written last |
| `01-QUESTIONS.md` | 12,615 | questions verbatim + the "Files in this folder" paragraph (names the cuts) |
| `02-greps.txt` | 274 | POINTER only — the searches exceed 38,000 B, so they are in ordered parts |
| `02-greps.txt.part1` | 30,087 | sections 1–10, cut at a heading |
| `02-greps.txt.part2` | 26,813 | section 11 (voice FINAL confirm shape) |
| `02-greps.txt.part3` | 12,198 | sections 12–19 |
| `10-PROPOSAL.md` | 29,546 | whole; `wc -c` = original 29,546; 0 trailing-whitespace lines in the original → byte-identical |
| `11-design-digest.md` | 5,741 | draft report :5-42, :48-60, :66 |
| `12-rulings.md` | 9,822 | R22, R65, R66, R67, R90, R93, R109, R39 + table headers |
| `13-v2-carry.excerpt.md` | 6,170 | v2 :74/:81, :84-87/:94, :127/:133-134/:141, :169/:173-174/:179/:181, :185/:189-190/:191 |
| `14-drc-shape.md` | 3,587 | headings + unit markers only |
| `20-drc-carry.excerpt.py` | 5,074 | pairing :143-174, store :177-179 and :220-250, test :249-273 |
| `21-drc-cited.excerpt.py` | 11,722 | pairing :1-30, :60-88, :117-129, :175-258; models :100-115, :160-170; 0016 :1-30, :80-95; propose :298-310 |
| `22-s3-r67-clause.excerpt.md` | 11,950 | S3 v3 :17-24, :141-165 |
| `27-laws-excerpt.md` | 14,726 | CUT (i) applied: L1, L3, L28, L57, L67 |

MANDATORY total 169,778 B (incl. `00`); whole packet **184,504 B** (≈ 46 k tokens). **Over the 140 KB target after the whole cut order** — the packet was over target before any cut (`02-greps` alone is 69,372 B). Cuts applied, in the prompt's order: (i) `27-` down to five laws · (ii) `26-voice-confirm.excerpt.md` whole · (iii) `24-store-whole.py` whole · (iv) `23-pairing-whole.py` whole. Each named in `00` and in `01`. Not a failure; listed under ESCALATE.

Verification done: `wc -c` on the proposal (whole copy) matches. Excerpts were copied by Read → Write; each was checked line-by-line with `grep -v -x -F -f <original(s)> <staged>`: every non-blank content line of `11-`, `12-`, `13-`, `20-`, `21-`, `22-`, `27-` appears verbatim in its source (only my own range headers and blank lines print). Two transcription errors of mine in `02-greps` (a shortened row, dropped lines) and two off-by-one ranges in `21-` were found and fixed before launch; the git-log output was completed to all 53 lines. `02-greps` parts were checked by line count (`^NN:` lines: 11 + 47; commit lines: 58 = 1 + 3 + 53 + 1), not line-by-line against a saved output (no redirect allowed). `14-` was not byte-compared (line numbers prefixed by design).

Trailing-whitespace disclosure: original proposal 0 lines; the built-code files `pairing.py`, `store.py` 0 lines; other originals are excerpts (not byte copies).
REDACTION (L32): `grep -c -E "TSLA|372[.]82|374[.]50"` (the literals from `73` §1) printed `0` on every staged file (00, 01, 02 + parts, 10, 11, 12, 13, 14, 20, 21, 22, 27). Replacements: 0. SHAPE-ONLY drops: headings dropped 0, marker lines dropped 0, body lines staged 0 (`14-`). Other user data noticed: none (the R67 hypothetical share figure is his ruling text, as the prompt says; the test fixture symbol `GGG` and v2's constructed `card 812` scenario are constructed fixtures).
NOT STAGED: his DRC note's and template's bodies, Rules.md, any daily note, the E1 fixture / any export, v2 / S3 v3 / VOICE-v3-FINAL whole, the D1 build and fix reports, any trade or production row.

## CONTINUE
next: close (§4) — replace the last line with the stop line. Both houses are DONE (`gemini-ruling.md` written 10:00; `grok-ruling.md` by Grok, notice 10:09); collate and the Anthropic-seat file-check are written above; no house is running, so no deadline is pending.
Launched together in one message (Grok: `grok --sandbox cobalt-job --allow "Write(…/scratch/tribunal-bars-0920/**)" -p "…"`; Gemini: `agy --model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 20m --add-dir /Users/cobalt/cobalt-wt/agy-trial --print="…"`), both `run_in_background`, one attempt each. Launch time: between `date` 09:57:12 (pre-launch gate row) and 09:58:20 (first `date` after) — taken as **09:58**. Deadlines (20 min, conservative from 09:57:30): **Grok 10:17 ET · Gemini 10:17 ET** (stop by task-stop, record TIMEOUT).

## Clock
| time | trigger | house minutes since launch | action |
|---|---|---|---|
| 09:57:12 | before launch (the (5') gate's second row) | — | R19 grep printed the row again (allowed) |
| 09:58:20 | after launch | grok ≈0 · gemini ≈0 | both launched in one message, background |
| 10:00:07 | Gemini completion notice (exit 0) | grok ≈2 · gemini done ≈2 | Gemini's printed answer written byte for byte (minus `[exited with code 0]`) to `gemini-ruling.md`; it carries a `TRIBUNAL R1: BUILD` line. Grok still running; deadline 10:17. |
| 10:09:16 | Grok completion notice (exit 0) | grok ≈11 (done) · gemini done | `grok-ruling.md` written by Grok itself (27,758 B); carries a `TRIBUNAL R1:` line. No timeout. |
| 10:10:09 | collate step (Independence greps, file-checks of the houses' claims) | both done | begun |
| 10:15:56 | close (§4) | both done | stop line written |
| 10:13:39 | collate step — Anthropic-seat file-check (its `tail -n 3` and the rest of the seat file-check were run in this step, just before this `date`) | both done | seat report ends `DRC OVERNIGHT FABLE R1 DONE ·` → read and file-checked |

## Rulings table
`item · grok · gemini · agreement (of the houses that ruled) · wording offered or reason (≤25 words per house)`. Astra: METER, did not rule. "2-0" = both houses gave that tag.

| item | grok | gemini | agreement | wording offered / reason |
|---|---|---|---|---|
| Q1 separate append-only table | ADOPT WITH | ADOPT | 2-0 for the separate table; wording differs | grok: current stated row = one no other row supersedes; two current rows FAIL; `record_stated_book` refuses inside `market_reset`. gemini: `record_day` deletes `drc_rows` per day, would wipe it. |
| Q2 migration numbering | ADOPT WITH | ADOPT | 2-0 with wording | grok: fold into `0016` only if unmerged AND not applied on `cobalt_dev`, else new file; never `0017`'s number. gemini: fold only if D1 unmerged; else next free (≥ `0018`). |
| Q3 forward re-pair | ADOPT WITH | ADOPT WITH | 2-0 ADOPT WITH (different wording) | grok: pair in memory first, one DB transaction, notes after commit, stale-mark on note failure. gemini: "a staged set, the note re-upserts after the DB". |
| Q4 stated position without cost | ADOPT WITH | ADOPT | 2-0 | grok: null cost is the stored input; exit realized `not computed — carried cost not stated`, `_reduce` not called. gemini: L57 forbids guessing; state why not computed. |
| Q5 no-trade DRC as the carry event | ADOPT | ADOPT | 2-0 ADOPT | both: R93 makes the no-trade DRC the only event; a trading day with neither is a broken chain (`check_contiguity`). |
| Q6 closed outside the export | ADOPT WITH | ADOPT | 2-0 | grok: resolve → CLOSED, realized only when prices stored, and the close runs the Q3 re-pair. gemini: export is truth, later export supersedes the resolve. |
| Q7 aging | ADOPT | ADOPT | 2-0 ADOPT | both: a swing is lawful; show `day <k>` and `last execution`; no alert (an N would be his, grok cites L53). |
| Q8 no morning mention outside `/drc` | ADOPT | ADOPT | 2-0 ADOPT | both: 09:00 reader unchanged; a wider quote is a later slice. |
| Q9 days before the lane | ADOPT | ADOPT | 2-0 ADOPT | both: FAIL naming the day + `rebuild <day>`; migration computes nothing. |
| Q10 landing set | ADOPT | ADOPT | 2-0 ADOPT | grok: K1–K3 with D2+D3; CLI calls `record_stated_book` only. gemini: K3 late → CLI fallback lets K1 land; B8 never in production. |
| Q11 unit leaves D5 | ADOPT | ADOPT | 2-0 ADOPT | both: the unit needs `drc_rows`, not S3 legs; D5 keeps the reconcile unit. |
| (a) fact base | text: B1–B9 hold, B10 as a comment; misses listed; 4 WRONG FACTS | text: holds exactly; no misses | both say the B-rows hold; differ on misses / wrong facts | grok misses: `store.py:193`, `pairing.py:113`, `daymode` uses, prefill writers. gemini: none missed. |
| (b) L1 no assumed book | text: A fail-loud; C not; four walks | text: A fail-loud; C not | 2-0 on C not fail-loud and on A (as worded) | grok's flat-tap residual: a stated flat + leading `B` opens a long, shown as `new today`. gemini: C's cover read as long. |
| (c) L57 replay | text: chain named; four figures with their inputs | text: replayable; link survives delete-and-replace | 2-0 replayable | grok: the link survives only if Q3 rewrites every dependent day in the same transaction. gemini: key is not the DB id. |
| (d) L28 / L40 unit and statement | text: one writer; statement is a DB input; L28 voice clause does not apply | same | 2-0 | grok: page form has no read-back; voice ACT confirms first. gemini: `2.6` confirm shape applies to the widget ACT. |
| (e) landing set | text: real dependency of the first `pair_day` caller, not of K1 | text: K1 can land alone as a no-op | 2-0 K1 alone is inert | grok: D2 without K1 is the bad deploy; L72 seam belongs in both prompts. gemini: dependency functional, not a deploy blocker. |
| (f) experiments first | X3–X5, X7, X8 | X1, X2 | 2-0 name the re-pair transaction and the Sync-revert hash as experiments | see `## Experiments named`. |
| closing line | `TRIBUNAL R1: BUILD AFTER Q1 Q2 Q3 Q4 Q6 paste wording is folded` | `TRIBUNAL R1: BUILD` | split: BUILD AFTER vs BUILD | verbatim in the two cells. |

## Wording offered, verbatim
Unedited copies of every `ADOPT WITH` replacement wording. (No `REJECT` was given by either house.) User-data spans: none. Astra: no ruling (METER).

**GROK**

Q1 — "ADOPT WITH: Stated opening books and resolves live only in append-only `"user".drc_stated_books`, not as a `drc_rows` kind. `record_day` runs `DELETE FROM drc_rows` for that day (`store.py:202`) and would erase a statement stored there. The current row for a day and kind is the row whose id is not the `supersedes` of any other row (same predicate as `store.py:92-93`). Two current `opening` rows for one day, or two current `resolve` rows for one `trade_id`, FAIL naming both ids. `record_stated_book` refuses inside `market_reset`, the same gate as `VaultWriter._session_gate` (`writer.py:388`, §12)."

Q2 — "ADOPT WITH: One new `db_migrations` file plus `.rollback.sql`. The desk numbers it at the L68 gate. Fold the `drc_rows.kind` widening into `0016_drc.sql` only when, at K1's cut, that file is still unmerged and `0016` is not applied on `cobalt_dev`. Otherwise a new file. Never a number already used by `0017_voice_turns.sql`."

Q3 — "ADOPT WITH: Forward re-pair is automatic and all-or-nothing, in memory first. On a superseding import of day P, load fills from the current import only (the `drc_imports` row no other row supersedes). Pair every later recorded day in date order, each seeded from the new prior book. If any later day fails, write nothing and FAIL naming that day. If all pair, one database transaction replaces `drc_rows` for P and every later day. Note re-upserts run after the commit, in date order. A note failure leaves the database committed, marks that unit stale, and FAILs naming the note. The morning book is read from the database, never from the note."

Q4 — "ADOPT WITH: A stated position may omit average cost. The carried lot stores that cost or null, and that null is the stored input. An exit against a null cost stores realized `not computed — carried cost not stated` and does not call the price arithmetic in `_reduce` (`pairing.py:117-129`)."

Q6 — "ADOPT WITH: A RESOLVE writes one `drc_stated_books` row `kind=resolve` for one `trade_id`. The trade is CLOSED, source stated. Realized P&L is computed only when every carried lot's price and `exit_price` are stored; otherwise the stored figure is `not computed — exit not in any export`, and the closed trade's inputs include the resolve row id. The close runs the Q3 forward re-pair so no later `book_close` still contains that `trade_id`. A later export that contains the closing execution supersedes the resolve and re-pairs from the export (R67: the export is the truth). A later export that still shows the shares open supersedes the resolve the same way and the position stays open. Never a silent close (R90)."

**GEMINI**

Q3 — "`ADOPT WITH a staged set, the note re-upserts after the DB`" — its reasoning, verbatim: "Automatic forward re-pair matches deterministic replay, but vault writes (`upsert_unit`) cannot be rolled back. Failing scenario: DB re-pairs day 2 and day 3; day 2's note upsert succeeds, but day 3's DB update fails. The DB rolls back, leaving day 2's note displaying a new book while the DB retains the old book, breaking L57. A staged set commits the DB first, leaving notes safely stale on failure."

(The full rulings are the two files `scratch/tribunal-bars-0920/drc-overnight/r1/grok-ruling.md` and `…/gemini-ruling.md`, kept; the derive step reads them there.)

## Checked against the files
Legend: `claim · who · file:line · verdict · ≤30 words`. Files opened by me: the D1 worktree `/Users/cobalt/cobalt-wt/drc-d1/` (pairing / store / models / migration / tests / propose), main `writer.py`, the proposal, v2, LAWS.md, the two vault shape greps. `02-greps` outputs are my own greps of the same trees (run 09:5x).

| # | claim · who | file:line | verdict | note |
|---|---|---|---|---|
| GM1 | Q1 `record_day` deletes and replaces the day's `drc_rows` · gemini | `store.py:201-203` | HOLDS | the DELETE is at `:202` |
| GM2 | Q2 `0017_voice_turns` exists on the voice branch; next free ≥ `0018` · gemini | `git log --all` → `69c376bd`; main ends `0011` | HOLDS | a floor, the desk numbers it |
| GM3 | Q3 scenario: a day-2 note upsert lands, then day 3's DB update fails · gemini | proposal `:104`, `:166` | DOES NOT HOLD | as an objection to the proposal: it orders "DB first, notes after"; the remedy gemini adopts is that same order |
| GM4 | (a) B1–B10 hold; no missed reader / writer of `open_position`, the seed, `carried_from` · gemini | `02-greps` §2, §9 | HOLDS | the reader is `seed_for` `store.py:246-248`, the writer `:179`; grok and the seat list extra citations, not extra readers |
| GM5 | (a) `replay/cards.py:110` is a rule-name string, not a reader · gemini | `replay/cards.py:110` | HOLDS | `RULE_10_PROXY = "two_open_positions"` |
| GM6 | (a) no path records a no-trade day · gemini | §3 grep | HOLDS | hits are `pairing.py:246`, `:252` and two unrelated comments |
| GM7 | (b) option C reads a morning cover as a long that stays open · gemini | `pairing.py:6`, `:189-193`, test `:265-272` | HOLDS | |
| GM8 | (b) "No 'assume' is left under Option A" · gemini | `10-PROPOSAL.md` §3, §4 | HOLDS | as worded (each start is a carried hash or his statement); the seat names a re-check gap (FC3, FC22) — both quoted under the contradictions below |
| GM9 | (c) the `(day, kind, ref)` + hash link survives delete-and-replace because it does not use the row id · gemini | `10-PROPOSAL.md:102`, `store.py:202` | HOLDS | narrow: the key excludes `id`; grok adds the stale-hash condition |
| GM10 | (d) one writer of the unit: `build.py` via `VaultWriter.upsert_unit` "L113" · gemini | `10-PROPOSAL.md:113` | HOLDS | `build.py` is not built; the citation is the proposal's row |
| GM11 | (d) the statement is a DB input, so L28's voice clause does not apply; the `2.6` confirm shape does · gemini | LAWS.md `:166`; voice FINAL `:88` | HOLDS | L28's clause is a vault field span; `2.6` is the ACT confirm |
| GM12 | (e) no production import path calls `seed_for` before D2 / D3; callers per `10-PROPOSAL.md:112` · gemini | `02-greps` §2; `10-PROPOSAL.md:112` | HOLDS | `seed_for` is uncalled in D1 src and absent from main |
| GM13 | WRONG FACTS: `none` · gemini | GK28–GK31, FC19, FC21 | DOES NOT HOLD | four statements the files contradict were found by grok and the seat and verified below |
| GK1 | Q1 the DELETE at `store.py:202`; `drc_rows.kind` CHECK at `0016:86` · grok | `store.py:202`; `0016_drc.sql:86` | HOLDS | |
| GK2 | Q1 `drc_rows` is not under `refuse_row_update` · grok | `02-greps` §6 | HOLDS | only `0007` attaches it |
| GK3 | Q1 "current row" predicate is `store.py:92-93` · grok | `store.py:92-93` | HOLDS | `id NOT IN (SELECT supersedes …)` |
| GK4 | Q1 the `market_reset` gate is `VaultWriter._session_gate` · grok | main `writer.py:387-388` | HOLDS | vault-only (`:401`) |
| GK5 | Q2 numbering: main ends `0011`; D1 has `0016`; `0012` / `0013` on other branches; `0017` = `69c376bd` · grok | `02-greps` §14, §15, §18, §19 | HOLDS | |
| GK6 | Q2 `CREATE TABLE IF NOT EXISTS` leaves an applied CHECK unchanged and the migrator skips the table · grok | `0016_drc.sql:80` | UNVERIFIABLE FROM READS | run: apply an edited `0016` on a `cobalt_dev` where the old one applied, insert `kind='seed'` (X-C) |
| GK7 | Q3 the DELETE names `drc_rows` only; the inputs stay · grok | `store.py:15`, `:202` | HOLDS | |
| GK8 | Q4 `_reduce` does `per_share * take` from `lot.price` · grok | `pairing.py:117-129` | HOLDS | also: `Lot.price: Decimal` is required (`models.py:98`), the point grok marked unverified |
| GK9 | Q5 `pair_day` on no executions leaves the seeded books; `prior_trading_day` skips weekends · grok | `pairing.py:220-236`; `propose.py:300-308` | HOLDS | |
| GK10 | Q6 a resolve is not "a superseding file", so §3's trigger does not fire · grok | `10-PROPOSAL.md:104` | HOLDS | a gap in the text as written |
| GK11 | Q7 `day <k>` from stored `opened_on` and the calendar · grok | `pairing.py:231` | HOLDS | `opened_on` is stored; the seat says `day <k>` is stored in the row (FC16 note) |
| GK12 | Q9 a D1-recorded day has `open_position` rows and no `book_close` · grok | `02-greps` §1 (no writer) | HOLDS | |
| GK13 | Q10 `seed_for` has no caller; `pair_day` is called only by `build_day`, itself uncalled · grok | `pairing.py:337`; `02-greps` §2 | HOLDS | my grep of `pair_day` / `build_day` / `DrcStore` |
| GK14 | Q11 no writer of unit `drc-trades/open_positions`; D5 waits on C2 · grok | `02-greps` §9; v2 `:179`, `:181` | HOLDS | |
| GK15 | (a) B4's "see G-c" points at nothing · grok | `10-PROPOSAL.md:18` | HOLDS | `grep -n "G-c"` prints only `:18` |
| GK16 | (a) `check_contiguity` is called only from `seed_for` · grok | `store.py:235` | HOLDS | |
| GK17 | (a) missed: `store.py:193`, `pairing.py:113`, `propose.py:380`, `daymode/drc.py:152`, `prefill/drc.py:427`, `:443`, `writer.py:671-672` · grok | `02-greps` §2, §8, §9 | HOLDS | each line is as described |
| GK18 | (a) (iv): four `no-trade` hits, none a writer · grok | `02-greps` §3 | HOLDS | |
| GK19 | (b) option C: first import, leading `B`, opens a long, next day seeds from it · grok | `pairing.py:6`, `:189-193` | HOLDS | |
| GK20 | (b) a skipped trading day FAILs at `check_contiguity` · grok | `pairing.py:250-254` | HOLDS | |
| GK21 | (b) under A "no pairing starts from a book that was neither a hash-checked carry nor his statement" · grok | `10-PROPOSAL.md` §3, §4 | HOLDS | as worded; the seat's gap is quoted below |
| GK22 | (c) `record_day` issues new ids on delete-and-replace; the logical key survives only with Q3 · grok | `store.py:202`, `:207-210` | HOLDS | |
| GK23 | (c) superseded fills remain (the DELETE names `drc_rows` only) · grok | `store.py:15`, `:202` | HOLDS | |
| GK24 | (d) prefill writes unit `tickers` and creates the note; `upsert_unit` refuses a missing note · grok | `prefill/drc.py:427`, `:443`; `writer.py:671-672` | HOLDS | |
| GK25 | (d) `drc-summary` is not on his note or template · grok | `14-drc-shape.md`; my `grep -c drc-summary` on both = 0 | HOLDS | the template's markers are not staged; I checked both files myself |
| GK26 | (e) B8 is `pairing.py:189-193`, pin `:265-272`; main has no `0016` · grok | `pairing.py`; `02-greps` §14 | HOLDS | |
| GK27 | (f) the hash is over stored `open_position` rows, not the unit's bytes · grok | `10-PROPOSAL.md:38` | HOLDS | |
| GK28 | WRONG FACT: digest says the only no-trade hits are `:246`, `:252` and one unrelated comment · grok | draft report `:52`; `02-greps` §3 | HOLDS | four hits: two more unrelated (`radar/seam.py:21`, `aset/web.py:311`) |
| GK29 | WRONG FACT: B4 "see G-c" · grok | `10-PROPOSAL.md:18` | HOLDS | same as GK15 |
| GK30 | WRONG FACT: `pair_day([], D, seed)` returns the seed "unchanged" — `OpenPosition.day` is the new day · grok | `pairing.py:231-232` | HOLDS | `opened_on` unchanged, `day=day` new |
| GK31 | WRONG FACT: digest "0017 not verified against a file" · grok | draft `:51`; `02-greps` §19 | HOLDS | `69c376bd` prints |
| GK32 | Q3 scenario: Monday re-imported, Tuesday not rewritten, Tuesday's seed stays H1 · grok | `10-PROPOSAL.md:104`, `:53` | HOLDS | follows if only Monday is replaced |
| GK-a | arithmetic: `5+4+5+2 = 16` · grok | `10-PROPOSAL.md:158` | ARITHMETIC OK | |

Counts: gemini 13 rows (11 HOLDS, 2 DOES NOT HOLD); grok 32 rows + 1 arithmetic (31 HOLDS, 1 UNVERIFIABLE FROM READS). **claims that HOLD: 42.**

Where the houses (or a house and the seat) contradict — quoted, not smoothed:
- Q2. grok: "Fold the `drc_rows.kind` widening into `0016_drc.sql` only when, at K1's cut, that file is still unmerged and `0016` is not applied on `cobalt_dev`." · gemini: "Folding into `0016` is safe only if D1 has not merged to main". · the seat: "`0016` is never edited after D1's check."
- WRONG FACTS. gemini: `none` · grok: four (GK28–GK31) · the seat: four (FC19–FC21, GK28-equivalent). Verified above and below.
- (b). grok: "No pairing starts from a book that was neither a hash-checked carry nor his statement." · gemini: "No 'assume' is left under Option A." · the seat: "Remaining assume path: an earlier day recorded after a later stated day." Mechanism verified (FC3, FC22); what is "assumed" is the seat's characterisation.
- `day <k>`. grok: "`day <k>` is rendered from the stored `opened_on` (`pairing.py:231`) and the NYSE calendar, not stored as its own number." · the seat: "`day <k>` and the held-lot average cost are stored in each `open_position` row's `derived` by `record_day`, not computed at render." (`OpenPosition` today carries no `k` field: `models.py:102-112`.)
- (c) placement of the book. the proposal: new `seed` / `book_close` `drc_rows` kinds. the seat: put both on the existing `day` row. Neither house comments.

## Anthropic-seat round-1 claims, file-checked
Seat report `drc-overnight-tribunal-fable-r1-2026-09-24.md`, stop line `DRC OVERNIGHT FABLE R1 DONE · verdict: BUILD AFTER re-pair triggers on every earlier-day record; stated-position model fields made Optional · adopt: 5 · adopt with wording: 12 · reject: 0 · experiments named: 9 · ESCALATE: 1`. WITHDRAWN: none. Seat run date `Thu Sep 24 08:44:53`; blind per its own line 1.

| FC | claim (seat report line) | file:line | verdict | note ≤30 words |
|---|---|---|---|---|
| FC1 | Q1 (`:36`): `record_day` deletes the day's rows first; `refuse_row_update` at `0007:105-113`, `:190`, `:199` | `store.py:201-203`; `02-greps` §6 | HOLDS | |
| FC2 | Q2 (`:39`): `0016` = `d583f6fd`, `0017` = `69c376bd`, main ends `0011` | `02-greps` §14, §18 | HOLDS | `d4e2fdc2` is main's last migration commit |
| FC3 | Q3 (`:45`): `check_contiguity(Mon, …, [Tue, Wed])` passes because `earlier` is empty | `pairing.py:249-250` | HOLDS | the drafted trigger is "a superseding file for day P" (`10-PROPOSAL.md:104`), which a first Monday file is not |
| FC4 | Q3 (`:41`): a later day recorded first is lawful today | `test_drc_pairing.py:350-351` | HOLDS | `test_a_later_recorded_day_is_not_history` |
| FC5 | Q3 (`:49`): `drc_fills` holds trading-log columns only; stats rows exist only as `drc_rows` `stats_row` | `0016_drc.sql:52-71`; `store.py:170-186` | HOLDS | |
| FC6 | Q3 (`:49`): `match_stats` needs a `ParsedStatsLog` | `pairing.py:260-316` | HOLDS | |
| FC7 | Q3 (`:41`): `record_day` commits per call | `store.py:198-212` | HOLDS | one `commit()` per call |
| FC8 | Q3 / WF3 (`:41`, `:176`): `record_import` commits the superseding file in its own transaction before any pairing | `store.py:85-150`, `:88-97` | HOLDS | proposal `:104` says "nothing is replaced"; it does not say the import row is uncommitted — the seat's reading is stricter |
| FC9 | Q4 (`:53-54`): required fields `Lot.price` / `Lot.time`, `OpenPosition.entry_time`, `Trade.gross_pnl`; `trade_id()` uses `entry_time.isoformat()`, `_trade` subtracts it, the sort keys on it | `models.py:97-98`, `:110`, `:164`; `pairing.py:69`, `:105`, `:235` | HOLDS | its list is incomplete: `Leg.price` (`:88`) and `Trade.avg_entry` (`:160`) are also required; `Trade.hold_seconds` is already Optional (`:159`) |
| FC10 | Q5 (`:57`): an empty day writes a `day` row with `inputs = {"import_ids": {}}` | `store.py:190` | HOLDS | |
| FC11 | Q6 (`:66`): `_trade` reads `exits[-1]` | `pairing.py:97` | HOLDS | the line fact; the resolve path that would reach it is unbuilt (FC24) |
| FC12 | Q8 (`:71`): the 09:00 reader reads the prior DRC note (`daymode/drc.py:85-165`) | `daymode/drc.py:85`, `:152` | HOLDS | anchors opened (`_drc_note` at `:85`); body not read line by line |
| FC13 | Q9 / (e) (`:73`, `:115-119`): `seed_for`, `record_day`, `record_import` have no caller in D1 and none in main; D2 / D3 bring callers (v2 `:176-177`) | `02-greps` §2; my grep of `record_day` / `record_import`; v2 `:176-177` | HOLDS | |
| FC14 | (a) (viii) (`:81`): built `carried_from` holds the trade's OPEN day | `pairing.py:149`, `:231`; `test_drc_pairing.py:233` | HOLDS | `_seeded` copies `opened_on`; `:231` keeps it |
| FC15 | (a) (`:96`): production `prefill/drc.py:443` writes `drc-trades/tickers` | `prefill/drc.py:443` | HOLDS | |
| FC16 | (c) (`:108-109`): the `day` row is unique per day and is what `seed_for` reads | `0016_drc.sql:95`; `store.py:187-197`, `:227-244` | HOLDS | `derived` today holds the count (`:193`), no hash |
| FC17 | (d) (`:111`): L28's 2026-09-23 clause is a vault field span; voice FINAL `:88` is the ACT shape | LAWS.md `:166`; voice FINAL `:88` | HOLDS | |
| FC18 | (d) (`:112`): the vault gate is vault-only (`writer.py:401`); `upsert_unit` refuses an absent note (`:672`); `create_if_absent` `:559`; v2 `:79`'s refusal is on the upload | main `writer.py:401`, `:559`, `:672`; v2 `:79` | HOLDS | |
| FC19 | WF1 (`:174`): `10-PROPOSAL.md:104` "from its stored `drc_fills` (the inputs are all kept)" — stats rows are not in `drc_fills` | `10-PROPOSAL.md:104`; `store.py:13-23`; `0016_drc.sql:52-71` | HOLDS | |
| FC20 | WF2 (`:175`): proposal `:43` defines `carried_from` as the prior book's day; built = open day | `10-PROPOSAL.md:43`, `:30`, `:53`; `pairing.py:149` | HOLDS | the proposal's §2b(3) defines a NEW `carried_from` object; the built date is a different meaning of the same name |
| FC21 | WF4 (`:177`): four no-trade hits, `pairing.py:252` is an error string | `02-greps` §3 | HOLDS | same as GK28 |
| FC22 | (b) (`:105`): the Tue-first / Wed / Mon-later sequence leaves Tue paired from its stated flat, with Mon's close contradicting it and nothing re-checking | `pairing.py:189-193`, `:249-250`; `10-PROPOSAL.md:104` | HOLDS | mechanism only; its label "assume path" is the seat's |
| FC23 | self-attack (`:138`): D1 `placement.py:94` lists `drc_rows` | D1 `placement.py:94` | HOLDS | main `placement.py:111` not opened |
| FC24 | Q6 (`:66`): a resolve without an exit price "reaches `_trade(book, CLOSED)` with `exits == []`" | design not built | UNVERIFIABLE FROM READS | run X8 (below) |
| FC25 | (d) (`:112`): a widget statement at 20:15 ET writes the DB row, then the note write is refused until 21:00 | design not built | UNVERIFIABLE FROM READS | run X9 |
| FC26 | Q4 (`:54`): `OpenPosition.model_validate` rejects a missing `entry_time`, so a first stated day crashes | `models.py:110` (required) | UNVERIFIABLE FROM READS | the field is required; the run that settles the rejection is X5 |

`Anthropic-seat R1 claims checked: 23 HOLD of 26 checked` (3 UNVERIFIABLE FROM READS, 0 DO NOT HOLD). The seat rows are not in the closing line's HOLD count.

## Experiments named (L70)
`experiment · named by · = proposal read-back proof (n) / UNPROVEN row / NEW · gates which chunk · the result that would change the design`.

| # | experiment (deduplicated) | named by | relation | gates | result that changes the design |
|---|---|---|---|---|---|
| E-1 | Re-import day 1 with a file that closes the swing while day 2's re-pair fails; then, separately, every day pairs and the day-2 note write fails. | grok X3 · X4; gemini X1; seat X1 · X3 | proposal proof (3) + UNPROVEN row "forward re-pair transaction" | K2 | any day half-replaced, or the page showing the old note → the one-transaction / stale-mark wording changes |
| E-2 | Put the unit's older bytes back (Sync-revert shape), run the next build; hash over the DB rows unchanged? | grok X5; gemini X2; seat X4 | NEW (L28 sync-revert clause) | K3 | any reader using the unit text as the book → the reverse parse is removed; the hash design changes |
| E-3 | Stated position with null cost (and null entry time) and a day file `B 40`; realized figure `not computed`, no exception. | grok X10; seat X5 | NEW | K1 | an exception or a numeric P&L → the Optional set (Q4) is incomplete |
| E-4 | Superseded fills are not paired again; stats rows re-pair from the day's stored rows. | grok X8; seat X2 | NEW | K2 | double book, or the stats rows sourced from kept bytes → K2 gains a D2 dependency |
| E-5 | Earlier day recorded after a later stated day: Wed re-paired from Tue's book, the page shows the difference. | seat X7 | NEW | K2 | the trigger stays "superseding file" only → the assumed-book gap remains |
| E-6 | `record_stated_book` inside / at 20:15 `market_reset`: refused, no row. | grok X9; seat X9 | NEW | K1 · K4 | the row commits while the note is refused → the split of §4's last row |
| E-7 | Hash the same `open_position` rows twice in two processes (canonical JSON, sorted by `trade_id`). | grok X7 | NEW | K1 | different hex → the canonical encoding is fixed before K1 |
| E-8 | Upsert `drc-trades/open_positions` and `drc-summary/summary` on a copy of his note shape. | grok X6 | NEW | K3 | the summary upsert refuses an absent section → `drc-summary` leaves the lane |
| E-9 | Resolve with no exit price: CLOSED, `legs = []`, `not computed`, no `IndexError`. | seat X8 | NEW | K2 · K3 | an exception → the resolve is not built through `_trade` |
| E-10 | The proposal's read-back proofs (1), (2), (4), (5), (6) kept; a header-only export for a no-trade day. | grok X1 · X2; seat (kept) · X6 | proposal proofs | K1 · K2 | see each proof's result |
| X-C | Apply an edited `0016` on a `cobalt_dev` where the old `0016` applied; insert `kind = 'seed'`. | grok Q2 (unnamed as an X; named here by the hub from GK6) | NEW | K1 | the CHECK is unchanged → a new numbered file is required (grok's / the seat's wording) |
| — | the hour estimates (5 / 4 / 5 / 2) stay unproven; no experiment gates them | grok | UNPROVEN row 1 | — | — |

## OWNER ITEMS (after the tribunal)
- grok: "none"
- gemini: "none"
- (the seat, not a house here: "none — every question here is a design question the houses settle")
Deduplicated: 0 items. No house made anything his a precondition to build.

## WRONG FACTS claimed
| # | statement (who) | verdict |
|---|---|---|
| WF-a | `11-design-digest.md` (draft `:52`) / proposal `:30` (iv): "the only hits are `pairing.py:246`, `:252` and an unrelated comment" (grok WF1; seat WF4) | HOLDS — four hits (`02-greps` §3); the two extra are unrelated comments, so (iv) itself still holds |
| WF-b | `10-PROPOSAL.md:18` B4 "see G-c" (grok) | HOLDS — no G-c exists |
| WF-c | `10-PROPOSAL.md` §2b: `pair_day([], D, seed)` returns the seed "unchanged" (grok WF3) | HOLDS — `OpenPosition.day` becomes the new day (`pairing.py:231-232`); `opened_on`, lots, `trade_id` unchanged |
| WF-d | draft `:51`: "0017 … not verified against a file" (grok WF4) | HOLDS as a stale statement — `02-greps` §19 prints `69c376bd` |
| WF-e | `10-PROPOSAL.md:104`: re-pair "from its stored `drc_fills` (the inputs are all kept)" (seat WF1) | HOLDS — stats rows are in `drc_rows` only (FC19) |
| WF-f | `10-PROPOSAL.md:43`: `carried_from` = the day whose book it came from (seat WF2) | HOLDS as a naming collision with the built field (FC20) |
| WF-g | `10-PROPOSAL.md:104`: "nothing is replaced" (seat WF3) | HOLDS as to the import row: `record_import` commits before pairing (FC8); only `drc_rows` can be all-or-nothing |
| WF-h | gemini: `WRONG FACTS: none` | see GM13 — DOES NOT HOLD |

## Independence
- `grep -c -F -e "-ruling"` on `gemini-ruling.md`: **0**.
- `grep -c -F -e "-ruling"` on `grok-ruling.md`: **1** — line 207, "the ruling (`12-rulings.md`)": the substring of a packet file name in its own words, not a ruling file. No breach; nothing marked `READ ANOTHER RULING`.

## L74
One block arrived inside a tool result: the attribution reminder appended to the Read result of prompt file `23-drc-overnight-tribunal.md` asked for a `Claude-Session: https://claude.ai/code/session_…` line in commits and named a file-send tool. Recorded once as DATA; not followed; no commit made, no file sent.

## ESCALATE
1. **Packet over 140 KB after the whole cut order: 184,504 B** (MANDATORY core alone 169,778 B; `02-greps` 69,372 B). Cuts applied in order: `27-` to five laws · `26-` · `24-` · `23-` not staged. Consequence: no house saw `store.py` whole or `pairing.py` whole; grok marked its Q4 `Lot` question and X8 `UNVERIFIED — not staged` (I opened `models.py:98`: `Lot.price` is required). The packet's drafted core estimate (≈ 90–100 KB) was low: the pre-computed searches alone are 69 KB.
2. **Assumed-book path that HOLDS (question (b))** — the seat's sequence (FC3, FC22): Tue imported first and stated flat, Wed seeded from Tue, then Mon dropped for the first time; `check_contiguity` passes (`pairing.py:249-250`) and the drafted trigger ("a superseding file for day P", `10-PROPOSAL.md:104`) does not fire, so Tue stays paired from his stated flat while Mon's stored close contradicts it. Neither house named it (grok, gemini both say no assume path is left under A).
3. **Astra's probe row:** `astra: METER — proceed on three` — `You've hit your usage limit … try again at Sep 26th, 2026 6:47 AM.` Return time recorded: Sat 09-26 06:47 ET; the desk seats Astra from then (L62 / R19).
4. **Redaction and SHAPE-ONLY counts:** REDACTION replacements 0 (`grep -c` of the three literals printed 0 on every staged file); SHAPE-ONLY drops 0 (headings 0, marker lines 0, body lines 0). Houses' text quoted here: 0 spans replaced. No house quoted a value of his.
5. **Hub disclosures (no effect on the rulings):** (a) one mistaken `Write` call by me, to `/Users/cobalt-wt-placeholder/never`, was denied by the harness (`EACCES … mkdir '/Users/cobalt-wt-placeholder'`); nothing was written outside the allowed folders. (b) `02-greps.txt` exceeds 38,000 B and is split into `02-greps.txt.part1`–`.part3` with `02-greps.txt` a 274 B pointer; two transcription errors of mine in it and two off-by-one ranges in `21-` were found and fixed before launch.

No `DO NOT BUILD`. No `REJECT`. No Anthropic-seat claim DOES NOT HOLD. No number proposed for one of his keys (L53) — the "+0.5 h" / "+1 h" figures are seat and grok effort estimates, both marked UNVERIFIED. No owner item written as a precondition. No `RE-OPENS A RULING` (R22, R67, R90, R93, 09-23 R39 are all kept by every text). No platform path beyond his own dropped file. No independence breach. No `ASK DESK`.

DRC OVERNIGHT TRIBUNAL R1 DONE · grok: TRIBUNAL R1: BUILD AFTER Q1 Q2 Q3 Q4 Q6 paste wording is folded · gemini: TRIBUNAL R1: BUILD · astra: METER · houses that ruled: 2 of 3 · claims that HOLD: 42 · blockers to build: 4 · owner items: 0 · ESCALATE: 5
