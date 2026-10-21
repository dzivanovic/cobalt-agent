## §0 Headline
Card 933 amended in place: the DEFAULT comments on `cos.poll_interval_s` and `hitl.request_ttl_min` are replaced by `# source: Dejan 2026-10-20 (brain relay)` everywhere the card instructs the builder.
Markers aligned to 0 (X1, FR-3, DEPLOY PROOF count and marker note, FR1 row sentence). The proof line reads `before 0 · after 0`.
Nothing run, nothing committed.

## DECISIONS
1. DEPLOY PROOF `before`: `0`. BASE `e69d5ab8` holds no such line (`git grep -c` returned no match); `ops/cos-tunables` (`af878860`) holds 2, so the after-build target is 0.
2. Header lines 15-16 keep the `DEFAULT <key>: <n>` prefix (the key/value anchor) but now name his word (R2237, R2239) and the source comment.
3. Left untouched: the Scope paragraph's "the brain's DEFAULTS … written as defaults" and the RECORDS line "Values: … defaults to him, not rulings". They state history, not a builder instruction for the comment. ASK DESK: reword them too? One line each.
4. The FR1 row and the prompt-954 record still spell the old comment string, as the thing being replaced / as history; neither instructs writing it.

## RECORDS
- 2026-10-20 21:01 EDT (`date`).
- Read: prompt 955; card 933 whole; `git grep -c -F "DEFAULT (brain; his word may change it)"` on `ops/cos-tunables` → 2 and on `e69d5ab8` → 0; `git rev-parse --short=8 ops/cos-tunables` → `af878860`; `grep -n -F` of the string in the card after the edit.
- Edited: card header lines 15-16, T1, X1, FR-3 check, DEPLOY PROOF count and marker note, FR1 marker sentence; RECORDS gained the verbatim line and a read record. Nothing run, nothing committed.

DRAFTED · decisions: 4
