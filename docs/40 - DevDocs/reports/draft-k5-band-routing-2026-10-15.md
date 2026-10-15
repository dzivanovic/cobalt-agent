# Drafter report — K5 band and builder routing card, 2026-10-15

## §0 Headline
- Card written: `prompts/2026-10-15/583-band-routing-card.md` (K5, `OFF-LADDER` R1532, `BASE` and `TIP` empty); rows B1 `CARD.md` `BAND:`, B2 `SHADOW-HUB.md` table and ledger rule, B3 launcher routing, B4 `BUILD-HUB.md` sentence, R3 RUN.
- Existing path to a non-Opus builder is the shadow gate seat only; B3 routes `LOW`/`MID` into it (`--routed`). That is decision 1.
- No overlap with cards 546, 549, 550 or 580 by line range; 550's fix round has no card to compare (decision 9).
- Nothing was run but reads and greps; every RED is UNPROVEN until the builder quotes it.

## DECISIONS
1. ASK DESK: how does a `LOW`/`MID` card reach Grok? `BUILD-HUB.md:12` has no `<model>` token (its `--model claude-opus-5-5` is a literal, pinned whole by `test_shadow_hub_file.py:112-119`); `<model>` (`desk-launch.sh:2233`) is filled only for kind `shadow`, whose gate seat runs the builder as a command. Default taken: `build <card>` on a `LOW`/`MID` card re-enters as `shadow <card> --model <id> --routed` (precedent `recut`, `:2214`); `--routed` alone skips three shadow refusals (`SHADOW OF`, `shadow/` branch, JOB slug); every other shadow refusal stands. [09:50 ET]
2. ASK DESK: what is a "new card" for the refusal of a missing `BAND`? Default taken: a card whose folder date is 2026-10-16 or later (`BAND_FROM`); older cards and every existing test fixture (`prompts/2026-01-02/`) launch as today. R1532 gives no date. [09:50 ET]
3. ASK DESK: a resume step or `PASS-2` on a routed card, and Terra as backup. Default taken: a routed `LOW`/`MID` launch is fresh only (`REFUSED`), no automatic Grok-to-Terra fallback; the backup is the desk's hand launch `shadow <card> --model gpt-5.6-terra --routed`. [09:50 ET]
4. ASK DESK: "HIGH Opus, Grok when I say so". Default taken: no mechanism; HIGH always builds on the `BUILD-HUB.md` line, and a Grok build of a HIGH card is a hand `shadow` launch the desk types on his word. [09:50 ET]
5. ASK DESK: the check and stop line of a routed build. `SHADOW-HUB.md`'s procedure and `SHADOW BUILT` stop line, and the check arm's reading of shadow cards (`desk-launch.sh:1722-1729`, a `SHADOW OF:` and `shadow/` branch), are not changed. Default taken: the first routed card proves what the check launch needs (L81 (3)); a routed card has no `SHADOW OF:`, so its check is the normal Opus check (condition 1). [09:50 ET]
6. ASK DESK: "Sonnet routing for now". Default taken: a table row in `SHADOW-HUB.md` `BAND ROUTING` only; no launcher change. [09:50 ET]
7. ASK DESK: the results ledger's home (condition 4). Default taken: B2 rewrites one sentence of `## RESULTS TABLE` (every finished non-Opus card adds a row; re-grade at n = 10 per model per band or after two BELOW in a row); the file stays the desk's `reports/complexity-shadow-results-…` and is filled by hand; no script. [09:50 ET]
8. ASK DESK: `BUILD-HUB.md:3` (`MODEL: Opus 5.5`) and `:17` (`L29 Opus, dontAsk`). Default taken: both stand; B4 adds one new paragraph saying the line below is the HIGH builder's, LOW/MID go to the gate seat. `LAWS.md` L29 already carries the LOW/MID amendment. [09:50 ET]
9. ASK DESK: card 550's fix round `card-template-1014-fr1` (FR-O1, FR-O2, FR-G2, FR-G3, R1548) has no card text; its `CARD.md` lines are UNPROVEN against B1's row after `:22` and paragraph at `:29-31`. Default taken: the desk compares before the launch; B1 finds its lines by content. [09:50 ET]
10. ASK DESK: wording not traced to R1532 or the routing answer: the stderr lines `BAND: <band> → …`, the refusal texts, and the `--routed` flag name are mine. Default taken: kept as written; the builder changes a text only on the desk's word. [09:50 ET]

## RECORDS
- `date` 2026-10-15 09:45 ET at the first write; `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `3acc5dd6`.
- `git -C /Users/cobalt/cobalt diff HEAD --stat -- CARD.md SHADOW-HUB.md BUILD-HUB.md ops/desk/desk-launch.sh ops/desk/desk-watch.sh ops/desk/stop-guard.py` (prompts under `docs/40 - DevDocs/prompts/`) printed nothing: the working tree equals HEAD for them; every `file:line` in the card was read on that tree.
- `grep -c -F "BAND"` → `0` on `CARD.md`, `BUILD-HUB.md` and `desk-launch.sh`; `grep -c -F "BAND ROUTING"` → `0` on `SHADOW-HUB.md`; `ls tests/ops/test_band_routing_1015.py` → no such file (the card's `## DEPLOY PROOF` before-values).
- Read whole or in the ranges the card's `## READ` names: `prompts/CARD.md`, `580-close-automation-card.md`, `549-desk-installs-card.md`, `550-card-template-card.md`, `routing-table-answer-2026-10-14.md`, `cto-2026-10-15-words.md` R1532, `cto-2026-10-15.md` rows R1532, R1536, R1542, R1545-R1551, `LAWS.md` L27, L29, L81, `writing-rules.md`; `SHADOW-HUB.md` `:1-30`, `:72-103`; `BUILD-HUB.md` `:1-20`; `desk-launch.sh` `:359-425`, `:948-1049`, `:1540-1730`, `:2205-2304`; `test_shadow_hub_file.py` `:55-259`, `test_build_hub_no_clutter.py` whole, `test_hub_lines.py` `:54-163`, `test_desk_launch_shadow.py` `:38-172`.
- Line range of card 580's launcher block: `:2294-2296`; B3's lines: `:384-392`, after `tree_state()` (`:1043-1049`) and before `merges=""` (`:1630`), `:1658`, `:1661-1664`, `:1675-1681`. No overlap; proved by range, not by running.
- Cards 547 and 548 are on `main` (`desk-launch.sh:1087`, `BUILD-HUB.md:83`, `:109`). Pins found by content: `test_shadow_hub_file.py:62-69`, `:122-127`, `:217-219`; `test_build_hub_no_clutter.py:51-54`, `:88-100`.
- No command beyond the allow line was run; no git write; nothing launched.

DRAFTED · decisions: 10
