# Ladder audit — 2026-09-19 (answering Dejan's 10:55 ET question)

Sonnet, read-only. Sources: `SPRINT-LADDER-v0_1.md`, `MVP-CHARTER-v0_2.md`, `BACKLOG.md`,
`PROJECT-LEDGER.md`; git log/tags of `~/cobalt`; `areas/cobalt-sprints.md`, `areas/cobalt.md`
`## NOW`; `reports/cto-2026-09-1[5-9].md`, `close-2026-09-1[5-8].md`, `deploy-2026-09-1[5-9]*.md`.
As of 2026-09-19 ~10:55 ET.

## §0 Headline

Not abandoned, but the ladder FILE is orphaned: last edited 09-13 (commit `476f67c`), and
neither `CTO-DESK-WAKEUP.md` nor `SESSION-CLOSE.md` names `SPRINT-LADDER-v0_1.md`, `BACKLOG.md`
or `MVP-CHARTER-v0_2.md` anywhere in their read/write steps — only `PROJECT-LEDGER.md`,
`LAWS.md` and `areas/cobalt.md`. The actual sprint state IS current and correctly tracked, just
in `areas/cobalt-sprints.md` (updated today) and the daily `cto-*.md` reports, not in the ladder
file itself. **S1 is done and was formally accepted 09-08.** S2 (09-10→09-23) has 4 of 7
features/§5-panel live-or-dark, 3 items built-not-merged, one whole parallel item (Agent SDK
spike) with zero evidence it ever ran, and **zero of the required 2–3 "live mornings beside DAS"
logged anywhere** — that is the one number that puts 09-23 AT RISK. Off-ladder process work
(deploy law, review tribunals, migration harness, archiver rebuild) consumed most of 09-15→09-18
in build time; that is ruled work, not drift, but it is why feature velocity looks stalled.

## §1 S1 — Foundation + firewall (planned 09-08→09-18)

| Item | Status | Evidence |
|---|---|---|
| F1 Session clock | DONE-LIVE | S1-P1, ladder S1-P1 outcome; `src/cobalt/session/`, 60 tests, 09-04 |
| F7 Card state machine | DONE-LIVE | S1-P2 outcome, `card_transitions` table, 88 tests, 09-04 |
| F6 Two-stage day mode + match check | DONE-LIVE | S1-P2 outcome, `.htk` attestation refusal, 09-04 |
| F18 Heartbeat | DONE-LIVE, one gap | S1-P3 outcome; **email channel NOT BUILT** — retired 09-14 (Google Publish gate), alerts = Mattermost DM only, per `areas/cobalt-sprints.md` [09-14] |
| F17 Task integrity | DONE-LIVE | S1-P3 outcome, `cobalt_jobs`/watchdog, 09-04 |
| F19 Exfiltration guard | DONE-LIVE | S1-P3 outcome, redactor proven live, 09-04 |
| F16 sweep | DONE-LIVE, recurring | S1-P1/P2/P3, repeats every sprint |
| bars.ts ADR-0007 | DONE-LIVE | executed 09-04, 4.76M rows, dump=rollback |

**S1 formally accepted:** 2026-09-08, chat-stated, recorded in `areas/cobalt-sprints.md`
[stated 2026-09-08]: "S1 live acceptance GREEN: attestation + rung→sheet gating applied on the
live ASET sheet, a real trade went through the cards, daily note intact, heartbeat green; CODE
FREEZE (declared 09-05) LIFTED 09-08." Also `scripts/smoke_s1.sh`, 19 checks, GREEN (ladder's own
S1-P3 section). Delivered ~10 days early against the 09-18 plan date. No separate ADR/ledger
appendix line names "S1 ACCEPTED" verbatim — the record is the sprints file + the freeze-lift,
not a dedicated acceptance document.

## §2 S2 — Radar 19a (planned 09-10→09-23)

| Feature/prompt | Status | Evidence | To go live |
|---|---|---|---|
| F2 Radar pool 24×5 | DONE-LIVE | S2-P1 LIVE 09-13 (`7bca336`), `com.cobalt.radar` resident, L13 acceptance run 09-14 | — |
| F8 Card at precondition (19a) | DONE-NOT-LIVE (dark) | S2-P2 chunks A–C complete 09-16; merged→reverted 09-17 (test conflict, no data touched); re-landed in `sprint-2/stack`, deployed **DARK** 09-19 08:25, tag `deploy-2026-09-19`, `radar.cards_enabled: false` | Shadow run + agreement stats + HITL token per **LAWS L7** (shadow-mode promotion — NN#12, it IS a trading-logic change); `card.shadow_promotion_bar`/`card.alignment_default` values still his to set ("09-19 values session", not yet held) |
| F10 Dots/ladder/accept-up-down | DONE-NOT-LIVE (dark) | same S2-P2 dark deploy | same as F8 |
| F3 Focus list, conviction WHY | PARTIAL | rank+WHY row live via S2-P1/S2-P3 pool view; pick-vs-rank persistence is S2-P4 R2, built, **not merged** (branch `sprint-2/p4`); DRC rendering deferred to F14/S3 | merge P4, then S3's F14 |
| Radar panel (§5 host) | PARTIAL | read-only `GET /radar` pool view LIVE since 09-15 (`deploy-2026-09-15`); card-ladder shell built, cards dark; **acceptance = 2–3 live mornings beside DAS — ZERO found in any report** (grep of all `cto-*.md`/`deploy-*.md` for "live morning" returns none since the panel shipped) | turn F8/F10 live, then bank the mornings |
| F12 Missed records (nightly replay) | BUILT-NOT-MERGED | S2-P4 R3 (`com.cobalt.replay` one-shot), verify hub `p4-verify-0919` → `READY` 10:50 ET today, branch `sprint-2/p4` not merged | merge + deploy P4 |
| F13 Auto-archive + benchmark + miss line | BUILT-NOT-MERGED | S2-P4 R5, same branch/status as F12 | merge + deploy P4 |
| S2-P1 | DONE-LIVE | 09-13 | — |
| S2-P2 | DONE-NOT-LIVE (dark) | 09-19 08:25 deploy | see F8/F10 |
| S2-P3 | DONE-NOT-LIVE (partial) | panel LIVE 09-15, card slice dark inside S2-P2 | live mornings, above |
| S2-P4 | BUILT, READY, NOT MERGED | verify stop line 10:50 ET today; **ASK DESK pending his A/B** on the `Asset Type` filter rule (changes what the live radar drops) — blocks merge | his ruling, then merge |
| Agent SDK spike | **NOT STARTED — no evidence found** | zero hits for "Agent SDK"/"SDK spike" in any `cto-*`/`deploy-*`/`close-*` report or BACKLOG since the ladder named it 09-04; last mention is the ladder line itself and a struck 08-29/31 ledger note | needs an explicit decision: run it before S5, or drop/replan |
| S2 smoke | BUILT, not yet run as acceptance | "STEP-9 cobalt smoke s2" built in S2-P4 chunk C (`a566cbc`, 09-17); can't be run as a real acceptance smoke until P2/P4 are merged live | run after merge |
| 2–3 live mornings beside DAS | **ZERO** | no report row found; a 09-15 review (`p2-review-astra-r1-2026-09-15.md:30`) already flagged the calendar math: mornings only exist from 09-22 (Tue) and 09-23 (Wed) if cards enable the evening before | see §3 |

## §3 Schedule

| Sprint | Planned | Actual |
|---|---|---|
| S1 | 09-08 → 09-18 | built 09-04, accepted 09-08 — **10 days early** |
| S2 | 09-10 → 09-23 (pulled forward from 09-21→10-02 on 09-09) | P1 live 09-13; P3 panel live 09-15; P2 dark 09-19 (2 days lost to a merge-revert cycle 09-17 and three failed deploy attempts 09-18); P4 READY but unmerged 09-19 |

**What must happen by 09-23, dated:**
- 09-19/09-20 (weekend): merge his P4 Asset Type ruling; merge `sprint-2/p4`; deploy 2 and 3 of
  the "three deployments by Monday" he ordered 09-19 R3 (ops-0919 round 2, archiver append-only —
  both built, house checks in flight as of this audit).
- Trading-day mornings remaining before 09-23 close: **Mon 09-21, Tue 09-22, Wed 09-23** only
  (Sun 09-20 has no trading session). If `radar.cards_enabled` flips true Monday evening (after a
  shadow run he still has to approve), only Tue/Wed count as live mornings beside DAS — 2, not
  the ladder's 2–3. If it flips Sunday night, 3 are possible.
- Verdict: **AT RISK.** Reason: not the ladder's dates but its own §5 acceptance clause — the
  card feature (F8/F10) must go from dark to live, complete a shadow run under L7, get his HITL
  approval, AND bank 2–3 live mornings, all inside 3 trading days that are also carrying two more
  weekend deploys and a Sunday bars tribunal. F12/F13 (P4) are separate: mergeable any time,
  not gated by a shadow run, lower risk.

**S3 (09-24 start):** design inputs mostly ready — DRC template review session (his + Claude)
still OWED per the ladder's own "Carried open items", stop-override authority (mock #6) still
OWED, both listed as preconditions "before S3-P2/P3". Neither has a report row showing it done.
**S3 cannot cleanly start 09-24 without these two sessions happening first**, independent of S2's
own slip.

## §4 Off-ladder work since 09-10 (not a ladder line)

| Item | Ruled by | Rough build days | Verdict |
|---|---|---|---|
| Migration harness (streamed proof, `--proof-only`, REPEATABLE READ, ambiguous-name refusal) | Forced by 09-18 production defect (`string_agg` over 8.4M rows hit Postgres's 1 GB ceiling); built as part of the `sprint-2/stack` deploy fix | ~1 day (09-18) | ladder-supporting (blocked all deploys until fixed) |
| Append-only archiver redesign | `docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md`, ruled via L67 four-house tribunal, his R8 "A on archiver" 09-19 09:30 (after his R5 09-19 07:35 retracted an earlier attempt to skip the tribunal step) | ~2 days design+build (09-19, still in three-house check) | ruled detour — infra defect discovered mid-sprint, not a Charter F-id, but load-bearing for F2/F12/F13's data path |
| Deploy-shape law (residents stopped before merge, restart in the pause) | R19, Dejan, 09-17 21:54 ET | folded same day | ruled detour (process) |
| L67 four-house build-check tribunal, "unattended-launch" standard | R5/R8/R11 references, 09-17; formalized 09-18 | spans 09-15→09-19, several hours/day | ruled detour (process) — largest off-ladder time sink of the week |
| Weekend push / minimum-idle-time rule | R3/R6, Dejan, 09-19 07:12/07:38 | ongoing | ruled directly by him |
| Heartbeat market-reset fix, day-open command, alert-fatigue transition-only alerting | Dejan/chat rulings 09-10, 09-14, 09-14 | ~1 day each | ladder-supporting (F18/F1 hardening) |
| Backup (restic→HDD after SSD death) | ruled 09-05, incident 09-06 | ~1–2 days | ladder-supporting (Charter §13 open item), B2 offsite still OFF |
| Ops batches 0915–0919 (email retirement, Finviz ceiling, RESTARTS classifier, grok-deny profile, seat-usage pin, etc.) | small chat rulings each day, R-numbers vary per report | ~0.5–1 day each, 5 days total | mixed: mostly ladder-supporting (unblocking deploys), a few (agy/Codex trial, seat-usage) are genuine drift from the F-id list |

**Net effect on velocity:** of the 5 build days 09-15→09-19, one shipped a ladder feature outright
(09-15, S2-P3 panel read layer); 09-16 was P2 build with no merge; 09-17 merged-then-reverted P2
(net zero); 09-18 shipped **nothing** (three failed deploy attempts, close report's own words:
"NOTHING SHIPPED"); 09-19 finally landed S2-P2 dark plus the infra fixes. Most of the gap is the
process/tribunal apparatus being built and exercised for the first time this week, which is real
work but is not a line on the ladder and was never surfaced to him as its own item.

## §5 Record hygiene

| File | Last content commit | Ledger appended at close? |
|---|---|---|
| PROJECT-LEDGER.md | 09-18 `0158028` (close appendix) | 09-15 ✓ `7101513`, 09-16 ✓ `e87b26b`, 09-17 ✓ `e08b932`, 09-18 ✓ `0158028` — every close this week appended |
| SPRINT-LADDER-v0_1.md | **09-13** `476f67c` | not touched by any close since; not named by any close step |
| BACKLOG.md | content last changed 09-16 (`ca4983a`, via feature commits, not a close routine); file mtime 09-19 08:19 from an unrelated nightly rewrite | still says "S2-P2 … HUB VERIFICATION PENDING" though S2-P2 is now dark-deployed — **stale** |
| MVP-CHARTER-v0_2.md | 09-08 (`fdf79d0`) | unchanged since ratification, expected — no drift here |

**LADDER is stale on:** S2-P1/P2/P3 status lines (still shows the 09-10 "LADDER EDITS" wording,
no note of the 09-17 revert, the 09-19 dark deploy, or P4's READY state); the "S2 smoke" and
"live mornings" rows carry no status at all; "Carried open items" still lists DRC template review
and stop-override authority as owed with no date movement since 09-04/09-10.

**Does any routine tell the desk to read/update the ladder?** No. `CTO-DESK-WAKEUP.md`'s INDEX
CARD (7 numbered sources) and `SESSION-CLOSE.md`'s 7 steps both name `LAWS.md`, `PROJECT-LEDGER.md`
and `areas/cobalt.md`/`areas/*.md` explicitly, and neither ever names `SPRINT-LADDER-v0_1.md`,
`BACKLOG.md`, or `MVP-CHARTER-v0_2.md`. The sprint state is being kept current in
`areas/cobalt-sprints.md` instead (correctly, and it IS current — updated today) — but that means
the document Dejan wrote the plan into is never the one anyone re-reads or re-writes.

**Smallest proposed fix (proposal only, not applied):**
- Add one line to `CTO-DESK-WAKEUP.md`'s INDEX CARD, after item 5 (LAWS.md): "6a.
  `docs/00 - Project/SPRINT-LADDER-v0_1.md` — current sprint window, feature/prompt table; check
  its dates against today before planning any new build."
- Add one line to `SESSION-CLOSE.md` step 4 (Append areas/topics): when a ladder feature or
  code-prompt changes status (built/dark/live/reverted), append the same line to the ladder file's
  own feature row (not just `areas/cobalt-sprints.md`) — one row edit, not a rewrite — so the two
  never diverge again.

## §6 Bottom line for his three questions

- **Did we abandon the ladder / are we off-script?** No feature has been dropped or contradicted;
  the plan is being followed. The ladder DOCUMENT was abandoned as a read/write target on 09-13;
  the actual tracking moved to `areas/cobalt-sprints.md` and the daily `cto-*.md` reports without
  anyone deciding that on the record.
- **How do we know we're running the correct sprint?** By reconstruction (this audit), yes — S2
  Radar 19a, 09-10→09-23, is the sprint in progress, matching `areas/cobalt-sprints.md` and every
  `cto-*.md` this week. Nothing currently confirms that automatically; see §5's fix.
- **Finished / left / behind?** S1 fully done and accepted 09-08. S2: pool (F2) live; cards
  (F8/F10) built and dark, pending a shadow run + his HITL approval; ranking persistence and
  replay/miss-line (F3 tail, F12, F13) built, not yet merged (P4, blocked on his one open A/B);
  the Agent SDK spike never ran; **zero live mornings** logged against a 2–3 requirement with only
  2–3 trading mornings left before 09-23. Verdict: AT RISK, not LATE yet — recoverable if P4
  merges this weekend and the cards flip live with a shadow run starting Sunday night/Monday.
