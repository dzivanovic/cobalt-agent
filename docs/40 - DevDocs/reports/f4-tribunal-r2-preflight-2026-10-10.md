# F4 round-2 tribunal prompts 258 · 259 · 260 — preflight · 2026-10-10

Clock: Sat 2026-10-10 13:38 EDT. Read-only; no git write, no launch. Prompt 261 is committed and clean.

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff --stat HEAD -- prompts/2026-10-10` | empty | OK |
| 2 | `git log -1 --format=%H` on 258, 259, 260 | each `5692b0d0c8512bd45e90fe5e771525d812ff7af9` | OK |
| 3 | `grep -c 'claude --bg "Read '` on 258, 259, 260 (the launcher's own count) | 1, 1, 1 | OK |
| 4 | `desk-launch.sh` `prompt` rules read at `:410-547`: one backticked launch line, first `cd` span, mode `auto`, deny pair, `--remote-control` before `--name`, no `<` or `>` in the line, text ends at `follow it exactly.`, no write string (`git add/commit/merge`, `Bash(git *)`, `uv run`, `launchctl`, `COBALT_ENV=`) | 258 line printed with `grep -o`: no `<`, no `>`, no write string; `cd /Users/cobalt/cobalt-wt/agy-trial` (exists); 259, 260 same `cd` | OK |
| 5 | `--add-dir` covers every path in each line | Vault, cobalt, cobalt-wt; all paths sit under one | OK |
| 6 | 258's whole `--allowedTools … --add-dir` span (14 allow, 3 deny) against `237-f4-tribunal.md`, `grep -c -F` | 1 (so each of the 14 allow and 3 deny counts ≥1) | OK |
| 7 | the same span of 258 against itself | 1 | OK |
| 8 | 259's span (7 allow, 3 deny) against `238-…-opus-seat.md` | 1 | OK |
| 9 | 260's span against `239-…-derive.md` | 1 | OK |
| 10 | 259 and 260's own span against themselves | 1 and 1 | OK |
| 11 | no Sol or Opus checker string in the launch line (`gpt-5.6-sol`, `claude -p --model`): `grep -c -F` on 258 | 1 each, both in the gate's prohibition text; the launch line printed in #4 has neither | OK |
| 12 | models: 258 `claude-sonnet-5-5`; 259 and 260 `claude-opus-5-5`; `claude-fable-5-1` in 259 | once, as "never" | OK |
| 13 | `grep -c -x -F "FABLE ROW: R109"` (259) and `"DERIVE ROW: R109"` (260) | 1 and 1 (filled) | OK |
| 14 | `grep -n "^| R109 "` `cto-2026-09-22.md` | `:56` `Make all Opus 5.5 for now`, `claude-opus-5-5`, `derive seat: claude-opus-5-5` | OK |
| 15 | date gates: `grep -n "^| R17 \|^| R19 "` `cto-2026-09-24.md`; 258 states NO DATED GATE | `:35` `Grok approved with no asking going forward`; `:37` `All 4 house models approved`; no date in any gate | OK |
| 16 | `grep -n "^| R849 \|^| R860 \|^| R876 \|^| R903 "` `cto-2026-10-10.md` | `S5 pulled forward`; `S5 tribunals use the 09-22 drafted shape`; R876 names `237-f4-tribunal.md`; R903 carries `7 items need round 2` | OK |
| 17 | `git log -1 -S"<literal>"` for R849, R903, `F4 TRIBUNAL R1 DONE`, `F4 DERIVED · DRAFT FINAL`, `F4 TRIBUNAL OPUS R1 DONE`, F4-FINAL | `2ef44c84`, `dcd29aaa`, `2045d8b3`, `04be9316`, `01ac13d6`, `04be9316` (all committed) | OK |
| 18 | round-1 chain: `tail -n 3` of the hub and derive reports; `grep -c -F "ROUND 2 OWED"` F4-FINAL | hub ends `F4 TRIBUNAL R1 DONE · … floor: MET`; derive ends `F4 DERIVED · DRAFT FINAL · … needs round 2: 7`; 8 markers | OK |
| 19 | `grep -n -F "258-f4-tribunal-r2.md"` `cto-2026-10-10.md` | no row yet (the desk writes it before launch) | NOTE N1 |
| 20 | guard pattern: `ops/desk/bare-guard.py:756` is `(^|/)prompts/20[^/]*/[0-9]+-(?!draft)[a-z0-9-]*-tribunal(-r[0-9]+)?\.md$`; applied by hand to each name | `258-f4-tribunal-r2.md` MATCHES (`258-` · `f4` · `-tribunal` · `-r2` · `.md`); `259-…-opus-seat.md`, `260-…-derive.md` and `261-…-preflight.md` do NOT (end is not `-tribunal(-rN).md`) | OK |
| 21 | the guard commit `git rev-parse 230b2463` | `230b24631c59d8c972bf4939f8f7884bb5729881`; the guard file carries the pattern (#20) | OK |
| 22 | stop lines and report paths agree: hub `F4 TRIBUNAL R2 DONE` at `reports/f4-tribunal-r2-2026-10-10.md`; seat `F4 TRIBUNAL R2 OPUS DONE` at `reports/f4-tribunal-r2-opus-2026-10-10.md`; 260 refuses unless both last lines start with these and are committed (`git log -S`), `floor: MET`, two outside rulings; 259 blocks the hub's path | same literals in 258 §3-4, 259 REPORT/STOP LINE, 260 preconditions | OK |
| 23 | 260 writes F4-FINAL under `docs/30 - Design/`; refuses when `ROUND 2 OWED` count is 0 | `F4-FINAL-2026-10-10.md`; refusal line present; `F-26` onward tags | OK |
| 24 | 258 questions R2-1…R2-7 against `## NEEDS ROUND 2` of the derive report (`:72-108`): titles, sub-questions, experiments | seven items in the same order, same question text; nothing extra (no sol/opus checker item, no self-assignment: every item `SELF: no`) | OK |
| 25 | verbatim spot-check by `grep -F`: Grok R2-1 "Refresh classifies, then builds the cobalt proposal from" and Astra "Never derive value age from the latest attempt stamp" in the round-1 hub report; Astra's R2-4 REJECT "Omit prefill from the shared gate" in F4-FINAL `:283`; Grok R2-3 "Exit 0: the job result lists every degraded field" | 1, 1, 1, 1 | OK |
| 26 | Charter quote of R2-5 B: `grep -c -F "the note exists at 05:15 with Cobalt blocks stamped"` | 0 on one line; the text is at `MVP-CHARTER-v0_2.md:82-83`, wrapped (`note` / `exists at 05:15 with Cobalt blocks stamped "as of HH:MM"`) | NOTE N3 |
| 27 | the hub's own round-1 row numbers: `F1`–`F37`, `FC1`–`FC26` exist; 258 numbers new rows from `FC27`; `## Rulings table`, `## Wording offered, verbatim`, `## Checked against the files`, `## Opus-seat round-1 claims, file-checked`, `## Experiments named (L70)` and `closing line` / `Where two houses contradict` exist | all present | OK |
| 28 | the Opus seat's round-1 report: `## Rulings`, `## Self-attack`, three `WITHDRAWN:` lines (`:181-183`) | present | OK |
| 29 | packet sources exist, 18 paths (`daily.py`, `cli.py`, `config.py`, `market.py`, `rules_gen.py`, `writer.py`, `merge.py`, `store.py`, `prefill.yaml`, `daily.md.j2`, `wrapper.py`, `jobs.yaml`, `radar/notes.py`, `archiver/runner.py`, `test_finviz_consumers.py`, `clock.py`, `daymode/note.py`, `aset/daily_note.py`, `heartbeat/runner.py`); the Charter; `73-…` and `04-…`; the draft report | all exist | OK |
| 30 | anchors: `def daily_note_path` `daymode/note.py:238`; `check_total_demand` `notes.py:276`; `scheduled_consumers` `:329`; `stub_template` `aset/daily_note.py:103`, `create_if_absent(path, stub_template` `:184`; `_write_with_retry` `writer.py:559`; `create_if_absent` `:588`; `upsert_unit` `:673`; `_merge_base` `:846`; `last_after` `store.py:91`; `recent_afters` `:111`; `overrides_for` `:232`; `purge_expired` `:247` | each equals the prompt's anchor | OK |
| 31 | the code: `git rev-parse d0a5fbb8`; `git diff --stat d0a5fbb8 HEAD -- src configs tests "docs/00 - Project"` | `d0a5fbb8761a7ddf46b22310db4089eec32f8b27`; one file changed, `tests/ops/test_bare_guard.py` (not a packet path) | OK |
| 32 | `ls` `scratch/tribunal-bars-0920` under `agy-trial` | exists (the hub's Grok string has its folder) | OK |
| 33 | LAWS headings the prompts cite (L1 L3 L9 L10 L28 L29 L32 L35 L36 L37 L39 L42 L43 L47 L52 L53 L58 L59 L60 L62 L67 L68 L70 L71 L72 L73 L74 L75 L76), `grep -c -E` | 29 of 29; L72 text is the seam-document rule (`LAWS.md:363`) | OK |
| 34 | Gemini and Round-1 spelling: 258 uses 237 §2's spellings unchanged (`gemini-3.8-flash-high`, `gpt-6-astra`, `grok-4.7`); round 1 ran with all three | Gemini ruled `TRIBUNAL R1: ADOPT` in round 1 | OK |
| 35 | floor (proposer plus two outside houses), round cap (round 2 of at most three, L39/L67), meter probe first (L47), Astra's PARTIAL capture, file-check of every claim and of the Opus seat's claims at collate (`FC27` on), STAGGER, clock at 20 minutes | all in 258 preflight, §2, §3, §4 | OK |
| 36 | no seat holding a side recommends (L37): 258 "no verdict of your own"; 260 "you recommend nothing to him"; 259 rules and approves nothing; OPEN items go to him as one A/B with no recommendation | present | OK |
| 37 | no personal content (L32): packet is committed code, config, design, reports, LAWS and the Charter; daily-note text, `Rules.md`, vault rows and `1 - Trading/` listed under NOT STAGED; the redaction `grep -c -E "TSLA|372[.]82|374[.]50"` on 258 itself | 0 | OK |

## ISSUES
- N1 NOTE: no launch row names 258 yet. The desk writes and commits it before launch (see LAUNCH ROW); 258, 259 and 260 each refuse without it.
- N2 NOTE: 258 §1 sends the hub to `73` §1 for its redaction command, `grep -c -E "TSLA|372[.]82|374[.]50"` (`73-s3-exits-tribunal.md:14`): alternation inside one pattern, against 258's own PATTERN RULE (the same N3 as round 1, which ran). A permission check may deny it, and the hub then has no redaction proof; three `-F -e` options would meet both. Not a fail: round 1 recorded the same.
- N3 NOTE: the Charter's R2-5 B quote is correct but wraps across two lines at `:82-83`, so a one-line `grep -F` of it prints 0. The hub's file-check of `FC20` should search `blocks stamped`.
- N4 NOTE: 260 requires exactly ONE row naming `258-f4-tribunal-r2.md` in `cto-2026-10-10.md`. Later desk rows (this preflight's included) must say "the F4 round-2 hub" and not repeat that literal, or 260 refuses. This report names it, which is a report file and does not count.
- N5 NOTE: 259 and 260 launch beside or after the hub on the same launch row; 259's STAGGER keeps the Opus seat off the day's code checks (`259:1`). The desk starts 259 only after the row is committed.
- N6 NOTE: 258's STAGGER needs a printed line that names `258-f4-tribunal-r2.md` AND `no other house hub is running`; any other house hub the desk names needs `<nn> is not running` in a line naming 258.

## LAUNCH ROW
One `| R<nn> |` row in `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md`, committed before launch, naming the file and carrying these literals (all three seats read this one row):
- `258-f4-tribunal-r2.md`
- `f4-design-proposal-2026-10-10.md`
- `Fable seat: yes`
- `derive seat: claude-opus-5-5`
- one of `gemini: sits` or `gemini: not seated` (neither literal means not seated)
- `no other house hub is running` (258's STAGGER row; any other house hub the desk names needs `<nn> is not running` in a line that also names `258-f4-tribunal-r2.md`)

No other row may name `258-f4-tribunal-r2.md` (N4). No later row may name a different `derive seat:` or `Fable seat:`.

PREFLIGHT DONE · prompts: f4-tribunal-r2 · checks: 37 · fails: 0 · ready: YES
