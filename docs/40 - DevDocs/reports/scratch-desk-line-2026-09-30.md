# Scratch desk line proof — 2026-09-30

## §0 Headline
A1 denied · A2 denied · A3 allowed. B1–B4 all ran (no permission refusals).
The narrowed desk line holds both deny rules and the four allow matches.

## PROOFS

| Step | Probe | Result |
|---|---|---|
| 1 | `date` | ran: `Wed Sep 30 16:38:04 EDT 2026` |
| A1 | Write `/Users/cobalt/cobalt/.git/scratch-probe-0930.txt` | DENIED: `File is in a directory that is denied by your permission settings.` |
| A2 | Write `/Users/cobalt/.claude/scratch-probe-0930.txt` | DENIED: `File is in a directory that is denied by your permission settings.` |
| A3 (control) | Write `docs/40 - DevDocs/reports/scratch-probe-0930.txt` | allowed: `File created successfully at: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/scratch-probe-0930.txt` |
| B1 | `sh /Users/cobalt/.claude/ops/desk-list.sh` | ran (exit 0): `6c4622c5 · cto-desk · ~/cobalt · busy · working` |
| B2 | `herdr tab list` | ran (exit 0): `{"id":"cli:tab:list","result":{"tabs":[{"agent_status":"idle",...` |
| B3 | `claude stop scratch-probe-no-such-id` | ran (exit 1): `No job matching 'scratch-probe-no-such-id'. Run 'claude agents' to list running sessions.` (PASS: match, not a permission refusal) |
| B4 | `claude rm scratch-probe-no-such-id` | ran (exit 1): `No job matching 'scratch-probe-no-such-id'` (PASS) |

## RECORDS
- A3 left `docs/40 - DevDocs/reports/scratch-probe-0930.txt` on disk (the step's own output; not removed, per "follow exactly").
- Neither `.git/scratch-probe-0930.txt` nor `.claude/scratch-probe-0930.txt` was created: both writes were refused.
- A2 and A3 were issued in one parallel batch (A1 alone first); no result depended on order.

SCRATCH PROOF DONE · A1 denied · A2 denied · A3 allowed · B 4 ran · decisions: 0 · for Dejan: 0
