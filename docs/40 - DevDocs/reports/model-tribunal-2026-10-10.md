# MODEL TRIBUNAL R1 — hub report (model-tribunal-1010)

## §0 Headline
- RULED: 18 items + (a)(b)(c) by Astra, Gemini, Grok (+ blind Opus seat, file-checked). Counted verdicts: 0 REJECT; every item ADOPT or ADOPT WITH. Closing lines: Astra ADOPT AFTER · Gemini ADOPT · Grok ADOPT AFTER · Opus seat ADOPT AFTER. Floor: MET (3 of 3 outside houses ruled).
- Opus-seat claims checked: 12 HOLD of 12 checked (2 WITHDRAWN by the seat, not checked). Grok's APART rulings counted: 0. Redactions: 1 (a client network address in `16-cards.excerpt.md`).
- DEFECT TO FIX: `gemini-ruling.md` is a STUB (my byte copy of Gemini's answer was stopped by a safety classifier). Gemini's full answer is intact in a task output file named in the stub and under `## ESCALATE`. Gemini's verdicts below are read from that output.
- ESCALATE: 9. Owner items: 0. This tribunal changes no model and no law.

## AUTHORIZATION
All run by the hub, each its own call (2026-10-10, ~16:5x ET):
- R919 `cto-2026-10-10.md:30` carries `model tribunal starts now`; R920 `:29` carries `only the model tribunal uses OpenAI`; R921 `:28` carries `model tribunal unchanged`; R908 `:41` carries `ONE OpenAI seat at a time` (rows have since moved; content unchanged). Each committed (`2542f686…`, R908 `fcded711…`).
- R109 `cto-2026-09-22.md:56` `Make all Opus 5.5 for now`; R95 `cto-2026-09-23.md:103` `only use Fable, Astra, and Grok for new designs`; R97 `:105` `unless it's a fourth`; R17 `cto-2026-09-24.md:35` and R19 `:37` (the grok / agy / astra gates) — all found; R17 `1758fd78…`, R19 `5055151d…` committed.
- His ruling block in `brain-direction-2026-10-02.md` committed (`ecfc36ec…`).
- Proposal done and committed: stop line `COMPLEXITY R2 PROPOSAL DRAFTED · decisions: 1`; proposal r2 and report r2 `17ef6b09…`; round 1 `a0ecdce4…`. Prompts 270 / 271 / 272 committed (`7c89f94e…`).
- Launch row `cto-2026-10-10.md:8` (R942) names 270 and carries `proposal: complexity-routing-proposal-r2-2026-10-10.md`, `Fable seat: yes`, `derive seat: claude-opus-5-5`, `gemini: sits`, `grok runs: 0 of 3`, `openai seat: free`; committed (`3fa4a0f9…`). No newer seat-changing row.
- Launch line adds no rule: all 14 allow and 3 deny strings counted ≥1 in `258-f4-tribunal-r2.md`; no Sol / Opus checker string.
- Verdict: AUTHORIZED.

## PREFLIGHT
| # | rule · command | exit | result |
|---|---|---|---|
| 1 | `date` | 0 | Sat Oct 10 16:55:52 EDT 2026 |
| 2 | R17 grep (grok gate), re-run 17:03 | 0 | allowed |
| 3 | R19 grep (agy / astra gate), re-run 17:03 | 0 | allowed |
| 4 | STAGGER from launch row: `grok runs: 0 of 3`, `openai seat: free` | 0 | allowed |
| 5 | slug `gpt-6-astra` in models cache | 0 | count 1 |
| 6 | Codex probe (background) | 0 | `OK`, 2,382 tokens → `astra: UP` |
| 7 | `grok --version` | 0 | grok 1.0.25 |
| 8 | `agy --version` | 0 | 1.3.3 |
| 9 | `ls scratch/tribunal-bars-0920` | 0 | present |
| 10 | `ls …/model-tribunal/r1` | 1 | absent → fresh run |
Floor: astra UP · grok up · gemini up → MET.

## Packet
Folder `scratch/tribunal-bars-0920/model-tribunal/r1/`. No part files; every file < 38,000 B. All eleven sources read at their drafting size.

| staged | source (last commit) | `wc -c` | trailing-ws lines |
|---|---|---:|---:|
| `10-PROPOSAL-R2.md` | `reports/complexity-routing-proposal-r2-2026-10-10.md` · `17ef6b09` | 17,958 (= source) | 0 |
| `11-REPORT-R2.md` | `reports/complexity-propose-r2-2026-10-10.md` · `17ef6b09` | 3,697 (= source) | 0 |
| `12-PROPOSAL-R1.md` | `reports/complexity-routing-proposal-2026-10-10.md` · `a0ecdce4` | 12,405 (= source) | 0 |
| `13-REPORT-R1.md` | `reports/complexity-propose-2026-10-10.md` · `a0ecdce4` | 2,155 (= source; first Write was 5 B short, corrected before launch) | 0 |
| `14-rulings.md` | `brain-direction-2026-10-02.md:186-198` `ecfc36ec`; `cto-2026-10-10.md` R921/R920/R919/R908 `1a876850`; `cto-2026-09-22.md` R109 `6f4da5e9` | 4,953 | n/a |
| `15-checks.excerpt.md` | strike check `c754ba22`; radar `758c07c9`; s4-p1 `5fc1e9a4`; g7 `32f2550c` | 21,738 | n/a |
| `16-cards.excerpt.md` | cards `bc051c44` / `0deb06fc` / `d35d6841` | 4,437 | n/a |
| `17-hubs.excerpt.md` | BUILD-HUB and CHECK-HUB `987ab80d`; `ops/grok-sandbox.toml` `68ba8658` | 5,239 | n/a |
| `27-laws-excerpt.md` | `LAWS.md` (vault path, not a path of main) | 15,924 | n/a |
| `02-greps.txt` | nine searches | 26,340 | n/a |
| `01-QUESTIONS.md` | verbatim from 270 + file list | 10,431 | n/a |
| `00-READING-ORDER.md` | written last | 2,190 | n/a |

Packet total 127,467 B (≈ 31.9k tokens); MANDATORY 101,867 B. Under the 200,000 B ceiling; no cut. Excerpts (14–17, 27) are my Read → Write transcriptions of line ranges, anchors checked, none moved; only the four whole files were byte-compared.
REDACTION: `grep -c -F -e TSLA -e 372.82 -e 374.50` = 0 on all eleven files. One client network address in the radar card's WHY replaced by `[user data]` (1).
DISCLOSED DEVIATION: `02-greps.txt` search 8 omits 12 matches that were lines of the tribunal's own prompt files (270 ×5, 271 ×1, 272 ×6); stated in the file.
Not staged: any note of his, `Rules.md`, vault rows, `desk-launch.sh`, whole check reports and hubs, the memory folder beyond LAWS.md, Grok session summaries.

## CONTINUE
next: none — all steps done at 20:4x ET; only the desk's copy of Gemini's answer into `gemini-ruling.md` is owed (see ESCALATE 1).

## Clock
| time | trigger | running houses | action |
|---|---|---|---|
| 16:55 ET | preflight | none | started |
| 17:03:12 ET | before launch | none | second R17 / R19 gate greps pass |
| 17:03:24 ET | after launch | grok / gemini / astra 0 min | all three launched in one message; deadline 17:23 |
| 17:09:11 ET | notice (astra) | grok 6 · gemini 6 | astra exit 0, 68,633 tokens; `astra-ruling.md` written (final message, once; the Write tool strips trailing double-space line breaks) |
| 17:10:55 ET | notice (gemini) | grok 7 | gemini exit 0; copy attempt stopped by a classifier (see ESCALATE 1) |
| 17:13:45 ET | notice (grok) | none | grok exit 0, wrote `grok-ruling.md` itself (32,449 B) |
| 20:37:52 ET | desk message / collate | none | collate; all houses finished well inside 20 min, no TIMEOUT |
| 20:5x ET | Opus-seat step and close | none | see below |

## Rulings table
Verdict words only. A = Astra, Ge = Gemini, Gr = Grok (APART on S1, S5, S6, S9), Op = Opus seat. SELF: yes where a house marked it (all unmarked = no). Agreement is across the COUNTED outside houses that ruled it.

| item | A | Ge | Gr | Op | agreement | SELF (house: evidence) |
|---|---|---|---|---|---|---|
| S1 | ADOPT | ADOPT | APART | ADOPT | 2-0 ADOPT | A yes UNMEASURED; Op stake |
| S2 | ADOPT | ADOPT | ADOPT | ADOPT WITH (E0 baseline run, swap a base-red card) | 3-0 ADOPT; Op wording | none |
| S3 | ADOPT | ADOPT | ADOPT WITH (shadow check skips the Sol probe) | ADOPT | 2 ADOPT, 1 WITH | A yes UNMEASURED; Gr yes (checker record `15-checks.excerpt.md` strike `:129`, radar `:246`, s4 `:160`) |
| S4 | ADOPT WITH (separate scored / descriptive counts) | ADOPT | ADOPT | ADOPT | 2 ADOPT, 1 WITH | A yes (cites `15-checks` strike `:137`, radar `:158-163`, s4 `:155-158`); Gr yes (same); Op yes UNMEASURED |
| S5 | ADOPT WITH | ADOPT | APART | ADOPT WITH | A WITH, Ge ADOPT: SPLIT in wording | A yes UNMEASURED; Gr yes UNMEASURED slacks |
| S6 | ADOPT WITH | ADOPT | APART | ADOPT WITH | A WITH, Ge ADOPT: SPLIT in wording | A yes UNMEASURED; Gr yes UNMEASURED |
| S7 | ADOPT WITH | ADOPT | ADOPT WITH | ADOPT WITH | 2 WITH, 1 ADOPT | Gr yes UNMEASURED |
| S8 | ADOPT | ADOPT | ADOPT | ADOPT | 3-0 | none |
| S9 | ADOPT | ADOPT | APART | ADOPT | 2-0 ADOPT | A yes UNMEASURED |
| Q1 | ADOPT | ADOPT | ADOPT | ADOPT | 3-0 | none |
| Q2 | ADOPT WITH | ADOPT | ADOPT WITH | ADOPT WITH | 2 WITH, 1 ADOPT | none |
| Q3 | ADOPT | ADOPT | ADOPT | ADOPT | 3-0 | A yes UNMEASURED |
| Q4 | ADOPT WITH | ADOPT | ADOPT | ADOPT | 2 ADOPT, 1 WITH | none |
| Q5 | ADOPT WITH | ADOPT | ADOPT WITH | ADOPT WITH | 2 WITH, 1 ADOPT | A yes UNMEASURED |
| Q6 | ADOPT WITH | ADOPT | ADOPT | ADOPT WITH | 2 ADOPT, 1 WITH | A yes UNMEASURED; Op yes UNMEASURED |
| Q7 | ADOPT WITH | ADOPT | ADOPT WITH | ADOPT | 2 WITH, 1 ADOPT | none |
| Q8 | ADOPT WITH | ADOPT | ADOPT | ADOPT | 2 ADOPT, 1 WITH | none |
| S11 | ADOPT WITH | ADOPT | ADOPT | ADOPT WITH | 2 ADOPT, 1 WITH | A yes UNMEASURED; Op yes UNMEASURED |
| (a) fact base | scores 2/5 verified, 13 UNVERIFIED; held and Opus-own counts HOLD; R1 total / median wrong | all HOLD; scores 2/5/13 right | s4-p1 score 9 (13 not held), counts HOLD | strike 1, radar 5, s4-p1 ≥7; "first gate" does not hold | SPLIT on the three scores | — |
| (b) fairness | lists leak and attribution risks | no leak identified | the gate's SHADOW-INSTRUCTIONS text is the largest lever | same; adds mutation asymmetry | all name the instructions file | — |
| (c) laws | no model-below-Opus write path; dontAsk is L29-by-launcher | none; dontAsk real | none; dontAsk real (launcher rule) | none; plus Grok repo-write scope not in the standing list | no objection to the R411 stop | — |

closing line row: Astra `TRIBUNAL R1: ADOPT AFTER Fold the replacements, correct arithmetic, and specify attribution and permission experiments in SHADOW-HUB.` · Gemini `TRIBUNAL R1: ADOPT` · Grok `TRIBUNAL R1: ADOPT AFTER bar drops Grok rows; check skips Sol; no gate hints` · Opus `TRIBUNAL R1: ADOPT AFTER fixing the gate, scoring and Grok-scope seams named in S2, S5, S11`.

Counted verdict totals (Astra + Gemini on all 18; Grok on the 14 counted): REJECT 0.
HOUSE PENDING: none (on S1, S5, S6, S9 both Astra and Gemini ruled).

## Grok, recorded apart (S1, S5, S6, S9)
Not counted anywhere; Grok's APART rulings counted: 0.
GROK — APART, NOT COUNTED (his R919, self-interest):
- S1: ADOPT (SELF: yes, UNMEASURED). Text: `grok-ruling.md:11-17`.
- S5: ADOPT WITH — bar counts Opus-own rows only; named keys `opus_held_slack`=1, `distinct_slack_at`=1, `distinct_slack_close`=3 labelled modelled; any SCOPE break is BELOW; a green-before-fix test demotes AT LEVEL. Text (verbatim): `grok-ruling.md:45-53`.
- S6: ADOPT WITH — cap 2 re-passes, gate never edits `src/` or `tests/`, an environment red scores nothing (`suites: environment`). Text: `grok-ruling.md:55-63`.
- S9: ADOPT (SELF: yes, UNMEASURED). Text: `grok-ruling.md:85-91`.

## Wording offered, verbatim
DEVIATION (disclosed): the full replacement wordings are long and the verbatim files are the sources; to avoid a second transcription error this section points to the exact verbatim text, per house, instead of recopying it. The derive reads these files whole.
- Astra (byte copy, `astra-ruling.md`, ITEM headings): S4 (ADOPT WITH §2.3 first four rows), S5 (§2.4), S6 (§2.2 step 6, §4 S6), S7 (§2.2 steps 3–5), Q2, Q4, Q5, Q6, Q7, Q8, S11 (§3 R411 stop, §4 S11).
- Gemini: no wording offered; every verdict ADOPT (full text: the task output file in ESCALATE 1).
- Grok counted items (`grok-ruling.md`): S3 `:29-31` (replacement for §2.2 step 8 and S3 default); S7 `:67-73`; Q2 `:103-109`; Q5 `:131-135`; Q7 `:149-153`. (S5 and S6 wording is APART, above.)
- Opus seat wordings are NOT copied here (the derive reads its report).

## Checked against the files
Real files opened by me. HOLDS / DOES NOT HOLD / UNVERIFIABLE FROM READS.
| # | claim · who | file:line | verdict | note |
|---|---|---|---|---|
| C1 | proposal's `s4-p1-check…:163-165` omits B1's REJECT at `:160` · Grok, Gemini, Opus | `s4-p1-check-2026-10-09.md:160,163-165` | HOLDS | :160 B1 REJECTED; :163-165 are B4, B3, B2 |
| C2 | R1 build total 5,569,914 (not 5,478,629) and median 195,971.5 (not ≈181,000) · Astra | `complexity-routing-proposal-2026-10-10.md:58-59` vs table `:29-54` | HOLDS | I re-summed the 26 builds: 5,569,914; middle values 194,339 and 197,604 → 195,971.5. ARITHMETIC OK. Gemini and Grok did not catch it |
| C3 | "only source that sat on every original" is literally false (Grok also sat) · Astra | `10-PROPOSAL-R2.md:31,37` | HOLDS | line 31 says Grok was house B on all three |
| C4 | strike `:129` reads "House B (Grok): no finding." not `FINDINGS: 0` · Gemini | `strike-fallback-env-check…:124,129,223` | HOLDS | text appears at :124 and :223 |
| C5 | unchanged CHECK-HUB seats Sol first when UP and probes Codex · Grok | `CHECK-HUB.md:23,65` | HOLDS | seat order OpenAI, Grok, Gemini; probe at :65 |
| C6 | BUILD-HUB line is 26 allow (4 file + 22 Bash), 4 deny · Astra, Opus, Gemini | `BUILD-HUB.md:12-14` | HOLDS | counted in the line |
| C7 | s4-p1 score = R5+S2+X2 = 9, 13 needs H4 · Grok (Opus: 7 from the card) | `10-PROPOSAL-R2.md:28`; card `72:14` | ARITHMETIC OK; H4 and X UNVERIFIABLE FROM READS | needs the drafter's launch row and R1 `:77-78` definition of X (seam shared with another open card) |
| C8 | strike card-field score is 1: card expects `com.cobalt.aset` only, radar is the builder's decision · Opus | `215-strike-fallback-env-card.md:46`; `strike…check:159` | HOLDS | the proposal's S2 uses the derived RESTARTS line |
| C9 | standing `Bash(grok *)` writes only under scratch, never the repo · Opus | `STANDING-LIST.md:98` | HOLDS | row text |
| C10 | prompt kind admits only auto|plan (`desk-launch.sh:454-456`) · Astra, Gemini, Grok, Opus | `desk-launch.sh:452-456` | HOLDS | grep lines 452,455,456 |
| C11 | `Bash(grok *)` and the four house strings are standing · Opus, Grok | `LAWS.md:321` | HOLDS | STANDING STRINGS clause |
| C12 | R920 / R921 override the CHECK-HUB seat text · Grok | `LAWS.md` L67 2026-10-10 lines (packet `27-laws-excerpt.md`) | HOLDS | lines read in the vault file |
| C13 | build tokens 761,148; checks 573,721; total 1,334,869 · Astra | `15-checks` BUILT / CHECK DONE lines | HOLDS | ARITHMETIC OK |
| C14 | at 30 per arm one outcome = 3⅓ points · Astra | arithmetic | HOLDS | 100 ÷ 30 |
| C15 | Opus Q5 steps: SE ≈ 0.073 per arm, ≈ 0.103 for the difference, P(|Z|>0.49) ≈ 0.62 · Opus | arithmetic | HOLDS | √(0.8·0.2/30)=0.0730; ×√2=0.1033; ARITHMETIC OK |
| C16 | s4-p1 BUILT line says `self-check: 2 of 3` · Grok | `s4-p1-check…:45` | HOLDS | read |
| C17 | live-vault test string and Vault add-dir in the build line · Astra | `BUILD-HUB.md:12` | HOLDS | present in the line |
| C18 | Gemini: omitting H would score s4-p1 at 9 · Gemini | `10-PROPOSAL-R2.md:28` | HOLDS | arithmetic 5+2+2 (if X counted) |
| C19 | R1 `:102` feeds JEV the score and `:140` says compare blind · Astra | `12-PROPOSAL-R1.md:102,140` | HOLDS | both lines read |
| C20 | Grok: R1 `:4` does not state "80%" for R8 · Grok | `12-PROPOSAL-R1.md:4,102,141` | HOLDS (text); what R8 actually said UNVERIFIABLE FROM READS | R8 not staged |
| C21 | CLI confinement, default effort `medium`, gate token cost, first-attempt suite history · Astra, Grok, Gemini, Opus | — | UNVERIFIABLE FROM READS | need experiments below (L70) |
Houses contradict each other: on s4-p1's score (Astra, Gemini accept 13 / Grok 9 / Opus ≥7); on S3 (Gemini and Astra and Opus: CHECK-HUB unchanged is enough; Grok: it still seats Sol first). I smooth neither.

## Opus-seat claims, file-checked
Run 20:4x ET; `tail -n 3` of `model-tribunal-opus-2026-10-10.md`: last non-blank line `MODEL TRIBUNAL OPUS R1 DONE · verdict: ADOPT AFTER fixing the gate, scoring and Grok-scope seams named in S2, S5, S11 · adopt: 10 · adopt with wording: 8 · reject: 0 · ESCALATE: 0`.
| FC | claim (Opus report) | file:line | verdict |
|---|---|---|---|
| FC1 | s4-p1 not green at the first gate (a W skip commit and a fix commit follow the build report) | `git log e4586978..2433078f` | HOLDS as a commit sequence (`f6e72c94 … W — skip …; build report`, then `2433078f … (W-1, S-1 …)`); that the W was red is the seat's inference from messages |
| FC2 | standing `Bash(grok *)` scope is scratch only | `STANDING-LIST.md:98` | HOLDS |
| FC3 | strike card expects `com.cobalt.aset` only | `215-…card.md:46` | HOLDS |
| FC4 | radar reach is the builder's DECISION | `strike…check:159` | HOLDS |
| FC5 | `desk-context.sh` prints CURRENT context size | `desk-context.sh:3-5` | HOLDS (that the BUILD `tokens:` fields use it is UNVERIFIABLE FROM READS) |
| FC6 | `card-fill.sh` refuses a BUILT line without `self-check: 3 of 3` | `card-fill.sh:5,70-71` | HOLDS |
| FC7 | `preflight.sh` status row requires `## <BRANCH>` (plus the report) | `preflight.sh:8-11,100,128` | HOLDS |
| FC8 | `LAWS.md:321` standing strings | `LAWS.md:321` | HOLDS |
| FC9 | B1's REJECT is at `:160` outside `:163-165` | `s4-p1-check…:160` | HOLDS |
| FC10 | BUILD-HUB 26 allow / 4 deny | `BUILD-HUB.md:14` | HOLDS |
| FC11 | prompt kind refuses all but auto|plan | `desk-launch.sh:452-456` | HOLDS |
| FC12 | Q5 noise arithmetic | steps | HOLDS (ARITHMETIC OK) |
Opus-seat claims checked: 12 HOLD of 12 checked. Two seat claims marked WITHDRAWN (the gate.sh untracked-file refusal; Gemini standing in for Sol) not checked. Its claims on `desk-launch.sh:917`, `:105-108`, `ops/desk/gate.sh:51`, the git log dates and the strike gate timings (621 s etc.) I did not open: UNCHECKED, not HOLDS.

## Experiments named (L70)
| experiment | named by | = proposal step | gates | result that would change the design |
|---|---|---|---|---|
| Grok CLI under `--sandbox cobalt-job`: writes only the glob; no shell command runs without `--always-approve`; denied homes / worktree `.env` unreadable | Astra X1, Gemini X1/X2, Grok X1, Opus X1 | §2.6 (new scope) | L29(2) permission gate | any write outside the worktree or a shell run: no shadow build launches |
| Cost of one Grok pass (messages, wall time, effort field) | Astra X2, Gemini X3, Grok X2, Opus X2 | §2.5 / S8 | cost unit | effort ≠ medium, or one pass near CHECK-HUB's 45 min |
| Gate-seat tokens on the LOW card | Gemini X4, Grok X4 | §2.5 | meter paragraph | far outside 300-450k modelled |
| Dev lock / schema level / BASE health before the with-DB suite (E0 on each BASE) | Grok X3, Opus X3, Astra X3 | NEW | S6 false BELOW, S2 card swap | base red or level ≠ 0013 |
| RED-FIRST / attribution rehearsal (green-before-fix, out-of-stage edit, untracked file) | Astra X4, Grok X7 | S7 | RED FIRST scoring | misclassification changes SHADOW-HUB |
| Known-answer replay on the frozen pre-check TIP | Astra X5 | T5 | replay | pass only after Opus repair |
| Review provenance (OWN findings before Grok list; pre/post-fix TIPs) | Astra X6 | §2.3 | comparability | contaminated check |
| Fresh-Opus run-to-run spread on one tip | Opus X5 | NEW | S5 tolerances | difference ≥ 2 widens AT LEVEL |
| Ignored path for SHADOW-INSTRUCTIONS.md | Opus X4 | NEW | check PREFLIGHT | no ignored path: add an rm string |
| Can headless Grok edit a large file without rewriting it whole | Opus X6 | NEW | tooling bias | whole-file rewrite on `PANEL_JS` |
| Launcher dry-run on the LOW card (current report paths, no Codex probe) | Astra X8 | S11 | launcher | stale pointers or a probe |
| CHECK-HUB dry reading against a shadow card that cites R920 | Grok X5 | S3 | S3 wording | file still launches Sol |
| radar red commit hash | Gemini X5, Grok X6 | T5 | known-answer set | recorded only |
| Suite isolation/restoration, live-note effects | Astra X3 | NEW | gate | restoration failure |

## OWNER ITEMS (after the tribunal)
Proposal `## 4`: no item is an owner item.
- Astra: "None of the eighteen items passes the owner test…" — names his laws (L29 amendment) but says it cannot be supplied by a house and is not a precondition. NAMED (laws). Not an item: it is the already-ruled word.
- Gemini: `none` — NAMED.
- Grok: `none` — NAMED (money, data, laws, trading judgement each addressed).
- Opus seat: `none`.
Deduplicated owner items: 0. No house made something his a precondition. No text re-opens R919–R921; each house states his rulings as inputs.

## WRONG FACTS claimed
| claim | who | my verdict |
|---|---|---|
| R1 §1.3 build sum 5,478,629 and median ≈181,000 are wrong (5,569,914; 195,971.5) | Astra | HOLDS (C2) |
| "only source" literal | Astra | HOLDS (C3) |
| `s4-p1-check…:163-165` omits B1 at `:160` | Gemini, Grok, Opus | HOLDS (C1) |
| strike `:129` cite for `FINDINGS: 0` | Gemini | HOLDS, minor (C4) |
| s4-p1 score 13 does not hold (9) | Grok | UNVERIFIABLE FROM READS (H and X) |
| strike score 2 should be 1 from the card | Opus | HOLDS (C8) |
| "all three originals BUILT on the first gate" | Opus | HOLDS as a commit sequence (FC1); red status inferred |
| "only existing strings" vs `STANDING-LIST.md:98` | Opus | HOLDS (C9) |
| stop-line `tokens:` are context sizes, not meter use | Opus | script text HOLDS (FC5); source of the build `tokens:` UNVERIFIABLE |
| R1 `:102,:141` credit 80% to R8 | Grok | HOLDS as text; R8's real wording not staged |
| literal scope metric vs the zero baselines | Astra | UNVERIFIABLE FROM READS (needs the check's scope verdicts and the gate list) |

## Independence
`grep -c -F -e "-ruling"`: gemini-ruling.md 3 (the stub, naming the file it stands in for and the task output), grok-ruling.md 5, astra-ruling.md 4 (`astra-ruling.partial.md` absent). I read every matching line: all hits are the packet file `14-rulings.md` ("-rulings"), or the stub's own text. No house opened another house's ruling file. No `READ ANOTHER RULING`.

## L74
none

## ESCALATE
1. `gemini-ruling.md` is a STUB: my byte copy of Gemini's answer was stopped partway by a safety classifier and I did not redo it. ASK DESK: copy lines 1-272 of `/private/tmp/claude-501/-Users-cobalt-cobalt-wt-agy-trial/f9872990-ddff-421e-98c3-23dc88d87405/tasks/b0bq2fwvv.output` into `scratch/tribunal-bars-0920/model-tribunal/r1/gemini-ruling.md` before the derive (272) runs; safe default: the derive treats Gemini's wording as unavailable. [20:4x ET]
2. `## Wording offered, verbatim` points to the verbatim files instead of copying the wordings (deviation named above); the derive must read `astra-ruling.md` and `grok-ruling.md` whole.
3. Figures that DO NOT HOLD (proposal / round 1): R1 build total and median (C2, only Astra caught it); `:163-165` range (C1); "only existing strings" (Opus WF2, C9); "all three originals BUILT on the first gate" (FC1); strike score 2 vs 1 (C8). The s4-p1 score 13 is UNVERIFIABLE (H, X).
4. Claim where houses split: CHECK-HUB unchanged seats Sol first (Grok C5) versus Astra/Gemini/Opus treating it as Grok house A — a wording seam for SHADOW-HUB.
5. SELF: yes with EVIDENCE UNMEASURED: Astra S1, S3, S5, S6, S9, Q3, Q5, Q6, S11; Grok S1, S5, S6, S7, S9 (S3 and S4 cite the checker record); Opus Q6, S11 (S4 UNMEASURED). Grok S3 / S4 cite `15-checks` ranges: HOLD as record, not as a measure of tier.
6. Numbers proposed without a measurement: Grok keys `opus_held_slack`=1, `distinct_slack_at`=1, `distinct_slack_close`=3, `weight_H`=0, `sonnet_ready_gap`=5, `jev_agreement`=80 (each labelled modelled by Grok); Astra's two-repair allowance (labelled UNVERIFIED pilot); Opus `sonnet_trial.margin_points` has no value by design.
7. Grok's four APART items, counted nowhere: S1 ADOPT · S5 ADOPT WITH · S6 ADOPT WITH · S9 ADOPT.
8. THE FLOOR: floor: MET (astra UP and ruled 18 of 18, gemini ruled, grok ruled; Opus seat report committed state not checked by me beyond its stop line). Astra's meter used 68,633 tokens; OpenAI counts as OUT after this run (R920).
9. Redactions: 1 (client network address in `16-cards.excerpt.md`).
No `DO NOT ADOPT`; no `REJECT`; no model-below-Opus write path HOLDS; no wording changes a model, seat or law by itself; no `RE-OPENS A RULING`; no independence breach.

MODEL TRIBUNAL R1 DONE · astra: TRIBUNAL R1: ADOPT AFTER Fold the replacements, correct arithmetic, and specify attribution and permission experiments in SHADOW-HUB. · gemini: TRIBUNAL R1: ADOPT · grok: TRIBUNAL R1: ADOPT AFTER bar drops Grok rows; check skips Sol; no gate hints (apart: S1 S5 S6 S9 not counted) · opus: TRIBUNAL R1: ADOPT AFTER fixing the gate, scoring and Grok-scope seams named in S2, S5, S11 · floor: MET · houses that ruled: 3 of 3 seated · claims that HOLD: 19 · dissents: 0 · owner items: 0 · ESCALATE: 9
