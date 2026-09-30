# C4 check `27` re-issue — the copy strings (R85)

Designed by the CTO desk `9ae345c8`, 2026-09-29 14:53 ET. NOT placed in any file until he approves.

## WHY
`27` `0bf02e14` staged Grok's copies by Read → Write. At 13:46 a safety classifier stopped the Write of `S3-EXITS-v3-2026-09-22.md.part3`; no checker ran (R84). R85 (B): the remaining copies are made by `cp`, so no model retypes a document. Four copies were still owed: v3 (its tail), LAWS.md, the C3 build report and the C3 fix r1 build report. Each is copied WHOLE; the v3 parts 1–2 already staged are superseded by the whole copy.

## THE STRINGS
Four exact allow strings, one per file, added to `27`'s launch line; each run once, bare, its own call. Single quotes only, so each survives the double-quoted `--allowedTools` argument.

1. `Bash(cp '/Users/cobalt/cobalt/docs/30 - Design/S3-EXITS-v3-2026-09-22.md' /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/s3-exits-c4/files/S3-EXITS-v3-2026-09-22.md)`
2. `Bash(cp '/Users/cobalt/Vault/Think/6 - Permanent/Memory/LAWS.md' /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/s3-exits-c4/files/LAWS.md)`
3. `Bash(cp '/Users/cobalt/cobalt-wt/s3-exits-c3/docs/40 - DevDocs/reports/s3-exits-c3-build-2026-09-28.md' /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/s3-exits-c4/files/s3-exits-c3-build-2026-09-28.md)`
4. `Bash(cp '/Users/cobalt/cobalt-wt/s3-exits-c3/docs/40 - DevDocs/reports/s3-exits-c3-fix-r1-build-2026-09-29.md' /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/s3-exits-c4/files/s3-exits-c3-fix-r1-build-2026-09-29.md)`

## SHAPE
- Reads: one committed doc, the law file, two committed build reports. Writes: one new file each, inside `27`'s own scratch folder in `agy-trial`.
- Never touches `.env`, a credential, the vault's write path, `cobalt_dev`, git or the network. No wildcard, so no other source or target matches.
- Proof per copy: `wc -c` of the copy equals the original's (the `wc *` string already on the line).
