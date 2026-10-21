## §0 Headline
- Card 933 FR1 part FR-3 amended in place (one sentence, `933-cos-tunables-card.md:27`): `cos.poll_interval_s` and `hitl.request_ttl_min` get `# source: Dejan 2026-10-20 (brain relay)`.
- Placement: no `# source:` comment exists on `ops/cos-tunables`; the sentence puts it on each `value:` line, in the place of the `# DEFAULT (brain; his word may change it)` comment.
- That breaks the card's DEPLOY PROOF marker 2 (after `2`) and check line FR-3 (still 2 DEFAULT lines): ASK DESK 1.
- Two verbatim RECORDS lines added plus my read record. No tests line. Nothing run, nothing committed.

## DECISIONS
- ASK DESK 1: the two DEFAULT comments are the only comment on those value lines. Replacing them makes `grep -c -F "DEFAULT (brain; his word may change it)"` after `0`, not `2`. Card lines to change if so: `## DEPLOY PROOF` line 57 and the marker-2 paragraph (line 59), check row FR-3 (line 53), and the sentence "marker 2 still counts exactly 2" in FR-3. I left them untouched (scope: one sentence). The alternative is to keep DEFAULT and add the source comment after it; say which.

## RECORDS
- 2026-10-20 20:57 EDT (`date`). `git rev-parse --short=8 ops/cos-tunables` → `af878860`.
- Read: `git grep` on `ops/cos-tunables` of `configs/cobalt/taxonomy/tunables.yaml:1008-1015, 1026-1033, 1035-1046`; same file `# source` grep → no match; the card (FR1 row, `:50-60`, `:63-75`); `areas/cobalt.md`.
- Edited only `docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md`.

DRAFTED · decisions: 1
