# Results sitting — 2026-10-12 (hub `results-sitting-1012`, Sonnet 5.5; one round; no verdict of the hub's own, L37)

## §0 Headline
- Cells closed 6 of 6, open 0, one-house 0: every counted pair gave the SAME grade. Ruled: Grok, Astra (probe UP, ruled all six), the blind Anthropic seat (`RESULTS SITTING OPUS DONE`). Floor MET. Closing line of all three: `SITTING: C1 BELOW · C2 CLOSE BELOW · C3 CLOSE BELOW · C4 CLOSE BELOW · C5 AT LEVEL · C6 BELOW`.
- Per band (lookup, not a routing rule): LOW Sonnet NOT YET · Terra WITH A REVIEW; MID Sonnet WITH A REVIEW · Terra CAN BUILD; HIGH Sonnet WITH A REVIEW · Terra NOT YET. Insufficient data (n=1 per band).
- Self-vendor rulings counted: 0. REDACTIONS: 0. Opus-seat claims checked: 15 HOLD of 15 checked (1 withdrawn by the seat, not checked). House claims that DO NOT HOLD: 3 (all on C6's fold of duplicates; no grade moves). ESCALATE: 6.

## AUTHORIZATION
All checked 2026-10-12 18:16–18:25 ET, each its own Bash call:
| row | check | result |
|---|---|---|
| R1069 | `grep -n "^| R1069 "` cto-2026-10-11 :74 | carries `tribunal seats approved` ✓; `git log -S` → `2322ed1e5044b6ec734e2cd0d225252408f87dbd` |
| R1127 | cto-2026-10-11 :16 | carries `then table, sitting, him` ✓; `54121dd7989b90a85d2becee3a4c0d9c0f865e1b` |
| R1019 | cto-2026-10-11 :123 | carries `can build every band` ✓; `df9a39ed5e90fe046a735b1b08575ca2ae1ae78b` |
| R1014 | cto-2026-10-11 :128 | carries `ROUTING, not exclusion` ✓; `9198f2f967af988870bda8738eec790609a58aca` |
| R908 | cto-2026-10-10 :104 | carries `ONE OpenAI seat at a time` ✓; `fcded7118a32c94045bbb07f1f83d2e8ea827af4` |
| R109 | cto-2026-09-22 :56 | carries `Make all Opus 5.5 for now` ✓; `75b2aa5790368bdd52e5802b64780567960163ed` |
| R17 (Grok gate) | cto-2026-09-24 :35 | carries `Grok approved with no asking going forward` ✓; `1758fd78a572f47b613b2ca831dcfa636ed8f65a` |
| R19 (Astra gate) | cto-2026-09-24 :37 | carries `All 4 house models approved` ✓; `5055151dbf68899b82de5b11f99733ed2d03048c` |
| INPUTS | results table last non-blank line `TABLE DONE · rows: 11 · unknown: 21` ✓; `-S"TABLE DONE"` → `2e2c648f0d33c599548467e65d843660124129ef`; stage answer last commit `f4bb5d5ac2bde27da497f6bcbfe92856bb7bc7ca` | committed |
| PROMPTS | 427 and 428, each its own `git log -1`: both `f4bb5d5ac2bde27da497f6bcbfe92856bb7bc7ca` | committed |
| LAUNCH ROW | cto-2026-10-12 `R1270`, 18:16 ET: `Fable seat: yes · grok read: open · grok runs: 0 of 3 · openai seat: free`; `-S"427-results-sitting-tribunal.md"` → `c6893c9bacd25f262843e90578fa65d1491a6d58` | committed; `grok read: open` (not `ruled`) |
| NO NEW RULE | `grep -c -F -e "<rule>"` on 270's file, each string with its quotes, 13 allow strings (grok, astra codex, mkdir, cobalt show/log, three s2-p2-cards show/log/diff, ls, grep, tail, wc, date) each `1`; denies `"AskUserQuestion"`, `"EnterWorktree"`, `"Bash(git push*)"` each `1` | all ≥1. No Sol/Terra/Opus-checker string and no `Bash(agy *)` in this launch line. |

## PREFLIGHT
| row | rule · command | exit | result |
|---|---|---|---|
| 1 | `date` | 0 | Mon Oct 12 18:16:53 EDT 2026 |
| 2 | R17 grep (GROK GATE) | 0 | allowed |
| 3 | R19 grep (ASTRA GATE) | 0 | allowed |
| 4 | STAGGER: launch row R1270 | 0 | `grok runs: 0 of 3` · `openai seat: free` — allowed |
| 5 | `grep -c -F "gpt-6-astra" /Users/cobalt/.codex/models_cache.json` | 0 | `1` |
| 6 | CODEX PROBE `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` (background) | 0 | `OK`, 2,382 tokens → **astra: UP** |
| 7 | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` |
| 8 | `ls scratch/tribunal-bars-0920` | 0 | present |
| 9 | `ls scratch/tribunal-bars-0920/results-sitting/r1` | 1 | `No such file or directory` — fresh run |
Floor MET (Grok up, Astra UP). Nothing denied by the launch line. Pre-launch rerun at 18:25:09 (date, R17, R19, STAGGER row): allowed.

## Packet
Folder `scratch/tribunal-bars-0920/results-sitting/r1/` (first Write created it; no `mkdir`). Read → Write; every non-header line of every excerpt re-checked verbatim against its source with `grep -v -x -F -f <source> <staged>` (only my header lines and blank lines differ). Trailing whitespace: results table 1 line (line 34 `Read: `, stripped by Write; 8,442 → 8,441 B), stage answer 0 (4,505 = 4,505). No part split (all < 38,000 B); no cut from the cut order; packet far under 200,000 B.
| file | bytes | source @ last commit |
|---|---|---|
| `00-READING-ORDER.md` | 2,861 | hub |
| `01-QUESTIONS.md` | 5,343 | prompt (verbatim) + file list |
| `02-greps.txt` | 28,307 | searches run by the hub |
| `10-RESULTS-TABLE.md` | 8,441 | reports/complexity-shadow-results-2026-10-11.md @ 54121dd7989b90a85d2becee3a4c0d9c0f865e1b |
| `11-STAGE-ANSWER.md` | 4,505 | reports/bakeoff-results-stage-answer-2026-10-11.md @ f4bb5d5ac2bde27da497f6bcbfe92856bb7bc7ca |
| `12-shadow-hub.excerpt.md` | 3,792 | prompts/SHADOW-HUB.md :37-38, :72-103 @ a790e54d137d1934642764bb2667b8f023456dab |
| `13-checks-LOW.excerpt.md` | 10,605 | 366 check @ 5de12b93e825b83030b7fdcecaadd923cebee2b9; 367 check @ 0f7911d3a1ffddec7d2df8c94b2c1314e1ce4b5a |
| `14-checks-MID.excerpt.md` | 10,725 | 369 check @ 7aedae079aa784233b25e48fea22c50f5fa3d34d; 370 check @ e25437147775e6e08e7fd7404cfeedf60ba15e86 |
| `15-checks-HIGH-sonnet.excerpt.md` | 7,570 | 372 check @ 8942ad967c2f87c888838bd8e9b93bc0d6d30634 |
| `16-checks-HIGH-terra.excerpt.md` | 22,527 | 373 check @ e25437147775e6e08e7fd7404cfeedf60ba15e86 (:3-7, :36-266, :270-309, :355) |
| `17-grok-unscored.excerpt.md` | 3,398 | 368 check @ 18fbb7d575e73990bce3d6c91d7938aaf1793df2; 378 check @ ed8587ab1d7f2fb32df6557f870862a2e78ee9fc |
| `18-baseline.excerpt.md` | 17,401 | strike-fallback-env-check-2026-10-10 @ c754ba2261c4716116778cc64dd51dbd5a19da98; radar-display-fix-check-2026-10-08 @ 758c07c9d90a873c6250086fd82264c129060961; s4-p1-check-2026-10-09 @ 5fc1e9a48018383697ec040f1bf85d17eb1d4441 |
| `19-rulings.md` | 3,056 | cto-2026-10-11 @ e0fa82842a48da446925db5b0155dc1688c84ebb; cto-2026-10-10 @ 007e29508a4df2b2261d8610e637e6615a068e1e (desk files carry no column-header row; said in the file) |
| `27-laws-excerpt.md` | 13,531 | LAWS.md (vault, no git hash) L8, L29, L32, L67, L70, L77 |
Total, whole packet: **142,062 B** (MANDATORY, excl. 17 and 27: 125,133 B). LAWS.md read in full by the hub (L59). HELD ranges bounded by the next `## Dropped`; each anchor checked with `grep -n`.
`.env` note: the 373 search of the prompt (with `-e ".env"`) was DENIED by the hub's own guard (`route: .env is never read; …`), not retried; the same search without that term is in `02-greps.txt`, stated there and in `00`.
REDACTION: `grep -c -F -e "TSLA" -e "372.82" -e "374.50"` (three `-e` fixed strings per the PATTERN RULE instead of `73`'s alternation) on all 14 staged files → `0` each; also `0` on the two house ruling files. Other user data: none (fixtures use constructed names such as `ZZD1`). **REDACTIONS: 0.**
NOT STAGED: any daily-note text, `Rules.md`, any note of his, any vault or production row; the build reports (the hub read them only for the file-check below); check reports beyond the ranges; `ops/grok-sandbox.toml` and the brain's FLAG.
Hub slips, disclosed: five of my own calls were mistaken (four `Write` calls to paths outside the packet and the repo, one `grep` on a nonexistent path). Three failed EACCES, one was refused by the harness classifier (`Irreversible Local Destruction`), the grep found no file. Nothing was written or changed.

## CONTINUE
next: none — collate done. Last `date` 18:33:36.

## Clock
| time (ET) | trigger | house minutes | action |
|---|---|---|---|
| 18:16:53 | start | — | authorization |
| 18:25:09 | pre-launch rerun | — | all allowed |
| 18:25:57 | launch grok (`grok -m grok-4.7 --sandbox cobalt-job …`) + astra (`codex exec … -m gpt-6-astra -s read-only … < /dev/null`), one message, background | 0 / 0 | launched; deadline 18:45 |
| 18:28:09 | astra completion notice | astra 2.2 · grok 2.2 | astra exit 0, final message written to `astra-ruling.md` |
| 18:28:44 | check | grok 2.8 | `grok-ruling.md` absent; output 138 B; wait |
| 18:32:38 | grok completion notice | grok 6.7 | exit 0, `grok-ruling.md` present (Grok wrote it itself) |
| 18:32:44 | Opus-seat tail | — | `RESULTS SITTING OPUS DONE …` |
| 18:33:36 | file-check of build reports | — | collate |

## Cells table
SELF = each house's own mark (Grok marked all six `no`; Astra yes on C4–C6; Opus seat yes on C1–C3). Counted pair: C1–C3 Grok + Astra; C4–C6 Grok + Opus seat.
| cell | model · band · card | grok | astra | opus | counted pair | result | reason ≤25 words per house |
|---|---|---|---|---|---|---|---|
| C1 | Sonnet · LOW · 366 | BELOW | BELOW (SELF: no) | BELOW (SELF: yes, apart) | Grok + Astra | **CLOSED BELOW** | Grok: opus-own 4 vs 1, extra 3. Astra: same count, four distinct, no duplicate pair among the four. |
| C2 | Sonnet · MID · 369 | CLOSE BELOW | CLOSE BELOW (SELF: no) | CLOSE BELOW (SELF: yes, apart) | Grok + Astra | **CLOSED CLOSE BELOW** | Grok: opus-own 3 vs 2 (Sol's A3 excluded), extra 1. Astra: same, three distinct. |
| C3 | Sonnet · HIGH · 372 | CLOSE BELOW | CLOSE BELOW (SELF: no) | CLOSE BELOW (SELF: yes, apart) | Grok + Astra | **CLOSED CLOSE BELOW** | Both: opus-own 3 vs 2, extra 1. Grok: first red not a red after the cap. Astra: red persistence UNVERIFIED (settled below). |
| C4 | Terra · LOW · 367 | CLOSE BELOW | CLOSE BELOW (SELF: yes, apart) | CLOSE BELOW (SELF: no) | Grok + Opus seat | **CLOSED CLOSE BELOW** | Grok: opus-own 2 vs 1; O2 = G1 one defect. Opus seat: same count, O1 cancels against the original's O1. |
| C5 | Terra · MID · 370 | AT LEVEL | AT LEVEL (SELF: yes, apart) | AT LEVEL (SELF: no) | Grok + Opus seat | **CLOSED AT LEVEL** | Grok: opus-own 2 vs 2, extra 0. Opus seat: same; the four house findings count for nothing. |
| C6 | Terra · HIGH · 373 | BELOW | BELOW (SELF: yes, apart) | BELOW (SELF: no) | Grok + Opus seat | **CLOSED BELOW** | Grok: 13 vs 2, extra 11, red is the model's own MISSED test. Opus seat: same, red stays red after both re-passes. |
| closing line | | `SITTING: C1 BELOW · C2 CLOSE BELOW · C3 CLOSE BELOW · C4 CLOSE BELOW · C5 AT LEVEL · C6 BELOW` | `SITTING: C1 BELOW · C2 CLOSE BELOW · C3 CLOSE BELOW · C4 CLOSE BELOW · C5 AT LEVEL · C6 BELOW` | `SITTING: C1 BELOW · C2 CLOSE BELOW · C3 CLOSE BELOW · C4 CLOSE BELOW · C5 AT LEVEL · C6 BELOW` | | | |

## Self-vendor, recorded apart
ASTRA — OWN VENDOR, APART, NOT COUNTED (brain §3) — C4, C5, C6 (Terra), text unedited from `astra-ruling.md`:
- **ITEM C4 — CLOSE BELOW**: Shadow Opus-own held: 2, O1/O2 (`13-checks-LOW.excerpt.md`, Terra :61–96, :193). Original: 1, O1 (`18-baseline.excerpt.md`, LOW :98–130, :223). Extra = 2 − 1 = 1. Exception-string handling and weak repeat-suppression assertion are distinct. O2 = G1 is one defect (`13-`, Terra :61–96); its house copy adds nothing. First-run suites green (`02-greps.txt:17`); check gate green (`13-`, Terra :193). No harness-red exclusion. SELF: yes
- **ITEM C5 — AT LEVEL**: Shadow Opus-own held: 2, O1/O2 (`14-checks-MID.excerpt.md`, Terra :94–131, :223). Original: 2, O1/O2 (`18-baseline.excerpt.md`, MID :3–7, :93–149, :246). Extra = 2 − 2 = 0. Unchecked second `owned` write and comment-satisfied fetch assertions are distinct. O2/A1/A2 share the comment defect (`14-`, Terra :3–7, :94–131); house findings add nothing. First-run suites green (`02-greps.txt:33`); check gate green (`14-`, Terra :223). No harness-red exclusion. SELF: yes
- **ITEM C6 — BELOW**: Shadow Opus-own held: 13, O1–O13 (`16-checks-HIGH-terra.excerpt.md`, :36–266, :355). Original: 2, O1/O3 (`18-baseline.excerpt.md`, HIGH :71–146, :279). Extra = 13 − 2 = 11. Opus findings identify separately remediable failures. O3’s missing resident wiring and O4’s failing injected DB test are not proven one defect; O6’s missing minimum message and O13’s literal ceiling are distinct. House duplicates: O1/G6, O2/G7, O3/G8, O4/G9, O5/G10, O6/G3, O8/G1, O10/G5, O12/G12 (`16-`, :270–309). The headline “11 distinct defects” lacks a demonstrated reconciliation; house findings add nothing. MISSED red belongs to the build’s code/test, reproduced under the managed DB gate; lock acquired, DB restored, `.env` removed (:270–309). Offline check failures are added held probes. Exact builder re-pass history remains unverified; held-count arithmetic independently establishes BELOW. SELF: yes

OPUS SEAT (Anthropic, Opus 5.5) — OWN VENDOR, APART, NOT COUNTED (brain §3) — C1, C2, C3 (Sonnet), text unedited from `results-sitting-opus-2026-10-12.md` `## Grades`:
- **C1 Sonnet LOW (366) — BELOW** · STAKE: yes — Sonnet is my own vendor's model, and the baseline is my own model's work · SELF: yes (recorded apart, counts on no cell). Shadow opus-own held: 4 — `strike-fallback-env-1010-sonnet-check-2026-10-11.md:277` (`held: 4 (opus-own 4 · house 0)`), findings O1–O4 at :100–168. Original opus-own held: 1 — `strike-fallback-env-check-2026-10-10.md:223` (`held: 1`, house A Sol's A1 rejected :5), O1 at :101–119. Extra = 4 − 1 = 3 → two or more → BELOW. Distinct defects: O1 (override unpinned, :102), O2 (60 s boundary unpinned, :126) and O3 (second-streak reset unpinned, :139) are three separate missing tests. O4 (:156) is the SAME defect as the original's O1 (unprintable exception escapes `step()`, original :103). The original's build had the same defect, so O4 cancels against the baseline and the 3 extra are all missing tests. No first-run red is recorded for 366: the table row (`complexity-shadow-results-2026-10-11.md:18`) names none, while it does name one for 372 and 373. The check gate on the tip is green (:6). I did not read the build's stop line itself: UNVERIFIED — `tail -n 1` of the 366 build report.
- **C2 Sonnet MID (369) — CLOSE BELOW** · STAKE: yes — Sonnet is my own vendor's model, and the baseline is my own model's work · SELF: yes (recorded apart). Shadow opus-own held: 3 — `radar-display-fix-1008-sonnet-check-2026-10-11.md:281` (`held: 3 (opus-own 3 · house 0)`), O1–O3 at :109–156. Original opus-own held: 2 — `radar-display-fix-check-2026-10-08.md:4` (held 3 = O1, O2 Opus + A3 Sol; table :143–148), :246 `held: 3`. Extra = 3 − 2 = 1 → CLOSE BELOW. Distinct defects: O1 (stale line can leave the `try`, :111), O2 (`since <time>` unpinned, :132) and O3 (unconditional TERMINAL restore, :146) are three distinct weak tests; O1 and O2 sit on one test but use different mutations. O4 is the original's O3 (rejected there too; original :126, shadow :160). It was REJECTED and is not counted. No first-run red is recorded for 369 in the table (:18). Build stop line not read: UNVERIFIED — `tail -n 1` of the 369 build report.
- **C3 Sonnet HIGH (372) — CLOSE BELOW** · STAKE: yes — Sonnet is my own vendor's model, and the baseline is my own model's work · SELF: yes (recorded apart). Shadow opus-own held: 3 — `s4-p1-1009-sonnet-check-2026-10-11.md:299` (`held: 8 (opus-own 3 · house 5)`), O1–O3 at :116–185. Original opus-own held: 2 — `s4-p1-check-2026-10-09.md:4` ("4 held … 2 defects … each found by Opus and by Sol": O1, O3), :279 `held: 4`. Extra = 3 − 2 = 1 → CLOSE BELOW. Distinct defects: O1 (same-day overwrite, :118), O2 (`seen_at` = tick start, :139) and O3 (unbounded `join`, :166) are distinct. O2 is the SAME defect as the original's O3 (original :107). House H3 = O2 (:5) is a house finding and counts for nothing. Red at first run: the model's own. Two reds, each fixed by one re-pass (2 of 2 used): `/Users/cobalt/cobalt-wt/s4-p1-1009-sonnet/docs/40 - DevDocs/reports/s4-p1-1009-sonnet-build-2026-10-11.md:7`, :157 (offline, "the model's own red"), :181 (with-DB `:163`). It was GREEN after pass S2 2 (:204, `197 passed`). A red only makes BELOW when it is still red after 2 re-passes (SHADOW-HUB :37, :78), so BELOW does not apply.

Not summed into any cell; §0 says `self-vendor rulings counted: 0`. Grok has no own-vendor cell (its 368 and 378 stay UNSCORED).

## Per band
Lookup of SHADOW-HUB :90-93 (CLOSED AT LEVEL → CAN BUILD · CLOSED CLOSE BELOW → WITH A REVIEW · CLOSED BELOW → NOT YET):
- `LOW — Sonnet (366): NOT YET · Terra (367): WITH A REVIEW · Grok (378): UNSCORED · Opus 5.5, Sol: can build (his word R1019, not measured) · insufficient data (n=1 per band)`
- `MID — Sonnet (369): WITH A REVIEW · Terra (370): CAN BUILD · Grok (368): UNSCORED · Opus 5.5, Sol: can build (his word R1019, not measured) · insufficient data (n=1 per band)`
- `HIGH — Sonnet (372): WITH A REVIEW · Terra (373): NOT YET · Grok (371): INCOMPLETE · Opus 5.5, Sol: can build (his word R1019, not measured) · insufficient data (n=1 per band)`
- `An indication for his word, not a routing rule: routing takes effect only on his word (L29).`

## Wording offered, verbatim
None. This sitting asks for grades, not wording; no house offered an `ADOPT WITH` or `REJECT` text. Experiments, owner lines and wrong-fact lines are quoted in their own sections.

## Checked against the files
Real files under `/Users/cobalt/cobalt/` and `/Users/cobalt/cobalt-wt/` (the build reports are read here only for this check). `H` = house claim.
| # | claim · who | file:line | verdict |
|---|---|---|---|
| H1 | C1 extra 4−1=3 (Grok, Astra, Opus) | strike check :277 `held: 4 (opus-own 4)`; original :223 `held: 1` | ARITHMETIC OK / HOLDS |
| H2 | C2 3−2=1; original held 3 = O1,O2 Opus + A3 Sol (Grok, Astra, Opus) | radar original :4, table :143-148, :246 | ARITHMETIC OK / HOLDS |
| H3 | C3 3−2=1; original 2 defects found by Opus and Sol (all three) | s4 original :4, :279 | ARITHMETIC OK / HOLDS |
| H4 | C4 2−1=1 (Grok, Astra, Opus) | strike terra check :193 | ARITHMETIC OK / HOLDS |
| H5 | C5 2−2=0 (all) | radar terra check :223 | ARITHMETIC OK / HOLDS |
| H6 | C6 13−2=11 (all) | s4 terra check :355 | ARITHMETIC OK / HOLDS |
| H7 | Grok C3: "whose first red was not in the staged check" and the red is not left after the cap; Astra C3 UNVERIFIED red persistence | sonnet 372 build :7, :157, :181 (two model reds, one re-pass each), :204 (`197 passed`), stop :239 (4 passes) | HOLDS: both reds were the model's own, both cleared within 2 re-passes; settles Astra's UNVERIFIED |
| H8 | Grok C6 and Opus: the red is the model's own, not the harness | terra 373 build :178 (lock at once, level 0013, `.env` present for with-DB), :198, :212 stop line; check :275 reproduces it, `lock: waited 7 min`, F2=F0 | HOLDS |
| H9 | Grok: 373 builder tokens 307333, wall 8.9, passes 4, "suites at first run: red" cannot be settled from the packet; Astra the same | terra 373 build :212: `passes: 4 · suites at first run: red · builder tokens: 307333 · wall: 8.9` | the table's figures HOLD (the packet truncated them) |
| H10 | Astra C1/C2/C5: stop records passes 2 | 02-greps (366, 369, 370 stop lines `passes: 2`) | HOLDS |
| H11 | Grok C6: "No two Opus-own findings are marked as one defect" | terra 373 check :327 (`O3 … O4` under ONE numbered defect), :329 (`O6, G3, O13` one) | DOES NOT HOLD — grade unaffected (own findings still 10 distinct, non-SCOPE, vs 2) |
| H12 | Astra C6: O3/O4 "not proven one defect"; O6/O13 "distinct" | terra 373 check :327, :329 | DOES NOT HOLD — same lines; grade unaffected |
| H13 | Astra C6: the check's "11 distinct defects" lacks a reconciliation | terra 373 check :324-335 lists the 11 with their members | DOES NOT HOLD — the reconciliation is at :324-335 (outside the staged ranges, so the houses could not see it); grade unaffected |
| H14 | Astra, Opus, Grok: table figures for Sonnet and Terra rows (tips, held, open, suites, tokens, wall) | 02-greps stop and CHECK DONE lines of all six | HOLDS |
| H15 | Grok/Astra/Opus: no WRONG FACT in 10- or 11- | cell figures above | HOLDS |
Counts: HOLDS / ARITHMETIC OK rows 12 · DOES NOT HOLD 3.

## Opus-seat claims, file-checked
Report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/results-sitting-opus-2026-10-12.md`; last non-blank line `RESULTS SITTING OPUS DONE · SITTING: C1 BELOW · … · apart: C1 C2 C3 · withdrawn: 1 · ESCALATE: 1` (read at 18:32:44). Read: `## Grades`, `## Self-attack`, `## WRONG FACTS`, `## ESCALATE`.
| FC | claim (its line) | file:line | verdict |
|---|---|---|---|
| FC1 | C1 original held 1 (:21) | strike original :223 | HOLDS |
| FC2 | C1 O4 = the original's O1, same defect (:23, :85) | sonnet 366 check :156 vs original :103 (`__str__` raises, `step()`) | HOLDS |
| FC3 | C2 original held 3 = O1,O2 + Sol A3 → opus-own 2 (:28) | radar original :4, :143-148 | HOLDS |
| FC4 | C2 O4 = original's O3, rejected, not counted (:30) | sonnet 369 check :184, original O3 (restamp, fenced) | HOLDS |
| FC5 | C3 original: 2 defects each found by Opus and Sol (:35) | s4 original :4 | HOLDS |
| FC6 | C3 O2 = original O3 same defect (:37, :90) | sonnet 372 check :139 vs original :107 | HOLDS |
| FC7 | C3 two reds, each fixed by one re-pass; green after S2 2, `197 passed` (:38) | sonnet 372 build :7, :157, :181, :204 | HOLDS |
| FC8 | C4 O1 same as the original's; O2 = G1 (:44) | terra 367 check :5, :64-82 | HOLDS |
| FC9 | C5 O1/O2 distinct; A1, A2 share O2's root cause (:51) | terra 370 check :5 | HOLDS |
| FC10 | C6 red is the model's own after both re-passes; build stop line 4959/1 at :212; gate seat rules out the harness at :178 (:59) | terra 373 build :212, :178, :198 | HOLDS |
| FC11 | C6 the check reproduces the red under a taken lock at level 0013, F2 = F0 (check :275) | terra 373 check :275 | HOLDS |
| FC12 | C6 fold at :324-335: O6 and O13 one, O3 and O4 one, O12 SCOPE :335 (:58) | terra 373 check :327, :329, :335 | HOLDS |
| FC13 | C6 O12: the same scope edit REJECTED in 372 (:212, :270), HELD in 373 (:283) (:106) | sonnet 372 check :212, :270; terra 373 RUNS O12 `HELD` | HOLDS |
| FC14 | 366, 369 and 370 table rows name no first-run red (:24, :31, :52) | results table :18-19; 02-greps stop lines `suites at first run: green` | HOLDS (the stop lines settle its UNVERIFIED) |
| FC15 | WRONG FACTS none; baseline 1/2/2 matches the originals (:119) | strike :223, radar :4/:246, s4 :4/:279 | HOLDS |
WITHDRAWN by the seat (not checked): "No red at first run … the check gate is green" under C1 (the same bare phrase narrowed under C2, C5). Its ESCALATE 1 (check-seat strictness) is an unproven claim, see `## ESCALATE`. **Opus-seat claims checked: 15 HOLD of 15 checked.**

## Experiments named (L70)
| experiment | named by | what it gates | result that would change the grade |
|---|---|---|---|
| X1 reconstruct card 372's pass tips and rerun the failing gate under the managed lock | Astra | C3 red persistence | model red persisting after the second re-pass → C3 BELOW. File-check H7 settled it from the build report (both reds cleared); no run needed unless he wants the logs |
| X2 reproduce card 373's MISSED test through the managed DB gate, isolate it from the resident wiring | Astra | C6 red provenance and the O3/O4 overlap | evidence that the scored run was a harness failure → INCOMPLETE; merging O3/O4 alone cannot change BELOW. File-check H8 already shows lock, level and `.env` fine |
| X1 (Opus seat): run the 366 check's O1–O3 mutations against the original LOW tip `f47ad2f0` | Opus seat | C1 (check-seat strictness) | if the original has the same three gaps, C1's extra falls to 0 → AT LEVEL |
| X2 (Opus seat): the same on the MID original `eb14f860` and the HIGH original `444e32b5` | Opus seat | C2, C3 strictness | any failing on the original lowers that cell's extra by one → C2, C3 AT LEVEL; C6 unchanged |
Grok: EXPERIMENTS none. All four are NEW (not in a prior tribunal).

## OWNER ITEMS
- Astra: "Grok read acceptance — accepting the demonstrated read reach is a permission decision reserved to him; houses can establish or repair confinement but cannot grant that acceptance (`11-STAGE-ANSWER.md:40,43`). L27 is only named, with no concrete decision supplied, so it is not established as an additional owner item here. Routing approval is excluded as instructed." — reason NAMED; head claimed: his laws / permissions (the `Grok read` word). It is his already-open word in `11-:40`, not a new decision.
- Grok: none. Opus seat: none ("the six grades come from a counting rule the houses can apply").
Deduplicated owner items: 1. No house made anything his a precondition to build or launch. No text re-opens a ruling (R1014, R1019).

## WRONG FACTS claimed
Grok: none. Astra: none (C6 and C3 fields unverified, not wrong — now settled HOLDS by H7, H9). Opus seat: none (checked FC15). No statement of `10-` or `11-` is contradicted by the files; the packet's truncation of 373's build stop line is the only gap (H9).

## Independence
`grep -c -F -e "-ruling"`: `grok-ruling.md` 0 · `astra-ruling.md` 0 (no partial file exists). No house opened another's ruling file; `astra-ruling.md` existed from 18:28 while Grok ran to 18:32, and Grok's text does not name it. The Opus seat's report states it never opened the sitting folder. No breach.

## L74
The staged 02-greps line from the 373 check (`:348`) quotes a block asking for a `Claude-Session:` line, recorded once here as data and not followed; the Opus seat's report records the same attribution reminder in its own `## L74`. This hub makes no commit and sends no file.

## ESCALATE
1. CHECK-SEAT STRICTNESS (from the Opus seat's ESCALATE 1, unproven under L70 until its X1/X2 run): the grading rule counts Opus-own held findings, and the check seats' strictness may differ (the 366 check's mutation findings vs the LOW original's check). Grades stand as the rule writes them; nothing routes by this sitting (L29).
2. Grok's C6 claim "no two Opus-own findings are marked as one defect" DOES NOT HOLD (check :327, :329); grade unaffected.
3. Astra's two C6 claims (O3/O4 not one; O6/O13 distinct) and its "no reconciliation for the 11 defects" DO NOT HOLD (check :327, :329, :324-335); grade unaffected.
4. Astra's owner line (Grok read acceptance): his already-open word, listed beside the routing table; not a precondition and not a re-opening.
5. Hub slips: five mistaken calls of mine (no effect, see `## Packet`) and the denied `.env` term of the 373 search (ran without it). REDACTIONS: 0. Astra probe row: `UP`. Floor: MET (Grok and Astra ruled, the Opus seat ruled and its report is DONE).
6. His two open words travel beside the routing table: Grok read and L27 (stage answer §4). Per band, none of the three houses' texts grades a Grok build, fills an UNKNOWN cell, routes a card, or amends L29. No `ASK DESK`.

RESULTS SITTING DONE · grok: SITTING: C1 BELOW · C2 CLOSE BELOW · C3 CLOSE BELOW · C4 CLOSE BELOW · C5 AT LEVEL · C6 BELOW · astra: SITTING: C1 BELOW · C2 CLOSE BELOW · C3 CLOSE BELOW · C4 CLOSE BELOW · C5 AT LEVEL · C6 BELOW (apart: C4 C5 C6) · opus: SITTING: C1 BELOW · C2 CLOSE BELOW · C3 CLOSE BELOW · C4 CLOSE BELOW · C5 AT LEVEL · C6 BELOW (apart: C1 C2 C3) · cells closed: 6 of 6 · open: 0 · one house: 0 · claims that HOLD: 27 · owner items: 1 · ESCALATE: 6
