BLIND: I did not read the houses' folder or the hub's report.
RUN DATE: 2026-09-22 19:50 EDT (started) · written 19:58 EDT (`date`)

## DIGEST FOR THE DESK

TRIBUNAL R1: ADOPT AFTER write-path scope ruled, bare § refs fixed, L33 profile carried, T6 run blind
- T1 ADOPT · SELF no
- T2 ADOPT · SELF no
- T3 ADOPT WITH · SELF no — "records as passing" undefined for RULED rows; cost orders permitted rows, never creates one
- T4 ADOPT WITH · SELF no — YAML keyed by task class; interim = the §4 ruling; MODELS.md and role hints rendered (L3)
- T5 ADOPT WITH · SELF no — S made checkable BEFORE a build: prompt names artifact path + failing test (L45)
- T6 ADOPT WITH · SELF no — non-Anthropic seat; classes assigned from prompts BLIND to outcomes, then joined
- T7 ADOPT WITH · SELF yes (UNMEASURED) — restore "or higher"; no bare §/[D1]; name the workspace change
- T8 ADOPT WITH · SELF no — PASS counts FIX rows (L75), not HOLD rows; shadow costs a build + a check
- T9 ADOPT WITH · SELF no — L23, L25 as proposed; L22 unchanged (L31 does not cover law text)
- T10 ADOPT · SELF no
- T11 ADOPT WITH · SELF yes (UNMEASURED) — Sonnet shadow on a prompt with a known Opus record; Haiku as CHECK hub on a known answer
- T12 ADOPT WITH · SELF no — add stale `grok-4.6-build` key, `report.py:127` "(L29)", L25 reason-class column, Grok model pin
- (a) ADOPT WITH · SELF no — row 3 DOES NOT HOLD for deploy-2026-09-22 (dev migrate, auto mode); rows 13/14 omit adverse records
- (b) ADOPT WITH · SELF no — Sol profile to L33 has no L33 text (dropped); L26 pasted text below
- (c) ADOPT · SELF no
- (d) ADOPT WITH · SELF no — floor LOOSENED by PASSED clause; never-auto KEPT; gate KEPT + changed
- (e) ADOPT WITH · SELF no — `05-stacked-deploy.md` is S+W, not "no write path"
- (f) ADOPT WITH · SELF no — the trial report holds numbers, the row cites it; n is his
- (g) ADOPT WITH · SELF yes (UNMEASURED) — rows cite R46; L67's ids to him as RE-OPENS A RULING (R46)
- (h) ADOPT WITH · SELF yes (UNMEASURED) — a meter event never edits a row; the fallback lands on Anthropic today
- EXPERIMENTS: X1 write-path launch-shape scratch test · X2 Grok model pin · X3 Sonnet shadow of bars chunk 2 · X4 Terra shadow · X5 Haiku check-hub known-answer replay · X6 local checker beside cloud · X7 blind retrospective · X8 5.5 shadow (trigger a)
- OWNER: D1 MIS-FRAMED (prod/dev decides all three W conditions, not the model alone) · D1 premise (Sync race, not tier) · D2 OK (Option A adds "none idle") · D3 missing "what the hub seat requires" · n / thresholds for T6, T8, trigger (c) · RE-OPENS A RULING (R46)
- SELF: yes = 4, all 4 UNMEASURED (RULED or none) · 6 lines AGAINST my house listed
- WITHDRAWN: 2 · ESCALATE: 2

## Rulings

### T1 — split ENGINE routing from SEAT routing
ADOPT
SELF: no
- The split rests on a measurement: my grep of `src/cobalt` for `completion(|messages.create|chat.completions|litellm|anthropic|openai|mainframe` returns only the heartbeat's port probe (`heartbeat/probes.py:252`, `runner.py:140`) and two comments (`jobs/restarts.py:34`, `seatusage/report.py:287`). There are no engine model calls in new-core.
- The old tree's calls are REDESIGN/Moot/Absorbed in TRIAGE (`TRIAGE.md:43`, `:124`, `:125`).

### T2 — L5's new text
ADOPT
SELF: no
- Old L5 bound "every LLM call goes through the routing layer; out-of-band calls … are routing bypasses". The new text binds the same for code ("ONE model-access module … a direct call … is a defect") and matches L22's "Cobalt code is the hub" (`LAWS.md:129`, `:16`). Nothing is dropped.
- The seat-table reference only works once the table exists. The interim is ruled under T4.

### T3 — L24: rungs are a cost order
ADOPT WITH "L24 Three-rung economics (ruled 08-29/31; amended <date>). The rungs are a COST order, never an assignment: (1) local = zero marginal cost · (2) subscription seats = prepaid and bounded by weekly meters, each meter a monitored resource (L25) · (3) metered APIs = paid per token, engine calls only, sync-only, bounded, cost-footered, the narrowest rung. Among the rows the seat table already names for a task class, the cheapest rung goes first; cost never creates a row."
SELF: no
- Failing scenario: today every seat row is RULED (`ROUTING-PROPOSAL-2026-09-22.md:148-161`). "Records as passing that task class" has no meaning for a RULED row. Two desks would disagree on whether Sonnet "passes" deploys. My wording lets cost choose only among rows that already exist.
- Dropped and named: the old rung-2 mechanism "async via dead-drop (Grok Bot etc.) and sync via in-session CLI bridges for code work" (`LAWS.md:138`). It describes channels and binds no obligation. "first" moves to L23 as "first ASSESSED" (see T9).

### T4 — the seat table's FORM and home
ADOPT WITH "The seat table is `configs/cobalt/seats.yaml`, keyed by TASK CLASS, never by model id. It has a Pydantic schema validated on load and a dry-run that prints the row a named prompt would take (L10). A table that fails to load crashes; a launch whose model the table does not name is refused loudly (L1). `docs/50 - Roles/MODELS.md` and the seat-usage role hints are rendered from it or retired (L3). Until the table is committed and loads, a seat's row is the desk-report §4 ruling that seated it, cited in the launch prompt."
SELF: no
- L3: there are already three copies of assignments: `MODELS.md:15-18` (stale `claude-fable-5`), `seat_usage.yaml:78-83` (hints citing "L29 floor/ceiling", stale `grok-4.6-build` at :82 against the observed `grok-4.7-build` at `seat-usage.md:33`), and the desk rulings.
- Failing scenario without the interim: the fold lands before `seats.yaml` is built. L5/L26/L29 then point every launch at a table that does not exist, and a worker could refuse a lawful seat. The interim sentence costs nothing: every launch prompt already cites its §4 row (this prompt's line 1).
- Cost: a build (schema, loader, dry-run, renderer), checked by three houses under L67.

### T5 — class S / H + W overlay
ADOPT WITH "Class S: the prompt names, by path, the real artifact its spec is defended against AND the committed test or fixture (L45) that fails on a wrong guess. Every other prompt is class H. W: the session's steps or allowlist include a write path (L29). The class is written on the prompt's SEAT line before launch. The key binds as a rule only after the retrospective validation (T6) is on file."
SELF: no
- His axis (`PROJECT-LEDGER.md:1325`) survives word for word in substance. What I add is the pre-build test. With the proposal's §4 wording, the class is readable only after the outcome: the proposal itself re-labels S2-P1 "H disguised as S" (`ROUTING-PROPOSAL-2026-09-22.md:182`). A 09-10 desk reading "defensible against a real-world artifact" would have classed it S.
- Cost: one `CLASS:` token on every prompt's SEAT line, checked by grep at dispatch.

### T6 — retrospective validation
ADOPT WITH "Before the class key binds, a hub seated on a house OTHER than the proposing house tables every build 09-10 → 09-22 in two passes. Pass 1 reads the build prompts only and assigns S/H/W. Pass 2 joins the known outcomes (check FIX rows, gate, rounds, deploy). The table and the pass-1 file are committed separately, pass 1 first. Dejan sets what match rate means 'predicts'."
SELF: no
- L26's conflict applies to the measurer. The proposer is Anthropic, and the table would decide Anthropic's builder seats.
- A classifier that can see outcomes fits them, as the S2-P1 relabel shows (above). Committing pass 1 first makes the fit checkable.
- Which non-Anthropic house runs it is the desk's choice by meter (L47). Codex is out until 09-26 06:47 (R13, `cto-2026-09-22.md:130`).

### T7 — L29's new text and trace; clause .6 by name
ADOPT WITH "L29 Write-path seat rule (ruled 09-03/04; amended 09-07, 09-10, 09-12, 09-13, <date>). A WRITE PATH is a vault or DB write, migration, delete, recovery or forensics. A session on a write path runs only when (1) its model is the house's top implementation model or higher, or its seat-table row (L26) records that model PASSED for that task class by a measured shadow trial; (2) the house's permission gate is proven in a scratch test to stop file AND command writes outside the session's own workspace; (3) its launch line states its permission mode, and that mode is never auto mode. A session with no write path takes its model from its seat-table row. Any house may hold any seat on these terms; no house is privileged. The architect seat is assigned to any house by his ruling, another house reviewing. Code sessions are cleared every turn: durable state lives in the plan file and the report; one scheduled small-context wake-up is permitted."
SELF: yes · EVIDENCE: UNMEASURED (RULED L29 09-03/04; no trial compares tiers on a write path)
- Clause .6 "never auto mode on a write path" is KEPT in (3), and its substance is word for word.
- What the proposal's text dropped, now restored: "or higher" (`LAWS.md:169`). Without it, a Fable forensics seat above the floor has no law text. The trace sends it to "seat table (ruled rows)" (`ROUTING-PROPOSAL-2026-09-22.md:106`), which is not a law.
- Removed: the bare "(§5)" and the "[D1]" placeholder. LAWS.md's notation rule makes the fold refuse a bare §-reference (`LAWS.md:12`). D1's outcome goes into the text as he rules it.
- Named change the trace omits: (2) adds "outside the session's own workspace". The old text said only "stop file AND command writes" (`LAWS.md:169`; H-L29c `LAWS-HISTORY.md:60`). I keep it, because a builder must write its worktree, but it is a change and is named here.
- Failing scenario the text cannot fix: builds `27`/`31` (`--model claude-opus-5-5 --permission-mode auto`, prompt :1) and deploy `05` (`claude-sonnet-5`, `--permission-mode auto`, `05-stacked-deploy.md:6`) run `COBALT_ENV=dev uv run cobalt db migrate`. That is a migration under both texts, so they are write paths in auto mode. This goes to his OWNER item (D1 re-framed) and is not settled here.

### T8 — re-test procedure, PASS bar, n
ADOPT WITH "PASS bar: gate green on both suites; FIX rows (L75 classification of the check's HOLD rows) ≤ the incumbent's on the same prompt; no false completion or failure claim (L35, L70); wall-clock and meter recorded. The check hub stages both builds' diffs unlabelled. A PASS verdict rests on the hub's file-check rows, never its opinion. n = 1 is a spot check, labelled so; the class-level n is his."
SELF: no
- HOLD ≠ defect. In `bars-chunk-1a-check-2026-09-20.md:204`, 25 rows HOLD, and rows 5, 6 and 25 (:174, :175, :194) are claims that the build is RIGHT. Counting "HOLD findings" would penalise a build its checkers confirmed. L75's FIX count is the defect count (`LAWS.md:425`).
- Cost: each trial adds one build and one three-house check on an already-checked prompt. With the Codex meter out, a trial that needs Sol or Astra waits.
- Unlabelled diffs: the hub already stages pre-computed diffs (`areas/cobalt-houses.md:63`). Labelling them A/B adds one rename.

### T9 — L23 "first ASSESSED", L25 pointer + vendor names, L22 wording
ADOPT WITH "L23 and L25 as proposed (`ROUTING-PROPOSAL-2026-09-22.md:139-140`); L22 unchanged."
SELF: no
- L25 pointer: ESCALATE 1 HOLDS. ADR-0008 has no "bake" (grep). No file in `docs/10 - Decisions` carries "bake-off", and `git log -S"bake-off"` over that folder's full history is empty, which is an unscoped read (L35).
- L22: L31 lists "code identifiers, schema, config keys, enum values or system design docs" (`LAWS.md:181`), not law text. L67's current text names four houses and `gpt-5.6-sol` (`LAWS.md:365`, `:370`). The edit also leaves "claude-login" and "Claude-on-subscription" in place, so it is cosmetic. Smaller text wins: L22 unchanged.
- L25's "→ LOCAL as the owned always-up floor (also always-on verifier/triage)" must survive the first-hop edit. The proposal touches only "Claude → next-best house".

### T10 — L49 marker off; local next trial role
ADOPT
SELF: no
- Tokens re-derived from `seat-usage.md` for 09-16…09-22: 827 (:199), 786 (:173), 845 (:146), 1,067 (:119), 684 (:91), 758 (:64), 844 (:35). The minimum is 684 and the maximum is 1,067, which HOLDS. GREEN is read for 09-20/21/22 (`day-open-2026-09-20.md:169`, `-21.md:174`, `-22.md:175`). 09-16…19 are UNVERIFIED by this seat.
- All three verdict lines carry a doubled prefix, "SEAT VERDICT: SEAT VERDICT:". Its cause (seat or command) was not read. A checker trial's verdict table therefore needs a fixed shape the hub parses.
- The checker trial never counts toward L67's three checkers (the proposal says "never replacing one"). It carries an L49 cost estimate.

### T11 — first trials
ADOPT WITH "Sonnet: a class-S shadow build of a prompt whose incumbent build and check are on file — `prompts/2026-09-20/11-bars-chunk-2-build.md` (Opus 5; FIX 6) — same base tip. Terra: the same prompt, when its meter allows. Haiku: a CHECK-hub replay of a closed check with a known answer — `bars-chunk-1a-check-2026-09-20` (HOLD 25 · DO NOT HOLD 3 · NOT CHECKABLE 5, :204) — PASS = the same counts and the same stops."
SELF: yes · EVIDENCE: UNMEASURED (Sonnet and Haiku as builder/hub never measured, `PROJECT-LEDGER.md:1325`)
- These are TRIAL rows, the re-test form an unmeasured self-assignment must take. None of them seats anyone.
- The Haiku trial is changed because a read-only tribunal hub has almost no STOP point. His bar for the hub is "verifying proofs against ground truth, and REFUSING TO PROCEED when a proof does not match" (`PROJECT-LEDGER.md:1326`). A known-answer check replay tests exactly that.
- Missing from the proposal: the live trigger (a) case. Opus 5 → 5.5 was seated by ruling (R32), and no committed check record names `claude-opus-5-5` (see SELF-ASSIGNMENTS). That is X8. It does not re-open R36.

### T12 — measurement gaps
ADOPT WITH "Also owed, same ops build: (1) `seat_usage.yaml:82` key `grok-4.6-build` vs observed `grok-4.7-build` (`seat-usage.md:33`), and `claude-opus-5-5` unmapped (`:37`); (2) `src/cobalt/seatusage/report.py:127` renders '(L29)' as the authority for consumer plans, which moves to L27 in this rewrite; (3) L25's reason-class column (status note, `LAWS.md:145`) — `seat-usage.md:29` has none, so no fallback is counted; (4) Grok's launch model is unpinned; (5) the pricing pin for `claude-opus-5-5`/`claude-fable-5-1` (`seat-usage.md:42`)."
SELF: no
- (4): no prompt in `prompts/2026-09-22` carries a `grok-4…` id (grep: only this prompt file). The table's model column cannot be checked against a Grok launch (X2).
- The role hints also use model ids as config KEYS (`seat_usage.yaml:78-83`), which is L31's "config keys" case. Rendering them from a task-class-keyed table (T4) closes it.

### (a) THE FACT BASE
ADOPT WITH the corrections below.
SELF: no
- Row 1 HOLDS (R36 `cto-2026-09-22.md:110`; R109 `:36`). Row 2 HOLDS (hub launch lines `--model claude-sonnet-5`, e.g. `prompts/2026-09-20/14-bars-chunk-1a-check.md:1`). Sonnet's six STOPs are at `PROJECT-LEDGER.md:1326`, not :1325.
- Row 3 DOES NOT HOLD as "no write path" for 1 of 4. `deploy-2026-09-22.md:80` shows the Sonnet hub ran `COBALT_ENV=dev uv run cobalt db migrate` on cobalt_dev, launched `--permission-mode auto` (`05-stacked-deploy.md:6`; :1 "ONE WRITE this run does make is the WITH-DB suite"). The model and DONE HOLD: 4 stop lines, "rollback: not used" (`deploy-2026-09-21.md`, `-21b`, `-21h`; `deploy-2026-09-22.md:212`). Their ESCALATE counts 3/3/3/6 are omitted.
- Rows 5, 8 HOLD (`27`/`31`/`48` :1 `claude-opus-5-5`; R32 `:111`). Row 7 HOLDS (R73 `:73`, R76 `:70`, R109). Rows 9–11 HOLD (R13 `:130`; R46 `cto-2026-09-21.md:57`; `cobalt-houses.md:55`). Row 12 HOLDS: 15,569 (`seat-usage.md:355`) + 36 (`:280`) = 15,605. Row 15 HOLDS (T10).
- Row 13 HOLDS on its evidence (`cobalt-houses.md:60`) but omits the 09-22 sandbox refusal (`:66`), and no launch line pins its id. Row 14 HOLDS on Attempt D (`:51-52`) but omits the audit-house HARNESS 3/3 (`:60`) and the 09-22 blind-seat death (`:66`), and it misses the launch id `gemini-3.1-pro-high` (e.g. `prompts/2026-09-20/14-bars-chunk-1a-check.md:33`). Row 4's `02-deploy-stack-3.md` model is UNVERIFIED here.
- MISSED: Opus as Astra's stand-in on code checks when Codex is out (`LAWS.md:370`; `cobalt-houses.md:65`), an Anthropic role live today. `claude-opus-5` is still running on 09-22 (1,272,075 output, `seat-usage.md:31`; R32's running-session clause). "Zero model calls" HOLDS (T1). ESCALATE 1 HOLDS (T9).

### (b) THE REWRITTEN CLAUSES — dropped obligations
ADOPT WITH (L26 text) "L26 House-agnostic routing (ruled 08-29/31; amended <date>). Right intelligence for the right task, across houses. Every seat assignment is ONE row of the seat table: task class, house, model id, meter, evidence, date, re-test trigger. Evidence is MEASURED (a trial report, a bake-off, a check record, a cost-ledger figure, each with its n) or RULED (his ruling, by date and R-number), named on the row; a ruled row stands, is never passed off as measured, and carries a re-test trigger like any other. The key is the spec class defined in L29's companion design (class S / H, W for a write path). A row is re-tested when its model id changes (a house release or a local model swap), when a meter change makes a cheaper row a candidate, when its class-S builds draw more FIX rows at check than its recorded baseline, or when Dejan asks. Claude recommends against Claude when measurements say so, and every house likewise. Model ids live in the table, never in this text."
SELF: no
- The proposed L26 carries bare "(§4)" / "§5" (`ROUTING-PROPOSAL-2026-09-22.md:57`). The fold refuses those (`LAWS.md:12`). My text inlines the triggers. The S/H definition sits in the derived FINAL, which the text cites by name.
- Named drops: L26's "re-tested as local models improve" (`LAWS.md:148`) was dropped. The proposal's trigger (a) says "a house ships", which misses a local swap, so it is restored as "a local model swap". The explicit "Claude recommends against Claude" was made house-neutral and dropped its words, so it is restored (+1 clause, binds nothing new). L29's Sol profile ("network on", "never `danger-full-access`", "Sol cannot commit", `LAWS.md:170`) goes "to L33" (`ROUTING-PROPOSAL-2026-09-22.md:115`), but no L33 text is proposed and L33 today carries none of the three (`LAWS.md:192-193`). It is DROPPED unless the same fold amends L33 with those words. L24's rung-2 mechanism is dropped as named in T3. L23/L25/L49 drop nothing (T9, T10).

### (c) THE LOCAL SEAT
ADOPT
SELF: no
- L49's text is kept whole. L25's floor clause and the exception-handler amendment are untouched except the pointer (`LAWS.md:142-143`). "First ASSESSED" keeps "Local trumps cloud even when cloud is free — continuity rationale" (`LAWS.md:133`) because only the last sentence changes.
- Gap, not a drop: L25 requires every fallback counted per reason class. No reason-class column exists (`seat-usage.md:29`; status note `LAWS.md:145`). So a cloud fallback that fired every morning would be counted nowhere today. It is carried in T12 (3).

### (d) L29's WRITE-PATH FLOOR
ADOPT WITH the T7 text.
SELF: no
- Top model: KEPT, and LOOSENED by the "or PASSED by a measured shadow trial" alternative. Never-auto: KEPT. Scratch-proven gate: KEPT, moved from the any-house sentence into the conditions, and changed ("outside the workspace", T7).
- Walk: a production migration by a model with a PASSED class-S row earned in a dev shadow build. The proposed TEXT allows it; the "[D1]" marker is not text. It still needs (2) and (3). No launch shape is proven to satisfy "never auto" unattended (`LAWS.md:350`), so today it could only run attended. Also, the dev shadow build that earned the row ran a with-DB gate, which is itself a W session. That session must meet (1)–(3) on the INCUMBENT's model, or no candidate can ever earn a W row.

### (e) THE ASSIGNMENT KEY
ADOPT WITH the T5 wording.
SELF: no
- I class `prompts/2026-09-22/05-stacked-deploy.md` as S + W. The proposal counts it among "S, no write path" (`ROUTING-PROPOSAL-2026-09-22.md:183`). §4's sentence "W overlay: a write path adds L29's three conditions" (:176), plus L29's list ("migration"), classes it W from `deploy-2026-09-22.md:80`.
- A class reading is checkable before the build when it names a path and a test (T5). Otherwise only T6's outcomes check it.

### (f) THE RE-TEST LOOP
ADOPT WITH "The trial report is the evidence; the seat-table row cites it (report path, n) and never copies its numbers (L3). The measurer is the check hub's file-check rows (L35), under L26's conflict clause whichever house the hub is. A row switches only on his one-message approval (L7 shape)."
SELF: no
- The evidence supports only n = 1 per prompt per tier. No prompt on file was built by two tiers. In the spirit of L8, every trial row reads "spot check, n = 1" until his n is met. The number is his (L53, R4).
- Today check hubs are Sonnet (Anthropic). A Terra-vs-Opus trial is measured by the incumbent's house, so the verdict must rest on counted rows, not prose.

### (g) L67's CHECKER SEATS
ADOPT WITH "Seat-table rows for code checks and design seats cite 09-21 R46 as RULED; L67's text is not edited by this fold. The model ids inside L67 [amended 2026-09-21] ('Sol (`gpt-5.6-sol`)', 'Opus 5') are carried to him as RE-OPENS A RULING (R46)."
SELF: yes · EVIDENCE: UNMEASURED (RULED 09-21 R46 + 09-22 R32; keeps the Anthropic checker seat)
- L3: L67 names `gpt-5.6-sol` and "Opus 5" (`LAWS.md:370`). The table would name `claude-opus-5-5` (R32). There would then be two sources, and L67's copy is already stale.
- Removing the ids changes L67's wording, which is his to rule, never folded by this tribunal.

### (h) METER EXHAUSTION
ADOPT WITH "A meter is read before launch (L47). A bound meter makes that launch take the fallback its row names, recorded with the meter reading and reason class in the day's desk report (L34 session row, L25 count). The row itself is never edited for a meter event (per-build, not sticky)."
SELF: yes · EVIDENCE: UNMEASURED (the fallback today names Anthropic: RULED R46, `cobalt-houses.md:65`)
- The 09-22 walk: Codex out until 09-26 06:47. The Astra design seat is covered by R13's per-case "proceed on three" (`cto-2026-09-22.md:130`), a ruling, not a fallback row. The Sol checker falls back to Opus by R46. So the fallback lands on my house.
- Failing scenario the proposal allows: Option A's "moves the seat to the fallback its row names" read as a row edit. That would make a meter event a sticky re-seat, against L47. Cost: one reason word on the existing §5 session row.

## Self-attack

Grep list (prompts = `prompts/2026-09-22` files carrying the name; code = `src/cobalt` + `configs/cobalt` hits):
- `L29`: prompts 37 files (02, 01, 04, 05, 07, 09, 12, 14, 15, 22, 26, 27, 28, 30, 31, 32, 33, 38, 40, 41, 42, 43, 44, 47, 48, 49, 50, 51, 52, 59, 60, 61, 62, 63, 64, 65, 66) · code: `seat_usage.yaml:71`, `:78`, `:79`, `:80`; `seatusage/report.py:127`
- `L25`: prompts 47, 58, 59, 60, 61, 62, 63, 64, 65 · code: none
- `L26`: prompts 07, 43, 44, 47, 62, 63, 64, 65 · code: none
- `L49`: prompts 44, 47, 62, 63, 64, 65 · code: `dayopen/__init__.py:11`
- `bake-off`: prompts 47, 62, 63, 64, 65 · code: none · decisions folder: none, history none
- `seat_usage`: prompts 63, 64, 65 · code: `heartbeat/runner.py`, `heartbeat/probes.py`, `seatusage/{config,runner,report,ccusage,cli}.py`, `configs/cobalt/{jobs,seat_usage}.yaml`, `taxonomy/tunables.yaml`
- `permission-mode`: prompts 66 files · code: none
- `claude-opus-5-5`: prompts 38 files (incl. 27, 31, 48–52 builders; 16, 28, 32, 53–57 checkers) · code: none · houses :66, :67
- `claude-sonnet-5`: prompts 27 files (incl. 05 deploy) · code `seat_usage.yaml:80` · houses: none
- `claude-fable-5-1`: prompts 18, 20, 21, 36, 39, 40, 41, 42, 64 · code `seatusage/ccusage.py:26`, `seat_usage.yaml:47`, `:79` · houses :67, :68
- `claude-haiku`: prompts 64 only · code none · houses none. **No committed file on this surface carries it.**
- `gpt-5.6-sol`: prompts 16 files · code none · houses :65
- `gpt-5.6-terra`: prompts 64 only · code none · houses none. **No committed file on this surface carries it.**
- `gpt-6-astra`: prompts 19, 28, 32, 35, 40, 44, 59, 63, 64 · code `seat_usage.yaml:47`, `:81` · houses none
- `grok-4`: prompts 64 only · code `seat_usage.yaml:82` (`grok-4.6-build`) · houses none
- `gemini-3.1`: prompts 14 files · code none · houses none
- `mainframe`: prompts 63, 64 · code `heartbeat/probes.py:252/256/258/862`, `runner.py:140`, `jobs/restarts.py:34`, `seatusage/report.py:287`, `seat_usage.yaml:59` · houses none

Walk of my text against the list:
- WITHDRAWN: "Terra's trial cannot run before 09-26 because Terra draws the Codex allowance" — `cobalt-houses.md:19` places Terra under the Codex CLI, but `:65` says only "Sol and Astra share the Codex allowance". Terra's meter is UNVERIFIED, so T11 now says "when its meter allows" (X4 reads it).
- WITHDRAWN: "the proposed condition (2) makes the gate proof per session" — the text says "the house's permission gate", and its origin says "before the seat stands" (`LAWS-HISTORY.md:60`). It is per house, not per session.

## SELF-ASSIGNMENTS

- T7 — keeps the top-implementation-model floor, which holds Anthropic Opus on write paths (map row 4). UNMEASURED (RULED L29 09-03/04).
- T11 — Sonnet and Haiku trial rows (trials, not seats). UNMEASURED (`PROJECT-LEDGER.md:1325`: never tested).
- (g) — table rows restating the Opus code-checker seat. UNMEASURED (RULED R46, R32).
- (h) — the Codex-out fallback lands on Opus. UNMEASURED (RULED R46).
- AGAINST MY HOUSE (1): the Opus 5 builds of bars chunk 1a and chunk 2 (`prompts/2026-09-20/10-bars-chunk-1a-build.md:1`, `11-bars-chunk-2-build.md:1`, `claude-opus-5`) drew FIX 13 and FIX 6 (`LAWS.md:425`). Chunk 1a took check rounds r1–r3 (`reports/bars-chunk-1a-check{,-r2}-2026-09-20.md`, `-r3-2026-09-21.md`). The proposal's §4 table shows only the fix speed (`ROUTING-PROPOSAL-2026-09-22.md:185`).
- AGAINST (2): no committed check record names `claude-opus-5-5`. grep count 0 in `setups-one-check`, `stale-marker-check-r2`, `stale-marker-fix-r2`, `ops-6a-check-r3`, `ops-fix-r3` (all 2026-09-22). Every 5.5 seat, this one included, is RULED (R32/R36/R109), and its cost is UNPRICED (`seat-usage.md:37`, `:42`).
- AGAINST (3): meter concentration on 09-22 (`seat-usage.md:31-37`, 19:00). Anthropic output = 1,272,075 + 2,431,236 + 1,053,653 + 1,227,982 = 5,984,946. Others = 616,653 + 26,054 + 844 = 643,551. Share = 5,984,946 / 6,628,497 = 90.3%. agy (Gemini) is not in ccusage, so its share is UNVERIFIED.
- AGAINST (4): the Anthropic builder seat came from the meter, not a measurement. "NO Sol builds this week — every build runs Opus 5 headless" (`cobalt-houses.md:55`).
- AGAINST (5): the write-path floor that holds Opus rests on an incident whose recorded root pattern is an Obsidian Sync race, not a model tier (`PROJECT-LEDGER.md:621-624`; `laws-audit-2026-09-20.md:315`).
- AGAINST (6): his 09-13 assessment, "Opus … cannot run the CTO seat with confidence" (`cobalt-houses.md:25`). It is an assessment, not a measurement. Row 1 is his R36/R76 trial.

## Experiments (L70)

- X1: the write-path launch shape. On a scratch worktree, launch `claude --bg` with a write-path allowlist missing one write command, under each mode the desk would use other than auto. PASS = it stops without a dialog and without writing (L63 note, `LAWS.md:350`). The result decides whether (3) is satisfiable unattended. Repeat per house for condition (2).
- X2: Grok model pin. Check whether the `grok` CLI takes a model argument and prints the model id it ran. If not, the seat table's Grok model column is observed-after, never enforced.
- X3: Sonnet 5 shadow build of `prompts/2026-09-20/11-bars-chunk-2-build.md` on its original base tip, with the same three-house check, compared to Opus 5's FIX 6. It changes whether Sonnet gets a class-S builder row.
- X4: Terra, the same prompt, after reading which meter Terra draws. It changes Terra's row and the Codex budget.
- X5: Haiku as check hub replaying `bars-chunk-1a-check-2026-09-20` on its staged packet. PASS = 25/3/5 counts and the same stop decisions. It changes whether Haiku can hold a check-hub seat.
- X6: the local seat as a read-and-judge checker beside a cloud checker on a class-S diff. It records wall-clock against its up-front L49 estimate and its verdict against the file-check rows. It changes whether local gets a (non-counting) checker row.
- X7: T6 run blind (pass 1 prompts only, committed; pass 2 outcomes). It changes whether the S/H/W key binds.
- X8: `claude-opus-5-5` shadow of a class-S prompt with an Opus 5 record, the trigger (a) case. It changes the Opus rows from RULED to MEASURED or not. It does not re-open R36 (his evaluation stands).

## OWNER (after the tribunal)

- D1 — MIS-FRAMED. It splits production from dev for condition (1) (the model) only. The same split decides whether a dev migration or a with-DB suite is a "write path" at all, and so whether (2) the gate and (3) never-auto bind it. Today builds `27`/`31` (Opus 5.5, auto) and deploy `05` (Sonnet 5, auto) ran dev migrations (`deploy-2026-09-22.md:80`). This is the audit's unanswered C5 question (`laws-audit-2026-09-20.md:270`, `:281`); L62 left the mode unsettled (`LAWS.md:344`). He rules the scope of "write path" for all three conditions.
- D1 — premise. "The floor exists because his notes were overwritten." The ledger's root pattern is a Sync race (`PROJECT-LEDGER.md:621-624`). Whether tier protects notes is unmeasured.
- D2 — framed correctly. Note that Option A adds a new obligation, "none is left idle by design", for EVERY house, where the old text said "all of the Codex weekly allowance used".
- D3 — missing half. His brief asked him to "Rule what the hub seat actually requires … and what the fallback is when it cannot" (`PROJECT-LEDGER.md:1326`). The proposal offers keep/retire only. The hub-trial PASS bar (X5 shape) is his.
- His numbers: the class-level n (T8); what match rate means "predicts" (T6); the FIX baseline for trigger (c).
- RE-OPENS A RULING (R46): the model ids in L67's 2026-09-21 amendment (g).
- L33: whether the Sol writer profile ("network on", "never `danger-full-access`", "cannot commit") is re-housed in L33 or stays in L29. Without one of the two, it is dropped.

## WRONG FACTS

- `ROUTING-PROPOSAL-2026-09-22.md:150`, `:183` ("production deploy hub, no write path … 4 × DEPLOY DONE"; "S, no write path") vs `deploy-2026-09-22.md:80` (dev `db migrate`) and `05-stacked-deploy.md:1`, `:6` ("ONE WRITE this run does make is the WITH-DB suite"; `--permission-mode auto`).
- `ROUTING-PROPOSAL-2026-09-22.md:38`, `:57`, `:66`, `:138`, `:140` cite L31 for "no vendor/model name in law text" vs `LAWS.md:181` (L31 lists code identifiers, schema, config keys, enum values, system design docs). L67 names houses and `gpt-5.6-sol` in current law (`LAWS.md:365`, `:370`).
- `ROUTING-PROPOSAL-2026-09-22.md:149`, `:184` (six STOPs, "LEDGER:1325") vs `PROJECT-LEDGER.md:1326` ("Sonnet did exactly that six times on 09-13"). :1325 gives no model.
- `ROUTING-PROPOSAL-2026-09-22.md:115` (Sol writer profile "→ L33 as its writer launcher profile") vs `LAWS.md:192-193`: L33 carries none of "network on", "never `danger-full-access`", "cannot commit".

## READING

- `prompts/2026-09-22/64-routing-tribunal-fable-seat.md` (whole); `63-routing-tribunal.md:31-42` (question paragraph through `TRIBUNAL R1:`; lines 43-44 seen in the same read, not used)
- `LAWS.md` :1-442 (full)
- `30 - Design/ROUTING-PROPOSAL-2026-09-22.md` :1-245 (full); `reports/routing-propose-2026-09-22.md` :1-40 (full)
- `reports/cto-2026-09-22.md` rows R4 :15, R109 :36, R81 :65, R76 :70, R74 :72, R73 :73, R36 :110, R32 :111, R30 :113, R13 :130; `cto-2026-09-21.md` R46 :57, R49 :60
- `LAWS-HISTORY.md` :27-72; `50 - Roles/MODELS.md` (whole); `areas/cobalt-houses.md` :19-68
- `PROJECT-LEDGER.md` :615-632, :900-912, :1140-1144, :1323-1326
- `configs/cobalt/seat_usage.yaml` :40-84; `reports/seat-usage.md` :1-50 + a model-row grep (mainframe / terra / haiku / astra, all days)
- `TRIAGE.md` :43, :124-125; `laws-audit-2026-09-20.md` :264-285, :380-399, :477-491 + a heading grep
- `10 - Decisions/` ls; ADR-0008 grep `bake|task class|local adapter`; folder grep `bake-off`; `git log -S"bake-off"` on the folder
- `src/cobalt` grep for model-call strings; `--model` grep over `prompts/2026-09-20`, `-21`, `-22` (the 09-21/22 output saved by the harness, grepped for deploy/stack lines)
- deploy stop lines: `deploy-2026-09-21.md`, `-21b`, `-21h`, `-22.md:212`; `deploy-2026-09-22.md` grep (`db migrate` :80, model :9); `deploy-2026-09-21b.md` grep (:4); `11-panel-order-deploy.md:1` grep; `05-stacked-deploy.md` :1, :6 greps; `27`/`31`/`48` :1 greps; `db migrate` grep over 09-21 reports and 09-22 prompts
- `day-open-2026-09-20.md:169`, `-21.md:174`, `-22.md:175` (verdict greps)
- `bars-chunk-1a-check-2026-09-20.md` grep (HOLD rows :6-7, :73-78, :136-138, :170-197, :204, :222, :227)
- `claude-opus-5-5` count grep over five 09-22 check/fix reports
- `ls "docs/40 - DevDocs/reports"` (directory listing; the forbidden hub report was not present in it and was not opened)
- Authorization greps / git logs as listed under CONTINUE; the self-attack greps as listed above
- NOT opened: `scratch/tribunal-bars-0920/routing-tribunal/` (any depth), `reports/routing-tribunal-2026-09-22.md`, `reports/routing-tribunal-draft-2026-09-22.md`, any house's ruling

## ESCALATE

1. **L31's reach.** This prompt's index card reads L31 as "no vendor or model name in law text". `LAWS.md:181` does not list law text, and L67 carries names (`LAWS.md:365`, `:370`). The desk should say which reading the derive (`65`) uses. This seat used the file.
2. **L29.6 vs today's launches.** Builds `27`/`31` (Opus 5.5) and deploy `05` (Sonnet 5) ran `COBALT_ENV=dev uv run cobalt db migrate` under `--permission-mode auto`. Read literally, the current L29 ("migration … never auto mode on a write path", `LAWS.md:169`) forbids that, and it was never ruled otherwise (C5 open, `LAWS.md:344`, `:350`). This is not a defect claim (L70). It is a live law-vs-practice gap for his plate, independent of this tribunal's timing.

## CONTINUE

AUTHORIZATION: PASS — FABLE ROW unfilled-count 0 → R109; `cto-2026-09-22.md:36` carries all four literals; committed `75b2aa57`; seat model `claude-opus-5-5` = this session's id; R76 :70 "You ask me"; R81 :65 "ROUTING TRIBUNAL RUNS THIS WEEK"; R4 :15 "Laws are all mine"; R46 `cto-2026-09-21.md:57` carries the design-seat sentence; proposal committed `1bcc1a89`; stop line committed `1bcc1a89`; ten launch strings each count 1 in `22-draft-setups-tribunal.md`.
next: none — run complete.

ROUTING TRIBUNAL FABLE R1 DONE · verdict: ADOPT AFTER write-path scope ruled, bare § refs fixed, L33 profile carried, T6 run blind · adopt: 4 · adopt with wording: 16 · reject: 0 · self-assignments: 4 · ESCALATE: 2
