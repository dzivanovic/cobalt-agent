# F4 tribunal prompts 237 · 238 · 239 — preflight · 2026-10-10

Clock: Sat 2026-10-10 08:18 EDT. Read-only; no git write, no launch.

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff --stat HEAD -- prompts/2026-10-10` | empty (prompts match HEAD) | OK |
| 2 | `git log -1 --format=%H` on 237, 238, 239 | each `bea907be7c18386698e98c2ce0a12f80413a7081` (committed) | OK |
| 3 | `grep -c 'claude --bg "Read '` (the launcher's own count) on 237, 238, 239, 249 | 1, 1, 1, 1 | OK |
| 4 | `desk-launch.sh` `prompt` rules, read at `:410-546`: one launch line, no `<` or `>` in the launch span, one `cd` span (237 and the other two: `cd /Users/cobalt/cobalt-wt/agy-trial`, under `$WT`), mode `auto`, `--remote-control` before `--name`, deny list, no write string | all met on 237, 238, 239; 249 reads `cd /Users/cobalt/cobalt` | OK |
| 5 | `--add-dir` covers every absolute path in each launch line | Vault, cobalt, cobalt-wt; every path in the lines sits under one | OK |
| 6 | `grep -c -F` of 237's 14 allow strings, each with its quotes, on `2026-09-22/63-routing-tribunal.md` (14 calls) | 1 each | OK |
| 7 | `grep -c -F` of the deny trio `"AskUserQuestion" "EnterWorktree" "Bash(git push*)"` on 63 | 1 | OK |
| 8 | `grep -c -F` of 237's whole `--allowedTools … --add-dir` span on `2026-09-29/12-f15-tribunal.md` (the file the hub's own gate greps) | 1 (so all 14 allow + 3 deny count ≥1) | OK |
| 9 | same, 237 against itself | 1 | OK |
| 10 | `grep -c -F` of 238's seven allow, deny, `--add-dir` span on `2026-09-22/64-…-fable-seat.md` and on `2026-09-29/13-f15-tribunal-anthropic-seat.md` | 1 and 1 | OK |
| 11 | `grep -c -F` of 239's same span on `2026-09-22/65-routing-tribunal-derive.md` and on `2026-09-29/14-f15-derive.md` | 1 and 1 | OK |
| 12 | `grep -c -F` of the two checker strings (`gpt-5.6-sol`, `claude -p --model`) in 237's launch line | none in the line (the one hit is the prohibition text in the gate paragraph) | OK |
| 13 | `grep -c -F "gpt-6-astra"` on `STANDING-LIST.md` | 0 (it lists the Sol string only); the Astra string is in the template 63 and 12 byte for byte, check 6/8 | OK (see ISSUES N2) |
| 14 | `grep -c -F "gpt-6-astra" ~/.codex/models_cache.json` | 1 | OK |
| 15 | models: 237 `claude-sonnet-5-5`; 238 and 239 `claude-opus-5-5`; `claude-fable-5-1` appears only as "never" in 238 line 1 | as stated | OK |
| 16 | date gates: `grep -n "^| R17 "` / `"^| R19 "` on `cto-2026-09-24.md` | R17 `:35` carries `Grok approved with no asking going forward`; R19 `:37` carries `All 4 house models approved`; 237 states NO DATED GATE, nothing expires | OK |
| 17 | `grep -n "^| R849 \|^| R860 \|^| R866 "` on `cto-2026-10-10.md` | `:33` `S5 pulled forward`; `:22` `S5 tribunals use the 09-22 drafted shape`; `:16` carries `f4-tribunal-draft` | OK |
| 18 | `grep -n "^| R109 "` on `cto-2026-09-22.md` | `:56` `Make all Opus 5.5 for now`, `claude-opus-5-5`, `derive` | OK |
| 19 | `grep -n "^| R95 \|^| R97 "` on `cto-2026-09-23.md` | R95 carries `only use Fable, Astra, and Grok for new designs`; R97 carries `unless it's a fourth` | OK |
| 20 | `git log -1 -S"<literal>"` for R849, R860, R17, R19, R109 | `2ef44c84`, `ddaae952`, `1758fd78`, `5055151d`, `75b2aa57` (all committed) | OK |
| 21 | `git log -1` on the proposal, the seam doc, and `-S"F4 DESIGN DRAFTED"` on the drafter report | each `8426e8f5…` (committed) | OK |
| 22 | `grep -c -x -F "FABLE ROW: R109"` (238) and `"DERIVE ROW: R109"` (239) | 1 each (filled, not `R__`) | OK |
| 23 | round-1 stop lines: 237 §4 `F4 TRIBUNAL R1 DONE …floor: MET…`; 238 `F4 TRIBUNAL OPUS R1 DONE …`; 239 refuses unless both are present and committed and `floor: MET` | same words in all three; report paths `reports/f4-tribunal-2026-10-10.md` and `reports/f4-tribunal-opus-2026-10-10.md` identical in 237 §3, 238 and 239 | OK |
| 24 | seats: hub Sonnet 5.5; houses Astra and Grok, Gemini optional; blind seat and derive Opus 5.5; each house told not to open `-ruling` files; 238 forbids the houses' folder and the hub report | present in 237 §2, 238 "BLIND", 239 | OK |
| 25 | floor (proposer + two outside), 3-round cap (L39/L67), meter probe FIRST (L47), file-check of every converging claim and of the Opus seat's claims at collate (L35) | present in 237 preflight, §2, §3 | OK |
| 26 | LAWS headings the prompts cite (L1 L2 L3 L8 L10 L28 L29 L32 L36 L37 L39 L42 L43 L47 L48 L52 L53 L55 L58 L59 L60 L62 L63 L67 L68 L70 L71 L72 L73 L74 L75 L76) | all present; L72 text is the seam-document rule | OK |
| 27 | 21 questions vs the drafter's 15 decisions (`f4-design-2026-10-10.md:19-33`, C1–C12, S1–S3) | 237 `THE ITEMS` lists C1–C12, S1–S3 in the same order with the same text, plus (a)–(f) = 21 | OK |
| 28 | `wc -c` of the 15 packet source files vs the sizes 237 states | all 15 equal (daily.py 24,310 … daymode/note.py 9,770) | OK |
| 29 | `wc -c` proposal / seam / drafter report | 16,224 / 4,503 / 6,363 (equal to 237 §1) | OK |
| 30 | `git rev-parse d0a5fbb8`; `git diff --stat d0a5fbb8 HEAD -- src configs tests "docs/00 - Project" "docs/90 - References"` | `d0a5fbb8761a7ddf46b22310db4089eec32f8b27`; diff empty (no path moved) | OK |
| 31 | `ls` of every packet source: archiver/runner.py, heartbeat/runner.py, aset/daily_note.py, tunables.py, tunables.yaml, Charter, ladder, `90 - References/INDEX.md`, the desk reports, `-words.md`, `73-…`, `04-…`, `CHECK-HUB.md`, LAWS.md | all exist | OK |
| 32 | Charter anchors `:82` F4 and `:89` F5; ladder `:923` S5 and `:939` code prompts owed | `:82`, `:89`; `:923`, `:939` (a second `Code prompts owed` at `:918`, F4 row range `:921-941` still holds) | OK |
| 33 | `ls scratch/tribunal-bars-0920` | exists; no `f4-tribunal` entry (fresh run) | OK |
| 34 | packet names no personal content (L32): sources are committed code, config, designs, reports, ruling rows, LAWS; daily-note text, `Rules.md`, vault rows listed under NOT STAGED | none found | OK |
| 35 | derive: FINAL path `docs/30 - Design/F4-FINAL-<date>.md`; `## FOR DEJAN` one A/B per owner item, proposal default as A, houses named, NO recommendation (L37); owner items only if they pass the owner test | present in 239 | OK |
| 36 | the desk launch row | NOT YET WRITTEN: `grep -n -F "237-f4-tribunal.md"` on `cto-2026-10-10.md` prints nothing (draft decision D2; the prompts stop at preflight without it) | NOTE |

## ISSUES
- N1 NOTE: the launch row for 237 does not exist yet; the desk writes and commits it before launch (see LAUNCH ROW). 237, 238 and 239 each refuse without it.
- N2 NOTE: the Astra `codex exec … gpt-6-astra …` string is not on `STANDING-LIST.md` (it lists Sol); it is in `63` and `12` byte for byte and on his R19, which the prompt cites. Passes by the template rule.
- N3 NOTE: 237 §1 sends the hub to `73` §1 for its REDACTION command, which is `grep -c -E "TSLA|372[.]82|374[.]50" <file>` (`73-s3-exits-tribunal.md:14`). That is alternation inside one pattern, against 237's own PATTERN RULE. A permission check may deny it, and the hub then has no redaction proof. Three `-e` options with `-F` would meet both. The hub does not run it unless it gets that far.
- N4 NOTE: `CHECK-HUB.md:92` and `STANDING-LIST.md` still spell Gemini `gemini-3.1-pro-high`; 237 pins `gemini-3.8-flash-high` (his 10-03 R6, draft D1). Unproven under that spelling; a refusal is recorded HARNESS, never retried.
- N5 NOTE: the floor is stricter than L67's text (`LAWS.md:342`: shrink "never below TWO houses"). R860 sets it; draft D3.
- N6 NOTE: 239 requires exactly ONE row naming `237-f4-tribunal.md` in `cto-2026-10-10.md`. The desk's later rows, this preflight's row included, must not repeat that literal (write "the F4 tribunal hub" instead), or 239 refuses.
- N7 NOTE: 237 reads `~/.codex/models_cache.json`, outside the `--add-dir` roots; `12-f15-tribunal.md` carries the same read and ran.

## LAUNCH ROW
One `| R<nn> |` row in `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md`, committed before launch, naming the file and carrying these literals (all three seats read this one row):
- `237-f4-tribunal.md`
- `f4-design-proposal-2026-10-10.md`
- `Fable seat: yes`
- `derive seat: claude-opus-5-5`
- one of `gemini: sits` or `gemini: not seated` (neither literal means not seated)
- `no other house hub is running` (237's STAGGER row; any other house hub the desk names needs `<nn> is not running` in a line that also names `237-f4-tribunal.md`)

No other row may name `237-f4-tribunal.md` (N6). No later row may name a different `derive seat:`.

PREFLIGHT DONE · prompts: f4-tribunal · checks: 36 · fails: 0 · ready: YES
