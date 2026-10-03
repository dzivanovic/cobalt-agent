# DEPLOY-HUB.md — other-house read (Grok), 2026-10-03

MODEL: `grok-4.7` (his 10-03 R3) · SEAT: other-house reader (L67; card `02` `## RECORDS`) · read-only · METER: xAI

You are a house other than the author (Anthropic Opus). Read only; write and run nothing that changes a file.

Files, all inside `/Users/cobalt/cobalt-wt/adoption-scripts-b2-1003` (branch tip `b7eeb80c`, sets `02` + `03c` stacked on BASE `0a4a7743`):
- `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (the file under read)
- `docs/40 - DevDocs/prompts/STANDING-LIST.md` §3
- `docs/40 - DevDocs/prompts/2026-10-03/02-adoption-hubs-card.md` rows A3, A4, A7, A8 (what changed and why)
- `docs/40 - DevDocs/prompts/2026-10-03/03c-adoption-scripts-b-card.md` row M3
- what changed: `git diff 0a4a7743 b7eeb80c -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`

Task: find where `DEPLOY-HUB.md` can stall, leave residents down, leave the `cobalt_dev` lock held, merge an unchecked tree, or let an allow-list string write past its step; and where it contradicts STANDING-LIST §3 or the two cards' rows. Weigh the changed lines first.

Output, plain text, in the shape of `docs/40 - DevDocs/reports/deploy-hub-other-house-read-2026-09-30.md`: one opening sentence; then numbered findings, each with **Line N** (against line M), the quoted text, the failure in two to four sentences, and one `grep -n` command that shows it. No finding without a quoted line. Nothing found → say `NO FINDINGS` and the sections you read. Last line: `READ DONE · findings: <n>`.
