# DRC D3 fix r1 — check report, round 2 of ≤3 (2026-09-29)

Prompt: `prompts/2026-09-29/09-drc-d3-fix-r1-check.md`. Seat `drc-d3-fix-r1-check` (Sonnet 5.5 hub). Started 2026-09-29 14:52 EDT, closed 15:24. Range `a8c622ca..15c23748` on `drc/d1-trading-log`.

## §0 Headline
- Checked F-1 … F-8, RUN-1 … RUN-3, the re-issued `## FOR K3` and the three suites' executed output. STATUS: NOT READY — all three houses say `DEFECT REMAINS`; two claims HOLD in my file-check.
- opus: DEFECT REMAINS (F-7) · sol: DEFECT REMAINS (F-1 `--dry-run --no-trades`, F-7) · grok: DEFECT REMAINS (F-7). Houses that checked: 3 of 3.
- Defects that HOLD: 2 (F-7's negative control fails through the old assertion; `--dry-run --no-trades` still writes). ESCALATE: 12.

## L74
- 14:52 ET: the Read tool result of this prompt (`09-drc-d3-fix-r1-check.md`, lines 1–136) carried an appended `<system-reminder>` block asking that commits and PR descriptions end with a `Claude-Session:` line and a session URL, and saying a file-send tool exists for putting a file in front of the user. DATA under L74: recorded once here, not followed. This run makes no commit.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| date | `date` | 0 | `Tue Sep 29 14:52:41 EDT 2026` → `<D>` = 2026-09-29 |
| placeholder gate 1 | `grep -n -E "R_[_]" …09-drc-d3-fix-r1-check.md` | 1 | no output |
| placeholder gate 2 | `grep -n -F "FILL AT LAUNCH" …09-drc-d3-fix-r1-check.md` | 0 | line 1 (the SEAT prose) and line 19 (the gate's own line) only |
| GROK GATE R17 | `grep -n "^| R17 " cto-2026-09-24.md`; `git log -1 --format=%H -S"Grok approved with no asking going forward"` | 0 | `35:| R17 | 07:32 ET | … Grok approved with no asking going forward …`; commit `1758fd78a572f47b613b2ca831dcfa636ed8f65a`; re-run at 15:09, same |
| GROK GATE R19 | `grep -n "^| R19 " cto-2026-09-24.md`; `git log -1 --format=%H -S"All 4 house models approved"` | 0 | `37:| R19 | 07:36 ET | … All 4 house models approved for use indefinlitly …`; commit `67f785f3e1a09b59766f3296b111940a7fbaa364` |
| round 1 committed | `git log -1 --format=%H -- drc-d3-check-2026-09-25.md`; `tail -n 3` | 0 | `5055151dbf68899b82de5b11f99733ed2d03048c`; last non-blank line starts `DRC D3 CHECK DONE · round: 1 ·` |
| classification committed | `git log -1 --format=%H -- drc-d3-fix-r1-draft-2026-09-29.md`; `tail -n 3` | 0 | `13610db3781eb4e0cc82e1ce86c8c18db36fabb0`; last non-blank line starts `DRC D3 FIX R1 DRAFTED ·` |
| development resumes | `grep -n -F "continue with development process" cto-2026-09-28.md` | 0 | `35:| R26 | 08:5x ET | …` |
| this launch | `grep -n "09-drc-d3-fix-r1-check.md" cto-2026-09-29.md`; `git log -1 --format=%H -S"09-drc-d3-fix-r1-check.md" -- cto-2026-09-2*.md` | 0 | `94:| R86 | 14:52 ET | — LAUNCH ROW …` (also `61` R53, `62` R54, `90` R82, `100` — none counted); commit `1db9851c4fdd53c228c074b7486682d74dda312f` |
| stagger | `grep -n -F "no other house hub is running" cto-2026-09-29.md` | 0 | line 94 (R86) carries the phrase and names `09-drc-d3-fix-r1-check.md` |
| grok | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` |
| worktree | `ls /Users/cobalt/cobalt-wt/drc-d1` | 0 | present |
| THE BUILT LINE | `tail -n 3` of the build report | 0 | `DRC D3 FIX R1 BUILT 15c23748 \| on a8c622ca \| red f616be37 \| migration none \| offline 3625/0 \| with-DB 4170/0 \| live-note 146/0 \| .env: removed \| 0020: rolled back \| RESTARTS: com.cobalt.aset com.cobalt.radar \| tests added: 13 \| FIX: 8 \| RUNS: 3 \| ESCALATE: 12`; every required field present; `<tip>` `15c23748`, `<red>` `f616be37` / `654dfeff`; no `0020: UNPROVEN`; `FIX: 8` |
| tip subject | `git log --oneline -1 15c23748` | 0 | `15c23748 fix(drc): D3 fix r1 — the dry run writes nothing (F-1), …` |
| range | `git log --oneline a8c622ca..15c23748` | 0 | `15c23748` · `654dfeff` · `f616be37` · `7dd031fb` (docs only). Non-docs commits 3 |
| code above tip | `git log --oneline 15c23748..drc/d1-trading-log -- src tests configs ops` | 0 | EMPTY |
| path union | `git log --stat --format=%h a8c622ca..15c23748` | 0 | 16 paths, exactly `09-29/08` F4's list (see `## Scope`) |
| report headers | `grep -n "^## " <build report>` | 0 | 17 headers in the prompt's order; no `(run 2)` section |
| SWEEP | six greps | — | see `## Checked against the branch` (i) |
| .env | `ls /Users/cobalt/cobalt-wt/drc-d1/.env` | 1 | `No such file or directory` |
| recovery | `ls scratch/tribunal-bars-0920/drc-check/d3-fix-r1` | 1 | `No such file or directory` → fresh run |
| probe: Opus | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` | 0 | `OK` (one harness notice line about a deny-rule spelling in `../../cobalt/.claude/settings.local.json`, recorded) → SEATED |
| probe: Sol | `codex exec … "Reply with only the word OK." < /dev/null` | 0 | `OK` → SEATED |
| Astra | — | — | astra: not a fix-round seat; D3's NEW BUILD Astra read is the desk's |

## Packet
28 files staged in `scratch/tribunal-bars-0920/drc-check/d3-fix-r1/`, each part < 15,000 B (largest `code-at-tip.part7.md` 14,891 B). MEASURED by `ls -la` (bytes): `fix-diff.part1/2/3` 12,235 + 11,146 + 13,919; `devdocs-diff.md` 8,319; `code-at-tip.part1…7` 10,815 + 6,147 + 12,851 + 9,827 + 4,671 + 2,613 + 14,891; `nbsp-proof.md` 4,237; `build-proof.part1/2/3` 8,687 + 8,381 + 6,208; `runs.md` 2,479; `suites.md` 6,594; `seam.md` 7,050; `round-1.part1/2` 9,212 + 11,504; `rules.md` 14,168; `prompt.part1…7` 10,946 + 8,956 + 7,361 + 9,488 + 8,332 + 8,133 + 9,508; `QUESTIONS-DRC-D3-FIX-R1.md` 9,370. **Total 258,048 B ≈ 64,512 tokens per checker**, under the 400,000 B ceiling; no cut applied.
Checks: `grep -c "^commit "` over the fix-diff parts = 1 + 1 + 1 = 3 = the non-docs commit count; `grep -c "^diff --git"` = 7 + 2 + 1 = 10 = the non-docs path-touches (`--stat`: 12 − 5 DevDocs paths, 2, 1). `grep -n "^=== "` over the `code-at-tip` parts lists every path the prompt names. Fixture copy: `template_shape.md` body 1,966 B = original 1,973 B − 7 (each U+00A0 written as U+0020), header 647 B. Trailing-whitespace lines in the fix diff: 51.
Deviations (facts): (1) L32: the fixture line's name is written `<his name — not written here, L32>` in `fix-diff.part1.md` (the removed `-` line) and `<his name — L32>` on round 1's report line 107 in `round-1.part1.md`; the source files carry it, the packet does not. (2) `QUESTIONS` names `round-1.*`, `build-proof.*`, `prompt.*` where the prompt says `round-1.md`, `build-proof.md`, `prompt.md`, because those files are parts. (3) Copies carry U+0020 where the sources carry U+00A0 (the E3 `Take all` literal, the F-6 test's literals, the fixture, the build report's E3 line). (4) The prompt's per-part cuts of `code-at-tip` (7 parts) and `prompt` (7 parts) were made at line boundaries. (5) `suites.md` adds a `THE DESELECTS, LISTED` block: each of the ten selector lines' `file:line` is my own `grep -rn -F` and none moved.

## CONTINUE
next: none — the run is over.

## Rows
Quotes are ≤30 words from each check; walked inputs included. Sol's line numbers are packet lines, walked at the real lines in `## Checked against the branch`.
| row | opus | sol | grok |
|---|---|---|---|
| F-1 | CLOSED — `test_drc_d3_fix_r1.py:26` exercises `cli.py:282`–`:283`; spy at `:40`, call `:45`, real `rules_checkbox_block`; constant `cli.py:50` | NOT CLOSED — `test_drc_d3_fix_r1.py:42` tests only `--dry-run` without `--no-trades`; `--dry-run --no-trades` reaches `no_trade` before the dry-run guard at `cli.py:267` | CLOSED — `test_drc_d3_fix_r1.py:45` exercises `cli.py:282`; dry-run replaces `rules_block`, prints `plan_note`, returns before `run_drc_build` (`:285`); `no_trades=False` walked |
| F-2 | CLOSED — `test_drc_d3_fix_r1_db.py:85` and `:102` exercise `s2.yaml:526`–`:535`; predicate byte-identical to `event_state` `:514`–`:523`; no `ts` predicate | CLOSED — `test_drc_d3_fix_r1_db.py:79` and `:94` exercise `s2.yaml:522`; writes restricted to the selected event's note without a clock-date predicate | CLOSED — `test_drc_d3_fix_r1_db.py:97` and `:116` exercise `s2.yaml:526`; `writes` counts rows whose `note` equals the same event's `note_path`; no `ts` predicate |
| F-3 | CLOSED — `test_drc_d3_fix_r1.py:61` (assert `:78`) exercises `build.py:632`; unmatched reads `not computed — missing`, matched `None` reads `not given`; pins green | CLOSED — `test_drc_d3_fix_r1.py:66` and `:82` exercise `build.py:632`; unmatched partial, matched-without-stop, matched-with-stop all covered | CLOSED — `test_drc_d3_fix_r1.py:78` exercises `build.py:632`; `_Stats.text` `:310`, `:314`, `:315`; no stop computed from risk, prices or shares |
| F-4 | CLOSED — `test_drc_d3_fix_r1.py:110` exercises `build.py:545` and `units.py:98`; `drc-risk` keeps `pnl`, `risk_parameters` under `PNL_PLACEMENT`; E3 `:306`, `:311` (and `:309` literal) | CLOSED — `test_drc_d3_fix_r1.py:105` exercises `build.py:545`, `units.py:52`, `:98`; both placements, membership, order and second-build idempotence asserted | CLOSED — `test_drc_d3_fix_r1.py:132` exercises `units.py:52` and `build.py:545`; open on next line, his line kept, order unchanged, second build changes nothing |
| F-5 | CLOSED — `test_drc_d3_fix_r1.py:150` exercises `playbooks.py:97`; tuple gains `UnicodeDecodeError` only; no other error newly swallowed | CLOSED — `test_drc_d3_fix_r1.py:156` exercises `playbooks.py:97`; note unmapped and counted, build completes | CLOSED — `test_drc_d3_fix_r1.py:166` exercises `playbooks.py:97`; bad note in `errors`, resolves `unmapped` with codec text, `run_drc_build` returns the note |
| F-6 | CLOSED — `test_drc_d3_fix_r1.py:186`, `:192` exercise fixture `:5`, `:49`, `:128`, `:134`, `:156`, `:173`, `:175`; 7 at tip, 0 at base; `--numstat` `7 7`; X-T 17 / 2 / 186 | CLOSED — `test_drc_d3_fix_r1.py:186`, `:194` exercise fixture `:5` and the seven positions; one at each, none at base, counts unchanged | CLOSED — `test_drc_d3_fix_r1.py:189`, `:197`–`:199` exercise fixture `:5`; `grep -c` 7 tip / 0 base, one match per required line, `7 7`, 17 / 2 / 186 |
| F-7 | NOT CLOSED — `test_drc_d3_fix_r1_db.py:140` rebuild input: helper's first line `test_drc_build_db.py:168` (old `:155`@a8c622ca) fails too; new note half `:173` never shown failing alone | NOT CLOSED — rebuild at `test_drc_d3_fix_r1_db.py:137`; old row-equality `test_drc_build_db.py:155`@a8c622ca also fails, as does the helper's identical first assertion `:168` | NOT CLOSED — `test_drc_d3_fix_r1_db.py:142` calls `_snapshot_holds` after a rebuild; the raise is the first assert `test_drc_build_db.py:168`, the old assertion; `:173` not reached |
| F-8 | CLOSED — `test_drc_d3_fix_r1_db.py:147` (`:156`–`:158`) exercises `test_drc_build_db.py:238`; `after != before_text` fails while `is_file()` passes | CLOSED — `test_drc_d3_fix_r1_db.py:145` exercises `test_drc_build_db.py:235`; old `is_file()` passes while the helper fails on the unrewritten note | CLOSED — `test_drc_d3_fix_r1_db.py:156`–`:158` exercise `_note_rebuilt` (`test_drc_build_db.py:230`); `is_file()` passes, helper raises at `:238` |
No cell is `INPUT NOT WALKED`: each names a test and a code line.

## Reds
| row | opus | sol | grok |
|---|---|---|---|
| F-1 | YES — `AssertionError: regenerate_rules_config called on a dry run`; `cli.py:277`@a8c622ca → `build.py:556` → `prefill/drc.py:82`@a8c622ca → `rules_gen.py:158`@a8c622ca | RED on base; `cli.py:276`@a8c622ca reaches `rules_gen.py:158`@a8c622ca; evidence build report `:65` | `AssertionError: regenerate_rules_config called on a dry run`; base calls `plan_note` with real deps `cli.py:277`@a8c622ca |
| F-2 | YES — (a) `writes ge 1 (actual 0)`; (b) `event_state ok; writes ok`; base `s2.yaml:526`@a8c622ca | both REDs for the named reasons; base predicate `s2.yaml:524`@a8c622ca | (a) `writes ge 1 (actual 0)`; (b) `PASS`; base filters on `ts` `s2.yaml:526`@a8c622ca |
| F-3 | YES — `['  - stop: not given'] == …`; `build.py:632`–`:633`@a8c622ca | RED with `stop: not given`; `build.py:632`@a8c622ca | `stop: not given` against the `not computed` line; `build.py:632`@a8c622ca–`:633`@a8c622ca |
| F-4 | YES — `no drc-risk-facts section`; `build.py:545`, `units.py:50`@a8c622ca | RED, no facts section above the paragraph; `build.py:545`@a8c622ca | `no drc-risk-facts section`; base `FACTS` `("drc-risk","facts")` `units.py:50`@a8c622ca |
| F-5 | YES — `UnicodeDecodeError … byte 0xff`; `playbooks.py:97`@a8c622ca | RED with the escaping `UnicodeDecodeError`; `playbooks.py:95`@a8c622ca | `UnicodeDecodeError` from `read_strategies`; base except lacks it `playbooks.py:97`@a8c622ca |
| F-6 | YES — (a) name on line 5 (redacted); (b) `[] == [5, 49, …]`, base 0 | both REDs; attribution `template_shape.md:5`@a8c622ca, no U+00A0 at base | line 5 not the constructed heading; U+00A0 list empty; base count 0 |
Hub, from the build report (report lines 61–86): F2 offline → `6 failed, 54 passed, 2 warnings in 8.21s`; the six failures, one line each: F-1 `AssertionError: regenerate_rules_config called on a dry run`; F-3 `assert ['  - stop: not given'] == ['  - stop: n...g: Open T...`; F-4 `AssertionError: no drc-risk-facts section`; F-5 `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 39`; F-6 (a) `assert '<the committed line 5, his name — not written here, L32>' == '# Example Trader DRC'`; F-6 (b) `assert [] == [5, 49, 128, ...156, 173, ...]`. F3 with-DB → `2 failed, 12 passed in 7.15s`: F-2 (a) `AssertionError: writes ge 1 (actual 0)`; F-2 (b) `AssertionError: event_state ok; writes ok` (verdict PASS, raw `done 1`). The reds are exactly F-1, F-3, F-4, F-5, F-6 (a)+(b) offline and F-2 (a)/(b) with-DB, each for its named reason (as quoted). The F-3 pin PASSED on `a8c622ca`; the F-7 pin and control and the F-8 pin and control PASSED on `a8c622ca` (build report `:83`); the build's ESCALATE 7 records no `NOT RED ON a8c622ca` and no pin red.

## Intent
| checker | SECOND answer |
|---|---|
| opus | KEPT. The old F-7 assertion now lives inside the helper (`test_drc_build_db.py:168`), and `is_file()` is kept. No mark was added. … |
| sol | KEPT — no D3 assertion was removed or loosened; no mark was added, and the named unchanged paths remain untouched. |
| grok | `KEPT`. No D3 assertion was removed or loosened: the card-snapshot test still requires the stored rows to equal `before` (`test_drc_build_db.py:168`) and adds the note check … |

## Scope
| checker | THIRD answer |
|---|---|
| opus | NOTHING WIDENED. The only `src/` paths are the four named ones, the only config change is K10.2, there is no migration, and the fixture shows `7 7`. |
| sol | NOTHING WIDENED — only the authorized source paths, K10.2, tests, fixture, and DevDocs changed; no migration was added. |
| grok | `NOTHING WIDENED`. Non-docs paths are `src/cobalt/drc/{cli,build,units,playbooks}.py`, `s2.yaml` (K10.2 only), the two test files, the two new test files, and the fixture (`7 7`). |
My PREFLIGHT path-union facts: 16 paths — `configs/cobalt/smoke/s2.yaml`; `docs/40 - DevDocs/cobalt/drc/{build,cli,playbooks,units}.md`; `docs/40 - DevDocs/cobalt/smoke/checks.md`; `src/cobalt/drc/{build,cli,playbooks,units}.py`; `tests/cobalt/test_drc_build.py`; `tests/fixtures/drc/template_shape.md` (`15c23748`); `tests/cobalt/test_drc_build_db.py`, `tests/cobalt/test_drc_d3_fix_r1_db.py` (`654dfeff`); `tests/cobalt/test_drc_d3_fix_r1.py` (`f616be37`); `docs/40 - DevDocs/reports/drc-d3-build-2026-09-25.md` (`7dd031fb`). No path outside the expectation.

## Seam
| checker | SIXTH answer |
|---|---|
| opus | SEAM STATED. Borne out by `code-at-tip`: `units.py:47`–`:56`, `:94`, `:98`; `build.py:554`; `s2.yaml:501`, `:512`. Not in any slice: `build.py:324`, `:689`, `:697`–`:713`, `units.py:125`, `store.py:1436`, `checks.py:461` … |
| sol | SEAM STATED — registration point and all unit IDs incl. `drc-risk-facts/facts`, loop, `record_build` and smoke guard agree with `build.py:545`, `units.py:47`, `:52`, `:98`, `s2.yaml:501`, `:512`. |
| grok | `SEAM STATED`. … the sliced cites match; `build.py:324`, `units.py:125`, `build.py:697`–`:713`, `store.py:1436`, `checks.py:461` are not slices — "Not a defect." |

## Suites
| suite | opus | sol | grok |
|---|---|---|---|
| offline | SHOWN — `3625 passed, 562 skipped, 1 xfailed, 23 warnings in 563.06s` | SHOWN — summary at build report `:119` (values written as `<value>`) | SHOWN — `3625 passed, 562 skipped, 1 xfailed, 23 warnings in 563.06s (0:09:23); 0 failed` |
| with-DB | SHOWN — `4170 passed, 6 skipped, 9 deselected, 3 xfailed`; `.env` removed; probe `28 == 34`, short by 6 | SHOWN — `.env` removal and absence-probe shortfall at build report `:122`, `:126`, `:127` | SHOWN — `4170 passed, 6 skipped, 9 deselected, 3 xfailed, 29 warnings in 680.39s (0:11:20); 0 failed`; probe short by six |
| live-note | SHOWN — `146 passed, 1 skipped, 15 warnings in 26.66s`; no skip names `COBALT_LIVE_VAULT_ROOT` | SHOWN — summary at build report `:116` | SHOWN — `146 passed, 1 skipped, 15 warnings in 26.66s; 0 failed` |
| deselects | DESELECTS AS STATED | DESELECTS AS STATED | `DESELECTS AS STATED` |
Hub, quoted from the build report itself (not the packet copy; report lines 117–127): offline `3625 passed, 562 skipped, 1 xfailed, 23 warnings in 563.06s (0:09:23)` — 0 failed, 0 errors. With-DB `4170 passed, 6 skipped, 9 deselected, 3 xfailed, 29 warnings in 680.39s (0:11:20)` — 0 failed, 0 errors. Live-note `146 passed, 1 skipped, 15 warnings in 26.66s` — 0 failed, 0 errors. SKIPPED lines naming `COBALT_LIVE_VAULT_ROOT` on the live-note leg: none (the only skip is `test_replay_line.py:266`, `COBALT_TEST_LIVE_DRC`); on the with-DB leg the six skips include three that name `COBALT_LIVE_VAULT_ROOT` not set (`test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262`), as the report states. Deselected: 9 (the ten selector lines of `suites.md`; my `grep -rn -F` per name printed the same lines the report names: `test_tenancy.py:692`, `:701`, `:714`, `:263`; `test_migrate_proof.py:306`; `test_voice_store.py:217`, `:234`, `:259`; `test_voice_confirm.py:218`; `test_voice_lifecycle.py:137`). Absence probe: `1 failed`, `E       assert 28 == 34`, short by exactly 6 (`drc_imports`, `drc_fills`, `drc_rows`, `drc_stated_books`, `voice_turns`, `drc_events`). `.env: removed, proven gone` is written for F3 (report line 85) AND F8 (line 127).

## Runs
| run | opus | sol | grok |
|---|---|---|---|
| RUN-1 | RESULT SHOWN — open trade status=open; P&L line rendered, nothing raised | RESULT SHOWN — at build report `:112` | RESULT SHOWN — `gross_pnl='8.0'; P&L line=- P&L: gross $8.0 · net not given · commission not given` |
| RUN-2 | RESULT SHOWN — `… equals the in-memory render = True; first difference = none` | RESULT SHOWN — at build report `:113` | RESULT SHOWN — `… = True; first difference = none` |
| RUN-3 | RESULT SHOWN — E3, E6, E8 offline + E8 real-rows + E11 with-DB, 5 PASSED lines, 4 of 4 | RESULT SHOWN — at build report `:114` | RESULT SHOWN — `4 of 4 PASSED`, five node ids quoted |
Hub, from the build report `## F5 THE RUNS` (lines 112–114): RUN-1 `RUN-1: open trade status=open; gross_pnl='8.0'; P&L line=- P&L: gross $8.0 · net not given · commission not given` → P&L line rendered. RUN-2 `RUN-2: re-render after the job row's JSON equals the in-memory render = True; first difference = none` → equal. RUN-3 → 4 of 4 PASSED (5 node ids).

## Checked against the branch
Walked in `/Users/cobalt/cobalt-wt/drc-d1/` at `15c23748` (Read / grep) and `git show a8c622ca:<path>`. Packet-line citations are given with both numbers.
| claim | who | file:line | verdict | note |
|---|---|---|---|---|
| F-7 NOT CLOSED: the control's rebuild fails the helper through its first, old assertion | opus, sol, grok | `tests/cobalt/test_drc_d3_fix_r1_db.py:140` (rebuild), `:141`–`:142` (`pytest.raises`); `tests/cobalt/test_drc_build_db.py:168` (helper's first line); `tests/cobalt/test_drc_build_db.py:155`@a8c622ca (old line, same text) | HOLDS | after a rebuild with the changed card `_build_rows` differs from `before`, so `:168` raises exactly as `:155`@a8c622ca would; `:173` (the note's `card:` stop) is never the raiser. Sol's `:137` = real `:140`; Grok's `:142` = the `pytest.raises` body |
| F-7's pin still cannot fail on a dict change with no rebuild | opus, grok | `tests/cobalt/test_drc_build_db.py:154`–`:155` | HOLDS | line `:154` sets the dict, `:155` calls the helper; nothing between them rebuilds. The pin's result is a stated PIN (green on base) per the prompt, its negative control is the row's proof |
| `--dry-run --no-trades` reaches `no_trade` before the dry-run branch | sol (grok: NOT CHECKABLE FROM READS) | `src/cobalt/drc/cli.py:268`–`:275` (branch), `:279` (dry-run branch after it), `:252`, `:254` (both flags independent `store_true`); `src/cobalt/drc/imports.py:672` (`store.record_stated_book(...)`), `:683` (`store.rebuild`) | HOLDS | the combined input runs `imports.no_trade`, which records a stated book — the dry-run guard is not reached. Sol's `cli.py:267` = real `:268`; Sol's `test …:42` = real `:45`. Not a path the F-1 test or the row names; the base has the same branch order (`cli.py:265`–`:277`@a8c622ca) |
| F-5 build half asserts `unmapped playbooks: 2`, not tied to the bad note | opus, grok | `tests/cobalt/test_drc_d3_fix_r1.py:172` (real; the packet's `code-at-tip.part3.md` line 172 is the same assertion) | NOT CHECKABLE FROM READS — needs a run that lists which names sum to the count; the resolution text is asserted at `:166` |
| the 21:10 process and the build's resident resolve the same vault root string | opus | `src/cobalt/replay/line.py:212`, `src/cobalt/drc/build.py:106`–`:109` | NOT CHECKABLE FROM READS — needs the environment of both production jobs |
| `test_drc_d3_fix_r1.py:197`–`:199` and `test_drc_build.py:309` hold a literal U+00A0 rather than an escape | opus | those lines | NOT CHECKABLE FROM READS by the checkers; hub fact: `grep -c -P 'startswith\("### \x{00A0}Take all"\)' tests/cobalt/test_drc_build.py` → `1` (a literal); the F-6 test's real line `:197` holds a NBSP character in its literal (the copy in the packet writes it as a space) |
| `risk_parameters_line` on the dry-run path writes nothing | opus | `src/cobalt/prefill/drc.py` (body not in the packet) | NOT CHECKABLE FROM READS |
| the seam's cites `build.py:324`, `:689`, `:697`–`:713`, `units.py:125`, `store.py:1436`, `checks.py:461` are true | opus, grok | build report `## F4` proofs (`:105` of the report) | NOT CHECKABLE FROM READS by the checkers (not sliced); hub: the build report's own greps print those lines and the preflight `grep -n "def text"` `304` and `plan_note` at `324` agree |
(i) SWEEP: `grep -n "regenerate_rules_config" cli.py` → no hit. `grep -n -F "stats.text(" build.py` → `610`, `611`, `627`, `629`, `630`, `632` (the stop line), `648`. `grep -n "drc-risk-facts" units.py` → `16`, `28`, `52`, `95`. `grep -n "UnicodeDecodeError" playbooks.py` → `97`. `grep -n -F "AT TIME ZONE" s2.yaml` → no hit. `grep -n "requires_relation" s2.yaml` → `165` (K5.1, `system.radar_score_run`), `501` (K10.1), `512` (K10.2) — unchanged. No write call, second regenerator path or removed guard among them.
(ii) `git log --oneline a8c622ca..15c23748 -- src/cobalt/drc/store.py … configs/cobalt/jobs.yaml` → EMPTY.
(iii) `git log -p a8c622ca..15c23748 -- configs/cobalt/smoke/s2.yaml` → two hunks, `@@ -523,7 +523,16 @@` and `@@ -533,7 +542,7 @@`, both inside K10.2 (lines 508–545).
(iv) L32: no ticker beyond the constructed ones, no real date or name of his, no file name of his and no value written (`grep -F` of his surname over this report → 0 hits).

## Ready for K3
| checker | CHECK line | ready | reason verbatim |
|---|---|---|---|
| opus | `CHECK DRC D3 FIX R1: DEFECT REMAINS · ready for K3: NO · F-7 control fails on old rows check; note half unproven` | NO | F-7 control fails on old rows check; note half unproven |
| sol | `CHECK DRC D3 FIX R1: DEFECT REMAINS · ready for K3: NO · dry-run no-trades still writes; F-7 control also fails old assertion` | NO | dry-run no-trades still writes; F-7 control also fails old assertion |
| grok | `CHECK DRC D3 FIX R1: DEFECT REMAINS · ready for K3: NO · F-7 control fails where the old row assertion also fails` | NO | F-7 control fails where the old row assertion also fails |

## FOR THE CLASSIFIER
Round 2 of ≤3 — a HOLD goes to fix round 2, classified first (L75); its check is round 3, THE LAST. No class or recommendation added.
1. "F-7 NOT CLOSED — the negative control's rebuild fails the helper through the old rows assertion" — opus, sol, grok — F-7 — `tests/cobalt/test_drc_d3_fix_r1_db.py:140`, `tests/cobalt/test_drc_build_db.py:168`, `:155`@a8c622ca — HOLDS
2. "F-7's pin still cannot fail on its defect (no rebuild between the dict change and the helper)" — opus, grok — F-7 — `tests/cobalt/test_drc_build_db.py:154`–`:155` — HOLDS
3. "`--dry-run --no-trades` reaches `no_trade` before the dry-run guard (F-1)" — sol — F-1 — `src/cobalt/drc/cli.py:268`–`:275`, `src/cobalt/drc/imports.py:672` — HOLDS
INPUT NOT WALKED: none.

## ESCALATE
1. Opus: `CHECK DRC D3 FIX R1: DEFECT REMAINS · ready for K3: NO · F-7 control fails on old rows check; note half unproven` — file-check: F-7 HOLDS (items 1–2).
2. Sol: `CHECK DRC D3 FIX R1: DEFECT REMAINS · ready for K3: NO · dry-run no-trades still writes; F-7 control also fails old assertion` — file-check: F-7 HOLDS; the `--no-trades` path HOLDS (item 3).
3. Grok: `CHECK DRC D3 FIX R1: DEFECT REMAINS · ready for K3: NO · F-7 control fails where the old row assertion also fails` — file-check: F-7 HOLDS. Its `--no-trades` note is NOT CHECKABLE FROM READS (Sol's walk of `imports.py:655`–`:688` settles it).
4. Items 1–3 under `## FOR THE CLASSIFIER` (restated by number); `defects that HOLD: 2` counts F-7 (items 1–2 are one defect) and the `--no-trades` path (item 3). NOT CHECKABLE rows are listed under `## Checked against the branch`; no `INPUT NOT WALKED`.
5. Packet: no cut; 258,048 B measured; deviations recorded under `## Packet` (the L32 redaction of his name in two places, `round-1.*` / `build-proof.*` / `prompt.*` naming, U+0020 for U+00A0 in copies). No checker wrote a file it was not told to: after the run the folder holds only the three `*-check.md` files beyond the packet, and `/Users/cobalt/cobalt-wt/drc-d1` is unchanged (`ls -la` before and after). No `ASK DESK` of mine. All three seats answered inside the 45-minute clock (Opus and Sol back by 15:14, Grok at 15:23; launched 15:09).
6. L74: recorded under `## L74`.
7. RUN-1: P&L line rendered (`gross_pnl='8.0'` → `$8.0`, no raise). RUN-2: equal (`first difference = none`). RUN-3: 4 of 4 PASSED (5 node ids). Results, not defects (L70).
8. O-1 was answered A (R66; his string R80) and F-6's U+00A0 half is built: `nbsp-proof.md` counts — 7 lines with U+00A0 at the tip (5, 49, 128, 134, 156, 173, 175, one each), 0 at the base; `--numstat` `7 7`.
9. Seats: opus SEATED — `CHECK DRC D3 FIX R1: DEFECT REMAINS · ready for K3: NO`; sol SEATED — `CHECK DRC D3 FIX R1: DEFECT REMAINS · ready for K3: NO`; grok SEATED — `CHECK DRC D3 FIX R1: DEFECT REMAINS · ready for K3: NO`. The builder's own open ASK DESK (build ESCALATE 2, the F-2 stamp set by an `UPDATE` of the writer's row, [14:24:44 EDT]) stays with the desk; none of the three checkers objected to it.
10. The build's `## FOR THE DEPLOY`, verbatim: "Records carried from `09-28/11` ESCALATE 8, in substance. None was run here. — RESTARTS: this range `a8c622ca..15c23748` → `RESTARTS: com.cobalt.aset com.cobalt.radar`. The DRC range `f52ed883..15c23748` → `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar`, widened by the two UNCLASSIFIED config rows (`configs/cobalt/prefill.yaml` M, `configs/cobalt/templates/drc.md.j2` D). Those stay UNCLASSIFIED (L42) for the desk to classify. The branch's `.clinerules` row is OWED to the DRC deploy (R74). — `0019` and `0020` at the deploy's migrate step. — `launchctl bootout gui/$(id -u)/com.cobalt.prefill-drc` + the plist removed from `~/Library/LaunchAgents`. — His daily-stop value loaded before the first build (D4's item — until then the risk facts say `not given`). — The E7 ops read of D2. — THE DEV-VAULT PROOF with a diff (L28 "writers off until proven on the dev vault with a diff"; v2 E3): the desk's HUB-RUN step after the check — `cobalt drc build` on the dev vault, with its unified diff. It also answers `11`'s "the build against his real template" (OUT OF SCOPE here). The first real build on a note that already carries `drc-risk/facts` under the PnL heading will move the `facts` unit into `drc-risk-facts` (an old `drc-risk/facts` unit body stays until removed by hand — the dev-vault diff shows it)."
11. Standing line: **"Round 2 of ≤3 covers DRC D3 fix r1 only (`a8c622ca..<tip>`): F-1 … F-8, RUN-1 … RUN-3, the re-issued `## FOR K3` (the seam K3 cites) and its three suites' executed output, checked by Opus 5.5 · Sol · Grok (L67; K22). With every seated house `ready for K3: YES`, `defects that HOLD: 0` and no `INPUT NOT WALKED`, D3 is checked (L67): the DRC set (D1 + K1 + K2 + D4 + D2 + D3) is ready for its deploy prompt (the state-book CLI the statement caller until K3, v3 `[F-10]`) and K3's drafter cites the fix r1 report's `## FOR K3`. A HOLD → fix round 2, classified first (L75); its check is round 3, THE LAST (L39). O-1 was his, answered A (R66; his string R80)."**
12. Standing line: **"The deploy's L68 gate re-proves offline, with-DB and the live-note suite on the stacked tree that ships (D1 + K1 + K2 + D4 + D2 + D3, migrations `0016` / `0018` / `0019` / `0020`); the deploy prompt gets its own house read (L67)."**

DRC D3 FIX R1 CHECK DONE · round: 2 · opus: CHECK DRC D3 FIX R1: DEFECT REMAINS · ready for K3: NO · F-7 control fails on old rows check; note half unproven · sol: CHECK DRC D3 FIX R1: DEFECT REMAINS · ready for K3: NO · dry-run no-trades still writes; F-7 control also fails old assertion · grok: CHECK DRC D3 FIX R1: DEFECT REMAINS · ready for K3: NO · F-7 control fails where the old row assertion also fails · houses that checked: 3 of 3 · defects that HOLD: 2 · ready for K3: NO · ESCALATE: 12
