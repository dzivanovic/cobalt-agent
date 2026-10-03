# DEPLOY-HUB.md — other-house read (Grok), 2026-10-03

MODEL: `grok-4.7` (his 10-03 R3) · SEAT: other-house reader (L67; card `02` `## RECORDS`) · read-only · METER: xAI

You are a house other than the author (Anthropic Opus). Read only. The one file you write is your findings file below.

Your CLI reads inside its workspace, so every file is an unchanged copy under `scratch/tribunal-bars-0920/deploy-hub-read-1003/files/` (branch tip `b7eeb80c`, sets `02` + `03c` stacked on BASE `0a4a7743`):
- `DEPLOY-HUB.md`: the file under read, at the tip
- `DEPLOY-HUB.base.md`: the same file at BASE. Compare the two to find what changed.
- `STANDING-LIST.md`: read §3
- `02-adoption-hubs-card.md`: rows A3, A4, A7 and A8 (what changed, and why)
- `03c-adoption-scripts-b-card.md`: row M3
- `shape-2026-09-30.md`: the shape your output follows

Task: find where `DEPLOY-HUB.md` can stall, leave residents down, leave the `cobalt_dev` lock held, merge an unchecked tree, or let an allow-list string write past its step. Also find where it contradicts STANDING-LIST §3 or the two cards' rows. Weigh the changed lines first.

Output: write `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/deploy-hub-read-1003/house-a.md` in plain text, writing each finding before you read for the next. Start with one opening sentence. Then give numbered findings. Each finding has **Line N** (against line M), the quoted text, the failure in two to four sentences, and one `grep -n` command on `files/DEPLOY-HUB.md` that shows it. A finding without a quoted line does not count. If you find nothing, write `NO FINDINGS` and the sections you read. The last line is `READ DONE · findings: <n>`. Reply with only that path.
