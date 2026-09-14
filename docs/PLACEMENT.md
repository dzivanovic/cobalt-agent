# PLACEMENT.md — where a new docs/ artifact goes

Dated 2026-09-13, Dejan ruled (tree cleanup). Enforced by `cobalt validate`
(the placement sweep in `src/cobalt/placement/check.py`). Every new
markdown artifact under `docs/` files into one of these — never at repo
root, never in a new ad-hoc folder (CLAUDE.md's Documentation standard).
The four D6 tiers this cleanup did not touch — `10 - Decisions/`,
`20 - Assessment/`, `30 - Design/`, `50 - Roles/` — stay governed by
CLAUDE.md's Documentation standard and are out of scope of this map; the
placement sweep allows their existing content through unchanged.

- **Plans** — working plans and briefs (any stage, any author) live in
  `docs/40 - DevDocs/plans/`; `PLAN-TEMPLATE.md` there carries the
  standing DEPLOY WINDOW header every new plan starts from.
- **Reports** — finished, delivered reports live in
  `docs/40 - DevDocs/reports/`, flat, one file per report.
- **Incidents** — incident forensics and post-incident artifact sets live
  in `docs/40 - DevDocs/incidents/<dated-slug>/`, one directory per
  incident.
  (`docs/40 - DevDocs/` also carries the per-.py-file DevDocs wiki proper —
  `cobalt/`, `ops/`, `tests/`, `INDEX.md`, loose topic docs — pre-existing,
  CLAUDE.md-governed, unchanged by this map.)
- **`docs/_archive/captures/`** is gitignored — raw reviewer/session
  captures and duplicate-content dumps are preserved on disk (never
  deleted) but never enter git; everything else under `docs/_archive/`
  (renamed/superseded content, the gemini-era vault-side snapshot) stays
  tracked as before.
- **One `_inflight`** — `docs/_inflight/` holds only `README.md` in git;
  a report copied there for pre-merge vault delivery is a local,
  gitignored artifact removed the moment the report lands in
  `40 - DevDocs/reports/` at merge (the validator allows more only under
  `COBALT_INFLIGHT_OK=1`, for that in-flight window).
- **`docs/60 - Agent Output/`** is the old scheduler's live Morning
  Briefing landing folder — out of scope of the D6 tiers, never a
  documentation tier, stays gitignored.
- **Inbox-as-drop** — `docs/0 - Inbox/` (old repo-side scheduler drop) and
  the vault's own `Think/0 - Inbox/` are transient landing zones, not
  storage: sort or archive what lands there, then the directory goes back
  to empty (or to only its live in-progress drop subdirectories).
- **`docs/00 - Project/` is record-only** — canonically
  `PROJECT-LEDGER.md`, `BACKLOG.md`, `COBALT-REQUIREMENTS.md`,
  `README.md` (CLAUDE.md's Documentation standard, pre-existing law),
  plus this cleanup's additions: `MVP-CHARTER*`, `SPRINT-LADDER*`, a
  `TRIAGE` pointer file, dated ledger-appendix files, and dated
  `INCIDENT-*-notes.md` project-level incident records. No captures, no
  plans, no per-session dumps.
- **`docs/90 - References/`** is untracked working material — only
  `INDEX.md` is committed; everything else stays on disk, gitignored.

See `docs/40 - DevDocs/reports/` for the tree-cleanup session report
(also mirrored to `Think/0 - Inbox/tree-cleanup-2026-09-13/report.md`
until it lands in `40 - DevDocs/reports/`).
