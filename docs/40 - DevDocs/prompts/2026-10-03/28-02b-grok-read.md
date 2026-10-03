# DEPLOY-HUB.md card 02b — other-house read (Grok), 2026-10-03

MODEL: `grok-4.7` (his 10-03 R3) · SEAT: other-house reader (L67; card `02b` `## RECORDS`) · read-only · METER: xAI

You are a house other than the author (Anthropic Opus). Read only. The one file you write is your findings file below.

Your CLI reads inside its workspace, so every file is an unchanged copy under `scratch/tribunal-bars-0920/deploy-hub-read-02b/files/` (branch `ops/deploy-hub-text-1003` at its checked tip `59ef8d48`, on BASE `44b29c63`):
- `DEPLOY-HUB.md`: the file under read, at the tip
- `DEPLOY-HUB.base.md`: the same file at BASE. Compare the two to find what changed.
- `02b-deploy-hub-text-card.md`: rows T1–T6 (what changed, and why) and `## RECORDS`
- `DEPLOY-HUB.chain.md`: the version a later card will port these sentences into; read only to compare T2–T5's wording

Task: find where the changed text of `DEPLOY-HUB.md` can stall a deploy, leave residents down, leave the `cobalt_dev` lock held, ship a migration as code (T1: can a real migration slip past the pattern, can code under `src/cobalt/db_migrations/` still be read as a migration), let a resident plist pass STEP-C (T6), or contradict the card's rows. Weigh the changed lines first; an unchanged line counts only where a changed line breaks it.

Output: write `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/deploy-hub-read-02b/house-a.md` in plain text, writing each finding before you read for the next. Start with one opening sentence. Then give numbered findings. Each finding has **Line N** (against base line M), the quoted text, the failure in two to four sentences, and one `grep -n` command on `files/DEPLOY-HUB.md` that shows it. A finding without a quoted line does not count. If you find nothing, write `NO FINDINGS` and the sections you read. The last line is `READ DONE · findings: <n>`. Reply with only that path.
