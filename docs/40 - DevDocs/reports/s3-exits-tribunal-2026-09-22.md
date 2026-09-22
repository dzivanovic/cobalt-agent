# S3 exits tribunal, round 1 — report named from PREFLIGHT row 1: date 2026-09-22

## §0 Headline
Grok and Gemini both ruled round 1 in full within the 20-minute window (astra skipped per today's own R13 — METER, proceed on three); both independently converge on the SAME two root defects — a two-transaction seam in `fill()`/`mark_filled` and a stale-`shares`-column stop recompute — which I verified myself against the real files (HOLDS both times). Grok: `BUILD AFTER` three named fixes; Gemini: `DO NOT BUILD` as specified. Fable's separate blind seat (also `BUILD AFTER`) converges on the identical two defects a third time; 7 of 8 sampled Fable claims file-checked HOLD (1 unverifiable-from-reads). Packet staged at 208144 B, over the 140 KB target even after all five required cuts (disclosed, not a failure). Status: R1 DONE, no FAILED. ESCALATE: 12.

Fable R1 claims checked: 7 HOLD of 8 checked.

## AUTHORIZATION
- R13 (`cto-2026-09-20.md:86`): "Push and approved everything... I'm expecting you to run for a while." — FOUND.
- R23 (`cto-2026-09-20.md:206`): "yes" — grok/agy through Mon 2026-09-21 23:59 ET — FOUND.
- R38 (`cto-2026-09-20.md:275`): "B with your addition" — stop-override authority — FOUND, carries required phrase.
- R46 (`cto-2026-09-21.md:57`): "For the designs and creations we need the higher level models" — FOUND, carries required phrase.
- Proposal committed: `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/30 - Design/S3-EXITS-PROPOSAL-2026-09-21.md"` → `b72b2047356f550a145f4090db1e4e2b9cc4328e` — NON-EMPTY.
- Proposal stop line committed: `git log -1 -S"S3 EXITS PROPOSED" -- "docs/40 - DevDocs/reports/s3-exits-design-2026-09-21.md"` → `b72b2047356f550a145f4090db1e4e2b9cc4328e` — NON-EMPTY.
- Launch row naming this file: `cto-2026-09-22.md:33` row **R34** (13:4x ET) — names `73-s3-exits-tribunal.md` explicitly, states stagger status, states date gate, states Astra METER re-issue. FOUND.
- Launch row committed: `git log -1 -S"73-s3-exits-tribunal.md" -- cto-2026-09-21.md cto-2026-09-22.md` → `000b46e6883680d43841b9a012d5b0a771766660` — NON-EMPTY.
- NO NEW RULE check against `08-bars-chunk-e-check.md`: all 14 allow strings + 3 deny strings counted ≥1 (grok/agy = 2 each, matching the setups R2 precedent; all others = 1). No Sol/Opus checker string present in this launch line.
- DATE + EXTENSION GATE: `date` → Tue Sep 22 13:39:45 EDT 2026. Date is 2026-09-22 → require a row extending grok/agy through 2026-09-22. Found: R39 (`cto-2026-09-21.md:50`, 16:48 ET, "All approved") carries the literal `Bash(grok *) and Bash(agy *) through 2026-09-22 23:59 ET`. Committed: `git log -1 -S"Bash(grok *) and Bash(agy *) through 2026-09-22" -- cto-2026-09-21.md cto-2026-09-22.md` → `77d4c5952ad405185f1d0110c887d3216129a438` — NON-EMPTY.
  - Noted, not relied upon: R34 also references a further "R30 extends grok/agy through 09-23 23:59" — not required for this gate and not verified further; today's authorization already stands on R39 alone.
- WINDOW CHECK: 13:39 ET is before 19:25 ET and before 23:20 ET → no window FAILED condition applies.
- **Result: AUTHORIZATION HOLDS. Proceeding.**

## PREFLIGHT
| rule | command | exit | allowed/DENIED + reason |
|---|---|---|---|
| date (gate, row 1) | `date` | 0 | Tue Sep 22 13:39:45 EDT 2026 — report named `s3-exits-tribunal-2026-09-22.md` |
| grok present | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` — allowed |
| agy present | `agy --version` | 0 | `1.2.8` — allowed |
| base folder | `ls scratch/tribunal-bars-0920` | 0 | exists (populated by many prior tribunals/checks) — allowed |
| recovery check | `ls scratch/tribunal-bars-0920/s3-exits-tribunal/r1` | 1 "No such file or directory" | FRESH RUN, no recovery needed |
| stagger s1 (38) | `tail -n 3 float-handicap-tribunal-2026-09-21.md` | 0 | `FLOAT HANDICAP TRIBUNAL R1 DONE ...` — not running, continue |
| stagger s2 (61) | `tail -n 3 stale-score-tribunal-2026-09-22.md` (2026-09-21 candidate: No such file) | 0 | `STALE SCORE TRIBUNAL R1 DONE ...` — not running, continue |
| stagger s3 (66) | `tail -n 3 setups-one-check-2026-09-22.md` | 0 | `SETUPS ONE CHECK DONE ...` — not running, continue |
| stagger s4 (68) | `tail -n 3 stale-marker-check-2026-09-22.md` | 0 | `STALE MARKER CHECK DONE ...` — not running, continue |
| stagger s5 (69) | `tail -n 3 ops-6a-check-2026-09-22.md` | 0 | `OPS 6A CHECK DONE ...` — not running, continue |
| astra launch shape | `grep -c -F "Experiment field: **reads started**" setups-tribunal-r2-2026-09-21.md` | 0 | `1` → the `< /dev/null` experiment is recorded as working (moot here — astra skipped, see below) |
| astra probe | NOT RUN | — | Today's `cto-2026-09-22.md:54` **R13** (09:4x ET, his word "A"): Codex meter out until Sat 2026-09-26 06:47 ET; the three queued design tribunals (`38`, `61`, `73` — this one) run THIS WEEK on Grok · Gemini · Fable **without Astra** (per-case override of L67's four-house floor, floor of three stands); Astra reads the derived FINAL when the meter returns. This prompt's own PREFLIGHT text (line 9) names the identical re-issue. Per its instruction: `astra: METER — proceed on three`, launch NOTHING for astra, proceed with Grok and Gemini. |

**PREFLIGHT: PASS (Grok + Gemini required; Astra: METER — proceed on three, per today's R13).**

## Packet
Staged at `scratch/tribunal-bars-0920/s3-exits-tribunal/r1/`, extracted from working-tree files under `/Users/cobalt/cobalt` (main, current HEAD) via anchor-verified line-range extraction (every anchor `grep -n`-checked before extraction; one drift found and corrected, see below), never through the Write tool (so no trailing-whitespace stripping risk) — trailing-whitespace check on the two whole-file copies (`10-PROPOSAL.md` source, `22-trade_note.py` source) both `0`, and both extracted with a plain copy/redaction-sed, byte-accountable.

**Per-file bytes** (final, after cuts): `00-READING-ORDER.md` 3293 · `01-QUESTIONS.md` 17737 · `02-greps.txt` 76053 · `10-PROPOSAL.md` 27282 (orig 27271; net +11 from redaction) · `11-design-digest.md` 7160 · `12-scope-and-rulings.md` 7419 · `13-templates-keys.md` 1045 · `20-fill-path.excerpt.py` 16405 · `21-cards-store.excerpt.py` 16886 · `22-trade_note.py` 6580 (orig 6580, exact — no redaction targets in this file) · `23-note-writers.excerpt.py` 9346 · `32-attestation-notify.excerpt.py` 4053 · `33-migrations.excerpt.sql` 2738 (cut, see below) · `34-r-expiry-panel.excerpt.py` 7266 (cut, see below) · `35-laws-excerpt.md` 4881 (cut, see below). **Packet total: 208144 B ≈ 52036 tokens (÷4).**

**Anchor drift found and corrected:** `12-scope-and-rulings.md`'s SPRINT-LADDER-v0_1.md range — the prompt's stated `## S3 — Exits + DRC on radar cards` at :586 has MOVED to real :606 (+20 lines, the file grew since the prompt was drafted). The range was shifted the same +20 (staged as :606-623) to preserve the intended span (the S3 table, the S3 smoke, the code prompts owed) — confirmed correct because the ladder's own DM-example line, named in the REDACTION rule as `:590`, is found at the shifted position :610 (590+20), consistent with a uniform +20 shift. No other anchor in the packet drifted from its stated line (all others confirmed exact via `grep -n`/`sed -n` before extraction).

**REDACTION (L32):** literal `TSLA`/`372.82`/`374.50` replaced with `[TICKER]`/`[PRICE]`/`[PRICE]` in every staged file. Occurrences replaced, by source location: `10-PROPOSAL.md` (proposal :139,:151) — TSLA×2, 372.82×1, 374.50×2; `11-design-digest.md` (author's report :43 — **this one was NOT in my first draft and was caught and fixed on a full-packet sweep**, see below) — TSLA×2, 372.82×1, 374.50×1; `12-scope-and-rulings.md` (ladder :610 shifted, Charter :145) — TSLA×4, 372.82×2, 374.50×2 combined. Total 17 literal occurrences redacted packet-wide. Final verification: `grep -c -E "TSLA|372[.]82|374[.]50" <file>` on all 15 staged files → `0` on every one (run twice, once mid-staging when the :43 leak was caught, once as a final full sweep after all cuts).

**Self-caught error, disclosed:** my first pass built `11-design-digest.md` WITHOUT applying the redaction sed (I had only checked the proposal file for the literals, not the digest report, despite the prompt naming "the author's report `:43`" explicitly as one of the four carve-out locations). A `grep -c` check on the output caught it before any house saw the folder; the file was rebuilt with redaction applied and reverified at `0`. No house was launched before this was fixed.

**Over-140KB cut order — ALL FIVE APPLIED, packet still over budget (disclosed here and in ## ESCALATE, per the prompt's own "not a failure" clause):**
(i) `34-r-expiry-panel.excerpt.py`: the `radar/evaluate.py:774-800` range removed (kept: replay/cards.py, cards/expire.py ranges).
(ii) `31-vaultwrite.excerpt.py`: removed whole.
(iii) `35-laws-excerpt.md`: cut from 11 laws (L1,L2,L3,L28,L29,L32,L42,L53,L57,L68,L70) down to L1,L3,L28,L53,L57,L70 only.
(iv) `33-migrations.excerpt.sql`: cut down to only the `db_migrations/__init__.py` and `placement.py` ranges (dropped the `0007_radar_cards.sql` two ranges and the `0002_card_stop_edits.sql` whole file).
(v) `30-cards-models.excerpt.py`: removed whole.

**Result: packet is 208144 B even after all five cuts** — 68144 B (≈49%) over the 140 KB target. Root cause: the MANDATORY core alone (files never subject to any cut: `01,02,10,11,12,13,20,21,22,23` = 185913 B) already exceeds both the 140 KB target and the drafter's own ≈125–135 KB estimate for that core (`s3-exits-tribunal-draft-2026-09-21.md` `## PACKET`), on its own, before any OPEN-AS-NEEDED file is added. The single largest contributor is `02-greps.txt` at 76053 B (847 lines total; no single command's output exceeds 400 lines, so no `02-greps-<n>.txt` split was triggered) — spot-checked and confirmed to be real, on-target search output (writer/transition/fill-column matches), not noise from an overly broad pattern or an unfiltered binary/vendor path. This is a genuine repo-growth fact since drafting, not a staging error, and is listed under `## ESCALATE`.

**Redaction beyond the three literals:** none found. No other ticker, price, share count or P&L of Dejan's was found in any staged file during extraction or during the full-packet review.

## CONTINUE
next: close the report with the final stop line (§4).

## Rulings table
`item · grok · gemini · astra · agreement · wording or reason, ≤25 words per house`

| item | grok | gemini | astra | agreement | notes |
|---|---|---|---|---|---|
| Q1 R_unit | ADOPT WITH: actual unit `\|entry_leg.price − stop_in_force\|`, not recomputed on later edits | ADOPT WITH: `actual \|fill - stop at fill\|` | — | 2-0 ADOPT WITH, same reading | both reject the planned unit; Fable's third read agrees, adds `r_planned` as a second named output |
| Q2 one `legs` table | ADOPT WITH: one table; keep `fills` declared, do not strike | ADOPT WITH: one table, `kind`, strike `fills` | — | split on striking `fills` | grok: declaration costs nothing, keep for later placement; gemini: strike it now |
| Q3 append-only corrections | ADOPT WITH: correction = new row same `(card_id,seq)`, no UNIQUE, writer enforces neighbor consistency under FOR UPDATE | ADOPT WITH: append-only + current view, correction rows | — | 2-0, same mechanism | Fable's `UNIQUE (card_id, seq) WHERE corrects IS NULL` is the sharper DDL form of both |
| Q4 keep fill columns | ADOPT WITH: keep as cache, written in same txn as entry leg + FILLED | ADOPT WITH: keep as cache | — | 2-0 identical | both note today's cache write is a SEPARATE transaction — HOLDS, verified |
| Q5 attestation at fill | ADOPT WITH: record + flag `sheet_mismatch` on entry leg only, never refuse | ADOPT WITH: record + flag sheet_mismatch | — | 2-0 identical | |
| Q6 "27% past plan" | ADOPT: = `distance_change_pct` under `compute_fill_recompute`, not price-vs-entry distance | ADOPT WITH: `drift_pct > P` | — | 2-0, same formula | Fable derives both algebraic readings coincide at 27 — independently confirms |
| Q7 DM ambiguity | ADOPT: refuse with candidate `TICKER#id` lines, never latest-wins | ADOPT WITH: refuse with candidates | — | 2-0 identical | |
| Q8 human note edit | ADOPT: human wins, override row, DB unchanged, no reverse parse | ADOPT WITH: override only, DB unchanged | — | 2-0 identical | |
| Q9 note timing | ADOPT WITH: synchronous after DB commit, banner on failure, idempotent CLI retry, no queue | ADOPT WITH: synchronous in the fill request | — | 2-0 identical | |
| Q10 TRIGGERED expiry | ADOPT: no new timer, `EXPIRABLE` covers it; caller coverage unproven (X5) | ADOPT WITH: existing radar expiry | — | 2-0 ADOPT | |
| Q11 ↺ target | ADOPT: `kind=reset` → `structural_stop` only, no in-trade trail; typed-equal stop stays `kind=edit` | ADOPT WITH: `structural_stop` at formation | — | 2-0 identical | |
| Q12 DM transport | ADOPT WITH: REST poll on existing HTTP path, interval is his setting, no default | ADOPT WITH: REST poll | — | 2-0, websocket rejected by both | |
| (a) fact base | ADOPT WITH: F1-32 stand w/ corrections; missed writer `store.py:607/622` (X8, unread); `cli.py:83` also calls `fill()`; F30 false | missed writers `:622` (state) and `:1032` (last_price); §2 false for O7 B (`IllegalTransition` on ARMED→FILLED) | — | both find missed writers; DISAGREE on O7 B's edge need | grok: no new edge, relax `strict` flag; gemini implies more; Fable sides with grok |
| (b) one fill path | ADOPT WITH: `fill(conn=)` pattern; today NOT one path; `fill()` commits BEFORE `mark_filled`'s UPDATE | two-transaction seam confirmed; `from_card` is a second rebuild path | — | 2-0 on the defect | **VERIFIED HOLDS** — I read `aset/store.py:185-257` and `cards/store.py:429-519` myself; `fill()` commits on its own connection before `mark_filled`'s separate `with self._connect()` UPDATE |
| (c) `legs` table | ADOPT WITH: Q3 rules + placement split (db_migrations vs cards/migrations); 4 running/state-disagreement scenarios named | UNIQUE can't survive corrections without a marker; double-tap race scenario | — | 2-0 substantively | Fable's partial-unique-index wording is the sharper fix both converge toward |
| (d) realized R | ADOPT WITH: Q1 formula; inputs on legs; no S3 aggregate; flags proposal is missing `direction` on entry leg | must use stop-in-force per exit leg; replayable; no n≥30 aggregate | — | 2-0 | grok's `direction`-column gap not named by gemini, confirmed real by Fable (§3 "reads ... direction and entry too") |
| (e) drift warning | ADOPT WITH: `drift_pct > P` alone, his setting; ATR/K/AND not in design; §4's two sentences contradict | smuggled `atr_working`/`>` vs `≥`/AND; contradiction; AND fails Charter's own 27% test on wide-ATR fixture | — | 2-0, essentially identical | **CONFIRMED three ways** — Fable independently REJECTs the same AND gate with the identical wide-ATR failing scenario |
| (f) stop override | ADOPT WITH: `in_trade_shares` should read tail leg's `running_after`, not the stale `shares` column | `record_stop_edit` reads `aset_sizings.shares`, which exits never update — critical defect, worked example | — | 2-0 identical | **VERIFIED HOLDS** — I read `cards/store.py:643-740` myself: `in_trade_shares=shares if state is CardState.FILLED else None` reads the `shares` column, and `mark_filled`'s UPDATE list (`aset/store.py:233-239`) never touches `shares`. Fable: this is a LIVE defect on main TODAY, independent of S3 (ESCALATE 3) |
| (g) DM line | ADOPT WITH: panel first; kill/resume checked before exits parser; coupling is process-death only (no listener exists today) | coupling flagged; crash scenario; prices each choice; O8 is his | — | 2-0 on kill-first | converges with Fable's "kill phrase checked FIRST on every post" |
| (h) trade note | ADOPT WITH: `trade_note_path` column, NULL on write failure, F14 reads the column not `find_trade_note_for_card` | O4 A/B both produce a two-note or missed-note failure under nearest-timestamp matching | — | 2-0 on the defect | grok's fix (store path on card, stop timestamp-matching) matches Fable's replacement wording |
| (i) attestation column | ADOPT WITH: Q5's three fields, entry leg only; `day_mode_id` has no current writer | record + flag; column not named anywhere in the proposal | — | 2-0 identical | |
| (j) Charter #16 | ADOPT: one entry fill, many exit legs; reconciles F11 + ladder; fractions are his (O1) | same reading; an OWNER item, not the tribunal's | — | 3-0 with Fable | |
| (k) platform boundary | ADOPT: NONE — grep hits are comments/refusals only | NONE | — | 3-0 with Fable, unanimous | **VERIFIED** — `02-greps.txt`'s platform-name grep is docstrings and refusal messages only |
| (l) chunks/hours | ADOPT WITH: C3/C4 sequential not parallel; C5 gated on O8=A; re-derived hours 30-38h/42-53h, HIGHER than proposal's 35/50; migration-number collision with `0012` | C3 and C4 cannot truly be parallel — same fill path | — | 2-0 on the parallel-claim being wrong | grok's fix (shared orchestrator) matches Fable's (b) replacement — 3-way convergence on mechanism |
| (m) F14/F15 seams | ADOPT WITH: leave `trade_note_path`/`legs_current_v`/Q1 function/both stops; (f)'s seam is real; miss-line clock is not this design's problem | seams left; miss-line clock unaffected, a ladder issue not a design issue | — | 2-0 identical framing | |
| (n) experiments | 12 named (X1-X12) | 2 named (X1-X2) | — | see `## Experiments named` | |
| closing line | `TRIBUNAL R1: BUILD AFTER one fill transaction, running-share risk, correction chain checks` | `TRIBUNAL R1: DO NOT BUILD 5 write paths with a broken risk recompute and two-transaction seam` | — | both name the SAME two root defects (transaction seam, share-count recompute) but weigh them differently — grok: fixable preconditions to BUILD AFTER; gemini: severe enough to DO NOT BUILD as currently specified | |

## Wording offered, verbatim
Full per-item text is preserved unedited in `grok-ruling.md` and `gemini-ruling.md` (staged folder) for the derive step to paste from directly — not reproduced in full here to keep this report to a workable length, per the operative sentence of each item:

**GROK**, operative ADOPT/REJECT sentence per item (full reasoning + scenario follows each in `grok-ruling.md`):
- Q1: "R_unit is `\|entry_leg.price − entry_leg.stop_in_force\|` (actual fill, his stop at fill). It is not `\|card.entry − stop\|`. It is not recomputed when a later leg stores a different stop."
- Q2: "One `\"user\".legs` table covers the entry and the exits. `fills` stays in `DECLARED_TABLES` as USER and is not built. Do not strike it."
- Q3: "A correction is a new row with the same `(card_id, seq)` and `corrects` = the current head's id. No UPDATE and no `is_current` flag."
- Q4: "Keep `aset_sizings.actual_fill`, `recomputed_shares`, `recomputed_used_risk`, `share_delta`, `distance_change_pct`, and `filled_at` as a cache of the entry leg plus `compute_fill_recompute`. Write them in the same transaction as the FILLED transition and the entry leg."
- Q5: "Do not refuse the fill. The entry leg records `day_mode_id`, `attested_sheet`, and `sheet_mismatch boolean NOT NULL`."
- Q6: "It means `distance_change_pct = 27` under `compute_fill_recompute`... It does not mean the fill price is 27% away from entry."
- Q7: "Zero or more than one card in the required state → `NOT RECORDED` plus the candidate `TICKER#id` lines. Never the latest card."
- Q8: "Human wins, override row, the DB leg is not changed. No reverse parse."
- Q9: "Write the note in the same request, after the DB commit. On failure the card stays FILLED, the banner is `FILLED — trade note NOT written: <reason>`, and `cobalt cards trade-note <card_id>` runs the same `upsert_trade_note` plus one `upsert_unit` per current leg."
- Q10: "No new timer. `EXPIRABLE` is WATCH, ARMED, TRIGGERED... `radar_expiry` applies avoid and deadline to all three, and stop-touch to WATCH only."
- Q11: "↺ writes a stop edit with `kind = reset` and `to_stop = structural_stop` from formation. There is no in-trade trail in this design. Do not build one."
- Q12: "REST poll, using the HTTP path `notify/mattermost.py` already has. No websocket. The poll interval is his (L53 cadence), not an engine tunable and not a committed default."
- (b): "`fill(conn=...)` follows `transition()`'s rule: commit only if it opened the connection. `mark_filled` opens one connection, passes it in, and before commit inserts the entry leg and runs the fill-column UPDATE."
- (e): "The warning is `distance_change_pct > P`, P his setting in `\"user\".trader_settings`, no committed default. The hard-coded 25 dies. The ATR term, K, `atr_working` versus the daily ATR, `≥` on K, the AND, and \"latest receipt\" are not in the design."
- (f): "His stop remains `aset_sizings.stop`. `structural_stop` stays visible. ↺ is `kind=reset` to that formation stop (Q11)... In FILLED, `record_stop_edit` passes `in_trade_shares` = the tail current leg's `running_after` when an entry leg exists, otherwise the `shares` column (legacy cards with no legs)."
- Closing: `TRIBUNAL R1: BUILD AFTER one fill transaction, running-share risk, correction chain checks`

**GEMINI**, full per-item answer (already terse — quoted in full above under each item's grep, reproduced here verbatim from `gemini-ruling.md`):
- Q1: "`actual \|fill - stop at fill\|`" · Q2: "`one legs table with kind, striking fills`" · Q3: "`append-only legs with correction rows + current view`" · Q4: "`keep aset_sizings.actual_fill columns as a cache`" · Q5: "`record + flag sheet_mismatch`" · Q6: "`drift_pct > P`" · Q7: "`refuse with candidates`" · Q8: "`override only, DB unchanged`" · Q9: "`synchronous in the fill request`" · Q10: "`existing radar expiry`" · Q11: "`structural_stop at formation`" · Q12: "`REST poll`"
- Closing: `TRIBUNAL R1: DO NOT BUILD 5 write paths with a broken risk recompute and two-transaction seam`

## Checked against the files
I opened the real files myself (Read tool, working tree under `/Users/cobalt/cobalt`, current at collate time) for every load-bearing claim both houses converged on, plus a sample of disputed and WRONG-FACTS claims:

| claim | who | file:line | verdict | note |
|---|---|---|---|---|
| `mark_filled` and `fill()` are two separate transactions/connections, not one | grok (b), gemini (b), Fable F36 | `aset/store.py:185-257`, `cards/store.py:429-519` | **HOLDS** | `filled = CardStore(self.db_name).fill(...)` runs and commits (`conn.commit()` inside `fill()`) on its own connection; `mark_filled` then opens a SEPARATE `with self._connect() as conn:` block for the fill-column UPDATE |
| `record_stop_edit`'s `in_trade_shares` reads the stale `shares` column, never updated by exits | grok (f), gemini (f), Fable ESCALATE 3 | `cards/store.py:643-740` (line 720), `aset/store.py:233-239` | **HOLDS** | verified: `in_trade_shares=shares if state is CardState.FILLED else None` reads `shares` from the `SELECT ... shares ... FROM aset_sizings`; `mark_filled`'s UPDATE list (`filled_at, actual_fill, recomputed_shares, recomputed_used_risk, share_delta, distance_change_pct`) never assigns `shares` |
| proposal `:3` pins main at `be58530`, stale | grok WRONG FACTS #1 | `10-PROPOSAL.md:3` vs `git log -1 main` | **HOLDS, and worse than grok found** | grok's own greps captured `67bc19b`; main has moved again since, to `1a3f5cf` as of my check — confirms this is a genuinely moving target, not a one-off staleness |
| F30 "`setups/seven-0921` and `s2/stale-marker-0921` do not exist" | grok WRONG FACTS #2, Fable WRONG FACTS (F30) | `10-PROPOSAL.md:42` (F30, not `:41` as grok cited — off by one line) | **HOLDS** | both branches exist: `setups/seven-0921` is 18 commits ahead of main (grok/Fable said 17 — branch grew further since their reads); `s2/stale-marker-0921` is 0 commits ahead (already merged into main), confirmed by direct `git log --oneline main..<branch>` |
| F8 "a radar card reaches FILLED only through `/card/{id}/move`" | grok WRONG FACTS #4 | `10-PROPOSAL.md:20` (F8, not `:19` — off by one), `cards/cli.py:60-91` | **HOLDS** | `cmd_move` in the CLI also calls `store.fill()` for a move to `FILL_TARGET` — a second caller, though the code comment itself says "a radar card is refused here too", so F8's substance (radar refused) stands even though its "only" claim about callers does not |
| F16 "today TRIGGERED is only his sheet button" | Fable WRONG FACTS | `cards/cli.py:88-100` | **HOLDS** | the CLI's generic `else` branch calls `store.transition(...)` for any non-FILL_TARGET state including TRIGGERED — a second path to TRIGGERED beyond the sheet button |
| "`radar_panel.py` was touched twice today on main" | Fable WRONG FACTS | `git log --oneline -- src/cobalt/aset/radar_panel.py` | **HOLDS** | four commits touch it: `a660a7c`, `04b0dbd`, `71a8368`, `490c231` — confirmed exactly |
| `cards/store.py:607/622` is a writer of `state`/`card_transitions` distinct from `transition()` | grok (a) X8 (flagged unread), gemini (a) (stated as fact) | `cards/store.py:560-629` | **HOLDS** | the containing function is `def create_state(` at line 560, not `transition()` (line 239) — a second writer confirmed to exist; grok's more cautious framing ("name unread") is the better-calibrated one since whether it is a live-card mover or a one-shot genesis writer (Fable's read: "genesis... not a fill path") was not settled by either grok or gemini themselves |
| ladder anchor `## S3 — Exits + DRC on radar cards` at `:586`, DM line at `:590` | (packet-staging finding, independently confirmed by Fable's own WRONG FACTS) | `SPRINT-LADDER-v0_1.md` | **HOLDS, self-consistent** | I found and corrected the same drift while staging (see `## Packet`): real position is `:606` (heading) / `:610` (DM line), a uniform +20-line shift. Fable independently found the identical shift (`:590`→`:610`, `:596-599`→`:615-618`) from its own unstaged full read of the ladder — cross-confirms the packet's staging correction was right |
| §9 L52 finding — nothing this design proposes feeds a score, a rank, or an admission | grok (k) (implicit, via NONE on the platform boundary — a related but separate finding), Fable (explicit check) | `src/cobalt/cards/scoring.py`, `cards/radar.py`, `radar/evaluate.py` | **HOLDS** (Fable's explicit check, not independently re-run by me beyond spot-checking that no chunk C1-C6 touches those three files per the proposal's own chunk table) | listed under `## ESCALATE` per the task's own rule (any claim that the design DOES reach scoring that HOLDS is escalated; here the opposite — that it does NOT reach scoring — HOLDS, which is the reassuring direction, still listed for visibility per L52) |

## Fable round-1 claims, file-checked
`ls` both candidates: `s3-exits-tribunal-fable-r1-2026-09-21.md` — No such file; `s3-exits-tribunal-fable-r1-2026-09-22.md` — exists. `tail -n 3` on the latter: last non-blank line starts `S3 EXITS TRIGGERED FABLE R1 DONE` — reading its full text: closing line is `S3 EXITS TRIBUNAL FABLE R1 DONE · verdict: BUILD AFTER derive folds same-transaction fill, leg lock, pct-only warning, 0014 numbering · adopt: 6 · adopt with wording: 19 · reject: 1 · experiments named: 12 · ESCALATE: 5`. Read in full (`## Rulings`, `## Self-attack`, `## WRONG FACTS`). This seat ran BLIND (did not read the houses' folder), independently, from its own full un-staged reads of the real files (it read `LAWS.md`, the proposal and the design-digest report whole, plus its own line-range selections — not this hub's packet). File-checked below (a representative set focused on its most load-bearing and its WRONG-FACTS claims; its remaining ADOPT WITH items overlap the items already verified above and are not re-verified a third time):

| id | claim (Fable report line) | file:line | verdict |
|---|---|---|---|
| FC1 | F36: "`mark_filled` is TWO transactions: `fill()` commits (`cards/store.py:519`), then a second connection UPDATEs the fill columns" (`:107`) | `cards/store.py:519`, `aset/store.py:230-250` | **HOLDS** — same verification as grok/gemini's convergent claim above |
| FC2 | ESCALATE 3: "a FILLED stop edit on the manual sheet recomputes open risk from the planned `shares` column... which the fill recompute never updates" (`:271`) | `cards/store.py:720`, `aset/store.py:233-240` | **HOLDS** — same verification as grok/gemini's convergent claim above; Fable additionally frames it as a LIVE defect on main today, independent of S3 — I did not independently re-derive that framing but it follows directly from the same code read |
| FC3 | F30 corrected: "at 13:4x ET 2026-09-22 both branches exist: `setups/seven-0921` is 17 commits ahead of main; `s2/stale-marker-0921` (`cddf32c`) is 0 commits ahead" (`:109`) | `git log --oneline main..<branch>` | **HOLDS, count now 18 not 17** — `s2/stale-marker-0921`'s head commit and 0-ahead count both confirmed exactly; `setups/seven-0921`'s ahead-count grew from 17 to 18 between Fable's read and mine (elapsed time, not an error) |
| FC4 | WRONG FACTS: "F16 ... also `cobalt cards move <id> TRIGGERED` (`cards/cli.py:91-99`)" (`:252`) | `cards/cli.py:88-100` | **HOLDS** |
| FC5 | WRONG FACTS: "`radar_panel.py` was touched twice today on main → four commits touch it since (`a660a7c`, `04b0dbd`, `71a8368`, `490c231`)" (`:256`) | `git log --oneline -- src/cobalt/aset/radar_panel.py` | **HOLDS**, all four SHAs confirmed exactly |
| FC6 | Ladder citation drift: "the S3 block is at `:606-623`; the smoke at `:615-618`" (`:251`) | `SPRINT-LADDER-v0_1.md:606-623` | **HOLDS** — matches my own independent staging-time correction exactly |
| FC7 | §9 L52 finding "HOLDS: no chunk touches `cards/scoring.py`, `cards/radar.py` or `radar/evaluate.py`'s scoring" (`:257`) | proposal §10 chunk table vs those three files | **HOLDS** (spot-checked, not exhaustively re-derived) |
| FC8 | "genesis" characterization of `cards/store.py:622`'s writer (`:112`) | `cards/store.py:560-629` (`def create_state`) | **UNVERIFIABLE FROM READS beyond confirming the function name** — Fable asserts it is specifically a genesis/backfill writer and "not a fill path, so no ruling turns on it"; I confirmed the function is `create_state`, distinct from `transition()`, but did not trace every call site to confirm it can never move a live card (the same gap grok flagged as its own X8) |

Fable R1 claims checked: 7 HOLD of 8 checked (FC8 unverifiable-from-reads, not a failure to hold — it is an open question grok also left open as X8).

## Experiments named (L70)
Deduplicated by what each actually runs (grok's X-numbers, gemini's, and Fable's overlap heavily on the same handful of real questions):

| experiment | named by | gates which item | result that would change the design |
|---|---|---|---|
| Two-connection crash between `fill()` commit and the fill-column UPDATE | grok X1 (says "not an experiment, already in staged code"), Fable X7 | (b) | if a constructed failure leaves the card FILLED with NULL fill columns today, confirms the seam must close in C1 |
| Dev-vault: blank `trade_def`/no `strategy` key, does the daily dataview omit the row | grok X2, gemini's implicit F25 concern, Fable X3/X4 | (h), F25 | if the note is omitted rather than shown blank, his template (not a Cobalt key) needs a fix before F22 can pass |
| `create_if_absent` + `upsert_unit` twice, then a hand-edit, then retry | grok X3, Fable X1 | Q8/Q9 | if the retry overwrites his line without an override row, Q8/Q9's "human wins" needs a stronger writer guard |
| `cobalt_dev`: append-only `legs` UPDATE-refusal + duplicate-seq insert + correction chain | grok X4, Fable X5 | Q3/(c) | if UPDATE is allowed, the append-only claim is false and Q3 changes; if the view returns two rows per seq, the partial-UNIQUE wording needs revision |
| TRIGGERED card left past `expires_at`, does the radar resident expire it | grok X5 | Q10 | if it does not, the caller (not `EXPIRABLE` itself) needs a fix, not a new state or window |
| `structural_stop` NULL on a manual `aset_sizings` row | grok X6 | (f) | if NOT NULL is enforced for every origin, the manual-card exception in the `legs.cobalt_stop` design must be dropped |
| Two concurrent ½-exit taps on one FILLED card | gemini's implicit concern, grok's (c) scenario 3, Fable X6 | (c) | two 50-share legs (running goes negative/wrong) instead of one 50 + one refused confirms the card-row-lock claim is insufficient as designed |
| `FILL_MATCH_TOLERANCE_SECONDS` value (not in the excerpt) | grok X7, Fable's tolerance note (`:67`, 30s) | (h) | if ≥ 1920s, a 09:40 and a 10:12 note can both match by accident under `find_trade_note_for_card`; Fable already read the constant as 30s directly — grok flagged it unread, a minor completeness gap in grok's own read, not a contradiction |
| `cards/store.py:531-642`'s unread writer at `:607`/`:622` | grok X8, Fable's "genesis" read | (a) | if it can move a live card, S3 must route or delete it before C1; if a one-shot backfill, not a hole — **UNSETTLED between grok and Fable, see FC8** |
| `SizingResult.from_card` vs `compute_sizing` on a persisted card | grok X9 | (b) | any default divergence changes `distance_change_pct` and the warning — fix the copy, not a second formula |
| Dev bot: `GET /api/v4/channels/{id}/posts` on a DM channel, credential scope | grok X10, Fable X8 (dedupe-by-user-id angle) | (g) | a 403 gates O8 A on this credential; Fable adds: the bot's OWN replies must also be skipped, not just by post id |
| `cobalt jobs restarts` on the C1-C5 file set | grok X12 (folded into it), Fable X9 | (l) | replaces every house's RESTARTS section with a measured list instead of a guess (L42) |
| `matches_kill_phrase` is exact-match, not substring | grok X11 (settled by read, not a run) | (g) | already confirmed by read, not an open experiment — kept here only because grok listed it |

Kept from the proposal's own §11 (not struck by any house): the 27%-drift Decimal derivation (confirmed correct by both grok Q6 and Fable X10, independently, same arithmetic), the with-DB fill-crash sequence, the dev-vault note-write sequence. Struck: the proposal's "fixture's ATR chosen so `drift_atr ≥ K`" framing — REJECTed as circular by Fable (e) and effectively the same objection grok and gemini raise for (e).

## OWNER ITEMS (after the tribunal)
Deduplicated, beside the proposal's O1-O8:
- O1 (⅓/½ rounding), O2 (drift pct threshold P + comparator), O3 (ATR floor K, or A: no gate until he names it), O4 (manual-sheet note timing, REFRAMED by Fable as A: create-at-sizing-refresh-at-fill vs B: create-only-at-fill), O5 (blank-field fill-in policy), O6 (`trade_def` on a radar note), O7 (radar fill before S4 — B priced by all three as a `strict`-flag relax, no new edge), O8 (DM line in S3 or after — priced by all three; none treat it as a precondition) — as the proposal frames them, none contradicted.
- O9 (missing, named by grok AND Fable independently): which ATR term, `atr_working` vs daily ATR, if he later wants one.
- O10 (missing, named by grok AND Fable independently): the DM poll interval value/key.
- O11 (missing, Fable only): the heartbeat RED rule (N missed polls) for the DM listener.
- O12 (missing, Fable only): whether a radar fill also writes the daily note's FILL UPDATE block the way the manual sheet does.
- O13 (missing, Fable only): the daily dataview's `strategy` vs `trade_def` column — his template, outside S3 (ESCALATE 5 in the original proposer's report).

No house made an owner item a precondition to BUILD.

## WRONG FACTS claimed
| claim | house | file:line cited | file-check verdict |
|---|---|---|---|
| proposal `:3` pins main at stale `be58530` | grok | `10-PROPOSAL.md:3` | HOLDS (see Checked against the files) |
| F30 says both branches don't exist; they do | grok, Fable | `10-PROPOSAL.md:42` | HOLDS (see Checked against the files) |
| F19's unit is "stop at fill", proposal calls it "stop in force at fill" — same stop, imprecise label | grok | `10-PROPOSAL.md:99`, `34-r-expiry-panel.excerpt.py` | HOLDS as a labeling imprecision — not independently re-derived beyond confirming F12's docstring says "stop at trigger"; since `STOP_EDITABLE` excludes ARMED/TRIGGERED (confirmed by both grok and Fable), stop-at-trigger and stop-at-fill are the same value, so this is a wording nit, not a substantive error |
| F8 "only `/card/{id}/move`" | grok | `10-PROPOSAL.md:20` | HOLDS, partially (see Checked against the files — the CLI is a second caller, but F8's radar-refusal claim itself is not wrong) |
| `:113`/`:161` "missing setting refuses" contradicts `:114` "never blocks" | grok, Fable | `10-PROPOSAL.md` §4 | HOLDS — confirmed by reading the proposal's own §4 text (staged in `10-PROPOSAL.md`), the two sentences are in the same section and do state opposite behaviors for a missing setting |
| F33 "no source text in the ladder" for the ATR-scaling phrase | grok, Fable | `10-PROPOSAL.md:46`, `SPRINT-LADDER-v0_1.md:610`/`:621` (shifted) | HOLDS — the ladder DOES carry "drift warning scaled to ATR (his 09-03 defect)" and "ATR-scaled drift" text; what remains genuinely unsourced is only the "09-03 defect" ORIGIN, not the phrase's existence |
| "radar expiry incl. TRIGGERED" in the digest is the predicate, not a shown caller | grok | `11-design-digest.md:31` | listed by grok as "not a false predicate", i.e. grok itself does NOT claim this is wrong — included in grok's list only as a caution against over-reading it; no file-check verdict needed, it is not an assertion of falsity |
| `10-PROPOSAL.md:178` "fill writes the entry leg in `fill()`'s transaction" | gemini | `10-PROPOSAL.md:178`, `aset/store.py:217-233` | HOLDS as a design-risk flag, though better categorized as a restatement of the (b) two-transaction finding than a standalone wrong fact about CURRENT state — the quoted text is a stated future design INTENT, not a false claim about what exists today; the underlying tension it points at is real and already captured under (b) |
| `10-PROPOSAL.md:60` "CLOSED written in the same transaction as the zero-running leg" | gemini | `10-PROPOSAL.md:60` | same categorization note as above — a design-intent statement, not a current-state falsehood; confirmed the quoted text is verbatim present at that line |
| F16 "TRIGGERED only via sheet button" | Fable | `cards/cli.py:91-99` (real: `:88-100`) | HOLDS (see Checked against the files) |
| §5 "the edit path already recomputes open risk... nothing new is needed" | Fable | `10-PROPOSAL.md` §5, `cards/store.py:720` | HOLDS — same defect as (f) above, independently phrased |
| §7/F21 "the body is his template's... verbatim" | Fable | `prefill/trade_note.py:93-104` | HOLDS as far as verifiable — confirmed `_render_body` is a hardcoded string literal in the Python source, not a read of the vault template file at write time; whether the literal still matches the template's current wording is Fable's own X2, correctly left as an experiment (L32 bars me from reading the template body to check further) |
| `radar_panel.py` "touched twice" | Fable | git log | HOLDS (see Checked against the files) |
| §9 L52 finding HOLDS (not wrong — recorded as checked) | Fable | proposal §9 | HOLDS, not a wrong-fact — Fable itself frames this as confirming the proposal is correct, listed under WRONG FACTS only per the section's own instruction to record every such check |

## Independence
`grep -c -F -e "-ruling"`: `grok-ruling.md` → 10 (all ten are references to the packet file `12-scope-and-rulings.md`, or grok's own "No `-ruling` file was read" line — read and confirmed line-by-line, none names `gemini-ruling.md`/`astra-ruling.md`) · `gemini-ruling.md` → 0. **No independence breach.** Astra was never launched, so no astra output exists to check.

## ESCALATE
1. **Two-transaction seam in `fill()`/`mark_filled`** — CONFIRMED HOLDS by my own file read, independently found by all three houses (grok (b), gemini (b), Fable F36/Q4). A crash between the two leaves a card FILLED with no fill price/shares recorded and no retry path (the retry raises `IllegalTransition` since the card is already FILLED). This is a REJECT-class claim under grok's own DO-NOT-BUILD-adjacent framing and gemini's explicit DO NOT BUILD line; it HOLDS.
2. **Stop-recompute uses the stale `shares` column, never updated by exits** — CONFIRMED HOLDS by my own file read, independently found by all three houses (grok (f), gemini (f), Fable ESCALATE 3). Fable additionally frames this as a LIVE DEFECT ON MAIN TODAY, independent of whether S3 is ever built — flagged here for visibility even though it predates this design.
3. **Packet over 140 KB even after all five required cuts** (208144 B final, 68144 B / ≈49% over target) — disclosed fully in `## Packet` above; not a staging failure per the prompt's own "not a failure" clause, but a real finding about the mandatory core's size versus the drafter's estimate.
4. **The drift-warning AND gate (`drift_pct > P` AND `drift_atr ≥ K`) fails the Charter's own acceptance test on a wide-ATR fixture** — independently derived THREE times (grok (e), gemini (e), Fable's explicit REJECT with the same wide-ATR scenario). All three converge on dropping the AND and firing on `drift_pct` alone.
5. **`C3 ∥ C4 ∥ C5` "parallel" claim is false as written** — both grok and gemini find C3/C4 touch the same fill-request code path; Fable's fix (a shared orchestrator function, `aset.fill_card(...)`) is the only one of the three that resolves it rather than just naming it, and matches grok's independently-proposed `fill(conn=...)` seam in spirit.
6. **Q2 split**: grok says keep `fills` declared in `DECLARED_TABLES` (do not strike), gemini says strike it now. Neither is a precondition; flagged as an unresolved 1-1 split between the two houses that ruled it (Fable ADOPTs Q2 outright, siding with striking it, giving 2-1 for striking overall — but the hub takes no side, per L37).
7. **`create_state`'s writer at `cards/store.py:560-629` (lines 607/622) is unsettled** — grok flags it as unread (X8), Fable characterizes it as a genesis/backfill writer "not a fill path", neither fully traces its call sites; I confirmed only that the function exists and is distinct from `transition()`. Whether it can move a LIVE card (a potential L3 one-path violation) is UNVERIFIABLE FROM READS as far as I traced it — an experiment, not a confirmed defect (L70).
8. **Redaction, disclosed in full**: 17 literal occurrences of `TSLA`/`372.82`/`374.50` redacted across the packet (see `## Packet`); one was caught and fixed mid-staging before any house saw the folder (the design-digest report's line 43, not originally checked).
9. **Anchor drift, disclosed in full**: the `SPRINT-LADDER-v0_1.md` S3-section anchor moved +20 lines from the prompt's stated position; corrected during staging and independently cross-confirmed by the Fable seat's own unstaged full read of the same file (its WRONG FACTS section names the identical real line numbers).
10. **No `ASK DESK` was needed** — both required houses ruled in full within the 20-minute window (grok: ~15 minutes; gemini: ~3 minutes); astra was never launched per today's already-ruled R13 (METER — proceed on three), so no astra-specific escalation applies.
11. **No claim that this design reaches scoring, ranking, or admission HOLDS** — the opposite (that it does NOT) HOLDS, per Fable's explicit check (§9 L52 finding), listed here per the section's own instruction to record it either way.
12. **No path to a trading platform HOLDS** — unanimous NONE across all three houses (k), confirmed by my own read of the platform-name grep results (comments and refusal messages only).

## Clock
| time | trigger | running houses | action |
|---|---|---|---|
| 13:39:45 ET | preflight | none launched yet | — |
| 13:56:35 ET | pre-launch date check | none yet | within window (before 19:25 and 23:20 ET) |
| 13:56:56 ET | both houses launched | grok `bkdvz5tu0` (launched 13:56:35, deadline 14:16:35) · gemini `bcjmbb3tr` (launched 13:56:56, deadline 14:16:56) | launched together per §2, `run_in_background`, neither pointed at the other's ruling |
| 13:59:40 ET | gemini completion notice | grok still running (deadline 14:16:35) | gemini exit 0, printed answer ending `TRIBUNAL R1: DO NOT BUILD 5 write paths with a broken risk recompute and two-transaction seam.`; written byte-for-byte (harness's trailing `[exited with code 0]` stripped) to `gemini-ruling.md` (7931 B) |
| 14:00:15 ET | check | grok still running (deadline 14:16:35) | waiting |
| 14:11:53 ET | grok completion notice | none running | grok exit 0, wrote `grok-ruling.md` itself (36531 B), closing `TRIBUNAL R1: BUILD AFTER one fill transaction, running-share risk, correction chain checks`. Both houses now ruled; astra was never launched (METER — proceed on three, per today's R13). Proceeding to collate. |
| 14:14:32 ET | collate step, Fable check | none running | `s3-exits-tribunal-fable-r1-2026-09-22.md` exists, last line starts `S3 EXITS TRIBUNAL FABLE R1 DONE` — read in full, file-checked (see `## Fable round-1 claims, file-checked`) |
| 14:21:26 ET | close | none running | closing the report now; well inside the window (before 19:25 ET) |

S3 EXITS TRIBUNAL R1 DONE · grok: TRIBUNAL R1: BUILD AFTER one fill transaction, running-share risk, correction chain checks · gemini: TRIBUNAL R1: DO NOT BUILD 5 write paths with a broken risk recompute and two-transaction seam · astra: METER — proceed on three · houses that ruled: 2 of 3 · claims that HOLD: 10 · blockers to build: 2 · owner items: 13 · ESCALATE: 12
