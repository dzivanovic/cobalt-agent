# _archive

Superseded or misfiled versioned-docs content, kept for history —
**nothing under `docs/` is ever deleted**, per the D6 documentation
standard (`CLAUDE.md`). Organized by why it's here, not dumped flat.

## `references-misfiled-duplicates/`

`ASSESSMENT.md` and `08-documentation-audit.md` — stray copies that had
been dropped directly into `docs/references/` (now `90 - References/`)
alongside the actual reference material. Misfiled duplicates, not
references; the canonical, current versions are
`docs/20 - Assessment/ASSESSMENT.md` and
`docs/20 - Assessment/08-documentation-audit.md`. Moved here as-is
(2026-08-26 D6 restructure), content unedited.

## `gemini-era/`

106 files — every `Morning_Briefing_*`, `Briefing_*`, `AutoNote_*`, and
`Daily_Log_*` note from `docs/0 - Inbox/` (now `docs/60 - Agent
Output/`, renamed 2026-08-31 — see `CLAUDE.md`'s Environment facts).
These are the old Gemini-era scheduler's daily output, not
versioned-docs content; archived here so `60 - Agent Output/` holds
only what the (still-running) scheduler might write next, plus a
handful of items that don't match those four prefixes and were left in
place (`2026-08-25.md`, `Split_Brain_Summary.md`,
`elite-finviz-com-api-explanation_files/`). Content unedited, moved
as-is.

---

Scope note: this restructure covers only already-versioned engineering
artifacts. `docs/60 - Agent Output/` (still gitignored — it's the old
scheduler's live briefing landing folder, D6-numbered 2026-08-31 for
naming-collision reasons only, not promoted to a documentation tier)
and `docs/0 - Projects/` (the gitignored playground vault —
live/uncertain prod surfaces) are otherwise untouched and do not appear
here beyond the one dated cleanup above; see `CLAUDE.md`'s strangler
rules.

## Email channel, retired 2026-09-14 — not archived here

The F18 second alert channel — email over Layer-B Google OAuth, built at
S1-P4 (2026-09-08) — retired by Dejan's ruling of 2026-09-14 and removed
from the new core on 2026-09-15 (ops/2026-09-15). Google's Publish step
for the `gmail.send` scope is gated on restricted-scope verification, so
the OAuth client stayed in Testing and its refresh token expired every
seven days. Ruled 2026-09-15: **source code is never archived under
`docs/`** — git history keeps it. `src/cobalt/notify/email.py`,
`store.py`, `cli.py`, `tests/cobalt/test_notify_email.py` and the
DevDocs `notify/cli.md`, `email.md`, `store.md` are all readable at
`0ed37f5` (`git show 0ed37f5:<path>`). The
`cobalt_email_sends` migration stays at
`src/cobalt/notify/migrations/0001_cobalt_email_sends.sql` because the
table still exists; dropping it is a separate HITL.
