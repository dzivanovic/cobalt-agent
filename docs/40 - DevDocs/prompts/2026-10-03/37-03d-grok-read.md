# DEPLOY-HUB.md card 03d — other-house READ (Grok), 2026-10-04

MODEL: `grok-4.7` (his 10-03 R3) · SEAT: other-house reader (L67; card `03d` `## RECORDS`) · read-only · METER: xAI

You are a house other than the author (Anthropic Opus). Read only. The one file you write is your findings file below.

Your CLI reads inside its workspace, so every file is an unchanged copy under `scratch/tribunal-bars-0920/deploy-hub-read-03d/files/` (branch `ops/adoption-port-1003` at its checked tip `5ff16b1f`, on BASE `a8d8a848` = main):
- `DEPLOY-HUB.md`: the file under read, at the tip
- `DEPLOY-HUB.base.md`: the same file at BASE. Compare the two to find what changed: the adoption chain's sentences (STEP-G, P1 (v), LAUNCH, THE RELEASE) ported onto main's text, plus four ruled sentences (card P2 items 5–8).
- `03d-adoption-port-card.md`: rows P1–P3 and `## RECORDS` (two judge readings are recorded there; an item they settle is not a finding)
- `gate.sh`: the gate whose exits STEP-G reads

Task: find where the changed text lets a deploy hub merge or deploy on a red gate, leave the `cobalt_dev` lock or a `.env` behind, skip the whole gate when the equal-tree clause does not hold, open a restart window outside (i)–(iv) without the STEP-R re-read, drop a sentence main had (P7, STEP-T, STEP-C) or stall a deploy. An unchanged line counts only where a changed line breaks it. A finding that only makes a FAILED line louder than needed is not a hold.

Output: write `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/deploy-hub-read-03d/house-a.md` in plain text, writing each finding before you read for the next. Start with one opening sentence. Then give numbered findings. Each finding has **Line N** (against base line M), the quoted text, the failure in two to four sentences, and one `grep -n` command on `files/DEPLOY-HUB.md` that shows it. A finding without a quoted line does not count. If you find nothing, write `NO FINDINGS` and the sections you read. The last line is `READ DONE · findings: <n>`. Reply with only that path.
