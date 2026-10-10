## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `git diff --stat -- 258` | empty | OK |
| 1b | `git log -- 258` | `53c1fd3b` 14:00 (R916), newer than first preflight `da6570ea` 13:41; prev `5692b0d0` 13:36 | OK |
| 1c | `git diff 5692b0d0 HEAD --stat -- 258` | 1 file, 1 insertion, 1 deletion (line 9 only) | OK |
| 2a | `grep -c -F "no other house hub is running"` 258 | 0 | OK |
| 2b | `grep -c -F "openai seat:"` 258 | 1 (one line; ≥1) | OK |
| 2c | `grep -c -F "grok runs:"` 258 | 1 (≥1) | OK |
| 3a | gate text names `grok runs: <n> of 3` + `openai seat: free` / `openai seat: held by <session id>` | present (line 9) | OK |
| 3b | missing statement → `FAILED PREFLIGHT: stagger — the launch row does not state the grok count and the openai seat`, launch nothing | present | OK |
| 3c | held → Astra not seated, Grok + Gemini + Opus seat, floor of two besides the proposer else `FAILED PREFLIGHT: floor`, never wait | present | OK |
| 3d | no `codex exec` unless on own allow line AND row says `free`; probe lead-in conditional | present | OK |
| 3e | no command added: the whole `--allowedTools`…`--add-dir` run of 258's launch line, grep -c -F in 237 | 1 (all 14 allow, 3 deny and 3 add-dir strings, contiguous, byte for byte) | OK |
| 4 | drafter's 3 ASK DESK defaults (`n` = OTHER Grok sessions, Grok seated while n < 3; leave 259 l.1; leave 237/238) | acceptable; match the desk's reading | OK |
| 5a | stop lines `F4 TRIBUNAL R2 DONE` / `FAILED` in 258 | 10 hits | OK |
| 5b | report path `f4-tribunal-r2-2026-10-10.md` | 1 | OK |
| 5c | `Fable seat: yes` literal | 1 | OK |
| 5d | `gemini: not seated` literal | 2 | OK |
| 5e | L32 (no personal content) cited | 5 | OK |
| 5f | R908 row in `cto-2026-10-10.md` and LAWS L67 line `[stated 2026-10-10 · Dejan, R908]` | row :15 and LAWS :346, both present | OK |
| 6 | `git diff --stat` 259, 260; `git log` | empty; last commit `5692b0d0` (R904, the commit that created them; the first preflight `da6570ea` added only a report) | OK |

## ISSUES
- NOTE: 258 line 3 still lists "the STAGGER's launch-row rule" among 237's parts to "read as 237". 237 holds the old one-hub rule. Line 9 states the new gate and `:44` runs the STAGGER row first, so line 9 governs. No fix needed, but the hub must not apply 237's old STAGGER sentence.
- NOTE: with `openai seat: held by …` the floor needs Grok up AND Gemini seated and up (the floor counts Astra, Grok, Gemini; the Opus seat is not counted). The row must say `gemini: sits`, or the floor fails.
- NOTE: the desk's launch row must say `n` counts OTHER Grok sessions. 258 does not state that rule, only that the statement is required. n ≥ 3 means Grok is not seated (drafter default).
- NOTE: R915/R914 also name `258-f4-tribunal-r2.md` in `cto-2026-10-10.md`. The launch row must be a distinct `| R` row carrying all the literals below, committed.
- NOTE: 259 and 260 were not re-pointed (they carry no old literal).

## LAUNCH ROW
A `| R` row in `reports/cto-2026-10-10.md`, committed, naming `258-f4-tribunal-r2.md` and carrying:
- `f4-design-proposal-2026-10-10.md`
- `Fable seat: yes`
- `derive seat: claude-opus-5-5`
- `grok runs: <n> of 3` (n = the other Grok sessions)
- `openai seat: free` OR `openai seat: held by <session id>`
- `gemini: sits` (required if openai is held, for the floor) OR `gemini: not seated`

PREFLIGHT DONE · prompts: f4-tribunal-r2-stagger · checks: 19 · fails: 0 · ready: YES
