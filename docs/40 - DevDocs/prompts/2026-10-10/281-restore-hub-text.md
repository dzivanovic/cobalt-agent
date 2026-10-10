MODEL: Sonnet 5.5 · SEAT: mechanical drafter · SESSION: fresh · mode: auto · METER: Anthropic
LAUNCH: `sh /Users/cobalt/.claude/ops/desk-launch.sh prompt "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/281-restore-hub-text.md"`

# Restore two hub files to HEAD (brain R932, L79)

Read [[writing-rules]] is not needed. Task, nothing else:

1. Two files in `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/` are dirty in main with an unapproved `--kill` text: `DEPLOY-HUB.md` (4 lines) and `STANDING-LIST.md` (1 line). The drafted text is already saved in `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/standing-list-kill-row-2026-10-10.md`; do not touch that file.
2. Read `git -C /Users/cobalt/cobalt diff -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md" "docs/40 - DevDocs/prompts/STANDING-LIST.md"`. With the Edit tool only, undo exactly those added or changed lines so each file equals `git show HEAD:<path>`. Use `git show` to read HEAD text where needed. No `git checkout`, `git restore`, `git stash`, `git reset`, no Write of a whole file, no commit.
3. Done when `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md" "docs/40 - DevDocs/prompts/STANDING-LIST.md"` prints nothing.
4. Write `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/restore-hub-text-2026-10-10.md` (≤5 lines: what you undid, the empty diff proof) whose last non-blank line is `RESTORED` or `FAILED: <reason>`.
