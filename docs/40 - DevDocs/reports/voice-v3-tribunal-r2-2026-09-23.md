# VOICE V3 TRIBUNAL R2 — hub `voice-v3-tribunal-r2-0923` (Sonnet 5), report

## §0 Headline
- Ruled: grok and gemini (2 of 3; Astra `METER — proceed on three`). Both closed `TRIBUNAL R2: BUILD`. R2-1: **CONVERGED**, 2-0 ADOPT B (the voice module deletes; the heartbeat probe only counts). R2-2: **SPLIT**, grok ADOPT S vs gemini ADOPT P. R2-3: **SPLIT**, grok ADOPT B (no slice in V1–V4) vs gemini ADOPT A (V1, 12 h).
- Converged: 1 of 3. ESCALATE: 8 (three gemini supporting claims DOES NOT HOLD as worded; one grok text quoted for R18; packet 111,218 B). Redactions: 0 in the packet, 2 in this report. Anthropic-seat R1 claims checked: 7 HOLD of 8 checked (C6's behaviour part UNVERIFIABLE FROM READS + a named run; none DOES NOT HOLD).
- No write refused. First run of this file (R37) stopped at PREFLIGHT on prompt `20`; this is the relaunch after the desk's R40. The Anthropic seat's round-2 report was not read.

## AUTHORIZATION
Relaunch of the same file after the desk's R40 (the first run stopped at PREFLIGHT on prompt `20`; that report was overwritten by this run). All checks below are own Bash calls, 10:17–10:19 ET on 2026-09-23. All PASS.
| check | result |
|---|---|
| `cto-2026-09-20.md` R13 (13:33 ET) | row present (line 86) |
| `cto-2026-09-20.md` R23 (17:47 ET) | row present (line 206) |
| `cto-2026-09-21.md` R46 | row present (line 57); carries `For the designs and creations we need the higher level models` |
| `cto-2026-09-22.md` R13 | row present (line 150); carries `without Astra` |
| `cto-2026-09-22.md` R109 | row present (line 56); carries `Make all Opus 5.5 for now` |
| `cto-2026-09-23.md` R18 | row present (line 21); carries `VOICE v3 DIRECTIVE` and `Solve this` |
| `cto-2026-09-23.md` R36 | row present (line 39); carries `needs round 2: 3` and `23-draft-voice-v3-r2.md` |
| derive stop line committed | `git log -1 -S"VOICE V3 DERIVED"` → `fc82bfaa03c5563fd2c5f82f52f0d04eb39520a0` |
| derived design committed | `git log -1 -- VOICE-v3-derived-2026-09-23.md` → `fc82bfaa03c5563fd2c5f82f52f0d04eb39520a0` |
| derive report last non-blank line | `VOICE V3 DERIVED · folds: 33 · verbatim: 22 · needs round 2: 3 · owner items: 1 · ESCALATE: 8` |
| LAUNCH ROW naming `24-voice-v3-tribunal-r2.md` | `cto-2026-09-23.md` R37 (line 40) and R40 (line 43, the relaunch row); `| R` rows, DESK LAUNCH, no words of his beyond R18 / R28 / 09-22 R13 / R109 |
| launch row committed | `git log -1 -S"24-voice-v3-tribunal-r2.md" -- cto-2026-09-23.md` → `0281aa716cef83fee0e4b54e3beac9f22ca6ec92` |
| R28 (grok/agy extension) | exactly one row (line 31): `His word: "A"`, `run rules EXTENDED through 2026-09-24 23:59 ET`, `for every house-lane hub`; committed `676fa870bc2b553a898e2734dd5cca2b64e92930` |
| NO NEW RULE | 14 allow strings + 3 deny strings, quotes included, each `grep -c -F` on `prompts/2026-09-20/08-bars-chunk-e-check.md` → 1 (17 of 17 ≥1) |
| Sol / Opus checker string on the launch line | none in the launch line this file carries |

LAWS.md read in full (442 lines, two pages).

## PREFLIGHT
| # | rule · command | exit | result |
|---|---|---|---|
| 1 | `date` (DATE + EXTENSION GATE + WINDOWS) | 0 | `Wed Sep 23 10:17:49 EDT 2026` → 09-23, R28 stands (see AUTHORIZATION); 10:17 is outside both windows (19:25–20:45, ≥23:20) → allowed |
| 2 | `grok --version` | 0 | allowed: `grok 1.0.25 (f7e67d6988e2) [stable]` |
| 3 | `agy --version` | 0 | allowed: `1.2.9` |
| 4 | `ls scratch/tribunal-bars-0920/voice-v3-tribunal` | 0 | allowed: lists `r1` |
| 5 | `ls scratch/tribunal-bars-0920/voice-v3-tribunal/r2` | 1 | allowed: `No such file or directory` → fresh run |
| 6 | STAGGER (s1): `tail -n 3 …/routing-x5-retro-2026-09-23.md` | 0 | last non-blank line `(run in progress — next step under ## CONTINUE)` → 19 running or paused |
| 6a | `ls scratch/tribunal-bars-0920/routing-x5/PAUSE` | 0 | PAUSE file exists |
| 6b | `grep -n -F "paused by the desk" …/routing-x5-retro-2026-09-23.md` | 0 | line 74 inside `## CONTINUE`: `next: PASS 1 from P06 — paused by the desk at 10:1x ET (PAUSE file present, row R37 voice v3 tribunal r2 needs the house lane) …` → **`19: PAUSED by the desk`** |
| 7 | STAGGER (s2): `ls …/reports` once, for the DRC checks | 0 | no `drc-d<k>-check-2026-09-*.md` for k = 1…5 → no `tail` calls; `53`–`57` rest on the launch row |
| 7a | `grep -n -F "53 is not running"` … `"57 is not running"`, one call each, on `cto-2026-09-23.md` | 0 ×5 | each prints R37 (line 40) and R40 (line 43); R40 names `24-voice-v3-tribunal-r2.md` → `53`–`57`: no report — not running (launch row) |
| 7b | `20` (`20-routing-x1-sonnet-shadow.md` PART B): report `routing-x1-shadow-check-2026-09-23.md` | — | ABSENT from the `ls` of `reports/` |
| 7c | `grep -n -F "20 is not running" …/cto-2026-09-23.md` | 0 | prints R40 (line 43): "20 is not running (never launched)", and the same line names `24-voice-v3-tribunal-r2.md` → `20: no report — not running (launch row)` |
| 7d | other house hubs (03, 05, 06, 08, 13, 17) | — | R40 names each `is not running`; no report checked further (the rule takes the launch row) |
| 8 | THE CODEX PROBE `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` (background) | 1 | `ERROR: You've hit your usage limit. Upgrade to Pro (https://chatgpt.com/explore/pro), visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at Sep 26th, 2026 6:47 AM.` → `astra: METER — proceed on three` (recorded, EXPECTED). Astra not launched. |

## Packet
Staged under `scratch/tribunal-bars-0920/voice-v3-tribunal/r2/` (gitignored in `~/cobalt-wt/agy-trial`; the folder was created by the first Write). Round 1's packet is NOT restaged: it stays at `../r1/`. Every anchor was checked with `grep -n` and sat at the line the prompt gave; NO boundary moved. `wc -c` after all drops:
| file | B | notes |
|---|---|---|
| `QUESTIONS-R2.md` | 14,630 | the prompt's text verbatim (unquoted) + the "Files in this folder:" paragraph; the three drop notes added to the guidance lines |
| `NEEDS-ROUND-2.md` | 4,976 | derive report :93–108 (last non-blank before `## OWNER TEST`), fold-table header :55–58, rows F-07 :65, F-09 :67, F-12 :70, F-22 :80, F-27 :85, ESCALATE item 1 :139 |
| `derived-sections.excerpt.md` | 29,183 | committed design ranges :1-11, :65-72, :76-79, :104-111, :113-127, :129-133, :152-164, :210-241, :254-262, :293-303 (`:276-290` DROPPED, see below) |
| `hub-checks.md` | 4,688 | round-1 hub report: header :125–127, C4 :131, C9 :136, C10 :137, FC header :139–143, FC3 :146, FC5 :148, OWNER ITEMS :176–184 |
| `seat-r1.excerpt.md` | 7,914 | Anthropic seat R1: T4 :52–57, T6 :61–66, T8 :72–76, (g) :159–163, WITHDRAWN :190–191, closing line :6 (the seat's closing `TRIBUNAL R1:` line sits in its DIGEST at :6, not at the bottom) |
| `grok-r1-own.excerpt.md` **[RAW RULING — Grok's own]** | 5,440 | `r1/grok-ruling.md` :21–26, :31–36, :43–46, :123–128, :145–148, :159 |
| `gemini-r1-own.excerpt.md` **[RAW RULING — Gemini's own]** | 2,272 | `r1/gemini-ruling.md` :13–16, :21–24, :29–32, :80–88, :92 |
| `writer.excerpt.py` | 9,685 | `vaultwrite/writer.py` :387-420, :457-470, :530-553, :644-700, :807-830, :895-935 (`:1-30` DROPPED) |
| `heartbeat.excerpt.py` | 8,007 | `heartbeat/runner.py` :126-167, :413-452; `heartbeat/probes.py` :30-44; `ops/com.cobalt.heartbeat.plist` :1-70; `ops/com.cobalt.aset.plist` :1-10 |
| `hitl-precedent.excerpt.py` | 8,165 | `radar/propose.py` :1-5, :422-470, :711-760; `notify/mattermost.py` :1-15, :130-160 (`radar/cli.py` and `settings/card.py` DROPPED) |
| `greps.txt` | 16,258 | the 11 commands' full output (none over 400 lines, no `greps-<n>.txt`); main HEAD `279a7be` |
| **TOTAL** | **111,218** | |

- **Size and drop order.** The staged set first measured 115,855 B (with QUESTIONS), over the prompt's 110 KB. The drop order was applied in full: (i) `writer.excerpt.py` `:1-30`; (ii) `hitl-precedent.excerpt.py`'s `radar/cli.py` and `settings/card.py` ranges; (iii) `derived-sections.excerpt.md`'s `:276-290`. The header of each affected file says what was dropped and, for (ii), quotes the dropped lines' claim; `QUESTIONS-R2.md`'s guidance lines say so. The order is exhausted at **111,218 B: under 110 KiB (112,640), over 110,000 B.** Listed under `## ESCALATE` (rule: "a packet over 110 KB after the drop order").
- **The prompt's grep sentence was wrong.** `greps.txt` was to say "this shell's `grep` honours `.gitignore`". The hub TESTED it: `grep -rl -e "NEEDS ROUND 2" scratch/tribunal-bars-0920/voice-v3-tribunal/r2` (a gitignored folder) listed two files, so it does NOT. `greps.txt` says that instead. The searches ran on tracked source, so no result is affected.
- **Trailing whitespace.** The Write tool strips trailing whitespace. Whole-file counts of trailing-whitespace lines in the originals the excerpts copy: derived design 0, `writer.py` 0, `heartbeat/runner.py` 0, `radar/propose.py` 0, `com.cobalt.heartbeat.plist` 0. The excerpts are composites (a heading line + real lines), so byte-identity to one original file is not a test that applies; the originals carry no trailing whitespace to lose.
- **Transcription corrections, disclosed.** While writing `greps.txt` the hub first mis-copied two lines (line 259's ending and a truncation of line 295 of the design); both were restored to the original text before any house read the folder (verified afterwards with `grep -c -F` on both restored passages: count 2). `heartbeat.excerpt.py`'s plist range originally ended one line early and its header was wrong; corrected (`:70` is `<key>StandardErrorPath</key>`).
- **REDACTION (L32).** `grep -c -E "TSLA|372[.]82|374[.]50"` on every staged file (11 files, one call): each printed `0`. No other ticker, price, share count or P&L was found. **Redactions: 0.**
- **NOT STAGED:** any audio, transcript or note of his; the proposal and the derived design whole; the Anthropic seat's round-1 report whole; any production row; and NEVER the Anthropic seat's round-2 report (`25`) — this hub did not read it. (`git log` shows its desk commit `279a7be` "voice v3 r2 Opus seat ruled" exists; the hub read nothing from it.)
- **Stray calls.** Two stray, malformed tool calls of the hub's own (a `Write` to a path outside the repo and an `Edit` of a nonexistent file) were issued and DENIED / failed; nothing was written. Recorded for honesty.

## CONTINUE
next: WAIT for Grok's completion notice (task `bn7y9tb2q`); at the notice run `date`, write the Clock row, read `r2/grok-ruling-r2.md` (or the task output); then §3 collate (Rulings table, Wording offered, Checked against the files, Experiments, OWNER answers, Independence greps, ESCALATE, §0, close).
DONE so far: preflight, authorization, packet, launch, `## Anthropic-seat round-1 claims, file-checked` (C1–C8 written), Gemini's ruling filed at `r2/gemini-ruling-r2.md` (closing line `TRIBUNAL R2: BUILD`), Grok's ruling read (10:47), all of §3 written. Own file-checks of Gemini's claims already made (to be written under `## Checked against the files`): `settings/` has no `propose.py`; the only inbound `approve` handler is the OLD tree's `cobalt_agent/interfaces/mattermost.py:380-419` (0 references to `cobalt settings`); `card.py:15-16` and `settings/cli.py:105-106` say "trader-run".
Houses launched together at ~10:31 ET (`date` read 10:31:09 right after the launch calls; date gate at 10:30:48): GROK task `bn7y9tb2q` (writes `r2/grok-ruling-r2.md` itself; launched 10:31, **20-minute deadline 10:51 ET**; at 10:35:34 it had produced 3 progress sentences and no ruling file), GEMINI task `brlzktczy` (finished 10:32:55).

## Clock
| time | trigger | house minutes since launch | action |
|---|---|---|---|
| 10:17:49 | preflight row 1 (`date`) | none launched | gate passed |
| 10:19:19 | staging start (`date`) | none launched | began staging `NEEDS-ROUND-2.md` |
| 10:29:19 | packet staged + redaction 0 (`date`) | none launched | STAGGER (s1) rechecked: 19 still PAUSED (last line in-progress, PAUSE file present) |
| 10:30:48 | DATE + EXTENSION GATE, second row (`date`) | none launched | 09-23 → R28 row present and committed (`676fa87…`); windows clear; gate passed |
| 10:31:09 | launch (`date`, right after both launch calls) | grok 0 · gemini 0 | GROK `bn7y9tb2q` and GEMINI `brlzktczy` launched together, one attempt each, deadline 10:51 |
| 10:32:19 | claims file-check, after C1–C8 code reads | grok ~1 · gemini ~1 | no ruling files yet (`ls`) |
| 10:32:39 | claims table, after C1–C2 written | grok ~1 · gemini ~1 | continue C3 |
| 10:32:53 | claims table, after C3 written | grok ~2 · gemini ~2 | continue C4 |
| 10:32:55 | Gemini completion notice (exit 0) | grok ~2 · gemini ~2 (finished) | Gemini printed a ruling ending `TRIBUNAL R2: BUILD`; hub wrote `r2/gemini-ruling-r2.md` byte for byte without `[exited with code 0]`. Grok output so far: three progress sentences, no ruling file yet |
| 10:33:19 – 10:34:12 | claims table between rows C4, C5, C6, C7–C8 (four `date` reads: 10:33:19, 10:33:29, 10:33:36, 10:33:52; 10:34:12 after the last row) | grok ~3 | claims table complete |
| 10:35:09 | own checks of Gemini's R2-3 claims (`ls settings`, `ls ops`, old bot grep) | grok ~4 | none |
| 10:35:34 | before ending the turn while Grok runs | grok ~4 (deadline 10:51) | `## CONTINUE` written; 10:35:48 Gemini independence greps (0, 0) |
| 10:47:22 | Grok completion notice (exit 0) | grok ≈16 (finished) · gemini finished | `r2/grok-ruling-r2.md` present (Grok wrote it itself, closing line `TRIBUNAL R2: BUILD`); no TIMEOUT |
| 10:48:18 | Grok independence greps + FOLD greps | — | Grok counts 0, 0; FOLD greps 1, 1, 1 |
| 10:49:18 | before writing the collate (`date` after the P-mechanics greps) | — | wrote §3 |
| 10:50:44 | after Rulings table + Wording written | — | wrote `## Checked against the files` … `## Independence` |
| 10:51:52 | before ESCALATE and close | — | wrote `## ESCALATE`, `§0`, last line |
| 10:52:31 | close (`date`) | none running | last line replaced with the stop line |

## Rulings table
Ruled: grok (own file `r2/grok-ruling-r2.md`, launched 10:31, notice 10:47:22, ≈16 min) and gemini (printed; hub wrote `r2/gemini-ruling-r2.md`; ≈2 min). Astra: `METER — proceed on three`, not launched. The Anthropic seat is not counted here (its round-2 report was not read).

| item | grok | gemini | agreement | NEITHER gist |
|---|---|---|---|---|
| R2-1 who deletes crash-leftover scratch | ADOPT B (changed its round-1 T8) | ADOPT B | 2-0 ADOPT B | none |
| R2-2 O1 fold mechanics | ADOPT S (changed its round-1 (g)) | ADOPT P | SPLIT 1-1 | none |
| R2-3 which slice builds the trading-logic draft | ADOPT B (no slice in V1–V4; request gets `unsupported`) | ADOPT A — slice V1, `trader_settings`, 12 h | SPLIT 1-1 | none |

**R2-1 sub-points**
| pt | grok | gemini |
|---|---|---|
| (a) heartbeat unlink? one function from two processes = one or two experts? | No; two experts under L40 (a second process calling the function is a second performer, not an ASK) | No; two experts, violates L40 |
| (b) `scratch_max_age_s ≤ stt_timeout_s` refusal required? | Yes, under both positions, for any sweep that runs while the resident stays up; walked turn `t-90` at 11:02:00; the `com.cobalt.aset` start sweep alone does not need it | Yes; a sweep could delete a long clip still being transcribed |
| (c) leftover after a quiet day; R18 (b); what A needs | Sits until next `com.cobalt.aset` start or next turn; R18 (b) does not bind a turn that never transcribed; A: heartbeat has no deleter and imports no voice module | Sits until next resident restart or turn; R18 (b) does not bind; A: heartbeat has no file deleters |
| (d) V4 probe / §9 V4 row | Probe only counts, never deletes; V4 row keeps "no (probes read)", closes the R2-1 tag as count-only; sweep on `com.cobalt.aset` in V1 | Probe only counts and alerts AMBER; V4 row must say it only reads/counts and never deletes |

**R2-2 sub-points**
| pt | grok | gemini |
|---|---|---|
| (a) whole diff/note vs target span | Target span; 16:40 typing elsewhere must not refuse, 16:41 editing the target must | "Both fail either way: F-09 disables the retry, making `_commit`'s whole-file mtime check immediately fatal if he types elsewhere in the note or edits the target itself" |
| (b) "note changed" vs "span changed"; does `_commit` refuse ANY byte change? | Span changed; `_commit` refuses any byte change between the writer's own read and write, not "since the read-back" | `_commit` refuses ANY byte change; P's "note changed" "accurately reflects this existing guard" |
| (c) "takes no retry" in law text? | Yes, in the law text | No, design (§2.6) only |
| (d) "remains his" inert? | Not inert (a stored `last_after` makes the new bytes the merge base) | Changes behaviour (avoiding ownership would mean bypassing `vault_writes`) |
| (e) law must match §2.6? | May state less; must not contradict; must state the baseline delta | May state the requirement; mechanics stay in the design |

FOLD lines vs each house's answer (checked by `grep -c -F` and by eye):
- **grok, ADOPT S:** FOLD A = the design's scope-A lead-in + scope-A clause + S's mechanics; FOLD B = scope-B clause + S's mechanics. The S mechanics string from "only when he orders …" to "Nothing else in this law changes." occurs once in the design (`VOICE-v3-derived-2026-09-23.md`, scope-B text) and FOLD B matches it (count 1); FOLD A's text through "since the read-back." matches with the scope-A clause swapped in (count 1); scope clauses verbatim (counts 1 and 1). A and B differ only in the scope clause. No difference to quote.
- **gemini, ADOPT P:** the P mechanics string ("his confirmation … is refused if the note changed since the read-back.") is present verbatim in BOTH FOLD lines (count 2 in its file; count 1 in the design); scope clauses verbatim; A and B differ only in the scope clause. DIFFERENCES from the design's fold text (`:299` / `:303` shape), quoted: the lead-in `[amended <date>] VOICE-ORDERED EDIT.` is absent; "only when he orders that exact edit in a turn of Cobalt's voice / text widget and confirms it: the widget reads back note, field and before → after; his confirmation" is written "when he orders that exact edit by voice and confirms it: his confirmation" (the word "only" and the read-back clause are absent); and the closing sentences "The trader is in the loop (as for `cobalt settings load --apply`, 2026-09-15); this is not a model-judged approval (L37). Nothing else in this law changes." are absent.

**R2-3 detail**
| | grok | gemini |
|---|---|---|
| slice | B (none in V1–V4) | A: V1 builds it |
| what it builds / covers | nothing in V1–V4; §2.4 stays the later slice; request → Plan kind `unsupported`, spoken line names the setting and the existing hand gate `cobalt settings load --card <file> --sha256 <hash> --apply` | targets: `trader_settings`; JSON artifact with new values + target sha256; HITL card via `notify/mattermost.py` `send_dm`; on his "approve" in the desk chat "the existing chat bot executes the trader-run settings apply under `settings/card.py`" |
| files / hours / RESTARTS | — | `cobalt/settings/propose.py`, `cobalt/aset/voice_tools.py`; 12 h; `com.cobalt.aset` and "desk chat bot" |
| before it ships | `unsupported` (not `refuse`), names the hand gate | "the voice agent is not live, so no request is refused" |
| L40: may the voice module APPLY? owner | No — only a draft to the owner: `settings/card.py` for `trader_settings` (his hand); `radar/propose.py` `apply` for a radar artifact | No — only a draft sent to the expert that owns it (the settings apply, `settings/card.py`) |

**closing line**
| house | `TRIBUNAL R2:` line, verbatim |
|---|---|
| grok | `TRIBUNAL R2: BUILD` |
| gemini | `TRIBUNAL R2: BUILD` |

**Per-item summary**
| item | outcome | why |
|---|---|---|
| R2-1 | **CONVERGED** — ADOPT B, 2-0 | both same letter; no supporting claim of either DOES NOT HOLD in the file-check (Gemini's/Grok's scenario claims are UNVERIFIABLE FROM READS, not contradicted) |
| R2-2 | **SPLIT** — grok ADOPT S, gemini ADOPT P | different letters; also two of gemini's supporting claims DOES NOT HOLD as worded (see `## Checked against the files` G5, G6) |
| R2-3 | **SPLIT** — grok ADOPT B, gemini ADOPT A (V1) | different answers; one of gemini's supporting claims DOES NOT HOLD as worded (G10) |

## Wording offered, verbatim
No house offered a `NEITHER`. Every FOLD line, the R2-3 slice text and every reasoning block, UNEDITED, house by house. REDACTIONS (L32): 2 spans in Grok's text, marked `[user data]` (an example spoken setting value and an example lesson phrase, almost certainly Grok's own synthetic scenarios); nothing else.

### GROK (`r2/grok-ruling-r2.md`, whole file)

(heading levels of Grok's own headings lowered by the hub so they do not read as report sections; no word changed)

##### GROK — VOICE v3 tribunal, round 2

##### R2-1

ADOPT B

I change my round-1 T8. "One unlink function" shared by the turn and a heartbeat sweep is two experts under L40, not one: `com.cobalt.heartbeat` (`ops/com.cobalt.heartbeat.plist:6`, its own `StartInterval` at `:60-61`) is a different process from the voice module's resident `com.cobalt.aset` (`ops/com.cobalt.aset.plist:6`), and L40's other roles ASK the owner — they do not perform the side effect.
`take_beat` (`src/cobalt/heartbeat/runner.py:126-167`) runs probes and `jobs.watchdog.sweep`; it does not import the voice module (`runner.py:41-60`). No `unlink` / `os.remove` / `rmtree` exists under `src/cobalt/heartbeat` (deleters today: `archiver/shadow.py:234`, `redact/secrets.py:280`, `vaultwrite/writer.py:478`, `radar/collector.py:108`, `backup/restic.py:197`).
§5's "on every heartbeat, a sweep deletes" (`docs/30 - Design/VOICE-v3-derived-2026-09-23.md:108`) contradicts §9 V4 "no (probes read)" (`:161`). Hub FC5 HOLDS. B is the smaller fix that makes both sentences true: the voice module deletes, the probe reads.
The agreed `com.cobalt.aset` start sweep stays. B's per-turn sweep is the same module and the same unlink, so it does not add an expert.

(a) No. The heartbeat process may not unlink a scratch file; one unlink function called from the two residents is two experts under L40, not one — the expert is the voice module's process, and a second process calling the function is a second performer, not an ASK.
(b) Yes, under both positions, for any sweep that runs while the resident stays up. At 11:02:00 turn `t-90` writes `/Users/cobalt/.cobalt/voice-scratch/t-90.webm` and is still inside `stt_timeout_s`; with `scratch_max_age_s ≤ stt_timeout_s` the file is already old enough to sweep, so A's next `take_beat` unlinks it under the Transcriber, and B's start of turn `t-91` does the same — the schema refusal (L10) is what stops that config loading. The `com.cobalt.aset` start sweep alone does not need it: that process's previous transcribe is already dead.
(c) Under B, with no restart and no later turn, `/Users/cobalt/.cobalt/voice-scratch/t-12.webm` from the 09:31:07 death sits the whole day, until the next `com.cobalt.aset` start or the next turn; R18(b) "deleted once transcribed" does not bind it, because that turn never transcribed. Under A the heartbeat would need a scratch deleter it does not have: no file deleter in its tree, and `runner.py:41-60` imports no voice module (`sweep` there is the job watchdog).
(d) V4's `voice_scratch` probe only counts files older than `scratch_max_age_s` and never deletes; §9's V4 row must keep "no (probes read)", close the R2-1 tag as count-only, and leave the sweep on `com.cobalt.aset` in V1.

##### R2-2

ADOPT S

I change my round-1 (g). P's "refused if the note changed" is wrong: at 16:40 he types in the risk paragraph of the same note while a lesson-span confirm is pending, Obsidian saves, and a note-level sha refuses and re-reads a span he did not touch (`docs/40 - DevDocs/reports/voice-v3-tribunal-fable-r1-2026-09-23.md:61-66`; the loop).
At 16:41 he edits that lesson line. Only a sha of that span's before and after bytes refuses and re-reads. P's "that one diff" plus a note-level refusal does not do this.
`_commit` (`src/cobalt/vaultwrite/writer.py:464-469`) already refuses any whole-file sha256 or mtime change between the writer's snapshot and the write. It does not cover the read-back-to-confirm window, so P's clause is not the guard the writer already has.
`_write_with_retry` (`writer.py:530-552`) rebuilds once after `NoteChangedOnDisk`. At 16:44:01 a `_precommit_hook` write into the target (`writer.py:461-462`; design X2) is overwritten on attempt 2. "Takes no retry" is that refusal, and §2.6 `[F-09]` already binds it for every confirmed act.
`_baseline` returns `last_after` (`writer.py:810`). `_merge_base` (`writer.py:807-830`) takes that as what Cobalt wrote, and anything else on disk is his and wins. A disk match is Cobalt's to replace. P never says otherwise. S's last sentence is the L28 change, not a restatement of human-wins.

(a) Bind the confirm to the target span, not the whole diff or the note. At 16:40 the risk-paragraph keystrokes change the note and must not refuse the pending lesson confirm; the span bytes still match, the risk paragraph is left as he typed it. At 16:41 he edits the lesson span itself; the span sha mismatches, the write is REFUSED, and the new before → after is read back.
(b) Refuse when the span changed since the read-back, not when the note changed — the 16:40 case is a note change with an unchanged span. `_commit` (`writer.py:464-469`) does refuse any byte change between the writer's own read and its write (file sha256 or `mtime_ns`); it does not implement "since the read-back".
(c) "Takes no retry" belongs in the law text: "through `VaultWriter`" otherwise includes `_write_with_retry`'s second build (`writer.py:530-552`), and the span check run once before that call does not see the 16:44:01 overwrite of the target (X2).
(d) Not inert. A write that stores `last_after` makes the new bytes the merge base (`writer.py:810`, `_merge_base` at `:807-830`: base is what Cobalt wrote; a later upsert whose disk still equals that base replaces them). At 16:55 he confirms the lesson span "[user data]"; without the sentence that span is Cobalt's on the next merge, with no new confirm.
(e) The law may state less than §2.6 builds (confirm-word list, TTL, single-flight stay in the design). It must not contradict §2.6, and it must state the L28 delta §2.6 does not: the replaced span does not become Cobalt's baseline.

FOLD A: [amended <date>] VOICE-ORDERED EDIT. Cobalt may replace text outside marker units — his text included — only when he orders that exact edit in a turn of Cobalt's voice / text widget and confirms it: the widget reads back note, field and before → after; his confirmation (a word from the closed confirm list matched by code, or a tap) is bound by sha256 to that target span's before and after bytes; the write replaces only that span, goes through `VaultWriter` with the mtime guard and `_session_gate`, takes no retry, is versioned with before, after and the turn id, and is refused if the span changed since the read-back. The replaced text remains his: no Cobalt ownership of it is created. The trader is in the loop (as for `cobalt settings load --apply`, 2026-09-15); this is not a model-judged approval (L37). Nothing else in this law changes.
FOLD B: [amended <date>] VOICE-ORDERED EDIT. Cobalt may replace text HE wrote — outside marker units, or inside a unit whose body is his (his voice units) — only when he orders that exact edit in a turn of Cobalt's voice / text widget and confirms it: the widget reads back note, field and before → after; his confirmation (a word from the closed confirm list matched by code, or a tap) is bound by sha256 to that target span's before and after bytes; the write replaces only that span, goes through `VaultWriter` with the mtime guard and `_session_gate`, takes no retry, is versioned with before, after and the turn id, and is refused if the span changed since the read-back. The replaced text remains his: no Cobalt ownership of it is created. The trader is in the loop (as for `cobalt settings load --apply`, 2026-09-15); this is not a model-judged approval (L37). Nothing else in this law changes.

##### R2-3

ADOPT B

§2.4 stays the later slice: a `trading_logic: true` tool is drafted as the exact change plus sha256 and sent, never executed (`docs/30 - Design/VOICE-v3-derived-2026-09-23.md:72`). No V1–V4 row builds that drafter (`:158-161`). Same shape as DRC, which V1 does not build and does not ban.
In V1–V4 the Plan kind is `unsupported` (`:68`), not `refuse`. At 10:41 "set my max risk to [user data]" the spoken line names the setting and the hand gate that already exists, `cobalt settings load --card <file> --sha256 <hash> --apply` (`settings/card.py:10-20`; trader-run apply is token-exempt at `:15`). It does not say the class is forbidden and does not name L7 as a ban.
`:144` joins his-text overwrite with trading logic under "spoken refusal naming the field and the law". That wording stays for his text until O1. Read as a ban on trading-logic requests, it is the class refusal F-07 did not fold, and it is not what those requests get.
The seat's "refuse until a slice builds it" re-opens R18(a). An unbuilt tool returning `unsupported`, with the command still specified in §2.4, does not.
`send_dm` (`notify/mattermost.py:130`) is send-only; that module is not a desk-chat listener (`:1-15`; only the heartbeat calls it, `heartbeat/runner.py:299`). V1–V4 do not call `radar/propose.py:711` `apply` and do not pass `--apply`.

Applying a trading-logic change is not an act the voice module may do under L40 — only a draft to the expert that owns it: `settings/card.py` for `trader_settings` (his hand), `radar/propose.py` `apply` for a radar artifact (non-empty `--hitl` at `:741`, target sha256 at `:734-737`, not `market_reset` at `:742-743`).

OWNER: none. R2-1 is which process unlinks scratch (L40, houses). R2-2 is fold mechanics (houses); O1's scope is already his and is not repeated. R2-3 is which slice builds a drafter (houses). None is his money, his data, his time, or a law no house can decide, and none is a precondition for a slice that does not need it.

EXPERIMENTS: none. No claim about Python, launchd, Obsidian, the writer, or a speech engine was used beyond the excerpts. E1–E11 and X1–X5, X12, X13 stand as already named.

TRIBUNAL R2: BUILD

### GEMINI (`r2/gemini-ruling-r2.md`, whole file; no redaction needed)

**R2-1**
ADOPT B
(a) No; one unlink function called from two processes creates two experts for the same side effect, violating L40.
(b) Yes; if `scratch_max_age_s` ≤ `stt_timeout_s`, a sweep could delete a long clip that is still actively being transcribed by the STT engine.
(c) It sits until the next resident restart or turn; R18(b)'s "deleted once transcribed" does not bind a dead turn that never transcribed. Under A, the heartbeat would need an `unlink` capability (it has no file deleters today).
(d) The V4 `voice_scratch` probe only counts leftovers and alerts AMBER; §9's V4 row must state that it only reads/counts and never deletes.

**R2-2**
ADOPT P
(a) Both fail either way: F-09 disables the retry, making `_commit`'s whole-file mtime check immediately fatal if he types elsewhere in the note or edits the target itself.
(b) `_commit` already checks the mtime and sha256 of the whole file, refusing ANY byte change; P's "note changed" accurately reflects this existing guard.
(c) "takes no retry" is an implementation mechanic belonging in the design (§2.6), not in the law text.
(d) It changes behaviour: to prevent Cobalt ownership, the write would have to bypass `vault_writes`, breaking `upsert_region`'s future 3-way merges.
(e) The law text may state the requirement (the confirmation and refusal) while leaving the precise mechanics (like disabling the retry) to the design.
FOLD A: Cobalt may replace text outside marker units — his text included — when he orders that exact edit by voice and confirms it: his confirmation (a word from the closed confirm list matched by code, or a tap) is bound by sha256 to that one diff; the write is the smallest span (that field's value), goes through `VaultWriter` with the mtime guard and `_session_gate`, is versioned with before and after and the turn id, and is refused if the note changed since the read-back.
FOLD B: Cobalt may replace text HE wrote — outside marker units, or inside a unit whose body is his (his voice units) — when he orders that exact edit by voice and confirms it: his confirmation (a word from the closed confirm list matched by code, or a tap) is bound by sha256 to that one diff; the write is the smallest span (that field's value), goes through `VaultWriter` with the mtime guard and `_session_gate`, is versioned with before and after and the turn id, and is refused if the note changed since the read-back.

**R2-3**
ADOPT A
Slice V1 builds it. Targets: `trader_settings`; the tool drafts a JSON artifact carrying the new values and target sha256, sending a HITL card via `notify/mattermost.py` `send_dm`; upon his 'approve' in the desk chat, the existing chat bot executes the trader-run settings apply under `settings/card.py` (which is exempt from the token). Files: `cobalt/settings/propose.py`, `cobalt/aset/voice_tools.py`; Hours: 12; RESTARTS: `com.cobalt.aset` and desk chat bot. Before V1 ships, the voice agent is not live, so no request is refused.
Applying a trading-logic change is not an act the voice module may do under L40; it is only a draft sent to the expert that owns the change (the settings apply, `settings/card.py`).

TRIBUNAL R2: BUILD

## Anthropic-seat round-1 claims, file-checked
Done WHILE the houses ran. Each row: the real file opened with Read on main at HEAD `279a7be` (the working tree of `/Users/cobalt/cobalt`), plus `grep -n`. The Anthropic seat's round-2 report (`25`) was NOT read.
| # | claim (source line) | file:line | verdict | note (≤30 words) |
|---|---|---|---|---|
| C1 | (seat T6, `voice-v3-tribunal-fable-r1-2026-09-23.md:64`) `_write_with_retry` re-reads and re-builds ONCE after `NoteChangedOnDisk` (`writer.py:530-552`) | `src/cobalt/vaultwrite/writer.py:530-553` | **HOLDS** | `for attempt in (1, 2)`: each pass takes a fresh `_snapshot` and re-runs `build`; `NoteChangedOnDisk` at attempt 1 → `continue`, at attempt 2 → `raise`. Function ends at :553, not :552. |
| C2 | (packet fact, R2-2 (b)) `_commit` refuses when the file's sha256 or mtime changed since the writer's own snapshot (`:457-470`, check at :464) | `writer.py:457-470`, `:526-527`, `:536` | **HOLDS** | :464 `if current.sha256 != snapshot.sha256 or current.mtime_ns != snapshot.mtime_ns:` raises `NoteChangedOnDisk`. WINDOW: `_snapshot` at :536 (writer's read) → `_commit` at :527. It does NOT cover read-back → his confirm. |
| C3 | (seat T8, `…fable-r1…:74`) `com.cobalt.heartbeat` is a launchd job separate from `com.cobalt.aset`, and no code under `src/cobalt/heartbeat` deletes a file today | `ops/com.cobalt.heartbeat.plist:6`; `ops/com.cobalt.aset.plist:6`; `greps.txt` deleters; own extra grep | **HOLDS** | Two plist files, two Labels; heartbeat runs `cobalt jobs run com.cobalt.heartbeat … heartbeat beat` (:30-43) at `StartInterval` 900 (:61). Deleters list has no heartbeat file; a wider grep in `heartbeat/` finds only `removeprefix` (`runner.py:207`). |
| C4 | (seat T8 = round-1 FC5, re-opened on the DERIVED text) §5's crash-leftover bullet vs §9's V4 row | `docs/30 - Design/VOICE-v3-derived-2026-09-23.md:108` vs `:161` (and V1 row `:158`) | **HOLDS** (still reads differently; the derived text marks it OPEN) | §5 `:108`: "on resident start and on every heartbeat, a sweep deletes any scratch file older than `scratch_max_age_s`; finding one is AMBER … an unlink that fails is RED (L9)." §9 V4 `:161`: "`voice_stt` / `voice_plan` / `voice_scratch` probes; … \| no (probes read) \| — \| V1; R2-1 for the `voice_scratch` probe's delete-or-count \| the heartbeat resident \| 2". V1 `:158` carries "scratch lifecycle + sweep". |
| C5 | (seat T4 (2), `…fable-r1…:55`) no slice in the derived §9 builds a HITL-card or draft-and-send tool, and no `trading_logic` mention or HITL-card sender exists under `src/cobalt` | design `:152-164`; `greps.txt`; own `grep -n -i hitl\|draft\|send_dm\|notify` on the design | **HOLDS** | V1–V4 rows (`:158-161`) name no HITL, draft or `send_dm` work; the design's HITL/draft hits are :72, :123, :259, :280 (prose about the gap). `src/cobalt`: zero `trading_logic` hits; `send_dm` callers are only the heartbeat's two alert paths (`runner.py:372`, `:483`). `hitl_proposals` (`db_migrations/placement.py:135`) is a frozen OLD-TREE table name, not a sender. |
| C6 | (seat (g), `…fable-r1…:162`) the replaced text "remains his", and "a later Cobalt merge never treats it as Cobalt's baseline" | `writer.py:807-810` (`_baseline`), `:621-641` (`_seed_baselines`), `:724`, `:766` (`upsert_unit`), `:943`, `:963-972` (`upsert_region`), `:507-522` (`_persist_and_write`); `vaultwrite/store.py:91-109` (`last_after`) | **PARTLY HOLDS · behaviour UNVERIFIABLE FROM READS** | Baseline = `vault_writes.unit_after` of the newest row for (note, section, unit), read by `store.last_after`. `upsert_unit` AND `upsert_region` (the only marker-less op today) both write a `unit_after` row, so both RECORD a baseline. No voice-overwrite op exists; whether the seat's sentence is inert depends on the op it will use. Run: dev vault + `cobalt_dev`, one marker-less span written twice through the chosen op with a hand edit between, then read the `vault_writes` rows and the merge result (= E9-shaped; NEW). |
| C7 | (packet fact, R2-3) `radar/propose.py` `apply` refuses on a changed target sha256, on an empty `--hitl`, and inside `market_reset` | `src/cobalt/radar/propose.py:711-760` | **HOLDS** | :715 artifact digest ≠ `--sha256` → refuse; :733-737 target note sha256 ≠ artifact's → refuse; :740-741 empty `str(args.hitl).strip()` → refuse; :742-743 `current_session() is Session.MARKET_RESET` → refuse. `--hitl` is only checked non-empty (a free-text label; L7's own note says so). |
| C8 | (packet fact, R2-3) `notify/mattermost.py:130` `send_dm` is outbound only: no inbound reader in that module | `src/cobalt/notify/mattermost.py` (defs at :47, :61, :65, :103, :130; body :103-168) | **HOLDS** | Module defs: `timeout_s`, `MattermostError`, `_creds`, `_api`, `send_dm`. `_api` is one HTTP call; `send_dm` reads only `/users/me` and `/users/username/…` (ids), opens the direct channel and POSTs `/posts`. No message reader, poller or websocket (:8-11 says so). |

Count: **Anthropic-seat R1 claims checked: 7 HOLD of 8 checked** (C1, C2, C3, C4, C5, C7, C8 HOLD; C6 PARTLY HOLDS — its baseline-recording part HOLDS, its behaviour part is UNVERIFIABLE FROM READS + the run named in the row; none DOES NOT HOLD).

## Checked against the files
Real files opened by the hub (Read / `grep -n`) on main HEAD `279a7be`. `= C<n>` = same as a row of `## Anthropic-seat round-1 claims`. Arguments that are readings of a law (L40, R18) with no file claim are not rows.

**Gemini**
| # | claim · who · | file:line | verdict | note |
|---|---|---|---|---|
| G1 | R2-1 (c) "Under A, the heartbeat would need an `unlink` capability (it has no file deleters today)" · gemini | `greps.txt` deleters; `heartbeat/` broader grep = `= C3` | **HOLDS** | No deleter under `src/cobalt/heartbeat`; only `removeprefix` (`runner.py:207`). |
| G2 | R2-1 (b) a sweep could delete a long clip still being transcribed when `scratch_max_age_s ≤ stt_timeout_s` · gemini | no code exists yet (voice module unbuilt) | **UNVERIFIABLE FROM READS** | Run (dev, synthetic long clip): a sweep fired while the transcribe is in flight, with the age key ≤ the STT timeout key; expected result = the file is unlinked under the Transcriber. Related to derived E7 but not the same run: **NEW**. |
| G3 | R2-1 (c) under B a leftover "sits until the next resident restart or turn" · gemini | seat T8 text (`seat-r1.excerpt.md`); design `:108` | **HOLDS** (as B's own wording) | B sweeps "on `com.cobalt.aset` start and at the start of every turn"; no timer job is named in B. |
| G4 | R2-2 (a) "F-09 disables the retry, making `_commit`'s whole-file mtime check immediately fatal if he types elsewhere in the note or edits the target itself" · gemini | `writer.py:536`, `:526-527`, `:464`; design `:78` | **DOES NOT HOLD as worded** | F-09 disabling the retry HOLDS (`:78`). But the writer takes its snapshot at execution (`:536`) and `_commit` compares against THAT snapshot (`:464`); typing elsewhere BEFORE execution is absorbed by the fresh snapshot. Only a byte change inside snapshot→commit refuses (= C2). |
| G5 | R2-2 (b) `_commit` refuses ANY byte change; P's "note changed" "accurately reflects this existing guard" · gemini | `writer.py:464`; P text `:299` "refused if the note changed since the read-back" | first half **HOLDS** (= C2); second half **DOES NOT HOLD as worded** | The guard's window is writer's read → write; P's clause is "since the read-back", a longer window the guard does not cover. |
| G6 | R2-2 (d) avoiding Cobalt ownership "would have to bypass `vault_writes`, breaking `upsert_region`'s future 3-way merges" · gemini | `writer.py:963-972`, `:946-951`, `:857-859`; `vaultwrite/store.py:91-109`; `merge.py:125-135` | **PARTLY HOLDS · rest UNVERIFIABLE FROM READS** | `upsert_region` records `unit_after` in `vault_writes` (the baseline). With no row, `_merge_base` returns `missing` (`:857-859`) and `upsert_region` uses base = the human's text (`:947`), so `merge3` lets Cobalt's next text apply. That a voice op "would have to" bypass is a claim about an unbuilt op (= C6 run). |
| G7 | R2-2 FOLD A/B mechanics = P verbatim; scope clauses verbatim · gemini | design `:299`; `grep -c -F` | **HOLDS** | Count 2 in its file, 1 in the design; differences from the design's fold text are quoted in `## Rulings table`. |
| G8 | R2-3 "`cobalt/settings/propose.py`" as a file to add · gemini | `ls src/cobalt/settings` | **HOLDS as a NEW file** | Directory holds `__init__.py, card.py, cli.py, migrations, models.py, store.py`; no `propose.py` exists today. |
| G9 | R2-3 "sending a HITL card via `notify/mattermost.py` `send_dm`" · gemini | `notify/mattermost.py:130-168` | **HOLDS** | `send_dm` posts a DM (`/posts`) after `redact()`; outbound only (= C8). |
| G10 | R2-3 "upon his 'approve' in the desk chat, the existing chat bot executes the trader-run settings apply under `settings/card.py` (which is exempt from the token)" · gemini | LAWS.md L7 (`:57`); `settings/card.py:15-16`; `settings/cli.py:6,105-106`; `cobalt_agent/interfaces/mattermost.py:380-419`; `notify/mattermost.py` (= C8) | **DOES NOT HOLD as worded** | L7: his "approve" in the desk chat is the approval and "the hub executes on the desk's relay". `card.py:15-16`: the token exemption is for a TRADER-RUN apply; `cli.py:105-106`: "A trader-run apply names the exact bytes it loads". The only inbound `approve` handler in the repo is the OLD tree's `interfaces/mattermost.py:380-419` (an old-tree proposal engine, `bypass_hitl=True` at :419); it has 0 references to `cobalt settings`. New core has no inbound reader (= C8). |
| G11 | R2-3 the tool "drafts a JSON artifact carrying the new values and target sha256" · gemini | `settings/card.py:10-13`; `radar/propose.py:422-430` | **NOTE (proposal, not a claim of today's code)** | The settings apply consumes a card FILE plus `--sha256` of its bytes; the JSON artifact with `target_note_sha256` is `radar/propose.py`'s shape. The two are different mechanisms. |
| G12 | R2-3 RESTARTS "`com.cobalt.aset` and desk chat bot" · gemini | `ls ops/` | **UNVERIFIABLE FROM READS** | `ops/` holds no job named for a "desk chat bot"; it holds `com.cobalt.agent.plist` (old tree) and `cto-desk.sh`. Which is meant is not stated; L42 derives restarts by rule at build. |
| G13 | R2-3 "Hours: 12" · gemini | design `:158` (V1 = 9 h) | **UNVERIFIABLE FROM READS** | A seat-hour estimate, not a fact; V1's derived row says 9 h GUESS. |

**Grok**
| # | claim · who | file:line | verdict | note |
|---|---|---|---|---|
| K1 | R2-1 the two plists, own Labels; `StartInterval` at `:60-61` · grok | `ops/com.cobalt.heartbeat.plist:6,60-61`; `ops/com.cobalt.aset.plist:6` (= C3) | **HOLDS** | `:60` key, `:61` `900`. |
| K2 | R2-1 `take_beat` runs probes and `jobs.watchdog.sweep`; imports no voice module · grok | `heartbeat/runner.py:126-167`, `:41-60` | **HOLDS** | Imports list carries no voice module (none exists yet); `sweep` is `cobalt.jobs.watchdog.sweep`. |
| K3 | R2-1 the deleters list · grok | `greps.txt`; `archiver/shadow.py:234`, `redact/secrets.py:280`, `writer.py:478`, `radar/collector.py:108`, `backup/restic.py:197` (= C3) | **HOLDS** | Exact five hits. |
| K4 | R2-1 §5 `:108` contradicts §9 V4 `:161`; hub FC5 HOLDS · grok | design `:108`, `:161`; hub row FC5 (= C4) | **HOLDS** | Quoted in C4. |
| K5 | R2-1 (b) `t-90` at 11:02:00; A's next `take_beat` and B's start of turn `t-91` unlink it under the Transcriber · grok | none (voice module unbuilt) | **UNVERIFIABLE FROM READS** | Same run as G2 (**NEW**); "B's start of turn `t-91`" also needs a second turn to start while the first transcribes, which no excerpt settles. |
| K6 | R2-1 (b) "the `com.cobalt.aset` start sweep alone does not need it: that process's previous transcribe is already dead" · grok | none | **UNVERIFIABLE FROM READS** | A `kill -9` + restart run: derived E7. |
| K7 | R2-1 (c) leftover sits until next start or turn under B; A needs a deleter it lacks · grok | seat T8 text; `greps.txt`; `runner.py:41-60` | **HOLDS** | = G1, G3. |
| K8 | R2-2 the seat's 16:40 typing-loop scenario, cited `…fable-r1…:61-66` · grok | `voice-v3-tribunal-fable-r1-2026-09-23.md:61-66` | **HOLDS as a citation** | The scenario is at :63; it is the seat's reasoning, not a run (L70). |
| K9 | R2-2 `_commit` `:464-469` refuses any sha256/mtime change between the writer's snapshot and write; not the read-back→confirm window · grok | `writer.py:457-470` (= C2) | **HOLDS** | |
| K10 | R2-2 `_write_with_retry` `:530-552` rebuilds once; at 16:44:01 a `_precommit_hook` write into the target (`:461-462`) is overwritten on attempt 2 · grok | `writer.py:530-553`, `:461-462` (= C1) | first part **HOLDS**; the overwrite **UNVERIFIABLE FROM READS** | Run = derived **X2** (dev vault, hook writing into the target between snapshot and commit). |
| K11 | R2-2 `_baseline` returns `last_after` (`:810`); `_merge_base` takes it as what Cobalt wrote, anything else on disk is his and wins · grok | `writer.py:807-810`, `:817-892`; `store.py:91-109` | **HOLDS** | `_merge_base` def starts `:817` (grok cited `:807-830`, the packet's certified range, which ends mid-docstring); `:860-861`, `:892` return `last_after`; a differing on-disk body is the human's (`merge3`). |
| K12 | R2-2 (d) a later upsert whose disk still equals the base replaces the new bytes; "without the sentence that span is Cobalt's on the next merge, with no new confirm" · grok | `writer.py:733`, `:951`; `merge.py:125-135` | first part **HOLDS**; second **UNVERIFIABLE FROM READS** | An unedited base group takes Cobalt's lines. Whether the (unbuilt) voice op stores `unit_after` = the C6 run. |
| K13 | R2-2 FOLD A/B = S mechanics with the scope clauses swapped · grok | design `:303`; `grep -c -F` (counts 1, 1, 1) | **HOLDS** | See `## Rulings table`. |
| K14 | R2-3 §2.4 text at `:72`; no V1–V4 row builds a drafter (`:158-161`); "same shape as DRC, which V1 does not build" · grok | design `:72`, `:158-161` (= C5) | **HOLDS** | DRC is V2 (`:159`). |
| K15 | R2-3 the Plan kind `unsupported` exists (`:68`) and is what a trading-logic request gets in V1–V4 · grok | design `:68`, `:72`, `:144` | **HOLDS that the kind exists; the routing is grok's PROPOSAL** | `:68` lists `answer, act, clarify, unsupported, refuse`. Two texts, both quoted, smoothed by neither: design `:72` "is never executed by voice — it is drafted … and sent to him as a HITL card"; design `:144` "His-text overwrite (until O1) / trading logic \| spoken refusal naming the field and the law". |
| K16 | R2-3 the hand gate `cobalt settings load --card <file> --sha256 <hash> --apply`, `settings/card.py:10-20`, token-exempt at `:15` · grok | `settings/card.py:10-16`; `settings/cli.py:6-7,105-106` | **HOLDS** | "A trader-run apply is exempt from the HITL token (L28, amended 2026-09-15)". |
| K17 | R2-3 `send_dm` send-only; not a desk-chat listener (`:1-15`); only the heartbeat calls it (`runner.py:299`) · grok | `notify/mattermost.py:1-15,130-168`; `greps.txt` (= C8) | **HOLDS** | Callers: `heartbeat/runner.py:299/304/372/483` (+ re-exports in `notify/__init__.py`). |
| K18 | R2-3 `radar/propose.py` apply: `--hitl` non-empty `:741`, target sha256 `:734-737`, not `market_reset` `:742-743` · grok | `radar/propose.py:711-760` (= C7) | **HOLDS** | |
| K19 | R2-3 design `:144` wording quoted · grok | design `:144` | **HOLDS** | Verbatim. |
| K20 | "I change my round-1 T8 / (g)" · grok | `grok-r1-own.excerpt.md` | **HOLDS** | Round-1 T8: "One unlink function for the turn and the sweep."; (g): "The fold text is correct and minimal". |

Two houses contradicting each other, quoted, smoothed by neither: on whether `_commit` matches P's clause — grok "P's clause is not the guard the writer already has" (`writer.py:464-469` covers writer read → write only) against gemini "P's 'note changed' accurately reflects this existing guard". The hub's reading of `:464` and `:536` is under G5 and K9.

## Experiments named (L70)
Named by the houses: **none** (grok wrote `EXPERIMENTS: none`; gemini wrote no `EXPERIMENTS:` line). Not house-named, but UNVERIFIABLE rows above and the run that settles each (for the second derive; the hub adds none of its own as a house claim): (1) G2/K5 — a sweep firing while a long synthetic clip transcribes, age key ≤ STT timeout key: **NEW**, would gate V1's config check; (2) K6 — `kill -9` then restart, leftover swept: **= derived E7**; (3) K10 — `_precommit_hook` write into the target on attempt 2: **= derived X2**; (4) C6/K12 — a marker-less span written twice through the chosen voice op with a hand edit between, then read `vault_writes` and the merge result: **NEW** (E9-shaped), would gate V3's overwrite class.

## OWNER answers
| house | line | NAMED / NOT NAMED | precondition to build |
|---|---|---|---|
| grok | "OWNER: none. R2-1 is which process unlinks scratch (L40, houses). R2-2 is fold mechanics (houses); O1's scope is already his and is not repeated. R2-3 is which slice builds a drafter (houses). None is his money, his data, his time, or a law no house can decide, and none is a precondition for a slice that does not need it." | no item offered (the line says why none passes the test); O1 = O1 (already his) | no |
| gemini | no `OWNER:` line written | — (no item offered) | no |

## Independence
`grep -c -F -e "-ruling"` on `grok-ruling-r2.md` → 0; on `gemini-ruling-r2.md` → 0. `grep -c -F -e "gemini-r1-own"` on grok's file → 0. `grep -c -F -e "grok-r1-own"` on gemini's file → 0. No breach in either text. (What a house opened is not observable from its text; both texts read only in their own terms.)

## ESCALATE
No recommendation is added (L37).
1. **Answers whose supporting claim DOES NOT HOLD (as worded):** gemini R2-2 (`G4`: typing elsewhere is "immediately fatal" — the writer re-snapshots at execution, `writer.py:536`; `G5`: P's "note changed" "accurately reflects" `_commit`, whose window is writer read → write only) and gemini R2-3 (`G10`: "the existing chat bot executes the trader-run settings apply" — L7 says the desk relay executes; `card.py:15-16` exempts a TRADER-RUN apply; the only inbound `approve` handler is the old tree's, with 0 references to `cobalt settings`).
2. **Text that may bear on R18, quoted, NOT judged by the hub:** grok R2-3 ADOPT B — "In V1–V4 the Plan kind is `unsupported` (`:68`), not `refuse`. … It does not say the class is forbidden and does not name L7 as a ban." and "The seat's 'refuse until a slice builds it' re-opens R18(a). An unbuilt tool returning `unsupported`, with the command still specified in §2.4, does not." (Grok says its answer is not a class refusal; the second derive weighs it.) Gemini's R2-3 text does not touch R18.
3. **Packet over 110 KB after the drop order:** 111,218 B (under 110 KiB = 112,640; over 110,000). All three drops applied (`writer.py:1-30`; `radar/cli.py` + `settings/card.py` ranges; design `:276-290`).
4. **REDACTIONS:** 0 in the packet; **2 in this report** — two example spans in Grok's R2-3 / R2-2 text (an example spoken setting value and an example lesson phrase), replaced by `[user data]`; likely Grok's own synthetic scenarios.
5. **Astra's probe:** `astra: METER — proceed on three` (`ERROR: You've hit your usage limit … try again at Sep 26th, 2026 6:47 AM`); not launched; Astra reads the FINAL on Sat 09-26 (09-22 R13).
6. **STAGGER (s1), prompt `19`:** `19: PAUSED by the desk` at preflight (10:17) and again at the launch gate (10:29–10:30): PAUSE file present and a `paused by the desk` line at `routing-x5-retro-2026-09-23.md:74`. The desk deletes `scratch/tribunal-bars-0920/routing-x5/PAUSE` after this stop line and relaunches `19` with its CONTINUE line. This run never touched the PAUSE file.
7. **For the desk, a prompt defect (fact, no ask):** `24` told the hub to state in `greps.txt` that this shell's `grep` honours `.gitignore`; the hub tested it and it does not (a gitignored folder was searched). `greps.txt` and `## Packet` say so.
8. **Gemini wrote no `OWNER:` and no `EXPERIMENTS:` line** (QUESTIONS-R2 asked for both); recorded as "no item offered" and "none named", not as a refusal. Grok wrote both lines ("none").

No `ASK DESK` lines. Also none of: a `DO NOT BUILD`; a path to his trading platform or an order; an Anthropic-seat claim that DOES NOT HOLD (C6's behaviour part is UNVERIFIABLE FROM READS + a named run); a number for an engine tunable; an owner item written as a precondition; a house that did not rule; an independence breach.

VOICE V3 TRIBUNAL R2 DONE · grok: TRIBUNAL R2: BUILD · gemini: TRIBUNAL R2: BUILD · astra: METER — proceed on three · houses that ruled: 2 of 3 · converged: 1 of 3 · ESCALATE: 8
