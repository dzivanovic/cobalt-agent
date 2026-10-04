# DEPLOY-HUB.md card 02b — other-house RE-READ (Grok), 2026-10-03

MODEL: `grok-4.7` (his 10-03 R3) · SEAT: other-house reader (L67; card `02b` `## RECORDS`) · read-only · METER: xAI

You are a house other than the author (Anthropic Opus). Read only. The one file you write is your findings file below.

Your CLI reads inside its workspace, so every file is an unchanged copy under `scratch/tribunal-bars-0920/deploy-hub-read-02b-r2/files/` (branch `ops/deploy-hub-text-1003` at its checked tip `2cc6330e`, on BASE `44b29c63`):
- `DEPLOY-HUB.md`: the file under read, at the tip
- `DEPLOY-HUB.base.md`: the same file at BASE. Compare the two to find what changed; the change is limited to P7, STEP-T and STEP-C.
- `02b-deploy-hub-text-card.md`: rows T1, T6, C1 and `## RECORDS`
- `jobs.yaml`: the registry STEP-C's sentence reads (labels are `label:` values)

This is a re-read after your first read's 8 findings were fixed (1–4) or cut from this card (5–8). Task: find where the changed P7, STEP-T or STEP-C text lets a real migration ship as code, reads code as a migration, misses a FORWARD registration in STEP-T, lets a resident plist pass STEP-C, or stalls a deploy. An unchanged line counts only where a changed line breaks it.

Output: write `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/deploy-hub-read-02b-r2/house-a.md` in plain text, writing each finding before you read for the next. Start with one opening sentence. Then give numbered findings. Each finding has **Line N** (against base line M), the quoted text, the failure in two to four sentences, and one `grep -n` command on `files/DEPLOY-HUB.md` that shows it. A finding without a quoted line does not count. If you find nothing, write `NO FINDINGS` and the sections you read. The last line is `READ DONE · findings: <n>`. Reply with only that path.
