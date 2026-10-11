# SDK spike live — brain decisions 2026-10-11

On `reports/sdk-spike-live-2026-10-11.md` (`## §0`, `## ANSWERS`, `## UNKNOWN`, `## DECISIONS`). Brain: the successor of `3d24c7e5`, on handover 349.

## §0 Headline
- D1, D3–D9 are KEEP. They become inputs to the F20 card drafter, byte for byte from the spike report's ANSWERS rows Q1, Q4 and U5.
- D2 (Q3: subscription or API key for unattended runs) goes to Dejan. It is a terms-of-service reading, not a build call. F20's DESIGN and BUILD do not wait for it: auth is a config switch (D2's default). Only F20's first UNATTENDED run in production waits for his word.
- D10 is a follow-up plan row, not blocking. Two more follow-up rows come from UNKNOWN U6 and U7, for the F20 card.

## PER ITEM
| # | Ruling | Reason |
|---|---|---|
| D1 | KEEP | Done; the desk copied the report. |
| D2 | FOR DEJAN (rec.: subscription for his single-user use, auth a config switch; he may say API key) | Anthropic's terms allow Pro/Max Agent SDK use for "ordinary, individual usage" and steer "developers building products" to API keys. Which side Cobalt's unattended CoS falls on is his reading, and money (an API key bills per token). The config switch means either answer costs config, not code. |
| D3 | KEEP | HITL as proven live: a `PreToolUse` hook per risky tool, `can_use_tool` deny-by-default, `allowed_tools` path rules for jailed reads, `HookMatcher.timeout` ≥ card TTL, and Cobalt's own card ledger. |
| D4 | KEEP | `setting_sources=[]` plus `strict_mcp_config=True`. Without them, connector tools entered the jailed session. This is a binding F20 card row. |
| D5 | KEEP | Fail on `is_error`/`terminal_reason`, never `subtype` alone. Own watchdog per session (L18). Kill the process group on teardown. Store `session_id` per task row. |
| D6 | KEEP for the spike only | Haiku spared his quota on a probe. F20's own sessions follow the model rules (R1008: nothing below Sonnet builds). The spike's Haiku is no precedent for F20. |
| D7 | KEEP | Test values only. |
| D8 | KEEP | His OAuth bearer never went to localhost: right. |
| D9 | KEEP | SPIKE-HUB's scratch dir holds over the base prompt's worktree line. |
| D10 | FOLLOW-UP row (plan) | Re-spike U2b/U9 (LiteLLM proxy started by a launched seat, plus the two-session test) after the F20 design; it does not block F20. Starting a proxy is a new command class for that seat: his word at launch. |

## FOLLOW-UP ROWS FOR THE F20 CARD DRAFTER (from UNKNOWN; row text, the brain writes no card)
- U6: "The F20 runner denies the `Agent` tool (no subagents) and treats parallel tool calls in one turn as unproven: a red test proves each risky call in a parallel turn still posts its own card, or the runner sets parallel tool use off."
- U7: "The card TTL is at most 300 s (the proven wait). A longer human absence ends the session by refusal, and it resumes later by `session_id` (Q4), never by a hook waiting hours."

## FOR THE CHECK
`SDK spike live 2026-10-11 brain: D1 D3-D9 KEEP (F20 card inputs); D2 to Dejan, F20 design/build not held, first unattended prod run waits for his word; D10 + U6 + U7 follow-up rows`
