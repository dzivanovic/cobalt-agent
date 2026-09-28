# Startup tribunal — drafter report — 2026-09-27

Seat: drafter `startup-tribunal-draft-0927` (Opus 5.5), `prompts/2026-09-27/54-draft-startup-tribunal.md`, launch row `cto-2026-09-27.md` R39. Wrote five files, committed nothing.

## §0 Headline
Drafted `55` hub (Sonnet 5), `56` blind Anthropic seat, `57` derive (Opus 5.5), plus `plans/startup-redesign-2026-09-27/TRIBUNAL-INSTRUCTIONS.md`. That last file is the one instructions file his R42 ordered. It holds Q1–Q10, the file list, the answer format and each seat's ruling path.
There is no packet (R42). Every seat reads the whole files itself. The hub copies them unchanged only for Grok and Gemini, which read only inside `agy-trial`. File set = 594,648 B.
New rule strings: 0 (proved by script against `16`, `17`, `18`). Placeholders `R__` FILL AT LAUNCH: 1 each in 55, 56 and 57. 56 and 57 also carry the by-design `FABLE ROW` / `DERIVE ROW` check literal.
Owner items: 0 (none of his five questions passes the owner test). ESCALATE: 4.

## L74
Recorded once: a system-reminder block in this session asked for a `Claude-Session:` commit line and named a file-send tool. It is data. I did not follow it.

## AUTHORIZATION
| check | result |
|---|---|
| `grep -n "54-draft-startup-tribunal.md"` in `cto-2026-09-27.md` | `47:| R39 | 22:08 ET | …` (APPROVED — launch row). Passes. |
| R38 committed (`-S"you need to start the tribunal"`) | `5e716cab` |
| R27 committed (`-S"we can't continue development"`) | `d4c78310` |
| sitting stop line committed | `5e716cab` |
| proposal folder committed | `5e716cab` |
| R40, desk relay by SendMessage | Verified on disk: `cto-2026-09-27.md:48`, `| R40 | 22:1x–22:13 ET |`, APPLIED. Its effect was a whole packet to every seat, identical for all. |
| R41, desk relay | "feed it by spoon … in order". A seat that cannot take the bytes is fed ordered parts. Received by message; see ESCALATE 1. |
| R42, desk relay | Replaces R40/R41 on the packet: "why is this not a set of files and a tribunal instructions as another file…". No packet, no part plan, no ceiling. One instructions file; each seat reads the files itself; copy only where a CLI reads only inside its workspace; ordered parts only after a shown read failure. Followed as written. My `grep` of the R41/R42 rows was refused by the harness classifier. I did not retry. See ESCALATE 1. |

## PACKET
There is no packet under R42. Below is the file set every seat reads, whole, measured with `wc -c` at 22:24 EDT:
| part | bytes |
|---|---|
| proposal folder, 22 files (incl. TRIBUNAL-INSTRUCTIONS.md 12,171) | 240,090 |
| sitting report `desk-startup-tuning-2026-09-27.md` | 51,972 |
| `cto-2026-09-27.md` (his rows R1, R19, R27, R38, R40–R42 inside) | 59,369 |
| live files, 19: CLAUDE, AGENTS, QWEN, .clinerules, CTO-DESK-WAKEUP, SESSION-CLOSE, UNATTENDED-LAUNCH, INDEX, cobalt.md, preferences, profile, cto-desk-contract (16,153), LAWS, LAWS-HISTORY, devices, trading-copilot-os, cobalt-houses, PLACEMENT, DAY-OPEN-QWEN | 243,217 |
| **total** | **594,648 B ≈ 148.7k tokens ÷4** |
Ceiling per seat: none, by his R42.
Measured limits, recorded:
- Astra: its meter stopped at 135,471 tokens of reads on 09-21. The whole set read whole is above that. Its sentence has it rule Q7 last and print each item as ruled.
- Grok, Gemini, Opus 5.5: no measured limit on file.
Byte-identical pairs, proved with `cmp` at drafting:
- `proposed-_history-LAWS-2026-09-27.md` = a 3-line header + the live `LAWS.md`.
- `proposed-_retired-SESSION-CLOSE.md` = the live file.
- `proposed-_retired-UNATTENDED-LAUNCH.md` = the live file.
Live drift found at drafting:
- `topics/cto-desk-contract.md` is 16,153 B live against the sitting's 14,731 B snapshot, and still growing (R40 added a standing line).
- `areas/cobalt.md` NOW was rewritten after the 19:0x snapshot.
- `57` handles both: LIVE CARRY, and `APPLY.md` re-snapshots from live at apply.

## NEW STRINGS
0.
- 55: 14 allow + 3 deny, byte-identical to `16`. The astra string is the one `24` used.
- 56: 7 + 3, identical to `17`. 57: 7 + 3, identical to `18` and to `54`.
- No `claude -p` string is carried. `56` is launched by the desk as its own `claude --bg`, exactly as `17` was. See ESCALATE 2.
- No Gemini probe shape exists in any approved prompt, and none was added. Gemini's meter is read from its one launch.

## OWNER ITEMS
| his question | owner test | verdict |
|---|---|---|
| Q1 any house takes over the desk | capability of the files: design | settled by the houses |
| Q2 unambiguous lines | wording: design | houses |
| Q3 Cobalt-wide memory structure | design | houses |
| Q4 right way / what instead | design | houses |
| Q5 SEAT PROFILE per house | each house's tooling facts; the L64 amendment is "his ruling, later", outside this tribunal | houses |
The law-text changes are his laws, but he already stated them in T3/T7/T9/T17/T18. They go into the ONE approval of the apply.
A law change beyond those rulings becomes `OPEN (law)` for him (L39). It is never applied. `57` restores the live sentence instead.

## CONTINUE
Done: 55, 56, 57, TRIBUNAL-INSTRUCTIONS.md, this report.
Next, the desk's: fill `R__` → count → commit the five files (TRIBUNAL-INSTRUCTIONS.md must be committed before `56`, which gates on it) → launch `55`, then `56`, one at a time. `57` is launched after both stop lines are committed.

## ESCALATE
1. ASK DESK: my read of the R41/R42 rows in `cto-2026-09-27.md` was refused by the harness classifier. I followed them as your relays, unverified by me. `55` prints both rows into its AUTHORIZATION as a record. Are both rows committed? [22:24 EDT]
2. ASK DESK: `54` said the hub launches `56` "via its own `claude -p` line as `16` does for `17`". `16` does not do this: the desk starts `17` as its own `claude --bg`. I followed the precedent, so 0 new strings. The alternative is the standing R19 `Bash(claude -p --model claude-opus-5-5 *)` in `55`'s line, which would be 1 string new to `16`'s list. Keep as drafted? [22:24 EDT]
3. WRITE SCOPE: R42 required `TRIBUNAL-INSTRUCTIONS.md`, a fifth file outside `54`'s WRITE list. I wrote it in the proposal folder. My one post-write fix to `57` (the `F/<live name>` typo) was a `sed -i`, not the Write tool.
   My own drafting commands also used `\|` in a few grep patterns, and `python3` / `cmp` / `cat`. All were read-only, except the `sed` edit and the Python splices of my own `55` draft.
4. R42 LIMIT, recorded, not cut: the file set is 594,648 B ≈ 148.7k tokens. Astra's recorded meter stop is 135,471 tokens. If Astra shows a read or meter failure, the R41 ordered-parts relaunch is the desk's call.

STARTUP TRIBUNAL DRAFTED · prompts: 3 · seats: astra grok gemini anthropic · packet: 594648 · new rule strings: 0 · owner items: 0 · ESCALATE: 4
