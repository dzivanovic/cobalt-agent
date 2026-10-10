## §0 Headline
- Re-pointed the STAGGER gate of `258-f4-tribunal-r2.md` to R908 (grok count plus openai seat statement; OpenAI held → Astra not seated, floor of two holds). One file edited, all on line 9.
- The Astra probe is now conditional on `openai seat: free`. No command added, no `pgrep`.
- 259 and 260 do not carry the old literal. 237 and 238 are round 1 and already ran (R876), so they are untouched.

## DECISIONS
- ASK DESK: does `grok runs: <n> of 3` count this hub? Default: `n` is the other Grok sessions, and the hub refuses Grok when `n` is 3 or more, so Grok is not seated. 258 states only that the statement is required, not that rule. [desk]
- ASK DESK: 259 line 1 says "the STAGGER keeps the Opus seat off the day's code checks". It is left unchanged because it carries no old literal, but R908 does not cover the Opus seat. Default: leave. [desk]
- ASK DESK: 237 and 238 still carry the old "one Grok hub" wording. Default: leave, since they are round-1 prompts that already ran. [desk]

## RECORDS
- Read: 262, 258 (whole), 259 (whole). Grep over `prompts/2026-10-10/` for `STAGGER` and `no other house hub is running`.
- Hits for `STAGGER`: 237, 238, 258, 259, 262. The literal `no other house hub is running` appeared only in 258 (:9).
- Changed in 258, both on `:9`:
  - the STAGGER paragraph, rewritten to the R908 gate;
  - the Codex probe lead-in, now conditional on `openai seat: free`.
- Unchanged and still consistent: 258 `:3` (the STAGGER launch-row rule), `:13` (relaunch re-runs the STAGGER), `:44` (STAGGER row first).
- `git diff --stat` for 258: 1 file, 1 insertion, 1 deletion. The `:9` paragraph is the only changed line.
- `grep -c -F "no other house hub is running"` in 258 → 0. `grep -c -F "openai seat:"` in 258 → 1 (one line, which is ≥ 1).

STAGGER RE-POINTED · files: 1 · decisions: 3
