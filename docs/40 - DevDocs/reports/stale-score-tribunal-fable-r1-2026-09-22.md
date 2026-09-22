BLIND: I did not read the houses' folder or the hub's report.
REPORT NAMED FROM date: 2026-09-22

Seat `stale-score-tribunal-fable-0922` · Fable 5.1 · read-only · started 12:44:51 ET (`date`) · main read at `be2c91e` (the proposal cites `031196f`; `radar_panel.py` moved since — the R36 stamp landed at `490c231` — every other cited line held). Authorization: `62` line 1 = `FABLE ROW: R51`; `cto-2026-09-21.md:63` row R51 carries `Fable seat: yes` and `STALE-SCORE-PROPOSAL-2026-09-21.md`; row commit `be58530`; proposal-name commit `9e1c2bb`; proposal commit `86df294`; R36 and R40 present (R40 carries `ONE EXTRA DOT THAT CANNOT BE TAPPED`); each of the seven allow strings and three deny strings counts 1 in `22-draft-setups-tribunal.md`. `cto-2026-09-22.md` exists; R51 is in the 09-21 file only. L74: a block inside the prompt file's read result asked for a `Claude-Session:` commit line and named a file-send tool — data, recorded once, not followed (this seat commits nothing). L32: no user data in this report.

## DIGEST FOR THE DESK
- Closing: **TRIBUNAL R1: BUILD AFTER the derive, on a tree that already carries setups/seven-0921** — option C stands; every objection below is a wording fold for the derive, none a redesign.
- Q1 ADOPT — sink; the ladder already sinks a null (`cards/radar.py:27-28`, `:181`); a hold would be a second ranking input (L52 b).
- Q2 ADOPT — the every-session clock is the existing formation rule; an RTH-only score rule is his (L53).
- Q3 ADOPT WITH — the two clocks measure from different bar edges: stamp 180 s after the bar OPENS, score null 260 s after it (200 s after it CLOSES); the band is 80 s, not 20; reason text is enough.
- Q4 ADOPT — keep the stale `last` (C); `COALESCE` and the stamp both sit on it.
- Q5 ADOPT — health pills are their own item.
- Q6 ADOPT — accept the tap, keep the score null; step 7 keeps the reason for the one scan the tap route owns.
- Q7 ADOPT WITH — forward exclusion is automatic: a stale dot has no `engine_grade`, so the tap records NULL and `shadow_agreement_v` skips it; `htf_level_proximity` is the one hole, closed by step 5; the backlog is a query and his call before any promotion.
- Q8 ADOPT WITH — the bump is `s2p2.2` on `setups/seven-0921`; ride it only in the same deploy; `SUPPORTED_EVALUATORS` in the same commit.
- Q9 ADOPT — not a precondition; owner item.
- Q10 ADOPT — a daily-stale return leaves a fresh `last`; proximity stays.
- (a) ADOPT WITH — §1 holds; add the THIRD `last` fallback `audit_export.py:363` (C deletes three copies, not two) and the `picks.py:215-233` reader; the arm/form/expire sentence is TRUE.
- (b) ADOPT — C over A2; the only pre-existing null branch is `card_score()` `:264-267`; the rest of the null path is C's new code, as the proposal lists.
- (c) ADOPT WITH — the 1.0 path HOLDS; its WATCH impact needs a card alive on a later trade date than it formed, which needs `expires_at` past the formation day's last scan (X10); the reason text must cover "no closed bar today".
- (d) ADOPT — sound in all four cases; no number smuggled.
- (e) ADOPT WITH — compute `intraday_stale` right after `last_price` (`:502`), before the `not_evaluable` return (`:518`), as a required field.
- (f) ADOPT WITH — audit-export has NO receipt-version gate on main; add a 3-line gate on `run["evaluator_version"]`, or X4 is red by design.
- (g) ADOPT WITH — the Q7 mechanism, written out; engineering forward, his backward, before promotion only.
- (h) ADOPT — two messages that answer two questions; the ladder moves at the next card action or page load, never on the periodic pool refresh.
- (i) ADOPT WITH — in the taps-moved branch recompute `card_score` from the locked conviction/suppression and the new proximity through `card_score()`: same lines as step 8, closes the fresh case too.
- (j) ADOPT WITH — stack on `setups/seven-0921` (C1's commit `58aa823` sits in a nine-step branch that adds ~980 lines to `evaluate.py`); the stamp is already on main; S1 gains `audit_export.py:363`; migration none; restarts radar + aset.
- (k) ADOPT WITH — X1–X9 kept, X4 rewritten, X10–X16 added.
- Experiments named: 16 (X1–X16). Owner items: 8. WITHDRAWN sentences: 4. ESCALATE: 4.

## Rulings

### Q1 — sink or hold?
**ADOPT** (sink).
`ladder_order` sorts WATCH by `_nulls_last(card_score)` first (`cards/radar.py:179-183`); a null is `(1, 0)` (`:161-164`) and lands after every scored card; the docstring names this the settled rule for an untapped card (`:27-28`). A hold needs a stored slot or the last non-null score as a second ordering input — a second authority (L52 b) or a stale number ordering the ladder (L1). Scenario: ticker X at rank chip #1 with score 72 on the 10:41:40 scan (last bar opened 10:40); at the 10:44:30 scan `as_of − (10:40 + 1 min) = 210 s > 200` → stale → score NULL; at the next `refreshLadder` (after any tap/key/promote, `radar_panel.py:1138`) or page load X renders after every scored WATCH card, among nulls by `pool_position`. That move is the loud state. His ladder is his: if he wants a hold, it is an owner item, not this design.

### Q2 — premarket nulls under the every-session clock
**ADOPT**.
`intraday_staleness` knows no session (`freshness.py:106-120`; the file's only "session" strings are the daily rule, `:25`, `:136-139`); it already stops formation (`evaluate.py:598`) and stales the computed dots (`:439`, `:459`) at every hour. C adds no second clock (L3). A thin premarket name that prints no bar for 260 s after its last bar opened goes NULL and returns on its next closed bar with no tap (`store.py:1038-1047`). Whether that flicker should be RTH-only is a new rule and his (L53). Whether thin names actually print gaps (bars per minute vs bars per print) is a data-source fact: X11.

### Q3 — the band between the stamp's clock and the score's clock
**ADOPT WITH** — replace the proposal's §4 sentence "The score nulls at 200 s and the stamp shows at 180 s, RTH only" and §8 Q3's first sentence with:
"The two clocks measure from different edges of the same bar. The stamp (`radar.poll_bar_max_age_s`, RTH only, `poller.py:117-121`) counts from the newest bar's OPEN; the score (`2 × radar.scan_interval`, every session, `evaluate.py:533`, `freshness.py:117-119`) counts from the newest closed bar's CLOSE. In one unit, at today's committed values, the stamp appears 180 s after the bar opens and the score nulls 260 s after it. Inside RTH there is an 80 s band with a stamp and a live score; outside RTH the score nulls and no stamp ever shows. The suppression line names the bar time, so the age is on the card in both cases. No value changes here; whether the two clocks should meet is his."
Derivation: `ttl = 2 × 100 = 200` (`tunables.yaml:467-468`, `freshness.py:117`); `observed_at = last_bar.ts + 60 s` (`evaluate.py:533`); stale iff `as_of − observed_at > 200` (`freshness.py:119`) ⇔ `as_of − last_bar.ts > 260`. Poller: `newest = max(bar.ts …)` (`poller.py:117-120`), stale iff `now − newest > 180` and `session is RTH` (`:121`, `tunables.yaml:514-515`). Both origins are code facts, not proposals. Reason text is enough; the clocks meeting is a number ruling.

### Q4 — keep writing the stale `last` (C) or null it (D)
**ADOPT** (C).
`refresh_radar_card` writes `last_price = COALESCE(%s, last_price)` on both branches (`store.py:1032`, `:1040`), so a None would keep the old print anyway; D would have to remove the COALESCE and would blank the value the stamp sits beside (`radar_panel.py:1038`, `_field(... "last_price" ..., after=stale_badge)`). Under C the card shows the real last print, the stamp when the poller agrees, and the suppression line naming the bar time — L1 is met by the line, not by hiding the print.

### Q5 — FILLED health pills on stale bars
**ADOPT** (own item).
`refresh_card:780-797` builds pills from `ev.working`, `ev.ema9` and the rvol observation on FILLED cards only; not a score, not a rank (pinned cards order by `pool_position` first, `radar.py:174-178`). Out of scope here; nothing in C touches it.

### Q6 — a tap during staleness
**ADOPT** (accept the tap, keep the score null).
`tap_dot` reads the stored proximity (`store.py:1194`, `:1217`) and `card_score(conv, None, …)` returns None (`scoring.py:265`). Without step 7 the tap route writes `score_suppressed = suppression(dots)` (`:1218`, `:1222`) — dots-only, so the stale reason is gone until the next scan's full write (`:1038-1047`; the next scan's `tap_version` matches, `evaluate.py:802`). Scenario: X stale at 10:44:30 with reason "bars stale — last bar 10:41:00 ET"; he taps `catalyst` 7 at 10:45:00 → score `—`, reason blank until 10:46:10. Step 7's constant closes that scan. Refusing the tap would refuse his grade for a Cobalt-side fact; his taps stay his (R40 refuses only `assumed_formation`).

### Q7 — earlier taps on stale-graded `htf_level_proximity` in the agreement stats
**ADOPT WITH** — add to §2 C step 5:
"Forward, no new mechanism: a computed dot observed stale is built without `engine_grade` (`scoring.py:172-176`), `refresh_dots` keeps the fresh dot's engine fields (`:232-234`), the upsert writes `engine_grade = EXCLUDED.engine_grade` (`store.py:1267-1272`), `tap_dot` records that NULL as `engine_grade_at_tap` (`:1200-1209`), and `shadow_agreement_v` skips NULL pairs (`0007:255`). This already holds for `atrs_from_open`, `Extension.leg_count` and `rvol`; `htf_level_proximity` is the one factor graded from a stale `last` (`evaluate.py:463-477`), and step 5 puts it under the same rule. Backward: a tap row stores no staleness fact (`0007:141-150`); rows recorded before this change are found by query (X12), and whether they are excluded from the L7 evidence is his, before any promotion, never before this build."
Only Rubberband names computed factors (W21), and after C1 its cards are score-null for life — the L7 pairs still record, so step 5 matters even where no score shows.

### Q8 — the version bump
**ADOPT WITH** — replace §2 C "Replay" last sentence and §6 "Sequencing" second sentence with:
"`setups/seven-0921` (the branch carrying C1, commit `58aa823`) already bumps `EVALUATOR_VERSION` to `s2p2.2` and sets `SUPPORTED_EVALUATORS = {"s2p2.2"}` (`replay/formations.py:81` on that branch). C rides `s2p2.2` when it lands in the same deploy as that branch; otherwise C takes its own bump, and `SUPPORTED_EVALUATORS` moves in the same commit — `replay/runner.py:219-224` and `formations.py:145-149` refuse the nightly replay loudly when the live version is outside the set. Neither check reads a receipt; see (f)."
Consumers of the string on main: `evaluate.py:132`, `:928`, `:1253`; `audit_export.py:161`, `:188`; `replay/formations.py:81`, `:145`; `replay/runner.py:219-223`.

### Q9 — more null scores → more WATCH cards ordered by `pool_position`
**ADOPT**.
The tie policy is live today for every untapped card (`radar.py:181-182`; `evaluate.py:134-138`); C adds nulls, not a new tie rule. Not a precondition; an owner item (r2 ESCALATE 2 stays open).

### Q10 — daily-stale `input_stale`: leave proximity computed
**ADOPT**.
The `:624` and `:629` returns are reached only after `if intraday_stale: return` at `:598`, so a daily-stale evaluation has a fresh closed bar and a fresh `last_price` (`:502`); proximity is a function of that `last` only (`scoring.py:254-261`). Keying the guard on the new field, never the label, is right (W3).

### (a) THE FACT BASE
**ADOPT WITH** — add to §1a:
"W22 A third `last` fallback: `radar/audit_export.py:363` `last=ev.last_price if ev.last_price is not None else trigger`. Dead on its own path (a formed evaluation has a closed bar, `evaluate.py:598` before `:632`), but a copy of the rule C deletes — C deletes it too (L3), so `audit_export.py` is a code change in S1, not 'signature only'. W23 A reader: `cards/picks.py:215-233` ranks by `card_score` and drops null scores from the cohort (`:226`); a stale card reads `unavailable: card_score suppressed` (`:224`) — correct, unchanged. W24 The create path also copies proximity/score (`evaluate.py:1418-1424`) and the ladder is rebuilt at every render (`radar_panel.py:743-744`). W25 The R36 stamp is on main (`490c231`; `radar_panel.py:908-912`, `:1038`, `:1069-1073`), a rendering of `poll_failures` mirrored every scan (`:1158`, `:1169`)."
The arm/form/expire sentence is TRUE: `ARMED` in `src/cobalt/radar/` matches only the `TIE_POLICY` string (`evaluate.py:135`); formation follows `:598`; `radar_expiry` (`expire.py:285-310`) takes stop touches from stored closed bars after the formation bar (`evaluate.py:1339-1344`, `:1468-1472`), `avoided` from `ev.evaluation == "avoided"` which an intraday-stale evaluation never reaches (`:598` before `:626`), and the deadline from the wall clock (`:305`). No sequence invents an expiry; a stop touch is found when the bar arrives. W1–W21 hold at their lines on `be2c91e` except W19's panel lines, which moved with the stamp (`_field` `:915-923`, the suppression line `:997-999`, RANK+WHY `:1039`, chips `:1023`, `:1068`).

### (b) OPTION C AGAINST L3
**ADOPT**.
Paths under a null proximity today: tap — `Decimal(locked[2]) if … else None` → `card_score` None (`store.py:1217-1219`), reason from dots only (step 7 fixes); refresh — `score_card(last: Decimal)` and `proximity()` take no None and `CardScore.proximity: Decimal` (`scoring.py:312`, `:322`, `:330`) — this is C's new code (steps 2, 6), the only pre-existing null branch is `card_score()` `:264-267`; replay — `:1079` falls back to entry (step 3 through the one helper); `refresh_radar_card` writes `proximity = %s` with no COALESCE on either branch (`:1032`, `:1040`) → NULL stores; taps-moved keeps the tap route's score (step 8 / (i)); `copy_card_values` writes as given (`radar/store.py:423-426`) into nullable columns (`0006:103-105`); `published_numbers` `str(update.proximity)` would publish `"None"` (`evaluate.py:1031`) — step 6 makes it null. Nothing raises, coerces to zero or loses the null; `OpenRadarCard` loads no proximity (`evaluate.py:700-716`, `store.py:901-902`) and the panel rows are `Decimal | None` (`radar_panel.py:237`, `:339`). C1's carrier is a static dot from formation (c1-facts path 2 "re-appends from the card's OWN stored dot"); a freshness dot must be re-derived on paths 2, 3 and 5 every scan — new code in a different shape, a second carrier for one fact, and a stale proximity still shown. C is the smaller mechanism.

### (c) ESCALATE 1 — NO BAR TODAY → PROXIMITY 1.0
**ADOPT WITH** — replace §1c's "Size" clause "If X has NO bar at all today: proximity = 1.0" and §7 X5 with:
"The path holds: `last = card.entry` (`evaluate.py:776`; `:1079` on replay), `proximity(last=trigger)` = `1 − 0/(3·risk)` = 1 → `1.000000` (`scoring.py:260-261`), `card_score = conv × 100`. `ev.last_price` is None only when no bar of `trade_date` has closed by `as_of` (`:498-502`; bars are loaded from midnight ET, `:1210-1214`), and a card forms only on a scan with a closed bar (`:598` → `:632`), so an open card meets this on a LATER trade date than its formation — after surviving `expires_at`, which defaults to the formation day's RTH close (`expire.py:254-261`, `:130-152`) and is checked every scan (`:1340`). On that first scan `refresh_card` writes 1.0 before the deadline expires the card (`:1345-1350`), so the value lands on a terminal card unless a def's window end is later (X10). C deletes the fallback at all three sites (`:776`, `:1079`, `audit_export.py:363`) and writes proximity NULL with the reason `bars stale — no closed bar today` (no bar time to name)."
Deleting it is safe: a premarket-formed card at the open has its formation bars (fresh or NULL-with-reason by the same rule); a carried card gets NULL then expires; a pre-change receipt that published `1.000000` replays as NULL and the export refuses it — by mismatch on main (`audit_export.py:255-259`), by version with (f)'s gate. `last_price` keeps the prior print through COALESCE (`store.py:1032`, `:1040`); in RTH the poller stamps it (`watermark` older than 180 s, `poller.py:117-121`).

### (d) THE CLOCK
**ADOPT**.
(1) Premarket: the rule is the one that already gates formation and dots (Q2). (2) Pause and overnight: no scan → no refresh → the row keeps its last written numbers; C cannot null what nothing recomputes, and today the same holds — the pool header's `last scan` (`radar_panel.py:882`) is the only age mark; cards default to expire at the RTH close (`expire.py:130-152`), so an overnight open card needs a def window (X10). (3) First scan after the open: a name whose first bar opens 09:30 closes it at 09:31; at a 09:31:40 scan `age = 40 s` → fresh; before any closed bar today → NULL with reason (correct; today 1.0). (4) Replay: `as_of` is the receipt's (`evaluate.py:1014`), `scan_interval` the snapshot's (`:1053`), and `intraday_staleness` refuses a future observation (`freshness.py:111-115`) — deterministic. No number, offset, factor or session rule is added anywhere in C's text; the reason names the key `radar.scan_interval`; `PROXIMITY_UNKNOWN` is a string. The one unit slip is Q3's, corrected there.

### (e) THE TWO MEANINGS OF `input_stale`
**ADOPT WITH** — replace §2 C step 1 with:
"`MemberEvaluation.intraday_stale: bool` — a required field, no default. It is computed immediately after `last_price` (`evaluate.py:502`: `True` when `last_bar is None`, else `intraday_staleness(observed_at=last_bar.ts + 1 min, as_of=member.as_of, scan_interval).stale`) and placed in `base`, so every return path carries it: the `not_evaluable` return at `:518-524` (today reached before `:529` computes the flag), the intraday return `:599` (True), the daily returns `:624`/`:629` (False — a fresh `last`), and `formed`. It is never keyed on `evaluation` (W3)."
Failing sequence without it: an evaluation returned at `:519` has `last_price` set and no flag; with a default `False`, `refresh_card` scores its card on whatever `last` it holds. With the same md5 that cannot happen (`evaluability(td)` is a function of the def alone, `registry.py:49`, so a def that formed is evaluable); through the slug-match path (`:1324-1328`) it is not settled from reads (X13). The wording removes the gap instead of arguing it. Replay: `rebuild_members` → `evaluate_member` → the same lines.

### (f) L57 — REPLAY
**ADOPT WITH** — replace §2 C "Replay" with:
"`replay_receipt` recomputes `intraday_stale` from the receipt's bars, `as_of` and `scan_interval` (`evaluate.py:1053`, `:1058-1063`) and scores through the same helper, so `proximity null`, `card_score null` and the reason (from `last_bar_ts`, `:354`, formatted once, in ET, dot reasons joined in `suppression()`'s order) equal the published dict, and `export_run` refuses any difference (`audit_export.py:248-259`). The nightly `com.cobalt.replay` never recomputes `card_score` (no `card_score` under `src/cobalt/replay/`; its own `input_stale` is a coverage status, `replay/cards.py:253`, `:312`). Receipts written before this change carry a computed proximity on stale bars; `export_run` has no receipt-version check today (`audit_export.py:203-243` checks status, receipt, chain and four hashes; `evaluator_version` appears only as a written field, `:90`, `:161`, `:188`). C adds one: `run['evaluator_version']` (`radar_score_run.evaluator_version`, `0006:76`, written at `evaluate.py:1253`, returned by `score_run`, `radar/store.py:460-465`) must equal `EVALUATOR_VERSION`, else `AuditExportError(f'run {run_id} was published by evaluator {…}; this build replays {EVALUATOR_VERSION} only')` before the replay. Cost: 3 lines in S1, one offline test. Version consumers: Q8."
Without the gate the design still fails loud (mismatch), but the message says Cobalt's replay disagrees with itself, which is the wrong fact; X4 as written expects the version refusal, so on main X4 is red by design, not by defect.

### (g) L7 — THE SHADOW STATS
**ADOPT WITH** — the Q7 wording, as §2 C step 5's text. Verdicts on the three asks: EXCLUDE forward by mechanism (a NULL `engine_grade_at_tap` is not a pair, `0007:255`), no flag column, no new stored fact; the backlog is identified by a query (a tap's `at` inside the window of a run whose `radar_score` row for that member/def is `input_stale` — the seam row does not separate the two meanings of the label, W3, so the query names candidates), counted by X12, and ruled by him. Owner item for the backlog (his promotion evidence); engineering for the forward rule; needed before any promotion, never before C builds — L7 says no promotion happens without the shadow run and a HITL token anyway.

### (h) WHAT HE SEES
**ADOPT**.
Two messages, two questions: the stamp says the poller fetched no new bar for `radar.poll_bar_max_age_s` (RTH), the line says the evaluator scored on no bar younger than `2 × radar.scan_interval` — Q3 gives the 80 s band (stamp, live score) and the outside-RTH case (line, no stamp); neither is wrong then, each names its own clock and the line names the bar time. Sink is engineering (L1 + the ladder's own null rule, `radar.py:27-28`); a hold is his. When it moves: the score nulls at the scan; the ladder strip keeps its old chip and slot until `refreshLadder` runs — only after a POST on any card (`radar_panel.py:1138`) or a page load — because the periodic `refreshPool` replaces the pool layer and mirrors the badge only (`:1161-1177`, `:1158`). Scenario: X nulls at 10:44:30; the STALE badge appears on X's strip within one scan (`mirrorStale`, RTH); the chip still reads 72 and X still sits at #1 until he taps any card or reloads, then X shows `—` and sinks. That lag is today's rendering rule for every score change, not C's; whether the ladder should re-render every scan is an owner item.

### (i) ESCALATE 4 — THE RACING TAP ON FRESH INPUT
**ADOPT WITH** — replace §2 C step 8 with:
"`store.refresh_radar_card`, taps-moved branch (`store.py:1029-1037`): the lock SELECT (`:1022-1026`) also reads `conviction, score_suppressed`; the branch computes `suppressed = update.score_suppressed if update.proximity is None else locked_score_suppressed` and `score = card_score(locked_conviction, update.proximity, suppressed)` (`scoring.py:264`), and its UPDATE also sets `card_score = %s, score_suppressed = %s`. Conviction and the proposed key stay the tap route's. NULL proximity → NULL score with the stale reason; fresh proximity → the tap's conviction on this scan's proximity."
Same lines and chunk (S2, same seat) as step 8, ~5 lines, no new file, one formula (`card_score()` — no SQL arithmetic, so no rounding claim to prove). Scenario closed: his tap at 10:41:35 lands between the 10:41:30 stage read and the 10:41:40 write; today the row ends with `proximity` new and `card_score` = conviction × old proximity for one scan; after this, both are this scan's. If the derive keeps step 8 alone, the fresh case stays a separate item and step 8 does not make it harder.

### (j) CHUNKS, SEATS, RESTARTS, ORDER
**ADOPT WITH** — replace §6 "Sequencing" with:
"C1 is commit `58aa823` on `setups/seven-0921` (worktree `~/cobalt-wt/setups-c1`, tip `60ddac4`, nine steps C1–C7, BUILT, not merged); no ref named `setups/c1-rubberband-0921` exists. That branch bumps the evaluator to `s2p2.2`, refuses the `assumed_formation` tap in `tap_dot` (`store.py:1205-1209` there), extends `suppression()`, and adds ~980 lines to `evaluate.py`; it does not touch the `card.entry` fallback or `intraday_stale` (`git log -S`, empty), so C's targets are unchanged on it. C is built on a tree that already carries `setups/seven-0921` — stacked under the L68 gate on the combined tree, or after it lands — never cut from a `main` without it. The R36 stamp is on `main` (`490c231`; `s2/stale-marker-0921` fully merged); no ordering against it remains."
Chunks: S1 pure as proposed plus `audit_export.py:363` and the (f) gate; S2 the two `store.py` writers with (i)'s wording. Seats: S2 on the Opus 5 floor (L29, user-table writes at `store.py:1032-1047`, `:1206-1225`); S1 on the same branch and seat as proposed. Migration: none (`0007:47-48`, `0006:103-106` nullable, no CHECK). RESTARTS by the L42 rule (GUESS until `cobalt jobs restarts <range>`): `com.cobalt.radar` (imports `radar.evaluate`), `com.cobalt.aset` (`radar_panel.py:30` imports `cobalt.cards.radar`), `com.cobalt.replay` one-shot reads the version on its next run; radar inside the pause, residents down before the merge (L43, L66). Live today: yes for any open card whose bars go stale with one tap (W21); after the setups branch lands, new cards are score-null for life until his `A-01` ruling (c1-facts 137), so "before `A-01`" orders the lane, it does not gate the build.

### (k) NOT CHECKABLE FROM READS
**ADOPT WITH** — X1–X3, X5–X9 kept as written; X4 replaced; X10–X16 added (full list under `## Experiments (L70)`).

OWNER (after the tribunal): see `## OWNER (after the tribunal)`.
WRONG FACTS: see `## WRONG FACTS`.

TRIBUNAL R1: BUILD AFTER the derive, on a tree that already carries setups/seven-0921

## Self-attack
Every grep `grep -rn <name> /Users/cobalt/cobalt/src/cobalt` (this shell's grep honours `.gitignore`), writers → readers:
- `last_price` — writers: `evaluate.py:502` (from the last closed bar), `:776`/`:1079`/`audit_export.py:363` (fallbacks), `store.py:1032`, `:1040` (COALESCE); readers: `evaluate.py:463-474` (htf), `:567` (seam obs), `:803`, `:1384`, `0007:227` (view), `radar_panel.py:252`, `:758`, `:1038`; the ASET sheet's own `last_price` (`aset/*`) is a different field.
- `proximity` — writers: `scoring.py:254-261`, `:330`; `evaluate.py:799`, `:1083`, `:1356`, `:1394`, `:1419`, `:1423`; `store.py:997`, `:1032`, `:1040`; `radar/store.py:423`; readers: `store.py:1194`, `:1217` (tap), `:1133`; `evaluate.py:1031`; `audit_export.py:373`; `radar_panel.py:237`, `:339`, `:769`, `:1039`; `radar.py:97` (creation spec, untouched).
- `card_score` — writers: `scoring.py:264-267`, `:334`; `evaluate.py:800`, `:1084`, `:1357`, `:1395`, `:1420`, `:1424`; `store.py:998`, `:1041`, `:1222`; `radar/store.py:423`; readers: `radar.py:177`, `:181`; `picks.py:216-233`; `evaluate.py:1033`; `radar_panel.py:744`, `:769`, `:1023`, `:1039`, `:1068`; `audit_export.py:373`; `evaluate_cli.py:25` (doc).
- `score_suppressed` — writers: `scoring.py:335`; `evaluate.py:800`, `:1084`, `:1358`, `:1395`, `:1420`, `:1424`; `store.py:998`, `:1041`, `:1222`; readers: `evaluate.py:1033`; `radar_panel.py:761`, `:998`, `:1039`; `audit_export.py:101`, `:374`.
- `intraday_stale` — set `evaluate.py:530`, `:532-534`; read `:439`, `:459`, `:557`, `:598`. Not a field of `MemberEvaluation` (`:339-364`).
- `input_stale` — `evaluate.py:140`, `:599`, `:624`, `:629`; `scoring.py:72`, `:175`, `:226-228`; `0006:100`; `replay/*` (a different status: `models.py:179`, `:220`, `:276`; `cards.py:253`, `:312`; `formations.py:205`).
- `engine_grade_at_tap` — writer `store.py:1207-1209`; readers `0007:147`, `:250-255`; `shadow_report.py:6`.
- `refresh_card` — def `evaluate.py:759`; caller `:1345` only.
- `tap_dot` — def `store.py:1182`; callers `aset/web.py:1362`, `evaluate_cli.py:381`.
- `refresh_radar_card` — def `store.py:1016`; caller `evaluate.py:1348` only.
- `replay_receipt` — def `evaluate.py:1043`; caller `audit_export.py:245` only.
- `score_card` — def `scoring.py:319`; callers `evaluate.py:777`, `:1080`, `:1384`; `audit_export.py:363`.
- `EVALUATOR_VERSION` / `SUPPORTED_EVALUATORS` / `s2p2.1` — `evaluate.py:132-133`, `:928`, `:1253`; `audit_export.py:64`, `:161`, `:188`; `replay/formations.py:81`, `:87`, `:145`; `replay/runner.py:56`, `:219-223`.
- Also run: `published_numbers` (`evaluate.py:1029`; callers `:1082`, `:1428`, `:1479`); `poll_failures`/`max_age_s` (`poller.py:121`; `radar/store.py:185-277`; `runner.py:276-448`; `radar_panel.py:94-615`, `:909`; `heartbeat/probes.py:111`); `ARMED` in `radar/` (`evaluate.py:135` only); `assumed_formation`/`assumed_keys` (none on main); session strings in `freshness.py`; `copy_card_values`/`radar_score_id`; `ladder_order`/`TIE_POLICY`/`NULLS LAST`; `compute_dots(`/`refresh_dots(`/`upsert_dot`; `radar_expiry`/`expire_due`; `card_dot_taps`; `def evaluability` (`registry.py:49`); `scan_interval` in `radar/`; `"proximity:"` fields; `evaluator_version` in `audit_export.py` and `0006`; `def score_run`; `_DOT_UPSERT_ENGINE`; `def open_radar_cards`; `class OpenRadarCard`; `def _field`/`bars_stale`/`score suppressed` and the refresh JS in `radar_panel.py`; `def radar_deadline`, `def window_end_for`; `def _i1_closed`.
- WITHDRAWN: "A NULL proximity on the row would fail the open-card loader's model on the next scan" — `evaluate.py:700-716` has no proximity field and `store.py:901-902` selects none.
- WITHDRAWN: "A tap during staleness erases the stale reason for the rest of the card's staleness" — the next scan's full write restores it (`store.py:1038-1047`; `tap_version` re-read at `evaluate.py:802`); it is one scan.
- WITHDRAWN: "A card carries the maximum proximity into the WATCH order on the next trade date" — the same scan expires it at the default RTH-close deadline (`expire.py:254-261`, `:130-152`; `evaluate.py:1340`, `:1350`); the WATCH claim needs a later window (X10).
- WITHDRAWN: "The stamp and the suppression line can contradict each other on one card" — they measure from different bar edges (`poller.py:117-121` vs `evaluate.py:533`) and answer different questions; a stamp with a live score is the 80 s band, not a contradiction.

## Experiments (L70)
- X1 (kept, RED on main): pure `refresh_card`, every dot tapped, a bar whose close is 201 s before `as_of` → main scores; new code gives proximity None, score None, reason naming the bar time.
- X2 (kept): `cobalt_dev` — form, tap all, stop bars, run the stage (NULL/NULL), tap another dot (NULL kept, reason kept), add a fresh bar, run the stage (score returns, no tap).
- X3 (kept, widened by (i)): a tap between the stage read and the write — stale: NULL score with the stale reason; fresh: `card_score` equals conviction × this scan's proximity.
- X4 (replaced): `audit-export` on a run with a stale card → recompute = published. A pre-change run: on main it is refused by MISMATCH (`audit_export.py:255-259`); with (f)'s gate it is refused by VERSION before the replay — the test asserts what the derive adopts.
- X5 (kept, RED on main): zero closed bars today → proximity `1.000000` on main, NULL after; reason `bars stale — no closed bar today`.
- X6 (kept): `htf_level_proximity` is `input_stale` whenever `intraday_stale`; its stored `engine_grade` is NULL; a tap records `engine_grade_at_tap` NULL.
- X7 (kept): `ladder_order` with one stale WATCH card → after every scored WATCH card; pinned order unchanged.
- X8 (kept): expiry unchanged under a stale window: deadline fires; a stored bar through the stop fires `stop_before_arm`.
- X9 (kept, hub-run on production read-only, L41): count radar cards whose `radar_score_id` row is `input_stale` while `card_score IS NOT NULL` — the occurrence proof.
- X10: on `cobalt_dev`, a def whose `preferred_windows_ref` ends after the last scan of the day, a card formed on it, a scan on the next trade date before any bar → does the card survive to that scan and does it publish proximity `1.000000` on main (WATCH impact of ESCALATE 1)? A "never survives" result makes ESCALATE 1 a terminal-card artifact.
- X11: on `cobalt_dev` with an archived low-volume ticker's i1 bars: are minutes with no prints stored as bars? If not, Q2's premarket nulls are frequent by design and RTH-only becomes a real owner question.
- X12: `cobalt_dev`, then the hub read-only on production: count `card_dot_taps` rows for `htf_level_proximity` with `engine_grade_at_tap IS NOT NULL` whose `at` falls inside a run whose `radar_score` row for that card's member/def is `input_stale`. Zero → Q7's backlog is empty.
- X13: pure: an open card refreshed through the slug-match path (`evaluate.py:1324-1328`) with an evaluation of `not_evaluable` — can `evaluability` differ while `formation_changes` is empty? Either result leaves (e)'s wording; a "yes" makes it load-bearing.
- X14: pure: the stage's `score_suppressed` text and `replay_receipt`'s are byte-identical for a stale card (ET time format, dot-reason order) — X4's precondition.
- X15: `cobalt_dev`: count receipts whose `published.proximity = '1.000000'` on a card whose seam row is `input_stale` — how often the fallback published in the past.
- X16: rendering: after a scan nulls a score, `/radar` fetched before and after a tap on another card — the strip's chip and slot change only after the tap; the badge appears within one `refreshPool`.

## OWNER (after the tribunal)
- Q1 / (h): whether a stale WATCH card holds its slot instead of sinking — a second ranking input; the ladder's null rule sinks it today.
- Q2: an RTH-only staleness rule for the SCORE (the evaluator's clock is session-blind, `freshness.py:106-120`).
- Q3 / (d): whether the poller's clock (`radar.poll_bar_max_age_s`, bar open) and the evaluator's (`2 × radar.scan_interval`, bar close) should meet — values and origins are his.
- Q7 / (g): whether `htf_level_proximity` tap pairs recorded on a stale `last` before this change leave `shadow_agreement_v` — before any promotion (X12 counts them).
- Q9: `pool_position` as the tie-break among null-score WATCH cards (r2 ESCALATE 2).
- Q5: FILLED health pills computed on stale bars.
- (h): whether the ladder re-renders every scan (today: on a card action or reload only; the badge mirrors every scan).
- R36 carry-over: the wording, size and colour of the STALE stamp and of the suppression line (R36 said not ruled; `radar_panel.py:908-911` says ASSUMED).

## WRONG FACTS
- PROPOSAL §4 and §8 Q3: "The score nulls at 200 s and the stamp shows at 180 s" — the evaluator counts from the bar's CLOSE (`evaluate.py:533` `last_bar.ts + 1 min`; `freshness.py:116-119`), the poller from the bar's OPEN (`poller.py:117-121` `bar.ts`); in one unit 260 s vs 180 s after the bar opens; the band is 80 s, not 20.
- PROPOSAL §2 C "Replay" ("replay refuses other versions (C1 gate 5)") and §7 X4 ("refused by the version, not by a mismatch"): `audit_export.py:203-259` has no receipt-version check (`evaluator_version` only written: `:90`, `:161`, `:188`); the version refusals at `replay/formations.py:145-149` and `replay/runner.py:219-224` gate the live module against the nightly binding, not a receipt. On main a pre-change run fails by mismatch.
- PROPOSAL §2 C "Files": "`radar/audit_export.py` (signature only; formation is never stale)" — `audit_export.py:363` carries its own `else trigger` fallback; C changes that line.
- DIGEST (author's report) "Only `Rubberband.md` names computed factors" — not contradicted; recorded as grep-scope only, as the author marked it (vault grep not re-run here: no vault read was needed for a ruling).

## READING
- `/Users/cobalt/Vault/Think/6 - Permanent/Memory/LAWS.md` 1–407 (whole).
- `docs/30 - Design/STALE-SCORE-PROPOSAL-2026-09-21.md` 1–187 (whole); `reports/stale-score-design-2026-09-21.md` 1–107 (whole); `prompts/2026-09-21/61-stale-score-tribunal.md` 1–42 and the `TRIBUNAL R1:` grep (lines 39, 47, 54, 65 printed by grep — 47/54/65 are launch and collate mechanics, read as grep output only); `prompts/2026-09-21/62-…` (this seat's prompt, whole); `reports/cto-2026-09-21.md` rows R36, R40, R51 by grep; `reports/setups-c1-draft-2026-09-21.md` 33–43, 137–140; `docs/10 - Decisions/ADR-0009-…md` 27–28.
- `src/cobalt/cards/scoring.py` whole (1–344); `src/cobalt/radar/evaluate.py` 128–140, 339–364, 429–535, 536–594, 595–632, 700–716 (grep -A), 755–829, 1029–1040, 1043–1090, 1205–1230, 1244–1257, 1315–1350, 1380–1400, 1416–1431, 1468–1480; `src/cobalt/cards/store.py` 896–908 (grep -A), 1016–1075, 1128–1157, 1182–1231, 1267–1273 (grep -A); `src/cobalt/cards/radar.py` 20–35, 84–139, 160–206; `src/cobalt/radar/poller.py` 90–125; `src/cobalt/radar/anatomy/freshness.py` 106–142; `configs/cobalt/taxonomy/tunables.yaml` 465–472, 512–522; `src/cobalt/cards/expire.py` 130–152 and 254–268 (grep -A), 272–312; `src/cobalt/radar/audit_export.py` 196–243, 240–260, 318–379; `src/cobalt/db_migrations/0007_radar_cards.sql` 44–50, 140–150, 215–258; `0006_radar_score.sql` 95–109 and the `evaluator_version` grep (:76); `src/cobalt/aset/radar_panel.py` 877–885, 905–934, 955–958, 996–999, 1060–1075, 1118–1179; `src/cobalt/cards/picks.py` 196–235; `src/cobalt/radar/store.py` 419–430, 460–465 (grep -A); `src/cobalt/replay/formations.py` 76–89, 136–151; `src/cobalt/replay/runner.py` 212–225; `ls src/cobalt/replay`.
- Git: `log -1` main = `be2c91e`; `log -3 setups/c1-rubberband-0921` → fatal (no such ref); `grep gitdir ~/cobalt-wt/setups-c1/.git` → `.git/worktrees/setups-c1`; its `HEAD` → `refs/heads/setups/seven-0921`; `log -3 setups/seven-0921` (tip `60ddac4`); `log --stat main..setups/seven-0921` (13 commits, names only read); `log -S"SUPPORTED_EVALUATORS"` and `-S"evaluator_version" -- audit_export.py` on that range; `log -S"else card.entry"` and `-S"intraday_stale" -- evaluate.py` on that range (both empty); `show 58aa823 -- replay/formations.py, cards/store.py, cards/scoring.py, radar/audit_export.py`; `log -3 s2/stale-marker-0921`; `log main..s2/stale-marker-0921` (empty); `log -4 -- src/cobalt/aset/radar_panel.py` (stamp at `490c231`); `ls ~/cobalt-wt`.
- Searches: the 13 mandated names plus those listed under `## Self-attack`.
- NOT read: the houses' folder, the hub's report, any file a house wrote about this proposal; the vault's trading notes; the tests; `evaluate.py` outside the ranges above; the C1 branch's files beyond the four `show`s.

## ESCALATE
1. The C1 branch the prompts name (`setups/c1-rubberband-0921`) does not exist; C1 is commit `58aa823` inside `setups/seven-0921` (nine steps, BUILT, unmerged, `evaluate.py` +~980 lines, version `s2p2.2`). The derive and the build prompt must name that branch; a C branch cut from today's `main` will conflict on landing.
2. `audit-export` has no receipt-version gate on main (WRONG FACTS 2); the proposal's X4 expects one. The derive picks the 3-line gate under (f) or rewrites X4 to the mismatch refusal.
3. The clock band is 80 s in one unit (bar open), not 20 (WRONG FACTS 1); the derive corrects §4 / Q3; no value changes.
4. The R36 stamp is on `main` at `490c231`; whether it is deployed to production is UNVERIFIED from reads (the 09-22 `52`/`54` prompts are its check and deploy review, outside this read set). No ordering of C against it remains.

## CONTINUE
None. The run is complete. Next steps are the desk's: commit this report; the hub `61` file-checks these claims at its collate step; after both stop lines are committed, the derive `63` on the seat his row names (`claude-fable-5-1`, no longer blind).

STALE SCORE TRIBUNAL FABLE R1 DONE · verdict: BUILD AFTER the derive, on a tree that already carries setups/seven-0921 · adopt: 10 · adopt with wording: 11 · reject: 0 · experiments named: 16 · ESCALATE: 4
