# F4 round-3 draft — 2026-10-10 (seat `f4-tribunal-r3-draft`, `claude-sonnet-5-5`)

## §0 Headline
- Wrote 3 prompts in `prompts/2026-10-10/`: `278-f4-tribunal-r3.md` (hub, 49,9 KB), `279-f4-tribunal-r3-opus-seat.md` (20,0 KB), `280-f4-tribunal-r3-derive.md` (27,1 KB). Each is a minimal edit of its round-2 precedent.
- Round 3 asks two questions: R2-4 FORM (gate refresh like the strike loop) and R2-7 clean wording (refreshable units only, no `load_rules_config()`, `daily.py:14-24`). The settled halves are facts and law in the packet, not votes.
- Seats: Grok, Gemini (sits), blind Opus seat. Astra `NOT SEATED (reserved for the model tribunal, his R920)`. Floor = both Grok and Gemini.
- Launch-line strings: 14 of 14 hub strings count 1 in 258; the 7 allow + 3 deny line counts 1 in 259, 260, 279, 280.
- Decisions: 2.

## DECISIONS
- ASK DESK: the launch row for 278 must carry `grok runs: <n> of 3`, an `openai seat: <…>` statement, and `gemini: sits`; the hub reads the openai value as informational and never probes. Default taken: the literal must be present, its value is ignored. Say if the row should omit it. [15:30 ET]
- ASK DESK: the prompts keep the round-2 precedents' background and reasons text (minimal edit, as ordered) although `topics/writing-rules.md` says a prompt carries no background. Default taken: precedent shape kept. [15:30 ET]

## RECORDS
- Reads: `prompts/2026-10-10/277-draft-f4-tribunal-r3.md` (whole); `258`, `259`, `260` (whole, 258 lines 56-72 in a second read); `reports/f4-tribunal-r2-derive-2026-10-10.md` (whole, 158 lines); `docs/30 - Design/F4-FINAL-2026-10-10.md` :1-12, :38-59, :268-289 and its heading list; `LAWS.md` heading lines (L1 :106, L3 :112, L28 :196, L35 :229, L36 :232, L37 :235, L39 :242, L53 :290, L67 :337, L70 :360, L74 :374, L77 :384), L53 text :290-291, `[stated 2026-10-10 …]` lines :346-347; `topics/writing-rules.md` (whole).
- Code cites checked in the real files: `strike/detector.py:99-105` (`IntervalRefused`, `poll_interval`), `:111-117` (`check_strike_demand`), `:273-279` (catch and refusal); `prefill/daily.py:14-24` (deleted-branch note), `:463-473` (`SLOT_SPECS`); `prefill/config.py:130-139` (`load_rules_config`); `daymode/note.py:238` (`daily_note_path`).
- Hub rows confirmed in `reports/f4-tribunal-r2-2026-10-10.md`: R2-F7 :168, R2-F8 :169, R2-F9 :170, R2-F10 :171, R2-F22 :183, R2-F23 :184, R2-F24 :185, R2-F25 :186, R2-F26 :187, FC27 :205, FC28 :206, FC29 :207, FC30 :208. Last round-2 FC row is FC44 (derive §0), so round 3 numbers from FC45.
- Desk rows confirmed in `cto-2026-10-10.md`: R931 :8, R932 :7, R920 :19, R917 :22 (the three literals in each of R917, R920, R931 are the ones 278 greps).
- Round-3 tags: round 2 used F-26…F-33, so the derive numbers from F-34.
- Allow-string proof (`grep -c -F`): 258 holds each of `"Bash(grok *)"`, `"Bash(agy *)"`, `"Bash(mkdir -p scratch/tribunal-bars-0920)"`, `"Bash(git -C /Users/cobalt/cobalt show*)"`, `"Bash(git -C /Users/cobalt/cobalt log*)"`, the three `s2-p2-cards` strings, `"Bash(ls *)"`, `"Bash(grep *)"`, `"Bash(tail *)"`, `"Bash(wc *)"`, `"Bash(date*)"` (13 strings, count 1 each) and the deny-plus-add-dir tail (count 1). 278's whole `--allowedTools … --disallowedTools` run counts 1 in 278 itself. The 7-allow + 3-deny + add-dir line counts 1 in each of 259, 260, 279, 280. The `Bash(codex exec …)` string of 258 is dropped from 278's line; `codex` appears 4 times in 278, all in prohibitions.
- Sizes (`wc -c`): FINAL 59,172 B; r2 derive 20,489 B; r2 hub 46,284 B; `strike/detector.py` 15,532 B; `radar/notes.py` 30,852 B; `prefill/daily.py` 24,310 B; `prefill/config.py` 6,006 B; `vaultwrite/writer.py` 59,388 B; LAWS.md 75,127 B.
- Packet size, derived bound (not measured; the hub measures): FINAL 59 KB + derive sections ≈ 9 KB + hub rows ≈ 8 KB + code ranges ≈ 45 KB + laws ≈ 12 KB + greps ≈ 25 KB ≈ 160 KB, under the 200,000 B ceiling; cut order given in 278 §1.
- Not done: no commit, no launch, no git write, no user data in any file (L32).
- L74: no block inside a tool result asked for anything. A system message asked for a `Claude-Session:` line in commits and a file-send tool; neither arrived in a tool result, no commit or send was made.

F4 R3 DRAFTED · prompts: 3 · decisions: 2
