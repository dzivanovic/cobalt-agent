# Open items — 2026-09-23 (all of them, one recommendation each)

Drafter `open-items-draft-0923` (Opus 5.5, `claude-opus-5-5`), prompt `prompts/2026-09-23/10-draft-open-items.md`, under his 09-23 R8 ("approved, and show all 36 here as well") and R7 (routing items come now; Astra's Saturday read is an after-check). Written 06:45 ET (`date`). Read-only run: this file is the only write.

## §0 Headline
- **37 items:** DRC 5 · SMOKE 2 · VOICE 12 · ROUTING 18. DRC has 5, not 4: the source's ESC 5 is also marked "his to veto" (ESCALATE 1).
- **Already ruled: 1.** This is VOICE item 12 (W5, scope), ruled by 09-22 R100.
- **You answer 36.** Reply "approved" plus the numbers you want changed, e.g. "approved, 9 B, 30 A".
- None of these blocks today's deploy (R4). Routing recommendations come from the same house that proposed and derived the design (ESCALATE 4).

## DRC (source: `reports/drc-reissue-draft-2026-09-22.md`)

1. **Playbook names that differ only by upper or lower case.** Source: "case in the one-to-one rule (R116). `50` D3-2b is built as EXACT, case-sensitive equality after the strip". Question: if a TradeZella name matches a strategy note title except for case, is it a match? — A: no. Only an exact match counts, and anything else shows `unmapped: <name>` (as built) · B: yes, case is ignored. — REC: A. You are renaming the names one-to-one anyway (R116, R117), and a miss shows up loudly as `unmapped`, never as a silent wrong match. (source: `drc-reissue-draft-2026-09-22.md:53`)

2. **Files you drop into the folder by hand.** Source: "Hand-dropped files are not imported. … a file placed in `_imports/drc/<date>/` by hand is never imported and never builds a DRC." Question: should Cobalt import files you put in the day's folder yourself? — A: yes. Cobalt reads `_imports/drc/<date>/` through the same header check, and the `/drc` upload saves into that same folder, so there is one parser and one place (L3) · B: no. Only files uploaded through the `/drc` page import. — REC: A. Dropping files by hand is how you deliver them today (R114), and under B that day never gets a DRC. A is a new entry path, so it needs its own build row and a check (L67). (source: `drc-reissue-draft-2026-09-22.md:54`)

3. **Which day the DAS log belongs to.** Source: "E1's trading log has no date and no zone. `Time` is `HH:MM:SS` only." Question: where does the date of the DAS rows come from? — A: from the folder or upload they arrived in (`_imports/drc/<date>/`) · B: the import FAILs until the log carries a date. — REC: A. The DAS export never carries a date, so B would fail every day. The folder date is the one you set. (source: `drc-reissue-draft-2026-09-22.md:55`)

4. **No stop price in the logs.** Source: "E1 has no stop-PRICE column. It carries `Trade Risk` (dollars) … A stop derived from `Trade Risk` ÷ shares would be a computation, so it needs a ruling; otherwise the stop renders `not given`." — A: the stop shows `not given` · B: Cobalt computes a stop price from `Trade Risk` ÷ shares and stores it with its inputs (L57). — REC: A. On a trade with several entries (your usual case, R114), risk ÷ shares gives a wrong price, and no value is invented (L1). If you want real stops, a stop column in the TradeZella export is the clean source. (source: `drc-reissue-draft-2026-09-22.md:56`)

5. **A file with only some of the expected columns.** Source: "some but not all of a kind's required names, and no kind complete → degraded, not parsed … if the vendor drops a column, the file degrades until the parser is changed". — A: the file is marked degraded and not read until the parser is fixed (the desk's reading) · B: Cobalt reads whatever columns are there. — REC: A. A vendor format change then fails loudly before it reaches your DRC (L1, L45). B would build a DRC from a partial file without telling you. (source: `drc-reissue-draft-2026-09-22.md:57`)

## SMOKE (source: `reports/s2-smoke-fixes-draft-2026-09-22.md`)

6. **The two nights with no missed-movers line (09-21, 09-22).** Source: "The replay died before writing them, and they cannot be rebuilt: the rebuild needs both of that day's mover files, and neither night saved both. This does NOT block closing S2". — A: accept the two nights as recorded gaps · B: ask for a design that can rebuild a lost night from another source (its own design lane and tribunal, after S2 closes). — REC: A. The data to rebuild them does not exist, and tonight's check reads tonight's note. B is a whole design lane spent to recover two nights. (source: `s2-smoke-fixes-draft-2026-09-22.md:60`)

7. **Five working files in `docs/_inflight/`.** Source: "The rules say that folder holds only its README, so `cobalt validate` — one of the S2 checks — fails. Live builds read those files where they are." — A: leave them for now, run tonight's smoke check with the rule's own "deliberate in-flight window" switch on, and move them at tonight's close · B: move them into their proper folders now and re-point the prompts that read them. — REC: A. Nothing that is running breaks. Under B, a build running today can fail on a missing file. The switch belongs to the placement rule, so no law step is skipped. (source: `s2-smoke-fixes-draft-2026-09-22.md:61`)

## VOICE (source: `reports/voice-tribunal-derive-2026-09-22.md`, `## FOR DEJAN`, quoted)

8. **W1: where you record.** "A (v2 default): a mic button on each filled/closed card on your phone or desk during the day, AND on each trade row of `/drc` at the DRC. B: only on the `/drc` trade row, at the DRC." — REC: A. You can capture a thought while the trade is fresh, and the DRC row is still there in the evening. (source: `voice-tribunal-derive-2026-09-22.md:102`)

9. **W2: is the audio kept.** "A (v2 default): kept as long as its transcript, so any block can be re-played and re-transcribed. B: deleted once the text lands in your note." — REC: A. B breaks "every number/value replayable" (L57), and a bad transcript could never be redone. (source: `voice-tribunal-derive-2026-09-22.md:104`)

10. **W3: where the audio lives.** "A (v2 default): in your vault next to the day's imports (`1 - Trading/5 - Review/_imports/drc/<date>/`), synced to every device. B: a folder on the Mac only, not synced." — REC: A. It is the import home you ruled (R92), and your phone can replay it. The size per minute is still unmeasured (X12), so revisit if sync gets heavy. (source: `voice-tribunal-derive-2026-09-22.md:106`)

11. **W4: when local speech-to-text is down.** "A (v2 default): a red "transcript pending — local speech-to-text down" on the card / `/drc` row, audio kept, a retry button; you can type meanwhile. B: your audio is sent to a named cloud speech service instead." — REC: A. Local first with a loud degraded state (L23, L9), no audio leaves the Mac, and no new paid lane opens. (source: `voice-tribunal-derive-2026-09-22.md:108`)

12. **W5: what voice covers.** "A (v2 default): per-trade answers only. B: also your per-day block and next-day review grade in the same build." — **ALREADY RULED 09-22 R100**: "A, B as soon as possible." → "a per-trade VOICE CAPTURE becomes its own design item NOW". Per-trade is the ruled scope. The per-day question is item 16 (W9). Not counted. (source: `voice-tribunal-derive-2026-09-22.md:110`)

13. **W6: how the phone records.** "A: the ASET page is served over HTTPS on your tailnet, and you record inside the page. B (v2 builds first): tap record → your phone's recorder app opens → the file uploads to the page; no change to how the page is exposed. V-E1 tests both on your phone before you choose." — REC: B first. It changes nothing about how the page is exposed. Pick A later only if the V-E1 test on your phone shows it is clearly better. (source: `voice-tribunal-derive-2026-09-22.md:112`)

14. **W7: limits on a clip** (max upload size, max clip length, how long a transcription may run). "A (v2 default, grok): until you set a size, an upload FAILs rather than guessing; the time limit is an engine setting. B (Fable seat): all three are yours; until set, uploads are unbounded, no clip limit, the time limit fails loud." — REC: A. It fails loudly instead of running unbounded (L1), and the numbers stay yours (L53). Under A, voice uploads refuse until you give a size, so you can add one to your reply (e.g. "14 A, 25 MB, 3 min"). (source: `voice-tribunal-derive-2026-09-22.md:114`)

15. **W8: the vocabulary hint** (the day's tickers plus your exit-structure words, given to the engine so it spells them right). "A (v2 default): on, from config, stored with each transcript; turned off if X6 shows it inserts words you did not say. B (Fable seat): off until X6 passes; your structure list lives in your settings, never in a committed file." — REC: B. Your structure words are your data and stay out of the repo (L32). A hint that could put words in your mouth stays off until the test proves it does not. (source: `voice-tribunal-derive-2026-09-22.md:116`)

16. **W9: voice on a no-trade day.** "A (v2 default): not in this build; you type your "why no trades" as today. B (Fable seat): a later slice records into the "Why no trades today" unit your R93 DRC already creates." — REC: B. It costs nothing now, the unit already exists (R93), and your R100 said voice "as soon as possible". (source: `voice-tribunal-derive-2026-09-22.md:118`)

17. **W10: the database row of each clip** (text, engine, timings). "A (v2 default): kept, no pruning. B (Gemini): a pruning schedule you set." — REC: A. The rows are small text, and keeping them keeps every block replayable (L57). A pruning rule can come later if they ever grow. (source: `voice-tribunal-derive-2026-09-22.md:120`)

18. **W11: who can reach the record button.** "A (v2 default; grok, Fable seat): whoever can reach the ASET page today — same as `/size` and `/fill`, until the access-token backlog item ships. B (Gemini): the voice upload only answers devices on your tailnet; a LAN-only browser is refused." — REC: A. Your trading PC is deliberately off the tailnet, so B would refuse the desk browser. The access-token item closes the gap for every page at once. (source: `voice-tribunal-derive-2026-09-22.md:122`)

19. **W12: test files.** "A (v2 default; proposal, grok): tests use your real clips' shape, stripped of what you name. B (Fable seat): no recording of your voice ever enters git; tests use synthetic sound in the phone's real file format, your clips stay on the Mac." — REC: B. A voice cannot be stripped of whose voice it is, and B still tests against the real file shape (L45) while keeping your data out of the repo (L32). (source: `voice-tribunal-derive-2026-09-22.md:124`)

## ROUTING (source: `reports/routing-tribunal-derive-2026-09-22.md`, `## FOR DEJAN`, quoted; context `30 - Design/ROUTING-v2-2026-09-22.md`)

20. **D1: production write paths.** "When a build or deploy touches the live vault, the production DB, or an `--allow-prod` migration, does it always run on the house's top model?" — A: "yes, until you rule otherwise; no trial earns it down (v2's L29, Grok's wording)" · B: "a lower model that passed a dev shadow build may run it (the proposal's D1-B)". — REC: A. It is L29's floor as in force today, and no trial has yet measured a lower model on a write path. Revisit when X1's numbers exist. (source: `routing-tribunal-derive-2026-09-22.md:175`)

21. **Write-path scope.** "A deploy hub on Sonnet ran a `cobalt_dev` migration in auto mode on 09-22." — A: "that is a write path, so today's launch shape is outside the law (v2 as written)" · B: "dev-only migrations and with-DB suites are scoped differently (the Anthropic seat, audit C5)". — REC: A. L29 lists "migration" with no dev exception, so A is the law as written. Today's deploy `07` already runs on Opus with `acceptEdits`, so A holds up nothing today (ESCALATE 6). (source: `routing-tribunal-derive-2026-09-22.md:179`)

22. **D2: a spent meter.** "When Codex runs out mid-week, what does the law say about that house?" — A: "every house's allowance is planned in the seat table, and a bound meter moves the seat to its row's fallback (the proposal)" · B: "keep "Codex is the overflow valve … most of it on Astra"". — REC: B for now. Grok says A conflicts with L47 (the meter is a precondition, not a router), and the sentence names the OpenAI house's role, which that house has not read yet (Astra, Sat). Re-ask after Astra's read if it favours A. (source: `routing-tribunal-derive-2026-09-22.md:182`)

23. **D3: the local model as Cobalt's hub.** — A: "keep it as the plan, gated on a measured hub trial" · B: "retire it; local stays on the morning check only (the proposal)". — REC: A. Local-first (L23) and "re-tested as local models improve" (L26) both argue for keeping the door open, and the gate costs nothing until a trial is run. (source: `routing-tribunal-derive-2026-09-22.md:186`)

24. **n for a PASS.** "How many shadow builds make a model "pass" a class?" — A: "unset — every trial reads "spot check, n = 1"" · B: "you set a number. Gemini offered 3 as a pointer." — REC: B, at 3, tunable later. Left unset, no model can ever pass a class, so the trials can never conclude. (source: `routing-tribunal-derive-2026-09-22.md:189`)

25. **What counts against a candidate in a shadow build.** — A: "the checkers' HOLD count (Grok)" · B: "FIX rows only, because some HOLDs confirm the build is right (the Anthropic seat; true of rows 5, 6 and 25 in the 09-20 chunk 1a check)". — REC: B. FIX is the class L75 builds from, and counting HOLDs that confirm a build is right would count correct work as a defect. (source: `routing-tribunal-derive-2026-09-22.md:192`)

26. **Who grades the S/H key against past builds.** — A: ""a hub job" (the proposal)" · B: "a house other than the proposer, classing blind from prompts first (the Anthropic seat)". — REC: B. The proposer grading its own key is a self-check, and L67's floor (never fewer than one other house) plus L26's conflict-of-interest rule point the same way. (source: `routing-tribunal-derive-2026-09-22.md:195`)

27. **Trigger (c) baseline.** — A: "unset" · B: "you set the defect baseline per seat". — REC: A for now. There is no measured defect rate per seat to set it from yet. Set it after the first trials give numbers ("see before you rule", 09-21 R18). (source: `routing-tribunal-derive-2026-09-22.md:198`)

28. **Cross-house seats.** — A: "L25's "cross-house seats NOT load-bearing" stays as written beside L67 (v2)" · B: "it is retired, since L67 made Grok, Gemini and OpenAI seats standing (raised by Grok)". — REC: B. Under L67 no build deploys without three checkers, so those seats already carry load. L25 itself says that status is "earnable later by explicit ruling", and L67 was that ruling. (source: `routing-tribunal-derive-2026-09-22.md:201`)

29. **Vendor names in law text.** — A: "L22 and L25 keep "Max", "Anthropic API" and "Claude →" (v2; L31 lists no law text)" · B: "substitute house-neutral words (the proposal; Grok and Gemini adopted it)". — REC: B. Two other houses adopted it, and a law that routes "Claude →" first is exactly the conflict of interest L26 says to neutralise. The ground is L26, not L31. (source: `routing-tribunal-derive-2026-09-22.md:204`)

30. **L26 wording.** — A: "the proposal's, which the desk cannot fold as written because of its bare §4 / §5" · B: "the Anthropic seat's, which inlines the triggers and uses FIX rows (tied to item 6)". — REC: B. A cannot be folded (LAWS.md "How to read" refuses a bare §), and B matches item 25's FIX-row rec. (source: `routing-tribunal-derive-2026-09-22.md:207`)

31. **Before `seats.yaml` exists, where does a launch read its seat?** — A: ""source pending" (v2)" · B: "the desk-report §4 ruling cited in the launch prompt (the Anthropic seat)". — REC: B. It is what launches already do (e.g. 09-22 R109), and it gives every launch a ruling it can check (L35). "Source pending" gives it nothing. (source: `routing-tribunal-derive-2026-09-22.md:210`)

32. **OpenAI writer profile** (workspace-write, network on, cannot commit). — A: "it stays in L29 (v2)" · B: "it moves into L33 (the Anthropic seat named this option). ASTRA PENDING." — REC: A. It changes the least law text, and the house it describes has not read it yet (Astra, Sat). (source: `routing-tribunal-derive-2026-09-22.md:213`)

33. **L67's model ids ("Sol", "Opus 5") — RE-OPENS R46.** — A: "L67 is untouched and the table records the ids" · B: "you re-rule L67 without ids". — REC: A. L67's ids are your in-force 09-21 R46 ruling, and the desk does not ask you to re-decide a law in force (L73). B stays open to you as an override whenever you want it. (source: `routing-tribunal-derive-2026-09-22.md:216`)

34. **"Blind code seat" for Grok.** — A: "not in the table (v2)" · B: "you seat it by ruling". — REC: A. The blind-code runs so far were one-off launches on your per-case approvals (09-22 R23, 09-23 R4/R9). A standing seat would be a house proposing itself with no measurement behind it (L26). (source: `routing-tribunal-derive-2026-09-22.md:219`)

35. **T12 ops owners.** — A: "none named (v2)" · B: "you name them". — REC: B, name the desk as owner. It puts each item on the plate with its next step. An item with no owner never moves (L25: "a fix ticket with an owner"). (source: `routing-tribunal-derive-2026-09-22.md:222`)

36. **What is class S** (the lower-tier-eligible work)? — A: "the proposal's §4 description" · B: "the prompt names an existing artifact and a test a wrong guess fails (Grok, the Anthropic seat)". — REC: B. Two houses agree, and it can be checked before launch (L45: the real artifact plus a test). A is a description a checker cannot verify. (source: `routing-tribunal-derive-2026-09-22.md:225`)

37. **L23 wording.** — A: "one sentence changes: "first candidate ASSESSED" (v2)" · B: "Grok's paragraph, which also says "local trumps cloud" is a reason, not a route". — REC: A. It changes the least frozen law text, the way the derive carries every wording split (L39). Grok's point is already served by the seat table's local rows. (source: `routing-tribunal-derive-2026-09-22.md:228`)

## ESCALATE
1. **DRC count is 5, not the plate's 4.** Item 5 is the source's ESC 5, which the source marks "his to veto". The other DRC ESCALATEs are not his to rule. ESC 6 (the comma split in playbook names; none of the 22 titles has a comma) is an engineering note. ESC 7 is recorded once in the source and never raised (L74). ESC 8 is the drafter's own process record.
2. **The smoke source's ESCALATE 1–4 are desk items, not his.** They are: the smoke look starts ≥21:40 ET; the `since` date correction; K3's STEP-D, already proven `ranked_without_metric 0` in 09-23 R2; and the replay's first live run past movers.
3. **Voice items that are not his:**
   - R2-V1 and R2-V5 are round-2 tribunal questions.
   - ESC 3–9 are seam-document items, owed before D2 or V2 launches (L72).
   - ESC 10–11 are desk record items.
   - ESC 12 is Astra's Saturday read.
4. **Routing recommendations and conflict of interest.** Items 20–37 were drafted by an Anthropic-house seat. The same house proposed and derived the routing design. The derive gave no recommendation and cited L37. L37 governs approvals, not recommendations, and his R8 ordered one recommendation per item. So each rec names the non-Anthropic house position where one exists, and three recs (25, 30, 31) back the Anthropic seat's own option. Astra reads the FINAL Saturday as an after-check (R7), and anything it raises comes back to him as a new item. Items 22, 32 and 33 name the OpenAI house.
5. **Item 33** recommends A because B would re-decide his in-force R46 (L73). Asking it at all is lawful only as the routing tribunal's own open item.
6. **Item 21, checked today:** `prompts/2026-09-23/07-stacked-deploy.md` line 1 runs on Opus 5.5 with `--permission-mode acceptEdits` for its write path, so rec A does not stop today's deploy. The 09-22 `05` Sonnet/auto dev migrate stays a record item, not a defect claim (L70).
7. **Item 14:** under rec A, voice uploads refuse until he gives a size. That is a later build, not today's.
8. **L74:** this session's system reminder carried a `Claude-Session:` commit line and named a file-send tool. I committed nothing and sent nothing. Recorded once.

OPEN ITEMS DRAFTED · items: 37 · already ruled: 1 · to answer: 36 · ESCALATE: 8
