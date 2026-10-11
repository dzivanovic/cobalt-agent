# SDK spike live draft 2026-10-11

## §0 Headline
- Live spike prompt written: `prompts/2026-10-11/330-sdk-spike-live.md`, in the shape of 225, with the brain's fixed seat, allow and deny sets verbatim.
- The PARTIAL report names no SDK package or version, so `«PIN»` is left in the allow line; the launcher refuses it until the desk fills it.
- Report path is the scratch dir (no write path under `docs/`); the desk copies it. Recorded in the prompt's `## DECISIONS`.

## DECISIONS
- ASK DESK: SDK package version to pin [11 Oct 2026]. Default: none; the prompt carries `claude-agent-sdk==«PIN»` and the launcher refuses until filled. The package name `claude-agent-sdk` is also my assumption (neither the spike report nor the repo names it): confirm it when filling.
- Noted, not asked: the launch line `cd`s to the scratch dir (the desk creates it before launch; the seat has no mkdir). Everything else is the brain's list, nothing added.

## RECORDS
- Read: `prompts/2026-10-10/225-sdk-spike.md:1-5`; `reports/sdk-spike-2026-10-10.md:1-37` (no package or version named; U1-U5 at :20-24); `docs/30 - Design/kashef-mining-memo.md:24-28`; `reports/cto-2026-10-10.md:153`; `reports/cto-2026-10-11.md:9`; vault `LAWS.md:39,51,73,80,84` (index lines for L29, L41, L63, L70, L74).
- Grep of `docs/` for `claude-agent-sdk|claude_agent_sdk|claude-code-sdk`: no match.
- Written: `prompts/2026-10-11/330-sdk-spike-live.md`; this report. No launch, no git write.

SDK SPIKE LIVE DRAFTED · decisions: 1
