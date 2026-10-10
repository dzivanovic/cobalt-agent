# Two preflights draft — 2026-10-10 (seat `two-preflights`, `claude-sonnet-5-5`)

## §0 Headline
- Wrote `prompts/2026-10-10/288-kill-hub-text-preflight.md` (precedent 273, re-pointed to card 284 rows K1-K3) and `289-f4-tribunal-r3-preflight.md` (precedents 276 and 261, re-pointed to 278-280).
- Both are read-only Sonnet preflights; header, allow line, report shape copied from the precedents. Neither file name contains `card`.
- Reports: `reports/kill-hub-text-preflight-2026-10-10.md`, `reports/f4-tribunal-r3-preflight-2026-10-10.md`; stop lines as ordered.
- Not committed, not launched. Decisions: 1.

## DECISIONS
- ASK DESK: 288's check (6) pins the card's red-first counts, and `## LAUNCH ROW` names TIP, CHECK REPORT and HOUSE B (empty in 284's header). Default taken: the preflight lists them as literals for the desk, not as a FAIL. Say if empty fields should FAIL. [15:45 ET]

## RECORDS
- Reads: `287-draft-two-preflights.md` (whole); `273-kill-row-preflight.md`, `276-model-tribunal-preflight.md`, `261-f4-tribunal-r2-preflight.md`, `275-kill-row-repreflight-grok-read.md` (whole); `284-kill-hub-card.md` :1-83 (whole); `reports/f4-tribunal-r3-draft-2026-10-10.md` :1-26 (whole); `topics/writing-rules.md` :1-27.
- `git -C /Users/cobalt/cobalt log --oneline -3 -- 284-kill-hub-card.md` and the same for `278-f4-tribunal-r3.md` → `0891e083` (committed); `git status --short -- prompts/2026-10-10` → empty before my writes.
- `git -C /Users/cobalt/cobalt rev-parse --verify 6fe8d690` → `6fe8d69077fe2b7942ba74e59ed21fdb0e82f7b8`; `grep -c -F "6fe8d690"` of 284 → 3.
- `grep -c -F "codex"` of 278 → 4 (matches the draft report's 4); `grep -c -F "grok runs:"` of 278 → 1.
- Glob of `reports/` confirmed present: `kill-hub-card-draft`, `kill-row-preflight`, `kill-row-grok-read`, `kill-sequence-amend`, `kill-label-fix`, `f4-tribunal-r2-derive`, `f4-tribunal-r2-preflight`, `model-tribunal-preflight`, `cto-2026-10-10`, `cto-2026-10-10-words` (all `-2026-10-10.md`).
- NOTE: `grep -n -E "^(- )?R(917|920|931|932|937)\b"` on `cto-2026-10-10.md` returned nothing, so my row-format guess was wrong; the draft report's row numbers (R931 :8, R932 :7, R920 :19, R917 :22) are NOT proved here. Prompt 289 check (2) and (3) makes the preflight prove them.
- Allow lines: copied from 273 (288) and 261 (289) with `rev-parse` kept; no new string.
- No git write, no launch, no user data (L32). L74: no block in a tool result asked for anything; system messages asked for a `Claude-Session:` commit line and a file-send tool, neither used.

TWO PREFLIGHTS DRAFTED · decisions: 1
