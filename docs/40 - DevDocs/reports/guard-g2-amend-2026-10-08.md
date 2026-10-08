## §0 Headline
Card `120` header `REPORT:` re-pointed to the worktree path the launcher requires.
All other header values compared against `desk-launch.sh` build mode: none else refused.
Only that one line of the card changed.

## CHANGES
Edited `prompts/2026-10-08/120-guard-g2-open-reads-card.md` line 7 only: `REPORT:` is now `/Users/cobalt/cobalt-wt/guard-g2-open-reads-1008/docs/40 - DevDocs/reports/guard-g2-open-reads-build-2026-10-08.md`.

Compared (script requirement → card value):
- JOB: `[a-z0-9-]`, not leading `-` (732) → `guard-g2-open-reads-1008` OK.
- LADDER: non-empty (721) → set OK.
- BRANCH: plain name `[A-Za-z0-9._/-]`, no `..` (735) → `ops/guard-g2-open-reads-1008` OK; no such branch exists and no worktree dir exists, so the worktree is created fresh (909).
- WORKTREE: one dir name, no leading `.`, not `agy-trial` (754-756) → OK.
- BASE: 8 hex and a commit (898-899) → `4125ff02` OK (resolves to 4125ff02c958…).
- REPORT: must start `$WT/$wt/docs/40 - DevDocs/reports/` and end `.md` (901) → was main-checkout path, REFUSED; now fixed.
- TAG: must be empty on build (895) → absent OK.
- RULINGS: `<date> R<n>` (738), row is one line in `cto-2026-10-08.md`, HIS RULING + APPROVED, committed → `2026-10-08 R686` OK (row present at line 39, file clean, committed d0978507).
- TIP, CHECK REPORT, HOUSE A/B: read only by check/deploy kinds (916-931), not by build; empty is fine. HOUSE A/B empty means no overruled row to prove.
- TREE STATE: optional (745), absent OK.
- `## ROWS` section: present (896).
- No «FILL tokens (695).

## DECISIONS
None.

## RECORDS
- Read prompt 130 and card 120 (lines 1-40).
- Read `ops/desk/desk-launch.sh` 166-169, 684-790, 890-931 and the refuse/field grep.
- `git rev-parse` of BASE: commit exists.
- `cto-2026-10-08.md`: R686 row (line 39), `git status` clean, last commit d0978507.
- `refs/heads/ops/guard-g2-open-reads-1008`: absent; `/Users/cobalt/cobalt-wt` has no `guard-g2-open-reads-1008`.
- Owed outside this job: the card edit is uncommitted; the launcher requires the card committed on main (759-761), so the desk must commit it before `build`.

GUARD G2 CARD AMENDED · decisions: 0
