# S5 this weekend, and the not-MVP list · brain answer · 2026-10-10

Request: desk R771, on his R849 (`cto-2026-10-10-words.md:4`): "finish everything you can … Whatever has you building most of the needed components", and "are you sure you are tracking everything not in MVP".
Sources: `docs/00 - Project/SPRINT-LADDER-v0_1.md` (LADDER), `docs/00 - Project/MVP-CHARTER-v0_2.md` (Charter), `docs/00 - Project/BACKLOG.md`, the Memory vault (LAWS, `areas/cobalt*.md`). Every line below cites the file:line it rests on.

## §0 Headline
- S5 has no design doc, card or draft for any component, and the Agent SDK spike that gates F20/F21 never ran (LADDER:488, status 09-24 "NOT STARTED"). Under L67 every S5 design goes through a tribunal before its card, so a build this weekend starts at the design proposal.
- The weekend runs four lanes in parallel. The design and tribunal work runs side by side; builds share only the `cobalt_dev` lock, so they run in series.
- The desk's parked list lacked six items: the JEV trial, X5, the model-by-complexity tribunal, bars 1a/2/E, H2, and B2 offsite. The full table is below. The desk writes it into memory now (10-05 ROW C).

## THE WEEKEND S5 PLAN

### Seams (who shares files)
- F4 and F5 share `src/cobalt/prefill/daily.py`, `configs/cobalt/prefill.yaml` and `configs/cobalt/jobs.yaml` (Charter:82-93; both write the daily note). LAWS:363 says the seam is settled in ONE doc both cards cite before either launches. His order is F4 first, then F5 (R849, `cto-2026-10-10.md:7`). F5 builds on F4's merge.
- F20 and F21 are linked through the SDK chassis and the `cobalt_brain` memory, and both are gated by the spike (LADDER:925-928). F21 also needs an embedder ADR first (`memory-history-2026-09-20.md:224-227`).
- F23 is independent. Only the one `jobs.yaml` row it adds is shared; that is a small seam, handled by the R746 rule if a trial merge conflicts.

### Lanes, in order of launch
1. **Lane A, F4 (MUST).** Opus 5.5 design drafter: the F4 proposal from Charter:82-87, LADDER:932 and the prebell references (`docs/90 - References/`, `areas/cobalt-sprints.md:42`), PLUS the F4/F5 seam doc (LAWS:363). Then the tribunal (Sonnet hub, four houses, L67). Then an Opus card drafter, the Sonnet preflight, the Opus 5.5 build (BUILD-HUB:3, L29 write path), the check (Opus plus both outside houses, next-flow change 1), and the deploy, any hour (L43).
2. **Lane B, F5 (MUST).** An Opus 5.5 design drafter starts at the same time as Lane A's and cites the same seam doc. Tribunal, then card. The build launches only after F4's merge, based on it.
3. **Lane C, the Agent SDK spike (gates F20/F21).** Sonnet 5.5, non-write, research only (LADDER:470; his 09-20 R39 "keep it"). Its questions are `docs/30 - Design/kashef-mining-memo.md:24`, and it writes one report. After its verdict: an Opus F20 design proposal, then tribunal. F21 waits for the F21 embedder ADR proposal (Opus), which can run in parallel with the spike, then tribunal. No F20/F21 build starts before the spike's report and its tribunal.
4. **Lane D, F23 (first to slip, LADDER:925).** An Opus design drafter, then tribunal, card, and an Opus build. The ladder's "Sonnet for S5-P5" (LADDER:942) is overtaken: BUILD-HUB:3 and L29 put every build on Opus 5.5. It runs whenever the lock is free after F4.

### Model per seat (the current rule; no complexity rule exists yet)
- **Builds and checks:** Opus 5.5 (BUILD-HUB:3, L29).
- **Design proposals and card drafting from a design:** Opus 5.5 (`topics/cto-desk-contract.md:34`).
- **Mechanical drafters, preflights and tribunal hubs:** Sonnet 5.5 (same :34, :40).
- **Fable 5.1:** not asked. No seat needs it unless a tribunal splits on a design; then I name it, and he says yes (`cto-desk-contract.md:39`).

### What must come before a build (L52, L67)
- **L67:** a design proposal and a tribunal for each of F4, F5, F20, F21 and F23 before its card. This is law, not a question for him.
- **L52** (scoring or ranking reaching the card): not triggered. No S5 item ranks or scores.
- **LAWS:363:** the F4/F5 seam doc comes before either card launches.
- **Spike:** F20/F21 need the spike report (Lane C) and F21's embedder ADR.
- **For Dejan, only if a design needs it:**
  - F20 needs a new resident subscription seat or a new permission class (Charter:195-198; the credential broker is "INTERIM until S5-P3", `LAWS-FINAL-2026-09-22.md:231`).
  - F4/F5 change a field he owns. His text stays byte-identical (Charter:82-87).
  The tribunal names either one if it arises. Nothing is asked now.
- **Retirements:** the old briefing and the Mattermost listener retire only when F5 and F20 land (`areas/cobalt-sprints.md:12`). This is not a blocker.

## THE NOT-MVP LIST (state · blocker · source)
| Item | State | Blocker | Source |
|---|---|---|---|
| JEV trial (typesafe.ai, `jev/trial-0923`, tip `f4e8de85`, $5 cap) | PARTIAL: built, 3 fix rounds, one keyed probe, NOT merged (09-23) | Final check `74` never launched; N3 (the trial runs) not approved; R34 "which house is JEV" open since 09-24 | LADDER:551; BACKLOG:370; PROJECT-LEDGER.md:1975 |
| JEV router ruling | RULED 10-03 R8: the router waits for the complexity tribunal and the JEV picker, then shadows an Anthropic seat to 80% agreement | The complexity tribunal | `areas/cobalt-houses.md:27`; `cto-2026-10-03.md:14` |
| Model-by-complexity tribunal | NOT STARTED. His R73 (10-02): wait at least a week and record per-job stats first | Precondition met in time (a week passed 10-09); the per-job MEASURE rows exist since 10-05 (next-flow change 5). STARTABLE: an Opus proposal from those rows, then tribunal, as a non-write side lane | PROJECT-LEDGER.md:2704 |
| X5 routing retro (94 rows, Grok/Gemini) | PAUSED 09-23; report untracked, last line "run in progress" | A free house lane (~5.3 h); routing laws frozen meanwhile | BACKLOG:84; `side-lanes-2026-09-27.md:13` |
| Routing tribunal (owner items 20–37) | DONE 09-23 R21 | — | BACKLOG:84 |
| Typed-classifier (typesafe) design tribunal | NOT STARTED; research done 09-21 | Queued after S2 and setups | `areas/cobalt-product-definition.md:47` |
| Bars chunks 1a, 2 and E | Built and checked, NOT merged (09-21); past L46's 3-day cap | On no plate since 09-23 | BACKLOG:85, 87, 370 |
| Second Chance redesign sitting | PENDING, unheld since 09-24; R117 keeps it off the radar until redesigned | His sitting (5–10 chart examples) | BACKLOG:614 |
| Second Chance radar cards despite R117 | OPEN TO HIM; ~8 cards a day since 09-24 | His call | `areas/cobalt.md:16`; `cto-2026-10-06.md:152` |
| VWAP Continuation sitting | PENDING, after Second Chance | His sitting | BACKLOG:615 |
| H2 low-float rank | NOT STARTED (09-25 R83); a design item after H1 | Pool order is his under L53; the 09-27 ALL STOP | BACKLOG:371 |
| Setup-builder | FUTURE (09-21 R45c) | Once the seven-setups pattern is proven | BACKLOG:363 |
| Guardian | Post-MVP MUST, first | Grading/EV live, alerting, Rules Engine session | Charter:352; BACKLOG:512-518 |
| Mailbox on his domain | Post-MVP (ruled A 09-16) | After MVP | BACKLOG:498-511 |
| macOS 27 host upgrade | DEFERRED (09-17 R18) | Build lane done, plus the 6-point checklist (restic rotation, offsite, rebuild manifest) | BACKLOG:460-483 |
| Rebuild / DR manifest | PARKED to S5 planning (09-09) | Gates the macOS upgrade | `areas/cobalt-sprints.md:17` |
| Sessions-as-jobs gap analysis | NOT STARTED (planned after S2) | The desk writes the prompt | BACKLOG:484-497 |
| B2 offsite backup, restic password rotation | NOT DONE; one local disk, which already died once (09-06) | B2 credential, his hand | LADDER:962-963; BACKLOG:90, 475 |
| Voice "stt mishears: next model up" | NOT TRIGGERED: transcripts clear, the planner was the cause, fixed 10-09. Speaker-to-microphone bleed noted | — | `voice-clarify-confirm-answer-2026-10-09.md:18` |
| Voice other: V1 device sitting, Kokoro TTS (HELD 09-27), X-E10 round 2, A1 "I" refusal | OPEN | His sitting; the ALL STOP hold | LADDER:679, 704, 706; BACKLOG:361, 365 |
| D5-3 rule question | OPEN TO HIM | His ruling (non-blocking) | `cto-2026-10-06.md:27, 161` |
| Wake-up log cause column | Kept empty by his 10-03 R78 | His word | `CTO-DESK-WAKEUP.md:35` |
| X29 fixture error (`offline_skip_guard`) | OPEN | Its own card, not drafted. STARTABLE: a small drafter card | `cto-2026-10-06.md:152`; BACKLOG:64 |
| "Dream" memory consolidation | PARKED at F21/S5 | F21 | `topics/memory-system.md:10`; Charter:398 |
| Rules Engine / Taxonomy / Data-Model sessions, HITL rebuild | Design-session register, unchecked | The Charter's order | BACKLOG:375-405 |
| S4 leftovers: Toast listener, other trigger types | Post-MVP lane | — | LADDER:916 |
| TV webhook extended hours, alert-slot cap | Post-MVP SHOULD | — | LADDER:968 |
| Purchase gate (Massive Advanced/Developer) | Last in the post-MVP lane | Proven value | Charter:362-368 |
| Strike live proofs: B5 alert, phone-DM fallback | Waits for Monday's first trigger, and a trigger no tab draws | Market hours | brain B5 answer 10-10 |
| Launcher card rows: `--fix-report`, accept held items named fixed, `.bak` in D0 | OWED, one card | A drafter | direction file, 10-09 plan rows |

## FOR THE DESK
1. Launch now, in parallel: the Lane A F4 design drafter (Opus, with the F4/F5 seam doc), the Lane B F5 design drafter (Opus, citing the seam doc), the Lane C spike (Sonnet, non-write), the F21 embedder ADR proposal (Opus), and the Lane D F23 design drafter (Opus). Then a tribunal hub per proposal as each lands.
2. Write this table into the vault memory's parked list in the same cycle (10-05 ROW C). The OPEN TO HIM line keeps only his items.
3. Startable side lanes, when a seat is free: the model-by-complexity tribunal proposal (Opus, from the MEASURE rows), the X29 card, and the launcher card.
