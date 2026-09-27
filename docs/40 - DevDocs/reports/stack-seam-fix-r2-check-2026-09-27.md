# Stack Seam Fix R2 Check — 2026-09-27 (round 3 of ≤3, the last, L39)

## §0 Headline
- Checked `48`'s report-only fix r2 build report (`c501e025` on `deploy/stacked-0925`, tree unchanged at `41c9c962`) — round 3 of ≤3, the last (L39).
- AUTHORIZATION + PREFLIGHT: all pass. Seats: Opus 5.5, Sol, Grok all UP and all answered.
- Status: DONE. `defects that HOLD: 0` · **ready for the gate: YES** · ESCALATE: 7 (all information-only / UNVERIFIABLE FROM READS).

## L74
None arrived — no tool result in this run asked for a `Claude-Session:` line or named a file-send tool.

## PREFLIGHT
| rule | command | exit | allowed/DENIED + reason |
|---|---|---|---|
| placeholder gate 1 | `grep -n -E "R_[_]" ".../49-stack-seam-fix-r2-check.md"` | 1 | allowed — no hits |
| placeholder gate 2 | `grep -n -F "FILL AT LAUNCH" ".../49-stack-seam-fix-r2-check.md"` | 0 | allowed — only the gate's own describing line (33) hit |
| grok gate R17 | `grep -n "^| R17 " cto-2026-09-24.md` | 0 | allowed — row present, "Grok approved with no asking going forward" |
| grok gate R17 commit | `git log -1 -S"Grok approved with no asking going forward" -- cto-2026-09-24.md` | 0 | allowed — `1758fd78a572f47b613b2ca831dcfa636ed8f65a` |
| grok gate R19 | `grep -n "^| R19 " cto-2026-09-24.md` | 0 | allowed — row present, "All 4 house models approved for use indefinlitly" |
| grok gate R19 commit | `git log -1 -S"All 4 house models approved" -- cto-2026-09-24.md` | 0 | allowed — `5055151dbf68899b82de5b11f99733ed2d03048c` |
| launch row R9 | `grep -n "^| R9 " cto-2026-09-27.md` | 0 | allowed — names `49-stack-seam-fix-r2-check.md`, carries `<build stop>` and ceiling 300,000 B |
| launch row R9 commit | `git log -1 -S"49-stack-seam-fix-r2-check.md" -- cto-2026-09-27.md` | 0 | allowed — `08ce2fbbc4392989956221c6b2219675f11ce0f9` |
| fix r2 stopped BUILT | `tail -n 3 stack-seam-fix-r2-build-2026-09-27.md` | 0 | allowed — last non-blank line equals `<build stop>` verbatim |
| fix r2 report on gate branch | `git log -1 --format=%h deploy/stacked-0925 -- stack-seam-fix-r2-build-2026-09-27.md` | 0 | allowed — `c501e025` |
| gate branch tip | `git log --oneline -1 deploy/stacked-0925` | 0 | allowed — `c501e025 docs(stack-seam-fix-r2): …` |
| gate branch ~1 | `git log --oneline -1 deploy/stacked-0925~1` | 0 | allowed — `52540593 docs(stack-seam-fix-r1): …` |
| gate branch ~2 | `git log --oneline -1 deploy/stacked-0925~2` | 0 | allowed — `41c9c962 fix(jobs): …` |
| `date` | `date` | 0 | allowed — `Sun Sep 27 14:06:29 EDT 2026` (after 2026-09-26 06:47 ET — Sol expected) |
| grok gate (version) | `grok --version` | 0 | allowed — `grok 1.0.25 (f7e67d6988e2) [stable]` — UP |
| opus probe | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` | 0 | allowed — `OK` — UP |
| sol probe | `codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only -c model_reasoning_effort="high" "Reply with only the word OK." < /dev/null` | 0 | allowed — `OK` — SEATED |
| astra | — | — | NOT A SEAT (L67 R95: fix round = Opus · Sol · Grok) |
| branch shape | `git log --oneline --first-parent 2b71fe49..deploy/stacked-0925` | 0 | allowed — 9 lines, exact match: `c501e025 52540593 41c9c962 57420087 a7296b44 00e2b7ff 91c631ac 35397ed5 f2377218` |
| gate sha stat | `git show --stat c501e025` | 0 | allowed — exactly `.../reports/stack-seam-fix-r2-build-2026-09-27.md`, 1182 insertions |
| fix stat | `git show --stat 41c9c962` | 0 | allowed — exactly `configs/cobalt/jobs.yaml` and `tests/cobalt/test_jobs_reads.py`, unchanged since round 2 |
| stagger | `grep -n -F "no other house hub is running" cto-2026-09-27.md` | 0 | allowed — R9 row, names `49-stack-seam-fix-r2-check.md` |
| recovery | `ls scratch/tribunal-bars-0920/stack-seam-fix-r2-0927` | 1 | allowed — "No such file or directory" = fresh run |

FAIL CLOSED check: three seats UP (Opus, Sol, Grok) — well above the floor of two, with Grok and Sol both among the answering non-author houses.

## Packet
Staged in `scratch/tribunal-bars-0920/stack-seam-fix-r2-0927/` (agy-trial worktree): `48-fix-r2-build.part1-4.md` (14,998+6,714+12,839+9,781 B), `fix-r2-report.part1-7.md` (14,671+14,669+14,808+14,706+14,697+12,899+2,603 B), `range.md` (2,027 B), `claims.md` (4,223 B), `laws.md` (6,246 B), `greps.part1-2.txt` (14,376+14,250 B), `QUESTIONS.md` (5,945 B). Sum of measured parts (`wc -c`): **180,452 B** — well under the CEILING **300,000 B** (R87/R88 measured, not estimated). 180,452 B ÷ 4 ≈ 45,113 tokens estimated per checker (each reads the whole packet). Every part verified byte-identical against its source via diff before staging (48-parts, fix-r2-report-parts, laws.md sections all diffed clean against source; range.md/claims.md/greps built directly from live command output/Read).

## CONTINUE
DONE. All three seats returned (Opus 14:29, Sol 14:30, Grok 14:44 EDT), each ending `CHECK: FIX STANDS · ready for the gate: YES` with no blocking claim. §3/§4 collated below; stop line written.

## Per question
`walked: YES` for every cell below — each seat cited both a first and last line for all four U1 lists, U2's stat/numstat bounds and summary, the pass-1/pass-2 command lines, the first-parent log + gate-sha stat, and both `cobalt_redactions` reads.

| Q | opus | sol | grok |
|---|---|---|---|
| (i) | YES — 14·49·50·60 paths, each (b) `(nothing, exit 0)`; U2 first `R:289`, last `R:450`, summary `R:451`; numstat first `R:461`, last `R:620`, count 157 (`opus-check.md`) | YES — same four ranges cited (`:45`–`:265` bounds); U2 first `:289`, last `:450`, summary `:451`; numstat first `:461`, last `:620` (`sol-check.md`) | YES — same bounds, with per-branch counts re-derived (14/49/50/60) and split points (80+77, 56+24+77) shown (`grok-check.md`) |
| (ii) | YES — pass-1 `R:697`(=P48:108), pass-2 `R:824`(=P48:113 byte for byte), pass-2 summary `9 passed …` `R:826` | YES — pass-1 `:697`, pass-2 `:824`, summary `:826` | YES — pass-1 `report:697` (8 `--deselect` naming 9 tests), pass-2 `report:824`, summary `report:826` |
| (iii) | YES — log `range.md:16–19`; stat ONE path `range.md:11–12`; `R:6`,`R:1168` no-edit statement; RESTARTS `R:1121`; UNCLASSIFIED `R:1123`; stop `R:1182` | YES — log and stat from supplied `range.md`; no-edit `:1168`; RESTARTS `:1121`; UNCLASSIFIED `:1123`; stop `:1182` | YES — log/stat as above; no-edit `report:6`,`:1168`; RESTARTS `report:1121`; UNCLASSIFIED `report:1123`; stop `report:1182` |
| (iv) | YES — full ordered chain `R:639`→`R:900`, offline `R:634–636`, all before stop `R:1182` | YES — same chain `:639`→`:900`, offline `:636`, all before `:1182` | YES — same chain, tabulated `report:639`→`report:900`, offline `report:635–636`, all before `report:1182` |
| (v) | writer = `tests/cobalt/test_redact.py` (grep names only it); which of its two `mattermost` calls (`:401`,`:421`) wrote row 1283 is UNVERIFIABLE FROM READS — not a defect (L70) | same: writer file identified `test_redact.py`; which call is unsettled, not a defect | same: WRITER line `report:734` names `test_redact.py`; `:401`/`:421`; remainder not a defect (L70) |

## Checked against the files
No seat raised a claim that anything is wrong, dropped, weakened, changed, unproven or would fail — all three converged on `CHECK: FIX STANDS · ready for the gate: YES` with zero blocking findings. Nothing here HOLDS as a defect. I still verified (i)–(iv) myself, independent of the seats, directly against the real files:

(i) THE SHAPE — `git -C /Users/cobalt/cobalt show --stat c501e025` names exactly one path (`docs/40 - DevDocs/reports/stack-seam-fix-r2-build-2026-09-27.md`, 1182 insertions) — confirmed in my own PREFLIGHT row. `git -C /Users/cobalt/cobalt log --oneline --first-parent 2b71fe49..deploy/stacked-0925` printed exactly nine lines, newest first: `c501e025`, `52540593`, `41c9c962`, `57420087`, `a7296b44`, `00e2b7ff`, `91c631ac`, `35397ed5`, `f2377218` — confirmed in my own PREFLIGHT row. `git -C /Users/cobalt/cobalt show --stat 41c9c962` names exactly `configs/cobalt/jobs.yaml` and `tests/cobalt/test_jobs_reads.py` — confirmed in my own PREFLIGHT row. **HOLDS (as a positive fact, not a defect) — blocks the gate? no.**

(ii) NO ELLIPSIS OF THE REPORT'S OWN — from `greps.part1.txt`: `grep -n -F "×"` → zero hits; `grep -n -F "identical in shape"` → zero hits. `grep -n -F "…"` hits are at report lines 640, 646, 687, 695, 710, 735, 742, 798, 804, 820, 828, 848, 850, 894, 1140, 1153, 1177 — all outside the U1 list ranges (43–280) and outside the U2 stat block (289–450); every one is either the `ls -la …/.env` shorthand in prose or a `git`'s own `.../` path abbreviation, never inside a quoted U1 list. **HOLDS — blocks the gate? no.**

(iii) THE COUNTS, independently re-derived from the real file (not the packet copy), `sed -n` + `wc -l` on `/Users/cobalt/cobalt-wt/stacked-0925/docs/40 - DevDocs/reports/stack-seam-fix-r2-build-2026-09-27.md`: U1 replay `:45`–`:58` = 14 lines; H1 `:71`–`:119` = 49 lines; stale `:136`–`:185` = 50 lines; voice `:206`–`:265` = 60 lines (all EXPECTED counts, exact). U2 `--stat` path lines `:289`–`:450` (excluding the 4 structural `part`/fence lines) = 157 lines matched by `grep -c '|'`, plus the summary line ` 157 files changed, 15263 insertions(+), 165 deletions(-)`. U2 `--numstat` `:458`–`:622` = 157 lines matched by `grep -cE '^[0-9]+\t[0-9]+\t'`. **HOLDS — blocks the gate? no.**

(iv) THE DERIVED LINE — report `## RESTARTS` (`:902`) last table line `:1121` reads `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar`; the stop line `:1182` carries the identical field `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar` — byte for byte equal. **HOLDS — blocks the gate? no.**

No seat contradicted another on any question.

## FOR THE DESK
None — no claim HOLDS as a defect, and no seat's answer was `INPUT NOT WALKED`.

## ESCALATE
1. UNVERIFIABLE FROM READS (question v, all three seats + my own read): the `cobalt_redactions` row added during pass 1 (id 1283, `channel=mattermost`, `pattern=jwt`) is written by `tests/cobalt/test_redact.py`, but which of that file's two `channel="mattermost"` calls (`:401`, `:421`) committed it cannot be settled from reads. Settling command: `COBALT_ENV=dev uv run pytest -q -p no:cacheprovider tests/cobalt/test_redact.py` with a `cobalt_redactions` read before/after (as Opus's ESCALATE 1 and Sol/Grok's (v) both note). Not a defect (L70).
2. Opus's ESCALATE (its own file, informational, none blocking): (a) U1 (b)'s excluded-path argument list is described rather than printed for H1/stale/voice — the prompt (P48:91) did not require it printed, and Opus independently re-derived and checked each list; (b) the redaction id gap (1270→1283 against a +1 row count) is unexplained but consistent with sequence ids consumed by rolled-back inserts — settling command named in `opus-check.md` ESCALATE 3; (c) the builder's own final-chat-message HEAD checks are not reproduced in the report body, but `range.md` proves the same facts independently.
3. No `ASK DESK` was needed — every seat answered with a `CHECK:` line on the first attempt; no relaunch.
4. No L74 block arrived from any seat or any tool result during this run.
5. Sol seated and answered (probed UP at 14:06 EDT, after the 2026-09-26 06:47 ET gate); Astra: NOT A SEAT (L67 R95: fix round = Opus · Sol · Grok).
6. No fold for `42`/`46` beyond what `48`'s own `## FOR THE CHECK` already carries — nothing here changes it.
7. **Round 3 of ≤3 — THE LAST (L39; L67 other check: Opus 5.5 · Sol · Grok, R95; Gemini out, R97). `ready for the gate: YES` → `46` (`42` re-issued with `43`'s `## FOR 42` and `47`'s deltas) launches its GATE PHASE on the lock after this report is committed, and re-proves the three suites on the tree that ships (L68). A HOLD that blocks → NO fourth round: the desk brings it to Dejan as ONE item (L39), with FALLBACK B (replay + H1 only, `42` re-issued) as the named alternative (`cto-2026-09-25.md` R66 (3)(f)).**

STACK SEAM FIX R2 CHECK DONE · round: 3 · opus: CHECK: FIX STANDS · ready for the gate: YES · sol: CHECK: FIX STANDS · ready for the gate: YES · grok: CHECK: FIX STANDS · ready for the gate: YES · defects that HOLD: 0 · ready for the gate: YES · ESCALATE: 7
