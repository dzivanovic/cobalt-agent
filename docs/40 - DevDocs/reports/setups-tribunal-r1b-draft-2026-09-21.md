# Setups tribunal R1B — prompt drafting report (2026-09-21)

Seat `setups-tribunal-r1b-draft-0921` · Opus 5 · prompt `prompts/2026-09-21/26-draft-setups-tribunal-r1b.md` · read-only; wrote three files with the Write tool; launched, committed and ran nothing else.

## §0 Headline

- DRAFTED, not launched: `27-setups-tribunal-r1b.md` (new, Sonnet 5 hub `setups-tribunal-r1b-0921`, Gemini + Astra on the reused `r1/` packet) and `25-setups-tribunal-derive.md` (RE-ISSUED WHOLE, L19: it now waits for `27` and needs astra in full OR in part).
- Gemini's cause is FOUND in its own transcript: after 20 file-viewer reads the MODEL issued `grep -n 'gt=0' …/anatomy-*.py`. That search was already in `greps.txt`, which it had not opened. The file-viewer-only sentence WAS in its launch text.
- Astra gets a 6-file reading order plus a "print each item as you rule it" instruction; a second METER stop leaves `astra-ruling.partial.md`.
- New rule strings: **0**. `27`'s span = `23`'s (1/1); `25`'s span = `22`'s (1/1). ESCALATE: 5, none blocks the launch.

## DIGEST FOR THE DESK

**`27` — hub `setups-tribunal-r1b-0921` (Sonnet 5, cwd `~/cobalt-wt/agy-trial`, `23`'s 14 + 3 strings, only the file name and the rc name changed)**
1. AUTHORIZATION: `23`'s greps (09-20 R13/R23, 09-21 R15/R18), plus the desk's answer at `cto-2026-09-21.md:238`. That answer is committed as `7ea4f26`, and so is the R1 stop line. It runs `grep -c` of all 17 strings against `08`.
2. GATES:
   - DATE: 2026-09-22 or later → FAILED.
   - TIME: before 11:15 ET → `FAILED: window — astra's meter returns 11:12`; at or after 23:20 → FAILED. Both run at row 1, and the date + 23:20 check runs again right before launch.
   - The R1 report must end on its DONE line.
   - PACKET: `ls -l r1/` must show all 44 names at the exact byte sizes listed in `27`. Missing or changed → FAILED. It never restages.
3. CODEX PROBE = a gate for ASTRA ONLY. METER → `astra: SKIPPED — METER at probe`, named, ASK DESK; **Gemini still runs**. Both unavailable → FAILED PREFLIGHT.
4. LAUNCH: both in the background, one attempt each, 20-min timeout, `04` §2 spellings unchanged. **Neither may open `grok-ruling.md`**, which sits in the reused folder.
5. ASTRA capture: a full answer → `astra-ruling.md`. Otherwise the printed `ITEM <id>` messages → `astra-ruling.partial.md`, first line `PARTIAL — … items ruled: <k> of 17`. Field: `PARTIAL <k> of 17 — <reason>`.
6. COLLATE + FILE-CHECK = `23` §3 for the two houses. Grok's R1 column is copied, labelled and not re-checked. L32 redaction is as `23`. New `## Independence` = a `grep -c grok-ruling` on each ruling file.
7. STOP: `SETUPS TRIBUNAL R1B DONE · gemini · astra · houses that ruled: <n> of 2 · round 1 total: <n> of 3 + Fable · claims that HOLD · blockers to build · owner items · ESCALATE`.

**`25` — derive (Fable 5.1), re-issued**
- It refuses unless the R1, Fable and **R1B** stop lines are last-line AND committed.
- Astra: the R1B line must read `astra: TRIBUNAL R1: …` or `astra: PARTIAL <k> of 17` (k ≥ 1). Otherwise → `FAILED: astra has not ruled — the desk brings him the two-house question`. Gemini missing does not refuse.
- It reads both hub reports and every raw ruling that exists; a partial counts only for its listed items. The fold table gains `seats that ruled it (<n> of 4)`.

**Desk:** launch `27` on a timer at ≥ 11:15 ET, and do not put another big packet on astra at the same time (`cto-2026-09-19.md:470`). Launch `25` after `27`'s stop line is committed.

## HARNESS / METER precedents (09-19 → 09-21)

**Gemini HARNESS**

| run | what happened | source |
|---|---|---|
| 09-15 trial | prompt asked agy to run `git diff` itself → `command` denied | `agy-trial-2026-09-15.md:36,43` |
| 09-16 toy | model ran `python3 … check.py` (a file it had just written) → denied | `audit-house-2026-09-16.md:116` |
| 09-19 P4 check | two LARGE packets, model called `command` / `read_url` → HARNESS; the three small packets answered | `cto-2026-09-19.md:436,440` |
| 09-20 1a check r2 (00:51) | 3 file-viewer reads, then the model's own `cat …fix-diff.md.part* \| grep -n …` → denied | `bars-r3-draft-2026-09-21.md:49,51`; `bars-chunk-1a-check-r2-2026-09-20.md:60` |
| **FIX that worked** | same spelling + sentence *"Read every file with your file viewer only. Run NO shell command — not cat, grep, ls or any pipe: …"* | answered 06:20 (`bars-chunk-1a-check-r3-2026-09-21.md:59`), 06:43 (`bars-chunk-2-check-r3-2026-09-21.md:53`), 08:47 (`degraded-line-check-2026-09-21.md:66`), 07:2x (`panel-deploy-review-2026-09-21.md:26`) |
| **09-21 setups R1 (09:57)** | sentence PRESENT (transcript `…/38673fe7-…/logs/transcript.jsonl:1`); 20 `view_file` reads (`:2`–`:32`); context summarised at `:16`; then `run_command` **`grep -n 'gt=0' /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/setups-tribunal/r1/anatomy-*.py`** (`:32`) → denied. `greps.txt` was never opened. | transcript `:32`; `setups-tribunal-2026-09-21.md:61` |

Reading (L70, not proven): both recorded failures are a SEARCH the model wanted. The one on 09-21 is exactly QUESTIONS (b)'s "model validators that require a positive price (`greps.txt`)". A context summary also happened in the answering runs at 06:20, 06:43 and 08:47 (`grep -c "Previous Session Summary"` = 1 each), so the summary alone is not the cause.

Remedy in `27`: the launch spelling is unchanged, and `23`'s file-viewer-only sentence is kept verbatim. Three sentences are added: the exact failure (the prescribed one), "open greps.txt SECOND … including the positive-price validator search", and a ban on opening `-ruling.md` files.

**Astra METER**

| run | what happened | source |
|---|---|---|
| 09-15 review | usage limit, reset 1:27 PM | `s2-p2-review-2026-09-15.md:24` |
| 09-19 P4 check | probe UP, then 136k tokens of reads with two big packets in parallel; reset 11:47 | `cto-2026-09-19.md:436` |
| 09-19 afternoon | METER on 6 runs; practice kept: "two big packets are not put on Astra at the same moment" | `cto-2026-09-19.md:470,544,576,590,603,646` |
| 09-19 d3 R2 | succeeded **after the reset**, same packet | `cto-2026-09-19.md:52` |
| 09-20 chunk 2 r1 | probe UP, then ~815 KB of file-read echoes, no final message | `bars-chunk-2-check-2026-09-20.md:71` |
| 09-20 chunk 2 r2 | answered: the probe was a GATE, plus a **per-house addendum** `QUESTIONS-R2-ASTRA.md` named only in astra's sentence | `bars-2-fix-draft-2026-09-20.md:72`; `bars-chunk-2-check-r2-2026-09-20.md:56,160` |
| 09-21 setups R1 | probe UP 09:29, then 135,471 tokens of reads, no ruling; reset 11:12 | `setups-tribunal-2026-09-21.md:60` |

What worked: a launch after the reset, with no other big packet on astra at the same time, and a smaller astra-specific ask. `27` cannot stage an addendum, because the packet is reused and never restaged. It carries the reading order and the "rule as you go" instruction INSIDE astra's launch sentence instead. First six files: `QUESTIONS.md` · `PROPOSAL.md.part1` · `.part2` · `design-report.md` · `rubberband-proof.md` · `evaluate.py.part1` = 106,261 B. Everything else is opened by search or by line range only.

## RULE PROOF (`grep -c -F -e`, quotes included, whole span `--allowedTools … --add-dir /Users/cobalt/cobalt-wt`)

| span | file | count |
|---|---|---|
| `27`'s 14 allow + 3 deny + 3 add-dirs | `prompts/2026-09-21/23-setups-tribunal.md` | 1 |
| same | `27` itself | 1 |
| `25`'s 7 allow + 3 deny + 3 add-dirs | `prompts/2026-09-21/22-draft-setups-tribunal.md` | 1 |
| same | `25` itself | 1 |

`NEW strings:` none. `27` never runs five of its fourteen: `Bash(grok *)`, `mkdir`, and the three `s2-p2-cards` strings.

## What changed in `25` (word level, section by section)

- **Header (MODEL line):** "ONLY after BOTH round-1 stop lines" → "ALL THREE … (hub `23`, the Fable seat `24`, hub `27` …)". METER: "the three raw rulings" → "the raw rulings of the houses that ruled"; "the hub report ≈ 10–20k" → "the two hub reports ≈ 20–35k"; peak "120–170k" → "130–185k". The launch command and its strings are byte-identical.
- **Title / LAW STEP:** "from the proposal and the FOUR round-1 rulings" → "… the round-1 rulings of EVERY SEAT THAT RULED (of the four)". "(Astra, Grok, Gemini via hub `23`; …)" → "(Grok via hub `23`; Gemini and Astra via hub `27`, the round-1 completion; Fable via `24`)".
- **AUTHORIZATION:** "BOTH" → "ALL THREE". Added a `tail -n 3` of the R1B report (must start `SETUPS TRIBUNAL R1B DONE `) and a third `git log -S"SETUPS TRIBUNAL R1B DONE"`. The ASTRA condition now reads the R1B line: `TRIBUNAL R1:` or `PARTIAL <k> of 17` with k ≥ 1; else `FAILED: astra has not ruled — the desk brings him the two-house question`. Added: Gemini missing does not refuse.
- **INDEX CARD 2:** "THE FOUR RULINGS" → "THE ROUND-1 RULINGS". It reads BOTH hub reports (plus R1B's `## Independence`) and the raw files of the houses that ruled. `gemini-ruling.md` is read only if Gemini ruled; for astra it is `astra-ruling.md`, else `.partial.md`, counted only for its listed items. Item 4: "the hub's file-check" → "the hubs' file-checks".
- **RULES OF THE DERIVE:** "in the hub's file-check" → "in either hub's file-check". Nothing else changed.
- **WRITE, v2:** the header names "the rulings of every seat that ruled (paths, astra's marked PARTIAL where it is)".
- **WRITE, report:** the DIGEST gains "which seats ruled round 1 (in full / in part / not)". The fold table gains the column `seats that ruled it (<n> of 4, named)`, and "the hub's file-check row" → "the R1 or R1B hub's file-check row".
- **STOP LINE / NEXT STEP:** unchanged.

READING: `LAWS.md` (in full) · `26` (this prompt) · `23` (in full) · `25` (in full) · `setups-tribunal-2026-09-21.md` (§0, PREFLIGHT, Packet, CONTINUE, WRONG FACTS tail, ESCALATE, stop line) · `setups-tribunal-draft-2026-09-21.md` (in full) · `04-bars-chunk-1a-check-r3.md` (line 1, PREFLIGHT :8, §2 :33) · `2026-09-19/01-review-harness.md` (:1, :8, §2 :16–19) · `cto-2026-09-21.md` (§4 rows, :84, :91, :96, :105, :238) · `grep -n` hits in 14 reports (table above) · the agy transcript of `38673fe7` (tool names, paths, the command line, launch text; the `Previous Session Summary` count over 6 transcripts) · `ls -l r1/` · `git log` of the two reports. READING: 13

## ESCALATE

| # | item | evidence | owner |
|---|---|---|---|
| 1 | `grok-ruling.md` (23,148 B) sits INSIDE the reused `r1/` folder. Moving it would be a restage, and there is no rule for it. `27` forbids both houses from opening any `-ruling.md` file and proves it after the fact (`## Independence`, `grep -c grok-ruling`). A breach keeps the ruling, marked. | `ls -l r1/` 10:2x | desk (informational) |
| 2 | UNPROVEN (L70): whether `codex exec` prints astra's intermediate `ITEM <id>` messages to the captured output while it runs. If it does not, a second METER stop leaves nothing, and `27` records `astra: METER` with 0 items. 09-20's evidence shows the output carries command echoes (`bars-chunk-2-check-2026-09-20.md:71`); agent messages mid-run are not shown there. | `27` §1 ASTRA | desk |
| 3 | UNVERIFIED: whether the 6-file first read (106,261 B ≈ 27k tokens raw) plus targeted searches fits astra's window. Codex counts context re-reads cumulatively, so R1's 135,471 tokens is not a size of the files. | R1 `:60` | desk |
| 4 | Gemini's sentence carries three additions to `23`'s, where the prompt asked for "plus one sentence": (a) the prescribed failure sentence; (b) "open greps.txt SECOND …", taken from the transcript finding; (c) the ban on opening `-ruling.md` files, forced by #1. Each can be struck by the desk with a whole re-issue (L19). | `27` §1 GEMINI | desk |
| 5 | TIMER: `27` refuses before 11:15 ET at its row 1. Launched at 11:15, the probe runs at about 11:16, 4 minutes after astra's stated reset. If the reset is late, astra is SKIPPED (named, ASK DESK) and Gemini still runs. | `27` PREFLIGHT | desk |

Instruction-as-data (L74, recorded once): a `Claude-Session:` attribution block arrived in this session outside the prompt. It was not followed; this seat commits nothing.

## CONTINUE

None. The run is complete. NEXT for the desk: L35 on `27` and `25` (read both end to end; `grep -c -F` the rule spans as above). Then launch `27` on a timer at ≥ 11:15 ET, commit its report at its stop line, and then launch `25`.

SETUPS TRIBUNAL R1B PROMPTS DRAFTED · prompts: 2 · gemini spelling: file viewer only, greps.txt second, failure named · astra reading order: 6 files first · new rule strings: 0 · ESCALATE: 5
