JOB: hub-deferred-1018
LADDER: OFF-LADDER — reports/draft-cos-outage-2026-10-18.md DECISION 1 2026-10-18 R1863
CLASS: K5
INSTALL: none
BRANCH: ops/hub-deferred-1018
WORKTREE: hub-deferred-1018
BASE: 170e90ca
TIP:
REPORT: /Users/cobalt/cobalt-wt/hub-deferred-1018/docs/40 - DevDocs/reports/hub-deferred-1018-build-2026-10-18.md
CHECK REPORT:
HOUSE B:
BAND: HIGH
DB: none
RESTARTS: none
RULINGS: 2026-10-18 R1863

## ROWS

Scope: one fixed hub file, `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (cited below as `DEPLOY-HUB.md`), and one new test file (brain L79; `reports/draft-cos-outage-2026-10-18.md` DECISION 1; `reports/f20-fix-preflight-2026-10-18.md` note 5). Card 730 ships `BOOTSTRAP: deferred com.cobalt.cos` and its RESTARTS holds `com.cobalt.agent com.cobalt.aset com.cobalt.cos com.cobalt.radar` (`730-f20-card.md:13-14`); today `DEPLOY-HUB.md:93` refuses that set. Every `file:line` below was read with `git show main:docs/40 - DevDocs/prompts/DEPLOY-HUB.md` at the drafting (`## RECORDS`); re-find each place by content before the edit (BUILD-HUB E3). The hub names neither `ops/desk/deploy-step0.sh` nor `ops/desk/deploy-outage.sh` (it types STEP-4 and STEP-5 itself); neither script changes. The changed `DEPLOY-HUB.md` is read by one other house before its deploy (L9, L67), and its deploy runs the gate on the merged hub text first (L68). Tests read the real hub text, in the form of `tests/ops/test_hub_text_1013.py` (each test pins only the lines its row changes, found by their own text; no whole-line pin, no BASE hash).

| row | what | red first | files |
|---|---|---|---|
| D1 | STEP-R's set check reads the restart set MINUS every label the card ships `deferred`. THE EDIT, three places: (a) `:5`, the names list: after `a \`deferred\` label is not in it; none → empty)` insert `, \`<deferred set>\` (the labels STEP-C admits \`· deferred\`: merged, not loaded, never in \`<restart set>\` and never named by a \`launchctl\` call of this file; none → empty)`; (b) `:89`, STEP-C: after `is \`<launchd set>\`, with its mode, named beside \`<restart set>\`` insert `; each \`ADMITTED:\` label marked \`· deferred\` is \`<deferred set>\`` (the script's line `ADMITTED: com.cobalt.<label> · add · deferred`, `ops/desk/deploy-step-c.sh:285-286`); (c) `:93`, the GATE: `and the \`RESTARTS:\` set within \`com.cobalt.agent com.cobalt.aset com.cobalt.radar\`` reads `and the \`RESTARTS:\` set, minus every label of \`<deferred set>\` (a label the card ships \`deferred\` merges unloaded: nothing restarts it), within \`com.cobalt.agent com.cobalt.aset com.cobalt.radar\``, and the line's `→ \`<restart set>\`` reads `→ \`<restart set>\`; write \`<deferred set>\` under \`## RESTARTS\` beside it`. The three names, the parenthesis `(one, two, all three, or none)` and the whole `Anything else (…)` sentence stand byte for byte: a label outside the three that is not deferred is still refused. No `launchctl` string is added to the launch line `:11` | NEW file `tests/ops/test_hub_deferred_1018.py`, helper `rule()` reading the STEP-R line that starts `- GATE: exit 0` (one line): `three` = the backticked span after `within ` (asserted exactly `com.cobalt.agent com.cobalt.aset com.cobalt.radar`), `minus` = the line holds `minus every label of \`<deferred set>\``; `admits(s, d)` = `(s - d if minus else s) <= three`. NEW `test_d1_card_730s_set_is_admitted`: `admits({agent, aset, cos, radar}, {cos})` is True. RED on BASE: False (no `minus` clause). CONTROL (green on BASE and after): `test_d1_a_label_outside_the_three_not_deferred_is_refused`: `admits({agent, aset, cos, radar}, set())` False, `admits({aset, "com.cobalt.herdr"}, {cos})` False, and the line still holds `Anything else (an \`UNCLASSIFIED\` row, \`com.cobalt.herdr\` / \`com.cobalt.mainframe\` / \`com.cobalt.obsidian\`, a non-zero exit)` | `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (`:5`, `:89`, `:93`), `tests/ops/test_hub_deferred_1018.py` |
| D2 | No `launchctl` call of the hub ever names a deferred label, said where each call takes its labels. THE EDIT, two places: (a) `:94`, THE SET DRIVES THE REST, after `Never copy an expectation from an earlier deploy.` append `A label of \`<deferred set>\` is never in \`<restart set>\` or \`<launchd set>\`, so no \`launchctl\` call of this file names it: P8 and D1 print \`com.cobalt.aset\` and \`com.cobalt.radar\` by name; 4.2, 4.6, STEP-5 (1), (3) and smoke (a) take their labels from \`<restart set>\`; D1's THE LAUNCHD SET, 4.6L and STEP-5 (1L), (2L) from \`<launchd set>\`; 4.6L-BO from a later bootstrap-only card's \`add\` line.` (the call sites at BASE: P8 `:65`, D1 `:122`, `:125`, 4.2 `:139`, 4.6 `:143`, 4.6L `:144`, 4.6L-BO `:145`, smoke (a) `:149`, STEP-5 (1) `:162`, (1L) `:163`, (2L) `:165`, (3) `:168`); (b) `:154`, smoke (f): `\`RESTARTS:\` = STEP-R's \`<restart set>\`` reads `\`RESTARTS:\` minus \`<deferred set>\` (as \`## RESTARTS\` records it) = STEP-R's \`<restart set>\`` (the tool prints the deferred label again after the merge; STEP-5 (4) `:169` re-runs (f) and inherits it). The MODEL line `:3` (`NO \`launchctl\` on any label but … and the labels of \`<launchd set>\``) stands: a deferred label is neither | In the same file: NEW `test_d2_the_deferred_set_is_named_where_it_is_made_and_read`: the line starting `This file is the same for every deploy` holds `<deferred set>` once; the STEP-C section's line holds `is \`<deferred set>\``; the line starting `- THE SET DRIVES THE REST` holds `A label of \`<deferred set>\` is never in \`<restart set>\` or \`<launchd set>\`` and each of `from \`<restart set>\``, `from \`<launchd set>\``; the line starting `- (f) \`COBALT_ENV=production uv run cobalt validate\`` holds `\`RESTARTS:\` minus \`<deferred set>\``. RED on BASE: the first assert (count 0). NEW `test_d2_no_launchctl_call_names_the_deferred_set`: no hub line holding `launchctl bootout`, `launchctl bootstrap`, `launchctl kickstart` or `launchctl print` holds `<deferred set>`, and exactly 5 lines hold `<deferred set>`. RED on BASE: 0 lines. CONTROL 2 (green on BASE and after): `test_d2_the_three_residents_strings_stand`: the `claude --bg ` line holds `<launchd strings>` once and each of the six strings `launchctl bootout gui/501/com.cobalt.aset`, `…/com.cobalt.radar`, `launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist`, `launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist`, `launchctl kickstart -k gui/501/com.cobalt.aset`, `…/com.cobalt.radar` once, and no `com.cobalt.cos`; the MODEL line holds `the labels of \`<launchd set>\`` and no `<deferred set>`. The builder runs both CONTROLs on BASE first and quotes them green. Quote whole: `uv run pytest -q -p no:cacheprovider tests/ops/test_hub_deferred_1018.py` → `3 failed, 2 passed` on BASE (the file copied onto BASE's hub), `0 failed` after; then `uv run pytest -q -p no:cacheprovider tests/ops` → `0 failed` (the hub's other readers: `test_hub_lines.py`, `test_hub_text_1013.py`, `test_deploy_step_c.py:298-330`, `test_deploy_freeze_1014.py:317-346`, `test_desk_launch_launchd.py`) | `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (`:94`, `:154`), `tests/ops/test_hub_deferred_1018.py` |

## NOT IN THIS JOB
- Any line of `DEPLOY-HUB.md` but `:5`, `:89`, `:93`, `:94`, `:154`; the launch line `:11`, the MODEL line `:3`, THE ONE RESUME `:53`, STEP-4 and STEP-5 text stand.
- `ops/desk/deploy-outage.sh`, `ops/desk/deploy-step0.sh` (card 784's two scripts), `ops/desk/deploy-step-c.sh`, `ops/desk/desk-launch.sh`, `ops/desk/deploy-card.sh`, `src/cobalt/jobs/restarts.py`, `data/deploy/bootstrap-owed.json`, `prompts/CARD.md`: untouched.
- The handling of `com.cobalt.aset`, `com.cobalt.radar`, `com.cobalt.agent`; any `launchctl` call, real or stubbed; loading `com.cobalt.cos`.
- F20's own deploy card and its `## LAUNCHD` line (card 730's deploy, the desk's).
- A red outside these rows: a `## DECISIONS` item, UNPROVEN (L70), with the output; never fixed here.

## READ
- `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` lines 3, 5, 53, 65, 89-96, 122-125, 137-145, 147-154, 161-170.
- `ops/desk/deploy-step-c.sh` lines 24-32, 280-290 (the `· add · deferred` line).
- `docs/40 - DevDocs/prompts/CARD.md` `## LAUNCHD` (line 69).
- `docs/40 - DevDocs/prompts/2026-10-18/730-f20-card.md` header lines 13-14, `## DECISIONS` D8.
- `tests/ops/test_hub_text_1013.py` (the form), `tests/ops/test_deploy_step_c.py` lines 290-330.

## CHECK ASKS
- X1 Are D1 (a)-(c) and D2 (a)-(b) the only changed lines of `DEPLOY-HUB.md` (`git diff <BASE> -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`), and does the `Anything else (…)` sentence of `:93` stand byte for byte?
- X2 Trace every `launchctl` call of the hub to its label source: can any path (a resume, STEP-5, 4.6L-BO) still name a label STEP-C admitted `· deferred`?
- X3 Does a resume (THE ONE RESUME, which does not re-run STEP-C) still reach smoke (f) with `<deferred set>`, read from `## RESTARTS`?
- X4 Is a set with a deferred label and nothing else (`RESTARTS:` = the deferred label alone) read as an EMPTY `<restart set>`, and does `:95` (a migration with an empty set) then refuse it as it should?

## DEPLOY PROOF
- `grep -c -F "<deferred set>" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `5`
- `grep -c -F "minus every label of" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `1`
- hub-deferred tests · `uv run pytest -q -p no:cacheprovider tests/ops/test_hub_deferred_1018.py` · green: `0 failed` (this smoke read quotes the gate's pytest run; the hub adds no test run in production)

## RECORDS
- Drafter `draft-hub-deferred` (prompt 786), 2026-10-18 16:33 EDT from `date`; `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `170e90ca` (the BASE).
- `git -C /Users/cobalt/cobalt show "main:docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` read whole (188 lines): `:3` MODEL launchctl rule; `:5` names (`a \`deferred\` label is not in it`); `:89` STEP-C `· add · deferred`; `:93` GATE set within the three; `:94` THE SET DRIVES THE REST; `:154` smoke (f) `RESTARTS:` = `<restart set>`; call sites `:65`, `:122`, `:125`, `:139`, `:143-145`, `:149`, `:162-169`. `deferred` occurs on `:5`, `:13`, `:89` only; `deploy-outage`, `deploy-step0` and `com.cobalt.cos` occur nowhere in it.
- The hub's path is `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (the prompt's `prompts/DEPLOY-HUB.md`).
- No test pins the five changed lines (grep of `tests/` and `ops/` for their texts: no match); `test_deploy_step_c.py:298-301` asserts the MODEL line holds `<launchd set>` and STEP-C names `deploy-step-c.sh` once: both kept.
- BAND HIGH: a fixed hub file read by every deploy (desk-set; L9 other-house read before the deploy).
- RESTARTS (K10): `docs/` and `tests/ops/` → no resident; the builder's `cobalt jobs restarts` line is the record.
- ORDER: this card deploys before card 730 (F20); card 784 (the two scripts) is independent of it.
