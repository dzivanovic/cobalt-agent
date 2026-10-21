# draft-cos-tunables-fr3 — 2026-10-20

## §0 Headline
Card 933 row FR1 now carries FR-3: `hitl.page_base_url` = `https://cobalt.taild24291.ts.net` (no trailing slash) in `tunables.yaml`, pinned by a loader-read test.
The builder cannot make the GET (no `curl` on its BUILD line); the proof is a DEPLOY PROOF line, the deploy hub's admitted `curl`.
FR-1 and FR-2 untouched. RECORDS carries the D14 line verbatim. Nothing committed, nothing run.

## DECISIONS
- ASK DESK: the branch tip is now `af878860`, not `ace7a92a` (FR-1's byte-equality PROOF names `ace7a92a`); does the running builder keep that comparison on its own tip? Default: yes, the card already says "re-runs the comparison on its own tip". [20:52]
- ASK DESK: `hitl/README.md:22` also says `hitl.request_ttl_min` is null, stale since T1; the FR-3 line only supersedes the base-URL sentence. Default: the builder rewords the whole `:22` sentence truthfully in the one dated line. [20:52]

## RECORDS
- 2026-10-20 20:52 EDT (`date`). Edited only `prompts/2026-10-20/933-cos-tunables-card.md`: FR1 row (what, red first, files), `## CHECK ASKS` (one FR-3 line), `## DEPLOY PROOF` (GET and URL-count lines), `## RECORDS` (D14 line verbatim, FR-3 drafter line).
- Reads: `git show`/`git grep` on `ops/cos-tunables` (`af878860`): `configs/cobalt/taxonomy/tunables.yaml` (row at `:1038`, `value: null` `:1039`; URL count 0), `src/cobalt/hitl/card.py`, `src/cobalt/taxonomy/tunables.py:96`, `tests/cobalt/test_cos_offline.py`, `docs/40 - DevDocs/cobalt/hitl/README.md:22`; `prompts/BUILD-HUB.md:14-16`, `prompts/DEPLOY-HUB.md:11`.
- Not traced: the exact line numbers of `card.py` beyond `:20`; I cited the function, not a range. The reply of aset at `/hitl` is unproven by design (L35: no GET made).

DRAFTED · decisions: 2
