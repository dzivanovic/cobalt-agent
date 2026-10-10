# F4 round-3 tribunal prompts 278 · 279 · 280 — preflight · 2026-10-10

Clock: Sat 2026-10-10 16:58 EDT. Read-only; no git write, no launch, no probe. Prompts committed at `0891e083`.

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff --stat HEAD -- prompts/2026-10-10` | only `231-ops-hand-card.md` (not ours); 278, 279, 280 clean | OK |
| 2 | `git log -1 --format=%H` on 278, 279, 280 | each `0891e0839400e2c80abacc648f6eb72f00c6d937` | OK |
| 3 | launch row: `grep -n -F "278-f4-tribunal-r3.md"` in `cto-2026-10-10.md` | no row yet (the desk writes it before launch) | NOTE N1 |
| 4 | rows R849 :102, R860 :91, R903 :48, R917 :34, R920 :31, R931 :20, R932 :19 each carry the literal 278 greps (`S5 pulled forward`, `S5 tribunals use the 09-22 drafted shape`, `7 items need round 2`, `258-f4-tribunal-r2.md`, `only the model tribunal uses OpenAI`, `F4 round 3, last, narrowed`) | all present | OK |
| 5 | the draft's desk-row line numbers (R931 :8, R932 :7, R920 :19, R917 :22) against HEAD | HEAD has R931 :20, R932 :19, R920 :31, R917 :34; the rows are right, the numbers are not | NOTE N2 |
| 6 | `git log -1 -S` on `cto-2026-10-10.md` for R849 `2ef44c84`, R860 `ddaae952`, R903 `dcd29aaa`, R920 `2542f686`, R931 `ecfc36ec` | all committed | OK |
| 7 | R17 :35 `Grok approved with no asking going forward`, R19 :37 `All 4 house models approved` in `cto-2026-09-24.md`; `-S` commits `1758fd78`, `5055151d` | present, committed | OK |
| 8 | R95 :103 `only use Fable, Astra, and Grok for new designs`, R97 :105 `unless it's a fourth` (`grep -c -E` on `^\| R95 .*literal`, `^\| R97 .*literal`) in `cto-2026-09-23.md` | 2 | OK |
| 9 | R109 :56 `cto-2026-09-22.md` `Make all Opus 5.5 for now`; `grep -c -x -F` `FABLE ROW: R109` (279) and `DERIVE ROW: R109` (280) | row present; 1 and 1 | OK |
| 10 | his-words gate: R917, R920, R931 in `cto-2026-10-10-words.md` | no row (empty). 278 greps words only for R849 (its AUTHORIZATION cites `cto-2026-10-10-words.md` R849), none for R917/R920/R931 | NOTE N3 |
| 11 | allow-string proof: `grep -o -F` of the 13 allow + 3 deny strings (quotes included) on 258 and on 278 | each of the 16 prints once in 258 and once in 278; none new | OK |
| 12 | the 7 allow + 3 deny strings of the Opus-seat line on 259, 279, 280 | each prints once in each of the three files | OK |
| 13 | launch lines obey `desk-launch.sh prompt` rules (read at round 2 `:410-547`): one `claude --bg "Read '…' and follow it exactly."`, `cd /Users/cobalt/cobalt-wt/agy-trial` (278 `…/agy-trial`, exists), mode `auto`, deny pair, `--remote-control` before `--name`, no write string in the line | same shape as 258/259/260 (read lines 1 of 278, 279, 280); no `<`/`>` in the three lines; 278's span differs from 258 only by the dropped codex string, prompt path and name | OK |
| 14 | `--add-dir` Vault, cobalt, cobalt-wt in all three; every path sits under one | present | OK |
| 15 | models: 278 `claude-sonnet-5-5`; 279, 280 `claude-opus-5-5`; `claude-fable-5-1` in 279 only as "never" | as stated | OK |
| 16 | no Sol or Opus checker string in 278's launch line (`gpt-5.6-sol`, `claude -p --model`) | both appear only inside the gate's prohibition text (line 7); the launch line (line 1) has neither | OK |
| 17 | `grep -c -F "codex"` 278 | 4 (lines 1, 7, 9, 33): line 1 "`Bash(codex exec …)` string of 258 is DROPPED", line 7 "a `codex` string in your launch line → FAILED", line 9 "no `codex` command", line 33 "NO `codex` command in this file". Each a prohibition | OK |
| 18 | `grep -c -F "Bash(codex"` 278, 279, 280 | 1, 0, 0. The one hit is 278 line 1's sentence that says the string is dropped (not in the launch line) | NOTE N4 |
| 19 | Astra literal `NOT SEATED (reserved for the model tribunal, his R920)` and floor = Grok + Gemini in 278 | present in header, STAGGER, §3, §4 stop line; floor "BOTH Grok and Gemini" | OK |
| 20 | guard pattern `ops/desk/bare-guard.py:756` `(^|/)prompts/20[^/]*/[0-9]+-(?!draft)[a-z0-9-]*-tribunal(-r[0-9]+)?\.md$`, applied by hand | `278-f4-tribunal-r3.md` MATCHES (`278-` · `f4` · `-tribunal` · `-r3` · `.md`); `279-f4-tribunal-r3-opus-seat.md` and `280-f4-tribunal-r3-derive.md` do NOT (the end is not `-tribunal(-rN).md`) | OK |
| 21 | date gates: R17/R19 gates say NO DATED GATE; R17/R19 greps run again before the houses launch (278 PREFLIGHT rows 2-3) | present, no date in any gate | OK |
| 22 | meter probe first (L47): `date`, R17, R19, `grok --version`, `agy --version`, `ls scratch/tribunal-bars-0920`, `ls …/f4-tribunal/r3` | in that order in 278 PREFLIGHT; `scratch/tribunal-bars-0920` exists; `f4-tribunal` holds `r1`, `r2` only (r3 absent: a fresh run) | OK |
| 23 | round cap: round 3 of at most three (L39/L67), "THE LAST round, no round 4" | in 278, 279, 280 | OK |
| 24 | file-check of every converging claim, and of the Opus seat's claims from `FC45` | 278 §3 and `## Opus-seat round-3 claims, file-checked`; last FC row of round 2 is `FC44` at `f4-tribunal-r2-2026-10-10.md:222`, no `FC45` | OK |
| 25 | next numbers: `F-34` after `F-33` (r2 derive `:34`; `F-34` count in F4-FINAL = 0); `FC45` after `FC44` | both free | OK |
| 26 | stop lines and report paths agree: hub `F4 TRIBUNAL R3 DONE` at `reports/f4-tribunal-r3-2026-10-10.md`; seat `F4 TRIBUNAL R3 OPUS DONE` at `reports/f4-tribunal-r3-opus-2026-10-10.md`; derive `F4 DERIVED R3` at `reports/f4-tribunal-r3-derive-2026-10-10.md` | same literals in 278 §3-4, 279 REPORT/STOP LINE, 280 preconditions | OK |
| 27 | round-2 chain, committed: hub ends `F4 TRIBUNAL R2 DONE · … floor: MET` (`2542f686`); derive ends `F4 DERIVED R2 · FINAL WITH OPEN ITEMS (R2-4, R2-7)` (`c44612dd`); seat ends `F4 TRIBUNAL R2 OPUS DONE` (`2542f686`); `OPEN AFTER ROUND 2` count in F4-FINAL = 10; F4-FINAL committed `c44612dd` | all as 278 requires | OK |
| 28 | the two questions are exactly R2-4 FORM and R2-7 clean wording of `## OPEN AFTER ROUND 2` of `f4-tribunal-r2-derive-2026-10-10.md` `:38-60` (the prompt says `## NEEDS ROUND 2`; that heading is not in this report) | R2-4 (Gemini omit vs Grok include; the form is the Opus seat's third form), R2-7 (A Gemini quoted at :52); nothing else asked | OK, NOTE N5 |
| 29 | hub rows the draft cites against `reports/f4-tribunal-r2-2026-10-10.md`: R2-F7 :168, F8 :169, F9 :170, F10 :171, F22 :183, F23 :184, F24 :185, F25 :186, F26 :187, FC27-FC30 :205-208 | each at its line; content matches the prompt's use | OK |
| 30 | code cites at `d0a5fbb8` (code unchanged since: `git diff --stat d0a5fbb8 HEAD -- src configs tests "docs/00 - Project"` shows tests only, no packet path): `strike/detector.py:99` `IntervalRefused`, `:103-108` `poll_interval` (the draft says :99-105; the prompt says :99-108), `:111-117`, `:273-279`; `prefill/daily.py:14-24`, `:463-473`, `:573-588`, `:578-582`; `prefill/config.py:130-139`, `:37-48`; `daymode/note.py:238`; `aset/daily_note.py:103-104`, `:184`; `writer.py:588`, `:597-607` area, `:673`; `radar/notes.py:276`, `:329`, `:360-362`, `:384`, `:441` | each Read at its line and says what the prompt says | OK |
| 31 | `d0a5fbb8` | `d0a5fbb8761a7ddf46b22310db4089eec32f8b27` | OK |
| 32 | file sizes (`wc -c`): FINAL 59,172; r2 derive 20,489; r2 hub 46,284; `detector.py` 15,532; `radar/notes.py` 30,852; `daily.py` 24,310; `config.py` 6,006; `writer.py` 59,388; LAWS 75,127 | equal the draft's figures | OK |
| 33 | no seat holding a side recommends (L37): 278 "no verdict of your own"; 279 rules, never approves; 280 "you recommend nothing to him"; an open item goes to him as one A/B with no recommendation | present | OK |
| 34 | derive 280 refuses unless the hub, seat and r2-chain lines are present and committed, `floor: MET` and BOTH `grok:` and `gemini:` carry a `TRIBUNAL R3:` line; writes `docs/30 - Design/F4-FINAL-2026-10-10.md` | present | OK |
| 35 | packet names only existing files and no personal content (L32): `grep -c -E` on `TSLA`, `372[.]82`, `374[.]50` on 278, 279, 280 | 0, 0, 0; daily-note text, `Rules.md`, vault rows listed as NOT STAGED | OK |
| 36 | launch-row literals the hub greps for (see `## LAUNCH ROW`) | all nameable; the desk can write each before launch | OK |

## ISSUES
- N1 NOTE: no launch row names 278 yet. The desk writes and commits it before launch (see LAUNCH ROW); 278, 279 and 280 each refuse without it.
- N2 NOTE: the draft report's desk-row line numbers (R931 :8, R932 :7, R920 :19, R917 :22) do not match HEAD (R931 :20, R932 :19, R920 :31, R917 :34). The rows and their literals are right. The prompts cite no such line numbers, so no prompt is affected.
- N3 NOTE: R917, R920 and R931 have no row in `cto-2026-10-10-words.md` (empty grep). 278 asks the words file only for R849 (a row of `cto-2026-10-10.md`), so no gate fails; R920 reads "(via brain, L79)" and R931 is a desk record.
- N4 NOTE: check 18 asks for `grep -c -F "Bash(codex"` = 0 on all three; 278 prints 1, the sentence in line 1 that says the `Bash(codex exec …)` string of 258 is DROPPED. The launch line has no codex string. Not a launch defect.
- N5 NOTE: the preflight order names `## NEEDS ROUND 2` of the round-2 derive; that report's heading is `## OPEN AFTER ROUND 2` (`:38`). The questions match it.
- N6 NOTE: 280 requires exactly ONE `| R` row naming `278-f4-tribunal-r3.md` in `cto-2026-10-10.md`. Later desk rows must say "the F4 round-3 hub" and not repeat that literal. This report names it; a report file does not count.
- N7 NOTE: 278's PATTERN RULE bans alternation inside one pattern, but the redaction command it borrows from `73` §1 (`grep -c -E "TSLA|372[.]82|374[.]50"`) uses it (same as rounds 1 and 2, which ran; three `-F -e` options would meet both).
- N8 NOTE: the two draft ASK DESK lines (the launch row must carry `grok runs` and an `openai seat:` statement; precedent shape kept) stand open for the desk.

## LAUNCH ROW
One `| R<nn> |` row in `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md`, committed before launch, naming the file and carrying these literals (all three seats read this one row):
- `278-f4-tribunal-r3.md`
- `f4-design-proposal-2026-10-10.md`
- `Fable seat: yes`
- `derive seat: claude-opus-5-5`
- `gemini: sits` (without it, or with `gemini: not seated`, 278 stops on the floor)
- `grok runs: <n> of 3` (the hub only needs the statement)
- `openai seat: <…>` (any value; informational, 278 never probes and makes no `codex` call; Astra is NOT SEATED, R920)

278 does not carry round 2's "no other house hub is running" literal (`grep -o` on 278 finds none); its STAGGER asks only for `grok runs: <n> of 3` and an `openai seat: <…>` statement. No later row may name a different `derive seat:` or `Fable seat:`.

PREFLIGHT DONE · prompts: f4-tribunal-r3 · checks: 36 · fails: 0 · ready: YES
