## §0 Headline
- Cards 162 and 164: `REPORT:` header line now holds the worktree path.
- Rule proven at `desk-launch.sh:901-904` and `CARD.md:19`.
- No other main-checkout `reports/` path in a header line of either card; three body mentions stay.
- Nothing else edited; `BASE`, `TIP` untouched.

## CHANGES
| card | line | before | after |
|---|---|---|---|
| `prompts/2026-10-09/162-guard-d1-card.md` | 7 | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/guard-d1-build-2026-10-09.md` | `/Users/cobalt/cobalt-wt/guard-d1-1009/docs/40 - DevDocs/reports/guard-d1-build-2026-10-09.md` |
| `prompts/2026-10-09/164-stop-guard-g7-card.md` | 7 | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/stop-guard-g7-build-2026-10-09.md` | `/Users/cobalt/cobalt-wt/stop-guard-g7-1009/docs/40 - DevDocs/reports/stop-guard-g7-build-2026-10-09.md` |

## DECISIONS
1. Body mentions left as is: 162 lines 34-35, 164 line 31 (read-source references, not header lines).
2. Preflight files not edited (the prompt scopes edits to the two cards and this report).

## RECORDS
- `/Users/cobalt/.claude/ops/desk-launch.sh:901-904`: `build` kind accepts `REPORT` only as `$WT/$wt/docs/40 - DevDocs/reports/*.md`, else refuses "incomplete card".
- `docs/40 - DevDocs/prompts/CARD.md:19`: build / check `REPORT` is the BUILD report, absolute path inside the worktree.
- Cards 162 and 164 lines 1-14: `WORKTREE` is `guard-d1-1009` and `stop-guard-g7-1009`; matches the new paths.
- grep `docs/40 - DevDocs/reports/` over both cards: 162 lines 7, 34, 35; 164 lines 7, 31. Only line 7 is a header line.
- grep `^REPORT:` after the edit: both lines hold the worktree path.

REPORT PATH AMENDED · decisions: 2
