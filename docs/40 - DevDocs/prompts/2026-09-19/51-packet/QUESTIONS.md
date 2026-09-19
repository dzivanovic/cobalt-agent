# QUESTIONS — house check of DEPLOY 3's build (the rebase resolutions + the three fix chunks)

This code ships to production TONIGHT if you clear it. It rebases two branches onto a `main` that now carries S2-P4, resolves a 9-file migration-registry conflict, rewrites six enumeration tests, folds two database read methods into one, and changes WHEN a paid data source may be contacted. Read it as the last thing between it and the live database.

`commits.txt` + `fixes.diff` = the four fix commits in full. `registry-after.py` = the merged migration registry. `rebase-report.md` = the build's own account: every conflict resolution file by file, and the three chunks' sections.

**Q1 — the nine conflict resolutions.** The report's §3 states, per file, what each side had and what was kept, under five fixed rules (union in numeric order; never a choice between sides; never delete a test). For each of the nine: is the stated resolution what the tree actually contains — go read the real files in `/Users/cobalt/cobalt-wt/archiver-append/` — and did it silently drop a hunk from either side? Name any hunk present on one side and absent now.

**Q2 — the merged registry.** `registry-after.py`: is `FORWARD` exactly 0001…0011 with no gap, no duplicate and no reordering, and is `REVERSE` its exact mirror? Does every file it names exist on disk, with a matching `.rollback.sql`? Would `--rollback --down-to 0009` reverse exactly 0011 and 0010, and `--down-to 0007` exactly 0011, 0010, 0009, 0008 — in that order?

**Q3 — the six rewritten pins.** Each asserted "the registry ends with exactly MY two migrations". They were rewritten to assert the united registry. For each: does it still protect the invariant it was written for, or was it weakened into a test that would pass on a broken registry? A pin that now asserts less than it used to is a finding, and so is one that was deleted.

**Q4 — the L3 fold.** `bars_between()` and `_bars_in_range` were folded into one range-read method. Do all previous callers still get the same rows, the same ordering and the same connection behaviour? The archiver's own-connection guarantee is pinned by three offline tests — are they still pinning it, on the surviving method?

**Q5 — R34 "B", the one Dejan ruled.** `radar.finviz_max_rpm` must still be **50** everywhere (the build grep-proved it; verify independently). The archiver's backfill must now (a) declare a demand window instead of `window=None`, and (b) actually refuse to run inside 04:00–09:30 ET — a declared window the runner does not enforce is a lie to the demand model. Is both halves present? Is the nightly 20:30 `full` run genuinely untouched? Did anything else's cadence, window or rate move?

**Q6 — what would break in production.** The archiver writes bars nightly and the radar polls Finviz all morning. Ignore the tests for a moment and ask what this diff does to a live 20:30 archiver run, a live 04:00 premarket radar, and a Monday 21:10 replay. Anything that changes what the archiver WRITES — rather than when it runs — is a BLOCKER; this build is supposed to ship in `upsert` mode, today's behaviour byte for byte.

**Q7 — anything else you would not ship**, severity BLOCKER / MAJOR / MINOR, one-line fix each.

**Not your business, and not findings:** the `append`-mode switch (his ruling, on shadow numbers, never this build), C the cadence stagger (queued by R34, not tonight), the §11 "follows 0006's pattern" wording (open ruling R3-1), and that a backfill is now refused during most scheduled hours (the build escalated it; it is Dejan's, not a defect).

Your verdict line: `VERDICT: SAFE TO DEPLOY` or `VERDICT: FIX FIRST <numbers>` or `VERDICT: DO NOT DEPLOY <numbers>`.
