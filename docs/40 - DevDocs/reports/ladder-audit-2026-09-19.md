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

## §7 CARDS LIVE BY MONDAY — critical path (added after R12/R13, 2026-09-19 10:56/11:00 ET)

**Correction to §2 above:** §2's F8/F10 "to go live" column read L7 as blocking the flip itself.
It does not — see (2) below. R13 (11:00 ET) already settled this exact question the same way this
section does; both are recorded here for one evidence trail.

### (1) What keeps the cards dark today, and the exact switch

Dark today by ONE key: `radar.cards_enabled: false`, in the card-settings file the desk wrote
`/Users/cobalt/cobalt/data/backups/pre-s2-p2-2026-09-17/p2-dark-settings.yaml`, sha256
`945e42f86997559267b2e7c20783f2d023b9135ae4bb437ca25a4999ca7cd3ca`
(`cto-2026-09-17.md:178`). Loaded into production as part of the `deploy-2026-09-19` stack
deploy 08:25 ET (`cto-2026-09-19.md` R7, `deploy-2026-09-19.md`). Absent/false = the radar's S5
"evaluate" stage (card creation, F8) refuses loudly; S1–S4 (pool scan) still run
(`cto-2026-09-16.md:79`).

**Switch:** `cobalt settings load --card <file> --sha256 <hash> --apply` — the same command,
against a NEW file with `radar.cards_enabled: true` plus the two dark-only-optional keys filled
(below). Built and tested in S2-P2 (`plan-s2-p2-2026-09-15.md` STEP-6 Astra R1-5/R2-2; already
merged/dark-deployed, so the mechanism itself needs no further code).

**Who may run it:** either (a) Dejan's own hand — exempt from a separate HITL token under
**L28** [amended 2026-09-15]: "a trader-run `cobalt settings load --apply` … is exempt from the
HITL token: the trader is already in the loop"; or (b) the CTO desk/a hub, on his explicit typed
"approve" of the exact file + sha256 in chat, which **L61**'s interim clause makes the HITL
approval ("Dejan's spoken or typed 'approve' … for the exact action the desk named … IS the HITL
approval").

**Restart needed?** **No.** `test_settings_are_re_read_on_every_call_not_cached`
(`s2-p2-build-opus-B-2026-09-16.md:53`) proves card settings are re-read on every call, not
cached — so **L43**/**L66**'s restart windows (20:00–21:00 ET pause, or overnight idle on a
trading day) do not gate this change; there is no merge and no resident restart in it. The
underlying WRITE does still refuse inside the 20:00–21:00 ET `market_reset` block
(`assert_writable`, `cto-2026-09-17.md:177`, `session/models.py:36`); **not verified** whether
that block is keyed to trading days or to wall-clock time alone (i.e., whether it would also
apply on Saturday/Sunday) — moot either way, since Sat/Sun leave many hours outside that one-hour
window. Sunday is a non-trading day (radar `idle:overnight` all day, confirmed
`cto-2026-09-19.md` §0 day-open); Monday premarket opens 04:00 ET.

### (2) Every gate between "deployed dark" and "live" — status

| Gate | Text | Met? | Evidence |
|---|---|---|---|
| **L52** tribunal before build (scoring/ranking design) | "A design that touches scoring, ranking or anything that reaches the card requires a TRIBUNAL before any build." | **MET** | `tribunal-grok-2026-09-14.md`, `tribunal-analyst-2026-09-14.md` preceded `plan-s2-p2-2026-09-15.md` |
| **L67** ≥1 other house checks every deployment | "any design, development or DEPLOYMENT is checked by at least ONE house other than its author" | MET for the code already dark-deployed (3-house check before 09-19 08:25, `cto-2026-09-19.md` §5a); **NOT YET MET for the go-live settings file itself** — a new artifact, not yet reviewed | needs a fast review round this weekend (pattern this week: ~15–90 min turnarounds) |
| **L28**/**L61** approval of the settings load | trader-run = exempt HITL; desk-run = his typed "approve" of file+sha256 | **NOT YET MET** — no go-live file drafted or approved yet as of this audit | — |
| Two dark-only-optional values (`card.alignment_default`, `card.shadow_promotion_bar`) | code refuses `cards_enabled=true` while these are null (`test_absent_dark_only_optional_keys_are_null_and_enabling_requires_them`, `s2-p2-build-opus-B-2026-09-16.md:53`) | **NOT YET MET** — "09-19 values session" still pending as of 10:56 ET (`areas/cobalt.md` NOW) | `card.shadow_promotion_bar` numeric defaults already tribunal-ruled 09-14 group-2 (`{sessions 10, pairs 30, median_max 1, within2_min 0.90}`, `plan-s2-p2-2026-09-15.md:223`) — likely just needs loading; `card.alignment_default`'s semantic mapping is explicitly OPEN in the plan (Astra R1-23/R2-6) and the plan's own fallback is to ship it N/A through S2 — confirming "ship N/A" is likely all that's needed here, not a fresh design |
| **L7** shadow-mode promotion ("no variable/grader/detector flips human-fed→engine-fed without a shadow run … and HITL-token approval") | Does this block Monday's flip? | **NO — does not block.** The plan defers the actual flip of computable dots to engine-authoritative to **S3**, not S2: `plan-s2-p2-2026-09-15.md:286` — "S3: … **curve tribunal + L7 promotion for computable dots** (R6) … the three desk dots' HITL flip on `shadow-report` evidence." In S2, dots render **hollow** regardless of the computed value (`s2-p2-build-opus-C-2026-09-16.md:7`: "hollow shadow dots"); the computed score is stored silently (`radar_score.desk_shadow`, mirrored only into the dot's *reason* text as "desk shadow: n", plan:204) and grading stays his tap (`STEP-6`, `POST /card/{id}/key {grade}`). **Confirmed directly**: Dejan ruled R13 (11:00 ET, `cto-2026-09-19.md:26`) — "Yes, Monday to Wednesday can be the shadow run" — cards visible/advisory, he grades by hand on the existing sheet, engine dots recorded beside his for the agreement numbers; this "does NOT cover: the switch-on itself … [or] PROMOTION after the shadow" (still L7/L8 gated, later) |
| **L8** sample-size (n<30 = "insufficient data", never a number) | EV/auto-grade display | **N/A now** — no EV or engine grade is asserted to him in S2; applies only at the later S3 promotion, per R13's own text ("n stated, L8") | — |
| **L43**/**L66** restart windows | resident restart timing | **N/A** — no restart required, see (1) | — |

### (3) Dependencies

- **S2-P4** (`sprint-2/p4`, READY, unmerged, blocked on the Asset Type A/B): **not a dependency**
  for the flip. F8/F10/the settings loader are entirely inside the already-merged S2-P2 code. P4
  covers F3's pick-vs-rank tail, F12 (missed replay), F13 (benchmark/miss line) — separable, can
  land after Monday.
- **S2-P3 panel**: **not an extra dependency** — the live card ladder route (`/radar`) is the
  same route S2-P3 built the read-only shell for; S2-P2 chunk C wired the real cards into it and
  that is already dark-deployed together. Pool view has been live since 09-15.
- **ops-0919 / archiver append-only**: **not a dependency** — parallel, unrelated hardening of
  the bars/archiver data path. F2 (pool) already runs live on the current archiver.

### (4) Ladder's "S2 smoke" — does it exist, has it run

Command exists: `cobalt smoke s2` (`src/cobalt/smoke/cli.py`, built in S2-P4 chunk C, commit
`a566cbc` 09-17). Recorded-session config exists: `configs/cobalt/smoke/s2.yaml` (checks K1–K18).
**Has not produced a green run anywhere in the evidence found** — the only invocation on record
is `uv run cobalt smoke --help` (`s2-p2-build-opus-C-2026-09-16.md:78`, sic — actually the P4
build report). By the P4 verify hub's own finding (`s2-p4-verify-2026-09-19.md` ESCALATE 5a),
some checks (K9.2/K9.3/K9.5/K9.6) read FAIL/ERROR "by design" until the first
`com.cobalt.replay` job runs — which only exists on the unmerged `sprint-2/p4` branch. **So a
genuinely green `cobalt smoke s2` cannot happen before P4 merges and one replay cycle completes —
not by Monday.** Whether the ladder's 2–3-live-mornings credit formally requires a green
`cobalt smoke s2` first (the ladder's own S2-smoke paragraph sequences it before "live mornings
1–3") or whether R12/R13 supersede that ordering for schedule reasons is **not settled in any
record found** — flagged as open, not answered here.

### (5) Dated minimum sequence, Sat 11:30 ET → Mon 04:00 ET

| When | Step | Gate it clears |
|---|---|---|
| Sat ~11:30–13:00 ET | Values session: Dejan confirms `card.shadow_promotion_bar` (load the 09-14 tribunal defaults) and `card.alignment_default` (confirm "ship N/A", the plan's own fallback) | the two null-value gate |
| Sat afternoon | Hub drafts the go-live settings file (`radar.cards_enabled: true` + the two values), sha256, dry-run diff | prerequisite artifact |
| Sat afternoon/evening | ≥1 non-Fable house reviews the go-live file (Fable is restricted to answering him + Sunday's tribunal under today's R9) | L67 floor |
| Sat evening or Sun (outside 20:00–21:00 ET) | Dejan approves by file+sha256 and runs `settings load --apply` himself, or approves for the desk/hub to run it | L28/L61 |
| Immediately after | Read-only proof (`cobalt validate` / radar log) confirms `radar.cards_enabled=true` loaded, S5 no longer refusing | verification |
| Sun (parallel, non-blocking) | P4 Asset-Type A/B, P4 merge, ops-0919/archiver checks, Sunday 13:05 bars tribunal | unrelated tracks |
| Sun overnight | Radar `idle:overnight` (session gate) — nothing to observe | — |
| **Mon 04:00 ET** | Premarket scan cycle re-reads settings (not cached), S5 evaluate stage runs, WATCH cards start forming on precondition (F8) | **first live/shadow morning begins** |

**Gate that cannot be met by Sunday night:** none of the mechanical gates found are structurally
impossible by Sunday night — the values session, the file draft, one house's review, and his
approval are all same-day-turnaround items by this week's own pattern. The one gate that
genuinely cannot complete by Monday is L7's full **promotion** (10 sessions / 30 pairs of
agreement data, L8's n stated) — but R13 already rules that gate does not apply to Monday's
go-live; it governs a later S3 flip. The real risk is execution bandwidth, not a law that blocks
the date: the values session has not happened yet as of this audit, and Dejan is simultaneously
running two more weekend deploys and Sunday's bars tribunal.
